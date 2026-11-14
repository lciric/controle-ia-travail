# Correction log, public page of the ideation organism: version 6

- Written on 14 November 2026, from 07:23 UTC to sealing (`date -u`), by the writer of v1 to v5.
- **Order:** the coordinator relays the project lead's "go" (R-2654).
- **Pieces** (hashes checked at 07:23 UTC):
  - `docs/notes/publiabilite-note-organisme-v1/journal-note-organisme-v2.md`, sha256 `2fcbdb181f98ffe772a8ca5ed68bf594e6561cedebdd9fad818106a3126d1ab1`. Used: § 5, items 1 to 4, and § 1, row M1 (cited below as JN).
  - `docs/notes/publiabilite-note-organisme-v1/lecture-adverse-note-v1.md`, sha256 `948bf30eecbced714f7d303d79d285f0d021b585c929d0c7c66494d0a4cd9d36`. Used: M1 (cited below as LA).
  - The public code at `1a1a419`: `orchestrator/pole/nul_v8.py`, l. 12-18 (members) and l. 83-91 (uncovered classes); `orchestrator/pole/nul_v9.py`, l. 64 and 118 (`NON_COUVERT_V9`).
- **Public head:** `git ls-remote origin refs/heads/main` returned `1a1a419cd15a451fea8f5b8d31530f6ef02d336a` at 07:23 UTC (read only). At `1a1a419`, `README.md`, `MANIFEST.md` and `resultats/controle-r1-blanche-noire/README.md` are byte-identical to v5 (`ffc016ef…`, `0cf35fe0…`, `e1b7c220…`). The v5 → v6 diff and the `1a1a419` → v6 diff are therefore the same file.
- **Not done:** the public clone was not touched, nothing was committed and nothing was pushed. v1 to v5 are untouched (R12).

## Exact-once check

Each source text was searched in v5 before replacement; the build stops on any count other than 1. All four counts were 1.

## Lines changed between v5 and v6

All changes are in `README.md`: 3 lines, 4 changes. `MANIFEST.md` and the R1 page are unchanged.

| line (v5 = v6) | order point | before (v5) | after (v6) | piece |
|---|---|---|---|---|
| l. 15 ("Related work", item *The judge's null*) | 1 | `beats, through an e-process computed outside the agents, the best fitted combination of the already known laws, including the organism's own archive ("nothing beyond the archive").` | `beats, through an e-process computed outside the agents, the best-fitting member of its null: a fixed library plus members fitted on the known laws, including the organism's own archive ("nothing beyond the archive"); in v8, their pooled mixture and a tempered version of each survivor; v9 adds one-level piecewise recombinations. Neither null covers every combination; each lists what it leaves out.` | LA M1; the M1 sentence of the note as JN § 1 gives it, taken nearly word for word; `nul_v8.py` l. 12-18 (pooled mixture "ajuste_lineaire:archive"; each survivor tempered and tilted "ajuste_log:archive:<survivante>"); `nul_v9.py` l. 64, 118 |
| l. 18 (status paragraph) | 2 | `That attack found the judge's one declared gap; a new null (v9) that closes it has a written, counter-read proof` | `That attack tested one of the classes the v8 null declares uncovered (piecewise recombinations); a new null (v9), which covers one-level piecewise recombinations and declares its own uncovered classes, has a written, counter-read proof` | JN § 5, item 2; `nul_v8.py` l. 83-91 (uncovered classes: piecewise recombinations, products of more than two laws, compositions, other deformations, laws outside the archive); `nul_v9.py` l. 64, 118 |
| l. 140 (Goodhart attack row, first cell) | 3 | `two toy worlds where every promotion is false by construction (W1 inside the v8 null; W2: known law S1 on sub-population 0 and S2 on sub-population 1, a piecewise recombination that the v8 null declares uncovered)` | `two toy worlds (W1, inside the v8 null, where every promotion is false by construction; W2: known law S1 on sub-population 0 and S2 on sub-population 1, a piecewise recombination that the v8 null declares uncovered: under v8 a promoted law predicts the world and is false only under the novelty criterion, under v9 every promotion is false by construction)` | JN § 5, item 3 ("« false by construction » vaut pour W1, et pour W2 sous v9"); the same cell further on, and the public status page `resultats/attaque-goodhart-v2/README.md`, l. 63 |
| l. 140 (Goodhart attack row, second cell) | 4 | `not a false prediction, and it needs no optimisation against the judge — reading its description is enough.` | `not a false prediction, and it needs no optimisation against the judge.` | JN § 5, item 4; only the clause "reading its description is enough" is removed |

## Deviations, stated

- **Point 1.** JN's sentence was adapted to the page:
  - "beats through an e-process" keeps the page's existing "computed outside the agents".
  - "known laws" carries the page's existing "including the organism's own archive ("nothing beyond the archive")".
  - "Neither covers" becomes "Neither null covers".
  - JN's note on this sentence still holds: it simplifies the null (the daughters' null and the archive null are not named), and the orchestrator author's confirmation is still missing (O4 note, § 4, condition a).
- **Point 3.** JN proposed "… where every promotion is false by construction under the judge being tested (W2 under v8: false only under the novelty criterion)". I used a split by world instead, because it says the same thing without "under the judge being tested", which a reader could take as covering W2 under v8. This is a deviation in wording, not in substance.
- **Point 2** also settles the wording "closes" (point 3 of section E of the v2 log), in the form the order gives.

## Left as they are (still open)

- The MANIFEST dated section does not record the edits of v4, v5 or v6.
- The R1 page's "Last updated" stamp still describes v2.
- Section E points 1, 8, 9 and 10, and the full route of M2.

## Files delivered

All are in `livrables/page-publique-organisme-2026-11-14-v6/` and sealed by `python -m controle_ia.scellement sceller`.

| file | public path |
|---|---|
| `README-corrige-v6.md` | `README.md` |
| `MANIFEST-corrige-v6.md` (identical to v5) | `MANIFEST.md` |
| `controle-r1-README-corrige-v6.md` (identical to v5) | `resultats/controle-r1-blanche-noire/README.md` |
| `diff-page-organisme-v5-v6.patch` | v5 → v6 |
| `diff-page-organisme-1a1a419-v6.patch` | `1a1a419` → v6, the differential a push would apply (same bytes as the previous file) |
| this log | — |

The full patch was replayed with `patch -p1` on fresh copies from `git show 1a1a419:` and gives the three v6 files byte for byte (`cmp`).

## Checks

- No embargoed content was added.
- No recipe was added: the change at point 4 removes one.
- No session identifier, private path, person's name or model identifier was added.
- No refusal by a permission check or a classifier.
