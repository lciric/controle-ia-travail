# Pivotal 2027 Q1 — application to Stefan Heimersheim (Google DeepMind) — v12
2 November 2026. v12 answers the two questions the form actually asks (received 11:15 Paris); it replaces the three paragraphs of v11 for this form. Q1 is given in a full version and in a 150-word version: use the full one unless the form's counter caps Q1 at 150 words. Q2 is under 150 words. Figures are from the sycophancy manuscript (Llama-3.1-8B-Instruct), already used in v11.

## Q1 — direction most likely to fail, and why

### Full version

(c) Activation steering against evaluation awareness.

The goal is to see how a model behaves when it believes it is not being evaluated: find a direction that reads "I am being tested" and subtract it. I think this is the most likely of the seven to miss its goal, for three reasons. I think that because I have run the same recipe on a neighbouring construct and watched it fail.

1. Readable is not causal. On Llama-3.1-8B-Instruct I found a direction that tracks sycophantic judgement shift (ρ = 0.68 with behaviour) and carries under 1% of the causal effect, against 68% for the full residual state. Six rank-1 interventions on it (steering, directional ablation, SAE clamping, fine-tuning against the probe, head/MLP zeroing) left judged behaviour unchanged. A rank-3 subspace from SVD of activation differences did move it, but a zero-pressure control showed the shift to be generic: verdicts moved with no social pressure applied. An evaluation-awareness vector found by contrastive prompting is the same kind of object. The likely outcomes are that nothing happens, or that something generic happens which cannot be told apart from damaging the model. The second is easy to report as success.

2. The construct is contaminated. "This is a test" co-varies with register: formal, artificial, multiple-choice, short context. A direction found by contrasting eval-like and deployment-like prompts reads the mixture. Steering against it pushes the model toward informal, deployment-like output, which looks exactly like "the model relaxed". A readout that separates the belief from the register is needed, and the model's verbal report is not that readout, since what it says and what it knows is precisely what is in question. Without it the test is unfalsifiable.

3. Suppressed is not removed. The belief is rebuilt from many weak cues over the whole context. A vector subtracted at one site is re-derived downstream, so suppression has to be continuous and at a dose. That dose may sit past the point where perturbations stop being neutral (your plateau question), and then the behavioural change is the intervention, not the belief.

What would change my mind: a dose–response curve for the awareness vector against a norm-matched random control, a behavioural ground truth for the belief that is not the model's own report, and a check that the steered model is not generically degraded. That is the experiment I would want before believing a steering result, and the one I would run.

### 150-word version

(c) Steering against evaluation awareness. Most likely failure: the direction that reads "I am being tested" is not the one doing the causal work. On Llama-3.1-8B I found exactly this for sycophancy: a direction with ρ = 0.68 to behaviour carried under 1% of the causal effect, against 68% for the full state; six rank-1 interventions did nothing, a rank-3 subspace moved behaviour, and a zero-pressure control showed that shift was generic. Second, the construct is contaminated: eval-like prompts also differ in register, so steering against the vector yields informal output that looks like "relaxed". Third, suppressed is not removed: the belief is re-derived downstream from many weak cues, so the dose needed may lie past the point where perturbations are neutral. A steering result would convince me with a dose–response curve, a norm-matched random control, and a belief readout that is not the model's own report.

## Q2 — why mechanistic interpretability (under 150 words)

Because I want to know whether what a probe reads is what the model uses. I came to this from neuroscience, low-rank recurrent networks and population dynamics, where a readable low-dimensional structure and the dynamics that drive behaviour can be different objects. My result on Llama-3.1-8B, a direction that predicts sycophancy and does under 1% of the causal work, is that gap in a language model. It matters for safety because activation monitors, steering defences and evaluation-awareness tests all assume the gap is small. I want to measure where it is small and where it is not, with preregistered interventions and controls, and publish the negative results. Your plateau question is the cleanest version of that measurement I know: it asks for a dose–response curve instead of a single intervention, which is what my rank-1 versus rank-3 result lacked.
