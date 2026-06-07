# Reference Plan - Task Deletion Bug

## Root Cause Analysis
The bug is an off-by-one error in the `delete_task` method. After removing a task from the internal list using `pop(index)`, the code does not properly adjust subsequent ID lookups or list indices. This causes ID mismatches for remaining tasks on future operations.

## Intended Fix
Update the deletion logic to correctly re-index or use a more robust data structure (e.g., filter by ID instead of relying on list position) so that task IDs remain stable after deletions.

## Test Plan
- fail_to_pass tests: deletion of middle tasks, deletion of last task, multiple deletions
- pass_to_pass tests: basic create/list, edge cases (empty list, delete non-existent, delete first task)
- Verify that IDs remain consistent and no IndexError occurs after deletions.

This task requires the agent to trace the data flow between task creation, ID assignment, deletion, and listing — a realistic multi-step debugging scenario.
