---
title: 'Steg 5: Endra datasettet ditt'
file_path: docs/nn/deposit/modify-your-data.md
language: nn
nav_label: Endra datasettet ditt
description: Les korleis du kan oppdatera publiserte datasett i DataverseNO, korleis versjonering påverkar referansar, og når deaksessjonering kan vera relevant.
seo_title: Endra publiserte datasett i DataverseNO | Versjonering, DOI, referanse og deaksessjonering
seo_description: Les korleis du kan oppdatera eit publisert datasett i DataverseNO, korleis nye versjonar blir kuraterte, korleis versjonering påverkar DOI og referanse, og når deaksessjonering kan vurderast.
tags:
- deposit
- dataverseno
- versioning
- doi
- deaccessioning
- research-data
- curation
keywords:
- endra datasett i DataverseNO
- endre datasett i DataverseNO
- oppdatera publisert datasett
- oppdatere publisert datasett
- datasettversjonering
- dataset DOI
- dataset citation version
- deaksessjonering
- deaccessioning
- publiserte forskingsdata
- DataverseNO dataset update
audience:
- forskarar
- deponentar
- forskingsstøtte
- datakuratorar
primary_user_intent: Brukaren vil forstå korleis ein kan oppdatera eit publisert datasett i DataverseNO, korleis versjonering påverkar referanse og DOI, og kva som skjer dersom tilgang til eit publisert datasett må fjernast.
parent_page: Arkiveringsguide
status: Draft
last_reviewed: null
review_cycle: Annual
related_data_sources:
- data/links.yml
- data/terms.yml
canonical_url: https://info.dataverse.no/nn/deposit/modify-your-data/
social_image: null
---

# Steg 5: Endra datasettet ditt

Publisering av eit datasett er ikkje nødvendigvis siste steg i livsløpet til datasettet. Dersom det trengst, kan du oppdatera eit datasett etter publisering for å retta feil, forbetra dokumentasjon, leggja til filer eller ta inn ny informasjon.

DataverseNO brukar versjonering for å sikra at endringar kan sporast, samtidig som tidlegare versjonar av datasettet framleis er tilgjengelege.

Dette steget forklarar:

- [SECTION: kvifor-endra-eit-datasett | Kvifor du kan trenga å endra eit datasett].

- [SECTION: korleis-versjonering-fungerer | Korleis versjonering fungerer].

- [SECTION: kan-eit-publisert-datasett-slettast | Korleis deaksessjonering fungerer].

## Kvifor endra eit datasett?

Du kan ønskja å laga ein ny versjon av eit datasett for å:

- retta på metadata.

- forbetra dokumentasjon.

- oppdatera README-fila.

- leggja til nye datafiler.

- erstatta filer med forbetra versjonar.

- leggja til informasjon om relaterte publikasjonar.

- følgja opp råd frå brukarar eller samarbeidspartnarar.

Oppdatering av eit datasett gjer det mogleg å forbetra kvaliteten og nytteverdien, samtidig som den vitskaplege dokumentasjonen blir teken vare på.

## Korleis versjonering fungerer

For å gjera endringar i eit publisert datasett loggar du inn på DataverseNO, går til datasettet du vil oppdatera, og klikkar på _Edit Dataset_. Dersom du vil lasta opp ein ny versjon av ei fil, bør du først sletta den gamle.

Når det blir gjort endringar, skjer følgjande:

- Det blir oppretta ein ny utkastversjon av datasettet.

- Utkastet må sendast til kuratering.

- Ein kurator gjennomgår endringane.

- Den nye versjonen blir publisert.

For å fremja openheit, reproduserbarheit og effektiv kuratering tilrår vi at du **dokumenterer alle endringar frå førre versjonen tydeleg i README-fila**. Informasjonen bør helst leggjast inn i den avmerkte delen for versjonshistorikk i README-filmalen, under spørsmålet  «Is this an updated version of a dataset published on DataverseNO?».

[ADMONITION]
Style: primary
Icon: pencil-square
Title: Hugs
Text: Dokumenter endringane frå førre versjonen tydeleg i README-fila før du sender det oppdaterte datasettet til kuratering.

### Kva skjer etter at du sender inn ein ny versjon?

Nye versjonar følgjer den same kurateringsprosessen som nye datasett.

Som forklart i [PAGE: publish-your-data | **Steg 3: Kuratering og publisering**], gjennomgår kuratorar datasett som er sende inn, for å bidra til at dei framleis er godt dokumenterte, forståelege og gjenbrukbare. Når ein ny versjon av eit datasett blir gjennomgått, blir det lagt særleg vekt på endringane som er gjorde sidan førre versjonen.

Tidlegare versjonar er framleis tilgjengelege etter at den nye versjonen er publisert. Dette sikrar at brukarar alltid kan få tilgang til den nøyaktige versjonen av dataa som blei brukt i tidlegare forsking.

### Kva skjer med DOI og referanse?

DataverseNO brukar [REUSE: terms/version-control] for å spora alle endringar som blir gjorde i eit publisert datasett. Dette sikrar openheit og gjer det mogleg for brukarar å identifisera nøyaktig kva versjon av datasettet som blei brukt i ein bestemd studie.

[REUSE: terms/digital-object-identifier | DOI-en] til datasettet er den same når ein ny versjon blir publisert. Det sørgjer for stabil identifisering av datasettet gjennom heile livsløpet.

Endringar får versjonsnummer. Avhengig av kva type endringar det er snakk om, kan ein versjon publiserast anten som ein **hovudversjon** eller ein **underversjon**.

#### Hovudversjonar

Hovudversjonar blir vanlegvis brukte når datafiler blir lagde til, fjerna, erstatta eller endra på annan måte.

Døme:

```text
[text]
V1 -> V2
V2 -> V3
```

Endringar i hovudversjonar blir kjem til uttrykk i datasettreferansen.

Døme:

```text
[text]
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2026). Bird observations from Northern Norway, 2018-2024 (Version 1) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
blir til:
Hansen, L. M., Berg, S. E., & Nilsen, T. R. (2027). Bird observations from Northern Norway, 2018-2024 (Version 2) [Data set]. DataverseNO. https://doi.org/10.18710/ABCDE1
```

#### Underversjonar

Underversjonar blir vanlegvis brukte for mindre oppdateringar som ikkje påverkar dei underliggjande datafilene.

Døme er retting eller utviding av metadata, til dømes å leggja inn informasjon i feltet _Related Publication_.

Døme:

```text
[text]
V1 -> V1.1
V1.1 -> V1.2
```

Endringar i underversjonar blir spora av arkivet, men kjem vanlegvis ikkje til uttrykk i datasettreferansen. I slike tilfelle held referansen seg på hovudversjonsnivå.

Til dømes vil den tilrådde datasettreferansen framleis visa til V1 sjølv om den interne arkivversjonen blir endra frå V1 til V1.1.

## Kan eit publisert datasett slettast?

Publiserte datasett kan vanlegvis ikkje slettast.

Årsaka er at publiserte datasett har [REUSE: terms/persistent-identifier | permanente identifikatorar], til dømes [REUSE: terms/digital-object-identifier | DOI-ar], og er ein del av forskingsdokumentasjonen.

### Deaksessering

I **særlege tilfelle** kan tilgangen til filer i eit publisert datasett fjernast. Denne prosessen blir kalla **deaksessering**. Deaksessering kan berre vurderast når det finst ein tungtvegande grunn, til dømes dersom datasettet ikkje oppfyller kriteria for arkivering i DataverseNO, inneheld skadevare, bryt med opphavsrett, avtalefesta plikter, lovkrav eller forskingsetikk.

Når eit datasett blir deaksessert:

- Datafilene er ikkje lenger ope tilgjengelege.

- Metadataa for datasettet er framleis synlege.

- README-fila er framleis tilgjengeleg.

- DOI-en til datasettet er framleis ein del av forskingsdokumentasjonen.

Dersom du meiner at eit publisert datasett bør deaksesserast, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

[ADMONITION]
Style: primary
Icon: exclamation-circle-fill
Title: Publiserte datasett er ein del av forskingsdokumentasjonen
Text: Deaksessering er eit unntak og bør berre vurderast når det finst ein tungtvegande grunn til å fjerna open tilgang til filer i eit publisert datasett.

## Treng du hjelp?

Dersom du er usikker på om eit datasett bør oppdaterast, korleis versjonering påverkar referansar, eller om deaksessering kan vera aktuelt, kan du kontakta [REUSE: links/contact-page | lokal brukarstøtte].

## Du har kome til slutten av arkiveringsprosessen

Gratulerer! No veit du korleis du kan:

- førebu dataa dine.

- arkivera dataa dine.

- få dataa dine publiserte.

- referera til dataa dine.

- oppdatera datasettet ditt når det trengst.

Meir rettleiing finn du her:

- [PAGE: deposit-quick-guide | Hurtigguide og sjekkliste].

- [PAGE: about/index | Om DataverseNO].

- [PAGE: contact/index | Kontaktinformasjon].
