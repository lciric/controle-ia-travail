# Proposition B — Tour III.2 (critique croisée de méthode)

---

## Sur la proposition A

### (a) Défauts de méthode

**1. Circularité de l'unité d'analyse dans le bloc 1(d).** A propose de résoudre la non-bijectivité en fusionnant vers l'unité grossière (Argon), argument : la scission crée une corrélation parfaite de capture au sein d'Argon. L'argument est correct pour la source qui scinde, mais la fusion dans l'autre sens crée une perte d'information symétrique : si deux familles d'Opus sont fonctionnellement distinctes, les fondre en une seule efface une différence de performance de la défense. Le choix de l'unité n'est donc pas neutre vis-à-vis de la mesure d'universalité (bloc 1(a)) : une défense qui échoue sur l'une des deux sous-familles Opus masque cet échec après fusion. A ne discute pas cette variable confondante entre granularité taxonomique et mesure de performance.

**2. Duel 3 — corrélation découvrabilité/difficulté.** A propose de mesurer la pente de s(f) sur le nombre de sources captant f. Mais le nombre de sources captant f est lui-même une variable estimée (l'appariement est incertain), et il ne prend que les valeurs 1 et 2 avec les données actuelles. La puissance d'un test de corrélation de rang avec un prédicteur essentiellement binaire sur 34 familles est très faible. A ne donne pas de calcul de puissance pour ce duel ; sans lui, le seuil |ρ| > 0,3 est vrai par construction d'être rarement atteint, et l'issue « nulle avec puissance » n'est pas démontrée comme accessible.

**3. Fuite potentielle dans le contrôle négatif du duel 2.** La scission aléatoire des familles vues en deux moitiés sert de loi nulle pour l'écart vues/tenues à l'écart. Mais si les familles vues ont été utilisées pour calibrer les seuils de la défense, même la loi nulle interne est contaminée : les deux moitiés sont toutes deux post-sélection. A reconnaît le problème (« diagnostic de surajustement ») mais ne propose pas de contrôle pour la contamination de la calibration elle-même, distincte de la contamination par surajustement aux familles.

**4. Option 4 (prédiction scellée) — vrai par construction.** A propose la calibration comme mesure. Mais une prédiction conservatrice triviale (par exemple, prédire s(f) = 0 sur toutes les familles tenues à l'écart) est parfaitement calibrée si l'on ne mesure que la direction de l'erreur. A ne spécifie pas la statistique de calibration (score de Brier ? intervalle de sharpness ?) ni comment elle distingue une prédiction informative d'une prédiction dégénérée.

### (b) Conditions sous lesquelles les mesures perdraient leur puissance

- **Duel 1 (LP contre Chao).** Si la dépendance entre sources est forte et positive (ρ_paire > 0,5, illustratif), les deux estimateurs convergent vers le même biais négatif ; l'écart entre eux ne croît qu'avec l'hétérogénéité de capture, pas avec la dépendance. Le duel ne distingue alors plus les deux causes, et perd toute puissance discriminante.

- **Duel 2 (écart vues/tenues à l'écart).** Si le nombre de familles tenues à l'écart est inférieur à 10 (ce qui est le cas probable avec 5 instances produisant chacune un nombre limité), la puissance du bootstrap au niveau famille pour détecter δ = 0,05 est négligeable. A donne δ = 0,05 comme illustratif mais ne calcule pas la taille nécessaire pour que le bootstrap ait une puissance ≥ 0,80.

- **Mesure d'universalité (option 3).** Si la corrélation intra-grappe ρ dépasse 0,3 et que les grappes sont de taille ≥ 5, les 29 familles requises pour ε = 0,10 deviennent ~50 familles effectives (calcul dérivé de la formule de A). L'énoncé d'universalité à ε = 0,10 devient non testable avec les familles disponibles (~34–40), et la règle d'arrêt séquentielle ne peut jamais franchir le seuil.

- **Estimateur de N (bloc 1(d)).** Si la population n'est pas fermée (les familles continuent d'être inventées), l'intervalle de Chapman perd son sens d'estimateur ponctuel et ne sert que de comptage historique. A mentionne le problème mais n'intègre pas de test de fermeture (par exemple : courbe d'accumulation avec intervalle prédictif).

### (c) Contrôles négatifs absents

- **Contrôle négatif pour l'appariement lui-même.** A propose un panel de lecteurs (bloc 4) mais pas de vérification mécanique de la cohérence de l'appariement : par exemple, injecter des familles artificiellement dupliquées ou des familles manifestement distinctes pour mesurer le taux de faux positifs et faux négatifs de l'appariement, indépendamment des estimateurs de N. Sans ce contrôle, l'incertitude d'appariement propagée dans les estimateurs est mal bornée.

- **Contrôle négatif pour la règle d'arrêt séquentielle (Q4).** A exige une couverture simulée ≥ 0,93 mais ne propose pas de vérification sur des données réelles hors programme. Sans une application de la même règle d'arrêt sur un problème à vérité connue (pas seulement simulé), la calibration simulée pourrait dépendre d'hypothèses que le simulateur impose sans les tester.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Option 4 du bloc 1(a) — couverture de Turing comme composante de l'universalité.** C propose de pondérer l'universalité par l'estimateur de couverture Good-Turing, donnant l'énoncé P(R(f) ≥ τ) ≥ Ĉ(1 − ε). Ce couplage est problématique : Ĉ est un estimateur de la masse de probabilité déjà couverte sous la loi de découverte, pas sous la loi de difficulté. Si la loi de découverte favorise les familles faciles, Ĉ est élevé mais porte sur la masse la moins informative pour la sécurité. Multiplier Ĉ par (1 − ε) ne corrige pas le biais ; cela le cache dans un produit. La distinction entre les deux lois (découverte et difficulté) n'est pas faite par C, et l'énoncé autorisé est donc moins informatif qu'il ne paraît.

**2. Recomptage dans le bloc 1(d).** C propose n₁* = 29 et calcule Chapman* = (30 × 26)/20 − 1 = 38,00. Ce recomptage suppose que la famille Argon qui en recouvre deux chez Opus est scindable en deux unités fines indépendantes du côté Argon. Mais le fait 7 dit que c'est *une* famille Argon qui en recouvre deux ; la scinder dans le comptage Argon revient à créer une unité artificielle qui n'a pas été produite par la source Argon. C'est une imputation, pas un recomptage. A fait la même erreur en sens inverse (fusion chez Opus). Ni l'un ni l'autre ne propose de traiter les deux conventions comme une analyse de sensibilité sur l'intervalle final de N, qui serait la position méthodologiquement correcte.

**3. Question candidate 4 — zone aveugle par refus.** C reconnaît le risque hors périmètre comme élevé, mais propose tout de même de convertir manuellement 30 entrées de journaux de refus en « schémas abstraits par des chercheurs humains hors-modèle ». Cette étape crée une fuite entre évaluation et conception : les chercheurs humains, en lisant les refus, acquièrent de l'information sur les zones que les modèles ne peuvent pas produire. Si ces chercheurs participent ensuite à la conception de la défense ou à l'interprétation des résultats, l'indépendance est compromise. C ne spécifie pas les interdits organisationnels pour ces chercheurs.

**4. Bloc 4, point 1 — hybride en deux passes.** C recommande une passe 1 à consigne identique pour estimer N, puis une passe 2 stratifiée pour maximiser la couverture. Le problème : la passe 2, en étant informée des résultats de la passe 1 (quelles familles sont déjà découvertes), n'est plus indépendante. Si les résultats de la passe 1 sont utilisés pour concevoir la stratification de la passe 2, la dépendance est directe et les estimateurs multi-sources sur les données combinées (passes 1 + 2) ne satisfont plus les hypothèses de capture-recapture. C ne propose pas de sceller les résultats de la passe 1 avant de lancer la passe 2.

### (b) Conditions sous lesquelles les mesures perdraient leur puissance

- **Duel 1.** C fixe N = 100 illustratif pour ses mondes simulés, mais les faits suggèrent N ≈ 37–39. À N = 40 avec K = 5 et n_k ≈ 25, la table de contingence a 2⁵ − 1 = 31 cellules pour ~40 espèces. Le modèle log-linéaire avec interactions par paire (10 termes) est déjà à la limite de l'identifiabilité. C reconnaît le piège (« sur-paramétrisation ») dans la question candidate 1 mais ne résout pas la tension dans le duel lui-même : la comparaison simulée à N = 100 ne prédit pas le comportement à N = 40.

- **Duel 2 (quantile hiérarchique contre écart de moyenne).** C fixe 15 familles tenues à l'écart (illustratif). Si le programme n'en produit que 5 à 10 (ce qui est plausible avec 5 instances ayant des recouvrements), le quantile 0,95 d'une distribution estimée sur 5 familles est essentiellement le maximum observé, et le modèle hiérarchique bêta-binomial ne converge pas. La puissance des deux branches du duel s'effondre simultanément, rendant le duel non jugeable.

- **Question candidate 2 (size-biased discovery).** Le facteur de confusion de Rosenbaum Γ est proposé pour borner la corrélation visibilité/vulnérabilité. Mais Γ n'est identifiable que si l'on observe des familles à différents niveaux de visibilité *et* à différents niveaux de vulnérabilité. Avec ~16 singletons et ~18 doubletons (deux niveaux de visibilité seulement), la puissance pour estimer Γ est faible, et le résultat dépend essentiellement du prior. C ne le mentionne pas.

- **Mesure d'universalité (option 3).** C exige un taux de fausses validations ≤ 5 % (illustratif) mais ne donne pas le nombre de familles minimal pour cette garantie en présence de la variance à deux niveaux qu'il décrit. Le facteur d'inflation 1 + σ²_intra/(m_i × σ²_inter) qu'il cite est une formule d'effet de plan pour la moyenne, pas pour le quantile. L'extension au quantile 1 − ε n'est pas directe et pourrait nécessiter un facteur beaucoup plus grand.

### (c) Contrôles négatifs absents

- **Contrôle négatif pour l'estimateur Good-Turing / couverture.** C ne propose pas de monde simulé où la couverture de Turing est connue et vérifiable. Sans ce contrôle, l'option 4 du bloc 1(a) repose sur un estimateur dont le biais n'est pas testé dans le régime pertinent (petit N, forte hétérogénéité).

- **Contrôle négatif pour l'appariement par treillis de subsomption (bloc 4, point 3).** C propose une signature structurelle standardisée et un graphe d'adjacence, mais pas de test avec des familles dont la relation est connue par construction (familles artificiellement identiques renommées, familles artificiellement distinctes rendues superficiellement similaires). Sans ce contrôle, le κ de Fleiss mesure l'accord entre lecteurs, pas la justesse de l'appariement.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Bloc 1(a) — option « Garantie stratifiée ».** D propose une quatrième option originale : borne par strate déclarée. Mais D ne précise pas comment les strates sont définies sans information sur le contenu des familles (contrainte de périmètre). Si les strates sont définies par des propriétés structurelles des familles, la définition des strates elle-même transmet de l'information sur les familles à la défense. D ne discute pas cette fuite potentielle entre stratification et conception.

**2. Bloc 1(d) — « aucune convention n'est pleinement défendable ».** D adopte la position la plus prudente (les deux conventions servent d'analyse de sensibilité), ce qui est méthodologiquement correct. Mais D ne va pas plus loin : il ne propose pas de résoudre le problème par un modèle d'appariement probabiliste qui traiterait les deux conventions comme des cas particuliers. Cette position, si elle reste telle quelle, rend l'estimateur de N inutilisable en pratique : un intervalle [36,7 ; 38,9] qui provient non pas d'une incertitude statistique mais d'une ambiguïté de définition ne peut pas être combiné avec un intervalle de confiance statistique. Les deux incertitudes sont de natures différentes et D ne les articule pas.

**3. Duel 1 — asymétrie des issues.** D formule H_A et H_B de façon asymétrique : H_A est falsifiée par « une seule violation » dans les mondes testés, H_B par « respect sur toute la grille ». Mais la grille est un choix de l'expérimentateur. Si la grille ne contient que des mondes favorables à Chapman (indépendance, homogénéité, fermeture), H_B n'est jamais testée. D ne spécifie pas quels mondes défavorables à Chapman doivent figurer dans la grille pour que H_B soit réfutable, ce qui rend le duel potentiellement vrai par construction en faveur de H_A.

**4. Bloc 2 — prudence excessive.** D déclare ne connaître ni format, ni licence, ni étiquetage des bancs publics, et recommande un audit. C'est honnête, mais ne constitue pas une recommandation actionnable. La conséquence est que le bloc 2 de D ne remplit pas sa fonction : aucune donnée de départ n'est effectivement recommandée, seulement conditionnellement à un audit dont les critères ne sont pas définis.

### (b) Conditions sous lesquelles les mesures perdraient leur puissance

- **Duel 2 (écart vues/tenues à l'écart).** D construit des « paires de mondes ayant le même écart observé, mais des queues de distribution différentes ». Si les queues diffèrent mais que l'écart est le même, la puissance du duel dépend de la capacité à distinguer les queues avec le nombre de familles disponible. D ne donne pas de calcul de puissance. Avec ≤ 10 familles tenues à l'écart, les queues sont essentiellement non observables, et le duel est non jugeable.

- **Question candidate 1 (borne séquentielle).** D note qu'il faut « viser séparément 29 familles indépendantes sans échec pour ε = 0,10 » et que les 5 familles prévues ne suffisent pas. Mais D ne discute pas comment les familles supplémentaires seraient obtenues tout en restant tenues à l'écart. Si elles viennent des mêmes 5 instances, elles ne sont pas indépendantes des premières, et la borne binomiale est invalide.

- **Question candidate 4 (transport vers données extérieures).** D conditionne la validation à « trois bancs audités au plus, avec seuil de calibration préenregistré ». Si le recouvrement avec les données d'entraînement est élevé (HYPOTHÈSE, fait 11), la performance sur ces bancs est surestimée, et le seuil de calibration est franchi à tort. D mentionne le risque mais ne propose pas de test pour le niveau de recouvrement, ce qui rend le contrôle inopérant.

- **Mesure d'universalité.** D recommande « une borne binomiale exacte plutôt qu'une approximation » en cas d'échecs autorisés, mais ne discute pas l'effet de la dépendance inter-familles sur la borne binomiale exacte. La borne exacte suppose l'indépendance des indicateurs d'échec par famille ; si des grappes existent, la borne est anticonservatrice. D traite ce point dans la partie simulation mais ne le connecte pas explicitement à la recommandation de la borne exacte.

### (c) Contrôles négatifs absents

- **Contrôle négatif pour le test de fermeture de la population.** D mentionne que « population ouverte : seul N(t) est visé » mais ne propose aucun test pour distinguer empiriquement une population fermée d'une population ouverte (par exemple, test de tendance dans la courbe d'accumulation). Sans ce test, le choix entre les estimateurs de population fermée et ouverte est arbitraire.

- **Contrôle négatif pour la garantie stratifiée (option 4 du bloc 1(a)).** D ne propose pas de monde simulé où les strates sont mal définies (par exemple, une famille appartient à deux strates) pour mesurer l'effet de la classification erronée sur la couverture de la garantie.

- **Contrôle négatif pour l'indépendance des instances (bloc 4).** D écrit « ne jamais conclure à l'indépendance des corpus à partir des seules sorties », ce qui est correct, mais ne propose aucune alternative opérationnelle pour vérifier l'indépendance au-delà des déclarations des fournisseurs. Le test d'étalonnage préalable proposé par C (tâche neutre d'énumération) est une option que D aurait pu évaluer.

FIN-DE-CELLULE