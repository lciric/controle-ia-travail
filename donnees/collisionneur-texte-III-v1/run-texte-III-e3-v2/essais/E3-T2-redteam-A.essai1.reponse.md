# Tour III.2 — Critique croisée de méthode (proposition A)

Les trois pièces B, C, D sont présentes et complètes (chacune se termine par sa ligne de clôture). Je ne les résume pas ; je critique estimateurs, définitions et plans de mesure. Tout chiffre non issu des faits est illustratif. Un constat transversal précède les sections : aucune des trois pièces ne traite la **direction** de la non-bijectivité (fait 5 : une unité d'Argon → deux unités d'Opus, lecteur de la lignée d'Opus, fait 6). Or une scission côté Opus peut être un artefact de lecture (le lecteur distingue mieux les formulations de sa lignée) autant qu'une propriété des familles ; sans mesure de l'asymétrie d'appariement, m = 18 et m = 19 ne sont pas deux conventions mais deux hypothèses sur le lecteur.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Duel 1, contradiction interne sur le signe du biais.** L'issue qui « falsifie H_A » est « LP surestime N dans les mondes hétérogènes » ; le bloc 1(d) de la même pièce affirme que l'hétérogénéité fait **sous-estimer** N. Le duel n'est pas jugeable tant que le sens attendu n'est pas fixé. De plus, H_B compare une **borne inférieure** (Chao) à un estimateur ponctuel (LP) sur le critère « biais relatif » : une borne inférieure a un biais négatif par construction ; la métrique avantage LP par construction dans les mondes homogènes et ne mesure pas ce qu'on veut (la couverture de la borne).
2. **Duel 2, vrai par construction.** La « puissance de discrimination » exige de définir une « défense non universelle ». Si on la définit par une proportion de familles sous τ, la définition par proportion gagne ; si on la définit par un minimum sous τ, le pire cas gagne. Le duel ne compare pas deux définitions, il compare chaque définition à son propre critère. Le contrôle négatif (« échoue sur exactement une famille sur k ») est en fait un cas discriminant, pas un contrôle.
3. **Duel 3, non identifiable et contrôle négatif erroné.** Avec deux listes, la table 2×2 a une cellule (non vue, non vue) inobservée ; le χ² d'indépendance n'est pas calculable sans hypothèse sur cette cellule (D le dit correctement). Le contrôle négatif proposé, « partition aléatoire d'un ensemble unique », produit deux listes **disjointes** (m = 0), c'est-à-dire une dépendance négative maximale, pas l'indépendance. Le contrôle valide est un tirage de deux listes par deux lois de Bernoulli indépendantes sur le même ensemble.
4. **Fuite entre régime informé et cloison.** 1(b) donne au banc informé « les familles vues », puis la cloison interdit que « la liste des familles d'entraînement » passe aux concepteurs de familles tenues à l'écart. Si le banc informé et les concepteurs sont les mêmes instances, la cloison est violée ; sinon il faut dire qui est qui.
5. **Convention m = 19 avec n₁ = 28 : unités mélangées.** B retient m = 19 parce que la famille recouvrante « fournit deux appariements », mais garde n₁ = 28 ; en grain fin, n₁ doit être recompté (C et D le relèvent). Le chiffre retenu n'est dans aucune unité cohérente.
6. **Budget par famille arithmétiquement faux.** « 100 éléments pour ±5 % (Clopper-Pearson) » : à p̂ = 0,5, la demi-largeur est ≈ 1,96·√(0,25/100) ≈ 0,10 (approximation normale, calcul refaisable) ; ±0,05 demande ≈ 400 éléments (illustratif). Le budget est sous-dimensionné d'un facteur 4.
7. **Q1 et Q2, confusion entre calibration et déplacement de loi.** Q1 valide N̂ si « la proportion de familles extérieures non appariées tombe dans l'IC prédit » ; cela ne tient que si les familles extérieures sont tirées selon la **même loi de découverte** que les sources internes, ce que l'option (i) du bloc 2 exclut par définition (conçues par d'autres). Un échec de Q1 ne distingue pas « N̂ mal calibré » de « loi extérieure différente ». Q2 a le même défaut : l'écart vu/écart mesure conjointement la généralisation de la défense et le déplacement entre deux mécanismes de découverte (familles vues issues d'une source, familles tenues à l'écart issues de cinq autres).
8. **Q4, mesure d'accord inadaptée.** Le kappa de Cohen/Fleiss porte sur des étiquettes catégorielles par unité ; l'appariement est un graphe biparti non bijectif. L'accord doit se mesurer au niveau des arêtes (accord sur chaque lien possible), sinon la scission 1→2 n'a pas de codage.
9. **Fuite non traitée dans l'instrument 2.** « Éléments honnêtes appariés » servent à mesurer les fausses alertes sans dire s'ils ont servi à fixer les seuils. S'ils ont servi, le taux de fausses alertes est biaisé vers le bas par construction.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Duel 1 : si le coefficient de variation des probabilités de capture tend vers 0, ou si la couverture n_obs/N tend vers 1, LP et Chao convergent et le duel ne tranche rien. Si Q₂ = 0 (aucune famille vue par exactement deux sources), Chao sous sa forme de base est indéfini.
- Duel 3 : avec K listes et 2^K − 1 cellules observables pour ≈ 40 familles (illustratif), les effectifs attendus par cellule sont < 5 ; le χ² asymptotique est invalide, le test est non jugeable sans test exact ou regroupement déclaré d'avance.
- Définition γ (proportion) : avec k familles sans échec, la borne sur ε est non informative dès que k < ln α / ln(1 − ε) ; avec grappes de familles corrélées, k doit être remplacé par le nombre de grappes.
- Écart vu/écart : si la variance inter-familles σ²_inter dépasse δ², la puissance d'un test d'équivalence sur |Δ| ≤ δ tend vers zéro quel que soit le nombre d'éléments par famille.
- Kappa (Q4) : si la proportion de paires effectivement liées est faible (graphe creux), le kappa est bas malgré un accord brut élevé (paradoxe du kappa) ; le seuil 0,70 devient non interprétable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Monde sans masse manquante** (N = n_obs) : l'estimateur doit rendre ≈ n_obs ; toute masse manquante détectée est une fausse alerte. Absent chez B.
- **Deux listes issues de deux exécutions du même modèle** : le test d'indépendance doit rejeter ; sinon il n'a aucune puissance contre la dépendance qui compte ici.
- **Lecteur d'appariement testé sur une liste et sa copie permutée** (doit donner m = n) et sur deux listes sans lien possible (doit donner m = 0) : mesure du taux de faux liens et de liens manqués du lecteur, préalable à toute correction d'appariement.
- **Défense constante** (score indépendant de l'entrée) : la mesure d'universalité doit la déclarer non universelle si τ dépasse le niveau de chance, sinon elle valide le vide.
- **Jeu de calibration des seuils disjoint du jeu de mesure des fausses alertes**, avec vérification que le taux mesuré sur le second est au niveau nominal.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duels non exclusifs et non exhaustifs (règle B4).** Duel 1 : H_A est falsifiée si couverture < 85 % **ou** RRMSE > Chapman ; H_B est falsifiée si Chapman sous-estime de > 25 % **et** couverture < 50 % **et** Chao couvre ≥ 90 %. Il existe des issues qui falsifient les deux (Chao couvre à 80 %, Chapman sous-estime de 30 % à 40 % de couverture) et des issues qui ne falsifient aucune. Duel 2 : même structure (H_A tombe si puissance < 0,50 ; H_B tombe si TOST < 0,30 et hiérarchique ≥ 0,80) ; l'issue « 0,6 contre 0,5 » ne tranche rien. Ce ne sont pas des duels mais deux cahiers des charges.
2. **Duel 2, non jugeable par dimensionnement.** Avec 15 familles tenues à l'écart et 10 % de familles défaillantes, l'espérance est 1,5 famille défaillante (calcul refaisable) ; aucune des deux méthodes ne peut atteindre une puissance 0,80, et la pièce le reconnaît elle-même (H_B). Le duel est perdu d'avance par les deux camps.
3. **Attribution erronée.** « Cormack-Jolly-Seber / Fienberg » pour les modèles log-linéaires à population fermée : Cormack-Jolly-Seber est un modèle de **population ouverte** avec ordre temporel des occasions ; les cinq sources n'ont pas d'ordre temporel. Le modèle pertinent est log-linéaire à population fermée (référence à vérifier). « Chao1 corrigée » est l'estimateur par abondances ; avec des listes, c'est Chao2 (la pièce utilise ensuite la bonne formule, mais le duel nomme le mauvais estimateur).
4. **Palier 2 informé : sélection sur la sortie de la défense.** Le banc reçoit les seuils et poids figés et peut « filtrer a posteriori » les schémas pour cibler la région sous-seuil. L'ensemble de familles dépend alors de la défense ; la proportion ε n'est plus une quantité de population mais une fonction de la défense. Aucune des définitions 1 à 4 du tableau 1(a) n'autorise un énoncé sur un ensemble ainsi sélectionné. Il faut déclarer la correspondance entre l'ensemble filtré et une population, ou abandonner l'énoncé par proportion pour ce palier.
5. **Fuite instrument 2.** « Trajectoires simulées sans sabotage pour fixer le seuil » puis « taux de fausses alertes ≤ 1 % » : si les deux utilisent le même jeu, le 1 % est obtenu par construction.
6. **Design effect appliqué à une borne à zéro échec.** n_eff = n/(1 + (n_c − 1)ρ) est la formule de la variance d'une moyenne ; une borne à zéro échec sur une proportion ne se corrige pas par ce facteur mais par le comptage de grappes indépendantes (D a raison sur ce point). Le 32,8 est arithmétiquement juste et méthodologiquement non fondé.
7. **Horvitz-Thompson validé sur les singletons.** Q2 confronte la borne HT au rappel sur les singletons Q₁. Or les singletons sont les unités à π̂_i minimal (variance HT maximale) **et** les unités dont l'appariement est le moins sûr (un singleton peut être un doublon non reconnu). Rareté et erreur d'appariement sont confondues dans le jeu de validation.
8. **Option 4 de 1(a)** : P(R ≥ τ) ≥ Ĉ(1 − ε) insère une quantité estimée Ĉ dans une borne sans propager son incertitude ; l'énoncé n'a pas de niveau de confiance défini.
9. **Bloc 4, point 1 (deux passes).** Si les mêmes instances exécutent la passe 2 après la passe 1, la seconde est contaminée par la première (même contexte) et ne constitue pas une source supplémentaire ; de plus la stratification « par axiomes orthogonaux » impose une structure commune à toutes les instances, donc une corrélation de capture par conception.
10. **Bloc 4, point 6 (7 instances pour absorber 2 refus).** Le refus n'est pas aléatoire : écarter les instances qui refusent sélectionne les sources selon leur permissivité, ce qui corrèle les K restantes précisément sur la variable qui définit la zone censurée.
11. **Q4, fuite et dépendance.** Convertir « manuellement » des entrées de journaux de refus en schémas par des chercheurs du programme produit des familles conçues par le programme, c'est-à-dire ni indépendantes ni tenues à l'écart ; la validation extérieure annoncée ne l'est pas.
12. **Ancrage.** Proposer des instances « telles que celles listées dans collisionneur_v5.py » (fait 13) contredit l'exigence d'indépendance de la pièce elle-même : cette liste contient des lignées des deux sources existantes (faits 5, 6, 13).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Chao2 : Q₂ = 0 rend la forme de base indéfinie ; Q₁ = 0 donne N̂ = n_obs par construction et interdit toute détection de masse manquante — ce qui arrive sous forte dépendance positive entre sources (les familles manquées le sont par toutes).
- Good-Turing p̂₀ = Q₁/Σn_k : estime la masse manquante **sous la loi de capture des sources** ; toute strate à π_i = 0 est invisible, la pièce le dit ; conséquence non dite : p̂₀ est une borne inférieure non calibrée dès qu'une telle strate existe, et aucun test interne ne le signale.
- Log-linéaire avec AICc : avec 31 cellules observables et ≈ 40 à 60 familles (illustratif), la sélection de modèle est instable ; l'interaction d'ordre K n'est jamais identifiable ; l'intervalle sur n₀ diverge dès que les termes d'interaction par paires sont libres (la pièce le note en Q1 sans en tirer de règle d'arrêt).
- Quantile 1 − ε hiérarchique : non jugeable dès que n_écart · ε < 1 (illustratif : 15 × 0,05 = 0,75).
- Horvitz-Thompson : variance non bornée quand min π̂_i → 0 ; identique à la moyenne naïve quand π_i est constant.
- Lan-DeMets : l'α-spending suppose une information maximale fixée ; si σ²_inter est estimée en cours de route, le taux d'erreur de type I n'est plus contrôlé.
- TOST sur l'écart : puissance nulle quand σ_inter > Δ.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Monde sans masse manquante** : présent au duel 1 sous forme de convergence, mais absent pour Good-Turing et pour l'option 4 (Ĉ doit valoir 1).
- **Deux listes du même modèle** et **deux listes disjointes par partition** : le test d'interaction doit détecter la dépendance dans les deux sens ; sans ce contrôle, le signe du biais au bloc 1(d) reste une affirmation.
- **Défense sans effet famille** (scores i.i.d. d'une loi unique) : le modèle bêta-binomial doit estimer un ICC ≈ 0 ; sinon l'instrument fabrique de l'hétérogénéité.
- **Jeu de seuils disjoint du jeu de fausses alertes** (voir défaut 5).
- **Palier 2 sans filtrage** : mesurer le même ensemble de familles avec et sans filtrage sous-seuil ; si les deux proportions coïncident, le filtrage n'apporte rien ; si elles divergent, l'énoncé par proportion est invalide pour ce palier.
- **Journal de refus d'une question sans contenu sensible** : taux de refus de base par fournisseur, sans lequel le « taux de censure » de Q4 n'a pas de référence.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Misinterprétation d'un fait RAPPORTÉ.** Le fait 4 annonce cinq **instances**, non cinq familles. D écrit « les cinq familles prévues ne suffisent pas » (1(c)), « cinq familles scellées (RAPPORTÉ) » (Q1), « mêmes cinq familles scellées » (Q5). Trois livrables reposent sur un comptage erroné de la donnée de départ ; le dimensionnement de Q1 et Q5 est à refaire.
2. **Duel 1 vrai par construction.** H_A : « dans les mondes où indépendance et homogénéité sont imposées, Chapman couvre à 95 % et biais ≤ 5 % ». Chapman est quasi sans biais exactement sous ces hypothèses ; le duel est un test d'implémentation, pas une inférence forte. H_B (« H_A est fausse dans au moins un monde ») est la négation logique, pas une hypothèse scientifique concurrente. Confondant supplémentaire : la couverture dépend de l'**intervalle** choisi (non précisé) autant que de l'estimateur ; un échec de couverture à m petit incrimine l'approximation normale de la variance, pas Chapman.
3. **Duel 2 à issue connue d'avance.** Aucune règle fondée sur la seule moyenne de l'écart ne peut borner une proportion de queue ; la construction « même écart, queues différentes » garantit la falsification de H_A. L'issue « H_B falsifiée » est impossible, ce qui viole B4 (chaque issue doit falsifier quelque chose).
4. **Contrainte binomiale exacte sous dépendance.** 1(c) recommande une « borne binomiale exacte » tout en exigeant que « les dépendances entre éléments sont conservées » (instrument 2). La binomiale exacte suppose l'indépendance ; la pièce ne dit pas comment les deux se concilient (grappes ? bêta-binomiale ?). La mesure n'est pas définie.
5. **« Familles indépendantes effectives » sans règle de comptage.** 1(c) et Q1 exigent de compter des familles indépendantes effectives, mais aucune définition opérationnelle n'est donnée (seuil de corrélation ? grappes déclarées ? ICC ?). Q1 (« viser 29 familles indépendantes sans échec ») est non jugeable en l'état.
6. **Contrôle négatif du duel 2 confondu.** La permutation des étiquettes vue/écart n'est valide que si les deux ensembles sont échangeables. Or les familles vues ont servi à construire la défense : un écart systématique après permutation reflète l'effet d'entraînement attendu, pas une fuite. Le contrôle doit être exécuté sur une défense non ajustée sur les familles vues (ou sur un instantané antérieur).
7. **Q5 : δ = 0,02 non dimensionné.** Un écart de 0,02 entre régimes aveugle et informé, mesuré sur les familles d'un petit nombre de sources, est sous le bruit inter-familles pour tout budget réaliste ; aucun calcul de puissance n'accompagne le seuil.
8. **Bloc 4, appariement : « analyse sur tous les appariements plausibles ».** L'ensemble des appariements d'un graphe biparti partiel est combinatoire ; sans règle d'énumération ou d'échantillonnage déclarée, « tous » n'est pas une procédure. Même remarque que pour C sur la règle de remplacement en cas de refus (sélection sur la permissivité).
9. **Garantie stratifiée** : « correction du risque global » laissée ouverte ; si les strates sont déclarées après observation, c'est une fuite ; si avant, le nombre de strates doit être figé et borné, ce que la pièce ne dit pas.
10. **Q4 sans chiffre.** La question de l'arbitre demande une validation chiffrée ; D renvoie tout chiffre « après audit ». Prudent mais non jugeable en préenregistrement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Chapman avec intervalle normal : couverture dégradée quand m < 10 (illustratif) ou quand la loi de N̂ est asymétrique ; non jugeable sans préciser l'intervalle (normal, log-normal, profil, bootstrap).
- Écart vs proportion : quand σ²_inter → 0 les deux coïncident et le duel 2 ne discrimine plus ; quand la queue porte toute la masse d'échec, l'écart perd toute puissance.
- Borne à zéro échec avec grappes : non jugeable dès que le nombre de grappes indépendantes g < ln α / ln(1 − ε), quel que soit le nombre de familles.
- Binomiale exacte sous ICC > 0 : couverture nominale perdue proportionnellement au design effect.
- Garantie stratifiée : si le nombre de strates croît avec n, la correction multiple ramène la puissance par strate vers zéro.
- Q5 : non détectable tant que l'écart-type de la différence entre régimes (dominé par σ_inter/√k) dépasse δ.
- Modèles multi-listes : non identifiables à deux listes ; à K listes, l'interaction d'ordre K reste non identifiable, ce que la pièce ne dit pas explicitement.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Monde sans masse manquante** : présent (seule pièce à le nommer explicitement comme contrôle du duel 1). À compléter par un monde où la masse manquante est portée par une strate à π = 0, pour vérifier que l'estimateur ne la revendique pas.
- **Deux listes du même modèle** : absent ; sans lui, « tester les interactions par modèles multi-listes » n'a pas de puissance démontrée contre la dépendance réelle.
- **Défense constante** : absent ; la mesure d'universalité doit la rejeter.
- **Lecteur d'appariement sur copie permutée et sur listes sans lien** : absent, alors que Q3 porte précisément sur l'erreur d'appariement.
- **Règle séquentielle sous H₀** : la pièce exige « validité à tout temps » mais ne prévoit pas la simulation qui vérifie le taux de type I à chaque temps d'arrêt ; sans elle, l'affirmation est invérifiable.
- **Permutation vue/écart sur une défense non entraînée** (voir défaut 6).

---

## Note transversale

B apporte des duels mais deux sur trois sont vrais par construction ou contradictoires ; C apporte l'appareil le plus riche mais ses duels violent B4 par non-exclusivité et son palier 2 sélectionne sur la sortie ; D est la plus prudente sur les hypothèses mais fonde trois livrables sur une mauvaise lecture du fait 4 et laisse ses instruments non définis (intervalle, règle de comptage des familles effectives). Aucune des trois ne propose le contrôle minimal commun : deux listes du même modèle comme borne de dépendance maximale, et une défense constante comme borne de non-information.

FIN-DE-CELLULE