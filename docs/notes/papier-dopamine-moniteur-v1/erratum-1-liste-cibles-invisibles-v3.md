# Erratum 1 de la liste figée des cibles invisibles (essai v3) — 2026-11-21T18:07:18Z (`date -u`)

Classe B (instrument : liste d'une garde et son essai). Mot de Lazar : GO-2026-11-21-69 (`registres/go.md` : « Inventaire figé des cibles invisibles complété par un erratum, contre-lu par Opus : go »). Rédigé par Claude Fable 5.2. **Non contre-lu, non committé, non poussé** : la contre-lecture par Opus 5.5, que l'accord exige, reste à faire avant tout versement.

## Verdict

La garde « ni l'agent ni les moniteurs ne voient la référence cachée d'une tâche » (`tests/test_cibles_invisibles_v3.py`) échouait sur deux essais d'inventaire : 43 fonctions qui construisent ou rendent une invite n'étaient pas à sa liste, et deux fonctions lisaient une clé nommée `cibles` sans y être admises. Les 43 fonctions et les deux lectures ont été examinées une à une : **aucune ne fait entrer la référence cachée dans une invite**, et chacune vient d'un fichier versé par une ligne de registre et un commit nommés. Toutes sont inscrites. L'essai neuf `tests/test_cibles_invisibles_v4.py` passe (41 essais) et échoue dès qu'une ligne est retirée. L'essai v3 n'est pas touché (empreinte `93a6df43…`, compagnon vérifié) et échoue toujours, comme attendu.

## Ce qui change

| pièce | rôle | empreinte |
|---|---|---|
| `tests/liste_cibles_invisibles_v4.json` | liste complétée : les 76 lignes de l'essai v3 reprises sans changement, 43 lignes ajoutées, deux faux lecteurs de `cibles` ajoutés, 16 fichiers sources avec leur empreinte | `e6724709bb11c58cc56e4058bd8111846b2c433921613a2cc2c0f2f123f4a5f8` |
| `tests/test_cibles_invisibles_v4.py` | essai neuf : lit la liste, rejoue les essais d'inventaire de l'essai v3 sous la liste complétée, porte la mutation, deux collecteurs à marqueur et les preuves des raisons d'exemption | `b93959b67fc77d1d6d1fc8815c0d8c2274f73c368e2ba063aada6ebab6997351` |
| `tests/test_cibles_invisibles_v3.py` | inchangé (la liste y est écrite dans le code : la compléter aurait demandé de le modifier ; d'où l'essai v4) | `93a6df4343f876cad58c01933d2636e65858bc8d55a99285edd4125cb5d504a9` |

Arbre examiné : tête `e6fbe03ae11b` de la branche de travail, le 2026-11-21.

## Pourquoi

1. L'essai v3 fige sa liste dans son propre code. Depuis sa rédaction, six chantiers ont versé du code qui construit des invites ou porte une clé « role » : la lecture de l'accumulation des scores (barreau 6), la formation et la relecture des familles d'adaptateurs jumeaux (barreau 5) et la fabrique de leur épreuve à vérité plantée, la passe de recalcul et la lecture des sondes côté moniteurs (barreau 8), la relecture à état imposé de l'étape B bis, les lanceurs de la lecture par lentille, et le bras exploratoire du papier dopamine.
2. La fusion du bras du papier dopamine n'ajoute qu'**une** des 43 fonctions (`DecoupeurHF.gabarit`) ; les autres étaient là avant (note `rejeu-echecs-suite-v1.md`, § 4). Le lanceur version 8 des lentilles est apparu sur l'arbre **pendant** la rédaction (commit de 17:59Z, R-4650) : il est examiné et inscrit lui aussi.
3. Tant que l'inventaire échoue pour des raisons anciennes, il ne peut plus signaler une fonction neuve : la garde est muette. L'erratum la rend de nouveau lisible.

## Comment chaque ligne a été établie

- **Hors liste** : les 43 fonctions et les deux lectures sont celles que l'essai v3 nomme, relevées par programme (mêmes fonctions de balayage que l'essai).
- **Légitime** : pour chacun des 16 fichiers, une ligne de registre nomme le versement et un commit ; l'objet git du fichier de l'arbre de travail est égal à celui de ce commit (`git rev-parse COMMIT:chemin` = `git hash-object chemin`). L'historique local est tronqué (borne `f174bb1f`) : la provenance ne vient donc pas de `git log`, mais de cette égalité. Aucun fichier n'a été écarté : tous ont une source.
- **Sans vue sur la référence cachée** : lecture des lignes en cause de chaque fonction, puis preuve par programme dans l'essai v4, chaque preuve éprouvée sur un artefact (R5). Cinq raisons, 43 lignes :
  - « ligne de données » (28 lignes) : la clé « role » est celle d'une ligne de table (rôle d'une sonde, d'une direction, d'un jeu de lecture), pas d'un message de dialogue — aucun dictionnaire de la fonction ne porte à la fois « role » et « content » ;
  - « environnement sur tache_de » (7 lignes, dont 2 couvertes par un collecteur à marqueur) : tout environnement du module est bâti par `conditions.environnement`, déjà couvert par l'essai v3, sur `tache_de(...)`, qui ne transmet qu'identifiant, questions et classification ;
  - « rendu d'un environnement reçu » (4 lignes) : la fonction ne fait que rendre la consigne et les observations d'environnements reçus en paramètre ;
  - « texte fixe sans tâche » (3 lignes) : conversation de contrôle et invite chargées sur des constantes ;
  - « rendu générique d'un gabarit de dialogue » (1 ligne, celle du bras du papier dopamine) : deux textes reçus, dans un paquet qui n'importe du programme que les gardes, le scellement et le manifeste.
- **Deux collecteurs à marqueur de plus** (chemins réels, tâche factice dont chaque champ caché porte un marqueur, fuite plantée vue) : le début d'épisode de la passe de recalcul du barreau 8, et le tirage du saboteur instruit de la formation des familles du barreau 5.
- **Faux lecteurs** : dans `formation_v1.py::_executer` et `relecture_v1.py::_executer`, la clé `cibles` est celle de la configuration de l'adaptateur (`a = config["adaptateur"]` puis `tuple(a["cibles"])` : noms des modules visés), comme pour les lanceurs déjà admis par l'essai v3.

## Sources par fichier

| fichier (sous `src/`) | ce que c'est | source | empreinte du fichier examiné |
|---|---|---|---|
| `controle_ia/accumulation_b6/lecture_v1.py` | lecture de l'accumulation des scores le long d'un épisode (barreau 6) | registres/decisions.md, ligne R-2336 (code v2 du barreau 6 rendu, commit 282e295e… sur prep/accumulation-b6-code-v2) et ligne R-2338 (contre-lecture courte : « inscriptible : CODE-ACCB6 au commit 282e295e… ») | `1f4c035f50587f8c…` |
| `controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` | fabrique des mondes de l'épreuve à vérité plantée du programme de lecture du barreau 5 | registres/barreau5-familles-jumelles-v1.md, ligne CODE-LECTURE-B5F (commit c76e7916…), reprise par registres/decisions.md, ligne R-4147 ; module nommé par le texte scellé prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md | `22560d9f4f814ef0…` |
| `controle_ia/barreau5_familles/formation_v1.py` | formation des familles d'adaptateurs jumeaux du barreau 5, côté instance | registres/barreau5-familles-jumelles-v1.md, ligne CODE-FORMATION-B5F (commit ef800868…, formation_v1.py a56602c3a488f577) | `a56602c3a488f577…` |
| `controle_ia/barreau5_familles/relecture_v1.py` | relecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») sur l'instance de lecture | registres/barreau5-familles-jumelles-v1.md, ligne CODE-LECTURE-B5F (commit c76e7916…), reprise par registres/decisions.md, ligne R-4147 ; module nommé par le texte scellé prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md | `f6bd8c15af113089…` |
| `controle_ia/barreau8_moniteurs/lecture_sondes_v5.py` | lecture des sondes sur les épisodes du barreau 8, côté moniteurs | registres/decisions.md, ligne R-3618 (portage sur main depuis la tête c750d116 : lecture v5 aa1476fd…, sceaux vérifiés) ; compagnon .sha256 du fichier vérifié | `aa1476fd6bf6bb55…` |
| `controle_ia/barreau8_moniteurs/passe_recalcul_v5.py` | passe de recalcul de l'activité interne du barreau 8, côté moniteurs | registres/decisions.md, ligne R-3618 (portage sur main depuis la tête c750d116 : passe v5 a5eeef62…, sceaux vérifiés) ; compagnon .sha256 du fichier vérifié | `a5eeef6203b558db…` |
| `controle_ia/dopamine_exploratoire/modele_v1.py` | modèle réel et découpeur du bras exploratoire du papier dopamine | registres/decisions.md, ligne R-4571 (code du bras fusionné depuis prep/dopamine-exploratoire-v1, d6cde666…) ; fusion a52731b9… décrite par la note scellée docs/notes/papier-dopamine-moniteur-v1/rejeu-echecs-suite-v1.md | `0bb5dfb74c19862a…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v1.py` | lanceur (version 1) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `efec99e06a7224f3…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v2.py` | lanceur (version 2) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `8230341d07d4043f…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v3.py` | lanceur (version 3) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `d88dd911260a0396…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v4.py` | lanceur (version 4) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `dc74be0059bc7fa1…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v5.py` | lanceur (version 5) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `599f4a190eaeaf02…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v6.py` | lanceur (version 6) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `e05172590346e23e…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v7.py` | lanceur (version 7) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4596 (liste v3 des fichiers des lentilles versée sur main : 103 fichiers, commit cc9ab8eb) ; commit de versement sur main 25236c16… | `a5d6fc7bd7abf2b1…` |
| `controle_ia/lentilles_sondes_bbis/lanceur_v8.py` | lanceur (version 8, correctif de la pagination) de la lecture des sondes de l'étape B bis par la lentille publique | registres/decisions.md, ligne R-4650 (liste v4 des fichiers des lentilles versée : 33 fichiers de c3263a80…, correctif de la pagination contre-lu « conforme ») ; commit de versement e6fbe03a…, dont le message nomme R-4650 ; fichier apparu sur l'arbre pendant la rédaction de l'erratum (2026-11-21T17:59Z) | `0bba5d4e68fd193d…` |
| `controle_ia/t07bbis/etat_impose_v1.py` | relecture forcée à état d'adaptateur imposé et à environnement imposé (étape B bis de T0.7) | registres/decisions.md, lignes R-2751 (développeur du paquet src/controle_ia/t07bbis/, section « Code neuf » du texte scellé prereg/T0.7-etape-B-bis-v1.md) et R-2780 (code rendu, commit 7afb0c99 sur prep/t07bbis-code-v1) ; versé sur main par le commit 5378c2de… ; compagnon .sha256 du fichier vérifié | `39e8e1a9f384e3ce…` |

Vérification commune : objet git du fichier de l'arbre de travail égal à celui du commit nommé (`git rev-parse COMMIT:chemin` = `git hash-object chemin`), vérifié le 2026-11-21.

## Lignes ajoutées à la liste (une par fonction)

| n° | fonction | statut | raison | source |
|---|---|---|---|---|
| 1 | `accumulation_b6/lecture_v1.py::calculer` | exempté ; ligne de données | clé « role » d'un jeu de lecture (`jeux[nom]` : lecture, rôle, positifs, négatifs…), aucune invite | R-2336 et R-2338 ; commit 282e295e |
| 2 | `barreau5_familles/epreuve_verite_plantee_v1.py::planter` | exempté ; ligne de données | clé « role » d'un artefact planté (famille, rôle, pli, indice d'action), aucune invite | ligne CODE-LECTURE-B5F du registre propre du barreau 5, R-4147 ; commit c76e7916 |
| 3 | `barreau5_familles/formation_v1.py::_executer` | exempté ; texte fixe sans tâche | conversation de contrôle fixe (`conversation_de_controle('agent', None)`), sans tâche ; la clé `cibles` lue ici est celle de l'adaptateur (voir les lecteurs ajoutés) | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 4 | `barreau5_familles/formation_v1.py::evaluer_membre` | exempté ; environnement sur tache_de | environnement honnête par `conditions.environnement` (couvert, agent_p3) sur `tache_de(...)` : identifiant, questions et classification seulement ; preuve par l'arbre syntaxique dans l'essai v4 | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 5 | `barreau5_familles/formation_v1.py::executer` | exempté ; texte fixe sans tâche | chargement d'invite (`charger_invite('H1-classification')`), sans tâche | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 6 | `barreau5_familles/formation_v1.py::jouer_sans_activations` | exempté ; rendu d'un environnement reçu | rendu : ne lit que consigne_privee et observation d'environnements reçus (comme harnais/episode.py::jouer_episodes) ; ses appelants du module les bâtissent sur `tache_de` | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 7 | `barreau5_familles/formation_v1.py::jouer_scripte_jouet` | exempté ; rendu d'un environnement reçu | mode jouet : même rendu d'environnements reçus, actions écrites par programme | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 8 | `barreau5_familles/formation_v1.py::membres_de_famille` | exempté ; environnement sur tache_de | environnement honnête par `conditions.environnement` (couvert, agent_p3) sur `tache_de(...)` : identifiant, questions et classification seulement ; preuve par l'arbre syntaxique dans l'essai v4 | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 9 | `barreau5_familles/formation_v1.py::tirer_famille` | couvert ; environnement sur tache_de | formation_tirage_saboteur (collecteur à marqueur de l'essai v4 : environnements du saboteur instruit interceptés par le crochet `jouer`) | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| 10 | `barreau5_familles/relecture_v1.py::_executer` | exempté ; environnement sur tache_de | conversation de contrôle fixe, chargement d'invite, et environnements honnêtes sans consigne par `conditions.environnement` (couvert, agent_p3) sur `tache_de(...)` : identifiant, questions et classification seulement ; preuve par l'arbre syntaxique dans l'essai v4 ; la clé `cibles` lue ici est celle de l'adaptateur (voir les lecteurs ajoutés) | ligne CODE-LECTURE-B5F du registre propre du barreau 5, R-4147 ; commit c76e7916 |
| 11 | `barreau5_familles/relecture_v1.py::rejouer` | exempté ; rendu d'un environnement reçu | rendu : consigne_privee et observation d'un environnement reçu de `_executer`, bâti sur `tache_de` | ligne CODE-LECTURE-B5F du registre propre du barreau 5, R-4147 ; commit c76e7916 |
| 12 | `barreau8_moniteurs/lecture_sondes_v5.py::_directions_attendues` | exempté ; ligne de données | clé « role » d'une ligne de direction (nom, couche, empreinte, rôle), aucune invite | R-3618 ; commit c750d116 |
| 13 | `barreau8_moniteurs/passe_recalcul_v5.py::debut_d_episode` | couvert ; environnement sur tache_de | passe_recalcul_debut (collecteur à marqueur de l'essai v4 : consigne et première observation rendues) | R-3618 ; commit c750d116 |
| 14 | `barreau8_moniteurs/passe_recalcul_v5.py::ecrire_fichiers_de_donnees` | exempté ; ligne de données | clé « role » d'une ligne de direction (nom, couche, empreinte, rôle), aucune invite | R-3618 ; commit c750d116 |
| 15 | `barreau8_moniteurs/passe_recalcul_v5.py::garde_p2_gabarit` | exempté ; rendu d'un environnement reçu | rendu générique : ouverture du gabarit sur un début (consigne, observation) reçu de `debut_d_episode` (couvert) | R-3618 ; commit c750d116 |
| 16 | `barreau8_moniteurs/passe_recalcul_v5.py::rebatir_episodes` | exempté ; environnement sur tache_de | environnement honnête sans texte privé (garde P8) par `conditions.environnement` (couvert, agent_p3) sur `tache_de(...)` : identifiant, questions et classification seulement ; preuve par l'arbre syntaxique dans l'essai v4 | R-3618 ; commit c750d116 |
| 17 | `dopamine_exploratoire/modele_v1.py::DecoupeurHF.gabarit` | exempté ; rendu générique d'un gabarit de dialogue | rendu générique du gabarit de dialogue du modèle sur deux textes reçus (système, utilisateur), comme harnais/formats.py::FormatChat ; le paquet n'importe ni les environnements ni les tâches du banc (preuve par l'arbre syntaxique dans l'essai v4) | R-4571 ; commit b1b29073, fusion a52731b9 |
| 18 | `lentilles_sondes_bbis/lanceur_v1.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 19 | `lentilles_sondes_bbis/lanceur_v1.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 20 | `lentilles_sondes_bbis/lanceur_v1.py::calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 21 | `lentilles_sondes_bbis/lanceur_v2.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 22 | `lentilles_sondes_bbis/lanceur_v2.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 23 | `lentilles_sondes_bbis/lanceur_v2.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 24 | `lentilles_sondes_bbis/lanceur_v3.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 25 | `lentilles_sondes_bbis/lanceur_v3.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 26 | `lentilles_sondes_bbis/lanceur_v3.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 27 | `lentilles_sondes_bbis/lanceur_v4.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 28 | `lentilles_sondes_bbis/lanceur_v4.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 29 | `lentilles_sondes_bbis/lanceur_v4.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 30 | `lentilles_sondes_bbis/lanceur_v5.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 31 | `lentilles_sondes_bbis/lanceur_v5.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 32 | `lentilles_sondes_bbis/lanceur_v5.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 33 | `lentilles_sondes_bbis/lanceur_v6.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 34 | `lentilles_sondes_bbis/lanceur_v6.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 35 | `lentilles_sondes_bbis/lanceur_v6.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 36 | `lentilles_sondes_bbis/lanceur_v7.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 37 | `lentilles_sondes_bbis/lanceur_v7.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 38 | `lentilles_sondes_bbis/lanceur_v7.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4596 ; commit cc9ab8eb, versé par 25236c16 |
| 39 | `lentilles_sondes_bbis/lanceur_v8.py::_Couche.calculer` | exempté ; ligne de données | clé « role » d'une ligne de lecture d'une sonde (sonde, cellule, pli, rôle, vecteur, couche), aucune invite | R-4650 ; commit c3263a80, versé par e6fbe03a |
| 40 | `lentilles_sondes_bbis/lanceur_v8.py::_calculer` | exempté ; ligne de données | clé « role » des tables des sondes et des vecteurs non calculables, aucune invite | R-4650 ; commit c3263a80, versé par e6fbe03a |
| 41 | `lentilles_sondes_bbis/lanceur_v8.py::_etiqueter` | exempté ; ligne de données | clé « role » d'une ligne d'étiquettes d'une sonde, aucune invite | R-4650 ; commit c3263a80, versé par e6fbe03a |
| 42 | `t07bbis/etat_impose_v1.py::charger` | exempté ; texte fixe sans tâche | conversation de contrôle fixe (`conversation_de_controle('agent', None)`), sans tâche | R-2751 et R-2780 ; commit 7afb0c99, versé par 5378c2de |
| 43 | `t07bbis/etat_impose_v1.py::rejouer_episode` | exempté ; environnement sur tache_de | environnement imposé par `conditions.environnement` (couvert, agent_p3 ; importé sous le nom `env_de`) sur `tache_de(tache)`, consignes scellées chargées par empreinte ; preuve par l'arbre syntaxique dans l'essai v4 | R-2751 et R-2780 ; commit 7afb0c99, versé par 5378c2de |

## Lecteurs de la clé `cibles` ajoutés

| module | fonction | raison | source |
|---|---|---|---|
| `controle_ia/barreau5_familles/formation_v1.py` | `_executer` | FAUX LECTEUR : `tuple(a["cibles"])` avec `a = config["adaptateur"]` (noms des modules visés par l'adaptateur LoRA), pas la référence cachée d'une tâche ; preuve par l'arbre syntaxique dans l'essai v4 | ligne CODE-FORMATION-B5F du registre propre du barreau 5 ; commit ef800868 |
| `controle_ia/barreau5_familles/relecture_v1.py` | `_executer` | FAUX LECTEUR : `tuple(a["cibles"])` avec `a = config["adaptateur"]` (noms des modules visés par l'adaptateur LoRA), pas la référence cachée d'une tâche ; preuve par l'arbre syntaxique dans l'essai v4 | ligne CODE-LECTURE-B5F du registre propre du barreau 5, R-4147 ; commit c76e7916 |

## Épreuves jouées

Commande : `PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_cibles_invisibles_v4.py --basetemp=<dossier neuf>`.

| cas | résultat |
|---|---|
| essai v4 sur la liste scellée | 41 passés |
| essai v3, inchangé | 2 échecs, 19 passés (les deux essais d'inventaire, comme avant) |
| copie de la liste rescellée sans changement (cas sain de la mutation) | 41 passés |
| une ligne ajoutée retirée (le gabarit du bras du papier dopamine) | 4 échecs, dont l'inventaire des constructeurs |
| une ligne ajoutée retirée (une fonction du lanceur version 8 des lentilles) | 3 échecs, dont l'inventaire des constructeurs |
| un faux lecteur ajouté retiré | 3 échecs, dont l'essai des lecteurs de la clé `cibles` |
| une ligne reprise de l'essai v3 retirée | 3 échecs, dont « la liste reprend le v3 sans rien changer » |

Les mutations sont jouées sur une copie de l'essai et de la liste dans un dossier de travail, la liste mutée rescellée pour que l'échec vienne de l'inventaire et non du sceau. L'essai v4 porte aussi la mutation en lui-même (`test_chaque_ligne_ajoutee_est_necessaire` : chacune des 43 lignes et chacun des deux lecteurs, retirés un à un).

## Réserves et limites

1. **Contre-lecture à faire** (Opus 5.5, puis vérification des corrections par le même lecteur) : l'accord la pose comme condition. Pièces à lui donner : cette note, la liste, l'essai v4, l'essai v3, et les 16 fichiers sources.
2. **L'inventaire bouge** : un fichier neuf est apparu pendant la rédaction. Toute fonction neuve qui construit une invite fera échouer l'essai v4 jusqu'à son examen — c'est son rôle. Les 16 fichiers examinés sont épinglés par empreinte : un fichier modifié se réexamine.
3. **Ce que l'examen couvre** : ce qui entre dans une invite. Il ne couvre pas ce que ces modules écrivent sur disque (par exemple, le tirage de la formation garde le dictionnaire de tâche entier en mémoire à côté des textes tirés : non suivi ici jusqu'aux fichiers).
4. **Raisons d'exemption** : 41 lignes sur 43 sont exemptées sur lecture et preuve par l'arbre syntaxique, 2 sont couvertes par un collecteur à marqueur. Une preuve par l'arbre voit la forme du code, pas son exécution ; les environnements eux-mêmes restent couverts par les collecteurs de l'essai v3.
5. **Lentilles** : la source des lanceurs versions 1 à 7 est la ligne R-4596 (commit `cc9ab8eb`, qui n'est pas un ancêtre de la tête ; le versement sur main est `25236c16`) ; l'inscription de la fiche du code au registre propre des lentilles n'a pas été vérifiée ici.
6. **Versement** : l'essai v4 est exclu localement de git (`.git/info/exclude`, ligne 87) ; la liste et cette note ne le sont pas. Un fichier d'essai neuf s'ajoute aux inventaires figés des fichiers d'essais (essais datés, déjà en échec attendu).
7. Écart à la consigne de travail, sans effet sur le fond : une commande de liste sur le paquet du bras du papier dopamine et des recherches récursives dans `src/controle_ia/` ont servi à l'examen ; aucun fichier interdit par le cloisonnement n'a été ouvert, aucun résultat lu.
