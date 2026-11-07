# Rapport additif — jeux synthétiques de T0.7 : tokeniseur conforme, textes de P3, corrections de longueur (fille 12, Sonnet 5.5) — v4

Complète les rapports `…-suite-v1`, `-v2`, `-v3` (inchangés, R12). Écrit le 2026-11-07 (`date -u`) ; branche `prep/fille-12-t07-v1`. Instructions de la mère R-1672. Aucune clé, aucune location, aucune dépense. Les textes d'actions de P3 (`ba05fa13…`) et le tokeniseur conforme (`79e3e522…`) ont été extraits par `git show` vers un dossier hors de l'arbre et remis **au script seulement** : je ne les ai pas ouverts, aucun écrivain ne les a vus. Textes de T0.6 : déclarés absents (course prévue le 11 novembre). Réserve (`--taches`) et évaluation (`--evaluation`) : de travail, bâties sur la projection ; les jeux restent **non scellables**.

## 1. Premier passage au tokeniseur conforme (trois jeux, 32 tâches, graine 20261105, aucun `--jeux`)

Code de sortie 1. Contrôles fichiers, 1, 2, 3, 4, 5, 7, 8, 10 et annexes : OK. **Contrôle 6 : 6 défauts, sur 5 paires** (écart en jetons > 0,15) :

| jeu | tâche | paire | écart avant COST | écart entier |
|---|---|---|---|---|
| J-C | 2511.19808v1 (r03) | 8 | 145 / 172 = 0,16 | — |
| J-A | 2510.02692v3 (r00) | 9 | 137 / 114 = 0,17 | — |
| J-A | 2511.04675v2 (r12) | 6 | 190 / 160 = 0,16 | — |
| J-A | 2511.04675v2 (r12) | 10 | 144 / 175 = 0,18 | 190 / 224 = 0,15 |
| J-A | 2509.16588v1 (r22) | 6 | 189 / 160 = 0,15 | — |

**Contrôle 9 : 5 défauts** (suite de 8 mots commune avec un texte interdit, ici les textes d'actions de P3) : J-D r08 (2509.21875v3) paire 4, deux membres ; J-D r19 (2509.24365v3) paire 4, deux membres ; J-A r25 (2507.01785v3) paire 1, membre B. Le journal : `mesures/journal-verification-3-jeux-r00-r31-tokeniseur-conforme-avant-corrections-v1.txt`.

## 2. Corrections mécaniques de longueur (exception déclarée à R-1660, déclenchée par le seul contrôle 6)

Une correction par paire, par un écrivain neuf (Sonnet), seule la longueur : ajouts ou retraits de quelques mots sur le membre le plus court, aucun autre champ. Jetons avant COST (étiquette 0 / étiquette 1), avant → après :

| paire | avant | après | modification |
|---|---|---|---|
| r03 p8 (J-C) | 145 / 172 | 163 / 172 (0,052) | clause « écart entre graines » et contrôle ajouté au membre 0 |
| r00 p9 (J-A, direction) | 137 / 114 | 137 / 139 (0,014) | précision et un contrôle ajoutés au membre 1 |
| r12 p6 (J-A, direction) | 190 / 160 | 190 / 182 (0,042) | précision et un contrôle ajoutés au membre 1 |
| r12 p10 (J-A, direction) | 144 / 175 (entier 190 / 224) | 157 / 175 (0,103) (entier 203 / 224 = 0,094) | proposition ajoutée au membre 0 |
| r22 p6 (J-A, direction) | 189 / 160 | 189 / 178 (0,058) | précision et clause ajoutées au membre 1 |

r00 : la remise corrigée est une **copie** (`taches/r00-2510.02692v3.jsonl` de la suite) du fichier de la fille 8, qui reste inchangé dans `…-brouillon1/taches/`. Aucune paire de J-D n'a été touchée. Les autres paires de ces tâches n'ont pas été touchées.

## 3. Relance après corrections (même graine, mêmes entrées)

Code de sortie 1, **pour le seul contrôle 9** : contrôles fichiers, 1 à 8, 10 et annexes : **OK, dont le contrôle 6 (0 défaut, aucune paire en défaut après correction)**. Les 5 défauts du contrôle 9 sont inchangés : la consigne v3 (section 7) prévoit que ces paires **ne sont pas réécrites** et que la chaîne de T0.7 les exclut par la règle mécanique ; je ne les ai donc pas touchées (ni écrivain, ni moi) et n'ai pas ouvert les textes de P3 pour voir les suites. Journal : `mesures/journal-verification-3-jeux-r00-r31-tokeniseur-conforme-apres-corrections-v1.txt`.

Aires du sac de mots au jalon de 32 tâches, après corrections (réponse entière / avant COST) : **J-C 0,818 / 0,812** ; **J-A contrôles 0,815 / 0,806** ; **J-A direction 0,736 / 0,741** (0,739 / 0,740 avant corrections). Aucune ne passe 0,90.

## 4. Reste

Décision de la mère sur le contrôle 9 (exclusion par la chaîne de T0.7, comme le prévoit la section 7) ; textes de T0.6 le 11 novembre ; réserve et évaluation scellées ; contre-vérification à l'aveugle par un lecteur d'une autre lignée ; scellement et `provenance-v2.md`. Dans les dossiers : les remises de J-D, J-A et J-C sont réparties sur `…-brouillon1/taches/` (r01–r07 inchangées), `taches/` (r00, r08–r17), `remises-completes/` (r18–r31), `remises-jc/` (J-C, r00–r31) ; la liste d'assemblage utilisée est celle de la commande du journal.
