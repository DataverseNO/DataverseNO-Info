---
title: Kven kan bruka DataverseNO?
file_path: docs/nn/about/who-can-use-dataverseno.md
language: nn
nav_label: Kven kan bruka DataverseNO?
description: Les kven som kan arkivera, dela og gjenbruka data i DataverseNO, inkludert forskarar ved partnarinstitusjonar, forskarar ved andre institusjonar, databrukarar og moglege partnarinstitusjonar.
seo_title: Kven kan bruka DataverseNO? | Kven kan arkivera, gjenbruka og bli partnar
seo_description: Les kven som kan bruka DataverseNO til å arkivera, dela og gjenbruka forskingsdata, kva som gjeld for forskarar ved partnar- og ikkje-partnarinstitusjonar, og korleis institusjonar kan bli partnarar.
tags:
- dataverseno
- service
- repository
- deposit
- support
- partners
- research-data
keywords:
- DataverseNO-brukarar
- hvem kan bruke DataverseNO
- kven kan bruka DataverseNO
- DataverseNO partnarinstitusjonar
- DataverseNO partnerinstitusjoner
- arkivera forskingsdata
- deponere forskningsdata
- gjenbruka forskingsdata
- gjenbruke forskningsdata
- norske forskingsinstitusjonar
- norske forskningsinstitusjoner
- bli DataverseNO-partnar
- bli DataverseNO-partner
- forskingsdatastøtte
- forskningsdatastøtte
audience:
- forskarar
- deponentar
- databrukarar
- forskingsstøtte
- partnarinstitusjonar
- moglege partnarinstitusjonar
- samlingsforvaltarar
- arkivforvaltarar
primary_user_intent: Brukaren vil vita om brukaren eller institusjonen kan bruka DataverseNO til å arkivera, dela, gjenbruka eller støtta forskingsdata.
parent_page: About
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/partners.yml
- data/links.yml
- data/values.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/nn/about/who-can-use-dataverseno/
social_image: null
---

# Kven kan bruka DataverseNO?

DataverseNO har ulike bruksområde, alt etter kven du er. Les meir om dei ulike bruksområda nedanfor:

[CARD GRID]
[NAVIGATION CARD]
Style: primary
Icon: database-add
Title: Dela data
Target: deling-av-data-i-dataverseno
[NAVIGATION CARD]
Style: primary
Icon: share
Title: Gjenbruka data
Target: gjenbruk-av-data-i-dataverseno
[NAVIGATION CARD]
Style: primary
Icon: pencil-square
Title: Bli partnarinstitusjon
Target: bli-partnarinstitusjon

## Deling av data i DataverseNO

Forskarar som er tilknytte ein norsk forskingsinstitusjon, kan bruka DataverseNO gratis til å arkivera og dela forskingsdataa sine.

### Forskarar frå partnarinstitusjonar

Dersom du er tilknytt ein DataverseNO-partnarinstitusjon, er det for tida inga avgrensing på kor mykje data du kan arkivera og dela i arkivet (men sjå [PAGE: deposit/deposit-your-data#tilrådingar-for-filer-og-datasett | tilrådingane våre for filer og datasett] før du arkiverer store eller komplekse datasett). Er du usikker på om institusjonen din er partnar? Dei noverande DataverseNO-partnarinstitusjonane er lista opp nedanfor:

[GENERATED COMPONENT]
ID: partner-institution-logo-grid
Language: nn
Source data: data/partners.yml
Output: Partner institution logo grid for the section "Forskarar frå partnarinstitusjonar".
Fallback: Use the partner IDs listed in the following CARD GRID if the component is not generated automatically.
Migration note: During Markdown migration, render this grid from data/partners.yml. The partner IDs below are source identifiers, not logo filenames.

[CARD GRID]
hiof
hvl
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
vid

Alle partnarinstitusjonane har veletablerte forskingsstøtteeiningar, til dømes universitetsbiblioteka, som har tett kontakt med forskarane under [PAGE: deposit/index | arkiveringsprosessen] og [PAGE: why-use-dataverseno#kuratering-og-langtidsbevaring | kurateringa]. Forskarar kan kontakta den lokale brukarstøtta på fleire måtar, til dømes ved å senda inn eit datasett til kuratering i den aktuelle institusjonssamlinga eller ved å kontakta brukarstøtta via adressa på [REUSE: links/contact-page].

### Forskarar frå norske ikkje-partnarinstitusjonar

Dersom du er tilknytt ein norsk forskingsinstitusjon som ikkje er DataverseNO-partnar, kan du få inntil 10 GB lagringsplass gratis. Dataa dine blir kuraterte av støttepersonell ved UiT. Dersom datasettet ditt er større enn 10 GB, kan du kontakta [REUSE: partners/repository_management/support.email].

### Forskarar frå institusjonar utanfor Noreg

Dersom du ikkje er tilknytt ein norsk forskingsinstitusjon, kan du likevel få høve til å arkivera datasett i DataverseNO dersom du samarbeider med ein forskar frå ein norsk forskingsinstitusjon som òg er ein av forfattarane av datasettet eller datasetta.

Meir informasjon om korleis du opprettar brukarkonto, finn du i [PAGE: deposit/index | arkiveringsguiden].

## Gjenbruk av data i DataverseNO

Datasett som er publiserte i DataverseNO, er gjenfinnbare i dei viktigaste oppdagingstenestene for forskingsdata (sjå [PAGE: why-use-dataverseno#kreditering-og-synlegheit]). Du kan òg [search](https://dataverse.no/dataverse/root/search) og bla gjennom alle DataverseNO-samlingane direkte i arkivet. Før du gjenbrukar data, bør du lesa dei datasettspesifikke gjenbruksvilkåra og forsikra deg om at du forstår den tilhøyrande [PAGE: deposit/deposit-your-data#vel-gjenbruksvilkår | datalisensen]. Uavhengig av lisenstype forventar både [Dataverse Community Norms](https://dataverse.org/best-practices/dataverse-community-norms) og god vitskapleg praksis at du gjev korrekt kreditering gjennom sitering. Bruk datasettreferansen som står på datasettsida. Les meir om å sitera datasett i DataverseNO i [PAGE: deposit/refer-to-your-data | arkiveringsguiden].

## Bli partnarinstitusjon

[GENERATED VALUE]
ID: partner-institution-count
Source data: data/partners.yml
Expression: count(partners)
Output: Number of current DataverseNO partner institutions

Norske forskingsinstitusjonar kan bli med i DataverseNO-konsortiet for å gje forskarane sine uavgrensa tilgang til eit påliteleg dataarkiv. For å bli partnar må institusjonen forplikta seg til å følgja [REUSE: links/dataverseno-organizational-agreement] ved å signera ein partnaravtale. DataverseNO-konsortiet består for tida av [GENERATED VALUE: partner-institution-count] [SECTION: forskarar-frå-partnarinstitusjonar | partnarinstitusjonar] og er ope for nye partnarar.

Partnarinstitusjonar får tilgang til dette:

- Innleiande opplæring: Samlingsforvaltarar og kuratorar ved partnarinstitusjonar får opplæring og hjelp til å komma i gang med DataverseNO.

- Løpande rettleiing: Samlingsforvaltarar og kuratorar ved partnarinstitusjonar får løpande støtte knytt til arkivering og kuratering av data. Det omfattar til dømes rettleiing på å byggja opp lokal kurateringskompetanse og om samlingsforvaltning.

- Nasjonalt fellesskap: Kuratorar ved partnarinstitusjonar får tilgang til eit nasjonalt kompetansenettverk som støttar kunnskapsdeling og samarbeid gjennom ei nettplattform, månadlege kuratormøte og nettverkssamlingar to gonger i året.

- Internasjonalt fellesskap: Partnarinstitusjonar får tilgang til internasjonalt samarbeid og støtte gjennom [Global Dataverse Community Consortium](https://www.gdcc.io/), mellom anna om programvareforbetringar og god praksis for arkivering og deling av forskingsdata.

Viktige punkt å merka seg for institusjonar som vurderer partnarskap:

- Tilgang til demoside: Institusjonar som ønskjer å testa funksjonaliteten i Dataverse-programvara, kan få tilgang til [sandkassa vår](https://demo.dataverse.no/) ved å kontakta [REUSE: partners/repository_management/support.email].

- Medlemskapsforplikting: [REUSE: terms/dataverseno-organizational-agreement] blir fornya kvart femte år. Partnarinstitusjonar forpliktar seg til medlemskap for heile den gjeldande perioden.

- Prismodell: Partnarinstitusjonar betaler ei eingongsavgift ved oppstart og ei årleg avgift, slik det er spesifisert i den årleg oppdaterte [REUSE: links/dataverseno-price-overview]. Prismodellen byggjer på vanlege samarbeidsmodellar i norsk universitets- og høgskulesektor. Meir informasjon finst i kapittel 4.2 i [REUSE: links/dataverseno-organizational-agreement].

- Mindre partnarinstitusjonar: For å støtta mindre institusjonar kan DataverseNO tilby ein alternativ kurateringsmodell der tilsette ved UiT handterer datasettkuratering i ein innleiande fase.

- Handtering av store datasett: DataverseNO støttar for tida små og mellomstore datasett, sjølv om vi arbeider med å auka kapasiteten for større datamengder. For datasett som er større enn [REUSE: values/dataset-size-limit] totalt, tilrår vi å bruka ei anna arkivteneste. Vi tilrår òg å avgrensa datasett til om lag [REUSE: values/file-number-limit], for å sikra smidig handtering av DOI-ar på filnivå.

- Organisasjonsdokument: Ei oversikt over organisasjonsdokumenta, inkludert avtalar og policy-rammeverk, finst i [REUSE: links/dataverseno-organizational-agreement].

Dersom du ønskjer meir informasjon om å bli partnarinstitusjon, kan du kontakta [REUSE: partners/repository_management/support.email].
