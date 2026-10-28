# EXTRAIT — EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution

- Auteurs : Xiaozhe Zhang, Chaozhuo Li, Hui Liu, Shaocheng Yan, Bingyu Yan, Qiwei Ye, Haoliang Li (université de la ville de Hong Kong, Pékin, Wuhan, Beihang) ; année : 2026 (cachet arXiv du 13 mai 2026 ; le corps du PDF porte « Date: May 8, 2026 ») ; identifiant : arXiv:2605.13411v1 (48 pages)
- Statut : préimpression arXiv cs.CR (cachet p.1) ; le PDF porte l'avertissement « This paper contains potentially harmful text »
- PDF source : `docs/sources/pdf/2605.13411v1.pdf` (branche main, non lue ici) ; SHA-256 du PDF : `a81514c51c33b6f8def74bb6df11c5f733cfe256bbc21768f607a3dc0e0029c0` (compagnon `.sha256` fourni, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1, 3-11, 31, 48
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, lignes rejointes en paragraphes ; formules extraites en texte linéaire, parfois dans le désordre, et alors coupées), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux extraits en mode mise en page (colonnes séparées par « | »). Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : annexe A.2.3 (construction détaillée de la bibliothèque de compétences d'attaque) ; annexe B.5 (exemple d'invite adverse construite à partir d'une compétence, p.32) ; annexes B.6, B.7 et D (données d'amorçage du défenseur, invites des juges, études de cas contenant des invites adverses réelles, p.33-47). Gardés : protocole de co-évolution, récompenses, partition de la bibliothèque (noms publics des méthodes sources), protocole d'évaluation, résultats, analyse de coût, limites.

---

[p.1]

Abstract Large language models remain vulnerable to adversarial prompts that elicit harmful outputs. Existing safety paradigms typically couple red-teaming and post-training in a closed, policy-centric loop, causing attack discovery to suffer from rapid saturation and limiting the exposure of novel failure modes, while leaving defenses inefficient, rigid, and difficult to transfer across victim models. To this end, we propose EvoSafety, an LLM safety framework built around persistent, inspectable, and reusable external structures. For red teaming, EvoSafety equips the attack policy with an adversarial skill library, enabling continued vulnerability probing through simple library expansion after saturation, while supporting the evolution of adversarial vectors. For defense learning, EvoSafety replaces model-specific safety fine-tuning with a lightweight auxiliary defense model augmented with memory retrieval. This enables efficient, transferable, and model-agnostic safety improvements, while allowing robustness to be enhanced solely through memory updates. With a single training procedure, the defense policy can operate in both Steer and Guard modes: the former activates the victim model’s intrinsic defense mechanisms, while the latter directly filters harmful inputs. Extensive experiments demonstrate the superiority of EvoSafety: in Guard mode, it achieves a 99.61% defense success rate, outperforming Qwen3Guard-8B by 14.13% with only 37.5% of its parameters, while preserving reasoning performance on benign queries. Warning: This paper contains potentially harmful text.

[COUPÉ : p.1-2 introduction (sauf le dernier paragraphe), figure 1, p.3 travaux voisins (équipe rouge, alignement)]

[p.3]

[COUPÉ] Our contributions are as follows: • We introduce EvoSafety, a framework that equips both attack and defense policies with external structures. By mitigating attack saturation and eliminating model-specific safety fine-tuning, EvoSafety supports lifelong, model-agnostic safety improvement. • EvoSafety is a co-evolutionary framework that demonstrates steady performance gains across rounds. To our knowledge, EvoSafety is the first RL-driven approach that bridges external skill use and the evolving landscape of novel attack vectors. • Experiments demonstrate that EvoSafety significantly strengthens safety without compromising general reasoning ability. In Guard mode, it achieves a 98.83% defense success rate against unseen attacks and outperforms Qwen3Guard while using fewer parameters.

[p.4]

Fig. 2 illustrates the architecture of EvoSafety, a co-evolutionary framework designed to iteratively optimize an Attack Policy 𝜋 𝐴 (Section 3.2) and a Defense Policy 𝜋 𝐷 (Section 3.3). For a given request 𝑟 , the process begins with the Skill Retriever fetching two expert skills 𝑒𝑠 from the Adversarial Skill Library to condition 𝜋 𝐴 , which in turn generates an adversarial prompt 𝑎𝑡 . Subsequently, the Memory Retriever identifies the top-2 relevant successful historical attacks 𝑒𝑚 from the Verified Memory Bank. These retrieved memories serve as references for 𝜋 𝐷 to produce a safety prefix 𝑑𝑡 tailored to 𝑎𝑡 . The frozen victim model T then processes the concatenated input [ 𝑑𝑡 ; 𝑎𝑡 ] to yield response 𝑦𝑡 , from which rewards are derived to update both policies. This process is detailed in Algorithm 1, where 𝜋 𝐴

[p.5]

[COUPÉ] After training, the learned defense policy 𝜋 𝐷 can be deployed in two distinct modes: Steer and Guard. Given a new prompt 𝑎new 𝑡 (potentially harmful or benign) and an arbitrary new victim model T new , both modes first sample a defense prefix 𝑑𝑡 ∼ 𝜋 𝐷 (· | 𝑒𝑚 , 𝑎new 𝑡 ). In Steer mode, the final response 𝑦𝑡 is generated by prepending the prefix to the prompt: 𝑦𝑡 ∼ T new [ 𝑑𝑡 ; 𝑎new . This mode aims to steer  𝑡 ] the victim model’s internal latent states to activate its intrinsic safety mechanisms, thereby eliciting a harmless response. In Guard mode, the system treats 𝑑𝑡 as a diagnostic signal. If 𝑑𝑡 is predicted to trigger a refusal from the victim model, the input is filtered; otherwise, the system proceeds with a standard rollout. Further details are provided in Appendix A.3.2.

Heterogeneous Attack Artifacts and Structured Skill Representation. Expert-crafted attack strategies manifest in heterogeneous forms, ranging from executable code to natural language descriptions. To cover a broader spectrum of attack vectors, we incorporate all such artifacts and leverage the proposed Dual-Path Skill Grounding to map them into a unified structured representation. Each skill is encapsulated by an executable script and a corresponding Markdown specification. The script converts standard requests into adversarial rewrites and may incorporate external APIs or local models to assist generation or enable gray-box attacks. The Markdown file documents the skill’s identity, provenance, and a high-level attack schema abstracted from the script. This dual representation preserves both execution details and strategic logic, thereby facilitating downstream skill induction and improving the generalization of attack policies. Tri-Axis Skill Validation. We implement multi-stage filtering to retain only skills that meet three criteria. (1) Functional validity measures the effectiveness of a skill via its attack success rate. (2) Schema consistency evaluates the fidelity of the derived high-level attack schema. (3) Behavioral diversity encourages each candidate skill to differ from the existing skill set. Skill Family Induction. We use the executable scripts and attack schemas of the validated skills to synthesize additional skills that follow the same strategic schema while differing in execution. The synthesized skills are then filtered using Tri-Axis Skill Validation, yielding a scalable adversarial skill library. Further details are provided in Appendix A.2.3.

[p.6]

To provide empirical references for safety-prefix generation and reduce the optimization burden, we avoid requiring the Auxiliary Defense Model 𝜋 𝐷 to learn a complex prompt-to-prefix mapping entirely from scratch. Instead, we equip it with a lightweight yet effective Verified Memory Bank B = { 𝑎 ( 𝑖 ) } 𝑖𝑁=1 , which stores only historical adversarial prompts. Given a new prompt 𝑎𝑡 , 𝜋 𝐷 first retrieves a support set N𝑘 ( 𝑎𝑡 ) ⊂ B containing the top-𝑘 semantically similar past attacks via efficient vector-based retrieval, and then generates the defense prefix according to

A straightforward approach is to train the defense policy using the negative of R judge ( 𝑟, 𝑦𝑡 ) in Eq. 3 as the reward. However, as discussed in Appendix A.3.1, optimizing this objective solely on harmful requests can lead to degenerate solutions: the policy may learn input-agnostic refusal patterns, such as producing a generic refusal prefix. To avoid this reward hacking, we instead define the reward over a mixture of benign and adversarial requests. For benign requests 𝑟 ∈ Dben , responses are scored by a correctness indicator 𝕀corr ( 𝑦𝑡 ) ∈ {0, 1}. We construct Dben offline from queries on which a surrogate model is consistently correct with low output variance, so that low rewards are more likely to reflect safety-prefix-induced errors rather than intrinsic reasoning uncertainty. While this filtering improves attribution, it also eliminates most intra-group ranking signals under GRPO Shao et al. [2024]: completions often receive identical

[COUPÉ : p.7 équation 6 (récompense du défenseur, mise en forme linéaire illisible) ; sa description suit]

[p.7]

[COUPÉ] We set the base correctness reward to 𝛼 = 0.8 and the shaping coefficient to 𝛽 = 0.2. For adversarial requests (𝑟 ∈ Dadv ), the reward is obtained by directly mapping the judge model’s safety classification to a scalar value.

Models. We initialize the attack policy from Mistral-7B-Instruct-v0.3. To improve defensive efficiency, we use Llama-3.2-3B-Instruct as the auxiliary defense model. For retrieval, we adopt Qwen3-Embedding-0.6B [Zhang et al., 2025] as the embedding backbone. We further employ Qwen3Guard-Gen-8B [Zhao et al., 2025] for two purposes: providing reward signals during training and serving as the safety/refusal judge during evaluation. Adversarial Skill Library and Verified Memory Bank. We partition the Attack Skill Library into an initial attack skill library, used for training, and a held-out attack skill library, used to evaluate out-of-library generalization and the framework’s capacity for sustained evolution. We also maintain a Verified Memory Bank as a growing repository of concrete adversarial prompts. We initialize this bank with adversarial prompts from WildJailbreak [Jiang et al., 2024] and continually expand it with prompts generated by attacker rollouts during training. Datasets and Metrics. We construct adversarial training data from AdvBench [Chen et al., 2022], CategoricalQA [Bhardwaj et al., 2024], HarmfulQA [Bhardwaj and Poria, 2023], DangerousQA [Shaikh et al., 2023], and PKU-SafeRLHF [Ji et al., 2025], following prior work [Guo et al., 2025b, Wang et al., 2026]. The constraint-satisfying benign examples used for RL-based defense training are sampled from GSM8K [Cobbe et al., 2021]. For evaluation, we adopt the standard HarmBench [Mazeika et al., 2024] behaviors to assess both attack and defense methods, and report attack success rate (ASR) to measure offensive effectiveness and defensive robustness. To examine whether improved defensive behavior trades off with general capabilities, we further evaluate on GSM8K [Cobbe et al., 2021] and MMLU [Hendrycks et al., 2020]. [COUPÉ]

[p.8]

Table 1 | ASR@1 (%) of different attack methods across multiple victim models. Values before and
after the slash denote results from Qwen3Guard [Zhao et al., 2025] and LLM-as-a-Judge, respectively.
For multi-turn methods, superscript denotes the number of interaction turns.
Open-Weight | Closed-Source
Attacker | Avg.
3-4B | 3.1-8B | 3.1-70B | 5.1 | 3-Flash
Single-Turn Methods
PAP [Zeng et al., 2024a] | 58.1/37.9 | 33.5/16.5 | 47.5/36 | 91.5/71.5 | 45/15 | 73/50.5
FlipAttack [Liu et al., 2024b] | 23.2/22.3 | 3.5/3.5 | 0/0 | 0/0 | 28/27.5 | 84.5/80.5
ArrAttack [Li et al., 2025] | 16.0/12.5 | 13.5/10.0 | 6.5/4.5 | 41.0/34.5 | 2.0/0.5 | 17.0/13.0
Jailbreak-R1 [Guo et al., 2025b] | 27.5/21.6 | 22/17.5 | 11.5/8.5 | 59/50 | 5/1.5 | 40/30.5
Multi-Turn Methods
ActorAttack (5) [Ren et al., 2024b] | 75.4/40.9 | 73/35.5 | 71.5/41 | 75/40.5 | 71/33 | 86.5/54.5
X-Teaming (7) [Rahman et al., 2025] | 80.1/71.9 | 73/68 | 75.5/69.5 | 97.5/95 | 77.5/58.5 | 77/68.5
FITD (11) [Weng et al., 2025] | 44.0/35.2 | 29.5/19 | 51.5/44 | 72/63 | 12/4 | 55/46
ICON (3) [Lin et al., 2026] | 90.2/84.7 | 98/98 | 96.5/94.5 | 100/100 | 69/49.5 | 87.5/81.5
Ours | 92.8/86.3 | 98/97 | 98.5/95 | 100/100 | 80.5/59.5 | 87/80
Ours (zero-shot) | 84.6/74.8 | 96/93.5 | 84.5/79 | 91.5/79.5 | 74/50.5 | 77/71.5

[RQ1-1] Main Attack Performance. We evaluate the attacker under both Qwen3Guard [Zhao et al., 2025] and GPT-4.1 as LLM-as-a-Judge to rule out the possibility that high ASR is driven by evaluator overfitting during training. As shown in Tab. 1, our method significantly outperforms the RL-based baseline Jailbreak-R1 [Guo et al., 2025b] by 65.3% in ASR, and even surpasses the state-of-the-art multi-turn method ICON [Lin et al., 2026] by 2.6% with a single interaction. In Appendix D.1, we demonstrate the capability of our framework to evolve novel attack vectors autonomously. [RQ1-2] Zero-shot Attack Performance on New Skills. We further retrieve skills from the held-out attack skill library to assess generalization. As shown in the last row of Tab. 1, the performance drops marginally and remains superior to most multi-turn methods, with a 12.18% higher average ASR. This indicates that the attacker learns how to exploit diverse skills effectively, enabling the continual discovery of novel attack vectors simply by expanding the skill library with newly extracted skills, without requiring attacker retraining. [RQ1-3] Scalability. We also evaluate the attacker’s ability to convert extra attempt budgets into higher ASR. We define ASR@ 𝑁 as the fraction of harmful queries for which at least one jailbreak succeeds within 𝑁 attempts. As shown in Fig. 3, small open-weight models reach 100% success with just 𝑁 = 2, while GPT-5.1 requires only five attempts.

[RQ2-1] Can Our Defender Activate the Victim Model’s Intrinsic Safety? We evaluate defense performance against skill-unseen method (entirely OOD), i.e., Jailbreak-R1 [Guo et al., 2025b]; skill-seen methods, i.e., CodeAttack [Ren et al., 2024a] and GPTFuzz [Yu et al., 2023]; and the co-evolved matched attacker.1 The test set comprises all HarmBench [Mazeika et al., 2024] samples that successfully attack the victim model. As shown in Tab. 2, our method delivers the strongest 1 The distinction between skill-seen methods and skill-unseen methods lies in whether the skills distilled from these

methods were used during the training process of our co-evolution framework.

[p.9]

Table 2 | ASR@1 (%) of different defense methods under three types of attack methods. Lower
values indicate stronger robustness. The right panel further reports the performance degradation of
the defended victim models on general reasoning benchmarks, where smaller drops indicate better
utility preservation.
Skill-Unseen Method | Skill-Seen Method | Evolved Attacker | Reasoning Benchmarks
Defender
4B | 8B | 70B | 4B | 8B | 70B | 4B | 8B | 70B | 3B | 8B | 70B

[COUPÉ : tableau 2, lignes de huit défenses de comparaison ; gardée : TriPlay-RL, que le texte p.9 désigne comme la base de comparaison la plus forte]

TriPlay-RL [Tan et al., 2026] | 24.29 | 25.68 | 28.31 | 19.64 | 21.00 | 12.35 | 16.00 | 22.42 | 9.55 | -1.79 -3.18 | -1.47
Ours | 14.76 | 17.93 | 21.66 | 13.25 | 2.38 | 3.80 | 11.59 15.22 | 4.03 | -0.25 | -0.61 | 0.00
Ours+ | 4.27 | 12.35 | 19.93 | 13.43 | 1.40 | 4.04 | 9.48 14.10 | 3.96 | -0.25 | -0.61 | 0.00

defensive performance across almost all attack types and model scales. It reduces the average ASR from 19.92% under TriPlay-RL [Tan et al., 2026], the strongest baseline and a co-evolutionary method, to 11.62%, corresponding to a relative reduction of over 40%. Meanwhile, it better preserves general reasoning ability (-0.29 vs. -2.15). [RQ2-2] Can Our Defender Serve as a Zero-Shot LLM Guard? We investigate whether an Auxiliary Defense Model, trained only once, can be repurposed as a zero-shot LLM guard. Mainstream baselines such as Llama-Guard [Llama Team, 2024] and Qwen3Guard [Zhao et al., 2025] are evaluated under the Moderating User Prompt setting, rather than the Moderating Model Response setting. As shown in Tab. 3, our 3B model achieves a nearly 100% filtering success rate on attacksuccessful prompts, while using substantially fewer parameters and outperforming Llama-Guard and Qwen3Guard by 24.92% and 14.13%, respectively. Moreover, our method yields negligible false positives on benign inputs. [RQ2-3] Can Memory Expansion Enhance Safety Without Additional Training? Finally, we examine whether defense performance can be further improved by directly adding current adversarial prompts to the Verified Memory Bank, without any additional parameter updates. We denote this memory-expanded variant as Ours+. As shown in Tab. 2 and Tab. 3, this lightweight extension consistently improves performance across both modes. Notably, in Guard mode, our method achieves a 100% success rate against entirely unseen attack vectors on both 4B and 70B victim models.

[p.10]

Table 3 | Accuracy (%) of multiple LLM guard models on input prompt classification. Left:
adversarial data (correct if classified as harmful); right: general reasoning data (correct if classified
as safe). Higher values indicate better performance for all metrics.
Skill-Unseen Method | Skill-Seen Method | Evolved Attacker | Reasoning Data
LLM Guard
4B | 8B | 70B | 4B | 8B | 70B | 4B | 8B | 70B GSM8K MMLU
WildGuard-7B [Han et al., 2024] | 72.02 61.53 | 85.53 | 73.12 | 75.70 | 85.96 | 99.25 | 97.94 | 98.70 | 99.92 | 99.12
Llama-Guard-3-8B [Llama Team, 2024] | 47.51 34.67 | 65.13 | 94.28 | 95.42 | 95.79 | 87.25 | 74.85 | 77.34 | 100 | 100
Qwen3Guard-8B [Zhao et al., 2025] | 83.50 61.31 | 86.80 | 74.47 | 77.23 | 86.77 | 99.87 | 99.56 | 99.83 | 100 | 99.12
Ours (Guard)-3B | 98.89 98.14 | 99.47 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 99.47
Ours+ (Guard)-3B | 100 | 99.93 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 99.47

Table 4 | Impact of continued training with newly emerging skills on defensive performance.
Defensive efficacy is evaluated using ASR (%) (lower is better), where Held-out Attack Methods
denote source methods for skills introduced during continued training, and Skill-seen Methods denote
those from the initial training phase. For Reasoning Benchmarks, the reported value is the percentage
(%) decrease in accuracy.
Held-out Attack Methods | Skill-Seen Methods | Reasoning Benchmarks
Mode | Setting
4B | 8B | 70B | 4B | 8B | 70B | 4B | 8B | 70B
Initial | 6.20 | 3.56 | 12.54 | 13.25 | 2.38 | 3.80 | -0.25 | -0.61 | 0.00
Steer | Continued | 1.71 | 1.30 | 2.31 | 12.80 | 2.50 | 3.64 | -0.21 | -0.61 | 0.00
Continued+ | 1.19 | 0.70 | 1.73 | 12.65 | 1.65 | 3.27 | -0.21 | -0.61 | 0.00
Initial | 0.33 | 1.02 | 0.74 | 0 | 0 | 0 | -0.27 | -0.26 | -0.27
Guard Continued | 0.03 | 0.05 | 0.10 | 0 | 0 | 0 | -0.27 | -0.26 | -0.27
Continued+ | 0 | 0 | 0.04 | 0 | 0 | 0 | -0.27 | -0.26 | -0.27

As demonstrated in Tab. 2 and Tab. 3, while our model achieves competitive zero-shot defense against OOD attacks, we further investigate whether incorporating distilled skills from these novel threats can elevate the robustness ceiling. To this end, we treat attack methods from the held-out attack library as nascent OOD signals and conduct incremental training on the extracted skills to evaluate their potential defense gains. As shown in Table 4,in Steer mode, the ASR on Llama-3.1-70B is reduced by over 5× relative to the baseline, from 12.54% to 2.31%. Meanwhile, in Guard mode with memory update, our method achieves 100% defense success across both 4B and 8B models, with no performance degradation on previously defended attack methods or general reasoning benchmarks. These results demonstrate that our approach can continuously adapt to newly emerging attack strategies, facilitating a step toward lifelong defense.

[p.11]

[RQ5-1: Defense Policy]. We ablate a key component, memory retrieval, and observe its impact on activating intrinsic safety in Steer mode. Specifically, we restrict the model to generate the safety prefix solely from the current user prompt. As shown in Tab. 5, disabling memory increases the average ASR of adversarial prompts by approximately 2×, demonstrating the advantage of leveraging historical experience rather than generating prefixes from scratch.

[RQ5-2: Attack Policy]. We ablate three key factors: skill integration, the number of invoked skills, and the inclusion of the high-level attack schema. As shown in Tab. 5, removing skill integration confines optimization to a closed environment and substantially degrades performance, resulting in an average drop of 36.5% and a maximum drop of 51.5%. Interestingly, increasing the number of skills does not yield monotonic gains; using four skills instead produces the weakest performance on both the 4B and 70B models. Finally, removing the attack schema leads to a small but consistent reduction in effectiveness.

Table 5 | Ablation study of EvoSafety. The
reported metric is ASR@1 (%).
Setting | 4B | 8B | 70B
Defense Policy
w/o Memory Retrieval 20.56 | 7.88 | 9.87
Ours | 13.25 | 2.38 | 3.80
Attack Policy
w/o Skill Integration | 66.5 | 47.0 | 73.5
→ Single-Skill Attack | 96.5 | 97.5 | 98.0
→ Four-Skill Attack | 93.0 | 98.5 | 97.5
w/o High-level Schema 96.0 | 97.5 | 98.5
Ours | 98.0 | 98.5 | 100

[COUPÉ : p.10-11 section 4.4 (courbes de co-évolution), p.11 conclusion (reprend le résumé)]

[COUPÉ : p.11-28 références et annexe A.1 à A.3.1 (analyse du détournement de récompense, motivation théorique de la porte de similarité, construction de la bibliothèque de compétences d'attaque)]

[COUPÉ : p.29 annexe A.3.2 (mode garde : le défenseur classe selon les premiers mots du préfixe), annexe A.4, définitions du modèle de coût (équations 20 à 25)]

[p.31]

Equivalently, the saving on the defense side from avoiding victim model updates must outweigh the additional cost of auxiliary prefix generation during attack optimization. Using the linear proxy in Eq. 20, the defense stage saving is positive whenever

This condition is expected to hold in the regime targeted by EvoSafety, where the auxiliary defense model is substantially smaller than the victim model and produces shorter safety prefixes, i.e., 𝑃 𝐷 ≪ 𝑃𝑇 and 𝐿 𝐷 < 𝐿𝑌 . For example, with a 3B auxiliary defender and an 8B victim model, the proxy update cost of the auxiliary defender is substantially smaller than that of updating the victim model; the gap becomes even larger as the victim model scales, e.g., to 70B class models.

Specifically, the initial attack skill library is derived from GPTFuzzer Yu et al. [2023] and CodeAttack Ren et al. [2024a]. The held-out attack skill library includes methods with released implementations, such as DeepInception Li et al. [2023], ReNeLLM Ding et al. [2024], TAP Mehrotra et al. [2024], FlipAttack Liu et al. [2024b], PAP Zeng et al. [2024a], JailbreakingLLMs Chao et al. [2025], Logibreak-DEBF Peng et al. [2025], QueryAttack Zou et al. [2025], Response Attack Miao et al. [2025], and StructTransform Yoosuf et al. [2025], as well as methods without released code, including Jailbroken Wei et al. [2023], SCP Wu et al. [2025], and ICL Wei et al. [2026]. Together, this construction also demonstrates our method’s ability to extract reusable skills from heterogeneous attack papers.

To avoid train–test contamination, we rigorously filter the training set to remove not only exact duplicates of HarmBench Mazeika et al. [2024] test samples, but also highly similar instances that may overlap semantically with the evaluation data. Concretely, we encode each sample with Qwen3-Embedding-8B Zhang et al. [2025] and compute its maximum cosine similarity to the HarmBench Mazeika et al. [2024] set. Samples with similarity above 0.88 are removed. Table 6 reports the resulting sample counts for each dataset.

[COUPÉ : p.32-36 reste de l'annexe B (effectifs, données de raisonnement, données d'amorçage, invites des juges)]

[COUPÉ : p.37-47 annexe C.1 (latence d'inférence), C.2 (validité de la génération automatique de compétences : tableau 7), C.3 et annexe D études de cas]

[p.48]

E. Limitations While our approach demonstrates promising results, we acknowledge several limitations. First, our current evaluation primarily focuses on standalone Large Language Models (LLMs), rather than autonomous agents equipped with tool-use capabilities. Second, the proposed framework does not yet support multimodal inputs. This restricts its applicability in defending vision-enabled models, such as browser-use agents. We leave the extension of our framework to these more complex agentic settings for future work.
