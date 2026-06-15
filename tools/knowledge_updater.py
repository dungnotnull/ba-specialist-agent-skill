"""
knowledge_updater.py — Skill 2: ba-specialist
Crawls authoritative BA/RE research sources and appends new entries to SECOND-KNOWLEDGE-BRAIN.md.

Schedule: Weekly (cron or manual trigger)
Dependencies: crawl4ai (optional — graceful fallback to requests), requests, hashlib, datetime, re, pathlib
"""

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────

KNOWLEDGE_BRAIN_PATH = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
SEEN_HASHES_PATH = Path(__file__).parent / ".seen_hashes.json"

RELEVANCE_KEYWORDS = [
    "requirements engineering",
    "user story",
    "stakeholder analysis",
    "requirements elicitation",
    "acceptance criteria",
    "BMAD",
    "agile requirements",
    "backlog",
    "story mapping",
    "MoSCoW",
    "business analysis",
    "BABOK",
    "software requirements",
    "user story quality",
    "requirements specification",
    "gap analysis",
    "non-functional requirements",
    "requirements prioritization",
    "verification and validation",
    "requirements traceability",
]

RECENCY_WEIGHT = 0.4
KEYWORD_WEIGHT = 0.6
MIN_RELEVANCE_SCORE = 0.25
MAX_ENTRIES_PER_RUN = 15
MAX_ENTRIES_PER_SOURCE = 5

CRAWL_SOURCES = [
    # ArXiv queries (5 required)
    {
        "name": "ArXiv cs.SE — Requirements Engineering",
        "url": "https://arxiv.org/search/?searchtype=all&query=requirements+engineering+agile&start=0",
        "type": "arxiv",
    },
    {
        "name": "ArXiv cs.SE — User Story Quality",
        "url": "https://arxiv.org/search/?searchtype=all&query=user+story+quality+acceptance+criteria&start=0",
        "type": "arxiv",
    },
    {
        "name": "ArXiv cs.SE — Stakeholder Analysis",
        "url": "https://arxiv.org/search/?searchtype=all&query=stakeholder+analysis+requirements&start=0",
        "type": "arxiv",
    },
    {
        "name": "ArXiv cs.SE — Requirements Specification & Validation",
        "url": "https://arxiv.org/search/?searchtype=all&query=software+requirements+specification+validation&start=0",
        "type": "arxiv",
    },
    {
        "name": "ArXiv cs.SE — Non-Functional Requirements & Quality Attributes",
        "url": "https://arxiv.org/search/?searchtype=all&query=non+functional+requirements+quality+attributes&start=0",
        "type": "arxiv",
    },
    # Web sources (4 required)
    {
        "name": "Agile Alliance — User Stories",
        "url": "https://www.agilealliance.org/glossary/user-stories/",
        "type": "web",
    },
    {
        "name": "Mountain Goat Software Blog",
        "url": "https://www.mountaingoatsoftware.com/blog",
        "type": "web",
    },
    {
        "name": "IIBA — Business Analysis Resources",
        "url": "https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/",
        "type": "web",
    },
    {
        "name": "IEEE — Requirements Engineering Standard",
        "url": "https://standards.ieee.org/ieee/29148/",
        "type": "web",
    },
]

# ─── Utility Functions ──────────────────────────────────────────────────


def load_seen_hashes() -> set:
    """Load previously processed entry hashes to prevent duplicates."""
    if SEEN_HASHES_PATH.exists():
        with open(SEEN_HASHES_PATH, encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_seen_hashes(hashes: set) -> None:
    """Persist processed entry hashes for deduplication."""
    SEEN_HASHES_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SEEN_HASHES_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(hashes), f, indent=2)


def compute_hash(url_or_doi: str) -> str:
    """Generate a SHA-256 hash (truncated) for deduplication by DOI/URL."""
    return hashlib.sha256(url_or_doi.strip().lower().encode()).hexdigest()[:16]


def score_relevance(title: str, abstract: str, pub_year: int) -> float:
    """
    Score an entry's relevance using keyword matching and recency.
    
    Formula: (keyword_weight * keyword_score) + (recency_weight * recency_score)
    keyword_score: fraction of relevant keywords present (capped at 1.0)
    recency_score: 1.0 for current year, decaying over 10 years
    """
    text = f"{title} {abstract}".lower()
    keyword_hits = sum(1 for kw in RELEVANCE_KEYWORDS if kw.lower() in text)
    keyword_score = min(keyword_hits / 5, 1.0)

    current_year = datetime.now().year
    age = max(current_year - pub_year, 0)
    recency_score = max(1.0 - (age / 10), 0.0)

    return round(KEYWORD_WEIGHT * keyword_score + RECENCY_WEIGHT * recency_score, 3)


def format_table_row(
    title: str,
    authors: str,
    year: int,
    venue: str,
    doi_or_url: str,
    relevance_note: str,
    score: float,
    date_added: str,
) -> str:
    """Format a single row for the Key Research Papers table in SECOND-KNOWLEDGE-BRAIN.md."""
    display_title = title[:58] + "..." if len(title) > 60 else title
    display_authors = authors[:28] + "..." if len(authors) > 30 else authors
    display_url = doi_or_url
    display_note = relevance_note[:38] + "..." if len(relevance_note) > 40 else relevance_note
    return (
        f"| {display_title} | {display_authors} | {year} | {venue[:20]} "
        f"| [{display_url}]({doi_or_url}) | {display_note} "
        f"| {score} | {date_added} |"
    )


def extract_year_from_arxiv_id(arxiv_id: str) -> int:
    """
    Extract publication year from ArXiv ID.
    
    ArXiv IDs use format YYMM.NNNNN (post-2007) or arch-ive/YYMMNNN (pre-2007).
    For modern papers, the first two digits represent the year (20XX).
    """
    year_prefix_match = re.match(r"(\d{2})", arxiv_id)
    if year_prefix_match:
        try:
            prefix = int(year_prefix_match.group(1))
            return 2000 + prefix if prefix <= 30 else 1900 + prefix
        except ValueError:
            pass
    return datetime.now().year


# ─── ArXiv Crawler ───────────────────────────────────────────────────────


def crawl_arxiv(source: dict, seen_hashes: set) -> list:
    """
    Crawl ArXiv search results and extract paper metadata.
    
    Uses crawl4ai if available, otherwise falls back to requests + basic HTML parsing.
    Returns a list of entry dicts sorted by relevance score.
    """
    entries = []

    try:
        from crawl4ai import WebCrawler
        use_crawl4ai = True
    except ImportError:
        use_crawl4ai = False

    html = ""
    if use_crawl4ai:
        try:
            crawler = WebCrawler()
            crawler.warmup()
            result = crawler.run(url=source["url"], word_count_threshold=50)
            if result.success:
                html = result.html or ""
            else:
                print(f"  crawl4ai failed for: {source['url']}", file=sys.stderr)
                use_crawl4ai = False
        except Exception as e:
            print(f"  crawl4ai error: {e}", file=sys.stderr)
            use_crawl4ai = False

    if not use_crawl4ai:
        try:
            import requests
            response = requests.get(source["url"], timeout=30, headers={
                "User-Agent": "ba-specialist-knowledge-updater/1.0"
            })
            response.raise_for_status()
            html = response.text
        except Exception as e:
            print(f"  requests fallback failed: {e}", file=sys.stderr)
            return []

    if not html:
        return []

    # Parse ArXiv search result HTML
    paper_blocks = re.findall(r'<li class="arxiv-result".*?</li>', html, re.DOTALL)
    if not paper_blocks:
        # Alternative: try finding arxiv IDs in links
        arxiv_ids = re.findall(r'href="/abs/([\d.]+)"', html)
        titles_raw = re.findall(r'<p class="title[^"]*">(.*?)</p>', html, re.DOTALL)
        authors_raw = re.findall(r'<p class="authors">(.*?)</p>', html, re.DOTALL)
        abstracts_raw = re.findall(r'<span class="abstract-full[^"]*">(.*?)</span>', html, re.DOTALL)

        for i, arxiv_id in enumerate(arxiv_ids[:MAX_ENTRIES_PER_SOURCE]):
            doi_url = f"https://arxiv.org/abs/{arxiv_id}"
            entry_hash = compute_hash(doi_url)
            if entry_hash in seen_hashes:
                continue

            title = re.sub(r'<[^>]+>', '', titles_raw[i]).strip() if i < len(titles_raw) else f"ArXiv Paper {arxiv_id}"
            authors = re.sub(r'<[^>]+>', '', authors_raw[i]).strip() if i < len(authors_raw) else "Unknown"
            abstract = re.sub(r'<[^>]+>', '', abstracts_raw[i]).strip() if i < len(abstracts_raw) else ""
            year = extract_year_from_arxiv_id(arxiv_id)

            score = score_relevance(title, abstract, year)
            if score < MIN_RELEVANCE_SCORE:
                continue

            entries.append({
                "title": title,
                "authors": authors[:50],
                "year": year,
                "venue": "ArXiv cs.SE",
                "doi_url": doi_url,
                "relevance_note": f"Score: {score} — {source['name']}",
                "score": score,
                "hash": entry_hash,
            })
    else:
        for block in paper_blocks[:MAX_ENTRIES_PER_SOURCE]:
            title_m = re.search(r'<p class="title[^"]*">(.*?)</p>', block, re.DOTALL)
            authors_m = re.search(r'<p class="authors">(.*?)</p>', block, re.DOTALL)
            abstract_m = re.search(r'<span class="abstract-full[^"]*">(.*?)</span>', block, re.DOTALL)
            id_m = re.search(r'href="/abs/([\d.]+)"', block)

            if not title_m or not id_m:
                continue

            title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip()
            authors = re.sub(r'<[^>]+>', '', authors_m.group(1)).strip() if authors_m else "Unknown"
            abstract = re.sub(r'<[^>]+>', '', abstract_m.group(1)).strip() if abstract_m else ""
            arxiv_id = id_m.group(1)
            doi_url = f"https://arxiv.org/abs/{arxiv_id}"
            year = extract_year_from_arxiv_id(arxiv_id)

            entry_hash = compute_hash(doi_url)
            if entry_hash in seen_hashes:
                continue

            score = score_relevance(title, abstract, year)
            if score < MIN_RELEVANCE_SCORE:
                continue

            entries.append({
                "title": title,
                "authors": authors[:50],
                "year": year,
                "venue": "ArXiv cs.SE",
                "doi_url": doi_url,
                "relevance_note": f"Score: {score} — {source['name']}",
                "score": score,
                "hash": entry_hash,
            })

    return sorted(entries, key=lambda x: x["score"], reverse=True)[:MAX_ENTRIES_PER_SOURCE]


# ─── Web Crawler ─────────────────────────────────────────────────────────


def crawl_web(source: dict, seen_hashes: set) -> list:
    """
    Crawl a general web page for BA-relevant content.
    
    Uses crawl4ai if available, otherwise falls back to requests.
    Returns a list of entry dicts.
    """
    entries = []
    entry_hash = compute_hash(source["url"])

    if entry_hash in seen_hashes:
        return []

    try:
        from crawl4ai import WebCrawler
        use_crawl4ai = True
    except ImportError:
        use_crawl4ai = False

    html = ""
    if use_crawl4ai:
        try:
            crawler = WebCrawler()
            crawler.warmup()
            result = crawler.run(url=source["url"], word_count_threshold=50)
            if result.success:
                html = result.html or ""
        except Exception:
            use_crawl4ai = False

    if not use_crawl4ai or not html:
        try:
            import requests
            response = requests.get(source["url"], timeout=30, headers={
                "User-Agent": "ba-specialist-knowledge-updater/1.0"
            })
            response.raise_for_status()
            html = response.text
        except Exception as e:
            print(f"  Failed to fetch {source['url']}: {e}", file=sys.stderr)
            return []

    # Extract page title
    title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else source["name"]

    # Extract text content for relevance scoring
    text_content = re.sub(r'<[^>]+>', ' ', html)
    text_content = re.sub(r'\s+', ' ', text_content).strip()[:500]

    score = score_relevance(title, text_content, datetime.now().year)
    if score < MIN_RELEVANCE_SCORE:
        return []

    entries.append({
        "title": title[:60],
        "authors": source["name"],
        "year": datetime.now().year,
        "venue": "Web Resource",
        "doi_url": source["url"],
        "relevance_note": f"Score: {score} — {source['name']}",
        "score": score,
        "hash": entry_hash,
    })

    return entries


# ─── Knowledge Brain Updater ─────────────────────────────────────────────


def append_to_knowledge_brain(entries: list, date_str: str) -> int:
    """
    Append new entries to the Key Research Papers table in SECOND-KNOWLEDGE-BRAIN.md.
    
    Handles both the existing table format and appends new rows.
    Also updates the Knowledge Update Log.
    Returns the number of entries added.
    """
    if not entries:
        return 0

    if not KNOWLEDGE_BRAIN_PATH.exists():
        print(f"Knowledge brain not found: {KNOWLEDGE_BRAIN_PATH}", file=sys.stderr)
        return 0

    content = KNOWLEDGE_BRAIN_PATH.read_text(encoding="utf-8")

    # Build new rows
    new_rows = []
    for entry in entries:
        row = format_table_row(
            entry["title"],
            entry["authors"],
            entry["year"],
            entry["venue"],
            entry["doi_url"],
            entry["relevance_note"],
            entry["score"],
            date_str,
        )
        new_rows.append(row)

    # Find the end of the Key Research Papers table (look for the separator line before next section)
    table_marker = "## Key Research Papers"
    if table_marker in content:
        # Find the table header
        table_start = content.find(table_marker)
        # Find the next section header after the table
        next_section = content.find("\n## ", table_start + len(table_marker))
        if next_section == -1:
            next_section = len(content)

        # Find the last row in the table (last line starting with | before next_section)
        table_content = content[table_start:next_section]
        # Insert new rows before the next section
        insert_pos = table_start + len(table_content)
        new_rows_text = "\n".join(new_rows) + "\n"
        new_content = content[:insert_pos] + new_rows_text + content[insert_pos:]
    else:
        # If the table marker doesn't exist, append at the end
        new_rows_text = "\n".join(new_rows)
        new_content = content + "\n\n## Crawled Entries\n\n" + new_rows_text + "\n"

    # Update the Knowledge Update Log
    log_marker = "## Knowledge Update Log"
    log_entry = f"| {date_str} | Automated crawl | {len(entries)} papers/articles | knowledge_updater.py run |"
    if log_marker in new_content:
        # Find the last row in the log table and insert after it
        log_start = new_content.find(log_marker)
        # Find the table header row after the log marker
        header_end = new_content.find("\n|", log_start + len(log_marker))
        if header_end != -1:
            # Find end of header separator line
            header_end = new_content.find("\n", header_end + 1)
            if header_end != -1:
                new_content = new_content[:header_end + 1] + log_entry + "\n" + new_content[header_end + 1:]
        else:
            new_content = new_content.replace(log_marker, f"{log_marker}\n\n{log_entry}\n", 1)

    KNOWLEDGE_BRAIN_PATH.write_text(new_content, encoding="utf-8")
    return len(entries)


# ─── Main ────────────────────────────────────────────────────────────────


def main() -> None:
    """Run the knowledge updater: crawl sources, deduplicate, score, and append entries."""
    print("=" * 60)
    print("ba-specialist Knowledge Updater")
    print(f"Run date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    seen_hashes = load_seen_hashes()
    all_entries = []
    date_str = datetime.now().strftime("%Y-%m-%d")

    for source in CRAWL_SOURCES:
        print(f"\nCrawling: {source['name']} ...")
        try:
            if source["type"] == "arxiv":
                entries = crawl_arxiv(source, seen_hashes)
            else:
                entries = crawl_web(source, seen_hashes)

            print(f"  Found {len(entries)} new relevant entries")
            all_entries.extend(entries)

        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            continue

    # Sort by relevance score, take top entries
    all_entries.sort(key=lambda x: x["score"], reverse=True)
    top_entries = all_entries[:MAX_ENTRIES_PER_RUN]

    if top_entries:
        added = append_to_knowledge_brain(top_entries, date_str)
        new_hashes = seen_hashes | {e["hash"] for e in top_entries}
        save_seen_hashes(new_hashes)
        print(f"\nDone. {added} entries appended to SECOND-KNOWLEDGE-BRAIN.md")
    else:
        print("\nNo new relevant entries found.")

    print("=" * 60)


if __name__ == "__main__":
    main()
