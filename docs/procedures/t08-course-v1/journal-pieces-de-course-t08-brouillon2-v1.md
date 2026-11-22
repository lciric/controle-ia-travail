# Journal — brouillons 2 des pièces de la course de la base boîte noire (T0.8)

Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon2-v1.py`. Chaque opération remplace un texte trouvé exactement une fois dans le fichier d'entrée ; « renvoi » : renvoi d'un brouillon à l'autre, sans constat.

Contre-lecture appliquée : `prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon1-cl1.md`, `3ea629e8b1818f885a655776a0ce025dcad9f8ce2f93fa5123690ec40961e2c6`.

## `ordre-course-t08-v1-brouillon1.md` → `ordre-course-t08-v1-brouillon2.md`

| n° | constat | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | sur une machine louée — v1 — brouillon 1 | sur une machine louée — v1 — brouillon 2 |
| 2 | renvoi | - **Statut** : **brouillon 1**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas en… | - **Statut** : **brouillon 2**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas en… |
| 3 | renvoi | **Contre-lecture** : par un sous-agent neuf d'un autre modèle, lancé par la session mère (`consigne-contre-lec… | **Contre-lecture** : brouillon 1 contre-lu par un sous-agent neuf d'un autre modèle, lancé par la session mère… |
| 4 | m-O2 | sont antérieures à l'heure de la machine (garde gardée par `GO-2026-11-22-122`) ¦ | sont antérieures à l'heure de la machine (garde gardée par `GO-2026-11-22-122`) ; l'essai de cette garde a son… |
| 5 | O-3 | la ligne de GO citée est de type « calcul » et valide à la date de création ; la garde de calcul, éprouvée à b… | la ligne de GO citée est de type « calcul » et valide à la date de création, prolongations comprises (GO-2026-… |
| 6 | renvoi | leurs empreintes sont celles de cet ordre (brouillon 2) ¦ | leurs empreintes sont celles de cet ordre (brouillon 3) ¦ |
| 7 | renvoi | Les commandes exactes sont au brouillon 2. | Les commandes exactes sont au brouillon 3. |
| 8 | O-2 | l'heure où la dépense projetée au prix de l'offre atteint le plafond est calculée et passée à l'amorce | l'heure où la dépense projetée au prix de l'offre atteint le plafond restant — 120 USD moins la dépense antéri… |
| 9 | m-O1 | Un relevé toutes les trente minutes : la machine est à l'inventaire | Un relevé toutes les trente minutes (geste de service : il ne fonde ni arrêt ni lecture) : la machine est à l'… |
| 10 | m-O2 | Deux heures sans ligne de progression : alerte à la session mère, **sans arrêt**. | Deux heures sans ligne de progression : alerte à la session mère, **sans arrêt** (essai de cette alerte, consi… |
| 11 | O-1 | 11. **Destruction par l'identifiant** (R10), après la vérification de la poussée ; | 10 bis. **Course arrêtée** (plafond, minuterie, processus mort, fichier interdit, empreinte ou commit différen… |
| 12 | renvoi | sous sa consigne (`consigne-lecteur-t08-v1-brouillon1.md`) | sous sa consigne (`consigne-lecteur-t08-v1-brouillon2.md`) |
| 13 | J-1 | sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon1.md`) ; ligne `VERDICT-T08` ; soumis à Lazar. | sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon2.md`) ; ligne `VERDICT-T08` ; soumis à Lazar par le … |
| 14 | renvoi | ## 12. À écrire au brouillon 2 | ## 12. À écrire au brouillon 3 |
| 15 | O-3 | le montant de crédit exigé au préalable P9 ; l'identifiant de la session exécutante. | le montant de crédit exigé au préalable P9 ; l'identifiant d'accord que porte la commande à la date de créatio… |

Entrée : `295493dd88a1e36a4981926fad9a5fa03e3c3d59ef699eacf240030c74ee0fde`. Sortie : `727db6ce402a5f23c76b1323d16d42f4c076ac47992a82452e40193a7ac9a6b1`. Opérations : 15.

## `consigne-lecteur-t08-v1-brouillon1.md` → `consigne-lecteur-t08-v1-brouillon2.md`

| n° | constat | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | jouer la lecture sur processeur — v1 — brouillon 1 | jouer la lecture sur processeur — v1 — brouillon 2 |
| 2 | renvoi | - **Statut** : brouillon 1, à contre-lire par un sous-agent neuf d'un autre modèle. La commande exacte de la l… | - **Statut** : brouillon 2. Il applique au brouillon 1 (`115fb0c0a79b4fad97e3ff37f3ea32de4534cce228c61c42cb11e… |
| 3 | m-L1 | les messages d'arrêt et les lignes de progression du programme. | les messages d'arrêt et les lignes de progression du programme, qui ne portent que des noms d'étape et d'état … |
| 4 | L-2 | le résultat `lecture-t08.json` et le fichier des tables, hors ce que dit la section 6 ; | le résultat `lecture-t08.json`, le fichier des tables et le fichier d'échantillon de l'audit, hors ce que dit … |
| 5 | L-1 | 5. Aucun fichier interdit n'est dans ton dossier de travail. | 5. Aucun fichier interdit n'est dans ton dossier de travail. ⏎ 6. Tu demandes à la session mère la ligne de so… |
| 6 | renvoi | Tu joues **une fois** la commande de la lecture (brouillon 2), | Tu joues **une fois** la commande de la lecture (brouillon 3), |
| 7 | L-2 | - S'il l'est, tu relis l'échantillon que le programme désigne : pour chaque action, | - S'il l'est, tu relis l'échantillon que le programme désigne et extrait lui-même (textes d'action, coûts lus,… |
| 8 | J-1 | La session mère inscrit la ligne `LECTURE-T08`. Rien de ce que tu produis ne va à une session qui conçoit un s… | La session mère inscrit la ligne `LECTURE-T08`. Rien de ce que tu produis ne va à une session qui conçoit un s… |

Entrée : `115fb0c0a79b4fad97e3ff37f3ea32de4534cce228c61c42cb11eeb755d77e0b`. Sortie : `3e39b3c30dafe7ab8d18c4878917432c236fbab880fe13308446defe3883d376`. Opérations : 8.

## `consigne-juge-verdict-t08-v1-brouillon1.md` → `consigne-juge-verdict-t08-v1-brouillon2.md`

| n° | constat | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | appliquer les tables D et F — v1 — brouillon 1 | appliquer les tables D et F — v1 — brouillon 2 |
| 2 | renvoi | - **Statut** : brouillon 1, à contre-lire par un sous-agent neuf d'un autre modèle. | - **Statut** : brouillon 2. Il applique au brouillon 1 (`2d40445bcb7a6f5792ce4a22892ee3930700a1dae7a82df6ccfce… |
| 3 | m-J1 | tu n'es ni le lecteur ni l'exécutante. | tu n'es ni le lecteur, ni l'exécutante, ni un contre-lecteur du texte de T0.8 ou de ces pièces. |
| 4 | m-J3 | un verdict d'une autre tâche, un fichier de 7a ou de P3-bis ; | un verdict d'une autre tâche (la ligne de la table A de T0.6, que demandent les lignes D2 et F1b, n'est lue qu… |
| 5 | m-J2 | 3. Les lignes `SCELLEMENT-T08` et `CODE-T08` sont antérieures à `COURSE-T08`, et `COURSE-T08` à `LECTURE-T08`. | 3. Les lignes `SCELLEMENT-T08` et `CODE-T08` sont antérieures à `COURSE-T08`, et `COURSE-T08` à `LECTURE-T08` … |
| 6 | J-3 | **Les phrases des tables D et F que porte le fichier des tables sont égales, à l'octet, à celles du texte scel… | **Les phrases des tables D et F que porte le fichier des tables sont égales, à l'octet, à celles du texte scel… |
| 7 | J-2 | celle du saboteur instruit ; la lecture descriptive | celle du saboteur instruit ; pour chaque dose, le compte des trajectoires diffuses (aucune alerte d'aucun surv… |
| 8 | J-1 | - Les deux scellés, poussés sur une branche neuve. La session mère inscrit `VERDICT-T08` et soumet le verdict … | - Les deux scellés, poussés sur une branche neuve. La session mère inscrit `VERDICT-T08`, par le chemin et l'e… |

Entrée : `2d40445bcb7a6f5792ce4a22892ee3930700a1dae7a82df6ccfceb546c709e9e`. Sortie : `3ae26fdbc00e270d3566eb3b4d8f58c9702eb6dd0d8a5a368a5bb826bf1d2506`. Opérations : 8.

## `consigne-chaine-de-lancement-t08-v1.md` → `consigne-chaine-de-lancement-t08-v2.md`

| n° | constat | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | de la base boîte noire (T0.8) — v1 | de la base boîte noire (T0.8) — v2 |
| 2 | renvoi | - **Nature** : mandat (classe C). | - **Version 2** : remplace la version 1 (`722ceb5e475c1cf06137f5482175f041b1a25b6c8f43636acdd873c2e8f44a67`, g… |
| 3 | renvoi | `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon1.md` | `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon2.md` |
| 4 | L-2, m-L1 | Une entrée de même forme pour le passage à blanc (`lecture_v1.passage_a_blanc_reel`) sur le registre réel. | Une entrée de même forme pour le passage à blanc (`lecture_v1.passage_a_blanc_reel`) sur le registre réel. ⏎  … |
| 5 | O-3 | - la ligne de GO, toujours par la variable `GO_ID` ; fin de validité et plafond lus au registre ; | - la ligne de GO, toujours par la variable `GO_ID` ; fin de validité et plafond lus au registre, **prolongatio… |
| 6 | O-2 | le plafond de la course est **120 USD cumulés sur toutes les tentatives**, dépense antérieure relevée au regis… | le plafond de la course est **120 USD cumulés sur toutes les tentatives**, dépense antérieure relevée au regis… |
| 7 | O-2 | à l'heure où la dépense projetée au prix de l'offre atteint le plafond, elle consigne et pousse | à l'heure où la dépense projetée au prix de l'offre atteint le plafond restant (120 USD moins la dépense antér… |
| 8 | O-2, O-3, m-O2, L-2, m-L1 | - Clonage : un fichier interdit présent sur la machine arrête avant tout calcul. | - Clonage : un fichier interdit présent sur la machine arrête avant tout calcul. ⏎ - Plafond restant (O-2) : d… |

Entrée : `722ceb5e475c1cf06137f5482175f041b1a25b6c8f43636acdd873c2e8f44a67`. Sortie : `a0da4962bedaa17b4dfc2bb27910ae4f36c982fb67e1b38341be304b6b8a20be`. Opérations : 8.

