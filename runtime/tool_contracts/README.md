# Tool Contracts

This folder defines what “tools” an NPC/agent may use and what each tool is allowed to return.

## Tools
- retrieval:anchors — fetches text snippets by Anchor ID
- retrieval:evidence — fetches evidence by Evidence ID
- state:read — reads player/NPC state
- state:write — writes allowed progress fields only

## Prohibited
- web browsing
- financial advice
- identity/credential claims not grounded in anchors/evidence