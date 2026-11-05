# Avancement — étape F de R1 v4, version 2 (rédacteur-développeur neuf, Claude Fable 5.1)

Consigne : `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-developpeur-gardes-analyses-r1-v4-v2.md` (`57b2f9d281c1dc0a…`, vérifiée par `sha256sum`).
Arbre : `/home/claude/controle-ia-travail`, `canal/conv-audit-n04`, `c82dafeb`. Deux redémarrages du conteneur (18:51 et 19:02 UTC) avant tout fichier écrit : reprise à zéro à 19:03 UTC.

## Fait (heure UTC, `date -u`)
- 19:03 — pièces lues et empreintes vérifiées : contre-lecture `39d1d035…` et couples `faafe414…` (compagnons OK), brouillon 1 `5d3ab56c…`, rapport v1 `879d2e93…`, listes fermées v1 `003e0a20…`, code v6/v7/v4 et leurs trois essais ; les trois empreintes des manifestes de la course v3 recalculées sur `runs/` du canal : `0587c398…`, `79f2a758…`, `91f711c6…` (égales à la consigne) ; seuls ces trois manifestes, sur 54, citent un des trois textes ou l'addendum (grep des octets).

## Plan (ordre)
1. Code v8 (principale : `constantes_v8`, `entrees_v5`, `lecture_v8`), v9 (par épisode : `constantes_v9`, `lecture_v9`), v5 (secondaire : `constantes_v5`, `entrees_v5`, `lecture_v5`) : K1, K2, K3.
2. Essais neufs `tests/test_analyse_principale_r1_r2_v8.py`, `tests/test_analyse_par_episode_v9.py`, `tests/test_analyse_blanche_noire_v5.py` ; une suite à la fois.
3. Listes fermées v2, différentiels hors renommage.
4. Brouillon 2 par scripts (couples C1–C15, puis substitutions exactes).
5. Rapport v2.

## Reste
- tout (début).
