<!-- docs/SYDTEK_GITHUB_ORG_STRUCTURE.md -->

# SydTek University — GitHub Organization Structure (Recommended)

## Top-Level Orgs
1) **SydTekUniversity** (institution + campuses + governance)
2) **GoldstonianConcordanceBible** (canon project repos)
3) **SydTekScholars** (K–12 homeschool curriculum repos)

---

## SydTekUniversity (Org)
**Purpose:** institutional governance, metaverse campuses, credential specs, templates.

Recommended repos:
- `sydtek-governance` (policies, codes, review rubrics, disclosures)
- `sydtek-credential-specs` (chain-agnostic credential specs, schemas)
- `sydtek-campus-tcgworld` (this repo, campus implementation)
- `sydtek-campus-assets` (signage packs, UI, posters, templates)
- `sydtek-repo-templates` (README, CITATION.cff, .zenodo.json, JSON-LD)

---

## GoldstonianConcordanceBible (Org)
**Purpose:** canonical text framework, series volumes, concordance spine, indices.

Recommended repos:
- `gcb-series-i` (Series I canonical content + indices)
- `gcb-spine` (Concordance Spine template + method docs)
- `gcb-canon-index` (CANON_INDEX.json, cross-link registry)
- `gcb-agents` (agent prompts, guardrails, QA tests)
- `gcb-publications` (Zenodo/DOI release packaging)

---

## SydTekScholars (Org)
**Purpose:** homeschool curriculum and age-tiered learning experiences.

Recommended repos:
- `phonics-of-the-promise-level-1`
- `faith-hackers-kids`
- `beta-israel-kids`
- `sydtek-scholars-assessments`

---

## Cross-Org Rules
- Canon lives in **GoldstonianConcordanceBible**
- Campuses & NPC delivery live in **SydTekUniversity**
- K–12 adaptations live in **SydTekScholars**
- Credential specs live in **SydTekUniversity** (single source of truth)