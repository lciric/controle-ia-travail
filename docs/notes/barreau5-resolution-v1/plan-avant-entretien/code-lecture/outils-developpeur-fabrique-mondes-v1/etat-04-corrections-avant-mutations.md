# État 04 — défauts de l'état 03 corrigés ; 138 essais passent ; avant le passage de mutations

20 novembre 2026 (horloge du conteneur). Pièce de travail du second développeur de la fabrique (Claude Opus 5.5).

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` | `f41377ae202590bb5c05f13bd0ce66bf84dcb5525e10a4f18a753a786e5cc692` |
| `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` | `37e136b087f9c9e39e318c45b356c48dc9a4e4b9a1f601b5b78fec5bb7135e1c` |
| `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` | `6ffe12e0d334a83dcf0369e1a879f3b7d4b8af8c922dceba391ea953ddb34802` |
| `…/outils-developpeur-fabrique-mondes-v1/mutations_fabrique_juge_v1.py` | `c5be482d0e13fda20f5c1983be16b020faab463e2512bcddf42c6c0b83c4bc5b` |

Corrections (défauts 1 à 6 de l'état 03) : ligne `ENGAGEMENT-B5F` au registre fabriqué, contenu paramétré, deuxième cas
de V7 en deux variantes (ouverture à l'empreinte engagée ; ouverture à la table reçue) ; V12 en deux signes de la trace,
moitié des mondes chacun ; épisodes d'évaluation sur 32 tâches, référence honnête sur 64 ; « copie » au nom de la famille ;
graines sur la clé `b5f/epreuve/<monde>` ; options laissées à l'agent de l'épreuve (lignes de registre en plus, résumé des
familles d'apprentissage, empreintes d'adaptateurs). Essais neufs : bruit indépendant d'un membre à l'autre, signe de V12,
deux variantes du deuxième cas, options, et six essais du juge.

Essais : `PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider
tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` → 138 passés en 106 s.

Ces fichiers peuvent encore changer selon le passage de mutations.
