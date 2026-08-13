---
title: 'Steg 1: Førebu dataa dine'
file_path: docs/nn/deposit/prepare-your-data.md
language: nn
nav_label: Førebu dataa dine
description: Les korleis du kan organisera, formatera, dokumentera og kontrollera storleiken på forskingsdata før du arkiverer eit datasett i DataverseNO.
seo_title: Førebu forskingsdata for DataverseNO | Filer, format, README og dokumentasjon
seo_description: Les korleis du kan førebu forskingsdata for DataverseNO ved å organisera filer, velja eigna filformat, laga ei README-fil, leggja til dokumentasjon og kontrollera storleiken på filer og datasett.
tags:
- deposit
- data-management
- documentation
- file-formats
- curation
- research-data
- fair
keywords:
- førebu forskingsdata
- forberede forskningsdata
- DataverseNO README-fil
- DataverseNO README file
- filorganisering
- file organization
- tilrådde filformat
- anbefalte filformater
- forskingsdatadokumentasjon
- forskningsdatadokumentasjon
- datasettdokumentasjon
- filer
- filstorleik
- filstørrelse
- FAIR data
audience:
- forskarar
- deponentar
- forskingsstøtte
- datakuratorar
primary_user_intent: Brukaren vil førebu eit datasett for arkivering i DataverseNO ved å organisera filer, velja eigna format, laga dokumentasjon og kontrollera storleiken på filer og datasett.
parent_page: Arkiveringsguide
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/values.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/nn/deposit/prepare-your-data/
social_image: null
---

# Steg 1: Førebu dataa dine

Før du arkiverer dataa dine i DataverseNO, bør du bruka litt tid på å organisera og dokumentera datasettet. Det gjer det lettare for andre å forstå, gjenbruka og sitera dataa dine, og det bidreg til ein smidigare publiseringsprosess.

Dei fleste datasett kan gjerast klare ved å følgja nokre enkle steg:

- [SECTION: organiser-filene-dine | **Organiser filene dine**], slik at dei er lette å finna fram i og forstå.

- [SECTION: vel-eigna-filformat | **Vel eigna filformat**] som stør opp om langtidsbevaring og gjenbruk.

- [SECTION: beskriv-dataa-dine | **Beskriv dataa dine**] med ei README-fil og annan relevant dokumentasjon.

- [SECTION: sjekk-fil-og-datasettstorleik | **Sjekk fil- og datasettstorleik**] før du lastar opp filene.

Du treng ikkje å ha alt perfekt. Føremålet med denne guiden er å hjelpa deg å førebu data som andre kan forstå og gjenbruka. Ved behov kan støttepersonell gje meir rettleiing under [REUSE: terms/curation | kurateringsprosessen] før publisering.

Dersom du er usikker på kva som gjeld for datasettet ditt, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte]. Vi hjelper gjerne.

## Organiser filene dine

God filorganisering gjer det lettare for samarbeidspartnarar, kuratorar og framtidige brukarar å finna fram i datasettet ditt.

### God praksis for filnamn

- Bruk beskrivande filnamn.

- Bruk konsekvent namngjeving.

- Hald filnamna rimeleg korte.

- Bruk datoformatet ÅÅÅÅ-MM-DD.

- Unngå mellomrom og spesialteikn.

[ADMONITION]
Style: secondary
Icon: check-circle-fill
Title: Døme: gode filnamn
Text:
- 00_README.txt
- survey_data_2025-08.csv
- species_observations_2024-06-27.tsv
- interview_metadata.xlsx

[ADMONITION]
Style: tertiary
Icon: x-circle-fill
Title: Døme: dårlege filnamn
Text:
- data 1.xlsx
- gruppe Ø-Å final final NEW.xlsx
- test.docx
- utan_namn.csv

### Rekneark og tabelldata

For rekneark og tabellfiler tilrår vi:

- Éin tabell per fil.

- Éi rad per observasjon.

- Éin kolonne per variabel.

- Éin verdi per celle.

- Variabelnamn utan mellomrom eller spesialteikn.

Du finn meir detaljert rettleiing i kapittelet [Data Organisation in Spreadsheets](https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-spreadsheets.html) i The Turing Way handbook to reproducible, ethical and collaborative data science.

## Vel eigna filformat

### Kvifor har filformat noko å seia?

Nokre filformat er lettare å bevara over tid og gjenbruka enn andre. DataverseNO tilrår derfor ei rekkje filformat som er særleg eigna for langtidsbevaring og gjenbruk over tid.

Mange datasett kan likevel publiserast i dei opphavlege formata sine. Bruk av eit ikkje-tilrådd format er som regel ikkje noko hinder for publisering.

Dersom dataa dine opphavleg er laga i eit ikkje-tilrådd filformat, tilrår vi ofte å lasta opp både eit tilrådd filformat og det opphavlege filformatet. Det tilrådde filformatet stør opp om langtidsbevaring og gjenbruk over tid, medan det opphavlege filformatet kan vera lettare for nokre brukarar å undersøkja eller arbeida med på kort sikt.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Hugs
Text: Tilrådde filformat stør opp om langtidsbevaring. Dei er ikkje alltid obligatoriske krav for publisering.

### Tilrådde filformat

Her er nokre vanlege døme:

| Datatype | Tilrådde format |
| --- | --- |
| Tekst | TXT, PDF/A |
| Tabelldata | TSV, CSV |
| Bilete | TIFF, PNG, JPEG |
| Lyd | WAV, AIFF, FLAC |
| Video | MP4 |
| Markup | XML, HTML |
| Statistiske data | R, SPSS-syntaks, STATA-syntaks |
| Programkode | Python, MATLAB, rein tekst-kjeldekode |

Sjå [PAGE: file-formats/index | oversikta over filformat i DataverseNO] for den komplette lista og rettleiing.

### Treng du hjelp til å konvertera filer?

Rettleiing på korleis konvertera dokument, rekneark, bilete, lydfiler, videofiler og andre datatypar til tilrådde filformat finn du i [PAGE: file-formats/index | DataverseNO-filformatoversikta].

### Opphavlege og konverterte filformat

Ofte kan data leverast både i eit tilrådd filformat og i det opphavlege filformatet som det tilrådde formatet er laga frå.

Døme:

```text
[text]
experiment_01.csv
experiment_01.xlsx
```

I dette dømet er:

- experiment_01.csv det tilrådde formatet for langtidsbevaring.

- experiment_01.xlsx det opphavlege arbeidsformatet.

Å levera begge versjonane kan stø opp om både langtidsbevaring og gjenbruk på kort sikt.

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Hugs
Text: Dersom du lastar opp både eit tilrådd filformat og eit opphavleg filformat, bør filnamna vera identiske bortsett frå filendinga.

## Beskriv dataa dine

God dokumentasjon gjer data lettare å oppdaga, forstå og gjenbruka.

I DataverseNO blir datasett dokumenterte på to måtar som utfyller kvarandre:

- Ei **README-fil** som du lagar før du arkiverer datasettet.

- **Metadata** som du legg inn når du opprettar datasettet i DataverseNO.

Denne delen handlar om å førebu ei README-fil og annan dokumentasjon før arkivering. Informasjon om metadata finst i det andre steget i arkiveringsprosessen: [PAGE: deposit-your-data | Steg 2: Arkiver dataa dine].

### Det viktigaste steget: Lag ei README-fil

Ei **README-fil** er ein guide til datasettet ditt. Ho forklarar kva dataa inneheld, korleis dei blei laga, korleis filene er organiserte, og kva andre må vita for å kunna forstå og gjenbruka dei.

Det er obligatorisk å leggja ved ei README-fil før eit datasett kan publiserast i DataverseNO.

README-fila bør minst innehalda:

- Tittel på datasettet og kontaktinformasjon.

- Beskriving av metodar og datainnsamling.

- Oversikt over filer og mapper.

- Forklaringar av variablar, forkortingar, kodar og terminologi.

- Informasjon om gjenbruksvilkår og lisensiering.

Vi tilrår å bruka ein av DataverseNO-malane:

[RESOURCE BOX GRID]
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: DataverseNO README-filmal - generell
URL: https://doi.org/10.5281/zenodo.7453999
Open: new-tab
[RESOURCE BOX]
Style: primary
Icon: journal-code
Title: DataverseNO README-filmal - programkode
URL: https://doi.org/10.5281/zenodo.7454015
Open: new-tab

**Døme på README-filer:**

[RESOURCE BOX GRID]
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: Døme 1 (livsvitskap)
URL: https://doi.org/10.18710/S94YFT/J2GAMK
Open: new-tab
[RESOURCE BOX]
Style: primary
Icon: file-ruled
Title: Døme 2 (samfunnsvitskap)
URL: https://doi.org/10.18710/JWTJJB/O77MAT
Open: new-tab

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Hugs
Text: Ei godt skriven README-fil er ofte den viktigaste enkeltfaktoren for at andre skal kunna forstå og gjenbruka dataa dine.

### Annan dokumentasjon

For nokre datasett kan det vera nyttig å leggja ved annan dokumentasjon saman med README-fila og visa til denne dokumentasjonen i README-fila der det er relevant.

Her er nokre døme:

- Protokollar for datainnsamling.

- Analyseskript.

- Kodebøker.

- Spørjeundersøkingar eller intervjuguidar.

- Arbeidsflytar for prosessering.

- Laboratorieprosedyrar.

- Dokumentasjon av rettar og løyve.

Jo meir spesialisert datasettet ditt er, jo viktigare blir ofte slik dokumentasjon.

### Kvifor dokumentasjon er viktig

God dokumentasjon aukar sjansen for at dataa dine kan:

- oppdagast av andre forskarar.

- tolkast og gjenbrukast riktig.

- reproduserast og validerast.

- bevarast og forståast i framtida.

Dokumentasjon er derfor nyttig både for framtidige brukarar av dataa dine, for deg sjølv og for samarbeidspartnarane dine.

## Sjekk fil- og datasettstorleik

For å sikra smidig opplasting, kuratering og gjenbruk bør du merka deg desse tilrådingane:

- Ei enkeltfil bør helst ikkje vera større enn [REUSE: values/file-size-limit].

- Éi enkelt opplasting bør helst ikkje vera større enn [REUSE: values/upload-size-limit].

- Eit datasett bør helst ikkje vera større enn [REUSE: values/dataset-size-limit].

- Eit datasett bør helst ikkje innehalda meir enn [REUSE: values/file-number-limit].

### Større datasett

Dersom filene eller datasettet ditt er større enn desse tilrådingane, bør du kontakta [REUSE: links/contact-page | lokal brukarstøtte] før du arkiverer dataa dine. Det er ofte mogleg å handtere slike store datasett.

## Treng du hjelp?

Dersom du er usikker på korleis du bør førebu datasettet ditt, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte]. Vi hjelper gjerne.

## Klar til å gå vidare?

Dersom filene dine er organiserte, dokumenterte og klare til deling, er du klar for neste steg.

[BUTTON]
Style: primary
Title: Steg 2: Arkiver dataa dine
Icon: arrow-right-circle-fill
Target: deposit-your-data
