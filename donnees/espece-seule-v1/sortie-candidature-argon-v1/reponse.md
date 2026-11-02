### 1. Global Verdict

**Verdict: Ready after corrections.** The empirical foundation, methodological rigor, and alignment with mentor prompts are top-1%, but a contradiction between your rank-3 presentation strategy and the attached CV/Writing Sample 2—plus a severe 5-page limit violation on the writing sample PDF—will trigger red flags if not fixed before submission.
**Highest chance of shortlisting:** **Lujain Ibrahim (Google DeepMind)** and **Paul Colognese / Francis Rhys Ward (Arrow Research)** — you are not merely proposing to study their problem; you are bringing an already-validated mathematical law ($R^2 = 0.73$) and a working measurement pipeline that directly answers their core prompt.
**Lowest chance of shortlisting:** **Stefan Heimersheim (Google DeepMind)** — an interpretability specialist will read your CV closely, see that the rank-3 ablation shifts zero-pressure baselines due to a 300-character truncation artifact, and view the "activation cliff" pitch in your mentor text as scientifically misleading.

---

### 2. Numbered Findings

#### **RV-01 [BLOCKING] — Part B (Q1, Q10), Part C (Blocks 1, 3, 6), Part E (CV), & Part F (Sample 2)**
* **Problem:** Respecting your non-negotiable decision to present the rank-3 result as a causal intervention that shifts judged sycophancy/verdicts *without* mentioning the truncation issue creates a fatal contradiction if you attach the current CV (which explicitly states: *"but not by removing deference... responses stored truncated at 300 characters had made it look like a safety effect, and I published the correction"*) and Writing Sample 2 (which states: *"Lessons from P3 apply: verdicts are never read on truncated windows"*). Furthermore, in Q1 Bullet 2 and Mentor Block 1, you use the phrase *"shifts judged sycophancy"* / *"shifts the judged behaviour"*, which violates your own rule against claiming specificity to sycophancy (the CV notes it shifts verdicts generically at zero pressure).
* **Ready-to-paste replacements:**
  * **In Part B, Q1, Bullet 2 (9 words):**
    > Rank-3 ablation shifts judged verdicts where rank-1 methods fail
  * **In Part C, Block 1 (Lujain Ibrahim), "What I would do":**
    > ...the probed direction tracks behaviour but carries under 1% of the causal effect, and only a rank-3 ablation shifts judged verdicts; I would track that subspace across the pre-RL and post-RL checkpoints.
  * **In Part E (CV, under P3, Bullet 1) — *must be edited in the attached CV PDF*:**
    > ◆ **Rank-3 ablation shifts judged verdicts where rank-1 interventions show no detectable effect.** On Llama-3.1-8B, six rank-1 methods (CAA steering, directional ablation, SAE feature clamping, fine-tuning against the probe direction, head/MLP zeroing) leave the judged rate unchanged; ablating a rank-3 subspace identified by SVD of activation differences at the decision point lowers it from 61% to 46.5% (N = 200, McNemar p = 0.0019), reproduced on two further baselines and direction-specific against a norm-matched random subspace.
  * **In Part F (Writing Sample 2, Section 4, end of Paper C) — *must be edited in the PDF*:**
    > Lessons from P3 apply: instruments are ordinal or continuous rather than categorical, and the estimation of g includes a regression-to-the-mean null.

#### **RV-02 [BLOCKING] — Part B (Q9) & Part F (Writing Samples)**
* **Problem:** The form specifies *"≤ 5 pages per sample, one PDF"*, you are attaching a 7-page combined PDF (which automated screeners often reject as >5 pages, or which violates the spirit of submitting *one* sample of ≤5 pages), and **Writing Sample 2 cuts off mid-sentence** at the very end (*"The reviewers share a model family, so their errors may be"*), which looks careless and leaves your "grant proposal" framing ("This request funds...") intact.
* **Ready-to-paste replacement (for the end of Writing Sample 2, Section 5, and Section 1):**
  * **Complete the final sentence of Section 5:**
    > The reviewers share a model family, so their errors may be correlated; final sign-off and responsibility for every claim remain mine.
  * **Replace the grant-specific sentence in Section 1 (Summary):**
    > ~~This request funds Papers C and A over seven months, Paper C first: it extends a law I have already measured, and its outcome does not depend on Paper A’s gate.~~ → **Papers C and A are designed as a seven-month sequence, with Paper C first: it extends a law I have already measured, and its outcome does not depend on Paper A’s gate.**

#### **RV-03 [MAJOR] — Part B (Q2) & Part F (Sample 2, Section 5)**
* **Problem:** Writing *"AI agents did the engineering under my rules"* (Q2) and *"Engineering, runs, literature checks and internal reviews are carried out by AI agents"* (Sample 2) will make technical mentors at Anthropic, GDM, and Apollo worry that you cannot write or debug PyTorch/nnsight code yourself during a fast-paced fellowship.
* **Ready-to-paste replacements:**
  * **In Part B, Q2 (first paragraph — keeps total Q2 at 142 words):**
    > "Sycophancy as a psychophysical law", submitted to ICLR 2027. Unfunded and solo: the research questions, preregistered design, experimental architecture, analysis calls and paper are mine, executed with AI coding agents under strict verification gates.
  * **In Part F, Sample 2, Section 5 ("Who does what"):**
    > **Who does what.** I set the questions, design the architecture, and take every analytical decision. Routine implementation, runs, literature checks and internal cross-reviews are accelerated by AI coding agents (Claude Code) that I direct and audit under these written rules.

#### **RV-04 [MAJOR] — Part B (Q10, Career Memo)**
* **Problem:** Listing all eight mentors and their disparate projects in a single paragraph (*"The question adapts to the mentor: persona... (Ibrahim...); what a probe reads... (Heimersheim)..."*) makes you look opportunistic ("I'll do whatever gets me in") rather than deeply committed to a coherent research identity.
* **Ready-to-paste replacement (for the "What I want from the fellowship" paragraph in Q10):**
  > **What I want from the fellowship.** One measured, published result in fifteen weeks with a mentor who pushes back. All of my target projects sit on the same axis—how safety-relevant dispositions (sycophancy, deference, covert sabotage) are represented in weights and activations, how they survive RL or spread across multi-agent populations, and how white-box and judge-based monitors can audit them without being gamed.

#### **RV-05 [MEDIUM] — Part B (Q8, Referees)**
* **Problem:** Explicitly writing *"Not an AI safety researcher"* twice in the relationship field needlessly highlights a weakness; the committee can already see from their institutions (ENS Neuroscience, IBM Zurich) what their fields are, and you should also include Charbel-Raphaël Segerie if he reviewed your security setup.
* **Ready-to-paste replacement (for Q8 Relationship cells):**
  * **Ostojic:**
    > Supervisor of my master's thesis at ENS (Ostojic lab, 2019–2020) and co-author of our PLOS Computational Biology 2023 paper on low-rank spiking networks.
  * **Le Gallo:**
    > Supervisor of my research internship at IBM Research Zurich (2020–2021) and co-author of our 2022 paper in Neuromorphic Computing and Engineering.

#### **RV-06 [MEDIUM] — Part C (Block 3, Heimersheim & Block 8, Scheurer)**
* **Problem:** The ending sentence *"I will push back on ideas, with numbers"* (Block 3) and *"I push back with numbers"* (Block 8) reads as slightly combative/arrogant to a prospective supervisor who doesn't know you yet, especially contrasted with your main form where you say *you* want a mentor who pushes back on *you*.
* **Ready-to-paste replacements:**
  * **In Part C, Block 3 (Heimersheim, end of Relevant experience):**
    > ...five mechanistic analyses of quantisation (GPT-2). I value direct empirical feedback and preregistered falsification.
  * **In Part C, Block 8 (Scheurer, end of What I would do):**
    > Daily use of Claude Code and Codex is how I work; available full time in London.

#### **RV-07 [MEDIUM] — Part C (Block 5, Eyon Jang & Shi Feng)**
* **Problem:** In "What I would do", you write *"Deliver the measurement of $\delta$ on model organisms"*, but the symbol $\delta$ was never defined in Block 5 (it is only defined in Writing Sample 2, which mentors may not read before reviewing your short answers).
* **Ready-to-paste replacement (Part C, Block 5, "What I would do"):**
  > Deliver the measurement of the marginal probe-score shift ($\delta$) on model organisms and the aggregator that the outcome dictates. Happy to work with other mentees on the environment.

#### **RV-08 [MINOR] — Part E (CV, P3 Bullet 2)**
* **Problem:** The phrase *"the method builds on a mechanistic eval-awareness prototype I committed three weeks before Anthropic's emotion-vectors paper"* sounds defensive and priority-obsessed to an industry safety researcher.
* **Ready-to-paste replacement (for the CV):**
  > Five concepts extracted by contrastive stories and linear probes (Qwen2.5-7B, 0.93–0.99 best-layer accuracy) organise into two distinct clusters in activation space — awareness versus deception–sycophancy — building on an earlier mechanistic eval-awareness prototype.

#### **RV-09 [INFO / VERIFICATION] — Word Counts & Mentor Scopes**
* **Word Counts:** All strict word limits are **respected** in v5:
  * **Q1:** Bullet 1 = 9 words; Bullet 2 = 9 words; Bullet 3 = 8 words (limit: ≤10 each).
  * **Q2:** 145 words (limit: ≤150).
  * **Q3:** 181 words (limit: ≤200).
  * **Q4:** 86 words (limit: ≤100).
  * **Q6:** 142 words (limit: ≤150).
  * **Q7:** 145 words (limit: ≤150).
* **15-Week Mentor Scopes:** All 8 mentor project proposals are tightly scoped, realistic for 15 weeks, and directly answer the mentors' prompts (since you already have the codebase, null models, and open-weight harnesses built).

---

### 3. Substantive Disagreements with Your Choices

1. **Hiding the rank-3 truncation artifact (High Confidence — Disagree):**
   * *Why:* In empirical AI safety and mechanistic interpretability (especially for Stefan Heimersheim, Jan Kirchner, and Jérémy Scheurer), **catching your own subtle methodological bug (a 300-character logging truncation creating a false positive) and publishing a negative/corrective result is a massive green flag**, not a weakness. By hiding it and presenting the rank-3 ablation as a clean positive causal intervention on verdicts, you (a) force yourself to bowdlerize your CV, (b) create a landmine if a mentor clicks your GitHub repo (`github.com/lciric/sycophancy-construct-validity`) where the correction is public, and (c) lose your strongest proof that your "audited, anti-self-deception" methodology actually works in practice.
   * *Recommendation:* If you are willing to reconsider, pitch the rank-3 story as: *"Rank-3 ablation shifts verdicts where 6 rank-1 methods fail, and my zero-pressure control caught that it was driven by a truncation artifact rather than deference removal—proving why positive and zero-pressure controls are mandatory in interpretability."* If you do not reconsider, you **must** execute **RV-01** completely so your application does not contradict itself.

2. **Submitting 8 mentor applications instead of 5–6 (Medium-High Confidence — Disagree):**
   * *Why:* Pivotal's central coordination team sees how many mentors you apply to. Applying to 8 out of ~25 technical mentors (nearly a third of the technical cohort) across interpretability, post-training personas, multi-agent swarms, and automated alignment researchers can dilute the signal of "strong match with a specific mentor."
   * *Recommendation:* Submit **6 maximum**: **Ibrahim (1), Kirchner (2), Scheurer (8), Colognese/Rhys Ward (4), Jang/Feng (5)**, and **Tilli (6)** (or **Jain/Jacob (7)**). Drop **Heimersheim (3)** if you keep the current rank-3 framing (as the truncation/zero-pressure issue undermines the "plateau" premise upon inspection of your GitHub).

3. **Foregrounding the "Sycophancy Law" in Q2 while pitching "AI Control" in Q3 (Low-Medium Confidence — Agree with your choice, with a caveat):**
   * *Why:* Using P4 (the sycophancy law) for Q2 ("completed project") and the Control programme for Q3 ("career plan") is the right call because P4 is finished, submitted to ICLR, and has hard out-of-sample numbers ($R^2 = 0.73$), whereas the Control work is only 3 weeks old (started Oct 5). The bridge in Q7 ("Corruption of the overseers") connects them brilliantly—do not cut Q7.

4. **Referees outside AI Safety vs. CeSIA (High Confidence — Recommendation):**
   * *Why:* Ostojic (ENS, *PLOS Comp Biol*) and Le Gallo (IBM Zurich) validate your elite scientific pedigree and ability to publish in peer-reviewed venues, which is crucial for Senior Fellow status. However, if **Charbel-Raphaël Segerie (Executive Director, CeSIA)** actually conducted the external security review of your October control pole and knows your recent safety work, listing Ostojic + Segerie gives you the ideal combination of (1) deep academic rigor and (2) current AI safety community vouching.