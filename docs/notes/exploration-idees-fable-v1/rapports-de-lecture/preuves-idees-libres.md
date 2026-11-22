# Preuves expérimentales sur les idées de recherche en langue libre (lecture du 22 novembre 2026)

Dossier des PDF : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/preuves-idees-libres/`. Les pages citées sont celles du fichier PDF (« p. N ») ; le numéro imprimé est donné quand il diffère. Toutes les sources sont des prépublications arXiv (URL : `https://arxiv.org/pdf/<id>`).

## Empreintes (sha256)

| Fichier | Version lue | sha256 |
|---|---|---|
| 2409.04109.pdf (Si et al. 2024) | v1, 6 sept. 2024 | fc1d14afd403c19bebb1c8ede9e74ed9aa3de0ee3a1f8656a6dcd6c7da90f79c |
| 2506.20803.pdf (Si et al. 2025) | v1 | a0e8327e44d2a0d5e212fbc8a94efcd3d9ff5aac44b504dafed1941c8b5daa96 |
| 2509.26603.pdf (DeepScientist) | v1 | 76c3805b2344c32f3245f0500bcfd8ae129cd221f821da509817121c1485cae8 |
| 2507.00310.pdf (AutoDiscovery) | v3, 12 févr. 2026 (NeurIPS 2025) | 30210132c2cf734607e20d08fd83e707677becd59048cdb6504f9193ef1c1914 |
| 2502.18864.pdf (Co-Scientist) | v2, 29 juin 2026 (révision pour Nature, titre « Accelerating scientific discovery with Co-Scientist ») | e603a77c9d2bdfb528313e4cf35405b72261e018a70da724fcebca94c96e4716 |
| 2504.08066.pdf (AI Scientist-v2) | v1 | 53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2 |
| 2410.07076.pdf (MOOSE-Chem) | v6 (ICLR 2025) | 0d6184da8958f0e8b4e127ea9238ce6dc58cfeebf4dc3c6c2520c66a6583ee4b |
| 2503.21248.pdf (ResearchBench) | v3, 20 avr. 2026 | c8a9b1eac45cc4efbacf4fd23abe16e14c1e86c96cb5e69f7103aecb828b579a |
| 2405.17044.pdf (SciMuse) | v4, 24 sept. 2026 | fcb49a059e17a25c351153a8022717aa594ddc279f6e276e204f1fbe9ce32af4 |
| 2511.02824.pdf (Kosmos) | v2 | bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8 |
| 2402.01727.pdf (Meincke et al.) | document de travail, 27 janv. 2024 | 4efee6c00b31138c67f85048395c8d53f05683749cbd08f747fe73720fb21fc0 |
| 2601.14525.pdf (Si, Yang et al. 2026) | v1 | ad9f9d0d152930510045d485eebb695ab15b8f775e9bfd63313355c591a675d7 |
| 2510.22954.pdf (Artificial Hivemind) | — | c1ac82916d2f76aa501e96a50466030d432c67eec42fdb8ddc11344f83a152fe |
| 2609.33936.pdf (Schaeffer et al., critique) | v1 | ee607c2533055c4f51adcf688377b29a27bf30aef427b99cf4946f936730d37d |
| 2501.19361.pdf (Wenger, Kenett) | v1 | 9ddd9eeb8eed906931d14248b6199a53f29db261c8a9fae6a0420019ad0b4b89 |
| 2607.26587.pdf (Implementation Lottery) | v2 | 145ef4cf20e2aa28e52eadc103b8b47464a03af6db20e4ccd65ec389e051d807 |

## 1. Si, Yang, Hashimoto 2024, « Can LLMs Generate Novel Research Ideas? », arXiv 2409.04109
- **Procédé** : un agent (Claude 3.5 Sonnet) génère 4 000 idées graines par sujet, retire les doublons, classe les idées par comparaisons par paires. Trois bras : idées humaines, idées de l'agent, idées de l'agent reclassées à la main par le premier auteur.
- **Doublons (a)** : encodage all-MiniLM-L6-v2, seuil cosinus 0,8 « based on manual inspection » ; « This leaves about 5% non-duplicated ideas » (lu sur PDF, p. 6, imprimé 4). « out of the 4000 generated seed ideas, there are only 200 non-duplicate unique ideas » ; la part des non-doublons dans chaque nouveau lot baisse et le cumul plafonne (figure 4, p. 13-14, imprimé 11-12). Les auteurs en tirent « a bottleneck on our inference-time scaling » (p. 14).
- **Résultat principal (b)** : 79 relecteurs à l'aveugle. Nouveauté : humains 4,84, idées de l'agent 5,64, agent avec reclassement humain 5,81 (p. 2 ; test à p < 0,01, p. 9). Faisabilité « slightly weaker » (p. 1). Accord entre relecteurs 56,1 % (aléatoire : 50 % ; NeurIPS 2021 : 66,0 %) (p. 13). Le meilleur juge-modèle (Claude-3.5, par paires) n'atteint que 53,3 % (p. 14). 17 des 49 idées seulement sont communes aux bras « classement par le modèle » et « reclassement humain » (p. 7).
- **Ce que l'article ne montre pas** : aucune exécution. Le seuil 0,8 n'est fixé qu'à l'œil. Le chiffre de 200 idées uniques dépend du codeur et du seuil (voir la critique 15 ci-dessous).

## 2. Si, Hashimoto, Yang 2025, « The Ideation-Execution Gap », arXiv 2506.20803
- **Procédé** : essai à affectation aléatoire. 43 experts exécutent une idée, soit humaine (N = 19), soit de la machine (N = 24) ; « Each expert spent over 100 hours » et écrit un article court de 4 pages (p. 1). Les projets exécutés sont relus à l'aveugle par des experts. Mesure : la note humaine du projet exécuté, et non une métrique de tâche.
- **Chiffres** (tableaux 4-5, p. 7). Notes avant exécution, humain contre machine : nouveauté 4,912 contre 5,778, excitation 4,404 contre 5,653, efficacité 4,833 contre 6,003, note globale 4,596 contre 5,382 (toutes à p < 0,05 après correction du taux de fausses découvertes). Après exécution : 4,903 contre 4,729, 4,482 contre 3,896, 4,782 contre 4,125, 3,968 contre 3,406 (aucun écart significatif). Écarts entre les deux temps, idées de la machine : −1,049, −1,760, −1,879, −1,976 ; idées humaines : −0,010, +0,078, −0,052, −0,628. La différence entre ces écarts est significative sur les quatre mesures (p de 0,001 à 0,025). Citation : « AI ideas score below human ideas after execution on all metrics » mais « not statistically significant » (p. 7).
- **Note avant exécution contre résultat (b)** : corrélations faibles. Pour les idées de la machine, excitation r = −0,321 et ρ = −0,386 ; note globale r = −0,092 (tableau 9, p. 26). Retirer les 6 idées dont l'évaluation humaine a été remplacée par une évaluation automatique ne change pas la conclusion (p. 8).
- **Ce que l'article ne montre pas** : l'échantillon est petit. Le résultat reste une note humaine, et non un dommage ou un gain mesuré par programme. Aucun procédé d'exploration n'y est comparé.

## 3. Weng et al. 2025, « DeepScientist », arXiv 2509.26603
- **Procédé** : optimisation bayésienne. Un relecteur-modèle de substitution donne trois notes de 0 à 100 (utilité, qualité, exploration), et une règle de borne supérieure de confiance choisit l'idée à exécuter : « argmax wu vu + wq vq + κ·ve » (p. 5). Gemini-2.5-Pro et Claude-4-Opus ; « Three human experts supervise the process to verify outputs and filter out hallucinations » (p. 5).
- **Entonnoir (p. 2, 8, figure 4)** : environ 5 000 idées, environ 1 100 exécutées, 21 progrès. Par tâche, d'après la figure 4a : détection de texte généré 2 472 / 600 / 7 ; attribution des échecs d'agents 1 330 / 196 / 12 ; accélération de l'inférence 1 077 / 312 / 2. Plus de 20 000 heures de processeur graphique (p. 1). Gains sur l'état de l'art : 183,7 %, 1,9 % et 7,9 % (p. 1).
- **Règle de choix contre le hasard** : « randomly sampling 100 ideas for each task and testing them yields a success rate of effectively zero. With our selection strategy, the success rate rises to approximately 1-3% » (p. 8). Les deux bras n'ont pas le même budget : 100 idées tirées au hasard contre 196 à 600 idées choisies. Aucun intervalle n'est donné.
- **Goulot** : sur 300 échecs examinés, « approximately 60% were terminated prematurely due to implementation errors », et l'essentiel des 40 % restants n'apporte aucun gain (p. 8). La vérification est désignée comme « a critical bottleneck » (p. 16). Avec 4 processeurs graphiques, 1 progrès ; avec 16, 11 progrès, en une semaine (p. 9, une seule course).
- **Ce que l'article ne montre pas** : aucune référence d'exploration à budget égal (ni tirage répété, ni recherche gloutonne). Le progrès est mesuré par exécution sur un banc, mais trois humains filtrent en cours de route.

## 4. Agarwal et al. 2025, « AutoDiscovery : Open-ended Scientific Discovery via Bayesian Surprise », arXiv 2507.00310
- **Procédé** : recherche arborescente de Monte-Carlo à élargissement progressif. La récompense est la surprise bayésienne, c'est-à-dire le déplacement de la croyance du modèle entre avant et après l'expérience sur les données. 21 jeux de données.
- **Références** : tirage répété, recherche linéaire, recherche gloutonne, faisceau de largeur 8. Le budget est égal : « the exploration budget (500 in all experiments) » (p. 6).
- **Chiffres** : « 5-29% more discoveries deemed surprising by the LLM » (p. 1). La recherche de Monte-Carlo est la meilleure sur 17 des 21 jeux de données (p. 8). La grandeur est la surprise jugée par le modèle lui-même.
- **Validation humaine** : 1 620 hypothèses, 3 annotateurs de niveau master ou doctorat. Part jugée surprenante par les humains : 0,67 avec la récompense « surprise bayésienne », contre 0,11, 0,15 et 0,21 avec les récompenses « surprise déclarée », « intérêt » et « utilité » du modèle (tableau 2, p. 8 ; intervalle à 95 % : [0,63 ; 0,71]). Ce tableau compare des récompenses, et non des procédés de recherche. Intérêt et utilité jugés par les humains : 0,73 à 0,80 pour toutes les récompenses (tableau 1, p. 8), donc rien ne les sépare. Validité des expériences 98,58 % et de leur mise en œuvre 98,01 % sur 175 nœuds (p. 9).
- **Ce que l'article ne montre pas** : si les découvertes sont vraies, répliquées ou utiles hors de l'échantillon. La recherche contre les références est jugée par le modèle seul.

## 5. Gottweis et al. 2025, « Towards an AI co-scientist », arXiv 2502.18864 (lu en v2, juin 2026)
- **Procédé** : système à plusieurs agents. Tournoi à classement Elo par débats, agent d'évolution, mémoire de contexte.
- **Davantage de calcul, meilleure qualité ?** Le classement Elo des hypothèses monte au fil des dix tranches de temps, sur 203 objectifs (p. 7-8). Les auteurs écrivent eux-mêmes : « the Elo metric is auto-evaluated and not based on independent ground truth » (p. 10). Pour ancrer l'Elo, ils regardent sa concordance avec l'exactitude sur GPQA diamant : 78,4 % au premier rang (p. 45). Effet de l'agent d'évolution sur GPQA : 70,9 % → 75,4 %, « absolute increase of 4.5% [95% CI: -2%, 11%] » (p. 54) ; l'intervalle contient zéro.
- **Experts** : 11 objectifs, 7 experts qui ont aussi rédigé les objectifs. Rang moyen de préférence 2,36 ; nouveauté 3,64 et impact 3,09 sur 5 (p. 11). Citation : « These evaluations reflect subjective expert assessments, not objective ground truth » (p. 11).
- **Laboratoire** : leucémie aiguë myéloïde. 30 candidats sont présentés à des oncologues, qui en retiennent 5 ; 3 inhibent la viabilité, dont le binimétinib avec une concentration inhibitrice médiane descendant à 2 nM (p. 13). Fibrose hépatique : 3 cibles, 2 actives sur organoïdes (p. 19). Îlots chromosomiques induits par les phages : l'hypothèse principale correspond à une découverte indépendante et contemporaine, non publiée (p. 19). Citation : « all three validations involved expert-in-the-loop » (p. 7).
- **Ce que l'article ne montre pas** : aucun bras témoin au laboratoire (aucun candidat issu d'un procédé plus simple testé dans les mêmes conditions). Le gain dû au tournoi et à l'évolution n'est mesuré hors du modèle que sur GPQA, un questionnaire à choix multiples, et il n'y est pas significatif.

## 6. Yamada et al. 2025, « The AI Scientist-v2 », arXiv 2504.08066
- **Procédé** : recherche arborescente agentique en quatre étapes, du meilleur d'abord, guidée par un modèle ; gestionnaire d'expériences ; retour d'un modèle de vision (p. 5-7).
- **Résultat vérifié** : 3 manuscrits soumis à un atelier d'ICLR ; un seul obtient 6,33 (notes 6, 7 et 6) et dépasse le seuil d'acceptation (p. 9). Sélection humaine : environ 20 + 20 idées générées, 3 retenues par les auteurs ; plusieurs graines par idée ; « we selected the single best-resulting manuscript for submission » (p. 10). Erreurs de citation relevées (p. 9).
- **Ablation** : je n'ai trouvé dans le PDF aucune ablation de la recherche arborescente contre la v1 linéaire ; le mot « ablation » ne renvoie qu'à l'étape 4 du système.
- **Ce que l'article ne montre pas** : l'effet de l'arbre ; la fréquence de réussite (« not what fraction of the time », p. 10).

## 7a. Yang et al. 2024, « MOOSE-Chem », arXiv 2410.07076 (ICLR 2025)
- **Procédé** : retrouver des inspirations, composer les hypothèses (mutation, recombinaison, en plusieurs étapes), puis les classer. 51 articles de chimie publiés après janvier 2024 ; GPT-4o, dont les données d'apprentissage vont jusqu'à octobre 2023 (p. 1, 7).
- **Inspirations retrouvées** : en gardant 4 % d'un corpus de 300 articles, 83,7 % des inspirations sont retrouvées ; sur 3 000 articles, 86,9 % (tableau 3, p. 7). Llama-3.1-8B : 43,5 % (tableau 5, p. 8). Le corpus est rempli au hasard parmi les 3 000 articles de chimie les plus cités de Nature (p. 7). Les leurres sont donc probablement plus faciles à écarter que des voisins proches ; c'est mon inférence, à rapprocher de ResearchBench ci-dessous.
- **Redécouverte** : avec les vraies inspirations fournies, les experts donnent la note maximale 5 pour 9 articles sur 51 (tableau 7, p. 9). En condition réelle, avec un corpus de 300 articles : experts 0 × 5, 2 × 4, 19 × 3 sur 51 (tableau 11, p. 10). Les références (SciMON, MOOSE, Qi et al.) obtiennent une note maximale de 2,55 à 2,88 contre 4,02, notes données par GPT-4o (tableau 10, p. 10) ; l'égalité de budget n'est pas indiquée.
- **Ce que l'article ne montre pas** : comme les vraies inspirations sont dans le corpus, la tâche est plus facile qu'une découverte réelle ; la comparaison aux références est jugée par un modèle.

## 7b. Liu et al. 2025, « ResearchBench », arXiv 2503.21248 (v3 2026)
- 1 386 articles de 12 disciplines, publiés en 2024 ou plus tard (p. 1, 4). Les leurres sont pris à trois distances : voisins par citation ou par sens, même discipline, autre discipline (p. 4).
- **Chiffres** : au premier tour (20 % gardés), environ 80 % des inspirations retrouvées ; avec 4 % gardés, « accuracy remains above 40%, with GPT-4o leading at 45.65% » (p. 6). La performance plafonne vers 70 milliards de paramètres (p. 6). Citation : « closer papers are more likely to be selected » (p. 6). Les modèles préfèrent donc le proche, ce qui va contre l'idée d'une force sur la littérature éloignée.
- **Ce que l'article ne montre pas** : la contamination n'est que « minimisée » (p. 4). Le banc mesure des sous-tâches, et non la valeur d'une hypothèse neuve.

## 8. Gu, Krenn, « SciMuse », arXiv 2405.17044 (v4, sept. 2026)
- **Procédé** : graphe de connaissances de 58 millions d'articles et GPT-4. 110 chefs de groupe de l'institut Max Planck notent 4 451 idées personnalisées (p. 6).
- **Chiffres** : moyenne 2,40 sur 5 ; note la plus fréquente 1 (36,7 %) ; 24,9 % des idées notées 4 ou 5 (p. 7). Paires de concepts promises à de nombreuses citations 23,3 %, paires au hasard 25,2 %, référence « titres seuls » de GPT 26,2 % (p. 7) : « no evidence that supplying either random or high-citation-predicted concept pairs improves expert-rated interest » (p. 8). Les paires promises à de nombreuses citations sont même un peu moins intéressantes (1,94σ, p. 7).
- **Ce qui prédit l'intérêt** : le degré dans le graphe (ρ = −0,166), le rang de page (ρ = −0,176) et la distance sémantique entre chercheurs (ρ = −0,223) jouent tous négativement (p. 8). Aire sous la courbe : GPT-4o en zéro-coup 67,44 %, réseau supervisé 63,20 %, GPT-3.5 60,39 % ; précision sur les 5 premières idées 49,2 % pour le réseau (p. 9-10). Base humaine de 148 idées : 29,1 % notées 4 ou 5, contre 25,0 % pour GPT-4 et 32,5 % pour GPT-5.2 (p. 8).
- **Ce que l'article ne montre pas** : la mesure est l'intérêt déclaré, sans aucune exécution. La distance se confond avec la proximité au domaine de l'évaluateur, ce que les auteurs signalent (p. 8).

## 9. Mitchener et al. 2025, « Kosmos », arXiv 2511.02824
- **Procédé** : modèle du monde structuré partagé entre un agent d'analyse de données et un agent de lecture de la littérature. Jusqu'à 200 déroulés par course, 42 000 lignes de code et 1 500 articles lus (p. 1).
- **Exactitude** : 102 affirmations tirées de 3 rapports ; 79,4 % exactes. Par type : analyse de données 85,5 %, littérature 82,1 %, synthèse 57,9 % (p. 4). Le nombre de « valuable findings » croît avec les cycles, d'après les collaborateurs, jusqu'à 20 cycles (p. 4). 7 découvertes : 3 reproduisent des résultats non vus, 4 sont nouvelles (p. 1).
- **Limites des auteurs** : « no automated method to reliably evaluate if a claim is accurate, novel, and significant » ; « multiple independent runs may not consistently converge on the same discoveries » (p. 19).
- **Ce que l'article ne montre pas** : aucune comparaison à un autre procédé d'exploration. Les 3 rapports sont dits « representative » mais ont été choisis par les auteurs. La croissance avec les cycles repose sur le jugement des collaborateurs.

## 10. Meincke, Mollick, Terwiesch 2024, « Prompting Diverse Ideas », arXiv 2402.01727
- **Domaine** : des produits de moins de 50 dollars pour étudiants, et non des idées de recherche.
- **Estimation de l'épuisement** : méthode de capture-recapture de Kornish et Ulrich. Une idée est un doublon si son cosinus avec une idée antérieure atteint 0,8 (Universal Sentence Encoder). T (nombre total estimé) est déduit de N (idées générées) et U (idées uniques), calcul en annexe F (p. 8). Réserve des auteurs : on n'estime que les idées « that can be found with a particular technique » (p. 8).
- **Chiffres** : similarité moyenne des groupes d'étudiants 0,243 ; chaîne de raisonnement 0,255 ; consigne de base 0,377 ; 35 consignes testées (p. 3, tableau 2 p. 11). Idées uniques estimées : « from around 3700 for the base prompt to 4700 » (p. 3). La chaîne de raisonnement tourne sur gpt4-1106-preview, les autres consignes sur gpt4-0314 (p. 8-9, tableau 2) : modèle et consigne sont confondus.

## 11. Recherche 2025-2026

**12. Si, Yang, Choi, Candès, Yang, Hashimoto 2026, « Towards Execution-Grounded Automated AI Research », arXiv 2601.14525**. C'est la seule étude trouvée qui compare deux procédés sur un résultat exécuté à budget égal.
- **Procédé** : un exécuteur automatique implémente des idées en langue libre sur deux environnements, le pré-apprentissage nanoGPT et le post-apprentissage GRPO.
- **Recherche évolutive contre meilleur-de-N** : la comparaison porte sur nanoGPT, avec GPT-5, « under the same sampling budget », N ∈ {80, 160, 240} ; « evolutionary search significantly outperforms best-of-N from epoch 1 onward » (p. 5). L'écart sur la figure 4 est petit (récompense 1/perte entre 0,309 et 0,313). Je n'ai vu dans le texte lu ni graines multiples ni intervalle.
- **Meilleurs résultats** : GRPO 69,4 % contre 48,0 % ; nanoGPT 19,7 minutes contre 35,9 minutes (p. 1). La meilleure solution GRPO vient d'un réglage des hyperparamètres et d'un gradient de politique simple (p. 5). Les modèles « saturate early » (p. 1).
- **Apprentissage par renforcement sur la récompense d'exécution** : la moyenne monte, pas le maximum (p. 8). Effondrement de la diversité : 51 sur 128 idées tombent sur deux idées communes à l'époque 0, 119 sur 128 à l'époque 68 (p. 9).

**13. Ning et al. 2026, « The Implementation Lottery », arXiv 2607.26587**. Sur 3 048 affectations et 31 tâches, « all four primary aggregation tests have Holm-adjusted p ≥ 0.56 » ; le gain du code choisi sur une mise en œuvre neuve n'est que de 0,38 [0,08 ; 0,82] point (p. 1). Un seul programme est donc une preuve faible pour une idée (lecture du résumé, p. 1).

**14. Jiang et al. 2025, « Artificial Hivemind », arXiv 2510.22954 (NeurIPS 2025)**. Pour un même modèle, « in 79% of cases, the average similarity exceeds 0.8 », à top-p 0,9 et t = 1,0 (p. 4). Avec min-p, 61,2 % des paires restent au-dessus de 0,8 (p. 5). Entre modèles, la similarité moyenne va de 71 % à 82 % (DeepSeek-V3 contre qwen-max : 0,82) (p. 5). Le corpus est fait de requêtes ouvertes, dont 15,2 % de remue-méninges (p. 3), et non d'idées de recherche.

**15. Schaeffer et al. 2026, critique, arXiv 2609.33936**. Contre une hypothèse nulle plus exigeante (même consigne, idées réellement différentes), « 20%–32% of such pairs already exceed the paper's 0.8 convergence threshold ». Un effet résiduel subsiste : de deux à trois fois plus de dépassements. La consigne augmente de façon fiable la diversité mesurée. « We do not resolve whether the Artificial Hivemind is real » (p. 1). La critique touche directement tout comptage de doublons au seuil de 0,8, celui de Si et al. 2024 compris. C'est mon inférence : le codeur n'est pas le même et l'équivalence reste à vérifier.

**16. Wenger, Kenett 2025, arXiv 2501.19361**. Sur des tests de créativité standard (usages alternatifs et autres), « LLM responses are much more similar to other LLM responses than human responses are to each other » (p. 1). Tâches non scientifiques.

## Synthèse

| Étude | Procédé | Référence | Budget égal | Grandeur, juge | Chiffre clé (page) |
|---|---|---|---|---|---|
| Si 2024 | sur-génération et classement | humains | — | nouveauté, experts | 4 000 → 200 uniques (p. 13) ; 5,64 contre 4,84 (p. 2) |
| Si 2025 | exécution 100 h | idées humaines | — | note d'experts après exécution | écart −1,05 à −1,98 contre ≈0 (p. 7) ; ρ excitation −0,386 (p. 26) |
| DeepScientist | borne supérieure de confiance sur notes de modèle | 100 idées au hasard | non | progrès sur banc, exécution | 5 000 → 1 100 → 21 ; 1-3 % contre ≈0 (p. 8) |
| AutoDiscovery | Monte-Carlo, surprise | tirage répété, glouton, faisceau | oui (500) | surprise du modèle ; humains : surprise | +5-29 % (p. 1) ; 0,67 contre 0,11-0,21 (p. 8) |
| Co-Scientist | tournoi Elo et évolution | modèles de pointe, experts | non | Elo, experts, laboratoire sans témoin | évolution +4,5 [−2 ; 11] (p. 54) ; 3/5 médicaments actifs (p. 13) |
| AI Scientist-v2 | arbre agentique | aucune ablation | — | relecture d'atelier | 1/3 accepté, après sélection humaine (p. 9-10) |
| MOOSE-Chem | inspirations et mutations | 3 systèmes | non dit | correspondance avec l'hypothèse publiée, experts | réel : 21/51 ≥ 3 sur 5 (p. 10) |
| ResearchBench | sous-tâches | modèles | — | inspirations retrouvées | 45,65 % à 4 % gardés ; biais vers le proche (p. 6) |
| SciMuse | graphe de connaissances | titres seuls | oui (16/16/16) | intérêt, 110 chefs de groupe | aucun gain du graphe (p. 7-8) ; aire 67 % (p. 10) |
| Kosmos | modèle du monde | aucune | — | exactitude, experts | 79,4 % ; synthèse 57,9 % (p. 4) |
| Meincke | 35 consignes | groupes d'étudiants | oui (1 000) | cosinus, capture-recapture | 3 700 → 4 700 uniques (p. 3) |
| Si et Yang 2026 | évolution, renforcement | meilleur-de-N | oui | métrique exécutée | évolution > meilleur-de-N (p. 5) ; renforcement : 119/128 idées identiques (p. 9) |
| Hivemind et critique | — | nul facile ou exigeant | — | cosinus | 79 % > 0,8 (p. 4) ; nul exigeant 20-32 % (p. 1) |

**Lecture d'ensemble**
1. La répétition est mesurée partout au seuil cosinus de 0,8 (de 4 000 à 200 idées ; 79 % au-dessus du seuil). La critique de 2026 montre que ce seuil compte comme doublons 20 à 32 % d'idées réellement différentes : l'ampleur exacte n'est pas établie, un effet résiduel l'est.
2. L'écart entre note et résultat est la mieux établie des trois questions : baisse forte après exécution, corrélations nulles ou négatives (Si 2025), 1 à 3 % de réussite (DeepScientist), une affirmation de synthèse sur deux fausse ou presque (Kosmos).
3. Sur un résultat vérifié hors modèle et à budget égal, une seule comparaison de procédés a été trouvée : évolution contre meilleur-de-N sur nanoGPT, écart petit, graines non vues.
4. Les autres gains (Monte-Carlo, tournoi, arbre, graphe) sont jugés par un modèle, par des humains sans exécution, ou n'ont pas de bras témoin. SciMuse et l'intervalle de l'agent d'évolution de Co-Scientist sont des résultats nuls ou non significatifs.
5. L'apprentissage par renforcement sur l'exécution effondre la diversité ; une seule exécution par idée est une preuve faible (Implementation Lottery).

## Non vérifié
- Idea Search (arXiv 2608.08958) : téléchargé (sha256 5dc8c9a575d179077b06c425efdf059ac77323c411b029e8fbf23dbdc69700f5), non lu ; résumé de la recherche seulement.
- ResearchGym (arXiv 2602.15112), « The Multilingual Artificial Hivemind » (NeurIPS 2026), arXiv 2608.19437, 2606.17350 : vus dans les résultats de recherche, non téléchargés.
- Si et Yang 2026 : graines et intervalles de la figure 4 non cherchés dans les annexes.
- Co-Scientist : la v1 de février 2025 n'a pas été lue ; ses chiffres peuvent différer de la v2.
- Annexe F de Meincke (formule de T) non lue ; l'annexe A.1 de ResearchBench (sous-ensemble sans contamination) non lue.
- Équivalence entre le codeur de la critique de Schaeffer et MiniLM-L6-v2 (Si 2024) : non vérifiée.
