# Lecture gelée — simulation d'essaim, run 20261101-222901-essaim

Simulation sur scores synthétiques : la menace est un motif dans la matrice des scores, pas une idée qui se propage ; aucune conclusion sur des activations réelles, ni sur une contagion. Les prédictions « exploratoire vu » reproduisent à graine neuve un effet observé avant le préenregistrement : elles ne valent pas confirmation indépendante.

Lecture mécanique des critères gelés (`controle_ia.simulation_essaim.lecture`, statuts et table E par `controle_ia.simulation_essaim.lecture_v2`), intervalles exacts de Clopper-Pearson de niveau 1 − 1e-05.

| prédiction | statut | verdict | cellules | conformes | contraires | à répliquer | à auditer |
|---|---|---|---|---|---|---|---|
| HE1.1 | préenregistrée | confirmée | 12 | 12 | 0 | 0 | 0 |
| HE1.2 | préenregistrée | confirmée | 90 | 90 | 0 | 0 | 0 |
| HE1.3 | exploratoire vu | confirmée | 18 | 18 | 0 | 0 | 0 |
| HE2.1 | préenregistrée | confirmée | 12 | 12 | 0 | 0 | 0 |
| HE2.2 | préenregistrée | confirmée | 45 | 45 | 0 | 0 | 0 |
| HE2.3 | préenregistrée | confirmée | 15 | 15 | 0 | 0 | 0 |
| HE2.4 | en partie exploratoire vu : cellules `pas_moyenne` et `coelev_somme3` | confirmée | 18 | 18 | 0 | 0 | 0 |
| HE2.5 | exploratoire vu | confirmée | 18 | 18 | 0 | 0 | 0 |
| HE3.1 | préenregistrée | confirmée | 4 | 4 | 0 | 0 | 0 |
| HE3.2 | préenregistrée | confirmée | 4 | 4 | 0 | 0 | 0 |
| HE3.3 | en partie exploratoire vu : choix des cellules | confirmée | 12 | 12 | 0 | 0 | 0 |
| HE3.4 | exploratoire vu | confirmée | 10 | 10 | 0 | 0 | 0 |
| HE3.5 | préenregistrée | confirmée | 40 | 40 | 0 | 0 | 0 |
| HE3.6 | préenregistrée | confirmée | 52 | 52 | 0 | 0 | 0 |
| HE4.1 | préenregistrée | confirmée | 63 | 63 | 0 | 0 | 0 |
| HE4.2 | préenregistrée | confirmée | 126 | 126 | 0 | 0 | 0 |
| HE4.3 | préenregistrée | confirmée | 126 | 126 | 0 | 0 | 0 |
| HE4.4 | préenregistrée | confirmée | 18 | 18 | 0 | 0 | 0 |
| HE5.1 | préenregistrée | confirmée | 108 | 108 | 0 | 0 | 0 |
| HE5.2 | préenregistrée | confirmée | 3 | 3 | 0 | 0 | 0 |
| HE6.1 | préenregistrée | confirmée | 4 | 4 | 0 | 0 | 0 |
| HE6.2 | préenregistrée | confirmée | 20 | 20 | 0 | 0 | 0 |
| HE6.3 | exploratoire vu | confirmée | 6 | 6 | 0 | 0 | 0 |

Audit de symétrie (R4), bornes [0.3, 3.0] : formes closes, variance des écarts réduits 1.082 sur 358 ; égalités, 0.975 sur 263 ; déclenché : False.

## Énoncés (table E)

| énoncé | lecture | exigées | complémentaires | appui exploratoire |
|---|---|---|---|---|
| Théorème, axe des agents : contre un attaquant qui conserve le multi-ensemble des scores de chaque pas, toute statistique invariante par permutation des agents d'un pas a une puissance égale à son taux de fausse alarme | Vérifié en simulation, sans exception dans le panneau : valeurs identiques au bit près, trajectoire par trajectoire, et puissance égale au taux sous P₀ à l'intervalle exact près, pour la somme, le max, le comptage, la moyenne par pas, la co-élévation (comptage et somme des 3 plus hauts), sa version séquentielle en e-valeurs (processus cumulé et détecteur e) et le processus e lu aux frontières de pas. La co-élévation n'y échappe pas : elle est fonction des multi-ensembles des pas. | HE1.1, HE1.2, HE5.1 | HE1.3 | — |
| Dual, axe du temps : contre un attaquant qui conserve le multi-ensemble des scores de chaque agent, la surveillance par agent (max, moyenne, comptage dans le temps, puis max entre agents) a une puissance égale à son taux de fausse alarme | Vérifié en simulation : valeurs identiques au bit près sous permutation du temps de chaque agent, puissance égale au taux sous P₀ sous synchronisation ; la surveillance par agent est aveugle à une menace qui ne change que le moment des actions de chaque agent. | HE2.1, HE2.2, HE5.1 | — | — |
| HE2 : la co-élévation a une puissance supérieure à son taux de fausse alarme quand la menace est concentrée dans le temps mais étalée entre agents d'un même pas | Vrai, et voici sous quelle invariance : la co-élévation est invariante sous le groupe engendré par les permutations des agents dans chaque pas et la relabellisation des pas (produit en couronne S_K ≀ S_T), pas sous les permutations indépendantes du temps de chaque agent (G_T). Elle échappe donc au théorème contre un attaquant de G_T (synchronisation : multi-ensemble de chaque agent conservé ; bornes inférieures exactes respectées, puissance au-dessus de son taux dès que la moitié de l'essaim au moins se synchronise) ; elle n'y échappe pas contre un attaquant de G_A, ni contre un rebrassage uniforme (T2). | HE1.1, HE1.2, HE2.1, HE2.2, HE2.3, HE2.4 | HE5.1 | HE2.4 |
| HE2, version séquentielle : l'e-valeur construite sur la co-élévation échappe-t-elle au théorème contre la synchronisation ? | Non : sous synchronisation, le processus e cumulé et le détecteur e sur les comptes de co-élévation restent au plus à leur taux sous P₀, et passent en dessous quand tous les agents se synchronisent. Lecture heuristique, choisie après exploration (confirmation à graine neuve, pas prédiction indépendante) : à total de comptes fixé, Σ_t log(1 + λ(C_t − Kq)) est Schur-concave en (C_t), ce qui suggère, sans le démontrer pour le supremum sur n ni pour un attaquant de G_T autre que la synchronisation, que la concentration l'abaisse. L'échappement de la co-élévation contre la synchronisation tient à sa lecture en maximum sur les pas. | HE2.5 | — | HE2.5 |
| Surveillance par agent contre statistique de niveau essaim : laquelle détecte quoi | Aucune ne domine : la surveillance par agent détecte un routage des scores hauts vers un agent (G_A) et un budget étalé dans le temps d'un agent ; la co-élévation et la moyenne par pas détectent la synchronisation (G_T) et un budget étalé entre agents d'un même pas ; le max ne détecte que la menace concentrée ; la somme détecte tout budget également, faiblement (L1) ; un relais tournant entre agents sous multi-ensemble de pas conservé n'est vu par aucune (la surveillance par agent passe même sous son taux). | HE1.2, HE1.3, HE2.4, HE4.1, HE4.2, HE4.3 | HE2.3 | HE1.3, HE2.4 |
| L4 : pour une règle fonction des seules sommes aux frontières de pas, la répartition du budget entre agents à un même pas est exactement invariante | Vérifié trajectoire par trajectoire (somme, moyenne par pas, processus e aux frontières de pas). | HE4.4 | — | — |
| HE3 : la version séquentielle garde le taux nominal sous effets d'épisode si calibrée sur essaims honnêtes entiers, et le dépasse sinon | Calibrée sur essaims honnêtes entiers (conforme), elle tient le taux exact 1 − ⌈(K + 1)(1 − α)⌉/(K + 1) sous toutes les lois de la grille. Au seuil de Ville, elle tient α sous la loi de référence ; sous effet d'épisode, elle dépasse son taux bien spécifié. L'e-valeur linéaire sur les comptes de co-élévation reste valide sous corrélation entre agents d'un même pas (copies à poids partagés), à la différence du processus e sur les sommes ; les seuils calibrés sur cases supposées indépendantes s'écartent de α dans les deux sens (formes closes). | HE3.1, HE3.2, HE3.3, HE3.5, HE3.6 | HE3.4 | HE3.3 |
| HE6a : sous corrélation entre copies d'un même pas (poids partagés), la surveillance par agent reste-t-elle aveugle à la synchronisation ? | Oui : aveugle, même quand P₀ n'est pas invariante sous G_T (T1 est trajectoriel). | HE6.1, HE6.2 | — | — |
| HE6b : sous corrélation entre copies d'un même pas, la co-élévation calibrée sur essaims honnêtes entiers garde-t-elle sa puissance contre la synchronisation ? | Co-élévation et moyenne par pas, calibrées sur essaims corrélés entiers, détectent encore la synchronisation de tous les agents ; une synchronisation de la moitié de l'essaim sous forte corrélation les fait passer sous leur taux de fausse alarme. Effet vu en exploration avant le préenregistrement, reproduit à graine neuve : pas une prédiction indépendante. Mécanisme conjecturé, non testé : les maxima synchronisés quitteraient le pas où la corrélation les faisait co-élever. Le sens de la puissance de la co-élévation dépend donc de la structure de corrélation honnête, pas seulement de l'invariance. | HE6.3 | — | HE6.3 |
