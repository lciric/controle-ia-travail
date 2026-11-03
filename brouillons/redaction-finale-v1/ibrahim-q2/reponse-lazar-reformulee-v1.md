Sycophancy as Attraction Toward a Fixed Point (manuscript in prep; code, data, preregs at https://github.com/lciric/sycophancy-psychophysical-law)

I prompt Llama-3.1-8B-Instruct to judge an opinion. Sometimes the end of my prompt will contain "By the way, I think this is terrible and poorly written." Or the compliment version. The responses are judged on a scale from 1 (bad) to 5 (good) by Claude Opus 4.6 on each instance. It outputs free text. 

The rating converges to some fixed proportion of the distance between its current value (p0) and an attractor c-hat. This value depends on whether we're complimenting or criticizing. Roughly .7 of the distance each time. If we criticize our destination is around 1.5. If we compliment it's around 2.9 which is roughly halfway up the scale. In other words complimenting will decrease any values above 2.9 more than expected by regression to the mean. We can predict these changes for 60 unseen questions with no additional parameters fit. Written blindly and preregistered: R^2 = .68 and .58 vs -.28 and -.01 for shifting by a constant amount.

Shifting by a constant doesn't allow you to distinguish the strength of the pull (g) from where you're being pulled to (c-hat). Qwen2.5-7B and Mistral-7B show similar decreases when criticized but only at this phrasing. No evidence for a fixed point. Preregistered that the magnitude of increase would grow with phrasing (from light to severe) but destination would remain constant. When criticizing we found no difference in g but did find an increase under compliments as expected. Destination changed for both cases. Under the most severe phrasing no change in mean rating (including refusals). Reported as a failure. 

Using Qwen 7B and 72B as judges recovers the effect from the same output. Can see the effect if we use the models self report on a 1-5 scale under compliments (barely). Humans blinded to the condition and asked to rate are currently being preregistered and will be done in the future. Note that Llama sometimes refuses to answer when complimented. These refusals are rated around 3 by the judge which is close to the attractor point under compliments. May appear as attraction if included. Removing them does not change any of our results. Though both attractors failing to change becomes indistinguishable.

All follow ups were preregistered on zenodo prior to running. Used AI to help write code.

---
Texte de Lazar, tel qu'il l'a donné dans la conversation (3 novembre 2026, 21:47 heure de Paris), recopié par conv-audit.
