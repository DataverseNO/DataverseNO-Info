---
title: Contact
file_path: docs/en/contact/index.md
language: en
nav_label: Contact
description: Find DataverseNO repository management contact information and local support services at DataverseNO partner institutions.
seo_title: Contact DataverseNO | Repository management and local support services
seo_description: Find contact information for DataverseNO repository management and local support services at partner institutions for questions about depositing, documenting, publishing, and using research data.
tags:
- dataverseno
- support
- repository
- partners
- research-data
keywords:
- contact DataverseNO
- DataverseNO support
- repository management contact
- local research data support
- DataverseNO partner institutions
- research data support Norway
- data deposit support
audience:
- researchers
- data depositors
- data users
- research support staff
- data curators
- collection managers
- repository managers
- partner institutions
primary_user_intent: User wants to find the correct DataverseNO contact point, either repository management or the local support service at their institution.
parent_page: null
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources: data/partners.yml
canonical_url: https://info.dataverse.no/en/contact/
social_image: null
---

# Contact

Need help with DataverseNO?

If you are affiliated with a DataverseNO partner institution, please contact the local support service at your institution. They can help with questions about depositing, documenting, and publishing research data in DataverseNO.

If your institution is not listed, or if your question concerns DataverseNO as a repository, please contact [REUSE: partners/repository_management/support.email].

## DataverseNO repository management

For questions about DataverseNO as a repository, repository policies, technical operation, partner institutions, or other repository-level matters, contact DataverseNO repository management.

[GENERATED COMPONENT]
ID: repository-management-contact-card
Language: en
Source data: data/partners.yml
Output: Repository management contact card
Fallback: Display the repository management support email from data/partners.yml as a mailto link.
Accessibility note: The generated contact card must use meaningful link text and remain usable if JavaScript is unavailable.

## Local support services

Find the local user support service at your institution below.

Use the search field to filter the list by institution name, abbreviation, city, or other common search terms.

[GENERATED COMPONENT]
ID: contact-search-input
Language: en
Source data: data/partners.yml
Output: Page-local search input for filtering partner institution contact cards
Default state: No search or filter is applied when the page first loads.
Fallback: Omit the search field if JavaScript is unavailable.
Accessibility note: The search input must have a visible label and must not prevent keyboard access.

[GENERATED COMPONENT]
ID: partner-contact-cards
Language: en
Source data: data/partners.yml
Output: Partner institution contact cards
Default state: Show all partner contact cards when no search or filter is active.
Fallback: Show all partner contact cards if JavaScript is unavailable.
Migration note: During Markdown migration, preserve this generated-component marker or replace it with the approved Contact page placeholder. Do not manually duplicate partner contact data from data/partners.yml.

## If your institution is not listed

If your institution is not listed above, please contact [REUSE: partners/repository_management/support.email].
