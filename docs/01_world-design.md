<!-- docs/01_world-design.md -->

# World Design — SydTek University Campus in TCG.world (GCB Focus)

## Institutional Affiliation Statement

This repository is institutionally affiliated with **SydTek University** for the purpose of:
- advancing open research, educational tooling, and reproducible curriculum systems
- publishing structured scholarly and instructional content for long-term archiving and citation
- building governance, compliance, and accountability frameworks for AI-assisted knowledge work
- supporting metaverse-based learning experiences and verifiable on-chain credentialing

Independence: SydTek University is an independent educational initiative. References to third-party platforms, protocols, companies, or standards are for interoperability and research purposes and do not imply endorsement or partnership unless explicitly stated.

---

## 1) Design Intent

The SydTek University campus inside TCG.world is a **living learning environment** built around the **Goldstonian Concordance Bible (GCB)**.

The world is designed to:
- Teach learners how to **navigate canon** (anchors → cross-links → interpretation → practice).
- Provide **repeatable learning loops** (learn → apply → prove → attest).
- Support **events + cohorts** (live sessions, guided tours, capstones).
- Produce **verifiable outputs** (artifacts + on-chain proofs).

This campus prioritizes:
- Clarity over spectacle
- Guided discovery over open wandering
- Measurable learning outcomes over “vibes”
- Governance and accountability over “anything goes”

---

## 2) Core Metaverse Learning Loop

Every experience follows a simple loop:

1. **Orientation** (what you are doing + why)
2. **Anchor** (what canonical source you start from)
3. **Cross-Link** (how to connect it to the concordance)
4. **Interpretation** (what it means in context)
5. **Practice** (what action changes)
6. **Proof** (what you submit/complete)
7. **Attestation** (badge/certificate eligibility)

This loop is implemented through **Zones + Quests + NPC roles + Artifacts**.

---

## 3) World Map (Conceptual)

**Player path (default):**
Spawn Hub → SydTek Library → Concordance Archives → Mirror/Water/Fire Hall → Exhibit Walkthrough → Lecture Theater → Creator Studio

### Zone Purposes
- **Spawn Hub:** “How the campus works” + onboarding quest.
- **SydTek Library:** curated reading lists + structured “canon anchors.”
- **Concordance Archives:** index browsing + cross-link exercises.
- **Mirror → Water → Fire Hall:** doctrine walk-through, interpretive method training.
- **Exhibit Walkthrough:** story-driven guided learning (placards + audio + checkpoints).
- **Lecture Theater:** live classes, recorded lectures, releases, debates.
- **Creator Studio:** submissions, remixing, building new quests/placards.

---

## 4) Zone Specifications

### 4.1 Spawn Hub (ZONES/00_spawn-hub.md)
**Goal:** Make every learner competent to navigate the campus.
**Key elements:**
- “Welcome kiosk” with campus rules + disclosures
- A short guided quest: *q001_introduction*
- A “Registrar NPC” that explains credential proofs

**Success criteria:**
- Learner completes onboarding checklist and receives “Orientation” micro-badge eligibility.

---

### 4.2 SydTek Library (ZONES/01_sydtek-library.md)
**Goal:** Canon literacy and source confidence.
**Key elements:**
- “Canonical Anchors” shelves (Ethiopian canon anchor, Concordance Spine)
- “Start here” panels per Series/Volume
- Quiet areas with “Reading Prompts”

**Success criteria:**
- Learner identifies anchors and can cite them correctly in a short response.

---

### 4.3 Concordance Archives (ZONES/02_concordance-archives.md)
**Goal:** Cross-linking discipline and index navigation.
**Key elements:**
- Index terminal / directory boards (“CANON_INDEX” references)
- Cross-link stations (3–5 per theme)
- A “Librarian NPC” that assigns cross-link drills

**Success criteria:**
- Learner completes a cross-link exercise with at least 3 valid links and one “hard question.”

---

### 4.4 Mirror → Water → Fire Hall (ZONES/03_mirror-water-fire-hall.md)
**Goal:** Method mastery (interpretation + governance).
**Key elements:**
- Three wings:
  - **Mirror:** observation, text integrity, definitions
  - **Water:** synthesis, cross-links, consistency checks
  - **Fire:** application, ethics, action, governance decisions
- “Method placards” and micro-assessments

**Success criteria:**
- Learner produces a “Mirror/Water/Fire” tri-fold memo from a provided anchor.

---

### 4.5 Lecture Theater (ZONES/04_lecture-theater.md)
**Goal:** Cohort learning and public scholarship.
**Key elements:**
- Event schedules and replay boards
- Speaker guidelines (no impersonation, no financial advice, etc.)
- “Office hours” sessions for learners

**Success criteria:**
- Learner can attend/complete an event reflection and identify one actionable takeaway.

---

### 4.6 Exhibit Walkthrough (ZONES/05_exhibit-walkthrough.md)
**Goal:** Guided narrative comprehension.
**Key elements:**
- A structured path of exhibits with checkpoint prompts
- Audio tour scripts (optional)
- “Docent NPC” for guided tours

**Success criteria:**
- Learner completes the walkthrough and answers checkpoint prompts accurately.

---

### 4.7 Creator Studio (ZONES/06_creator-studio.md)
**Goal:** Build and contribute responsibly.
**Key elements:**
- Submission booth (issue template references)
- Quality gates and review rubric
- Remix policy and attribution
- “Build a quest” capstone path

**Success criteria:**
- Learner submits a compliant artifact (quest, placard set, lesson plan) that passes review.

---

## 5) NPC Roles and Responsibilities

### Registrar NPC
- Explains credential options
- Links to credential spec
- Verifies completion steps (off-chain evaluation + on-chain proof)

### Librarian NPC
- Assigns reading/citation drills
- Teaches how to reference anchors
- Routes learner to appropriate Series/Volume

### Docent NPC
- Guides exhibit walkthroughs
- Ensures checkpoint completion
- Helps learners translate content into practice

NPC scripts live in `campus/tcgworld/NPC_SCRIPTS/`.

---

## 6) Quest Design Standard

Each quest file should include:
- Objective
- Required anchors
- Steps (3–7)
- Proof submission instructions
- Scoring rubric
- Badge mapping (if any)

Quest files live in `campus/tcgworld/QUESTS/`.

---

## 7) Accessibility and Safety

Minimum requirements:
- Clear signage and simple language
- Short quests with checkpoint feedback
- No “gotcha” mechanics
- No pressure tactics, no deceptive prompts
- Strong disclaimers for finance/crypto content when present

---

## 8) Versioning and Releases

- Every campus release gets a version tag (e.g., `v0.3.0`)
- Release notes go in `docs/07_release-notes.md`
- Credentials reference program version at time of completion

---

## 9) Acceptance Checklist (World Design)

- [ ] All zones have a purpose statement and success criteria
- [ ] Onboarding quest exists and is completable
- [ ] At least 4 quests mapped to modules
- [ ] NPC scripts match the learning loop
- [ ] Credential mapping documented and consistent
- [ ] Governance and content review gates are operational