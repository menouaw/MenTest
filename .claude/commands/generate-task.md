# Create TASK Document

## Output File: TASK.md

Generate or refresh **TASK.md** to act as the authoritative backlog, tracking work items and their lifecycle. The file should be human-readable, merge-friendly, and easy for automation to parse.

---

## Research Process

1. **Collect Requirements & Features**
   - Review `INITIAL.md`, open PRPs, and existing command files for referenced tasks.
   - Inspect codebase TODO comments and open Git issues (if any).

2. **Prioritisation & Grouping**
   - Cluster tasks by feature area or milestone.
   - Identify dependencies and approximate ordering.

3. **Status Alignment**
   - Determine current state (`pending`, `in_progress`, `completed`) for each item.
   - Cross-check with git history to spot already-addressed tasks.

---

## TASK.md Structure

```markdown
# Task Tracker

## Backlog
- [ ] YYYY-MM-DD | **Task Title** – brief description (status: pending)

## In Progress
- [ ] YYYY-MM-DD | **Task Title** – description (status: in_progress)

## Completed
- [x] YYYY-MM-DD | **Task Title** – description (status: completed)

## Discovered During Work
- [ ] YYYY-MM-DD | **Task Title** – description (status: pending)
```

*Use checkboxes for quick visual feedback; include dates for traceability.*

---

## Implementation Blueprint

1. Draft headings and template rows as shown above.
2. Populate tasks collected during research into appropriate sections.
3. Sort by priority/date within each section.
4. Keep line length reasonable (< 120 chars) for readability.
5. Ensure Markdown renders correctly.

---

## Validation Gates (Executable)
```bash
# Style / Lint
markdownlint TASK.md
# Basic schema check (optional – implement script later)
```

---

## Quality Checklist
- [ ] Sections present (Backlog, In Progress, Completed, Discovered During Work).
- [ ] Every task has date, title, description, and status.
- [ ] Checkboxes correctly reflect status.
- [ ] No duplicate task titles.
- [ ] Lint passes (`markdownlint`).
- [ ] ≤ 500 lines.

> **Goal**: Provide an up-to-date, actionable task list that integrates smoothly with development workflow and automation. 