# Règles de pré-contrôle C-1 et C-2 pour la réécriture de J-C — v1 (fille 12, R-1675)

Écrit le 2026-11-07. Outil : `outils/precontrole_c1_c2_v1.py` ; essais R5 : `outils/test_precontrole_c1_c2_v1.py` (8 essais : cas sain et artefact pour chaque règle, dont les cas « mot chez les deux membres » et « mot hors zone », paires factices écrites par le test). Aucune règle du script officiel changée ; aucun écrivain lancé.

## Règles fixes et seuils

| règle | objet | seuil |
|---|---|---|
| **C-1** (indice confirmé, 81 paires sur 320 = 25,3 %) | un mot d'ampleur dans le **titre ou la première phrase de PROPOSAL** d'un seul des deux membres d'une paire | **défaut de la paire**, tolérance zéro |
| **C-2** (« modèle plus gros », 25,0 %, non confirmé ; précaution déclarée) | une des formes ViT-L, Swin-L, Swin-B, XL, 70B, 27B, 3.1B, larger, large datasets / encoder / models, **avant COST**, dans un seul des deux membres | **défaut de la paire**, tolérance zéro |

Mots d'ampleur de C-1 (mots entiers, sans casse) : across, swept, sweep(s), scaled, scaling, several, multiple, repeated, larger, large, more seeds, backbones, various, numerous, a number of, a range of, dense grid(s), dense angle (les expressions du lecteur Opus, titre seulement, plus ses « quantificateurs vagues », étendues à la première phrase de la proposition par la demande de la mère).

## Comptage sur le J-C actuel (320 paires, pour mémoire)

- **C-1 : 104 paires en défaut (32,5 %)**, dont 86 où le membre porteur est le membre gonflé (étiquette 1).
- **C-2 : 77 paires en défaut (24,1 %)**, dont 67 où le porteur est le membre gonflé.
(La règle C-1 est plus large que celle du lecteur : elle compte aussi la première phrase de PROPOSAL et les quantificateurs vagues, donc davantage que les 81 paires de l'indice confirmé.) Aucune décision n'est prise sur ces valeurs.

## Usage prévu le 10 novembre

Appliquer C-1 et C-2 à chaque tâche de J-C réécrite dès son écriture ; le motif d'un renvoi peut nommer le défaut de C-1 ou de C-2 ; les autres pré-contrôles fixes (journal des règles fixes, `verif_lot_v1.py cout`) restent en vigueur.
