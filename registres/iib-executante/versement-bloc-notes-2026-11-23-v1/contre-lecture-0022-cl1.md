# Contre-lecture cl1 du correctif 0022 — vitesse mesurée en marche au premier lot, liste de l'étalonnage v7

Pièce de classe B (instrument). Contre-lecteur neuf (Claude Opus 5.5). Il n'a écrit ni le correctif ni son rapport. Aucun fichier interdit n'a été ouvert. Rien n'a été poussé, rien dépensé, aucun modèle appelé.

## Verdict : autorisable après corrections

Aucun point bloquant. Le code fait ce que dit le rapport. Les nombres annoncés sont retrouvés. Il y a un point majeur, que l'ordre doit trancher, et quatre points mineurs.

Base 0021 : arbre `725f3d5884c3617065aa913d04e9b3eee0e2afac`. Correctif : sha256 `f570581e…6a87`, conforme. Arbre après `git am` : `a814f0701f413ba38f37de781929f4f24610cbb7`, conforme.

## Ce qui est vérifié et conforme
- `lanceur_v5.vitesse_du_premier_lot` (`src/controle_ia/iib/lanceur_v5.py:243-257`) n'écrit que des durées, des comptes et la méthode de tirage. Elle n'écrit ni texte, ni jeton, ni sortie d'oracle. Le fichier passe par `_ecrire`, qui ajoute l'avertissement, refuse d'écraser et scelle.
- Son appel dans `verser` (`lanceur_v5.py:303-308`) a lieu une seule fois, au lot 1 (honnêtes : génération puis les deux oracles), après le scellement et la poussée de ce lot. Le chronomètre ne contient alors que ce lot.
- Une durée non mesurée est refusée par une `GardeArret`. Le fichier n'écrit jamais zéro à sa place. Le refus est éprouvé par un essai unitaire.
- La marque de progrès `etape=vitesse lot=1 generation_s_par_episode=… oracle_P_s_par_action=… oracle_N_s_par_action=…` est conforme à `MOTIF_PROGRES` et ne touche aucun motif de `MOTIF_INTERDIT` (`scripts/amorce_instance_iib_v5.sh:266-267`). Dans la répétition, elle est relayée au journal de l'instance, et le journal compte zéro ligne « non relayée ».
- Le fichier de vitesse est poussé par le versement, motif « vitesse du premier lot ». Le commit dit « versement vitesse du premier lot » et ne se compte pas parmi les commits « (versement lot ». Quand l'origine refuse, la vitesse est refusée comme un lot. Les trois refus de suite tombent donc après le lot 2, et non plus après le lot 3. L'essai le dit (`tests/test_iib_versement_v5.py:132-139`). Le fichier reste scellé sur le disque.
- `scripts/tests-cibles-iib-v5-v7.txt` est égal à la v6 plus `tests/test_tirage_carte_v1.py`, trié (un `diff` ne montre que cette ligne). Son sha256 vaut `81e2f75ac9cab360324485f4d76b326d97e7297a0aeaf5af70a52f515e8f21b8`, celui écrit en dur dans l'amorce (`scripts/amorce_instance_iib_v5.sh:394`).
- Aucune régression vue. La course, la coupure de l'étalonnage et l'écriture de fin sont intactes. Le seul ajout aux sorties est la clé `VITESSE`, qui entre dans les empreintes du résumé. La répétition locale courte va de bout en bout, course comprise, avec le code 0.
- `TESTS_ATTENDUS` : le comptage le confirme, 311 pour l'étalonnage v7 et 313 pour la course v2 (détails plus bas).

## Points

### Majeur
**M1. Le fichier de vitesse, un diagnostic, peut maintenant arrêter une course payante que la fin d'étalonnage aurait tolérée.** Voir `lanceur_v5.py:250-256`.
- `vitesse_du_premier_lot` exige les deux oracles mesurés au lot 1.
- `duree_d_une_action_d_oracle` (`lanceur_v5.py:237-240`) n'en exige qu'un.
- Les actions d'oracle ne sont comptées que sur une coupe conforme (`oracle_v5.py:155`).
- N ne tire ses propres suites qu'à partir de la troisième action (`oracle_v5.py:145-149`).
- Conséquence : un premier lot de 8 épisodes sans coupe conforme mesurable pour l'un des oracles arrête l'étalonnage après le lot 1.
- Si c'est voulu (« durée non mesurée = refus » au sens d'arrêt), l'ordre doit le dire et un essai doit le prouver.
- Sinon, correction proposée : une durée non mesurée s'écrit `null`, avec `"non_mesurees": ["oracle_N_s_par_action", …]`, et la marque porte `vitesse=incomplete`. Jamais un zéro, et la course continue.
- Dans les deux cas, ajouter un essai d'intégration (R5, cas artefact) : chronomètre d'un oracle forcé à zéro dans `executer("etalonnage", …)`, puis vérifier que le lot 1 est scellé et poussé, et que le motif d'arrêt est écrit ou que le `null` est écrit.
- Aujourd'hui, l'artefact n'est éprouvé que sur la fonction seule (`tests/test_iib_lanceur_v5.py:727-728`).

### Mineurs
**m1. L'arrondi à 4 décimales peut écrire un zéro** (`lanceur_v5.py:253`).
- Une durée réelle inférieure à 50 µs devient `0.0`, ce que la règle interdit. Dans le jouet, les durées valent déjà 0,0005 s par action.
- Correction : ne pas arrondir (ou garder 9 chiffres significatifs, `float(f"{x:.9g}")`), et refuser si le résultat vaut 0.
- Autre défaut : un numérateur absent (`chrono[s]`) lève une `KeyError` et non une `GardeArret`. Remplacer par `chrono.get(s)` avec le même refus.

**m2. Le tirage déclaré est déduit, pas lu** (`lanceur_v5.py:257`).
- `getattr(modele, "tirage", None) or "processeur (…)"` écrit « processeur (multinomial…) » pour le modèle jouet, qui ne tire pas par torch. C'est le cas du fichier de la répétition.
- Correction : passer à `phase_etalonnage` le tirage effectif reçu par `executer` (`--tirage`, déjà écrit au résumé) et l'écrire tel quel.

**m3. `--liste-figee` de la répétition locale ne peut passer nulle part** (`scripts/repetition_locale_iib_v5.py:37`).
- Avec `ATTENDUS = 297` et la liste v7 :
  - sans torch, on obtient « 297 passed, 1 skipped » ;
  - avec torch sur processeur, « 310 passed, 1 skipped » ;
  - sur une machine à carte, 311.
- Le contrôle de l'amorce exige « N passed » sans saut. Le commentaire « ne passe que sur la machine » est donc faux.
- Correction : `ATTENDUS = 311` avec un commentaire juste, ou faire refuser explicitement `--liste-figee` hors d'une machine à carte (`torch.cuda.is_available()`).

**m4. L'en-tête de l'amorce est périmé** (`scripts/amorce_instance_iib_v5.sh:6`).
- Le point (b) cite encore `tests-cibles-iib-v5-v6.txt`, alors que la ligne 394 cite la v7.
- Le point (i) est placé avant le (h) (lignes 19-22).
- Correction : écrire « v7 (correctif 0022) » au point (b) et remettre (i) après (h).

Remarque, sans correction demandée. Sur la machine, `test_tirage_carte_v1.py` saute en entier si `transformers` ou `scipy` manque (`importorskip`, lignes 9-11). Le contrôle « 311 passed » arrêterait alors la machine avant tout calcul. C'est sûr, mais il faut vérifier que l'image les porte.

## Commandes jouées et comptes
Worktree neutre : `…/scratchpad/cl-0022`, base 6696aca1, puis `git am` du correctif.

| Essai | Résultat obtenu | Résultat annoncé |
|---|---|---|
| v7 sans torch (venv `venv-cl0022-st`, `requirements-cpu.txt` sans la ligne torch) | 297 passed, 1 skipped, en 583 s | 297 passed, 1 skipped : conforme |
| v6 sans torch | 297 passed, en 609 s | 297 : conforme |
| v7 avec torch 2.14.1 (`requirements-cpu.txt`, qui porte déjà torch) | 310 passed, 1 skipped, en 640 s | 310 passed, 1 skipped : conforme |
| course v2 avec torch | 312 passed, 1 skipped, en 634 s | 312 passed, 1 skipped : conforme |

Commande des essais : `PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no $(cat scripts/tests-cibles-iib-v5-v7.txt)`, la forme de l'amorce.

Comptage par `pytest --collect-only -q`, avec torch :

| Liste | Essais collectés |
|---|---|
| v7 | 311 |
| course v2 (= v7 + `tests/test_iib_distillation_torch_v5.py`) | 313 |
| v6 | 297 |
| `tests/test_tirage_carte_v1.py` | 14 |

`TESTS_ATTENDUS` est donc confirmé : 311 pour l'étalonnage, 313 pour la course.

Répétition locale courte, sans torch :
- Commande : `PYTHONPATH=src python3 scripts/repetition_locale_iib_v5.py …/scratchpad/repetition-0022-cl1`.
- Code 0, « RÉPÉTITION RÉUSSIE ».
- Vu : 28 poussées par lot plus « versement vitesse du premier lot » poussé, une marque `etape=vitesse` relayée, `diag/<run>/vitesse-premier-lot-iib-v5.json` présent.
- Sceau du fichier conforme : sha256 f067ec51…62eb.
- Contenu du fichier : 9 clés, durées et comptes seulement.
