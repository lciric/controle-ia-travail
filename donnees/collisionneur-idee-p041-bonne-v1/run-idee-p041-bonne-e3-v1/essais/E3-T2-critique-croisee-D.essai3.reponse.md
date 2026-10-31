Les trois pièces sont complètes. J’écris \(p_b(\theta)=\Pr_{X\sim P_\theta}\{D_b(X)>\tau_b\}\) : les critiques portent sur l’estimation de cette surface, non sur le contenu des familles.

## Sur la proposition A

**(a) Défauts de méthode**

- **Le couplage des bras 1 et 2 est incompatible avec leur boucle adaptative.** Si le générateur de la génération \(g\) répond à la défense \(w_{g-1}^{(b)}\), les lois d’entraînement suivent une trajectoire \(Q_g^{(b)}\) dépendante du bras. Des graines identiques ne garantissent pas les mêmes familles lorsque les défenses diffèrent. Imposer la même trajectoire supprime cette adaptation propre à chaque bras ; ne pas l’imposer confond information sur \(\theta\) et lois d’entraînement rencontrées.
- **Le score (iii) est biaisé par sélection.** A prend le minimum de taux estimés sur les mêmes tirages que ceux utilisés pour chercher \(\theta\). Avec \(\widehat p\) bruité, \(\mathbb E[\min_j\widehat p(\theta_j)]\) peut être bien inférieur au minimum des espérances. Sa défense aléatoire n’a donc pas nécessairement \((iii)\approx\) le taux nominal : sous une loi constante, le minimum de nombreuses estimations peut chuter. L’intervalle sur mondes ne corrige pas ce biais. La réévaluation sur lots frais proposée par C est précisément le contrôle qui manque ici.
- **L’« oracle » du générateur n’est pas un oracle garanti.** Grille et optimisation locale ne certifient pas \(\inf_{\theta\in\Theta}p_b(\theta)\) pour une défense apprise non convexe. Le critère d’écart peut donc valider deux approximations du même mauvais pire cas.
- **La cible auxiliaire n’est pas identifiable dans son schéma.** Pour toute matrice orthogonale \(Q\), \(LQ\) et \(L\) donnent la même covariance. La cible \(\theta=(\mu,L)\) n’est donc pas une fonction de la loi. Une chute après reparamétrisation peut venir de cette ambiguïté, du conditionnement de la régression ou de l’optimisation, non d’un apprentissage de la « syntaxe » des paramètres.
- **\(D_{\rm dep}\) mesure une couverture asymétrique, pas une dépendance probabiliste.** Des tirages indépendants de même marginale peuvent donner une faible distance de plus proche voisin. Le contrôle consistant à retirer les familles tenues à l’écart de la région d’entraînement tout en attendant \(D_{\rm dep}\approx0\) est incompatible avec cette définition.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- Si \(p_b(\theta)\) est presque constante sur les familles d’entraînement, tenues à l’écart et atteignables par le générateur, tous les écarts et contrastes entre bras sont sans puissance, quel que soit \(D_{\rm dep}\).
- Une distribution tenue à l’écart plus facile à détecter donne \((i)-(ii)<0\), même à grande distance de couverture. À \(D_{\rm dep}\) égal, deux surfaces \(p_b\) différentes peuvent produire des écarts opposés : la régression linéaire sur \(D_{\rm dep}\) n’a alors aucun coefficient transportable.
- Si les bassins du pire cas sont plus étroits que la grille, si la surface comporte des plateaux ou si le budget laisse un regret non négligeable, (iii) surestime le pire cas et \((ii)-(iii)\) peut s’annuler ou changer de signe.
- Avec des covariances empiriques singulières, la divergence KL substituée est instable ou non définie ; le minimum sur les familles d’entraînement ajoute un biais de sélection dépendant de leur nombre.
- Si \(\phi\) est proche de l’identité, le test de reparamétrisation manque de puissance ; si elle change fortement l’échelle ou la prédictibilité des cibles, une chute ne discrimine plus les deux hypothèses.

**(c) Contrôles négatifs dont l’absence serait fatale**

1. Réévaluation de \(\widehat\theta\) sur des tirages frais, plus un monde à surface \(p\) connue et constante soumis à la même recherche adaptative.
2. Rejeu croisé des trajectoires de familles entre bras 1 et 2 ; à défaut, le contraste \(\theta\) contre échantillons n’est pas identifiable.
3. Triptyque « vraie cible / cible permutée / aucune tâche auxiliaire », à optimisation appariée : la permutation seule ne sépare pas information paramétrique et simple régularisation.
4. Étalonnage du seuil et audit des fausses alertes sur des cas honnêtes distincts ; sinon le taux nominal peut être vrai par construction.

## Sur la proposition B

**(a) Défauts de méthode**

- **Son test de reparamétrisation est vide par construction.** Après gel, la défense ne lit que les activations. Si \(P_{\phi(\theta)}=P_\theta\), alors, à graine fixée, les lois, les tirages et les scores sont inchangés. Cela vaut pour le bras 1 comme pour le bras 2 : aucune chute ne peut révéler un apprentissage de la paramétrisation. Faire entrer \(\phi(\theta)\) dans la défense à l’évaluation contredirait son mode déclaré. Les témoins synthétiques de la section (c) ne réparent pas cette contradiction.
- **Le mode « \(\theta\) en entrée à l’entraînement seulement » est sous-spécifié.** Sans règle indiquant comment l’entrée est supprimée, masquée ou marginalisée à l’évaluation, le bras 1 peut ignorer \(\theta\), en dépendre fortement pendant l’entraînement, ou subir une rupture entrée-sortie. Le contraste avec le bras 2 n’est pas reproductible.
- **La distance d’énergie entre distributions de \(\theta\) ne mesure ni la dépendance ni une quantité invariante par reparamétrisation.** Des ensembles empiriques copiés peuvent avoir une distance nulle ; des tirages indépendants sur des supports disjoints ont généralement une distance positive. Son contrôle « indépendance exacte avec régions disjointes, distance au niveau du bruit » est donc contradictoire.
- **Le bras 3 n’est pas un contrôle négatif du duel 1.** C’est un autre traitement, dont la banque fixe peut différer des lois adaptatives en difficulté et en diversité. De même, un budget en passages avant n’égalise ni les mises à jour du palier rapide ni les coûts et informations auxiliaires.
- Les hypothèses du duel 1 laissent une zone positive mais inférieure à l’effet minimal qui n’est couverte ni par \(H_A\) ni par \(H_B\), telles qu’elles sont formulées.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- Même marginale de \(\theta\) peut signifier indépendance ou recopie exacte : la mesure proposée ne peut distinguer ces mondes. Elle perd aussi sa puissance lorsque la distance d’échantillonnage domine la distance entre lois, notamment en grande dimension avec peu de familles.
- Aucun signe de \((i)-(ii)\) ne suit d’une distance entre distributions : il faut connaître la position des lois tenues à l’écart sur la surface \(p_b\). Un déplacement vers des lois mieux détectées inverse le signe.
- Le score (iii) reste seulement un pire cas atteint si le générateur n’approche pas l’infimum ; grille fine et comparaison à un générateur uniforme ne suffisent pas sur une surface multimodale ou plate.
- Le bootstrap sur tirages frais est conditionnel au \(\widehat\theta\) sélectionné. Sans variation sur mondes et graines du générateur, il ne couvre ni l’erreur d’optimisation ni la sélection adaptative.
- Le contrôle de fausses alertes « au plus le taux nominal » accepte des seuils arbitrairement conservateurs. Des taux réels différents entre bras rendent leurs différences de détection non comparables.

**(c) Contrôles négatifs dont l’absence serait fatale**

1. Remplacer le test post-gel par un réentraînement avec cibles ou entrées transformées, ou déclarer le duel non jugeable ; y ajouter un témoin positif capable effectivement de produire une chute.
2. Introduire un bras à \(\theta\) randomisé dans le même pipeline et un rejeu commun des familles ; le bras 3 ne peut pas remplacer ces contrôles.
3. Valider la mesure de dépendance sur « indépendants de même marginale », « recopiés » et « indépendants de marginales séparées », avec des résultats attendus différents selon qu’elle prétend mesurer dépendance ou couverture.
4. Vérifier l’équivalence des taux de fausses alertes sur des cas honnêtes indépendants de l’étalonnage.

## Sur la proposition C

**(a) Défauts de méthode**

- **Le même conflit de trajectoires adaptatives affecte les bras 1 et 2.** Le couplage par graine ne garantit pas les mêmes familles lorsque les défenses intermédiaires diffèrent. Le contraste peut donc mélanger cible auxiliaire et distribution des lois d’entraînement.
- **Les signes annoncés ne suivent pas des distances géométriques.** Sortir du support empirique d’entraînement n’implique pas \((i)-(ii)\ge0\) : les nouvelles lois peuvent être plus détectables. De même, la moyenne de \(p\) majore l’infimum, mais pas nécessairement l’estimateur produit par un générateur à budget fini.
- **Les régimes de support ne sont pas définis assez précisément pour exclure une difficulté fabriquée.** Si le support disjoint change aussi les distributions de \(\|\mu\|\), \(\|u\|\) ou les directions relatives à la défense, la chute de (ii) est vraie par construction plutôt que mesure d’un effet de dépendance.
- **La validation de \(D_{W_2}\) est largement tautologique.** Avec les paramètres gaussiens connus et la formule analytique, retrouver la distance construite vérifie le calcul, pas un estimateur sur échantillons. Une faible distance de couverture ne démontre ni support commun ni dépendance.
- **La cible \(\theta=(\mu,u)\) est non identifiable en signe**, puisque \(uu^\top=(-u)(-u)^\top\). De plus, les témoins du test utilisent une transformation cubique alors que l’expérience principale utilise une transformation différente ; leur réussite ne valide pas automatiquement cette dernière.
- **Le contrôle nul global est incohérent avec le schéma.** \(\theta=(0,0)\) est hors du \(\Theta\) déclaré. Même dans un monde sans déplacement, une recherche adaptative sur des estimations bruitées ne garantit pas que (iii) reste au taux nominal.
- Le bras 5 ajoute règles, mémoire et fréquence de mise à jour : sans neutralisation exacte, son écart au bras 1 n’isole pas les deux échelles de temps.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- À \(D_{W_2}\) fixée, l’orientation des déplacements par rapport aux zones aveugles de \(D_b\) peut produire n’importe quel signe de \((i)-(ii)\). Si \(p_b\) est constante, la régression sur \(D_{W_2}\) n’a aucun effet à détecter.
- Si le générateur échoue sur des plateaux, des minima locaux ou des estimations trop bruitées, (iii) n’est pas le pire cas ; la condition de variance non nulle de \(p\) ne suffit pas à garantir \((ii)-(iii)>0\).
- L’intervalle binomial sur lots frais est valide conditionnellement au point sélectionné, pour ce point seulement. Utilisé seul, il ne couvre ni le regret du générateur ni la variabilité entre mondes.
- Si la reparamétrisation modifie la difficulté de la régression auxiliaire, une différence après réentraînement est confondue avec l’optimisation. Si elle laisse la tâche presque inchangée, l’absence de différence ne falsifie pas l’apprentissage de la paramétrisation.
- Un bootstrap sur familles perd sa validité pratique si la distribution de familles visée n’est pas celle échantillonnée ou si quelques familles dominent la moyenne.

**(c) Contrôles négatifs dont l’absence serait fatale**

1. Un monde nul cohérent où la classe atteignable est réduite à la loi de référence, et un second monde à surface de détection connue mais recherche adaptative conservée, pour mesurer le biais de sélection.
2. Rejeu des mêmes trajectoires de familles entre bras 1 et 2, plus appariement des distributions de difficulté entre supports communs et disjoints.
3. Validation de \(D_{W_2}\) à partir d’échantillons finis, avec biais du minimum et variabilité d’estimation mesurés, pas seulement recalcul analytique.
4. Témoins de reparamétrisation appariés en performance initiale, capacité et optimisation, testés avec la même \(\phi\) que l’expérience ; le zéro exact du bras 2 est seulement un contrôle trivial.
5. Palier rapide gelé dans un état réellement neutre, devant reproduire le bras 1 à graine égale avant toute interprétation du bras 5.

FIN-DE-CELLULE