---
name: sub-gap-analyzer
description: Compare the current as-is state against the desired to-be state across People, Process, and Technology dimensions. Produce a Gap Analysis Table, root cause analysis for top gaps, and bridging action recommendations.
---

## Purpose

Gap analysis identifies where the organization is today and what needs to change to reach the desired future state. Without it, requirements are disconnected from operational reality — teams build the right features for the wrong context. This sub-skill structures the gap discovery process using McKinsey 7S dimensions, impact assessment, and root cause analysis (5 Whys).

---

## Inputs

- Project brief
- Stakeholder Register (from sub-stakeholder-mapper)
- Raw Requirements List (from sub-requirements-gatherer)
- User Story Map (from sub-persona-story-mapper)

---

## Execution Steps

### Step 1: Describe the As-Is State

Capture the current state across three primary dimensions. For each dimension, write 2–5 bullet points describing how things work today:

**People (As-Is):**
- Who does what in the current workflow?
- What skills do they have?
- What manual steps do they perform?
- What are their biggest pain points?

**Process (As-Is):**
- What is the end-to-end workflow today? (numbered steps)
- Where are the handoffs between people or systems?
- Where does the process break down or slow down?
- What workarounds exist?

**Technology (As-Is):**
- What tools/systems are currently used?
- How are they connected (or not)?
- What data exists today and where is it stored?
- What are the technical limitations?

Format as a structured description:
```
AS-IS STATE
─────────────────────────────────────────────────────
PEOPLE:
  • [bullet]
  • [bullet]

PROCESS:
  • Step 1: [current step]
  • Step 2: [current step]
  ...
  Pain Points: [list key friction points]

TECHNOLOGY:
  • [tool/system]: [role in current process]
  • [tool/system]: [limitation]
─────────────────────────────────────────────────────
```

### Step 2: Describe the To-Be State

Describe the desired future state derived from the requirements and story map. Use the same three-dimension structure:

**People (To-Be):**
- What roles will exist and what will they do?
- What new skills or training are needed?
- What manual work will be eliminated or reduced?

**Process (To-Be):**
- What does the end-to-end workflow look like after the project?
- Where do the new system features change the flow?
- What approvals, handoffs, or steps are automated?

**Technology (To-Be):**
- What systems will the project deliver or replace?
- How will they integrate?
- What data will be available and in what format?

Format as a structured description (same template as As-Is, labeled TO-BE STATE).

### Step 3: Identify Gaps

A gap is any difference between As-Is and To-Be that requires deliberate action. Gaps occur at:
- **People gaps:** Missing skills, changed roles, training needs, organizational resistance
- **Process gaps:** Changed workflows, eliminated steps, new approvals, missing procedures
- **Technology gaps:** Missing systems, integration needs, data migration, decommissioning, infrastructure gaps

For each gap, assign:
- **Impact:** High (blocks a Must Have requirement) / Medium (affects Should Have) / Low (affects Could Have)
- **Type:** People / Process / Technology
- **Root Cause Known?** Yes/No

**Gap Analysis Table:**

| Gap ID | Description | Type | Affected Requirement | Impact | Root Cause Known? | Priority |
|--------|-------------|------|---------------------|--------|------------------|----------|
| GAP-001 | No centralized order tracking system exists; orders tracked manually in spreadsheets | Technology | FR-005, FR-006 | High | Yes | 1 |
| GAP-002 | Operations team lacks training on data export workflows | People | FR-009 | Medium | No | 3 |
| GAP-003 | Current approval process requires 3 manual sign-offs adding 2-day delay | Process | NFR-001 (performance) | High | Yes | 2 |

### Step 4: Root Cause Analysis (Top 3 Gaps)

For the top 3 gaps by impact and priority, conduct a **5 Whys Root Cause Analysis**:

```
Gap: GAP-001 — No centralized order tracking
Why 1: Orders are tracked in spreadsheets
  → Why 2: No order management system was purchased
  → Why 3: Previous budget cycles prioritized other systems
  → Why 4: Order volume was low enough that spreadsheets sufficed
  → Why 5: Business grew faster than infrastructure investment

Root Cause: Infrastructure investment lagged behind business growth;
            no scalable system was provisioned proactively.

Implication: New system must support data migration from existing
             spreadsheets and handle 5× current order volume.
```

**Root Cause Analysis Rules:**
- Always ask "Why?" 5 times or until a systemic cause is found
- Root causes should be actionable — not "because we didn't have money" but "investment prioritization process did not scale with business growth"
- Each root cause must have at least one implication for the project
- If root cause is organizational/political, note it and propose a mitigation rather than a fix

### Step 5: Bridging Actions

For each gap, propose a specific bridging action — the step needed to close the gap. Bridging actions become inputs to the project's work breakdown or sprint backlog.

| Gap ID | Bridging Action | Owner | Timeline | Dependencies |
|--------|----------------|-------|----------|-------------|
| GAP-001 | Implement order management module per FR-005/006; migrate historical data | Dev Team | Sprints 1–3 | FR-005 must-have |
| GAP-002 | Conduct 2-hour training workshop for operations team before UAT | Product Owner | Week before UAT | Training materials |
| GAP-003 | Redesign approval workflow to use system-based digital sign-off (1-step) | Business Analyst + Sponsor | Sprint 2 | Process owner buy-in |

**Bridging Action Rules:**
- Every High-impact gap must have a bridging action with a named owner
- Timeline must reference a sprint or week number (not "TBD")
- Dependencies must be identified; if unknown, mark as "To be confirmed"
- For People gaps, prefer training + documentation; avoid "hire more people" unless explicitly requested
- For Process gaps, prefer redesign + automation; for Technology gaps, prefer build + integrate + migrate

### Step 6: Impact Matrix Summary

Produce a visual impact matrix showing gap priority by type and impact:

```
IMPACT MATRIX
──────────────────────────────────────────────────────────
             │ HIGH IMPACT  │ MEDIUM IMPACT │ LOW IMPACT
─────────────┼──────────────┼───────────────┼──────────────
TECHNOLOGY   │ GAP-001      │               │
PROCESS      │ GAP-003      │               │
PEOPLE       │              │ GAP-002       │
──────────────────────────────────────────────────────────
Priority action: GAP-001, GAP-003 (both High — must close before sprint 1)
```

---

## Outputs

1. **As-Is State Description** (People / Process / Technology, structured format)
2. **To-Be State Description** (same structure)
3. **Gap Analysis Table** (Gap ID, Description, Type, Affected Requirement, Impact, Priority)
4. **Root Cause Analysis** for top 3 gaps (5 Whys format)
5. **Bridging Action Table** (Gap ID, Action, Owner, Timeline, Dependencies)
6. **Impact Matrix** (visual summary)

---

## Quality Gate

Before passing to quality review:
- [ ] At least 3 gaps identified and documented
- [ ] Every gap has an impact level (High/Medium/Low) and type (People/Process/Technology)
- [ ] Root cause analysis completed for the top 3 highest-impact gaps
- [ ] Every gap has a bridging action with an owner and timeline
- [ ] Impact matrix produced and readable
- [ ] All gaps traceable to ≥ 1 requirement from the FR/NFR list
- [ ] As-Is and To-Be states cover all three dimensions (People, Process, Technology)
- [ ] No "TBD" or "Unknown" in root cause statements
