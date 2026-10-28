# EXTRAIT — RvB: Automating AI System Hardening via Iterative Red-Blue Games

- Auteurs : Lige Huang, Zicheng Liu, Jie Zhang (contribution égale), Lewen Yan, Dongrui Liu, Jing Shao (auteure correspondante) ; Laboratoire d'intelligence artificielle de Shanghai, Institut d'ingénierie de l'information de l'Académie chinoise des sciences, Université Jiao-tong de Shanghai ; année : 2026 (v1 du 27 janvier 2026) ; identifiant : arXiv:2601.19726v1 (15 pages)
- Statut : préimpression arXiv cs.CR ; aucune mention de conférence ou de revue dans les pages lues ; le texte emploie le format d'un article d'une conférence de traitement du langage (sections « Limitations », « Ethics Statement »), sans l'indiquer.
- PDF source : `docs/sources/pdf/2601.19726v1.pdf` ; SHA-256 du PDF : `53a465a479fc1887e724b424a749910eb09251be49c966a5a639c65d890e7e44` (compagnon `.sha256` fourni avec le PDF, vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-9 (sans la bibliographie), 11-15 (annexes A à C et E)
- Nature : texte du PDF repris mot pour mot (`pdftotext -layout`, une colonne à la fois, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]`. Les figures sont des graphiques dont le texte est brouillé ou sans valeur : seules les légendes sont reprises ; les formules sont extraites en texte linéaire, parfois dans le désordre (se reporter à la page citée). Aucun chiffre retapé à la main (R7). Les notes entre crochets sont de la main de l'instance.
- Retiré pour sûreté (niveau méthode seulement) : p.12, annexe A.4 point 1, l'exemple d'entrée de journal d'attaque (fichier visé, ligne de code vulnérable, type d'injection et charge utile) ; il ne reste que la classe d'attaque (vulnérabilités logiques de services web, injection incluse, nommée p.4 et p.12) et le protocole. Retiré par économie de place : travaux voisins (section 2), une partie de la section 3 (formalisme bayésien, équations (2) et (3), puces de la section 3.3), déclaration d'éthique, annexe A.1, bibliographie, annexes A.4 (procédure détaillée), B.2 (procédure), D (figure 11, tableau de tentatives par tâche) et tableau 2 des prix.

---

[p.1]

Abstract The dual offensive and defensive utility of Large Language Models (LLMs) highlights a critical gap in AI security: the lack of unified frameworks for dynamic, iterative adversarial adaptation hardening. To bridge this gap, we propose the Red Team vs. Blue Team (RvB) framework, formulated as a training-free, sequential, imperfect-information game. In this process, the Red Team exposes vulnerabilities, driving the Blue Team to learning effective solutions without parameter updates. We validate our framework across two challenging domains: dynamic code hardening against CVEs and guardrail optimization against jailbreaks. Our empirical results show that this interaction compels the Blue Team to learn fundamental defensive principles, leading to robust remediations that are not merely overfitted to specific exploits. RvB achieves Defense Success Rates of 90% and 45% across the respective tasks while maintaining near 0% False Positive Rates, significantly surpassing baselines. This work establishes the iterative adversarial interaction framework as a practical paradigm that automates the continuous hardening of AI systems.

[COUPÉ : introduction (dualité offensive et défensive des grands modèles de langage ; flux disjoints de la recherche offensive et défensive), puis :]

To bridge this gap, we propose a novel Red Team vs. Blue Team (RvB) framework. In contrast to traditional reinforcement learning paradigms that are constrained by high sample complexity and necessitate expensive model fine-tuning, our framework is formulated as a training-free, sequential, imperfect-information game. As illustrated in Figure 1, we model security hardening as an iterative turn-based interaction. In each round, the Red Team (Attacker) interacts with the dynamic environment to execute multi-step exploits. Conversely, the Blue Team (Defender) uses attack logs as a basis but conducts autonomous interrogation, probing the system state to pinpoint the root cause and synthesize a fix. This information asymmetry forces the defender to transcend superficial log pattern matching; instead, it must employ inductive reasoning to infer the underlying vulnerability logic, thereby generating generalized patches that secure the system against potential variants.

[p.2]

[COUPÉ : légende de la figure 1, suite de l'introduction]

We validate the versatility and effectiveness of our RvB framework across two distinct and challenging domains:

• Cyber Security (Code Hardening): We deploy agents in a realistic network environment to autonomously identify and patch logic vulnerabilities (e.g., CVEs). The Red Team utilizes tool-use capabilities to penetrate the system, forcing the Blue Team to analyze execution logs and generate functional code patches that pass rigorous regression tests.

• Content Security (Guardrail Optimization): We simulate an adversarial dialogue between a Jailbreaker and a Guardrail. The Red Team iteratively optimizes prompt injection strategies, driving the Blue Team to dynamically refine its safety rules to block diverse jailbreak attempts effectively.

[COUPÉ : résultats annoncés (redite du résumé), section 2 travaux voisins]

[p.3]

3 The RvB Framework: A Formal Paradigm In this section, we formalize the Red Team vs. Blue Team (RvB) framework as a training-free, sequential, imperfect-information game. In contrast to traditional Multi-Agent Reinforcement Learning (MARL) which relies on internal policy updates, our paradigm leverages Externalized Memory (Figure 2). Although the agents remain computationally stateless and reset between rounds, the theoretical Bayesian belief updates are manifested through the persistent state transitions of the target system.

State as Externalized History. Let Mk denote the interaction log history up to round k. We define the Target System State Sk as a physical encoding of this history, i.e., Sk ∼ = Encode(Mk ). The transition Sk → Sk+1 represents the consolidation of historical interaction data into the environment.

[p.4]

[COUPÉ : suite du formalisme : équations (2) et (3) (utilité espérée subjective, mise à jour bayésienne de la croyance) ; texte de la figure 2 brouillé ; section 3.3 :]

3.3 Information-Theoretic Analysis We quantify capability enhancement as the reduction of epistemic uncertainty regarding the optimal

attack vector. Since the state transition provides information gain (assuming non-negative mutual information), the entropy of the agent’s belief monotonically decreases: H(bk+1 ) ≤ H(bk ). (4)

[COUPÉ : puces « Exploration » et « Exploitation »]

4 Experiment 4.1 The Attacker vs. Defender in Cyber Security Experiment Setting In this experiment, we selected 10 specific vulnerability, including CVE-2022-30887, within the Pharmacy Management System v1.0. We constructed a vulnerable PHP service environment by deploying the application’s source code within a Docker container. We employed CAI (Mayoral-Vilches et al., 2025) as

[p.5]

the red team agent within our red-blue teaming paradigm. Equipped with specialized interfaces such as Bash and the Model Context Protocol (MCP), this agent is capable of performing attack prediction against the network environment, dynamically probing the system, and generating comprehensive vulnerability reports. For the blue team agent, we selected the Mini-SWE-Agent (Yang et al., 2024b), which functions by probing the system status and utilizing Bash commands to directly modify the source code, thereby achieving the remediation of environmental vulnerabilities.

The optimization process terminates if any of the following stopping criteria are met: (i) the failure of both the Red and Blue teams to generate any new structured findings (null production); (ii) an execution failure within the batch remediation module; (iii) metric convergence, defined as the vulnerability count remaining unchanged for three consecutive epochs (Count_delay = 3); or (iv) reaching the maximum number of predefined epochs (max_epoch = 5). To facilitate quantitative evaluation, we archive all interaction artifacts from each epoch and trace the vulnerability reduction trajectory, denoted as (Ci−1 , Ci ). Metrics To rigorously validate the effectiveness of the RvB framework, we established a metric suite centered on defensive robustness. We measure the per-round Defense Success Rate (DSR) to

evaluate the Blue Team’s remediation capabilities and employ the Attack Success Count (ASC) as a quantitative proxy for Attack Complexity (AC). Crucially, to guarantee fidelity in automated remediation, we proposed a granular decomposition of DSR into True DSR (TDSR) and Fake DSR (FDSR). This distinction allows us to isolate effective semantic fixes from destructive patches that technically mitigate vulnerabilities only by inducing service outages or interface failures. The formal definitions and calculation logic for these metrics are detailed in Appendix A.3.

1) The RvB framework significantly enhances cybersecurity operational capabilities. As illustrated in Figure 4, the adversarial interaction effectively drives performance gains for both agents. We established a Baseline simulating a standard cooperative Multi-Agent System (MAS), where the Defense Success Rate (DSR) and Attack Success Count (ASC) are calculated as the cumulative union of results over the maximum epochs. Observations indicate that while the RvB framework’s initial DSR was lower than the baseline, it rapidly improved, surpassing the baseline at Iteration 3 (80%) and reaching 90% by Iteration 5. Concurrently, the Red Team demonstrated improved Attack Capability (AC) through state updates, identifying new vulnerabilities and increasing the ASC from 5 to 7. These results validate that the RvB paradigm effectively elevates the capabilities of

[p.6]

both offensive and defensive agents compared to a static cooperative baseline.

2) The RvB framework improves the safety and robustness of the multi-agent system. As shown in Figure 5, the system employing the RvB framework exhibits a substantially lower service drop rate. To quantify this, we defined three metrics: True DSR (TDSR), representing cases where the vulnerability is fixed and the service remains functional; Fake DSR (FDSR), where the attack check fails potentially due to service destruction (e.g., the Blue Team deleting critical files); and Service Disruption Rate (SDR), calculated as the difference between FDSR and TDSR. Remarkably, the RvB framework maintains an SDR of 0 throughout the process. In contrast, the cooperative baseline exhibits an SDR as high as 60%. Analysis of execution logs reveals that the Red Team’s directed adversarial reports provide precise, actionable contexts, preventing the Blue Team from making indiscriminate or destructive modifications to the codebase. This confirms that the adversarial feedback loop is crucial for ensuring valid, non-disruptive remediation.

4.2 The Jailbreaker vs. Guardrail in Content Security Experiment Setting To evaluate the RvB framework in a realistic security context, we designed

an experiment simulating an adversarial dialogue between a Jailbreaker (Red Team) and a Guardrail (Blue Team). We selected harmful prompts from the HarmBench benchmark (Mazeika et al., 2024) as the attack targets. The Red Team agent, built upon the Composition-of-Principles (CoP) framework (Xiong et al., 2025a), iteratively refines attack strategies to generate effective jailbreak prompts. The Blue Team agent is an adaptive guardrail system based on NeMo Guardrails (Rebedea et al., 2023), which can dynamically augment its rule set to defend against novel attacks.

[COUPÉ : suite du dispositif de l'expérience de gardes de contenu ; définitions des métriques (annexe C)]

[p.7]

Appendix C. [fin de la phrase de la p.6]

Figure 7: Defense Success Rate and Average Attack Time comparison. As iterations progress, DSR (bars, right y-axis) consistently rises, while AAT (line, left y-axis) also trends upward, indicating that the Blue Team’s guardrail is becoming progressively stronger and more difficult to bypass.

Results and Analysis By compiling the metrics across four adversarial rounds, we obtained the following key results:

1) The RvB framework drives continuous and significant security improvement. As depicted in Figure 7, the Blue Team’s Defense Success Rate (DSR) against the Red Team’s attacks shows a clear upward trend with each adversarial round, climbing from 0% in the initial rounds to 45% by the final iteration. This indicates that the guardrail’s ability to intercept novel attacks is continuously improving. Concurrently, the Average Attack Turns (AAT) required for a successful breach also steadily rise, ultimately reaching 11.09 turns in the final round—a more than 7-fold increase from the baseline of 1.50. This further confirms that the Red Team’s task is becoming progressively more difficult. The task-level analysis in Figure 11 (in Appendix) corroborates this, showing that the number of attempts required for successful attacks increases substantially in later rounds for most tasks.

2) The Blue Team learns generalizable rules without catastrophic forgetting. A crucial aspect of iterative learning is avoiding overfitting to the most recent attacks. Figure 8 illustrates the Cross-Round Defense Efficacy (CRDE), showing how guardrails from later rounds perform against attacks from earlier rounds. Each line represents the performance of a progressively updated guardrail (from Guard Round 1 to 4) tested against a fixed set of historical attacks (from Round 1, 2, 3, or 4). A clear upward trend is observable across all lines, demonstrating two key findings. Firstly, the guardrail’s ability to defend against new attacks im-

proves with each iteration. Secondly, and more importantly, its defense performance against older attack sets (e.g., the Guard Round 4’s performance on Round 1 attacks) does not degrade but consistently improves. This indicates our iterative augmentation mechanism successfully avoids catastrophic forgetting. Furthermore, as shown in Figure 9, the False Positive Rate (FPR) remains at a very low level, demonstrating that the enhanced security does not come at the cost of excessive over-interception.

3) The evolved guardrail demonstrates strong out-of-domain generalization. To verify that the learned defensive capabilities generalize beyond the specific attack patterns seen during interaction, we evaluated the initial and final guardrails on 100 randomly selected prompts from four external, unseen jailbreak benchmarks. As shown in Figure 10, the Final Guard consistently outperforms the Initial Guard across all external datasets (JailBreakBench (Chao et al., 2024), AdvBench (Zou et al., 2023), SorryBench (Xie et al., 2024), and XGuard-Train

[p.8]

(Upadhayay et al., 2025)), with its defense success rate improving from 96% to 99% on JailBreak-Bench and achieving a perfect 100% on AdvBench. This indicates that the adversarial iterations compelled the Blue Team to learn more fundamental and robust principles of defense, enhancing its resilience against a broader spectrum of unseen jailbreak attacks.

5 Discussion Our findings substantiate the efficacy of the RvB framework, offering improvements that stem directly from the game-theoretic structure rather than mere model scaling. We analyze the mechanisms driving these results below. Convergence to Practical Equilibrium. The adversarial interaction drives the system toward a practical equilibrium where defensive coverage matches the high-probability attack manifold. As the Red Team’s belief entropy (H(bk )) decreases, its strategy shifts from broad exploration to focused exploitation. The resulting convergence of high Defense Success Rates with escalating Attack Costs suggests that further exploitation becomes computationally prohibitive. While a formal Nash Equilibrium in the high-dimensional discrete space of natural language remains theoretically elusive, the monotonic state progression confirms that offensive and defensive utilities balance at a robust security standard.

[COUPÉ : fin de la discussion (« Interaction-Driven Generalization », « Operational Viability via Semantic Verification »), conclusion (section 6)]

Limitations The efficacy of the RvB framework relies intrinsically on the reasoning capabilities of the underlying foundation models. Regarding evaluation scope,

[p.9]

our current experiments utilized a representative but constrained set of web vulnerabilities. Rigorous testing against larger-scale, diverse benchmarks is required to further verify generalizability. We also note that the turn-based simulation serves as a controlled abstraction, effectively simplifying the asynchronous dynamics inherent in real-world security operations.

[COUPÉ : déclaration d'éthique, références]

[p.11]

[COUPÉ : annexe A, expérience de sécurité informatique : réglage de l'équipe rouge (A.1), puis :]

A.2 Blue Team Setting The blue team’s Mini-SWE-Agent is designed to simulate the remediation workflow of a security engineer. Its inputs are the vulnerability report generated by the red team and the project’s source code. The blue team’s workflow comprises three stages: fault localization, patch generation, and regression verification. First, the agent analyzes the codebase based on the vulnerability report to locate the vulnerable PHP files. Next, it generates a patch in git diff format and applies it to the environment. Finally, it restarts the Docker container to verify service availability and confirm the mitigation of the vulnerability. To ensure the accuracy of code modifications and prevent disruption of existing business logic, the blue team model requires a high level of code comprehension and generation capability; thus, we also selected gemini-3.0-flash as its underlying model. If the initial repair fails, the blue team is permitted a maximum of 3 retry attempts to correct the patch.

A.3 Metric Definitions for Cyber Security In the context of the Cyber Security (Code Hardening) task, let D = {x1 , x2 , . . . , xN } denote the set of vulnerability test cases. For each test case xi at a given interaction round, we define the outcome (i) (i) state as a tuple (ratt , rreg ), where: (i)

• ratt ∈ {0, 1} denotes the outcome of the Red (i) Team’s attack. ratt = 1 indicates a successful breach (exploit succeeded), while 0 indicates a failed attack (defense succeeded). (i)

• rreg ∈ {0, 1} denotes the outcome of the ser- (i) vice regression test. rreg = 1 indicates the service remains functional, while 0 indicates a service disruption (e.g., HTTP 500 error or missing interface).

Defensive Metrics: DSR, TDSR, and FDSR The Defense Success Rate (DSR) represents the overall ratio of cases where the Blue Team successfully fixes the system. True Defense Success Rate (TDSR): The proportion of cases where the vulnerability is mitigated and the service integrity is preserved.

N 1 X (i) (i) DSR = TDSR = I(ratt = 0 ∧ rreg = 1) N i=1 (5)

[p.12]

Fake Defense Success Rate (FDSR): The proportion of cases where the attack fails solely because the defensive patch rendered the service non-functional. N 1 X (i) FDSR = I(ratt = 0) (6) N i=1

N 1 X (i) (i) SDR = I(ratt = 0 ∧ rreg = 0) (7) N i=1

Service Disruption Rate (SDR): A measure of availability loss caused by defensive over-optimization. It denotes the frequency with which valid user requests are blocked or service interfaces become unresponsive as a direct result of the applied security patches.

From the equations above, it holds that SDR = FDSR − TDSR. A robust automated defense agent should maximize TDSR while maintaining SDR near zero.

Offensive Metric: Attack Success Count (ASC) We utilize Attack Success Count (ASC) to measure the diversity and complexity of the attack vectors discovered by the Red Team. Let Ek be the set of unique, valid exploit payloads successfully executed by the Red Team up to round k. The ASC is defined as the cardinality of this cumulative set:

[COUPÉ : équation (8) et procédure A.4 (le point 1, avec son exemple d'entrée de journal d'attaque, est retiré pour sûreté) ; annexe B, expérience de gardes de contenu :]

• Target Model (target_model): The model to be attacked, protected by the Blue Team’s guardrail. To better observe the iterative improvement of the guardrail, this model was selected to have relatively weak intrinsic safety features but adequate question-answering capabilities. We chose Qwen2-7B-Instruct.

• Helper Model (helper_model): Responsible for generating diverse attack strategies. This role requires high capability without being prone to refusal. We chose DeepSeek-V3.

[p.13]

• Attack Model (attack_model): Guided by the strategies from the helper model, this component generates the actual attack prompts.

• Judge Model (judge_model): Evaluates the success of an attack by checking if the target model’s response aligns with the harmful intent, while also monitoring for topic drift.

For the attack_model and judge_model, we required highly capable open-source models that could reliably follow complex instructions. We chose Qwen3-32B for both roles. Blue Team Components The Blue Team agent, based on NeMo Guardrails, consists of the following:

• Target Model (target_model): The same Qwen2-7B-Instruct used by the Red Team.

[COUPÉ : composants de l'équipe bleue (modèle de garde, modèle de rustines)]

Both the guard_model and patch_model require stable, high-quality reasoning and are less likely to trigger refusal mechanisms. Therefore, we leveraged a powerful closed-source model with strong safety alignments, selecting GPT-4o-mini for these roles. Validation Component To prevent the augmented rules from overfitting, a validation step is performed using negative samples. The generate_model for creating these benign samples needs to be capable yet avoid refusal. We chose DeepSeek-V3 for this role. For each positive (harmful) prompt, three corresponding negative (benign) samples were generated.

[COUPÉ : annexe B.2 (procédure) ; annexe C, définitions :]

• Defense Success Rate (DSR): Our primary metric, measuring the proportion of harmful samples in round i that are successfully intercepted by the guardrail from the previous state, Guardi−1 . It is the inverse of the Attack Success Rate (ASR), calculated as 1 − ASRi . 1 X DSRi = 1 − IsSuccess(pq,i , Gi−1 ) Ntotal q∈D harm (9) where IsSuccess(p, G) returns 1 if prompt p bypasses guardrail G.

• Average Attack Turns (AAT): The average number of inner attack attempts the Red Team requires for a successful jailbreak in round i. P q∈Si kq,i AATi = (10) |Si | where Si is the subset of successfully attacked samples and kq,i is the number of attempts for sample q.

[p.14]

• Cross-Round Defense Efficacy (CRDE): Formerly DSR, this metric measures the capability of the guardrail at iteration i to defend against the set of effective attacks from a previous or current iteration j (where j ≤ i). It tests for catastrophic forgetting.

• False Positive Rate (FPR): The proportion of harmless samples from Dbenign,j that are incorrectly blocked by Guardi . P pb ∈Dbenign,j IsBlocked(pb , Guardi ) FPRi,j = |Dbenign,j | (12) where IsBlocked(pb , G) returns 1 if the benign prompt pb is incorrectly intercepted.

[COUPÉ : annexe D (figure 11) ; annexe E, coût :]

Security Table 1 details the token usage across the same experimental settings(Max_epoch=5). The RvB framework consumes a total of 5,105,759 tokens, representing an 18.35% reduction in total computational cost compared to the Cooperative MAS (Pure Blue) baseline (6,253,192 tokens).

Table 1: Comparison of cumulative token consumption during the hardening process. The RvB framework significantly reduces input token overhead by leveraging targeted adversarial reports, which prevent redundant exploratory reasoning in the Blue Team.

Setting Input Output Total Pure Red 576,140 17,742 593,882 (Offense) Pure Blue 5,943,099 310,093 6,253,192 (Cooperative MAS) RvB (Ours) 4,800,430 305,329 5,105,759

[p.15]

Table 3: Comparison of token consumption and estimated costs per round for the content security experiment.

Round / Setting Total Tokens Estimated Cost ($)
Baseline 4,040,889 $1.42
RvB Round 1 2,828,789 $1.00
RvB Round 2 5,961,159 $2.10
RvB Round 3 10,490,319 $3.70
RvB Round 4 12,223,668 $4.31
