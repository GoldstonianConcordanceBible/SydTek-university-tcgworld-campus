<!-- campus/tcgworld/WORLD_BRIEF.md -->

# WORLD BRIEF — SydTek University Campus (GCB) for TCG.world

## 1) Build Objective

Create a SydTek University campus within TCG.world that delivers:
- A guided educational experience built around the Goldstonian Concordance Bible (GCB)
- Repeatable quests and learning loops
- A clear path to on-chain credential eligibility (badges + certificate)

The campus must be:
- Easy to navigate
- Clearly signposted
- Governance-first (quality control, attribution, and compliance)

---

## 2) Campus Narrative (One Sentence)

“A university in the metaverse where learners move from canon anchors to cross-links to practice—and prove mastery through verifiable credentials.”

---

## 3) Layout Requirements (High-Level)

### Zones (must exist)
1. Spawn Hub
2. SydTek Library
3. Concordance Archives
4. Mirror → Water → Fire Hall
5. Lecture Theater
6. Exhibit Walkthrough
7. Creator Studio

### Navigation
- Signage at every zone entrance
- A campus map at Spawn Hub and Library
- “Return to Spawn Hub” markers at least every 2 zones

---

## 4) Visual Language & Signage

### Visual identity
- Academic + archival aesthetic
- “Museum placard” style for exhibits
- Consistent icon system:
  - Mirror icon for observation
  - Water icon for synthesis
  - Fire icon for application

### Signage requirements
Each zone must have:
- A title sign
- A “What you will do here” sign
- A “Proof / Completion” sign
- A “Where to go next” sign

Media assets live in `campus/media/`.

---

## 5) Content Requirements

### Minimum viable content (MVC)
- Quests:
  - q001_introduction
  - q002_concordance-basics
  - q003_mirror-water-fire
  - q004_capstone
- NPC scripts:
  - librarian.md
  - docent.md
  - registrar.md
- Exhibits:
  - At least 8 placards in Exhibit Walkthrough
- Library:
  - 3 anchor shelves (Ethiopian canon, Concordance spine, Series I starter)

---

## 6) Quest & Checkpoint Mechanics (Design)

- Quests must be completable in 5–15 minutes each
- Checkpoints should be:
  - multiple choice, short answer, or “bring artifact”
- Proof requires:
  - a short submission (memo, cross-link map, reflection, or artifact)
- “Capstone” requires:
  - a structured tri-fold memo OR a content contribution that passes review

---

## 7) Coordinates / Build Mapping

Use this repo file to track final placements:
- `BUILD_COORDINATES_TEMPLATE.md`

Each zone should record:
- Approximate coordinates
- Entrance direction
- Nearby landmarks
- Screenshot references (if available)

---

## 8) Event Layer (Lecture Theater)

Recurring events (suggested):
- Weekly: “Mirror/Water/Fire walkthrough”
- Biweekly: “Concordance Cross-Link Lab”
- Monthly: “Release + Exhibit Update Tour”

Event recordings should be referenced in:
- `docs/07_release-notes.md`
- or a zone bulletin board inside Lecture Theater

---

## 9) Compliance & Disclosures (On-Site)

Must display near Spawn Hub + Lecture Theater:
- Not financial advice
- No guarantee of employment/certification
- Safety + conduct policy
- Attribution policy for community contributions

Detailed language is in `docs/06_compliance-disclosures.md`.

---

## 10) Definition of Done (Build)

The campus is “done” for v0 when:
- [ ] All 7 zones exist and are navigable
- [ ] All 4 quests are live and completable
- [ ] NPCs can direct learners correctly
- [ ] Exhibits contain at least 8 placards
- [ ] On-chain credential spec is published in-repo
- [ ] Governance + content review process is active