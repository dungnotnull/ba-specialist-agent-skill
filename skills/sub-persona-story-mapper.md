---
name: sub-persona-story-mapper
description: Generate BMAD-aligned user personas from stakeholder data, then construct a user story map with walking-skeleton slice identification and full acceptance criteria in Given/When/Then format.
---

## Purpose

This sub-skill transforms stakeholder and requirements data into behavioral user artifacts: richly detailed personas and a structured user story map. It follows BMAD methodology (grounded in Jeff Patton's story mapping practice) to ensure stories emerge from user behavior — not arbitrary feature lists — and that a walking skeleton MVP slice is explicitly identified.

---

## Inputs

- Stakeholder Register (from sub-stakeholder-mapper)
- Functional & Non-Functional Requirements (from sub-requirements-gatherer)
- Project brief and domain context

---

## Execution Steps

### Step 1: Derive User Personas

From the stakeholder register, identify the 2–4 most important user-facing roles (Primary Users and Key Secondary Users). For each, construct a persona card:

**Persona Card Format:**

```
════════════════════════════════════════════════════════════════
PERSONA: [Fictional Name] — [Role Title]
════════════════════════════════════════════════════════════════
Background:   [2-3 sentences about their role, context, typical day]
Goals:        1. [Primary goal]
              2. [Secondary goal]
              3. [Tertiary goal]
Frustrations: 1. [Top pain point with current solution]
              2. [Second pain point]
Tech Comfort: [Low / Medium / High] — [one sentence explaining level]
Quote:        "[A sentence this persona might say in an interview]"
Key Stories:  [FR IDs this persona drives: FR-001, FR-004, ...]
════════════════════════════════════════════════════════════════
```

**Persona derivation rules:**
- Each persona maps to ≥ 1 stakeholder category
- Personas are fictional composites — not real people
- Tech Comfort is grounded in the stakeholder's known background
- Quote captures a real frustration or aspiration, not marketing language
- Every functional requirement should be traceable to at least one persona

#### Persona Archetypes (Reference for BA)

Use these 5 archetypes to guide persona creation when data is thin. Each archetype represents a common stakeholder pattern that appears across domains:

**1. The Skeptic (Low Tech Comfort)**
- *Profile:* Has seen failed technology projects before. Fears disruption to existing workflows that already work. Values reliability, stability, and simplicity over novelty.
- *Typical Role:* Long-tenured operations staff, administrative assistants, field workers.
- *Key Concern:* "Will this new system break what already works?"
- *BA Strategy:* Emphasize training, phased rollout, and parallel run periods. Provide fallback procedures. Show concrete evidence of reliability before asking for adoption.

**2. The Power User (High Tech Comfort)**
- *Profile:* Lives in the system daily. Craves efficiency, keyboard shortcuts, batch operations, and integration with other tools. Dislikes "hand-holding" UIs that slow experts down.
- *Typical Role:* Data analysts, experienced operators, dev leads, system administrators.
- *Key Concern:* "Don't make me click five times for something I do fifty times a day."
- *BA Strategy:* Include power-user stories (bulk actions, API access, keyboard navigation). Interview them early to capture edge cases and hidden requirements.

**3. The Executive (Medium Tech Comfort)**
- *Profile:* Makes decisions based on dashboards and KPIs. Has very limited time. Needs information aggregated, actionable, and immediately understandable. Rarely uses the system directly beyond reports.
- *Typical Role:* CEO, VP, department heads, board members.
- *Key Concern:* "Give me the three numbers I need to make a decision, not a spreadsheet."
- *BA Strategy:* Focus stories on reporting, dashboards, and decision-support features. Keep their persona stories high-level and outcome-oriented.

**4. The Compliance Officer (Medium Tech Comfort)**
- *Profile:* Focuses on risk, audit trails, and regulatory adherence over usability or speed. Needs every action traceable. Willing to trade convenience for control. Often the strongest advocate for non-functional requirements.
- *Typical Role:* Compliance managers, auditors, data protection officers, risk analysts.
- *Key Concern:* "Can you prove this process was followed correctly for every single record?"
- *BA Strategy:* Include audit-trail stories, data-retention stories, and role-permission stories. Treat their NFR concerns as Must Have. Involve them early in security and privacy requirements.

**5. The New Joiner (Low-to-Medium Tech Comfort)**
- *Profile:* Recently onboarded or unfamiliar with the domain. Needs intuitive onboarding, clear labeling, discoverable features, and contextual help. Makes mistakes frequently during the learning phase. Represents the "first-time user" perspective.
- *Typical Role:* New employees, interns, recently promoted staff, external contractors.
- *Key Concern:* "How do I even get started? I don't know the jargon yet."
- *BA Strategy:* Include onboarding stories, tooltip/help stories, and error-recovery stories. Test with this persona for usability. Ensure walking skeleton covers first-time use flows.

### Step 2: Identify User Activities (Story Map Row 1)

Activities are high-level things a persona does to achieve their goal. They are not features — they are user behaviors.

For each primary persona, list 3–6 activities:
- Use verb-noun format: "Manage Orders", "Track Shipment", "Generate Report"
- Activities should span the full user journey from first contact to goal achievement
- Order activities left-to-right in temporal sequence (narrative flow)

**Example Activity Map (e-commerce):**
```
[Browse Products] → [Select & Configure] → [Checkout] → [Track Order] → [Return/Review]
```

### Step 3: Decompose into Tasks (Story Map Row 2)

Under each activity, list 2–5 specific tasks the persona performs:
- Tasks are also verb-noun: "Search by category", "Apply discount code", "View order status"
- Tasks are at the level of individual screen interactions or process steps

**Example Task Breakdown:**
```
[Browse Products]
  ├── Search by keyword
  ├── Filter by category
  ├── View product detail
  └── Save to wishlist
```

### Step 4: Write User Stories (Story Map Rows 3+)

Under each task, write 1–3 user stories. Follow the BMAD format strictly:

**Story Format:**
```
As a [Persona Name],
I want to [specific action or capability],
so that [concrete benefit or outcome].
```

**Rules:**
- Use the persona's actual name (not "user" or "customer")
- The "want" clause must be specific and testable — not vague ("I want a good experience" is invalid)
- The "so that" clause must name a real benefit — not restate the want

**Acceptance Criteria (Given/When/Then):**

For every user story in the Must Have and Should Have layers, write ≥ 2 acceptance criteria:

```
Story: As Maya (Operations Manager), I want to filter orders by status, so that I can quickly identify orders needing action.

Acceptance Criteria:
  AC-1: Given I am on the Orders page,
        When I select "Pending" from the Status filter,
        Then only orders with Pending status are displayed.

  AC-2: Given I have applied a filter,
        When I click "Clear Filters",
        Then all orders are shown and no filter is active.

  AC-3: Given no orders match the selected filter,
        When the filter is applied,
        Then I see a "No orders found" message with a suggestion to change filters.
```

### Step 5: Identify the Walking Skeleton

The **Walking Skeleton** is the thinnest possible version of the system that demonstrates end-to-end functionality. It is the MVP slice.

Selection criteria for walking skeleton stories:
1. Covers the most critical user journey from start to finish
2. Each persona's primary goal can be achieved through at least one story
3. Each major system component is touched at least once
4. Delivers demonstrable value to the primary persona
5. Is small enough to be completed in 1–2 sprints

Mark walking skeleton stories with the tag: `[WS]`

Present the walking skeleton as a named release slice:
```
Walking Skeleton (Sprint 0–1 Release):
  [WS] Story 1 → [WS] Story 2 → [WS] Story 3 → [WS] Story 4
  "End-to-end: [Persona] can [complete main journey] without errors."
```

### Step 6: Compile Story Backlog

Collect all stories into a structured backlog table:

| Story ID | Persona | Story | Layer | AC Count | Linked FR | Notes |
|----------|---------|-------|-------|----------|-----------|-------|
| US-001 | Maya | As Maya, I want to filter orders by status... | Must | 3 | FR-001 | Core path |

---

## User Story Examples (Reference for BA)

Below are 10 high-quality stories with full acceptance criteria across different domains. Use these as templates for writing stories in any project:

**1. E-commerce (Payment)**
- Story: As Sarah (Customer), I want to save my credit card details securely, so that I can checkout faster in future purchases.
- AC-1: Given I am on the payment page, When I check "Save this card", Then the card is tokenized and stored using PCI-DSS-compliant encryption.
- AC-2: Given I am a returning user, When I reach payment, Then my saved card (masked: XXXX-XXXX-XXXX-1234) is presented as a pre-selected option.
- AC-3: Given I select a saved card, When I confirm payment, Then the transaction processes without requiring re-entry of card details.

**2. Fintech (KYC)**
- Story: As Marcus (Compliance Officer), I want to flag accounts with mismatched ID and Address, so that I can investigate potential fraud.
- AC-1: Given a new account registration, When the address verification service returns "No Match", Then the account status is set to "Pending Review" and a flag is created.
- AC-2: Given I am in the Review Dashboard, When I open a flagged account, Then the specific mismatch reason is highlighted in red with a link to the source documents.
- AC-3: Given a flagged account, When I click "Escalate", Then the case is assigned to a senior compliance analyst and a timestamp is recorded.

**3. HealthTech (Telemedicine)**
- Story: As Dr. Chen (Physician), I want to see the patient's last 3 vitals in a trend graph, so that I can quickly assess their health stability.
- AC-1: Given I open a patient profile, When I view the Vitals tab, Then a line graph shows the last 3 recorded vital measurements with dates.
- AC-2: Given a vital reading exceeds the normal threshold, When the graph renders, Then that data point is highlighted in red with a warning icon.
- AC-3: Given I hover over a data point, When the tooltip appears, Then the exact value, date, and time of the measurement are displayed.

**4. LogiTech (Route Optimization)**
- Story: As Leo (Driver), I want to receive an updated route in real-time based on traffic conditions, so that I can maintain my delivery window.
- AC-1: Given I am on an active route, When a traffic jam is detected on the current path, Then a notification suggests an alternative route with estimated time savings.
- AC-2: Given I accept the new route, When the map updates, Then the estimated arrival time is recalculated and the turn-by-turn directions reflect the new path.
- AC-3: Given I decline the alternative route, When I continue on the original path, Then the system logs my decision and adjusts the arrival estimate accordingly.

**5. GovTech (Permits)**
- Story: As Elena (Applicant), I want to upload a PDF of my site plan, so that the city can review my building permit application.
- AC-1: Given I am on the application page, When I upload a file larger than 20MB, Then I receive an error: "File size exceeds the 20MB limit. Please compress and try again."
- AC-2: Given I upload a valid PDF under 20MB, When I click submit, Then the file is linked to my application ID and a confirmation receipt is generated.
- AC-3: Given I upload a non-PDF file, When the system validates the format, Then an error message states "Only PDF files are accepted" and the upload is rejected.

**6. Enterprise (Audit)**
- Story: As Julian (Auditor), I want to export the full change log for a specific record, so that I can verify the audit trail for a regulator.
- AC-1: Given I search for Record X, When I click "Export Audit Log", Then a CSV is generated containing all timestamps, user IDs, and action types for that record.
- AC-2: Given a record has no changes, When I export, Then the CSV contains only the creation entry with a note: "No subsequent modifications recorded."
- AC-3: Given I export a log with more than 10,000 entries, When the file is generated, Then it is paginated into multiple sheets and a summary dashboard is included at the top.

**7. SaaS (Onboarding)**
- Story: As Mia (New User), I want a guided tour of the dashboard, so that I can understand the core features without reading a manual.
- AC-1: Given I log in for the first time, When I enter the dashboard, Then a highlight box appears over the "Create Project" button with the text "Start by creating your first project."
- AC-2: Given I click "Skip Tour", When the tour closes, Then a "Help" button remains visible in the top navigation for later access.
- AC-3: Given I complete all tour steps, When the tour finishes, Then a checkmark badge appears on my profile indicating onboarding is complete.

**8. B2B (Inventory)**
- Story: As Sam (Warehouse Manager), I want to receive an alert when stock drops below the safety threshold, so that I can reorder before stock-out.
- AC-1: Given a product's current stock is 11 units and the threshold is 10, When a sale of 2 units occurs, Then a notification is sent to the Manager and the item is flagged "Low Stock" in the dashboard.
- AC-2: Given I set a new threshold for Product Y, When I click save, Then the alert trigger is updated immediately and the new threshold is displayed.
- AC-3: Given multiple products are below threshold, When the daily alert runs, Then a consolidated email lists all low-stock items sorted by urgency (lowest stock first).

**9. EdTech (LMS)**
- Story: As Professor Plum (Educator), I want to assign a specific reading list to a student group, so that they have the required material for the week.
- AC-1: Given I am in the Course Manager, When I select a group and a reading list, Then all students in that group receive a notification with the list title and due date.
- AC-2: Given a student is in two overlapping groups, When they check their readings, Then they see a merged and deduplicated list of all assigned materials with the earliest due date highlighted.
- AC-3: Given I remove a reading from the list, When I save the change, Then the updated list is pushed to all group members and the removed item is flagged as "Removed by instructor."

**10. AI Platform (Prompt Engineering)**
- Story: As Dev (Developer), I want to save a "Golden Prompt" template, so that I can replicate high-quality outputs consistently.
- AC-1: Given I have a prompt that produces good results, When I click "Save as Template", Then it is stored in the Template Library with a name, category, and version number.
- AC-2: Given I select a template from the Library, When it loads into the editor, Then all placeholder variables are highlighted in yellow for me to fill in before execution.
- AC-3: Given I update an existing template, When I save, Then a new version is created and the previous version remains accessible via the version history.

---

## BMAD Story Mapping Template

Use this template when constructing user story maps. It follows the Jeff Patton story mapping methodology adapted for BMAD:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        BMAD USER STORY MAP                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ACTIVITIES (Row 1 — Narrative Flow, Left→Right):                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │ Activity │  │ Activity │  │ Activity │  │ Activity │               │
│  │    A     │  │    B     │  │    C     │  │    D     │               │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘               │
│       │              │              │              │                     │
│  TASKS (Row 2):                                                        │
│  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐              │
│  │Task A.1  │  │Task B.1  │  │Task C.1  │  │Task D.1  │              │
│  │Task A.2  │  │Task B.2  │  │Task C.2  │  │Task D.2  │              │
│  │Task A.3  │  │          │  │          │  │          │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       │              │              │              │                     │
│  STORIES (Rows 3+ — Per Task, stacked vertically):                     │
│  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐             │
│  │ US-001   │  │ US-004   │  │ US-007   │  │ US-010   │             │
│  │ US-002   │  │ US-005   │  │ US-008   │  │ US-011   │             │
│  │ US-003   │  │ US-006   │  │ US-009   │  │          │             │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘             │
│                                                                         │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
│  WALKING SKELETON SLICE (MVP — stories marked [WS]):                   │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │ [WS] US-001 → [WS] US-004 → [WS] US-007 → [WS] US-010     │      │
│  │ "End-to-end: Primary persona completes core journey"        │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                         │
│  PRIORITIZATION BACKLOG (below the line):                               │
│  Must Have:  US-001, US-004, US-007, US-010                            │
│  Should Have: US-002, US-005, US-008, US-011                            │
│  Could Have:  US-003, US-006, US-009                                    │
│  Won't Have:  US-012 (future: advanced reporting)                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Walking Skeleton Identification Rules:**
1. Select exactly one story per activity column (the most critical path story)
2. The walking skeleton must form a complete left-to-right narrative
3. Each persona must be able to complete at least one core goal through the skeleton
4. Walking skeleton stories are automatically tagged as Must Have
5. Total walking skeleton stories should be ≤ 40% of total stories

---

## Quality Gate

Before passing to backlog:
- [ ] Every persona has goals, frustrations, and a quote
- [ ] Every user story follows "As a / I want / So that"
- [ ] All Must Have stories have ≥ 2 AC in Given/When/Then
- [ ] Walking skeleton is clearly identified as a sequence of stories
- [ ] Every story is traceable to at least one FR/NFR
- [ ] No "generic" personas (e.g., "The User")
- [ ] No "placeholder" acceptance criteria
- [ ] Story map has at least 3 activities in narrative flow
- [ ] Walking skeleton covers end-to-end from first activity to last

---

## Graceful Degradation

If stakeholder data is thin:
- Derive personas from the 5 domain archetypes above (The Skeptic, The Power User, The Executive, The Compliance Officer, The New Joiner)
- Generate a "Hypothesized Personas" list and mark them as such
- Note: "[Personas derived from archetypes — stakeholder validation required before finalized story map]"
