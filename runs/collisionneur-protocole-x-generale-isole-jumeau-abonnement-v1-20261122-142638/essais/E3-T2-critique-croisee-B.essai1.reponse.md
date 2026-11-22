# Proposition B, tour III.2 : critique croisée de méthode

**Pièces.** Les pièces A, C, D et E sont présentes. Chacune se termine par FIN-DE-CELLULE puis par sa balise de fin, et aucune ne paraît coupée. Les empreintes sha256 figurent dans les balises, mais je ne les ai pas recalculées. FAITS et QUESTION ont la même empreinte et le même texte. Le bloc FAITS ne porte aucune étiquette de statut et je ne lui en attribue pas. Je n'ai fait aucune recherche et ne cite aucune référence nouvelle.

**Conventions.**
- (i) Tout nombre de cette cellule est illustratif, y compris ceux que je reprends des pièces. Seuls « deux mois » et « huit milliards » viennent des faits.
- (ii) Ce que je dis du contenu des pièces est une lecture du texte transmis, qu'on peut vérifier en le relisant. Mes diagnostics (confusions, effets produits par construction, fuites) sont des HYPOTHÈSE. Les résultats mathématiques que j'invoque sont rappelés de mémoire : statut RAPPORTÉ, sans source attribuée.
- (iii) Je ne modifie aucun statut posé par une pièce. Je signale ceux qu'aucune pièce transmise ne fonde.
- (iv) Notations de la partie (b) : n est le nombre d'unités indépendantes (tâches ou dossiers) ; s_t le score honnête d'un instrument à l'étape t ; ρ(h) l'autocorrélation de ce score à l'intérieur d'une trajectoire ; π la fraction d'étapes dégradées.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **k\* mêle la loi du défenseur et la stratégie de l'adversaire.** Avec l'adversaire (P), k est un résultat compté par script, pas une variable manipulée. Le décalage par acte μ peut dépendre du taux 1/r et de T, car une politique peut diluer chaque acte quand la tâche s'allonge. La pente de log k\* contre log T mesure alors γ − d log μ/d log T : l'exposant du défenseur se confond avec la dilution choisie par l'adversaire.
2. **Le dégât n'est pas k.** Le duel 1 juge en dégât D, les duels 2 à 6 en nombre d'actes. Si le dégât par acte dépend de la position ou de T, k\*(T) ne donne pas la frontière dégât-détection demandée par la question.
3. **Fuite d'horizon dans le duel 6.** Le seuil est calibré « à 5 % pour chaque T » sur des trajectoires honnêtes. À T ∈ {64, 128}, cette calibration utilise des données de l'horizon testé, qui renseignent sur τ et sur la dépendance entre étapes. La prédiction « sans réajustement » n'est hors échantillon que si le seuil est lui aussi prédit à partir de T ≤ 16.
4. **Comparateur faible dans le duel 6.** Le prédicteur naïf (dégât ∝ T) est ajusté à T ≤ 16 puis extrapolé d'un facteur 8. Il perd contre n'importe quelle loi courbée, si bien que H_A peut l'emporter sans que l'unité commune apporte rien.
5. **Le duel 3 est en partie vrai par construction.** Dans le modèle de A, le gain de l'appariement dépend de τ/σ, qui ne concerne que la loi honnête. La manipulation « hétérogénéité » fait varier τ directement, et la saturation en m découle de la forme algébrique 1+1/m. Le duel teste une décomposition de la variance honnête, pas une propriété de l'adversaire, qui n'observe pas m.
6. **Coïncidence n'est pas coordination (duel 4).** Des copies portant la même LoRA (P), sur le même préfixe, coïncident dès que leur choix d'étapes a peu d'entropie. κ dépend alors de la température d'échantillonnage. Lire κ > 0 comme « des copies se coordonnent sans communiquer » confond une politique partagée presque déterministe avec une coordination.
7. **La sonde peut lire l'adaptateur.** Si le témoin vient du modèle de base et l'acte dégradé du modèle adapté, la sonde peut séparer les poids plutôt que le sabotage, et elle le fera sur toute étape du modèle adapté, dégradée ou non. A prévoit le piège « consigne présente, acte honnête », mais pas son équivalent pour la LoRA. Sont touchés les duels 1, 2 et 5 et le verdict « activations non redondantes ».
8. **Sélection dans le duel 5.** La règle « l'évidence dans X chute d'au moins 50 %, sinon attaque échouée » ne retient que les adaptations réussies. Le rapport conjoint dépend alors de la corrélation honnête entre les deux moniteurs, que A ne rapporte pas.

### (b) Conditions où les mesures perdent leur puissance

- **Mémoire longue.** Si Var(Σ_{t≤T} s_t) ∝ T^{2H} avec H > 1/2 (autocorrélations non sommables), le bruit de l'agrégateur somme croît comme T^H. On obtient alors k\* ∝ T^H sans rien de propre à l'attaque. Le seuil 0,75 du duel 2 se compare donc à H et non à 0,5. Le duel est non jugeable si l'intervalle de Ĥ, estimé sur l'honnête, recouvre 0,75. Le contrôle (S) détecte ce cas, mais les règles de A ne disent pas qu'il rend le duel indécis.
- **Queues lourdes.** Si s_t relève d'une loi stable d'indice α < 2, la somme se normalise en T^{1/α} et γ tend vers 1/α. La standardisation par l'écart-type empirique ne définit alors plus la loi nulle.
- **Variance de k̂\*.** k\* est le point où la courbe détection(k) coupe 1/2. Par la méthode delta, Var(k̂\*) ≈ 1/(4n·p′(k\*)²), où p′ est la pente locale de cette courbe. La mesure est non jugeable quand la courbe est plate autour de 1/2.
- **Discrétisation.** Si k\*(T_min) vaut 0 ou 1, log k\* est indéfini ou dominé par l'arrondi. L'erreur relative du duel 6 souffre du même défaut quand k\* est petit.
- **Duel 3.** Si l'intervalle du gain non apparié, au dénominateur, contient 0, le rapport des gains n'est pas défini. Il faut tester une différence, pas un rapport.
- **Duel 4.** κ devient instable quand π est proche de 0 (paradoxe de prévalence). La marge de ± 0,10 n'est jugeable que si √(p(1−p)/n) est nettement plus petit.
- **Duel 6.** La médiane de quatre configurations par régime n'a pas d'intervalle utilisable. Le critère « intervalle d'un seul côté », que A applique au duel 2, n'est pas appliqué ici.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA neutre.** Un adaptateur de même rang et de même budget d'entraînement, sur objectif bénin, plus les étapes non dégradées de (P), comparés au témoin de base. La sonde doit rester au hasard.
2. **μ_P(T) mesuré à chaque T** sur témoins appariés. S'il varie avec T, le γ du duel 2 n'est pas l'exposant du défenseur.
3. **Au duel 6, seuil prédit et non recalibré**, avec le taux de fausses alertes effectivement obtenu.
4. **Copies honnêtes à température identique**, plus des copies (P) à deux températures. Si κ suit la température, le duel 4 mesure l'entropie de la politique.

A prévoit déjà les contrôles honnête contre honnête, (S) à décalage nul, moniteur factice et test d'échange.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duel 3 : hypothèses non exhaustives, recherche asymétrique.** H_A exige un λ\* qui franchit trois seuils. H_B exige que toute baisse d'AUROC sur les activations entraîne soit une AUROC texte+comparaison au-dessus du seuil haut, soit un ΔU sous le seuil bas. Les zones intermédiaires ne relèvent d'aucune des deux, et aucune zone indécise n'est déclarée. Surtout, l'absence de λ\* est conclue d'une grille bornée (six λ et trois graines) : un optimiseur faible suffit à « établir la loi de conservation ». C'est une absence de preuve lue comme une preuve.
2. **Fuite de l'adversaire vers la sonde.** Les sondes MLP sont « ré-entraînées par validation croisée sur des familles de tâches disjointes ». Le texte ne dit pas si elles sont ajustées sur l'adversaire même qu'elles doivent détecter. Disjoindre les tâches ne disjoint pas l'adversaire.
3. **Duel 1 en partie produit par construction.** Le saboteur est contraint à un score textuel par étape sous le centile 95 honnête. Cette troncature affaiblit mécaniquement le comparateur textuel cumulé, et ΔAUROC > 0 en découle en partie. La sonde peut aussi lire la LoRA ou la consigne, comme chez A. Enfin, H_A affirme un mécanisme (« sans état interne ») alors que la métrique ne teste que ce qu'une sonde détecte : son échec ne prouve pas l'absence d'état.
4. **Duel 2 : la perturbation est taillée sur la géométrie honnête.** Un bruit orthogonal au sous-espace principal des activations honnêtes épargne l'honnête par construction. Il frappe tout calcul situé hors de ce sous-espace, y compris un simple décalage dû à l'adaptateur. Un R_div élevé est donc attendu pour tout modèle qui s'écarte de ce sous-espace, saboteur ou non. Comme cette intervention porte sur les activations, elle fait aussi passer l'instrument de l'article 2 dans le champ de l'article 3.
5. **Duel 4 : l'adaptativité se confond avec le couplage.** La cascade est séquentielle et adaptative, alors que son comparateur répartit le budget en fractions fixes. Le gain peut venir de l'adaptativité seule, obtenue avec un seul signal. Et si les seuils de la cascade sont réglés sur les saboteurs du duel 3, qui figurent aussi dans le flux de test, il y a fuite.
6. **Métrique mal définie.** « ΔAUROC à t = 12 à un taux de fausses alertes fixé » mélange une mesure sans seuil et un point de fonctionnement. Il faut choisir entre une AUROC partielle et un taux de détection à taux de fausses alertes fixé.
7. **Statuts (je n'en change aucun).** VÉRIFIÉ est posé sur une conséquence d'un seuil illustratif (partie c, moniteur de texte). OBSERVÉ-NON-AUDITÉ est posé sur l'auto-correction des erreurs des modèles. Aucune pièce transmise ne fonde l'un ni l'autre.

### (b) Conditions où les mesures perdent leur puissance

- **Dérive de position.** Si E[s_t | honnête] dépend de t (les activations varient avec la longueur du contexte), ou si ρ(1) > 0, le délai moyen avant fausse alarme du CUSUM tombe sous sa valeur nominale. L'avantage du CUSUM à t fixé se confond alors avec la position. La mesure est non jugeable sans stationnarité de s_t en t.
- **ΔAUROC apparié.** Sa variance dépend de la corrélation entre les deux scores sur les mêmes trajectoires et du nombre n₁ de saboteurs retenus après sélection. Si n₁ est petit, une borne inférieure strictement positive est hors d'atteinte.
- **Existence de λ\*.** On retient le meilleur de G points (λ × graines). Sous un bruit d'estimation d'écart-type σ_A, la probabilité qu'un point franchisse les trois seuils par hasard croît avec G. Sans correction de multiplicité, cela biaise vers H_A.
- **R_div.** Pour ce rapport de moyennes, la méthode delta donne une variance ∝ Var(D_s)/E[D_h]², où D_h est la divergence honnête et D_s la divergence sous sabotage. Elle explose quand E[D_h] est proche de 0, par exemple sur des tâches factuelles à faible entropie.
- **Duel 4.** La puissance du test apparié dépend du nombre de paires discordantes parmi n_s trajectoires sabotées. La zone comprise entre les deux seuils de ΔRappel n'est pas déclarée indécise.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA neutre de même rang** (duels 1 et 3).
2. **Bruit dans un sous-espace aléatoire de même dimension**, et même perturbation appliquée à un modèle honnête légèrement décalé (autre consigne de style, LoRA bénigne). Si R_div monte autant, la décorrélation ne détecte pas le sabotage.
3. **Cascade à signal unique** (texte seul) à budget égal. Si elle capte l'essentiel du gain, la conclusion « système indissociable » tombe.
4. **Permutation des vecteurs de signaux entre trajectoires d'une même classe** (duel 4). Elle détruit le couplage en conservant les distributions marginales.
5. **Pénalité λ contre une direction factice** (duel 3). Le contrôle prévu (honnête pénalisé) teste la capacité générale du modèle, pas l'effet de viser la sonde.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Pas d'adversaire, et un générateur commun.** Le dommage vient de perturbations placées par l'expérimentateur, sur les mêmes dossiers, dans les trois régimes. Le transfert « un régime laissé de côté » peut donc réussir parce que le processus qui crée le dommage est partagé, et non parce que les signaux prédisent une même quantité. D écarte lui-même l'extrapolation au sabotage spontané, et le cas « l'adversaire est l'agent » n'est pas testé.
2. **L'influence se confond avec la suspicion.** La cible est calculée sur le graphe connu du générateur. Une règle apprise peut gagner en retrouvant la centralité d'une pièce (position, dépendants visibles dans le texte) sans rien lire du sabotage. Le témoin « priorité au nombre de dépendants » n'apparaît que pour le placement des vérifications ; il doit faire partie de M dans G.
3. **Le moniteur visé est défini par la présentation.** Une restitution canonique peut effacer des indices de dommage autant que neutraliser une manipulation. L'effet de l'exposition se confond avec celui du format.
4. **Régime des copies.** Les contextes sont distincts et aucun adversaire n'est partagé : il n'y a pas de coïncidence d'actes adverses à mesurer.
5. **Le duel 1 dépend de l'échelle de la perte.** I est une interaction calculée sur une perte bornée. La saturation peut rendre I négatif : une seule décision suffit déjà à fausser une conclusion. Et le signe d'une interaction peut changer par transformation monotone, par exemple en logit. Sur une même chaîne, les décisions sont aussi forcément à des profondeurs différentes, ce qui gêne l'appariement des positions.

### (b) Conditions où les mesures perdent leur puissance

- **G est le minimum de six termes.** L'estimateur du minimum est biaisé vers le bas (E[min] ≤ min E), et le bootstrap d'un minimum n'est pas consistant quand deux termes sont égaux. La probabilité d'obtenir une borne inférieure positive se comporte comme un produit de Φ((δ_i − c·s_i)/s_i), où δ_i est la marge vraie du terme i, s_i son écart-type et c le quantile simultané. Avec un n modeste, l'issue attendue est « indécis », quel que soit l'état du monde.
- **Si les signaux n'ajoutent rien à la centralité**, c'est-à-dire si l'information mutuelle conditionnelle I(signaux ; ΔL | centralité, position) = 0, alors L_T = L_M dès que M inclut la centralité, et le premier terme de G vaut environ −b.
- **Duel 1.** Var(Î) contient la somme de k pertes isolées estimées et croît comme k·v/n, où v est la variance par décision. La marge n'est jugeable que si √(k·v/n) reste petit devant elle.
- **Perte rare.** Si P(conclusion fausse | perturbation) est faible, Var(L_M − L_T) est dominée par les dossiers sans dommage.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Règle aveugle aux instruments.** Même apprentissage, avec pour seules entrées la position, le type de pièce et la profondeur dans le graphe. Si elle transfère aussi bien, le transfert vient du générateur.
2. **Exactitude honnête égale sous les deux présentations**, comme condition d'admissibilité du régime visé. D en publie les bascules, mais n'en fait pas une condition.
3. **Perturbation à effet nul**, en même nombre et aux mêmes positions. Toute politique doit alors avoir le même L.

D prévoit déjà la permutation intra-dossier des priorités et le contrôle additif du duel 1.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Duel 1 : la furtivité textuelle est fixée par l'objectif d'entraînement.** L'adversaire est entraîné avec une pénalité de divergence de Kullback-Leibler (KL) par étape. À contexte égal, un moniteur qui lit une seule étape vérifie AUROC ≤ 1/2 + TV − TV²/2 (calcul direct), où TV est la distance de variation totale. Et l'inégalité de Pinsker donne TV ≤ √(KL/2). Une AUROC textuelle basse découle donc de l'entraînement ; seule la jambe Δ_dir est informative. La jambe sonde, à l'inverse, est biaisée vers la détection par l'adaptateur. AUROC_étape prend le maximum de deux biais de sens opposés.
2. **Duel 2 : le « résumé factuel neutre » est un oracle.** Rédiger un résumé factuel suppose de savoir ce qui est vrai. S'il est dérivé de la vérité terrain, l'exécution de comparaison emprunte sa puissance à la vérification coûteuse. S'il est rédigé par le modèle adverse, il peut porter le biais. La pièce ne fixe pas qui le rédige, alors que le couplage entre les articles 1 et 3 en dépend.
3. **Duel 2, autres confusions.**
   - L'entraînement anti-moniteurs peut à lui seul modifier la sensibilité au contexte.
   - L'égalité de Δ_dir entre politiques s'obtient en choisissant des points de contrôle de l'entraînement.
   - La mesure n'est faite que si l'évasion a réussi.
   - La normalisation z ne précise pas à quel modèle honnête elle se réfère.
4. **Règle de décision : la non-significativité vaut réfutation.** Aux duels 2, 3 et 4, un effet sous le seuil ou p ≥ 0,05 suffit à falsifier l'hypothèse. Un échantillon trop petit produit donc mécaniquement « articles distincts » au duel 4. Sans zone indécise, une erreur de seconde espèce se lit comme une réfutation, et la conception penche vers la séparation.
5. **Duel 3 : détecteur non spécifié.** On ne sait pas quel instrument produit la détection dans le débat. Sans équipe hétérogène, un échec du débat ne peut pas être attribué au partage des poids.
6. **Duel 4 : adaptativité contre couplage.** Le comparateur modulaire doit disposer de la même allocation séquentielle du budget, sans termes d'interaction. Sinon, le gain mesure l'adaptativité. Le transfert vers une famille d'adversaire non vue ne protège pas si l'une des deux familles est une LoRA que la sonde reconnaît.
7. **Statuts (je n'en change aucun).** VÉRIFIÉ est posé sur Wald (1945), pourtant cité de mémoire, et sur des éléments du cadre. Aucune pièce transmise ne contient la vérification correspondante.

### (b) Conditions où les mesures perdent leur puissance

- **Dépendance intra-trajectoire.** La taille effective des mesures par étape est n_eff = n·T/(1 + (T−1)ρ̄), où ρ̄ est la corrélation moyenne entre étapes d'une même trajectoire. Sans intervalles groupés par tâche, la précision est surévaluée. Le maximum de deux AUROC estimées est en outre biaisé vers le haut, d'un terme de l'ordre de leur écart-type.
- **Dilution au duel 2.** Si les étapes sondées sont choisies sans signal utile (les moniteurs étant contournés), l'effet observé vaut environ π·δ. La taille d'échantillon nécessaire croît alors comme 1/π².
- **Effet sur la variance seule.** Si l'évasion augmente Var(z_CF) sans en déplacer la moyenne, un test de moyenne n'a aucune puissance.
- **Dommage concentré.** Si la contribution des actes à Δ_dir est à queue lourde, Δ_dir franchit le seuil alors qu'il n'y a pas de régime diffus. A mesure la part du dégât portée par l'acte le plus nocif ; E ne la mesure pas.
- **Tests appariés des duels 3 et 4.** La puissance dépend du nombre de paires discordantes, faible quand les taux de détection sont proches de 0 ou de 1. Par la règle (a)4, ce manque de puissance « falsifie » H_A.
- **Calibration des seuils.** Si les seuils à 5 % des deux politiques sont calibrés sur des ensembles honnêtes différents, ou sur l'échantillon même, les taux de fausses alertes réels diffèrent. Les taux de détection ne sont alors plus comparés à fausses alertes égales.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA honnête entraînée avec la même pénalité anti-moniteurs sur des trajectoires non dégradées.** Si δz_CF monte aussi, le « déplacement de signature » vient de l'entraînement contre les moniteurs, pas du sabotage.
2. **Résumé rédigé sans accès à la vérité** (gabarit fixe ou modèle tiers), comparé à un résumé dérivé de la vérité. Si la divergence n'apparaît qu'avec le second, l'instrument est un oracle.
3. **Équipe hétérogène** au duel 3.
4. **Adversaire à décalage nul** passé dans toute la chaîne des duels 2 à 4 : δz_CF et l'écart entre politique conjointe et modulaire doivent être nuls.

E prévoit déjà le contrôle de bruit non dirigé au duel 1 et la permutation entre tâches au duel 4.

FIN-DE-CELLULE