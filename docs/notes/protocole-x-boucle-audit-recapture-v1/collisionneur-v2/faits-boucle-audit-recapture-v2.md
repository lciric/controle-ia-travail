# Faits : une boucle « audit, recapture, réapprentissage » devant un interdit d'usage de l'oracle

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter, ou à borner, un agent qui sabote discrètement des tâches de recherche, par beaucoup de petits dommages plutôt que par un coup unique. Son dispositif :

- des sondes linéaires sur les états internes de l'agent (dimension de l'ordre de quatre mille), sans moyenne sur les jetons ; leur seule garantie porte sur leur taux de fausses alertes, calibré sur des épisodes honnêtes ;
- un oracle du dommage, qui juge le produit d'un épisode après coup : pour chaque contrôle d'une référence cachée, des lecteurs (des modèles d'autres familles que les moniteurs, aveugles à la condition) répondent à une question fermée ; l'oracle ne voit pas tout dommage, et sa probabilité de reconnaître un dommage qu'il regarde n'est pas encore mesurée ;
- un plancher d'audit : une part des épisodes est tirée au hasard et en secret, après la fin de l'épisode, et jugée par l'oracle ; une alarme sonne sur le dommage audité. Une autre part de l'audit peut suivre le soupçon, c'est-à-dire le score des sondes ; toutes les probabilités de tirage sont consignées ;
- la recapture : parmi les épisodes endommagés que l'audit au hasard trouve, le compte de ceux que le moniteur avait signalés ; trop basse, elle fait annoncer « moniteur invalide » ;
- des organismes saboteurs construits pour l'épreuve, et un jumeau honnête (le même modèle sans sabotage) qui n'existe qu'au banc d'essai ; au banc, on sait par construction quels épisodes sont sabotés ;
- des portes : des lectures décisives préenregistrées qui comparent les moniteurs entre eux sur des épisodes réservés, dont une famille de sabotage tenue à l'écart de la conception des moniteurs et lue une seule fois ;
- une réserve de détecteurs jamais employés dans une décision que l'agent observe.

Le programme n'a pas encore de déploiement réel : ses flux d'épisodes sont joués au banc ; un déploiement est un usage futur de la méthode.

## La boucle

Il est proposé que le flux d'audit au hasard fournisse des épisodes endommagés étiquetés ; que la recapture dise si la sonde est devenue aveugle ; et que la sonde soit réapprise sur ces épisodes, les poids de l'agent étant gelés et aucun verdict ne lui revenant, de sorte que le défenseur joue en dernier. Grandeur à rapporter : le rappel retrouvé en fonction du nombre d'épisodes endommagés audités. Deux tests de mort sont écrits. Si le rappel retrouvé avec les étiquettes disponibles avant le seuil de dommage toléré reste sous le niveau validé, la boucle ne se ferme pas à temps. Si un canal de retour vers l'agent est ouvert, le rétablissement doit s'effondrer ; sinon le banc ne mesure rien.

## L'interdit

Une règle antérieure du programme dit : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur ». À l'origine, les sorties de l'oracle ne servent que d'étiquette de vérité à la lecture d'une expérience (un fichier scellé que les moniteurs ne voient pas) et au choix d'une dose de sabotage commune, sans filtrer un seul épisode ; l'oracle est tenu hors de la vue de ceux qui conçoivent les moniteurs. Réapprendre une sonde sur des épisodes jugés par l'oracle entre dans la lettre de cet interdit. Deux options sont sur la table :

- (a) garder l'interdit entier : une détection ne devient un exemple d'apprentissage que dans un cycle déclaré de reconception des sondes, sur des modes de sabotage déjà vus, jamais à partir d'un verdict de l'oracle ;
- (b) restreindre l'interdit au banc et permettre le réapprentissage en service ; inconvénient noté : l'oracle entre dans la sélection des moniteurs, et la recapture ne les juge plus à l'aveugle.

Autres règles du programme : aucun score de moniteur n'entre dans l'entraînement ni dans la sélection de l'agent ; les épisodes sur lesquels un moniteur est calibré sont des épisodes honnêtes, exogènes au suspect : un épisode du suspect, signalé ou non, n'y entre jamais, et un épisode signalé sans preuve de dommage monte dans la file d'audit sans y entrer ; une sonde n'est en principe jamais entraînée et évaluée sur les mêmes organismes ; les moniteurs sont sans mémoire d'un épisode à l'autre ; une lecture décisive ne se relit pas. Une lecture proposée, non encore confirmée, tient qu'annoncer « moniteur invalide » n'est pas sélectionner un moniteur, à deux conditions : la suite d'une annonce n'est jamais un choix, un réglage ou une reconception de moniteur sur les épisodes audités ; les verdicts par épisode ne vont pas aux concepteurs de moniteurs, qui ne reçoivent que le compte et l'annonce.

## Ce qui est publié, dans le domaine

- Un moniteur co-entraîné sur des audits tirés au hasard, face à un ouvrier adverse, a un taux d'erreur qui s'annule si la classe des fonctions de jugement est apprenable en ligne ; les étiquettes y sont supposées sûres, et l'ouvrier y est entraîné avec le retour du moniteur (« Improving scalable oversight with co-trained monitors », arXiv 2609.36049).
- Un modèle peut apprendre, des seuls verdicts passés d'une sonde, à déplacer ses états pour lui échapper ; l'évasion survit à un réajustement de la sonde sur des états sains ; une sonde réapprise sur des tentatives d'évasion étiquetées retrouve la détection, ce qui suppose de les avoir déjà identifiées (« LLMs Learn to Evade Latent Monitors from Prior Feedback Alone », arXiv 2609.36490).
- Un audit d'une fraction tirée au hasard, à probabilités connues et bornées par un plancher, donne une borne valide à tout instant sur un taux de violation, si la pièce reste cachée de l'agent avant l'action (« Blindfold », arXiv 2610.37055).
- Un entraînement ordinaire par renforcement suffit à aveugler des sondes de tromperie apprises hors domaine ; une sonde refaite sur le domaine retrouve la détection (« The Obfuscation Atlas », arXiv 2602.15515).
- Une étude de contrôle asynchrone itère moniteurs et attaques sur des cadres d'entraînement et rapporte son chiffre final sur un cadre tenu à l'écart (« Async Control », arXiv 2512.13526).

## Contraintes

- Peu d'étiquettes : le taux d'audit est celui qui donne une prise avant le seuil de dommage toléré avec probabilité 0,95, quand l'honnête ne commet jamais ce dommage. Quand l'honnête échoue aussi, l'oracle dit « endommagé », pas « saboté ».
- Le jumeau honnête n'existe qu'au banc ; hors du banc, la référence honnête est un autre modèle ou un état antérieur.
- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (suppositions de défense violées), jamais par un mode opératoire.
