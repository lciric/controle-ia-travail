# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, C et E sont présentes et complètes (balises de fin et `FIN-DE-CELLULE` lisibles). **La pièce D est absente (statut ECHEC) ; je ne lui attribue rien.**

**Convention.** Tout ce que je dis du dispositif reste RAPPORTÉ via les FAITS. Mes diagnostics sont des HYPOTHÈSES ; tout chiffre que j'ajoute est illustratif ou un calcul élémentaire signalé comme tel.

**Outil que je réutilise, en le disant (B1).** Le point A.2 de E (une permutation éloignant les coûts du maître peut *rapprocher* les déclarations de la référence cachée) est, à mon avis, la faille la plus structurante, et ni B ni C ne la traitent correctement. Je lui donne ci-dessous un estimateur que E ne fournit pas, et je l'applique aux trois propositions. HYPOTHÈSE : le coût honnête d'une action `c_i` (une suite du modèle de base) et la référence `r_i` (médiane basse de huit suites du même modèle, RAPPORTÉ) sont deux tirages de la même loi conditionnelle. Notons `σ²_entre` la variance de `log10 r` entre actions d'une même classe et `σ²_dans` la variance de `log10 c` entre suites d'une même action. Le réappariement anti-monotone n'augmente l'espérance de M2 que si le coefficient intra-classe `ICC = σ²_entre / (σ²_entre + σ²_dans)` est nettement positif ; si `ICC → 0`, les rangs des `c_i` sont du bruit et leur inversion ne déplace rien en espérance. Les huit suites existent déjà : `σ²_dans` et `σ²_entre` sont estimables sur CPU, avant tout adaptateur, sans lecture de résultat.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Contrôle négatif de F1 vrai par construction.** B propose de comparer `f_active` au « regroupement aléatoire (permutation des indicateurs de forme parmi actions) ». Permuter les 6-uplets entre actions préserve exactement le multiensemble des 6-uplets, donc la distribution des tailles de classe, donc `f_active`. Le test de Fisher annoncé compare deux quantités identiques : il ne peut rien falsifier. Il faudrait un regroupement de référence à *entropie contrôlée* (6-uplets tirés indépendamment coordonnée par coordonnée selon les marginales), pas une permutation.
2. **Contrôle négatif de F2 tautologique.** « Ajouter un indicateur supplémentaire devrait réduire `Δ_intra` » : raffiner une partition ne peut qu'abaisser l'étendue intra-classe. Ce n'est pas un contrôle, c'est une inégalité.
3. **`Δ_intra` n'est pas la quantité qui gouverne M2.** M2 dépend du déplacement *par action* `|log c_σ(i) − log c_i|`, pondéré par le nombre d'actions ; B prend la médiane *par classe* de l'étendue, qui est dominée par les classes de taille 2 si elles sont majoritaires. Et surtout, F2 ignore `σ²_dans` : une étendue de 0,30 décade n'apporte rien si elle est faite de bruit d'échantillonnage (cf. outil commun).
4. **Fuite de conception dans la garde de F2.** « Si `Δ_intra < 0,15`, modifier la conception (classes plus larges) » : les classes sont définies par les six indicateurs de la base (RAPPORTÉ). Élargir les classes au vu des données brise l'identité P4 (les marginales de forme ne sont plus préservées) *et* ajuste le mécanisme à l'effet recherché. C'est précisément une fuite construction→évaluation.
5. **F3 : appariement indéfini.** `M2_distill = |log coût_élève − log coût_maître_réapparié|` suppose que l'élève, en génération libre, émet la *même action* que le maître. Rien ne le garantit ; sans forçage d'enseignant (teacher forcing) ou appariement par clé d'action, la paire n'existe pas. En outre, si l'appariement est fait sur les épisodes d'entraînement, `M2_distill` mesure la mémorisation, pas le transfert.
6. **F4 : hypothèse et métrique discordantes.** `H_A` est énoncée en « taux de détection ≤ 0,05 (au hasard) » — un taux de détection égal au niveau nominal est le FPR, pas le hasard — puis mesurée en AUC. Et la falsification de `H_B` exige « AUC ≈ 0,50 sur le maître », ce que B présente comme acquis par construction. Ce n'est acquis que si le score de la base est une fonction des seules marginales (voir ma critique de C, point 4, et E A.1).
7. **F6 confond réécriture et entraînement.** Le témoin monotone est un *adaptateur entraîné* ; le modèle de base nu ne l'est pas. Un écart Mann-Whitney ne distingue pas l'effet de la réécriture (que les FAITS disent déjà à l'identique, RAPPORTÉ) de l'effet de l'optimisation. C traite cette distinction (E5) ; B ne la voit pas.
8. **F7 : duel non exhaustif.** `H_A : M2 ≤ 0,50`, `H_B : M2 > 0,50`, mais la falsification de `H_A` ajoute « *et* indistinguable du couplage aléatoire ». Le cas `M2 > 0,50` *et* distinguable ne falsifie ni l'un ni l'autre tel qu'énoncé. De plus, le « couplage aléatoire sans structure de classe » viole l'invariance de forme : ce n'est pas un contrôle du même bras, c'est un autre bras.
9. **(c) : « détecteur trivial M2 = 0 ».** M2 est une métrique de dommage, pas un classifieur ; « le battre en RMSE » n'a pas d'objet défini.
10. **Aucune tâche réservée.** Toutes les mesures de B se font sur les 8–16 tâches qui servent aussi à construire les classes et à entraîner : la fuite construction/évaluation est totale sur le transfert.

### (b) Conditions sous lesquelles les critères de B perdent leur puissance (HYPOTHÈSE)

- **F1 (`f_active`, Fisher).** Si l'appartenance de classe est déterminée au niveau de la tâche (toutes les actions d'une tâche partagent un 6-uplet), les épisodes ne sont pas indépendants : `n_eff` ≈ nombre de tâches (8–16), et le Fisher sur épisodes surestime l'évidence d'un facteur ≈ (actions par tâche). Non jugeable si la corrélation intra-tâche `ρ → 1`.
- **F2 (`Δ_intra`).** Médiane d'étendues : si la loi des tailles de classe donne `P(n_k = 2) > 0,5`, l'estimateur est l'étendue de deux tirages, dont la loi a une masse importante près de 0 ; aucun seuil ne sépare `H_A` de `H_B` si le nombre de classes de taille ≥ 2 est inférieur à ~5 (illustratif).
- **F3 (`M2_distill`).** Si, dans une classe, la loi des coûts est dégénérée (`σ²_entre ≈ 0`), `M2_distill ≈ 0` à toutes les doses : `H_A` est vraie par construction. Si l'élève et le maître diffèrent d'action sur une fraction `q` des épisodes, la médiane n'est définie que sur `1 − q` : non jugeable dès que `q` dépend de la dose.
- **F4 (AUC, seuil 0,55).** Avec `n` ≈ 16 épisodes par bras, l'écart-type de l'AUC sous `AUC = 0,5` est ≈ 0,10 (calcul approché selon Hanley & McNeil, 1982, *The meaning and use of the area under a ROC curve*, Radiology). Un seuil à 0,55 est à un demi-écart-type du hasard : indécidable. Il faut `n ≳ 200` par bras (illustratif) pour que 0,55 soit à deux écarts-types.
- **F5 (incréments, test des signes, Holm).** Test des signes unilatéral à `n = 8` : `p = 1/256 ≈ 0,004` si 8/8 positifs, `≈ 0,035` si 7/8 (calcul exact). Après Holm sur 3 contrastes, le premier doit être < 0,0167 : seul 8/8 passe. Si les incréments vrais valent une fois leur écart-type, `P(8/8) ≈ 0,84⁸ ≈ 0,25` (illustratif). Puissance ≈ 0,25 pour un effet pourtant net.
- **F6 (Mann-Whitney).** Si M2 a une masse en 0 (chaînes identiques), les ex æquo écrasent la statistique ; si les actions d'une même tâche sont corrélées, le test est anti-conservateur.
- **F7 (seuil 0,50 décade).** Si l'étendue maximale intra-classe de `log10 c` est < 0,50, `H_B` est impossible par construction : le duel ne porte plus que sur le bruit.

### (c) Contrôles négatifs dont l'absence serait fatale chez B

- **Contrôle positif de sensibilité de la base** (ex. coûts multipliés par un facteur fixe) : sans lui, « la base échoue sur l'élève » (F4) est indistinguable d'une base incompétente. B n'en a aucun.
- **Second lot indépendant de références cachées** : sans lui, l'alignement entre `c_i` et `r_i` (outil commun) n'est pas mesurable et P3 peut échouer ou réussir pour une raison sans rapport avec le couplage.
- **Diagnostic « constante par classe »** (corrélation de rang élève/référence) : sans lui, un élève qui émet la médiane de classe passe F3 et F7 et donne un faux positif de mécanisme.
- **Tâches réservées** : sans elles, aucun énoncé de transfert n'est jugeable.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **E1 confond référence cachée et coût d'origine.** Le contrôle négatif de E1 exige une « déviation exactement nulle par rapport au coût honnête d'origine » à `p = 0`. Mais M2 est définie contre la *référence cachée* (RAPPORTÉ), pas contre le coût d'origine : `M2_maître(p = 0)` n'est pas nulle, c'est l'erreur honnête naturelle. Et `M2_maître(p = 1)` n'est pas le déplacement intra-classe : c'est `|log c_σ(i) − log r_i|`, qui peut *baisser* par rapport à `p = 0` si les `c_i` sont mal alignés avec les `r_i` (point A.2 de E). E1 est donc mal posée : sa borne « capacité du canal » n'est pas une borne de M2.
2. **« AUROC = 0,5000 exactement par identité M-3 » est faux en général.** L'identité M-3 porte sur les marginales du corpus (multiensemble des coûts, indicateurs par action, octets des autres champs). La base note des *transcriptions* ; à `p = 1`, chaque transcription diffère de son homologue `p = 0` par l'appariement action–coût. Si le score de la base dépend de la relation entre description et coût — ce que les FAITS ne précisent pas —, l'AUROC sur le maître peut s'écarter de 0,5. C érige en contrôle négatif exact une propriété qui n'est garantie que pour une base dont le score est une fonction des marginales seules. C'est la même erreur que B (F4) ; E (A.1) l'évite.
3. **« Vice d'échelle » de E2 surestimé.** C affirme qu'à `p = 1/4`, « échanger uniquement des voisins immédiats ne déplace les coûts que de quelques pourcents ». Faux : `k` transpositions adjacentes le long d'une géodésique peuvent déplacer *un* élément de `k` rangs (le « faire remonter »). Le déplacement en décades à dose nominale `p` dépend de la permutation particulière tirée par graine, pas de l'adjacence des opérations. L'effet de plateau est une possibilité, pas une conséquence mécanique ; le ratio `R_1/2` mesure alors surtout la variabilité du tirage.
4. **Contrôle négatif de E2 circulaire.** La permutation uniforme intra-classe a bien une distance de Kendall normalisée d'espérance 1/2 (vrai). Mais lui attribuer « `R_1/2 ≈ 0,50` attendu » présuppose la linéarité Kendall→M2, qui est ce que E2 veut tester.
5. **E3 : la corrélation de rang est indéfinie en génération libre.** `τ_élève` intra-classe suppose que l'élève émet des actions appartenant aux mêmes classes que le maître, en nombre ≥ 2 par classe. Rien ne le garantit (même objection qu'à B.F3). De plus, le contrôle `τ(p = 0) ≥ +0,40` est une exigence sur l'*alignement honnête* `c`–`r`, pas sur l'élève : il échoue dès que `ICC` est faible, pour une raison étrangère à la distillation.
6. **E3 et E5 non exhaustifs.** E3 : si `M2_élève(1) < 0,15`, aucune hypothèse n'est falsifiée ; C ne le dit pas. E5 : `Δ_0 < −0,03` (l'adaptateur identité *dégrade* M2) ne falsifie ni `H_A` ni `H_B` tel qu'énoncé — or c'est le cas qui produirait un faux négatif sur P3.
7. **Statuts glissés.** « `q_proj, k_proj, v_proj, o_proj` » et « 8 suites par action évaluée » sont présentés comme RAPPORTÉ ; les FAITS disent seulement « projections d'attention » et « huit suites du modèle de base ». Faible gravité, mais règle 1.
8. **Fuite construction/évaluation.** L'étape 2 de C exécute E3–E5 (lecture de M2 et d'AUROC sur l'élève) sur les tâches de réserve avant scellement, puis rien n'exclut ces tâches de l'expérience décisive. Les seuils (0,25 ; −0,25 ; 0,03) sont calibrés sur les mêmes données qui serviront à juger.
9. **Ce que C fait mieux que B** (je m'en sers) : scission P4a/P4b ; diagnostic d'effondrement modal (E3) ; contrôle positif de sensibilité de la base ; test médiane basse/haute ; taux d'illisibilité différentiel par dose ; vérification de la dose réalisée. Ce sont des contrôles que B n'a pas.

### (b) Conditions de perte de puissance (HYPOTHÈSE)

- **E1 (`M2_maître(1)`, seuil 0,25).** Espérance de `M2_maître(1) − M2_maître(0)` ≈ fonction croissante de `ICC` et de `σ²_entre` ; si `σ²_dans ≥ σ²_entre` (ICC ≤ 0,5), l'inversion des rangs des `c_i` déplace surtout du bruit et l'écart tend vers 0 quelle que soit la « capacité du canal ». E1 peut falsifier `H_A` pour une raison que C n'a pas nommée.
- **E2 (`|τ_mesuré − p| ≤ 0,02`).** La distance de Kendall normalisée est discrétisée au pas `1/N`, `N = Σ_k C(n_k, 2)` (sous l'hypothèse de normalisation globale de C). Si `N < 50`, le pas dépasse 0,02 : la tolérance est inatteignable par construction. Le ratio `R_1/2` a un dénominateur `M2_maître(1)` ; s'il est proche du plancher honnête, le ratio a une variance divergente.
- **E3 (`τ_élève`).** Si `P(n_k = 2)` domine, `τ` par classe ∈ {−1, +1} ; l'agrégat est une somme de Bernoulli signées dont l'écart-type vaut `1/√(nombre de classes)` ; avec 20 classes (illustratif), ±0,22 — le seuil −0,25 est au bord du bruit. Les ex æquo dans les coûts générés par l'élève (répétition d'une valeur) rendent `τ` indéfini sur une fraction qui peut dépendre de la dose.
- **E4 (AUROC ∈ [0,45 ; 0,55]).** Même objection qu'à B.F4 : avec 16 épisodes par bras, l'écart-type est ≈ 0,10 ; l'intervalle [0,45 ; 0,55] est franchi par le hasard environ une fois sur deux (illustratif).
- **E5 (`|Δ_0| ≤ 0,03`).** Écart-type de la médiane de 8 tirages ≈ `1,25·σ_dans/√8`. Pour `σ_dans = 0,3` décade (illustratif) : 0,13 par action ; sur 240 actions indépendantes, ≈ 0,01 ; mais si l'unité d'indépendance est la tâche (16), ≈ 0,03 : le seuil est au niveau du bruit, non jugeable. C a le bon contrôle (deux lots de 8 suites) mais n'en tire pas la condition.
- **Contrôle positif de la base (TPR ≥ 0,80 sur ×10^0,15).** Si la loi des coûts honnêtes a une dispersion inter-tâches ≫ 0,15 décade, un facteur global de 1,41 est noyé dans la marginale et le contrôle positif échoue sans que la base soit en cause ; il faut un contrôle positif *apparié* (même action, coût altéré).

### (c) Contrôles négatifs dont l'absence serait fatale chez C

- **Mesure de `ICC` (σ²_dans vs σ²_entre) sur les huit suites** avant E1 : sans elle, un échec de E1 est inexplicable et une réussite peut être un artefact d'alignement.
- **Appariement par clé d'action ou forçage d'enseignant** pour E3 : sans lui, `τ_élève` n'est pas calculable.
- **Vérification que le score de la base est fonction des seules marginales** (ou calcul effectif de l'AUROC sur le maître sans la supposer à 0,5) : sans elle, le « contrôle négatif » de E4 est une pétition de principe.
- **Jeu de tâches disjoint pour l'expérience décisive** : sans lui, les seuils de C sont ajustés sur les données de jugement.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Peu d'estimateurs.** E énonce les bonnes failles (A.1 sur la loi jointe, A.2 sur la référence, A.3 sur Kendall, A.6 sur le témoin entraîné, A.7 sur les fuites de provenance) mais, pour la plupart, sans estimateur ni seuil. Une faille sans estimateur n'est pas jugeable (R13 : critères gelés). En particulier A.2, la faille la plus importante, reste une anecdote `(0,1)/(1,0)` ; l'outil `ICC` ci-dessus en est une formulation mesurable que E ne donne pas.
2. **Duel I n'est pas un duel empirique.** `H_B` est « falsifiée par une preuve sur le code gelé » : une preuve, pas une mesure. Si la base est un modèle (les FAITS ne disent pas si elle est neuronale), « identité exacte sans tolérance » échoue sur des différences d'ordre de sommation en virgule flottante, et le duel devient un faux positif de non-identité. E ne distingue pas différence de représentation et différence numérique inerte.
3. **Duel II : composite et sensible au bruit.** `H_A` exige `Δ_p` non décroissants *et* `Δ_1 ≥ 0,15`. Avec trois comparaisons bruitées, une baisse entre doses voisines due au seul bruit falsifie `H_A` : E dit « verdict indécis » mais ne donne aucune règle (bandes, test de tendance) pour distinguer baisse et bruit. Par ailleurs, E ne remarque pas que, la référence étant déjà disponible, **tout le Duel II est calculable sur CPU avant tout entraînement** — ce qui en fait une porte à coût nul que E chiffre pourtant dans son enveloppe GPU.
4. **Duel III : degrés de liberté.** L'estimation « par famille de tâches et graine » est correcte en principe, mais avec 8–16 tâches au total, réserver des *familles* laisse 2 à 4 unités par bras (illustratif) : E reconnaît l'indécision possible sans dire que c'est le cas probable.
5. **Duel IV : marge indétectable.** « Taux de détection dépasse les fausses alertes de plus de 5 points » : différence de deux proportions estimées sur ≈ 16 épisodes chacune, écart-type ≈ `√(2·0,05·0,95/16)` ≈ 0,077 (calcul) : la marge est inférieure à un écart-type. Non jugeable à cette taille.
6. **Duel V : seuil sans loi.** « Changement de `Δ_1` < 0,05 décade entre lots de référence » : la loi de la différence de deux médianes basses de 8 tirages a un écart-type ≈ `√2·1,25·σ_dans/√8` par action ; sans estimation de `σ_dans`, le seuil est posé à l'aveugle.
7. **Pas de diagnostic de mécanisme.** E mentionne la « dégradation générale » et la mémorisation, mais ne propose pas l'estimateur qui sépare inversion de rang et constante par classe (C.E3). Un élève émettant la médiane de classe passe les Duels II–V de E.
8. **Enveloppe incohérente avec ses propres chiffres.** 48 M jetons cumulés (illustratif) à un débit LoRA plausible de quelques milliers de jetons/s (illustratif) donnent quelques heures-GPU, pas 40–160. E reproduit l'objection 4 des juges (« devis sur débit non mesuré ») qu'il cite lui-même.
9. **Ce que E fait mieux que B et C** (je m'en sers) : séparation des quatre portes (P4-maître, P3-maître, P3-élève, discrétion-élève) ; témoin identité passé *intégralement* dans le même pipeline, distinct du modèle nu ; trajectoires de permutations imbriquées préspécifiées ; dénominateur gelé avant exclusion des classes inertes ; interdiction d'appeler « discrétion » le couple absence de détection + absence de dommage.

### (b) Conditions de perte de puissance (HYPOTHÈSE)

- **Duel I.** Si le score de la base est une fonction `s(marginales) + ε` avec `ε` numérique, l'identité stricte est violée presque sûrement ; si `s` dépend de la loi jointe (action, coût), l'identité est fausse mais le duel ne le détecte que si l'échantillon contient des classes où la jointe change — ce qui dépend encore de `ICC` et de `σ²_entre`.
- **Duel II.** `P(au moins une baisse entre doses voisines | incréments vrais μ, bruit σ)` ≈ `1 − Π Φ(μ_j/σ)` ; pour `μ_j/σ = 0,5`, ≈ 0,66 (illustratif) : `H_A` est falsifiée par le bruit deux fois sur trois même si l'effet est réel.
- **Duel III.** Avec `k` familles réservées et 3 graines, l'estimateur de contraste a `k·3 − 1` degrés de liberté au mieux, mais les graines partagent les familles : `df` effectif ≈ `k − 1`. Pour `k ≤ 3`, aucun seuil n'est jugeable.
- **Duel IV.** Voir (a).5 ; jugeable seulement si `n ≳ 300` épisodes par bras (illustratif) ou si la marge est portée à ~15 points.
- **Duel V.** Jugeable seulement si `σ_dans` est estimé et si le seuil est fixé à un multiple gelé de l'écart-type plancher mesuré par recalcul sur deux lots.

### (c) Contrôles négatifs dont l'absence serait fatale chez E

- **Estimateur d'alignement `c`–`r` (ICC) et prédiction exacte de `M2_maître(p)` sur CPU** : E nomme la faille A.2 mais n'a pas le contrôle qui la ferme.
- **Diagnostic d'inversion de rang chez l'élève** (corrélation de rang intra-classe, avec appariement par clé d'action) : sans lui, Duel III ne distingue pas mécanisme et étourderie (objection 6 des juges, RAPPORTÉ).
- **Contrôle positif apparié de la base** (même action, coût altéré d'un facteur gelé) : E le mentionne comme « anomalies mécaniques connues » sans le spécifier ; sans spécification gelée, il n'est pas un contrôle.
- **Mesure de débit avant devis** : sans elle, l'enveloppe de E ne peut pas passer la porte « toute dépense sous devis et GO ».

---

## Note transversale (pour l'arbitre, sans fusion)

Les trois propositions partagent un angle mort que je n'ai vu nommé par aucune : la référence cachée et le coût honnête du maître sont deux tirages du même modèle. Tant que `ICC` n'est pas mesuré, (i) `Δ_intra` de B, (ii) `M2_maître(1)` de C et (iii) le Duel II de E peuvent tous donner un résultat trop propre dans l'un ou l'autre sens — un effet nul parce que les rangs des coûts étaient du bruit, ou un effet net parce que les coûts honnêtes étaient, par hasard de tirage, anti-alignés avec la référence. Duel proposé, exécutable sur CPU avant scellement : `H_A` : `ICC ≥ 0,5` (illustratif) dans les classes de taille ≥ 2 ; `H_B` : `ICC < 0,5`. Si `H_B`, le bras B n'est pas testable avec cette référence quel que soit l'élève ; si `H_A`, la hausse attendue de M2 sur le maître devient une prédiction *chiffrée* à inscrire dans le préenregistrement, et un écart du maître à cette prédiction serait le premier signal d'un pipeline défaillant (R4).

FIN-DE-CELLULE