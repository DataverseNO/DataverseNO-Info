---
title: Kontakt
file_path: docs/nn/contact/index.md
language: nn
nav_label: Kontakt
description: Finn kontaktinformasjon til DataverseNO-arkivforvaltninga og lokale støttetenester ved DataverseNO-partnarinstitusjonane.
seo_title: Kontakt DataverseNO | Arkivforvaltning og lokale støttetenester
seo_description: Finn kontaktinformasjon til DataverseNO-arkivforvaltninga og lokale støttetenester ved partnarinstitusjonar for spørsmål om å arkivera, dokumentera, publisera og bruka forskingsdata.
tags:
- dataverseno
- support
- repository
- partners
- research-data
keywords:
- kontakt DataverseNO
- DataverseNO-støtte
- DataverseNO support
- kontakt arkivforvaltning
- repository management contact
- lokal forskingsdatastøtte
- lokal forskningsdatastøtte
- DataverseNO-partnarinstitusjonar
- DataverseNO-partnerinstitusjoner
- forskingsdatastøtte Noreg
- forskningsdatastøtte Norge
- dataarkiveringsstøtte
- data deposit support
audience:
- forskarar
- deponentar
- databrukarar
- forskingsstøtte
- datakuratorar
- samlingsforvaltarar
- arkivforvaltarar
- partnarinstitusjonar
primary_user_intent: Brukaren vil finna rett kontaktpunkt i DataverseNO, anten DataverseNO-arkivforvaltninga eller den lokale støttetenesta ved institusjonen sin.
parent_page: null
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources: data/partners.yml
canonical_url: https://info.dataverse.no/nn/contact/
social_image: null
---

# Kontakt

Treng du hjelp med DataverseNO?

Dersom du er tilknytt ein DataverseNO-partnarinstitusjon, bør du kontakta den lokale brukarstøtta ved institusjonen din. Dei kan hjelpa med spørsmål om arkivering, dokumentasjon og publisering av forskingsdata i DataverseNO.

Dersom institusjonen din ikkje står på lista, eller dersom spørsmålet gjeld DataverseNO som arkiv, kan du kontakta [REUSE: partners/repository_management/support.email].

## DataverseNO-arkivforvaltninga

For spørsmål om DataverseNO som arkiv, arkivpolicyar, teknisk drift, partnarinstitusjonar eller andre spørsmål på arkivnivå, kontakt DataverseNO-arkivforvaltninga.

[GENERATED COMPONENT]
ID: repository-management-contact-card
Language: nn
Source data: data/partners.yml
Output: Repository management contact card
Fallback: Display the repository management support email from data/partners.yml as a mailto link.
Accessibility note: The generated contact card must use meaningful link text and remain usable if JavaScript is unavailable.

## Lokal brukarstøtte

Finn den lokale brukarstøtta ved institusjonen din nedanfor.

Bruk søkjefeltet for å filtrera lista etter institusjonsnamn, forkorting, stadnamn eller andre vanlege søkjeord.

[GENERATED COMPONENT]
ID: contact-search-input
Language: nn
Source data: data/partners.yml
Output: Page-local search input for filtering partner institution contact cards
Default state: No search or filter is applied when the page first loads.
Fallback: Omit the search field if JavaScript is unavailable.
Accessibility note: The search input must have a visible label and must not prevent keyboard access.

[GENERATED COMPONENT]
ID: partner-contact-cards
Language: nn
Source data: data/partners.yml
Output: Partner institution contact cards
Default state: Show all partner contact cards when no search or filter is active.
Fallback: Show all partner contact cards if JavaScript is unavailable.
Migration note: During Markdown migration, preserve this generated-component marker or replace it with the approved Contact page placeholder. Do not manually duplicate partner contact data from data/partners.yml.

## Dersom institusjonen din ikkje står på lista

Dersom institusjonen din ikkje står på lista ovanfor, kan du kontakta [REUSE: partners/repository_management/support.email].
