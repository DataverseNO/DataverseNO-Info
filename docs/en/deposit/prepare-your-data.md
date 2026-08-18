---
title: 'Step 1: Prepare your data'
file_path: docs/en/deposit/prepare-your-data.md
language: en
nav_label: Prepare your data
description: Learn how to organize, format, document, and size-check research data before depositing a dataset in DataverseNO.
seo_title: Prepare research data for DataverseNO | Files, formats, README, and documentation
seo_description: Learn how to prepare research data for DataverseNO by organizing files, choosing suitable file formats, creating a README file, adding documentation, and checking file and dataset size.
tags:
- deposit
- data-management
- documentation
- file-formats
- curation
- research-data
- fair
keywords:
- prepare research data
- DataverseNO README file
- file organization
- preferred file formats
- research data documentation
- dataset documentation
- data files
- file size recommendations
- FAIR data
audience:
- researchers
- data depositors
- research support staff
- data curators
primary_user_intent: User wants to prepare a dataset for deposit in DataverseNO by organizing files, choosing suitable formats, creating documentation, and checking file and dataset size.
parent_page: Deposit Guidelines
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/values.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/en/deposit/prepare-your-data/
social_image: null
---

# Step 1: Prepare your data

Before depositing your data in DataverseNO, spend some time organizing and documenting your dataset. Doing so will make it easier for others to understand, reuse, and cite your data, and will help ensure a smooth publication process.

Most datasets can be prepared by following a few simple steps:

- [SECTION: organize-your-files | Organize your files] so that they are easy to navigate and understand.

- [SECTION: choose-suitable-file-formats | Choose suitable file formats] that support long-term access and reuse.

- [SECTION: describe-your-data | Describe your data] using a ReadMe file and other relevant documentation.

- [SECTION: check-file-and-dataset-size | Check file and dataset size] before uploading your files.

You do not need to get everything perfect. The purpose of these guidelines is to help you prepare data that can be understood and reused by others. If needed, support staff can provide additional guidance during the [REUSE: terms/curation | curation process] before publication.

If you are unsure what applies to your dataset, please contact your [REUSE: links/contact-page | local user support]. We are happy to help.

## Organize your files

Clear file organization makes it easier for collaborators, curators, and future users to navigate your dataset.

### Good practice for file names

- Use descriptive file names.

- Use consistent naming conventions.

- Keep file names reasonably short.

- Use the date format YYYY-MM-DD.

- Avoid spaces and special characters.

[ADMONITION]
Style: secondary
Icon: check-circle-fill
Title: Example: Good file names
Text:
- 00_README.txt
- survey_data_2025-08.csv
- species_observations_2024-06-27.tsv
- interview_metadata.xlsx

[ADMONITION]
Style: tertiary
Icon: x-circle-fill
Title: Example: Bad file names
Text:
- data 1.xlsx
- group Ø-Å final final NEW.xlsx
- test.docx
- untitled.csv

### Spreadsheets and tabular data

For spreadsheets and tabular files, we recommend:

- One table per file.

- One row per observation.

- One column per variable.

- One value per cell.

- Variable names without spaces or special characters.

For more detailed guidance, see chapter [Data Organisation in Spreadsheets](https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-spreadsheets.html) in The Turing Way handbook to reproducible, ethical and collaborative data science.

## Choose suitable file formats

### Why do file formats matter?

Some file formats are easier to preserve and reuse than others. DataverseNO therefore recommends a number of preferred file formats for long-term access and reuse.

However, many datasets can still be published in their original formats. The use of a non-preferred format does not automatically prevent publication.

If your data were originally created in a non-preferred file format, we often recommend uploading both the preferred file format and the original file format. The preferred file format supports long-term preservation and reuse, while the original file format may be easier for some users to inspect or work with in the short term.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Keep in mind
Text: Preferred file formats are recommendations that support long-term preservation. They are not always mandatory requirements for publication.

### Preferred file formats

Examples include:

| Data type | Preferred formats |
| --- | --- |
| Text | TXT, PDF/A |
| Tabular data | TSV, CSV |
| Images | TIFF, PNG, JPEG |
| Audio | WAV, AIFF, FLAC |
| Video | MP4 |
| Markup | XML, HTML |
| Statistical data | R, SPSS syntax, STATA syntax |
| Software code | Python, MATLAB, plain-text source code |

For the complete list including guidance, see the [PAGE: file-formats/index | DataverseNO file formats overview].

### Need help converting files?

Guidance on how to convert documents, spreadsheets, images, audio files, video files, and other data types into preferred file formats is available in the [PAGE: file-formats/index | DataverseNO file formats overview].

### Original and converted file formats

Often, data may be provided both in a preferred file format and in the original file format from which it was derived.

Example:

```text
[text]
experiment_01.csv
experiment_01.xlsx
```

In this example:

- experiment_01.csv is the preferred preservation format.

- experiment_01.xlsx is the original working format.

Providing both versions can help support both long-term preservation and immediate reuse.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Keep in mind
Text: If you upload both a preferred file format and an original file format, the file names should be identical except for the file extension.

## Describe your data

Good documentation makes data easier to find, understand, and reuse.

In DataverseNO, datasets are documented in two complementary ways:

- A ReadMe file that you prepare before depositing your dataset.

- Metadata that you enter when creating the dataset in DataverseNO.

This section focuses on preparing a ReadMe file and other documentation before deposit. Information about metadata is provided in the second step of the deposit workflow: [PAGE: deposit-your-data | Step 2: Deposit your data].

### The most important step: Create a ReadMe file

A ReadMe file is a guide to your dataset. It explains what the data contain, how they were created, how the files are organized, and what someone needs to know to understand and reuse them.

Providing a ReadMe file is required before a dataset can be published in DataverseNO.

The ReadMe file should, at a minimum, contain:

- Dataset title and contact information.

- Description of methods and data collection.

- Overview of files and folders.

- Explanations of variables, abbreviations, codes, or terminology.

- Information about terms of reuse and licensing.

We recommend using one of the DataverseNO templates:

[RESOURCE BOX GRID]
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: DataverseNO README File Template - General
URL: https://doi.org/10.5281/zenodo.7453999
Open: new-tab
[RESOURCE BOX]
Style: primary
Icon: journal-code
Title: DataverseNO README File Template - Software Code
URL: https://doi.org/10.5281/zenodo.7454015
Open: new-tab

Sample ReadMe files:

[RESOURCE BOX GRID]
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: Example 1 (Life Sciences)
URL: https://doi.org/10.18710/S94YFT/J2GAMK
Open: new-tab
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: Example 2 (Social Sciences)
URL: https://doi.org/10.18710/JWTJJB/O77MAT
Open: new-tab

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Keep in mind
Text: A well-written ReadMe file is often the single most important factor enabling others to understand and reuse your data.

### Additional documentation

Depending on the nature of your dataset, it may be helpful to include additional documentation alongside the ReadMe file and refer to it in the ReadMe file where relevant.

Examples include:

- Data collection protocols.

- Analysis scripts.

- Codebooks.

- Survey instruments or interview guides.

- Processing workflows.

- Laboratory procedures.

- Documentation of rights and permissions.

The more specialized your dataset is, the more important such documentation often becomes.

### Why documentation matters

Good documentation increases the likelihood that your data can be:

- Found by other researchers.

- Correctly interpreted and reused.

- Reproduced and validated.

- Preserved and understood in the future.

Documentation therefore benefits not only future users of your data, but also your future self and your collaborators.

## Check file and dataset size

To ensure smooth uploading, curation, and reuse, please note the following recommendations:

- Individual files should preferably not exceed [REUSE: values/file-size-limit].

- A single upload should preferably not exceed [REUSE: values/upload-size-limit].

- A dataset should preferably not exceed [REUSE: values/dataset-size-limit].

- A dataset should preferably not contain more than [REUSE: values/file-number-limit].

### Larger datasets

If your files or dataset exceed these recommendations, contact your [REUSE: links/contact-page | local user support] before depositing your data. Large datasets can often be accommodated.

## Need help?

If you are unsure how to prepare your dataset, contact your [REUSE: links/contact-page | local user support]. We are happy to help.

## Ready to continue?

If your files are organized, documented, and ready to share, you are ready for the next step.

[BUTTON]
Style: primary
Title: Step 2: Deposit your data
Icon: arrow-right-circle-fill
Target: deposit-your-data
