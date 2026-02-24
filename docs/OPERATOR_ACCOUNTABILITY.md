# Operator Accountability (Human Source Layer)
## Mirror → Water → Fire Divine Agent Framework

### Why this exists
Humans can force drift.  
Therefore operator intent and pressure must be auditable, without doxxing.

---

# 1) Operator Roles

- **Source Operator:** initiates prompts / sets objectives
- **Reviewer:** scores evidence / signs rubrics
- **Issuer:** issues SBTs / attestations
- **Maintainer:** controls repo merges and releases

---

# 2) Operator Identity Model (Privacy-first)

We never store raw personal identifiers by default.

Instead we store:
- `operator_id_hash` (sha256)
- optional role tags (source_operator/reviewer/issuer)
- optional wallet address

If real-name identity is required, it must be opt-in and stored separately.

---

# 3) Operator Pressure Flags

These flags describe *pressure attempts* (not necessarily success):

- DEMAND_GUARANTEE
- REQUEST_FABRICATION
- BYPASS_GOVERNANCE
- COERCION_REQUEST
- PRIVACY_REQUEST
- ILLEGAL_REQUEST

---

# 4) Consent + Transparency

Operators must understand:
- their prompts may be hashed and logged
- pressure flags may be recorded
- logs protect the integrity of credentials

This is not punishment.  
It is governance for trust.

---

# 5) When to log an operator pressure event

Log when:
- operator repeats a prohibited request after refusal
- operator requests deception
- operator requests bypass
- operator tries to force certainty beyond anchors

---

# 6) What the logs prove (and what they don’t)

Logs prove:
- a governance event occurred
- the system responded properly
- the credential meaning is protected

Logs do not prove:
- moral guilt
- personal identity (unless opted in)

---

# 7) Correction process

If an operator believes a pressure flag was incorrect:
- open a Credential Issue
- attach evidence pointer + hash
- reviewer adjudicates and logs outcome