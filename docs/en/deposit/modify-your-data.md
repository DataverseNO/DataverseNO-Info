---
title: 'Step 5: Modify your data'
file_path: docs/en/deposit/modify-your-data.md
language: en
nav_label: Modify your data
description: Learn how to update published datasets in DataverseNO, how versioning affects citations, and when deaccessioning may be relevant.
seo_title: Modify published datasets in DataverseNO | Versioning, DOI, citation, and deaccessioning
seo_description: Learn how to update a published dataset in DataverseNO, how new versions are reviewed, how versioning affects DOI and citation, and when deaccessioning may be considered.
tags:
- deposit
- dataverseno
- versioning
- doi
- deaccessioning
- research-data
- curation
keywords:
- modify dataset DataverseNO
- update published dataset
- dataset versioning
- dataset DOI
- dataset citation version
- deaccessioning
- published research data
- DataverseNO dataset update
audience:
- researchers
- data depositors
- research support staff
- data curators
primary_user_intent: User wants to understand how to update a published dataset in DataverseNO, how versioning affects citation and DOI, and what happens if access to a published dataset must be removed.
parent_page: Deposit Guidelines
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/en/deposit/modify-your-data/
social_image: null
---

# Step 5: Modify your data

Publishing a dataset is not necessarily the final step in its lifecycle. If necessary, you can update a dataset after publication to correct errors, improve documentation, add files, or incorporate additional information.

DataverseNO uses versioning to ensure that changes can be tracked while preserving access to earlier versions of the dataset.

This step explains:

- [SECTION: why-modify-a-dataset | Reasons to modify a dataset].

- [SECTION: how-versioning-works | How versioning works].

- [SECTION: can-a-published-dataset-be-deleted | How deaccessioning works].

## Why modify a dataset?

You may wish to create a new version of a dataset in order to:

- Correct metadata.

- Improve documentation.

- Update the ReadMe file.

- Add new data files.

- Replace files with improved versions.

- Add information about related publications.

- Address recommendations from users or collaborators.

Updating a dataset allows you to improve its quality and usefulness while preserving the scholarly record.

## How versioning works

To make changes to a published dataset, log in to DataverseNO, navigate to the dataset you want to update, and click Edit Dataset on the dataset landing page. To upload a new version of a file, you should first delete the old one.

When changes are made:

- A new draft version of the dataset is created.

- The draft must be submitted for review.

- A curator reviews the changes.

- The new version is published.

To support transparency, reproducibility, and an efficient review process, we recommend clearly documenting all changes from the previous version in the ReadMe file. This information should preferably be recorded in the dedicated Version history section of the ReadMe file template, under the question “Is this an updated version of a dataset published on DataverseNO?”.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Keep in mind
Text: Document the changes from the previous version clearly in the ReadMe file before submitting the updated dataset for review.

### What happens after you submit a new version?

New versions follow the same review process as new datasets.

As explained in [PAGE: publish-your-data | Step 3: Curation and publishing], curators review submitted datasets to help ensure that they remain well documented, understandable, and reusable. When reviewing a new version of a dataset, particular attention is paid to the changes introduced since the previous version.

Earlier versions remain available after publication of the new version. This ensures that users can always access the exact version of the data that was used in earlier research.

### What happens to the DOI and citation?

DataverseNO uses [REUSE: terms/version-control] to track all changes made to a published dataset. This ensures transparency and allows users to identify exactly which version of the dataset was used in a particular study.

The dataset [REUSE: terms/digital-object-identifier | DOI] remains the same when a new version is published. This provides a stable identifier for the dataset throughout its lifecycle.

Changes are assigned version numbers. Depending on the nature of the changes, a version may be released as either a major version or a minor version.

#### Major versions

Major versions are typically used when data files are added, removed, replaced, or otherwise modified.

Examples:

```text
[text]
V1 -> V2
V2 -> V3
```

Major version changes are reflected in the dataset citation.

Example:

```text
[text]
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

becomes:

Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2027). Bird observations from Northern Norway, 2018-2024 (Version 2) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

#### Minor versions

Minor versions are typically used for smaller updates that do not affect the underlying data files.

Examples include correcting or expanding metadata, for example adding information to the Related Publication field.

Examples:

```text
[text]
V1 -> V1.1
V1.1 -> V1.2
```

Minor version changes are tracked by the repository but are normally not reflected in the dataset citation. In these cases, the citation remains at the major version level.

For example, even if the internal repository version changes from V1 to V1.1, the recommended dataset citation will continue to refer to V1.

## Can a published dataset be deleted?

Published datasets cannot normally be deleted.

This is because published datasets have [REUSE: terms/persistent-identifier | persistent identifiers], such as [REUSE: terms/digital-object-identifier | DOIs], and form part of the scholarly record.

### Deaccessioning

In exceptional cases, access to files in a published dataset may be removed. This process is called deaccessioning. Deaccessioning may be considered only when there is a compelling reason, for example if the dataset does not meet DataverseNO deposit criteria, contains malware, violates copyright, contractual obligations, legal requirements, research ethics, or involves research misconduct.

When a dataset is deaccessioned:

- The data files are no longer publicly accessible.

- The dataset metadata remains visible.

- The ReadMe file remains accessible.

- The dataset DOI remains part of the scholarly record.

If you believe that a published dataset should be deaccessioned, please contact your [REUSE: links/contact-page | local user support].

[ADMONITION]
Style: primary
Icon: exclamation-circle-fill
Title: Published datasets are part of the scholarly record
Text: Deaccessioning is exceptional and should only be considered when there is a strong reason to remove public access to files in a published dataset.

## Need help?

If you are unsure whether a dataset should be updated, how versioning will affect citation, or whether deaccessioning may be appropriate, please contact your [REUSE: links/contact-page | local user support].

## You've reached the end of the deposit workflow

Congratulations! You now know how to:

- Prepare your data.

- Deposit your data.

- Get your data published.

- Refer to your data.

- Update your dataset when needed.

For additional guidance, see:

- [PAGE: deposit-quick-guide | Quick guide and checklist].

- [PAGE: about/index | About DataverseNO].

- [PAGE: contact/index | Contact information].
