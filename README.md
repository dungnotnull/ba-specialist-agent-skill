# 🧠 BA Specialist — Business Analysis Agent Skill

> **Transform vague ideas into airtight software requirements — the BMAD way.**

[![Phase](https://img.shields.io/badge/Phase-5%20Complete-brightgreen)]()
[![Skill Type](https://img.shields.io/badge/Skill-Agent%20Harness-blue)]()
[![Cluster](https://img.shields.io/badge/Cluster-A%20Professional-purple)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Problem It Solves](#-problem-it-solves)
- [Architecture](#-architecture)
- [Harness Flow](#-harness-flow)
- [Sub-Skills](#-sub-skills)
- [Quality Gates](#-quality-gates)
- [Knowledge Pipeline](#-knowledge-pipeline)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Test Scenarios](#-test-scenarios)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**BA Specialist** is a production-grade agent skill that transforms any project brief into a comprehensive Business Analysis specification. Inspired by the **BMAD methodology** (Business, Management, Architecture, Development) and grounded in **IEEE 29148**, **IIBA BABOK v3**, and **Agile story mapping** practices, it guides an AI agent through six structured stages:

`
Brief Intake → Stakeholder Mapping → Requirements Elicitation → Persona & Story Mapping → Gap Analysis → Quality Gate → Specification Document
`

The result is a professional BA deliverable containing stakeholder registers, prioritized user stories with acceptance criteria, gap analysis, and a complete specification document ready for development teams.

---

## 🔥 Problem It Solves

Most software projects fail not from bad code, but from **bad requirements**. Ambiguous briefs, missed stakeholders, untested assumptions, and inconsistent user stories cascade into rework, scope creep, and delivery failures.

| Without BA Specialist | With BA Specialist |
|---|---|
| ❌ Vague "the system should be fast" | ✅ NFR-001: P95 response time < 3s on 4G |
| ❌ "As a user, I want a good experience" | ✅ As Maya (Ops Manager), I want to filter orders by status, so that I can quickly identify orders needing action |
| ❌ 47 Must-Have stories in the backlog | ✅ MoSCoW prioritization with ≤ 60% Must-Have |
| ❌ Contradictory requirements slip through | ✅ 5 contradiction detection heuristics catch conflicts |
| ❌ No traceability from stakeholder to story | ✅ Every story linked to FR/NFR and stakeholder concern |

---

## 🏗️ Architecture

`
┌─────────────────────────────────────────────────────────────────┐
│                     /ba-specialist                              │
│                    MAIN HARNESS ENTRY                            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
    ┌──────────────────────┼──────────────────────┐
    │                      ▼                       │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 0: Brief Intake & Clarification│   │
    │  │  → Ask clarifying questions if vague   │   │
    │  └──────────────────┬───────────────────┘   │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 1: Stakeholder Mapping         │   │
    │  │  📋 sub-stakeholder-mapper            │   │
    │  └──────────────────┬───────────────────┘   │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 2: Requirements Elicitation      │   │
    │  │  🔍 sub-requirements-gatherer         │   │
    │  └──────────────────┬───────────────────┘   │
    │                     ▼                        │
    │  ╔══════════════════════════════════════╗    │
    │  ║  ⏸  CHECKPOINT: User confirms reqs  ║    │
    │  ╚══════════════════════════════════════╝    │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 3: Persona & Story Mapping      │   │
    │  │  👤 sub-persona-story-mapper           │   │
    │  └──────────────────┬───────────────────┘   │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 4: Gap Analysis                 │   │
    │  │  📊 sub-gap-analyzer                  │   │
    │  └──────────────────┬───────────────────┘   │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 5: Quality Gate                 │   │
    │  │  ✅ sub-quality-reviewer               │   │
    │  │  → INVEST + MoSCoW + Consistency       │   │
    │  ╔══════════════════════════════════════╗    │
    │  ║  Score ≥ 80 → PASS                   ║    │
    │  ║  Score 60-79 → WARN (retry once)     ║    │
    │  ║  Score < 60 → BLOCK (revise)        ║    │
    │  ╚══════════════════════════════════════╝    │
    │                     ▼                        │
    │  ┌──────────────────────────────────────┐   │
    │  │  Stage 6: Specification Synthesis      │   │
    │  │  📄 Full BA Specification Document      │   │
    │  └──────────────────────────────────────┘   │
    └──────────────────────────────────────────────┘
`

---

## 🔄 Harness Flow

### Stage 0: Brief Intake & Clarification
Reads the user's project brief. If it's vague (< 3 sentences or lacks a clear goal), asks 3–5 targeted clarifying questions **before** proceeding. Never skips this stage.

### Stage 1: Stakeholder Mapping → sub-stakeholder-mapper
Identifies all stakeholders, classifies them using the **Mitchell Salience Model** (Definitive, Dominant, Dependent, Dangerous, Discretionary, Dormant, Demanding), places them on a **Power/Interest Grid**, and assigns engagement strategies.

### Stage 2: Requirements Elicitation → sub-requirements-gatherer
Generates **domain-specific interview question banks** (Software Product, Internal Business Process, External Service/API), produces **FR/NFR lists** with ISO/IEC 25010 categorization, and records all assumptions with confidence levels.

> **⏸ CHECKPOINT:** Requirements list presented to user for confirmation before proceeding to story mapping. This is mandatory.

### Stage 3: Persona & Story Mapping → sub-persona-story-mapper
Derives **2–4 user personas** from 5 archetypes (The Skeptic, The Power User, The Executive, The Compliance Officer, The New Joiner), constructs a **BMAD Story Map** (Activities → Tasks → Stories), identifies the **Walking Skeleton** MVP slice, and writes stories with **Given/When/Then acceptance criteria**.

### Stage 4: Gap Analysis → sub-gap-analyzer
Compares **As-Is vs. To-Be** across People/Process/Technology dimensions, identifies gaps with impact levels, performs **5 Whys root cause analysis** on the top 3 gaps, and proposes **bridging actions** with owners and timelines.

### Stage 5: Quality Gate → sub-quality-reviewer
Applies four validation dimensions:
- **MoSCoW Prioritization** — tags every story with Must/Should/Could/Won't
- **INVEST Validation** — scores each Must/Should story on 6 criteria (≥ 4/6 to pass)
- **Completeness Checklist** — 10-item pass/fail audit
- **Consistency Review** — 5 contradiction detection heuristics

Calculates a **Quality Score (0–100)** with weighted dimensions. Follows a fail/retry loop: PASS (≥ 80), WARN (60–79, retry once), BLOCK (< 60, return to failing stage).

### Stage 6: Specification Document Synthesis
Compiles all outputs into a professional **10-section BA Specification Document** with stakeholder register, personas, story map, gap analysis, and quality gate results.

---

## 🧩 Sub-Skills

| Sub-Skill | File | Purpose | Key Feature |
|-----------|------|---------|-------------|
| 📋 Stakeholder Mapper | skills/sub-stakeholder-mapper.md | Identify, classify, and map stakeholders | Mitchell Salience Model + Power/Interest Grid + 16 domain examples |
| 🔍 Requirements Gatherer | skills/sub-requirements-gatherer.md | Structured elicitation with interview banks | 3 domain banks (Software, Process, API) + ISO/IEC 25010 NFR |
| 👤 Persona & Story Mapper | skills/sub-persona-story-mapper.md | Generate personas and story maps | 5 archetypes + BMAD Story Map template + 10 example stories |
| 📊 Gap Analyzer | skills/sub-gap-analyzer.md | As-Is/To-Be gap analysis | 5 Whys root cause + Impact Matrix + Bridging Actions |
| ✅ Quality Reviewer | skills/sub-quality-reviewer.md | Validate requirements quality | INVEST scoring + MoSCoW tagging + 5 contradiction heuristics |

### Sub-Skill Design Principles

Every sub-skill follows a consistent structure:

1. **Frontmatter** — YAML metadata (
ame, description)
2. **Purpose** — Why this sub-skill exists
3. **Inputs** — What it receives from previous stages
4. **Execution Steps** — Numbered, actionable instructions
5. **Outputs** — What it produces (tables, diagrams, artifacts)
6. **Quality Gate** — Pass/fail criteria before passing to next stage
7. **Graceful Degradation** — Fallback behavior when tools/data are unavailable

---

## ✅ Quality Gates

The quality gate in Stage 5 enforces **9 mandatory criteria** before the specification document is synthesized:

| # | Gate | Criterion | Threshold |
|---|------|-----------|-----------|
| 1 | 📋 Stakeholder Coverage | ≥ 3 stakeholder classes identified | Must pass |
| 2 | 📝 Requirements Volume | ≥ 5 FR + 3 NFR documented | Must pass |
| 3 | 📖 Story Format | All stories follow "As a / I want / So that" | 100% |
| 4 | ✅ Acceptance Criteria | All Must/Should stories have ≥ 2 AC in Given/When/Then | 100% |
| 5 | 🎯 INVEST Compliance | All Must Have stories score ≥ 4/6 on INVEST | Must pass |
| 6 | 🏷️ MoSCoW Tagged | All stories tagged | 100% |
| 7 | 📊 Gap Analysis | ≥ 3 gaps identified with impact levels | Must pass |
| 8 | 🔍 Consistency | 0 unresolved contradictions | Must pass (or documented) |
| 9 | 📈 Quality Score | Composite score ≥ 80/100 | Must pass |

**Score Calculation:**

`
Quality Score = (INVEST × 0.30) + (MoSCoW × 0.20) + (Completeness × 0.30) + (Consistency × 0.20)
`

**Fail/Retry Behavior:**

| Score Range | Status | Action |
|-------------|--------|--------|
| ≥ 80 | ✅ PASS | Proceed to synthesis |
| 60–79 | ⚠️ WARN | Identify failing items, propose fixes, re-run once |
| < 60 | 🚫 BLOCK | Return to failing stage with revision instructions |

---

## 🔎 Contradiction Detection Heuristics

The quality reviewer implements **5 detection heuristics** to catch requirement conflicts:

| # | Heuristic | Description | Example |
|---|-----------|-------------|---------|
| 1 | Direct Contradiction | Two requirements that cannot both be satisfied | "Real-time sync" vs. "Offline-first" |
| 2 | Story vs. NFR Conflict | A user story violates a non-functional requirement | "Admin can view all records" vs. "Only direct managers see team data" |
| 3 | Gap-Bridging vs. Constraint | A bridging action conflicts with a stated constraint | "Implement real-time dashboards" vs. "Must work on legacy offline hardware" |
| 4 | Assumption vs. Stakeholder | An assumption contradicts a stakeholder statement | Assumed "users prefer email" vs. stakeholder said "I never read emails" |
| 5 | MoSCoW Priority Mismatch | Must Have story serves only a Low-influence stakeholder | Must Have requested by a Monitor-quadrant stakeholder |

---

## 🧠 Knowledge Pipeline

The skill includes a **self-improving knowledge base** powered by an automated crawl pipeline:

### SECOND-KNOWLEDGE-BRAIN.md
- **22+ research entries** from requirements engineering, agile BA, and story mapping domains
- References: IEEE 29148, BABOK v3, INVEST criteria, MoSCoW prioritization, Jeff Patton story mapping
- Requirements smell taxonomy, ISO/IEC 25010 quality model, and analytical frameworks

### tools/knowledge_updater.py
Automated pipeline that:
- 🔍 Crawls **5 ArXiv cs.SE queries** for latest RE research
- 🌐 Fetches **4 authoritative web sources** (IIBA, Agile Alliance, Mountain Goat Software, IEEE)
- 🔄 Deduplicates entries by DOI/URL hash
- 📊 Scores relevance using keyword matching (60%) + recency (40%)
- 📝 Appends scored entries to SECOND-KNOWLEDGE-BRAIN.md

`ash
# Run the knowledge updater
python tools/knowledge_updater.py
`

**Fallback:** If crawl4ai is not installed, the script falls back to equests for HTTP-based crawling.

---

## 📁 Project Structure

`
ba-specialist-agent-skill/
├── 📄 CLAUDE.md                              # Skill identity, harness flow, integration notes
├── 📄 README.md                              # This file
├── 📄 PROJECT-detail.md                      # Full technical specification
├── 📄 PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase-by-phase build roadmap (all complete)
├── 📄 SECOND-KNOWLEDGE-BRAIN.md              # Self-improving domain knowledge base
├── 📄 progression.json                        # Skill completion status
├── 📁 skills/
│   ├── 📄 main.md                            # Main harness (6-stage pipeline)
│   ├── 📄 sub-stakeholder-mapper.md          # Stakeholder identification & classification
│   ├── 📄 sub-requirements-gatherer.md       # Structured elicitation & interview banks
│   ├── 📄 sub-persona-story-mapper.md        # Persona generation & story mapping
│   ├── 📄 sub-gap-analyzer.md                # As-Is/To-Be gap analysis
│   └── 📄 sub-quality-reviewer.md            # INVEST + MoSCoW quality gate
├── 📁 tests/
│   └── 📄 test-scenarios.md                  # 5 validation scenarios
└── 📁 tools/
    └── 🐍 knowledge_updater.py               # ArXiv + web crawl pipeline
`

---

## 🚀 Quick Start

### 1. Invoke the Skill

Simply provide a project brief:

`
/ba-specialist

We're building an order management system for a mid-size e-commerce company.
Customers place orders on our website; operations staff process and ship them.
Currently everything is tracked in spreadsheets. We need a web app to streamline this.
`

### 2. For Vague Briefs

The skill will **pause and ask clarifying questions** before proceeding:

`
/ba-specialist

We need an app.
`

→ The skill asks: "What problem does this app solve?", "Who are the primary users?", "What does success look like?"

### 3. For Process Improvement (Non-Software)

`
/ba-specialist

We need to redesign our vendor onboarding process. Currently it takes 6 weeks
and involves 5 departments. We want to cut it to 2 weeks. No software is being
built — this is a process improvement project.
`

The skill **adapts its language** from software to process context automatically.

---

## 🧪 Test Scenarios

Five comprehensive test scenarios validate the skill:

| # | Scenario | Domain | Key Validation |
|---|----------|--------|----------------|
| 1 | 🛒 E-Commerce Order Management | Standard software | Full pipeline, ≥ 8 FR + 4 NFR, INVEST ≥ 80 |
| 2 | 🏥 Hospital Appointment System | Regulated (HIPAA) | Compliance officer engaged, PHI stories have security AC |
| 3 | ❓ Underspecified Brief | Edge case | Pauses at Stage 0, assumptions Low confidence |
| 4 | ⚠️ Conflicting Requirements | Edge case | Contradiction logged, escalated, -20 penalty applied |
| 5 | 🔄 Process Redesign | Non-software | Adapts language to process context, INVEST Testable adapted |

All 5 scenarios **PASS** with documented results in 	ests/test-scenarios.md.

---

## ⚙️ Configuration

### Quality Gate Thresholds

| Parameter | Default | Description |
|-----------|---------|-------------|
| INVEST_WEIGHT | 0.30 | Weight for INVEST compliance in quality score |
| MOSCOW_WEIGHT | 0.20 | Weight for MoSCoW coverage |
| COMPLETENESS_WEIGHT | 0.30 | Weight for completeness checklist |
| CONSISTENCY_WEIGHT | 0.20 | Weight for consistency review |
| PASS_THRESHOLD | 80 | Minimum score to proceed to synthesis |
| WARN_THRESHOLD | 60 | Below this = BLOCK, 60-79 = WARN |
| MOSCOW_MUST_CAP | 0.60 | Must Have stories must be ≤ 60% of total |
| INVEST_MIN_SCORE | 4/6 | Minimum INVEST criteria pass per story |
| MAX_RETRIES | 2 | Maximum quality gate retry cycles |

### Knowledge Updater

| Parameter | Default | Description |
|-----------|---------|-------------|
| RECENCY_WEIGHT | 0.4 | Weight for publication recency in relevance scoring |
| KEYWORD_WEIGHT | 0.6 | Weight for keyword match in relevance scoring |
| MIN_RELEVANCE_SCORE | 0.25 | Minimum score to include a crawled entry |
| MAX_ENTRIES_PER_RUN | 15 | Maximum new entries per crawl run |
| CRAWL_FREQUENCY | Weekly | How often to run the knowledge updater |

---

## 🔗 Cross-Skill Integration

BA Specialist is part of **Cluster A — Professional Role & Audit Harnesses**:

| Skill | Integration Point |
|-------|-------------------|
| 🏗️ **project-manager** | Shared Power/Interest Grid methodology; BA produces stakeholder register → PM produces RACI matrix |
| 🎨 **brand-recognition-auditor** | Shared quality gate pattern (weighted 0-100 score with PASS/WARN/BLOCK); both use YAML frontmatter and consistent sub-skill structure |

When multiple Cluster A skills are invoked on the same project, they produce **compatible deliverables** — stakeholder registers, quality scores, and sub-skill invocations follow the same patterns.

---

## 📚 Key References

| Reference | Source | Application |
|-----------|--------|-------------|
| IEEE 29148:2018 | IEEE | Requirements engineering international standard |
| IIBA BABOK v3 | IIBA | Business analysis best practices |
| INVEST Criteria | Bill Wake (2003) | Story quality validation |
| MoSCoW Prioritization | Dai Clegg / DSDM | Priority tagging |
| User Story Mapping | Jeff Patton (2014) | BMAD-aligned story mapping |
| Stakeholder Salience Model | Mitchell et al. (1997) | Power/Interest classification |
| 5 Whys Root Cause | Toyota Production System | Gap root cause analysis |
| ISO/IEC 25010 | ISO | Non-functional requirements quality model |
| Requirements Smells | Femmer et al. (2017) | Detecting poorly formed requirements |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Ensure all sub-skill quality gates still pass
5. Commit with descriptive messages
6. Push to your fork and submit a pull request

Please ensure all new sub-skills follow the standard structure: **Frontmatter → Purpose → Inputs → Execution Steps → Outputs → Quality Gate → Graceful Degradation**.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with 🧠 by the BA Specialist team**

*Transforming vague ideas into airtight requirements, one story at a time.*

</div>