# Proposition B, Tour III.2 : critique croisée de méthode

## Pièces et statuts

- Les quatre pièces A, C, D et E sont présentes. Chacune se termine par FIN-DE-CELLULE, et je n'y vois aucune coupure.
- Le bloc FAITS ne porte aucune étiquette de statut, et je ne lui en attribue pas. Il est identique au bloc QUESTION.
- Tout ce que j'ajoute a le statut **HYPOTHÈSE**, y compris les dérivations élémentaires, que je n'ai pas fait auditer.
- Je reprends tels quels les statuts que les auteurs ont posés. Quand une étiquette me paraît mal fondée, je le signale sans la modifier.
- Les chiffres repris des pièces restent illustratifs. Les miens sont marqués « ill. ».

## Deux outils, appliqués séparément dans chaque section

**Borne de handicap.** Supposons que la politique qui sert de référence pour l'étroitesse soit aussi un bras comparé, au même budget. Une idée n'est « étroite » que si P_R(x) ≤ 2^{−ν*}. La probabilité que ce bras produise une idée étroite-profonde (EP) est donc bornée par construction : P(R produit une idée EP) ≤ |EP_w|·2^{−ν*}. Le duel « système contre cette référence » se ramène alors à tester si le taux du système dépasse 0 plus le seuil. On ne compare plus deux chercheurs.

**CN-1, divergence triviale.** Le « système » est remplacé par la référence elle-même, légèrement déplacée : température relevée, consigne paraphrasée ou graine d'une autre famille. Aucune capacité scientifique n'est ajoutée.
- H_A : le gain EP de ce bras reste sous le seuil de décision. Le critère ne récompense pas l'écart de distribution en tant que tel.
- H_B : le gain dépasse le seuil. Tout avantage mesuré du système peut alors venir de sa seule divergence par rapport à la référence.
- Chaque issue falsifie l'une des deux hypothèses.

**CN-2, chasseur d'étroitesse.** Un générateur tire depuis la référence en rejetant les candidats estimés probables sous elle. Il n'a aucun accès à la profondeur.
- H_A : sur des mondes sans idée EP, mais avec des leurres étroits et inertes, son taux EP reste sous le taux de fausses alertes admis.
- H_B : il marque des points. Le critère EP est alors perméable à l'étroitesse seule.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **La borne de handicap s'applique à E4.** ν_{R,b} est calculée contre le modèle seul, et ce même modèle est le bras best-of-N. Si b vaut le budget B de E4, le best-of-N est majoré par |EP_w|·2^{−ν*}. A doit fixer b_ν ≪ B, ou montrer numériquement que la borne laisse au best-of-N une marge réelle.

2. **E1 est vrai par construction si l'étiquette et la mesure partagent leur source.** Le concepteur déclare une idée plantée « profonde » au vu des conséquences qu'il a construites. Si Δ est calculée par le même solveur, sur ces mêmes régimes retenus, l'AUC teste l'implémentation et non le concept. Il faut une étiquette produite indépendamment : un second jeu de conséquences tiré sans connaître x, ou un second solveur.

3. **L'oracle dilué de E3 se contredit.** Insérer l'idée plantée avec une probabilité q augmente P_R(x).
   - Si ν est estimée sur la référence diluée, on a ν ≤ log₂(1/q), soit environ 2,3 bits à q = 0,20, en deçà de ν*. L'idée plantée cesse d'être étroite.
   - La puissance mesurée devient alors une fonction décroissante de q, artefactuelle.
   - ν doit être figée sur la référence non diluée.

4. **E7 est en partie mécanique sous l'énumérateur.** Le prédicteur de déceptivité (la part d'inertes parmi les M premiers candidats énumérés) est fonctionnellement lié au rang d'énumération des idées profondes, donc à leur étroitesse sous l'énumérateur. Celui-ci est déterministe : l'indépendance des exécutions, invoquée par A, n'y change rien. H_A est en partie acquise d'avance pour cette référence.

5. **E4 appelle une correction de choix.**
   - **Risque.** Si « la meilleure référence » est désignée après les résultats, son choix parmi cinq bras introduit une sélection.
   - **Correction.** Exiger la supériorité contre chaque référence (intersection-union).

6. **La puissance de E4 est calculée contre zéro.** Les 140 mondes de A sont dimensionnés pour un écart de 5 % contre 15 % testé contre zéro. La règle exige pourtant un intervalle entièrement au-dessus de +5 points. L'écart effectif est donc de 5 points, ce qui demande environ quatre fois plus de mondes (ill.).

7. **E6 dépend du générateur de mondes.** Le ratio « gain privé / gain public » dépend de la corrélation entre conséquences publiques et privées, fixée par le générateur. Il mesure donc une propriété du générateur autant qu'une fuite. Le contrôle F3 n'y remédie qu'en partie.

### (b) Conditions de perte de puissance

- **ν et E2 :** dès que p_R(x) ≪ 3/K, on a P(N_x = 0) = (1−p)^K ≈ 1. La quasi-totalité des idées candidates est censurée au plafond log₂(K/3).
  - Le Spearman de E2 porte alors sur des ex-aequo et devient non jugeable.
  - La fiabilité de 0,9 en demi-échantillons est inatteignable par construction.
- **E1 :** si P(Δ = 0 | profonde) et P(Δ = 0 | leurre) sont tous deux grands, l'AUC tend vers 0,5 quelle que soit la validité du concept. Cela arrive quand le budget du solveur sature : conséquences insolubles même avec x, ou solubles sans x.
- **E4 (McNemar) :** le nombre de paires discordantes vaut environ n(π_S + π_R). Avec π_R borné par le handicap et π_S ≤ 0,05 (ill.), on attend moins de 8 discordances sur 150 mondes. Exclure +5 points devient impossible.
- **E7 :** avec un taux de base proche du plancher de 2 % de A, chaque quartile d'environ 37 mondes attend moins d'un succès. L'intervalle du ratio de densités n'est pas borné.
- **Borne de biais du juge :** si TPR − FPR tend vers 0, la différence corrigée entre bras n'est plus bornée.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1.** L'A/A de A ne le remplace pas : le handicap frappe identiquement les deux copies, et l'A/A ne peut donc pas le voir.
- **CN-2.** Le bras « bizarre » de A n'émet que des leurres scriptés. Il obtient zéro par construction et ne teste rien.
- **Profondeur conditionnée par une autre idée.** Calculer Δ(x) sur des conséquences engendrées à partir d'une autre idée plantée x′.
  - H_A : Δ(x) ≈ 0.
  - H_B : Δ(x) > 0, et la profondeur mesure alors la compatibilité générique avec le solveur.
- **ν figée.** Dans E3, ν doit être calculée sur la référence non diluée, sinon E3 est inopérante.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **L'équivalence extensionnelle fait s'effondrer les classes éligibles.**
   - Deux règles sont la même idée si elles prédisent la même chose sur tout le domaine.
   - Toute règle fausse est inéligible.
   - Donc toute règle éligible qui prédit l'ensemble des observables coïncide avec la vérité cachée : il n'y a qu'une classe éligible par monde.
   - Le plan en quatre quadrants n'existe alors que pour des règles partielles. L'équivalence entre règles à domaines emboîtés n'est pas définie, et l'étroitesse d'une règle partielle dépend de cette convention.

2. **L'énumérateur à ordre randomisé ne discrimine rien.** Sous une permutation uniforme de M classes, au budget B, on a p_enum(c) = B/M pour toute classe c.
   - Cette politique n'apporte qu'un plancher constant au maximum des probabilités.
   - Si B/M ≥ τ, aucune classe n'est étroite.

3. **La borne de handicap s'applique.** Le « modèle solo avec outils » sert à la fois de politique d'étroitesse et de bras gelé. Les recherches de référence sont indépendantes de celles qui nomment les classes, ce qui règle la sélection mais pas le handicap.

4. **La source des problèmes aval n'est pas spécifiée.** C les tire « secrètement », sans dire par quel générateur.
   - Si ce générateur est conditionné par la règle plantée c, la profondeur de c est fabriquée.
   - Le placebo « règle vraie de même longueur » ne protège que si sa propre profondeur est tirée du même mécanisme.

5. **Plusieurs statuts VÉRIFIÉ ne sont pas auditables ici.** C étiquette VÉRIFIÉ deux citations bibliographiques. Je ne modifie pas ces statuts, mais rien dans les pièces ne permet de les auditer.

6. **Mérite à retenir.** Seule C dimensionne la puissance contre l'écart au seuil (« g au seuil, non à zéro »). Ce défaut, présent chez A, D et E, ne s'applique pas à C.

### (b) Conditions de perte de puissance

- **Maximum des probabilités sur R politiques.** Pour borner simultanément max_r p_r < τ avec zéro occurrence, il faut environ n ≥ ln(R/α)/τ exécutions par politique (ill.).
  - Si une politique a un p_r vrai compris entre τ/2 et τ, la puissance de la déclaration « étroite » s'effondre.
  - Le maximum est dominé par la politique la plus bruitée.
- **Profondeur.** La borne inférieure de la différence appariée doit dépasser 0,15 (ill.). Cela échoue si les fractions résolues avec et sans c saturent toutes deux, près de 0 ou de 1. Cela échoue aussi si le nombre m de problèmes aval par classe est petit, l'écart-type étant de l'ordre de √(1/m).
- **Duel principal.** Si π_S < 0,05 (ill.), H_A : T > 0 est impossible. Seule une borne supérieure non positive peut conclure, au prix d'un n que la discordance q, faible, rend très grand.
- **Duel des régions.** Avec 40 familles (ill.) et une forte variance de rendement entre familles, l'intervalle simultané couvre 0 : le duel est non décisif.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** C prévoit déjà la « règle vraie très rare portant sur une variable inutilisée ». C'est un cas scripté et non un chercheur : il ne remplace pas CN-2.
- **Monde à classe éligible unique.** Le pipeline ne doit rapporter aucune autre classe EP.
  - H_A : zéro classe rapportée en plus.
  - H_B : des classes en plus sont rapportées, et l'équivalence extensionnelle est mal implémentée.
- **Aval conditionné par une autre règle.** Le gain de c doit être nul sur des problèmes aval engendrés à partir d'une règle c′.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Des choix de conception sont étiquetés VÉRIFIÉ.** Exemples : la correction du quotientage par e-graphes, l'effet « obfuscation » d'un retour de N, la borne adaptative en O(√(T ln|X|/n)). Je ne change pas ces statuts. Je signale qu'en Phase I, les critères d'arrêt reposent sur la correction du quotient, qui est une hypothèse à tester (porte 5) et non un acquis.

2. **N n'a pas de gradation au seuil choisi.** Avec les valeurs de D (M0 = 1000, α = 0,05) :
   - zéro occurrence donne N ≈ −ln(1 − 0,05^{1/1000}) ≈ 5,81 nats ;
   - une occurrence donne N ≈ −ln(0,00474) ≈ 5,35 nats (ill.) ;
   - le seuil τ_N = 5,5 équivaut donc à « jamais vu en 1000 tirages ».
   
   L'excès continu Z n'en tire aucune gradation. Le décalage médian ΔN ≥ 0,7 nat de Exp. III est mécaniquement borné par ce plafond.

3. **Budget de référence et budget de comparaison.** Les tirages de référence sont « courts » (b0), alors que B = 64 000 jetons. Si B/b0 ≥ M0/3, un best-of-N au budget B devrait trouver des idées dites étroites avec une probabilité non négligeable. L'étroitesse n'est donc définie qu'au budget b0, et non au budget de la comparaison. Inversement, si la référence et le bras coïncident en budget, la borne de handicap s'applique (μ0 inclut le modèle de base seul).

4. **D_MDL est biaisée vers le haut.** La troncature max(0, ·) régime par régime en est la cause. Pour une expression x non pertinente, soit s l'écart-type du bruit de L_null − L(D_r|x). On a alors :
   - E[Σ_r max(0, ·)] ≈ 0,4·R·s ;
   - les leurres passent τ_D dès que 0,4·R·s > K + τ_D.
   
   De plus, si les constantes de x sont ajustées sur D_r, il y a fuite : la profondeur est calculée sur les données d'ajustement.

5. **Exp. I est vraie par construction pour l'énumérateur.** Les trois DSL sont « formellement isomorphes ». Si l'isomorphisme préserve la taille, le classement par coût est identique et τ_K = 1. S'il ne la préserve pas, Exp. I mesure les fonctions de coût, pas la stabilité de la cible.

6. **Exp. IV est en partie circulaire.** S_region = 1 signifie que les références simples échouent. Or N est définie par l'échec des références. Davantage d'idées N-élevées par définition entrent dans le numérateur de l'odds ratio.

7. **Exp. V viole B4 dans une zone intermédiaire.** Si Δ < 10 nats mais que la chute relative atteint ou dépasse 5 %, aucune des deux hypothèses n'est falsifiée. Les hypothèses sont exclusives, mais pas exhaustives.

8. **La puissance n'est pas cohérente avec la règle.** La Phase IV dimensionne 100 problèmes pour détecter 0,05 contre 0,18 testé contre zéro. La règle d'intersection-union exige pourtant δ_min = 0,10. L'excès effectif est de 0,03, ce qui demande de l'ordre de (1,96 + 0,84)²·0,2/0,03² ≈ 1,7 × 10³ paires (ill., avec une discordance de 0,2).

9. **Certaines exigences ne sont pas certifiables.** « TPR_causal = 1,00 » ou « FPR = 0 » ne se certifient pas statistiquement : seules des bornes unilatérales sont estimables.

### (b) Conditions de perte de puissance

- **Exp. II :** si π_MA − max_b π_b est proche de δ_min, la puissance de l'intersection-union est d'environ 0,5 au mieux (ill.). Avec π_b plafonné par le handicap, le test se réduit à π_MA ≥ 0,10.
- **Exp. III :** avec N censurée au voisinage de 5,8, la distribution de N des retenus est bimodale (sous τ_N ou au plafond), et le décalage médian est non jugeable.
- **Exp. IV :** si P(solution EP | S = 0) tend vers 0, l'odds ratio diverge sans information. Avec 60 problèmes par strate et une prévalence de quelques pour cent (ill.), le test de Fisher conclut rarement.
- **Exp. VI :** une borne de FPR inférieure à 0,01 sur 500 négatifs n'est atteinte qu'avec au plus environ 1 alerte, la borne à zéro alerte étant d'environ 0,006 (ill.). La moindre alerte rend H_B infalsifiable.
- **Correction Rogan-Gladen :** si TPR_g − FPR_g tend vers 0, π_g n'est pas borné.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** L'A/A de BestOfN-Mono est aveugle au handicap.
- **D_MDL d'expressions aléatoires.** Mesurer D_MDL pour des expressions de même K_L, non reliées au monde, avec les constantes figées sur D_train.
  - H_A : E[D] ≤ 0.
  - H_B : E[D] > 0, et la troncature fabrique de la profondeur.
- **Isomorphisme non conservatif.** Inclure dans Exp. I un isomorphisme qui ne conserve pas la taille, sans quoi Exp. I ne peut pas échouer pour l'énumérateur.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **R est estimée par un estimateur ponctuel sans protection contre la sélection.**
   - R = min_Q(−log₂ p̂_Q) utilise p̂ ponctuel. Pour une idée jamais vue, p̂ = 0 et R = ∞ : l'estimateur n'est pas défini sur l'événement dominant.
   - E ne précise pas que p̂ est estimé sur des exécutions disjointes de celles qui ont produit les idées évaluées. A et C le font.
   - Sans cette disjonction, les idées retenues parce que la référence les a manquées par hasard paraissent étroites, par régression vers la moyenne.

2. **U contredit sa propre justification.** E écarte le « maximum brut » parce qu'il récompense la variance. Or U(P, B) = max_{x∈S(P,B)} D_ext·𝟙[·] est un maximum sur tout l'ensemble engendré S, et non sur la sortie sélectionnée.
   - **Le harnais court-circuite le sélecteur.** Il évalue D_ext sur tout S et agit comme un sélecteur parfait. La sélection du système n'est donc plus mesurée.
   - **U croît avec |S|.** Il favorise le bras qui produit le plus de candidats sur l'axe budgétaire non égalisé : l'énumérateur à FLOPs égaux, le modèle de langage à appels d'oracle égaux.

3. **L'égalisation simultanée des deux budgets (E5) est impossible.** E note lui-même 10⁶ appels pour l'énumérateur contre 10² pour un modèle (ill.). Ce que H_A compare n'est pas défini : deux duels, chacun à un axe fixé et l'autre libre ?

4. **L'enveloppe par problème est biaisée et change l'estimande.** Pour E[U_multi − max_b U_b], on a E[max_b U_b] ≥ max_b E[U_b] : le critère est plus sévère que « meilleur que chaque référence ». La correction de Holm qui s'y ajoute est redondante.

5. **Les seuils standardisés dépendent des données.** Les seuils exprimés en σ dépendent d'un écart-type estimé, dont la source et les bras inclus ne sont pas spécifiés.

6. **E3 relève de la pseudo-réplication.** L'hypothèse porte sur des familles, et il n'y en a que 4 (2 prédites fertiles, 2 négatives). Les 40 problèmes par famille ne sont pas des réplications de l'interaction. Le n effectif pour « la taxonomie prédit » est de 4. De plus, E3 valide sur un modèle de 8B et E5 exploite un modèle de 70B : le transfert est supposé.

7. **E2 agrège trois hypothèses.** L'invariance, le juge et la contamination sont réunis dans un seul H_A. Un échec ne dit pas laquelle est réfutée, ce qui ne satisfait pas l'inférence forte au sens de B4.

8. **La puissance est calculée contre zéro.** N ≈ 50–60 pour d = 0,5 est calculé contre zéro, alors que la règle exige δ₅ = 0,20σ. L'effet effectif est de 0,30σ, ce qui demande environ 2,8 fois plus de problèmes (ill.).

9. **Statuts.** P1 est étiqueté « RAPPORTÉ » sans référence. Je ne change pas ce statut, mais il n'est pas auditable dans la pièce.

10. **Borne de handicap.** Elle s'applique si Q_LLM-1 est le modèle du bras Best-of-K au même budget.

### (b) Conditions de perte de puissance

- **R :** si p_Q(x) ≪ 1/n_Q pour la plupart des idées, la fraction de R infinies tend vers 1. La moyenne et l'aire sous la courbe sont alors non définies ou dominées par la convention de plafond.
- **U comme maximum :** si D_ext a une queue droite lourde, la variance de U croît avec |S|. Le bootstrap en grappes sous-couvre quand la différence entre bras est portée par quelques problèmes extrêmes.
- **PPI :** avec une prévalence de positifs π et un sous-échantillon audité de taille n, on attend nπ positifs audités. Si nπ < 10 environ (ill.), l'intervalle PPI est plus large que tout effet réaliste. C'est le cas en régime rare, précisément celui visé.
- **E3 :** avec 4 familles, l'interaction n'a pratiquement aucun degré de liberté au niveau famille. La conclusion reste non jugeable quelle que soit la taille par famille.
- **E5, arrêt pour futilité :** si la variance entre problèmes est inconnue avant le pilote, la puissance conditionnelle à 50 % est elle-même très incertaine. La règle « < 0,10 » peut arrêter un vrai effet.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** CN-2 est d'autant plus nécessaire que U récompense le volume.
- **Étroitesse par sélection.** Évaluer R sur les sorties d'une réplication de référence, d'abord avec les mêmes exécutions qui les ont produites, puis avec des exécutions disjointes.
  - H_A : aucun excès d'étroitesse avec les exécutions disjointes.
  - H_B : un excès apparaît, et l'estimateur fabrique de la rareté par sélection.
- **Bras à volume gratuit.** Un bras émet beaucoup de candidats aléatoires valides à coût négligeable sur l'axe non égalisé.
  - H_A : U reste au niveau du tirage aléatoire.
  - H_B : U monte, et la métrique mesure le volume.

FIN-DE-CELLULE