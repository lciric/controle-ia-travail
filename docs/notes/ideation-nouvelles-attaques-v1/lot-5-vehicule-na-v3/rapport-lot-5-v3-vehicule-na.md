# Rapport du développeur — véhicule NA-1, lot 5 v3 (registre des tentatives, registre servi et passeport marqués `par_repli`) — v1

Développeur du lot 5 v3 du véhicule NA-1, modèle O, et auteur de la v2. Écrit le 2026-11-22. Aucun appel de modèle, aucun
réseau, aucune dépense ; données factices seules ; rien d'écrit dans un dépôt. Dossier :
`/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/vehicule-na-lot-5-v3/`.

## 1. Verdict

La v3 tient l'erratum 2 (`erratum-2-interface-lots-5-6-7-repli-v1.md`), sur ses points (a), (b) et (d) :
- **(a)** la classe « refus » s'applique aux trois tentatives d'une chaîne de trois refus ;
- **(b)** un refus suivi d'une tentative sans réponse prend la classe de défaut, jamais « servi par repli » ;
- **(d)** chaque fiche du registre servi porte un champ fermé `par_repli`, et le passeport du portier aussi.

Résultats : **137 essais passent ; 68 mutations sur 68 sont tuées**, témoins conformes. **Le banc reste sur doublures
déclarées des lots 1 à 3**, comme en v2 ; un vérificateur doit rejouer sur une copie réelle (§ 5).

## 2. Livrables (noms neufs, R12 ; la v2 n'est pas touchée)

| fichier | rôle |
|---|---|
| `paquet/orchestrator/pole/registre_na_v3.py` | registre des tentatives et registre servi marqué (495 lignes) |
| `paquet/orchestrator/pole/verifier_registre_servi_na_v3.py` | vérification du registre servi marqué (arrêts n° 8, 9, 19) |
| `paquet/orchestrator/pole/portier_na_v3.py` | portier du v1 enveloppé, passeport marqué |
| `paquet/orchestrator/essais/aides_na_lot5_v3.py`, `test_na_lot5_v3_registre.py`, `mutations_na_lot5_v3.py` | aides, 137 essais, 68 mutations |
| `jouer_banc_lot_5_v3.py` | banc : vérifie les modules v1 contre le manifeste v1, pose le paquet v3, joue les essais |
| `banc-doublures/orchestrator/pole/*.py` | doublures déclarées ; celle de `requete_na_v3` gagne un assemblage réduit pour le portier |
| `journal-essais-na-lot-5-v3.txt`, `journal-mutations-na-lot-5-v3.json` | journaux |
| `table-empreintes-dossier-na-lot-5-v3.txt` | table d'empreintes ; un compagnon `.sha256` par fichier livré |

## 3. Ce que le code porte

- **(a)** est gardé de la v2 : les trois tentatives d'une chaîne de trois refus portent la classe « refus du modèle »
  (`_clore`).
- **(b)** (`registre_na_v3.py`, l. 287) : quand la chaîne finit sans réponse, chaque refus qui précède la dernière tentative
  doit porter la classe de défaut, « réponse illisible » (V9, l. 99, comme l'erratum 1, point 3). La classe de repli y est
  refusée. Au niveau de la ligne, la classe de défaut est admise avec `refusal` (l. 186). La cohérence est vérifiée au
  niveau de la chaîne :
  - la classe de défaut avant une tentative servie est refusée ;
  - elle est refusée aussi dans une chaîne de trois refus.
- **(d), registre servi** (`fabriquer_registre_servi_v3`, l. 457 ; `_marquer`, l. 446) :
  - on part du registre servi du v1, sur les seules lignes `fiche`, avec le même ordre et les mêmes comptes ;
  - chaque ligne de tentative passée y reçoit un champ fermé, placé entre la classe et l'énoncé :
    `tentative : <nom> ; <f1> ; <f2> ; <f3> ; passée ; par_repli : vrai|faux ; <énoncé JSON>` ;
  - la marque est `vrai` pour une fiche rendue par une tentative de rang 1 ou 2 ;
  - `marques_par_repli` (l. 473) rend les noms marqués, pour la lecture qui les retirerait après coup ;
  - retirer le champ rend, octet pour octet, le registre servi du v1.
- **(d), vérification** (`verifier_registre_servi_na_v3`) :
  - le champ absent ou hors liste est un défaut de l'arrêt n° 19 ;
  - la borne (arrêt n° 8) se contrôle sur le fichier servi, marques comprises ;
  - tous les autres contrôles sont ceux du v1, sans qu'aucun motif soit réécrit ;
  - l'exception est une sous-classe de celle du v1, donc le lot 6 l'attrape sans changement.
- **(d), passeport** (`portier_na_v3.py`) :
  - le classement du v1 est repris sans changer une ligne ;
  - le dictionnaire du noyau doit porter `par_repli`, un booléen ; absent ou d'un autre type, il est refusé, jamais deviné ;
  - le `PasseportV3` porte la marque, `exiger_passeport` le rend, et l'arrêt A17 est inchangé ;
  - le compte `passeports_par_repli` s'ajoute aux comptes.
- **Ancien format** : une ligne ou un fichier du lot 5 v1 ou du lot 5 v2 lève `RegistreAncienFormat`, avec un message qui le
  dit.

## 4. Différence avec la v2

| | v2 (`registre_na_v2`, `84c87c38…`) | v3 |
|---|---|---|
| refus puis sans réponse | refus « servi par repli » exigé | **classe de défaut exigée ; « servi par repli » refusé** |
| version de ligne | `registre-tentatives-na-v2` | `registre-tentatives-na-v3` ; une ligne v2 est dite ancien format |
| registre servi | v1 à l'octet, sans marque | **v1 plus `par_repli` sur chaque ligne passée** ; `fabriquer_registre_servi_v3`, `marques_par_repli` |
| vérification | `verifier_registre_servi_na_v1` | `verifier_registre_servi_na_v3` (marque, borne sur le fichier servi, puis le v1) |
| passeport | `portier_na_v1.Passeport` | `portier_na_v3.PasseportV3` (`par_repli`) ; `appeler` rend `par_repli` |
| noms | `RegistreTentativesV2`, `lire_…_v2`, `garde_du_coffre_v2` | `…V3`, `…_v3` ; la garde du coffre est inchangée en fond |

Tout le reste est identique à la v2 : `type_ligne`, les listes fermées, les trois fins, (a), le comptage sur les seules
lignes `fiche` et `categorie_refus` à `null`.

## 5. Essais et réserves

- **Sain et artefact (R5)** :
  - pour (b) : un cas sain, quatre artefacts (dont un fichier v2) ;
  - pour (d), registre servi : deux cas sains, cinq artefacts ;
  - pour (d), passeport : trois cas sains, quatre artefacts.
- **Mutations** : 14 sont neuves (M3-01 à M3-14), les 54 de la v2 sont gardées. Une première passe a laissé M3-12 non tuée :
  la marque est gardée deux fois dans le portier, et la mutation n'en retirait qu'une. J'ai élargi la mutation aux deux
  gardes (garde en profondeur, code inchangé), puis rejoué entièrement.
- **Rejeu sur copie réelle**, à faire par le vérificateur :
  1. `python -B jouer_banc_lot_5_v3.py BASE BANC JOURNAL` sans `--doublures`, sur une copie où les lots 2 v5, 3 v3 et 5 v1
     sont posés ;
  2. puis `essais/mutations_na_lot5_v3.py`.

  Les essais du portier v3 appellent `requete_na_v3.assembler_portier_fiche` : la doublure n'en a qu'une forme réduite,
  donc ce chemin est le plus exposé au rejeu réel.
- **Ce que la lettre ne fixe pas** :
  - la forme du champ dans le registre servi (`par_repli : vrai|faux`, après la classe) est la mienne ;
  - la garde de motifs du lot 2 ne l'a pas lue ;
  - la clé `par_repli` de l'issue d'appel est une interface neuve pour le lot 6 v4 ;
  - (c) est un écart que l'additif doit déclarer ;
  - (d) est une décision provisoire de la mère, soumise à Fable et à Lazar.

## 6. Règles tenues

J'ai lu par chemin complet : ma liste fermée, les errata 1 et 2, et ma v2. J'ai lu `verifier_registre_servi_na_v1` en deux
tranches de moins de 150 lignes. Je n'ai listé que mes dossiers de sortie et rien lu sous `/root/.claude/`. Aucun refus
d'outil ni de classifieur.
