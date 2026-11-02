# Pivotal 2027 Q1 — application to Paul Colognese and Francis Rhys Ward (Arrow Research) — v17
2 November 2026. v17 = v16 with the concern sentence of Q2 in Lazar's wording (19:00 UTC), verbatim, no substance change; v14 = v13 with Q1 shortened to 197 words (cuts only, given to Lazar at 12:47 UTC and pasted by him in the form, 13:11 UTC); v13 = v12 with the optional answer as Lazar pasted it in the form (13:11 UTC), one substance fix (« out of three resisting seeds » → « one resisting seed out of three ») and the unfinished phrase completed (« honest episodes »); v12 = v11 with Q1 rewritten by Lazar (12:46 UTC, after the deadline; the form is still editable per Lazar), substance-only minimal fixes. v11 answers the two questions the form actually asks (received 12:52 Paris): an ML experiment run end to end (max 200 words) and, optional, their post « Character training can mitigate reward hacking, but can also make it harder to detect » (LessWrong, read 12:54 Paris). Q1: Lazar's last wording (form review, 12:57) with the four substance corrections given at 12:58; whether Lazar applied them before submitting is not known here. No figure from their post.

## Q1 — Describe an ML experiment you ran end to end (max 200 words)

Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the ordinal judge. Permutation nulls. Performed surgery on history and compared to a sham of the same length. All pre-registered and hash-locked.

When you're being sycophantic you're moving towards a set point, not randomly changing odds. It's proportional to distance from the set point. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure. A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%.

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).

## Q2 (optional) — their post: anything to do differently, most interesting finding

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning never includes the hack. One of my biggest concerns about this type of training is that we can train away blatant forms of bad logic but more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well.

Things I would do differently: (1) using more seeds per character, since one resisting seed out of three is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest episodes.
