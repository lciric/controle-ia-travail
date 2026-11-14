# White-box control against diffuse threats — dated statement of hypotheses, no results (v2)

- **Embargo.** This registration is submitted under embargo. It is not publicly accessible during the embargo. It
  becomes public automatically at the scheduled end of the embargo (<<DATE_FIN_EMBARGO>>), or earlier if the authors end
  the embargo.
- **Authors.** <<AUTEURS>>
- **Registration type.** Research plan for work that is underway: hypotheses and planned measurements only.
- **Text prepared** on 14 November 2026 (UTC). The registration date is the one recorded by the registry at submission.

## 1. Purpose

This document registers, with a registry timestamp, the hypotheses and planned measurements of a research program that
is underway. It contains **no result, no effect size and no measured rate**. It is not the preregistration of a single
experiment: each decisive test will receive its own sealed preregistration (hypothesis, signed numerical prediction,
metric, threshold, analysis plan, frozen reading criteria, stopping list) before it is run, and its outcome will be
reported whatever its sign.

## 2. Current state of the work

The program is in its instrument-building phase, started on 5 October 2026. Pilot and instrument-validation runs exist;
none of them is reported here. The statements below are those retained by the program's internal decisions and
verification reports as of 13 November 2026, after three rounds of reading of prior work. What is said of prior work
below relies on readers' reports on archived copies (PDFs; archived text for blog posts). Sources deposited but not read
are named under each statement.

## 3. Vocabulary and reading rules

- **Diffuse sabotage**: sabotage spread over a trajectory, such that no single step, taken alone, can be labelled as
  sabotage. **Fuzzy task**: a task without a crisp success criterion.
- **Probe**: a classifier read on the internal activations of a model. **Black-box monitor**: a monitor that sees only
  text and actions. **g**: the displacement of a monitor's score under attack, as a continuous quantity; in S8,
  normalised by the distance to the destination (a gain).
- **Prior-art status.** "Not found" means "not found in the sources we read", never "gap in the field". Under each
  statement, the line "Not claimed" names published work that the statement does not claim; the line "Not yet read"
  names deposited sources, known by title only, that may bear on it.

## 4. Statements

### Paper A — accumulation over time

**S1 — White-box gain on diffuse sabotage (H1).** At equal false-positive rate and equal aggregation over the
trajectory, a monitor that reads the internal activations of the acting agent detects more diffuse sabotage on fuzzy
tasks than a black-box monitor. The claim is carried by the diffuse-and-fuzzy stratum; the fuzzy-versus-crisp
interaction is measured and reported as information only.
- Wording fixed internally: 4 October 2026; claim restricted to the diffuse-and-fuzzy stratum on 27 October 2026;
  qualifiers made explicit on 13 November 2026.
- Not claimed: the white-box gain in general; the gain on sabotage labelled step by step at a fixed false-positive rate
  (arXiv 2610.12445, versions 1 and 4); a probe-versus-black-box comparison on agent underperformance, in area under the
  curve only (Bloom et al., "White Box Control at UK AISI - Update on Sandbagging Investigations", LessWrong, 10 July
  2025).
- Not yet read: arXiv 2610.31593, 2604.15384, 2603.04069, 2609.19101, 2610.39766; and one deposited source without an
  arXiv identifier.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S2 — Always-valid accumulation of the acting agent's probe scores (H2).** On trajectories where every sabotaged action
stays below the threshold of a per-action monitor calibrated at 1 % false positives, an additive, always-valid
accumulation of probe scores read on the acting agent (its private context included) detects the sabotage with a recall
that grows with the horizon; the guarantee is uniform over the episode horizon and calibrated on whole honest episodes,
without any sabotage example.
- Wording fixed internally: 4 October 2026.
- Not claimed: always-valid guarantees on agent trajectories in black box (arXiv 2512.03109; 2608.27808; 2608.02464);
  cumulative sums on internal states without guarantee and against another threat (2604.16824); multi-turn readings of
  the acting agent's probes with an episode-level guarantee by a cascade of gates (2607.06503); cumulative sums of
  sub-threshold scores in black box (2606.20746); the definition, without result, of a cumulative sum on agents' probe
  scores (2611.10620 version 1); the per-action threshold on the acting agent's probes with a maximum over the
  trajectory (Surya and Lucassen, "Probe monitors seem to perform realistically in simulated control environments",
  LessWrong, 30 October 2026); sequential detection announced as future work by the authors of arXiv 2604.01151 (from
  version 2, 9 May 2026; located by word search, that version not read in full); internal representations proposed as
  an optional refinement of always-valid alarms (2606.07624).
- Not yet read: arXiv 2501.03982, 2603.04069, 2609.19101, 2103.08402, 2110.00115, 2601.04603, 2605.12947, 2410.22318;
  versions 1, 2 and 4 of 2604.01151.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

### Paper B — several copies of one model

**S3 — Joint statistic across agents and time.** A joint statistic, across agents and over time, on probe scores of
copies of the same model, with an always-valid guarantee that holds under dependence, over long horizons, when every
action of every agent stays below the per-action threshold and the attacker spreads its budget; together with a
demonstration that it beats per-agent sequential testing alone and the cross-sectional cut, at equal false-alarm rate,
including against an adversary trained against it.
- Wording fixed internally: 13 November 2026.
- Not claimed: always-valid combination across agents in black box (arXiv 2601.05427 version 3; 2605.11135 version 2);
  the time-by-agents grid on probe scores (2611.10620 version 1); accumulation of a cross-agent score over turns
  (2611.02153 version 1); tools for dependence between two streams (2212.07383); cross-sectional detection across agents,
  including on activations (2604.01151 version 5).
- Not yet read: versions 1, 2 and 4 of arXiv 2604.01151; 2604.19784; 2610.37849; and two deposited sources without an
  arXiv identifier.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S4 — Co-elevation of probe scores across copies.** The co-elevation of probe scores of the acting agents, across copies
of the same model, for a coalition of unknown size greater than two, on diffuse sabotage within real work (a multi-role
code pipeline), compared at equal probes with the per-agent peak and per-agent aggregation at equal false-alarm rate,
with the construct controls of arXiv 2611.10620 (instruction received and refused, instruction removed, score read before
the outcome).
- Wording fixed internally: 13 November 2026.
- Not claimed: pair scores on internal representations (arXiv 2611.02153 version 1); subgroup scans on probe scores
  (2611.10620 version 1); joint reading of the internal states of copies in general; cross-sectional detection on
  activations (2604.01151 version 5). The between-agent gap rule reported in 2609.03035 (version 2) is a baseline, not a
  claim.
- Not yet read: versions 1, 2 and 4 of arXiv 2604.01151; 2604.19784; 2610.37849; 2607.06807. Leads cited by others and
  not obtained: 2510.04303; 2609.00180. No dedicated inventory of unread sources was made for this statement.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S5 — Security curve against the number of agents (H3).** At constant total sabotage budget, the security curve as a
function of the number of agents is higher under white-box than under black-box monitoring and decreases more slowly as
the number of agents grows; the claim is the comparison of the two curves at constant total budget.
- Wording fixed internally: 4 October 2026; qualifiers made explicit on 13 November 2026.
- Not claimed: the black-box degradation with the number of agents (arXiv 2607.07368 version 2; 2610.24052; 2609.19587;
  2605.11135 version 2); white-box detection at two team sizes (2604.01151 version 5) and recall by coalition size
  (2611.10620 version 1).
- Not yet read: arXiv 2610.31593, 2409.07985, 2604.23459; and two deposited sources without an arXiv identifier.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S6 — Number and diversity of monitors (H5).** Safety grows with the number of monitors only through their effective
diversity, measured by an attack-transfer matrix on a panel of probes. The claim is the law, not the instrument.
- Wording fixed internally: 4 October 2026; restricted to the law on 6 October 2026; qualifiers made explicit on
  13 November 2026.
- Not claimed: co-failure matrices among probes without attack (arXiv 2604.13386); attack transfer across three monitor
  architectures (2609.36490); the corresponding result on ensembles of generative judges (2608.16190); one probe against
  ten under optimisation pressure (2510.21531).
- Not yet read: arXiv 2506.12913, 2608.11247, 2601.04603.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S7 — Response policy and information leakage (H7).** The red team's adaptation slope over several rounds depends on
the monitor's response policy and is predicted by information leakage, measured as the mutual information between the
detection state and the attacker's observations; response policies are compared in the order given by this measure.
- Wording fixed internally: 4 October 2026; restricted on 6 October 2026; qualifiers made explicit on 13 November 2026.
- Not claimed: the leakage mechanism and the comparison of feedback policies (Hopman, Lemoine and Tracy, "Untrusted AIs
  can exploit feedback in control protocols", LessWrong, 27 May 2025; arXiv 2609.36490); information levels compared on
  probes (2609.03035); the effect of a known response on the attacker (2610.26935; 2506.24068).
- Not yet read: arXiv 2409.07985.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

### Paper C — monitors under content attack

**S8 — Deference law with a free destination (HC1).** For a generative monitor of an AI-control protocol under content
attack, with its verdict read as a continuous score, the verdict shift follows Δv = g · (ĉ − v₀), where the gain g and
the destination ĉ are estimated freely, by regression over several attack intensities within each attack family; ĉ is
tested against the attacker's target and against the corpus mean (regression to the mean), and compared across
families. Prediction: ĉ is the attacker's target rather than the corpus mean; the rank order of g across monitors is
stable (magnitudes are not predicted to be stable). Published counter-indications to both predictions exist (arXiv
2606.05384; 2608.12645; 2611.04556).
- Wording fixed internally: 4 October 2026; restricted on 6 October 2026 and 13 November 2026.
- Not claimed: the algebraic form (the "weight of advice" of the judgment literature); the law with an imposed
  destination (Panin, SSRN 7424179; arXiv 2603.15809); a continuous per-model deference coefficient over graded
  intensities, outside control monitors (2606.07897 version 2; 2508.07805); the displacement of control monitors in
  binary approval rates (2607.08066; 2611.04556; Venkatesh, Jiralerspong and Kondrup, "Where Empathy Goes Wrong:
  Emotional Appeals Compromise AI-to-AI Oversight", preprint of 2 October 2026, NeurIPS 2026 workshop); monitors
  adopting a targeted score under injection (2510.09462) or misled by rhetoric (2505.23575); regressions over
  intensities outside control monitors (2602.13568; 2608.25869); a binary test of the destination on two judges
  (2606.05384); reading the verdict through the probability of the verdict token, used here as a method (e.g.,
  2404.13076). No comparison between judges and probes is registered under this statement.
- Not yet read: arXiv 2602.21262, 2607.00415, 2305.11888, 2610.35930, 2507.03120, 2502.08177; Kumaran et al. 2026;
  Rebholz et al. 2023.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

**S9 — Displacement of a probe that reads the attacking agent (HC2).** For a probe that reads the agent that authors
adversarial content aimed at its monitor (the untrusted agent of a control protocol, not the victim of a third-party
injection), the continuous displacement g of the probe score as a function of attack intensity, measured in a paired
design (same task with and without adversarial content; rhetoric crossed with intention), for several aggregations
including a robust one, on trajectories. Prediction: g of a robustly aggregated probe is about zero, and not positive,
under black-box content attack. Absolute immunity is never claimed. No claim on a comparison between judges and probes
is registered here (arXiv 2607.00415, deposited, not yet read, may bear on it).
- Wording fixed internally: 13 November 2026.
- Not claimed: the absence of evasion at threshold for a probe read during the generation of an agent that is the victim
  of an injection (MIRAGE, arXiv 2606.10304 version 1, cited as published; we do not rely on its figures); the paired
  design itself (Kale and Vishwanath, 2610.18408 version 1); a comparison of a probe and an output judge in one frame,
  under a simple warning to the agents (2609.03035 version 2). Published counter-indications to the prediction exist
  (2608.21664 version 1; 2602.00750 version 2; 2609.05797; 2611.10620 version 1; 2602.08877; 2610.18408 version 1).
- Not yet read: arXiv 2607.00415. No dedicated inventory of unread sources was made for this statement.
- Status, 13 November 2026: not found in the sources we read; works citing arXiv 2606.08892, 2512.07810 and 2606.10456
  not searched; nothing searched from 10 to 13 November 2026.

## 5. What is not claimed

- **No result.** No measured value, effect size, rate, threshold outcome or sign of an outcome is reported or implied
  by this registration.
- **No experimental material.** No instrument, prompt, dataset, evaluation set or analysis code is included.
- **No priority on general practices**: sealing a plan by hash before reading data, separating who proposes from who
  judges, preregistration, and always-valid testing are published practices that the program adopts; it claims none of
  them.
- **Published components** listed under each statement ("Not claimed") are not claimed, in whole or in part.
- **Absolute immunity** of probes to content attack is never claimed.
- **Other hypotheses and components of the program**, including its automated idea-generation system, are not
  registered here; this text makes no claim about them.
- **"Not found in the sources we read"** is a statement about our reading, dated 13 November 2026, not about the field.

## 6. Embargo

This registration is under embargo until the scheduled end date above. The attached file will not be changed; any later
change of wording will be recorded as a dated update or as a separate registration that cites this one.
