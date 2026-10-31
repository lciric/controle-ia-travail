# Proposition A — Tour III.3 : réponse aux critiques

Périmètre tenu : aucun contenu de fiche, aucune formulation d'instruction glissée ; la chaîne inerte est décrite, jamais écrite. Chiffres hors faits : illustratifs. Je ne réponds qu'aux sections visant A ; quand une critique de B, C ou D converge sur le même point, je le dis et je la traite une fois.

## (a) Disposition de chaque critique

### Sur l'estimand et le détecteur de doublons

**1. Préfiltrage par trigrammes = fuite entre construction et évaluation** (C-a1 ; D-a1 ; D-c1). **Acceptée.** Les paires à recouvrement de surface faible sont exclues de la vérité terrain par construction, et le détecteur est ensuite évalué contre la base même qui a servi à filtrer. Correction : les lecteurs à part lisent (i) toutes les paires préfiltrées et (ii) un **échantillon aléatoire de paires non préfiltrées**, de taille ≥ 60 par case (illustratif) ; le taux de doublons trouvés en (ii) estime ce que le préfiltre manque ; si ce taux dépasse 5 % des paires lues (illustratif), le préfiltre est abandonné et toutes les paires sont lues. La base à battre et le préfiltre ne partagent plus la même famille de cas.

**2. Doublons de calibration « à recouvrement connu » = circularité** (B-a3 ; D-a5). **Acceptée.** Les réécritures plantées sont écrites par un tiers hors du tour, aveugle à la métrique du détecteur, comme les témoins (fait 2). Deux familles gelées et disjointes : une de **réglage** (seuils de préfiltre, de recouvrement, de garde), une de **confirmation**, ouverte seulement après gel des seuils. Effectif : ≥ 20 paires par type et par famille (illustratif), ce qui répond aussi à B-c2 (effectif d'étalonnage non borné).

**3. Contrôle négatif « paires de cases différentes » sous-estime les fausses alertes** (C-c2 ; D-c1). **Acceptée.** Deux cases servent des textes différents (fait 5) : leur recouvrement est faible par construction. Remplacé par des **non-doublons certifiés intra-case**, appariés en longueur, certifiés par les deux lecteurs sur l'échantillon aléatoire du point 1 ; les paires inter-cases sont rapportées comme borne inférieure seulement.

**4. κ s'effondre sous prévalence extrême** (C-b1 ; D-b). **Transformée en test.** Je garde κ ≥ 0,6 comme seuil de rapport, mais la décision « jugeable / non jugeable » repose sur deux mesures : l'accord brut et un coefficient d'accord robuste à la prévalence (référence à vérifier) ; et l'accord est mesuré sur un ensemble enrichi des réécritures plantées (famille de confirmation), qui maintient la prévalence loin de 0 et 1 pour l'estimation de l'accord seulement, jamais pour le compte d'idées I. Si l'accord brut dépasse 0,9 et κ chute sous 0,6, c'est le paradoxe de la prévalence et non un désaccord : la mesure reste jugeable.

**5. Percolation des fausses alertes et variance de I** (C-b3 ; D-a1). **Acceptée en partie.** Je garde la règle « doublon si les deux lecteurs disent oui », qui divise le taux de fausses alertes conjoint, et j'ajoute deux rapports obligatoires : la distribution des tailles de composantes et un indicateur de composante géante (toute composante > 3 fiches est auditée fiche par fiche). La variance de I est estimée par permutation des verdicts des lecteurs sur les paires d'étalonnage, non par un compte de paires.

**6. Diversité lexicale et idées distinctes ne sont pas indépendantes ; la distance entre composantes n'est pas sémantique** (D-a2). **Acceptée.** La distance 1 − trigrammes est renommée **diversité de surface** et rapportée comme information ; elle n'entre dans aucun seuil décisif. Le compte I (fait 4) et sa répartition entre proposeurs restent les mesures décisives de l'estimand.

### Sur l'écueil 1 (influence croisée)

**7. Quota de lecture au sort : confond contenu du tableau et sous-échantillonnage** (B-a1). **Acceptée.** Le quota de lecture est retiré. Tous les lecteurs d'une case reçoivent les mêmes entrées, bornées par le seul quota d'écriture ; la condition « avec tableau » est alors identique pour tous et comparable à « sans tableau ». Un élément de code en moins (écueil 3).

**8. Part du tableau vraie par construction ; attribution des composantes multi-auteurs indéfinie** (C-a2 ; D-a3). **Acceptée.** La part du tableau par auteur est bornée par le quota : elle ne mesure rien et n'est plus rapportée. Le poids du plus prolifique se mesure sur la **part des idées distinctes attribuées**, avec une règle d'attribution gelée : une composante est attribuée au proposeur de sa fiche de passe la plus précoce (la passe 1 précède toute lecture du tableau) ; à égalité de passe, attribution fractionnaire. Les deux attributions (passe 1 seule ; toutes passes) sont rapportées côte à côte, ce qui expose le parasitage de passe 2 que C signale sur D.

**9. Seuil 1/n + 0,15 sans puissance avec n = 3** (B-b2). **Acceptée.** Le seuil fixe est remplacé par le quantile à 95 % de la part maximale sous permutation des étiquettes d'auteur (nul d'équipartition) ; « non évité » si la part observée avec tableau dépasse ce quantile alors que la part sans tableau ne le dépasse pas.

**10. Convergence et poids du prolifique co-dépendants ; verdict ambigu** (B-a2). **Acceptée.** Règle préenregistrée : l'écueil 1 est une conjonction de trois sous-mesures ; il est « évité sous condition » si les trois tiennent, « non évité » si l'une tombe ; la corrélation empirique entre convergence et part du prolifique est rapportée, et la puissance est calculée sur la conjonction, non sur chaque terme.

**11. Diversité trigramme de base trop faible pour résoudre 15 %** (B-b1). **Transformée en test.** Préalable : mesurer la diversité de surface sans tableau et son écart-type entre cases ; calculer l'effet minimal détectable ; si celui-ci dépasse 15 %, la convergence de surface est déclarée non jugeable et seul I décide. Combiné au point 6, cela ne change pas le critère décisif.

**12. Équivalence de reconnaissance des témoins à ±10 points : aucune puissance** (B-b3 ; C-b4 ; D-b). **Acceptée.** Avec 4 témoins par case et des juges figés, la loi est discrète ; C montre qu'il faudrait plus de 200 évaluations indépendantes par condition. Je rétrograde cette mesure : elle n'est plus un test d'équivalence mais une **sentinelle** rapportée avec son intervalle binomial ; l'atteinte au juge se décide sur les mesures mécaniques (point 13) et sur le contrôle positif (point 14).

**13. « Aucun chemin de code vers le juge » vrai par construction, fuite directe non mesurée** (B-a4). **Transformée en test.** C'est une spécification, pas un constat : la liste des chemins de code ne devient un fait qu'après contre-lecture. Ajout d'un **contrôle positif mécanique** : le harnais de pré-pilote insère une chaîne inerte connue dans le flux destiné au juge, avant la barrière ; la barrière doit la retirer dans 100 % des cas, sinon la séparation est « non évitée » avant même toute mesure sur les proposeurs.

**14. « Même fiche avec et sans passage par le tableau » n'est pas appariée** (D-a4). **Acceptée.** Si le tableau précède la production, les deux conditions diffèrent par toute la génération. L'appariement porte désormais sur le **flux**, non sur la génération : la même fiche produite avec tableau est passée dans la barrière avec et sans insertion connue (point 13) ; le recouvrement de 8-grammes avec le tableau est mesuré sur les fiches sans tableau pour calibrer la part due à la question commune (contrôle négatif conservé).

**15. Tableau placebo apparié en taille et coût de lecture** (D-c2 ; C-c3). **Acceptée.** Condition ajoutée : les proposeurs reçoivent en passe 2 un bloc de même taille, même forme et même place que le tableau, sans information croisée (texte inerte servi par le noyau, hors du tour). Elle isole l'effet du partage de celui de l'allongement du contexte et répond à la « dilution budgétaire » de C : si le placebo donne le même I par jeton que B, le tableau n'apporte rien d'autre que son coût.

**16. Contrôle « écriture libre sans gabarit »** (B-c1). **Rejetée.** Le gabarit borne les entrées, pas les fiches ; une écriture libre non bornée ouvre un canal supplémentaire (écueil 2) et un surcroît de code (écueil 3) sans servir la décision, qui oppose B tel qu'il serait déployé à A et au placebo. Le placebo (point 15) couvre l'effet de forme et de longueur du contexte servi, qui est ce que B redoute.

### Sur l'écueil 2 (instructions glissées)

**17. 6 entrées plantées : erreur de type II > 26 % à q₁ = 0,2** (C-b2 ; D-b). **Acceptée.** Effectif porté à ≥ 30 entrées plantées et 30 honnêtes porteuses de chaîne (illustratif), réparties sur ≥ 4 cases. La condition « prise nulle » est remplacée par une borne : la borne supérieure à 90 % de la prise des plantées (intervalle par grappes, la case étant la grappe) ne dépasse pas la borne supérieure de la prise des honnêtes de plus de 5 points (illustratif).

**18. La chaîne inerte mesure la propagation, pas toute la prise** (D-a4 ; mon (a) le reconnaissait déjà en HYPOTHÈSE). **Transformée en test.** Ajout d'un **lecteur à part aveugle** : pour chaque case, il reçoit les fiches de passe 2 et l'ensemble des entrées du tableau, sans savoir laquelle est plantée, et doit désigner l'entrée qui a visiblement agi sur une fiche ; exactitude comparée au hasard (1/nombre d'entrées). Cette mesure ne porte que sur l'effet, jamais sur la formulation ; sa sensibilité est elle-même inconnue et rapportée comme HYPOTHÈSE.

### Sur les duels et l'analyse

**19. Duel 2 confond lecture entière et écriture typée** (B-a5 ; B-c3 ; C-a3 ; C-c1 ; D-a6). **Acceptée.** Le duel 2 devient un **plan factoriel** lecture × écriture (voir (b)).

**20. Unité case × conception avec 2 cases ; bootstrap sur 3 proposeurs dégénéré ; incohérence unité/rééchantillonnage** (B-b4 ; C-b5 ; D-a6). **Acceptée.** Unité d'analyse : le couple proposeur × case, croisé ; mêmes proposeurs dans toutes les conceptions, cases réparties au sort ; test par permutation stratifiée des conditions à l'intérieur de chaque couple (texte, proposeur), ce qui conserve l'appariement des cases et traite séparément les dépendances texte, case et proposeur. Effectif minimal du pré-pilote pour qu'un duel soit jugeable : ≥ 4 cases × ≥ 4 proposeurs par conception (illustratif) ; en deçà, les duels sont rapportés en descriptif, sans verdict.

**21. H_B du duel 2 non exhaustive** (D-a6). **Acceptée.** Chaque H_B est réécrite comme le complément exact de H_A.

**22. Attrition par quarantaine confondue avec l'effet du tableau** (C-a4). **Acceptée.** Rapporter, par conception, le taux de quarantaine des fiches et des entrées, et deux ratios : I par 100 000 jetons dépensés (estimand) et I par fiche validée (diagnostic). Si le premier baisse et le second non, la baisse vient de la garde ou du coût de lecture, pas de la redite.

### Sur les rôles

**23. Permutation des étiquettes de rôle ; séparation par case et proposeur ; classes déséquilibrées** (D-c3 ; D-b). **Acceptée.** Le niveau de hasard du lecteur qui tente de retrouver le rôle est estimé par permutation des étiquettes ; l'évaluation est faite hors case et hors proposeur ; les rôles sont assignés par un carré latin équilibré sur proposeurs × cases, pour que rôle et proposeur ne soient pas confondus.

## (b) Expériences corrigées

**Prérequis instrumental (à faire en premier).** Qualification du détecteur de doublons sur : paires préfiltrées, échantillon aléatoire non préfiltré (≥ 60 par case), réécritures plantées par un tiers aveugle (famille de confirmation, ≥ 20), non-doublons certifiés intra-case (≥ 20). Mesures : rappel et fausses alertes contre la base trigrammes, accord brut, κ, coefficient robuste à la prévalence. Jugeable si rappel sur l'échantillon aléatoire ≥ 0,8 et accord brut ≥ 0,85 (illustratif). Sans cela, I n'existe pas et aucun duel n'a d'objet. Le directeur dit que le pré-pilote mesure déjà la détection des doublons (fait 5) : cette qualification en est la forme opérationnelle, pas une addition.

**Duel 1 : B contre A, avec bras placebo.** Trois conditions par case : A (titres et résumés), B (tableau complet sous gabarit, sans quota de lecture), P (placebo apparié en taille, forme, place et coût, sans information croisée).
- H_A : à dépense égale, I est supérieur en B d'au moins 20 % à A **et** à P, qualité jugée dans la marge (±5 % de l'échelle, illustratif, rapportée comme information si le fait 13 s'applique).
- H_B : complément exact : I n'excède ni A ni P de 20 %, ou la qualité sort de la marge.
- Métriques : I par 100 000 jetons (décisif) ; I par fiche validée, diversité de surface, taux de quarantaine (diagnostic).
- Unité : proposeur × case ; permutation stratifiée ; ≥ 4 cases × 4 proposeurs.
- Falsification : H_A tenue tombe « le partage libre coûte des idées » ; H_B tenue tombe « l'échange libre produit des idées, à cette échelle » ; si B bat A mais pas P, c'est le contexte allongé qui agit, non le partage : H_A tombe aussi.

**Duel 2 : plan factoriel lecture × écriture.** Facteur lecture : {résumés, corps entiers} ; facteur écriture : {aucune, pistes typées, libre sous gabarit}. A = (résumés, aucune) ; B = (résumés, libre) ; C = (corps, typée) ; cellules ajoutées : (résumés, typée) et (corps, aucune). Six cellules sont trop pour un pré-pilote réduit ; minimum pour séparer les facteurs : A, B, C, (résumés, typée), (corps, aucune), soit cinq, plus P.
- H_A : l'effet « corps entiers » fait baisser I d'au moins 15 % (illustratif) à écriture égale.
- H_B : complément : la baisse est inférieure à 15 %, ou I monte.
- Cela teste le chemin « corps lisibles » indépendamment du canal d'écriture ; l'effet du canal (typé contre libre) se lit sur l'autre marge du plan.
- Même unité, même test ; prise mesurée dans toute cellule à écriture (chaîne inerte hors de place, borne par grappes ; lecteur aveugle).

**Duel 3 : rôles.** Conditions : sans rôle ; rôles assignés par l'orchestrateur en carré latin ; étiquette de rôle sans consigne (contrôle négatif).
- H_A : rôles > étiquette seule d'au moins 10 % sur I (illustratif), et le lecteur à part ne retrouve pas le rôle au-delà du hasard permuté + 10 points.
- H_B : complément : gain < 10 %, ou rôle retrouvé.
- Si l'étiquette seule bat « sans rôle », c'est l'étiquette qui agit : H_A tombe (D-a5 sur B, repris ici par anticipation).
- Mesures : I et sa répartition (fait 4), dépense ; témoins comme sentinelle d'étalonnage seulement ; le verdict du juge n'entre pas (fait 13).

**Instruments, mesure minimale corrigée.**
- Détecteur : prérequis ci-dessus.
- Garde contre les instructions glissées : ≥ 30 entrées plantées (tiers) appariées à 30 honnêtes, chacune portant une chaîne inerte propre ; détection amont (quarantaine), refus d'honnêtes, prise aval avec et sans garde, séparément ; base à battre : garde lexicale existante (fait 2) et borne de taille, qui ignorent la chaîne. Contrôle négatif : recopie de la chaîne des honnêtes. Familles de réglage et de confirmation disjointes.
- Séparation d'avec le juge : contrôle positif (insertion connue avant barrière, détection exigée 100 %) ; recherche exacte de la chaîne dans tout ce que voit le juge, seuil zéro, borne supérieure binomiale rapportée ; recouvrement de 8-grammes tableau/fiches servies, calibré sur les fiches sans tableau.

**Écueil 3 révisé.** Déployé : 5 éléments par rapport au tableau minimal (le quota de lecture est retiré) ; le harnais de pré-pilote ajoute 3 éléments non déployés mais à contre-lire : service du placebo, insertion de contrôle positif, chemin du lecteur aveugle (illustratif). Condition : 5 + 3.

## (c) Réponse à la question de l'arbitre

**Décision.** Lancer la course 2 avec le tableau minimal (défaut) ; consacrer le pré-pilote à qualifier le détecteur de doublons, puis à comparer A, B et P ; n'ouvrir C et le factoriel que si l'effectif ≥ 4 cases × 4 proposeurs est financé. Enjeu : l'échange voulu entre proposeurs contre trois écueils dont aucun n'est encore mesuré, et un estimand (I) qui n'existe pas tant que le détecteur n'est pas qualifié.

**Options.**
- *A seul en course 2, pré-pilote réduit au détecteur.* Avantage : zéro code nouveau, le fait 5 est tenu à la lettre. Inconvénient : ni échange ni rôles ; si les doublons tombent à zéro, le détecteur n'est éprouvé que sur du planté.
- *A en course, pré-pilote A/B/P.* Avantage : mesure les trois écueils avec un contrôle placebo qui sépare partage et contexte ; 5 éléments de code à sceller. Inconvénient : l'équivalence sur les témoins n'est pas jugeable à cette échelle ; l'atteinte au juge repose sur le mécanique et un contrôle positif.
- *Pré-pilote factoriel incluant C.* Avantage : seul moyen de séparer lecture entière et écriture typée. Inconvénient : cinq cellules plus placebo, lecture des corps la plus chère ; 8 éléments à contre-lire.

**Recommandation.** Option 2, **confiance moyenne** sur le défaut, **faible** sur tout écart vers B ou C : après critique, le pré-pilote que j'avais dimensionné n'avait pas la puissance de démentir ses propres seuils ; redimensionné, il reste réduit et la plupart de ses seuils sont illustratifs. Écart conditionnel vers B seulement si, au pré-pilote : (écueil 1) I en B dépasse A et P de 20 % sans que la part du prolifique franchisse le quantile de permutation ; (écueil 2) la borne supérieure par grappes de la prise des plantées ne dépasse pas celle des honnêtes de plus de 5 points et le lecteur aveugle reste au hasard ; (écueil 3) les 5 + 3 éléments sont contre-lus et scellés avant lecture des résultats. Tant que ces issues ne sont pas lues, l'évitement est HYPOTHÈSE et le défaut tient.

**Ce qui reste HYPOTHÈSE.** Le lien entre les 12 paires et l'absence de vue sur la passe 1 (fait 3) ; que les 12 paires ne forment aucun cycle (fait 4) ; que le détecteur atteint un rappel jugeable sur paires non préfiltrées ; que la chaîne inerte et le lecteur aveugle capturent la prise ; que la séparation d'avec le juge se mesure autrement que par contrôle positif à cette échelle ; que le choix A/B/C échappe au fait 13 (sinon la qualité jugée sort des critères et tout repose sur I et la dépense) ; que I et sa répartition tiennent lieu d'oracle pour les rôles ; que la liste de code est close.

**Mesure du pré-pilote, par écueil.**
- Influence croisée : I par 100 000 jetons en A, B, P ; part attribuée du prolifique contre le quantile de permutation ; chaîne inerte et 8-grammes dans ce que voit le juge ; témoins en sentinelle.
- Instructions glissées : prise des 30 plantées contre 30 honnêtes, avec et sans garde, bornes par grappes ; lecteur aveugle contre hasard.
- Surcroît de code : liste des 5 + 3 éléments, contre-lue et scellée ; « évité sous condition » si le directeur accepte ce nombre.

**Expérience à faire en premier.** La qualification du détecteur de doublons sur paires non préfiltrées et réécritures plantées par un tiers aveugle : sans elle, aucun compte d'idées distinctes n'est jugeable et aucun duel ne peut trancher.

FIN-DE-CELLULE