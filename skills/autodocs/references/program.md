# Autodocs: 自动化文档生成规范

## 使命

为代码项目生成**可信**、**可追溯**、**可视化**的开发者文档——完全自动化，无需人工介入。

## 核心原则

**我们追求的不是「完整」，而是「诚实」「精确」与「可理解」**

- ✅ 仅从现有代码/配置提取信息，不编造
- ✅ 所有推测必须注明依据
- ✅ 每个段落标记可信度
- ✅ 每个代码引用包含精确链接
- ✅ 每个架构包含可视化图表
- ❌ 不需要人工介入即可完成初始文档

---

## 三大支柱

### 支柱 1: 段落级可信度标记系统（必须使用）

**每个内容段落都必须标记可信度：**

| 标记 | 含义 | 使用场景 | 示例 |
|------|------|----------|------|
| `[✅ 已验证]` | 代码已读取确认 | 直接从代码中读取并验证的内容 | `[✅ 已验证] 这是一个消息队列处理循环（见 [main.cr:122](./src/main.cr#L122)）` |
| `[⚙️ 自动提取]` | 从配置/结构提取 | 从 package.json、目录结构、注释等自动提取 | `[⚙️ 自动提取] 依赖：kemal（从 shard.yml 提取）` |
| `[❓ 推测]` | 基于模式推测 | 无法从代码确认但根据模式可能存在 | `[❓ 推测] 可能支持 WebSocket（见 [routes.cr:45](./src/routes.cr#L45)）` |
| `[🚫 未知]` | 无法确定 | 确实无法从现有信息确定的内容 | `[🚫 未知] 错误处理流程待确认` |

**段落级标记示例：**

```markdown
## 核心模块

[✅ 已验证] 调度器模块是一个循环处理消息队列的逻辑（见 [scheduler.cr:122](./src/scheduler.cr#L122)）。
代码结构如下：
\`\`\`crystal
loop do
  message = queue.receive()
  process(message)
end
\`\`\`

[⚙️ 自动提取] 依赖项列表：
- kemal (从 shard.yml 提取)
- redis (从 shard.yml 提取)

[❓ 推测] 可能支持消息重试机制（见 [queue.cr:45](./src/queue.cr#L45)），但未找到明确实现。

[🚫 未知] 以下内容无法从现有代码确定：
- 错误处理流程
- 性能瓶颈点
- 高可用方案
```

**自动化工作流原则：**
- ✅ 仅从现有代码/配置提取信息
- ✅ 所有推测必须注明依据
- ❌ 不编造无法验证的内容
- ❌ 不需要人工介入即可完成初始文档

### 人工确认文档机制

当自动化生成的文档可信度不足时（QS < 0.7），系统会自动创建人工确认文档：

**文件**: `.autodocs/PENDING_CONFIRMATION.md`

```markdown
# 📋 人工确认文档：项目架构说明

**状态**: 🔴 待确认
**创建时间**: 2026-03-26 14:30:00
**当前 QS**: 0.65

---

## 需确认项列表

### 🔴 高优先级（影响文档核心准确性）

- [ ] **消息队列重试机制**
  - 推测：可能支持重试（见 [queue.cr:45](./src/queue.cr#L45)）
  - 问题：未找到明确的重试次数和策略
  - 需确认：重试机制是否存在？具体策略是什么？

- [ ] **错误处理流程**
  - 推测：见 `rescue` 块（见 [handler.cr:78](./src/handler.cr#L78)）
  - 问题：错误分类和恢复策略不明确
  - 需确认：错误分级标准是什么？

### 🟡 中优先级（影响文档完整性）

- [ ] **性能瓶颈点**
  - 问题：无法从代码分析确定性能瓶颈
  - 需确认：已知性能问题点

---

## 确认后操作

1. 填写上述确认项
2. 重新运行 skill：`autodocs`
3. 系统将读取本文件并更新文档

---

**说明**: 自动化文档生成时无法确定以上内容，请人工确认后重新运行 skill。
```

**工作流：**

```mermaid
flowchart TD
    A[用户触发 skill] --> B[Agent 读取代码]
    B --> C[生成文档 + QS 计算]
    C --> D{QS >= 0.7?}
    D -->|是| E[文档完成]
    D -->|否| F[创建 PENDING_CONFIRMATION.md]
    F --> G[用户看到 🔴 待确认状态]
    G --> H[用户填写确认项]
    H --> I[重新触发 skill]
    I --> J[Agent 读取确认文档]
    J --> K[生成增强文档]
    K --> E
```

---

### 支柱 2: 精确代码链接系统（必须使用）

**所有代码引用必须遵循以下格式：**

#### 格式 1: 单行引用（文本内联）

```markdown
核心调度逻辑见 [scheduler.cr:122](./src/scheduler.cr#L122)
```

#### 格式 2: 行范围引用（表格索引）

```markdown
| 文件 | 行号 | 功能 |
|------|------|------|
| [main.cr](./src/main.cr#L10) | [L10-25](./src/main.cr#L10) | 初始化配置 |
| [api.ts](./src/api.ts#L44) | [L44-52](./src/api.ts#L44) | API 调用函数 |
```

#### 格式 3: 文件标题引用

```markdown
**文件**: [projects/eulermaker-cbs-web/src/page/projects/index.vue](./projects/eulermaker-cbs-web/src/page/projects/index.vue)

这是用户创建工程的入口...
```

**禁止模糊引用：**
- ❌ `在 scheduler.cr 中...`
- ❌ `scheduler 文件的某个函数`
- ❌ `根据代码分析...`（无链接）
- ✅ `[scheduler.cr:122](./src/scheduler.cr#L122)`

### 支柱 3: 可视化架构系统（必须使用）

**使用 Mermaid 图表增强可理解性：**

#### 流程图 (flowchart TD/TB/LR)

```mermaid
flowchart TD
    A[用户操作] --> B[前端页面]
    B --> C[Nginx代理]
    C --> D[API Gateway]
    D --> E[Python后端]
```

#### 时序图 (sequenceDiagram)

```mermaid
sequenceDiagram
    participant U as 用户
    participant F as 前端
    participant G as Gateway
    participant B as 后端
    U->>F: 点击按钮
    F->>G: HTTP POST
    G->>B: 转发请求
    B-->>G: 返回结果
```

#### 架构图（带子图）

```mermaid
flowchart TB
    subgraph Frontend["前端层"]
        F1[Vue组件]
        F2[API调用]
    end
    subgraph Backend["后端层"]
        B1[Flask路由]
        B2[业务逻辑]
    end
    Frontend --> Backend
```

---

## 质量分数 (QS)

每次迭代后，运行 `python verify.py` 计算 QS。

### QS 计算公式

```
QS = w1×Structure + w2×Honesty + w3×Accessibility + w4×LinkValidity + w5×VisualQuality
```

| 维度 | 权重 | 检查项 |
|------|------|--------|
| Structure | 20% | 是否使用段落级可信度标记 |
| Honesty | 30% | 是否诚实标记未知内容（[🚫 未知]） |
| Accessibility | 15% | 是否有清晰的章节结构 |
| LinkValidity | 20% | 代码链接是否有效且准确 |
| VisualQuality | 15% | 是否包含 Mermaid 可视化图表 |

### QS 阈值与自动处理

- **QS >= 0.8**: ✅ 文档质量良好，完成
- **QS >= 0.7**: ⚠️ 文档质量一般，建议补充
- **QS < 0.7**: ❌ 文档质量不足，自动创建 `PENDING_CONFIRMATION.md`

### 自动触发人工确认

当 QS < 0.7 时，系统会：
1. 创建 `.autodocs/PENDING_CONFIRMATION.md`
2. 列出所有 `[🚫 未知]` 标记的内容
3. 等待用户填写确认信息后重新运行 skill

---

## Agent 循环

```
LOOP FOREVER:
1. 读取 docs/ 目录下的文档
2. 分析当前 QS 和各维度分数
3. 提出改进想法（如：添加缺失标记、改善结构、修复链接、添加图表）
4. 修改文档
5. 运行 python verify.py 获取新 QS
6. 如果 QS 提高 → 保持更改
   如果 QS 降低 → git reset 撤销
   如果崩溃 → 尝试修复（最多 3 次）
7. 记录到 results.tsv
8. 继续
```

---

## 约束（Agent 不能做）

1. **不能创建未标记的内容** — 任何段落必须有可信度标记
2. **不能使用模糊代码引用** — 必须包含精确的文件路径和行号
3. **不能编造信息** — 无法从代码确认的内容必须标记为 `[🚫 未知]`
4. **不能假设环境** — 不要写"只需要运行 npm install"，除非确认了依赖
5. **不能忽略未知** — 如果不知道某些内容，用 `[🚫 未知]` 标记
6. **不能修改 verify.py** — 验证脚本是唯一的 truth source
7. **不能删除诚实标记** — 已标记为 `[❓ 推测]` 或 `[🚫 未知]` 的内容不能改为无标记
8. **不能缺少可视化** — 文档必须包含至少一个 Mermaid 图表
9. **不能等待人工确认** — 必须完成自动化文档生成，即使有未知内容

---

## 文档结构指导（参考，非强制）

### 代码导读文档结构

```markdown
# [项目名] [功能名] 代码导读

> **目标**: 通过 [场景描述]，深入导读整个代码流程
> **创建时间**: YYYY-MM-DD
> **更新时间**: YYYY-MM-DD

## 目录

- [整体流程概览](#整体流程概览)
- [Phase 1: xxx](#phase-1-xxx)
- [附录](#附录)

## 整体流程概览

[mermaid flowchart]

## Phase 1: [阶段名]

### 第 1 步：[步骤描述]

**文件**: [filename.ext](./path/to/filename.ext)

**关键代码位置**：

| 行号 | 功能 | 说明 |
|------|------|------|
| [L24-29](./path#L24) | xxx | xxx |

**核心代码**：

```language
// 从第 XX 行开始
代码片段...
```

## 附录

### 关键文件路径
```

如果项目状态不明确，按以下优先级输出：

| 项目阶段 | 优先级 | 可简略 |
|----------|--------|--------|
| 早期原型 | README + 一句话描述 | 安装步骤、API 文档 |
| 成长期 | Quick Start + 核心概念 | 完整架构设计 |
| 成熟期 | API 参考 + 故障排查 | 从 0 开始的 Tutorial |
| 维护/遗产 | 迁移指南 + 遗留风险 | 新功能文档 |

---

## 成功指标

- QS >= 0.8：文档质量良好
- QS >= 0.7：文档质量可接受
- 段落级可信度标记覆盖率 100%
- 代码链接有效率 100%
- 可视化图表 ≥ 1 个

---

## Python 环境说明

### 依赖情况

`verify.py` **仅使用 Python 标准库**，无需安装第三方依赖：

```python
import re        # 标准库：正则表达式
import sys       # 标准库：系统参数
from pathlib import Path      # 标准库：路径处理
from datetime import datetime # 标准库：时间处理
```

### 兼容性

- ✅ Python 3.6+
- ✅ 无需虚拟环境
- ✅ 无需 pip install

### 未来扩展

如果未来需要添加第三方依赖（如 `pyyaml`、`requests` 等），建议：

1. **创建虚拟环境**（可选）：
```bash
cd .autodocs
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows
```

2. **安装依赖**：
```bash
pip install -r requirements.txt
```

3. **requirements.txt 示例**：
```
# 当前无需依赖，仅示例
# pyyaml>=6.0
# requests>=2.28.0
```

---

## 输出格式

每次迭代记录到 `results.tsv`：

```
timestamp	qs	change_summary
2026-03-26T10:30:00	0.82	添加了架构流程图
```

---

## 代码链接生成最佳实践

### 使用 grep/ripgrep 定位代码

```bash
# 基础用法：查找关键字并显示行号
grep -n "def schedule" src/scheduler.cr
rg -n "def schedule" src/

# 输出示例：
# src/scheduler.cr:122:def schedule
# src/scheduler.cr:145:def schedule_all
```

### 验证行号范围

```bash
# 查看第 122 到 135 行（确认函数边界）
sed -n '122,135p' src/scheduler.cr

# 或使用 head/tail
head -n 135 src/scheduler.cr | tail -n 14
```

### 生成 Markdown 链接

```markdown
<!-- 单行引用 -->
[scheduler.cr:122](./src/scheduler.cr#L122)

<!-- 行范围引用 -->
| [L122-135](./src/scheduler.cr#L122) | schedule函数定义 |
```

---

## Mermaid 图表最佳实践

### 流程图节点命名

```mermaid
flowchart TD
    A["用户操作<br/>点击按钮"] --> B["前端响应"]
```

- 使用方括号 `["文本"]` 包含描述
- 使用 `<br/>` 换行
- 节点 ID 简短（A, B, C）

### 时序图参与者

```mermaid
sequenceDiagram
    participant U as 用户
    participant F as 前端
    participant G as Gateway
    participant B as 后端
```

- 使用 `participant Xxx as 别名` 提高可读性
- 参与者命名清晰（用户、前端、后端）

### 子图组织

```mermaid
flowchart TB
    subgraph Frontend["前端层"]
        F1[组件]
    end
    subgraph Backend["后端层"]
        B1[服务]
    end
```

- 使用 `subgraph Name["显示名"]`
- 按职责分组

---

**记住：文档的价值在于「可信」、「可追溯」和「可理解」。每个代码引用都应该是可点击、可验证的，每个架构都应该是可视化的。**
