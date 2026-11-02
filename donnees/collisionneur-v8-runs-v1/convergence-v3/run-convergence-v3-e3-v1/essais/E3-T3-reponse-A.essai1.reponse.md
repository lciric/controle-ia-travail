# Proposition A — tour III.3 : réponse aux critiques, expériences corrigées, réponse à l'arbitre

**Pièces** : les cinq pièces et les quatre critiques sont lisibles entières ou dans l'extrait annoncé. Non servis : le PDF de Bailey et collègues, le pilote `4d1fb23f…`, la liste `resultats` du calibrage. Tout chiffre du pilote v4 reste RAPPORTÉ (brouillon 4, recoupé par la vérification), jamais vérifié par moi. Statuts : VÉRIFIÉ = lu dans le code servi ou recalculé sur la pièce 5 ; RAPPORTÉ ; OBSERVÉ-NON-AUDITÉ ; HYPOTHÈSE.

Je ne réponds qu'aux sections visant A. Je regroupe les critiques par objet, chacune attribuée.

---

## (a) Pour chaque critique : acceptée, rejetée, ou transformée en test

### 1. La valeur nulle de I3 et mon présupposé A4

**E (VÉRIFIÉ) : une loi i.i.d. à peu de modes ne peut pas produire I3 > (t−2)/(t−1).** **Acceptée, et je retire A4 dans sa première moitié.** Conditionnellement au déplacement courant v_t, les t−1 cosinus passés sont i.i.d., donc échangeables ; le maximum des t−2 premiers dépasse le dernier avec probabilité exactement (t−2)/(t−1) pour toute loi continue, quel que soit le nombre de modes ; des atomes et le test strict `>` (VÉRIFIÉ, `taux_retours`) ne peuvent que baisser cette probabilité. Mon argument « peu de bassins → I3 gonflé sans dynamique » était faux. Ce qui tient de A4 : (i) la nulle est violée **vers le bas** par le départ chaud (VÉRIFIÉ, `departs_suppl=[attaques[-1]]`), ce que D et B′ montrent (RAPPORTÉ : −0,23 à −0,38) ; (ii) sous A, l'attaque t dépend du moniteur t−1, lui-même fonction des attaques passées : la loi n'est pas échangeable par construction, quelle que soit la « dynamique ». L'excès de A au-dessus de 0,7345 mesure donc une **dépendance temporelle** réelle, mais pas forcément ce que la Table 5 appelle « cycle ».

**E et D : la permutation teste l'échangeabilité temporelle, pas un cycle ; huit tours n'identifient aucune période ; une alternance stochastique ou une dérive la fait rejeter.** **Acceptées.** Je retire le mot « cycle » de toute lecture issue de I3 ou de sa permutation ; la lecture devient « retours non échangeables ». La périodicité est un objet distinct, mesuré à part (autocorrélation des cosinus aux décalages 2 et 3, descriptif, sans verdict à T = 8).

**C4 : permuter brise l'autocorrélation de pas 1 induite par le départ chaud, ce qui gonfle I3 sous permutation ; l'instrument confond inertie de l'optimiseur et absence de cycle.** **Transformée en test.** C'est exactement la raison pour laquelle le test doit être **bilatéral** et **comparé à un témoin au même attaquant** : le bras A0 (M0 gelé huit tours, même attaquant, même départ chaud, même départ vers l'origine) fournit la loi de I3 et de son rang de permutation **quand le moniteur ne bouge pas**. La question « dynamique ou géométrie » devient : le rang de permutation de A diffère-t-il de celui de A0, apparié par instance ? D (contrôle c.5, « trajectoire produite par l'optimiseur seul, moniteur gelé ») demande le même témoin.

**D : retirer le départ vers l'origine change l'attaquant et les données d'entraînement.** **Acceptée** ; l'ablation ne se fait plus que sur A0, où aucun entraînement n'a lieu : elle n'affecte alors que l'attaquant.

**B-A3 et C-(b)2 : puissance non calculée ; dégénérescence de la loi de permutation en présence d'égalités.** **Acceptées en partie.** La permutation se calcule sur les vecteurs observés : des atomes y produisent des égalités que l'on compte (part de tâches avec cosinus égaux à 10⁻⁹, rapportée) ; c'est un avantage sur la nulle gaussienne, pas un défaut. Puissance : à préenregistrer par simulation sur le pilote avant gel, comme la S10 du brouillon 4 ; aucun chiffre ici.

**E (contrôles) : lois i.i.d. multimodales, lois atomiques, Markov alternante sans période.** **Acceptée** : elles entrent au banc d'instruments de l'expérience E2 ci-dessous, avec les trajectoires fabriquées de D (périodique, convergente, i.i.d. unimodale, i.i.d. multimodale).

### 2. Le Duel 1 : confondants, sélection, exclusivité

**B-A2, C1, E : A_q diffère de A sur deux axes (pondération q contre uniforme ; attaques de B contre attaques de A).** **Acceptée.** Correction : plan 2 × 2 {attaques de A, attaques de B} × {uniforme, équilibre q}. Les deux cellules manquantes sont A_q^A (q calculé sur la matrice 9 × 9 des moniteurs et attaques de A ; VÉRIFIÉ : le code ne construit G que pour B et B′, mais les moniteurs, attaques et échantillons d'évaluation de A existent, la matrice se calcule par `taux_cache`) et A_unif(B) (moniteur linéaire entraîné contre le mélange uniforme des attaques de B ; témoin demandé par C-(c)1).

**C2, C-(b)1, D, E : le maximum sur treize candidats, évalués sur les mêmes tirages, est optimiste (ordre σ√(2 ln M / N) selon C) ; un maximum choisi après observation est une sélection.** **Acceptée.** Correction : plus de maximum. Chaque candidat de la **liste gelée** porte son propre contraste V(X) − V(A) avec bornes de Bonferroni sur la liste ; l'hypothèse porte sur l'union protégée, comme la Table 4 du brouillon 4. Si Lazar veut un seul chiffre « meilleur de la liste », il faut sélection sur un jeu de graines d'évaluation et estimation sur un autre, avec meilleure réponse fraîche contre le sélectionné — je ne le recommande pas.

**E : le maximum sur une liste est une borne inférieure du supremum sur la classe linéaire ; l'échec ne réfute pas l'existence d'un autre moniteur linéaire ni « tous les mécanismes qui rendent un moniteur pur ».** **Acceptée.** Je reprends la réparation d'E : H_A et H_B portent sur la **liste gelée**, pas sur l'existence. Conséquence pour les mécanismes (c), (f) : un échec de la liste ne les réfute qu'**en leur instance listée** (moyenne de directions, pire cas sur l'historique), pas en général.

**D : plafond de classe et mauvaise règle peuvent être vrais ensemble ; les hypothèses ne sont pas exclusives.** **Acceptée.** Les nouvelles hypothèses sont exclusives par construction : H_A « aucun membre de la liste ne bat A de m » contre H_B « au moins un le bat ».

**B-A4 : D − A est un contrôle positif ; le vrai contrôle négatif est A_moy sur neuf copies de M0.** **Acceptée**, étiquettes corrigées.

**E : moyenner les poids dépend de l'échelle, les décisions seuillées étant invariantes par transformation affine positive du score.** **Acceptée.** VÉRIFIÉ : pour un moniteur linéaire recalibré au quantile 1 − α, multiplier (W, b) par c > 0 ne change aucune décision. A_moy est redéfini sur les **directions** w/‖w‖ (biais recalculés par calibration) ; contrôle négatif étendu : neuf copies de M0 à échelles différentes doivent rendre des décisions identiques sur le même Xcal (comparaison au bit sur les décisions, pas sur V, comme E le demande).

**B-(b) : à δ = 1,6, V(A) ≈ 3,6 α (RAPPORTÉ) ; tous les moniteurs linéaires seuls peuvent être au plancher.** **Transformée en condition de jugeabilité** : la liste n'est lue à un δ que si V(A) ≥ 5α à ce δ (illustratif ; seuil à geler) ; sinon « non jugeable à ce δ ». Option pour Lazar : δ = 1,2 (VÉRIFIÉ pièce 5 : V(A) = 0,161, erreur-type 0,016) comme second budget de cette seule expérience.

**B-(c)3 : aucun bras à V analytique.** **Transformée.** V exige une meilleure réponse, donc n'est jamais analytique ; mais le **taux de détection** d'une gaussienne connue par un moniteur linéaire l'est : Φ̄((t − w·μ)/(‖w‖σ)) composante par composante. Ce contrôle de l'estimateur `taux_defense` à 10⁻³ près (illustratif) est ajouté ; il contrôle l'instrument, pas la borne haute qu'est V (déclaré).

### 3. Le Duel 3 : nom, construction, comparabilité

**E : v_G − min_j U(p̄, j) n'est pas NashConv mais un déficit de sécurité du défenseur dans G.** **Acceptée**, renommé « déficit de sécurité restreint ».

**C3 : les colonnes de la matrice de A ne contiennent aucune meilleure réponse à A̅ ; le déficit restreint de A̅ est petit par construction.** **Acceptée.** Le déficit restreint sort de la métrique principale ; A̅ est évalué comme tout bras : défense figée, meilleure réponse standard puis renforcée, V (VÉRIFIÉ : `phase_finale` accepte toute défense mixte, c'est ce que fait C1 sur B).

**B-A1, D, E : comparer T = 8 et T = 16 compare des jeux différents ; une décroissance du déficit peut venir de l'enrichissement de la matrice ; les conditions de Brown–Robinson ne sont pas réunies.** **Acceptées.** Le contraste devient V(A̅_T) − V(A_T) à T = 8 et T = 16, avec le même instrument V ; « valeur restreinte − V » reste descriptif. H_A n'est plus « Robinson transposé » mais une hypothèse empirique nue, écrite au § (b).

**B-(b), C-(b)3 : rang effectif de la matrice de A non rapporté ; biais d'optimiseur.** **Acceptées** : rang effectif de la matrice des déplacements et de G_A rapportés ; A̅ entre dans l'audit d'attaquant indépendant (S17) ; V reste une borne haute, écrit à chaque lecture.

**D : A2 (attaquant à mémoire) confond apprentissage et déploiement.** **Transformée en plan factoriel** déploiement {dernier moniteur, mélange uniforme des moniteurs passés} × cible de l'attaquant {défense déployée… } — voir E3. VÉRIFIÉ : `objectif_lisse` prend déjà une défense mixte en argument, donc l'attaquant « historique » et le défenseur « mélange déployé » ne changent que la liste passée.

### 4. Mon présupposé A2 (équilibre mélangé → le dernier itéré pur revisite)

**D et E : la déduction exige un jeu figé, des réponses exactes et une classe inchangée ; elle n'implique ni périodicité ni retours angulaires ; les poids non purs de B sont ceux du jeu restreint final de B et ne disent rien des équilibres accessibles à A ; un petit poids maximal minimal prouve l'existence d'un optimum mélangé, pas sa nécessité.** **Acceptées.** A2 est rétrogradé à HYPOTHÈSE conditionnelle et rendu testable sur la **matrice de A elle-même** : sur G_A par tâche, v(G) = max_p min_j (pᵀG)_j et d(G) = max_i min_j G_ij ; avec ‖Ĝ − G‖_∞ ≤ η, l'erreur sur v − d est au plus 2η (E, VÉRIFIÉ par substitution). VÉRIFIÉ : n_eval = 19 998, donc η ≤ √(0,25/19 998) ≈ 0,0035 pour l'erreur binomiale seule. Si v − d ≤ 2η dans la majorité des tâches, le jeu restreint de A admet une ligne pure optimale et mon explication du revisitage est réfutée sans aucun calcul lourd. Contrôles de matrices (D-c4, E) : selle pure, équilibre intérieur, lignes optimales dupliquées (v − d doit y valoir 0 bien que le mélange soit « disponible »), ligne dominante.

### 5. Le Duel 5

**B-(b), C-(c)3, D : à deux unités, D₂ et B′₂ peuvent être au plancher ; changer les unités change le jeu ; retomber à la classe linéaire ramène à Q1.** **Acceptées** : conditions de jugeabilité ajoutées, V(D₂) ≥ V(A) + m et V(B′₂) ≥ V(B) + m ; critère de posabilité remplacé par v(G) − d(G) > 2η (plutôt que la part pure, qui ne distingue pas mélange disponible et nécessaire, E). Le changement de jeu est assumé : l'expérience ne dit que « existe-t-il une classe où le mélange est nécessaire dans le jeu restreint ».

### 6. I1 et le Duel 4

**D : I1 perd sa puissance si les oscillations se compensent entre fenêtres ; un seuil de décision inférieur au taux de convergence disponible ne réfute pas une convergence asymptotique.** **Acceptées** : I1 reste descriptif, lu avec A0 en regard ; dans le jouet, l'hypothèse porte sur l'exploitabilité de la **moyenne empirique** à horizon fini fixé d'avance (illustratif : 1 000 coups), comparée à celle de la meilleure réponse pure et du jeu fictif bilatéral sur le même jeu exact, pas sur une limite.

**Rejetée, une seule :** l'idée implicite de C-(b)2 que la discrétisation de I3 rend la permutation **inapplicable** ; elle rend seulement la loi de permutation discrète, ce que le rapport du quantile atteint et du nombre d'ordres distincts rend lisible.

---

## (b) Expériences corrigées

Tous les bras nouveaux sont **linéaires** et légers ; racines neuves à geler dans la plage 20264001–20264999 (VÉRIFIÉ, `exiger_racine_permise`), gel nouveau, pilote avant décision. Seuils m = 0,02 repris de S6 (RAPPORTÉ, « par principe ») et **illustratifs**. V est partout une borne haute (déclaré) ; S17 s'applique aux bras lus.

### E1 — Liste gelée de défenses linéaires seules (ex-Duel 1)

- **Liste** : A0 (M0 gelé), A_moy (moyenne des directions des 9 moniteurs de A, calibrée), A_pire (entraîné sur la pire attaque passée de A), A_q^A, A_unif(B), A_q^B ; les deux dernières paires forment le 2 × 2 {attaques A/B} × {uniforme / q}.
- **H_A** : aucun membre ne bat A de m à un δ jugeable ; **H_B** : au moins un le bat (union protégée, Bonferroni sur la liste, bornes par rééchantillonnage apparié).
- **Jugeabilité** : V(A) ≥ 5α au δ (illustratif) ; sinon « non jugeable à ce δ ».
- **Contrôles** : négatif — A_moy et A̅ sur neuf copies de M0 à échelles différentes rendent des décisions identiques à M0 sur le même Xcal (au bit) ; positif — D − A (RAPPORTÉ +0,36 / +0,32) ; instrument — `taux_defense` contre la formule analytique sur une gaussienne connue.
- **Issues** : H_B réfutée → à classe linéaire, ni la moyenne de directions, ni le pire cas, ni la pondération q, ni l'historique de B ne changent le dernier itéré seul (mécanismes (c), (f) en leur instance listée) ; H_A réfutée → la cellule gagnante nomme le facteur (pondération ou historique d'attaques).

### E2 — Dépendance temporelle des attaques (ex-Duel 2)

- **Statistique par tâche** : rang de I3 observé dans la loi exacte des 8! permutations des déplacements, bilatéral ; égalités comptées.
- **H_A** : le rang de A diffère de celui de A0 (apparié, bornes B2, lu sur la médiane des rangs) ; **H_B** : A et A0 ont la même loi de rang (différence dans ]−0,1 ; +0,1[, illustratif).
- **Témoins** : A0 (géométrie de l'attaquant seule) ; D (continuité attendue, queue basse) ; A0 sans départ vers l'origine (ablation possible car sans entraînement).
- **Banc d'instruments** (trajectoires fabriquées, graines gelées) : périodique, convergente, i.i.d. unimodale, i.i.d. multimodale, atomique avec égalités, Markov alternante sans période, marche à départ chaud ; I3 − 0,7345 et rang de permutation sur chacune. Critère : la nulle gaussienne doit rejeter ≤ 0,05 sur les i.i.d. (prédiction désormais : elle le fera, E) et la permutation doit rejeter la Markov alternante (ce qui montre qu'un rejet n'est pas un « cycle »).
- **Issues** : H_A réfutée → les retours de A sont ceux de l'attaquant contre un moniteur immobile ; la Table 5 ne lit plus rien de la dynamique ; H_B réfutée → dépendance temporelle propre au ré-entraînement, nommée « retours non échangeables », jamais « cycle » sans la périodicité mesurée à part.

### E3 — Factoriel déploiement × mémoire de l'attaquant (fusion des Duels 1 et 3)

- **Cellules** (linéaires, T = 8 puis T = 16 sur A seul) : A (dernier moniteur, attaquant contre la défense déployée) ; A2 (dernier moniteur déployé, attaquant répondant au mélange uniforme des moniteurs passés) ; JF2 (mélange uniforme déployé et entraînement contre l'historique uniforme : jeu fictif des deux côtés, l'attaquant répondant à la défense déployée) ; A̅ (mélange uniforme calculé après coup sur la trajectoire de A).
- **Métrique** : V contre meilleure réponse fraîche (standard et renforcée), apparié ; diagnostics : « valeur restreinte − V », v(G_A) − d(G_A) avec 2η, `poids_max_min_equilibres` sur G_A (VÉRIFIÉ), rang effectif.
- **H_A** : V(JF2) − V(A) ≥ m et V(A̅) − V(A) ≥ m aux δ jugeables, et l'écart ne baisse pas de T = 8 à T = 16 ; **H_B** : l'un des deux écarts est < m.
- **Contrôles** : négatif — JF2 et A̅ sur copies de M0 = M0 ; positif — C1 sur B (RAPPORTÉ ≈ +0,11 contre A) ; matrices témoins (selle pure, intérieure, lignes dupliquées, ligne dominante) pour v − d et pour le programme de non-unicité.
- **Issues** : H_A tient → « la défense pure ne converge pas, son mélange uniforme la bat » ; le double oracle n'ajoute que le choix des poids (RAPPORTÉ : B − C1 ≈ +0,02) et la distribution d'entraînement ; H_A réfutée → le mélange des moniteurs de A n'aide pas ; si de plus v − d ≤ 2η sur G_A, l'explication par l'équilibre mélangé tombe ; si A2 ≠ A, la mémoire de l'attaquant compte et le « cycle » tient en partie à sa myopie.

### E4 — Jouet (ex-Duel 4), inchangé sauf l'hypothèse

Pierre–feuille–ciseaux, pile ou face apparié, jeu de Shapley ; dynamiques : meilleure réponse pure, jeu fictif bilatéral, règle de A ; horizon fixé d'avance ; Gambit en vérité. **H_A** : l'exploitabilité de la moyenne de la règle de A est < 0,01 (illustratif) à l'horizon fixé dans les deux jeux à somme nulle ; **H_B** : non. Disponibilité de Shapley et de l'exploitabilité pour matrices définies à la main dans OpenSpiel : à vérifier dans la documentation.

### E5 — Rendre Q2 posable (ex-Duel 5)

Classe réduite (illustratif : 2 ou 3 unités, K = 3 ou 5), D ré-entraîné à la même classe. **Posable** si v(G) − d(G) > 2η sur plus de la moitié des tâches **et** V(D_u) ≥ V(A) + m **et** V(B′_u) ≥ V(B) + m ; sinon « non jugeable » ou « retour à Q1 ». Puis Table 6 telle qu'écrite.

**Coût** (illustratif, d'après VÉRIFIÉ pièce 5 : 768 s de processeur pour 432 tâches « A seul, léger », soit 1,8 s par tâche) : E1 à E3 ≈ 2 à 6 s par bras et par tâche, de l'ordre de 2 h de processeur pour 100 instances × 2 δ ; E2 sans calcul neuf hors A0 ; E5 de l'ordre du pilote v4 (RAPPORTÉ ≈ 49 min pour 48 tâches). Le délai de 9 000 s déjà fragile (RAPPORTÉ, CM4-01) impose des runs séparés.

---

## (c) Réponse à l'arbitre

**Ce qui est établi, sur les pièces.**
- VÉRIFIÉ : la règle de A n'est pas le jeu fictif de Brown–Robinson : la cible non modifiée pèse 1/(t+1) dans son historique ; les deux oracles sont approchés et locaux ; l'attaquant répond au dernier moniteur avec départ chaud et départ fixe. Le jeu codé est à somme nulle en extension mixte (`resoudre_jeu`, détection d'un mélange = moyenne pondérée, fausses alertes du mélange à α).
- VÉRIFIÉ (correction d'E) : une loi i.i.d. de déplacements, quel qu'en soit le nombre de modes, donne I3 = (t−2)/(t−1) en espérance ; l'excès de A (RAPPORTÉ : +0,17 et +0,21) mesure une dépendance temporelle réelle, pas un artefact de modes. La nulle est en revanche violée vers le bas par le départ chaud (RAPPORTÉ : D et B′).
- RAPPORTÉ : Q1 réfutée (C3 et D battent B) ; B′ pur et forcé par le jeu restreint ; A à I1 ≈ 0.

**Ce qui n'est pas établi.**
- Que la dépendance temporelle de A soit un **cycle** : aucune périodicité n'est mesurée, huit tours ne le permettent pas, et aucun témoin au moniteur gelé (A0) ne dit quelle part des retours vient de l'attaquant seul.
- Que I1 ≈ 0 soit une **non-convergence** : sans A0, un plafond de la classe linéaire pure est indiscernable d'une dynamique qui n'apprend pas.
- Que l'équilibre du jeu restreint **de A** soit mélangé : les poids non purs de B portent sur la matrice de B ; v(G_A) − d(G_A) n'a jamais été calculé, alors que ses ingrédients existent.
- Que la **moyenne** des moniteurs de A fasse mieux que le dernier : C1 mélange les moniteurs de B.
- Quelle métrique de convergence est lisible sur des sondes réelles : seul V d'une défense figée à fausses alertes α sur des attaques tenues à l'écart l'est sans attaquant exact, et il y reste une borne haute ; I3 exige des déplacements d'activations et une nulle par permutation, I1 un témoin gelé.
- Tout ce qui concerne Bailey et collègues et les mécanismes (a)–(f) sur modèles de langage : rien dans les pièces ; références à vérifier.

**L'expérience à faire en premier : un run léger « A, A0, A̅ » sur racines neuves gelées**, aux deux δ (et 1,2 en option), avec G_A, v − d, le programme de non-unicité sur G_A, et le rang de permutation de I3 pour A et A0. Elle conditionne tout le reste : si V(A0) ≈ V(A) et si les rangs de permutation de A et A0 se confondent, « non-convergence » et « cycle » se réduisent à un plafond de classe plus la géométrie de l'attaquant, et les mécanismes (a)–(d), (f) n'ont rien à guérir à classe linéaire ; si A̅ bat A de m, la question se reformule « la défense pure ne converge pas, son mélange uniforme oui », et le double oracle n'est jugé que sur ce qu'il ajoute à l'uniforme ; si v(G_A) − d(G_A) ≤ 2η, l'explication par l'équilibre mélangé est écartée avant d'avoir coûté un bras. Chacune de ces trois issues réfute une lecture écrite ; aucune ne requiert d'attaque nouvelle ni de modèle réel.

**Compte de ce qui peut être réfuté** : cinq expériences à deux issues écrites ; deux présupposés déjà réfutés par la critique (A4 première moitié, A2 en sa forme forte) et remplacés par des tests.

FIN-DE-CELLULE