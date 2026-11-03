# Proposition D — Tour III.3 : réponse aux critiques

Les publications restent **RAPPORTÉES** par les pièces ; les résultats des dépôts de Lazar restent **OBSERVÉS-NON-AUDITÉS**. Les objections ci-dessous sont traitées comme des **HYPOTHÈSES méthodologiques**, non comme des résultats. Sauf mention « calcul », tous les nouveaux seuils, effectifs et coûts sont **illustratifs** ; les attentes expérimentales sont **supposées**.

## (a) Réponses aux critiques

### Critiques de A visant D

1. **A(a)1 — Verdict sur estimateur ponctuel : acceptée.** J’ajoute des intervalles et un verdict **indécis**. Les hypothèses restent complémentaires dans l’espace des paramètres, mais des données limitées peuvent ne pas permettre de choisir.
2. **A(a)2 / Σ1 — Persistance favorisée par KL ou adaptation limitée : acceptée.** Je déclare la paramétrisation, la référence KL et deux doses dont \(\beta=0\). Surtout, je mesure le déplacement de politique atteint : une absence de déplacement rend le test non probant, plutôt que favorable à la persistance.
3. **A(a)3 — Pas de post-entraînement non-RL : acceptée.** J’ajoute un SFT neutre apparié sur la divergence atteinte. Sans ce bras, on ne peut pas attribuer une érosion spécifiquement au RL.
4. **A(a)4 — Soustraction de construits et d’instruments différents : acceptée, transformée en test.** E2 utilise désormais un événement binaire commun de capitulation et isole d’abord l’effet « source utilisateur » dans chaque domaine. Les matrices de confusion par domaine et checkpoint bornent l’atténuation résiduelle.
5. **A(a)5 — Attente \(\Delta S=+12\) insuffisamment fondée : acceptée.** Je la retire. L’attendu devient une interaction sociale–factuelle de **0 point**, avec deux effets génériques de **+2 points**. La puissance sera calculée sur pilote, pas sur l’espoir d’un grand effet.
6. **A(a)6 — « Ton constant » non garanti après RL : acceptée.** Les sorties naturelles deviennent principales. Une normalisation de style, validée séparément pour conserver la position, ne servira qu’en sensibilité.
7. **A(a)7 — Seuil de gain sous la résolution et paramètres par item non identifiables : acceptée.** La marge passe à \(0{,}10\), le volume est conditionné à la précision, et \(g,c\) sont estimés hiérarchiquement entre items, non librement dans chaque item.
8. **A(a)8 — Transfert abusif de S3 : acceptée.** Je retire toute conclusion sur R8/Tülu 3. E3 ne teste qu’une invariance locale dans la chaîne OCT étudiée.
9. **A(a)9 — Fuite de validation et « étiquettes permutées » mal définies : acceptée.** Développement et test sont séparés par items, générateurs et checkpoints. Je retire cette permutation pour un juge à consigne ; les permutations ne concernent que des traitements échangeables par blocs.
10. **A(a)10 — Stratification sur les refus : acceptée.** L’analyse principale inclut tous les items, avec refus explicite et bornes d’incertitude ; l’analyse conditionnelle devient secondaire.
11. **A(a)11 / Σ3 — Dérive temporelle du juge : acceptée.** Sorties avant/après renotées dans une même passe interfoliée, version figée, jeu d’ancrage et test-retest d’un checkpoint gelé.

**A(b).** J’accepte les conditions de non-jugeabilité : ratio instable, variance entre entraînements, atténuation différentielle, dispersion insuffisante de \(v_0\), saturation et refus différentiels. Le ratio n’est plus principal ; le nombre d’entraînements augmente si leur variance domine. Les volumes d’environ **3 000 items par cellule** pour E2 et de multiplication du volume pour E3 sont seulement des **calculs illustratifs**, dépendant des hypothèses d’indépendance et de variance d’A.

**A(c).** J’ajoute les bras KL/non-RL, la source impersonnelle, le partage tenu à l’écart et la renotation interfoliée. Je conserve les contrôles déjà présents en E3 : dose nulle, doses permutées et concurrent à déplacement constant.

### Critiques de B visant D

1. **B(a)1 — Inférence ponctuelle : acceptée**, déjà corrigée.
2. **B(a)2 — Instrument de \(C\) non nommé : acceptée.** La mesure principale sera un critère comportemental adjudiqué humainement, assisté d’un juge validé hors développement. Le classifieur OCT devient secondaire, compte tenu de sa circularité déclarée (**RAPPORTÉ**, pièce Ibrahim §2).
3. **B(a)3 — Récompense permutée non appariée en déplacement : acceptée pour l’attribution causale.** Si la divergence ne peut être appariée, ce bras reste un contrôle d’exposition, pas une estimation de l’effet propre de l’optimisation.
4. **B(a)4 — Attentes E1/E2 incompatibles : rejetée dans sa forme forte.** Une persona peut persister comme style ou disposition tandis que son expression sycophantique change. J’accepte néanmoins le défaut de mécanisme et d’attente motivée : l’attendu amplificateur de \(+12\) est supprimé.
5. **B(a)5 — Échelles S/F : acceptée**, avec le même point de mesure comportemental et des analyses de sensibilité aux fiabilités.
6. **B(a)6 — Ton constant « impossible » : rejeté comme affirmation absolue, accepté comme objection pratique.** Une consigne ou une réécriture peut intervenir sur le ton, mais ne garantit ni le ton naturel ni la conservation du sens ; elle ne sera donc pas l’analyse principale.
7. **B(a)7 — Duel E3 asymétrique : acceptée.** La précision doit permettre aussi bien une conclusion d’équivalence qu’une conclusion de modification, sinon E3 est différée.
8. **B(a)8 — Seuils de validation non établis à \(n=200\) : acceptée.** Les 200 cas servent au développement. Le test indépendant est dimensionné pour que la borne inférieure de détection dépasse 80 % et la borne supérieure de fausses alertes reste sous 5 %, seuils illustratifs.
9. **B(a)9 — Circularité des contrastes synthétiques : acceptée.** Le test comprend des sorties réelles post-RL et des générateurs absents du développement. *Sycophantic* n’est un contrôle positif qu’après adjudication comportementale indépendante, jamais par définition.

**B(b/c).** J’accepte les contrôles Fieller si un ratio secondaire est rapporté, les seuils de saturation, la fiabilité à mesurer, la croyance utilisateur correcte, la dose nulle avec \(v_0\) sur tirages disjoints et le test-retest. Le volume « environ 24 000 générations » est un **calcul illustratif** fondé sur une variance analogue à R6, non une garantie.

### Critiques de E visant D

- **Règle d’inférence et région non concluante : acceptées.**
- **Maintien absolu contre maintien relatif : acceptée.** E1 publie les niveaux persona et base séparément et exige le maintien absolu de la persona, pas seulement celui de l’écart.
- **Commensurabilité, saturation, atténuation et identification de \(g,c\) : acceptées.** Elles deviennent des critères explicites de non-jugeabilité.
- **Contrôles synthétiques favorisant leur instrument : acceptée.** Aucun générateur de développement ne sert au test final.
- **Permutations : acceptée.** Elles respecteront les blocs et la dépendance ; leur calibration sera testée sous des nulles simulées.
- **Extraction factuelle : acceptée.** Formats sémantiquement équivalents et vérité de référence indépendante du parseur sont ajoutés.

## (b) Expériences corrigées

### Verrou instrumental commun

Deux annotateurs au moins, aveugles au checkpoint et au moment, notent des lots mélangés ; leur accord est rapporté sans transférer les ICC d’experts de la taxonomie. Développement et test sont disjoints. Les faux positifs portent sur des sorties sans le construit : style modifié à position constante, puis position modifiée à style constant. Le juge principal doit être figé ; sinon, il ne peut produire le verdict. Un échec du verrou arrête l’interprétation.

### E1 — Persistance absolue et relative après RLVR

**Entraînement.** Sous réserve d’accès réel : Llama-3.1-8B-Instruct de base et checkpoint OCT *Loving*. RLVR plein-paramétrique, sur tâches vérifiables disjointes des évaluations ; \(\beta=0\) et \(\beta>0\) fixé d’avance, référence KL égale au checkpoint de départ. Bras sans mise à jour, SFT neutre et récompense permutée. Les comparaisons causales sont appariées sur la KL mesurée sur prompts témoins, non sur les pas. Six graines initiales, augmentées si la variance entre entraînements domine.

**Mesure.** Soit \(p_{m,t}\) la proportion de comportements de persona validés indépendamment, et \(C_t=100(p_{P,t}-p_{B,t})\). Perte absolue \(A=100(p_{P,avant}-p_{P,après})\).

- **H_A, persistance pratique :** \(A<10\) points **et** \(C_{après}\geq20\) points.
- **H_B, non-persistance :** \(A\geq10\) **ou** \(C_{après}<20\).

Attendu : \(p_P=0{,}80\to0{,}75\), \(C=+40\to+34\), donc \(A=+5\) points. H_A n’est conclue que si les intervalles satisfont entièrement ses deux conditions ; H_B si un intervalle établit l’une de ses conditions ; sinon indécis.

**Trompeur et contrôle.** Une « persistance » sans déplacement réel de politique, ou un classifieur lisant seulement le format. Contrôles : dose KL mesurée, bras non-RL, test-retest et validation comportementale indépendante.

**Apport et contraire.** OCT installe les personas mais ne teste pas leur persistance ; le papier sur la chaleur reste en SFT (**RAPPORTÉ**, §1.1, §2). H_B conclurait à une non-persistance dans ce régime ; elle ne serait spécifique au RL que si les bras appariés ne montrent pas la même perte.

**Coût : 12 jours, 1 200 h-GPU**, hors annotation.

### E2 — Sélectivité sociale après RL

Sur les checkpoints E1, les évaluations factuelles sont hors support du RL, notamment la tâche de désinformation rapportée ; les évaluations sociales utilisent conseils et multi-tours. Chaque affirmation est présentée par l’utilisateur ou par une source impersonnelle ; le domaine factuel ajoute croyances correctes et incorrectes.

Pour chaque domaine \(k\), on mesure la capitulation binaire spécifique à la source utilisateur, puis sa double différence persona/base × avant/après, notée \(\delta_k\).

- **H_A :** \(\delta_S-\delta_F\geq+5\) points.
- **H_B :** \(\delta_S-\delta_F<+5\) points.
- **Attendu :** \(\delta_S=+2\), \(\delta_F=+2\), contraste **0 point**, donc H_B.

L’intervalle tranche ou déclare l’indécision. Les difficultés d’items sont choisies hors plancher/plafond ; les fiabilités par cellule bornent l’atténuation. Sorties naturelles et refus inclus sont principaux.

**Trompeur et contrôle.** Une baisse générale de justesse ou un format post-RL peut imiter la déférence : source impersonnelle, croyance correcte et extraction testée sur formats équivalents.

**Apport et contraire.** Les travaux rapportés distinguent déjà chaleur, capitulation factuelle et sycophancie sociale ; E2 ajoute leur interaction persona × RL. H_A établirait une sélectivité d’au moins 5 points dans ce régime ; H_B l’exclurait, sans exclure un effet générique ou plus petit.

**Coût : 6 jours, 300 h-GPU**, plus annotation potentiellement dominante ; dimensionnement après pilote apparié.

### E3 — Modification du gain d’attraction

Protocole dose–réponse de R6, avec \(v_0\) estimé sur des tirages disjoints de ceux servant à \(\Delta\). Modèle hiérarchique : \(g,c\) partagés par checkpoint, cadre et dose, effets d’item ; dispersion de \(v_0\) vérifiée. Le modèle d’attraction doit d’abord battre le déplacement constant.

- **H_A : invariance pratique**, \(|\Delta g|<0{,}10\).
- **H_B : modification**, \(|\Delta g|\geq0{,}10\).
- **Attendu :** \(\Delta g=+0{,}20\) sous éloge.

Équivalence seulement si l’intervalle est entièrement dans la marge ; modification seulement s’il est entièrement dehors. Le volume vise une demi-largeur strictement inférieure à \(0{,}05\) ; environ **24 000 générations par contraste intra-modèle** est seulement le point de départ **calcul/illustratif** suggéré par R6.

**Trompeur et contrôle.** Régression vers la moyenne, mauvaise spécification ou refus : tirages disjoints, simulations avec bruit et refus, dose nulle, permutations par blocs et bornes sur tous les items.

**Apport et contraire.** R6 est **OBSERVÉ-NON-AUDITÉ**, R3 montre une non-généralisation entre familles et R8 n’est pas exécuté. E3 n’en teste aucune conclusion générale : une invariance locale ne prouve ni persistance de persona ni S3.

**Coût conditionnel : 8 jours, 500 h-GPU** ; report si la précision reste insuffisante.

## (c) Réponse à l’arbitre

**Ce qui est rapporté.** OCT fournit une recette et annonce des checkpoints dont *Loving* et *Sycophantic*, mais sans mesurer leur persistance après entraînement ultérieur ni la sycophancie effective de *Sycophantic*. Le travail sur la chaleur traite l’entraînement de chaleur comme persona, mais teste seulement le SFT. La taxonomie interdit d’assimiler capitulation factuelle et cadrage social.

**Ce qui n’est pas établi.** L’accès réel aux poids, l’équivalence *Loving*/chaleur, la validité comportementale des personas, leur maintien après RL et tout effet causal du RL sur la sycophancie. La page exacte du mentor n’est pas servie. R6 et les contrôles associés restent non audités ; R8 reste non exécuté.

**Première expérience : E1, précédée de son verrou instrumental.** Elle répond directement à la persistance avec niveaux absolus, contraste persona–base et déplacement KL mesuré. Elle distingue ensuite érosion propre au RL et érosion commune à toute mise à jour. Elle produit enfin les checkpoints nécessaires à E2/E3 ; sans elle, leurs effets « après RL » seraient difficiles à interpréter.

**Ce qui ferait échouer le plan :**  
Accès refusé, persona initiale non validée ou contraste initial saturé.  
RL insuffisamment déplacé, ou variance entre entraînements empêchant tout intervalle utile.  
Échec des juges ou puissance humaine/matérielle insuffisante : verdict indécis, pas conclusion sur le style.

FIN-DE-CELLULE