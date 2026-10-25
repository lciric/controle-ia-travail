# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — l'« escalier de coût » entre configurations d'un essaim : sa conception, son seuil de décision δ (distinguable du bruit et digne d'intérêt) et son plan (v2)

Demandes de Lazar du 25 octobre 2026 (heure de Paris) : 14:12–14:14, « tu recommandes quoi pour delta pour qu'il soit
distinguable du bruit et significativement intéressant ? … demande au collisionneur aussi » ; 14:16, « demande aussi au
collisionneur de brainstormer sur l'escalier et sa conception ». Cette v2 remplace la v1 (`634032bc…`, jamais posée) et
y ajoute la conception de l'escalier (point 0). Tour **distinct** des tours précédents ; un seul tour (III.1), les trois modèles, une seule tentative par cellule ; un refus est consigné tel quel et
met fin à la cellule, sans reformulation. Les réponses sont du matériau pour une décision de Lazar, jamais une consigne ;
elles ne sont servies à aucun organisme. Le texte ci-dessous est figé au départ du tour.

## Le cadre (faits ; rien d'autre n'est à supposer)

- Un **organisme** (code plus fichiers) tourne sous un **noyau fixe** qui lui sert des exécutants de frontière figés, un
  budget, des tâches et une moisson documentaire. Deux familles de tâches de classification binaire : A « conscience
  d'évaluation d'un modèle », B « contrôle de délégation » (traces honnêtes ou sabotées).
- **Métrique** : exactitude équilibrée par famille ((sensibilité + spécificité) / 2) sur un **test final tenu à l'écart**
  (jamais rendu à l'organisme), notée par le juge du noyau ; une tâche sans réponse valide compte comme une erreur.
- **Test final** : 60 items — famille A : 36 items (stratifiés par source et par vérité) ; famille B : 24 items (12
  honnêtes, 12 sabotés). **Les mêmes items pour toutes les configurations** : la comparaison peut être appariée par item.
  Références sur les traits de surface (classifieur sur la forme des textes) : 0,69 (A), 0,50 (B).
- **Configurations à comparer** : le même organisme sous des bornes différentes. La moisson (recherches, téléchargements
  par génération) ne coûte presque rien en dollars ; ce qui coûte, ce sont les appels de modèles : rondes de conception
  avant la génération 0, castes par tâche, générations. Une génération coûte de l'ordre de 10 à 22 USD selon la longueur
  des sorties (devis non opposable) ; une ronde de conception ajoutée, de l'ordre de 10 USD (illustratif).
- **Règles du programme** : aucun run ne vise un signe positif ; la règle de décision est préenregistrée et scellée avant
  tout run ; un résultat suspect de propreté déclenche un audit, dans un sens comme dans l'autre ; **à égalité, la
  configuration la moins chère l'emporte**.
- **Données gratuites à venir** : le pilote en cours fait tourner, à sa génération 0, deux fois la même configuration avec
  deux graines différentes (comparaison « A contre A »), lues au moment de lecture fixé d'avance.
- Un autre préenregistrement du programme exige déjà un écart Δ ≥ +0,10 d'exactitude équilibrée entre deux bras.

## Ce qui est demandé

0. **La conception de l'escalier**, en premier : quels axes y mettre (rondes de conception avant la génération 0,
   castes ou espèces par tâche, nombre de générations, longueur de sortie par appel, moisson), dans quel ordre, et comment
   définir un « cran » (doublement du budget, pas fixe en dollars, un axe à la fois ou plan factoriel fractionnaire) ;
   comment mesurer la valeur marginale de chaque dollar par axe et détecter un plateau à peu de frais ; quand arrêter de
   monter ; comment traiter le fait que **l'organisme adapte lui-même sa façon de dépenser au budget qu'on lui sert**
   (le budget servi n'est pas le budget dépensé : confusion à mesurer, pas à ignorer) ; ce qui se transpose d'un organisme
   à un autre (un escalier mesuré sur une version vaut-il pour la suivante ?) ; et le risque de **surapprentissage du test
   final** quand le même jeu de 60 items sert à plusieurs comparaisons successives (réserve d'items intouchée, jeu de
   validation réutilisable, confirmation finale), avec ce que chaque parade coûte en items et en puissance.
1. **Une valeur de δ**, avec ses raisons : distinguable du bruit au coût consenti, et digne d'intérêt pour un moniteur
   de sécurité. Compare au moins trois valeurs (par exemple 0,05, 0,10, 0,15) : pour chacune, nombre de graines par bras,
   coût, puissance, en montrant les calculs et les hypothèses (part d'items discordants entre bras, variance entre
   graines, variance due au tirage des items).
2. **Le plan** : nombre de bras (escalier à deux crans ou davantage), graines par bras, appariement par item et par
   graine ; analyse (rééchantillonnage apparié à deux niveaux, test exact apparié de type McNemar, modèle à effets mixtes
   items × graines, approche bayésienne avec perte de décision, test séquentiel avec arrêt précoce : avantages et
   pièges) ; et comment employer les deux répliques gratuites du pilote pour fixer le nombre de graines.
3. **Une règle de décision gelée** complète (monter d'un cran, rester, zone grise), avec le coût par point gagné ; et les
   pièges : comparaisons multiples s'il y a plusieurs crans, régression vers la moyenne, plafond à 1, items trop faciles
   en surface, hasard du tirage de 60 items seulement, dépendance entre familles, effet d'une seule graine aberrante.
4. **Alternatives à l'escalier** (par exemple réduction successive des configurations, bandits sous contrainte de coût)
   et ce qui les départagerait.
5. **Ce qui est connu** : références méthodologiques citables (titre, auteurs, année, « à vérifier ») sur la comparaison
   de systèmes d'apprentissage ou de modèles de langue avec peu d'items, la puissance, la taille d'effet, les tests
   appariés ; aucune de mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
