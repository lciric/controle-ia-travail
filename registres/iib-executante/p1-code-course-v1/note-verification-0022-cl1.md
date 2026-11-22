# Vérification des corrections de la contre-lecture cl1 du 0022, par le correctif 0025

Pièce de classe B. Vérification faite par le même contre-lecteur (Claude Opus 5.5). Mêmes interdits, rien poussé, rien dépensé.

## Verdict : autorisable

Le majeur et les quatre mineurs sont corrigés. Il reste deux retouches de commentaire, facultatives.

Commit vérifié : `f7a5123e0fe8e55cfecbb0ac16b17eff50b0d4e1`, arbre `717f0b203a78256f44a822dd3891ba31c88c22d8`, conforme. L'amorce de l'étalonnage a le sha256 `4140d3b3cadd6dae3a39845ce841a9491d4f7e86586d89af4e8fc549a0083717`, conforme. La liste v7 est inchangée (`81e2f75a…`).

## Points corrigés
- **Majeur.** `vitesse_du_premier_lot` (`src/controle_ia/iib/lanceur_v5.py:246-278`) ne lève plus d'exception.
  - Une durée non mesurée (compte nul ou absent, durée absente ou non positive) s'écrit `null`. Elle est nommée dans `non_mesurees`.
  - La marque dit `non_mesuree` (`marque_de_vitesse`). Ce mot ne touche aucun motif interdit de l'amorce.
  - L'essai `tests/test_iib_vitesse_0025.py` retire l'oracle N du chronomètre au lot 1. L'étalonnage va alors jusqu'à son fichier de fin, la vitesse est scellée avec N `null`, et la marque le dit.
  - Limite acceptable : la panne est injectée au niveau de la fonction, pas dans l'oracle.
- **Mineur 1.** Plus d'arrondi. `KeyError`, `TypeError` et `ValueError` sont absorbées et deviennent `null`. L'essai sur des durées de 1e-7 s n'obtient jamais un zéro.
- **Mineur 2.** Le tirage est passé par `executer` puis `phase_etalonnage`, sinon pris dans l'attribut du modèle, sinon « non lu ». Dans la répétition, le fichier écrit `"tirage": "processeur"`.
- **Mineur 3.** `ATTENDUS = 311`, avec un commentaire juste (`scripts/repetition_locale_iib_v5.py:37`).
- **Mineur 4.** Le point (b) de l'en-tête cite la v7. Correction partielle, voir plus bas.

## Retouches facultatives (commentaires seulement, sans effet)
- `scripts/amorce_instance_iib_v5.sh:6-7`, point (b) :
  - il garde « v6, correctif 0014 » et « vingt-cinq fichiers », alors que la v7 en compte 26 ;
  - écrire plutôt « v7, correctif 0022 : vingt-six fichiers (v6 et l'essai du tirage) ».
- Lignes 19-22 : le point (i) précède encore le (h).

## Commandes jouées et comptes
Toutes jouées avec `PYTHONPATH=src` et `pytest -q -p no:cacheprovider`, dans le worktree `…/scratchpad/cl-0022` mis sur f7a5123e.

| Essai | Résultat |
|---|---|
| `tests/test_iib_vitesse_0025.py`, `tests/test_iib_lanceur_v5.py`, `tests/test_iib_versement_v5.py` (sans torch) | 35 passed |
| v7 sans torch | 297 passed, 1 skipped |
| v7 avec torch 2.14.1 | 310 passed, 1 skipped |

Comptage par `--collect-only` :

| Liste | Essais collectés |
|---|---|
| v7 | 311 |
| course v2 | 313 |

`TESTS_ATTENDUS` est donc confirmé : 311 pour l'étalonnage, 313 pour la course.

Répétition locale courte (`scripts/repetition_locale_iib_v5.py`, sans torch) :
- code 0, « RÉPÉTITION RÉUSSIE » ;
- « versement vitesse du premier lot » poussé ;
- marque `etape=vitesse … generation_s_par_episode=0.00216592 …` relayée, avec 0 ligne « non relayée » ;
- fichier de vitesse avec `non_mesurees: []` et `tirage: processeur`, sceau OK.

Nettoyage fait à la fin : répétitions, environnements virtuels et worktree retirés.
