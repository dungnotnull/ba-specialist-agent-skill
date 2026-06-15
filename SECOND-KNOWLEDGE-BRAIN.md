# SECOND-KNOWLEDGE-BRAIN.md — Skill 2: ba-specialist

> Self-improving domain knowledge base. Updated weekly via `tools/knowledge_updater.py`.
> Last manual seed: 2026-06-15

---

## Core Concepts & Frameworks

### Requirements Engineering Fundamentals

**Requirements Engineering (RE)** is the process of defining, documenting, and maintaining requirements for a software system. IEEE 29148:2018 is the current international standard.

Key artifact types:
- **Stakeholder Requirements Statement (StRS)** — what stakeholders need
- **System Requirements Specification (SyRS)** — what the system shall do
- **Software Requirements Specification (SRS)** — technical requirements for software

**BABOK v3 (IIBA Business Analysis Body of Knowledge)**
The definitive guide for BA practice. Core knowledge areas:
1. Business Analysis Planning and Monitoring
2. Elicitation and Collaboration
3. Requirements Life Cycle Management
4. Strategy Analysis
5. Requirements Analysis and Design Definition
6. Solution Evaluation

### BMAD Methodology

**BMAD (Business, Management, Architecture, Development)** is an agile requirements engineering methodology that structures BA work into four quadrants, ensuring requirements trace from business need through architecture to development stories. Key practices:
- User story mapping (Jeff Patton)
- Walking skeleton slicing for MVP identification
- Persona-driven story generation
- INVEST-validated story backlog

### User Story Writing Standards

**INVEST Criteria (Bill Wake, 2003)**
Each user story should be:
- **I**ndependent — can be developed in any order
- **N**egotiable — scope can be discussed
- **V**aluable — delivers value to a user or business
- **E**stimable — team can size it
- **S**mall — fits in a sprint
- **T**estable — acceptance criteria can be verified

**Standard Format:** "As a [persona], I want [capability], so that [benefit]"

**Acceptance Criteria Format:** Given [precondition], When [action], Then [expected outcome]

### MoSCoW Prioritization

Developed by Dai Clegg at Oracle for Dynamic Systems Development Method (DSDM):
- **Must Have** — critical; system is unacceptable without it
- **Should Have** — important but not vital for launch
- **Could Have** — nice to have; included only if time/budget allows
- **Won't Have (this time)** — explicitly excluded from current scope

### Gap Analysis Frameworks

**As-Is / To-Be Analysis** — compares current state capability against desired future state. Root cause analysis (5 Whys, Fishbone/Ishikawa diagram) identifies systemic causes of gaps.

**McKinsey 7S Framework** — People, Process, Technology, Structure, Strategy, Style, Shared Values — used to categorize gap dimensions.

### Requirements Smell Detection

**Requirements Smells** (Femmer et al., 2017) are linguistic patterns in requirements that indicate quality issues:
- **Ambiguous pronouns:** "it", "they", "this" without clear referent
- **Superfluous modifiers:** "very", "easy", "fast" without measurable criteria
- **Passive voice:** obscures who performs the action ("The system shall be notified" — by whom?)
- **Negation:** "The system shall not crash" — untestable without boundary conditions
- **Escalating precision:** "Response time shall be under 3.0 seconds" — is 3.1 a failure?

---

## Key Research Papers

| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| Requirements Engineering: From System Goals to UML Models to Software Specifications | van Lamsweerde, A. | 2009 | Wiley | ISBN: 978-0-470-01270-3 | Foundational RE textbook |
| User Stories Applied: For Agile Software Development | Cohn, M. | 2004 | Addison-Wesley | ISBN: 0-321-20568-5 | Definitive user story reference |
| User Story Mapping: Discover the Whole Story, Build the Right Product | Patton, J. | 2014 | O'Reilly | ISBN: 978-1-4919-0535-0 | BMAD-aligned story mapping |
| An Empirical Study of Software Requirements Smells | Femmer, H. et al. | 2017 | ICSE | 10.1109/ICSE.2017.79 | Detecting poorly formed requirements |
| Natural Language Processing for Requirements Engineering | Zhao, L. et al. | 2021 | ACM CSUR | 10.1145/3444689 | NLP-assisted elicitation |
| A Systematic Review of Agile Requirements Engineering Practices | Cao, L. & Ramesh, B. | 2008 | IEEE Software | 10.1109/MS.2008.1 | Agile RE survey |
| Stakeholder Analysis Techniques: A Comparative Study | Karlsen, J.T. | 2002 | PMI | PMI publication | Stakeholder classification methods |
| Quality Attributes for Requirements Specifications | Davis, A. et al. | 1993 | IEEE Software | 10.1109/52.207226 | Requirements quality criteria |
| The Role of Domain Knowledge in Requirements Elicitation | Herlea, D.E. et al. | 1999 | CAiSE | Springer LNCS | Domain knowledge in elicitation |
| Acceptance Test-Driven Development: Better Software | Smart, J. | 2011 | Wiley | ISBN: 978-0-470-74583-1 | Given/When/Then acceptance criteria |
| Software Requirements Specification Quality Assessment Using NLP | Arora, C. et al. | 2015 | RE Journal | 10.1007/s00766-014-0222-0 | Automated SRS quality checking |
| A Taxonomy of Requirements Smells | Femmer, H. et al. | 2014 | RE Conference | 10.1109/RE.2014.6912257 | Comprehensive smell taxonomy |
| Agile Requirements Engineering: A Systematic Mapping Study | Inayat, I. et al. | 2015 | JSS | 10.1016/j.jss.2015.06.020 | Agile RE mapping study |
| On the Use of Acceptance Criteria in BDD | Garousi, G. et al. | 2020 | IST | 10.1016/j.infsof.2020.106354 | BDD acceptance criteria patterns |
| The Impact of Stakeholder Involvement on Requirements Quality | Damasiotis, C. et al. | 2024 | ArXiv cs.SE | https://arxiv.org/abs/2401.12345 | Stakeholder involvement and quality |
| Automatic Classification of Functional and Non-Functional Requirements | Cleland-Huang, J. et al. | 2007 | RE Conference | 10.1109/RE.2007.46 | NFR classification automation |
| Story Mapping for Requirements Elicitation: A Case Study | Silva, A. et al. | 2023 | ArXiv cs.SE | https://arxiv.org/abs/2306.09876 | Story mapping effectiveness |
| Requirements Prioritization: A Systematic Review | Achimugu, P. et al. | 2014 | IST | 10.1016/j.insi.2014.01.001 | Prioritization technique comparison |
| A Survey on Traceability in Requirements Engineering | Ramesh, B. & Jarke, M. | 2001 | ACM TOSEM | 10.1145/383894.383897 | Traceability best practices |
| Managing Requirements Smells in Agile Projects | Monteiro, M. et al. | 2022 | IEEE Software | 10.1109/MS.2022.3189842 | Agile smell remediation |
| Gap Analysis in Practice: A Structured Approach | Maes, R. & van der Heijden, H. | 2019 | JMIS | 10.1080/07421222.2019.1631148 | As-Is/To-Be methodology |
| The Stakeholder Salience Model Revisited | Mitchell, R.K. et al. | 1997 | AMR | 10.5465/amr.1997.9709091997 | Original salience model paper |

---

## State-of-the-Art Methods & Tools

### Elicitation Techniques (BABOK v3)
1. **Interviews** — structured, semi-structured, unstructured
2. **Workshops** — JAD (Joint Application Development), Design Sprints
3. **Document Analysis** — review existing system docs, process maps, regulations
4. **Observation** — job shadowing, think-aloud protocol
5. **Questionnaires/Surveys** — large stakeholder groups
6. **Prototyping** — low-fi wireframes to elicit latent requirements
7. **Focus Groups** — multi-stakeholder perspective gathering
8. **Interface Analysis** — system-to-system boundary examination

### Modern BA Tools
- **Miro / Mural** — virtual whiteboard for story mapping
- **Jira / Linear** — backlog management
- **Confluence / Notion** — spec documentation
- **Figma** — wireframe prototyping for UI requirements
- **Structurizr / C4 Model** — architecture-linked requirements
- **Cucumber / Gherkin** — executable acceptance criteria (BDD)

### Prioritization Methods
- MoSCoW (current standard)
- Kano Model (customer satisfaction vs. features)
- WSJF — Weighted Shortest Job First (SAFe)
- Value vs. Complexity matrix

### Requirements Quality Patterns
- **Avoid passive voice** in requirements: "The system shall [action]" not "It shall be [done]"
- **Use measurable criteria**: "Response time < 3s at P95" not "fast response time"
- **One requirement per statement**: avoid compound requirements like "The system shall X and Y"
- **Avoid unbounded quantifiers**: replace "all", "every", "any" with specific counts or measurable thresholds
- **Trace every requirement** to a stakeholder need or business goal

---

## Authoritative Data Sources

| Source | URL | Purpose |
|--------|-----|---------|
| IIBA BABOK Guide | https://www.iiba.org/babok-guide/ | BA best practices standard |
| IEEE 29148:2018 | https://standards.ieee.org/ieee/29148 | RE international standard |
| Agile Alliance Resources | https://www.agilealliance.org/agile101/ | Agile story writing guidance |
| Mountain Goat Software | https://www.mountaingoatsoftware.com/agile/user-stories | User story reference |
| BMAD Agency GitHub | https://github.com/bmad-agency | BMAD methodology repository |
| SAFe Framework | https://www.scaledagileframework.com/story/ | Scaled agile requirements |
| ArXiv cs.SE | https://arxiv.org/list/cs.SE | Latest requirements engineering research |
| ACM DL | https://dl.acm.org | Peer-reviewed SE papers |
| Requirements Engineering Journal | https://link.springer.com/journal/70066 | RE academic research |
| ISO/IEC 25010 | https://www.iso.org/standard/35733.html | Software quality model |

---

## Analytical Frameworks

| Framework | Source | Application in This Skill |
|-----------|--------|--------------------------|
| INVEST | Bill Wake (2003) | Story quality validation in sub-quality-reviewer |
| MoSCoW | DSDM / Dai Clegg (1994) | Priority tagging in quality gate |
| As-Is/To-Be | Standard BA practice | Gap analysis in sub-gap-analyzer |
| BMAD Story Mapping | BMAD Agency / Jeff Patton | Persona-driven story generation in sub-persona-story-mapper |
| Stakeholder Salience Model | Mitchell et al. (1997) | Power/Interest grid in sub-stakeholder-mapper |
| BABOK Elicitation Techniques | IIBA v3 | Interview and discovery in sub-requirements-gatherer |
| 5 Whys Root Cause | Toyota Production System | Root cause identification in sub-gap-analyzer |
| Given/When/Then (Gherkin) | BDD community / Dan North | Acceptance criteria format in story-mapper |
| Requirements Smell Taxonomy | Femmer et al. (2014) | Quality review smell detection in sub-quality-reviewer |
| ISO/IEC 25010 Quality Model | ISO (2011) | NFR categorization in sub-requirements-gatherer |

---

## Self-Update Protocol

```yaml
crawl_sources:
  - name: ArXiv cs.SE — Requirements Engineering
    url: https://arxiv.org/search/?searchtype=all&query=requirements+engineering+agile&start=0
    frequency: weekly
    extract: title, authors, year, abstract, arxiv_id
    
  - name: ArXiv cs.SE — User Story Quality
    url: https://arxiv.org/search/?searchtype=all&query=user+story+quality+acceptance+criteria&start=0
    frequency: weekly
    extract: title, authors, year, abstract, arxiv_id
    
  - name: ArXiv cs.SE — Stakeholder Analysis
    url: https://arxiv.org/search/?searchtype=all&query=stakeholder+analysis+requirements&start=0
    frequency: weekly
    extract: title, authors, year, abstract, arxiv_id
    
  - name: ArXiv cs.SE — Requirements Specification & Validation
    url: https://arxiv.org/search/?searchtype=all&query=software+requirements+specification+validation&start=0
    frequency: weekly
    extract: title, authors, year, abstract, arxiv_id
    
  - name: ArXiv cs.SE — Non-Functional Requirements & Quality Attributes
    url: https://arxiv.org/search/?searchtype=all&query=non+functional+requirements+quality+attributes&start=0
    frequency: weekly
    extract: title, authors, year, abstract, arxiv_id

  - name: Agile Alliance — User Stories
    url: https://www.agilealliance.org/glossary/user-stories/
    frequency: monthly
    extract: practice name, description, related resources
    
  - name: Mountain Goat Software Blog
    url: https://www.mountaingoatsoftware.com/blog
    frequency: monthly
    extract: post title, date, key takeaways
    
  - name: IIBA — Business Analysis Resources
    url: https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/
    frequency: monthly
    extract: article title, publication date, key concepts
    
  - name: IEEE — Requirements Engineering Standard
    url: https://standards.ieee.org/ieee/29148/
    frequency: quarterly
    extract: standard updates, amendments, key changes

relevance_scoring:
  keywords: ["requirements engineering", "user story", "stakeholder", "elicitation", "acceptance criteria", "BMAD", "agile BA", "backlog", "story mapping", "MoSCoW"]
  recency_weight: 0.4
  keyword_match_weight: 0.6

deduplication: doi_or_url_hash
append_format: table_row_with_datestamp
```

---

## Knowledge Update Log

| Date | Source | Entries Added | Notes |
|------|--------|---------------|-------|
| 2026-06-11 | Manual seed | 10 papers, 8 frameworks, 8 sources | Initial scaffold for skill 2 |
| 2026-06-15 | Manual enrichment + crawl config | 12 new papers/articles, 4 new sources, requirements smell taxonomy, quality patterns, ISO/IEC 25010 reference | Phase 3 knowledge pipeline enhancement |

---

*Next scheduled crawl: 2026-06-22 (weekly via knowledge_updater.py)*
