# Proposition A — tour III.3 : réponse aux critiques

Convention des statuts inchangée (RAPPORTÉ, VÉRIFIÉ, OBSERVÉ-NON-AUDITÉ, HYPOTHÈSE). Tout seuil que j'introduis est **illustratif**. Les quatre critiques (B, C, D, E) sont présentes et entières ; je ne réponds qu'aux sections « Sur la proposition A ». Je ne reconstruis pas les clauses retirées de la pièce 7 § h.

## (a) Réponses, critique par critique

Je regroupe par expérience. « Acceptée » signifie que le dessin de (b) intègre la correction ; « rejetée » donne la raison ; « transformée en test » signifie que l'objection devient une hypothèse ou un contrôle de (b).

### E1 — dents du pôle

| auteur | critique | verdict et raison |
|---|---|---|
| D | le contrôle « même lancement sur T0.5 déjà lue » change banque, distribution, calibrage, difficulté : une puissance supérieure n'est pas une fuite | **Acceptée.** Contrôle retiré. Mon intention était de sonder l'option D-P4 (b) de la pièce 7 ; cela relève d'E2, pas d'E1. |
| D, E | H_A (≥ 0,70) et H_B (< 0,30) ne couvrent pas l'intervalle ; une puissance élevée avec erreur excessive n'appartient à aucune issue | **Acceptée.** H_A et H_B deviennent complémentaires et portent sur le couple (puissance, erreur) — voir (b). |
| B | il manque un témoin de loi correctement spécifiée à effet exactement nul (θ = 0), distinct des faux par permutation | **Acceptée.** Troisième classe de témoins ajoutée ; sans elle « rejette les faux » et « rejette tout ce qui n'est pas tautologique » sont indiscernables. |
| C | il manque un témoin « vrai mais mal calibré » (effet réel 0,3, déclaré 1,2) : sans pari à fraction, le juge élimine des lois directionnellement vraies (μ_i ≤ 0) | **Transformée en test.** Quatrième classe de témoins. La pièce 5 signale un « pari à fraction (levier de puissance à coder) » (RAPPORTÉ) : l'issue dit si ce levier est un préalable à la boucle. |
| B (b), C (b), D (b) | puissance nulle quand N·d_i ≤ log(m/α) ; aucune courbe e-BH à petit m n'existe ; E1 confondra « faux » et « faible » | **Acceptée.** La courbe e-BH à petit m (déjà dans mon tableau (c), 0 $) devient **préalable** à E1 et fixe n ; E1 mesure une courbe puissance × force (0,3 / 0,5 / 0,8), pas un seuil unique. « Pas de dents à la force 0,3 » n'est plus lu comme « pas de dents ». |
| E (b) | corrélation intraclasse des témoins (n_eff ≈ n / [1 + (b − 1)ρ]) | **Acceptée.** Témoins répartis sur des moniteurs distincts ; n_eff déclaré au préenregistrement. |

### E2 — fuite entre générations

| auteur | critique | verdict |
|---|---|---|
| B 1, D, E | les filles d'éliminées ne sont pas « non exposées » : leurs parents ont reçu un verdict sur E₁, et le canal mémoire-leçons est partagé par tous les bras (pièce 4 : les leçons « parlent de science », RAPPORTÉ) | **Acceptée.** Contrôle remplacé par deux contrôles : (i) filles de parents tirés au sort dans g1 **avant tout verdict** (D, B (c) 2) ; (ii) plan croisé sélection × mémoire : la mémoire (leçons, survivantes, éliminées) est transmise ou non dans chaque bras d'épreuve. |
| C 3 | les témoins faux plantés en g2 (permutation dans la tâche) ne descendent pas des parents sélectionnés : même loi sur E₁ et E₂, ils diluent l'estimateur de fuite | **Acceptée, avec séparation.** Les témoins faux servent au **niveau** (vérifier α par bras), pas à la **fuite**. La fuite se mesure sur les filles produites par la chaîne adaptative. |
| D, E | R − F confond réutilisation et différence de distribution si P_{E₁} ≠ P_{E₂} ; il faut échanger les lots | **Acceptée.** Réplique miroir : g1 sélectionnée sur E₂, g2 jugée sur E₂ (R′) et E₁ (F′). |
| E | fréquence de faux témoins promus ≠ FDR ; une fille de parents faux peut être vraie | **Acceptée pour le réel, rejetée pour la simulation.** En simulation la nullité d'une fille est définie par le générateur (nul des filles v2, « filles triviales », pièce 6, RAPPORTÉ), pas par ses parents. Sur banque réelle aucune vérité des filles n'existe : la réplique réelle ne rend que Δ(R − F), exploratoire. Métrique : FDP par bras = V / max(R_s, 1), taux par témoin déclaré à part. |
| B (b) | 20 témoins par bras : Δ détectable ≈ 0,22 ; dessin sous-dimensionné | **Acceptée.** Les témoins sans agent coûtent 0 appel (pièce 5, RAPPORTÉ) : en simulation ≥ 200 témoins par bras ; le réel reste borné par le nombre de fiches et n'est pas décisif. |
| D (b) | après sélection sur E₁, E[e_{g,i} | F_{g−1}] ≤ 1 n'est plus garanti : c'est la garantie conditionnelle de Ville qui disparaît | **Acceptée comme formulation de H_A.** |

### E3 — héritage des éliminées

| auteur | critique | verdict |
|---|---|---|
| B 2, C (via E), D, E | SE-perm conserve volume et vocabulaire : il ne sépare pas « raison » et « texte » ; les raisons permutées peuvent devenir incohérentes (archive moins crédible) ; S reçoit moins de texte | **Acceptée.** Quatre bras appariés en longueur : S ; SE-exact ; SE-vide (éliminées sans raison, complétées par un texte de catalogue public apparié) ; SE-perm gardé comme bras de bruit. Je rejette l'archive « hors domaine » que B emprunte à E : comme C le dit sur E, elle introduit une distraction, donc n'est pas neutre. |
| D, E | la redite est définie par la mémoire que l'expérience doit évaluer : circularité ; s = f rend R̂ non identifiant | **Acceptée.** Vérité de redite scellée par un metteur en forme tiers (paraphrases plantées d'éliminées, voisines réellement distinctes) ; le refus de la mémoire devient une mesure de l'instrument, lue contre cette vérité. |
| D (b) | sœurs corrélées : l'unité est la population, pas la fiche | **Acceptée.** Réplication par (proposeur × graine). |

### E4 — ablation

| auteur | critique | verdict |
|---|---|---|
| C 2 | les parents de P ont passé le pont (sortie 1) ; leurs filles héritent opérateurs et moniteurs du catalogue et sont traduisibles ; celles de J et T sont renvoyées N1–N4 avant E₃ : avantage vrai par construction de la **traduisibilité**, pas du juge | **Acceptée — c'est la critique la plus lourde reçue.** Bras ajouté : **Tr** = fiches en sortie 1 du pont avec accord, ensemencées **sans** verdict du juge (C (c) 1). P se compare à Tr, pas à J. |
| B 3, D, E | épreuve fraîche ≠ fin de la circularité : alignement d'instrument (mêmes nuls, mêmes classes de lois) ; audit indépendant à horizon fixe requis | **Acceptée en partie, rejetée en partie.** Acceptée : confirmation terminale à **horizon fixe** (pas de règle d'arrêt), gelée avant, commune à tous les bras, jamais utilisée pour choisir les parents. Rejetée : qu'un juge « de structure différente » (autre nul) soit plus valide — il change l'estimand ; le nul informé **est** la question scientifique (« bat-elle le connu ? »). Ce qui doit changer, c'est la règle d'arrêt et le gel, pas le nul. |
| C 1, E (b) | ratio promues / coût confond effet causal et coût fixe au dénominateur ; r = E[Y]/E[C] ≠ E[Y/C] | **Rejetée comme erreur, acceptée comme confusion de deux questions.** Si le pôle double la part de filles vraies et triple le coût, conclure « coût de vérification, pas sélecteur en boucle » n'était pas une erreur pour la question de **rendement**. Mais la question d'**héritabilité** en est une autre : deux métriques primaires séparées — part de filles confirmées à effectif égal ; coût total par bras rapporté à part. |
| B (c) 3 | bras « pôle inversé » (éliminées) plus informatif que T | **Acceptée pour le bras P̄, rejetée pour le retrait de T.** Sans T on ne sait pas si P est meilleur ou P̄ pire ; l'asymétrie est la mesure. |
| C (b) 2, B (b), D (b), E | Fisher à n = 10 : puissance nulle dès que S ≤ 2 ; sœurs corrélées ; ratios 0/0 | **Acceptée.** Je conclus ce que je n'avais pas conclu : **en l'état, E4 n'est pas jugeable.** Il devient conditionnel à E1 (H_A tenue) et à ≥ 3 populations indépendantes par bras ; sinon il n'est pas lancé. |
| D | étiquettes de parents permutées à bassins, budgets et effectifs constants | **Acceptée** comme contrôle. |

### E5 — règle de sortie

| auteur | critique | verdict |
|---|---|---|
| B 4, D, E | kappa mesure l'accord, pas la validité ; il faut des reparamétrisations exactes et des voisines distinctes à vérité scellée | **Acceptée.** Métrique primaire = exactitude sur témoins scellés (reparamétrisation / paraphrase / voisine distincte / hors périmètre) ; kappa secondaire. |
| C 4 | une fiche hors périmètre est classée « neuve » par défaut de case : accord par construction | **Acceptée.** Grille à quatre états : redite de Hx / affine Hx / neuve dans le périmètre / hors périmètre. |
| C (b) 3 | prévalence « neuve » → 1 car la mémoire a filtré en amont ; Var(κ) diverge | **Acceptée pour le remède, rejetée pour la cause.** La mémoire du pôle refuse les redites de **fiches du pôle**, pas les redites de H1–H9 (qui n'y sont pas, sauf plantation). La prévalence est contrôlée par la plantation (≈ moitié de témoins « redite »). |
| D, E | contrôle sur éliminées non décisif ; « tautologique » ≠ « neuve mais non décisive » ; « décisive pour une porte » n'a pas d'estimateur | **Acceptée.** Contrôle et témoin retirés ; « décisive pour une porte » reste hors de toute mesure (mon S9). |

### E6 — effondrement sur une lignée

| auteur | critique | verdict |
|---|---|---|
| B (b) | si L ≤ 3 lignées initiales, l'effondrement est certain sous toute sélection | **Transformée en test.** L devient un facteur (3, 10, 30, illustratif) ; « 17 idées distinctes » est RAPPORTÉ, « beaucoup partagent un axe » est une HYPOTHÈSE de B. |
| D, E | le monde plat peut se concentrer par dérive : interdire la concentration y définit l'artefact | **Acceptée.** Référence = distribution de concentration sous **reproduction neutre** avec le même graphe de parenté (E) ; H_A porte sur le dépassement de son quantile. |
| E | descendances à deux parents | **Acceptée.** Contribution fractionnaire ½ par parent ; entropie sur les contributions. |
| D | vrai dans le seul monde paramétré pour cela | **Acceptée** ; déjà dit, redit en (c). |

## (b) Expériences corrigées

Règle commune, en réponse à D et E sur l'exhaustivité : chaque duel oppose H_A : θ > δ et H_B : θ ≤ δ (complémentaires). Décision par borne de confiance préenregistrée ; un intervalle qui chevauche δ ne falsifie **pas** l'hypothèse mais falsifie le **dimensionnement**, et l'expérience n'est lancée que si ce cas a une probabilité ≤ 0,2 (illustratif) sous les deux valeurs typiques déclarées. Graines par `SeedSequence` (R9), lecture par lecteur neuf (R13), symétrie R4.

### Préalable P0 — courbe e-BH à petit m (processeur, 0 $)
Simulation sur les banques synthétiques de l'expérience 1 du juge : m ∈ {5, 10, 20, 50}, k = 2 lois vraies, forces 0,3 / 0,5 / 0,8, 1 000 courses. Sortie : n requis pour une puissance de 0,7 (illustratif) par (m, force). Sans ce nombre, aucune des expériences suivantes n'a d'effectif.

### E1′ — dents sur épreuve fraîche
- **Témoins (4 classes, moniteurs distincts)** : V (vrai, force 0,3 / 0,5 / 0,8) ; F (faux par permutation dans la tâche, pièce 7 a.3) ; Z (loi bien formée, θ = 0, B) ; M (vraie directionnellement, amplitude déclarée × 4, C).
- **H_A** : π(0,5) > 0,5 **et** FDP ≤ 0,05 sur {F, Z} (illustratif). **H_B** : complément.
- **Secondaire** : π(M) / π(V à force égale) : si < 0,5, le pari à fraction ou l'affinage sur développement est un préalable.
- **Issue** : H_B → la règle (a) de la demande (mort ∧ promue) est une règle d'extinction à cet effectif ; trois états obligatoires et budget d'épisodes avant toute course 2. H_A → l'appui principal des trois états tombe ; reste la traduisibilité (S3).
- **Condition** : une épreuve fraîche (banque sœur) de n fixé par P0. Sans elle, non lançable.

### E2′ — fuite (simulation décisive, réel exploratoire)
- **Plan 2 × 2 × 2** : épreuve {R : réutilisée, F : fraîche} × mémoire {transmise, vide} × lot {E₁ puis E₂, E₂ puis E₁}. Vérité des filles définie par le générateur (nul des filles v2).
- **Contrôles** : filles de parents tirés au sort avant verdict (niveau non sélectionné) ; témoins F pour le niveau α par bras, hors de l'estimateur de fuite.
- **H_A** : FDP(R) − FDP(F) > 0,05 (illustratif) à mémoire vide : la sélection seule casse la garantie conditionnelle. **H_B** : ≤ 0,05. Effet de la mémoire lu dans l'interaction.
- **Issue** : H_A → « fraîche seulement » obligatoire ; D-P4 (b) falsifiée, coût ≈ une banque par génération (pièce 7 a.4, 300 épisodes pour 17 fiches, RAPPORTÉ). H_B → D-P4 (b) admissible en exploratoire ; si l'interaction mémoire est positive, le canal à fermer est la mémoire, pas l'épreuve.
- ≥ 200 témoins par bras en simulation (0 appel) ; réplique réelle rapportée sans décision.

### E3′ — héritage des éliminées
- **Quatre bras appariés en longueur** : S ; SE-exact ; SE-vide ; SE-perm. Réplication par (proposeur × graine), ≥ 4 populations par bras (illustratif).
- **Vérité scellée** : paraphrases plantées d'éliminées et voisines distinctes, écrites par un metteur en forme tiers.
- **H_A** : part de redites vraies proposées (SE-exact) < part (SE-vide) − 0,1 (illustratif), à promues neuves ≥ 0,8 × S. **H_B** : complément.
- **Issue** : H_A → (b) de la demande tenue, la raison porte de l'information. H_B → éliminées à la mémoire seulement, jamais aux proposeurs ; si SE-vide ≈ SE-exact ≈ S, l'archive détaillée n'a pas de marge (effet de plafond, D).

### E4′ — ablation (conditionnelle)
- **Lancée seulement si** E1′ rend H_A et ≥ 3 populations indépendantes par bras.
- **Cinq bras à effectif de filles égal** : P (promues) ; P̄ (éliminées du pôle) ; Tr (sortie 1 du pont sans verdict) ; J (juges-modèles seuls, mais restreint aux fiches passées par le pont pour que les filles soient jugeables) ; T (aléatoire). Contrôle : étiquettes de parents permutées.
- **Confirmation terminale** : horizon fixe gelé sur E₃ fraîche, test de permutation sur la log-vraisemblance hors échantillon contre le nul informé ; jamais utilisée pour choisir les parents.
- **H_A** : part confirmée (P) − part (Tr) > δ. **H_B** : ≤ δ. Coût par bras rapporté séparément, hors critère.
- **Issue** : H_A → le juge hérite quelque chose au-delà de la traduisibilité ; (f) tient. H_B avec Tr ≈ P → ce qui s'hérite est la traduisibilité : le pont sélectionne, le pôle vérifie. P̄ < T → le pôle élimine du faux même s'il n'enrichit pas.

### E5′ — lisibilité de la sortie
- **Grille à 4 états** ; témoins scellés : reparamétrisation exacte de H5, HC1, H9 (vérité « redite ») ; paraphrase (« redite ») ; voisine réellement distincte (« neuve ») ; hors périmètre. Prévalence plantée ≈ 0,5.
- **H_A** : exactitude ≥ 0,8 sur témoins **et** kappa ≥ 0,45 (pièce 1 § 6, RAPPORTÉ). **H_B** : complément.
- **Issue** : H_B → la règle (c) exige un préenregistrement par fiche lu par Lazar. « Décisive pour une porte » : pas d'estimateur, hors test.

### E6′ — diversité (0 $)
- Démonstration B du cycle v5 étendue : 10 générations ; L ∈ {3, 10, 30} ; deux mondes ; avec et sans garde ; lignées à contribution ½ par parent.
- **Référence** : distribution de la part de la lignée dominante sous reproduction neutre, même graphe de parenté, 1 000 tirages.
- **H_A** : sans garde, dans le monde fécond, la part dominante dépasse le quantile 0,95 de la neutre avant g10 pour L ≥ 10. **H_B** : complément.
- **Issue** : H_A → garde (d) nécessaire, coût lu en vraies filles perdues ; H_B → superflue dans ce monde. Pour L = 3, l'effondrement attendu même sous neutralité ne juge pas la garde (B). Rien ici ne borne une population réelle (D).

**Ordre** : P0 et E6′ (0 $) ; essai du pont (pièce 7 g, plafond 5 $, RAPPORTÉ) ; E5′ ; E2′ en simulation ; E1′ dès qu'une épreuve fraîche est devisée ; E3′ ; E4′ en dernier et sous condition.

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, recoupé entre pièces).** Le pôle a une plomberie qui tient : 136 appels, 5,89 $, 2 témoins vrais promus, 2 faux éliminés, 11 rejeux sur 11, dans un monde tautologique (pièce 4 ; chiffres OBSERVÉS-NON-AUDITÉS). Sur la seule banque réelle, il n'a pas de dents : 0 témoin vrai sur 20 à 120 épisodes, richesse 2,28 pour un seuil de 3,0 à 288 (pièces 5, 7). L'épreuve réelle est entièrement lue ; aucune épreuve fraîche n'existe ; couches 2 et 3 ne sont pas construites. Les tests de mort n'ont jamais été activés. Le pont est codé et essayé à modèles factices ; sa part attendue de fiches jugeables immédiatement est de l'ordre de 5 à 15 %, SUPPOSÉ par son auteur. La mémoire, le nul des filles et les marchepieds sont vérifiés en simulation, dans des mondes construits pour les faire réussir (pièce 6). Les hypothèses du programme ont déjà changé de lecture (N-013) et H9 vit sous réserve d'antériorité.

**Ce qui n'est pas établi.** (1) Que le juge figé promeuve une loi vraie de force réaliste sur une épreuve fraîche à un effectif payable : c'est la condition de toute la boucle, et elle n'a aucune mesure. (2) Que la règle « mort ∧ promue » sélectionne plutôt qu'elle n'éteint : avec S1 à S4, elle laisse 85 à 95 % des fiches hors jugement ; il faut trois états, et la pièce 2 (« indécise → test plus puissant ») contredit « non concluante ne passe pas » — la question impose l'une des deux sans le dire. (3) Que la sélection inter-générations soit compatible avec la garantie de Ville : D a raison que la garantie est conditionnelle et que la réutilisation d'épreuve la fait disparaître par construction ; la mémoire est un second canal, partagé. (4) Que ce qui s'hérite d'une génération à l'autre soit autre chose que la traduisibilité (C) : aucun dessin servi ne séparait les deux ; E4′ le fait, mais n'est jugeable qu'après E1′. (5) Que « neuve par rapport au programme » et « décisive pour une porte » soient des règles : la seconde n'a pas d'estimateur ; la première se teste (E5′) seulement contre des témoins à vérité scellée. (6) Que des lignées fécondes existent sur fiches réelles ; la perte de diversité commence avant la sélection (17 idées pour 29 fiches). (7) Q7 : les antériorités de la pièce 7 § i et celles de qualité-diversité (Lehman & Stanley 2011 ; Mouret & Clune 2015 ; à vérifier sur PDF) ne sont pas lues ; rien n'est « à reprendre tel quel » ; POPPER (référence à vérifier) reste la plus proche à lire durement.

**Ce que les critiques ont changé dans ma position.** Trois choses. Mon ablation E4 était non jugeable et circulaire par la traduisibilité, pas seulement par le juge ; elle devient conditionnelle. Mes contrôles négatifs d'E2 n'étaient pas non exposés ; la fuite se mesure d'abord en simulation, sur un plan sélection × mémoire × lots échangés. Mes métriques en ratio (promues par euro) confondaient rendement et héritabilité ; elles sont séparées. Je maintiens, contre une partie de B et D, que l'audit terminal doit garder le nul informé et changer la règle d'arrêt, pas le nul.

**L'expérience à faire en premier.** E1′ : quatre classes de témoins (vrais à trois forces, faux par permutation, nuls bien formés, vrais mal calibrés) sur une épreuve fraîche d'effectif fixé par la courbe e-BH à petit m. Si H_B tient, la boucle (a) à (g) ne peut pas être préenregistrée comme sélection : c'est un dispositif à trois états avec un budget d'épisodes par génération qui n'a pas de prix dans les pièces. Si H_A tient, E2′ puis E4′ deviennent jugeables. Le nœud qui commande E1′ est le devis de production d'une épreuve fraîche (≈ 300 épisodes du modèle de 8 milliards notés par deux juges pour 17 fiches, pièce 7 a.4 ; coût absent des pièces), chez session-depot. En attendant ce devis, deux pièces se jouent à 0 $ et tranchent des points réels : la courbe e-BH à petit m (elle dit si une génération de 5 à 20 fiches peut jamais promouvoir quoi que ce soit sous contrôle de multiplicité) et E6′ (elle dit si la garde de diversité a un objet dans le seul monde où on sait la mesurer). Aucune des trois ne contient de conception d'attaque ; aucune ne touche au sujet suspendu.

FIN-DE-CELLULE