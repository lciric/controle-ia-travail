# TEXTE INTÉGRAL — arXiv:2601.19726v1

- Identifiant : arXiv:2601.19726v1
- Titre (tel qu'écrit dans le PDF) : RvB: Automating AI System Hardening via Iterative Red-Blue Games
- PDF source : `docs/sources/pdf/2601.19726v1.pdf` ; SHA-256 du PDF : `53a465a479fc1887e724b424a749910eb09251be49c966a5a639c65d890e7e44` (compagnon `.sha256` vérifié par `sha256sum -c` avant lecture)
- Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0), page par page, marqueur `[p.N]` au début de chaque page (N = numéro de page du PDF, à partir de 1)
- Nombre de pages : 15
- Caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : 446, les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée) ; pages : 5 (282), 6 (164)
- Nombre de caractères du texte extrait (marqueurs `[p.N]` compris, en-tête exclu) : 107004
- Mention : texte intégral, aucun retrait, contenu d'attaque verbatim possible — dépôt privé seulement (jamais dans la copie expurgée publique ; règle de sûreté modifiée par R-439).
- Provenance : tout chiffre repris ailleurs doit citer la page `[p.N]` et être relu sur le PDF empreinté (R7). La mise en page en colonnes, les formules et les tableaux peuvent être mal ordonnés dans l'extraction : se reporter au PDF.

---

[p.1]

                                             RvB: Automating AI System Hardening via Iterative Red-Blue Games
                                                                          Lige Huang1,2 *     Zicheng Liu1,3 * Jie Zhang1 *
                                                                            Lewen Yan1        Dongrui Liu1 Jing Shao1†
                                                                            1
                                                                              Shanghai Artificial Intelligence Laboratory
                                                            2
                                                                Institute of Information Engineering, Chinese Academy of Sciences
                                                                                   3
                                                                                     Shanghai Jiao Tong University

                                                                                  ryukosei@sjtu.edu.cn
                                                                     {huanglige, zhangjie1, shaojing}@pjlab.org.cn
                                                                    Abstract                 defensive adapters (Castro et al., 2025) to automate
                                                                                                        vulnerability patching and incident response, and
                                                 The dual offensive and defensive utility of
arXiv:2601.19726v1 [cs.CR] 27 Jan 2026




                                                                                                        function as dynamic guardrails to prevent harmful
                                                 Large Language Models (LLMs) highlights a
                                                 critical gap in AI security: the lack of unified       content generation (Zeng et al., 2024).
                                                 frameworks for dynamic, iterative adversarial             However, despite these parallel advancements,
                                                 adaptation hardening. To bridge this gap, we           offensive and defensive research streams remain
                                                 propose the Red Team vs. Blue Team (RvB)               largely disjoint (Zou et al., 2025). Defensive frame-
                                                 framework, formulated as a training-free, se-          works predominantly rely on static benchmarks
                                                 quential, imperfect-information game. In this          or post-hoc analysis, limiting their capacity to an-
                                                 process, the Red Team exposes vulnerabilities,         ticipate novel attack vectors (Chao et al., 2024).
                                                 driving the Blue Team to learning effective so-
                                                 lutions without parameter updates. We vali-
                                                                                                        Conversely, offensive agents often operate without
                                                 date our framework across two challenging do-          a responsive adversary, failing to assess the target’s
                                                 mains: dynamic code hardening against CVEs             resilience under worst-case adversarial scenarios.
                                                 and guardrail optimization against jailbreaks.         This isolation highlights a critical gap: the absence
                                                 Our empirical results show that this interaction       of a unified game-theoretic paradigm that forces
                                                 compels the Blue Team to learn fundamental             these systems to engage in a continuous cycle of
                                                 defensive principles, leading to robust reme-          iterative adversarial adaptation, thereby proactively
                                                 diations that are not merely overfitted to spe-
                                                                                                        discovering and mitigating unknown vulnerabilities
                                                 cific exploits. RvB achieves Defense Success
                                                 Rates of 90% and 45% across the respective             (Huynh et al., 2025).
                                                 tasks while maintaining near 0% False Posi-               To bridge this gap, we propose a novel Red
                                                 tive Rates, significantly surpassing baselines.        Team vs. Blue Team (RvB) framework. In
                                                 This work establishes the iterative adversarial        contrast to traditional reinforcement learning
                                                 interaction framework as a practical paradigm          paradigms that are constrained by high sample
                                                 that automates the continuous hardening of AI          complexity and necessitate expensive model fine-
                                                 systems.                                               tuning, our framework is formulated as a training-
                                         1       Introduction                                           free, sequential, imperfect-information game. As
                                                                                                        illustrated in Figure 1, we model security hardening
                                         The rapid proliferation of Large Language Models               as an iterative turn-based interaction. In each round,
                                         (LLMs) has introduced a fundamental duality to the             the Red Team (Attacker) interacts with the dynamic
                                         field of security (Li and Fung, 2025). On one hand,            environment to execute multi-step exploits. Con-
                                         LLMs serve as powerful offensive instruments, ex-              versely, the Blue Team (Defender) uses attack logs
                                         emplified by autonomous agents like Pentest-Agent              as a basis but conducts autonomous interrogation,
                                         (Shen et al., 2025) and collaborative frameworks               probing the system state to pinpoint the root cause
                                         like CAI (Mayoral-Vilches et al., 2025), which can             and synthesize a fix. This information asymme-
                                         independently execute complex exploits, as well                try forces the defender to transcend superficial log
                                         as orchestrate sophisticated jailbreaking attacks              pattern matching; instead, it must employ induc-
                                         (Mazeika et al., 2024). On the other hand, they                tive reasoning to infer the underlying vulnerability
                                         act as sophisticated defensive shields, enabling sys-          logic, thereby generating generalized patches that
                                         tems such as SWE-agent (Yang et al., 2024b) and                secure the system against potential variants.
                                             *    Equal contribution.                                      This paradigm shifts the focus from static bench-
                                             †
                                                  Corresponding author.                                 marking to dynamic adversarial hardening. By cap-

                                                                                                    1

[p.2]

 AC:43%   DSR:39%   AC:59%   DSR:64%         AC:92%   DSR:93%       Crucially, the system exhibits robust generaliza-
      Env                Env                      Envn.
                                       ...                          tion to unseen attacks. Furthermore, it maintains a
      1.                 2.
                                                                    computational cost comparable to cooperative base-
     State 1            State 2                  State N
                                                                    lines, even reducing token consumption by over
Figure 1: The Red vs. Blue (RvB) framework across                   18% in code remediation scenarios. Collectively,
successive states (S1 → SN ). The Attack Complex-                   these findings establish RvB as a practical, training-
ity (AC) represents the escalating sophistication and               free paradigm that automates the continuous hard-
specificity of exploits required to bypass the hardening            ening of AI systems.
environment as epistemic uncertainty decreases. The
Defense Success Rate (DSR) measures the Blue Team’s                 2     Related Work
growing efficacy in neutralizing vulnerabilities through
iterative fixes.                                                    2.1    Multi-Agent Systems (MAS)
                                                                    Multi-Agent Systems (MAS) have emerged as a
italizing on the in-context reasoning capabilities of               powerful paradigm for solving complex problems
foundation models within a persistent environment,                  that exceed the capabilities of a single agent, foster-
our framework establishes a virtuous cycle where                    ing emergent collective intelligence through inter-
the adversarial interplay directly translates into sys-             action, coordination, and collaboration (Dorri et al.,
tem robustness. Crucially, rather than permanently                  2018). With the advent of LLMs, a new wave of re-
enhancing the agents themselves, this process iter-                 search has focused on building LLM-based agents
atively adapts the security artifacts: the Red Team                 capable of sophisticated, knowledge-intensive be-
exposes latent, high-complexity vulnerability paths,                haviors. A prominent line of this work centers on
necessitating the Blue Team to construct more com-                  cooperative problem-solving, where agents with
prehensive and resilient defense protocols. This                    a shared goal employ diverse strategies, such as
ensures that the target system is hardened against                  decentralized coordination or collaborative reason-
not merely specific exploits, but broader classes of                ing (Tao et al., 2024; Wang et al., 2024; Ishibashi
emergent threats.                                                   and Nishimura, 2024; Yang et al., 2025c; Jha et al.,
   We validate the versatility and effectiveness of                 2025).
our RvB framework across two distinct and chal-                        However, the assumption of a fully trusted con-
lenging domains:                                                    text in these cooperative frameworks limits their ap-
                                                                    plicability in security-critical domains. To address
   • Cyber Security (Code Hardening): We de-                        this, another significant branch of MAS research ex-
     ploy agents in a realistic network environment                 plores adversarial interactions. Studies have de-
     to autonomously identify and patch logic vul-                  veloped agents capable of executing sophisticated
     nerabilities (e.g., CVEs). The Red Team uti-                   attacks, such as prompt injection, communication
     lizes tool-use capabilities to penetrate the sys-              attacks, or exploiting system weaknesses through
     tem, forcing the Blue Team to analyze execu-                   adversarial prompting (Lee and Tiwari, 2024; He
     tion logs and generate functional code patches                 et al., 2025; Arora et al., 2025). Concurrently, de-
     that pass rigorous regression tests.                           fensive frameworks have emerged, utilizing agents
                                                                    to defend against specific threats like jailbreaks or
   • Content Security (Guardrail Optimiza-
                                                                    backdoor attacks (Zeng et al., 2024; Fan and Li,
     tion): We simulate an adversarial dialogue be-
                                                                    2025). While this adversarial dynamic drives capa-
     tween a Jailbreaker and a Guardrail. The Red
                                                                    bility enhancement, many existing works are either
     Team iteratively optimizes prompt injection
                                                                    modeled as symmetric self-play or focus on spe-
     strategies, driving the Blue Team to dynam-
                                                                    cific, predefined attack-defense vectors. This often
     ically refine its safety rules to block diverse
                                                                    leaves a gap in addressing unknown threats and
     jailbreak attempts effectively.
                                                                    ensuring that the global objective remains a non-
  Our empirical results demonstrate that this it-                   zero-sum goal of system hardening, rather than a
erative adversarial adaptation significantly outper-                zero-sum win for either the attacker or the defender.
forms baselines. Across dynamic code hardening
and guardrail optimization tasks, RvB achieves De-                  2.2    AI Security
fense Success Rates of 90% and 45%, respectively,                   The application of LLMs to cybersecurity has in-
while maintaining near-zero False Positive Rates.                   troduced a fundamental duality between automated

                                                                2

[p.3]

vulnerability discovery and remediation. On the of-           more robust and aligned LLMs.
fensive side, research focuses on automating pene-
tration testing and fuzzing. Agents such as Pentest-          3     The RvB Framework: A Formal
GPT (Deng et al., 2024) and AutoPentest (Henke,                     Paradigm
2025) leverage LLMs to decompose complex at-
tack procedures, autonomously guiding standard                In this section, we formalize the Red Team vs.
security tools to exploit target systems. LLM-                Blue Team (RvB) framework as a training-free, se-
enhanced fuzzing frameworks, exemplified by Ti-               quential, imperfect-information game. In contrast
tanFuzz (Deng et al., 2023) and Fuzz4All (Xia                 to traditional Multi-Agent Reinforcement Learning
et al., 2024), utilize LLMs to synthesize edge-case           (MARL) which relies on internal policy updates,
inputs that trigger deep-logic vulnerabilities in soft-       our paradigm leverages Externalized Memory (Fig-
ware libraries. Conversely, defensive research has            ure 2). Although the agents remain computation-
pivoted toward Automated Program Repair (APR).                ally stateless and reset between rounds, the theoreti-
Systems such as InferFix(Jin et al., 2023) and Vul-           cal Bayesian belief updates are manifested through
Repair(de Fitero-Dominguez et al., 2024) employ               the persistent state transitions of the target system.
fine-tuned models to localize and patch security
                                                              3.1    Formal Model Setup
defects based on static analysis. More recently,
autonomous software engineering agents, such as               We define the game dynamics via the following
SWE-agent(Yang et al., 2024a), have demonstrated              tuple:
the capacity to resolve GitHub issues and apply
                                                              Sequential Interaction. The game proceeds in
functional patches in real-world repositories. How-
                                                              discrete rounds k = 1, 2, . . . , N , progressing from
ever, these offensive and defensive streams operate
                                                              an initial vulnerable state to a robust state. Let
largely in isolation: offensive agents lack a respon-
                                                              ΠR and ΠB denote the fixed meta-strategy spaces
sive patching mechanism, while defensive repair
                                                              (i.e., agent capabilities and toolsets) for the Red
tools typically rely on static benchmarks rather than
                                                              and Blue teams, respectively. In our training-free
dynamic, adversarial feedback.
                                                              setting, Π remains static, no gradient updates occur.
   Within AI Safety, the adversarial adaptation be-
tween offensive Red Team and defensive Blue                   State as Externalized History. Let Mk denote
Team agents has become a critical research area for           the interaction log history up to round k. We define
addressing jailbreak attacks. On the offensive side,          the Target System State Sk as a physical encoding
autonomous agents systematically discover model               of this history, i.e., Sk ∼
                                                                                        = Encode(Mk ). The tran-
vulnerabilities through diverse strategies. These             sition Sk → Sk+1 represents the consolidation of
include frameworks that compose human-defined                 historical interaction data into the environment.
principles (Xiong et al., 2025a), reframe harm-
ful queries as reasoning tasks for self-jailbreaking          Belief Distribution. Operating under partial ob-
(Ying et al., 2025), evolve a library of reusable             servability, the Red Team observes the state Sk but
attack strategies (Liu et al., 2025), or simulate             not the Blue Team’s specific defense logic πB . The
multi-turn human attacks via multi-agent collabo-             Red Team’s Belief Distribution(b) at the start of
ration (Rahman et al., 2025). In response, adaptive           round k is conditioned directly on the observable
Blue Team agents have emerged with a range of                 state:
defensive approaches. Some operate at the prompt
level by optimizing a universal defensive suffix                    bk (πB ) = P (πB | Mk ) ≡ P (πB | Sk ).      (1)
(Zhou et al., 2024; Xiong et al., 2025b). Others
function as external, training-free guardians, us-            3.2    Mechanism: Belief Update via
ing either dynamic, user-defined policies (Hoover                    Environmental Feedback
et al., 2025) or a retrieval-augmented database of            Capability enhancement is modeled not as parame-
known attacks (Yang et al., 2025a). A third ap-               ter tuning, but as the refinement of the belief distri-
proach re-trains models to incorporate an internal,           bution bk through the interaction loop.
step-by-step safety reasoning process (Zhu et al.,
2025; Yang et al., 2025b). This ongoing arms race             Decision Process (Subjective Expected Utility).
between increasingly sophisticated red and blue               At round k, the Red Team selects an action akR
agents is a primary driver of progress in building            to maximize utility based on the current belief bk .

                                                          3

[p.4]

        LLM           Tools                                                                              Tools      LLM

                                                          Target State n
                                                          (Robust System)


       Context                                                                                           Blue      Context
                       Red
                      Team                                                                              Team
                      Scope                                    .....                                    Scope


                                                ① Env     Target State 2         ③ Blue Act
                                                          (Hardened System)
                                             ② Red Log                           ② Red Log


                                                                       ④ State Update


                                     ① Env                                              ③ Blue Act
                                                         Target State 1
                                    ② Red Log             (Initial System)              ② Red Log




Figure 2: Overview of the RvB Framework. Modeled as a sequential, imperfect-information game, the process drives
system hardening (S1 → SN ) through iterative adversarial interactions. The environment acts as an externalized
memory, necessitating the iterative adversarial adaptation of agent strategies without requiring internal model
parameter updates.


The agent computes the Subjective Expected Utility                     attack vector. Since the state transition provides
(SEU):                                                                 information gain (assuming non-negative mutual in-
                                                                       formation), the entropy of the agent’s belief mono-
      akR = arg max EπB ∼bk [UR (ar , πB )],                (2)        tonically decreases:
                 ar ∈AR

where UR is the reward function. In early rounds                                              H(bk+1 ) ≤ H(bk ).             (4)
(S1 ), the high-entropy belief results in generalized
exploration.                                                           This inequality formalizes the system’s progres-
                                                                       sion:
Posterior Update via State Transition. The ex-
ecution logs LR generated by the Red Team trigger                            • Exploration (k = 1): Maximal entropy H1
a remediation step by the Blue Team, inducing a                                implies a uniform prior, leading to trial-and-
state transition to Sk+1 . This transition acts as the                         error attacks.
Evidence (Ek ). The agent updates its belief to the                          • Exploitation (k → N ): As the environ-
posterior bk+1 using Bayes’ Theorem.                                           ment accumulates defenses, the evidence E1:k
  bk+1 (πB ) = P (πB | Ek , Sk )                                               prunes the feasible strategy space. The belief
                                                                               bN becomes low-entropy (sharp), compelling
                    P (Ek | πB , Sk ) · bk (πB )
             =P                                       .                        the agent to execute highly specific, sophisti-
                                    ′              ′
                   π ′ ∈ΠB P (Ek | π , Sk ) · bk (π )                          cated exploits to bypass the accumulated con-
                                                     (3)                       straints.
The Stateless Implementation. Since the agent
is reset, this posterior calculation is realized by                    4      Experiment
the filtering mechanism of the environment. The
new state Sk+1 physically invalidates the subset of                    4.1     The Attacker vs. Defender in Cyber
strategies exploitable in Sk . Consequently, when                              Security
the Red Team observes Sk+1 , its effective search                      Experiment Setting In this experiment, we se-
space is mathematically equivalent to sampling                         lected 10 specific vulnerability, including CVE-
from the posterior bk+1 .                                              2022-30887, within the Pharmacy Management
                                                                       System v1.0. We constructed a vulnerable PHP ser-
3.3   Information-Theoretic Analysis                                   vice environment by deploying the application’s
We quantify capability enhancement as the reduc-                       source code within a Docker container. We em-
tion of epistemic uncertainty regarding the optimal                    ployed CAI (Mayoral-Vilches et al., 2025) as

                                                                  4

[p.5]

                                                                                                                                                                                                                                                        'HIHQVH�6XFFHVV�5DWH�'65����
                                                                                                                             ��                                                                                                                  ���
                                                                                                                                                                                                                                     �����




                                                                          $WWDFN�6XFFHVV�&RXQW����
               ① t+1 Env                                                                                                       �                                                              �����           �����                     ��
                              Target State t+1
                                                   ③ Fix Act
                                                                                                                                       �����                                               ����             ����         ����
               ② Attack Log                      ② Attack Log
                                                                                                                               �                        �����        �����                                                              ��
                                       ⑤ Vuln Check                                                                                     ����          ����          ����
                                       ④ State Update
  Attack                                                        Fix                                                            �                                                                                                                  ��
                  ① t Env                         ③ Fix Act
                               Target State t                                                                                  �                                                                                                                  ��
               ② Attack Log                     ② Attack Log


                                                                                                                               � %DVHOLQH          �                �                  �                   �               �
                                                                                                                                                                                                                                                   �
Figure 3: Overview of the iterative Red-Blue adversarial                                                                                                                         ,WHUDWLRQ
loop. At each state t, the Red Team probes the environ-                                                                                     $WWDFN�6XFFHVV�&RXQW                        'HIHQVH�6XFFHVV�5DWH
ment (1) to generate a vulnerability report (2). The Blue
Team utilizes this report to apply a patch (3), updating                       Figure 4: Performance trajectory of the Red and Blue
the system to state t + 1 (4). A final verification (5)                        agents across 5 iterations. The bar chart (left axis) repre-
confirms if the vulnerability is mitigated.                                    sents the cumulative count of successful exploits discov-
                                                                               ered by the Red Team, while the line graph (right axis)
                                                                               tracks the Blue Team’s Defense Success Rate (DSR).
the red team agent within our red-blue teaming                                 The convergence toward a high DSR alongside sustained
paradigm. Equipped with specialized interfaces                                 attack intensity validates the framework’s effectiveness
such as Bash and the Model Context Protocol                                    in automated security hardening.
(MCP), this agent is capable of performing attack
prediction against the network environment, dy-
                                                                               evaluate the Blue Team’s remediation capabilities
namically probing the system, and generating com-
                                                                               and employ the Attack Success Count (ASC) as
prehensive vulnerability reports. For the blue team
                                                                               a quantitative proxy for Attack Complexity (AC).
agent, we selected the Mini-SWE-Agent (Yang
                                                                               Crucially, to guarantee fidelity in automated re-
et al., 2024b), which functions by probing the sys-
                                                                               mediation, we proposed a granular decomposition
tem status and utilizing Bash commands to directly
                                                                               of DSR into True DSR (TDSR) and Fake DSR
modify the source code, thereby achieving the re-
                                                                               (FDSR). This distinction allows us to isolate effec-
mediation of environmental vulnerabilities.
                                                                               tive semantic fixes from destructive patches that
   The entire process is structured as a multi-round
                                                                               technically mitigate vulnerabilities only by induc-
game where the two teams drive the iterative adver-
                                                                               ing service outages or interface failures. The formal
sarial adaptation of offensive and defensive capa-
                                                                               definitions and calculation logic for these metrics
bilities. We established a closed-loop adversarial
                                                                               are detailed in Appendix A.3.
workflow to simulate the continuous evolution of
system security, as illustrated in Figure 3. A de-
                                                                              Results and Analysis Based on the experiments
tailed breakdown of the agent architectures, model
                                                                              described above, we obtained the following key
selections, and the step-by-step procedure is pro-
                                                                              results:
vided in Appendix A.
                                                                                 1) The RvB framework significantly enhances
   The optimization process terminates if any of
                                                                              cybersecurity operational capabilities. As illus-
the following stopping criteria are met: (i) the
                                                                              trated in Figure 4, the adversarial interaction ef-
failure of both the Red and Blue teams to gener-
                                                                              fectively drives performance gains for both agents.
ate any new structured findings (null production);
                                                                              We established a Baseline simulating a standard
(ii) an execution failure within the batch remedia-
                                                                              cooperative Multi-Agent System (MAS), where
tion module; (iii) metric convergence, defined as
                                                                              the Defense Success Rate (DSR) and Attack Suc-
the vulnerability count remaining unchanged for
                                                                              cess Count (ASC) are calculated as the cumulative
three consecutive epochs (Count_delay = 3); or
                                                                              union of results over the maximum epochs. Obser-
(iv) reaching the maximum number of predefined
                                                                              vations indicate that while the RvB framework’s
epochs (max_epoch = 5). To facilitate quantitative
                                                                              initial DSR was lower than the baseline, it rapidly
evaluation, we archive all interaction artifacts from
                                                                              improved, surpassing the baseline at Iteration 3
each epoch and trace the vulnerability reduction
                                                                              (80%) and reaching 90% by Iteration 5. Concur-
trajectory, denoted as (Ci−1 , Ci ).
                                                                              rently, the Red Team demonstrated improved At-
Metrics To rigorously validate the effectiveness                              tack Capability (AC) through state updates, identi-
of the RvB framework, we established a metric                                 fying new vulnerabilities and increasing the ASC
suite centered on defensive robustness. We mea-                               from 5 to 7. These results validate that the RvB
sure the per-round Defense Success Rate (DSR) to                              paradigm effectively elevates the capabilities of

                                                                      5

[p.6]

                 ���
                   ��                                                                                                                                  ① t+1 Env                         ③ Add Rule Set
                                                                                                                                                                        LLM w. guard t+1
                                                                                                                                                      ② Attack Prompt                      ② Attack Prompt
5DWH���


                   ��                                                                                                                                                          ⑤ Validity Check

                                                                                                                                                                                 ④ Guard Update
                                                                                                                                         Attack
                   ��                                                                                                                                                                                      Guard
                                                                                                                                                         ① t Env                          ③ Add Rule Set
                                                                                                                                                                         LLM w. guard t
                   ��                                                                                                                               ② Attack Prompt                     ② Attack Prompt



                     �
                           �                   �              �                        �                        �                  Figure 6: Overview of the iterative adversarial dialogue
                                                         ,WHUDWLRQ                                                             for guardrail optimization. The interaction cycle pro-
                            %DVHOLQH�)'65           5Y%�7'65                                                       ceeds as follows: (1) The Red Team probes the current
                            %DVHOLQH�7'65           %DVHOLQH�6HUYLFH�'LVUXSWLRQ�5DWH
                            5Y%�)'65                     5Y%�6HUYLFH�'LVUXSWLRQ�5DWH                 environment state; (2) it executes an adaptive attack
                                                                                                                                        prompt aimed at bypassing the guard; (3) The Blue
  Figure 5: Comparative analysis of defense robustness                                                                                  Team analyzes the successful exploit to synthesize a
  between the Baseline and RvB frameworks. The solid                                                                                    targeted rule set; (4) The guardrail undergoes a dynamic
  lines track the True Defense Success Rate (TDSR), rep-                                                                                update, transitioning the system to a more robust state
  resenting valid fixes, while the dashed lines indicate                                                                                t + 1; and (5) A validity check using benign queries is
  the Fake Defense Success Rate (FDSR). The purple                                                                                      performed to prevent over-interception and ensure the
  line highlights the significant Service Disruption Rate                                                                               preservation of model utility.
  (SDR) in the Baseline, caused by destructive patches. In
  contrast, the RvB framework (brown line) maintains a
  near-zero SDR, demonstrating that adversarial feedback                                                                                an experiment simulating an adversarial dialogue
  ensures high-quality remediation without compromising                                                                                 between a Jailbreaker (Red Team) and a Guardrail
  service availability.                                                                                                                 (Blue Team). We selected harmful prompts from
                                                                                                                                        the HarmBench benchmark (Mazeika et al., 2024)
                                                                                                                                        as the attack targets. The Red Team agent,
  both offensive and defensive agents compared to a                                                                                     built upon the Composition-of-Principles (CoP)
  static cooperative baseline.                                                                                                          framework (Xiong et al., 2025a), iteratively re-
     2) The RvB framework improves the safety                                                                                           fines attack strategies to generate effective jail-
  and robustness of the multi-agent system. As                                                                                          break prompts. The Blue Team agent is an adap-
  shown in Figure 5, the system employing the RvB                                                                                       tive guardrail system based on NeMo Guardrails
  framework exhibits a substantially lower service                                                                                      (Rebedea et al., 2023), which can dynamically aug-
  drop rate. To quantify this, we defined three met-                                                                                    ment its rule set to defend against novel attacks.
  rics: True DSR (TDSR), representing cases where                                                                                          The entire process is structured as a multi-round
  the vulnerability is fixed and the service remains                                                                                    game where the two teams drive the iterative ad-
  functional; Fake DSR (FDSR), where the attack                                                                                         versarial adaptation of offensive and defensive ca-
  check fails potentially due to service destruction                                                                                    pabilities, as illustrated in Figure 6. A detailed
  (e.g., the Blue Team deleting critical files); and Ser-                                                                               breakdown of the agent architectures, model selec-
  vice Disruption Rate (SDR), calculated as the differ-                                                                                 tions, and the step-by-step procedure is provided in
  ence between FDSR and TDSR. Remarkably, the                                                                                           Appendix B.
  RvB framework maintains an SDR of 0 throughout
  the process. In contrast, the cooperative baseline                                                                                    Metrics To quantitatively measure the dynam-
  exhibits an SDR as high as 60%. Analysis of ex-                                                                                       ics of this adversarial interplay, we designed a set
  ecution logs reveals that the Red Team’s directed                                                                                     of corresponding metrics. To maintain a consis-
  adversarial reports provide precise, actionable con-                                                                                  tent defensive perspective, our primary metrics fo-
  texts, preventing the Blue Team from making indis-                                                                                    cus on the Blue Team’s performance. We mea-
  criminate or destructive modifications to the code-                                                                                   sure the Defense Success Rate (DSR) against the
  base. This confirms that the adversarial feedback                                                                                     Red Team’s latest attacks in each round, and the
  loop is crucial for ensuring valid, non-disruptive                                                                                    Average Attack Turns (AAT) the Red Team re-
  remediation.                                                                                                                          quires for a successful breach. For a more granular
                                                                                                                                        analysis of learning capabilities, we introduce the
  4.2                     The Jailbreaker vs. Guardrail in Content                                                                      Cross-Round Defense Efficacy (CRDE) to test
                          Security                                                                                                      for catastrophic forgetting, and the False Positive
  Experiment Setting To evaluate the RvB frame-                                                                                         Rate (FPR) to assess over-interception. The for-
  work in a realistic security context, we designed                                                                                     mal definitions of these metrics are provided in

                                                                                                                                    6

[p.7]

                                                                                           60
                      12.5                                                                                                                                    100                                      94.7%       94.7%




                                                                                           Defense Success Rate (%)

                                                                                                                           Cross-Round Defense Efficacy (%)
                                                                                 11.09
Average Attack Time
                                                                                 45%       50                                                                        84.2%             84.2%
                      10.0                                                                                                                                     80
                                                                                           40
                       7.5                                                                                                                                                                             63.2%       66.7%
                                                                         5.67              30                                                                                                                      61.1%
                                                           4.89                                                                                                60
                       5.0                     4.44                      25%               20                                                                                                          44.4%
                       2.5                     10%         10%                                                                                                 40
                             1.50     1.10                                                 10
                             0%       0%
                       0.0 Baseline                                                        0                                                                                 Round 1
                                       1        2               3         4        5                                                                           20            Round 2                               13.3%
                                                    Iteration                                                                                                                Round 3   11.1%
                                Average Attack Time                 Defense Success Rate                                                                                     Round 4
                                                                                                                                                                0
                                                                                                                                                                       1                 2                 3           4
                                                                                                                                                                                             Guard Round
  Figure 7: Defense Success Rate and Average Attack
  Time comparison. As iterations progress, DSR (bars,                                                                         Figure 8: Cross-Round Defense Efficacy (CRDE) for
  right y-axis) consistently rises, while AAT (line, left y-                                                                  exp. 2. Each line shows that newer guardrails (e.g.,
  axis) also trends upward, indicating that the Blue Team’s                                                                   Round 4) perform better against attacks from all rounds,
  guardrail is becoming progressively stronger and more                                                                       including older ones (e.g., Round 1), indicating no catas-
  difficult to bypass.                                                                                                        trophic forgetting.

                                                                                                                                                              20.0
  Appendix C.                                                                                                                                                                                                  Round 1
                                                                                                                                                              17.5                                             Round 2
                                                                                                                          False Positive Rate (%)             15.0
                                                                                                                                                                                                               Round 3
                                                                                                                                                                                                               Round 4
  Results and Analysis By compiling the metrics
                                                                                                                                                              12.5
  across four adversarial rounds, we obtained the
                                                                                                                                                              10.0                                                   10%
                                                                                                                                                                                                                 8.77%
  following key results:
                                                                                                                                                               7.5                                     7.02%
     1) The RvB framework drives continuous and                                                                                                                      5.26%
                                                                                                                                                               5.0                     3.51%
  significant security improvement. As depicted in                                                                                                                                                     2.35%
                                                                                                                                                               2.5
  Figure 7, the Blue Team’s Defense Success Rate                                                                                                                                       0.00%           0.00%     0.00%
                                                                                                                                                               0.0
  (DSR) against the Red Team’s attacks shows a clear                                                                                                                   1                 2                 3       4
                                                                                                                                                                                             Guard Round
  upward trend with each adversarial round, climbing
  from 0% in the initial rounds to 45% by the final it-                                                                       Figure 9: False Positive Rate (FPR) for exp. 2. The FPR
  eration. This indicates that the guardrail’s ability to                                                                     remains consistently low across all rounds, indicating
  intercept novel attacks is continuously improving.                                                                          minimal over-interception of benign prompts.
  Concurrently, the Average Attack Turns (AAT) re-
  quired for a successful breach also steadily rise, ul-
  timately reaching 11.09 turns in the final round—a                                                                         proves with each iteration. Secondly, and more im-
  more than 7-fold increase from the baseline of 1.50.                                                                       portantly, its defense performance against older at-
  This further confirms that the Red Team’s task is                                                                          tack sets (e.g., the Guard Round 4’s performance on
  becoming progressively more difficult. The task-                                                                           Round 1 attacks) does not degrade but consistently
  level analysis in Figure 11 (in Appendix) corrob-                                                                          improves. This indicates our iterative augmentation
  orates this, showing that the number of attempts                                                                           mechanism successfully avoids catastrophic forget-
  required for successful attacks increases substan-                                                                         ting. Furthermore, as shown in Figure 9, the False
  tially in later rounds for most tasks.                                                                                     Positive Rate (FPR) remains at a very low level,
     2) The Blue Team learns generalizable rules                                                                             demonstrating that the enhanced security does not
  without catastrophic forgetting. A crucial aspect                                                                          come at the cost of excessive over-interception.
  of iterative learning is avoiding overfitting to the                                                                          3) The evolved guardrail demonstrates strong
  most recent attacks. Figure 8 illustrates the Cross-                                                                       out-of-domain generalization. To verify that the
  Round Defense Efficacy (CRDE), showing how                                                                                 learned defensive capabilities generalize beyond
  guardrails from later rounds perform against at-                                                                           the specific attack patterns seen during interaction,
  tacks from earlier rounds. Each line represents the                                                                        we evaluated the initial and final guardrails on 100
  performance of a progressively updated guardrail                                                                           randomly selected prompts from four external, un-
  (from Guard Round 1 to 4) tested against a fixed                                                                           seen jailbreak benchmarks. As shown in Figure 10,
  set of historical attacks (from Round 1, 2, 3, or                                                                          the Final Guard consistently outperforms the Initial
  4). A clear upward trend is observable across all                                                                          Guard across all external datasets (JailBreakBench
  lines, demonstrating two key findings. Firstly, the                                                                        (Chao et al., 2024), AdvBench (Zou et al., 2023),
  guardrail’s ability to defend against new attacks im-                                                                      SorryBench (Xie et al., 2024), and XGuard-Train

                                                                                                                      7

[p.8]

Defense Success Rate (%)                                               Initial Guard       probes for blind spots, functioning as a continuous
                                                                       Final Guard         regularizer. This pressure penalizes superficial pat-
                                              100%100%        100%           100%
                           100         99%                 99%            99%              tern matching, forcing the Blue Team to induce
                                                                                           abstract, invariant security principles—such as de-
                                 96%                                                       tecting malicious intent structures over specific key-
                           95                                                              words. The interaction effectively synthesizes a
                                                                                           curriculum of “hard negatives” from the tail of the
                                                                                           vulnerability distribution, driving generalization
                           90JailBreakBench   Advbench    Sorrybench   XGuard-Train        without explicit supervision.
                                                     Dataset
                                                                                           Operational Viability via Semantic Verification.
   Figure 10: Out-of-Domain performance comparison be-                                     Crucially, the adversarial pairing resolves the “de-
   tween the initial and final guardrail. The final guardrail
                                                                                           structive remediation” bottleneck often found in
   shows significantly improved defensive performance on
   four unseen external benchmarks.                                                        autonomous software engineering. The near-zero
                                                                                           Service Disruption Rate (SDR) confirms that the
                                                                                           Red Team serves as a stringent semantic verifier.
  (Upadhayay et al., 2025)), with its defense success                                      By coupling remediation with immediate, targeted
  rate improving from 96% to 99% on JailBreak-                                             exploitation, the framework imposes a check-and-
  Bench and achieving a perfect 100% on AdvBench.                                          balance dynamic absent in cooperative systems,
  This indicates that the adversarial iterations com-                                      ensuring that security hardening does not compro-
  pelled the Blue Team to learn more fundamental                                           mise system availability.
  and robust principles of defense, enhancing its re-
  silience against a broader spectrum of unseen jail-                                      6   Conclusion
  break attacks.                                                                           In this work, we present a unified Red Team vs.
                                                                                           Blue Team (RvB) framework that automates the
   5                        Discussion
                                                                                           continuous hardening of AI systems. By formaliz-
   Our findings substantiate the efficacy of the RvB                                       ing security operations as a sequential, imperfect-
   framework, offering improvements that stem di-                                          information game, we bridge the gap between of-
   rectly from the game-theoretic structure rather than                                    fensive discovery and defensive mitigation, en-
   mere model scaling. We analyze the mechanisms                                           abling a self-reinforcing loop of capability enhance-
   driving these results below.                                                            ment without model tuning.
                                                                                              Experiments on cyber and content security
  Convergence to Practical Equilibrium. The ad-                                            demonstrate that this paradigm shifts security au-
  versarial interaction drives the system toward a                                         tomation from static, post-hoc patching to itera-
  practical equilibrium where defensive coverage                                           tive adversarial adaptation. The framework not
  matches the high-probability attack manifold. As                                         only successfully repairs vulnerabilities with high
  the Red Team’s belief entropy (H(bk )) decreases,                                        precision and minimal service disruption, but also
  its strategy shifts from broad exploration to focused                                    produces defensive guardrails with strong out-of-
  exploitation. The resulting convergence of high De-                                      distribution generalization. These findings suggest
  fense Success Rates with escalating Attack Costs                                         that the most effective way to secure foundation
  suggests that further exploitation becomes compu-                                        models is to subject them to the adversarial pres-
  tationally prohibitive. While a formal Nash Equi-                                        sures they face in real-world scenarios, governed
  librium in the high-dimensional discrete space of                                        by a structured game-theoretic architecture.
  natural language remains theoretically elusive, the                                         Future work will explore the theoretical bounds
  monotonic state progression confirms that offensive                                      of this convergence in multi-modal environments
  and defensive utilities balance at a robust security                                     and investigate the application of this framework
  standard.                                                                                to more complex, long-horizon security tasks.
   Interaction-Driven Generalization. The strong
                                                                                           Limitations
   performance on out-of-domain attacks (Figure 10)
   indicates that robustness emerges from the adver-                                       The efficacy of the RvB framework relies intrinsi-
   sarial dynamic rather than latent model knowledge                                       cally on the reasoning capabilities of the underlying
   alone. In this zero-sum loop, the Red Team actively                                     foundation models. Regarding evaluation scope,

                                                                                       8

[p.9]

our current experiments utilized a representative           Sebastián R. Castro, Roberto Campbell, Nancy Lau, Oc-
but constrained set of web vulnerabilities. Rig-              tavio Villalobos, Jiaqi Duan, and Alvaro A. Cardenas.
                                                              2025. Large language models are autonomous cyber
orous testing against larger-scale, diverse bench-
                                                              defenders. In 2025 IEEE Conference on Artificial
marks is required to further verify generalizability.         Intelligence (CAI), page 1125–1132. IEEE.
We also note that the turn-based simulation serves
as a controlled abstraction, effectively simplifying        Patrick Chao, Edoardo Debenedetti, Alexander Robey,
the asynchronous dynamics inherent in real-world              Maksym Andriushchenko, Francesco Croce, Vikash
                                                              Sehwag, Edgar Dobriban, Nicolas Flammarion,
security operations.                                          George J. Pappas, Florian Tramer, Hamed Hassani,
                                                              and Eric Wong. 2024. Jailbreakbench: An open ro-
Ethics Statement                                              bustness benchmark for jailbreaking large language
                                                              models. Preprint, arXiv:2404.01318.
This work involves the development of automated
agents capable of executing software exploits and           David de Fitero-Dominguez, Eva Garcia-Lopez, Anto-
generating adversarial jailbreaks. We acknowledge             nio Garcia-Cabot, and Jose-Javier Martinez-Herraiz.
the dual-use nature of such technologies; while               2024. Enhanced automated code vulnerability repair
                                                              using large language models. Engineering Applica-
intended for system hardening, the offensive capa-            tions of Artificial Intelligence, 138:109291.
bilities of the Red Team agent could theoretically
be repurposed for malicious attacks. To mitigate            Gelei Deng, Yi Liu, Víctor Mayoral-Vilches, Peng Liu,
these risks, we strictly adhered to the following             Yuekang Li, Yuan Xu, Tianwei Zhang, Yang Liu,
                                                              Martin Pinzger, and Stefan Rass. 2024. Pentestgpt:
safety protocols:                                             An llm-empowered automatic penetration testing tool.
Controlled Environments. All cybersecurity ex-                Preprint, arXiv:2308.06782.
periments were conducted within isolated, network-          Yinlin Deng, Chunqiu Steven Xia, Haoran Peng,
gated Docker containers with no internet access               Chenyuan Yang, and Lingming Zhang. 2023. Large
beyond the local simulation loop. This ensures that           language models are zero-shot fuzzers: Fuzzing
the automated exploit generation cannot propagate             deep-learning libraries via large language models.
                                                              Preprint, arXiv:2212.14834.
to external systems or critical infrastructure.
                                                            Ali Dorri, Salil S Kanhere, and Raja Jurdak. 2018.
Defensive Focus. The primary objective of the
                                                              Multi-agent systems: A survey. Ieee Access,
RvB framework is to minimize the epistemic uncer-             6:28573–28593.
tainty of the defender (Blue Team). The offensive
agent functions solely as a diagnostic tool to drive        Falong Fan and Xi Li. 2025. Peerguard: Defending
this defensive adaptation. We do not release of-              multi-agent systems against backdoor attacks through
                                                              mutual reasoning. arXiv preprint arXiv:2505.11642.
fensive agent that function independently of the
hardening loop.                                             Pengfei He, Yuping Lin, Shen Dong, Han Xu, Yue Xing,
                                                              and Hui Liu. 2025. Red-teaming llm multi-agent
Responsible Disclosure and Data. For the con-                 systems via communication attacks. In Findings of
tent security tasks, we utilized public benchmarks            the Association for Computational Linguistics: ACL
(e.g., HarmBench) and strictly monitored the gen-             2025, pages 6726–6747.
erated outputs. No new private datasets of harm-
                                                            Julius Henke. 2025. Autopentest: Enhancing vulner-
ful content were distributed. Our code release in-             ability management with autonomous llm agents.
cludes safeguards to prevent the standalone deploy-            Preprint, arXiv:2505.10321.
ment of the Red Team agent for malicious probing.
We believe that documenting these automated red-            Monte Hoover, Vatsal Baherwani, Neel Jain, Khalid Sai-
                                                             fullah, Joseph Vincent, Chirag Jain, Melissa Kazemi
teaming dynamics is essential for the community              Rad, C. Bayan Bruss, Ashwinee Panda, and
to develop robust defenses against emerging au-              Tom Goldstein. 2025. Dynaguard: A dynamic
tonomous threats.                                            guardian model with user-defined policies. Preprint,
                                                             arXiv:2509.02563.

References                                                  Trung-Kiet Huynh, Duy-Minh Dao-Sy, Thanh-Bang
                                                              Cao, Phong-Hao Le, Hong-Dan Nguyen, Phu-Quy
Nirmit Arora, Sathvik Joel, Ishan Kavathekar, Ro-             Nguyen-Lam, Minh-Luan Nguyen-Vo, Hong-Phat
  han Gandhi, Yash Pandya, Tanuja Ganu, Aditya                Pham, Phu-Hoa Pham, Thien-Kim Than, and 1 others.
  Kanade, Akshay Nambi, and 1 others. 2025. Expos-            2025. Understanding llm agent behaviours via game
  ing weak links in multi-agent systems under adver-          theory: Strategy recognition, biases and multi-agent
  sarial prompting. arXiv preprint arXiv:2511.10949.          dynamics. arXiv preprint arXiv:2512.07462.


                                                        9

[p.10]

Yoichi Ishibashi and Yoshimasa Nishimura. 2024. Self-           Wei Tao, Yucheng Zhou, Yanlin Wang, Wenqiang
  organized agents: A llm multi-agent framework to-              Zhang, Hongyu Zhang, and Yu Cheng. 2024. Magis:
  ward ultra large-scale code generation and optimiza-           Llm-based multi-agent framework for github issue
  tion. arXiv preprint arXiv:2404.02183.                         resolution. Advances in Neural Information Process-
                                                                 ing Systems, 37:51963–51993.
Kunal Jha, Wilka Carvalho, Yancheng Liang, Si-
  mon S Du, Max Kleiman-Weiner, and Natasha                     Bibek Upadhayay, Vahid Behzadan, and Ph. D. 2025.
  Jaques. 2025. Cross-environment cooperation en-                 X-guard: Multilingual guard agent for content mod-
  ables zero-shot multi-agent coordination. arXiv                 eration. Preprint, arXiv:2504.08848.
  preprint arXiv:2504.12714.
                                                                Zhefan Wang, Yuanqing Yu, Wendi Zheng, Weizhi Ma,
Matthew Jin, Syed Shahriar, Michele Tufano, Xin                   and Min Zhang. 2024. Multi-agent collaboration
 Shi, Shuai Lu, Neel Sundaresan, and Alexey Svy-                  framework for recommender systems. arXiv preprint
 atkovskiy. 2023. Inferfix: End-to-end program repair             arXiv:2402.15235.
 with llms. Preprint, arXiv:2303.07263.
                                                                Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian,
Donghyun Lee and Mo Tiwari. 2024. Prompt infec-                   Michael Pradel, and Lingming Zhang. 2024.
  tion: Llm-to-llm prompt injection within multi-agent            Fuzz4all: Universal fuzzing with large language mod-
  systems. arXiv preprint arXiv:2410.07283.                       els. In Proceedings of the IEEE/ACM 46th Interna-
                                                                  tional Conference on Software Engineering, ICSE
Miles Q Li and Benjamin CM Fung. 2025. Security con-              ’24, page 1–13. ACM.
  cerns for large language models: A survey. Journal
  of Information Security and Applications, 95:104284.          Tinghao Xie, Xiangyu Qi, Yi Zeng, Yangsibo Huang,
                                                                  Udari Madhushani Sehwag, Kaixuan Huang, Luxi
Xu Liu, Yan Chen, Kan Ling, Yichi Zhu, Hengrun                    He, Boyi Wei, Dacheng Li, Ying Sheng, and 1 oth-
  Zhang, Guisheng Fan, and Huiqun Yu. 2025. An au-                ers. 2024. Sorry-bench: Systematically evaluating
  tomated framework for strategy discovery, retrieval,            large language model safety refusal. arXiv preprint
  and evolution in llm jailbreak attacks. arXiv preprint          arXiv:2406.14598.
  arXiv:2511.02356.
                                                                Chen Xiong, Pin-Yu Chen, and Tsung-Yi Ho. 2025a.
Víctor Mayoral-Vilches, Luis Javier Navarrete-Lozano,             Cop: Agentic red-teaming for large language mod-
  María Sanz-Gómez, Lidia Salas Espejo, Martiño                   els using composition of principles. arXiv preprint
  Crespo-Álvarez, Francisco Oca-Gonzalez, Francesco               arXiv:2506.00781.
  Balassone, Alfonso Glera-Picón, Unai Ayucar-
  Carbajo, Jon Ander Ruiz-Alcalde, Stefan Rass, Mar-            Chen Xiong, Xiangyu Qi, Pin-Yu Chen, and Tsung-Yi
  tin Pinzger, and Endika Gil-Uriarte. 2025. Cai: An              Ho. 2025b. Defensive prompt patch: A robust and
  open, bug bounty-ready cybersecurity ai. Preprint,              interpretable defense of llms against jailbreak attacks.
  arXiv:2504.06017.                                               Preprint, arXiv:2405.20099.
Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,                Guangyu Yang, Jinghong Chen, Jingbiao Mei, Weizhe
 Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel                  Lin, and Bill Byrne. 2025a. Retrieval-augmented
 Li, Steven Basart, Bo Li, and 1 others. 2024. Harm-              defense: Adaptive and controllable jailbreak pre-
 bench: A standardized evaluation framework for auto-             vention for large language models.      Preprint,
 mated red teaming and robust refusal. arXiv preprint             arXiv:2508.16406.
 arXiv:2402.04249.
                                                                John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian
Salman Rahman, Liwei Jiang, James Shiffer, Genglin                Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir
  Liu, Sheriff Issaka, Md Rizwan Parvez, Hamid                    Press. 2024a. Swe-agent: Agent-computer interfaces
  Palangi, Kai-Wei Chang, Yejin Choi, and Saadia                  enable automated software engineering. Preprint,
  Gabriel. 2025. X-teaming: Multi-turn jailbreaks and             arXiv:2405.15793.
  defenses with adaptive multi-agents. arXiv preprint
  arXiv:2504.13203.                                             John Yang, Carlos E Jimenez, Alexander Wettig, Kilian
                                                                  Lieret, Shunyu Yao, Karthik R Narasimhan, and Ofir
Traian Rebedea, Razvan Dinu, Makesh Narsimhan                     Press. 2024b. SWE-agent: Agent-computer inter-
  Sreedhar, Christopher Parisien, and Jonathan Cohen.             faces enable automated software engineering. In The
  2023. Nemo guardrails: A toolkit for controllable               Thirty-eighth Annual Conference on Neural Informa-
  and safe llm applications with programmable rails.              tion Processing Systems.
  In Proceedings of the 2023 conference on empiri-
  cal methods in natural language processing: system            Xianglin Yang, Gelei Deng, Jieming Shi, Tianwei
  demonstrations, pages 431–445.                                  Zhang, and Jin Song Dong. 2025b. Enhancing model
                                                                  defense against jailbreaks with proactive safety rea-
Xiangmin Shen, Lingzhi Wang, Zhenyuan Li, Yan Chen,               soning. Preprint, arXiv:2501.19180.
  Wencheng Zhao, Dawei Sun, Jiashui Wang, and
  Wei Ruan. 2025. Pentestagent: Incorporating llm               Yingxuan Yang, Huacan Chai, Shuai Shao, Yuanyi Song,
  agents to automated penetration testing. Preprint,              Siyuan Qi, Renting Rui, and Weinan Zhang. 2025c.
  arXiv:2411.05185.                                               Agentnet: Decentralized evolutionary coordination


                                                           10

[p.11]

    for llm-based multi-agent systems. arXiv preprint           A.2   Blue Team Setting
    arXiv:2504.00587.
                                                                The blue team’s Mini-SWE-Agent is designed to
Zonghao Ying, Deyue Zhang, Zonglei Jing, Yisong                 simulate the remediation workflow of a security
  Xiao, Quanchen Zou, Aishan Liu, Siyuan Liang,                 engineer. Its inputs are the vulnerability report gen-
  Xiangzheng Zhang, Xianglong Liu, and Dacheng                  erated by the red team and the project’s source code.
  Tao. 2025. Reasoning-augmented conversation for
  multi-turn jailbreak attacks on large language models.        The blue team’s workflow comprises three stages:
  arXiv preprint arXiv:2502.11054.                              fault localization, patch generation, and regression
                                                                verification. First, the agent analyzes the codebase
Yifan Zeng, Yiran Wu, Xiao Zhang, Huazheng Wang,                based on the vulnerability report to locate the vul-
  and Qingyun Wu. 2024. Autodefense: Multi-agent
  llm defense against jailbreak attacks. arXiv preprint         nerable PHP files. Next, it generates a patch in
  arXiv:2403.04783.                                             git diff format and applies it to the environment.
                                                                Finally, it restarts the Docker container to verify
Andy Zhou, Bo Li, and Haohan Wang. 2024. Ro-                    service availability and confirm the mitigation of
  bust prompt optimization for defending language
  models against jailbreaking attacks.   Preprint,              the vulnerability. To ensure the accuracy of code
  arXiv:2401.17263.                                             modifications and prevent disruption of existing
                                                                business logic, the blue team model requires a high
Junda Zhu, Lingyong Yan, Shuaiqiang Wang, Dawei                 level of code comprehension and generation capa-
  Yin, and Lei Sha. 2025. Reasoning-to-defend:
  Safety-aware reasoning can defend large lan-
                                                                bility; thus, we also selected gemini-3.0-flash
  guage models from jailbreaking.      Preprint,                as its underlying model. If the initial repair fails,
  arXiv:2502.12970.                                             the blue team is permitted a maximum of 3 retry
                                                                attempts to correct the patch.
Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak,
  Mateusz Dziemian, Nick Winter, Alexander Grattan,             A.3   Metric Definitions for Cyber Security
  Valent Nathanael, Ayla Croft, Xander Davies, and 1
  others. 2025. Security challenges in ai agent deploy-         In the context of the Cyber Security (Code Harden-
  ment: Insights from a large scale public competition.         ing) task, let D = {x1 , x2 , . . . , xN } denote the set
  arXiv preprint arXiv:2507.20526.
                                                                of vulnerability test cases. For each test case xi at
Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr,             a given interaction round, we define the outcome
  J Zico Kolter, and Matt Fredrikson. 2023. Univer-                                (i) (i)
                                                                state as a tuple (ratt , rreg ), where:
  sal and transferable adversarial attacks on aligned
  language models. arXiv preprint arXiv:2307.15043.                    (i)
                                                                   • ratt ∈ {0, 1} denotes the outcome of the Red
                                                                                       (i)
A     Experiment Details of The Attacker vs.                         Team’s attack. ratt = 1 indicates a successful
      Defender in Cyber Security                                     breach (exploit succeeded), while 0 indicates
                                                                     a failed attack (defense succeeded).
A.1    Red Team Setting
                                                                       (i)
The architecture of the red team agent (CAI) con-                  • rreg ∈ {0, 1} denotes the outcome of the ser-
                                                                                             (i)
sists of three core components: a Planner respon-                    vice regression test. rreg = 1 indicates the
sible for deducing attack paths, an Executor for                     service remains functional, while 0 indicates
executing specific Bash/MCP commands, and a Re-                      a service disruption (e.g., HTTP 500 error or
porter for summarizing attack outcomes. During                       missing interface).
the offensive process, the red team first performs
passive reconnaissance on the target environment.               Defensive Metrics: DSR, TDSR, and FDSR
The Planner generates attack hypotheses based on                The Defense Success Rate (DSR) represents the
system feedback, after which the Executor invokes               overall ratio of cases where the Blue Team success-
tools to conduct active probing and payload deliv-              fully fixes the system.
ery. Upon a successful exploit, the agent maintains             True Defense Success Rate (TDSR): The propor-
access and triggers the Reporter to generate a vul-             tion of cases where the vulnerability is mitigated
nerability report containing reproduction steps. For            and the service integrity is preserved.
this experiment, we selected gemini-3.0-flash                                             N
as the backbone model. The maximum number of                                         1 X (i)             (i)
                                                                 DSR = TDSR =              I(ratt = 0 ∧ rreg = 1)
interaction turns was set to 30 to ensure sufficient                                 N
                                                                                       i=1
probing depth.                                                                                                 (5)

                                                           11

[p.12]

Fake Defense Success Rate (FDSR): The pro-                           {
                                                                     "file": "php_action/removeOrder.php",
portion of cases where the attack fails solely be-                   "code":       "$orderId=    $_GET[’id’];\n
cause the defensive patch rendered the service non-                  if($orderId) { \n $sql = \"UPDATE orders
functional.                                                          SET order_status = 2 WHERE order_id =
                                                                     {$orderId}\"; ... }",
                          N                                          "bug": "SQL Injection via ’id’ parameter
                   1 X (i)                                           in GET request. The variable $orderId is
            FDSR =    I(ratt = 0)                (6)                 interpolated without sanitization.",
                   N
                         i=1                                         "payload": "id=1 OR 1=1"
                                                                     }
Service Disruption Rate (SDR): A measure
of availability loss caused by defensive over-                      This structured output details the exploit
optimization. It denotes the frequency with which                   methodology and reproduction steps, serving
valid user requests are blocked or service interfaces               as the ground truth for the subsequent fix.
become unresponsive as a direct result of the ap-
plied security patches.                                          2. Remediation (Blue Team): Acting on the
                                                                    information provided in the Attack Log, the
                   N
            1 X (i)          (i)
                                                                    Blue agent analyzes the codebase to localize
      SDR =    I(ratt = 0 ∧ rreg = 0)            (7)                the fault. It then synthesizes a code patch and
            N
                   i=1
                                                                    performs a Fix Act to repair the vulnerability.
  From the equations above, it holds that SDR =
                                                                 3. State Update & Verification: The generated
FDSR − TDSR. A robust automated defense agent
                                                                    patch is applied to the Docker container, tran-
should maximize TDSR while maintaining SDR
                                                                    sitioning the system to Target State t + 1. Fi-
near zero.
                                                                    nally, a Vuln Check is executed to verify the ef-
Offensive Metric: Attack Success Count (ASC)                        fectiveness of the fix and ensure no regression
We utilize Attack Success Count (ASC) to mea-                       errors were introduced. If the vulnerability
sure the diversity and complexity of the attack vec-                persists, the Blue agent is triggered to refine
tors discovered by the Red Team. Let Ek be the                      its patch in subsequent iterations.
set of unique, valid exploit payloads successfully
executed by the Red Team up to round k. The ASC              B     Experiment Details of The Jailbreaker
is defined as the cardinality of this cumulative set:              vs. Guardrail in Content Security
                                                             B.1     Agent Architecture and Model Selection
 ASCk = |Ek |
            k
                                                             The Red and Blue teams were designed with spe-
                                                             cialized components and models to fulfill their re-
            [
        =       {e | e ∈ Payloadst , IsSuccess(e)}
            t=1                                              spective roles in the adversarial framework.
                                                 (8)
                                                             Red Team Components The Red Team agent,
Higher ASC values indicate that the Red Team is              based on the Composition-of-Principles (CoP)
capable of evolving its strategy to uncover deeper           framework, includes four main LLM-driven com-
logic vulnerabilities as the environment hardens.            ponents:

A.4   Detailed Procedure                                          • Target Model (target_model): The model
                                                                    to be attacked, protected by the Blue Team’s
  1. Attack Generation (Red Team): The Red                          guardrail. To better observe the iterative im-
     agent initiates the cycle by interacting with                  provement of the guardrail, this model was se-
     the current environment (t Env). It performs                   lected to have relatively weak intrinsic safety
     reconnaissance and exploitation to identify se-                features but adequate question-answering ca-
     curity flaws. Upon successful compromise, it                   pabilities. We chose Qwen2-7B-Instruct.
     produces a structured Attack Log containing
     the vulnerable file path, the snippet of prob-               • Helper Model (helper_model): Responsible
     lematic code, and the root cause of the bug.                   for generating diverse attack strategies. This
     A representative log entry is formatted as fol-                role requires high capability without being
     lows:                                                          prone to refusal. We chose DeepSeek-V3.

                                                        12

[p.13]

   • Attack Model (attack_model): Guided by the                  2. The Blue Team receives the set of successful
     strategies from the helper model, this compo-                  jailbreak prompts (Ai ) from the Red Team.
     nent generates the actual attack prompts.                      It uses the patch_model to analyze these
                                                                    prompts, identify common patterns, and gen-
   • Judge Model (judge_model): Evaluates the                       erate a new, more generalized set of defensive
     success of an attack by checking if the tar-                   rules.
     get model’s response aligns with the harmful
     intent, while also monitoring for topic drift.              3. The Blue Team integrates these new rules
                                                                    into its existing rule set to form an updated
For the attack_model and judge_model, we re-                        guardrail, Guardi .
quired highly capable open-source models that
could reliably follow complex instructions. We                   4. To prevent overfitting and ensure the new rules
chose Qwen3-32B for both roles.                                     do not incorrectly block harmless queries, the
                                                                    Blue Team validates Guardi against a set of
Blue Team Components The Blue Team agent,
                                                                    benign prompts (Dbenign,i ).
based on NeMo Guardrails, consists of the follow-
ing:                                                             5. The process repeats, with the Red Team now
                                                                    facing the hardened guardrail Guardi in the
   • Target Model (target_model): The same
                                                                    next iteration (i + 1). A detailed flowchart of
     Qwen2-7B-Instruct used by the Red Team.
                                                                    this procedure is shown in Figure X.
   • Guard Model (guard_model): Used dur-
     ing the defense phase to classify incoming
                                                             C     Metric Definitions
     prompts based on the current rule set.                  Here we provide the formal definitions for the met-
                                                             rics used in our evaluation. Let Dharm be the set of
   • Patch Model (patch_model): Used to ana-
                                                             harmful test samples (Ntotal = |Dharm |). Let Aj
     lyze successful attack prompts and augment
                                                             be the set of effective attack prompts generated by
     the rule set with more general, robust rules.
                                                             the red team in iteration j. Let Dbenign,j be the set
Both the guard_model and patch_model require                 of benign (negative) samples for validation in iter-
stable, high-quality reasoning and are less likely to        ation j. Let Guardi be the blue team’s guardrail
trigger refusal mechanisms. Therefore, we lever-             system after iteration i.
aged a powerful closed-source model with strong
                                                                  • Defense Success Rate (DSR): Our primary
safety alignments, selecting GPT-4o-mini for these
                                                                    metric, measuring the proportion of harmful
roles.
                                                                    samples in round i that are successfully in-
Validation Component To prevent the aug-                            tercepted by the guardrail from the previous
mented rules from overfitting, a validation step                    state, Guardi−1 . It is the inverse of the Attack
is performed using negative samples. The gen-                       Success Rate (ASR), calculated as 1 − ASRi .
erate_model for creating these benign samples
                                                                                   1      X
needs to be capable yet avoid refusal. We chose                     DSRi = 1 −                    IsSuccess(pq,i , Gi−1 )
                                                                                 Ntotal q∈D
DeepSeek-V3 for this role. For each positive                                               harm
                                                                                                                       (9)
(harmful) prompt, three corresponding negative                      where IsSuccess(p, G) returns 1 if prompt p
(benign) samples were generated.                                    bypasses guardrail G.
B.2   Detailed Procedure
                                                                  • Average Attack Turns (AAT): The average
The adversarial interaction proceeds as follows:                    number of inner attack attempts the Red Team
                                                                    requires for a successful jailbreak in round i.
  1. The Red Team is given a set of harmful
     prompts (e.g., from HarmBench). For each
                                                                                          P
                                                                                             q∈Si kq,i
     prompt, it conducts up to 3 outer rounds of                                 AATi =                        (10)
                                                                                              |Si |
     strategy refinement, with up to 10 inner attack
     attempts per round, to generate a set of effec-                where Si is the subset of successfully attacked
     tive jailbreak prompts that bypass the Blue                    samples and kq,i is the number of attempts for
     Team’s current guardrail (Guardi−1 ).                          sample q.

                                                        13

[p.14]

          • Cross-Round Defense Efficacy (CRDE):                                           E     Cost Analysis
            Formerly DSR, this metric measures the capa-
                                                                                           To evaluate the operational viability of the RvB
            bility of the guardrail at iteration i to defend
                                                                                           framework, we conduct a comprehensive analysis
            against the set of effective attacks from a pre-
                                                                                           of computational costs in terms of token consump-
            vious or current iteration j (where j ≤ i). It
                                                                                           tion. Contrary to the intuition that iterative adver-
            tests for catastrophic forgetting.
                                                                                           sarial loops increase overhead, our results demon-
                               1 X                                                         strate that the RvB paradigm is more resource-
                 CRDEi,j =              (1 − IsSuccess(p, Gi )) (11)
                              |Aj | p∈A
                                        j
                                                                                           efficient than traditional cooperative Multi-Agent
                                                                                           Systems (MAS).

          • False Positive Rate (FPR): The proportion                                      E.1    The Attacker vs. Defender in Cyber
            of harmless samples from Dbenign,j that are                                           Security
            incorrectly blocked by Guardi .
                                                        Table 1 details the token usage across the same
                              P                         experimental settings(Max_epoch=5). The RvB
                  pb ∈Dbenign,j IsBlocked(pb , Guardi )
     FPRi,j =                                           framework consumes a total of 5,105,759 tokens,
                              |Dbenign,j |              representing an 18.35% reduction in total compu-
                                                  (12)
                                                        tational cost compared to the Cooperative MAS
     where IsBlocked(pb , G) returns 1 if the be-
                                                        (Pure Blue) baseline (6,253,192 tokens).
     nign prompt pb is incorrectly intercepted.
                                                           We attribute this efficiency to the precision of
                                                        adversarial feedback. In a cooperative MAS en-
D Additional Results and Figures                        vironment, the defender often performs broad, in-
This section provides supplementary figures ref- discriminate reasoning to identify vulnerabilities,
erenced in the main body. Figure 11 provides a          leading to high input token counts. Conversely, the
task-level breakdown of the attack difficulty across    Red Team in the RvB framework provides targeted,
the adversarial rounds.                                 structured attack logs that serve as precise action-
                                                        able contexts. This focused evidence prunes the
   1    1     1     12     2       5      4             Blue Team’s search space, which is mathematically
   2    4     1      5                                  equivalent to reducing the epistemic uncertainty
   3    1     1      2     3       1
                                               Failed   and entropy of the defense policy. Consequently,
   4    1     1      6     1      20      6
                                                        the Blue Team achieves higher remediation quality
   5    1     1     24     4
                                               30+      with fewer redundant reasoning cycles.
   6    2     1      1     1       1      5
           7      1       1       1         5    13   34
           8      2       1       5         2                21-30                         Table 1: Comparison of cumulative token consumption
                                                                    Attack Attempts




           9      1       2       5         5    6                                         during the hardening process. The RvB framework
Task ID




          10      1       1       1         18   10   2      16-20
                                                                                           significantly reduces input token overhead by leveraging
          11      1       1       5                                                        targeted adversarial reports, which prevent redundant
          12      5       1       1         1    2    7                                    exploratory reasoning in the Blue Team.
                                                             11-15
          13      2       1       6         1    9    39
          14      1       2       1         15                                              Setting                  Input    Output        Total
                                                             6-10
          15      1       1       2         2    2    11                                    Pure Red
          16      1       1       1         1    2    1                                                            576,140     17,742     593,882
                                                                                            (Offense)
          17      1       1       1         1    2           1-5                            Pure Blue
                                                                                                                 5,943,099    310,093   6,253,192
          18      1       1                 8    6                                          (Cooperative MAS)
          19      1       1       1         14   1    5                                     RvB (Ours)           4,800,430    305,329   5,105,759
               baseline   1       2         3    4    5
                                  Iteration
                                                                                           E.2 The Jailbreaker vs. Guardrail in Content
Figure 11: The Attack Time (number of attempts) of                                             Security
each task across all the adversarial rounds. A clear trend
of increasing attack difficulty (color shifting from yel-                                  In the content security experiment, we analyze the
low to red/darker) is visible for most tasks in later itera-                               computational cost to demonstrate the framework’s
tions, complementing the aggregate AAT trend shown                                         efficiency and accessibility. A key characteristic of
in Figure 7.                                                                               this setup is its primary reliance on high-capability
                                                                                           open-source models, allowing for local deployment.

                                                                                      14

[p.15]

To provide a tangible measure of the resources
consumed, we estimate the hypothetical cost of
each round using publicly available reference API
prices1 . The pricing for all models utilized in this
experiment is detailed in Table 2.

Table 2: Reference API pricing for models used in the
content security experiment. Prices are listed per million
(M) tokens.

   Model                    Input Prices    Output Prices
   DeepSeek-V3                   $0.2820           $1.1270
   Qwen3-32B                     $0.1410           $0.5640
   GPT-4o-mini                   $0.0970           $0.3870
   Qwen2-7B-Instruct             $0.0000           $0.0000


   Table 3 details the total token usage and the cor-
responding estimated costs for a static baseline and
each iterative round of the RvB process. The costs
are calculated by applying the reference prices from
Table 2 to the precise input and output token con-
sumption of each model involved in each stage.

Table 3: Comparison of token consumption and esti-
mated costs per round for the content security experi-
ment.

  Round / Setting       Total Tokens     Estimated Cost ($)
  Baseline                  4,040,889                  $1.42
  RvB Round 1              2,828,789                   $1.00
  RvB Round 2              5,961,159                   $2.10
  RvB Round 3             10,490,319                   $3.70
  RvB Round 4             12,223,668                   $4.31


   The results clearly indicate the economic viabil-
ity of our framework. Even the most computation-
ally intensive iteration, Round 4, has a hypothetical
cost of only $4.31. This demonstrates that, even
when benchmarked against commercial API rates,
the per-round overhead of our iterative adversarial
framework is well within an acceptable and modest
range for academic research and practical applica-
tion. This highlights the framework’s accessibility,
making advanced, co-evolutionary security harden-
ing a financially feasible endeavor.




   1
       Reference pricing data sourced from Third-party Platform


                                                                  15

