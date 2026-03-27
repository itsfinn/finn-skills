---
name: autodocs
description: >-
  Generate credible developer documentation with precise code references and visual diagrams.
  Use when user explicitly asks to generate/create/write project documentation, API docs, or code walkthroughs.
  Triggers: "generate docs", "create documentation", "文档", "代码导读", "write docs", "autodocs".
  Do NOT trigger for: code queries, bug fixes, refactoring, or general code understanding tasks.
  Output: Markdown docs with credibility markers, code links, and Mermaid diagrams in .autodocs/.
---

# Autodocs

Generate credible, traceable, visual developer documentation.

## Skill Boundary

You are a **user** of this skill, not a maintainer.

| Scope | Action |
|-------|--------|
| Skill files (SKILL.md, references/, scripts/) | **Read only** — never edit or copy |
| Project code (what you document) | **Read only** — never edit |
| `.autodocs/` output files | **Write** — this is your only output |

Skill files are your "manual." Project code is your "analysis target." You only create new files in `.autodocs/`.

## Workflow

### 1. Explore the codebase

Use `glob`, `read`, and `grep` tools (or `explore` agent for large codebases) to understand the project structure.

### 2. Generate documentation

Create `.autodocs/` directory in project root. **Generate markdown files directly in `.autodocs/`** — do NOT create subdirectories like `.autodocs/docs/`.

**Correct structure**:
```
project-root/
├── .autodocs/
│   ├── architecture.md
│   ├── api.md
│   └── deployment.md
└── src/
```

**Incorrect structure** (do NOT do this):
```
project-root/
├── .autodocs/
│   └── docs/              ← ❌ Do NOT create this
│       ├── architecture.md
│       └── api.md
└── src/
```

**Link format**: Links must point to project root source files. Calculate the relative path prefix based on your output file location:

```
.autodocs/doc.md          → [file](./src/file.cr#L10)
.autodocs/arch/doc.md     → [file](../src/file.cr#L10)
.autodocs/a/b/doc.md      → [file](../../src/file.cr#L10)
```

> ⚠️ **Important**: If you create subdirectories under `.autodocs/` (like `.autodocs/architecture/`), adjust your link prefix accordingly. The safest approach is to put all docs directly in `.autodocs/` and use `./` prefix.

**Credibility markers** (every paragraph needs one):

| Marker | Meaning | When to use |
|--------|---------|-------------|
| `[✅ 已验证]` | Verified | You read the specific code line and can quote it |
| `[⚙️ 自动提取]` | Extracted | From config files, package.json, YAML, etc. |
| `[❓ 推测]` | Inferred | Saw partial code, cannot fully confirm |
| `[🚫 未知]` | Unknown | Cannot find evidence |

> ⚠️ `[✅ 已验证]` requires quoting the actual code. If you're guessing, use `[❓ 推测]`. Honesty matters more than completeness.

### 3. Verify quality (optional, user-initiated)

```bash
python3 {baseDir}/scripts/verify.py .autodocs/
```

Replace `{baseDir}` with this skill's directory path. Do NOT copy verify.py to the project.

## Rules

1. Only create files under `.autodocs/` — never edit SKILL.md, scripts/, or project code
2. **Do NOT create `.autodocs/docs/` subdirectory** — put docs directly in `.autodocs/`
3. Every paragraph must have a credibility marker
4. Every code reference must include a clickable link with line number
5. Include at least one Mermaid diagram per document
6. Do NOT optimize for QS score — honest marking is more important than high scores

## References

| Document | Contents |
|----------|----------|
| [references/program.md](./references/program.md) | Full specification: marker system, link formats, visualization, QS formula |
| [references/templates.md](./references/templates.md) | Document templates for different doc types |
| [DESIGN.md](./DESIGN.md) | Known issues and design decisions (read before modifying this skill) |
