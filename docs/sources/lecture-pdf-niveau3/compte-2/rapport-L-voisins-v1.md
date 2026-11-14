# Antériorité du lemme d'additivité « L » — deux voisins versés (Ker ; Bash, Goeckel et Towsley) — v1

- Début du travail : 2026-11-14 06:37:00 UTC ; ce fichier est écrit le 2026-11-14 06:43:05 UTC. Les deux heures ont été relevées par `date -u`, la seconde dans la commande qui écrit ce fichier.
- Lecteur : modèle A. Je suis aussi l'auteur des rapports L du lot 8, `rapport-L-lot8-v1.md` (`130283ad…`) et `rapport-L-lot8-v2.md` (`8d9f2654…`). Ces deux fichiers ne sont pas modifiés. Le présent rapport est un rapport neuf ; il ne remplace pas la v2 : il la complète sur deux voisins que la v2 nommait sans les avoir lus.
- Consigne appliquée : `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (vérifié), complétée par les interdits de mon premier mandat.
- Avant d'écrire, j'ai vérifié par un `ls` du seul dossier `compte-2/` qu'il n'existait ni `rapport-L-voisins-v1.md` ni `fichiers-de-travail-L-voisins-v1.tar`.
- Pièces, dans `…/scratchpad/pieces-main-complement-v1/`. L'empreinte sha256 de chacune a été vérifiée contre son compagnon `.sha256`, avec égalité :
  - `ker-2006/ker-2006-batch-steganography-pooled-steganalysis.pdf` (17 pages) : `a6ab71a257034976636aad130fb9a7715a45d3dd06cb69cf046475f8f231a2aa`
  - `bash-2012/1202.6423v4.pdf` (27 pages) : `ab6caeadb380ec322fb6d9400cde5aa04d6e32ddbb55a869c7efd6f3eebd1c49`
  - J'ai aussi relu les pages de bibliographie déjà lues au lot 8, pour l'identification seulement : `1906.08938v2.pdf` p. 15 (`3fbaedd9…`) et `2605.16140v1.pdf` p. 34-35 (`1f70a328…`).
- Citations contrôlées par programme : **67 citations, 0 échec**.
  - Script `controle_citations_voisins_v1.py` (même code que pour le lot 8) : `pdftotext` avec et sans `-layout`, normalisation des espaces, ligatures, césures, apostrophes et tirets.
  - Essai préalable : un cas juste réussi, deux cas altérés refusés. Le premier passage sur le fichier complet a donné 3 échecs (coupures de page, espace avant un point) ; ils ont été corrigés, et le journal est gardé.
  - Les citations sont dans `citations-L-voisins-v1.json`, qui se trouve dans l'archive seulement (sha256 `fc9b1e4544f490cecbfd830955fa74ed500134e23383b52a622d540d5b1c16b7`).
- Convention :
  - Tout extrait anglais entre « », titres compris, est une citation contrôlée suivie de son identifiant : [Kn] pour Ker, [An] pour Bash et collègues, [Rn] pour les renvois bibliographiques des pièces du lot 8.
  - Les formules sont marquées « lu sur le PDF, non contrôlé par programme ».
  - Chaque chiffre porte sa nature : « auteurs », « figure » ou « calcul ».

## Fichiers lus et étendue

1. `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, en entier.
2. Rappel : les interdits communs v2, ainsi que les extraits nommés de N-003/N-004, de la note mathématique v2, du programme et des états de l'art, ont été lus lors de mon premier mandat. Je ne les ai pas rouverts.
3. Ker : les 17 pages, lues ligne à ligne en texte brut, annexe (preuve du lemme 2) comprise. Aux p. 13 et 14, les graduations d'axes ont été filtrées. La page 13 (figure 4) a été vue en image.
4. Bash et collègues : les 27 pages, lues ligne à ligne en texte brut, annexes A à C et bibliographie comprises. Les longues dérivées de l'annexe A (p. 22-23) ont été parcourues sans être refaites.
5. `1906.08938v2.pdf` p. 15 et `2605.16140v1.pdf` p. 34-35, par leur texte, déjà extrait au lot 8.
6. `ls` du seul dossier `compte-2/`, et des deux dossiers de pièces.

Aucune ouverture fautive. Aucune recherche récursive dans le dépôt, aucune commande git, aucun appel réseau ni de modèle, aucune dépense. Aucun refus.

## 0. En tête : occupations

1. **L1, cœur de l'invariance — occupée en partie par Ker (2006).** Dans le cadre de la stéganographie par lots, Ker énonce l'invariance, à budget total fixé, de la loi de la statistique moyenne vis-à-vis de la répartition entre objets :
   - le budget total est fixé : « We also assume that the Steganographer wants to embed a fixed total amount of secret data » [K7] (p. 4), avec la contrainte r·p = B ;
   - la répartition est le choix de l'attaquant : « Within this range, he can vary r or p and should do so to try to minimize the chance of overall detection. » [K8] (p. 4) ;
   - le modèle est un pur décalage : « the distribution of the detector response only depends on p in the form of a shift, so that the (additive) estimation error is independent of the true value. » [K6] (p. 3) ;
   - l'énoncé : « the distributional shape of » [K14] … « does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B. » [K15] (p. 7) ;
   - la conséquence côté défenseur : « Also, the average method cannot punish the Steganographer for using a suboptimal embedding strategy. » [K21] (p. 14) ;
   - la vérification empirique : « Because performance of the average detector does not depend on r, we can pick only a single value of r and plot the false positive rate as N varies. » [K22] (p. 14), et la figure 4 (p. 13, vue en image), où la courbe de la moyenne est plate en r à (B, N) fixés (lu sur la figure).

   **Fait** : la puissance de la statistique somme (ici la moyenne) ne dépend que de (N, B, ψ), pour toute répartition (r, p) du budget entre objets, sans théorème central limite pour l'invariance elle-même. Lois à queues lourdes comprises (p. 7, lemme 1).
   **Non fait** :
   - des valeurs de décalage inégales : « In future work we should consider allowing the Steganographer to vary the amount of data embedded in each object » [K28] (p. 15) ;
   - une répartition adaptative ;
   - un énoncé trajectoriel écrit (il se déduit en une ligne de son modèle, calcul en section 2.1) ;
   - un ordre temporel ou séquentiel : « This suggests the study of sequential embedding and tests. We reserve this topic for future work » [K10] (p. 5) ;
   - une lecture toujours valide ;
   - la loi nulle exacte à n fini : Ker l'ajuste ou l'approche asymptotiquement (p. 7, 12).
2. **L1, « à B fixé, la puissance décroît avec n₀ » — occupée (cas du test à horizon fixe) par Ker et par Bash et collègues.**
   - Ker, pour la statistique moyenne (formule (3), p. 7, lue sur le PDF : pf = 1 − Φ(N^{1/2}·B/k) si ν > 2), puis « To fix the risk of detection, we must » [K20] B ∝ N^{−1/2} (p. 11). Résumé de l'article : « a steganographer should not spread the embedding across all covers, and the secure capacity increases only as the square root of the number of objects. » [K5] (p. 1).
   - Bash et collègues : la loi de la racine carrée, « We present a square root limit on the amount of information transmitted reliably and with low probability of detection (LPD) over additive white Gaussian noise (AWGN) channels. » [A4] (p. 1), y compris pour un détecteur somme (le détecteur de puissance de la réciproque, p. 15-17).
   - La v2 disait « analogue d'échelle ». C'est à corriger : pour la statistique somme elle-même, l'échelle en √N est **énoncée** par Ker (p. 7, 11).
3. **L1, dépendance au seul budget pour un détecteur somme — occupée en partie par Bash et collègues (2012), sous forme de moments.**
   - Le détecteur de puissance est la moyenne des carrés des observations : « but he is oblivious to her signal properties and employs only a simple power detector. » [A10] (p. 15).
   - Sa moyenne et sa variance ne dépendent que de la puissance moyenne du mot de code : formules (15) et (16), p. 16, lues sur le PDF : E[S] = σ² + P_k et Var[S] = (4P_kσ² + 2σ⁴)/n.
   - Les auteurs l'énoncent : « determines its detectability by this detector, and that our result applies to all codewords with power of the same order. » [A12] (p. 16) ; « Note that Willie’s detector is oblivious to any details of Alice’s codebook construction. » [A14] (p. 17).
   - **Fait** : pour tout mot de code (toute répartition de l'énergie dans le temps), la détectabilité par ce détecteur somme est gouvernée par l'énergie totale, avec le seuil en √n (p. 16-17).
   - **Non fait** : l'égalité en loi (seulement l'espérance et la variance, par l'inégalité de Tchebychev), un budget linéaire de décalage sur la moyenne (ici l'énergie), l'adaptatif, le séquentiel, le toujours valide.
4. **L4 — occupée en partie par Ker** pour un seul pas. Le lot de N objets traités en même temps est le cas d'un seul pas avec N agents. L'invariance de la moyenne à la répartition entre objets est l'énoncé de L4 pour T = 1, à horizon fixe. **Non fait** : plusieurs pas, lecture aux frontières de pas, lecture toujours valide.
5. **Toujours non trouvé dans les pièces lues** (lot 8 et voisins) :
   - L2 au seuil exact et à n fini ;
   - L3 : la borne invariante, le coût du report et le prix de la garantie toujours valide ;
   - la comparaison processus e cumulé contre détecteur de rupture ;
   - la non-compensation ;
   - la validité sous dépendance ;
   - l'application aux sondes.

   Ker réserve explicitement le séquentiel ([K10]). C'est une limite reconnue par l'article, pas un trou du champ : ses travaux suivants et la pièce de Trivedi et Chandramouli (2003, séquentielle) ne sont pas lus (section 6).

## 1. Identification des pièces

- **Ker.** Titre imprimé : « Batch Steganography and Pooled Steganalysis » [K1], par « Andrew D. Ker » [K2]. Venue imprimée p. 1 : « J. Camenisch et al. (Eds.): IH 2006, LNCS 4437, pp. 265–281, 2007. » [K3] (Information Hiding 2006, Lecture Notes in Computer Science 4437, Springer, 2007).
  - **Ce n'est pas la pièce « Ker 2007 » que nommait ma v2.** La v2 la nommait d'après 2605.16140 : « A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [R5] (p. 34), pièce que cite aussi Bash et collègues : « A. D. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, Aug. » [A22] (p. 27).
  - La pièce versée est un article antérieur et distinct, publié en actes de conférence, sur le même sujet. La lettre de 2007 ([R5]) reste **non lue**.
- **Bash, Goeckel et Towsley.** Titre imprimé : « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » [A1], par « Boulat A. Bash, Dennis Goeckel, Don Towsley » [A2]. Aucune venue de revue n'est imprimée : « arXiv:1202.6423v4 [cs.IT] 20 Mar 2013 » [A3].
  - 1906.08938 cite la même pièce : « B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” » [R1] ; « Sel. Areas Commun., vol. 31, no. 9, pp. 1921–1930, Sep. 2013. » [R2] (p. 15), dans une revue de l'association des ingénieurs électriciens, 2013.
  - **Ce n'est ni la pièce « 2014 » ni la pièce « 2016 » de ma v2** (« B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” » [R3] ; « B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” » [R4], p. 15). C'est l'**autre** pièce de ma liste : l'origine de la loi de la racine carrée, rangée en priorité 3. Les pièces de 2014 et 2016, sur le guetteur qui ignore l'instant de départ, restent non lues.

## 2. Fiches par article

### 2.1 Ker, « Batch Steganography and Pooled Steganalysis » [K1]

- **Cadre.**
  - Un stéganographe cache une charge totale fixée dans N objets : « We also assume that the Steganographer wants to embed a fixed total amount of secret data » [K7] (p. 4). Il en choisit rN au hasard et en remplit chacun à la proportion p, avec r·p = B : « the Steganographer has no control over the objects themselves, and chooses which to embed in at random. » [K9] (p. 4).
  - Un guetteur fait une analyse groupée, c'est-à-dire qu'il combine des statistiques par objet pour décider si un lot contient de la stéganographie. N est fixé et connu : « we are assuming that the number of cover objects N is fixed from the start, and known to both the Steganographer and Warden. » [K11] (p. 5).
  - Hypothèse de décalage : [K6] (p. 3). Loi des scores sous l'alternative (lu sur le PDF, non contrôlé par programme, p. 5) : f(x) = (1 − r)ψ(x) + rψ(x − p).
  - Métrique : « Fix a detection threshold so that the overall false negative rate (the probability of type-II error for (1)) is 50%; then measure the false positive rate » [K35] (p. 5).
- **Trois détecteurs groupés** : « simple nonparametric tests for median, the average component statistic, and a more sophisticated method based on a generalized maximum likelihood ratio test. » [K12] (p. 6). Plus le test des rangs signés, empirique seulement.
  - **Test des signes.** Formule (2), p. 6, lue sur le PDF : pf = 1 − Φ(2√N·B·(Ψ(p) − ½)/p). L'attaquant concentre : « Therefore the Steganographer will choose p = 1 and r = B, hiding maximal amounts of data in as few cover objects as possible. » [K13] (p. 6).
  - **Moyenne.** Invariance à la répartition, [K14] [K15] (p. 7). Puissance (3), p. 7, lue sur le PDF : 1 − Φ(N^{1/2}B/k) si ν > 2 ; 1 − F_ν(N^{1−1/ν}B/k) si 1 < ν < 2. Et « As long as ν > 1, evidence does accumulate, but the rate at which this happens, as N increases, depends critically on whether ν is greater, or less, than 2. » [K16] (p. 7).
  - **Rapport de vraisemblance généralisé** (lemme 2, p. 9 ; preuve en annexe, p. 17). Pour B petit, « the Steganographer’s best strategy to evade detection by the generalized likelihood ratio test is to take » [K17] p = B, r = 1, c'est-à-dire étaler. Pour B grand, il faut concentrer (p. 10, figure 3) ; la stratégie bascule directement de l'une à l'autre : « spread the payload as thinly as possible for small B » [K18] (p. 10).
  - **Synthèse** : « we see that the Steganographer’s best strategy is to take p=1 and r=B, concentrating all the payload in as few covers as possible. » [K19] (p. 11) ; puis « To fix the risk of detection, we must » [K20] B ∝ N^{−1/2} (lu sur le PDF, p. 11).
- **Chiffres (auteurs).**
  - Le guetteur dispose de 14 000 images : « We used a set of 14000 images, selected for size and image quality out of 20000 on a stock photo CD » [K34] (p. 12).
  - Paramètres de la loi des scores : t de Student, ν = 1,61, λ = 0,00956 (p. 12).
  - Plan d'expérience : B ∈ {0,01 ; 0,003 ; 0,001}, N jusqu'à 4000 ; 10 000 tirages sous l'hypothèse nulle et 1000 sous l'alternative (p. 12-13).
  - Figure 4 : « The false positive detection rate (y-axis) when the false negative rate is 50%, » [K33] (p. 13).
- **Calcul (mien, déduction élémentaire).** Sous l'hypothèse de décalage, la somme des décalages vaut rN·p = BN pour tout (r, p). La moyenne vaut donc exactement Ȳ + B **trajectoire par trajectoire**, et l'invariance en loi de Ker en découle. L'énoncé trajectoriel de L1 est ainsi à une ligne du modèle de Ker. Pour des valeurs inégales et des choix adaptatifs, la même ligne vaut tant que la somme des décalages est fixée : c'est l'apport formel de L1, et il est **élémentaire**.
- **Contre-indices et voisins utiles à L.**
  - **L2.** La meilleure répartition dépend du détecteur : « We emphasise that it cannot apply to every type of pooling algorithm. » [K26] (p. 15). Un détecteur à seuil, voisin du maximum, se comporte comme L2 le dit : « the number of observations greater than 1 is quite sensitive to embedding at p = 1, although worthless for other batch parameters. » [K27] (p. 15). Ker n'étudie pas le maximum au seuil exact. À l'inverse, les tests des signes et du rapport de vraisemblance à grand B **punissent la fragmentation** ([K13], [K19]). Une phrase qui dirait « fragmenter aide toujours l'attaquant, sauf contre la somme » serait donc fausse.
  - **Validité hors hypothèses.** Un biais honnête ruine l'analyse groupée : « the effect is to destroy the reliability of the pooled detectors, flooding them with false positives for any large value of » [K23] (p. 14), car un « systematic bias of b is indistinguishable from a batch Steganographer’s behaviour with p = b and r = 1. » [K24] (p. 15). Le remède proposé est l'étalonnage sur des objets honnêtes du bon type : « If we train the detector first on covers of the right type (effectively removing the bias) then the problem goes away. » [K25] (p. 15). C'est le voisin direct de la garde de L, « faux positifs vérifiés sur épisodes honnêtes entiers » et calibrage sur épisodes honnêtes. Il s'agit d'un biais, pas d'une dépendance.
- **Limites reconnues.**
  - Le séquentiel est réservé ([K10]) ; les valeurs inégales sont renvoyées à plus tard ([K28]) ; et « Finally, we would like to prove a general result on how steganographic capacity increases with » [K29] (p. 15).
  - Ker note : « There seems to be little literature on this problem » [K31] (p. 2). Il nomme une pièce séquentielle : « Trivedi [1] has used sequential hypothesis tests to repeat steganalysis, but only in the context of locating a hidden message embedded sequentially within a single image. » [K30] (p. 2), « Active steganalysis of sequential steganography. » [K32] (p. 16).
- **Résultats trop beaux** : la courbe plate de la moyenne (figure 4) est prédite analytiquement, donc attendue. Aucune réserve de propreté à faire.
- **Verdict d'ensemble pour L : occupée en partie** (L1 et L4, cas d'un seul pas à horizon fixe, valeurs égales, choix non adaptatif) ; voisin et contre-indice pour L2 ; voisin pour la validité hors hypothèses.

### 2.2 Bash, Goeckel et Towsley, « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » [A1]

- **Cadre.**
  - Alice émet n symboles sur un canal à bruit blanc gaussien additif. Willie observe toute la fenêtre : « Willie observes all n of Alice’s channel uses » [A11] (p. 15). Il connaît la loi d'entrée d'Alice dans la partie atteignabilité : « To strengthen the achievability result, we assume that Alice’s channel input distribution, as well as the distribution of the AWGN on the channel between Alice and Willie, are known to Willie. » [A6] (p. 5).
  - La discrétion se mesure par α + β ≥ 1 − ε, c'est-à-dire par la distance en variation totale, majorée par l'inégalité de Pinsker : « Since total variation lower-bounds the error of all hypothesis tests Willie can use, a clever choice of f allows Alice to limit Willie’s detector performance. » [A7] (p. 6).
- **Résultat : la loi de la racine carrée.** On peut transmettre O(√n) bits si une borne inférieure du bruit du guetteur est connue, o(√n) sinon. Au-delà de ω(√n) bits, Alice est détectée ou Bob décode mal. Théorème p. 3, théorèmes 1.1, 1.2 et 2, formules lues sur le PDF.
  - **Atteignabilité** (p. 7-13). VT ≤ (P_f/(2σ²))·√(n/2) (formule (4), p. 9, lue sur le PDF). Elle repose sur « That relative entropy is locally quadratic is well-known » [A8] (p. 8).
  - **Réciproque** (p. 14-18). Elle tient avec un seul **détecteur somme**, la moyenne des carrés : [A10] (p. 15). Formules (13) à (17), p. 15-16, lues sur le PDF. Puis [A12] (p. 16), [A14] (p. 17), « Thus, with enough observations, Willie can detect with arbitrarily low error probability Alice’s codewords with the average symbol » [A15] (p. 17), et « Thus, Alice cannot break the square root law using an arbitrarily high transmission rate and retransmissions while keeping the power below Willie’s detection threshold. » [A16] (p. 18).
  - Lien avec la stéganographie : « The square root law of steganography in the passive warden environment states that » [A5] (p. 2) ; « The square root law in steganography has the same form as our square root law because both laws follow from the property that relative entropy is locally quadratic » [A9] (p. 14).
- **Calcul (mien).** Sous l'alternative, n·S/σ² suit une loi du khi-deux décentrée, de paramètre de décentrage n·P_k/σ². Sa loi ne dépend donc que de l'énergie totale, et pas de sa répartition dans le temps. L'article ne l'écrit pas : il s'arrête aux deux premiers moments.
- **Répartition dans le temps.**
  - Appendice B : « First, Alice and Bob randomly select the symbol periods that they will use for their transmission by flipping a biased coin n times » [A20] (p. 24). Les auteurs montrent que la borne sur la variation totale ne dépend que du produit τa² : « This product is the average symbol power used by Alice. » [A21] (p. 24 ; formule (41), lue sur le PDF).
  - C'est une **borne** invariante, pour deux allocations particulières : pleine (τ = 1) ou clairsemée et aléatoire (τ petit). Ce n'est pas une égalité.
- **Instant de départ** : aucun. Willie observe la fenêtre entière et connue. La seule discussion d'a priori porte sur l'état « émet ou n'émet pas » : « The proofs of achievability (Theorems 1.1 and 1.2) in Section III assume that Willie has no prior knowledge on whether Alice transmits or not. » [A18] (p. 20). Rien sur le calendrier : la v2 renvoyait pour cela aux pièces de 2014 et 2016, qui ne sont pas celle-ci.
- **Limites et perspectives** : « The impact of dynamism in the network should also be examined » [A19] (p. 21) ; la détection cyclostationnaire est laissée à plus tard (p. 21) ; « Thus, spread spectrum systems are also limited by the square root law. » [A17] (p. 19).
- **Venue** : prépublication, version 4, mars 2013 ([A3]) ; parution en revue, 2013, d'après [R2].
- **Verdict d'ensemble pour L : occupée en partie** pour L1 (échelle en √n pour un détecteur somme ; détectabilité par ce détecteur gouvernée par le seul budget total, en moments) ; ne touche pas les autres composantes.

## 3. Table composante × article (les deux voisins ; les verdicts du lot 8 restent ceux de la v2)

| composante de L | Ker (2006) | Bash, Goeckel et Towsley (2012) |
|---|---|---|
| L1 — égalité en loi de la statistique somme sous budget fixé, toute répartition | **occupée en partie** : invariance en loi de la moyenne à la répartition (r, p), modèle de décalage, p. 3, 4, 7, 14, figure 4 [K6, K7, K8, K14, K15, K21, K22] ; non fait : valeurs inégales [K28], adaptatif, ordre temporel [K10], toujours valide, énoncé trajectoriel écrit (déduction en une ligne, calcul) | **occupée en partie** : moyenne et variance du détecteur somme fonctions de la seule énergie totale, pour tout mot de code, p. 16-17 [A12, A14] ; non fait : égalité en loi (calcul : khi-deux décentré), budget linéaire de moyenne, adaptatif, séquentiel |
| L1 — décroissance en n₀ à B fixé | **occupée** (horizon fixe) : B ∝ N^{−1/2} pour la moyenne, p. 7, 11 [K16, K20] ; [K5] | **occupée** (horizon fixe) : loi de la racine carrée, y compris pour le détecteur somme, p. 1, 15-18 [A4, A15, A16] |
| L4 — répartition entre agents au même pas | **occupée en partie** : cas d'un seul pas (N objets en même temps) ; non fait : plusieurs pas, frontières de pas, toujours valide | ne touche pas (un seul émetteur) |
| L2 — max au seuil exact, n fini, plancher | voisin et contre-indice : le meilleur choix dépend du détecteur [K26] ; un détecteur à seuil est sensible à la concentration et inutile sinon [K27] ; les signes et le rapport de vraisemblance à grand B punissent la fragmentation [K13, K19] ; maximum non étudié | ne touche pas |
| L3 — calendrier, borne invariante, report, prix du toujours valide | ne touche pas (séquentiel réservé, p. 5 [K10]) | ne touche pas (fenêtre entière observée [A11]) |
| Processus e cumulé contre détecteur de rupture | ne touche pas | ne touche pas |
| Non-compensation | ne touche pas | ne touche pas |
| Validité hors hypothèses et sous dépendance | voisin : un biais honnête inonde l'analyse groupée de fausses alarmes ; remède : étalonnage sur objets honnêtes du bon type, p. 14-15 [K23, K24, K25] ; aucune dépendance | ne touche pas (bruit indépendant) |
| Scores de sondes internes | ne touche pas | ne touche pas |

## 4. Verdict d'ensemble sur L (table fermée)

**Occupé en partie.** La case est inchangée, mais son **contenu change**. Jusqu'à la v2, l'occupation ne portait que sur le cœur classique, non revendiqué. Désormais, **deux composantes revendiquées sont occupées en partie** :
- L1 : l'invariance de la statistique somme à la répartition, à budget fixé, et son échelle en √n₀ (Ker 2006 ; Bash et collègues 2012) ;
- L4, dans le cas d'un seul pas (Ker 2006).

La v2 écrivait « non trouvé dans les trois pièces lues » pour l'égalité de L1 et pour L4. C'est à lire désormais : « occupé en partie, dans le cas par lots à horizon fixe ».

## 5. Ce qui reste revendicable (formulation)

« Restent revendicables :
- l'extension de l'invariance de la statistique somme, connue pour la stéganographie par lots à valeurs égales, choix aléatoire et horizon fixe (Ker 2006), à des décalages **inégaux et adaptatifs, ordonnés dans le temps**, avec un énoncé trajectoriel. L'apport formel est élémentaire, puisqu'il se déduit en une ligne du modèle de décalage ;
- la **couche séquentielle et toujours valide** :
  - L4 sur plusieurs pas, lu aux frontières de pas ;
  - L3 : borne inférieure invariante fonction de (B, n₀), coût du report et prix de la garantie toujours valide, chiffrés ;
  - la comparaison processus e cumulé contre détecteur de rupture pour l'alarme avant le dommage ;
- L2 au seuil exact et à n fini ;
- la validité sous dépendance ;
- la mesure sur scores de sondes internes.

Se citent comme publiés :
- l'invariance de la moyenne à la répartition et l'échelle en √N du détecteur somme (Ker 2006, p. 7, 11, 14) ;
- la loi de la racine carrée, y compris pour un détecteur de puissance (Bash, Goeckel et Towsley 2012) ;
- la dépendance au détecteur de la meilleure répartition (Ker 2006) ;
- le danger d'un biais honnête pour l'analyse groupée et son remède par étalonnage (Ker 2006). »

**Réserve (règle R8).** Ker réserve le séquentiel et les valeurs inégales comme travaux futurs. La zone qui reste est donc **séduisante**, et elle a pu être occupée depuis par Ker ou d'autres (section 6). Elle se vérifie plus durement avant toute revendication.

## 6. Ce qu'une phrase publique déclarant L ne doit pas affirmer (ajouts à la liste de la v2)

Je ne rédige pas cette phrase : ce rôle m'est exclu. Elle ne doit pas affirmer :
1. que l'invariance de la statistique somme (ou moyenne) à la répartition du budget, à budget total fixé, est nouvelle : Ker l'énonce pour l'analyse groupée ([K14], [K15], [K21], p. 7 et 14) ;
2. que l'échelle en √n₀ de cette statistique n'est qu'un « analogue » de la loi de la racine carrée : elle est énoncée pour la moyenne ([K20], p. 11), et la loi elle-même est démontrée avec un détecteur somme ([A10], [A12], p. 15-16). Ceci corrige la ligne 1 de la v2 ;
3. que L4 (répartition entre agents au même pas) est sans précédent : le cas d'un seul pas à horizon fixe est celui de Ker ;
4. que « fragmenter aide l'attaquant » en général, ou contre tout détecteur autre que la somme : contre le test des signes et le rapport de vraisemblance à grand budget, concentrer est meilleur ([K13], [K19]) ;
5. que la nécessité d'étalonner sur des données honnêtes entières est un constat du programme : un biais honnête indiscernable d'un sabotage étalé, et son remède par étalonnage, sont chez Ker ([K24], [K25]) ;
6. que la zone « séquentiel et toujours valide » est libre : non trouvée dans les pièces lues, et réservée par Ker en 2006 ; ses travaux suivants ne sont pas lus.

Les lignes de la v2 restent valables, sauf la ligne 1, corrigée par le point 2 ci-dessus.

## 7. Effet sur la colonne « déclarable » de L

**Elle reste à « non ».** Les motifs sont plus nombreux qu'avant :
- la réserve M4 n'est pas levée : la pièce de Huang, Wang et Poor (« K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” » [R6]), celle de 2014 ([R3]) et celle d'Arumugam et Bloch (« K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” » [R7]) ne sont pas versées ;
- la pièce « Ker 2007 » ([R5], [A22]) n'est pas celle qui a été versée, et reste non lue ;
- deux composantes revendiquées (L1, L4) sont désormais **occupées en partie** : toute déclaration doit d'abord resserrer la revendication sur la couche séquentielle et toujours valide (section 5), puis citer Ker 2006 et Bash et collègues 2012.

Le resserrement de la revendication est une décision du directeur ; je ne la prends pas.

## 8. Voisins nommés dans les pièces et non lus

| priorité | pièce (titre imprimé) | où elle est nommée | composantes concernées |
|---|---|---|---|
| 1 | Ker 2007, « A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [R5] | 2605.16140 p. 34 ; Bash et collègues p. 27 | L1, L4 (capacité d'un lot, loi générale en N, que Ker 2006 souhaitait prouver [K29]) |
| 1 | Trivedi et Chandramouli 2003, « Active steganalysis of sequential steganography. » [K32] | Ker p. 2, 16 | L3 et la couche séquentielle (stéganalyse séquentielle, dans une seule image d'après Ker [K30]) |
| 1 | Huang, Wang et Poor 2021 [R6] ; Bash et collègues 2014 [R3] et 2016 [R4] ; Arumugam et Bloch 2016 [R7] | 2605.16140 p. 35 ; 1906.08938 p. 15 | L3, sécurité avant le dommage, calendrier ; réserve M4 |
| 2 | Filler, Ker et Fridrich 2009, « The square root law of steganographic capacity for markov covers » [A23] | Bash et collègues p. 27 | L1 (loi de la racine carrée pour des couvertures dépendantes de Markov : lien avec la validité sous dépendance) |
| 3 | Ker 2009, « The square root law requires a linear key » [A24] ; Filler et Fridrich 2009, « Fisher information determines capacity of » [A25] | Bash et collègues p. 27 | échelle, information de Fisher |

## 9. Ce que je n'ai pas fait

- Je n'ai lu aucune pièce non versée. Ce que je dis des pièces de la section 8 se limite à leur titre imprimé et aux phrases des pièces lues.
- Je n'ai pas refait les dérivées de l'annexe A de Bash et collègues, ni la preuve du lemme 2 de Ker au-delà de sa lecture.
- Seule la figure 4 de Ker a été vue en image. Les autres figures sont lues par leur légende.
- Mes deux calculs sont des déductions élémentaires sur les modèles des articles (section 2) : je n'ai lancé aucun programme numérique pour ce rapport.

## 10. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — citations contrôlées (`citations-L-voisins-v1.json`, dans l'archive)

| id | n° JSON | pièce | page | citation exacte |
|---|---|---|---|---|
| K1 | 1 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | Batch Steganography and Pooled Steganalysis |
| K2 | 2 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | Andrew D. Ker |
| K3 | 3 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | J. Camenisch et al. (Eds.): IH 2006, LNCS 4437, pp. 265–281, 2007. |
| K4 | 4 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | and the dual problem of hiding information securely when spreading across a batch of covers. |
| K5 | 5 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | a steganographer should not spread the embedding across all covers, and the secure capacity increases only as the square root of the number of objects. |
| K6 | 6 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 3 | the distribution of the detector response only depends on p in the form of a shift, so that the (additive) estimation error is independent of the true value. |
| K7 | 7 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | We also assume that the Steganographer wants to embed a fixed total amount of secret data |
| K8 | 8 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | Within this range, he can vary r or p and should do so to try to minimize the chance of overall detection. |
| K9 | 9 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | the Steganographer has no control over the objects themselves, and chooses which to embed in at random. |
| K10 | 10 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | This suggests the study of sequential embedding and tests. We reserve this topic for future work |
| K11 | 11 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | we are assuming that the number of cover objects N is fixed from the start, and known to both the Steganographer and Warden. |
| K12 | 12 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 6 | simple nonparametric tests for median, the average component statistic, and a more sophisticated method based on a generalized maximum likelihood ratio test. |
| K13 | 13 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 6 | Therefore the Steganographer will choose p = 1 and r = B, hiding maximal amounts of data in as few cover objects as possible. |
| K14 | 14 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | the distributional shape of |
| K15 | 15 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B. |
| K16 | 16 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | As long as ν > 1, evidence does accumulate, but the rate at which this happens, as N increases, depends critically on whether ν is greater, or less, than 2. |
| K17 | 17 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 9 | the Steganographer’s best strategy to evade detection by the generalized likelihood ratio test is to take |
| K18 | 18 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 10 | spread the payload as thinly as possible for small B |
| K19 | 19 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | we see that the Steganographer’s best strategy is to take p=1 and r=B, concentrating all the payload in as few covers as possible. |
| K20 | 20 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | To fix the risk of detection, we must |
| K21 | 21 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 14 | Also, the average method cannot punish the Steganographer for using a suboptimal embedding strategy. |
| K22 | 22 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 14 | Because performance of the average detector does not depend on r, we can pick only a single value of r and plot the false positive rate as N varies. |
| K23 | 23 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 14 | the effect is to destroy the reliability of the pooled detectors, flooding them with false positives for any large value of |
| K24 | 24 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | systematic bias of b is indistinguishable from a batch Steganographer’s behaviour with p = b and r = 1. |
| K25 | 25 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | If we train the detector first on covers of the right type (effectively removing the bias) then the problem goes away. |
| K26 | 26 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | We emphasise that it cannot apply to every type of pooling algorithm. |
| K27 | 27 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | the number of observations greater than 1 is quite sensitive to embedding at p = 1, although worthless for other batch parameters. |
| K28 | 28 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | In future work we should consider allowing the Steganographer to vary the amount of data embedded in each object |
| K29 | 29 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | Finally, we would like to prove a general result on how steganographic capacity increases with |
| K30 | 30 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 2 | Trivedi [1] has used sequential hypothesis tests to repeat steganalysis, but only in the context of locating a hidden message embedded sequentially within a single image. |
| K31 | 31 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 2 | There seems to be little literature on this problem |
| K32 | 32 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 16 | Active steganalysis of sequential steganography. |
| K33 | 33 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 13 | The false positive detection rate (y-axis) when the false negative rate is 50%, |
| K34 | 34 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 12 | We used a set of 14000 images, selected for size and image quality out of 20000 on a stock photo CD |
| K35 | 35 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | Fix a detection threshold so that the overall false negative rate (the probability of type-II error for (1)) is 50%; then measure the false positive rate |
| A1 | 36 | `1202.6423v4.pdf` | 1 | Limits of Reliable Communication with Low Probability of Detection on AWGN Channels |
| A2 | 37 | `1202.6423v4.pdf` | 1 | Boulat A. Bash, Dennis Goeckel, Don Towsley |
| A3 | 38 | `1202.6423v4.pdf` | 1 | arXiv:1202.6423v4 [cs.IT] 20 Mar 2013 |
| A4 | 39 | `1202.6423v4.pdf` | 1 | We present a square root limit on the amount of information transmitted reliably and with low probability of detection (LPD) over additive white Gaussian noise (AWGN) channels. |
| A5 | 40 | `1202.6423v4.pdf` | 2 | The square root law of steganography in the passive warden environment states that |
| A6 | 41 | `1202.6423v4.pdf` | 5 | To strengthen the achievability result, we assume that Alice’s channel input distribution, as well as the distribution of the AWGN on the channel between Alice and Willie, are known to Willie. |
| A7 | 42 | `1202.6423v4.pdf` | 6 | Since total variation lower-bounds the error of all hypothesis tests Willie can use, a clever choice of f allows Alice to limit Willie’s detector performance. |
| A8 | 43 | `1202.6423v4.pdf` | 8 | That relative entropy is locally quadratic is well-known |
| A9 | 44 | `1202.6423v4.pdf` | 14 | The square root law in steganography has the same form as our square root law because both laws follow from the property that relative entropy is locally quadratic |
| A10 | 45 | `1202.6423v4.pdf` | 15 | but he is oblivious to her signal properties and employs only a simple power detector. |
| A11 | 46 | `1202.6423v4.pdf` | 15 | Willie observes all n of Alice’s channel uses |
| A12 | 47 | `1202.6423v4.pdf` | 16 | determines its detectability by this detector, and that our result applies to all codewords with power of the same order. |
| A13 | 48 | `1202.6423v4.pdf` | 16 | The variance of Willie’s test statistic (16) is computed by adding the variances conditioned on |
| A14 | 49 | `1202.6423v4.pdf` | 17 | Note that Willie’s detector is oblivious to any details of Alice’s codebook construction. |
| A15 | 50 | `1202.6423v4.pdf` | 17 | Thus, with enough observations, Willie can detect with arbitrarily low error probability Alice’s codewords with the average symbol |
| A16 | 51 | `1202.6423v4.pdf` | 18 | Thus, Alice cannot break the square root law using an arbitrarily high transmission rate and retransmissions while keeping the power below Willie’s detection threshold. |
| A17 | 52 | `1202.6423v4.pdf` | 19 | Thus, spread spectrum systems are also limited by the square root law. |
| A18 | 53 | `1202.6423v4.pdf` | 20 | The proofs of achievability (Theorems 1.1 and 1.2) in Section III assume that Willie has no prior knowledge on whether Alice transmits or not. |
| A19 | 54 | `1202.6423v4.pdf` | 21 | The impact of dynamism in the network should also be examined |
| A20 | 55 | `1202.6423v4.pdf` | 24 | First, Alice and Bob randomly select the symbol periods that they will use for their transmission by flipping a biased coin n times |
| A21 | 56 | `1202.6423v4.pdf` | 24 | This product is the average symbol power used by Alice. |
| A22 | 57 | `1202.6423v4.pdf` | 27 | A. D. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, Aug. |
| A23 | 58 | `1202.6423v4.pdf` | 27 | The square root law of steganographic capacity for markov covers |
| A24 | 59 | `1202.6423v4.pdf` | 27 | The square root law requires a linear key |
| A25 | 60 | `1202.6423v4.pdf` | 27 | Fisher information determines capacity of |
| R1 | 61 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” |
| R2 | 62 | `1906.08938v2.pdf` | 15 | Sel. Areas Commun., vol. 31, no. 9, pp. 1921–1930, Sep. 2013. |
| R3 | 63 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” |
| R4 | 64 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” |
| R5 | 65 | `2605.16140v1.pdf` | 34 | A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. |
| R6 | 66 | `2605.16140v1.pdf` | 35 | K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” |
| R7 | 67 | `1906.08938v2.pdf` | 15 | K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” |
