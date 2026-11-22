# Comparaison des suites complètes, main seule contre main plus la liste v3 — v1

Session des lentilles, 2026-11-21. Liste : `fiche-code/liste-a-verser-sur-main-code-v7-v3.txt` (b4ad54d5…, commit cc9ab8eb).

Deux arbres neufs ont été tirés de main f9139e66 : l'un porte main seule, l'autre main plus les 103 fichiers de la liste. Environnement : Python 3.13.18, torch 2.14.1+cpu, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`.

Ce document ne donne que des comptes. Aucun nom d'essai n'y figure, parce que certains noms d'essais de main touchent des sujets cloisonnés pour la session des lentilles.

## 1. Collecte de tout `tests/`

| | main seule | main plus la v3 |
|---|---|---|
| Essais collectés | 10 459 | 12 511 |
| Erreurs de collecte | 1 | 1 |

- Les 2 052 essais d'écart sont exactement ceux du paquet.
- L'erreur de collecte est la même dans les deux arbres. Elle est antérieure : il manque `sklearn` dans l'environnement.
- Sorties : `collecte-main-seule-liste-v3.txt` (04a3e19d…) et `collecte-main-plus-liste-v3.txt` (54902aac…).

## 2. Suite complète sur main plus la v3

- La première course d'un seul tenant, détachée, a été coupée à deux heures sans bilan.
- Elle a été remplacée par quatre éclats parallèles, répartis par fichier (369 fichiers `test_*.py` en tout), lancés avec `-v --tb=no --continue-on-collection-errors`.

| Éclat | Réussis | Échecs | Sautés | Erreurs | Échecs dans le paquet |
|---|---|---|---|---|---|
| 0 | 2 996 | 49 | 337 | 1 (collecte, la même) | 0 |
| 1 | 3 283 | 76 | 7 | 0 | 0 |
| 2 | 2 747 | 39 | 5 | 0 | 0 |
| 3 | 2 912 | 55 | 1 | 0 | 0 |
| **Total** | **11 938** | **219** | **350** | **1** | **0** |

Les essais du paquet passent tous : 2 052 réussis sur 2 052 (529 + 533 + 496 + 494).

## 3. Échecs rejoués sur main seule

Les fichiers contenant un échec ont été rejoués en entier sur main seule, puis les deux ensembles d'échecs ont été comparés par programme.

| Éclat | Échecs sur la v3 | Échecs sur main seule | Sur la v3 seulement | Sur main seule seulement |
|---|---|---|---|---|
| 0 | 49 | 48 | 1 | 0 |
| 1 | 76 | 76 | 0 | 0 |
| 2 | 39 | 39 | 0 | 0 |
| 3 | 55 | 55 | 0 | 0 |

**L'écart unique de l'éclat 0** :
- C'est un essai de main, hors du paquet.
- Seul, il passe sur les deux arbres, et encore trois fois de suite sur l'arbre de la v3.
- Son fichier entier donne le même résultat sur les deux arbres : 8 échecs, 4 réussis, et l'essai réussi dans les deux cas.
- Lecture : cet essai est instable sous la charge des quatre éclats parallèles. L'écart ne vient pas de la liste.

## 4. Conclusion

La liste v3 n'ajoute aucun échec ni aucune erreur de collecte à main seule, en dehors de cet essai instable sous charge. Ses 2 052 essais propres passent tous.

Les 218 échecs communs existent déjà sur main dans cet environnement. Ce n'est pas à la session des lentilles de les examiner.
