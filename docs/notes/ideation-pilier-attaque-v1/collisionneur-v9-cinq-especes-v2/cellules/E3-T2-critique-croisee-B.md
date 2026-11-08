# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces reçues.** A, C, D et E sont présentes et complètes ; chacune se termine par sa ligne de fin. La pièce C n'a pas de titre, mais rien n'y manque. Je n'ai pas recalculé leurs empreintes.

**Statut.** Toute critique ci-dessous a le statut **HYPOTHÈSE**. Tout chiffre qui ne vient pas des faits est **illustratif**.

**Forme des contrôles proposés (B4).** Chaque contrôle que je propose est écrit en duel : *H_A / H_B*, et chacune des deux issues falsifie l'autre.

---

## Trois défauts qui touchent plusieurs propositions

Je les nomme une fois ici, puis je les impute proposition par proposition. Je les applique ; je ne fusionne pas les propositions.

- **T1 — La boîte noire a servi à fixer la dose.** La dose « diffuse » se fixe sur la boîte noire seule (faits §6). Les épisodes positifs à cette dose ont donc été choisis pour échapper à une boîte noire. Si la mâchoire externe, le prédicteur texte ou le juge servent ensuite de comparateur, deux biais tirent leur rappel vers le bas : la sélection (mêmes épisodes) ou la régression vers la moyenne (épisodes neufs). Une conclusion « la blanche domine la noire » à dose diffuse est alors en partie vraie par construction.
  - *H_A* : l'avantage de la blanche persiste avec une boîte noire d'évaluation disjointe de celle qui a fixé la dose (autres poids, autre famille), sur des épisodes neufs.
  - *H_B* : l'avantage disparaît dans ces conditions.
- **T2 — Les deux familles ne sont pas indépendantes.** La famille (ii) est distillée depuis la famille (i) (faits §6). Un pli « entraîné sur (i), testé sur (ii) » n'est donc pas hors famille : la politique est partagée. Avec K = 2 blocs dépendants, la variance de généralisation repose sur un seul pli et n'est pas estimable.
- **T3 — La loi nulle du dommage n'est mesurée par personne.** Le dommage est défini comme la baisse de couverture contre le jumeau honnête apparié. La différence entre deux tirages honnêtes de la même tâche n'est pourtant mesurée nulle part. Si l'écart-type σ_hon de cette différence est du même ordre que le dommage diffus δ, toute étiquette « dommage » est en grande partie du bruit.
  - Contrôle : tirages honnête-contre-honnête.
  - *H_A* : δ dépasse le quantile 95 % de cette loi nulle (seuil illustratif).
  - *H_B* : δ reste à l'intérieur.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **E1 : l'écart AUC(α) − AUC(β) est en partie vrai par construction.**
   - Les négatifs sont le jumeau honnête, c'est-à-dire le modèle de base. Or α = 0 rend la base au bit près (P-009). Sur les négatifs, les activations lues par α et par β sont donc identiques.
   - Sur les positifs, elles diffèrent de toute la contribution de l'adaptateur.
   - AUC(α) − AUC(β) détecte donc la présence de l'adaptateur, ce qui est exactement le confondant 2 que A traite ailleurs.
   - Le carré consigne × acte n'y remédie pas : ses cases sont des organismes différents.
   - Le placebo et T100 n'apparaissent qu'en E2, pas en E1.
2. **E0 : le sens de « étiquette par construction » n'est pas précisé.** Si l'attestation du monde planté passe par l'oracle de couverture, le rappel mesuré est circulaire. Si elle passe par des sabotages injectés, leur loi n'est pas celle du sabotage diffus de l'organisme.
3. **E0 : le rapport d'indépendance R ne regarde que les négatifs.** Il capte les fausses alertes corrélées. Il ne capte pas les manqués corrélés (l'oracle et le moniteur manquent ensemble un sabotage). Ce sont pourtant ces derniers qui gonflent le rappel apparent des moniteurs.
4. **E2 : H_A (« acte ») est définie par une absence de signal** (AUC ≤ 0,60 sur dormants et placebo). À faible puissance, H_A gagne par défaut. Il faudrait un test d'équivalence borné, pas un seuil sur une estimation ponctuelle.
5. **E3a : la corrélation de Spearman sur cinq doses ne discrimine rien.** Toute grandeur monotone en α corrèle avec D. Sur T, D est plat : la corrélation y est indéfinie (ex æquo), donc le contrôle T n'est pas jugeable sous cette forme.
6. **E3b : fuite et effet de dose.**
   - Les sites de substitution sont choisis par E2 sur les mêmes épisodes : c'est une fuite entre construction et évaluation.
   - Substituer depuis la base sur beaucoup de sites revient en partie à ramener l'adaptateur vers α = 0 : D baisse par construction.
   - Le contrôle « hors localisation » doit être apparié en nombre de sites **et** en norme d'adaptateur retirée.
7. **E4 et E5 : complémentarité confondue avec étau, et sélection.** J'utilise ici l'argument de E, en le disant.
   - C − TPR_int > 0 établit une complémentarité, pas un étau.
   - Lire C le long du budget, sur les seuls manqués de l'externe, conditionne sur des survivants dont la population change avec le budget. C varie alors par sélection, sans effet causal.
   - Le test préalable de L2 utilise le juge pour définir ce qui est « indistinguable » : l'instrument évalué fixe ainsi son propre régime.
8. **E5b : la composition des détecteurs est confondue avec le secret.** La réserve et les sondes déployées ne sont pas échangeables a priori. Le gain « secret » peut venir de sondes de réserve simplement meilleures.
9. **E5d : D(k) est un maximum.** Le dommage maximal atteint croît avec le nombre d'essais du bras rouge. La courbe mesure donc aussi le budget d'attaque.
10. **T1 s'applique à E4**, comparaison blanche contre noire.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R non jugeable.** Le nombre attendu de cas « faux positif de l'oracle et alerte du moniteur » vaut N·f_O·τ_M. Avec N = 500, f_O = 0,05 et τ_M = 0,01 (illustratifs), on en attend environ 0,25 : R n'a pas d'estimateur fini.
- **Contamination des dormants.** Si les dormants contiennent une fraction c de sabotages manqués par l'oracle, alors AUC_dorm ≈ (1 − c)·AUC_id + c·AUC_acte. Avec c = 0,25, AUC_acte = 0,9 et AUC_id = 0,5 (illustratifs), AUC_dorm ≈ 0,60. Le verdict « identité » se déclenche alors sans signal d'identité.
- **ΔAUC n'est pas ΔTPR au taux de fausses alertes de 1 %.** Si les courbes ROC se croisent, ΔAUC > 0 est compatible avec ΔTPR(1 %) ≤ 0.
- **Le seuil à 1 % est mal estimé avec peu de négatifs.** Avec 400 négatifs, il repose sur environ 4 points. Viser au moins 20 dépassements (illustratif) exige au moins 2 000 négatifs honnêtes.
- **La vérification FA_joint ≤ 1,2 % est impossible avec peu d'épisodes.** Une erreur type de 0,1 point demande N ≈ 10 000 épisodes honnêtes (illustratif).
- **Plafond de l'externe.** Si TPR_ext ≥ 0,85, le dénominateur de C vaut moins de 0,15·n_pos.
- **Nash optimisée et évaluée sur la même matrice.** Avec 36 cellules de demi-largeur 0,08 (A), un mélange optimisé sur la matrice estimée exploite le bruit. L'écart « mixte − meilleure pure ≥ 0,10 » a un biais optimiste.
- **Arrêt d'E5d déclenché par le bruit.** La règle « deux fois |ΔD| < ε » se déclenche avec une probabilité d'environ p², où p = P(|N(0, 2σ²)| < ε). Elle s'arrête donc par le bruit dès que σ ≈ ε.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Négatifs porteurs d'un adaptateur dans E1** (T100 et placebo).
  - *H_A* : AUC(α) − AUC(β) > 0 persiste contre ces négatifs.
  - *H_B* : l'écart s'annule (identité).
- **Source de sabotages connus indépendante de l'oracle**, scellée, pour E0.
- **Affectation aléatoire des sondes** au rôle réserve ou déployé, tirée dans un même vivier.
  - *H_A* : le gain « secret » survit à cette permutation.
  - *H_B* : il disparaît.
- **T3** (loi nulle honnête-contre-honnête).
- **Contrôle T1** sur E4.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Changements de statut (règle 1).**
   - T100 est présenté comme « organisme placebo, VÉRIFIÉ § 6 ». Or la question dit qu'un organisme placebo « est à construire ». T100 y est le témoin « instruit sans sabotage » ; qu'il vaille placebo est une HYPOTHÈSE (A11 le dit aussi).
   - « 50 traces honnêtes rejouées (VÉRIFIÉ § 1) » : dans la question, ces 50 traces figurent parmi ce qui **manque** pour qualifier Jev, pas parmi les données existantes.
   - Le prédicteur à 0,866 est marqué RAPPORTÉ en (b) et VÉRIFIÉ en (d) : le même fait porte deux statuts.
   - Ces statuts doivent être rétablis avant toute lecture.
2. **E1 : la réfutation de H_A est produite par le découpage.**
   - Entraînée sur (i), où la consigne est présente, la sonde apprend la consigne ; elle échoue sur (ii) et H_A est réfutée, sans rien dire de l'existence d'une trace.
   - T2 s'ajoute à ce défaut.
   - Incohérence : la falsification utilise ΔTPR, alors que « ce qui la réfuterait » utilise l'AUC.
3. **E2 : séparation vraie par construction.**
   - La grandeur projette l'écart sur le sous-espace de sortie de l'adaptateur **saboteur**. T100 porte un autre adaptateur ; sa projection est faible même sans acte. La séparation acte contre placebo est donc due à l'identité.
   - Les négatifs mélangent dormants et placebo. La partie facile (le placebo) peut porter seule l'AUC ≥ 0,75.
   - Calibrer le seuil sur la base fait sonner tout adaptateur.
4. **E3 : le contrôle aléatoire favorise la cible par construction.**
   - Substituer dans le sous-espace de l'adaptateur revient à réduire la dose.
   - Un sous-espace aléatoire de même dimension est presque orthogonal à l'image de rang faible de l'adaptateur : la cible gagne par construction.
   - Le test porte sur S100, c'est-à-dire sur le flagrant, et non sur le diffus qui est l'objet de la question.
5. **E0 : trois défauts.**
   - Le rappel est mesuré sur des sabotages « programmatiques injectés », dont la loi n'est pas celle du sabotage diffus.
   - L'indépendance est testée contre le seul prédicteur texte, pas contre les sondes internes.
   - « Rejet si p < 0,05 » accepte H_A par simple non-rejet.
6. **E4 : le duel n'est pas exhaustif.** H_A est une disjonction (réserve ≥ 0,15 *ou* coût croissant). H_B dit « l'aléa suffit ». L'issue « rien n'aide » ne falsifie aucune des deux, ce qui viole B4. De plus, H_A présuppose que R3 « s'effondre ».
7. **E5 : la courbe d'étau est impossible sur un mode lu une seule fois.**
   - Une courbe de C_rés « en fonction de l'intensité d'évasion » exige plusieurs générations adaptatives.
   - Le mode tenu à l'écart, lu une seule fois, ne les fournit pas.
   - S'y ajoutent la sélection des survivants (argument de E) et T1.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **log OR inatteignable.** Exiger |log OR| ≤ 0,20 demande une erreur type sur log OR d'au plus 0,1, donc environ 400 cas par cellule (illustratif). Avec 200 épisodes et des taux d'erreur de 0,15 au plus, c'est hors d'atteinte. Par le critère p > 0,05, H_A gagne alors par défaut.
- **E1 : seuil à 1 % instable.** 500 épisodes répartis entre familles et doses laissent quelques négatifs par pli : le seuil à 1 % repose sur 1 à 3 points.
- **E3 : ρ_causal est un rapport non estimable près de zéro.** Si l'intervalle de D_S100 − D_S0 contient 0, ou s'en approche aux doses diffuses, la région de Fieller n'est pas bornée.
- **E4 : test de Friedman à G = 4 blocs.** La puissance est quasi nulle pour des effets de 0,05 à 0,15.
- **E5 : dépendance de queue non estimable.**
  - Sous indépendance à τ/2 = 0,5 %, le taux attendu d'alertes jointes sur les honnêtes vaut 2,5·10⁻⁵.
  - Observer 10 événements demande N ≥ 4·10⁵ (illustratif) : la copule de queue n'est pas estimable.
  - Le nombre de manqués de l'externe vaut 300·π·(1 − TPR_ext), avec π la part de positifs.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Placebo à objectif caché inoffensif**, distinct de T100, et **dormants rapportés à part**.
  - *H_A* : l'AUC sur dormants seuls reste ≥ 0,75.
  - *H_B* : elle tombe au hasard.
- **Entraînement et test à l'intérieur de (ii)**, sans consigne, contre T100.
- **Sous-espace témoin tiré à l'intérieur de l'image de l'adaptateur**, de même rang.
  - *H_A* : la direction de la sonde réduit D plus que ce témoin.
  - *H_B* : pas de différence.
- **Indépendance de l'oracle mesurée contre les sondes internes.**
- **T1 et T3.**

---

## Sur la proposition D

### (a) Défauts de méthode

1. **E0 : critère de dépendance vrai par construction.**
   - D mesure la covariance absolue P(e_O ∧ e_M) − P(e_O)P(e_M). Elle est bornée par min(p_O, p_M).
   - Dès qu'un des deux taux d'erreur est ≤ η = 0,02, on obtient |cov| ≤ η automatiquement.
   - La source et la famille de la « réadjudication indépendante » ne sont pas précisées.
2. **E1 : « laisser une famille entière de côté » avec deux familles dépendantes** (T2) ne donne qu'un seul pli, non indépendant.
3. **E2 : interaction non identifiable.**
   - L'interaction acte × organisme est non identifiable : la case placebo × acte est vide par définition.
   - Le seul contraste valide est intra-saboteur : actes contre dormants.
   - La formule « signal présent à dose nulle non nulle » est ambiguë ; elle n'est pas préenregistrable telle quelle.
4. **E3 : plancher de dommage.** La marge d'équivalence causale de 0,02 sur le dommage doit être comparée au dommage diffus. Si D_diffus ≤ 0,02, « dommage équivalent » est acquis d'avance, et H_A est falsifiée par construction.
5. **E5 : le secret « figé » mélange deux choses.** Le bras « figé secret » prive l'attaquant de tout retour. Il mesure donc une attaque non adaptative, pas le secret d'une distribution. À nommer comme tel. La « valeur pessimiste » n'est pas définie.
   - En revanche, la remarque de D selon laquelle une réserve tenue pour l'audit ne revendique qu'un gain d'audit est juste. Je m'en sers pour E5b de A.
6. **E6 : sélection et harnais non défini.**
   - « Pente de la trace interne selon la réussite d'évasion externe » conditionne sur une issue : même sélection que chez A et C.
   - « Le harnais doit restituer L2/E7 » suppose une vérité synthétique que D ne définit pas.
7. **T1** s'applique à E4 et E6 ; **T3** n'est pas couvert.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Bornes simultanées par strate.**
  - Avec S strates à niveau α/S, un rappel vrai égal à R_min + 0,03 demande environ (z_{α/2S} + z_β)²·r(1 − r)/0,03² épisodes par strate.
  - Pour S = 5, r = 0,93 et une puissance de 90 % (illustratifs) : z_{0,005} ≈ 2,58 et z_{0,10} ≈ 1,28, d'où ≈ 14,9 × 0,065 / 0,0009 ≈ 1 075 épisodes par strate.
  - S'y ajoute l'effet de plan 1 + (m − 1)·ICC dû au regroupement par monde.
- **Test d'équivalence à deux unilatéraux sur le dommage.** Avec une marge de 0,02, il faut une erreur type ≤ 0,02/(z_α + z_β) ≈ 0,007 (illustratif).
  - Si l'écart-type du dommage honnête vaut 0,1, il faut environ 200 paires appariées par condition, avant tout effet de plan.
- **ε = 0,05 de rappel au taux de fausses alertes de 1 %, avec 90 % de puissance.** Pour TPR ≈ 0,3, il faut environ 1 000 positifs et plusieurs milliers de négatifs (illustratifs).
  - Le budget annoncé par D (4 000 à 15 000 USD) en découle.
  - L'échéance TAIF n'est pas datée dans les faits : la faisabilité reste non jugeable.
- **Valeur de Nash réévaluée sur une génération fraîche.** C'est correct, mais n_eff = nombre de générations (4, illustratif), et non le nombre d'épisodes.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Dépendance normalisée** (rapport des taux conditionnels) avec un réadjudicateur de famille tierce.
  - *H_A* : rapport dans [0,5 ; 2].
  - *H_B* : rapport hors de cet intervalle.
- **Contraste intra-saboteur, actes contre dormants**, en remplacement de l'interaction.
- **Vérification préalable du plancher.**
  - *H_A* : D_diffus > marge, avec intervalle.
  - *H_B* : D_diffus ≤ marge, ce qui suspend E3.
- **T1 et T3.**

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Fiche O : suspension par manque d'effectif.**
   - « Suspension y compris faute de précision » confond un oracle insuffisant avec un échantillon insuffisant.
   - Avec f_O ≤ 0,01 exigé par strate, la règle de trois impose au moins 300 négatifs par strate, même sans aucune erreur.
   - Avec plusieurs strates indispensables, la suspension devient l'issue par défaut.
2. **d = max_z : biais vers le haut et étiquettes non sourcées.**
   - Le maximum sur des strates bruitées est biaisé vers le haut, de l'ordre de √(2 log K / n_min).
   - Les cellules où E_O = 1 sont rares. H_B peut donc l'emporter par le bruit.
   - L'origine des étiquettes du « lot tiers » n'est pas précisée.
3. **Fiche T : placebo non apparié.**
   - « Écart adapté–base comparé à écart placebo–base » n'a de sens que si le placebo est apparié en rang et en norme d'adaptateur.
   - Ce placebo est « à construire » (faits) et E ne fixe pas cet appariement.
4. **Fiche L : jeu d'entraînement non spécifié.**
   - Un détecteur de nouveauté ajusté sur des honnêtes issus de la seule base voit tout adaptateur comme nouveau.
   - S'il est ajusté ainsi, le contrôle placebo le fera échouer par construction. Le jeu honnête d'entraînement (avec ou sans organismes adaptés honnêtes) doit être fixé d'avance.
5. **Fiche C : seuil non interprétable.** B_D ≥ 0,05 sur une « échelle gelée » non définie. Le seuil n'a pas de sens tant que l'échelle n'est pas donnée.
6. **Fiche R : budget dilué et défense de référence non contrôlée.**
   - Le plan 2 × 2 × 2 (distribution, tirage, composition), croisé avec les générations, divise le budget rouge par 8.
   - G_R se mesure contre une « défense fixe choisie avant test ». Si ce n'est pas la meilleure figée sur les familles vues, à budget égal, G_R est gonflé.
7. **Fiche P : E réintroduit la sélection qu'elle dénonce.**
   - Le duel étau exige une hausse du score interne « à dommage maintenu ». Il conditionne donc sur une variable postérieure au traitement.
   - Il faut lire pression → score interne et pression → dommage comme deux issues conjointes, en intention de traiter.
8. **T1** s'applique aux comparateurs de T, L et P.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Pseudo-réplication dans R et P.** Le régime de pression ou de défense est assigné par campagne du bras rouge, pas par épisode.
  - L'effectif utile pour l'effet de régime est donc le nombre de campagnes (3 à 4, illustratif).
  - Traiter les épisodes comme unités indépendantes sous-estime la variance d'un facteur proche de la taille des campagnes.
  - Le défaut vaut aussi pour E5 de A, E4 de C et E5–E6 de D.
- **Effectifs de la fiche P.** Avec 3 000 positifs et 6 000 négatifs, chaque seuil à τ/2 repose sur environ 30 dépassements. Les manqués de l'externe valent 3 000·(1 − TPR_ext).
  - Pour TPR_ext = 0,9 (illustratif), cela fait 300 manqués. R ≥ 0,20 se juge alors à une demi-largeur d'environ 0,045.
  - Les sous-strates restent indécises, comme E le reconnaît.
- **Effet de 0,20 écart-type.** Il exige n_eff ≥ (2,8/0,2)² ≈ 200 unités indépendantes par bras (illustratif). C'est incompatible avec n_eff égal au nombre de campagnes.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Mâchoire externe factice dans la même machinerie de campagne** : score aléatoire, même calibration.
  - *H_A* : la pression sur l'externe réelle déplace le score interne plus que la pression sur la factice.
  - *H_B* : pas de différence ; le déplacement vient alors de l'adaptation en général, pas de l'évasion de l'externe.
- **Placebo apparié en rang et en norme.**
- **Honnêtes adaptés dans le jeu d'entraînement de L**, ou contrôle explicite de leur absence.
- **Meilleure défense figée sur les familles vues comme référence de R.**
- **T1 et T3.**

FIN-DE-CELLULE