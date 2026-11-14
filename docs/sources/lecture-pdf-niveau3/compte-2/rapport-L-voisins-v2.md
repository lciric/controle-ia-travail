# Antériorité du lemme d'additivité « L » — deux voisins versés (Ker ; Bash, Goeckel et Towsley) — v2

- Version 1 écrite le 2026-11-14 à 06:42 UTC ; reprise pour la version 2 commencée le 2026-11-14 à 06:53:23 UTC ; ce fichier écrit le 2026-11-14 06:57:04 UTC. Heures relevées par `date -u`, la dernière dans la commande qui écrit ce fichier.
- Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.
- **Rapport remplacé** : `rapport-L-voisins-v1.md`, sha256 `cb5829539e3fba66e6916aebe79fa1a8a4e3bd320d2754311581fdf43ca2fbde`, archivé sans modification. Son archive : `fichiers-de-travail-L-voisins-v1.tar`, `ee87065d282c8b43d7329e356ac7d71f894aa3b48928dd5f6d7e6f210ec17023`.
- **Contre-lecture intégrée** :
  - `contre-lecture-rapport-L-voisins-v1.md`, `58e7ad2d5cba602c1c79259340a625af06b8bf8a5a95d343719259c91fcee929` ;
  - son archive `fichiers-de-travail-contre-lecture-L-voisins-v1.tar`, `23fd5efecccba85f481d37785adf720298bc4c81e947f60ee2d0e21c7047ed53` ;
  - empreintes vérifiées, égales aux valeurs attendues ; archive extraite dans un sous-dossier neuf ;
  - verdict de la contre-lecture : « tient avec corrections », six constats majeurs (A à F), six mineurs (G à L), aucun bloquant.
- Rapports antérieurs sur L (non modifiés) : `rapport-L-lot8-v1.md` (`130283ad…`) et `rapport-L-lot8-v2.md` (`8d9f2654…`).
- Consigne : `consigne-lecteur-compte-2-v1.md` (`cb0623c4…`). Avant d'écrire, un `ls` du seul dossier `compte-2/` a montré qu'il n'existait ni `rapport-L-voisins-v2.md` ni `fichiers-de-travail-L-voisins-v2.tar`.
- Pièces, empreintes vérifiées contre leur compagnon `.sha256` :
  - `ker-2006-batch-steganography-pooled-steganalysis.pdf` (17 pages) : `a6ab71a257034976636aad130fb9a7715a45d3dd06cb69cf046475f8f231a2aa`
  - `1202.6423v4.pdf` (27 pages) : `ab6caeadb380ec322fb6d9400cde5aa04d6e32ddbb55a869c7efd6f3eebd1c49`
  - renvois bibliographiques seulement : `1906.08938v2.pdf` p. 15 (`3fbaedd9…`) et `2605.16140v1.pdf` p. 34-35 (`1f70a328…`).
- Citations contrôlées par programme : **92 citations, 0 échec**. Script `controle_citations_voisins_v1.py`, inchangé. Les citations sont dans `citations-L-voisins-v2.json`, qui figure dans l'archive seulement (sha256 `8abf9f29a85da5ce9bb8a51599c4f85d461dc4ea0008a831d4e4008eef4c873b`).
  - Identifiants : K1 à K35, A1 à A25 et R1 à R7 sont ceux de la v1 ; K36 à K50, A26 à A36 sont nouveaux.
  - Tout extrait anglais entre « », titres compris, est une citation contrôlée.
  - Les formules sont « lues sur le PDF, non contrôlées par programme ».
  - Nature des chiffres : « auteurs », « figure » ou « calcul ».

## Fichiers lus et étendue

1. La consigne du compte 2, en entier (lue en v1).
2. Ker : 17 pages, lues ligne à ligne en texte brut en v1. En v2, j'ai relu les p. 3 à 7 et 11 à 16, ainsi que la p. 13 (figure 4) en image, déjà vue en v1.
3. Bash et collègues : 27 pages, lues ligne à ligne en v1. En v2, j'ai relu les p. 14 à 18, ainsi que les p. 2, 8, 21, 26 et 27 pour les passages cités.
4. La contre-lecture, en entier. Dans son archive, j'ai lu le script `calcul_detecteur_puissance_v1.py` et sa sortie, sans les exécuter. J'ai refait le calcul en forme fermée (section 2.2).
5. `1906.08938v2.pdf` p. 15 et `2605.16140v1.pdf` p. 34-35, par leur texte déjà extrait.

Aucune ouverture fautive, aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucune suppression. Aucun refus.

## 0. En tête : occupations

1. **Une seule composante revendiquée est occupée en partie : le cœur de L1, par Ker.** (La v1 en comptait deux et y ajoutait Bash et collègues : constats A et B corrigés.)
   - Le modèle est un pur décalage : « the distribution of the detector response only depends on p in the form of a shift, so that the (additive) estimation error is independent of the true value. » [K6] (p. 3).
   - La charge totale est fixée : « We also assume that the Steganographer wants to embed a fixed total amount of secret data » [K7] (p. 4). Elle est répartie sur rN objets de même capacité (« all cover objects have the same capacity » [K49]), à la proportion p chacun, avec r·p = B. Les objets sont choisis au hasard : « the Steganographer has no control over the objects themselves, and chooses which to embed in at random. » [K9] (p. 4).
   - L'énoncé tient en une phrase, donnée comme évidente et sans preuve : « It is immediate that » [K36] … « the distributional shape of » [K14] … « does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B. » [K15] (p. 7). Il est repris p. 14 : « Also, the average method cannot punish the Steganographer for using a suboptimal embedding strategy. » [K21] ; « Because performance of the average detector does not depend on r, we can pick only a single value of r and plot the false positive rate as N varies. » [K22].
   - **Fait** : la loi de la statistique moyenne (c'est-à-dire la somme, à un facteur 1/N près) ne dépend pas de la répartition du budget. Cela vaut à N fini et pour toute loi des scores. La répartition est restreinte à deux valeurs (0 ou p), aléatoire et non adaptative.
   - **Non fait** :
     - valeurs inégales : « In future work we should consider allowing the Steganographer to vary the amount of data embedded in each object » [K28] (p. 15) ;
     - répartition adaptative ;
     - énoncé trajectoriel écrit (il se déduit en une ligne : calcul confirmé par le contre-lecteur) ;
     - fonction de puissance exacte à n fini ;
     - tout ordre temporel ou séquentiel : « This suggests the study of sequential embedding and tests. We reserve this topic for future work » [K10] (p. 5).
2. **L1, « à budget fixé, la puissance décroît avec n₀ » : occupée pour un test à horizon fixe, sous forme asymptotique, par Ker seul.**
   - Ce n'est vrai qu'après un changement d'échelle d'une ligne : le B de Ker est une proportion par objet, « is the proportionate bandwidth. » [K38] (p. 4), et la charge totale est « The total amount of data hidden by the Steganographer is proportional to » [K39] B·N (p. 11). Le budget total de L vaut donc N fois le B de Ker (constat D).
   - Ker imprime la forme « capacité » (« To fix the risk of detection, we must » [K20] B ∝ N^{−1/2}, p. 11, lu sur le PDF). Il ne dit jamais « à charge totale fixée, la détection décroît avec N ».
   - L'exposant dépend de l'indice de queue ν (constat E) :
     - √N si la variance est finie (ν > 2) ;
     - N^{1−1/ν} si 1 < ν < 2 : « in this case the discrimination of the average statistic increases only as a power law » [K40] (p. 11).
   - Les données de Ker sont dans ce second cas : « is well modelled by a t-distribution with ν = 1.61 » [K41] (p. 12).
3. **L4 : voisin (constat A corrigé).** Chez Ker, il n'y a ni agents, ni pas, ni lecture aux frontières de pas, ni garantie toujours valide : « we believe that the practice of sequential steganography and steganalysis may be rather different from the fixed-size batch problems studied here. » [K48] (p. 5). Son lot de N objets ne donne que le cas T = 1, où L4 et L1 sont une seule et même proposition.
4. **Bash, Goeckel et Towsley : voisin**, pour l'invariance comme pour l'échelle (constats B et C corrigés ; motif précisé en 2.2).
5. **Non trouvé dans les pièces lues** :
   - L2 au seuil exact et à n fini ;
   - L3 : borne invariante, coût du report, prix de la garantie toujours valide ;
   - la comparaison processus e cumulé contre détecteur de rupture ;
   - la non-compensation ;
   - la validité sous dépendance ;
   - l'application aux sondes internes.

   Ker réserve en toutes lettres le séquentiel ([K10]), les valeurs inégales ([K28]) et le comptage à seuil (« for example the pooling method of counting observations greater than some threshold » [K43], écarté « because this leads to a game theoretical setup which can be intractable. » [K44], p. 15). Ce sont des limites reconnues, pas un trou du champ.

## 1. Suite donnée à la contre-lecture

Les pages en cause ont été relues : Ker p. 3-7 et 11-16, Bash et collègues p. 14-18. Le calcul du constat B a été refait en forme fermée.

| constat | gravité | décision | où dans la v2 | motif |
|---|---|---|---|---|
| A — L4 compté deux fois (même phrase de Ker, cas T = 1) | majeur | corrigé | sections 0 (point 3), 3, 4, 5, 6 | Ker n'a ni pas ni lecture aux frontières ni garantie toujours valide ([K48], p. 5) ; à T = 1, L4 est L1 : une seule composante revendiquée est occupée en partie. |
| B — Bash et collègues : invariance sous budget d'énergie, voisin | majeur | corrigé | sections 0 (point 4), 2.2, 3 | Verdict ramené à « voisin ». Mon calcul en forme fermée confirme les chiffres du contre-lecteur. Je retiens un autre motif principal : résultat d'ordre de grandeur par Tchebychev ([A26], p. 16), propre au bruit gaussien, jamais énoncé comme invariance à la répartition. Dans l'espace des scores y², le budget est linéaire et le détecteur est une somme (section 2.2). |
| C — Bash et collègues : décroissance en n₀, « analogue d'échelle » | majeur | corrigé | sections 0 (point 2), 2.2, 3, 6 | Ramené à « voisin ». Pour le détecteur de puissance, c'est la même échelle, en ordre de grandeur et sur le score y² (p. 16-17). Ce n'est pas l'énoncé de L1 sur la puissance d'un test de la somme. |
| D — le B de Ker est une proportion par objet | majeur | corrigé | sections 0 (point 2), 2.1, 3 | « is the proportionate bandwidth. » [K38] (p. 4), et la charge totale est proportionnelle à B·N ([K39], p. 11). À B de Ker fixé, la détection s'améliore avec N ; l'énoncé de L s'obtient en posant B(L) = N·B(Ker). |
| E — l'échelle en racine exige ν > 2 | majeur | corrigé | sections 0 (point 2), 2.1, 3, 6 | Formule (3), p. 7, et [K40], p. 11 : l'exposant est N^{1−1/ν} pour 1 < ν < 2, et les données de Ker ont ν = 1,61 ([K41], p. 12). |
| F — section 5 trop généreuse | majeur | corrigé | sections 5, 7 | Le cœur de L1 est imprimé chez Ker ; valeurs inégales, adaptatif et trajectoire tiennent en une ligne de calcul ; l'ordre temporel n'ajoute rien à une somme terminale. L1 s'énonce comme une remarque avec renvoi à Ker. |
| G — comptage à seuil nommé puis écarté par Ker | mineur | corrigé | sections 0 (point 5), 2.1, 3 | [K43] et [K44] (p. 15) : limite reconnue, zone à vérifier plus durement dans les travaux suivants de Ker. |
| H — piste de dépendance entre objets chez Ker | mineur | corrigé | sections 2.1, 3, 8 | « If we may assume that all, or most, of the steganography is performed using the same secret key » [K46] … « there could be an amplification of the statistical traces, which we might exploit. » [K45] (p. 16) : il n'y a aucun résultat, mais une piste nommée. Elle est à transmettre aussi au papier B (co-élévation entre copies), qui est hors de mon mandat. |
| I — années et versions | mineur | corrigé | sections 1, 3, 8 | Ker : atelier de 2006, actes parus en 2007 (« Springer-Verlag Berlin Heidelberg 2007 » [K47]) ; Bash et collègues : version 4 de mars 2013 ([A3]) ; la version de revue de septembre 2013 n'est pas lue. |
| J — trois voisins nommés manquants | mineur | corrigé | section 8 | Ker 2010 (« The square root law does not require a linear key » [A30]) ; Che et collègues (« Reliable deniable communication: Hiding messages in noise » [A31]) ; le livre de Fridrich (« Steganography in Digital Media: Principles, Algorithms, and Applications » [A35]), chapitre 13, cité pour « symbols in covertext of size n may safely be modified » [A32] (p. 2). |
| K — coquille de Ker ; hypothèse de décalage hors domaine | mineur | corrigé | section 2.1 | « under the null hypothesis is approximately B. » [K37] (p. 7) devrait se lire sous l'alternative. L'hypothèse de décalage échoue aux fortes charges, « there is both a shape change and a negative bias for higher rates » [K42] (p. 4), alors que la figure 4 va jusqu'à p = 1 : la platitude à forte charge est empirique, hors de l'hypothèse. |
| L — journal v1 incomplet | mineur | corrigé | journal v2 (archive) ; « Fichiers lus » | Le journal v1 n'avait pas consigné la vue en image de la p. 13 ; c'est noté dans le journal v2. Le journal v1, scellé, ne se réécrit pas. |

Les décisions ne suivent pas la contre-lecture par déférence. Pour B, j'adopte le verdict mais pas tout le motif. L'argument « budget d'énergie, non linéaire ; somme de carrés, non somme » dépend de l'espace où l'on lit le score. Si le score est y², le budget d'Alice (la puissance moyenne) est le décalage moyen total de ces scores, et le détecteur de puissance est leur somme. Ce qui écarte l'occupation, c'est donc l'ordre de grandeur par Tchebychev et le cadre gaussien.

## 2. Fiches par article

### 2.1 Ker — « Batch Steganography and Pooled Steganalysis » [K1], par « Andrew D. Ker » [K2] (atelier de 2006, actes de 2007)

- **Venue** imprimée p. 1 : « J. Camenisch et al. (Eds.): IH 2006, LNCS 4437, pp. 265–281, 2007. » [K3] ; « Springer-Verlag Berlin Heidelberg 2007 » [K47]. Ce n'est pas la lettre de 2007 citée par 2605.16140 (« A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [R5], p. 34) et par Bash et collègues (« A. D. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, Aug. » [A22], p. 27). Cette lettre reste non lue.
- **Cadre** :
  - un stéganographe répartit une charge totale fixée sur N objets ([K7], [K9], [K49], p. 4) ;
  - B est une proportion par objet ([K38], p. 4) ;
  - modèle de pur décalage ([K6], p. 3), objets indépendants (« Suppose that all Xi are independent and identically distributed » [K50], p. 7) ;
  - un guetteur fait une analyse groupée sur N objets fixés et connus (« we are assuming that the number of cover objects N is fixed from the start, and known to both the Steganographer and Warden. » [K11], p. 5) ;
  - métrique : « Fix a detection threshold so that the overall false negative rate (the probability of type-II error for (1)) is 50%; then measure the false positive rate » [K35] (p. 5).
- **Résultats** (formules lues sur le PDF, non contrôlées par programme) :
  - **Test des signes** : pf = 1 − Φ(2√N·B·(Ψ(p) − ½)/p) (2), p. 6 ; l'attaquant concentre : « Therefore the Steganographer will choose p = 1 and r = B, hiding maximal amounts of data in as few cover objects as possible. » [K13].
  - **Moyenne** : sa loi est indépendante de (r, p) ([K14], [K15], p. 7). Puissance (3), p. 7 : 1 − Φ(N^{1/2}B/k) si ν > 2 ; 1 − F_ν(N^{1−1/ν}B/k) si 1 < ν < 2 ; et « As long as ν > 1, evidence does accumulate, but the rate at which this happens, as N increases, depends critically on whether ν is greater, or less, than 2. » [K16].
  - **Rapport de vraisemblance généralisé** (lemme 2, p. 9) : « the Steganographer’s best strategy to evade detection by the generalized likelihood ratio test is to take » [K17] p = B, r = 1 (étaler) si B est petit ; concentrer si B est grand (p. 10 ; « spread the payload as thinly as possible for small B » [K18]).
  - **Synthèse** : « we see that the Steganographer’s best strategy is to take p=1 and r=B, concentrating all the payload in as few covers as possible. » [K19] (p. 11), puis [K20] (p. 11), avec les deux exposants ([K40]).
- **Chiffres (auteurs)** :
  - 14 000 images (« We used a set of 14000 images, selected for size and image quality out of 20000 on a stock photo CD » [K34], p. 12) ;
  - loi des scores : t de Student, ν = 1,61, λ = 0,00956 ([K41], p. 12) ;
  - B ∈ {0,01 ; 0,003 ; 0,001}, N jusqu'à 4000 (p. 12-13) ;
  - figure 4 : « The false positive detection rate (y-axis) when the false negative rate is 50%, » [K33] (p. 13).
- **Changement d'échelle (calcul)** : charge totale T = B·N. À T fixé, et si ν > 2, la puissance de la moyenne vaut 1 − Φ(T/(k√N)), ce qui décroît avec N : c'est la forme de L1. Si 1 < ν < 2, elle vaut 1 − F_ν(T·N^{−1/ν}/k).
- **Trajectoire (calcul, confirmé par le contre-lecteur)** : avec exactement rN objets chargés, la somme des scores vaut la somme honnête plus T, trajectoire par trajectoire.
- **Réserves de propreté (constat K)** :
  - « under the null hypothesis is approximately B. » [K37] (p. 7) est une coquille : c'est sous l'alternative ;
  - l'hypothèse de décalage échoue aux fortes charges ([K42], p. 4), alors que la figure 4 va jusqu'à p = 1 ;
  - la platitude de la courbe de la moyenne est nette à grand N, seulement approximative à petit N (lu sur la figure, p. 13). À forte charge, c'est un constat empirique hors de l'hypothèse.
- **L2 (constat G)** :
  - la meilleure répartition dépend du détecteur : « We emphasise that it cannot apply to every type of pooling algorithm. » [K26] (p. 15) ;
  - un détecteur à seuil réagit comme L2 le dit : « the number of observations greater than 1 is quite sensitive to embedding at p = 1, although worthless for other batch parameters. » [K27] (p. 15) ;
  - Ker nomme le comptage au-dessus d'un seuil et l'écarte : [K43] [K44] (p. 15) ;
  - les tests des signes et du rapport de vraisemblance à grande charge punissent la fragmentation ([K13], [K19]) ;
  - le maximum au seuil exact n'est pas étudié.
- **Validité hors hypothèses** :
  - un biais honnête ruine l'analyse groupée : « the effect is to destroy the reliability of the pooled detectors, flooding them with false positives for any large value of » [K23] (p. 14) ;
  - car il y a « systematic bias of b is indistinguishable from a batch Steganographer’s behaviour with p = b and r = 1. » [K24] (p. 15) ;
  - remède proposé : « If we train the detector first on covers of the right type (effectively removing the bias) then the problem goes away. » [K25] (p. 15).
- **Dépendance (constat H)** : aucun résultat. Une piste est nommée : [K46] [K45] (p. 16), c'est-à-dire des objets chargés avec la même clé, dont les traces s'amplifient d'un objet à l'autre et peuvent être exploitées par le guetteur.
- **Limites reconnues** : [K10], « we believe that the practice of sequential steganography and steganalysis may be rather different from the fixed-size batch problems studied here. » [K48] (p. 5) ; [K28] et « Finally, we would like to prove a general result on how steganographic capacity increases with » [K29] (p. 15) ; « There seems to be little literature on this problem » [K31] (p. 2) ; pièce séquentielle nommée : « Trivedi [1] has used sequential hypothesis tests to repeat steganalysis, but only in the context of locating a hidden message embedded sequentially within a single image. » [K30], « Active steganalysis of sequential steganography. » [K32].
- **Verdict pour L** :
  - **occupée en partie** pour le cœur de L1 ;
  - occupée pour la décroissance en n₀ dans le cas du test à horizon fixe, sous forme asymptotique, après changement d'échelle, avec un exposant qui dépend de la queue ;
  - voisin pour L4, L2 et la validité.

### 2.2 Bash, Goeckel et Towsley — « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » [A1], par « Boulat A. Bash, Dennis Goeckel, Don Towsley » [A2] (version 4 du 20 mars 2013)

- **Venue** : « arXiv:1202.6423v4 [cs.IT] 20 Mar 2013 » [A3]. La version de revue est « B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” » [R1] ; « Sel. Areas Commun., vol. 31, no. 9, pp. 1921–1930, Sep. 2013. » [R2] (1906.08938, p. 15) ; elle n'est pas lue. Ce n'est ni la pièce 2014 (« B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” » [R3]) ni la pièce 2016 (« B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” » [R4]).
- **Cadre** :
  - fenêtre entière observée : « Willie observes all n of Alice’s channel uses » [A11] (p. 15) ;
  - loi d'entrée connue du guetteur dans la partie atteignabilité : « To strengthen the achievability result, we assume that Alice’s channel input distribution, as well as the distribution of the AWGN on the channel between Alice and Willie, are known to Willie. » [A6] (p. 5) ;
  - critère α + β ≥ 1 − ε, par la variation totale et l'inégalité de Pinsker : « Since total variation lower-bounds the error of all hypothesis tests Willie can use, a clever choice of f allows Alice to limit Willie’s detector performance. » [A7] (p. 6).
- **Résultat** : « We present a square root limit on the amount of information transmitted reliably and with low probability of detection (LPD) over additive white Gaussian noise (AWGN) channels. » [A4] (p. 1).
  - L'atteignabilité repose sur « That relative entropy is locally quadratic is well-known » [A8] (p. 8), où intervient l'information de Fisher : « is the Fisher information that an observation of noise carries about its power. » [A29] (p. 8).
  - Lien avec la stéganographie : « The square root law in steganography has the same form as our square root law because both laws follow from the property that relative entropy is locally quadratic » [A9] (p. 14) ; « The square root law of steganography in the passive warden environment states that » [A5] (p. 2).
- **Réciproque avec un détecteur somme** :
  - « Suppose Alice employs an arbitrary codebook » [A27] ; « but he is oblivious to her signal properties and employs only a simple power detector. » [A10] (p. 15) ;
  - formules (13) à (17), p. 15-16, lues sur le PDF : E[S] = σ² + P_k, Var[S] = (4P_kσ² + 2σ⁴)/n ;
  - « We bound it using (13) and (14) with Chebyshev’s Inequality » [A26] (p. 16) ; « determines its detectability by this detector, and that our result applies to all codewords with power of the same order. » [A12] (p. 16) ; « Note that Willie’s detector is oblivious to any details of Alice’s codebook construction. » [A14] (p. 17) ; « Thus, with enough observations, Willie can detect with arbitrarily low error probability Alice’s codewords with the average symbol » [A15] (p. 17) ; « On the other hand, if the transmitted codeword has the average symbol power » [A36] (p. 17) ; « Thus, Alice cannot break the square root law using an arbitrarily high transmission rate and retransmissions while keeping the power below Willie’s detection threshold. » [A16] (p. 18).
- **Calculs** (`calcul_puissance_khi2_v2.py`, formes fermées, niveau 0,05, n = 200, σ = 1 ; nature : calcul).
  - n·S/σ² suit un khi-deux décentré dont le paramètre est l'énergie totale.
  - À énergie 40 fixée, la puissance vaut 0,588 pour toute répartition. Le contre-lecteur trouvait 0,584 à 0,586 par simulation.
  - Sous le **budget linéaire de L** (B = 25 sur y, m décalages égaux, énergie B²/m), la puissance du détecteur de puissance vaut 1,000 (m = 1), 0,870 (m = 10) et 0,069 (m = 200). Celle de la somme vaut 0,549 dans les trois cas. Ces chiffres concordent avec ceux du contre-lecteur (1,00 ; 0,87 ; 0,07 ; 0,549).
- **Lecture.**
  - Si le score de L est y, le détecteur de puissance n'est pas la somme et voit la fragmentation : c'est une statistique de type L5.
  - Si le score est y² :
    - le budget d'Alice (P_k) est le décalage moyen total des scores ;
    - la variance de chaque score est linéaire en son décalage ;
    - la somme des scores a une loi fonction du seul budget.
  - C'est alors une invariance au sens de L1 hors du pur décalage. Mais l'article ne l'énonce qu'**en ordre de grandeur**, par la moyenne, la variance et l'inégalité de Tchebychev, pour un bruit gaussien. Il ne la présente jamais comme une invariance à la répartition.
  - Annexe B : « First, Alice and Bob randomly select the symbol periods that they will use for their transmission by flipping a biased coin n times » [A20] ; « This product is the average symbol power used by Alice. » [A21] (p. 24) donne une borne, pas une égalité.
- **Instant de départ** : aucun. Seul l'état « émet ou n'émet pas » est discuté (« The proofs of achievability (Theorems 1.1 and 1.2) in Section III assume that Willie has no prior knowledge on whether Alice transmits or not. » [A18], p. 20). Le délai est cité comme perspective : « under additional constraints such as delay should be analyzed. » [A33] (p. 21).
- **Dépendance** : piste nommée « This result was extended to Markov » [A28] (p. 14).
- **Verdict pour L : voisin** (invariance et échelle).

## 3. Table composante × article

| composante de L | Ker (atelier 2006, actes 2007) | Bash, Goeckel et Towsley (v4, 2013) |
|---|---|---|
| L1 — égalité en loi, trajectorielle, de la somme sous budget linéaire, toute répartition, adaptatif | **occupée en partie** : invariance en loi de la moyenne, N fini, toute loi des scores, deux valeurs de décalage, choix aléatoire non adaptatif, énoncée comme immédiate, p. 7 et 14 [K36, K14, K15, K21, K22] ; non fait : valeurs inégales [K28], adaptatif, trajectoire écrite, puissance exacte, ordre temporel [K10] | voisin : moments du détecteur de puissance fonctions de la seule énergie, ordre de grandeur, bruit gaussien, p. 15-17 [A12, A26] ; sous le budget linéaire de L sur y, il voit la fragmentation (calcul) |
| L1 — décroissance en n₀ à budget fixé | **occupée** pour un test à horizon fixe, asymptotique, après B(L) = N·B(Ker) ; exposant N^{1/2} si ν > 2, N^{1−1/ν} si 1 < ν < 2 ; données à ν = 1,61, p. 4, 7, 11, 12 [K38, K39, K20, K40, K41] | voisin : même échelle en ordre de grandeur pour le détecteur de puissance ; loi de la racine carrée sur des bits [A4, A16] |
| L4 — agents au même pas, frontières de pas, toujours valide | voisin : cas T = 1 seulement, identique à L1 [K48] | ne touche pas |
| L2 — max au seuil exact, n fini, plancher | voisin et contre-indice : comptage à seuil nommé puis écarté [K43, K44] ; fragmentation punie par les signes et le rapport de vraisemblance à grande charge [K13, K19] | ne touche pas |
| L3 — borne invariante, report, prix du toujours valide | ne touche pas (séquentiel réservé [K10, K48]) | ne touche pas (délai en perspective [A33]) |
| Processus e cumulé contre détecteur de rupture | ne touche pas | ne touche pas |
| Non-compensation | ne touche pas | ne touche pas |
| Validité hors hypothèses, dépendance | voisin : biais honnête et étalonnage [K23, K24, K25] ; piste de dépendance « même clé » [K45, K46] | ne touche pas ; piste Markov nommée [A28] |
| Scores de sondes internes | ne touche pas | ne touche pas |

## 4. Verdict d'ensemble sur L (table fermée)

**Occupé en partie.** Pour la première fois, une composante revendiquée est touchée :
- **L1, cœur de l'invariance : occupée en partie** (Ker) ;
- **L1, décroissance en n₀ : occupée** pour le test à horizon fixe, sous forme asymptotique, après changement d'échelle (Ker) ;
- **L4 : voisin** (cas T = 1 identique à L1) ;
- **L2 au seuil exact, L3, processus e cumulé contre détecteur de rupture, non-compensation, dépendance, sondes : non trouvés dans les pièces lues** (lot 8 et voisins).

La collision remonte au directeur : N-003/N-004 revendique des « invariances exactes ».

## 5. Ce qui reste revendicable (formulation) — resserrée

« L1 n'est pas revendicable comme apport. Son cœur est imprimé chez Ker (2006, p. 7 et 14). L'extension aux valeurs inégales et adaptatives et l'écriture trajectorielle tiennent en une ligne de calcul : elles s'énoncent comme une **remarque avec renvoi à Ker**. Restent revendicables, sous réserve des lectures de la section 8 :
- L4 dans son contenu propre : plusieurs pas, lecture aux frontières de pas, garantie toujours valide (mathématiquement, L1 appliqué pas par pas : élémentaire) ;
- L3 : borne inférieure invariante fonction de (B, n₀), coût du report, prix de la garantie toujours valide chiffré ;
- la comparaison, pour l'alarme avant le dommage, entre processus e cumulé et détecteurs de rupture ;
- L2 au seuil exact, à n fini, avec son plancher ;
- la validité sous dépendance ;
- la mesure sur scores de sondes internes. »

Règle R8 : Ker réserve le séquentiel, les valeurs inégales et le comptage à seuil. Cette zone est séduisante et se vérifie plus durement.

## 6. Ce qu'une phrase publique déclarant L ne doit pas affirmer (ajouts à la v2 du lot 8)

Je ne rédige pas cette phrase. Elle ne doit pas affirmer :
1. que l'invariance de la statistique somme à la répartition, à budget fixé, est nouvelle (Ker, p. 7 et 14) ;
2. que Ker la démontre, ou qu'il couvre les valeurs inégales et l'adaptatif : il l'énonce comme immédiate ([K36]), pour deux valeurs, avec un choix aléatoire ([K9], [K28]) ;
3. que L1 et L4 sont deux composantes ayant chacune un précédent ou chacune une nouveauté : à T = 1 c'est une seule proposition ;
4. que l'échelle est en √n₀ pour toute loi F₀ : elle est en N^{1−1/ν} si l'indice de queue est entre 1 et 2 ([K40], [K41]) ;
5. que Ker énonce « à charge totale fixée, la détection décroît avec N » : il donne la forme capacité, avec B par objet ([K38], [K20]) ;
6. que Bash et collègues établissent une invariance à la répartition sous un budget linéaire, ou qu'un détecteur de puissance est aveugle à la fragmentation au sens de L (calcul, section 2.2) ;
7. que « fragmenter aide l'attaquant » en général ([K13], [K19]) ;
8. que l'étalonnage sur données honnêtes entières est un constat propre au programme ([K24], [K25]) ;
9. que la pièce de Ker lue est la lettre de 2007, ou que l'énoncé lu de Bash et collègues date de 2012 (version 4 de 2013 ; version de revue non lue) ;
10. que la zone « séquentiel et toujours valide » est libre : elle est non trouvée, et réservée par Ker en 2006.

## 7. Ce qui reste distinctif (lignes sèches pour présenter le nœud ; non tranché)

- L1, cœur — imprimé (Ker 2006, p. 7, 14) ; résidu : valeurs inégales, adaptatif, trajectoire ; une ligne ; nature : remarque citée.
- L1, décroissance en n₀ — imprimée en forme capacité (Ker, p. 11 ; exposant selon la queue) ; loi de la racine carrée (Bash et collègues) ; résidu : aucun.
- L4 — non trouvé hors du cas T = 1 ; contenu propre : plusieurs pas, frontières de pas, toujours valide ; mathématiquement élémentaire.
- L3, borne invariante P(E⁺_{n₀} ≥ 1/α) fonction de (B, n₀) — non trouvée.
- L3, coût du report et prix de la garantie toujours valide chiffrés — non trouvés ; séquentiel réservé par Ker.
- Alarme avant le dommage, processus e cumulé contre détecteurs de rupture — comparaison non trouvée ; critère publié (Huang et collègues, lot 8).
- L2, maximum au seuil exact, n fini, plancher — non trouvé ; sens qualitatif chez Ker (comptage à seuil) ; forme close chez Huang et collègues (Shewhart, lot 8).
- Validité sous dépendance (équicorrélation, effet épisode) — non trouvée ; pistes nommées (même clé, Ker ; Markov, Bash et collègues).
- Biais honnête et étalonnage — publié (Ker, p. 14-15).
- Application aux scores de sondes internes — non trouvée.
- Lectures préalables à toute phrase : la lettre de Ker 2007 ; Trivedi et Chandramouli 2003 ; Huang, Wang et Poor 2021 ; Bash et collègues 2014 et 2016 ; Arumugam et Bloch 2016 ; Filler, Ker et Fridrich 2009.
- Repli déjà prévu par N-004, option (c) : L présenté comme corollaire cité, effort porté sur la mesure ; toute bascule effective est un nœud.

## 8. Voisins nommés dans les pièces et non lus

| priorité | pièce (titre imprimé) | où | composantes |
|---|---|---|---|
| 1 | Ker 2007, lettre : [R5] | 2605.16140 p. 34 ; Bash et collègues p. 27 [A22] | L1, échelle (résultat général de capacité souhaité par Ker, [K29]) |
| 1 | Trivedi et Chandramouli 2003 : [K32] | Ker p. 2, 16 [K30] | séquentiel, L3 |
| 1 | Huang, Wang et Poor 2021 : « K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” » [R6] ; Bash et collègues 2014 [R3] et 2016 [R4] ; Arumugam et Bloch : « K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” » [R7] | 2605.16140 p. 35 ; 1906.08938 p. 15 | L3, calendrier, alarme avant le dommage ; réserve M4 |
| 2 | Filler, Ker et Fridrich 2009 : « The square root law of steganographic capacity for markov covers » [A23] | Bash et collègues p. 27, [A28] p. 14 | dépendance (couvertures de Markov), échelle |
| 2 | Fridrich, livre : [A35], chapitre 13 | Bash et collègues p. 2, 26 [A32] | échelle en nombre de symboles modifiés : le voisin d'échelle le plus proche d'un budget linéaire |
| 3 | Ker 2009 : « The square root law requires a linear key » [A24] ; Ker 2010 : [A30] ; Filler et Fridrich 2009 : « Fisher information determines capacity of » [A25] ; Che et collègues : [A31] | Bash et collègues p. 27 | échelle, information de Fisher, clé |

## 9. Ce que je n'ai pas fait

- Aucune pièce non versée lue. Rien du lot 8 n'a été rouvert à l'œil, hors des renvois bibliographiques.
- La preuve du lemme 2 de Ker et les dérivées de l'annexe A de Bash et collègues sont lues, pas refaites.
- Je n'ai exécuté aucun script de la contre-lecture. Mon calcul (`calcul_puissance_khi2_v2.py`) est en formes fermées : aucun tirage aléatoire, donc aucune graine nécessaire. Il a été lancé par le Python du dépôt, sur processeur.

## 10. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — citations contrôlées (`citations-L-voisins-v2.json`, dans l'archive)

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
| K36 | 68 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | It is immediate that |
| K37 | 69 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | under the null hypothesis is approximately B. |
| K38 | 70 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | is the proportionate bandwidth. |
| K39 | 71 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | The total amount of data hidden by the Steganographer is proportional to |
| K40 | 72 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | in this case the discrimination of the average statistic increases only as a power law |
| K41 | 73 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 12 | is well modelled by a t-distribution with ν = 1.61 |
| K42 | 74 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | there is both a shape change and a negative bias for higher rates |
| K43 | 75 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | for example the pooling method of counting observations greater than some threshold |
| K44 | 76 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | because this leads to a game theoretical setup which can be intractable. |
| K45 | 77 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 16 | there could be an amplification of the statistical traces, which we might exploit. |
| K46 | 78 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 16 | If we may assume that all, or most, of the steganography is performed using the same secret key |
| K47 | 79 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | Springer-Verlag Berlin Heidelberg 2007 |
| K48 | 80 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | we believe that the practice of sequential steganography and steganalysis may be rather different from the fixed-size batch problems studied here. |
| K49 | 81 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | all cover objects have the same capacity |
| K50 | 82 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | Suppose that all Xi are independent and identically distributed |
| A26 | 83 | `1202.6423v4.pdf` | 16 | We bound it using (13) and (14) with Chebyshev’s Inequality |
| A27 | 84 | `1202.6423v4.pdf` | 15 | Suppose Alice employs an arbitrary codebook |
| A28 | 85 | `1202.6423v4.pdf` | 14 | This result was extended to Markov |
| A29 | 86 | `1202.6423v4.pdf` | 8 | is the Fisher information that an observation of noise carries about its power. |
| A30 | 87 | `1202.6423v4.pdf` | 27 | The square root law does not require a linear key |
| A31 | 88 | `1202.6423v4.pdf` | 27 | Reliable deniable communication: Hiding messages in noise |
| A32 | 89 | `1202.6423v4.pdf` | 2 | symbols in covertext of size n may safely be modified |
| A33 | 90 | `1202.6423v4.pdf` | 21 | under additional constraints such as delay should be analyzed. |
| A35 | 91 | `1202.6423v4.pdf` | 26 | Steganography in Digital Media: Principles, Algorithms, and Applications |
| A36 | 92 | `1202.6423v4.pdf` | 17 | On the other hand, if the transmitted codeword has the average symbol power |
