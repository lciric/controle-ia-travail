# EXTRAIT — AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

- Auteurs : Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang (Laboratoire d'intelligence artificielle de Shanghai ; universités Fudan, Jiaotong de Shanghai, Zhejiang) ; année : 2026 (v1 du 14 octobre 2026) ; identifiant : arXiv:2610.19422v1 (25 pages)
- Statut : préimpression arXiv cs.AI ; code et modèles annoncés (p.1) ; le PDF porte l'avertissement « This paper contains potentially offensive and harmful text » ; le titre du PDF est « AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety »
- PDF source : `docs/sources/pdf/2610.19422v1.pdf` ; SHA-256 du PDF : `4812c7037c4c4363f4fe7ebbcf027e2f286341446dbd503e20bd8a4b72715bac` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-11
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, lignes rejointes en paragraphes ; formules extraites en texte linéaire, parfois dans le désordre), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux extraits en mode mise en page (colonnes séparées par « | »). Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : p.4 figure 2 (exemples illustrés de tâches adverses : fragments de consignes d'injection et de détournement dans des descriptions d'outils et des observations) ; annexe B (composition des données d'entraînement et taxonomie de 13 sous-types d'attaque) ; annexe C (invites de l'attaquant, du défenseur et des juges) ; annexes A, D, E non reprises. Gardés : les six classes d'attaque nommées (p.4), le protocole de co-évolution, la conception des récompenses, le protocole d'évaluation, les résultats, les limites et la déclaration d'éthique (p.11).

---

[p.1]

observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSafeEvo, a co-evolutionary reinforcement learning framework for agent safety built on an attacker–defender game spanning diverse tasks and attack types. The attacker learns to construct adversarial agent tasks that expose weaknesses in the defender’s tool use, while the defender learns to complete tasks safely under these attacks. We further introduce learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task’s contribution to attacker and defender updates. Extensive experiments on agent safety and general capability benchmarks demonstrate that our method improves adversarial robustness while maintaining general agent capabilities.

1. Introduction The emergence of large language model (LLM) agents marks a shift from text generation to active interaction with external environments. Through multi-turn interactions with external tools, agents can search for information, process documents, and manage schedules to complete complex, multi-step tasks [1, 2, 3]. However, tool use broadens the attack surface beyond user queries to include tool descriptions and environment observations. Malicious content alters task instructions, misrepresents tool behavior, or misleads subsequent decisions, inducing unsafe actions during execution [4, 5]. A central challenge is therefore to improve agents’ robustness across diverse tasks and attack types without compromising task performance. Research on LLM safety has explored adversarial training to reduce harmful responses to jailbreak prompts. However, training on a fixed attack set leaves the attack distribution unchanged as the defender’s capabilities evolve [6]. Adversarial co-evolution addresses this limitation through an iterative attacker–defender game. The attacker learns to generate attacks that induce unsafe behavior, while the defender learns to resist these attacks. Throughout training, the attacker refines its attacks against the evolving defender using feedback on attack outcomes, while the defender learns from the newly generated attacks. Existing safety-oriented approaches have primarily focused on language-level safety [6, 7, 8, 9]. For example, Self-RedTeam [6] trains a single model in both attacker and defender roles through online self-play. MAGIC [9] instead alternately optimizes separate attacker and defender models for adversarial prompt rewriting and safe response generation. For LLM agents, safety depends not only on responses but also on the decisions and actions taken during multi-turn tool interactions. ARLAS [10] extends co-evolution to this setting by training an attacker to inject malicious instructions into observations of given web tasks. However, its attacker is limited to † Corresponding author.

[p.2]

refining indirect prompt injections within supplied tasks, leaving adversarial task construction outside the co-evolutionary process. This raises a central question: How can adversarial task construction and safe task execution co-evolve across diverse tasks and attack types? In this paper, we introduce AgentSafeEvo, a co-evolutionary reinforcement learning framework for adaptive attack generation and robust defense across diverse agent tasks and attack types. AgentSafeEvo couples adversarial task generation with defensive learning through an attacker– defender game over multi-turn tool interactions. The attacker learns to construct adversarial agent tasks designed to induce unsafe behavior, while the defender learns to resist these attacks and complete tasks safely. Both models are updated using feedback on the safety and utility of the defender’s execution, allowing task generation to adapt to the defender’s evolving capabilities. Figure 1 contrasts AgentSafeEvo with language-level co-evolution. Adversarial co-evolution relies on generated tasks not only to challenge the defender but also to guide its learning. Task-level zero-sum rewards favor tasks that lower the defender’s average reward, without directly accounting for within-task reward variation. The defender learns from these reward differences, but task-wise normalization largely removes differences in their scale across tasks. We therefore introduce learnability-guided task weighting, assigning larger relative weights to tasks with greater within-task variation in defender rewards. These weights adjust each task’s contribution to the attacker and defender policy updates. Co-evolution across diverse tasks and attack types requires an attacker capable of constructing valid adversarial agent tasks. To develop this capability, we construct an agent safety training dataset spanning 50 agent scenarios, approximately 7,000 tools, and a broad range of attack types. Each adversarial task combines a user query with a corresponding tool-environment configuration, providing structured supervision for attacker initialization. The dataset also includes seed instances for subsequent co-evolutionary training. Our main contributions are as follows:

• We introduce AgentSafeEvo, a co-evolutionary framework for LLM agent safety. Beyond conventional attacker–defender games, AgentSafeEvo co-evolves adversarial agent tasks across diverse attack types. We further propose learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task’s contribution to attacker and defender updates. • We construct an agent safety training dataset spanning 50 agent scenarios and approximately 7,000 tools, covering a broad range of attack types. It includes adversarial tasks with paired user

[p.3]

queries and tool-environment configurations for attacker initialization, as well as seed instances for co-evolution. • Extensive experiments on agent safety and general capability benchmarks demonstrate that AgentSafeEvo improves adversarial robustness and general task performance. Further analyses show that both attack effectiveness and defensive robustness improve during co-evolution, with attack improvements generalizing to substantially larger target models.

[COUPÉ : p.3 travaux voisins (co-évolution des modèles de langage, évaluation de la sûreté des agents)]

3. Methods We focus on LLM agents that solve complex tasks through multi-turn interactions with external tools. During these interactions, agents may encounter untrusted content in user queries, tool descriptions, or environment observations, which can manipulate their decisions or induce unsafe actions. We consider six attack categories: direct prompt injection, indirect prompt injection, tool-description injection, misinformation, harmful tool execution, and user-query jailbreak. To improve robustness against these attacks, we introduce an adversarial training framework that jointly optimizes an attacker model (𝜋𝐴 ) and a defender agent (𝜋𝐷 ) over multi-turn tool-interaction trajectories, allowing their attack and defense capabilities to co-evolve.

[p.4]

Figure 2: Overview of AgentSafeEvo. Phase 1 initializes the attacker through supervised fine-tuning on synthesized adversarial tasks. Phase 2 jointly trains the attacker and defender using GRPO over multi-turn tool interactions. Defender rewards combine safety and utility, while the attacker reward for each task is the negative mean defender reward. Learnability-guided task weighting uses within-task defender-reward standard deviations to compute a shared task-specific weight for both policies’ GRPO advantages.

• Attacker model (𝜋𝐴 ). Given an agent scenario, a seed intent, and environment information, 𝜋𝐴 constructs an agent task by generating a user query, tool definitions, and environment observations. We refer to tasks that incorporate malicious content as adversarial agent tasks. • Defender agent (𝜋𝐷 ). Given an agent task, 𝜋𝐷 interacts with the available tools over multiple turns and produces a final answer. We record the resulting sequence of tool calls, environment observations, and final answer as an interaction trajectory.

The training procedure is summarized in Appendix A (Algorithm 1). As shown in Figure 2, AgentSafeEvo consists of two stages: Red-Team Attacker Initialization and Joint Adversarial Training. The first stage trains 𝜋𝐴 to construct adversarial tasks with consistent user queries and tool-environment configurations. Building on this initialization, the second stage jointly optimizes 𝜋𝐴 and 𝜋𝐷 through adversarial reinforcement learning over multi-turn tool-interaction trajectories.

3.1. Red-Team Attacker Initialization Adversarial training faces a cold-start problem because the initial 𝜋𝐴 cannot reliably generate valid adversarial tasks. [COUPÉ] For each training example, let x𝐴 denote the attacker input and y𝐴 the corresponding target output. The SFT objective is ⎡ ⎤ |y𝐴 | ∑︁ ℒSFT (𝜃𝐴 ) = −E(x𝐴 ,y𝐴 )∼𝒟SFT ⎣ log 𝜋𝐴 (𝑦𝐴,𝑡 | x𝐴 , y𝐴,<𝑡 ; 𝜃𝐴 )⎦ . (1) 𝑡=1

[p.5]

3.2. Joint Adversarial Training 3.2.1. Reward Design (𝑖) For each agent task y𝐴 generated by 𝜋𝐴 , the defender agent 𝜋𝐷 produces 𝐾 interaction trajectories {𝜏𝑖,𝑗 }𝐾 𝑗=1 . Each trajectory is evaluated in terms of safety and utility to obtain a trajectory-level reward for 𝜋𝐷 . The rewards across the 𝐾 trajectories are then aggregated to evaluate the corresponding agent task for 𝜋𝐴 . The complete judge prompts are provided in Appendix C.3.

Safety Reward. We evaluate safety at the trajectory level. We employ Qwen3.8-27B [30] as the reward model to classify each interaction trajectory 𝜏𝑖,𝑗 as either safe or unsafe. The safety reward is defined as {︃ +1, if 𝜏𝑖,𝑗 is safe, 𝑅safety (𝜏𝑖,𝑗 ) = (2) −1, if 𝜏𝑖,𝑗 is unsafe.

Utility Reward. Adversarial tasks may introduce harmful content alongside legitimate requirements. Optimizing solely for safety may therefore cause 𝜋𝐷 to reject the entire task rather than selectively ignore or refuse the harmful content. To discourage over-refusal, the same reward model independently assesses whether 𝜋𝐷 fulfills the legitimate requirements. The utility reward is defined as {︃ +1, if the legitimate requirements are fulfilled, 𝑅utility (𝜏𝑖,𝑗 ) = (3) −1, otherwise.

Progress toward the harmful objective is not counted as fulfilling the legitimate requirements. For entirely harmful requests, a safe refusal receives 𝑅utility = +1.

The maximum reward is obtained only when 𝜋𝐷 remains safe while fulfilling the legitimate requirements, thereby discouraging both harmful compliance and indiscriminate refusal.

Attacker Reward. Unlike the defender reward assigned to each individual trajectory, the attacker reward is defined at the task level. For each agent task, we average the defender rewards over its 𝐾 trajectories and define the attacker reward as the negative of this mean: 𝐾 (𝑖) 1 ∑︁ 𝑅𝐴 = − 𝑅𝐷 (𝜏𝑖,𝑗 ). (5) 𝐾 𝑗=1

This definition makes the task-level rewards zero-sum, assigning a higher attacker reward to a task that yields a lower mean defender reward.

3.2.2. Joint Policy Optimization To improve adversarial robustness while preserving general agent capabilities, we construct an RL dataset 𝒟RL comprising both benign and red-team seed instances. Each seed consists of an agent scenario, an intent, and the corresponding environment information, which together form the input to 𝜋𝐴 . For each seed, 𝜋𝐴 generates 𝑀 agent tasks, and 𝜋𝐷 produces 𝐾 trajectories for each task. We employ Group Relative Policy Optimization (GRPO) [31] to jointly optimize 𝜋𝐴 and 𝜋𝐷 .

[p.6]

Learnability-Guided Task Weighting. A task’s attack effectiveness does not fully characterize the (𝑖) learning opportunities it provides to the current defender. The attacker reward 𝑅𝐴 depends on the mean defender reward. It can therefore be high even when all 𝐾 defender trajectories receive the same low reward, leaving their GRPO advantages at zero. Meanwhile, defender GRPO normalizes rewards within each task, largely removing differences in reward scale across tasks. We therefore use within-task defender-reward variability to define a shared task-specific update weight. This weight adjusts each task’s contribution to the attacker and defender policy updates. Our hypothesis is that giving greater relative weight to tasks with differences in the defender’s combined safety and utility rewards can support continued co-evolution. (𝑖) [COUPÉ]

[COUPÉ : p.6-7 optimisation conjointe (équations 6 à 13)]

[p.7]

4. Experiments 4.1. Experiment settings Models. We use Qwen3-8B [32] as the backbone for both the attacker and defender. Qwen3.8- 27B [30] serves as the reward model, providing both safety and utility judgments.

Training data. For the SFT phase, we sample approximately 20,000 source tasks from TOUCAN [28], a large-scale tool-agent dataset comprising over 1.5 million trajectories synthesized from 495 real-world MCP servers. [COUPÉ] These examples are combined with approximately 10,000 benign examples for attacker initialization. [COUPÉ]

Baselines. We compare AgentSafeEvo against the following baselines: (1) the original Qwen3-8B model; (2) the prompt-based defense Spotlighting with Delimiting [24], which marks tool outputs as untrusted content using explicit delimiters; (3) the detector-based defense Prompt Guard 2 [25], which detects prompt injections in tool outputs and filters flagged content before it reaches the agent; and (4) the training-based baseline Static Adversarial Training (Static-AT), which keeps the SFT attacker fixed and updates only the defender during RL. Further details on these baselines are provided in the Appendix D.2.

4.2. Evaluation We evaluate both agent safety and general agent capabilities. We report the mean and standard deviation over three independent runs.

[p.8]

Table 1: Agent safety evaluation results. Lower ASR and harm score are better, while higher UA and NRP are
better.
Agent-SafetyBench AgentHarm | AgentDojo | MSB
Method | ASR ↓ | Harm score ↓ | ASR ↓ | UA ↑ | ASR ↓ | NRP ↑
Qwen3-8B | 49.11 ±0.51 | 50.37 ±3.63 | 22.20 ±0.57 | 53.64 ±0.90 | 60.43 ±0.97 | 28.12 ±1.30
+ Spotlighting | 48.52 ±0.78 | 53.00 ±2.60 | 19.25 ±1.04 | 57.82 ±1.11 | 58.53 ±0.73 | 29.55 ±0.46
+ Prompt Guard 2 | 44.13 ±0.64 | 54.67 ±1.07 | 16.44 ±0.45 | 47.35 ±0.52 | 59.02 ±1.57 | 29.71 ±1.29
+ Static-AT | 31.01 ±0.33 | 30.00 ±2.05 | 6.71 ±0.43 | 61.43 ±0.15 | 38.64 ±2.24 | 40.64 ±0.93
+ AgentSafeEvo (ours) | 17.84 ±0.24 | 6.53 ±0.38 | 6.18 ±0.18 | 66.52 ±1.43 | 31.25 ±1.24 | 46.00 ±0.54
Table 2: General agent capability results measured by accuracy (%).
Method | BFCL-V3 | ALFWorld | ToolHop
Qwen3-8B | 66.13 ±0.22 | 30.28 ±4.59 | 21.84 ±1.23
+ Spotlighting | 66.08 ±0.37 | 32.13 ±2.69 | 25.76 ±0.15
+ Prompt Guard 2 | 66.01 ±0.17 | 31.08 ±4.12 | 23.05 ±0.71
+ Static-AT | 66.73 ±0.50 | 30.89 ±0.43 | 39.43 ±0.09
+ AgentSafeEvo (ours) | 65.98 ±0.14 | 43.72 ±3.03 | 48.04 ±1.40

Safety evaluation. We evaluate agents on Agent-SafetyBench [21], AgentHarm [18], AgentDojo [20], and MCP Security Bench (MSB) [22]. The reported metrics are benchmark-specific: Agent-SafetyBench uses Attack Success Rate (ASR); AgentHarm uses the harm score; AgentDojo uses ASR and Utility under Attack (UA); and MSB uses ASR and Net Resilient Performance (NRP). [COUPÉ]

4.3. Main Results Consistent improvements across agent safety benchmarks. Table 1 shows that AgentSafeEvo achieves the best mean performance across all reported metrics on the four safety benchmarks for Qwen3-8B. Compared with Static-AT, the strongest safety baseline, it reduces ASR from 31.01% to 17.84% on Agent-SafetyBench and from 38.64% to 31.25% on MSB. The harm score on AgentHarm also decreases from 30.00 to 6.53. On AgentDojo, UA increases from 61.43% to 66.52% while ASR remains low at 6.18%. NRP on MSB also rises from 40.64 to 46.00. The higher UA on AgentDojo indicates better task completion under attack, while the higher NRP on MSB reflects an improved combination of task performance and attack resistance.

[p.9]

Attack effectiveness and defensive robustness improve during co-evolution. To assess each side against fixed opponents, we cross-evaluate attackers and defenders from different training stages using a shared set of 100 seed instances held out from training. Each attacker generates adversarial tasks from these seeds, and all defenders are evaluated on each resulting task set. Figure 3(a) shows that later-stage attackers achieve higher ASR against every defender, while later-stage defenders reduce ASR against every attacker. Against the base defender, ASR increases from 55.81% for the SFT attacker to 92.59% for the final attacker. Against this final attacker, ASR decreases from 92.59% for the base defender to 49.82% for the final defender. These results show that the defender becomes more robust even against the stronger attacks developed during co-evolution.

Attack improvements generalize across target models. Figure 3(b) compares the SFT attacker with the final attacker co-evolved against Qwen3-8B. Beyond Qwen3-8B, the evolved attacker achieves

[p.10]

higher ASR on all four additional target models. For example, ASR increases from 43.7% to 80.7% on Llama3.3-70B [37] and from 12.3% to 22.5% on GPT-5 [38]. These results suggest that the attack improvements are not confined to the defender used for co-evolution.

Table 3: Ablation results for Qwen3-8B on agent benchmarks for safety and general capabilities. Lower ASR is
better; higher NRP and accuracy are better.
Safety | General
Method
Agent-SafetyBench | MSB | ALFWorld | ToolHop
ASR ↓ | ASR ↓ | NRP ↑ | Acc ↑ | Acc ↑
AgentSafeEvo (ours) | 17.84 ±0.24 | 31.25 ±1.24 | 46.00 ±0.54 | 43.72 ±3.03 | 48.04 ±1.40
w/o attacker updates | 31.01 ±0.33 | 38.64 ±2.24 | 40.64 ±0.93 | 30.89 ±0.43 | 39.43 ±0.09
w/o learnability weighting | 22.91 ±0.35 | 32.89 ±0.66 | 41.48 ±0.21 | 36.70 ±0.75 | 40.07 ±0.58
w/o defender weighting | 14.13 ±0.33 | 28.47 ±1.03 | 43.04 ±0.73 | 29.05 ±0.43 | 40.80 ±0.22
w/o attacker weighting | 15.52 ±0.27 | 34.92 ±0.89 | 41.87 ±0.33 | 34.25 ±1.89 | 40.63 ±0.29
Note. The “w/o attacker updates” variant is Static-AT: the SFT attacker is fixed, task weighting is disabled, and only the
defender is trained.

Effect of co-evolution. Comparing variants (i) and (ii), co-evolution improves all reported metrics over defender-only training. ASR decreases by 8.10 and 5.75 percentage points on Agent-SafetyBench and MSB, respectively, while accuracy on ALFWorld increases from 30.89% to 36.70%. The frozen attacker already generates tasks online, but its task-generation policy remains unchanged throughout defender training. The improvements therefore indicate that online task generation alone does not account for the benefits of co-evolution. These results support updating the task-generation policy during defender training.

[p.11]

5. Conclusion In this paper, we introduced AgentSafeEvo, a co-evolutionary reinforcement learning framework for LLM agent safety that couples adversarial task construction with safe task execution over multi-turn tool interactions. The improvements over a fixed online attacker highlight the value of using defender feedback to update the task-generation policy as the agent’s capabilities evolve. Further gains come from learnability-guided task weighting, which uses within-task defender-reward variability to reweight both policies’ updates. These findings suggest that adversarial co-evolution can strengthen the robustness of tool-using LLM agents while preserving their general capabilities. Future work will extend AgentSafeEvo to collaborative multi-agent settings, focusing on safety risks arising from communication and task delegation.

AI Use Statement We used generative AI tools at several stages of this work. During manuscript preparation, these tools helped improve wording, readability, and clarity. We also used them to locate potentially relevant publications and explore related work. In the research process, AI tools supported the development of research ideas and aspects of their implementation. AI models were additionally used to produce synthetic data for the study. These tools served as research and writing aids, with the authors retaining responsibility for methodological decisions, the interpretation of experimental results, and the presentation of the work. We take full responsibility for the accuracy and integrity of the final manuscript, including its claims, results, and references.

Ethics Statement This work aims to improve the safety of tool-using LLM agents while preserving their ability to complete legitimate tasks. AgentSafeEvo generates adversarial tasks and uses them to train defenders against unsafe behavior in multi-turn tool interactions. These tasks may contain harmful instructions or attempts to manipulate an agent’s decisions. Their purpose is to expose failure modes and provide training signals for improving agent safety. This study does not involve the collection or use of personal data. We recognize the dual-use risks of this approach. An attacker trained to identify weaknesses in LLM agents could also be repurposed to construct malicious prompts or manipulate tool interactions. The framework and its generated tasks are intended to support safety research, defensive training, and evaluation. Any release or reuse of attacker models and adversarial data should account for their potential to facilitate misuse. Finally, improvements on the evaluated benchmarks do not establish safety in all deployment settings. Practical deployment requires further assessment of the tools, permissions, and environments available to the agent.

[COUPÉ : p.11-25 références et annexes]
