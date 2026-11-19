# Différences entre le brouillon 1 et le brouillon 2 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 1 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon1.md`, empreinte `9851ec3d6ccaef84d00621bcbfbb3558f99dc7a56709782122dc1fa5e5b0f1cb`.
- Rapport du contre-lecteur neuf (Opus 5.5) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon1-v1.md`, empreinte `f679ea3d9528265ad55934e529fc8d4c1e23d7532fb794e7b18d0cb4b6d3d552`.
- Brouillon 2 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon2.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 vers 00:02Z (`date -u`).
- Le rapport numérote 37 remarques (1 à 6 bloquantes, 7 à 30 à corriger, 31 à 37 mineures) ; le mandat en annonçait 30 : les 37 sont traitées ci-dessous.

## 1. Une ligne par remarque du contre-lecteur

| n° | objet | état | où, dans le brouillon 2 ; ou raison |
|---|---|---|---|
| 1 | champs ouverts invisibles pour le validateur | traitée | « Champs ouverts qui bloquent le scellement » : chaque état ouvert porte le marqueur que `prereg.problemes` refuse ; règle « la mère vérifie que la liste est vide » ; essai sur cas sain et artefact exigé. Essai joué par le rédacteur sur des copies : texte rempli → liste vide ; un seul champ ouvert → message |
| 2 | issue des audits sans verdict | traitée | « Critères de lecture gelés » : lignes AU-a et AU-b, liste fermée des défauts D1 à D5 |
| 3 | seuil du « trop beau » mal attribué | traitée | Vérifié par le rédacteur : ligne 1378 du texte des sondes v0 = « saturation » d'une aire de validation générique, constat ; ligne 1928 = déclencheurs de l'audit. « Seuil » : déclencheurs d1 à d4 repris de la ligne 1928 ; 0,99 retiré |
| 4 | pas de repli si sondes ou planchers manquent | traitée | « Choix des sondes et des couches » : table des identités et règle mécanique ; fichier absent ou d'empreinte différente → sonde « sans objet », jamais un choix (consigne de la mère). Le niveau reste 98,33 % (et non 0,9875 : trois sondes, option (a1)) |
| 5 | familles non linéaires | traitée | « Métrique », dernier point : lecture décisive bornée aux trois sondes linéaires ; descriptif B8-P5 borné à la même famille ; perceptron, attention et Mahalanobis : aucune lecture définie, les noter est un écart. Artefact de A0 (ii) : le vecteur w |
| 6 | champs qui bloquent à tort ; code de la lecture | traitée | « Conditions de départ » (D-1 à D-9) séparées des champs bloquants ; « Code : lignes de registre et contrôle de conformité » : scellement avant le code, lignes `CODE-…`, contrôle de conformité, refus mécanique (décision de routine de la mère, selon son complément) |
| 7 | mot « confirmé » de L1 | traitée | Table des issues, L1 |
| 8 | validité de la sonde de dissimulation | traitée | « Hypothèse », point « Validité de la sonde de dissimulation » ; « Autres combinaisons » |
| 9 | règle du témoin-jumeau ambiguë | traitée dans sa forme actuelle | « Règle du témoin-jumeau (forme actuelle, sans ambiguïté) ». L'option plus stricte n'est pas adoptée (consigne de la mère) : décision pour Lazar |
| 10 | ligne L6 sans source ni chemin | traitée | L6 : toute action sans activité → non concluant ; plan, point 2 ; garde P3 étendue à la fenêtre du modèle |
| 11 | audit A2 sans source, audits non symétriques | traitée | Un seul audit, même contenu ; déclencheur du négatif : aire inférieure à 0,05 (ligne 1928) ; « 0,01 de 0,5 » retiré |
| 12 | essai A0 (i) : niveau, plan, graine | traitée | A0 (i) : niveau décisif, règle selon I-8, clé `sain/<sonde>` |
| 13 | portée de A0 (ii) ; artefact d'alignement ; un seul jeton | traitée, avec une adaptation | Renommé « essai de la chaîne de lecture » ; un seul jeton ; A0 (iii) artefact d'alignement. Adaptation : la permutation des clés se fait entre actions de `H` d'une même tâche, pas entre conditions, pour que l'essai ne lise aucune condition sabotée avant la lecture décisive |
| 14 | placebo | traitée | B8-P4 et « Métrique » : seulement pour les sondes au-dessus, niveau décisif, tous les épisodes de la tâche, 200 permutations avec source |
| 15 | prédicteurs triviaux | traitée | B8-P7 et « Métrique » : grandeur comparée écrite, longueur du contexte ajoutée ; base « coût seul » : B8-P9, conditionnelle à I-10 et I-4 |
| 16 | bras « moyenne » pour toutes les familles | traitée | B8-P6 : défini pour les trois sondes lues (toutes linéaires) ; la question des autres familles ne se pose plus |
| 17 | étiquette par épisode | traitée | F-7 par fraction (1, ½, ¼) ; B8-P8 décidée maintenant, conditionnelle à I-11 ; L2 « à fraction d'actions sabotées inconnue » |
| 18 | demi-précision | traitée | « Passe », précision : `float16` standard, classe `ActivationsDemi` citée avec empreinte ; écart de quantification écrit au manifeste, sans seuil |
| 19 | branche « I-6 dit oui » | traitée | « Passe », contextes et identifiants : identifiants consommés tels quels ; passe conduite par un agent déjà exclu ; lecture dite « organisme instruit » |
| 20 | ordre non scellé | traitée, avec une adaptation | Condition de départ D-6 et liste d'arrêt 16. Adaptation : la comparaison à l'ordre scellé est une condition de départ, et se fait avant le scellement seulement si l'ordre est scellé le premier (le texte doit pouvoir être scellé avant la première sortie de la course même si l'ordre tarde). Fermeture de la condition « test de transfert » : « Ce que ce texte est » |
| 21 | citation de N-056 | traitée | « Passe », couches : « par analogie déclarée » |
| 22 | avantage de l'option (b) surestimé | traitée | Option (a3) : « dépend quand même du fichier des planchers à 800 directions » |
| 23 | option « seules les couches lues » | non adoptée, portée à Lazar | Consigne de la mère : ne pas l'adopter ; listée comme décision pour Lazar dans le rapport de remise ; l'inconvénient est écrit sous (a1) |
| 24 | niveau si moins de sondes lues | traitée | « Seuil » : 98,33 % dans tous les cas |
| 25 | combinaisons non couvertes | traitée | S5 ; I-9 étendu à la liste fermée des états ; règle « hors liste → non jugée » ; la garde des tirages tient lieu d'effectif minimal (écrit) |
| 26 | audit mené par le juge | traitée | « Qui lit, qui juge » : auditeur neuf, ni lecteur, ni juge, ni auteur |
| 27 | scellement tardif | traitée | « Ce que ce texte est » ; liste d'arrêt 14 : écart, nœud de Lazar |
| 28 | liste des exclus mouvante | traitée | D-5 et « Qui lit, qui juge » : chemins et empreintes dans les mandats, recopiés par le verdict ; lecteur des lectures (1) et (2) exclu |
| 29 | source de la règle « condition jugée » | traitée | « Seuil » : étape T2 de la note (ligne 84) en source, N-063 v2 en précédent, effet de D-7 écrit |
| 30 | recette de la puissance | traitée | Plan, point 10 ; F-7 n'est plus qu'un nombre à verser |
| 31 | heure de fin du brouillon 1 | traitée | En-tête |
| 32 | « mot » au lieu de « texte de la ligne » | traitée | En-tête, accords |
| 33 | nombres sans source à l'endroit | traitée | « Métrique » : 2 000 tirages (ligne 1194), 200 permutations (ligne 1217), 10⁻¹² (`plancher_v3`, ligne 39) |
| 34 | opérationnalisation partielle | traitée | « Hypothèse », renvoi au programme |
| 35 | modèle et révision des sondes | traitée | « Hypothèse », hypothèse de travail 1 |
| 36 | clés de graines | traitée | Plan, point 5 |
| 37 | formule sur la liste des exclus | traitée | En-tête, auteur |

Remarques non traitées : aucune. Deux ne sont pas adoptées telles quelles et vont à Lazar (9, pour son option plus stricte ; 23). Deux sont traitées avec une adaptation déclarée (13, 20).

## 2. Changements de la propre initiative du rédacteur, ou sur consigne de la session mère

1. **Option (a1)** (consigne de la mère, par anticipation sous GO-2026-11-18-61) : trois sondes au lieu de quatre, niveau 98,33 % ; la sonde du domaine sort de tout critère ; la seconde écriture « sondes génériques seules » et la combinaison « porté par la seule sonde du domaine » sont retirées.
2. **Clé du texte** `LECTURE-SONDES-BARREAU8-V1` et clés des lignes de code `CODE-LECTURE-SONDES-BARREAU8-V1`, `CODE-PASSE-BARREAU8-V1` : noms choisis par le rédacteur.
3. **F-8 fermé par une règle** : décalage de 2 écarts-types des scores d'action sur `H`, sur un seul jeton. Choix du rédacteur, déclaré, sans source.
4. **Recette de la puissance** : grille d'aires, fractions, 1 000 répétitions, seuil de 80 %, effet de tâche d'écart-type 0,5. Choix du rédacteur, déclarés, sans source.
5. **F-9 fermé** par le chemin et l'empreinte du verdict du témoin positif planté et de sa pièce d'issue, transmis par la mère ; le rédacteur ne les a pas ouverts ni n'a vérifié leur empreinte.
6. **Défaut D5 de l'audit** (plancher qui sépare le témoin-jumeau de l'honnête) : ajouté par le rédacteur, sur l'argument de la remarque 3.
7. **Ligne L3 élargie** : un état U sans règle du témoin-jumeau tenue rend « non tranché » (c'était une combinaison au brouillon 1).
8. **Garde P0** ajoutée à la passe (texte scellé, ligne de code, accord).
9. **I-4, I-6, I-7, I-9, I-11 précisés** (champ de coût, réponse par oui ou non, fenêtre du modèle, liste fermée des états, marque binaire).
10. **Garde P6** : reprend la règle de `ActivationsDemi` (arrêt avant le stockage) au lieu de « avant et après la conversion ».
11. **B8-P2** : le contraste `B50` contre `TJ100` est rapporté en plus de `B100` contre `TJ100`.
12. **Définition de l'état N** précisée : « toutes celles qui sont au-dessus sont non interprétables ».

## 3. Champs ouverts

- Bloquent le scellement : 15 (I-1 à I-12 ; F-3, F-6, F-7).
- Conditions de départ, ne bloquent pas le scellement : 9 (D-1 à D-9).
- Fermés depuis le brouillon 1 : F-1, F-2, F-8, F-9. Passés en conditions de départ : F-4, F-5, F-10, F-11, F-12, F-13.
