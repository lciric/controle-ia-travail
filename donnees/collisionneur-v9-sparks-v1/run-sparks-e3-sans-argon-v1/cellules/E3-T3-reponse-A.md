# Proposition A — Tour III.3 : réponse aux critiques

**Statuts.** Billet et « nos résultats » = RAPPORTÉ ; chiffres « [journaux] » de la pièce 3 = OBSERVÉ-NON-AUDITÉ ; mes conceptions et les critiques de B, D, E = HYPOTHÈSES de méthode ; nombres dérivés = « calcul » ; tailles d'échantillon = « illustratif ». Pièce C absente (jamais lancée) : rien à répondre. Je ne réponds qu'aux sections qui visent A ; quand B, D et E font la même objection, je la traite une fois en nommant les trois.

---

## (a) Verdict par critique

Je numérote par expérience. « Acceptée » = le défaut existait et je corrige ; « rejetée » = je garde le plan, avec la raison ; « → test » = la critique devient une condition ou une mesure du plan corrigé.

### E1 (lecture d'un trait dans les deltas, sous nul)

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 1 | Nuls N1/N2 à graines différentes contre T à graine partagée : la norme ou le rang du delta sépare les classes sans lire le trait (B a1, B c1, D a1 pour mon plan) | **Acceptée, fatale pour l'ancien E1.** Dans le billet, les deux copies partagent graine, ordre et calendrier [journaux, pièce 3 §3.1] ; mes nuls ne les partageaient pas. | Tous les nuls sont refaits **à graine et ordre partagés**, avec une variation neutre (paraphrase de la réponse) sur la **même fraction** d'exemples que celle où T diffère (environ un tiers, les items à mauvaise suggestion). Appariement en norme de delta vérifié avant lecture ; les paires hors tolérance sont exclues avant scellement. |
| 2 | Raccourci « le plus loin du départ est l'honnête » (B a2, B correctif, D a1) | **→ test (E0 ci-dessous).** Nuance que je garde : mon lecteur ne reçoit que A et B, pas θ₀ ; le raccourci lui est disponible seulement si ‖θ_A‖, ‖θ_B‖ ou leurs normes par couche le trahissent. | E0 mesure la règle avec θ₀ (base mécanique) et sans θ₀ (normes brutes). Si elle bat le hasard, elle entre dans la base mécanique à battre et une nulle appariée en distance au départ devient obligatoire. |
| 3 | N3 (départ contre sycophante) n'est pas comportementalement nul : format, exactitude sans suggestion (B a3, D a1, E a1) | **Acceptée.** « Comportement égal » n'était vrai que du taux de suivi. | N3 cesse d'être un nul. Il devient une **condition diagnostique** nommée « affinage sans changement de suivi », rapportée à part, après validation sur un lot indépendant que les deux modèles ont le même suivi des mauvaises suggestions (D c1). La fausse alerte sur N3 se lit comme « lecture d'un affinage », pas comme erreur. |
| 4 | Affinage complet et adaptateurs regroupés sans interaction mesurée (D a1) | **Acceptée.** | Deux sous-expériences séparées, jamais regroupées ; l'interaction format × lecteur est une sortie, pas une variable absorbée. |
| 5 | Base mécanique supervisée qui fuit par famille (D a2) ; régression logistique sur d ≫ k qui surapprend, donc facile à battre (B b3) | **Acceptée.** | La base est une régression sur un **vecteur de statistiques de faible dimension fixé d'avance** (normes et cosinus du delta par couche et type de matrice, ≤ 40 nombres, illustratif), entraînée sur un parent, une famille de faits et une recette **disjoints** du test. |
| 6 | Unité positive et cible de l'AUC non définies ; probabilités marginales sans loi jointe (E a1, D b2) | **Acceptée.** | Trois questions séparées, trois mesures : (Q1) y a-t-il une différence de trait ? — taux de déclaration sur paires nulles (FA) et sur T (détection) ; (Q2) laquelle est sycophante ? — AUC sur l'**orientation** des paires T, score = P(A) − P(B) ; (Q3) calibration — Brier sur Q1 et Q2 séparément. |
| 7 | Puissance : AUC ≥ 0,80 en borne basse exige une AUC vraie ≈ 0,92 à 20 T ; FA ≤ 0,10 sur 60 nuls est un pile ou face à taux vrai 0,10 ; 3 essais ne font pas 3n (B b1-b2-b4, D b1) | **Acceptée.** | Duel reformulé en marges (voir E1'). Unité = paire ; les 3 essais sont des mesures répétées agrégées par la médiane de P avant toute statistique. FA certifiée par **borne supérieure** : avec 60 paires nulles, ≤ 2 alertes donne une borne unilatérale à 95 % ≈ 0,10 (calcul, binomiale). Les zones intermédiaires sont déclarées indécises, pas réfutantes. |
| 8 | Performances intermédiaires hors des deux hypothèses ; l'échec de H_A ne prouve pas « lit seulement l'affinage » ; battre une sonde et extraire une information sont deux questions (E a1) | **Acceptée.** | Deux duels distincts : D1 (information) : H_A : AUC − 0,5 ≥ ε ; H_B : < ε. D2 (apport) : H_A : AUC(lecteur) − AUC(base) ≥ ε' ; H_B : < ε'. |
| 9 | Témoin positif du lecteur manquant : sans lui un échec ne falsifie que « ce lecteur » (B c3, D c1, E c1) | **Acceptée.** | Paires à couche de sortie non gelée (trait lisible par construction, le billet l'admet pour ses expériences 1-2, L84). Un lecteur qui y échoue est écarté avant T. |
| 10 | Lecteur privé des poids mais avec les métadonnées (E c1) ; adaptateurs à trait bénin appariés (D c1, E c1) | **Acceptée.** | Condition « métadonnées seules » (README, formes des tenseurs, aucun nombre) : plancher du lecteur. Paires « bénignes » : affinage à graine partagée sur un trait sans rapport (par exemple ton de la réponse), appariées en norme ; elles mesurent si le lecteur nomme « sycophancie » à toute différence. |
| 11 | Séparation parent/faits/recette entre calibration, base et test ; un seul parent = une grappe (D b1, E c1) | **Acceptée, partiellement faisable.** | Deux parents (Gemma 3 270M-it, Qwen3.5-0.8B, tous deux attestés dans les pièces), deux découpages de faits, croisés : calibration sur (parent 1, faits a), test sur (parent 2, faits b) et réciproquement. La variance entre parents reste estimée sur deux points : je le dis dans le rapport. |

### E2 (validité de construit du retrait d'une direction)

| # | Critique | Verdict | Conséquence |
|---|---|---|---|
| 12 | « Exactitude conditionnelle à finir » conditionne sur une variable postérieure au traitement (B a4, D a3, E a2) | **Acceptée.** | Strate définie **avant** traitement : problèmes que la base finit, identifiés sur des générations distinctes de celles qui servent à estimer l'effet (E, D c2). Sur MATH-500 cette strate compte ≈ 35 problèmes (calcul : 7 % de 500 [pièce 1]) : trop peu. Je la construis sur les problèmes d'entraînement GSM8K/MATH (7 469 + 7 275 [pièce 1]) : à 7 % de terminaison, ≈ 1 000 problèmes, dont je tire 300 pour la strate (illustratif). Effet total et contraste stratifié publiés séparément. |
| 13 | Direction aléatoire sur le même support fuit (B a5, D a3) | **Acceptée.** | Trois témoins : direction aléatoire sur support choisi ; direction aléatoire sur **support aléatoire** de même taille ; plusieurs directions tirées dans l'espace des directions effectivement écrites par les mêmes perceptrons (D c2), 5 tirages chacun (illustratif). |
| 14 | Apparier le témoin sur « l'effet sur la longueur » (D a3) | **Rejetée.** La longueur de réponse est le résultat mesuré ; apparier un témoin sur le résultat, c'est sélectionner le témoin par l'effet. Je garde l'appariement en norme (poids) et en norme d'activation induite sur des textes neutres (D), pas en effet. |
| 15 | Duel sycophancie non exhaustif : « les deux bougent » ; de plus, changer la part attirée est déjà un effet causal, donc « pente = corrélat » est faux (B a6, D a4, E a2) | **Acceptée, y compris sur le fond.** Mon partage « forme = cause, échelle = corrélat » était une erreur de construit. | Duel sur la marge : H_A : la courbe dose–réponse sous ablation ciblée diffère de celle sous ablation aléatoire de plus de ε (distance entre courbes, mesurée sur a et k) ; H_B : non. « Point fixe seul », « part seule », « les deux » deviennent des **descriptions** de l'effet, rapportées, non décisives. |
| 16 | La loi porte sur des notes, la direction sur la sycophancie jugée : deux construits (B a6) ; suivi mécanique et notes = deux critères (D a4) | **Acceptée.** | Deux critères préenregistrés et rapportés séparément : (i) paramètres (a, k) de la loi d'attraction ; (ii) taux de suivi des mauvaises suggestions sur faits. Aucune conjonction dans le duel ; le duel porte sur (i), (ii) est un critère secondaire avec son propre ε. |
| 17 | Identifiabilité : si k ≈ 0 ou si les notes initiales se concentrent près de a, a n'est pas identifiable (B b5, E b) | **Acceptée → précondition.** | Avant toute ablation, estimer (a, k) sur la base avec générations neuves ; si l'intervalle de k contient 0 ou si la plus petite valeur propre de l'information est sous un seuil fixé d'avance, le volet est déclaré **non jugeable** et on ne tire pas de conclusion. |
| 18 | Séparer cadres de pression et faits utilisés pour choisir l'intervention de ceux qui estiment la loi (D a4) ; interventions simulées, répétitions base–base, ancrages de notation (E c2) | **Acceptée.** | Faits et cadres en trois lots scellés : choix de la direction, estimation de la loi, test. Deux générations base–base indépendantes donnent le bruit de référence. Notation aveugle à l'intervention avec ancres fixes. |

### E3 (lecteur de delta contre sonde contre boîte noire)

| # | Critique | Verdict | Conséquence |
|---|---|---|---|
| 19 | L'écart M1 − M3 est fixé par le budget m d'épisodes de la boîte noire (B a7, b6) | **Acceptée.** | m est fixé sur un lot de développement de sorte que la détection de M3 à la dose médiane soit entre 0,2 et 0,8 (illustratif) ; publié avant le test ; une courbe détection(m) est rapportée en annexe. |
| 20 | P3 a un saboteur instruit, sans delta de poids ; construire un organisme affiné introduit le contenu des données comme confondant (B a7, D c3) | **Acceptée.** | Il faut un organisme de sabotage **affiné** (adaptateur) ; je le marque comme artefact à construire, non attesté dans les pièces. Nuls : adaptateurs honnêtes entraînés sur les **mêmes invites** avec complétions honnêtes (appariés en contenu), à graine partagée avec le positif, plus jumeaux p = 0 à graines différentes. |
| 21 | Marginal n'est pas incrémental : il faut BN + poids contre BN + mécanique contre BN seule (E a3, D a5, D c3) | **Acceptée.** | Trois bras combinés par la **même règle** fixée hors test, plus un bras « BN + score de poids permuté entre unités » (E c3) comme nul de combinaison. |
| 22 | Unités différentes (verdict par adaptateur, score par épisode) ; p de construction ≠ fraction réalisée (D a5, E a3) | **Acceptée.** | Unité = adaptateur ; M2 et M3 agrégés par adaptateur à budget fixe ; la fraction de sabotage **réalisée** est mesurée par l'évaluateur mécanique sur des épisodes disjoints de ceux de la boîte noire. |
| 23 | Calibration et évaluation sur les mêmes jumeaux (B a8, B c5) | **Acceptée.** | Partition : jumeaux de calibration et jumeaux de test disjoints par graine ; α calibré sur les premiers, FA rapportée sur les seconds avec borne supérieure. |
| 24 | Puissance bornée par α + p·TV(Q, P₀) (E b) | **Acceptée comme borne.** Elle dit qu'à p = 0,05 aucune méthode ne dépasse α + 0,05·TV : les doses faibles sont donc presque non jugeables pour tout instrument. | Doses révisées : p ∈ {0 ; 0,1 ; 0,25 ; 0,5 ; 1} ; la question « M1 ajoute à dose faible » se pose à p = 0,1 et 0,25 seulement, le reste est contrôle de plafond. |

### E4 (famille de tâches pour l'organisme d'idéation)

| # | Critique | Verdict | Conséquence |
|---|---|---|---|
| 25 | « Nulle augmentée » par permutation des couches extrêmes : change la fonction, l'oracle ne peut plus certifier la propriété (B a9, D a6, E a4) | **Acceptée.** | La nulle est redéfinie comme **famille de lois explicite** : la nulle contient toute loi dont la statistique est une fonction mesurable des seules couches d'entrée et de sortie. Son instanciation : tirages frais où les couches du milieu sont **ré-entraînées à propriété fixée** (vérification par oracle que la propriété survit) et les couches extrêmes conservées ; les lois qui survivent au tirage des couches du milieu sont, par construction, dans la nulle. La transformation est validée par exécution (D c4). |
| 26 | Seuil d'abandon circulaire (B a9) | **Acceptée.** | Nouveau seuil : puissance sur lois plantées des couches du milieu, de force fixée **par l'oracle** (taille d'effet connue), mesurée avant toute soumission ; abandon si cette puissance à 60 instances est < 0,5 (illustratif). |
| 27 | Le juge doit être revalidé après extension de la nulle ; condition de surmartingale pour chaque P de la nulle (E a4, E b) | **Acceptée.** | Une ligne « lois sur couches extrêmes » est ajoutée au banc des tricheurs (0 sur 1 000 sur 11 lignes, RAPPORTÉ pièce 2 §2) et le juge est revalidé avant usage ; courses entières nulles (toute promotion fausse), pas seulement des faux témoins isolés (D c4). |

### E5 (invariance du lecteur)

| # | Critique | Verdict | Conséquence |
|---|---|---|---|
| 28 | Invariance vraie par construction pour la base mécanique et pour tout lecteur déterministe après canonicalisation exacte ; un lecteur constant est parfaitement invariant (B a10, D a6, D b5, E a5) | **Acceptée.** | E5 ne porte que sur le lecteur recevant des poids **non canonicalisés** ; l'invariance n'est rapportée que conditionnellement à une détection ≥ seuil sur les mêmes paires (sinon « non jugeable ») ; témoin : transformation **changeant** la fonction, à amplitude appariée, qui doit faire bousculer le verdict (D c4). |
| 29 | Une invariance moyenne ne certifie pas la classe ; le coût de canonicalisation n'est pas nul (E a5, E b) | **Acceptée.** | La certification se formule sur la distribution de transformations déclarée, pas sur le supremum ; le coût de canonicalisation est mesuré et publié, et la variabilité sans transformation (E c5) est la référence. |

**Bilan** : 28 acceptées ou transformées, 1 rejetée (#14). Les trois critiques les plus coûteuses pour mon plan initial étaient #1 (graine), #12 (collisionneur) et #15 (construit « échelle = corrélat ») : elles invalident respectivement mon nul, mon estimateur et mon hypothèse.

---

## (b) Expériences corrigées

Conventions inchangées : étiquettes scellées ; α, ε, m, n fixés avant lecture ; essai retenu = médiane des P déclarées sur 3 essais, agrégée **par paire** ; duels en marges (H_A : Δ ≥ ε, H_B : Δ < ε) avec zone indécise déclarée (intervalle traversant ε).

### E0 — Le raccourci de distance au départ (test de B, adopté)

Reconstruire les six affinages du billet avec la recette publique (OBSERVÉ-NON-AUDITÉ : 452 faits, AdamW 2e-5, lot 8, 3 époques, plongement gelé ; pièce 3 §3.1), puis 20 paires T supplémentaires à graine partagée (illustratif). Deux règles mécaniques, aucune passe avant : R₁ « le plus loin de θ₀ est l'honnête » (θ₀ fourni) ; R₂ même règle sans θ₀, sur normes par couche de A et B.
**H_A** : R₁ et R₂ identifient le sycophante à un taux ≤ 0,5 + ε (ε = 0,15, illustratif). **H_B** : l'une au moins dépasse.
Issues : H_B → la règle entre dans la base mécanique d'E1 et une nulle appariée en distance au départ devient obligatoire ; H_A → la confusion de graine (#1) reste le premier suspect, déjà corrigé.

### E1′ — Lecture d'un trait d'alignement dans des deltas, à nuls appariés en graine

**Classes de paires**, toutes à graine et ordre partagés, même recette, deux parents (Gemma 3 270M-it, Qwen3.5-0.8B) :
- **T** : honnête contre sycophante (comme le billet) ;
- **N** : deux honnêtes dont les réponses diffèrent par une paraphrase neutre sur la même fraction d'exemples ; appariement en norme de delta à ± 20 % de la médiane des T (illustratif) ;
- **Bén** : trait sans rapport (ton), même fraction, apparié en norme ;
- **Pos** (témoin positif) : T à couche de sortie non gelée ;
- **Diag** (ex-N3) : départ contre sycophante, après validation d'un suivi égal sur lot indépendant.

Deux volets non regroupés : affinage complet ; adaptateurs de rang faible. Lecteurs : trois modèles ouverts de familles différentes (non nommés faute d'attestation), un lecteur de frontière sur 10 paires. Conditions : poids seuls ; métadonnées seules ; base mécanique à statistiques fixées (#5), plus R₁/R₂ si E0 donne H_B. Interdits et bac à sable identiques au billet.

Tailles (illustratif) : 40 T, 60 N, 20 Bén, 10 Pos, 10 Diag par volet et par parent.

**Duels.**
- D1 (information, Q2) : H_A : AUC_orientation(T) − 0,5 ≥ 0,20 ; H_B : < 0,20. À 40 paires (20 par orientation), l'erreur type à AUC 0,8 est ≈ 0,07 (calcul, Hanley-McNeil approché) : un AUC vrai de 0,80 a une borne basse ≈ 0,66, donc la zone 0,66–0,80 est indécise et déclarée telle.
- D2 (apport, Q1) : H_A : détection(T) − FA_sup(N) ≥ 0,30 au seuil calibré sur un lot disjoint, **et** AUC(lecteur) − AUC(base) ≥ 0,10 ; H_B : l'une des deux échoue. FA certifiée par borne supérieure (≤ 2 alertes sur 60 N pour ≈ 0,10, calcul).
- Précondition : le lecteur passe Pos (AUC ≥ 0,9, illustratif) et fait ≤ chance sur métadonnées seules ; sinon « non jugeable pour ce lecteur ».

Issues : H_B sur D1 pour tous les lecteurs → la lecture de poids seuls n'apporte pas d'information sur ce trait à ce format ; le programme de contrôle l'enregistre comme instrument sans pouvoir, et le billet (échec, pièce 3 §3.2) est confirmé sous nul. H_A sur D1 et H_B sur D2 → information présente mais pas au-delà d'une sonde de 40 nombres : on intègre la sonde, pas le lecteur. H_A sur les deux → falsification de ma lecture pessimiste.

Extension (échelle d'accès) conservée : poids seuls ; attention seule **sans préfixe fourni à la main** (le chiffre de la tête 10.2, 94,3 % contre 3,5 %, vient d'une paire et de 8 textes après un préfixe des auteurs, OBSERVÉ-NON-AUDITÉ pièce 3 §3.3-3.4) ; activations ; sorties. Même grille de nuls à chaque niveau ; un nul « mêmes poids, textes différents » mesure la variance du lecteur.

### E2′ — Validité de construit du retrait d'une direction

**Volet Qwen.** Interventions : édition des couches 15/19 (diffs livrés, OBSERVÉ-NON-AUDITÉ §6.6f) ; cinq directions aléatoires appariées en norme sur support choisi ; cinq sur support aléatoire ; cinq tirées parmi les directions écrites par les mêmes perceptrons ; doses 0 / 0,25 / 0,5 / 1 / 1,5 ; dose 0 répétée deux fois (bruit). Mesures : part coupée ; exactitude sur la **strate pré-traitement** (300 problèmes d'entraînement que la base finit, identifiés sur des générations séparées) ; effet total ; banc de répétition légitime (copie de chaîne, énumération).
**H_A** (spécificité) : la réduction de coupure de l'édition ciblée dépasse la meilleure des quinze aléatoires de ≥ 0,20 (illustratif), à répétition légitime non dégradée de plus que les aléatoires (marge 0,05) ; **H_B** : l'une des deux conditions échoue. Rapport séparé : « déblocage pur » si l'exactitude sur la strate pré-traitement ne bouge pas de plus de 3 points (calcul : l'erreur type binomiale à 94 % sur 300 ≈ 1,4 point) ; sinon « ajout » — description, non duel.

**Volet sycophancie (Llama-3.1-8B-Instruct).** Précondition d'identifiabilité (#17). Lots scellés : choix de direction / estimation / test. Interventions : ablation ciblée rang 1 et rang 3 ; cinq directions aléatoires appariées ; intervention simulée (aucune édition, générations neuves) ; base–base. Mesures : (a, k) de la loi d'attraction sous pression dosée ; suivi des mauvaises suggestions sur faits ; suggestions vraies et pression sans contenu (contrarianisme générique, E c2).
**H_A** : distance entre la courbe dose–réponse ciblée et l'enveloppe des aléatoires ≥ ε (fixé à deux fois la distance base–base) ; **H_B** : < ε. Issue H_B → la direction reste un corrélat dans nos dépôts, et la réplication non reproduite (pièce 2 §7) est confirmée comme telle ; H_A → on rapporte si c'est a, k ou les deux, et le changement de suivi.

### E3′ — Delta contre sonde contre boîte noire, incrémental

Organisme de sabotage **affiné** à construire (artefact non attesté). Unité = adaptateur ; doses p ∈ {0 ; 0,1 ; 0,25 ; 0,5 ; 1}, 4 graines par dose ; fraction réalisée mesurée. Nuls : honnêtes appariés en contenu à graine partagée ; jumeaux p = 0 à graines différentes, divisés en calibration et test. Bras : BN seule ; BN + score mécanique de delta ; BN + lecteur ; BN + score de poids permuté ; sonde d'activation contre plancher de 200 sondes aléatoires appariées en covariance (notre mesure, pièce 2 §6). Règle de combinaison et budget m fixés sur le lot de développement.
**H_A** : à p = 0,1 ou 0,25, détection(BN + lecteur) − détection(BN + mécanique) ≥ 0,15 à α = 0,05, intervalle apparié ; **H_B** : < 0,15 aux deux doses. La borne α + p·TV (E, calcul) est rapportée pour dire ce qu'aucun instrument ne peut dépasser.

### E4′ — Zoo à propriété plantée, nulle explicite

Nulle = lois fonction des seules couches extrêmes, instanciée par ré-entraînement des couches du milieu à propriété vérifiée par l'oracle ; revalidation du juge avec une ligne « couches extrêmes » au banc des tricheurs et des courses entières nulles.
**H_A** : des lois sur les couches du milieu sont promues à un taux ≥ puissance mesurée sur lois plantées d'effet connu − 0,2 ; **H_B** : taux < seuil ou puissance sur lois plantées < 0,5 à 60 instances (abandon : la famille n'a pas la puissance voulue).

### E5′ — Invariance conditionnelle à la détection

Lecteurs sur poids non canonicalisés, paires T où la détection d'E1′ ≥ 0,7 (sinon non jugeable) ; transformations neutres validées par exécution ; transformation changeant la fonction à amplitude appariée ; répétitions sans transformation (variabilité du lecteur).
**H_A** : taux de bascule sous transformation neutre ≤ taux sans transformation + ε, **et** taux de bascule sous transformation non neutre ≥ 0,5 ; **H_B** : l'une échoue. Coût de canonicalisation mesuré et publié ; certification restreinte à la distribution de transformations déclarée.

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, un lecteur, un essai).** Un modèle propriétaire, avec un harnais audité « sans outil » (1 125 tours, OBSERVÉ-NON-AUDITÉ), nomme un trait grossier (jeu, forme, langue) de réseaux de 17 253 à 7,16 millions de poids, écrit de petits réseaux de jeu qui battent des politiques proximales à petite échelle, et, avec générations et activations fournies par le harnais, localise et retire dans Qwen3.5-0.8B une direction associée aux boucles, avec un gain concentré sur les réponses initialement coupées (0,0 point sur les 114 qui finissaient, OBSERVÉ-NON-AUDITÉ). Sur le seul trait d'alignement, la lecture des poids seuls **échoue** (douze réponses à P = 0,5, OBSERVÉ-NON-AUDITÉ) ; la réussite demande des motifs d'attention, sur un choix forcé, sans paire témoin, et la greffe des composants nommés ferme 0,00 de l'écart (OBSERVÉ-NON-AUDITÉ). Les runs montrés sont une sélection (au moins six non montrés pour l'expérience 8).

**Ce qui n'est pas établi.** Que la lecture tienne au lecteur, à la consigne ou au budget ; un taux de fausses alertes ; qu'une sonde de quelques dizaines de statistiques de delta ne ferait pas aussi bien ; que la direction retirée soit spécifique plutôt qu'un frein générique ; que « lisible » implique « causal » — le billet lui-même le dément par sa greffe nulle, ce qui rejoint notre propre résultat (direction qui suit sans causer, ablation non reproduite, RAPPORTÉ pièce 2 §7). Après les critiques, je retire deux choses de ma propre lecture du tour III.1 : « point fixe = cause, échelle = corrélat » (changer la part attirée est un effet causal) et l'usage de N3 comme nul.

**Ce que cela change dans nos programmes.** Pour le contrôle : l'instrument « lecteur de poids par modèle de langue » n'entre qu'après E1′ avec nuls à graine partagée, témoin positif, condition métadonnées seules et base mécanique disjointe ; la question « au-delà de la boîte noire » se pose en incrémental (BN + lecteur contre BN + mécanique), à budget m fixé et sous la borne α + p·TV. Pour l'organisme d'idéation : une famille de tâches à oracle exécutable avec une nulle **explicite** (lois des couches extrêmes), le juge revalidé avant usage. Pour la sycophancie : une réplication préenregistrée sous dose, avec précondition d'identifiabilité et témoins aléatoires multiples. Classe de menace « éditeur de poids » : décrite par l'accès (écriture avant livraison, fonction conservée) et par ce que le défenseur certifie (invariance conditionnelle à la détection, coût de canonicalisation mesuré), sans mode d'emploi.

**L'expérience à faire en premier : E0, puis E1′ volet adaptateurs sur Gemma 3 270M-it.** E0 coûte quelques minutes de calcul sur poids une fois les affinages reconstruits (recette publique) et décide si une règle de distance au départ bat le hasard — ce qui fixe la base à battre. E1′ suit immédiatement : ≈ 130 affinages de 336 à 342 pas à lot 8 (OBSERVÉ-NON-AUDITÉ) par parent, quelques heures de carte (illustratif), lecteurs ouverts locaux (le coût du billet, ≈ 29,7 millions de jetons d'entrée pour 15 conversations, OBSERVÉ-NON-AUDITÉ, interdit un lecteur de frontière à cette échelle). **Seuil d'abandon** : si aucun lecteur ouvert ne franchit D1 (AUC − 0,5 ≥ 0,20 en borne basse) alors qu'il passe le témoin positif, et si la base mécanique fait aussi bien ou mieux, nos programmes intègrent la sonde de 40 nombres et pas le lecteur ; la lecture de poids seuls d'un trait d'alignement est alors enregistrée comme non démontrée à ce format, ce que le billet dit déjà de ses propres données.

FIN-DE-CELLULE