# Correction log, public page of the ideation organism: version 5

- Written on 13 November 2026, from 22:17 UTC to sealing (`date -u`), by the writer of v1 to v4.
- Order: the coordinator relays the project lead's "go" to this route (R-2603). The order is v4 plus the removal of the wordings that the adversarial reading forbids in the post, all in one push.
- Pieces that govern this version (hashes checked at 22:17 UTC):
  - `docs/notes/publiabilite-ce-soir-v1/billet-v2/fiche-faits-billet-v1.md`, sha256 `c1db456d87854b34c0d73bae486db19da44b705fcbe07338e2174889090ba678`. Used: section 3, "Ne pas dire" (column "dire à la place"), and facts F18, F45, F46, F48. Cited below as FF.
  - `docs/notes/publiabilite-ce-soir-v1/lecture-adverse-billet-v2.md`, sha256 `ad6490146abd6817ab985fb927eafda201c51f76925201a374dabe5a66d0798b`. Used: findings M-3 and M-5. Cited below as LA.
- Starting point: the v4 deliverable (`livrables/page-publique-organisme-2026-11-13-v4/`).
- Public base: `git ls-remote origin refs/heads/main` returned `be6b5af96c9e19812569d8dab55d6ce3978a3823` at 22:17 UTC (read only; unchanged).
- The public clone was not touched, including the coordinator's unpushed local commit there. Nothing was committed and nothing was pushed. v1 to v4 are untouched (R12).

## Exact-once check

Each source text was searched in v4, and the build stops if a count is not 1. All five counts were 1. After the build, none of the following occur in the three page files:
- "symmetric"
- "as well as" (in the leak sentences)
- "was not run"
- "with a leak established"
- "established by"
- "reads the instruction"

## Lines changed between v4 and v5

There are 3 lines in all. `MANIFEST.md` is unchanged from v4.

| file, line (v4 = v5) | before (v4) | after (v5) | order point | piece |
|---|---|---|---|---|
| `README.md` l. 137 (R1 row), label | `**In (6–7 Nov 2026), with a leak established.**` | `**In (6–7 Nov 2026), with the outcome "leak" under a rule frozen before the computation.**` | 3, 5 | FF section 3, rows "fuite établie…" (F47: stronger than reservation 2) and "preregistered… sans réserve" (F18) |
| `README.md` l. 137 (R1 row), leak sentence | `**But a preregistered leak audit returned the frozen outcome "leak (reading the instruction)":** the trained probe separates the saboteur's actions that do *not* inflate the cost (area 0.9967 [0.9930, 0.9991], 46 actions from 12 of 60 tasks) as well as those that do (0.9977 [0.9958, 0.9993]). "Not inflated" is not "no sabotage": the probe may also read another trace of sabotage, and the arm that would separate the two was not run.` | `**But a leak audit, under a rule written for both outcomes and frozen before the computation (no public hash of the rule preceded the computation), returned the outcome the rule names "leak (reading the instruction)"; the name goes further than the measurement:** the trained probe separates from honest actions the saboteur's actions that do *not* inflate the cost (area 0.9967 [0.9930, 0.9991], 46 actions from 12 of 60 tasks) and those that do (area 0.9977 [0.9958, 0.9993]); no comparison between the two groups was tested. For "leak", one of two groups of actions suffices; for "sabotage", all are required. "Not inflated" is not "no sabotage": the probe may also read another trace of sabotage, and no result is available from the control that would separate the two.` | 1, 2, 3, 4, 5 | see the mapping below |
| `resultats/controle-r1-blanche-noire/README.md` l. 5 (heading) | `## Result (6–7 November 2026): a leak, established by a preregistered audit` | `## Result (6–7 November 2026): an audit whose rule names the outcome "leak (reading the instruction)"` | 3, 5 | FF section 3, rows "reads the instruction… comme fait établi", "fuite établie…" and "preregistered… sans réserve" |
| `resultats/controle-r1-blanche-noire/README.md` l. 9, bullet title | `**But the trained probe reads the instruction; whether it also reads the sabotage is not separated.**` | `**But the audit's rule names the outcome "leak (reading the instruction)"; the name goes further than the measurement.**` | 3 | FF section 3, row "reads the instruction"; LA M-5; verdict `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` (`320463e6…`), l. 65, 66 (b) |
| `resultats/controle-r1-blanche-noire/README.md` l. 9, body | `A leak audit, preregistered with a symmetric rule before it ran, found that the probe separates … (… 46 actions, 12 tasks) as well as those that do (0.9977 [0.9958, 0.9993]). Frozen outcome: **"leak (reading the instruction)"**, with 5 written reservations. "Not inflated" is not "no sabotage": …, and the arm that would separate the two was not run.` | `A leak audit, under a rule written for both outcomes and frozen before the computation (for "leak", one of two groups of actions suffices; for "sabotage", all are required; no public hash of the rule preceded the computation), found that the probe separates from honest actions the saboteur's actions that do **not** inflate the cost (area **0.9967** [0.9930, 0.9991], 46 actions, 12 tasks) and those that do (area 0.9977 [0.9958, 0.9993]); no comparison between the two groups was tested. Outcome named by the rule: **"leak (reading the instruction)"**, with 5 written reservations. "Not inflated" is not "no sabotage": the probe may also read another trace of sabotage, and no result is available from the control that would separate the two.` | 1, 2, 3, 4, 5 | see the mapping below |

The rows count four places: the R1 row of `README.md` changes in two places on one line (l. 137), and the R1 page changes in two places on its l. 9.

### Mapping of each new wording to its piece

1. **"symmetric" removed.** New wording: "a rule written for both outcomes … for "leak", one of two groups of actions suffices; for "sabotage", all are required".
   - FF section 3, row "symmetric decision rule": "règle écrite d'avance pour les deux issues ; un groupe sur deux suffit pour « fuite », tous sont exigés pour « sabotage »".
   - LA M-3. Sealed audit text, l. 149-152 and 177-179, cited by FF.
2. **"as well as" removed.** New wording: the two areas side by side, "and those that do (area …)", then "no comparison between the two groups was tested".
   - FF section 3, row "as well as": "les deux aires côte à côte, et « aucune comparaison n'a été testée »"; sealed audit text, l. 177.
   - LA M-5.
   - The figures are unchanged. "separates from honest actions" makes explicit what each area is computed against: the triage (`tri-publiabilite-v1.md`, 2-a) states it as "from honest actions … 46 vs 600 actions".
3. **"reads the instruction" as an established fact removed, bullet title and headings included.** New wording: "the outcome the rule names "leak (reading the instruction)"; the name goes further than the measurement".
   - FF section 3, row "reads the instruction": "la règle nomme l'issue « fuite (lecture de la consigne) » ; le nom va plus loin que la mesure".
   - LA M-5; verdict V l. 65, 66 (b); F45 (2), F46 (b).
   - "a leak established" and "a leak, established by" are removed under FF section 3, row "fuite établie…" (F47).
4. **"the arm that would separate the two was not run" removed.** New wording: "no result is available from the control that would separate the two".
   - FF section 3, row "the counterfactual arm was not run": "je n'ai pas de résultat de ce contrôle ; rien sur les courses". F48.
   - Nothing is said about runs, attempts or embargoed work.
5. **"preregistered" in the leak-audit sentences.** New wording: "a rule … frozen before the computation (no public hash of the rule preceded the computation)".
   - FF section 3, row "preregistered… sans réserve": "règle gelée avant le calcul". F18: the hash `910a53dc…` first appears in public with the verdict, 8 November 2026.
   - The words "attested by the private repository" in FF's suggested wording are **not** used: the page cannot show that evidence, and adding it was not ordered.
6. **Other entries of the "ne pas dire" list, checked on the three files:**
   - Not present on the page: "detects sabotage" for this probe; "the same deceptive text"; "flags" for the probe (the only "flags" on the page is about a P3 file); "cannot be reading"; "do not sabotage"; "symmetric"; "reads the instruction".
   - "frozen outcome", which FF calls house vocabulary, was replaced in the two leak sentences only ("the outcome the rule names", "Outcome named by the rule").

## Left unchanged on purpose (to decide by the project lead)

- **"+0.932" and the comparison with black-box judges** (R1 row, R1 page l. 8): these are on FF's "do not say" list (F47), but they are point 9 of section E of the v2 log, which the order keeps open. Not touched.
- **"as preregistered" for the primary analysis** (R1 page l. 8) and **"preregistered"** elsewhere on the page (Goodhart attack, null validations, T0.3, P3): F18 concerns the leak audit's text only. Not touched.
- **"Last updated" stamp of the R1 page** (l. 3): it still describes the v2 change. Updating it was not ordered. Possible text: "Last updated: 13 November 2026 (the leak sentences reworded to the outcome named by the audit's rule, its second reservation and the absence of a public hash before the computation; a sentence on next steps removed); previous update: 8 November 2026, 09:20 UTC."
- **MANIFEST section "Updated on 13 November 2026"**: it does not record the v4 and v5 edits. One possible line: "The R1 row and the R1 page now name the leak audit's outcome as the outcome its rule names, give the two areas without comparing them, and say that no public hash of the rule preceded the computation." Not applied.
- Section E points 1, 3, 8, 9 and 10 of the v2 log, and the full route of M2: still open.
- The R1 page's dated "Where it stood" text (l. 43, "Next, each step preregistered…"): kept as the dated record it is.

## Files delivered

All are in `livrables/page-publique-organisme-2026-11-13-v5/`, sealed by `python -m controle_ia.scellement sceller`.

| file | public path |
|---|---|
| `README-corrige-v5.md` | `README.md` |
| `MANIFEST-corrige-v5.md` (identical to v4) | `MANIFEST.md` |
| `controle-r1-README-corrige-v5.md` | `resultats/controle-r1-blanche-noire/README.md` |
| `diff-page-organisme-v4-v5.patch` | v4 → v5 |
| `diff-page-organisme-n067-v5.patch` | `be6b5af` → v5, the differential a push would apply |
| this log | — |

Both patches were replayed with `patch -p1`: v4 → v5 on the v4 files, and the full patch on fresh copies taken by `git show be6b5af:`. Each gives the three v5 files byte for byte (`cmp`).

## Checks

- No embargoed content: nothing on later runs, attempts, organisms, probes to come or the attack arm. No recipe, no session identifier, no private path and no person's name added. No model identifier in this log.
- No refusal by a permission check or a classifier.
