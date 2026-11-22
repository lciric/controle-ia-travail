# Procédés de recherche pour la découverte automatique : huit prépublications (juin-octobre 2026)

Question directrice : à budget égal, un procédé d'exploration fait-il mieux que le tirage répété et indépendant, sur des résultats vérifiés par programme ?

Les PDF ont été téléchargés depuis arxiv.org/pdf/ID. Les dates viennent de l'historique de dépôt de la page arxiv.org/abs/ID. Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/recent-strategies/`. Les numéros de page sont ceux du fichier PDF ; ils coïncident avec la numérotation imprimée quand elle existe. Statut de toutes les citations : « lu sur PDF, p. N ». Les valeurs lues sur une figure sont signalées comme approximatives.

| ID | Fichier | sha256 | Dépôt (v1 ; versions suivantes) |
|---|---|---|---|
| 2606.25198 | 2606.25198.pdf | b6f17cd34a259190c748af1d636c2fab0c6617498e3b5d6c9ecc360234a80fa6 | 23 juin 2026 ; v2 1er juill. (fichier lu = v2) |
| 2607.18235 | 2607.18235.pdf | 7d86c5be02d94eb4a492debc6b1d3443dd25421119a6afb181360ca4013b19a7 | 20 juill. 2026 |
| 2610.00707 | 2610.00707.pdf | a4fe6688e040b92c75ee0287e2515022a65671a2a7e037aed7a7d4fac2e605f1 | 30 sept. 2026 |
| 2609.25510 | 2609.25510.pdf | 78d0183ff913809da5a49c2728827dc1575ed20d87c2a12ef288d200285b540a | 22 sept. 2026 ; v2 25 sept. (lu = v2) |
| 2606.05408 | 2606.05408.pdf | 2d55e3af16ebdcf4bd64350115211d62493c98cb3cddb0325691a376a5177185 | 3 juin 2026 |
| 2608.09855 | 2608.09855.pdf | 2e92f9f20a7b33cbf416907e3eaa9355a62425cb0094c859bb0785033a1834e8 | 10 août 2026 ; v2 24 août (lu = v2) |
| 2606.10587 | 2606.10587.pdf | 356fb9a4ce50115da06cca8fe8a1b0f70367c8f522cec5cc792cf9b0860a6f38 | 9 juin 2026 |
| 2608.26081 | 2608.26081.pdf | d6a63c277f30cd590d2f3c27c5c46e9f7b95c2a3e82d75234631553f17bdb4c1 | 26 août 2026 |

---

## 1. Heuresis — Antoniades, Nathani, Saha, Amayuelas, Bercovich, Weng, Baskaran, Bhatia, Wang (UC Santa Barbara ; Hexo AI), arXiv 2606.25198

- **Dispositif (p. 4-7).** Un agent qui propose l'idée (Gemini-3.1-Pro avec OpenCode) et un agent qui l'exécute sur un A100 réel. Un correcteur extérieur à l'environnement isolé extrait la métrique. Un auditeur (Claude Sonnet 4.6) cherche les fraudes. Trois tâches :
  - préentraînement nanoGPT, mesuré en val_bpb ;
  - apprentissage par renforcement sur MinAtar Breakout ;
  - désapprentissage WMDP-cyber, mesuré avec MMLU-STEM pour la capacité conservée.
- **Procédés et budget (p. 7).** Six procédés : glouton, MAP-Elites, Go-Explore, îles, curiosité, Omni. 300 courses exécutées par case, 5 400 au total, dont 3 222 notées. Le budget est égal en **courses exécutées**. Il n'est égal ni en jetons, ni en dollars, ni en courses valides : Omni ne compte pas les idées rejetées par sa porte, qui en laisse passer 10 % sur nanoGPT (417/4158, p. 10).
- **Graines.** Une seule par case. Les auteurs l'écrivent : « we run a single seed per (strategy, task) cell » (p. 76). Aucune barre d'erreur : réponse « [No] » à la question de signification statistique (p. 79).
- **Référence simple.** Aucun tirage indépendant. Le glouton (« Top-K parents by score », p. 4) sert de référence.

**Qualité (p. 8), vérifiée par programme.**
- « no single strategy performs well on all three » (p. 8).
- nanoGPT : le glouton gagne (best 0.9567, moyenne des dix meilleurs 0.9579). Omni atteint 0.9584.
- Renforcement (score normalisé, la référence vaut 1.0) :

| Procédé | Meilleur score |
|---|---|
| MAP-Elites | 1.582 |
| Îles | 1.563 |
| Go-Explore | 1.561 |
| Glouton | 1.368 |
| Curiosité | 1.298 |
| Omni | 1.196 |

- Désapprentissage : le glouton gagne (1.0309), la curiosité suit (1.0012), « No other strategy crosses the baseline » (p. 9).
- La pente du meilleur score courant s'aplatit après 50 à 100 solutions valides (p. 9).

**Diversité (p. 9-10).** Elle est mesurée par la distance cosinus entre plongements gemini-embedding-001 des plans d'idées, donc par un modèle.
- MAP-Elites et Go-Explore sont en tête sur les trois tâches.
- Omni a la plus forte médiane sur nanoGPT (0.208) mais la plus faible sur le renforcement (0.124) et le désapprentissage (0.094).
- Le glouton est le plus bas sur nanoGPT (0.088).
- Les îles sont en bas partout : « Migration accelerates this convergence » (p. 10).

**Nouveauté (p. 10-11).** Elle est jugée par un classeur agentique Claude-Code Sonnet 4.6 qui cherche sur la toile, avec la grille en 5 points de Gupta et Pruthi. Les notes ≤ 2 passent une seconde vérification. **Aucun humain n'intervient.**
- « 0 ideas reach the most novel rating NS = 1 across 3,222 scored and rated runs » (p. 11).
- Le meilleur côté nouveau varie selon la tâche :

| Tâche | Procédé en tête | Part d'idées notées ≤ 2 |
|---|---|---|
| nanoGPT | curiosité | 20/200, les autres procédés 0 |
| Renforcement | MAP-Elites | 5 % |
| Désapprentissage | Omni | 14.1 % |

**Phrases demandées.**
- Résumé (p. 1) : « completely novel ideas are rare. No idea across our scored runs is rated as “Original” […] novel ideas never approach the highest-performing known-recipe scores. Across all six strategies and three domains, only one such idea lands in the top-10 by quality ».
- Écart au sommet (p. 12) : 3.2 % sur nanoGPT (0.9873 contre 0.9567), 6.0 % sur le désapprentissage, 1.2 % sur le renforcement. Les médianes sont égales à 2.4 % près.

**Généralisation (p. 13).** Sur une tâche tenue à l'écart (Asterix), le classement s'inverse :
- îles 3.991, MAP-Elites 2.755 ;
- glouton et Omni : aucun score valide.

**Fraudes (p. 12).** 40 fabrications sur 1 628 courses notées.

**Limites dites.** 300 itérations par case ; procédés et invites non réglés (p. 14). La liste de contrôle contredit le texte : elle annonce deux domaines et 20 minutes par course sur nanoGPT (p. 76, 79), le texte 35 minutes (p. 7).

**Ce que l'article ne montre pas.** Aucune comparaison au tirage indépendant. Aucune répétition. La nouveauté n'est validée par aucun humain. Le budget n'est pas égal en calcul.

---

## 2. Automated Discovery Has No Universally Superior Harness — Gupta, Lei, Lu, Anumanchipalli (UC Berkeley), Choshen (MIT, MIT-IBM), arXiv 2607.18235

**Dispositif (p. 3-4).**
- Le point de départ est le « Sequential Best-of-N » : « repeatedly mutates only the best program discovered so far » (p. 3). C'est une **montée gloutonne**, pas un tirage indépendant.
- Composants ajoutés un à un sur deux branches :
  - branche OpenEvolve : archive des K meilleurs, exploration ε-glouton sur l'historique, budget déplacé de la largeur vers la profondeur, inspirations, MAP-Elites, îles ;
  - branche TTT-Discover : valeur du sous-arbre, puis UCT, puis PUCT, puis plusieurs parents.
- 30 montages, 4 modèles (Qwen2.5-3B, Qwen3-4B, GPT-OSS-20B et 120B), 3 problèmes (circle packing, triangle de Heilbronn, seconde inégalité d'autocorrélation). Plus de 3,1 millions de tirages (p. 1).
- La grandeur est vérifiée par programme (évaluateur).

**Budget et répétitions (p. 4).** Le budget est égal en **nombre de tirages** au sein d'un couple : 1 600 pour Qwen, 320 pour GPT-OSS-20B, 160 pour GPT-OSS-120B. Cinq courses par montage. Le réservoir de référence compte 100 courses pour Qwen et 30 pour GPT-OSS.

**Statistique (p. 5-6).**
- Le maximum sur cinq courses est comparé par rééchantillonnage (100 000 tirages) au maximum de cinq courses de référence.
- Un score « majorité » mesure la victoire sur au moins 7 couples sur 12. Le test se fait par permutation, avec correction de Holm.
- Il n'y a pas de calcul formel du nombre d'essais nécessaires. Les auteurs justifient seulement le choix de cinq courses : « larger than the common three-run protocol » (note p. 5).

**Résultats.**
- Les archives K plus grandes ne donnent aucun gain significatif sur aucun couple (p. 7).
- Le montage le meilleur est l'ε-glouton (K = 1, ε = 20 %) : score majorité 0.914, p = 0.023, **p = 0.678 après Holm** (p. 8-9).
- OpenEvolve complet : score majorité 0.033, p = 0.978, « the lowest observed majority-win score » (p. 8).
- « Finding 1. No tested fixed harness is significantly better than a simple baseline » (p. 8).
- « the complete recipe underperforms the baselines that strip its components away » (p. 8). Les alternatives simples sont l'ε-glouton, UCT et PUCT avec un seul parent.
- Corrélation de Spearman entre le meilleur score partiel et le score final : 0.000 à 0.474 à 10 % du budget ; au-dessus de 0.70 pour 11 couples sur 12 à 50 % (p. 9).

**Allocation adaptative à cinq courses complètes (Table 1, p. 11).**

| Politique | Moyenne |
|---|---|
| Montée gloutonne, 5 courses | 84.35 % |
| Un montage tiré au hasard | 82.49 % |
| Portefeuille de montages sans élagage | 84.54 % |
| Élagage 12→5→2→1 | 85.75 % |

Erreur type Monte-Carlo : 0.02.

**Ce que l'article ne montre pas.** Aucun tirage indépendant depuis le programme initial. Aucune vérification de nouveauté. Le gain adaptatif (environ 1,4 point) repose sur le rééchantillonnage de réservoirs déjà collectés, non sur des courses nouvelles (p. 10). Aucune section de limites trouvée.

---

## 3. Initialization Improves LLM-Driven Discovery — Sakarvadia (Chicago), Ciccone (Vector), Raffel (Vector, Toronto), arXiv 2610.00707

**Dispositif (p. 3, 17).**
- 12 montages « Modular » : 4 façons de muter × 3 façons de choisir le parent, dérivés d'OPRO.
- 3 montages de l'état de l'art : ShinkaEvolve, OpenEvolve, optimize anything.
- 5 tâches, toutes vérifiées par programme : CloudCast, Can't Be Late, TSP à 100 villes, circle packing à 26 cercles, invite GSM8K.
- **Budget égal en jetons** : de 150 000 à 2 millions selon la tâche (Table 6, p. 17). Les auteurs écartent le comptage par évaluations comme « not an exact comparison » (p. 3).
- **Référence de tirage parallèle** : « directly querying the LLM independently in parallel » à partir de la même graine, avec un contexte qui ne change jamais (p. 4).
- Les intervalles de confiance à 95 % sont pris **entre montages** (n = 12, n = 3). Le nombre de graines par montage n'est pas trouvé.

**Résultats.**
- Le tirage parallèle bat certains montages séquentiels, pas tous. Le séquentiel gagne sur TSP, le parallèle sur circle packing. Les meilleurs montages changent selon le couple tâche-modèle (p. 4).
- **Effondrement de diversité** (Fig. 3, Table 2, p. 5) : la diversité de fenêtre glissante baisse au fil de la trajectoire. Les ensembles parallèles sont plus divers que les ensembles séquentiels.
- Diversité moyenne des montages Modular : de 0.02 ± 0.01 (Can't Be Late) à 0.40 ± 0.04 (invite).
- **Interventions de diversité** (seuil cosinus 0.95 ou 0.8, juge modèle, déduplication ; Table 3, p. 6) : elles augmentent la diversité, mais pas le score. Sur circle packing, la base fait 2.44 ± 0.08 et la déduplication 2.04 ± 0.44. Les auteurs parlent de « variable effects […] in some cases, harm performance » (p. 6).
- Montages de l'état de l'art contre Modular (Table 4) : 2.51 contre 2.44 sur circle packing, mais -1772 ± 250 contre -1719 sur TSP.
- **Prédiction par les premières découvertes** (Fig. 4, p. 6) : régression de la médiane des 15 premières découvertes sur le maximum final. R² de 0.050 et 0.063 sur deux tâches, de 0.714 et 0.628 sur deux autres, de 0.134 sur la cinquième. La prédiction est donc forte sur deux tâches seulement.

**Intervention (p. 7-9).** Une part r du budget part en tirages parallèles. On garde ensuite les m = 15 meilleurs, filtrés au seuil s = 0.98, puis on lance le séquentiel.
- Elle « uniformly outperforms both fully serial and parallel » (p. 8), sur les figures, pour la moyenne des 12 montages.
- Appliquée aux montages de l'état de l'art : « Post-initialization discovery scores increase by 2%-21% » (p. 9).

**Ce que l'article ne montre pas.**
- Le budget r est choisi a posteriori : il est annoncé « coincides » avec le meilleur (p. 8).
- La phase parallèle est elle-même un tirage indépendant, ce qui donne raison au tirage comme initialisation, non comme procédé complet.
- Pas de répétitions déclarées. Pas de test statistique.

---

## 4. Hill Sampling — Beck, Ogren, Kobren (Oracle), arXiv 2609.25510

**Définition (p. 4).** « Each round, Hill Sampling draws N edits independently from the current incumbent ». Le meilleur candidat de la manche devient l'incumbent s'il est ≥ (égalités acceptées). Le procédé n'a ni archive, ni croisement, ni mise à jour de poids. N vaut 64 ou 512.

**Références (p. 5).**
- Tirage répété (« Repeated Sampling ») : éditions du code **initial**, sans reporter le meilleur. C'est un vrai tirage indépendant.
- Bruit de modèle, stratégies d'évolution (« evolution strategies », ES) sur les poids de 20 à 30 milliards de paramètres, ES max@8, ES softmax, et hill sampling combiné à ES.

**Protocole.**
- Budget : « All compute is matched by the number of LLM completions » (p. 5).
- Trois graines par méthode (p. 4). La température est réglée par méthode (p. 14).
- Tâches vérifiées par programme, avec des vérificateurs durcis contre la fraude : circle packing (gpt-oss-20b), sommes et différences d'ensembles (OLMo-3.1-32B), recouvrement minimal d'Erdős (Mistral-24B). Un seul modèle par tâche.

**Chiffres.**
- Fig. 1 (p. 6), lecture approximative sur la figure, scores normalisés à AlphaEvolve :

| Tâche | Hill sampling, 512 | Tirage répété |
|---|---|---|
| Circle packing | ≈ 1.000 | ≈ 0.995 |
| Ensembles | ≈ 0.9575 | ≈ 0.9573 |
| Erdős | ≈ 0.9993 | ≈ 0.9991 |

- Sur les ensembles : « there is no significant difference between the methods ». Sur Erdős : « RS achieves a high average max return ».
- Meilleurs résultats (Table 1, p. 6) : circle packing 2.635983084917604 contre 2.6359830774 pour ThetaEvolve. Erdős 0.38089767, mieux qu'AlphaEvolve mais moins bien que TTT-Discover.
- Sur Erdős, le tirage répété à température 1 a « the best maximum score » face au bruit de modèle (p. 7).
- Dix variantes (archives des K meilleurs, diversité, îles, retour d'exécution, renforcement en contexte, etc.) n'apportent « No significant advantage » (p. 9).

**Ce que l'article ne montre pas.** Les écarts au tirage répété sont minimes. Le titre « Better » repose surtout sur circle packing. Trois graines seulement, et un seul modèle par tâche. Le record de circle packing dépend de la tolérance numérique : les auteurs le disent (note, p. 7).

---

## 5. Mutation Without Variation — Gurkan (Northwestern), Stonedahl (Augustana), Wilensky (Northwestern), arXiv 2606.05408 (atelier GECCO 2026)

**Dispositif (p. 4).**
- Chaînes de 300 mutations acceptées sans sélection, dans un petit langage typé de contrôle d'agent. On ne mesure aucun comportement : l'étude est « purely genotypic » (p. 2).
- Comparaison à la mutation de sous-arbre classique, avec une profondeur maximale de 4.
- Expérience 1 : 50 invites × 3 programmes initiaux, soit 150 chaînes, avec Gemini 3.1 Flash Lite.
- Expérience 2 : 4 invites × 30 répétitions.
- Expérience 3 : 7 modèles × 4 invites, sans répétition.

**Chiffres (p. 5-6).**
- « 71% visit fewer than 100 unique programs and 87% visit fewer than 20 unique skeletons over 300 steps. Put differently, in 87% of chains, over 93% of individual mutations revisit a previously seen structural form » (p. 6).
- La mutation classique visite environ 270 programmes uniques et 143 squelettes par chaîne (p. 5).
- La médiane des chaînes du modèle visite environ 10 squelettes.

**Ce qui module la convergence.**
- La formulation de l'invite. Avec 30 répétitions : 269 programmes pour l'invite la plus ouverte, 52 pour l'invite médiane, 1.7 squelette pour la plus fermée (p. 6).
- Le modèle : Claude Sonnet 4 descend à 6 programmes et 1 squelette ; GPT-5 Mini avec raisonnement monte à 301 programmes et 225 squelettes. Le raisonnement augmente la diversité.
- La taille du programme initial n'a qu'un effet « modest ».
- Les cycles courts dominent : cycles de 2 au niveau programme, boucles sur soi au niveau squelette (p. 7).

**Limites dites (p. 8).** Un seul petit langage. Analyse génotypique seulement. Pas de répétition entre modèles.

**Ce que l'article ne montre pas.** Rien sur la qualité. Rien avec sélection. Rien sur les langages courants.

---

## 6. The Greatness of Science Cannot Be Planned — He, Wang, Zhao, Shi, Liu, Chen (UC Davis, ARA Lab, Zhejiang, Michigan, HKU), arXiv 2608.09855

**Nature.** Article de **position**.

**L'analogie (p. 1-3, Table 1).**
- Le test logiciel à couverture guidée (fuzzing greybox, AFL, Angora) sépare deux rôles. La couverture, signal dense et bon marché, guide la mutation. Un oracle séparé (plantage, sanitizer) certifie.
- L'auto-recherche doit faire de même : un signal dense de « progrès épistémique » guide la recherche, une validation protégée certifie.

**Le signal proposé (p. 4).**
- Il doit être bon marché (C1), corrélé au progrès réel (C2) et robuste à l'optimisation (C3).
- Exemples : écarter une explication, situer une frontière, surprise contre un modèle, désaccord entre répliques.
- Dans l'exemple travaillé (p. 6) : la « surprise » (résidu normalisé par σ) et l'« enveloppe » des régimes explorés.

**Validation protégée (p. 5-6).** Les preuves doivent être « protected from adaptive reuse » : test caché, réplication, revue. Le texte cite Dwork et al. 2015.

**Trois prédictions réfutables (p. 2, 9).** Aucune n'est testée. L'une dit : « feedback-directed search must beat repeated sampling per validated discovery ».

**Résultats.**
- Un exemple sur DiscoverPhysics, présenté comme « an existence proof, not an evaluation » (p. 6).
- 31 courses archivées ont été rejouées (p. 6). Sur un monde, deux courses sont comparées :
  - sans le panneau de lectures, l'explication est notée 0.4 pour un seuil de 0.75 ;
  - avec le panneau, elle est notée 1.0 et la perte passe de 19.6 à environ deux fois le plancher de bruit (p. 7).
- La Figure 5 est « Schematic, not run data » (p. 6).
- L'explication est « judged » ; le juge n'est pas précisé.

**Ce que l'article ne montre pas.** Aucune comparaison chiffrée au tirage répété. Aucune répétition. L'affirmation du résumé sur l'échec des références (« Optimization-driven baselines fail ») repose sur des exemples choisis.

---

## 7. Towards Diverse Scientific Hypothesis Search (EvoDiverse) — Wang, Shojaee, Meidani, Sun, Hernández-Lobato, Head-Gordon, He, Reddy, Zhang, Du (Georgia Tech, Virginia Tech, CMU, Berkeley, Cambridge, Microsoft Research), ICML 2026, arXiv 2606.10587

**Procédé (p. 3-4, 33).**
- Deux réservoirs : un froid (β = 1, T = 1) et un chaud (β = 0.25, T = 4), avec sélection stochastique de Boltzmann.
- Échanges acceptés par Metropolis-Hastings. Un facteur ξ s'ajuste pour viser 30 à 50 % d'échanges acceptés.
- Les invites peuvent différer selon la température.

**Budget.** Égal en **appels à l'oracle** :
- molécules : 10 000 appels, oracle substitut de JNK3 et GSK3β ;
- équations : 1 000 évaluations, LLM-SRBench ;
- circle packing : 1 000 évaluations.

**Références.** MOLLEO ou un algorithme génétique à population unique, un ensemble de populations isolées, une population unique à haute température, des îles. **Pas de tirage indépendant.** PySR est en annexe.

**Effondrement (p. 5).** Les auteurs ne donnent pas de chiffre direct de perte de diversité au fil de l'eau. Ils donnent ceci : à convergence, EvoDiverse « proposes approximately 90 diverse candidates, nearly doubling the ∼50 samples produced by MOLLEO ». Sur circle packing, les îles ont la plus faible diversité (0.48, Table 3, p. 8).

**Gains.**
- Molécules, AUC des dix meilleurs (Table 1, p. 6) : sur JNK3, 0.63 ± 0.05 contre 0.58 pour MOLLEO et 0.54 pour l'ensemble. Sur GSK3β, 0.76 contre 0.70 et 0.73. Tests appariés sur trois graines (p. 24) : p = 0.011 contre MOLLEO sur JNK3, mais 0.111 contre l'ensemble et 0.086 contre MOLLEO sur GSK3β.
- Équations (Table 2) : meilleure exactitude à 0.1 de 0.408 contre 0.301 en physique, 0.212 contre 0.104 en biologie.
- Circle packing (Table 3) : meilleure somme 2.5461 contre 2.4986 pour l'algorithme génétique simple, avec diversité TF-IDF 0.78 contre 0.61.

**Limites dites (p. 9).** Plusieurs réservoirs réduisent les évaluations par réservoir. Les hyperparamètres sont à régler par tâche.

**Ce que l'article ne montre pas.** Aucune référence de tirage indépendant. Trois graines. Nombre de graines du circle packing non trouvé. L'activité moléculaire vient d'un oracle substitut ; l'arrimage moléculaire est en annexe.

---

## 8. SwarmWorld — Pal, Wang, Buehler (MIT), arXiv 2608.26081

**Dispositif (p. 4, 39, 43).**
- Agents gpt-5 homogènes dans un monde simulé déterministe. Ils construisent des artefacts et écrivent des contrôleurs.
- La fonction est évaluée sans les agents, sous 8 perturbations inédites.
- Quatre conditions : culture complète, sans communication, sans culture explicite (stigmergie seule), recherche isolée.
- La recherche isolée consiste en N mondes à un agent, résumée par une « enveloppe meilleur-de-N » point par point, avec « the same scheduled decision opportunities ». Le budget est **égal en occasions de décision, pas en jetons** : « Equal decision opportunity does not imply equal token use » (p. 43).
- Quatre graines de monde par case (p. 4).

**Résultats à 3 200 pas, N = 100 (p. 12, 15).**

| Mesure | Culture complète | Sans culture explicite | Recherche isolée |
|---|---|---|---|
| Résilience du portefeuille | 0.2474 | 0.2365 | 0.1794 |
| Inventions validées | 5.75 | 7.00 | 2.75 |
| Résilience hors échantillon | ≈ égale à la suivante | 0.0446 | 0.0356 |
| **Meilleur artefact final** | 0.2380 | — | **0.3488** |

Les sociétés gagnent sur l'ampleur et la robustesse, l'isolée sur le meilleur artefact : « isolated agents can still win a contest defined only by the strongest single artifact » (p. 15).

**Échelle de population (p. 4).** Le résultat n'est pas monotone. À N = 50, deux conditions partagées restent sous l'isolée en AUC de découverte.

**Ce que l'article ne montre pas.** Quatre graines seulement. Monde simulé. Le budget en jetons n'est pas égalisé. « Invention » est un critère interne du simulateur.

---

## Synthèse

| Article | Tirage indépendant comparé ? | Unité de budget | Vérification | Graines | Verdict sur la question |
|---|---|---|---|---|---|
| Heuresis | non (glouton seulement) | courses exécutées | programme ; nouveauté jugée par un modèle | 1 | aucun procédé ne domine ; nouveauté jamais au sommet |
| Pas de montage supérieur | non (montée gloutonne) | tirages | programme | 5, référence 30 à 100 | rien de significatif contre la montée gloutonne après Holm ; OpenEvolve dernier |
| Initialisation | **oui** (parallèle) | jetons | programme | non dit (intervalles entre montages) | parallèle puis séquentiel > chacun seul ; parallèle seul bat certains montages |
| Hill sampling | **oui** | complétions | programme | 3 | léger avantage du hill sampling ; égalité sur une tâche sur trois |
| Mutation sans variation | sans objet | 300 pas | génotype | 30 (exp. 2) | mutation répétée converge, plus que le hasard classique |
| Fuzzing | non testé | — | exemple | 1 à 2 | position seulement |
| EvoDiverse | non | évaluations | programme ou oracle substitut | 3 | mieux que les algorithmes génétiques à population unique ou isolées, gains modestes |
| SwarmWorld | **oui** (meilleur-de-N isolé) | occasions de décision | simulateur | 4 | sociétés devant sur l'ampleur ; isolé devant sur le meilleur artefact |

**Lecture d'ensemble.**
- Trois articles seulement comparent au tirage indépendant. Aucun ne montre qu'un procédé d'exploration complexe le bat nettement :
  - le hill sampling, simple, l'emporte de peu ;
  - l'initialisation parallèle puis séquentielle bat chacun des deux ;
  - SwarmWorld laisse à l'isolé le meilleur artefact.
- Contre une montée gloutonne, les procédés élaborés (OpenEvolve, îles, interventions de diversité) ne sont pas supérieurs de façon significative. Ils sont parfois inférieurs (articles 2, 3 et 4).
- La diversité mesurée monte avec ces procédés sans que le score suive (articles 1 et 3). La convergence de l'opérateur de mutation est forte sans sélection (article 5).
- Les gains rapportés en faveur de l'exploration portent sur l'ampleur d'un portefeuille (articles 7 et 8) ou sur une tâche tenue à l'écart (article 1), avec une à quatre graines.
- Le classement dépend de la tâche et du modèle dans tous les articles qui comparent.

## Non vérifié
- Gideoni, Risi, Gal 2026, « Simple baselines are competitive with code evolution » (arXiv 2602.16805) : seulement cité dans les articles 2 et 4, non lu.
- Nombre de graines de l'article 3 et du circle packing de l'article 7 : non trouvé.
- Valeurs de la Figure 1 de l'article 4 : lues sur l'image, approximatives.
- Nature du juge de l'explication dans l'article 6 : non précisée.
- Pages d'annexes non lues en entier : article 1 p. 15-75, article 2 tableaux p. 38-50, article 7 annexes, article 8 p. 16-57 (lues seulement par recherche ciblée).
