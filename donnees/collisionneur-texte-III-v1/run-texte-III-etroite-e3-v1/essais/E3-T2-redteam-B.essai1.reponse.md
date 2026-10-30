# Critique croisée — Proposition B (Tour III.2)

Je critique ci-dessous les propositions A, C et D sur les axes demandés : défauts de méthode, conditions où la puissance se perd, et contrôles négatifs manquants. Je ne lisse ni ne fusionne ; chaque critique est autonome.

---

## Sur la proposition A

### (a) Défauts de méthode

**1. Affectation des recaptures : écart entre les déviances rapportées et la conclusion.** A rapporte trois valeurs de G² — 14,6 ; 13,4 ; 12,85 — et retient la dernière comme seule compatible avec 12,9 (RAPPORTÉ). C rapporte pour les mêmes cas 14,22 ; 13,20 ; 12,90. D donne 14,63 ; 13,36 ; 12,85. Les trois propositions convergent sur le même cas retenu, mais les chiffres diffèrent au centième. A ne donne pas le détail du calcul de N̂₀ ni des fréquences attendues, ce qui empêche un tiers de trancher entre ces arrondis. La conclusion est vraisemblablement correcte, mais le chemin est insuffisamment documenté pour être refait.

**2. Formule de n_eff et affirmation que ρ « plafonne ce qui est certifiable ».** A écrit n_eff = n / (1 + (n−1)ρ) et en déduit que n_eff ne peut dépasser 1/ρ. Ce résultat suppose une corrélation échangeable entre les indicateurs binaires de réussite des familles. HYPOTHÈSE. Si la structure de corrélation est par grappes de taille variable plutôt qu'échangeable, n_eff dépend de la taille des grappes et non de n seul ; la borne 1/ρ ne tient plus. A ne pose pas cette condition et donne l'affirmation comme générale.

**3. Duel 2 : variable confondante entre γ et la définition de « non découverte ».** Le duel 2 teste si l'écart vues / tenues à l'écart masque un échec parmi les familles « non découvertes ». Mais dans le monde simulé, les familles non découvertes sont celles qui n'ont pas été tirées. Si le seuil δ est calculé sur les tenues à l'écart (qui *ont* été découvertes puis mises de côté), et que la part d'échec est mesurée sur les non découvertes (qui n'ont jamais été tirées), le duel compare deux populations différentes sans qu'un mécanisme les relie, sauf via γ. Le duel est donc un test de la forme fonctionnelle du lien (γ linéaire sur le logit), pas de l'option 2 en tant que telle. A ne sépare pas ces deux questions.

**4. Modèle saturé : interprétation trompeuse.** A écrit N̂ ≈ 186, puis « variance pratiquement non bornée ». Le modèle saturé à 0 ddl a un ajustement exact aux sept cellules mais n'a aucune puissance résiduelle pour tester u₁₂₃ = 0. A mentionne ce point mais le range parmi les « estimateurs comparés » du plan de simulation sans dire que sa couverture à 0 ddl n'est définie que sous la supposition u₁₂₃ = 0. Si la simulation inclut des mondes où u₁₂₃ ≠ 0, l'estimateur saturé ne sera pas biaisé mais son intervalle sera indéfini — ce n'est pas un biais, c'est une non-identifiabilité. Le plan ne mesure alors rien sur cet estimateur.

**5. Chao2 vs Chao1 : nomenclature instable.** A écrit « Chao2 » pour la formule basée sur les fréquences de capture f₁, f₂ avec T sources. La formule donnée (S_obs + ((T−1)/T) f₁²/(2f₂)) est correctement celle de Chao pour données d'incidence (Chao, 1987). Mais en écologie, « Chao2 » désigne habituellement l'estimateur basé sur les données d'incidence par échantillon, par opposition à « Chao1 » qui porte sur les données d'abondance. C utilise « Chao1 » pour la même formule f₁²/(2f₂) sans le facteur (T−1)/T, ce qui est une convention différente. Le lecteur ne peut pas comparer les résultats (55,3 chez C vs 49,2 chez A) sans recalculer lui-même. Ce n'est pas une erreur mathématique mais une source de confusion méthodologique.

### (b) Conditions où la puissance se perd

- **Duel 1** : si σ (hétérogénéité) et τ (paire) varient simultanément, la couverture de M₀ peut tomber pour deux raisons indiscernables. Avec 2 000 mondes par cellule et un plan factoriel à ≥ 4 facteurs × 4 niveaux (≥ 256 cellules), certaines cellules extrêmes auront une erreur Monte-Carlo de couverture ≈ 0,01, ce qui rend le seuil de 0,80 vs 0,90 juste détectable. Si la taille N est petite (N = 40), les intervalles de tous les estimateurs sont larges ; le duel ne disqualifie personne car toutes les couvertures sont élevées par trivialité.

- **Instrument 2** : sous γ = 0,6 et ρ = 0,20 simultanément, l'effectif effectif est si petit et le biais de sélection si fort que la couverture du fait 9 et de la règle corrigée sont toutes deux proches de zéro. Le duel ne départage plus rien : il montre seulement que les deux procédures échouent, ce qui est prévisible et non informatif.

- **Bloc 4** : avec m = 25 familles extérieures, la puissance du test « ≥ 6 échecs falsifie ε = 0,10 » n'est pas donnée. Si la vraie part d'échec extérieure est 0,15 (juste au-dessus de 0,10), P(≥ 6 | m=25, p=0,15) ≈ 0,15 (illustratif). Le test est alors trop faible pour détecter un écart de 5 points, ce qui rend la prédiction scellée non falsifiable en pratique.

### (c) Contrôles négatifs manquants

- **Aucun contrôle sur l'erreur d'appariement du simulateur lui-même.** A simule des fusions et scissions à tort comme facteurs, mais ne vérifie pas que son code d'appariement simulé produit bien le taux φ ou ψ déclaré. Il faut un contrôle où les identités vraies des familles sont comparées aux identités attribuées, indépendamment de l'estimateur de N̂.

- **Pas de contrôle négatif pour la règle séquentielle.** A mentionne un plan séquentiel à zéro échec avec dépense d'α, mais ne prévoit pas de monde où la vraie proportion est exactement ε, pour vérifier que la probabilité de certification est bien ≤ α. C'est le test de calibration minimal de toute procédure séquentielle.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Chao1 appliqué à des données d'incidence multi-sources.** C écrit la formule Chao1 = S_obs + f₁²/(2f₂) = 55,29. Cette formule est celle de Chao (1984) pour des données d'abondance (nombre d'individus observés une fois, deux fois, etc. dans un seul échantillon). Or ici, f₁ = 16 désigne le nombre de familles vues par exactement une source sur trois, et f₂ = 7 celles vues par exactement deux sources. Ce sont des données d'incidence (présence/absence dans T échantillons). L'estimateur approprié pour T échantillons d'incidence inclut le facteur (T−1)/T, donnant 49,2 (comme A). C omet ce facteur. Le résultat 55,29 surestime la borne inférieure, ce qui est paradoxalement dangereux pour une borne inférieure (elle perd sa propriété de borne). C donne ensuite séparément la version corrigée avec le facteur, obtenant 47,0, mais sans signaler que sa première formule n'est pas appropriée au plan d'échantillonnage.

**2. Estimateur de couverture corrigé : référence « à vérifier » et formule non standard.** C donne Ĉ_corr ≈ 84,5 % avec une formule attribuée à « Chao et Jost, 2012, *Ecology*, réf. à vérifier ». Cette honnêteté est conforme aux règles, mais la formule n'est pas dérivée ni justifiée dans le texte. Un tiers ne peut pas juger si elle s'applique ici (T = 3 sources, données d'incidence) ou si elle suppose des données d'abondance.

**3. Duel 2 : l'estimateur de Horvitz-Thompson suppose des probabilités d'inclusion connues.** C propose, sous découverte biaisée, de corriger par pondération inverse (Horvitz-Thompson) avec des probabilités d'inclusion « estimées par capture-recapture ». Mais les probabilités de capture estimées par capture-recapture sont précisément ce que le bloc 3 tente d'estimer, et elles ne sont fiables que sous un modèle de capture. Le duel teste donc la correction par Horvitz-Thompson sous une circularité : les poids viennent du modèle, et si le modèle est mal spécifié, les poids sont faux, et la correction ne corrige rien. C ne prévoit pas de monde simulé où les poids estimés sont volontairement mal spécifiés.

**4. Modèle saturé et hétérogénéité : affirmation contestable.** C écrit que l'hétérogénéité « crée u₁₂₃ > 0 » et que « poser u₁₂₃ = 0 gonfle artificiellement n̂₀₀₀ ». C'est un argument qualitatif correct dans le cas classique (Link, 2003, *Biometrics* — référence à vérifier), mais la direction du biais de u₁₂₃ dépend de la forme de l'hétérogénéité. Sous une loi bêta symétrique avec CV modéré, u₁₂₃ peut être positif ou négatif selon les valeurs de capture. L'affirmation n'est pas universelle, et C ne donne pas la condition sous laquelle elle tient.

**5. Bloc 4 : le protocole de « double lecture aveugle avec arbitrage pré-enregistré » est un comportement d'agent.** Le périmètre exclut tout comportement d'agent. Ce point n'est pas une critique de méthode statistique mais un rappel de périmètre ; je le note sans développer.

### (b) Conditions où la puissance se perd

- **Duel 1** : C fixe N = 100 (illustratif) pour toutes les réplications. Si la vraie N est proche de S_obs (par exemple N = 42), la puissance du modèle log-linéaire saturé pour détecter n₀₀₀ > 0 est très faible (n₀₀₀ = 5, erreur standard > 5 typiquement). Le duel ne discrimine que pour N >> S_obs, ce qui est le cas le moins intéressant.

- **Instrument 2** : sous ρ_fam = 0,6 et m = 20 éléments par famille, la mesure d'universalité a une variance intra-famille dominante et une variance inter-famille géante. La base à battre (moyenne brute) et l'instrument proposé auront tous deux une erreur de type I proche de 1 si ε est petit. Le plan ne départage rien dans cette zone.

- **Bloc 4 validation familles inconnues** : C donne un intervalle de prédiction pour K_nouv sous Chao1, mais le test « K_nouv ≥ 20 falsifie Chao1 » suppose que la source extérieure échantillonne uniformément, ce qui est une HYPOTHÈSE non testée. Si la source extérieure a un biais de capture corrélé positivement aux trois premières sources, K_nouv sera faible même si N est grand, et le test ne falsifiera rien.

### (c) Contrôles négatifs manquants

- **Pas de contrôle négatif pour la couverture corrigée Ĉ_corr.** C introduit un estimateur corrigé à 84,5 % mais ne prévoit pas de monde simulé où la couverture vraie est connue et où l'on vérifie que Ĉ_corr est non biaisé. Cet estimateur pourrait être systématiquement biaisé vers le haut sous dépendance positive, ce qui rendrait la « couverture » rassurante à tort.

- **Pas de contrôle négatif pour le SPRT.** C mentionne Wald (1945) et une frontière alpha-spending de Pocock, mais ne prévoit pas de monde où la proportion est exactement au seuil (π = ε) pour calibrer la procédure. Le contrôle négatif de l'instrument 2 (toutes les familles à θ = τ) est bien conçu mais ne teste pas la procédure séquentielle, seulement la procédure à taille fixe.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Concision qui masque des choix.** D est la plus concise des trois propositions, ce qui a l'avantage de la lisibilité mais le défaut de laisser implicites des choix de modélisation. Par exemple, le modèle génératif du bloc 2 est décrit par « une loi de découverte D, des risques q_f hétérogènes, des éléments corrélés intra-famille, et une corrélation inter-familles paramétrée », sans spécifier de famille paramétrique. La variance σ²_B/n + σ²_W/(nm_f) est donnée comme « forme minimale » mais c'est la décomposition sous échangeabilité ; D n'énonce pas cette condition.

**2. Prédiction du bloc 4 sur les familles inconnues.** D scelle une part nouvelle de 1 − 37/49,19 = 24,78 %. Ce calcul suppose que la source extérieure échantillonne uniformément dans la population estimée par Chao, ce qui est une HYPOTHÈSE. Plus grave : la formule 37/N̂_Chao est la proportion de familles *observées* dans la population estimée, pas la probabilité qu'une famille tirée au hasard dans la population soit parmi les 37. Ces deux quantités ne coïncident que si chaque famille de la population a la même probabilité de capture par la source extérieure. Or l'hétérogénéité de capture est précisément le problème. La bonne prédiction serait basée sur la couverture de Good-Turing (Ĉ = 0,778, comme D le calcule par ailleurs), pas sur 37/N̂_Chao. D donne les deux mais scelle la mauvaise.

**3. Duel 1 : formulation asymétrique et issue intermédiaire non décisive.** D écrit : « un résultat intermédiaire ne départage pas et invalide les deux énoncés forts ». C'est honnête, mais cela signifie que le duel a trois issues dont une est non décisive. La règle B4 du protocole demande que chacune des *deux* issues falsifie quelque chose. Si le résultat intermédiaire a une probabilité substantielle (ce qui est probable quand la dépendance est modérée), le duel ne remplit pas sa fonction la plupart du temps. Le duel devrait être reformulé avec deux issues exclusives et exhaustives, quitte à restreindre la grille de mondes.

**4. N̂₀ = 39,2184 : précision excessive.** D donne N̂₀ avec quatre décimales, ce qui implique une précision arithmétique que le statut RAPPORTÉ des données ne supporte pas. Les comptes sont des entiers de statut RAPPORTÉ ; donner N̂₀ au millième suggère une fausse précision. Il conviendrait d'arrondir à l'unité (39) ou de donner un intervalle.

**5. Déviances rapportées.** D donne 12,85 ; 13,36 ; 14,63. A donne 12,85 ; 13,4 ; 14,6 (arrondis). C donne 12,90 ; 13,20 ; 14,22. Pour le cas retenu, D et A convergent sur 12,85, C donne 12,90. Cet écart de 0,05 est petit mais non nul ; il vient vraisemblablement de différences dans l'optimisation de N̂₀ (le MLE de N sous indépendance n'est pas entier et dépend de la méthode de résolution). D ne signale pas cette sensibilité numérique.

### (b) Conditions où la puissance se perd

- **Duel 2** : D teste l'écart vues / tenues à l'écart comme mesure de transport vers l'extérieur. La couverture peut tomber sous 90 % dès que la partition vues / tenues à l'écart n'est plus échangeable. Mais si le nombre de familles tenues à l'écart est petit (par exemple 10 sur 37), l'intervalle de Δ sera large et la couverture nominale sera atteinte par trivialité (tout est dans l'intervalle). La puissance du duel dépend du nombre de familles tenues à l'écart, que D ne fixe ni ne fait varier.

- **Bloc 3** : D utilise Good-Turing (Ĉ = 77,78 %) et note correctement que cela couvre la « masse de probabilité de capture, non 77,78 % des familles ». Cette distinction est juste. Mais sous hétérogénéité forte, les familles à faible capture portent une masse de probabilité faible ; Ĉ peut être 0,78 alors que 40 % des familles en nombre n'ont pas été vues. Le plan de D ne prévoit pas de simulation mesurant l'écart entre Ĉ et la proportion effective de familles couvertes (N_obs/N) en fonction de l'hétérogénéité.

- **Bloc 4** : la validation du « nombre nécessaire » scelle une couverture de π ≥ 95 %, falsifiée si elle tombe sous 90 %. La puissance de cette vérification dépend du nombre de réplications extérieures. Si une seule population extérieure « entièrement mesurée » est disponible, on a une observation unique de la couverture (elle couvre ou ne couvre pas), et la probabilité de détecter une couverture réelle de 85 % avec une seule observation est… 15 %. D ne discute pas le nombre de réplications nécessaire pour cette méta-validation.

### (c) Contrôles négatifs manquants

- **Pas de contrôle négatif explicite pour le modèle à classes latentes.** D mentionne les « variantes à classes latentes » comme estimateurs à soumettre au plan de simulation, mais ne prévoit pas de monde simulé *sans* classes latentes où l'on vérifie que cet estimateur ne surestime pas N̂. Un modèle à classes latentes surajusté peut inférer des classes fantômes et gonfler N̂ ; sans contrôle, ce biais est invisible.

- **Pas de contrôle négatif pour la suite de confiance (martingale).** D évoque une « suite de confiance valide à tout temps » mais ne prévoit pas de monde où la proportion est au seuil ε pour calibrer la martingale. C'est le même manque que chez C, mais plus préoccupant car D ne donne aucune référence pour la procédure séquentielle retenue.

- **Pas de contrôle sur la fermeture de la population pendant la simulation.** D mentionne que « une population non fermée exige dates et modèle ouvert » mais le plan de simulation ne comporte pas de monde où des familles sont ajoutées pendant l'énumération. Sans ce contrôle, on ne sait pas comment les estimateurs se comportent sous violation de la fermeture, qui est pourtant une HYPOTHÈSE identifiée par D.

---

## Note transversale

Les trois propositions partagent un défaut commun que je relève sans le développer pour chacune : **aucune ne propose de simulation où l'interaction d'ordre trois u₁₂₃ est non nulle** comme facteur du plan expérimental. Or cette interaction est la seule hypothèse commune à tous les modèles log-linéaires identifiables, et elle est non testable de l'intérieur (0 ddl dans le modèle saturé). Le contrôle négatif minimal serait un monde où u₁₂₃ > 0 (ou < 0), pour mesurer le biais de tous les estimateurs sous cette violation. Son absence est, à mon avis, le trou le plus grave dans les trois plans de simulation.

FIN-DE-CELLULE