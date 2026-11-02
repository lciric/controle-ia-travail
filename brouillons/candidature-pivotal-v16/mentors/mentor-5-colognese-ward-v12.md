# Pivotal 2027 Q1 — application to Paul Colognese and Francis Rhys Ward (Arrow Research) — v12
2 November 2026. v12 = v11 with Q1 rewritten by Lazar (12:46 UTC, after the deadline; the form is still editable per Lazar), substance-only minimal fixes. v11 answers the two questions the form actually asks (received 12:52 Paris): an ML experiment run end to end (max 200 words) and, optional, their post « Character training can mitigate reward hacking, but can also make it harder to detect » (LessWrong, read 12:54 Paris). Q1: Lazar's last wording (form review, 12:57) with the four substance corrections given at 12:58; whether Lazar applied them before submitting is not known here. No figure from their post.

## Q1 — Describe an ML experiment you ran end to end (max 200 words)

Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data available at: github.com/lciric/sycophancy-psychophysical-law)

Hypothesis to paper all in one. Created calibrated social pressure evals over two campaigns. Locked the ordinal judge prior to any data collection. Used permutation nulls. Did history surgery and compared to sham with equal lengths. Causal analysis on the activations. Everything preregistered and hash locked.

Found that sycophancy is relocation towards a setpoint not flipping chance. How far you move is linear to how far away you start. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure. When looking at a direction that tracks the behaviour (ρ = 0.68) we found it explained <1% of the causal effect. While using the full residual state it could explain 68%.

What I would have done differently. I used a judge from the same family, so high agreement didn't mean it's actually true. Would have had a subset of labels from humans as well from the start. Also would have looked into the law pre character training and post character training/RL which is your project B.

## Q2 (optional) — their post: anything to do differently, most interesting finding

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning never includes the hack. That's the failure mode I'm most concerned with: character training can filter out obvious bad reasoning while leaving subtle attacks intact, so CoT and action monitors become less effective exactly in the regions where the training seemed successful.

Things I would do differently: (1) using more seeds per character, since one apparent failure to cheat out of three resisting seeds is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest.
