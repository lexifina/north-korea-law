# How this repository was made (North Korea (Democratic People's Republic of Korea))

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Wikidata | <https://www.wikidata.org/wiki/Q423> | 2026-10-30 | CC0 1.0 |
| UN Treaty Collection (MTDSG status pages) | <https://treaties.un.org/> | 2026-10-29 | Facts only (treaty action, date, depositary); no text copied |
| WIPO Lex member profile | <https://www.wipo.int/wipolex/en/members/profile/KP> | 2026-10-30 | WIPO content: CC BY 4.0 (https://www.wipo.int/web/terms-of-use); only facts copied |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `legal-system` | North Korea (Democratic People's Republic of Korea): legal system facts (Wikidata) | 2 | 1948-09-09 to 2026-10-30 |
| `treaties` | Treaty actions of Democratic People's Republic of Korea (UN Treaty Collection) | 31 | 1973-05-19 to 2016-12-06 |
| `catalogue` | Catalogue of laws of North Korea (Democratic People's Republic of Korea) recorded by WIPO Lex (title, date, link only; no law text) | 21 | 1950-03-03 to 2025-11-01 |
| `wipo-treaties` | Treaty actions of North Korea (Democratic People's Republic of Korea) recorded by WIPO Lex (facts only; no treaty text) | 37 | 1957-08-27 to 2024-11-22 |

The build made 106 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 102 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 3 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 107 laws in the record.
- 194 tags.

## Dates

Each commit is dated at noon (Asia/Pyongyang) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applicable: this record holds facts and treaty actions, not law text. Each treaty action is dated by the day it was taken. https://treaties.un.org/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `e0702164758e9f42b100021adf6df13a722777ca900895ef969cc70ca853ed1a` (352357 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- No law text is published.
- legal-system holds Wikidata facts (CC0). Facts with a day-precision date (inception of the state) are dated by that date; the rest are dated by the retrieval date, 2026-10-30, as the oldest version available. The constitution items (the 1948, 1955, 1972 and later constitutions) are listed only with the dates Wikidata records.
- treaties holds 31 multilateral treaties from the UN Treaty Collection status pages (retrieved 2026-10-29) to which North Korea is a party or signatory; each action (signature, ratification, accession or succession) is dated by the action date. Coverage is limited to those selected status pages, not every treaty, and a withdrawal notice North Korea sent for the ICCPR (25 August 1997) is not shown as an action; see the UN Treaty Collection for that treaty.
- WIPO Lex: 25 laws from the member profile dated by the date WIPO Lex records (promulgation, entry into force, commencement, adoption, in that order); 0 laws with no recorded date are left out. Treaty actions: 46. Titles, dates and links only; no text. WIPO Lex gives some laws only 'January 1' of a year, a placeholder rather than a known date.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
