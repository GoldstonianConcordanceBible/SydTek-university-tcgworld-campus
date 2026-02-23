<!-- onchain/credential-spec.md -->

# Credential Specification (Chain-Agnostic)

## 1) Credential Types

### 1.1 Badge (Micro-credential)
Represents completion of a specific quest/module or competency.

### 1.2 Certificate (Program Credential)
Represents completion of a defined set of badges + capstone approval.

---

## 2) Core Fields (Required)

These fields MUST be present for every badge/certificate metadata object:

- `credential_id` (string, unique)
- `credential_type` ("badge" | "certificate")
- `program_name` (string)
- `program_version` (string, e.g., "v0.3.0")
- `issuer` (object)
- `recipient` (object, minimal)
- `issued_at` (ISO-8601 datetime)
- `requirements` (array of objects)
- `evidence` (array of objects)
- `revocation` (object or null)
- `integrity` (object: hashes/signatures)

---

## 3) Issuer Object (Required)

```json
{
  "name": "SydTek University",
  "entity_type": "educational_initiative",
  "website": "TBD",
  "repository": "https://github.com/<ORG>/<REPO>",
  "contact": "TBD"
}