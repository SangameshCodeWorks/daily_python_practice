# Daily Python Practice Workflow & Standards Rule

Whenever the user adds new Python practice files, asks for documentation, or practices new modules in this repository, follow this automated procedure without requiring repetitive prompts or reminders from the user.

## 1. Educational Enhancement Standard
Format every Python practice module with the established repository design pattern:

### A. Module Header Banner
```python
# ==============================================================================
# Module: <Filename.py>
# Topic: <Descriptive Topic Title>
# ==============================================================================
```

### B. Structured Concept Blocks
Break every concept down into numbered sections containing the 3 mandatory pillars:
```python
# ------------------------------------------------------------------------------
# <N>. <Feature / Concept Name>
# • What is it for:
#   <Why this concept exists and what goal it achieves>
# • What it does:
#   <Step-by-step evaluation mechanics and value flow>
# • Where it is used:
#   <Concrete real-world applications and engineering scenarios>
# ------------------------------------------------------------------------------
```

### C. Code & Annotations
- Preserve all existing code, functions, variables, and logic.
- Add descriptive inline annotations next to `print(...)` and critical statements indicating exact evaluated results (`# Result: ...`).
- When gotchas or common interview questions appear (e.g. `is` vs `==`, dict membership on keys vs items, short-circuiting returns), explicitly highlight them.

## 2. Testing & Verification
Always execute the script using the shell before finishing:
```powershell
python <Filename.py>
```
Confirm zero runtime errors, zero syntax errors, and that output matches comments.

## 3. Sync README.md Automatically
- Add the day and module to the **Learning Roadmap Overview** table.
- Add the itemized bullet points to **Daily Practiced Concepts & File Mappings**.
- Add the CLI test command to **How to Run Any Practice Script**.

## 4. Sync TODO.md Automatically
- Mark the completed day with `[x]` under **Completed Practice Modules** with clickable links to the files.
- Update the **Quick Progress Summary** counters (completed days, total scripts).
- Keep the **Upcoming Learning Modules** current.
