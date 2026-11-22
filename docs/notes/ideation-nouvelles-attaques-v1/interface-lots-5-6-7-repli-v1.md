# Interface commune des lots 5 v2, 6 v4 et 7 v1 du véhicule NA-1 — v1

Pièce de travail de la session de l'organisme, écrite le 2026-11-22 vers 10:50Z sur l'ordre de la mère (10:45Z). Elle fixe les champs que les trois lots, écrits en parallèle, se passent entre eux. Si un développeur ne peut pas la tenir, il le dit dans son rapport et ne la change pas de lui-même.

## Registre des tentatives (lot 5 v2 l'écrit, lot 6 v4 l'alimente, lot 7 le lit)
Chaque ligne d'une tentative d'appel porte, en plus des champs du lot 5 v1 :

| champ | type | valeurs |
|---|---|---|
| `generation` | entier | 1, 2, 3… |
| `filiation` | chaîne ou `null` | identifiant de la fiche mère, ou `null` |
| `espece` | chaîne fermée | nom de rôle de l'espèce **demandée** (`espece-1` à `espece-5`, `aiguilleur`, `portier`, `juge-1`, `juge-2`, `passe-x`) |
| `case` | chaîne fermée ou `null` | valeur de la case servie, ou `null` pour les requêtes sans case |
| `rang_repli` | entier | 0 pour l'appel demandé, 1 pour le premier repli, 2 pour le second |
| `modele_demande` | chaîne | identifiant par rôle, jamais un nom de modèle en clair dans une pièce servie |
| `modele_servi` | chaîne | identifiant lu dans la réponse |
| `raison_arret` | chaîne | raison d'arrêt du fournisseur (`end_turn`, `refusal`, …) |
| `categorie_refus` | chaîne ou `null` | catégorie si le fournisseur la rend, sinon `null` (jamais devinée) |
| `cout_compte_usd` | décimal | coût compté de la tentative, au pire si l'usage manque |
| `classe_issue` | chaîne fermée | les classes de la v9 plus la classe « refus par classifieur, servi par repli » |

## Comptes (lot 6 v4 les produit, lot 7 les lit)
- M6 par case **et** par espèce demandée, en plus du compte par rôle.
- Un compte de replis par espèce demandée et par modèle servi : nombre et coût.
- Une fiche servie par repli est attribuée au modèle servi et rapportée à part. Elle compte dans M3 et dans la garde du coffre (arrêt n° 5).
- En M4, seule la première tentative est comptée à l'espèce ; une ligne « replis » est ajoutée.

## Règle de lecture pour les trois développeurs
- Les fichiers de plus de 150 lignes se lisent par tranches de moins de 150 lignes.
- Aucun `find` ni `grep -r` hors des dossiers listés dans le mandat.
- Rien sous `/root/.claude/` ne se lit, ni un chemin que l'outil rend comme sortie enregistrée.
- Le dossier `resultats/` de l'orchestrateur de base ne se lit pas.
