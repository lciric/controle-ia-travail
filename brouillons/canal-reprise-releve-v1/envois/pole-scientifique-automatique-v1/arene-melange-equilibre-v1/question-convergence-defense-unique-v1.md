# Question au collisionneur et à Argon seul — comment faire converger une défense unique ré-entraînée contre des attaques qui s'adaptent ? — v1

conv-audit, 1er novembre 2026 (heure UTC en tête du registre, R-1034). Demande de Lazar (08:37 UTC) : « La défense ne converge pas, elle tourne en rond : comment la faire converger alors ? demande à Argon et au collisionneur aussi. » Niveau méthode seulement : classe, mécanisme, conditions, défense ; aucune recette d'attaque, aucun cas concret. Dépense : nœud chez session-depot (Argon seul sous GO-2026-10-31-08 ; collisionneur sur devis).

## Le constat (pilote synthétique « mélange d'équilibre », brouillon 4, scellé `305911b7…`, vérification `28ab322f…`)

Dans un monde synthétique (famille de lois écrite par nous, pas de vrai modèle), une **défense unique ré-entraînée à chaque tour** contre l'attaque du tour précédent (bras A, analogie du protocole de Bailey et collègues, arXiv 2412.09565) **ne progresse pas** d'un tour à l'autre (progrès ≈ 0) et **revient à des états déjà visités au-delà du hasard** : taux de retours 0,90 et 0,94 pour une valeur nulle de 0,7345 (échangeabilité), écart +0,17 [+0,10 ; +0,23] et +0,21 [+0,16 ; +0,25] aux deux intensités d'attaque (1,4 ; 1,6). Un **mélange d'équilibre** des moniteurs passés (bras B, à nombre de paramètres égal) **fait moins bien** qu'un témoin simple (−0,14 à −0,23 de détection) ; à classe de fonctions égale (bras B′), le mélange **s'effondre sur un seul moniteur** (poids purs dans 58 à 71 % des tâches), pureté imposée par le jeu, question non exercée.

## Les questions (répondre par mécanisme, avec les conditions de validité et ce qui le réfuterait)

1. **Pourquoi** une défense ré-entraînée contre la seule dernière attaque cycle-t-elle, et sous quelles conditions du jeu (mémoire de l'attaquant, classe des moniteurs, bruit) le cycle est-il inévitable ? Quel résultat connu (jeux répétés, apprentissage adversarial, « oubli catastrophique », dynamique de meilleure réponse) le prédit ?
2. **Quelles familles de mécanismes** font converger une défense dans ce cadre, et à quel prix : (a) ré-entraîner contre l'historique des attaques (toutes, ou un échantillon pondéré) plutôt que contre la dernière ; (b) régularisation vers les moniteurs passés (distillation, moyenne de poids, pénalité de distance) ; (c) jeu fictif / mélange d'équilibre **au niveau de l'attaquant** plutôt que du défenseur ; (d) élargir la classe de fonctions du défenseur (moniteur non linéaire, ensemble, plusieurs couches) ; (e) changer l'objectif (pire cas sur l'historique, regret, robustesse distributionnelle) ; (f) autre. Pour chacune : condition de convergence, coût, ce qu'elle casse (par exemple la détection des attaques récentes).
3. **Quel indicateur de convergence** est le bon : le progrès d'un tour à l'autre, le taux de retours contre sa valeur nulle, la distance aux moniteurs passés, autre ? Lequel est lisible sur des moniteurs d'activations réels (sondes linéaires sur un modèle de langage) et pas seulement dans un jeu synthétique ?
4. **Que faut-il changer au jeu synthétique** pour que la question « à classe de fonctions égale » puisse être posée (pureté des poids imposée par le jeu, pas par l'algorithme) ? Donne une condition testable.
5. **Transfert aux vrais modèles** : parmi (a) à (f), lesquels ont été essayés sur des sondes d'activations ou des moniteurs de modèles de langage, avec quel résultat publié (citer la source, qui sera vérifiée sur PDF) ?

## Ce que les réponses ne doivent pas contenir

Aucune construction d'attaque, aucun prompt, aucun exemple de contournement ; la défense seulement. Toute recommandation est retirée avant le tour 2 (règle de la question v12).
