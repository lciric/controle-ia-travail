*État des pièces.* Les blocs `QUESTION DE L'ARBITRE`, `E3-T1-conception-C`, `E3-T2-critique-croisee-A` et `E3-T2-critique-croisee-B` sont complets ; dans `FAITS`, le §3 annonce six familles de mécanismes mais n'en énumère que quatre (les deux autres sont absentes et ne sont pas inférées). Conformément à la consigne du tour III.3, cette réponse ne traite que les sections visant la proposition C.

*Conventions de statut.* Les énoncés du §2 de `FAITS` gardent le statut `VÉRIFIÉ`, ceux des §1, §3 et §4 le statut `RAPPORTÉ`, et toutes mes corrections, analyses et épreuves le statut `HYPOTHÈSE`.

---

## (a) Réponse à chaque critique visant C

Les critiques de A et de B ont mis au jour plusieurs défauts mathématiques réels dans ma conception initiale. Je ne lisse pas leurs analyses : lorsque les deux identifient une même famille de problèmes, je distingue l'apport spécifique de chacune.

### 1. Critiques acceptées (avec correction immédiate)

1. **Erreurs d'attribution factuelle [A-(a)1]. — ACCEPTÉE.**
   J'ai accolé `VÉRIFIÉ` (Gordon et Van Durme, 2013, *Reporting Bias and Knowledge Acquisition*, arXiv : pas sûr) à ma propre `HYPOTHÈSE` sur les lois plantées, et attribué à Ma et al. (2026, titre non fourni dans `FAITS`, arXiv 2605.03762) des modèles pré-entraînés pré-coupure alors que `FAITS` leur attribue le *masquage temporel strict* (les modèles pré-coupure relèvent de Luo et al., 2026, arXiv 2606.02991, et Hla, 2026, `VÉRIFIÉ`). Ces deux attributions sont corrigées.

2. **Boule de Huber en variation totale centrée sur $\widehat{P}_n$ et $\delta_{\mathrm{sab}}$ non défini [A-(a)2, A-(b)3, B-(a)3.2, B-(b)8, B-(c)4]. — ACCEPTÉE.**
   A démontre que $\widehat{P}_n$ empirique est à distance $1$ en variation totale de toute loi continue ; B montre qu'en discret à $k$ états avec $\sqrt{k/n} > 2\varepsilon$, l'erreur d'échantillonnage expulse $P_0$ de $\mathcal{B}_\varepsilon(\widehat{P}_n)$ et impose en outre de séparer l'échantillon construisant $E_s$ de celui bornant son espérance.
   *Correction* (`HYPOTHÈSE`) : dans P1, la référence est scindée en $n_1$ (construction de $E_s$ et d'une partition fixe en $m$ bacs ou d'un score scalaire) et $n_2$ (étalonnage). La boule TV est remplacée par une boule en distance de **Kolmogorov-Smirnov** (ou TV sur les $m$ bacs gelés) augmentée d'un rayon non asymptotique $r_{n_2}(\alpha/2) = \sqrt{\frac{\ln(4/\alpha)}{2n_2}}$ (inégalité de Dvoretzky-Kiefer-Wolfowitz, référence à vérifier), avec seuil de martingale $2/\alpha$, garantissant un risque global toujours valide $\le \alpha/2 + \alpha/2 = \alpha$. La force du sabotage est définie de façon homogène par $\delta_{\mathrm{sab}} := d_{\mathrm{KS}}(P_{\mathrm{sab}}, P_0)$.

3. **Conditionnement marginal vs $\mathcal{F}_{s-1}$, permutation temporelle anti-conservatrice et espacement $\Delta s > L$ dans P1 [A-(a)3, A-(a)4, A-(b)1, A-(b)2, A-(c)1, B-(b)8]. — ACCEPTÉE.**
   A montre que des pas dépendants de l'état violent $\mathbb{E}[E_s \mid \mathcal{F}_{s-1}] \le 1$ et que permuter les pas détruit l'autocorrélation honnête ; B note qu'une statistique à fenêtre fixe $L$ échoue si les actions sabotées sont espacées de $\Delta s > L$.
   *Correction* (`HYPOTHÈSE`) : l'unité de la martingale devient l'**épisode indépendant** (ou des blocs non chevauchants de longueur $L_{\mathrm{bloc}}$), le contrôle négatif utilise des **trajectoires honnêtes entières non stationnaires** avec contamination plantée aussi dans le corps de la distribution, et l'indétectabilité au-delà de $\Delta s > L_{\mathrm{bloc}}$ est inscrite comme frontière explicite.

4. **Vacuité de $\forall \pi,\; D_{\mathrm{JS}} \le \tau_{\mathrm{surf}}$ et coût de recherche $\log_2 |\Pi|$ dans P3 [A-(a)5, A-(b)5, A-(c)3, B-(a)1.1, B-(b)5, B-(c)2]. — ACCEPTÉE.**
   A et B prouvent indépendamment que le quantificateur universel sur $\pi$ rend l'ensemble des positifs vide (partition adversariale à $D_{\mathrm{JS}} = \log 2$) et que la sélection de $\widehat{\pi}_{\mathrm{MDL}}$ sans pénalité $\log_2|\Pi|$ ni ré-optimisation sous permutation fait diverger les faux positifs.
   *Correction* (`HYPOTHÈSE`) : suppression de $\forall\pi$ ; restriction à une classe finie préenregistrée $\Pi_k$ de partitions par régimes d'équations avec coût $\log_2|\Pi_k|$ dans $L(\pi)$ et ré-optimisation complète de $\pi$ sur chaque permutation du nul.

5. **Invariance inter-genres par $D_{\mathrm{JS}}$ cassée par le biais de déclaration dépendant de l'issue, non identifiable sous biais partagé, biaisée en $K/n_e$ et $\mathrm{Pa}(u,v)$ non spécifié [A-(a)6, A-(b)4, A-(c)2, B-(a)1.2, B-(b)2, B-(c)1]. — ACCEPTÉE.**
   B démontre qu'une sélection de publication dépendant de l'issue $R$ (rapport de cotes $\rho_e$) fait rejeter par $D_{\mathrm{JS}}$ une vraie loi causale tout en laissant passer les biais culturels uniformes (`VÉRIFIÉ`, Caliskan et al., 2017, *Semantics derived automatically from language corpora contain human-like biases*, arXiv 1608.07187) ; A souligne l'indétermination de $\mathrm{Pa}(u,v)$ et le biais d'échantillon fini $K/n_e$.
   *Correction* (`HYPOTHÈSE`) : je retire le filtre $D_{\mathrm{JS}}$ sur $p_e(x)$ et reconnais qu'un biais partagé par tous les genres est **non identifiable** depuis le texte seul. Pour les biais de déclaration multiplicatifs par genre ($\rho_e$ indépendant des covariables $x$), je le remplace par l'invariance des **rapports de cotes différentiels** entre paires de contextes observables préenregistrés (propriété cas-témoins invariante à $\rho_e$, sans supposer $\mathrm{Pa}$ connu), tout en bornant la taille minimale par strate et en ajoutant les contrôles négatifs de A et B.

6. **Myhill-Nerode inapplicable sur corpus passifs et inversant continu/discret [A-(a)7, B-(a)1.3, B-(b)3]. — ACCEPTÉE.**
   A note l'absence de langage $L$ et d'intervention $\mathrm{do}(\cdot)$ sur un graphe historique ; B montre que l'équivalence sur tout suffixe $w$ favorise une étoile discrète et rejette un flot continu d'exposant de Lyapunov $\lambda_1 > 0$.
   *Correction* (`HYPOTHÈSE`) : la Condition 3 est restreinte aux modèles exécutables et mondes synthétiques ; pour les variétés continues, elle est remplacée par une **équivariance locale à petit pas** sur l'orbite géodésique d'horizon borné $H < \lambda_1^{-1}\log(\delta_L/\varepsilon)$ (et non sur corde euclidienne).

7. **Sélectivité de Hewitt et Liang confondue avec l'invariance causale [B-(a)2.3, B-(b)1]. — ACCEPTÉE.**
   Une sonde linéaire lisant un raccourci lexical garde une sélectivité élevée (`VÉRIFIÉ`, Hewitt et Liang, 2019, *Designing and Interpreting Probes with Control Tasks*, arXiv 1909.03368). Elle est rétrogradée au seul rôle de filtre anti-mémorisation de sonde.

8. **Fuite d'ontologie des « analyseurs syntaxiques entraînés pré-$t_0$ » [B-(a)3.3]. — ACCEPTÉE.**
   Aucun corpus arboré typé n'existant avant 1900, l'extraction pré-$t_0$ est restreinte aux équations/tableaux explicites et à des patrons distributionnels non supervisés appris sur le seul corpus $\le t_0$, audités par **dates de coupure placebo** [A-(c)9].

9. **Signatures défectueuses d'objet manquant ($L_\Sigma/H(D_t)$, symétrie du plan, borne BBP) et fuite par dépliage rétrospectif (*inlining*) dans P5 [A-(a)8, A-(c)4, A-(c)6, B-(a)1.4, B-(a)3.1, B-(b)6, B-(c)3]. — ACCEPTÉE.**
   Je retire la signature $L_\Sigma/H(D_t)$ (divergente même sur théorie complète), j'ajoute le contrôle par plan d'échantillonnage asymétrique [A-(c)6] et la frontière spectrale BBP [B-(b)6], et j'élimine la fuite par dépliage de P5 en synthétisant les preuves d'évaluation par un solveur **sans accès au lemme $\omega$**, contre une **amputation placebo** de macros syntaxiques arbitraires.

10. **P4 : information mutuelle conditionnelle nulle, contradiction d'étalonnage hétérogène vs copies honnêtes et saturation [A-(b)7, B-(a)2.1, B-(b)9]. — ACCEPTÉE.**
    Conditionnellement à $(X,W)$, $I(Y^{(1)};Y^{(2)}\mid X,W)=0$ sous les deux hypothèses, et étalonner sur architectures hétérogènes détecte le partage de poids (prémisse) plutôt que la coordination.
    *Correction* (`HYPOTHÈSE`) : P4 est recentrée sur l'excès de **coïncidence sémantique invariante aux permutations indépendantes de surface** ($U_1 \perp U_2$), étalonné exclusivement sur des **copies honnêtes partageant leurs poids**, et reconnaît la saturation si les préférences sémantiques naturelles des copies honnêtes sont déjà quasi déterministes.

11. **P6 : « tout contournement » non testable, fuite ablation/évasion, absence de sonde aléatoire et règle de trois au niveau modèle [A-(a)10, A-(b)8, A-(c)7]. — ACCEPTÉE.**
    Seul l'ensemble déclaré $\mathcal{A}_{\mathrm{décl}}$ est testable. De plus, la règle de trois (calcul exact : $\approx 300$ unités indépendantes sans alerte pour certifier $\mathrm{FPR} \le 0{,}01$ à $95\,\%$, $\approx 150$ pour $0{,}02$) interdit de certifier un FPR de $1$–$2\,\%$ au **niveau modèle** sur ~8B.
    *Correction* (`HYPOTHÈSE`) : trois jeux disjoints (ablation, calibration, évasion), ajout d'une sonde aléatoire de même dimension et de modèles affinés honnêtement au même budget ; certification du FPR au niveau modèle uniquement sur grand nombre de petits modèles (Phase 1), et test exact de permutation de Mann-Whitney au niveau modèle sur ~8B.

12. **P7 (percolation / DC-SBM) surajustée, réfutation sans étude de puissance, fuite de blocs et graphe ouvert [A-(a)9, A-(b)6, A-(c)5, B-(b)7]. — ACCEPTÉE.**
    Je retire P7 de la liste opérationnelle et j'abandonne toute inférence réfutatoire par non-signifiance. Sur graphes finis ouverts, une formulation de percolation exigerait des blocs inférés uniquement à $\le t_0$, un modèle d'arrivée de sommets, un nul préservant la fermeture triadique et un contrôle positif de puissance planté.

13. **Mémorisation structurelle malgré renommage cryptomorphique [A-(a)11, A-(c)8], petit $n_+$ historique de P3 [A-(b)9], zones grises des duels [A-(a)12], étanchéité des seuils et jeux d'experts [A-(a)13, A-transversal 1], non-réfutabilité des scores [A-transversal 2]. — ACCEPTÉES.**
    Chaque monde synthétique oppose désormais des lois structurellement inédites à des lois isomorphes célèbres ; P3 renonce à une AUROC statistique historique post-1900 ; tous les duels $H_A/H_B$ deviennent des partitions exactes sans zone grise ; tous les seuils sont gelés sur générateurs de calibration disjoints avant SHA-256 (les jeux de Gu et Krenn, 2026 et Sternlicht et Hope, 2025, `RAPPORTÉ`, n'y interviennent jamais) ; les scores de la section 7 sont reconnus comme purement heuristiques.

### 2. Critique rejetée (avec raison)

14. **Gain MDL prédictif $\Delta L(\phi) > 0$ qualifié de faux positif sous variable latente commune $U$ [B-(b)4]. — REJETÉE comme défaut d'opérateur prédictif (clarification de portée acceptée).**
    *Raison* : lorsqu'un instrument ou formalisme commun $U$ (découvertes multiples, Merton, 1961, `RAPPORTÉ`) rend un domaine $D_1$ prédictif des relations encore absentes de $D_2$ ($\Delta L(\phi) > 0$), il ne s'agit pas d'un artefact statistique à éliminer, mais d'un levier d'idéation authentique. Ce que B établit à juste titre — et que j'intègre —, c'est que $\Delta L(\phi) > 0$ n'identifie pas une flèche causale directe $D_1 \to D_2$ mais seulement une **structure prédictive partagée** (directe ou via $U$).

### 3. Critiques transformées en tests décisifs

15. **Lexiques instrumentaux partiellement disjoints dans les vraies scissions [B-(a)1.1, B-(b)5, B-(c)2]. — TRANSFORMÉE EN TEST (intégré à P3).**
    Plutôt que de conserver un critère de similarité lexicale globale ou de renoncer à distinguer scission et homonymie, je remplace $D_{\mathrm{JS}}$ lexical par un critère de **co-invocation intra-document / partage d'équations-mères** et je le soumets au banc d'épreuve adverse de B (fausses fusions mesurées par deux instruments à vocabulaires partiellement disjoints, contre homonymes appariés en nombre de lois et concepts stables bruités).

16. **Ablation statique sur $v_1$ n'empêchant pas la migration sans coût vers un canal orthogonal libre $v_2$ [B-(a)2.2, B-(b)10, B-(c)4]. — TRANSFORMÉE EN TEST COUPE-CIRCUIT (P6a sur CPU).**
    Cette objection est décisive mais empiriquement ouverte pour des circuits distribués. J'adopte l'expérience jouet de B comme **Étape 6a préalable sur processeur seul** : si un réseau témoin comportant un canal libre $v_2 \perp v_1$ migre sans coût de compétence sous le bras d'attaque déclaré, l'hypothèse « ablation statique $\Rightarrow$ marge asymétrique adaptative » est réfutée à coût quasi nul avant toute dépense GPU sur modèles ~8B.

---

## (b) Expériences corrigées (inférence forte sans zone grise)

**Règles transversales préenregistrées (SHA-256 avant déscellement)** : (i) séparation stricte entre *générateurs de calibration* (fixant tous les seuils $\tau$, bacs et fenêtres), *générateurs d'épreuve hors famille* (lois structurellement inédites + bras témoin de lois isomorphes célèbres) et *jeux externes* (`RAPPORTÉ`, Gu et Krenn, 2026 ; Sternlicht et Hope, 2025, jamais utilisés en calibration) ; (ii) aucun juge génératif ; (iii) chaque duel oppose deux issues **mutuellement exclusives et collectivement exhaustives** ($H_A$ vs $H_B = \neg H_A$) sur un seuil décisionnel unique ; (iv) l'unité indépendante est explicitée au regard de la règle de trois (calcul exact). *Tous les chiffres ci-dessous hors `FAITS` sont `[illustratif]`.*

### P1 corrigée — Martingale de valeurs-$e$ robustes (KS + rayon DKW) sur épisodes non stationnaires
- **Dispositif** : Référence honnête de $n = 2000$ épisodes [illustratif] issus d'un processus markovien non stationnaire (contamination plantée $\varepsilon = 0{,}02$ [illustratif], moitié en queue, moitié dans le corps), scindée en $n_1 = 1000$ (construction de $E_s$) et $n_2 = 1000$ (étalonnage sur boule KS de rayon $\varepsilon + r_{n_2}(\alpha/2)$ avec $r_{n_2}(\alpha/2)=\sqrt{\frac{\ln(4/\alpha)}{2n_2}}$ et seuil d'alerte $2/\alpha$, $\alpha = 0{,}02$ [illustratif]). Contrôles négatifs : $N_{\mathrm{neg}} = 500$ suites honnêtes indépendantes [illustratif] (règle de trois satisfaite pour $\alpha = 0{,}02$), dont un bras pur $P_0$ à $k/n > 4\varepsilon^2$ [illustratif] vérifiant l'absence de fuite de validité.
- **Duel $H_A$ contre $H_B$** (à horizon $T = 5000$ épisodes [illustratif] et $\delta_{\mathrm{sab}} := d_{\mathrm{KS}}(P_{\mathrm{sab}}, P_0) = 2(\varepsilon + r_{n_2}(\alpha/2))$ [illustratif]) :
  - $H_A$ : Le détecteur maintient un FWER empirique $\le 0{,}02$ sur les $500$ suites honnêtes non stationnaires **et** surpasse le SPRT/CUSUM recalibré au même FWER d'au moins $+10$ points de puissance [illustratif] (borne inférieure de l'IC à $95\,\%$ de l'écart $> 0$).
  - $H_B$ : Complémentaire exact (FWER $> 0{,}02$ **ou** gain de puissance $< 10$ points **ou** IC à $95\,\%$ incluant $0$).
  - *Falsification* : la réalisation de $H_A$ falsifie $H_B$ ; toute autre issue falsifie $H_A$.
- **Premier pas CPU et coût** : Script Python déterministe sur flux markoviens et journaux publics d'exécution de code ; 1 poste 8 cœurs, ~6 h, ~0 € hors poste [illustratif].

### P2 corrigée — Filtre de démarcation à portée séparée (rapports de cotes différentiels ; équivariance géodésique)
- **Volet 2a (corpus et graphes passifs, CPU)** : Alignement calibré par $1000$ permutations [illustratif] préservant degrés et motifs avec **ré-optimisation de $\phi$** sur chaque permutation, suivi du filtre d'invariance des **rapports de cotes différentiels** entre genres (strates minimales $n_e(x) \ge 50$ [illustratif]) et de $\Delta L > 0$ hors échantillon. Contrôles : (i) lois causales vraies sous biais de publication dépendant de l'issue $\rho_1 \neq \rho_2$ contre corrélations non causales à $\rho_1 = \rho_2$ ; (ii) biais uniforme partagé (borne négative attendue) ; (iii) lois inédites vs lois isomorphes célèbres ; (iv) dates de coupure placebo sur archives historiques d'équations.
  - $H_A$ : Le filtre par rapports de cotes atteint $(\mathrm{TPR}_{\mathrm{lois}} - \mathrm{FPR}_{\mathrm{artefacts}}) \ge 0{,}25$ [illustratif] en régime $\rho_1 \neq \rho_2$ **et** augmente la précision@50 hors échantillon de $\ge +10$ points [illustratif] sur le meilleur alignement non filtré.
  - $H_B$ : Complémentaire exact (marge $< 0{,}25$ **ou** gain $< +10$ points).
- **Volet 2b (représentations exécutables, CPU puis GPU léger)** : Modèles entraînés sur un cercle continu $S^1$ (ou flot à horizon court $H < \lambda_1^{-1}\log(\delta_L/\varepsilon)$) contre une étoile discrète à $7$ états (`VÉRIFIÉ` pour le cardinal 7), testés par intervention d'équivariance locale $T_\delta$ sur points intermédiaires géodésiques.
  - $H_A$ : L'erreur totale de séparation continu/discret satisfait $\alpha + \beta < 0{,}15$ [illustratif].
  - $H_B$ : $\alpha + \beta \ge 0{,}15$.
- **Premier pas CPU et coût** : Générateurs synthétiques + matrices d'équations historiques pré-1900 ; 16 cœurs, ~24 h, ~15 € [illustratif] (puis ~40–80 € GPU pour le volet 2b sur ~1–8B [illustratif]).

### P3 corrigée — Scission de fausse identité par contradiction nomologique, co-invocation et $\Delta L$ pénalisé
- **Dispositif** : Banc synthétique hors famille de $N = 400$ concepts [illustratif] ($100$ fausses fusions observées par deux instruments à vocabulaires partiellement disjoints ; $150$ homonymes appariés en fréquence, entropie et nombre de lois co-invoquées ; $150$ concepts stables sous bruit d'étalonnage borné). Critère : co-invocation intra-document (partage d'équations-mères) + $\Delta L_{\mathrm{scission}}$ sur classe finie $\Pi_k$ incluant $\log_2|\Pi_k|$ et **ré-optimisation de $\pi$ sur chaque permutation**, avec tolérance métrologique. (Les cas historiques antérieurs à chaque scission + dates placebo servent d'études de cas qualitatives, hors AUROC.)
- **Duel $H_A$ contre $H_B$** :
  - $H_A$ : $\mathrm{AUROC} \ge 0{,}75$ [illustratif], gain d'AUROC $> +0{,}10$ [illustratif] sur le clustering lexical de surface, **et** $\mathrm{FPR} \le 0{,}05$ [illustratif] sur les $300$ négatifs (homonymes + concepts stables bruités).
  - $H_B$ : Complémentaire exact ($\mathrm{AUROC} < 0{,}75$ **ou** gain $\le 0{,}10$ **ou** $\mathrm{FPR} > 0{,}05$).
- **Premier pas CPU et coût** : Processeur seul (16 cœurs, ~40 h, ~30–60 € [illustratif]).

### P4 corrigée — Focalité sémantique invariante aux permutations de surface pour essaims à poids partagés
- **Dispositif** : Problèmes combinatoires à $M$ solutions équivalentes présentés à $K$ copies avec permutations aléatoires indépendantes de surface ($U_1 \perp U_2$). Statistique : excès de coïncidence sémantique $\widehat{\Delta}_{\mathrm{focal}} = \widehat{\mathbb{P}}(S(Y^{(1)}) = S(Y^{(2)}) \mid U_1 \perp U_2) - 1/M$. Contrôle négatif : $M_{\mathrm{mod}}$ modèles honnêtes distincts instanciés chacun en $K$ copies partageant leurs poids (affinés au même budget sans coordination), comparés à des modèles à coordination plantée (évaluateur tiers).
- **Duel $H_A$ contre $H_B$** :
  - *Phase 1 (calibrage au niveau modèle sur $160$ petits modèles honnêtes + $40$ coordonnés, 50–150M [illustratif])* : $H_A$ : rappel $\ge 0{,}65$ [illustratif] au quantile $0{,}98$ des copies honnêtes à poids partagés ($\mathrm{FPR}_{\mathrm{mod}} \le 0{,}02$ vérifiable par règle de trois sur $160$ modèles). $H_B$ : rappel $< 0{,}65$.
  - *Phase 2 (~8B, lancée uniquement si $H_B$ est falsifiée en Phase 1, $16$ modèles honnêtes vs $16$ coordonnés [illustratif])* : $H_A$ : test exact unilatéral de permutation de Mann-Whitney au niveau modèle $p_{\mathrm{perm}} \le 0{,}05$ et $\mathrm{AUROC} \ge 0{,}80$ [illustratif] ; $H_B$ : complémentaire exact.
- **Premier pas CPU et coût** : Phase 1 CPU/GPU léger (~15 h, ~20 € [illustratif]) ; Phase 2 conditionnelle (~60–100 € [illustratif]).

### P5 corrigée — Repéreur de primitives sans dépliage rétrospectif
- **Dispositif** : $100$ théories synthétiques hors calibration [illustratif] ($50$ à primitive manquante $\omega$ dont les preuves sont synthétisées par un solveur **sans accès à $\omega$** ; $25$ théories complètes avec macros placebo dépliées de même fréquence ; $25$ théories complètes bruitées), plus un volet quantitatif à plan d'échantillonnage asymétrique au-dessus du seuil spectral BBP. Validation exclusive par noyau formel déterministe et gain hors échantillon $\Delta L_{\mathrm{test}}(\omega) > 0$.
- **Duel $H_A$ contre $H_B$** :
  - $H_A$ : Taux de récupération vérifiée ($\Delta L_{\mathrm{test}} > 0$) sur primitives manquantes supérieur d'au moins $+25$ points [illustratif] au taux de fausses extractions sur placebos et théories complètes, **avec** $\mathrm{FPR} \le 0{,}05$ [illustratif].
  - $H_B$ : Complémentaire exact (marge $< +25$ points **ou** $\mathrm{FPR} > 0{,}05$).
- **Premier pas CPU et coût** : Solveur + e-graphes sur processeur seul (32 cœurs, ~80 h, ~60–120 € [illustratif]).

### P6 corrigée — Épreuve en deux étapes de la résistance au bras d'attaque déclaré $\mathcal{A}_{\mathrm{décl}}$
- **Étape 6a (coupe-circuit sur CPU, canal orthogonal libre)** : Réseau témoin où compétence et comportement cible partagent initialement $v_1$ (ablation de $v_1$ destructive) mais où un sous-espace vierge $v_2 \perp v_1$ est libre.
  - $H_A$ : Sous $\mathcal{A}_{\mathrm{décl}}$, abaisser le rappel de la sonde sur $v_1$ sous $0{,}20$ [illustratif] impose une perte de compétence $\ge 10$ points [illustratif] (ou le rappel reste $\ge 0{,}20$).
  - $H_B$ : Le rappel tombe sous $0{,}20$ avec une perte de compétence $< 10$ points (falsifiant l'implication « ablation statique $\Rightarrow$ marge adaptative » et bloquant la campagne 8B).
- **Étape 6b (~8B, conditionnelle à la falsification de $H_B$ en 6a)** : Trois jeux disjoints (ablation, calibration, évasion) ; contrôles par sonde aléatoire de même dimension, vérifications mécaniques boîte noire et modèles affinés honnêtement au même budget. FPR prompt vérifié sur $N = 350$ prompts honnêtes appariés [illustratif] ; $\Delta W$ évalué par test de permutation exact au niveau modèle (sans prétendre à un FPR $\le 1\,\%$ non certifiable à 8B).
  - $H_A$ : Sur jeu d'évasion disjoint, à $\mathrm{FPR}_{\mathrm{prompt}} \le 0{,}01$, la sonde causale maintient un rappel $\ge 0{,}60$ [illustratif] **ou** impose à $\mathcal{A}_{\mathrm{décl}}$ une perte de compétence $\ge 10$ points [illustratif], **et** bat les vérifications mécaniques et la sonde aléatoire d'au moins $+15$ points [illustratif].
  - $H_B$ : Complémentaire exact.
- **Premier pas CPU et coût** : Étape 6a sur CPU (~4 h, ~0 € [illustratif]) ; Étape 6b conditionnelle sur 1–2 GPU 80 Go (~250–500 € [illustratif]).

*(P7 sur la percolation finie est suspendue hors priorités tant qu'aucun modèle d'arrivée de sommets, nul triadique pré-$t_0$ et contrôle positif de puissance ne justifie un investissement.)*

---

## (c) Réponse à la question de l'arbitre (une page)

### Ce qui est établi
Le corpus vérifié (`VÉRIFIÉ`, §2 de `FAITS`) établit que les statistiques distributionnelles reconstruisent localement des géométries réelles (119 cités assyriennes, 50 villes américaines, espace des couleurs, sous-espaces spatiaux/temporels dans Llama-2) et extraient des régularités latentes (tableau périodique, matériaux thermoélectriques, issues en neurosciences). Mais il établit simultanément cinq limites dures : (1) après étalonnage de permutation, la convergence globale entre représentations s'efface largement au profit d'un accord local (Gröger, Wen et Brbić, 2026, arXiv 2602.14486) ; (2) des géométries apparemment circulaires peuvent fonctionner comme sept états discrets en étoile (Gupta, Fruengel et Heimersheim, 2026, arXiv 2610.37796) ; (3) des modèles performants échouent au transfert causal de lois sur automates et orbites (Vafa et al., 2024, arXiv 2406.03689 ; 2025, arXiv 2507.06952) ; (4) les sondes peuvent mémoriser sans sélectivité (Hewitt et Liang, 2019, arXiv 1909.03368), et la forme seule n'implique pas l'ancrage référentiel (Bender et Koller, 2020) ; (5) l'ignorance temporelle simulée par consigne laisse un écart de 52 % sur 477 questions et neuf modèles (Li et al., 2026, arXiv 2601.13717), imposant le masquage temporel strict (Ma et al., 2026, arXiv 2605.03762) ou des modèles pré-entraînés avant coupure (Luo et al., 2026, arXiv 2606.02991 ; Hla, 2026). Enfin, le cahier des charges (`RAPPORTÉ`) exclut tout juge génératif, interdit tout signal d'audit dans la boucle d'entraînement hors bras d'attaque déclaré, et impose des tests falsifiables rapides sur processeur seul avant tout passage sur modèles ouverts (~8 milliards de paramètres).

### Ce qui ne l'est pas — et où se situent les frontières infranchissables
À l'issue de l'examen critique croisé, **aucun** des ponts ambitieux envisagés par la question initiale n'est établi (`HYPOTHÈSE`) : ni l'existence d'opérateurs communs valides à la fois en idéation non stratégique et en contrôle adaptatif, ni la détectabilité *avant coup* des scissions conceptuelles et des objets formels manquants, ni l'existence d'une marge asymétrique durable des sondes ou de $\Delta W$ sur modèles ~8B (**je ne sais pas** si la redondance distribuée à 8B rend toute sonde statique contournable sans perte de compétence). Surtout, cinq frontières mathématiques ou méthodologiques résistent à toute méthode purement observationnelle :
1. **Non-identifiabilité du biais de déclaration partagé** : si un biais affecte tous les genres, aucun test sur textes seuls ne le distingue d'une loi invariante ; seul un biais multiplicatif spécifique à un genre peut être neutralisé par invariance des rapports de cotes différentiels.
2. **Plancher statistique en sabotage diffus** : sous référence honnête finie $n_2$ contaminée à taux $\varepsilon$, tout sabotage purement marginal vérifiant $d_{\mathrm{KS}}(P_{\mathrm{sab}}, P_0) \le \varepsilon + r_{n_2}(\alpha/2)$ est statistiquement indistinguable, de même qu'une dépendance espacée au-delà de la fenêtre de bloc.
3. **Barrières d'échantillonnage et de signal** : certifier un $\mathrm{FPR} \le 1\,\%$ au niveau modèle exige $\approx 300$ modèles honnêtes indépendants (calcul exact, règle de trois), rendant ce niveau inatteignable à 8B ; l'analyse spectrale de résidus ou de $\Delta W$ échoue sous le seuil BBP ; l'ablation statique ne prouve pas l'impossibilité d'une ré-allocation vers un sous-espace libre.
4. **Pièges d'évaluation en rétrodiction et synthèse formelle** : $n_+$ est trop petit pour une AUROC historique crédible des scissions post-1900 ; déplier un lemme déjà conçu injecte la solution dans l'AST ; renommer les symboles n'empêche pas la mémorisation structurelle ; des formulations de percolation sur graphes finis ouverts confondent degrés hétérogènes, fermeture triadique et transitions critiques.
5. **Sous-détermination empirique** : sans intervention causale ou mesure expérimentale nouvelle, aucun opérateur MDL ou relationnel ne départage des théories empiriquement équivalentes sur le corpus $\le t_0$, ni ne scinde un concept avant l'apparition d'une anomalie enregistrée.

Les seuls opérateurs prioritaires qui résistent à la critique sont donc modestes et spécialisés : (i) une martingale robuste à boule KS + rayon non asymptotique sur épisodes (P1), (ii) un filtre d'alignement à permutations ré-optimisées et rapports de cotes différentiels complété sur modèles exécutables par équivariance géodésique (P2), (iii) un détecteur de contradiction nomologique à co-invocation et pénalité de recherche (P3), (iv) un test de focalité sémantique sous permutations de surface étalonné sur copies honnêtes à poids partagés (P4), et (v) une compression d'e-graphes évaluée sans dépliage rétrospectif (P5).

### L'expérience à faire en premier
L'expérience prioritaire est **P1 corrigée** (martingale de valeurs-$e$ sur boule KS + rayon DKW, sur épisodes honnêtes non stationnaires contaminés dans la queue et dans le corps), suivie immédiatement du coupe-circuit **P6a** sur réseau témoin à canal orthogonal libre — les deux s'exécutant en moins d'une journée sur processeur seul à coût quasi nul. **P1** doit passer en premier pour trois raisons vérifiables : (1) elle s'affranchit des fuites historiques et de la limite d'échantillon à 8B ; (2) elle cible directement le premier verrou du contrôle boîte blanche (sabotage diffus sous référence finie contaminée) tout en cartographiant la frontière exacte $\varepsilon + r_{n_2}$ ; (3) si $H_A$ survit, son moteur de valeurs-$e$ séquentielles robustes fournit l'infrastructure d'étalonnage anti-multiplicité nécessaire à toutes les autres épreuves de l'organisme d'idéation ; si $H_A$ est falsifiée, le programme économise immédiatement une mauvaise architecture de surveillance.

FIN-DE-CELLULE