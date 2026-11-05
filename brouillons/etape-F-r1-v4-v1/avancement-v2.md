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

## Reprise T2 (sous-agent neuf de la fille 7, 5 novembre 2026, 19:24 UTC ; arbre `/home/user/wt/canal`, tête `64236ae4`)
- 19:24 — consigne v2 revérifiée (`57b2f9d2…`, compagnon OK) ; contre-lecture et couples (compagnons OK) ; les trois empreintes des manifestes de la course v3 recalculées sur `runs/` du canal, égales à la consigne ; seuls ces trois manifestes (sur 54) citent un des textes ou l'addendum.
- 19:28 — deux arrêts « mémoire » (code 137) d'un interpréteur Python pendant qu'un autre sous-agent occupait 14 Go ; attente de mémoire libre avant chaque lancement.
- 19:34 — fait, J1 : code v8 (`constantes_v8`, `entrees_v5`, `lecture_v8`), v9 (`constantes_v9`, `lecture_v9`), secondaire v5 (`constantes_v5`, `entrees_v5`, `lecture_v5`) : K1 (gardes juste après la fiche, avant tout chargeur), K2 (liste close `PASSAGES_V3` + `COMMANDES_ADDENDUM`, arrêt `PassageHorsListe`, code de fin 2, tolérés écrits par nom), K3 (`lecture_v9.exiger_principale_sous_addendum`). Importations vérifiées (22, 33, 31 fichiers).
- 19:35 — J1 commis et poussé : `4b164694`.
- 19:42 — fait, essais neufs : `tests/test_analyse_principale_r1_r2_v8.py` (4 réussis, 5 s), `tests/test_analyse_par_episode_v9.py` (3 réussis, 8 s, après deux corrections d'essai : motif « K3 » et artefact K2 passé par la garde directe, car altérer `PASSAGES_V3` change l'empreinte des constantes), `tests/test_analyse_blanche_noire_v5.py` (4 réussis, 12 s) ; suites anciennes rejouées une à une en arrière-plan (verrou `/home/user/wt/.pytest.lock` tenu par l'autre sous-agent par moments : attentes longues).
- 19:45 — fait, J3 : `listes-fermees-generees-v2.md` par `generer-listes-fermees-v2.py` (même forme que la v1, 15 fichiers « (neuf) », constantes `0546b602…`, `e23108ec…`, `b8022ea4…`) ; onze différentiels v2 (bruts : lecture, constantes, entrées ; hors renommage : les trois lectures).
- 19:49 — fait, J4 : `appliquer-couples-v2.py` ; C1 à C15 appliqués dans l'ordre (`brouillon1-plus-couples-C1-C15-v2.md`, journal) ; 34 opérations de substitution (`couples-substitutions-code-v8-v9-v5-v2.json` : bloc des listes remplacé, 33 couples exacts dont S33 ajouté après une première passe, sortie régénérée avant tout commit) → `prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon2.md` (`465b5334…`) ; marqueurs : exactement `<<COMMIT_CODE>>` et `<<GO_LAZAR_SECOND_PASSAGE>>` ; `prereg.problemes` : les deux lignes attendues ; listes fermées vérifiées par le code lui-même (22, 33, 31).
