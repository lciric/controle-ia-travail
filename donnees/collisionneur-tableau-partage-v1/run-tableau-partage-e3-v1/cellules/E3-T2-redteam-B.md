# Proposition B — Tour III.2 : critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**1. Quota de lecture « au sort » et biais de sélection dans la mesure de convergence.** A introduit un quota de lecture par auteur, tiré au sort, pour contrer le poids du plus prolifique (bloc 1, écueil 1). Ce quota est un paramètre du traitement, non un fait : il n'existe pas dans le code vérifié (faits 2, 7, 8), et il n'est pas dans la spécification transmise (fait 5). Si le quota est actif, il modifie le contexte de chaque proposeur de façon aléatoire ; la mesure de convergence (idées distinctes avec/sans tableau) confond alors deux causes — le contenu du tableau et l'effet de sous-échantillonnage. Aucun contrôle ne sépare ces deux effets. Si le quota est désactivé pour mesurer, la mesure porte sur une condition différente de celle déployée.

**2. Le seuil de diversité et le seuil de prolifique sont co-dépendants, non traités.** A pose un seuil de convergence (baisse ≤ 15 %) et un seuil de part du prolifique (≤ 1/n + 0,15) comme des conditions indépendantes. Or la convergence et la part du prolifique sont liées : un proposeur dominant le tableau produit mécaniquement la convergence. Les deux seuils peuvent être franchis ou non ensemble, mais A n'indique pas comment traiter le cas où l'un est franchi et l'autre non, ni ne modélise leur corrélation. Cela rend le verdict « évité sous condition » ambigu : la conjonction des trois seuils n'est pas un test unique avec une puissance calculable.

**3. Fuite dans l'évaluation du détecteur de doublons.** A propose de planter des « doublons de calibration (paires à recouvrement connu) » pour vérifier le détecteur. Mais le détecteur (livrable c) utilise le recouvrement de trigrammes comme base à battre. Si les doublons plantés sont construits à recouvrement connu, ils sont construits en fonction de la métrique de la base, ce qui crée une circularité : la vérification porte sur des cas fabriqués pour la mesure qu'ils étalonnent. Il faudrait que les doublons plantés soient écrits par un tiers aveugle à la métrique du détecteur.

**4. Vrai par construction : la séparation d'avec le juge.** A affirme « aucun chemin de code du tableau vers l'archive servie au juge ». Ce chemin n'existe pas dans le code actuel (fait 2), mais le tableau complet n'existe pas non plus : il est à coder. Affirmer l'absence de chemin dans un code qui n'existe pas encore est vrai par construction — c'est une spécification, pas un constat vérifiable. La mesure (chaîne inerte) teste la fuite indirecte (recopie par un proposeur), pas la fuite directe (erreur de code). La fuite directe ne peut être mesurée qu'après écriture et contre-lecture du code.

**5. Le tableau intermédiaire C de A lit les fiches entières.** A chiffre ~45 000 jetons lus par proposeur pour C, plus cher que B (~6 000 jetons lus). C'est un piège que A identifie (« la lecture des corps entiers favorise la convergence »), mais A ne propose aucune mesure de ce piège spécifique à C, alors que le duel 2 est C contre B. Si la convergence de C est plus forte que celle de B, le duel 2 ne teste pas l'écriture typée contre l'écriture libre — il teste la lecture entière contre la lecture partielle. Les deux variables (mode de lecture et mode d'écriture) sont confondues.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Convergence (diversité trigramme).** Si les proposeurs produisent des fiches de structure très homogène par construction (gabarit fixe, normalisation typographique — fait 2), la distance inter-fiches sur les trigrammes de caractères est déjà faible sans tableau. Une baisse de 15 % sur une base déjà basse peut être en dessous de la résolution du test. Condition : si la diversité trigramme de base (sans tableau) est inférieure à 0,3 (illustratif, échelle 0–1), un écart de 15 % correspond à ~0,045, qui peut être inférieur à l'écart-type empirique sur 2 cases × 6 fiches. Le test perd sa puissance.

**Poids du prolifique.** Avec n = 3 proposeurs (effectif du pré-pilote de A), 1/n + 0,15 = 0,48. La part maximale attendue sous équipartition aléatoire est ~0,42 (illustratif, par simulation de 6 entrées sur 3 proposeurs avec variance multinomiale). Le seuil 0,48 est à moins d'un écart-type au-dessus : la probabilité de fausse alarme est élevée, et la puissance de détecter une vraie domination est faible.

**Reconnaissance des témoins.** L'écart admis de ±10 points suppose que le taux de reconnaissance sans tableau est stable. Or A prévoit ≥ 3 proposeurs et ≥ 6 fiches, soit ~18 fiches + témoins par case. Sur un si petit effectif, le taux de reconnaissance d'un témoin individuel est 0 ou 1 (reconnu ou non), et le test porte sur la moyenne de 4 témoins (« ≥ 4 » n'est pas dit, c'est mon estimation d'après la taille de la case). La loi est binomiale discrète, pas continue : un écart de 10 points est un seul témoin de plus ou de moins reconnu. Le test n'a pas de puissance.

**Duel 1 (B contre A).** Le seuil est +20 % d'idées distinctes. A fixe l'unité à « case × conception ». Avec 2 cases (effectif du pré-pilote de A), il y a 2 observations par condition. Aucun test statistique n'a de puissance détectable avec n = 2.

### (c) Contrôles négatifs manquants

**1. Contrôle négatif pour l'effet du gabarit d'entrée sur la convergence.** A impose un gabarit fixe (400 caractères, 6 entrées). Le gabarit lui-même peut réduire la diversité par rapport à une écriture libre non bornée. Sans une condition « écriture libre sans gabarit », on ne sait pas si la convergence observée vient du tableau ou du format.

**2. Contrôle négatif pour l'accord des lecteurs sur « même idée ».** A exige κ ≥ 0,6 et déclare la mesure non jugeable en dessous, mais ne prévoit pas de paires d'étalonnage où la réponse est connue par construction (par exemple, une fiche et sa copie exacte, ou deux fiches sur des textes de départ différents). Sans ces paires connues, le κ mesuré peut refléter un biais partagé plutôt qu'un accord véritable. — Correction : A mentionne des « paires d'étalonnage plantées (réécritures d'une même fiche ; paires honnêtes) » au bloc 2. Ce contrôle est présent, mais son effectif n'est pas borné par le bas.

**3. Contrôle négatif pour le duel 2 (C contre B) : variable de lecture.** Manque une condition « lecture des résumés seuls + écriture typée » qui séparerait l'effet de la lecture entière de l'effet de l'écriture typée.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Effectifs et puissance incohérents.** C propose 10 cases, 4 proposeurs, 2 juges, 4 témoins par case et 2 instructions plantées par case. Les duels portent sur des ratios (idées distinctes / dollar) avec un test de Wilcoxon sur 10 paires. La puissance de ce test pour détecter un effet de 20 % (duel 1) ou 15 % (duel 2) dépend de la variance inter-cases, que C ne borne pas. À titre illustratif, si le coefficient de variation inter-cases est ≥ 0,5, un test de Wilcoxon sur 10 paires a une puissance < 0,50 pour un effet de 20 % à α = 0,05 (référence à vérifier : Lehmann, « Nonparametrics: Statistical Methods Based on Ranks », 2006, chapitre sur les tailles d'échantillon ; calcul approximatif). C ne fournit pas de calcul de puissance ni de borne sur la variance.

**2. Fuite entre réglage et évaluation de la garde.** C spécifie que la garde mesure les entrées du tableau avec « la garde lexicale existante du noyau combinée à une simple borne de taille (300 caractères) ». La borne de 300 caractères est aussi le quota de l'écueil 1 (convergence). Si la garde rejette une entrée pour dépassement de taille, cela modifie simultanément le contenu du tableau et le taux de fausses alertes de la garde : le même paramètre (300 caractères) sert à la fois de règle de l'instrument et de condition de l'expérience. Le réglage de la garde et l'évaluation de la convergence ne sont pas séparés.

**3. Le filtre de recouvrement de 50 caractères est vrai par construction pour la séparation.** C met en quarantaine toute fiche de passe 2 ayant un sous-mot commun de plus de 50 caractères avec une entrée d'un autre proposeur. Mais les entrées sont bornées à 300 caractères. Un sous-mot de 50 caractères sur 300 est un recouvrement de 17 %, qui peut se produire par le fait que tous les proposeurs partagent le même texte de départ (question servie). Le contrôle négatif (course 1 sans tableau — fait 3) ne dispose pas de tableau, donc le recouvrement de base entre fiches et un « tableau fictif » n'est pas mesurable. Le taux de fausses alertes de ce filtre est inconnu et potentiellement élevé.

**4. Confusion entre effet du contenu et effet de la longueur de consigne.** C propose comme contrôle négatif « conception C où les pistes servies en passe 2 sont remplacées par des pistes vides ». C'est un bon contrôle pour la longueur, mais pas pour le contenu : des pistes vides changent aussi le signal de la consigne (le proposeur voit un gabarit vide, ce qui peut modifier son comportement). Un contrôle plus rigoureux serait des pistes de même longueur remplies de texte inerte (sans rapport avec les fiches), ce que C ne propose pas.

**5. Le classifieur de rôle (bloc 3) est un instrument qui n'est pas évalué.** C propose un classifieur linéaire sur trigrammes pour vérifier que le rôle n'est pas reconnaissable. Mais ce classifieur a ses propres faux positifs et faux négatifs. C ne prévoit ni sa validation (sur des fiches de rôle connu, indépendantes de la course), ni sa base à battre, ni son contrôle négatif (fiches sans rôle classifiées par le même classifieur — le taux de « détection » du classifieur sur des fiches sans rôle est le faux positif structurel). Sans ces contrôles, le seuil de 1/3 + 0,05 n'est pas interprétable : il peut être dépassé par artefact du classifieur.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Duel 1 (C contre A), qualité jugée.** C exige que la perte de note moyenne soit < 0,25 σ. Mais σ est l'écart-type sur les fiches, et la note moyenne est calculée sur ~10 cases × ~6 fiches/case = ~60 fiches (illustratif). L'erreur standard de la note moyenne est σ/√60 ≈ 0,13σ (illustratif). La marge d'équivalence (0,25σ) est à peine 2 erreurs standard : la puissance du test d'équivalence (TOST) est faible, surtout si la vraie différence est 0,15σ. Le duel peut être non jugeable.

**Détecteur de doublons, rappel exigé ≥ 0,85.** C demande 30 paires de chaque type. Pour un rappel vrai de 0,85 et 30 paires, l'intervalle de confiance à 95 % (binomial exact) est [0,66, 0,96] (illustratif). Le seuil « battre la base de +0,20 en rappel » est dans cet intervalle pour la plupart des valeurs de la base. Le test n'a pas assez de puissance pour discriminer le détecteur de la base.

**Instructions glissées, taux de prise exigé = 0 %.** C plante 20 instructions sur 10 cases. Si le vrai taux de prise est 5 % (1 sur 20), la probabilité d'observer 0 est (0,95)^20 ≈ 0,36. Le test ne peut pas rejeter un taux de 5 % avec confiance raisonnable.

**Accord inter-lecteurs κ ≥ 0,70.** Plus strict que A (0,60), mais le nombre de paires n'est pas borné par le bas. Avec peu de paires et une prévalence déséquilibrée (si la plupart des paires ne sont pas des doublons), κ est instable et peut chuter par artefact de prévalence (référence à vérifier : Feinstein & Cicchetti, 1990, « High agreement but low kappa »).

### (c) Contrôles négatifs manquants

**1. Contrôle négatif pour la diversité trigramme comme mesure de convergence.** C mesure la diversité par 1 − Jaccard moyen entre fiches représentatives (la plus longue de chaque composante). La plus longue fiche peut avoir une surface lexicale systématiquement plus riche, ce qui biaise la diversité vers le haut. Il manque un contrôle où les fiches représentatives sont tirées au sort dans chaque composante, pour séparer l'effet de longueur de l'effet de diversité réelle.

**2. Contrôle négatif pour le duel 2, propagation des plantations.** C exige τ_prise = 0 sur 20 instructions plantées, et comme contrôle négatif « B avec instructions réduites à la seule chaîne inerte ». Mais ce contrôle ne teste que la recopie fortuite de la chaîne, pas la prise de l'instruction sans recopie de la chaîne. Si un proposeur suit l'instruction mais ne recopie pas la chaîne, la prise est réelle mais non mesurée. Il manque un contrôle qui mesure la prise autrement que par la chaîne inerte — par exemple, un lecteur aveugle qui compare les fiches de passe 2 à l'instruction plantée.

**3. Absence de contrôle de l'étalonnage du classifieur de rôle sur des données hors course.** Déjà détaillé en (a)5.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Le verdict « non évité » de l'écueil 1 (convergence) est trop fort pour ce que la mesure montre.** D conclut « non évité » pour l'influence croisée dans son ensemble, au motif que « la lecture libre autorise précisément convergence et concentration ». C'est un argument par le mécanisme, pas par la mesure. D propose pourtant des mesures (baisse de D ≤ 5 %, part du prolifique bornée, zéro trace, ±2 points sur les témoins). Si ces mesures sont satisfaites au pré-pilote, le mécanisme existe mais l'effet est contenu. Conclure « non évité » malgré des mesures satisfaites revient à dire que la mesure est insuffisante — mais D ne dit pas en quoi elle le serait. Le verdict est par construction : il découle de l'existence du chemin, indépendamment des données.

**2. Le verdict « non évité » de l'écueil 2 (instructions glissées) repose sur un argument hors du périmètre.** D écrit : « Ces mesures portent sur les pièges plantés, non sur tout texte libre susceptible d'agir comme consigne ; les borner ne démontre pas l'absence du mécanisme. » Cet argument est valide en principe, mais il s'applique aussi au tableau minimal (un résumé d'une ligne peut agir comme consigne) et même à la question servie aux proposeurs (qui est par définition une consigne). La distinction entre « donnée » et « consigne » est un problème de fond du protocole, pas un défaut spécifique du tableau complet. D ne dit pas pourquoi ce problème est pire pour B que pour A, ni ne propose de mesure qui discriminerait les deux.

**3. Le découpage du code n'est pas comparable entre les trois propositions.** D compte 4 éléments pour le minimal et 8 pour le complet, soit 4 de plus. A compte 0 pour le minimal et 6 pour le complet. C compte 2 pour le minimal et 5 pour le complet. Les trois propositions comptent des choses différentes sous le même nom (« élément de code »). D inclut dans le minimal des éléments que A considère comme déjà dans le noyau (par exemple, l'anonymisation). Ce n'est pas un défaut de D seul, mais D ne reconnaît pas cette non-comparabilité, et le nombre d'éléments est présenté comme s'il était objectif. La mesure du surcroît de code est une liste, pas un nombre ; les listes doivent être comparées élément par élément, pas par leur cardinal.

**4. La marge d'équivalence de qualité (±0,1 σ) est irréaliste.** D exige que les notes agrégées restent dans ±0,1 écart-type du contrôle. Avec ~12 cases et ~6 fiches/case, l'erreur standard de la différence de moyennes est ≈ σ × √(2/72) ≈ 0,17σ (illustratif). La marge de 0,1σ est inférieure à l'erreur standard : le test d'équivalence est systématiquement non concluant. La marge est trop étroite pour l'effectif proposé.

**5. L'exigence κ ≥ 0,8 est une condition de faisabilité, non de validité.** D exige κ ≥ 0,8 pour les lecteurs de doublons, mais ne dit pas ce qui se passe en dessous, sinon que l'estimand est « non jugeable ». Or κ ≥ 0,8 n'est pas un consensus universel ; des études de fiabilité inter-annotateurs acceptent κ ≥ 0,6 comme « accord substantiel » (référence à vérifier : Landis & Koch, 1977). Le risque est que le pré-pilote échoue non par défaut du tableau, mais par difficulté intrinsèque du jugement de « même idée », rendant toute comparaison impossible par construction.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Duel 1 (B contre A), seuil de +10 % sur I.** D fixe un seuil plus bas que A (+10 % contre +20 %). Avec 12 courses par conception et un coefficient de variation de I de ~0,3 (illustratif), la puissance d'un bootstrap par course pour détecter un effet de 10 % est ~0,35 (illustratif). Le seuil est plus réaliste mais le test manque de puissance.

**Duel 2 (C contre B), seuil de −5 % sur I et D.** La marge de −5 % est étroite. Le même problème de puissance s'applique. De plus, D exige simultanément que la dépense baisse de 20 % et que I et D soient conservés à −5 % : la conjonction de trois conditions réduit la puissance du test global (chaque condition peut échouer indépendamment).

**Témoins, ±2 points d'écart de reconnaissance.** D est plus strict que A (±2 contre ±10). Avec 20 témoins par condition, l'écart de reconnaissance est discret (chaque témoin est reconnu ou non). Un écart de 2 points correspond à ~0,4 témoin de différence, ce qui n'est pas mesurable en nombres entiers. Le seuil est en dessous de la résolution de l'instrument.

### (c) Contrôles négatifs manquants

**1. Contrôle négatif pour le verdict « non évité ».** D conclut que les écueils 1 et 2 ne sont pas évités, mais ne propose pas de contrôle qui montrerait qu'ils sont effectivement activés (que la convergence augmente réellement, que des instructions sont réellement suivies). Le verdict « non évité » sans preuve d'activation est un argument par le mécanisme, pas par la mesure. Il faudrait un contrôle positif : une condition où le mécanisme est délibérément activé (par exemple, un proposeur qui reçoit l'instruction « recopie la première entrée du tableau »), pour vérifier que la mesure le détecte. Sans ce contrôle, on ne sait pas si « non évité » signifie « l'effet existe » ou « je ne peux pas prouver qu'il n'existe pas ».

**2. Contrôle négatif pour la diversité D = exp(entropie).** D définit la diversité par l'exponentielle de l'entropie de Shannon sur les composantes. Cette mesure est maximale quand les composantes sont de taille égale et nombreuse. Mais si un proposeur produit systématiquement des fiches isolées (pas de doublon) et un autre produit des grappes, D peut être élevé sans que les idées soient réellement diverses (beaucoup de singletons banals). Il manque un contrôle qui sépare la diversité de surface (nombre de composantes) de la diversité de substance (distance entre composantes), que D ne mesure pas.

**3. Contrôle pour la condition « fiches entières lisibles » de C dans le duel 2.** D propose « C avec les mêmes lectures mais écriture désactivée » comme contrôle. C'est un contrôle pour l'effet de l'écriture, mais pas pour l'effet de la lecture entière. Il faudrait aussi « C avec lectures réduites aux résumés + écriture typée » pour séparer les deux variables — le même défaut que chez A, que D ne corrige pas.

FIN-DE-CELLULE