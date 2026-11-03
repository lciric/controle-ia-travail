# Épreuves sans appel de la suite du tour v9 — v1

Session fille, 3 novembre 2026, écrit à 07:24 UTC (heure relevée par `date -u`). Ordre `docs/procedures/ordre-fille-collisionneur-v9-suite-v1.md`
(`9be11cba…`, `main` 866e30fc). Aucune clé dans l'environnement des épreuves ; aucun appel réseau ; copies d'essai hors du dépôt.

Copie : `git archive ac25c055 donnees/collisionneur-v9-brainstorm-v1` vers `donnees/collisionneur-v9-brainstorm-v1-suite/` ;
59 fichiers, 59 compagnons conformes (`sha256sum -c`).

Fichiers neufs (compagnons posés) :
- `appel_controle_v11.py` `40247e50194ae4505fba44750b59cde90875c22cdfdcbb6f4859dd896beb15b3` (v10 `a451f910…` + lettres D/E en argument).
- `barrage_suite_v1.py` `9db63276d461e8c421ea80abb0bbe8e80993296cbe8010c05fad354a53e4681c` (barrage (a), par la fonction `verifier` du collisionneur chargé comme module : la sous-commande `verifier` réécrit `etat.md`, ce qui casserait son compagnon avant `avant-suite-v1.txt`).
- `lancer-tour-brainstorm-v9-v1-suite.sh` `ff878fad2df0b293a638de810a5d2efe080ca66e47b0b8989e5e14409ca2b63e` (v1 `2fd85687…`).

| N° | Cas | Attendu | Obtenu |
|---|---|---|---|
| 1 | sain (copie entière, aucune clé) | toutes les gardes passent, barrage (a) conforme, arrêt à la présence des clés | code 2 « KIMI_API_KEY absente » après « barrage (a) : 13 cellules valides ; non valides [D, E du tour E3-T3] ; problèmes 0 ; conforme » |
| 2 | sans `GO_ID` | refus | code 1, « GO_ID absent » |
| 3 | GO absent du registre | refus | code 2 |
| 4 | run manquant | refus | code 2, « run-brainstorm-e3-v1 absent » |
| 5 | un compagnon ne tient pas (un octet ajouté à une cellule) | refus | code 2, « compagnon non conforme » |
| 6 | barrage (a), cellule `E3-T3-reponse-C` retirée avec son compagnon | refus | code 2, « 12 cellules valides ; non valides [C, D, E] » |
| 7 | sans `PY_COLLISIONNEUR` | refus | code 1 |
| 8 | `controle-brainstorm-v1-suite.json` déjà présent | refus (R12) | code 2 |
| 9 | contrôle v11, lettres C, DC, DD, A, vide, DEX, sans argument | refus, aucune sortie | code 2, aucune sortie créée |
| 10 | contrôle v11, lettres DE, sur un collisionneur factice (aucun réseau) | seuls D et E appelés | code 0 ; appelants appelés : D, E ; espèces consignées KIMI_K3_1_PRO, GPT_6_ASTRA |

La copie saine est restée identique octet pour octet après l'épreuve 1. Barrage (b) (clés factices) non éprouvé par un appel : aucun appelant A, B ou C n'est atteint (barrage (a) et cas 10).
