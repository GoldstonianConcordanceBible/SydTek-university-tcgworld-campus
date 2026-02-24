<!-- campus/tcgworld/BUILD_COORDINATES_TEMPLATE.md -->

# BUILD COORDINATES TEMPLATE — SydTek University Campus (GCB) in TCG.world

Use this file to record where everything is placed in-world so the campus can be rebuilt, audited, or migrated.

## How to Use
- Fill one section per structure.
- Use the same zone naming as `campus/tcgworld/ZONES/`.
- If TCG.world uses chunk/parcel identifiers, record BOTH coordinates and parcel IDs.
- Add a screenshot reference whenever possible.

---

# 0) Campus Metadata

- Campus Name: SydTek University — GCB Campus (TCG.world)
- Program Version: v0.1.0 (update on each release)
- Build Lead:
- Date Started:
- Date Updated:
- World / Server / Instance:
- Parcel IDs (if applicable):
- Notes:

---

# 1) Global Orientation Points

## 1.1 Primary Spawn / Arrival Point
- Zone: Spawn Hub
- Coordinates (x, y, z):
- Facing Direction (N/E/S/W or degrees):
- Landmark Reference:
- Screenshot(s):
- Notes:

## 1.2 Campus Map Board
- Zone:
- Coordinates (x, y, z):
- Facing Direction:
- Nearby Landmark:
- Screenshot(s):
- Notes:

## 1.3 Return-to-Spawn Markers (list)
| Marker ID | Zone | Coordinates (x,y,z) | Facing | Nearby Landmark | Screenshot | Notes |
|---|---|---|---|---|---|---|
| RTS-01 |  |  |  |  |  |  |
| RTS-02 |  |  |  |  |  |  |
| RTS-03 |  |  |  |  |  |  |

---

# 2) Zone Placement Records (repeat for each zone)

## Zone Record Template
- Zone Name:
- File Reference: campus/tcgworld/ZONES/<zone_file>.md
- Entrance Coordinates (x, y, z):
- Entrance Facing Direction:
- Bounding Area / Footprint (optional):
- Primary Landmark(s):
- Zone Sign Coordinates:
- “What you do here” Sign Coordinates:
- “Proof / Completion” Sign Coordinates:
- “Where next” Sign Coordinates:
- NPC Placements (IDs + coords):
- Quest Start Point(s) (IDs + coords):
- Exhibit Placards (IDs + coords):
- Screenshot(s):
- Notes:

---

# 3) Zone Records

## 3.1 Spawn Hub
- Zone Name: Spawn Hub
- File Reference: campus/tcgworld/ZONES/00_spawn-hub.md
- Entrance Coordinates (x, y, z):
- Entrance Facing Direction:
- Primary Landmark(s):
- Zone Sign Coordinates:
- “What you do here” Sign Coordinates:
- “Proof / Completion” Sign Coordinates:
- “Where next” Sign Coordinates:
- NPC Placements:
  - Registrar NPC:
  - Optional Greeter NPC:
- Quest Start Point(s):
  - q001_introduction:
- Screenshot(s):
- Notes:

## 3.2 SydTek Library
- Zone Name: SydTek Library
- File Reference: campus/tcgworld/ZONES/01_sydtek-library.md
- Entrance Coordinates (x, y, z):
- Entrance Facing Direction:
- Primary Landmark(s):
- NPC Placements:
  - Librarian NPC:
- Quest Start Point(s):
  - q002_concordance-basics:
- Anchor Shelves (IDs + coords):
  - Ethiopian Canon Anchor Shelf:
  - Concordance Spine Shelf:
  - Series I Starter Shelf:
- Screenshot(s):
- Notes:

## 3.3 Concordance Archives
- Zone Name: Concordance Archives
- File Reference: campus/tcgworld/ZONES/02_concordance-archives.md
- Entrance Coordinates (x, y, z):
- NPC Placements:
  - Librarian NPC (or assistant):
- Cross-Link Stations (IDs + coords):
- Quest Start Point(s):
  - q002_concordance-basics (checkpoint):
- Screenshot(s):
- Notes:

## 3.4 Mirror → Water → Fire Hall
- Zone Name: Mirror → Water → Fire Hall
- File Reference: campus/tcgworld/ZONES/03_mirror-water-fire-hall.md
- Entrance Coordinates (x, y, z):
- Wing Entrances (IDs + coords):
  - Mirror Wing:
  - Water Wing:
  - Fire Wing:
- Quest Start Point(s):
  - q003_mirror-water-fire:
- NPC Placements:
  - Docent NPC:
- Screenshot(s):
- Notes:

## 3.5 Lecture Theater
- Zone Name: Lecture Theater
- File Reference: campus/tcgworld/ZONES/04_lecture-theater.md
- Entrance Coordinates (x, y, z):
- Stage Coordinates:
- Audience Seating Area (bounds):
- “Disclosures” Board Coordinates:
- NPC Placements:
  - Host NPC (optional):
- Screenshot(s):
- Notes:

## 3.6 Exhibit Walkthrough
- Zone Name: Exhibit Walkthrough
- File Reference: campus/tcgworld/ZONES/05_exhibit-walkthrough.md
- Entrance Coordinates (x, y, z):
- Placards (IDs + coords):
  - P01:
  - P02:
  - P03:
  - P04:
  - P05:
  - P06:
  - P07:
  - P08:
- NPC Placements:
  - Docent NPC:
- Screenshot(s):
- Notes:

## 3.7 Creator Studio
- Zone Name: Creator Studio
- File Reference: campus/tcgworld/ZONES/06_creator-studio.md
- Entrance Coordinates (x, y, z):
- Submission Booth Coordinates:
- “Templates” Board Coordinates:
- “Rubric” Board Coordinates:
- NPC Placements:
  - Creator Studio Mentor NPC:
- Quest Start Point(s):
  - q004_capstone:
- Screenshot(s):
- Notes:

---

# 4) Asset Registry (Optional but recommended)

| Asset ID | Type (Sign/Placard/NPC/Terminal) | Zone | Coordinates (x,y,z) | File Pointer | Screenshot | Notes |
|---|---|---|---|---|---|---|
| SIGN-SPAWN-01 | Sign | Spawn Hub |  |  |  |  |
| NPC-REG-01 | NPC | Spawn Hub |  |  |  |  |
| PLC-EX-01 | Placard | Exhibit |  |  |  |  |

---

# 5) Change Log

| Date | Version | What changed | Who | Notes |
|---|---|---|---|---|
|  |  |  |  |  |