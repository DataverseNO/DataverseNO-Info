---
title: Who can use DataverseNO?
file_path: docs/en/about/who-can-use-dataverseno.md
language: en
nav_label: Who can use DataverseNO?
description: Learn who can archive, share, reuse, and support data in DataverseNO, including researchers from partner institutions, researchers from other institutions, data users, and prospective partner institutions.
seo_title: Who can use DataverseNO? | Eligibility, reuse, and partner institutions
seo_description: Learn who can use DataverseNO to archive, share, and reuse research data, what applies to researchers at partner and non-partner institutions, and how institutions can become partners.
tags:
- dataverseno
- service
- repository
- deposit
- support
- partners
- research-data
keywords:
- DataverseNO users
- who can use DataverseNO
- DataverseNO partner institutions
- deposit research data Norway
- archive research data
- reuse research data
- Norwegian research institutions
- become DataverseNO partner
- research data support
audience:
- researchers
- data depositors
- data users
- research support staff
- partner institutions
- prospective partner institutions
- collection managers
- repository managers
primary_user_intent: User wants to know whether they or their institution can use DataverseNO to archive, share, reuse, or support research data.
parent_page: About
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/partners.yml
- data/links.yml
- data/values.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/en/about/who-can-use-dataverseno/
social_image: null
---

# Who can use DataverseNO?

DataverseNO supports different use cases, depending on who you are. Read more about the different types of use below:

[CARD GRID]
[NAVIGATION CARD]
Style: primary
Icon: database-add
Title: Sharing data
Target: sharing-data-in-dataverseno
[NAVIGATION CARD]
Style: primary
Icon: share
Title: Reusing data
Target: reusing-data-in-dataverseno
[NAVIGATION CARD]
Style: primary
Icon: pencil-square
Title: Becoming a partner institution
Target: becoming-a-partner-institution

## Sharing data in DataverseNO

Researchers affiliated with a Norwegian research institution can use DataverseNO free of charge to archive and share their research data.

### Researchers from partner institutions

If you are affiliated with a DataverseNO partner institution, there are currently no limitations to the amount of data you can archive and share in the repository (but please see [PAGE: deposit/deposit-your-data#file-and-dataset-recommendations | our file and dataset recommendations] before depositing large or complex datasets). Are you unsure whether your institution is a partner? The current DataverseNO partner institutions are listed below:

[GENERATED COMPONENT]
ID: partner-institution-logo-grid
Language: en
Source data: data/partners.yml
Output: Partner institution logo grid for the section "Researchers from partner institutions".
Fallback: Use the partner IDs listed in the following CARD GRID if the component is not generated automatically.
Migration note: During Markdown migration, render this grid from data/partners.yml. The partner IDs below are source identifiers, not logo filenames.

[CARD GRID]
mf
nibio
nmbu
nofima
nord
ntnu
oslomet
uit
uia
uib
inn
uio
usn
uis
hvl
hiof
vid

All partner institutions have well-established research support units, such as university libraries, that communicate closely with researchers during the [PAGE: deposit/index | deposit process] and [PAGE: about/why-use-dataverseno#curation-and-preservation | curation]. Researchers can contact local user support in several ways, for example by submitting a dataset for review in the relevant institutional collection or by using the contact information on [REUSE: links/contact-page].

### Researchers from Norwegian non-partner institutions

If you are affiliated with a Norwegian research institution that is not a DataverseNO partner, you can receive up to 10 GB storage space free of charge. Your data will be curated by support staff at UiT. If your dataset exceeds 10 GB, please contact [REUSE: partners/repository_management/support.email].

### Researchers from institutions outside Norway

If you are not affiliated with a Norwegian research institution, you may still be able to deposit datasets in DataverseNO if you collaborate with a researcher from a Norwegian research institution who is also one of the authors of the dataset or datasets.

More information about how to create a user account is available in [PAGE: deposit/index | the Deposit Guidelines].

## Reusing data in DataverseNO

Datasets published in DataverseNO are discoverable in the main discovery services for research data (see [PAGE: about/why-use-dataverseno#credit-and-visibility]). You can also [search](https://dataverse.no/dataverse/root/search) and browse all DataverseNO collections directly in the repository. Before reusing data, you should review the dataset-specific terms of reuse and make sure that you understand the accompanying [PAGE: deposit/deposit-your-data#choose-terms-for-reuse | data licence]. Regardless of licence type, both [Dataverse Community Norms](https://dataverse.org/best-practices/dataverse-community-norms) and good scientific practice expect that proper credit is given through citation. Use the dataset citation provided on the dataset page. To learn more about citing datasets in DataverseNO, see [PAGE: deposit/refer-to-your-data | the Deposit Guidelines].

## Becoming a partner institution

[GENERATED VALUE]
ID: partner-institution-count
Source data: data/partners.yml
Expression: count(partners)
Output: Number of current DataverseNO partner institutions

Norwegian research institutions can join the DataverseNO consortium to offer their researchers unlimited access to a trustworthy data repository. To become a partner, the institution must agree to comply with [REUSE: links/dataverseno-organizational-agreement] by signing a partner agreement. The DataverseNO consortium currently includes [GENERATED VALUE: partner-institution-count] [SECTION: researchers-from-partner-institutions | partner institutions] and is open to new partners.

Partner institutions get access to the following:

- Initial training: Collection managers and curators at partner institutions receive training and help getting started with DataverseNO.

- Continuous guidance: Collection managers and curators at partner institutions receive continuous support related to archiving and curating data. This includes, for example, guidance on building local curation expertise and on collection management.

- National community: Curators at partner institutions gain access to a national competence network that supports knowledge sharing and collaboration through an online platform, monthly curator calls, and network meetings twice a year.

- International community: Partner institutions have access to international collaboration and support through the [Global Dataverse Community Consortium](https://www.gdcc.io/), including work on software improvements and good practices for research data archiving and sharing.

Important points to note for prospective partner institutions:

- Access to demo site: Institutions wishing to test the functionality of the Dataverse repository software can get access to [our sandbox](https://demo.dataverse.no/) by contacting [REUSE: partners/repository_management/support.email].

- Membership commitment: The [REUSE: terms/dataverseno-organizational-agreement] is renewed every five years. Partner institutions commit to membership for the full duration of the current period.

- Pricing model: Partner institutions pay a one-time start-up fee and a recurring annual fee, as specified in the annually updated [REUSE: links/dataverseno-price-overview]. The pricing model builds on common collaboration models in the Norwegian higher education sector. Further details are available in chapter 4.2 of [REUSE: links/dataverseno-organizational-agreement].

- Smaller partner institutions: To support smaller institutions, DataverseNO can offer an alternative curation model in which staff at UiT handle dataset curation during an initial phase.

- Handling of large datasets: DataverseNO currently supports small and medium-sized datasets, although we are working to increase our capacity to handle larger volumes. For datasets exceeding [REUSE: values/dataset-size-limit] in total size, we recommend using another repository service. We also recommend limiting datasets to approximately [REUSE: values/file-number-limit], to ensure smooth handling of file-level Digital Object Identifiers (DOIs).

- Organizational documents: An overview of the organizational documents, including agreements and the policy framework, is available in the [REUSE: links/dataverseno-organizational-agreement].

For more information about becoming a partner institution, please contact [REUSE: partners/repository_management/support.email].
