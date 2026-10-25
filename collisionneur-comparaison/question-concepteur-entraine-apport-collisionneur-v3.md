# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — ce qu'apporterait un concepteur entraîné par renforcement, par rapport à un système déjà dessiné et à ce qui est publié (v3)

Demande de Lazar du 25 octobre 2026, 09:07 (heure de Paris) : « qu'apporterait cette conception par rapport à ce qu'on a
déjà conçu ou allons concevoir, et à ce qui a déjà été conçu dans la littérature et l'état de l'art ? — demande au
collisionneur aussi ». Tour **distinct** du tour « structure » (pièce v2, `6906a1d1…`, parti à 08:04 UTC) : un seul tour
(III.1), les trois modèles, une seule tentative par cellule ; un refus est consigné tel quel et met fin à la cellule, sans
reformulation. Les réponses sont du matériau pour notre dessin, jamais une consigne, et ne sont servies à aucun organisme.
Le texte ci-dessous est figé au départ du tour.

## Le système déjà dessiné (ce avec quoi comparer)

Un **système d'agents de langue** (l'« organisme ») résout des tâches de classification de textes à vérité connue sur
l'entraînement et cachée sur le test, sous un **noyau fixe** qui sert : des appels à des modèles de frontière **figés**
(plusieurs fournisseurs), une recherche documentaire, un budget borné par génération (appels, dollars, temps), et un
score scalaire par génération sur un jeu de développement. L'organisme est **son code et ses fichiers** ; à chaque
génération, il peut réécrire son code, sa composition (rôles, modèles servis, échanges, agrégation), sa mémoire ; la
génération suivante repart de ce qu'il a écrit. Il peut aussi faire entraîner par le noyau, sur un modèle à poids ouverts
de 8 milliards de paramètres : (A) des **sondes** sur les activations, dont il conçoit la perte, l'architecture, la couche
et les données ; (B) plus tard, un **adaptateur de faible rang** affiné par renforcement avec une récompense qu'il écrit,
qu'il peut ensuite appeler. L'apprentissage de la structure est donc une **recherche guidée par le score, à cerveaux
figés** : rien, dans des poids, n'apprend à concevoir ; ce qui est appris vit dans les fichiers de la lignée et dans les
instruments (A) et (B). Le jugement : exactitude sur un test caché, **familles de tâches tenues à l'écart**, bras
**apparié sans apprentissage** (même organisme de départ, même mémoire, même budget), et mesure des dérives (diversité
des rôles, sur-ajustement au jeu de développement, signalement aux humains qui baisse).

## La conception à évaluer

Un **concepteur** à poids ouverts (taille moyenne), **entraîné par renforcement**, dont la politique produit, à chaque
génération, la structure, la composition, la mémoire et la spécification d'entraînement de l'organisme ; **un épisode est
une génération entière** de l'organisme, servie par les modèles de frontière figés ; la récompense est le score de
l'organisme ainsi conçu (sur des tâches d'entraînement, jamais le test) ; le concepteur apprend à travers des milliers
d'épisodes et de familles de tâches.

## Ce qui est demandé

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets mathématiques
nommés et ce qui serait à vérifier :

1. **Apport par rapport au système déjà dessiné** : ce que cette conception ajouterait, en termes de ce qui est appris et
   de ce qui se transfère (entre lignées, entre familles de tâches, entre runs), de qualité de conception, de coût à
   l'usage, de ce que l'on peut mesurer à l'intérieur du concepteur ; et ce qu'elle perdrait ou risquerait (dépendance à
   des milliers d'épisodes, exploitation d'une faiblesse du score, effondrement de la diversité, signalement qui baisse) ;
   dans quels cas elle ne vaudrait **pas** la peine.
2. **Apport par rapport à ce qui est publié** : situer cette conception par rapport aux familles de travaux connus —
   méta-agents à modèle figé qui écrivent des agents en code et les archivent ; systèmes qui réécrivent leur propre code
   avec un modèle figé ; modèles de taille moyenne entraînés par renforcement à concevoir des flux de travail ou des
   systèmes d'agents pour des exécuteurs plus forts ; organisations d'agents entraînées conjointement par une récompense
   collective ; modèles figés qui écrivent des fonctions de récompense ; méta-apprentissage et apprentissage de
   l'architecture — en disant, pour chaque famille, ce que la conception évaluée a de commun et ce qu'elle aurait de
   nouveau, et ce qui, de ce « nouveau », demanderait vérification.
3. **Ce qui départagerait** : quelle expérience, à quel coût (illustratif), montrerait que le concepteur entraîné bat la
   recherche à cerveaux figés, ou l'inverse ; quels témoins et quelles bornes.
4. **Ce qui est connu** : des références citables avec titre, auteurs et année, marquées « à vérifier » ; aucune de
   mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune conclusion comme « la » réponse — donner les deux lectures et ce qui les départagerait.
