# Conception du véhicule — course « nouvelles attaques », à cinq espèces, trois générations — v1

Pièce de travail (classe C), non contre-lue, non scellée. Elle conçoit ; elle ne tranche rien de ce que la lettre laisse ouvert. Processeur seul : aucun appel, aucune dépense, aucun code écrit pour être lancé, aucun lancement, aucune écriture dans un dépôt.

- Auteur : concepteur du véhicule, modèle F. Je n'ai écrit ni la v9, ni l'inventaire, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 06:45:57Z, après la lecture des pièces, avant l'écriture.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-conception-vehicule-course-nouvelles-attaques-v1.md` (`d2130f6b0aab5d4d32f01f51acd71b23cc3d1623769b24cd4d6fb06317c19af2`, égale à son compagnon), lu en entier.
- Point de départ : l'inventaire de l'allumage (`0737906f9901de39ddd9b1585679b5b44e6bac67e7051a10374d3e0e496c06e0`), son § 4, et le gabarit des témoins (`a84de0bf3168d93dda6928e2e165c14ecb8b091e976a629ace828813c24c89c0`).
- Lecture : `origin/main` du dépôt de l'organisme au commit `ebb7492a8a2923a6a790ee0f8d29ee320b530f3d` ; le code existant sur le disque de la branche `lot/compte-organisme-v1` (commit `9555d8b696d3aae9d17a9c41399d0ab24704c530`) et dans le dépôt de l'orchestrateur (commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`). Pièces et empreintes : rapport joint, § 1.
- Ce que ce texte ne contient pas : aucune méthode d'attaque, aucun procédé, aucune recette, aucun nom ni énoncé de mode, aucune case nommée, aucun identifiant de modèle, aucune valeur ni nom de variable de clé, aucun motif de la garde de motifs.

Sigles de renvoi (numéros de ligne) : V9, A1, CV, AC, DV, OC comme à l'inventaire ; PS, la partie servie (`4cd360ba…`) ; R68, le rapport du développeur de la v68 (`ad42b722…`) ; C68, sa contre-lecture (`d2cfeac1…`) ; A69, l'additif des interrupteurs de la v69, v1 (`aef8ff2f…`) ; L9 et L10, les lanceurs de course v9 et v10 (`1b47c1cf…`, `f4196ec5…`) ; E9, l'épreuve des témoins v9 (`5be161fa…`).

## 0. En bref

1. **Base retenue.** Orchestrateur : le commit `a41b7b50…` plus le paquet v68 (huit fichiers neufs, manifeste `4ed9fd8e…`, contre-lu « Conforme »). Lanceur : le lanceur de course v9 (`1b47c1cf…`), le seul qui ait porté une course réelle de cette composition, avec deux lectures reprises du lanceur v10 (`f4196ec5…`). Épreuve des témoins : celle de la course v9 (`5be161fa…`). Le lanceur 11 n'a pas de code : il n'existe que par la liste de ce qu'il doit épingler (A69, § 7), que le lanceur neuf suit.
2. **Plus petite différence.** Le véhicule ne récrit ni le noyau des appels, ni le budget d'une génération, ni la garde de budget de la course, ni les relais, ni la conservation des réponses, ni l'inventaire de fin. Il ajoute des fichiers neufs, jamais une modification (règle R12).
3. **Ce qui est neuf, et lourd** : l'assemblage exact de la requête, la garde de motifs et le journal posés dans un adaptateur gardé, au dernier point avant l'envoi ; le routage par rôle sur quatre relais actifs ; le portier à trois classes et quatre classes d'issue d'appel ; le registre servi ; des cases neuves à chaque génération ; les mesures.
4. **Dix lots** : un lot 0 de relevé du code, sans écriture, puis neuf lots de code. Chemin critique : 0, 1, 3, 4, 6, 8, 9.
5. **Calendrier, dit sans forcer** : de l'ordre de 31 heures de sessions de développeur et de vérificateur, et de 14 heures de rédaction, de contre-lecture et de scellement autour. En deux files parallèles et sans interruption : 30 à 36 heures d'horloge avant les deux lignes à part. **L'échéance du 2026-11-22 de GO-2026-11-20-67 ne tient pas avec une marge honnête.**
6. **Trois trous que l'inventaire ne nomme pas** (§ 9, points 1 à 3) : les consignes du portier et des juges pour cette question ne sont écrites nulle part ; la partie servie ne dit pas la syntaxe de la sortie, et rien d'autre de fixe ne doit partir ; le registre servi veut un « nom » que la fiche ne porte pas.

## 1. Le choix de base

### 1.1 Ce qui existe, lu sur pièces

| pièce | où | empreinte | état |
|---|---|---|---|
| orchestrateur, commit de base | dépôt de l'orchestrateur, lu à `/home/user/lciric/ideation-organism` (le chemin `/home/user/ideation-organism` que cite R68 est absent de cette machine ; L10, l. 530, nomme les deux) | commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` | a porté la course v9 en réel, une génération, par `demonstrations/ideation_v8.py` |
| paquet v68 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/paquet/…`, sur le disque de la branche | manifeste `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` | contre-lu « Conforme » (C68) ; moteur simulé seulement ; refuse le moteur réel par construction |
| lanceur de course v9 (L9) | `scripts/lancer_course_auto_conception_v9.py`, disque de la branche | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` | contre-lu « Scellable. » ; a lancé la course v9 |
| lanceur de course v10 (L10) | `scripts/lancer_course_auto_conception_v10.py`, disque de la branche | `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` | éteint, égal à L9 ; allumé, refusé en réel ; lit les coûts de plusieurs générations à blanc |
| épreuve des témoins v9 (E9) | `scripts/epreuve_temoins_auto_conception_v9.py`, disque de la branche | `5be161fa35e339d171399a3ba2a2c927cd517fba42c745306fd867a4b3e3c69b` | a joué l'épreuve réelle de la course v9 |
| lanceur de course 11 | aucun fichier | — | réservé au palier 1 de l'héritage ; décrit par A69, § 7 ; non écrit |
| orchestrateur v69, v70 | aucun code | — | additif et cadre scellés (registre, R-4131) ; noms réservés |

**Ces pièces de code ne sont pas sur `origin/main`** au commit lu (`git show` répond « exists on disk, but not in 'origin/main' » pour le rapport de la v68 et pour les deux scripts de la course v9). Le mandat veut « chemin et empreinte sur `main` » : je donne le chemin et l'empreinte sur le disque de la branche. Le versement sur `main` avant les mandats de code est une décision de la mère (rapport, D10).

### 1.2 Ce que le véhicule garde, retire, ajoute

**De l'orchestrateur (base et v68), gardé sans y toucher :**

| ce qui est gardé | fichier | pourquoi |
|---|---|---|
| l'appel d'un rôle, sa consommation notée dans tous les cas, son plafond borné au reste de l'étape | `pole/noyau_v56.py`, `appel` (l. 147 à 188) | c'est là que passe chaque envoi ; l'adaptateur gardé du § 2.3 s'y glisse sans le changer |
| le budget d'une génération et la règle des seuils : plafond dur de la proposition, aiguillage et juges lancés sous leur seuil | `pole/budget_v56.py`, configuration v5 de la course v9 (150 ; 140, 135, 120 : L10, l. 46 à 49) | ce sont exactement les valeurs des arrêts n° 6 et n° 7 à cinq espèces (A1, l. 166, 167) |
| la garde de budget de la course : réservation du plafond d'une génération avant de la jouer, arrêt au plafond de la course | `pole/budget_course_v68.py` | arrêt n° 6 ; V9, l. 377 ; R68, § 3, point 3 |
| le montant requis, N fois le plafond d'une génération, sans étage | `pole/configuration_v68.py` | 3 × 150 = 450 USD ; régime « éteint, sans étage » de R68, § 5 |
| la boucle des générations, la ligne de chaque génération, le bilan de course scellé | `pole/course2_v68.py`, `executer_course_v68` | point de départ de la boucle du § 2.9 |
| la lecture en objet de ce qui est servi à la génération suivante, la garde ligne par ligne, le titre de section passé en argument, la section omise quand il n'y a rien, `heritage_lu` | `pole/course2_v68.py`, `rendre_heritage_v68`, `GenerationV68` | forme reprise pour le registre servi (§ 2.6) |
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
- Le lanceur neuf « suit le lanceur 11 » (V9, l. 402) par son rang et par ce qu'il épingle : je reprends la liste d'A69, § 7, point par point, au § 2.11. Il ne peut pas en suivre le code : il n'y en a pas.
- Ce que je n'ai pas pu établir par lecture est rassemblé au lot 0 (§ 7) : onze questions fermées posées au code avant d'écrire.

### 1.4 Le nom

Les numéros 69, 70 et 71 sont déjà portés, hors de cette course, par une autre lignée du même orchestrateur (registre, l. 2507, 2558, 2579). Un numéro de plus risque une seconde collision. **Proposition, non tranchée** : une série propre, la version dans le nom (règle R12) : suffixe `_na_v1` pour les fichiers de l'orchestrateur, `lancer_course_nouvelles_attaques_v1.py` pour le lanceur, « véhicule NA-1 » dans les textes. Le régime porte un seul nom, écrit en toutes lettres dans le code et dans la ligne d'accord : `trois_generations_sans_etage_lecture_du_registre_des_tentatives`. L'autre option, un numéro neuf vérifié libre, est au rapport (D1).

## 2. Les modules

Un module par fonction du cahier des charges. Pour chacun : la lettre qui l'impose, ce qu'il fait, ce qu'il lit et rend. Les épreuves sont au § 6, les interfaces au § 5. « Dossier de sortie » désigne le dossier de la course hors de l'arbre de travail, qui est la quarantaine ; « dossier du run », le dossier des manifestes, qui en est dehors.

**Règle commune à tous les modules** (V9, l. 82, 83, 387, 388) : hors du dossier de sortie ne s'écrivent que des identifiants, des empreintes, des tailles et des comptes. Aucun message d'erreur, aucune ligne d'écran, aucun manifeste du dossier du run ne recopie un octet d'une réponse de modèle, d'une fiche ou d'une ligne du registre servi. Le lanceur L9 recopie aujourd'hui la fin de la sortie d'erreur de l'orchestrateur dans son refus (L10, l. 2998) : ce lieu est à fermer (lot 8).

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

Deux précisions.

- **Ce que la garde lit.** La requête assemblée est le texte remis à l'adaptateur. Ce que l'adaptateur et le relais ajoutent pour le transport (nom du modèle demandé, réglages, texte fixe du rôle s'il y en a un) n'est pas vu par ce pas : c'est le lot 0 qui relève, octet par octet, ce que chaque type d'adaptateur ajoute, et l'additif le déclare comme « enveloppe » ou le fait retirer (§ 9, point 2). L'essai à blanc ferme la boucle : le faux fournisseur garde ce qu'il reçoit, et un programme vérifie que le texte reçu, transport retiré, a l'empreinte du journal (§ 6.3).
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
| classe d'issue de fiche, ensuite | « passée », « au coffre », « hors case », exclusives. Ordre proposé (§ 9, point 5) : (i) programme de forme : un champ hors des douze du contrat, « au coffre » ; (ii) portier, étiquette fermée « niveau de l'idée » ou « concret » : « concret », « au coffre » ; (iii) programme : un champ fermé qui diffère à l'octet de la ligne de case, « hors case » ; (iv) sinon « passée », avec passeport |
| garde « hors case » | arrêt n° 4 : comparaison par programme, à l'octet, aux trois chaînes de la ligne de case ; la fiche est refusée et comptée, son texte n'est servi à personne. À la case « autre, à nommer », la valeur attendue du champ fermé est cette chaîne même (V9, l. 110) |
| garde du coffre | arrêt n° 5 : après chaque génération, part « au coffre » parmi les fiches rendues, strictement au-dessus d'un quart : la génération suivante ne part pas ; à la troisième, consigné |
| ne fait pas | juger la nouveauté ; lire la relecture ; servir quoi que ce soit du coffre |
| pièce qui manque | **la consigne du portier pour cette question** (ses deux étiquettes de fiche, ses trois étiquettes d'appel) n'est écrite nulle part (§ 9, point 1) |

### 2.5 Juges joués pour information — module existant, câblage neuf

| | |
|---|---|
| lettre | V9, l. 64, 159 ; arrêt n° 7 |
| fait | les deux juges, des espèces 3 et 1, lisent chaque fiche « passée », une par appel, sous identifiant anonyme, comme à la course v9 ; leurs verdicts vont au coffre de la génération, leur classement est écrit dans le dossier de sortie |
| ne fait pas | entrer dans le registre servi, dans un tirage, dans une mesure autre que I1, dans un passage |
| garde | l'étape n'est lancée que sous le seuil de 120 USD (budget d'une génération, inchangé) |
| pièce qui manque | **la consigne des juges et leurs items pour cette question** (§ 9, point 1) |

### 2.6 Registre des tentatives, registre servi, quarantaine — modules `registre`, `verifier_registre_servi`, `quarantaine`

| | |
|---|---|
| lettre | V9, l. 62, 63 ; arrêts n° 8, 9, 17, 18, 19 ; garde-fous 2 et 3, l. 119, 120 ; clés 12 et 13, l. 308 |
| registre des tentatives | dans le dossier de sortie, ajout seul : pour chaque fiche rendue, son identifiant, sa génération, l'identifiant de sa case, sa classe d'issue ; pour une fiche « passée », ses trois champs fermés, son nom et son énoncé d'une ligne (§ 9, point 3) ; rien d'un juge, rien du coût, rien de l'espèce |
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
| garde | arrêt n° 15 : refus de calculer tant que le bilan de course ne dit pas trois générations complètes, ou un arrêt nommé, et tant que l'attestation de relecture manque ; une seule lecture, consignée ; une course arrêtée rend ses mesures sous le titre de l'arrêt, M1 et M2 « sans objet » si la seule génération 1 est complète |
| point ouvert | M5 ne peut être lue qu'après la lecture d'antériorité, plus tard que les autres (§ 9, point 11) |

### 2.9 Génération et course du régime — modules `course` et lanceur de l'orchestrateur

| | |
|---|---|
| lettre | V9, l. 60, 61, 402, 419 ; OC, l. 33 ; arrêts n° 5, 6, 7, 10, 14 |
| génération | une classe neuve qui hérite de `GenerationV68` : ses cases sont celles de sa génération, lues au tirage scellé ; sa proposition assemble la requête par le module `requete`, sans la section « Case » de la v54 ; ses étapes sont « proposition », « aiguillage », « juges », et aucune autre ; son portier est celui du § 2.4 |
| course | une fonction neuve sur le modèle d'`executer_course_v68` : trois générations exactement ; au départ de chacune, garde d'empreintes (arrêt n° 14), garde de disjonction (arrêt n° 10), registre servi fabriqué et vérifié (arrêts n° 8, 9, 19), réservation de 150 USD sur le plafond de 450 (arrêt n° 6) ; après chacune, garde du coffre (arrêt n° 5), ligne de la génération, sceaux |
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
| lit | l'issue de chaque témoin contre la table scellée des issues attendues, par programme | « accepte » ou « refuse », par la règle du § 9, point 7 |
| arrêts | n° 3 : un témoin manqué, aucune course ; n° 4 : l'épreuve de la garde « hors case » | n° 1 : refus d'un classifieur ; n° 2 : l'espèce refuse ; n° 27 : refus pour crédit, erreur d'accès, réponse illisible : non relancée, départ refusé |
| routage, hors de la course | portier et juge de l'espèce 3 sur Minuit ; juge de l'espèce 1 sur le deuxième relais | espèces 3 et 4 sur Minuit ; espèces 1 et 5 sur le deuxième relais ; espèce 2 sur le troisième, après le relevé de son statut |
| plafond | 5 USD, ligne à part | 1 USD, ligne à part |
| rend | un rapport en deux parts : dans le dossier de sortie, les réponses brutes ; dehors, par témoin, l'issue attendue, l'issue lue, « tenu » ou « manqué », le coût | par espèce : l'issue, le coût, l'empreinte et la taille de la réponse ; la réponse brute reste dans le dossier de sortie |

### 2.11 Lanceur de course — script `lancer_course_nouvelles_attaques_v1.py`

Il suit, point par point, ce qu'A69, § 7, demande au lanceur 11, transposé à ce régime.

| A69, § 7 | ce que le lanceur neuf épingle ou vérifie |
|---|---|
| 1 | les empreintes des fichiers de base de l'orchestrateur (liste de L10, l. 534 à 561), les huit du paquet v68, et chaque fichier neuf du véhicule |
| 2 | sans objet : aucun étage, aucune chaîne du tour fermé |
| 3 | l'additif du véhicule, scellé, à son chemin et à son empreinte |
| 4 | la V9, A1, CV, AC, le devis v11, la configuration, le tirage scellé, la partie servie, la synthèse servie, les consignes du portier et des juges, les témoins et leur table, la liste des motifs et son programme, la pièce de relevés du jour |
| 5 | le seul appel permis : le lanceur de l'orchestrateur du § 2.9, régime nommé, trois générations ; tout autre jeu d'options refusé |
| 6 | le montant requis, recoupé sans écriture avec l'orchestrateur : 450 USD ; la ligne d'accord de la course à ce montant exact ; les lignes à part à 5 et à 1 USD |
| 7 | les bornes des relais comptées pour trois générations ; le plafond de chaque relais égal à la part de sa clé, **non à la ligne de course** (V9, l. 235) ; arrêt n° 11 au départ |
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
| consignes du portier et des juges | modèle F (proposé) | un autre modèle | la mère, après son attestation « aucune recette » | oui, au portier et aux juges |
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

**Proposition, à écrire à l'additif** (rapport, D4) :

- un mot de trois syllabes, chaque syllabe faite d'une consonne prise dans douze et d'une voyelle prise dans cinq, les consonnes choisies hors des lettres qui servent à écrire l'hexadécimal ; six lettres, aucun chiffre : jamais huit caractères hexadécimaux de suite ;
- 216 000 mots possibles pour 120 cases : le mot ne dit rien du compte ;
- les 120 mots sont tirés une fois, sans remise, pour **toutes** les cases, dans l'ordre canonique, par une **clé de tirage neuve** (je propose le numéro 40, libre) : `rng.choice(216000, size=120, replace=False)` sur `SeedSequence(entropy=racine, spawn_key=(40,))` ; un mot ne dépend donc ni de la génération, ni du fait que la case soit servie, tenue à l'écart ou en réserve ;
- la lettre le permet : « si sa construction demande un tirage, c'est une clé de tirage neuve, qui ne change aucun tirage écrit » (V9, l. 75, 254) ; elle la veut « portée au complément contre-lu », et il n'y a pas de lot 2 : où elle se porte est au § 9, point 4 ;
- la table des 120 mots sort du tirage, scellée avec lui ; elle n'est jamais servie ; chaque mot passe la garde de motifs avant le scellement ; un mot qui la ferait refuser arrête le tirage par un refus nommé, sans second tirage en silence.

**La ligne de case.** Proposition : `case : <identifiant> ; <valeur 1> ; <valeur 2> ; <valeur 3>`, les trois valeurs à l'octet de la légende, le séparateur « ; » encadré d'une espace de chaque côté (aucune valeur de la légende ne le porte ; deux portent une virgule, deux des parenthèses). Borne : 256 octets, gardée ; la plus longue ligne possible est à mesurer par le programme, je l'estime sous 200 octets.

**Les témoins.** Le gabarit attend de l'additif l'identifiant neutre et la ligne de case que porte un témoin (gabarit, l. 61, 98). Proposition (§ 9, point 8) : tous les témoins portent **la première case de la réserve**, celle de la sonde de refus : elle n'est ni servie par la course, ni de la famille tenue à l'écart, elle n'est déjà plus fraîche, et aucune case de plus n'est consommée. Leur champ `case` prend le mot de cette case dans la table scellée ; leur ligne de case est construite par le même programme que les trente-trois autres. Les témoins ne peuvent donc être scellés qu'après le tirage.

### 5.3 L'enveloppe de la requête

Valeur ouverte, à l'additif (V9, l. 254). Proposition :

| rôle | suite d'octets |
|---|---|
| proposeur, génération 1 | partie servie remplie ; une ligne vide ; synthèse servie à l'octet |
| proposeur, générations 2 et 3 | la même ; une ligne vide ; le titre de la section du registre, sur une ligne ; le registre servi. Si le registre est vide : section omise, la requête est celle d'une génération 1, et la ligne de la génération le dit (défaut de la v68, R68, § 3, point 5) |
| sonde de refus | partie servie remplie, seule |
| portier, juge | leur consigne fixe ; une ligne vide ; la fiche, dans la forme servie par l'orchestrateur |

Le titre de la section, la règle du registre vide et la question de la syntaxe de sortie sont au § 9, points 2 et 3.

### 5.4 Le contrat de sortie d'une fiche

Les douze champs de PS, l. 19, dans cet ordre, tous des chaînes. Une fiche « au contrat » : les douze présents, chaque champ libre sous sa borne en octets, `idee` comprise (bornes à l'additif, sur la mesure). Un champ de plus ne sort pas la fiche du contrat : il l'envoie au coffre. La syntaxe lue (un objet par fiche, ou des lignes « champ : valeur ») dépend du § 9, point 2.

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
| n° 12, part épuisée, étendu | un appel qui tient sous la part, sur sa clé : lancé et compté sur elle, pour chacune des quatre clés | un appel qui dépasserait la part d'un centime : refusé, arrêt nommé ; le juge de l'espèce 3 présenté sur la clé de l'aiguilleur ; le proposeur de l'espèce 2 présenté sur le deuxième relais ; **un envoi adressé à Rigaud** : refusés. Les deux lignes à part, par leur table : non refusées | 4 |
| n° 13, refus pour crédit | réponse normale | refus pour crédit simulé : arrêt nommé, qui dit la clé ; aucune bascule | 4, 8 |
| n° 14, empreinte différente | toutes égales : départ | un octet changé dans la partie servie, puis dans la liste des motifs, puis dans une consigne, puis dans le tirage : refus qui nomme la pièce ; rejoué au départ de la génération 2, de la sonde et de l'épreuve | 6, 9 |
| n° 15, mesure lue trop tôt | bilan à trois générations et attestation présente : calcul | bilan à deux générations sans arrêt nommé ; attestation absente ; seconde lecture : refus | 7 |
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

| lot | contenu | dépend de | arrêts et gardes éprouvés |
|---|---|---|---|
| 0 | **relevé du code, sans écriture** : onze réponses fermées (ci-dessous) | — | — |
| 1 | `tirage` : cases, clés 0, 1, 2, 3, 30, identifiants, réserve, C1, ligne de case et son contrôle | 0 | n° 10 (premier temps) ; ligne de case ; tirage |
| 2 | `garde_motifs` : programme, format de la liste, témoins positifs ; la liste elle-même est une rédaction du modèle F, en parallèle | 0 | n° 16 |
| 3 | `requete` et `journal` : partie servie, enveloppe, composition par rôle, journal d'ajout seul | 1, 2 | partie servie ; requête journalisée ; n° 8 (mesure de la taille) |
| 4 | `routage` et adaptateur gardé : table des rôles et des clés, part par clé, tables des lignes à part, statuts de retour | 3 | n° 1, n° 12, n° 13, n° 16 (au point d'envoi) |
| 5 | `portier`, contrat de fiche, `registre`, `verifier_registre_servi` | 1, 3 | n° 4, n° 5, n° 8, n° 9, n° 19 ; classes d'appel |
| 6 | `course`, lanceur de l'orchestrateur, `simulation`, configuration de course | 3, 4, 5 | n° 5, n° 6, n° 7, n° 10, n° 14 ; régime |
| 7 | `mesures`, export hors quarantaine, deux outils de quarantaine | 5 ; les formats du lot 6 | n° 15, n° 17, n° 18 |
| 8 | lanceur de course | 6 | n° 11, n° 13 ; régime ; rien ne fuit |
| 9 | `sonde_refus`, `epreuve_temoins`, essai à blanc de bout en bout, mesure des consignes sans appel | 7, 8 | n° 2, n° 3, n° 4, n° 14, n° 27 ; § 6.3 |

Ordre : 0 ; puis 1 et 2 ensemble ; puis 3 ; puis 4 et 5 ensemble ; puis 6 et 7 ensemble ; puis 8 ; puis 9. Chemin critique : 0, 1, 3, 4, 6, 8, 9.

**Les onze questions du lot 0**, chacune avec le fichier et la ligne en réponse :

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

Une réponse qui contredit cette conception revient au concepteur avant le lot concerné.

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
| consignes du portier et des juges, leur contre-lecture | 2,25 |
| liste des motifs, jouée sur le gabarit, la synthèse et les témoins | 1,5 |
| additif du véhicule, sa contre-lecture, ses corrections | 3 |
| contre-lecture du véhicule entier et confirmation de la répartition (règle R2) | 2,5 |
| jeu du tirage, de l'essai à blanc et de la mesure, constats | 1,5 |
| **somme** | **13,75** |

**Lecture.** Environ 45 heures de sessions. Sur le chemin critique : 22,5 heures de lots, puis la contre-lecture du véhicule et le scellement de l'additif, soit 28 à 32 heures d'horloge si deux files tournent sans arrêt, sans limite d'usage atteinte et sans lot rendu deux fois ; 30 à 36 heures avec les témoins scellés et la liste des motifs jouée. Viennent ensuite la pièce de relevés, les deux lignes à part, la lettre de départ, puis la course elle-même, dont je ne connais pas la durée.

**Pour l'échéance de GO-2026-11-20-67.** Parti le 21 novembre vers 07:00Z, le véhicule contre-lu ne peut pas être prêt avant le 22 novembre en fin de journée, et cela sans aucune marge. Un départ honnête se situe entre le 23 et le 24 novembre. Je propose de demander à Lazar une échéance au **2026-11-26** (rapport, D9) : elle couvre un lot à refaire, les deux lignes à part et la course.

Ce qui peut allonger : la place du modèle F, déjà interrompue par sa limite d'usage (OC, l. 44) ; une réponse du lot 0 qui contredit le § 2.3 ou le § 2.9 ; les décisions du rapport, dont trois bloquent un lot (D2 et D3 bloquent les lots 3 à 5 ; D4 bloque le lot 1).

## 9. Ce que la lettre ne fixe pas

Chaque point est repris de l'inventaire, de son rapport ou du gabarit, ou trouvé ici. Chacun porte une **proposition marquée, jamais tranchée**. Les trois premiers sont neufs et pèsent sur le chemin critique.

1. **Les consignes du portier et des juges** *(neuf)*. La V9 gèle ce que reçoit un proposeur ; elle ne dit rien du texte que reçoivent le portier et les juges, et l'inventaire ne le compte pas. Les consignes de la course v9 portent une autre question et d'autres classes. Sans elles, ni l'épreuve des témoins, ni la course ne peuvent partir ; ce sont des pièces fixes servies, donc sous l'arrêt n° 14 et la garde de motifs. *Proposition* : deux consignes courtes, écrites par le modèle F contre la partie servie, aux seules étiquettes fermées du § 2.4, contre-lues, attestées « aucune recette » et scellées par la mère ; les items des juges repris de la course v9 s'ils sont neutres, sinon réduits à un rang.
2. **La syntaxe de la sortie, et ce que l'enveloppe peut porter** *(neuf)*. La partie servie nomme les champs d'une fiche, non la syntaxe où les écrire (PS, l. 19). La V9 dit « rien d'autre de fixe » (l. 73) et confie l'enveloppe à l'additif (l. 77, 254). L'orchestrateur lit aujourd'hui un bloc structuré, et j'ignore ce que son texte fixe de rôle dit au proposeur (lot 0, question 1). *Proposition* : si ce texte fixe existe, est neutre et passe la garde de motifs, il est déclaré à l'additif comme l'enveloppe, épinglé et mis sous l'arrêt n° 14 ; sinon, aucun texte n'est ajouté, et le lecteur de fiches accepte deux syntaxes, un objet par fiche ou des lignes « champ : valeur ». Dans les deux cas, la part « réponse illisible » de l'essai et de la sonde est regardée avant le départ.
3. **Le « nom » d'une ligne du registre servi** *(neuf)*. La V9 sert, pour une tentative passée, « son nom » et « son énoncé ramené à une ligne » (l. 63). La fiche de la question v5 n'a ni champ de nom, ni champ d'énoncé (PS, l. 19) ; son champ `filiation` cite « l'identifiant d'une fiche du registre servi ». *Proposition* : le nom est l'identifiant opaque de la fiche, celui que `filiation` cite ; l'énoncé est le champ `idee`, espaces ramenés à un seul, sans coupe. Un champ `idee` au-dessus de sa borne sort la fiche du contrat à la réception, pour qu'une idée trop longue n'arrête pas la génération suivante par l'arrêt n° 19. Les lignes de compte ne sont écrites que pour un compte non nul ; elles sont permutées avec les autres.
4. **Où se porte la clé de tirage de l'identifiant.** Au « complément contre-lu » (V9, l. 254) ; il n'y a pas de lot 2 (CV, l. 68). *Proposition* : à l'additif du véhicule, que la mère dit valoir complément pour cette seule valeur.
5. **L'ordre du portier, et ce qu'on appelle « le portier ».** La lettre dit que « le portier » envoie au coffre une fiche à champ de plus et refuse une fiche hors case. *Proposition* : le portier est l'ensemble du programme et du modèle, dans l'ordre du § 2.4 ; le modèle n'est pas appelé pour une fiche que le programme de forme a déjà envoyée au coffre. Une réponse illisible ou un refus du modèle portier vaut « au coffre », comme à la course v9, et se compte à part, parce qu'elle pèse sur la garde du coffre.
6. **L'arrêt n° 1 en course.** « Le tour s'arrête » (V9, l. 372) ne dit pas si c'est l'appel, le rôle ou la course. *Proposition* : l'appel ; il est consigné sous le nom de l'arrêt, non relancé, sans reformulation ; la course continue et le rapport le dit par espèce. À la sonde, il arrête le départ.
7. **La lecture « accepte » ou « refuse » à la sonde.** La lettre la confie à « la même garde » sans la décrire ; la table des lignes à part ne prévoit aucun appel de portier à la sonde (CV, l. 127 à 130). *Proposition* : par programme seul. Au moins une fiche complète au contrat : « accepte ». Statut de refus d'un classifieur : arrêt n° 1. Tout le reste, texte sans fiche compris : « réponse que la garde ne sait pas lire », arrêt n° 27, et la mère demande une étiquette à la session à part sans lire la réponse. La borne de sortie de la sonde est mise assez haut pour une fiche entière.
8. **La case que portent les témoins** (gabarit, § 6, point 9). *Proposition* : la première case de la réserve (§ 5.2).
9. **Le devis final** (inventaire, n° 9). *Proposition* : la mesure des consignes sans appel et la pièce de relevés en tiennent lieu, si la mère le dit ; le véhicule rend les chiffres, il n'écrit pas de devis.
10. **Le pire d'un appel d'aiguilleur et de juge, et où il s'écrit** (rapport de l'inventaire, § 3, point 4). *Proposition* : à l'additif du véhicule, sur la mesure ; candidats du § 2.3.
11. **Les mesures « lues une fois »** (V9, l. 315). M5 dépend de la lecture d'antériorité, qui suit de loin la relecture. *Proposition* : deux lectures scellées, chacune unique : M1 à M4, M6, M7, C1 et I1 après la relecture ; M5 après la lecture d'antériorité.
12. **L'ordre entre les témoins et la garde de motifs** (inventaire, § 3). *Proposition* : brouillons des deux, garde jouée sur les témoins en moteur simulé au lot 2, puis scellement ensemble.
13. **Les cinq programmes du § 4.10 de l'inventaire.** *Propositions* : les chaînes de requête de la classe (i) de l'antériorité, dans le véhicule, au lot 7, parce qu'elles se calculent « à partir de la case » et du tirage ; le programme de la condition (c) de l'additif 1 et celui d'ouverture de la branche, hors du véhicule, dus après le départ, sauf les deux contrôles du § 2.6 ; le programme de la pièce de relevés, hors du véhicule, à la mère.
14. **La mémoire qui évite les redites** (OC, l. 27), que la V9 ne reprend pas. *Proposition* : non jouée. Elle écarterait ou marquerait des fiches hors des trois classes que la V9 gèle, et rien ne dit qu'elle doive.
15. **La branche de quarantaine avant les deux lignes à part** (rapport de l'inventaire, § 3, point 8). Le véhicule n'en dépend pas : il écrit dans un dossier de sortie hors de l'arbre de travail. *Proposition* : le dossier suffit pour les lignes à part ; la branche est due avant la première lecture.
16. **Qui lance le véhicule.** La session de l'organisme le lance et ne doit rien lire d'une fiche. *Proposition* : la règle commune du § 2 et l'épreuve « rien ne fuit » la tiennent ; la mère dit si cela suffit, ou si le lancement revient à la session à part.
17. **Un artefact de l'arrêt n° 12 a perdu son objet.** La V9 éprouve « un appel du juge de l'espèce 3 présenté sur la clé du proposeur de l'espèce 3 » (l. 383), et l'additif 1 garde ce cas (A1, l. 169). Depuis l'additif au complément, ces deux rôles sont sur la même clé (AC, l. 56) : l'artefact ne peut plus être refusé. *Proposition* : le remplacer par « le juge de l'espèce 3 présenté sur la clé de l'aiguilleur », et garder les deux artefacts écrits depuis (CV, l. 166 ; AC, l. 175) ; c'est un changement de la lettre d'une épreuve, donc un mot de la mère.

## 10. Réserves du concepteur

1. **J'ai lu le code en partie.** En entier : `course2_v68.py`, `noyau_v56.py`, `aiguilleur_v53.py`. En partie : `course2_v53.py` (l. 1 à 330), L10 (l. 1 à 140, 496 à 565, 2889 à 3160, et la liste de ses fonctions), E9 (l. 1 à 120). Non lus : les adaptateurs, les relais, `ideation_v8.py`, `budget_v56.py`, les fichiers de fiches et de juges, L9 hors son empreinte et le compte de ses fonctions. Le lot 0 existe pour cela.
2. **Je n'ai lu ni la question, ni le corps de la synthèse servie, ni aucune sortie de modèle.** La partie servie est lue en entier.
3. **L'additif de la v69 est lu dans sa v1** (`aef8ff2f…`), son § 7 seulement ; la version scellée est la v4 (registre, R-4131), que je n'ai pas ouverte.
4. **Les heures du § 8 sont une estimation**, sans mesure propre : elles s'appuient sur deux durées lues et sur le nombre de pièces.
5. **Les valeurs chiffrées que je propose** (numéro de clé 40, forme du mot, forme de la ligne de case, séparateurs) sont des valeurs du concepteur ; aucune n'a valeur de règle avant l'additif scellé.
6. Les parts, les seuils et la table des rôles sont recopiés de CV et d'AC ; en cas d'écart, ces pièces font foi.

— concepteur du véhicule, modèle F
