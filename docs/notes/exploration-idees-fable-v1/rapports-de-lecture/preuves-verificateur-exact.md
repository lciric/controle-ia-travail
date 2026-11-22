# Exploration structurée contre tirage répété, sous vérificateur exact : ce que les articles montrent

Dossier des sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/preuves-verificateur-exact/`. Pages = pages du fichier PDF (numéro imprimé identique sauf mention). Les valeurs « lues sur figure » sont approximatives (lecture d'une courbe, pas d'un tableau).

## Verdict
La preuve publiée en faveur de l'évolution tient à des ablations internes, en général à nombre de propositions égal, sur peu de graines, souvent une seule tâche. Les contre-épreuves de 2026, qui contrôlent l'invite, l'espace de recherche et le coût en jetons, trouvent que le tirage indépendant ou presque indépendant fait souvent jeu égal. Une seule marge nette survit (le problème des triangles de Heilbronn, environ 23 à 28 %).

## 1. FunSearch (Romera-Paredes et al., Nature 2024, « Mathematical discoveries from program search with large language models »)
- Fichier : `docs/sources/exploration-idees-v1/romera-paredes-2023-funsearch-nature-v1.pdf`, sha256 `52c4992d…f392ce` (empreinte complète : 52c4992d0da617eef8f1571b294e011f4903da5fde206542e5fa4c778bf392ce). Les ablations sont dans les informations supplémentaires, absentes de ce PDF ; je les ai trouvées et lues : `funsearch-si.pdf` (static-content.springer.com, MOESM1), sha256 ee6f3651fb8dd11f61fe9055e0fafab25b91fa5b30062dafe0833b4f31eeea19, 39 p.
- **Procédé** (lu sur PDF, p. 3 et 9) : base de programmes divisée en m îles. On tire une île au hasard, puis k = 2 programmes de cette île : « best-shot prompting » (p. 3). Dans une île, les programmes sont groupés par signature (scores sur les entrées). On tire un groupe par sélection de Boltzmann sur le score, puis un programme qui favorise les plus courts (p. 9). Remise à zéro : « Every 4 h, we discard all the programs from the m/2 islands whose best instances have the lowest score » ; chacune est réensemencée avec le meilleur programme d'une île survivante (p. 9). L'ordre de grandeur est « 10^6 » tirages (p. 2).
- **Ablations** (informations supplémentaires, PDF p. 3-4, p. 3 imprimée, fig. A.1). Tâche : ensemble admissible I(15,10), 5 graines, axe des x « Programs Generated » jusqu'à 2,5·10^6, donc **budget égal en programmes**. « W/O Evolution » = « only the initial (user-provided) prompt is used to generate a large number of programs » : c'est exactement le tirage répété. Lu sur la figure : FunSearch ≈ −60, une seule île (« Less Diversity ») ≈ −100, sans évolution ≈ −245, sans squelette ≈ −205 (écart à la taille pleine). Taille pleine atteinte : 2/5 pour FunSearch, 1/5 sans fusion (k = 1), 0/5 pour les autres. Texte : « the use of a skeleton and the evolution of prompts are particularly critical ».
- Mutations au hasard sans modèle de langage (PDF p. 5-6, fig. A.2) : nettement pires. Note de bas de page p. 6 : « Even after leaving “Random” generate more than 50 million programs, none of the runs were able to surpass −240 ».
- Robustesse (article, p. 9) : « only four out of 140 experiments discovering a cap set of size 512 ».
- **Ce que l'article ne montre pas** : l'ablation porte sur une seule tâche, avec 5 graines et sans test statistique. Le tirage sans évolution n'est pas comparé sur la cap set ni sur le bin packing. Le coût est compté en programmes, pas en jetons : une invite évolutive porte 2 programmes, l'invite fixe un seul.

## 2. AlphaEvolve (Novikov et al., arXiv 2506.13131)
- `alphaevolve.pdf`, sha256 f092c8cbd65da89951ee6496374da9a54963f9035758c25ac6e4625f506df9ad, 44 p.
- **Base de programmes** (p. 8, § 2.5) : « inspired by a combination of the MAP elites algorithm [74] and island-based population models ». Aucun autre détail.
- **Ablations** (p. 17-18, § 4, fig. 8). Deux tâches : décomposition de tenseurs pour la multiplication de matrices et nombres d'embrassement. Trois graines. Axe : « Fraction of compute budget », donc **budget égal, en fraction de calcul**. « No evolution » = « repeatedly feeds the same initial program to the language model » (p. 17), c'est-à-dire le tirage répété.
- Lu sur la figure (p. 18). Tenseurs : méthode complète ≈ −2 ; sans méta-invite, petit modèle seul, sans contexte et sans évolution du fichier entier entre −2,5 et −3,5 ; sans évolution ≈ −6,5. Embrassement : complète ≈ −4, sans évolution ≈ −25, sans contexte ≈ −30. Texte : « each of the components is responsible for a significant improvement ».
- **Ne montre pas** : aucun chiffre en tableau, métrique agrégée sur des cibles non listées, trois graines, pas d'intervalle entre méthodes. La mesure du budget n'est pas définie (appels ou jetons ?). Aucune ablation des îles ni de MAP-Elites séparément.

## 3. Darwin Gödel Machine (Zhang, Hu, Lu, Lange, Clune, arXiv 2505.22954 v. ICLR 2026)
- `dgm.pdf`, sha256 13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de, 72 p.
- **Procédé** : archive d'agents. Le parent est choisi avec une probabilité non nulle pour tout nœud, « roughly proportional to their performance score and number of children » (p. 25).
- **Références comparées** (p. 6) : « w/o open-ended exploration » = « eliminates the use of an archive and always self-modifies the latest stored version » ; « w/o self-improve » = méta-agent figé (façon ADAS) ; « DGM Greedy » = « always selects the best-performing node » (p. 25).
- **Chiffres** (tableau 1, p. 25) : SWE-bench 50,0 % (DGM), 23,0 % (sans exploration ouverte), 39,0 % (sans auto-amélioration), 39,7 % (glouton). Polyglot : 38,0 / 14,0 / 28,0 / 30,0 %. Courbes p. 7, sur 80 itérations.
- **Budget** : itérations égales (80), mais **coût inégal** : « about USD 22,000 » pour une course de la machine contre « about USD 10,000 » pour chaque base (p. 32). Les comparaisons semblent reposer sur une course par bras. Trois courses existent seulement pour la machine elle-même sur Polyglot : 40,7 ± 2,3 % (p. 26).
- **Ne montre pas** : aucune référence de tirage répété indépendant. Pas de graines multiples pour les bases. Le choix se fait sur des sous-ensembles du même banc que le score rapporté (Polyglot complet évalué seulement pour le meilleur agent, p. 6). Ce n'est pas un vérificateur de découverte au sens strict.

## 4. ShinkaEvolve (Lange, Imajuku, Cetin, arXiv 2509.19349)
- `shinka.pdf`, sha256 ee287343c53240126e16a444d5ade2cd0ad0f290a400e78b97a040b93d965087, 52 p.
- **Procédés** (p. 3-5) : choix du parent par loi de puissance sur le rang, ou pondéré, avec sigmoïde de la performance et pénalité sur le nombre d'enfants. Rejet des candidats dont la similarité d'enchâssement dépasse 0,95, juge de nouveauté optionnel (p. 11). Choix du modèle par bandit UCB1 (p. 5). Îles avec élitisme (configurations p. 21).
- **Ablations** (p. 10-11, fig. 9). Seulement l'empilement de cercles (26 cercles), jusqu'à 150 propositions évaluées, donc **budget égal en propositions**. « The Best-of-N baseline ignores the evolutionary history, always using the initial program as parent ». Lu sur la figure : meilleur de N ≈ 2,45, escalade gloutonne ≈ 2,57, pondéré ≈ 2,63. Le bandit fait mieux qu'un modèle seul (≈ 2,43) et qu'un ensemble fixe ; le rejet fait mieux que l'absence de rejet (≈ 2,48).
- Le texte dit « across all tasks » (p. 10), mais seul l'empilement de cercles est montré.
- **Ne montre pas** : nombre de graines non indiqué, aucune barre d'erreur, une seule tâche. Le meilleur de N part d'un programme initial et d'une invite riche en indices (voir § 9, Gideoni).

## 5. Toledo et al. 2025 (Meta, arXiv 2507.02554 v2)
- `toledo.pdf`, sha256 0b3cba7c7f4b8ac09bbc5814f958df61cc3b62b5cac53efd3908f2dd03ed0cad, 34 p.
- **Cadre** : MLE-bench lite (22 tâches), **budget égal** de 24 h et 1 H200 par course (p. 5), 20 graines (p. 8). Taux de médaille. Le vérificateur n'est **pas exact** : la recherche se guide sur la validation, le score se lit sur un test tenu à part.
- **Avec les opérateurs d'AIDE** (p. 7, fig. 3) : glouton R1 38,18 %, arborescente de Monte-Carlo 34,55 à 36,36 %, évolutionnaire 39,61 %. Texte : « agents using more advances search policies (e.g., MCTS, evolutionary algorithms) gain no advantage, underscoring the operator set as the bottleneck ».
- **Avec les opérateurs AIRA** (p. 9). Glouton 45,5 % contre AIDE glouton 39,8 % : effet des opérateurs seuls. Arborescente de Monte-Carlo R1 ≈ 47 %, évolutionnaire R1 ≈ 43,0 % (fig. 6a, p. 10). Avec o3 : glouton 47,73 % ≈ arborescente 47,27 % (fig. 5).
- **Écart validation/test** (p. 10) : chercher sur le score de test gagnerait 9,4 et 12,4 points (arborescente, évolutionnaire), et 15 à 16,6 points (gloutons).
- **Ne montre pas** : aucun tirage répété indépendant. La comparaison oppose des politiques entre elles, avec un juge bruité. Les classements changent dans le temps : « Meaningful divergence in performance appears only after 19 hours » (p. 10).

## 6. Audran-Reiss et al. 2025, « What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity » (arXiv 2511.15593)
- Titre et auteurs vérifiés sur PDF, p. 1 : Audran-Reiss, Armengol-Estapé, Hambardzumyan, …, Bachrach (FAIR at Meta, UCL, MSL, UBC). `ideation.pdf`, sha256 1713c15073d03844083a969e30e417b41b7e2bc62c3f04015fade80f3219be73.
- **Mesure** (p. 2 et 5) : « Shannon entropy … on the distribution of model architectures that the agent plans to implement ». Corpus de 11 000 trajectoires (p. 2). Corrélation avec le taux de médaille : « Pearson r = 0.57 » (p. 1, fig. 1). Avec d'autres métriques, r = 0,72 et 0,66 (p. 9).
- **Expérience contrôlée** (p. 5 et 8) : 22 tâches, 10 graines. Le bras appauvri retire la complexité adaptative et la mention de diversité, **et demande explicitement des idées semblables** (p. 5). Médaille : AIRA glouton 45,5 → 38,6 (−6,9), arborescente 47,0 → 38,6 (−8,4) (p. 8). Les soumissions valides tombent de 98 % à 92 % et 90 % (p. 9). Environ la moitié de la baisse vient de deux compétitions où l'agent réessaie T5 et échoue (p. 9).
- **Ne montre pas** : le bras appauvri n'est pas neutre (l'invite pousse vers l'uniformité). Aucune comparaison au tirage indépendant. Juge bruité (validation et test).

## 7. Large Language Monkeys (Brown et al., arXiv 2407.21787 v3)
- `monkeys.pdf`, sha256 33889c6cb265ae11ed67e50070d3a31cd894036d8c9b404212a38df1783e8884.
- **Loi de couverture** (p. 1, 7-8) : la couverture, part des problèmes résolus par au moins un tirage, croît sur quatre ordres de grandeur ; elle se modélise par « an exponentiated power law », c = exp(a·k^b). SWE-bench Lite : « from 15.9% with one sample to 56% with 250 samples », contre 43 % pour le meilleur à un seul essai (p. 1). CodeContests avec Gemma-2B : 0,02 % → 7,1 % à 10 000 tirages (p. 2).
- **Rôle du vérificateur** (p. 3 et 10) : sur MATH, la couverture passe de 82,9 % à 98,44 %, mais vote majoritaire et modèle de récompense « saturate before reaching 100 samples » (p. 10, fig. 7).
- Vérificateur imparfait même en code : « 11.3% of problems have flaky test suites » (p. 11).
- **Ne montre pas** : aucune comparaison à une recherche guidée. Il s'agit de tâches à solution unique, pas d'optimisation d'un score continu.

## 8. Georgiev, Gómez-Serrano, Tao, Wagner 2025 (arXiv 2511.02864)
- `tao.pdf`, sha256 77b43844077c98c26dfc76ad391cadbbd53d48a1d290ddae575ff4d1bcdef9d2, 81 p.
- **Mode recherche** (p. 3) : faire évoluer des heuristiques de recherche plutôt que des constructions, parce que « for problems where the scoring function is cheap to compute, the sheer brute-force advantage of traditional methods can be hard to overcome ».
- **Limites** (p. 4) : excelle sur un score lisse « possible to ‘hill-climbing’ on », « sometimes struggles otherwise ».
- **Parallélisme** (p. 6) : avec plus de fils, la découverte est plus rapide mais coûte plus d'appels au total.
- **Modèle** (p. 6-7) : sur le problème 6.2, le moins cher sur beaucoup de courses était le plus rentable, mais il échoue sur Nikodym. Les courses qui mêlent des modèles moins chers battent parfois les courses au seul haut de gamme, peut-être par la variance qu'ils ajoutent.
- **Ce qui décide** (p. 7) : le choix du vérificateur, une perte continue plutôt que discrète, la tricherie (« leaky verifier »), et les conseils d'expert dans l'invite : « almost always led to significantly better results ».
- **Ne montre pas** : aucune comparaison au tirage répété ni à une autre recherche, à budget égal.

## 9. Recherche 2025-2026 : résultats négatifs ou d'égalité (lus sur PDF)
**a. Gideoni, Risi, Gal, « Simple Baselines are Competitive with Code Evolution », arXiv 2602.16805 v2, NeurIPS 2026.** `gideoni.pdf`, sha256 42514c0bc84a1be69c235643f549802af9f067cb0fcae9745df007e9a4b20913.
- Deux bases (p. 3) : le tirage indépendant avec choix du meilleur (« IID RS »), et un tirage conditionné sur un sous-ensemble au hasard des programmes qui s'exécutent, « no explicit fitness-based selection ».
- Mêmes modèles (Gemini 2.5), même invite minimale, **budget égal de 20 $** (p. 4).
- Bornes mathématiques, 9 problèmes d'AlphaEvolve (p. 5, tableau 1) : le tirage indépendant égale ou dépasse ShinkaEvolve sur 4/9, le tirage conditionné sur 6/9. Probabilité d'égaler ShinkaEvolve à 20 $ : 41 % et 73 % (fig. 2). Une seule course de ShinkaEvolve par problème (p. 4).
- Avec l'invite experte, ShinkaEvolve retrouve sa borne de cercles 3/3 fois ; avec l'invite minimale, 1/3 (p. 4).
- Changer la formulation fait passer la borne d'incertitude de 0,3521 à 0,3482 pour toutes les méthodes (p. 6).
- Échafaudages (p. 6) : P(Shinka > IID RS) = 0,49 ; tous font moins bien que le vote majoritaire sur le test.
- ALE-Bench, 50 programmes : les deux bases battent ShinkaEvolve sur 8/10 (p. 9).
- MLE-bench, 24 h : le tirage conditionné bat AIDE sur 6/10 (p. 8).

**b. Oved, Pony, Naparstek, Barzelay (IBM), « Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search », arXiv 2609.19799.** `rethink.pdf`, sha256 daaa9353563eca9ca0ced77bb68ce73dc604b96936dafd870ceb4d22af4434a0.
- 3 stratégies (OpenEvolve, EvoX, AdaEvolve), 5 tâches, 40 graines × 200 itérations (p. 2).
- Le classement s'inverse avec le budget : « the strategy worst at one seed is best at forty » (p. 2).
- La référence sans évolution, avec meilleur de N à 8000 appels, est tracée « as a reference, not part of the strategy comparison » (p. 7, fig. 4). Lu sur la figure : elle rejoint EvoX et OpenEvolve sur PRISM, reste sous les trois sur Cloudcast, et colle à EvoX et OpenEvolve sur l'ordonnancement.
- Le meilleur score d'AdaEvolve en ordonnancement (21 277) vient d'un programme qui place 3 transactions sur 300 (p. 12, tableau 4).

**c. Oved et al., « LLM Evolutionary Search Strategies Should be Compared by Tokens », arXiv 2610.23977.** `tokens.pdf`, sha256 aa439be406da477b13b21d9c2243d216acf76bcec2b03923236846e0a0058a84.
- 600 courses rejouées. Une proposition coûte 16 000 à 39 000 jetons, « about six times one independent sample » (p. 1).
- À jetons égaux, après retrait des exploits du correcteur : « Evolution beats independent sampling by 5% or less on 12 of 15 task-method pairs, retaining a 23 to 28% margin on only 3, all on one task » (p. 1). Cette tâche est Heilbronn (p. 3).
- La réplication sur Claude Haiku 4.5 reproduit le partage ; un troisième modèle change l'ampleur (p. 1).

**d. Zhang R., Liu, Lin, Wang, Lu, Zhang Q., « Understanding the Importance of Evolutionary Search in Automated Heuristic Design with LLMs », arXiv 2407.10873 (PPSN 2024).** `ahd.pdf`, sha256 6740349414d6b90ddde305aa31285bbb269cd31686b0f84375994fff887d4976.
- **Sens inverse**, en faveur de la recherche. « Standalone LLMs are highly ineffective on AHD problems, even when granted an order of magnitude more queries » (p. 9). L'escalade (1+1) à 500 requêtes fait mieux que le tirage seul jusqu'à 100 000 essais (p. 9, fig. 2, GPT-3.5, 4 problèmes, 5 courses).
- La (1+1) gloutonne rivalise avec FunSearch, EoH et ReEvo sauf sur un problème (p. 12).
- Budgets inégaux, mais au désavantage de la recherche, ce qui renforce le résultat.

## Tableau de synthèse

| Article | Procédé contre référence | Budget égal ? | Grandeur vérifiée | Résultat (page) |
|---|---|---|---|---|
| FunSearch (informations supplémentaires) | îles + meilleur-dans-l'invite contre même invite répétée | oui, en programmes (pas en jetons) | taille d'un ensemble admissible (exacte) | ≈ −60 contre ≈ −245 ; 2/5 contre 0/5 (SI p. 4) |
| AlphaEvolve | complet contre « no evolution » | oui, en « fraction of compute » non définie | rang de tenseur, nombre d'embrassement (exacts) | nettement mieux, figure seule, 3 graines (p. 18) |
| Darwin Gödel Machine | archive contre dernier agent ou glouton | itérations égales, coût ×2,2 | SWE-bench, Polyglot (tests) | 50 contre 23 et 39,7 % (p. 25) |
| ShinkaEvolve | parent pondéré contre meilleur de N et glouton | oui, en propositions | somme des rayons (exacte) | ≈ 2,63 contre 2,45 ; une tâche, graines non dites (p. 10) |
| Toledo | glouton, arborescente, évolutionnaire | oui, 24 h | médaille (validation bruitée) | politique sans effet avec les opérateurs d'AIDE (p. 7) ; les opérateurs comptent plus (p. 9) |
| Audran-Reiss | diversité normale contre appauvrie | oui | médaille | −6,9 et −8,4 points (p. 8) |
| Brown | tirage répété seul | sans objet | couverture | 15,9 → 56 % (p. 1) |
| Gideoni | ShinkaEvolve et AIDE contre tirage indépendant ou conditionné | oui, en dollars, programmes ou heures | bornes, ALE, MLE | jeu égal ou mieux pour les bases (p. 5, 8, 9) |
| Oved (jetons) | 3 évolutions contre tirage indépendant | oui, en jetons | 5 tâches | ≤ 5 % sur 12/15, 23-28 % sur Heilbronn (p. 1) |
| Zhang 2024 | (1+1) contre modèle seul | non, au détriment de la recherche | heuristiques combinatoires | la recherche l'emporte (p. 9) |

## Lecture d'ensemble
1. **Établi** : avec un vérificateur exact, le tirage répété croît en couverture selon une loi régulière (Brown). Une boucle qui réinjecte les meilleurs programmes bat l'invite fixe à nombre de programmes égal dans les ablations des concepteurs (FunSearch, AlphaEvolve, ShinkaEvolve, Zhang 2024).
2. **Non établi** : que l'archive, les îles, MAP-Elites ou le bandit apportent quelque chose au-delà d'une réinjection simple, à jetons égaux. Aucune ablation des concepteurs ne mesure en jetons, et aucune n'a assez de graines pour un test.
3. Les contrôles tiers de 2026 (Gideoni ; Oved ×2) trouvent l'égalité dans la plupart des cas une fois l'invite, l'espace et le coût égalisés. La seule marge robuste est sur une tâche (Heilbronn).
4. L'invite, la formulation du problème, les opérateurs et le bruit du vérificateur pèsent plus que la politique de recherche (Gideoni p. 4-6 ; Toledo p. 7 et 10 ; Tao p. 7).
5. Les correcteurs exploitables faussent les comparaisons à grand nombre de graines (Oved p. 12 ; Tao p. 7).

## Non vérifié
- Tsoukalas et al. (cité par Gideoni p. 10 : un pipeline simple rivalise avec AlphaEvolve sur des preuves) : non lu.
- Gideoni, Tang et al., « Random Baselines for Simple Code Problems are Competitive with Code Evolution » (atelier NeurIPS 2025) : vu seulement dans les résultats de recherche.
- Beck et al. 2026 (cité par Oved, jetons, p. 1) : non lu.
- Annexes I et J de Gideoni (efficacité par nombre d'évaluations, autres reformulations) : non lues en détail.
- Annexes des tâches de Toledo (K) et de la Darwin Gödel Machine (paramètres de C.2) : non lues.
- Les valeurs lues sur figure (FunSearch, AlphaEvolve, ShinkaEvolve, Oved fig. 4) sont approximatives.
- Li, « Verifier Noise Is a Temperature » (arXiv 2611.09699) : téléchargé, non lu ; il porte sur des juges bruités, hors de la question.
