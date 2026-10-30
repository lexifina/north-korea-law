import sys
sys.path.insert(0, r'~/Documents/lexifina/scripts/world-law')
from p3lib import write_docs
rows = [('legal-system', 'Legal system facts from Wikidata (form of government, institutions, languages, constitution items)', 2, 'State inception 9 September 1948; facts as of 30 October 2026'),
        ('treaties', 'Treaty actions of the DPRK: signature, ratification, accession (UN Treaty Collection)', 31, 'Each action on its own date, 1973 to 2016')]
holds = """**Metadata only, no law text.** North Korea's official legal portal (naenara.com.kp) refuses automated access from our machine (HTTP 403 for robots.txt and the home page), and we do not work around that. No other official, reusable text of the Socialist Constitution or of any statute was found. So this repository holds only facts that are safe to publish: the legal-system facts Wikidata records, and the treaties North Korea has signed or joined.

The text of North Korean law is not in it; to read it, use the official sources."""
source = """- **Wikidata** (https://www.wikidata.org/wiki/Q423), CC0 1.0, retrieved 30 October 2026.
- **UN Treaty Collection** (https://treaties.un.org/), status pages of selected multilateral treaties, retrieved 29 October 2026. Facts only: treaty, action, date and depositary; no treaty text is copied."""
dates = """- `legal-system`: the first version is dated **9 September 1948**, the inception date Wikidata records for the state; the second version is the Wikidata facts as retrieved on 30 October 2026 and was not enacted on that date.
- `treaties`: each version is the day a treaty action was taken, credited to that action (for example `untc-iv-4-1981-09-14-accession`)."""
limits = """- No law text. Statutes, the constitution and the gazette are not in this record.
- Treaties come from a selected set of UN Treaty Collection status pages (human rights, refugees, terrorism, drugs, environment, law of the sea and others), not every treaty; some treaties are not deposited with the UN Secretary-General.
- North Korea's notification of withdrawal from the ICCPR (25 August 1997) is not shown as an action; the UN Secretary-General's position is that withdrawal is not possible, see the UN Treaty Collection page for the treaty.
- Wikidata facts are community-edited and are given as Wikidata holds them."""
lic = """No legal text is held in this repository.

The facts in `legal-system` come from Wikidata, released under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/).
The treaty actions in `treaties` are facts (treaty, action, date, depositary) taken from the UN Treaty Collection (https://treaties.un.org/); no treaty text or descriptive text is copied."""
write_docs(r'~/Documents/lexifina/scripts/north-korea-law', 'north-korea', 'KP', "North Korea (Democratic People's Republic of Korea)", rows, holds, source, dates, limits, lic, 'wikidata')
