## 7. Rishub Jain, Josh Jacob (Sampura Research) — robustness of AI judges under optimisation pressure [if added]

**Why this project.** Paper C of my programme asks whether a monitor can be moved rather than evaded, and at what cost: a deference law under graded pressure, judges versus probes. The sycophancy law is the judge-side half, measured on a model used as a judge; the probe side is the adversarial-evasion cost on activations.

**What I would do.** One optimisation game: a policy trained against a fixed LLM judge on a safety-relevant task with known ground truth, the pressure varied by training steps. Primary, preregistered outcome: the drift of the judge's verdicts, measured with the displacement law (gain, target) as a function of pressure, against the ground truth. Secondary: the same measurement on an activation probe at matched false-positive rate. Stretch: harder safety-eval items built from the failure modes found. Deliverable: a preprint, the game and the evaluation items.

**Relevant experience.** LLM-judge pipelines with ordinal judges and exact nulls; construct validity of judges; control programme.
