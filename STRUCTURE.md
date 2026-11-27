# Structure

| Folder | What it holds |
| --- | --- |
| `헌법/` | 조선민주주의인민공화국 사회주의헌법 (the Socialist Constitution); `제001조.md` is 제1조, `서문.md` the preamble |
| `당규/<이름>/` | 조선로동당 규약 and 당의 유일적령도체계확립의 10대원칙, which the source files with the Constitution |
| `법/<분야>/<법명>/` | Every other law, by the source's 19 sectors (분야), e.g. `법/형·민사부문/형법/`, `법/계획·로동·재산관리부문/로동법/`, `법/외교·대외경제부문/외국인투자법/` |
| `법/현행목록외/<법명>/` | Laws the source prints only in older editions (not in its current list), so with no sector |

Each law folder holds one file per article (`제001조.md` is 제1조; `부칙-제001조.md` an article of a 부칙), `서문.md`
for a preamble, `장.md` with the chapter (장) headings, and `README.md` with the source's adoption and amendment
record. No folder holds more than 1,000 entries. Folder and file names are in Korean as the source writes them, with
spaces turned into `-`.

## Source

The Ministry of Unification (Republic of Korea) North Korea Information Portal, 북한법령
(<https://nkinfo.unikorea.go.kr/NKLaw>), which prints each law in several editions (2004, 2008, 2010, 2017, 2019,
2020, 2022, 2024, 2026), each with the adoption and amendment record of the text it prints. Every version is tagged
`Source-status: secondary copy (...)`: North Korea publishes no official legislation online that can be read, and
North Korean hosts are not accessed.

## Dates

Each version is one commit, dated 12:00 Asia/Pyongyang on the day of the decision that adopted or last amended the
text (최고인민회의 or 최고인민회의 상임위원회 정령/결정), the last entry of the edition's own record; its `In-force:`
trailer repeats the day, and `In-force-basis: adoption-decree (as recorded by the Ministry of Unification North Korea
Information Portal)` says where it comes from. There is no separate gazette. For a two-day session of the Supreme
People's Assembly, the session's closing day. Two editions with the same day: the later edition's text, once. An
edition with no record, or older than a version already committed: held. Versions before 1970 are dated 1 January
1970 (git cannot store earlier dates), with the real day in the `In-force:` trailer. No date in this repository is
the day we downloaded anything.

Only the editions the portal prints are here, so a law's history starts at its oldest printed edition, not at its
adoption; each README lists every date of the record.
