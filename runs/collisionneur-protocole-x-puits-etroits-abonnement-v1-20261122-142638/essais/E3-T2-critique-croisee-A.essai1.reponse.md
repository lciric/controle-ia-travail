# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, C, D, E et F sont présentes et closes par leur balise de fin ; aucune ne paraît coupée. Ma propre conception du tour III.1 n'est pas transmise : je ne m'y réfère pas. Le bloc FAITS ne contient que la question, sans donnée ni statut ; je ne me sers pas des chiffres de son en-tête. Empreintes non recalculées.

**Conventions.** « VÉRIFIÉ (calcul ici) » désigne un calcul fait dans ce texte. Mes autres jugements sont des HYPOTHÈSES de relecteur. Je ne réécris aucun statut des pièces ; je signale ceux que la pièce n'étaye pas. Tous les chiffres sont illustratifs : repris des pièces, ou calculés ici à partir d'eux. Je n'ajoute aucune référence.

## Sur la proposition B

**(a) Défauts de méthode**

- **D6 n'estime pas α.** R5 définit α = P(V=1 | V*=0). L'estimateur proposé est P(V*=0 | V=1), le complément de la précision, qui dépend de la prévalence parmi les sorties sélectionnées. Une pente en log n peut donc apparaître à α constant. VÉRIFIÉ (calcul ici, depuis R5). Si les tests étendus contiennent ceux d'origine, β = 0 par construction, et les fausses acceptations de V* restent invisibles.
- **D1, témoin possiblement vide.** La couverture de Clopper–Pearson ne dépend que du nombre de succès par sous-échantillon. Une permutation interne au sous-échantillon redonne la même couverture par construction. Il faut permuter entre sous-échantillons ; le texte ne le précise pas.
- **D3, fuite entre strates et mesure.** Les strates viennent des p̂ de D2, donc des verdicts qui servent aussi à estimer t. Une instance classée « basse » l'est en partie par hasard.
- **D2 et D5 ne sont pas exhaustifs.** D2 : une loi de P sans plancher ni queue en puissance réfute les deux modèles, issue sans lecture prévue. D5 : une baisse d'un facteur deux réfute H_A sans donner H_B.
- **Arrêt optionnel.** Augmenter l'échantillon quand l'issue est indécise, avec des tests à n fixé, contredit l'exigence de validité à tout instant que B rappelle en R3.

**(b) Perte de puissance, en termes de lois**

- **D1.** La couverture réelle sous Bin(n, p) dépasse le nominal : une dépendance n'est vue que si elle consomme cette marge plus 0,02. L'écart-type de la couverture estimée sur 200 sous-échantillons vaut ≈ 0,015 ; le seuil 0,93 est à ≈ 1,3 écart-type de 0,95. VÉRIFIÉ (calcul ici). La puissance n'est établie que contre l'alternative markovienne, pas contre un mélange ∫ Bern(θ)^{⊗n} dΠ(θ). La mesure se fait à p modéré, alors que R3 est invoqué à p faible.
- **D2.** Avec p₀ libre, H_A n'est pas réfutable dès que p₀ ≲ ln(1/δ)/n : p₀ doit être pré-enregistré. Les estimateurs de U(k ≤ n/16) et de U(n) partagent les tirages ; leurs erreurs sont corrélées.
- **D3.** t̂ par strate a pour dénominateur le nombre de positifs, d'espérance Σᵢ n·pᵢ : non jugeable quand il vaut quelques unités. Quand p → 0, R7 devient c_v(t−f) > c_g(1−t)+c_f ; à r grand, le signe ne s'inverse que si t−f ≈ 0. La conjonction « chute de 0,2 et inversion » n'est donc atteinte que par un filtre proche du hasard. Un t qui passe de 0,9 à 0,3 avec f petit ne tranche rien.
- **D5.** Avec des intervalles à 95 %, le non-recouvrement exige environ 9 succès de la base face à zéro succès de l'affiné (bornes de Poisson 4,12 contre 3,69). À p_base = 10/n et p divisé par 10, la puissance par instance est ≈ 0,4, pas 0,8. VÉRIFIÉ (calcul ici, approximation de Poisson). Le duel est muet sous ~10/n, donc sur les puits étroits que sa « portée » vise.
- **D6.** P(V*=0 | V=1) n'identifie α que si la prévalence parmi les sélectionnés ne varie pas avec n.

**(c) Contrôles négatifs dont l'absence serait fatale**

- D6 : un vérificateur synthétique à taux de fausse acceptation fixé, indépendant de l'objet, soumis à la même sélection. Toute pente mesurée y est un artefact.
- D3 : strates calculées sur une moitié des tirages, t estimé sur l'autre.
- D4 : un générateur synthétique dont la loi conditionnelle exacte est calculable, avec écart connu nul. La grammaire triviale ne teste que la tuyauterie.
- D5 : la base à température abaissée jusqu'à l'entropie de l'affiné. Si elle « perd » autant d'instances, l'effet n'est pas celui de l'affinage.

## Sur la proposition C

**(a) Défauts de méthode**

- **Deux énoncés marqués VÉRIFIÉ sont faux tels qu'écrits (§3.3).** Le signe des covariances deux à deux ne fixe pas P(Z ≥ 1). Contre-exemple à trois tirages, p = 0,1 : P(111) = 0,011, chaque configuration à un seul succès 0,089, P(000) = 0,722. Toutes les covariances valent +0,001, et P(Z ≥ 1) = 0,278 > 0,271 = 1 − 0,9³. À l'inverse, avec P(111) = 0 et chaque configuration à deux succès à 0,0098, les covariances valent −0,0002 et P(000) = 0,7294 > 0,729. VÉRIFIÉ (calcul ici). Une borne inférieure qui baisse ne prouve pas une baisse. L'énoncé correct demande l'association négative, que F invoque.
- **« Remplacer N par N/D »** (Duel 3) n'est pas une correction valide. Je me sers du contre-exemple de F, VÉRIFIÉ chez F : sous variable latente, P(S_n > 0) ≤ η pour tout n. Aucun facteur fini ne rétablit la garantie.
- **Duel 1, vrai par le choix de N.** q_N = M_N/N décroît avec N pour toute loi à collisions. Le verdict est une fonction de N autant que de μ.
- **Duel 1, fuite.** Les doublons injectés sont fabriqués par les transformations que le normalisateur est construit pour défaire. Le témoin réussit par construction.
- **Duel 2, trois seuils** (2,0 ; 1,5 ; 1,0), avec un mélange d'estimation ponctuelle et d'intervalle. La zone (1 ; 1,5) n'a pas d'issue.
- **Duel 4.** L'énumérateur par profondeur croissante est déterministe : ses 50 répétitions rendent la même valeur. Le verdict tient à la profondeur du premier positif, pour une seule propriété choisie par l'expérimentateur.
- **Garantie « bandits ».** La borne, au mieux de l'ordre de (K−1)·ln M/p*, dépasse le coût 1/p* d'un premier succès : elle est vide pour l'objectif posé. F le dit : pas de séparation des bras avant un succès.
- **Statuts et attributions.** Des définitions, et l'énoncé 1.C qui ne quantifie ni N ni B, portent VÉRIFIÉ sans démonstration. L'énoncé « p décroît exponentiellement avec la profondeur » est attribué à Knuth (1975), et des « axiomes de coût » à Feller (1968) : références à vérifier.

**(b) Perte de puissance, en termes de lois**

- **Duel 1.** E[M_N] = Σ_c [1 − (1−μ(c))^N] : q_N → 1 quand N est petit, → 0 quand N dépasse le support effectif. Non jugeable sans N fixé par le budget visé. r̂ = 1 est trivial s'il y a peu de classes positives à plusieurs membres : zéro violation sur m classes ne borne le taux de violation qu'à ln(1/δ)/m.
- **Duel 2.** Avec q = 0,05 et ρ = 100, le rappel critique vaut 6/101 ≈ 0,059 : H_B équivaut à r ≤ 0,059 et H_A à r ≥ 0,119. L'échantillon de m rejetés ne contient aucun positif avec probabilité ≈ exp(−m·p(1−r)/(1−q)). Dans ce cas r̂ = 1 et Γ̂ ≈ 16,8 : H_A est « validée » par construction. VÉRIFIÉ (calcul ici). Jugeable seulement si m·p(1−r)/(1−q) ≥ ln(1/δ).
- **Duel 3.** D̂ ne porte d'information que par les paires de succès dans un même bloc, d'espérance ≈ (nombre de blocs)·(Lp)²/2 sous indépendance : 0,5 pour p = 10⁻³. L'événement de substitution (classe rare) n'a pas la loi de l'indicatrice de succès.
- **Duel 4.** La médiane n'existe que si P(succès avant B) > ½ dans les deux bras.
- **Banc.** Avec 10 000 objets vérifiés, p < 10⁻⁴ donne en espérance moins d'un positif : r et Γ ont un dénominateur nul. D demande de les déclarer non estimables.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Duel 1 : des paires voisines (x⁺, x⁻) qui ne doivent pas fusionner. E l'exige pour son canoniseur ; C non.
- Duel 3 : une suite de Bernoulli indépendantes à p_t dérivant. Elle donne D > 1 sans dépendance ; sans elle, dérive et dépendance sont confondues.
- Duel 4 : une propriété définie par hachage, comme chez E et F, et une population de propriétés tirées selon une loi déclarée.
- Duel 2 : scores permutés à longueur égale.

## Sur la proposition D

**(a) Défauts de méthode**

- **Deux duels sur trois sont déjà tranchés.** D démontre lui-même que H_A est fausse dans les duels 1 et 2. Une des deux issues est impossible : la règle B4 n'est pas remplie. Ce sont des tests de calcul, pas des expériences.
- **Duel 3, seuil nul sans marge.** Sur un banc gelé, le signe de la différence est exact, mais une seule session discordante renverse le verdict. D limite sa conclusion au banc ; le duel ne répond alors pas à la question au niveau des lois.
- **« Meilleur contrôle mécanique ».** S'il est choisi sur le banc d'évaluation, c'est une sélection sur l'échantillon de test, biaisée contre le score.
- **Ancrage vrai par construction.** La propriété, la loi et le score linéaire sur les comptes de règles sont choisis par l'expérimentateur. Que le score porte un signal dépend de ce choix, non du phénomène.
- **Couverture.** Aucune méthode répandue n'est nommée ; la taille de la grammaire et le rapport des coûts ne font l'objet d'aucun duel.

**(b) Perte de puissance, en termes de lois**

- **Duel 3.** Une session à j positifs parmi m objets, dont k vérifiés, est résolue par l'ordre brut avec probabilité 1 − C(m−j, k)/C(m, k) (formule de D). Si cette probabilité est proche de 0 ou de 1 pour presque toutes les sessions, les deux politiques coïncident et la différence est nulle par plancher ou par plafond. Un test des signes bilatéral à 5 % demande au moins 6 sessions discordantes de même sens. VÉRIFIÉ (calcul ici).
- **Condition de dépendance.** Je m'en sers : la borne (1−q)ⁿ sous risque conditionnel minoré est l'objet qui convient. Son estimateur est ĥ_k = (sessions réussissant au tirage k+1)/(sessions à k échecs). Sous mélange, h_k décroît avec k. Il n'est estimable que sur des sessions indépendantes ; une trajectoire unique ne l'identifie pas. D ne propose pas cette mesure.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Duel 3 : une propriété définie par hachage, indépendante des traits du score. Tout gain mesuré y signale une fuite ou une erreur de comptabilité.
- Duel 3 : le contrôle mécanique désigné avant de voir le banc, ou sur une partie séparée.
- Duel 3 : un score appris sur des étiquettes permutées. Le gain doit être nul.

## Sur la proposition E

**(a) Défauts de méthode**

- **E1, test du mauvais nul.** Le test exact de Fisher teste Λ = 1 ; il ne contrôle aucune erreur pour « Λ ≤ 2 ». Les 40 réplicats portent sur un seul couple (générateur, propriété).
- **E1, vrai par le choix de B et de L.** La loi uniforme de référence dépend de la longueur maximale L, paramètre libre qui peut déplacer p_unif de plusieurs ordres de grandeur.
- **E2, bras presque identiques.** γ = 0 et γ = 0,20 partagent les 0,8·k premières vérifications. La règle de réfutation de H_A contient une clause, « γ = 0 manque une solution trouvée par la branche uniforme », dont la probabilité tend vers 1 avec le nombre d'instances pour tout score de rappel < 1. H_A et H_B peuvent alors être réfutées ensemble.
- **E2, fuite.** Le score vient de la même famille de modèles que le générateur : la séparation annoncée n'écarte pas les angles morts communs.
- **E3 est aveugle à la dépendance que E juge la plus grave.** Si Θ n'est tirée qu'une fois, tous les blocs d'une trajectoire la partagent. Le non-rejet y vaut en outre réfutation de H_B sans puissance établie.
- **E4 mesure la VPP, qui dépend de la prévalence** (N3 de E). Elle est mesurée là où les positifs abondent ; le paramètre à estimer est α_V.

**(b) Perte de puissance, en termes de lois**

- **E1.** Λ ≤ 1/P_hit(Unif, B) : Λ > 2 est impossible dès que P_hit(Unif, B) ≥ ½, et Λ̂ n'est pas défini si R·P_hit(Unif, B) < 1. VÉRIFIÉ (calcul ici). Le paramètre invariant est le rapport des taux de succès par unité de coût ; je me sers ici de la « loi de bascule » de C.
- **E2.** La discordance ne naît que des 0,2·k dernières places. McNemar exact à 0,01 demande au moins 8 instances discordantes de même sens, sur 50. VÉRIFIÉ (calcul ici).
- **E3.** Sous ∫ Bern(θ)^{⊗∞} dΠ(θ), la dispersion d'une trajectoire unique tend vers 1 pour presque tout θ. Var_Π n'est identifiable qu'avec des réinitialisations indépendantes. À p faible, l'information vient des paires de succès par bloc, d'espérance ≈ 200·(100p)²/2, soit 1 pour p = 10⁻³ ; le seuil χ² n'y est plus valide.
- **E4.** Il faut N·P(V=1) ≥ 460. Zéro alerte sur n négatifs certifie α_V ≤ ln(1/δ)/n : 0,009 pour 500 mutants, 4,6·10⁻⁴ pour 10 000. L'exigence α_V ≤ 0,01·p n'est alors démontrée que pour p ≥ 0,046. VÉRIFIÉ (calcul ici). Les mutants n'ont pas la loi μ(· | hors A).

**(c) Contrôles négatifs dont l'absence serait fatale**

- E1 : le même échantillonneur uniforme placé dans les deux bras ; Λ̂ doit valoir 1. Et la référence recalculée à deux valeurs de L.
- E3 : la loi nulle obtenue par permutations répétées, non par le seuil χ².
- E4 : des négatifs tirés des sorties du générateur que V* rejette.
- E2 : scores permutés à longueur égale, et un score d'une autre famille.

## Sur la proposition F

**(a) Défauts de méthode**

- **E1 ne détecte pas le contre-exemple de F.** Voir (b).
- **E1, verdict fixé par la définition du bloc.** Si un bloc est une tâche, p(Θ) varie avec la difficulté et H_B est vraie par construction. Si un bloc est une suite d'appels à graines indépendantes sur un même prompt, H_A l'est.
- **Arrêt optionnel.** « Poursuivre jusqu'à séparation » avec des intervalles bootstrap répétés n'est pas valide à tout instant. F audite ce défaut pour l'instrument 4 et ne l'applique pas à ses propres duels.
- **E2.** H_A est une conjonction ; l'intervalle (1 ; 2) n'a pas d'issue. Le lift n'est défini que sur les tâches à positifs : sélection sur l'issue.
- **E3, critère d'effondrement.** τ̂ = 0 par tâche a pour probabilité (1−τ)^{n⁺}. Avec un seul positif par tâche, elle vaut 1−τ : H_B est vraie par construction pour tout τ < 0,95. VÉRIFIÉ (calcul ici). Les positifs de l'audit élargi viennent des tâches les moins étroites.
- **E4.** Si la stratégie adaptative apprend d'une tâche à l'autre, les tâches ne sont plus des réplicats, et le gain mesure l'hétérogénéité des configurations. La « mutation locale » soumet à V des objets non tirés : autre modèle d'accès, que F signale lui-même en (a).6.
- **Tableau (c), ligne 3.** Un « faux signal de succès » à p = 0 est une fausse acceptation de V. Je reprends la remarque de D : le générateur n'annonce pas de verdict.

**(b) Perte de puissance, en termes de lois**

- **E1.** Pour la loi latente de F, D − 1 = (m−1)·p(1−η)/[η(1−p)]. Avec m = 50, p = 10⁻³, η = 0,8 : D ≈ 1,012, sous le seuil 1,10, alors que P(S_n > 0) ≤ 0,8 pour tout n. VÉRIFIÉ (calcul ici). Le second moment est insensible à la masse de Π près de 0, qui gouverne E[(1−P)ⁿ]. Je me sers de R4 de B, dont la courbe U(k) vise cet objet. La détection demande m·p(1−η)/η ≳ 0,4, donc m de l'ordre de 1/p. Les seuils 1,10 et 1,40 équivalent à une corrélation intra-bloc de 0,002 et 0,008 : c'est elle qu'il faut pré-enregistrer, pas D.
- **E2.** G_déd ≤ 1+ρ, et dépend de N_g. Un positif tel que N_g·μ(x) ≪ 1 n'apparaît qu'une fois : le classement par fréquence ne peut pas le remonter. H_B est vraie par construction dès que N_g·max_{x∈A} μ(x) ≲ 1.
- **E3.** Jugeable seulement si la loi de n⁺ par tâche rend (1−τ)^{n⁺} négligeable devant 5 %.
- **E4.** Le rapport des probabilités de succès sature : R → 1 quand n·p_max ≫ 1, et aucun bras n'est séparable quand n·p_max ≲ 1.

**(c) Contrôles négatifs dont l'absence serait fatale**

- E1 : des blocs faits de tâches différentes à tirages indépendants. Ils donnent D > 1 sans dépendance du générateur.
- E3 : un filtre synthétique qui laisse passer chaque positif avec probabilité 0,95. Le taux d'effondrement mesuré doit rester sous 5 % ; il ne le fera pas à un positif par tâche.
- E2 : départage aléatoire à fréquence égale ; le lift doit valoir 1.
- E4 : K bras identiques (R ≤ 1) et ordre des tâches permuté.

FIN-DE-CELLULE