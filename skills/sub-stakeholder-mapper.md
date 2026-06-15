---
name: sub-stakeholder-mapper
description: Identify, classify, and map all project stakeholders by role, influence level, interest level, and engagement strategy. Produces a Stakeholder Register and Power/Interest Grid.
---

## Purpose

This sub-skill systematically identifies every person, group, or organization that affects or is affected by the project. It classifies them using the Stakeholder Salience Model (Mitchell et al., 1997) and the Power/Interest Grid, then assigns an engagement strategy to each.

---

## Inputs

- Project brief (description, domain, goal)
- Any named parties mentioned by the user
- Domain context (from WebSearch if needed)

---

## Execution Steps

### Step 1: Brainstorm Stakeholder Universe

Generate a complete list of potential stakeholders across these categories:

| Category | Description | Examples |
|----------|-------------|---------|
| **Sponsor / Decision Maker** | Funds or authorizes the project | CEO, Product Owner, Business Owner, Board Member |
| **Primary Users** | Directly use the system daily | End users, customers, operators, clinicians, warehouse staff |
| **Secondary Users** | Use outputs or reports from the system | Managers, analysts, auditors, executives receiving dashboards |
| **Subject Matter Experts (SME)** | Provide domain knowledge | Domain specialists, compliance officers, legal counsel, clinicians |
| **Technical Stakeholders** | Build or maintain the system | Developers, DevOps, architects, DBAs, QA engineers |
| **Impacted Parties** | Affected by the project but don't use it | Departments whose workflows change, data owners, external vendors |
| **Regulatory / External** | External authorities with requirements | Regulatory bodies (HIPAA, GDPR, SOX), industry standards groups, government agencies |
| **Customers / End Beneficiaries** | Ultimate recipients of value | If different from users — e.g., patients in a hospital system |

### Step 2: Classify Each Stakeholder

For each stakeholder, assign:
- **Influence:** High (can block/change the project) / Medium (can influence) / Low (minimal impact)
- **Interest:** High (directly affected, actively engaged) / Medium (somewhat affected) / Low (peripheral awareness)
- **Salience Class** (Mitchell et al., 1997):
  - **Definitive:** High power + High legitimacy + High urgency → Must always engage
  - **Dominant:** High power + High legitimacy → Always engage
  - **Dependent:** High legitimacy + High urgency → Engage and protect
  - **Dangerous:** High power + High urgency → Monitor and manage carefully
  - **Discretionary:** High legitimacy only → Keep informed
  - **Dormant:** High power only → Monitor
  - **Demanding:** High urgency only → Minimal engagement

### Step 3: Power/Interest Grid Placement

Categorize each stakeholder into one of four quadrants:

```
              HIGH INTEREST
                    |
    KEEP SATISFIED  |  MANAGE CLOSELY
                    |
HIGH POWER ─────────┼───────────────── LOW POWER
                    |
    MONITOR         |  KEEP INFORMED
                    |
              LOW INTEREST
```

### Step 4: Assign Engagement Strategy

| Quadrant | Strategy |
|----------|---------|
| Manage Closely (High Power, High Interest) | Active collaboration; regular status meetings; co-design sessions; include in all major decisions |
| Keep Satisfied (High Power, Low Interest) | Regular briefings; consult on major decisions; avoid surprises; send executive summaries |
| Keep Informed (Low Power, High Interest) | Regular updates; feedback channels; user testing invitations; newsletters |
| Monitor (Low Power, Low Interest) | Periodic check-ins; include in announcements; observe for changes in interest level |

### Step 5: Identify Key Concern Per Stakeholder

For each stakeholder, state their primary concern in one sentence:
- What do they fear most about this project?
- What do they want most from this project?

### Step 6: Produce Stakeholder Register

Format as a table:

| ID | Name/Role | Category | Influence | Interest | Quadrant | Salience Class | Key Concern | Engagement Strategy |
|----|-----------|----------|-----------|----------|----------|----------------|-------------|---------------------|
| SH-001 | Product Owner | Sponsor | High | High | Manage Closely | Definitive | On-time, on-budget delivery | Weekly status meeting + co-prioritization sessions |
| SH-002 | End User | Primary User | Low | High | Keep Informed | Dependent | Ease of use, minimal disruption | UAT sessions, feedback surveys |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## Stakeholder Classification Examples (Reference for BA)

Below are real-world classification examples across different domains. Use these as templates when classifying stakeholders for any project:

| Domain | Stakeholder | Category | Influence | Interest | Quadrant | Salience Class | Key Concern | Strategy |
|--------|------------|----------|-----------|----------|----------|----------------|-------------|----------|
| E-commerce | Logistics Manager | Impacted Party | High | High | Manage Closely | Definitive | Last-mile delivery efficiency | Weekly sync on fulfillment SLAs |
| E-commerce | Customer Service Rep | Primary User | Low | High | Keep Informed | Dependent | Quick access to order status for customer calls | Training sessions, feedback loop |
| E-commerce | CFO | Sponsor | High | Medium | Keep Satisfied | Dominant | ROI within 18 months | Monthly executive dashboard |
| Fintech | Compliance Officer | SME | High | High | Manage Closely | Definitive | Regulatory reporting accuracy | Co-design compliance features, weekly review |
| Fintech | Retail Investor | End Beneficiary | Low | High | Keep Informed | Dependent | Transparent fee disclosure and real-time data | In-app notifications, beta testing |
| Fintech | Bank Regulator | Regulatory | High | Low | Keep Satisfied | Dominant | Adherence to KYC/AML regulations | Proactive compliance reports, audit readiness |
| Healthcare | Nurse Practitioner | Primary User | Medium | High | Keep Informed | Dependent | Patient data entry overhead reducing care time | Workflow observation, usability testing |
| Healthcare | Hospital CIO | Technical | High | Medium | Keep Satisfied | Dominant | System integration with existing EHR | Architecture review meetings |
| Healthcare | Patient | End Beneficiary | Low | High | Keep Informed | Dependent | Access to own records and appointment self-service | Patient portal feedback, survey |
| GovTech | Budget Committee | Sponsor | High | Low | Keep Satisfied | Dormant | Budget alignment with policy objectives | Quarterly financial reports |
| GovTech | Citizens | End Beneficiary | Low | Medium | Monitor | Discretionary | Service accessibility and transparency | Public feedback portal, town halls |
| GovTech | IT Security Officer | Technical | High | High | Manage Closely | Definitive | Data protection and cyber resilience | Security review board, threat modeling |
| SaaS | Power User / Admin | Primary User | Medium | High | Keep Informed | Dependent | Keyboard shortcuts, API access, bulk actions | Power user advisory panel |
| SaaS | Sales VP | Sponsor | High | Medium | Keep Satisfied | Dominant | Pipeline visibility and forecast accuracy | CRM dashboard demos |
| Internal Process | Department Head | Sponsor | High | High | Manage Closely | Definitive | Process efficiency within their department | Workshop facilitation, co-ownership of KPIs |
| Internal Process | Frontline Staff | Primary User | Low | High | Keep Informed | Dependent | Simpler workflows, less manual data entry | Process observation, pilot program |

---

## Outputs

1. **Stakeholder Register** (table as above)
2. **Power/Interest Grid** (ASCII diagram)
3. **Top 2 Stakeholders** — identified as primary requirements drivers
4. **Engagement Plan Summary** — one-paragraph narrative describing overall engagement approach

---

## Quality Gate

Before passing outputs to the next stage:
- [ ] At least 3 distinct stakeholder categories represented
- [ ] Every stakeholder has an influence, interest, quadrant, and engagement strategy assigned
- [ ] At least one Definitive or Dominant salience stakeholder identified
- [ ] Top 2 requirements-driving stakeholders clearly identified
- [ ] No placeholder or "Unknown" entries in key fields
- [ ] Each stakeholder's key concern is specific and non-generic
- [ ] Engagement strategies are actionable (not just "communicate")

---

## Graceful Degradation

If WebSearch is unavailable:
- Use domain knowledge from SECOND-KNOWLEDGE-BRAIN.md to identify common stakeholder roles for the domain
- Use the classification examples table above to bootstrap similar stakeholders
- Note in the register: "[Domain research not available — stakeholders derived from brief and domain knowledge only]"
