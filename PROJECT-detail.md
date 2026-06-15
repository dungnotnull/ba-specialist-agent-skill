# PROJECT-detail.md — Skill 2: ba-specialist

## Executive Summary

The `ba-specialist` skill is a full harness that transforms any project brief into a professional Business Analysis (BA) deliverable. Inspired by the BMAD methodology and grounded in IEEE 29148, IIBA BABOK v3, and Agile story mapping practices, it guides Claude through six structured stages: stakeholder mapping → requirements elicitation → persona & story mapping → gap analysis → quality gate → specification document synthesis.

---

## Problem Statement

Most software projects fail not from bad code but from bad requirements. Ambiguous briefs, missed stakeholders, untested assumptions, and inconsistent user stories cascade into rework, scope creep, and delivery failures. A skilled Business Analyst prevents this by structuring discovery, challenging assumptions, and producing traceable, prioritized requirements artifacts. This skill operationalizes that expertise at the level of a senior BA, making it available for any user who provides a project idea or brief.

---

## Target Users & Use Cases

| User | Trigger | Skill Output |
|------|---------|-------------|
| Product Manager | "I have a new feature idea, help me spec it out" | Full user stories, acceptance criteria, stakeholder map |
| Startup Founder | "Turn my app concept into requirements for developers" | Personas, story map, gap analysis, spec doc |
| Developer | "We need a BA document before we start sprint planning" | INVEST-validated backlog, MoSCoW priorities |
| Business Stakeholder | "Document what our new process should look like" | As-is/to-be gap analysis, impact matrix |
| Student / Learner | "Teach me how to write user stories for this system" | Annotated examples, requirement critique |

---

## Harness Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        /ba-specialist                               │
│                      MAIN HARNESS ENTRY                             │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  Stage 1: Project Brief Intake  │
              │  Output: brief summary, context │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  sub-stakeholder-mapper         │
              │  Output: stakeholder register   │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  sub-requirements-gatherer      │
              │  Output: raw requirements list, │
              │  assumption log, interview guide │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  sub-persona-story-mapper       │
              │  Output: 2-4 personas, story    │
              │  map, story slices              │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  sub-gap-analyzer               │
              │  Output: as-is/to-be analysis,  │
              │  gap table, impact matrix       │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  sub-quality-reviewer           │
              │  Quality Gate: INVEST + MoSCoW  │
              │  + completeness + consistency   │
              └────────────────┬────────────────┘
                               │
              ┌────────────────▼────────────────┐
              │  Stage 6: Spec Document Synth.  │
              │  Output: Full BA Specification  │
              └─────────────────────────────────┘
```

---

## Full Sub-Skill Catalog

### sub-stakeholder-mapper

**Purpose:** Identify all stakeholders in a project, classify them by role, and map their influence and interest levels.

**Inputs:** Project brief, domain context, any named parties

**Outputs:** Stakeholder Register (table: Name/Role, Category, Influence, Interest, Key Concern, Engagement Strategy)

**Tools:** WebSearch (industry role research), Read (briefs), Write (register)

**Quality Gate:** At least 3 stakeholder classes identified (sponsor/user/impacted); every stakeholder has an engagement strategy

---

### sub-requirements-gatherer

**Purpose:** Conduct structured requirements elicitation using interview protocols, document analysis, and assumption logging.

**Inputs:** Stakeholder register, project brief

**Outputs:**
- Interview question bank (by stakeholder type)
- Raw requirements list (functional + non-functional)
- Assumption & constraint log
- Open questions backlog

**Tools:** WebSearch (domain research), Read (uploaded docs), Write (elicitation artifacts)

**Quality Gate:** At least 5 functional requirements, 3 non-functional requirements; every assumption is marked with confidence level (High/Medium/Low)

---

### sub-persona-story-mapper

**Purpose:** Generate BMAD-aligned user personas and produce a user story map with walking-skeleton story slices.

**Inputs:** Stakeholder register, raw requirements list

**Outputs:**
- 2–4 User Personas (Name, Role, Goals, Frustrations, Tech Comfort, Quote)
- User Story Map (activities → tasks → user stories)
- Walking-skeleton story slice (MVP release)
- Story backlog (full list with acceptance criteria)

**Tools:** WebSearch (persona methodology), Write (personas + map)

**Quality Gate:** Every story follows "As a [persona], I want [action], so that [benefit]" format; walking skeleton slice identified; acceptance criteria in Given/When/Then format

---

### sub-gap-analyzer

**Purpose:** Compare the current as-is state against the desired to-be state, identify capability gaps, and produce an impact/priority matrix.

**Inputs:** Raw requirements, project brief, stakeholder concerns

**Outputs:**
- As-Is State Description (people, process, technology)
- To-Be State Description
- Gap Analysis Table (Gap ID, Description, Affected Area, Impact, Priority)
- Root Cause Analysis for top-3 gaps
- Recommended bridging actions

**Tools:** Read, Write, WebSearch (benchmark data)

**Quality Gate:** Every gap has an impact level (High/Medium/Low) and a recommended action; root cause identified for top 3 gaps

---

### sub-quality-reviewer

**Purpose:** Validate all requirements artifacts for completeness, consistency, INVEST principle compliance, and MoSCoW prioritization.

**Inputs:** All previous stage outputs

**Outputs:**
- INVEST validation table (each story scored on I/N/V/E/S/T criteria)
- MoSCoW priority table (Must/Should/Could/Won't)
- Completeness checklist result (pass/fail per item)
- Consistency review (contradiction log, resolution notes)
- Final quality score (0–100)

**Tools:** Read, Write

**Quality Gate:** All Must-have stories pass INVEST; no unresolved contradictions; completeness checklist ≥ 90%

---

## Skill File Format Specification

### Frontmatter Schema (main.md)

```yaml
---
name: ba-specialist
description: Transform any project brief into a professional BA specification — stakeholder mapping, user story writing, gap analysis, MoSCoW prioritization, and full spec document
---
```

### Required Sections in main.md
1. Role & Persona
2. Workflow (Harness Flow) — numbered stages with sub-skill invocations
3. Sub-skills Available
4. Tools
5. Output Format
6. Quality Gates

---

## E2E Execution Flow

```
1. User invokes /ba-specialist with a project brief
2. Claude reads brief, asks 3–5 clarifying questions if ambiguous
3. Invokes sub-stakeholder-mapper → produces stakeholder register
4. Invokes sub-requirements-gatherer → produces elicitation artifacts
5. CHECKPOINT: presents requirements list to user for correction/addition
6. Invokes sub-persona-story-mapper → produces personas + story map
7. Invokes sub-gap-analyzer → produces gap analysis
8. Invokes sub-quality-reviewer → runs INVEST + MoSCoW quality gate
   → If gate fails: identify failed stories, request revision, re-run gate
   → If gate passes: proceed to synthesis
9. Synthesizes full BA Specification Document
10. Presents final document with summary and next-step recommendations
```

---

## SECOND-KNOWLEDGE-BRAIN Integration

**Sources:**
- ArXiv cs.SE — requirements engineering, formal specification, agile methods
- IIBA BABOK v3 summaries and guides
- IEEE 29148 (Requirements Engineering standard)
- Agile Alliance resources (user stories, acceptance criteria, story mapping)
- BMAD methodology documents

**Crawl Config (knowledge_updater.py):**
- Search queries: "requirements engineering survey", "user story quality", "BMAD methodology BA", "agile requirements elicitation", "stakeholder analysis techniques"
- Sources: arxiv.org/cs.SE, iiba.org, agilealliance.org, mountaingoatsoftware.com
- Frequency: Weekly
- Append format: Table row in SECOND-KNOWLEDGE-BRAIN.md with date stamp

---

## Quality Gates Definition

Before final spec document is shown, ALL of the following must pass:

| Gate | Criterion | Pass Threshold |
|------|-----------|----------------|
| Stakeholder Coverage | All stakeholder classes identified | ≥ 3 classes |
| Requirements Completeness | Functional + non-functional requirements present | ≥ 5 FR + 3 NFR |
| Story Format | All stories follow BMAD user story format | 100% |
| Acceptance Criteria | All stories have Given/When/Then AC | 100% of Must/Should stories |
| INVEST Compliance | Each story passes INVEST validation | ≥ 80% score |
| MoSCoW Tagged | All stories have MoSCoW priority | 100% |
| Gap Analysis | As-is/to-be comparison complete | At least 3 gaps identified |
| Consistency | No contradictions in requirements | 0 unresolved contradictions |

---

## Test Scenarios

See `tests/test-scenarios.md` for 5+ concrete scenario tests.

---

## Key Design Decisions

1. **BMAD-inspired story mapping** is the core innovation — stories are generated from persona activities, not just wish lists, ensuring behavioral traceability.
2. **MoSCoW as a quality gate** (not just a tag) — stories that cannot be classified are flagged for stakeholder review before the spec is finalized.
3. **INVEST validation per story** surfaces poorly formed requirements before they reach developers.
4. **Assumption log** is mandatory — every untested assumption is recorded with confidence level to manage discovery risk.
5. **Walking skeleton slice** ensures the MVP is explicitly identified early, giving developers a clear first-sprint target.
6. **Gap analysis roots causes** are required for top-3 gaps, preventing surface-level gap lists without actionable bridging strategies.
7. **Research-first**: elicitation output is enriched with domain research via WebSearch before personas are finalized.
