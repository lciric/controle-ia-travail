# Code de P3-bis sous la règle (a') — différence appariée et 800 directions — rapport du développeur, v1

(BROUILLON EN COURS D'ÉCRITURE — rapport écrit au fil de l'eau ; la version scellée remplacera ce brouillon.)

Écrit à partir du 2026-11-11 à 10:56 UTC (heures relevées par `date -u`) par un **développeur neuf** (Claude Opus 5.5,
`claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-code-p3bis-regle-a-v1.md`
(`39300056eab009d8999e74fcfb5ca2967c8cfac66602a9611e81607fcea299d4`, vérifiée par `sha256sum -c` de son compagnon avant
lecture, 10:33 UTC). Je n'ai écrit ni P3-bis, ni son code, ni sa chaîne, ni T0.7, ni leurs contre-lectures ; je n'ai ouvert
aucune sortie de P3-bis, de T0.6, de 7a ni de 7b, rien sous `docs/notes/bras-attaque/`.

## 1. Où naît le plancher dans la chaîne de P3-bis, et comment obtenir 800 directions dont les 200 premières sont celles de P3

Le run de P3-bis est `premier_test_ia.run_v2`, qui appelle **tel quel** `run._executer_apres_manifeste` (`run_v2.py`
l. 106-107) : le plancher naît donc exactement comme dans P3, au commit de base `614fd5da` (fichiers inchangés depuis P3,
mêmes blobs qu'à C7) :

| étape | où (au commit `614fd5da`) | ce qui s'y fait |
|---|---|---|
| graine | `run.py` l. 135-140 (`cles_des_graines`, clé `plancher/<concept>` l. 138) ; `manifeste.py` l. 33-48 | une graine par clé, dérivée du **nom** de la clé (`cle_de_tache` = sha256 du nom, `spawn_key`) et de l'entropie citée : la graine de `plancher/tromperie` ne dépend ni des autres clés ni de `n_plancher` |
| nombre | `run.py` l. 443-444 : `plancher_de(principale, seq[concept], idx_e, config["n_plancher"], graine_entiere(g[f"plancher/{concept}"]))` | `n_plancher` est **une clé de la configuration** (`CLES_P3`, l. 72), sans contrôle de valeur dans `exiger_config_p3` ; P3 : 200 |
| tirage | `entrainement.py` l. 117-120 → `sondes/evaluation.py` l. 66-82 (`plancher_apparie`) | covariance et moyenne des jetons d'entraînement de la principale, Cholesky, puis `rng = default_rng(graine)` (l. 76) et, **l'une après l'autre**, `w = L @ rng.standard_normal(d)` (l. 79), `q = L @ rng.standard_normal(d)` pour l'attention seulement (l. 80), nom `f"{nom}-plancher-{k}"` (l. 81), b = −w·μ |
| figement | `run.py` l. 455-479 | sondes figées = 30 sondes + planchers des deux concepts ; `meta["planchers"]` (l. 458) ; fichier complet et léger scellés ; `sondes-figees.json` liste chaque sonde et son empreinte |
| notation | `run.py` l. 482 (`Notation(sondes, appareil)`), l. 280 (`notation.noter(seg)`) ; `notation.py` l. 35-49 et 81-85 | **notation matricielle en ligne, sur la carte** (mode réel) : toutes les sondes linéaires d'une couche, directions de plancher comprises, en un produit `A @ W + b` (l. 83), puis maximum ou attention ; garde d'identité contre la boucle du harnais (`score_action`) sur la première action notable de chaque lot, **toutes sondes** (l. 287, `notation.exiger_identite` l. 144-160) |
| stockage | `run.py` l. 313-329 et 492-496 | `scores-p3.npz` : une colonne par sonde et par direction (`noms_sondes`) |
| lecture | `lecture.py` l. 231-232 et 256-260 | la lecture de P3 prend **toutes** les directions dont le nom commence par `<principale>-plancher-` |

**800 directions dont les 200 premières sont celles de P3** : il suffit de **`n_plancher` = 800 dans la configuration de
P3-bis**, rien d'autre. Sous la graine de P3 (même entropie, même clé `plancher/tromperie`), `plancher_apparie` consomme le
générateur dans le même ordre pour k = 0 à 199 qu'avec 200 directions : les 200 premières directions (w, q pour
l'attention, b, et leur nom) sont **celles de P3** dès que la covariance et la moyenne réextraites sont identiques — ce
qu'éprouve justement PB-9 (empreintes des 30 sondes et des directions, processeur EPYC 7513 et 64 fils d'OpenBLAS, comme
à la régénération identique, R-679). Les directions 200 à 799 sont neuves, sans référence dans P3. Chaque concept a son
propre générateur : le plancher d'enjeux garde lui aussi ses 200 premières. Essai versé : préfixe exact, maximum et
attention, sur une covariance jouet (`tests/test_premier_test_ia_lecture_p3bis_v2.py`).

**Conséquence non écrite au brouillon 12** : la lecture de P3, inchangée (R12), lira alors ses dix jeux, le placebo, T1,
T4 et l'audit R4 **sur les 800 directions** (`lecture.py` l. 231 ; `n_plancher` = 800 dans `lecture-p3.json`). Ce n'est ni
la règle décisive ni « l'ancienne règle à 200 » ; d'où le module neuf (point 2), qui recalcule lui-même la lecture décisive
et l'ancienne règle sur les 200 premières, et ne lit plus E dans `lecture-p3.json`.

## 2. Lecture décisive de PB-1 sous la règle (a) — module neuf

(à compléter)

## 3. Chaîne

(à compléter)

## 4. Essais, mutations

(à compléter)

## 5. Couples proposés

(à compléter)

## 6. Réserves et points ouverts

- La consigne écrit la tête de `prep/p3bis-lanceur-v1` « `614fd5dab…` » ; la tête réelle, locale et distante (récupérée par
  refspec à 10:34 UTC), est `614fd5da4d63b3849f40d5dbf320ccb50d1a1330` ; aucun objet ne commence par `614fd5dab`. Lu comme
  une coquille ; branche partie de `614fd5da4d63…`.
