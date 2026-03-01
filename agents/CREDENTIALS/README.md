# Tokenized Credentials (SydTek University)

This folder defines token-based credentials used to unlock continuation environments
(e.g., premium cohorts, gated modules, private library shelves).

**Important:**
- This is an access-control / credential mechanism, not investment advice.
- Never request or store private keys in this repo.
- Verification must be read-only: wallet proves ownership, system grants access.

## Credential Model

We support 2 credential types:

1) **Token-Gated Badge (Fungible Token Gate)**
   - User proves they hold >= threshold of a specified token mint.
   - Good for simple membership / supporter access.

2) **Signed Credential (Verifiable Credential)**
   - Server issues a signed credential after a learning event (quiz, module completion).
   - Can be verified by any LLM/agent that supports JSON-LD.

This repo starts with Token-Gated Badge using:
- $GCB on pump.fun (Solana mint inferred from the link)
- Mint: `E68E27Y72FHTJH1MycB6KjX5PQAyKPYsRGZjMEx9`
- Source page: https://pump.fun/coin/E68E27Y72FHTJH1MycB6KjX5PQAyKPYsRGZjMEx9pump

## How verification works (high-level)

1. User connects wallet in the platform UI.
2. System checks token holdings for the configured mint.
3. If holdings >= threshold, user receives access role(s).
4. Aurelia routes the user to gated shelves / monetized continuation environments.

Next chunks will add:
- verifier implementation
- tests
- routing integration