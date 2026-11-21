# Conception du véhicule — course « nouvelles attaques », à cinq espèces, trois générations — v2

Pièce de travail (classe C), non scellée ; la v1 est contre-lue (verdict « À corriger »), la v2 porte ses corrections et reste à vérifier par le même contre-lecteur. Elle conçoit ; elle ne tranche rien de ce que la lettre laisse ouvert : ce qui est tranché l'est par la mère, et c'est dit. Processeur seul : aucun appel, aucune dépense, aucun code écrit pour être lancé, aucun lancement, aucune écriture dans un dépôt.

- Auteur : concepteur du véhicule, modèle F. Je n'ai écrit ni la v9, ni l'inventaire, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 06:45:57Z, après la lecture des pièces, avant l'écriture. Version 2 : 07:10:25Z, après la lecture de la contre-lecture, avant l'écriture.
- Version : la v2 remplace la v1 (`675f8d39dc64548f34e36763b3a523277d9c1daa1c208e3b2b678dd9f79ace9b`, non scellée, archivée sans modification) après la contre-lecture `docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v1/contre-lecture-v1/contre-lecture-conception-vehicule-na-v1.md` (`f5b7aacc9d96dfd3bb10eaa80a6f451d646b3b7c06844dbb4da6837182cf36db`, égale à son compagnon, lue en entier ; notée CL). Elle porte : (1) les décisions de la mère de 06:58Z, D1 à D7 et D10, écrites comme décisions (§ 0 bis) ; (2) les corrections de CL, point par point (table au rapport v2) ; (3) les décisions de la mère de 07:10Z sur trois points de CL (D11 ; la fiche hors contrat de longueur ; la lecture des mesures, gardée à la lettre de la V9 d'ici le mot de Lazar) et sur le calendrier. Le différentiel v1 → v2 est joint.
- **Ce qui dépend du relevé du lot 0** est marqué « [lot 0] » : un développeur O neuf le fait en parallèle, et ses réponses peuvent encore changer cette v2.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-conception-vehicule-course-nouvelles-attaques-v1.md` (`d2130f6b0aab5d4d32f01f51acd71b23cc3d1623769b24cd4d6fb06317c19af2`, égale à son compagnon), lu en entier.
- Point de départ : l'inventaire de l'allumage (`0737906f9901de39ddd9b1585679b5b44e6bac67e7051a10374d3e0e496c06e0`), son § 4, et le gabarit des témoins (`a84de0bf3168d93dda6928e2e165c14ecb8b091e976a629ace828813c24c89c0`).
- Lecture : `origin/main` du dépôt de l'organisme au commit `ebb7492a8a2923a6a790ee0f8d29ee320b530f3d` ; le code existant sur le disque de la branche `lot/compte-organisme-v1` (commit `9555d8b696d3aae9d17a9c41399d0ab24704c530`) et dans le dépôt de l'orchestrateur (commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`). Pièces et empreintes : rapport joint, § 1.
- Ce que ce texte ne contient pas : aucune méthode d'attaque, aucun procédé, aucune recette, aucun nom ni énoncé de mode, aucune case nommée, aucun identifiant de modèle, aucune valeur ni nom de variable de clé, aucun motif de la garde de motifs.

Sigles de renvoi (numéros de ligne) : V9, A1, CV, AC, DV, OC comme à l'inventaire ; PS, la partie servie (`4cd360ba…`) ; R68, le rapport du développeur de la v68 (`ad42b722…`) ; C68, sa contre-lecture (`d2cfeac1…`) ; A69, l'additif des interrupteurs de la v69 : sa v4 scellée (`cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578`, registre, R-4131) fait foi ; je n'ai lu que le § 7 de sa v1 (`aef8ff2f…`) et je tiens de CL, § 1.5, ce que la v4 y ajoute ; L9 et L10, les lanceurs de course v9 et v10 (`1b47c1cf…`, `f4196ec5…`) ; E9, l'épreuve des témoins v9 (`5be161fa…`) ; CL, la contre-lecture de la v1 (`f5b7aacc…`).

## 0. En bref

1. **Base retenue.** Orchestrateur : le commit `a41b7b50…` plus le paquet v68 (huit fichiers neufs, manifeste `4ed9fd8e…`, contre-lu « Conforme »). Lanceur : le lanceur de course v9 (`1b47c1cf…`), le seul qui ait porté une course réelle de cette composition, avec deux lectures reprises du lanceur v10 (`f4196ec5…`). Épreuve des témoins : celle de la course v9 (`5be161fa…`). Le lanceur 11 n'a pas de code : il n'existe que par la liste de ce qu'il doit épingler (A69, v4 scellée, § 7), que le lanceur neuf suit.
2. **Plus petite différence.** Le véhicule ne récrit ni le noyau des appels, ni le budget d'une génération, ni la garde de budget de la course, ni les relais, ni la conservation des réponses, ni l'inventaire de fin. Il ajoute des fichiers neufs, jamais une modification (règle R12). **Il lève les deux refus de la v68 par deux fichiers neufs**, un lanceur de l'orchestrateur et une fonction de course ; la course de la v68 lui sert de modèle et n'est pas appelée (§ 1.2).
3. **Ce qui est neuf, et lourd** : l'assemblage exact de la requête, la garde de motifs et le journal posés dans un adaptateur gardé, au dernier point avant l'envoi ; le routage par rôle sur quatre relais actifs ; le portier à trois classes et quatre classes d'issue d'appel ; le registre servi ; des cases neuves à chaque génération ; les mesures ; le sort des gardes héritées du noyau, que la V9 ne porte pas (§ 2.13).
4. **Dix lots** : un lot 0 de relevé du code, sans écriture, puis neuf lots de code ; plus un lot 10 facultatif, hors du chemin critique (colonne « matière première », éteinte par défaut, dont la course ne dépend pas). Chemin critique : 0, 2, 3, 5, 6, 8, 9, soit 24 heures au plus bas.
5. **Calendrier, dit sans forcer** : 31 heures de sessions de développeur et de vérificateur et environ 15 heures autour sont une borne basse, non une attente. L'attente honnête est de **40 à 50 heures d'horloge** : un véhicule contre-lu le 23 novembre au plus tôt, un départ le 24 ou le 25. **L'échéance du 2026-11-22 de GO-2026-11-20-67 ne tient pas.** La mère demande à Lazar une échéance au 2026-11-27 : demandée, non accordée.
6. **Trois trous que l'inventaire ne nomme pas** (§ 9, points 1 à 3), tous trois tranchés depuis par la mère (D2, D3, D5) : les consignes du portier et des juges pour cette question ne sont écrites nulle part ; la partie servie ne dit pas la syntaxe de la sortie, et rien d'autre de fixe ne doit partir ; le registre servi veut un « nom » que la fiche ne porte pas.

## 0 bis. Décisions de la mère (2026-11-21, 06:58Z), portées par cette v2

Reçues par le message de reprise ; CL les dit inscrites au registre (R-4381, R-4383), que je n'ai pas relu.

| n° | décision de la mère | où elle est portée |
|---|---|---|
| D1 | série NA-1, suffixe `_na_v1` | § 1.4 |
| D2 | **rien n'est ajouté à l'enveloppe** | § 2.3, § 5.3, § 5.4, § 9, point 2 |
| D3 | les consignes du portier et des juges sont un manque neuf ; elles sont écrites par le modèle F et contre-lues | § 2.4, § 2.5, § 4, § 9, point 1 |
| D4 | clé de tirage n° 40 pour l'identifiant neutre | § 2.1, § 5.2 |
| D5 | au registre servi, le nom est l'identifiant de la fiche, l'énoncé est le champ `idee` sur une ligne | § 2.6, § 9, point 3 |
| D6 | ordre du portier : forme, modèle, hors case ; une réponse illisible du modèle portier va au coffre | § 2.4, § 9, point 5 |
| D7 | la sonde de refus est lue par programme seul | § 2.10, § 9, point 7 |
| D10 | le code de base est versé sur la branche `verse/vehicule-na-v1`, commit `61987a3a`, en attente de `main` | § 1.1, § 2.11 |

**Décisions de la mère de 07:10Z**, reçues par un second message pendant l'écriture :

| n° | décision de la mère | où elle est portée |
|---|---|---|
| D11 | l'épreuve de l'arrêt n° 12 sous GO-2026-11-21-02 : acceptée telle que le contre-lecteur la propose (CL, § 5) : un cas sain neuf, deux artefacts, la mutation « routeur par espèce » | § 6.1, ligne du n° 12 ; § 9, point 17 |
| D13 | **règle d'écriture** : une fiche hors contrat de longueur (un champ au-dessus de sa borne, `idee` compris) est traitée comme illisible, donc « au coffre » (D6), comptée, jamais réparée | § 2.4, § 5.4, § 9, point 3 |
| — | les mesures lues deux fois sont un nœud de Lazar ; d'ici son mot, **la lettre de la V9 est gardée** (l. 315, « lues une fois ») ; l'option est notée à part, soumise à Lazar | § 2.8, § 9, point 11 (D12) |
| — | calendrier : 40 à 50 heures d'horloge, départ le 24 ou le 25 ; la mère demande à Lazar une échéance au 2026-11-27 : **demandée, non accordée** | § 8 |

Vont à Lazar : D8 (portée de l'arrêt n° 1 en course), D9 (échéance de GO-2026-11-20-67), D12 (lecture des mesures). Le numéro D13 est de moi, pour le renvoi.

**Ajout relayé par la mère vers 07:14Z, corrigé à 07:15Z** : une colonne « matière première », tenue à l'écart des proposeurs. La matière n'existe pas à ce jour et la décision revient à Lazar : la colonne est conçue comme une possibilité, éteinte par défaut, dont la course ne dépend pas (§ 2.14, § 2.15 ; lot 10, facultatif).

## 1. Le choix de base

### 1.1 Ce qui existe, lu sur pièces

| pièce | où | empreinte | état |
|---|---|---|---|
| orchestrateur, commit de base | dépôt de l'orchestrateur, lu à `/home/user/lciric/ideation-organism` (le chemin `/home/user/ideation-organism` que cite R68 est absent de cette machine ; L10, l. 530, nomme les deux) | commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` | a porté la course v9 en réel, une génération, par `demonstrations/ideation_v8.py` |
| paquet v68 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/paquet/…`, sur le disque de la branche | manifeste `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` | contre-lu « Conforme » (C68) ; moteur simulé seulement ; refuse le moteur réel par construction |
| lanceur de course v9 (L9) | `scripts/lancer_course_auto_conception_v9.py`, disque de la branche | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` | contre-lu « Scellable. » ; a lancé la course v9 |
| lanceur de course v10 (L10) | `scripts/lancer_course_auto_conception_v10.py`, disque de la branche | `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` | éteint, égal à L9 ; allumé, refusé en réel ; lit les coûts de plusieurs générations à blanc |
| épreuve des témoins v9 (E9) | `scripts/epreuve_temoins_auto_conception_v9.py`, disque de la branche | `5be161fa35e339d171399a3ba2a2c927cd517fba42c745306fd867a4b3e3c69b` | a joué l'épreuve réelle de la course v9 |
| lanceur de course 11 | aucun fichier (son chemin supposé est absent du disque, vérifié ; CL, § 1.4) | — | réservé au palier 1 de l'héritage ; décrit par A69, v4 scellée, § 7 ; non écrit |
| orchestrateur v69, v70 | aucun code | — | additif v4 (`cb352811…`) et cadre v3 scellés (registre, R-4131) ; noms réservés |

**Ces pièces de code ne sont pas sur `origin/main`** au commit lu (`git show` répond « exists on disk, but not in 'origin/main' » pour le rapport de la v68 et pour les deux scripts de la course v9). **Décision de la mère (D10)** : le code de base est versé sur la branche `verse/vehicule-na-v1`, tirée de `main`, commit `61987a3a`, en attente de `main`. Les chemins et les empreintes que les mandats de code et le lanceur épinglent citent ce commit de cette branche (CL, § 1.7) ; les empreintes des fichiers sont celles de la table ci-dessus, que je n'ai pas recalculées sur cette branche.

### 1.2 Ce que le véhicule garde, retire, ajoute

**De l'orchestrateur (base et v68), gardé sans y toucher :**

| ce qui est gardé | fichier | pourquoi |
|---|---|---|
| l'appel d'un rôle, sa consommation notée dans tous les cas, son plafond borné au reste de l'étape | `pole/noyau_v56.py`, `appel` (l. 147 à 188) | c'est là que passe chaque envoi ; l'adaptateur gardé du § 2.3 s'y glisse sans le changer |
| le budget d'une génération et la règle des seuils : plafond dur de la proposition, aiguillage et juges lancés sous leur seuil | `pole/budget_v56.py`, configuration v5 de la course v9 (150 ; 140, 135, 120 : L10, l. 46 à 49) | ce sont exactement les valeurs des arrêts n° 6 et n° 7 à cinq espèces (A1, l. 166, 167) |
| la garde de budget de la course : réservation du plafond d'une génération avant de la jouer, arrêt au plafond de la course | `pole/budget_course_v68.py` | arrêt n° 6 ; V9, l. 377 ; R68, § 3, point 3 |
| le montant requis, N fois le plafond d'une génération, sans étage | `pole/configuration_v68.py` | 3 × 150 = 450 USD ; régime « éteint, sans étage » de R68, § 5 |
| la classe de génération, comme classe mère | `pole/course2_v68.py`, `GenerationV68` | la classe neuve en hérite ; elle lui passe un héritage `None`, parce que son constructeur n'accepte que l'objet de sélection de la v68 (l. 164), et sert le registre par sa propre proposition (§ 2.9) |

**De la v68, pris pour modèle et non appelé** (correction de CL, § 1.3). La v1 rangeait `executer_course_v68` parmi ce qui est gardé : c'était faux. La v68 porte deux refus qui ferment ce régime :

| refus de la v68 | où | comment le véhicule le lève, sans toucher au paquet |
|---|---|---|
| le moteur réel est refusé toujours, interrupteurs éteints compris | son lanceur, `demonstrations/ideation_v68.py` (`MoteurReelRefuseV68` ; R68, § 4) | **un lanceur de l'orchestrateur neuf**, qui n'appelle pas celui de la v68 (§ 2.9) |
| la lecture sans étage est refusée | la bibliothèque : `verifier_regime_v68` (`course2_v68.py`, l. 235 à 237), que `executer_course_v68` appelle (l. 303) | **une fonction de course neuve**, écrite sur le modèle d'`executer_course_v68` (boucle, réservation, ligne de génération, bilan scellé), qui n'appelle ni l'une ni l'autre |

La forme de la lecture servie à la génération suivante (`rendre_heritage_v68` : objet, garde ligne par ligne, titre passé en argument, section omise quand il n'y a rien, `heritage_lu`) est de même reprise comme modèle pour le registre servi (§ 2.6), non appelée.

**De l'orchestrateur, gardé sans y toucher, suite :**

| ce qui est gardé | fichier | pourquoi |
|---|---|---|
| les juges croisés, anonymat de la fiche, passeport exigé | `pole/juges_croises_v53.py`, `pole/noyau_v56.py`, `juger` | juges joués pour information (§ 2.5) |
| le coffre, le sceau des sorties, l'arrêt propre sur signal | `pole/coffre_v53.py`, `pole/outils.py`, `pole/noyau_v56.py` | inchangés |

**De l'orchestrateur, retiré de ce régime** (non joué ; les fichiers restent) : l'étage des tests de mort et la machine jetable (OC, l. 13, 42) ; la passe « tableau », les lecteurs d'étiquettes, les fusions et le bisociateur (`pole/course2_v53.py`, l. 9 à 14 : la V9 ne compose que cinq proposeurs, un portier et deux juges, l. 61) ; la mémoire qui évite les redites (§ 9, point 14) ; la lecture de la sélection d'un étage ; les deux interrupteurs de la v68.

**De l'orchestrateur, ajouté** (fichiers neufs, § 2) : une génération et une course pour ce seul régime, nommé ; l'assemblage de la requête ; l'adaptateur gardé ; le portier de cette course ; le registre des tentatives et le registre servi ; le tirage ; les mesures ; un moteur simulé au contrat de cette course ; un lanceur de l'orchestrateur qui lève le refus du moteur réel pour ce seul régime et épingle l'additif (OC, l. 33).

**Du lanceur L9, gardé** : la vérification du préenregistrement, de l'additif, de la contre-lecture et de son verdict exact ; la ligne d'accord vérifiée au montant exact, en période, non révoquée (`verifier_go`) ; le registre dérivé ; la pièce de départ ; la déclaration des relais, la procédure des relais, la porte à blanc ; l'environnement filtré ; la sonde du bac ; l'enveloppe de conservation des réponses brutes ; l'inventaire de fin quelle que soit l'issue ; l'arrêt au premier refus pour crédit, par identifiant de processus ; les manifestes de départ et de fin ; les réglages par espèce de la course v9, dont la composition est celle de cette course (V9, l. 61 ; A1, l. 142).

**Du lanceur L9, retiré** : la matière première et son découpage en lots ; les courses closes admises et le mot de reprise ; la clé unique du premier relais ; les sondes propres à la course d'auto-conception qui n'ont pas d'objet ici. **De L10, repris** : la lecture des coûts génération par génération et la relecture du bilan de course par comptes (`couts_generation`, `bilan_allume`). **De L10, non repris** : les interrupteurs.

**Du lanceur, ajouté** : cinq clés nommées dont une hors course, quatre relais actifs, la table des rôles et des clés ; l'arrêt n° 11 lu sur la pièce de relevés ; les bornes des relais comptées pour trois générations ; l'épinglage du tirage, de la garde de motifs, des témoins, des pièces servies, de la V9 et de ses compléments ; le routage des deux lignes à part.

### 1.3 Pourquoi cette base

- Aucune autre version ne joue plusieurs générations sous un plafond de course : la v68 seule le fait (OC, l. 25), et sa garde de budget est éprouvée par cas sain, artefacts et trois mutations (C68, constat 5).
- Aucun autre lanceur n'a porté en réel la composition de cette course : L9 seul. Partir de L10 ferait hériter de deux interrupteurs que le régime n'emploie pas ; partir de L9 et reprendre de L10 deux fonctions de lecture est le plus court.
- Le lanceur neuf « suit le lanceur 11 » (V9, l. 402) par son rang et par ce qu'il épingle : je reprends la liste d'A69, v4 scellée, § 7, point par point, au § 2.11. Il ne peut pas en suivre le code : il n'y en a pas.
- Ce que je n'ai pas pu établir par lecture est rassemblé au lot 0 (§ 7) : treize questions fermées posées au code avant d'écrire.

### 1.4 Le nom

Les numéros 69, 70 et 71 sont déjà portés, hors de cette course, par une autre lignée du même orchestrateur (registre, l. 2507, 2558, 2579). Un numéro de plus risque une seconde collision. **Décision de la mère (D1)** : une série propre, « NA-1 », la version dans le nom (règle R12) : suffixe `_na_v1` pour les fichiers de l'orchestrateur, `lancer_course_nouvelles_attaques_v1.py` pour le lanceur, « véhicule NA-1 » dans les textes. Le régime porte un seul nom, écrit en toutes lettres dans le code et dans la ligne d'accord : `trois_generations_sans_etage_lecture_du_registre_des_tentatives` (ce nom-là est une valeur du concepteur).

## 2. Les modules

Un module par fonction du cahier des charges. Pour chacun : la lettre qui l'impose, ce qu'il fait, ce qu'il lit et rend. Les épreuves sont au § 6, les interfaces au § 5. « Dossier de sortie » désigne le dossier de la course hors de l'arbre de travail, qui est la quarantaine ; « dossier du run », le dossier des manifestes, qui en est dehors.

**Règle commune à tous les modules** (V9, l. 82, 83, 387, 388) : hors du dossier de sortie ne s'écrivent que des identifiants, des empreintes, des tailles et des comptes. Aucun message d'erreur, aucune ligne d'écran, aucun manifeste du dossier du run ne recopie un octet d'une réponse de modèle, d'une fiche ou d'une ligne du registre servi. Le lanceur recopie aujourd'hui la fin de la sortie d'erreur de l'orchestrateur dans son refus : je le tiens de L10, l. 2998 ; le lieu dans L9 est relevé au lot 0, question 13 [lot 0]. Ce lieu est à fermer (lot 8).

### 2.1 Tirage des cases, de la clé n° 30, des identifiants — module `tirage`

| | |
|---|---|
| lettre | V9, l. 300 à 313 ; A1, l. 79 à 82, 119 ; arrêt n° 10, l. 381 ; C1, l. 158 ; A1, l. 160, 163 |
| fait | lit la légende des trois axes dans le gabarit de la partie servie, à l'octet (jamais dans la question) ; forme les 120 triplets dans l'ordre canonique ; tire la clé 0, puis les clés 1, 2, 3 ; tire la clé 30 parmi les seules cases servies dont la menace du programme est le sabotage (A1, l. 78, 79), ou ne tire rien s'il n'y en a aucune ; désigne la première case de la réserve ; tire les identifiants neutres (§ 5.2) ; expose, pour la course, les tirages des clés 12, 13 et 20, qui ne se jouent qu'une fois leurs n connus |
| lit | le gabarit à son empreinte ; la racine écrite, jamais recalculée ; la version de `numpy`, refusée sous 1.25 |
| rend | un seul fichier, octets déterministes (clés triées, fins de ligne fixes, aucune heure) : famille tenue à l'écart, cases des trois générations, case de la clé 30 ou « aucune », case de la réserve, table des identifiants, contrôles C1, versions, racine, clés. L'heure et le commit vont au manifeste, à part, pour que deux jeux soient égaux à l'octet |
| garde | disjonction (arrêt n° 10) : rejouée par la course au départ de chaque génération, contre ce fichier scellé |

### 2.2 Assemblage de la requête, partie servie, ligne de case — module `requete`

| | |
|---|---|
| lettre | V9, l. 69 à 77 ; arrêt n° 14, l. 385 ; arrêt n° 8, l. 379 |
| fait | charge le gabarit, vérifie son empreinte, exige un seul emplacement sur une ligne propre, le remplace par la ligne de case ; assemble la requête d'un rôle (§ 5.3) ; rend la suite d'octets et sa composition |
| ne fait jamais | ouvrir la question : le chemin de la question donné à la place du gabarit est refusé par son empreinte et par son nom ; ajouter un octet hors de l'enveloppe de l'additif |
| contrôle | les trente-trois lignes de case, plus celle de la réserve : trois valeurs égales à l'octet à la légende, identifiants distincts, aucune suite de huit caractères hexadécimaux, aucun chiffre, borne de 256 octets |
| rend | pour un proposeur : partie servie remplie, synthèse servie à l'octet, registre servi aux générations 2 et 3 ; pour une sonde de refus : la partie servie remplie, seule ; pour le portier et un juge : leur consigne fixe et une fiche (§ 2.4, § 2.5) |

### 2.3 Adaptateur gardé : routage, garde de motifs, journal, part de la clé — modules `routage`, `garde_motifs`, `journal`

C'est la pièce centrale. Chaque adaptateur de fournisseur est enveloppé une fois, à la construction de la course. L'appel du noyau (`self.ad[fournisseur].lancer(...)`, `noyau_v56.py`, l. 165) ne change pas : il atteint l'adaptateur gardé, qui fait, dans cet ordre, puis passe la main à l'adaptateur d'origine.

| pas | ce qui est fait | arrêt | lettre |
|---|---|---|---|
| 1 | **routage** : le couple (rôle, clé de l'adaptateur) est cherché dans la table scellée des rôles et des clés ; un rôle sur une autre clé que la sienne, ou tout envoi adressé à la clé hors course, est refusé | n° 12, seconde clause | V9, l. 383 ; AC, l. 88, 175 |
| 2 | **part de la clé** : cumul compté sur la clé, plus le pire des appels en vol sur elle, plus le pire de l'appel à lancer ; au-delà de la part : aucun appel neuf sur cette clé, arrêt nommé de la course, qui dit la clé ; aucune bascule | n° 12, première clause | V9, l. 383 ; CV, l. 166 |
| 3 | **garde de motifs** sur la requête assemblée : normalisation, deux familles, refus qui nomme la famille et le rang ; le texte trouvé ne va qu'au journal | n° 16 | V9, l. 387 |
| 4 | **journal** : une ligne avant l'envoi : taille, empreinte SHA-256, génération, rôle, identifiant de la case, clé par son nom d'usage ; un appel sans ligne ne part pas | — | V9, l. 77 |
| 5 | **égalité** : l'empreinte de ce qui est remis à l'adaptateur d'origine est recalculée et comparée à la ligne du journal ; une différence refuse l'envoi | — | V9, l. 77 (« une requête changée d'un octet après la journalisation est refusée à l'envoi ») |
| 6 | envoi par l'adaptateur d'origine, inchangé ; au retour : coût compté sur la clé ; statut lu pour les arrêts n° 1 et n° 13 | n° 1, n° 13 | V9, l. 372, 384 |

Trois précisions.

- **Un envoi refusé ne coûte rien** (CL, § 2.2). Dans le noyau, un refus levé à l'intérieur de `lancer` passe par le bloc `finally` d'`appel`, qui compte alors le plafond entier de l'appel comme dépensé et l'inscrit au coffre et au cumul de la génération (`noyau_v56.py`, l. 163 à 175) : ce coût fantôme nourrirait la garde de budget de la course et M4 pour un appel jamais parti. **Voie retenue par la conception** : aux pas 1, 2, 3 et 5, l'adaptateur gardé ne lève rien dans `lancer` ; il rend un résultat de statut « non envoyé », au coût déclaré nul et connu, sans texte, écrit « non envoyé » au journal avec le numéro de l'arrêt, et arme l'arrêt ; la génération neuve et le portier neuf lèvent l'arrêt nommé dès le retour de l'appel, avant tout autre envoi. L'autre voie, les pas 1 à 4 joués avant d'entrer dans le noyau, demande de reprendre chacun des lieux qui appellent un adaptateur (la proposition, les juges, le portier, qui appelle l'adaptateur sans passer par `appel`) ; je ne la retiens pas. Que le noyau reçoive sans faute un statut neuf et un coût nul est à confirmer [lot 0, question 5]. Épreuve : § 6.2.
- **Ce que la garde lit, et le texte fixe de rôle** (D2 ; CL, § 2.3 et § 6.4). La requête assemblée est le texte remis à l'adaptateur. L'appel du noyau passe aussi un nom de rôle (`lancer(role_kit, consigne, …)`, l. 165), qui laisse l'adaptateur ajouter un texte fixe de rôle. **Sous D2, rien n'est ajouté à l'enveloppe : ce texte fixe de rôle est retiré**, pour les proposeurs, pour le portier et pour les juges, par un réglage déclaré à l'additif et sans modifier l'adaptateur ; sinon un texte que la V9 ne nomme pas partirait (V9, l. 73). Comment l'adaptateur le permet (un rôle déclaré à texte vide, ou un fichier d'adaptateur neuf si aucun réglage n'existe) est relevé octet par octet [lot 0, question 1]. Il ne reste alors hors de la requête assemblée que le transport (nom du modèle demandé, réglages). L'essai à blanc ferme la boucle : le faux fournisseur garde ce qu'il reçoit, et un programme vérifie que le texte reçu, transport retiré, a l'empreinte du journal (§ 6.3).
- **La table des rôles et des clés** (D-1 de l'inventaire ; AC, l. 56 à 58, 143, 144, 175), portée par la configuration scellée :

| clé (nom d'usage) | relais | rôles de la course | part |
|---|---|---|---|
| Minuit | un | juge de l'espèce 3 ; proposeur de l'espèce 3 | 156,56 USD |
| Luc | un | aiguilleur (le portier) ; proposeur de l'espèce 4 | 125,63 USD |
| deuxième relais | un | juge de l'espèce 1 ; proposeurs des espèces 1 et 5 | 140,39 USD |
| troisième relais | un | proposeur de l'espèce 2 | 17,01 USD |
| Rigaud | aucun | aucun rôle ; tout envoi refusé | sans part |

Soit cinq clés, quatre relais actifs. La lettre dit « trois relais » au sens du devis (DV, l. 391 à 397) : le premier relais du devis se paie sur les clés Claude, « un relais par clé » (V9, l. 182). Une seconde table, à part, route les deux lignes à part hors de la course (§ 2.10) ; la seconde clause de l'arrêt n° 12 ne la lit pas (registre, R-4306).

Le pire d'un appel : 6,05 USD pour un proposeur (V9, l. 383). Pour l'aiguilleur et le juge, la valeur est ouverte (CV, l. 83). La configuration de la course v9 porte un plafond de session de 0,25 USD pour l'aiguilleur et de 0,60 USD pour le juge (E9, l. 41, 42) : c'est le candidat naturel, à confirmer par la mesure des consignes sans appel avant de l'écrire à l'additif. Je ne le fixe pas.

### 2.4 Portier et ses classes — module `portier`

| | |
|---|---|
| lettre | V9, l. 88, 92 à 101, 110, 148, 375 ; PS, l. 19, 21 |
| base | `pole/aiguilleur_v53.py` : une session neuve par fiche, consigne figée empreintée, une fiche anonyme par appel, passeport pour la seule fiche qui passe, journal scellé sans contenu ; une réponse illisible ou un refus de l'aiguilleur vaut aiguillage |
| classe d'issue d'appel, d'abord | par programme : au moins une fiche au contrat de sortie, « fiches rendues ». Sinon, une étiquette fermée du portier parmi trois : « réponse vide motivée », « refus du modèle », « réponse illisible ». Aucune n'est relancée. Le refus d'un classifieur de sûreté n'entre pas ici : il est lu sur le statut de l'appel (arrêt n° 1) |
| classe d'issue de fiche, ensuite | « passée », « au coffre », « hors case », exclusives. **Ordre décidé par la mère (D6)** : forme, modèle, hors case. (i) programme de forme : un champ hors des douze du contrat, « au coffre » ; **une fiche hors contrat de longueur, « au coffre » (D13, ci-dessous)** ; (ii) portier, étiquette fermée « niveau de l'idée » ou « concret » : « concret », « au coffre » ; **une réponse illisible ou un refus du modèle portier, « au coffre » (D6)**, comptée à part ; (iii) programme : un champ fermé qui diffère à l'octet de la ligne de case, « hors case » ; (iv) sinon « passée », avec passeport |
| fiche hors contrat de longueur | **règle d'écriture, décidée par la mère (D13)** : une fiche dont un champ dépasse sa borne en octets, `idee` compris, est traitée comme illisible, donc « au coffre », comptée, **jamais réparée** : ni coupée, ni ramenée sous la borne, ni renvoyée. Elle est une fiche rendue et entre dans le dénominateur de M3 et de la garde du coffre ; son compte est aussi rendu à part. L'arrêt n° 19 garde son objet : il ne peut plus être déclenché par une idée trop longue, puisque seule une fiche « passée » entre au registre servi |
| garde « hors case » | arrêt n° 4 : comparaison par programme, à l'octet, aux trois chaînes de la ligne de case ; la fiche est refusée et comptée, son texte n'est servi à personne. À la case « autre, à nommer », la valeur attendue du champ fermé est cette chaîne même (V9, l. 110) |
| garde du coffre | arrêt n° 5 : après chaque génération, part « au coffre » parmi les fiches rendues, strictement au-dessus d'un quart : la génération suivante ne part pas ; à la troisième, consigné |
| ne fait pas | juger la nouveauté ; lire la relecture ; servir quoi que ce soit du coffre |
| pièce qui manque | **la consigne du portier pour cette question** (ses deux étiquettes de fiche, ses trois étiquettes d'appel) n'est écrite nulle part : manque neuf, écrite par le modèle F et contre-lue (D3 ; § 9, point 1) |
| garde héritée à tenir | une réponse sans fiche d'un proposeur ne doit ni compter comme un échec du rôle, ni l'arrêter (§ 2.13) |

### 2.5 Juges joués pour information — module existant, câblage neuf

| | |
|---|---|
| lettre | V9, l. 64, 159 ; arrêt n° 7 |
| fait | les deux juges, des espèces 3 et 1, lisent chaque fiche « passée », une par appel, sous identifiant anonyme, comme à la course v9 ; leurs verdicts vont au coffre de la génération, leur classement est écrit dans le dossier de sortie |
| ne fait pas | entrer dans le registre servi, dans un tirage, dans une mesure autre que I1, dans un passage |
| garde | l'étape n'est lancée que sous le seuil de 120 USD (budget d'une génération, inchangé) |
| pièce qui manque | **la consigne des juges et leurs items pour cette question** : manque neuf, écrite par le modèle F et contre-lue (D3 ; § 9, point 1) |

### 2.6 Registre des tentatives, registre servi, quarantaine — modules `registre`, `verifier_registre_servi`, `quarantaine`

| | |
|---|---|
| lettre | V9, l. 62, 63 ; arrêts n° 8, 9, 17, 18, 19 ; garde-fous 2 et 3, l. 119, 120 ; clés 12 et 13, l. 308 |
| registre des tentatives | dans le dossier de sortie, ajout seul : pour chaque fiche rendue, son identifiant, sa génération, l'identifiant de sa case, sa classe d'issue ; pour une fiche « passée », ses trois champs fermés, son nom et son énoncé d'une ligne : **le nom est l'identifiant de la fiche, l'énoncé est son champ `idee` sur une ligne, espaces ramenés à un seul, sans coupe (D5)** ; rien d'un juge, rien du coût, rien de l'espèce |
| registre servi | fabriqué au départ des générations 2 et 3, à partir de toutes les générations précédentes : une ligne par tentative « passée » (trois champs fermés, nom, énoncé d'une ligne, classe « passée ») ; pour « au coffre » et « hors case », le seul compte par case ; ordre des lignes : rangées par identifiant, puis permutées par la clé 12 ou 13 ; taille bornée |
| vérification, avant tout envoi | par programme, sur le fichier entier : champs permis seulement ; une ligne par tentative ; énoncé sous sa borne ; aucune marque de code, d'étape numérotée ou de consigne (arrêt n° 19) ; aucune étiquette interdite : note, rang, verdict de juge, étiquette d'antériorité, coût (arrêt n° 9) ; consigne et registre sous leur borne (arrêt n° 8). Un défaut : la génération ne part pas ; aucune ligne n'est retirée |
| ce qu'il rend en plus | sur la ligne de la génération, ce qui a été lu : empreinte du registre servi, nombre de lignes, section servie ou omise, nombre de requêtes qui l'ont reçue (forme de `heritage_lu`, R68, § 3, point 4) |
| quarantaine | le registre servi, les fiches, les réponses brutes et le classement des juges ne quittent pas le dossier de sortie. Un programme d'export produit ce qui en sort (identifiants, empreintes, tailles, comptes par case) sur une liste fermée de champs, et refuse tout champ libre (arrêt n° 17). Deux outils à part servent la session à part : contrôle qu'une branche n'a aucun ancêtre commun avec `main`, contrôle du journal des lectures contre la liste nominative (arrêt n° 18 ; § 9, point 13) |

### 2.7 Journal — module `journal`

| | |
|---|---|
| lettre | V9, l. 77, 156, 315 ; OC, l. 39, 54 |
| journal des requêtes | une ligne par envoi (§ 2.3, pas 4), ajout seul, dans le dossier de sortie ; jamais servi ; scellé à la fin de chaque génération |
| ligne de la génération | cases servies (identifiants), fiches rendues, comptes par classe et par case, classes d'issue d'appel, coût par espèce et par rôle, ce qui a été lu de la précédente |
| journal des arrêts n° 11 à n° 13 | le cumul par clé ne vit que là : il n'entre ni dans M4 ni dans ce qui est rendu à la composition (V9, l. 156) |
| arrêts | chaque arrêt est écrit avec son numéro et son nom, la génération, le poste ; pour l'arrêt n° 16, la famille et le rang dehors, le texte trouvé dedans |

### 2.8 Mesures M1 à M7, C1 et I1 — module `mesures`

| | |
|---|---|
| lettre | V9, l. 84, 146 à 163, 315, 328, 362 ; arrêt n° 15, l. 386 ; CV, l. 189 |
| lit | le registre des tentatives, les lignes des générations, le journal, le tirage scellé ; l'attestation scellée de la relecture « aucune recette » (une étiquette par identifiant de fiche : gardée, ou au coffre) ; pour M5, les étiquettes scellées de la lecture d'antériorité et, branche « avec », les classes de l'épreuve 4 et le compte des désaccords |
| rend | chaque part avec son numérateur et son dénominateur ; M1 et M1 bis par génération et par espèce ; M2 ; M3 par génération et par case ; M4 ; M6 ; M7 ; C1 ; I1 sous le titre « pour information » ; seuls des comptes, des parts et des identifiants sortent du dossier |
| garde | arrêt n° 15 : refus de calculer tant que le bilan de course ne dit pas trois générations complètes, ou un arrêt nommé, et tant que l'attestation de relecture ou les étiquettes scellées d'antériorité manquent ; une seule lecture, consignée ; la seconde est refusée |
| une seule lecture | **la lettre de la V9 est gardée** (l. 315, « lues une fois ») : le programme calcule toutes les mesures en une lecture, et refuse la seconde. M5 exigeant les étiquettes scellées de la lecture d'antériorité, cette lecture unique ne peut se faire qu'une fois ces étiquettes scellées : aucune mesure n'est donc lue avant. L'option de deux lectures est notée à part et soumise à Lazar (§ 9, point 11 ; D12) ; le véhicule ne la porte pas |
| course arrêtée | V9, l. 362 : mesures sur les seules générations complètes, sous le titre « course arrêtée par [nom de l'arrêt] » ; M1 et M2 « sans objet » si la seule génération 1 est complète ; épreuve au § 6.2 |
| M4 et les clés | M4 ne lit jamais le cumul par clé, qui ne vit qu'au journal des arrêts n° 11 à n° 13 (V9, l. 156) ; épreuve au § 6.2 |

### 2.9 Génération et course du régime — modules `course` et lanceur de l'orchestrateur

| | |
|---|---|
| lettre | V9, l. 60, 61, 402, 419 ; OC, l. 33 ; arrêts n° 5, 6, 7, 10, 14 |
| génération | une classe neuve qui hérite de `GenerationV68` : elle lui passe un héritage `None`, parce que le constructeur de la v68 n'accepte que l'objet de sélection d'un étage (`course2_v68.py`, l. 164) et refuserait le registre ; elle sert le registre par sa propre proposition ; ses cases sont celles de sa génération, lues au tirage scellé ; sa proposition assemble la requête par le module `requete`, sans la section « Case » de la v54 ; ses étapes sont « proposition », « aiguillage », « juges », et aucune autre [lot 0, question 3] ; son portier est celui du § 2.4 ; elle lève l'arrêt armé par l'adaptateur gardé au retour de chaque appel (§ 2.3) ; sa lecture d'une réponse de proposeur rend toujours un objet lisible dès qu'un texte est rendu (§ 2.13) |
| course | une fonction neuve sur le modèle d'`executer_course_v68`, qu'elle n'appelle pas, non plus que `verifier_regime_v68` (§ 1.2) : trois générations exactement ; au départ de chacune, garde d'empreintes (arrêt n° 14), garde de disjonction (arrêt n° 10), registre servi fabriqué et vérifié (arrêts n° 8, 9, 19), réservation de 150 USD sur le plafond de 450 (arrêt n° 6) ; après chacune, garde du coffre (arrêt n° 5), ligne de la génération, sceaux |
| lanceur de l'orchestrateur | lève le refus du moteur réel **pour ce seul régime**, à quatre conditions tenues ensemble : le nom du régime ; la ligne d'accord au montant exact ; l'additif du véhicule épinglé à son empreinte ; trois générations, aucun étage. Tout autre jeu d'options reste refusé, moteur simulé compris hors de l'essai à blanc |
| composition | figée dans la configuration : cinq proposeurs, un aiguilleur, deux juges ; 55 appels de proposeur par génération ; rien n'apprend ni ne se réécrit (V9, l. 61) |

La garde d'empreintes lit une table scellée, portée par la configuration : la partie servie, la synthèse servie, les consignes du portier et des juges, les témoins plantés, la question (jamais ouverte : son empreinte seule), la liste des motifs et son programme, la configuration, l'additif, le tirage, la V9, A1, CV, AC. Elle nomme la pièce fautive.

### 2.10 Épreuve des témoins plantés et sondes de refus — modules `epreuve_temoins`, `sonde_refus`

| | épreuve des témoins | sonde de refus |
|---|---|---|
| lettre | V9, l. 129, 374, 375 ; CV, l. 122 à 126 ; gabarit, § 2 et § 5 | A1, l. 118, 160 ; V9, l. 373 ; DV, l. 418 ; AC, l. 120 à 128 |
| base | E9 : une épreuve par tentative, mode hors ligne à juges factices, sonde du bac, manques techniques dits « non conclue », rapport scellé exigé par le lanceur, du jour, à ses empreintes | la sonde minimale de la clé Luc pour la manière (une requête, un relais épinglé, arrêt par identifiant) |
| envoie | chaque partie présentée d'un témoin au portier, et aux deux juges pour information ; les deux réponses sans fiche au chemin des classes d'issue d'appel | cinq requêtes, une par proposeur : la partie servie remplie de la première case de la réserve, seule ; sortie bornée |
| passe | garde d'empreintes, garde de motifs sur chaque requête et sur chaque témoin, journal | garde d'empreintes, garde de motifs, journal |
| lit | l'issue de chaque témoin contre la table scellée des issues attendues, par programme | « accepte » ou « refuse », **par programme seul (D7)** : au moins une fiche complète au contrat, « accepte » ; statut de refus d'un classifieur, arrêt n° 1 ; tout le reste, arrêt n° 27 (§ 9, point 7) |
| arrêts | n° 3 : un témoin manqué, aucune course ; n° 4 : l'épreuve de la garde « hors case » | n° 1 : refus d'un classifieur ; n° 2 : l'espèce refuse ; n° 27 : refus pour crédit, erreur d'accès, réponse illisible : non relancée, départ refusé |
| routage, hors de la course | portier et juge de l'espèce 3 sur Minuit ; juge de l'espèce 1 sur le deuxième relais | espèces 3 et 4 sur Minuit ; espèces 1 et 5 sur le deuxième relais ; espèce 2 sur le troisième, après le relevé de son statut |
| plafond | 5 USD, ligne à part | 1 USD, ligne à part |
| rend | un rapport en deux parts : dans le dossier de sortie, les réponses brutes ; dehors, par témoin, l'issue attendue, l'issue lue, « tenu » ou « manqué », le coût | par espèce : l'issue, le coût, l'empreinte et la taille de la réponse ; la réponse brute reste dans le dossier de sortie |

### 2.11 Lanceur de course — script `lancer_course_nouvelles_attaques_v1.py`

Il suit, point par point, ce qu'A69, dans sa v4 scellée (`cb352811…`), § 7, demande au lanceur 11, transposé à ce régime. Je tiens la lettre du point 7 de la v4 de CL, § 1.5 ; les autres points sont ceux de la v1 que j'ai lue, à comparer à la v4 par le vérificateur du lot 8. Les chemins et empreintes épinglés du code de base citent la branche `verse/vehicule-na-v1`, commit `61987a3a` (D10).

| A69, v4, § 7 | ce que le lanceur neuf épingle ou vérifie |
|---|---|
| 1 | les empreintes des fichiers de base de l'orchestrateur (liste de L10, l. 534 à 561), les huit du paquet v68, et chaque fichier neuf du véhicule |
| 2 | sans objet : aucun étage, aucune chaîne du tour fermé |
| 3 | l'additif du véhicule, scellé, à son chemin et à son empreinte |
| 4 | la V9, A1, CV, AC, le devis v11, la configuration, le tirage scellé, la partie servie, la synthèse servie, les consignes du portier et des juges, les témoins et leur table, la liste des motifs et son programme, la pièce de relevés du jour |
| 5 | le seul appel permis : le lanceur de l'orchestrateur du § 2.9, régime nommé, trois générations ; tout autre jeu d'options refusé |
| 6 | le montant requis, recoupé sans écriture avec l'orchestrateur : 450 USD ; la ligne d'accord de la course à ce montant exact ; les lignes à part à 5 et à 1 USD |
| 7 | les bornes des relais comptées pour trois générations ; le plafond de chaque relais égal à la part de sa clé, **non à la ligne de course** (V9, l. 235) : un relais déclaré au-dessus de la part de sa clé est refusé au départ ; arrêt n° 11 au départ ; **le relevé de ce qui reste sur chaque clé avant et après la course** (ajout de la v4 : « R-3209, point 2 ») : avant, c'est la pièce de relevés ; après, le lanceur écrit, par clé désignée par son nom d'usage, le cumul compté et le reste qui s'en déduit, au journal des arrêts n° 11 à n° 13 et là seulement (V9, l. 156), jamais dans M4 |
| 8 | la relecture, par comptes, du budget de course et du bilan ; les coûts par espèce et par rôle, génération par génération |
| 9 | sans objet : aucun interrupteur |
| 10 | sans objet : aucune machine louée |

**Arrêt n° 11.** Le lanceur lit la pièce de relevés scellée par la mère, à son empreinte, datée du jour, dans ses cinq lignes à libellé fixe (AC, l. 136 à 144). Minuit et Luc : reste calculé, comparé à la part ; un centime sous la part, refus. Deuxième relais : statut « payant » attesté ; sans relevé ou non payant, refus ; jamais d'euros comparés à des dollars (CV, l. 140 à 146). Troisième relais : statut « recharge automatique » attesté ; sinon, reste relevé en dollars lu contre 17,01 USD (AC, l. 175). Rigaud : rien à lire pour le départ.

**Manifeste de run** (V9, l. 313 ; règle R9) : version de `numpy`, racine, clés de tirage, commits des deux dépôts, empreintes de tout ce qui est épinglé, table des rôles et des clés par nom d'usage, valeurs jamais lues.

### 2.12 Moteur simulé, faux fournisseur, essai à blanc, mesure des consignes — module `simulation`, scripts d'essai

| | |
|---|---|
| lettre | V9, l. 384, 409 ; règle R5, l. 368 |
| moteur simulé | adaptateurs simulés au contrat de cette course : des proposeurs qui rendent, selon l'empreinte de l'identifiant, des fiches au contrat, une fiche à un champ de plus, une fiche à champ fermé différent, une réponse sans fiche de chaque sorte ; un portier et des juges simulés aux étiquettes fermées. Textes inertes, sans rapport avec la question |
| faux fournisseur | un amont local derrière les vrais relais : il garde ce qu'il reçoit, et rend à la demande une réponse normale, un refus pour crédit, une erreur d'accès, un refus de classifieur, une réponse coupée |
| essai à blanc | la course entière, trois générations, par le lanceur, en moteur simulé, puis par les relais contre le faux fournisseur ; les deux lignes à part de même ; chaque arrêt provoqué une fois (§ 6) |
| mesure des consignes sans appel | assemble les trente-trois requêtes de proposeur de la génération 1, les plus grandes requêtes possibles des générations 2 et 3 à la borne du registre, les requêtes du portier et des juges sur la plus grande fiche permise ; rend les tailles en octets par rôle et le pire d'un appel par rôle, à la règle de compte et au relevé de tarif du devis ; ces chiffres vont à l'additif (bornes en octets, pire d'un appel d'aiguilleur et de juge) |

### 2.13 Les gardes héritées du noyau, que la V9 ne porte pas (CL, § 2.1)

Le noyau gardé tient des gardes d'arrêt par rôle que la V9 n'écrit pas. Laissées telles quelles, elles agiraient dans la course sans nom d'arrêt de la V9. Chacune est donc **rattachée à un arrêt de la V9, ou rendue inerte par une valeur déclarée à l'additif** ; une garde gardée sans arrêt de la V9 est une proposition à la mère. La liste complète, fichier et ligne, est relevée [lot 0, question 12] : ce qui suit est ce que j'en ai lu (`suivi_roles_v54.py`, `620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb`, l. 1 à 95 ; `noyau_v56.py`).

| garde héritée | ce qu'elle fait | ce qu'elle heurte | sort proposé |
|---|---|---|---|
| **A3**, échecs consécutifs | un appel coupé, ou dont la lecture rend « rien », est un échec ; un nombre fixé d'échecs de suite arrête le rôle, et ses appels suivants ne sont plus lancés (`suivi_roles_v54.py`, l. 5 à 7, 72 à 83 ; `noyau_v56.py`, l. 155 à 160) | **la « réponse vide motivée »** : sans fiche, elle serait lue « rien » ; un proposeur qui répond à bon droit sans fiche à quelques cases de suite serait arrêté sans bruit. Contraire à V9, l. 97 (« jamais un refus »), l. 101 (« la course continue »), à M6, aux 55 appels figés (A1, l. 142, 161) | **deux tenues, ensemble** : (i) la lecture d'une réponse de proposeur rend un objet dès qu'un texte est rendu, avec ou sans fiche ; le classement en quatre classes d'issue d'appel se fait après, par le portier (§ 2.4) ; une réponse sans fiche n'est donc jamais un échec du rôle ; (ii) le nombre d'échecs consécutifs qui arrête un rôle est déclaré à l'additif au-dessus du nombre d'appels du rôle sur la course : la garde est inerte, et le dit. Les appels coupés et sans texte restent comptés (M6, « réponse illisible »), non relancés |
| **A14**, part d'appels inexploitables | au-delà d'une part, l'étape est marquée « non mesurée (technique) » (`noyau_v56.py`, l. 273 à 278) | aucun seuil d'arrêt n'est posé sur M6 (V9, l. 101) | rendue inerte : part maximale déclarée à 1 à l'additif ; M6 rapporte |
| **A11 et A2**, modèle servi différent du modèle demandé, limite d'usage | arrêt du rôle, sans bascule (`suivi_roles_v54.py`, l. 63 à 67, 80, 81 ; `noyau_v56.py`, l. 176 à 185, 205 à 211) | la composition figée (V9, l. 61) : un rôle arrêté en course n'est plus la composition du texte | rattachée à « aucune bascule » (V9, l. 182) pour le refus de tout autre modèle ; **son effet en course est une proposition à la mère** : arrêt nommé de la course plutôt qu'arrêt silencieux du rôle |
| **coupure au plafond dur de l'étape** | quand le reste de l'étape est nul, l'appel n'est pas lancé et rend « rien » (`noyau_v56.py`, l. 150 à 154) | rien : c'est le plafond dur de la proposition, 140 USD | rattachée à l'arrêt n° 7 ; chaque appel non lancé est écrit à la ligne de la génération, compté à part, jamais dans M6 |
| **11a**, cumul au-delà du plafond de la génération après une étape | arrêt (`noyau_v56.py`, l. 280 à 282) | rien | rattachée à l'arrêt n° 6 |
| **garde propre à un fournisseur** (débordement d'un proposeur, `aiguilleur_v53.py`, l. 109 à 130) | arrête le rôle d'un proposeur d'un fournisseur nommé | aucune espèce de cette course n'est de ce fournisseur | sans objet ; vérifié à la configuration |

Épreuve (§ 6.2) : onze réponses vides motivées consécutives d'un même proposeur ne l'arrêtent pas, aucun de ses appels n'est sauté, et chacune est classée et comptée à M6.

### 2.14 La colonne « matière première » — possibilité, éteinte par défaut — module `matiere_premiere`

**La colonne « matière première » est une possibilité, désactivée par défaut, dont la course ne dépend pas : la course part sans elle, ses épreuves de cas sain et d'artefact restent écrites, et le lot qui l'écrit est facultatif et hors du chemin critique.**

*D'où elle vient.* Un mot de Lazar, que la mère dit inscrit en GO-2026-11-21-19 et relaie vers 07:14Z, verserait à la course, comme matière première, des modes écrits en quarantaine sur une branche orpheline, sur le précédent des idées des mentors (N-072). La mère a corrigé à 07:15Z : **cette matière n'existe pas à ce jour, rien n'a été écrit, et la décision revient à Lazar.** Je n'ai lu ni cet accord, ni N-072, et je n'ouvre pas cette branche : je conçois sur la forme seulement. La colonne n'est dans aucun texte scellé de la course : l'allumer est un écart à la V9, donc un additif contre-lu et le mot de Lazar.

| | |
|---|---|
| ce qu'elle est | une colonne tenue à l'écart des proposeurs, lue à la fin par les lecteurs d'antériorité et par les juges de la course, sans passer par aucun proposeur |
| entrée | un fichier scellé, fait du côté de la quarantaine, posé dans le dossier de sortie : une ligne par entrée, à trois champs : un identifiant de ligne, **un nom neutre, un énoncé d'une ligne**, dans la forme d'une ligne du registre servi ; l'empreinte de chaque ligne et celle du fichier ; le nom de la branche et son commit. **Jamais un procédé.** La mère donne le chemin, le commit et les empreintes |
| à l'entrée | chaque ligne passe le programme de vérification du registre servi (champs permis seuls, une ligne par entrée, énoncé sous sa borne, aucune marque de code, d'étape numérotée ou de consigne : forme de l'arrêt n° 19) et la garde de motifs ; une ligne non conforme : la colonne n'est pas chargée, rien n'est retiré en silence |
| interrupteur | `colonne_matiere_premiere`, éteint par défaut, sans chemin d'allumage par variable ni par configuration seule. Allumé, il exige : l'additif à la V9 épinglé, le fichier de la colonne à son empreinte sous l'arrêt n° 14, une ligne d'accord qui le nomme. Éteint, le module n'est pas chargé |
| **garde de la colonne** | trois tenues : (i) le module `requete` n'a aucune entrée par où la colonne puisse arriver : la requête d'un proposeur n'est composée que des pièces du § 5.3, par liste fermée ; (ii) dans l'adaptateur gardé, pour tout rôle de proposeur et pour la sonde, la requête assemblée est comparée, après la normalisation de la garde de motifs, à chaque nom et à chaque énoncé de la colonne : une présence refuse l'envoi, « non envoyé », arrêt nommé ; (iii) aucun identifiant de la colonne n'entre au registre des tentatives ni au registre servi, vérifié au départ des générations 2 et 3. Cet arrêt n'a pas de numéro dans la V9 : l'additif le lui donne |
| lecture à la fin | après la troisième génération : chaque ligne est présentée aux deux juges, pour information, et aux lecteurs d'antériorité, sous un identifiant que rien ne distingue de celui d'une fiche de la course. *Proposition* : les lignes sont lues en plus des soixante fiches, comme les témoins |
| « affinés par l'organisme » | **proposition, marquée, non tranchée.** Aucun affinage ne peut passer par les cinq proposeurs sans leur servir la ligne, ce que le mot interdit. Deux voies : (a) *par défaut, celle que le lot écrit* : aucun affinage dans ce véhicule ; la ligne va telle quelle à la lecture de fin ; (b) *option* : une passe à part, après la troisième génération, par un rôle distinct des proposeurs, qui ne reçoit que le nom et l'énoncé d'une ligne et les récrit au niveau de l'idée dans les douze champs d'une fiche, pour qu'ils passent le même portier que les idées de la course ; jamais le procédé ; ses fiches portent l'origine « matière première », n'entrent ni au registre servi ni dans M1 à M7, et se paient sur une ligne à part. La voie (b) sert un texte neuf à un rôle neuf : un devis, un additif, le mot de Lazar |
| comparaison finale | **sans juge qui décide** (N-058) : une table descriptive, par programme, de deux colonnes, « idées de la course » et « matière première » : comptes par étiquette d'antériorité, par classe de l'épreuve 4, par classe du portier si la voie (b) est jouée. Le classement des juges y figure à part, « pour information ». Aucune phrase ne dit qu'une colonne vaut mieux ; l'épreuve, sur devis, est hors de cette course |
| mesures de la course | inchangées : aucune ligne de la colonne n'entre dans M1 à M7, C1 ni I1 de la course |
| point pour la mère | le mot relayé fait sortir de la branche des noms et des énoncés d'une ligne ; la V9 veut « ni énoncé ni nom de mode dans un registre du dépôt, une passation ou un message » (l. 83). Dans le véhicule, le fichier de la colonne reste dans le dossier de sortie, et seuls des identifiants, des empreintes et des comptes en sortent ; le reste est à dire par la mère et par Lazar |

### 2.15 Le lecteur de la liste nominative qui ouvrirait la branche

Sur la forme seulement. Rien de ce paragraphe ne s'ouvre tant que la matière n'existe pas et que Lazar n'a pas tranché.

| | |
|---|---|
| qui | deux rôles que le mot relayé nomme : le concepteur et l'opérateur du banc. Des sessions à part ; jamais la mère, ni une session qui conçoit sondes, agrégateurs, traits de texte ou seuils. Leur inscription à une liste nominative est un mot de Lazar, comme la cinquième entrée de la liste de la course (GO-2026-11-20-65). Cette branche est une autre quarantaine que celle de la course : *proposition*, sa liste est tenue à part, par la mère, sans nom ni énoncé |
| quand | au moment de l'épreuve, hors de cette course, sous les garde-fous 1, 4 et 5 de la V9 (arrêts n° 20 à n° 22) : après l'étiquette scellée d'antériorité, sur le banc scellé, sous une ligne d'accord qui cite l'exécution |
| ce qu'il lit | sur la branche, au commit et aux empreintes donnés par la mère : le procédé des seules lignes retenues pour l'épreuve, et rien d'autre de la branche |
| ce qu'il écrit | avant chaque ouverture, une ligne au journal des lectures : son rôle, l'heure, le commit, les empreintes de ce qu'il ouvre ; après, ce que le texte préenregistré de l'épreuve lui fait écrire. Hors de la branche : des identifiants, des empreintes, des tailles, des comptes |
| preuve, arrêt n° 17 | par programme (outil du § 2.6) : la branche n'a aucun ancêtre commun avec `main` ; aucune empreinte d'un fichier de la branche ne se retrouve dans l'arbre de travail, dans le dossier du run ni dans un export ; tout export est fait sur une liste fermée de champs |
| preuve, arrêt n° 18 | par programme : chaque ouverture a sa ligne, écrite avant elle, par un rôle inscrit ; une lecture sans ligne, ou par un rôle absent de la liste, est refusée là où un programme la tient, sinon constatée, consignée et portée à Lazar |
| preuve, arrêt n° 19 | toute ligne qui sort de la branche (nom neutre, énoncé d'une ligne) passe d'abord le programme de vérification du registre servi et la garde de motifs ; non conforme, rien ne sort, sans retrait silencieux |
| limite, dite sans forcer | la règle d'ouverture se tient par procédure et par journal, non par une serrure : une lecture hors règle se constate, elle ne s'empêche pas toujours (V9, l. 125) |

## 3. Vue d'ensemble

```
lanceur de course ──(vérifie, épingle, arrêt n° 11, relais par clé)──► lanceur de l'orchestrateur (régime nommé)
                                                                              │
        tirage scellé ─► course : 3 générations ─► génération g ─► proposition ─► aiguillage ─► juges
                              │  (arrêts 14, 10, 8, 9, 19, 6)                  │              │
                              │                                 module requete │              │
                              ▼                                                ▼              ▼
                    registre des tentatives ◄── portier ◄──────  adaptateur gardé (routage, part, motifs, journal)
                              │                                                │
                    registre servi (g+1), ligne de génération        relais de la clé ─► fournisseur
                              │
                    mesures (après la relecture) ─► export hors quarantaine (comptes seulement)
```

## 4. Ce qui est scellé, et par qui

| pièce | qui l'écrit | qui la contre-lit ou la vérifie | qui la scelle | servie ? |
|---|---|---|---|---|
| code du véhicule, lot par lot | modèle O | modèle S | empreintes au manifeste du paquet ; épinglées par le lanceur | — |
| véhicule entier, additif, garde de motifs | — | un autre modèle (règle R2), avec la confirmation de la répartition | — | — |
| additif du véhicule | modèle F | un autre modèle | la mère | non |
| configuration de course | modèle O, sur les valeurs de l'additif | modèle S | la mère, avec l'additif | non |
| consignes du portier et des juges | modèle F (D3) | un autre modèle (D3) | la mère, après son attestation « aucune recette » | oui, au portier et aux juges |
| liste des motifs | modèle F | avec le véhicule | la mère | jamais |
| sortie du tirage | le programme, joué deux fois par la session de l'organisme | égalité par `cmp` | la mère, avant tout appel payant | non ; les lignes de case qui en sortent le sont |
| témoins plantés et table des issues | un agent neuf de la mère | — | la mère | les parties présentées, à l'épreuve |
| pièce de relevés | la mère, par programme | `cmp` | la mère | non |
| journal, registre des tentatives, registre servi, fiches, réponses brutes, classement des juges | le véhicule | — | le véhicule, par compagnon, dans le dossier de sortie | le registre servi seul, aux proposeurs |
| rapports des lignes à part, bilan de course, mesures | le véhicule | constat par la mère, sur les parts hors quarantaine | le véhicule, puis la mère au registre | non |

## 5. Les interfaces

### 5.1 Entrées et sorties, module par module

| module | entrées | sorties | lu ensuite par |
|---|---|---|---|
| `tirage` | gabarit (empreinte), racine, clés | fichier du tirage ; table des identifiants | `requete`, `course`, `mesures`, lanceur, témoins |
| `requete` | gabarit, synthèse, ligne de case, registre servi, consignes fixes, enveloppe | octets de la requête ; composition (pièces, tailles) | adaptateur gardé |
| `garde_motifs` | octets ; liste scellée | « passe », ou famille et rang ; texte trouvé vers le journal | adaptateur gardé ; départ ; épreuves |
| `routage` | rôle, clé, table scellée, parts, pires par rôle | « permis », ou arrêt n° 12 nommé | adaptateur gardé |
| `journal` | ligne d'envoi ; ligne de génération ; arrêt | fichiers d'ajout seul, scellés par génération | `mesures`, export, essai à blanc |
| `portier` | réponse d'un proposeur ; ligne de case ; consigne | classe d'issue d'appel ; fiches et leur classe ; passeports | `registre`, juges, `mesures` |
| `registre` | fiches classées | registre des tentatives ; registre servi | `requete`, `verifier_registre_servi`, `mesures` |
| `verifier_registre_servi` | registre servi ; bornes | « conforme », ou arrêt n° 8, 9 ou 19 nommé | `course` |
| `course` | configuration, tirage, adaptateurs gardés | dossiers des générations ; bilan de course | lanceur, `mesures` |
| `mesures` | registre, journaux, tirage, attestations scellées | mesures, dans le dossier ; part exportable | export |
| export | dossier de sortie | inventaire hors quarantaine | dossier du run, la mère |
| `sonde_refus`, `epreuve_temoins` | tirage, témoins, table des issues, tables de routage à part | rapports en deux parts | lanceur (exigés, du jour, aux empreintes du véhicule) |

### 5.2 L'identifiant neutre, et celui des témoins

Contraintes de la lettre (V9, l. 75) : ni rang, ni numéro sur un total, ni morceau d'empreinte ; aucune suite de huit caractères hexadécimaux ; rien qui laisse déduire le compte des cases, l'ordre du tirage, la génération ou la famille tenue à l'écart.

**La clé de tirage n° 40 est décidée par la mère (D4).** La forme du mot reste une valeur du concepteur, à écrire à l'additif :

- un mot de trois syllabes, chaque syllabe faite d'une consonne prise dans douze et d'une voyelle prise dans cinq, les consonnes choisies hors des lettres qui servent à écrire l'hexadécimal ; six lettres, aucun chiffre : jamais huit caractères hexadécimaux de suite ;
- 216 000 mots possibles pour 120 cases : le mot ne dit rien du compte ;
- les 120 mots sont tirés une fois, sans remise, pour **toutes** les cases, dans l'ordre canonique, par une **clé de tirage neuve, la clé n° 40 (D4)** : `rng.choice(216000, size=120, replace=False)` sur `SeedSequence(entropy=racine, spawn_key=(40,))` ; un mot ne dépend donc ni de la génération, ni du fait que la case soit servie, tenue à l'écart ou en réserve ;
- la lettre le permet : « si sa construction demande un tirage, c'est une clé de tirage neuve, qui ne change aucun tirage écrit » (V9, l. 75, 254) ; elle la veut « portée au complément contre-lu », et il n'y a pas de lot 2 : où elle se porte est au § 9, point 4 ;
- la table des 120 mots sort du tirage, scellée avec lui ; elle n'est jamais servie ; chaque mot passe la garde de motifs avant le scellement ; un mot qui la ferait refuser arrête le tirage par un refus nommé, sans second tirage en silence.

**La ligne de case.** Proposition : `case : <identifiant> ; <valeur 1> ; <valeur 2> ; <valeur 3>`, les trois valeurs à l'octet de la légende, le séparateur « ; » encadré d'une espace de chaque côté (aucune valeur de la légende ne le porte ; deux portent une virgule, deux des parenthèses). Borne : 256 octets, gardée ; la plus longue ligne possible est à mesurer par le programme, je l'estime sous 200 octets.

**Les témoins.** Le gabarit attend de l'additif l'identifiant neutre et la ligne de case que porte un témoin (gabarit, l. 61, 98). Proposition (§ 9, point 8) : tous les témoins portent **la première case de la réserve**, celle de la sonde de refus : elle n'est ni servie par la course, ni de la famille tenue à l'écart, elle n'est déjà plus fraîche, et aucune case de plus n'est consommée. Leur champ `case` prend le mot de cette case dans la table scellée ; leur ligne de case est construite par le même programme que les trente-trois autres. Les témoins ne peuvent donc être scellés qu'après le tirage.

### 5.3 L'enveloppe de la requête

Valeur ouverte, à l'additif (V9, l. 254). **Décision de la mère (D2) : rien n'est ajouté à l'enveloppe.** Elle ne porte donc que des séparateurs et, aux générations 2 et 3, le titre de la section du registre ; aucun texte sur la syntaxe de sortie, aucun texte fixe de rôle (§ 2.3). Forme proposée, à écrire à l'additif :

| rôle | suite d'octets |
|---|---|
| proposeur, génération 1 | partie servie remplie ; une ligne vide ; synthèse servie à l'octet |
| proposeur, générations 2 et 3 | la même ; une ligne vide ; le titre de la section du registre, sur une ligne ; le registre servi. Si le registre est vide : section omise, la requête est celle d'une génération 1, et la ligne de la génération le dit (défaut de la v68, R68, § 3, point 5) |
| sonde de refus | partie servie remplie, seule |
| portier, juge | leur consigne fixe ; une ligne vide ; la fiche, dans la forme servie par l'orchestrateur |

Le titre de la section et la règle du registre vide restent des valeurs ouvertes de l'additif (§ 9, point 3). Pour le portier et un juge, « leur consigne fixe » est la pièce de D3, et rien d'autre.

### 5.4 Le contrat de sortie d'une fiche

Les douze champs de PS, l. 19, tous des chaînes. Une fiche est reconnue quand les douze sont présents. **Sous D2, le lecteur de fiches accepte deux syntaxes**, puisque rien ne dit au proposeur laquelle écrire : un objet structuré par fiche, ou des lignes « champ : valeur » ; ce que lit le lecteur existant est relevé [lot 0, question 6]. Un champ de plus ne sort pas la fiche du contrat : il l'envoie au coffre. **Une fiche hors contrat de longueur** (un champ au-dessus de sa borne en octets, `idee` compris ; bornes à l'additif, sur la mesure) **est traitée comme illisible, donc « au coffre », comptée, jamais réparée (D13).** La part « réponse illisible » de l'essai à blanc et de la sonde est regardée avant le départ.

## 6. Les épreuves

Chaque garde et chaque arrêt confié au véhicule, avec son cas sain et son artefact (règle R5). « Lot » dit où l'épreuve s'écrit ; toutes sont rejouées à l'essai à blanc du lot 9. Les arrêts n° 20 à n° 26 gardent ce qui suit la course et ne sont pas dans le véhicule.

### 6.1 Arrêts nommés

| arrêt | cas sain | artefact | lot |
|---|---|---|---|
| n° 1, refus d'un classifieur | réponse normale : lue | refus de classifieur simulé par le faux fournisseur : consigné sous son nom, non relancé | 4, 9 |
| n° 2, espèce qui refuse à la sonde | cinq acceptations : départ permis | une espèce refuse : retirée, la course ne part pas | 9 |
| n° 3, témoin manqué | tous les témoins à leur issue attendue | un témoin dont l'issue lue diffère : « aucune course » | 9 |
| n° 4, garde « hors case » | une fiche dans sa case passe | le témoin « hors case », puis une fiche dont un champ fermé diffère d'un octet : refusées et comptées ; une fiche hors case à champ de plus : au coffre | 5, 9 |
| n° 5, garde du coffre | un quart exactement au coffre : la génération suivante part | une fiche de plus au coffre : elle ne part pas ; à la troisième génération : consigné | 5, 6 |
| n° 6, plafonds | réservation égale au reste : permise | réservation d'un centime de trop : arrêt avant le poste ; poste plus cher que sa réservation : arrêt (essais de la v68 repris) | 6 |
| n° 7, seuils d'une génération | cumul à 135 et à 120 : aiguillage et juges lancés | cumul d'un centime au-dessus : poste non lancé, consigné | 6 |
| n° 8, consigne trop longue | requête égale à sa borne : départ | un octet de plus : départ refusé | 5, 6 |
| n° 9, étiquette interdite au registre | registre sans étiquette : passe | une ligne qui porte chacune des cinq étiquettes, tour à tour : la génération ne part pas, aucune ligne retirée | 5 |
| n° 10, disjonction | trente-trois cases distinctes, hors de la famille tenue à l'écart | une case de cette famille, puis une case déjà servie, plantées dans une copie du tirage : départ refusé | 1, 6 |
| n° 11, reste sous la part | reste égal à la part : départ | un centime sous la part : refus ; relevé absent ; compte dit non payant, crédit en euros : refus nommé ; troisième relais sans recharge automatique et reste en dollars au-dessus, puis au-dessous de 17,01 | 8 |
| n° 12, part épuisée, étendu (**D11, acceptée par la mère, telle que CL, § 5, la propose**) | un appel qui tient sous la part, sur sa clé : lancé et compté sur elle, pour chacune des quatre clés ; **cas sain neuf : le juge et le proposeur de l'espèce 3, tous deux sur Minuit, sont lancés et comptés sur Minuit, la part cumulant les deux rôles** (AC, l. 56, 72) : l'ancien artefact de V9, l. 383, est devenu un cas permis | un appel qui dépasserait la part d'un centime : refusé, arrêt nommé ; **artefact en course : l'aiguilleur présenté sur Minuit est refusé** (Minuit est sa clé à l'épreuve des témoins, non en course : la table de la course ne lit pas celle des lignes à part) ; **artefact sur table plantée** : une copie de la table des rôles et des clés, marquée artefact, jamais chargée par la course (donnée à la course, son empreinte est refusée par l'arrêt n° 14), où le juge et le proposeur de l'espèce 3 sont sur deux clés : le juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 y est refusé ; **mutation « routeur par espèce »** : le routeur remplacé par une recherche par espèce laisse passer cet artefact, et l'essai doit échouer ; le proposeur de l'espèce 2 présenté sur le deuxième relais (CV, l. 166) ; **un envoi adressé à Rigaud** (AC, l. 175) : refusés ; en plus, le juge de l'espèce 3 présenté sur la clé de l'aiguilleur. Les deux lignes à part, par leur table : non refusées | 4 |
| n° 13, refus pour crédit | réponse normale | refus pour crédit simulé : arrêt nommé, qui dit la clé ; aucune bascule | 4, 8 |
| n° 14, empreinte différente | toutes égales : départ | un octet changé dans la partie servie, puis dans la liste des motifs, puis dans une consigne, puis dans le tirage : refus qui nomme la pièce ; rejoué au départ de la génération 2, de la sonde et de l'épreuve | 6, 9 |
| n° 15, mesure lue trop tôt | bilan à trois générations, attestation de relecture et étiquettes d'antériorité scellées présentes : calcul, une fois | bilan à deux générations sans arrêt nommé ; attestation absente ; étiquettes d'antériorité absentes ; seconde lecture : refus | 7 |
| n° 16, motif interdit | les requêtes des trente-trois cases passent ; chaque témoin positif mord ; le gabarit, la synthèse et les témoins passent sans un refus | par famille : un motif planté en clair, puis sous une forme que la normalisation ramène : refus qui nomme la famille et le rang ; un motif qui ne mord pas sur son témoin positif : départ refusé | 2, 4 |
| n° 17, quarantaine rompue | export aux seuls champs permis | un champ libre planté dans l'export : refus ; une branche tirée de `main` : refus | 7 |
| n° 18, lecture hors liste | lecteur inscrit, ligne écrite | lecteur absent de la liste ; lecture sans ligne : refus, consigné | 7 |
| n° 19, registre servi non conforme | registre aux seuls champs permis : passe | un champ de plus ; deux lignes pour une tentative ; un énoncé d'un octet de trop ; une marque de code ; une étape numérotée : refus, sans retrait | 5 |
| n° 27, sonde illisible | réponse lisible : issue lue | refus pour crédit, puis erreur d'accès, puis réponse coupée : non relancée, départ refusé, consigné | 9 |

### 6.2 Gardes sans numéro

| garde | cas sain | artefact | lot |
|---|---|---|---|
| partie servie | le gabarit à son empreinte est rempli et envoyé au moteur simulé | le chemin de la question à la place du gabarit ; un gabarit à zéro, puis à deux emplacements : refusés | 3 |
| ligne de case | les trente-trois lignes passent le contrôle | une valeur qui diffère d'un octet ; un identifiant numéroté sur un total ; huit caractères hexadécimaux de suite : départ refusé | 1 |
| requête journalisée | la requête rejouée à partir des pièces scellées rend l'empreinte du journal | un octet changé après la journalisation : envoi refusé ; un appel sans ligne de journal : ne part pas | 3, 4 |
| tirage | deux jeux égaux à l'octet | `numpy` sous 1.25 : refus ; racine recalculée sur une autre empreinte : refus | 1 |
| portier, forme | une fiche à douze champs va au portier | le témoin à champ de plus : au coffre sans autre cause | 5 |
| classes d'issue d'appel | une réponse à fiches : « fiches rendues » | le témoin « réponse vide motivée » et son artefact : chacun à sa classe, jamais l'arrêt n° 1 | 5, 9 |
| régime | le régime nommé, trois générations, aucun étage : permis | deux générations ; un étage ; un autre nom ; l'additif absent ou d'une autre empreinte ; une ligne d'accord d'un autre montant : refusés avant toute écriture | 6, 8 |
| rien ne fuit | une course simulée entière | un marqueur inerte planté dans chaque réponse simulée : absent, par recherche de programme, du dossier du run, de l'écran et de l'export | 8, 9 |
| clé n° 30 (A1, l. 79 à 82) | une seule case est tirée, parmi les seules cases servies dont la menace est le sabotage, à son rang dans l'ordre canonique | aucune case de sabotage servie (tirage d'essai planté) : rien n'est tiré, la sortie dit « aucune » ; une demande de second tirage : refusée | 1 |
| identifiant, clé n° 40 | les 120 mots sont distincts et passent la garde de motifs | un mot que la garde refuse (liste d'essai plantée) : le tirage s'arrête par un refus nommé, sans second tirage en silence | 1, 2 |
| case « autre, à nommer » (V9, l. 110) | une fiche dont le champ fermé est égal à cette chaîne, la supposition nommée écrite dans `idee` : passe | la supposition nommée écrite dans le champ fermé : « hors case » ; la part « hors case » de ces cases est rendue à part (M7) | 5, 7 |
| fiche hors contrat de longueur (D13) | une fiche dont chaque champ est à sa borne : suit son chemin | un champ d'un octet de trop, `idee` puis un autre : « au coffre », comptée, texte inchangé à l'octet dans le dossier de sortie ; mutation « couper à la borne » : l'essai doit échouer | 5 |
| gardes héritées (§ 2.13) | un proposeur qui rend des fiches : suivi normal | onze réponses vides motivées de suite d'un même proposeur : il n'est pas arrêté, aucun appel sauté, chacune classée et comptée à M6 ; mutation « lecture qui rend rien sans fiche » : le rôle s'arrête, et l'essai doit échouer | 5, 6 |
| envoi refusé sans coût (§ 2.3) | un appel permis : coût compté sur sa clé, au cumul de la génération et à M4 | un refus de l'arrêt n° 12, puis de l'arrêt n° 16 : le cumul de la génération, la garde de budget de la course et M4 sont inchangés au centime ; le journal dit « non envoyé » et le numéro de l'arrêt ; l'arrêt est levé au retour | 4, 6 |
| texte fixe de rôle retiré (D2) | à l'essai par les relais, le texte reçu par le faux fournisseur, transport retiré, a l'empreinte du journal, pour un proposeur, le portier et un juge | un texte de rôle remis par une configuration d'essai : l'égalité échoue, départ refusé | 4, 9 [lot 0] |
| course arrêtée (V9, l. 362) | trois générations complètes : mesures sous leur titre | arrêt provoqué pendant la génération 2 : mesures sur la seule génération 1, sous le titre « course arrêtée par [nom de l'arrêt] », M1 et M2 « sans objet » ; arrêt pendant la génération 3 : mesures sur les générations 1 et 2 | 7 |
| plafond du relais (V9, l. 235) | chaque relais déclaré au plafond égal à la part de sa clé : départ | un relais déclaré un centime au-dessus de la part, puis à la ligne de course : départ refusé | 8 |
| M4 sans cumul par clé (V9, l. 156) | M4 rendue par espèce et par rôle | recherche par programme, dans la sortie des mesures et l'export, des noms d'usage des clés et du champ de cumul par clé : absents ; présents au seul journal des arrêts n° 11 à n° 13 | 7 |
| relevé de fin par clé (A69, v4, § 7, point 7) | après une course simulée, cumul et reste par clé écrits au journal des arrêts n° 11 à n° 13 | le relevé de fin absent : le manifeste de fin rend un échec | 8 |
| aucune valeur de clé recopiée | une course simulée entière, variables de clé factices | un marqueur inerte planté comme valeur de chaque variable factice : absent, par recherche de programme, des manifestes, des journaux, de l'écran et de l'export | 8, 9 |
| réponses brutes conservées (V9, l. 396) | chaque appel de l'essai, pour chacun des quatre relais et pour chaque type d'adaptateur, laisse sa réponse brute dans le dossier de sortie, à l'empreinte de ce que le faux fournisseur a rendu | conservation rendue impossible (dossier en lecture seule) : l'appel s'arrête, rien n'est rendu sans copie | 8, 9 [lot 0, question 10] |
| colonne « matière première », éteinte (défaut) | la course simulée entière part et finit sans fichier de colonne ; le module n'est pas chargé | une demande d'allumage sans additif épinglé, sans ligne d'accord qui la nomme, ou par une variable d'environnement : refusée avant toute écriture | 10, facultatif |
| garde de la colonne, allumée à l'essai (§ 2.14) | une colonne d'essai aux lignes inertes : les 165 requêtes de proposeur sont **égales à l'octet** à celles de la course sans colonne ; aucune ne porte un nom ni un énoncé de la colonne ; les lignes arrivent aux juges à la fin | une ligne de la colonne plantée dans le registre servi, puis donnée à la place de la synthèse, puis sous une forme que la normalisation ramène : envoi refusé, « non envoyé », arrêt nommé ; un identifiant de la colonne planté au registre des tentatives : départ de la génération refusé ; une ligne d'entrée à champ de plus ou à marque de code : colonne non chargée ; mutation « garde retirée » : l'essai doit échouer | 10, facultatif |
| mutations | — | pour chaque garde, la garde retirée fait échouer son essai (manière de la v68, R68, § 4) | chaque lot |

### 6.3 L'essai à blanc de bout en bout, et la mesure des consignes

1. **En moteur simulé**, par le lanceur : sonde de refus, épreuve des témoins, trois générations, mesures, export. Constats, par comptes : trente-trois cases servies, 165 appels de proposeur, registre servi lu aux générations 2 et 3, les trois classes de fiche et les quatre classes d'appel toutes vues, bilan scellé, cumul sous le plafond.
2. **Par les relais, contre le faux fournisseur** : la même course ; égalité, appel par appel, entre l'empreinte du journal et l'empreinte du texte reçu, transport retiré ; coût compté sur la clé du rôle ; aucune requête reçue sur la clé hors course.
3. **Chaque arrêt provoqué une fois** dans une course simulée à part, et son nom relu au bilan.
4. **Le taux de faux refus de la garde de motifs** sur les registres servis et sur les requêtes du portier et des juges de l'essai (réserve de V9, l. 387) : rapporté, non corrigé.
5. **La mesure des consignes sans appel** (§ 2.12), dont la sortie est scellée et citée par l'additif.

L'essai est joué par la session de l'organisme et constaté par le vérificateur ; il ne lit aucune sortie d'aucun modèle.

## 7. Le découpage en mandats de code

Un lot est écrit par un développeur O et vérifié par un vérificateur S, sur un mandat tiré de cette conception. Fichiers neufs seulement ; paquet, manifeste et programme d'application à la manière de la v68 (R68, § 2). Chaque lot rend ses essais, ses mutations et son rapport.

| lot | contenu | dépend, en code, de | dépend, hors code, de | arrêts et gardes éprouvés |
|---|---|---|---|---|
| 0 | **relevé du code, sans écriture** : treize réponses fermées (ci-dessous) | — | le code de base sur `verse/vehicule-na-v1`, commit `61987a3a` (D10) | — |
| 1 | `tirage` : cases, clés 0, 1, 2, 3, 30 et 40, identifiants, réserve, C1, ligne de case et son contrôle | 0 | pour l'épreuve du mot refusé : une liste de motifs d'essai ; pour le jeu scellé : la liste des motifs scellée | n° 10 (premier temps) ; ligne de case ; tirage ; clés n° 30 et n° 40 |
| 2 | `garde_motifs` : programme, format de la liste, témoins positifs | 0 | **la liste des motifs**, rédaction du modèle F, en parallèle : le programme s'écrit et s'éprouve sur une liste d'essai ; l'épreuve par famille de l'arrêt n° 16 se joue sur la liste réelle, contre le gabarit, la synthèse et les témoins | n° 16 |
| 3 | `requete` et `journal` : partie servie, enveloppe sans ajout (D2), composition par rôle, journal d'ajout seul | 1, 2 | la forme de la ligne de case et de l'enveloppe, à l'additif (un brouillon suffit pour écrire) | partie servie ; requête journalisée ; n° 8 (mesure de la taille) |
| 4 | `routage` et adaptateur gardé : table des rôles et des clés, part par clé, tables des lignes à part, statuts de retour, envoi refusé sans coût, texte fixe de rôle retiré | 3 | les réponses 1 et 5 du lot 0 | n° 1, n° 12 (D11), n° 13, n° 16 (au point d'envoi) ; envoi refusé sans coût |
| 5 | `portier`, lecteur de fiches à deux syntaxes, contrat de fiche, `registre`, `verifier_registre_servi` | 1, 3 | **les consignes du portier et des juges (D3)**, en brouillon pour écrire ; les bornes en octets, en brouillon | n° 4, n° 5, n° 8, n° 9, n° 19 ; classes d'appel ; « autre, à nommer » ; hors contrat de longueur ; gardes héritées |
| 6 | `course`, lanceur de l'orchestrateur, `simulation`, configuration de course | 3, 4, 5 | les valeurs de l'additif en brouillon (bornes, gardes héritées rendues inertes) ; la réponse 12 du lot 0 | n° 5, n° 6, n° 7, n° 10, n° 14 ; régime ; gardes héritées |
| 7 | `mesures`, export hors quarantaine, deux outils de quarantaine, **chaînes de requête de la classe (i) de l'antériorité** (§ 9, point 13) | 5 ; **les formats du lot 6** | le format des attestations de relecture et des étiquettes d'antériorité, convenu avec la mère | n° 15, n° 17, n° 18 ; course arrêtée ; M4 sans cumul par clé |
| 8 | lanceur de course, **rendu comme différentiel contre L9** (ci-dessous) | 6 | **l'additif du véhicule scellé**, pour l'épinglage ; la pièce de relevés, par un exemplaire d'essai ; la réponse 13 du lot 0 | n° 11, n° 13 ; régime ; rien ne fuit ; plafond du relais ; relevé de fin ; aucune valeur de clé |
| 9 | `sonde_refus`, `epreuve_temoins`, essai à blanc de bout en bout, mesure des consignes sans appel | 7, 8 | **la liste des motifs scellée ; les consignes scellées (D3) ; les témoins scellés et leur table**, écrits par un agent de la mère, qui ne se scellent qu'après le tirage joué et scellé (§ 5.2) ; l'additif scellé | n° 2, n° 3, n° 4, n° 14, n° 27 ; § 6.3 ; réponses brutes conservées |

| 10, **facultatif** | `matiere_premiere` : colonne tenue à l'écart, sa garde, la lecture de fin, la table de comparaison (§ 2.14) ; voie (a) seule | 3, 4, 5, 7 | pour l'écrire : rien ; pour l'allumer : le mot de Lazar, un additif à la V9 contre-lu et scellé, le fichier de la colonne et ses empreintes donnés par la mère | garde de la colonne ; interrupteur éteint |

Le lot 10 est hors du chemin critique : aucun autre lot n'en dépend, la course part sans lui, et il ne s'écrit que si la mère le demande.

**Ordre.** 0 ; puis 1 et 2 ensemble ; puis 3 ; puis 4 et 5 ensemble ; puis 6 ; puis 7 et 8 ensemble ; puis 9. **Le lot 7 dépend des formats du lot 6** (dossiers des générations, ligne de génération, bilan de course) : il se joue après lui, sauf si ces formats sont figés au mandat du lot 6, sur le § 5 ; ils peuvent alors partir ensemble.

**Chemin critique : 0, 2, 3, 5, 6, 8, 9**, soit 1,25 + 2 + 2 + 3,75 + 4,75 + 5,5 + 4,75 = **24 heures** au plus bas (correction de CL, § 3.3 : la v1 passait par les lots 1 et 4, plus courts que les lots 2 et 5 joués en même temps). Hors code, trois pièces sont sur ce chemin si elles tardent : les consignes de D3 et les témoins scellés avant le lot 9, l'additif scellé avant l'épinglage du lot 8.

**Le lot 8 se rend comme un différentiel** (CL, § 3.1). Un fichier neuf de l'ordre de 3 000 lignes tiré de L9 ne se vérifie pas en une heure et demie. Le développeur rend : le fichier neuf ; le différentiel lisible contre L9 (`1b47c1cf…`) ; la liste de ses fonctions, en trois colonnes : gardées à l'octet, retirées, ajoutées ou changées, chacune avec sa raison. Le vérificateur S vérifie le différentiel et la liste, rejoue les essais, et ne relit en entier que ce qui est ajouté ou changé.

**Les treize questions du lot 0**, chacune avec le fichier et la ligne en réponse :

1. Ce que chaque type d'adaptateur ajoute au texte remis (texte fixe du rôle, réglages, outils), octet par octet, pour un proposeur, pour le portier, pour un juge.
2. Où les noms de fournisseurs sont fixés (L10, l. 641 à 647 ; lanceur `ideation_v8.py`) et ce qu'il faut pour déclarer deux adaptateurs du même type sur deux relais.
3. Comment la configuration v5 de la course v9 ne joue pas la passe « tableau », les étiquettes et les fusions, et si une génération peut ne déclarer que trois étapes (`course2_v53.py`, l. 70 à 104, les exige toutes).
4. Si rien d'autre que la boucle des cases (`course2_v68.py`, l. 186) ne suppose les mêmes cases à chaque génération.
5. Les statuts de retour d'un appel et ce qui distingue un refus de classifieur, un refus pour crédit, une erreur d'accès, une réponse coupée.
6. Ce que lisent `fiches_du_texte` et `preparer`, et ce que `champs_fiche` peut porter.
7. Ce qui existe déjà comme relais factices et faux fournisseur dans l'essai à blanc de L9.
8. Où le coût par espèce et par rôle est écrit pour une génération, et s'il l'est pour plusieurs (OC, l. 39 : « non vérifié »).
9. Si les relais tiennent un plafond cumulé sur trois générations et un compte d'appels suffisant.
10. Si les réponses brutes des adaptateurs du premier relais sont conservées comme celles des commandes externes.
11. Si les appels d'une étape sont lancés l'un après l'autre (le terme « appels en vol » de l'arrêt n° 12 vaut alors zéro, et reste écrit).
12. **Toutes les gardes héritées du noyau et de ses modules** (A2, A3, A11, A14, 11a, coupure au plafond, toute autre), chacune avec son fichier, sa ligne, la valeur de configuration qui la règle, et ce qu'elle fait à un rôle (§ 2.13).
13. **La structure de L9** : ses fonctions, celles que le § 1.2 retire, garde ou change ; le lieu où il recopie la sortie d'erreur de l'orchestrateur ; ce qui le distingue de L10 hors les interrupteurs. Le concepteur n'en a lu que l'empreinte.

Les questions 1 et 5 portent aussi, depuis la v2 : comment retirer le texte fixe de rôle sans modifier l'adaptateur (D2), et si le noyau reçoit sans faute un statut « non envoyé » au coût nul (§ 2.3).

Une réponse qui contredit cette conception revient au concepteur avant le lot concerné. Sont suspendus à ces réponses, et marqués « [lot 0] » dans le texte : la voie du refus sans coût et le retrait du texte fixe de rôle (§ 2.3), les trois étapes seules (§ 2.9), le sort des gardes héritées (§ 2.13), le lecteur de fiches (§ 5.4), la conservation des réponses brutes (§ 6.2), le découpage du lot 8.

## 8. Le calendrier

Estimation en heures de session, sans appel payant. Repères lus : la v68, huit fichiers et 2 096 lignes, écrite et essayée en trente minutes d'horloge, contre-lue en douze (R68, en-tête ; C68, en-tête) ; les textes de cette course ont demandé de trois à cinq allers et retours chacun le 20 novembre (A1, en-tête). Je compte large, parce que le lanceur est le plus gros fichier du dépôt (2 944 lignes pour L9) et que chaque lot porte ses mutations.

| lot | développeur O | vérificateur S | corrections et nouvelle vérification | somme |
|---|---|---|---|---|
| 0 | 0,75 | 0,5 | — | 1,25 |
| 1 | 0,75 | 0,5 | 0,5 | 1,75 |
| 2 | 1 | 0,5 | 0,5 | 2 |
| 3 | 1 | 0,5 | 0,5 | 2 |
| 4 | 1,25 | 0,75 | 0,5 | 2,5 |
| 5 | 2 | 1 | 0,75 | 3,75 |
| 6 | 2,5 | 1,25 | 1 | 4,75 |
| 7 | 1,5 | 0,75 | 0,5 | 2,75 |
| 8 | 3 | 1,5 | 1 | 5,5 |
| 9 | 2,5 | 1,25 | 1 | 4,75 |
| **somme** | **16,25** | **8,5** | **6,25** | **31** |

Autour du code, sur les places des modèles F et O et sur la mère :

| travail | heures |
|---|---|
| dix mandats de code, tirés de cette conception | 3 |
| consignes du portier et des juges (D3) : deux textes servis, passés à la garde de motifs, contre-lus, attestés « aucune recette », scellés | 3 à 4 ; hors du chemin critique s'ils partent tout de suite |
| liste des motifs, jouée sur le gabarit, la synthèse et les témoins | 1,5 |
| additif du véhicule, sa contre-lecture, ses corrections | 3 |
| contre-lecture du véhicule entier et confirmation de la répartition (règle R2) | 2,5 |
| jeu du tirage, de l'essai à blanc et de la mesure, constats | 1,5 |
| **somme** | **14,5 à 15,5** |

**Lecture** (corrigée sur CL, § 4). Les 31 heures de lots et les 15 heures autour sont **une borne basse, non une attente** : elles supposent un seul tour de correction par lot, aucune attente d'un scellement de la mère, aucune limite d'usage atteinte et aucune réponse du lot 0 qui contredise la conception. Les ajouts de cette v2 (gardes héritées, envoi refusé sans coût, épreuves de plus, lot 8 en différentiel) ne sont pas rechiffrés lot par lot : ils sont dans l'attente ci-dessous. Sur le chemin critique, 24 heures de lots, puis la contre-lecture du véhicule entier et le scellement de l'additif : 30 à 36 heures d'horloge est le cas sans aucun incident. **L'attente honnête est de 40 à 50 heures d'horloge**, soit un véhicule contre-lu le 23 novembre au plus tôt, et **un départ le 24 ou le 25**, après la pièce de relevés, les deux lignes à part et la lettre de départ. La durée de la course elle-même ne m'est pas connue.

**Pour l'échéance de GO-2026-11-20-67.** Le 22 novembre ne tient pas. Le 26 tiendrait avec une marge mince. **La mère demande à Lazar une échéance au 2026-11-27 : elle est demandée, non accordée** (message de 07:10Z) ; tant qu'elle ne l'est pas, la ligne échoit le 22.

Ce qui peut allonger : la place du modèle F, déjà interrompue par sa limite d'usage (OC, l. 44) ; une réponse du lot 0 qui contredit le § 2.3, le § 2.9 ou le § 2.13 ; les pièces hors code du § 7 (consignes, témoins, additif), si elles tardent ; D8 et D12, qui attendent Lazar, sans bloquer l'écriture d'aucun lot.

**La colonne « matière première » (§ 2.14)** n'entre pas dans ces chiffres : son lot est facultatif et hors du chemin critique, de l'ordre de 3,5 heures (2 de développeur, 1 de vérificateur, 0,5 de correction), plus un additif à la V9 et le mot de Lazar si elle est un jour allumée.

## 9. Ce que la lettre ne fixe pas

Chaque point est repris de l'inventaire, de son rapport ou du gabarit, ou trouvé ici. Depuis la v2, chacun dit son état : **tranché par la mère**, **décision de Lazar**, ou **proposition marquée, jamais tranchée**. Les trois premiers étaient neufs à la v1.

1. **Les consignes du portier et des juges** *(neuf à la v1)*. La V9 gèle ce que reçoit un proposeur ; elle ne dit rien du texte que reçoivent le portier et les juges, et l'inventaire ne le compte pas. Les consignes de la course v9 portent une autre question et d'autres classes. Sans elles, ni l'épreuve des témoins, ni la course ne peuvent partir ; ce sont des pièces fixes servies, donc sous l'arrêt n° 14 et la garde de motifs. **Tranché par la mère (D3)** : c'est un manque neuf ; elles sont écrites par le modèle F et contre-lues. Restent des propositions du concepteur : deux consignes courtes, contre la partie servie, aux seules étiquettes fermées du § 2.4, attestées « aucune recette » et scellées par la mère ; les items des juges réduits à un rang.
2. **La syntaxe de la sortie, et ce que l'enveloppe peut porter** *(neuf à la v1)*. La partie servie nomme les champs d'une fiche, non la syntaxe où les écrire (PS, l. 19). La V9 dit « rien d'autre de fixe » (l. 73) et confie l'enveloppe à l'additif (l. 77, 254). **Tranché par la mère (D2) : rien n'est ajouté à l'enveloppe.** Conséquences écrites : le texte fixe de rôle de l'adaptateur est retiré (§ 2.3) ; le lecteur de fiches accepte deux syntaxes (§ 5.4) ; la part « réponse illisible » de l'essai et de la sonde est regardée avant le départ.
3. **Le « nom » d'une ligne du registre servi** *(neuf à la v1)*. La V9 sert, pour une tentative passée, « son nom » et « son énoncé ramené à une ligne » (l. 63). La fiche de la question v5 n'a ni champ de nom, ni champ d'énoncé (PS, l. 19) ; son champ `filiation` cite « l'identifiant d'une fiche du registre servi ». **Tranché par la mère (D5)** : le nom est l'identifiant de la fiche ; l'énoncé est le champ `idee` sur une ligne. **Tranché par la mère (D13, 07:10Z)**, après que la contre-lecture a montré que la v1 débordait de D5 (CL, § 6.2) : une fiche hors contrat de longueur est traitée comme illisible, donc « au coffre », comptée, jamais réparée. Deux lectures sont de moi et restent des **propositions à la mère** : cette fiche est une fiche rendue, au dénominateur de M3 et de la garde du coffre ; les lignes de compte du registre servi ne sont écrites que pour un compte non nul, et sont permutées avec les autres.
4. **Où se porte la clé de tirage de l'identifiant.** La clé n° 40 est décidée (D4). Le lieu : au « complément contre-lu » (V9, l. 254) ; il n'y a pas de lot 2 (CV, l. 68). *Proposition* : à l'additif du véhicule, que la mère dit valoir complément pour cette seule valeur.
5. **L'ordre du portier, et ce qu'on appelle « le portier ».** **Tranché par la mère (D6)** : forme, modèle, hors case ; une réponse illisible du modèle portier va au coffre. Elle se compte à part, parce qu'elle pèse sur la garde du coffre ; le modèle n'est pas appelé pour une fiche que le programme de forme a déjà envoyée au coffre.
6. **L'arrêt n° 1 en course.** « Le tour s'arrête » (V9, l. 372) ne dit pas si c'est l'appel, le rôle ou la course. **Décision de Lazar (D8), en attente.** *Proposition du concepteur, que le code porte d'ici son mot comme une valeur de configuration* : l'appel ; il est consigné sous le nom de l'arrêt, non relancé, sans reformulation ; la course continue et le rapport le dit par espèce. À la sonde, il arrête le départ.
7. **La lecture « accepte » ou « refuse » à la sonde.** La lettre la confie à « la même garde » sans la décrire ; la table des lignes à part ne prévoit aucun appel de portier à la sonde (CV, l. 127 à 130). **Tranché par la mère (D7)** : par programme seul. Au moins une fiche complète au contrat, dans l'une des deux syntaxes : « accepte ». Statut de refus d'un classifieur : arrêt n° 1. Tout le reste, texte sans fiche compris : « réponse que la garde ne sait pas lire », arrêt n° 27. Restent des propositions : la mère demande alors une étiquette à la session à part sans lire la réponse ; la borne de sortie de la sonde est mise assez haut pour une fiche entière.
8. **La case que portent les témoins** (gabarit, § 6, point 9). *Proposition* : la première case de la réserve (§ 5.2).
9. **Le devis final** (inventaire, n° 9). *Proposition* : la mesure des consignes sans appel et la pièce de relevés en tiennent lieu, si la mère le dit ; le véhicule rend les chiffres, il n'écrit pas de devis.
10. **Le pire d'un appel d'aiguilleur et de juge, et où il s'écrit** (rapport de l'inventaire, § 3, point 4). *Proposition* : à l'additif du véhicule, sur la mesure ; candidats du § 2.3.
11. **Les mesures « lues une fois »** (V9, l. 315) — **nœud de Lazar (D12) ; d'ici son mot, la lettre de la V9 est gardée.** La v1 proposait deux lectures parmi les « autres points » : c'était un écart à un préenregistrement scellé, non porté comme décision (CL, § 6.3). **Ce que le véhicule fait** : une seule lecture de toutes les mesures, refusée tant que l'attestation de relecture et les étiquettes d'antériorité ne sont pas scellées, refusée une seconde fois (§ 2.8). **L'option, notée à part, soumise à Lazar, que le véhicule ne porte pas** :
    - *Décision.* Les mesures sont-elles lues en deux fois, M5 plus tard que les autres ?
    - *Enjeu.* M5 dépend de la lecture d'antériorité, qui suit de loin la relecture « aucune recette ». À la lettre, aucune mesure n'est lue avant la fin de cette lecture ; M1 à M4, M6, M7, C1 et I1 attendent donc M5.
    - *Options.* (a) Garder la lettre : une lecture, après la lecture d'antériorité ; aucun écart ; les mesures de l'héritage et du coût attendent. (b) Deux lectures scellées, chacune unique : M1 à M4, M6, M7, C1 et I1 après la relecture, M5 après l'antériorité ; les premières sont connues plus tôt ; c'est un écart à un texte scellé, par additif contre-lu, et la première lecture est faite avant que les lecteurs d'antériorité aient fini.
    - *Recommandation.* (a), confiance 0,6 : rien dans la course ne dépend de connaître M1 plus tôt, et (b) ouvre un chemin par où un chiffre lu pourrait toucher une lecture en cours. Je passerais à (b) si la lecture d'antériorité devait durer des semaines.
    - *Défaut.* Aucun : c'est un écart à un préenregistrement scellé. Sans mot, (a) vaut, puisque c'est la lettre.
12. **L'ordre entre les témoins et la garde de motifs** (inventaire, § 3). *Proposition* : brouillons des deux, garde jouée sur les témoins en moteur simulé au lot 2, puis scellement ensemble.
13. **Les cinq programmes du § 4.10 de l'inventaire.** *Propositions* : les chaînes de requête de la classe (i) de l'antériorité, dans le véhicule, au lot 7, parce qu'elles se calculent « à partir de la case » et du tirage ; le programme de la condition (c) de l'additif 1 et celui d'ouverture de la branche, hors du véhicule, dus après le départ, sauf les deux contrôles du § 2.6 ; le programme de la pièce de relevés, hors du véhicule, à la mère.
14. **La mémoire qui évite les redites** (OC, l. 27), que la V9 ne reprend pas. *Proposition* : non jouée. Elle écarterait ou marquerait des fiches hors des trois classes que la V9 gèle, et rien ne dit qu'elle doive.
15. **La branche de quarantaine avant les deux lignes à part** (rapport de l'inventaire, § 3, point 8). Le véhicule n'en dépend pas : il écrit dans un dossier de sortie hors de l'arbre de travail. *Proposition* : le dossier suffit pour les lignes à part ; la branche est due avant la première lecture.
16. **Qui lance le véhicule.** La session de l'organisme le lance et ne doit rien lire d'une fiche. *Proposition* : la règle commune du § 2 et l'épreuve « rien ne fuit » la tiennent ; la mère dit si cela suffit, ou si le lancement revient à la session à part.
17. **Un artefact de l'arrêt n° 12 a perdu son objet.** La V9 éprouve « un appel du juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 » (l. 383), et l'additif 1 garde ce cas (A1, l. 169). Depuis l'additif au complément, ces deux rôles sont sur la même clé (AC, l. 56) : l'artefact ne peut plus être refusé. L'artefact que la v1 proposait à sa place (« le juge de l'espèce 3 sur la clé de l'aiguilleur ») n'éprouvait qu'« un rôle sur une autre clé », et perdait l'objet de l'arrêt, que la table soit lue **par rôle, non par espèce** (V9, l. 402 ; CL, § 5). **Tranché par la mère (D11, 07:10Z) : la proposition du contre-lecteur est acceptée telle quelle** : un cas sain neuf (le juge et le proposeur de l'espèce 3 sur Minuit, comptés sur Minuit) ; un artefact en course (l'aiguilleur présenté sur Minuit, refusé) ; un artefact sur une table plantée que la course ne charge jamais, où le juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 est refusé ; la mutation « routeur par espèce », qui doit faire échouer l'essai. L'artefact de la v1 reste en plus, avec ceux du complément et de son additif (CV, l. 166 ; AC, l. 175). Lettre de l'épreuve : § 6.1, ligne du n° 12.
18. **La colonne « matière première »** *(neuf à la v2)*. Possibilité désactivée par défaut, dont la course ne dépend pas ; son allumage est une décision de Lazar et un écart à la V9 (§ 2.14).
19. **Le sort des gardes héritées du noyau** *(neuf à la v2)*. Le sort de chacune est proposé au § 2.13 ; l'effet d'A2 et d'A11 en course, et toute garde que le lot 0 trouverait en plus, sont des propositions à la mère.

## 10. Réserves du concepteur

1. **J'ai lu le code en partie.** En entier : `course2_v68.py`, `noyau_v56.py`, `aiguilleur_v53.py`. En partie : `course2_v53.py` (l. 1 à 330), L10 (l. 1 à 140, 496 à 565, 2889 à 3160, et la liste de ses fonctions), E9 (l. 1 à 120). Non lus : les adaptateurs, les relais, `ideation_v8.py`, `budget_v56.py`, les fichiers de fiches et de juges, L9 hors son empreinte et le compte de ses fonctions. Le lot 0 existe pour cela.
2. **Je n'ai lu ni la question, ni le corps de la synthèse servie, ni aucune sortie de modèle.** La partie servie est lue en entier.
3. **L'additif de la v69 est lu dans sa v1** (`aef8ff2f…`), son § 7 seulement ; la version scellée est la v4 (`cb352811…`, registre, R-4131), que je n'ai pas ouverte : ce qu'elle ajoute au point 7 de son § 7 est repris de la contre-lecture (CL, § 1.5), et le vérificateur du lot 8 compare la table du § 2.11 à la v4.
4. **Les heures du § 8 sont une estimation**, sans mesure propre : elles s'appuient sur deux durées lues et sur le nombre de pièces.
5. **Les valeurs chiffrées que je propose** (forme du mot, forme de la ligne de case, séparateurs) sont des valeurs du concepteur ; aucune n'a valeur de règle avant l'additif scellé. Le numéro de clé 40 est décidé par la mère (D4).
6. Les parts, les seuils et la table des rôles sont recopiés de CV et d'AC ; en cas d'écart, ces pièces font foi.
7. **Les décisions de la mère de 06:58Z et de 07:10Z, et l'ajout de 07:14Z corrigé à 07:15Z, sont portés d'après les messages de reprise** ; je n'ai relu ni le registre des décisions ni celui des accords depuis le commit `ebb7492a…`, et je n'ai lu ni GO-2026-11-21-17, ni GO-2026-11-21-19, ni N-072.
8. **La colonne « matière première » est conçue sur la forme seule**, sans rien savoir de la matière ; je n'ai ouvert aucune branche de quarantaine.
9. **De `suivi_roles_v54.py`, lu pour la v2**, les lignes 1 à 95 ; les gardes héritées que je n'ai pas vues sont l'objet de la question 12 du lot 0.

— concepteur du véhicule, modèle F
