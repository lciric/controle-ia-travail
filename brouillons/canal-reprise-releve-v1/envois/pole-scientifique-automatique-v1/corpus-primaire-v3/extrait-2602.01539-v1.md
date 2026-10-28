# EXTRAIT — MAGIC: A Co-Evolving Attacker–Defender Adversarial Game for Robust LLM Safety

- Auteurs : Xiaoyu Wen, Zhida He (contribution égale), Han Qi, Ziyu Wan, Zhongtian Ma, Ying Wen, Tianhang Zheng, Xingcheng Xu, Chaochao Lu, Qiaosheng Zhang ; Laboratoire d'intelligence artificielle de Shanghai, Université Jiao-tong de Shanghai, Université du Zhejiang ; année : 2026 (v2 du 6 février 2026 ; la page 1 porte « 2026-2-9 ») ; identifiant : arXiv:2602.01539v2 (40 pages)
- Statut : préimpression arXiv cs.AI ; aucune mention de conférence ou de revue dans les pages lues ; le résumé donne un dépôt de code.
- PDF source : `docs/sources/pdf/2602.01539v2.pdf` ; SHA-256 du PDF : `793d32725d82e364f0ecbb0be994694d2aca20f8daf8391e6583be58f067540e` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-2 et 4-12 (corps, sans la bibliographie ; la page 3, fin de la liste des contributions et travaux voisins, n'est pas reprise), puis les annexes pages 24, 25, 28, 29, 30
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]`. Les tableaux sont reconstitués en mode mise en page (colonnes séparées par « | » ; les chiffres sont ceux du PDF, la grille est approximative : en cas de doute, se reporter à la page citée). Les formules sont extraites en texte linéaire, parfois dans le désordre. Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : p.11, le cas « Novel Combinatorial Attack Strategies » (invite brute et réécriture complète de l'attaquant, avec son raisonnement) ; annexe B (gabarits d'invites de l'attaquant, du défenseur et de la distillation), annexe F (taxonomie fine des stratégies d'attaque avec définitions et exemples, p.30-37), tableau 16 (exemples d'attaques découvertes, p.40) et paramètres détaillés des attaques (tableau 7). Restent : les noms des classes d'attaque évaluées (GCG, PAIR, TAP, AutoDAN, AutoDAN-turbo), le protocole, les résultats et les limites. Retiré par économie de place : travaux voisins, démonstrations, tableau 2 (capacités générales), annexes G et suivantes (ablation complète), bibliographie.

---

[p.1]

Ensuring robust safety alignment is crucial for Large Language Models (LLMs), yet existing defenses often lag behind evolving adversarial attacks due to their reliance on static, pre-collected data distributions. In this paper, we introduce MAGIC, a novel multi-turn multi-agent reinforcement learning framework that formulates LLM safety alignment as an adversarial asymmetric game. Specifically, an attacker agent learns to iteratively rewrite original queries into deceptive prompts, while a defender agent simultaneously optimizes its policy to recognize and refuse such inputs. This dynamic process triggers a co-evolution, where the attacker’s ever-changing strategies continuously uncover long-tail vulnerabilities, driving the defender to generalize to unseen attack patterns. Remarkably, we observe that the attacker, endowed with initial reasoning ability, evolves novel, previously unseen combinatorial strategies through iterative RL training, underscoring our method’s substantial potential. Theoretically, we provide insights into a more robust game equilibrium and derive safety guarantees. Extensive experiments validate our framework’s effectiveness, demonstrating superior defense success rates without compromising the helpfulness of the model. Our code is available at https://github.com/BattleWen/MAGIC.

[COUPÉ : avertissement sur les textes offensants ; introduction]

[p.2]

how to endow the attacker model with initial offensive reasoning capabilities and (2) how to iteratively optimize decoupled agents. For the first problem, prior methods typically rely on static red-teaming datasets or heuristic mutations (Liu et al., 2023). While these approaches can bypass simple filters, they lack the strategic reasoning capabilities required for complex, multi-turn deception. Ideally, we aim to empower the attacker with autonomous reasoning, but progress in this direction is bottlenecked by a scarcity of high-quality Chain-of-Thought (CoT) data tailored for offensive scenarios (Chao et al., 2023). This scarcity prevents the emergence of novel, non-templated attack patterns, as shown in Fig. 1 left. For the second problem, recent works like AdvEvo-MARL (Pan et al., 2025) emphasize the topological safety in multi-agent systems rather than intrinsic robustness of individual models. Conversely, Self-RedTeam (Liu et al., 2025) employs shared-parameter self-play, where a single model alternates between attacker and defender roles. This setup inevitably leads to gradient conflicts by imposing opposing objectives onto the same parameter space, as shown in Fig. 1 right. Moreover, these frameworks often model the interaction as a symmetric normal-form game, neglecting the inherently asymmetric and sequential nature of real-world interaction scenarios. To systematically address these challenges, we introduce MAGIC (Multi-Agent Adversarial Game for Improving safety and Compliance), a novel multi-turn multi-agent reinforcement Learning (MARL) framework. MAGIC models LLM safety alignment as an adversarial interaction between an attacker and a defender, employing an asymmetric design with distinct roles and objectives. This design enables both agents to co-evolve through iterative interactions. To enhance adversarial exploration, we further construct an Attack Pool Benchmark initialized with diverse CoT rewriting strategies for automated red-teaming. Combined, these components facilitate stable training and promote progressively more challenging attacks. In conclusion, our contributions are summarized as follows:

[COUPÉ : liste des contributions (cadre de jeu séquentiel asymétrique, banque d'attaques avec raisonnement par chaîne de pensée, expériences) ; page 3 entière (fin de la liste des contributions, section 2 « Related Work » : travaux voisins sur les attaques de contournement et sur l'alignement par jeux multi-agents)]

[p.4]

3. Problem Formalization The problem of language model red-teaming is formulated as a two-player sequential game. The attacker first selects an attack prompt 𝑦𝐴 ∈ 𝒴𝐴 , the defender selects 𝑦𝐷 ∈ 𝒴𝐷 after observing 𝑦𝐴 . The rewards obtained by attacker and defender are 𝑟𝐴 (𝑦𝐴 , 𝑦𝐷 ) and 𝑟𝐷 (𝑦𝐴 , 𝑦𝐷 ), respectively. The attacker’s strategy is represented as 𝜋𝐴 , and the defender’s strategy is a conditional distribution 𝜋𝐷 (·|𝑦𝐴 ). We define “safety" as 𝑟𝐷 (𝑦𝐴 , 𝑦𝐷 ) ≥ 0 and “unsafety" as 𝑟𝐷 (𝑦𝐴 , 𝑦𝐷 ) < 0. Since this is a sequential game, the most natural equilibrium concept is the SPNE. It requires that the defender takes an optimal response in each subgame (i.e., for each 𝑦𝐴 ), not just the expected 𝑦𝐴 under 𝜋𝐴 .

[COUPÉ : définition 3.1 (équilibre de Nash parfait en sous-jeux) et équations (1) et (2)]

Theorem 3.2. Assume that for any 𝑦𝐴 , there exists a rejection or safe fallback action 𝑦ref such that * , 𝜋 * ) satisfies that for any 𝑦 ∈ 𝒴 and 𝑦 𝑟𝐷 (𝑦𝐴 , 𝑦ref ) ≥ 0. Then, any SPNE (𝜋𝐴 𝐷 𝐴 𝐴 𝐷 ∈ 𝒴𝐷 such that * 𝜋𝐷 (𝑦𝐷 |𝑦𝐴 ) > 0: 𝑟𝐷 (𝑦𝐴 , 𝑦𝐷 ) ≥ 0. (3)

[COUPÉ : section 4, introduction]

Unlike Liu et al. (2025), which guarantees safety only in expectation under Nash equilibrium, we adopt subgame perfect Nash equilibrium and obtain stronger pointwise safety guarantees.

[p.5]

We explicitly formulate the safety alignment process as a multi-agent adversarial sequential game between Attacker (𝜋𝐴 ) and Defender (𝜋𝐷 ). The training process consists of two phases: (1) Offensive Capability Initialization, and (2) Iterative Co-evolution by RL Training, as shown in Fig. 2. Phase 1: Offensive Capability Initialization. We observe that directly employing a base model (e.g. Llama3.1-8B-Instruct) as an attacker results in a high refusal rate when attempting to rewrite harmful queries. To address this cold-start problem, we construct an Attack Pool Benchmark and employ it to perform Supervised Fine-Tuning (SFT) on the attacker model 𝜋𝐴 . Specifically, we leverage Gemini-2.5-Pro (Comanici et al., 2025) to enrich SorryBench (Xie et al., 2024) with high-quality CoT completions. The training objective is to minimize the negative log-likelihood of the adversarial prompt 𝑦𝐴 given the seed query 𝑥:

This step equips the attacker with generalizable initial capabilities, enabling it to actively discover vulnerabilities. Phase 2: Iterative RL Training. To ensure safety without compromising general capability, we construct a reinforcement learning dataset 𝒟RL containing an equal mix of harmful queries and benign instructions. We employ Group Relative Policy Optimization (GRPO) (Guo et al., 2025a) for parameter updates. We approximate the bilevel optimization structure via an alternating procedure that decouples the inner and outer problems:

• Defender Optimization: This step corresponds to solving the inner maximization problem in Eq. (1). We freeze the attacker 𝜋𝐴 to fix the attack distribution. For a generated adversarial constraint 𝑦𝐴 (derived from seed 𝑥), the defender 𝜋𝐷 explores the action space by generating (𝑖) (𝑖) a group of 𝐺 diverse responses {𝑦𝐷 }𝐺 𝑖=1 , where 𝑦𝐷 ∼ 𝜋𝐷 (·|𝑦𝐴 ). The policy 𝜋𝐷 is updated to maximize safety rewards given 𝑦𝐴 , effectively pushing the defender towards the pointwise best response.

[COUPÉ : optimisation de l'attaquant (figure 2 et suite)]

[p.6]

[COUPÉ : suite de l'optimisation de l'attaquant, objectif GRPO (équations (5) et (6)), section 4.2 :]

Note: Through ablation studies (Tab. 5), we found that enforcing this format on the defender (using base models like Qwen2.5 or Llama3.1) degrades general capability. Thus, 𝑅fmt is only applied to the attacker. 2. Harmfulness Reward (𝑅harm ). This is the core metric for safety. We employ Qwen3Guard (Zhao et al., 2025) as our reward model, which provides robust and precise reward signals. We adopt a strict safety standard where responses labeled as “controversial" are also treated as harmful. {︃ −𝑟harm if 𝑦𝐷 is unsafe/controversial 𝑅harm (𝑦𝐷 ) = (8) +𝑟harm if 𝑦𝐷 is safe

3. Refusal Reward (𝑅ref ). To prevent the defender from falling into an “over-safety" collapse (i.e., refusing all queries), we introduce a refusal reward. Also judged by Qwen3Guard, this reward penalizes both false positives (refusing safe queries) and false negatives (answering unsafe queries): ⎧ ⎪ ⎪ ⎪ +𝑟ref if 𝑥 is unsafe and 𝑦𝐷 refused ref if 𝑥 is unsafe and 𝑦𝐷 not refused ⎪ ⎨−𝑟 𝑅ref (𝑦𝐷 ) = (9) ⎪ ⎪ ⎪ −𝑟ref if 𝑥 is safe and 𝑦𝐷 refused ref if 𝑥 is safe and 𝑦𝐷 not refused ⎪ ⎩+𝑟

[p.7]

Final Reward Formulation. The interaction regarding safety is modeled as a zero-sum game, while auxiliary constraints are agent-specific. The total rewards for the Defender (𝑅𝐷 ) and Attacker (𝑅𝐴 ) are:

𝑅𝐷 = 𝑅harm (𝑦𝐷 ) + 𝑅ref (𝑦𝐷 ), (10) 𝑅𝐴 = −𝑅𝐷 + 𝑅fmt (𝑦𝐴 ). (11)

Models. We use instruction-tuned models from the Qwen2.5 and Llama3.1 families covering multiple model sizes. Unless otherwise specified, Qwen3Guard (Zhao et al., 2025) serves as the reward model during training and as the safety judge in subsequent evaluations. We additionally conduct a comparative analysis of safety judgments produced by Qwen3Guard and GPT-4o (§D.3). Training dataset. For the SFT phase, we construct a CoT training set containing both harmful and benign examples. The harmful subset is constructed from SorryBench (Xie et al., 2024), which contains 440 vanilla prompts and 8,800 adversarial harmful prompts covering 20 linguistic mutation strategies (e.g., role-playing and persuasion). Since SorryBench only provides paired vanilla and

[p.8]

[COUPÉ : suite de la description des jeux de données d'entraînement]

We evaluate both safety capability and general capability. When evaluating Self-RedTeam on the Qwen2.5 model family, we use the open-source checkpoints released on HuggingFace. For the Llama3.1 model family, we directly report the results from the original paper without re-running the experiments. Safety evaluation. We adopt Qwen3Guard as the safety moderation model to assess both queries and responses, and we follow Ai2’s safety (Han et al., 2024; Jiang et al., 2024b) evaluation suite. We evaluate two aspects: (1) harmful refusal, i.e., the model’s ability to refuse harmful prompts, measured on the HarmBench vanilla and adversarial splits (Mazeika et al., 2024), WildGuardTest (Han et al., 2024), the WildJailBreak adversarial-harm split (Jiang et al., 2024b), OR-Bench-Toxic (Cui et al., 2024), XSTest contrast categories (Röttger et al., 2023), StrongREJECT (Souly et al., 2024), and DAN (DoAnythingNow) (Shen et al., 2023); and (2) benign compliance, measured on XSTest all-safe categories (Röttger et al., 2023), the WildJailBreak adversarial-benign split (Jiang et al., 2024b). (3) For multi-turn evaluation, we adopt X-Teaming (Rahman et al., 2025), which generates multi-turn attacks via agent planning. More detailed benchmarks descriptions are provided in the Appendix §D.1. General capabilities evaluation. To assess whether adversarial training impacts instruction following and general capabilities, we consider two types of benchmarks: (1) rule-based evaluations, including MMLU (Hendrycks et al., 2021), ARC-Challenge (Clark et al., 2018), GPQA (Rein et al., 2023), and IFEval (Zhou et al., 2023); and (2) judge-based evaluation using AlpacaEval 2 (Dubois et al., 2024). More details are provided in the Appendix §D.2.

Question1: Does MAGIC’s safety gain come at the cost of over-refusal?

Our proposed method, MAGIC, demonstrates consistent and substantial safety improvements across multiple benchmarks, model families, and scales (Tab. 1). On benchmarks like WildGuardTest, HarmBench, and DAN, it effectively suppresses harmful behaviors under both vanilla and adversarial prompts. Taking Qwen2.5-7B-Instruct as a representative case, MAGIC reduces the Attack Success Rate (ASR) on WildGuardTest from 36.5% to just 2.3%. Beyond improving safety, MAGIC also maintains strong benign compliance and does not introduce excessive refusals. On benchmarks designed to evaluate benign behavior, particularly under adversari-

[p.9]

Table 1: Safety evaluation on harmful refusal and benign compliance. Lower Attack Success Rate (ASR) indicates stronger refusal; higher Robustness to Attacks (RTA) / Compliance Rate (Comply) indicates better safety and helpfulness.

Harmful Refusal | Benign Compliance
Method | WG:Test | WJB | DAN | HarmBench | OR-Bench | XSTest | StrongREJECT | WJB | XSTest
ASR↓ | ASR↓ | ASR↓ | ASR↓ | RTA↑ | RTA↑ | RTA↑ | ASR↑ | Comply↑
adv | van. | adv | adv | adv | van. | van. | van. | van. | adv | van.
harm | harm | harm | harm | harm | harm | harm | harm | harm | benign | benign
Qwen2.5-7B-Instruct | 0.365 | 0.038 | 0.701 | 0.327 | 0.363 | 0.250 | 0.892 | 0.800 | 0.964 | 0.992 | 0.940
+ Self-RedTeam | 0.255 | 0.017 | 0.442 | 0.323 | 0.237 | 0.047 | 0.973 | 0.825 | 0.988 | 0.980 | 0.904
+ MAGIC(ours) | 0.023 | 0.002 | 0.198 | 0.043 | 0.055 | 0.019 | 0.977 | 0.860 | 0.988 | 0.968 | 0.945
Qwen2.5-14B-Instruct | 0.228 | 0.036 | 0.583 | 0.173 | 0.171 | 0.094 | 0.899 | 0.820 | 0.978 | 1.000 | 0.936
+ Self-RedTeam | 0.065 | 0.005 | 0.402 | 0.136 | 0.083 | 0.006 | 0.963 | 0.860 | 0.990 | 0.992 | 0.924
+ MAGIC(ours) | 0.009 | 0.000 | 0.076 | 0.003 | 0.013 | 0.006 | 0.996 | 0.915 | 0.994 | 0.944 | 0.888
Llama3.1-8B-Instruct | 0.187 | 0.046 | 0.659 | 0.517 | 0.213 | 0.094 | 0.881 | 0.950 | 0.983 | 0.992 | 0.908
+ Self-RedTeam | 0.094 | 0.003 | 0.214 | 0.239 | 0.144 | 0.044 | 0.942 | 0.943 | 0.958 | 0.936 | 0.949
+ MAGIC(ours) | 0.012 | 0.002 | 0.147 | 0.050 | 0.017 | 0.000 | 0.945 | 0.960 | 0.989 | 0.968 | 0.932

[COUPÉ : tableau 2 (capacités générales) ; commentaire sur la conformité aux requêtes bénignes]

[p.10]

Table 3: Defender generalization evaluation on HarmBench using the OpenRT (Shanghai AI Lab, 2026) with GPT-4o as the judge model.

Attacker (HarmBench ASR↓)(%)
Defender | no-rev | GCG | PAIR | TAP | AutoDAN | AutoDAN turbo
Gemini-2.5-Flash | 27.50 | - | 37.50 | 40.63 | 44.38 | 35.00
Qwen2.5-7B-Instruct | 25.62 | 43.90 | 44.38 | 63.75 | 47.81 | 75.00
+ Self-Eval | 24.06 | 28.75 | 37.19 | 50.00 | 42.81 | 89.06
+ SmoothLLM | 19.38 | 20.00 | 30.63 | 61.25 | 62.19 | 70.31
+ Self-RedTeam | 19.38 | 22.50 | 31.88 | 40.00 | 30.31 | 66.88
+ MAGIC(ours) | 13.44 | 11.25 | 25.31 | 35.63 | 24.38 | 54.69

Notably, unlike Self-RedTeam, which mixes in SFT updates on a self-distilled dataset concurrently with RL, MAGIC trains the defender using RL alone.

[COUPÉ : question 3 (attaques à plusieurs tours : texte)]

Table 4: Multi-turn evaluation results from X-Teaming. The multi-turn ASR counts an attack as successful if any of the 10 adversarial rewriting strategies for a harmful seed succeed; JailBreak Rate measures the fraction of adversarial prompts that jailbreak models.

Model | Multi-turn ASR↓ | Imp. (ASR)↑ | JailBreak Rate↓ | Imp. (JB)↑
Qwen2.5-7B-Instruct | 94.9% | – | 50.7% | –
+ Self-RedTeam | 89.9% | 5.27% | 50.4% | 0.6%
+ MAGIC(ours) | 85.4% | 10.1% | 43.0% | 15.2%

[COUPÉ : question 4 (évolution de l'attaquant : texte)]

[p.11]

[COUPÉ : figure 3 (carte thermique des évaluations croisées) ; cas d'attaque retiré pour sûreté]

Moreover, we evaluate the transferability of the MAGIC-trained attacker’s jailbreak capability across diverse defender models, and use an Attacker-base setting for comparative attack pattern analysis (Appendix §E, Appendix §F).

Surprisingly, we observe that under iterative reinforcement learning, the attacker is able to evolve novel and previously unseen combinatorial attack strategies, as shown in Case 5.3 (see Tab. 16 for additional cases). This finding is similar to that of Yuan et al. (2025), which suggests that RL can teach LLMs genuinely new, generalizable skills by incentivizing the composition of previously learned atomic skills, rather than merely reranking existing behaviors.

[p.12]

Table 5: Ablation summary on safety, compliance, and instruction following (Qwen2.5-7B-IT).

Harmful Refusal | Benign Compliance Instruct Following
Method | WJB StrongREJECT | WJB | XSTest | AlpacaEval 2
ASR↓ | RTA↑ | ASR↑ | Comply↑ | LC Win↑
adv harm van. harm adv benign van. benign | vs gpt4-turbo
Qwen2.5-7B-Instruct | 0.701 | 0.964 | 0.992 | 0.940 | 33.733%
+ No-Game | 0.127 | 0.988 | 0.496 | 0.996 | 34.481%
+ Defender-only | 0.127 | 0.994 | 0.916 | 0.812 | 23.491%
+ w/ def. CoT | 0.136 | 0.986 | 0.900 | 0.700 | 30.791%
+ MAGIC-base | 0.080 | 0.977 | 0.876 | 0.888 | 28.184%
+ MAGIC(ours) | 0.198 | 0.988 | 0.968 | 0.945 | 33.224%

[COUPÉ : description des variantes d'ablation (sans jeu, défenseur seul, attaquant de base, MAGIC)]

6. Conclusion In this paper, we introduced MAGIC, a multi-turn multi-agent adversarial reinforcement learning framework that formulates LLM safety alignment as an asymmetric sequential game between an attacker and a defender. By decoupling their objectives and enabling iterative co-evolution, MAGIC allows the attacker to continuously uncover diverse, long-tail vulnerabilities, while guiding the defender to learn robust refusal behaviors that generalize beyond static adversarial data. Both our theoretical analysis and extensive empirical results demonstrate that this game-theoretic formulation leads to improved safety robustness while largely preserving benign compliance and instruction-following capabilities. While effective, this online adversarial paradigm introduces computational overhead and requires careful management of training dynamics. Additionally, the attacker’s exploration is highly sensitive to the SFT initialization and the attacker model’s capacity. Future work may extend MAGIC to multimodal or tool-use settings, improve scalability, and explore alternative game-theoretic formulations. We hope this work inspires a shift toward treating safety alignment as a evolving process.

[p.24]

Table 6: Key training hyperparameters.

Setting | Value
Training order | Defender → Attacker
Training step | 300 steps (early stop in step200)
GPUs | 4 GPUs per role
Training batch sizes | 64
Eval batch sizes | 256
Max prompt lengths | 8192
Max response lengths | 6144
Learning rate | 1 × 10−6
Rollout number | 𝑛=4
Rollout temperature | 𝑡 = 1.0
KL loss coeff | 𝛽=0
Switching frequency | 15
Update ratio | 1:1
Reward | 𝑟harm = 1.0, 𝑟ref = 0.5, 𝑟fmt = 0.5

[COUPÉ : description des défenses de comparaison, jeux de données de mise au point supervisée]

[p.25]

Evaluation setup. Unless otherwise stated, we set the sampling temperature to 0 and cap the generation length at 8,192 tokens, including both the reasoning process and the final answer. We then truncate the final answer to 512 tokens and feed it to judge model to assess harmfulness and refusal. This evaluation pipeline strictly follows the implementation in Liu et al. (2025). For the publicly available Qwen2.5 family models in the Self-Redteam evaluation, we use Qwen3Guard (Zhao et al., 2025) as the judge model. For the unreleased Llama models, in order to align with the evaluation results of Self-RedteamLiu et al. (2025), we select WildGuard (Han et al., 2024) as the evaluation model.

[p.28]

Reward Model Accuracy. The choice of reward/judge model can affect evaluation outcomes. GPT- 4o provides a dense harmfulness score on a 0-5 scale (counting an attack as successful only when the score equals 5), whereas Qwen3Guard produces a binary harmful/harmless prediction (0/1). To compare these signals, we evaluate responses generated by Qwen2.5-7B-IT on HarmBench vanilla prompts and score them with both judges. We find that the resulting ASR is similar (25.625% with GPT-4o vs. 24.063% with Qwen3Guard), indicating broadly consistent binary decisions. However, the calibrated score distributions differ substantially: after normalization, the mean score is 0.24 for Qwen3Guard and 0.49 for GPT-4o (equivalently 2.44 on the 0-5 scale). This gap helps explain why evaluations of stronger trained defenders (e.g., MAGIC on HarmBench) can diverge across judges: GPT-4o provides a more fine-grained and more rigorous signal, which better distinguishes between closely performing defenses.

[COUPÉ : autres résultats de généralisation]

[p.29]

[COUPÉ : annexe E, transférabilité de l'attaquant :]

Defenders. We consider: (i) open instruction-tuned models, including Qwen2.5-7B-IT, Llama3.1- 8B-IT (safety-aligned), and Mistral-7B-IT (Jiang et al., 2023); (ii) a proprietary model, Gemini-2.5- Flash (Comanici et al., 2025); and (iii) MAGIC-defender, obtained by training a defender with MAGIC starting from Qwen2.5-7B-IT.

Attackers. We compare a base attacker (Qwen2.5-7B-IT) against our MAGIC-attacker.

Protocol. We sample 600 vanilla harmful prompts from the WildJailbreak test split as seeds. Both attackers and defenders use the same prompting template (Appendix §B). The attacker rewrites each seed once (temperature 0.0; single rollout), the defender answers the rewritten prompt, and GPT-4o judges attack success following the OpenRT pipeline (Shanghai AI Lab, 2026).

[p.30]

Results. As shown in Tab. 10, MAGIC-attacker substantially increases ASR across all base defenders, indicating that the learned jailbreak behaviors transfer across model families rather than overfitting to a single target. Meanwhile, the MAGIC-defender exhibits notably stronger robustness to both attackers, and is particularly resilient to MAGIC-attacker: because MAGIC-defender is co-trained against (and thus aligned to) the MAGIC-attacker’s rewrite distribution, the MAGIC-attacker’s advantage largely disappears on MAGIC-defender and can even be slightly weaker than the base attacker in this setting.

Table 10: Attack success rate (%) on 600 WildJailbreak vanilla harmful prompts, judged by GPT-4o following OpenRT (Shanghai AI Lab, 2026). Each attacker produces a single rewrite per seed (single rollout; temperature 0.0). Lower ASR indicates a stronger defender.

Defender (ASR↓)
Attacker | Qwen2.5-7B-IT | Llama3.1-8B-IT | Mistral-7B-IT | Gemini-2.5-Flash | MAGIC-defender
Base | 37.33 | 25.00 | 46.83 | 24.67 | 10.50
MAGIC-attacker | 58.00 | 35.83 | 64.17 | 31.33 | 9.00

[COUPÉ : annexe F (analyse des motifs d'attaque par un classifieur sur les réécritures de l'attaquant ; définitions et exemples retirés pour sûreté)]
