# Ordre de course — base boîte noire (T0.8) : épisodes honnêtes d'étalonnage et lectures des juges sur une machine louée — v1 — brouillon 3

- **Statut** : **brouillon 3**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas encore (section 3, préalable P7). Il inscrit au brouillon 2 (`727db6ce402a5f23c76b1323d16d42f4c076ac47992a82452e40193a7ac9a6b1`) la décision de la session mère sur le constat J-1 (R-5017 de `registres/decisions.md` : sections 2 et 10) et le contrôle du commit que porte le manifeste de la course (section 2, étape 9, section 12) ; opérations : `journal-pieces-de-course-t08-brouillon3-v1.md`, même dossier. Le brouillon 2 appliquait au brouillon 1 (`295493dd88a1e36a4981926fad9a5fa03e3c3d59ef699eacf240030c74ee0fde`) les constats O-1, O-2, O-3, m-O1 et m-O2 de la contre-lecture 1 (`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon1-cl1.md`, `3ea629e8b1818f885a655776a0ce025dcad9f8ce2f93fa5123690ec40961e2c6`) ; rien d'autre n'y change, hors les renvois d'un brouillon à l'autre (opérations : `journal-pieces-de-course-t08-brouillon2-v1.md`, même dossier). Ce brouillon fixe la séquence, les contrôles, les arrêts, la dépense et les rôles ; le brouillon des commandes y portera les commandes exactes, quand la chaîne sera écrite et contre-lue. Aucune machine ne se crée sur ce brouillon.
- **Auteur** : rédacteur du texte de T0.8 (modèle B), session `session_013QMayo5SNVbiUW6hGnPrCo`, le 2026-11-22 à partir de 19:25 UTC. **Contre-lecture** : brouillon 1 contre-lu par un sous-agent neuf d'un autre modèle, lancé par la session mère (`consigne-contre-lecture-pieces-de-course-t08-v1.md`, même dossier) ; les corrections des brouillons 2 et 3 sont à vérifier par le même contre-lecteur.
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
| P7 | Chaîne de lancement | lanceur, amorce, configuration réelle de la course : écrits, contre-lus, corrections vérifiées ; leurs empreintes sont celles de cet ordre (brouillon des commandes) |
| P8 | Minuterie du plafond | son essai, cas sain et artefact, est joué avant la création (« Liste d'arrêt » du texte) |
| P9 | Compte du loueur | aucune machine du programme pour cette tâche n'y existe déjà (inventaire par identifiants) ; le crédit couvre le pire cas d'une tentative |
| P10 | Clés | présentes par leur nom : loueur, dépôt des modèles, dépôt de code |
| P11 | Suite | le lecteur et le juge de verdict sont désignés, inscrits à la liste « qui a lu quoi », et n'ont vu aucun résultat de sonde de la course de confirmation — non bloquant pour la création, bloquant pour la lecture |

## 4. Étapes

Chaque étape se journalise avant la suivante. Les commandes exactes sont au brouillon des commandes.

1. **Dossier et journal.** Un dossier de travail neuf ; un journal de l'exécutante, une ligne par geste, heure de la machine.
2. **Préalables P1 à P10**, dans l'ordre.
3. **Contrôles à blanc du lanceur**, sans dépense : configuration, calendrier de l'accord, bornes de l'offre, clés par leur nom.
4. **Offre.** Recherche filtrée dans les bornes de « Machine » : une carte A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 8 cœurs effectifs, 64 Go de mémoire vive, 100 Go de disque, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go. Les prix se lisent dans la réponse du loueur, jamais à la main. Aucune offre dans les bornes : aucune création ; l'exécutante l'écrit et attend.
5. **Commande de création imprimée, relue avant toute exécution** : la carte, les prix, le disque, l'amorce à son empreinte, la branche d'entrée, le commit du code, l'accord cité par `GO_ID`. Un champ qui diffère de cet ordre : aucune création.
6. **Création, une fois.** L'identifiant de la machine se lit dans le fichier de lancement, jamais retapé. L'exécutante prévient la session mère, qui inscrit la machine « en tâche » dans l'état vivant.
7. **Plafond tenu sans la session.** À la création, l'heure où la dépense projetée au prix de l'offre atteint le plafond restant — 120 USD moins la dépense antérieure sous cet accord, relevée en P5 — est calculée et passée à l'amorce ; la minuterie consigne et pousse les résultats partiels à cette heure, puis détruit.
8. **Surveillance.** Un relevé toutes les trente minutes (geste de service : il ne fonde ni arrêt ni lecture) : la machine est à l'inventaire, la dernière ligne de progression, la dépense cumulée. Deux heures sans ligne de progression : alerte à la session mère, **sans arrêt** (essai de cette alerte, consigne de la chaîne de lancement, § 4 : une ligne récente, rien ; deux heures écoulées, alerte, sans arrêt). **Aucun couperet de temps** pour une course lente mais vivante. À 40 USD cumulés : compte rendu à Lazar par la session mère.
9. **Fin.** Les sorties scellées sont poussées par l'amorce sur la branche de sortie. L'exécutante vérifie la poussée sans ouvrir les contenus : noms, tailles, compagnons, empreinte du résultat `course-t08.json`. Elle vérifie aussi, par les noms seuls, le commit que porte le manifeste de la course : son seul parent est le commit du code que cite `CODE-T08`, et il n'y ajoute que la liste déclarée — entrées de la liste blanche de la course, texte scellé, configuration réelle de la course, leurs compagnons —, rien sous un chemin gelé du code. (Le manifeste exige un arbre propre et le texte scellé sous la racine ; le texte scellé cite le commit du code et ne peut donc pas s'y trouver : la tête de la course est un enfant de ce commit, fait par l'amorce avant la course.) Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis.
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

1. **Lecture sur processeur**, par le lecteur neuf, sous sa consigne (`consigne-lecteur-t08-v1-brouillon3.md`) ; ligne `LECTURE-T08`.
2. **Verdict** des tables D et F, par le juge de verdict neuf, sous sa consigne (`consigne-juge-verdict-t08-v1-brouillon3.md`) ; ligne `VERDICT-T08`, inscrite par la session mère par le chemin et l'empreinte ; soumis à Lazar par la session relais du verdict de T0.8 (section 2).

## 11. Compte rendu de l'exécutante

À la session mère, des nombres de service seulement : identifiant de la machine, heures de création, de fin et de destruction, prix de l'offre, dépense, identifiant du run, branche de sortie, empreinte de `course-t08.json`, nombre de fichiers poussés, arrêts et alertes. **Aucun score, aucun taux, aucun compte tiré des sorties.**

## 12. À écrire au brouillon des commandes

Les commandes exactes des étapes 2 à 11 ; les empreintes du lanceur, de l'amorce, du programme de la branche d'entrée et de la configuration réelle de la course ; le nom de la branche d'entrée et de la branche de sortie ; le filtre exact de l'offre ; le montant de crédit exigé au préalable P9 ; l'identifiant d'accord que porte la commande à la date de création (préalable P4) ; la commande qui vérifie le commit du manifeste et la liste déclarée de ce qu'il ajoute (étape 9) ; l'identifiant de la session exécutante.
