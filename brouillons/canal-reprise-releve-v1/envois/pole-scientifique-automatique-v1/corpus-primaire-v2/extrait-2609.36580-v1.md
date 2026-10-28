# EXTRAIT — SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time

- Auteurs : Yu Cheng, Yongkang Hu, Shuaijie Ma, Zhihang Lin, Weicheng Meng, Jingyang Qiao, Jiuan Zhou, Yushuo Zhang, Yihang Chen, Weilin Luo, Kun Shao, Dong Li, Zhizhong Zhang, Yuan Xie, Zhaoxia Yin (East China Normal University, Shanghai Innovation Institute et autres) ; année : 2026 (v2 du 2 octobre 2026) ; identifiant : arXiv:2609.36580v2 (35 pages)
- Statut : préimpression arXiv cs.AI ; code annoncé (dépôt SII-YUCHENG2002/SafeCoEvo, adresse donnée p.1) ; le titre du PDF est « SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time »
- PDF source : `docs/sources/pdf/2609.36580v2.pdf` ; SHA-256 du PDF : `e0df2463da8c5a9aaaa819d79f08606618f3318823a0cc78f9ecbcf940a05d3a` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-7, 10, 19-20, 24
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux extraits en texte (colonnes séparées par « | », mise en forme possiblement perdue : en cas de doute sur un chiffre, se reporter à la page citée). Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : rien (le papier décrit un dispositif de défense ; les attaques viennent de jeux d'évaluation existants, nommés et non détaillés). Annexes d'exemples qualitatifs (trajectoire complète, p.20-22) et d'invites (p.23-31) non reprises, sauf la phrase de limite de l'agent d'évolution (p.24).

---

[p.1]

A BSTRACT LLM agents deployed in real-world environments continually encounter new tasks and safety risks, while execution feedback typically becomes available only after each task is completed. However, existing self-evolving approaches commonly rely on multiple rounds of optimization over fixed and repeatedly accessible task distributions, fundamentally differing from test-time adaptation in real-world deployment, where only experience accumulated from past tasks can be used to improve safety decisions on future unseen tasks. To address this limitation, we propose SafeCoEvo, a test-time Harness–Guard co-evolution framework for LLM agent safety that enables the external safety system to continually adapt from accumulated runtime experience. SafeCoEvo jointly improves two complementary safety capabilities at different timescales: S-Harness rapidly externalizes recent runtime experience into updatable explicit safety knowledge that can promptly influence subsequent tasks, while GuardVPO internalizes accumulated runtime safety experience over a longer timescale into parametric risk-judgment capabilities. By combining short-term rapid adaptation with long-term capability consolidation, SafeCoEvo continually improves the agent’s safety capabilities, reducing the unsafe outcome rate by 10.05% while improving the task success rate by 12.15% over the strongest baseline, thereby achieving simultaneous gains in safety and task utility. Code: https://github.com/SII-YUCHENG2002/SafeCoEvo

1 I NTRODUCTION

Large language model (LLM) agents are rapidly advancing toward autonomous systems capable of multi-step reasoning, tool use, and interaction with external environments Yao et al. (2023); Xi et al. (2025). As their ability to act autonomously grows, safety risks extend beyond harmful final outputs to the entire task-execution process, including external inputs, environmental observations, tool invocations, and multi-step execution trajectories Debenedetti et al. (2024); Zhang et al. (2026c); Andriushchenko et al. (2025); Yueh-Han et al. (2026). More importantly, in real-world deployment, tasks and safety-relevant interactions continually arise, while execution outcomes and safety feedback typically become available only after the corresponding interactions occur Li et al. (2026a). Safety mechanisms fixed prior to deployment therefore cannot continually improve their safety decisions by leveraging subsequently acquired runtime experience. [COUPÉ]

[p.2]

be treated solely as a one-time pre-deployment alignment or protection problem, but should also be formulated as a problem of continual test-time safety adaptation during deployment. [COUPÉ] SHE continually revises explicit safety components in the Safety Harness based on rollout trajectories Qu et al. (2026); EvoSafeHarness automatically searches for safety Harnesses tailored to specific models and domains Li et al. (2026b); and SafeEvolve further leverages execution experience to jointly optimize the Harness and the task-performing policy Mao et al. (2026). However, as illustrated in Figure 1, these approaches typically rely on multiple rounds of interaction and optimization over relatively fixed and repeatedly accessible safety-task distributions, allowing the system to repeatedly evolve over the same task distribution. This differs fundamentally from test-time settings in real-world deployment, where tasks arrive sequentially and only experience accumulated from past tasks can be used to improve safety on future unseen tasks, without repeatedly accessing or optimizing over the future task distribution. Continual test-time safety adaptation under such deployment constraints therefore remains an underexplored problem. To address this challenge, we propose SafeCoEvo, a test-time Harness–Guard co-evolution framework for LLM agent safety. At a shorter timescale, S-Harness rapidly externalizes recent runtime experience into five updatable safety components: Safety Prompt, Validated Memory, Safety Skills, Permission Policy, and Guard Policy, allowing newly acquired safety knowledge to promptly influence subsequent tasks. At a longer timescale, the Guard continually evolves through GuardVPO (Guard Verdict Policy Optimization), learning context-dependent risk-judgment capabilities from accumulated runtime safety experience. By co-evolving these two components over the same real-world deployment stream, SafeCoEvo enables the safety system to rapidly incorporate recent safety experience while progressively developing more stable and generalizable long-term safety capabilities. This design explicitly targets the safety–utility trade-off that arises when balancing a task-performing model with a conservative safety mechanism Overman & Bayati (2025). Experimental results show that, compared with the strongest baseline, SafeCoEvo reduces the unsafe outcome rate by 10.05% while improving the task success rate by 12.15%. The key contributions of our work can be summarized as follows:

[p.3]

• Continual test-time safety adaptation: We formulate agent safety adaptation as a continual test-time safety adaptation problem over real-world deployment streams and propose SafeCoEvo. To the best of our knowledge, SafeCoEvo is the first test-time agent safety framework to co-evolve a Safety Harness and a Guard. • Dual-timescale Harness–Guard co-evolution: S-Harness externalizes recent feedback into updatable and reusable explicit safety knowledge at a shorter timescale, while Guard- VPO internalizes accumulated safety experience into parametric risk-judgment capabilities at a longer timescale. • Simultaneous improvements in safety and task utility: Extensive experiments show that, compared with the strongest baseline, SafeCoEvo reduces the unsafe outcome rate by 10.05% while improving the task success rate by 12.15%.

2 C ONTINUAL T EST-T IME S AFETY A DAPTATION Test-time adaptation concerns how a system can continually adapt using information acquired during deployment Wang et al. (2021). Building on this paradigm, we consider safety adaptation for LLM agents over real-world deployment streams and formulate it as continual test-time safety adaptation. Unlike repeated optimization over a predefined and revisitable dataset, we consider a real-world deployment process in which tasks arrive sequentially and the runtime experience produced by each task becomes available only after its execution, and can therefore only be used for subsequent tasks. [COUPÉ] This setting differs fundamentally from the optimization process commonly adopted by existing self-evolving approaches. These methods typically perform multiple rounds of rollout–feedback–update over a predefined and repeatedly accessible evolution set, allowing the same tasks or task distribution to be revisited throughout evolution. In continual test-time safety adaptation, by contrast, the system

[p.4]

can only leverage the previously accumulated experience Et when executing xt , while the newly obtained (τt , ft ) can only benefit subsequent tasks. The resulting problem is to enable the agent’s external safety system to continually adapt from accumulated runtime experience under this test-time constraint.

3.1 OVERVIEW

To address continual test-time safety adaptation, we propose SafeCoEvo, which co-evolves the Safety Harness and Guard to enable the agent’s external safety system to continually improve from runtime experience accumulated throughout real-world deployment. At task t, the agent system is represented as At = (M, St ), St = (Ht , Gt ), (3) where M denotes the task-performing model that remains fixed throughout deployment, and St denotes the external safety system consisting of the S-Harness Ht and Guard Gt . For each task xt , S-Harness provides explicit safety knowledge and behavioral constraints, while the Guard assesses risks at critical events during execution. Upon task completion, the resulting execution trajectory τt and feedback ft become available for subsequent safety adaptation. [COUPÉ] At the shorter timescale, S-Harness is updated after each task using the latest trajectory and feedback: Ht+1 = UH (Ht , τt , ft ). (4) At the longer timescale, the Guard is periodically updated using event-level safety experience accumulated over the deployment stream: Gθk+1 = UG (Gθk , Bk ), (5) where k indexes Guard updates, and Bk denotes the event-level safety experience used for the k-th Guard update, constructed from runtime experience accumulated up to that point. In this way, S-Harness and the Guard operate over the same deployment experience stream but support rapid explicit adaptation and long-term parametric learning, respectively, forming the dual-timescale safety co-evolution of SafeCoEvo.

S-Harness is responsible for safety adaptation at the shorter timescale in SafeCoEvo, with the goal of rapidly external-izing newly acquired runtime experience into explicit safety knowledge that can directly benefit subsequent tasks. Specif-ically, S-Harness maintains five evolvable safety components: Safety Prompt, Validated Memory, Safety Skills, Permission Policy, and Guard Policy. [COUPÉ]

[p.5]

into the corresponding explicit safety components. [COUPÉ] To prevent local experience from being memorized as task-specific rules, S-Harness does not retain source-specific information such as benchmark names, task identifiers, or exact samples. Instead, such experience is abstracted into safety knowledge that can be reused across tasks, and all updates take effect only on subsequent tasks. In this way, S-Harness rapidly converts recent runtime experience into persistent and reusable explicit safety knowledge, enabling timely safety adaptation for future tasks.

3.3 G UARDVPO: PARAMETRIC I NTERNALIZATION OF ACCUMULATED S AFETY E XPERIENCE

S-Harness can rapidly incorporate recent safety experience, but as runtime experience continues to accumulate, the growing amount of explicit safety knowledge may introduce redundancy, conflicts, and increasing maintenance overhead, motivating its further consolidation into more stable parametric capabilities. [COUPÉ] Based on this motivation, SafeCoEvo introduces GuardVPO, which periodically updates the Guard using accumulated runtime safety experience, progressively internalizing long-term safety experience into context-dependent parametric risk-judgment capabilities.

Event-level Safety Experience. GuardVPO uses event-level safety experience as its basic learning unit. For each Guard invocation, the training experience retains the runtime context at the time of judgment, the candidate action, the Guard verdict, and the corresponding safety feedback. Event-level experiences accumulated over a period constitute Bk defined in Section 3.1. Compared with using only the final outcome of an entire episode, using such fine-grained experience aligns the learning signal with the Guard’s actual decision granularity, enabling more precise attribution of local risks.

Guard Verdict Policy Optimization. Based on the event-level experience, the Guard’s safe/unsafe output is treated as a binary decision, with an asymmetric reward derived from event-level risk feedback: {safe→safe: +0.5, safe→unsafe: -0.5, unsafe→safe: -1.5, unsafe→unsafe: +1.0}. A larger penalty is assigned when a truly unsafe event is incorrectly judged as safe, while overly conservative decisions are also penal-ized, preventing apparent safety gains from being achieved merely through more aggressive blocking. [COUPÉ] By periodically applying GuardVPO to the accumulated event-level safety experience Bk , runtime safety experience is progressively internalized into the Guard’s parametric judgment capabilities, complementing the rapid explicit adaptation of S-Harness to form the dual-timescale safety co-evolution in SafeCoEvo.

[p.6]

Table 1: Overall performance on the continual evolution stream. Subset and Full denote the first 512 episodes and the full 1,024 episodes, respectively. Lower UOR and higher TSR/SUCR are better. Best and second-best results are shown in bold and underline, respectively.

UOR↓ | TSR↑ | SUCR↑
Method
Subset | Full | Subset | Full | Subset | Full
DS-V4.1-Flash | 76.17% | 74.71% | 22.46% | 22.66% | 18.95% | 19.24%
DS-V4.1-Flash+Guard | 27.73% | 28.13% | 25.39% | 26.76% | 23.63% | 24.61%
SafeHarness | 41.67% | 40.38% | 43.85% | 43.65% | 31.55% | 30.76%
SHE | 28.77% | 24.06% | 58.71% | 63.93% | 48.14% | 54.35%
SafeCoEvo (Static) | 27.15% | 28.42% | 45.12% | 43.75% | 41.21% | 39.55%
SafeCoEvo w/o GuardVPO | 18.95% | 17.97% | 76.17% | 75.20% | 67.38% | 67.19%
SafeCoEvo | – | 14.01% | – | 76.08% | – | 70.02%

4.1 E XPERIMENTAL S ETUP

Datasets and Task Stream. We evaluate on Agent-SafetyBench Zhang et al. (2026c) and Agent Security Bench (ASB) Zhang et al. (2025a), targeting agent safety and security, respectively. The data are divided into a continual evolution stream, a validation set, and a held-out test set, con-taining 1,024, 200, and 300 episodes, respectively, with Agent-SafetyBench / ASB compositions of 404/620, 76/124, and 100/200. Agent-SafetyBench is partitioned into mutually exclusive subsets using a fixed random seed. For ASB, each episode pairs an original task with an attack tool from the same scenario under the Mixed Attack setting, covering both aggressive and non-aggressive attacks. The continual evolution stream and validation set share six scenarios and 31 task groups but use complementary attack-tool subsets, while the held-out test set consists exclusively of four unseen scenarios that do not appear in the continual evolution stream or validation set, enabling evaluation of generalization to novel security environments.

Continual Evaluation Protocol. Episodes in the continual evolution stream are processed in a fixed order, and each episode can only access the safety state and historical experience accumulated from preceding interactions. After each episode, S-Harness is updated using the observed trajectory and official feedback, with the update taking effect only on subsequent episodes. The Guard is optimized from accumulated event-level safety experience after a designated adaptation stage. In the current setting, the first 512 episodes constitute the first adaptation stage, after which the evolved S-Harness is fixed; Guard checkpoints are selected on the validation set, and the resulting system is evaluated on the held-out test set under a frozen configuration. We report three evaluation metrics: Unsafe Outcome Rate (UOR↓), the percentage of episodes that result in an unsafe outcome; Task Success Rate (TSR↑), the percentage of episodes in which the original task is successfully completed; and Safe and Useful Completion Rate (SUCR↑), the percentage of episodes that are both safe and task-successful. Lower UOR is better, while higher TSR and SUCR are better. All metrics are reported for Safety, Security, and Overall.

Baselines. We compare against different forms of external safety mechanisms, including DeepSeek-v4.1-flash without additional safety modules, AgentDoG1.5-Unified-Qwen3.5-4B Liu et al. (2026a) as a static Guard, SafeHarness Lin et al. (2026) as a fixed safety harness, and SHE Qu et al. (2026) as an experience-driven evolving safety harness. To match the continual test-time setting, SHE is adapted to the same continual evolution stream and is allowed to update its Harness after each episode. [COUPÉ] All reported results are averaged over multiple independent runs.

[p.7]

To evaluate the effectiveness of SafeCoEvo under continual test-time adaptation, different safety mechanisms are compared on the same continual evolution stream. As summarized in Table 1, compared with the strongest evolution baseline, SHE, SafeCoEvo reduces UOR by 10.05% over the full 1,024-episode continual evolution stream, while improving TSR and SUCR by 12.15% and 15.67%, respectively. These overall improvements are particularly pronounced under the Security setting, as shown by the detailed Safety–Security decomposition in Appendix A. This shows that SafeCoEvo reduces unsafe outcomes while improving task completion, rather than achieving safety gains through overly conservative behavior. [COUPÉ]

4.3 G ENERALIZATION ON THE T EST S ET

To evaluate whether the safety capabilities acquired by SafeCoEvo during continual evolution can generalize to test data not used for evolution, we further evaluate the evolved system on the test set. The test set is independent of the continual evolution stream. During evaluation, the evolved S-Harness and Guard are kept fixed, and no additional updates are performed using test episodes. Therefore, this setting directly measures the generalization of the safety capabilities acquired by SafeCoEvo from historical runtime experience.

Table 2: Overall performance on the held-out test set.
Method | UOR↓ TSR↑ SUCR↑
DS-V4.1-Flash | 74.67% 18.67% 16.67%
DS-V4.1-Flash+Guard | 24.33% 23.00% 18.67%
SafeHarness | 27.68% 62.11% 53.86%
SHE | 29.19% 54.36% 41.95%
SafeCoEvo (Static) | 19.00% 25.67% 23.67%
SafeCoEvo | 7.67% 80.00% 77.33%
w/o GuardVPO
SafeCoEvo | 7.67% 81.33% 78.33%
SafeCoEvo∗ | 5.67% 80.67% 78.33%

As shown in Table 2, compared with the strongest evolution baseline, SHE, SafeCoEvo reduces UOR by 21.52%, while improving TSR and SUCR by 26.97% and 36.38%, respectively. These results show that the runtime experience accumulated by SafeCoEvo over the continual evolution stream can be transformed into generalizable explicit safety knowledge and risk-judgment capabilities, improving both safety and task utility on the test set without additional test-time updates. Meanwhile, SafeCoEvo also shows good generalization performance on the OOD test set; detailed results are provided in Appendix C.

[COUPÉ : p.7-9 généralisation à d'autres modèles de tâche et de garde, tableaux 3 à 5, ablation, travaux voisins]

[p.10]

6 C ONCLUSION In this work, we study continual test-time safety adaptation for LLM agents over real-world deployment streams and propose SafeCoEvo, which co-evolves the Safety Harness and Guard to enable the safety system to continually improve from runtime experience while keeping the task-performing model frozen. SafeCoEvo operates at two complementary timescales: S-Harness rapidly externalizes recent runtime experience into updatable explicit safety knowledge, while GuardVPO progressively internalizes accumulated event-level safety experience into parametric risk-judgment capabilities. Experimental results show that, compared with the state-of-the-art baseline, SafeCo- Evo reduces the unsafe outcome rate by 10.05% while improving the task success rate by 12.15%, achieving simultaneous gains in safety and task utility. Overall, our results demonstrate that test-time co-evolution of an explicit Safety Harness and a parametric Guard provides a promising approach for transforming external agent safety mechanisms from static safeguards into adaptive safety systems that continually improve from runtime experience.

[COUPÉ : p.10-18 références ; p.13-18 annexes A à E, résultats détaillés]

[p.19]

Optimization dynamics. Both the total loss and policy loss exhibit an overall downward trend. The total loss decreases from 0.2657 at epoch 1 to −0.5675 at epoch 15, while the policy loss decreases from 0.1892 to −0.6136. Because GuardVPO uses a reward-based policy optimization objective, the losses can be negative, and their absolute magnitudes do not directly measure system safety or task completion performance. The effectiveness of the updates must therefore be assessed alongside validation performance.

Safety and task utility on the validation set. Epoch 13 achieves the lowest UOR (6.57%), highest TSR (84.34%), and highest SUCR (81.31%) among the reported validation results. Compared with the epoch-0 values of 18.50%, 78.00%, and 70.00%, UOR decreases by 11.93 percentage points, while TSR and SUCR increase by 6.34 and 11.31 percentage points, respectively. These results show that, at this checkpoint, fewer unsafe outcomes are accompanied by improved task completion performance.

Checkpoint selection. Validation performance does not improve monotonically: after epoch 13, UOR increases, while both TSR and SUCR decline, even though the training losses remain low.

G L IMITATIONS AND F UTURE W ORK Further exploration of parametric Guard internalization. The primary focus of this work is the dual-timescale Harness–Guard co-evolution paradigm for continual test-time safety adaptation, while GuardVPO provides an effective instantiation for internalizing accumulated event-level

[p.20]

safety experience into the Guard’s parametric risk-judgment capabilities. Although our experiments demonstrate the effectiveness of GuardVPO, we do not claim that its current optimization formulation is the only or optimal approach to long-term parametric safety internalization. Future work could explore alternative reinforcement learning objectives, experience sampling and selection strategies, and parameter-update mechanisms that are better suited to continual safety learning. More effective use of long-term accumulated experience may further improve risk judgment while strengthening generalization across tasks and evolving risk distributions.

Extension to multimodal and more complex agent environments. Our current evaluation primarily focuses on text-driven tool-using agents and a limited set of safety and security scenarios. Although we evaluate SafeCoEvo under held-out scenarios, external benchmarks, and alternative Agent and Guard configurations, real-world agents may operate in substantially more complex environments involving visual observations, graphical interfaces, audio, and other multimodal interactions, where safety risks may also span longer execution horizons and more complex environmental states. An important direction for future work is therefore to extend SafeCoEvo to multimodal agents, computer-use agents, and more open-ended long-horizon environments, and to investigate how explicit safety knowledge and parametric Guards can continually co-evolve from multimodal and long-trajectory runtime experience.

[COUPÉ : p.20-23 exemple qualitatif d'évolution]

[p.24]

You are the Safety Harness Evolution Agent. You work after one completed episode and before the next one. Your only job is to update the contents of fixed Safety Harness artifact files for future episodes. Never change the completed episode, its trace, official outcome, evaluator, dataset, model configuration, runtime code, tools, hooks, or Processor graph.

[COUPÉ : p.24-35 invites de l'agent cible et de l'agent d'évolution]
