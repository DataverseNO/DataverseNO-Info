---
title: Arkiveringsguide
file_path: docs/nn/deposit/index.md
language: nn
nav_label: Arkiveringsguide
description: Les korleis du kan førebu, arkivera, publisera, sitera og endra forskingsdatasett i DataverseNO.
seo_title: DataverseNO arkiveringsguide | Førebu, arkivera, publisera, sitera og oppdatera forskingsdata
seo_description: Følg DataverseNO-arkiveringsguiden for å førebu forskingsdata, oppretta og senda inn datasett, bidra til kuratering og publisering, sitera datasett og oppdatera publiserte data.
tags:
- deposit
- dataverseno
- repository
- curation
- fair
- research-data
- data-management
keywords:
- DataverseNO arkiveringsguide
- DataverseNO deposit guidelines
- arkivera forskingsdata
- deponere forskningsdata
- publisera forskingsdata
- publisere forskningsdata
- førebu forskingsdata
- forberede forskningsdata
- datasettkuratering
- FAIR-data
- opne forskingsdata
- åpne forskningsdata
- sitera datasett
- sitere datasett
- oppdatera datasett
- forskingsdataarkiv Noreg
- forskningsdataarkiv Norge
audience:
- forskarar
- deponentar
- forskingsstøtte
- datakuratorar
- samlingsforvaltarar
primary_user_intent: Brukaren vil forstå heile arkiveringsløpet i DataverseNO og finna rettleiing for å førebu, arkivera, publisera, sitera og endra eit datasett.
parent_page: null
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/terms.yml
- data/values.yml
canonical_url: https://info.dataverse.no/nn/deposit/
social_image: null
---

# Arkiveringsguide

Vil du publisera og dela forskingsdataa dine gjennom DataverseNO? Dei fleste datasett kan gjerast klare ved å følgja nokre enkle steg, og du kan få støtte gjennom heile prosessen.

Føremålet med denne guiden er å hjelpa deg å organisera og dokumentera dataa dine på ein måte som legg til rette for gjenbruk og langtidsbevaring. Guiden forklarar korleis du kan (1) førebu dataa dine, (2) arkivera dei i arkivet som eit datasett, (3) publisera datasettet, (4) referera til det og, dersom det trengst, (5) endra datasettet etter publisering.

[WORKFLOW]
Step 1:
Number: 1
Icon: card-checklist
Title: Førebu dataa dine
Style: primary
Target: prepare-your-data
Step 2:
Number: 2
Icon: cloud-arrow-up
Title: Arkiver dataa dine
Style: primary
Target: deposit-your-data
Step 3:
Number: 3
Icon: bookmark-check
Title: Kuratering og publisering
Style: secondary
Target: publish-your-data
Step 4:
Number: 4
Icon: blockquote-left
Title: Referer til dataa dine
Style: primary
Target: refer-to-your-data
Step 5:
Number: 5
Icon: pencil-square
Title: Endra datasettet ditt
Style: primary
Target: modify-your-data
Migration note: The connecting arrows in the workflow should use the DataverseNO workflow styling defined by the Website implementation.

## Før du går i gang

Før du byrjar å førebu datasettet ditt, er det nokre viktige spørsmål og svar du bør vurdera. Dersom du er usikker på omgrep som DOI, metadata, embargo, kuratering eller datasett, kan du ta ein titt på [PAGE: glossary/index | ordlista].

### Kan eg bruka DataverseNO til å publisera og dela dataa mine?

DataverseNO tek imot forskingsdata frå alle fagområde og er gratis å bruka for forskarar som er tilknytte norske forskingsinstitusjonar. Les meir om kven som kan dela data i DataverseNO på [PAGE: about/who-can-use-dataverseno#deling-av-data-i-dataverseno | Om-sida].

### Kva om dataa mine er sensitive?

DataverseNO tek for tida berre imot data som kan delast ope. Dersom dataa dine har beskyttelsesbehov, kan det vera nødvendig med visse steg eller vurderingar før dataa kan delast ope. Dersom du er usikker på kva som gjeld for datasettet ditt, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

### Får eg hjelp til å publisera dataa mine?

Du kan få støtte gjennom heile prosessen. Alle datasett som blir sende inn til DataverseNO, blir gjennomgått av opplærte datakuratorar før publisering. Kuratorane vurderer ikkje den vitskaplege kvaliteten på sjølve forskinga, men kan hjelpa med å forbetra dokumentasjon, metadata, filorganisering, filformat og lisensinformasjon. Du treng ikkje ha alt perfekt frå starten. Les meir om kuratering på [PAGE: about/why-use-dataverseno#kuratering-og-langtidsbevaring | Om-sida].

### Kva om eg treng avgrensa tilgang?

DataverseNO tilbyr for tida ikkje avgrensa filtilgang. Det er mogleg å spesifisera ein embargoperiode der filene som er omfatta av embargo, ikkje er tilgjengelege, medan metadataa for datasettet framleis er synlege. Embargoperioden er mellombels og sluttar automatisk på ein bestemt sluttdato, maksimalt [REUSE: values/embargo-period] etter publisering. Les meir om bruk av embargo i [PAGE: deposit/deposit-your-data#embargoperiode | Steg 2: Arkiver dataa dine].

### Blir datasettet mitt siterbart?

Publiserte datasett får ein [REUSE: terms/digital-object-identifier | DOI], som gjer dei siterbare og lettare å oppdaga og gjenbruka. Les meir om synlegheit for datasett på [PAGE: about/why-use-dataverseno#kreditering-og-synlegheit | Om-sida], eller lær korleis du siterer datasett i [PAGE: deposit/refer-to-your-data | arkiveringsguiden].

### Kan eg endra datasettet mitt etter publisering?

Ja, det er mogleg å endra datasettet ditt etter publisering. Det vil oppretta ein ny versjon av datasettet. Les meir om versjonering på sida [PAGE: deposit/modify-your-data].

[ADMONITION]
Style: primary
Icon: exclamation-circle-fill
Title: Dataa dine må kunna delast ope
Text: DataverseNO er eit arkiv for forskingsdata som kan delast ope. Dersom datasettet ditt inneheld persondata, helsedata, urfolksdata, opphavsrettsleg verna materiale, kommersielt sensitiv informasjon eller annan informasjon med beskyttelsesbehov, kan det vera nødvendig med fleire steg før publisering. Dersom du er usikker på kva som gjeld for datasettet ditt, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

## Klar til å komma i gang?

Alt etter kva du treng, kan du velja ein av to måtar å komma i gang på:

- Steg 1: Førebu dataa dine gjev full rettleiing om korleis du kan organisera, dokumentera og førebu datasettet ditt for publisering.

- Hurtigguide og sjekkliste gjev ei kort oversikt over dei viktigaste stega og krava for erfarne brukarar, eller for dei som ønskjer ei rask oversikt før dei går vidare til detaljane.

[BUTTON]
Style: primary
Icon: arrow-right-circle-fill
Title: Steg 1: Førebu dataa dine
Target: prepare-your-data
[BUTTON]
Style: secondary
Icon: arrow-right-circle-fill
Title: Hurtigguide og sjekkliste
Target: deposit-quick-guide

## Nyttige ressursar

Leitar du etter ein bestemt ressurs? Kanskje det er ein av desse:

[RESOURCE BOX GRID]
[RESOURCE BOX]
Style: primary
Icon: file-earmark-check
Title: Tilrådde filformat
Target: file-formats/index
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: README-filmal
URL: https://doi.org/10.5281/zenodo.7453999
Open: new-tab
[RESOURCE BOX]
Style: primary
Icon: gear-fill
Title: Full metadataguide (lenkje kjem)
Target: [pending]
Migration note: Replace [pending] with the approved internal target before publication, or remove this resource box until the target page exists.
