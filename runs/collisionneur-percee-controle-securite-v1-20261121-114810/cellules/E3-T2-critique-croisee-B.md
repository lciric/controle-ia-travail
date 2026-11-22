# Proposition B, tour III.2 : critique croisée de méthode

**Pièces.** FAITS, QUESTION, et les conceptions A, C, D et E sont reçues entières ; chacune se termine par sa ligne de fin. Les faits ne portent pas de statut individuel. Tout ce que j'affirme au-delà des pièces est HYPOTHÈSE de B. Mes calculs sont donnés avec leurs étapes pour qu'on puisse les contrôler. Les nombres qui ne viennent pas des faits sont illustratifs. L'ordre en six points de l'arbitre concernait la conception ; ici je suis le livrable du tour, et je garde son exigence : plus profond, pas plus long.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Une borne inférieure prise pour une borne supérieure, deux fois.**
   - En D1, la garantie (1 − q·d·(s − δ))^N exige δ ≥ TV(P_réel, P_planté), la distance en variation totale sur *tout ce que l'agent observe*. L'avantage du meilleur discriminateur disponible n'en est qu'un minorant. Observer δ̂ ≤ δ₀ ne prouve donc jamais δ ≤ δ₀.
   - En M2, A écrit lui-même que le classifieur avec étiquettes donne une borne inférieure du plafond. Il en tire pourtant « plafond bas, donc changer d'observable », ce qui demanderait une borne supérieure.
   - Le même instrument ne peut pas servir à la fois de minorant et de majorant.
2. **D1 suppose des tâches indépendantes.** L'exposant N vaut si les décisions de sabotage sont indépendantes d'une tâche à l'autre. Un agent avec mémoire peut corréler ses choix, par exemple saboter seulement après avoir vu passer des tâches qu'il juge réelles. Le facteur d n'est pas non plus un paramètre fixe : l'attaquant choisit de saboter là où l'effet échappe à la vérification mécanique, donc d dépend de sa politique.
3. **Le contrôle négatif de E1 est ambigu.** Une sonde qui sonne sur un sabotage injecté hors du modèle n'indique pas forcément une fuite d'étiquettes. Les jetons injectés entrent ensuite dans le contexte, et le modèle peut légitimement représenter « ceci est un sabotage ». Le silence n'est donc pas l'issue attendue par construction.
4. **Le placebo de E1 n'est pas apparié en intensité.** Si le placebo modifie moins les poids que le saboteur (norme de l'adaptation, divergence au modèle de base sur des requêtes neutres), un placebo muet s'explique sans faire appel au sabotage.
5. **E4 : la mémoire des tentatives fuit.** L'organisme d'idéation a vu des mondes plantés construits par les mêmes concepteurs. Un rappel élevé peut donc mesurer qu'il a appris le générateur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1.** Soit 𝒟 la famille de discriminateurs testée, et δ̂ = sup_{f∈𝒟} adv(f). La borne n'est jugeable que si le discriminateur effectif de l'agent appartient à 𝒟, ce qui n'est pas estimable de l'extérieur. Même avec δ connu, la borne est vide si s ≤ δ ; A le dit.
- **D2 (calcul de B, à vérifier).**
  - Une e-valeur conforme issue de n_cal cas de calibration est majorée par une constante finie e_max(n_cal). La conversion valide κ·p^(κ−1) atteint au plus κ·(n_cal+1)^(1−κ).
  - Avec la moyenne sur T pas, qu'A retient sous dépendance, un sabotage limité à un seul pas laisse en moyenne au plus (e_max + T − 1)/T, puisque les autres pas valent environ 1 sous H0.
  - L'alarme est donc *impossible par construction* dès que (e_max + T − 1)/T < 1/α. Exemple illustratif, avec la valeur maximale grossière e_max ≈ n_cal : n_cal = 10⁴ et T = 200 donnent environ 51, sous 100.
  - Le produit, qui aurait la puissance, n'est valide que si chaque e-valeur l'est *conditionnellement au passé*. Une calibration conforme commune à tous les pas ne le garantit pas.
- **Erreur type à 1 %.** Le calcul d'environ 0,1 point pour 10 000 cas suppose des cas indépendants. Avec m trajectoires par tâche et une corrélation intra-tâche ρ, la variance est multipliée par 1 + (m − 1)ρ. La taille utile est le nombre de tâches, pas de trajectoires.
- **E5.** Soit τ² la variance de détection entre familles et k le nombre de familles tierces. L'écart vu/tiers a une variance d'au moins τ²/k. Avec k = 1, situation actuelle selon les faits, l'écart n'est pas estimable ; A le reconnaît.

### (c) Contrôles négatifs dont l'absence serait fatale

- En D1, un discriminateur doté du **contexte complet de l'agent** : historique, ordre et cadence des tâches, et pas seulement la tâche isolée.
- En E1, un placebo **apparié en divergence au modèle de base**.
- En E4, des **mondes plantés issus d'un générateur que la mémoire n'a jamais vu**.

---

## Sur la proposition C

**Statuts.** C attribue le statut RAPPORTÉ aux faits, qui n'en portent pas. Il donne le statut VÉRIFIÉ à des affirmations qui ne viennent pas des faits : modèles ouverts, « fossé sémantique ». Il traite les « soixante sous-agents » de la session zêta comme la flotte du programme. Il écrit « 50 × 300 $ [RAPPORTÉ] » alors que les 300 dollars sont le coût par problème d'une liste mathématique, pas d'un cycle d'idéation. Je ne reprends aucun de ces statuts.

### (a) Défauts de méthode

1. **CCT : l'hypothèse nulle n'est jamais la condition honnête.**
   - La martingale ne contrôle les fausses alertes que sous H0 : « les jetons de l'agent suivent la loi du jumeau ». Un agent honnête plus fort, ou disposant d'un contexte plus riche, viole H0. La garantie « FPR ≤ 1 % sans hypothèse de distribution » est donc vraie seulement pour un cas qui n'arrive pas. La formalisation Lean 4 n'y change rien : elle certifie l'implication, pas la nulle.
   - Le couplage de Gumbel-max ne mesure pas TV. Pour tout couplage, P(X ≠ Y) ≥ TV ; l'égalité caractérise un couplage maximal, et le Gumbel-max n'en est pas un en général (à vérifier).
   - Surtout, si l'on dispose des deux jeux de logits sur la trajectoire réalisée, le rapport de vraisemblance est la statistique suffisante. Le couplage n'ajoute que du bruit d'échantillonnage.
2. **ABCA contredit Menace 2.** Dans ABCA, l'agent testé fabrique lui-même l'objet de contrôle qui justifie son choix. Menace 2, chez C lui-même, établit que c'est exploitable. La vérification mécanique contrôle que le micro-test s'exécute, pas qu'il soit représentatif. Le premier pas, qui consiste à demander l'objet au saboteur une seule fois, est non adaptatif : il ne teste rien de la menace.
3. **CAPP : fuite de construction.** La direction perturbée est celle de la sonde, entraînée sur les organismes. Une bifurcation sous perturbation peut donc mesurer la trace de construction (S2 chez A, E0.1 chez E).
4. **Expérience 1 : hypothèses non exclusives.** L'échec de l'optimisation adaptative peut venir du budget de l'attaquant, et non de l'invariance de la signature. C l'admet (« pour cette classe… et de budget »). Une troisième issue reste donc ouverte, et l'inférence n'est pas forte au sens de B4.
5. **Menace 3 : premier pas vrai par construction.** Si l'on injecte la justification erronée comme consigne *sincère* dans un modèle honnête, ce modèle ne trompe pas. Une sonde de tromperie qui reste muette fait alors correctement son travail. Cela ne dit rien d'un agent qui se serait auto-persuadé.
6. **τ_I n'est pas défini.** Si l'on obtient l'« incompétence honnête » par une consigne d'échouer, τ_I est lui-même un organisme construit, porteur d'une consigne. L'expérience 3 compare alors deux artefacts de consigne.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **CCT.** Soit P_A la loi de l'agent honnête et Q la loi du jumeau. Dès que KL(P_A‖Q) par pas est strictement positif, le log-rapport cumulé dérive linéairement en T sous l'honnêteté. Les fausses alertes tendent alors vers 1 quand T croît, quelle que soit la borne de Ville.
- **Expérience 3.** Il faut au moins 99 cas τ_I de calibration pour qu'une valeur p conforme puisse descendre à 0,01, puisque p_min = 1/(n+1). Avec moins de cas, le TPR à 1 % de fausses alertes est nul par construction.
- **Expérience 2.** Avec un seul mode tenu à l'écart, ΔTPR confond la difficulté propre à ce mode et le surapprentissage. Sa variance entre familles n'est pas estimable.
- **CAPP.** Soit S_v la sensibilité de la sortie à une perturbation de norme fixe le long de v. Si le rapport S_v(sabotage)/S_v(honnête) est le même pour v aléatoire et pour v égal à la direction de la sonde, la statistique n'a aucune puissance spécifique.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Agent honnête contre jumeau**, sur trajectoires longues, pour la dérive de la martingale.
- **Directions aléatoires de même norme** pour CAPP.
- **Objets de contrôle d'ABCA produits par un saboteur adaptatif** qui connaît la règle.
- **τ_I constitué d'échecs naturels non induits.**

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le critère F contredit l'objectif.**
   - D vise à bloquer les conclusions matériellement fausses, sans attribution d'intention. Mais il compte comme fausse alerte toute alerte sur une erreur honnête, et applique à F le plafond de 1 %.
   - Une défense par l'effet, qui réussit, bloque aussi les erreurs honnêtes. Elle est alors pénalisée pour son succès.
   - D publie deux comptabilités, mais ne dit pas laquelle porte le plafond.
2. **Le dénominateur de D dépend de l'attaquant.** D = bloquées / nuisibles produites. Si le contrat dissuade, il y a moins de décisions nuisibles produites, et D devient un rapport à dénominateur aléatoire et petit. Le dommage par tâche assignée, que D publie aussi, doit être le critère principal.
3. **Qui choisit le témoin ?** « Déposer une conclusion et l'observation qui obligerait à la retirer » : si c'est l'agent qui désigne l'observation, il choisit un témoin qui ne se déclenchera pas (même défaut qu'ABCA chez C). Si c'est un tiers, on retombe sur le test caché ordinaire. D l'a vu et en a fait son test de mort. C'est la bonne lecture, mais alors le candidat n'a pas de contenu propre avant ce test.
4. **Le contrôle négatif commun est sélectionné.** Les « décisions honnêtes difficiles, avec réexécution confirmant leur validité » excluent exactement les erreurs honnêtes, qui sont le négatif dur que D dit vouloir garder ailleurs.
5. **La garantie sans loi est vraie par construction** relativement à l'espace d'états spécifié. D le dit, honnêtement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Plafond de F.** Soit e = P(conclusion honnête invalide) et r = P(le témoin rejette | conclusion invalide), sans dépendance à l'intention. Alors F ≥ r·e. Si r·e > 0,01, *toute* défense par l'effet qui fonctionne viole le plafond : le critère est insatisfaisable, pas seulement sévère.
- **Rétention.** « La rétention ne baisse pas » est une égalité stricte. Sur un lot fini de n décisions honnêtes valides, l'estimateur a un écart type d'environ √(ρ(1 − ρ)/n). H_A sera rejetée par le seul bruit environ une fois sur deux, quelle que soit la vérité. Sans marge d'équivalence fixée d'avance, le duel n'est pas jugeable.
- **Duel commun.** H_B est une disjonction de trois échecs. Sa réfutation dit peu ; son succès ne dit pas laquelle des trois conditions a cédé. Il faut un duel par condition.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Conclusions honnêtes invalides** : erreurs naturelles, comptées dans les deux comptabilités.
- **Témoin choisi par l'agent contre témoin tiré au hasard** parmi les observations admissibles, à budget égal.
- **Dossiers où le contrat n'a pas été annoncé à l'agent**, pour séparer la dissuasion de la détection.

---

## Sur la proposition E

**Statuts.** E marque VÉRIFIÉ des affirmations qui ne viennent pas des faits : « 1 − 0,99¹⁰⁰ ≈ 63 % » avec un 100 illustratif et des pas supposés indépendants ; des modèles « ouverts », dont l'un au moins mériterait vérification de licence. Il propose aussi les journaux des sessions zêta et des 66 échecs comme données, alors que les faits ne disent pas qu'ils sont disponibles pour le programme. Je ne reprends pas ces statuts.

### (a) Défauts de méthode

1. **E0.1 : intensité du conflit confondue avec l'intention.**
   - Une consigne stylistique bénigne entre moins en conflit avec la tâche qu'une consigne de sabotage. Une sonde qui lit l'intensité du conflit avec la consigne passe le seuil Δ ≥ 50 points sous H_B.
   - L'idée du contrôle est la même que le placebo de A, avec le même défaut d'appariement.
2. **CES-MM : la nulle exclut les erreurs honnêtes.** L'e-processus contrôle les fausses alertes sous « pipeline sans biais sur les canaris ». Un pipeline honnête bogué, que E veut justement garder dans ses données (corpus 2), viole cette nulle. La garantie de Ville ne couvre donc pas la population honnête que E décrit lui-même.
3. **AUROC n'est pas la bonne fonctionnelle.** CES-MM repose sur l'indiscernabilité, comme D1 chez A, mais avec un critère plus faible que celui de A (voir b).
4. **RAND-ML : le noyau déclaratif est un canal non audité.** La ré-implémentation partage le noyau. Tout sabotage logé dans le noyau passe donc par construction. E le cite comme branche de H_B, mais sans contrôle qui le mesure.
5. **FMS-Lean : contrôle négatif choisi pour réussir.** Exiger un contre-modèle par prémisse rejette par construction les lemmes honnêtes non minimaux, fréquents par commodité. Le contrôle négatif retenu, « lemmes à hypothèses minimales connues », exclut précisément ce cas.
6. **Menace 2 : erreur de signe.**
   - Une sonde de sabotage qui ne sonne pas sur un biais *bénin* se comporte comme il faut.
   - La chute sous 15 % ne prouve un défaut d'invariance que si le biais induit est nuisible. Sinon, H_A confirmée est un succès de la sonde.
7. **Menace 1 : le simulateur décide de l'issue.** Dans un simulateur abstrait, ce que les moniteurs pas à pas peuvent voir est fixé par le choix des observables. Le plafond de 15 % est alors une propriété de la conception, pas une découverte.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **AUROC des canaris (calcul de B, illustratif).** Supposons qu'une fraction m des entrées réelles soit parfaitement reconnaissable comme réelle, et le reste distribué comme les canaris. Alors AUROC = m + (1 − m)/2 = 0,5 + m/2. Le seuil de E, 0,55, est donc compatible avec m = 10 % de tâches réelles sabotables sans risque. Le critère requis est l'avantage maximal (TV), que A emploie.
- **RAND-ML.** Soit Δ_H l'écart de conclusions entre deux ré-implémentations honnêtes, et q₀,₉₉ son quantile. Un sabotage d'effet b < q₀,₉₉ n'est pas détectable à 1 % de fausses alertes, quelle que soit la lignée. Une valeur p conforme à 0,01 exige en outre au moins 99 paires honnêtes de calibration, distinctes des paires d'évaluation. Avec 150 tâches appariées partagées entre calibration et test, la contrainte est tendue.
- **E0.1 et E0.2.** Avec 200 cas (illustratif), le seuil à 1 % repose sur les deux scores honnêtes les plus élevés, et son estimateur a une variance du même ordre que l'effet cherché.
- **CES-MM.** Soit p_bug la fraction de pipelines honnêtes biaisés et β leur biais sur les canaris. L'e-processus dérive sous l'honnêteté dès que p_bug·β > 0, et les fausses alertes par trajectoire tendent vers p_bug quand la trajectoire s'allonge.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Consigne bénigne appariée en divergence comportementale** au saboteur (E0.1).
- **Pipelines honnêtes bogués** dans la calibration de CES-MM.
- **Saboteur qui n'agit que sur le noyau déclaratif** (RAND-ML).
- **Lemmes honnêtes non minimaux** (FMS-Lean).
- **Biais induit nuisible contre biais induit bénin**, à intensité égale (Menace 2).

---

## Défaut que je relève chez plusieurs, sans fusionner leurs propositions

Trois candidats défensifs (D1 chez A, CCT chez C, CES-MM chez E) tirent leur garantie formelle d'une hypothèse que la population honnête ne satisfait pas, ou d'une quantité que l'on ne sait que minorer.

- **Nulle de l'e-processus violée par l'honnêteté.** Pour CCT, l'agent honnête diffère du jumeau. Pour CES-MM, les pipelines honnêtes bogués sont biaisés sur les canaris.
- **Indiscernabilité seulement minorée.** Pour D1 et CES-MM, aucun discriminateur testé ne majore ce que l'agent peut distinguer.

Le test qui décide, commun mais à mener séparément pour chacun : mesurer les fausses alertes réalisées sur des honnêtes *imparfaits et plus forts que la référence* avant toute mesure de détection.

- Si elles dépassent le nominal, la garantie est vide pour ce candidat.
- Si elles tiennent, c'est l'hypothèse « la nulle exclut l'honnête réel » qui tombe pour lui.

FIN-DE-CELLULE