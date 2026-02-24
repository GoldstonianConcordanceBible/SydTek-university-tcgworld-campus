# Privacy & Consent (Metaverse NPCs)

## What data may be received
The dialogue endpoint spec includes `player_id`, `npc_id`, and `state`.

## Principle
**Consent-first.** Do not store or use conversation logs for training unless the player explicitly opts in.

## Storage rules (default)
- Store **pseudonymous identifiers only** (hashed `player_id`), or store nothing.
- Never store wallet addresses, emails, or unique identifiers in plaintext logs.
- Keep retention short (e.g., 30 days) unless explicitly required for credentials and governed.

## Player rights
Provide a mechanism to request deletion of stored data linked to a pseudonymous identifier.

## AI transparency
NPC responses must include a clear disclosure that the player is interacting with an AI system where required.