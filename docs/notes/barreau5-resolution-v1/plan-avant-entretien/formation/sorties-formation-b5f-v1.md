# Sorties de la formation du barreau 5 — v1

Pièce de la ligne `SORTIES-FORMATION-B5F` du registre propre (`registres/barreau5-familles-jumelles-v1.md`), rédigée par la session de formation (`session_01QPDgKjCQYmTHUEjN63ThC8`) le 2026-11-21 après la fin de toutes les instances et de toute relance (plan de marche de la session, points 4 et question 4). Aucune sortie de marche lue : seuls les journaux « B5F », les inventaires finaux scellés par l'amorce et `git` ont servi.

Pour chaque instance : branche de sortie, commit prouvé (ligne « versement final prouvé … au commit » du journal de l'instance), tête de la branche à la rédaction, identifiant de marche, nombre de fichiers et empreinte sha256 de `traces-b5f/inventaire-final.json` au commit prouvé. Chaque commit prouvé est un ancêtre de la tête, et l'empreinte de l'inventaire est égale à celle de son compagnon `.sha256` ; la garde `detruire` du lanceur du commit de course (4bdf0d22…) a accepté chaque versement avant la destruction de l'instance.

| instance | branche de sortie | commit prouvé | tête | marche | fichiers | inventaire sha256 |
|---|---|---|---|---|---|---|
| 1-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-1-x1` | eb4b946c333be96515f3c36fa9537816259673ac | b5b5917946221e09f7b56ba664f4635cd54df34d | 20261121-055443-b5f-formation-1-x1 | 53 | c9f9310df9f1efcf60334c9dab2070ad871a1fc8ad10c28e5eb1e794c8e8f293 |
| 2-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-2-x1` | 7b0e19b928d76c1f655dc512eea72440a570ebce | e6923e7250b369b02489ee29d0aacdc4233abf83 | 20261121-060152-b5f-formation-2-x1 | 53 | 1a30355a2834da19093e614c708b81ba5007f27c8e7d32b9adde2495879c7eae |
| 3-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-3-x1` | f74795a16c609eb00cc86c5043bf211805c428bb | 8615f2aab048cce9418a9fce8084e601997a8bae | 20261121-071239-b5f-formation-3-x1 | 53 | 01031f467a5f2d59c808adbf9c407b78efa0bfc8ee8c862d001efe0b0241f057 |
| 4-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-4-x1` | 75814afec793814f44afff946344e94d46ea8f0e | c23e6a03d957b77c783cf13d303def63e2590c84 | 20261121-072248-b5f-formation-4-x1 | 53 | a0cb97cbc13c15f2de10306638b6b4d2bf4c70660db69fc28745b22bd40e4ea6 |
| 5-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-5-x1` | e37790479d51c4f5fd7d68f11037254f15749de5 | 33431bf85975f10c195b5964bf2c09dc3ea439e4 | 20261120-144431-b5f-formation-5-x1 | 53 | 436675e2a567213910038c796f4d39400055dcce32cea2289508fd180c6137b3 |
| 6 | `donnees/barreau5-familles-jumelles-v1-formation-instance-6` | 0a6af341244900da047ea850a966bf137dee279b | 85a4942b02178edb2bf228a0b995bee2dcf4e97d | 20261120-012937-b5f-formation-6 | 53 | 6d80070c2c7ec895a87b599e720fb3b12e93bc1fd1758d01481480a96bddcf88 |
| 7-x1 | `donnees/barreau5-familles-jumelles-v1-formation-instance-7-x1` | 7714b0ac6a9a11cd2b1644a747bda0dcccec513a | a7bc1faea6edce7780ef0a693c2388c6c102b976 | 20261120-144552-b5f-formation-7-x1 | 35 | 1e82f1d92528c81fca0aed1c25b1f8980a05d9ad478777ffe246bc408190087c |

Notes :
- Instances 1, 2, 3 et 4 : copies `-x1` des recréations du 21 novembre (additif 2 v6, GO-2026-11-21-01 et -03). Pour 2, 3 et 4, les têtes citées sont celles des branches des recréations ; les têtes supprimées par Lazar (4fef6073…, b35dfe17…, 77fd59da…) restent copiées sous `traces/barreau5-relance-<n>-premiere-tentative` et ne sont jamais réunies à la branche de la formation.
- Instance 5 et 7 : copies `-x1` des relances du 20 novembre (additif 1 v3). Instance 6 : première marche, jamais relancée.
- Réunion de la branche de la formation : à faire par la session mère, à partir des commits ci-dessus, avec un seul dossier `donnees/<marche>` par instance (exigence du code de lecture figé, `_familles_formees`).
