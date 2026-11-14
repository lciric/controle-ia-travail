# Correction log, public page of the ideation organism, under N-067: version 3

- Written on 13 November 2026, from 20:43 UTC to sealing (`date -u`), by the writer of v1 and v2.
- Source of this version: `livrables/page-publique-organisme-2026-11-13-v2/verification-courte-page-v2.md`, sha256 `84b6bce570e868ddc3840886aa6583c0be9f0a0becee7dbde3025438774c723e`, read in full. It was filed at commit `b13ff07b` (R-2590). Its verdict: "poussable après corrections", no blocker.
- Starting point: the v2 files, which are identical to the v2 deliverable:
  - `README-corrige-v2.md` `73f0b053…`
  - `MANIFEST-corrige-v2.md` `a3dd9e79…`
  - `controle-r1-README-corrige-v2.md` `3acf0a9d…`
- Public base, unchanged: `origin/main` = `be6b5af96c9e19812569d8dab55d6ce3978a3823`, re-fetched with an explicit refspec at 20:43 UTC.
- Nothing was written in the public clone, nothing was committed and nothing was pushed. The v1 and v2 folders are untouched (R12).

## Files delivered

All are in `livrables/page-publique-organisme-2026-11-13-v3/`, each sealed with its `.sha256` companion by `python -m controle_ia.scellement sceller`.

| file | role | public path it replaces |
|---|---|---|
| `README-corrige-v3.md` | corrected page | `README.md` |
| `MANIFEST-corrige-v3.md` | corrected manifest | `MANIFEST.md` |
| `controle-r1-README-corrige-v3.md` | R1 result page, identical to v2 (no finding touched it) | `resultats/controle-r1-blanche-noire/README.md` |
| `diff-page-organisme-v2-v3.patch` | v2 → v3 differential (paths `a/`, `b/`) | — |
| `diff-page-organisme-n067-v3.patch` | full differential `be6b5af` → v3, the one a push would apply | — |
| this log | — | — |

Both patches were replayed with `patch -p1`: v2 → v3 on the v2 files, and base → v3 on copies of `be6b5af`. Each gives the three v3 files byte for byte (`cmp`).

## Finding by finding

| finding | what was done | text now on the page | evidence |
|---|---|---|---|
| **M1**, first couple (MANIFEST) | applied word for word | "the judge's null is described as what the system does, and the published work it assembles is cited." | verification, section 4, M1; README "Related work", item *The judge's null* |
| **M1**, second couple (MANIFEST) | applied word for word | "- No new run and no new file. New on the page: the fresh reader's verdict on T0.3 (10 November 2026), and figures already given on the result pages or read in the cited papers." | verification, section 4, M1 |
| **M1**, follow-on (MANIFEST; deviation, stated) | the manifest also quoted the A1-v4 sign as "no false promotion". After M4 it would have contradicted the page again, so it now reads "the A1-v4 row says that the sign "false promotions held at or near zero" is already published" | — | same reason as M1 (manifest contrary to the page) |
| **M2** (README, T0.3 row) | short route applied word for word: "Fresh-reader verdict (one reader, 10 November 2026; its text is not public, and the linked result page predates it): "confirmed with reservations"." The full route (a fourth file, `resultats/controle-simulation-defenses/README.md`) is **not** applied; the verification leaves the choice to the project lead (see "To decide" below) | as quoted | verification, section 4, M2; `resultats/controle-simulation-defenses/README.md` at `be6b5af`, l. 12 and 85; verdict T0.3, `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` (`bc53b746…`), l. 10-22 |
| **M3**, Ma et al. title (README) | applied word for word | "Ma et al., "Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space", arXiv:2610.07627v1, 2026, pp. 1, 4, 15" | title checked by me on p. 1 of `docs/sources/pdf/lecture-o4-v1/arxiv-2610.07627/2610.07627v1.pdf` (`pdftotext`) |
| **M3**, SSRN pages (README) | applied word for word | "SSRN 6569258, version dated April 2026, pp. 1, 4, 26, 28;" | `docs/sources/pdf/lecture-o4-v1/ssrn-6569258/provenance-v1.md`, l. 21-22 (title page dated "April, 2026"; byte identity with SSRN's PDF not verifiable) |
| **M4** (README, A1-v4 row) | applied word for word | "the sign of "resists", false promotions held at or near zero, is already published (zero false admissions under a frozen referee: Qu, Chen, Wang, p. 15; none of 10,716 candidates admitted: CONFIRM, p. 9)" | verification, section 4, M4; `resultats/attaque-goodhart-v2/README.md` at `be6b5af`, l. 17 and 30 (1 of 24 promoted under v9) |
| **m1** (scope of the opening sentence over the null) | no couple given; nothing changed. Read literally, nothing is claimed for the judge, which matches R-2587 (neither free nor new). Flagged here so that the project lead sees it in the differential | — | verification, section 5, m1 |
| **m2** (README, T0.3 row) | applied word for word | "by code extracted at the commit cited on the result page" | verification, section 5, m2 (commit `d73ac46` is on the result page) |
| **m3** (log only) | corrected here. (i) R1 page l. 38 ("The three texts will be made public with the result") is in the section "Sealed before the data", not in "Where it stood". It is a promise since kept (the texts are public), not a plan, and is left unchanged. Only l. 43 is inside the dated "Where it stood" text. (ii) The v2 log said both "eight items" and "seven items": the v2 "Related work" has one lead sentence followed by **eight** list items (seven principles plus the Co-Scientist item), unchanged in v3. (iii) The log is in English because the page is in English, as instructed for this writer | — | verification, section 5, m3 |
| **m4** (denominator of the null) | nothing to change on the page. The public sentence is true and weaker than the code: the denominator is the best of all null members (`orchestrator/pole/nul_v8.py` at `be6b5af`, l. 12-18 and 27-31). Already noted in the v2 log, section C | — | verification, section 5, m4 |

The verification records two B1 deviations that it judges harmless and that were not stated in the v2 log. I state them here: "writing any law of a closed grammar" became "writing its laws in a closed grammar", and the opening "What section 4 measures is narrower:" became "The instrument of section 4, as the public code builds it (…):".

Sentences changed from v2 to v3:
- README, 5: the Ma title, the SSRN version, the A1-v4 sign, the T0.3 verdict parenthesis, and the commit of the T0.3 row.
- MANIFEST, 3: two M1 couples and the M1 follow-on.
- R1 page: none.

No new number. The words "April 2026", "not public" and "predates" come from the pieces cited above.

## To decide by the project lead (not applied)

1. **M2, full route.** Update `resultats/controle-simulation-defenses/README.md` too, using the verification's couples (section 4, M2: the bullet "No fresh-reader verdict" and the bullet "A fresh-reader verdict, or any criterion…"), and its "Last updated" date. This removes the contradiction in the public tree instead of naming it. It is a fourth file, and it adds the verdict's figures (886 cells, byte-for-byte reproduction) to that page.
2. Items 1 to 10 of section E of the v2 log (`livrables/page-publique-organisme-2026-11-13-v2/journal-page-organisme-n067-v2.md`) remain open. They are unchanged by v3: the O4 "not found" clause, "cannot" in the title, "closes", the private repository, branch and file names, the "42 of the 48" sentence, the "+0.932" of the R1 row, and N-067 point 3 against the code.

## Content checks

- No embargoed content was added: nothing on the probes beyond what the R1 rows already state, nothing on the positive witness, the attack arm, TASTE or P3-bis.
- No recipe, no session identifier, no private path, and no person's name other than cited authors.
- No priority word was added.
- No refusal by a permission check or a classifier.
