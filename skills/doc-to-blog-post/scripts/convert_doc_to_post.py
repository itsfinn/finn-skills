#!/usr/bin/env python3
"""
Convert document to Hugo blog post and publish via git
"""

import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(text):
    """Convert text to URL-safe slug"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def extract_title(content):
    """Extract title from content (first line or first heading)"""
    lines = content.strip().split("\n")
    for line in lines[:5]:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        elif line and not line.startswith("---"):
            return line
    return "Untitled Post"


def extract_description(content, max_length=150):
    """Extract description from content"""
    content = re.sub(r"^---.*?---\n", "", content, flags=re.DOTALL)
    paragraphs = content.split("\n\n")
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith("#"):
            return para[:max_length] + ("..." if len(para) > max_length else "")
    return ""


def create_post_file(content, title=None, date=None, output_dir="content/post"):
    """Create Hugo post file"""
    if title is None:
        title = extract_title(content)

    if date is None:
        date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")

    description = extract_description(content)

    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"

    template_path = Path(__file__).parent.parent / "assets" / "post_template.md"
    with open(template_path, "r") as f:
        template = f.read()

    post_content = template.replace("{{TITLE}}", title)
    post_content = post_content.replace("{{DATE}}", date)
    post_content = post_content.replace("{{DESCRIPTION}}", description)
    post_content = post_content.replace("{{CONTENT}}", content)
    output_path = Path(output_dir) / filename
    with open(output_path, "w") as f:
        f.write(post_content)

    return output_path, title


def git_operations(file_path, title):
    """Perform git add, commit, push"""
    os.system(f'git add "{file_path}"')
    commit_msg = f"Add new post: {title}"
    os.system(f'git commit -m "{commit_msg}"')
    os.system("git push")


def main():
    parser = argparse.ArgumentParser(description="Convert document to Hugo blog post")
    parser.add_argument("content", help="Document content (can be file path or text)")
    parser.add_argument("--title", help="Custom title (optional)")
    parser.add_argument("--output-dir", default="content/post", help="Output directory")

    args = parser.parse_args()

    content = args.content
    if os.path.isfile(content):
        with open(content, "r") as f:
            content = f.read()

    file_path, title = create_post_file(content, args.title, output_dir=args.output_dir)

    print(f"Created post: {file_path}")
    git_operations(file_path, title)

    print("Post published successfully!")


if __name__ == "__main__":
    main()
