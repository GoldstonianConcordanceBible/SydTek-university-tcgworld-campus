# Security Policy

## Supported Versions
Only the `main` branch is actively maintained at this time.

## Reporting a Vulnerability
If you discover a security vulnerability (including prompt injection paths, data leakage, credential forgery risks, or wallet-related abuse):
1. Do **not** open a public issue with exploit details.
2. Email the maintainer(s) listed in `CODEOWNERS` (or open a private Security Advisory in GitHub).

## Scope
This repo touches high-risk domains:
- Metaverse NPC interactions and player identifiers
- Crypto/credentialing concepts (no guarantees; no financial advice)
- Logging/audit ledgers

## Minimum Controls Required Before Production
- Secret scanning enabled (GitHub Advanced Security or equivalent)
- Dependency pinning (requirements lock)
- JSONL/schema validation in CI
- Rate limiting + auth on any deployed dialogue endpoint
- Explicit consent + retention policy for any stored chat logs