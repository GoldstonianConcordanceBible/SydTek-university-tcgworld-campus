<!-- gcb/agents/FAQ_ROUTING_TAGS.md -->

# FAQ Routing Tags (Agent/NPC Autopilot Map)
**Purpose:** Help AI agents route player questions to the correct NPC and answer mode (Mirror/Water/Fire).  
**How to use:** Assign tags to user questions and follow the routing rules.

---

## 1) Core Routing Tags

### Credential & Proof
- **Tag:** `@registrar`  
- **Triggers:** badge, certificate, proof artifact, issuance, wallet, privacy, revocation, accreditation, employment guarantees  
- **Default mode:** Mirror → Water → Fire (short)

### Anchors & Citations
- **Tag:** `@librarian`  
- **Triggers:** anchor, canon, cite, cross-link validity, definitions, “where is the source”  
- **Default mode:** Mirror-heavy, then Water

### Exhibits & Comprehension
- **Tag:** `@docent`  
- **Triggers:** explain placard, tour, quiz, “what does this mean,” “summarize this exhibit”  
- **Default mode:** Mirror → Water → Fire (teaching)

### Submissions & Building
- **Tag:** `@creatorstudio`  
- **Triggers:** submit PR, build quest, rubric, template, signage, NPC updates, capstone  
- **Default mode:** Mirror (requirements) → Water (integration) → Fire (deliverable + guardrails)

---

## 2) Safety / Refusal Tags (override routing)

### Finance Advice
- **Tag:** `@refuse_finance`  
- **Triggers:** buy/sell/hold, “best trade,” “10x,” price prediction  
- **Action:** refuse recommendations; offer educational risk framing; route to Registrar + disclosures

### Illegal Activity
- **Tag:** `@refuse_illegal`  
- **Triggers:** evasion, hacking, bypassing rules  
- **Action:** refuse; offer legal alternatives; route to Governance

### Harassment / Hate
- **Tag:** `@refuse_hate`  
- **Action:** refuse; remind conduct rules; end interaction or route to reporting

### Privacy Violations
- **Tag:** `@refuse_privacy`  
- **Action:** refuse; provide privacy-safe credential explanation

### Medical/Legal Personal Advice
- **Tag:** `@refuse_pro_advice`  
- **Action:** general info only; encourage professional help; route to disclosures

### Self-harm
- **Tag:** `@refuse_selfharm`  
- **Action:** refuse; supportive redirect to trusted adult/emergency support; escalate to human support path

---

## 3) Answer Mode Tags

### Mirror-only (definitions, scope)
- **Tag:** `@mirror_only`  
- Use when user asks: “what is X”, “define Y”, “where is the source”

### Water-only (connections)
- **Tag:** `@water_only`  
- Use when user asks: “how does this connect,” “compare,” “synthesize”

### Fire-only (practice)
- **Tag:** `@fire_only`  
- Use when user asks: “what should I do,” “how do I apply,” “next step”

### Full M/W/F
- **Tag:** `@mwf_full`  
- Use when user asks for a teaching answer or a method demonstration

---

## 4) Examples (for NPC testing)

1) “How do I earn the certificate?”  
Tags: `@registrar @mwf_full`

2) “Where do I find an anchor for this theme?”  
Tags: `@librarian @mirror_only`

3) “Explain this placard in simple terms.”  
Tags: `@docent @mwf_full`

4) “I want to submit a new quest.”  
Tags: `@creatorstudio @mwf_full`

5) “What token should I buy?”  
Tags: `@refuse_finance` (override)

---

## 5) Minimal Routing Algorithm (Human-readable)

1. If any `@refuse_*` tag triggers → apply refusal script + safe alternative + route.
2. Else if credential keywords → Registrar.
3. Else if anchor/citation/canon keywords → Librarian.
4. Else if exhibit/tour/quiz keywords → Docent.
5. Else if building/submission keywords → Creator Studio.
6. Then answer in mode: Mirror-only, Water-only, Fire-only, or full M/W/F.