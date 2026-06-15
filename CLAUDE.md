# CLAUDE.md — Skill 2: ba-specialist

## Skill Identity
- **Name:** ba-specialist
- **Tagline:** Transform vague ideas into airtight software requirements — the BMAD way
- **Current Phase:** Phase 5 — Complete, production-ready
- **Cluster:** A — Professional Role & Audit Harnesses

---

## Problem This Skill Solves

Business Analysts are the bridge between business stakeholders and development teams. Without structured elicitation, requirements are ambiguous, incomplete, or contradictory — leading to failed projects, rework, and scope creep. This skill harness transforms any project brief into a professional BA deliverable: structured user stories with acceptance criteria, a gap analysis between as-is and to-be states, MoSCoW-prioritized backlog, and a complete specification document. It is inspired by the BMAD (Business, Management, Architecture, Development) methodology for requirements engineering and story mapping.

---

## Harness Flow Summary

`
User invokes /ba-specialist
│
├── Stage 0: Project Brief Intake & Clarification
│   └── Ask clarifying questions if brief is vague; confirm understanding before proceeding
│
├── Stage 1: Stakeholder Mapping
│   └── [sub-stakeholder-mapper] → Identify all stakeholders, roles, influence, interests
│
├── Stage 2: Requirements Elicitation
│   └── [sub-requirements-gatherer] → Interview guide + document analysis + assumption log
│
│   ╔══════════════════════════════════════════════════╗
│   ║  CHECKPOINT: User confirms requirements before    ║
│   ║  proceeding to story mapping (mandatory)        ║
│   ╚══════════════════════════════════════════════════╝
│
├── Stage 3: Persona & Story Mapping
│   └── [sub-persona-story-mapper] → BMAD-aligned personas → user story map → story slices
│
├── Stage 4: Gap Analysis
│   └── [sub-gap-analyzer] → As-is state → To-be state → gap identification → impact matrix
│
├── Stage 5: Quality Gate — MoSCoW Prioritization
│   └── [sub-quality-reviewer] → Completeness check → consistency check → MoSCoW tagging → INVEST validation
│
│   ╔══════════════════════════════════════════════════╗
│   ║  QUALITY GATE: Score >= 80 = PASS               ║
│   ║               Score 60-79 = WARN (retry once)    ║
│   ║               Score < 60  = BLOCK (revise)      ║
│   ╚══════════════════════════════════════════════════╝
│
└── Stage 6: Specification Document Synthesis
    └── [main] → Full spec document: personas, stories, AC, gap report, priority backlog
`

---

## Sub-Skills

| File | Purpose |
|------|---------|
| skills/sub-stakeholder-mapper.md | Identify, classify, and map all project stakeholders by role, influence, and interest |
| skills/sub-requirements-gatherer.md | Guide structured elicitation: interview protocols, document analysis, assumption logging |
| skills/sub-persona-story-mapper.md | Generate BMAD-aligned personas and produce user story maps with story slices |
| skills/sub-gap-analyzer.md | Compare as-is vs to-be state, identify gaps, and produce an impact/priority matrix |
| skills/sub-quality-reviewer.md | Validate requirements for completeness, consistency, INVEST compliance, and MoSCoW tagging |

---

## Tools Required

- WebSearch — search BMAD methodology, IEEE 29148, domain-specific best practices
- WebFetch — fetch ArXiv papers, industry standards documents, Agile/BA resources
- Read — read uploaded source documents, existing specs, user-provided context
- Write — produce all deliverable files
- Bash / PowerShell — run knowledge_updater.py pipeline

---

## Knowledge Sources

- **ArXiv categories:** cs.SE (Software Engineering), cs.HC (Human-Computer Interaction)
- **Domain URLs:**
  - https://www.iiba.org (IIBA BABOK Guide)
  - https://www.scaledagileframework.com (SAFe requirements)
  - https://github.com/bmad-agency (BMAD methodology reference)
  - https://agilealliance.org
  - https://www.mountaingoatsoftware.com/agile/user-stories
- **Standards:** IEEE 29148 (Requirements Engineering), ISO/IEC 29110 (SE for small orgs), ISO/IEC 25010 (Quality Model)

---

## Supporting Tools

- 	ools/knowledge_updater.py — crawl4ai pipeline fetching latest BA research from ArXiv, IIBA, IEEE, Agile Alliance; appends scored entries to SECOND-KNOWLEDGE-BRAIN.md

---

## Cross-Skill Integration (Cluster A)

This skill aligns with other Cluster A skills through shared patterns and conventions:

### Skill 1: project-manager
- **Shared pattern:** sub-stakeholder-mapper uses the same Power/Interest Grid classification (Mitchell et al. salience model) as the project-manager skill's stakeholder identification step
- **Alignment note:** When both skills are invoked on the same project, they should produce consistent stakeholder registers. The BA skill produces more detailed engagement strategies; the PM skill produces more detailed RACI matrices
- **Invoked by:** The project-manager skill may invoke sub-stakeholder-mapper first and pass the register to sub-requirements-gatherer

### Skill 3: brand-recognition-auditor
- **Shared pattern:** sub-quality-reviewer INVEST scoring and completeness check pattern matches the brand-recognition-auditor's quality gate pattern
- **Alignment note:** Both skills use a weighted quality score (0-100) with PASS/WARN/BLOCK thresholds. The scoring weights differ per domain but the mechanism is consistent
- **Invoked by:** Either skill can reference the other's quality gate mechanism when auditing cross-domain deliverables

### Shared Sub-Skill Conventions
- All sub-skills use YAML frontmatter (---name/description---) for metadata
- All sub-skills include: Purpose, Inputs, Execution Steps, Outputs, Quality Gate, Graceful Degradation
- Quality gates produce Pass/Fail results, not just advisory notes
- All sub-skills support graceful degradation when WebSearch is unavailable (fall back to SECOND-KNOWLEDGE-BRAIN.md)

---

## Active Development Tasks

- [x] Phase 0: Scaffold all files
- [x] Phase 1: Implement core sub-skills with worked examples, 5 persona archetypes, 10 annotated user stories
- [x] Phase 2: Implement main harness + quality gate sub-skills with checkpoint logic, fail/retry loop, contradiction heuristics
- [x] Phase 3: Wire knowledge pipeline with 5 ArXiv queries, 4 web sources, deduplication, and relevance scoring
- [x] Phase 4: Validate all 5 test scenarios (e-commerce, hospital HIPAA, underspecified brief, conflicting reqs, process redesign)
- [x] Phase 5: Cross-skill alignment with Cluster A, progression.json updated, integration notes in CLAUDE.md

---

## Reference Files

- PROJECT-detail.md — full technical specification
- PROJECT-DEVELOPMENT-PHASE-TRACKING.md — build roadmap and milestones
- SECOND-KNOWLEDGE-BRAIN.md — domain knowledge base (self-improving)
- progression.json — skill completion status for cross-skill orchestration
- 	ests/test-scenarios.md — 5 validation scenarios with pass/fail criteria