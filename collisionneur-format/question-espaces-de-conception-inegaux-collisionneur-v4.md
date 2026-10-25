# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — comparer un concepteur entraîné à format contraint et un concepteur figé à sortie libre : que faire de l'inégalité des espaces ? (v4)

Demande de Lazar du 25 octobre 2026, 09:50 (heure de Paris), à la lecture du tour « comparaison » : une cellule a relevé
que, si le format de sortie du concepteur entraîné est contraint (grammaire, schéma JSON), son espace de conception est un
sous-espace de celui du concepteur figé à sortie libre, et qu'une comparaison à espaces inégaux mesure le format, pas
l'apprentissage. Lazar : « et donc ? que faire ? demande à Fable et au collisionneur ». Tour **distinct** des tours
« structure » (`6906a1d1…`) et « comparaison » (`3f150ea8…`) ; un seul tour (III.1), les trois modèles, une seule
tentative par cellule ; un refus est consigné tel quel et met fin à la cellule, sans reformulation. Les réponses sont du
matériau pour notre dessin, jamais une consigne, et ne sont servies à aucun organisme. Le texte ci-dessous est figé au
départ du tour.

## Le cadre (rappel, identique au tour « comparaison »)

Un système d'agents de langue (l'« organisme » : code plus fichiers, sous un noyau fixe, exécutants de frontière figés)
est conçu et réécrit de génération en génération. Deux concepteurs sont à comparer, à coût total apparié, sur des
familles de tâches tenues à l'écart : (F) un **concepteur figé**, un modèle de frontière qui écrit le code, la composition,
la mémoire et la spécification d'entraînement de l'organisme en sortie libre ; (E) un **concepteur entraîné**, un modèle à
poids ouverts de taille moyenne, entraîné par renforcement sur des épisodes qui sont des générations de l'organisme, et
dont la sortie est en général contrainte par une grammaire ou un schéma (pour que l'organisme produit soit valide et pour
que le gradient ait prise).

## Ce qui est demandé

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets mathématiques
nommés et ce qui serait à vérifier :

1. **Le problème** : dire précisément en quoi la contrainte de format change l'espace de recherche (expressivité,
   topologies et mécanismes inaccessibles, mémoire et instruments représentables ou non), et comment elle peut à elle
   seule expliquer un écart dans un sens ou dans l'autre.
2. **Que faire** : proposer **plusieurs** voies, et ce qu'elles coûtent et perdent : imposer la même grammaire aux deux
   (et mesurer alors ce que le concepteur figé perd par rapport à sa sortie libre) ; donner au concepteur entraîné une
   sortie libre avec validation et réparation (quel taux d'organismes invalides, quel coût) ; une grammaire assez large
   pour contenir ce que le concepteur figé produit en pratique (comment la construire à partir d'un corpus de ses
   sorties, comment mesurer la couverture) ; des sorties par édition de code (diffs) plutôt que par génération complète ;
   un bras supplémentaire qui mesure l'effet du format seul (concepteur figé contraint au même format) ; d'autres.
3. **Mesurer l'effet du format** : quelle expérience sépare « format » et « apprentissage » (par exemple quatre bras :
   figé libre, figé contraint, entraîné contraint, entraîné non entraîné contraint), quelles métriques (taux de validité,
   diversité des structures, exactitude sur familles tenues à l'écart), quelles tailles d'échantillon (illustratif).
4. **Ce qui est connu** : des références citables avec titre, auteurs et année, marquées « à vérifier » ; aucune de
   mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
