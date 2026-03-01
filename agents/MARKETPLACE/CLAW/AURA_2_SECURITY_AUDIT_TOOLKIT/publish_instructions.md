# Publishing to Claw Market

1. Register account on Claw Market.
2. Generate API key from dashboard.
3. Store key in environment variable:
   CLAW_API_KEY=...

4. Package directory:
   zip -r aura-2-security-audit-toolkit.zip AURA_2_SECURITY_AUDIT_TOOLKIT/

5. Upload via marketplace dashboard or API.

Important:
- Do not commit API keys.
- Use .env for local development.
- Use CI secret storage for automation.