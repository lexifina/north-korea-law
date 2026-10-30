# North Korea (Democratic People's Republic of Korea): law history in git

The law of North Korea (Democratic People's Republic of Korea) as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

No other official, reusable text of the Socialist Constitution or of any statute was found. So this repository holds only facts that are safe to publish: the legal-system facts Wikidata records, and the treaties North Korea has signed or joined.

The text of North Korean law is not in it; to read it, use the official sources.

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `legal-system/` | Legal system facts from Wikidata (form of government, institutions, languages, constitution items) | 2 | State inception 9 September 1948; facts as of 30 October 2026 |
| `treaties/` | Treaty actions of the DPRK: signature, ratification, accession (UN Treaty Collection) | 31 | Each action on its own date, 1973 to 2016 |
| `catalogue/` | 25 laws of the DPRK recorded by WIPO Lex: title, subject, date, link; no law text | 21 | Dated by the date WIPO Lex records for each law, 1950 to 2025 |
| `wipo-treaties/` | 46 treaty actions of the DPRK recorded by WIPO Lex (name, administering organisation, dates; no treaty text) | 37 | One per action date |

## Source

- **Wikidata** (https://www.wikidata.org/wiki/Q423), CC0 1.0, retrieved 30 October 2026.
- **WIPO Lex** (https://www.wipo.int/wipolex/en/members/profile/KP), CC BY 4.0, retrieved 30 October 2026. Facts only: law titles, subject, dates and links; treaty names, dates and administering organisation. No text of any law or treaty is copied.
- **UN Treaty Collection** (https://treaties.un.org/), status pages of selected multilateral treaties, retrieved 29 October 2026. Facts only: treaty, action, date and depositary; no treaty text is copied.

## Dates

- `legal-system`: the first version is dated **9 September 1948**, the inception date Wikidata records for the state; the second version is the Wikidata facts as retrieved on 30 October 2026 and was not enacted on that date.
- `catalogue` and `wipo-treaties`: each version is one date WIPO Lex records (a law's promulgation, entry into force, commencement or adoption date; a treaty action's instrument, entry-into-force or signature date).
- `treaties`: each version is the day a treaty action was taken, credited to that action (for example `untc-iv-4-1981-09-14-accession`).

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law (or, for facts, the retrieval) that made the change, with an e-mail address that cannot exist (`<law key>@wikidata.invalid`). The committer is always Lexifina.

## Limits

- No law text. Statutes, the constitution and the gazette are not in this record.
- Treaties come from a selected set of UN Treaty Collection status pages (human rights, refugees, terrorism, drugs, environment, law of the sea and others), not every treaty; some treaties are not deposited with the UN Secretary-General.
- North Korea's notification of withdrawal from the ICCPR (25 August 1997) is not shown as an action; the UN Secretary-General's position is that withdrawal is not possible, see the UN Treaty Collection page for the treaty.
- Wikidata facts are community-edited and are given as Wikidata holds them.
