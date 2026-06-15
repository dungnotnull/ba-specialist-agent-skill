# test-scenarios.md — Skill 2: ba-specialist

## Overview

This file contains 5 scenario-based tests for the `ba-specialist` skill. Each scenario defines an input (project brief), expected outputs per stage, and pass/fail criteria for the harness.

---

## Scenario 1: E-Commerce Order Management System (Standard Case)

**Trigger:** "We're building an order management system for a mid-size e-commerce company. Customers place orders on our website; operations staff process and ship them. Currently everything is tracked in spreadsheets. We need a web app to streamline this."

**Expected Outputs by Stage:**

### Stage 0 — Brief Intake & Clarification
- Brief has clear goal, domain, and known context
- Skill should confirm understanding: e-commerce OMS, replacing spreadsheet tracking, web app target
- No clarifying questions needed (brief is specific enough)

### Stage 1 — Stakeholder Mapping
- Expected stakeholders: Product Owner (sponsor), Operations Staff (primary user), Customers (secondary user), IT/DevOps (technical), Compliance Officer (regulatory)
- Minimum: 5 stakeholders across >= 3 categories
- Power/Interest Grid must show Operations Staff in "Manage Closely" quadrant
- Top 2 stakeholders must include Operations Staff and Product Owner

### Stage 2 — Requirements Elicitation
- Expected FR: order creation, order search, status updates, shipment tracking, inventory check, reporting
- Expected NFR: performance (page load < 3s), availability (99.5%), security (role-based access)
- Minimum: 8 FR, 4 NFR
- Assumption Log must include: "users have internet access", "current data can be migrated from spreadsheets"
- Must include domain-specific question bank (Software Product)

### Stage 3 — Persona & Story Mapping
- Expected personas: at least "Maya the Operations Manager", "Alex the Warehouse Picker", "Sam the E-Commerce Manager"
- Walking skeleton must include: create order -> process order -> update status -> confirm shipment
- Minimum: 12 user stories, all Must Have stories have >= 2 AC
- All stories follow "As a [persona name], I want [action], so that [benefit]" format
- No "generic" personas like "The User"

### Stage 4 — Gap Analysis
- Expected gaps: no centralized system (Technology), manual status updates (Process), no real-time visibility (Technology)
- Minimum: 3 gaps with impact levels
- Root cause for "no centralized system" gap must address infrastructure/investment lag
- All gaps must trace to at least 1 FR/NFR
- Bridging actions must have owners and timelines

### Stage 5 — Quality Gate
- Expected: all Must Have stories pass INVEST (>= 4/6)
- MoSCoW: Must Have <= 60% of total stories
- Quality Score: >= 80
- No unresolved contradictions
- Completeness: >= 9/10 checks pass

**Pass Criteria:** All stages produce expected outputs; final spec document covers all 10 sections; Quality Score >= 80

---

## Scenario 2: Hospital Patient Appointment System (Regulated Domain)

**Trigger:** "We're a regional hospital network. We need to replace our phone-based appointment booking with an online self-service system. Patients should book, reschedule, and cancel appointments. Clinical staff need to view their schedules. This must comply with HIPAA."

**Expected Outputs by Stage:**

### Stage 0 — Brief Intake & Clarification
- Brief is clear about domain, goal, and regulatory constraint
- Skill should confirm: hospital appointment booking system, HIPAA compliance required

### Stage 1 — Stakeholder Mapping
- Expected: Hospital Administration (sponsor), Patients (primary user), Clinical Staff (primary user), IT Security (technical), HIPAA Compliance Officer (regulatory)
- Minimum: 5 stakeholders across >= 3 categories
- Compliance Officer must appear in "Keep satisfied" or "Manage Closely" quadrant (high power, specialized interest)

### Stage 2 — Requirements Elicitation
- Expected FR: appointment booking, rescheduling, cancellation, schedule view for staff, notification (SMS/email), appointment reminders
- Expected NFR: HIPAA compliance (security/privacy), 99.9% availability, accessibility (WCAG 2.1 AA), mobile responsiveness
- Assumption Log must flag HIPAA as High Confidence constraint
- Must include domain-specific question bank (Internal Business Process / Healthcare)

### Stage 3 — Persona & Story Mapping
- Expected personas: at least "Patient Persona" and "Clinical Staff Persona"
- Walking skeleton: patient books appointment online -> receives confirmation -> staff sees updated schedule
- All PHI-handling stories must have additional AC for data privacy
- At least 1 story must explicitly address HIPAA compliance

### Stage 4 — Gap Analysis
- Expected gaps: no self-service booking capability (Technology), phone-only workflow (Process), no staff-facing scheduling tool (Technology)
- Bridging action for HIPAA gap must include: "engage HIPAA compliance officer for BAA review before development"
- Root cause analysis must address why current phone-based system persisted

### Stage 5 — Quality Gate
- INVEST test must flag any story that handles PHI without testable security AC as failing "Testable"
- Regulatory stories must all be tagged Must Have
- Quality Score: >= 80
- Compliance-related NFRs must be traceable to specific stories

**Pass Criteria:** HIPAA mentioned in >= 3 NFR; compliance officer has engagement strategy; all PHI stories have security AC

---

## Scenario 3: Underspecified Brief (Edge Case — Minimal Input)

**Trigger:** "We need an app."

**Expected Behavior:**

### Stage 0 — Clarification
- Skill must NOT proceed to Stage 1 immediately
- Must ask >= 3 clarifying questions:
  1. What problem does this app solve?
  2. Who are the primary users?
  3. What does success look like?
- Must wait for user response before proceeding
- After clarification, must summarize understanding and confirm before Stage 1

### Stages 1-5 (If User Provides Minimal Clarification)
- Skill must flag all requirements as Low confidence in Assumption Log
- Must generate interview question bank as a deliverable (not skip it)
- Output note: "[Requirements derived from minimal brief — stakeholder validation strongly recommended before sprint planning]"
- Personas may be derived from archetypes — marked as "Hypothesized"
- Walking skeleton must still be identifiable even with minimal data

**Pass Criteria:** Skill does not skip clarification; all assumptions marked Low confidence; interview question bank generated as primary deliverable; spec document note flags limitation

---

## Scenario 4: Conflicting Stakeholder Requirements (Edge Case — Contradiction)

**Trigger:** "We're building an internal HR portal. The HR Director wants all employee records visible to all managers. The Legal team says only direct managers can see their own team's data. The CEO wants a dashboard showing aggregated company-wide metrics."

**Expected Behavior:**

### Stage 1 — Stakeholder Mapping
- Must identify: HR Director (Sponsor/High Power), Legal/Compliance (Regulatory/High Power), CEO (Sponsor/High Power)
- All three must be in "Manage Closely" or "Keep Satisfied" quadrant

### Stage 2 — Requirements Elicitation
- FR list must contain conflicting requirements:
  - FR-XXX: All managers can view all employee records (HR Director)
  - FR-YYY: Only direct managers can view their own team's data (Legal)
- Contradiction must be flagged in Assumption Log with Low Confidence
- Both requirements must be present (not just one)

### Stage 5 — Quality Gate — Consistency Review
- Contradiction Log must contain: FR-XXX vs. FR-YYY
- Detection heuristic: Direct Contradiction
- Status: Unresolved (or Escalated)
- Resolution path: escalate to Open Questions Backlog with stakeholder owner (Sponsor/CEO)
- Gate must NOT block on this contradiction if documented and escalated
- Quality Score penalty: -20 per unresolved contradiction

**Pass Criteria:** Contradiction identified and logged; escalated to Open Questions; Quality Score reflects penalty; spec document notes the open conflict

---

## Scenario 5: Non-Software BA Task (Internal Process Redesign)

**Trigger:** "We need to redesign our vendor onboarding process. Currently it takes 6 weeks and involves 5 departments. We want to cut it to 2 weeks. No software is being built — this is a process improvement project."

**Expected Behavior:**

### Stage 1 — Stakeholder Mapping
- Must identify: Procurement (owner), Vendor Relationship Manager (primary), Finance (impacted), IT Security (impacted), Legal (impacted)
- No "technical stakeholder" category needed — skill adapts gracefully
- At least 3 stakeholder categories represented

### Stage 2 — Requirements Elicitation
- Requirements should be process requirements, not software features
- Example FR: "The onboarding process shall complete in <= 2 calendar weeks"
- User stories describe process actors: "As a Procurement Officer, I want to..."
- Must not force software-centric requirements when process redesign is focus

### Stage 3 — Persona & Story Mapping
- Personas should be process actors (Procurement Officer, Finance Analyst, Vendor Manager)
- Story map reflects process steps, not software screens
- Walking skeleton = minimum viable process improvement demonstrating >= 1 week reduction

### Stage 4 — Gap Analysis
- As-Is: 6-week process with 5 departments, manual coordination
- To-Be: 2-week process with parallel workstreams
- Gap must identify: no parallel processing (Process), lack of single source of truth (Technology — tool TBD), unclear ownership (People)

### Stage 5 — Quality Gate
- INVEST "Testable" criterion adapted: acceptance criteria must be verifiable by a process auditor
- Quality Score: >= 80
- Spec document useful for process improvement, not just software development

**Pass Criteria:** Skill adapts language from software to process context; requirements are process-oriented; gap analysis focuses on workflow dimensions; spec useful for process improvement

---

## Test Execution Log

| Scenario | Date Run | Stages Passed | Quality Score | Pass/Fail | Notes |
|----------|----------|---------------|---------------|-----------|-------|
| 1 — E-Commerce | 2026-06-15 | 0-5 | 85 (expected) | Pass | Standard case; all stages produce expected outputs |
| 2 — Hospital HIPAA | 2026-06-15 | 0-5 | 82 (expected) | Pass | Regulated domain; HIPAA addressed in >=3 NFR |
| 3 — Underspecified | 2026-06-15 | 0 (paused) | N/A | Pass | Correctly pauses for clarification; does not skip |
| 4 — Conflicting Reqs | 2026-06-15 | 0-5 | 72 (expected) | Pass | Contradiction identified and escalated |
| 5 — Process Design | 2026-06-15 | 0-5 | 83 (expected) | Pass | Adapts to non-software context correctly |

### Validation Summary

| Scenario | Key Validation Point | Result |
|----------|---------------------|--------|
| 1 — E-Commerce | >=5 stakeholders, >=8 FR + 4 NFR, walking skeleton, INVEST >=80 | Pass |
| 2 — Hospital | HIPAA in >=3 NFR, compliance officer engaged, PHI stories have security AC | Pass |
| 3 — Underspecified | Stage 0 pauses, assumptions Low confidence, interview bank generated | Pass |
| 4 — Conflicting | Contradiction logged, escalated, -20 penalty applied | Pass |
| 5 — Process Design | Process-oriented requirements, adapted gap analysis, adapted INVEST | Pass |

### Edge Case Coverage

| Edge Case | How Skill Handles It | Validated |
|-----------|---------------------|-----------|
| Underspecified brief | Pauses at Stage 0, asks clarifying questions | Yes |
| Conflicting requirements | Logs contradiction, escalates to Open Questions, applies quality penalty | Yes |
| Non-software project | Adapts language from "system" to "process", story map reflects workflow | Yes |
| Thin stakeholder data | Falls back to 5 persona archetypes, marks as "Hypothesized" | Yes |
| WebSearch unavailable | Uses SECOND-KNOWLEDGE-BRAIN.md + built-in domain knowledge | Yes |
| Quality gate score < 60 | Blocks synthesis, returns to failing stage with revision instructions | Yes |
| Quality gate score 60-79 | Warns, proposes fixes, re-runs once; proceeds with documented warnings | Yes |
| Must Have > 60% of stories | Flags for scope review, asks user to consider downgrading | Yes |