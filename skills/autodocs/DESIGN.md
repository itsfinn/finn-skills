# Autodocs Design Decisions

Known issues and their solutions. Read this before modifying the skill.

## Problems Solved

### P1: Agent modifies skill files

- **Symptom**: Agent treats SKILL.md and scripts/ as project code and tries to edit them
- **Root cause**: Skill files and project code in same context, no clear boundary
- **Solution**: SKILL.md has "Skill Boundary" section at top. Agent only creates files in `.autodocs/`, never edits existing files
- **Anti-regression**: The boundary section must remain the first content after the frontmatter

### P2: False credibility marking

- **Symptom**: Agent marks everything as `[✅ 已verified]` even without reading the code, to get high QS
- **Root cause**: Goodhart's Law — QS formula rewards `[✅ 已verified]`, so agent games the metric
- **Solution**: `[✅ 已verified]` requires quoting specific code. Default to `[❓ 推测]` when uncertain. Agent must NOT optimize for QS
- **Anti-regression**: Keep the "verified requires evidence" rule prominent in SKILL.md

### P3: Relative path resolution

- **Symptom**: Links like `./src/foo.cr` in `.autodocs/doc.md` resolve to `.autodocs/src/foo.cr` (wrong)
- **Root cause**: Docs in `.autodocs/` use `./` prefix which resolves relative to doc location, not project root
- **Solution**: verify.py uses `find_project_root()` and strips `../`/`./` prefix before resolving. Agent can use any prefix depth
- **Anti-regression**: verify.py must always resolve links relative to project root, not docs_dir

### P4: Unnecessary directory nesting

- **Symptom**: `.autodocs/docs/` adds a useless nesting level
- **Root cause**: No reason for the extra `docs/` directory
- **Solution**: Docs go directly in `.autodocs/`. Subdirectories (architecture/, api/) are optional for organization
- **Anti-regression**: All examples and verify.py assume `.autodocs/` as the docs root

### P5: verify.py script path

- **Symptom**: Agent copies verify.py to project directory or doesn't know how to run it
- **Root cause**: SKILL.md didn't clearly specify where the script lives and how to call it
- **Solution**: Use `{baseDir}/scripts/verify.py` pattern. Agent runs from project root, passes docs dir as argument
- **Anti-regression**: verify.py takes docs_dir as sys.argv[1], no hardcoded paths

### P6: Agent Loop with git reset

- **Symptom**: Iterative improvement uses `git reset` which loses uncommitted changes
- **Root cause**: Original design assumed clean git state
- **Solution**: Use file backup/restore instead of git. Backup to `.autodocs.backup/` outside `.autodocs/`
- **Anti-regression**: Never use git reset in iteration flow

### P7: SKILL.md too long

- **Symptom**: 555 lines with duplicated content from program.md
- **Root cause**: All details inlined in SKILL.md
- **Solution**: SKILL.md is thin (~80 lines). Details in references/. Agent loads references only when needed
- **Anti-regression**: If SKILL.md approaches 150 lines, move content to references/

### P8: Trigger phrases too broad

- **Symptom**: "代码是怎么工作的" triggers autodocs instead of explore agent
- **Root cause**: Overlapping with general code understanding tasks
- **Solution**: Only trigger on explicit documentation requests (生成文档, create documentation, etc.)
- **Anti-regression**: Test trigger phrases against common non-doc tasks before adding new ones

## Design Principles

1. **SKILL.md is a manual, not code** — It tells the agent WHAT to do and HOW to run scripts, not how to implement the logic
2. **Scripts do heavy lifting** — Verification, formatting, etc. go in scripts/. Agent orchestrates, doesn't implement
3. **Agent creates, never edits** — Only `.autodocs/` output files are writable
4. **Honesty over completeness** — `[❓ 推测]` is better than fake `[✅ 已verified]`
5. **Dynamic paths** — No hardcoded directory depth. verify.py finds project root dynamically
