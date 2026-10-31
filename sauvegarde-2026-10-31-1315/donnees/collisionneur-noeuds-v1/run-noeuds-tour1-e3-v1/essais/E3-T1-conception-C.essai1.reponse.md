**Intégrité des pièces (Règle 2)** : La pièce 10 (`calcul-puissance-pre-pilote-course-2-v6.sortie.txt`) est déclarée retirée pour budget de mots (0 mot) ; l'annexe du tour 2 (`annexe-tour-2-recommandations-v1.md`) est absente de cet envoi ; la ligne finale de la pièce N9-1 est visiblement coupée après « dans toute la population restée non ».

---

## (a) Ce que la question suppose sans que ce soit établi

- **N1** : Suppose que corriger la métrique V5 en T2 suffit à garantir qu'un bras candidat n'exploite pas l'artefact de rareté sur l'étiquette retenue par l'étage commun, alors que l'écart de fréquence entre vrai d'opérateur et proche reste d'environ 1,4 en M_bien (Pièce 2, § 3) — **HYPOTHÈSE**.
- **N3** : Suppose qu'un substitut inspiré de Gu, X. et Krenn, M. (2024, « Forecasting high-impact research topics via machine learning on evolving knowledge graphs ») fondé sur deux seuils entiers (S31 : 20 et 5) conserve un pouvoir prédictif sur un graphe du contrôle des IA — **HYPOTHÈSE**. Suppose que leur vocabulaire de 37 960 concepts ne couvre pas le contrôle des IA : ce point est en réalité **VÉRIFIÉ** dans la Pièce SD-4 (§ 5, script `couverture_vocabulaire_v1.py`).
- **N4** : Suppose que la cloche de conventionnalité des références d'un article (Uzzi, Mukherjee, Stringer et Jones, 2013, *Science* 342 — **VÉRIFIÉ** sur PDF, Pièce 13, § 5) se transpose telle quelle à une échelle discrète (1 à 5) de distance de contenu entre six niches — **HYPOTHÈSE** (marquée SUPPOSÉ en Pièce 13). Suppose une loi a priori des niches (n6 à 5 %), un accord des lecteurs à 0,7 et une probabilité de structure partagée à 0,3 — **HYPOTHÈSE**.
- **N5** : Suppose que la lecture par programme en mémoire ou journalisée au coffre (v55, Pièce 15) équivaut en sécurité épistémique à une séparation physique des clés détenues par une autre session — **HYPOTHÈSE**.
- **N6** : Suppose que les temps unitaires d'exécution permettent de tenir 5 graines en 140 h (5,8 jours) — **HYPOTHÈSE**. Suppose les garanties théoriques de PCMCI, prédiction causale invariante, DirectLiNGAM et Reisach et al. sans vérification sur PDF (marquées SUPPOSÉ, Pièce 17, DL-6 ; référence à vérifier pour les titres exacts hors Reisach) — **RAPPORTÉ**. Suppose que le décodeur appris en B-θ est injectif (Pièce 17, Nœuds ouverts § 5e) — **HYPOTHÈSE**.
- **N9** : Suppose qu'un modèle entraîné pour prédire l'impact à 3 ans (IR citations) transfère sa capacité au classement de l'apparition pure d'une arête (IR = 1) — **HYPOTHÈSE**. Suppose que conditionner la population sur la non-apparition en 2023 (option b) induit un biais strictement monotone de −0,01 à −0,05 contre le modèle — **HYPOTHÈSE**.
- **N10** : Suppose, sur la base d'un pilote sur racine d'essai (**OBSERVÉ-NON-AUDITÉ**), que l'équilibre contre un attaquant adaptatif est presque pur à classe de fonctions égale et que le levier réside dans la capacité de la classe et l'archive — **HYPOTHÈSE**. (Référence Bailey et collègues et soumission « Telltale Circuits » : référence à vérifier).

---

## Tour 1 — Avis propre par nœud et expériences décisives (b)

### N1. Bisociation à deux espaces (échec de V5)
- **Option retenue** : **Option manquante (Option B-bis)**, sinon **B** par repli.
- **Option qui manque (B-bis)** : B (V5 redéfinie en T2 + ancienne grandeur rapportée sans seuil + nouvelles graines de validation + déclaration de l'écart R1/R12), **plus** l'ajout d'une condition de monde descriptive ou d'un contrôle vérifiant que l'écart N − N_β0 reste positif sur le sous-ensemble des paires plantées **sans étiquette d'opérateur** (vrai conceptuel, faux, proche) et **hors repli**.
- **Confiance** : 0,80 (illustratif).
- **Condition de défendabilité** : Redéfinir un critère de la porte V0 après lecture n'est défendable que si (1) un diagnostic sur graines indépendantes démontre que le critère initial mesurait un mélange confondant la loi à tester (S16d) avec une loi héritée (G2) et un bruit à queue lourde (repli, erreur type de 0,29 à 0,60 pour un seuil de 0,5, Pièce 2, § 1.4 — **VÉRIFIÉ**) ; (2) le texte déclare l'écart ; (3) les graines de validation (0 à 299) sont abandonnées au profit d'une plage vierge.
- **Pire cas et garde** : Le bras N exploite l'écart de fréquence résiduel sur l'étiquette retenue (vrai d'opérateur à 3,44 contre proche à 4,93 en M_bien, Pièce 1 — **VÉRIFIÉ**) pour battre les témoins sans lire la valeur conceptuelle. *Garde* : Jugeabilité J (S14), placebos d'inertie (M_inertes, A8) et de permutation (N_PCg), complétés par la lecture stratifiée hors opérateurs de B-bis.
- **Pièce sans dépense qui trancherait (Duel N1)** : Calcul sur les 200 mondes d'essai déjà générés (indices 990000–990199, Pièce 2) de la corrélation entre le score de N (ou d1c) et le statut « opérateur sans trace ».
  - **$H_A$** : La rareté de l'étiquette d'opérateur retenue suffit à séparer vrai d'opérateur et faux ponts dans le classement de d1c.
  - **$H_B$** : Le gain de d1c sur c provient des concepts rares plantés (S16d), non de l'asymétrie des étiquettes d'opérateur.
  - **Métrique et seuil** : Écart $\Delta(\text{d1c}, c)$ recalculé en masquant les paires dont l'étiquette retenue est un opérateur exclusif (`j{t}`) ou de groupe. Seuil : borne basse à 95 % de $\Delta(\text{d1c}, c) > 0$ (seuil S14, Pièce 3).
  - **Contrôle négatif** : Miroirs de `M_inertes` sur les mêmes graines (où $\Delta(\text{d1c}, c)$ doit couvrir 0, V9).
  - **Falsification** : Si $\text{lb95} \le 0$ hors opérateurs exclusifs, $H_B$ est réfutée (le canal conceptuel seul ne porte pas J). Si $\text{lb95} > 0$ et que l'écart reste à moins de 0,5 point (illustratif) du $\Delta$ global, $H_A$ est réfutée.

### N3. Pré-pilote, décision D-j (Substitut Gu-Krenn sans reproduction)
- **Option retenue** : **Oui** (garder le bras sous forme de substitut S31 sans attendre la reproduction).
- **Confiance** : 0,85 (illustratif).
- **Pire cas et garde** : Le substitut S31 produit des paires dégénérées (bruit pur ou couverture < 0,60), gaspillant 1 fusion au pré-pilote et 4 par proposeur en course (Pièce 19, R-635 — **RAPPORTÉ**). *Garde* : Garde R5 ligne 20 et 21 (déclaration obligatoire « substitut » au manifeste à É0, arrêt si « modèle » est revendiqué, Pièce 7), réserve de couverture S27 (0,60), et filtrage en aval par l'aiguilleur et les trois juges.
- **Option qui manque** : Imposer à É0 un contrôle de non-trivialité de S31 sur la moisson : le substitut ne doit pas seulement trouver une paire notée 1 et une notée 0 (garde 20, Pièce 7), mais battre un tirage aléatoire à degré fixé sur une rétrodiction interne de la moisson (paires apparues la dernière année de la moisson).
- **Pièce sans dépense qui trancherait (Duel N3)** : Script d'essai de S31 sur la moisson existante (`donnees/moisson-openalex-v1`, Pièce SD-4, § 4.1) coupé temporellement avant la dernière année disponible.
  - **$H_A$** : La règle S31 (« jamais reliés, deux concepts actifs » aux seuils 20 et 5, Pièce 9) sélectionne des paires qui se relient l'année suivante au même taux qu'un tirage aléatoire stratifié par fréquence des concepts.
  - **$H_B$** : S31 enrichit significativement le taux d'apparition de liens l'année suivante par rapport au tirage stratifié.
  - **Métrique et seuil** : Rapport de cotes (odds ratio) d'apparition d'une arête l'année $t+1$ entre paires notées 1 par S31 à l'année $t$ et paires notées 0 appariées par fréquence. Seuil : borne basse à 95 % > 1,2 (illustratif).
  - **Contrôle négatif** : Rétrodiction inversée (prédire les arêtes de $t-1$ à partir de l'état futur, Pièce 18, § iv.1) ou permutation des étiquettes de concepts à degré constant.
  - **Falsification** : Borne basse $\le 1,2$ réfute $H_B$ (S31 est un générateur aléatoire stratifié) ; borne basse $> 1,2$ avec contrôle négatif $\approx 1,0$ réfute $H_A$.

### N4. Annexe des paramètres du bras méta et CA1-04
- **Option retenue** : **(a) Accepter le repli comme mesure au pré-pilote**, combinée à l'**option qui manque** (correction des défauts structurels CA1-01 et CA1-03 de la grille avant gel). Sur **CA1-04** : **ne pas compter les jeux de données, et retirer également du compte $s(a,b)$ les trois structures séquentielles quasi universelles** (`om_somme_cumulee_temps_arret`, `om_martingale_e_processus`, `me_test_sequentiel_cusum`, Pièce 12, § D).
- **Option qui manque** : Corriger la table de distance/canal de l'annexe pour (1) retirer `n1–n2` du profil (passer $c(n_1,n_2)$ de 1 à 2, puisque le code fusionne n1 et n2, CA1-01, Pièce 12) et (2) ouvrir un partenaire à `n5` (abaisser $e(n_4,n_5)$ ou $e(n_5,n_6)$ de 4 à 3, sinon 40 % des axes sont exclus par construction, CA1-03, Pièce 12), tout en gardant (a) (10 fiches, repli accepté et déclaré dans le nom du bras).
- **Confiance** : 0,75 (illustratif).
- **Pire cas et garde** : Le profil devient trop rare après retrait des trois structures séquentielles universelles, ou à l'inverse `n1–n2` fabrique de fausses paires « éloignées » par simple désaccord de lecteurs sur l'axe 1. *Garde* : Garde 22a (non-vacuité sur jeu d'essai synthétique de 10 fiches : au moins une paire dans le profil et une hors profil, Pièce 7) et étiquetage explicite « repli joué » dans le rapport du pré-pilote.
- **Pièce sans dépense qui trancherait (Duel N4)** : Rejeu du script de non-vacuité et de P14 (`annexe-bras-meta-v1-brouillon1.md`, Pièce 13, § 6) après retrait des trois structures séquentielles quasi universelles et correction de `n1–n2` et `n5`.
  - **$H_A$** : Sans les structures imposées par le texte I (D1 et les trois structures séquentielles), le profil s'effondre ($P(\text{zéro paire dans le profil à 10 fiches}) > 0,60$, illustratif).
  - **$H_B$** : Le profil corrigé (avec `n5` inclus et sans `n1–n2`) maintient une probabilité de trouver au moins une paire du profil à 10 fiches $\ge 0,65$ (soit $P(\text{zéro}) \le 0,35$, niveau actuel de la Pièce 12, § C).
  - **Métrique et seuil** : $P(\text{zéro dans le profil})$ sur 100 000 tirages Monte-Carlo (graine 20261101, Pièce 13) avec probabilité de structure partagée recalée hors structures universelles. Seuil : $\le 0,35$.
  - **Contrôle négatif** : Jeu d'essai synthétique où les fiches ne partagent que `jd_simulateur_fige` et `om_somme_cumulee_temps_arret` (doit donner score 0 dans le profil).
  - **Falsification** : Si $P(\text{zéro}) > 0,60$, $H_B$ est réfutée (la grille de 20 structures est trop pauvre hors structures imposées) ; si $\le 0,35$ et non-vacuité tenue sur `e01–e10`, $H_A$ est réfutée.

### N5. Orchestrateur, règle de non-lecture A21 et choix CL19
- **Option retenue** : **(b) Boîte tenue par une autre session (`session-depot`)** qui détient la clé et ne rend que « passe / nœud + comptes », sinon **(a)** uniquement sous condition d'un essai d'artefact R5 vérifiant l'absence de fuite par l'ordre des identifiants ou la mémoire.
- **Confirmation des choix de code CL19 (§ G, Pièce 14 et 15)** :
  - **Choix 1** : **Confirmé** (arrêt au premier « non mesuré », ni fin d'É9 ni ouverture de clé en v55, conforme à O12).
  - **Choix 5** : **Confirmé** (un témoin N dont le relecteur ne voit pas le défaut est exclu et compte dans A5 : un témoin N sans défaut visible invalide l'étalonnage des juges).
  - **Choix 8** : **Confirmé** (à $n=2$, aucun report au bras suivant, lecture littérale de la garde 16, Pièce 7).
  - **Choix 10** : **Confirmé** (les définitions exactes des indices de forme S18/S19 et la pénalité de crête `ridge` doivent être gelées dans le texte du préenregistrement, non laissées au code).
  - **Portée du plafond (CL18-11)** : S17 par génération pour le pré-pilote ($N=1$) ; plafond global séquencé pour la course ($N>1$, aligné sur le devis v6, Pièce 20).
- **Confiance** : 0,90 (illustratif).
- **Pire cas et garde** : Sous (a), bien que la v55 supprime la copie en mémoire et trie É6 par identifiants opaques (Pièce 19, R-685 — **RAPPORTÉ**), un bug de l'orchestrateur lit le journal du coffre ou reconstruit les classes par effet de bord avant É9. *Garde* : Garde R5 ligne 30 étendue à « toute lecture hors journal ou fuite d'identifiant trié par classe ». Sous (b), la séparation est physique par construction.
- **Option qui manque** : Chiffrement asymétrique ou hachage salé des classes où l'orchestrateur exécute un binaire scellé en sous-processus isolé sans accès mémoire partagé, évitant l'intervention manuelle de `session-depot` en cours de run.
- **Pièce sans dépense qui trancherait (Duel N5)** : Contre-lecture CL20 de la v55 (annoncée non faite en R-685, Pièce 19) avec test de mutation sur `_boite_e5` et `etape_e6_juges`.
  - **$H_A$** : En v55, la trajectoire d'exécution de É6 à É9 (ordre des appels, arrêts A3, sacrifices A1) est strictement invariante par permutation des classes P/N/C/G dans la clé scellée (une fois la décision binaire d'É5 passée).
  - **$H_B$** : Une dépendance résiduelle à la clé des classes subsiste dans l'état de l'orchestrateur après É5 (comme le tri de `primaires_non_ambigus` relevé en v54, Pièce 14, § A21.3c).
  - **Métrique et seuil** : Différence bit à bit des journaux d'appels d'É6 à É9 sur deux runs simulés avec clés de classes permutées (à décision d'É5 forcée à « passe »). Seuil : 0 octet de différence.
  - **Contrôle négatif** : Run v54 (où l'ordre d'É6 dépendait de la classe, Pièce 14, § A21.5 — **VÉRIFIÉ**).
  - **Falsification** : Toute différence $> 0$ octet réfute $H_A$ et impose (b) ; 0 différence sur 100 permutations aléatoires réfute $H_B$ et valide techniquement (a).

### N6. Épreuve semi-réelle d'identification causale (DL-1 à DL-9)
- **Options retenues** :
  - **DL-1** : **(2)** B-θ décide, B-hors en descriptif (30 mondes). Tester l'iVAE uniquement hors des hypothèses du théorème de Khemakhem et collègues (2020 — **VÉRIFIÉ** sur PDF, Pièce 17) ne réfute rien en cas d'échec.
  - **DL-2** : **(2)** 5 graines, S15 = 140 h (10 paires de graines pour la stabilité, marge de 1,26× avant réduction, Pièce 17).
  - **DL-3** : **(2)** R2⁻ en condition descriptive (la puissance en R2⁻ n'étant pas égale à celle de R2 à cause du fond ajouté à 90 % des paires-années, Pièce 17, S20, un échec en décision confondrait manque de puissance et asymétrie de signe).
  - **DL-4** : **(1)** CITRIS hors de la gradation 1 (lui donner la cible C tue l'épreuve d'identification).
  - **DL-5** : **(1)** Moitiés coupées par paire, graine choisie par perte sur $E_1$ sans vérité, table d'effet séparée à règle de Wilson ($\ge 37/50$, $\le 2/50$).
  - **DL-6** : **(1)** Obtenir et lire les PDF manquants avant le gel (exigence R7).
  - **DL-7** : **(2)** Arbitrer explicitement S3, S8, S9, geler le reste en bloc.
  - **DL-8** : **(1)** Échelle de trois définitions ($u_1, u_2, u_3$) écrite d'avance, la première atteignant 22 valeurs (dissout la question de lecture R1 avant scellement, $u_2 = 36$ sur la base minimale, Pièce 17, S19).
  - **DL-9** : **(1)** Redéfinir T2b sur la règle d'orientation de chaîne de Reisach et al. (PDF p. 9 — **VÉRIFIÉ**, Pièce 17) limitée aux conditions O, **sous réserve** d'étalonner les seuils 0,20 et 0,05 après lecture du PDF complet (DL-6).
- **Confiance** : 0,80 (illustratif).
- **Pire cas et garde** : Les temps unitaires réels dépassent 1,57× les temps supposés, provoquant un arrêt à 140 h avant les mondes de décision (Pièce 17, DL-2). *Garde* : Règle de réduction chiffrée du préenregistrement et étape de validation/gardes initiale (≈ 4 h, Pièce 17, § 8) qui mesure le temps unitaire réel avant de lancer les 200 mondes.
- **Option qui manque** : En DL-2, un arrêt-pilote chronométré sur les 5 mondes de validation permettant d'activer la réduction du nombre de mondes descriptifs avant d'entamer le budget des mondes de décision. En DL-3, calibrer la variance du fond en R2⁻ pour égaliser le rapport signal-bruit avec R2.
- **Pièce sans dépense qui trancherait (Duel N6)** : Intégration de la synthèse des 10 cellules valides de la Question 6 (Pièce SD-1 — **VÉRIFIÉ**) et banc d'étalonnage de temps et de puissance R2 contre R2⁻ sur un monde jouet purement synthétique (hors `donnees/`).
  - **$H_A$** : À taille d'effet $|\beta| = 0,20$ égale, le rapport signal-bruit en R2⁻ (retrait sur fond ajouté à 90 %) abaisse la puissance de détection d'un oracle linéaire de plus de 10 points par rapport à R2.
  - **$H_B$** : La puissance de l'oracle linéaire en R2⁻ reste à moins de 5 points de celle de R2.
  - **Métrique et seuil** : Écart de taux de détection à $\alpha = 0,05$ entre R2 et R2⁻ sur 1 000 mondes synthétiques calibrés sur la loi marginale de Poisson du script de règles (`calcul-regles-identification-semi-reel-v1-brouillon3.py`, Pièce 17). Seuil : écart $\le 0,05$.
  - **Contrôle négatif** : Jumeau sans effet $C^0$ ($\beta = 0$, taux de détection attendu $\approx \alpha$).
  - **Falsification** : Écart $> 0,10$ réfute $H_B$ (interdit DL-3 option 1 en décision sans recalibrage) ; écart $\le 0,05$ réfute $H_A$ (autorise DL-3 option 1).

### N9. Gu-Krenn, décision D-GK-1 (Fenêtre du test hors échantillon HB)
- **Option retenue** : **(a) Population à fin 2022, fenêtre 1er janvier 2023 – 30 septembre 2026** (l'option (b) étant rapportée en information).
- **Confiance** : 0,90 (illustratif).
- **Pire cas et garde** : La dérive de la base OpenAlex (« Walden », novembre 2025, retraits/récupérations de résumés, Pièce SD-4, § 4.5 — **RAPPORTÉ**) crée un artefact d'apparition d'arêtes dès 2023 qui gonfle ou dégrade artificiellement B-i et B-ii. *Garde* : Étape B2 de « pont » (reconstruire avec la moisson actuelle les arêtes 2020–2022 et vérifier la concordance des comptes avec leur graphe publié avant d'évaluer 2023–2026, Pièce SD-4, § 4.5) et appariement strict sur le degré et l'âge à fin 2022 (B-ii).
- **Option qui manque** : Évaluer sur la population non conditionnée à fin 2022 (comme en a), mais décomposer la courbe de survie/apparition par tranche annuelle (2023 seul, 2024 seul, 2025–2026) avec hasard proportionnel ou test de maintien du classement à horizon croissant, sans filtrer la population sur l'issue 2023.
- **Pièce sans dépense qui trancherait (Duel N9)** : Simulation analytique ou sur le graphe publié 2016→2019 / 2019→2022 (déjà dans `data_for_features`, Pièce SD-4, § 4.2, sans ouvrir `frp_example.zip`) de l'effet de troncature de la première année d'évaluation (retirer les paires reliées en 2020 pour évaluer 2021–2022).
  - **$H_A$** : Retirer de la population d'évaluation à $y=2019$ les paires qui se relient dès $y+1$ (2020) induit un biais de sélection (collisionneur sur la survie à non-liaison) qui abaisse l'aire appariée d'un prédicteur monotone de plus de 0,03.
  - **$H_B$** : L'aire appariée sur 2021–2022 après retrait des liées de 2020 reste invariante (écart $< 0,01$ par rapport à l'évaluation 2020–2022 complète).
  - **Métrique et seuil** : $\Delta \text{AUC}_{\text{appariée}} = \text{AUC}(2020\text{–}2022) - \text{AUC}(2021\text{–}2022 \mid \text{non lié en } 2020)$ calculée avec les règles gratuites (attachement préférentiel et similarité de Simpson seule, Pièce N9-1) sur leur graphe 2019–2022. Seuil : $|\Delta \text{AUC}| > 0,03$.
  - **Contrôle négatif** : Retrait aléatoire uniforme du même nombre de paires positives (qui doit laisser l'espérance de l'AUC exactement invariante).
  - **Falsification** : Si $\Delta \text{AUC} > 0,03$ alors que le retrait uniforme donne $\approx 0$, $H_B$ est réfutée (la fenêtre littérale (b) biaise mécaniquement le test contre le modèle).

### N10. Course d'idéation et robustesse contre un attaquant adaptatif
- **Option retenue** : **(b) Poser la question en génération 2** pour le plan de base, **combinée à (c) préparée en parallèle** (rédiger dès maintenant le préenregistrement et le devis d'une sous-session dédiée « robustesse adaptative », déclenchée immédiatement après la course 2 ou en génération 2 si le calcul décisif du pilote confirme l'effondrement sur racine de décision). Le mot du directeur (v10) ne justifie pas (a), car rouvrir le texte I (11 700 caractères) invaliderait les empreintes du pré-pilote (A16, Pièce 7) et diluerait les 24 fusions.
- **Pistes méthodes à chercher (leviers que l'attaquant ne contrôle pas à bas coût)** :
  1. *Invariants de coût asymétrique sur la trajectoire* : forcer l'attaquant qui minimise le score d'un moniteur d'activations à dégrader sa propre utilité dans la tâche ou à allonger la trace séquentielle (couplage de la voie 3 « détection × coût » de R-880, Pièce N10-2, avec les tests séquentiels à horizon mobile).
  2. *Moniteurs sur sous-espaces fonctionnels causaux nécessaires à l'exécution* : au lieu de lire des directions linéaires passives (contournables par l'optimiseur sur un 8B, Pièce N10-2), lier la sonde aux sous-espaces dont l'ablation détruit la capacité d'exécution de l'attaque (intervention causale / patching en ligne).
  3. *Accumulation séquentielle de preuves à mémoire d'archive (e-processus sur familles)* : même si chaque instance contourne le seuil ponctuel, tester la dérive de la distribution des entrées ou des activations par rapport à la loi honnête $P_0$ (plancher de variation totale $\text{TV}(P_f, P_0) \ge \eta_{\min}$, Pièce N10-1, § 2.7).
- **Confiance** : 0,85 (illustratif).
- **Pire cas et garde** : La génération 1 de la course 2 produit 24 fusions de moniteurs statiques que l'attaquant adaptatif (protocole de Bailey et collègues, R-880) contourne à 100 % lors de l'examen final. *Garde* : L'axe 3 (failles du programme) et l'axe 7 (angles non occupés) de la génération 1 restent ouverts ; le banc instrumental de l'arène (Pièce N10-1, § 2.10) filtre les architectures avant dépense GPU.
- **Option qui manque** : Injecter le résultat du pilote synthétique et la contrainte d'attaquant adaptatif comme **critère d'attaque au bras d'attaque / tests de mort** à la sortie de la génération 1, pour sélectionner les survivantes qui passent en génération 2 sans modifier le texte I d'entrée.
- **Pièce sans dépense qui trancherait (Duel N10)** : Exécution du calcul décisif du pilote synthétique « mélange d'équilibre » (brouillon 3, sur processeur, 0 USD) à classe de fonctions égale contre un optimiseur adaptatif.
  - **$H_A$ (Hasard utile)** : À capacité totale de paramètres et classe de fonctions égales, un mélange stochastique de moniteurs à l'équilibre de Nash abaisse le taux d'évasion de l'attaquant adaptatif d'au moins 10 points (illustratif) par rapport au meilleur moniteur déterministe unique (« ou » logique ou réseau unique).
  - **$H_B$ (Capacité et archive seules)** : À classe de fonctions égale, l'avantage du mélange stochastique sur le moniteur déterministe unique est inférieur à 2 points (illustratif) ; seul l'élargissement de la classe de fonctions sur l'archive des attaques réduit l'évasion.
  - **Métrique et seuil** : Rappel au pire cas certifié $L = \min_m [\hat{R}_{\text{LCB}}] - L_{\text{Lip}}\cdot h - \varepsilon_{\text{cal}}$ (Pièce N10-1, § 2.5) à taux de fausses alertes fixé sur le troisième jeu honnête disjoint (§ 2.4). Seuil de supériorité : $\Delta L \ge 0,10$.
  - **Contrôle négatif** : Bras réétiquetés (permutation des étiquettes de bras sur la trajectoire commune du générateur, Pièce N10-1, § 1 et § 2.1).
  - **Falsification** : Si $\Delta L < 0,02$, $H_A$ est réfutée (confirme l'observation du pilote sur racine d'essai et déclenche la recherche de nouvelles pistes en génération 2 / sous-session c) ; si $\Delta L \ge 0,10$, $H_B$ est réfutée.

---

## Tour 2 — Attaque des recommandations

Conformément à la règle d'intégrité 2 et aux consignes de la question (« Les recommandations des auteurs des pièces sont servies dans un second envoi, après réception du tour 1 (fichier `annexe-tour-2-recommandations-v1.md`) » ; dans les pièces jointes, toute recommandation a été remplacée par « `[retiré, règle 2 : recommandation ou confiance d'auteur]` »), le fichier `annexe-tour-2-recommandations-v1.md` est absent de cet envoi.

Deux seules recommandations résiduelles figurent en clair dans le texte de la Question de l'arbitre :
1. **N9 (D-GK-1, option a recommandée par `session-depot`)** : **Tenue**, car elle évite le biais de sélection par conditionnement sur l'issue intermédiaire 2023 (testé par le Duel N9).
2. **N10 (option b recommandée par `conv-audit`, confiance 0,55)** : **Tenue sous condition** que le préenregistrement d'une sous-session dédiée (c) ou le dossier de génération 2 intégrant les leviers d'invariance causale et de coût asymétrique soit préparé dès la confirmation du pilote synthétique, sans toucher au texte I de la course 2.
3. **N1, N3, N4, N5, N6** : **Indécidable sans la pièce `annexe-tour-2-recommandations-v1.md`** (non servie à ce tour).

---

## (c) Mesure minimale de validité des instruments nommés

| Instrument | Taux de détection et fausses alertes exigés | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Générateur et porte V5 / J (N1)** | Écart inter-statuts sur concepts rares (T2) $\le 0,5$ (S13) ; plafond de l'oracle $\ge 0,30$ (S8) ; jugeabilité $J : \text{lb95 }\Delta(\text{d1c}, c) > 0$ en M_bien et M_moyen ; fausse alerte sur `M_inertes` $\le 0,02$ à effet nul (V9, Pièce 3). | 300 mondes M_bien, 300 M_moyen et 300 miroirs `M_inertes` partageant exactement les mêmes latents bit à bit (rôles 0 à 3, Pièce 3). | Tirage uniforme $c$, stratifié par domaine $b$, et Swanson par opérateur $d_1$ ($\text{lb95 }\Delta(N, d_1) > 0$, A2). |
| **Substitut Gu-Krenn S31 et Moissonneur (N3, N9)** | Garde 17 : 100 % des références réelles (PDF empreinté) trouvées, 0 % des références inventées (Pièce 7). Pour HB (N9) : $\text{B-i} \ge 0,85$, $\text{lb95 B-ii} > 0,60$, $\text{lb95 B-iii} > 0$ (Pièce N9-1). | Pour chaque paire positive reliée dans la fenêtre, $k=5$ paires négatives tirées dans la même case de quantile de degré (bas, haut) et d'âge à fin 2022 (Pièce SD-4, § 4.4 ; Pièce N9-1, B4). | Attachement préférentiel (produit des degrés) et similarité de Simpson seule sur le même échantillon apparié (B-iii). |
| **Lecteurs de niches / structures et score méta (N4)** | Accord inter-lecteurs S28 : $\kappa \ge 0,40$ sur les niches, Jaccard moyen $\ge 0,30$ sur les structures (Pièce 13). Garde 22a : $\ge 1$ paire dans le profil et $\ge 1$ hors profil sur les 10 fiches synthétiques. | Jeu d'essai synthétique de 10 fiches (`e01` à `e10`, 45 paires dont 5 dans le profil, 36 hors profil, 4 de même niche refusées, Pièce 13, § 6). | Bras basique (loin en domaine, proche en concept, S24) et tirage aléatoire sur paires de niches distinctes. |
| **Orchestrateur, Coffre et Boîte É5 (N5)** | Contrôles de forme : aire sous la courbe (ROC AUC) témoins / Kimi $\le \text{S18}$ (0,75 en R-2) et P / N par la forme $\le \text{S19}$ (0,70 en R-3) (Pièce 9). 0 ouverture de clé hors journal avant la fin d'É9 (garde 30, Pièce 7). | 28 squelettes rendus (et 4 appariés sous D-i (2)), 23 témoins primaires (au moins 8 P et 10 N, au plus 4 ambigus, S20, Pièce 7 et 14). | Régression logistique à pénalité de crête (`ridge`) sur longueur, nombre de chiffres et nombre de champs (doit donner AUC $\approx 0,5$ sur cas sain et $\approx 1$ sur artefact P à 6 500 contre N à 3 500 caractères, garde 27, Pièce 7). |
| **Méthodes d'identification causale M1–M5 et T2b (N6)** | Recouvrement de la cause plantée $C$ selon le seuil S9 ; étape d'effet B-θ : $\ge 37/50$ mondes détectés et $\le 2/50$ fausses détections (règle de Wilson, DL-5, Pièce 17) ; fausse détection globale bornée à $\alpha = 0,0069$ (borne binomiale exacte, Pièce 17, § 7). | Paires de niches d'OpenAlex coupées en deux moitiés disjointes par paire ($E_1$ sélection, $E_2$ test, S21), avec jumeau sans effet $C^0$ (même loi d'affectation que $C$, effet nul) et leurre collisionneur $L$ (Pièce 17). | Témoins T0 (popularité seule, Poisson pénalisé), T1 (forêt d'arbres par gradient), T2 (`sortnregress`, tri par variance + Lasso BIC) et T2b (orientation de chaîne de Reisach, échelles brute et standardisée, Pièce 17). |
| **Banc de certification et moniteurs d'arène (N10)** | Taux de fausses alertes tenu sur le jeu d'évaluation ($\text{FPR} \le 1,5\%$ chez B, Pièce N10-1, § 2.6) ; continuité $L_{\text{Lip}}\cdot h \le 0,10$ sinon certificat « NON DÉLIVRÉ » (§ 2.3) ; test de permutation sur $P=8$ paires de graines appariées (plancher $p = 1/256 \approx 0,004$, § 2.2). | Trois jeux honnêtes disjoints tirés de $P_0$ (calibration du seuil, évaluation du FPR, test de rappel / contrôles, § 2.4) et familles d'attaques admissibles vérifiant $\text{TV}(P_f, P_0) \ge \eta_{\min}$ (§ 2.7). | Moniteur déterministe unique (« ou » logique / réseau unique à budget de paramètres égal) et base « instances seules » au protocole de Bailey et collègues (Pièce N10-2, R-880). |

---

## (d) Ancrage matériel, modèles, calcul et coûts

- **N1 (Bisociation v2)** : Processeur seul, aucun appel de modèle, **0 USD** (Pièce 3, S15 — **VÉRIFIÉ**). Diagnostic V5 sur 400 mondes : $\approx 50\text{ s}$ sur `python3` (Pièce 2). Run complet de décision : 16 200 mondes (jusqu'à 23 400 avec extension S9), quelques minutes à quelques heures de processeur local (illustratif).
- **N3, N4, N5 (Pré-pilote et Course 2)** :
  - *Modèles* : Kimi K3.1 Pro, Gemini 4 Argon, Claude Opus 5.5, Claude Sonnet 5.5 (tiers T), Claude Fable 5.1 (relecteur) (Pièces 4, 9, SD-1 — **VÉRIFIÉ**).
  - *Coûts* : Pré-pilote plafonné à **50 USD** (arrêt d'étape 45 USD, dépense médiane tirée 40,6 USD, moyenne 40,3 USD, Pièce 11, § 3.3 et Question v5 — **VÉRIFIÉ**). Course 2 (4 sous-sessions, 24 fusions) : attendue aux bases 117,9 USD, moyenne tirée 139,2 USD, plafond total séquencé tranché à **160 USD** (Pièce 11 et Question — **VÉRIFIÉ**). Script P14 de l'annexe méta (100 000 tirages `numpy` 2.5.3) : processeur local, **0 USD**, $< 5\text{ s}$ (illustratif).
- **N6 (Identification semi-réelle, gradation 1)** : Processeur seul (`python3`, `tigramite`, `lingam`, `scikit-learn`, `scipy`, `statsmodels`, `torch`), **0 USD** de dépense d'API (Pièce 17 — **VÉRIFIÉ**). Budget de calcul sous DL-2 option 2 (5 graines) : **$\approx 107\text{ h}$** de calcul de base, **$\approx 111\text{ h}$** avec validation et gardes, plafond S15 = **140 h** (5,8 jours de temps mural continu avant fin novembre 2026, Pièce 17 — **RAPPORTÉ**).
- **N9 (Gu-Krenn reproduction et hors échantillon)** :
  - *Données* : Zenodo 9,5 + 17,8 Go ; instantané public OpenAlex 744 Go en Parquet (ou API > 50 000 pages de filtre soit $> 5\text{ USD}$ / plus d'une semaine d'allocation gratuite de 1 USD/jour) ; disque libre local de 9 Go insuffisant (Pièce SD-4, § 4.3 et Pièce SD-3, R-873 — **VÉRIFIÉ**).
  - *Calcul et coût* : Réentraînement obligatoire (8 à 30 h de processeur par valeur d'IR ou carte graphique) exigeant une machine louée : coût de carte graphique estimé entre **10 USD** (ordre de grandeur de la machine jetable v2 : 0,5 USD attendu, 7,4 USD au pire, GO proposé 10 USD, Pièce SD-3, R-866) et **300–1 000 €** selon l'estimation de B en synthèse (Pièce 18, § iii.2 — **RAPPORTÉ** ; fourchette 20–50 USD illustratif pour 3 graines sur GPU loué à l'heure).
- **N10 (Pilote mélange d'équilibre et Examen final P-041)** : Pilote synthétique sur processeur : **0 USD**. Examen final (optimiseur sur les entrées d'un modèle ouvert 8B contre défense figée, Pièce N10-2, R-880 et R-890) : nécessite location de GPU (devis séparé non engagé, coût illustratif de 15 à 80 USD selon le nombre de pas d'optimisation et les $P=8$ paires de réplications).

---

## Liens entre nœuds et ordre optimal de décision pour le directeur

1. **Lien N4 $\rightarrow$ N5 $\rightarrow$ N3 (Chemin critique du gel du pré-pilote)** : Le directeur ayant tranché D-h (a) (attendre l'annexe scellée du bras méta, Question v6), **le gel du pré-pilote est bloqué par N4** (correction de `n1–n2`, inclusion de `n5`, retrait des 3 structures séquentielles universelles en CA1-04) et par **N5** (amendement d'A21 ou boîte externe, et gel des formules de S18/S19 dans le texte du brouillon 8). **N3 (D-j = oui)** débloque immédiatement l'essai de S31 sur la moisson existante (É0), sans attendre **N9**.
2. **Lien N1 $\leftrightarrow$ Décision 1 de la synthèse (Six garde-fous, Pièce 18)** : L'échec de V5 en N1 est la manifestation exacte en monde synthétique de la violation du premier garde-fou de la synthèse (« une étiquette de pont indépendante du canal ») : l'étage commun retient l'étiquette la plus rare, qui pour les ponts d'opérateur dépend du mécanisme de plantation (jumeau à fréquence 2). Adopter **B-bis** en N1 applique ce garde-fou sans retarder l'expérience v2.
3. **Lien N8 (tranché) $\rightarrow$ Synthesis Question 6 $\rightarrow$ N6** : L'absence de Kimi étant acceptée (Pièce SD-1, 10 cellules valides sur 12), la synthèse de la Question 6 peut être écrite immédiatement. Or le brouillon 3 de **N6** comporte une section bloquante « À intégrer après le verdict du collisionneur sur la question 6 » (Pièce 17, l. 687). Le directeur peut trancher **DL-1 à DL-9** dès maintenant (en particulier **DL-6 = obtenir les 4 PDF**), pendant que la synthèse de la Question 6 est intégrée au brouillon 4 de N6, afin de lancer les 5,8 jours de calcul avant la porte G0 de fin novembre.
4. **Ordre séquentiel recommandé au directeur** :
   - **Pas 1 (Immédiat, débloque le pré-pilote)** : Trancher **N3** (D-j = oui), **N4** (option a + correction grille CA1-01/03 + retrait des 3 structures séquentielles en CA1-04) et **N5** (option b ou a avec CL20 + confirmation des choix 1, 5, 8, 10).
   - **Pas 2 (Immédiat, débloque les calculs processeur et la procuration des sources)** : Trancher **N1** (option B-bis sur nouvelles graines) et **N6** (DL-1 à DL-9, en versant les PDF de DL-6 pendant que la synthèse de la Question 6 se termine).
   - **Pas 3 (En parallèle, chantiers sur machine louée et génération 2)** : Trancher **N9** (D-GK-1 = option a) et **N10** (option b + préparation du préenregistrement de c après le calcul décisif du pilote synthétique).

FIN-DE-CELLULE