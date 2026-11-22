# Rapport de lecture — parents lointains (analogie, transfert, rapprochement de littératures)

Date : 22 novembre 2026. Dossier des sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/parents-lointains/`. Pages = pages du fichier PDF ; le numéro imprimé est donné quand il diffère.

## 1. Gentner, Rattermann et Forbus 1993 (rappel ≠ solidité)

- Référence : Gentner D., Rattermann M. J., Forbus K. D. (1993). The Roles of Similarity in Transfer: Separating Retrievability From Inferential Soundness. *Cognitive Psychology* 25, 524-575.
- URL : https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf
- Fichier : `gentner1993.pdf`, sha256 `ccb7655fb1cead48f3ee81c5b8f65b6c33d78faac5c2dbf5341bd62b1724bce8` (26 pages ; scan à deux pages imprimées par page du fichier : page N du fichier = pages imprimées 522+2N et 523+2N).
- Codes des types : AN = analogie vraie (R1 + R2, relations de premier ordre et d'ordre supérieur) ; SS = ressemblance de surface, « mere appearance » (OA + R1) ; FOR = relations de premier ordre seules (R1) ; LS = similarité littérale (OA + R1 + R2) ; OO = objets seuls.

| Affirmation | Page fichier (imprimée) | Citation verbatim | Statut |
|---|---|---|---|
| Thèse | p. 1 (525) | « We conclude that there is a dissociation between the similarity that governs access to long-term memory and that which is used in evaluating and reasoning from a present match. » | lu sur PDF, p. 1 |
| Expérience 1, tableau 3 : solidité AN 4,40 / SS 2,80 / FOR 2,74 ; proportion rappelée AN .44 / SS .78 / FOR .25 ; qualité du rappel 1,48 / 2,36 / .86 | p. 7 (537) | « Soundness 4 .40 2 .80 2.74 / Proportion recalled .44 .78 .25 » (tableau, échelles 1-5) | lu sur PDF, p. 7 |
| Expérience 2 : solidité LS 4,41, AN 4,16, SS 2,70, FOR 2,58 ; rappel LS .56, SS .53, AN .12, FOR .09 | p. 9-10 (540-543) ; p. 18 (558) | « recalled more LS (M = .56) and SS (M = .53) matches than AN (M = .12) and FOR (M = .09) matches » | lu sur PDF, p. 10 |
| Expérience 3 : SS .52, OO .17 mieux rappelés que AN .07 | p. 13 (548-549) | « .52) and 00 matches (M .17) were better retrieved than AN matches (M = .07) » (extraction de colonne) | lu sur PDF, p. 13 |
| Synthèse sur le rappel | p. 20 (563) | « The results for access were almost the reverse of the results for soundness. Subjects tended not to retrieve the matches they considered most sound. » ; « The proportions of surface matches retrieved across the three studies were .78, .53, and .52, respectively, substantially higher than the retrieval rate for analogies (.44, .12, and .07, respectively). » | lu sur PDF, p. 20 |
| Nuance (l'accès relationnel n'est pas nul) | p. 20 (563) | « higher-order relational similarities can sometimes promote access, but that the effects are less robust than the effects for surface matches » | lu sur PDF, p. 20 |
| Expérience 4 : la structure est encodée, l'échec est au rappel | p. 15 (553) | « We conclude that the locus of the surface superiority effect is at retrieval. » | lu sur PDF, p. 15 |
| Similarité jugée ≠ ordre de rappel | p. 1 (525) | « Ratings of the similarity of the pairs did not predict the retrievability ordering » | lu sur PDF, p. 1 |

### 1 bis. Forbus, Gentner et Law, MAC/FAC

- Référence : Forbus K. D., Gentner D., Law K. MAC/FAC: A Model of Similarity-based Retrieval. *Cognitive Science* 19, 141-205. L'en-tête du PDF porte « (1994) » ; l'année de la revue est 1995, de mémoire, à vérifier.
- URL : https://qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1994/Forbus_1994_MAC_FAC_Model_Similarity-Based_Retrieval_CogSci.pdf
- Fichier : `macfac1994cogsci.pdf`, sha256 `490364eaac37ea159fe8ddd42173da452205fbb0632a555ad558b1f9570bf0f1` (65 pages).
- p. 1 (résumé), lu sur PDF : « The first stage uses a computationally cheap, non-structural matcher to filter candidate long-term memory items. It uses content vectors, a redundant encoding of structured representations whose dot product estimates how well the corresponding structural representations will match. The second stage uses SME (structure-mapping engine) to compute structural matches on the handful of items found by the first stage. » Les phénomènes à reproduire : « (b) in retrieval, superficial similarity is more important than structural similarity; and yet (c) purely structural (analogical) remindings are sometimes experienced. »
- Simulation dans l'article de 1993, p. 18 (558-559), tableau : proportion retrouvée par MAC/FAC, LS .78, SS .67 (ou .44), AN .33 (ou .11), FOR .22 (ou 0), deux colonnes dont je n'ai pas lu l'en-tête. Statut : extraction de tableau, en-têtes non vérifiés.
- Seul le résumé du MAC/FAC de 1995 est lu ; le corps n'est pas lu.

## 2. Hope, Chan, Kittur et Shahaf 2017 (Accelerating Innovation Through Analogy Mining)

- Référence : Hope T., Chan J., Kittur A., Shahaf D. (2017). Accelerating Innovation Through Analogy Mining. KDD 2017 ; arXiv 1706.05585.
- URL : https://arxiv.org/pdf/1706.05585 — fichier `hope2017.pdf`, sha256 `a98a603544058cb47166300834984183d93fe909db214087fb67f7414e858dfa` (9 pages).

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Méthode : vecteurs séparés du but et du mécanisme, appris sur des annotations de la foule | p. 1 | « “problem schemas”, which specify the purpose of a product and the mechanisms by which it achieves that purpose » | lu sur PDF, p. 1 |
| Analogies lointaines = même but, mécanisme éloigné | p. 2 | « find far analogies – products with high purpose similarity, and low mechanism similarity » | lu sur PDF, p. 2 |
| Gain annoncé | p. 2 | « increasing the relative proportion of positively-rated ideas by at least 25% » | lu sur PDF, p. 2 |
| Précision de rappel, tableau 2 : TF-IDF 0,63 au 1 % du haut, but et mécanisme concaténés 0,696, mécanisme seul 0,739 | p. 6 | (tableau 2) | lu sur PDF, p. 6 |
| Plan : 38 travailleurs de la plateforme de microtravail d'Amazon, trois conditions (méthode, TF-IDF, hasard), 12 inspirations | p. 7 | « We recruited 38 AMT workers to redesign an existing product » ; « BASELINE: RANDOM: participants receive 12 product inspirations sampled at random » | lu sur PDF, p. 7 |
| Juges : cinq doctorants, critère nouveauté, qualité, faisabilité ; accord kappa de Fleiss 0,51 | p. 8 | « We recruited five graduate students to judge each idea » ; « with a Fleiss kappa of 0.51 » | lu sur PDF, p. 8 |
| k = 2 (9 graines communes) : 46 % méthode, 37 % hasard, 30 % TF-IDF | p. 8 | « The proportion of good ideas in our condition was 46% (N = 105). Next was the random baseline with 37% (49), and finally the TF-IDF baseline achieved 30% (N=54). » | lu sur PDF, p. 8 |
| k = 3 : 38 %, 22 %, 21 % | p. 8 | « 38% (N = 118). Next-up was the random baseline with 22% (68), and finally the TF-IDF baseline achieved 21% (N=63) » | lu sur PDF, p. 8 |
| Modèle à effets aléatoires, k = 2 : pr(Good) 0,71 [0,48 ; 0,87], TF-IDF 0,28, hasard 0,27 | p. 8 | « pr(Good) = 0.71, 95% confidence interval = [0.48, 0.87] in our condition. TF-IDF had pr(Good) = 0.28 [0.16, 0.44], and random had pr(Good) = 0.27 [0.16, 0.41] » | lu sur PDF, p. 8 |
| Limite (intervalles larges) | p. 8 | « Replications of this experiment, possibly with more data, could yield results somewhere in between, with more precise estimates on the true size of the effect. » | lu sur PDF, p. 8 |
| Limite (représentation) | p. 9 | « our purpose and mechanism vectors did not distinguish between higher and lower level purposes/mechanisms, or core/peripheral purposes/mechanisms, and also did not encode dependencies » | lu sur PDF, p. 9 |

À noter dans le texte : avec k = 2, la base au hasard (37 %) dépasse la recherche par mots TF-IDF (30 %).

## 3. Kang et al. 2022 (Augmenting Scientific Creativity with an Analogical Search Engine)

- Référence : Kang H. B., Qian X., Hope T., Shahaf D., Chan J., Kittur A. (2022). Augmenting Scientific Creativity with an Analogical Search Engine. *ACM TOCHI* ; arXiv 2205.15476 v1.
- URL : https://arxiv.org/pdf/2205.15476 — fichier `kang2022.pdf`, sha256 `7a8fe7ececfe743cfc5b1cbebb73addd72cf39b89d9ed3b5b52a9db98514a554` (36 pages).

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Étude 1 : huit chercheurs diplômés recrutés ; deux sans assez d'articles dans le moteur | p. 9-10 | « We recruited eight graduate (four women) researchers » ; « the search engine did not contain enough papers for two of the participants » | lu sur PDF, p. 9-10 |
| Filtrage humain dans la boucle, environ 26 % d'erreur du modèle 1 | p. 6 | « (about 12/45 = 26% error rate) » | lu sur PDF, p. 6 |
| Adaptation créative 5,3 fois plus fréquente avec les articles analogiques (53 contre 10) ; application directe surtout par les mots (3 contre 16) | p. 13 | « Creative adaptation is 5.3 times more frequent among analogy papers (53 in Analogy vs. 10 in Keyword), while most of direct application is from keyword papers (3 in Analogy vs. 16 in Keyword). » | lu sur PDF, p. 13 |
| Nouveauté jugée 2,7 contre 2,3 (échelle en 3 points) | p. 13 | « higher in Analogy: 2.7 (SD: 0.48) than in Keyword: 2.3 » | lu sur PDF, p. 13 |
| La correspondance partielle du but médiatise l'effet, la nouveauté du contenu ne le médiatise pas | p. 16 | « the effect of condition (Keyword vs. Analogy) on the binary outcome of creative adaptation was mediated by the degree of purpose-match, but not by the novelty of content » | lu sur PDF, p. 16 |
| Taux d'adaptation créative : mots, correspondance complète 0 %, partielle 21 % ; analogie, partielle 47 % | p. 17 | « Analogy Part 47% vs. Keyword Part 21% » ; « (Keyword Full, 0%) to the keyword papers that partially match in purpose (Keyword Part, 21%) » | lu sur PDF, p. 17 |
| Revers : beaucoup de correspondances partielles ne donnent rien | p. 18 | « a large portion of them also resulted in no ideation outcome (38%) » | lu sur PDF, p. 18 |
| Limites : codeurs non experts, qualité non mesurée, pas d'ablation du filtrage humain, seule base = mots | p. 28 | « it is possible that they judged ideas differently from domain experts » ; « domain-expert-judged idea quality are largely inaccessible within the studies presented here » ; « future work may add ablation studies to quantify the effects of human filtering » | lu sur PDF, p. 28 |
| Biais d'échantillonnage voulu | p. 28 | « analogical papers were sampled twice as much as keyword papers » | lu sur PDF, p. 28 |

## 4. Alvarez-Melis et Jaakkola 2018 (Gromov-Wasserstein Alignment of Word Embedding Spaces)

- Référence : Alvarez-Melis D., Jaakkola T. (2018). Gromov-Wasserstein Alignment of Word Embedding Spaces. EMNLP 2018 ; arXiv 1809.00013.
- URL : https://arxiv.org/pdf/1809.00013 — fichier `alvarez2018.pdf`, sha256 `8fa1fe59c389dd233a64b21e17bdd913a0ccb31009d1456c44c2ebb601486af9` (10 pages).

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Non convexe, tenseur d'ordre 4 | p. 4 | « the objective is now not only non-linear, but non-convex too. In addition, it requires operating on a fourth-order tensor » | lu sur PDF, p. 4 |
| Difficulté de calcul (note 1) | p. 4 | « the discrete (Monge-type) formulation of the problem is essentially an instance of the well-known (and NP-hard) quadratic assignment problem (QAP). » | lu sur PDF, p. 4 |
| Tableau 1 (exactitude au premier rang, sans supervision) : G-W λ = 10⁻⁵ : EN→ES 81,7, EN→FR 81,3, EN→DE 71,9, EN→IT 78,9, EN→RU 45,1 (RU→EN 43,7) ; Procrustes à 5 000 paires : EN→RU 47,2 ; Conneau et al. : 52,4 ; temps 37 min contre 957 min | p. 7 | « Table 1: Performance (P@1) of unsupervised and minimally-supervised methods on the dataset of Conneau et al. (2018). The time columns shows the average runtime in minutes » | lu sur PDF, p. 7 |
| Paires éloignées : apprentissage plus lent | p. 6 | « More related languages (e.g., EN→FR in 2b,2a) lead to faster optimization, while more distant pairs yield slower learning curves (EN→RU, 2c). » | lu sur PDF, p. 6 |
| Échec sous géométries inégales | p. 7 | « the wide discrepancy between word distance across languages, which translates into uneven distance matrices (Figure 3), and in turn leads to poor results for G-W » | lu sur PDF, p. 7 |
| Taille : mise à l'échelle par une seconde étape | p. 5 ; p. 9 | « it is best suited to small-to-moderate vocabulary sizes, since its optimization becomes prohibitive for very large problems » ; « scaling up to large vocabularies made it necessary to learn an explicit mapping via Procrustes » | lu sur PDF, p. 5 et 9 |
| Aucune paire connue utilisée | p. 5 | « at no point we use train (let alone test) supervision » | lu sur PDF, p. 5 |
| Sensibilité à l'initialisation | p. 3 | « is sensitive to initialization » : la phrase porte sur l'approche antérieure (Zhang et al. 2017b), pas sur la leur | lu sur PDF, p. 3 |

## 5. Recombinaison de parents éloignés (Drummond et al. 2005)

- Référence : Drummond D. A., Silberg J. J., Meyer M. M., Wilke C. O., Arnold F. H. (2005). On the conservative nature of intragenic recombination. *PNAS* 102(15), 5380-5385. doi:10.1073/pnas.0500729102.
- URL : https://authors.library.caltech.edu/records/dta0d-msr84/files/DRUpnas05a.pdf?download=1 (dépôt de Caltech ; l'interface d'Europe PMC a répondu par une erreur 500 pour PMC556249).
- Fichier : `drummond2005.pdf`, sha256 `416bb145a45189d67c38652c0f1d335de9c4696fd21d1bb17f8f1ab0526a75a1` (6 pages ; page 1 = p. 5380 imprimée).

| Affirmation | Page fichier (imprimée) | Citation verbatim | Statut |
|---|---|---|---|
| Résultat principal | p. 1 (5380) | « among β-lactamase variants containing the same number of amino acid substitutions, variants created by recombination retain function with a significantly higher probability than those generated by random mutation » | lu sur PDF, p. 1 |
| Parents : 43 % d'identité ; 31 chimères fonctionnelles ; seuil de sélection bas | p. 3 (5382) | « PSE-4 and TEM-1 β-lactamases (43% amino acid identity and 0.98-Å backbone rms deviation) » ; « A total of 31 functional chimeras were identified » ; « an ampicillin concentration that is approximately two orders of magnitude lower than the minimal inhibitory concentrations » | lu sur PDF, p. 3 |
| 54 % de tolérance par substitution (mutation) contre au moins 79 % (recombinaison) | p. 3 (5382) | « the individual amino acid substitutions created by error-prone PCR are tolerated 54% of the time versus at least 79% for substitutions created by recombination » | lu sur PDF, p. 3 |
| Forme : déclin exponentiel pour la mutation, parabolique en logarithme pour la recombinaison, au plus bas à mi-chemin | p. 3 (5382) | « the logarithm of the minimum fraction of functional chimeras has a parabolic shape with its vertex found near the substitution level farthest from both parents (m = 75) » | lu sur PDF, p. 3 |
| Extrapolation à mi-chemin | p. 3 (5382) | « recombination is at least 16 orders of magnitude more effective than random mutation at creating the most highly substituted chimeras » (extrapolation de la courbe de mutation) | lu sur PDF, p. 3 |
| Bornes de la mesure | p. 3 (5382) | « These data represent a lower bound on the fraction of functional chimeras. » | lu sur PDF, p. 3 |
| Protéines sur réseau simulées : la tolérance à la recombinaison décroît avec la distance entre parents, faiblement | p. 4 (5383) | « The values of ρ anticorrelated with sequence distance D with high significance but low variation (mean R2 = 0.75; mean slope, −0.002). » | lu sur PDF, p. 4 |
| Domaine testé en simulation : 20 % à 80 % d'identité | p. 5 (5384) | « for homologs sharing 80% to as little as 20% of their primary sequence, in support of the idea that, at least for these simulated proteins, recombinational tolerance is a property of the structure » | lu sur PDF, p. 5 |

- Les contacts rompus (modèle SCHEMA, Voigt et al. 2002) ne sont pas traités dans cet article ; Voigt 2002 n'est pas lu.

## 6. DreamCoder (Ellis et al. 2021)

- Référence : Ellis K. et al. (2021). DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning. PLDI 2021 ; arXiv 2006.08381 (le PDF arXiv est la version longue de 22 pages).
- URL : https://arxiv.org/pdf/2006.08381 — fichier `dreamcoder.pdf`, sha256 `547027556f1220f22555c35f91d2527d78d825553a1b24201f58d56274ec0e80`.

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Ablations comparées : sans modèle de reconnaissance, sans abstraction ; bases « Memorize » | p. 10 et 13 | « ablations missing either the neural recognition model (the “dreaming” sleep phase) or ability to form new library routines (the “abstraction” sleep phase) » | lu sur PDF, p. 10 |
| Résultat global | p. 13 | « each of DreamCoder’s core components – library learning with refactoring and compression during the sleep-abstraction phase, and recognition model learning during the sleep-dreaming phase – contributes substantively to its overall performance » | lu sur PDF, p. 13 |
| Seul chiffre en texte | p. 13 | « LOGO graphics and tower building, where no alternative model ever solves more than 60% of held-out tasks while DreamCoder learns to solve nearly 100% of them » | lu sur PDF, p. 13 |
| Profondeur de bibliothèque et réussite | p. 13 | « deeper libraries correlate well with solving more tasks (r = 0.79) » | lu sur PDF, p. 13 |
| Coût | p. 13 | « typically takes around a day using moderate compute resources (20-100 CPUs) » | lu sur PDF, p. 13 |
| Réutilisation entre tâches d'un même domaine (lois physiques) | p. 14 | « after 8 wake/sleep cycles DreamCoder learns 93% of the laws and identities » ; « the inverse square law schema that enables it to learn Newton’s law of gravitation and Coulomb’s law » | lu sur PDF, p. 14 |
| Limite | p. 16 | « We focused here on problems where the solution space is well captured by crisp symbolic forms » ; « much real-world data is far messier » | lu sur PDF, p. 16 |

- Les parts de tâches résolues avec et sans abstraction, domaine par domaine, ne figurent que dans les courbes de la figure 6A (p. 14), pas dans le texte : non relevées. Je n'ai trouvé aucune expérience de réutilisation d'une bibliothèque d'un domaine vers un autre : chaque bibliothèque est apprise dans son domaine (« grow a domain-specific language »). C'est une absence dans ma lecture, pas une affirmation des auteurs.

## 7. Prédiction de liens à date gelée (Krenn et al. ; Gu et Krenn)

### 7a. Krenn et al.
- Référence : Krenn M. et al. arXiv 2210.00881 v1 (23 sept. 2022), titre de la v1 : « Predicting the Future of AI with AI: High-Quality link prediction in an exponentially growing knowledge network ». Le titre de *Nature Machine Intelligence* 2023 est celui de la consigne ; la version de la revue n'est pas lue.
- URL : https://arxiv.org/pdf/2210.00881 — fichier `krenn2023.pdf`, sha256 `88a48f8de98e000b2ad381838f9106a1a8344247b79b63e01f50f2fee346ec46` (13 pages).

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Ce qui porte le signal | p. 1 | « Surprisingly, the most powerful methods use a carefully curated set of network features, rather than an end-to-end AI approach. » | lu sur PDF, p. 1 |
| Comparaison des méthodes | p. 6 | « Surprisingly, using purely network theoretical features without machine learning works competitively. Pure ML methods were not yet able to outperform those that use hand-crafted features. » | lu sur PDF, p. 6 |
| Aires sous la courbe | p. 6 | « While the prediction of new links can reach an AUC of up to 93%, we find that the prediction of links that are generated at least three times can be solved with AUC>99.5% » (le PDF imprime « AUC¿99.5% ») | lu sur PDF, p. 6 |
| Trait le plus important (méthode M3) | p. 7 | « We found that the degree centrality of the nodes is the most important feature » | lu sur PDF, p. 7 |
| Ce qui est prévisible n'est pas surprenant | p. 9 | « predicting the most likely new connection between concepts does not necessarily directly coincide with the goal of suggestions of new surprising research directions. After all, those links are predictable, thus potentially not surprising by themselves. » | lu sur PDF, p. 9 |
| Ni l'importance ni l'impact ne sont prédits | p. 9 | « This prediction however does not say anything about the potential importance and impact of the new connection. » | lu sur PDF, p. 9 |
| Paires à grande distance dans le graphe | aucune page | rien trouvé (recherche de « distance », « shortest path ») | non trouvé |

### 7b. Gu et Krenn
- Référence : Gu X., Krenn M. Forecasting high-impact research topics via machine learning on evolving knowledge graphs. arXiv 2402.08640 v4 (11 juin 2025).
- URL : https://arxiv.org/pdf/2402.08640 — fichier `gu2024.pdf`, sha256 `6b3d29db7cd6f7dec0c10afb5f6612e598d0e9fc8ece4eb72b34e652c6630fdb` (18 pages).
- Ce qui est prédit : l'impact (citations au-delà d'un seuil) de paires non encore reliées, pas seulement l'apparition du lien.

| Affirmation | Page | Citation verbatim | Statut |
|---|---|---|---|
| Aires sous la courbe | p. 1 | « AUC values beyond 0.9 for most experiments » ; figures 6-7, p. 7-8 : réseau dense, transformeur, forêt et XGBoost tous entre ≈ 0,93 et 0,98 | lu sur PDF, p. 1, 7, 8 |
| Traits faits à la main : 141 par paire | p. 4 | « calculated 141 features for each pair. These features include 41 network features, divided into 20 node features (such as the number of neighbors and PageRank [43] over the past three years) and 21 edge features » | lu sur PDF, p. 4 |
| Aucun accès au graphe entier | p. 9 | « All of our models use the same set of input features and do not directly access the full knowledge graph. » | lu sur PDF, p. 9 |
| Le bout en bout reste à essayer | p. 9 | « Exploring more end-to-end approaches that integrate more information from the entire knowledge graph could reveal whether such methods can outperform the models and hand-crafted features demonstrated in this work. » | lu sur PDF, p. 9 |
| Paires peu semblables (proxy de distance : similarité cosinus des voisinages) | p. 6 (figure 5) | « Concepts with low similarity and low degree yet predicted to have high impact could be surprising and offer interesting suggestions. » (figure descriptive, sans mesure d'exactitude par distance) | lu sur PDF, p. 6 |

## 8. Évaluation datée de la découverte fondée sur la littérature (Yetisgen-Yildiz et Pratt)

- L'article visé, Yetisgen-Yildiz M., Pratt W. (2009), *Journal of Biomedical Informatics* 42(4), 633-643, doi:10.1016/j.jbi.2008.12.001, n'a pas de PDF en accès libre trouvé : non lu. Je n'ai rien tenté au-delà d'une recherche.
- Lu à la place : le chapitre des mêmes auteurs, « Evaluation of Literature-based Discovery Systems » (2009, chapitre d'ouvrage chez Springer, de mémoire, à vérifier). URL https://faculty.washington.edu/melihay/publications/LBDChapter2009.pdf ; fichier `yetisgen_chapitre2009.pdf`, sha256 `039a6519caea736b258862d44ad2c09d1f02fd10b1ec3a5e364d431a566d21d8` (13 pages).
  - p. 7 : coupure au 1er janvier 2004, test de janvier 2004 à septembre 2005 : « a baseline set including only publications before a selected cut-off date, and (2) a test set including only publications between the cut-off date and another later date ». Lu sur PDF, p. 7.
  - p. 8 : « its main drawback is that the calculated precision for target terms is the lower bound. The target term gold standard only includes the new correlations that are published between the cut-off date and the date of the experiment. » Lu sur PDF, p. 8.
  - Ce chapitre ne donne aucune valeur chiffrée de précision ni de rappel dans les passages lus.

## Non vérifié
- Yetisgen-Yildiz et Pratt 2009 (*Journal of Biomedical Informatics*) : PDF non trouvé en accès libre, aucun chiffre de précision ni de rappel.
- Voigt, Martinez, Wang, Mayo et Arnold 2002 (*Nature Structural Biology*), contacts rompus et modèle SCHEMA : non téléchargé.
- MAC/FAC (Forbus, Gentner et Law) : seul le résumé est lu ; l'année de la revue (1994 sur le PDF, 1995 selon ma mémoire) est à vérifier.
- Gentner 1993, tableau de simulation p. 18 : en-têtes des deux colonnes non lus.
- DreamCoder : les parts de tâches résolues avec et sans abstraction, par domaine, ne se lisent que sur la figure 6A, non relevées ; pas trouvé de transfert d'une bibliothèque entre domaines.
- Krenn et al. : version de *Nature Machine Intelligence* 2023 non lue (seule l'arXiv v1, titre différent) ; aucun résultat par distance dans le graphe.
- Gu et Krenn : importance relative des traits non lue ; pas d'exactitude rapportée par distance.
- Hope 2017 et Kang 2022 : numéros de page de la version publiée (KDD, TOCHI) non vérifiés, seule la version arXiv est lue.
