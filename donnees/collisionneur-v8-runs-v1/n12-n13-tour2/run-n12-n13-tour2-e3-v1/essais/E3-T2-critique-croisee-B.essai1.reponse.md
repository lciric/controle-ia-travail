# Proposition B — Tour III.2 : critique croisée de méthode

## Préambule

Les pièces analysées ci-dessous sont les conceptions du tour III.1 de A, C, D et E. Mes statuts sont ceux de la synthèse v2 : tout chiffre repris de la synthèse est RAPPORTÉ ; mes propres assertions sont HYPOTHÈSE sauf mention. Les chiffres qui ne viennent ni de la synthèse ni de la question sont « illustratifs ». Les six pièces du tour 1 et les deux lectures scellées ne sont pas servies ; je n'en invente pas le contenu.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D1 — « pression manifeste » par un comportement bénin collectif-seulement planté.** Le comportement planté (convention de format partagée) est un stimulus choisi par le concepteur. L'agent peut l'adopter sans que la pression d'optimisation ait produit l'insularité d'Avalon : la convention est un équilibre de coordination, pas un équilibre social de dissimulation. Si l'agent l'adopte sous crédit individuel aussi (par simple imitation entre agents partageant un contexte), le bras « crédit permuté » ne l'isole pas. **Confondant :** type de jeu (coordination vs dilemme social) et mécanisme cible (pression d'optimisation collective → omission). Le contrôle négatif « bras à crédit permuté » ne ferme pas cette porte : un agent qui lit les traces de ses pairs dans le contexte peut reproduire une convention indépendamment du crédit.

2. **D2 — dilution, simulation sur processeur.** A fixe un rapport de variances hors de [0,8 ; 1,25] comme seuil. Si le modèle de bruit est symétrique et la taille du groupe M est faible (M = 4, comme proposé dans les duels d'entraînement), la variance de sélection sous crédit plat est analytiquement calculable : Var(R_plat) = σ²/M + (M−1)·Cov/M. Le résultat dépend entièrement de la covariance inter-agents Cov, qui est un paramètre libre du modèle de bruit. **Vrai par construction** si Cov = 0 (rapport = 1/M, hors bande pour M ≥ 2) ; **vrai par construction** dans l'autre sens si Cov = σ² (rapport = 1). Le duel ne falsifie rien : il illustre un choix de Cov. Le contrôle négatif « deux bras au même crédit, rapport attendu 1 » vérifie le simulateur, pas l'hypothèse.

3. **D3 — « le lecteur de la précaution lit ».** A propose de planter des chutes dans un journal synthétique et de mesurer le rappel du lecteur (sous-agent d'une autre famille). Mais les chutes plantées ont une amplitude fixée (10, 20, 30 points). Si l'amplitude réelle en production est plus faible (par exemple 5 points, étalée sur trois points de contrôle), le rappel mesuré sur les chutes grossières ne prédit pas la sensibilité réelle. **Fuite construction/évaluation** : le concepteur du test choisit l'amplitude, et le lecteur est évalué sur ce choix ; le spectre d'amplitudes réel est inconnu.

4. **D6 — confiance des juges.** A écrit : « ≤ 0,55 falsifie H_A → RLCR sans objet ». Cela suppose que l'absence d'information dans la confiance brute implique que l'entraînement RLCR ne peut pas en créer. Or Damani montre précisément que RLCR améliore la calibration d'un modèle dont la confiance brute est quasi nulle (AUROC 0,47–0,56, pièce 5, l. 807, RAPPORTÉ). L'issue « RLCR sans objet » ne suit pas de « confiance brute non informative » ; elle suit seulement de « aucun signal exploitable dans les représentations internes », ce que l'AUROC sur la confiance verbalisée ne mesure pas. **Variable confondante** : information superficielle (confiance verbalisée) prise pour proxy de l'information latente.

5. **Divergence 1 — cession à C.** A cède que (ii) ≡ (iii) « pour la trajectoire » sous couche 3 fermée, mais conserve « le résidu se lit dans le journal ». Si les moniteurs neufs ne sont jamais générés (couche 3 fermée), aucun journal ne contient leur sortie ; le résidu mesurable est celui du catalogue existant (convergence 11), pas celui d'un moniteur hypothétique. La cession est cohérente dans l'énoncé mais inopérante dans la mesure : le résidu de moniteurs neufs ne peut pas être lu s'ils n'existent pas.

6. **Divergence 3 — contrôle de pression.** A propose un « comportement bénin qui ne paie que sous crédit collectif ». Pour qu'un tel comportement n'apparaisse que sous crédit collectif et pas sous crédit individuel, il faut que l'agent individuel n'ait aucune incitation privée à l'adopter. Mais un agent qui lit le contexte partagé peut adopter une convention de format pour réduire ses propres coûts de coordination, indépendamment du crédit. Aucune garantie formelle que le comportement soit strictement collectif-seulement n'est fournie ; c'est une HYPOTHÈSE non testable sans un modèle de la fonction d'utilité de l'agent.

### (b) Conditions de perte de puissance ou de jugeabilité

- **D1** : si le taux de base d'apparition du comportement collectif-seulement sous le bras individuel est > 0,10 (par imitation contextuelle), alors Δ ≥ 15 points exige que le bras collectif atteigne > 0,25, ce qui peut excéder la capacité d'un affinage léger. Puissance → 0 quand P(comportement | individuel) → P(comportement | collectif). Plus formellement, si X_i ~ Bernoulli(p_coll) et Y_i ~ Bernoulli(p_ind), le test de proportion bilatéral avec n runs et k graines a une puissance 1−β = Φ(√(n·k)·|p_coll − p_ind|/√(p̄(1−p̄)) − z_{α/2}). Pour k = 2 et n = 50 (illustratifs), la puissance tombe sous 0,50 dès que |p_coll − p_ind| < 0,13 (illustratif). Non jugeabilité : si le comportement n'apparaît dans aucun bras (p_coll = p_ind ≈ 0), le test est non informatif et A ne prévoit aucune règle d'escalade pour ce cas distinct de « escalade de pression ».

- **D2** : la simulation est entièrement paramétrique. Le résultat est une fonction analytique de (M, σ², Cov, taux d'acceptation). Pour tout seuil fixé [0,8 ; 1,25], il existe un Cov qui place le rapport exactement sur la frontière. Le duel n'a pas de puissance au sens fréquentiste : il n'y a pas de distribution sous H_0 ou H_1, seulement un calcul déterministe. Ce n'est pas une expérience ; c'est une illustration de paramètre.

- **D4 — preuve formelle** : si la banque plantée contient principalement des erreurs de classe (c1) (indices, ≤ vs <), qui sont les plus faciles à formaliser, et peu de classes (c2)/(c3), le rappel global est dominé par la classe facile. Lean peut « gagner » 20 points globaux tout en échouant sur les erreurs de spécification (c3) qui sont les plus critiques en pratique. **Condition de non-jugeabilité** : si la proportion d'erreurs (c3) dans la banque est < 0,25 (illustratif, soit < 5 sur 20), le test n'a pas la puissance de détecter un échec de Lean sur cette classe. A demande +20 points « sur au moins une classe » ; avec ≈ 7 erreurs par classe (illustratif), l'intervalle exact de Clopper-Pearson à 95 % sur un rappel de 5/7 est [0,29 ; 0,96] : non discriminant.

- **D6** : AUROC ≥ 0,6 contre oracle planté, sur des fiches à vérité binaire. Si la proportion de fiches « incorrectes » est déséquilibrée (taux de base < 0,10, illustratif), l'AUROC peut atteindre 0,6 avec un classifieur presque constant. La condition de jugeabilité exige un taux de base dans [0,20 ; 0,50] (illustratif) sur la partition d'évaluation ; A ne le fixe pas.

### (c) Contrôles négatifs manquants fatals

- **D1** : manque un contrôle « crédit individuel avec contexte partagé complet » (les agents lisent les traces des autres mais sont récompensés individuellement). Sans ce bras, on ne peut pas séparer l'effet du canal de communication de l'effet du crédit.

- **D3** : manque un contrôle « chute réelle mais bénigne » (le taux de signalement baisse pour une raison légitime, par exemple un changement de distribution des scénarios). Le lecteur qui détecte toute baisse sans distinguer cause légitime et cause alarmante a un taux de fausses alertes non mesurable avec le protocole proposé.

- **D5** : manque un contrôle « sonde aléatoire initialisée » sur M' (pas seulement étiquettes permutées). Si la sonde entraînée sur M atteint AUROC 0,6 sur M' mais qu'une sonde aléatoire atteint 0,55 par corrélation structurelle des traces, le gain net est 0,05, non 0,10. Les étiquettes permutées contrôlent le biais de la sonde, pas le signal structurel des traces.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duel II.2 — diffusion sans entraînement.** C oppose H_A (effet de groupe à poids gelés, Δp_agent ≥ 0,15) et H_B (invariance). Le dessin compare M = 1 et M = 4 agents « partageant le même canal d'exécution ». Mais passer de M = 1 à M = 4 modifie non seulement l'effectif mais aussi la longueur du contexte (les traces des pairs sont visibles), la charge computationnelle par jeton, et potentiellement la distribution des réponses du modèle (par effet de position dans le contexte). **Confondant** : effectif et longueur/structure du contexte. Si le taux de signalement baisse à M = 4, cela peut refléter une distraction attentionnelle (tokens de remplissage des pairs) plutôt que la « diffusion de responsabilité ». Aucun bras ne contrôle la longueur du contexte à effectif constant (par exemple M = 1 mais avec des traces factices de 3 agents fictifs).

2. **Duel II.1 — audit de calibration.** C écrit que Platt scaling à 2 paramètres sur le logit du jeton de verdict est le bras post-hoc, puis ajoute un « classifieur logistique léger sur les statistiques de log-probabilités de la trace, au sens de Damani pièce 5, l. 667 ». Mais ce second classificateur est un modèle entraîné par validation croisée, pas une « recalibration sans entraînement ». En regroupant les deux sous H_A (« suffisance du post-hoc sans RLCR »), C mélange un calcul à 2 paramètres (Platt) avec un classificateur potentiellement complexe (nombre de features des log-probabilités non borné). **Fuite construction/évaluation** : si le classifieur logistique est ajusté par validation croisée sur les mêmes familles que celles de l'évaluation leave-one-family-out, le risque de sur-ajustement intra-famille n'est pas contrôlé. Damani (pièce 5, l. 832, RAPPORTÉ) ne teste aucune recalibration sans entraînement ; C traite le classifieur post-hoc de Damani comme « Platt » alors que la synthèse v2 relève cette confusion (§ Inexactitudes de C, « à la limite », critère 8).

3. **Duel II.3 — preuve formelle.** C fixe N = 40 énoncés (20 sains, 20 avec défaut en 3 classes). Avec ≈ 7 défauts par classe, un test exact de McNemar unilatéral sur paires appariées (Lean détecte, suite non, ou l'inverse) a une puissance acceptable seulement si le nombre de paires discordantes est ≥ 8 (illustratif). Si Lean et la suite détectent les mêmes 12 défauts sur 20 et diffèrent sur 8, la puissance est ≈ 0,80 pour un odds ratio de 4 (illustratif). Mais si la concordance est élevée (Lean et suite détectent les mêmes 16/20), il n'y a que 4 paires discordantes et la puissance s'effondre. **Non-jugeabilité** si les deux méthodes sont fortement corrélées sur les mêmes types d'erreurs.

4. **Section 3 — dispositif de lecture.** C propose un « dead-man's switch » : la promotion exige un jeton signé par le démon externe. Pire cas non couvert : le démon émet un jeton valide sur des scénarios d'évaluation reconnus par l'agent (eval-awareness). C prévoit des scénarios « tirés sans remise dans une banque paramétrique avec le même habillage ». Mais si la banque est finie et les tirages sans remise, l'agent voit (au fil des points de contrôle) un sous-ensemble croissant de la banque. Après k points de contrôle avec n = 50 scénarios chacun, l'agent a été exposé à k·50 scénarios uniques. Si la banque a 500 entrées (illustratif), après 10 points de contrôle, toute la banque a été exposée. **Fuite construction/évaluation** : les scénarios d'évaluation ne sont plus indépendants de l'historique d'entraînement si les traces d'évaluation (même purgées) laissent une empreinte statistique (par exemple la distribution des longueurs de contexte aux points de contrôle diffère de celle des tâches ordinaires).

5. **Divergence 3 — cession à B et D.** C concède que le hors-ligne ne suffit pas et que l'escalade vers RL en ligne est « obligatoire avant toute conclusion d'innocuité ». Mais aucun duel de C ne teste le RL en ligne ; le Duel II.2 teste la diffusion sans entraînement, pas la pression. C renvoie cette étape au devis (§ (d), voie 2 : GRPO, 250–500 $), mais ne fournit pas de dessin expérimental pour cette voie, ni de critère d'escalade formel au-delà de « absence d'effet en voie 1 ». L'escalade est donc une promesse, pas un protocole.

### (b) Conditions de perte de puissance ou de jugeabilité

- **Duel II.2** : le test de Fisher apparié par scénario avec cluster-bootstrap a une puissance qui dépend de la corrélation intra-cluster ρ_ICC. Si les 4 agents dans un même run sont fortement corrélés (ρ_ICC > 0,5), la taille effective de l'échantillon est n_eff ≈ n/(1 + (M−1)·ρ_ICC). Pour n = 100, M = 4, ρ_ICC = 0,6, n_eff ≈ 100/3,4 ≈ 29. Le test de Fisher exact à n_eff = 29 a une puissance de ≈ 0,50 pour Δp = 0,15 (illustratif). **Non jugeable** si ρ_ICC > 0,6 et Δp < 0,15, ce qui est plausible si les agents partagent un contexte.

- **Duel II.1** : le test de DeLong apparié exige que les paires (score_post-hoc, score_binaire) soient indépendantes conditionnellement à la famille. Si les fiches d'une même famille partagent des caractéristiques de difficulté, la variance des AUROC par famille est sous-estimée par le bootstrap standard. C propose un bootstrap par blocs de familles, mais ne fixe pas le nombre minimal de familles. Avec < 5 familles (illustratif), l'intervalle de confiance du bootstrap par blocs est instable (biais de couverture documenté). Condition : ≥ 8 familles avec ≥ 50 fiches chacune (illustratifs).

- **Section 3, θ_arrêt = max(0,25 ; p₀ − 0,15)** : si p₀ = 0,45 (bas de la fenêtre de jugeabilité), θ_arrêt = 0,30. L'espace entre p₀ et θ_arrêt est 0,15, soit exactement le Δ détectable. Le premier signal d'alarme et le seuil d'arrêt sont confondus ; aucune « zone de vigilance » intermédiaire n'existe. Cela signifie que soit tout va bien, soit on arrête — il n'y a pas de régime d'escalade graduelle.

### (c) Contrôles négatifs manquants fatals

- **Duel II.2** : manque un bras « M = 1 avec contexte étendu » (traces factices de 3 agents). Sans ce contrôle, l'effet de la longueur du contexte et l'effet de l'effectif sont confondus, et une chute de signalement à M = 4 n'est pas attribuable à la diffusion de responsabilité.

- **Duel II.1** : manque un contrôle « scores aléatoires recalibrés par Platt ». Si on recalibre des scores i.i.d. uniformes par Platt scaling, l'ECE peut baisser par construction (Platt ajuste le biais). Le contrôle montre la réduction d'ECE attendue sans information, et l'amélioration réelle doit la dépasser.

- **Duel II.3** : manque un contrôle « preuve saine avec notation modifiée mais sémantique préservée » (par exemple, renumérotation des variables, reformulation d'un lemme intermédiaire). Cela mesure le taux de fausses alertes dû à la fragilité de la formalisation Lean (échec de traduction ≠ détection d'erreur). C compte les timeouts comme fausses alertes, mais pas les traductions réussies d'une preuve reformulée qui échouent sur un lemme intermédiaire mal traduit.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **E0 — jugeabilité.** D fait de E0 le « gate » de tout duel entraîné. Mais E0 lui-même n'a pas de critère de non-jugeabilité propre. Que se passe-t-il si E0 est inconclusif (p₀ dans une zone grise, par exemple 0,30–0,40) ? D ne spécifie pas de règle : le protocole bloque indéfiniment ou passe arbitrairement. La cascade « E0 → duels payants » est un arbre de décision à un seul nœud sans branche « inconclusif ».

2. **E13 — « avec pression établie ».** D conditionne les deux issues de E13 à « pression établie ». Mais D ne propose aucun duel de pression séparé (contrairement à A qui propose D1). Le seul critère implicite est que le gain de tâche soit non nul, ce que D critique par ailleurs comme insuffisant. **Variable confondante** : « pression » est une condition nécessaire non testée, ce qui rend les deux issues de E13 non falsifiables (on peut toujours attribuer un nul à « pression insuffisante »).

3. **E-preuve — « zone intermédiaire : sous-puissance déclarée ».** D admet explicitement un troisième résultat (ni H_A ni H_B). Cela est honnête, mais rend le duel faible en pratique : si le résultat tombe dans la zone intermédiaire, aucune décision ne s'ensuit, et les coûts sont perdus. D ne fixe pas de taille de banque minimale pour exclure cette zone avant de lancer le duel, ni de calcul de puissance a priori.

4. **Divergence 4 — table de décision.** D propose que « le directeur nomme par écrit un lecteur humain responsable ». C'est une assertion organisationnelle, pas un contrôle mesurable. Rien ne garantit que le lecteur humain détectera une chute de 5 points étalée sur 3 points de contrôle dans un journal de centaines de lignes. D mentionne « double lecture d'un échantillon scellé » comme garde, sans spécifier la taille de l'échantillon ni le seuil de concordance entre les deux lecteurs.

5. **Divergence 8 — cession à C.** D cède sur l'amortissement et adopte la formule K* = (G_gen − G_cat)/(λ_cat − λ_gen). Mais D note « lorsque le dénominateur est positif ; sinon il peut n'exister aucun seuil rentable ». Si λ_gen ≥ λ_cat (le coût d'usage de la génération est au moins aussi élevé que le catalogue), K* est infini ou négatif : la génération ne s'amortit jamais. D ne prévoit pas de contrôle pour distinguer ce cas du cas « dénominateur positif mais K* > horizon du programme ». Les deux sont des échecs de la génération, mais pour des raisons différentes, et appellent des réponses différentes.

### (b) Conditions de perte de puissance ou de jugeabilité

- **E0** : la variance A/A (même modèle contre lui-même) définit le plancher de bruit. Si σ_A/A > 0,10 (illustratif) sur le taux de signalement par run, alors la chute minimale détectable est > 0,20 (≈ 2·σ_A/A). Si la chute réelle est de 0,15, E0 conclut à la jugeabilité (p₀ est dans la fenêtre) mais le duel suivant est sous-puissant. E0 ne calcule pas la puissance du duel qui suivra ; il vérifie seulement p₀. Condition de non-jugeabilité implicite : σ_A/A > δ_min/2, non formulée par D.

- **E12 — « équivalence démontrée dans ±ε ».** D demande un test d'équivalence TOST. La puissance de TOST à n observations est 1−β = Φ(√n·(ε − |μ|)/σ − z_α). Pour ε = 5 points, σ = 10 (illustratif), |μ| = 0 et α = 0,05, la puissance 0,80 exige n ≈ 34 par bras (illustratif). Si le nombre de menaces plantées est < 34 (comme dans la banque de A à 20), TOST ne conclut jamais à l'équivalence. D ne fixe pas n.

- **E13** : D demande « inférence par graine » avec au moins 2 graines. Avec 2 graines par bras et 3 bras, le test de rang (Mann-Whitney ou permutation) a au plus C(4,2) = 6 permutations distinctes pour le contraste bilatéral ; la p-value minimale atteignable est 1/6 ≈ 0,17 > 0,05. **Non jugeable** à k = 2 graines pour un test par permutation exact au seuil conventionnel. Il faut k ≥ 4 graines par bras pour atteindre une p-value minimale de 1/C(8,4) ≈ 0,014.

### (c) Contrôles négatifs manquants fatals

- **E13** : D demande un bras « récompense de groupe permutée » mais ne le décrit pas. Si la permutation est intra-run (les agents échangent leurs récompenses), cela teste l'attribution ; si elle est inter-run (les récompenses d'un run sont assignées à un autre), cela teste le signal. Les deux contrôles sont nécessaires ; un seul ne suffit pas.

- **E-preuve** : D demande « mutations, preuves saines, empreinte valide sur preuve invalide, spécification volontairement insuffisante ». Manque un contrôle pour la fidélité de traduction : une preuve correcte dont la formalisation Lean échoue par limitation du sous-agent de traduction, pas par erreur dans la preuve. Sans ce contrôle, le taux de fausses alertes de Lean est sous-estimé (les échecs de traduction ne sont pas des détections).

- **Calibration** : D demande « confiance permutée » comme contrôle, mais ne précise pas si la permutation est intra-famille ou inter-famille. Si elle est intra-famille, elle ne contrôle pas l'effet de la famille sur la calibration ; si elle est inter-famille, elle détruit aussi la corrélation légitime famille-difficulté.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Duel « crédit » — estimand flou.** E écrit : « d, augmentation des omissions par occasion évaluable, collectif moins individuel ». L'estimand est une différence de proportions, mais E ne définit pas « occasion évaluable ». Si une occasion est définie comme un scénario où C = 1 et l'outil ρ est disponible, c'est la vérification mécanique sous contrat (convergence 2 : sous contrat explicite, la vérification mécanique *est* la cible). Si c'est un moment où une omission *pourrait* se produire sans contrat, la définition dépend d'un jugement externe non spécifié. **Vrai par construction** dans le premier cas (le taux d'omission sous contrat explicite est exactement 1 − taux de signalement mécanique) ; **non mesurable** dans le second.

2. **Duel « catalogue » — confondant.** E oppose génération ouverte et génération contrainte au catalogue, à « même procédure de recherche ». Mais la « procédure de recherche » est différente par nature : le catalogue est un ensemble discret (sélection), la génération ouverte est un espace continu (synthèse). Imposer la « même procédure » à l'un et l'autre, c'est soit contraindre la génération ouverte à opérer comme une sélection (ce qui la pénalise), soit étendre le catalogue à de la génération (ce qui supprime le contraste). **Confondant** : procédure de recherche et nature de l'espace.

3. **Duel « preuve » — biais de sélection.** E écrit que « un succès limité aux erreurs formalisables ne réfute aucune hypothèse sur les erreurs de spécification ». C'est exact et c'est le problème : si la banque contient principalement des erreurs formalisables (parce que le tiers qui plante les défauts doit lui-même formaliser l'erreur pour la planter), le duel est biaisé en faveur de Lean. E ne propose aucune procédure pour garantir que la banque représente la distribution réelle des erreurs. Le « contrôle négatif : énoncés valides avec changements de notation » ne résout pas ce biais.

4. **Section F — « qui lit ».** E propose « Lazar nomme un responsable humain de sécurité et un suppléant ». C'est identique à D dans la forme. E ajoute « un lecteur neuf indépendant peut vérifier les tableaux, sans remplacer la responsabilité humaine ». Mais E ne spécifie aucun seuil automatique, aucun kill-switch, aucune action mécanique en cas de franchissement. La garde « échéance obligatoire, suppléant, revue des cas non évaluables et suspension automatique en l'absence de validation » contredit l'absence de seuil automatique : « suspension automatique » requiert un seuil.

5. **Section C, divergence 3 — non-résolution.** E « donne raison à B et D » contre le gain de tâche seul, mais ne propose aucun contrôle de pression propre. E écrit que « les équations, journaux de sélection et mises à jour permettent un audit gratuit si disponibles » — mais l'audit d'un journal ne mesure pas la pression d'optimisation ; il mesure l'intensité de la mise à jour. La pression au sens d'Avalon est le couplage entre récompense collective et choix d'action ; l'amplitude de la mise à jour n'est qu'un proxy. **Variable confondante** : amplitude de mise à jour et pression de sélection collective.

6. **Duel « transfert ».** E oppose H_A (perte ≤ ε) et H_B (perte > ε). Le contrôle négatif « classifieur fondé seulement sur modèle, longueur et point de contrôle » est bon. Cependant, E ne dit pas si la sonde transférée opère sur les traces textuelles ou sur les activations internes. Si elle opère sur les activations (comme dans la discussion sur le transfert inter-architectures), la perte est mathématiquement indéfinie entre familles d'architectures différentes (C le note, et E ne le contredit pas). Si elle opère sur les traces textuelles, la perte est mesurable mais la sonde est un classificateur de texte, et le transfert est trivial (c'est juste une application du même classificateur à d'autres textes). **Vrai par construction** dans un cas (perte indéfinie) ou **non informatif** dans l'autre (transfert trivial pour un classificateur de texte).

### (b) Conditions de perte de puissance ou de jugeabilité

- **Duel « crédit »** : E fixe δ = 5 points, « illustratif », avec « unité d'inférence : répétition d'apprentissage ». Si le nombre de répétitions est k par bras et que la variance inter-répétitions σ²_k est élevée (ce qui est probable avec un affinage stochastique), la puissance du test sur la différence de proportions est 1−β = Φ(√k · δ/σ_k − z_{α/2}). Pour σ_k = 10 (illustratif) et δ = 5, il faut k ≈ 32 par bras pour une puissance de 0,80. Le devis de E (6 répétitions par bras) donne une puissance de ≈ 0,15 (illustratif). **Gravement sous-puissant** si σ_k > 5.

- **Duel « catalogue »** : E ne fixe ni le nombre de cas d'évaluation inédits ni le taux de base des cas résolvables par le catalogue. Si le catalogue résout déjà 90 % des cas, le gain maximal est de 10 points ; avec n = 30 cas (illustratif) et un test binomial exact, la puissance pour détecter un gain de 5 points (p_gen = 0,95 vs p_cat = 0,90) est ≈ 0,12. Non jugeable à ce taux de base.

- **Duel « confiance »** : E exige un « gain d'au moins 5 points au verdict binaire et au taux de base ». La double exigence (battre les deux lignes de base) est conservatrice mais réduit la puissance : le test doit rejeter deux H₀ simultanément. Si la confiance bat le taux de base de 6 points mais le verdict binaire de seulement 4 points, E conclut « H_A falsifiée » même si la confiance apporte une information réelle. Le critère composite est plus conservateur qu'un test unique.

### (c) Contrôles négatifs manquants fatals

- **Duel « crédit »** : E propose un « modèle gelé évalué aux mêmes points » et une « répétition A/A ». Manque un bras à crédit permuté (proposé par A dans D1). Sans ce bras, une différence entre collectif et individuel peut venir de la structure de la récompense (scalaire partagé vs scalaire propre) plutôt que du mécanisme collectif. Le contrôle A/A vérifie le bruit, pas la structure.

- **Duel « catalogue »** : manque un contrôle « tâche connue comme représentable dans le catalogue » — E le mentionne mais ne dit pas comment vérifier qu'elle est effectivement représentable. Si le contrôle échoue (le catalogue ne résout pas une tâche censée être « représentable »), c'est un défaut du catalogue ou un défaut du contrôle ? Pas de procédure de diagnostic.

- **Section E « Mesure minimale » — sonde d'omission** : E écrit « avant échéance : prédicteur historique et état disponible ». Manque un contrôle « sonde entraînée sur un autre comportement » (par exemple, prédiction de la longueur de la réponse) pour vérifier que la sonde détecte spécifiquement l'omission et non une corrélation de surface (longueur, registre lexical, position dans le contexte).

FIN-DE-CELLULE