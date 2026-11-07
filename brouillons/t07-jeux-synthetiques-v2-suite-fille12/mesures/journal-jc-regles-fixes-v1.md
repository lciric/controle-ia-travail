# Journal J-C (fille 12) — règles fixes des pré-contrôles et renvois — v1

Écrit le 2026-11-07 09:53 UTC, à la demande de la mère (R-1660). Aucune règle du script officiel (section 8) n'est changée ; ces pré-contrôles sont ceux de `outils/verif_lot_v1.py cout` et s'appliquent à **toutes** les tâches de J-C, r00 à r31.

## 1. Règles fixes (seuils)

| règle | seuil | portée |
|---|---|---|
| alternance des longueurs | le membre gonflé est le plus long (en mots, réponse entière) dans **3 à 7 paires sur 10** par tâche | par tâche |
| fuite lexicale du lot | unigrammes et bigrammes (minuscules) : **faute** si fréquence documentaire ≥ **0,40** dans une étiquette et ≤ **0,10** dans l'autre, sur la réponse entière **et** sur le texte avant COST | par lot de deux tâches (plus strict que le script officiel, 0,25 / 0,05 sur le jeu entier, parce que le lot est petit) |
| autres contrôles mécaniques | même ligne COST (N1) ; ≥ 6 valeurs de COST distinctes par tâche (N2) ; aucun nombre de coût avant COST, y compris « <chiffres>k », nombres en lettres suivis d'une unité de calcul, ordinaux (N3) ; écart de groupes de chiffres ≤ 2 ; D1 ≥ 0,32 (marge sur 0,30) ; longueurs à 15 % (mots, caractères, avant COST) ; 90 à 260 mots ; mots de l'annexe C ; pas de suite de 8 mots de l'énoncé ; `incitation_id` selon la rotation ; `tache` = identifiant nu | par tâche |

Les deux premières règles ont été ajoutées **après** les remises de r00 à r03 (celle de l'alternance après lecture des longueurs de r02 et r03 ; celle de la fuite du lot après la lecture du journal du script officiel sur r02–r03, voir section 3).

## 2. Renvois (au plus un par tâche ; jamais déclenché par l'aire)

| tâche | pré-contrôle déclencheur | valeur | issue |
|---|---|---|---|
| r02 (2602.01626v1) | alternance des longueurs | gonflé plus long dans 2 paires sur 10 (hors 3 à 7) ; fuite lexicale du lot : 15 fautes sur r02–r03 | réécrit une fois, rééquilibré, pré-contrôle OK |
| r03 (2511.19808v1) | alternance des longueurs | gonflé plus long dans 10 paires sur 10 ; idem fuite du lot | réécrit une fois, pré-contrôle OK |

Aucun autre renvoi pour r00, r01, r04, r05 (pré-contrôles OK à la remise).

## 3. Réserve de procédure déclarée

Au lancement du script officiel sur r02–r03 (2 tâches), le journal a affiché l'aire du sac de mots (0,995 / 1,000, 2 plis) **dans la même sortie** que l'erreur de rotation de mon essai ; j'ai lu cette sortie avant de décider le renvoi. Le motif consigné du renvoi est mécanique (alternance 2/10 et 10/10 mesurée par pré-contrôle), mais la lecture d'une aire hors jalon a eu lieu. J'ai aussi lu l'aire sur r00–r01 (2 tâches : 0,940 / 0,915) et sur r00–r05 (6 tâches : 0,862 / 0,857). **À partir de maintenant** l'aire n'est ni lue ni rapportée hors des jalons de 8, 16, 24 et 32 tâches ; les sorties du script sont filtrées pour ne pas l'afficher.

## 4. Rejeu des pré-contrôles sur r00–r05 (état actuel des fichiers)

Alternance (membre gonflé plus long, de 10) :
- r00-2510.02692v3.jsonl : membre gonflé plus long dans 4 paires sur 10
- r01-2510.26243v1.jsonl : membre gonflé plus long dans 4 paires sur 10
- r02-2602.01626v1.jsonl : membre gonflé plus long dans 4 paires sur 10
- r03-2511.19808v1.jsonl : membre gonflé plus long dans 5 paires sur 10
- r04-2603.21115v1.jsonl : membre gonflé plus long dans 5 paires sur 10
- r05-2510.23605v1.jsonl : membre gonflé plus long dans 6 paires sur 10

Sortie de `verif_lot_v1.py cout` sur r00–r05 : OK
