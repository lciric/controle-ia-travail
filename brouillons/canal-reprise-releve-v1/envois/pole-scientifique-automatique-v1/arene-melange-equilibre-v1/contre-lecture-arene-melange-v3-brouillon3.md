# Contre-lecture (R2) — préenregistrement « arène : mélange d'équilibre, Q1 à nombre de paramètres égal, Q2 à classe de fonctions égale » v1, brouillon 3 — brouillon 1 de la contre-lecture 3

Contre-lecteur : sous-agent neuf Sonnet 5.5 (autre modèle que l'auteur, un Opus ; n'a écrit aucune contre-lecture précédente de ce pilote). 31 octobre 2026. Lecture, essais et recalculs sur processeur seulement ; aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien lu sous `donnees/`, aucun `git fetch`. Racine de décision RACINE jamais employée. Racines d'essai neuves employées : **20269731 / 20269732** (diagnostic de code, section 1) et **20269741 / 20269742** (deux simulations de quelques lignes, section 1) ; ces racines ne figurent nulle part dans le dépôt (recherche hors `donnees/`).

Brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon3.md`, `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0`. Contre-lecture 2 relue : `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427`.

## 0. Verdict

**Présentable après corrections.** 0 bloquant, 4 majeurs, 7 moyens, 5 mineurs. Le travail est honnête et solide sur la traçabilité : les 16 constats de la contre-lecture 2 sont traités, les 57 essais passent, la puissance se rejoue à l'identique, la prédiction Q2 précède bien toute autre trace datable, et le brouillon déclare lui-même ses prédictions réfutées. Ce qui doit changer touche **ce que le résultat Q2 veut dire** et **trois mécanismes de lecture mal réglés** : (i) le critère d'artefact S17 est mal calibré pour Q2 (il se déclenche sur du bruit et ne voit pas un changement de classe) ; (ii) l'explication donnée de la pureté de B′ est contredite par les données du pilote, et « le tirage ne se pose pas » côtoie « ce n'est pas le tirage » ; (iii) la condition d'application affiche un indicateur de retours (I3) sans sa valeur nulle, et A est au plancher à δ 1,8 ; (iv) l'audit « conforme et trop propre » ne couvre que P4, P5, P8 et n'audite jamais A. Les corrections sont de texte, de critère et d'un champ de code (S17) ; aucune ne demande de nouveau pilote ni de toucher à une racine de décision. Trois décisions reviennent à Lazar (section 5).

## 1. Ce que j'ai fait (traçabilité)

- Empreintes : `sha256sum -c` sur les 34 compagnons du dossier (essais compris, depuis leur sous-dossier) : tous conformes. Les 23 empreintes citées au brouillon 3, au LISEZMOI v3 et au gel v3 recoupées une à une avec les fichiers du dossier ; celles des documents hors dossier (brainstorm, réponse pont, gabarit, fusion v3 sur `origin/main` lue par `git show`, sans réseau) recalculées : conformes.
- Essais : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider essais/test_arene_melange_v3.py` : **57 réussis en 68,6 s**. Aucun `__pycache__` créé.
- Rejeu de `calcul-puissance-arene-melange-v3.py` sur le pilote et l'audit d'essai (sortie dans `/tmp`, pas dans le dossier) : **identique ligne à ligne** à `calcul-puissance-arene-melange-v3-sortie.txt` (291 lignes, `diff` vide).
- Lecture intégrale du brouillon 3, du gel v3, du LISEZMOI v3, du journal, de la sortie (M3) ; lecture du code v3 (configuration, graines, moniteurs, `MoniteurOu`, entraînement, `resoudre_jeu`, `trajectoire`, `defense_temoin`, `phase_finale`, `indicateurs_cycle`, `analyser`, `lire_tables`, attaquant indépendant, `juger_audit`, arrêt par PID) et des essais clés.
- Statistiques du pilote v3 recalculées depuis `essai-pilote-arene-melange-v3-detection.json` : répartition des poids de B′ (indice du moniteur dominant, seuils de pureté), B′ − D selon pureté, courbes par tour, valeur du jeu restreint.
- **Diagnostic de code, racine d'essai neuve 20269731 / 20269732, non opposable** (script dans `/tmp/cl3/diag.py`, hors dossier) : 8 instances × 2 δ ; pour chaque tâche, V de D, B′, d'un **témoin « mode »** (le moniteur de poids maximal de B′, déployé seul) et d'un **maxout unique de 73 unités** (D73, même total d'unités que B′, entraîné à chaque tour contre le mélange uniforme des attaques passées). Résultats en CM3-02.
- Deux simulations de quelques lignes, racine 20269741 / 20269742 : incertitude de la part pure, fausse alerte de S10, valeur nulle de I3 (CM3-02, CM3-03, CM3-05).

## 2. Réponses aux points demandés

### 2.1 CM2-01 à CM2-16 — traités ?

| Id | Traité ? | Où (ligne du brouillon 3) | Réserve |
|---|---|---|---|
| CM2-01 | oui | l. 458, 506 ; `test_decision_refusee_copie_brouillon3_pour_la_bonne_raison` (copie temporaire, sans compagnon puis scellée) | essai passé ; le décompte « 57 » est exact |
| CM2-02 | oui, étendu | titre ; l. 119, 136-137, 148-149, 161, 165-166 | Q2 posée correctement pour D ; **pas pour C3′** (CM3-07) ; interprétation de Q2 : CM3-02 |
| CM2-03 | en partie | l. 120, 151, 231, 422-432 ; Table 5 | indicateurs mesurés, mais lecture trop forte (CM3-03) |
| CM2-04 | oui | l. 123, 266-267, 366, 381 | m = 0,02 fixée dans le gel avant le pilote : vérifié (gel § 1.5) |
| CM2-05 | en partie | déclencheur 9 l. 372 ; S17 l. 308-311 | critère S17 mal calibré (CM3-01) ; couverture partielle de R4 (CM3-04) |
| CM2-06 | déclaré, non corrigé | l. 127, 290 | acceptable si Lazar décide ; effet nouveau sur la Table 5 (CM3-03) |
| CM2-07 | oui | l. 124, 248 ; (M3) § 3 | rejeu identique ; une coquille au résumé (CM3-12) |
| CM2-08 | oui dans la forme | l. 285 | la bande déclenche à tort environ une fois sur trois (CM3-05) |
| CM2-09 | oui | l. 175, 374 | probabilités conditionnelles au pilote : voir CM3-06 |
| CM2-10 | oui | l. 366, 381 (déclencheur 3 hors ligne 1) | — |
| CM2-11 | oui | l. 161 | — |
| CM2-12 | oui | l. 281, 454 | — |
| CM2-13 | oui | l. 200 | — |
| CM2-14 | oui | l. 349, 480-481 ; essais PID et TERM passés | `resource_tracker` non consigné : déclaré, sans conséquence |
| CM2-15 | oui, déclaré | l. 171, 520 | l'audit couvre D, B′, C3′ |
| CM2-16 | oui | l. 9 | — |

### 2.2 La prédiction Q2 a-t-elle été gelée avant toute exécution de B′ ?

**Oui, autant que les traces le permettent ; non prouvable au-delà.**
- Dates de naissance des fichiers (`stat`, heure locale +0100 ramenée en UTC) : gel v3 **10:25:21** (modification = naissance : jamais rouvert) ; fichier d'essais v3 10:29:22 ; PID du pilote 10:39:50 ; pilote 11:08:31 ; audit d'essai 11:19 ; brouillon 3 11:29:58 ; journal 11:32:05. Le gel précède toute autre trace de v3 datable. Le contenu du gel (règle « non exercée », seuil 0,5, S6, S15, critère S17, rôle de S10) est celui que le brouillon invoque : vérifié, rien de ces règles n'a été ajouté après le pilote.
- **Limites** : (a) le journal a été écrit en une fois à 11:32 UTC, après tout : ses horodatages sont rétrospectifs, seules les naissances de fichiers corroborent ; (b) le code au gel (`04df57d2…`) a été écrasé (le fichier `arene_melange_v3.py` naît à 10:38 : version finale) ; l'affirmation « jamais exécuté avant le gel » n'est pas vérifiable ; (c) l'étape 4 du journal a exécuté à 10:32 une tâche pleine taille (B′ inclus, racine d'essai de tests) « pour le temps et les compteurs seulement », après le gel et avant l'accélération du code : sans effet sur l'ordre gel puis pilote, mais la phrase « lus : temps et compteurs seulement » est une déclaration ; (d) le gel a été écrit en connaissant le pilote v2 (D > B, B − A = +0,13) : la prédiction n'est pas aveugle, elle est antérieure au calcul de B′ seulement (le gel le dit, § 0). **Aucun écart d'ordre constaté.** Voir CM3-08 pour la recommandation de preuve.
- Les prédictions Q2 ont été **réfutées** (8 branches), pas retouchées : le bilan du brouillon (l. 196) compte pourtant 36 branches, 28 tenues ; je retrouve 26 tenues et 8 réfutées (34), ou 26 et 10 (36) si la clause « support ≥ 2 » est comptée (CM3-12).

### 2.3 Code : classe égale, double oracle, cycle, gardes, graines

- **B′ contre D, classe égale : oui pour le moniteur déployé.** B′ : 9 unités, 63 paramètres par requête (7 si M0, linéaire, est tiré) ; D : 9 unités à la fin ; sorties du pilote : `parametres_par_requete` B′ ≤ 63, D 63 ✓. Écarts réels mais déclarés : B′ entraîne 8 moniteurs de 9 unités (D : t + 1 unités au tour t) ; B′ s'entraîne contre la stratégie d'équilibre q de l'attaquant, D contre le mélange uniforme ; **B′ ajoute une étape de sélection par programme linéaire** (maximin sur 9 moniteurs). Donc B′ − D mesure « tirage + sélection + distribution d'entraînement », pas le tirage seul (CM3-02).
- **C3′ n'est pas de même classe que B′** : 511 paramètres déployés par requête, contre ≤ 63 (CM3-07).
- **Double oracle maxout** : `trajectoire` appelle `ctx.entrainer(cb, t, attaques, q, cfg.unites_Bp)` avec q = stratégie d'équilibre de l'attaquant sur la matrice G (colonnes : cible puis attaques ; lignes : M0 puis moniteurs) ; graine d'initialisation du rôle 8, code de bras 8 ; programme linéaire primal et dual contrôlés. Conforme au texte. Réserve : l'oracle des maxouts emploie un seuil gaussien approché (déclaré, l. 171), alors qu'il est exact en population pour B (linéaire) : léger avantage du côté de B dans Q1.
- **Mesure du cycle de A** : `indicateurs_cycle` recalculée à la main sur la matrice H : I1 = moyenne des tours 5-8 moins 1-4 de (iii) ; I2 = moyenne sur t = 1…7 de H[t,t] − H[8,t] ; I3 comme décrit. Les indices correspondent au texte et à l'essai `test_indicateurs_cycle_sain`. Limites d'interprétation : CM3-03.
- **Gardes (R5)** : 62 sites `raise GardeArret`, 62 motifs, chacun avec un essai nommé (cas sain et artefact, `pytest.raises(match=…)`) ; contrôle par arbre syntaxique passé. Pas de repli silencieux trouvé (`except` limités à la lecture de `/proc`, au JSON et aux signaux). La garde de variance de `MoniteurOu` est absolue (1e-12) : un moniteur presque constant mais non nul passerait et verrait son bruit amplifié par la standardisation ; sans effet observé au pilote.
- **Graines (R9)** : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))` dans `gen`, avec garde de racine de décision ; chaque bras tire de son propre code (essai d'ordre des bras passé, avec et sans B′) ; manifeste : configuration et empreinte, versions, empreintes de bibliothèque, commit (arbre sans le code : déclaré, CM2-16). Le champ « graines » de `creer_manifeste` n'est pas employé : déclaré, schéma consigné à la place.
- **Continuité v2** : `test_bras_v2_inchanges` passe (A, B, C1, C2, C3, D identiques champ à champ au code v2 à la configuration réduite) ; non vérifiable à pleine taille faute de pilote v2 sur la même racine.

### 2.4 « Q2 non exercée », la règle, le tirage, le maxout de 73 unités

Voir CM3-02 (analyse complète). Réponse courte :
- **La règle est juste dans sa mécanique** (gel § 1.7 ; `lire_tables` : part pure > 0,5 à au moins un δ ; seuil de pureté sans ambiguïté sur les données : les poids maximaux sont soit 1,000 soit ≤ 0,95).
- **Un équilibre presque pur veut dire** : à classe de 9 unités, le jeu restreint a une solution (presque) en stratégie pure, et la valeur du jeu restreint est à 0,004-0,005 de V (un nouvel attaquant ne trouve presque rien de plus). Dans ce monde, à cette classe, **le tirage n'apporte rien de mesurable** (B′ ≈ D, +0,001 / +0,009). Ce n'est **pas** « la question ne se pose pas » : c'est une réponse locale (classe riche, δ, T, attaquant local) qui contraste avec la classe linéaire, où tirer au hasard parmi les moniteurs de B bat A de +0,10 et même le mélange uniforme C1 bat A d'environ +0,08. Le tirage se comporte ici en **substitut de capacité**, pas en gain à capacité égale.
- **Le maxout de 73 unités ne change pas la conclusion, d'après mon diagnostic** (non opposable, 8 instances par δ, bruit ≈ 0,003) : D73 − D = +0,003 (δ 1,4) et −0,001 (δ 1,8) ; D73 − B′ = −0,002 et +0,003. Il ne fait ni mieux ni pire que D ou B′ au bruit près. La lacune reste à déclarer, mais elle ne retourne rien. Elle serait sans doute plus gênante pour un résultat « Q2 confirmée », non attendu.

### 2.5 Seuils S1 à S18

Cohérence : S1 = S5 = S6 = S15 = 0,02 (deux fois α), tous **fixés dans le gel avant le pilote** (vérifié) ; S7, S9, S11, S12, S14 hérités du gel v2 ; S10 : règle fixée au gel, **bandes** calculées sur le pilote. Choisis ou réglés **après** lecture du pilote v3 : **S18 = 0,10** (reco), S4 (N = 100), S8 (`timeout 9000`) ; ils sont déclarés (l. 355). Pour S18, le « principe » est faible (CM3-09). Tailles réelles : 0,017 (Q1, équivalence) et 0,026 (Q2, équivalence) lues dans (M3) § 3b, 3c et rejouées à l'identique ; elles dépassent le nominal d'un facteur 2 à 3 dans quelques cellules, sans conséquence pour les lectures prédites (aucune près de la frontière, hors C1 à δ 1,8, déclarée non ferme). S17 et S10 : CM3-01, CM3-05.

### 2.6 R3, R4, portée

- **R3 tenu** : aucun run ne vise un signe positif ; les prédictions Q2 allaient dans le sens défavorable à la piste (0,6-0,7). Le chemin « bifurcation après le pilote v2 » est déclaré. Réserve de fond : Q2 est une deuxième fourche après une réfutation de Q1 ; si Q2 sort « non exercée », une troisième (moins d'unités) serait de la même veine — à décider avec cette lecture en tête, pas à cacher (CM3-02, section 5).
- **R4** : couverture partielle (CM3-04). Résultat conforme et « propre » : P4, P5 (1,000), P1, P10, P11 (1,000 ou 0,998), B′ ≈ D (1,000).
- **Portée** : rubrique présente (l. 145-151) et utile ; trois phrases la contredisent (CM3-02, CM3-03).

### 2.7 Faisabilité du calcul

57,0 s de processeur par tâche (max 79,8 s ≪ 600 s), 190 min de processeur, **120 min de mur** à N = 100 sur 2 cœurs avec l'efficacité mesurée de 0,80 sur machine chargée ; cohérent avec le pilote (1 720 s de mur pour 48 tâches). `timeout 9000` donne 25 % de marge. Voir CM3-10.

## 3. Constats

### Majeurs

**CM3-01 — S17 : le critère d'artefact se déclenche sur du bruit pour Q2 et ne voit pas un changement de classe** (majeur)
- Où : l. 310-311 (S17), l. 372 (déclencheur 9), `juger_audit` (code l. 1535), config `audit_critere = 0.05`.
- Constat : l'artefact est déclaré si la moyenne audit/source d'un contraste « change de signe ou de plus de 0,05 ». (1) Pour B′ − D, dont le pilote donne +0,0009 et +0,0091 avec un écart-type par tâche de 0,012, le signe de la moyenne sur 5 tâches vaut presque une pièce : une variation de 0,001 à 0,003 entre V et V_audit suffit à le retourner avec une probabilité que j'estime à 10-30 % par δ (erreur-type de la moyenne ≈ 0,0055 ; variations observées à l'audit d'essai : 0,0002 à 0,0038). Un « artefact trouvé » fabriqué bloque la phrase de synthèse des Tables 4 et 7. (2) À l'inverse, B′ − D peut passer de +0,001 à +0,045 (classe « ≈ » → « B′ > D », avec m = 0,02) sans franchir 0,05 et sans changer de signe : non détecté. L'échelle pertinente pour Q2 est m = 0,02, pas 0,05. (3) `V_audit` est le minimum de V et de trois réponses de l'attaquant indépendant : il est biaisé vers le bas, bras par bras, d'une quantité qui dépend du bras (D : 0,004 sur la tâche d'essai) ; comparer V (deux réponses) et V_audit (quatre) introduit un écart systématique de l'ordre de 0,002-0,004 dans les contrastes. (4) Le bruit invoqué à l'appui de 0,05 vient d'un audit d'essai où **n = 1 tâche par δ** (sortie M3 § 8 : « n 1 »), pas de « 5 tâches » (l. 311).
- Correction : exprimer le critère en classes : « artefact si la classe de la Table 3 ou 6 recalculée sur V_audit diffère de celle de V, ou si |écart| > m/2 = 0,01 » ; ne compter un changement de signe que si |moyenne source| ≥ m ; comparer V_audit au minimum des mêmes trois réponses côté source, ou comparer le minimum des quatre réponses des deux côtés ; estimer le bruit apparié sur ≥ 5 tâches par δ avant gel (le mode `audit-essai --instances 0:5` existe ; racine d'essai déjà employée ou nouvelle à choisir). Le champ `audit_critere` et `juger_audit` changent : empreinte du code à régénérer, essais à rejouer.

**CM3-02 — L'explication de la pureté de B′ est contredite par les données ; « la question ne se pose pas » et « ce n'est pas le tirage » ne tiennent pas ensemble** (majeur)
- Où : l. 121-122, 149, 196, 218 ; (M3) § 6.
- Constats, tous recalculés depuis `essai-pilote-arene-melange-v3-detection.json` :
  1. **L. 196** : « le moniteur entraîné contre l'équilibre de l'attaquant domine presque toujours les précédents dans le jeu restreint ». Faux sur les données : le poids pur tombe sur le moniteur de l'indice 2 (entraîné au **tour 2**) dans 12 tâches sur 24 à δ 1,4 (indice 8, le dernier, dans 4 tâches) et dans 10 sur 24 à δ 1,8 (indice 8 : 3 tâches) (indice du poids maximal, toutes tâches). Le moniteur qui l'emporte est souvent l'un des premiers, pas le dernier ; les courbes par tour de B′ et D sont plates dès le tour 4 (≈ 0,45 à δ 1,4, 0,25 à δ 2). Lecture compatible avec les données : saturation de la classe de 9 unités, qui atteint très tôt un plafond de ce monde (V(B′) = 0,449, V(D) = 0,448) ; les moniteurs ultérieurs n'améliorent plus le pire cas sur le pool. Or sous un plafond, B′ ne peut presque pas dépasser D : **Q2 est peu discriminante par construction**, pas seulement « non exercée ».
  2. **« Presque pas employé » (l. 218) est inexact** : 9 tâches sur 24 (δ 1,4) et 11 sur 24 (δ 1,8) ont un mélange réel (poids maximal moyen 0,89 et 0,82 sur l'ensemble). Sur ces tâches B′ − D vaut +0,004 et +0,009 (n = 9 et 11, erreur-type ≈ 0,004) : rien d'exploitable, mais le tirage y est employé.
  3. **L. 149 contre l. 218** : « Q2 non exercée : la question du tirage ne se pose pas (ni pour, ni contre) » puis « ce qui guérit la non-convergence est la richesse de la classe, pas le tirage ». On ne peut pas écrire les deux. Les données disent : B bat A de +0,10 / +0,12 et C1 (tirage uniforme parmi les mêmes moniteurs) bat A d'environ +0,08 : **le tirage guérit en partie à classe linéaire** ; D bat A de +0,33 / +0,22 : la richesse guérit bien davantage. Formulation défendable : « le tirage est un substitut partiel de capacité à classe pauvre ; à classe de 9 unités l'équilibre est presque pur et B′ ≈ D ».
  4. **B′ − D ne mesure pas le tirage** : B′ ajoute à D une sélection (maximin sur 9 moniteurs) et une distribution d'entraînement différente (q au lieu du mélange uniforme). Le témoin direct du tirage à classe égale est le moniteur de poids maximal de B′ déployé seul (« mode »). Je l'ai calculé (racine 20269731/32, 8 instances par δ, non opposable) : B′ − mode = +0,001 à δ 1,4 (+0,003 sur les 2 tâches à mélange réel) et +0,004 à δ 1,8 (+0,006 sur les 5 tâches à mélange réel). Pas d'effet détectable, mais un signe plutôt favorable au tirage quand il est employé ; 5 tâches ne tranchent pas.
  5. **Maxout de 73 unités** : D73 − D = +0,003 / −0,001 ; D73 − B′ = −0,002 / +0,003 (mêmes 16 tâches). Aucune conclusion ne change ; la lacune peut rester déclarée.
  6. Part pure à δ 1,8 dans mon échantillon indépendant : 3 tâches sur 8 (contre 13 sur 24 au pilote) : voir CM3-06.
- Correction : réécrire l. 196 (retirer l'explication, ou la remplacer par la saturation observée et l'indice du moniteur dominant) ; réécrire l. 149 et 218 d'un seul tenant (voir ci-dessus) ; ajouter aux descriptives un **B′ − D selon pureté** et, si Lazar y consent (nouveau code, nouvelle empreinte), un **témoin « mode »** dans la décision ; dire dans le résumé que Q2 est « non exercée » **et** adossée à un plafond.

**CM3-03 — Condition d'application : lecture trop forte de I3, I2 et de la Table 5 à δ 1,8** (majeur, parce que le point 2 du résumé est un titre)
- Où : l. 120, 151, 231, 422-432 ; code `indicateurs_cycle`.
- Constats : (1) **I3 = 0,88 et 0,93 pour A** est présenté comme « retours vers d'anciennes attaques » sans valeur nulle. Sous échangeabilité des déplacements, la valeur attendue de I3 sur t = 3…8 est la moyenne de (t − 2)/(t − 1) = **0,735** (simulation sur 20 000 tirages de vecteurs aléatoires à 36 coordonnées : 0,735). B donne 0,74-0,75 (= valeur nulle) ; D 0,32-0,45 (sous la valeur nulle) ; seul A est au-dessus. À écrire avec sa valeur nulle ; sinon « 88 % » trompe. (2) **I2** (baisse de H[t,t] à H[8,t]) mélange l'oubli et la saturation d'un moniteur linéaire qui doit couvrir plus d'attaques ; D a I2 < 0 (− 0,03 / − 0,02) précisément parce que sa classe est plus riche. Le gel le disait (« ne dira pas pourquoi ») mais la ligne « A ne progresse pas, avec oubli » et le titre « non-convergence analogue à Bailey » (l. 120) vont plus loin. (3) **A est au plancher à δ 1,8** (iii par tour 0,021-0,032 ; 2,7 α) : « ne progresse pas » y est presque acquis (S15 = 0,02 est de l'ordre du niveau entier de A) ; la Table 5 à ce δ discrimine peu. (4) I2 et la matrice H de B et B′ portent sur les moniteurs un à un, pas sur la défense mixte déployée : le mot « oubli » ne s'y applique pas.
- Correction : afficher la valeur nulle de I3 (0,735) à côté de chaque valeur ; renommer I2 « baisse de détection des attaques passées (oubli ou saturation) » ; écrire au résumé que A est plat à un niveau bas (plafond de classe ou cycle, non distingués) et que la Table 5 à δ 1,8 est peu informative ; préciser que H/I2 de B et B′ sont par moniteur.

**CM3-04 — R4 : l'audit « conforme et trop propre » est incomplet, et A n'est jamais audité** (majeur)
- Où : l. 372 (déclencheur 9), `BRAS_AUDIT = (B, C3, D, B′, C3′)`.
- Constat : le déclencheur 9 couvre P4, P5 (1,000) et P8 (« ≈ ») ; P1 (plomberie, 1,000), P10 (Q2 non exercée, 0,998) et P11 (Table 5, 1,000) sont tout aussi conformes et « propres » et n'en déclenchent aucun. L'attaquant indépendant ne s'exerce jamais contre A, dont dépendent les Tables 1, 2 et 5 (A est près du plancher, donc là où une optimisation locale faible fausserait le plus l'écart relatif). Conséquence : le même résultat prévu et net peut être audité d'un côté (Q1) et pas de l'autre (condition d'application, plomberie). R4 demande le même audit pour un résultat conforme et trop propre.
- Correction : ajouter A à `BRAS_AUDIT` (coût négligeable : moniteur linéaire) et à `PAIRES_AUDIT` (B − A) ; étendre le déclencheur 9 à P1, P10, P11 ; ou écrire pourquoi la lecture de la plomberie et de la Table 5 n'en a pas besoin.

### Moyens

**CM3-05 — S10 : la bande « ± 5 erreurs-types » donne une fausse alerte environ une fois sur trois** (moyen)
- Où : l. 285 ; (M3) § 7. La demi-largeur est 5 × σ/√N, soit 0,5 σ à N = 100, mais la bande est centrée sur la moyenne d'un pilote à 24 tâches dont l'erreur est σ/√24 = 0,20 σ. L'écart entre la moyenne de la décision et celle du pilote a pour écart-type σ√(1/24 + 1/100) = 0,227 σ : la bande vaut 2,2 écarts-types, soit 2,8 % de fausse alerte par bande, **36 % sur les 16 bandes** (8 bras × 2 δ), sans aucun changement réel (calcul direct). Le déclencheur 2 « bloque toutes les tables ».
- Correction : demi-largeur = k σ √(1/24 + 1/N), k = 4 (≈ 0,9 σ, fausse alerte ≈ 10⁻⁴ par bande) ; règle fixée avant sceau, sans lecture. Recalculer les 16 bandes.

**CM3-06 — Probabilité de « Q2 non exercée » : 0,998 est conditionnel à un pilote de 24 tâches** (moyen)
- Où : l. 122, 213 (P10), (M3) § 4. La part pure au pilote est 15/24 (δ 1,4) et 13/24 (δ 1,8). Le rééchantillonnage du pilote pris pour vérité traite ces parts comme exactes. Avec l'incertitude du pilote (lois bêta 16/10 et 14/12, N = 100 en décision), la probabilité que la part pure dépasse 0,5 à au moins un δ vaut environ **0,94** (0,85 pour δ 1,4, 0,62 pour δ 1,8). Mon échantillon indépendant donne 6/8 et 3/8. La confiance 0,95 de P10 tient ; le chiffre 0,998 est trop net, et « surprise » (déclencheur 1f) devient un événement de l'ordre de 6 %.
- Correction : écrire « 0,998 conditionnel au pilote ; ≈ 0,94 avec son incertitude » (racine d'essai 20269741 pour la simulation).

**CM3-07 — C3′ n'est pas « à classe égale » avec B′ ; le contraste B′ − C3′ ne teste pas le tirage** (moyen)
- Où : titre, l. 119, 137, 166, 330. C3′ déploie 511 paramètres par requête contre ≤ 63 pour B′ ; le titre et le résumé disent « à classe de fonctions égale… bat D et C3′ ». Le texte l. 137 le précise, pas le titre. De plus C3′ agrège les moniteurs faibles des premiers tours et paie un seuil resserré : B′ > C3′ (+0,008 / +0,029) mesure surtout cela. Un « ou » restreint au support de B′ serait le contraste de même moniteurs qui répond à la question.
- Correction : titre et l. 119 : « à classe égale contre D, à moniteurs égaux contre C3′ » ; noter l'effet de dilution ; option pour Lazar : témoin « ou » sur le support de B′ (code à ajouter).

**CM3-08 — Preuve de l'ordre « gel puis exécution » : repose sur des déclarations** (moyen)
- Où : gel § 0 ; journal ; section 2.2 ci-dessus. Aucun commit ne fixe le gel avant l'exécution ; les horodatages du journal sont rétrospectifs ; le code au gel est perdu.
- Correction : consigner dans `registres/decisions.md` l'empreinte du gel et son heure de naissance de fichier ; à l'avenir, committer le gel avant tout lancement (le dépôt est git ; l'auteur a travaillé sans committer, déclaré).

**CM3-09 — S18 : seuil choisi après lecture du pilote, principe faible, rupture de chaîne d'empreinte** (moyen)
- Où : l. 315-316, 355. S18 = 0,10 est choisi pour ramener le risque d'arrêt de 0,16 à 2 × 10⁻⁵, calculé avec un taux de 0,0012 par entraînement tiré de **2 événements** sur 1 632 (intervalle très large : à la borne haute du taux, le risque à 0,05 dépasse 0,8). Le chiffre « 0,16 » lui-même est donc fragile dans les deux sens. Changer `taux_nonconv_max` modifie le code (nouvelle empreinte) : le pilote, les essais et la puissance ont tourné sur `88c87818…`, la décision tournerait sur un autre fichier (calculatoirement équivalent sur le chemin sans garde). Le texte dit à la fois « aucun changement de code après le pilote » (l. 355) et recommande de changer le champ.
- Correction : (a) soit garder 0,05 et accepter le risque affiché ; (b) soit remplacer la garde par une garde d'agrégat (part d'entraînements non convergés sur l'ensemble des tâches ≤ 5 %, principe : dérive massive) plus un plafond par tâche large (0,25) ; dans les deux cas déclarer la rupture de chaîne et rejouer les 57 essais. Décision de Lazar.

**CM3-10 — Temps : marge de 25 % et perte totale en cas de dépassement** (moyen)
- Où : l. 125, 258, 275. 120 min projetées (efficacité 0,80 mesurée sur machine chargée), `timeout 9000` = 150 min ; `pool.map` ne rend rien avant la fin (aucun point de reprise partiel, déclaré) ; l'audit de 10 tâches est quasi certain (déclencheur 9 prévu) : 19 à 51 min de plus ; une seule reprise complète permise. À une efficacité de 0,65 le run dure 148 min. Faisable, mais avec un risque de perte non négligeable que le texte ne chiffre pas.
- Correction : `timeout 12600` (3 h 30) pour N = 100, ou N = 80 (96 min projetées) ; écrire la durée totale prévue décision + audit (≈ 2 h 20 à 3 h 30).

**CM3-11 — Les audits d'essai et le calcul de puissance reposent sur peu de tâches pour ce qu'ils justifient** (moyen)
- Où : l. 311, 17 de (M3) § 8. Voir CM3-01 (4). La taille de l'audit d'essai (1 tâche par δ) ne permet de fonder ni 0,05 ni « aucun artefact » pour Q2. À présenter comme un essai de fonctionnement, pas comme un contrôle de l'attaquant.

### Mineurs

**CM3-12 — Coquilles et comptes** : (a) résumé l. 124 : « Q2 jusqu'à 0,010, 0,015 et 0,026 » ; (M3) § 3c donne 0,008, 0,015 et 0,026 (S2, l. 248, est exact) ; (b) bilan l. 196 « 36 branches, 28 tenues, 8 réfutées » : je compte 26 tenues et 8 réfutées (34), ou 26 et 10 (36) ; (c) pureté : le texte (gel § 1.7, Table 7) dit « un poids ≥ 1 − 10⁻⁹ », le code (`resume_bras`) emploie `> 1 − 1e-9` ; sans effet sur les données ; (d) l. 183 : « réfutée (signe) » pour B′ − D à δ 1,4 (+0,0009, IC contenant 0, dans la plage prédite [−0,10 ; +0,02]) est correct selon la règle du gel, mais le lecteur gagnerait à lire « ≈ 0, signe opposé ».

**CM3-13 — Les compagnons des essais sont en chemin relatif** : `essais/*.sha256` ne se vérifie que depuis `essais/` ; sans conséquence, à noter dans le LISEZMOI.

**CM3-14 — `resource_tracker`, plateforme** : déjà déclarés ; rien à faire.

**CM3-15 — Garde de variance absolue de `MoniteurOu`** (1e-12) : un moniteur presque constant passerait et amplifierait son bruit par la standardisation ; ajouter une garde relative (σ_i / échelle des scores propres) ou la déclarer.

**CM3-16 — Valeurs de `delta` et `A` au plancher** : déjà déclarées (CM2-06) ; voir CM3-03 pour la Table 5.

### Positif

**CM3-17** : 57 essais réussis ; puissance rejouée à l'identique ; empreintes toutes conformes ; arrêt par PID et TERM essayés ; `test_bras_v2_inchanges` ; graines par `SeedSequence` et garde de racine de décision ; aucune fuite de RACINE ni de RACINE_TENUE ; transcription des chiffres de (M3) fidèle (S10, S2, résumé hors CM3-12) ; prédictions réfutées déclarées en bloc, y compris celle dont dépendait l'intérêt de Q2 ; règle « non exercée » fixée avant le pilote et non retouchée après.

## 4. R3 et symétrie

- **R3** : tenu (section 2.6).
- **R4, résultat conforme et trop propre** : le pilote donne 1,000 pour presque toutes les classes prédites (Q1, plomberie, Table 5, B′ ≈ D). Les contrôles intégrés (fausses alertes à 0,0006 de α, standard moins renforcé ≤ 0,003 en moyenne, valeur du jeu restreint − V à 0,004 pour B′, audit d'essai) vont dans le bon sens et je n'y trouve pas d'artefact de code. La netteté vient de l'écart de classe (Q1 : 0,08 à 0,22) et du plafond (Q2). Deux zones n'ont pas le même audit : A (Tables 1, 2, 5) et la lecture « B′ ≈ D » comme plafond, plutôt que comme égalité de deux méthodes (CM3-02, CM3-04).
- **Portée** : la rubrique est bonne ; les phrases à corriger sont l. 120, 149, 196, 218.

## 5. Corrections demandées, dans l'ordre

1. CM3-01 : critère S17 en classes (code `juger_audit`, config, essais, empreintes).
2. CM3-02, CM3-03 : réécrire l. 120, 149, 196, 218 ; afficher la valeur nulle de I3 ; ajouter B′ − D selon pureté.
3. CM3-04 : A dans l'audit ; déclencheur 9 étendu ou justifié.
4. CM3-05, CM3-06 : bandes S10 avec √(1/24 + 1/N) ; 0,998 conditionnel, 0,94 avec l'incertitude.
5. CM3-07 à CM3-11, CM3-12 : titre, bilan, coquilles, temps.

**Décisions pour Lazar** (rien à trancher par moi, mais l'enjeu est écrit) :
- **Q2 telle quelle ou refaite ?** Telle quelle, la décision réplique un résultat déjà connu à 0,94-0,998 (« non exercée ») pour 2 à 3 h de processeur ; elle a le mérite d'être une réplication scellée. Option : une conception où le mélange est forcément employé (moins d'unités par moniteur de B′ et de D), donc nouveau gel, nouveau pilote, racine fraîche. Recommandation : garder la décision telle quelle, **corrigée** (CM3-01 à CM3-04), et noter que Q2 est adossée à un plafond ; ne refaire la conception que si Lazar tient à la question du tirage à classe riche. Confiance moyenne. Défaut sous 48 heures : garder.
- **Recalibrer les δ** (A au plancher à δ 1,8) : la Table 1 et la Table 5 y sont peu informatives, Q1 et Q2 non (D, B′ valent 0,25 à ce δ). Recommandation : ne pas recalibrer (changement de conception après pilote) ; noter la limite. Défaut : ne pas recalibrer.
- **S18, N, `timeout`** (CM3-09, CM3-10) : recommandation S18 en garde d'agrégat ou 0,05 déclaré ; N = 100 avec `timeout 12600`.

## 6. Limites de cette contre-lecture

- Les chiffres de mon diagnostic (8 instances par δ, racine 20269731/32) sont **non opposables** : bruit ≈ 0,003 ; ils servent à juger si une conclusion tourne, pas à en fonder une.
- Les probabilités de CM3-01 (10-30 %) et de CM3-06 (0,94) sont des ordres de grandeur d'après la loi des moyennes sur 5 et 100 tâches et des lois bêta, pas des simulations de la règle complète.
- Je n'ai pas exécuté le mode `decision`, ni l'audit de 10 tâches, ni relu `controle_ia/prereg.py` et `scellement.py` (seulement leurs empreintes et leur emploi par les essais).
- Je n'ai pas vérifié les références d'antériorité (toutes SUPPOSÉ dans le texte, R7/R8).
- La preuve de l'ordre gel puis exécution est limitée aux traces de fichiers ; je n'ai pas accès à l'historique des commandes de la session de l'auteur.
