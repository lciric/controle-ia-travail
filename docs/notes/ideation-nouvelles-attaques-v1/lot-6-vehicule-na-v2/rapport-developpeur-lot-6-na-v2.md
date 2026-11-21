# Rapport du développeur — véhicule NA-1, lot 6 v2 (reprise du lot 6 v1 récupéré, refus de câblage) — v1

- Développeur neuf du lot 6 v2 du véhicule NA-1, modèle O. Je n'ai écrit ni le lot 6 v1, ni les lots 1 à 5 ni 10 a, ni la conception, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21, session du compte organisme, vers 18:30Z et après.
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucun relais lancé, aucun commit, aucune écriture dans un dépôt, aucune attache de dépôt. Rien ouvert sous `additif-matiere-premiere-v1/`, `archives-reponses-modeles/`, `/root/.claude/` ; aucune branche `quarantaine/…` ni `matiere-premiere/…`. Données factices seules. **Aucun refus de permission, de classifieur ni de garde rencontré.**
- Mot de Lazar en tête du mandat (GO-2026-11-21-74), lu : « tous de faux positifs je confirme ». Aucune coupure n'est revenue.

## 1. Verdict

- **Refus de câblage écrit et éprouvé** : au départ de la course et à la construction de chaque génération, un contexte d'appel en état 1 ou 2 dont le journal n'est pas `JournalRequetesColonneNA` est refusé par l'arrêt nommé `ArretCablageColonneNA` (numéro à l'additif), inscrit aux arrêts connus, au journal des arrêts et des générations et au bilan. Les trois épreuves du mandat passent (état 1 avec le journal de la colonne : départ ; états 1 et 2 avec un journal ordinaire : refus nommé ; état 0 avec un journal ordinaire : départ) ; les mutations qui retirent le refus (N01, N02, N03 et suivantes) sont tuées.
- **Essais du lot 6 v2 seuls : 116 passés, 0 échec** (`journal-essais-na-lot-6-v2.txt`) : 96 portés du v1 (95 du v1 et un neuf du lanceur), 20 neufs du câblage.
- **Chaîne entière sur copie neuve** (v68, lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a posés par leurs programmes, puis le paquet v2 par le mien, `--lancer-essais`) : **759 passés, 78 sous-essais passés, 0 échec** (`journal-essais-chaine-copie-neuve-na-lot-6-v2.txt`). Décompte : lots 3 à 5, 361 ; lot 10 a, 99 (égaux à leurs rapports) ; lot 6 v2, 116 ; lot 2 v5 et v68, 183 (égal au reste de la chaîne du v1, 639 − 361 − 95).
- **Mutations : 51 tuées sur 51** sur la copie d'application (`journal-mutations-na-lot-6-v2.json`) : les 34 du v1 rejouées sur les fichiers v2, et 17 neuves ; témoin non muté : passe ; témoin inerte : survit ; aucune invalide. Même issue sur la copie de travail, avant le manifeste (`brouillon-mutations-travail-v2.json`).
- Programme d'application : cas sain appliqué ; six refus éprouvés (§ 5).
- Rapport, table d'empreintes, un compagnon par fichier : écrits (le v1 ne les avait pas).

## 2. Pièces lues (empreinte recalculée)

| pièce | empreinte |
|---|---|
| mandat de reprise du lot 6 v2 | `89b2a38d1b38d3a925afa8c40fa59415abd7935e09f429a2fd0ec1686abe7b1a` (égale à celle donnée) |
| mandat du lot 6 v1 | `b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d` |
| erratum 1 v2 (prime sur le mandat v1) | `24d37f857f1e77399c8015a00b5d0b0d2f422301f1c873c39a760806d1601730` |
| note de lancement (racine, dossiers) | `08a6bac6…` (voir § 9, table) |
| LISEZ-MOI du lot 6 v1 récupéré | voir § 9 |
| lot 10 a : rapport ; vérification (remarque 1 et ligne 3 du § 2) | `dcbe5f8d…` ; voir § 9 |
| base v68, tirée d'`origin/main` par `git show … >` mon dossier : manifeste ; programme d'application | `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` ; `9b6e684389037e0018cfe74b41ca60863d85c92ccf7bef530f1db7e33a18c4e7` (égales à leurs compagnons sur `origin/main`) ; les huit fichiers du paquet v68 vérifiés par son programme contre son manifeste |
| orchestrateur, clone en lecture seule | `/home/user/lciric/ideation-organism`, tête `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (relevée par `git rev-parse HEAD`) |

## 3. Ce que la v2 ajoute : le refus de câblage

Lettre : mandat de reprise, point 1 ; mot de la mère du 21 novembre à 18:15Z (GO-2026-11-21-69) ; vérification du lot 10 a, § 2 ligne 3 et § 5 remarque 1 (« rien ne force le journal de la colonne … au lot 6 ou 8 de refuser un contexte dont le journal n'est pas `JournalRequetesColonneNA` quand l'état ≥ 1 »).

Module `paquet/orchestrator/pole/course_na_v2.py` (noté C2).

| exigence | code |
|---|---|
| la course reçoit l'état de l'interrupteur et une fabrique de journal, sans défaut | C2:653 `executer_course_na_v2(…, etat_colonne, fabrique_journal, …)` (arguments nommés obligatoires) |
| état inconnu ou fabrique absente : refus avant toute écriture | C2:664 à C2:669 |
| refus au départ de la course | C2:706 (journal de la génération 1 fait par la fabrique), C2:707 `refuser_cablage(…, "départ de la course")` |
| refus à la construction de chaque génération | C2:339 dans `GenerationNA.__init__`, avant tout appel au constructeur de la v68 et du lot 4 ; l'état passe par `ContexteGenerationNA.etat_colonne` (C2:293, C2:730) |
| la règle : état 1 ou 2 et journal autre que `JournalRequetesColonneNA` : refus | C2:166 `refuser_cablage`, C2:178 à C2:180 ; états gardés C2:89 |
| arrêt nommé, numéro à l'additif | C2:150 `ArretCablageColonneNA` (numéro `None`) |
| inscrit aux arrêts connus | C2:228 (`ARRETS_CONNUS`) ; attributs sans contenu portés à la ligne d'arrêt : `moment`, `etat_colonne`, `type_journal`, `cause` (C2:236 `decrire_arret`) |
| inscrit au journal des arrêts et des générations | par le chemin d'arrêt commun du v1 (C2:784, ligne « arrêt » ; C2:793, « clôture » ; sceau C2:794) ; l'état reçu est aussi écrit à la ligne « départ » (C2:695) |
| le journal de la génération 1, ouvert au départ, est scellé s'il n'a pas servi ; un refus de sceau est dit à la ligne d'arrêt, jamais tu | C2:199 `_sceller_si_ouvert`, chemin d'arrêt de la course C2:771 à C2:780 |
| la fabrique de la colonne pour le lanceur | C2:188 `fabrique_journal_colonne(depart)` (exige un `DepartColonne`) |
| le lanceur exige le contrôle de départ de la colonne et passe état et fabrique | `demonstrations/lancer_orchestrateur_na_v2.py` (noté L2) : L2:126 (refus avant toute écriture), L2:156, L2:157 |

Pour le reste (génération, surcharge de `juger`, étapes, gardes héritées, arrêts n° 5, 6, 7, 8, 10, 14, A17, A2, garde de remplacement, journal des arrêts, ligne de la génération), le code est celui du v1 récupéré, inchangé ; § 4 en donne les lieux dans C2.

## 4. Exigences du lot 6 (v1, reprises) et lieux du code

Lieux dans C2 sauf mention ; `pole/configuration_course_na_v1.py` noté F (inchangé, mêmes octets que le v1) ; `pole/simulation_na_v1.py` noté S (inchangé).

| exigence (lettre) | code |
|---|---|
| classe de génération : le mélange du lot 4 devant `GenerationV68` | C2:323 `GenerationNA(ag.AppelGardeNA, GenerationV68)` |
| `fournisseurs_requis` : seuls les rôles de la table (proposeurs, aiguilleur, juges) | C2:327 |
| proposition neuve (lot 3 ; aucune reprise du noyau) | C2:380 `_proposer`, C2:399 `_classer_retour_proposeur`, C2:312 `_lire_texte` |
| six étapes, deux retirées : jouées = arrêt | C2:363, C2:367 (`EtapeNeutraliseeJouee`, C2:144) |
| étape « aiguillage » surchargée, portier neuf (lot 5) ; E4 : `refus_ecrit` rendu avant `r` et `lu` | C2:458 ; C2:431 `_appeler_portier` |
| surcharge de `juger` : passeport du portier neuf (A17), identifiant réencodé fait des mêmes octets, `self.appel`, verdicts au coffre, A2 sur version servie changée | C2:493 ; C2:498 ; C2:484 et C2:491 ; C2:523 |
| refus écrits, par rôle ; garde de remplacement ; un rôle arrêté le reste (contrôle de la v5, point 1) | C2:399 à C2:409 ; C2:121 `ArretRemplacementRefusEcritsNA` ; borne lue F:277 |
| A3 et A14 désactivées par écrit, vérifiées au départ ; délai d'A3 actif ; A11 ; nom réservé | F:235 `verifier_gardes_heritees` (F:243 à F:275) |
| régime (quatre conditions) | F:201 `verifier_regime` |
| copie de la configuration par génération ; arrêt n° 14 | F:325, F:345 ; C2:711, C2:713 ; F:366 |
| n° 10 (disjonction) | C2:714 |
| n° 8 (borne de la requête) ; n° 8, 9, 19 (registre servi) | C2:585 ; C2:590, C2:601 |
| n° 6 (réservation) ; n° 7 (seuils, nœud budgétaire nommé) ; n° 5 (coffre) | C2:722 ; C2:132 et chemin du nœud ; C2:758 |
| E5 : journal des arrêts et des générations, ajout seul, scellé, jamais servi | C2:257 ; C2:794 |
| E6 : ligne de la génération, comptes fusionnés sans renommer | C2:614 `ligne_de_generation` |
| E7 : table « artefact » refusée | F:294 ; contexte du lot 4 |
| E8 : faux fournisseur, taille et empreinte du corps et de chaque message | S:223 `empreintes_messages`, S:244 `FauxFournisseurNA`, S:255 |
| mémoire déclarée, servie à personne | `executer` de la v56 (non surchargé) ; ligne C2:614 (`memoire.servie = False`) |
| lanceur : moteur simulé à l'essai à blanc seul ; moteur réel aux quatre conditions | L2:54 `decider_moteur`, L2:124 `preparer`, L2:87 |

## 5. Essais et mutations

**Commandes** (`TMPDIR` posé dans mon dossier avant le premier essai ; une commande simple par appel ; interprète `/home/user/controle-ia-travail/.venv/bin/python`, sauf les programmes d'application, joués par `python3 -B`) :
1. `python3 -B pieces-origin-main/v68/appliquer_paquet_orchestrateur_v68_v1.py --source /home/user/lciric/ideation-organism --destination application` : conforme, huit fichiers, `git status` propre.
2. Les programmes des lots 2 v5, 3 v3, 4 v1, 5 v1 et 10 a, `--destination application`, dans cet ordre : 17, 6, 9, 12 et 4 fichiers copiés, aucun refus.
3. `ecrire_manifeste_et_compagnons_na_lot6_v2.py manifeste /home/user/orchestrateur-a41b7b50/orchestrator /home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1` : 11 fichiers, 56 dépendances, manifeste `f978a5c9…`.
4. `env TMPDIR=… NA_LISTE_REELLE_DEPOT=/home/user/controle-ia-travail …/python -B appliquer_paquet_vehicule_na_lot_6_v2.py --destination application --lancer-essais` : 11 fichiers copiés, **759 passés, 78 sous-essais passés**.
5. `env TMPDIR=… …/python -B -m pytest -v -p no:cacheprovider` sur les trois fichiers d'essais du lot 6 v2 dans la copie : **116 passés**.
6. `env TMPDIR=… …/python -B application/orchestrator/essais/mutations_na_lot6_v2.py --racine application/orchestrator --journal journal-mutations-na-lot-6-v2.json` : 53 jouées, 51 tuées, témoins conformes.
7. Refus du programme d'application : seconde application sur `application` (« cible déjà présente … (R12) ») ; destination `/home/user/orchestrateur-a41b7b50` (« source de l'orchestrateur ») ; destination `paquet` ; copie nue, v68 seule (« dépendance absente … `garde_motifs_na_v4.py` ») ; même copie avec les lots 2 à 5 mais sans le lot 10 a (« dépendance absente … `matiere_premiere_na_v1.py` ») ; paquet altéré d'une ligne, dans une copie sous `tmp/` (« fichier du paquet absent ou altéré : `paquet/orchestrator/pole/course_na_v2.py` »). Code 2 chaque fois, rien copié.

**Essais du refus de câblage** (`essais/test_na_lot6_v2_cablage.py`, 20) :

| garde | cas sain | artefact |
|---|---|---|
| refus au départ | état 1, journal de la colonne en état 1 ; état 2, journal de la colonne en état 2 (conditions d'allumage d'essai du lot 10 a) ; état 0, journal ordinaire ; état 0, journal de la colonne éteinte : trois générations, aucun arrêt, un journal neuf par génération, `etat_colonne` à la ligne « départ » | états 1 et 2, journal ordinaire : `ArretCablageColonneNA`, moment « départ de la course », numéro `None`, une ligne « arrêt », aucun appel, aucune génération, journal de la génération 1 scellé vide, bilan sans génération |
| refus à la construction | état 0, journal ordinaire à la génération 2 : trois générations | états 1 et 2, journal ordinaire à la génération 2 : arrêt au moment « construction de la génération 2 », génération 1 au bilan, rien de la génération 2, son journal scellé vide, aucun journal de la génération 3 |
| renforcement (E-1) | états égaux (ci-dessus) | état 1 et journal de la colonne en état 0 ; état 2 et journal en état 1 ; état 1 et journal en état 2 : refus « autre état » |
| état et fabrique | — | états 3, −1, `True`, `False`, `"1"`, `1.0`, `None` ; fabrique `None`, chaîne, objet non appelable : refus avant toute écriture ; fabrique qui rend un objet non journal (états 0 et 1) : refus au départ, aucun fichier de journal ; course sans `etat_colonne` ni `fabrique_journal` : `TypeError`, rien écrit ; `fabrique_journal_colonne` sans `DepartColonne` : `DefautLot6` |
| ce que le refus protège | journal ordinaire, état 0 : la ligne plantée part (une ligne « envoi » à son empreinte) | journal de la colonne, état 1 : `ArretColonneNA`, une ligne « non envoyé » de l'arrêt de la colonne, aucun envoi à son empreinte |

**Essais portés du v1** (`test_na_lot6_v2_course.py`, 53, dont 52 du v1 ; `test_na_lot6_v2_arrets.py`, 43, tous du v1) : les 95 du v1, inchangés dans leur fond (imports v2 ; le montage court en état 1 avec le journal de la colonne ; le lanceur reçoit un contrôle de départ en état 1), plus `TestLanceur::test_sans_controle_de_depart_de_la_colonne_refus_avant_toute_ecriture` (trois moteurs ou modes × trois contrôles faux : code 2, `LancementRefuseNA` nommé par `executer`, rien écrit, aucune fabrique réelle appelée). Les cas sains et artefacts des arrêts n° 5, 6, 7, 8, 10, 14, 19, d'A17, A2, de la garde de remplacement, des refus écrits par rôle, des gardes héritées une par une, du régime, des étapes neutralisées, de `hors_course`, de la mémoire, d'E5 à E8 et des identifiants des juges sont ceux du v1 (liste au journal des essais).

**Mutations** (`essais/mutations_na_lot6_v2.py`) : T0 (témoin non muté) passe ; T1 (témoin inerte) survit ; M01 à M34 (celles du v1 : E4, garde de remplacement et son cran, A17, A2, identifiant hexadécimal servi au juge, n° 10, n° 14 trois fois, A3, A14, délai d'A3, A11, S12 deux fois, `fournisseurs_requis`, lecture qui rend rien, n° 8, n° 5, n° 7, n° 6, étape neutralisée en silence, n° 19, Z4-25, E8, lanceur, régime deux fois, E6, verdict absent, case non jouée, E5 deux fois, fiche non portée au registre) : toutes tuées sur les fichiers v2 ; N01 à N17 (neuves) :

| id | faute | tuée par |
|---|---|---|
| N01 | aucun état n'exige le journal de la colonne | refus au départ, états 1 et 2 |
| N02 | refus au départ retiré | refus au départ, état 1 (le moment devient « construction de la génération 1 ») |
| N03 | refus à la construction retiré | refus à la génération 2, état 1 |
| N04, N05 | état 2, puis état 1, non gardé | refus au départ, état 2 ; état 1 |
| N06 | renforcement retiré | renforcement, deux essais |
| N07, N08 | état inconnu, booléen, admis au départ | états inconnus (refus après écriture : la sortie existe) |
| N09 | fabrique absente : repli silencieux sur le journal ordinaire | fabrique absente |
| N10, N11 | lanceur : état 0 imposé ; journal ordinaire passé | essai à blanc du lanceur |
| N12 | lanceur : contrôle de départ non exigé | refus nommé du lanceur (la panne fortuite ne suffit pas) |
| N13 | refus trop large (état 0 refusé) | état 0, journal ordinaire |
| N14 | journal de la génération 1 non scellé au refus de départ | refus au départ, état 1 |
| N15 | arrêt hors des arrêts connus | refus au départ, état 1 (nom) |
| N16 | générations 2 et 3 sur le journal de la génération 1 | cas sain, état 1 |
| N17 | fabrique de la colonne qui rend un journal ordinaire | cas sain, état 1 |

## 6. Formats pour les lots 7, 8 et 10 a (figés ici ; le v1 ne les avait pas écrits)

Tous les fichiers sont dans le dossier de sortie de la course, neuf (R12) ; aucun ne recopie un octet d'une réponse, d'une fiche ou d'une ligne du registre servi hors des dossiers `generation-<g>/`.

**Arborescence de la sortie.**
- `journal-arrets-et-generations-na-v1.jsonl` (+ `.sha256` au sceau) : le journal des arrêts et des générations (E5). Nom de fichier gardé du v1 (le format n'a gagné qu'un champ de la ligne « départ » et une sorte d'arrêt ; la liste fermée des événements est la même).
- `bilan-course-na-v1.json` (scellé par `ecrire_json_scelle`) : le bilan ; son champ `version` vaut `course-na-v2`.
- `journaux/journal-requetes-g<g>.jsonl` (+ `.sha256`) : le journal des requêtes de la génération g, fait par la fabrique reçue ; en état 1 ou 2, un `JournalRequetesColonneNA` (lot 10 a), qui écrit au format du lot 3 v3 (quatre événements : `envoi`, `non envoyé`, et les deux autres du lot 3), sans événement neuf.
- `generation-<g>/` : le dossier de la génération (v68 et v56), dont `registre-tentatives-g<g>.jsonl`, `journal-portier-g<g>.jsonl`, `memoire.json` (déclarée, servie à personne), `manifeste-fin.json`.

**Journal des arrêts et des générations** (ajout seul, `pole.portier_na_v1.FichierAjoutSeul`, lu par `course_na_v2.lire_journal_arrets_generations(chemin, exiger_sceau=True)`). Champs permis par ligne : `evenement`, `generation`, `depart`, `copies`, `arret`, `ligne`, `cles`, `cloture` (et ceux de la classe d'ajout seul : rang, chaînage). Événements, liste fermée, dans cet ordre :
1. `départ` — `depart` : `version` (`course-na-v2`), `regime`, `gardes_heritees` (l'état vérifié, F:280), `plafond_course_usd`, `empreintes` (table des empreintes des pièces), `statut_des_valeurs`, `go`, **`etat_colonne`** (neuf en v2 : 0, 1 ou 2).
2. `copies de configuration` — `copies` : {"1": sha256, "2": sha256, "3": sha256}.
3. pour chaque génération complète : `génération` (`generation`, `ligne` : la ligne de la génération, ci-dessous) puis `cumul par clé` (`generation`, `cles` : `cumul`, `cause_non_etablie_par_cle`, `etat_relais_illisible_par_cle`) — seul lieu des comptes par clé.
4. au plus une ligne `arrêt` — `generation` (None au départ), `arret` : `type`, `numero` (None : à l'additif), `nom`, et, s'ils existent et sont sans contenu : `role`, `cle`, `piece`, `generation`, `etape`, `clause`, `famille`, `rang`, `cause`, `n`, **`moment`**, **`etat_colonne`**, **`type_journal`** (ces trois neufs en v2), puis `poste`, `motif` (signal), et `journal_requetes_g1` si le sceau du journal de la génération 1 a été refusé.
5. `clôture` — `cloture` : `generations_completes`, `arret`. Puis le sceau.

Le refus de câblage s'y lit ainsi : au départ, `arret.type = "ArretCablageColonneNA"`, `arret.nom = "câblage de la colonne : journal du contexte d'appel autre que celui de la colonne"`, `arret.moment = "départ de la course"`, `generation = None`, aucune ligne `génération` ; à la construction, `arret.moment = "construction de la génération <g>"`, `generation = g`, les générations précédentes au journal.

**Ligne de la génération** (C2:614 ; E6), clés : `generation`, `cases_servies`, `copie_configuration_sha256`, `registre_servi` (None à la génération 1 ; sinon `sha256`, `taille`, `lignes`, `lignes_tentative`, `lignes_compte`, `comptes_permutes`, `section`, `requetes_l_ayant_recu`), `comptes_melange_lot_4` (tel quel, `na_comptes`), `comptes_portier_lot_5` (tel quel, `portier.comptes()`), `comptes_journal_lot_3` (tel quel, `journal_na_v3.comptes`), `comptes_envois_lot_4`, `comptes_lot_6` (`appels_proposeur`, `issues_proposeur`, `cases_non_jouees`, `refus_ecrits_proposeur`, `verdicts_absents`, `appels_juge`, `fiches_jugees`, `registre_servi_recu_par`), `au_coffre_par_refus_du_portier` (à part), `arrets_consignes`, `coffre` (`au_coffre`, `rendues`, `depasse`, `consigne`), `etapes`, `cout_generation_usd`, `cout_par_role_usd`, `cout_par_adaptateur_usd`, `memoire` ({`fichier`: `memoire.json`, `servie`: false}), `journal_requetes_sha256`, `noeud`. **Les refus de la garde de la colonne** (tenue ii) ne sont pas dans `na_comptes` : ils sont au journal des requêtes, ligne `non envoyé` d'arrêt « garde de la colonne « matière première » », donc dans `comptes_journal_lot_3` ; le compte par rôle `JournalRequetesColonneNA.comptes_colonne` n'est pas recopié à la ligne (remarque R3, § 7).

**Bilan** (`bilan-course-na-v1.json`) : `version`, `regime`, `go`, `generations` (les lignes ci-dessus), `arret` (comme au journal, ou None), `signaux`, `budget_course` (état de `GardeBudgetCourseV68` : `version`, `regle`, `plafond_course_usd`, `cumul_usd`, `reste_usd`, `depassement_usd`, `journal`), `statut_des_valeurs`.

**Pour le lot 8 (lanceur de course).**
```
depart = mp.preparer_depart(...)                     # lot 10 a, avant toute écriture
rc = lancer_orchestrateur_na_v2.principal(argv, depart_colonne=depart)   # ou executer(args, depart_colonne=depart)
# en interne : cn.executer_course_na_v2(..., etat_colonne=depart.etat,
#                                       fabrique_journal=cn.fabrique_journal_colonne(depart), ...)
```
Sans `DepartColonne`, le lanceur refuse avant toute écriture (`LancementRefuseNA`, code 2). Qui appelle la course sans le lanceur doit passer `etat_colonne` et `fabrique_journal` (arguments obligatoires, sans défaut) ; un journal ordinaire en état 1 ou 2 est refusé par l'arrêt nommé. La tenue (iii) du lot 10 a (`mp.garder_registre_servi`) et le contrôle des pièces fixes à la génération 2 se branchent par `gardes_depart_en_plus=(f,)`, `f(g, registre_servi, requetes)` (inchangé du v1) ; le lot 6 v2 ne les branche pas lui-même (le mandat de reprise ne le demande pas).

**Pour le lot 10 a.** Le lot 6 v2 lit de `matiere_premiere_na_v1` : `ETAT_ETEINTE`, `ETAT_GARDE_SEULE`, `ETAT_ALLUMEE`, `DepartColonne` (`etat`, `colonne`), `Colonne`, `JournalRequetesColonneNA` (constructeur `(dossier, nom, *, depart)`, attribut `depart`), `ArretColonneNA`, `GenerationRefuseeColonneNA`, `RefusColonneNA`, `ARRET_COLONNE`. Ce sont ses interfaces figées ; une autre forme casse le refus au départ (essais du câblage).

**Pour le lot 7.** Il lit le journal des arrêts et des générations et le bilan aux formats ci-dessus ; les comptes de chaque source sont sous leur clé, jamais additionnés ; l'état de la colonne est à la ligne `départ`.

## 7. Écarts du v1 (LISEZ-MOI) et les miens

**Écarts du v1, tels que le LISEZ-MOI de la session les dit** (`b7073926…`) — repris, non corrigés par moi sauf mention :
- V1-1. Orchestrateur lu sur les copies données à la reprise (commit `a41b7b50`). Repris : j'ai cloné, en lecture seule, `/home/user/lciric/ideation-organism` (tête `a41b7b50…` relevée), par le programme de la v68.
- V1-2. Base v68 posée par copie de ses fichiers tirés d'`origin/main`. Repris : tirés par `git show origin/main:… >` vers `pieces-origin-main/v68/`, programme d'application et manifeste égaux à leurs compagnons ; la base est posée par **son propre programme**, qui vérifie chaque fichier du paquet contre son manifeste et le `git status` de la copie.
- V1-3. Variable `NA_LISTE_REELLE_DEPOT` posée pour trois essais du lot 2. Repris, de même (§ 5), vers `/home/user/controle-ia-travail` : le défaut écrit des lots 2 à 5 nomme une racine absente de ce conteneur. La liste est lue par l'essai, jamais affichée ni copiée.
- V1-4. Dossiers temporaires `/tmp/essais-na-lot6-*` créés avant `TMPDIR`. Non reproduit : `TMPDIR` posé dans mon dossier avant le premier essai. Je n'ai pas nettoyé ceux du v1 (hors de mon dossier).
- V1-5. Une sortie trop longue rangée par l'outil sous `/root/.claude/`, non ouverte. Non reproduit à ma connaissance ; je n'ai rien ouvert sous `/root/.claude/`.
- V1-6. Rapport, table, compagnons manquants. Comblé par ce rapport, sa table et un compagnon par fichier.
- V1-7 (vu par moi). Les remarques que le v1 n'a pas écrites (ce que la lettre ne fixe pas) : je les écris au § 7, remarques R1 à R6, pour ce que j'ai vu du code ; je n'ai pas reconstitué les choix du v1 au-delà du code.

**Mes écarts.**
- E-1. **Renforcement du refus** (au-delà de la lettre, dans son sens) : en état 1 ou 2, un `JournalRequetesColonneNA` dont le contrôle de départ porte **un autre état**, ou aucune colonne chargée, est refusé par le même arrêt (C2:181 à C2:184). Raison : un journal de la colonne en état 0 (`colonne = None`) laisse tout passer ; sans ce renforcement, la garde serait muette sous une course qui se dit en état 1. Essais et mutation N06. Comme le mot de la mère, il renforce la garde ; il est à confirmer.
- E-2. Un état autre que 0, 1, 2 (booléen compris) et une fabrique absente sont refusés par le même arrêt nommé, **avant toute écriture** (C2:664 à C2:669), et non par un `DefautLot6`. Un objet qui n'est pas un journal du lot 3 l'est aussi, au départ.
- E-3. Le contrôle « au départ de la course » porte sur **le journal de la génération 1**, fait par la fabrique dès le départ (après la création de la sortie et les lignes `départ` et `copies de configuration`, pour que l'arrêt soit inscrit au journal des arrêts) ; ce journal sert ensuite à la génération 1. S'il n'a pas servi (arrêt avant la génération 1), il est scellé vide.
- E-4. Le lanceur v2 **exige** le contrôle de départ de la colonne (`depart_colonne`, argument Python de `principal` et `executer`) ; il n'y a pas d'option en ligne de commande pour l'état : l'état ne vient ni de la ligne de commande, ni de la configuration, ni de l'environnement (lot 10 a). Un essai à blanc en ligne de commande seule est donc refusé ; le lot 8 ou 9 passe le `DepartColonne`.
- E-5. **Noms** : les fichiers changés ou neufs portent `v2` ; les quatre fichiers inchangés (`configuration_course_na_v1`, `simulation_na_v1`, `ecrire_configuration_course_essai_na_v1`, `configuration_essai_na_lot6_v1`) gardent leur nom et leurs octets (empreintes égales au manifeste du v1). Le v1 récupéré n'est pas posé : ni `course_na_v1.py`, ni le lanceur v1, ni ses essais ne sont dans le paquet v2, pour qu'aucune course sans le refus ne soit installable à côté. Les 95 essais du v1 sont **portés** (imports v2, montage câblé en état 1) et rejoués ; ses 34 mutations sont rejouées sur les fichiers v2.
- E-6. Noms des fichiers de sortie gardés du v1 (`journal-arrets-et-generations-na-v1.jsonl`, `bilan-course-na-v1.json`) pour ne pas déplacer le lot 7 ; la version est dans le champ `version`. À trancher si R12 doit s'appliquer aux sorties.
- E-7. Le montage d'essai du lot 6 v2 tourne par défaut **en état 1, avec le journal de la colonne** (contrôle de départ d'essai du lot 10 a, registre aux lignes inertes) : tous les essais portés du v1 jouent ainsi la garde de la colonne en course. Les pièces fixes contrôlées au départ par le lot 10 a sont ses pièces factices, non celles de la configuration du lot 6 (le contrôle des pièces fixes n'est pas du ressort du lot 6).
- E-8. Une commande de liste hors des dossiers permis : `ls` du dossier `docs/notes/ideation-nouvelles-attaques-v1/` lui-même (noms seuls, pour trouver les dossiers des lots ; aucun sous-dossier interdit ouvert). Écart au mandat, dit.
- E-9. La copie d'application est un clone git (fait par le programme de la v68, comme le v1) dans mon dossier ; je n'y ai fait aucun commit.
- E-10. Une sortie trop longue (une comparaison `diff -rq` du paquet et de la copie de travail, noms de fichiers seuls) a été rangée d'office par l'outil sous `/root/.claude/…/tool-results/` ; je ne l'ai pas ouverte, et j'ai refait la comparaison par empreintes, fichier par fichier (onze fichiers égaux). Même écart que V1-5 du v1.
- E-11. Les dossiers `travail/` (copie de développement) et `copie-nue/` (refus d'application) et `tmp/` sont dans mon dossier, hors de la table ; `travail/` porte aussi le paquet, pour les mutations de brouillon.

**Remarques (ce que la lettre ne fixe pas ; rien n'est tranché ici).**
- R1. Numéro de l'arrêt de câblage : à l'additif (`numero = None`).
- R2. En état 0, le journal de la colonne est reçu (il ne garde rien) ; un journal ordinaire aussi. La lettre ne dit rien d'un état 0 servi par un journal de la colonne d'un autre état ; je le reçois.
- R3. Les refus de la garde de la colonne ne sont comptés qu'au journal des requêtes (`comptes_journal_lot_3`, sous le nom de l'arrêt) ; `comptes_colonne` du journal de la colonne n'est pas porté à la ligne de la génération (E6 ne le nomme pas). Point pour le lot 7 ou l'additif.
- R4. La garde de la colonne, en course, lève `ArretColonneNA` qui arrête la course (arrêt nommé, au journal) : c'est le comportement du lot 10 a, que je ne change pas ; mon objet de contrôle le montre (§ 5).
- R5. Les tenues (iii) et le contrôle des pièces fixes à la génération 2 ne sont pas branchés par le lot 6 v2 (voir § 6) : à brancher par le lot 8, ou à mander au lot 6.
- R6. `GenerationNA` reçoit l'état par `ContexteGenerationNA.etat_colonne`, que la course remplit ; une génération construite hors de la course (essai, outil) doit le remplir aussi, sans défaut.

## 8. Relevé de méthode

**Chaîne de raisonnement.**
1. Le mandat de reprise (`89b2a38d…`) demande, en plus du v1 récupéré, le refus de câblage : au départ de la course et à la construction de chaque génération, refus si l'état est 1 ou 2 et que le journal n'est pas `JournalRequetesColonneNA` ; arrêt nommé, numéro à l'additif ; trois épreuves nommées ; une mutation qui retire le refus doit être tuée.
2. Le besoin vient de la vérification du lot 10 a (`b2e77af1…`, § 2 ligne 3, sonde V-F) : le contexte du lot 4 accepte tout `jn.JournalRequetes`, donc un journal ordinaire en état 1 laisse partir une ligne égale à une entrée de la colonne.
3. La garde de la colonne en course (tenue ii) vit dans `JournalRequetesColonneNA.journaliser_envoi` (`matiere_premiere_na_v1.py`, l. 491 à 520, fichier posé à l'empreinte du manifeste du lot 10 a par son programme) ; elle ne lit que `self.depart.colonne` : un journal de la colonne dont le départ est en état 0 (`colonne = None`) ne garde rien (l. 508 et 509). D'où le renforcement E-1 (pas 1 et 3 ; supposé conforme à l'intention de la mère : il ne fait que refuser davantage).
4. Le contrôle est placé à deux lieux : C2:707 (départ, sur le journal de la génération 1 fait par la fabrique) et C2:339 (construction, avant tout constructeur hérité). Un essai pour chacun, aux moments distincts (`moment` à la ligne d'arrêt), et une mutation pour chacun (N02, N03), tuées (pas 6).
5. Le reste est le v1 inchangé : 95 essais portés (imports v2, montage en état 1) passent, plus un essai neuf du lanceur ; les 34 mutations du v1 rejouées sur les fichiers v2 sont tuées (calcul rejoué, § 5).
6. Les essais du câblage (20) passent ; les 17 mutations neuves sont tuées ; témoin non muté : passe ; témoin inerte : survit (journal des mutations, § 5).
7. Sur copie neuve (v68, lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a, posés par leurs programmes, puis le paquet v2 par le mien) : la chaîne entière passe (§ 5).
8. Le programme d'application refuse : seconde application (R12), copie de référence de l'orchestrateur, paquet comme destination, copie nue (sans le lot 2), copie sans le lot 10 a, paquet altéré d'un octet (§ 5).

**Objets de contrôle.**
- Refus de câblage, au départ. Faux par construction (« le câblage est sûr » est faux) : état 1, puis état 2, avec un journal ordinaire. Attendu : arrêt nommé `ArretCablageColonneNA`, moment « départ de la course », aucun appel, aucune génération, journal de la génération 1 scellé vide, ligne au journal des arrêts. Rendu : idem (`TestCablageRefuseAuDepart`). Vrai par construction : état 1 et état 2 avec le journal de la colonne au même état, état 0 avec un journal ordinaire ; attendu : trois générations, aucun arrêt ; rendu : idem (`TestCablageSain`).
- Refus de câblage, à la construction. Faux par construction : génération 1 câblée juste, génération 2 avec un journal ordinaire (états 1 et 2). Attendu : arrêt nommé au moment « construction de la génération 2 », génération 1 au bilan, rien de la génération 2 écrit. Rendu : idem. Vrai : état 0, même fabrique mixte ; attendu et rendu : trois générations.
- Renforcement (E-1). Faux : état 1 avec un journal de la colonne en état 0 ; état 2 avec un journal en état 1 ; état 1 avec un journal en état 2. Attendu : refus « autre état ». Rendu : refus. Vrai : états égaux (ci-dessus).
- État et fabrique. Faux : états 3, −1, `True`, `False`, `"1"`, `1.0`, `None` ; fabrique `None`, chaîne, objet non appelable ; fabrique qui rend un objet qui n'est pas un journal. Attendu : refus nommé, avant toute écriture (ou, pour l'objet rendu, au départ, aucun fichier de journal). Rendu : idem.
- Ce que le refus protège. Une ligne égale à une entrée du registre d'essai, plantée dans une requête de proposeur. Journal ordinaire, état 0 : attendu « elle part » ; rendu : une ligne « envoi » à son empreinte. Journal de la colonne, état 1 : attendu « elle ne part pas » ; rendu : `ArretColonneNA`, une ligne « non envoyé » de l'arrêt de la colonne, aucun envoi à son empreinte (`TestCeQueLeRefusProtege`).
- Lanceur. Faux : sans contrôle de départ (`None`, un dictionnaire, un entier) pour les deux moteurs et pour `--verifier-seulement`. Attendu : `LancementRefuseNA` nommé, avant toute écriture, aucune fabrique réelle appelée. Rendu : idem (l'essai exige le refus nommé, non une panne fortuite : mutation N12 tuée). Vrai : contrôle de départ en état 1, essai à blanc simulé et moteur réel factice ; rendu : course complète, `etat_colonne` à la ligne « départ ».
- Juge des mutations. Témoin non muté : passe ; témoin inerte : survit ; aucune mutation invalide (chaque texte cherché présent une fois).
- Programme d'application. Six artefacts refusés, un cas sain appliqué (§ 5).

**Premier pas non justifié.** Le pas 3, pour sa partie « renforcement » : que refuser un journal de la colonne d'un autre état que celui de la course est voulu par la mère. Le justifierait un mot de la mère (ou l'additif) qui l'écrit ; jusque-là c'est l'écart E-1, déclaré.

**Mode d'échec affecté.** Sans objet : je suis développeur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je suis développeur, non agent de re-dérivation.

**Trouvaille de côté.**
- Les essais du v1 et les miens laissent leurs dossiers temporaires (`essais-na-lot6-v2-*`) sous `TMPDIR` : dans mon dossier, données factices seules, hors de la table.
- `comptes_colonne` du journal de la colonne n'est porté nulle part dans la ligne de la génération (remarque R3).
- La garde de la colonne, en course, arrête toute la course à la première ligne égale (R4) ; si la mère voulait un refus de case seulement, c'est au lot 10 a ou à l'additif.

**Évaluateur et conseil.** Ce qui juge mon produit : les essais du lot 6 v2 (portés du v1 et neufs) et les 51 mutations, rejouables par le vérificateur S sur une copie neuve par mon programme d'application ; témoins non muté et inerte. Par où il pourrait être bien jugé sans le mériter : les essais, les mutations et le code sont du même auteur (sauf les 34 mutations et 95 essais du v1, d'un autre développeur O) ; le registre de la colonne et le contrôle de départ sont ceux, factices, du lot 10 a ; le refus repose sur `isinstance` d'une classe du lot 10 a, qu'une sous-classe qui surchargerait `journaliser_envoi` pour ne rien garder contournerait (non éprouvé : hors de la lettre ; à dire au vérificateur).

## 9. Table d'empreintes et pièces

Pièces lues (recalculées, égales à leurs compagnons) : mandat de reprise `89b2a38d1b38d3a925afa8c40fa59415abd7935e09f429a2fd0ec1686abe7b1a` ; mandat du lot 6 v1 `b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d` ; erratum 1 v2 `24d37f857f1e77399c8015a00b5d0b0d2f422301f1c873c39a760806d1601730` ; note de lancement `08a6bac6bcf7298a0b33b371262d61c5c8de50b64701fd245ffb4d8af3737852` ; LISEZ-MOI du v1 récupéré `b707392642fde3e8381c035b8d3465eaad7856d2315a1f5973e3c840194d8c25` ; manifeste du v1 récupéré `2c18dd2cb14eb691cbffb72e7b0508922eef9d8a5e264e5fea5802bcbc66c2c7` ; rapport du lot 10 a `dcbe5f8d705120f5b18739ca006f9b68c8e3c32d36b902aa19d6c8aa0e6c366c` ; vérification du lot 10 a `b2e77af10732e23b14cc6be495fee7f622789c86c19912075ed6d23161b8ad9b`.

Livré (dossier `dev-vehicule-na-lot-6-v2/`, copie aux jalons sous `/home/user/dossiers-developpeurs-vehicule-na-v1/lot-6-v2/`) :

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/course_na_v2.py` | `03e6bd4d624c563d42e5ad0de4f26b407de31411e58aa4adf1461b1962dd8932` |
| `paquet/orchestrator/demonstrations/lancer_orchestrateur_na_v2.py` | `0252ba2746d663e301503fd94807b2b52a84daec6b1873ef930970da1c41610b` |
| `paquet/orchestrator/essais/aides_na_lot6_v2.py` | `aa4351c5bb4181ecc2847d49cb80e61a8c5026d7630c6256d9ca96c6aaa90dab` |
| `paquet/orchestrator/essais/test_na_lot6_v2_course.py` | `1a2046a54ac356d8d38be78ba15cd7e096b97025aa173a7059624ea0a8f7da1e` |
| `paquet/orchestrator/essais/test_na_lot6_v2_arrets.py` | `a6039e459c50fd30bac6471e34d2073c7adedf4c1544a5b84028b533e29d088f` |
| `paquet/orchestrator/essais/test_na_lot6_v2_cablage.py` | `f7a0b74d9f6fe7329c0b462137b5590df0410dba7063e55d88ecab1ba9b71e91` |
| `paquet/orchestrator/essais/mutations_na_lot6_v2.py` | `3f04969b8f65b55917d16392243ca4151d40b264e01accbeee588e9f93d86cfc` |
| `paquet/orchestrator/pole/configuration_course_na_v1.py` (inchangé du v1) | `0264479234576b3b66e7fd1af35475c3a7858a9a1ef3c5cf949c2f753aaf5c18` |
| `paquet/orchestrator/pole/simulation_na_v1.py` (inchangé) | `3ab45961b588641081cbdd027e00b2025dad08cbdfcdbfe72d0c0f800ee91344` |
| `paquet/orchestrator/demonstrations/ecrire_configuration_course_essai_na_v1.py` (inchangé) | `ea23b740ecc670cd60582f5d900ff6dd84308b284ae648aad234aa3d040e8283` |
| `paquet/orchestrator/essais/configuration_essai_na_lot6_v1.py` (inchangé) | `5372190597287f7ed860c9d6a30bc583bd7b0afbddf42f1da5f2e053f4b77ca6` |
| `manifeste-paquet-vehicule-na-lot-6-v2.json` | `f978a5c9f496af26b6799247e85c127e757ac74a7b7ce0bb7e48a34f70641815` |
| `appliquer_paquet_vehicule_na_lot_6_v2.py` | `f07379ed8b9dbaaeb90f9adc99d5cd5d676ea548ba1ffdcabf3202be8272183a` |
| `ecrire_manifeste_et_compagnons_na_lot6_v2.py` | `4ae1201852ba341b9b745c8a57c944f421325b989fa82758f0001b205a65e723` |
| `journal-essais-na-lot-6-v2.txt` | `eed5c83d36407fdf0afb5e83ad4427f3ab38fa4370a7840186e20444855eefb2` |
| `journal-essais-chaine-copie-neuve-na-lot-6-v2.txt` | `aa0433cbcdbcc0bc2967ce823c7bdccafe7e7e3fcf953536e2ebba71a2feda21` |
| `journal-mutations-na-lot-6-v2.json` ; `brouillon-mutations-travail-v2.json` (mêmes octets) | `b49b5d5d21cf866fa97f6e2d1894d7c16dd430e9a61314755d3270a7bccd9591` |
| `pieces-origin-main/v68/…` (hors table, tirés d'`origin/main`) | manifeste `4ed9fd8e…`, programme `9b6e6843…` |

La table complète, ce rapport compris, est `table-empreintes-dossier-na-lot-6-v2.txt` (écrite après ce rapport, avec son compagnon) ; un compagnon `.sha256` par fichier de la table.

— développeur du lot 6 v2 du véhicule NA-1, modèle O
