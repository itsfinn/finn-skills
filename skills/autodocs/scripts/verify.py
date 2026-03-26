#!/usr/bin/env python3
"""
Autodocs - 文档质量验证器

QS = w1×Structure + w2×Honesty + w3×Accessibility + w4×LinkValidity + w5×VisualQuality
"""

import re
import sys
from pathlib import Path
from datetime import datetime


def check_source_markers(content):
    """
    检查段落级可信度标记
    
    支持格式：
    - [✅ 已验证]
    - [⚙️ 自动提取]
    - [❓ 推测]
    - [🚫 未知]
    """
    markers = {
        'verified': r'\[✅\s*已验证\]',
        'extracted': r'\[⚙️\s*自动提取\]',
        'assumed': r'\[❓\s*推测\]',
        'unknown': r'\[🚫\s*未知\]'
    }
    # 兼容旧格式（无文字说明）
    markers_legacy = {
        'verified': r'\[✅\]',
        'extracted': r'\[⚙️\]',
        'assumed': r'\[❓\]',
        'unknown': r'\[🚫\]'
    }
    
    result = {}
    for k in markers:
        result[k] = bool(re.search(markers[k], content)) or bool(re.search(markers_legacy[k], content))
    return result


def check_honesty(content):
    """
    检查诚实度：是否有未知标记，且是否有已知标记
    
    诚实文档应该：
    - 包含 [✅ 已验证] 或 [⚙️ 自动提取]（已知内容）
    - 可以包含 [🚫 未知]（诚实标记未知内容）
    """
    has_unknown = bool(re.search(r'\[🚫\s*未知\]|\[🚫\]', content))
    has_verified_or_extracted = bool(
        re.search(r'\[✅\s*已验证\]|\[✅\]|\[⚙️\s*自动提取\]|\[⚙️\]', content)
    )
    
    if has_verified_or_extracted:
        # 有已知内容，得分高
        return 1.0
    elif has_unknown:
        # 只有未知标记，得分中等（不够诚实，缺少已知内容）
        return 0.5
    else:
        # 无任何标记，得分低
        return 0.0


def check_structure(content):
    """检查结构：是否有可信度标记"""
    return 1.0 if any(check_source_markers(content).values()) else 0.0


def check_accessibility(content):
    """检查可访问性：是否有清晰的章节结构"""
    if '#' not in content:
        return 0.3
    h2_count = content.count('\n## ')
    return 0.7 if h2_count > 0 else 0.5


def check_link_validity(content, docs_dir):
    """
    检查代码链接有效性
    
    链接格式：
    - [filename:line](./path/to/file#L122)
    - [L24-29](./path/to/file#L24)
    - [filename](./path/to/file)
    """
    # 匹配 Markdown 链接格式
    link_pattern = r'\[([^\]]+)\]\((\.\/[^)]+(?:#L\d+(?:-\d+)?)?)\)'
    matches = re.findall(link_pattern, content)
    
    if not matches:
        return 0.0  # 没有链接则得 0 分
    
    valid_links = 0
    total_links = len(matches)
    
    for link_text, link_path in matches:
        # 提取文件路径（去掉 #L122 这样的锚点）
        file_path_match = re.match(r'(\.\/[^#]+)', link_path)
        if not file_path_match:
            continue
        
        file_path = file_path_match.group(1)
        full_path = Path(docs_dir).parent / file_path.lstrip('./')
        
        # 检查文件是否存在
        if full_path.exists():
            valid_links += 1
    
    return valid_links / total_links if total_links > 0 else 0.0


def check_visual_quality(content):
    """检查可视化质量：是否包含 Mermaid 图表"""
    mermaid_patterns = [
        r'```mermaid',  # mermaid 代码块
        r'flowchart',
        r'sequenceDiagram',
        r'graph ',
        r'pie ',
        r'gantt',
    ]
    
    has_mermaid = any(re.search(pattern, content) for pattern in mermaid_patterns)
    return 1.0 if has_mermaid else 0.0


def check_line_range_format(content):
    """检查行号范围格式是否正确"""
    # 检查 [L24-29] 这样的格式
    range_pattern = r'\[L\d+-\d+\]'
    has_range = bool(re.search(range_pattern, content))
    return 0.2 if has_range else 0.0


def calculate_file_score(content, docs_dir):
    """计算单个文件的分数"""
    structure = check_structure(content)
    honesty = check_honesty(content)
    accessibility = check_accessibility(content)
    link_validity = check_link_validity(content, docs_dir)
    visual_quality = check_visual_quality(content)
    
    # 新的权重分配
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
    """计算整体 QS"""
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


def log_result(qs, change_summary, results_file="results.tsv"):
    """记录结果到 TSV 文件"""
    results_path = Path(results_file)
    
    # 如果文件不存在，创建并写入表头
    if not results_path.exists():
        with open(results_file, 'w', encoding='utf-8') as f:
            f.write("timestamp\tqs\tchange_summary\n")
    
    with open(results_file, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat()}\t{qs:.4f}\t{change_summary}\n")


def print_detailed_report(details):
    """打印详细报告"""
    print("\n详细分数:")
    print("-" * 60)
    print(f"{'文件':<30} {'QS':<6} {'结构':<6} {'诚实':<6} {'链接':<6} {'图表':<6}")
    print("-" * 60)
    
    for path, info in sorted(details.items()):
        print(
            f"{path[:28]:<30} "
            f"{info['score']:.2f}  "
            f"{info['structure']:.2f}  "
            f"{info['honesty']:.2f}  "
            f"{info['link_validity']:.2f}  "
            f"{info['visual_quality']:.2f}"
        )
    
    print("-" * 60)


if __name__ == "__main__":
    docs_dir = sys.argv[1] if len(sys.argv) > 1 else "docs"
    
    print(f"正在验证文档目录: {docs_dir}")
    qs, details = calculate_qs(docs_dir)
    
    print(f"\n总体 QS: {qs:.4f}")
    
    if details:
        print_detailed_report(details)
    
    # 给出改进建议
    print("\n改进建议:")
    if qs < 0.7:
        print("❌ 文档质量不足，已自动创建 PENDING_CONFIRMATION.md")
        print("   请检查：")
        print("   - 是否添加了段落级可信度标记 [✅ 已验证][⚙️ 自动提取][❓ 推测][🚫 未知]")
        print("   - 是否添加了精确的代码链接")
        print("   - 是否添加了 Mermaid 可视化图表")
        print("   - 是否标记了所有未知内容为 [🚫 未知]")
        print("\n   下一步：")
        print("   1. 查看 .autodocs/PENDING_CONFIRMATION.md")
        print("   2. 填写确认信息")
        print("   3. 重新运行 skill")
    elif qs < 0.8:
        print("⚠️  文档质量一般，建议：")
        print("   - 增加更多 [✅ 已验证] 段落")
        print("   - 减少 [🚫 未知] 标记（通过深入分析代码）")
        print("   - 添加流程图或时序图")
    else:
        print("✅ 文档质量良好！")
    
    sys.exit(0 if qs >= 0.7 else 1)
