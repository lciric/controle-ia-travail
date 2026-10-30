# Réponse indépendante à la question 3 — fertilité d'un croisement, transition de phase, essaims — v1

- Répondant : instance neuve et indépendante (« Fable ») ; aucun fichier `reponse-*`, `relecture-*`, `revue-*` ni `donnees/` lu.
- Modèle : claude-fable-5-1.
- Date (`date -u`) : Fri Oct 30 17:07:43 UTC 2026.
- Lu : `question-3-fertilite-v1.md` ; contexte : `question-1-chapelles-v1.md`, `question-2-niches-v1.md`.
- « vérifié » = existence confirmée le jour même par recherche sur le web, sans PDF empreinté (non opposable, règle R7) ; « SUPPOSÉ » = de mémoire. Niveau méthode ; aucune décision.

## Verdict

La fertilité n'est pas une propriété de la distance mais d'un quadruplet (paire, procédé de croisement, budget, juge). On peut la définir avant tout calcul comme la sur-additivité du rendement validé : ce que A et B réunis produisent, moins ce que chacun produit seul. L'hypothèse « transition de phase » est testable, mais a trois rivales (décroissance monotone, cloche, seuil à queue lourde) à geler avant de regarder. L'argument des essaims n'a de contenu que si l'essaim bat, à calcul égal, le meilleur de N agents indépendants ; sinon c'est de l'échantillonnage.

## 1. Ce qu'un expert ferait, que tu ne demandes pas

- Séparer trois notions que le mot « fertilité » fusionne : la fécondité d'une théorie (Kuhn, 1977 : la « fruitfulness » est l'une de ses cinq vertus pour choisir une théorie, SUPPOSÉ ; McMullin distingue fertilité prouvée et fertilité potentielle, vérifié) ; la fertilité d'un croisement, qui est une interaction et non une somme ; la probabilité d'étincelle, événement rare à queue lourde (Fleming, 2001, vérifié : recombiner des composants jamais combinés abaisse la moyenne et élargit la variance). Viser la moyenne, la queue ou la probabilité de dépasser un seuil ne classe pas les paires dans le même ordre : l'expert choisit d'abord.
- Définir la fertilité ex post (la mesure) avant la fertilité ex ante (le prédicteur) ; sinon le prédicteur devient la définition et tout calcul confirme ce qu'il suppose.
- Écrire les hypothèses rivales de forme avant de chercher la transition : décroissance monotone avec la distance ; cloche avec distance optimale (en biologie, Price et Waser, 1979, vérifié ; en conception, Chan et coll., 2011, vérifié : les analogies lointaines aident jusqu'à un point) ; seuil franc avec queue lourde (percolation). Un événement rare est non linéaire sans être critique : l'étincelle ne prouve pas la transition.
- Pour les essaims, nommer la ligne de base (meilleur-de-N indépendant, agent unique à budget multiplié par N) et vérifier l'indépendance : des agents issus d'un même modèle partagent leur bruit, et l'influence mutuelle détruit la sagesse des foules (Lorenz et coll., 2011, vérifié).
- Traiter l'antériorité comme un corpus structuré (définition adoptée, métrique, forme de courbe trouvée, échantillon, contraires), non comme une liste.

## 2. Données brutes de départ

- Mondes inventés : axiomes, graphe complet des dérivations, vérités cachées, et surtout journaux complets des proposeurs (chaque tentative, pas seulement les succès) : la fertilité se lit dans le taux d'échec autant que dans les réussites.
- Littérature réelle avec coupure temporelle : listes de références complètes et datées (OpenAlex, Semantic Scholar), codes de classification (mathématiques MSC, brevets CPC, médecine MeSH), catégories croisées d'arXiv. Jamais les indices dérivés (nouveauté, disruption) : on les recalcule.
- Cas historiques en liste brute : découvertes multiples (Merton, 1961, vérifié), « occasions manquées » entre mathématiques et physique (Dyson, 1972, vérifié), hypothèses de littératures disjointes de Swanson (1986, vérifié : huile de poisson et syndrome de Raynaud) avec leur sort clinique ultérieur (SUPPOSÉ).
- Essais contrôlés existants, au niveau individuel : Chan et coll., 2011 ; Lazer et Friedman, 2007, vérifié ; Derex et Boyd, 2016, vérifié ; Mason et Watts, 2012, SUPPOSÉ.
- Pour les essaims : journaux des messages entre agents (qui a lu quoi, quand), pas seulement la sortie finale.

## 3. Méthodes et outils

### 3a. Définir la fertilité avant de la calculer

Soit R(X) le rendement validé d'un ensemble de prémisses X sous procédé, budget et juge figés : nombre ou valeur des résultats nouveaux validés par les juges et survivant aux tests de mort. Définition proposée :

F(A, B) = R(A ∪ B) − R(A) − R(B) + R(A ∩ B),

et probabilité d'étincelle = Pr[F ≥ s] pour un seuil s gelé. En monde inventé, la vérité est connue : R se calcule exactement (résultats vrais atteignables en k pas depuis A ∪ B et depuis aucun des deux seuls). C'est une interaction au sens d'inclusion-exclusion ; cousines formelles : synergie en décomposition partielle de l'information (Williams et Beer, 2010), épistasie, supermodularité ; variantes continues : surprise bayésienne (Itti et Baldi), progrès de compression (Schmidhuber, 2010) ; tous SUPPOSÉ. Variante épistémologique : l'« analogie neutre » de Hesse (1966, SUPPOSÉ), les propriétés de A dont on ignore si elles valent dans B, est le réservoir ; la fertilité réalisée est la part de ce réservoir tranchée positivement. Uzzi et coll. (2013, vérifié) mesurent la nouveauté par les paires de revues atypiques citées et trouvent l'impact maximal pour « conventionnel plus une pointe d'atypique » : mesure d'impact, non de vérité, et à retard (Wang, Veugelers, Stephan, 2017, SUPPOSÉ) ; critère externe, non définition.

### 3b. Tester l'hypothèse de transition de phase

Nommer un paramètre de contrôle (couplage entre niches : concepts partagés, capacité du canal ; ou la distance) et un paramètre d'ordre (F moyen, ou Pr[F ≥ s]). Prédictions gelées qui distinguent une vraie transition d'une simple non-linéarité : (i) la courbe se raidit quand la taille du monde croît et les courbes se superposent après remise à l'échelle ; (ii) la variance (susceptibilité) culmine à la même valeur du paramètre ; (iii) la distribution des tailles de cascades (résultats déclenchés par un résultat) suit une loi de puissance au seuil seulement ; (iv) hystérésis si la transition est du premier ordre. Comparaison de modèles préenregistrée : logistique contre cloche contre linéaire contre loi de puissance, critère d'information fixé d'avance. Modèles générateurs : percolation sur graphe de concepts (Silverberg et Verspagen, 2005, SUPPOSÉ), urne de Pólya à nouveautés corrélées (Tria et coll., 2014, vérifié), paysages NK et sauts longs (Kauffman et Levin, 1987, SUPPOSÉ). En psychologie, Stephen et coll. (2009, vérifié) ont déjà traité la découverte mathématique individuelle comme transition de phase, par un pic d'entropie avant l'insight : méthode à reprendre sur les journaux de proposeurs.

### 3c. Tester l'argument des essaims

Plan croisé : nombre d'agents N × force du couplage (de l'isolement au consensus), avec deux contrôles obligatoires : meilleur-de-N indépendant, et agent unique à budget N fois plus grand. Prédictions de l'argument : F maximal à couplage intermédiaire (les réseaux partiellement connectés explorent mieux : Lazer et Friedman, 2007 ; Derex et Boyd, 2016) ; sur-additivité par rapport au meilleur-de-N ; et, condition d'émergence, perte de l'avantage quand on coupe les messages (ablation). Signatures de physique statistique comme en 3b : raidissement avec N, pic de variance. Ne pas s'appuyer sur le théorème « la diversité bat la compétence » (Hong et Page, 2004, SUPPOSÉ), réfuté sur sa forme mathématique (Thompson, 2014, vérifié). Outils d'ingénieur : MAP-Elites (Mouret et Clune, 2015, vérifié) entretient des niches explicites et mesure couverture × qualité ; l'algorithme CHC (Eshelman, 1991, vérifié) impose une distance minimale entre parents (« prévention d'inceste »), précédent direct d'un seuil de distance de croisement.

### 3d. Protocole d'antériorité

Requêtes en trois langues (fertilité, fécondité, fruitfulness, Fruchtbarkeit ; recombinaison ; distance d'analogie ; insight ; multiples), boule de neige par citations amont et aval, grille d'extraction (définition, métrique, forme de courbe, échantillon, domaine), recherche des contraires (qui a trouvé que la distance nuit). Pistes, toutes SUPPOSÉ : Poincaré (1908, « L'invention mathématique » : les combinaisons fécondes viennent souvent de domaines éloignés, libellé à vérifier) ; Hadamard (1945) ; Wiener (1948, les « régions frontières » sont les plus riches, libellé à vérifier) ; Koestler (1964) ; Mednick (1962, associations distantes) ; Campbell (1960, variation aveugle, rétention sélective) ; Boden (1990, créativité combinatoire contre transformationnelle) ; Fauconnier et Turner (2002, intégration conceptuelle) ; Gentner (1983, alignement structurel) ; Burt (2004, trous structuraux) ; Fleck (1935, collectifs de pensée) ; Galison (1997, zones d'échange) ; Altshuller (niveaux d'invention par analyse de brevets) ; Lenat (heuristiques d'intérêt du programme AM) ; Peirce (économie de la recherche).

## 4. Vérification hors de toi et de nous

- Réplication par un tiers, sur données ouvertes, de l'indice d'atypie (Uzzi, 2013) et de la courbe F contre distance ; fragilité des indices à la fenêtre de citation (SUPPOSÉ) à rapporter.
- Prédiction gelée avec coupure temporelle : classer les paires de codes (MSC, CPC) par fertilité prédite avant une date t ; un tiers mesure après t ; comparer à la référence Sourati et Evans (2023).
- Jeu d'épreuve historique : retrouver les multiples de Merton, les occasions manquées de Dyson et les hypothèses de Swanson avec un taux de faux positifs chiffré sur des paires témoins.
- Juges humains externes à l'aveugle sur les résultats produits (technique d'évaluation consensuelle d'Amabile, SUPPOSÉ), accord inter-juges publié.
- Transition : exposants et superposition reproduits par une équipe indépendante sur un monde qu'elle génère elle-même avec le générateur scellé et d'autres graines.
- Essaims : ablation des messages reproductible ; si l'avantage disparaît sous le meilleur-de-N, l'argument tombe.

## Reformulation de la demande

« Avant tout calcul, définir la fertilité d'un croisement de niches comme la sur-additivité du rendement validé, F(A, B) = R(A ∪ B) − R(A) − R(B) + R(A ∩ B), sous procédé, budget et juges figés, et la probabilité d'étincelle comme Pr[F ≥ s] ; geler s. Geler ensuite trois hypothèses rivales sur la forme de F en fonction du couplage entre niches (monotone, cloche, seuil critique) et les quatre signatures qui les départagent (raidissement avec la taille, pic de variance, cascades en loi de puissance au seuil, hystérésis), puis les tester d'abord en mondes inventés, puis sur la littérature réelle avec coupure temporelle. Tester l'argument des essaims par un plan N × couplage contre meilleur-de-N et agent unique à budget égal, avec ablation des messages. Conduire l'antériorité comme un corpus structuré, en trois langues, contraires compris, et livrer grille, scripts et données brutes pour qu'un tiers rejoue tout. »

## Références

Vérifiées (existence) : McMullin, « The fertility of theory and the unit for appraisal in science » (année SUPPOSÉ : 1976) ; Fleming, « Recombinant uncertainty in technological search », *Management Science* 47(1), 2001 ; Uzzi, Mukherjee, Stringer, Jones, « Atypical combinations and scientific impact », *Science* 342, 2013 ; Price, Waser, « Pollen dispersal and optimal outcrossing in *Delphinium nelsoni* », *Nature* 277, 1979 ; Chan, Fu, Schunn, Cagan, Wood, Kotovsky, *Journal of Mechanical Design*, 2011 (et Fu et coll., 2013, « near » contre « far ») ; Lorenz, Rauhut, Schweitzer, Helbing, *PNAS*, 2011 ; Merton, « Singletons and multiples in scientific discovery », 1961 ; Dyson, « Missed opportunities », *Bulletin of the American Mathematical Society* 78, 1972 ; Swanson, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge », 1986 ; Lazer, Friedman, « The network structure of exploration and exploitation », *Administrative Science Quarterly*, 2007 ; Derex, Boyd, « Partial connectivity increases cultural accumulation within groups », *PNAS*, 2016 ; Tria, Loreto, Servedio, Strogatz, « The dynamics of correlated novelties », *Scientific Reports*, 2014 ; Stephen, Boncoddo, Magnuson, Dixon, « The dynamics of insight: mathematical discovery as a phase transition », *Memory & Cognition*, 2009 ; Thompson, « Does diversity trump ability? », *Notices of the AMS*, 2014 ; Mouret, Clune, « Illuminating search spaces by mapping elites », arXiv 1504.04909, 2015 ; Eshelman, algorithme CHC avec prévention d'inceste (année 1991 SUPPOSÉ).

SUPPOSÉ : toutes les autres références nommées ci-dessus, à vérifier sur PDF empreinté avant tout usage.
