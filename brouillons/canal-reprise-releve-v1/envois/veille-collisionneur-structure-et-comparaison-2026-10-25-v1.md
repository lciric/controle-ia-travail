# Veille — tours « structure » et « comparaison » du collisionneur, 25 octobre 2026 (v1)

Pièce pour `registres/veille.md` (semaine 2026-W43), à inscrire par « session-depot ». Rédigée par « conv-audit » le
25 octobre 2026 (09:05 UTC). Tout est au **niveau transcription** (R7) : titres, auteurs et années tels que les trois
cellules les rapportent, dédoublonnés et marqués « à vérifier » ; aucun chiffre repris ; aucun identifiant arXiv n'a été
inventé. Six titres ont en plus leur **résumé lu aujourd'hui** sur la page arXiv ou une page relais (jamais le PDF) :
notés « (résumé lu) ». Rien de ceci n'est servi aux organismes.

## Ligne de veille proposée

| semaine | sources balayées | parutions retenues | revendication touchée | action |
|---|---|---|---|---|
| 2026-W43 (collisionneur, 25 oct.) | deux tours III.1 à trois cellules (Fable, Opus, Argon) : « structure » (`donnees/collisionneur-structure-v1`, `6f485f3` ; pièce `6906a1d1…`) et « comparaison » (`donnees/collisionneur-comparaison-v1`, `9e61306` ; pièce `3f150ea8…`) ; 2,04 + 1,93 USD ; recherche web de « conv-audit » sur six résumés | voir la liste ci-dessous ; convergences méthodologiques : plancher de bruit test–retest ; témoin « un modèle, vote à k, coût apparié » ; contrôles « meilleur de N » et « score permuté » ; holdout réutilisable ; conflit d'intérêts récompense/juge ; Goodhart ; canaris de signalement ; myopie « épisode = génération » ; « poids contre archive » | H-E1, H-G1 (lectures : plancher de bruit, témoins), H-G2 (témoins SFT et récompense aléatoire), étape 2 (score net, concepteur), objectif ultime (N-044) ; aucune revendication scellée changée | note de décision proposée (`decision-N-composition-apprise-cout-dans-le-signal-v1.md`, `6577feee…`) ; cinq propositions à Lazar en cours ; recherche bibliographique 2025–2026 obligatoire avant toute revendication sur le concepteur entraîné |

## Références rapportées par les cellules (toutes « à vérifier »)

**Recherche automatique de structures d'agents, auto-amélioration (famille du système dessiné)**
- Hu, Lu, Clune (2024), « Automated Design of Agentic Systems » (résumé lu, page relais).
- Zhang, Hu, Lu, Lange, Clune (2025), « Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents » (résumé lu, arXiv 2505.22954).
- Zelikman, Lorch, Mackey, Kalai (2023/2024), « Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation ».
- Yin et al. (2024), « Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement ».
- Zhang et al. (2024), « AFlow: Automating Agentic Workflow Generation ».
- Zhuge et al. (2024), « GPTSwarm: Language Agents as Optimizable Graphs ».
- Khattab et al. (2023), « DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines ».
- Yuksekgonul et al. (2024), « TextGrad: Automatic “Differentiation” via Text ».
- Fernando et al. (2023), « Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution ».
- Yang et al. (2023), « Large Language Models as Optimizers ».
- Novikov et al. (2025), « AlphaEvolve: A coding agent for scientific and algorithmic discovery ».
- Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models ».
- Schmidhuber, « Gödel Machines » (année et intitulé exacts à vérifier).

**Concepteurs entraînés pour des exécutants (famille la plus proche de la conception évaluée)**
- Nie, Feng, Ye, Liang, Lu, Yao, Alahi, Zou (2025), « Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors » (résumé lu, arXiv 2504.04785 ; non citée par les cellules, trouvée par « conv-audit »).
- Gao et al. (2025), « FlowReasoner: Reinforcing Query-Level Meta-Agents » (résumé lu, arXiv 2504.15257 ; idem).
- Ye et al. (2025), « MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems » (résumé lu, arXiv 2503.03686).

**Recherche d'architecture, méta-apprentissage**
- Zoph, Le (2016/2017), « Neural Architecture Search with Reinforcement Learning ».
- Real, Aggarwal, Huang, Le (2019), « Regularized Evolution for Image Classifier Architecture Search ».
- Li, Talwalkar (2019), « Random Search and Reproducibility for Neural Architecture Search ».
- Liu, Simonyan, Yang (2019), « DARTS: Differentiable Architecture Search ».
- Li, Jamieson, DeSalvo, Rostamizadeh, Talwalkar (2018), « Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization ».
- Snoek, Larochelle, Adams (2012), « Practical Bayesian Optimization of Machine Learning Algorithms ».
- Finn, Abbeel, Levine (2017), « Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks ».
- Duan et al. (2016), « RL²: Fast Reinforcement Learning via Slow Reinforcement Learning » ; Wang et al. (2016), « Learning to reinforcement learn » ; Oh et al. (2020), « Discovering Reinforcement Learning Algorithms ».
- Dennis et al. (2020), « Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design » ; Lehman, Stanley (2011), « Abandoning Objectives » ; Mouret, Clune (2015), « Illuminating search spaces by mapping elites ».

**Renforcement, récompenses, Goodhart**
- Schulman et al. (2017), « Proximal Policy Optimization Algorithms » ; Shao et al. (2024), « DeepSeekMath » (GRPO) ; DeepSeek-AI (2025), « DeepSeek-R1 » ; Rafailov et al. (2023), « Direct Preference Optimization ».
- Hu et al. (2021/2022), « LoRA: Low-Rank Adaptation of Large Language Models ».
- Ma et al. (2023), « Eureka: Human-Level Reward Design via Coding Large Language Models » (résumé lu, arXiv 2310.12931) ; Kwon, Xie, Bullard, Sadigh (2023), « Reward Design with Language Models » ; Yu et al. (2023), « Language to Rewards for Robotic Skill Synthesis » ; Yuan et al. (2024), « Self-Rewarding Language Models ».
- Gao, Schulman, Hilton (2022/2023), « Scaling Laws for Reward Model Overoptimization » ; Skalse, Howe, Krasheninnikov, Krueger (2022), « Defining and Characterizing Reward Hacking » ; Manheim, Garrabrant (2018), « Categorizing Variants of Goodhart's Law » ; Amodei et al. (2016), « Concrete Problems in AI Safety ».
- « Gains sous récompenses fallacieuses en renforcement à récompense vérifiable » (2025) : signalé sans attribution par une cellule ; à identifier.
- Foerster et al. (2018), « Counterfactual Multi-Agent Policy Gradients » ; Rashid et al. (2018), « QMIX » ; Shapley (1953), « A Value for n-Person Games ».
- Gneiting, Raftery (2007), « Strictly Proper Scoring Rules, Prediction, and Estimation ».

**Sondes, états internes**
- Alain, Bengio (2016), « Understanding intermediate layers using linear classifier probes » ; Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks » ; Belinkov (2022), « Probing Classifiers: Promises, Shortcomings, and Advances ».
- Burns, Ye, Klein, Steinhardt (2022/2023), « Discovering Latent Knowledge in Language Models Without Supervision » ; Kadavath et al. (2022), « Language Models (Mostly) Know What They Know » ; Li, Patel, Viégas, Pfister, Wattenberg (2023), « Inference-Time Intervention » ; Azaria, Mitchell (2023), « The Internal State of an LLM Knows When It's Lying ».

**Validité statistique, agrégation**
- Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The reusable holdout » ; Blum, Hardt (2015), « The Ladder » ; Recht, Roelofs, Schmidt, Shankar (2019), « Do ImageNet Classifiers Generalize to ImageNet? ».
- Agarwal et al. (2021), « Deep Reinforcement Learning at the Edge of the Statistical Precipice » ; Friedman, Dieng (2023), « The Vendi Score ».
- Wang et al. (2022/2023), « Self-Consistency Improves Chain of Thought Reasoning in Language Models » ; Du et al. (2023), « Improving Factuality and Reasoning in Language Models through Multiagent Debate » ; Wolpert (1992), « Stacked Generalization ».

## Ce que la veille ne fait pas

Aucune de ces références n'entre dans un préenregistrement ni dans un papier avant lecture sur PDF empreinté, page citée
(R7). Une zone qui paraît vierge (concepteur entraîné sur une génération entière, état de lignée en entrée, familles tenues
à l'écart, dérives mesurées) est une question, pas un trou (R8) : recherche ciblée 2025–2026 à faire avant toute
revendication.
