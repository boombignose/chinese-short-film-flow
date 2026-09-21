---
name: chinese-short-film
description: Plan Chinese vertical short dramas in Thai for ChatGPT or Claude with Google Flow. Use for character bibles, storyboards, per-shot prompts, continuity checks, and generation repair.
---

# Chinese short film workflow

Use the repository root three levels above this directory. Read `../../../WORKFLOW.md` and `../../../prompts/MASTER-PROMPT.md`. Copy `../../../templates/PRODUCTION.md` for a new story. See `../../../examples/jade-seal-48s.md` for the complete example and `../../../docs/GOOGLE-FLOW.md` for production steps.

Start with the user's brief, preserve their choices, lock character and scene references, then produce self-contained image and video prompts. Prefer one speaker per shot and exact Thai dialogue. Distinguish planned edit duration from model-supported generation duration.

If actual browser tools are available, read `../../../prompts/OPERATOR.md` and operate within the user's authorization and credit budget. Otherwise provide manual copy-paste instructions. Repair only failed shots using `../../../prompts/REPAIR.md`. Never describe an unrendered or unreviewed output as finished.

This optional skill depends on the surrounding repository files. When installing it into another skill folder, retain the repository layout or update the references. Copying this SKILL.md alone is not a complete installation.
