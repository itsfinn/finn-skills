---
name: conventional-commit
description: "按照约定式提交规范生成提交消息并提交到当前分支。Use when user wants to create a git commit following conventional commit standards. Triggers: commit, git commit, conventional commit, generate commit message, create commit."
---

# 约定式提交 (Conventional Commits)

## 概述

约定式提交规范是一种基于提交信息的轻量级约定，提供一组简单规则来创建清晰的提交历史。它使提交信息与 SemVer 相互对应，便于自动化生成 CHANGELOG 和版本管理。

提交说明的结构：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## 工作流程

### 步骤 1: 分析变更文件

1. 运行 `git status` 查看当前变更状态
2. 运行 `git diff --staged` 或 `git diff` 查看具体的代码变更
3. 根据变更内容判断最合适的 type

### 步骤 2: 选择提交类型

| 类型 | 用途 | SemVer |
|------|------|--------|
| **feat** | 新增功能 | MINOR |
| **fix** | 修复 bug | PATCH |
| **docs** | 仅文档变更 | - |
| **style** | 代码格式调整（不影响功能） | - |
| **refactor** | 重构代码（不新增功能或修复bug） | - |
| **perf** | 性能优化 | - |
| **test** | 测试相关 | - |
| **build** | 构建系统或依赖变更 | - |
| **ci** | CI/CD 配置变更 | - |
| **chore** | 其他杂项（如工具配置） | - |
| **revert** | 撤销之前的提交 | - |

### 步骤 3: 确定 Scope（可选）

Scope 用于指定变更影响的代码范围，例如：
- `feat(auth):` - 认证模块
- `fix(api):` - API 接口
- `docs(readme):` - README 文档
- `refactor(utils):` - 工具函数

### 步骤 4: 编写描述

- 使用祈使句，现在时态（如 "add" 而非 "added"）
- 首字母小写
- 末尾不加句号
- 简洁明了（50字符以内）

### 步骤 5: 编写正文（可选）

当变更需要更多上下文时使用：
- 解释 "为什么" 而不是 "做了什么"
- 与之前行为的对比
- 使用空行分隔段落

### 步骤 6: 编写脚注（可选）

常用格式：
- `BREAKING CHANGE:` - 破坏性变更说明
- `Refs: #123` - 关联的 Issue/PR
- `Closes: #456` - 关闭的 Issue
- `Reviewed-by:` - 审核人

### 步骤 7: 破坏性变更标记

如果包含破坏性变更，使用以下方式之一标记：

**方式 1**: 在 type/scope 后加 `!`
```
feat(api)!: remove deprecated endpoints
```

**方式 2**: 在脚注中添加 BREAKING CHANGE
```
feat: remove legacy authentication

BREAKING CHANGE: The old auth token format is no longer supported.
```

## 完整示例

### 简单提交
```
fix: correct typo in README
```

### 带 scope 的提交
```
feat(auth): add OAuth2 login support
```

### 带正文的提交
```
feat: implement user authentication

Add JWT-based authentication for API endpoints.
Users can now login with email/password and receive
tokens for subsequent requests.
```

### 带脚注的提交
```
refactor: simplify error handling

Refs: #234
Reviewed-by: Alice
```

### 破坏性变更
```
feat(api)!: change response format for user endpoints

BREAKING CHANGE: User object now returns `userId` instead of `id`.
Migration guide: update all references from `.id` to `.userId`.
```

## 执行流程

1. **检查变更**: 分析 git 状态，理解变更内容
2. **生成交互式问题**: 询问用户相关信息
   - 变更类型是什么？
   - 影响范围是？
   - 简短描述是什么？
   - 是否需要详细正文？
   - 是否包含破坏性变更？
   - 是否需要关联 Issue/PR？
3. **生成提交消息**: 根据用户输入组合成规范格式
4. **展示并确认**: 显示完整的提交消息，询问用户是否需要修改
5. **执行提交**: 用户确认后执行 `git commit -m "消息"`

## 注意事项

- **原子提交**: 每个提交只做一件事
- **清晰描述**: 让其他开发者理解变更意图
- **BREAKING CHANGE**: 破坏性变更必须明确标记
- **关联 Issues**: 使用 `Closes: #123` 或 `Refs: #456` 关联相关 Issue

## Resources

- `references/conventional-commits-spec.md` - 完整规范文档
