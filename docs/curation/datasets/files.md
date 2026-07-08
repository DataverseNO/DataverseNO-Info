# Files

Review the uploaded files for completeness, format compliance, and documentation quality.

## Limits

| Limit | Value |
|---|---|
| Files per dataset | 300 (DOI activation constraint) |
| Single file | 100 GB |
| Single upload session | 200 GB |

## Checklist

- [ ] A README file is present
- [ ] README is informative (see below)
- [ ] File names use no spaces, commas, or special characters, and all files have extensions
- [ ] Files are in preferred formats, or open equivalents are provided alongside proprietary ones
- [ ] Tabular data is encoded as tab-separated plain text (UTF-8, no BOM)
- [ ] No personal or sensitive data present
- [ ] Total file count does not exceed 300
- [ ] Files can be opened and are not corrupted

## README quality

The README must enable another researcher to understand and reuse the data without contacting the depositor. It should cover:

- What each file contains
- How the data was collected or generated
- Variable names, units, and value codes for each data file
- Any software required to open the files
- Reuse terms

A README stating only "data from the project" is not sufficient — return the dataset to the author.

## File formats

Preferred formats are open, non-proprietary, and use Unicode UTF-8 encoding. If the depositor has submitted only proprietary formats (e.g. `.xlsx`, `.sav`, `.dta`), request that open equivalents are added (`.csv`, `.tsv`).

See [Prepare your data — Preferred file formats](../../deposit/prepare.md#preferred-file-formats) for the full format table.

## Container files

Container files (`.zip`, `.tar`) must not use compression passwords or encryption. Folder structures inside containers are preserved.

## Missing files

If files referenced in the README or dataset description are absent from the deposit, return the dataset to the author.
