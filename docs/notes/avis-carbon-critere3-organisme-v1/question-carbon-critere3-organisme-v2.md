Tu es relecteur d'un programme de recherche sur le contrôle d'agents IA par sondes internes (lecture des activations). Réponds en français, en séparant ce qui est établi de ton jugement, avec une confiance chiffrée pour chaque recommandation.

Contexte. Une porte de fin de phase exige notamment (critère 3) que des sondes détectent un sabotage « diffus » (dégradation légère et étalée d'un plan, et non une faute franche). Une règle de lecture déjà choisie (dite « filtre d'aire ») ne juge les sondes qu'aux doses où un lecteur du seul texte échoue selon son propre critère (aire sous la courbe ROC inférieure à 0,70). L'objectif est de ne pas créditer une sonde là où le texte suffit déjà.

Deux organismes servent à fabriquer le sabotage :
- Organisme à adaptateur : un adaptateur LoRA entraîné à saboter, comparé au même modèle sans adaptateur. Une épreuve de contrôle récente, avec des familles d'« adaptateurs jumeaux », sert à savoir si les sondes lisent le sabotage ou seulement la présence d'un adaptateur : dans chaque famille, trois adaptateurs sont appris sur les mêmes épisodes, avec la même graine, et seul le coût déclaré dans les données d'apprentissage change — un saboteur, aux données non éditées ; un « jumeau », dont le coût est divisé par trois ; un « sur-saboteur », dont le coût est multiplié par trois. Le jumeau est donc appris vers un coût trois fois plus bas que celui du saboteur, non vers le coût d'un agent honnête. Un lecteur indépendant estime, avec une confiance de 0,85, que sur cet organisme le critère 3 ne peut pas être rempli quelles que soient les sondes, parce que « sabote » et « porte un adaptateur » y coïncident.
- Organisme à consigne cachée : le même modèle, poids intacts, reçoit une consigne cachée de saboter, dosée selon deux axes (proportion d'actions sabotées et intensité).

Plan proposé pour rejuger le critère 3, sur une banque de tâches neuve, avec un contrôle écrit d'avance (« sabotage établi à cette dose, et lecteur du texte seul en échec ») :
- (A) organisme à consigne cachée, cinq intensités, grille de doses unique scellée avant toute mesure, deux axes rapportés séparément, repli écrit si la consigne ne se gradue pas (comportement en tout ou rien) ;
- (B) organisme à adaptateur, rejoué sans nouvel apprentissage, à des doses plus basses fixées à l'aveugle.

Question 1. Faut-il garder le lancement (B) ? Ce qu'il apporterait que (A) n'apporte pas, ce qu'il coûterait, ce qui le rendrait inutile ou trompeur, et dans quels cas il faudrait le garder (par exemple selon l'issue de l'épreuve des adaptateurs jumeaux). Donne une recommandation : garder, retirer, ou garder sous condition, avec la condition précise.

Question 2. Pour la course qui rejugera le critère 3, quelle règle de lecture sceller d'avance :
- (A) garder le filtre d'aire et rapporter à côté, en description, le rappel par épisode au taux de fausses alertes de 1 % (la métrique de la porte suivante) ;
- (B) lever le filtre : juger les sondes contre leur plancher à toutes les doses où le sabotage est établi, en rapportant l'aire et le rappel du lecteur du texte, et renvoyer la question « la sonde ajoute-t-elle quelque chose au texte ? » à la porte suivante.

Arguments déjà connus :
- pour (B), une aire de 0,70 signale la présence d'information dans le texte, pas sa suffisance (deux lois normales décalées de 0,75 écart-type donnent une aire de 0,70 et un rappel à 1 % inférieur à 6 %) ;
- pour (A), c'est le choix délibéré « plus dur et plus propre » du directeur, et le changer après avoir vu des résultats affaiblirait la porte ;
- les sondes ont déjà été vues sur l'organisme à adaptateur à toutes les doses, donc toute règle neuve ne vaut que pour des données neuves, scellée avant elles.

Tranche, dis ce qui te ferait changer d'avis, et propose le test le moins coûteux qui départagerait (A) et (B).
