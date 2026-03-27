# Autodocs Document Templates

Templates for different types of documentation. Use these as starting points when generating docs.

## Template 1: Complete Workflow (完整工作流程)

**Use for**: End-to-end workflow documentation for developers who want to understand how the system works from start to finish.

**Target audience**: New developers, project developers, anyone learning the module.

**Key questions this template answers**:
- How to deploy the system from scratch?
- Where is the entry point?
- How does the program flow from A to B to C?
- How does data flow through the system?
- What are the key decision points?

```markdown
# [系统名] 完整工作流程

> **目标**: 从部署到运行的完整流程，帮助开发者理解整个系统如何工作
> **创建时间**: YYYY-MM-DD

## 目录

- [快速开始](#快速开始)
- [完整工作流程](#完整工作流程)
- [关键数据流](#关键数据流)
- [常见场景](#常见场景)
- [故障排查](#故障排查)

---

## 快速开始

### 5 分钟理解系统

[✅ 已验证] 系统的核心流程是：[一句话描述核心流程]（见 [main.ts:10](./src/main.ts#L10)）。

**关键概念**：
- [概念1]: [一句话解释]
- [概念2]: [一句话解释]
- [概念3]: [一句话解释]

---

## 完整工作流程

### 阶段 1: 部署启动

**从零到运行的步骤**：

#### 步骤 1.1: [部署步骤]

[✅ 已验证] 部署文件：[deployment.yaml](./deployment.yaml#L1)

**做什么**：
- [动作1]
- [动作2]

**为什么**：
- [原因1]
- [原因2]

**验证**：
```bash
# 验证部署成功
kubectl get pods -n <namespace>
```

#### 步骤 1.2: [初始化步骤]

[✅ 已验证] 初始化代码：[init.ts:20](./src/init.ts#L20)

**做什么**：
- [动作1]
- [动作2]

**关键代码**：
```typescript
// 从第 20 行开始
代码片段...
```

**数据流**：
```
[输入数据] → [处理1] → [处理2] → [输出数据]
```

---

### 阶段 2: 程序入口

**程序从哪里开始**：

#### 入口点 1: [入口名称]

[✅ 已验证] 入口代码：[entry.ts:10](./src/entry.ts#L10)

**触发条件**：
- [条件1]
- [条件2]

**执行流程**：
```
[入口] → [步骤1] → [步骤2] → [步骤3]
```

**关键代码**：
```typescript
// 从第 10 行开始
代码片段...
```

#### 入口点 2: [入口名称]

[✅ 已验证] 入口代码：[entry2.ts:5](./src/entry2.ts#L5)

**触发条件**：
- [条件1]
- [条件2]

---

### 阶段 3: 核心流程

**程序如何跳转**：

#### 流程 1: [流程名称]

[✅ 已验证] 流程代码：[flow.ts:30](./src/flow.ts#L30)

**完整流程**：
```
[A] → [B] → [C] → [D]
  ↓     ↓     ↓     ↓
[数据] [数据] [数据] [数据]
```

**步骤详解**：

**步骤 1**: [步骤名称]
- **文件**: [file1.ts:10](./src/file1.ts#L10)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]
- **关键代码**:
  ```typescript
  代码片段...
  ```

**步骤 2**: [步骤名称]
- **文件**: [file2.ts:20](./src/file2.ts#L20)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]
- **关键代码**:
  ```typescript
  代码片段...
  ```

**步骤 3**: [步骤名称]
- **文件**: [file3.ts:30](./src/file3.ts#L30)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]
- **关键代码**:
  ```typescript
  代码片段...
  ```

#### 流程 2: [流程名称]

[✅ 已验证] 流程代码：[flow2.ts:40](./src/flow2.ts#L40)

**完整流程**：
```
[A] → [B] → [C]
  ↓     ↓     ↓
[数据] [数据] [数据]
```

**步骤详解**：

**步骤 1**: [步骤名称]
- **文件**: [file4.ts:10](./src/file4.ts#L10)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]

**步骤 2**: [步骤名称]
- **文件**: [file5.ts:20](./src/file5.ts#L20)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]

---

### 阶段 4: 数据流转

**数据如何流动**：

#### 数据流 1: [数据流名称]

[✅ 已验证] 数据流代码：[dataflow.ts:50](./src/dataflow.ts#L50)

**完整数据流**：
```
[数据源] → [处理1] → [处理2] → [处理3] → [数据存储]
    ↓         ↓         ↓         ↓         ↓
  [格式1]   [格式2]   [格式3]   [格式4]   [格式5]
```

**阶段详解**：

**阶段 1**: 数据生成
- **文件**: [generator.ts:10](./src/generator.ts#L10)
- **数据格式**: [格式描述]
- **关键代码**:
  ```typescript
  代码片段...
  ```

**阶段 2**: 数据处理
- **文件**: [processor.ts:20](./src/processor.ts#L20)
- **数据格式**: [格式描述]
- **关键代码**:
  ```typescript
  代码片段...
  ```

**阶段 3**: 数据存储
- **文件**: [storage.ts:30](./src/storage.ts#L30)
- **数据格式**: [格式描述]
- **关键代码**:
  ```typescript
  代码片段...
  ```

#### 数据流 2: [数据流名称]

[✅ 已验证] 数据流代码：[dataflow2.ts:60](./src/dataflow2.ts#L60)

**完整数据流**：
```
[数据源] → [处理1] → [处理2] → [数据存储]
    ↓         ↓         ↓         ↓
  [格式1]   [格式2]   [格式3]   [格式4]
```

---

## 关键数据流

### 数据流图

```mermaid
flowchart LR
    A[数据源] --> B[处理1]
    B --> C[处理2]
    C --> D[处理3]
    D --> E[数据存储]
    
    style A fill:#e1f5ff
    style E fill:#e8f5e9
```

### 关键数据结构

#### 数据结构 1: [结构名称]

[✅ 已验证] 定义位置：[types.ts:10](./src/types.ts#L10)

**结构定义**：
```typescript
interface DataStructure {
  field1: string;
  field2: number;
  field3: boolean;
}
```

**字段说明**：
- `field1`: [说明]
- `field2`: [说明]
- `field3`: [说明]

#### 数据结构 2: [结构名称]

[✅ 已验证] 定义位置：[types2.ts:20](./src/types2.ts#L20)

**结构定义**：
```typescript
interface DataStructure2 {
  field1: string;
  field2: number;
}
```

**字段说明**：
- `field1`: [说明]
- `field2`: [说明]

---

## 常见场景

### 场景 1: [场景名称]

**场景描述**：[一句话描述场景]

**完整流程**：
```
[用户操作] → [系统响应] → [数据处理] → [结果返回]
```

**步骤详解**：

**步骤 1**: [步骤名称]
- **文件**: [scenario1.ts:10](./src/scenario1.ts#L10)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]

**步骤 2**: [步骤名称]
- **文件**: [scenario1.ts:20](./src/scenario1.ts#L20)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]

### 场景 2: [场景名称]

**场景描述**：[一句话描述场景]

**完整流程**：
```
[用户操作] → [系统响应] → [数据处理] → [结果返回]
```

**步骤详解**：

**步骤 1**: [步骤名称]
- **文件**: [scenario2.ts:10](./src/scenario2.ts#L10)
- **做什么**: [动作描述]
- **输入**: [输入数据]
- **输出**: [输出数据]

---

## 故障排查

### 问题 1: [问题描述]

**症状**：[症状描述]

**可能原因**：
1. [原因1]
2. [原因2]

**排查步骤**：
```bash
# 步骤 1
命令1

# 步骤 2
命令2
```

**解决方案**：
- [解决方案1]
- [解决方案2]

### 问题 2: [问题描述]

**症状**：[症状描述]

**可能原因**：
1. [原因1]
2. [原因2]

**排查步骤**：
```bash
# 步骤 1
命令1

# 步骤 2
命令2
```

**解决方案**：
- [解决方案1]
- [解决方案2]

---

## 附录

### 关键文件路径

| 文件 | 路径 | 说明 |
|------|------|------|
| 主入口 | [main.ts](./src/main.ts) | 程序入口 |
| 配置文件 | [config.yaml](./config.yaml) | 系统配置 |
| 路由定义 | [routes.ts](./src/routes.ts) | API路由 |

### 依赖项

[⚙️ 自动提取] 从 package.json 提取：
- [依赖1]: [版本]
- [依赖2]: [版本]

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| VAR1 | [说明] | [默认值] |
| VAR2 | [说明] | [默认值] |

### 未知项

[🚫 未知] 以下内容无法从现有代码确定：
- [未知项1]
- [未知项2]
```

---

## Template 2: Code Walkthrough (代码导读)

Use for: Deep dive into specific features, user flows, or complex logic.

```markdown
# [项目名] [功能名] 代码导读

> **目标**: 通过 [场景描述]，深入导读整个代码流程
> **创建时间**: YYYY-MM-DD
> **更新时间**: YYYY-MM-DD

## 目录

- [整体流程概览](#整体流程概览)
- [Phase 1: xxx](#phase-1-xxx)
- [Phase 2: xxx](#phase-2-xxx)
- [附录](#附录)

## 整体流程概览

[✅ 已验证] 整体流程如下（见 [main.cr:10](./src/main.cr#L10)）：

```mermaid
flowchart TD
    A[用户操作] --> B[前端处理]
    B --> C[后端API]
    C --> D[数据库]
```

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

[✅ 已验证] 这段代码实现了 [功能描述]（见 [filename.ext:XX](./path#LXX)）。

### 第 2 步：[步骤描述]

[⚙️ 自动提取] 配置项：
- xxx: yyy (从 config.yml 提取)

[❓ 推测] 可能支持 [功能]（见 [file.ext:XX](./path#LXX)），但未找到明确实现。

## Phase 2: [阶段名]

[✅ 已验证] [功能描述]（见 [file.ext:XX](./path#LXX)）。

## 附录

### 关键文件路径

| 文件 | 路径 | 说明 |
|------|------|------|
| 主入口 | [main.cr](./src/main.cr) | 应用启动 |
| 路由 | [routes.cr](./src/routes.cr) | API路由定义 |

### 依赖项

[⚙️ 自动提取] 从 shard.yml 提取：
- kemal: x.x.x
- redis: x.x.x

### 未知项

[🚫 未知] 以下内容无法从现有代码确定：
- 错误处理流程
- 性能瓶颈点
```

---

## Template 3: Component Documentation (组件文档)

Use for: Documenting individual components, modules, or classes.

```markdown
# [组件名] 组件文档

> **模块**: [模块路径]
> **创建时间**: YYYY-MM-DD

## 概述

[✅ 已验证] [组件名] 负责 [功能描述]（见 [component.ts:10](./src/components/component.ts#L10)）。

## 架构

```mermaid
flowchart TB
    subgraph Component["[组件名]"]
        A[输入]
        B[处理逻辑]
        C[输出]
    end
    A --> B --> C
```

## API

### 方法: [方法名]

**签名**: `method(param1: Type1, param2: Type2): ReturnType`

**位置**: [component.ts:XX](./src/components/component.ts#LXX)

**功能**: [功能描述]

**参数**:

| 参数 | 类型 | 说明 |
|------|------|------|
| param1 | Type1 | [说明] |

**返回值**: [返回值说明]

**示例**:

```typescript
const result = component.method(arg1, arg2);
```

[✅ 已验证] 该方法实现了 [功能]（见 [component.ts:XX](./src/components/component.ts#LXX)）。

### 属性: [属性名]

**类型**: Type

**位置**: [component.ts:XX](./src/components/component.ts#LXX)

**说明**: [属性说明]

## 使用场景

[✅ 已验证] 该组件用于 [场景描述]（见 [usage.ts:XX](./src/usage.ts#XX)）。

## 依赖项

[⚙️ 自动提取] 依赖：
- [依赖1]: [版本]
- [依赖2]: [版本]

## 限制

[🚫 未知] 以下限制无法从代码确认：
- 性能限制
- 并发限制
```

---

## Template 4: API Documentation (API文档)

Use for: Documenting API endpoints, request/response formats.

```markdown
# [项目名] API 文档

> **Base URL**: [http://localhost:3000/api](http://localhost:3000/api)
> **创建时间**: YYYY-MM-DD

## 概述

[✅ 已验证] API 提供 [功能描述]（见 [routes.ts:10](./src/routes.ts#L10)）。

## 认证

[✅ 已验证] 使用 [认证方式]（见 [auth.ts:XX](./src/auth.ts#XX)）。

## 端点列表

### POST /api/users

**功能**: 创建用户

**位置**: [routes.ts:XX](./src/routes.ts#LXX)

**请求头**:

| Header | 值 | 说明 |
|--------|-----|------|
| Content-Type | application/json | 请求体格式 |

**请求体**:

```json
{
  "name": "string",
  "email": "string"
}
```

**响应**:

```json
{
  "id": "number",
  "name": "string",
  "email": "string",
  "createdAt": "string"
}
```

**状态码**:

| 状态码 | 说明 |
|--------|------|
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 409 | 用户已存在 |

[✅ 已验证] 该端点实现了 [功能]（见 [routes.ts:XX](./src/routes.ts#LXX)）。

### GET /api/users/:id

**功能**: 获取用户信息

**位置**: [routes.ts:XX](./src/routes.ts#LXX)

**路径参数**:

| 参数 | 类型 | 说明 |
|------|------|------|
| id | number | 用户ID |

**响应**:

```json
{
  "id": "number",
  "name": "string",
  "email": "string"
}
```

**状态码**:

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 404 | 用户不存在 |

[✅ 已验证] 该端点实现了 [功能]（见 [routes.ts:XX](./src/routes.ts#LXX)）。

## 错误处理

[✅ 已验证] 错误响应格式如下（见 [error-handler.ts:XX](./src/error-handler.ts#LXX)）：

```json
{
  "error": {
    "code": "string",
    "message": "string"
  }
}
```

## 速率限制

[🚫 未知] 速率限制策略无法从代码确认。
```

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

[✅ 已验证] 这段代码实现了 [功能描述]（见 [filename.ext:XX](./path#LXX)）。

### 第 2 步：[步骤描述]

[⚙️ 自动提取] 配置项：
- xxx: yyy (从 config.yml 提取)

[❓ 推测] 可能支持 [功能]（见 [file.ext:XX](./path#LXX)），但未找到明确实现。

## Phase 2: [阶段名]

[✅ 已验证] [功能描述]（见 [file.ext:XX](./path#LXX)）。

## 附录

### 关键文件路径

| 文件 | 路径 | 说明 |
|------|------|------|
| 主入口 | [main.cr](./src/main.cr) | 应用启动 |
| 路由 | [routes.cr](./src/routes.cr) | API路由定义 |

### 依赖项

[⚙️ 自动提取] 从 shard.yml 提取：
- kemal: x.x.x
- redis: x.x.x

### 未知项

[🚫 未知] 以下内容无法从现有代码确定：
- 错误处理流程
- 性能瓶颈点
```

---

## Template 2: Component Documentation (组件文档)

Use for: Documenting individual components, modules, or classes.

```markdown
# [组件名] 组件文档

> **模块**: [模块路径]
> **创建时间**: YYYY-MM-DD

## 概述

[✅ 已验证] [组件名] 负责 [功能描述]（见 [component.ts:10](./src/components/component.ts#L10)）。

## 架构

```mermaid
flowchart TB
    subgraph Component["[组件名]"]
        A[输入]
        B[处理逻辑]
        C[输出]
    end
    A --> B --> C
```

## API

### 方法: [方法名]

**签名**: `method(param1: Type1, param2: Type2): ReturnType`

**位置**: [component.ts:XX](./src/components/component.ts#LXX)

**功能**: [功能描述]

**参数**:

| 参数 | 类型 | 说明 |
|------|------|------|
| param1 | Type1 | [说明] |

**返回值**: [返回值说明]

**示例**:

```typescript
const result = component.method(arg1, arg2);
```

[✅ 已验证] 该方法实现了 [功能]（见 [component.ts:XX](./src/components/component.ts#LXX)）。

### 属性: [属性名]

**类型**: Type

**位置**: [component.ts:XX](./src/components/component.ts#LXX)

**说明**: [属性说明]

## 使用场景

[✅ 已验证] 该组件用于 [场景描述]（见 [usage.ts:XX](./src/usage.ts#LXX)）。

## 依赖项

[⚙️ 自动提取] 依赖：
- [依赖1]: [版本]
- [依赖2]: [版本]

## 限制

[🚫 未知] 以下限制无法从代码确认：
- 性能限制
- 并发限制
```

---

## Template 3: Architecture Overview (架构概览)

Use for: High-level system architecture, data flow, or system design.

```markdown
# [项目名] 架构概览

> **创建时间**: YYYY-MM-DD

## 系统架构

[✅ 已验证] 系统采用 [架构模式]（见 [main.ts:10](./src/main.ts#L10)）。

```mermaid
flowchart TB
    subgraph Frontend["前端层"]
        F1[Vue组件]
        F2[API调用]
    end
    subgraph Backend["后端层"]
        B1[Flask路由]
        B2[业务逻辑]
        B3[数据库]
    end
    Frontend --> Backend
```

## 数据流

```mermaid
sequenceDiagram
    participant U as 用户
    participant F as 前端
    participant B as 后端
    participant D as 数据库
    U->>F: 操作
    F->>B: API请求
    B->>D: 查询
    D-->>B: 返回数据
    B-->>F: 响应
    F-->>U: 显示结果
```

## 核心模块

### [模块1]

[✅ 已验证] 负责 [功能]（见 [module1.ts:XX](./src/module1.ts#LXX)）。

### [模块2]

[✅ 已验证] 负责 [功能]（见 [module2.ts:XX](./src/module2.ts#LXX)）。

## 技术栈

[⚙️ 自动提取] 从 package.json 提取：
- 前端: Vue 3.x, TypeScript
- 后端: Flask 2.x, Python 3.9+
- 数据库: PostgreSQL 13.x

## 部署架构

[❓ 推测] 可能使用 [部署方式]（见 [docker-compose.yml:XX](./docker-compose.yml#LXX)），但未完全确认。

## 扩展点

[🚫 未知] 以下扩展点无法从代码确定：
- 插件机制
- 自定义钩子
```

---

## Template 4: API Documentation (API文档)

Use for: Documenting API endpoints, request/response formats.

```markdown
# [项目名] API 文档

> **Base URL**: [http://localhost:3000/api](http://localhost:3000/api)
> **创建时间**: YYYY-MM-DD

## 概述

[✅ 已验证] API 提供 [功能描述]（见 [routes.ts:10](./src/routes.ts#L10)）。

## 认证

[✅ 已验证] 使用 [认证方式]（见 [auth.ts:XX](./src/auth.ts#LXX)）。

## 端点列表

### POST /api/users

**功能**: 创建用户

**位置**: [routes.ts:XX](./src/routes.ts#LXX)

**请求头**:

| Header | 值 | 说明 |
|--------|-----|------|
| Content-Type | application/json | 请求体格式 |

**请求体**:

```json
{
  "name": "string",
  "email": "string"
}
```

**响应**:

```json
{
  "id": "number",
  "name": "string",
  "email": "string",
  "createdAt": "string"
}
```

**状态码**:

| 状态码 | 说明 |
|--------|------|
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 409 | 用户已存在 |

[✅ 已验证] 该端点实现了 [功能]（见 [routes.ts:XX](./src/routes.ts#LXX)）。

### GET /api/users/:id

**功能**: 获取用户信息

**位置**: [routes.ts:XX](./src/routes.ts#LXX)

**路径参数**:

| 参数 | 类型 | 说明 |
|------|------|------|
| id | number | 用户ID |

**响应**:

```json
{
  "id": "number",
  "name": "string",
  "email": "string"
}
```

**状态码**:

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 404 | 用户不存在 |

[✅ 已验证] 该端点实现了 [功能]（见 [routes.ts:XX](./src/routes.ts#LXX)）。

## 错误处理

[✅ 已验证] 错误响应格式如下（见 [error-handler.ts:XX](./src/error-handler.ts#LXX)）：

```json
{
  "error": {
    "code": "string",
    "message": "string"
  }
}
```

## 速率限制

[🚫 未知] 速率限制策略无法从代码确认。
