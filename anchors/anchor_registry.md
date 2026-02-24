<!-- gcb/canon/anchors/anchor_registry.md -->

# Anchor Registry (Campus Machine-Readable Index)
**Purpose:** Assign stable IDs to anchors, quests, placards, zones, and NPCs so AI agents and tooling can route reliably.  
**Scope:** Campus-facing registry (not the entire GCB canon).

---

## 1) Naming Rules

### 1.1 IDs must be:
- lowercase
- snake_case
- stable over time
- unique within this repo

### 1.2 Prefix conventions
- `zone_` for zones
- `npc_` for NPC roles
- `quest_` for quests
- `placard_` for exhibits
- `anchor_` for canon/method anchors
- `cls_` for cross-link stations

---

## 2) Zones

| id | display_name | path |
|---|---|---|
| zone_spawn_hub | Spawn Hub | campus/tcgworld/ZONES/00_spawn-hub.md |
| zone_library | SydTek Library | campus/tcgworld/ZONES/01_sydtek-library.md |
| zone_archives | Concordance Archives | campus/tcgworld/ZONES/02_concordance-archives.md |
| zone_mwf_hall | Mirror → Water → Fire Hall | campus/tcgworld/ZONES/03_mirror-water-fire-hall.md |
| zone_lecture | Lecture Theater | campus/tcgworld/ZONES/04_lecture-theater.md |
| zone_exhibits | Exhibit Walkthrough | campus/tcgworld/ZONES/05_exhibit-walkthrough.md |
| zone_creator_studio | Creator Studio | campus/tcgworld/ZONES/06_creator-studio.md |

---

## 3) NPCs

| id | role_name | script_path | primary_zone |
|---|---|---|---|
| npc_registrar | Registrar NPC | campus/tcgworld/NPC_SCRIPTS/registrar.md | zone_spawn_hub |
| npc_librarian | Librarian NPC | campus/tcgworld/NPC_SCRIPTS/librarian.md | zone_library |
| npc_docent | Docent NPC | campus/tcgworld/NPC_SCRIPTS/docent.md | zone_exhibits |
| npc_creator_mentor | Creator Studio Mentor | campus/tcgworld/NPC_SCRIPTS/creator_studio_mentor.md | zone_creator_studio |

---

## 4) Quests

| id | display_name | path | badge_code | zones |
|---|---|---|---|---|
| quest_q001 | q001 Introduction | campus/tcgworld/QUESTS/q001_introduction.md | orientation | zone_spawn_hub |
| quest_q002 | q002 Concordance Basics | campus/tcgworld/QUESTS/q002_concordance-basics.md | concordance | zone_library, zone_archives |
| quest_q003 | q003 Method Mastery | campus/tcgworld/QUESTS/q003_mirror-water-fire.md | mwf | zone_mwf_hall |
| quest_q004 | q004 Capstone | campus/tcgworld/QUESTS/q004_capstone.md | capstone | zone_creator_studio |
| quest_q005 | q005 Exhibit Reflection (optional) | campus/tcgworld/QUESTS/q005_exhibit_reflection.md | none | zone_exhibits |

---

## 5) Placards (Exhibits)

| id | display_name | path | zone |
|---|---|---|---|
| placard_p01 | P01 Foundation | gcb/exhibits/placards/P01_foundation.md | zone_exhibits |
| placard_p02 | P02 Mirror | gcb/exhibits/placards/P02_mirror.md | zone_exhibits |
| placard_p03 | P03 Water | gcb/exhibits/placards/P03_water.md | zone_exhibits |
| placard_p04 | P04 Fire | gcb/exhibits/placards/P04_fire.md | zone_exhibits |
| placard_p05 | P05 Proof Artifacts | gcb/exhibits/placards/P05_proof_artifacts.md | zone_exhibits |
| placard_p06 | P06 AI Agents | gcb/exhibits/placards/P06_ai_agents.md | zone_exhibits |
| placard_p07 | P07 Governance-First | gcb/exhibits/placards/P07_governance_first.md | zone_exhibits |
| placard_p08 | P08 Hard Questions | gcb/exhibits/placards/P08_hard_questions.md | zone_exhibits |

---

## 6) Anchors (Method + Canon Shelves)

| id | display_name | path | zone |
|---|---|---|---|
| anchor_mwf_method | Mirror → Water → Fire Method | docs/03_learning-loop.md | zone_mwf_hall |
| anchor_concordance_spine | Concordance Spine Anchor | gcb/canon/anchors/concordance-spine.md | zone_library |
| anchor_concordance_spine_short | Concordance Spine (Short Form) | gcb/canon/anchors/concordance-spine_signage_short.md | zone_library |
| anchor_ethio_canon | Ethiopian Canon Anchor Shelf | gcb/canon/anchors/ethiopian-canon.md | zone_library |

---

## 7) Cross-Link Stations

| id | display_name | zone | pointer |
|---|---|---|---|
| cls_01_support_echo | Support / Echo | zone_archives | gcb/canon/CANON_INDEX.json#crosslink_stations[0] |
| cls_02_context_tension | Context / Tension | zone_archives | gcb/canon/CANON_INDEX.json#crosslink_stations[1] |
| cls_03_direction_not_application | Direction (Not Application Yet) | zone_archives | gcb/canon/CANON_INDEX.json#crosslink_stations[2] |

---

## 8) Versioning Notes
- Do not rename IDs once referenced by credentials or attestations.
- If something must change, add a new ID and deprecate the old one in release notes.