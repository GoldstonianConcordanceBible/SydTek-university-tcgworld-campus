# TCG.world NPC Dialogue Endpoint Spec

## Request (game → agent)
- player_id
- npc_id
- player_utterance
- state (optional snapshot)
- quest_context (optional)

## Response (agent → game)
- npc_id
- route (onboarding|quest_help|policy_question|out_of_scope)
- mwf_stage (mirror|water|fire)
- npc_response_text
- citations (Anchor/Evidence IDs)
- state_patch (allowed progress updates)

## Failure Mode
If the agent fails:
- Respond with a short safe redirect to QUEST onboarding and avoid new claims.