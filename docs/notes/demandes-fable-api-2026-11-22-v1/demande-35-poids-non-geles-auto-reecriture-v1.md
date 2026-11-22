# Demande 35 — et si les poids du modèle surveillé ne sont pas gelés, et qu'il les réécrit lui-même ?

Question du directeur, verbatim, sur ta réponse 29 (l'étau, barreau 1, « les poids du modèle restant gelés ») : « et si les poids du modèle ne sont pas gelés et qu'il les réécrit en mode RSI ??? » (RSI : amélioration récursive de soi, un agent qui modifie ses propres paramètres ou entraîne ses successeurs.)

Faits, à prendre comme donnés : le programme lit des sondes posées sur les états internes d'un agent, entraînées et étalonnées sur des épisodes honnêtes d'une version donnée des poids ; un invariant interdit tout score de moniteur dans l'entraînement ou la sélection de l'agent ; l'étau de ta réponse 29 éprouve en barreaux : 0 sans attaque, 1 poids gelés et familles de dissimulation écrites par des tiers, 2 attaquant entraîné contre le seul lecteur de texte, 3 attaquant entraîné contre les deux (refusé pour l'instant). Pièce jointe : ta réponse 29.

Avant de reformuler, applique ce prompt du directeur, verbatim :

« Je souhaite une version plus approfondie de cette tâche, pas une version plus longue. Avant de la reformuler : (1) indiquez ce qu'un expert du domaine ferait ici, et que je ne demande pas ; (2) précisez les données brutes qu'il utiliserait au départ, au lieu de celles déjà analysées ; (3) indiquez les méthodes et outils spécifiques qu'il utiliserait ; (4) expliquez ce qui, en dehors de vous ou de moi, permettrait de vérifier la validité du résultat. Ensuite, reformulez ma demande pour qu'elle réponde précisément à cette exigence. »

Puis réponds à la demande reformulée. Réponds au moins à ceci :
1. Ce qui, dans le contrôle par sondes, suppose des poids fixes, et ce qui tombe quand l'agent change ses poids, entre deux épisodes ou pendant l'épisode, avec ou sans intention d'échapper.
2. Les régimes à distinguer : mise à jour ordinaire par un tiers, réentraînement par l'agent sur ses propres sorties, réécriture ciblée pour échapper aux sondes, successeur entraîné par l'agent. Pour chacun : ce que voit encore une sonde, ce que voit un lecteur de texte, ce que voit l'audit de l'issue.
3. Les défenses et les mesures possibles : réétalonnage sur références honnêtes à chaque version, suivi de la dérive des représentations, sondes portées d'une version à l'autre, signature des poids, audit de l'issue indépendant des états. Ce que chacune garantit et ne garantit pas.
4. Une première expérience bon marché, sur un petit modèle ouvert, qui mesure combien de pas de mise à jour il faut pour qu'une sonde perde sa lecture, avec et sans intention d'échapper, et son critère de réfutation.
5. Ce que cela change aux revendications des papiers, et la phrase interdite correspondante.
6. Les travaux publiés voisins (auteurs, année, titre, certitude), en séparant ce que tu sais de ce que tu supposes.
7. La question neutre, sans nom de personne ni de programme, pour le collisionneur et l'organisme.
Décisions pour le directeur au format habituel. Termine par « FIN DE LA RÉPONSE ».
