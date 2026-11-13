# Rapport de lecture — H2, pièces versées et jamais lues contre elle — v1

- **Date et heures (relevées par `date -u`)** : début 2026-11-13 23:36:46 UTC ; rédaction commencée 2026-11-13 23:46:00 UTC ; l'heure de scellement figure dans le compagnon `.sha256`.
- **Rôle** : lecteur. **Modèle** : modèle A.
- **Mandat** : verdict d'antériorité sur H2 (énoncé de N-007) par lecture des pièces de la section 5 de la contre-lecture du niveau 3 (ligne « H2, conjonction ») et contrôle du constat m6 (date de l'annonce du séquentiel dans NARCBench).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme).
- **Citations contrôlées** : 70, **0 échec** (script et sortie dans l'archive). Tout extrait anglais entre guillemets ci-dessous figure dans `citations-H2-v1.json` (titres compris).
- **Ouverture fautive** : aucune. **Refus** : aucun.

## 0. Verdict en tête

- **Aucune occupation de la conjonction (f) dans les six pièces lues.**
- **Occupations partielles, déjà connues ou génériques** :
  - 2110.00115 (Choe et Ramdas) fournit, comme **outil générique**, les composantes (a) accumulation additive et (b) garantie toujours valide **pour tout score borné** (p. 1, 17, 32) ; non appliqué à des sondes, à des agents ni à des moniteurs : outil classique à citer, pas une occupation de la conjonction.
  - NARCBench (2604.01151) tient (c) sondes et (d) agent qui agit (déjà au dossier) ; il **annonce** (a) et (b) sur ces sondes **depuis la version 2 du 9 mai 2026** (p. 8 et 9), sans jamais le faire dans les versions 1, 2 et 4 lues.
- **Verdict d'ensemble sur H2 (table fermée)** : **occupé en partie** — chaque morceau a un titulaire ou un outil ; la conjonction reste **non trouvée dans les pièces lues**. Les six pièces ne déplacent pas le verdict du niveau 3 ; elles le précisent (outil à citer, annonce datée).
- **m6 confirmé et complété** : version 1 (1er avril 2026) sans aucune mention du séquentiel ; version 2 (9 mai 2026) l'annonce deux fois (p. 8 et p. 9, la p. 8 n'était pas relevée) ; version 4 (12 octobre 2026) l'annonce quatre fois (p. 3, 18, 19, 26) et pose un cadre formel où le moniteur décide sur l'historique des signaux de sondes (p. 10-11), mais les agents n'y sont sondés qu'au début et à la fin (p. 11).

## 1. Fichiers lus et étendue

Fichiers du dépôt (aux lignes indiquées seulement) :
- `docs/programme-controle-ia-v2.md`, lignes 85-125 et 180-200 ;
- `docs/decisions/decision-N-007-N-008-v1.md`, lignes 1-56 ;
- `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 62-94 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 100-136 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 838-875, puis `grep -n 'm6'` sur ce seul fichier (il affiche les lignes 139, 785 et 897) et la seule section m6 (lignes 785-821) ;
- la consigne commune et `interdits-communs-v2.md` (nommé par la consigne), en entier.

PDF (dossier de pièces hors dépôt ; empreintes vérifiées contre les compagnons `.sha256`, toutes conformes) :

| fichier | sha256 | pages | étendue lue |
|---|---|---|---|
| `lot8/2501.03982v5.pdf` | `e40c11311e785508a78953d87c5004be05b42e44a8277545b51c29886a3e96f1` | 26 | en entier, ligne à ligne, annexes et preuves comprises |
| `lot10/2103.08402v3.pdf` | `2e259a65ddca593a95dbe014297f4bdf3d9ceb25cbe6f551fc6230d62c8de886` | 26 | p. 1-22 ligne à ligne ; p. 23-26 (figures d'annexe) parcourues, sans texte hors étiquettes d'axes |
| `lot10/2110.00115v6.pdf` | `fd87e23a30c6657fd8dd272f671d0bd8a3aa469f5aafbec85a00bb9501764286` | 61 | en entier, ligne à ligne, annexes A à I comprises |
| `lot10/2604.01151v1.pdf` | `ca9a8623307849be9df9f905086ea4c499f09c1a20208bcc4ed969e420eb08b3` | 11 | en entier, ligne à ligne |
| `lot10/2604.01151v2.pdf` | `ba39580b0e05b948e5cc8102ba8fb9209b810aff1b07b4d42b86276413ea0f40` | 29 | par mots sur les 29 pages ; en entier p. 1, 8, 9 ; passages p. 4, 11, 23 |
| `lot10/2604.01151v4.pdf` | `6d7c29a6b72c65ac53b018b9798b4f0f9eca2d8978ebb4faebec6276338cd650` | 47 | par mots sur les 47 pages ; en entier p. 1-3, 6, 7, 10-13, 18, 19, 26 ; passages p. 4-5, 14-17, 20, 22, 24, 25, 46-47 |

Mots cherchés dans NARCBench (toutes pages) : sequential, accumulat, anytime, always valid, optional stop, stopping, martingale, e-value, e-process, SAVI, Ville, cusum, over time, across turns, across rounds, multi-turn, temporal, horizon, cumulative, Howard ; puis threshold, recall at, 1% FPR, rounds, final-round, average.

## 2. L'énoncé confronté (N-007, l. 28 ; lecture de « toujours valide », l. 30-34)

Sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de faux positifs, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le sabotage avec un rappel qui croît avec l'horizon ; contexte privé compris ; seuil calibré sur des épisodes honnêtes, sans exemple de sabotage ; « toujours valide » lu comme uniforme sur toutes les lectures de l'horizon de l'épisode, calibré sur épisodes honnêtes entiers (N-007, l. 31-32).

Composantes : (a) accumulation additive dans le temps ; (b) garantie toujours valide ; (c) scores de sondes ; (d) de l'agent qui agit ; (e) sous un moniteur par action à 1 % ; (f) la conjonction.

## 3. Article par article

### 3.1 2501.03982v5 — Koning et van Meer, « Anytime Validity is Free: Inducing Sequential Tests »

**Venue imprimée** : prépublication arXiv, math.ST, version 5 du 21 décembre 2025 ; date de tête « December 23, 2025 » (p. 1). Remerciements à deux rapporteurs anonymes (p. 17) ; aucune revue nommée.

**Ce qu'il fait.**
- Résultat principal : « for any valid test based on N observations, we show how to construct an anytime valid sequential test that matches it after N observations » (p. 1). Le test séquentiel induit est l'espérance conditionnelle, sous l'hypothèse nulle, du test terminal (p. 2 et théorème 1, p. 5 ; martingale de Doob). Formule, lue sur le PDF, non contrôlée par programme : φ′ₙ = E_P[φ_N | Xⁿ] (p. 2, éq. 5 p. 5).
- La construction est « à rebours » et s'oppose explicitement à l'accumulation : « This is different from the 'forward' construction that is common in the literature, which relies on designing martingale-increments and sequentially accumulating these. » (p. 4).
- Hypothèses composites (théorème 2, p. 6), rapport de vraisemblance monotone (théorème 3, p. 8), test z et test t séquentialisés (sections 3 et 4, p. 8-11), continuation optionnelle (théorèmes 4 et 5, p. 12), lien avec les e-valeurs et le test séquentiel du rapport de probabilités (sections 6.1-6.3, p. 14-16).
- Dans l'exemple du test z (p. 9), le test induit est une fonction de la somme courante des observations, pour des données « are independently drawn from the normal distribution » (p. 8) : additif dans cet exemple seulement. Formule, lue sur le PDF, non contrôlée : Φ((N^(−1/2) Σᵢ≤ₙ xᵢ/σ − z₁₋α)/√rₙ), rₙ = (N − n)/N (p. 9, éq. 6).
- Chiffres (auteurs, p. 2) : dans un cas normal (μ = 0 contre μ = 0,3, N = 100), le test z rejette avec probabilité 91 %, le test séquentiel du rapport de probabilités 79 % (47 % s'il apprend l'alternative) ; le test induit coïncide avec le test z au temps N.

**Ce qu'il ne fait pas.** Aucune donnée réelle ; aucun moniteur, aucune sonde, aucun agent, aucun modèle de langue (recherche par mots sur les 26 pages : aucune occurrence). Pas de détecteur de rupture.

**Limites reconnues.** Le test induit exige une loi nulle spécifiée et, faute de forme close, « one may have to resort to numerical approximations » (p. 6, remarque 4). Les auteurs écrivent : « we do not advocate for everyone to use sequential tests induced from classical Neyman-Pearson-style tests » (p. 16), car ces tests sont mesurés à un temps fini N, « so that they do not naturally continue beyond this time » (p. 16).

**Incohérences, résultats trop beaux** : aucun relevé ; le titre (« gratuit ») vaut pour la puissance au seul temps N, ce que le texte dit (remarque 10, p. 12).

**Verdict par composante.**
- (a) accumulation additive : **voisin** (outil) ; la construction générale n'est pas une accumulation (p. 4), l'exemple du test z l'est (p. 9).
- (b) garantie toujours valide : **outil générique à citer** — tout test valide à horizon fixe induit un test toujours valide sur l'horizon (théorème 1, p. 5). C'est exactement la lecture de N-007 (« uniforme sur toutes les lectures de l'horizon de l'épisode »), **à condition de spécifier la loi nulle des scores honnêtes** (p. 2, p. 6).
- (c), (d), (e) : **ne touche pas**.
- (f) conjonction : **ne touche pas**.

**Ce qu'il apporte à H2 (analyse du lecteur).** Au temps terminal, la version séquentielle d'un test à horizon fixe a exactement sa puissance (p. 1, p. 5) : le gain revendicable d'une accumulation toujours valide ne peut donc pas être une puissance supérieure au meilleur test à horizon fixe lu en fin d'épisode ; il se mesure en latence (alerte plus tôt) ou contre d'autres agrégations. Cela rejoint le contre-indice déjà versé (2607.02510 : un seuil unique calibré égale un test séquentiel).

### 3.2 2103.08402v3 — Henzi et Ziegel, « Valid sequential inference on probability forecast performance »

**Venue imprimée** : arXiv, stat.ME, version 3 du 1er juillet 2022 ; date de tête July 4, 2022 (p. 1). Publication à Biometrika 2022, 109(3), selon la bibliographie de 2110.00115 (p. 29) ; le PDF lu ne l'imprime pas.

**Ce qu'il fait.**
- E-valeurs pour tester la dominance d'une prévision probabiliste d'un événement binaire sur une autre, sous une règle de score (théorèmes 3.1-3.3, p. 5-6). Formule, lue sur le PDF, non contrôlée : E(y) = 1 + λ (S(p, y) − S(q, y)) / |S(p, 1{p > q}) − S(q, 1{p > q})| (p. 6, éq. 6).
- Accumulation **multiplicative** : « e-values from different time points can be merged by products into a non-negative supermartingale or test-martingale » (p. 2) ; produit additif en logarithme seulement.
- Garantie : « The e-values proposed in this article are valid in finite samples without any assumptions on the data generating processes. » et « They also allow optional stopping » (p. 1) ; validité au temps d'arrêt (proposition 3.5, p. 8).
- Nulle **forte** : la dominance conditionnelle à chaque instant ; « they require conditional dominance at all time points » (p. 4).
- Simulations (p. 9-11) et cas réel sur la pluie à quatre aéroports (p. 12-16, tableaux 2 et 3) ; « Even if the score differences are only small, evidence eventually accumulates over the whole time period » (p. 15).
- Chiffre (auteurs, p. 3) : des tests usuels au niveau 0,05 « may yield rejection rates of up to 0.15 under optional stopping » ; 0,12 dans l'exemple de la p. 10 (figure 1a, auteurs).

**Ce qu'il ne fait pas.** Aucune application à un moniteur, une sonde, un agent ou un modèle de langue (recherche par mots : aucune occurrence). Le cadre exige un **résultat observé** Y à chaque pas pour noter la prévision ; dans H2, l'étiquette de sabotage n'est pas observée en ligne : le cadre ne se transpose pas directement aux scores de sondes (analyse du lecteur).

**Limites reconnues.** « The advantages of e-values for forecast comparison relative to the currently available methods come at a price, namely, lower power. » (p. 3) ; décalage h > 1 moins puissant (p. 11, p. 15).

**Verdict par composante.** (a) **voisin** (accumulation multiplicative de e-valeurs) ; (b) **outil voisin** (e-valeurs à arrêt optionnel, sous une nulle forte et avec résultats observés) ; (c), (d), (e), (f) **ne touche pas**.

**Contre-indice faible, pour la forme de H2.** Il chiffre le prix en puissance d'une garantie toujours valide (p. 3, p. 10) ; à rapprocher de 2501.03982, qui montre que ce prix n'existe pas au temps terminal quand la loi nulle est spécifiée (§ 3.1). Les deux constats ne se contredisent pas : ils portent sur des cadres différents (nulle sans hypothèse de loi contre nulle spécifiée).

### 3.3 2110.00115v6 — Choe et Ramdas, « Comparing Sequential Forecasters »

**Venue imprimée** : arXiv, stat.ME, version 6 du 9 novembre 2023 ; date de tête November 10, 2023 ; le PDF indique en note de bas de page la publication à Operations Research (p. 1).

**Ce qu'il fait.**
- Suites de confiance et e-processus pour la différence moyenne, variable dans le temps, entre les scores de deux prévisionnistes ; « Our methods do not make distributional assumptions on the forecasts or outcomes » et « our main theorems apply to any bounded scores » (p. 1).
- Accumulation **additive** : l'e-processus du théorème 3 (p. 17) est l'exponentielle d'une somme de différences de scores bornées, corrigée d'un temps intrinsèque de variance. Formule, lue sur le PDF, non contrôlée : E_t(λ) = exp{λ Σᵢ≤ₜ δ̂ᵢ − ψ_E,c(λ) V̂_t}, V̂_t = Σᵢ≤ₜ (δ̂ᵢ − γᵢ)² (p. 17, éq. 24) ; mélange en λ (p. 14-15, p. 34-36).
- Garantie : « we define safe, anytime-valid inference (SAVI) methods as ones that satisfy either the time-uniform coverage guarantee (CS) or the anytime-valid guarantee (e- or p-processes) » (p. 4) ; l'e-processus « quantifies the amount of accumulated evidence against the null up to time t » (p. 4).
- Lemme général (annexe A.1, p. 32) : la surmartingale vaut pour toute suite de variables bornées inférieurement, soit toute suite « be any process whose conditional means » existent, centrée sur ses moyennes conditionnelles.
- Nulle **faible**, sur la moyenne : « whether one forecaster outperforms another on average (rather than always) » (p. 1) ; formule, lue sur le PDF, non contrôlée : H₀ʷ : Δ_t = (1/t) Σᵢ≤ₜ δᵢ ≤ 0 pour tout t (p. 16, éq. 18).
- Expériences : simulations non stationnaires à ruptures (p. 18-22), base-ball 2010-2019, T = 25 165 (p. 23-24, tableau 4), pluie (p. 24-26, figure 5), décalages (annexe E, tableau 5 p. 47).
- Chiffres (auteurs) : l'intervalle à horizon fixe perd sa couverture uniforme, « the fixed-time CI is only valid at a fixed time t and not uniformly over time, despite its tighter width » (p. 20) ; les tests classiques dépassent α = 0,05 en erreur cumulée « after roughly 100 and 1000 steps, respectively » (p. 54, figure 7).

**Ce qu'il ne fait pas.** Aucun moniteur, aucune sonde, aucun agent, aucun modèle de langue (recherche par mots sur les 61 pages : le mot monitor n'y désigne que la surveillance continue d'une suite statistique, p. 1, 3, 17). Aucun seuil par action, aucun calibrage sur épisodes.

**Limites reconnues.** Scores bornés exigés pour les théorèmes non asymptotiques (p. 13-14, p. 26) ; « Deriving a fully general anytime-valid procedure for unbounded domains and scoring rules remains an open problem. » (p. 51) ; conclusions descriptives : « the inferential conclusions drawn from our methods need not extrapolate to future time steps » (p. 27).

**Incohérences, résultats trop beaux.** Taux de non-couverture « toujours nul » pour les suites non asymptotiques (p. 20-21, figure 3) : conservatisme attendu d'une surmartingale, que les auteurs disent eux-mêmes ; pas une réserve.

**Verdict par composante.**
- (a) accumulation additive : **faite comme outil générique** (p. 17, p. 32).
- (b) garantie toujours valide : **faite comme outil générique**, sans hypothèse de loi, pour tout score borné (p. 1, p. 4, p. 17).
- (c), (d), (e) : **ne touche pas**.
- (f) : **ne touche pas**. Conformément au mandat : outil classique à citer, non une occupation de la conjonction.

**Ce qui pèse sur H2 (analyse du lecteur, à tenir au préenregistrement de G1).**
1. La nulle est une borne sur les **moyennes conditionnelles** pas à pas. Sous un effet épisode (un épisode honnête dont le niveau moyen de sonde est plus haut), la nulle est fausse pour cet épisode honnête : l'e-processus le « rejette » à bon droit statistique, ce qui fait une fausse alarme du point de vue du programme. Cela rend compte du constat de T0.3 cité par N-007 (avec le seul seuil de Ville, 0,21 à 0,35 au lieu de 0,05 en simulation sous effet épisode ou corrélation, N-007 l. 33) et confirme qu'il faut une garantie calibrée sur épisodes honnêtes entiers, non la seule garantie de l'e-processus.
2. Sur une nulle de moyenne, l'e-processus redescend quand le signe s'inverse (p. 20, figure 3) : un sabotage concentré sur une part de la trajectoire est dilué par les passages honnêtes (rejoint 2603.13791, dilution, déjà au dossier).
3. Des scores de sondes non bornés (logits) demandent un écrêtage ou la suite asymptotique (annexe C, p. 37-38).

### 3.4 NARCBench (2604.01151), « Detecting Multi-Agent Collusion Through Multi-Agent Interpretability » — versions 1, 2 et 4

**Ce que fait l'article, toutes versions.** Une direction de tromperie apprise par sonde linéaire sur les activations de chacun des agents en collusion (agents qui agissent), puis des statistiques de groupe sur les scores par agent : « propose five probing techniques that aggregate per-agent deception scores to classify scenarios at the group level » (v1, p. 1). Quatre agents, deux en collusion, comité ou tâches de transfert ou partie de cartes à signaux cachés.

**Version par version, sur la lecture séquentielle, l'accumulation dans le temps, la garantie toujours valide, l'arrêt optionnel.**

| version | date imprimée | ce qui est écrit | pages |
|---|---|---|---|
| v1 | tampon arXiv « 1 Apr 2026 » (p. 1, marge) ; aucune autre date | **rien** sur le séquentiel, l'accumulation de scores, la garantie toujours valide ou l'arrêt optionnel (le seul « Multi-Turn Interactions » est dans un titre de référence, p. 10). Agrégation dans le temps : activations **moyennées** sur les tours pour le comité (« we average each agent's activations across all discussion rounds to capture their sustained representation of the shared deliberation », p. 5) ; dernier tour seul ailleurs (« we use final-round activations only (the last round where all agents receive identical user prompts) », p. 5). Le maximum par agent est dit fragile parce que « colluding agents could coordinate to keep individual scores below a detection threshold » (p. 6) : seuil entre agents, non dans le temps. | 1, 5, 6, 9, 10 |
| v2 | tampon arXiv « 9 May 2026 » (p. 1) ; aucune autre date | **Annonce, deux fois, sans résultat.** p. 8 : rappel de « even the best method (Deception Split) achieves only 0.38 recall at 1% FPR » sur le transfert (auteurs), puis la lecture séquentielle, « accumulating evidence across interactions via SAVI [Howard et al., 2022] for example », « is a natural next step ». p. 9 : « Sequential detection. Accumulating evidence across multiple interactions [Kulkarni, 2026], via SAVI [Howard et al., 2022] for example, would yield formal stopping guarantees. » Méthode inchangée : « we average across all discussion rounds » pour le comité, « we use final-round activations only, where all agents receive identical user prompts » ailleurs (p. 4). | 4, 8, 9, 11, 23 |
| v4 | tampon arXiv « 12 Oct 2026 » (p. 1) ; aucune autre date | **Annonce, quatre fois, sans résultat, et cadre formel.** p. 3 : « Multi-turn extensions of our detection setting call for sequential detection machinery » (cite Ramdas et al. 2023, Xie et Siegmund 2013, Wen et al. 2024, Nasvytis et al. 2024). p. 18 : « One-shot detection at strict » [légende de figure intercalée] « thresholds is therefore insufficient for structural collusion. » ; « Sequential detection that accumulates evidence across inter » (mot coupé en fin de ligne, suite « actions », avec la légende intercalée ; cite Wald 1945, Ramdas et al. 2023, Xie et Siegmund 2013) « is a natural next step ». p. 19 : « Future work will explore principled sequential detection techniques ». p. 26 : « Accumulating evidence across multiple interactions (Kulkarni, 2026), via SAVI (Howard et al., 2021) for example, would yield formal stopping guarantees. » Cadre HELIOS (p. 10-11) : « Local sensors can be external (local monitors) or internal (probes). » (p. 10) et le moniteur central « E bases its decision rule on its own aggregated history » des signaux (p. 11) ; mais « Finally, agents are only probed just after the initial prompt and at the end of the period. » (p. 11). Tests de rapport de vraisemblance généralisé à un instant, au niveau α sous un modèle nul des scores (p. 15-17, 46-47). | 1, 3, 10, 11, 18, 19, 26 |

Les mots anytime, e-process, e-value, martingale et Ville n'apparaissent dans aucune version hors d'un titre de référence de v4 (« Game-theoretic statistics and Safe Anytime-Valid Inference », p. 24). Le sigle SAVI n'est développé dans aucune version lue ; son sens est celui de 2110.00115 (p. 4).

**Ce qui touche à H2 au-delà de l'annonce.**
- Menace diffuse sans accumulation : la famille de transfert de v2 intitulée « News Framing (gradual narrative drift) » décrit une dérive où « Each individual contribution is defensible in isolation » ; « This is the only Transfer family with iterated public contributions that build on each other. » (p. 23). Elle est lue sur le **dernier tour seul** (p. 4) : c'est la base (iii) de N-007, « sonde sur le dernier état seul ».
- Seuil à 1 % : v2 p. 8 et v4 p. 18 rapportent le rappel à 1 % de faux positifs **par scénario** (0,38 au mieux sur le transfert, auteurs ; 1,00 sur la partie de cartes, auteurs), non un moniteur par action ; aucune condition « chaque action sous le seuil ».
- Menace : collusion de plusieurs agents, non sabotage d'un agent seul ; l'annonce est toutefois générale (« across multiple interactions »).

**Limites reconnues.** v1 : « The adversarial robustness of these techniques is untested » (p. 9) ; v2 : « Adversarial robustness is untested. » (p. 9) ; v4 : une expérience restreinte de conscience d'évaluation (annexe H, annoncée p. 26), un résultat voisin cité, « fixed-threshold recall can drop sharply » (p. 3).

**Incohérence relevée (mineure).** v2 cite « Howard et al., 2022 » (p. 9) et date 2022 l'article des Annals of Statistics 49(2) (« Time-uniform, nonparametric, nonasymptotic confidence sequences », p. 11) ; v4 et 2110.00115 le datent 2021 (v4 p. 22 ; 2110.00115 p. 29).

**Verdict par composante (versions 1, 2, 4).**
- (a) accumulation additive : **annoncée, non faite**, à partir de v2 (p. 8, 9) ; v1 et v2 font une moyenne d'activations sur les tours (non des scores, sans garantie) ; v4 ne sonde qu'au début et à la fin (p. 11).
- (b) garantie toujours valide : **annoncée, non faite** (« would yield formal stopping guarantees », v2 p. 9, v4 p. 26).
- (c) sondes : **faite** (v1 p. 1, 5).
- (d) agent qui agit : **faite** (sondes sur les agents en collusion eux-mêmes, v1 p. 5).
- (e) moniteur par action à 1 % : **voisin** (rappel à 1 % par scénario, v2 p. 8, v4 p. 18).
- (f) conjonction : **non faite** ; **annoncée depuis le 9 mai 2026**.
- Verdict d'ensemble pour NARCBench : **occupe en partie** ((c), (d)) ; **annonce sans résultat** de (a) et (b) sur sondes d'agents.

### 3.5 Contrôle du constat m6

- Absence du mot sequential dans la version 1 (1er avril 2026) : **confirmée** par recherche sur les 11 pages et lecture intégrale.
- « la version 2 (9 mai 2026) écrit, p. 9, … » : **confirmé**, citation exacte contrôlée.
- **Complément** : v2 l'annonce aussi p. 8, en lien avec le rappel de 0,38 à 1 % de faux positifs ; v4 (12 octobre 2026) l'annonce p. 3, 18, 19 et 26 et pose le cadre formel p. 10-11. Le texte corrigé de m6 (« son annonce du séquentiel figure dès la version 2 du 9 mai 2026 (p. 9…) ») tient ; il gagne à citer aussi la p. 8. Versions 3 et 5 non lues dans ce mandat.

## 4. Table de synthèse

| source | (a) additive | (b) toujours valide | (c) sondes | (d) agent qui agit | (e) moniteur par action 1 % | (f) conjonction | verdict |
|---|---|---|---|---|---|---|---|
| 2501.03982v5 | voisin (p. 4, 9) | outil générique (p. 1, 5) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | ne touche pas ; outil à citer |
| 2103.08402v3 | voisin, multiplicative (p. 2, 7) | outil voisin, nulle forte, résultats observés (p. 1, 4, 8) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | ne touche pas |
| 2110.00115v6 | outil générique (p. 17, 32) | outil générique, tout score borné (p. 1, 4, 17) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | voisin ; outil à citer pour (a) et (b) |
| 2604.01151 v1 | non (moyenne d'activations, p. 5) | non | faite (p. 1, 5) | faite (p. 5) | non | non | occupe en partie ((c), (d)) |
| 2604.01151 v2 | annoncée (p. 8, 9) | annoncée (p. 9) | faite | faite | voisin, par scénario (p. 8) | non faite, annoncée | occupe en partie ; annonce datée du 9 mai 2026 |
| 2604.01151 v4 | annoncée (p. 3, 18, 26) ; cadre formel (p. 10-11) | annoncée (p. 26) | faite | faite | voisin, par scénario (p. 18) | non faite, annoncée | occupe en partie ; annonce maintenue au 12 octobre 2026 |

**Verdict d'ensemble sur H2, table fermée : occupé en partie** (la conjonction : non trouvée dans les pièces lues).

## 5. Ce qui reste revendicable (formulation exacte)

« La conjonction de l'énoncé N-007 — accumulation additive à garantie uniforme sur l'horizon de l'épisode, calibrée sur des épisodes honnêtes entiers sans exemple de sabotage, de scores de sondes lues sur l'agent qui agit, contexte privé compris, sur des trajectoires dont chaque action sabotée reste sous un moniteur par action calibré à 1 %, avec un rappel mesuré en fonction de l'horizon — n'est réalisée dans aucune des six pièces lues ; l'outil statistique (accumulation additive toujours valide d'un score borné) est publié et se cite (2110.00115 ; 2501.03982 pour la garantie sur un horizon fini), et la lecture séquentielle de sondes d'agents est annoncée sans résultat par l'équipe de NARCBench depuis la version 2 du 9 mai 2026. »

Les résultats revendicables portent sur la mesure (le rappel en fonction de l'horizon sous la condition « sous le seuil par action », le gain contre les bases (ii) et (iii) de N-007), non sur l'outil.

## 6. Ce qu'une phrase publique sur H2 ne doit pas affirmer

- Que l'accumulation additive toujours valide de scores est nouvelle, ou qu'elle est apportée par le programme : elle est publiée pour tout score borné (2110.00115, p. 1, 17, 32).
- Que la garantie de l'e-processus donne à elle seule un taux de fausses alarmes ≤ α sur des épisodes honnêtes : sa nulle porte sur les moyennes conditionnelles pas à pas (2110.00115, p. 16-17) ; sous effet épisode, elle ne tient pas (constat de T0.3 rappelé par N-007, l. 33).
- Que la garantie toujours valide « coûte » nécessairement de la puissance, ou qu'elle « apporte » de la puissance en fin d'épisode : au temps terminal, le test induit égale le test à horizon fixe (2501.03982, p. 1, 5) ; le prix existe dans d'autres cadres (2103.08402, p. 3).
- Que personne n'a envisagé la lecture séquentielle de sondes d'agents : NARCBench l'annonce depuis le 9 mai 2026 (v2, p. 8-9) et la maintient au 12 octobre 2026 (v4, p. 3, 18, 19, 26).
- Que NARCBench ne lit qu'un instant par principe : v4 pose un cadre où le moniteur décide sur l'historique des signaux de sondes (p. 10-11), même si ses expériences ne sondent qu'au début et à la fin (p. 11).
- Que la zone est « vide » : « non trouvée dans les pièces lues » seulement (R8) ; l'annonce datée rend la zone exposée.

## 7. Voisins nommés dans les pièces et non lus (page où ils sont nommés)

- Das et al. 2026, « You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring » — cité v4 p. 3 (résultat sur le rappel à seuil fixe), référence p. 20 ; titre contrôlé sur le fragment « Evaluation Awareness and Multi-Agent Monitoring » (p. 20).
- Shi et al. 2026, « Emergent collusion in long-horizon llm agent interaction » (arXiv 2609.24967) — v4 p. 18 (environnement nommé Verdict, dix tours, sondes non cumulées), référence p. 24.
- Xie et Siegmund 2013, « Sequential multi-sensor change-point detection » — v4 p. 3 et 18, référence p. 25.
- Wen et al. 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » — v4 p. 3, référence p. 25 (déjà au dossier sous 2411.17693, voisin avec réserve).
- Nasvytis et al. 2024 (détection hors distribution en apprentissage par renforcement) — v4 p. 3, référence p. 23.
- Ramdas et al. 2023, « Game-theoretic statistics and Safe Anytime-Valid Inference » — v4 p. 3 et 18, référence p. 24 (synthèse statistique, outil).
- Kulkarni 2026, « Latent adversarial detection: Adaptive probing of LLM activations for multi-turn attack detection » (2604.28129) — v2 p. 9, v4 p. 26 ; déjà lu au niveau 2 (occupe en partie).
- Howard et al. 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences » — v2 p. 9 et 11, v4 p. 26 ; 2110.00115 p. 3, 6 ; outil statistique.
- Versions 3 et 5 de 2604.01151 : non lues dans ce mandat (lues par C1 selon m6).
- Dans 2110.00115 : Arnold, Henzi et Ziegel 2023 (calibrage séquentiel de prévisions, p. 26, 28) ; Johari et al. 2022 (surveillance continue de tests A/B, p. 4, 30) ; Waudby-Smith et al. 2021 (suites de confiance asymptotiques, p. 19, 37) — outils, hors du champ des moniteurs.

## 8. Réserves (R4, R8)

- Lecture par mots pour v2 et v4 : une lecture séquentielle effectuée hors des mots cherchés (par exemple sous un autre vocabulaire, dans une annexe d'expérience) pourrait m'avoir échappé ; les pages des expériences sur plusieurs tours de v4 (p. 18, annexe M annoncée) ont été vérifiées par mots seulement.
- Le verdict « occupé en partie » est stable mais non « propre » : l'outil (a)+(b) est public et l'annonce de NARCBench est datée ; une version 5 ou ultérieure, ou un travail de la même équipe, peut occuper la conjonction à tout moment. Exposition jugée **moyenne à forte** (la contre-lecture disait « moyenne »).
- Les points d'analyse marqués « analyse du lecteur » (§ 3.1, 3.3) sont des déductions sur la portée des théorèmes, non des énoncés des auteurs.
