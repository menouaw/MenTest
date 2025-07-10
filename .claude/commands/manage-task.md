# Manage TASK List

This command standardises how the AI assistant reads, updates, and maintains the project task tracker in **TASK.md**.

## Target File: TASK.md
 
## Usage Scenarios
- **Before starting any new piece of work**: Verify the task exists in TASK.md; if not, create it.
- **During development**: Add "Discovered During Work" subtasks for any new findings.
- **After completing work**: Mark the task (and related subtasks) as completed and record the completion date.

## Process

1. **Initial Review**
   - Open TASK.md and locate the section corresponding to the current task.
   - Note existing status (`pending`, `in_progress`, `completed`).

2. **Add Missing Tasks**
   - If no entry exists, append a new bullet under the appropriate section with:
     - Task title
     - Brief description
     - Creation date (YYYY-MM-DD)
     - Initial status: `pending`

3. **Status Updates**
   - When work begins, change status to `in_progress`.
   - Upon completion, update status to `completed` and add completion date.

4. **Discovered During Work**
   - For any new subtasks or follow-ups, add them under a **“Discovered During Work”** heading.

5. **Validation & Commit**
   - Ensure Markdown list formatting remains intact.
   - Confirm no merge conflicts or duplicate entries.

## Checklist (Pass/Fail)
- [ ] Current task entry exists with correct status.
- [ ] New tasks or subtasks added where necessary.
- [ ] Completed tasks marked with date.
- [ ] Markdown formatting preserved.

---

*If TASK.md grows beyond readability, consider refactoring into dated sections or archived files.*