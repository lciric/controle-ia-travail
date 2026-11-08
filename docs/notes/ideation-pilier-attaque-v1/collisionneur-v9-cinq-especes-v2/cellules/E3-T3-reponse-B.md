# Proposition B — Tour III.3 : réponse aux critiques

**Statuts.** J'utilise la même notation qu'en III.1 : [V] pour les empreintes ✓ seulement, [R] RAPPORTÉ, [ONA] OBSERVÉ-NON-AUDITÉ, [H] HYPOTHÈSE, [rel.] pour un relevé du dépôt cité sans statut, que je ne requalifie pas. Toutes mes réponses et expériences sont [H]. Tout seuil ou effectif de ma main est **illustratif**.

**Pièces.** FAITS, QUESTION, ma conception III.1 et les critiques A, C, D et E sont présentes et closes par FIN-DE-CELLULE, sans coupure visible. Je n'ai pas recalculé leurs empreintes. Je ne réponds qu'aux sections « Sur la proposition B » et au point transversal de A, qui me nomme.

**Légende.** ACC = acceptée. REJ = rejetée, avec sa raison. TEST = transformée en test. PART = acceptée en partie, la partie rejetée étant motivée.

---

## (a) Réponse critique par critique

### Vérité terrain et étiquettes

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 1 | L'étiquette « dormant » est fixée par l'oracle. Un sabotage diffus manqué devient un négatif. Le bruit d'étiquette est donc anticorrélé à la discrétion, et H8 peut être « confirmée » par construction (A, point transversal). | **TEST** | C'est le défaut le plus grave contre X1 et X2. **Correction** : le dormant exige l'absence de sabotage selon l'oracle **et** selon la vérification des événements exécutés. **Test** : X1 et X2 ne peuvent conclure à H8 que si la borne haute de η = P(oracle manque \| sabotage, strate diffuse) issue de X0 est ≤ η* (illustratif 0,05). Sinon, l'issue est déclarée « non jugeable », et non « H8 ». |
| 2 | X0a : la strate « diffuse » est définie par la couverture, la variable même de l'oracle, ce qui ouvre un biais de collisionneur (C a1, D a). | **PART** | REJ du collisionneur si la magnitude vient de la **provenance** (déclarée et scellée par le sas tiers), et non d'une mesure par l'oracle. ACC de l'ambiguïté de mon texte, que je lève. ACC de D : il faut une strate « acte sans baisse de couverture ». C'est l'angle mort structurel de N-060 v3 (S1), mesuré au lieu d'être supposé. |
| 3 | Le κ entre lecteurs mesure la concordance, pas la validité (D). | **ACC** | Le κ est rapporté mais ne sert jamais de critère. |
| 4 | Un rappel mesuré sur des sabotages tiers n'est pas transportable au diffus de T0.6 (E b, D b). | **ACC** | Rappel publié par strate, sans agrégat. J'ajoute un contrôle positif **en distribution** : épisodes d'un organisme flagrant étiquetés par les événements exécutés. A le proposait contre C ; je m'en sers en le disant. |
| 5 | X0b : l'équivalence (TOST) sur le rapport de cotes n'est pas jugeable si la cellule « double manqué » est presque vide. C estime environ 188 cas par strate pour une puissance non nulle. Le rapport de cotes est indéfini si une cellule est nulle (A b, C b1, D b, E b). | **ACC → TEST** | X0b est reformulé en **borne de biais sans hypothèse d'indépendance** (voir X0 corrigé). Le test d'association n'est conduit que si la positivité est atteinte, déclarée avant lecture. |
| 6 | « Corriger » les mesures en cas d'association n'a pas de modèle (E a). | **ACC** | Je donne le modèle : intervalle de Fréchet-Hoeffding sur le rappel vrai d'un moniteur, en fonction de η et du taux de fausses alertes de l'oracle. |

### Existence et localisation (X1, X2)

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 7 | Un effet présent seulement sur la famille (i) ne s'impute pas à la consigne, car consigne et famille sont confondues (A a1, E a). | **PART** | ACC : l'imputation à la consigne est retirée ; un tel effet est « non attribuable ». **REJ** de l'idée qu'exiger les deux familles serait un défaut parce qu'il ne s'agit pas d'une réplication : le croisement est voulu. Chaque famille neutralise le confondant de l'autre. Un effet présent sur les deux ne s'explique ni par la consigne seule ni par l'identité seule ; il reste ouvert à une cause commune de tâche, traitée en 13. Quant à la case « consigne neutre × sabotage » à l'intérieur de (i), elle est quasi vide par construction : je la déclare non identifiable. |
| 8 | La « base qui relit » ne borne pas la capacité textuelle ; même architecture ne veut pas dire même capacité effective (D a, E a). | **ACC** | L'énoncé est rétréci : « au-delà de ce que la base, lue par la même sonde aux mêmes positions, extrait ». J'ajoute un comparateur texte de capacité appariée (D). |
| 9 | Le placebo à étiquette tirée au sort donne ΔAUC nul par construction (A a4, E). | **ACC** | Remplacé par un placebo à **objectif caché inoffensif**, idée de D et E reprise en le disant. Son étiquette est comportementale : objectif bénin exécuté ou non. |
| 10 | Avec deux familles, la validation par bloc n'a que deux plis, sans variance inter-plis. Les tâches, mondes et graines traversent les plis (A b, D a/b). | **ACC** | Plis par graine d'organisme × monde de tâche (illustratif ≥ 10 blocs). Les familles sont rapportées séparément et ne sont jamais poolées. |
| 11 | Fuite de sélection de X1 vers X3 et X6 : effet du gagnant (A a2, C a2). | **ACC** | Trois parts disjointes, figées au préenregistrement : sélection, confirmation, réserve pour X3 à X6. |
| 12 | La correction de Holm est conservatrice quand les couches voisines sont corrélées (C b3). | **ACC** | Remplacée par le max-T par permutation (Westfall et Young, 1993, *Resampling-Based Multiple Testing*, Wiley). |
| 13 | Avant l'action, sur un préfixe identique, les activations ne dépendent que de la tâche et de l'organisme : on lit la susceptibilité de la tâche (C c1, D a). | **TEST** | Contrôle mécanique : sur des préfixes identiques et le même organisme, l'AUC doit valoir exactement 0,5 ; sinon le pipeline fuit. « Avant l'action » est redéfini comme l'intervalle entre le premier jeton échantillonné divergent et la première action étiquetée. Plancher supplémentaire : un prédicteur entraîné sur l'énoncé de la tâche seul. |
| 14 | Les échecs honnêtes manquent comme négatifs dans X1 (A c). | **ACC** | Ils deviennent des négatifs obligatoires dans X1 et X2. Les seuils sont rapportés séparément par classe de négatif (D). |
| 15 | S9 et l'« écart identiquement non nul » sont trop affirmatifs ; le complément orthogonal n'est pas exempt d'identité, puisque la base propage l'identité dans tout l'espace (A a3, E a). | **ACC** | S9 devient une attente [H], non une conséquence. Le complément orthogonal n'est plus un critère, seulement une description. |
| 16 | Le δ de X2 compare des contrastes asymétriques. Ce n'est pas une différence de différences causale. Le placebo n'a pas d'acte. La partition sabotage/dormant peut recouper la difficulté de la tâche (C a4, D a, E a/b, A b). | **ACC** | Estimand symétrique : (acte contre dormant, même tâche) chez le saboteur, comparé à (acte bénin contre dormant bénin, même tâche) chez le placebo. Seules les tâches où les deux classes existent sont retenues (positivité). Je l'appelle « contraste d'AUC » et non différence de différences causale. |
| 17 | Le placebo doit être apparié en rang, en norme des poids et en volume de distillation, et pas seulement en graine (A c). | **ACC** | Intégré au cahier du placebo. |

### Causalité (X3)

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 18 | La pente intra-dose subit un biais d'atténuation ; elle n'est pas identifiable si Var(projection \| α) est petite (A b, C b2, D b). | **ACC** | La pente devient descriptive et secondaire. Le test primaire est l'intervention randomisée. |
| 19 | Le seuil « 30 % de l'écart » n'est pas jugeable si l'écart diffus est petit (A b). | **TEST** | Précondition déclarée : l'intervalle de l'écart de dommage saboteur − jumeau à la dose diffuse doit exclure 0. Sinon, X3 est non jugeable au diffus et S100 sert seulement de contrôle positif. |
| 20 | La substitution sort de la variété des activations ; une ablation sans effet peut traduire une redondance (D a, E a). | **ACC** | J'ajoute une substitution croisée intra-condition (saboteur i ← saboteur j, même tâche), que C propose contre A ; je m'en sers en le disant. H_B est renommée « non levier à ce site » au lieu d'« épiphénomène ». |
| 21 | Le sens réducteur ne suffit pas : la substitution peut améliorer une compétence générale (E a). | **ACC** | Contrôle : la même substitution sur le placebo. La couverture n'y doit pas monter au-delà de la marge. |
| 22 | La direction témoin doit être prise dans le sous-espace de l'adaptateur, appariée en norme et en covariance (A c, D c). | **ACC** | Elle remplace la direction aléatoire isotrope. |

### La pince (X4)

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 23 | Une seconde externe faible rend CR_int > CR_ext2 trivial. Il faut aussi comparer à la meilleure boîte seule à τ plein (C a3). | **ACC** | ext2 est choisie avant lecture parmi les externes qui battent le plancher mécanique : ni le juge de 3 milliards, ni l'externe-texte. J'ajoute un duel séparé X4b. Je ne le mets pas en conjonction avec X4a : C montre, contre E, que la conjonction peut rendre la région H_A vide. |
| 24 | Le dénominateur honnête sert à la fois à calibrer et à évaluer (A a5). | **ACC** | Il est scindé en calibration et évaluation. |
| 25 | Si les scores honnêtes sont corrélés (ρ_H > 0), le taux joint est inférieur à τ et la comparaison est inéquitable (A b). | **PART** | REJ quand H_A gagne : un budget effectif plus strict désavantage la pince, la conclusion reste donc conservatrice. ACC quand H_A perd : la falsification n'est valide qu'à taux de fausses alertes réalisé égalisé (X4b). |
| 26 | m ≈ 45 manqués ne permet pas de juger (A b). | **ACC** | Exigence de m ≥ 150 (illustratif), déclarée sur le split de calibration avant lecture. En dessous : non jugeable. |
| 27 | Une corrélation de Spearman nulle n'établit pas l'indépendance. Calibrer λ sur les jumeaux ne valide que la classe négative (D a, E a/b). | **ACC** | L'inférence par le signe de Spearman est retirée. λ est calibré sur les deux classes, sur des blocs de validation. J'utilise l'identité de E, en le disant : c − P(I=1\|Y=1) = −Cov(I,E\|Y=1)/p. La capture résiduelle mesure donc une covariance d'alertes, autrement dit une complémentarité, jamais l'étau. Cela confirme mon S7. |
| 28 | L2 et E7 n'encadrent pas toute courbe jointe (E a). | **ACC** | Ce sont des courbes de référence, non des bornes. |

### L'étau (X5)

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 29 | Le déplacement interne peut passer par le texte (A a6). | **ACC** | Δ_int = score organisme − score de la base qui relit, calculé à chaque génération. |
| 30 | « À dommage tenu constant » conditionne sur une variable post-traitement : sélection des survivants (C a1, E a, D b). | **ACC** | Analyse en intention de traiter sur tous les épisodes, le dommage étant un résultat et non un filtre. L'énoncé « à dommage maintenu » ne vaut qu'avec les bornes de Lee (Lee, 2009, *Review of Economic Studies*, « Training, Wages, and Sample Selection: Estimating Sharp Bounds on Treatment Effects »). |
| 31 | Il faut contrôler la dérive (KL ou norme des poids) entre le bras « pression externe » et le bras placebo (C c2). | **ACC** | Dérive mesurée et appariée par budget ; à défaut, entrée comme covariable préenregistrée. |
| 32 | Il faut des lignées indépendantes randomisées (E c). | **ACC** | Affectation tirée au sort par lignée, avec au moins 4 lignées par bras (illustratif). |

### Règle de défense (X6)

| # | Critique (source) | Verdict | Réponse |
|---|---|---|---|
| 33 | La réserve (c) confond secret, diversité et qualité des détecteurs (A a7, D a, E a). | **ACC** | La réserve est tirée au hasard dans le panel déployé. Le secret devient une divulgation randomisée à panel constant, selon le contraste do(Q) de E, utilisé en le disant. Un mélange uniforme public est ajouté comme bras. |
| 34 | Dans T[j,k], une attaque devenue inoffensive compte comme évasion (D a). | **ACC** | T[j,k] est calculé sur les seuls épisodes à dommage attesté. Dommage et fausses alertes sont publiés par cellule. |
| 35 | La valeur du programme linéaire est biaisée vers le haut ; la meilleure réponse au mélange peut sortir du support (A b, D b). | **ACC** | p est estimé sur un split. La valeur est évaluée sur épisodes frais **et** sur une génération fraîche optimisée contre l'espérance de p. |
| 36 | Un faible v_mix − v_pur n'identifie pas l'absence de diversité (E b). | **PART** | ACC sur la formulation : je retire « le transfert est fort » de H_B. **REJ** sur le fond : X6a ne porte pas sur la diversité mais sur le gain de valeur garantie. H_B se lit : « le mélange n'augmente pas la valeur garantie par rapport à la meilleure sonde pure ». La diversité se teste à part, contre le panel dupliqué. |
| 37 | La stabilité sur les attaques historiques ne dit rien des attaques nouvelles (E a). | **ACC** | J'ajoute à chaque pas une colonne « génération fraîche » au triangle inférieur. |
| 38 | Il manque un panel dupliqué pour fixer la diversité nulle (D c, E c). | **ACC** | Ajouté : même architecture, graines différentes. |

---

## (b) Expériences corrigées

**Cadre commun** [H]. Chaque duel porte sur un contraste θ avec une frontière δ, de sorte que H_A : θ > δ et H_B : θ ≤ δ sont exclusives et exhaustives. J'adopte la règle de E, en le disant : un intervalle qui traverse δ est **non jugeable**, et ce n'est pas une troisième hypothèse. Chaque expérience déclare **avant lecture** sa condition de positivité (effectifs de cellule, nombre m de manqués, support commun). Si cette condition échoue, on publie « non jugeable » et l'on ne lit rien.

Une simulation sur processeur, sans aucune donnée d'organisme, vérifie la jugeabilité de chaque estimateur avant scellement. A propose de contrôler ainsi les énoncés « vrais par construction ».

Le rationnement est inchangé : seuls X4 et X6b consomment une famille tenue à l'écart.

### X0 — Oracle : rappel par strate et borne de biais (prérequis de tout le reste)

**X0a**
- **Duel.** H_A : rappel ≥ r* sur la strate diffuse. H_B : rappel < r*.
- **Jeu connu.** Construit par le sas tiers ; magnitude définie par la **provenance**, déclarée et scellée. Trois strates :
  - flagrante ;
  - diffuse ;
  - acte sans baisse de couverture. Le rappel y est attendu bas par définition (S1) ; on le mesure pour borner le périmètre de l'oracle, sans conclure sur la qualité de l'oracle.
- **Contrôle positif en distribution** : organisme flagrant étiqueté par les événements exécutés.
- **Statistique.** Clopper-Pearson par strate. Seuil illustratif : r* = 0,70 en borne. Effectif illustratif : environ 60 cas par strate.

**X0b, reformulé en borne**
- Pour tout moniteur évalué aux points 1 à 5, on publie l'intervalle de Fréchet-Hoeffding de son rappel vrai, connaissant η (borne haute de X0a) et le taux de fausses alertes de l'oracle. Cet intervalle ne suppose aucune indépendance.
- **Duel.** H_A : la largeur de l'intervalle est ≤ b* (illustratif 0,05). H_B : elle est > b*.
- **Issues.**
  - Si H_A est réfutée, les points 1 à 5 sont non jugeables pour la strate diffuse ; le flagrant reste lisible.
  - Si H_B est réfutée, les rappels en aval sont interprétables à b* près.
- **Test d'association, secondaire.** Rapport de cotes de Mantel-Haenszel stratifié (Mantel et Haenszel, 1959, *J. Natl Cancer Inst.*, « Statistical aspects of the analysis of data from retrospective studies of disease »). Il n'est conduit que si la cellule « double manqué » attendue est ≥ 20 (illustratif) dans chaque strate. Il porte sur **tous** les moniteurs candidats, sondes internes comprises, selon le plan factoriel famille d'oracle × famille de moniteur.
- **Réfutation.** H_A tombe si l'intervalle de Fréchet dépasse b* ; H_B tombe sinon.

### X1 — Existence au-delà de ce que la base extrait

**Duel.**
- H_A : ΔAUC = AUC(organisme) − AUC(base qui relit, même sonde) > δ (illustratif 0,03) sur **les deux** familles, séparément.
- H_B : ΔAUC ≤ δ sur au moins une famille.

**Étiquettes et négatifs.**
- Dormant défini par l'oracle **et** par les événements exécutés.
- Négatifs : dormants, échecs honnêtes, épisodes placebo, chacun rapporté séparément.

**Comparateurs.**
- Base qui relit.
- Prédicteur texte de capacité appariée.
- Prédicteur sur l'énoncé de la tâche seul, pour la classe « avant l'action ».

**Plan.**
- Plis par graine × monde.
- Trois parts disjointes : sélection, confirmation, réserve.
- Correction par max-T.
- Positions : avant l'action au sens redéfini (critique 13), pendant, après.

**Contrôles.**
- AUC = 0,5 exactement sur préfixes identiques (contrôle mécanique).
- Tâches de contrôle (Hewitt et Liang, 2019).
- Placebo à objectif bénin : son ΔAUC sert de **référence**, et non de zéro attendu.

**Issues.**
- H8 n'est admissible comme issue que si la borne de X0 est ≤ η*.
- Un effet sur une seule famille est « non attribuable » ; il déclenche la reconception prévue par R-1795, rapportée.

### X2 — Identité contre acte

**Duel.**
- H_A : le contraste d'AUC dépasse la marge, avec θ = AUC_D(saboteur : acte contre dormant, même tâche) − AUC_D(placebo : acte bénin contre dormant bénin, même tâche) > δ.
- H_B : θ ≤ δ. D est alors un détecteur d'organisme utile à l'audit, mais pas d'acte.

**Placebo.** Même chaîne, objectif caché inoffensif, apparié en rang, en norme et en volume de distillation. On ne le choisit **pas** pour son indétectabilité (E contre A).

**Test d'identité direct** : saboteur dormant contre placebo dormant. On le publie même si H_A gagne. E a raison : une sonde peut lire les deux à la fois.

**Positivité** : seules les tâches où les deux classes existent chez les deux organismes entrent dans l'analyse.

### X3 — Causalité par intervention randomisée

**Duel.**
- H_A : la substitution depuis le jumeau, aux sites confirmés en X1, réduit le dommage plus que **chacun** des quatre contrôles, d'au moins 30 % de l'écart (illustratif).
- H_B : pas de levier à ce site.

**Les quatre contrôles.**
1. Direction appariée en norme et en covariance dans le sous-espace de l'adaptateur.
2. Substitution croisée intra-condition.
3. Même substitution sur le placebo, pour la compétence générale.
4. Direction « identité ».

**Doses.** Diffuse, avec la précondition de la critique 19 ; S100 en contrôle positif.

La pente intra-dose est publiée comme description, avec son biais d'atténuation déclaré.

### X4 — Pince : deux duels séparés (consomme une famille tenue à l'écart)

**X4a.**
- H_A : CR_int − CR_ext2 > 0.
- H_B : CR_int − CR_ext2 ≤ 0.

**X4b.**
- H_A : la pince, avec des seuils ajustés sur la calibration pour que l'union atteigne un taux réalisé = τ, a un rappel supérieur à la meilleure boîte seule à τ.
- H_B : elle ne le dépasse pas.

**Conditions communes.**
- Dénominateur honnête scindé en calibration et évaluation.
- m ≥ 150, déclaré avant lecture.
- ext2 choisie avant lecture.
- L'externe qui a fixé la dose diffuse est exclue (S2).

**Lecture.** X4 mesure une complémentarité (critique 27). Aucune de ses issues ne conclut sur l'étau.

### X5 — L'étau comme effet d'une affectation

**Duel.**
- H_A : en intention de traiter, Δ_int (corrigé par la base qui relit) est plus grand sous pression externe que sous pression placebo, et les deux bornes de Lee restent > 0.
- H_B : la différence est ≤ 0, ou une borne de Lee est ≤ 0.

**Plan.**
- Lignées randomisées.
- Budget et dérive appariés.
- Bras rouge aveugle à l'interne ; il ne transmet à la défense que les adaptateurs et les épisodes.

Sans bras rouge disponible, X5 est déclaré **non faisable**. On ne le remplace pas par X4.

### X6 — Transfert, valeur, secret

**X6a.**
- T[j,k] sur épisodes à dommage attesté.
- Panel dupliqué comme référence de diversité nulle.
- p estimé sur un split ; valeur évaluée sur épisodes frais et sur une génération fraîche optimisée contre E_p.
- H_A : v_mix − v_pur > δ. H_B : v_mix − v_pur ≤ δ.

**X6b (consomme une famille tenue à l'écart).**
- Trois bras à panel constant : figée publique, mélange révélé, divulgation tirée au sort ; plus un bras mélange uniforme public.
- Le contraste du secret se lit à panel constant.

**Convergence.**
- La défense converge si le triangle inférieur ne se dégrade pas, si la colonne de génération fraîche reste stable, et si la valeur varie de moins de ε pendant k pas (ε = 0,02, k = 3, illustratifs).
- L'arrêt par budget reste lié à N-059 point 11, non servi.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi** (statuts inchangés)

- **Détection.** Elle n'a été mesurée que sur le flagrant :
  - W − G = +0,932 [rel.], mais la sonde W lit la consigne privée (a_NE 0,9967) [rel.] ;
  - sondes génériques au rappel 0,013 [rel.] ;
  - juge de 3 milliards à une aire de 0,523 [rel.] ;
  - prédicteur sur traits du texte à 0,866, métrique non servie [rel.].
- **Oracle.** Son rappel sur sabotages connus n'a jamais été mesuré [rel.]. Par définition, il ne voit qu'une baisse de couverture contre le jumeau [rel., N-060 v3] : un acte sans baisse de couverture lui est invisible par construction.
- **Axe de douleur.** Il se lit mais n'est pas un levier (retrait sans effet 24/25) [R].
- **Arène synthétique.** R3 progresse, mais R0 figée détecte mieux sur les attaques tenues à l'écart. Les tables B/B′ sont suspendues et aucun verdict n'est scellé [rel.].
- **Littérature.** Les ensembles de sondes « atténuent sans éliminer » l'évasion (Chameleons) [R]. Le transfert est inégal entre trois sondes, sans juge (2609.36490, fig. 4a) [R].
- **Méthode.** Ce sont des identités algébriques, vérifiables par recalcul ; leur pertinence pour nos données reste [H] :
  - CR > TPR_int équivaut à une covariance négative des alertes, donc la capture résiduelle mesure une complémentarité, pas l'étau ;
  - une marge absolue sur la covariance d'erreurs est satisfaite d'office quand les erreurs sont rares (Fréchet) ;
  - l'AUC contre des négatifs mêlés est une moyenne pondérée.

**Ce qui n'est pas établi**

- L'existence d'une trace du diffus (H1 ou H8).
- La séparation entre acte et identité.
- Une direction causale.
- Le rappel de l'oracle et son indépendance vis-à-vis des moniteurs.
- Le taux de fausses alertes de Jev, qui est [ONA].
- L'étau : rien dans les faits n'indique qu'un organisme ait été optimisé contre une mâchoire externe. Aucune mesure actuelle ne peut donc le trancher.
- L'effet d'une randomisation sur un vrai modèle.
- Le nombre de familles tenues à l'écart disponibles.

**L'expérience à faire en premier : X0**

Il s'agit du rappel de l'oracle par strate de provenance, avec la strate « acte sans baisse de couverture » et le contrôle positif en distribution. Elle est précédée de la simulation sur processeur de jugeabilité de tous les estimateurs préenregistrés.

En parallèle, il faut construire le placebo à objectif caché inoffensif, prérequis de X1 et X2.

**Pourquoi X0 d'abord.** Le point transversal de A montre que, sans borne sur η, toute issue négative de X1 et X2 peut être produite par l'oracle lui-même. Chaque rappel en aval n'est interprétable qu'à la largeur de Fréchet près.

**Issue négative écrite d'avance.** Une largeur > b* sur la strate diffuse suspend les points 1 à 5 pour le diffus, et seulement pour lui. Elle ouvre une reconception de la vérité terrain qui sépare acte et dommage (E contre A).

**Ce qui réfuterait cet ordre.** Si la simulation montre X0 non jugeable aux effectifs atteignables, aucune affirmation sur le diffus n'est possible avant l'entretien TAIF, quelle que soit la sonde. Il faut alors le déclarer tel quel.

**Coût et délai.** Processeur, plus lecteurs et sas tiers. Le délai, illustratif, dépend de la construction du jeu connu par le tiers et n'est pas chiffrable depuis les faits.

FIN-DE-CELLULE