# Matière première de l'auto-conception de l'organisme d'idéation — mécanismes publiés d'exploration, d'originalité, d'épreuve, de jugement, de mémoire, de sélection, de coût et d'auto-conception — v1

Pièce servie telle quelle à des proposeurs. Elle décrit ce que dit un moissonnage de 630 travaux ; elle ne juge aucun mécanisme et ne dit pas lequel est bon. Écrite le 18 novembre 2026 à partir de `docs/notes/matiere-premiere-auto-conception-v1/releve-mecanismes-v1.json` (relevé par mécanisme, vingt et un lots corrigés selon `contre-lecture-matiere-premiere-v1.md`).

## 0. Comment lire cette pièce

- **Qui affirme quoi.** Chaque mécanisme est ce qu'*affirment les auteurs* de chaque travail, d'après la notice, le résumé, la page ou la lecture approfondie du dépôt selon la « lecture » indiquée. Rien n'est vérifié par nous : aucun chiffre n'est opposable avant lecture sur PDF empreinté, page citée (R7).
- **Éprouvé contre le réel : « oui, mesuré »** — les auteurs disent avoir mesuré ; mesure non vérifiée par le programme ni par nous (R7) : jamais un fait établi.
- **Éprouvé contre le réel : « oui, affirmé »** — les auteurs affirment un effet sans mesure propre à ce mécanisme, ou le résultat est lu sur une notice ; non opposable.
- **Éprouvé contre le réel : « non »** — aucune épreuve contre le réel : proposition, argument de position ou simulation seule.
- **Éprouvé contre le réel : « inconnu »** — la notice ne dit pas si le mécanisme a été éprouvé contre le réel.
- **Lecture** — « lecture approfondie sur PDF » : une fiche de lecture du dépôt a été relue ; « page ou résumé » : résumé, page ou fiche d'OpenReview lus par la veille ; « notice seule » : titre et courte description de la table seuls ; toute entrée sur page, résumé ou notice est non opposable (R7).
- **Suggéré par le titre** — mécanisme inféré du seul titre ou d'après le titre : compté à part, jamais additionné aux mécanismes décrits. Ils sont en section 6.
- **Absence** — toute absence dans ce moissonnage est une question, pas un trou du champ (R8). Une absence dans cette pièce veut seulement dire : non trouvé dans ce moissonnage, à la profondeur de lecture indiquée.
- **Identifiants.** « 593.3 » veut dire : quatrième mécanisme (position 3) du travail d'indice 593 de la table fusionnée. Le relevé donne, pour chaque identifiant, la phrase complète du mécanisme et sa source (chemin et empreinte sha256) : `releve-mecanismes-v1.json`. Les regroupements de cette pièce sont des rapprochements de lecture du relevé ; un travail peut y figurer sous plusieurs regroupements.
- **Regroupement.** Les mécanismes décrits sont regroupés par ressemblance de ce qu'ils font. Le regroupement est un choix de lecture, rejouable par `programmes/ecrire_matiere_v1.py` ; il n'est pas une classification des auteurs.

### Comptes

- 630 travaux ; 592 portent au moins un mécanisme ; 38 n'en portent aucun : 20 « exclue », 12 « hors sujet », 3 « liste sans mécanisme », 3 « notice muette » (section 8).
- 1106 mécanismes au total, dont **899 décrits** et **207 suggérés par le titre** (comptés à part, jamais additionnés).
- Mécanismes décrits par famille : exploration 188 ; originalité 84 ; épreuve 190 ; jugement 141 ; mémoire 93 ; sélection 80 ; coût 69 ; auto-conception 35 ; autre 19.
- Mécanismes décrits par éprouvé contre le réel (selon les auteurs) : oui, mesuré 476 ; oui, affirmé 124 ; non 70 ; inconnu 229.
- Travaux par lecture : lecture approfondie sur PDF 8 ; page ou résumé 459 ; notice seule 163.
- Trois travaux de la dernière tranche (indices 605, 612, 625) ont une lecture approfondie au dépôt qui n'a pas été ouverte pour cette pièce : ils sont relevés d'après l'entrée de la table seulement.

## 1. Mécanismes distincts, par famille

Format d'une ligne : *titre (date) — adresse · identifiant(s) du mécanisme · éprouvé contre le réel selon les auteurs · lecture · « machine » si le travail est l'un des systèmes de la section 2.*

### Famille « exploration »

**exploration n° 1 — Idéation ancrée dans la littérature ou un graphe de connaissances : récupération, trajectoires de citations, supervision par les citations ultérieures**

13 mécanismes, 13 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 11, inconnu 2. Lecture : page ou résumé 13.

- Tracing the Influence of Retrieved Literature on Scientific Ideation in LLMs (2026-10-28) — https://arxiv.org/abs/2610.39060 · 6.0 · oui, mesuré · page ou résumé
- Read, Grep, and Synthesize: Diagnosing Cross-Domain Seed Exposure for LLM Research Ideation (2026-05-12) — https://arxiv.org/abs/2605.11532 · 44.0 · oui, mesuré · page ou résumé
- AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era (2026-09-07) — https://arxiv.org/abs/2609.07611 · 72.0 · oui, mesuré · page ou résumé
- Tree-of-Ideas: Automated Research Ideation via Cross-Trajectory Reasoning over Scholarly Evolution (2026-08-11) — https://arxiv.org/abs/2608.10740 · 134.0 · oui, mesuré · page ou résumé · machine
- Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation (2026-10-16) — https://arxiv.org/abs/2610.23038 · 147.0 · oui, mesuré · page ou résumé
- IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas (2026-10-06) — https://arxiv.org/abs/2610.08781 · 148.0 · oui, mesuré · page ou résumé
- Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure (2026-06-17) — https://arxiv.org/abs/2608.20361 · 155.0 · inconnu · page ou résumé
- Graph2Idea:Retrieval-Augmented Scientific Idea Generation with Graph-Structured Contexts (2026-06-08) — https://arxiv.org/abs/2606.09105 · 156.0 · oui, mesuré · page ou résumé
- Graphs of Research: Citation Evolution Graphs as Supervision for Research Idea Generation (2026-05-14) — https://arxiv.org/abs/2605.14790 · 157.0 · oui, mesuré · page ou résumé
- Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another (2026-11-14) — https://arxiv.org/abs/2611.19108 · 161.0 · inconnu · page ou résumé
- REI: Learning Ideation from Repository Evolution (2026-09-14) — https://openreview.net/forum?id=f5f1OtpnyR · 524.0 · oui, mesuré · page ou résumé
- CoI‑Pro: Scientific Idea Generation via Retrieval over Research Trajectories (2026-09-17) — https://openreview.net/forum?id=MtTWQDzv0e · 529.0 · oui, mesuré · page ou résumé · machine
- From Black-Box Judgments to Auditable Graphs: Structured Idea Generation and Evaluation via Scientific Knowledge Graphs (2026-08-22) — https://openreview.net/forum?id=ZmCMvyomhA · 530.1 · oui, mesuré · page ou résumé

**exploration n° 2 — Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs**

9 mécanismes, 8 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, non 4, inconnu 2. Lecture : page ou résumé 6, notice seule 2.

- IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation (2026-09-18) — https://arxiv.org/abs/2610.04074 · 150.0 · oui, mesuré · page ou résumé · machine
- Unlocking LLM Creativity in Science through Analogical Reasoning (2026-05-11) — https://arxiv.org/abs/2605.11258 · 158.0 · oui, mesuré · page ou résumé
- LLM Daydreaming (2025-07) — https://gwern.net/ai-daydreaming · 472.0 · non · notice seule
- Idea mill (réponse critique à LLM Daydreaming) (2025) — https://seangoedecke.com/idea-mill/ · 473.0 · inconnu · notice seule
- CL-ML/open-collider (2026-05-10) — https://github.com/CL-ML/open-collider · 488.0, 488.1 · non · page ou résumé · machine
- junjiezhou1122/ideascientist-claude-code (2026-10-09) — https://github.com/junjiezhou1122/ideascientist-claude-code · 492.0 · inconnu · page ou résumé
- Forming Feasible Research Ideas by Analogical Transfer over Rationale-Bearing Graphs (2026-09-18) — https://openreview.net/forum?id=Dxbrq5y5aD · 533.0 · oui, mesuré · page ou résumé
- IdeaGraph: Evidence-Bearing Synergy Junctions for Cross-Field Scientific Ideation (2026-08-27) — https://openreview.net/forum?id=92DdZnwXPh · 550.0 · non · page ou résumé · machine

**exploration n° 3 — Information réduite, ignorance volontaire, regard neuf, point de départ inattendu, exploration libre sans objet désigné, directions que les chercheurs ne formuleraient pas**

9 mécanismes, 9 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 1, inconnu 3. Lecture : page ou résumé 9.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.0 · oui, mesuré · page ou résumé · machine
- The Value of Not Knowing: How Fresh Eyes through Naive LLMs Fuel Creativity (2026-11-09) — https://arxiv.org/abs/2611.11725 · 3.0 · inconnu · page ou résumé
- More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation (2026-05-07) — https://arxiv.org/abs/2605.06345 · 159.0 · oui, mesuré · page ou résumé
- Can LLMs Uncover Hidden Physical Laws through Free Exploration? (2026-10-27) — https://arxiv.org/abs/2610.37649 · 164.1 · oui, mesuré · page ou résumé
- Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space (2026-10-06) — https://arxiv.org/abs/2610.07627 · 177.0 · inconnu · page ou résumé
- The Alien Space of Science: Sampling Coherent but Cognitively Unavailable Research Directions (2026-03-01) — https://arxiv.org/abs/2603.01092 · 228.0 · inconnu · page ou résumé
- Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration (2026-10-13) — https://arxiv.org/abs/2610.17874 · 444.0 · oui, mesuré · page ou résumé
- Do AI Agents Have Research Taste? SENSE-Bench for Anomaly-Driven Scientific Exploration (2026-09-16) — https://openreview.net/forum?id=IvMOtnkFXk · 504.2 · oui, affirmé · page ou résumé
- Mathematica Incognita: Characterizing Open-Ended Mathematical Exploration in Language Models (2026-09-19) — https://openreview.net/forum?id=z0nQAdCOH0 · 540.0 · oui, mesuré · page ou résumé

**exploration n° 4 — Conditionnement du proposeur : personas, sujets, amorces, température, structure en étapes**

8 mécanismes, 8 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, oui, affirmé 2, inconnu 3. Lecture : page ou résumé 8.

- Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs (2026-09-24) — https://arxiv.org/abs/2609.30492 · 17.0 · inconnu · page ou résumé
- Human diversity fuels collective creativity that large language models cannot simulate or sustain (2026-07-29) — https://arxiv.org/abs/2607.26899 · 25.0 · oui, affirmé · page ou résumé
- Beyond the Hivemind: Escaping LLM Homogeneity via Meta-Persona Anchoring and Sequential Temperature Scaling (2026-05-31) — https://arxiv.org/abs/2608.02618 · 37.0 · inconnu · page ou résumé
- Anchorless Diversification for Parallel LLM Ideation (2026-05-28) — https://arxiv.org/abs/2605.30150 · 38.0 · inconnu · page ou résumé
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.2 · oui, mesuré · page ou résumé
- Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output (2026-05-01) — https://arxiv.org/abs/2605.00557 · 160.0 · oui, mesuré · page ou résumé
- Diversifying Personalized Research Ideation against AI-Induced Homogenization (2026-07-30) — https://arxiv.org/abs/2607.28087 · 323.0 · oui, affirmé · page ou résumé
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (2026-08-28) — https://arxiv.org/abs/2608.28945 · 460.0 · oui, mesuré · page ou résumé

**exploration n° 5 — Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses**

18 mécanismes, 18 travaux (7 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 12, oui, affirmé 2, inconnu 4. Lecture : page ou résumé 17, notice seule 1.

- Holistic Diversity Management in LLM-Guided Evolutionary Search (2026-10-28) — https://arxiv.org/abs/2610.38407 · 7.0 · oui, mesuré · page ou résumé
- IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation (2026-07-24) — https://arxiv.org/abs/2607.22375 · 26.0 · oui, mesuré · page ou résumé
- Towards Diverse Scientific Hypothesis Search with Large Language Models (2026-06-09) — https://arxiv.org/abs/2606.10587 · 35.0 · oui, mesuré · page ou résumé
- DEI: Diversity in Evolutionary Inference for Quality-Diversity Search (2026-05-26) — https://arxiv.org/abs/2605.27130 · 40.0 · inconnu · page ou résumé
- What Do Evolutionary Coding Agents Evolve? (2026-05-19) — https://arxiv.org/abs/2605.20086 · 41.0 · oui, mesuré · page ou résumé
- FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics (2026-05-17) — https://arxiv.org/abs/2605.17373 · 42.0 · oui, mesuré · page ou résumé
- HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses (2026-09-14) — https://arxiv.org/abs/2609.15938 · 133.0 · oui, mesuré · page ou résumé · machine
- EvoGens: A Population-Based Heuristic Search Framework for Scientific Idea Generation (2026-05-29) — https://arxiv.org/abs/2605.30961 · 139.0 · oui, mesuré · page ou résumé · machine
- EvoSci: A Bio-Inspired Multi-Agent Framework for the Evolution of Scientific Discovery (2026-05-20) — https://arxiv.org/abs/2605.24018 · 140.0 · inconnu · page ou résumé
- SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution (2026-05-14) — https://arxiv.org/abs/2605.15308 · 141.0 · oui, mesuré · page ou résumé · machine
- GEAR: Genetic AutoResearch for Agentic Code Evolution (2026-05-08) — https://arxiv.org/abs/2605.13874 · 142.0 · oui, mesuré · page ou résumé · machine
- AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench (2025-07-03) — https://arxiv.org/abs/2507.02554 · 237.0 · oui, mesuré · page ou résumé
- AlphaEvolve: A coding agent for scientific and algorithmic discovery (2025-06-16) — https://arxiv.org/abs/2506.13131 · 239.0 · oui, affirmé · page ou résumé · machine
- Organon : From Evolutionary Search to Recursive Self-Improving Agents for Scientific Discovery (2026-10-17) — https://arxiv.org/abs/2610.33046 · 384.2 · inconnu · page ou résumé · machine
- Initialization Improves LLM-Driven Discovery (2026-09-30) — https://arxiv.org/abs/2610.00707 · 406.0 · oui, mesuré · page ou résumé
- SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents (2026-10-01) — https://arxiv.org/abs/2610.02361 · 454.1 · oui, affirmé · page ou résumé
- Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing (SSRN 6569258 ; lu sur la copie de conférence) (2026-04) — https://skbi.smu.edu.sg/sites/skbi.smu.edu.sg/files/2026-06/Day1_0915_Danqing%20Mei%20(paper).pdf · 623.0 · oui, mesuré · page ou résumé
- SakanaAI/ShinkaEvolve (dépôt de code) (2025-09-17) — https://github.com/SakanaAI/ShinkaEvolve · 629.0 · inconnu · notice seule · machine

**exploration n° 6 — Recherche en arbre : plans, hypothèses, auto-modifications, bandit, Monte-Carlo**

11 mécanismes, 11 travaux (7 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 3, inconnu 3. Lecture : lecture approfondie 2, page ou résumé 9.

- PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research (2026-09-15) — https://arxiv.org/abs/2609.17846 · 70.0 · oui, mesuré · page ou résumé · machine
- Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research (2026-10-18) — https://arxiv.org/abs/2610.24944 · 102.1 · inconnu · page ou résumé · machine
- XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery (2026-07-14) — https://arxiv.org/abs/2607.12301 · 118.1 · inconnu · page ou résumé · machine
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.3 · oui, mesuré · lecture approfondie · machine
- Idea Search: Guiding Tree Search with Ideas to Explore Diverse Scientific Methods (2026-08-09) — https://arxiv.org/abs/2608.08958 · 135.0 · oui, mesuré · page ou résumé · machine
- Learning the ARTS of Search for Automated Discovery (2026-06-20) — https://arxiv.org/abs/2606.21891 · 138.0 · oui, mesuré · page ou résumé
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (2025-04-08) — https://arxiv.org/abs/2504.08066 · 241.0 · oui, affirmé · page ou résumé · machine
- Autoresearch in Mixed-Integer Linear and Nonlinear Programming (2026-09-18) — https://arxiv.org/abs/2609.39360 · 365.0 · oui, affirmé · page ou résumé
- Toward Generalist Autonomous Research via Hypothesis-Tree Refinement (2026-06-10) — https://arxiv.org/abs/2606.11926 · 453.0 · oui, affirmé · page ou résumé
- Compute Allocation for Self-Evolving LLMs: From Depth-Breadth to Multi-Armed Bandits (2026-05-28) — https://arxiv.org/abs/2605.29268 · 584.1 · inconnu · page ou résumé
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.1 · oui, mesuré · lecture approfondie · machine

**exploration n° 7 — Tirages indépendants, bifurcations, redémarrages, meilleur de N : bases simples de l'exploration**

10 mécanismes, 10 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 3. Lecture : lecture approfondie 2, page ou résumé 8.

- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.0 · oui, mesuré · page ou résumé · machine
- Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery (2026-07-05) — https://arxiv.org/abs/2607.04108 · 136.1 · oui, mesuré · page ou résumé · machine
- AI-Powered (Finance) Scholarship (2024-12) — https://www.nber.org/papers/w33363 · 394.0 · oui, affirmé · page ou résumé
- Large Language Bayes (2025-04-18) — https://arxiv.org/abs/2504.14025 · 395.0 · oui, mesuré · page ou résumé · machine
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.2 · oui, mesuré · lecture approfondie
- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) — https://openreview.net/forum?id=Ur08wiPVM3 · 502.0 · oui, mesuré · page ou résumé
- LLM Evolutionary Search Strategies Should be Compared by Tokens (2026-10-13) — https://arxiv.org/abs/2610.23977 · 581.1 · oui, mesuré · lecture approfondie
- Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search (2026-09-17) — https://arxiv.org/abs/2609.19799 · 582.1 · oui, mesuré · page ou résumé
- Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training (2026-09-22) — https://arxiv.org/abs/2609.25510 · 583.0 · oui, affirmé · page ou résumé
- Large Language Monkeys: Scaling Inference Compute with Repeated Sampling (2024-07-31) — https://arxiv.org/abs/2407.21787 · 591.0 · oui, affirmé · page ou résumé

**exploration n° 8 — Équipes d'agents : rôles, débat, coordination, communication, isolement, composition du vivier de proposeurs**

26 mécanismes, 25 travaux (9 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9, oui, affirmé 6, non 2, inconnu 9. Lecture : page ou résumé 25.

- Scaling Discovery Requires Forgetting (2026-10-14) — https://arxiv.org/abs/2610.20563 · 10.1 · oui, mesuré · page ou résumé
- Creative Generation via Multi-Agent Debate: Does Debate Suppress Diversity? (2026-09-01) — https://arxiv.org/abs/2609.00683 · 19.0 · oui, affirmé · page ou résumé
- The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams (2026-08-24) — https://arxiv.org/abs/2608.23541 · 22.0 · oui, affirmé · page ou résumé
- LLM Jaggedness Unlocks Scientific Creativity (2026-05-11) — https://arxiv.org/abs/2605.10574 · 46.1 · oui, affirmé · page ou résumé
- Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation (2026-04-20) — https://arxiv.org/abs/2604.18005 · 48.1 · non · page ou résumé
- Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition (2026-11-03) — https://arxiv.org/abs/2611.04420 · 53.1 · oui, affirmé · page ou résumé
- Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery (2026-09-28) — https://arxiv.org/abs/2609.35315 · 111.0 · inconnu · page ou résumé · machine
- Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery (2026-11-16) — https://arxiv.org/abs/2611.21847 · 126.0 · inconnu · page ou résumé · machine
- SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization (2026-11-05) — https://arxiv.org/abs/2611.08483 · 127.0 · inconnu · page ou résumé
- Distill, Debate, Discover: Grounding Multi-Agent Research Ideation in Graph-Distilled Insights (2026-10-23) — https://arxiv.org/abs/2610.33366 · 128.0 · inconnu · page ou résumé · machine
- The Weight of Teamwork: Does Communication Structure Help LLM Scientists Search for Scientific Laws? (2026-10-16) — https://arxiv.org/abs/2610.24131 · 130.1 · inconnu · page ou résumé
- Can AI Scientists Coordinate at Runtime? (2026-09-17) — https://arxiv.org/abs/2610.00980 · 131.0 · oui, mesuré · page ou résumé
- Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation (2026-05-06) — https://arxiv.org/abs/2605.04922 · 143.1 · oui, mesuré · page ou résumé
- Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station (2026-09-16) — https://arxiv.org/abs/2610.08927 · 178.0 · oui, mesuré · page ou résumé
- Accelerating scientific discovery with Co-Scientist (2025-02-26) — https://arxiv.org/abs/2502.18864 · 245.0 · oui, affirmé · page ou résumé · machine
- Automated Weak-to-Strong Researcher (2026-04-14) — https://alignment.anthropic.com/2026/automated-w2s-researcher/ · 259.0 · oui, mesuré · page ou résumé · machine
- AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration (2026-03-15) — https://arxiv.org/abs/2605.20025 · 279.0 · inconnu · page ou résumé · machine
- AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework (2026-09-24) — https://arxiv.org/abs/2609.30541 · 359.1 · inconnu · page ou résumé
- CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery (2026-04-02) — https://arxiv.org/abs/2604.01658 · 398.0 · oui, mesuré · page ou résumé · machine
- Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors (2026-09-22) — https://arxiv.org/abs/2609.27051 · 441.2 · oui, affirmé · page ou résumé · machine
- Coarse-Grained Dynamics of Multi-Agent Collective AutoResearch (2026-09-19) — https://openreview.net/forum?id=HorMYlEerY · 509.0 · oui, mesuré · page ou résumé
- How Many Scientists? Epistemic Diversity in Expanding-Frontier Discovery (2026-09-19) — https://openreview.net/forum?id=mqzDjlr57k · 543.0, 543.2 · oui, mesuré · page ou résumé
- Against Homogeneous Consensus: Why Scientific Discovery Requires Heterogeneous Adversarial LLM Agents (2026-03-16) — https://openreview.net/forum?id=Vm1U9Sh4wV · 571.0 · non · page ou résumé
- AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation (2026-05-27) — https://arxiv.org/abs/2605.28655 · 611.0 · inconnu · page ou résumé · machine
- Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction (2026-08-25) — https://arxiv.org/abs/2608.24001 · 619.0 · inconnu · page ou résumé

**exploration n° 9 — Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur**

9 mécanismes, 9 travaux (4 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 1, inconnu 3. Lecture : page ou résumé 9.

- JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models (2026-10-09) — https://arxiv.org/abs/2610.13194 · 105.0 · inconnu · page ou résumé
- AIM: Agentic Idea Management for Automated Research (2026-09-16) — https://arxiv.org/abs/2609.38445 · 110.0 · oui, mesuré · page ou résumé · machine
- Letting AI Formulate the Research Question: Autonomous Research Agents (2026-10-29) — https://arxiv.org/abs/2610.39620 · 145.0 · oui, mesuré · page ou résumé
- Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench (2026-10-13) — https://arxiv.org/abs/2610.18938 · 170.0 · inconnu · page ou résumé
- Explore, Then Commit: Measurement-Efficient Scientific Law Discovery with Language Models (2026-10-06) — https://arxiv.org/abs/2610.07620 · 176.1 · inconnu · page ou résumé
- AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise (2025-06-30) — https://arxiv.org/abs/2507.00310 · 198.0 · oui, mesuré · page ou résumé · machine
- An AI Scientist that Doesn't Drift: Taste, Structure, and Falsifiable Findings in a Quadruped Navigation Research Loop (2026-07-30) — https://arxiv.org/abs/2608.07542 · 332.0 · oui, affirmé · page ou résumé · machine
- Principle-Evolvable Scientific Discovery via Uncertainty Minimization (2026-02-06) — https://arxiv.org/abs/2602.06448 · 397.0 · oui, mesuré · page ou résumé · machine
- ConflictGuide: AutoResearch Improves When Competing Behaviors Are Made Visible (2026-09-07) — https://openreview.net/forum?id=LL5XvuYznc · 535.0 · oui, mesuré · page ou résumé

**exploration n° 10 — Mesures de l'exploration d'un run : bassins d'idées, étroitesse, plateau, redécouverte, espace d'hypothèses**

16 mécanismes, 16 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 12, inconnu 4. Lecture : page ou résumé 15, notice seule 1.

- Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game (2026-10-13) — https://arxiv.org/abs/2611.14487 · 1.1 · oui, mesuré · page ou résumé
- SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery (2026-07-02) — https://arxiv.org/abs/2607.02807 · 30.0 · oui, mesuré · page ou résumé · machine
- Modeling Authentic Research Trajectories: A Graph View of Research Ideation (2026-10-19) — https://arxiv.org/abs/2610.27337 · 146.0 · inconnu · page ou résumé
- Open-Endedness Bench: Measuring Epistemic Process from Agent Records (2026-09-14) — https://arxiv.org/abs/2610.02588 · 180.2 · oui, mesuré · page ou résumé
- Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery (2026-07-17) — https://arxiv.org/abs/2607.15766 · 189.0 · oui, mesuré · page ou résumé
- FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games (2026-06-03) — https://arxiv.org/abs/2606.04751 · 191.1 · inconnu · page ou résumé
- Evaluating LLMs' Divergent Thinking Capabilities for Scientific Idea Generation with Minimal Context (2024-12-23) — https://arxiv.org/abs/2412.17596 · 248.0 · inconnu · page ou résumé
- ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds (2026-09-24) — https://arxiv.org/abs/2609.30199 · 418.1 · oui, mesuré · page ou résumé
- How models explore ideas (2026-11-10) — https://bespokelabs.ai/blog/how-models-explore-ideas · 462.0 · oui, mesuré · page ou résumé
- Introducing AutoResearchExam (billet, page du banc et dépôt bespokelabsai/AutoResearchExam) (2026-09-10) — https://benchmarks.bespokelabs.ai/autoresearchexam/ · 463.1 · oui, mesuré · page ou résumé
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) — https://metr.org/blog/2026-07-21-expenditure-horizon/ · 464.1 · oui, mesuré · page ou résumé
- fab: how to do (alignment) research at scale (2026) — https://www.lesswrong.com/posts/tKkyzDSqDrduEvawc/fab-how-to-do-alignment-research-at-scale · 474.0 · inconnu · notice seule
- IdeaCompass: Making Exploration Measurable in Autonomous AI Research Agents (2026-09-18) — https://openreview.net/forum?id=ZamzIss4oQ · 501.1 · oui, mesuré · page ou résumé
- IdeaPrism: Beyond Ground-Truth Matching for Hypothesis Evaluation (2026-09-12) — https://openreview.net/forum?id=9YBQu8n3Uk · 522.1 · oui, mesuré · page ou résumé
- Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry (2026-08-07) — https://openreview.net/forum?id=IZjj0suAJZ · 551.2 · oui, mesuré · page ou résumé
- Search Pathology Diagnosis for Automated Discovery (2026-09-06) — https://openreview.net/forum?id=H9X0A1afdz · 554.1 · oui, mesuré · page ou résumé

**exploration n° 11 — Diagnostics de l'effondrement de la diversité et de l'homogénéité des idées**

19 mécanismes, 19 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 13, oui, affirmé 2, inconnu 4. Lecture : page ou résumé 19.

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) — https://arxiv.org/abs/2611.21408 · 0.1 · oui, mesuré · page ou résumé
- Language Models are Lazy Poets: Creative Mode Collapse at Scale (2026-10-16) — https://arxiv.org/abs/2610.24223 · 8.0 · inconnu · page ou résumé
- Large Language Models Extend Known Research But Do Not Create New Research Directions (2026-10-12) — https://arxiv.org/abs/2610.17439 · 11.1 · oui, mesuré · page ou résumé
- Measuring the Gap Between Human and LLM Research Ideas (2026-07-01) — https://arxiv.org/abs/2607.01233 · 31.1 · oui, affirmé · page ou résumé
- Contemporary AI lacks the imagination to diverge or negate in science (2026-06-06) — https://arxiv.org/abs/2606.08251 · 36.1 · oui, mesuré · page ou résumé
- AI Research Agents Narrow Scientific Exploration (2026-05-27) — https://arxiv.org/abs/2605.27905 · 39.0 · oui, mesuré · page ou résumé
- Multi-LLM Systems Exhibit Robust Semantic Collapse (2026-05-16) — https://arxiv.org/abs/2605.17193 · 43.0 · inconnu · page ou résumé
- Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs (2026-05-11) — https://arxiv.org/abs/2605.11128 · 45.0 · inconnu · page ou résumé
- Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation (2026-04-20) — https://arxiv.org/abs/2604.18005 · 48.0 · oui, mesuré · page ou résumé
- A Cognitive Framework for Idea Diversity in Large Language Models (2026-02-23) — https://arxiv.org/abs/2602.20408 · 49.0 · inconnu · page ou résumé
- What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity (2025-11-19) — https://arxiv.org/abs/2511.15593 · 233.0 · oui, mesuré · page ou résumé
- Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) (2025-10-27) — https://arxiv.org/abs/2510.22954 · 235.0 · oui, affirmé · page ou résumé
- Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024-09-06) — https://arxiv.org/abs/2409.04109 · 253.1 · oui, mesuré · page ou résumé
- Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization (2026-05-19) — https://arxiv.org/abs/2605.19782 · 399.0 · oui, mesuré · page ou résumé
- Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution (2026-06-03) — https://arxiv.org/abs/2606.05408 · 401.0 · oui, mesuré · page ou résumé
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) — https://arxiv.org/abs/2610.24291 · 408.0 · oui, mesuré · page ou résumé
- Homogenization in Multi-Agent Systems (2026-09-18) — https://openreview.net/forum?id=giMpNTtGsL · 507.0 · oui, mesuré · page ou résumé
- Outside the Dictionary: LLM-Guided Equation Discovery Is Limited by What It Proposes (2026-09-18) — https://openreview.net/forum?id=gb3n5lRwjw · 545.2 · oui, mesuré · page ou résumé
- Same Algorithms, Different Scientist: Design Space Bias in AI Discovery (2026-08-29) — https://openreview.net/forum?id=zrObNoC4GY · 549.2 · oui, mesuré · page ou résumé

**exploration n° 12 — Remèdes à l'effondrement de la diversité, et leurs limites : diversification dirigée, repondération, injection de sujets, dissidence imposée**

14 mécanismes, 14 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9, non 2, inconnu 3. Lecture : page ou résumé 14.

- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) — https://arxiv.org/abs/2609.00077 · 20.0 · oui, mesuré · page ou résumé
- Budgeted Subset Refinement for Execution-Aware LLM Research Ideation (2026-05-09) — https://arxiv.org/abs/2607.14118 · 90.2 · oui, mesuré · page ou résumé
- ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery (2026-09-17) — https://arxiv.org/abs/2610.29303 · 101.1 · oui, mesuré · page ou résumé
- Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and Connection in Base Language Models (2026-08-20) — https://arxiv.org/abs/2608.19893 · 404.0 · oui, mesuré · page ou résumé
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) — https://arxiv.org/abs/2610.24291 · 408.2 · oui, mesuré · page ou résumé
- Directing to Diversify: Multi-Directional Search for Automatic Heuristic Design (2026-10-22) — https://arxiv.org/abs/2610.31048 · 409.0 · oui, mesuré · page ou résumé
- r2m-ai/scholar-loop (2026-06-15) — https://github.com/r2m-ai/scholar-loop · 491.1 · inconnu · page ou résumé · machine
- Homogenization in Multi-Agent Systems (2026-09-18) — https://openreview.net/forum?id=giMpNTtGsL · 507.1 · oui, mesuré · page ou résumé
- Gap Detection: Mitigating Homogenization through Demand and Defensibility (2026-09-18) — https://openreview.net/forum?id=daTX7ANiGL · 508.0 · oui, mesuré · page ou résumé
- Hypothesis Portfolio Search: Shared Feedback for Genetic Perturbation Discovery (2026-09-18) — https://openreview.net/forum?id=NQ43G4FtQH · 541.2 · oui, mesuré · page ou résumé · machine
- Unlearning Sycophancy Improves Machine Creativity in Large Language Models (2026-09-17) — https://openreview.net/forum?id=Mms8QWnalJ · 542.0 · non · page ou résumé
- On the Effects of Reasoning Effort and Prompt-Based Diversification on Scientific Ideation Diversity (2026-04-21) — https://openreview.net/forum?id=xt5P634aET · 566.0 · non · page ou résumé
- Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity (2025-10-01) — https://arxiv.org/abs/2510.01171 · 614.0 · inconnu · page ou résumé
- AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining (2026-09-24) — https://arxiv.org/abs/2609.29014 · 615.0 · inconnu · page ou résumé

**exploration n° 13 — Entraînement de l'exploration par renforcement ou supervision**

4 mécanismes, 4 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4. Lecture : page ou résumé 4.

- Training Reasoning Models to Generate Diverse Scientific Ideas (2026-09-18) — https://arxiv.org/abs/2610.22324 · 9.0 · oui, mesuré · page ou résumé
- Reinforcing Agentic Creativity in Scientific Ideation with Night Science (2026-09-18) — https://arxiv.org/abs/2609.35706 · 15.0 · oui, mesuré · page ou résumé
- TIGER: Learning from Researcher Taste to Generate Tailored Research Ideas (2026-09-17) — https://arxiv.org/abs/2611.02234 · 56.0 · oui, mesuré · page ou résumé
- Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents (2026-06-30) — https://arxiv.org/abs/2606.31229 · 154.0 · oui, mesuré · page ou résumé

**exploration n° 14 — Un seul agent, une seule lignée : boucle simple ou chaîne complète**

2 mécanismes, 2 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 2. Lecture : page ou résumé 2.

- The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (2024-08-12) — https://arxiv.org/abs/2408.06292 · 254.0 · oui, affirmé · page ou résumé · machine
- autoresearch (dépôt de code) (2026-03-06) — https://github.com/karpathy/autoresearch · 396.0 · oui, affirmé · page ou résumé · machine

**exploration n° 15 — Résultats négatifs ou nuls sur des composants d'exploration : rôles, récupération, opérateurs, architectures**

9 mécanismes, 9 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 2. Lecture : lecture approfondie 1, page ou résumé 8.

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) — https://arxiv.org/abs/2611.21408 · 0.3 · oui, mesuré · page ou résumé
- Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty (2026-06-23) — https://arxiv.org/abs/2606.25198 · 32.0 · oui, mesuré · page ou résumé
- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.4 · oui, mesuré · lecture approfondie · machine
- Operator Packages, Proposer Strength, and Construction-Family Plateaus in Office-Scale Verified Search (2026-08-28) — https://arxiv.org/abs/2609.29636 · 405.0 · oui, mesuré · page ou résumé
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) — https://arxiv.org/abs/2610.24291 · 408.3 · oui, mesuré · page ou résumé
- Ground, Iterate, Trace: Decomposing AI Research Ideation (2026-09-18) — https://openreview.net/forum?id=IIRDWIcWDM · 520.0 · oui, mesuré · page ou résumé
- HorizonBench: Evaluating Ideation Agents on Future Scientific Discoveries (2026-05-26) — https://openreview.net/forum?id=EcRNKKVL1O · 569.2 · oui, mesuré · page ou résumé
- The Illusion of Multi-Agent Advantage (2026-06-11) — https://arxiv.org/abs/2606.13003 · 588.0 · oui, affirmé · page ou résumé
- Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models (2026-09-26) — https://arxiv.org/abs/2609.35875 · 612.0 · oui, affirmé · page ou résumé

**exploration n° 16 — Positions et théories de l'exploration**

6 mécanismes, 6 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 1, non 5. Lecture : page ou résumé 5, notice seule 1.

- The Greatness of Science Cannot Be Planned: Agentic Auto-Research is Fuzz Testing (2026-08-10) — https://arxiv.org/abs/2608.09855 · 24.0 · non · page ou résumé
- Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks (2026-06-12) — https://arxiv.org/abs/2606.14386 · 34.0 · oui, affirmé · page ou résumé
- Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery (2026-05-09) — https://arxiv.org/abs/2605.08956 · 215.0 · non · page ou résumé
- Navigating Epistemic Monocultures in AI-Driven Science: A Simulation Study (2026-08-19) — https://arxiv.org/abs/2608.19390 · 403.0 · non · page ou résumé
- Sampling Is Not Curiosity: Why LLM Agents Should Investigate (2026-11-07) — https://arxiv.org/abs/2611.10501 · 410.0 · non · page ou résumé
- You Are Not Immune To Mode Collapse (2026-05) — https://www.lesswrong.com/posts/vKtuRbo4e3ffixmee/you-are-not-immune-to-mode-collapse · 475.0 · non · notice seule

**exploration n° 17 — Exploration décrite sans mécanisme précisé par la notice**

5 mécanismes, 5 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : non 2, inconnu 3. Lecture : page ou résumé 5.

- Evolutionary Intelligence for Scientific Discovery: From Evolutionary Computation to Cumulative Discovery Systems (2026-07-10) — https://arxiv.org/abs/2607.09025 · 222.1 · non · page ou résumé
- TASTE: Can AI Models Judge AI Safety Research Proposals? (2026-08-28) — https://alignment.anthropic.com/2026/taste/ · 258.2 · non · page ou résumé
- MindFlow: Mind Supernet Powered Thinking Flows for Research Idea Innovation (2026-10-08) — https://arxiv.org/abs/2610.11966 · 370.0 · inconnu · page ou résumé · machine
- APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents (2026-05-20) — https://arxiv.org/abs/2605.21240 · 400.1 · inconnu · page ou résumé
- A Probabilistic Framework for LLM-Based Model Discovery (2026-02-20) — https://arxiv.org/abs/2602.18266 · 429.0 · inconnu · page ou résumé

### Famille « originalité »

**originalité n° 1 — Nouveauté mesurée par distance ou direction dans un espace de plongements ou de structures ; limites de ces distances**

8 mécanismes, 8 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 8. Lecture : page ou résumé 8.

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) — https://arxiv.org/abs/2611.21408 · 0.0 · oui, mesuré · page ou résumé
- AlienBench: A Benchmark of Structural Novelty in Language Model Outputs (2026-11-06) — https://arxiv.org/abs/2611.09094 · 4.0 · oui, mesuré · page ou résumé
- Large Language Models Extend Known Research But Do Not Create New Research Directions (2026-10-12) — https://arxiv.org/abs/2610.17439 · 11.0 · oui, mesuré · page ou résumé
- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.4 · oui, mesuré · page ou résumé · machine
- Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution (2026-06-03) — https://arxiv.org/abs/2606.05408 · 401.1 · oui, mesuré · page ou résumé
- Do Semantic Distance Tests Actually Predict Creativity in LLMs? Evidence for Jagged Creativity (2026-05-13) — https://arxiv.org/abs/2605.13450 · 413.0 · oui, mesuré · page ou résumé
- StructSim: Measuring Idea Similarity at Scale Through Structural Representation (2026-09-28) — https://arxiv.org/abs/2609.34046 · 419.0 · oui, mesuré · page ou résumé
- IdeaCompass: Making Exploration Measurable in Autonomous AI Research Agents (2026-09-18) — https://openreview.net/forum?id=ZamzIss4oQ · 501.0 · oui, mesuré · page ou résumé

**originalité n° 2 — Nouveauté mesurée contre la littérature : récupération d'antériorité, décomposition en contributions ou en facettes, vérification par recherche documentaire**

11 mécanismes, 11 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, inconnu 4. Lecture : page ou résumé 10, notice seule 1.

- Measuring the Creativity of Frontier LLMs in Automated Research (2026-09-12) — https://arxiv.org/abs/2609.14057 · 18.0 · oui, mesuré · page ou résumé
- Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks (2026-08-30) — https://arxiv.org/abs/2608.30047 · 21.0 · oui, mesuré · page ou résumé
- Do AI Scientists Know What's New? (2026-10-27) — https://arxiv.org/abs/2610.36511 · 59.0 · oui, mesuré · page ou résumé
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (2025-04-08) — https://arxiv.org/abs/2504.08066 · 241.2 · inconnu · page ou résumé · machine
- All That Glitters is Not Novel: Plagiarism in AI Generated Research (2025-02-23) — https://arxiv.org/abs/2502.16487 · 246.0 · oui, mesuré · page ou résumé
- The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (2024-08-12) — https://arxiv.org/abs/2408.06292 · 254.3 · inconnu · page ou résumé · machine
- SciMON: Scientific Inspiration Machines Optimized for Novelty (2023-05-23) — https://arxiv.org/abs/2305.14259 · 257.0 · inconnu · notice seule
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (2026-08-28) — https://arxiv.org/abs/2608.28945 · 460.2 · inconnu · page ou résumé
- EGRD: Assessing Research Novelty through Evidence-Grounded Residual Decomposition (2026-09-17) — https://openreview.net/forum?id=az80j8XH3L · 531.0 · oui, mesuré · page ou résumé
- NovCompass: Scientific Novelty Analysis through Traceable Paper Comparison (2026-09-16) — https://openreview.net/forum?id=wPHKdqHuzl · 532.0 · oui, mesuré · page ou résumé
- Recombination or Discovery? A Retrieval-Grounded Novelty Audit of Machine-Generated Research Papers (2026-07-30) — https://openreview.net/forum?id=Ew2phMa9Ou · 547.0 · oui, mesuré · page ou résumé

**originalité n° 3 — Nouveauté jugée par un modèle ou par des experts : bancs de nouveauté, étalonnage du juge, limites du juge modèle**

12 mécanismes, 11 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9, non 1, inconnu 2. Lecture : page ou résumé 10, notice seule 1.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.4 · oui, mesuré · page ou résumé · machine
- Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation (2026-10-01) — https://arxiv.org/abs/2610.02022 · 68.0, 68.2 · oui, mesuré · page ou résumé
- NovGauge: A Fine-Grained Benchmark for Diagnosing LLMs' Capability in Paper Novelty Assessment (2026-09-10) — https://arxiv.org/abs/2609.11234 · 71.0 · inconnu · page ou résumé
- Think-Probe-Respond: Improving Large Language Models as Judges of Research Idea Novelty (2026-08-26) — https://arxiv.org/abs/2608.25660 · 77.1 · oui, mesuré · page ou résumé
- On the Limits of LLM-as-Judge for Scientific Novelty Assessment (2026-06-10) — https://arxiv.org/abs/2606.12071 · 86.1 · oui, mesuré · page ou résumé
- An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics (2026-04-16) — https://arxiv.org/abs/2604.15145 · 91.0 · oui, mesuré · page ou résumé
- Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas (2026-03-11) — https://arxiv.org/abs/2603.10303 · 94.1 · oui, mesuré · page ou résumé
- Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024-09-06) — https://arxiv.org/abs/2409.04109 · 253.2 · non · page ou résumé
- NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment (2026-04-13) — https://arxiv.org/abs/2604.11543 · 459.0 · inconnu · notice seule
- MathIdeaBench: A Benchmark For Mathematical Research Idea Generation (2026-08-26) — https://openreview.net/forum?id=yIlEoQe7es · 526.1 · oui, mesuré · page ou résumé
- What Does a Machine-Written Submission Actually Contain? A Pre-Registered Citation and Readiness Audit of an Autonomous Research Agent (2026-08-28) — https://openreview.net/forum?id=zmzPzCj2Cm · 563.1 · oui, mesuré · page ou résumé

**originalité n° 4 — Nouveauté comme écart de croyance ou d'a priori : surprise avant et après la preuve, vrai en excès, information indépendante, test contre les lois publiées**

6 mécanismes, 6 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4, oui, affirmé 1, inconnu 1. Lecture : lecture approfondie 2, page ou résumé 4.

- Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks (2026-06-12) — https://arxiv.org/abs/2606.14386 · 34.1 · oui, affirmé · page ou résumé
- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.1 · oui, mesuré · lecture approfondie · machine
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.0 · oui, mesuré · lecture approfondie · machine
- AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise (2025-06-30) — https://arxiv.org/abs/2507.00310 · 198.1 · oui, mesuré · page ou résumé · machine
- Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior (2025-06-03) — https://arxiv.org/abs/2506.03444 · 574.0 · inconnu · page ou résumé
- Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing (SSRN 6569258 ; lu sur la copie de conférence) (2026-04) — https://skbi.smu.edu.sg/sites/skbi.smu.edu.sg/files/2026-06/Day1_0915_Danqing%20Mei%20(paper).pdf · 623.2 · oui, mesuré · page ou résumé

**originalité n° 5 — Diversité et homogénéité des sorties ou des populations : effondrement de mode, monoculture, idées uniques, redondance d'options**

24 mécanismes, 24 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 11, oui, affirmé 2, non 3, inconnu 8. Lecture : page ou résumé 24.

- Evaluating LLM Creativity through Long-Tail Performance (2026-10-09) — https://arxiv.org/abs/2610.12998 · 12.0 · inconnu · page ou résumé
- Auditing Pairwise Equivalence Judgments: Self-Critique Effects and Diversity Measurement in Multi-Agent Hypothesis Generation (2026-09-14) — https://arxiv.org/abs/2610.04133 · 14.1 · oui, mesuré · page ou résumé
- How Strong Is the Evidence for the Artificial Hivemind? Reevaluating Evidence for the Open-Ended Homogeneity of Language Models (2026-09-27) — https://arxiv.org/abs/2609.33936 · 16.0 · inconnu · page ou résumé
- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) — https://arxiv.org/abs/2609.00077 · 20.4 · oui, mesuré · page ou résumé
- Are LLMs becoming similarly creative? Evidence from three years of models (2026-08-19) — https://arxiv.org/abs/2608.19437 · 23.0 · inconnu · page ou résumé
- The Hitchhiker's Guide to Monoculture: AI Homogenizes Syntax, Not (Necessarily) Semantics (2026-07-12) — https://arxiv.org/abs/2607.13077 · 28.0 · inconnu · page ou résumé
- Comment on arXiv:2607.01233: Survivorship Bias in Published-Paper Baselines for Research-Idea Distributions (2026-07-09) — https://arxiv.org/abs/2609.15996 · 29.0 · non · page ou résumé
- Measuring the Gap Between Human and LLM Research Ideas (2026-07-01) — https://arxiv.org/abs/2607.01233 · 31.0 · oui, mesuré · page ou résumé
- Thinking Like a Scientist? A Structural Study of LLM-Generated Research Methods (2026-06-15) — https://arxiv.org/abs/2606.26130 · 33.0 · inconnu · page ou résumé
- AI Research Agents Narrow Scientific Exploration (2026-05-27) — https://arxiv.org/abs/2605.27905 · 39.1 · oui, mesuré · page ou résumé
- LLM Jaggedness Unlocks Scientific Creativity (2026-05-11) — https://arxiv.org/abs/2605.10574 · 46.0 · oui, mesuré · page ou résumé
- Ex Ante Evaluation of AI-Induced Idea Diversity Collapse (2026-05-07) — https://arxiv.org/abs/2605.06540 · 47.0 · inconnu · page ou résumé
- A Cognitive Framework for Idea Diversity in Large Language Models (2026-02-23) — https://arxiv.org/abs/2602.20408 · 49.1 · inconnu · page ou résumé
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.1 · oui, mesuré · page ou résumé
- Unlocking LLM Creativity in Science through Analogical Reasoning (2026-05-11) — https://arxiv.org/abs/2605.11258 · 158.1 · oui, mesuré · page ou résumé
- Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output (2026-05-01) — https://arxiv.org/abs/2605.00557 · 160.1 · inconnu · page ou résumé
- Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) (2025-10-27) — https://arxiv.org/abs/2510.22954 · 235.1 · oui, affirmé · page ou résumé
- Diversifying Personalized Research Ideation against AI-Induced Homogenization (2026-07-30) — https://arxiv.org/abs/2607.28087 · 323.1 · oui, affirmé · page ou résumé
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) — https://arxiv.org/abs/2610.24291 · 408.1 · oui, mesuré · page ou résumé
- Gap Detection: Mitigating Homogenization through Demand and Defensibility (2026-09-18) — https://openreview.net/forum?id=daTX7ANiGL · 508.1 · oui, mesuré · page ou résumé
- Mathematica Incognita: Characterizing Open-Ended Mathematical Exploration in Language Models (2026-09-19) — https://openreview.net/forum?id=z0nQAdCOH0 · 540.1 · oui, mesuré · page ou résumé
- Same Algorithms, Different Scientist: Design Space Bias in AI Discovery (2026-08-29) — https://openreview.net/forum?id=zrObNoC4GY · 549.1 · oui, mesuré · page ou résumé
- On the Effects of Reasoning Effort and Prompt-Based Diversification on Scientific Ideation Diversity (2026-04-21) — https://openreview.net/forum?id=xt5P634aET · 566.1 · non · page ou résumé
- When Idea Generation Scales: Idea-Level Evaluation for Autonomous Scientific Discovery (2026-05-20) — https://openreview.net/forum?id=4N7tBhjF8f · 567.0 · non · page ou résumé

**originalité n° 6 — Protection contre la contamination et la mémorisation : coupure de date, mondes contrefactuels, graine privée, masquage, banques renouvelées**

21 mécanismes, 21 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, oui, affirmé 8, non 1, inconnu 9. Lecture : page ou résumé 21.

- Tracing the Scientific Discovery Capacity of LLMs to Their Training Data (2026-11-02) — https://arxiv.org/abs/2611.03617 · 5.0 · inconnu · page ou résumé
- Eliciting Research Taste in LLMs through Future Research Direction Choice (2026-06-29) — https://arxiv.org/abs/2611.19794 · 51.2 · oui, affirmé · page ou résumé
- Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents (2026-09-07) — https://arxiv.org/abs/2609.09219 · 73.1 · oui, affirmé · page ou résumé
- Can Large Language Models Forecast What Researchers Study Next? (2026-09-01) — https://arxiv.org/abs/2609.00747 · 75.1 · inconnu · page ou résumé
- Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies (2026-08-17) — https://arxiv.org/abs/2608.16645 · 80.1 · inconnu · page ou résumé
- Unsatz: Evaluating Scientific Discovery Without a Given Ansatz (2026-10-31) — https://arxiv.org/abs/2611.03713 · 162.1 · inconnu · page ou résumé
- SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World (2026-10-27) — https://arxiv.org/abs/2610.37919 · 165.1 · inconnu · page ou résumé
- Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes (2026-09-29) — https://arxiv.org/abs/2609.36726 · 181.1 · inconnu · page ou résumé
- Can LLMs Discover Scientific Laws in Real and Parallel Worlds? (2026-09-01) — https://arxiv.org/abs/2609.01552 · 184.1 · inconnu · page ou résumé
- DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking (2026-05-25) — https://arxiv.org/abs/2605.26087 · 193.1 · oui, affirmé · page ou résumé
- NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents (2025-10-08) — https://arxiv.org/abs/2510.07172 · 196.1 · inconnu · page ou résumé
- LLMs are below chance on TASTE once a shortcut is removed (2026-11-15) — https://www.lesswrong.com/posts/tpKE33scJGzqYKEBW/llms-are-weirdly-below-chance-on-taste-without-a-shortcut · 260.1 · oui, affirmé · page ou résumé
- Can Frontier Models Autocomplete Safety Research? (2026-07-12) — https://www.lesswrong.com/posts/Tdk698MTERHg4tdpG/can-frontier-models-autocomplete-safety-research · 261.1 · oui, affirmé · page ou résumé
- Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot (2026-08-17) — https://arxiv.org/abs/2608.16795 · 415.1 · oui, mesuré · page ou résumé
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) — https://github.com/Dawes-Institute/ai-peer-review-benchmark · 489.2 · non · page ou résumé
- Do LLMs Have Research Taste? An Analysis Using BóLèBench (2026-09-12) — https://openreview.net/forum?id=vSABCIC1OM · 500.2 · oui, affirmé · page ou résumé
- Beyond Hypothesis Recovery: Evaluating Scientific Hypothesis Generation through Evidence-Hypothesis Transitions (2026-09-19) — https://openreview.net/forum?id=71lz12sujF · 538.1 · inconnu · page ou résumé
- Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists (2026-09-25) — https://openreview.net/forum?id=KqWQxzp9Xn · 553.2 · oui, mesuré · page ou résumé
- Beyond Imitation: Evaluating LLM Reviewers by Impact ? (2026-08-29) — https://openreview.net/forum?id=TiAGTPFXW5 · 562.1 · oui, mesuré · page ou résumé
- HorizonBench: Evaluating Ideation Agents on Future Scientific Discoveries (2026-05-26) — https://openreview.net/forum?id=EcRNKKVL1O · 569.1 · oui, affirmé · page ou résumé
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) — https://openreview.net/forum?id=KufsJAHeGn · 572.1 · oui, affirmé · page ou résumé

**originalité n° 7 — Absence de contrôle de nouveauté, ou débat sur sa définition**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : non 2. Lecture : page ou résumé 1, notice seule 1.

- The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery (2026-10-13) — https://arxiv.org/abs/2610.18933 · 375.3 · non · page ou résumé
- Have LLMs Generated Novel Insights? (2025-02) — https://www.lesswrong.com/posts/GADJFwHzNZKg2Ndti/have-llms-generated-novel-insights · 471.0 · non · notice seule

### Famille « épreuve »

**épreuve n° 1 — Mondes plantés à vérité connue du constructeur : mondes simulés, générés ou contrefactuels, erreurs plantées, tables entièrement tabulées**

18 mécanismes, 17 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9, oui, affirmé 4, inconnu 5. Lecture : lecture approfondie 2, page ou résumé 15.

- Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks (2026-06-12) — https://arxiv.org/abs/2606.14386 · 34.2 · oui, mesuré · page ou résumé
- Auditing AI peer reviewers: a benchmark on real scientific papers (2026-11-12) — https://arxiv.org/abs/2611.17052 · 52.0 · oui, mesuré · page ou résumé
- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.0 · oui, mesuré · lecture approfondie · machine
- Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents (2026-10-10) — https://arxiv.org/abs/2610.14683 · 104.0 · oui, affirmé · page ou résumé · machine
- Unsatz: Evaluating Scientific Discovery Without a Given Ansatz (2026-10-31) — https://arxiv.org/abs/2611.03713 · 162.0 · inconnu · page ou résumé
- Can LLMs Uncover Hidden Physical Laws through Free Exploration? (2026-10-27) — https://arxiv.org/abs/2610.37649 · 164.0 · oui, mesuré · page ou résumé
- SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World (2026-10-27) — https://arxiv.org/abs/2610.37919 · 165.0 · inconnu · page ou résumé
- DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists (2026-10-07) — https://arxiv.org/abs/2610.09558 · 175.0 · inconnu · page ou résumé
- Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes (2026-09-29) — https://arxiv.org/abs/2609.36726 · 181.0 · inconnu · page ou résumé
- DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking (2026-05-25) — https://arxiv.org/abs/2605.26087 · 193.0 · oui, affirmé · page ou résumé
- NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents (2025-10-08) — https://arxiv.org/abs/2510.07172 · 196.0 · inconnu · page ou résumé
- ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds (2026-09-24) — https://arxiv.org/abs/2609.30199 · 418.0 · oui, mesuré · page ou résumé
- Evaluating LLM Research Agents as Tests of Return Predictability (2026-11-02) — https://arxiv.org/abs/2611.04070 · 450.0, 450.1 · oui, mesuré · lecture approfondie
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) — https://github.com/Dawes-Institute/ai-peer-review-benchmark · 489.0 · oui, mesuré · page ou résumé
- Do AI Agents Have Research Taste? SENSE-Bench for Anomaly-Driven Scientific Exploration (2026-09-16) — https://openreview.net/forum?id=IvMOtnkFXk · 504.0 · oui, mesuré · page ou résumé
- Does Failure Feedback Direct Agent Self-Modification? (2026-10-10) — https://arxiv.org/abs/2610.14662 · 596.1 · oui, affirmé · page ou résumé
- Can an AI Scientist really discover knowledge? (banc Albert) (2026-06-05) — https://aria.org.uk/insights/can-an-ai-scientist-really-discover-knowledge · 626.0 · oui, affirmé · page ou résumé

**épreuve n° 2 — Vérité prise dans le futur : coupure de date, gel du corpus, rejeu historique, prévision contre la littérature à venir**

12 mécanismes, 12 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9, oui, affirmé 1, inconnu 2. Lecture : page ou résumé 12.

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) — https://arxiv.org/abs/2611.21408 · 0.2 · oui, mesuré · page ou résumé
- AI Research Agents Narrow Scientific Exploration (2026-05-27) — https://arxiv.org/abs/2605.27905 · 39.2 · oui, mesuré · page ou résumé
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.0 · oui, mesuré · page ou résumé
- Can Large Language Models Forecast What Researchers Study Next? (2026-09-01) — https://arxiv.org/abs/2609.00747 · 75.0 · oui, mesuré · page ou résumé
- ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment (2026-05-30) — https://arxiv.org/abs/2606.00644 · 87.0 · oui, mesuré · page ou résumé
- HindSight: Evaluating LLM-Generated Research Ideas via Future Impact (2026-03-16) — https://arxiv.org/abs/2603.15164 · 93.0 · inconnu · page ou résumé
- Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments (2026-01-12) — https://arxiv.org/abs/2601.07606 · 95.1 · inconnu · page ou résumé
- DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses (2026-10-16) — https://arxiv.org/abs/2610.23839 · 103.1 · oui, mesuré · page ou résumé
- Priced Guidance: Can Language Models Generate Future Research Ideas? (2026-09-17) — https://arxiv.org/abs/2610.04976 · 149.0 · oui, mesuré · page ou résumé
- Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot (2026-08-17) — https://arxiv.org/abs/2608.16795 · 415.0 · oui, mesuré · page ou résumé
- HorizonBench: Evaluating Ideation Agents on Future Scientific Discoveries (2026-05-26) — https://openreview.net/forum?id=EcRNKKVL1O · 569.0 · oui, mesuré · page ou résumé
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) — https://openreview.net/forum?id=KufsJAHeGn · 572.0 · oui, affirmé · page ou résumé

**épreuve n° 3 — Redécouverte d'un résultat publié, ou retrouvé d'une idée tenue cachée, comme épreuve**

9 mécanismes, 9 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9. Lecture : page ou résumé 9.

- Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game (2026-10-13) — https://arxiv.org/abs/2611.14487 · 1.0 · oui, mesuré · page ou résumé
- Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies (2026-08-17) — https://arxiv.org/abs/2608.16645 · 80.0 · oui, mesuré · page ou résumé
- OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery (2026-10-27) — https://arxiv.org/abs/2610.37739 · 166.0 · oui, mesuré · page ou résumé
- Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station (2026-09-16) — https://arxiv.org/abs/2610.08927 · 178.2 · oui, mesuré · page ou résumé
- TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents (2026-09-04) — https://arxiv.org/abs/2609.05079 · 183.0 · oui, mesuré · page ou résumé
- Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery (2026-07-17) — https://arxiv.org/abs/2607.15766 · 189.1 · oui, mesuré · page ou résumé
- FIRE-Bench: Evaluating AI Agents on the Rediscovery of Scientific Insights (2026-02-02) — https://arxiv.org/abs/2602.02905 · 195.0 · oui, mesuré · page ou résumé
- Can Frontier Models Autocomplete Safety Research? (2026-07-12) — https://www.lesswrong.com/posts/Tdk698MTERHg4tdpG/can-frontier-models-autocomplete-safety-research · 261.0 · oui, mesuré · page ou résumé
- prometheus-eval/into-the-unknown (arXiv 2610.19159) (2026-09-24) — https://arxiv.org/abs/2610.19159 · 490.0 · oui, mesuré · page ou résumé

**épreuve n° 4 — Exécution sous un évaluateur exécutable ou un correcteur programmé : l'oracle est la note calculée**

22 mécanismes, 22 travaux (7 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 16, oui, affirmé 5, inconnu 1. Lecture : lecture approfondie 2, page ou résumé 20.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.3 · oui, mesuré · page ou résumé · machine
- Scaling Discovery Requires Forgetting (2026-10-14) — https://arxiv.org/abs/2610.20563 · 10.4 · oui, mesuré · page ou résumé
- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.5 · oui, mesuré · page ou résumé · machine
- The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams (2026-08-24) — https://arxiv.org/abs/2608.23541 · 22.1 · oui, affirmé · page ou résumé
- FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics (2026-05-17) — https://arxiv.org/abs/2605.17373 · 42.1 · oui, mesuré · page ou résumé
- From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? (2026-09-18) — https://arxiv.org/abs/2611.05108 · 98.2 · oui, mesuré · lecture approfondie
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.1 · oui, mesuré · lecture approfondie · machine
- Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling (2026-10-26) — https://arxiv.org/abs/2610.35866 · 167.0 · oui, mesuré · page ou résumé
- Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild? (2026-10-20) — https://arxiv.org/abs/2610.28763 · 168.0 · oui, mesuré · page ou résumé
- Can LLMs Discover Scientific Laws in Real and Parallel Worlds? (2026-09-01) — https://arxiv.org/abs/2609.01552 · 184.0 · inconnu · page ou résumé
- How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks (2026-08-14) — https://arxiv.org/abs/2608.14905 · 185.0 · oui, mesuré · page ou résumé
- Towards Execution-Grounded Automated AI Research (2026-01-20) — https://arxiv.org/abs/2601.14525 · 229.0 · oui, mesuré · page ou résumé
- The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas (2025-06-25) — https://arxiv.org/abs/2506.20803 · 238.0 · oui, mesuré · page ou résumé
- AlphaEvolve: A coding agent for scientific and algorithmic discovery (2025-06-16) — https://arxiv.org/abs/2506.13131 · 239.1 · oui, affirmé · page ou résumé · machine
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (2025-04-08) — https://arxiv.org/abs/2504.08066 · 241.1 · oui, affirmé · page ou résumé · machine
- The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (2024-08-12) — https://arxiv.org/abs/2408.06292 · 254.1 · oui, affirmé · page ou résumé · machine
- The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery (2026-10-13) — https://arxiv.org/abs/2610.18933 · 375.0 · oui, mesuré · page ou résumé
- MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering (2024-10-09) — https://arxiv.org/abs/2410.07095 · 392.0 · oui, mesuré · page ou résumé
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts (2024-11-22) — https://arxiv.org/abs/2411.15114 · 393.0 · oui, mesuré · page ou résumé
- autoresearch (dépôt de code) (2026-03-06) — https://github.com/karpathy/autoresearch · 396.1 · oui, affirmé · page ou résumé · machine
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (2026-08-28) — https://arxiv.org/abs/2608.28945 · 460.3 · oui, mesuré · page ou résumé
- Introducing AutoResearchExam (billet, page du banc et dépôt bespokelabsai/AutoResearchExam) (2026-09-10) — https://benchmarks.bespokelabs.ai/autoresearchexam/ · 463.0 · oui, mesuré · page ou résumé

**épreuve n° 5 — Préenregistrement, engagement préalable et enregistrement des essais avant exécution ou avant les décisions**

11 mécanismes, 10 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 2, non 1, inconnu 1. Lecture : lecture approfondie 3, page ou résumé 7.

- Human diversity fuels collective creativity that large language models cannot simulate or sustain (2026-07-29) — https://arxiv.org/abs/2607.26899 · 25.1 · oui, affirmé · page ou résumé
- Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition (2026-11-03) — https://arxiv.org/abs/2611.04420 · 53.2 · oui, mesuré · page ou résumé
- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.6 · oui, mesuré · lecture approfondie · machine
- Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery (2026-05-09) — https://arxiv.org/abs/2605.08956 · 215.1 · non · page ou résumé
- LLM-as-a-Judge Version Shift: The Instrument Changed, Not the Standard (2026-09-07) — https://arxiv.org/abs/2610.32986 · 416.1 · oui, mesuré · page ou résumé
- Same Papers, Different Verdicts: Tracing Version Drift in LLM Peer Review (2026-11-16) — https://arxiv.org/abs/2611.20608 · 425.1 · oui, mesuré · page ou résumé
- Evaluating LLM Research Agents as Tests of Return Predictability (2026-11-02) — https://arxiv.org/abs/2611.04070 · 450.4, 450.6 · inconnu / oui, mesuré · lecture approfondie
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.3 · oui, mesuré · lecture approfondie
- What Does a Machine-Written Submission Actually Contain? A Pre-Registered Citation and Readiness Audit of an Autonomous Research Agent (2026-08-28) — https://openreview.net/forum?id=zmzPzCj2Cm · 563.0 · oui, mesuré · page ou résumé
- Mitigating LLM-based p-Hacking by Preregistering for the Next LLM (2026-06-26) — https://arxiv.org/abs/2606.27687 · 580.0 · oui, affirmé · page ou résumé

**épreuve n° 6 — Séparer le signal qui sert à chercher de la mesure finale : tâches tenues à l'écart, transfert, validation figée, jeu lu une fois**

17 mécanismes, 16 travaux (4 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 4, inconnu 6. Lecture : lecture approfondie 3, page ou résumé 13.

- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) — https://arxiv.org/abs/2609.00077 · 20.3 · oui, mesuré · page ou résumé
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.2, 112.5 · inconnu / oui, mesuré · lecture approfondie · machine
- Automated Weak-to-Strong Researcher (2026-04-14) — https://alignment.anthropic.com/2026/automated-w2s-researcher/ · 259.2 · oui, mesuré · page ou résumé · machine
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.7 · oui, mesuré · lecture approfondie
- Outside the Dictionary: LLM-Guided Equation Discovery Is Limited by What It Proposes (2026-09-18) — https://openreview.net/forum?id=gb3n5lRwjw · 545.0 · oui, mesuré · page ou résumé
- Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks (2026-09-27) — https://arxiv.org/abs/2609.33180 · 579.1 · oui, affirmé · page ou résumé
- Rethinking the Evaluation of Harness Evolution for Agents (2026-07-14) — https://arxiv.org/abs/2607.12227 · 585.1 · oui, mesuré · page ou résumé
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.5 · oui, mesuré · lecture approfondie · machine
- Training Language Agents to Learn from Experience (2026-05-19) — https://arxiv.org/abs/2605.20477 · 598.1 · oui, affirmé · page ou résumé
- Agent Plasticity: Measuring Self-Improvement Through Experience (2026-10-06) — https://arxiv.org/abs/2610.08902 · 600.1 · inconnu · page ou résumé
- SEAGym: An Evaluation Environment for Self-Evolving LLM Agents (2026-06-16) — https://arxiv.org/abs/2606.17546 · 602.0 · inconnu · page ou résumé
- EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer (2026-07-06) — https://arxiv.org/abs/2607.05202 · 603.0 · oui, affirmé · page ou résumé
- Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts (2026-09-16) — https://arxiv.org/abs/2609.18366 · 605.0 · oui, affirmé · page ou résumé
- One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models (2026-08-10) — https://arxiv.org/abs/2608.10178 · 606.0 · inconnu · page ou résumé
- The Ladder: A Reliable Leaderboard for Machine Learning Competitions (2015-02-16) — https://arxiv.org/abs/1502.04585 · 621.0 · inconnu · page ou résumé
- MetaEvoForge: Learning to Improve Agents Faster Across Task Environments (2026) — https://neurips.cc/virtual/2026/169839 · 625.2 · inconnu · page ou résumé · machine

**épreuve n° 7 — Témoins, nuls et placebos : base simple, nul planté, permutation, réimplémentation fraîche, plancher de bruit, opérateur classique**

14 mécanismes, 14 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 10, oui, affirmé 4. Lecture : page ou résumé 14.

- The Implementation Lottery: Auditing Idea Reliability in Automated Research (2026-07-29) — https://arxiv.org/abs/2607.26587 · 85.0 · oui, mesuré · page ou résumé
- Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery (2026-07-05) — https://arxiv.org/abs/2607.04108 · 136.0 · oui, mesuré · page ou résumé · machine
- Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution (2026-06-03) — https://arxiv.org/abs/2606.05408 · 401.2 · oui, mesuré · page ou résumé
- Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models (2026-06-15) — https://arxiv.org/abs/2606.16999 · 437.1 · oui, mesuré · page ou résumé
- The Little Scientist: What Does the Scientific Method Buy an LLM Agent? (2026-08-16) — https://arxiv.org/abs/2608.16951 · 458.0 · oui, mesuré · page ou résumé
- Approval Is Not Discovery: When Can a Model of the Scientist Steer a Discovery Agent? (2026-09-27) — https://openreview.net/forum?id=h34BJbxwoY · 546.1 · oui, mesuré · page ou résumé
- Same Algorithms, Different Scientist: Design Space Bias in AI Discovery (2026-08-29) — https://openreview.net/forum?id=zrObNoC4GY · 549.0 · oui, mesuré · page ou résumé
- The Placebo Improvement: Stress-Testing False Claims by Autonomous Research Agents (2026-08-30) — https://openreview.net/forum?id=NymGpli1U1 · 552.0 · oui, mesuré · page ou résumé
- PermuLoop: Causal Evidence That LLM Discovery Agents Use Experimental Feedback (2026-09-27) — https://openreview.net/forum?id=EopwVp2E1m · 555.0 · oui, mesuré · page ou résumé
- AUDIT: Validating LLM Judges Through Controlled Error Injection (2026-08-27) — https://openreview.net/forum?id=fpeLFP6JEE · 558.1 · oui, mesuré · page ou résumé
- Harness-Delta Attribution: Dissecting Gains From Harness Evolution (2026-10-15) — https://arxiv.org/abs/2610.22466 · 586.0 · oui, affirmé · page ou résumé
- How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks (2026-06-15) — https://arxiv.org/abs/2606.20695 · 589.0 · oui, affirmé · page ou résumé
- The Limits of Inference Scaling Through Resampling (2024-11-26) — https://arxiv.org/abs/2411.17501 · 592.0 · oui, affirmé · page ou résumé
- Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models (2026-09-26) — https://arxiv.org/abs/2609.35875 · 612.1 · oui, affirmé · page ou résumé

**épreuve n° 8 — Multiplicité et garanties statistiques : correction de Holm, e-valeurs, validité à tout instant, taux de fausses découvertes**

13 mécanismes, 13 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, oui, affirmé 3, inconnu 4. Lecture : page ou résumé 12, notice seule 1.

- The Implementation Lottery: Auditing Idea Reliability in Automated Research (2026-07-29) — https://arxiv.org/abs/2607.26587 · 85.2 · oui, mesuré · page ou résumé
- Open-ended Scientific Discovery with Possibilistic Reasoning (2026-10-08) — https://arxiv.org/abs/2610.11289 · 174.0 · oui, mesuré · page ou résumé
- Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing (2026-08-07) — https://arxiv.org/abs/2608.07437 · 207.0 · oui, affirmé · page ou résumé
- Finite Resources False Discovery Rate Control in Structured Hypothesis Spaces (2026-06-13) — https://arxiv.org/abs/2606.15393 · 210.0 · inconnu · page ou résumé
- Automated Hypothesis Validation with Agentic Sequential Falsifications (2025-02-14) — https://arxiv.org/abs/2502.09858 · 247.0 · oui, mesuré · page ou résumé
- AI-Powered (Finance) Scholarship (2024-12) — https://www.nber.org/papers/w33363 · 394.1 · oui, affirmé · page ou résumé
- E-valuator: Reliable Agent Verifiers with Sequential Hypothesis Testing (2025-12-02) — https://arxiv.org/abs/2512.03109 · 427.0 · inconnu · notice seule
- Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors (2026-09-22) — https://arxiv.org/abs/2609.27051 · 441.1 · oui, affirmé · page ou résumé · machine
- Replay the Scientist: Calibrated Evidence After Interactive LLM Hypothesis Search (2026-09-19) — https://openreview.net/forum?id=NPn5klkDyV · 511.0 · oui, mesuré · page ou résumé
- When Statistical Discoveries Become State: Reliability in Continual Research Agents (2026-09-18) — https://openreview.net/forum?id=IflcbZNgHy · 512.1 · oui, mesuré · page ou résumé
- NxN E-valuation: Hypothesis Certification via a Conformal CRT Null (2026-08-06) — https://arxiv.org/abs/2608.06621 · 575.0 · inconnu · page ou résumé
- PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents (2026-06-06) — https://arxiv.org/abs/2606.08106 · 576.1 · inconnu · page ou résumé · machine
- Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing (SSRN 6569258 ; lu sur la copie de conférence) (2026-04) — https://skbi.smu.edu.sg/sites/skbi.smu.edu.sg/files/2026-06/Day1_0915_Danqing%20Mei%20(paper).pdf · 623.1 · oui, mesuré · page ou résumé

**épreuve n° 9 — Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes**

20 mécanismes, 20 travaux (4 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 13, oui, affirmé 2, non 1, inconnu 4. Lecture : lecture approfondie 1, page ou résumé 19.

- Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty (2026-06-23) — https://arxiv.org/abs/2606.25198 · 32.1 · oui, mesuré · page ou résumé
- Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents (2026-09-07) — https://arxiv.org/abs/2609.09219 · 73.0 · oui, mesuré · page ou résumé
- When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents (2026-11-10) — https://arxiv.org/abs/2611.14326 · 97.1 · inconnu · page ou résumé
- YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents (2026-10-01) — https://arxiv.org/abs/2610.01097 · 107.1 · oui, mesuré · page ou résumé · machine
- Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents (2026-07-10) — https://arxiv.org/abs/2607.09195 · 119.1 · inconnu · page ou résumé
- Open-Endedness Bench: Measuring Epistemic Process from Agent Records (2026-09-14) — https://arxiv.org/abs/2610.02588 · 180.1 · oui, mesuré · page ou résumé
- StatefulDiscovery: Evidence-Calibrated Claim Formation in Open-Ended Scientific Discovery (2026-06-10) — https://arxiv.org/abs/2606.11851 · 211.1 · oui, mesuré · page ou résumé
- When Should an AI Scientist Stop? Verifiable Experiment Steering and Refusal for Autonomous Discovery (2026-05-26) — https://arxiv.org/abs/2606.07576 · 212.0 · oui, mesuré · page ou résumé
- The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems (2025-09-10) — https://arxiv.org/abs/2509.08713 · 217.0 · oui, mesuré · page ou résumé
- How Far Are We From True Auto-Research? (2026-05-18) — https://arxiv.org/abs/2605.19156 · 227.1 · oui, mesuré · page ou résumé
- AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration (2026-03-15) — https://arxiv.org/abs/2605.20025 · 279.1 · inconnu · page ou résumé · machine
- An AI Scientist that Doesn't Drift: Taste, Structure, and Falsifiable Findings in a Quadruped Navigation Research Loop (2026-07-30) — https://arxiv.org/abs/2608.07542 · 332.1 · oui, affirmé · page ou résumé · machine
- ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch (2026-09-18) — https://arxiv.org/abs/2610.18088 · 421.0 · oui, mesuré · page ou résumé
- r2m-ai/scholar-loop (2026-06-15) — https://github.com/r2m-ai/scholar-loop · 491.0 · inconnu · page ou résumé · machine
- appleweiping/WEIPING_LAB (2026-05-24) — https://github.com/appleweiping/WEIPING_LAB · 495.1 · non · page ou résumé
- AIS-Bench: An AI Scientist Benchmark for Autonomous Scientific Discovery (2026-09-18) — https://openreview.net/forum?id=RT78MFtfKQ · 521.0 · oui, mesuré · page ou résumé
- Epistemic Control for Open-world AI Scientists (2026-09-01) — https://openreview.net/forum?id=dzf2UKinnX · 534.0 · oui, mesuré · page ou résumé
- Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists (2026-09-25) — https://openreview.net/forum?id=KqWQxzp9Xn · 553.0 · oui, mesuré · page ou résumé
- AutoResearchArena: A Comprehensive Evaluation of AI-Driven Research Across Ideation, Experimentation, and Writing (2026-10-12) — https://openreview.net/forum?id=5WpKsBuzpI · 568.1 · oui, affirmé · page ou résumé
- LLM Evolutionary Search Strategies Should be Compared by Tokens (2026-10-13) — https://arxiv.org/abs/2610.23977 · 581.3 · oui, mesuré · lecture approfondie

**épreuve n° 10 — Dispersion, reproductibilité et variabilité des analyses ou des runs menés par des agents**

7 mécanismes, 7 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, inconnu 2. Lecture : page ou résumé 6, notice seule 1.

- Automated Discovery Has No Universally Superior Harness (2026-07-20) — https://arxiv.org/abs/2607.18235 · 27.1 · oui, mesuré · page ou résumé
- Letting AI Formulate the Research Question: Autonomous Research Agents (2026-10-29) — https://arxiv.org/abs/2610.39620 · 145.2 · oui, mesuré · page ou résumé
- Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development (2026-08-13) — https://arxiv.org/abs/2608.13417 · 186.1 · inconnu · page ou résumé
- AI "errors" (2026) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6408138 · 428.0 · inconnu · notice seule
- Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse (2026-02-21) — https://arxiv.org/abs/2602.18710 · 430.0 · oui, mesuré · page ou résumé
- Nonstandard Errors in AI Agents (2026-03-17) — https://arxiv.org/abs/2603.16744 · 431.0 · oui, mesuré · page ou résumé
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) — https://metr.org/blog/2026-07-21-expenditure-horizon/ · 464.2 · oui, mesuré · page ou résumé

**épreuve n° 11 — Évaluation sans fuite et consciente du nombre d'essais ; rendement rapporté contre rendement réel**

5 mécanismes, 5 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, inconnu 2. Lecture : lecture approfondie 1, page ou résumé 4.

- From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? (2026-09-18) — https://arxiv.org/abs/2611.05108 · 98.4 · inconnu · lecture approfondie
- The Alpha Illusion: Reported Alpha from LLM Trading Agents Should Not Be Treated as Deployment Evidence (2026-05-16) — https://arxiv.org/abs/2605.16895 · 435.0 · oui, mesuré · page ou résumé
- What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery (2026-08-27) — https://arxiv.org/abs/2608.27734 · 439.0 · oui, mesuré · page ou résumé
- Agentic Empirical Asset Pricing: Methodological Foundations (2026-09-01) — https://arxiv.org/abs/2609.00731 · 440.0 · inconnu · page ou résumé
- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) — https://openreview.net/forum?id=Ur08wiPVM3 · 502.1 · oui, mesuré · page ou résumé

**épreuve n° 12 — Réfutabilité, prédiction avant exécution et effet attendu : prévoir puis observer, séparer conception et exécution**

8 mécanismes, 7 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, inconnu 1. Lecture : page ou résumé 7.

- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment (2026-10-29) — https://arxiv.org/abs/2610.40488 · 58.0 · oui, mesuré · page ou résumé
- Language Models as AI Research World Models (2026-10-08) — https://arxiv.org/abs/2610.12235 · 64.0 · oui, mesuré · page ou résumé
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (2026-10-05) — https://arxiv.org/abs/2610.06824 · 67.0 · oui, mesuré · page ou résumé
- What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation (2026-08-24) — https://arxiv.org/abs/2608.22948 · 78.0 · oui, mesuré · page ou résumé
- Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure (2026-06-17) — https://arxiv.org/abs/2608.20361 · 155.2 · inconnu · page ou résumé
- Do Research Agents Improve for the Right Reasons? (2026-09-19) — https://openreview.net/forum?id=V1RpRHq5O8 · 506.0, 506.1 · oui, mesuré · page ou résumé
- EffectPreconception: Guiding ML Research Agents through Effect Prediction and Observation (2026-09-14) — https://openreview.net/forum?id=lUYmgIJixT · 516.0 · oui, mesuré · page ou résumé

**épreuve n° 13 — Environnements et bancs interactifs de découverte (lois, causalité, mécanismes, composants isolés)**

6 mécanismes, 6 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, inconnu 4. Lecture : page ou résumé 6.

- Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments (2026-10-19) — https://arxiv.org/abs/2610.25747 · 169.0 · inconnu · page ou résumé
- Causal Discovery Bench: Can LLMs Autonomously Conduct Effective Experiments? (2026-10-13) — https://arxiv.org/abs/2611.09934 · 172.0 · oui, mesuré · page ou résumé
- ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure (2026-05-28) — https://arxiv.org/abs/2605.30284 · 192.0 · inconnu · page ou résumé
- CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists (2026-05-25) — https://arxiv.org/abs/2605.26029 · 194.0 · inconnu · page ou résumé
- DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (2024-06-10) — https://arxiv.org/abs/2406.06769 · 200.0 · inconnu · page ou résumé
- CreativeBench2.0: Benchmarking Creative Method Discovery and Foresight Toward Recursive Self-Improvement (2026-09-15) — https://openreview.net/forum?id=l9Zt4H8wXT · 544.0 · oui, mesuré · page ou résumé

**épreuve n° 14 — Positions, constats et synthèses sur l'épreuve**

13 mécanismes, 13 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, non 9, inconnu 1. Lecture : page ou résumé 13.

- Large Language Models Extend Known Research But Do Not Create New Research Directions (2026-10-12) — https://arxiv.org/abs/2610.17439 · 11.2 · non · page ou résumé
- Workflow Closure Is Not Scientific Closure in Auto-Research Systems (2026-05-25) — https://arxiv.org/abs/2605.26200 · 213.0 · non · page ou résumé
- Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap (2026-06-29) — https://arxiv.org/abs/2608.05179 · 224.0 · non · page ou résumé
- Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts (2026-01-06) — https://arxiv.org/abs/2601.03315 · 230.0 · oui, mesuré · page ou résumé
- Optimal Post-Hoc Theorizing (2025-05-15) — https://arxiv.org/abs/2505.10370 · 426.0 · non · page ou résumé
- Sound Agentic Science Requires Adversarial Experiments (2026-04-23) — https://arxiv.org/abs/2604.22080 · 434.0 · non · page ou résumé
- Takes on Automating Alignment (2026-04-20) — https://www.lesswrong.com/posts/dgXmxkqZcQo5QdTd9/takes-on-automating-alignment · 468.0 · non · page ou résumé
- How I'm thinking about different types of automated alignment (2026-11-11) — https://www.lesswrong.com/posts/NFkj9J2BBLSjNuH5G/how-i-m-thinking-about-different-types-of-automated · 469.0 · non · page ou résumé
- Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research (2026-09-15) — https://openreview.net/forum?id=DK9rlpEHBf · 514.1 · oui, mesuré · page ou résumé
- AI Scientists Need Stronger Verification Framework to Address Systemic Fragility (2026-09-19) — https://openreview.net/forum?id=UAC2KYmvj7 · 527.0 · non · page ou résumé
- Beyond Hypothesis Recovery: Evaluating Scientific Hypothesis Generation through Evidence-Hypothesis Transitions (2026-09-19) — https://openreview.net/forum?id=71lz12sujF · 538.0 · oui, mesuré · page ou résumé
- Position: AI Scientists Are Not Yet Ready for Open-Ended and Fully Autonomous Scientific Discovery (2026-05-26) — https://openreview.net/forum?id=EWbCCYsR9M · 573.0 · inconnu · page ou résumé
- Toward Evaluation Frameworks for Multi-Agent Scientific AI Systems (2026-03-18) — https://arxiv.org/abs/2603.26718 · 620.0 · non · page ou résumé

**épreuve n° 15 — Épreuve décrite sans montage précisé par la notice**

15 mécanismes, 15 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, oui, affirmé 3, inconnu 9. Lecture : page ou résumé 14, notice seule 1.

- Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures (2026-10-29) — https://arxiv.org/abs/2610.40382 · 163.1 · inconnu · page ou résumé
- Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench (2026-10-13) — https://arxiv.org/abs/2610.18938 · 170.2 · inconnu · page ou résumé
- Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery (2026-10-13) — https://arxiv.org/abs/2610.18449 · 171.1 · oui, mesuré · page ou résumé
- Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space (2026-10-06) — https://arxiv.org/abs/2610.07627 · 177.1 · inconnu · page ou résumé
- From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists (2026-10-04) — https://arxiv.org/abs/2610.05197 · 179.0 · inconnu · page ou résumé
- MechBench: Can AI Scientific Agents Discover Mechanisms Beyond Phenomenal Laws? (2026-09-28) — https://arxiv.org/abs/2609.35515 · 182.0 · inconnu · page ou résumé
- Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities (2026-08-04) — https://arxiv.org/abs/2608.03569 · 187.1 · oui, affirmé · page ou résumé
- Can AI agents conduct open-ended AI research? Early evidence from two case studies (2026-07-29) — https://arxiv.org/abs/2607.27191 · 188.0 · oui, mesuré · page ou résumé
- Accelerating Scientific Research with Gemini in the Real-World (2026-08-27) — https://arxiv.org/abs/2608.26701 · 220.0 · inconnu · page ou résumé
- FARS: A Fully Automated Research System Deployed at Scale (2026-06-30) — https://arxiv.org/abs/2606.31651 · 223.0 · oui, mesuré · page ou résumé
- Accelerating scientific discovery with Co-Scientist (2025-02-26) — https://arxiv.org/abs/2502.18864 · 245.3 · inconnu · page ou résumé · machine
- Autonomous Scientific Discovery via Iterative Meta-Reflection (2026-07-01) — https://arxiv.org/abs/2607.01131 · 303.1 · oui, affirmé · page ou résumé
- RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving (2026-11-11) — https://arxiv.org/abs/2611.14949 · 391.0 · inconnu · notice seule
- Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training (2026-09-22) — https://arxiv.org/abs/2609.25510 · 583.2 · oui, affirmé · page ou résumé
- From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining (2026-09-28) — https://arxiv.org/abs/2609.35559 · 590.1 · inconnu · page ou résumé

### Famille « jugement »

**jugement n° 1 — Goût de recherche et préférences d'experts : choix forcé ou comparaisons par paires contre des experts, des chercheurs, des auteurs ou des pairs**

22 mécanismes, 20 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 21, non 1. Lecture : page ou résumé 19, notice seule 1.

- Contemporary AI lacks the imagination to diverge or negate in science (2026-06-06) — https://arxiv.org/abs/2606.08251 · 36.0 · oui, mesuré · page ou résumé
- Eliciting Research Taste in LLMs through Future Research Direction Choice (2026-06-29) — https://arxiv.org/abs/2611.19794 · 51.0, 51.1 · oui, mesuré · page ou résumé
- What makes a theorem interesting? Operationalizing interestingness for open-ended exploration (2026-11-02) — https://arxiv.org/abs/2611.02905 · 55.0 · oui, mesuré · page ou résumé
- AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment (2026-09-18) — https://arxiv.org/abs/2610.33644 · 60.0 · oui, mesuré · page ou résumé
- Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents (2026-10-12) — https://arxiv.org/abs/2610.21082 · 62.0 · oui, mesuré · page ou résumé
- Learning Individual Scientific Taste with Privileged Hindsight Distillation (2026-10-14) — https://arxiv.org/abs/2610.19719 · 63.0 · oui, mesuré · page ou résumé
- Ideation Arena: Evaluating LLM Generated Research Ideas with Battle-style Human Expert Assessment (2026-08-30) — https://arxiv.org/abs/2608.29696 · 76.0 · oui, mesuré · page ou résumé
- LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation (2026-08-13) — https://arxiv.org/abs/2608.13136 · 82.0 · oui, mesuré · page ou résumé
- SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones? (2026-05-28) — https://arxiv.org/abs/2605.30329 · 88.0 · oui, mesuré · page ou résumé
- Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas (2026-03-11) — https://arxiv.org/abs/2603.10303 · 94.0 · oui, mesuré · page ou résumé
- Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024-09-06) — https://arxiv.org/abs/2409.04109 · 253.0 · oui, mesuré · page ou résumé
- TASTE: Can AI Models Judge AI Safety Research Proposals? (2026-08-28) — https://alignment.anthropic.com/2026/taste/ · 258.0, 258.1 · oui, mesuré · page ou résumé
- LLMs are below chance on TASTE once a shortcut is removed (2026-11-15) — https://www.lesswrong.com/posts/tpKE33scJGzqYKEBW/llms-are-weirdly-below-chance-on-taste-without-a-shortcut · 260.0 · oui, mesuré · page ou résumé
- TastyBench: Toward Measuring Research Taste in LLM (dépôt parviam/tastybench) (2025-12-02) — https://www.lesswrong.com/posts/Mxsy7wYvsCRv5dGrw/llms-don-t-have-superhuman-research-taste-tastybench · 262.0 · oui, mesuré · page ou résumé
- AI Can Learn Scientific Taste (2026-03-15) — https://arxiv.org/abs/2603.14473 · 412.0 · oui, mesuré · page ou résumé
- The Scientific Research Taste Benchmark (SciTaste-Bench): A Multi-Disciplinary Benchmark for Assessing Large Language Models' Judgment of Research Taste in Scientific Papers (2026-10-09) — https://arxiv.org/abs/2610.28653 · 420.0 · oui, mesuré · page ou résumé
- Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI? (2026-11-09) — https://arxiv.org/abs/2611.12429 · 424.0 · oui, mesuré · page ou résumé
- My Research Process: Understanding and Cultivating Research Taste (2025) — https://www.lesswrong.com/s/2owK4Wra9acMaDyBo/p/r2yTwkGt3kbQG2mXi · 476.0 · non · notice seule
- Do AI Agents Have Research Taste? SENSE-Bench for Anomaly-Driven Scientific Exploration (2026-09-16) — https://openreview.net/forum?id=IvMOtnkFXk · 504.1 · oui, mesuré · page ou résumé
- ConjectureLineage: Learning Mathematical Taste from Documented Follow-Up (2026-09-07) — https://openreview.net/forum?id=lBoeKHuibU · 559.0 · oui, mesuré · page ou résumé

**jugement n° 2 — Juge confronté à une vérité différée ou à l'issue réelle : citations, temps écoulé, exécution, impact**

11 mécanismes, 10 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 1, inconnu 3. Lecture : page ou résumé 10.

- HindSight: Evaluating LLM-Generated Research Ideas via Future Impact (2026-03-16) — https://arxiv.org/abs/2603.15164 · 93.1 · inconnu · page ou résumé
- Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments (2026-01-12) — https://arxiv.org/abs/2601.07606 · 95.0 · inconnu · page ou résumé
- Predicting Empirical AI Research Outcomes with Language Models (2025-06-01) — https://arxiv.org/abs/2506.00794 · 96.0 · inconnu · page ou résumé
- The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas (2025-06-25) — https://arxiv.org/abs/2506.20803 · 238.1 · oui, mesuré · page ou résumé
- PaperScorer: How Predictable Is Paper Acceptance? (2026-10-22) — https://arxiv.org/abs/2610.31791 · 422.0 · oui, mesuré · page ou résumé
- When AI builds itself (2026-09-18) — https://www.anthropic.com/institute/recursive-self-improvement · 461.0 · oui, mesuré · page ou résumé
- Do LLMs Have Research Taste? An Analysis Using BóLèBench (2026-09-12) — https://openreview.net/forum?id=vSABCIC1OM · 500.0, 500.1 · oui, mesuré · page ou résumé
- IdeaReward: Benchmarking and Training Reward Models for Research Idea Generation (2026-09-19) — https://openreview.net/forum?id=KL3GMYps6X · 505.1 · oui, mesuré · page ou résumé
- CreativeBench2.0: Benchmarking Creative Method Discovery and Foresight Toward Recursive Self-Improvement (2026-09-15) — https://openreview.net/forum?id=l9Zt4H8wXT · 544.1 · oui, mesuré · page ou résumé
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) — https://openreview.net/forum?id=KufsJAHeGn · 572.2 · oui, affirmé · page ou résumé

**jugement n° 3 — Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle**

19 mécanismes, 19 travaux (6 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, oui, affirmé 5, non 5, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 16, notice seule 2.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.5 · oui, affirmé · page ou résumé · machine
- Read, Grep, and Synthesize: Diagnosing Cross-Domain Seed Exposure for LLM Research Ideation (2026-05-12) — https://arxiv.org/abs/2605.11532 · 44.1 · oui, mesuré · page ou résumé
- Auditing AI peer reviewers: a benchmark on real scientific papers (2026-11-12) — https://arxiv.org/abs/2611.17052 · 52.1 · oui, mesuré · page ou résumé
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.5 · oui, affirmé · page ou résumé
- TIGER: Learning from Researcher Taste to Generate Tailored Research Ideas (2026-09-17) — https://arxiv.org/abs/2611.02234 · 56.1 · non · page ou résumé
- Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies (2026-08-17) — https://arxiv.org/abs/2608.16645 · 80.2 · oui, mesuré · page ou résumé
- Distill, Debate, Discover: Grounding Multi-Agent Research Ideation in Graph-Distilled Insights (2026-10-23) — https://arxiv.org/abs/2610.33366 · 128.1 · non · page ou résumé · machine
- EvoSci: A Bio-Inspired Multi-Agent Framework for the Evolution of Scientific Discovery (2026-05-20) — https://arxiv.org/abs/2605.24018 · 140.1 · non · page ou résumé
- Can LLMs Uncover Hidden Physical Laws through Free Exploration? (2026-10-27) — https://arxiv.org/abs/2610.37649 · 164.2 · inconnu · page ou résumé
- The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (2025-04-08) — https://arxiv.org/abs/2504.08066 · 241.3 · inconnu · page ou résumé · machine
- Accelerating scientific discovery with Co-Scientist (2025-02-26) — https://arxiv.org/abs/2502.18864 · 245.1 · oui, affirmé · page ou résumé · machine
- Evaluating LLMs' Divergent Thinking Capabilities for Scientific Idea Generation with Minimal Context (2024-12-23) — https://arxiv.org/abs/2412.17596 · 248.1 · non · page ou résumé
- The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (2024-08-12) — https://arxiv.org/abs/2408.06292 · 254.2 · oui, affirmé · page ou résumé · machine
- The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery (2026-10-13) — https://arxiv.org/abs/2610.18933 · 375.2 · oui, mesuré · page ou résumé
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.5 · oui, mesuré · lecture approfondie
- NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment (2026-04-13) — https://arxiv.org/abs/2604.11543 · 459.1 · inconnu · notice seule
- How models explore ideas (2026-11-10) — https://bespokelabs.ai/blog/how-models-explore-ideas · 462.1 · oui, affirmé · page ou résumé
- LLM Daydreaming (2025-07) — https://gwern.net/ai-daydreaming · 472.1 · non · notice seule
- CoI‑Pro: Scientific Idea Generation via Retrieval over Research Trajectories (2026-09-17) — https://openreview.net/forum?id=MtTWQDzv0e · 529.1 · oui, mesuré · page ou résumé · machine

**jugement n° 4 — Instabilité du juge : cadrage, version, panel, probabilité déclarée, biais de faveur**

11 mécanismes, 10 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 11. Lecture : lecture approfondie 2, page ou résumé 8.

- Auditing Pairwise Equivalence Judgments: Self-Critique Effects and Diversity Measurement in Multi-Agent Hypothesis Generation (2026-09-14) — https://arxiv.org/abs/2610.04133 · 14.0 · oui, mesuré · page ou résumé
- Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation (2026-10-01) — https://arxiv.org/abs/2610.02022 · 68.1 · oui, mesuré · page ou résumé
- Think-Probe-Respond: Improving Large Language Models as Judges of Research Idea Novelty (2026-08-26) — https://arxiv.org/abs/2608.25660 · 77.0 · oui, mesuré · page ou résumé
- On the Limits of LLM-as-Judge for Scientific Novelty Assessment (2026-06-10) — https://arxiv.org/abs/2606.12071 · 86.0 · oui, mesuré · page ou résumé
- Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch (2026-07-30) — https://arxiv.org/abs/2607.27687 · 117.1 · oui, mesuré · page ou résumé
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.5 · oui, mesuré · lecture approfondie · machine
- LLM-as-a-Judge Version Shift: The Instrument Changed, Not the Standard (2026-09-07) — https://arxiv.org/abs/2610.32986 · 416.0 · oui, mesuré · page ou résumé
- Same Papers, Different Verdicts: Tracing Version Drift in LLM Peer Review (2026-11-16) — https://arxiv.org/abs/2611.20608 · 425.0 · oui, mesuré · page ou résumé
- Evaluating LLM Research Agents as Tests of Return Predictability (2026-11-02) — https://arxiv.org/abs/2611.04070 · 450.2, 450.7 · oui, mesuré · lecture approfondie
- Agreement With Humans Is Not a Property of the Judge (2026-08-30) — https://openreview.net/forum?id=QmrmObszBY · 557.0 · oui, mesuré · page ou résumé

**jugement n° 5 — Validation et tests de sensibilité d'un juge : erreurs plantées, accord insuffisant, protocole, témoins**

9 mécanismes, 9 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 9. Lecture : page ou résumé 9.

- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) — https://openreview.net/forum?id=Ur08wiPVM3 · 502.3 · oui, mesuré · page ou résumé
- Approval Is Not Discovery: When Can a Model of the Scientist Steer a Discovery Agent? (2026-09-27) — https://openreview.net/forum?id=h34BJbxwoY · 546.0 · oui, mesuré · page ou résumé
- Recombination or Discovery? A Retrieval-Grounded Novelty Audit of Machine-Generated Research Papers (2026-07-30) — https://openreview.net/forum?id=Ew2phMa9Ou · 547.1 · oui, mesuré · page ou résumé
- The Placebo Improvement: Stress-Testing False Claims by Autonomous Research Agents (2026-08-30) — https://openreview.net/forum?id=NymGpli1U1 · 552.1 · oui, mesuré · page ou résumé
- Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists (2026-09-25) — https://openreview.net/forum?id=KqWQxzp9Xn · 553.1 · oui, mesuré · page ou résumé
- PermuLoop: Causal Evidence That LLM Discovery Agents Use Experimental Feedback (2026-09-27) — https://openreview.net/forum?id=EopwVp2E1m · 555.1 · oui, mesuré · page ou résumé
- AUDIT: Validating LLM Judges Through Controlled Error Injection (2026-08-27) — https://openreview.net/forum?id=fpeLFP6JEE · 558.0 · oui, mesuré · page ou résumé
- When Correction Memory Fails: Episodic Retrieval Is Not Test-Time Learning for Pairwise Judges (2026-08-27) — https://openreview.net/forum?id=d7EYjlyvpg · 560.1 · oui, mesuré · page ou résumé
- The Grade Says Little, the Score Orders: AI Reviewer Panels Against a Venue's Ratings and Decisions (2026-09-06) — https://openreview.net/forum?id=ZdyUuxGxJ5 · 561.0 · oui, mesuré · page ou résumé

**jugement n° 6 — Corrélation des erreurs, monoculture et nombre de votes effectifs d'un collège de juges**

9 mécanismes, 7 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4, oui, affirmé 2, non 3. Lecture : page ou résumé 6, notice seule 1.

- We need more decorrelated evidence (2026-11-12) — https://www.lesswrong.com/posts/EuhQ5fnGR4tAQTTgd/we-need-more-decorrelated-evidence · 465.0 · non · page ou résumé
- Automated Alignment is Harder Than You Think (arXiv 2605.06390 ; repris sur LessWrong) (2026-05-07) — https://arxiv.org/abs/2605.06390 · 470.0 · non · notice seule
- Homogenization in Multi-Agent Systems (2026-09-18) — https://openreview.net/forum?id=giMpNTtGsL · 507.2 · oui, mesuré · page ou résumé
- Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels (2026-08-28) — https://openreview.net/forum?id=g3CgpBqz2y · 556.0 · oui, mesuré · page ou résumé
- LLM Reviewers Err Together: Shared Blind Spots and Correlated Judgments in Peer Review (2026-08-28) — https://openreview.net/forum?id=EW1CD8Z0IV · 564.0, 564.1 · oui, mesuré · page ou résumé
- Do AI Reviewers Converge? Diversity Collapse in Model-Generated Peer Review (2026-03-16) — https://openreview.net/forum?id=NdDKcU9HlU · 570.0, 570.1 · oui, affirmé · page ou résumé
- Against Homogeneous Consensus: Why Scientific Discovery Requires Heterogeneous Adversarial LLM Agents (2026-03-16) — https://openreview.net/forum?id=Vm1U9Sh4wV · 571.1 · non · page ou résumé

**jugement n° 7 — Juge ou vérificateur entraîné à cette fin : modèle de récompense, petit critique, grille intériorisée, signal différé**

6 mécanismes, 6 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, inconnu 1. Lecture : page ou résumé 6.

- Verify Less, Evolve More: Training Idea-Level Critics for Verification-Efficient ML Evolving Agents (2026-09-18) — https://arxiv.org/abs/2610.08993 · 66.2 · oui, mesuré · page ou résumé
- Teaching Language Models to Forecast Research Success Through Comparative Idea Evaluation (2026-03-20) — https://arxiv.org/abs/2605.21491 · 92.0 · inconnu · page ou résumé
- Learning to Ideate for Scientific Impact (2026-05-14) — https://arxiv.org/abs/2609.29802 · 151.1 · oui, mesuré · page ou résumé
- IdeaReward: Benchmarking and Training Reward Models for Research Idea Generation (2026-09-19) — https://openreview.net/forum?id=KL3GMYps6X · 505.0 · oui, mesuré · page ou résumé
- Small Critics Make Strong Models Count: Learning to Verify Stronger Models for Efficient AutoResearch (2026-09-19) — https://openreview.net/forum?id=oYzABaBXFN · 518.0 · oui, mesuré · page ou résumé
- Internalizing Rubric Guidance for Research Agents (2026-09-17) — https://openreview.net/forum?id=dRjFFUs2oU · 536.0 · oui, mesuré · page ou résumé

**jugement n° 8 — Séparation de qui propose, qui exécute et qui juge ; arbitre ou règle de décision fixés hors de l'agent**

8 mécanismes, 8 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 2, inconnu 1. Lecture : lecture approfondie 1, page ou résumé 7.

- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment (2026-10-29) — https://arxiv.org/abs/2610.40488 · 58.2 · oui, mesuré · page ou résumé
- What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation (2026-08-24) — https://arxiv.org/abs/2608.22948 · 78.1 · oui, mesuré · page ou résumé
- Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research (2026-10-18) — https://arxiv.org/abs/2610.24944 · 102.2 · inconnu · page ou résumé · machine
- AIM: Agentic Idea Management for Automated Research (2026-09-16) — https://arxiv.org/abs/2609.38445 · 110.3 · oui, mesuré · page ou résumé · machine
- Letting AI Formulate the Research Question: Autonomous Research Agents (2026-10-29) — https://arxiv.org/abs/2610.39620 · 145.1 · oui, mesuré · page ou résumé
- Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling (2026-10-26) — https://arxiv.org/abs/2610.35866 · 167.1 · oui, mesuré · page ou résumé
- Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors (2026-09-22) — https://arxiv.org/abs/2609.27051 · 441.0 · oui, affirmé · page ou résumé · machine
- Evaluating LLM Research Agents as Tests of Return Predictability (2026-11-02) — https://arxiv.org/abs/2611.04070 · 450.3 · oui, affirmé · lecture approfondie

**jugement n° 9 — Jugement ancré dans des preuves traçables, des journaux ou un audit des artefacts plutôt que dans un avis libre**

10 mécanismes, 10 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 8, oui, affirmé 2. Lecture : page ou résumé 10.

- Open-Endedness Bench: Measuring Epistemic Process from Agent Records (2026-09-14) — https://arxiv.org/abs/2610.02588 · 180.0 · oui, mesuré · page ou résumé
- TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents (2026-09-04) — https://arxiv.org/abs/2609.05079 · 183.1 · oui, mesuré · page ou résumé
- DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking (2026-05-25) — https://arxiv.org/abs/2605.26087 · 193.2 · oui, affirmé · page ou résumé
- FIRE-Bench: Evaluating AI Agents on the Rediscovery of Scientific Insights (2026-02-02) — https://arxiv.org/abs/2602.02905 · 195.1 · oui, mesuré · page ou résumé
- The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems (2025-09-10) — https://arxiv.org/abs/2509.08713 · 217.1 · oui, mesuré · page ou résumé
- How Far Are We From True Auto-Research? (2026-05-18) — https://arxiv.org/abs/2605.19156 · 227.0 · oui, mesuré · page ou résumé
- prometheus-eval/into-the-unknown (arXiv 2610.19159) (2026-09-24) — https://arxiv.org/abs/2610.19159 · 490.1 · oui, mesuré · page ou résumé
- Do Research Agents Improve for the Right Reasons? (2026-09-19) — https://openreview.net/forum?id=V1RpRHq5O8 · 506.2 · oui, mesuré · page ou résumé
- From Black-Box Judgments to Auditable Graphs: Structured Idea Generation and Evaluation via Scientific Knowledge Graphs (2026-08-22) — https://openreview.net/forum?id=ZmCMvyomhA · 530.0 · oui, mesuré · page ou résumé
- IdeaGraph: Evidence-Bearing Synergy Junctions for Cross-Field Scientific Ideation (2026-08-27) — https://openreview.net/forum?id=92DdZnwXPh · 550.1 · oui, affirmé · page ou résumé · machine

**jugement n° 10 — Humain dans la boucle : validation, correction, classement par des experts ou un mainteneur**

6 mécanismes, 6 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 2, non 2, inconnu 1. Lecture : page ou résumé 5, notice seule 1.

- Can AI agents conduct open-ended AI research? Early evidence from two case studies (2026-07-29) — https://arxiv.org/abs/2607.27191 · 188.1 · oui, mesuré · page ou résumé
- AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration (2026-03-15) — https://arxiv.org/abs/2605.20025 · 279.2 · inconnu · page ou résumé · machine
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) — https://metr.org/blog/2026-07-21-expenditure-horizon/ · 464.3 · oui, affirmé · page ou résumé
- Human-Guided Agentic Research: A Research Agenda (2026-06-29) — https://www.lesswrong.com/posts/8KrTuCAzL2fdYHNrv/human-guided-agentic-research-a-research-agenda · 467.0 · non · page ou résumé
- How we built Kosmos (et Kosmos, arXiv 2511.02824) (2025-11) — https://arxiv.org/abs/2511.02824 · 482.1 · oui, affirmé · notice seule · machine
- CL-ML/open-collider (2026-05-10) — https://github.com/CL-ML/open-collider · 488.3 · non · page ou résumé · machine

**jugement n° 11 — Audit d'intégrité et de fausse nouveauté des articles produits par des agents**

4 mécanismes, 4 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, inconnu 1. Lecture : page ou résumé 4.

- SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems (2026-05-11) — https://arxiv.org/abs/2605.10246 · 214.0 · oui, mesuré · page ou résumé
- All That Glitters is Not Novel: Plagiarism in AI Generated Research (2025-02-23) — https://arxiv.org/abs/2502.16487 · 246.1 · oui, mesuré · page ou résumé
- wanshuiyin/Anti-Autoresearch (2026-06-26) — https://github.com/wanshuiyin/Anti-Autoresearch · 496.0 · inconnu · page ou résumé
- Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers (2026-09-17) — https://openreview.net/forum?id=Ln1iZccT04 · 537.0 · oui, mesuré · page ou résumé

**jugement n° 12 — Relecteurs modèles évalués contre les relectures et décisions humaines**

5 mécanismes, 5 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, oui, affirmé 1, inconnu 1. Lecture : page ou résumé 4, notice seule 1.

- How Well Do LLMs Perform in Peer Review? Evidence from Finance and Accounting (2026-10-13) — https://arxiv.org/abs/2610.18435 · 445.0 · inconnu · notice seule
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) — https://github.com/Dawes-Institute/ai-peer-review-benchmark · 489.1 · oui, mesuré · page ou résumé
- The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake (2026-08-29) — https://openreview.net/forum?id=Xo66awQ992 · 548.1 · oui, mesuré · page ou résumé
- Beyond Imitation: Evaluating LLM Reviewers by Impact ? (2026-08-29) — https://openreview.net/forum?id=TiAGTPFXW5 · 562.0 · oui, mesuré · page ou résumé
- AutoResearchArena: A Comprehensive Evaluation of AI-Driven Research Across Ideation, Experimentation, and Writing (2026-10-12) — https://openreview.net/forum?id=5WpKsBuzpI · 568.0 · oui, affirmé · page ou résumé

**jugement n° 13 — Constats et positions sur le jugement (goulot, vérification, objectif donné, origine du goût)**

8 mécanismes, 8 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, oui, affirmé 1, non 5. Lecture : page ou résumé 7, notice seule 1.

- Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game (2026-10-13) — https://arxiv.org/abs/2611.14487 · 1.2 · oui, affirmé · page ou résumé
- Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition (2026-11-03) — https://arxiv.org/abs/2611.04420 · 53.0 · oui, mesuré · page ou résumé
- How Is Automated Research Evaluated? A Survey of Benchmarks and Evaluation Practices (2026-10-08) — https://arxiv.org/abs/2610.11877 · 65.0 · non · page ou résumé
- Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts (2026-06-22) — https://arxiv.org/abs/2606.23175 · 208.0 · non · page ou résumé
- The Ideation Bottleneck: Decomposing the Quality Gap Between AI-Generated and Human Economics Research (2026-04-03) — https://arxiv.org/abs/2604.03338 · 433.0 · oui, mesuré · page ou résumé
- The Verification Bottleneck (2026-11-01) — https://arxiv.org/abs/2611.02265 · 449.0 · non · page ou résumé
- Lessons from building an automated research scaffold (2026-10-02) — https://www.lesswrong.com/posts/zGaQ3SS9C6So9NXFg/lessons-from-building-an-automated-research-scaffold · 466.1 · non · page ou résumé
- AIs can now often do massive easy-to-verify SWE tasks (2026) — https://blog.redwoodresearch.org/p/ais-can-now-often-do-massive-easy · 485.0 · non · notice seule

**jugement n° 14 — Critères de valeur construits autrement qu'un avis de juge : logits, croyance, e-valeurs, agrégation d'objectifs**

6 mécanismes, 6 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 2, inconnu 3. Lecture : page ou résumé 6.

- Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking (2026-08-18) — https://arxiv.org/abs/2608.17270 · 79.0 · oui, mesuré · page ou résumé
- Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another (2026-11-14) — https://arxiv.org/abs/2611.19108 · 161.1 · inconnu · page ou résumé
- Scientific discovery as meta-optimization: a combinatorial optimization case study (2026-06-25) — https://arxiv.org/abs/2606.26728 · 299.1 · oui, affirmé · page ou résumé
- Large Language Bayes Is Not Reparameterisation-Invariant (2026-09-24) — https://arxiv.org/abs/2610.00265 · 442.0 · inconnu · page ou résumé
- Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior (2025-06-03) — https://arxiv.org/abs/2506.03444 · 574.1 · inconnu · page ou résumé
- On the Use of LLM Priors in Multiple Hypothesis Testing with e-Values (2026) — https://neurips.cc/virtual/2026/172148 · 624.0 · oui, affirmé · page ou résumé

**jugement n° 15 — Évaluer l'ensemble produit ou le processus plutôt que l'appariement à une cible unique**

7 mécanismes, 7 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, oui, affirmé 1, inconnu 3. Lecture : page ou résumé 6, notice seule 1.

- More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation (2026-05-07) — https://arxiv.org/abs/2605.06345 · 159.1 · inconnu · page ou résumé
- Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures (2026-10-29) — https://arxiv.org/abs/2610.40382 · 163.0 · inconnu · page ou résumé
- Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation (2026-07-09) — https://arxiv.org/abs/2607.08758 · 309.2 · oui, affirmé · page ou résumé
- FrontierScience: evaluating AI's ability to perform expert-level scientific tasks (arXiv 2601.21165) (2025-12) — https://arxiv.org/abs/2601.21165 · 483.0 · inconnu · notice seule
- IdeaPrism: Beyond Ground-Truth Matching for Hypothesis Evaluation (2026-09-12) — https://openreview.net/forum?id=9YBQu8n3Uk · 522.0 · oui, mesuré · page ou résumé
- IdeaDec: Benchmarking Long-Horizon Scientific Idea Decoding in AI Research Agents (2026-09-18) — https://openreview.net/forum?id=ab0kueYOjm · 523.0 · oui, mesuré · page ou résumé
- MathIdeaBench: A Benchmark For Mathematical Research Idea Generation (2026-08-26) — https://openreview.net/forum?id=yIlEoQe7es · 526.0 · oui, mesuré · page ou résumé

### Famille « mémoire »

**mémoire n° 1 — Oubli et vidage : ne garder que le meilleur survivant, vider l'historique, séparer l'espace de travail de la conversation**

2 mécanismes, 2 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2. Lecture : page ou résumé 2.

- Scaling Discovery Requires Forgetting (2026-10-14) — https://arxiv.org/abs/2610.20563 · 10.0 · oui, mesuré · page ou résumé
- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.1 · oui, mesuré · page ou résumé · machine

**mémoire n° 2 — Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer : îles, lignées, versions**

14 mécanismes, 14 travaux (6 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, oui, affirmé 2, inconnu 5. Lecture : lecture approfondie 3, page ou résumé 11.

- Holistic Diversity Management in LLM-Guided Evolutionary Search (2026-10-28) — https://arxiv.org/abs/2610.38407 · 7.1 · inconnu · page ou résumé
- IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation (2026-07-24) — https://arxiv.org/abs/2607.22375 · 26.1 · oui, mesuré · page ou résumé
- DEI: Diversity in Evolutionary Inference for Quality-Diversity Search (2026-05-26) — https://arxiv.org/abs/2605.27130 · 40.1 · inconnu · page ou résumé
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.3 · oui, mesuré · page ou résumé
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.3 · oui, mesuré · lecture approfondie · machine
- Praxist: From Experimental Artifacts to Solution Lineages (2026-08-26) — https://arxiv.org/abs/2608.25955 · 114.0 · inconnu · page ou résumé
- Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025-05-29) — https://arxiv.org/abs/2505.22954 · 240.1 · inconnu · page ou résumé · machine
- Initialization Improves LLM-Driven Discovery (2026-09-30) — https://arxiv.org/abs/2610.00707 · 406.1 · oui, mesuré · page ou résumé
- Toward Generalist Autonomous Research via Hypothesis-Tree Refinement (2026-06-10) — https://arxiv.org/abs/2606.11926 · 453.1 · oui, affirmé · page ou résumé
- Wright--G\"odel Machine: Mitigating Homogenization in Self-Improving Agents (2026-09-11) — https://openreview.net/forum?id=cQkSamYGQi · 513.1 · oui, mesuré · page ou résumé · machine
- Self-Evolving Agents with Anytime-Valid Certificates (2026-07-01) — https://arxiv.org/abs/2607.00871 · 577.2 · inconnu · page ou résumé · machine
- LLM Evolutionary Search Strategies Should be Compared by Tokens (2026-10-13) — https://arxiv.org/abs/2610.23977 · 581.4 · oui, mesuré · lecture approfondie
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.4 · oui, mesuré · lecture approfondie · machine
- Automated Design of Agentic Systems (2024-08-15) — https://arxiv.org/abs/2408.08435 · 595.1 · oui, affirmé · page ou résumé · machine

**mémoire n° 3 — Trajectoire ou historique de la recherche conservé et lu par le contrôleur ou le proposeur**

8 mécanismes, 8 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, inconnu 1. Lecture : page ou résumé 8.

- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) — https://arxiv.org/abs/2609.00077 · 20.1 · oui, mesuré · page ou résumé
- The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory (2026-11-17) — https://arxiv.org/abs/2611.22661 · 50.1 · oui, mesuré · page ou résumé
- Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research (2026-10-18) — https://arxiv.org/abs/2610.24944 · 102.0 · inconnu · page ou résumé · machine
- Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents (2026-09-17) — https://arxiv.org/abs/2610.02525 · 108.2 · oui, mesuré · page ou résumé
- Learning the ARTS of Search for Automated Discovery (2026-06-20) — https://arxiv.org/abs/2606.21891 · 138.2 · oui, mesuré · page ou résumé
- IdeaTrail: Full-Process Agent Trajectories for Scientific Ideation (2026-07-11) — https://arxiv.org/abs/2607.10144 · 152.0 · oui, mesuré · page ou résumé
- Long-Horizon Autonomous Architecture Research with a Language-Model Agent: A Behavioural Case Study (2026-08-03) — https://arxiv.org/abs/2608.01995 · 402.0 · oui, mesuré · page ou résumé
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (2026-08-28) — https://arxiv.org/abs/2608.28945 · 460.1 · oui, mesuré · page ou résumé

**mémoire n° 4 — État de la recherche tenu hors du modèle : graphe éditable, Git, registre auditable, base épistémologique, agents sans état**

8 mécanismes, 8 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, non 1, inconnu 4. Lecture : page ou résumé 8.

- Agora: Git as Shared Memory for Collective AutoResearch (2026-09-16) — https://arxiv.org/abs/2609.18094 · 113.0 · non · page ou résumé
- XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery (2026-07-14) — https://arxiv.org/abs/2607.12301 · 118.0 · inconnu · page ou résumé · machine
- Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents (2026-07-10) — https://arxiv.org/abs/2607.09195 · 119.0 · inconnu · page ou résumé
- Evolving Idea Graphs with Learnable Edits-and-Commits for Multi-Agent Scientific Ideation (2026-05-06) — https://arxiv.org/abs/2605.04922 · 143.0 · oui, mesuré · page ou résumé
- StatefulDiscovery: Evidence-Calibrated Claim Formation in Open-Ended Scientific Discovery (2026-06-10) — https://arxiv.org/abs/2606.11851 · 211.0 · oui, mesuré · page ou résumé
- mikamikasuki/forest (2026-09-29) — https://github.com/mikamikasuki/forest · 493.0 · inconnu · page ou résumé
- rekursiv-ai/trackinizer (2026-07-22) — https://github.com/rekursiv-ai/trackinizer · 494.0 · inconnu · page ou résumé
- Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research (2026-09-15) — https://openreview.net/forum?id=DK9rlpEHBf · 514.0 · oui, mesuré · page ou résumé

**mémoire n° 5 — Mémoire des échecs et des directions ratées : banque d'échecs, connaissance négative, plans abandonnés**

7 mécanismes, 6 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, inconnu 2. Lecture : page ou résumé 6.

- PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research (2026-09-15) — https://arxiv.org/abs/2609.17846 · 70.2 · oui, mesuré · page ou résumé · machine
- YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents (2026-10-01) — https://arxiv.org/abs/2610.01097 · 107.0 · oui, mesuré · page ou résumé · machine
- Negative Knowledge as Failure-aware Shared Memory for AutoResearch (2026-06-19) — https://arxiv.org/abs/2606.21024 · 122.0 · oui, mesuré · page ou résumé
- SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery (2026-10-20) — https://arxiv.org/abs/2610.28706 · 129.0 · inconnu · page ou résumé
- When Failure Banks Kill Good Ideas: Calibrated Negative Memory for Autonomous Research (2026-09-19) — https://openreview.net/forum?id=eOItnNfHVf · 499.0, 499.1 · oui, mesuré · page ou résumé
- AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation (2026-05-27) — https://arxiv.org/abs/2605.28655 · 611.1 · inconnu · page ou résumé · machine

**mémoire n° 6 — Leçons admises en mémoire seulement après test ou preuve ; garde contre les transferts négatifs**

5 mécanismes, 5 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1, inconnu 3. Lecture : page ou résumé 5.

- When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents (2026-11-10) — https://arxiv.org/abs/2611.14326 · 97.0 · inconnu · page ou résumé
- Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents (2026-10-10) — https://arxiv.org/abs/2610.14683 · 104.1 · oui, affirmé · page ou résumé · machine
- Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery (2026-09-28) — https://arxiv.org/abs/2609.35315 · 111.1 · inconnu · page ou résumé · machine
- Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery (2026-11-16) — https://arxiv.org/abs/2611.21847 · 126.1 · inconnu · page ou résumé · machine
- When Statistical Discoveries Become State: Reliability in Continual Research Agents (2026-09-18) — https://openreview.net/forum?id=IflcbZNgHy · 512.0 · oui, mesuré · page ou résumé

**mémoire n° 7 — Base de connaissances ou banque d'idées partagée entre agents et sessions**

13 mécanismes, 13 travaux (5 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 3, non 1, inconnu 4. Lecture : page ou résumé 12, notice seule 1.

- Toward Knowledge-Centric AI: Discovering, Internalizing, and Using Explicit Knowledge Across Agents and Generations (2026-11-02) — https://arxiv.org/abs/2611.03157 · 99.0 · non · page ou résumé
- Continual Graph Memory and Community Infrastructure for AI-Assisted Mathematical Discovery (2026-09-19) — https://arxiv.org/abs/2610.02945 · 106.0 · oui, mesuré · page ou résumé
- AIM: Agentic Idea Management for Automated Research (2026-09-16) — https://arxiv.org/abs/2609.38445 · 110.2 · oui, mesuré · page ou résumé · machine
- Idea Search: Guiding Tree Search with Ideas to Explore Diverse Scientific Methods (2026-08-09) — https://arxiv.org/abs/2608.08958 · 135.1 · oui, mesuré · page ou résumé · machine
- Graphs of Research: Citation Evolution Graphs as Supervision for Research Idea Generation (2026-05-14) — https://arxiv.org/abs/2605.14790 · 157.1 · inconnu · page ou résumé
- Automated Weak-to-Strong Researcher (2026-04-14) — https://alignment.anthropic.com/2026/automated-w2s-researcher/ · 259.1 · oui, mesuré · page ou résumé · machine
- Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation (2026-07-09) — https://arxiv.org/abs/2607.08758 · 309.0 · oui, affirmé · page ou résumé
- Autoresearch in Mixed-Integer Linear and Nonlinear Programming (2026-09-18) — https://arxiv.org/abs/2609.39360 · 365.1 · oui, affirmé · page ou résumé
- The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery (2026-10-13) — https://arxiv.org/abs/2610.18933 · 375.1 · inconnu · page ou résumé
- CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery (2026-04-02) — https://arxiv.org/abs/2604.01658 · 398.1 · oui, mesuré · page ou résumé · machine
- How we built Kosmos (et Kosmos, arXiv 2511.02824) (2025-11) — https://arxiv.org/abs/2511.02824 · 482.0 · inconnu · notice seule · machine
- REI: Learning Ideation from Repository Evolution (2026-09-14) — https://openreview.net/forum?id=f5f1OtpnyR · 524.1 · inconnu · page ou résumé
- Knowledge-Centric Self-Improvement (2026-07-21) — https://arxiv.org/abs/2607.19592 · 610.0 · oui, affirmé · page ou résumé

**mémoire n° 8 — Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée : méta-réflexion, hiérarchie d'enseignements, modèle de l'expérience**

13 mécanismes, 13 travaux (5 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 4, inconnu 8. Lecture : page ou résumé 13.

- ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery (2026-09-17) — https://arxiv.org/abs/2610.29303 · 101.0 · oui, mesuré · page ou résumé
- Experimental Experience Modeling for Autonomous Research (2026-09-30) — https://arxiv.org/abs/2609.39392 · 109.0 · inconnu · page ou résumé
- $\varepsilon$-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution (2026-08-12) — https://arxiv.org/abs/2608.12522 · 115.0 · inconnu · page ou résumé
- Hyperagents (2026-03-19) — https://arxiv.org/abs/2603.19461 · 125.1 · inconnu · page ou résumé · machine
- Autonomous Scientific Discovery via Iterative Meta-Reflection (2026-07-01) — https://arxiv.org/abs/2607.01131 · 303.0 · oui, affirmé · page ou résumé
- An AI Scientist that Doesn't Drift: Taste, Structure, and Falsifiable Findings in a Quadruped Navigation Research Loop (2026-07-30) — https://arxiv.org/abs/2608.07542 · 332.2 · inconnu · page ou résumé · machine
- Organon : From Evolutionary Search to Recursive Self-Improving Agents for Scientific Discovery (2026-10-17) — https://arxiv.org/abs/2610.33046 · 384.1 · inconnu · page ou résumé · machine
- APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents (2026-05-20) — https://arxiv.org/abs/2605.21240 · 400.0 · inconnu · page ou résumé
- AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle (2026-05-29) — https://arxiv.org/abs/2605.31468 · 452.0 · oui, affirmé · page ou résumé · machine
- SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents (2026-10-01) — https://arxiv.org/abs/2610.02361 · 454.0 · oui, affirmé · page ou résumé
- CaliMem: Search-Efficient Data Agent via Calibrated Memory (2026-10-25) — https://arxiv.org/abs/2610.34500 · 455.0 · oui, affirmé · page ou résumé
- Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining (2026-10-21) — https://arxiv.org/abs/2610.29663 · 616.1 · inconnu · page ou résumé
- MetaEvoForge: Learning to Improve Agents Faster Across Task Environments (2026) — https://neurips.cc/virtual/2026/169839 · 625.1 · inconnu · page ou résumé · machine

**mémoire n° 9 — Issues vérifiées et croyances gardées comme mémoire du sélecteur**

3 mécanismes, 3 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, inconnu 1. Lecture : lecture approfondie 1, page ou résumé 2.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.6 · oui, mesuré · page ou résumé · machine
- BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery (2026-06-29) — https://arxiv.org/abs/2606.30335 · 120.0 · inconnu · page ou résumé · machine
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.2 · oui, mesuré · lecture approfondie · machine

**mémoire n° 10 — Mémoire apprise dans les poids ou par un réflecteur entraîné**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 1, inconnu 1. Lecture : page ou résumé 2.

- Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks (2026-06-27) — https://arxiv.org/abs/2606.29082 · 137.0 · inconnu · page ou résumé
- Training Language Agents to Learn from Experience (2026-05-19) — https://arxiv.org/abs/2605.20477 · 598.0 · oui, affirmé · page ou résumé

**mémoire n° 11 — Mesures de ce que la mémoire ou l'héritage apportent : instance persistante contre remise à zéro, témoins factices, ablations, organisation de la connaissance**

13 mécanismes, 11 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 8, oui, affirmé 2, inconnu 3. Lecture : lecture approfondie 2, page ou résumé 9.

- From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? (2026-09-18) — https://arxiv.org/abs/2611.05108 · 98.0, 98.1 · oui, mesuré · lecture approfondie
- Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery? (2026-10-23) — https://arxiv.org/abs/2610.32046 · 100.0 · oui, mesuré · page ou résumé
- Evaluating Memory Condensation Strategies for Coding Agents in Data-Driven Scientific Discovery (2026-05-13) — https://arxiv.org/abs/2605.18854 · 124.0 · inconnu · page ou résumé
- Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery (2026-07-05) — https://arxiv.org/abs/2607.04108 · 136.4 · oui, mesuré · page ou résumé · machine
- Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development (2026-08-13) — https://arxiv.org/abs/2608.13417 · 186.0 · inconnu · page ou résumé
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.0, 456.6 · oui, mesuré · lecture approfondie
- How Does Knowledge Organization Shape LLM-Based Scientific Ideation (2026-09-19) — https://openreview.net/forum?id=OTp0pTawnX · 525.0 · oui, mesuré · page ou résumé
- When Correction Memory Fails: Episodic Retrieval Is Not Test-Time Learning for Pairwise Judges (2026-08-27) — https://openreview.net/forum?id=d7EYjlyvpg · 560.0 · oui, mesuré · page ou résumé
- Agent Plasticity: Measuring Self-Improvement Through Experience (2026-10-06) — https://arxiv.org/abs/2610.08902 · 600.0 · inconnu · page ou résumé
- Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell (2026-10-06) — https://arxiv.org/abs/2610.07782 · 609.0 · oui, affirmé · page ou résumé
- Can an AI Scientist really discover knowledge? (banc Albert) (2026-06-05) — https://aria.org.uk/insights/can-an-ai-scientist-really-discover-knowledge · 626.1 · oui, affirmé · page ou résumé

**mémoire n° 12 — Dérives de la mémoire d'état : réentrée des trouvailles acceptées, provenance de la trace, liens retenus**

3 mécanismes, 3 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, non 1. Lecture : page ou résumé 2, notice seule 1.

- LLM Daydreaming (2025-07) — https://gwern.net/ai-daydreaming · 472.2 · non · notice seule
- Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry (2026-08-07) — https://openreview.net/forum?id=IZjj0suAJZ · 551.1 · oui, mesuré · page ou résumé
- Search Pathology Diagnosis for Automated Discovery (2026-09-06) — https://openreview.net/forum?id=H9X0A1afdz · 554.0 · oui, mesuré · page ou résumé

**mémoire n° 13 — Positions sur ce que doit être la mémoire d'un agent de recherche**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : non 2. Lecture : page ou résumé 2.

- Evolutionary Intelligence for Scientific Discovery: From Evolutionary Computation to Cumulative Discovery Systems (2026-07-10) — https://arxiv.org/abs/2607.09025 · 222.0 · non · page ou résumé
- Position: Scientific Memory Is Not Chat History: Reframing Long-Term Memory Evaluation for Research Agents (2026-09-19) — https://openreview.net/forum?id=ABOPBAJFiT · 510.0 · non · page ou résumé

### Famille « sélection »

**sélection n° 1 — Acceptation gloutonne à un pas : un seul parent survit, le candidat ne remplace le meilleur que s'il fait mieux**

6 mécanismes, 6 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4, oui, affirmé 2. Lecture : lecture approfondie 2, page ou résumé 4.

- Scaling Discovery Requires Forgetting (2026-10-14) — https://arxiv.org/abs/2610.20563 · 10.2 · oui, mesuré · page ou résumé
- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.2 · oui, mesuré · page ou résumé · machine
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.1 · oui, mesuré · lecture approfondie · machine
- autoresearch (dépôt de code) (2026-03-06) — https://github.com/karpathy/autoresearch · 396.2 · oui, affirmé · page ou résumé · machine
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.1 · oui, mesuré · lecture approfondie
- Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training (2026-09-22) — https://arxiv.org/abs/2609.25510 · 583.1 · oui, affirmé · page ou résumé

**sélection n° 2 — Porte de validation sur une métrique distincte, tenue à l'écart ou privée ; banc de sélection ; régularisation de la sélection**

5 mécanismes, 5 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, non 1, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 4.

- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) — https://arxiv.org/abs/2609.00077 · 20.2 · oui, mesuré · page ou résumé
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.7 · non · lecture approfondie · machine
- RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (2026-09-21) — https://arxiv.org/abs/2609.24972 · 358.1 · inconnu · page ou résumé · machine
- Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents (2026-11-06) — https://arxiv.org/abs/2611.08946 · 601.1 · inconnu · page ou résumé
- Infinity Machine: a self-improving AI agent for research (2026-10-26) — https://arxiv.org/abs/2610.35579 · 607.1 · inconnu · page ou résumé · machine

**sélection n° 3 — Porte statistique valide à tout instant ou certifiée : test séquentiel de promotion, certificat, point de rupture**

4 mécanismes, 4 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 1, inconnu 3. Lecture : page ou résumé 4.

- PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents (2026-06-06) — https://arxiv.org/abs/2606.08106 · 576.0 · inconnu · page ou résumé · machine
- Self-Evolving Agents with Anytime-Valid Certificates (2026-07-01) — https://arxiv.org/abs/2607.00871 · 577.1 · inconnu · page ou résumé · machine
- When Is Enough Enough in Self-Evolving LLM Systems? (2026-10-03) — https://arxiv.org/abs/2610.04756 · 578.1 · inconnu · page ou résumé
- Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks (2026-09-27) — https://arxiv.org/abs/2609.33180 · 579.0 · oui, affirmé · page ou résumé

**sélection n° 4 — Crédit par la descendance et signaux de lignée**

5 mécanismes, 5 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 4.

- Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025-05-29) — https://arxiv.org/abs/2505.22954 · 240.2 · oui, affirmé · page ou résumé · machine
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.0 · oui, mesuré · lecture approfondie · machine
- HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning (2026-10-21) — https://arxiv.org/abs/2610.30042 · 594.0 · inconnu · page ou résumé · machine
- Evaluation-Free Recursive Self-Improvement for Coding Agents (2026-11-16) — https://arxiv.org/abs/2611.21056 · 608.0 · inconnu · page ou résumé
- Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining (2026-10-21) — https://arxiv.org/abs/2610.29663 · 616.0 · inconnu · page ou résumé

**sélection n° 5 — Archive, population, qualité-diversité et sélection de parents**

8 mécanismes, 8 travaux (6 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, inconnu 6. Lecture : page ou résumé 6, notice seule 2.

- IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation (2026-07-24) — https://arxiv.org/abs/2607.22375 · 26.2 · inconnu · page ou résumé
- Towards Diverse Scientific Hypothesis Search with Large Language Models (2026-06-09) — https://arxiv.org/abs/2606.10587 · 35.1 · inconnu · page ou résumé
- GEAR: Genetic AutoResearch for Agentic Code Evolution (2026-05-08) — https://arxiv.org/abs/2605.13874 · 142.1 · oui, mesuré · page ou résumé · machine
- ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution (2025-09-17) — https://arxiv.org/abs/2509.19349 · 236.1 · inconnu · notice seule · machine
- AlphaEvolve: A coding agent for scientific and algorithmic discovery (2025-06-16) — https://arxiv.org/abs/2506.13131 · 239.2 · inconnu · page ou résumé · machine
- Accelerating scientific discovery with Co-Scientist (2025-02-26) — https://arxiv.org/abs/2502.18864 · 245.2 · inconnu · page ou résumé · machine
- Wright--G\"odel Machine: Mitigating Homogenization in Self-Improving Agents (2026-09-11) — https://openreview.net/forum?id=cQkSamYGQi · 513.0 · oui, mesuré · page ou résumé · machine
- SakanaAI/ShinkaEvolve (dépôt de code) (2025-09-17) — https://github.com/SakanaAI/ShinkaEvolve · 629.1 · inconnu · notice seule · machine

**sélection n° 6 — Sélection d'un ensemble ou d'un portefeuille ; pondération des candidats par l'évidence ou la croyance**

5 mécanismes, 5 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4, inconnu 1. Lecture : page ou résumé 5.

- Budgeted Subset Refinement for Execution-Aware LLM Research Ideation (2026-05-09) — https://arxiv.org/abs/2607.14118 · 90.1 · oui, mesuré · page ou résumé
- Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery (2026-07-05) — https://arxiv.org/abs/2607.04108 · 136.2 · oui, mesuré · page ou résumé · machine
- Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments (2026-10-19) — https://arxiv.org/abs/2610.25747 · 169.1 · inconnu · page ou résumé
- Open-ended Scientific Discovery with Possibilistic Reasoning (2026-10-08) — https://arxiv.org/abs/2610.11289 · 174.1 · oui, mesuré · page ou résumé
- Large Language Bayes (2025-04-18) — https://arxiv.org/abs/2504.14025 · 395.1 · oui, mesuré · page ou résumé · machine

**sélection n° 7 — Tri avant exécution par un prédicteur, un critique ou un modèle de préférence entraîné**

11 mécanismes, 11 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, oui, affirmé 1, non 1, inconnu 3. Lecture : page ou résumé 11.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.1 · oui, mesuré · page ou résumé · machine
- Verify Less, Evolve More: Training Idea-Level Critics for Verification-Efficient ML Evolving Agents (2026-09-18) — https://arxiv.org/abs/2610.08993 · 66.0 · oui, mesuré · page ou résumé
- Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking (2026-08-18) — https://arxiv.org/abs/2608.17270 · 79.1 · oui, mesuré · page ou résumé
- AI Research Preference Models (2026-08-14) — https://arxiv.org/abs/2608.13940 · 81.0 · inconnu · page ou résumé
- Predicting Empirical AI Research Outcomes with Language Models (2025-06-01) — https://arxiv.org/abs/2506.00794 · 96.1 · inconnu · page ou résumé
- Experimental Experience Modeling for Autonomous Research (2026-09-30) — https://arxiv.org/abs/2609.39392 · 109.1 · inconnu · page ou résumé
- PRIME: Predictive Routing of Interventions by Modeling Effects for Scientific Ideation (2026-11-02) — https://arxiv.org/abs/2611.03055 · 144.0 · oui, mesuré · page ou résumé
- IdeaReward: Benchmarking and Training Reward Models for Research Idea Generation (2026-09-19) — https://openreview.net/forum?id=KL3GMYps6X · 505.2 · oui, affirmé · page ou résumé
- Think Before You Experiment: Efficient Experiment Selection for AI Research Agents (2026-09-17) — https://openreview.net/forum?id=Wq7bCHcIED · 515.0 · oui, mesuré · page ou résumé
- Hypothesis Portfolio Search: Shared Feedback for Genetic Perturbation Discovery (2026-09-18) — https://openreview.net/forum?id=NQ43G4FtQH · 541.1 · oui, mesuré · page ou résumé · machine
- ConjectureLineage: Learning Mathematical Taste from Documented Follow-Up (2026-09-07) — https://openreview.net/forum?id=lBoeKHuibU · 559.1 · non · page ou résumé

**sélection n° 8 — Choix de la prochaine direction par une règle d'acquisition : croyance, surprise, rendement attendu, contrôleur modèle**

9 mécanismes, 9 travaux (5 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 8.

- The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory (2026-11-17) — https://arxiv.org/abs/2611.22661 · 50.0 · oui, mesuré · page ou résumé
- Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents (2026-09-17) — https://arxiv.org/abs/2610.02525 · 108.0 · oui, mesuré · page ou résumé
- AIM: Agentic Idea Management for Automated Research (2026-09-16) — https://arxiv.org/abs/2609.38445 · 110.1 · oui, mesuré · page ou résumé · machine
- BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery (2026-06-29) — https://arxiv.org/abs/2606.30335 · 120.1 · inconnu · page ou résumé · machine
- Evidence-Informed LLM Beliefs for Continual Scientific Discovery (2026-06-28) — https://arxiv.org/abs/2606.29182 · 121.4 · oui, mesuré · lecture approfondie · machine
- AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise (2025-06-30) — https://arxiv.org/abs/2507.00310 · 198.2 · oui, mesuré · page ou résumé · machine
- MindFlow: Mind Supernet Powered Thinking Flows for Research Idea Innovation (2026-10-08) — https://arxiv.org/abs/2610.11966 · 370.1 · inconnu · page ou résumé · machine
- Search or Experiment? Budget-Aware Metareasoning for LLM-Driven Scientific Discovery (2026-09-18) — https://openreview.net/forum?id=esQwmkeDoL · 517.1 · oui, mesuré · page ou résumé
- Epistemic Control for Open-world AI Scientists (2026-09-01) — https://openreview.net/forum?id=dzf2UKinnX · 534.1 · inconnu · page ou résumé

**sélection n° 9 — Rejet explicite et journalisé des directions faibles ; mérite d'une hypothèse séparé de la qualité de son exécution**

6 mécanismes, 6 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, non 2, inconnu 3. Lecture : page ou résumé 6.

- Learning the ARTS of Search for Automated Discovery (2026-06-20) — https://arxiv.org/abs/2606.21891 · 138.1 · oui, mesuré · page ou résumé
- IdeaTrail: Full-Process Agent Trajectories for Scientific Ideation (2026-07-11) — https://arxiv.org/abs/2607.10144 · 152.1 · inconnu · page ou résumé
- Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure (2026-06-17) — https://arxiv.org/abs/2608.20361 · 155.1 · inconnu · page ou résumé
- Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench (2026-10-13) — https://arxiv.org/abs/2610.18938 · 170.1 · inconnu · page ou résumé
- CL-ML/open-collider (2026-05-10) — https://github.com/CL-ML/open-collider · 488.2 · non · page ou résumé · machine
- appleweiping/WEIPING_LAB (2026-05-24) — https://github.com/appleweiping/WEIPING_LAB · 495.0 · non · page ou résumé

**sélection n° 10 — Entraînement sur un signal différé, retour d'exécution rendu au modèle, tri en deux temps**

3 mécanismes, 3 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3. Lecture : lecture approfondie 1, page ou résumé 2.

- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.2 · oui, mesuré · lecture approfondie · machine
- Learning to Ideate for Scientific Impact (2026-05-14) — https://arxiv.org/abs/2609.29802 · 151.0 · oui, mesuré · page ou résumé
- Towards Execution-Grounded Automated AI Research (2026-01-20) — https://arxiv.org/abs/2601.14525 · 229.1 · oui, mesuré · page ou résumé

**sélection n° 11 — La sélection mesurée ou décrite comme goulot : qualité du tri avant exécution, écart de capacité, constats d'auteurs**

11 mécanismes, 11 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, oui, affirmé 1, non 2, inconnu 2. Lecture : page ou résumé 10, notice seule 1.

- The Greatness of Science Cannot Be Planned: Agentic Auto-Research is Fuzz Testing (2026-08-10) — https://arxiv.org/abs/2608.09855 · 24.1 · non · page ou résumé
- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment (2026-10-29) — https://arxiv.org/abs/2610.40488 · 58.1 · oui, mesuré · page ou résumé
- Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents (2026-10-12) — https://arxiv.org/abs/2610.21082 · 62.1 · oui, mesuré · page ou résumé
- The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks (2026-09-22) — https://arxiv.org/abs/2609.25804 · 69.0 · oui, mesuré · page ou résumé
- ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment (2026-05-30) — https://arxiv.org/abs/2606.00644 · 87.1 · oui, mesuré · page ou résumé
- Can LLMs Discover Scientific Laws in Real and Parallel Worlds? (2026-09-01) — https://arxiv.org/abs/2609.01552 · 184.2 · inconnu · page ou résumé
- Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities (2026-08-04) — https://arxiv.org/abs/2608.03569 · 187.0 · oui, affirmé · page ou résumé
- AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench (2025-07-03) — https://arxiv.org/abs/2507.02554 · 237.1 · oui, mesuré · page ou résumé
- Lessons from building an automated research scaffold (2026-10-02) — https://www.lesswrong.com/posts/zGaQ3SS9C6So9NXFg/lessons-from-building-an-automated-research-scaffold · 466.0 · non · page ou résumé
- Research acceleration: The view inside OpenAI (2026-09-06) — https://openai.com/index/research-acceleration-view-inside-openai/ · 481.0 · inconnu · notice seule
- Outside the Dictionary: LLM-Guided Equation Discovery Is Limited by What It Proposes (2026-09-18) — https://openreview.net/forum?id=gb3n5lRwjw · 545.1 · oui, mesuré · page ou résumé

**sélection n° 12 — Dérives mesurées de la sélection : agrégat trompeur, sélection sans signal, cible de sélection, famine de la queue, marque « mort », malédiction de l'optimiseur**

7 mécanismes, 7 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 6, inconnu 1. Lecture : page ou résumé 7.

- The Implementation Lottery: Auditing Idea Reliability in Automated Research (2026-07-29) — https://arxiv.org/abs/2607.26587 · 85.1 · oui, mesuré · page ou résumé
- The Weight of Teamwork: Does Communication Structure Help LLM Scientists Search for Scientific Laws? (2026-10-16) — https://arxiv.org/abs/2610.24131 · 130.0 · inconnu · page ou résumé
- Search Discipline for Long-Horizon Research Agents (2026-06-09) — https://arxiv.org/abs/2606.11522 · 436.0 · oui, mesuré · page ou résumé
- Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models (2026-06-15) — https://arxiv.org/abs/2606.16999 · 437.0 · oui, mesuré · page ou résumé
- When Failure Banks Kill Good Ideas: Calibrated Negative Memory for Autonomous Research (2026-09-19) — https://openreview.net/forum?id=eOItnNfHVf · 499.2 · oui, mesuré · page ou résumé
- The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake (2026-08-29) — https://openreview.net/forum?id=Xo66awQ992 · 548.0 · oui, mesuré · page ou résumé
- Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry (2026-08-07) — https://openreview.net/forum?id=IZjj0suAJZ · 551.0 · oui, mesuré · page ou résumé

### Famille « coût »

**coût n° 1 — Filtrer avant d'exécuter : un prédicteur, un critique ou un vérificateur peu coûteux trie les idées pour ne payer l'exécution que sur un sous-ensemble**

10 mécanismes, 10 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 7, inconnu 3. Lecture : page ou résumé 10.

- Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists (2026-11-09) — https://arxiv.org/abs/2611.12184 · 2.2 · oui, mesuré · page ou résumé · machine
- Language Models as AI Research World Models (2026-10-08) — https://arxiv.org/abs/2610.12235 · 64.1 · inconnu · page ou résumé
- Verify Less, Evolve More: Training Idea-Level Critics for Verification-Efficient ML Evolving Agents (2026-09-18) — https://arxiv.org/abs/2610.08993 · 66.1 · oui, mesuré · page ou résumé
- AI Research Preference Models (2026-08-14) — https://arxiv.org/abs/2608.13940 · 81.1 · inconnu · page ou résumé
- SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones? (2026-05-28) — https://arxiv.org/abs/2605.30329 · 88.1 · oui, mesuré · page ou résumé
- Budgeted Subset Refinement for Execution-Aware LLM Research Ideation (2026-05-09) — https://arxiv.org/abs/2607.14118 · 90.0 · oui, mesuré · page ou résumé
- Teaching Language Models to Forecast Research Success Through Comparative Idea Evaluation (2026-03-20) — https://arxiv.org/abs/2605.21491 · 92.1 · inconnu · page ou résumé
- Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents (2026-09-17) — https://arxiv.org/abs/2610.02525 · 108.1 · oui, mesuré · page ou résumé
- Think Before You Experiment: Efficient Experiment Selection for AI Research Agents (2026-09-17) — https://openreview.net/forum?id=Wq7bCHcIED · 515.1 · oui, mesuré · page ou résumé
- Small Critics Make Strong Models Count: Learning to Verify Stronger Models for Efficient AutoResearch (2026-09-19) — https://openreview.net/forum?id=oYzABaBXFN · 518.1 · oui, mesuré · page ou résumé

**coût n° 2 — Allocation dynamique du budget : parallélisme, tour suivant, branches ou viviers répartis selon l'état de la recherche ou le budget restant**

9 mécanismes, 8 travaux (4 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 5, oui, affirmé 1, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 7.

- SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery (2026-07-02) — https://arxiv.org/abs/2607.02807 · 30.1 · inconnu · page ou résumé · machine
- The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory (2026-11-17) — https://arxiv.org/abs/2611.22661 · 50.2 · inconnu · page ou résumé
- PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research (2026-09-15) — https://arxiv.org/abs/2609.17846 · 70.1 · oui, mesuré · page ou résumé · machine
- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) — https://openreview.net/forum?id=Ur08wiPVM3 · 502.2 · oui, affirmé · page ou résumé
- Search or Experiment? Budget-Aware Metareasoning for LLM-Driven Scientific Discovery (2026-09-18) — https://openreview.net/forum?id=esQwmkeDoL · 517.0 · oui, mesuré · page ou résumé
- Hypothesis Portfolio Search: Shared Feedback for Genetic Perturbation Discovery (2026-09-18) — https://openreview.net/forum?id=NQ43G4FtQH · 541.0 · oui, mesuré · page ou résumé · machine
- How Many Scientists? Epistemic Diversity in Expanding-Frontier Discovery (2026-09-19) — https://openreview.net/forum?id=mqzDjlr57k · 543.1 · oui, mesuré · page ou résumé
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.2, 593.6 · inconnu / oui, mesuré · lecture approfondie · machine

**coût n° 3 — Largeur contre profondeur à dépense totale égale : un agent, agents parallèles, meilleur de N, partage entre lignées**

7 mécanismes, 7 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 4, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 6.

- Scaling Discovery Requires Forgetting (2026-10-14) — https://arxiv.org/abs/2610.20563 · 10.3 · oui, mesuré · page ou résumé
- Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents (2026-09-18) — https://arxiv.org/abs/2610.07447 · 13.3 · oui, mesuré · page ou résumé · machine
- Automated Discovery Has No Universally Superior Harness (2026-07-20) — https://arxiv.org/abs/2607.18235 · 27.2 · inconnu · page ou résumé
- LLM Evolutionary Search Strategies Should be Compared by Tokens (2026-10-13) — https://arxiv.org/abs/2610.23977 · 581.2 · oui, mesuré · lecture approfondie
- Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search (2026-09-17) — https://arxiv.org/abs/2609.19799 · 582.0 · oui, mesuré · page ou résumé
- Compute Allocation for Self-Evolving LLMs: From Depth-Breadth to Multi-Armed Bandits (2026-05-28) — https://arxiv.org/abs/2605.29268 · 584.0 · inconnu · page ou résumé
- From Search to Research: Exploring Search Scaling in Autonomous Quantitative Factor Mining (2026-09-28) — https://arxiv.org/abs/2609.35559 · 590.0 · inconnu · page ou résumé

**coût n° 4 — Budget apparié et compté de bout en bout (jetons, temps, évaluations) ; le budget comme variable contrôlée de la mesure ou de la tâche**

9 mécanismes, 9 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 8, oui, affirmé 1. Lecture : lecture approfondie 4, page ou résumé 5.

- AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment (2026-09-18) — https://arxiv.org/abs/2610.33644 · 60.1 · oui, mesuré · page ou résumé
- The Implementation Lottery: Auditing Idea Reliability in Automated Research (2026-07-29) — https://arxiv.org/abs/2607.26587 · 85.3 · oui, mesuré · page ou résumé
- From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? (2026-09-18) — https://arxiv.org/abs/2611.05108 · 98.3 · oui, mesuré · lecture approfondie
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.4 · oui, mesuré · lecture approfondie · machine
- Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery (2026-10-13) — https://arxiv.org/abs/2610.18449 · 171.0 · oui, mesuré · page ou résumé
- RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts (2024-11-22) — https://arxiv.org/abs/2411.15114 · 393.1 · oui, mesuré · page ou résumé
- autoresearch (dépôt de code) (2026-03-06) — https://github.com/karpathy/autoresearch · 396.3 · oui, affirmé · page ou résumé · machine
- Lineage Is Memory: Parent Inheritance and Feedback Disclosure in Short-Budget LLM-Guided Optimization (2026-10-30) — https://arxiv.org/abs/2610.41157 · 456.4 · oui, mesuré · lecture approfondie
- LLM Evolutionary Search Strategies Should be Compared by Tokens (2026-10-13) — https://arxiv.org/abs/2610.23977 · 581.0 · oui, mesuré · lecture approfondie

**coût n° 5 — Témoin à calcul apparié : le calcul d'inférence ajouté, le vote à k tirages ou une base simple comme explication concurrente du gain**

6 mécanismes, 6 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 3, non 1, inconnu 1. Lecture : page ou résumé 6.

- On the Effects of Reasoning Effort and Prompt-Based Diversification on Scientific Ideation Diversity (2026-04-21) — https://openreview.net/forum?id=xt5P634aET · 566.2 · non · page ou résumé
- Rethinking the Evaluation of Harness Evolution for Agents (2026-07-14) — https://arxiv.org/abs/2607.12227 · 585.0 · oui, mesuré · page ou résumé
- Harness-Delta Attribution: Dissecting Gains From Harness Evolution (2026-10-15) — https://arxiv.org/abs/2610.22466 · 586.1 · oui, affirmé · page ou résumé
- Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds (2026-07-31) — https://arxiv.org/abs/2608.02636 · 587.1 · inconnu · page ou résumé
- The Illusion of Multi-Agent Advantage (2026-06-11) — https://arxiv.org/abs/2606.13003 · 588.1 · oui, affirmé · page ou résumé
- The Limits of Inference Scaling Through Resampling (2024-11-26) — https://arxiv.org/abs/2411.17501 · 592.1 · oui, affirmé · page ou résumé

**coût n° 6 — Règles d'arrêt : convergence, vérification, test séquentiel valide à tout instant, plateau, bascule « explorer puis s'engager »**

6 mécanismes, 6 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, inconnu 3. Lecture : page ou résumé 6.

- SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution (2026-05-14) — https://arxiv.org/abs/2605.15308 · 141.1 · oui, mesuré · page ou résumé · machine
- Explore, Then Commit: Measurement-Efficient Scientific Law Discovery with Language Models (2026-10-06) — https://arxiv.org/abs/2610.07620 · 176.0 · inconnu · page ou résumé
- When Should an AI Scientist Stop? Verifiable Experiment Steering and Refusal for Autonomous Discovery (2026-05-26) — https://arxiv.org/abs/2606.07576 · 212.1 · oui, mesuré · page ou résumé
- Automated Hypothesis Validation with Agentic Sequential Falsifications (2025-02-14) — https://arxiv.org/abs/2502.09858 · 247.1 · inconnu · page ou résumé
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) — https://arxiv.org/abs/2610.24291 · 408.4 · oui, mesuré · page ou résumé
- When Is Enough Enough in Self-Evolving LLM Systems? (2026-10-03) — https://arxiv.org/abs/2610.04756 · 578.0 · inconnu · page ou résumé

**coût n° 7 — Rendement décroissant et calcul gaspillé, mesurés**

4 mécanismes, 4 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 3, inconnu 1. Lecture : page ou résumé 4.

- Recovering Wasted Compute in Autoresearch Agents (2026-03-25) — https://arxiv.org/abs/2608.10424 · 116.0 · oui, mesuré · page ou résumé
- Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch (2026-07-30) — https://arxiv.org/abs/2607.27687 · 117.0 · oui, mesuré · page ou résumé
- SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery (2026-10-20) — https://arxiv.org/abs/2610.28706 · 129.1 · inconnu · page ou résumé
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) — https://metr.org/blog/2026-07-21-expenditure-horizon/ · 464.0 · oui, mesuré · page ou résumé

**coût n° 8 — Le coût dans la sélection : plafond de coût, voie bon marché avant la voie chère, modèle par rôle, signal sans exécution aval**

4 mécanismes, 4 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, inconnu 3. Lecture : lecture approfondie 1, page ou résumé 3.

- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.5 · oui, mesuré · lecture approfondie · machine
- Harness Evolution Hits a Ceiling: When Weight Training Should Begin (2026-10-08) — https://arxiv.org/abs/2610.11655 · 599.1 · inconnu · page ou résumé
- Evaluation-Free Recursive Self-Improvement for Coding Agents (2026-11-16) — https://arxiv.org/abs/2611.21056 · 608.1 · inconnu · page ou résumé
- Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (2026-10-22) — https://arxiv.org/abs/2610.31743 · 618.1 · inconnu · page ou résumé

**coût n° 9 — Efficacité de la recherche mesurée en appels ou en essais**

3 mécanismes, 3 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1, inconnu 1. Lecture : page ou résumé 2, notice seule 1.

- Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery (2026-07-05) — https://arxiv.org/abs/2607.04108 · 136.3 · oui, mesuré · page ou résumé · machine
- ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution (2025-09-17) — https://arxiv.org/abs/2509.19349 · 236.2 · inconnu · notice seule · machine
- CaliMem: Search-Efficient Data Agent via Calibrated Memory (2026-10-25) — https://arxiv.org/abs/2610.34500 · 455.1 · oui, affirmé · page ou résumé

**coût n° 10 — Le coût de la recherche entre dans la preuve : nombre d'essais dans le seuil, coût de la vérification comme borne**

3 mécanismes, 3 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, non 2. Lecture : page ou résumé 2, notice seule 1.

- What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery (2026-08-27) — https://arxiv.org/abs/2608.27734 · 439.1 · oui, mesuré · page ou résumé
- The Verification Bottleneck (2026-11-01) — https://arxiv.org/abs/2611.02265 · 449.1 · non · page ou résumé
- LLM Daydreaming (2025-07) — https://gwern.net/ai-daydreaming · 472.3 · non · notice seule

**coût n° 11 — Coût total des lancements rapporté (appels, dollars, heures), sans règle d'allocation**

3 mécanismes, 3 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 2. Lecture : lecture approfondie 1, page ou résumé 2.

- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) — https://arxiv.org/abs/2611.03424 · 54.4 · oui, affirmé · page ou résumé
- Automated Weak-to-Strong Researcher (2026-04-14) — https://alignment.anthropic.com/2026/automated-w2s-researcher/ · 259.3 · oui, mesuré · page ou résumé · machine
- Evaluating LLM Research Agents as Tests of Return Predictability (2026-11-02) — https://arxiv.org/abs/2611.04070 · 450.5 · oui, affirmé · lecture approfondie

**coût n° 12 — Le coût comme métrique même (efficacité de calcul) ou la montée de l'effort de test d'un juge**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2. Lecture : page ou résumé 2.

- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (2026-10-05) — https://arxiv.org/abs/2610.06824 · 67.1 · oui, mesuré · page ou résumé
- TASTE: Can AI Models Judge AI Safety Research Proposals? (2026-08-28) — https://alignment.anthropic.com/2026/taste/ · 258.3 · oui, mesuré · page ou résumé

**coût n° 13 — Taille d'équipe et passage à l'échelle : taille effective, temps d'achèvement, goulot de priorisation**

3 mécanismes, 3 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1, non 1. Lecture : page ou résumé 2, notice seule 1.

- 2026-03-19 org uplift game (note) (2026-03-19) — https://metr.org/notes/2026-03-19-org-uplift-game/ · 486.0 · non · notice seule
- Coarse-Grained Dynamics of Multi-Agent Collective AutoResearch (2026-09-19) — https://openreview.net/forum?id=HorMYlEerY · 509.1 · oui, mesuré · page ou résumé
- The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size (2026-05-31) — https://arxiv.org/abs/2606.02646 · 613.0 · oui, affirmé · page ou résumé

### Famille « auto-conception »

**auto-conception n° 1 — Réécriture du code de l'agent : la modification n'est gardée que si elle est validée empiriquement**

3 mécanismes, 3 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, oui, affirmé 1. Lecture : lecture approfondie 2, page ou résumé 1.

- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.0 · oui, mesuré · lecture approfondie · machine
- Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025-05-29) — https://arxiv.org/abs/2505.22954 · 240.0 · oui, affirmé · page ou résumé · machine
- Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24) — https://arxiv.org/abs/2510.21614 · 593.3 · oui, mesuré · lecture approfondie · machine

**auto-conception n° 2 — Un méta-agent écrit de nouveaux agents en code, ou pilote la stratégie de recherche à la place d'une stratégie fixée par un humain**

2 mécanismes, 2 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1. Lecture : page ou résumé 2.

- AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding (2026-10-04) — https://arxiv.org/abs/2610.05334 · 407.0 · oui, mesuré · page ou résumé · machine
- Automated Design of Agentic Systems (2024-08-15) — https://arxiv.org/abs/2408.08435 · 595.0 · oui, affirmé · page ou résumé · machine

**auto-conception n° 3 — La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration)**

4 mécanismes, 4 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 3, inconnu 1. Lecture : page ou résumé 4.

- Hyperagents (2026-03-19) — https://arxiv.org/abs/2603.19461 · 125.0 · oui, affirmé · page ou résumé · machine
- Scientific discovery as meta-optimization: a combinatorial optimization case study (2026-06-25) — https://arxiv.org/abs/2606.26728 · 299.0 · oui, affirmé · page ou résumé
- Organon : From Evolutionary Search to Recursive Self-Improving Agents for Scientific Discovery (2026-10-17) — https://arxiv.org/abs/2610.33046 · 384.0 · inconnu · page ou résumé · machine
- MetaEvoForge: Learning to Improve Agents Faster Across Task Environments (2026) — https://neurips.cc/virtual/2026/169839 · 625.0 · oui, affirmé · page ou résumé · machine

**auto-conception n° 4 — Boucle d'évolution du harnais de l'agent : lire trajectoires, scores et échecs, proposer une modification, l'évaluer, recommencer**

4 mécanismes, 4 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 2, inconnu 2. Lecture : lecture approfondie 1, page ou résumé 3.

- Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench (2026-10-31) — https://arxiv.org/abs/2611.00643 · 57.3 · oui, mesuré · lecture approfondie · machine
- Rethinking the Evaluation of Harness Evolution for Agents (2026-07-14) — https://arxiv.org/abs/2607.12227 · 585.2 · oui, mesuré · page ou résumé
- Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds (2026-07-31) — https://arxiv.org/abs/2608.02636 · 587.0 · inconnu · page ou résumé
- HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning (2026-10-21) — https://arxiv.org/abs/2610.30042 · 594.1 · inconnu · page ou résumé · machine

**auto-conception n° 5 — Contraintes et régularisation des modifications de harnais contre le surajustement aux tâches d'évolution**

3 mécanismes, 3 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : inconnu 3. Lecture : page ou résumé 3.

- RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (2026-09-21) — https://arxiv.org/abs/2609.24972 · 358.0 · inconnu · page ou résumé · machine
- HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses (2026-08-03) — https://arxiv.org/abs/2608.01918 · 604.0 · inconnu · page ou résumé
- Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts (2026-09-16) — https://arxiv.org/abs/2609.18366 · 605.1 · inconnu · page ou résumé

**auto-conception n° 6 — Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique)**

3 mécanismes, 3 travaux (3 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : inconnu 3. Lecture : page ou résumé 3.

- PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents (2026-06-06) — https://arxiv.org/abs/2606.08106 · 576.2 · inconnu · page ou résumé · machine
- Self-Evolving Agents with Anytime-Valid Certificates (2026-07-01) — https://arxiv.org/abs/2607.00871 · 577.0 · inconnu · page ou résumé · machine
- Infinity Machine: a self-improving AI agent for research (2026-10-26) — https://arxiv.org/abs/2610.35579 · 607.0 · inconnu · page ou résumé · machine

**auto-conception n° 7 — Cadres et bancs d'évaluation des boucles d'auto-amélioration**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 1, inconnu 1. Lecture : page ou résumé 2.

- Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks (2026-09-27) — https://arxiv.org/abs/2609.33180 · 579.2 · oui, affirmé · page ou résumé
- Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents (2026-11-06) — https://arxiv.org/abs/2611.08946 · 601.0 · inconnu · page ou résumé

**auto-conception n° 8 — Composants des harnais décomposés et comparés ; résultats sans configuration supérieure partout ou sans ablation**

3 mécanismes, 3 travaux (1 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, oui, affirmé 1, inconnu 1. Lecture : lecture approfondie 1, page ou résumé 2.

- Automated Discovery Has No Universally Superior Harness (2026-07-20) — https://arxiv.org/abs/2607.18235 · 27.0 · oui, mesuré · page ou résumé
- Recursive self-improvement of AI research agents (2026-09-22) — https://arxiv.org/abs/2609.26457 · 112.6 · inconnu · lecture approfondie · machine
- Does Failure Feedback Direct Agent Self-Modification? (2026-10-10) — https://arxiv.org/abs/2610.14662 · 596.0 · oui, affirmé · page ou résumé

**auto-conception n° 9 — Composition de l'équipe d'agents et affectation d'un modèle par rôle**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, affirmé 1, inconnu 1. Lecture : page ou résumé 2.

- Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems (2026-10-14) — https://arxiv.org/abs/2610.19799 · 617.0 · oui, affirmé · page ou résumé
- Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (2026-10-22) — https://arxiv.org/abs/2610.31743 · 618.0 · inconnu · page ou résumé

**auto-conception n° 10 — Entraînement des poids aux compétences d'auto-évolution, seuls ou croisés avec l'évolution du harnais**

2 mécanismes, 2 travaux (0 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : inconnu 2. Lecture : page ou résumé 2.

- Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning (2026-07-24) — https://arxiv.org/abs/2607.21971 · 597.0 · inconnu · page ou résumé
- Harness Evolution Hits a Ceiling: When Weight Training Should Begin (2026-10-08) — https://arxiv.org/abs/2610.11655 · 599.0 · inconnu · page ou résumé

**auto-conception n° 11 — Auto-modification annoncée, mécanisme non précisé par la notice**

7 mécanismes, 7 travaux (2 sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : oui, mesuré 1, non 1, inconnu 5. Lecture : page ou résumé 6, notice seule 1.

- When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents (2026-11-10) — https://arxiv.org/abs/2611.14326 · 97.2 · inconnu · page ou résumé
- Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research (2026-10-18) — https://arxiv.org/abs/2610.24944 · 102.3 · inconnu · page ou résumé · machine
- DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses (2026-10-16) — https://arxiv.org/abs/2610.23839 · 103.0 · oui, mesuré · page ou résumé
- Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery (2026-11-16) — https://arxiv.org/abs/2611.21847 · 126.2 · inconnu · page ou résumé · machine
- Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station (2026-09-16) — https://arxiv.org/abs/2610.08927 · 178.1 · inconnu · page ou résumé
- From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement (2026-09-14) — https://arxiv.org/abs/2610.14625 · 218.0 · non · page ou résumé
- RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving (2026-11-11) — https://arxiv.org/abs/2611.14949 · 391.1 · inconnu · notice seule

## 2. Machines : systèmes complets et les mécanismes qu'ils assemblent

« Machine » veut dire ici : un système ou une boucle complète décrit comme tel par ses auteurs (ou par le dépôt de code), qui assemble au moins deux mécanismes du relevé. La liste est celle du relevé d'après le titre et la nature du travail ; elle n'est pas exhaustive (R8). Pour chaque machine : les mécanismes qu'elle assemble, avec le regroupement où chacun se range (section 1).

### 2.1 Machines relevées d'après une lecture approfondie du dépôt

- **Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine** (2025-10-24) — https://arxiv.org/abs/2510.21614 — lecture : lecture approfondie
  - assemble : sélection n° 4 (Crédit par la descendance et signaux de lignée) [593.0, oui, mesuré] ; exploration n° 6 (Recherche en arbre) [593.1, oui, mesuré] ; coût n° 2 (Allocation dynamique du budget) [593.2, oui, mesuré] ; auto-conception n° 1 (Réécriture du code de l'agent) [593.3, oui, mesuré] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [593.4, oui, mesuré] ; épreuve n° 6 (Séparer le signal qui sert à chercher de la mesure finale) [593.5, oui, mesuré] ; coût n° 2 (Allocation dynamique du budget) [593.6, inconnu]
- **Recursive self-improvement of AI research agents** (2026-09-22) — https://arxiv.org/abs/2609.26457 — lecture : lecture approfondie
  - assemble : auto-conception n° 1 (Réécriture du code de l'agent) [112.0, oui, mesuré] ; sélection n° 1 (Acceptation gloutonne à un pas) [112.1, oui, mesuré] ; épreuve n° 6 (Séparer le signal qui sert à chercher de la mesure finale) [112.2, oui, mesuré] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [112.3, oui, mesuré] ; coût n° 4 (Budget apparié et compté de bout en bout (jetons, temps, évaluations) ; le budget comme variable contrôlée de la mesure ou de la tâche) [112.4, oui, mesuré] ; épreuve n° 6 (Séparer le signal qui sert à chercher de la mesure finale) [112.5, inconnu] ; auto-conception n° 8 (Composants des harnais décomposés et comparés ; résultats sans configuration supérieure partout ou sans ablation) [112.6, inconnu] ; sélection n° 2 (Porte de validation sur une métrique distincte, tenue à l'écart ou privée ; banc de sélection ; régularisation de la sélection) [112.7, non]
- **Evidence-Informed LLM Beliefs for Continual Scientific Discovery** (2026-06-28) — https://arxiv.org/abs/2606.29182 — lecture : lecture approfondie
  - assemble : originalité n° 4 (Nouveauté comme écart de croyance ou d'a priori) [121.0, oui, mesuré] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [121.1, oui, mesuré] ; mémoire n° 9 (Issues vérifiées et croyances gardées comme mémoire du sélecteur) [121.2, oui, mesuré] ; exploration n° 6 (Recherche en arbre) [121.3, oui, mesuré] ; sélection n° 8 (Choix de la prochaine direction par une règle d'acquisition) [121.4, oui, mesuré] ; jugement n° 4 (Instabilité du juge) [121.5, oui, mesuré]
- **Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench** (2026-10-31) — https://arxiv.org/abs/2611.00643 — lecture : lecture approfondie
  - assemble : épreuve n° 1 (Mondes plantés à vérité connue du constructeur) [57.0, oui, mesuré] ; originalité n° 4 (Nouveauté comme écart de croyance ou d'a priori) [57.1, oui, mesuré] ; sélection n° 10 (Entraînement sur un signal différé, retour d'exécution rendu au modèle, tri en deux temps) [57.2, oui, mesuré] ; auto-conception n° 4 (Boucle d'évolution du harnais de l'agent) [57.3, oui, mesuré] ; exploration n° 15 (Résultats négatifs ou nuls sur des composants d'exploration) [57.4, oui, mesuré] ; coût n° 8 (Le coût dans la sélection) [57.5, oui, mesuré] ; épreuve n° 5 (Préenregistrement, engagement préalable et enregistrement des essais avant exécution ou avant les décisions) [57.6, oui, mesuré]

Autres études lues en profondeur, qui ne sont pas des machines mais des protocoles d'étude (leurs mécanismes sont en section 1) : indices 98, 450, 456 et 581. L'indice 136, dont les pages 1 à 4 du PDF ont été relues pour le relevé, figure en 2.2 faute de fiche de lecture approfondie au dépôt.

### 2.2 Machines relevées d'après la notice, le résumé ou la page (non opposable, R7)

- **Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery** (2026-07-05) — https://arxiv.org/abs/2607.04108 — lecture : page ou résumé
  - assemble : épreuve n° 7 (Témoins, nuls et placebos) [136.0, oui, mesuré] ; exploration n° 7 (Tirages indépendants, bifurcations, redémarrages, meilleur de N) [136.1, oui, mesuré] ; sélection n° 6 (Sélection d'un ensemble ou d'un portefeuille ; pondération des candidats par l'évidence ou la croyance) [136.2, oui, mesuré] ; coût n° 9 (Efficacité de la recherche mesurée en appels ou en essais) [136.3, oui, mesuré] ; mémoire n° 11 (Mesures de ce que la mémoire ou l'héritage apportent) [136.4, oui, mesuré]
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (2025-05-29) — https://arxiv.org/abs/2505.22954 — lecture : page ou résumé
  - assemble : auto-conception n° 1 (Réécriture du code de l'agent) [240.0, oui, affirmé] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [240.1, inconnu] ; sélection n° 4 (Crédit par la descendance et signaux de lignée) [240.2, oui, affirmé]
- **AlphaEvolve: A coding agent for scientific and algorithmic discovery** (2025-06-16) — https://arxiv.org/abs/2506.13131 — lecture : page ou résumé
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [239.0, oui, affirmé] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [239.1, oui, affirmé] ; sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [239.2, inconnu]
- **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution** (2025-09-17) — https://arxiv.org/abs/2509.19349 — lecture : notice seule
  - assemble : sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [236.1, inconnu] ; coût n° 9 (Efficacité de la recherche mesurée en appels ou en essais) [236.2, inconnu]
- **SakanaAI/ShinkaEvolve (dépôt de code)** (2025-09-17) — https://github.com/SakanaAI/ShinkaEvolve — lecture : notice seule
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [629.0, inconnu] ; sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [629.1, inconnu]
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (2025-04-08) — https://arxiv.org/abs/2504.08066 — lecture : page ou résumé
  - assemble : exploration n° 6 (Recherche en arbre) [241.0, oui, affirmé] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [241.1, oui, affirmé] ; originalité n° 2 (Nouveauté mesurée contre la littérature) [241.2, inconnu] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [241.3, inconnu]
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (2024-08-12) — https://arxiv.org/abs/2408.06292 — lecture : page ou résumé
  - assemble : exploration n° 14 (Un seul agent, une seule lignée) [254.0, oui, affirmé] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [254.1, oui, affirmé] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [254.2, oui, affirmé] ; originalité n° 2 (Nouveauté mesurée contre la littérature) [254.3, inconnu]
- **Accelerating scientific discovery with Co-Scientist** (2025-02-26) — https://arxiv.org/abs/2502.18864 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [245.0, oui, affirmé] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [245.1, oui, affirmé] ; sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [245.2, inconnu] ; épreuve n° 15 (Épreuve décrite sans montage précisé par la notice) [245.3, inconnu]
- **Hyperagents** (2026-03-19) — https://arxiv.org/abs/2603.19461 — lecture : page ou résumé
  - assemble : auto-conception n° 3 (La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration)) [125.0, oui, affirmé] ; mémoire n° 8 (Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée) [125.1, inconnu]
- **Automated Design of Agentic Systems** (2024-08-15) — https://arxiv.org/abs/2408.08435 — lecture : page ou résumé
  - assemble : auto-conception n° 2 (Un méta-agent écrit de nouveaux agents en code, ou pilote la stratégie de recherche à la place d'une stratégie fixée par un humain) [595.0, oui, affirmé] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [595.1, oui, affirmé]
- **autoresearch (dépôt de code)** (2026-03-06) — https://github.com/karpathy/autoresearch — lecture : page ou résumé
  - assemble : exploration n° 14 (Un seul agent, une seule lignée) [396.0, oui, affirmé] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [396.1, oui, affirmé] ; sélection n° 1 (Acceptation gloutonne à un pas) [396.2, oui, affirmé] ; coût n° 4 (Budget apparié et compté de bout en bout (jetons, temps, évaluations) ; le budget comme variable contrôlée de la mesure ou de la tâche) [396.3, oui, affirmé]
- **How we built Kosmos (et Kosmos, arXiv 2511.02824)** (2025-11) — https://arxiv.org/abs/2511.02824 — lecture : notice seule
  - assemble : mémoire n° 7 (Base de connaissances ou banque d'idées partagée entre agents et sessions) [482.0, inconnu] ; jugement n° 10 (Humain dans la boucle) [482.1, oui, affirmé]
- **Automated Weak-to-Strong Researcher** (2026-04-14) — https://alignment.anthropic.com/2026/automated-w2s-researcher/ — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [259.0, oui, mesuré] ; mémoire n° 7 (Base de connaissances ou banque d'idées partagée entre agents et sessions) [259.1, oui, mesuré] ; épreuve n° 6 (Séparer le signal qui sert à chercher de la mesure finale) [259.2, oui, mesuré] ; coût n° 11 (Coût total des lancements rapporté (appels, dollars, heures), sans règle d'allocation) [259.3, oui, mesuré]
- **Organon : From Evolutionary Search to Recursive Self-Improving Agents for Scientific Discovery** (2026-10-17) — https://arxiv.org/abs/2610.33046 — lecture : page ou résumé
  - assemble : auto-conception n° 3 (La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration)) [384.0, inconnu] ; mémoire n° 8 (Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée) [384.1, inconnu] ; exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [384.2, inconnu]
- **Infinity Machine: a self-improving AI agent for research** (2026-10-26) — https://arxiv.org/abs/2610.35579 — lecture : page ou résumé
  - assemble : auto-conception n° 6 (Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique)) [607.0, inconnu] ; sélection n° 2 (Porte de validation sur une métrique distincte, tenue à l'écart ou privée ; banc de sélection ; régularisation de la sélection) [607.1, inconnu]
- **MetaEvoForge: Learning to Improve Agents Faster Across Task Environments** (2026) — https://neurips.cc/virtual/2026/169839 — lecture : page ou résumé
  - assemble : auto-conception n° 3 (La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration)) [625.0, oui, affirmé] ; mémoire n° 8 (Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée) [625.1, inconnu] ; épreuve n° 6 (Séparer le signal qui sert à chercher de la mesure finale) [625.2, inconnu]
- **AIM: Agentic Idea Management for Automated Research** (2026-09-16) — https://arxiv.org/abs/2609.38445 — lecture : page ou résumé
  - assemble : exploration n° 9 (Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur) [110.0, oui, mesuré] ; sélection n° 8 (Choix de la prochaine direction par une règle d'acquisition) [110.1, oui, mesuré] ; mémoire n° 7 (Base de connaissances ou banque d'idées partagée entre agents et sessions) [110.2, oui, mesuré] ; jugement n° 8 (Séparation de qui propose, qui exécute et qui juge ; arbitre ou règle de décision fixés hors de l'agent) [110.3, oui, mesuré]
- **PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research** (2026-09-15) — https://arxiv.org/abs/2609.17846 — lecture : page ou résumé
  - assemble : exploration n° 6 (Recherche en arbre) [70.0, oui, mesuré] ; coût n° 2 (Allocation dynamique du budget) [70.1, oui, mesuré] ; mémoire n° 5 (Mémoire des échecs et des directions ratées) [70.2, oui, mesuré]
- **Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery** (2026-11-16) — https://arxiv.org/abs/2611.21847 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [126.0, inconnu] ; mémoire n° 6 (Leçons admises en mémoire seulement après test ou preuve ; garde contre les transferts négatifs) [126.1, inconnu] ; auto-conception n° 11 (Auto-modification annoncée, mécanisme non précisé par la notice) [126.2, inconnu]
- **AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation** (2026-05-27) — https://arxiv.org/abs/2605.28655 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [611.0, inconnu] ; mémoire n° 5 (Mémoire des échecs et des directions ratées) [611.1, inconnu]
- **CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery** (2026-04-02) — https://arxiv.org/abs/2604.01658 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [398.0, oui, mesuré] ; mémoire n° 7 (Base de connaissances ou banque d'idées partagée entre agents et sessions) [398.1, oui, mesuré]
- **Wright--G\"odel Machine: Mitigating Homogenization in Self-Improving Agents** (2026-09-11) — https://openreview.net/forum?id=cQkSamYGQi — lecture : page ou résumé
  - assemble : sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [513.0, oui, mesuré] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [513.1, oui, mesuré]
- **HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning** (2026-10-21) — https://arxiv.org/abs/2610.30042 — lecture : page ou résumé
  - assemble : sélection n° 4 (Crédit par la descendance et signaux de lignée) [594.0, inconnu] ; auto-conception n° 4 (Boucle d'évolution du harnais de l'agent) [594.1, inconnu]
- **RRSI: Regularized Recursive Self-Improvement of Agent Harnesses** (2026-09-21) — https://arxiv.org/abs/2609.24972 — lecture : page ou résumé
  - assemble : auto-conception n° 5 (Contraintes et régularisation des modifications de harnais contre le surajustement aux tâches d'évolution) [358.0, inconnu] ; sélection n° 2 (Porte de validation sur une métrique distincte, tenue à l'écart ou privée ; banc de sélection ; régularisation de la sélection) [358.1, inconnu]
- **PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents** (2026-06-06) — https://arxiv.org/abs/2606.08106 — lecture : page ou résumé
  - assemble : sélection n° 3 (Porte statistique valide à tout instant ou certifiée) [576.0, inconnu] ; épreuve n° 8 (Multiplicité et garanties statistiques) [576.1, inconnu] ; auto-conception n° 6 (Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique)) [576.2, inconnu]
- **Self-Evolving Agents with Anytime-Valid Certificates** (2026-07-01) — https://arxiv.org/abs/2607.00871 — lecture : page ou résumé
  - assemble : auto-conception n° 6 (Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique)) [577.0, inconnu] ; sélection n° 3 (Porte statistique valide à tout instant ou certifiée) [577.1, inconnu] ; mémoire n° 2 (Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer) [577.2, inconnu]
- **Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists** (2026-11-09) — https://arxiv.org/abs/2611.12184 — lecture : page ou résumé
  - assemble : exploration n° 3 (Information réduite, ignorance volontaire, regard neuf, point de départ inattendu, exploration libre sans objet désigné, directions que les chercheurs ne formuleraient pas) [2.0, oui, mesuré] ; sélection n° 7 (Tri avant exécution par un prédicteur, un critique ou un modèle de préférence entraîné) [2.1, oui, mesuré] ; coût n° 1 (Filtrer avant d'exécuter) [2.2, oui, mesuré] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [2.3, oui, mesuré] ; originalité n° 3 (Nouveauté jugée par un modèle ou par des experts) [2.4, oui, mesuré] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [2.5, oui, affirmé] ; mémoire n° 9 (Issues vérifiées et croyances gardées comme mémoire du sélecteur) [2.6, oui, mesuré]
- **Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents** (2026-09-18) — https://arxiv.org/abs/2610.07447 — lecture : page ou résumé
  - assemble : exploration n° 7 (Tirages indépendants, bifurcations, redémarrages, meilleur de N) [13.0, oui, mesuré] ; mémoire n° 1 (Oubli et vidage) [13.1, oui, mesuré] ; sélection n° 1 (Acceptation gloutonne à un pas) [13.2, oui, mesuré] ; coût n° 3 (Largeur contre profondeur à dépense totale égale) [13.3, oui, mesuré] ; originalité n° 1 (Nouveauté mesurée par distance ou direction dans un espace de plongements ou de structures ; limites de ces distances) [13.4, oui, mesuré] ; épreuve n° 4 (Exécution sous un évaluateur exécutable ou un correcteur programmé) [13.5, oui, mesuré]
- **HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses** (2026-09-14) — https://arxiv.org/abs/2609.15938 — lecture : page ou résumé
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [133.0, oui, mesuré]
- **EvoGens: A Population-Based Heuristic Search Framework for Scientific Idea Generation** (2026-05-29) — https://arxiv.org/abs/2605.30961 — lecture : page ou résumé
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [139.0, oui, mesuré]
- **GEAR: Genetic AutoResearch for Agentic Code Evolution** (2026-05-08) — https://arxiv.org/abs/2605.13874 — lecture : page ou résumé
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [142.0, oui, mesuré] ; sélection n° 5 (Archive, population, qualité-diversité et sélection de parents) [142.1, oui, mesuré]
- **SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution** (2026-05-14) — https://arxiv.org/abs/2605.15308 — lecture : page ou résumé
  - assemble : exploration n° 5 (Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses) [141.0, oui, mesuré] ; coût n° 6 (Règles d'arrêt) [141.1, oui, mesuré]
- **Idea Search: Guiding Tree Search with Ideas to Explore Diverse Scientific Methods** (2026-08-09) — https://arxiv.org/abs/2608.08958 — lecture : page ou résumé
  - assemble : exploration n° 6 (Recherche en arbre) [135.0, oui, mesuré] ; mémoire n° 7 (Base de connaissances ou banque d'idées partagée entre agents et sessions) [135.1, oui, mesuré]
- **Tree-of-Ideas: Automated Research Ideation via Cross-Trajectory Reasoning over Scholarly Evolution** (2026-08-11) — https://arxiv.org/abs/2608.10740 — lecture : page ou résumé
  - assemble : exploration n° 1 (Idéation ancrée dans la littérature ou un graphe de connaissances) [134.0, oui, mesuré]
- **IdeaScientist: Orchestrating Agents for Grounded Scientific Ideation** (2026-09-18) — https://arxiv.org/abs/2610.04074 — lecture : page ou résumé
  - assemble : exploration n° 2 (Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs) [150.0, oui, mesuré]
- **Distill, Debate, Discover: Grounding Multi-Agent Research Ideation in Graph-Distilled Insights** (2026-10-23) — https://arxiv.org/abs/2610.33366 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [128.0, inconnu] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [128.1, non]
- **AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration** (2026-03-15) — https://arxiv.org/abs/2605.20025 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [279.0, inconnu] ; épreuve n° 9 (Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes) [279.1, inconnu] ; jugement n° 10 (Humain dans la boucle) [279.2, inconnu]
- **AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle** (2026-05-29) — https://arxiv.org/abs/2605.31468 — lecture : page ou résumé
  - assemble : mémoire n° 8 (Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée) [452.0, oui, affirmé]
- **Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research** (2026-10-18) — https://arxiv.org/abs/2610.24944 — lecture : page ou résumé
  - assemble : mémoire n° 3 (Trajectoire ou historique de la recherche conservé et lu par le contrôleur ou le proposeur) [102.0, inconnu] ; exploration n° 6 (Recherche en arbre) [102.1, inconnu] ; jugement n° 8 (Séparation de qui propose, qui exécute et qui juge ; arbitre ou règle de décision fixés hors de l'agent) [102.2, inconnu] ; auto-conception n° 11 (Auto-modification annoncée, mécanisme non précisé par la notice) [102.3, inconnu]
- **YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents** (2026-10-01) — https://arxiv.org/abs/2610.01097 — lecture : page ou résumé
  - assemble : mémoire n° 5 (Mémoire des échecs et des directions ratées) [107.0, oui, mesuré] ; épreuve n° 9 (Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes) [107.1, oui, mesuré]
- **XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery** (2026-07-14) — https://arxiv.org/abs/2607.12301 — lecture : page ou résumé
  - assemble : mémoire n° 4 (État de la recherche tenu hors du modèle) [118.0, inconnu] ; exploration n° 6 (Recherche en arbre) [118.1, inconnu]
- **BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery** (2026-06-29) — https://arxiv.org/abs/2606.30335 — lecture : page ou résumé
  - assemble : mémoire n° 9 (Issues vérifiées et croyances gardées comme mémoire du sélecteur) [120.0, inconnu] ; sélection n° 8 (Choix de la prochaine direction par une règle d'acquisition) [120.1, inconnu]
- **Large Language Bayes** (2025-04-18) — https://arxiv.org/abs/2504.14025 — lecture : page ou résumé
  - assemble : exploration n° 7 (Tirages indépendants, bifurcations, redémarrages, meilleur de N) [395.0, oui, mesuré] ; sélection n° 6 (Sélection d'un ensemble ou d'un portefeuille ; pondération des candidats par l'évidence ou la croyance) [395.1, oui, mesuré]
- **Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors** (2026-09-22) — https://arxiv.org/abs/2609.27051 — lecture : page ou résumé
  - assemble : jugement n° 8 (Séparation de qui propose, qui exécute et qui juge ; arbitre ou règle de décision fixés hors de l'agent) [441.0, oui, affirmé] ; épreuve n° 8 (Multiplicité et garanties statistiques) [441.1, oui, affirmé] ; exploration n° 8 (Équipes d'agents) [441.2, oui, affirmé]
- **CL-ML/open-collider** (2026-05-10) — https://github.com/CL-ML/open-collider — lecture : page ou résumé
  - assemble : exploration n° 2 (Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs) [488.0, non] ; exploration n° 2 (Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs) [488.1, non] ; sélection n° 9 (Rejet explicite et journalisé des directions faibles ; mérite d'une hypothèse séparé de la qualité de son exécution) [488.2, non] ; jugement n° 10 (Humain dans la boucle) [488.3, non]
- **r2m-ai/scholar-loop** (2026-06-15) — https://github.com/r2m-ai/scholar-loop — lecture : page ou résumé
  - assemble : épreuve n° 9 (Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes) [491.0, inconnu] ; exploration n° 12 (Remèdes à l'effondrement de la diversité, et leurs limites) [491.1, inconnu]
- **An AI Scientist that Doesn't Drift: Taste, Structure, and Falsifiable Findings in a Quadruped Navigation Research Loop** (2026-07-30) — https://arxiv.org/abs/2608.07542 — lecture : page ou résumé
  - assemble : exploration n° 9 (Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur) [332.0, oui, affirmé] ; épreuve n° 9 (Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes) [332.1, oui, affirmé] ; mémoire n° 8 (Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée) [332.2, inconnu]
- **SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery** (2026-07-02) — https://arxiv.org/abs/2607.02807 — lecture : page ou résumé
  - assemble : exploration n° 10 (Mesures de l'exploration d'un run) [30.0, oui, mesuré] ; coût n° 2 (Allocation dynamique du budget) [30.1, inconnu]
- **Hypothesis Portfolio Search: Shared Feedback for Genetic Perturbation Discovery** (2026-09-18) — https://openreview.net/forum?id=NQ43G4FtQH — lecture : page ou résumé
  - assemble : coût n° 2 (Allocation dynamique du budget) [541.0, oui, mesuré] ; sélection n° 7 (Tri avant exécution par un prédicteur, un critique ou un modèle de préférence entraîné) [541.1, oui, mesuré] ; exploration n° 12 (Remèdes à l'effondrement de la diversité, et leurs limites) [541.2, oui, mesuré]
- **IdeaGraph: Evidence-Bearing Synergy Junctions for Cross-Field Scientific Ideation** (2026-08-27) — https://openreview.net/forum?id=92DdZnwXPh — lecture : page ou résumé
  - assemble : exploration n° 2 (Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs) [550.0, non] ; jugement n° 9 (Jugement ancré dans des preuves traçables, des journaux ou un audit des artefacts plutôt que dans un avis libre) [550.1, oui, affirmé]
- **CoI‑Pro: Scientific Idea Generation via Retrieval over Research Trajectories** (2026-09-17) — https://openreview.net/forum?id=MtTWQDzv0e — lecture : page ou résumé
  - assemble : exploration n° 1 (Idéation ancrée dans la littérature ou un graphe de connaissances) [529.0, oui, mesuré] ; jugement n° 3 (Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle) [529.1, oui, mesuré]
- **MindFlow: Mind Supernet Powered Thinking Flows for Research Idea Innovation** (2026-10-08) — https://arxiv.org/abs/2610.11966 — lecture : page ou résumé
  - assemble : exploration n° 17 (Exploration décrite sans mécanisme précisé par la notice) [370.0, inconnu] ; sélection n° 8 (Choix de la prochaine direction par une règle d'acquisition) [370.1, inconnu]
- **AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise** (2025-06-30) — https://arxiv.org/abs/2507.00310 — lecture : page ou résumé
  - assemble : exploration n° 9 (Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur) [198.0, oui, mesuré] ; originalité n° 4 (Nouveauté comme écart de croyance ou d'a priori) [198.1, oui, mesuré] ; sélection n° 8 (Choix de la prochaine direction par une règle d'acquisition) [198.2, oui, mesuré]
- **Principle-Evolvable Scientific Discovery via Uncertainty Minimization** (2026-02-06) — https://arxiv.org/abs/2602.06448 — lecture : page ou résumé
  - assemble : exploration n° 9 (Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur) [397.0, oui, mesuré]
- **Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents** (2026-10-10) — https://arxiv.org/abs/2610.14683 — lecture : page ou résumé
  - assemble : épreuve n° 1 (Mondes plantés à vérité connue du constructeur) [104.0, oui, affirmé] ; mémoire n° 6 (Leçons admises en mémoire seulement après test ou preuve ; garde contre les transferts négatifs) [104.1, oui, affirmé]
- **Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery** (2026-09-28) — https://arxiv.org/abs/2609.35315 — lecture : page ou résumé
  - assemble : exploration n° 8 (Équipes d'agents) [111.0, inconnu] ; mémoire n° 6 (Leçons admises en mémoire seulement après test ou preuve ; garde contre les transferts négatifs) [111.1, inconnu]
- **AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding** (2026-10-04) — https://arxiv.org/abs/2610.05334 — lecture : page ou résumé
  - assemble : auto-conception n° 2 (Un méta-agent écrit de nouveaux agents en code, ou pilote la stratégie de recherche à la place d'une stratégie fixée par un humain) [407.0, oui, mesuré]

## 3. Mécanismes hors de toute machine

Idées de méthode publiées (adresses et lecture : section 1, au même regroupement) dont le relevé ne trouve l'assemblage dans aucun des systèmes recensés en section 2. « Hors de toute machine » ne dit pas « inédit » : cela dit que, dans ce moissonnage, le travail qui porte le mécanisme n'est pas l'un des systèmes de la section 2 ; le mécanisme peut figurer dans un système non recensé (R8).

### 3.1 Regroupements dont aucun travail n'est une machine recensée

**exploration n° 4 — Conditionnement du proposeur : personas, sujets, amorces, température, structure en étapes** (8 travaux ; éprouvé selon les auteurs : oui, mesuré 3, oui, affirmé 2, inconnu 3)

- Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs (2026-09-24) · 17.0
- Human diversity fuels collective creativity that large language models cannot simulate or sustain (2026-07-29) · 25.0
- Beyond the Hivemind: Escaping LLM Homogeneity via Meta-Persona Anchoring and Sequential Temperature Scaling (2026-05-31) · 37.0
- Anchorless Diversification for Parallel LLM Ideation (2026-05-28) · 38.0
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) · 54.2
- Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output (2026-05-01) · 160.0
- Diversifying Personalized Research Ideation against AI-Induced Homogenization (2026-07-30) · 323.0
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (2026-08-28) · 460.0

**exploration n° 11 — Diagnostics de l'effondrement de la diversité et de l'homogénéité des idées** (19 travaux ; éprouvé selon les auteurs : oui, mesuré 13, oui, affirmé 2, inconnu 4)

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) · 0.1
- Language Models are Lazy Poets: Creative Mode Collapse at Scale (2026-10-16) · 8.0
- Large Language Models Extend Known Research But Do Not Create New Research Directions (2026-10-12) · 11.1
- Measuring the Gap Between Human and LLM Research Ideas (2026-07-01) · 31.1
- Contemporary AI lacks the imagination to diverge or negate in science (2026-06-06) · 36.1
- AI Research Agents Narrow Scientific Exploration (2026-05-27) · 39.0
- Multi-LLM Systems Exhibit Robust Semantic Collapse (2026-05-16) · 43.0
- Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs (2026-05-11) · 45.0
- Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation (2026-04-20) · 48.0
- A Cognitive Framework for Idea Diversity in Large Language Models (2026-02-23) · 49.0
- What Does It Take to Be a Good AI Research Agent? Studying the Role of Ideation Diversity (2025-11-19) · 233.0
- Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) (2025-10-27) · 235.0
- Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024-09-06) · 253.1
- Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization (2026-05-19) · 399.0
- Mutation Without Variation: Convergence Dynamics in LLM-Driven Program Evolution (2026-06-03) · 401.0
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) · 408.0
- Homogenization in Multi-Agent Systems (2026-09-18) · 507.0
- Outside the Dictionary: LLM-Guided Equation Discovery Is Limited by What It Proposes (2026-09-18) · 545.2
- Same Algorithms, Different Scientist: Design Space Bias in AI Discovery (2026-08-29) · 549.2

**exploration n° 13 — Entraînement de l'exploration par renforcement ou supervision** (4 travaux ; éprouvé selon les auteurs : oui, mesuré 4)

- Training Reasoning Models to Generate Diverse Scientific Ideas (2026-09-18) · 9.0
- Reinforcing Agentic Creativity in Scientific Ideation with Night Science (2026-09-18) · 15.0
- TIGER: Learning from Researcher Taste to Generate Tailored Research Ideas (2026-09-17) · 56.0
- Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents (2026-06-30) · 154.0

**exploration n° 16 — Positions et théories de l'exploration** (6 travaux ; éprouvé selon les auteurs : oui, affirmé 1, non 5)

- The Greatness of Science Cannot Be Planned: Agentic Auto-Research is Fuzz Testing (2026-08-10) · 24.0
- Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks (2026-06-12) · 34.0
- Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery (2026-05-09) · 215.0
- Navigating Epistemic Monocultures in AI-Driven Science: A Simulation Study (2026-08-19) · 403.0
- Sampling Is Not Curiosity: Why LLM Agents Should Investigate (2026-11-07) · 410.0
- You Are Not Immune To Mode Collapse (2026-05) · 475.0

**originalité n° 5 — Diversité et homogénéité des sorties ou des populations : effondrement de mode, monoculture, idées uniques, redondance d'options** (24 travaux ; éprouvé selon les auteurs : oui, mesuré 11, oui, affirmé 2, non 3, inconnu 8)

- Evaluating LLM Creativity through Long-Tail Performance (2026-10-09) · 12.0
- Auditing Pairwise Equivalence Judgments: Self-Critique Effects and Diversity Measurement in Multi-Agent Hypothesis Generation (2026-09-14) · 14.1
- How Strong Is the Evidence for the Artificial Hivemind? Reevaluating Evidence for the Open-Ended Homogeneity of Language Models (2026-09-27) · 16.0
- Beneath the Diff: Diagnosing and Mitigating Algorithmic Mode Collapse in Code-Level Autonomous Research Loops (2026-08-31) · 20.4
- Are LLMs becoming similarly creative? Evidence from three years of models (2026-08-19) · 23.0
- The Hitchhiker's Guide to Monoculture: AI Homogenizes Syntax, Not (Necessarily) Semantics (2026-07-12) · 28.0
- Comment on arXiv:2607.01233: Survivorship Bias in Published-Paper Baselines for Research-Idea Distributions (2026-07-09) · 29.0
- Measuring the Gap Between Human and LLM Research Ideas (2026-07-01) · 31.0
- Thinking Like a Scientist? A Structural Study of LLM-Generated Research Methods (2026-06-15) · 33.0
- AI Research Agents Narrow Scientific Exploration (2026-05-27) · 39.1
- LLM Jaggedness Unlocks Scientific Creativity (2026-05-11) · 46.0
- Ex Ante Evaluation of AI-Induced Idea Diversity Collapse (2026-05-07) · 47.0
- A Cognitive Framework for Idea Diversity in Large Language Models (2026-02-23) · 49.1
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) · 54.1
- Unlocking LLM Creativity in Science through Analogical Reasoning (2026-05-11) · 158.1
- Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output (2026-05-01) · 160.1
- Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) (2025-10-27) · 235.1
- Diversifying Personalized Research Ideation against AI-Induced Homogenization (2026-07-30) · 323.1
- An important Bottleneck in LLM Optimizers: Principle-Level Local Optima (2026-10-16) · 408.1
- Gap Detection: Mitigating Homogenization through Demand and Defensibility (2026-09-18) · 508.1
- Mathematica Incognita: Characterizing Open-Ended Mathematical Exploration in Language Models (2026-09-19) · 540.1
- Same Algorithms, Different Scientist: Design Space Bias in AI Discovery (2026-08-29) · 549.1
- On the Effects of Reasoning Effort and Prompt-Based Diversification on Scientific Ideation Diversity (2026-04-21) · 566.1
- When Idea Generation Scales: Idea-Level Evaluation for Autonomous Scientific Discovery (2026-05-20) · 567.0

**originalité n° 6 — Protection contre la contamination et la mémorisation : coupure de date, mondes contrefactuels, graine privée, masquage, banques renouvelées** (21 travaux ; éprouvé selon les auteurs : oui, mesuré 3, oui, affirmé 8, non 1, inconnu 9)

- Tracing the Scientific Discovery Capacity of LLMs to Their Training Data (2026-11-02) · 5.0
- Eliciting Research Taste in LLMs through Future Research Direction Choice (2026-06-29) · 51.2
- Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents (2026-09-07) · 73.1
- Can Large Language Models Forecast What Researchers Study Next? (2026-09-01) · 75.1
- Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies (2026-08-17) · 80.1
- Unsatz: Evaluating Scientific Discovery Without a Given Ansatz (2026-10-31) · 162.1
- SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World (2026-10-27) · 165.1
- Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes (2026-09-29) · 181.1
- Can LLMs Discover Scientific Laws in Real and Parallel Worlds? (2026-09-01) · 184.1
- DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking (2026-05-25) · 193.1
- NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents (2025-10-08) · 196.1
- LLMs are below chance on TASTE once a shortcut is removed (2026-11-15) · 260.1
- Can Frontier Models Autocomplete Safety Research? (2026-07-12) · 261.1
- Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot (2026-08-17) · 415.1
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) · 489.2
- Do LLMs Have Research Taste? An Analysis Using BóLèBench (2026-09-12) · 500.2
- Beyond Hypothesis Recovery: Evaluating Scientific Hypothesis Generation through Evidence-Hypothesis Transitions (2026-09-19) · 538.1
- Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists (2026-09-25) · 553.2
- Beyond Imitation: Evaluating LLM Reviewers by Impact ? (2026-08-29) · 562.1
- HorizonBench: Evaluating Ideation Agents on Future Scientific Discoveries (2026-05-26) · 569.1
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) · 572.1

**originalité n° 7 — Absence de contrôle de nouveauté, ou débat sur sa définition** (2 travaux ; éprouvé selon les auteurs : non 2)

- The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery (2026-10-13) · 375.3
- Have LLMs Generated Novel Insights? (2025-02) · 471.0

**épreuve n° 2 — Vérité prise dans le futur : coupure de date, gel du corpus, rejeu historique, prévision contre la littérature à venir** (12 travaux ; éprouvé selon les auteurs : oui, mesuré 9, oui, affirmé 1, inconnu 2)

- Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next (2026-11-16) · 0.2
- AI Research Agents Narrow Scientific Exploration (2026-05-27) · 39.2
- IdeaTaste: Do LLMs Share the Research Taste of Human Researchers? (2026-08-31) · 54.0
- Can Large Language Models Forecast What Researchers Study Next? (2026-09-01) · 75.0
- ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment (2026-05-30) · 87.0
- HindSight: Evaluating LLM-Generated Research Ideas via Future Impact (2026-03-16) · 93.0
- Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments (2026-01-12) · 95.1
- DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses (2026-10-16) · 103.1
- Priced Guidance: Can Language Models Generate Future Research Ideas? (2026-09-17) · 149.0
- Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot (2026-08-17) · 415.0
- HorizonBench: Evaluating Ideation Agents on Future Scientific Discoveries (2026-05-26) · 569.0
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) · 572.0

**épreuve n° 3 — Redécouverte d'un résultat publié, ou retrouvé d'une idée tenue cachée, comme épreuve** (9 travaux ; éprouvé selon les auteurs : oui, mesuré 9)

- Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game (2026-10-13) · 1.0
- Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies (2026-08-17) · 80.0
- OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery (2026-10-27) · 166.0
- Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station (2026-09-16) · 178.2
- TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents (2026-09-04) · 183.0
- Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery (2026-07-17) · 189.1
- FIRE-Bench: Evaluating AI Agents on the Rediscovery of Scientific Insights (2026-02-02) · 195.0
- Can Frontier Models Autocomplete Safety Research? (2026-07-12) · 261.0
- prometheus-eval/into-the-unknown (arXiv 2610.19159) (2026-09-24) · 490.0

**épreuve n° 10 — Dispersion, reproductibilité et variabilité des analyses ou des runs menés par des agents** (7 travaux ; éprouvé selon les auteurs : oui, mesuré 5, inconnu 2)

- Automated Discovery Has No Universally Superior Harness (2026-07-20) · 27.1
- Letting AI Formulate the Research Question: Autonomous Research Agents (2026-10-29) · 145.2
- Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development (2026-08-13) · 186.1
- AI "errors" (2026) · 428.0
- Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse (2026-02-21) · 430.0
- Nonstandard Errors in AI Agents (2026-03-17) · 431.0
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) · 464.2

**épreuve n° 11 — Évaluation sans fuite et consciente du nombre d'essais ; rendement rapporté contre rendement réel** (5 travaux ; éprouvé selon les auteurs : oui, mesuré 3, inconnu 2)

- From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks? (2026-09-18) · 98.4
- The Alpha Illusion: Reported Alpha from LLM Trading Agents Should Not Be Treated as Deployment Evidence (2026-05-16) · 435.0
- What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery (2026-08-27) · 439.0
- Agentic Empirical Asset Pricing: Methodological Foundations (2026-09-01) · 440.0
- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) · 502.1

**épreuve n° 12 — Réfutabilité, prédiction avant exécution et effet attendu : prévoir puis observer, séparer conception et exécution** (7 travaux ; éprouvé selon les auteurs : oui, mesuré 7, inconnu 1)

- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment (2026-10-29) · 58.0
- Language Models as AI Research World Models (2026-10-08) · 64.0
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (2026-10-05) · 67.0
- What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation (2026-08-24) · 78.0
- Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure (2026-06-17) · 155.2
- Do Research Agents Improve for the Right Reasons? (2026-09-19) · 506.0, 506.1
- EffectPreconception: Guiding ML Research Agents through Effect Prediction and Observation (2026-09-14) · 516.0

**épreuve n° 13 — Environnements et bancs interactifs de découverte (lois, causalité, mécanismes, composants isolés)** (6 travaux ; éprouvé selon les auteurs : oui, mesuré 2, inconnu 4)

- Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments (2026-10-19) · 169.0
- Causal Discovery Bench: Can LLMs Autonomously Conduct Effective Experiments? (2026-10-13) · 172.0
- ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure (2026-05-28) · 192.0
- CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists (2026-05-25) · 194.0
- DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (2024-06-10) · 200.0
- CreativeBench2.0: Benchmarking Creative Method Discovery and Foresight Toward Recursive Self-Improvement (2026-09-15) · 544.0

**épreuve n° 14 — Positions, constats et synthèses sur l'épreuve** (13 travaux ; éprouvé selon les auteurs : oui, mesuré 3, non 9, inconnu 1)

- Large Language Models Extend Known Research But Do Not Create New Research Directions (2026-10-12) · 11.2
- Workflow Closure Is Not Scientific Closure in Auto-Research Systems (2026-05-25) · 213.0
- Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap (2026-06-29) · 224.0
- Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts (2026-01-06) · 230.0
- Optimal Post-Hoc Theorizing (2025-05-15) · 426.0
- Sound Agentic Science Requires Adversarial Experiments (2026-04-23) · 434.0
- Takes on Automating Alignment (2026-04-20) · 468.0
- How I'm thinking about different types of automated alignment (2026-11-11) · 469.0
- Stateful Search with Stateless Agents: Scaling Long-Horizon Automated Research (2026-09-15) · 514.1
- AI Scientists Need Stronger Verification Framework to Address Systemic Fragility (2026-09-19) · 527.0
- Beyond Hypothesis Recovery: Evaluating Scientific Hypothesis Generation through Evidence-Hypothesis Transitions (2026-09-19) · 538.0
- Position: AI Scientists Are Not Yet Ready for Open-Ended and Fully Autonomous Scientific Discovery (2026-05-26) · 573.0
- Toward Evaluation Frameworks for Multi-Agent Scientific AI Systems (2026-03-18) · 620.0

**jugement n° 1 — Goût de recherche et préférences d'experts : choix forcé ou comparaisons par paires contre des experts, des chercheurs, des auteurs ou des pairs** (20 travaux ; éprouvé selon les auteurs : oui, mesuré 21, non 1)

- Contemporary AI lacks the imagination to diverge or negate in science (2026-06-06) · 36.0
- Eliciting Research Taste in LLMs through Future Research Direction Choice (2026-06-29) · 51.0, 51.1
- What makes a theorem interesting? Operationalizing interestingness for open-ended exploration (2026-11-02) · 55.0
- AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment (2026-09-18) · 60.0
- Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents (2026-10-12) · 62.0
- Learning Individual Scientific Taste with Privileged Hindsight Distillation (2026-10-14) · 63.0
- Ideation Arena: Evaluating LLM Generated Research Ideas with Battle-style Human Expert Assessment (2026-08-30) · 76.0
- LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation (2026-08-13) · 82.0
- SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones? (2026-05-28) · 88.0
- Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas (2026-03-11) · 94.0
- Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers (2024-09-06) · 253.0
- TASTE: Can AI Models Judge AI Safety Research Proposals? (2026-08-28) · 258.0, 258.1
- LLMs are below chance on TASTE once a shortcut is removed (2026-11-15) · 260.0
- TastyBench: Toward Measuring Research Taste in LLM (dépôt parviam/tastybench) (2025-12-02) · 262.0
- AI Can Learn Scientific Taste (2026-03-15) · 412.0
- The Scientific Research Taste Benchmark (SciTaste-Bench): A Multi-Disciplinary Benchmark for Assessing Large Language Models' Judgment of Research Taste in Scientific Papers (2026-10-09) · 420.0
- Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI? (2026-11-09) · 424.0
- My Research Process: Understanding and Cultivating Research Taste (2025) · 476.0
- Do AI Agents Have Research Taste? SENSE-Bench for Anomaly-Driven Scientific Exploration (2026-09-16) · 504.1
- ConjectureLineage: Learning Mathematical Taste from Documented Follow-Up (2026-09-07) · 559.0

**jugement n° 2 — Juge confronté à une vérité différée ou à l'issue réelle : citations, temps écoulé, exécution, impact** (10 travaux ; éprouvé selon les auteurs : oui, mesuré 7, oui, affirmé 1, inconnu 3)

- HindSight: Evaluating LLM-Generated Research Ideas via Future Impact (2026-03-16) · 93.1
- Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments (2026-01-12) · 95.0
- Predicting Empirical AI Research Outcomes with Language Models (2025-06-01) · 96.0
- The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas (2025-06-25) · 238.1
- PaperScorer: How Predictable Is Paper Acceptance? (2026-10-22) · 422.0
- When AI builds itself (2026-09-18) · 461.0
- Do LLMs Have Research Taste? An Analysis Using BóLèBench (2026-09-12) · 500.0, 500.1
- IdeaReward: Benchmarking and Training Reward Models for Research Idea Generation (2026-09-19) · 505.1
- CreativeBench2.0: Benchmarking Creative Method Discovery and Foresight Toward Recursive Self-Improvement (2026-09-15) · 544.1
- LiveIdeaBench: Forecasting Emerging Research Ideas Against Future Literature (2026-06-29) · 572.2

**jugement n° 5 — Validation et tests de sensibilité d'un juge : erreurs plantées, accord insuffisant, protocole, témoins** (9 travaux ; éprouvé selon les auteurs : oui, mesuré 9)

- The Novelty Trap: When Repetition Helps LLM Research (2026-09-19) · 502.3
- Approval Is Not Discovery: When Can a Model of the Scientist Steer a Discovery Agent? (2026-09-27) · 546.0
- Recombination or Discovery? A Retrieval-Grounded Novelty Audit of Machine-Generated Research Papers (2026-07-30) · 547.1
- The Placebo Improvement: Stress-Testing False Claims by Autonomous Research Agents (2026-08-30) · 552.1
- Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists (2026-09-25) · 553.1
- PermuLoop: Causal Evidence That LLM Discovery Agents Use Experimental Feedback (2026-09-27) · 555.1
- AUDIT: Validating LLM Judges Through Controlled Error Injection (2026-08-27) · 558.0
- When Correction Memory Fails: Episodic Retrieval Is Not Test-Time Learning for Pairwise Judges (2026-08-27) · 560.1
- The Grade Says Little, the Score Orders: AI Reviewer Panels Against a Venue's Ratings and Decisions (2026-09-06) · 561.0

**jugement n° 6 — Corrélation des erreurs, monoculture et nombre de votes effectifs d'un collège de juges** (7 travaux ; éprouvé selon les auteurs : oui, mesuré 4, oui, affirmé 2, non 3)

- We need more decorrelated evidence (2026-11-12) · 465.0
- Automated Alignment is Harder Than You Think (arXiv 2605.06390 ; repris sur LessWrong) (2026-05-07) · 470.0
- Homogenization in Multi-Agent Systems (2026-09-18) · 507.2
- Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels (2026-08-28) · 556.0
- LLM Reviewers Err Together: Shared Blind Spots and Correlated Judgments in Peer Review (2026-08-28) · 564.0, 564.1
- Do AI Reviewers Converge? Diversity Collapse in Model-Generated Peer Review (2026-03-16) · 570.0, 570.1
- Against Homogeneous Consensus: Why Scientific Discovery Requires Heterogeneous Adversarial LLM Agents (2026-03-16) · 571.1

**jugement n° 7 — Juge ou vérificateur entraîné à cette fin : modèle de récompense, petit critique, grille intériorisée, signal différé** (6 travaux ; éprouvé selon les auteurs : oui, mesuré 5, inconnu 1)

- Verify Less, Evolve More: Training Idea-Level Critics for Verification-Efficient ML Evolving Agents (2026-09-18) · 66.2
- Teaching Language Models to Forecast Research Success Through Comparative Idea Evaluation (2026-03-20) · 92.0
- Learning to Ideate for Scientific Impact (2026-05-14) · 151.1
- IdeaReward: Benchmarking and Training Reward Models for Research Idea Generation (2026-09-19) · 505.0
- Small Critics Make Strong Models Count: Learning to Verify Stronger Models for Efficient AutoResearch (2026-09-19) · 518.0
- Internalizing Rubric Guidance for Research Agents (2026-09-17) · 536.0

**jugement n° 11 — Audit d'intégrité et de fausse nouveauté des articles produits par des agents** (4 travaux ; éprouvé selon les auteurs : oui, mesuré 3, inconnu 1)

- SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems (2026-05-11) · 214.0
- All That Glitters is Not Novel: Plagiarism in AI Generated Research (2025-02-23) · 246.1
- wanshuiyin/Anti-Autoresearch (2026-06-26) · 496.0
- Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers (2026-09-17) · 537.0

**jugement n° 12 — Relecteurs modèles évalués contre les relectures et décisions humaines** (5 travaux ; éprouvé selon les auteurs : oui, mesuré 3, oui, affirmé 1, inconnu 1)

- How Well Do LLMs Perform in Peer Review? Evidence from Finance and Accounting (2026-10-13) · 445.0
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) · 489.1
- The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake (2026-08-29) · 548.1
- Beyond Imitation: Evaluating LLM Reviewers by Impact ? (2026-08-29) · 562.0
- AutoResearchArena: A Comprehensive Evaluation of AI-Driven Research Across Ideation, Experimentation, and Writing (2026-10-12) · 568.0

**jugement n° 13 — Constats et positions sur le jugement (goulot, vérification, objectif donné, origine du goût)** (8 travaux ; éprouvé selon les auteurs : oui, mesuré 2, oui, affirmé 1, non 5)

- Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game (2026-10-13) · 1.2
- Verifier strength does not buy discovery quality: a pre-registered two-domain test of LLM-based automated research, with post-hoc evidence pointing to proposer-pool composition (2026-11-03) · 53.0
- How Is Automated Research Evaluated? A Survey of Benchmarks and Evaluation Practices (2026-10-08) · 65.0
- Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts (2026-06-22) · 208.0
- The Ideation Bottleneck: Decomposing the Quality Gap Between AI-Generated and Human Economics Research (2026-04-03) · 433.0
- The Verification Bottleneck (2026-11-01) · 449.0
- Lessons from building an automated research scaffold (2026-10-02) · 466.1
- AIs can now often do massive easy-to-verify SWE tasks (2026) · 485.0

**jugement n° 14 — Critères de valeur construits autrement qu'un avis de juge : logits, croyance, e-valeurs, agrégation d'objectifs** (6 travaux ; éprouvé selon les auteurs : oui, mesuré 1, oui, affirmé 2, inconnu 3)

- Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking (2026-08-18) · 79.0
- Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another (2026-11-14) · 161.1
- Scientific discovery as meta-optimization: a combinatorial optimization case study (2026-06-25) · 299.1
- Large Language Bayes Is Not Reparameterisation-Invariant (2026-09-24) · 442.0
- Exploiting LLMs for Automatic Hypothesis Assessment via a Logit-Based Calibrated Prior (2025-06-03) · 574.1
- On the Use of LLM Priors in Multiple Hypothesis Testing with e-Values (2026) · 624.0

**jugement n° 15 — Évaluer l'ensemble produit ou le processus plutôt que l'appariement à une cible unique** (7 travaux ; éprouvé selon les auteurs : oui, mesuré 3, oui, affirmé 1, inconnu 3)

- More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation (2026-05-07) · 159.1
- Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures (2026-10-29) · 163.0
- Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation (2026-07-09) · 309.2
- FrontierScience: evaluating AI's ability to perform expert-level scientific tasks (arXiv 2601.21165) (2025-12) · 483.0
- IdeaPrism: Beyond Ground-Truth Matching for Hypothesis Evaluation (2026-09-12) · 522.0
- IdeaDec: Benchmarking Long-Horizon Scientific Idea Decoding in AI Research Agents (2026-09-18) · 523.0
- MathIdeaBench: A Benchmark For Mathematical Research Idea Generation (2026-08-26) · 526.0

**mémoire n° 10 — Mémoire apprise dans les poids ou par un réflecteur entraîné** (2 travaux ; éprouvé selon les auteurs : oui, affirmé 1, inconnu 1)

- Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks (2026-06-27) · 137.0
- Training Language Agents to Learn from Experience (2026-05-19) · 598.0

**mémoire n° 12 — Dérives de la mémoire d'état : réentrée des trouvailles acceptées, provenance de la trace, liens retenus** (3 travaux ; éprouvé selon les auteurs : oui, mesuré 2, non 1)

- LLM Daydreaming (2025-07) · 472.2
- Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry (2026-08-07) · 551.1
- Search Pathology Diagnosis for Automated Discovery (2026-09-06) · 554.0

**mémoire n° 13 — Positions sur ce que doit être la mémoire d'un agent de recherche** (2 travaux ; éprouvé selon les auteurs : non 2)

- Evolutionary Intelligence for Scientific Discovery: From Evolutionary Computation to Cumulative Discovery Systems (2026-07-10) · 222.0
- Position: Scientific Memory Is Not Chat History: Reframing Long-Term Memory Evaluation for Research Agents (2026-09-19) · 510.0

**sélection n° 11 — La sélection mesurée ou décrite comme goulot : qualité du tri avant exécution, écart de capacité, constats d'auteurs** (11 travaux ; éprouvé selon les auteurs : oui, mesuré 6, oui, affirmé 1, non 2, inconnu 2)

- The Greatness of Science Cannot Be Planned: Agentic Auto-Research is Fuzz Testing (2026-08-10) · 24.1
- rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment (2026-10-29) · 58.1
- Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents (2026-10-12) · 62.1
- The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks (2026-09-22) · 69.0
- ForeSci: Evaluating LLM Agents for Forward-Looking AI Research Judgment (2026-05-30) · 87.1
- Can LLMs Discover Scientific Laws in Real and Parallel Worlds? (2026-09-01) · 184.2
- Adversarial Fast-Moving Real-World Domains as Test Beds for Benchmarking AI Scientist Capabilities (2026-08-04) · 187.0
- AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench (2025-07-03) · 237.1
- Lessons from building an automated research scaffold (2026-10-02) · 466.0
- Research acceleration: The view inside OpenAI (2026-09-06) · 481.0
- Outside the Dictionary: LLM-Guided Equation Discovery Is Limited by What It Proposes (2026-09-18) · 545.1

**sélection n° 12 — Dérives mesurées de la sélection : agrégat trompeur, sélection sans signal, cible de sélection, famine de la queue, marque « mort », malédiction de l'optimiseur** (7 travaux ; éprouvé selon les auteurs : oui, mesuré 6, inconnu 1)

- The Implementation Lottery: Auditing Idea Reliability in Automated Research (2026-07-29) · 85.1
- The Weight of Teamwork: Does Communication Structure Help LLM Scientists Search for Scientific Laws? (2026-10-16) · 130.0
- Search Discipline for Long-Horizon Research Agents (2026-06-09) · 436.0
- Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models (2026-06-15) · 437.0
- When Failure Banks Kill Good Ideas: Calibrated Negative Memory for Autonomous Research (2026-09-19) · 499.2
- The Selection-Target Problem in AI-Assisted Science: Reviewer Novelty and Later Scientific Uptake (2026-08-29) · 548.0
- Tail Starvation in Recursive Discovery: A Boundary for Validation and Re-entry (2026-08-07) · 551.0

**coût n° 5 — Témoin à calcul apparié : le calcul d'inférence ajouté, le vote à k tirages ou une base simple comme explication concurrente du gain** (6 travaux ; éprouvé selon les auteurs : oui, mesuré 1, oui, affirmé 3, non 1, inconnu 1)

- On the Effects of Reasoning Effort and Prompt-Based Diversification on Scientific Ideation Diversity (2026-04-21) · 566.2
- Rethinking the Evaluation of Harness Evolution for Agents (2026-07-14) · 585.0
- Harness-Delta Attribution: Dissecting Gains From Harness Evolution (2026-10-15) · 586.1
- Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds (2026-07-31) · 587.1
- The Illusion of Multi-Agent Advantage (2026-06-11) · 588.1
- The Limits of Inference Scaling Through Resampling (2024-11-26) · 592.1

**coût n° 7 — Rendement décroissant et calcul gaspillé, mesurés** (4 travaux ; éprouvé selon les auteurs : oui, mesuré 3, inconnu 1)

- Recovering Wasted Compute in Autoresearch Agents (2026-03-25) · 116.0
- Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch (2026-07-30) · 117.0
- SpecEvo: Speculative Evolution with Large Language Models for Cost-Efficient Scientific Discovery (2026-10-20) · 129.1
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (2026-07-21) · 464.0

**coût n° 10 — Le coût de la recherche entre dans la preuve : nombre d'essais dans le seuil, coût de la vérification comme borne** (3 travaux ; éprouvé selon les auteurs : oui, mesuré 1, non 2)

- What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery (2026-08-27) · 439.1
- The Verification Bottleneck (2026-11-01) · 449.1
- LLM Daydreaming (2025-07) · 472.3

**coût n° 12 — Le coût comme métrique même (efficacité de calcul) ou la montée de l'effort de test d'un juge** (2 travaux ; éprouvé selon les auteurs : oui, mesuré 2)

- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (2026-10-05) · 67.1
- TASTE: Can AI Models Judge AI Safety Research Proposals? (2026-08-28) · 258.3

**coût n° 13 — Taille d'équipe et passage à l'échelle : taille effective, temps d'achèvement, goulot de priorisation** (3 travaux ; éprouvé selon les auteurs : oui, mesuré 1, oui, affirmé 1, non 1)

- 2026-03-19 org uplift game (note) (2026-03-19) · 486.0
- Coarse-Grained Dynamics of Multi-Agent Collective AutoResearch (2026-09-19) · 509.1
- The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size (2026-05-31) · 613.0

**auto-conception n° 7 — Cadres et bancs d'évaluation des boucles d'auto-amélioration** (2 travaux ; éprouvé selon les auteurs : oui, affirmé 1, inconnu 1)

- Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks (2026-09-27) · 579.2
- Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents (2026-11-06) · 601.0

**auto-conception n° 9 — Composition de l'équipe d'agents et affectation d'un modèle par rôle** (2 travaux ; éprouvé selon les auteurs : oui, affirmé 1, inconnu 1)

- Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems (2026-10-14) · 617.0
- Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (2026-10-22) · 618.0

**auto-conception n° 10 — Entraînement des poids aux compétences d'auto-évolution, seuls ou croisés avec l'évolution du harnais** (2 travaux ; éprouvé selon les auteurs : inconnu 2)

- Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning (2026-07-24) · 597.0
- Harness Evolution Hits a Ceiling: When Weight Training Should Begin (2026-10-08) · 599.0

### 3.2 Regroupements portés à la fois par des machines et par d'autres travaux

Pour chacun : nombre de travaux hors machine (liste complète en section 1, sans la marque « machine »).

- exploration n° 1 — Idéation ancrée dans la littérature ou un graphe de connaissances : 2 travaux sous forme de machine, 11 hors machine (6, 44, 72, 147, 148, 155, 156, 157, 161, 524, 530)
- exploration n° 2 — Transfert analogique, collision de concepts et recombinaison entre domaines ou entre champs : 3 travaux sous forme de machine, 5 hors machine (158, 472, 473, 492, 533)
- exploration n° 3 — Information réduite, ignorance volontaire, regard neuf, point de départ inattendu, exploration libre sans objet désigné, directions que les chercheurs ne formuleraient pas : 1 travaux sous forme de machine, 8 hors machine (3, 159, 164, 177, 228, 444, 504, 540)
- exploration n° 5 — Population, qualité-diversité, îles, algorithmes génétiques et recherche évolutive de programmes ou d'hypothèses : 7 travaux sous forme de machine, 11 hors machine (7, 26, 35, 40, 41, 42, 140, 237, 406, 454, 623)
- exploration n° 6 — Recherche en arbre : 7 travaux sous forme de machine, 4 hors machine (138, 365, 453, 584)
- exploration n° 7 — Tirages indépendants, bifurcations, redémarrages, meilleur de N : 3 travaux sous forme de machine, 7 hors machine (394, 456, 502, 581, 582, 583, 591)
- exploration n° 8 — Équipes d'agents : 9 travaux sous forme de machine, 16 hors machine (10, 19, 22, 46, 48, 53, 127, 130, 131, 143, 178, 359, 509, 543, 571, 619)
- exploration n° 9 — Pilotage de l'exploration par la surprise, l'incertitude, les principes, le goût ou un contrôleur : 4 travaux sous forme de machine, 5 hors machine (105, 145, 170, 176, 535)
- exploration n° 10 — Mesures de l'exploration d'un run : 1 travaux sous forme de machine, 15 hors machine (1, 146, 180, 189, 191, 248, 418, 462, 463, 464, 474, 501, 522, 551, 554)
- exploration n° 12 — Remèdes à l'effondrement de la diversité, et leurs limites : 2 travaux sous forme de machine, 12 hors machine (20, 90, 101, 404, 408, 409, 507, 508, 542, 566, 614, 615)
- exploration n° 14 — Un seul agent, une seule lignée : 2 travaux sous forme de machine, 0 hors machine (aucun)
- exploration n° 15 — Résultats négatifs ou nuls sur des composants d'exploration : 1 travaux sous forme de machine, 8 hors machine (0, 32, 405, 408, 520, 569, 588, 612)
- exploration n° 17 — Exploration décrite sans mécanisme précisé par la notice : 1 travaux sous forme de machine, 4 hors machine (222, 258, 400, 429)
- originalité n° 1 — Nouveauté mesurée par distance ou direction dans un espace de plongements ou de structures ; limites de ces distances : 1 travaux sous forme de machine, 7 hors machine (0, 4, 11, 401, 413, 419, 501)
- originalité n° 2 — Nouveauté mesurée contre la littérature : 2 travaux sous forme de machine, 9 hors machine (18, 21, 59, 246, 257, 460, 531, 532, 547)
- originalité n° 3 — Nouveauté jugée par un modèle ou par des experts : 1 travaux sous forme de machine, 10 hors machine (68, 71, 77, 86, 91, 94, 253, 459, 526, 563)
- originalité n° 4 — Nouveauté comme écart de croyance ou d'a priori : 3 travaux sous forme de machine, 3 hors machine (34, 574, 623)
- épreuve n° 1 — Mondes plantés à vérité connue du constructeur : 2 travaux sous forme de machine, 15 hors machine (34, 52, 162, 164, 165, 175, 181, 193, 196, 418, 450, 489, 504, 596, 626)
- épreuve n° 4 — Exécution sous un évaluateur exécutable ou un correcteur programmé : 7 travaux sous forme de machine, 15 hors machine (10, 22, 42, 98, 167, 168, 184, 185, 229, 238, 375, 392, 393, 460, 463)
- épreuve n° 5 — Préenregistrement, engagement préalable et enregistrement des essais avant exécution ou avant les décisions : 1 travaux sous forme de machine, 9 hors machine (25, 53, 215, 416, 425, 450, 456, 563, 580)
- épreuve n° 6 — Séparer le signal qui sert à chercher de la mesure finale : 4 travaux sous forme de machine, 12 hors machine (20, 456, 545, 579, 585, 598, 600, 602, 603, 605, 606, 621)
- épreuve n° 7 — Témoins, nuls et placebos : 1 travaux sous forme de machine, 13 hors machine (85, 401, 437, 458, 546, 549, 552, 555, 558, 586, 589, 592, 612)
- épreuve n° 8 — Multiplicité et garanties statistiques : 2 travaux sous forme de machine, 11 hors machine (85, 174, 207, 210, 247, 394, 427, 511, 512, 575, 623)
- épreuve n° 9 — Audit des revendications et des artefacts contre les journaux, les preuves, les registres et les contrôles déterministes : 4 travaux sous forme de machine, 16 hors machine (32, 73, 97, 119, 180, 211, 212, 217, 227, 421, 495, 521, 534, 553, 568, 581)
- épreuve n° 15 — Épreuve décrite sans montage précisé par la notice : 1 travaux sous forme de machine, 14 hors machine (163, 170, 171, 177, 179, 182, 187, 188, 220, 223, 303, 391, 583, 590)
- jugement n° 3 — Notation d'idées ou d'articles par des juges modèles ou des relecteurs automatiques sans épreuve exécutée ; critique ou filtre modèle dans la boucle : 6 travaux sous forme de machine, 13 hors machine (44, 52, 54, 56, 80, 140, 164, 248, 375, 456, 459, 462, 472)
- jugement n° 4 — Instabilité du juge : 1 travaux sous forme de machine, 9 hors machine (14, 68, 77, 86, 117, 416, 425, 450, 557)
- jugement n° 8 — Séparation de qui propose, qui exécute et qui juge ; arbitre ou règle de décision fixés hors de l'agent : 3 travaux sous forme de machine, 5 hors machine (58, 78, 145, 167, 450)
- jugement n° 9 — Jugement ancré dans des preuves traçables, des journaux ou un audit des artefacts plutôt que dans un avis libre : 1 travaux sous forme de machine, 9 hors machine (180, 183, 193, 195, 217, 227, 490, 506, 530)
- jugement n° 10 — Humain dans la boucle : 3 travaux sous forme de machine, 3 hors machine (188, 464, 467)
- mémoire n° 1 — Oubli et vidage : 1 travaux sous forme de machine, 1 hors machine (10)
- mémoire n° 2 — Archive ou arbre de tout ce qui a été produit (agents, idées, hypothèses), relu avant de proposer : 6 travaux sous forme de machine, 8 hors machine (7, 26, 40, 54, 114, 406, 453, 581)
- mémoire n° 3 — Trajectoire ou historique de la recherche conservé et lu par le contrôleur ou le proposeur : 1 travaux sous forme de machine, 7 hors machine (20, 50, 108, 138, 152, 402, 460)
- mémoire n° 4 — État de la recherche tenu hors du modèle : 1 travaux sous forme de machine, 7 hors machine (113, 119, 143, 211, 493, 494, 514)
- mémoire n° 5 — Mémoire des échecs et des directions ratées : 3 travaux sous forme de machine, 3 hors machine (122, 129, 499)
- mémoire n° 6 — Leçons admises en mémoire seulement après test ou preuve ; garde contre les transferts négatifs : 3 travaux sous forme de machine, 2 hors machine (97, 512)
- mémoire n° 7 — Base de connaissances ou banque d'idées partagée entre agents et sessions : 5 travaux sous forme de machine, 8 hors machine (99, 106, 157, 309, 365, 375, 524, 610)
- mémoire n° 8 — Expérience accumulée structurée, distillée ou synthétisée, puis réutilisée : 5 travaux sous forme de machine, 8 hors machine (101, 109, 115, 303, 400, 454, 455, 616)
- mémoire n° 9 — Issues vérifiées et croyances gardées comme mémoire du sélecteur : 3 travaux sous forme de machine, 0 hors machine (aucun)
- mémoire n° 11 — Mesures de ce que la mémoire ou l'héritage apportent : 1 travaux sous forme de machine, 10 hors machine (98, 100, 124, 186, 456, 525, 560, 600, 609, 626)
- sélection n° 1 — Acceptation gloutonne à un pas : 3 travaux sous forme de machine, 3 hors machine (10, 456, 583)
- sélection n° 2 — Porte de validation sur une métrique distincte, tenue à l'écart ou privée ; banc de sélection ; régularisation de la sélection : 3 travaux sous forme de machine, 2 hors machine (20, 601)
- sélection n° 3 — Porte statistique valide à tout instant ou certifiée : 2 travaux sous forme de machine, 2 hors machine (578, 579)
- sélection n° 4 — Crédit par la descendance et signaux de lignée : 3 travaux sous forme de machine, 2 hors machine (608, 616)
- sélection n° 5 — Archive, population, qualité-diversité et sélection de parents : 6 travaux sous forme de machine, 2 hors machine (26, 35)
- sélection n° 6 — Sélection d'un ensemble ou d'un portefeuille ; pondération des candidats par l'évidence ou la croyance : 2 travaux sous forme de machine, 3 hors machine (90, 169, 174)
- sélection n° 7 — Tri avant exécution par un prédicteur, un critique ou un modèle de préférence entraîné : 2 travaux sous forme de machine, 9 hors machine (66, 79, 81, 96, 109, 144, 505, 515, 559)
- sélection n° 8 — Choix de la prochaine direction par une règle d'acquisition : 5 travaux sous forme de machine, 4 hors machine (50, 108, 517, 534)
- sélection n° 9 — Rejet explicite et journalisé des directions faibles ; mérite d'une hypothèse séparé de la qualité de son exécution : 1 travaux sous forme de machine, 5 hors machine (138, 152, 155, 170, 495)
- sélection n° 10 — Entraînement sur un signal différé, retour d'exécution rendu au modèle, tri en deux temps : 1 travaux sous forme de machine, 2 hors machine (151, 229)
- coût n° 1 — Filtrer avant d'exécuter : 1 travaux sous forme de machine, 9 hors machine (64, 66, 81, 88, 90, 92, 108, 515, 518)
- coût n° 2 — Allocation dynamique du budget : 4 travaux sous forme de machine, 4 hors machine (50, 502, 517, 543)
- coût n° 3 — Largeur contre profondeur à dépense totale égale : 1 travaux sous forme de machine, 6 hors machine (10, 27, 581, 582, 584, 590)
- coût n° 4 — Budget apparié et compté de bout en bout (jetons, temps, évaluations) ; le budget comme variable contrôlée de la mesure ou de la tâche : 2 travaux sous forme de machine, 7 hors machine (60, 85, 98, 171, 393, 456, 581)
- coût n° 6 — Règles d'arrêt : 1 travaux sous forme de machine, 5 hors machine (176, 212, 247, 408, 578)
- coût n° 8 — Le coût dans la sélection : 1 travaux sous forme de machine, 3 hors machine (599, 608, 618)
- coût n° 9 — Efficacité de la recherche mesurée en appels ou en essais : 2 travaux sous forme de machine, 1 hors machine (455)
- coût n° 11 — Coût total des lancements rapporté (appels, dollars, heures), sans règle d'allocation : 1 travaux sous forme de machine, 2 hors machine (54, 450)
- auto-conception n° 1 — Réécriture du code de l'agent : 3 travaux sous forme de machine, 0 hors machine (aucun)
- auto-conception n° 2 — Un méta-agent écrit de nouveaux agents en code, ou pilote la stratégie de recherche à la place d'une stratégie fixée par un humain : 2 travaux sous forme de machine, 0 hors machine (aucun)
- auto-conception n° 3 — La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration) : 3 travaux sous forme de machine, 1 hors machine (299)
- auto-conception n° 4 — Boucle d'évolution du harnais de l'agent : 2 travaux sous forme de machine, 2 hors machine (585, 587)
- auto-conception n° 5 — Contraintes et régularisation des modifications de harnais contre le surajustement aux tâches d'évolution : 1 travaux sous forme de machine, 2 hors machine (604, 605)
- auto-conception n° 6 — Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique) : 3 travaux sous forme de machine, 0 hors machine (aucun)
- auto-conception n° 8 — Composants des harnais décomposés et comparés ; résultats sans configuration supérieure partout ou sans ablation : 1 travaux sous forme de machine, 2 hors machine (27, 596)
- auto-conception n° 11 — Auto-modification annoncée, mécanisme non précisé par la notice : 2 travaux sous forme de machine, 5 hors machine (97, 103, 178, 218, 391)

## 4. Ce que l'organisme actuel fait déjà

**Cette section est remplie d'après les décisions de Lazar nommées ci-dessous, et d'elles seules** : elle dit ce que ces décisions retiennent ou interdisent, non ce que le code ou les courses ont réalisé. Plusieurs énoncés valent « à partir de l'étape 2 » ou « sur devis » ; une décision qui retient un énoncé n'est pas une mesure faite. Pièces lues, avec empreinte :

- `docs/decisions/decision-N-044-v1.md` — sha256 `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`
- `docs/decisions/decision-N-045-v2.md` — sha256 `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`
- `docs/decisions/decision-N-049-v1.md` — sha256 `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460`
- `docs/decisions/decision-N-050-v1.md` — sha256 `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58`
- `docs/decisions/decision-N-053-v1.md` — sha256 `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae`
- `docs/decisions/decision-N-058-v1.md` — sha256 `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`
- `docs/decisions/decision-N-064-v1.md` — sha256 `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97`
- `docs/decisions/decision-N-065-v1.md` — sha256 `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4`
- `docs/decisions/decision-N-067-v1.md` — sha256 `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`
- `docs/decisions/decision-resserrement-juge-au-nul-v1.md` — sha256 `9700fe6fce74840d383e3cbbf2e0f87f7914887759df3c0aa0fea687b433c184`
- `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` — sha256 `b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd`

### 4.1 Ce que les décisions disent que l'organisme est ou fait

- **Un organisme qui se conçoit seul** sur un vivier de tâches à vérité connue, avec le droit de se réécrire ; sa méta-architecture est ensuite figée, et il répond à des questions nouvelles sans réentraînement ni réorganisation (N-044, énoncé 1). L'universalité se mesure sur des familles jamais vues à la conception, non sur des items inédits des familles de conception — **distinction que N-073 interdit de présenter comme nôtre** (section 4.3).
- **Trois régimes de budget** (conception, usage, re-conception) : proposés à Lazar, en attente de son mot pour l'étape 1 (N-044, énoncé 2) ; **vivier de conception** à part de la banque scellée, identifiants disjoints du test et du test final (énoncé 3) ; le vivier existe en code dans le noyau de l'étape 1 (N-049, § 1) ; **questions ouvertes** posées aux organismes avant tout matériau, réponses archivées comme matière et jamais comme consigne (énoncé 4).
- **Diversité des candidats** : trois bras à l'étape 2 (mission avec miroir fonctionnel ; contrainte câblée ; rien), le juge étant la seule pression ; un résultat négatif se publie (N-044, énoncé 5).
- **Composition apprise** : nombre de parties, rôles, modèle par rôle (modèle de frontière ou instrument local entraîné), ordre des échanges, règle d'agrégation, mémoire transmise, part de budget (N-045 v2, énoncé 1) ; **coût dans le signal** rendu à l'organisme à côté de l'exactitude, score net gelé au préenregistrement (énoncé 2) ; **nécessité de la frontière mesurée** comme sortie, par rôle (énoncé 3) ; **voies bon marché avant la voie chère** : éliminations successives, matrices en cache, substituts à 8 milliards, affinage sur réponses filtrées ou préférences hors ligne, modèle de substitution du score, transitions depuis un tampon de rejeu, récompense dense par génération, distillation du concepteur figé (énoncé 4) ; **héritage d'une génération récompensé**, signal sur K générations avec K au moins 3 (énoncé 5 — lettre resserrée par N-073) ; **deux expériences bon marché** avant tout concepteur entraîné : pilote de bruit puis « poids contre archive » (énoncé 6) ; **espaces de conception égaux** entre concepteur contraint et libre (énoncé 7). Inchangé : les modèles de frontière ne sont jamais entraînés, la vérité du test caché ne nourrit ni l'organisme ni un concepteur (énoncé 8). Ces énoncés valent à partir de l'étape 2 ; pour les courses actuelles, l'historique servi contient déjà toutes les générations passées.
- **Tâches fraîches** : à chaque génération, la part de test tirée dans un vivier plutôt que servie fixe ; banque sœur construite d'avance par quelqu'un qui n'a lu aucun score, lue une seule fois ; confirmation sur la banque scellée, famille tenue à l'écart (N-049 ; la construction de la banque sœur est une dépense sur devis, non décidée). **Part de test final lue une seule fois, à la fin de la boucle** (N-050).
- **Composition des proposeurs jugée sur l'oracle du monde planté et sur le coût mesuré, seuls** ; le verdict du juge, aveugle à l'identité du proposeur, n'entre pas dans ce choix (N-058, point 1) ; l'invariant « aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent » vaut aussi pour l'organisme (N-053, point 5 ; N-065, point 4). La sélection des fiches par la sévérité du test survécu reste permise (N-058).
- **Juge statistique** : statistique calculée par l'orchestrateur hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois connues (l'archive), avec contrôle des comparaisons multiples (N-064) ; après N-067, **ne reste revendiqué en propre que le nul formé des lois déjà connues** (O2 resserrée, O4 seul porteur de la revendication du juge) ; après N-071, ce nul d'archive est occupé dans ses deux moitiés séparément, **seule leur réunion reste revendicable** (nul formé de l'archive entière et croissante, mis en commun et ajusté avant le gel, dans une règle de promotion à garantie valide à tout instant, sur prédictions scellées, hors des agents), et « lois prédictives et non rendements » n'est plus présenté comme une différence nette.
- **Place dans le programme** : l'organisme est un second terrain du papier C (juges de la recherche automatisée), et un atelier d'idées du programme : ses fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement scellé (N-065, rôles 1 et 2). Le banc de tricheurs et l'attaque de Goodhart du juge (revendications O11 et O12 de N-064 et N-067) relèvent d'une famille exclue de lecture de contenu pour cette pièce : **exclue** ; voir `docs/decisions/decision-N-064-v1.md` et `docs/decisions/decision-N-067-v1.md`.

### 4.2 Ce que les décisions retirent de ce qui était revendiqué comme propre (N-064, N-067, N-071)

Plus revendiqués comme propres : le recours aux e-valeurs et à un seuil posé hors des agents ; la statistique calculée hors des agents ; l'engagement scellé par empreinte ; le contrôle des comparaisons multiples ; le principe d'architecture « séparer qui propose de qui juge » (O1) ; le sceau par empreinte (O3) ; le gel avant lecture et l'interdit du repli silencieux comme idées (O17) — publiés dans leur principe ou occupés en partie, citations obligatoires dans tout texte qui présente l'organisme : POPPER, Dwork et al., Blum et Hardt (« The Ladder »), Co-Scientist, et les pièces nommées par N-067 et N-071.

### 4.3 Ce que N-073 interdit désormais de présenter comme nôtre

Lettre de `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (version de travail, contre-lecture à venir selon son texte) :

1. **Héritage d'une génération récompensé** (N-045 v2, énoncé 5) : principe occupé par la machine de Huxley-Gödel (Wang et al., arXiv 2510.21614). Ne plus écrire comme idée ou constat du programme : « récompenser l'héritage d'une génération » ; « créditer un agent par les résultats de sa descendance » ; « le score immédiat est un mauvais guide du potentiel à long terme » ; « un signal sur plusieurs générations, tronqué à K et actualisé » présenté comme une idée ; « faire compter dans le mérite d'une génération ce qu'elle construit et qui ne sert qu'aux suivantes » ; « servir tout l'historique au concepteur ». La lettre retenue cite Wang et al. (2025), Schmidhuber et Zhao (1996, 1997 — à lire sur source avant de les citer), Sutton et Barto. Restent décrits sans être dits nouveaux ni propres : les objets (mémoire transmise, sondes et adaptateurs servis à la génération suivante), le concepteur entraîné avec le coût dans le signal, la question causale « l'archive héritée cause-t-elle les découvertes ? ». Indice contraire à dire avec la prémisse : chez Qin et al. (arXiv 2611.05108), ce qui est légué rapporte surtout au départ.
2. **« Le séquentiel doit battre le meilleur de N tirages, à budget égal »** (N-045 v2, énoncés 4 et 6) : protocole occupé (Oved et al., arXiv 2610.23977 ; compagnon arXiv 2609.19799), issue occupée en partie ; les gardes de la porte (familles tenues à l'écart, témoin « un modèle, vote à k ») sont très probablement prises aussi, d'après des notices seulement. La porte reste une condition du programme, présentée comme **pratique publiée, citée**.
3. **« Familles inédites contre items inédits des familles vues »** (N-044) : distinction faite en mots propres par Srikanth et al. (arXiv 2609.26457, p. 6) ; elle se cite. Ce qui se décrit comme mise en œuvre, sans priorité : la mesure par famille préenregistrée.
4. **Banque sœur** (N-049) : elle sépare « adapté aux textes » de « adapté à la famille telle que ce générateur la rend », non de « adapté au générateur » (Zhu et al., « Bad Genius », arXiv 2609.18366, p. 5 : contredit faible) ; le générateur est audité avant toute banque sœur. La lecture unique du lot final est une pratique ancienne, citée.
5. **Proposeurs de plusieurs fournisseurs** (N-045 v2, énoncés 1 à 3 ; N-067) : l'énoncé reste « voisin » ; tout texte qui présente la diversité des fournisseurs cite l'indice contraire de Ferreira, Liu, Zheng (arXiv 2609.35875) avec sa borne de terrain (réponses fermées, petits modèles ouverts), à côté de deux autres déjà au dépôt.

Les restrictions antérieures (« lois prédictives et non rendements » ; e-valeurs ; calcul hors des agents ; sceau ; etc.) sont en 4.2. Rien dans cette section n'est une déclaration « libre » : « non trouvé dans les pièces lues » ne veut jamais dire « trou du champ » (R8).

## 5. Questions ouvertes

Ce sont des questions posées par la matière, jamais des affirmations d'absence : chacune dit ce que ce moissonnage montre et ce qu'il ne montre pas. Les comptes viennent du relevé, recalculés par programme.

1. **Regroupements sans aucun mécanisme marqué « oui, mesuré »** (13 sur 103) : exploration n° 14 (Un seul agent, une seule lignée) ; exploration n° 16 (Positions et théories de l'exploration) ; exploration n° 17 (Exploration décrite sans mécanisme précisé par la notice) ; originalité n° 7 (Absence de contrôle de nouveauté, ou débat sur sa définition) ; mémoire n° 10 (Mémoire apprise dans les poids ou par un réflecteur entraîné) ; mémoire n° 13 (Positions sur ce que doit être la mémoire d'un agent de recherche) ; sélection n° 3 (Porte statistique valide à tout instant ou certifiée) ; auto-conception n° 3 (La procédure d'amélioration est elle-même modifiable (méta-niveau, critère d'évaluation, politique d'amélioration)) ; auto-conception n° 5 (Contraintes et régularisation des modifications de harnais contre le surajustement aux tâches d'évolution) ; auto-conception n° 6 (Porte qui encadre chaque auto-modification (adaptateur et harnais versionnés, contrôles tenus à l'écart, test statistique)) ; auto-conception n° 7 (Cadres et bancs d'évaluation des boucles d'auto-amélioration) ; auto-conception n° 9 (Composition de l'équipe d'agents et affectation d'un modèle par rôle) ; auto-conception n° 10 (Entraînement des poids aux compétences d'auto-évolution, seuls ou croisés avec l'évolution du harnais). Question : ces mécanismes sont-ils éprouvés quelque part hors de ce moissonnage, et sur quelle vérité ?
2. **Éprouvé contre le réel et machines.** Parmi les travaux sous forme de machine (section 2), la part de mécanismes éprouvés « oui, mesuré » est 81 sur 176 (selon les auteurs). Question : quels mécanismes d'une machine sont isolés par une ablation, et lesquels ne sont éprouvés qu'ensemble ? (Le relevé note plusieurs cas d'absence d'ablation : indices 112 et 593.)
3. **Largeur et profondeur à budget apparié.** Le regroupement « coût n° 3 » et le regroupement « coût n° 5 » portent les comparaisons à dépense totale égale et les témoins à calcul apparié. Question : quelle part de ces comparaisons distingue le gain d'une architecture du gain d'un calcul d'inférence ajouté, sur des familles de tâches tenues à l'écart ?
4. **Vérité de l'épreuve.** Le relevé range sous « épreuve » des vérités très différentes (monde planté, futur, redécouverte, exécutable, expert). Question : un même mécanisme d'exploration garde-t-il son classement quand on change la vérité de l'épreuve, à coût égal ?
5. **Originalité.** La nouveauté se mesure par distance dans un espace, par antériorité, par juge ou par écart de croyance. Question : ces quatre mesures s'accordent-elles sur les mêmes idées, et laquelle suit un résultat réel obtenu plus tard ?
6. **Diversité.** Le relevé porte des diagnostics d'effondrement et des remèdes dont plusieurs sont notés sans effet par leurs auteurs (exploration n° 12 et n° 15). Question : quels remèdes survivent quand on juge sur l'oracle d'un monde planté et sur le coût plutôt que sur un juge de nouveauté ?
7. **Mémoire.** La mémoire se mesure surtout par comparaison « avec / sans » ; plusieurs mesures du regroupement « mémoire n° 11 » ne trouvent pas de gain constant au résultat final. Question : que lègue réellement une génération à la suivante, au départ, à mi-budget et à l'échéance, une fois l'effet de départ séparé ?
8. **Jugement.** Les juges sont mesurés contre des experts, des issues ou des preuves traçables ; plusieurs travaux du regroupement « jugement n° 6 » rapportent des erreurs corrélées entre juges modèles (selon les auteurs). Question : quelle composition d'un collège de juges garde un nombre de votes effectifs supérieur à celui d'un seul juge sur des idées de recherche ?
9. **Auto-conception.** Le relevé range des systèmes qui se réécrivent (auto-conception n° 1 à 4). D'après la lecture approfondie de l'indice 112, relayée par N-073 (§ 3), sa mesure sur une famille inédite tient en une tâche et trois graines. Question : que devient une auto-modification sélectionnée quand la famille de tâches de la mesure est inédite à la conception, avec plus de familles et de graines ?
10. **Entrées lues sur notice seule.** 163 travaux ne sont lus que par le titre ou une courte description ; leurs mécanismes (section 6) sont des hypothèses de lecture. Question : lesquels, lus sur PDF, tiennent ?
11. **Limites du moissonnage.** Une seconde passe de recherche, limitée à la périphérie du juge (finance empirique, découverte de modèles, billets de laboratoire), est accordée par N-073 (§ 7) après le 22 novembre 2026 ; les voisins nommés par N-073 à lire sur PDF ne le sont pas encore. Les lectures approfondies des travaux d'indices 605, 612 et 625 n'ont pas été ouvertes pour cette pièce.

## 6. Mécanismes suggérés par le titre (comptés à part)

207 mécanismes dont la phrase du relevé dit qu'ils sont inférés du seul titre ou d'après le titre. Ce sont des hypothèses de lecture : ni description des auteurs, ni mesure. Par famille : exploration 59 ; originalité 11 ; épreuve 47 ; jugement 24 ; mémoire 16 ; sélection 3 ; coût 9 ; auto-conception 27 ; autre 11.

### exploration (59)

- EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery (2025-12-15) — https://arxiv.org/abs/2512.13857 — 232.0 — inconnu — lecture : notice seule — Évolution de programmes guidée par un modèle de langue, en qualité-diversité, avec plusieurs variantes gardées dans une représentation en graphe (d'après le titre seul).
- ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution (2025-09-17) — https://arxiv.org/abs/2509.19349 — 236.0 — inconnu — lecture : notice seule — Évolution de programmes ouverte, guidée par des modèles, visant l'économie d'échantillons (d'après le titre seul).
- Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas (2024-10-18) — https://arxiv.org/abs/2410.14255 — 250.0 — inconnu — lecture : notice seule — Planification et recherche itératives pour augmenter la nouveauté et la diversité des idées générées (d'après le titre) ; mécanisme non précisé par la notice.
- Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents (2024-10-17) — https://arxiv.org/abs/2410.13185 — 251.0 — inconnu — lecture : notice seule — Développement d'idées nouvelles par des agents, organisé en « chaîne d'idées » (d'après le titre) ; mécanisme non précisé par la notice.
- Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System (2024-10-12) — https://arxiv.org/abs/2410.09403 — 252.0 — inconnu — lecture : notice seule — Génération d'idées scientifiques par un système de plusieurs agents, annoncé meilleur qu'un agent seul (d'après le titre) ; rôles non précisé par la notice.
- ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models (2024-04-11) — https://arxiv.org/abs/2404.07738 — 255.0 — inconnu — lecture : notice seule — Génération itérative d'idées de recherche appuyée sur la littérature scientifique (d'après le titre) ; mécanisme non précisé par la notice.
- Homogenization Effects of Large Language Models on Human Creative Ideation (2024-02-02) — https://arxiv.org/abs/2402.01536 — 256.0 — inconnu — lecture : notice seule — Constat annoncé d'une homogénéisation de l'idéation créative humaine quand elle s'appuie sur des modèles de langue (d'après le titre) : un risque pour la diversité, non un mécanisme de recherche ; mesure non précisé par la notice.
- SciMON: Scientific Inspiration Machines Optimized for Novelty (2023-05-23) — https://arxiv.org/abs/2305.14259 — 257.1 — inconnu — lecture : notice seule — Génération d'idées par inspiration tirée de la littérature, optimisée pour la nouveauté (d'après le titre) ; mécanisme non précisé par la notice.
- LLM-Guided Open Hypothesis Learning from Autonomous Scanning Probe Microscopy Experiments (2026-05-07) — https://arxiv.org/abs/2605.06839 — 270.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (apprentissage d'hypothèses « ouvert », guidé par un modèle de langue) ; mécanisme non précisé par la notice.
- AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents (2026-05-12) — https://arxiv.org/abs/2605.11732 — 272.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (rôles séparés puis collaboration entre agents de recherche documentaire approfondie ouverte) ; mécanisme non précisé par la notice.
- Multi-agent AI systems outperform human teams in creativity (2026-05-18) — https://arxiv.org/abs/2605.17885 — 276.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (systèmes à plusieurs agents comparés à des équipes humaines sur la créativité) ; mécanisme non précisé par la notice.
- Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine (2026-05-18) — https://arxiv.org/abs/2605.18144 — 277.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération d'hypothèses par agents à partir de cette carte) ; mécanisme non précisé par la notice.
- Claw AI Lab: An Autonomous Multi-Agent Research Team (2026-05-21) — https://arxiv.org/abs/2605.22662 — 281.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (équipe de recherche autonome à plusieurs agents, donc à rôles) ; mécanisme non précisé par la notice.
- Multi-Persona Debate System for Automated Scientific Hypothesis Generation (2026-04-14) — https://arxiv.org/abs/2605.23917 — 283.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (débat entre plusieurs personas pour engendrer des hypothèses scientifiques) ; mécanisme non précisé par la notice.
- Influence-Guided Symbolic Regression: Scientific Discovery via LLM-Driven Equation Search with Granular Feedback (2026-05-27) — https://arxiv.org/abs/2605.29184 — 286.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche d'équations conduite par un modèle de langue) ; mécanisme non précisé par la notice.
- MOOSE-Copilot: A Web-Based Interactive Assistant for Unified Exploratory and Fine-Grained Scientific Hypothesis Discovery (2026-05-28) — https://arxiv.org/abs/2605.29475 — 287.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (assistant interactif qui unirait découverte d'hypothèses exploratoire et découverte à grain fin) ; mécanisme non précisé par la notice.
- Conditional Hypothesis Generation for LLM-Based Text Analysis with Researcher-Specified Covariates (2026-06-02) — https://arxiv.org/abs/2606.03029 — 289.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération d'hypothèses conditionnée à des covariables fixées par le chercheur, pour l'analyse de textes) ; mécanisme non précisé par la notice.
- Deliberate Evolution: Agentic Reasoning for Sample-Efficient Symbolic Regression with LLMs (2026-06-03) — https://arxiv.org/abs/2606.04360 — 290.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution « délibérée » par raisonnement d'agents, en régression symbolique) ; mécanisme non précisé par la notice.
- MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery (2026-06-04) — https://arxiv.org/abs/2606.06473 — 291.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte d'algorithmes d'apprentissage automatique par évolution) ; mécanisme non précisé par la notice.
- FunctionEvolve: Structure-Guided Symbolic Regression with LLMs (2026-06-05) — https://arxiv.org/abs/2606.07704 — 292.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (régression symbolique guidée par la structure, avec des modèles de langue) ; mécanisme non précisé par la notice.
- Socratic agents for autonomous scientific discovery in high-dimensional physical systems (2026-06-25) — https://arxiv.org/abs/2606.26722 — 298.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents « socratiques », donc à questionnement, pour la découverte dans des systèmes physiques de grande dimension) ; mécanisme non précisé par la notice.
- One Reflection Is Not Enough: Self-Correcting Autonomous Research via Multi-Hypothesis Failure Attribution (2026-06-30) — https://arxiv.org/abs/2606.31478 — 301.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (plusieurs hypothèses d'explication de l'échec tenues en parallèle) ; mécanisme non précisé par la notice.
- Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination (2026-07-01) — https://arxiv.org/abs/2607.00924 — 302.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération d'hypothèses par recombinaison de concepts sur un graphe, pilotée par apprentissage par renforcement) ; mécanisme non précisé par la notice.
- EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation (2026-07-02) — https://arxiv.org/abs/2607.01584 — 304.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (chaîne de trois agents à rôles distincts pour produire des hypothèses en observation de la Terre) ; mécanisme non précisé par la notice.
- AutoResearch: An Execution-Grounded Multi-Agent Framework for Reliable Research Workflow Automation (2026-05-04) — https://arxiv.org/abs/2607.02520 — 305.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cadre à plusieurs agents) ; mécanisme non précisé par la notice.
- Language models guide symbolic equation discovery by controlling search (2026-07-05) — https://arxiv.org/abs/2607.04156 — 307.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le modèle de langue guiderait la découverte d'équations symboliques en pilotant la recherche elle-même plutôt qu'en proposant directement les équations) ; mécanisme non précisé par la notice.
- ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes (2026-07-05) — https://arxiv.org/abs/2607.04439 — 308.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (suite de compétences d'idéation de recherche) ; mécanisme non précisé par la notice.
- Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation (2026-07-09) — https://arxiv.org/abs/2607.08758 — 309.1 — inconnu — lecture : page ou résumé — Génération d'idées appuyée sur la filiation (« lineage-grounded », d'après le titre et le résumé) ; la façon dont la filiation guide la génération est non précisée par la notice.
- GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization (2026-07-11) — https://arxiv.org/abs/2607.10127 — 310.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution augmentée par un graphe pour la découverte scientifique) ; mécanisme non précisé par la notice.
- LLM-PDESR: Robust PDE Discovery via Subdomain Weighted Residuals and LLM-Guided Symbolic Hypothesis Generation (2026-07-12) — https://arxiv.org/abs/2607.10546 — 311.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (hypothèses symboliques d'équations aux dérivées partielles proposées par un modèle de langue) ; mécanisme non précisé par la notice.
- Automatic Ordinary Differential Equations Discovery For Biological Systems Using Large Language Model Powered Agentic System (2026-07-15) — https://arxiv.org/abs/2607.13608 — 313.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (système d'agents qui découvre des équations différentielles ordinaires pour des systèmes biologiques) ; mécanisme non précisé par la notice.
- ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System (2026-07-15) — https://arxiv.org/abs/2607.14178 — 314.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (système à plusieurs agents appuyé sur une base de connaissances, pour la découverte par raisonnement en mathématiques appliquées) ; mécanisme non précisé par la notice.
- Autonomous mechanistic discovery of colorectal cancer vulnerabilities via multi-scale AI swarms (2026-06-28) — https://arxiv.org/abs/2607.16262 — 315.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (essaims d'agents à plusieurs échelles pour la découverte autonome de mécanismes de vulnérabilité du cancer colorectal) ; mécanisme non précisé par la notice.
- MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models (2026-05-08) — https://arxiv.org/abs/2607.18249 — 316.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (système à plusieurs agents guidé par un modèle de langue) ; mécanisme non précisé par la notice.
- HALO: Interactive Co-abductive Reasoning in Scientific Hypothesis Generation (2026-07-20) — https://arxiv.org/abs/2607.18564 — 317.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (raisonnement abductif mené conjointement et de façon interactive, vraisemblablement entre l'humain et le modèle, pour produire des hypothèses) ; mécanisme non précisé par la notice.
- AI and Its Impact on Creativity and Diversity: An Empirical Study of LLM-Generated Product Ideas (2026-07-30) — https://arxiv.org/abs/2607.27553 — 321.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (effet du modèle de langue sur la diversité d'un ensemble d'idées) ; mécanisme non précisé par la notice.
- Abduction Without a Body? Representational Grounding and the Abduction Loop for Scientific Hypothesis Generation (2026-08-03) — https://arxiv.org/abs/2608.02505 — 325.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (abduction comme mode de génération d'hypothèses) ; mécanisme non précisé par la notice.
- AgentPanel: Toward a New Paradigm for Human--AI Collaboration in Exploring Scientific Questions (2026-08-04) — https://arxiv.org/abs/2608.03283 — 326.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (panel d'agents en collaboration avec l'humain pour explorer des questions scientifiques) ; mécanisme non précisé par la notice.
- A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination (2026-08-05) — https://arxiv.org/abs/2608.04872 — 329.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (coordination hiérarchique d'agents pour chercher des expressions symboliques) ; mécanisme non précisé par la notice.
- Project2Task: Graph-Guided Project-Level Planning for Autonomous Research (2026-08-05) — https://arxiv.org/abs/2608.05225 — 330.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (planification d'un projet de recherche autonome guidée par un graphe, du projet vers les tâches) ; mécanisme non précisé par la notice.
- MBA: Multimodal Benchmark and Agents for Real-World Business Ideation (2026-08-12) — https://arxiv.org/abs/2608.11616 — 333.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents d'idéation d'affaires accompagnant le banc d'essai) ; mécanisme non précisé par la notice.
- Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery (2026-08-19) — https://arxiv.org/abs/2608.19047 — 340.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (répartition des rôles entre agents décidée par tâche) ; mécanisme non précisé par la notice.
- Hallucination as a Feature, not a Defect: Evaluating a multi-agent architecture to transform speculative language-model outputs into testable scientific hypotheses (2026-06-11) — https://arxiv.org/abs/2608.19206 — 341.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (les sorties spéculatives du modèle, d'ordinaire traitées comme des erreurs, servent de source d'idées) ; mécanisme non précisé par la notice.
- HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning (2026-08-26) — https://arxiv.org/abs/2608.25770 — 345.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération automatisée d'hypothèses par plusieurs agents) ; mécanisme non précisé par la notice.
- MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry (2026-08-28) — https://arxiv.org/abs/2608.28315 — 347.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération adaptative d'hypothèses) ; mécanisme non précisé par la notice.
- Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents (2026-09-01) — https://arxiv.org/abs/2609.01294 — 349.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche guidée par des hypothèses, où l'agent explore plusieurs pistes avant de s'engager sur une seule) ; mécanisme non précisé par la notice.
- LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28 (2026-09-04) — https://arxiv.org/abs/2609.05093 — 351.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution de programmes guidée par un modèle de langue, appliquée à l'empilement de cercles) ; mécanisme non précisé par la notice.
- Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis (2026-09-26) — https://arxiv.org/abs/2609.32746 — 362.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte symbolique par plusieurs agents, appliquée à l'analyse financière fondamentale) ; mécanisme non précisé par la notice.
- RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models (2026-09-30) — https://arxiv.org/abs/2609.39551 — 366.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc de recherche automatique à plusieurs agents qui fait évoluer des modèles de classement) ; mécanisme non précisé par la notice.
- EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution (2026-10-03) — https://arxiv.org/abs/2610.04517 — 367.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de recherche autonomes qui font évoluer par itérations des architectures de prévision) ; mécanisme non précisé par la notice.
- SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm (2026-10-14) — https://arxiv.org/abs/2610.20431 — 376.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (essaim, donc population d'agents ; règle d'évolution non dite) ; mécanisme non précisé par la notice.
- MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery (2026-10-17) — https://arxiv.org/abs/2610.24454 — 377.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (coordination hiérarchique des agents, donc répartition de rôles) ; mécanisme non précisé par la notice.
- NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research (2026-10-18) — https://arxiv.org/abs/2610.25211 — 379.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche autonome à double boucle appliquée à l'analyse et au décodage d'électroencéphalogrammes ; rôle de chaque boucle non dit) ; mécanisme non précisé par la notice.
- Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures (2026-10-20) — https://arxiv.org/abs/2610.28887 — 380.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (équipes de chercheurs artificiels, donc rôles, pour la découverte autonome d'architectures d'attention linéaire) ; mécanisme non précisé par la notice.
- SplatLab: Autonomous Scientific Discovery for 3DGS Research (2026-10-21) — https://arxiv.org/abs/2610.30468 — 381.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte scientifique autonome appliquée à la recherche sur le rendu par éclats gaussiens en trois dimensions) ; mécanisme non précisé par la notice.
- Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery (2026-10-23) — https://arxiv.org/abs/2610.32195 — 383.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (passage, au moment de l'inférence, d'hypothèses à la construction de principes pour la découverte scientifique) ; mécanisme non précisé par la notice.
- PACE: Research Proving Agent for Adaptive Conjecture Exploration (2026-10-24) — https://arxiv.org/abs/2610.33690 — 386.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agent de preuve qui explore des conjectures de façon adaptative) ; mécanisme non précisé par la notice.
- Creative Priming: Decoupling Process from Product to Escape the Creative Paradox (2026-11-09) — https://arxiv.org/abs/2611.11740 — 411.0 — inconnu — lecture : notice seule — Amorçage créatif : découpler le processus du produit pour échapper au « paradoxe créatif » (d'après le titre) ; le mécanisme est non précisé par la notice.
- FlowPIE: Test-Time Scientific Idea Evolution with Flow-Guided Literature Exploration (2026-08-30) — https://openreview.net/forum?id=L4yt1ihvmb — 539.0 — oui, mesuré — lecture : page ou résumé — Couple récupération de littérature et génération pour faire évoluer des idées au moment de l'inférence, l'exploration de la littérature étant guidée par un flot (d'après le titre) ; opérateur d'évolution non précisé par la notice.

### originalité (11)

- LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models (2025-04-14) — https://arxiv.org/abs/2504.10415 — 199.0 — inconnu — lecture : notice seule — Banc de découverte d'équations conçu contre la mémorisation, d'après le titre seul ; procédé non précisé par la notice.
- Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine (2026-05-18) — https://arxiv.org/abs/2605.18144 — 277.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cartographie de la frontière des connaissances appuyée sur des preuves, en nanomédecine) ; mécanisme non précisé par la notice.
- SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs (2026-05-29) — https://arxiv.org/abs/2605.30711 — 288.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (porte de nouveauté filtrant ce qui entre dans la mémoire) ; mécanisme non précisé par la notice.
- Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination (2026-07-01) — https://arxiv.org/abs/2607.00924 — 302.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (hypothèses « traçables » : le chemin de concepts qui mène à l'idée resterait lisible) ; mécanisme non précisé par la notice.
- Plato-Bio: verification-first biological novelty screening with temporal rediscovery and structural benchmarks (2026-07-27) — https://arxiv.org/abs/2607.23975 — 319.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (criblage de la nouveauté en biologie qui commence par la vérification, avec des bancs de redécouverte temporelle — retrouver ce qui a été publié après une date de coupure — et des bancs structurels) ; mécanisme non précisé par la notice.
- AI and Its Impact on Creativity and Diversity: An Empirical Study of LLM-Generated Product Ideas (2026-07-30) — https://arxiv.org/abs/2607.27553 — 321.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (étude empirique de la créativité et de la diversité d'idées de produits générées par des modèles de langue) ; mécanisme non précisé par la notice.
- Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs (2026-08-07) — https://arxiv.org/abs/2608.06967 — 331.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (mesure de l'idéation créative visuelle de modèles de langue sans vision ; il s'agit d'une mesure de créativité, pas d'un mécanisme de recherche d'idées) ; mécanisme non précisé par la notice.
- MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry (2026-08-28) — https://arxiv.org/abs/2608.28315 — 347.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (ancrage des hypothèses dans la littérature) ; mécanisme non précisé par la notice.
- HypoKG: Evidence-Disciplined Biomedical Hypothesis Generation Beyond Endpoint Knowledge (2026-09-10) — https://arxiv.org/abs/2609.12260 — 355.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (« au-delà de la connaissance du point d'arrivée » : le titre suggère une garde contre la fuite de la réponse déjà connue vers l'hypothèse engendrée) ; mécanisme non précisé par la notice.
- Not Every Term Adds New Structure: Sobolev Novelty for Symbolic Regression (2026-09-26) — https://arxiv.org/abs/2609.32597 — 361.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (mesure de nouveauté dite de Sobolev pour la régression symbolique, selon laquelle un terme ajouté n'apporte pas toujours de structure nouvelle) ; mécanisme non précisé par la notice.
- Can large language models generate novel scientific ideas? A comprehensive study on data-driven astronomy (2026-06-18) — non relevée (entrée de Semantic Scholar sans identifiant arXiv) — 414.0 — inconnu — lecture : notice seule — Étude de la nouveauté des idées scientifiques produites par des modèles en astronomie guidée par les données (d'après le titre) ; la mesure de la nouveauté est non précisé par la notice.

### épreuve (47)

- SLDBench v2: Active Scaling Law Discovery (2026-10-12) — https://arxiv.org/abs/2610.16297 — 173.0 — inconnu — lecture : page ou résumé — Découverte active de lois d'échelle par agents, seconde version d'un banc existant (d'après le titre et la notice de la table) ; le choix des mesures demandées avant d'énoncer la loi est une lecture du mot « active » du titre, non une affirmation de la notice ; notation non précisée par la notice.
- FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games (2026-06-03) — https://arxiv.org/abs/2606.04751 — 191.0 — inconnu — lecture : page ou résumé — Jeux de découverte de règles à vérité connue du constructeur : l'agent propose des essais pour confirmer ou réfuter ses hypothèses sur une règle cachée (falsification, d'après le titre et la notice).
- Can Language Models Discover Scaling Laws? (2025-07-27) — https://arxiv.org/abs/2507.21184 — 197.0 — inconnu — lecture : notice seule — Découverte de lois d'échelle par des modèles de langue, d'après le titre seul ; mécanisme non précisé par la notice.
- LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models (2025-04-14) — https://arxiv.org/abs/2504.10415 — 199.1 — inconnu — lecture : notice seule — Les équations proposées sont confrontées à des équations de référence, d'après le titre seul ; notation non précisée par la notice.
- The Station: An Open-World Environment for AI-Driven Discovery (2025-11-09) — https://arxiv.org/abs/2511.06309 — 234.0 — inconnu — lecture : notice seule — Environnement ouvert (« monde ouvert ») pour la découverte conduite par des modèles (d'après le titre seul) ; mécanismes non précisés par la notice.
- ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition (2025-03-27) — https://arxiv.org/abs/2503.21248 — 242.0 — inconnu — lecture : notice seule — Banc de découverte scientifique décomposée en tâches selon l'inspiration (d'après le titre) ; mécanisme non précisé par la notice.
- LLM-Guided Open Hypothesis Learning from Autonomous Scanning Probe Microscopy Experiments (2026-05-07) — https://arxiv.org/abs/2605.06839 — 270.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (hypothèses apprises à partir d'expériences autonomes de microscopie à sonde locale) ; mécanisme non précisé par la notice.
- Beyond AI as Assistants: Toward Autonomous Discovery in Cosmology (2026-05-14) — https://arxiv.org/abs/2605.14791 — 274.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte autonome en cosmologie, au-delà du rôle d'assistant) ; mécanisme non précisé par la notice.
- MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility (2026-05-15) — https://arxiv.org/abs/2605.16616 — 275.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc de reproduction de résultats d'apprentissage automatique par des systèmes de recherche autonomes) ; mécanisme non précisé par la notice.
- Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators (2026-05-21) — https://arxiv.org/abs/2605.22343 — 280.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (thèse du titre : la recherche autonome a besoin de harnais d'essai et d'erreur, pas de générateurs d'articles) ; mécanisme non précisé par la notice.
- LLM-AutoSciLab: Closed-Loop Scientific Discovery via Active Experimentation with LLMs (2026-05-21) — https://arxiv.org/abs/2605.24043 — 284.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte en boucle fermée par expérimentation active conduite par des modèles de langue) ; mécanisme non précisé par la notice.
- Influence-Guided Symbolic Regression: Scientific Discovery via LLM-Driven Equation Search with Granular Feedback (2026-05-27) — https://arxiv.org/abs/2605.29184 — 286.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (régression symbolique, donc ajustement d'équations à des données) ; mécanisme non précisé par la notice.
- Deterministic Integrity Gates for LLM-Assisted Clinical Manuscript Preparation: An Auditable Biomedical Informatics Architecture (2026-06-08) — https://arxiv.org/abs/2606.09500 — 293.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (portes d'intégrité déterministes et auditables dans la préparation de manuscrits cliniques assistée par modèle de langue) ; mécanisme non précisé par la notice.
- The Calibration Turn in AI-Assisted Research: A Conceptual and Methodological Framework for Evidence-Licensed Claims (2026-06-30) — https://arxiv.org/abs/2606.31273 — 300.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cadre conceptuel et méthodologique où une affirmation de recherche assistée n'est permise que dans la mesure des preuves qui l'appuient) ; mécanisme non précisé par la notice.
- One Reflection Is Not Enough: Self-Correcting Autonomous Research via Multi-Hypothesis Failure Attribution (2026-06-30) — https://arxiv.org/abs/2606.31478 — 301.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche autonome qui se corrige en attribuant un échec à plusieurs hypothèses de cause concurrentes plutôt qu'à une seule réflexion) ; mécanisme non précisé par la notice.
- AutoResearch: An Execution-Grounded Multi-Agent Framework for Reliable Research Workflow Automation (2026-05-04) — https://arxiv.org/abs/2607.02520 — 305.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (automatisation du travail de recherche « ancrée dans l'exécution » : les étapes seraient appuyées sur du code réellement exécuté) ; mécanisme non précisé par la notice.
- Language models guide symbolic equation discovery by controlling search (2026-07-05) — https://arxiv.org/abs/2607.04156 — 307.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte d'équations, donc en principe ajustement à des données) ; mécanisme non précisé par la notice.
- LLM-PDESR: Robust PDE Discovery via Subdomain Weighted Residuals and LLM-Guided Symbolic Hypothesis Generation (2026-07-12) — https://arxiv.org/abs/2607.10546 — 311.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (équations confrontées aux données par des résidus pondérés par sous-domaine, pour la robustesse) ; mécanisme non précisé par la notice.
- Automatic Ordinary Differential Equations Discovery For Biological Systems Using Large Language Model Powered Agentic System (2026-07-15) — https://arxiv.org/abs/2607.13608 — 313.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte d'équations, donc en principe ajustement à des données biologiques) ; mécanisme non précisé par la notice.
- MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models (2026-05-08) — https://arxiv.org/abs/2607.18249 — 316.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents qui raisonnent sur des modèles métaboliques à contraintes à l'échelle du génome, c'est-à-dire sur un simulateur mécaniste) ; mécanisme non précisé par la notice.
- CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference (2026-07-24) — https://arxiv.org/abs/2607.22511 — 318.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche automatisée en inférence causale « formellement fondée ») ; mécanisme non précisé par la notice.
- LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents (2026-07-30) — https://arxiv.org/abs/2607.27690 — 322.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de laboratoire humide « ancrés », donc en principe confrontés à des expériences réelles) ; mécanisme non précisé par la notice.
- Abduction Without a Body? Representational Grounding and the Abduction Loop for Scientific Hypothesis Generation (2026-08-03) — https://arxiv.org/abs/2608.02505 — 325.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (boucle d'abduction et question de l'ancrage des représentations dans le réel pour la génération d'hypothèses) ; mécanisme non précisé par la notice.
- EviGraph: Evidence-Guided Autonomous Research Agents (2026-08-05) — https://arxiv.org/abs/2608.04738 — 328.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de recherche autonomes guidés par les preuves, vraisemblablement organisées en graphe) ; mécanisme non précisé par la notice.
- A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination (2026-08-05) — https://arxiv.org/abs/2608.04872 — 329.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (régression symbolique, donc en principe ajustement à des données) ; mécanisme non précisé par la notice.
- AQuA: Recursively Self-Improving Quantitative Trading Research Agents (2026-08-13) — https://arxiv.org/abs/2608.12841 — 334.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le domaine, des stratégies de marché, laisse supposer une épreuve chiffrée sur des données de marché, ce que le titre ne dit pas) ; mécanisme non précisé par la notice.
- AutoResearch: Insight In, Hallucination Out (2026-08-18) — https://arxiv.org/abs/2608.17906 — 339.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (boucle de recherche automatisée qui chercherait à garder les apports réels et à écarter les affirmations inventées ; on ne sait pas par quel contrôle) ; mécanisme non précisé par la notice.
- Hallucination as a Feature, not a Defect: Evaluating a multi-agent architecture to transform speculative language-model outputs into testable scientific hypotheses (2026-06-11) — https://arxiv.org/abs/2608.19206 — 341.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (une architecture à plusieurs agents transforme ces spéculations en hypothèses testables ; le titre annonce une évaluation de cette architecture, pas l'exécution des tests) ; mécanisme non précisé par la notice.
- AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement (2026-08-20) — https://arxiv.org/abs/2608.20318 — 343.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (un banc d'essai suppose une note exécutée par tâche, ce que le titre ne détaille pas) ; mécanisme non précisé par la notice.
- HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning (2026-08-26) — https://arxiv.org/abs/2608.25770 — 345.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (mise à l'épreuve automatisée des hypothèses engendrées) ; mécanisme non précisé par la notice.
- HyGRAIL: Cost-Aware and Evidence-Grounded Scientific Hypothesis Discovery over Knowledge Graphs (2026-09-02) — https://arxiv.org/abs/2609.02056 — 350.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (hypothèses ancrées dans des preuves tirées du graphe ; ancrage documentaire, pas expérience exécutée d'après le titre) ; mécanisme non précisé par la notice.
- LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28 (2026-09-04) — https://arxiv.org/abs/2609.05093 — 351.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (dix records d'un classement public d'empilements seraient battus : la note d'un empilement se calcule exactement, c'est un oracle) ; mécanisme non précisé par la notice.
- Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System (2026-09-10) — https://arxiv.org/abs/2609.10922 — 353.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de recherche autonomes appliqués à un système de recommandation à l'échelle industrielle, ce qui laisse supposer une épreuve sur des métriques réelles de production, que le titre ne dit pas) ; mécanisme non précisé par la notice.
- HypoKG: Evidence-Disciplined Biomedical Hypothesis Generation Beyond Endpoint Knowledge (2026-09-10) — https://arxiv.org/abs/2609.12260 — 355.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération d'hypothèses biomédicales « disciplinée par les preuves », sur un graphe de connaissances) ; mécanisme non précisé par la notice.
- AutoPDEBench: Benchmarking LLM Auto-Research for Neural PDE Solver Design (2026-09-26) — https://arxiv.org/abs/2609.32245 — 360.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai de la recherche automatique par modèles de langue, appliquée à la conception de solveurs neuronaux d'équations aux dérivées partielles) ; mécanisme non précisé par la notice.
- DISCERN: Can AI Agents Work Like Scientists and Guide Discovery? (2026-09-27) — https://arxiv.org/abs/2609.33357 — 363.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évaluation de la capacité d'agents à travailler comme des scientifiques et à guider la découverte) ; mécanisme non précisé par la notice.
- RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models (2026-09-30) — https://arxiv.org/abs/2609.39551 — 366.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le titre revendique la fiabilité du banc ; ce qui la garantit n'est pas dit) ; mécanisme non précisé par la notice.
- EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution (2026-10-03) — https://arxiv.org/abs/2610.04517 — 367.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le titre revendique la fiabilité des agents ; ce qui la garantit n'est pas dit) ; mécanisme non précisé par la notice.
- MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training (2026-10-04) — https://arxiv.org/abs/2610.05398 — 368.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai de la recherche autonome sur l'entraînement complémentaire de modèles multimodaux) ; mécanisme non précisé par la notice.
- EvoBelief: Falsifiable World Models for Self-Improving LLM Agents (2026-10-08) — https://arxiv.org/abs/2610.12789 — 372.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (modèles du monde réfutables — croyances que l'agent expose à la réfutation — pour des agents qui s'améliorent eux-mêmes) ; mécanisme non précisé par la notice.
- AI-Assisted Tumor-Growth Law Discovery from Sparse Data: Refitting and LLM-Based Ranking (2026-10-12) — https://arxiv.org/abs/2610.16891 — 373.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte de lois de croissance tumorale à partir de données rares, avec réajustement des lois candidates sur les données) ; mécanisme non précisé par la notice.
- Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks (2026-10-18) — https://arxiv.org/abs/2610.25069 — 378.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'évaluation d'agents de recherche automatique sur des tâches médicales réelles) ; mécanisme non précisé par la notice.
- PACE: Research Proving Agent for Adaptive Conjecture Exploration (2026-10-24) — https://arxiv.org/abs/2610.33690 — 386.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (la preuve mathématique comme mise à l'épreuve des conjectures) ; mécanisme non précisé par la notice.
- SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery (2026-11-09) — https://arxiv.org/abs/2611.12552 — 389.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte scientifique en boucle fermée, donc expériences dont les résultats reviennent au système) ; mécanisme non précisé par la notice.
- Operator Packages, Proposer Strength, and Construction-Family Plateaus in Office-Scale Verified Search (2026-08-28) — https://arxiv.org/abs/2609.29636 — 405.1 — inconnu — lecture : page ou résumé — La boucle étudiée est une recherche « vérifiée » (d'après le titre) : les candidats passent un vérificateur ; sa nature est non précisé par la notice.
- BackTrend: Evaluating Scientific Weak-Signal Prediction via Backward Reconstruction (2026-09-21) — https://arxiv.org/abs/2609.24921 — 417.0 — inconnu — lecture : notice seule — Évalue la prédiction de signaux faibles scientifiques par reconstruction à rebours (d'après le titre) ; le protocole est non précisé par la notice.
- BAITBENCH (EMNLP 2026 Findings, 2477) (2026) — https://aclanthology.org/2026.findings-emnlp.2477.pdf — 627.0 — inconnu — lecture : notice seule — Raccourcis exploitables plantés dans des tâches tabulaires synthétiques pour dire si un gain rapporté est réel ; l'écart entre score public et score tenu à l'écart sert de vérité sur le gain (d'après le titre et la page de recherche seulement ; non lu).

### jugement (24)

- Training AI Co-Scientists Using Rubric Rewards (2025-12-29) — https://arxiv.org/abs/2512.23707 — 231.0 — inconnu — lecture : notice seule — Entraînement de co-scientifiques par des récompenses tirées d'une grille de notation (d'après le titre seul) ; qui remplit la grille est non précisé par la notice.
- GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation (2025-03-16) — https://arxiv.org/abs/2503.12600 — 244.0 — inconnu — lecture : notice seule — Évaluation d'idées par un cadre léger à base de graphe et de modèle de langue (d'après le titre) ; construction du graphe non précisé par la notice.
- IdeaBench: Benchmarking Large Language Models for Research Idea Generation (2024-10-31) — https://arxiv.org/abs/2411.02429 — 249.0 — inconnu — lecture : notice seule — Banc d'évaluation de la génération d'idées de recherche par des modèles de langue (d'après le titre) ; mécanisme non précisé par la notice.
- Multi-agent AI systems outperform human teams in creativity (2026-05-18) — https://arxiv.org/abs/2605.17885 — 276.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (comparaison de créativité entre systèmes et équipes humaines ; le juge n'est pas nommé) ; mécanisme non précisé par la notice.
- Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents? (2026-05-18) — https://arxiv.org/abs/2605.19196 — 278.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (fiabilité des juges modèles de langue pour des agents de recherche appuyés sur des preuves) ; mécanisme non précisé par la notice.
- Automated Creativity Evaluation of Language Models Across Open-Ended Tasks (2026-06-10) — https://arxiv.org/abs/2606.11762 — 294.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évaluation automatisée de la créativité de modèles de langue sur des tâches ouvertes) ; mécanisme non précisé par la notice.
- SciText2Eq: Assessing LLMs for Explainable Equation Generation for Scientific Creativity (2026-06-14) — https://arxiv.org/abs/2606.16003 — 295.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évaluation de modèles de langue sur la génération d'équations explicables, rattachée à la créativité scientifique) ; mécanisme non précisé par la notice.
- PaperClaw: Harnessing Agents for Autonomous Research and Human-in-the-Loop Refinement (2026-06-21) — https://arxiv.org/abs/2606.22610 — 296.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (affinage par un humain dans la boucle d'une recherche conduite par agents) ; mécanisme non précisé par la notice.
- The Calibration Turn in AI-Assisted Research: A Conceptual and Methodological Framework for Evidence-Licensed Claims (2026-06-30) — https://arxiv.org/abs/2606.31273 — 300.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (« tournant de l'étalonnage » : la confiance accordée aux affirmations serait étalonnée sur les preuves) ; mécanisme non précisé par la notice.
- ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes (2026-07-05) — https://arxiv.org/abs/2607.04439 — 308.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (idéation appuyée sur les issues de conférences d'apprentissage automatique, c'est-à-dire sur des verdicts passés de relecteurs) ; mécanisme non précisé par la notice.
- Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists (2026-07-13) — https://arxiv.org/abs/2607.11079 — 312.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai qui mesure par capacité si les modèles de langue sont prêts pour la découverte scientifique) ; mécanisme non précisé par la notice.
- RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement (2026-07-28) — https://arxiv.org/abs/2607.25886 — 320.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai : mesure d'une capacité de recherche) ; mécanisme non précisé par la notice.
- Can AI Evaluate AI Scientists? A Benchmarking Study of Autonomous Research Generation Systems Using Automated Multi-Model Review (2026-04-18) — https://arxiv.org/abs/2607.28631 — 324.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (étude comparative de systèmes de génération autonome de recherche, évalués par une relecture automatisée à plusieurs modèles ; question posée de la validité de ce juge) ; mécanisme non précisé par la notice.
- AgentPanel: Toward a New Paradigm for Human--AI Collaboration in Exploring Scientific Questions (2026-08-04) — https://arxiv.org/abs/2608.03283 — 326.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (« panel » : plusieurs agents donneraient des avis) ; mécanisme non précisé par la notice.
- Visualizing Graph-to-Answer Mechanism Recovery in Materials-Science Hypothesis Generation (2026-08-04) — https://arxiv.org/abs/2608.04170 — 327.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (visualisation de la façon dont un mécanisme porté par un graphe est retrouvé dans la réponse, en génération d'hypothèses de science des matériaux) ; mécanisme non précisé par la notice.
- MBA: Multimodal Benchmark and Agents for Real-World Business Ideation (2026-08-12) — https://arxiv.org/abs/2608.11616 — 333.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai multimodal pour l'idéation d'affaires en situation réelle : les idées y seraient notées, on ne sait ni par qui ni comment) ; mécanisme non précisé par la notice.
- BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics (2026-08-17) — https://arxiv.org/abs/2608.16211 — 338.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (grilles de notation par étape de la recherche, qui guideraient cette évolution) ; mécanisme non précisé par la notice.
- Symposium: Trust via Auditable Records for Communities of AI Scientist Agents (2026-08-20) — https://arxiv.org/abs/2608.19511 — 342.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (la confiance entre agents reposerait sur ces registres vérifiables plutôt que sur la déclaration de chacun) ; mécanisme non précisé par la notice.
- DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation (2026-08-14) — https://arxiv.org/abs/2609.22104 — 357.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (un agent instructeur évalue des idées) ; mécanisme non précisé par la notice.
- Recursive Self-Improvement through Multi-Agent Self-Supervision (2026-10-08) — https://arxiv.org/abs/2610.12176 — 371.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (les agents se supervisent entre eux ; le signal de supervision n'est pas dit) ; mécanisme non précisé par la notice.
- AI-Assisted Tumor-Growth Law Discovery from Sparse Data: Refitting and LLM-Based Ranking (2026-10-12) — https://arxiv.org/abs/2610.16891 — 373.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (classement des lois candidates par un modèle de langue) ; mécanisme non précisé par la notice.
- Beyond Better Ideas: How Human-AI Collaboration Shapes Scientific Ideas and Human Perceptions (2026-10-22) — https://arxiv.org/abs/2610.30568 — 382.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (étude de la collaboration entre humains et modèles : effet sur les idées scientifiques produites et sur la perception qu'en ont les humains) ; mécanisme non précisé par la notice.
- Aligning Autoresearch: Co-Improvement between Agents and Humans (2026-10-28) — https://arxiv.org/abs/2610.38882 — 388.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (co-amélioration entre agents de recherche automatique et humains, sous l'angle de l'alignement ; place de l'humain non dite) ; mécanisme non précisé par la notice.
- Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and Connection in Base Language Models (2026-08-20) — https://arxiv.org/abs/2608.19893 — 404.1 — inconnu — lecture : page ou résumé — La nouveauté est lue par un jugement de surprise et de connexion (d'après le titre) ; qui juge : non précisé par la notice.

### mémoire (16)

- EvoLattice: Persistent Internal-Population Evolution through Multi-Alternative Quality-Diversity Graph Representations for LLM-Guided Program Discovery (2025-12-15) — https://arxiv.org/abs/2512.13857 — 232.1 — inconnu — lecture : notice seule — Population interne persistante (d'après le titre seul) ; fonctionnement non précisé par la notice.
- AgentRxiv: Towards Collaborative Autonomous Research (2025-03-23) — https://arxiv.org/abs/2503.18102 — 243.0 — inconnu — lecture : notice seule — Dépôt partagé de travaux entre agents de recherche autonomes, pour une recherche collaborative (d'après le titre) ; fonctionnement non précisé par la notice.
- NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation (2026-05-11) — https://arxiv.org/abs/2605.10813 — 271.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (co-évolution annoncée de compétences, de mémoire et de politique) ; mécanisme non précisé par la notice.
- EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents (2026-05-13) — https://arxiv.org/abs/2605.13941 — 273.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (architecture de mémoire d'agents) ; mécanisme non précisé par la notice.
- The Compressive Knowledge Graph Hypothesis: Which Graph Facts Matter for Scientific Hypothesis Generation? (2026-05-26) — https://arxiv.org/abs/2605.27176 — 285.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (quels faits d'un graphe de connaissances comptent pour engendrer des hypothèses ; hypothèse dite « compressive ») ; mécanisme non précisé par la notice.
- SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs (2026-05-29) — https://arxiv.org/abs/2605.30711 — 288.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution de la mémoire d'agents) ; mécanisme non précisé par la notice.
- ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System (2026-07-15) — https://arxiv.org/abs/2607.14178 — 314.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (base de connaissances mobilisée par les agents) ; mécanisme non précisé par la notice.
- LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents (2026-07-30) — https://arxiv.org/abs/2607.27690 — 322.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution de l'expérience accumulée, sans entraînement, pour des agents de laboratoire humide) ; mécanisme non précisé par la notice.
- EviGraph: Evidence-Guided Autonomous Research Agents (2026-08-05) — https://arxiv.org/abs/2608.04738 — 328.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (graphe de preuves tenu au fil de la recherche) ; mécanisme non précisé par la notice.
- Symposium: Trust via Auditable Records for Communities of AI Scientist Agents (2026-08-20) — https://arxiv.org/abs/2608.19511 — 342.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (registres vérifiables partagés par une communauté d'agents de recherche) ; mécanisme non précisé par la notice.
- HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning (2026-08-26) — https://arxiv.org/abs/2608.25770 — 345.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (apprentissage de savoir-faire scientifiques réutilisés d'une tâche à l'autre) ; mécanisme non précisé par la notice.
- MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry (2026-08-28) — https://arxiv.org/abs/2608.28315 — 347.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (génération d'hypothèses en chimie conduite par une mémoire et de façon incrémentale) ; mécanisme non précisé par la notice.
- DeepInstructor: An Agentic AI Instructor for Experience-Driven Idea Evaluation (2026-08-14) — https://arxiv.org/abs/2609.22104 — 357.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cette évaluation s'appuierait sur l'expérience accumulée) ; mécanisme non précisé par la notice.
- Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks (2026-10-08) — https://arxiv.org/abs/2610.11794 — 369.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recueils de règles réflexifs tenus comme mémoire réutilisable) ; mécanisme non précisé par la notice.
- Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery (2026-10-23) — https://arxiv.org/abs/2610.32195 — 383.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (des hypothèses seraient condensées en principes ; réemploi non dit) ; mécanisme non précisé par la notice.
- AutoScientist: An Autonomous Agent for Long-Horizon Scientific Discovery via Connectome Memory (2026-09-18) — https://openreview.net/forum?id=naSQqdvnfD — 528.0 — oui, mesuré — lecture : page ou résumé — Mémoire en « connectome » (structure reliée, d'après le titre) pour un agent de découverte à long horizon ; contenu et règle de mise à jour non précisés par la notice.

### sélection (3)

- Influence-Guided Symbolic Regression: Scientific Discovery via LLM-Driven Equation Search with Granular Feedback (2026-05-27) — https://arxiv.org/abs/2605.29184 — 286.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (retour fin, guidé par l'influence, rendu à la recherche d'équations) ; mécanisme non précisé par la notice.
- GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization (2026-07-11) — https://arxiv.org/abs/2607.10127 — 310.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution optimisée par renforcement : ce qui survit serait appris) ; mécanisme non précisé par la notice.
- LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28 (2026-09-04) — https://arxiv.org/abs/2609.05093 — 351.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (évolution de programmes : une population dont les meilleurs se reproduisent ; règle de survie non précisée) ; mécanisme non précisé par la notice.

### coût (9)

- SLDBench v2: Active Scaling Law Discovery (2026-10-12) — https://arxiv.org/abs/2610.16297 — 173.1 — inconnu — lecture : page ou résumé — Lecture du relevé d'après le titre (« active ») : un banc actif laisserait supposer une économie de mesures ; la notice ne précise ni budget ni mécanisme de coût.
- Finite Resources False Discovery Rate Control in Structured Hypothesis Spaces (2026-06-13) — https://arxiv.org/abs/2606.15393 — 210.1 — inconnu — lecture : page ou résumé — Les ressources finies entrent dans le contrôle statistique lui-même (d'après le titre et la notice) ; règle d'allocation non précisée par la notice.
- SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs (2026-05-29) — https://arxiv.org/abs/2605.30711 — 288.2 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (porte annoncée comme rendant l'évolution de la mémoire « efficace ») ; mécanisme non précisé par la notice.
- Deliberate Evolution: Agentic Reasoning for Sample-Efficient Symbolic Regression with LLMs (2026-06-03) — https://arxiv.org/abs/2606.04360 — 290.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (économie d'échantillons annoncée) ; mécanisme non précisé par la notice.
- Federation Is Nearly Free, Reasoning Is Not: Tradeoffs for AI Co-Scientists in Protein Characterization Workflows (2026-08-25) — https://arxiv.org/abs/2608.25215 — 344.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (comparaison des coûts dans des chaînes de caractérisation de protéines : fédérer les ressources coûterait presque rien, le raisonnement du modèle coûterait cher) ; mécanisme non précisé par la notice.
- Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents (2026-09-01) — https://arxiv.org/abs/2609.01294 — 349.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (l'engagement différé pose une question d'allocation de l'effort entre exploration et approfondissement, que le titre ne chiffre pas) ; mécanisme non précisé par la notice.
- HyGRAIL: Cost-Aware and Evidence-Grounded Scientific Hypothesis Discovery over Knowledge Graphs (2026-09-02) — https://arxiv.org/abs/2609.02056 — 350.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte d'hypothèses scientifiques sur des graphes de connaissances qui tient compte du coût) ; mécanisme non précisé par la notice.
- LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28 (2026-09-04) — https://arxiv.org/abs/2609.05093 — 351.3 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le titre affiche une dépense totale de 28 dollars) ; mécanisme non précisé par la notice.
- AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement (2026-10-13) — https://arxiv.org/abs/2610.18083 — 374.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (mise à l'échelle adaptative, donc allocation de ressources ; règle non dite) ; mécanisme non précisé par la notice.

### auto-conception (27)

- Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch (2026-07-30) — https://arxiv.org/abs/2607.27687 — 117.2 — inconnu — lecture : page ou résumé — Le remède proposé par le travail (« répéter » avant d'appliquer, d'après le titre) pour une auto-recherche qui s'améliore elle-même est non précisé par la notice.
- NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation (2026-05-11) — https://arxiv.org/abs/2605.10813 — 271.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le système d'automatisation de la recherche ferait évoluer ses propres compétences et sa politique) ; mécanisme non précisé par la notice.
- EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents (2026-05-13) — https://arxiv.org/abs/2605.13941 — 273.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (l'architecture de mémoire évoluerait d'elle-même par une boucle de recherche automatisée) ; mécanisme non précisé par la notice.
- AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration (2026-03-15) — https://arxiv.org/abs/2605.20025 — 279.3 — inconnu — lecture : page ou résumé — Famille suggérée par le seul titre (recherche « qui se renforce elle-même ») ; mécanisme non précisé par la notice.
- Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators (2026-05-21) — https://arxiv.org/abs/2605.22343 — 280.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (harnais d'essai et d'erreur qui évoluerait de lui-même) ; mécanisme non précisé par la notice.
- MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery (2026-06-04) — https://arxiv.org/abs/2606.06473 — 291.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cadre annoncé comme évoluant de lui-même) ; mécanisme non précisé par la notice.
- Autonomous Scientific Discovery via Iterative Meta-Reflection (2026-07-01) — https://arxiv.org/abs/2607.01131 — 303.2 — inconnu — lecture : page ou résumé — Famille suggérée par le seul titre (« méta-réflexion » : le système réfléchirait sur sa propre démarche ; rien ne dit qu'il modifie sa conception) ; mécanisme non précisé par la notice.
- CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference (2026-07-24) — https://arxiv.org/abs/2607.22511 — 318.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cadre d'agents annoncé comme s'améliorant lui-même) ; mécanisme non précisé par la notice.
- RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement (2026-07-28) — https://arxiv.org/abs/2607.25886 — 320.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai de l'amélioration récursive de soi, restreint à la recherche centrée sur les données) ; mécanisme non précisé par la notice.
- A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical Coordination (2026-08-05) — https://arxiv.org/abs/2608.04872 — 329.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de régression symbolique annoncés comme évoluant eux-mêmes) ; mécanisme non précisé par la notice.
- AQuA: Recursively Self-Improving Quantitative Trading Research Agents (2026-08-13) — https://arxiv.org/abs/2608.12841 — 334.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents de recherche en finance quantitative qui s'améliorent eux-mêmes de façon récursive) ; mécanisme non précisé par la notice.
- BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics (2026-08-17) — https://arxiv.org/abs/2608.16211 — 338.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agent de recherche médicale qui évolue de lui-même) ; mécanisme non précisé par la notice.
- Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery (2026-08-19) — https://arxiv.org/abs/2608.19047 — 340.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (un agent de niveau supérieur compose l'orchestration des agents selon la tâche de découverte scientifique) ; mécanisme non précisé par la notice.
- AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement (2026-08-20) — https://arxiv.org/abs/2608.20318 — 343.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (banc d'essai qui mesure la capacité d'agents à concevoir des algorithmes d'apprentissage automatique, en vue de l'auto-amélioration récursive) ; mécanisme non précisé par la notice.
- HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning (2026-08-26) — https://arxiv.org/abs/2608.25770 — 345.3 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (le cadre se dit capable de s'améliorer lui-même, par ces savoir-faire appris) ; mécanisme non précisé par la notice.
- Self-Evolving Multi-Agent Symbolic Discovery for Financial Fundamental Analysis (2026-09-26) — https://arxiv.org/abs/2609.32746 — 362.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (système dit auto-évolutif ; ce qui évolue n'est pas dit) ; mécanisme non précisé par la notice.
- Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks (2026-10-08) — https://arxiv.org/abs/2610.11794 — 369.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive fondée sur un modèle, par des recueils de règles issus de la réflexion de l'agent) ; mécanisme non précisé par la notice.
- Recursive Self-Improvement through Multi-Agent Self-Supervision (2026-10-08) — https://arxiv.org/abs/2610.12176 — 371.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive par supervision mutuelle entre plusieurs agents) ; mécanisme non précisé par la notice.
- EvoBelief: Falsifiable World Models for Self-Improving LLM Agents (2026-10-08) — https://arxiv.org/abs/2610.12789 — 372.1 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agents à modèles de langue qui s'améliorent eux-mêmes en faisant évoluer leurs croyances) ; mécanisme non précisé par la notice.
- AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement (2026-10-13) — https://arxiv.org/abs/2610.18083 — 374.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive dont l'échelle et la coordination sont adaptées en cours de route) ; mécanisme non précisé par la notice.
- SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm (2026-10-14) — https://arxiv.org/abs/2610.20431 — 376.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive par un essaim d'agents scientifiques qui évolue) ; mécanisme non précisé par la notice.
- MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery (2026-10-17) — https://arxiv.org/abs/2610.24454 — 377.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive pour la découverte scientifique à plusieurs agents) ; mécanisme non précisé par la notice.
- LegoSR: A Unified Framework for Self-Improving Agent-Guided Scientific Discovery (2026-10-24) — https://arxiv.org/abs/2610.33465 — 385.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (cadre unifié de découverte scientifique guidée par un agent qui s'améliore lui-même ; le sigle évoque la régression symbolique et des briques assemblables, sans confirmation) ; mécanisme non précisé par la notice.
- SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery (2026-11-09) — https://arxiv.org/abs/2611.12552 — 389.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (auto-amélioration récursive à plusieurs agents) ; mécanisme non précisé par la notice.
- Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery (2026-11-09) — https://arxiv.org/abs/2611.12762 — 390.0 — inconnu — lecture : notice seule — Le titre annonce une architecture « métacognitive » pour la découverte scientifique ; le mécanisme lui-même est non précisé par la notice (classement dans cette famille d'après le seul titre, à confirmer).
- Wright--G\"odel Machine: Mitigating Homogenization in Self-Improving Agents (2026-09-11) — https://openreview.net/forum?id=cQkSamYGQi — 513.2 — inconnu — lecture : page ou résumé — Cadre d'un système auto-améliorant à archive (lignée des machines de Gödel à archive, d'après le titre) où les agents descendants sont des modifications de leurs parents ; non précisé par la notice au-delà.
- Beyond Self-Evolution: Meta-Evolving Agents for Cross-Task Agent Improvement (2026) — https://openreview.net/forum?id=0b4wysHrzh — 628.0 — inconnu — lecture : notice seule — Agents qui méta-évoluent pour améliorer d'autres agents entre tâches (d'après le titre seul ; soumission anonyme ; non lu).

### autre (11)

- SciResearcher: Scaling Deep Research Agents for Frontier Scientific Reasoning (2026-05-02) — https://arxiv.org/abs/2605.01489 — 266.0 — inconnu — lecture : notice seule — Système de recherche automatisée (agents de recherche approfondie pour le raisonnement scientifique, d'après le titre) ; mécanisme d'exploration, d'épreuve ou de jugement non précisé par la notice.
- NORA: A Harness-Engineered Autonomous Research Agent for End-to-End Spatial Data Science (2026-05-03) — https://arxiv.org/abs/2605.02092 — 267.0 — inconnu — lecture : notice seule — Système de recherche automatisée (agent de recherche autonome de bout en bout pour la science des données spatiales, d'après le titre) ; mécanisme d'exploration, d'épreuve ou de jugement non précisé par la notice.
- ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration (2026-05-04) — https://arxiv.org/abs/2605.03042 — 268.0 — inconnu — lecture : notice seule — Système de recherche automatisée (recherche autonome par collaboration adverse entre agents, d'après le titre) ; mécanisme d'exploration, d'épreuve ou de jugement non précisé par la notice.
- AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents (2026-05-07) — https://arxiv.org/abs/2605.06607 — 269.0 — inconnu — lecture : notice seule — Système de recherche automatisée (découverte ouverte en mécanique des fluides numérique par agents, d'après le titre) ; mécanisme d'exploration, d'épreuve ou de jugement non précisé par la notice.
- OmniScientist: An Omni-Modal Omni-Discipline AI Scientist (2026-08-13) — https://arxiv.org/abs/2608.13558 — 335.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (système complet de recherche automatisée couvrant toutes les modalités et toutes les disciplines ; aucune famille précise ne se lit dans le titre) ; mécanisme non précisé par la notice.
- ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond (2026-08-14) — https://arxiv.org/abs/2608.14354 — 336.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (agent à long horizon pour la recherche en apprentissage automatique et la découverte scientifique ; aucune famille précise ne se lit dans le titre) ; mécanisme non précisé par la notice.
- Personalized Auto-Research: Towards a True AI Co-Scientist (2026-08-14) — https://arxiv.org/abs/2608.14881 — 337.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (recherche automatisée personnalisée selon le chercheur humain accompagné ; aucune famille précise ne se lit dans le titre) ; mécanisme non précisé par la notice.
- AI Scientist Mission Control (AIMC): Visual Analytics for Human Oversight of Autonomous Scientific Discovery (2026-08-10) — https://arxiv.org/abs/2608.28637 — 348.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (supervision humaine : tableau de bord visuel pour suivre et contrôler un système de découverte scientifique autonome) ; mécanisme non précisé par la notice.
- AutoKD: Autonomous Knowledge Discovery (2026-09-06) — https://arxiv.org/abs/2609.06366 — 352.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (découverte autonome de connaissances ; aucune famille précise ne se lit dans le titre) ; mécanisme non précisé par la notice.
- Doc2LoRA Provides Decodable Representations of Scientific Ideas (2026-09-29) — https://arxiv.org/abs/2609.38374 — 364.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (autre : représentation des idées scientifiques — des adaptateurs de rang faible tirés de documents donneraient des représentations décodables d'idées ; lien possible avec la mesure de distance entre idées, non confirmé) ; mécanisme non précisé par la notice.
- Learning Scientific Trajectories to Predict Future Biomedical Discoveries (2026-10-28) — https://arxiv.org/abs/2610.38719 — 387.0 — inconnu — lecture : notice seule — Famille suggérée par le seul titre (autre : prédiction — apprentissage de trajectoires scientifiques pour prédire de futures découvertes biomédicales ; lien possible avec la mesure de nouveauté par antériorité datée, non confirmé) ; mécanisme non précisé par la notice.

## 7. Mécanismes classés « autre » : reclassés ou justifiés

Quarante mécanismes étaient classés « autre » dans les lots. Neuf ont été reclassés dans une des huit familles, un a été retiré (cloisonnement), trente sont conservés avec une justification (dix-neuf ci-dessous, onze suggérés par le titre en section 6 ; table `programmes/corrections-v1.json`, correction 4 de la contre-lecture). Les mécanismes « autre » suggérés par le titre sont en section 6.

- Agentic Economies for Autonomous Scientific Discovery (2026-09-25) — https://arxiv.org/abs/2609.31562 — 132.0 — non — lecture : page ou résumé — Autre : organisation de la découverte autonome en économie d'agents, avec sa gouvernance ; texte de position, aucun mécanisme précisé par la notice. — *reste « autre » : organisation et gouvernance d'un collectif, texte de position sans mécanisme d'idéation, d'épreuve ou de jugement*
- FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents (2026-07-06) — https://arxiv.org/abs/2607.05682 — 153.0 — oui, mesuré — lecture : page ou résumé — Autre (traçabilité de la question) : la formation de la première question de recherche d'un agent est rendue auditable ; la table classe ce travail du côté de l'intégrité des agents de recherche, en marge du sujet ; le procédé d'audit est non précisé par la notice. — *reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées*
- DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists (2026-10-07) — https://arxiv.org/abs/2610.09558 — 175.1 — inconnu — lecture : page ou résumé — Autre (terrain d'entraînement) : les mêmes mondes synthétiques servent aussi à entraîner les agents, pas seulement à les noter ; séparation entre mondes d'entraînement et d'épreuve non précisée par la notice. — *reste « autre » : entraînement des agents (récompense, terrain d'entraînement), ni l'épreuve des idées ni leur sélection*
- Beyond fabrication: Misattributed numbers in papers written by AI research agents (2026-10-28) — https://arxiv.org/abs/2610.38691 — 201.0 — inconnu — lecture : page ou résumé — Intégrité du compte rendu : audit par provenance des nombres écrits dans des articles produits par agents, pour repérer ceux attribués à la mauvaise source ; hors du champ de l'exploration d'idées selon la veille. — *reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées*
- Quantifying Claim Smoothing by LLM Research Agents (2026-10-26) — https://arxiv.org/abs/2610.35793 — 202.0 — inconnu — lecture : page ou résumé — Intégrité du compte rendu : mesure du « lissage » des revendications, c'est-à-dire d'affirmations plus fortes que les preuves que l'agent a lui-même produites ; procédé de mesure non précisé par la notice. — *reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées*
- RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention (2026-10-22) — https://arxiv.org/abs/2610.31372 — 203.0 — oui, mesuré — lecture : page ou résumé — Intégrité du compte rendu : détection automatique des violations d'intégrité d'un agent de recherche pendant l'exécution, avec intervention en cours de run ; types de violations non précisés par la notice. — *reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées*
- Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing (2026-08-07) — https://arxiv.org/abs/2608.07437 — 207.1 — oui, affirmé — lecture : page ou résumé — Entraînement de l'agent : il est entraîné à des tests d'hypothèses fiables par une récompense statistique vérifiée ; forme de la récompense non précisée par la notice. — *reste « autre » : entraînement des agents (récompense, terrain d'entraînement), ni l'épreuve des idées ni leur sélection*
- AI-Research Agents in the Wild. From GitHub and arXiv to Regularities and Gaps (2026-09-01) — https://arxiv.org/abs/2609.11975 — 219.0 — inconnu — lecture : page ou résumé — Cartographie : recense les agents de recherche publics (dépôts GitHub, arXiv), leurs régularités et leurs manques ; les mécanismes recensés sont non précisés par la notice. — *reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre*
- A Vocabulary for Multi-Agent Automated Research Systems (2026-07-13) — https://arxiv.org/abs/2607.22682 — 221.0 — non — lecture : page ou résumé — Vocabulaire commun pour décrire et comparer les systèmes de recherche automatisée à plusieurs agents (outil de description, pas un mécanisme) ; utile pour nommer rôles et compositions. — *reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre*
- EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery (2026-06-11) — https://arxiv.org/abs/2606.13662 — 225.0 — oui, mesuré — lecture : page ou résumé — Ingénierie de l'environnement de l'agent (ce qui l'entoure, plutôt que l'agent lui-même) présentée comme le levier de la découverte autonome ; ce qui est aménagé dans l'environnement est non précisé par la notice. — *reste « autre » : aménagement de l'environnement de l'agent, dont la notice ne précise pas le contenu*
- AI for Auto-Research: Roadmap & User Guide (2026-05-18) — https://arxiv.org/abs/2605.18661 — 226.0 — non — lecture : page ou résumé — Feuille de route et guide de la recherche automatisée, avec liste entretenue (521 identifiants arXiv relevés par la veille, rubriques « génération d'idées », « nouveauté et faisabilité », « systèmes évolutifs et auto-améliorants ») : porte d'entrée bibliographique, aucun mécanisme propre. — *reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre*
- TraceML: What Auto-Research Agents Miss in Long-Horizon ML Development (2026-08-26) — https://arxiv.org/abs/2608.26086 — 346.0 — oui, affirmé — lecture : page ou résumé — Diagnostic et non mécanisme : corpus de trajectoires d'agents de recherche automatisée comparées à des cohortes humaines sur de longs développements en apprentissage automatique, pour relever ce que les agents manquent (affirmation des auteurs, lue sur fiche de soumission ; la table note « mesuré sans données publiées » ; ce que les agents manquent n'est pas précisé par la notice). — *reste « autre » : diagnostic ou mesure descriptive sur des agents de recherche, pas un mécanisme que l'organisme assemble*
- AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework (2026-09-24) — https://arxiv.org/abs/2609.30541 — 359.0 — oui, affirmé — lecture : page ou résumé — Diagnostic : la boucle de recherche automatisée de Karpathy est appliquée à l'échelle de la production et ses modes d'échec sont documentés ; la veille la range sous l'étroitesse et la convergence de l'exploration des proposeurs (affirmation des auteurs, lue sur résumé ; la liste des modes d'échec n'est pas précisée par la notice ; la table note « mesuré sans données publiées »). — *reste « autre » : diagnostic ou mesure descriptive sur des agents de recherche, pas un mécanisme que l'organisme assemble*
- AI-Powered (Finance) Scholarship (2024-12) — https://www.nber.org/papers/w33363 — 394.2 — oui, affirmé — lecture : page ou résumé — Rédaction automatique : des modèles de langue écrivent des articles complets autour des signaux retenus (production du texte séparée de la découverte). — *reste « autre » : rédaction automatique, séparée de la découverte*
- Stacking-Based Weighting for Large Language Bayes in M-Open Settings (2026-11-02) — https://arxiv.org/abs/2611.03966 — 451.0 — inconnu — lecture : page ou résumé — Agrégation statistique de modèles candidats : remplace la moyenne bayésienne de modèles par un empilement (pondération par performance prédictive) quand aucun candidat n'est le vrai modèle ; le lien à l'idéation est indirect (comment peser plusieurs hypothèses écrites par un modèle de langue) ; le détail n'est pas précisé par la notice. — *reste « autre » : agrégation statistique de modèles candidats, lien à l'idéation indirect selon le lot*
- From Rules to Reasoning: A Survey of Large Language Model-Based Approaches to Scientific Hypothesis and Idea Generation (2026-05-22) — non relevée (entrée de Semantic Scholar sans identifiant arXiv) — 457.0 — non — lecture : notice seule — Revue de littérature des approches de génération d'hypothèses et d'idées par modèles de langue ; aucun mécanisme propre ; contenu non précisé par la notice (utile seulement comme porte d'entrée bibliographique). — *reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre*
- We need more decorrelated evidence (2026-11-12) — https://www.lesswrong.com/posts/EuhQ5fnGR4tAQTTgd/we-need-more-decorrelated-evidence — 465.1 — non — lecture : page ou résumé — Recension d'une dizaine de travaux de 2026 sur le goût de recherche et l'étroitesse des idées des modèles (porte d'entrée bibliographique, pas un mécanisme). — *reste « autre » : porte d'entrée bibliographique, vocabulaire ou cartographie, aucun mécanisme propre*
- Dawes-Institute/ai-peer-review-benchmark (2026-08-09) — https://github.com/Dawes-Institute/ai-peer-review-benchmark — 489.3 — oui, affirmé — lecture : page ou résumé — Autre — traçabilité du résultat : un programme unique reproduit chaque chiffre du compte rendu à partir des résultats stockés, et un journal de travail garde le déroulé réel de l'analyse pour qu'il soit inspectable. — *reste « autre » : intégrité ou traçabilité du compte rendu (provenance des nombres, audit), hors des huit familles de recherche, de jugement et d'épreuve des idées*
- Scaling Automatic Research Agents via World Models (2026-09-12) — https://openreview.net/forum?id=h4nx21WBtn — 519.0 — inconnu — lecture : page ou résumé — Entraînement des proposeurs : post-entraîne des agents de recherche par renforcement à l'aide d'un modèle du monde (qui tiendrait lieu d'expériences réelles ; ce point est non précisé par la notice). — *reste « autre » : entraînement des agents (récompense, terrain d'entraînement), ni l'épreuve des idées ni leur sélection*

## 8. Travaux sans mécanisme relevé

Pour chacun, le statut dit pourquoi. Les travaux « exclue » relèvent de familles exclues de toute lecture de contenu pour cette pièce : seuls l'indice, le statut et le chemin sont donnés.

- indice 61 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[61]
- indice 74 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[74]
- indice 83 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[83]
- indice 84 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[84]
- indice 89 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[89]
- indice 123 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[123]
- indice 190 — hors sujet — Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle (2026-06-05) — https://arxiv.org/abs/2606.07462
- indice 204 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[204]
- indice 205 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[205]
- indice 206 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[206]
- indice 209 — hors sujet — PseudoBench: Measuring How Agentic Auto-Research Fuels Pseudoscience (2026-06-16) — https://arxiv.org/abs/2606.18060
- indice 216 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[216]
- indice 263 — liste sans mécanisme — Awesome-LLM-Scientific-Discovery (date non donnée) — https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery
- indice 264 — liste sans mécanisme — Awesome-AI-Scientist (date non donnée) — https://github.com/ResearAI/Awesome-AI-Scientist
- indice 265 — liste sans mécanisme — Awesome-AI-Scientist-Papers (date non donnée) — https://github.com/openags/Awesome-AI-Scientist-Papers
- indice 282 — notice muette — AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery (2026-05-22) — https://arxiv.org/abs/2605.23204
- indice 297 — hors sujet — AI Scientists as Engines of Discovery: A Case for Development within Reformed Institutions (2026-06-22) — https://arxiv.org/abs/2606.22859
- indice 306 — notice muette — Rethinking Scientific Discovery in the Agentic Era (2026-07-04) — https://arxiv.org/abs/2607.03863
- indice 354 — hors sujet — Sci-MMR: Benchmarking Multi-Step Evidence-Grounded Scientific Reasoning in Multimodal Agents (2026-09-10) — https://arxiv.org/abs/2609.11243
- indice 356 — hors sujet — An immune world model for multiscale forecasting and therapeutic hypothesis generation (2026-09-13) — https://arxiv.org/abs/2609.14709
- indice 423 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[423]
- indice 432 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[432]
- indice 438 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[438]
- indice 443 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[443]
- indice 446 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[446]
- indice 447 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[447]
- indice 448 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[448]
- indice 477 — hors sujet — AI for Agent Foundations Etc.? (2026-03-12) — https://www.pulse.bot/ai/blogs/ai-for-agent-foundations-etc-634408b2-8c9e-442b-b18c-2c6d766939f9
- indice 478 — notice muette — We should try to automate AI safety work asap (date non donnée) — https://www.lesswrong.com/posts/W3KfxjbqBAnifBQoi/we-should-try-to-automate-ai-safety-work-asap
- indice 479 — hors sujet — A basic case for differentially accelerating conceptual reasoning (date non donnée) — https://www.lesswrong.com/posts/eimAN67tiNsrrtnbK/a-basic-case-for-differentially-accelerating-conceptual
- indice 480 — hors sujet — What would it take for AI to discover penicillin (date non donnée) — https://www.lesswrong.com/posts/83nKFa27uWYDSAvLF/what-would-it-take-for-ai-to-discover-penicillin
- indice 484 — hors sujet — Toward an O*NET for AI R&D (2026-06) — https://epoch.ai/gradient-updates/toward-an-onet-for-ai-rnd
- indice 487 — hors sujet — Q3.5 timelines update (AI Futures Project) — « singularité par le goût seul » (2026) — https://blog.aifutures.org/p/q35-timelines-update-looks-like-the
- indice 497 — hors sujet — EvoMap/AutoResearch ; OpenNSWM-Lab/FAROS ; RUC-NLPIR/Arbor ; YihongT/CoAutoResearch ; EIMP-Lab/Hypoloom (2026-05) — https://github.com/EvoMap/AutoResearch
- indice 498 — hors sujet — Trae1ounG/SAEScientist ; MasterAI-EAM/ai-scientists-last-exam ; Omni-Scientist/Awesome-AI-Scientist (2026-08) — https://github.com/Omni-Scientist/Awesome-AI-Scientist
- indice 503 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[503]
- indice 565 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[565]
- indice 622 — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[622]

## 9. Retraits et pièces

- Retraits : indice 259 (correction 4) ; indice 57 (correction 6) — lignes retirées du relevé parce qu'elles reprenaient une facette d'une famille exclue ; leur contenu n'est pas reproduit.
- `docs/notes/matiere-premiere-auto-conception-v1/releve-mecanismes-v1.json` — sha256 `1110ef784e5c628dc2017e9aab1abbd57ca10ba784ecb4f18d2c732bdc453faa`
- `docs/notes/matiere-premiere-auto-conception-v1/programmes/corrections-v1.json` — sha256 `7b129cffe729c29805c613fd66c86c33160829d255602dc661d0f96d4fe68890`
- `docs/notes/matiere-premiere-auto-conception-v1/programmes/fusionner_v1.py` — sha256 `8935d5096dbca729a70d900069547577622fa55dc834b398fd3eac5be11efe60`
