# DataverseNO-Info

Source files for the [DataverseNO information website](https://dataverseno.github.io/DataverseNO-Info/).

This is where the content of the website lives. When you save a change here, the website updates automatically within a few minutes — no technical steps required.

---

## How it works

The website content is written in **Markdown** — a simple text format where you use plain characters for formatting, for example `**bold**` for **bold** and `# Heading` for a heading. You edit files directly in your browser on GitHub, or locally on your computer.

When a change is saved (committed) to the `main` branch, GitHub automatically rebuilds and publishes the website.

---

## Folder structure

```
docs/
  en/              English pages
  nn/              Norwegian Nynorsk pages (mirrors en/ exactly)
  stylesheets/     Visual styling (colours, fonts) — do not edit unless needed
prompts/           AI prompt templates for common tasks
context/           Background documents and design specifications
```

> Each page in `docs/en/` has a matching page in `docs/nn/` at the same path.
> Example: `docs/en/deposit/prepare-your-data.md` ↔ `docs/nn/deposit/prepare-your-data.md`

---

## Common tasks

### Edit an existing page

1. Find the file in `docs/en/` (or `docs/nn/` for the Norwegian version)
2. Click the pencil icon on GitHub to edit it
3. Make your changes
4. Click **Commit changes** — the website will update automatically

### Add a news post

1. Create a new file in `docs/en/news/posts/` named `YYYY-MM-DD-short-title.md`
   — for example: `2026-08-01-new-deposit-guidelines.md`
2. Use this frontmatter at the top of the file:

```yaml
---
date: 2026-08-01
authors:
  - name: DataverseNO
tags:
  - DataverseNO
---

Your post content here.
```

3. Create a matching file in `docs/nn/news/posts/` with the Norwegian translation
4. Use the AI prompt in [`prompts/create-news-post.md`](prompts/create-news-post.md) if you want help writing the post

### Add a new page

1. Create the Markdown file in the right folder under `docs/en/`
2. Create the matching Norwegian file under `docs/nn/`
3. Add the page to the navigation in `mkdocs.yml` under the `nav:` section
4. Ask a technical colleague if you are unsure about step 3

### Translate a page

Use the AI prompt template in [`prompts/translate-page.md`](prompts/translate-page.md):
paste the English page content into an AI assistant with that prompt, then save the result as the Norwegian file.

---

## Checking the live website

The website is published at:
**https://dataverseno.github.io/DataverseNO-Info/**

After committing a change, it usually takes **1–3 minutes** for the website to update.
If it seems unchanged after 5 minutes, check the **Actions** tab at the top of this repository to see if the build has finished or if there was an error.

---

## Markdown quick reference

| What you want | What to write |
|---|---|
| **Bold** | `**bold**` |
| *Italic* | `*italic*` |
| [Link](https://example.com) | `[Link text](https://example.com)` |
| Heading 1 | `# Heading` |
| Heading 2 | `## Heading` |
| Bullet list | `- item` |
| Numbered list | `1. item` |
| Note/admonition | `!!! note` followed by indented text |

Full MkDocs Material documentation: https://squidfunk.github.io/mkdocs-material/

---

## Getting help

For questions about the website or this repository, contact [support@dataverse.no](mailto:support@dataverse.no).
