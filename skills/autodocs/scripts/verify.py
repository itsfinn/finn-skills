#!/usr/bin/env python3
"""
Autodocs - 文档质量验证器

QS = 0.20×Structure + 0.30×Honesty + 0.15×Accessibility + 0.20×LinkValidity + 0.15×VisualQuality
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def check_source_markers(content):
    markers = {
        'verified': r'\[✅\s*已验证\]|\[✅\]',
        'extracted': r'\[⚙️\s*自动提取\]|\[⚙️\]',
        'assumed': r'\[❓\s*推测\]|\[❓\]',
        'unknown': r'\[🚫\s*未知\]|\[🚫\]'
    }
    return {k: bool(re.search(pattern, content)) for k, pattern in markers.items()}


def check_honesty(content):
    has_unknown = bool(re.search(r'\[🚫\s*未知\]|\[🚫\]', content))
    has_known = bool(re.search(r'\[✅\s*已验证\]|\[✅\]|\[⚙️\s*自动提取\]|\[⚙️\]', content))

    if has_known and has_unknown:
        return 1.0
    elif has_known:
        return 0.8
    elif has_unknown:
        return 0.4
    return 0.0


def check_structure(content):
    markers = check_source_markers(content)
    count = sum(1 for v in markers.values() if v)
    if count >= 3: return 1.0
    if count >= 2: return 0.7
    if count >= 1: return 0.4
    return 0.0


def check_accessibility(content):
    lines = content.split('\n')
    h1 = sum(1 for l in lines if l.startswith('# ') and not l.startswith('## '))
    h2 = sum(1 for l in lines if l.startswith('## ') and not l.startswith('### '))
    h3 = sum(1 for l in lines if l.startswith('### '))
    has_toc = bool(re.search(r'##?\s*目录|##?\s*Table of Contents|##?\s*TOC', content, re.IGNORECASE))

    score = 0.0
    if h1 >= 1: score += 0.3
    if h2 >= 3: score += 0.4
    elif h2 >= 1: score += 0.2
    if h3 >= 2: score += 0.2
    if has_toc: score += 0.1
    return min(score, 1.0)


def find_project_root(start_path):
    current = Path(start_path).resolve()
    while current != current.parent:
        if any((current / marker).exists() for marker in ['.git', 'package.json', 'Cargo.toml', 'go.mod', 'pyproject.toml', 'Makefile']):
            return current
        current = current.parent
    return Path(start_path).resolve()


def check_link_validity(content, docs_dir):
    link_pattern = r'\[([^\]]+)\]\(((?:\.\./|\./)[^)]+(?:#L\d+(?:-\d+)?)?)\)'
    matches = re.findall(link_pattern, content)

    if not matches:
        return 0.0

    valid = 0
    total = len(matches)
    project_root = find_project_root(Path(docs_dir).resolve())

    for link_text, link_path in matches:
        file_match = re.match(r'((?:\.\./|\./)[^#]+)', link_path)
        if not file_match:
            continue

        relative_path = re.sub(r'^(\.\.\/|\.\/)+', '', file_match.group(1))
        full_path = project_root / relative_path
        if not full_path.exists():
            continue

        line_match = re.search(r'#L(\d+)', link_path)
        if line_match:
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    if int(line_match.group(1)) <= len(f.readlines()):
                        valid += 1
            except (IOError, UnicodeDecodeError):
                pass
        else:
            valid += 1

    return valid / total if total > 0 else 0.0


def check_visual_quality(content):
    patterns = [
        r'```mermaid',
        r'flowchart\s+(?:TD|TB|LR|RL)',
        r'sequenceDiagram',
        r'graph\s+(?:TD|TB|LR|RL)',
        r'pie\s+',
        r'gantt',
    ]
    count = sum(1 for p in patterns if re.search(p, content))
    if count >= 2: return 1.0
    if count >= 1: return 0.7
    return 0.0


def calculate_file_score(content, docs_dir):
    structure = check_structure(content)
    honesty = check_honesty(content)
    accessibility = check_accessibility(content)
    link_validity = check_link_validity(content, docs_dir)
    visual_quality = check_visual_quality(content)

    score = (
        structure * 0.20 +
        honesty * 0.30 +
        accessibility * 0.15 +
        link_validity * 0.20 +
        visual_quality * 0.15
    )

    return score, {
        'structure': structure,
        'honesty': honesty,
        'accessibility': accessibility,
        'link_validity': link_validity,
        'visual_quality': visual_quality
    }


def calculate_qs(docs_dir="docs"):
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        return 0.0, {}

    scores, details = [], {}
    for md_file in sorted(docs_path.rglob("*.md")):
        if md_file.name.startswith('.') or len(md_file.read_text()) < 50:
            continue

        content = md_file.read_text(encoding='utf-8')
        file_score, file_details = calculate_file_score(content, docs_dir)
        scores.append(file_score)
        details[str(md_file.relative_to(docs_path))] = {
            'score': file_score,
            **file_details
        }

    return (sum(scores) / len(scores) if scores else 0.0), details


def get_unknown_items(content):
    pattern = r'\[🚫\s*未知\]\s*(.*?)(?=\n\n|\n\[|$)'
    return [m.strip() for m in re.findall(pattern, content, re.DOTALL) if m.strip()]


def get_assumed_items(content):
    pattern = r'\[❓\s*推测\]\s*(.*?)(?=\n\n|\n\[|$)'
    return [m.strip() for m in re.findall(pattern, content, re.DOTALL) if m.strip()]


def create_pending_confirmation(docs_dir, qs, details):
    docs_path = Path(docs_dir)
    confirm_path = docs_path.parent / ".autodocs" / "PENDING_CONFIRMATION.md"

    high_priority = []
    medium_priority = []

    for md_file in sorted(docs_path.rglob("*.md")):
        if md_file.name.startswith('.'):
            continue
        content = md_file.read_text(encoding='utf-8')
        rel_path = str(md_file.relative_to(docs_path))

        for item in get_unknown_items(content):
            high_priority.append(f"- [ ] **{rel_path}**: {item[:100]}")
        for item in get_assumed_items(content):
            medium_priority.append(f"- [ ] **{rel_path}**: {item[:100]}")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    doc = f"""# 📋 人工确认文档

**状态**: 🔴 待确认
**创建时间**: {now}
**当前 QS**: {qs:.2f}

---

## 需确认项

### 🔴 高优先级（影响文档核心准确性）

{chr(10).join(high_priority[:10]) if high_priority else '- 无 `[🚫 未知]` 标记项'}

### 🟡 中优先级（影响文档完整性）

{chr(10).join(medium_priority[:10]) if medium_priority else '- 无 `[❓ 推测]` 标记项'}

---

## 确认后操作

1. 填写上述确认项
2. 重新运行 autodocs skill
3. 系统将读取本文件并更新文档

---

**说明**: 自动化文档生成时无法确定以上内容，请人工确认后重新运行 skill。
"""

    confirm_path.parent.mkdir(parents=True, exist_ok=True)
    with open(confirm_path, 'w', encoding='utf-8') as f:
        f.write(doc)

    return str(confirm_path)


def log_result(qs, change_summary, results_file="results.tsv"):
    results_path = Path(results_file)
    if not results_path.exists():
        with open(results_file, 'w', encoding='utf-8') as f:
            f.write("timestamp\tqs\tchange_summary\n")
    with open(results_file, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat()}\t{qs:.4f}\t{change_summary}\n")


def print_detailed_report(details):
    print("\n详细分数:")
    print("-" * 70)
    print(f"{'文件':<30} {'QS':>5} {'结构':>5} {'诚实':>5} {'链接':>5} {'图表':>5}")
    print("-" * 70)
    for path, info in sorted(details.items()):
        print(f"{path[:28]:<30} {info['score']:>5.2f} {info['structure']:>5.2f} {info['honesty']:>5.2f} {info['link_validity']:>5.2f} {info['visual_quality']:>5.2f}")
    print("-" * 70)


if __name__ == "__main__":
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else "docs"

    print(f"正在验证文档目录: {docs_dir}")
    qs, details = calculate_qs(docs_dir)

    print(f"\n总体 QS: {qs:.4f}")

    if details:
        print_detailed_report(details)

    print("\n改进建议:")
    if qs < 0.7:
        print("❌ 文档质量不足")
        confirm_path = create_pending_confirmation(docs_dir, qs, details)
        print(f"   已创建: {confirm_path}")
        print("\n   请检查：")
        print("   - 是否添加了段落级可信度标记 [✅ 已验证][⚙️ 自动提取][❓ 推测][🚫 未知]")
        print("   - 是否添加了精确的代码链接")
        print("   - 是否添加了 Mermaid 可视化图表")
        print("\n   下一步：")
        print("   1. 查看 PENDING_CONFIRMATION.md")
        print("   2. 填写确认信息")
        print("   3. 重新运行 autodocs skill")
    elif qs < 0.8:
        print("⚠️  文档质量一般，建议：")
        print("   - 增加更多 [✅ 已验证] 段落")
        print("   - 减少 [🚫 未知] 标记")
        print("   - 添加流程图或时序图")
    else:
        print("✅ 文档质量良好！")

    sys.exit(0 if qs >= 0.7 else 1)
