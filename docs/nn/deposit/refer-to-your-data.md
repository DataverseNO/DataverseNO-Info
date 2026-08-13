---
title: 'Steg 4: Referer til dataa dine'
file_path: docs/nn/deposit/refer-to-your-data.md
language: nn
nav_label: Referer til dataa dine
description: Les korleis du kan sitera publiserte datasett, referera til datasett før publisering, skriva datatilgjengelegheitserklæringar og handtera datasettversjonar i DataverseNO.
seo_title: Siter og referer til datasett i DataverseNO | DOI, datatilgjenge, utkast og versjonering
seo_description: Les korleis du kan sitera publiserte datasett i DataverseNO, referera til datasettutkast under vurdering, skriva datatilgjengelegheitserklæringar og handtera datasettreferansar og versjonering.
tags:
- deposit
- dataverseno
- data-citation
- doi
- versioning
- research-data
- publication
keywords:
- sitera datasett
- sitere datasett
- DataverseNO-sitering
- DataverseNO citation
- dataset DOI
- data availability statement
- sitera forskingsdata
- sitere forskningsdata
- datasettutkast
- double-blind peer review data
- datasettversjonering
- research data citation
audience:
- forskarar
- deponentar
- forfattarar
- tidsskriftredaktørar
- fagfellar
- forskingsstøtte
- datakuratorar
primary_user_intent: Brukaren vil vita korleis ein kan sitera eller referera til eit DataverseNO-datasett i publikasjonar, under fagfellevurdering eller etter versjonsoppdateringar.
parent_page: Arkiveringsguide
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/nn/deposit/refer-to-your-data/
social_image: null
---

# Steg 4: Referer til dataa dine

Når datasettet er publisert, blir det eit siterbart forskingsresultat som kan brukast i artiklar, bøker, avhandlingar, rapportar og andre vitskaplege publikasjonar.

Dette steget forklarar:

- [SECTION: etter-publisering | Kva som skjer etter publisering].

- [SECTION: kvifor-datasett-bor-siterast | Kvifor datasett bør siterast].

- [SECTION: korleis-sitera-eit-publisert-datasett | Korleis du siterer eit publisert datasett].

- [SECTION: korleis-referera-til-datasett-i-ein-publikasjon | Korleis du refererer til datasett i ein publikasjon].

- [SECTION: referera-til-eit-datasett-for-publisering | Korleis du refererer til eit datasett før publisering].

- [SECTION: datasettreferanse-og-versjonering | Korleis versjonering påverkar datasettreferansen].

## Etter publisering

Når datasettet er publisert, skjer følgjande:

- [REUSE: terms/digital-object-identifier | DOI-en] blir aktiv.

- Datasettet blir offentleg tilgjengeleg.

- Datasettet blir søkbart i DataverseNO og eksterne søkjetenester.

- Datasettet kan siterast og delast som forskingsresultat.

[ADMONITION]
Style: primary
Icon: exclamation-circle-fill
Title: Hugs
Text: Ikkje distribuer eller siter datasett-DOI-en offentleg før datasettet er publisert og DOI-en er aktivert.

## Kvifor datasett bør siterast

Forskingsdata bør siterast på same måte som andre vitskaplege resultat, til dømes tidsskriftartiklar, bøker, programvare eller rapportar.

Datasitering har fleire føremål:

- Det gjev kreditering til dei som har laga datasettet.

- Det gjer det mogleg for andre å finna dei nøyaktige dataa som er brukte i ein studie.

- Det gjer forskinga meir transparent og reproduserbar.

- Det hjelper med å etablera koplingar mellom publikasjonar og underliggjande forskingsdata.

Som hovudregel bør datasettet siterast dersom ein publikasjon byggjer på datasettet.

## Korleis sitera eit publisert datasett

Når eit datasett er publisert, blir ein tilrådd referanse vist i den blåe boksen på datasettsida. Slik finn du referansen:

- Opna datasettsida.

- Finn den blåe boksen nær toppen av sida.

- Kopier referansen og tilpass han dersom publikasjonskanalen krev ein annan siteringsstil.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Døme: Sitering av publisert datasett i APA-stil, 7. utgåve
Text: Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

## Korleis referera til datasett i ein publikasjon

Datasett bør normalt refererast til på to måtar:

### I referanselista

Ta med ein full datasettreferanse i referanselista, på same måte som du ville gjort for ein artikkel, ei bok eller eit anna verk du siterer.

Døme, APA-stil, 7. utgåve:

```text
[text]
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

### I teksten

Referer til datasettet i teksten med den siteringsstilen som publikasjonskanalen krev.

Døme, APA-stil, 7. utgåve:

```text
[text]
The underlying data are available in Hansen et al. (2026).
```

Døme, parentesreferanse:

```text
[text]
The underlying data have been published in DataverseNO (Hansen et al., 2026).
```

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Hugs
Text: Ei DOI-lenkje åleine er som regel ikkje nok som vitskapleg referanse. Datasett bør normalt stå i referanselista saman med andre siterte arbeid.

### Referera til datasett i datatilgjengelegheitserklæringar

Mange tidsskrift, forlag og finansiørar krev ei eiga **datatilgjengelegheitserklæring** (Data Availability Statement).

Når datasettet er publisert, bør erklæringa normalt visa til DOI-en til datasettet. Dersom publikasjonskanalen har andre krav, følg instruksjonane frå publikasjonskanalen.

Døme:

```text
[text]
The data supporting the findings of this study are available in DataverseNO:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

### Kopla datasett og publikasjonar

Dersom datasettet ditt stør opp om ein publikasjon, tilrår vi å laga tydelege koplingar i begge retningar:

#### I datasettet

Legg til publikasjonen i feltet _Related Publication_, som er beskrive i [PAGE: deposit-your-data#related-publication | **Steg 2: Arkiver dataa dine**].

#### I publikasjonen

I publikasjonen bør du sitera datasettet slik det er forklart ovanfor: Ta med ein full datasettreferanse i referanselista, og vis til datasettet i teksten der det er relevant.

Dette gjer det lettare for lesarar å navigera mellom publikasjonen og dei underliggjande dataa.

## Referera til eit datasett før publisering

I nokre situasjonar kan det vera nødvendig å referera til og dela eit datasett før det er publisert i DataverseNO, til dømes under manuskriptvurdering når redaktørar, fagfellar eller samarbeidspartnarar skal få tilgang.

I slike tilfelle kan DataverseNO gje tilgang til eit upublisert datasettutkast gjennom ein preview URL. Dersom du treng å dela eit datasett før publisering, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

Rettleiinga nedanfor forklarar korleis du kan referera til datasettutkast, og korleis referansar bør tilpassast når dobbelblind fagfellevurdering krev anonymitet.

### Datasettutkast under vurdering

På utkaststadiet gjeld følgjande:

- DOI-en er tildelt.

- DOI-en er ikkje aktivert.

- Datasettet er ikkje publisert enno.

Eit datasettutkast kan derfor refererast til i manuskript under vurdering, men av referansen må det gå tydeleg fram at datasettet framleis er eit utkast.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Døme: Sitering av datasettutkast, APA-stil, 7. utgåve
Text: Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1

### Dobbelblind fagfellevurdering

Dersom manuskriptet er under dobbelblind vurdering, må identifiserande informasjon fjernast.

I slike tilfelle gjeld følgjande:

- Informer kuratoren gjennom feltet _Related Publication_ eller direkte.

- Kuratoren kan hjelpa med å laga ein anonymisert vurderingsversjon av datasettet.

- Manuskriptet bør bruka ein anonymisert datasettreferanse.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Døme: anonym datasettreferanse for utkast, APA-stil, 7. utgåve
Text: Anonymous. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
After the manuscript is accepted, this citation should be replaced with the normal citation containing the authors' names.

### Oppdatera referansar etter publisering

Dersom eit manuskript siterer eit datasettutkast under fagfellevurdering, bør referansen oppdaterast når datasettet er publisert.

Vanlege endringar er:

- Byt ut **Draft version** med **Version 1**.

- Set inn forfattarnamn att dersom anonymisering blei brukt.

- Oppdater publiseringsåret dersom det trengst.

Døme:

```text
[text]
Before publication, APA-stil, 7. utgåve:
Anonymous. (2026). Bird observations from Northern Norway, 2018-2024 (Draft version) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
After publication, APA-stil, 7. utgåve:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

## Datasettreferanse og versjonering

Datasett i DataverseNO kan oppdaterast etter publisering. Sjå [PAGE: modify-your-data | Steg 5: Endra datasettet ditt] for informasjon om oppdatering av datasett og datasettversjonering.

Når endringar er godkjende og publiserte, gjeld følgjande:

- Det blir oppretta ein ny versjon av datasettet.

- Eldre versjonar er framleis tilgjengelege.

- DOI-en er uendra.

- Versjonsnummeret kan bli oppdatert.

Føremålet med versjonering er å gjera det mogleg for lesarar å identifisera den nøyaktige versjonen som er brukt i ein studie.

```text
[text]
Version 1, APA-stil, 7. utgåve:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
Version 2, APA-stil, 7. utgåve:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2027). Bird observations from Northern Norway, 2018-2024 (Version 2) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

## Treng du hjelp?

Dersom du er usikker på korleis du skal sitera eit datasett, referera til eit datasett under fagfellevurdering eller handtera datasettversjonering, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

## Klar for neste steg?

Datasett kan oppdaterast etter publisering dersom metadata, dokumentasjon eller filer må rettast eller utvidast. Gå vidare til:

[BUTTON]
Style: primary
Title: Steg 5: Endra datasettet ditt
Icon: arrow-right-circle-fill
Target: modify-your-data
