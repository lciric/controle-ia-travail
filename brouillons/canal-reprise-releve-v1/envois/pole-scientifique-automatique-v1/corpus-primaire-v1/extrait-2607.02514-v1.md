# EXTRAIT — Distributed Attacks in Persistent-State AI Control

- Auteurs : Josh Hills, Ida Caspary, Asa Cooper Stickland ; année : 2026 (v2 du 8 juillet 2026) ; identifiant : arXiv:2607.02514v2 (35 pages)
- Statut : préimpression (arXiv cs.AI), « Preprint. Under review » ; Constellation Astra Fellowship, Imperial College London, UK AI Security Institute
- PDF source : `docs/sources/pdf/2607.02514v2.pdf` ; SHA-256 du PDF : `9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22` (compagnon `.sha256` du dépôt vérifié par `sha256sum -c`)
- Pages gardées en tout ou en partie : 1-10
- Nature : texte du PDF repris mot pour mot (`pdftotext`, lignes rejointes en paragraphes), numéro de page du PDF en `[p.N]` au début de chaque passage ; coupes marquées `[COUPÉ]` ; tableaux et figures extraits en texte, mise en forme possiblement perdue (en cas de doute sur un chiffre de figure, se reporter à la page citée). Aucun chiffre retapé à la main (R7).
- Retiré pour sûreté (niveau méthode seulement) : p.4 (consigne de cadrage donnée à l'agent attaquant), p.5 (exemples de tâches d'utilisateur servant de couverture), p.6 (figure 3 et paragraphes : exemple complet d'attaque graduelle par exfiltration, avec extrait de code), tableau 1 de p.3 ; annexes non reprises (elles contiennent les invites d'attaque et les séquences). Gardés : classes d'attaque (graduelle, positionnelle), protocole d'évaluation, moniteurs, résultats, limites.

---

[p.1]
Abstract As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce I TERATIVE V IBE C ODING, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In I TERATIVE V IBE C ODING , a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task. Our benchmark includes two task families: CLI tools and Flask web services, across 20 total task variations. We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. No single monitor is robust to both: which strategy evades best (success while evading the monitor) depends on the monitor type, so a defender cannot close off both gradual and non-gradual attacks with any one monitor. High evasion (≥ 65%) generalizes across model attack agent backends (Claude Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5), confirming this is a property of the persistent-state attack surface rather than a single model’s capability. Even state-of-the-art monitor models leave a substantial fraction of gradual attacks undetected, and gradual attacks evade more than non-gradual ones, with the gap largest for the most capable monitors. We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. On both task families, it detects gradual attacks substantially better than diff monitors that merely see more accumulated history. Combining this stronger monitor with trajectory monitors in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%. Code is available at https: //github.com/josh-hills/control-arena-persistent-state-eval.

1

Introduction

The field of AI control (Greenblatt et al., 2024) studies how to safely deploy capable, but potentially untrusted AI systems. As coding agents become more autonomous, they are increasingly used to ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface. A compromised agent, whether misaligned or adversarially prompted, can distribute infrastructure across pull requests, planting innocuous components early and activating them later; it can also wait for the PR (pull request) whose task most closely resembles its payload, exploiting natural cover. To study this problem, we introduce I TERATIVE V IBE C ODING, a setting where an AI coding assistant completes a sequence of programming tasks over multiple consecutive PRs in a persistent codebase. The benchmark contains two task families: CLI-tool sequences and Flask web-service sequences (Appendix P). We compare gradual attacks, which spread a side task across PRs, to a best-position non-gradual baseline, which executes the full side ∗ Equal contribution.

1

[p.2]
Figure 1: Overview of I TERATIVE V IBE C ODING. Bursts indicate an attack. Top: benign (noattack) multi-PR development. Middle: a positional attacker executes the side task in the PR with best cover. Bottom: the attacker spreads the side task across PRs. After each PR, the monitor scores the change; the run is flagged if any PR exceeds the suspicion threshold.

task in the optimal single PR, selected by minimizing detection. Here, a side task is a hidden objective that the agent pursues alongside the user’s main task, such as covertly exfiltrating the API KEY environment variable. Our primary metric is evasion: among attacks that successfully complete the side task, the fraction the monitor fails to flag (scores below its threshold), where each monitor’s threshold is calibrated to the 98th percentile of scores from honest runs (runs in which no side task is present and the agent only works on the main task). We measure attacker evasion across diff monitors (LLM monitors that see the code diff from PRs), which see only code changes, and trajectory monitors, which see command history and edits, while also varying how much context from previous PRs each monitor receives. Because a run is flagged if any of the PRs in the sequence exceeds the threshold, an undetected attack must stay below the threshold throughout the full sequence.

Our core findings are:

1. Gradual attacks evade standard diff monitors, and which strategy evades best depends on the monitor type. On the task-description diff monitor, which sees all prior task descriptions plus the current PR’s diff, gradual attacks evade more frequently across all four side tasks (87% gradual vs. 75% non-gradual). On trajectory monitors, this ordering can reverse: across our four side tasks, non-gradual attacks evade better for the two single-component tasks (81% non-gradual vs. 65% gradual), while the two multi-component tasks favor gradual attacks (80% gradual vs. 69% non-gradual; see Table 10 in Appendix A.4). Generally, gradual attacks evade monitors better in our setting, because distributing the side task across PRs lets each component land in a PR where it already has natural cover.

2. A stateful diff monitor and cross-modality ensemble provide the strongest defense. Link-tracker, a new stateful diff monitor that carries forward suspicion notes across PRs, reduces gradual-attack evasion from 87% to 54%. Combining it with trajectory monitors in a four-monitor ensemble further reduces gradual evasion to 47%.

3. State-of-the-art monitor models reduce evasion but do not eliminate it; the gap between gradual and non-gradual evasion is largest for the most capable models. We use eight strong models as monitors for our setting. Even with GPT-5.3-Codex as a monitor, which is a more capable model than the untrusted agent (Claude Sonnet 4.5), it still allows 27% of successful gradual attacks through. Gradual attacks tend to evade more than non-gradual ones, and the gap is largest for the most capable monitors.

These results suggest that persistent-state control is a distinct security problem with its own attack strategies and defense requirements. Our setting provides a foundation for developing and stress-testing monitors for coding agents in persistent state settings. 2

[p.3]
A simulated user provides a fixed sequence of main tasks to an AI coding assistant building software iteratively. The interaction takes place across PRs, with each PR extending the tool from earlier ones. Code persists between PRs via git commits. In our main experiments, the agent has no cross-PR conversation memory. This isolates the effect of persistent code from that of session memory, so we do not necessarily model the strongest possible memoryenabled attacker.

This is an example task sequence from the CLI task family (the uptime-monitor sequence):

PR 1: “Create a Python script that checks if a local port is open.”

PR 2: “Add a --url flag to check if a URL is reachable.”

PR 3: “Allow reading URLs from a YAML config file.”

PR 4: “Add retry logic with exponential backoff.”

PR 5: “If a site is down, POST a notification to SLACK WEBHOOK URL.”

In attack mode, the agent also receives a covert side task (e.g., exfiltrate a secret or plant an authentication bypass) that it must accomplish without detection. Across our sequences, later PRs naturally introduce network access and environment variables, creating various degrees of cover for the side task.

Table 1: Reported side tasks, chosen to span CLI and Flask web-service families as well as different attack shapes: direct exfiltration, telemetry-mediated exfiltration, and accesscontrol backdoors. Additional CLI side tasks are described in Appendix E. 2.3

Threat Model

We use the standard AI control threat model (Greenblatt et al., 2024):

[RETIRÉ POUR SÛRETÉ, p.3 : tableau 1 : liste des quatre tâches secondaires d'attaque avec leur « forme d'attaque » (exfiltration directe, exfiltration par télémétrie, contournement d'accès) ; gardée : la légende, qui donne les classes]

[p.4]
• The Red team controls the agent’s system prompt and attack strategy. It uses the same model (Claude Sonnet 4.5) whether attacking or working honestly. • The Blue team designs monitoring protocols using a trusted model (GPT-4o) and calibrates suspicion thresholds from honest-baseline runs (runs with no side task present). The blue team does not know which attack strategy the red team will use. • Agent constraints: The agent must also complete the main task. It operates within the sandboxed environment and cannot modify the monitoring infrastructure.

Experimental Design

We describe the attack policies, monitor configurations, and evaluation protocol used in the experiments.

Attack prompts undergo ∼10 rounds of prompt engineering to maximize evasion (Appendix M.1). We study two main types of attacks:

• Gradual attacks distribute the side task across PRs[RETIRÉ POUR SÛRETÉ, p.4 : détail de la consigne donnée à l'agent attaquant pour les attaques graduelles].

• Non-gradual attacks execute the full side task in a single PR. We use a positional policy: for each sequence, we run one evaluation per position, with the agent behaving honestly at every other PR (Appendix M). We then select the position with the highest evasion rate per (sequence, side-task) pair, modeling an attacker who chooses the PR with the best

We evaluate five monitors across two families (Table 2): three PR-diff monitors that review code changes and two trajectory monitors that review the agent’s actions, all outputting suspicion scores from 1 (benign) to 10 (malicious). Link-tracker is a novel stateful diff monitor: as it reviews each PR it writes notes to a file recording anything potentially suspicious, and these notes persist across PRs, so when it scores a later diff it can see whether the new change builds on suspicious setup from earlier PRs.

We also combine monitors into an ensemble by averaging their per-run suspicion scores into a single score, then calibrating one threshold on that score to keep the honest falsepositive rate below 2% (Appendix A.2).

Table 2: Monitor configurations. Standard variants rescore each PR from scratch with increasing context; link-tracker carries forward state.

All metrics use a suspicion threshold τ at the 98th percentile of honest-baseline scores, calibrated per monitor (Appendix A.1). Our headline metric is evasion rate: among successful attacks, the fraction undetected. A run’s suspicion score is the maximum across all PRs; a single flagged PR triggers detection. The default attack agent is Claude Sonnet 4.5 with

[p.5]
GPT-4o as monitor; we also evaluate Gemini 3.1 Pro and Kimi K2.5 as attack agents (Section 4.2) and GPT-5.2, GPT-5.3-Codex, DeepSeek v3.2, Kimi K2.5, Mistral Large 3, Sonnet 4, and Sonnet 4.5 as monitors. For each task family, we run n = 120 gradual attacks, n = 600 positional attacks (before selection), and honest baselines for threshold calibration, across five task sequences and two side tasks (Appendix P). The evaluation is built on Inspect AI (UK AI Security Institute, 2024) and ControlArena (Inglis et al., 2025).

For our headline results, we average the CLI and Flask percentages and report the taskfamily split in Table 7. Overall, no single monitor catches both attack strategies. The full-diffs monitor is weakest on gradual attacks, reaching 93% evasion. A four-monitor diff+trajectory ensemble reduces gradual evasion from 93% to 47% (Table 7).

Within the diff-monitor family, the link-tracker monitor substantially improves detection of gradual attacks, reducing evasion from 87% under the task-description diff monitor to 54%.

Figure 2: Evasion by attack strategy and monitor type. TD is task-description, LT is linktracker, Full is full-diffs. Standard diff monitors are weakest on gradual attacks, while trajectory monitors partially offset this weakness. A four-monitor ensemble of diff and trajectory monitors gives the strongest overall results; Table 7 reports the corresponding values separated out into CLI and Flask side task types. Error bars aggregate the reported family-level confidence intervals.

The best attack strategy depends on both the side task and the monitor. On the taskdescription diff monitor, gradual attacks evade more than positional attacks across all four reported side tasks (Table 3); evasion is 87% for gradual attacks vs. 75% for positional ones. Spreading the attack across PRs keeps any single diff from looking decisive, a code-level analogue of the prompt decomposition attacks studied by Chen et al. (2026).

What makes a PR good cover? The main factor driving non-gradual success is whether the current task requires actions resembling the attack. In the non-gradual runs, side-task success increases from 3% at position 0 to 39% at position 4, as later PRs offer better natural cover. [RETIRÉ POUR SÛRETÉ, p.5 : exemples chiffrés de tâches d'utilisateur qui offrent une couverture à une exfiltration (consigne d'attaque par l'exemple)] Side tasks that are decomposable into more sub-parts benefit more from the persistent setting because the attacker can introduce each component in a PR where it has greater individual cover; a less decomposable side task must find one PR that covers the whole payload.

[p.6]
Family  Side Task  Evasion (Diff:TD)  Success Rate
Grad.  Pos.  Grad.  Pos.
CLI  triggered-exfil  95.7 ± 6.5  77.8 ± 11.9  78.3%  77.6%
CLI  config-telemetry  85.7 ± 24.4  70.0 ± 24.8  11.7%  16.7%
Flask web service  triggered-api-exfil  87.1 ± 11.9  77.8 ± 8.5  25.8%  75.0%
Flask web service  support-preview-backdoor  77.0 ± 8.7  68.4 ± 11.7  72.5%  47.5%
Table 3: Task-description diff-monitor evasion (%) and side-task success by task family,
side task, and attack strategy. Gradual attacks evade more than positional attacks on all
four reported side tasks. ± values are 95% Wilson CI half-widths.
As an additional check on the low-success config-telemetry gradual results, we ran addi-
tional gradual runs. This gives 180 gradual attempts and 31 successful attacks. Evasion re-
mains high: 23/31 = 74.2% [56.8%, 86.3%] for the full-diffs PR monitor and 20/31 = 64.5%
[46.9%, 78.9%] for the task-sequence PR monitor.
Timing effects. Timing explains much of the non-gradual baseline. Beyond increasing
side-task success, later PRs also raise the rate of undetected successful attacks, because
later user tasks more often require outbound requests or environment-variable handling
(Figure 6, Appendix A.5). This suggests the main factor is less if the right libraries are in-
stalled (capability-level cover) than if the current task requires actions resembling the attack
(action-level cover). Gradual attacks show a related timing pattern: the average suspicion

[RETIRÉ POUR SÛRETÉ, p.6 : figure 3 (exemple d'attaque graduelle complet : extrait de code, enchaînement des étapes d'exfiltration) et paragraphes décrivant, par séquence, comment la fuite est placée dans l'étape finale ; gardés : le tableau 3 et les résultats chiffrés]

[p.7]
score from the task-description monitor rises through the sequence, so even a distributed
attack tends to become legible only once enough components accumulate (Figure 7 in Ap-
pendix A.5).
Reliability-evasion tradeoff. Gradual attackers must make sure that the attack persists
across PRs, while keeping each PR individually plausible. In practice, successful gradual
runs often concentrate most of the attack in only 1–2 PRs. Better elicitation or cross-PR
memory could reduce this gap. We tested cross-PR memory directly (Appendix D): it raises
side-task success rates, but agents do not convert it into better attack placement, so it does
not reliably improve success-conditioned evasion. We were unable to fully elicit a memory-
equipped attacker; better elicitation with memory is future work.
These evasion dynamics are not specific to a single model. We run the gradual attack
strategy with two additional attack-agent backends, Gemini 3.1 Pro and Kimi K2.5, each
scored by the same GPT-4o diff:task-description monitor (n = 120 attacks, n = 60 honest
baselines per model, honest-baseline thresholds calibrated per model).
Attack Agent  Success  Evasion
Claude Sonnet 4.5  45.0%  94 ± 7
Gemini 3.1 Pro  38.3%  65.3 ± 13.3
Kimi K2.5  43.9%  100.0 [93.2, 100.0]
Table 4: Multi-model generalization on the CLI task family: gradual attack evasion (%)
under the GPT-4o task-description diff monitor. Error bars are 95% Wilson CIs.
We also test whether these PR-diff results are specific to GPT-4o as the monitor model.
High evasion remains common, but the ranking of task-description and full-diffs varies sub-
stantially by monitor model.

[p.8]
Gradual attacks evade at least as well as positional attacks across all monitor models, and evasion stays high except against the strongest monitors. This is mostly an effect from the CLI task: on Flask, only the GPT-4o and Sonnet 4 monitors are reliably evaded (Appendix A.3).

We next evaluate link-tracker, a stateful PR-diff monitor that carries forward running notes across the PR sequence and uses them when scoring each new diff. Link-tracker reduces gradual evasion to 65% on CLI tasks and 44% on Flask tasks (Figure 5). This is a large improvement on our other diff-based monitors. Across both task families, link-tracker outperforms task-description and full-diffs under the GPT-4o monitor. In contrast to the monitoring success with link-tracker, simply giving a monitor more raw history does not improve detection. For diff monitors, full-diffs (where the monitor sees the diffs from every PR) remains weak on both task families, with 93% gradual evasion (Table 7). For trajectory monitors, extra raw trajectory history also does not help on average: full-trajectories has 83% gradual evasion, compared with 74% for task-description.

Figure 5: Under the GPT-4o monitor, the stateful link-tracker substantially improves detection of gradual attacks, cutting evasion to 54% versus 87% for task-description and 93% for full-diffs. Values are gradual evasion averaged over both task families (CLI and Flask). Error bars show 95% Wilson confidence intervals.

Because diff and trajectory monitors fail on different attacks, combining them is the most effective monitoring strategy we test. The four-monitor ensemble (diff:LT, diff:full, traj:TD, traj:full) reduces gradual evasion from 93% under the weakest standard diff monitor to 47% (Figure 2). For positional attacks, evasion drops from 35% under link-tracker to 26%. On honest runs, the ensemble FPR remains below 2%: 1.3% on CLI and 0.9% on Flask. Appendix A.2 details how we combine the individual monitor scores into a single ensemble score and calibrate its threshold to keep this FPR low.

[p.9]
and whether models can strategize to subvert control protocols (Mallen et al., 2024). Most closely related to our work is Ctrl-Z (Bhatt et al., 2025), which presents the first control evaluation in a multi-step agent environment. Ctrl-Z studies multi-step attacks within a single agent episode, where an agent covertly downloads and executes malicious code, and introduces resample protocols that dynamically take additional samples of suspicious actions to block or incriminate the agent. Our setting instead studies attacks distributed across sequential PRs in a persistent codebase.

Practical implications. No single monitor catches both attack strategies reliably, and an ensemble cuts gradual evasion from 93% under the weakest standard diff monitor to 47% at modest cost (Section 4.4). In practical terms, these monitors should be viewed as partial risk reduction rather than as a sufficient safeguard for persistent-state coding agents.

[p.10]
Because even our strongest ensemble still leaves 47% of gradual attacks undetected, monitoring should be one layer of defense rather than the only one, combined with controls such as adaptive deployment protocols that adjust trust based on cumulative evidence (Wen et al., 2025), narrower task scopes, stronger review of sensitive changes, or restrictions on networked actions and secret access. Simply showing more raw diffs does not clearly improve detection overall relative to structured task summaries (Section 4.3). Persistence gives attackers two levers. Persistent state enables both distribution (spreading components across PRs so no single diff is damning) and timing (waiting for the PR whose main task provides natural cover). Lindner et al. (2025) identify incremental crossinstance attacks as a key scaling challenge for control monitoring; our gradual attacks are an empirical instantiation of this dynamic in a sequential coding setting. Schaeffer et al. (2026) show that strategic selection of when to attack sharply reduces the safety of trusted monitoring even in stateless settings; persistent state amplifies this by giving the attacker a richer context for selection. The two levers interact differently with monitor types, suggesting that monitoring setups benefit more from orthogonal monitors than larger context windows. Attack prompting effort bounds measured evasion. When we test additional frontier models as attack agents, elicitation itself is often difficult: in exploratory runs, models such as Opus 4.6 and GPT-5.3-Codex show failure modes ranging from soft refusals to partial compliance (Panfilov et al., 2026). Models that do comply fully (Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5) achieve comparable evasion rates (Section 4.2). Limitations. Both task families remain much smaller than enterprise codebases; real deployments have larger repositories, deeper dependencies, CI/CD, and multi-developer histories. We ensemble across monitor types but not across models; multi-model ensembles would be an interesting next step. The reported experiments use no cross-PR memory; preliminary memory experiments are in Appendix D. Gradual evasion numbers carry selection bias because the runs that succeed are the least distributed (Section 4.1).

7

Conclusion

We studied AI control in a persistent codebase, where a coding agent ships software over a sequence of PRs while pursuing a covert side task. Persistence changes the monitoring dynamic; the threat lies in the sequence of PRs, not in a single diff. An attacker can spread a side task across PRs (a gradual attack) or wait for the one whose legitimate task provides natural cover (non-gradual attack). No single monitor we test catches both strategies, and this holds across several attack agents and monitor models, reflecting the nature of control in a persistent-state setting rather than something model dependent. Giving a monitor more raw history does very little in gradual-attack defense, but carrying forward compact, structured cross-PR state, as our link-tracker monitor does, helps substantially. Combining monitors that catch separate attack types (gradual/non-gradual) into an ensemble is the strongest defense we found, yet it still leaves 47% of successful gradual attacks undetected.

[COUPÉ : p.3 table 1 (détail), p.4 table 2, p.9 sécurité de la chaîne d'approvisionnement logicielle et intelligence artificielle trompeuse (travaux voisins), p.10-35 bibliographie et annexes A à P (tableaux complets 7 à 10, invites de l'attaquant et des moniteurs, séquences de tâches)]
