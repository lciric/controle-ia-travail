# Proposition B, tour III.3 : réponse aux critiques

**Pièces manquantes.** La critique croisée C est absente (jamais lancée) ; je n'en suppose aucun contenu. Le texte de la page du mentor n'est pas servi non plus.

**Statuts.**
- Les faits tirés des papiers sont RAPPORTÉ.
- Les résultats des dépôts publics de Lazar sont OBSERVÉ-NON-AUDITÉ. Au tour III.1, je les avais marqués RAPPORTÉ. Les pièces ne leur attribuent aucun statut explicite, la proposition A les classe OBSERVÉ-NON-AUDITÉ, et je retiens le moins fort des deux.
- Mes réponses, corrections et prédictions sont HYPOTHÈSE.
- Mes seuils et mes coûts sont « supposé » ou « illustratif » ; les dérivations sont marquées « calcul ».

---

## (a) Réponse critique par critique

Codes : **A-**, **D-** et **E-** renvoient à la proposition qui critique ; le chiffre ou la lettre renvoie à sa section.

### Défauts partagés signalés par A

| Critique | Verdict | Traitement |
|---|---|---|
| **A-Σ1.** La persistance serait vraie par construction : pénalité KL vers la persona, adaptation de rang faible sur des mathématiques. | **Rejetée comme certitude, transformée en test.** Le sous-espace « disjoint » est lui-même une hypothèse : l'adaptateur RL et la persona fusionnée (`maius`, points de contrôle fusionnés, piece-ibrahim §3) touchent les mêmes couches. Le risque est réel. | Deux bras : β = 0 et β_réf. La politique de référence est déclarée : c'est le point de contrôle de départ. Sous β_réf, je **prédis** \|ΔC\| < 0,1 (supposé). Cela sert de contrôle interne de l'argument de A. |
| **A-Σ2.** Le ratio r est instable quand son dénominateur est bruité. | **Acceptée.** | L'estimand principal devient une **différence**. r n'est rapporté qu'à titre descriptif, et seulement si l'IC de C_avant reste loin de 0. Les niveaux absolus de chaque modèle sont publiés (E-b : une perte commune laisse r inchangé). |
| **A-Σ3.** La version du juge est confondue avec le passage avant/après. | **Acceptée.** | Juge figé par version. Les sorties avant et après sont notées dans la **même passe, entrelacées**, avec des sorties ancres répétées (repris de D-c2, adressé à E). |

### Critiques propres à B

| Critique | Verdict | Traitement |
|---|---|---|
| **A-1, D-a1, E-a2.** Mon attendu r ≈ 0,6 tombait dans la zone « non tranché ». | **Acceptée.** C'est le défaut principal de ma conception. | Le duel est reparamétré : érosion d'au moins δ contre équivalence à ±δ (voir b). L'attendu (ΔC ≈ −0,2, supposé) se trouve dans une région décisive. La taille de l'expérience est fixée par un pilote pour que ce soit tenable. |
| **A-2, D-a5, E-a5.** Le SFT neutre est apparié sur le nombre de pas, et des gains mathématiques égaux n'impliquent pas des déplacements égaux. | **Acceptée.** | Points de contrôle intermédiaires. KL(π ‖ π₀) est mesurée sur des invites conversationnelles tenues à l'écart. Les bras sont comparés **à KL égale**, sur une courbe érosion–déplacement, et non à pas égaux. |
| **A-(c), D-c3, E-b.** Il manque une récompense non informative pour E1, et cette récompense peut ne rien optimiser. | **Acceptée.** | Bras « récompense permutée », mêmes invites, même optimiseur. On vérifie qu'il produit un déplacement KL réel ; sinon, il est déclaré inopérant. |
| **E-c.** Il manque un bras sans mise à jour. | **Acceptée.** | Bras gelé, réévalué à chaque passe : il mesure la dérive de l'instrument. |
| **A-3.** Recouvrement construit entre persona et sycophancie ; classifieur peut-être évalué sur ses données de construction ; circularité importée. | **Acceptée.** | Classifieur d'une autre famille que le professeur (GLM 4.5 Air, piece-ibrahim §2). Construction sur des données disjointes des 12 000 transcriptions. Évaluation sur un lot réservé. J'ajoute des items de chaleur **sans opinion à approuver** : idée de la proposition E, que je reprends telle que A la rapporte. |
| **A-4, D-a4, D-c2.** Un reformatage artificiel ne représente pas le format réellement produit après RL. | **Acceptée.** | Nulle de format : Instruct avant et après le même RL. Validation sur des **sorties post-RL réelles** de chaque bras. Paires à position constante et ton, format ou longueur variables (E-c). |
| **E-a3.** La rétention dépend de l'échelle du classifieur. | **Acceptée.** | Mesure principale : une étiquette binaire « persona présente », à seuil calibré sur annotation humaine. En secondaire, une AUC persona contre base, invariante par transformation monotone. Je signale sa saturation près de 1 (A-b). |
| **A-9.** Juge validé hors distribution. **A-(b), E-b.** Atténuation différentielle selon le bras. | **Acceptée.** | Annotation humaine aveugle **par bras**, y compris après RL. Sensibilité s et spécificité p estimées par bras. Correction π = (π* + p − 1)/(s + p − 1), d'après la formule de A. |
| **D-a3, E-a4, E-b.** Cas positifs circulaires : les sorties de *Sycophantic* prises comme vérité. | **Acceptée.** | Les cas positifs sont définis par une **annotation comportementale aveugle**, sans connaître le point de contrôle. On y ajoute des accords justifiés et des désaccords injustifiés (E-c). |
| **D-b.** Le kappa est instable quand la prévalence est extrême. | **Acceptée.** | Je rapporte s, p et l'accord par classe. Le kappa seul n'est plus un critère. |
| **A-8, D-a2, E-a6.** E4 est un contrôle positif ; ses thèses « ton / disposition » dépassent ce qu'il mesure ; l'ordre imposé à *Loving* crée une issue non assignée. | **Acceptée en partie.** Je retire les thèses et l'ordre. Je **rejette** l'idée qu'une issue H_A n'apprendrait rien : Open Character Training n'a pas mesuré la sycophancie de *Sycophantic* (RAPPORTÉ, piece-ibrahim §2). | E4' devient le contrôle positif de la **manipulation** et de l'instrument (voir b). |
| **D-c4.** Il manque la croyance correcte et la source impersonnelle dans E4. | **Acceptée.** | Quatre conditions : sans croyance, croyance correcte, croyance fausse de l'utilisateur, même affirmation fausse d'origine impersonnelle. |
| **D-b.** La manipulation peut être inerte, ou l'erreur peut être au plafond, ce qui rend H_B vraie par construction. | **Transformée en test.** | Prérequis déclaré : l'erreur sans croyance doit se situer entre 0,1 et 0,9 (supposé). Sinon, E4' est déclaré non jugeable, et non H_B. |
| **E-a1.** E3 confond v₀ (valeur initiale de l'item) et c (point fixe). | **Acceptée.** C'est une erreur de ma part. Dans Δ = g·(c − v₀), le point fixe est c (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §1). | Les hypothèses d'E3' portent désormais sur c et g. v₀ devient une covariable mesurée sur des tirages indépendants. |
| **A-7.** Pas de test de spécification de la loi. | **Acceptée.** | Le modèle concurrent à déplacement constant est ajusté **avant** toute lecture de Δg. S'il l'emporte sur *Loving*, E3' est déclaré non applicable (même cas que R3). |
| **D-b, E-b.** Identifiabilité de g et c, et atténuation par l'erreur de mesure sur v₀. | **Transformée en test.** | Simulation de récupération de paramètres avant les données réelles. Deux générateurs : c constant et v₀ variable, puis v₀ constant et c variable, avec erreur de mesure. g est partagé entre items dans un modèle hiérarchique, et non estimé item par item. |
| **A-(b).** La résolution d'E3 est inférieure à mes seuils (demi-largeur ≈ 0,2 au volume de R6). | **Acceptée.** | Volume ×4, ce qui ramène la demi-largeur à ≈ 0,1 (calcul : (0,2/0,1)², à partir de A) ; seuils relevés. |
| **D-a7.** Les générations d'E1 ne servent pas à E3. | **Acceptée.** | E3' a son propre protocole dosé, sur les **mêmes points de contrôle** et non sur les mêmes générations. Le coût marginal annoncé au tour III.1 était faux. |
| **A-5, D-a6, E-b.** Appariement sur la longueur, variable post-traitement. | **Acceptée.** | E2 est reportée. Si elle est jouée, la pénalité de longueur est déclarée d'avance dans la récompense, et l'analyse marginale sur sorties intégrales est l'analyse principale. |
| **A-6.** Le modèle de récompense d'E2 peut favoriser la validation. | **Transformée en test.** | Prérequis d'E2 : sonder le modèle de récompense par des paires minimales qui ne diffèrent que par les mots de validation, ou que par la longueur. Si la récompense suit ces paires, l'amplification est un artefact de construction, déclaré comme tel. |
| **A-(b).** E2 demande n ≈ 17 000 par cellule sans appariement (calcul de A). | **Acceptée.** | E2 n'est pas jugeable au premier tour. |
| **A-(b), D-b, E-a, E-c.** Refus exclus, ce qui revient à conditionner sur une variable post-traitement. | **Acceptée.** | Le refus devient une catégorie explicite. Analyse principale marginale, avec bornes de pire cas : refus compté juste, puis faux. Analyse conditionnelle en secondaire. |
| **A-(b), E-b.** Trois graines donnent deux degrés de liberté ; la variance entre entraînements domine. | **Acceptée.** | Pilote à deux graines pour estimer σ_entraînement. K est fixé d'avance par calcul (voir b). |
| **A-10.** Multiplicité des tests. | **Acceptée.** | Un estimand principal (Duel 1 d'E1'). Tous les autres sont secondaires, avec correction de Holm. |
| **A-(b).** Saturation de l'échelle. | **Acceptée.** | Prérequis : P(persona \| Instruct) doit être non nulle pour estimer la nulle de format. Lecture en logit en secondaire. |
| **A-E-a2.** Fuite de domaine entre récompense et évaluation (critique adressée à E). | **Reprise, en le disant.** | L'évaluation de la sycophancie porte uniquement sur des items non mathématiques : désinformation et phrases émotionnelles (piece-ibrahim §1.1). |

---

## (b) Expériences corrigées

### Temps zéro (porte, 1 jour) : E4' et validation des instruments

- **Ce qu'on mesure.** Instruct, *Loving* et *Sycophantic* (sous réserve d'accès, piece-ibrahim §3), sans entraînement, dans les quatre conditions de croyance (D-c4), sur la tâche de désinformation et les phrases émotionnelles (§1.1).
- **Duel.**
  - H_A, « la manipulation a prise » : pour *Sycophantic*, erreur(fausse croyance de l'utilisateur) − erreur(sans croyance) ≥ 10 points, **et** cet écart dépasse de ≥ 5 points celui de la source impersonnelle (supposé). Cette issue falsifie « instrument ou point de contrôle inerte ».
  - H_B : écart < 3 points (supposé). Cette issue falsifie « *Sycophantic* capitule factuellement sur ces items ». Le volet factuel d'E1' est alors déclaré non jugeable, et la mesure bascule vers la sycophancie sociale (§1.6).
  - Prérequis : erreur sans croyance entre 0,1 et 0,9 (supposé).
- **Instruments, dans la même journée.**
  - Annotation humaine aveugle, deux annotateurs, ≈ 300 sorties (illustratif), tirées d'un lot réservé.
  - s et p rapportés séparément pour le juge et pour le classifieur de persona.
  - Le classifieur doit battre trois prédicteurs mécaniques : longueur, présence d'une chaîne de raisonnement, compte lexical des mots de validation.
- **Coût illustratif.** ≈ 10 heures de carte et ≈ 1 jour.

### E1' (principale) : érosion de la persona sous RLVR, comparée à KL égale

- **Départs.** Instruct et *Loving*. *Sycophantic* n'est utilisé qu'au temps zéro.
- **Bras, pour chaque départ :**
  - (i) gelé ;
  - (ii) RLVR mathématique, β = 0 ;
  - (iii) RLVR, β_réf, référence = départ ;
  - (iv) récompense permutée, β = 0 ;
  - (v) SFT neutre.
- **Points de contrôle.** Plusieurs étapes par course. KL(π ‖ π₀) est mesurée sur des invites conversationnelles tenues à l'écart.
- **Estimand principal.**
  - C_t = P(persona | *Loving*, t) − P(persona | Instruct, t), après correction par (s, p) estimés par bras.
  - ΔC = C_après − C_avant, dans le bras (ii) en fin de course.
  - Le passage Instruct avant → après sert de nulle de format : un effet de format commun aux deux modèles s'annule dans C.

**Duel 1 (principal).** δ = 0,1 en proportion (supposé).

| Issue de l'IC95 de ΔC | Verdict |
|---|---|
| Entièrement sous −δ | H_A « le RLVR érode la persona » est retenue ; H_B est falsifiée. |
| Entièrement dans ]−δ ; +δ[ | H_B « pas d'érosion d'ampleur δ » est retenue ; H_A est falsifiée. |
| Entièrement au-dessus de +δ | Amplification : falsifie les deux. Issue déclarée d'avance. |
| Autre | Non concluant, déclaré d'avance. |

**Duel 2 (secondaire, Holm).** À KL appariée par tranches :
- H_A « effet propre de la récompense » : l'érosion sous RLVR dépasse de ≥ δ celle de la récompense permutée et celle du SFT neutre.
- H_B « l'érosion est fonction du déplacement seul » : différences dans ±δ.
- Chaque issue falsifie l'autre.

**Résultat attendu (supposé, signé).**
- C_avant ≈ +0,6 (illustratif).
- Bras (ii) : ΔC ≈ −0,2, soit une érosion.
- Bras (iii) : |ΔC| < 0,1, ce qui confirmerait l'argument A-Σ1.
- Duel 2 : H_B attendue. Une récompense mathématique ne contient rien sur la persona ; je prévois une érosion générique liée au déplacement.
- Volet sycophancie (secondaire, uniquement si E4' donne H_A) : l'écart *Loving* − Instruct sur fausse croyance + tristesse **garde son signe** après RL. Pour repère hors chaîne : −15,06 points de justesse sous SFT de chaleur (RAPPORTÉ, tableau E5, §1.1).

**Ce qui rendrait le résultat trompeur, et son contrôle.**
- *Dérive de format ou de juge* lue comme une érosion. Contrôles : nulle Instruct, (s, p) par bras sur sorties post-RL réelles, notation entrelacée, bras gelé.
- *Refus différentiels.* Contrôle : bornes de pire cas.
- *Persistance artificielle due à β.* Contrôle : bras β = 0.

**Puissance.**
- La demi-largeur visée est ≤ 0,08 (supposé), pour que l'attendu −0,2 sorte de la zone non concluante.
- Avec K graines, demi-largeur ≈ t_{K−1}·s/√K. À K = 5, cela fait 1,24·s, d'où s ≤ 0,065 entre graines (calcul sur valeurs supposées).
- Le pilote mesure s. Si K > 8 serait nécessaire (illustratif), je supprime le bras (v) avant de réduire K.

**Coût illustratif.**
- Pilote : 10 h.
- Courses : 2 départs × 5 bras entraînés ou gelés × 5 graines, ≈ 40 courses entraînées × ≈ 5 h, soit ≈ 200 h.
- Évaluation : ≈ 20 h.
- Annotation : ≈ 600 sorties × 2 annotateurs.
- Durée : ≈ 7 à 8 jours.

### E3' (secondaire) : point fixe c ou gain g

- **Ce qu'on mesure.** Protocole dosé au format de R6, volume ×4 (≈ 5 400 générations par modèle, calcul). Instruct et *Loving*, avant RL puis après le bras (ii).
- **Prérequis.**
  - Simulation de récupération des paramètres.
  - Le modèle à déplacement constant doit être battu.
- **Duel (seuils supposés).**
  - H_A « persona = point fixe » : |Δc| ≥ 0,5 point d'échelle et |Δg| < 0,1.
  - H_B « persona = gain » : Δg ≥ 0,2 et |Δc| < 0,25.
  - Si les deux bougent, ou si aucun ne bouge, les deux lectures simples sont falsifiées. Issues déclarées.
- **Limite de portée.** Ce duel ne réfute pas l'a priori de R8 : la chaîne est autre et la DPO est déjà présente (A et D).
- **Coût illustratif.** ≈ 20 h de carte par modèle.

### E2 : reportée

Ses prérequis ne sont pas remplis : sonde du modèle de récompense, pénalité de longueur, appariement par item. Sans eux, le volume nécessaire la rend non jugeable au premier tour (calcul de A).

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi** (RAPPORTÉ, piece-ibrahim) :
- Un **ajustement supervisé** de chaleur, traité comme une persona, augmente l'erreur quand l'utilisateur exprime une fausse croyance (+11 points, portée par modèle non établie, §1.1). Le plus grand effet est un écart de 11,9 points sous tristesse. Sur Llama-3.1-8B, −12,96 points de justesse avec tristesse, contre −0,25 sans contexte (tableau E5).
- Seul l'ajustement supervisé a été testé. Le rôle des préférences y est **supposé**.
- 88,7 % des experts désignent l'apprentissage par préférences comme cause principale de la sycophancie. C'est une opinion d'experts, pas un résultat (§1.2).
- Des points de contrôle *Loving* et *Sycophantic* existent sur Llama-3.1-8B-Instruct (§3). Leur persistance après un entraînement ultérieur et la sycophancie de *Sycophantic* n'ont **pas** été mesurées (§2).
- OBSERVÉ-NON-AUDITÉ : la loi d'attraction tient sur Llama-3.1-8B-Instruct et ne passe pas aux autres familles (R3). R8 n'est pas exécuté (piece-sycophancie §1–§2).

**Ce qui ne l'est pas :**
- l'accès réel aux poids ;
- la conformité de la direction à la page du mentor ;
- l'existence d'une chaîne publique avec une étape RL sur ces personas ;
- la capacité des classifieurs de persona à lire autre chose que le format ;
- l'effet d'un RL, quel qu'il soit, sur la persona ou sur sa sycophancie.

**La première expérience : E1', précédée de sa porte au temps zéro.**

- **Ce qu'on entraîne.** *Loving* et Instruct reçoivent la même étape RLVR mathématique, avec adaptation de rang faible, à β = 0 et à β_réf. Témoins : récompense permutée, SFT neutre, bras gelé. Cinq graines.
- **Ce qu'on mesure.** ΔC, l'évolution de l'écart de persona *Loving* − Instruct. Il est lu par un classifieur d'une autre famille que le professeur, corrigé par (s, p) estimés par bras sur annotation humaine aveugle, et comparé à KL égale.
- **Résultat attendu (supposé).**
  - ΔC ≈ −0,2 à β = 0 : érosion, signe négatif.
  - |ΔC| < 0,1 à β_réf.
  - Érosion indiscernable entre RLVR et récompense permutée à KL égale.
  - L'écart de sycophancie sous fausse croyance garde son signe.
- **Ce qui pourrait tromper.** Le RLVR change le format des sorties, et les juges lisent ce format comme une perte de persona.
- **Contrôle.**
  - Nulle de format : Instruct avant et après le même RL.
  - Validation sur sorties post-RL réelles.
  - Notation entrelacée, juge figé.
- **Lecture d'un résultat contraire.** Si le SFT neutre efface autant que le RLVR à KL égale, « après RL » est la mauvaise question. Il faut alors étudier la persistance sous déplacement générique.
- **Coût illustratif.** ≈ 230 heures de carte et 8 jours. La porte au temps zéro, ≈ 10 heures, peut tout arrêter dès le premier jour.

**Ce qui ferait échouer le plan :**
- l'accès aux poids est refusé ;
- s entre graines dépasse ≈ 0,065, ce qui rend Duel 1 non concluant à budget tenable ;
- le classifieur ne bat pas les prédicteurs de format sur les sorties post-RL.

FIN-DE-CELLULE