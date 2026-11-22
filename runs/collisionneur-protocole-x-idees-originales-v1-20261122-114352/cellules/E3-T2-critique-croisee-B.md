# Proposition B — Tour III.2 : critique croisée de méthode

## 0. Constats d'intégrité

- **Bloc FAITS.** Il recopie la question (empreinte annoncée identique, que je ne recalcule pas). Il ne contient aucun fait porteur de statut. Toute affirmation empirique des cinq pièces relève donc, au mieux, du RAPPORTÉ ou de l'HYPOTHÈSE de son auteur.
- **Pièces A, C, D, E, F.** Elles sont présentes et paraissent complètes : chacune se termine par sa ligne de clôture.
- **Statuts.** C et E attribuent le statut VÉRIFIÉ à plusieurs énoncés : estimateurs de Good, théorème de Rice, identité de Bayes, garanties « par construction ». Je ne modifie pas ces statuts. Je signale seulement que le bloc FAITS n'en adosse aucun, et je ne les utilise pas comme résultats.
- **Références.** Je ne mentionne que des références déjà nommées par les pièces, en les leur attribuant, sans en garantir le contenu. Toute autre piste est notée « référence à vérifier ».
- **Notation pour (b).**
  - p_c : masse de la classe c sous la loi de référence P₀.
  - N : nombre de tirages ; f₁, f₂ : nombre de classes vues une et deux fois.
  - M_rare = Σ_{p_c ≤ τ} p_c : masse totale des classes rares.
  - π(r) : part d'idées vraies à rareté r.
  - α, β : taux de fausse confirmation et de non-détection du contrôle.
  - ε_s : probabilité qu'une réécriture d'une classe soit comptée comme une autre classe (sous-fusion) ; ε_f : probabilité de fusion à tort (sur-fusion).
  - z : quantile du niveau préenregistré.
- **Convention pour (c), au titre de B4.** Chaque contrôle négatif est donné avec deux issues : celle attendue si l'instrument est sain, et celle qui l'invalide.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Le canoniseur κ fusionne toutes les idées vraies sur le banc proposé.** Les idées sont des inégalités entre invariants de graphes, et la signature est « le vecteur des verdicts » sur une batterie de graphes.
   - Si le verdict est binaire (l'inégalité tient ou non), toute inégalité vraie a la même signature, « tout vrai ». κ réunit alors toutes les vraies en une seule classe, dont la masse est la masse totale des vraies.
   - Conséquence, vraie par construction : la strate rare ne contient que des inégalités fausses, qui échouent sur des graphes différents. D2 et D3 deviennent triviaux ou indéfinis.
   - Correctif nécessaire : prendre pour signature le vecteur des écarts numériques (membre gauche moins membre droit) ou des valeurs des invariants, et le préenregistrer.
2. **Fuite entre les sondes de κ et le contrôle T.** Si les petits graphes aléatoires de T recoupent la batterie-sonde de κ, deux idées de même classe reçoivent nécessairement le même verdict de T. La confirmation n'ajoute alors rien à l'appartenance à la classe. A ne déclare pas que les deux tirages sont disjoints.
3. **Le nul de D2 rend H_A quasi garantie.** Une inégalité tirée au hasard d'une grammaire fermée est probablement presque toujours fausse (HYPOTHÈSE, à mesurer). Un rapport supérieur à 1 oppose alors « modèle » à « hasard », et non « queue » à « mode ». A en conclut à tort que « la thèse “le mode contient tout” tombe ». Seul le contraste entre classes rares et classes fréquentes du même système, à forme appariée, porte sur cette thèse.
4. **f₁/N joue deux rôles.** Cette quantité est une masse manquante agrégée, pas une masse par classe. A l'utilise à la fois pour piloter I1 et comme mesure de rareté. Pour certifier p_c ≤ τ par classe, il faut un panel P₀ frais. A ne le dimensionne pas et ne prévoit pas de couverture simultanée sur les classes testées.
5. **Recouvrement possible entre panel P₀ et bras de base en D4.** Si le panel qui définit la rareté est tiré dans le même échantillon que le bras de base, les classes rares de la base sont par construction celles que le panel n'a pas revues. Il faut des tirages indépendants, et le déclarer.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1.** Le verdict n'est pas jugeable dans trois cas :
  - Var(f₁/N) ≥ (θ − M₀)², où M₀ est la vraie masse manquante.
  - Les tirages sont corrélés au sein d'un lot (même invite ou même serveur), avec une corrélation intra-lot ρ > 0 sur des lots de taille m. N_eff = N/(1+(m−1)ρ) et f₁/N est biaisé vers le bas.
  - La sous-fusion ajoute environ ε_s · N · (1 − M_rare) singletons parasites. Dès que ε_s(1 − M_rare) est du même ordre que θ, H_A et H_B ne se distinguent plus.
- **D2 et D3.** Le nombre de confirmées rares vaut n_r ≈ N · M_rare · [π_rare(1−β) + (1−π_rare)α]. Si n_r · δ² < z² · FDR(1−FDR), l'intervalle déborde ±δ et l'issue est « non tranchée » à coup sûr.
- **D4.** Soit σ l'écart-type entre graines de R et r le nombre de réplications. Si σ/(R_base · √r) ≳ ε/z, le rapport ne peut sortir de la bande [1, 1+ε].

### (c) Contrôles négatifs dont l'absence est fatale

- **Vraies distinctes plantées** (absent) : K inégalités vraies, connues et non équivalentes.
  - Si κ est sain : K classes.
  - Si elles sont fusionnées : κ est invalide sur ce banc, et D2 et D3 aussi.
- **Disjonction sondes/contrôle** (absent) : relancer T sur un échantillon de graphes disjoint de la batterie-sonde.
  - Si l'instrument est sain : l'accord est inchangé.
  - Si l'accord chute : la confirmation était héritée de la signature.
- **Contraste rare/fréquent apparié** (à ajouter à D2), avec permutation des étiquettes de rareté (présente, à conserver).
- **Essai A/A et générateur synthétique de couverture plantée** (présents) : à conserver tels quels.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **La rareté est mesurée dans l'échantillon même qui sert à sélectionner.** En E1, le bras I1 soumet à V les classes dont p̂ ≤ 0,01 (illustratif) dans son propre échantillon, et Y_rare est compté avec ce même p̂.
   - Dès que N ≥ 1/τ, tout singleton passe le seuil : « rare » se réduit à « vu une fois ».
   - Le nombre de singletons croît avec N_gen. Le bras qui génère davantage est donc favorisé par construction.
   - La référence (P₀ figée) n'est jamais fixée.
2. **L'homogénéité intra-classe postulée pour I1** (φ(x) = φ(x') ⇒ V(x) = V(x')) a deux statuts possibles. Elle est vraie par construction si les sondes E sont incluses dans les cas de V : c'est alors une fuite. Elle est fausse sinon, et le représentant unique peut écarter une variante vraie. C ne dit pas lequel des deux cas il retient.
3. **I3 confond fréquence de génération et probabilité a priori de vérité.**
   - Pondérer Benjamini-Hochberg par p̂(s) suppose que π(r) est monotone, ce qui est précisément l'inconnue.
   - Les poids et le nombre k(p̂) de contrôles sont estimés sur les données mêmes qui sont testées. Les garanties des procédures pondérées supposent en général des poids indépendants des p-valeurs (référence à vérifier).
   - V est décrit comme binaire. Une p-valeur n'existe qu'avec un taux de passage sous le nul calibré sur des idées fausses échangeables avec les idées générées.
4. **Le contrôle négatif de E3 n'en est pas un.** Inverser la pénalité « doit dégrader maximalement le FDR », mais l'effet attendu dépend de la pente de π(r), qui est inconnue. Son issue sous « instrument sain » n'est pas déterminée.
5. **Banc « à puits connus » (instrument 3).** Les 18 niches sont connues des concepteurs, qui choisissent aussi la grille d'I2 : la construction et l'évaluation ne sont pas séparées. De plus, le caractère « non standard » est posé, pas mesuré sous P₀.
6. **V* n'est appliqué qu'aux candidats confirmés (section d).** β par strate est donc inestimable, et la formule de la limite 1 ne peut pas être instanciée sur le banc.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E0.** E[N₁] contient un terme ε_s · N. Si ε_s est du même ordre que le seuil retenu pour Ĉ, la falsification de H_A ne distingue pas « absence de puits » de « φ défaillant », comme C l'admet lui-même. M_10% dépend du nombre de classes observées, donc de N : la statistique n'est pas invariante en taille d'échantillon.
- **E1.** Si Y_rare(témoin) suit une loi de Poisson de paramètre λ petit, P(Y_rare = 0) = e^{−λ} n'est pas négligeable et le rapport 1,5× (illustratif) est indéfini sur une part des réplications.
- **E3.**
  - Si Corr(V_j, V_k | faux) = 1, c'est-à-dire si les erreurs de V sont déterministes par classe, k contrôles équivalent à un seul. La puissance de I3 contre les faux positifs est alors nulle.
  - Si le nombre de confirmées rares n vérifie n · 0,1 · 0,9 < (z · marge)² (seuils illustratifs de C), l'intervalle du FDR recouvre 0,10.

### (c) Contrôles négatifs dont l'absence est fatale

- **A/A** (absent) : témoin contre témoin, graines différentes, même chaîne. Il donne la loi nulle du rapport. Sans lui, le seuil 1,5× n'a pas de niveau.
- **Priorisation aléatoire** (absent) : même N_gen, même déduplication, et le même nombre de classes soumises à V, tirées au hasard sans regard à p̂.
  - Si la priorisation par rareté est utile : I1 bat ce bras.
  - Si l'égalité est observée : le gain venait du seul surcroît de génération.
- **Disjonction sondes E / cas de V** (absent).
- **φ_rand et grille orthogonale** (présents) : à conserver.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le terrain supprime l'objet de la question.**
   - L'identité est le vecteur des décisions sur toutes les instances admissibles ; la valeur est le coût pondéré sur ces mêmes instances. La valeur est donc une fonction de la classe.
   - Le contrôle est un oracle, et son homogénéité intra-classe est vraie par construction.
   - F est nul par construction si l'exécution est exacte, ce que D reconnaît. La contrainte « sans augmenter les fausses découvertes » ne porte plus aucune information, et le transport du contrôle vers la queue n'est pas testable.
   - Conséquence : les résultats de D ne disent rien du régime visé par la question, celui où le contrôle est imparfait.
   - Correctif possible : un contrôle sur un sous-ensemble d'instances et un audit sur l'ensemble complet, pour réintroduire un FDR mesurable.
2. **L'intervention « dédupliquer » est vide par construction sur ce terrain.** Calculer la clé revient à calculer le contrôle. Le duel est décidé d'avance ; D le pressent sans en tirer la conséquence.
3. **Certification simultanée.** D donne la condition d'arrêt pour une seule classe. La couverture simultanée sur K classes, qu'il exige lui-même, est plus coûteuse. Sous le budget correspondant, Y = 0 dans tous les bras.
4. **Le second interpréteur partage la spécification.** Les erreurs de spécification sont alors parfaitement corrélées entre les deux implémentations. Leur accord mesure l'erreur d'exécution, pas l'erreur de spécification.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Certification de rareté.** Avec n appels de panel, une classe sans réapparition a une borne supérieure binomiale d'environ ln(K/α)/n en couverture simultanée. Si n · τ ≲ ln(K/α), aucune classe n'est certifiable : la puissance est nulle.
- **Duel.** Si E[Y] = λ est petit dans les deux bras, P(Y_int = Y_témoin = 0) est élevée et la région de confiance appariée chevauche 0 par construction.
- **Contrainte sur F.** Si F ≡ 0 presque sûrement, ΔF ≤ 0 est toujours satisfaite. H_B ne peut se réaliser que par ΔY ≤ 0, et la clause « fausses découvertes » est non jugeable.
- **Allocation.** La formule 1 − ∏_m(1 − p_mc)^{n_m} exige des estimations de p_mc ≪ 1/n_pilote. En dessous de cette résolution, l'allocation choisie sur le pilote ne dépend que du bruit, et le duel perd sa puissance.

### (c) Contrôles négatifs dont l'absence est fatale

- **A/A par campagnes** (absent).
- **Erreurs plantées dans la chaîne de publication** (partiellement présent) : D prévoit des différences sur une instance peu pondérée pour l'identité et des échecs de faisabilité pour le contrôle. Il faut l'étendre à des règles fautives injectées en amont de la publication.
  - Si la chaîne est saine : F les détecte.
  - Si F reste à 0 : la mesure est aveugle.
- **Alias du même modèle** (présent) : excellent, à conserver.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **p_GT n'est pas une rareté par classe.**
   - (r+1)S_{r+1}/(N·S_r) donne la même valeur à toutes les classes vues r fois.
   - Pour une classe absente de l'échantillon nominal (r = 0), il n'existe pas de valeur par classe.
   - Pour M-B et M-C, qui produisent par conception des classes hors de l'échantillon nominal, le critère p_GT ≤ 0,01 (illustratif) est indéfini.
   - Si la convention retenue est « non vu ⇒ rare », toute variante que φ ne fusionne pas devient rare gratuitement.
2. **La décorrélation exigée en Exp-C est obtenue par construction.** Deux échantillons indépendants d'une même loi à queue lourde ont des ensembles de classes rares dont le Jaccard est faible, par sous-échantillonnage, même pour un seul modèle. Le critère Jaccard < 0,30 (illustratif) est satisfait sans aucune hétérogénéité. Il faut une référence en moitiés intra-modèle, comme le fait A.
3. **Fuite entre V_orth et V*.** V_orth teste des « distributions adverses décalées » et V* porte sur 2 000 instances hors distribution (illustratif). Si les familles de décalage se recouvrent, M-B consomme une partie de l'oracle et FDR(M-B) est sous-estimé par construction. E ne déclare aucune disjonction des générateurs d'instances.
4. **Facteurs confondus.**
   - M-C fait varier trois facteurs à la fois : modèles de base ou alignés, invite à exemples formels (coût en jetons), et test d'invariance.
   - M-B est comparé à M-A, ce qui mélange l'effet de l'automate tabou et celui de V_orth. Le contrôle haute température ne neutralise que le premier.
5. **Le « contrôle négatif » de Exp-A n'en est pas un.** La déduplication par SHA-256 est un comparateur dont on attend un gain, pas un nul.
6. **La valeur MDL est biaisée contre la rareté.** L(c) dépend du représentant retenu. Si c'est le plus court observé, son espérance décroît avec le nombre de membres vus. Les classes fréquentes paraissent donc plus compressives, et la mesure de valeur est confondue avec la rareté.
7. **Benjamini-Hochberg sur un V binaire** pose le même problème qu'en C, point 3. E le reconnaît comme HYPOTHÈSE.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Exp-A à C.** Avec 5 graines (illustratif), soit c_v le coefficient de variation de R_vrai entre graines. Si c_v · √(2/5) ≳ 0,20/z, le seuil de +20 % (illustratif) n'est pas atteignable de façon discriminante. Le test exact de Fisher sur le FDR n'a pas de puissance quand l'espérance du nombre de fausses confirmées par bras est de l'ordre de l'unité.
- **p_GT.** Pour r tel que S_{r+1} = 0, p_GT = 0 : l'estimateur dégénère. Le lissage annoncé n'est pas spécifié.
- **Majoration α_V · α_orth.** Elle exige Cov(V, V_orth | faux) ≤ 0. Avec une covariance positive c, le taux joint vaut α_V · α_orth + c, et la garantie disparaît.
- **Exp-Diag.** Le FDR des singletons repose sur n₁ᶜ singletons confirmés. Si n₁ᶜ · 0,1 · 0,9 est petit devant z² fois la marge au carré, l'issue n'est pas tranchée. La conjonction de trois critères empêche en outre d'attribuer une falsification de H_A à un composant précis.

### (c) Contrôles négatifs dont l'absence est fatale

- **Jaccard en moitiés intra-modèle** (absent) : fatal pour Exp-C.
  - Si la décorrélation est réelle : le Jaccard inter-familles est inférieur au Jaccard intra-modèle.
  - Si les deux sont égaux : le critère est vide.
- **A/A** (absent).
- **Partition aléatoire de même cardinalité avant V** (absent) : vrai nul de M-A.
  - Si φ apporte de l'information : M-A bat ce bras.
  - Si l'égalité est observée : le gain vient de la seule réallocation du budget.
- **Disjonction des générateurs de V_orth et V*** (absent).
- **Générateur d'arbres syntaxiques aléatoires soumis à V** (présent) : à conserver.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **H_A0 n'est pas jugeable telle qu'écrite.** Elle exige qu'une recherche exhaustive établisse des idées valides « de masse p₀ ≤ τ ». Une idée construite et jamais observée sous P₀ n'a qu'une borne supérieure. p₀ = 0 (hors support) et 0 < p₀ ≤ τ ne se distinguent pas. Or F sépare explicitement ces deux cas dans son présupposé A4.
2. **Test de permutation avec 5 graines.** E1 exige p < 0,01 par un test de permutation apparié sur graines, avec au moins 5 graines (valeurs illustratives de F). Avec 5 paires, il n'existe que 2⁵ = 32 affectations de signe. La plus petite p-valeur unilatérale atteignable est 1/32, soit environ 0,03. Si le test est mené domaine par domaine, H_A1 est infalsifiable de ce côté par construction. F doit préciser que le test agrège domaines et graines, ou augmenter le nombre de graines.
3. **I1 regroupe plusieurs facteurs.** I1 combine hétérogénéité des familles, modèles de base, décodage contraint et déduplication ; I0 n'a que la déduplication. Un gain peut venir du seul décodage contraint. F ne précise pas si le contrôle négatif (clones avec variations d'invite) garde ce décodage.
4. **Sélection du « meilleur modèle unique » pour I0.** Si ce modèle est choisi sur les domaines ou l'audit du duel, I0 est surestimé et le duel est biaisé contre I1. S'il est choisi sur un pilote séparé, il faut le déclarer.
5. **Les mesures de valeur sont confondues avec la rareté.**
   - La « longueur minimale dans la classe » est en pratique le minimum observé, biaisé en faveur des classes fréquentes, comme en E, point 6.
   - Le gain de portefeuille se calcule contre « l'union des classes fréquentes validées ». Cet ensemble grossit avec le N du bras : il faut le figer sur le panel P₀.
6. **Dev et audit tirés du même générateur.** Pour des instances synthétiques tirées par graine, la « coupure temporelle » est sans objet. Si Φ_dev et Φ_audit sortent du même générateur d'instances, l'audit est dans la distribution de la recherche, et le qualificatif « hors distribution » n'est pas satisfait.
7. **Jeu étalonné de E4.** Les « idées rares valides » qui le composent sont vraisemblablement construites par les concepteurs. Le taux de faux négatifs qu'on y mesure ne se transporte pas aux idées rares du système.
8. **Pas de couverture simultanée pour Clopper-Pearson.** Avec K classes proches de τ, chacune certifiée au risque δ, on attend environ δK fausses certifications de rareté.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Certification.** Pour k = 0, la borne supérieure vaut environ ln(1/δ)/N₀ par classe, ou ln(K/δ)/N₀ en simultané. Si N₀ · τ ≲ ln(K/δ), aucune certification n'est possible.
- **Chao1.** Il est indéfini si f₂ = 0, et sa variance explose quand f₁ ≫ f₂. Une variante corrigée du biais existerait (référence à vérifier).
- **UCB.** La garantie de regret suppose des récompenses stationnaires. Or « classes rares nouvelles » décroît par construction, puisque chaque découverte épuise le bras. La non-stationnarité est structurelle, et la garantie citée (Auer et al., 2002, selon F) ne s'applique pas.
- **E-values d'audit.** Elles exigent une loi des scores sous le nul « non valide ». Pour un audit déterministe, cette loi n'est pas définie sans calibration sur des fausses échangeables, ce qui ramène au transport du contrôle vers la queue.

### (c) Contrôles négatifs dont l'absence est fatale

- **A/A** (absent).
- **Idée hors support injectée** (absent) : une idée valide construite, soumise à la procédure de rareté.
  - Si la procédure est saine : verdict « non certifiable », car p₀ = 0 et p₀ ≤ τ sont indistinguables.
  - Si elle rend « rare » : la procédure confond hors-support et puits.
- **Générateur d'audit décalé** (absent) : audit tiré d'une famille d'instances différente de celle de dev.
  - Si la recherche ne surajuste pas : le rapport de transfert est stable.
  - S'il s'effondre seulement sous décalage : E2 était dans la distribution.
- **Descripteurs aléatoires, exclusion de motifs aléatoires, clones du meilleur modèle, variantes « gonflées »** (présents) : à conserver.

FIN-DE-CELLULE