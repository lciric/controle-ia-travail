**État des pièces.** Les cinq conceptions A, C, D, E et F sont présentes, non vides et chacune close par sa ligne de fin ; je n'ai pas recalculé les empreintes. Toutes mes critiques sont des HYPOTHÈSES de méthode. Tout chiffre que j'avance est illustratif, y compris quand je le calcule à partir des seuils illustratifs d'une autre proposition. Je ne modifie aucun statut attribué par les autres propositions : quand un statut me paraît mal étayé, je le signale sans le réécrire.

---

## Sur la proposition A

**(a) Défauts de méthode**
- **E1 confond deux propriétés.** Une sonde linéaire entraînée sur les étiquettes « planté / réel » mesure ce que les activations encodent, pas ce que la politique exploite. De plus, H_B (« AUROC ≥ 0,60 pour l'un des deux ») est une disjonction de deux tests sans correction de multiplicité, ce qui la favorise.
- **Fuite dans E1.** Si la sonde est entraînée et testée sur des unités issues du même générateur de plantage, elle apprend la signature de ce générateur. Il faut séparer les générateurs : entraînement sur G1, test sur G2.
- **Banc commun.** Les familles de fautes (conclusion biaisée, étape omise, chiffre altéré) et l'auditeur sont conçus par la même équipe. La sensibilité de l'auditeur à ces familles est donc en partie fixée par construction. Une famille de fautes doit être tenue à l'écart du réglage de l'auditeur.
- **E3 n'est pas exclusif à l'interprétation.** H_B regroupe deux mécanismes : la convergence sur un point focal et la variance honnête qui sature le score. Un échec de H_A ne désigne donc pas le point focal.
- **E4 peut être vrai par construction.** Si le déclencheur de l'équipe rouge est lexical (un identifiant), le masquage le neutralise par définition. Le déclencheur doit être sémantique et ré-identifiable en principe.
- **E0.** Le critère d'inclusion (« adversaire stratégique » et « hasard explicitement secret ») est assez étroit pour que H_A devienne quasi automatique. Le contrôle positif sur U1 ne calibre pas la sévérité de ce critère pour U8 ou U11.

**(b) Conditions de perte de puissance ou de non-jugeabilité**
- **E2.** Avec un budget p = 0,02 et K fautes par trajectoire, la détection sous tirage vaut 1 − 0,98^K. Sous un calendrier déterministe connu, elle est proche de 0. L'écart de 15 points n'est atteignable que si K ≥ 9 (illustratif). Si la loi de K est concentrée sur de petites valeurs, H_B est vraie par construction.
- **E3.** Le TPR à 1 % de fausses alertes exige le quantile 0,99 de la loi du désaccord honnête D_h. Avec k = 5 tirages, un score de désaccord prend au plus quelques valeurs. Le quantile tombe alors sur un atome, et le taux de 1 % n'est atteignable qu'avec un seuil randomisé : le critère est non jugeable tel quel.
- **Règle d'arrêt.** « Si l'intervalle chevauche le seuil, on augmente n » est un arrêt optionnel. Sans correction séquentielle, le niveau de 95 % n'est pas tenu. Si l'AUROC vraie vaut exactement 0,60, la procédure ne s'arrête jamais. Il faut un n maximal préenregistré.
- **E0.** Un κ ≥ 0,7 est ininterprétable quand la prévalence d'inclusion est proche de 0 : l'accord brut peut être élevé alors que κ est faible ou instable. Il faut rapporter aussi l'accord spécifique sur les inclusions.

**(c) Contrôles négatifs dont l'absence serait fatale**
- **E1, contrôle réel contre réel.** Deux lots d'unités réelles, produits à des moments ou avec des gabarits différents, doivent être étiquetés « planté / réel ». La permutation d'étiquettes ne détecte qu'une fuite de l'estimateur, pas un décalage entre lots.
- **E2, calendrier tiré mais révélé à l'équipe rouge.** C'est le seul contraste qui sépare le *secret* du tirage de son caractère *aléatoire*. Sans lui, la conclusion « le hasard fait un travail stratégique » n'est pas soutenue.
- **E3, équipe rouge à faute déterministe** (indépendante de la graine). Son désaccord doit rester au niveau honnête. Sinon le score détecte la présence d'une faute par un autre canal que la non-coordination.

---

## Sur la proposition C

**(a) Défauts de méthode**
- **Statuts.** De nombreuses références citées de mémoire portent le statut VÉRIFIÉ, alors que leurs années sont marquées « illustratif ». Une année illustrative rend l'attribution invérifiable au sens de la règle 3, et rien dans la session n'étaye ces statuts.
- **Instrument V.** L'énoncé « condition nécessaire et suffisante […] O(√T) », marqué VÉRIFIÉ, va au-delà de ce que je peux attribuer : référence à vérifier.
- **Expérience 1 : fuite entre construction et évaluation.** L'attaque est conçue pour n'insérer aucune affirmation fausse au niveau de la phrase, et le bras de référence vérifie justement l'exactitude locale des affirmations. Le comparateur est donc aveugle à l'attaque par construction, et ΔTPR ≥ 0,25 est presque acquis d'avance. Ce résultat ne dirait rien de la permutation.
- **Expérience 1 : coûts.** Deux passes complètes contre un oracle portant sur 10 % des affirmations : ces coûts ne sont pas commensurables. Le « coût équivalent » annoncé n'est pas défini.
- **Expérience 1 : contrôle négatif 2.** Il prescrit son issue (TPR < 0,10). C'est une hypothèse auxiliaire, pas un contrôle.
- **Expérience 1 : falsification.** Elle attribue à P2 (décomposabilité) un résultat qui ne la teste pas.
- **Expérience 3 : deux facteurs confondus.** Les bras diffèrent à la fois par le type de pièges (recombinés ou standard) et par le seuil (stochastique ou fixe). Sans plan factoriel 2×2, aucun effet n'est attribuable à l'Instrument V. De plus, l'agent reçoit des expérimentateurs un module de détection des pièges : la détectabilité mesurée est celle de ce module.
- **Expérience 2.** On ne sait pas qui extrait le « score de risque ». Si c'est un modèle de langue, il est commun aux deux bras et produit lui-même des violations métamorphiques honnêtes.
- **Absence d'annotation humaine.** Le texte annonce « aucun coût d'annotation humaine ». Les invariants métamorphiques servent alors à la fois de vérité et d'instrument.

**(b) Conditions de perte de puissance ou de non-jugeabilité**
- **Expérience 1 : score binaire.** Le score est une divergence binaire de recommandation après dé-permutation. La courbe ROC n'a donc qu'un point, et l'AUROC vaut (1 + TPR − FPR)/2 : AUROC ≥ 0,80 exige TPR − FPR ≥ 0,60.
- **Expérience 1 : FPR non atteignable.** Le critère « TPR à FPR = 0,05 » n'est défini que si P(divergence | loyal) ≤ 0,05. À T = 0,7, si cette probabilité dépasse 0,05, le critère est non jugeable.
- **Expérience 2.** Supposons m = 3 transformations tirées uniformément parmi M modules, et que seule une perturbation dans les c modules voisins de la vulnérabilité cachée puisse révéler la dissimulation. Alors TPR ≲ 1 − (1 − c/M)³. Le seuil TPR ≥ 0,75 exige c/M ≥ 0,37 environ (illustratif).
- **Instrument V : concavité de la ROC.** Face à un attaquant non adaptatif, un seuil tiré à FPR moyen égal donne E[TPR(τ)]. Si la ROC est concave, ce point est sur une corde, donc sous le TPR du seuil fixe. Le gain n'existe que si l'adaptation du contrôlé dépasse cette perte.
- **Expérience 3.** L'AUROC_agent repose sur des estimations internes de l'agent. Si elles prennent peu de valeurs, on retrouve le problème des atomes.

**(c) Contrôles négatifs dont l'absence serait fatale**
- **Expérience 1.** Un agent déloyal dont le biais est invariant à la permutation (par exemple « défavoriser l'option la plus coûteuse »). Sa divergence doit rester au niveau loyal ; sinon la détection ne vient pas de la permutation.
- **Expérience 3.** Le plan 2×2, plus une condition « seuil tiré mais révélé ».
- **Expérience 2.** Des perturbations hors du voisinage causal, appliquées à l'agent déloyal, pour mesurer les violations qui ne doivent rien à la dissimulation.

---

## Sur la proposition D

**(a) Défauts de méthode**
- **Asymétrie de réglage.** G est mesuré contre « le meilleur comparateur mécanique réglé sur développement ». Choisir le maximum parmi plusieurs comparateurs sur le développement, alors que l'instrument aléatoire est réglé une seule fois, crée une asymétrie dont le sens dépend du nombre de candidats. Il faut des budgets de réglage égaux et déclarés.
- **Dissuasion par gains simulés.** Les paiements sont énoncés dans la consigne. Une baisse des choix fautifs mesure alors la conformité à un énoncé, pas la sensibilité à une sanction. Pour un agent qui ne subit rien, « sanction avec conséquence sur le score » et « sanction sans conséquence » sont deux textes : le contrôle prévu ne sépare donc pas les deux interprétations.
- **Audit contre tri par anomalies.** L'issue dépend de qui place les fautes et de ce qu'il sait du comparateur. Il faut croiser le facteur « agent informé / non informé de la règle de tri ».
- **Sentinelles.** Si le classifieur de reconnaissance est entraîné sur les sorties du générateur de sondes, il apprend la signature du générateur. Même remède qu'en A : séparer les générateurs.
- **Longueur non contrôlée.** Le pilote prévoit 3 000 jetons générés par rôle. La longueur de contexte n'est pas contrôlée, alors qu'elle module probablement la détectabilité des effets du tirage. Le « long » de la question n'est pas garanti sur ce banc.

**(b) Conditions de perte de puissance ou de non-jugeabilité**
- **Règle commune.** Les IC sont calculés par grappes de tâches, avec m remises par tâche et une corrélation intra-tâche ρ. L'effectif efficace vaut n/(1 + (m − 1)ρ). Pour un taux voisin de 0,5, la demi-largeur à 95 % passe sous 5 points seulement si n_eff ≳ 385 (illustratif). Avec 400 paires et ρ > 0, la plupart des duels resteront non tranchés.
- **Sondage pondéré (Horvitz-Thompson).** Si les fautes sont rares et Σ π_i y_i < 1, l'estimateur vaut 0 dans la majorité des réalisations. L'EQM comparée à l'extrapolation est alors dominée par cet atome, et le duel est non jugeable à faible prévalence.
- **Défi algébrique.** La borne 1/2 vaut sur un corps exact. En virgule flottante avec une tolérance η, si les entrées de AB − C sont inférieures à η/‖r‖, la puissance est nulle. Le banc comptable doit être en entiers ou en rationnels.
- **Marque.** On suppose une statistique z sur une liste verte de fraction γ et de longueur L, comme dans le travail cité par D (RAPPORTÉ). Si la réécriture ramène la proportion verte à γ + δ avec δ√L/√(γ(1−γ)) bien inférieur à z₁₋α, la puissance retombe à environ α.

**(c) Contrôles négatifs dont l'absence serait fatale**
- **Test A/A.** Comparer un instrument à lui-même (deux tirages indépendants du même protocole), pour vérifier que l'IC par grappes couvre 0 au taux nominal. Toute la règle de décision de D repose sur cet IC.
- **Sentinelles.** Un contrôle réel contre réel, avec des lots honnêtes issus de générateurs différents, et pas seulement du même générateur.
- **Audit.** Un tirage révélé au contrôlé, pour isoler l'apport du secret.

---

## Sur la proposition E

**(a) Défauts de méthode**
- **Incohérence de statut.** L'énoncé U4 (ii), « deux instances clonées ne peuvent pas coordonner », est marqué VÉRIFIÉ, alors que E2 de la même pièce teste précisément cette capacité comme HYPOTHÈSE. Une expérience ne peut pas à la fois tester et présupposer la même proposition ; l'interprétation de E2 en dépend.
- **E1 : format et hasard confondus.** U3 diffère de U1 à la fois par l'artefact (graphe engagé ou rapport) et par le tirage. Sans un bras « graphe + arêtes choisies par règle fixe », le gain peut venir du format seul.
- **E1 : comparateur faible par construction.** Contre un mensonge unique sur la conclusion, 3 affirmations tirées uniformément parmi N détectent avec une probabilité d'environ 3/N. Le gain de U3 sur U1 est donc presque acquis. Le comparateur pertinent, « audit du seul dernier saut », figure dans le tableau (c) mais pas dans E1.
- **E2 : transformations groupées.** U4 regroupe trois transformations, ce qui empêche d'attribuer l'effet. De plus, une transformation affine des montants préserve les rapports et les ordres : des quasi-identifiants sont conservés par construction.
- **E3 : position confondue.** Le critère ne porte que sur le dernier tiers. Un effet y confond l'adaptation stratégique et la dégradation due au long contexte.
- **E4 : fuite construite.** Sans tampon temporel, une intervention qui ajoute une latence visible fabrique elle-même la fuite : on mesure alors le dispositif, pas P1. De plus, demander à l'agent une prédiction hors bande mesure une capacité sollicitée, pas un comportement.
- **Tableau (c).** La cible U1, TPR ≥ 1 − (1 − p)^k − 0,05, dépend de k, qui est choisi par l'attaquant. Le critère change avec l'attaque.

**(b) Conditions de perte de puissance ou de non-jugeabilité**
- **U7.** La formule 1 − q^m − (1 − q)^m suppose des décisions d'attaque i.i.d. entre branches. Pour des Bernoulli échangeables de corrélation ρ et m = 2, P(divergence) = 2q(1 − q)(1 − ρ). Si les transformations sont neutres et que la décision dépend de l'entrée, ρ tend vers 1 et la puissance tend vers 0.
- **E3.** L'argument de concavité vu en C s'applique au seuil de Laplace à taux de révision honnête égal. De plus, si l'échelle b du bruit est petite devant l'écart entre les lois de score honnête et subversive, les deux bras sont indiscernables.
- **E4.** Il y a 100 positifs répartis en 20 tâches. Si les prédictions de l'agent sont corrélées au sein d'une tâche, un IC par grappes à 20 grappes est trop large pour trancher autour de 0,65 (illustratif).

**(c) Contrôles négatifs dont l'absence serait fatale**
- **E1.** Un bras graphe + arêtes déterministes.
- **E2.** Des paires honnêtes soumises à U4, pour calibrer le taux de 5 % de fausses alertes, qui est annoncé sans contrôle honnête.
- **E3.** Un attaquant de langue non adaptatif sur les mêmes 60 étapes, pour séparer l'effet de position de l'effet d'adaptation.
- **E4.** Une condition à latence égalisée, et un contrôle réel contre réel.

---

## Sur la proposition F

**(a) Défauts de méthode**
- **E1 : règle non exclusive.** Il y a deux comparateurs (mécanique, et sans engagement), plus une condition « ne perd pas significativement » dont le test n'est pas défini. Il existe donc des issues où ni H_A ni H_B n'est falsifiée, ce qui contredit B4.
- **E2 : critère disjonctif.** « Réduction ≥ 70 % OU TPR_meta ≥ 80 % » donne deux chances d'accepter H_A.
- **E3 : dépendance au rédacteur.** La règle de coordination de Schelling est écrite par les expérimentateurs. La difficulté de coordination, donc l'issue de H_B, dépend de la qualité de cette règle.
- **E4 : nombre de relèves confondu.** Une loi géométrique de paramètre 0,15 sur 30 étapes donne environ 4,5 relèves attendues, contre une seule relève dans le contrôle à instant fixe. L'écart mêle le nombre de relèves et l'aléa.
- **E5 : construction des leurres.** Les leurres sont obtenus par perturbation minimale de tâches historiques. Deux problèmes : (i) la vérité terrain du leurre n'est plus connue par construction ; (ii) les originaux peuvent figurer dans les données d'entraînement, de sorte qu'un ε_dist élevé peut refléter la mémorisation plutôt que la détection d'évaluation.
- **Résidu (tableau c).** Mesurer le « gain sur le résidu » conditionne sur le passage du filtre mécanique, ce qui modifie les lois des cas honnêtes et fautifs. Le taux de fausses alertes doit être rapporté sur les deux dénominateurs, total et résiduel.

**(b) Conditions de perte de puissance ou de non-jugeabilité**
- **U5 (cut-and-choose).** Avec M = 5 et k = 3 ouverts, un attaquant qui corrompt un seul artefact échappe avec probabilité C(4,3)/C(5,3) = 0,4. La détection vaut alors 0,6, sous la cible de 0,8 : le critère échoue par construction contre cette attaque, si l'agrégation des deux artefacts restants est atteinte par un seul corrompu.
- **E3.** Le seuil à 5 % de fausses alertes est estimé sur 200 paires honnêtes. L'erreur standard du taux réalisé est d'environ √(0,05·0,95/200) ≈ 0,015, donc le taux effectif peut se situer entre 2 et 8 % (illustratif). Si le score NLI est discret, on retrouve le problème des atomes.
- **E2.** Le critère n'est jugeable qu'avec une correction pour la disjonction ; sans elle, le risque d'accepter H_A à tort dépasse le niveau annoncé.

**(c) Contrôles négatifs dont l'absence serait fatale**
- **E4.** Des relèves en nombre égal, à positions fixes.
- **E3.** Des clones sabotés *sans* règle canonique, pour montrer que la coordination tient à la règle.
- **E5.** Un contraste entre tâches réelles historiques et tâches réelles nouvelles, pour contrôler la mémorisation.
- **E1.** Le contrôle « défi prévisible » est bien conçu ; il lui manque une règle de décision chiffrée.

FIN-DE-CELLULE