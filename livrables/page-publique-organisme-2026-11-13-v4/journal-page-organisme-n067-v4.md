# Correction log, public page of the ideation organism, under N-067: version 4

- Written on 13 November 2026, from 21:11 UTC to sealing (`date -u`), by the writer of v1 to v3.
- Order: the coordinator relays the project lead's "go" to publish tonight and to apply, in the same push, points 2, 4, 5, 6 and 7 of section E of the v2 log (`livrables/page-publique-organisme-2026-11-13-v2/journal-page-organisme-n067-v2.md`). Point 4 takes the variant given in that log's note: the commit is kept.
- Not applied, still open: point 1 (the "not found" clause on O4), point 3 ("closes"), points 8, 9 and 10, and the full route of M2.
- Starting point: the v3 deliverable (`livrables/page-publique-organisme-2026-11-13-v3/`). All six companions were checked OK at 21:11 UTC.
- Public base: `git ls-remote origin refs/heads/main` returned `be6b5af96c9e19812569d8dab55d6ce3978a3823` at 21:11 UTC (read only; unchanged).
  - Remote: `https://github.com/lciric/ideation-organism`.
  - Local clone: `/home/user/lciric/ideation-organism`. It was not modified; its local `main` is still `6510199`.
- Nothing committed, nothing pushed. v1 to v3 untouched (R12).

## Exact-once check

Each source text was searched in v3 before replacement, and the build stops if a count is not 1. Every count was 1, so nothing was improvised. After the build, these strings no longer occur in any of the three page files:
- `controle-ia-travail`
- `canal/conv-audit-n04`
- `lecture-t05-graines-neuves-v1.json`
- "copies the two archive"

## Lines changed between v3 and v4

| file, line (v3 = v4 numbering) | section E point | before (v3) | after (v4) |
|---|---|---|---|
| `README.md`, l. 1 | 2 | `# Ideation organism — an automated research pole that cannot grade its own homework` | `# Ideation organism — an automated research pole built so that no agent grades its own homework` |
| `README.md`, l. 134 (fresh-seed reading row) | 6 | `the output is sealed in the private working repository (`lecture-t05-graines-neuves-v1.json`, sha256 `07bc2aea…`` | `the output is sealed in the private working repository (sha256 `07bc2aea…`` (hash kept) |
| `README.md`, l. 140 (Goodhart attack row) | 7 | `**42 of the 48 are, byte for byte, the world's own law** (the proposer copies the two archive laws per sub-population): a breach of the novelty criterion "nothing beyond the archive", not a false prediction,` | `**42 of the 48 reproduce the world's own law exactly**: a breach of the novelty criterion "nothing beyond the archive", not a false prediction,` |
| `README.md`, l. 219 (section 8) | 4, variant | `The tree is an exact extract of the private working repository `controle-ia-travail` at commit `91a3c7f8` (1 November 2026);` | `The tree is an exact extract of a private working repository at commit `91a3c7f8` (1 November 2026);` (commit kept) |
| `MANIFEST.md`, l. 3 | 5 | `Extract of the private working repository `controle-ia-travail` (branch `canal/conv-audit-n04`, commit `91a3c7f8`, 1 November 2026).` | `Extract of a private working repository (commit `91a3c7f8`, 1 November 2026).` |

These are 5 lines in all: 4 in `README.md` and 1 in `MANIFEST.md`. `resultats/controle-r1-blanche-noire/README.md` is unchanged from v3.

Each "after" text above is the couple from section E of the v2 log, used as is. The one exception is point 4, where the form given by the coordinator is used, word for word. No new number and no new claim.

## Files delivered

All are in `livrables/page-publique-organisme-2026-11-13-v4/`, sealed by `python -m controle_ia.scellement sceller`.

| file | public path |
|---|---|
| `README-corrige-v4.md` | `README.md` |
| `MANIFEST-corrige-v4.md` | `MANIFEST.md` |
| `controle-r1-README-corrige-v4.md` (identical to v3) | `resultats/controle-r1-blanche-noire/README.md` |
| `diff-page-organisme-v3-v4.patch` | v3 → v4 |
| `diff-page-organisme-n067-v4.patch` | `be6b5af` → v4, the differential a push would apply |
| this log | — |

Both patches were replayed with `patch -p1`: v3 → v4 on the v3 files, and the full patch on fresh copies taken by `git show be6b5af:`. Each gives the three v4 files byte for byte (`cmp`).

## Note for the push

The MANIFEST section "Updated on 13 November 2026" (added in v2 and v3) does not list the five edits of v4: the title, the provenance wording, the private names removed, and the description of the promoted laws shortened. If the project lead wants the manifest to record them, that is one more line, not applied here because it was not ordered.

## Checks

- No refusal by a permission check or a classifier.
- No embargoed content, no recipe, no session identifier, no private path, and no person's name added.
