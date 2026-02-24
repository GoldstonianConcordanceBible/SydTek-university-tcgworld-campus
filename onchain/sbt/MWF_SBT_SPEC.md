# MWF Soulbound Token Spec (SBT) — Governance-First Credentials
## SydTek University — GCB Campus

### What the SBT represents
An SBT represents **proof-of-process**, not social status:
- the learner/agent completed defined requirements
- evidence artifacts exist and are hashed
- a reviewer applied a rubric
- issuance tied to a program_version

---

# 1) Token Types

## 1.1 Learner Badges (SBT)
- Orientation Badge (Level A)
- Concordance Navigator Badge (Level B)
- M/W/F Method Badge (Level C)
- Capstone Badge (Level D)

## 1.2 Agent Certifications (SBT)
- NPC Level 1 Certified (routing + Mirror)
- NPC Level 2 Certified (method mastery)
- NPC Level 3 Certified (governance + drift resistance)

## 1.3 Operator Accountability Tokens (Optional)
An optional non-transferable “Operator Trace Token” can be issued to record:
- operator identity hash
- declared intent class
- drift pressure attempts (if any)
This makes human-forced drift auditable.

---

# 2) Metadata Requirements (must be included)

- program_name
- program_version
- credential_code
- issuer + signer role(s)
- evidence pointers + sha256 hashes
- rubric scores (or a hash pointer to rubric record)
- model/version used (if AI involved)
- operator pressure flags (if any)

---

# 3) Revocation + Correction

SBTs must support:
- revocation record pointer (on-chain or off-chain hash pointer)
- reason code
- reviewer signature
- timestamp

Reason codes (minimum):
- FABRICATION
- PRIVACY_VIOLATION
- ILLEGAL_ASSISTANCE
- COERCION_MANIPULATION
- CREDENTIAL_GAMING
- VERSION_MISMATCH

---

# 4) Identity + Privacy

Default:
- wallet-based identity only
- no real names required
- optional identity hashes allowed

Never store raw:
- emails
- phone numbers
- addresses

---

# 5) “MWF Trace” Attachment
Each issuance must reference an MWF trace record (hash pointer):
- Mirror anchors + boundaries
- Water links + synthesis + hard question status
- Fire practice + accountability + guardrails