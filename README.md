# Python Task Manager Fix - Silver SWE-Bench Style Task

## Task Overview
Fix a realistic off-by-one error in the Task Manager CLI's deletion logic.

## Files
- `instruction.md` - Agent-facing task description
- `main.py` - Broken implementation
- `solution/solve.sh` - Reference solution (git patch)
- `tests/` - Complete test harness

## How to Test Locally (Harbor Style)

```bash
# 1. Null check (should fail)
bash tests/test.sh

# 2. Apply fix
bash solution/solve.sh

# 3. Oracle check (should pass)
bash tests/test.sh
