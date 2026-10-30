"""North Korea: no law text. Wikidata facts + UN Treaty Collection actions -> corpus.json (private)."""
import sys, json
sys.path.insert(0, r'~/Documents/lexifina/scripts/world-law')
import p3lib, p3_untc
STATE = "Democratic People's Republic of Korea"
act1, law1, src1 = p3lib.legal_system_act('Q423', 'North Korea (Democratic People\'s Republic of Korea)',
                                          extra_items=['Q707454', 'Q75048974', 'Q131446392', 'Q96749110', 'Q83221947', 'Q67174082'])
act2, law2, src2, n = p3_untc.treaties_act(STATE)
laws = dict(law1); laws.update(law2)
corpus = {
 'country': {'code': 'KP', 'name': "North Korea (Democratic People's Republic of Korea)", 'slug': 'north-korea', 'lang': 'en', 'tz': 'Asia/Pyongyang', 'future_branch': 'future',
   'publisher': {'name': 'Wikidata and the UN Treaty Collection (facts only)', 'email': 'facts@wikidata.invalid'},
   'default_in_force_rule': {'text': 'Not applicable: this record holds facts and treaty actions, not law text. Each treaty action is dated by the day it was taken.', 'source': 'https://treaties.un.org/'},
   'licence_note': 'Wikidata facts are CC0 1.0. Treaty actions are facts recorded by the UN Treaty Collection; no text is copied.'},
 'sources': [src1, src2],
 'laws': laws,
 'acts': [act1, act2],
 'applies': [],
 'decisions': [
  'No law text is published: the official portal (naenara.com.kp) answers this machine with HTTP 403 and was not read, the register lists no official online legislation, and the only full set of North Korean laws online is a volunteer repository that is not an official source.',
  'legal-system holds Wikidata facts (CC0). Facts with a day-precision date (inception of the state) are dated by that date; the rest are dated by the retrieval date, 2026-10-30, as the oldest version available. The constitution items (the 1948, 1955, 1972 and later constitutions) are listed only with the dates Wikidata records.',
  f'treaties holds {n} multilateral treaties from the UN Treaty Collection status pages (retrieved 2026-10-29) to which North Korea is a party or signatory; each action (signature, ratification, accession or succession) is dated by the action date. Coverage is limited to those selected status pages, not every treaty, and a withdrawal notice North Korea sent for the ICCPR (25 August 1997) is not shown as an action; see the UN Treaty Collection for that treaty.',
 ],
 'ai_use': ['none'],
}
# Wikidata legal-system act has first_law None: fine ("oldest version available").
json.dump(corpus, open(r'~/Documents/lexifina/scripts/north-korea-law/corpus.json', 'w', encoding='utf8', newline='\n'), ensure_ascii=False, indent=1)
print('ok', len(laws), [len(a['versions']) for a in corpus['acts']])
