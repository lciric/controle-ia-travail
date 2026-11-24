# Proposition A — Tour III.3 : réponse aux critiques

## Pièces et statuts

- Les quatre critiques (B, C, D, E) sont présentes, se terminent par FIN-DE-CELLULE et ne montrent aucune coupure. Le bloc QUESTION est identique au bloc FAITS (même empreinte).
- Je ne réponds qu'aux sections « Sur la proposition A ».
- Je ne modifie aucun statut. C, D et E étiquettent VÉRIFIÉ leurs déductions mathématiques : je reprends ces étiquettes sans pouvoir les auditer ici.
- Tout ce que j'ajoute est **HYPOTHÈSE**, y compris les dérivations élémentaires que j'ai refaites à la main, non auditées. Rien n'a été exécuté. Tout chiffre est **illustratif** (« ill. »).
- Deux recalculs à la main concordent avec les critiques : la puissance de 0,29 à 0,53 pour E4 à n = 150 (E), et la proportion de fausses découvertes d'environ 0,92 pour un juge à 0,10 de fausses alertes sous une prévalence de 0,01 (D).

---

## (a) Verdict par critique

### Critiques de B

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| B-a1 | Borne de handicap : la référence qui définit l'étroitesse est aussi un bras de E4, donc son taux EP est majoré par construction. | **Acceptée.** C'est le défaut le plus grave de ma conception. | Budgets découplés, borne rapportée, bras CN-1 dans E4 (voir T2 et E4′). |
| B-a2 | E1 est vrai par construction si l'étiquette « profonde » et Δ partagent leur source. | **Acceptée.** | E1 remplacée par E1′, sans étiquette du concepteur. |
| B-a3 | L'oracle dilué augmente P_R(x) ; ν doit être figée sur la référence non diluée. | **Acceptée** (spécification manquante). | ν figée avant E3, sur des exécutions disjointes et non diluées. |
| B-a4 | Le prédicteur de E7 est lié mécaniquement au rang d'énumération. | **Acceptée.** | Prédicteur redéfini ; l'énumérateur sort du critère de E7. |
| B-a5 | Choisir « la meilleure référence » après coup est une sélection. | **Acceptée.** | Intersection-union : supériorité contre chaque bras. |
| B-a6 | La puissance de E4 est calculée contre zéro, la règle exige +5 points. | **Acceptée.** Mon dimensionnement était faux. | 280 à 600 mondes (ill.) au lieu de 150. |
| B-a7 | Le ratio de E6 dépend du couplage public/privé du générateur de mondes. | **Transformée en test.** | Le couplage devient un facteur de E6′. |
| B-b (ν) | Censure au plafond : Spearman sur ex-aequo, fiabilité 0,9 inatteignable. | **Acceptée.** | E2′ porte sur une étiquette binaire. |
| B-b (E1) | Si le solveur sature, l'AUC tend vers 0,5 quel que soit le concept. | **Transformée en verrou.** | Fraction résolue sans x exigée entre 0,2 et 0,8 (ill.), réglée sur des mondes de développement. |
| B-b (E4) | Trop peu de paires discordantes si les taux sont au plancher. | **Transformée en verrou.** | Le pilote doit montrer un bras hors système au-dessus du plancher mesurable. |
| B-b (E7) | Moins d'un succès attendu par quartile. | **Acceptée.** | E7′ devient exploratoire. |
| B-b (juge) | La correction n'est plus bornée si TPR − FPR tend vers 0. | **Acceptée.** | Juge exclu de toute mesure (T4). |
| B-c CN-1 | L'A/A est aveugle au handicap ; il faut un bras « référence déplacée ». | **Acceptée.** | Les bras CN-1 entrent dans E4′ comme adversaires à battre. |
| B-c CN-2 | Il faut un chasseur d'étroitesse ; le bras « bizarre » ne teste rien. | **Acceptée pour CN-2. Rejetée en partie pour « ne teste rien ».** Le bras scripté vérifie que la chaîne de notation ne crédite pas un rare-inerte, ce qui échoue si Δ a un biais positif. Il ne teste pas un chercheur, et B a raison sur ce point. | CN-2 ajouté à E3b ; le bras « bizarre » reste comme contrôle d'instrument. |
| B-c | Δ(x) sur des conséquences engendrées à partir d'une autre idée x′. | **Acceptée.** | Contrôle de E1′. |

### Critiques de C

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| C-a (rang) | Un rang d'énumération n'est pas une probabilité d'atteinte ; un tirage uniforme sur classes ne les ordonne pas. | **Acceptée.** Sous tirage uniforme sur classes, ν est la même constante pour toutes : mon E2 n'avait rien à comparer pour cette référence. | Le tirage uniforme sort du panel d'étroitesse et reste un bras. L'énumérateur donne une étiquette binaire exacte (rang ≤ b_ν ou non). |
| C-a (E1) | L'AUC vérifie la cohérence des étiquettes. | **Acceptée** (même défaut que B-a2). | E1′. |
| C-a (E3) | Injecter dans le vivier ne fixe pas l'effet en sortie ; le gain vaut q(1−p₀)s. | **Acceptée.** | E3a injecte en sortie finale (effet connu) ; l'injection dans le vivier mesure s séparément. |
| C-a (E5) | Battre une critique hors sujet ne montre pas que la critique aide par rapport au silence. | **Acceptée.** | Trois témoins dans E5′. |
| C-b (E2) | Spearman indéfini à variance nulle ; la concordance des rangs n'implique pas l'accord au seuil. | **Acceptée.** | E2′ mesure l'accord au seuil. |
| C-b (E3–E5) | Variance (d − Δ²)/n ; McNemar teste l'égalité, pas une marge. | **Acceptée.** | Intervalle sur la différence appariée contre la marge (T1). |
| C-b (E6–E8) | Ratios indéfinis ; présence et détection confondues en E7 ; signe non résolu en E8. | **Acceptée.** | Différences au lieu de ratios ; E7′ déclare mesurer un rendement ; E8′ non confirmatoire. |
| C-b (audits) | Un taux moyen ne borne pas l'erreur sur une variante de poids nul ; « antérieur » n'identifie pas « vu à l'entraînement ». | **Acceptée comme limite.** | Les fiches d'instrument rapportent le pire taux par strate. Le test de fuite détecte un signal de mémorisation, pas l'exposition. |
| C-c (leurres) | Produire les leurres par une autre grammaire, inertie établie indépendamment. | **Acceptée pour l'inertie indépendante. Transformée en test pour l'autre grammaire** : des leurres d'une autre grammaire peuvent être reconnaissables à leur forme, ce qui casserait l'appariement. | Un classifieur ne voyant que la forme doit rester à une AUC d'environ 0,5 ; sinon ces leurres sont écartés. |
| C-c | Injecter un leurre par le même canal que l'oracle. | **Acceptée.** | Contrôle de E3a. |
| C-c | Rejouer en A/A toute la procédure, choix compris. | **Acceptée.** | E3b. |
| C-c | Message neutre du même problème, même longueur. | **Acceptée.** | E5′. |

### Critiques de D

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| D-a1 | E1 ne teste pas la séparabilité sur les idées effectivement produites par des chercheurs. | **Acceptée.** | E1′ est répétée sur les sorties du pilote. |
| D-a2 | L'étiquette « inerte » du prédicteur de E7 dépend de Δ privé : fuite. | **Acceptée.** Erreur de ma part : le prédicteur n'était pas calculable sans la vérité retenue. | Prédicteur public seul (E7′). |
| D-a3 (coûts) | Plafonner à l'identique les appels au vérificateur bride l'énumérateur et PySR. | **Acceptée.** | Coût matériel mesuré (T3). Le test de D devient l'analyse primaire ; l'ancien plafond devient une analyse de sensibilité. |
| D-a3 (placebo) | Le placebo hors problème peut distraire. | **Acceptée** (comme C-a). | E5′. |
| D-a4 | Dimensionnement faux ; un juge à 0,10 de fausses alertes donne plus de 0,91 de fausses découvertes à prévalence 0,01. | **Acceptée** pour les deux. | Le seuil de 0,10 de ma fiche « juge » est retiré. À cette prévalence, viser 0,2 de fausses découvertes demanderait environ 0,002 de fausses alertes (ill.), soit environ 1 500 négatifs sans alerte (ill.) : le juge est exclu. |
| D-b1 | Troncature et effondrement du critère de demi-échantillons. | **Acceptée.** | E2′. |
| D-b2 | La puissance de certification décroît en exp(−K Σ_r p_r). | **Acceptée.** | Seules les idées avec Σ_r p_r ≲ 0,1/K sont certifiées avec une probabilité d'environ 0,9 (ill.). C'est écrit dans T2. |
| D-b3 | Formule de taille contre une marge non nulle. | **Acceptée**, et je m'en sers pour E4′. | n ≥ (z_α + z_β)²(ψ − θ²)/(θ − θ₀)². |
| D-b4 | Ratios à région de confiance non bornée (Fieller 1954, RAPPORTÉ par D) ; E8 sans décision. | **Acceptée.** | Différences ; E8′ non confirmatoire. |
| D-c1 | Canonisation adversariale par termes neutres. | **Transformée en verrou.** | Appartenance à une classe décidée par canonisation et équivalence numérique sur des points incluant les régimes d'intervention ; taux de fausse scission ≤ 1 % (ill.) sur des obscurcissements engendrés par modèle. |
| D-c2 | Placebo hors problème contre remplissage neutre intra-problème. | **Transformée en test**, tel que D l'énonce. | Si le hors-problème est inférieur au neutre, il est retiré comme témoin. |
| D-c3 | Égaliser en coût matériel total. | **Transformée en test** (voir D-a3). | E4′. |

### Critiques de E

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| E-a1, E-c3 | Fuite de la vérité retenue dans le prédicteur de E7 ; test d'invariance sous permutation des régimes retenus. | **Acceptée** (comme D-a2). | L'invariance devient un contrôle de code de E7′. |
| E-a2 (E1) | Vrai par construction ; leurres non appariés en ν sous modèle. | **Acceptée.** Je rejette seulement l'exigence implicite d'une « séparabilité générale », qu'aucun monde clos n'établit. | E1′ ; appariement en ν sous modèle revérifié après le pilote. |
| E-a2 (E3) | E3 sur processeur est satisfaite par construction et n'éprouve ni la canonisation des sorties de modèle ni le bruit de ν. | **Transformée en test.** Un contrôle positif est construit par nature : E3a vérifie la statistique de décision, et rien de plus. | E3b après le pilote, avec sorties de modèle. |
| E-a3 | Placebo destructeur ; conditionnement sur une variable post-traitement ; hétérogénéité confondue avec le niveau moyen. | **Acceptée** pour les trois. | La décomposition rappel/précision devient descriptive. L'attribution passe par le croisement vivier × sélecteur. Le bras « N copies » est lancé pour chaque famille. |
| E-a4 (test) | « Un seul test confirmatoire » contre 5 références et 3 budgets. | **Acceptée.** | Un budget primaire préenregistré ; les deux autres sont descriptifs. |
| E-a4 (jetons) | Sommer entrées et sorties confond des coûts différents. | **Acceptée.** | Coût matériel mesuré (T3). |
| E-a4 (ν) | Si ν n'inclut pas PySR ni le best-of-N, une idée banale pour eux est étiquetée EP. | **Rejetée comme lecture** : ma définition exige ν ≥ ν* « sous chaque référence ». **Acceptée sur le fond** : je n'avais chiffré que la calibration sous modèle. | Calibration de PySR ajoutée au plan. |
| E-a5 | E6 : couplage structurel public/privé. | **Transformée en test** (comme B-a7). | La conclusion de E6′ ne vaut que pour le niveau de couplage testé. |
| E-b | Saturation de ν et fausses alertes en e^{−3c} ; atténuation de Spearman ; borne d'AUC et corrélation intra-groupe ; quatre défauts de la décision E4, dont l'arrêt séquentiel sans frontière ; ratios ; E8. | **Acceptée** en bloc. | T1, T2, bootstrap par monde. |
| E-c1 | Bras « sans critique, jetons réalloués ». | **Acceptée.** Je me sers aussi d'une remarque que C adresse à une autre proposition : ce bras mesure une politique budgétaire, pas l'effet de lire une critique. Les deux témoins sont donc nécessaires. | E5′. |
| E-c2 | Paraphrases adversariales engendrées par les modèles. | **Transformée en verrou** (avec D-c1). | E3b. |
| E-c4 | Règles fausses non triviales passées au solveur : Δ ≤ 0 attendu. | **Acceptée.** | Contrôle de E1′. |
| E-c5 | A/A complet incluant la recalibration de ν. | **Acceptée.** | E3b. |

---

## (b) Expériences corrigées

### Changements transversaux

**T1. Règle de décision.**
- Le n est fixe, avec une seule analyse et aucune prolongation.
- La statistique est un intervalle à 95 % sur la différence appariée par monde, comparé à la marge (Newcombe 1998, *Statistics in Medicine*, RAPPORTÉ, page non vérifiée).
- Il y a trois issues : au-dessus, au-dessous, ou « instrument insuffisant ».

**T2. Étroitesse.**
- **Étiquette.** C'est une étiquette binaire censurée, pas un scalaire. « Étroite sous R » signifie zéro atteinte en K exécutions de R au budget de calibration b_ν. Ces exécutions sont disjointes de la comparaison et figées avant elle.
- **Panel.** Énumérateur (rang > b_ν, exact), PySR et modèle seul.
- **Puissance de certification.** Elle vaut environ e^{−KΣp} (D-b2). En pratique, « étroite » veut donc dire Σp ≲ 0,1/K, et non p ≤ 3/K.
- **Handicap.** Une référence du panel, rejouée au budget B = m·b_ν, atteint une idée certifiée avec une probabilité d'au plus environ m·p. Pour K = 300 et m = 10 (ill.), cela donne environ 0,3 % par idée.
- **Compromis.** « Certifiable » et « atteignable par la référence » ne sont compatibles que si m est de l'ordre de K.
- **Conséquence.** Le duel contre un membre du panel est signalé « non comparatif » dès que la borne passe sous la marge. Il reste une condition nécessaire, mais ne décide rien.

**T3. Coût.** C'est le coût matériel mesuré (secondes de GPU et de processeur valorisées), évaluations publiques comprises. Les jetons sont journalisés. Aucun bras n'accède à l'évaluation privée.

**T4. Juge.** Il est exclu de toute mesure primaire ou secondaire.

### E1′ — Δ se reproduit-il à rareté fixée ?

- **Population** : toutes les classes d'un espace énuméré exhaustivement, puis les sorties du pilote. Il n'y a aucune étiquette du concepteur.
- **Mesure** : deux jeux de conséquences C1 et C2, tirés par le générateur de régimes avant toute idée et sans la connaître, et deux solveurs S1 et S2.
- **H_A** : dans chaque strate de rang d'énumération, la proportion de classes « profondes » selon (C1, S1) qui le restent selon (C2, S2) est d'au moins 0,7 (ill.).
- **H_B** : elle est inférieure.
- **Contrôles** :
  - Δ sur les conséquences d'un autre monde doit être d'environ 0 (B).
  - Les règles fausses doivent donner Δ ≤ 0 (E).
  - Les régimes permutés doivent ramener au taux de base.
  - Le verrou de non-saturation doit être passé.
  - Le bootstrap se fait par monde.
- **Si H_A est retenue** : « à rareté fixée, Δ n'est que du bruit » est réfutée pour cette famille.
- **Si H_B est retenue** : ma définition de la profondeur est réfutée, et on arrête.

### E2′ — L'étiquette « étroite » dépend-elle de la référence ?

- **H_A** : parmi les classes étroites sous une référence du panel, la proportion étroite sous une autre est d'au moins 0,6 (ill.).
- **H_B** : elle est inférieure. La cible doit alors nommer R.
- **Contrôles** : l'accord test-retest de l'étiquette sur deux moitiés disjointes d'exécutions ; les mondes ré-encodés.
- **Rapporté en plus** : la part de classes non résolues.

### E3a puis E3b — Verrou

- **E3a** (processeur) :
  - Une idée EP est injectée en sortie finale avec une probabilité q, ν étant figée.
  - Un leurre injecté par le même canal doit donner un gain nul.
  - Un test A/A complète l'ensemble.
  - H_A et H_B sont inchangées.
  - E3a ne valide que la statistique de décision.
- **E3b** (après le pilote) :
  - **A/A complet.** Il porte sur des sorties de modèle et rejoue toute la procédure, recalibration de ν comprise.
  - **CN-2.** Le chasseur d'étroitesse tourne sur des mondes sans idée EP. H_A : son taux EP ne dépasse pas le taux de fausses alertes admis. H_B : il le dépasse, et le critère est alors perméable à la rareté seule.
  - **Obscurcissements.** Ceux engendrés par modèle sont soumis à la canonisation.
- **Arrêt** : tout échec arrête le plan.

### E4′ — Comparaison

- **Bras** : le système ; le panel (énumérateur, PySR, modèle seul en fil unique et en best-of-N) ; et deux bras CN-1 hors panel, à savoir la référence à température relevée et une autre famille avec consigne paraphrasée.
- **Métrique** : P(au moins un succès EP parmi k finales), en différence appariée par monde, au budget primaire.
- **H_A** : la différence est d'au moins +5 points (ill.) contre chaque bras.
- **H_B** : elle est inférieure contre au moins un bras.
- **Décision** : H_A si toutes les bornes inférieures dépassent la marge. H_B si une borne supérieure est sous la marge. Sinon, l'instrument est insuffisant.
- **Taille** : 600 mondes (ill.), pour un écart vrai de 10 points et une discordance de 0,20. La puissance conjointe est au plus celle du contraste le plus faible.
- **Lecture** :
  - Une victoire contre le panel seul, sans victoire contre les CN-1, réfute l'affirmation : l'avantage est alors de la divergence.
  - Le secondaire obligatoire est le succès « profond » sans condition d'étroitesse, où aucun bras n'est handicapé.

### E5′ — Attribution

- **Plan** : le factoriel reste. La critique active doit dépasser chacun des trois témoins : hors problème, neutre intra-problème, et sans critique avec jetons réalloués.
- **Sélection** : le croisement vivier × sélecteur l'attribue par intervention.
- **Hétérogénéité** : elle est testée contre le meilleur bras homogène, désigné sur des mondes de développement.

### E6′ — Retour

- **Estimande** : l'écart (public − privé) sous F2, moins le même écart sous F0.
- **Facteur** : couplage fort ou faible entre conséquences publiques et privées.
- **Contrôle positif** : F3, avec un troisième jeu vierge.
- **Portée** : toute conclusion est indexée par le niveau de couplage.

### E7′ — Régions (exploratoire)

- **Prédicteur** : la dispersion des prédictions hors régimes observés parmi les M candidats les mieux ajustés au public. Il se calcule sans vérité retenue.
- **Plan** : prévalence plantée égale entre strates ; différence de taux entre deux moitiés.
- **Portée** : E7′ mesure un rendement de recherche, pas l'existence de régions.

### E8′ — Transport

Le plan est inchangé, mais le test devient non confirmatoire. Il ne conclut que si chaque effet a un intervalle excluant zéro dans les deux domaines.

### Plan révisé (ill.)

1. Arithmétique de T2 pour les (K, m, ν*) retenus. Coût nul.
2. Instruments, E1′, E2′ mécanique, E3a. Processeur, moins de 200 cœur-heures.
3. Pilote ν sous modèle (20 mondes), E3b.
4. E6′.
5. Calibration : 600 mondes × 300 exécutions × b_ν. C'est toujours le poste dominant.
6. E4′, puis E5′ si H_A.
7. E7′ et E8′.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

Aucun résultat empirique n'existe : rien n'a été exécuté. Ce qui tient est de deux ordres.

- **Littérature (RAPPORTÉ dans ma pièce, pages non vérifiées)** :
  - la borne 3/K (Hanley & Lippman-Hand 1983) ;
  - la dégradation d'un jeu retenu par usage adaptatif (Dwork et al. 2015) ;
  - les biais de juge en général (Zheng et al. 2023 ; Panickssery, Bowman, Feng 2024).
- **Arithmétique des critiques**, avec les statuts de leurs auteurs :
  - La censure de l'étroitesse au plafond log₂(K/3).
  - La décroissance de la puissance de certification en exp(−KΣp), VÉRIFIÉ selon D.
  - Le dimensionnement contre la marge et non contre zéro, VÉRIFIÉ selon C, D et E.
  - La borne de handicap, HYPOTHÈSE selon B. Je l'ai refaite à la main et la tiens pour correcte ; elle n'a pas été auditée.

### Ce qui n'est pas établi

- Que la profondeur Δ soit reproductible à rareté fixée (E1′).
- Que « étroit » ait un sens sans nommer la référence (E2′).
- Que le taux de base soit mesurable.
- Qu'un système multi-agents batte quoi que ce soit.
- Que des régions favorables existent.
- Qu'un résultat en monde clos se transporte.

### Où le cadrage est fautif

« Rarement atteint par la recherche ordinaire » et « meilleur que les références » ne sont pas indépendants. Si la référence définit l'ordinaire, elle perd par définition (B-a1). L'affirmation réfutable devient : « à coût égal, le système trouve des idées profondes, étroites pour un panel figé, plus souvent que des variantes trivialement divergentes de ce panel ».

### Confiance révisée par point

| Point | Confiance | Motif du changement |
|---|---|---|
| 1. Cible | 0,5 | L'étroitesse est binaire et censurée ; Δ n'est pas encore éprouvé. |
| 2. Sources | 0,65 | Inchangé ; le juge est exclu. |
| 3. Comparaison | 0,6 | Handicap ; marge ; CN-1. |
| 4. Choix de problèmes | 0,25 | Mon prédicteur fuyait ; E7′ est exploratoire. |
| 5. Retour | 0,55 | Le résultat dépend du couplage. |
| 6. Validation | 0,75 | Renforcée par CN-1, CN-2 et E3b. |
| 7. Plan | 0,5 | Tailles multipliées par quatre. |
| 8. Limites | 0,55 | Le compromis de T2 s'ajoute. |

### Preuves que la cible est mal posée ou le harnais infaisable

- E1′ retient H_B.
- Les bras CN-1 gagnent autant que le système en E4′.
- Aucun couple (K, m) abordable ne sort tous les bras du plancher.
- E3b échoue.

### L'expérience à faire en premier

1. **Le calcul de T2, à coût nul.** Pour les K, m et ν* envisagés, on calcule la borne de handicap et la puissance de certification. Si aucun réglage ne laisse un bras hors système au-dessus du plancher, la forme comparative de la cible est à abandonner avant d'écrire du code.
2. **E1′ sur processeur.** Si l'étiquette « profonde » ne se reproduit pas entre deux jeux de conséquences et deux solveurs indépendants, à rareté fixée, la définition de la profondeur tombe et rien d'autre ne mérite d'être lancé.

FIN-DE-CELLULE