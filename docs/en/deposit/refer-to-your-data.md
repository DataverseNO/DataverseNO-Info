---
title: 'Step 4: Refer to your data'
file_path: docs/en/deposit/refer-to-your-data.md
language: en
nav_label: Refer to your data
description: Learn how to cite published datasets, refer to datasets before publication, use data availability statements, and handle dataset versions in DataverseNO.
seo_title: Cite and refer to DataverseNO datasets | DOI, data availability, drafts, and versioning
seo_description: Learn how to cite published datasets in DataverseNO, refer to draft datasets during review, write data availability statements, and handle dataset citation and versioning.
tags:
- deposit
- dataverseno
- citation
- doi
- versioning
- research-data
- publishing
keywords:
- cite dataset
- DataverseNO citation
- dataset DOI
- data availability statement
- cite research data
- draft dataset citation
- double-blind peer review data
- dataset versioning
- research data citation
audience:
- researchers
- data depositors
- authors
- journal editors
- peer reviewers
- research support staff
- data curators
primary_user_intent: User wants to know how to cite or refer to a DataverseNO dataset in publications, during peer review, or after dataset version updates.
parent_page: Deposit Guidelines
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/en/deposit/refer-to-your-data/
social_image: null
---

# Step 4: Refer to your data

Once published, your dataset becomes a citable research output that can be referred to in articles, books, dissertations, reports, and other scholarly publications.

This step explains:

- [SECTION: after-publication | What happens after publication].

- [SECTION: why-cite-datasets | Why datasets should be cited].

- [SECTION: how-to-cite-a-published-dataset | How to cite a published dataset].

- [SECTION: how-to-refer-to-datasets-in-a-publication | How to refer to datasets in a publication].

- [SECTION: referring-to-a-dataset-before-publication | How to refer to a dataset before publication].

- [SECTION: dataset-citation-and-versioning | How versioning affects dataset citation].

## After publication

When the dataset is published:

- The [REUSE: terms/digital-object-identifier | DOI] becomes active.

- The dataset becomes publicly accessible.

- The dataset becomes searchable in DataverseNO and external discovery services.

- The dataset can be cited and shared as research output.

[ADMONITION]
Style: primary
Icon: exclamation-circle-fill
Title: Keep in mind
Text: Do not publicly distribute or cite the dataset DOI until the dataset has been published and the DOI has been activated.

## Why cite datasets

Research data should be cited in the same way as other scholarly outputs such as journal articles, books, software, or reports.

Data citation serves several purposes:

- It gives credit to dataset creators.

- It enables others to locate the exact data used.

- It supports transparency and reproducibility.

- It helps establish links between publications and underlying research data.

As a general rule, if a publication relies on a dataset, the dataset should be cited.

## How to cite a published dataset

Once a dataset has been published, a recommended citation is displayed in the citation box on the dataset landing page. To find it:

- Open the dataset landing page.

- Locate the citation box near the top of the page.

- Copy the citation and adapt it if required by the citation style used by the publication venue.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Example: Citing a published dataset in APA Style, 7th edition
Text: Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

## How to refer to datasets in a publication

Datasets should normally be referred to in two ways:

### In the reference list

Include a full dataset citation in the reference list, just as you would for an article, book, or other cited work.

Example, APA Style, 7th edition:

```text
[text]
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

### In the text

Refer to the dataset in the text using the citation style required by the publication venue.

Example, APA Style, 7th edition:

```text
[text]
The underlying data are available in Hansen et al. (2026).
```

Example, parenthetical citation:

The underlying data have been published in DataverseNO (Hansen et al., 2026).

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Keep in mind
Text: A DOI link alone is usually not a substitute for a proper scholarly citation. Datasets should normally appear in the reference list alongside other cited works.

### Referring to datasets in Data Availability statements

Many journals, publishers, and funders require a dedicated Data Availability Statement.

When a dataset has been published, the statement should normally refer to the dataset DOI. Where publisher requirements differ, follow the instructions provided by the publisher.

Example:

```text
[text]
The data supporting the findings of this study are available in DataverseNO:

Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

### Linking datasets and publications

If your dataset supports a publication, we recommend creating explicit links in both directions:

#### In the dataset

Add the publication using the Related Publication field described in [PAGE: deposit-your-data#related-publication | Step 2: Deposit your data].

#### In the publication

In the publication, cite the dataset as explained above by including a full dataset citation in the reference list and referring to it in the text where appropriate.

This helps readers move seamlessly between the publication and the underlying data.

## Referring to a dataset before publication

In some situations, a dataset may need to be referred to and shared before it has been published in DataverseNO, for example during manuscript review when providing access to editors, reviewers, or collaborators.

In these cases, DataverseNO can provide a preview URL that grants access to an unpublished dataset draft. If you need to share a dataset before publication, please contact your [REUSE: links/contact-page | local user support].

The guidance below explains how to refer to draft datasets and how citations should be adapted when double-blind peer review requires author anonymity.

### Draft datasets under review

At the draft stage:

- The DOI has been assigned.

- The DOI has not yet been activated.

- The dataset has not yet been published.

A draft dataset may therefore be referred to in manuscripts under review, but the reference must clearly indicate that the dataset is still a draft.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Example: Citing a draft dataset, APA Style, 7th edition
Text: Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

### Double-blind peer review

If the manuscript is subject to double-blind review, identifying information must be removed.

In such cases:

- Inform the curator through the Related Publication field or directly.

- The curator can assist in creating an anonymized review version of the dataset.

- The manuscript should use an anonymized dataset citation.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Example: Anonymous draft dataset citation, APA Style, 7th edition
Text: Anonymous. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

After the manuscript is accepted, this citation should be replaced with the normal citation containing the authors' names.

### Updating citations after publication

If a manuscript cites a draft dataset during peer review, the citation should be updated once the dataset has been published.

Typical changes include:

- Replace Draft version with Version 1.

- Restore author names if anonymization was used.

- Update the publication year if necessary.

Example:

```text
[text]
Before publication, APA Style, 7th edition:
Anonymous. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

After publication, APA Style, 7th edition:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

## Dataset citation and versioning

Datasets in DataverseNO can be updated after publication. For information about updating datasets and dataset versioning, see [PAGE: modify-your-data | Step 5: Modify your data].

When changes are approved and published:

- A new version of the dataset is created.

- Older versions remain available.

- The DOI remains unchanged.

- The version number may be updated.

The purpose of versioning is to allow readers to identify the exact version used in a study.

```text
[text]
Version 1, APA Style, 7th edition:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

Version 2, APA Style, 7th edition:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2027). Bird observations from Northern Norway, 2018-2024 (Version 2) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

## Need help?

If you are unsure how to cite a dataset, refer to a dataset during peer review, or handle dataset versioning, please contact your [REUSE: links/contact-page | local user support].

## Ready for the next step?

Datasets can be updated after publication when metadata, documentation, or files need to be corrected or expanded. Proceed to:

[BUTTON]
Style: primary
Title: Step 5: Modify your data
Icon: arrow-right-circle-fill
Target: modify-your-data
