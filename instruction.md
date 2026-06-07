# Fix Task Deletion Bug in Python Task Manager

## Bug Description

The Task Manager application has a bug in its task deletion feature. When a task is deleted by its ID, the internal list handling causes subsequent operations (such as listing remaining tasks or deleting another task) to fail or behave incorrectly.

## Expected Behavior

- Deleting a task by its valid ID should permanently remove it from the list.
- Remaining tasks should keep their original IDs unchanged.
- The `list_tasks()` method should correctly show all remaining tasks after any number of deletions.
- Multiple deletions in sequence should work without errors or crashes.
- No IndexError or ID lookup failures should occur after deletions.

## Steps to Reproduce

1. Create three tasks with IDs 1, 2, and 3.
2. Delete the task with ID 2.
3. Attempt to list all remaining tasks.
4. Try to delete the task with ID 3.

The application fails or shows incorrect results in steps 3 or 4.
