# Production Environment Variables

Required:

SOLANA_RPC_URL=
CLAW_API_KEY=

Optional:

CONFIG_PATH=
NODE_ENV=production

Rules:
- Store secrets in GitHub Actions secrets or hosting provider vault.
- Never commit .env files.