# Tour III.2 — Proposition A : critique croisée de méthode

**Pièces.** B, C, D et E sont reçues, chacune close par sa ligne de fin ; je ne vois aucune coupure. Ma propre conception n'est pas retransmise et je ne m'y réfère pas.

**Lecture de la question.** Le bloc QUESTION est celui auquel les conceptions ont répondu. Le livrable du tour fixe la forme (a)(b)(c). J'en garde l'exigence « plus profond, pas plus long » : je ne retiens que les défauts qui changeraient un verdict.

**Statuts.**
- Les FAITS ne portent pas de statut explicite ; je les cite comme « FAITS » sans les promouvoir.
- Toutes mes critiques sont des **HYPOTHÈSES** : analyse sur pièces, rien n'a été exécuté.
- Les théorèmes classiques invoqués sont **RAPPORTÉ**, de mémoire.
- Les nombres marqués « (calcul) » sont dérivés d'une loi binomiale, pas des faits.
- Les seuils des autres propositions sont cités comme « (illustratif, de X) ».

---

## Sur la proposition B

### (a) Défauts de méthode

1. **P2 est décidé avant calcul, dans les deux sens.** Pour un agrégateur « seuil sur somme » et des marges discrètes fixées, la borne connue sous dépendance arbitraire est une borne de Fréchet sur la loi d'une somme (type Makarov–Rüschendorf ; RAPPORTÉ, à vérifier). Évaluée sur ces mêmes marges, elle est la valeur du même programme linéaire multi-marginal.
   - Comparée à cette borne sur marges discrètes, la courbe coïncide par construction : H_A est acquise sans expérience.
   - Comparée à une forme close pour marges continues, un écart strict apparaît génériquement par discrétisation : H_B est acquise sans expérience.
   - Le critère « écart strictement positif, certifié en rationnel, sans tolérance » certifie donc l'artefact avec la même rigueur qu'une découverte.
2. **P2 : la liste des agrégateurs est une variable confondante.** L'objet d'intérêt est sup sur les agrégateurs de inf sur les dépendances. B calcule l'inf agrégateur par agrégateur, donc le résultat dépend de la liste. De plus, le taux de fausses alertes « fixé » suppose une loi jointe honnête que personne ne choisit dans le texte. Si elle est estimée, le niveau devient un estimateur et non un paramètre.
3. **P3 : le duel dépend de la définition de l'avantage linéaire.** B écrit que l'appariement des moments d'ordre ≤ 2 rend toute sonde linéaire aveugle par construction. Ce n'est vrai que si l'avantage est une différence de moyennes du score.
   - Si l'avantage est sup sur les demi-espaces de |P(H) − Q(H)| (sonde seuillée), la sonde lit toute la loi de la projection. Un avantage nul dans toutes les directions impose alors P = Q (Cramér–Wold, RAPPORTÉ).
   - Sous la première définition, H_B est fausse par construction ; sous la seconde, H_A l'est.
   - L'antériorité probable sous la seconde est le pseudo-aléa contre les demi-espaces par indépendance bornée (référence à vérifier).
4. **P3 : δ n'est pas une fonctionnelle de (P, Q).** « La sortie diffère d'au moins δ » exige une application activations → sortie. Si elle est libre et non linéaire, le score se maximise trivialement.
5. **P3 : effort de recherche asymétrique.** La boucle optimise hors de la famille connue, mais rien n'optimise dans la famille. H_B peut être « confirmée » par une recherche faible du côté connu.
6. **P4 : fuite.** Les quarante énoncés connus servent déjà à éprouver le juge de nouveauté (FAITS). Des mutants de ces énoncés sont détectables par souvenir de la forme canonique, pas par lecture. Par ailleurs, H_A dit « aussi bien qu'un humain », mais aucun bras humain n'est mesuré ; le seuil est absolu.
7. **Utilité (section 4) : circularité possible.** Rejouer la décision « avec et sans le résultat » sur les mondes plantés est circulaire si ces mondes ont servi à tuer ou à sélectionner le résultat.

### (b) Conditions de perte de puissance

- **P1.** Le nombre de connus déguisés classés « réduit » suit Bin(n, π). Avec n = 1, le contrôle passe avec probabilité π. Pour exclure π < 0,9 au risque 5 %, il faut n ≥ 29 succès sans échec (calcul).
- **P2.** Soit Δ_m l'écart à m points de grille.
  - Non jugeable si Δ_m → 0 quand m croît. Jugeable seulement si inf Δ_m > 0 sur une suite de grilles emboîtées fixée d'avance.
  - Sans puissance si TV(P0_i, P1_i) = 0 pour tout i : la valeur vaut α pour tout agrégateur.
  - Sans puissance aussi si les supports sont disjoints : la valeur vaut 1.
- **P3.** Si le support compte n ≤ d + 1 points en position générale, tout sous-ensemble est découpé par un demi-espace. L'avantage linéaire vaut alors TV(P, Q) et le critère ne distingue plus la sonde linéaire d'un test quelconque. Il faut n ≫ d.
- **P4.**
  - Un raté sur 20 (illustratif, de B) est compatible avec un taux de ratés jusqu'à ≈ 0,22 (borne supérieure unilatérale à 95 %, calcul).
  - Les inégalités large et stricte coïncident sous toute loi sans atome. Si une fraction e des mutants est équivalente à l'original, l'étiquette « faux » est erronée et la détection plafonne à 1 − e.
- **P5.** Le nombre de classes observées est un estimateur de richesse biaisé vers le bas, croissant avec le nombre de morts, et borné par le nombre de mondes tueurs. Il n'est pas jugeable sans estimateur de masse manquante (fréquence des singletons).

### (c) Contrôles négatifs dont l'absence serait fatale

- **P2.** Le cas k = 2, où la borne exacte est connue : le programme linéaire doit la rendre à l'identique. Sans lui, et sans les grilles emboîtées, aucun écart n'est interprétable.
- **P3.** L'optimum exact, ou une recherche à budget égal, restreint à la famille connue.
- **P4.** Des mutants équivalents plantés, qui ne doivent pas être signalés, et des énoncés pris hors des quarante.
- **Tableau (c), recherche d'antériorité.** Les « énoncés vraiment neufs (paramètres inédits) » sont des spécialisations de théorèmes connus. Leur étiquette « neuf » est fausse par construction et le taux de faux « connu » mesuré sur eux n'a pas de sens.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts promus.** C étiquette « [VÉRIFIÉ dans les faits] » des éléments que les FAITS déclarent sans statut, et « [VÉRIFIÉ] » des références citées de mémoire. Conséquence de méthode : l'Expérience 2 suppose douze mondes dotés d'une valeur scalaire V*. Les FAITS disent « vérité calculée », pas « valeur minimax ».
2. **Méthode 1 : U n'est pas indépendante de L.** Le bras B « observe la structure de la distribution gagnante » puis propose une formule. U décrit donc L, et |U − L| petit est un ajustement, pas un écart de dualité.
   - Un écart de dualité oppose une borne côté saboteur (une loi exhibée) à une borne côté moniteur (un test exhibé).
   - C range Fano et Pinsker parmi les bornes supérieures, alors qu'elles minorent le risque. Deux minorants proches ne ferment rien.
   - Le sup porte sur des saboteurs contre des « moniteurs existants » : l'inf sur les moniteurs manque.
3. **Fuite construction/évaluation.** Les mêmes douze mondes gèlent la conjecture (|U − L| < 10⁻⁴ « sur tous les mondes plantés », illustratif, de C) et l'évaluent (δ). Une formule à douze paramètres libres ou plus interpole n'importe quoi.
4. **Expérience 2 : la vérité fuit par le verdict.** Si le test de mort tue U < V* et laisse vivre U ≥ V*, le bras binaire fait une dichotomie : t verdicts localisent une constante à 2⁻ᵗ près. Les deux bras atteignent alors δ → 0 par construction dès que la borne est une constante. L'expérience mesure le débit de fuite de la vérité, pas la découverte. Elle contredit aussi le principe des FAITS : la vérité reste hors de la machine.
5. **Expérience 1 : trois problèmes.**
   - Deux ingrédients sont confondus : l'élagage et la réinjection du contre-exemple dans l'invite.
   - Les théorèmes de niveau licence sont dans les corpus d'entraînement. Le taux de sous-lemmes faux y diffère de celui sur énoncés neufs.
   - Un gain entre 10 % et 20 % (illustratifs, de C) ne falsifie rien, ce qui viole B4.
6. **Faux morts irréversibles.** Un sous-lemme vrai tué par une erreur de traduction en Python reste mort (FAITS : « un mort reste mort »). Ce taux n'est mesuré nulle part.
7. **Témoin de non-vacuité insuffisant.** ∃x P(x) est satisfait par un témoin dégénéré (Dirac, horizon nul). Il ne détecte pas non plus les conventions de division totale.
8. **Méthode 3 : vrai par construction.** Δ(ρ) est choisi « pour que l'inégalité redevienne vraie sur tous les mondes plantés ». Tout Δ assez grand convient. Il manque un critère de serrage hors échantillon.

### (b) Conditions de perte de puissance

- **Filtre numérique (Méthode 2, Instrument 2).**
  - Un sous-lemme faux est violé sur une région de masse p sous la loi de tirage de la banque. La puissance vaut 1 − (1 − p)^N. Elle est nulle si p = 0, par exemple si la violation exige des moments infinis ou une dépendance non stationnaire absents de la banque.
  - Pour une inégalité vraie et serrée, la marge inf(droite − gauche) vaut 0. Avec un estimateur Monte-Carlo d'écart-type σ/√N, le faux rejet au cas d'égalité est voisin de 1/2.
  - Une tolérance τ rétablit la survie mais annule la puissance contre toute violation inférieure à τ.
  - « Survie des vrais = 100 % » (illustratif, de C) est donc inatteignable pour une borne serrée estimée.
  - « Constante violée de 10 % » (illustratif, de C) n'est détectable que si 0,1·|V| ≫ σ/√N.
- **Expérience 1.** Avec 20 théorèmes appariés, le meilleur cas au seuil est quatre discordances toutes dans le même sens. La probabilité unilatérale sous l'égalité des bras est (1/2)⁴ = 0,0625 (calcul). Le seuil franchi ne rejette pas l'égalité à 5 %.
- **Expérience 2.** δ est indéfini si V* = 0. Le duel est non jugeable si la borne n'a qu'un paramètre scalaire, à cause de la dichotomie.
- **Expérience 3.**
  - Le critère « `exact?` ferme en 5 s ⇒ connu » a pour rappel P(fermeture | connu), conditionné au succès de la formalisation. Je ne sais pas l'estimer. Hors lemmes déjà dans Mathlib, je l'attends faible.
  - L'aire sous la courbe ROC n'est pas interprétable si les quarante énoncés « réellement modifiés » contiennent une fraction inconnue d'énoncés faux ou déjà connus.

### (c) Contrôles négatifs dont l'absence serait fatale

- Des paramètres hors plage : U est ajustée sur les mondes de développement et évaluée en extrapolation. Sans cela, la Méthode 1 n'est pas jugeable.
- Un bras binaire dont le verdict vient d'une recherche de contre-exemple, sans accès à V*.
- Des sous-lemmes vrais et serrés plantés, pour mesurer le taux de faux morts.
- Des énoncés connus hors des quarante, pour le juge de nouveauté.
- Des théorèmes plantés non vacus mais vrais seulement sur des instances dégénérées, pour le témoin de non-vacuité.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Seuil « gain strict » sur lot fini, sans réplication.** Si les deux bras ont la même loi, P(gain > 0) = (1 − P(égalité))/2. Le verdict est alors tiré au sort. L'égalité compte contre H_A, ce qui crée une asymétrie non justifiée.
2. **Une moitié du critère est vide.** Les séparations sont certifiées par calcul exact, donc les fausses séparations valent zéro dans les deux bras par construction. « Sans fausse séparation supplémentaire » ne contraint rien.
3. **La référence par énumération décide l'issue.** Avec c contraintes, la suppression systématique visite 2^c sous-ensembles.
   - Si 2^c fois le coût d'un programme linéaire tient dans le budget, elle trouve tout et H_A est fausse par construction.
   - Au-delà, elle ne couvre qu'une fraction et H_A est vraie par construction.
   - L'issue est donc une fonction de (c, taille du jeu, budget) et de la loi des tailles dans le lot réservé, pas de la méthode.
4. **D-valeur : la récurrence ne calcule peut-être pas le bon objet.** La récurrence arrière est valide si l'adversaire est une loi fixée (décision à un joueur) ou si la mémoire est parfaite.
   - Un auditeur restreint à une statistique est un joueur à mémoire imparfaite.
   - Contre un saboteur stratégique, stratégies mixtes et comportementales cessent de coïncider et la valeur ne s'obtient plus par récurrence (théorème de Kuhn, RAPPORTÉ ; résultat de complexité attribué à Koller et Megiddo, référence à vérifier).
   - D ne dit pas lequel des deux modèles est visé. Dans le second, le certificat exact certifie autre chose que la valeur du jeu.
5. **Généricité.** Dans une famille de jeux à probabilités génériques, fusionner deux historiques de postérieurs distincts fait perdre de la valeur presque sûrement. Compter les séparations compte alors des instances, pas des découvertes. D reconnaît la réduction au critère de suffisance d'un état, mais garde le comptage comme métrique du duel.
6. **Utilité avant/après par la même équipe.** L'équipe apprend le cas réservé entre les deux calculs. L'effet d'ordre est confondu avec l'effet du résultat.
7. **Cloisonnement « par famille ».** La définition de la famille est choisie par le programme, donc ajustable. La fuite par les corpus d'entraînement des proposeurs n'est pas traitée.

### (b) Conditions de perte de puissance

- **Duels de comptage.** Soit q la probabilité qu'une séparation existe sous la loi du lot. Si q est proche de 0 ou de 1 et que la couverture des deux bras est au plancher ou au plafond, alors P(égalité) → 1. H_A est falsifiée mécaniquement, sans information sur la méthode.
- **D-frontière.** Une contrainte peut être redondante sur l'arbre (horizon T, alphabet a) et active à (T + 1, a + 1). La « frontière » estimée est une fonction de (T, a). Elle n'est pas jugeable sans stabilité sur au moins deux couples. D refuse d'extrapoler mais compte quand même les frontières du lot.
- **Antériorité.** Le verdict est « aucune réduction trouvée dans ce périmètre ». Avec un a priori π que l'énoncé soit connu et un rappel ρ du relecteur, P(connu | rien trouvé) = π(1 − ρ) / (π(1 − ρ) + 1 − π). Sans estimateur de ρ, le verdict ne porte aucune information chiffrable.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un test A/A : le même bras avec deux graines doit rendre « pas de différence ». Au seuil strict, il en rendra une environ une fois sur deux.
- Des jeux plantés où les seules divergences d'action sont en états inatteignables : zéro séparation attendue.
- Un même jeu résolu par récurrence et par programme linéaire en forme séquentielle : accord exigé à adversaire fixé, désaccord à détecter à adversaire stratégique.
- Un théorème placebo, vrai et sans rapport, divulgué à l'équipe d'utilité. Il mesure l'effet de recevoir un théorème quelconque.
- Des réductions plantées, pour estimer ρ.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts auto-attribués.** « VÉRIFIÉ » est posé sur de la littérature citée de mémoire, sur des jugements (« VÉRIFIÉ méthodologiquement ») et sur une affirmation concernant la part de chance. Aucune vérification n'est jointe.
2. **M1 : prémisse trop large.** Un certificat dual rationnel fini existe pour un programme linéaire à données rationnelles. Trois cas sortent de ce périmètre :
   - n observations indépendantes : la loi du saboteur entre au degré n, le problème n'est plus linéaire ;
   - sondes de rang k : l'ensemble des tests est une union sur les projections, non convexe ;
   - programmes semi-définis : l'optimum dual est en général algébrique irrationnel, sans certificat rationnel exact.
   
   Les cibles annoncées pour M1 touchent les deux premiers.
3. **M1 : le dual n'est pas identifié.** Si le programme est dégénéré, la face optimale duale est de dimension positive et le solveur rend un sommet arbitraire.
   - La suite y*(m) peut sauter d'un sommet à l'autre. Le test de mort « support non interpolable » tue alors sur un artefact de solveur.
   - Inversement, onze points (m de 2 à 12, illustratif, de E) et une famille de formules à onze coefficients ou plus garantissent une interpolation exacte.
4. **M1 : la « réduction » de la preuve n'est pas établie.** E écrit que la preuve se réduit à vérifier A^⊤ y*(n, d) ≥ c par `positivity` ou `linarith`. Pour n symbolique, c'est une famille infinie d'inégalités, qui demande une récurrence ou des identités de sommes. Aucune expérience de E ne le teste.
5. **E3 : vrai par construction.** Dans R2, l'énoncé est scellé. Un énoncé faux y est improuvable par correction du noyau, et l'agent ne peut pas le dégrader. Le 0 % est connu d'avance. E3 est une mesure à un seul bras (R1) présentée comme un duel.
6. **E4 : contenu confondu.** Les deux versions sont deux théorèmes différents, la version `Fintype` étant un cas particulier. H_A est quasi infalsifiable. Le coût pertinent se compare à énoncé final égal : `Fintype` plus relèvement, contre preuve directe.
7. **M2 : trois défauts.**
   - Quarante rondes (illustratif, de E) adaptatives interrogent la même banque scellée. C'est le surajustement que E cite lui-même sous « analyse de données adaptative ».
   - Une hypothèse est une propriété d'une loi. « Satisfaite par 90 % des traces » (illustratif, de E) exige un estimateur et un test qui ne sont pas donnés.
   - L'hypothèse n'est vérifiée que sur des traces honnêtes. Lue à l'envers, elle contraint le saboteur, qui peut la violer.
   
   Les FAITS n'attestent pas l'existence de ces traces.
8. **M3 : séparation par spécialisation.**
   - Toute borne propre à une instance, par exemple la valeur exacte du monde, bat strictement toute borne générale sur cette instance. Le « témoin de séparation » existe par construction.
   - La nouveauté mesurée est l'incomplétude d'une base fermée de trente bornes (illustratif, de E).
   - Si la base est construite en regardant les quarante énoncés, le rappel sur ces quarante est acquis par construction.

### (b) Conditions de perte de puissance

- **M1.**
  - Si la dimension de la face optimale duale est positive, y*(m) n'est pas identifié. Il faut une règle de sélection canonique fixée d'avance.
  - Avec p paramètres libres et M points, le critère est non jugeable si p ≥ M. Seuls des points hors plage le rendent jugeable.
- **E3.**
  - Zéro sur dix est compatible avec un taux jusqu'à ≈ 0,26 (calcul : 1 − 0,05^(1/10)). « R1 à 0 % falsifie H_A » n'est donc pas soutenu.
  - Le taux observé vaut 1 − (1 − p)^N avec N tentatives par énoncé. Il faut rapporter p par tentative, sinon le budget fixe le résultat.
- **E1.**
  - Avec n = 15, l'écart-type de l'estimateur au voisinage de 0,2 est ≈ 0,10 (calcul).
  - La cellule « juge nu > 20 % et ΔR < 25 points » (illustratifs, de E) n'a pas de verdict.
- **E2.** Les 24 instances sont tirées de 12 mondes. Si la corrélation intra-monde est forte, la taille effective est 12, et le seuil « +4/24 » (illustratif, de E) peut venir de deux mondes.
- **M2.** Après T rondes adaptatives sur une banque de taille n, la fraction satisfaite surestime la fraction en population. J'attends un biais croissant avec T/n. La forme exacte est à vérifier.
- **M3.** P(séparé | spécialisation d'un connu) ≈ 1 : le portier n'a aucune puissance contre cette classe.

### (c) Contrôles négatifs dont l'absence serait fatale

- **M1.** Un monde sans forme close, dont les valeurs n'ont pas de structure en m : la méthode doit rendre « pas de formule ».
- **M1.** Un programme dégénéré planté, de formule duale connue : il éprouve la sélection canonique.
- **M3.** Des spécialisations de théorèmes connus (verdict attendu : « connu ») et des connus hors de la base.
- **M2.** Une banque de validation jamais consultée pendant les rondes.
- **M2.** Une hypothèse plantée, vraie sur l'honnête et violable par le saboteur, qui doit être signalée.
- **E4.** La comparaison à énoncé final égal.

---

## Ce dont je me sers, en le disant

- **De B** : le verdict jamais fondé sur un flottant, et l'issue « déjà connu » comptée comme valide.
- **De D** : l'exigence d'une perte depuis l'état initial, et le verdict d'antériorité borné à un périmètre.
- **De E** : l'évaluation d'une formule hors de la plage d'ajustement.
- **De C** : le proposeur trivial conservateur comme contrôle.

Aucun de ces emprunts ne lève les défauts ci-dessus.

FIN-DE-CELLULE