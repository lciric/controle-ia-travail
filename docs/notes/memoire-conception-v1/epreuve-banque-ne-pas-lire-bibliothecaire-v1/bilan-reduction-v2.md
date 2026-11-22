# Bilan de la réduction et des moitiés (v2)

- Règle : `epreuve-bibliothecaire-v2.md`, § 2, « Réduction et moitiés (v2) » ; script `tirage-v2.py` ; numpy 2.5.3.
- Entrée : `jeu-final-v1.jsonl`, sha256 `1133788756dd8343489cea700fb2083cb797231004a55b51e0b6b6ea62c82211`.
- Graines : réduction `SeedSequence([2026112202, k])`, moitiés `SeedSequence([2026112203, k])`, k = rang du type (0 à 5).

| Type | Concordantes | Gardées (cible) | Écartées | mise_au_point | reserve |
|---|---|---|---|---|---|
| paraphrase | 35 | 30 (30) | 5 | 15 | 15 |
| confusion | 12 | 10 (10) | 2 | 5 | 5 |
| detail | 12 | 10 (10) | 2 | 5 | 5 |
| sans_reponse | 24 | 20 (20) | 4 | 10 | 10 |
| hors_perimetre | 12 | 10 (10) | 2 | 5 | 5 |
| erratum | 14 | 10 (10) | 4 | 5 | 5 |
| total | 109 | 90 (90) | 19 | 45 | 45 |

- Sorties : `jeu-epreuve-v2.jsonl` sha256 `97ac326afd3132bd0a516a8b51fedbcb293c8e01447864d4652b64fd9d916705` ; `ecartees-v2.jsonl` sha256 `441cdad364ca7be5a461d83a86d8e357fe4f379d779f1d24bf8412382e3ef775`.
- Chaque type atteint exactement sa cible (vérifié par assertion).
