# Changelog

All notable changes to the autodocs skill will be documented in this file.

## [2.2.2] - 2026-03-27

### 🐛 Bug Fixes

#### 1. Agent 在文档中编造 QS 分数

- **问题**: Agent 在文档中自己写 "质量评分: QS = 0.92"，这是虚假信息
- **根因**: SKILL.md 和 program.md 没有明确禁止在文档中包含 QS 分数
- **修复**:
  - SKILL.md 新增规则 #7: "Do NOT include QS scores in documents"
  - program.md 新增警告：QS 由 verify.py 计算，不应该出现在文档中
  - program.md 新增约束 #12: "不能在文档中编造 QS 分数"

**影响**: 修复后，Agent 不会在文档中编造 QS 分数，QS 只能由 verify.py 脚本计算。

---

### 📝 Documentation Updates

#### SKILL.md

- ✅ 新增规则 #7: 禁止在文档中包含 QS 分数

#### references/program.md

- ✅ QS 部分新增警告：QS 由 verify.py 计算，不应该出现在文档中
- ✅ 新增约束 #12: 不能在文档中编造 QS 分数

---

### 🎯 Summary

| 类别 | 变更数 |
|------|--------|
| Bug Fixes | 1 |
| Documentation Updates | 2 |

**核心改进：**
- ✅ 修复 Agent 在文档中编造 QS 分数的问题
- ✅ 明确 QS 只能由 verify.py 计算
- ✅ 防止虚假质量评分出现在文档中

---

**维护者**: Sisyphus Agent
**更新时间**: 2026-03-27

## [2.2.1] - 2026-03-27

### 🐛 Bug Fixes

#### 1. Agent 创建错误的文档目录结构

- **问题**: Agent 创建 `.autodocs/docs/` 子目录，导致链接路径错误
- **根因**: SKILL.md 指示不够明确，没有明确禁止创建子目录
- **修复**:
  - SKILL.md 新增明确的文档结构示例（正确 vs 错误）
  - 新增规则 #2: "Do NOT create `.autodocs/docs/` subdirectory"
  - 强化链接前缀规则说明
  - 添加警告：最安全的方式是直接在 `.autodocs/` 下创建文档

**影响**: 修复后，Agent 会正确地将文档直接放在 `.autodocs/` 下，链接路径也会正确。

---

### 📝 Documentation Updates

#### SKILL.md

- ✅ 新增文档结构示例（正确 vs 错误）
- ✅ 新增规则 #2: 禁止创建 `.autodocs/docs/` 子目录
- ✅ 强化链接前缀规则说明
- ✅ 添加警告：最安全的方式是直接在 `.autodocs/` 下创建文档

---

### 🎯 Summary

| 类别 | 变更数 |
|------|--------|
| Bug Fixes | 1 |
| Documentation Updates | 1 |

**核心改进：**
- ✅ 修复 Agent 创建错误文档目录结构的问题
- ✅ 修复链接路径错误的问题
- ✅ SKILL.md 指示更明确

---

**维护者**: Sisyphus Agent
**更新时间**: 2026-03-27

## [2.2.0] - 2026-03-27

### 🔴 Breaking Changes

#### 1. SKILL.md 架构重构

**旧版本（v2.1）：**
- SKILL.md ~250 行，包含大量详细规范
- 与 references/program.md 重复内容较多

**新版本（v2.2）：**
- SKILL.md ~80 行，仅保留核心工作流
- 详细规范移至 references/ 目录
- 新增 "Skill Boundary" 部分明确 Agent 权限

**变更原因：**
- ✅ 遵循 baoyu-skills 设计模式（SKILL.md 是手册，不是代码）
- ✅ 减少重复内容，提高可维护性
- ✅ 明确 Agent 只能创建 `.autodocs/` 下的文件，不能修改 skill 文件

---

### 🐛 Bug Fixes

#### 1. Goodhart's Law 问题（虚假可信度标记）

- **问题**: Agent 为了追求高 QS 分数，将所有内容标记为 `[✅ 已验证]`，即使没有实际读取代码
- **根因**: QS 公式奖励 `[✅ 已验证]`，Agent 优化指标而非诚实标记
- **修复**:
  - SKILL.md 明确说明：`[✅ 已验证]` 必须引用具体代码行
  - 新增警告：`⚠️ [✅ 已验证] requires quoting the actual code. If you're guessing, use [❓ 推测]. Honesty matters more than completeness.`
  - 新增约束 #11: "不能追求 QS 分数 — 诚实标记比高分更重要"

#### 2. Agent 修改 skill 文件

- **问题**: Agent 将 SKILL.md、references/、scripts/ 视为项目代码并尝试修改
- **根因**: Skill 文件和项目代码在同一上下文中，没有明确边界
- **修复**:
  - SKILL.md 新增 "Skill Boundary" 部分（第 15-25 行）
  - 明确说明：Skill files 和 project code 都是只读的，只有 `.autodocs/` 输出文件可写
  - 新增规则 #1: "Only create files under `.autodocs/` — never edit SKILL.md, scripts/, or project code"

---

### ✨ Improvements

#### 1. 新增 DESIGN.md（问题注册表）

创建 `DESIGN.md` 文档，记录所有已知问题和解决方案：

| 问题 | 描述 | 解决方案 |
|------|------|----------|
| P1 | Agent 修改 skill 文件 | Skill Boundary 部分 |
| P2 | 虚假可信度标记 | 明确 `[✅ 已验证]` 要求 |
| P3 | 相对路径解析 | `find_project_root()` 动态解析 |
| P4 | 不必要的目录嵌套 | 文档直接放 `.autodocs/` |
| P5 | verify.py 脚本路径 | `{baseDir}/scripts/verify.py` 模式 |
| P6 | Agent Loop 使用 git reset | 文件备份/恢复代替 |
| P7 | SKILL.md 过长 | 精简至 ~80 行 |
| P8 | 触发短语过宽 | 收窄为明确的文档请求 |

**设计原则：**
1. SKILL.md 是手册，不是代码
2. Scripts 负责繁重工作
3. Agent 只创建，从不编辑
4. 诚实比完整更重要
5. 动态路径，无硬编码

#### 2. 新增 references/templates.md

创建文档模板文件，包含 4 种模板：

| 模板 | 用途 |
|------|------|
| Code Walkthrough | 深入导读特定功能、用户流程 |
| Component Documentation | 文档化单个组件、模块或类 |
| Architecture Overview | 高层系统架构、数据流 |
| API Documentation | 文档化 API 端点、请求/响应格式 |

**改进：**
- 从 references/program.md 移出模板内容
- 提供完整的 Markdown 模板示例
- 包含 Mermaid 图表示例
- 包含代码链接格式示例

#### 3. 精简 references/program.md

| 指标 | v2.1 | v2.2 | 变化 |
|------|------|------|------|
| 行数 | 512 行 | ~307 行 | -40% |

**移除内容：**
- Agent 迭代优化流程（已在 SKILL.md 中）
- 文档结构指导（移至 templates.md）
- Python 环境说明（非核心规范）
- 输出格式（非核心规范）
- 代码链接生成最佳实践（非核心规范）
- Mermaid 图表最佳实践（非核心规范）

**保留内容：**
- 使命和核心原则
- 三大支柱（标记系统、链接格式、可视化）
- QS 计算公式
- 约束列表
- 成功指标

#### 4. SKILL.md 进一步精简

| 指标 | v2.1 | v2.2 | 变化 |
|------|------|------|------|
| 行数 | ~250 行 | ~80 行 | -68% |

**保留内容：**
- Frontmatter（触发短语）
- Skill Boundary（Agent 权限）
- Workflow（3 个步骤）
- Rules（5 条规则）
- References（链接到详细文档）

**移至 references/：**
- 三大支柱详细说明 → references/program.md
- 文档模板 → references/templates.md
- 设计决策 → DESIGN.md

---

### 📝 Documentation Updates

#### 新增文件

- ✅ `DESIGN.md` — 已知问题和设计决策
- ✅ `references/templates.md` — 文档模板

#### 更新文件

- ✅ `SKILL.md` — 精简至 ~80 行，新增 Skill Boundary
- ✅ `references/program.md` — 精简至 ~307 行，移除非核心内容

#### 删除文件

- ✅ `scripts/results.tsv` — 临时结果文件
- ✅ `scripts/__pycache__/` — Python 缓存目录

---

### 🎯 Summary

| 类别 | 变更数 |
|------|--------|
| Breaking Changes | 1 |
| Bug Fixes | 2 |
| Improvements | 4 |
| Documentation Updates | 5 |

**核心改进：**
- ✅ SKILL.md 精简 68%，遵循 baoyu-skills 模式
- ✅ 新增 DESIGN.md 防止问题回归
- ✅ 新增 templates.md 提供完整模板
- ✅ 精简 program.md 40%，聚焦核心规范
- ✅ 修复 Goodhart's Law 问题（虚假可信度标记）
- ✅ 修复 Agent 修改 skill 文件问题

---

**维护者**: Sisyphus Agent
**更新时间**: 2026-03-27

## [2.1.0] - 2026-03-27

### 🔴 Breaking Changes

#### 1. Agent Loop 安全性重构

**旧版本（v2.0）：**
```
如果 QS 降低 → git reset 撤销
```

**新版本（v2.1）：**
```
如果 QS 降低 → 恢复备份（mv docs.backup/ docs/）
```

**变更原因：**
- ❌ `git reset` 会丢失用户未提交的修改（危险操作）
- ✅ 使用文件备份/恢复，不影响 git 状态
- ✅ 添加了明确的终止条件（最大轮次、QS 阈值、连续无提升）

---

### 🐛 Bug Fixes

#### 1. PENDING_CONFIRMATION.md 自动创建

- **问题**: v2.0 声称 QS < 0.7 时自动创建，但 verify.py 仅打印消息未实际创建
- **修复**: 新增 `create_pending_confirmation()` 函数，实际生成文件
- **新增函数**:
  - `get_unknown_items()` — 提取所有 `[🚫 未知]` 标记内容
  - `get_assumed_items()` — 提取所有 `[❓ 推测]` 标记内容

#### 2. 删除未使用的函数

- **删除**: `check_line_range_format()` — 定义但从未在 QS 计算中使用
- **影响**: 无（该函数从未影响评分结果）

#### 3. 脚本路径问题

- **问题**: SKILL.md 中 `cd .autodocs && python3 ../scripts/verify.py` 路径不明确
- **修复**: 改为从 skill 目录运行: `python3 <skill目录>/scripts/verify.py <docs_dir>`

#### 4. Agent 修改 skill 脚本

- **问题**: Agent 执行 verify.py 时，hook 检测到注释，Agent 尝试修改 skill 自带脚本
- **根因**: SKILL.md 没有明确禁止修改 skill 基础设施文件
- **修复**: 
  - SKILL.md 新增约束 #6: "不修改 skill 脚本"、#7: "不修改 skill 文件"
  - Step 4 添加警告: "不要将 verify.py 复制到 .autodocs/ 目录中"
  - references/program.md 约束 #6 更新: "不能修改 skill 脚本 — 只运行，不复制到项目目录，不修改其内容"

#### 5. 相对路径错误 — 链接无法定位文件

- **问题**: 文档位于 `.autodocs/docs/`，链接用 `./projects/...` 解析到错误路径
- **根因**: 硬编码目录深度和路径前缀，不支持灵活的文档组织
- **修复**:
  - 去掉 `.autodocs/docs/` 嵌套，文档直接放 `.autodocs/`
  - SKILL.md: 链接前缀由 agent 根据文档位置动态计算，不再硬编码
  - verify.py: 新增 `find_project_root()` 自动检测项目根目录
  - verify.py: 使用 `resolve()` 解析相对路径，不再假设固定深度
  - 支持文档子目录组织（`.autodocs/architecture/`、`.autodocs/api/` 等）

---

### ✨ Improvements

#### 1. SKILL.md 大幅精简

| 指标 | v2.0 | v2.1 | 变化 |
|------|------|------|------|
| 行数 | 555 行 | ~250 行 | -55% |
| 与 program.md 重复度 | 高 | 低 | 大幅减少 |

**改进方式：**
- 三大支柱详细说明移至 references/program.md
- 模板示例精简，完整版引用 references/
- 可信度标记规范精简为速查表

#### 2. 触发短语收窄

**移除的过宽触发短语：**
- ❌ `"代码是怎么工作的"` — 会与 explore agent 冲突
- ❌ `"explain the codebase"` — 同上

**保留的明确触发短语：**
- ✅ `"生成文档"`, `"create documentation"`, `"generate docs"`
- ✅ `"文档"`, `"autodocs"`, `"文档生成"`, `"代码导读"`

#### 3. 添加工具使用指引

新增执行步骤中的工具选择说明：
- 简单项目（<50 文件）→ 直接用 `glob` + `read` 工具
- 复杂项目（50+ 文件）→ 启动 `explore` agent 并行搜索
- 不熟悉的框架/库 → 启动 `librarian` agent 查文档

#### 4. verify.py 评分逻辑改进

| 函数 | 改进 |
|------|------|
| `check_honesty()` | 4 级评分（1.0/0.8/0.4/0.0）替代旧的 3 级 |
| `check_structure()` | 基于标记类型数量评分（3+ 种 = 1.0，2 种 = 0.7，1 种 = 0.4） |
| `check_accessibility()` | 检查 H1/H2/H3 层级 + 目录，替代简单的 `#` 计数 |
| `check_visual_quality()` | 基于图表数量评分（2+ = 1.0，1 = 0.7，0 = 0.0） |
| `check_link_validity()` | 新增行号有效性检查（不仅检查文件存在） |

#### 5. Mermaid 图表指引

新增图表类型选择表：

| 场景 | 图表类型 |
|------|----------|
| 用户操作流程 | `flowchart TD` |
| 系统架构 | `flowchart TB` + `subgraph` |
| API 调用链 | `sequenceDiagram` |
| 数据处理流程 | `flowchart LR` |

#### 6. 可信度标记格式统一

- 新文档统一使用完整格式: `[✅ 已验证]` `[⚙️ 自动提取]` `[❓ 推测]` `[🚫 未知]`
- 旧格式 `[✅]` `[⚙️]` `[❓]` `[🚫]` 仅作为兼容支持
- SKILL.md 和 verify.py 同步更新

#### 7. 语言风格统一

- SKILL.md 全部使用中文（v2.0 混用中英文）
- 英文术语仅在代码/格式中保留

---

### 📝 Documentation Updates

#### SKILL.md

- ✅ 精简至 ~250 行
- ✅ 添加工具使用指引
- ✅ 添加 Mermaid 图表类型选择表
- ✅ 修复脚本路径说明
- ✅ 添加 PENDING_CONFIRMATION.md 创建逻辑

#### references/program.md

- ✅ 重写 Agent Loop（安全迭代逻辑）
- ✅ 添加终止条件
- ✅ 添加安全原则说明
- ✅ 新增约束 #10: 不能使用 git reset

#### scripts/verify.py

- ✅ 删除未使用的 `check_line_range_format()`
- ✅ 改进 4 个评分函数
- ✅ 新增 `get_unknown_items()` / `get_assumed_items()`
- ✅ 新增 `create_pending_confirmation()` 自动创建逻辑
- ✅ 改进链接验证（检查行号有效性）

---

### 🎯 Summary

| 类别 | 变更数 |
|------|--------|
| Breaking Changes | 1 |
| Bug Fixes | 3 |
| Improvements | 7 |
| Documentation Updates | 3 |

**核心改进：**
- ✅ 安全的迭代逻辑（不再使用 git reset）
- ✅ PENDING_CONFIRMATION.md 自动创建实际生效
- ✅ SKILL.md 精简 55%，去重
- ✅ 评分逻辑更精细、更准确
- ✅ 触发短语收窄，减少误触发

---

**维护者**: Sisyphus Agent  
**更新时间**: 2026-03-27

## [2.0.0] - 2026-03-26

### 🏷️ Branding

- **Skill 重命名**: `doc-autoresearch` → `autodocs`
  - 更简洁直观
  - 强调"自动化"特性
  - 与输出目录 `.autodocs/` 保持一致

### 🔴 Breaking Changes

#### 1. 可信度标记系统重构

**旧版本（v1.x）：**
```markdown
[✅] 已验证（人工确认）
[⚙️] 自动提取（从代码）
[❓] 推测（AI 假设）
[🚫] 未知（待补充）
```

**新版本（v2.0）：**
```markdown
[✅ 已验证] - 代码已读取确认（自动化）
[⚙️ 自动提取] - 从配置/结构提取
[❓ 推测] - 基于模式推测
[🚫 未知] - 无法确定
```

**变更原因：**
- ❌ 移除"人工确认"概念（自动化工作流无需人工介入）
- ✅ 强调段落级标记（而非文档级）
- ✅ 明确标记含义（已验证 ≠ 人工确认）

#### 2. QS 阈值调整

| 指标 | 旧阈值 | 新阈值 |
|------|--------|--------|
| 合格 | QS >= 0.5 | QS >= 0.7 |
| 良好 | QS >= 0.8 | QS >= 0.8 |
| 优秀 | QS >= 0.9 | - |

**变更原因：**
- 提高文档质量门槛
- QS < 0.7 时自动触发人工确认流程

---

### ✨ New Features

#### 1. 段落级可信度标记

每个段落都可以独立标记可信度：

```markdown
[✅ 已验证] 这是一个消息队列处理循环（见 [main.cr:122](./src/main.cr#L122)）。

[⚙️ 自动提取] 依赖项：kemal（从 shard.yml 提取）。

[❓ 推测] 可能支持重试机制（见 [queue.cr:45](./src/queue.cr#L45)）。

[🚫 未知] 错误处理流程待确认。
```

#### 2. 人工确认文档机制

当 QS < 0.7 时，自动创建 `.autodocs/PENDING_CONFIRMATION.md`：

```markdown
# 📋 人工确认文档：项目架构说明

**状态**: 🔴 待确认
**当前 QS**: 0.65

## 需确认项列表

- [ ] **消息队列重试机制**
  - 推测：可能支持重试
  - 需确认：重试策略是什么？

- [ ] **错误处理流程**
  - 问题：错误分类不明确
  - 需确认：错误分级标准？
```

**工作流：**
```mermaid
flowchart TD
    A[生成文档] --> B{QS >= 0.7?}
    B -->|是| C[完成]
    B -->|否| D[创建 PENDING_CONFIRMATION.md]
    D --> E[用户填写确认]
    E --> F[重新运行 skill]
```

#### 3. Python 环境说明

- ✅ 仅使用 Python 标准库（无第三方依赖）
- ✅ 兼容 Python 3.6+
- ✅ 无需虚拟环境
- 📝 添加了虚拟环境方案（未来扩展用）

#### 4. 代码链接格式增强

新增表格行号范围格式：

```markdown
| 文件 | 行号 | 功能 |
|------|------|------|
| [main.cr](./src/main.cr#L10) | [L10-25](./src/main.cr#L10) | 初始化配置 |
```

---

### 📝 Documentation Updates

#### SKILL.md

- ✅ 重写"核心理念"部分
- ✅ 新增"人工确认文档机制"
- ✅ 更新 QS 计算权重
- ✅ 更新代码链接格式示例
- ✅ 更新使用场景（增加"代码导读"）

#### references/program.md

- ✅ 重写"三大支柱"
- ✅ 新增"段落级可信度标记"示例
- ✅ 新增"人工确认文档机制"
- ✅ 新增"Python 环境说明"
- ✅ 更新约束列表（新增"不能等待人工确认"）

#### scripts/verify.py

- ✅ 支持新可信度标记格式（`[✅ 已验证]`）
- ✅ 兼容旧格式（`[✅]`）
- ✅ 更新诚实度检查逻辑
- ✅ 更新 QS 阈值（0.5 → 0.7）
- ✅ 更新改进建议信息

---

### 🔧 Technical Details

#### QS 计算权重调整

| 维度 | 旧权重 | 新权重 |
|------|--------|--------|
| Structure | 25% | 20% |
| Honesty | 35% | 30% |
| Accessibility | 15% | 15% |
| LinkValidity | 15% | 20% |
| VisualQuality | 10% | 15% |

#### Python 依赖检查

```python
import re        # 标准库
import sys       # 标准库
from pathlib import Path      # 标准库
from datetime import datetime # 标准库
```

**结论：** 无第三方依赖，无需 `pip install`。

---

### 📚 Migration Guide

#### 从 v1.x 升级到 v2.0

1. **更新可信度标记**：
   - 旧：`[✅] 内容`
   - 新：`[✅ 已验证] 内容`

2. **调整 QS 预期**：
   - 旧：QS >= 0.5 合格
   - 新：QS >= 0.7 合格

3. **处理人工确认文档**：
   - 如果 QS < 0.7，会自动创建 `PENDING_CONFIRMATION.md`
   - 填写确认项后重新运行 skill

---

### 🎯 Summary

| 类别 | 变更数 |
|------|--------|
| Breaking Changes | 2 |
| New Features | 4 |
| Documentation Updates | 3 |
| Technical Improvements | 2 |

**核心改进：**
- ✅ 完全自动化工作流（无需人工介入）
- ✅ 段落级可信度标记
- ✅ 自动触发人工确认机制
- ✅ 零第三方依赖

---

**维护者**: Sisyphus Agent  
**更新时间**: 2026-03-26
