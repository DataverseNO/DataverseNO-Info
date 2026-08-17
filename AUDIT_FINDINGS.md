# info.dataverse.no — full spec-vs-implementation audit

Utført 2026-08-17 med 7 parallelle agenter, hver tildelt et sammenhengende
kapittelsett fra `technical-architecture-and-implementation-standard.docx`
(§1-17 + vedlegg A-D), som uavhengig sjekket spec-tekst opp mot faktisk kode,
innhold og bygget nettsted — ikke mot planen eller `PENDING_ITEMS.md`s egne
påstander. Bakgrunn: en tidligere økt markerte §9 (innholdskomponenter) som
"ferdig" uten at noe faktisk gjengav riktig; denne revisjonen fant flere
tilfeller av samme mønster.

Status-koder: **IMPLEMENTERT** / **DELVIS** / **MANGLER** / **UTSATT (bevisst)**
/ **IKKE VERIFISERBART HER** (prosess/organisasjon, ikke kode).

---

## KRITISK — bryter funksjonalitet i produksjon i dag

1. **EOF-bug i `hooks/content_blocks.py`** (denne øktens egen kode).
   `_FIELD_LINE`-regexen krever at hvert felt slutter med `\n`. MkDocs
   strippar den siste linjeskiftet fra sidekilden før `on_page_markdown`
   kjører, så når et `[BUTTON]`/`[NAVIGATION CARD]`/`[RESOURCE BOX]`-blokks
   siste felt også er filens siste linje, blir feltet stille droppet.
   Resultat: knappen renders som permanent deaktivert/pending, OG rå
   kildetekst som `Target: contact/index` lekker som synlig tekst på siden.
   Bekreftet i det bygde nettstedet på **forsiden, About-siden, og 3 av 5
   Deposit-steg** — begge språk. Dette er det samme "ser ferdig ut, er det
   ikke"-mønsteret revisjonen skulle fange, og det unnslapp valideringen
   denne økten selv skrev.
   → Fiks: gjør avsluttende `\n` valgfri i `_FIELD_LINE`, eller
   `markdown.rstrip("\n") + "\n"` før prosessering.

2. **People-siden har ingen fungerende søk/filter.** `people.css` og
   `people-filter.js` er uendrede stubbe-filer arvet direkte fra
   migreringspakken (bekreftet byte-for-byte identiske), begge eksplisitt
   merket "skal ferdigstilles under AI-assistert migrering" — altså under
   dette prosjektet. Den faktiske rendreren (`generated_components.py`)
   bruker helt andre klassenavn (`person-card`, `people-filter`) enn det
   stubbene forventer (`data-people-page`, `data-institution-filter`,
   `data-role-filter`). Institusjonsfilter og rollefilter finnes ikke i
   det hele tatt. Søkefeltet står der, men gjør ingenting.
   → Motparten på Contact-siden (`contact.css`/`contact-filter.js`) er
   korrekt koblet og fungerer — bra referanseimplementasjon å kopiere fra.

3. **Footer, norsk nynorsk: feil lenketekst.** Spec §8.13 krever
   "Lokal brukarstøtte", faktisk tekst er "Lokale støttetenester"
   (`overrides/partials/footer.html`).

4. **Sticky navigation-faner er ikke aktivert.** `navigation.tabs.sticky`
   mangler i `mkdocs.yml` (kun `navigation.tabs` er satt), til tross for at
   `overrides/partials/header.html` allerede har sticky-bevisst logikk som
   aldri utløses.

5. **Dark mode er ikke tilgjengelig for brukere**, selv om CSS for det
   finnes. `mkdocs.yml` deklarerer bare ett palette-scheme
   (`scheme: default`), ingen `scheme: slate`, ingen `toggle:`-konfig.
   Ingen synlig knapp for å bytte modus. `dataverseno.css` har et helt sett
   `[data-md-color-scheme="slate"]`-regler for header/footer som aldri
   nås i produksjon.

6. **Footer-tekst har for lav kontrast i lys modus.** CC0/sitat-teksten i
   footer (§8.12, akkurat den lovpålagte lisensteksten) har kontrast 3.9:1
   mot krav om 4.5:1 for liten skrift — gjelder alle sider. (Mørk modus,
   når/hvis den blir tilgjengelig, består fint på 14.9:1.)

7. **"NONE" lekker som synlig tekst** på forsiden/About-siden — et
   navigasjonskort har `Description: NONE` i kildeinnholdet (migrerings-
   placeholder), og rendereren behandler det som ekte tekst i stedet for
   "ingen beskrivelse".

---

## HØY — samme mønster som utløste revisjonen: ting er "koblet til" men aldri validert

8. **`data/tags.yml` er lastet inn men aldri validert.** 112 sider bruker
   `tags:` i front matter, ingen script sjekker dem mot den kontrollerte
   vokabularen. En stavefeil i en tag ville bygge og deploye helt stille.

9. **`[SECTION: ...]`-ankere valideres aldri.** `content_blocks.py` gjør
   dem om til `<a href="#anker">` uten å sjekke at et heading med den
   ID-en faktisk finnes på målsiden — en foreldet/feilstavet anker gir en
   stille død lenke.

10. **Ingen dedikert validering av header/footer/glossary-lenker.** Alt
    hviler på manuelle "Status: ferdig"-påstander i `PENDING_ITEMS.md`,
    ikke en kjørende sjekk — nøyaktig mønsteret som lot §9 gli gjennom.

11. **Institusjonslogoer vises ikke på Contact-siden.** `_partner_card()`
    leser aldri `partner["logo"]`, så partnerkortene på Contact-siden har
    ingen logo (kun på About-sidens egen logo-grid, som er en annen
    komponent).

12. **`[REUSE: terms/...]` lenker aldri til ordlisten**, selv om hvert
    ordlisteoppslag har en klar, stabil anker-ID (`id="term-{id}"`) klar
    til bruk. Render gir bare ren tekst.

---

## MEDIUM

13. **`site_url` i `mkdocs.yml` stemmer ikke med faktisk deploy-URL.**
    Satt til `https://info.dataverse.no`, men ingen `CNAME`-fil finnes, og
    README/CONTRIBUTING peker fortsatt til GitHub Pages-standardadressen
    (`dataverseno.github.io/...`). Kanonisk URL/sitemap/SEO-metadata blir
    feil helt til `CNAME` + DNS er på plass.
14. **`LICENSE`-fil mangler** i repo-roten, til tross for at spec§3.1s
    anbefalte struktur eksplisitt lister den.
15. **`docs/assets/documents/{en,nn}` mangler** (ingen nedlastinger
    referert ennå, så ikke et aktivt brudd i dag).
16. **Open Graph-metadata mangler**, og — i motsetning til
    Matomo-analytics-utsettelsen som er tydelig dokumentert — er dette
    ikke nevnt noe sted som en bevisst beslutning.
17. **Søkeindeksen er kun engelsk** (`mkdocs.yml` har `lang: [en]`), selv
    om nettstedet er tospråklig — nynorsk-sider indekseres med engelsk
    stemming/stoppord.
18. **Ikonfilnavn stemmer ikke med spec-teksten** (`dataverseno-icon.svg`
    vs. spec sin `dataverse-icon.svg`) — fungerer, men avviker tekstlig.

---

## LAV / kosmetisk

19. Duplikat YAML-nøkkel i `data/terms.yml` (samme innhold begge steder,
    ufarlig, men bør ryddes).
20. `--strict`-avviket i CI (26 kjente advarsler, bevisst ikke blokkerende)
    er en fornuftig og korrekt vurdering, men står bare i den interne
    build-loggen — ikke i `PENDING_ITEMS.md` eller noe spec-synlig sted en
    fremtidig vedlikeholder ville finne.
21. `canonical_url`-feltet i front matter blir aldri lest av noe (Material
    løser kanonisk URL riktig uansett via en annen mekanisme) — dødt felt,
    kan forvirre redaktører.

## Prosess/styring — ikke kode, ingen handling mulig herfra

- §17.2 styringsroller (Content owners / Editors / Technical maintainers /
  Repository management) er ikke dokumentert noe sted i repoet — kun i
  spec-dokumentet.
- §14/16 "valider før commit" er implementert som CI (etter push), ikke
  som pre-commit-hook — en mild "should" i spec, ikke et hardt krav.
- §1, §17.3, §17.4: målsettinger/prinsipper uten egen sjekkbar overflate;
  vurdert indirekte via resten av revisjonen.

---

## Ting som faktisk er solid implementert (ingen handling nødvendig)

People-data-pipelinen (TSV → generering → validering → CI) er nøyaktig
implementert ned til minste detalj, inkludert den historisk risikable
`search_aliases`-genereringen og den kontrollerte rollevokabularen.
Reusable links/values/terms-oppløsning, footer-tekstens EN/NN-ordlyd
(§8.12, verifisert byte-for-byte), directory-struktur, editorial/generert/
derivert data-skillet, glossary-generering, deployment-pipelinen (§17.1),
og det aller meste av §9-komponentene (bortsett fra EOF-bugen over) er alle
korrekt og nøyaktig som spesifisert.
