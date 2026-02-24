<!-- onchain/attestations/README.md -->

# Attestations (Evidence + Reviews)

This folder stores structured records that support badge/certificate issuance.

Recommended file types:
- `*_evidence.json` (learner submissions + pointers + hashes)
- `*_review.json` (reviewer scoring + decision + signature)
- `*_issuance.json` (final issuance record, if separate)

All records should include:
- program_version
- quest_id or credential_code
- evidence pointers
- sha256 content hashes (where possible)
- reviewer signature object (or reference)

Never store raw personal identifiers.
Use hashes if identity linking is required.