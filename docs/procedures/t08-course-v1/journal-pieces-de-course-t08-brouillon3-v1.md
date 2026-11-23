# Journal — brouillons 3 des pièces de la course de la base boîte noire (T0.8)

Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon3-v1.py`. Chaque opération remplace un texte trouvé exactement une fois dans le fichier d'entrée.

Causes : « J-1 », décision de la session mère (R-5017 de `registres/decisions.md`) sur le constat J-1 de la contre-lecture 1 ; « commit », réponse du rédacteur à la question du développeur de la chaîne de lancement sur la tête de la course ; « renvoi », renvoi d'un brouillon à l'autre.

## `ordre-course-t08-v1-brouillon2.md` → `ordre-course-t08-v1-brouillon3.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | sur une machine louée — v1 — brouillon 2 | sur une machine louée — v1 — brouillon 3 |
| 2 | renvoi | - **Statut** : **brouillon 2**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas en… | - **Statut** : **brouillon 3**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas en… |
| 3 | renvoi | ; le brouillon 3 y portera les commandes exactes, | ; le brouillon des commandes y portera les commandes exactes, |
| 4 | renvoi | les corrections de ce brouillon 2 sont à vérifier par le même contre-lecteur. | les corrections des brouillons 2 et 3 sont à vérifier par le même contre-lecteur. |
| 5 | commit | hors le manifeste de sa propre course pour son identifiant et sa date. | hors le manifeste de sa propre course pour son identifiant, sa date et son commit. |
| 6 | J-1 | les seuils et les scores des moniteurs ne vont pas du côté de ceux qui conçoivent un saboteur. | les seuils et les scores des moniteurs ne vont pas du côté de ceux qui conçoivent un saboteur. ⏎ - **Relais du… |
| 7 | renvoi | leurs empreintes sont celles de cet ordre (brouillon 3) ¦ | leurs empreintes sont celles de cet ordre (brouillon des commandes) ¦ |
| 8 | renvoi | Les commandes exactes sont au brouillon 3. | Les commandes exactes sont au brouillon des commandes. |
| 9 | commit | noms, tailles, compagnons, empreinte du résultat `course-t08.json`. | noms, tailles, compagnons, empreinte du résultat `course-t08.json`. Elle vérifie aussi, par les noms seuls, le… |
| 10 | renvoi | sous sa consigne (`consigne-lecteur-t08-v1-brouillon2.md`) | sous sa consigne (`consigne-lecteur-t08-v1-brouillon3.md`) |
| 11 | J-1 | sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon2.md`) ; ligne `VERDICT-T08` ; soumis à Lazar par le … | sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon3.md`) ; ligne `VERDICT-T08`, inscrite par la session… |
| 12 | renvoi | ## 12. À écrire au brouillon 3 | ## 12. À écrire au brouillon des commandes |
| 13 | commit | l'identifiant d'accord que porte la commande à la date de création (préalable P4) ; | l'identifiant d'accord que porte la commande à la date de création (préalable P4) ; la commande qui vérifie le… |

Entrée : `727db6ce402a5f23c76b1323d16d42f4c076ac47992a82452e40193a7ac9a6b1`. Sortie : `6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8`. Opérations : 13.

## `consigne-lecteur-t08-v1-brouillon2.md` → `consigne-lecteur-t08-v1-brouillon3.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | jouer la lecture sur processeur — v1 — brouillon 2 | jouer la lecture sur processeur — v1 — brouillon 3 |
| 2 | renvoi | - **Statut** : brouillon 2. Il applique au brouillon 1 | - **Statut** : brouillon 3. Il inscrit au brouillon 2 (`3e39b3c30dafe7ab8d18c4878917432c236fbab880fe13308446de… |
| 3 | renvoi | La commande exacte de la lecture vient au brouillon 3, | La commande exacte de la lecture vient au brouillon des commandes, |
| 4 | renvoi | Tu joues **une fois** la commande de la lecture (brouillon 3), | Tu joues **une fois** la commande de la lecture (brouillon des commandes), |
| 5 | renvoi | brouillon 3 : chemin du fichier d'échantillon | brouillon des commandes : chemin du fichier d'échantillon |
| 6 | J-1 | La session mère reçoit les chemins et les empreintes ; elle n'ouvre ni `lecture-t08.json` ni le verdict tant q… | **Relais du verdict** (décision de la session mère, R-5017 de `registres/decisions.md`, sur le constat J-1 de … |

Entrée : `3e39b3c30dafe7ab8d18c4878917432c236fbab880fe13308446defe3883d376`. Sortie : `6a39a5d9aa1dc0e289494c0fea0828fdc8216f866f0358b08446605881c89cdf`. Opérations : 6.

## `consigne-juge-verdict-t08-v1-brouillon2.md` → `consigne-juge-verdict-t08-v1-brouillon3.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | appliquer les tables D et F — v1 — brouillon 2 | appliquer les tables D et F — v1 — brouillon 3 |
| 2 | renvoi | - **Statut** : brouillon 2. Il applique au brouillon 1 | - **Statut** : brouillon 3. Il inscrit au brouillon 2 (`3ae26fdbc00e270d3566eb3b4d8f58c9702eb6dd0d8a5a368a5bb8… |
| 3 | J-1 | La session mère reçoit les chemins et les empreintes ; elle n'ouvre ni `lecture-t08.json` ni le verdict tant q… | **Relais du verdict** (décision de la session mère, R-5017 de `registres/decisions.md`, sur le constat J-1 de … |

Entrée : `3ae26fdbc00e270d3566eb3b4d8f58c9702eb6dd0d8a5a368a5bb826bf1d2506`. Sortie : `a99adb596f94a82c534d204325f7884180bca6c446dad0d089192c663711cb9c`. Opérations : 3.

## `consigne-chaine-de-lancement-t08-v2.md` → `consigne-chaine-de-lancement-t08-v3.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | de la base boîte noire (T0.8) — v2 | de la base boîte noire (T0.8) — v3 |
| 2 | renvoi | - **Version 2** : remplace la version 1 | - **Version 3** : remplace la version 2 (`a0da4962bedaa17b4dfc2bb27910ae4f36c982fb67e1b38341be304b6b8a20be`, g… |
| 3 | renvoi | `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon2.md` | `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon3.md` |
| 4 | commit | - avant tout calcul : `entrees_v1.exiger_instance_sans_interdits`, le commit du code égal à celui du texte sce… | - avant tout calcul : `entrees_v1.exiger_instance_sans_interdits`, le commit du code égal à celui du texte sce… |
| 5 | commit | artefact : une ligne qui en porte un fait échouer l'essai. | artefact : une ligne qui en porte un fait échouer l'essai. ⏎ - Commit local de la course : liste déclarée exac… |
| 6 | renvoi | Une branche poussée (`prep/t08-chaine-de-lancement-v1`) | Une branche poussée (`t08/chaine-de-lancement-v1`, nom donné par la session mère) |
| 7 | renvoi | de l'ordre de course**, pour son brouillon 2. | de l'ordre de course**, pour son brouillon des commandes. |

Entrée : `a0da4962bedaa17b4dfc2bb27910ae4f36c982fb67e1b38341be304b6b8a20be`. Sortie : `6f52c4db8d1a3fd0a530cbbfc3cc59e0b0d47f745191d8316aa5d0560e94346e`. Opérations : 7.

