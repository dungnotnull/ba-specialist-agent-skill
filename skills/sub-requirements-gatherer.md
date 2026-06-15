---
name: sub-requirements-gatherer
description: Conduct structured requirements elicitation using BABOK v3 techniques — interview question banks, document analysis, assumption logging, and raw requirements extraction. Produces FR/NFR lists, assumption log, and open questions backlog.
---

## Purpose

This sub-skill operationalizes IIBA BABOK v3 elicitation techniques to extract complete, unambiguous requirements from the project context. It generates interview question banks tailored by stakeholder type, analyzes any available documents, and produces a categorized requirements list with an explicit assumption log.

---

## Inputs

- Stakeholder Register (from sub-stakeholder-mapper)
- Project brief and any uploaded documents
- Domain context

---

## Execution Steps

### Step 1: Select Elicitation Techniques

Based on the project context, select the most appropriate techniques from:

| Technique | Best For | Apply When |
|-----------|---------|-----------|
| Structured Interview | Primary users, sponsors | Always — for all top-2 stakeholders |
| Document Analysis | Existing systems, process docs | When source docs are available |
| Observation | Workflow/process requirements | When current processes need to be captured |
| Workshops (JAD) | Multiple stakeholders, conflicting views | When rapid alignment is needed |
| Questionnaire | Large user groups | When >5 users need to be surveyed |
| Prototyping | UI/UX requirements | When visual feedback is needed |

For each session, note the primary technique and any secondary techniques.

### Step 2: Generate Interview Question Banks

#### Domain-Specific Question Banks

To ensure deep elicitation, use these specialized banks in addition to universal questions:

##### 1. Software Product (B2C/SaaS)
- How do users currently discover the value proposition?
- What is the "Aha! moment" we must protect in the requirements?
- How do we handle multi-tenancy and data isolation for different users?
- What are the critical paths for user retention (churn prevention)?
- How does the system handle "noisy neighbors" in a shared resource environment?
- What is the expected user session duration and frequency?
- How do users currently solve the problem this product addresses?
- What analytics or telemetry data do we need to validate product-market fit?

##### 2. Internal Business Process (Enterprise/ERP)
- Where are the "shadow processes" (manual spreadsheets used outside the system)?
- What is the cost of a mistake in this process (financial/legal/operational)?
- How do we manage hand-offs between disparate departments?
- Who is the "silent" stakeholder who can block the process but isn't in the meetings?
- How does the process change during peak seasonal load?
- What is the current error/rework rate at each process step?
- Which steps require approval and what is the average approval cycle time?
- How are exceptions handled when the process deviates from the normal flow?

##### 3. External Service / API-First Integration
- What is the expected throughput (TPS) and peak burst capacity?
- How do we handle partial failures in downstream dependencies (Circuit Breaker needs)?
- What is the contract for error handling and status codes?
- How do we ensure idempotency for repeated requests?
- What are the authentication/authorization requirements for external consumers?
- What is the expected SLA for response time and availability?
- How do versioning and backward compatibility work for the API?
- What rate limiting and throttling policies apply?

**Universal Opening Questions (ask all stakeholder types):**
1. What problem does this project solve for you?
2. What does success look like 6 months after launch?
3. What would cause you to consider this project a failure?
4. What do you wish the current system/process did that it doesn't?
5. Who else should I be talking to?

**Sponsor / Decision Maker Questions:**
1. What business outcome does this project need to achieve?
2. What is the budget envelope and timeline?
3. What are the top 3 constraints (technical, regulatory, organizational)?
4. How will ROI be measured?
5. What decisions are you delegating to the team vs. keeping for yourself?
6. What is the minimum viable product you'd accept for initial launch?

**Primary User Questions:**
1. Walk me through a typical day — where does this product fit?
2. What takes the most time in your current workflow?
3. What information do you need most often that's hard to get?
4. Have you used similar tools? What did you love or hate about them?
5. What would make you stop using this tool?
6. How do you measure your own success in this role?
7. What do you wish you could do but can't with the current system?

**Technical Stakeholder Questions:**
1. What are the existing systems this must integrate with?
2. What are the performance SLAs we need to meet?
3. What security or compliance constraints apply?
4. What is the preferred technology stack or are there mandated choices?
5. What technical debt or legacy constraints exist?
6. What monitoring and observability requirements do you have?

**Regulatory / Compliance Questions:**
1. What regulations apply to this system or its data?
2. What audit or reporting requirements must be supported?
3. What data retention and deletion policies apply?
4. What certifications or compliance frameworks are mandatory?
5. What are the consequences of non-compliance (fines, legal, reputational)?

### Step 3: Document Analysis (if applicable)

If the user provides existing documents (specs, process flows, manuals):
1. List all provided documents.
2. For each: extract implied requirements, identify gaps, flag contradictions.
3. Add extracted requirements to the raw list tagged with the source document.

### Step 4: Produce Raw Requirements List

**Functional Requirements (FR):**
Describe what the system shall do. Format: "The system shall [action] [object] [condition]."

| ID | Requirement | Source | Priority Hint | Notes |
|----|-------------|--------|---------------|-------|
| FR-001 | The system shall allow users to register with email and password | User interview | High | SSO integration TBD |
| FR-002 | The system shall send email notifications when an order status changes | Sponsor brief | Medium | Notification preferences needed |
| ... | ... | ... | ... | ... |

**Non-Functional Requirements (NFR):**
Describe quality attributes. Use ISO/IEC 25010 categories:

| ID | Category | Requirement | Measurable Criterion | Source |
|----|----------|-------------|----------------------|--------|
| NFR-001 | Performance | Page load time under 3 seconds | P95 < 3000ms on 4G connection | Stakeholder |
| NFR-002 | Security | All user data encrypted at rest and in transit | AES-256 + TLS 1.3 | Compliance |
| NFR-003 | Availability | System available 99.5% uptime | Measured monthly | Sponsor |
| NFR-004 | Usability | New users complete onboarding without support | Task completion rate ≥ 85% in UAT | Primary User |
| ... | ... | ... | ... | ... |

ISO/IEC 25010 NFR categories to always consider:
- Functional Suitability, Performance Efficiency, Compatibility, Usability
- Reliability, Security, Maintainability, Portability

### Step 5: Assumption & Constraint Log

Record every assumption made during elicitation:

| ID | Assumption | Type | Confidence | Validation Method | Owner |
|----|-----------|------|-----------|-------------------|-------|
| ASM-001 | Users have stable internet connection | Technical | High | Check analytics of current system | Dev Team |
| ASM-002 | Regulatory review will complete before MVP launch | Business | Low | Confirm with compliance officer | Sponsor |
| CON-001 | Must deploy on AWS (mandated by IT policy) | Constraint | High | Written in IT policy doc | Architect |
| ... | ... | ... | ... | ... | ... |

Confidence levels:
- **High**: Verified by stakeholder or documented evidence
- **Medium**: Reasonable inference, needs validation
- **Low**: Guess or unverified — flag immediately for resolution

### Step 6: Open Questions Backlog

| ID | Question | Stakeholder to Answer | Priority | Status |
|----|---------|----------------------|----------|--------|
| OQ-001 | Does the system need offline functionality? | Primary User + Architect | High | Open |
| OQ-002 | What is the data migration strategy for existing records? | Technical + Sponsor | High | Open |
| ... | ... | ... | ... | ... |

---

## Outputs

1. **Interview Question Bank** (by stakeholder type)
2. **Functional Requirements List** (FR-001 ... FR-N, table format)
3. **Non-Functional Requirements List** (NFR-001 ... NFR-N, table format)
4. **Assumption & Constraint Log** (table format)
5. **Open Questions Backlog** (table format)

---

## Quality Gate

Before passing to story mapping:
- [ ] At least 5 functional requirements documented
- [ ] At least 3 non-functional requirements across ≥ 2 ISO/IEC 25010 categories
- [ ] Every requirement has a source (traceable to brief, interview, or document)
- [ ] Every assumption has a confidence level and validation method
- [ ] Open questions are prioritized (High/Medium/Low)
- [ ] No duplicate or contradictory requirements (or contradictions noted in assumption log)
- [ ] Domain-specific question bank generated for the relevant domain
- [ ] At least 1 question per top-2 stakeholder type in the interview bank

---

## Graceful Degradation

If only a brief is available and no documents or interviews:
- Generate requirements from the brief alone
- Mark all assumptions as Low confidence
- Generate a recommended interview question bank as a deliverable for the user to conduct real interviews
- Note: "[Requirements derived from brief only — stakeholder validation recommended before story mapping]"
