<!-- docs/05_governance.md -->

# Governance — Quality, Integrity, and Accountability

## Purpose

This governance framework protects:
- Canon integrity (accurate anchors and citations)
- Learner safety (no deceptive or harmful content)
- Contributor integrity (attribution, anti-plagiarism)
- Credential meaning (proof-based, review-based)

This is a **governance-first campus**: content is welcome, but not unreviewed.

---

## Governance Roles

### Maintainers
- Own releases and approvals
- Control merging and tagging
- Maintain credential requirements

### Reviewers
- Evaluate submissions using rubrics
- Sign review records (integrity object)
- Can request revisions or reject

### Contributors
- Submit quests, placards, lessons, NPC scripts, assets
- Must follow templates and attribution rules

---

## Contribution Types

1. **World content**
   - Zones, signage text, navigation boards
2. **Learning content**
   - Quests, lesson plans, assessments
3. **Canon content**
   - Anchors, cross-links, indices (high scrutiny)
4. **Credential metadata**
   - Badge templates, schema, attestation records
5. **Media assets**
   - Posters, thumbnails, UI panels

Each type has different review gates.

---

## Quality Gates (Required)

### Gate 1 — Attribution & Integrity
Submission must include:
- Sources/anchors used (where applicable)
- Author/contributor credit
- “AI assistance” disclosure if used (simple, honest)

**Fail conditions:**
- Plagiarism
- Fabricated citations
- Misleading claims

---

### Gate 2 — Canon & Method Alignment
If content references the GCB method:
- Must respect the Mirror/Water/Fire structure
- Must not contradict defined anchors without explicitly labeling as interpretation/opinion
- Must not misrepresent sources

**Fail conditions:**
- Unclear anchor basis
- Conflating opinion with canon
- Missing “hard questions” where appropriate

---

### Gate 3 — Learner Safety & Conduct
Content must:
- Avoid manipulation, deception, or pressure tactics
- Avoid claims that imply guaranteed outcomes (money, jobs, certification)
- Include required disclosures for finance/crypto contexts

**Fail conditions:**
- “Get rich quick” tone
- Unlicensed financial advice
- Harassment or hate content
- Encouraging dangerous acts

---

### Gate 4 — Credential Impact Review (If badge/certificate mapped)
If submission affects credentials (quests/rubrics):
- Must include rubric + passing threshold
- Must specify evidence artifact type
- Must be versioned

**Fail conditions:**
- No measurable proof
- Requirements too vague
- Evidence not collectible/auditable

---

## Review Process

### For normal content (placards, quests, NPC scripts)
1. Contributor opens PR
2. Reviewer applies rubric and comments
3. Revisions if needed
4. Reviewer approves
5. Maintainer merges

### For canon/index changes (CANON_INDEX, anchors)
- Requires 2 reviewers minimum
- Requires release note entry
- Must include a “change rationale” section

---

## AI Use Policy (Simple + Enforceable)

AI tools may be used for:
- drafting, summarization, structure, grammar
- generating templates and checklists

AI tools may NOT be used to:
- fabricate citations or source claims
- impersonate real people
- “launder” plagiarism

Required disclosure format (1–2 lines in PR):
> AI use: Drafted with AI assistance for structure/clarity. Final review and accountability remain with the human contributor.

---

## Versioning Policy

- Any change that affects learning outcomes, rubrics, or credential requirements:
  - increments program version (at least patch; minor if meaningfully changed)
  - updates `docs/07_release-notes.md`
- Credentials must store the program_version used at issuance time.

---

## Enforcement

Maintainers may:
- request edits
- reject submissions
- revert merged content
- revoke credentials for proven fraud/plagiarism

All revocations:
- must be recorded with reason code + timestamp
- must reference this governance document

---

## Disclosures (Required Campus Copy)

Place this near onboarding and events:

- No guarantee of employment or certification
- Education-only; not financial advice
- Credential meaning depends on evidence + review
- Policies and requirements can change by version

---

## Governance Checklist (Maintainer)

Before each release:
- [ ] All credential-mapped quests have rubrics
- [ ] All evidence pointers are resolvable
- [ ] Release notes updated
- [ ] Any canon/index changes have 2 reviews
- [ ] Disclosures visible in Spawn Hub + Lecture Theater