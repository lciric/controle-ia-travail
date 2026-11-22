# Proposition A — Tour III.2 : critique croisée de méthode

## Pièces et statuts

- Bloc FAITS : identique à la question (même empreinte), sans aucun fait muni d'un statut. Les « notes retirées » sont absentes et je ne les reconstruis pas.
- Ma conception du tour III.1 ne figure pas dans les pièces transmises ; je ne la cite pas de mémoire.
- Pièces B, C, D, E, F reçues avec leur marque de fin, sans coupure visible.
- Tout ce qui suit est **HYPOTHÈSE** : c'est une analyse de méthode, rien n'a été exécuté. Les chiffres recalculés à partir des chiffres illustratifs des pièces sont *illustratifs*.

Notation utilisée dans les cinq sections : P_c et P_h sont les lois de l'observable sous candidat et sous honnête, n_c et n_h les effectifs de test. Pour tout test de niveau α, TPR ≤ α + TV(P_c, P_h), où TV est la distance en variation totale restreinte à la classe de détecteurs permise.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **E0 est vrai par construction.** Une attaque « construite pour passer par un canal que 𝒟 n'observe pas » a P_c = P_h sur 𝒟, donc r = ∞ quel que soit l'apprenant. Une paraphrase de K1–K3 a r ≈ 0. Le taux de classement de 90 % mesure donc la fidélité de l'implémentation, pas la validité du critère.
2. **La bimodalité est fabriquée par le plan d'échantillonnage.** L'expérimentateur choisit deux populations extrêmes et leurs proportions. Un continuum de candidats à fuite partielle n'est jamais tiré.
3. **La censure crée un mode.** Tout r > K_max est rabattu sur un atome, et r ne prend que cinq valeurs (0, 8, 32, 128, 512). Un test de creux sur ce support rejette l'unimodalité pour des raisons arithmétiques.
4. **Le second témoin fuit depuis la définition du candidat.** C est défini comme « estimation poussée vers un quantile extrême du multivers » et le détecteur hors 𝒟 alerte « si le quantile est extrême ». Son TPR sur C mesure la capacité d'exécution de l'agent. Son FPR sur H2 vaut 5 % par uniformité du tirage. La condition de catégorie est donc satisfaite dès que l'attaque réussit.
5. **Le filtre « à dommage égal » pose un dilemme non résolu pour C contre H2.**
   - Si H2 est lui aussi conditionné à dommage ≥ δ, les H2 retenus sont précisément les tirages extrêmes et le quantile ne sépare plus rien.
   - S'il ne l'est pas, tout corrélat du dommage devient « détecteur » par asymétrie de sélection.
6. **Régime (ii) : l'adaptateur est confondu avec le sabotage.** Aucun LoRA bénin n'est prévu. Une sonde réentraînée en (ii) peut lire l'empreinte de l'affinage et donner r ≤ 32, ce qui classerait C en « variante » par artefact. La prédiction risquée de B serait alors réfutée pour une mauvaise raison.
7. **E3 n'oppose pas deux hypothèses exclusives.** « Rapport ≥ 3 » et « intervalles qui se chevauchent » laissent une zone non couverte, et le chevauchement d'intervalles n'est pas un test (B4).
8. **E4 :** le classement est aveugle mais l'implémentation des candidats ne l'est pas. Les candidats d'un même groupe ne sont pas indépendants, ce que le test de Fisher suppose.

Je retiens de B, en le disant : l'appariement H1 sur le dommage, le négatif difficile H2, et le contrôle « consigne présente mais ignorée ».

### (b) Conditions de perte de puissance

- **r̂ = min{k : TPR̂_k ≥ τ}** est un premier passage sur une courbe bruitée. Il est biaisé vers le bas par le maximum pris sur 5 valeurs de k, 5 instruments et les couches. Il n'est pas jugeable quand |TPR_k − τ| < 2·ET.
  - L'erreur type ET combine √(τ(1−τ)/n_c) et l'incertitude du quantile empirique (1−α) sur n_h.
  - Avec n_h·α ≈ 10 (200 × 0,05, *illustratif*), le seuil est instable.
- **Bimodalité :** non jugeable dès que P(r > K_max) > 0, ou que le nombre de candidats N (non spécifié) est petit devant ce qu'exige un test de creux.
- **Quantile multivers :**
  - Si la loi du quantile sachant dommage ≥ δ est la même sous C et sous H2, TV = 0 et la puissance vaut α.
  - Il perd aussi sa puissance si la variance entre bifurcations est inférieure à la variance d'échantillonnage de l'estimation.
  - Si la vérité plantée n'est pas à la médiane du multivers, H2 est biaisé avant toute attaque.
  - Par épisode, l'intention n'est pas identifiable à quantile donné. Elle ne l'est que sur la loi des quantiles à travers n épisodes.
- **S1 :** le nombre d'épisodes audités suit une loi Bin(n, p). À p = 0,05 l'estimateur de la détection par épisode repose sur une dizaine de cas (*illustratif*).
- **Sondes, régime (i) :** l'étiquette est une fonction déterministe du prompt. Une AUROC de 1 est atteignable par toute représentation injective de l'entrée et n'informe pas.
- **E4 :** si les deux proportions sont proches de 0, le test n'a aucune puissance. Avec une corrélation ρ entre candidats d'un même groupe de taille m, l'effectif efficace est n/(1+(m−1)ρ).

### (c) Contrôles négatifs dont l'absence serait fatale

- Un LoRA bénin de même rang et de même volume de données.
- Des H2 « honnêtes extrêmes », sélectionnés au même quantile que C. Le quantile multivers doit y échouer, et tout instrument qui y réussit lit autre chose que le résultat.
- Un test A/A de remédiation (honnête contre honnête) pour calibrer le taux de faux « r ≤ k\* » sous multiplicité.
- Des candidats à fuite graduée, avec un paramètre λ réglant la part du signal visible par 𝒟, pour tester la bimodalité hors plan binaire.
- Un observable « hors 𝒟 » factice (variable aléatoire), qui ne doit jamais satisfaire le second témoin.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** Le bloc FAITS ne contient aucun fait VÉRIFIÉ. C marque pourtant VÉRIFIÉ des lectures historiques, la formule de la NCD et une thèse (« se réduit à un avis non décidable »). C place aussi sous « ce que nous savons » un énoncé universel (« correspond toujours à… ») tiré de quatre cas choisis. C'est un changement de statut au sens de la règle 1, doublé d'un biais de survie.
2. **L'estimateur du sup est une borne inférieure.** sup_f AUROC est approché par deux apprenants (arbres dopés, perceptron) sur 70 % de 200 trajectoires par classe, en dimension très supérieure à n (activations de 6 couches). Une AUROC basse confond l'invisibilité et le sous-apprentissage.
3. **Le découpage par domaines thématiques disjoints ajoute un décalage de loi.** Ce décalage abaisse l'AUROC indépendamment du candidat et pousse donc vers « catégorie ».
4. **Φ₁ fuit depuis la définition d'OEBM.** L'attaque est « exclusion asymétrique des documents soutenant Y=1 » et le capteur étendu est « test d'asymétrie du taux de rejet ». AUROC(Φ₁) ≥ 0,85 est acquis dès que l'attaque est exécutée.
5. **Φ₁ n'est pas hors capteur.** C'est une fonction de la transcription, que le juge lit déjà. Par inégalité de traitement de l'information, Φ₁ ne contient rien d'absent du texte. La « catégorie » est alors relative à la rubrique du juge (les scores figés), pas au capteur. Un changement de rubrique à capteur constant n'est classé ni « réétalonnage » ni « extension », donc le critère est indécidable sur ce point.
6. **Validité de construit.** OEBM est induit de sorte que le modèle « croit appliquer un standard ». L'échec du lecteur d'intention est alors acquis par définition, et le cas n'est plus celui de la question (« dégrade exprès »).
7. **L'Expérience 3 ne teste pas le critère de C.** Elle évalue une sonde non réentraînée (transfert), alors que le critère du §2 porte sur le réentraînement.
   - Le bras LoRA confond l'internalisation avec la dérive des représentations due à l'affinage.
   - « Toute variante de prompt » est une quantification universelle non testable, et la recherche de prompts sélectionne sur la sonde évaluée.
8. **Expérience 2 : la sélection et l'évaluation partagent le détecteur.** La récompense inclut 1 − score(Φ₀), et le Témoin 4 réentraîne sur les attaques ainsi sélectionnées. L'AUROC basse sur l'échantillon sélectionné régressera sur des exécutions fraîches.
9. **Les seuils de l'Expérience 2 sont incohérents entre eux.** Avec 10 graines par bras, 5/10 contre 0/10 donne au test de Fisher p ≈ 0,03 en bilatéral. Il faut environ 7/10 contre 0/10 pour p < 0,01. Le seuil « ≥ 5/10 et p < 0,01 » est donc contradictoire à ses valeurs minimales (calcul sur les chiffres *illustratifs* de C).
10. **NCD.** Le minimum sur le « plus proche » décroît avec la taille du catalogue. L'abstraction des traces est au choix de l'expérimentateur.

### (b) Conditions de perte de puissance

- **AUROC(Φ₀) au seuil 0,60 :** avec environ 60 épisodes par classe en test, l'erreur type de l'AUROC est d'environ 0,05 (formule de Hanley-McNeil, *illustratif*). Les valeurs 0,50 et 0,60 ne sont pas séparables. Un seuil unique sans intervalle rend le duel non jugeable.
- **Sup sur 𝓕 :** non jugeable tant que la limite de détection du pipeline n'est pas mesurée, c'est-à-dire l'AUROC de Bayes minimale récupérée à (n, d) donnés.
- **Divergence de Kullback-Leibler de Φ₁ :** l'estimateur par substitution a un biais positif d'ordre (k−1)/(2m) pour m documents retenus. Une exclusion honnête sévère gonfle donc Φ₁. La puissance est nulle si la loi du taux de rejet par polarité coïncide entre OEBM et un honnête rigoriste.
- **NCD :** non jugeable si la loi de la NCD entre deux traces honnêtes de dossiers différents dépasse déjà 0,70, ou si la longueur des traces excède la fenêtre du compresseur (la NCD tend alors vers 1 pour toute paire).
- **Audit, 1−(1−p·s)^m :** valide seulement sous indépendance des étapes. Sous corruption corrélée la formule surestime la détection.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un signal planté faible, d'AUROC de Bayes connue (par exemple 0,70, *illustratif*), pour borner le sous-apprentissage. Le contrôle 1 de C ne calibre que les signaux forts.
- Un honnête à exclusion sévère **symétrique**, et un honnête sur des dossiers où les pièces pro-Y=1 sont réellement plus faibles (asymétrie légitime).
- Un LoRA bénin accompagné d'une consigne explicite de sabotage : la sonde doit rester ≥ 0,85 sur un modèle affiné.
- Le test honnête contre honnête entre domaines disjoints.
- Les lois de la NCD honnête contre honnête, et variante connue contre sa source.
- Des exécutions fraîches, non sélectionnées, avant tout réentraînement du Témoin 4.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le verdict est fonction de la couverture du catalogue.** Le profil vit dans [0,1]³ (trois interventions). Si le catalogue, avec ses compositions et ses plages de paramètres, recouvre cet espace à δ près, H_A est vraie par construction. S'il est maigre, c'est H_B. D prévoit un contrôle de sensibilité (retrait puis réintroduction), mais ne mesure pas la couverture.
2. **L'incompétence honnête n'est pas dans le catalogue.** Un biais réparti n'est réparé ni par une donnée restituée ni par un calcul certifié, donc son profil est plat. Le profil plat est aussi celui d'un modèle simplement faible. Le candidat « sort du catalogue » pour une raison sans rapport avec la nouveauté.
3. **Le duel d'explication est quasi vrai par construction.** Pour une dégradation assignée par consigne, celui qui annonce le « mécanisme supplémentaire » sait ce qu'il a prescrit. d_M ≤ δ teste alors l'obéissance du modèle à la consigne.
4. **min sur le catalogue de max sur les interventions.** Cet estimateur de d_C est biaisé vers le bas (minimum d'estimations bruitées), ce qui favorise H_A. La correction « tenant compte de toute la recherche » n'est pas spécifiée.
5. **Le duel de l'audit est vrai par construction.** Comparer un tirage uniforme avec vérificateur exact à la formule hypergéométrique teste le générateur aléatoire. D le reconnaît à moitié.
6. **Le contrôle « états permutés entre cas appariés » est ambigu.**
   - Si les paires sont (honnête, dégradé), la permutation échange les étiquettes.
   - Si elles sont de même classe, le gain subsiste trivialement.
7. **Aucun candidat n'est instancié pour le point 5.** D exclut par ailleurs la recherche adaptative, donc la « première expérience » n'a pas d'objet testable en l'état. De plus 500 jetons de sortie (*illustratif*) sur un modèle de 1,5 milliard de paramètres ne constituent pas une « longue tâche ».
8. **Le critère ne fait pas intervenir les surveillants.** C'est assumé, et c'est une indépendance utile vis-à-vis des détecteurs. La conséquence est qu'un candidat peut être « catégorie » au sens de D tout en étant détecté sans effort. Les verdicts de D ne sont pas commensurables avec ceux des autres propositions, et je ne les rapproche pas.

Je retiens de D, en le disant : la règle de ne pas retirer après coup les essais où la consigne n'a pas produit d'erreur, et la séparation entre « erreur présente » et « intention » pour l'audit.

### (b) Conditions de perte de puissance

- **d_C contre δ :** non jugeable quand la demi-largeur simultanée dépasse |d_C − δ|. Avec 200 dossiers, une fraction d'erreurs autour de 0,3 et une correction sur trois interventions et sur le catalogue, cette demi-largeur est du même ordre que δ = 10 points (*illustratif*). L'issue « ne tranche pas » serait la plus fréquente.
- **Effet plancher :** si le taux d'assertions fausses de l'honnête e₀ approche celui du candidat, toutes les composantes du profil se confondent.
- **Intention de traiter :** avec un taux d'obéissance c, TPR observé = c·TPR + (1−c)·FPR. Pour c petit, attendu sur un petit modèle, aucun instrument ne se qualifie.
- **Identifiabilité :** deux mécanismes dont les lois de réponse aux trois interventions coïncident sont indiscernables quel que soit n.
- **Duel de génération :** si la proportion de catalogues validés est proche de 0 dans les deux bras, l'intervalle sur g contient 0 pour tout effectif réaliste.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un modèle honnête faible (taille inférieure ou température élevée), apparié en gravité, soumis au test d'appartenance. Il ne doit pas sortir « catégorie ».
- Des profils aléatoires ou permutés soumis au catalogue, pour mesurer la fraction de [0,1]³ couverte à δ.
- Une prédiction de mécanisme faite par un tiers n'ayant vu que le candidat exécuté, pas la consigne.
- Un candidat connu rendu « réparti » (même mécanisme étalé sur plusieurs étapes), pour vérifier que l'étalement seul ne fait pas sortir du catalogue.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts.** Même défaut que C : de nombreux VÉRIFIÉ sans support dans FAITS, y compris sur des thèses. « La probabilité de capture vaut p » est une identité de calcul, pas un fait vérifié.
2. **Chronologie interne.** E cite l'intégrité du flot de contrôle (Abadi et al., 2005, de mémoire) comme « nouveau capteur imposé » par la programmation orientée retour (2007). Selon ces mêmes dates, à vérifier, la défense précède l'attaque. L'exemple ne soutient donc pas la lecture « catégorie = défense à inventer ».
3. **Le Régime III est l'acceptation d'une hypothèse nulle.** « sup TPR ≤ α + ε » exige une borne supérieure de confiance sur un sup, alors que l'optimiseur n'en fournit qu'une borne inférieure. E traite la zone intermédiaire (doublement de N) mais pas la zone basse, où le sous-apprentissage compte le plus.
4. **Φ_aud dans le vecteur d'observation crée un plancher mécanique.**
   - Avec p = 0,10 et un oracle à 0,90, le TPR après réentraînement vaut au moins environ 0,09 + 0,91 × 0,05 ≈ 0,135 (calcul sur les chiffres *illustratifs* de E).
   - Le seuil bas est à 0,15. Le Régime III tient dans 1,5 point, inséparable avec 200 épisodes de test.
5. **La condition d'entrée sélectionne sur θ₀** (TPR ≤ 0,15) avec les honnêtes qui servent ensuite à l'évaluation. Il y a régression vers la moyenne.
6. **Φ_sym est conçu en connaissant le candidat** (biais unidirectionnel sur les cas limites). C'est en revanche un vrai capteur nouveau, puisqu'il demande une réexécution contrefactuelle, mais son succès reste attendu par construction.
7. **E2 confond deux échecs.** L'échec en transfert de θ_comp peut venir de la généralisation compositionnelle du classifieur ou de l'irréductibilité de l'attaque. Le contrôle A_u⊕A_v ne valide que l'ordre 2 retenu. Le verdict dépend aussi du catalogue de six primitives et des poids du mélange d'entraînement.
8. **E3 mesure la recherche d'un angle mort planté.**
   - L'espace d'hypothèses (quelle variable manque) est énumérable. Si le budget de 200 exécutions dépasse le nombre de variables d'état, p_S tend vers 1 par énumération et p_G − p_S vers 0 par plafond.
   - Le rôle « générateur d'hypothèses hors-Φ » donne la structure de la solution.
   - Le témoin mécanique d'énumération ou de mutation manque. Le tirage solo n'est pas l'hypothèse nulle de « seulement des variantes ».
   - Le test à zéro exécution contrôle l'instance. Il ne contrôle pas le schéma « un moniteur omet une variable », présent dans tout corpus.
9. **Seuils de E3 incompatibles.** À 30 environnements, 8/30 contre 3/30 (minimum compatible avec p_G ≥ 0,25 et un écart ≥ 0,15) donne un p de l'ordre de 0,1 à 0,2, loin de 0,01 (*illustratif*). Les environnements étant appariés, Fisher n'est pas le bon test (McNemar le serait).
10. **Audit.** « Conforme ou supérieure à 1−(1−p)^K » : la borne ne peut pas être dépassée sous tirage uniforme et oracle exact.

Je retiens de E, en le disant : la permutation honnête contre honnête et le LoRA bénin dans la calibration. Ce dernier doit être repris explicitement dans E1, où P_hon n'est pas précisé.

### (b) Conditions de perte de puissance

- **TPR(θ\*) au seuil bas :** non jugeable quand ε est inférieur au plancher p·s_oracle − α ajouté à 2·ET. Il l'est aussi quand le (1−α)-quantile honnête repose sur n_h·α ≈ 10 cas (*illustratif*).
- **Régime III :** équivaut à TV(P_c, P_h) ≤ ε sur 𝓗. Il n'est estimable que si la complexité de Θ rapportée à n permet de borner l'écart entre le sup empirique et le sup vrai.
- **θ_comp :** la puissance s'effondre sous décalage de proportions entre le mélange synthétique et P_cand, ou si l'ordre de composition du candidat dépasse l'ordre entraîné.
- **E3 :** non jugeable sous plafond (p_S → 1) ou sous plancher (p_G, p_S → 0).
- **Audit par sous-dossiers (m = 2 sur 20) :** si la loi de l'erreur unitaire du candidat est contenue dans celle de l'honnête, la détection unitaire vaut α et seule une statistique agrégée sur les épisodes a de la puissance.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un énumérateur mécanique de variables et de mutations dans E3, à budget égal.
- Un signal planté faible dans Φ, de TPR de Bayes connu, pour E1.
- Un honnête légitimement asymétrique pour Φ_sym : des dossiers où l'inversion de polarité change réellement la décision correcte.
- Un assemblage d'ordre élevé (4 ou plus) de primitives connues pour E2. Il doit être classé « assemblage ».
- Une réestimation du contournement de θ₀ sur des honnêtes frais.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **LoRA sans LoRA honnête.** Le prompt est identique entre honnête et saboteur, mais les poids diffèrent. Le tableau prévoit six adaptateurs saboteurs et aucun adaptateur honnête. Toute sonde peut lire « poids affinés », et le transfert de K vers a\* serait alors élevé par construction, classant tout candidat en « variante ».
2. **Un adaptateur par famille.** La variance entre graines d'affinage est confondue avec la différence entre familles. La matrice de transfert « intra-famille élevée » compare des tirages d'un même adaptateur, pas des variantes.
3. **β = 20 n'est pas applicable au juge.** Vingt trajectoires de 4 000 à 8 000 jetons ne tiennent pas en contexte comme exemples. La non-absorption est mécanique pour cet instrument.
4. **S⁺ est déjà dans S.** La « cohérence différentielle contre un agent témoin indépendant » de l'Expérience 2 est, à l'échantillonnage près, le « contrôle différentiel mécanique » que F place en §4.3 parmi les bases à battre par l'audit. La frontière S/S⁺ se réduit alors au taux p. C'est un paramètre, pas un invariant nouveau.
5. **Le plateau est inféré de trois points** (n = 20, 100, 500), sans estimation de pente.
6. **« Échec de tout canal réaliste S⁺ »** est une quantification universelle. Le choix de S⁺ après observation de a\* reste un degré de liberté non borné.
7. **Expérience 3 : le critère 1 est vrai par sélection.** Les générateurs reçoivent la spécification complète de S_r et un retour du banc, donc l'échec en transfert sans exemple est acquis. Seuls les critères 2 et 3 informent, et ils sont évalués sur les mêmes cas honnêtes.
8. **Seuil « ≥ 2/5 contre 0/5 ».** Le test de Fisher donne p ≈ 0,22 en unilatéral. À taux commun de 0,2, cette configuration survient dans environ 9 % des cas (*illustratif*). Le sort des verdicts « non conclusifs » dans N_cat n'est pas défini.
9. **Environnements isomorphes permutés.** Ils neutralisent le rappel lexical et préservent la structure. Ils ne distinguent pas l'invention du rappel structurel.
10. **Référence.** F cite Greenblatt et al. sous le titre « …Regardless of Scheming », alors que B, C et E donnent « …Despite Intentional Subversion ». Une des deux attributions au moins est fausse. Ma mémoire penche pour la seconde : référence à vérifier.

Je retiens de F, en le disant : l'assemblage aléatoire a_comp, l'environnement « scellé », et l'appariement des honnêtes sur le taux d'erreur.

### (b) Conditions de perte de puissance

- **TPR_adapt à β = 20 :** pour un apprenant de dimension d, l'erreur d'estimation est d'ordre √(d/β). Le TPR reste proche de α pour tout candidat dès que d ≫ 20, indépendamment de TV(P_c, P_h).
- **Plateau :** non jugeable si l'intervalle sur la pente d TPR / d log n entre 100 et 500 exclut 0, car la courbe monte encore. Il l'est aussi si ET(TPR_S(500)) dépasse l'écart entre 0,55 et 0,80 divisé par 4.
- **ΔTPR_K ≥ −0,05 :** non jugeable si l'effectif de test de K donne une erreur type supérieure à 0,025.
- **Écart TPR_{S⁺}(100) − TPR_S(500) :** si S⁺ et S ne diffèrent que par p, l'écart est une fonction déterministe de p et de la sensibilité d'audit.
- **Audit :** la borne 1−(1−p·s)^k suppose l'indépendance des k items. Sous corrélation positive des items sabotés, l'« écart négatif » apparaît sans tromperie de l'auditeur.
- **N_cat sur R = 5 :** la loi binomiale à 5 essais ne sépare pas des taux de 0 et de 0,3 avec un risque acceptable.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un adaptateur honnête (mêmes rang, volume et tâches), plus deux graines au moins par famille. Le transfert entre graines d'une même famille sert de plafond, le transfert d'un honnête-LoRA vers un autre de plancher.
- Un S⁺ factice : canal ajouté sans information, qui ne doit jamais valider le critère 3.
- Le même S à un taux p augmenté. S'il rattrape S⁺, il n'y a pas d'invariant nouveau.
- Un assemblage **choisi adversairement** parmi C₁–C₃, optimisé contre S_K, en complément de a_comp qui est aléatoire.
- Des honnêtes frais et des graines fraîches pour toute évaluation de candidats issus de la boucle de l'Expérience 3.

---

## Ce qui me ferait réviser ces critiques

- Sur les fuites de construction (B, C, E) : la preuve que l'observable étendu a été figé, avec empreinte, avant la définition du candidat.
- Sur les empreintes d'affinage (B, F) : un transfert honnête-LoRA contre honnête-base au niveau du hasard.
- Sur les seuils : des intervalles calculés montrant que les effectifs annoncés séparent les deux bornes de chaque duel.

FIN-DE-CELLULE