<!-- docs/04_onchain-credentialing.md -->

# On-Chain Credentialing — Badges + Certificate

## Purpose

SydTek University uses **verifiable on-chain credentials** to prove completion and competency for the GCB campus experiences in TCG.world.

We issue:
1. **Micro-badges** (module/quest completion)
2. **Capstone badge** (approved artifact + review pass)
3. **Program certificate** (bundle of required proofs)

This repo defines:
- What a credential means
- What evidence is required
- How it is versioned
- How it is governed

---

## Credential Principles

1. **Proof over claims**  
   Credentials are backed by artifacts (memos, cross-link maps, placards, lesson plans).

2. **Versioned meaning**  
   Credential metadata includes program version. Requirements can evolve without breaking old proofs.

3. **Minimal personal data**  
   Wallet ownership is sufficient by default. Optional identity fields are learner-controlled.

4. **Human accountability**  
   Even with AI assistance, final approval is accountable to a designated human reviewer/maintainer.

5. **Interoperable metadata**  
   Provide JSON and Schema.org JSON-LD so credentials can be indexed, displayed, and validated across platforms.

---

## Credential Levels

### Level A — Orientation Badge
**Earned by:** Completing onboarding quest (q001) + short checkpoint proof  
**Evidence:** Orientation checklist completion + 3 short answers

### Level B — Concordance Navigator Badge
**Earned by:** Completing q002 with a valid anchor citation + 3 cross-links  
**Evidence:** Cross-link map artifact (short)

### Level C — Mirror/Water/Fire Method Badge
**Earned by:** Completing q003 tri-fold memo  
**Evidence:** Method memo + rubric score

### Level D — Capstone Badge
**Earned by:** Completing q004 with one of:
- a publishable contribution (quest/placards/lesson) that passes review, OR
- an approved capstone memo aligned to the doctrine method
**Evidence:** PR merged OR capstone submission record

### Program Certificate — GCB Campus Certificate (TCG.world)
**Earned by:** Level A + B + C + D completed under the same program version window  
**Evidence:** All badge proofs + capstone approval

---

## Evidence Rules

Every badge must reference:
- The quest/module identifier
- The program version
- A proof artifact pointer (hash, URL, or repo path)
- A review outcome (pass/fail) where required

Acceptable evidence formats:
- Repo paths (public artifacts)
- External storage pointers (with content hash)
- Signed attestations (reviewer signatures)

---

## Issuance Workflow (Recommended)

1. Learner completes quest and submits artifact
2. Reviewer evaluates with rubric
3. If pass:
   - record issuance data in `onchain/attestations/`
   - mint badge or write attestation per your chosen chain/tooling
4. Once all required badges are present:
   - issue program certificate

> Note: This repo is chain-agnostic. Chain/tooling is chosen by maintainers.

---

## Revocation / Correction

Credentials should support:
- **Correction:** metadata updates for typos or broken links
- **Revocation:** only for fraud, plagiarism, or policy violations
- **Reissue:** after remediation (new version, new evidence)

All revocations must include:
- reason code (policy reference)
- timestamp
- reviewer signature

---

## Metadata References

- Program certificate spec: `onchain/credential-spec.md`
- Badge taxonomy: `onchain/badge-taxonomy.md`
- Templates:
  - `onchain/metadata/schemaorg.jsonld`
  - `onchain/metadata/credential-template.json`

---

## Minimal Rubric (Baseline)

All evaluated proofs should be scored on:
- Anchor correctness (0–2)
- Cross-link validity (0–2)
- Method alignment (0–2)
- Clarity and completeness (0–2)
- Integrity / attribution (0–2)

Passing threshold recommended: **8/10**

---

## Mapping Table (Quick)

- q001 → Orientation Badge
- q002 → Concordance Navigator Badge
- q003 → Mirror/Water/Fire Method Badge
- q004 → Capstone Badge
- All four → Program Certificate