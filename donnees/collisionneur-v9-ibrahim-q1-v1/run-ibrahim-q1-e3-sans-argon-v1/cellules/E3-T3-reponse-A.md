# Cellule A — Tour III.3 : réponse aux critiques

**Statuts.** Les faits des trois pièces restent **RAPPORTÉS** (lus sur page primaire par un rédacteur, non audités par moi) ; je ne tranche pas l'écart signalé par B entre mon classement (RAPPORTÉ) et celui de D (OBSERVÉ-NON-AUDITÉ) pour les chiffres des dépôts de Lazar, je le laisse à l'arbitre. Les critiques reçues sont des HYPOTHÈSES de méthode ; mes réponses aussi. Les chiffres non issus des pièces sont « illustratifs », « supposés » ou « calcul ». La pièce C est absente (jamais lancée) : rien à répondre.

Je ne réponds qu'aux sections visant A. Quand B, D et E font la même critique, je la traite une fois et renvoie.

---

## (a) Réponse critique par critique

### Critiques de B

**B1 — Statut de l'accès aux poids OCT.** *Acceptée.* La pièce dit « accès filtré annoncé, non vérifié » (pièce Ibrahim §3) : c'est une annonce RAPPORTÉE, personne n'a observé l'accès. Je corrige mon point (a)5 : RAPPORTÉ, et « poids inaccessibles » reste la première cause d'échec du plan.

**B2 — E1 : duel non exhaustif, seuil incohérent (≥ +11 contre 5), portée du +11 non établie.** *Acceptée sur les trois points* (même critique chez D, premier tiret, et E, « VÉRIFIÉ »). Le duel conjoint « erreur **et** g » laissait trois issues sans hypothèse. Correction en (b) : deux duels à un paramètre chacun, chacun avec une région « indécis » (règle d'E, reprise en le disant). Le « +11 » (*Nature* p. 1163, RAPPORTÉ, portée non établie, pièce Ibrahim §4) ne sert plus d'attendu pour Llama-3.1-8B ; il ne reste qu'un ordre de grandeur cité. Le seul chiffre du papier propre au 8B est −15,06 sous tristesse + fausse croyance (tableau E5, prépublication v2, RAPPORTÉ, non revérifié dans *Nature*) ; je ne l'utilise pas comme attendu non plus, car il combine deux manipulations.

**B3 — Δg ≥ 0,2 étiqueté « calcul » alors que c'est un choix ; variance inter-points-de-contrôle plus grande ; puissance ≈ 50 %.** *Acceptée.* Je réétiquette : δ_g = 0,2 est un **effet minimal d'intérêt supposé**, pas un calcul. Le dimensionnement devient une cible de demi-largeur d'intervalle de 0,1 sur le contraste entre points de contrôle ; sous l'hypothèse de B (variance au moins double d'un contraste intra-modèle, demi-largeur 0,21 à 450 générations par dose dans R6, calcul à partir de 1 350 = 3 doses × 450, pièce sycophancie §1), il faut environ 4 à 8 fois plus de générations par bras, soit 1 800 à 3 600 par bras et par dose (calcul, illustratif). Je l'inscris au budget d'E1.

**B4 — Le contrôle par consigne système prouve autre chose.** *Acceptée* (même point chez D et E). Égalité des déplacements entre persona entraînée et base consignée montre une équivalence de deux interventions, pas que le juge lit le style. Et une sortie réellement chaleureuse classée *Loving* est une détection, pas une fausse alerte : B a raison, ma définition en (c) confondait « style induit par consigne » et « absence du construit ». Correction : le vrai négatif devient la **paire contenu/style** (même position, style varié ; même style, position variée), annotée par des humains (contrôle B(c)1 = D(c)1 = E(c) « persona versus style », repris en le disant). Le bras consigné est conservé, mais comme question distincte (« la consigne reproduit-elle l'effet de l'entraînement ? »), sans inférence sur l'instrument.

**B5 — Fuite entre construction de l'instrument et évaluation ; la troncature est elle-même un artefact.** *Acceptée.* Le classifieur OCT est à base de modèles avec biais et circularité déclarés (pièce Ibrahim §2) ; toute dérive de format sous RLVR se lirait comme érosion. Correction : banque de validation **réservée**, construite en deux phases (avant RL ; après RL, sur sorties post-RL réelles, avant toute levée d'aveugle sur E2), avec paires contenu/style. La concordance tronqué/entier est **abandonnée** : E a raison qu'elle peut accepter deux instruments biaisés ; l'analyse principale porte sur les sorties entières.

**B6 — Régression vers la moyenne dans ĝ.** *Transformée en test.* La pièce sycophancie ne dit pas si R6 estime v₀ sur des tirages disjoints de ceux de Δ ; je ne le suppose pas. Correction : v₀ estimé sur une moitié des tirages, Δ sur l'autre (division fixée d'avance) ; **dose nulle placebo** (deux lots sans pression, même estimateur) qui doit donner ĝ ≈ 0 ; simulation avec l'atténuation d'E, ĝ → (g·Var(V) + Var(ε)) / (Var(V) + Var(ε)), alimentée par la variance entre tirages mesurée sur le modèle réel. Si le placebo donne ĝ hors de [−0,1 ; 0,1] (supposé), l'instrument g est déclaré non utilisable pour cette persona.

**B7 — E2 : la falsification ne suit pas (H_B par rétention seule ; R8 non réfuté ; R8 vise Tülu 3 ; zone 50–80 % vide).** *Acceptée* (même point chez D, quatrième tiret, et E). Je retire la prétention de « réfuter l'a priori R8 ». E2 teste la **condition S3** (« RLVR ne change pas g », pièce sycophancie §2, préenregistrée, non exécutée) sur une **autre chaîne** (OCT, déjà passée par DPO) : c'est un test de généralité, pas une réfutation ; un Δg ≥ δ sous RLVR contredirait seulement une version exclusive de « le gain vient de l'optimisation des préférences ». E2 est scindé en deux duels à un paramètre, sans zone vide (voir (b)).

**B8 — Persistance vraie par construction si le RLVR ne bouge presque pas la politique.** *Acceptée, transformée.* L'axe de dose devient la **divergence KL mesurée sur les prompts d'évaluation** (persona et sycophancie), avec arrêt à trois cibles de KL, et non un nombre de pas ; un départ qui n'atteint pas la cible minimale rend son bras non jugeable.

**B9 — E3 : facteurs confondus, paires rééquilibrées = troisième modalité, seuil d'interaction sous-dimensionné.** *Acceptée.* Le modèle de récompense rééquilibré est une intervention, pas un contrôle (D le dit aussi) ; le contrôle négatif devient le modèle de récompense **à préférences permutées** (B(c)5, repris en le disant), apparié en KL. L'interaction passe au second plan : E montre que mon duel annonçait des effets principaux et testait une interaction ; E3 teste désormais l'effet principal de l'étape sur g et F, persona en bloc. Le facteur √2 de B sur l'interaction est accepté comme calcul.

**B10 — Dérive du juge (alias non figé).** *Acceptée.* Jeu d'ancrage rejugé à chaque passe (B(c)4) ; sorties avant/après mélangées dans les mêmes lots de jugement ; juge principal à version figée : un juge à poids ouverts d'une autre famille est déjà nommé dans les préenregistrements R1a/R1b (Qwen2.5-72B, pièce sycophancie §1, RAPPORTÉ) ; GPT-4o et Claude en juges secondaires.

**B(b) — Fieller, saturation, Var(v₀) → 0, déplacement constant, refus, graines.** *Acceptés.* Rétention : la **différence brute** (contraste persona–base après moins avant) devient l'analyse principale, le ratio est secondaire et n'est publié que si l'intervalle de C_avant exclut 0 (même exigence chez D et E). Saturation du classifieur : critère d'arrêt écrit d'avance en E0. Gain : le modèle d'attraction est opposé au modèle à déplacement constant (cas Qwen/Mistral en R3, pièce sycophancie §1) avant toute lecture de g. Refus : analyse principale avec le refus comme **catégorie explicite** (E(c), D(b)) ; analyse secondaire avec exclusion commune par item fixée sur l'union des bras (B) ; je note que cette seconde règle conditionne encore sur une variable post-traitement, symétriquement, d'où son rang secondaire. Graines : K = 3 entraînements par cellule ; j'accepte le calcul de B/D (t à 2 degrés de liberté ≈ 4,30, facteur ≈ 2,2) et je le prends comme coût ; K = 5 si le budget le permet (illustratif).

**B(c)3 — Test-retest à la place de l'autodistillation.** *Acceptée comme ajout, rejetée comme substitution.* Le test-retest d'un point de contrôle gelé mesure le plancher de bruit de l'instrument ; l'autodistillation mesurait l'exposition aux prompts. Ce sont deux rôles. Mais D a raison que l'autodistillation n'apparie ni gradients ni distance : elle est rétrogradée en bras secondaire, et le témoin principal devient la récompense non informative appariée en KL (D(c)2, E(c) « effet propre du RL »).

### Critiques de D (points non encore traités)

**Information de construit I(Y;Ŷ | X,Z,T) > 0 et non-transport des taux avant/après.** *Acceptée, transformée.* La banque réservée de E0 contient des paires contenu/style **post-RL** ; détection et fausse alerte sont réestimées dans le régime post-RL, pas transportées.

**Corrélations intra-item / intra-graine : taille effective inférieure au nombre de générations.** *Acceptée.* Modèle hiérarchique (item, graine d'entraînement, tirage) pour tous les intervalles ; aucun intervalle calculé sur générations indépendantes.

**Dépasser un lexique en AUC n'établit pas que le classifieur lit autre chose que Z.** *Acceptée* (E le formalise : égalité d'AUC n'implique pas égalité de lois). Correction : le classifieur est testé **conditionnellement** sur les paires de E0 (à style constant, sépare-t-il les positions ? à position constante, le style ?). Le résultat dit ce que l'instrument lit, dans l'un ou l'autre cas ; un instrument qui ne lit que le style reste utilisable pour mesurer la persistance **du style**, à condition de le nommer ainsi.

**Croyance correcte et assertion fausse de source impersonnelle (D(c)3).** *Acceptée.* La pièce Ibrahim ne dit pas si la tâche de désinformation du papier chaleur contient ces contrastes ; ils sont à construire sur les mêmes items.

### Critiques d'E (points non encore traités)

**c = a/g non borné si g plausible contient 0.** *Acceptée.* Le point fixe n'est rapporté que si l'intervalle de ĝ exclut 0 ; sinon seul le déplacement moyen est publié.

**Sondes : AUC de construction sans borne sur l'AUC d'évaluation.** *Acceptée.* Les sondes restent hors du plan principal ; si on les ajoute, AUC sur un point de contrôle jamais vu et plancher de sondes aléatoires appariées (procédé P3, pièce nos-résultats §6, RAPPORTÉ), sur lots réservés.

**Rien n'est rejeté sur le fond** ; les deux rejets partiels (B4 sur la définition de fausse alerte, B(c)3 sur la substitution) sont notés ci-dessus avec leur raison.

---

## (b) Expériences corrigées

Modèle : Llama-3.1-8B-Instruct ; points de contrôle OCT *Loving*, *Sycophantic* (pièce Ibrahim §3, accès RAPPORTÉ non vérifié). Toutes les règles de décision, seuils et divisions d'échantillon sont écrits avant toute génération ; verdict « indécis » si l'intervalle (modèle hiérarchique) chevauche le seuil.

### E0 — Instruments (nouveau ; conditionne tout)

*Mesure.* Banque réservée en deux phases : (i) avant RL, 300 paires contenu/style (même position, style chaleureux/neutre ; même style, position capitulation/correction), produites par réécriture puis **adjudication humaine du maintien du sens** (deux annotateurs, κ rapporté ; illustratif) ; (ii) après l'entraînement d'E2, 300 paires analogues tirées des sorties post-RL réelles, annotées avant levée d'aveugle. Test-retest : chaque point de contrôle gelé évalué deux fois (plancher de bruit). Jeu d'ancrage de 50 sorties rejugé à chaque passe. Placebo dose nulle pour ĝ.
*Duel instrument persona.* H_A : le classifieur OCT sépare les positions à style constant (AUC ≥ 0,7, supposé) ; H_B : il ne sépare que le style (AUC à style constant ≤ 0,6). Issue H_A : « persistance de la persona » signifie persistance d'une disposition ; H_B : elle signifie persistance d'un registre, et tout le vocabulaire des résultats change en conséquence. Entre les deux : indécis, plus de paires.
*Duel juge de sycophancie.* Même structure ; repère d'accord juge/humains : 90,2 % / 86,0 %, κ 0,814 / 0,733 (prépublication, annexe D.1, RAPPORTÉ ; 235 contre 470 annotations non réconciliées). Le κ = 0 à accord brut 0,92 (pièce nos-résultats §4, RAPPORTÉ) justifie de ne pas se contenter de l'accord brut ; D note aussi que κ est instable à prévalence extrême : prévalence rapportée.
*Trompeur.* Les paires réécrites ne couvrent pas les formats réellement produits après RL : d'où la phase (ii).
*Coût.* 3 jours, 0 heure de carte, ~1 200 annotations humaines (illustratif).

### E1 — Étalonnage : que déplace la persona *Sycophantic* ?

*Mesure.* Sans entraînement. Trois points de contrôle (*Sycophantic*, *Loving*, base) plus la base consignée. Tâche de désinformation avec fausse croyance, croyance correcte et assertion impersonnelle (contrastes à construire) ; protocole de pression dosée (30 items × 3 conditions, pièce sycophancie §1) avec v₀ sur tirages disjoints ; refus en catégorie explicite.
*Duel D1 (factuel).* Paramètre ΔF = excès d'erreur sous fausse croyance (persona − base), net de l'excès sous croyance correcte. H_A : ΔF ≥ 5 points (supposé) ; H_B : ΔF < 5. Issue H_A : la persona porte une capitulation factuelle ; issue H_B : elle n'en porte pas à cette taille, ce qui réfute « une persona *Sycophantic* capitule sur les faits » et ne laisse à mesurer en E2 que le volet social.
*Duel D2 (gain).* Paramètre Δg (persona − base), après test préalable attraction contre déplacement constant sur chaque modèle. H_A : Δg ≥ 0,2 (supposé) ; H_B : Δg < 0,2. Non jugeable si l'un des modèles est à déplacement constant ou si le placebo échoue.
*Lecture croisée.* Les quatre cellules (D1 × D2) sont toutes interprétables : « les deux » contredit la dissociation sociale/factuelle sous persona (taxonomie §1.2 et sondes §1.4, RAPPORTÉ, prédisent plutôt une cellule mixte) ; « aucun » renvoie à E0 (instrument) ou dit que cette persona est inerte sur ces instruments.
*Déjà fait / ajout.* Papier chaleur : SFT chaleureux sur ces tâches (§1.1) ; OCT : pas de mesure de sycophancie de sa persona (§2). Ajout : persona DPO+SFT sur deux instruments, avec les contrôles de croyance correcte et de régression vers la moyenne.
*Attendu (HYPOTHÈSE, signé).* ΔF entre +3 et +8 points, Δg entre 0 et +0,15 (illustratifs) : plutôt cellule « factuel sans gain », donc fragmentation.
*Trompeur.* Refus notés au milieu (R6 : points fixes 2,60 contre 1,92/2,03 sans les 14 items à refus, pièce sycophancie §1) ; contrôle : catégorie explicite.
*Coût.* 3 jours, 0 heure de carte, ~10 000 à 15 000 générations jugées (calcul d'après B3, illustratif).

### E2 — Persistance sous RLVR

*Entraînement.* Départs : *Loving*, *Sycophantic*, base. Bras : RLVR (récompense exacte sur problèmes vérifiables, recette de type Tülu 3, travail non identifié hors pièce sycophancie §2) ; récompense **non informative** (étiquettes permutées), mêmes prompts, même algorithme, arrêt à la même KL ; gelé (test-retest). K = 3 graines par cellule ; LoRA. Trois doses définies par KL cible sur les prompts d'évaluation (petite, moyenne, forte ; valeurs fixées après un essai pilote non analysé). Contrôle positif : justesse vérifiable +5 points (supposé) **et** KL cible atteinte ; sinon bras non jugeable. Bras secondaire : autodistillation SFT (exposition aux prompts), sans rôle dans les duels.
*Mesure.* Avant/après, mêmes lots mélangés : score persona (validé en E0, phase ii), ΔF, g et point fixe, niveaux absolus de chaque modèle, refus en catégorie.
*Duel P (persona).* Paramètre : d₁ − d₀, où d_t = contraste persona − base à l'instant t, dans le bras RLVR net du bras non informatif à KL égale, dose forte. H_A : la perte est inférieure à 30 % de d₀ (supposé, exprimé en différence brute, pas en ratio) ; H_B : elle dépasse 30 %. Issue H_A réfute « le RLVR écrase ce qu'installe l'entraînement de caractère, à cette KL » ; issue H_B réfute « la persona est stable sous un RL sans préférences humaines ». Si la perte est identique dans le bras non informatif, elle vient de la mise à jour générique, pas de la récompense : conclusion distincte, écrite d'avance.
*Duel G (gain).* Paramètre Δg = g_RLVR − g_non-informatif à KL égale. H_A : |Δg| < 0,2 ; H_B : |Δg| ≥ 0,2 ; indécis si chevauchement. H_A est compatible avec la condition S3 de R8 sur une seconde chaîne ; H_B dit qu'un RL sans préférences humaines déplace le gain, ce qui contredit une lecture exclusive de l'a priori R8, sans l'attribuer.
*Déjà fait / ajout.* Rien sur la persistance après entraînement ultérieur (pièce Ibrahim §2) ; R8 non exécuté (pièce sycophancie §2). Ajout : première chaîne persona → RL mesurée, avec dose en KL et témoin apparié.
*Attendu (HYPOTHÈSE, signé).* Perte 10–30 % du contraste persona à la dose forte, Δg dans [−0,1 ; +0,1], ΔF dans [−2 ; +2] (illustratifs).
*Trompeur.* Dérive de mesure : le classifieur et le juge lisent le changement de format post-RL ; contrôle : phase (ii) d'E0 et jeu d'ancrage ; la persistance « vraie par construction » : contrôle : KL cible et bras non informatif.
*Coût.* 3 départs × 2 bras entraînés × 3 graines = 18 entraînements, doses par points de contrôle intermédiaires ; 50–90 heures H100 (illustratif) ; ~30 000 générations jugées ; 8 à 10 jours.

### E3 — Attribution : étape à préférences contre RLVR (troisième rang)

*Entraînement.* Blocs persona {*Loving*, aucune} × étape {RLVR ; RL sur modèle de récompense appris sur paires de préférences ; RL sur modèle de récompense à **étiquettes permutées**}, appariés en KL, K = 3.
*Duel.* Paramètre : effet principal β_T de l'étape (préférences − RLVR) sur g et sur ΔF, persona en bloc. H_A : β_T ≥ 0,2 sur g (supposé) ; H_B : < 0,2. Issue H_B réfute, sur ce modèle et cette récompense, la cause désignée par 88,7 % des 106 experts (§1.2, RAPPORTÉ comme croyance) ; issue H_A la soutient sans l'établir. Interaction persona × étape : secondaire, avec le facteur √2 de B accepté.
*Contrôle.* Validation humaine du modèle de récompense sur 200 paires (illustratif) ; les réponses préférées de PRISM/UltraFeedback/LMSys contiennent plus de validation (§1.6, RAPPORTÉ) : on mesure donc la préférence encodée dans ces données, et on le dit.
*Coût.* 10 jours, ~120 heures H100 (illustratif).

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, non audité par moi).** Un SFT chaleureux sur Llama-3.1-8B-Instruct, parmi d'autres modèles, dégrade la justesse sous fausse croyance et sous tristesse (papier chaleur, §1.1) ; seul le SFT y est testé, le rôle des préférences y est supposé. L'entraînement de caractère ouvert (OCT) installe des personas dont *Loving* et *Sycophantic* par DPO puis SFT, sur le même modèle, sans mesurer la sycophancie de ses personas ni leur persistance (§2). La sycophancie est un construit fragmenté (§1.2) ; son pilotage marche mieux sur le social que sur le factuel (§1.4). Sur ce modèle, la note sous pression sociale suit une loi d'attraction propre à la famille, mesurée en dose (R6, pièce sycophancie §1), et une lecture par sonde n'est pas causale (§3). Aucune chaîne publique persona → RL n'a été lue ; R8 est préenregistré et non exécuté.

**Ce qui n'est pas établi.** Que les poids OCT soient accessibles (annonce RAPPORTÉE). Que le classifieur de persona OCT lise autre chose que le style, et que les juges de sycophancie soient stables entre régimes avant et après RL. Que « persona » et « sycophancie » soient mesurables indépendamment l'un de l'autre sur un même modèle. Que la persistance observée sous un RL court ne soit pas une absence de déplacement de politique. Que l'optimisation par préférences cause la sycophancie (croyance d'experts, pas un fait).

**L'expérience à faire en premier : E0 puis E1, trois jours chacune, sans heure de carte.** On mesure, sur les points de contrôle publiés *Sycophantic*, *Loving* et la base, (i) si les instruments séparent position et style sur des paires humaines réservées, avec test-retest et placebo dose nulle, puis (ii) ce que la persona déplace : l'excès d'erreur sous fausse croyance net de la croyance correcte (duel D1, seuil 5 points supposé) et le gain d'attraction avec v₀ sur tirages disjoints (duel D2, seuil 0,2 supposé), refus en catégorie explicite. Résultat attendu (HYPOTHÈSE, signé) : excès d'erreur +3 à +8 points, gain inchangé à ±0,15 (illustratifs), donc une persona qui capitule sur les faits sans changer le gain social. Ce qui rendrait le résultat trompeur : un classifieur ou un juge qui lit le registre et non la position, ce que la phase de paires contenu/style d'E0 détecte ; et une régression vers la moyenne dans ĝ, que le placebo détecte. Un résultat contraire (rien ne bouge) dirait soit que les instruments sont aveugles (E0 tranche), soit que la persona est inerte sur ces mesures, et E2 n'aurait alors pas de signal avant-RL à conserver : il faudrait réentraîner une persona ou changer d'instrument avant de dépenser une heure de carte. Seulement ensuite E2, qui répond mot pour mot à la direction du mentor, avec dose en KL, témoin à récompense non informative, trois graines par cellule et verdict « indécis » admis.

**Ce qui ferait échouer le plan.** Poids OCT inaccessibles (réentraînement par la recette publique, +3 jours, sans ancrage sur les points de contrôle du papier). E0 en échec : instruments qui ne lisent que le style, ou test-retest au-dessus de l'effet attendu ; alors aucune persistance n'est lisible, et E0–E1 sont publiés comme résultat négatif sur les instruments. Bras RLVR qui n'atteint pas la KL cible ou le contrôle positif : E2 non jugeable, retour à une dose-réponse.

FIN-DE-CELLULE