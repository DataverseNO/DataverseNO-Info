---
title: Prepare Your Data
description: How to prepare your dataset for deposit in DataverseNO — file formats, naming, documentation, and metadata.
tags:
  - deposit
  - file formats
  - metadata
  - README
---

# Prepare Your Data

DataverseNO only accepts data that can be openly shared. If your data is personal, health-related, Indigenous, copyrighted, commercially sensitive, or raises security concerns, contact your local support before preparing your dataset.

## File naming and organisation

- Use consistent, descriptive file names — keep them under 25 characters
- No spaces; use underscores, hyphens, or camelCase
- Avoid special characters including `æ Æ ø Ø å Å ä Ä ö Ö`
- Use `YYYY-MM-DD` date format
- If you save a file in both its original and a preferred format, use identical names with different extensions

**For tabular data (spreadsheets):**

- One table per file
- One column per variable, one row per observation
- Column headers in the first row
- Consistent date formatting throughout

## Preferred file formats

Use open, non-proprietary formats encoded in Unicode UTF-8. Proprietary formats are accepted alongside open equivalents, not instead of them.

| Data type | Preferred formats | Avoid |
|---|---|---|
| Tabular | CSV, TSV (tab-separated plain text) | XLSX, ODS |
| Text | TXT, PDF/A | DOC, DOCX |
| Images | TIFF, PNG | PSD, AI |
| Audio | WAV, FLAC | MP3, AAC |
| Video | MP4 (H.264) | MOV, AVI |
| Geospatial | GeoTIFF, Shapefile, GeoJSON | MXD |
| Statistical | CSV + syntax file | SAV, DTA, SAS7BDAT alone |

!!! tip "Converting files"
    Most statistical software (SPSS, Stata, R, SAS) can export to CSV. Keep the original file too and include both in your deposit.

## Documentation

Every dataset must include two forms of documentation:

### Metadata

Fill in the metadata fields in DataverseNO accurately and in English (or standard scientific language). Good metadata makes your dataset discoverable.

### README file

Include a README file (plain text or PDF) that acts as a user guide to your dataset. It should cover:

- Title and DOI
- Contact information
- How and where the data was collected (methods)
- Overview of files and folder structure
- Description of variables, units, and codes for each file
- Software required to open the files
- Reuse terms and licensing

A [README template](https://doi.org/10.5281/zenodo.7962353) is available as a checklist.

## File size limits

| Limit | Value |
|---|---|
| Files per dataset | 300 |
| Single file | 100 GB |
| Single upload session | 200 GB |

Deposits exceeding 200 GB total require prior coordination — contact your institution's DataverseNO support.

!!! warning "Sensitive data"
    Remove all personal, sensitive, or confidential information before depositing. DataverseNO does not accept data that cannot be openly shared. If unsure, contact your institution's data protection officer first.
