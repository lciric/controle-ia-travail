# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Les conceptions A, C, D et E sont présentes. Aucune n'est coupée : chacune se termine par sa ligne de clôture. Les blocs FAITS et QUESTION portent la même empreinte, ce qui est cohérent avec leur contenu identique.

**Portée.** Tout ce qui suit est HYPOTHÈSE de critique. Ce sont des arguments sur la méthode, pas des résultats. Tout chiffre que je donne est illustratif, sauf les calculs exacts que je signale comme tels.

**Statuts.** Je ne modifie aucun statut. Je signale seulement les étiquettes qui me paraissent incohérentes avec leur propre justification, pour que l'arbitre les audite.

---

## Sur la proposition A

### (a) Défauts de méthode

**Type 3 : l'exposant γ ≈ 0,5 est en grande partie vrai par construction.**
- Le banc rend le dommage additif sur des micro-décisions, et le détecteur est une somme de scores. Si les bruits sont indépendants et que le décalage du score est linéaire en δ, on obtient γ = 0,5 sans rien supposer sur l'agent. A le reconnaît en partie : contrôle positif gaussien, seconde tâche.
- Mais γ mélange en réalité deux autres grandeurs propres à l'agent :
  - la persistance du bruit honnête des scores ;
  - l'exposant β de la relation dose-réponse δ → décalage du score.
- Sans mesurer β et la persistance séparément, un γ ≠ 0,5 n'est pas interprétable comme une capacité adverse (voir (b)).

**Le δ réalisé n'est pas le δ commandé.**
- Une consigne « sabote d'amplitude δ » donne un dommage réalisé aléatoire.
- Ce dommage dépend probablement de T, parce que le résumé d'état d'une étape à l'autre peut effacer ou corriger des touches antérieures. L'additivité peut donc varier avec T. C'est un facteur confondant direct de la pente log-log.
- Il faut régresser sur le dommage réalisé par étape, pas sur la consigne.

**Prédiction « γ ≥ 0,85 contre le détecteur du maximum par étape ».**
- À taux de fausses alertes fixé par trajectoire, le seuil du maximum croît comme √(2 log T).
- Entre T = 8 et T = 128, ces corrections logarithmiques peuvent à elles seules déplacer l'exposant apparent autour de 0,85.
- La frontière entre les deux hypothèses tombe dans une zone dominée par des termes en log que l'expérience n'identifie pas.

**Type 2 : incohérences internes.**
- La réponse attendue annonce un gain d'au moins 15 points, mais le duel tranche à 5 points. Les 15 points ne sont donc jamais testés.
- A dit les seuils « gelés avant toute attaque », alors que la sonde est entraînée sur les attaques de la famille (i). Il faut préciser ce qui est gelé : la sonde est construite avec des attaques, et seule la famille d'évaluation reste tenue à l'écart.

**Type 1 : la borne est un fait d'échantillonnage.**
- Si c et q tiennent, si les audits sont tirés indépendamment des positions touchées et si le rapport est figé avant tirage, la fréquence de survie ne peut pas dépasser la borne, sauf par erreur d'estimation.
- L'expérience teste donc P3 et P6, pas la borne. A le dit à moitié ; il faut le dire entièrement.
- La condition « q mesuré ≥ q supposé − 0,1 » est circulaire si q supposé vient d'un pilote mené sur les mêmes familles.

### (b) Conditions sous lesquelles les critères perdent leur puissance

- **Bruit persistant.** Si le processus des scores honnêtes est stationnaire avec un exposant de Hurst H ≠ 0,5, la variance de la somme croît comme T^{2H}. Un δ constant donne alors D* ∝ T^{H}.
  - Le γ estimé est l'exposant H du bruit honnête, pas un exposant d'attaque.
  - Le critère γ ∈ [0,4 ; 0,6] devient non jugeable dès que H̃ (estimé sur les honnêtes) est hors de [0,4 ; 0,6].
- **Réponse non linéaire.** Si le décalage moyen vaut f(δ) ∝ δ^β, alors D* ∝ T^{1 − 1/(2β)}. Avec β = 2, γ = 0,75 sans aucun changement d'adversaire. γ n'est identifiable que si β est estimé indépendamment.
- **Plancher de N.** Avec N = 5 références, le plus petit niveau étalonnable sans hypothèse de loi est 1/6 (A le note lui-même en (c)). La cellule « 5 % de fausses alertes, N = 5 » de la prédiction 3 est non jugeable sans modèle paramétrique, qu'il faudrait alors déclarer.
- **Intervalles trop étroits.** Les trajectoires de cellules différentes partagent leurs graines et leurs données. Un bootstrap qui ignore ce regroupement sous-estime la variance de la pente.
- **Type 1, sensibilité hétérogène.** Si la sensibilité q_i varie selon les étapes et que l'adversaire concentre le dommage là où q_i est faible (covariance négative entre q_i et dommage d_i), la borne calculée avec la moyenne de q est invalide. La borne correcte utilise le minimum de q_i sur les étapes touchées.
- **Type 1, effectif.** Pour montrer une fréquence de survie inférieure à une borne b avec zéro événement observé, il faut au moins environ 3/b trajectoires par famille (règle de trois).
  - Avec b ≈ 0,04 (exemple illustratif de A), il faut environ 75 trajectoires par famille, soit à peine ce qu'offrent environ 67 par famille.
  - Le duel est donc à la limite du jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Type 3 : consigne de sabotage présente, dommage forcé à zéro** (micro-décisions remplacées par les décisions honnêtes). Sinon le détecteur cumulatif peut accumuler la signature de la consigne, qui croît aussi en √T, et γ ≈ 0,5 sort sans aucun lien avec le dommage.
- **Type 2 : adaptateur LoRA bénin de même rang**, entraîné sur des données neutres. Sans lui, une sonde qui détecte la famille (ii) peut ne détecter que le changement de poids.
- **Type 1 : erreurs naturelles de même amplitude injectées hors adversaire.** Il faut vérifier que q mesure la visibilité du dommage et non la signature stylistique des attaques de l'équipe rouge.

---

## Sur la proposition C

### (a) Défauts de méthode

**Statuts à auditer.** C étiquette VÉRIFIÉ des références qu'il déclare lui-même citées de mémoire : Vovk et al. 2005, Burns et al. 2023, Allan 1966, Hurst 1951. Il étiquette aussi VÉRIFIÉ le choix du modèle. Une citation de mémoire ne peut pas porter à la fois ce statut et cette justification. Je ne change pas le statut, je signale l'incohérence.

**Type 1 : la garantie n'est pas dérivée.**
- Une martingale de conformité contrôle les fausses alertes sous échangeabilité (inégalité de Ville). Elle ne borne pas la perte d'utilité sous l'alternative.
- Aucun argument ne relie le score de non-conformité à ε. « L'adversaire est mathématiquement contraint » est donc une HYPOTHÈSE présentée sous une forme de théorème.
- Comparer le taux d'échec silencieux à α revient à confondre le niveau des fausses alertes et le taux de détections manquées. Rien ne justifie qu'ils soient égaux.

**« Jamais vues lors de la calibration » est vrai par construction.** Un étalonneur à une classe ne voit jamais d'attaque. La nouveauté réelle des attaques n'est pas testée.

**Fuite de conception.** Les attaques sont contraintes à garder une valeur-p à l'échelle w = 1 au-dessus de 0,10. Elles sont donc construites avec la statistique même du défenseur. Ce sont des attaques adaptées à une composante du détecteur, pas des attaques inédites.

**Type 2 : le résidu mesure surtout le décalage de distribution.**
- Une régression ridge activations → texte sur environ 50 × 30 = 1 500 étapes (illustratif), en dimension 4 096, est sous-déterminée.
- Le résidu hors échantillon augmente pour tout décalage de distribution : nouveau sujet, consigne système différente. Une consigne de sabotage change les activations à toutes les positions. Le résidu détecte alors la consigne, pas le dommage.
- Le critère « ΔpAUC ≥ 0,15 sur FPR ∈ [0 ; 0,05] » n'a pas de sens sans normalisation : la pAUC non normalisée vaut au plus 0,05. Il est non jugeable en l'état.

**Type 3 : la variance d'Allan est aveugle au décalage de niveau.**
- C'est un défaut structurel. La variance d'Allan est invariante par ajout d'une constante à y_t, puisqu'elle ne porte que sur des différences de moyennes adjacentes.
- Une attaque par consigne présente dès l'étape 1, qui décale le niveau de la projection, est invisible par construction.
- Seule une dérive cumulée (une rampe ou une marche aléatoire de y_t) modifie la pente μ. H_A suppose donc tacitement que les touches s'intègrent dans y_t, ce qui n'est ni mesuré ni contrôlé.

**Fuites supplémentaires.**
- Le sous-espace de projection est estimé sur les 50 références. Rien n'indique qu'elles sont disjointes des 100 exécutions honnêtes évaluées.
- L'amplitude des attaques est définie dans ce même espace projeté : l'adversaire est défini dans l'espace de mesure.

**Seuils incohérents.** H_A exige Δμ ≥ 0,7, la falsification de H_A se déclenche à Δμ < 0,15, et l'intervalle entre les deux n'est déclaré nulle part comme « non concluant ».

### (b) Conditions sous lesquelles les critères perdent leur puissance

- **Type 1, autocorrélation.** Si l'autocorrélation des scores honnêtes intra-trajectoire est non nulle (ρ₁ ≠ 0), les valeurs-p séquentielles ne sont ni indépendantes ni uniformes. Le contrôle de Ville tombe et les fausses alertes ne sont plus bornées.
- **Type 1, non-stationnarité.** Il en va de même si la loi marginale du score dépend de la position t, par exemple une norme d'activation qui croît avec la longueur du contexte. Mettre en commun les étapes des références rend alors les valeurs-p non uniformes, même sur des trajectoires honnêtes.
- **Type 2, sur-ajustement.** Si le nombre effectif d'échantillons n = N·T est inférieur à la dimension d, l'espérance du carré du résidu sur des honnêtes tenus à l'écart dépasse celle observée en entraînement d'un terme croissant en d/n.
  - Un seuil fixé sur les résidus d'entraînement produit des fausses alertes au-delà du nominal.
- **Type 2, dépendance au décodage.** Si la variance du résidu honnête est dominée par l'échantillonnage du décodage, le rapport signal-sur-bruit dépend de la température. Le critère n'est comparable qu'à température fixée.
- **Type 3, variance de l'estimateur.** Avec M = 64 et τ = 16, l'estimateur d'Allan dispose d'environ M/(2τ) = 2 différences indépendantes par trajectoire. C'est un khi-deux à environ 2 degrés de liberté. La pente μ estimée par trajectoire a une variance telle qu'une AUC de 0,85 par trajectoire est improbable sans moyenne sur plusieurs trajectoires.
- **Type 3, attaque de niveau.** Si l'effet de l'attaque est un décalage de niveau constant, μ_attaque a la même loi que μ_honnête : la puissance est nulle quelle que soit l'amplitude.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Type 1 : consigne de sabotage non suivie** (dommage nul mesuré). Il faut séparer l'alerte due à la consigne de l'alerte due au dommage.
- **Type 2 : consigne système bénigne de même longueur, et résidu calculé sur des paires texte/activations permutées entre étapes.** Si le CUSUM détecte encore dans le second cas, il lit les activations seules.
- **Type 3 : injection synthétique, dans les trajectoires honnêtes, d'un décalage constant et d'une marche aléatoire de même énergie.** Le premier ne doit rien changer à μ, le second doit le faire. Sans ce contrôle d'instrument, une issue H_B ne se distingue pas d'une cécité de la mesure.

---

## Sur la proposition D

### (a) Défauts de méthode

**Le modèle d'adversaire n'est pas spécifié.**
- D parle de « familles de dégradation réservées » sans dire qui dégrade : l'agent lui-même (consigne, poids) ou l'environnement (documents).
- Pour le duel sur le mécanisme, c'est un facteur confondant de premier ordre :
  - dans le cas endogène, les activations peuvent coder la présence de la consigne ;
  - dans le cas exogène, elles peuvent ne rien coder.
- Le gain mesuré n'est interprétable qu'à modèle de menace fixé.

**Garantie.**
- La borne hypergéométrique est exacte sous ses conditions. Le statut VÉRIFIÉ de « calcul conditionnel » me paraît cohérent.
- Le certificat porte toutefois sur le monde clos des obligations définies par l'équipe, à partir du même calcul de référence qui définit « conclusion grave ». Les deux partagent leur source : la garantie couvre les attaques qui passent par la table, pas celles qui passent par la règle de recalcul ou par une obligation manquante.
- « Jamais vu » se réduit donc à « quelconque à l'intérieur du format ». D le dit en partie ; la portée doit être écrite ainsi dans l'article.

**Phénomène : D·I ≃ h est presque une identité.**
- Pour tout accumulateur additif dont les incréments ont une moyenne μ > 0 après le changement, l'identité de Wald donne E[délai]·μ ≈ h + E[dépassement], que le score soit une log-vraisemblance ou non.
- Si I est estimé comme l'incrément moyen post-changement du même score, comme le protocole semble le prévoir, la loi est vérifiée par construction à la correction de dépassement près.
- Le contenu réfutable se limite alors à la dépendance et à la non-stationnarité des incréments.
- D écarte le cas « débit calculé sur trajectoire arrêtée », mais pas celui-ci.
- Le comparateur « prédicteur ignorant I » est trop faible pour éclairer quoi que ce soit au-delà de Wald.

**Mécanisme, définition du succès.** Un succès n'est compté que si le vérificateur confirme une erreur pertinente. Si le corrigé indépendant et le vérificateur partagent la même table source, leurs erreurs sont corrélées. L'indépendance revendiquée doit être montrée, par exemple par un désaccord mesuré entre les deux sur un échantillon.

### (b) Conditions sous lesquelles les critères perdent leur puissance

- **Garantie, case pivot.** Si la loi de m sur les dossiers met une masse non négligeable en m = 1, la borne vaut 1 − b/N sur ces dossiers. Le critère « ≤ 10 % » exige approximativement m·b/N ≳ 2,3 (approximation exponentielle, illustratif) et devient inatteignable à budget fixé.
- **Garantie, audit imparfait.** Si la sensibilité q de l'audit est inférieure à 1, la borne devient environ (1 − q·m/N)^b. Toute estimation de q dont l'intervalle exclut 1 invalide le certificat exact. D le prévoit (garde-fou), mais cela restreint fortement le domaine couvert.
- **Mécanisme, regroupement.** L'unité indépendante est le dossier. Si la corrélation intra-dossier des issues de détection est élevée, l'effectif effectif approche le nombre de dossiers de test. Un intervalle de demi-largeur inférieure à 10 points exige alors de l'ordre de quelques centaines de dossiers positifs (illustratif) ; ce n'est pas garanti avec 200 dossiers au total.
- **Phénomène, grand dépassement.** Si la variance des incréments est comparable à h, le dépassement moyen relatif est grand. L'erreur relative de 25 % est alors dominée par le dépassement, pas par la loi.
- **Phénomène, débit variable.** Si le débit post-changement croît avec l'accumulation du dommage, un I constant est mal spécifié, et l'échec ne dit pas si la loi ou le modèle d'incréments est en cause.
- **Phénomène, censure.** Si la probabilité de non-alarme avant l'horizon est élevée, E[délai] n'est pas identifiable. D le déclare.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Mécanisme : relecture du même texte par un modèle propre.** On extrait les activations d'un modèle sain qui relit le texte produit (sonde de ré-encodage, au sens où A l'a proposé ; je m'en sers en le disant). Sans ce contrôle, « intuition interne » n'est pas séparé de « information du texte ». La permutation proposée par D ne fait pas cette séparation.
- **Mécanisme : perturbation bénigne de même canal que l'attaque** (consigne neutre ou document modifié sans effet sur la conclusion), une fois le modèle de menace fixé.
- **Phénomène : marche aléatoire synthétique de même moyenne et de même variance d'incréments, plus permutation des incréments post-changement.** Si la prédiction est aussi bonne sur ces substituts, la « loi » ne dit rien de l'agent au-delà de Wald.
- **Garantie : rapports honnêtes avec omissions légitimes de compression.** Une case vide ne doit pas compter comme invalide ; sinon m est gonflé artificiellement.

---

## Sur la proposition E

### (a) Défauts de méthode

**Statuts à auditer.**
- E étiquette VÉRIFIÉ « le bruit honnête s'annule en 1/√t ». Ce n'est vrai que pour des incréments indépendants et centrés, ce que E ne mesure pas.
- E combine OBSERVÉ-NON-AUDITÉ et un chiffre illustratif (« 15 à 20 étapes ») : une observation qui porte un chiffre inventé est incohérente.
- Je ne change aucun statut.

**Type 1 : la borne U n'est pas dérivée.**
- L'identité télescopique sur la valeur d'achèvement honnête est exacte. En revanche, le passage « sortie du tube texte-activations ⇔ grand saut de valeur » est une régularité non démontrée (E l'admet sous H_B). Le calcul de U n'est donné nulle part.
- **Asymétrie de décision.** H_A est retenue si aucun test ne rejette (p ≥ 0,05). Une expérience peu puissante favorise donc mécaniquement la « garantie ». C'est l'inverse de ce qu'exige une garantie : l'absence de violation observée n'est pas un résultat sans calcul de puissance.
- Tester « D̂_max ≤ U » par un test binomial sur un maximum de moyennes prises sur plusieurs attaques est mal défini : le maximum de plusieurs estimateurs est biaisé vers le haut et n'a pas de loi binomiale.
- Le contrôle « activations permutées ⇒ U ≥ 0,85 » n'a de sens que si U dépend des activations, ce que la construction de U ne précise pas.

**Type 2 : contrôle par permutation temporelle.**
- Ce contrôle n'est pas diagnostique. Pour une attaque à biais constant par étape, la somme cumulée est (à la réflexion du CUSUM près) invariante par permutation de l'ordre.
- Un mécanisme valide ne perdrait donc pas son gain, et le contrôle le déclarerait à tort falsifié. Il ne sert que pour des attaques à structure temporelle.

**Type 2 : le rejeu depuis t − 6 suppose un modèle propre.**
- Si l'attaque est endogène, le même agent rejoue le sabotage.
- Si un modèle propre est disponible, la question P8 soulevée par A s'applique (je la reprends en le disant) : la comparaison à la ré-exécution devient la ligne de base à battre, et E ne l'inclut pas.

**Type 3 : R̂_eff est biaisé par construction.**
- **Effet du seuil.** Les « descendants déviés » sont comptés au-delà du 95e centile honnête. Une trajectoire non perturbée produit donc en moyenne 0,05 dépassement par étape aval.
  - Sur K étapes aval, le compte attendu sans aucune propagation est 0,05·K (calcul exact sous indépendance) : 0,75 pour K = 15, 1 pour K = 20.
  - R̂_eff est proche de 1 par construction et décroît avec t₀ par simple effet d'horizon.
  - Le contrôle « paraphrase bénigne < 0,30 » échouerait mécaniquement.
- **Pas d'arbre à observer.** « Descendant direct » n'est pas défini dans une chaîne autorégressive où chaque étape dépend de tout le contexte. Une trajectoire est une lignée unique, pas un arbre de Galton-Watson : la loi de la descendance n'est pas identifiable sans branchements contrefactuels explicites, et le critère de seuil à 1 n'a pas d'objet mesurable.
- **Circularité.** La corruption finale est mesurée sur une étape qui figure parmi les descendants comptés. Le rapport de cotes « supercritique contre sous-critique » est en partie tautologique : c'est une sélection sur l'issue.
- **Position confondante.** Les étapes à fort χ̂ (forte réutilisation aval) sont probablement les premières étapes. Aucune comparaison à « auditer les premières étapes » n'est prévue.

### (b) Conditions sous lesquelles les critères perdent leur puissance

- **Type 1, sorties honnêtes du tube.** Un tube à 95 % par transition, sur T = 30 transitions supposées indépendantes, laisse une trajectoire honnête en sortir au moins une fois avec probabilité 1 − 0,95³⁰ ≈ 0,79 (calcul exact sous indépendance).
  - Sans correction pour la multiplicité, « sortir du tube » n'est pas un événement rare, et le taux de fausses alertes de 0,05 visé est incompatible avec ce tube.
- **Type 1, puissance.** Si la probabilité de violation p_v est inférieure à environ 3/n, avec n trajectoires par attaque, le test ne peut pas rejeter H_A, qui gagne par défaut.
- **Type 2, blanchiment.** Si N·T est inférieur à d, la matrice Σ̂ est singulière et Σ̂^{−1/2} n'existe pas. Tout rétrécissement introduit un paramètre λ qui fixe, à lui seul, le taux de fausses alertes et la puissance. Sans réglage de λ sur des données tenues à l'écart, le critère est non jugeable.
- **Type 3, compte de base.** Si les dépassements honnêtes sont autocorrélés, la variance du compte nul dépasse celle de la loi binomiale B(K ; 0,05). L'écart entre perturbations « supercritiques » et « sous-critiques » est alors noyé dans la variance de base.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Type 3 : ré-échantillonnage pur à t₀**, avec une autre graine et aucune perturbation. Il donne le R̂_eff nul dû à la stochasticité du décodage et au seuil. Sans lui, aucune valeur de R̂_eff n'est interprétable. La paraphrase ne le remplace pas, car elle ajoute une perturbation.
- **Type 3 : audit des B premières étapes** (ligne de base de position), face à l'audit des B étapes de plus fort χ̂.
- **Type 2 : canal bénin de même nature que l'attaque** : consigne cachée neutre pour le cas endogène ; documents modifiés à même distance d'édition sans effet sémantique pour le cas exogène.
- **Type 1 : comptage du nombre de sorties du tube par trajectoire honnête,** et comparaison de la borne à celle de l'audit uniforme seul, à budget égal. E le mentionne pour la nouveauté, mais pas comme contrôle.

---

**Ce qui est réfutable dans cette critique elle-même.**
1. **Allan (C).** L'invariance de la variance d'Allan par décalage constant se vérifie en une ligne de calcul.
2. **R̂_eff (E).** Le biais de seuil se vérifie par simulation sous l'hypothèse nulle de non-propagation.
3. **D·I ≃ h (D).** La réduction à l'identité de Wald se vérifie sur une marche aléatoire synthétique.
4. **γ (A).** La dépendance de γ à H et à β se vérifie en injectant un bruit persistant et une réponse non linéaire dans le contrôle positif de A.

Si l'un de ces quatre calculs ne donne pas ce que j'annonce, la critique correspondante tombe.

FIN-DE-CELLULE