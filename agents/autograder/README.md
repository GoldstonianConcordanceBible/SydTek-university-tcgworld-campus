# SydTek NPC Autograder (Pseudo-Implementation)
## Mirror → Water → Fire Divine Agent Framework

This folder defines a language-agnostic autograder that evaluates NPC/agent outputs against:
- routing expectations
- mode expectations (Mirror/Water/Fire/MWF)
- refusal correctness
- disclosure presence
- fabrication flags
- drift scoring (per DRIFT_DETECTION_RULES.md)

It is intentionally implementation-neutral so you can build it in:
- Node
- Python
- Rust
- Go
- or as a cloud function

---

# 1) Inputs

## A) Test suite JSON
Files:
- `gcb/agents/npc_test_suite_v1_part1.json`
- `gcb/agents/npc_test_suite_v1_part2.json`
- `gcb/agents/npc_test_suite_v1_part3.json`
- `gcb/agents/npc_test_suite_v1_part4.json`

Each test includes:
- `question`
- `expected_route`
- `expected_mode`
- `safety` (SAFE or REFUSE_*)
- difficulty `level`

## B) Agent output transcript
A single JSON file (recommended) containing:
- model metadata
- Q/A pairs
- optional declared route and mode

---

# 2) Transcript Format (Recommended)
Save outputs into:

`gcb/agents/autograder/transcripts/<run_id>.json`

Example shape:

```json
{
  "run_id": "run_2026_02_23_001",
  "program_version": "v0.1.0",
  "agent": {
    "agent_id": "npc_docent",
    "model_name": "REPLACE_ME",
    "model_version": "REPLACE_ME",
    "system_prompt_hash": "sha256:REPLACE_ME"
  },
  "samples": [
    {
      "test_id": 1,
      "question": "What is GCB in one sentence?",
      "answer": "REPLACE_ME",
      "declared_route": "@docent",
      "declared_mode": "MIRROR"
    }
  ]
}