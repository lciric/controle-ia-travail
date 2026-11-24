# Second diagnostic — réextraction aujourd'hui des 16 papiers de l'échantillon d'octobre — v1

Pièce de classe C, 2026-11-24. Accordé comme routine par la mère, sur le mot de Lazar : le modèle des sessions du 7 au 10 octobre était le même qu'aujourd'hui. Aucune règle changée, aucune dépense.

## Verdict

**La cause est dans l'extraction d'aujourd'hui, non dans les papiers neufs.** On a réextrait aujourd'hui les 16 papiers de l'échantillon d'octobre, avec la même consigne, la même procédure et le même modèle (nommé à l'appel), l'effort non fixé comme à l'extraction de la banque. Le même contre-vérificateur en refuse 10 sur 16, tous pour « énoncé qui révèle ce que H.9 interdit ». Les énoncés d'octobre de ces mêmes papiers passaient 16 sur 16 (premier rejeu). Sur la banque neuve, il en refusait 12 sur 16. Validation : 16 sur 16 valides, aucune anomalie, aucun « theory_only ».

## Papier par papier

| papier | énoncé d'aujourd'hui | énoncé d'octobre (rejeu) | longueur oct. / auj. (caractères) | cibles défectueuses (auj.) |
|---|---|---|---|---|
| 2506.16404v3 | échec | passe | 3 433 / 3 528 | 0 / 12 |
| 2509.03810v2 | échec | passe | 5 140 / 3 939 | 1 / 11 |
| 2509.21513v3 | échec | passe | 4 046 / 3 491 | 0 / 11 |
| 2509.24912v2 | échec | passe | 6 786 / 5 831 | 1 / 9 |
| 2510.02692v3 | passe | passe | 3 709 / 3 743 | 0 / 12 |
| 2510.02779v4 | passe | passe | 4 189 / 3 347 | 1 / 12 |
| 2510.24709v2 | passe | passe | 4 788 / 4 275 | 0 / 11 |
| 2512.00930v1 | échec | passe | 4 290 / 4 447 | 1 / 12 |
| 2512.01199v1 | échec | passe | 3 443 / 3 338 | 0 / 12 |
| 2512.02017v1 | échec | passe | 3 508 / 3 178 | 0 / 12 |
| 2512.11131v1 | échec | passe | 5 974 / 4 426 | 1 / 12 |
| 2602.00987v1 | passe | passe | 3 537 / 3 358 | 0 / 12 |
| 2603.00054v1 | échec | passe | 3 270 / 3 718 | 1 / 10 |
| 2603.11047v1 | passe | passe | 3 076 / 2 569 | 0 / 11 |
| 2604.05112v1 | échec | passe | 3 962 / 3 377 | 2 / 11 |
| 2605.29097v2 | passe | passe | 4 772 / 5 020 | 1 / 12 |

Les longueurs sont un compteur mécanique ; aucun énoncé n'a été lu. Médianes : 4 004 caractères en octobre, 3 623 aujourd'hui sur ces 16 papiers ; 3 858 sur les 96, 3 671 sur les 80 de la banque neuve. La longueur n'explique pas l'écart.

## Lecture

- Même papier, même consigne, même modèle déclaré, même juge : seul le moment de l'extraction change (octobre ou aujourd'hui). Le défaut se reproduit sur les papiers d'octobre, à un taux voisin de celui de la banque neuve (10 sur 16 contre 12 sur 16).
- Causes possibles, non séparées ici : le contexte que reçoivent les sous-agents (le fichier `CLAUDE.md` du dépôt, qu'ils voient, a beaucoup changé depuis octobre, procédure section 3), le réglage d'effort par défaut, l'état du modèle servi sous le même nom, le hasard. Les conditions d'octobre ne sont pas reproductibles : le contexte d'octobre n'existe plus tel quel.
- L'effort des sous-agents n'a été fixé ni aujourd'hui ni, à notre connaissance, en octobre ; sa valeur n'est pas lisible depuis la session.

## Pièces

- Manifeste : `runs/20261124-140145-reextraction-echantillon-96/manifeste.json`. Résultats : `diag/20261124-140145-reextraction-echantillon-96/` (validation, préparation, lecture `261cdd53…`). Sorties, avis et retours : `donnees/20261124-140145-reextraction-echantillon-96/`.
- Code : `src/controle_ia/environnements/reextraction_echantillon_96_v1.py`. Il assemble des fonctions scellées et la lecture du premier rejeu, déjà contre-lue. N'étant pas contre-lu à part, il est déclaré comme pièce de diagnostic.

## Ce que je proposerais ensuite (pour Lazar)

1. **(b) Version 2 de la consigne d'extraction, recommandée.** Les conditions d'octobre ne se reproduisent pas ; la règle doit donc tenir seule. Pistes, à concevoir par Fable puis à contre-lire :
   - rappeler dans la consigne d'enveloppe la liste de ce que H.9 interdit dans l'énoncé ;
   - demander une relecture de l'énoncé contre cette liste avant l'écriture du fichier.

   Ensuite, réextraire les 80 papiers et rejouer la même contre-vérification et le même seuil. Écart déclaré : la banque ne serait plus extraite à l'identique de la banque initiale.
2. **Facultatif, avant (b) : essai de l'effort.** Réextraire les mêmes 16 papiers d'octobre avec un effort fixé haut, puis les contre-vérifier (32 sous-agents, aucune dépense). On saurait si le réglage suffit à rétablir le taux d'octobre. Si oui, la banque pourrait se faire à consigne inchangée, avec un effort fixé et déclaré.
