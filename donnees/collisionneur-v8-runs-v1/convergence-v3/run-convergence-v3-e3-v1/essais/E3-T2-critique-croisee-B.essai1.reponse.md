# Proposition B — Tour III.2 : critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**A1. Confusion entre règle de mise à jour et jeu fictif.** La proposition A identifie correctement que la règle de A n'est pas le jeu fictif (trois raisons de code : inclusion de la loi cible, oracles approchés, attaquant myope). Mais elle construit ensuite les Duels 3 et 4 sur l'hypothèse que la *moyenne temporelle des moniteurs de A* pourrait converger au sens de Brown-Robinson — tout en ayant montré que les conditions de ce théorème ne sont pas réunies. Le Duel 3 demande de mesurer la NashConv de A̅ à T = 16 contre T = 8, mais **le NashConv restreint sous-estime systématiquement l'exploitabilité vraie** (déclaré dans le texte de A, mais non absorbé dans la construction du duel). HYPOTHÈSE : une décroissance de NashConv restreint de T = 8 à T = 16 pourrait tenir simplement parce que la matrice 17 × 17 offre plus de colonnes au solveur, sans que la défense moyenne soit moins exploitable par un attaquant hors matrice. Le duel confond donc un artefact d'enrichissement de la matrice avec une convergence dynamique.

**A2. Variable confondante dans le Duel 1.** Le bras A_q (moniteur entraîné contre q, l'équilibre de l'attaquant de B) est présenté comme testant « la distribution d'entraînement ». Mais A_q et A diffèrent sur **deux** axes : la distribution d'entraînement (q contre uniforme) et le jeu d'attaques sur lequel q est défini (les attaques de B, pas celles de A). VÉRIFIÉ dans le code : les attaques de B et de A divergent dès le tour 1, car leurs moniteurs sont différents. Un A_q qui bat A pourrait donc simplement refléter que les attaques de B couvrent mieux l'espace, pas que la distribution q est supérieure. Pour isoler l'effet, il faudrait un bras A_q_propre entraîné contre le q calculé sur la matrice des moniteurs *de A* eux-mêmes — bras absent de la proposition.

**A3. Le Duel 2 repose sur une permutation dont la validité est douteuse.** HYPOTHÈSE : la nulle par permutation des 8 déplacements teste « l'ordre compte ». Mais les déplacements ne sont pas échangeables même sous H_B (la proposition le reconnaît pour D et B′ via le départ chaud). Plus fondamentalement, avec T = 8 tours, il y a 8! = 40 320 ordres, dont seuls ≈ 2,5 % (≈ 1 008) donnent I3 au-dessus du 97,5e percentile. Avec seulement 24 instances, le test « part des tâches où I3 dépasse le quantile 0,975 de la permutation > 0,5 » n'a de puissance que si l'effet est très grand. Aucun calcul de puissance n'est donné. HYPOTHÈSE : la puissance est insuffisante pour les tailles d'effet plausibles si les déplacements sont faiblement dépendants (ni i.i.d. ni strictement cycliques).

**A4. Le « contrôle négatif » du Duel 1 (D − A = +0,36) n'est pas un contrôle négatif.** Un contrôle négatif doit montrer que l'instrument ne détecte pas de différence quand il n'y en a pas. D − A montre que l'instrument détecte une différence quand il y en a une (c'est un contrôle *positif*). Le contrôle négatif serait A_moy construit sur 9 copies de M0, qui doit donner V(M0) — c'est effectivement proposé, mais classé comme « contrôle mécanique », pas comme contrôle négatif. L'absence de vrai contrôle négatif du Duel 1 (un bras dont on sait que le conteste doit être nul) est une lacune.

### (b) Conditions de perte de puissance ou de non-jugeabilité

**Duel 1.** La métrique max_X V(X) − V(A) perd sa puissance si tous les moniteurs linéaires déployés seuls ont une V similaire contre leur meilleure réponse respective. Condition probabiliste : si la valeur minimax du jeu restreint à la classe linéaire pure (un seul hyperplan déployé) est constante à ε près pour tout hyperplan entraîné sur n'importe quelle distribution supportée dans Θ_δ, alors max_X V(X) − V(A) ≈ 0 *par construction*, et le duel ne distingue plus capacité de dynamique. Cela arrive quand δ est assez grand pour que toute attaque contourne tout hyperplan unique à un taux proche de α (ce qui est déjà presque le cas à δ = 1,6, où V(A) = 0,036 ≈ 3,6α [RAPPORTÉ]).

**Duel 3.** Le NashConv restreint devient non jugeable quand la matrice des gains est mal conditionnée (colonnes presque colinéaires) : le programme linéaire reste résolu, mais les poids d'équilibre deviennent instables numériquement. Condition : si les 9 attaques de A tombent dans un sous-espace de dimension ≤ 2 de ℝ^{Kd} = ℝ^{18}, la matrice 9 × 9 a un rang effectif ≤ 2, et la valeur restreinte dépend de perturbations d'arrondi. Les pièces ne rapportent pas le rang effectif de la matrice de A.

**Duel 5.** Réduire unites_Bp à 2 change à la fois la classe de fonctions *et* la capacité de chaque moniteur d'entraînement à capturer le signal. Si un maxout à 2 unités détecte mal même une seule attaque (parce que 2 unités linéaires en dimension 6 avec K = 3 composantes n'offrent que 14 paramètres, dont 12 pour les poids et 2 pour les biais), alors V(B′₂) et V(D₂) sont tous deux au plancher, et l'écart B′₂ − D₂ est dominé par le bruit. La condition testable est V(D₂) ≥ V(A) + m aux deux δ ; si elle échoue, Q2 à m = 2 est triviale et non exercée.

### (c) Contrôles négatifs absents

1. **Bras « M0 gelé » (A0)** est proposé mais non exécuté. Son absence est déclarée comme un manque dans les pièces, mais la proposition A le traite comme un futur bras sans garantir qu'il sera fait avant les duels. Si V(A) ≈ V(A0), tout le récit de « non-convergence dynamique » s'effondre en un constat de plafond de classe — l'absence de A0 avant les duels rend toute interprétation causale non falsifiable.

2. **Contrôle de l'attaquant : retirer le départ vers l'origine.** Proposé dans le Duel 2 mais comme un contrôle « si I3 s'effondre ». Ce contrôle devrait être une condition préalable, pas un post-hoc optionnel. Sans lui, on ne sait pas quelle fraction de I3 vient de la structure géométrique des départs plutôt que de la dynamique.

3. **Contrôle de la métrique V elle-même.** Aucun bras à V connu analytiquement (par exemple un moniteur de Bayes sur le mélange à 3 composantes, calculable en dimension 6 pour des gaussiennes) n'est proposé. Sans ce calibrage absolu, V reste une borne haute de statut inconnu.

---

## Sur la proposition C

### (a) Défauts de méthode

**C1. L'Expérience 1 confond capacité et dynamique par construction.** L'Expérience 1 mesure D_train(A) = (1/T)Σ H_A[T, t−1], le taux de détection du moniteur final de A sur les attaques mêmes de son entraînement. La proposition C déclare que si D_train(A) < 0,20, alors H_B (instabilité dynamique) est falsifiée. Mais un moniteur linéaire entraîné par un objectif lissé avec 8 départs (VÉRIFIÉ) sur un mélange de 9 attaques en dimension 6 peut fort bien échouer à dépasser 0,20 sur ce mélange *pour des raisons d'optimisation*, pas seulement de capacité géométrique. La variable confondante est la qualité de l'optimiseur d'entraînement. Le seuil de 0,20 est déclaré mais non justifié par un calcul de capacité (quel est le taux de détection maximal d'un hyperplan optimal sur ce mélange ?).

**C2. L'Expérience 2 (C3p_support) suppose que la dilution est le seul mécanisme, sans le tester isolément.** C3p_support retire les moniteurs de poids nul de C3′ puis recalibre le « ou » sur les survivants. Mais cette opération change deux choses à la fois : le nombre de composantes du log-somme-exp *et* le seuil de calibration. Si C3p_support ≈ B′, on ne sait pas si c'est parce que la dilution était le seul problème ou parce que le nouveau seuil compense un autre effet. Il faudrait aussi un témoin C3_tous_recalibre (« ou » de *tous* les moniteurs, même seuil que C3p_support) pour isoler l'effet du nombre de composantes de celui du seuil.

**C3. L'Expérience 3 change simultanement la classe (m = 2 au lieu de 9) et le rapport classe/horizon.** La proposition le reconnaît partiellement (« sous-paramétrisation stricte par rapport à l'horizon »), mais ne contrôle pas pour l'effet de la capacité brute sur V. HYPOTHÈSE : à m = 2, V(D₂) peut être si faible que toute comparaison B′₂ − D₂ est dominée par le plancher. Le contrôle « pour unites_Bp = 1, B′₁ reproduit B et D₁ reproduit A au bit près » est correct mais insuffisant : il vérifie la plomberie du code, pas la puissance de la comparaison à m = 2.

**C4. Le tableau des mécanismes (a)-(g) présente des jugements de « déjà réfuté » qui ne tiennent pas.** Le mécanisme (a) est déclaré « déjà réfuté en déploiement pur par A ». Mais le jeu fictif ne promet la convergence qu'en *déploiement mixte* (stratégies moyennes), pas en déploiement pur — la proposition A le dit explicitement. Dire que (a) est « réfuté » par A revient à réfuter une prédiction que le théorème ne fait pas. De même, (b) est déclaré « déjà réfuté pour Q1 » parce que B − C3 < 0, mais la question n'est pas si B bat C3 en V(iii) : c'est si le double oracle converge vers l'équilibre du jeu, ce qui n'est pas mesuré par V(B) − V(C3).

### (b) Conditions de perte de puissance ou de non-jugeabilité

**Expérience 1.** Le seuil D_train(A) = 0,20 (falsification de H_B) et V(A_JF-bilatéral) − V(A) = 0,05 (falsification de H_A) sont asymétriques : le premier exige une mesure positive forte, le second un effet d'intérêt trois fois plus grand que m. HYPOTHÈSE : si D_train(A) est dans l'intervalle [0,20; 0,25] et V(A_JF) − V(A) dans [0,02; 0,05], aucune hypothèse n'est falsifiée. Or cet intervalle est plausible : D_train(A) à δ = 1,4 devrait être autour de 0,15–0,30 (8 composantes à séparer de N(0,I) en dimension 6 avec un hyperplan, HYPOTHÈSE illustrative). Le duel est donc possiblement non tranché.

**Expérience 2.** La mesure Δ(B′, C3p_support) perd sa puissance si le support de B′ est de taille 1 dans la majorité des tâches (les tâches pures de B′ = 71 % à δ = 1,4 [RAPPORTÉ]) : sur ces tâches, C3p_support se réduit à un seul moniteur et coïncide avec B′, ce qui tire la moyenne vers zéro. Le signal vient uniquement des 29 % de tâches non pures, soit ≈ 7 tâches sur 24 au pilote. L'erreur-type du contraste sur 7 tâches est vraisemblablement ≫ m = 0,02.

**Expérience 3.** La condition de validité (part_pure ≤ 0,20) est un critère de conception, pas un résultat : si m = 2 produit encore des poids purs (ce qui est plausible si l'attaquant local ne génère que 2 directions effectives en 8 tours), l'expérience est non jugeable. Aucune garantie théorique n'est donnée que m < K × T suffise à forcer un équilibre intérieur dans ce jeu spécifique.

### (c) Contrôles négatifs absents

1. **Pas de contrôle de l'objectif d'entraînement.** L'Expérience 1 attribue le cycle à la « saturation géométrique de W₁ », mais ne contrôle pas pour la possibilité que l'objectif lissé (`objectif_detection`) converge vers un autre hyperplan que la meilleure réponse dure. Un contrôle : entraîner A avec l'objectif logistique (déjà implanté, VÉRIFIÉ : `entrainement = "logistique"` dans le code) et comparer D_train. Si le résultat change, la cause est l'objectif, pas la géométrie.

2. **Pas de contrôle de la calibration du seuil.** Le seuil t_α est recalculé à chaque tour sur le même Xcal (VÉRIFIÉ). Si Xcal est petit par rapport à la variance du quantile, le seuil fluctue et contribue au « cycle » apparent. Aucun contrôle avec un Xcal beaucoup plus grand (par exemple 200 000) n'est proposé.

3. **Pas de matrice à équilibre intérieur connu pour valider le solveur.** La proposition C mentionne Gambit mais ne l'intègre pas comme contrôle négatif systématique. Pour un jeu 9 × 9 synthétique à équilibre intérieur connu analytiquement, `resoudre_jeu` doit retrouver les poids et la valeur à la tolérance déclarée.

---

## Sur la proposition D

### (a) Défauts de méthode

**D1. Sous-spécification des expériences.** Les expériences E0-E4 sont des cadres, pas des protocoles exécutables. E1 demande de construire « la mixture uniforme de ses moniteurs et l'équilibre de leur jeu restreint » sur la trajectoire de A, sans préciser comment l'équilibre restreint de A sera calculé (les moniteurs de A n'ont pas de matrice de gains croisés dans le code actuel — la matrice G n'est construite que pour B et B′, VÉRIFIÉ). L'absence de cette matrice pour A est un obstacle d'implémentation non déclaré.

**D2. Fuite potentielle dans E3.** E3 demande de « définir le gain d'une extension défensive indépendante, à classe inchangée et budget de recherche préfixé » sur les tâches pures. Mais « extension défensive indépendante » n'est pas définie : s'il s'agit d'ajouter un moniteur entraîné sur de nouvelles attaques fraîches, cela change la bibliothèque d'attaques (et donc le jeu restreint). Si c'est un moniteur entraîné sur les attaques existantes avec un nouveau départ aléatoire, le gain mesure la sous-optimalité de l'optimiseur, pas le plafond de classe. La variable confondante « source des attaques d'entraînement » n'est pas contrôlée.

**D3. Le critère de convergence proposé (gap de selle) n'est pas calculable dans ce jeu.** La proposition le reconnaît (« un petit gap local n'atteste pas un petit gap global ») mais propose néanmoins le gap comme métrique principale. VÉRIFIÉ : le supremum sur m ∈ M_α et l'infimum sur θ ∈ Θ_δ sont des optimisations en dimension continue avec des objectifs non convexes. Le code n'a accès qu'à des bornes du gap, pas au gap lui-même. La proposition ne dit pas comment distinguer un gap apparemment faible (parce que les optimiseurs sont faibles) d'un gap réellement faible.

### (b) Conditions de perte de puissance ou de non-jugeabilité

**E1.** La mesure « NashConv restreint des derniers et moyens itérés » devient non jugeable si la matrice 9 × 9 de A est proche du rang 1 (un seul moniteur domine, ou une seule attaque est difficile). Dans ce cas, l'équilibre restreint est trivial (masse 1 sur le moniteur dominant), le NashConv est nul par construction, et le test ne distingue pas convergence de dégénérescence. Condition : rang effectif de la matrice ≤ 2 (les valeurs singulières sont calculables sur les données du pilote, mais non rapportées).

**E2 (factoriel minimal).** Le factoriel 2 × 2 (attaquant myope / historique × défenseur approché / exact) a 4 cellules. Avec 24 instances par cellule et des effets bruités, la puissance d'une interaction (le « aucune explication simple si persistance dans les quatre cellules ») est très faible. Aucun calcul de puissance n'est donné. HYPOTHÈSE illustrative : pour détecter une interaction de taille 0,03 sur V avec un écart-type par tâche de 0,10 et 24 instances, la puissance est ≈ 0,15.

**E4.** Le transfert réel « conditionné au succès synthétique » est non jugeable si le succès synthétique n'est pas défini avec un seuil préenregistré. La proposition dit « un gain réel préenregistré et audité falsifie H_B », mais le « gain préenregistré » n'a pas de valeur numérique.

### (c) Contrôles négatifs absents

1. **Pas de contrôle négatif explicite pour E1.** Le moniteur figé M0 est mentionné dans le protocole commun, mais la proposition D ne dit pas ce que M0 doit donner sur les mesures de E1 (quel NashConv restreint ? quelle V ?). Sans cette prédiction, on ne peut pas vérifier que l'instrument ne déclare pas un succès sur un bras inerte.

2. **Pas de contrôle de l'optimiseur côté attaquant.** E2 varie l'attaquant (myope / historique) et le défenseur (approché / exact), mais ne contrôle pas la qualité de l'optimiseur SLSQP de l'attaquant. Si l'attaquant « historique » est aussi résolu par SLSQP local, il peut échouer à trouver la meilleure réponse au mélange (problème plus dur que la réponse au dernier moniteur), et toute réduction du cycle pourrait refléter un attaquant plus faible plutôt qu'une meilleure dynamique.

3. **Pas de matrice synthétique de calibration dans E3.** Pour vérifier que le programme de non-unicité fonctionne, il faut une matrice à équilibre intérieur strict *et* une à ligne dominante, avec des valeurs connues analytiquement. La proposition le mentionne mais comme un « contrôle » non spécifié, pas comme une condition préalable.

---

## Sur la proposition E

### (a) Défauts de méthode

**E1. Le critère v_mix − v_pur est vrai par construction dans la classe linéaire.** VÉRIFIÉ : pour les moniteurs linéaires de B, les poids ne sont jamais purs (support 3,7 [RAPPORTÉ]), donc v_mix > v_pur dans le jeu restreint 9 × 9 de B. La proposition E propose ce critère comme test de « posabilité du mélange ». Mais v_mix > v_pur est une propriété de la matrice G du jeu restreint, qui dépend des moniteurs et attaques effectivement générés. HYPOTHÈSE : si l'on change la racine ou l'horizon, la même classe peut produire une matrice où v_mix = v_pur. Le critère est donc instable et ne caractérise pas la classe de fonctions, mais l'instance.

**E2. La proposition ne distingue pas les niveaux de mesure.** Le « tableau de bord proposé » (gap certifié, détection robuste, désaccord fonctionnel, I1/I3 descriptifs) mélange des quantités de statut très différent : le gap certifié est un objet théorique non calculable dans ce jeu (la proposition E le reconnaît : « gap restreint ou empirique, explicitement nommé, ailleurs »), tandis que la détection robuste est un chiffre calculé par le code. Le risque est que le lecteur traite le gap restreint comme s'il avait la même force probante que le gap exact.

**E3. L'intervention « historique bilatéral » est proposée sans spécifier l'implémentation.** Le tableau des mécanismes dit « conservation de l'historique des deux côtés ; comparer à A ; témoin négatif : répéter des éléments sans modifier leurs poids effectifs ». Mais « historique bilatéral » signifie que l'attaquant répond au mélange uniforme des moniteurs passés — ce que le code actuel ne fait *pas* pour l'attaquant (VÉRIFIÉ : l'attaquant de chaque bras répond à la défense déployée, qui pour A est le dernier moniteur). Implémenter cette variante exige de modifier `objectif_lisse` pour qu'il prenne une mixture côté défenseur dans la boucle *de l'attaquant*, pas seulement dans celle du défenseur. C'est faisable mais non trivial et non déclaré.

### (b) Conditions de perte de puissance ou de non-jugeabilité

**Expérience « mesure ou dynamique ? »** Le duel H_A (gap du dernier profil > 0,02) contre H_B (≤ 0,02) perd sa puissance si le gap ne peut être calculé qu'en version restreinte, et si la matrice restreinte sous-estime l'exploitabilité. Condition : si l'attaquant indépendant (S17) trouve un V significativement inférieur à celui de la meilleure réponse standard (ce qui n'est pas le cas au pilote, écart ≤ 0,0011 [RAPPORTÉ]), le gap restreint est trompeur. Plus généralement, la puissance du test est bornée par la qualité de l'optimiseur d'attaque, pas seulement par N.

**Expérience « plafond de classe ou bibliothèque incomplète ? »** Le contrôle négatif (réinsérer des copies des moniteurs existants) est correct mais l'expérience perd sa puissance si le « budget de recherche préfixé » est trop faible pour trouver un moniteur d'extension significatif. HYPOTHÈSE : dans la classe linéaire en dimension 6, tout nouvel hyperplan entraîné sur les mêmes 9 attaques est probablement proche de l'un des 9 existants (espace de dimension 7 pour 9 attaques en ℝ^6). Le gain d'extension est alors nul par saturation du sous-espace, pas par plafond de classe au sens fonctionnel.

**v_mix − v_pur.** Ce critère devient non jugeable si la matrice G est estimée avec bruit (les gains sont des taux de détection estimés sur des échantillons finis). Si l'écart v_mix − v_pur est de l'ordre de 0,01 (comparable à l'erreur d'estimation des entrées de G), la conclusion « mélange nécessaire » ou « non nécessaire » dépend de l'arrondi. Aucune propagation de l'incertitude des entrées de G vers v_mix − v_pur n'est proposée.

### (c) Contrôles négatifs absents

1. **Pas de contrôle du gap sur un jeu à solution connue.** Le gap de selle est proposé comme métrique principale, mais aucun jeu synthétique à gap connu analytiquement n'est spécifié pour valider le calcul. Le jeu jouet (protocole en 5 lignes) mentionne « pile-ou-face apparié d'OpenSpiel » mais ne donne pas le gap attendu numériquement (il est 0 à l'équilibre et ≈ 0,5 sous la meilleure réponse pure cyclique, VÉRIFIÉ algébriquement).

2. **Pas de contrôle négatif pour le « désaccord fonctionnel ».** Le tableau de bord propose de mesurer le désaccord fonctionnel entre moniteurs sur une banque tenue à l'écart. Mais aucun seuil n'est donné pour distinguer un désaccord attendu (les moniteurs sont entraînés sur des distributions différentes) d'un désaccord pathologique. Un contrôle négatif serait : le désaccord fonctionnel entre 9 copies du même moniteur (M0) doit être nul.

3. **Pas de contrôle de l'extraction d'activations pour le transfert réel.** La proposition E mentionne « extraction et évaluation : 8–24 heures GPU » mais ne donne pas de contrôle vérifiant que les activations extraites sont stables (par exemple, deux extractions du même prompt donnent la même activation au bit près en mode déterministe). Sans ce contrôle, le bruit d'extraction peut dominer le signal des sondes.

FIN-DE-CELLULE