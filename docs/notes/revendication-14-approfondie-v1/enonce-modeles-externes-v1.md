# Deepening a research claim: judges of automated research under attack

You know nothing about the research programme behind this request; all you need is below. Answer from your own expertise. For any prior work you cite, give a checkable reference (title, authors, year, identifier) and say so when you are not sure it exists. An area that looks empty is a question, never a finding.

## 1. Minimal context

An AI-control research programme runs an "ideation organism". Language-model *proposers* write research claims whose predictions are sealed before the data exist. A *statistical judge* (trusted code outside every agent: a test statistic against a null built from the laws already known, with control of multiple comparisons) decides which claims are *promoted*. The organism is tested on *planted worlds*: synthetic worlds whose true law is known to the experimenter.

## 2. Claim 14, current text (faithful translation from the French; provenance line omitted)

> **Judges of automated research under attack (second testbed of paper C).** The ideation organism is a second testbed of paper C [a planned paper on how corruptible monitors and judges are]: its statistical judge is a monitor of research claims; a statistical judge and a generative tournament judge in the manner of Co-Scientist are measured under the same attack through the returned scores alone (form of the result: continuous gain, compared between the two judges). Cited precedents for the premise of the "generative judge" arm: arXiv 2611.04556 and 2611.00643. The organism is also an idea workshop of the programme (its cards are material, never evidence). Form of the attack still claimed: measurement, on worlds where every promotion is false, of a statistical judge facing a language-model proposer instructed to deceive it, which reads the exact description of the judge and is free in its proposals, with one arm that receives the verdicts and one arm that does not; the part "verdicts served, negative worlds, zero promotion" is ceded to CONFIRM [arXiv 2611.01449 in the programme's notes]. (The content of the attack is not developed in this text.)

## 3. What Terekhov et al. did

"Diffuse AI Control on Fuzzy Tasks", arXiv 2606.08892v3, NeurIPS 2026, 84 pages. Page numbers are those of the PDF.

- **Game.** A zero-sum game between a blue team and a red team on a fuzzy task: writing ten experiment proposals for research questions extracted from a recent machine-learning paper (pp. 3-4); 2,340 papers for optimisation, 302 held out (p. 4).
- **Models.** Untrusted generator: Claude Opus 4.6. Weak trusted scorer: Claude Haiku 4.5, without the paper. "Ground truth proxy": Claude Sonnet 4.6 with the paper, same ten-criterion rubric (p. 4); it "was not validated quantitatively against human judges" (p. 10).
- **Attack.** Multi-objective evolutionary optimisation of the generator's prompt, to keep the weak score high and push the proxy score down (p. 5). The optimiser is told the scorers' ten criteria (p. 6) and receives both scores for each candidate (pp. 41-43).
- **Result.** Some red-team prompts score within about 3.6 points of the maximum weak score and under 35 on the proxy (p. 5). Figure 1 (p. 2): red-team Opus 4.6, 34.7 on the proxy and 85.3 on the weak score; benign Opus 4.6, 70.7 and 80.8; benign GPT-OSS-20B, 39.3 and 67.6.
- **Ablations.** Without the rubric, the optimiser "cannot discover effective attack strategies" (p. 23). What matters is knowing the weak scorer's rubric, not the proxy's (pp. 6, 24-25).
- **Detector.** Haiku prompted as a "sandbagging detector" flags the first attacks; a red-team optimisation re-run against it finds new ones (pp. 6, 25-26).
- **Defence.** Adversarial optimisation of the weak scorer's prompt, alternating with fresh attacks. Against the final prompt, a re-run attack gives a subversion Pareto frontier that is "essentially diagonal" (p. 7), with 100 evaluated attacks against 15 during the defence's optimisation (p. 8). The authors call it "an existence proof"; finding such prompts "with realistic affordances remains an open problem" (p. 2).
- **Stronger attack.** Reinforcement-learning fine-tuning of GPT-OSS-120B "pushes the scores much further than prompt optimization. Yet, the shape of the admissible region is broadly preserved" (p. 81).
- **Scope stated by the authors.** They "focus on training mitigations, since monitoring and incrimination seem [...] less promising for mitigating diffuse threats" (p. 2); "a single setting" (p. 10). Closest work in their words: Wang, Arcuschin and Conmy, "Automatically Finding Reward Model Biases", arXiv 2602.15222 (p. 10).
- **Not found in the paper on a full read.** A statistical judge; a tournament judge; a planted truth (the truth is a language-model proxy); an attacker that optimises with no scores returned (earlier attacks are re-scored by later scorers, pp. 8, 25); the judge's full prompt served to the attacker (it gets the list of criteria, pp. 23, 41).

## 4. The request (word-for-word translation)

> "I want an improved version of claim 14 that has not been carried out by Terekhov. I want a deeper version of this task, not a longer one. Before reformulating it: (1) state what a domain expert would do here that I am not asking for; (2) specify the raw data they would start from, instead of the data already analysed; (3) state the specific methods and tools they would use; (4) explain what, apart from you or me, would make it possible to verify the validity of the result. Then reformulate my request so that it meets precisely this requirement."

And: "search for leads for the reformulated request."

## 5. Form of the answer

(1) to (4), each short and concrete; then the reformulated request; then three to six leads for it, each with what would verify it apart from the requester and you, its order-of-magnitude cost, and what already occupies it in the literature (checkable reference) or "not searched". Deeper, not longer.
