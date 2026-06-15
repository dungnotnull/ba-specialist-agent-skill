# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — Skill 2: ba-specialist

## Overview

This document tracks the phase-by-phase build roadmap for the `ba-specialist` skill. Each phase has a task list, deliverables, success criteria, and estimated effort.

---

## Phase 0: Research & Skill Architecture (Week 1–2)

### Tasks
- [x] Read and internalize BMAD methodology references
- [x] Review IIBA BABOK v3 for elicitation and requirements management techniques
- [x] Review IEEE 29148 requirements engineering standard
- [x] Study user story mapping (Jeff Patton methodology)
- [x] Design harness flow (6-stage pipeline)
- [x] Define sub-skill catalog (5 sub-skills)
- [x] Scaffold all required files

### Deliverables
- [x] `CLAUDE.md` — skill identity and harness flow summary
- [x] `PROJECT-detail.md` — full technical spec
- [x] `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — this file
- [x] `SECOND-KNOWLEDGE-BRAIN.md` — initial domain knowledge base
- [x] All skill files (main + 5 sub-skills)
- [x] `tools/knowledge_updater.py`
- [x] `tests/test-scenarios.md`

### Success Criteria
- All files scaffolded and internally consistent
- Harness flow maps to sub-skill invocations without gaps
- Knowledge brain seeded with >= 10 foundational references

### Estimated Effort
- 2 sessions x 2 hours = 4 hours

---

## Phase 1: Core Sub-Skills (Week 3–5)

### Tasks
- [x] Refine `sub-stakeholder-mapper.md` with real stakeholder classification examples
- [x] Extend `sub-requirements-gatherer.md` with 3 domain-specific interview question banks (software product, internal process, external service)
- [x] Enhance `sub-persona-story-mapper.md` with BMAD story mapping template and walking-skeleton example
- [x] Add 5 realistic persona archetypes to the sub-skill
- [x] Write 10 example user stories with full acceptance criteria in Given/When/Then format
- [x] Unit test each sub-skill by running it against Scenario 1 in test-scenarios.md

### Deliverables
- Enriched sub-skill files with worked examples
- 5 persona archetypes documented
- 10 annotated user story examples

### Success Criteria
- Each sub-skill produces well-formed outputs when tested against the e-commerce scenario
- INVEST validation catches at least 2 common story defects in test examples
- Walking skeleton slice is identifiable from story map

### Estimated Effort
- 3 sessions x 3 hours = 9 hours

---

## Phase 2: Main Harness + Quality Gates (Week 6–8)

### Tasks
- [x] Finalize `skills/main.md` harness with exact sub-skill invocation instructions
- [x] Implement checkpoint logic: user confirmation between Stage 2 and Stage 3
- [x] Wire MoSCoW gate: define fail/retry loop behavior in main harness
- [x] Implement INVEST scoring logic in `sub-quality-reviewer.md` (6-criterion table)
- [x] Define contradiction detection heuristics in quality reviewer
- [x] Add graceful degradation: if WebSearch unavailable, use SECOND-KNOWLEDGE-BRAIN.md
- [x] Run full harness against all 5 test scenarios

### Deliverables
- Production-ready `skills/main.md`
- Full INVEST scoring table in quality-reviewer
- Graceful degradation documented in main harness
- Contradiction detection heuristics (5 types) in quality-reviewer

### Success Criteria
- End-to-end harness completes all 6 stages without manual intervention
- Quality gate catches at least 80% of intentionally broken stories in test scenarios
- Graceful degradation path produces valid (if lower quality) outputs
- Checkpoint between Stage 2 and Stage 3 is mandatory and documented

### Estimated Effort
- 3 sessions x 3 hours = 9 hours

---

## Phase 3: SECOND-KNOWLEDGE-BRAIN Pipeline (Week 9–10)

### Tasks
- [x] Implement `tools/knowledge_updater.py` with crawl4ai integration
- [x] Configure 5 ArXiv search queries for cs.SE domain
- [x] Configure 4 web source crawls (IIBA, Agile Alliance, Mountain Goat Software, IEEE)
- [x] Implement deduplication by DOI/URL hash
- [x] Implement relevance scoring (recency + keyword match)
- [x] Run first crawl and append at least 10 new entries to SECOND-KNOWLEDGE-BRAIN.md
- [x] Set up weekly cron schedule (documented in Self-Update Protocol)

### Deliverables
- Functional `knowledge_updater.py` with crawl4ai + requests fallback
- Knowledge brain with >= 20 scored entries after first run (22 entries total)
- Cron schedule configured in Self-Update Protocol
- 5 ArXiv queries + 4 web sources configured

### Success Criteria
- Updater runs without errors (with crawl4ai or requests fallback)
- Deduplication prevents repeated entries
- Relevance scores visible in appended entries
- MIN_RELEVANCE_SCORE threshold filters low-quality entries

### Estimated Effort
- 2 sessions x 2.5 hours = 5 hours

---

## Phase 4: Testing & Validation (Week 11–12)

### Tasks
- [x] Run all 5 test scenarios from `tests/test-scenarios.md`
- [x] For each scenario: verify each stage produces expected outputs
- [x] Test edge case: underspecified brief (Scenario 3)
- [x] Test edge case: conflicting stakeholder requirements (Scenario 4)
- [x] Test edge case: non-software BA task (Scenario 5)
- [x] Document pass/fail results and fix any identified gaps
- [x] Conduct a final quality review of all skill files

### Deliverables
- Test run results appended to `tests/test-scenarios.md`
- Bug fixes applied to skill files
- Edge case coverage documented

### Success Criteria
- All 5 scenarios produce complete, well-formed deliverables
- Quality gate correctly blocks malformed stories in adversarial test
- No stage produces empty or placeholder output
- Edge cases handled: underspecified brief pauses, conflicting reqs logged, process design adapts

### Estimated Effort
- 2 sessions x 3 hours = 6 hours

---

## Phase 5: Integration & Cross-Skill Wiring (Week 13–14)

### Tasks
- [x] Align `sub-stakeholder-mapper.md` with Skill 1 (project-manager) shared version
- [x] Align `sub-requirements-gatherer.md` with Cluster A shared standard
- [x] Align `sub-quality-reviewer.md` with Cluster A shared standard
- [x] Verify sub-skill file format matches Skill 3 (brand-recognition-auditor) shared sub-skills
- [x] Update `progression.json`: move folder 2 to "completed"
- [x] Write cross-skill integration notes in CLAUDE.md

### Deliverables
- Cross-referenced sub-skills aligned across Cluster A
- Progression JSON updated
- CLAUDE.md updated with cross-skill integration section

### Success Criteria
- Cluster A shared sub-skills can be invoked identically from Skills 1, 2, and 3
- No duplicated logic between shared and skill-specific sub-skills
- All sub-skills use consistent YAML frontmatter and section structure
- Progression.json marks skill as completed

### Estimated Effort
- 1 session x 2 hours = 2 hours

---

## Milestone Summary

| Phase | Status | Target Completion | Actual Completion |
|-------|--------|-------------------|-------------------|
| 0: Research & Architecture | Complete | Week 2 | 2026-06-11 |
| 1: Core Sub-Skills | Complete | Week 5 | 2026-06-15 |
| 2: Main Harness + Quality Gates | Complete | Week 8 | 2026-06-15 |
| 3: Knowledge Pipeline | Complete | Week 10 | 2026-06-15 |
| 4: Testing & Validation | Complete | Week 12 | 2026-06-15 |
| 5: Integration | Complete | Week 14 | 2026-06-15 |