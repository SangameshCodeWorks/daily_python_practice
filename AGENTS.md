# AGENTS.md — Workspace Guidelines for Daily Python Practice

This repository is dedicated to daily Python practice and fundamentals mastery. Any agent operating in this workspace must adhere to the following workflow automatically without needing repeated instructions from the user.

---

## 🎯 Mandatory Automation for Upcoming Practice Files

Whenever the user adds new `.py` practice files or mentions that new modules have been created:

### 1. Code Structuring & Educational Commenting
Each module must follow the established educational standard:
1. **Module Header Banner**:
   ```python
   # ==============================================================================
   # Module: <filename>.py
   # Topic: <Concise, Descriptive Topic Title>
   # ==============================================================================
   ```
2. **Section Commentary Blocks**:
   Each concept must include:
   - `# • What is it for:`
   - `# • What it does:`
   - `# • Where it is used:`
3. **Inline Result Annotations**:
   - Annotate evaluated outputs (e.g. `# Result: <value>`).
   - Preserve all existing user code and variables.

### 2. Execution Testing
- Run `python <filename>.py` to verify error-free execution and output correctness.

### 3. Synchronize `README.md`
- Add the day and file mapping to the **Learning Roadmap Overview** table.
- Detail the bulleted concept list under **Daily Practiced Concepts & File Mappings**.
- Provide sample terminal run commands under **How to Run Any Practice Script**.

### 4. Synchronize `TODO.md`
- Check off the completed day `[x]` with clickable links to the files under **Completed Practice Modules**.
- Update the counter in **Quick Progress Summary**.
