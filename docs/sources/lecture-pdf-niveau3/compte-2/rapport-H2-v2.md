# Rapport de lecture — H2, pièces versées et jamais lues contre elle — v2

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Rapport remplacé** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H2-v1.md`, sha256 `340319248d4cd878b219790258f1f13515d38b9a3d30e7611c824a1d44da08f3` (non modifié) ; son archive `fichiers-de-travail-H2-v1.tar`, sha256 `32c291fa903f71b4781269307befb61858a91015f13e966ba950d3fc780fc88a`.
- **Contre-lecture intégrée** : `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-H2-v1.md`, sha256 `708b48c23f0e116071c05edca5075c97a10306f0dbc08b2dcff5f13471bf1def` (vérifiée) ; son archive `fichiers-de-travail-contre-lecture-H2-v1.tar`, sha256 `47171de8d4ccc83fc26c66443653960c618db09ae49f7dc985903779a4a55f07` (vérifiée, extraite dans un sous-dossier neuf du dossier de travail, lue comme une donnée).
- **Date et heures (relevées par `date -u`)** : première lecture 2026-11-13 23:36:46 UTC ; reprise pour la version 2 le 2026-11-14 à 00:01:20 UTC ; rédaction de la version 2 commencée après 00:05:46 UTC ; l'heure de scellement figure dans le compagnon `.sha256`.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme), tous interdits tenus.
- **Citations contrôlées** : 126, **0 échec** (`citations-H2-v2.json`, dans l'archive seulement). Tout extrait anglais entre guillemets ci-dessous, titres compris, y figure tel quel.
- **Ouverture fautive** : aucune. **Refus** : aucun.

## 0. Verdict en tête

- **Verdict sur H2, table fermée : occupé en partie.** La conjonction (f) de l'énoncé de N-007 est **non trouvée dans les six pièces lues**. Le contre-lecteur rend le même verdict.
- **Occupations, même partielles :**
  - **NARCBench (2604.01151)** occupe (c) sondes et (d) agent qui agit. Il est **plus près de (a) que la version 1 de ce rapport ne le disait** : la version 4 lit les sondes à chacun des dix tours d'un environnement de collusion émergente, chaque tour classé seul (p. 18) ; les versions 1 et 2 calculent un score de sonde par agent et par main, testé sur 39 mains regroupées (v1 p. 8 ; v2 p. 28). **Aucune de ces lectures n'est une accumulation au sein d'un épisode, aucune ne porte de garantie toujours valide, aucune ne donne de courbe selon le nombre de tours.** L'accumulation et la garantie sont **annoncées** depuis la version 2 du 9 mai 2026, jamais faites dans les versions 1, 2 et 4 (lues en entier pour cette version 2 du rapport).
  - **L'outil statistique** (accumulation additive à garantie toujours valide d'une suite bornée) est publié : lemme de Howard et collègues (2020), non lu, dont 2110.00115 donne l'extension (proposition 1, p. 32). Les théorèmes principaux de 2110.00115 portent sur des différences de règles de score de prévisions, non sur des scores de détecteur. C'est un outil à citer, non une occupation de la conjonction.
- **Exposition : forte** (relevée de « moyenne à forte ») : l'équipe de NARCBench a le matériau (scores de sondes par tour), annonce la lecture séquentielle et nomme elle-même le cas d'un agent seul qui se coordonne avec lui-même dans le temps comme hors de son cadre actuel (v4 p. 7, note 3).
- **Suite donnée à la contre-lecture** : onze constats, lettres A à K ; dix « corrigé », un « réserve maintenue » (E, sur la généralité d'une formule ; les corrections de fond de E sont faites). Section 3.

## 1. Fichiers lus et étendue

Fichiers du dépôt, aux lignes indiquées seulement (inchangé depuis la version 1, plus deux fichiers de la contre-lecture) :
- `docs/programme-controle-ia-v2.md`, lignes 85-125 et 180-200 ;
- `docs/decisions/decision-N-007-N-008-v1.md`, lignes 1-56 ;
- `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 62-94 (nommé par mon premier mandat) ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 100-136 ;
- `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 838-875, et la section m6 (lignes 785-821), repérée par le `grep -n 'm6'` que mon premier mandat prescrivait (il a affiché les lignes 139, 785 et 897) ;
- la consigne commune et `interdits-communs-v2.md` (nommé par la consigne) ;
- pour la version 2 : `contre-lecture-rapport-H2-v1.md` (215 lignes, en entier) et l'archive de la contre-lecture (journal, JSON, scripts, sorties), extraite hors du dépôt.

PDF (dossier de pièces hors dépôt ; empreintes vérifiées contre les compagnons `.sha256`, toutes conformes) :

| fichier | sha256 | pages | étendue lue (versions 1 et 2 du rapport cumulées) |
|---|---|---|---|
| `lot8/2501.03982v5.pdf` | `e40c11311e785508a78953d87c5004be05b42e44a8277545b51c29886a3e96f1` | 26 | en entier, ligne à ligne ; p. 2-4 et 12 relues pour la version 2 |
| `lot10/2103.08402v3.pdf` | `2e259a65ddca593a95dbe014297f4bdf3d9ceb25cbe6f551fc6230d62c8de886` | 26 | p. 1-22 ligne à ligne ; p. 23-26 (figures) parcourues |
| `lot10/2110.00115v6.pdf` | `fd87e23a30c6657fd8dd272f671d0bd8a3aa469f5aafbec85a00bb9501764286` | 61 | en entier, ligne à ligne ; p. 1, 11, 16-20, 26, 29, 32, 38 relues pour la version 2 |
| `lot10/2604.01151v1.pdf` | `ca9a8623307849be9df9f905086ea4c499f09c1a20208bcc4ed969e420eb08b3` | 11 | en entier, ligne à ligne |
| `lot10/2604.01151v2.pdf` | `ba39580b0e05b948e5cc8102ba8fb9209b810aff1b07b4d42b86276413ea0f40` | 29 | **en entier, ligne à ligne** pour la version 2 (annexes A à I) |
| `lot10/2604.01151v4.pdf` | `6d7c29a6b72c65ac53b018b9798b4f0f9eca2d8978ebb4faebec6276338cd650` | 47 | **en entier, ligne à ligne** pour la version 2 (annexes A à R, preuves des théorèmes 5.1 et 5.2) |

Les pages de figures sont lues sur le texte extrait (légendes, étiquettes), non relues à l'image.

## 2. L'énoncé confronté (N-007, l. 28 ; lecture de « toujours valide », l. 30-34)

Sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de faux positifs, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le sabotage avec un rappel qui croît avec l'horizon ; contexte privé compris ; seuil calibré sur des épisodes honnêtes, sans exemple de sabotage. « Toujours valide » se lit comme uniforme sur toutes les lectures de l'horizon de l'épisode, calibré sur épisodes honnêtes entiers (N-007, l. 31-32) ; le seuil de Ville seul n'est pas tenu sous effet épisode ou corrélation, 0,21 à 0,35 au lieu de 0,05 en simulation (N-007, l. 33).

Composantes : (a) accumulation additive dans le temps ; (b) garantie toujours valide ; (c) scores de sondes ; (d) de l'agent qui agit ; (e) sous un moniteur par action à 1 % ; (f) la conjonction.

## 3. Suite donnée à la contre-lecture

Lettres relevées dans la contre-lecture : A, B, C, D, E (majeurs), F, G, H, I, J, K (mineurs). Aucun bloquant.

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — v4 lit les sondes à chaque tour sur dix tours ; le rapport disait « sondés au début et à la fin » | majeur | corrigé | § 0, § 4.4, § 5, § 6, § 8 | Lu en entier : v4 p. 18, « agents judge each other's work over 10 rounds » et « rounds had at least one agent colluding » : chaque tour est une unité classée seule (480 tours), « three probes perform no better than chance ». La phrase de la p. 11 (« Finally, agents are only probed just after the initial prompt and at the end of the period. ») ne décrit pas cette expérience ; v4 p. 27 moyenne en outre sur les tours 1 à 3 (« round-N public message averaged over rounds »). J'avais vu l'environnement (liste des voisins de la version 1) sans le porter à (a) : erreur de portée, corrigée. (a) reste « non faite » : aucun cumul d'un tour à l'autre. |
| B — l'analyse par main de v1 et v2 est omise | majeur | corrigé | § 4.4, § 5, § 6 | v1 p. 8 : « to obtain a single score per agent per hand », puis « one-sided t-test » sur 39 mains (« For each of the 39 hands where the big player speaks after the counter ») ; repris en v2 p. 28 (« We consider this preliminary (39 examples, single layer) ») ; absent de v4. Agrégation de plusieurs instants, mais regroupée entre parties, sans seuil, sans taux de faux positifs, et en connaissant le complice : pas un détecteur, pas une accumulation par épisode. |
| C — « pour tout score borné » : portée fausse ; titulaire de l'outil : Howard et collègues 2020 | majeur | corrigé | § 0, § 4.3, § 6, § 7, § 8, § 10 | Relu p. 1, 26, 32 : les « scores » de 2110.00115 sont des règles de score de prévisions (« require the use of bounded scoring rules », p. 26) ; l'énoncé général porte sur des « sums of random variables that are bounded from below » (p. 32) et « This is an extension of Lemma 3(e) from Howard et al. (2020) » (p. 32). Titulaire : Howard et collègues 2020, « Time-uniform Chernoff bounds via nonnegative supermartingales » (titre relevé en 2110.00115 p. 29 et 2501.03982 p. 18), non lu. |
| D — la nulle de 2110.00115 n'est pas « pas à pas » | majeur | corrigé | § 4.3, § 8 | Relu p. 11, 16, 17 : nulle faible sur la moyenne cumulée des moyennes conditionnelles (« the first forecaster (p) is no better than the second forecaster (q) on average », p. 16) ; le « pas à pas » est la nulle forte (« at every time step », p. 17), celle de Henzi et Ziegel. Ma conclusion tient par une autre page : la filtration contient « any information available to Reality before the outcome » (p. 11), donc le niveau propre de l'épisode. |
| E — 2501.03982 : l'égalité au terme ne vaut pas pour l'accumulation vers l'avant ; le test induit n'alerte pas plus tôt | majeur | réserve maintenue | § 4.1, § 8, § 9 | Les trois corrections de fond sont faites (§ 4.1) : égalité au terme pour le test induit seul ; perte de l'accumulation vers l'avant dans l'exemple de l'article (91 % contre 79 %, 47 % si l'alternative est apprise, p. 2) ; pas d'alarme franche avant le terme (p. 3), alarme anticipée au prix d'une erreur bornée par le niveau divisé par le seuil (p. 4) ; gain plus tôt seulement par continuation optionnelle (p. 12). **Réserve maintenue** sur une formule : « une somme lue en fin d'épisode avec un seuil à horizon fixe bat l'accumulation toujours valide ». Les pages la montrent dans un cas (loi normale, alternative connue) ; en général, le test à horizon fixe le plus puissant ne peut qu'égaler ou dépasser, au terme, tout test séquentiel valide (lemme de Neyman et Pearson, déduction du lecteur), sans que l'écart soit garanti strictement ni chiffré hors de l'exemple, et sous une loi nulle spécifiée. J'écris « ne peut pas faire mieux au terme, et perd dans l'exemple ». La proposition pour G1 qui en découle est décrite en § 9, non tranchée. |
| F — la dilution n'est pas à la page citée | mineur | corrigé | § 4.3 | p. 20 : « It then decreases back to values below 1 » quand la moyenne cumulée change de signe. L'érosion par des pas honnêtes est une déduction de l'équation 24 (p. 17), marquée comme telle. |
| G — le rappel de 0,38 à 1 % : un seul modèle, une trentaine de contrôles, aucun intervalle dans le texte | mineur | corrigé | § 4.4, § 8 | v2 p. 8, figure 5 (« ROC curves on Llama-3.1-70B ») ; v2 p. 24 : « results throughout the paper use the 30 audited-collusion runs paired with the 30 corresponding control runs ». Avec 30 contrôles, 1 % de faux positifs revient à zéro faux positif (calcul : 1/30 ≈ 0,033). Bandes de confiance seulement sur la figure, aucun intervalle sur le chiffre dans le texte. |
| H — incohérences de v2 et v4 sur l'instant d'extraction | mineur | corrigé | § 4.4, § 8 | v2 p. 4 (« we average across all discussion rounds ») contre v2 p. 18 (« Activations are extracted at this phase. », tour final) et p. 17 (« any probe signal captured at the final-phase extraction position ») ; v4 p. 11 contre p. 27 (« round-N public message averaged over rounds »), p. 32 (« public discussion phase where activations are extracted ») et p. 33 (« prompt, at which activations are extracted », consigne du tour final). Confirmé. |
| I — v4 écarte l'agent seul dans le temps et l'annonce | mineur | corrigé | § 0, § 4.4, § 8, § 11 | v4 p. 7, note 3 : « Our current environmental setup excludes self-communication and hence self-collusion over time. » et « We plan to explore this in future additional benchmarks. » C'est la menace de H2 (un agent, des actions réparties) : nommée par l'équipe, hors de son cadre actuel. |
| J — voisins nommés en v4 et absents de la liste | mineur | corrigé | § 10 | Ajoutés, Makins et collègues 2026 et Oldfield et collègues 2026 en tête, avec Golechha et Garriga-Alonso 2025, McKenzie et collègues 2025, Tailor 2025, et la source du lemme générique. |
| K — journal du lecteur (fichier ouvert, recherche de motif ; contradiction sur la p. 18 de v4) | mineur | corrigé | § 1, § 11 | Contradiction levée : la p. 18 de v4 était lue en entier (section 1 de la version 1) et la réserve de la section 8 de la version 1 la disait « par mots » à tort ; v4 est désormais lue en entier. Le fichier `anteriorite-v1.md` (l. 62-94) était nommé par mon premier mandat, et le `grep -n 'm6'` qui a affiché trois lignes hors des plages était prescrit par lui ; je le déclare comme dans la version 1, sans autre affichage hors des plages. |

## 4. Article par article

### 4.1 2501.03982v5 — Koning et van Meer, « Anytime Validity is Free: Inducing Sequential Tests »

**Venue imprimée** : arXiv, math.ST, version 5 du 21 décembre 2025 ; date de tête « December 23, 2025 » (p. 1) ; aucune revue nommée.

**Ce qu'il fait.** Résultat principal : « for any valid test based on N observations, we show how to construct an anytime valid sequential test that matches it after N observations » (p. 1). Le test induit est l'espérance conditionnelle, sous la nulle, du test terminal (martingale de Doob ; théorème 1, p. 5). Formule, lue sur le PDF, non contrôlée par programme : φ′ₙ = E_P[φ_N | Xⁿ] (p. 2). Construction « à rebours », distincte de l'accumulation vers l'avant, « which relies on designing martingale-increments and sequentially accumulating these » (p. 4). Hypothèses composites (p. 6), rapport de vraisemblance monotone (p. 8), tests z et t séquentialisés (p. 8-11), continuation optionnelle (p. 12), lien avec les e-valeurs (p. 14-16). Données simulées seulement : des observations qui « are independently drawn from the normal distribution » (p. 8).

**Ce que les pages disent de la puissance (corrigé, constat E).**
- Au temps terminal, le test induit à rebours égale le test à horizon fixe (p. 1, 5).
- L'accumulation vers l'avant, qui est l'objet de H2, perd au terme dans l'exemple de l'article : « the z-test rejects with probability 91% while this sequential test rejects at any time » … « with probability just 79% », et « then its power is just 47% » si l'alternative est apprise en ligne (p. 2 ; auteurs ; loi normale, μ = 0 contre 0,3, N = 100). Les auteurs notent que cet écart « seems to be generally viewed as the cost of anytime validity » (p. 2).
- Le test induit ne donne pas d'alarme franche avant le terme : « the final observation may be arbitrarily small or large with some tiny probability » (p. 3), si bien qu'il reste strictement entre 0 et 1. Une alarme anticipée par seuil sur la probabilité conditionnelle (« stochastic curtailment », p. 4) a une erreur de première espèce « which they show has a Type I error bounded by » le niveau divisé par ce seuil (p. 4).
- Pour le test le plus puissant au terme, « straying from this implicit optional continuation cannot increase power at time N » ; « with optional continuation we can obtain more power at an earlier or later (stopping) time » (p. 12) : un gain plus tôt suppose un autre plan.

**Ce qu'il ne fait pas.** Aucun moniteur, aucune sonde, aucun agent, aucun modèle de langue. **Limites reconnues** : loi nulle à spécifier, et sans forme close « one may have to resort to numerical approximations » (p. 6) ; « we do not advocate for everyone to use sequential tests induced from classical Neyman-Pearson-style tests » (p. 16), mesurés à un temps fini, « so that they do not naturally continue beyond this time » (p. 16).

**Verdict par composante.** (a) **voisin** (construction à rebours ; l'accumulation vers l'avant n'y est qu'un comparateur, p. 2, 4) ; (b) **outil générique** pour une garantie sur un horizon fini, loi nulle spécifiée (p. 5) ; (c), (d), (e) **ne touche pas** ; (f) **ne touche pas**. **Contre-indice pour la forme de H2** : à horizon connu et loi nulle spécifiée, l'accumulation toujours valide ne peut pas faire mieux, au terme, que le meilleur test à horizon fixe, et perd dans l'exemple (p. 2) ; le gain revendicable se mesure contre une somme à horizon fixe et en latence à erreur égale (§ 9).

### 4.2 2103.08402v3 — Henzi et Ziegel, « Valid sequential inference on probability forecast performance »

**Venue imprimée** : arXiv, stat.ME, version 3 du 1er juillet 2022 ; publication à Biometrika 2022 selon la bibliographie de 2110.00115 (p. 29).

**Ce qu'il fait.** E-valeurs de dominance entre deux prévisions d'un événement binaire (p. 5-6) ; formule, lue sur le PDF, non contrôlée : E(y) = 1 + λ (S(p, y) − S(q, y)) / |S(p, 1{p > q}) − S(q, 1{p > q})| (p. 6). Accumulation **multiplicative** : « e-values from different time points can be merged by products into a non-negative supermartingale or test-martingale » (p. 2). « The e-values proposed in this article are valid in finite samples without any assumptions on the data generating processes. » ; « They also allow optional stopping » (p. 1). Nulle forte : « they require conditional dominance at all time points » (p. 4). Cas réel sur la pluie (p. 12-16) ; « Even if the score differences are only small, evidence eventually accumulates over the whole time period » (p. 15). Des tests usuels au niveau 0,05 « may yield rejection rates of up to 0.15 under optional stopping » (p. 3, auteurs).

**Ne fait pas** : aucun moniteur, sonde, agent ; le cadre exige un résultat observé à chaque pas, ce que H2 n'a pas en ligne (déduction du lecteur). **Limite reconnue** : « The advantages of e-values for forecast comparison relative to the currently available methods come at a price, namely, lower power. » (p. 3).

**Verdict** : (a) voisin (produit de e-valeurs) ; (b) outil voisin (nulle forte, résultats observés) ; (c)-(f) ne touche pas.

### 4.3 2110.00115v6 — Choe et Ramdas, « Comparing Sequential Forecasters »

**Venue imprimée** : arXiv, stat.ME, version 6 du 9 novembre 2023 ; publication à Operations Research indiquée en note (p. 1).

**Ce qu'il fait.** Suites de confiance et e-processus pour la différence moyenne des scores de deux prévisionnistes, sans hypothèse de loi : « Our methods do not make distributional assumptions on the forecasts or outcomes » et « our main theorems apply to any bounded scores » (p. 1). **Portée exacte (corrigé, constat C)** : ces « scores » sont des règles de score de prévisions comparées à un résultat observé ; les théorèmes non asymptotiques « require the use of bounded scoring rules » (p. 26). L'énoncé général, la proposition 1 de l'annexe A.1, porte sur des « sums of random variables that are bounded from below », centrées sur leurs moyennes conditionnelles (une suite « be any process whose conditional means » existent, p. 32), et les auteurs le présentent ainsi : « This is an extension of Lemma 3(e) from Howard et al. (2020) » (p. 32). Le titulaire de l'outil générique est donc Howard et collègues 2020, « Time-uniform Chernoff bounds via nonnegative supermartingales » (2110.00115 p. 29), non lu.

Formules, lues sur le PDF, non contrôlées : e-processus E_t(λ) = exp{λ Σᵢ≤ₜ δ̂ᵢ − ψ_E,c(λ) V̂_t}, V̂_t = Σᵢ≤ₜ (δ̂ᵢ − γᵢ)² (p. 17, éq. 24) ; nulle faible H₀ʷ : Δ_t = (1/t) Σᵢ≤ₜ δᵢ ≤ 0 pour tout t, avec δᵢ = Eᵢ₋₁[δ̂ᵢ] (p. 11, 16).

Garantie : « we define safe, anytime-valid inference (SAVI) methods as ones that satisfy either the time-uniform coverage guarantee (CS) or the anytime-valid guarantee (e- or p-processes) » (p. 4) ; l'e-processus « quantifies the amount of accumulated evidence against the null up to time t » (p. 4). Applications : base-ball, pluie, simulations ; le seul déploiement évoqué est celui d'une entreprise qui « deploys a daily forecasting algorithm may want to A/B test » (p. 38). Aucun moniteur, aucune sonde, aucun agent. Chiffres (auteurs) : « the fixed-time CI is only valid at a fixed time t and not uniformly over time, despite its tighter width » (p. 20) ; les tests classiques dépassent le niveau en erreur cumulée « after roughly 100 and 1000 steps, respectively » (p. 54). Limites : « Deriving a fully general anytime-valid procedure for unbounded domains and scoring rules remains an open problem. » (p. 51) ; « the inferential conclusions drawn from our methods need not extrapolate to future time steps » (p. 27).

**Ce qui pèse sur H2 (analyses du lecteur, tenues par le contre-lecteur dans leur conclusion).**
1. **Nulle (corrigé, constat D).** La nulle faible borne, à tout instant, la **moyenne cumulée** des moyennes conditionnelles (« whether one forecaster outperforms another on average (rather than always) », p. 1 ; « the first forecaster (p) is no better than the second forecaster (q) on average », p. 16) ; la borne « at every time step » est la nulle forte (p. 17), celle de Henzi et Ziegel (« The recent work by Henzi and Ziegel (2022) develops e-processes », p. 17). Les moyennes conditionnelles se prennent par rapport à une filtration qui contient « any information available to Reality before the outcome » (p. 11), donc le niveau propre de l'épisode. Sous un effet épisode, un épisode honnête de niveau haut a une moyenne cumulée au-dessus de la référence : la nulle est fausse pour lui et l'e-processus le rejette à bon droit statistique, ce qui fait une fausse alarme du point de vue du programme. Cela rend compte des 0,21 à 0,35 de T0.3 (N-007, l. 33) et confirme qu'il faut une garantie calibrée sur épisodes honnêtes entiers.
2. **Érosion (corrigé, constat F).** La p. 20 montre que l'e-processus « It then decreases back to values below 1 » quand la moyenne cumulée devient négative. Par l'équation 24, chaque pas sans signal ajoute au terme de variance : un sabotage concentré sur une part de la trajectoire est érodé par les passages honnêtes. C'est une déduction du lecteur, non un énoncé des auteurs.
3. Scores de sondes non bornés : écrêtage ou suite asymptotique (annexe C, p. 37-38).

**Verdict.** (a) et (b) : **outil** (variante de Howard et collègues 2020, p. 32) ; (c), (d), (e), (f) : **ne touche pas**.

### 4.4 NARCBench (2604.01151), « Detecting Multi-Agent Collusion Through Multi-Agent Interpretability » — versions 1, 2 et 4, lues en entier

**Ce que fait l'article.** Une direction de tromperie apprise par sonde linéaire sur les activations de chaque agent, dont les agents en collusion (agents qui agissent) ; puis des statistiques de groupe sur les scores par agent : « propose five probing techniques that aggregate per-agent deception scores to classify scenarios at the group level » (v1 p. 1). Chaque statistique donne un nombre par épisode : « they compute a single scalar per run » (v2 p. 5). Modèle nul : « each agent's deception score is drawn from a common honest distribution » (v2 p. 5). Quatre modèles à poids ouverts en v2 et v4 (dont Llama-3.1-70B, le plus fort).

**Lectures répétées des sondes (corrigé, constats A et B).**
- v1 p. 8 et v2 p. 28 : score par jeton puis moyenne sur les jetons du message, « to obtain a single score per agent per hand » ; écart entre le complice et les honnêtes sur 39 mains (« For each of the 39 hands where the big player speaks after the counter », v1 p. 8 ; « For each of the 39 hands where the Big Player speaks after the Counter », v2 p. 28), par « one-sided t-test » (v1 p. 8). Dit préliminaire : « This localisation is preliminary (39 examples, single layer) » (v1 p. 9) ; « We consider this preliminary (39 examples, single layer) » (v2 p. 28). Absent de v4.
- v4 p. 18 (section 6.3, collusion émergente) : « agents judge each other's work over 10 rounds » ; 48 épisodes de dix tours, 480 tours dont 229 où « rounds had at least one agent colluding » (auteurs) ; chaque tour est une unité classée seule ; résultat faible : « three probes perform no better than chance ». v4 p. 44-45 (annexe M) : autre environnement émergent, lecture par épisode ; « Further work needs to establish whether emergent collusion can be detected using probes. » (p. 45).
- v4 p. 16 : les statistiques sont définies à un instant, « We analyse the scores at time t and suppress the indexing by t » et, pour la séparation, « We fix a time t and suppress this index below. » ; aucune combinaison entre instants.
- Agrégation dans le temps des activations du comité : moyenne sur les tours (v1 p. 5, « we average each agent's activations across all discussion rounds to capture their sustained representation of the shared deliberation » ; v2 p. 4, « we average across all discussion rounds » ; v4 p. 27, « round-N public message averaged over rounds »), dernier tour ailleurs (v1 p. 5, « we use final-round activations only (the last round where all agents receive identical user prompts) » ; v2 p. 4, « we use final-round activations only, where all agents receive identical user prompts »).

**Incohérences internes (corrigé, constat H).** v2 p. 4 dit la moyenne sur les tours, mais p. 18 « Activations are extracted at this phase. » (tour final) et p. 17 « any probe signal captured at the final-phase extraction position ». v4 p. 11 dit « Finally, agents are only probed just after the initial prompt and at the end of the period. », p. 27 la moyenne sur les tours 1 à 3, p. 32 « public discussion phase where activations are extracted », p. 33 « prompt, at which activations are extracted » (tour final). L'article ne dit pas d'une seule voix quand il lit le comité. Autre incohérence mineure : v2 date de 2022 l'article de Howard et collègues (« Time-uniform, nonparametric, nonasymptotic confidence sequences », v2 p. 11), que v4 (p. 22) et 2110.00115 datent de 2021.

**Seuil à 1 % (corrigé, constat G).** « even the best method (Deception Split) achieves only 0.38 recall at 1% FPR » sur le transfert (v2 p. 8 ; v4 p. 18 ; auteurs), 1,00 sur la partie de cartes ; pour un seul modèle (« ROC curves on Llama-3.1-70B », v2 p. 8) ; par épisode ; sur « results throughout the paper use the 30 audited-collusion runs paired with the 30 corresponding control runs » (v2 p. 24), où 1 % revient à zéro faux positif (calcul : 1/30 ≈ 0,033) ; bandes de confiance sur la figure, aucun intervalle sur ce chiffre dans le texte. Aucun moniteur par action : le seul juge de texte rend un verdict par partie, « an independent LLM monitor reads all public table talk and tags each shoe » (v2 p. 27 ; v4 p. 44). Le seul « sous un seuil » est entre agents à un instant : « colluding agents could coordinate to keep individual scores below a detection threshold » (v1 p. 6).

**Menace diffuse et agent seul (corrigé, constat I).** La famille « News Framing (gradual narrative drift) » décrit une dérive où « Each individual contribution is defensible in isolation » ; « This is the only Transfer family with iterated public contributions that build on each other. » (v2 p. 23 ; v4 p. 39) ; elle est lue au dernier tour (v2 p. 4), soit la base (iii) de N-007. Le cadre de v4 écarte l'agent qui se coordonne avec lui-même dans le temps : « Our current environmental setup excludes self-communication and hence self-collusion over time. » ; « We plan to explore this in future additional benchmarks. » (v4 p. 7, note 3).

**Cadre formel de v4.** Capteurs internes ou externes : « Local sensors can be external (local monitors) or internal (probes). » (p. 10) ; « internal sensors called collusion probes » (p. 15) ; le moniteur central « E bases its decision rule on its own aggregated history » des signaux (p. 11). Le cadre admet une lecture séquentielle de sondes ; aucune règle séquentielle n'y est définie.

**Limites reconnues.** « The adversarial robustness of these techniques is untested » (v1 p. 9) ; « Adversarial robustness is untested. » (v2 p. 9) ; v4 ajoute une petite expérience de conscience d'évaluation (annexe H, p. 31) et cite un résultat voisin, « fixed-threshold recall can drop sharply » (p. 3).

**Verdict par composante.**
- (a) **annoncée, non faite** à partir de v2 (p. 8, 9). v1, v2 et v4 moyennent des activations sur les tours du comité (avec les contradictions ci-dessus). v1 et v2 calculent un score par main, testé sur 39 mains regroupées. v4 lit les sondes à chacun des dix tours d'un environnement de collusion émergente et classe chaque tour seul (p. 18). Aucun cumul d'un instant à l'autre au sein d'un épisode, aucune courbe selon le nombre de tours.
- (b) **annoncée, non faite** (« would yield formal stopping guarantees », v2 p. 9 ; v4 p. 26).
- (c) **faite** ; (d) **faite**.
- (e) **voisin** (rappel à 1 % par épisode ; aucun moniteur par action).
- (f) **non faite, annoncée** ; matériau présent (scores par tour en v4).
- Verdict pour NARCBench : **occupe en partie** ((c), (d)).

## 5. Datation de NARCBench, version par version

| version | date imprimée (tampon arXiv, p. 1 ; aucune autre date) | lecture séquentielle, accumulation dans le temps, garantie toujours valide, arrêt optionnel | lectures répétées des sondes, sans cumul |
|---|---|---|---|
| v1 | « 1 Apr 2026 » | **rien** ; le seul « Multi-Turn Interactions » est un titre de référence (p. 10) | moyenne d'activations sur les tours du comité (p. 5) ; score par main sur 39 mains, test de Student unilatéral (p. 8) |
| v2 | « 9 May 2026 » | **annonce, deux fois** : p. 8, « accumulating evidence across interactions via SAVI [Howard et al., 2022] for example », « is a natural next step », après le rappel de 0,38 à 1 % ; p. 9, « Sequential detection. Accumulating evidence across multiple interactions [Kulkarni, 2026], via SAVI [Howard et al., 2022] for example, would yield formal stopping guarantees. » | moyenne sur les tours dite p. 4, tour final dit p. 17-18 ; score par main en annexe I (p. 28) |
| v4 | « 12 Oct 2026 » | **annonce, quatre fois** : p. 3, « Multi-turn extensions of our detection setting call for sequential detection machinery » ; p. 18, « One-shot detection at strict » [légende intercalée] « thresholds is therefore insufficient for structural collusion. », puis « Sequential detection that accumulates evidence across inter » [césure, « actions »] « is a natural next step » ; p. 19, « Future work will explore principled sequential detection techniques » ; p. 26, « Accumulating evidence across multiple interactions (Kulkarni, 2026), via SAVI (Howard et al., 2021) for example, would yield formal stopping guarantees. » ; cadre formel p. 10-11 ; agent seul dans le temps écarté et annoncé (p. 7) | sondes lues à chacun des dix tours d'un environnement émergent, chaque tour classé seul (p. 18) ; moyenne sur les tours 1 à 3 (p. 27) ; statistiques à un instant fixé (p. 16) ; l'analyse par main a disparu |

Les mots anytime, e-process, e-value, martingale et Ville n'apparaissent dans aucune version hors d'un titre de référence de v4 (« Game-theoretic statistics and Safe Anytime-Valid Inference », p. 24) ; le sigle SAVI n'est développé dans aucune version (son sens est celui de 2110.00115, p. 4). Le constat m6 de la contre-lecture du niveau 3 est confirmé ; il gagne à citer aussi la v2 p. 8. Versions 3 et 5 non lues dans ce mandat.

## 6. Table composante × article

| source | (a) additive | (b) toujours valide | (c) sondes | (d) agent qui agit | (e) moniteur par action à 1 % | (f) conjonction | verdict |
|---|---|---|---|---|---|---|---|
| 2501.03982v5 | voisin : construction à rebours ; l'accumulation vers l'avant perd au terme dans l'exemple (p. 2, 4) | outil, horizon fini, loi nulle spécifiée (p. 5) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | ne touche pas ; contre-indice pour la forme de H2 (p. 2, 3, 12) |
| 2103.08402v3 | voisin, produit de e-valeurs (p. 2, 7) | outil voisin, nulle forte, résultats observés (p. 1, 4, 8) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | ne touche pas |
| 2110.00115v6 | outil : proposition 1, extension de Howard et collègues 2020 (p. 32) | outil, nulle faible sur la moyenne cumulée (p. 16, 17) | ne touche pas | ne touche pas | ne touche pas | ne touche pas | voisin ; outil à citer, avec Howard et collègues 2020 |
| 2604.01151 v1 | non ; score par main sur 39 mains regroupées (p. 8) ; moyenne d'activations sur les tours (p. 5) | non | faite (p. 1, 5) | faite (p. 5) | non (seuil entre agents, p. 6) | non | occupe en partie ((c), (d)) |
| 2604.01151 v2 | annoncée (p. 8, 9) ; score par main (p. 28) | annoncée (p. 9) | faite | faite | voisin, par épisode (p. 8, 24) | non faite, annoncée le 9 mai 2026 | occupe en partie |
| 2604.01151 v4 | annoncée (p. 3, 18, 19, 26) ; sondes lues à chaque tour sur dix tours, sans cumul (p. 18) ; cadre formel (p. 10-11) | annoncée (p. 26) | faite | faite | voisin, par épisode (p. 18) | non faite, annoncée ; matériau présent ; agent seul écarté et annoncé (p. 7) | occupe en partie |

**Verdict d'ensemble sur H2, table fermée : occupé en partie.** Conjonction (f) : non trouvée dans les pièces lues.

## 7. Ce qui reste revendicable (formulation exacte)

« La conjonction de l'énoncé N-007 — accumulation additive à garantie uniforme sur l'horizon de l'épisode, calibrée sur des épisodes honnêtes entiers sans exemple de sabotage, de scores de sondes lues sur l'agent qui agit, contexte privé compris, sur des trajectoires dont chaque action sabotée reste sous un moniteur par action calibré à 1 %, avec un rappel mesuré en fonction de l'horizon — n'est réalisée dans aucune des six pièces lues. L'outil statistique est publié et se cite (Howard et collègues 2020, non lu, et sa variante dans 2110.00115 ; 2501.03982 pour la garantie sur un horizon fini). La lecture séquentielle de sondes d'agents est annoncée sans résultat par l'équipe de NARCBench depuis la version 2 du 9 mai 2026, qui lit déjà des sondes tour par tour sans les cumuler (version 4, 12 octobre 2026) et écarte de son cadre actuel l'agent seul qui se coordonne avec lui-même dans le temps. »

Ce qui se revendique est une mesure, non un outil : le rappel en fonction de l'horizon sous la condition « sous le seuil par action », et le gain contre les bases de comparaison (celles de N-007, et la somme à horizon fixe si Lazar l'ajoute, § 9), à erreur égale, en latence.

## 8. Ce qu'une phrase publique sur H2 ne doit pas affirmer

- Que l'accumulation additive toujours valide d'une suite de scores est nouvelle ou apportée par le programme : elle est publiée (Howard et collègues 2020, non lu ; variante en 2110.00115, p. 32).
- Que 2110.00115 a établi l'outil « pour tout score » de détecteur : ses théorèmes principaux portent sur des règles de score de prévisions (p. 1, 26) ; l'énoncé général est un lemme étendu de Howard et collègues (p. 32).
- Que la garantie de l'e-processus donne à elle seule un taux de fausses alarmes ≤ α sur des épisodes honnêtes : sa nulle porte sur la moyenne cumulée des moyennes conditionnelles, prises par rapport à une filtration qui contient l'état propre de l'épisode (2110.00115, p. 11, 16) ; sous effet épisode, elle ne tient pas (N-007, l. 33).
- Que l'accumulation toujours valide égale en puissance, en fin d'épisode, un test à horizon fixe : cela vaut pour le test induit à rebours, non pour l'accumulation vers l'avant, qui ne peut pas faire mieux au terme et perd dans l'exemple de l'article (2501.03982, p. 2, 4).
- Qu'une garantie toujours valide donne sans coût une alerte plus précoce (2501.03982, p. 3, 4, 12).
- Que personne n'a envisagé la lecture séquentielle de sondes d'agents : NARCBench l'annonce depuis le 9 mai 2026 (v2, p. 8-9) et la maintient au 12 octobre 2026 (v4, p. 3, 18, 19, 26).
- Que NARCBench ne lit ses sondes qu'à un instant par épisode : v4 les lit à chacun des dix tours d'un environnement (p. 18) ; v1 et v2 calculent un score par main (v1 p. 8 ; v2 p. 28).
- Que NARCBench sonde « au début et à la fin » ou « moyenne sur les tours », sans réserve : l'article se contredit (v2 p. 4, 17, 18 ; v4 p. 11, 27, 32, 33).
- Que le rappel de 0,38 à 1 % de NARCBench est un rappel par action, ou un chiffre précis : il est par épisode, pour un modèle, sur une trentaine de contrôles (v2 p. 8, 24).
- Que le cas d'un agent seul qui répartit son sabotage dans le temps est ignoré de cette équipe : elle l'écarte de son cadre actuel et l'annonce (v4 p. 7, note 3).
- Que la zone est « vide » : « non trouvée dans les pièces lues » seulement (R8) ; exposition forte.

## 9. Proposition du contre-lecteur pour le préenregistrement de G1 (décrite, non tranchée)

**Ce qui est proposé** (contre-lecture, constat E, point 3) : ajouter aux quatre bases de comparaison de N-007 une **somme à horizon fixe des mêmes scores de sondes, lue en fin d'épisode, avec un seuil calibré sur épisodes honnêtes entiers**.

**Ce qui la motive dans les pièces** : 2501.03982 montre qu'au terme l'accumulation vers l'avant ne fait pas mieux que le meilleur test à horizon fixe et perd dans l'exemple normal (91 % contre 79 %, auteurs, p. 2) ; le test z de l'exemple est précisément une somme des observations lue au terme (p. 8-9).

**Ce qu'elle isolerait** : le prix de la garantie toujours valide à sondes égales et à accumulation égale. La base (iii) de N-007, sonde sur le dernier état seul, mesure autre chose (pas de somme) ; la base (ii), cascade de portes, aussi.

**Points que Lazar aurait à fixer s'il l'accepte** (relevés par le lecteur, sans recommandation) :
- l'horizon de lecture (fin d'épisode réelle ou horizon fixé d'avance) ;
- la métrique de comparaison (puissance au terme, latence à erreur égale, ou les deux) ;
- la place de cette base dans le critère de G1 ou seulement dans H2, à l'image de la répartition de N-007 entre bases de G1 et bases de H2.

Cette proposition modifie un préenregistrement à venir : décision de Lazar, hors du rôle du lecteur et du contre-lecteur.

## 10. Voisins nommés dans les pièces et non lus (page où ils sont nommés)

- **Makins et collègues 2026**, « Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors » — v4 p. 3, où l'équipe dit qu'ils « explore centralised black-box detection of multi-agent attacks » ; référence p. 23. Touche la condition « sous le moniteur par action » de H2. **À lire en premier.**
- **Oldfield et collègues 2026**, « Beyond Linear Probes: Dynamic Safety Monitoring for Language Models » — v4 p. 46 (« (McKenzie et al., 2025; Oldfield et al., 2026) »), référence p. 23. Surveillance « dynamique » par sondes d'après le titre. **À lire en premier.**
- Golechha et Garriga-Alonso 2025, « Among Us: A Sandbox for Measuring and Detecting Agentic Deception » — v4 p. 3, qui les décrit comme voulant « detect deception within a multi-agent game by considering single-agent whitebox detectors » ; référence p. 21.
- McKenzie et collègues 2025, « Detecting High-Stakes Interactions with Activation Probes » — v4 p. 46, référence p. 23.
- Howard et collègues 2020, « Time-uniform Chernoff bounds via nonnegative supermartingales » — 2110.00115 p. 32 (source du lemme), référence p. 29 ; 2501.03982 référence p. 18 (« Time-uniform chernoff bounds via nonnegative supermartingales »). Titulaire de l'outil générique.
- Howard et collègues 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences » — v2 p. 9 et 11, v4 p. 26 ; 2110.00115 p. 3, 6.
- Das et collègues 2026, « You Can't Escape Your Own Activations : Evaluation Awareness and Multi-Agent Monitoring » (arXiv 2609.03035) — v4 p. 3 (rappel à seuil fixe), référence p. 20.
- Shi et collègues 2026, « Emergent collusion in long-horizon llm agent interaction » (arXiv 2609.24967) — v4 p. 18, l'environnement aux dix tours, référence p. 24.
- Tailor 2025 (détection de collusion stéganographique), décrit comme une méthode qui « fuses several black-box tests » — v4 p. 3, référence p. 25.
- Xie et Siegmund 2013, « Sequential multi-sensor change-point detection » — v4 p. 3 et 18, référence p. 25.
- Wen et collègues 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » — v4 p. 3, référence p. 25 (déjà au dossier sous 2411.17693).
- Ramdas et collègues 2023, « Game-theoretic statistics and Safe Anytime-Valid Inference » — v4 p. 3 et 18, référence p. 24.
- Kulkarni 2026, « Latent adversarial detection: Adaptive probing of LLM activations for multi-turn attack detection » (2604.28129) — v2 p. 9, v4 p. 26 ; déjà lu au niveau 2.
- Lan et collègues 1982 — 2501.03982 p. 4 : arrêt sur probabilité conditionnelle, avec sa borne d'erreur.
- Nasvytis et collègues 2024 (détection hors distribution en apprentissage par renforcement) — v4 p. 3, référence p. 23.
- Versions 3 et 5 de 2604.01151 : non lues dans ce mandat.

## 11. Réserves (R4, R8)

- La contradiction de la version 1 sur la profondeur de lecture de la p. 18 de v4 est levée : v2 et v4 sont lues en entier pour la version 2. Reste que les figures ne sont pas relues à l'image : une courbe selon le tour, ni annoncée par sa légende ni par le texte, m'échapperait ; aucune légende lue n'en annonce.
- Le verdict « rien de fait » sur la lecture séquentielle est le résultat attendu et commode (R4) : il a été cherché à l'envers, page par page, dans les annexes d'expériences de v2 et v4 et dans les preuves de v4.
- L'exposition est **forte** : matériau présent (scores de sondes par tour, v4 p. 18), annonce datée (9 mai 2026), cas de l'agent seul dans le temps nommé et annoncé (v4 p. 7). Une version 5 ou ultérieure, ou un travail de la même équipe, peut occuper la conjonction.
- Réserve maintenue sur le constat E (§ 3) : la supériorité stricte d'une somme à horizon fixe n'est établie que dans l'exemple de l'article ; en général, « pas mieux au terme » seulement.
- Les points marqués « déduction du lecteur » (§ 4.1, § 4.3, § 3 E) sont des conséquences tirées des théorèmes, non des énoncés des auteurs.
