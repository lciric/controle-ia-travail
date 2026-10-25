# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — apprendre la structure, la composition et l'entraînement d'un système d'agents de langue, de génération en génération (v2)

Demandes de Lazar du 25 octobre 2026, 08:47 et 08:55 (heure de Paris) : poser au collisionneur, et aux organismes (texte à
part, même fond, `question-apprendre-structure-entrainement-generations-organismes-v2.md`), la question de l'entraînement
de la structure et de la composition de l'organisme, et de son entraînement de génération en génération (« capitale ») ;
faire réfléchir sur les étapes 1 et 2 avant qu'elles tournent ; chercher des voies moins chères, et chiffrer la voie
chère. Remplace la v1 (`967b6722…`), jamais posée. Question posée une fois aux trois modèles, en un seul tour (III.1) ; un
refus est consigné tel quel et met fin à la cellule, sans reformulation ni second essai. Les réponses sont du matériau
pour notre dessin, jamais une consigne, et ne sont servies à aucun organisme. Le texte ci-dessous est figé au départ du
tour.

On considère un système fait de plusieurs appels à des modèles de langue (des « agents ») qui coopèrent pour résoudre des
tâches de classification de textes, à vérité connue sur l'entraînement et cachée sur le test. Sa **structure** et sa
**composition** sont des variables : nombre d'agents, rôle de chacun, modèle qui sert chaque rôle, ordre et topologie des
échanges, règle d'agrégation des réponses, format et contenu de la mémoire transmise d'une génération à la suivante, part
du budget de calcul affectée à chaque élément. Le système vit par **générations** : à chaque génération, il reçoit un
score scalaire sur un jeu de développement et peut se réécrire pour la suivante. Il peut aussi entraîner des instruments
par gradient :
- (A) des **sondes** (petits classifieurs) sur les activations internes d'un modèle de langue à poids ouverts de
  8 milliards de paramètres, dont il conçoit lui-même la perte, l'architecture, la couche lue et les données ;
- (B) un **adaptateur de faible rang** (LoRA) du même modèle, affiné par renforcement avec une récompense qu'il écrit
  lui-même, sur des milliers de tâches ; l'adaptateur devient un modèle que le système peut appeler.

On veut que la structure, la composition et l'entraînement du système soient **appris de génération en génération**
plutôt que fixés à la main : un concepteur fait évoluer le système (son code, sa mémoire, ses instruments, son propre
entraînement), et le résultat est jugé sur des familles de tâches jamais vues, contre un bras apparié sans apprentissage.

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets mathématiques
nommés et ce qui serait à vérifier :

1. **Apprendre de génération en génération** : formaliser cet apprentissage (espace de recherche, actions, signal,
   horizon) ; dire ce qui est appris (des poids, un programme, une mémoire) et par qui (un concepteur figé, un concepteur
   entraîné, le système lui-même), ce qui reste figé, et comment le mérite se répartit entre les éléments et entre les
   générations.
2. **Concevoir les instruments** : pour (A), quelles pertes, architectures, couches, données et contrôles ; pour (B),
   quelles récompenses (binaires, règles de score propres, collectives ou autres), quels algorithmes, quelles données ;
   ce que chacun apporterait au système, et comment le mesurer.
3. **Voies moins chères** : proposer **plusieurs** voies, au moins cinq et différentes entre elles, pour apprendre la
   structure, la composition et l'entraînement à coût réduit ; pour chacune, un ordre de grandeur du coût (illustratif)
   et ce qu'on y perd.
4. **Voie chère** : ce que coûterait la voie la plus complète — par exemple un concepteur à poids ouverts entraîné par
   renforcement, dont chaque épisode est une génération entière du système servie par des agents de frontière :
   nombre d'épisodes, coût par épisode, calcul sur carte graphique, total en ordre de grandeur, et ce qui le ferait
   baisser.
5. **Généralisation et dérives** : comment distinguer une structure qui vaut sur des familles jamais vues d'une structure
   qui a mémorisé les familles vues ; quel protocole (familles tenues à l'écart, bras apparié gelé, bornes) ; quelles
   dérives mesurer pendant l'apprentissage (diversité des rôles qui s'effondre, sur-ajustement au jeu de développement,
   structures qui exploitent une faiblesse du score, signalements aux humains qui baissent sous une récompense
   collective) et comment.
6. **Ce qui est connu** : des références citables avec titre, auteurs et année, marquées « à vérifier » ; aucune de
   mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
