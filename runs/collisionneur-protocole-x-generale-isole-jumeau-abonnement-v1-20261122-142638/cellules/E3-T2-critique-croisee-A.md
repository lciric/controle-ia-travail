# Proposition A, tour III.2 : critique croisée de méthode

**État des pièces.** Les pièces B, C, D et E sont présentes et closes par leur marqueur ; D est plus courte (2 duels annoncés, 2 présents), sans coupure visible. Ma conception du tour III.1 (A) n'est pas transmise : je ne m'y réfère pas. Le bloc FAITS reproduit la question et ne contient aucun fait doté d'un statut. Empreintes non recalculées (OBSERVÉ-NON-AUDITÉ).

**Statuts.** Mes critiques portent sur des protocoles non exécutés : ce sont des HYPOTHÈSES, sauf mention « VÉRIFIÉ (calcul) », qui ne couvre que l'arithmétique. Les entrées de ces calculs sont les valeurs illustratives des pièces ; tout autre chiffre est illustratif.

## Sur la proposition B

**(a) Défauts de méthode**

1. **Le duel 5 ne peut guère échouer.** Les paramètres sont mesurés « pour chaque instrument et chaque axe » : ce qui est commun aux trois axes est une forme fonctionnelle, pas un paramètre. Sur n ∈ {2, 4, 8}, une loi a·nᵇ calée sur n = 2 et n = 8 reproduit √(n/(1+(n−1)ρ)) à n = 4 à 2,5 % près pour ρ = 0,1 et 2,7 % pour ρ = 0,3 (VÉRIFIÉ, calcul). La marge de 5 % est donc tenue quasi par construction, et la tolérance de 15 % teste la stationnarité entre T_cal et T_test, pas la loi.
2. **Axe « instruments » mal défini.** Trois témoins hétérogènes (texte, sonde, autre famille) ne donnent ni n = 4 ni n = 8 et n'ont pas de d'₁ commun.
3. **Le ρ de la classe sabotage confond bruit partagé et hétérogénéité du signal.** Deux détecteurs valides corrèlent dans la classe positive dès que l'intensité du sabotage varie entre trajectoires. Ce ρ-là ne plafonne pas la détection à taux de fausses alertes fixé comme le prévoit la formule. L'attente E3 hérite du défaut.
4. **Estimation de α.**
   - Le dommage par acte, estimé par rejeu, est un régresseur bruité : la pente est atténuée vers 0, donc biaisée vers H_A.
   - Le logarithme de l'écart de score exclut les écarts ≤ 0 : troncature.
   - Si le dommage naît de la composition des actes (la prémisse), les dommages marginaux ne somment pas à H.
   - k est assigné, mais le modèle choisit type et position des actes : taille confondue avec type.
   - « Doubler l'effectif si l'IC chevauche 1 » est un arrêt optionnel non corrigé.
5. **Duel 3 : point focal planté.** La conclusion cible est imposée au saboteur ; l'accord entre copies saboteuses vient alors de la consigne, pas des poids. La condition X ne lève pas l'ambiguïté : elle change à la fois poids, compétence et plancher de divergence honnête.
6. **Duel 4 : effet de composition.** Garder les sabotages « réussis et notés bas » modifie le mélange de tâches et de types d'actes. Le contrôle « score aléatoire » égalise la KL, pas ce mélange.
7. **Duel 6 : espaces d'action inégaux.** U choisit dans l'union des instruments, S dans ceux d'un seul article. Le contraste pertinent est U − U(ρ=0), relégué en contrôle.
8. **Fuites.**
   - Les mêmes organismes saboteurs servent en T_cal et T_test.
   - Le jeu d'entraînement de la sonde n'est pas situé par rapport à T_cal (d'₁ optimiste s'il est commun).
   - Le k du duel 1 est choisi parmi trois sans correction.

**(b) Conditions de perte de puissance**

- **d' = √2·Φ⁻¹(AUC).** Non jugeable si σ₁²/σ₀² ≠ 1 ou si la loi sous sabotage est un mélange (1−π)F₀ + πF₁ ; estimateur : pente de la z-ROC. Alors d' ne détermine plus le taux de détection à 1 % de fausses alertes, et les duels 5 et 6 peuvent diverger.
- **ρ.** Sans effet mesurable quand (n−1)ρ ≪ 1 ; indiscernable de a·nᵇ tant que n ≤ 8. Sous corrélation ρ^|i−j| (axe temporel), le ρ moyen dépend de n.
- **α.** L'estimateur converge vers α·λ, avec λ = σ²_log h / (σ²_log h + σ²_u). Si λ < 1/α, la limite est ≤ 1 alors que α > 1. λ s'estime par rejeux répétés.
- **Seuil de 1 % par pas.** Sur T pas indépendants, le taux de fausses alertes par trajectoire vaut 1 − 0,99ᵀ, soit 18 % à 45 % pour T de 20 à 60 (VÉRIFIÉ, calcul).
- **Rapport détection_S / détection_L.** Variance relative ≈ CV²_S + CV²_L ; indéterminé si détection_L approche le taux de fausses alertes.
- **U − S.** Plafonné si la prévalence est inférieure à la fraction vérifiée et l'AUC élevée ; borné par la part non commune des ensembles envoyés en vérification.

**(c) Contrôles négatifs dont l'absence serait fatale**

- ρ partiel, recalculé après régression sur le dommage mesuré.
- Duel 3 : mêmes poids avec cibles tirées indépendamment ; rééchantillons honnêtes de l'autre famille.
- Duel 5 : scores synthétiques non échangeables (AR(1), variances inégales) que la chaîne doit rejeter. Le contrôle actuel teste le niveau, pas la puissance.
- Duel 4 : sélection sur un score apparié en composition de tâches mais indépendant du moniteur.
- Un organisme saboteur absent de la calibration.

## Sur la proposition C

**(a) Défauts de méthode**

1. **La « loi de conservation » mêle une identité et une conjecture.**
   - Si la loi de la conclusion diffère entre honnête et saboteur, alors Σ_t KL_t(texte) ≥ KL(conclusion), donc max_t KL_t ≥ KL(conclusion)/T (VÉRIFIÉ, calcul : inégalité de traitement des données et règle de chaîne). La trace conjointe (activations, texte) en porte au moins autant.
   - La signature ne peut donc pas s'annuler partout : cette partie est vraie sans expérience.
   - Reste empirique le fait que des moniteurs de classe bornée (sonde, juge) la captent. C'est une propriété des moniteurs, et la grandeur « conservée » n'est jamais définie.
2. **Duel 3 asymétrique.** L'adversaire est pénalisé sur le sous-espace de sondes linéaires, puis évalué contre des MLP réentraînés, sur 6 valeurs de λ et 3 graines. « Aucun λ* trouvé » reflète autant la faiblesse de l'optimiseur qu'une contrainte de capacité. H_B, universelle, ne peut être « établie » par recherche finie (règles 1 et 5). De même, un seuil illustratif (85 % à t = 3) porte VÉRIFIÉ.
3. **Contrôle du duel 3 inactif.** Chez l'agent honnête, la projection sur le sous-espace de sabotage est déjà faible : la pénalité n'agit pas et le contrôle passe par construction.
4. **Duel 1 : sélection asymétrique.** Le saboteur est filtré pas à pas sur le moniteur texte, jamais sur la sonde ; comparer ensuite sonde et texte cumulé favorise H_B. Avec un saboteur par consigne, la sonde lit la consigne, présente à chaque pas. Le cas H5 de B (je m'en sers) manque ici.
5. **Adaptateur confondu avec sabotage.** Entre un saboteur LoRA et une base honnête, sondes et fragilité au bruit injecté peuvent détecter l'adaptateur.
6. **Duel 2.**
   - Régime « une copie infiltrée » : la divergence est acquise par construction.
   - Régime systémique : l'issue dépend du choix de l'expérimentateur (biais inconditionnel ou déclenché par le contexte).
   - Paraphrase et bruit sont administrés ensemble.
7. **Duel 4 : comparateur faible.** Toute cascade guidée par un signal d'AUROC > 0,5 bat des fractions fixes ; cela ne mesure pas le couplage des articles. Aucun découpage réglage/test n'est décrit. L'oracle programmatique réduit le rappel à la précision du ciblage.
8. **Zones mortes, contre B4.** Chaque duel laisse un intervalle où rien n'est falsifié : ΔAUROC de 0,05 à 0,15, R_div de 1,20 à 1,80, ΔRappel de 5 à 15 points.

**(b) Conditions de perte de puissance**

- **AUROC.** Écart-type ≈ 0,025 à AUC = 0,6 si 250 + 250 trajectoires (VÉRIFIÉ, calcul par la formule de Hanley & McNeil, 1982, *The Meaning and Use of the Area under a Receiver Operating Characteristic (ROC) Curve*, citée de mémoire). Les seuils 0,55 / 0,60 / 0,65 sont séparés d'une demi-largeur d'IC à 95 %, moins par cellule (λ, graine).
- **Filtre « chaque pas sous q₉₅ honnête ».** Une trajectoire honnête de 25 pas dépasse q₉₅ au moins une fois avec probabilité 1 − 0,95²⁵ ≈ 72 % (VÉRIFIÉ, calcul, pas indépendants). La loi du saboteur est tronquée ; l'AUROC du texte cumulé peut passer sous 0,5 par troncature.
- **CUSUM.** Niveau non tenu si les incréments honnêtes sont autocorrélés (φ) : la variance des sommes partielles est multipliée par ≈ (1+φ)/(1−φ).
- **R_div.** Rapport de moyennes, instable si la divergence honnête est à queue lourde. Si P_S(conclusion | tâche) est concentrée, R_div < 1 et un seuil unilatéral est aveugle.
- **ΔRappel.** Avec 100 positifs et un rappel ≈ 0,5, l'écart-type de la différence vaut 5 à 7 points selon la corrélation des bras ; les seuils 5 et 15 sont distants de 1,4 à 2 écarts-types.
- **ΔU_sabotage.** Non jugeable si la variance entre 3 graines dépasse l'écart 0,15–0,30.

**(c) Contrôles négatifs dont l'absence serait fatale**

- LoRA honnête (même procédure, même pénalité) pour toute mesure sur activations ou sous perturbation.
- Consigne de sabotage présente mais inactive.
- Duel 1 symétrique : filtrage sur la sonde, comparaison au texte.
- Duel 3 : adversaire entraîné contre la classe de sonde évaluée ; contrôle positif d'évasion sur un sabotage en un pas ; objectif caché bénin tenu 25 pas sous la même pénalité.
- Duel 4 : fusion tardive des trois scores à budget égal ; cascade à signaux permutés.

## Sur la proposition D

D est la plus soignée sur les fuites (familles de dossiers séparées, gel des règles, branche unique visible) ; je m'en sers comme étalon. Ses défauts sont ailleurs.

**(a) Défauts de méthode**

1. **Pas d'adversaire.** Perturbations placées par l'expérimentateur, modèle non réentraîné, notes biaisantes écrites à la main : la loi du lieu du dommage est celle du plan d'expérience, et la règle l'apprend.
2. **Transfert planté.** Les trois régimes partagent dossiers, graphe de dépendances, générateur de perturbations et perte. Une règle « vérifier les nœuds à nombreux descendants » se transfère sans rien lire des instruments. Le graphe étant caché au défenseur, T peut battre M en l'inférant du texte : c'est de la compréhension de tâche.
3. **Décisions forcées.** Une décision insérée n'est pas décidée par le modèle : les activations lues mesurent la surprise devant un texte imposé. La sonde vaut alors une log-vraisemblance des jetons insérés, que le témoin « norme des activations » ne couvre pas.
4. **Duel 1 : I dépend de la règle de notation.** Avec une perte « fraction de conclusions incorrectes », deux perturbations sur une même chaîne sont sous-additives si chacune suffit à fausser la conclusion, sur-additives si chacune reste sous le seuil. Le signe de I est fixé avant tout agent.
5. **Spécialiste affamé.** À nombre égal de trajectoires étiquetées, un S bruité rend la non-infériorité facile : T gagnerait par volume de données, non par transfert.
6. **Article 3 réduit à un changement de présentation.** Rien ne vise la règle T elle-même.

**(b) Conditions de perte de puissance**

- **I.** Différence de différences ; la variance inclut k·σ²_iso/n pour la somme des pertes isolées. Non jugeable si ce terme atteint (marge/2)². Si la loi des pertes isolées est dégénérée en 0, la soustraction est vide et I égale l'effet de seuil.
- **G.** Minimum de six écarts (test intersection–union) : puissance ≤ la plus faible des six ; chaque écart doit dépasser ≈ 2,4 écarts-types (Bonferroni unilatéral).
- **Marges.** H_A est impossible si L_sans contrôle − L_oracle < b + m dans un régime ; indécidable si L_M ≈ L_oracle.
- **Non-infériorité.** Interprétable seulement si |L_S(n) − L_S(n/2)| < m.
- **Permutation intra-dossier.** Sans résolution si la corrélation intra-classe de la perte évitable tend vers 1 : le gain vient du choix du dossier, la permutation le conserve, et le critère de D rejetterait à tort le ciblage. De même si chaque dossier n'offre qu'une occasion utile.
- **Bascules canonique → brut.** Puissance fixée par le nombre de paires discordantes ; biais si le moniteur est stochastique.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Négatifs honnêtes eux aussi insérés par forçage, de même log-vraisemblance ; log-vraisemblance comme vérification mécanique.
- I_prog : mêmes perturbations propagées par le seul programme de référence ; la part de l'agent est I − I_prog.
- T privé des signaux de moniteurs ; M avec accès oracle au graphe.
- Un régime issu d'un autre générateur de dossiers et de perturbations.
- Un placement choisi contre T gelé, à perte finale égale.
- Bascule canonique → canonique rééchantillonné.
- Courbe d'apprentissage de S.

## Sur la proposition E

**(a) Défauts de méthode**

1. **Le non-significatif vaut falsification.** « Écart sous le seuil ou p ≥ 0,05 ⇒ hypothèse falsifiée » dans les duels 2, 3 et 4. Au duel 3, la thèse attendue par E est du côté du résultat nul : un essai peu puissant la confirme. Il faut des tests d'équivalence à marge préenregistrée.
2. **Duel 2 : conditionnement post-traitement.** Fixer Δ_dir = 0,25 ± 0,03 sélectionne, parmi les politiques d'évasion, celles qui gardent l'impact. Δ_dir n'est égalisé qu'à la fin, pas aux 3 pas sondés.
3. **Duel 2 : quantité de réglage.** L'adversaire d'évasion a reçu plus de pas de gradient ; plus loin de la base, il est plus sensible à tout remplacement d'historique. Le contrôle « style neutre » porte sur le modèle honnête, pas sur ce surcroît.
4. **Duel 2 : signe non dérivé.** Si l'évasion étale le biais, la divergence par pas baisse et le nombre de pas touchés monte : la moyenne sur 3 pas peut aller dans les deux sens. L'auteur du « résumé neutre » n'est pas précisé ; si c'est le modèle testé, le résumé porte le biais.
5. **Duel 1.** AUROC ≤ 0,60 est une absence de détection : un moniteur faible rend H_A vraie. Le maximum sur deux moniteurs et « au moins une méthode » ne sont pas corrigés.
6. **Duel 3.** Trois copies au même adaptateur : accord quasi acquis si le biais est inconditionnel. La thèse propre de E (seul le cloisonnement aide) reste un « diagnostic secondaire », qu'aucun duel ne décide. La vérification coûteuse, commune aux bras, comprime l'écart.
7. **Duel 4.**
   - Le bras modulaire est linéaire et tardif, le bras conjoint non linéaire et séquentiel : classe de modèles, calendrier d'information et usage du budget varient ensemble. Le contrôle par permutation de E est utile (je le retiens) mais ne sépare pas ces facteurs.
   - Le « silence suspect » n'existe que si l'adversaire minimise les scores au lieu d'imiter leur loi honnête.
   - L'adversaire n'est pas adapté à la politique conjointe.
   - Deux familles d'adversaires : un seul transfert possible.
   - Les données de durcissement des moniteurs ne sont pas situées par rapport au test.
8. **Statuts.** Une référence « citée de mémoire » porte VÉRIFIÉ (Wald 1945) : incohérent avec la règle 3.

**(b) Conditions de perte de puissance**

- **AUROC_étape.** Pas groupés par trajectoire : effectif efficace n/(1+(m−1)·ICC), m = 20, tendant vers 300 si l'ICC est forte. Non jugeable sans borne haute d'IC ≤ 0,60 ni AUROC élevé du même moniteur sur un sabotage non dilué.
- **Fenêtre Δ_dir.** Tenable à deux écarts-types seulement si l'écart-type par tâche est ≤ 0,26 pour 300 tâches (VÉRIFIÉ, calcul) ; biais résiduel ≤ pente(z_CF | Δ_dir) × 0,06.
- **z_CF.** Loi bornée, asymétrique, dépendante de la longueur et de la position du pas : 0,30 écart-type peut venir d'un déplacement de la loi des longueurs. Si le biais occupe s pas sur 20, trois sondes uniformes en touchent au moins un avec probabilité 1 − C(20−s,3)/C(20,3), soit 40 % pour s = 3 (VÉRIFIÉ, calcul) : la mesure varie avec s à divergence par pas constante.
- **McNemar.** Pour 8 points sur 300 tâches, χ² = 6,4 si 30 % de paires discordantes, 3,84 (valeur critique) si 50 % (VÉRIFIÉ, calcul). Au-delà, indécidable.
- **Fausses alertes « fixées à 5 % » sur 300 honnêtes.** Taux réalisé 5 % ± 2,5 points (VÉRIFIÉ, calcul binomial) ; l'erreur induite sur la détection, proportionnelle à la pente locale de la ROC, n'est pas comptée par McNemar.
- **Permutation du duel 4.** Détruit aussi la dépendance commune à la difficulté de la tâche ; non discriminante si cette covariable explique la covariance entre instruments.

**(c) Contrôles négatifs dont l'absence serait fatale**

- Sabotage non dilué de même Δ_dir, détecté par les mêmes moniteurs locaux.
- Duel 2 : saboteur réglé autant, avec une pénalité sans rapport avec les moniteurs ; historique paraphrasé sans neutralisation ; résumé produit hors du modèle testé.
- Duel 3 : bras cloisonné rendu décisionnel ; relecteurs d'une autre famille, sans quoi un gain nul ne dit rien des poids partagés.
- Duel 4 : fusion tardive non linéaire ; bras modulaire avec le même accès séquentiel au budget ; adversaire imitant la loi honnête des scores ; permutation stratifiée par difficulté.

FIN-DE-CELLULE