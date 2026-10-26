# Proposition B · Tour III.2 : équipe rouge croisée

**État des pièces.** La pièce FAITS est vide par décision de l'arbitre (message n° 28 § 1) ; je n'invente aucun fait. Les pièces A et C sont présentes, se terminent par leur marqueur de fin et ne paraissent pas coupées. Je ne peux pas vérifier les empreintes sha256 : elles sont reprises telles quelles, non auditées.

**Conventions.** Je ne prête à A et à C que ce qui figure dans leur texte. Tout chiffre de ma main repose sur un paramètre illustratif tiré de la question ou des pièces, et porte la mention « illustratif ». Les calculs sont montrés. Dans les expériences, les étiquettes H_A et H_B désignent des hypothèses et non les propositions A et C.

---

## Contre la proposition A

### (a) Failles

**A-1. Les duels violent B4, et A le démontre lui-même.**
- **Duel 1.** H_A est falsifiée si la puissance est inférieure à 0,5 ; H_B l'est si elle dépasse 0,8. Entre les deux, rien n'est falsifié.
- **Duels 2, 3 et 5.** Ils exigent un intervalle de confiance entièrement au-dessus de δ, ou entièrement dans [−δ, δ]. Un tel intervalle doit être plus étroit que δ.
- **Ce que dit le calcul de A.** Sur la famille 2, avec D = 6 items discordants, un item sur 24 et une seule graine, la variance vaut (1/24)·(0,25 − Δ²), soit environ 0,01. L'écart-type est donc d'environ 0,10 (illustratif, paramètres de A).
- **Conséquence.** Un intervalle à 90 % a une demi-largeur d'environ 0,16 (illustratif), plus large que δ = 0,10. L'issue la plus probable de chaque duel est donc la zone non falsifiante. A conçoit des instruments que sa propre analyse de puissance déclare non concluants.

**A-2. Le contrôle négatif du factoriel n'existe pas.**
- Le plan 2^{4−1} de résolution IV, de générateur I = ABCD, compte 8 essais, soit 7 contrastes.
- Ces 7 contrastes se répartissent ainsi : 4 effets principaux, chacun aliasé avec une interaction d'ordre 3 (par exemple D = ABC), et 3 paires d'interactions d'ordre 2 aliasées entre elles (AB = CD, etc.).
- Il ne reste aucun contraste libre. Le « contraste alias d'ordre 3 (attendu nul) » de A est en fait un effet principal.
- Avec une seule graine et un bootstrap sur les items, aucun terme ne mesure l'erreur pure entre graines. Les intervalles des contrastes ignorent une variance que A juge pourtant importante.
- Deux interactions de signes opposés aliasées ensemble (AB + CD ≈ 0) font paraître le système additif : l'hypothèse A3 est validée par construction du plan.

**A-3. Le détecteur de plateau est presque aveugle.**
- La règle de A : deux crans consécutifs dont la borne supérieure de l'intervalle à 90 % reste sous δ.
- Avec l'écart-type d'environ 0,10 de la famille 2, cela demande Δ̂ < 0,10 − 1,645 × 0,10 ≈ −0,064. Sur un vrai plateau (Δ = 0), cela arrive avec une probabilité Φ(−0,64) ≈ 0,26 par cran (illustratif).
- Deux différences consécutives partagent le bras du milieu avec des signes opposés. Leur corrélation est négative (environ −0,5 si les variances sont égales, illustratif). La probabilité conjointe tombe donc sous 0,26² ≈ 0,07 (illustratif).
- Conséquence : un vrai plateau n'est presque jamais déclaré, et l'escalier monte faute de pouvoir s'arrêter.

**A-4. La règle d'arrêt par λ n'est pas définie dans le régime typique.**
- Le coût par point vaut C_k / (100 · borne inférieure). Quand la borne inférieure est négative, ce qui est le cas courant d'après A-1, le ratio est négatif et ne « dépasse » jamais λ.
- Combinée à A-3, cette règle n'arrête rien.
- De plus, il faut avoir exécuté le cran k+1 pour connaître son intervalle. L'arrêt survient donc toujours un cran trop tard, et ce cran est payé.

**A-5. Une fuite entre construction et évaluation, à deux endroits.**
- *Les deux répliques gratuites* servent à la fois à calibrer le bruit et à mesurer le taux de fausse alerte de l'essai A/A.
  - Un test de permutation est exact sous échangeabilité. L'appliquer à deux graines d'une même configuration ne fait que vérifier cette échangeabilité, vraie par construction.
  - Le vrai risque est la non-échangeabilité entre configurations (canal « réponse invalide », format). Ce contrôle ne la voit pas.
  - Rééchantillonner les items d'une seule paire A/A donne une distribution conditionnelle à une seule réalisation de graines.
- *La réserve* est l'unique remède de la zone grise (« ajouter des items de la réserve ») et aussi le support de la confirmation finale.
  - Avec m crans en zone grise, m ponctions sont faites sur la réserve. La confirmation porte alors sur une réserve consommée.
  - Le jeu d'items change d'un cran à l'autre, ce qui rompt l'appariement le long de l'escalier.

**A-6. L'injection d'effet est vraie par construction.**
- Basculer au hasard ⌈δ/w⌉ items suppose que les items sont échangeables.
- Or un vrai gain se concentre sur certains items, par exemple les items durs où le classifieur trivial échoue. La puissance mesurée sur le banc est donc celle du modèle de A, pas celle du système.

**A-7. Le tableau de puissance est incohérent.**
- La colonne « graines par bras pour saturer : 2–3 » n'est pas dérivée.
- Les puissances de 0,12 à 0,44 sont des McNemar exacts à **une** graine et à D fixé. Le nombre K de graines n'y intervient pas.
- La décomposition d_ki = δ′_i + u_i + v_k + e_ki contient deux termes par item, δ′_i et u_i, qui ne sont pas identifiables séparément.
- La phrase « irréductible à items fixes » se contredit : si l'on raisonne à items fixes, le terme lié aux items disparaît (C le dit correctement).

**A-8. Une confusion temporelle non traitée.**
- L'escalier est séquentiel : l'indice du cran est confondu avec la date d'exécution (dérive silencieuse du fournisseur, limites de débit, cache).
- L'« ancre » de A ne couvre que le changement de version du système, pas la dérive à version constante.
- A dit que b est « randomisé » pour l'estimateur à variable instrumentale. Rien dans le plan ne randomise l'ordre des bras.

**A-9. Le Duel 3 conditionne sur une variable postérieure au traitement.**
- Apparier les items à dépense s égale sélectionne, dans le bras à budget élevé, les items sur lesquels le système s'est arrêté tôt, c'est-à-dire les faciles. Un écart de BA apparaît alors par simple sélection.
- Retirer la mention du budget dans l'invite ne teste qu'un canal. Si b agit par max_tokens ou par la configuration, l'exclusion est violée sans que le duel la voie.
- Enfin, l'ablation crée un nouveau traitement, ce qui confond deux causes.

**A-10. Les statuts sont mal attribués (règle 1).**
- A7 porte le statut OBSERVÉ-NON-AUDITÉ alors que rien n'a été observé, puisque FAITS est vide : c'est une HYPOTHÈSE.
- A10 porte le statut « Illustratif », qui n'est pas l'un des quatre statuts admis.
- En § 0, « RAPPORTÉ … illustratif » accolés sur le même chiffre est ambigu.
- A et C supposent tous deux que les répliques gratuites sont celles de la configuration de **base**. La question dit seulement « de la même configuration » : c'est une HYPOTHÈSE.

### (b) Scénarios d'évasion

Coûts illustratifs : 16 USD par graine et par bras, milieu de la fourchette 10–22 USD de la question, elle-même illustrative.

| Instrument de A | Manœuvre adverse | Coût |
|---|---|---|
| Permutation / McNemar pondéré | Lancer des graines hors journal, ne garder que 3 graines favorables. « Rapporter chaque graine » ne protège que les graines déclarées. | Environ 16 USD par graine cachée (illustratif) |
| Bootstrap, couverture sur A/A | Rien à faire : il passe par construction (A-5). Le vrai écart est logé dans le canal invalide ou dans le format. | 0 |
| Détecteur de plateau + λ | Aucune manœuvre nécessaire : il ne déclenche presque jamais (A-3, A-4). Un opérateur qui veut la configuration chère n'a qu'à continuer. | 0 |
| Variable instrumentale (Duel 3) | Faire lire b par le système via la configuration plutôt que par l'invite. L'ablation de l'invite passe. | 0 |
| Factoriel 2^{4−1} | Choisir le générateur, donc l'alias, qui masque l'interaction gênante. | 0 |
| Règle « minimum des familles » | Dégrader la famille 2 de 2 items (environ 0,083 < δ, illustratif) pour gagner sur la famille 1. La règle « rester si une famille perd plus de δ » ne se déclenche pas. | 0 |
| Zone grise → réserve | Provoquer une zone grise à chaque cran pour vider la réserve avant la confirmation. | Environ 1 cran par ponction |

**Tous à la fois.** Un opérateur décidé à faire adopter le bras coûteux procède ainsi :
- il choisit l'ordre des axes et le générateur du factoriel ;
- il cache 2 à 4 graines par bras ;
- il laisse l'escalier monter faute d'arrêt effectif ;
- il épuise la réserve par les zones grises.

Coût supplémentaire : environ 100 à 250 USD (illustratif), en plus du budget de A estimé à environ 600 USD. Ce sont les règles de A elles-mêmes qui rendent cette fraude bon marché. Seuls un journal scellé, chaque essai étant engagé par son empreinte avant exécution, et un exécutant distinct de l'analyste la rendent coûteuse.

### (c) Contrôles négatifs dont l'absence serait fatale

Chaque contrôle est écrit sous forme de duel B4 : les deux issues falsifient quelque chose.

| Contrôle | H_A | H_B | Issue |
|---|---|---|---|
| **Base rejouée en entrelacé** (début, milieu, fin de l'escalier, même version) | Pas de dérive temporelle : écart entre base précoce et base tardive inférieur à 1 item net | Dérive d'au moins 2 items nets | Écart d'au moins 2 items : H_A falsifiée, les Δ de l'escalier sont invalides. Écart inférieur à 1 : H_B falsifiée. Seuils illustratifs, à sceller. |
| **Provenance des rondes de mise au point** : empreintes des données utilisées par R, croisées avec les empreintes des 60 items et de la réserve | Intersection vide | Intersection non vide | Non vide : H_A falsifiée, l'axe R mesure une fuite. Vide : H_B falsifiée. Sans ce contrôle, l'axe que A place en premier est ininterprétable. |
| **A/A hors échantillon** : une troisième exécution de la base, jamais utilisée pour calibrer | Le taux de fausse alerte du test reste nominal sur une paire non utilisée pour construire le modèle de variance | Il dépasse le nominal | Dépassement : H_A falsifiée. Sinon : H_B falsifiée. C'est le seul moyen de rompre la fuite A-5. |
| **Placebo de format** : mêmes sorties, réanalysées avec troncature à la longueur L du bras rival, sans nouvel appel | Δ ne vient pas du parsing | Δ vient du parsing | Changement de signe de Δ : H_A falsifiée. Sinon : H_B falsifiée. Coût quasi nul. |
| **Réplicat d'erreur pure dans le factoriel** : au moins 2 points centraux ou 2 graines sur 2 configurations | Les contrastes dépassent l'erreur pure | Ils n'excèdent pas l'erreur pure | Sans ce réplicat, le Duel 2 n'a aucun dénominateur. |

---

## Contre la proposition C

### (a) Failles

**C-1. Le choix du régime d'inférence n'est pas scellé.**
- Le tableau offre deux régimes côte à côte : « super-population » (puissance 0,55 à δ = 0,10, K = 1) et « conditionnel aux 60 items » (0,94).
- C conclut que le second « justifie l'exigence Δ ≥ 0,10 ». Choisir le régime après coup est une bifurcation analytique.
- Le régime conditionnel ne parle que de ces 60 items. Or c'est précisément ce régime qui rend nuisible la réutilisation du jeu le long de l'escalier : on optimise sur l'ensemble même sur lequel on conclut.

**C-2. La puissance à δ = 0,10 est surestimée par l'approximation normale.**
- Paramètres de C : p_d = 0,20, soit 12 items discordants sur 60 ; Δ = 0,10, soit 6 items nets, d'où n₁₀ = 9 et n₀₁ = 3 ; poids égaux ; une graine.
- Seuil du McNemar exact unilatéral à α = 0,05 sur 12 discordants :
  - P(X ≥ 10 | ½) = 79/4096 ≈ 0,019 ;
  - P(X ≥ 9 | ½) = 299/4096 ≈ 0,073, donc on rejette à partir de X ≥ 10.
- Puissance pour p = 0,75 : 66·0,75¹⁰·0,25² + 12·0,75¹¹·0,25 + 0,75¹² ≈ 0,232 + 0,127 + 0,032 ≈ **0,39** (illustratif), contre **0,55** chez C.
- La discrétude, que C reconnaît pourtant au point 2, coûte environ 16 points de puissance (illustratif). Les poids de BA par famille (1/48 contre 1/72) augmentent encore la variance d'environ 4 % (facteur donné par C).

**C-3. La spécification d'étalonnage contredit le modèle de C.**
- Instrument 3 : C exige une détection d'au moins 80 % à ΔBA = +0,118 avec p_d = 0,20.
- Avec la formule de C : écart-type = √((0,20 − 0,118²)/60) ≈ 0,0557 ; z = 0,118 / 0,0557 − 1,645 ≈ 0,47 ; puissance Φ(0,47) ≈ **0,68** (illustratif), et moins en calcul exact.
- L'instrument échoue donc à sa propre spécification, ou bien le seuil a été posé sans calcul.

**C-4. La borne de Thresholdout réfute la recommandation de C.**
- C présente comme démontrée (« la théorie … montre ») une borne O(√(T·log 2 / N)). Pour T = 6 et N = 60 : √(6 × 0,693 / 60) ≈ **0,26** (illustratif), soit 2,6 fois δ. Même pour T = 1 : √(0,693 / 60) ≈ 0,107 > δ.
- La « voie statistiquement supérieure » est donc non informative à N = 60.
- Le mécanisme de Dwork et al. (2015) suppose en outre un jeu d'entraînement distinct et un bruit ajouté aux réponses du jeu tenu à l'écart. Le plan de C n'a ni l'un ni l'autre.
- C'est une HYPOTHÈSE présentée comme résultat (règle 1).

**C-5. Le contrôle de l'erreur familiale par séquence fixe n'est pas valide ici.**
- La séquence fixe exige un ordre prédéfini. Or C choisit la « trajectoire gagnante » après le mini-factoriel de l'expérience 3 : l'ordre dépend des données.
- Chaque étape compte deux regards : décision à K = 1, puis seconde graine en zone grise, testée à nouveau à p < 0,05, sans dépense d'α. L'α par étape dépasse donc 0,05.
- « Contrôlé mathématiquement sans aucune perte de puissance » est une formulation de certitude (règle 5).

**C-6. La parade contre la régression vers la moyenne est indisponible et insuffisante.**
- Indisponible : sur le chemin nominal, le vainqueur n'a qu'**une** graine (K₀ = 1). Il n'existe pas de « 2ᵉ réplique » sauf en zone grise.
- Insuffisante : une graine fraîche ne corrige pas la malédiction du gagnant au niveau des items, puisque le vainqueur a été choisi sur les mêmes 60 items.

**C-7. L'expérience 1 présente une fuite et une hypothèse vraie par construction.**
- Y_iA1 figure à la fois au numérateur (A1 contre A2) et au dénominateur (B1 contre A1) du ratio ρ_G, ce qui corrèle les deux estimations.
- σ̄²_G de la différence vaut deux fois la variance de graine de A. C'est vrai seulement si B est aussi instable que A, or B diffère précisément par le nombre d'itérations ou de sous-modèles.
- Le seuil de 0,50 porte sur une estimation ponctuelle tirée de 60 désaccords de Bernoulli, sans intervalle.
- Le contrôle « température 0 ou cache » vaut zéro par construction : il teste la plomberie, pas l'estimateur.
- La décision « K = 1 partout » n'a pas le même sens selon le régime (C-1). En régime conditionnel, le bruit de graine est la seule source de bruit.

**C-8. L'expérience 2 sélectionne sur une variable postérieure au traitement.** C'est la même faille que A-9, en plus net : les « items où l'allocateur s'est arrêté spontanément à s ≈ b_bas » sont les items faciles. Un écart de BA à dépense égale est attendu même si l'exclusion est vraie.

**C-9. La règle de dominance ne comporte aucun test.** « Δs ≤ 0 et ΔBA ≥ 0 ⇒ MONTER » repose sur une estimation ponctuelle. Une égalité bruitée suffit, et le test dépend entièrement de la comptabilité de s.

**C-10. Statuts et confusions.**
- Les coûts de 10 à 22 USD et de 10 USD sont marqués « (illustratif) » par la question elle-même. C les étiquette RAPPORTÉ à de nombreuses reprises : c'est un changement de statut (règle 1).
- « 69 % des items résolus par la forme » confond la BA du classifieur trivial, 0,69, avec une part d'items trivialement réussis par le système.
- Le « +0,23 sur le sous-ensemble non trivial » n'est pas reproductible à partir des chiffres donnés : 0,10 × 60/35 ≈ 0,17, et 0,10 × 36/11 ≈ 0,33, illustratif.
- « Écart-type incompressible dû aux graines » est faux : cet écart diminue en 1/√K.
- La confusion temporelle A-8 vaut aussi pour C : aucun entrelacement, aucune randomisation de l'ordre des bras.

### (b) Scénarios d'évasion

| Instrument de C | Manœuvre adverse | Coût |
|---|---|---|
| Dominance par le coût | Déplacer la dépense hors de s : compter les rondes R comme « coût fixe », ou faire servir des appels par le cache sans facturation. B passe sans aucun test. | 0 |
| Auditeur « trop propre » | Laisser n₀₁ ≥ 1 à 2 régressions volontaires et garder |Δ| < 0,35. Une fuite partielle donnant +0,30 passe l'audit. | 1 à 2 items sacrifiés (illustratif) |
| Expérience 1 (choix de K) | Baisser la température ou activer le cache pendant la mesure (σ̄²_G ≈ 0, donc K = 1 pour toujours), puis remonter la température pour l'escalier. | 0 |
| Choix du régime | Annoncer le régime conditionnel après avoir vu les résultats (écart-type ≈ 0,03, illustratif). Cinq items nets suffisent alors. | 0 |
| Zone grise | Viser +0,03 < Δ̂ < +0,10 pour obtenir un second tirage à α plein, sans pénalité. | Environ 16 USD (illustratif) |
| Séquence fixe | Réordonner les axes après le 2 × 2. | 0 |
| Expérience 2 | Programmer un arrêt précoce sur les items faciles. Le test à dépense égale lit alors un effet de difficulté. | 0 |
| Graine | Si l'aléa vient du fournisseur et non de la graine, « K graines » est une fiction. Personne ne vérifie que la même graine donne la même sortie. | 0 |

**Tous à la fois.** Un opérateur qui veut faire adopter B procède ainsi :
- il fixe la température basse pendant l'expérience 1, d'où K = 1 ;
- il choisit le régime conditionnel ;
- il laisse 1 à 2 régressions pour rester sous l'audit ;
- il utilise la zone grise comme second tirage ;
- il réordonne les axes.

Coût marginal : environ 16 à 50 USD (illustratif) sur un budget de C de 124 USD (illustratif). Le plan de C est le moins cher à exécuter, et il est aussi le moins cher à tromper. Ces deux propriétés viennent des mêmes choix : K = 1, estimations ponctuelles, régime non scellé.

### (c) Contrôles négatifs dont l'absence serait fatale

| Contrôle | H_A | H_B | Issue |
|---|---|---|---|
| **Même graine rejouée deux fois** (le pendant manquant du contrôle « température 0 ») | La graine détermine l'aléa : sorties identiques | Aléa non contrôlé par la graine | Sorties différentes : H_A falsifiée, tout le modèle à deux niveaux de C tombe. Sorties identiques : H_B falsifiée. Coût : 1 exécution, environ 16 USD (illustratif). |
| **A/A sur la règle complète en deux temps** (K = 1, puis seconde graine en zone grise), sur des paires A/A non utilisées pour calibrer | α effectif ≤ 0,05 | α effectif > 0,05 | Dépassement : H_A falsifiée, le contrôle par séquence fixe n'est pas acquis. Sinon : H_B falsifiée. C n'étalonne que le test à un seul regard. |
| **Base rejouée en entrelacé** | Comme contre A | | |
| **Provenance des rondes R** | Comme contre A | | |
| **Appariement à dépense égale sur une covariable antérieure au traitement** (difficulté mesurée sur la base, ou désaccord avec le classifieur trivial) au lieu de s | L'effet de b à difficulté égale est nul | L'effet est non nul | Remplace l'expérience 2. Les deux issues sont interprétables, ce qui n'est pas le cas de l'appariement sur s. |
| **Rapprochement de s avec la facturation** | s journalisé = montant facturé (à ±5 %, illustratif) | Écart | Écart : H_A falsifiée, la règle de dominance est inutilisable. |

---

## Ce dont je me sers, en le disant (B1)

**1. Le désaccord entre A et C sur la puissance à δ = 0,10 est un instrument.**

A annonce une puissance d'environ 0,2 à 0,3, C d'environ 0,55 à 0,94. Le désaccord n'a pas à être lissé : il désigne trois variables cachées que l'arbitre peut trancher par le calcul, avant toute dépense :
- le régime d'inférence (super-population ou conditionnel) ;
- la discrétude (test exact ou approximation normale) ;
- la granularité (familles séparées ou poolées).

Mon calcul exact (C-2) donne environ 0,39 dans le cadre de C (illustratif). Cette valeur se situe entre les deux, plus près de A. La conclusion de A selon laquelle δ = 0,10 est sous la résolution de l'instrument à 60 items tient en super-population. Elle ne tient pas en régime conditionnel, qui est aussi le seul où la réutilisation du jeu pose problème.

Duel B4, sans nouvel essai :
- **H_A** : à p_d = 0,20, avec le test exact et les poids de BA par famille, la puissance est inférieure à 0,5.
- **H_B** : elle est d'au moins 0,5.
- Le calcul est fermé, et l'une des deux est falsifiée.

Ce duel reste conditionnel à p_d. Seule la mesure de p_d sur des données réelles rend le résultat applicable, comme A le demande à juste titre.

**2. J'adopte la critique de C contre la scission 40/20 (puissance de confirmation d'environ 26 %, illustratif) pour attaquer le régime (ii)+(iii) de A.** J'adopte en retour C-4 contre l'option B de C. Il ne reste aucune voie de réutilisation qui garde à la fois la puissance et la validité à N = 60. La seule voie que ni A ni C ne réfute est celle d'items nouveaux, dont A dit à raison que le coût humain n'est pas estimable.

**3. Les deux propositions partagent trois angles morts fatals :**
- l'ordre temporel des bras ;
- la provenance des données des rondes R ;
- le contrôle A/A construit sur les mêmes répliques que celles qui servent à calibrer le bruit.

FIN-DE-CELLULE