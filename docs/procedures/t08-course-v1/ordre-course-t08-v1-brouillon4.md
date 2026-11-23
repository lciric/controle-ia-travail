# Ordre de course — base boîte noire (T0.8) : épisodes honnêtes d'étalonnage et lectures des juges sur une machine louée — v1 — brouillon 4

- **Statut** : **brouillon 4**, pièce de classe A : **le brouillon des commandes**. Il ajoute au brouillon 3 (`6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8`) les commandes exactes rendues par le développeur de la chaîne de lancement (section 13), et ce que son rapport demande à l'ordre (P7, étape 9) ; opérations : `journal-pieces-de-course-t08-brouillon4-v1.md`. **Il n'est exécutable qu'une fois la chaîne contre-lue et les préalables P1 à P10 tenus.** Le brouillon 3 inscrivait au brouillon 2 (`727db6ce402a5f23c76b1323d16d42f4c076ac47992a82452e40193a7ac9a6b1`) la décision de la session mère sur le constat J-1 (R-5017 de `registres/decisions.md` : sections 2 et 10) et le contrôle du commit que porte le manifeste de la course (section 2, étape 9, section 12) ; opérations : `journal-pieces-de-course-t08-brouillon3-v1.md`, même dossier. Le brouillon 2 appliquait au brouillon 1 (`295493dd88a1e36a4981926fad9a5fa03e3c3d59ef699eacf240030c74ee0fde`) les constats O-1, O-2, O-3, m-O1 et m-O2 de la contre-lecture 1 (`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon1-cl1.md`, `3ea629e8b1818f885a655776a0ce025dcad9f8ce2f93fa5123690ec40961e2c6`) ; rien d'autre n'y change, hors les renvois d'un brouillon à l'autre (opérations : `journal-pieces-de-course-t08-brouillon2-v1.md`, même dossier). Ce brouillon fixe la séquence, les contrôles, les arrêts, la dépense et les rôles ; ce brouillon 4 y porte les commandes exactes. Aucune machine ne se crée tant qu'un préalable manque.
- **Auteur** : rédacteur du texte de T0.8 (modèle B), session `session_013QMayo5SNVbiUW6hGnPrCo`, le 2026-11-22 à partir de 19:25 UTC. **Contre-lecture** : brouillon 1 contre-lu par un sous-agent neuf d'un autre modèle, lancé par la session mère (`consigne-contre-lecture-pieces-de-course-t08-v1.md`, même dossier) ; les brouillons 2 et 3 ont été vérifiés conformes par le même contre-lecteur (`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon2-verification-cl1.md` (`4440161d1fbc9150a6b0aca0c40ef9f314d2e0608db7813e4f892f52e310614b`) et `…-brouillon3-verification-cl1.md` (`d24b216b752b80e16133232ae9779bbd890c13d2a962d8a50a40a98fd03428bd`)) ; la différence de ce brouillon 4 est à vérifier de même.
- **Ce que l'auteur savait** : aucun fichier de données, de diagnostic ni de run de la course de confirmation ouvert ; aucun résultat lu ; du code, le rapport du premier développeur de T0.8 (§ 6 et § 7), l'en-tête et l'entrée en ligne de commande du module de course, les en-têtes du lanceur et de l'amorce de la course de confirmation, le plan de son ordre de course.
- **Accord de dépense** : `GO-2026-11-10-12`, type « calcul », plafond 120 USD, prolongée au 31 décembre 2026 par `GO-2026-11-22-79` et `GO-2026-11-22-93`.

## 0. Objet

Jouer une fois, sur une carte louée, la course que décrit le texte scellé de T0.8 : 320 épisodes honnêtes d'étalonnage, puis les lectures des juges à 8 et à 3 milliards de paramètres sur les actions de la course de confirmation et de l'étalonnage ; pousser ses sorties scellées ; détruire la machine. La lecture sur processeur et le verdict viennent après, par d'autres agents (section 10).

## 1. Ce qui fait foi

Le texte scellé de T0.8 (`prereg/T0.8-bases-boite-noire-v0-v1.md`, ligne `SCELLEMENT-T08`) : son « Plan d'analyse » (points 1 à 4), sa « Liste d'arrêt », sa section « Machine, devis et dépense ». **Cet ordre n'ajoute ni ne change aucune règle de ce texte ; en cas de divergence, le texte scellé prime, et l'exécutante s'arrête et l'écrit.** Il dit seulement dans quel ordre faire les gestes, qui les fait, et ce qui les arrête.

## 2. Embargo et chemins interdits

- La machine ne reçoit que la branche d'entrée et le code cité. Jamais la branche de sortie de la course de confirmation ; jamais un fichier dont le nom commence par `lecture-sondes-t06`, ni `resume.json`, ni `distillation-t06.json`, ni une activation, ni un adaptateur.
- **L'exécutante ne lit aucune sortie de la course** : les scores des juges sont des résultats. Elle manipule des noms, des tailles, des empreintes et des lignes de journal de service. Elle n'ouvre aucun fichier de `diag/`, `runs/` ou `donnees/` de quelque course que ce soit, hors le manifeste de sa propre course pour son identifiant, sa date et son commit.
- Elle n'ouvre aucune pièce du saboteur à budget, du bras A ni du bras d'attaque, et n'envoie rien de cette course à leurs sessions : les seuils et les scores des moniteurs ne vont pas du côté de ceux qui conçoivent un saboteur.
- **Relais du verdict** (décision de la session mère, R-5017 de `registres/decisions.md`, sur le constat J-1 de la contre-lecture 1) : la session mère, qui orchestre aussi le saboteur à budget, ne reçoit de la lecture et du verdict de T0.8 que des chemins et des empreintes ; le verdict est soumis à Lazar par la **session relais du verdict de T0.8** — neuve, inscrite à la liste « qui a lu quoi », sans aucune part au saboteur —, que la session mère crée au moment voulu ; les branches de la lecture et du verdict de T0.8 sont interdites aux sessions du saboteur à budget.
- Les clés passent par leur nom, jamais par leur valeur ; aucune n'est affichée ni écrite.

## 3. Préalables bloquants

Vérifiés par l'exécutante, un par un, écrits à son journal avec l'heure relevée par la machine. Un préalable non tenu : aucune création.

| n° | préalable | preuve |
|---|---|---|
| P1 | Texte scellé | le fichier, son compagnon et la ligne `SCELLEMENT-T08` portent la même empreinte ; le validateur de préenregistrement ne trouve rien |
| P2 | Code cité | la ligne `CODE-T08` cite le commit que porte le texte ; l'arbre extrait à ce commit a les empreintes de sa pièce ; son rapport de contre-lecture est celui que cite le texte |
| P3 | Antériorité | le passage à blanc sur le registre réel rend le code 0 : `SCELLEMENT-T08` et `CODE-T08` sont antérieures à l'heure de la machine (garde gardée par `GO-2026-11-22-122`) ; l'essai de cette garde a son cas sain et son artefact — une ligne `SCELLEMENT-T08` postérieure à l'heure de la machine est refusée (consigne de la chaîne de lancement, § 4) |
| P4 | Accord de dépense | la ligne de GO citée est de type « calcul » et valide à la date de création, prolongations comprises (GO-2026-11-22-79 et -93 : fin au 31 décembre, plafond de GO-2026-11-10-12) ; la garde de calcul et le lanceur, éprouvés à blanc à une date antérieure et à une date postérieure au 30 novembre, admettent la commande avec ce GO et la refusent sans lui. **Fait relevé dans la garde de calcul** (`.claude/hooks/garde_calcul.py`) : elle contrôle l'échéance de chaque identifiant d'accord que porte la commande, sans suivre les prolongations. Jusqu'au 30 novembre, la commande porte `GO-2026-11-10-12`. À partir du 1er décembre, elle porte la ligne de prolongation `GO-2026-11-22-79` et aucun identifiant échu ; le lanceur vérifie que cette ligne prolonge `GO-2026-11-10-12` et lit le plafond, 120 USD, à la ligne d'origine ; l'accord d'origine et `GO-2026-11-22-93` sont cités au journal et au registre des dépenses, hors de la commande. La garde de calcul n'est pas modifiée |
| P5 | Dépense | la ligne d'engagement est inscrite ; la dépense antérieure sous cet accord est relevée au registre des dépenses et passée au lanceur |
| P6 | Branche d'entrée | construite par programme ; sa liste de fichiers est la liste blanche de la course, à l'octet et aux empreintes du texte ; aucun fichier interdit ; branche orpheline |
| P7 | Chaîne de lancement | lanceur, amorce, configuration réelle de la course : écrits, contre-lus, corrections vérifiées ; leurs empreintes au commit `C` sont celles du rapport de contre-lecture de la chaîne ; l'essai du code aligné que l'amorce écarte de la machine est joué dans la session au commit `C`, réussi (section 13) |
| P8 | Minuterie du plafond | son essai, cas sain et artefact, est joué avant la création (« Liste d'arrêt » du texte) |
| P9 | Compte du loueur | aucune machine du programme pour cette tâche n'y existe déjà (inventaire par identifiants) ; le crédit couvre le pire cas d'une tentative |
| P10 | Clés | présentes par leur nom : loueur, dépôt des modèles, dépôt de code |
| P11 | Suite | le lecteur et le juge de verdict sont désignés, inscrits à la liste « qui a lu quoi », et n'ont vu aucun résultat de sonde de la course de confirmation — non bloquant pour la création, bloquant pour la lecture |

## 4. Étapes

Chaque étape se journalise avant la suivante. Les commandes exactes sont en section 13.

1. **Dossier et journal.** Un dossier de travail neuf ; un journal de l'exécutante, une ligne par geste, heure de la machine.
2. **Préalables P1 à P10**, dans l'ordre.
3. **Contrôles à blanc du lanceur**, sans dépense : configuration, calendrier de l'accord, bornes de l'offre, clés par leur nom.
4. **Offre.** Recherche filtrée dans les bornes de « Machine » : une carte A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 8 cœurs effectifs, 64 Go de mémoire vive, 100 Go de disque, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go. Les prix se lisent dans la réponse du loueur, jamais à la main. Aucune offre dans les bornes : aucune création ; l'exécutante l'écrit et attend.
5. **Commande de création imprimée, relue avant toute exécution** : la carte, les prix, le disque, l'amorce à son empreinte, la branche d'entrée, le commit du code, l'accord cité par `GO_ID`. Un champ qui diffère de cet ordre : aucune création.
6. **Création, une fois.** L'identifiant de la machine se lit dans le fichier de lancement, jamais retapé. L'exécutante prévient la session mère, qui inscrit la machine « en tâche » dans l'état vivant.
7. **Plafond tenu sans la session.** À la création, l'heure où la dépense projetée au prix de l'offre atteint le plafond restant — 120 USD moins la dépense antérieure sous cet accord, relevée en P5 — est calculée et passée à l'amorce ; la minuterie consigne et pousse les résultats partiels à cette heure, puis détruit.
8. **Surveillance.** Un relevé toutes les trente minutes (geste de service : il ne fonde ni arrêt ni lecture) : la machine est à l'inventaire, la dernière ligne de progression, la dépense cumulée. Deux heures sans ligne de progression : alerte à la session mère, **sans arrêt** (essai de cette alerte, consigne de la chaîne de lancement, § 4 : une ligne récente, rien ; deux heures écoulées, alerte, sans arrêt). **Aucun couperet de temps** pour une course lente mais vivante. À 40 USD cumulés : compte rendu à Lazar par la session mère.
9. **Fin.** Les sorties scellées sont poussées par l'amorce sur la branche de sortie. L'exécutante vérifie la poussée sans ouvrir les contenus : noms, tailles, compagnons, empreinte du résultat `course-t08.json`. Elle vérifie aussi, par les noms seuls, le commit que porte le manifeste de la course : son seul parent est le commit du code que cite `CODE-T08`, et il n'y ajoute que la liste déclarée — entrées de la liste blanche de la course, texte scellé, configuration réelle de la course, leurs compagnons —, rien sous un chemin gelé du code. (Le manifeste exige un arbre propre et le texte scellé sous la racine ; le texte scellé cite le commit du code et ne peut donc pas s'y trouver : la tête de la course est un enfant de ce commit, fait par l'amorce avant la course.) Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis. **Fin en anomalie de taille** (rapport de la chaîne, réserve 5 : un fichier de plus de 90 Mo est retiré du commit et reste sur la machine) : aucune destruction, aucune ligne `COURSE-T08` ; nœud pour la session mère, qui décide du versement (section 8).
10. **Ligne `COURSE-T08`**, inscrite par la session mère : chemin et empreinte de `course-t08.json`.
10 bis. **Course arrêtée** (plafond, minuterie, processus mort, fichier interdit, empreinte ou commit différents) : aucune ligne `COURSE-T08` ; les résultats partiels sont versés sous un nom qui dit « partiel » (section 8) et n'entrent dans aucune lecture ; la destruction de l'étape 11 suit ce versement ; tant qu'aucune sortie scellée de la course n'existe, le juge de verdict rend la ligne D1 et, pour chaque dose, la ligne F1 (texte, tables D et F), sur le motif consigné. Une relance n'a lieu que dans les conditions de la section 9, et jamais après un arrêt au plafond, qui ne laisse pas de quoi la payer.
11. **Destruction par l'identifiant** (R10), après la vérification de la poussée ; inventaire final ; ligne au registre des arrêts ; dépense réelle au registre des dépenses. Aucune garde de 72 heures : rien n'est à relire sur la machine.

## 5. Carte H200

Aucune, ni en relance automatique ni en repli. Elle demande un mot de Lazar, donné pour cette course.

## 6. Dépense

- Attendu ≈ 17 à 30 USD : 14 à 20 h de carte. Pire cas d'une tentative ≈ 57 USD ; ≈ 114 USD avec une relance.
- Plafond : **120 USD cumulés, toutes tentatives comprises**. À ce montant : arrêt par l'identifiant, résultats partiels consignés comme tels.
- Les débits des juges sont supposés d'après P3 ; c'est le poste le plus incertain. Une course plus lente que prévu n'est pas une panne.

## 7. Arrêts

Ceux de la « Liste d'arrêt » du texte, et eux seuls. Pour l'exécutante :

- processus de la course mort sans arrêt consigné : arrêt de la machine par son identifiant ;
- dépense cumulée au plafond : arrêt par l'identifiant ;
- un fichier interdit trouvé sur la machine, ou un chemin hors de la liste blanche demandé : arrêt et nœud ;
- une empreinte d'entrée, le commit du code ou le texte scellé qui diffèrent de ce qui est consigné : arrêt.

Elle n'arrête jamais sur un résultat : elle n'en lit pas. Tout arrêt se fait par l'identifiant de la machine, jamais par un motif de ligne de commande (R10).

## 8. Avant de détruire une machine en échec

Mot de Lazar du 19 novembre : récupérer ce qui est récupérable. Avant toute destruction après un arrêt : inventaire de ce que la machine porte (noms, tailles, empreintes, sans ouvrir les contenus), versement scellé sur une branche dont le nom dit ce qu'elle est (« partiel », « arrêtée »). Ce qui est versé n'entre dans aucune lecture sans un texte contre-lu et le mot de Lazar.

## 9. Panne technique et relance

Une course arrêtée pour une cause technique déclarée — authentification, quota, crédit, perte de la machine, réseau, transfert ou poussée tronqués — a droit à **une** relance sur le même accord, sous le même texte scellé, sur une branche de sortie neuve, si aucune lecture n'a eu lieu (ligne D1 du texte ; GO-2026-11-22-77). La borne de 400 jetons par action n'est jamais une panne. Une seconde erreur de chaîne : nœud, aucune relance. L'essai entre au registre des idées de la veille de cap avec son issue codée.

## 10. Ce qui suit, et qui ne revient pas à l'exécutante

1. **Lecture sur processeur**, par le lecteur neuf, sous sa consigne (`consigne-lecteur-t08-v1-brouillon4.md`) ; ligne `LECTURE-T08`.
2. **Verdict** des tables D et F, par le juge de verdict neuf, sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon3.md`) ; ligne `VERDICT-T08`, inscrite par la session mère par le chemin et l'empreinte ; soumis à Lazar par la session relais du verdict de T0.8 (section 2).

## 11. Compte rendu de l'exécutante

À la session mère, des nombres de service seulement : identifiant de la machine, heures de création, de fin et de destruction, prix de l'offre, dépense, identifiant du run, branche de sortie, empreinte de `course-t08.json`, nombre de fichiers poussés, arrêts et alertes. **Aucun score, aucun taux, aucun compte tiré des sorties.**

## 12. Ce qui était à écrire, et qui l'est en section 13

Les commandes exactes des étapes 2 à 11 ; les empreintes du lanceur, de l'amorce, du programme de la branche d'entrée et de la configuration réelle de la course ; le nom de la branche d'entrée et de la branche de sortie ; le filtre exact de l'offre ; le montant de crédit exigé au préalable P9 ; l'identifiant d'accord que porte la commande à la date de création (préalable P4) ; la commande qui vérifie le commit du manifeste et la liste déclarée de ce qu'il ajoute (étape 9) ; l'identifiant de la session exécutante (donné par la session mère).

## 13. Commandes exactes

Source : rapport du développeur de la chaîne de lancement, § 8, `docs/notes/t08-chaine-de-lancement-v1/rapport-chaine-de-lancement-t08-v2.md` (`47da96229401335b5b87b32111b4df1d56bb7da15a33c94fd21288d33aaf13b7`, branche `t08/chaine-de-lancement-v1`, commit `12eb328a6bf84960116e4b26bbad332f0df0f257`). Elles sont recopiées, non réécrites. **Elles ne valent qu'au commit `C` que cite `CODE-T08`**, après la contre-lecture de la chaîne (préalable P7) : si cette contre-lecture change une commande, cet ordre change par un brouillon neuf.

**Valeurs données par la session mère au scellement**, écrites au journal de l'exécutante avant l'étape 2 : `S`, commit de `main` qui ajoute le texte scellé ; `C`, commit du code (marqueur `COMMIT_CODE_T08`), qui porte le code aligné et la chaîne de lancement ; `BC`, branche qui porte `C` ; `EA`, empreinte de `scripts/amorce_instance_t08_v1.sh` au commit `C` ; `GO`, `GO-2026-11-10-12` jusqu'au 30 novembre, `GO-2026-11-22-79` à partir du 1er décembre ; `ANT`, dépense antérieure sous cet accord. `D` est le dossier de travail neuf ; `ID`, l'identifiant de la machine, lu dans `$D/lancement.txt`. Branche d'entrée : `entree/t08-course-v1` ; branche de sortie : `calcul/t08-course-v1`. Crédit exigé au préalable P9 : au moins 57 USD, pire cas d'une tentative (section 6).

**Toutes les commandes se lancent depuis un clone de `main` à jour** : sur une branche dont le registre des accords porte une ligne illisible, la garde de calcul refuse toute commande de lancement (rapport, réserve 3).

Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante) : la configuration réelle de la course (`scripts/ecrire_configuration_course_t08_v1.py`), puis la branche d'entrée (`scripts/construire_branche_entree_t08_v1.py construire`), aux commandes du rapport, § 8.

- **P1** : `sha256sum prereg/T0.8-bases-boite-noire-v0-v1.md && cat prereg/T0.8-bases-boite-noire-v0-v1.md.sha256 && grep '^| SCELLEMENT-T08 ' registres/scellements-v1.md`, puis `PYTHONPATH=src python3 -c 'import sys; from controle_ia.prereg import problemes; p = problemes("prereg/T0.8-bases-boite-noire-v0-v1.md"); print(p); sys.exit(1 if p else 0)'`.
- **P2** : `grep '^| CODE-T08 ' registres/scellements-v1.md && git merge-base --is-ancestor $C origin/$BC`.
- **P3** : `PYTHONPATH=src python3 -m controle_ia.t08.passage_a_blanc_v1 --config prereg/T0.8-configuration-course-v1.json --registre registres/scellements-v1.md --prereg prereg/T0.8-bases-boite-noire-v0-v1.md --racine-piece .` (code 0 exigé) ; essai de la garde : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lecture_v1.py -k passage_a_blanc`.
- **P4** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh --verifier-go-seulement prereg/T0.8-configuration-course-v1.json $ANT` ; garde à blanc et dates simulées : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lancement_v1.py -k "garde_de_calcul or accord_prolonge or sans_identifiant_echu"`.
- **P6** : `python3 -I -B scripts/construire_branche_entree_t08_v1.py verifier --depot . --ref refs/remotes/origin/entree/t08-course-v1 --commit-texte $S --texte prereg/T0.8-bases-boite-noire-v0-v1.md --config prereg/T0.8-configuration-course-v1.json`.
- **P7** : `sha256sum scripts/amorce_instance_t08_v1.sh scripts/lancer_t08_v1.sh scripts/construire_branche_entree_t08_v1.py scripts/tests-cibles-t08-v1.txt`, à comparer au rapport de contre-lecture de la chaîne ; puis, dans la session, l'essai que l'amorce écarte de la machine : `PYTHONPATH=src python3 -m pytest -q "tests/test_t08_entrees_rendu_v1.py::test_amorce_instance_clone_de_l_arbre_aligne"`.
- **P8** : `PYTHONPATH=src python3 -m pytest -q tests/test_t08_chaine_lancement_v1.py -k "minuterie or plafond_restant or deux_heures"`.
- **Étape 3** : `GO_ID=$GO T08_BRANCHE_ENTREE=entree/t08-course-v1 T08_BRANCHE_CODE=$BC T08_AMORCE_SHA256=$EA bash scripts/lancer_t08_v1.sh controles $D`. Code 0 exigé ; clés `HF_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN` présentes par leur nom.
- **Étapes 4 et 5** : `GO_ID=$GO bash scripts/lancer_t08_v1.sh creation auto course $ANT $D` ; la commande de création est imprimée, non exécutée. À relire : carte, prix, `--disk 100`, amorce, `BRANCHE_ENTREE` et `ENTREE_COMMIT`, `COMMIT=$C`, `GO_ID=$GO`, et `DEPENSE_EPUISEE_UTC_S`, l'heure du plafond restant. Codes : 0, commande imprimée ; 2, échec ; 3, nœud (aucune offre conforme, machine déjà présente, reste nul).
- **Étape 6** : exécuter la commande imprimée, telle quelle. Code 5 : offre retirée ; rejouer `creation` comme imprimé, trois essais au plus, puis nœud.
- **Étape 8** : `INTERVALLE=1800 bash scripts/lancer_t08_v1.sh surveillance $ID $D`. Codes : 0, fin ; 3, arrêt ; 4, refus de l'amorce.
- **Étape 9** : `git fetch origin refs/heads/calcul/t08-course-v1:refs/remotes/origin/calcul/t08-course-v1 && git ls-tree -r -l refs/remotes/origin/calcul/t08-course-v1 -- runs diag donnees traces` ; empreinte du résultat : `git show refs/remotes/origin/calcul/t08-course-v1:diag/<run>/course-t08.json | sha256sum`, à comparer au compagnon ; commit du manifeste : `PYTHONPATH=src python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import commit_local_v1 as c; sys.exit(c.main(sys.argv[1:]))" verifier-distant . refs/remotes/origin/calcul/t08-course-v1 $C refs/remotes/origin/entree/t08-course-v1` (code 0 exigé).
- **Étape 11** : `vastai destroy instance $ID`, puis `vastai show instances --raw`. L'amorce laisse la machine à l'état arrêté en fin de course ; elle n'est détruite que par ce geste, après l'étape 9.

**Deux différences avec la consigne de la chaîne, déclarées par le développeur et acceptées ici** : (1) l'heure du plafond restant retranche aussi le forfait de téléchargement (environ 2 USD), comme la chaîne de la course de confirmation — la minuterie tombe un peu plus tôt, jamais plus tard ; (2) un essai du code aligné, qui clone l'arbre entier, est écarté de la suite jouée sur la machine et joué dans la session (P7).

**Jamais joué avant la course** (rapport, réserve 6) : le mode réel sur une carte, le vrai loueur, la poussée vers le dépôt distant depuis un clone partiel. Une panne à l'un de ces points relève de la section 9.
