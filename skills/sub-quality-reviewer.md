---
name: sub-quality-reviewer
description: Validate all requirements artifacts for completeness, consistency, INVEST principle compliance, and MoSCoW prioritization. Produces a quality score (0–100) and blocks final synthesis if gates fail.
---

## Purpose

Requirements quality directly determines development outcomes. This sub-skill acts as the BA's final quality gate before the specification document is synthesized. It enforces four quality dimensions: INVEST compliance (story well-formedness), MoSCoW prioritization (scope clarity), completeness (nothing missing), and consistency (no contradictions).

---

## Inputs

- Stakeholder Register (from sub-stakeholder-mapper)
- Requirements List: FR + NFR (from sub-requirements-gatherer)
- Assumption Log + Open Questions (from sub-requirements-gatherer)
- User Personas + Story Map + Story Backlog (from sub-persona-story-mapper)
- Gap Analysis Table (from sub-gap-analyzer)

---

## Execution Steps

### Step 1: MoSCoW Prioritization

Tag every user story in the backlog with one MoSCoW priority. Apply the decision rules below:

| Priority | Decision Rule |
|----------|--------------|
| **Must Have** | Without this story, the system cannot function OR delivers no value to the primary persona in their core journey; or a regulatory/legal requirement mandates it |
| **Should Have** | Highly valuable but the system can launch without it; workaround exists temporarily; strong stakeholder demand |
| **Could Have** | Nice to have; adds polish or secondary value; only included if time/budget permits |
| **Won't Have (this iteration)** | Explicitly out of scope for this release; may be deferred to a future version; document the reason |

**MoSCoW Table:**

| Story ID | Story (short form) | Persona | MoSCoW | Rationale |
|----------|--------------------|---------|--------|-----------|
| US-001 | Filter orders by status | Maya | Must Have | Core workflow — system unusable without it |
| US-002 | Export orders to CSV | Maya | Should Have | High demand; workaround: manual copy-paste |
| US-003 | Dark mode UI | Arjun | Could Have | Aesthetic preference; no functional impact |
| US-004 | AI-powered reorder prediction | Maya | Won't Have | Out of scope v1; requires ML infrastructure |

**MoSCoW rules:**
- Must Have stories should represent ≤ 60% of total stories (if >60%, scope is too large — flag for review)
- All Must Have stories must have acceptance criteria
- "Won't Have" items must include a documented reason
- Every story must have exactly one MoSCoW tag — no untagged stories

### Step 2: INVEST Validation

For every **Must Have** and **Should Have** story, validate against all 6 INVEST criteria:

**INVEST Scoring Table:**

| Story ID | I — Independent | N — Negotiable | V — Valuable | E — Estimable | S — Small | T — Testable | Score | Pass? |
|----------|----------------|----------------|-------------|---------------|-----------|--------------|-------|-------|
| US-001 | Pass | Pass | Pass | Pass | Pass | Pass | 6/6 | ✓ |
| US-005 | Fail* | Pass | Pass | Pass | Fail** | Pass | 4/6 | ✗ |

*US-005 fails Independent — it can only be built after US-001 (must resequence or split)
**US-005 fails Small — too large for one sprint (must split)

**INVEST Criteria Definitions:**

| Criterion | Pass | Fail |
|-----------|------|------|
| **Independent** | Story can be developed and deployed without requiring another story to be done first | Story has a hard dependency on another incomplete story |
| **Negotiable** | Scope details can be discussed and refined with stakeholders; story is not a rigid specification | Story is rigid with no room for implementation choices or discussion |
| **Valuable** | Delivers measurable value to a user or business stakeholder | Internal technical task with no user-visible benefit |
| **Estimable** | Development team can provide a reasonable size estimate based on the information given | Too vague, complex, or unknown to estimate |
| **Small** | Can be completed in one sprint (typically ≤ 2 weeks of effort) | Would take more than one sprint alone; must be split |
| **Testable** | Acceptance criteria can be written and objectively verified through testing | Cannot be objectively verified; no clear pass/fail condition |

**Required actions for Fail stories:**
- **Independence failure:** Split the story into independent parts, or resequence so dependencies are built first; document the dependency chain
- **Smallness failure:** Split into 2+ smaller stories; each must still deliver standalone value
- **Testability failure:** Add or rewrite acceptance criteria until they are verifiable; if impossible, flag as a technical spike instead
- **Value failure:** Review with stakeholder; may be an implementation task — convert to a technical spike or remove from backlog
- **Negotiable failure:** Rewrite the story to focus on the outcome, not the implementation; add "so that" clause
- **Estimable failure:** Schedule a technical spike to gather information; rewrite story once estimate is possible

**INVEST Pass Threshold:** A story passes INVEST validation if it scores ≥ 4/6 criteria. Stories scoring < 4/6 must be rewritten before proceeding.

### Step 3: Completeness Checklist

Run through each item and mark Pass/Fail:

| Check | Criterion | Result | Notes |
|-------|-----------|--------|-------|
| C-01 | Every FR has ≥ 1 user story | Pass/Fail | FR-007 uncovered |
| C-02 | Every NFR is documented as constraint or NFR story | Pass/Fail | NFR-002 (security) not in backlog |
| C-03 | Every stakeholder has ≥ 1 story addressing their key concern | Pass/Fail | SH-003 concern unaddressed |
| C-04 | Walking skeleton stories all have AC | Pass/Fail | US-003 missing AC |
| C-05 | All Must Have stories have ≥ 2 AC | Pass/Fail | US-001 only has 1 AC |
| C-06 | Assumption log has validation method for all Low confidence assumptions | Pass/Fail | ASM-004 missing method |
| C-07 | Open questions backlog is prioritized | Pass/Fail | All OQ priorities set |
| C-08 | Gap analysis covers all 3 dimensions (People/Process/Technology) | Pass/Fail | Only 2 dimensions covered |
| C-09 | All personas have goals, frustrations, and a quote | Pass/Fail | Persona 2 missing quote |
| C-10 | Won't Have items have documented rationale | Pass/Fail | US-010 rationale missing |

Completeness Score = (Pass items / 10) × 100

### Step 4: Consistency Review — Contradiction Detection Heuristics

Scan the entire requirements set for contradictions using these detection heuristics:

**Contradiction Types and Detection Rules:**

1. **Direct Contradiction:** Two requirements that cannot both be satisfied simultaneously.
   - *Detection rule:* Search for FR/NFR pairs where one requires X and another requires not-X, or where achieving one would prevent the other.
   - *Example:* FR-003 "Real-time data sync" vs. NFR-003 "Offline-first capability"

2. **Story vs. NFR Conflict:** A user story that contradicts a stated non-functional requirement.
   - *Detection rule:* For each story, check if its implementation would violate any NFR.
   - *Example:* Story "Admin can view all employee records" vs. NFR "Only direct managers can access team data"

3. **Gap-Bridging vs. Constraint Conflict:** A bridging action that conflicts with a stated constraint.
   - *Detection rule:* Cross-reference each bridging action against the constraint log.
   - *Example:* Bridging action "Implement real-time dashboards" vs. CON-001 "Must work on legacy offline hardware"

4. **Assumption vs. Stakeholder Statement:** An assumption that contradicts an explicit stakeholder statement.
   - *Detection rule:* For each Low/Medium confidence assumption, verify it does not directly oppose what a stakeholder stated.
   - *Example:* ASM-002 "Users prefer email notifications" vs. stakeholder quote "I never read emails — send me SMS"

5. **MoSCoW Priority Mismatch:** Stories tagged with conflicting priorities relative to stakeholder influence.
   - *Detection rule:* If a Must Have story only addresses a Low-influence stakeholder's concern, or a Could Have story addresses a Definitive stakeholder's concern, flag for review.
   - *Example:* Must Have story requested only by a Monitor-quadrant stakeholder

**Contradiction Log:**

| ID | Item 1 | Item 2 | Contradiction Type | Description | Resolution | Status |
|----|--------|--------|-------------------|-------------|------------|--------|
| CON-01 | FR-003: Real-time sync | NFR-003: Offline capability | Direct Contradiction | Real-time sync and offline-first are mutually exclusive without explicit sync conflict resolution | Add conflict resolution requirement: FR-003a | Resolved |
| CON-02 | US-005: Admin can delete any user | ASM-002: GDPR soft-delete only | Story vs. NFR | Story contradicts assumed constraint | Revise US-005 to "soft-delete with 30-day recovery" | Resolved |

All contradictions must be resolved before synthesis. If resolution requires stakeholder input, add to Open Questions Backlog with status "Escalated."

### Step 5: Calculate Quality Score

```
Quality Score = weighted average across 4 dimensions:

  INVEST Compliance   = (Must/Should stories passing INVEST / total Must/Should) × 100  [Weight: 30%]
  MoSCoW Coverage     = (stories with MoSCoW tag / total stories) × 100                 [Weight: 20%]
  Completeness        = (passed completeness checks / 10) × 100                          [Weight: 30%]
  Consistency         = 100 if 0 unresolved contradictions; -20 per unresolved           [Weight: 20%]

Final Score = (INVEST × 0.30) + (MoSCoW × 0.20) + (Completeness × 0.30) + (Consistency × 0.20)
```

**Thresholds:**
- ≥ 80: Gate passes — proceed to synthesis
- 60–79: Gate warns — identify failing items; propose and apply fixes; re-run gate
- < 60: Gate blocks — significant revision required; return to affected stage

**Fail/Retry Loop Behavior:**
1. If Quality Score is 60–79 (WARN): list all failing items, propose specific fixes, apply fixes, and re-run the quality gate once.
2. If re-run still scores 60–79: proceed to synthesis with a "Quality Warnings" section in the final document.
3. If Quality Score is < 60 (BLOCK): return to the failing stage with specific revision instructions. Do NOT proceed to synthesis.
4. After revision, re-run from the failing stage forward. Maximum 2 retry cycles; on 3rd failure, produce the best possible document with all unresolved issues documented.

### Step 6: Gate Result Report

Produce a brief Quality Gate Results section:

```
QUALITY GATE RESULTS
──────────────────────────────────────────────────────────
INVEST Compliance:   [X/Y stories pass] — [score]%
MoSCoW Coverage:     [X/Y stories tagged] — [score]%
Completeness:        [X/10 checks pass] — [score]%
Consistency:         [N contradictions] — [score]%
──────────────────────────────────────────────────────────
FINAL QUALITY SCORE: [score]/100
GATE STATUS:         [PASS / WARN / BLOCK]
──────────────────────────────────────────────────────────
Issues requiring action:
  1. [Issue + proposed fix]
  2. [Issue + proposed fix]
```

---

## Outputs

1. **MoSCoW Priority Table** (all stories tagged with rationale)
2. **INVEST Validation Table** (Must/Should stories scored per criterion)
3. **Completeness Checklist** (10-item, Pass/Fail with notes)
4. **Contradiction Log** (all contradictions with resolution status)
5. **Quality Gate Results Report** (final score + gate status)

---

## Quality Gate (Self-Gate)

This sub-skill itself passes only when:
- [ ] All Must Have stories tagged with MoSCoW
- [ ] Every Must Have story has INVEST score
- [ ] All 10 completeness checks completed (Pass or Fail — no blanks)
- [ ] All contradictions either resolved or escalated to Open Questions
- [ ] Final quality score calculated and gate status declared
- [ ] If BLOCK status: specific revision instructions provided for the affected stage
- [ ] Fail/retry loop behavior defined and communicated
