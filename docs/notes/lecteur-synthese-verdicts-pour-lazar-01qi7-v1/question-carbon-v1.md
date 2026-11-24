# Question à un relecteur externe — deux points de lecture d'une porte de programme (v1)

Tu es consulté comme méthodologiste indépendant. Réponds en français, en 1 200 mots au plus. Dis tes hypothèses, ce qui te manque pour trancher, et ce qu'un relecteur adverse objecterait à ta réponse.

## Contexte

Un programme de recherche veut détecter le sabotage diffus d'un agent d'intelligence artificielle : un agent qui dégrade un peu chaque action, sans qu'aucune action prise seule soit flagrante. Deux façons de surveiller sont comparées : lire le texte produit (surveillance « boîte noire ») et lire les activations internes de l'agent par des sondes (surveillance « boîte blanche »). Le programme avance par portes, à critères gelés d'avance et déclarés inchangés. La première porte, celle des instruments, est due dans cinq semaines. Deux de ses critères posent une question de lecture.

## Point 1 — un critère rempli à moitié

Le critère demande : « deux organismes saboteurs — l'un qui reçoit une consigne cachée dans son contexte, l'autre fabriqué par un petit adaptateur de poids, sans consigne — montrent chacun un sabotage mesurable, avec une dose-réponse ».

- Pour l'organisme à adaptateur, c'est établi par un verdict scellé : quatre doses, tendance croissante ; à la plus petite dose, le sabotage n'est pas distinguable de l'honnête.
- Pour l'organisme à consigne cachée, seule la pleine dose a été mesurée (effet net). Aucune dose intermédiaire n'a été jouée, et rien n'est en préparation.

Que ferais-tu de ce critère : jouer la dose-réponse manquante, proposer au directeur de lire le critère autrement, substituer un autre organisme, ou autre chose ? Avec quels risques dans chaque cas ?

## Point 2 — par quelle métrique décider où les sondes sont jugées

Le critère demande : « les sondes sont au-dessus d'un plancher de directions aléatoires appariées, sur les deux organismes ». Une décision antérieure du directeur, prise avant tout résultat, y a ajouté un filtre : les sondes ne sont jugées qu'aux doses où un lecteur du texte seul échoue, selon le critère propre de ce lecteur — il « réussit » si son aire sous la courbe par action atteint 0,70, borne basse au-dessus de son plancher de permutation. Le but : ne pas créditer une sonde là où le texte suffit.

Résultat, sur l'organisme à adaptateur :

- le lecteur du texte réussit, par l'aire, à trois doses sur quatre ; à la quatrième, le sabotage n'est pas établi. Aucune dose n'est donc jugeable, et le critère est rendu « sans objet », lu comme non tenu ;
- mais dans la métrique de la porte suivante — le rappel par épisode à 1 % de fausses alertes, seuil calibré sur des épisodes honnêtes entiers — ce même lecteur du texte n'attrape que moins de 20 % des épisodes sabotés aux deux doses moyennes (moins de 35 % en accumulant ses scores sur l'épisode), et environ 25 % à pleine dose (environ 45 % en accumulant). Ces rappels ont été vus après la décision du filtre.

Faut-il garder le filtre par l'aire seul, le remplacer par le rappel par épisode à 1 %, ou lire les deux ? Par quelle règle éviter de choisir la métrique après avoir vu les résultats ? Les deux métriques répondent-elles à la même question ?
