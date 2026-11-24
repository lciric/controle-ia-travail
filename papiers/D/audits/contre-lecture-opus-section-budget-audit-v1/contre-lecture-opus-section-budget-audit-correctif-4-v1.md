# Contre-lecture de la section sur le budget d'audit et l'audit tiré au hasard (papier D), version correctif 4 — v1

- Contre-lecteur neuf : Opus 5.5, effort élevé. Je n'ai pas écrit la pièce et je n'ai lu aucune contre-lecture antérieure. Je n'ai modifié aucun fichier du dépôt.
- Pièce : `papiers/D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`. Son empreinte est conforme à son compagnon `.sha256`, comme celles des quatre versions antérieures et du script `check_audit_v1.py`.
- Scripts de vérification : `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/verif-budget-audit/` (`stats_sorties.py`, `budget_check.py`, `checks_section.py`, `dp_exact.py`, essai de compilation dans `compil/`).

## Verdict

**Accepté avec corrections.**

- Je n'ai trouvé aucune erreur dans les énoncés, les preuves ni les exemples chiffrés. Les chiffres de la remarque sur la simulation préenregistrée sont conformes au verdict de lecture et aux sorties scellées ; je les ai recalculés.
- Deux défauts bloquent l'insertion **telle quelle** dans le manuscrit de base (D1 et D2). Ils sont simples à lever.
- La remarque sur la simulation doit être resserrée sur trois points (D4 à D6). Elle ne confond pas la marge et le budget, mais elle laisse deux lectures trop fortes.
- Plusieurs conflits de notation et de clés bibliographiques sont à corriger avant l'insertion (D3, D7 à D11).

## Défauts

### D1 — Bloquant pour l'insertion : la section dépend d'une section absente du manuscrit de base

- **Emplacement** : ligne 36 (« We use the logit recursion of the earlier section ») et ligne 22 (« The static analysis charges every episode an audit probability $\rho$ »).
- **Constat** : le manuscrit de base `main-v4-correctif-3-erratum-1.tex` est entièrement statique.
  - Il ne contient ni récurrence des logits, ni gradient naturel, ni pas $\gamma$ : `grep logit` ne renvoie rien, et $\gamma$ n'apparaît qu'une fois, dans les limitations.
  - La récurrence visée est celle de la section de dynamique, `brouillon-fable-dynamique-v1/dynamics-section-v1-correctif-3.tex` (règle (a) ancrée, $\phi_{k+1}=(1-\gamma/\eta)\phi_k+\gamma r$). Cette section n'est pas dans le manuscrit de base.
  - De même, « the static analysis » qui fixe une probabilité d'audit $\rho$ est le régime R3 du théorème `thm:escape`, où $\rho$ est la part des épisodes pièges. Aucun renvoi n'y mène.
- **Correction** : choisir l'une des deux voies.
  - (a) Insérer d'abord la section de dynamique, puis remplacer « the earlier section » par `Section~\ref{sec:dynamics}`, en citant l'équation exacte de la règle ancrée.
  - (b) Rendre le lemme `lem:audit-logodds` autonome : une phrase qui pose le gradient naturel régularisé par le KL sur la loi softmax des strates, et qui rappelle que son point fixe $\theta-\theta_0=\eta r$ est la loi de Gibbs de l'opérateur B quand le moniteur est aveugle.
  - Dans les deux cas, écrire « Theorem~\ref{thm:escape}(R3) » à la ligne 22. Définir aussi $L:=\log(p_{\mathrm h}/p_{\mathrm f})$ dans les notations du manuscrit, en supposant $p_{\mathrm f}<p_{\mathrm h}$ : la section de dynamique le définit, le manuscrit de base ne le définit pas.
  - Ajouter une demi-phrase qui justifie l'abandon de la strate visible : sous le gradient naturel en softmax, l'écart de logits $\theta^f-\theta^h$ ne dépend pas de la strate $v$. L'abandon est donc exact pour $\ell_k$, et pas seulement une simplification.

### D2 — Bloquant pour la compilation : environnements non définis

- **Emplacement** : `lem:audit-logodds`, `def:audit-budgets`, `cor:audit-tradeoff`.
- **Constat** : le manuscrit ne définit que `theorem`, `proposition` et `remark`. J'ai inséré la section avant « Limitations » avec le préambule inchangé et compilé : trois erreurs « Environment lemma/definition/corollary undefined ». Une fois les trois environnements ajoutés, la section compile sans erreur ni boîte trop large qui lui soit propre ; seules les citations restent indéfinies (voir D7).
- **Correction** : ajouter au préambule `\newtheorem{lemma}[theorem]{Lemma}`, `\newtheorem{corollary}[theorem]{Corollary}`, et `\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}` (ou le style par défaut), sur le compteur commun.

### D3 — À corriger : conflits de notation avec le manuscrit et avec la section de dynamique

| Symbole | Manuscrit de base | Section de dynamique | Cette section | Correction proposée |
|---|---|---|---|---|
| $C$ | pénalité d'interception de l'opérateur B (et pénalité des pièges dans R3) | idem | pénalité d'**audit** ; celle du moniteur s'y appelle $C_{\mathrm{loop}}$ (ligne 59) | renommer la pénalité d'audit ($C_{\mathrm a}$) et écrire $C$ au lieu de $C_{\mathrm{loop}}$ ; ou dire explicitement que, dans la proposition `prop:audit-indist`, la pénalité d'audit joue le rôle du $C$ de R3 |
| $\beta$ | probabilité de survie au moniteur | idem | erreur de seconde espèce dans `thm:audit-detection`(c), lignes 293-295 | $\beta_{\mathrm{II}}$, ou « miss probability » |
| $\varepsilon$ | $\varepsilon_{\mathrm{trap}}$ = probabilité qu'un piège rate | — | marge (`thm:audit-random`) ; taux alternatif (`thm:audit-detection`(c), `rem:audit-detect-deter`) ; $\varepsilon_a$ = probabilité qu'un audit rate | garder $\varepsilon$ pour la marge ; renommer le taux ($\varepsilon_0$, ou $q$) ; écrire $\varepsilon_{\mathrm{trap}}$ au lieu de $\varepsilon_a$, ou relier les deux |
| $T$ | nombre de tours de rejet répété (`rem:modelA`) | — | nombre total d'épisodes $nK$ | renommer l'un des deux |
| $\rho$ | part des pièges (R3), compatible | $\rho:=\beta_f/\beta_h$ | taux d'audit | si la dynamique entre, renommer son $\rho$ |
| $\tau$ | probabilité de tricher (R3), compatible | temps d'atteinte | probabilité de tricher | renommer le temps de la dynamique |
| $G$, $\Gamma$ | — | $G(\pi)$ gradient ; $\Gamma(y)$ fonction | $G_k$, $\Gamma_K$ | noter que $G_k=\eta\lambda_k$ avec le $\lambda_k$ de la dynamique, et renommer l'un des deux |
| $\Delta R$ | $\Delta R_{\mathrm f}=\Delta R_{\mathrm v}-\delta_{\mathrm{maint}}$ | $\Delta R$ | avantage de la strate furtive | écrire $\Delta R_{\mathrm f}$, ou se placer dans le régime canonique |
| « operator~B » | « Operator~B » | | ligne 59 | majuscule |

Les autres symboles sont compatibles ou cohérents : $\eta$ y est la même pression d'optimisation (le point fixe de la récurrence est $e^{\eta r}\pi_0$) ; de même pour $\delta_{\mathrm{ind}}$, $\gamma$, $\Prob$ et $\Var$. Aucun label de la section ne double un label du manuscrit (préfixe `audit`), et aucun renvoi interne ne pend.

### D4 — À corriger : la remarque `rem:audit-random-sim` annonce « 138 configurations » pour une grille de 144

- **Emplacement** : ligne 451, première phrase.
- **Constat** : le produit des valeurs listées fait $3\times2\times2\times3\times2\times2=144$. Le préenregistrement et le verdict comptent 144 points, dont 138 admissibles. Les 6 points non admissibles ($n=100$, $\gamma=0{,}2$, $\eta=1$, $C=19$) ont $\varepsilon>c$ : l'hypothèse de `thm:audit-random`(c) y échoue et la garantie est vide. C'est une information sur la portée du théorème, et le texte la tait.
- **Correction** : « on a grid of 144 configurations (...); in 6 of them ($n=100$, $\gamma=0.2$, $\eta=1$, $C=19$) the margin exceeds the headroom, $\varepsilon>c$, so that part (c) does not apply, and the remaining 138 were simulated ».

### D5 — À corriger : « a margin is necessary » contredit en apparence `rem:audit-random` et dit moins qu'il ne semble

- **Emplacement** : ligne 451 (« Without margin ... : a margin is necessary »), à rapprocher de la ligne 441 (« we do not claim that the margin is necessary »).
- **Constat** :
  - Sans marge, la trajectoire en champ moyen du plan juste à temps est posée sur le seuil pendant au moins 24 tours. Le franchissement est donc presque certain par construction ; le préenregistrement le justifiait ainsi, sans tirage.
  - Ce résultat montre que l'instrument voit le franchissement. Il ne dit rien de la nécessité d'une marge de l'**ordre** de $\varepsilon$, qui est ce que la remarque `rem:audit-random` refuse de revendiquer.
  - Les deux phrases, à dix lignes d'écart, se lisent comme une contradiction.
- **Correction** : « Without margin the mean-field path sits on the threshold, and the threshold is crossed with frequency at least 0.86 (median 0.97): some positive margin is needed, as expected, and the instrument detects crossings. » Retoucher en même temps `rem:audit-random` : « we do not claim that a margin of the order of $\varepsilon$ is necessary; on the grid of Remark~\ref{rem:audit-random-sim} it is larger than needed by a factor 1.75 to 3.56. »

### D6 — À corriger : la marge empirique est un oracle, et l'économie porte sur $B_\varepsilon$, pas sur les audits réservés

- **Emplacement** : ligne 451 (« the smallest margin that keeps the crossing frequency at $\delta/2$ ... in reserved audits, using that smaller margin would save ... »).
- **Constat**, en quatre points :
  1. **Ce que mesure le facteur.** $\varepsilon_{\mathrm{emp}}$ est la borne haute d'une bissection sur la fréquence ponctuelle du processus **sans plafond**, au niveau $\delta/2$. C'est le niveau de l'étape de preuve, pas celui de l'énoncé (c), qui porte sur le processus plafonné au niveau $\delta$. La marge est calibrée par simulation, à paramètres connus, sur 137 points (le point n° 31 n'a pas de bissection). Elle n'est pas disponible a priori : « would save » laisse croire qu'on pourrait s'en servir.
  2. **La quantité économisée.** Je l'ai recalculée par la forme close de `eq:audit-unif` : c'est $(B_\varepsilon-B_{\varepsilon_{\mathrm{emp}}})/B^\star_{\mathrm{unif}}(c)$, avec $B_m=n\sum_k\rho_k(m)$, le nombre **moyen** d'audits du plan. Sur le plafond $B_{\mathrm{rand}}$, que « reserved audits » évoque, l'économie irait de 2,0 % à 63 % (médiane 10,9 %), et non de 2 % à 57 %.
  3. **Marge et budget.** La phrase « The margin is not the budget » est juste et bienvenue : la remarque ne confond pas les deux. Le facteur sur la marge est le plus grand à $\eta=\infty$ (médiane 3,10), là où l'économie est la plus faible (médiane 7,8 %). À $\eta=1$, c'est l'inverse : facteur 1,95, économie 18,9 %. Pour éviter toute lecture « le budget est surdimensionné de 2,5 fois », il aiderait de donner aussi le surcoût total de la marge.
  4. **Formulation.** « keeps ... at $\delta/2$ » devrait être « keeps ... at most $\delta/2$ ».
- **Correction** : « an empirical, oracle estimate (bisection on the uncapped process at level $\delta/2$, on the 137 configurations where it ran) of the smallest margin keeping the crossing frequency at most $\delta/2$ is smaller than $\varepsilon$ by a factor between 1.75 and 3.56 (median 2.49). The margin is not the budget: planning with that oracle margin would lower the expected number of audits $B_\varepsilon$ by 2% to 57% of $B^\star_{\mathrm{unif}}$ (median 10.5%). »
  - **Ajout facultatif.** Le surcoût $(B_\varepsilon-B^\star)/B^\star$ va de 2,7 % à 101 % (médiane 20 %), et la marge oracle en reprendrait 43 % à 72 % (médiane 60 %). Ces chiffres sont **mon calcul** à partir des sorties scellées. Ils ne figurent dans aucune pièce scellée : ne les inscrire qu'après un calcul versé et empreinté (R6).

### D7 — À corriger : clés bibliographiques divergentes ou absentes

- **Constat** :
  - Deux clés doublonnent des entrées existantes du manuscrit, sous un autre nom : `greenblatt2023control` (manuscrit : `greenblatt2023`) et `griffin2024games` (manuscrit : `griffin2024`).
  - `wen2024adaptive` porte au registre le nom `wen2024`.
  - Les 19 autres clés n'existent pas dans le `thebibliography` du manuscrit : elles ne sont qu'en commentaire, et la compilation les laisse toutes indéfinies.
  - `gans2026randomized` et `zhu2026blindfold` ne figurent pas au registre des références du papier D, v2.
- **Correction** :
  - Renommer les trois clés, comme le demande la correction 5 du registre v2.
  - Convertir les entrées en commentaire en `\bibitem` au format du manuscrit.
  - Ajouter Gans et Holden, et Zhu, Zuo et Sun, au registre, avec les empreintes des PDF qui figurent dans la note de lecture des sept voisins.

### D8 — À corriger : références non confirmées ou non lues sur PDF, et une antériorité manquante

1. **`zhang2008policyteaching`** : NON_CONFIRMEE au registre v2. La recherche y trouve un autre article (Zhang, Parkes, Chen, 2009), et la correction 7 du registre dit : « ne pas la garder sans vérification des actes d'AAAI 2008 ». Ma mémoire m'indique que l'article d'AAAI 2008 de Zhang et Parkes existe sous ce titre, mais elle n'est pas opposable (R7). Retirer la citation ou la confirmer avant l'insertion.
2. **Aslam et Rivest : antériorité manquante pour `thm:audit-detection`(b).** La taille minimale d'un échantillon sans remise qui trouve au moins un élément corrompu parmi $k$ sur $T$ est exactement le problème de la taille d'un audit statistique d'élection :
   - Rivest, « On Estimating the Size of a Statistical Audit », brouillon de 2006 ; le second vérificateur a établi sa source et son empreinte ;
   - Aslam, Popa et Rivest, « On Estimating the Size and Confidence of a Statistical Audit », EVT 2007 : titre donné par la page de Rivest, mais encore NON_CONFIRMEE au registre.

   Si mon souvenir est exact, leur approximation, de la forme $(N-(b-1)/2)(1-\alpha^{1/b})$, tombe entre les deux bornes $(T-k+1)(1-\delta^{1/k})$ et $\lceil T(1-\delta^{1/k})\rceil$ de la section. Cette forme est à vérifier sur le PDF avant de l'écrire. La remarque `rem:audit-related` ne cite pas cette littérature, alors qu'elle cite les jeux de cache-cache. Il faut l'ajouter : « the minimal audit size (b) is known in election auditing~\cite{rivest2006,aslam2007} », en citant les deux, comme le demande la correction 6 du registre.
3. **`blocki2013audit`** : auteurs confirmés sur arXiv ; lieu IJCAI 2013 non lu.
4. **`boucheron2013concentration`** : le numéro « Theorem 2.10 and Corollary 2.11 » reste à lire sur PDF (correction 8 du registre).
5. **`freedman1975tail`** : notice confirmée, mais la constante « $2bt$ » attribuée à Freedman n'a pas été lue sur PDF. Elle est cohérente avec la forme $\exp(-a^2/(2(a+b)))$ de son théorème 1.6, telle que je m'en souviens.
6. **`christiano2021lowstakes`** : le billet s'intitule « Low-stakes alignment ». Le texte dit « low-stakes control » : écrire « the low-stakes setting ».
7. **Gans et Holden, et « Blindfold »** : ce qui leur est attribué est conforme à la note de lecture sur PDF. Gans et Holden : $p_i\ge\sup(g_i-c_i)/(F_id_i)$ (Prop. 3, p. 11-13), et le plancher indépendant de la sanction quand le tirage s'apprend avant l'action (Prop. 5, p. 15-16). « Blindfold » : biais au pire proportionnel à la distinguabilité, que l'élévation du taux d'audit ne corrige pas (p. 1). Mais ce sont des prépublications arXiv v1, non évaluées : « Two published neighbours » doit devenir « Two recent preprints ».
8. **Aucun chiffre de l'état de l'art n'est présenté comme vérifié sans pièce** : la section ne tire aucun nombre de la littérature. Les autres clés concordent sur leur notice au registre v2 (Avenhaus, Dresher, Tambe, Becker, Yao, Le Cam, Yu, Hoeffding, Serfling, Greenblatt, Griffin, Wen, Deng, Rakhsha, Christiano). Leurs affirmations, en revanche, n'ont pas été lues sur PDF : la section le dit déjà pour les « voisins ».

### D9 — À corriger : notes de travail dans le corps du texte

- **Emplacement** :
  - ligne 408 : `\cite[..., to be checked]{...}` ;
  - ligne 529 : « (to locate and verify) » et deux fois « (no reference checked) » ; « Apart from these two, the neighbours above have not been read on PDF, and the claims below are made subject to that reading » ;
  - ligne 534 : « this last point must still be confronted with ... before it is kept as a contribution ».
- **Constat** : ces mentions s'impriment dans le texte. Elles sont honnêtes, mais elles n'ont pas leur place dans un manuscrit.
- **Correction** : les résoudre avant l'insertion. Lire et citer, ou retirer le voisin non trouvé (« steering by payments under a budget », « inspection games in which the inspectee learns », « inverse-probability-weighted sparse rewards »). Sinon, les déplacer en commentaire LaTeX, et garder dans le texte une seule phrase sobre de limite.

### D10 — Mineur : identifiants internes et état périmé dans les commentaires

- **Constat** : les commentaires LaTeX citent des chemins du dépôt et des identifiants internes : `papiers/D/...`, `docs/notes/...`, « chantier3 », « R6 », « R7 », « Fable », « Opus », « second daughter session », « B1-B9 ». C'est toléré dans un commentaire, mais à purger avant toute diffusion du source, puisqu'arXiv publie les sources.
  - L'en-tête porte encore « STATUS: A REVOIR PAR FABLE. Not for diffusion. », qui date du correctif 1. Il dit aussi « ALL citations are A VERIFIER SUR PDF (R7) until the reference check » alors que le registre v2 existe.
  - La mention du correctif 4 précède celle du correctif 3.
  - Aucun identifiant interne ne figure dans le corps du texte.
- **Correction** : mettre à jour l'état ; supprimer les chemins avant la diffusion.

### D11 — Mineur : provenance de la remarque sur la simulation

- **Constat** :
  - Le verdict cité en commentaire n'est pas sur la branche courante (`papier-d/evasion-post-entrainement-v1`) : il n'existe que sur `origin/lecture/seuil-papier-d-v1`. Je l'ai lu par `git show`, et son empreinte est conforme au commentaire (`6967654e…af288`).
  - L'empreinte des sorties y est tronquée (« f739c1df...54c6 »). L'empreinte complète, vérifiée, est `f739c1df19b015b57c0ec817b13feba10e36ffd2dbde63bb315649f4445954c6`.
  - Le texte destiné au lecteur ne nomme ni le script ni les sorties, alors que le manuscrit nomme ses scripts compagnons dans une note.
- **Correction** : verser le verdict sur la branche du papier ; écrire l'empreinte complète ; nommer le script de la simulation parmi les scripts compagnons.

### D12 — Mineur : précisions de mathématique et de formulation

1. **Ligne 251.** Après « for the uniform criterion, from an upper bound on $\gamma$ », la phrase « The final-criterion budget is not monotone in $\gamma$ » répond à une autre question. Le point utile est que le plan concentré en fin d'horizon, calculé avec un $\hat\gamma\ge\gamma$, peut être infaisable : je l'ai constaté dans 5 323 tirages aléatoires sur 19 751. Écrire : « no such safe direction exists in $\gamma$ for the final criterion ».
2. **Ligne 474.** « a stratum with $\tau\le\delta_{\mathrm{ind}}$ **has** $d_j=(1-\rho_j)\tau\Delta R$ » ne vaut que pour la strate la pire, $\tau_A=0$ : écrire « the worst such stratum ($\tau_A=0$) has ».
3. **Ligne 434** (`rem:audit-random`). « negligible against $B^\star_{\mathrm{unif}}$ » est asymptotique. Sur la grille, à $\eta=\infty$, le surcoût de la marge atteint 53 % de $B^\star$ (médiane 11 %, mon calcul). Écrire « asymptotically negligible ».
4. **Ligne 451.** Une seule configuration a servi à un essai de fonctionnement avant la course, avec des graines distinctes (déclaration versée). Ce n'est pas nécessaire au papier, mais « fixed before any draw » reste exact : le préenregistrement était scellé avant cet essai.
5. **Ligne 451**, piste « maximal martingale inequality » : elle s'applique telle quelle à $\eta=\infty$, où $\hat x_k-x_k$ est une martingale en $k$. Pour $\eta<\infty$, les poids $a^{k-1-j}$ dépendent de $k$, et il faut passer par $a^kM_k$, plus un découpage en tranches. À préciser en une demi-phrase.
6. **Facultatif, pour asseoir « never crossed ».** Sur les 32 configurations calculables exactement (à $\eta=\infty$), la probabilité exacte de franchissement avec la marge est au plus $2{,}7\times10^{-7}$ (verdict, § 8). La marge est donc prudente de plusieurs ordres de grandeur **en probabilité**, alors qu'elle ne l'est que d'un facteur 1,75 à 3,56 **en marge**. C'est un argument de plus contre la confusion entre marge et budget, ou entre marge et probabilité.

## Ce qui a été vérifié et tient

### Mathématique : énoncés, hypothèses, preuves, refaits à la main

- **Lemme `lem:audit-logodds`** : la différence des deux coordonnées donne bien $\ell_{k+1}+L=a(\ell_k+L)+\gamma d_k$. La condition $\gamma\le\eta$ garantit $a\ge0$.
- **Équations `eq:audit-adv` et `eq:audit-x`** : on retrouve $G_k=\eta(1-a^k)$ et la borne $\eta\Delta R$. La faisabilité de $\rho\equiv1$ ($x_k=-CG_k$) et l'arrondi vers le haut, au plus un audit de plus par tour, tiennent.
- **Théorème `thm:audit-deterrence`(i)** :
  - l'identité `eq:audit-identity` (somme de la récurrence, $1-a=\gamma/\eta$) ;
  - la borne inférieure, qui est la dualité faible de la programmation linéaire ;
  - le plan juste à temps : $x_{\kappa+1}=c$, puis maintien en $c$ ;
  - $0<\rho_\kappa\le\rho_{\mathrm{hold}}\le\Delta R/W$ ;
  - l'unicité pour $\eta<\infty$.
- **Théorème `thm:audit-deterrence`(ii)** :
  - le cas $\gamma=\eta$ ;
  - le multiplicateur $\lambda=a^{-m}$ et le calcul $\sum_{i<m}(1-a^{i-m})=m-a^{-m}G_m/\gamma$ ;
  - la faisabilité du plan concentré en fin d'horizon ;
  - la forme explicite de $m$ (le plancher reste $\le K$ car $1-D/(\eta W)\ge a^K$) ;
  - la borne `eq:audit-fin-bound`. Elle est vraie pour tout horizon dès qu'un horizon donne $D>0$, car alors $\eta\Delta R>c$ et le membre de droite est positif.
- **Corollaire `cor:audit-tradeoff`(a)-(c)** et **remarque `rem:audit-criteria`**, monotonies comprises. J'ai prouvé à la main la sûreté d'un plan uniforme calculé avec $\hat\gamma\ge\gamma$ : au tour $\hat\kappa+1$, $a-(\gamma/\hat\gamma)\hat a=1-\gamma/\hat\gamma$. J'ai vérifié numériquement, sur 19 751 tirages, qu'aucun plan uniforme calculé avec $\hat\gamma\ge\gamma$ n'est infaisable ; et sur 40 000 cas, qu'aucun plan calculé avec $\hat\eta\ge\eta$ ne l'est.
- **Théorème `thm:audit-detection`** :
  - (a) l'argument du chemin $Q(u)$, la symétrie hypergéométrique et la direction facile du principe de Yao ;
  - (b) les encadrements de $q$, l'inégalité de Bernoulli et les quatre bornes de $B^\star_{\det}$ ;
  - (c) la borne à deux points, $\min\max=\mu/(1+\mu)$, et les deux conditions de budget.
- **Remarque `rem:audit-detect-deter`** : l'exemple $T=257$, $k=1$, $\delta=0{,}05$ donne bien $B^\star_{\det}=245$ contre 769,9 ; la borne $(1-e^{-1})(T-k+1)$ et la condition d'évasion tiennent.
- **Théorème `thm:audit-random`** :
  - (a) les variables bornées par $\gamma W/n$, la variance majorée par $(\gamma W)^2\bar\rho\Gamma_K/n$, et le choix de $t$ dans Bernstein (inégalité $\sqrt{A+B}\le\sqrt A+\sqrt B$) ; la remarque sur $b\Lambda/3$ est juste ;
  - (b) ;
  - (c) le partage $\delta/2+\delta/2$ et le plafond ;
  - l'inflation `eq:audit-inflation`, qui est le caractère 1-lipschitzien en $c$ ;
  - les deux formes explicites, avec $\Gamma_K=K$ et $\Gamma_K\le\eta/\gamma$.
  - L'énoncé du théorème est identique à celui du correctif 1 éprouvé par la course : seule la mention de Boucheron a changé.
- **Proposition `prop:audit-indist`** : règle de Bayes et borne de (a) ; avantage et substitution $(\tau\Delta R,\tau C_\delta)$ ; taux de maintien et son inégalité ; cas $\tau\le\delta_{\mathrm{ind}}$. Je retrouve les deux exemples chiffrés : 1,7912 (« 1,79 ») et 3,9991 (« 4,0 »). Les deux extensions de la ligne 59 sont exactes : audit qui rate ($W\to(1-\varepsilon_a)W$, $C'$) et moniteur de l'opérateur B avec $\beta_h=1$.
- **Script de l'auteur** `check_audit_v1.py` : rejoué dans un environnement à part. L'écart maximal entre la programmation linéaire et la forme close vaut $2{,}4\times10^{-8}$. Les formes explicites de $m$ et de $\kappa$, et les bornes de détection, passent sans violation.

### Remarque sur la simulation : chiffres contre le verdict et contre les sorties scellées

- **Pièces.** J'ai trouvé le verdict sur `origin/lecture/seuil-papier-d-v1` ; son empreinte est conforme au commentaire. Le manifeste (`a44f3ab6…`) et les sorties (`f739c1df…54c6`) sont conformes à leurs compagnons ; la course est valide et la liste des défauts d'instrument est vide.
- **Recalcul sur les sorties brutes** (`stats_sorties.py`, `budget_check.py`) :
  - 138 points ; à marge nominale, $V=0$ partout ; $V'$ : 618 au total, au plus 156 sur $10^5$, en 25 points ; les classes « sous » partout ;
  - sans marge, 137 « au-dessus » et 1 « non concluant » (le point n° 31) ; fréquence minimale 0,866, médiane 0,970 : « at least 0.86 (median 0.97) » est exact ;
  - 137 bissections valides : $\varepsilon/\varepsilon_{\mathrm{emp}}$ de 1,7504 à 3,5556, médiane 2,4854, soit « 1.75 to 3.56, median 2.49 » ✓ ;
  - économie de 0,0194 à 0,5745, médiane 0,1052, soit « 2 % à 57 %, médiane 10,5 % » ✓ ; recalculée par la forme close de $B^\star_{\mathrm{unif}}$, elle concorde avec le champ des sorties à $10^{-6}$ près ;
  - $c$ et $\varepsilon$ recalculés : écart relatif inférieur à $3\times10^{-15}$ ;
  - la borne d'inflation `eq:audit-inflation` tient en chacun des 138 points.
- **Audit exact par programmation dynamique, refait de mon côté** (`dp_exact.py`) : 32 points à mémoire entière ; probabilité exacte de franchissement à marge nominale au plus $2{,}67\times10^{-7}$ ; 0,096 franchissement attendu au total. Sans marge, les fréquences de la course concordent avec la valeur exacte (écart réduit maximal 2,04). C'est conforme au § 8 du verdict.
- **Formulations conformes au verdict** :
  - « confirmed in 137, inconclusive in 1, not contradicted », motif de sensibilité à la tolérance compris ;
  - « predictions and reading criteria fixed before any draw » : le préenregistrement est scellé avant l'essai de fonctionnement, et l'erratum ne change que deux valeurs des bancs témoins ;
  - la clause finale de non-portée (ni preuve, ni hors grille, ni boucle fermée, ni actions échantillonnées), fidèle au § 10 du verdict.
- **Marge et budget.** La remarque ne les confond pas : elle les distingue explicitement. Les réserves sur ce point sont celles de D5 et D6 : oracle, niveau $\delta/2$ sans plafond, $B_\varepsilon$ plutôt qu'audits réservés, nécessité « par construction ».

### Insertion

- Aucun label en double ni renvoi pendant.
- Les macros `\Prob` et `\Var` existent dans le manuscrit.
- Une fois D2 corrigé, la section compile sans erreur dans le manuscrit de base ; seules ses 21 clés de citation restent indéfinies (D7).
- Le modèle de la section est compatible avec le modèle à trois strates : l'abandon de la strate visible est exact pour le rapport des logits (D1), et le régime R3 se retrouve comme cas statique de `prop:audit-indist`.
