---
name: doc-to-blog-post
description: Convert provided documents into Hugo blog posts in the content/post directory, then commit and push changes to the remote repository. Use when you need to automatically publish documents as blog posts with git integration, such as converting notes, articles, or reports into published content.
---

# Doc To Blog Post

## Overview

This skill automates the process of converting documents into Hugo-compatible blog posts and publishing them. It handles document parsing, Hugo frontmatter generation, file placement, and git operations for seamless publishing.

## Workflow

1. **Document Processing**: Parse the provided document content
2. **Hugo Post Creation**: Generate Hugo frontmatter and format content as Markdown
3. **File Placement**: Save the post to `content/post/` directory with appropriate filename
4. **Git Operations**: Add, commit, and push changes to remote repository

## Usage

When this skill is triggered, provide:
- Document content (as text/Markdown)
- Optional: Custom title, date, or other frontmatter fields

The script will automatically:
- Extract or generate a title from the document
- Add current timestamp as date
- Format content for Hugo
- Generate a URL-safe filename
- Commit with message "Add new post: [title]"

## Resources

### scripts/
- `convert_doc_to_post.py`: Main script for document conversion and publishing

### assets/
- `post_template.md`: Hugo post template with frontmatter
