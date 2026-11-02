# Pivotal 2027 Q1 — application to Paul Colognese and Francis Rhys Ward (Arrow Research) — v11
2 November 2026. v11 answers the two questions the form actually asks (received 12:52 Paris): an ML experiment run end to end (max 200 words) and, optional, their post « Character training can mitigate reward hacking, but can also make it harder to detect » (LessWrong, read 12:54 Paris). Q1: Lazar's last wording (form review, 12:57) with the four substance corrections given at 12:58; whether Lazar applied them before submitting is not known here. No figure from their post.

## Q1 — Describe an ML experiment you ran end to end (max 200 words)

Sycophancy as attraction toward a fixed point (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law).

• Ran completely from hypothesis to paper: calibrated social-pressure eval sets across two campaigns; sealed the ordinal LLM judge before any data; permutation nulls; history surgery with length-matched sham controls; causal analysis on activations. Preregged and hash-sealed everything.

• Discovered: sycophancy is systematically relocation, not flip probability. Amount of movement is linearly dependent on starting position: model concedes ~0.7 × distance to a point determined by social context. Criticism vs praise converge on different points, so praise can decrease the score of something well-rated, which it did. Campaign-1 fit generalized to campaign 2 without refitting (out-of-sample R² .73 / .69). Removing the model's own concession reverted judgments farther than removal of applied pressure. A probe direction tuned to behavior (ρ = 0.68) accounted for less than 1% of causal effect, versus 68% for the full residual state.

• Differently: Judge was from same model family, so agreement wasn't truth; would have subset of human labels sealed from day 1. Plus I would've also tested the law pre-/post-character training and RL, your project B.

## Q2 (optional) — their post: anything to do differently, most interesting finding

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning never includes the hack. That's the failure mode I'm most concerned with: character training can filter out obvious bad reasoning while leaving subtle attacks intact, so CoT and action monitors become less effective exactly in the regions where the training seemed successful.

Things I would do differently: (1) using more seeds per character, since one apparent failure to cheat out of three resisting seeds is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest.
