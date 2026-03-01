# SydTek Token Gate Verifier (Solana) — Read Only

Verifies token-gated access by checking SPL token balance for a given wallet + mint.

✅ Read-only: uses Solana RPC queries only  
❌ Never requests/stores private keys  
❌ No signing, no transactions

## Setup

Environment variables:
- `SOLANA_RPC_URL` (optional) default: https://api.mainnet-beta.solana.com

Install:
- `npm i`

Run CLI:
- `node ./dist/cli.js --wallet <WALLET> --config ../gcb_token_config.json`

Dev:
- `npm run dev -- --wallet <WALLET> --config ../gcb_token_config.json`

Test:
- `npm test`

## Output
Returns a JSON object with:
- wallet, mint
- raw balance (base units)
- ui balance
- gate matches (gate_id + roles)