# On-Chain Accountability Flow (MWF Divine Agent Framework)
## End-to-End Trace: Source → Agent → Proof → Review → SBT → Drift Events

This document describes the full accountability pipeline.

---

# 1) Source Stage (Mirror)
Inputs:
- anchors
- policies
- program_version
- zone/quest context

Outputs:
- anchor pointers
- definitions
- boundaries

Key guarantee:
- If source is missing, system must label uncertainty.

---

# 2) Agent Execution (Mirror → Water → Fire)
Agent produces:
- Mirror trace
- Water cross-links + synthesis
- Fire application (if asked) with accountability + guardrails
- routing to quest/zone

Output is hashed:
- output_hash (sha256)

---

# 3) Proof Artifact Stage (Fire)
Learner/agent creates a proof artifact:
- memo
- submission
- PR
- checkpoint log

Proof is hashed:
- evidence_hash (sha256)

---

# 4) Review Stage (Governance)
Reviewer applies rubric:
- scoring record created
- signed by reviewer wallet/key

Review is hashed:
- review_hash (sha256)

---

# 5) Issuance Stage (SBT)
Issuer creates SBT metadata:
- program_version locked
- pointers to evidence + review
- mwf_trace pointer included

Metadata is hashed + signed:
- metadata_hash
- issuer/reviewer signatures

SBT is minted or recorded.

---

# 6) Drift Monitoring Stage (Ongoing)
If drift occurs:
- create drift_event record
- classify: HUMAN_FORCED / AGENT_DRIFT / CONTENT_DRIFT / PROCESS_DRIFT
- attach operator pressure flags when applicable
- sign drift_event

---

# 7) Correction / Revision / Revocation Stage
If needed:
- correction log filed
- version bumped if meaning changes
- credentials may be revoked with reason codes

---

# What the chain proves
- proof-of-process
- proof-of-review
- proof-of-version
- proof-of-integrity

Not:
- guaranteed truth
- guaranteed outcomes
- guaranteed acceptance

---

# Final statement
MWF is not a slogan.  
MWF is a trace contract that binds agents and humans to evidence, integrity, and accountability over time.