# Notice — module des autres moniteurs et de la lecture commune du bras A, version 10 — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `reponses-sans-interne-demandes-v8-v3.md`, même dossier.

Écrit par le développeur habilité neuf côté moniteurs, le 20 novembre 2026, sur les corrections de la contre-lecture habilitée de la version 9 (`contre-lecture-habilitee-autres-moniteurs-v9-v1.md`, `517fecb3a04f4d67de2155ef9ed21c231856c889c2465544cd2450ea8a58c25e`, verdict « conforme après ces corrections »), commandées par la mère sous GO-2026-11-20-21 (mandat v2, `8c60bfe7…`). Classe B. **Se lit avec la notice de la version 9** (`notice-developpeur-habilite-autres-moniteurs-v9-v1.md`, `fe28737d1d2465e7e1280c950a7ba70fafecf774f74ed8476e30d66542002cc4`), dont tout reste vrai sauf ce qui est dit ici. La version 9 (commit `92842ac54`) reste intacte. Aucun résultat lu, aucun poids chargé, aucune dépense. Ni commit ni poussée. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 10 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v10.py` | `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v10.py` | `75ef245065ae8407eed36d50290e3ffbef4065de6462e0830f41b5efda374537` |
| épreuve par retrait : script | `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-autres-moniteurs-v10-v1/passage_mutations_v10.py` | `c39cc55a59e4228d572a0d8d0c5a918f82383a6d59e736d51eee4f767a1b8676` |
| épreuve par retrait : relevé | `…/epreuve-par-retrait-autres-moniteurs-v10-v1/mutations-v10-resultats.md` | `d8eef9e2f5aedecf647bf02de75411897f779ca35ffd577a106d30583a9dd0aa` |
| épreuve de forme : script | `scripts/bras_a_v2_habilite_epreuve_de_forme_v10_v1.py` | `41a377e6e455deeee767e712fa027214f0942737700f8d5fe0e76a63f185d130` |
| épreuve de forme : sorties | `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v10-v1/` | partie 4 |

Essais : `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v10.py` ; dernière ligne : `77 passed in 351.80s (0:05:51)`.

## 2. Corrections (partie 6 de la contre-lecture) ; aucun calcul ne change

| correction | version 10 | essais |
|---|---|---|
| 1. forme de `comptes_des_lectures` | `exiger_comptes_des_lectures` : les deux moniteurs à modèle de langue ; par moniteur, une entrée par condition lue ; par condition, les cinq clés de `comptes_des_lectures`, dans leur ordre, des entiers ; les tables des états de la balise et des jointures n'ont pour clés que des éléments de leurs listes fermées | `_gardes_de_la_sortie` (six artefacts), `test_l_assemblage_garde_la_sortie_lui_meme` |
| 1. forme de `preuve_d_ordre` | `exiger_preuve_d_ordre` : par moniteur, une date au format du journal et l'empreinte de ses scores, de soixante-quatre signes pour les trois moniteurs lus sur des scores, nulle pour les deux moniteurs appris ; l'engagement de la table, soixante-quatre signes | `_gardes_de_la_sortie` (cinq artefacts), `test_l_assemblage_…` |
| 2. épreuve de forme | refaite : le fichier par unité porte les cinq moniteurs, l'agrégateur à l'unité de l'épisode ; exclusions, comptes des lectures, table des identifiants et preuve d'ordre faits par les fonctions du module | partie 4 |
| 3. borne haute au cas A | un flottant de 0 à 1 (un nombre non fini est refusé) | `_gardes_de_la_sortie` (quatre artefacts : 1,5 ; infini ; non-nombre ; −0,1) |
| 3. gardes sans morsure | garde à l'assemblage : artefacts propres, qui ne passent que par l'assemblage ; refus d'un nombre non fini à l'écriture : arrêt de garde nommé (« un nombre non fini ne s'écrit pas »), éprouvé garde de forme retirée | `test_l_assemblage_garde_la_sortie_lui_meme`, `test_un_nombre_non_fini_ne_s_ecrit_pas` |
| 4. `nombres_rendus` | trois phrases récrites : valeur de la famille (valeur p haute, 1 aux cas B et C), borne et quantile au seul cas A, motif en liste fermée ; comptes de la règle du 1 % selon le cas ; « le score ou le rang » selon la forme du fichier par unité | `test_nombres_rendus_de_la_version_10` |

Le texte libre ne passe plus par ces deux champs. La garde du chemin en clair garde un artefact qui ne passe que par elle : une clé de pli qui a la forme d'un chemin.

## 3. Inscrit, à la demande de la mère

- **`calculable` vaut vrai aux cas A, D et E, faux aux cas B et C.** La table des formes du texte ne fixe pas la valeur aux cas D et E et dit que ce champ n'entre dans aucune règle de jugement ; vrai est retenu parce que l'aire et les valeurs p y sont rendues (contre-lecture, partie 3, point 1).
- **La garde statique des essais de la version 8 échoue, et celle des essais de la version 9 aussi, parce que leur liste ignore les versions suivantes** : le fichier d'essais v8 ne connaît pas `autres_moniteurs_v9.py` et le fichier v9 ne connaît pas `autres_moniteurs_v10.py`. Ce n'est pas une régression : chaque version neuve refait cet échec dans le fichier d'essais de la précédente. Les essais de la version 10 portent leur propre liste et passent.

## 4. Épreuve de forme, refaite (demande 17)

Construction : voir l'en-tête du script. Fichier par unité : les cinq moniteurs, l'agrégateur sans pas (unité de l'épisode). Les deux moniteurs appris sont lus sur les scores du moniteur boîte noire, par la fonction du module, et rangés sous leurs noms ; le juge ne lit qu'une action sur deux ; au cas C, les permutations perdues sont injectées.

| sortie | chemin, sous `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v10-v1/` | empreinte | lignes du fichier par unité |
|---|---|---|---|
| cas A | `cas-a/lecture-commune-moniteurs-bras-a.json` | `665ec2343cca430e078a2dbc3a2597517e063111ab7c8a745528a523283c4737` | 8 192, cinq moniteurs |
| cas B | `cas-b/lecture-commune-moniteurs-bras-a.json` | `1acc3688d8ca029134bd582ac78309400cd45464ba0483cf9328f9943e27de92` | 6 144, cinq moniteurs |
| cas C | `cas-c/lecture-commune-moniteurs-bras-a.json` | `444d640cbf3460f4eece57e1b29b6b362ef81e37a1183440d69dedf8294239f4` | 8 192, cinq moniteurs |
| cas D | `cas-d/lecture-commune-moniteurs-bras-a.json` | `ba19720b294f9f8711b85ea0666a5dcf2f2d88a1b3a238bdfae6ac9414dd3053` | 1 536, cinq moniteurs |
| cas E | `cas-e/lecture-commune-moniteurs-bras-a.json` | `609faf0508e80b25f531fd4ec54191757e6308ed0138774b2f56c0675ed1a6bd` | 1 024, cinq moniteurs |
| cas A, une valeur p haute arrondie à quatre décimales (à refuser) | `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | `33249e747607aeb5fd07538d1a2423a4e6f069767631295557dca59ca6aae47e` | celui du cas A |

## 5. Épreuve par retrait

67 retraits listés, joués un à un sur la version 10, essais ciblés après chaque retrait : **65 mordent sur 65 joués**. Les 9 retraits neufs de la version 10 mordent tous : les trois gardes des comptes des lectures, les trois de la preuve d'ordre, la borne de 0 à 1, et les deux que la contre-lecture de la v9 avait vus sans morsure (garde à l'assemblage, refus d'un nombre non fini). Les 56 retraits repris de la v9 qui s'appliquent encore mordent aussi. Deux retraits de la v9 ne sont pas joués, leur texte n'existant plus : les deux anciennes gardes de premier niveau de la preuve d'ordre et des comptes, remplacées par les fonctions neuves, dont les retraits sont parmi les neuf. Le module est remis à l'identique après chaque retrait ; son empreinte, vérifiée à la fin, est celle de la partie 1. Les sept retraits de la contre-lecture de la v9 ne sont pas rejoués ici.

## 6. Réserves, pour le contre-lecteur

- Les remarques de la contre-lecture sans correction exigée restent ouvertes : l'empreinte du module est calculée sur le fichier à l'assemblage, non à l'import ; la lecture commune scelle le fichier par unité avant la garde et l'écriture de la sortie (à dire dans la règle de reprise du lanceur).
- Au cas B de l'épreuve, les deux champs de l'agrégateur valent nul à chaque dose (aire non calculable), forme admise.
- Écart de méthode pendant cette version : une vérification de syntaxe a été passée en ligne à l'interpréteur (`python -c`), contre la règle du mandat ; aucun refus, rien d'écrit par elle.
- Restent non faits, comme en version 9 : le lanceur (demande 18) et la note sur le lanceur du bras.
