# Contributing to DataverseNO-Info

This repository contains the source for the [DataverseNO information website](https://DataverseNO.github.io/DataverseNO-Info/).

## Structure

```
docs/
  en/          English content (primary)
  nn/          Norwegian Nynorsk content
assets/        Shared images, icons, logos
stylesheets/   CSS customisation
prompts/       AI prompt templates for content workflows
```

## Adding or editing content

1. Edit the relevant Markdown file in `docs/en/` (English) or `docs/nn/` (Norwegian Nynorsk)
2. For new pages, add the file and update `nav:` in `mkdocs.yml`
3. Create a pull request — CI will build and validate the site

## Translating content

Use the prompt template in [`prompts/translate-page.md`](prompts/translate-page.md) to translate a page from English to Norwegian Nynorsk.

## Adding news posts

Create a new file in `docs/en/news/posts/` with the naming convention `YYYY-MM-DD-short-title.md`.

Use the prompt template in [`prompts/create-news-post.md`](prompts/create-news-post.md).

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

The site will be available at `http://localhost:8000`.

## Contact

For questions about this repository, contact [support@dataverse.no](mailto:support@dataverse.no).
