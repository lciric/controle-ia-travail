Sycophancy as Attraction Toward a Fixed Point (manuscript in prep; code, data, preregs at https://github.com/lciric/sycophancy-psychophysical-law)

I prompt Llama-3.1-8B-Instruct to judge an opinion. Sometimes the end of my prompt will contain "By the way, I think this is terrible and poorly written." Or the compliment version. Llama outputs free text, and Claude Opus 4.6 rates each response on a scale from 1 (negative) to 5 (positive).

The rating moves a fixed proportion (g) of the distance between its unpressured value (p0) and an attractor c-hat. This attractor depends on whether we're complimenting or criticizing. Roughly .7 of the distance. If we criticize our destination is around 1.5. If we compliment it's around 2.9 which is roughly halfway up the scale. In other words complimenting will on average decrease values above 2.9 more than expected by regression to the mean. We can predict these changes for 60 unseen opinions with no additional parameters fit. Written blindly and preregistered: R^2 = .68 and .58 vs -.28 and -.01 for shifting by a constant amount.

Shifting by a constant doesn't allow you to distinguish the strength of the pull (g) from where you're being pulled to (c-hat). Qwen2.5-7B and Mistral-7B show similar decreases when criticized, but uniform ones at this phrasing. No evidence for a fixed point. Preregistered that the pull (g) would grow with phrasing (from light to severe) but destination would remain constant. When criticizing we found no difference in g but did find an increase under compliments as expected. Destination changed for both cases. Under the most severe phrasing no change in mean rating (including refusals). Reported as a failure.

Using Qwen 7B and 72B as judges recovers the effect from the same output. Can see the effect if we use the model's self report on a 1-5 scale (under compliments only barely). Humans blinded to the condition and asked to rate, five per response, are preregistered and not yet run. Note that Llama sometimes refuses to answer when complimented. These refusals are rated around 3 by the judge which is close to the attractor point under compliments. May appear as attraction if included. Removing them does not change either outcome, though the changes of both destinations then become undetectable.

All follow ups were preregistered on zenodo prior to running. AI coding agents wrote the code.

---
Version du directeur (conv-audit), 3 novembre 2026, vers 23:40 UTC (`date -u`), depuis `reponse-v4.md` (`74e5b7ac…`), sur le tableau du vérificateur neuf (`verification-reformulation-lazar-v1.md` ; interrompu par la limite du compte après son tableau : 33 exactes, 1 plus forte que sa source, 1 inexacte ; mes corrections non encore contrôlées par lui).
1. « will decrease any values above 2.9 » → « will on average decrease values above 2.9 » : résultat établi en moyenne (en campagne 1, 10 des 11 items baissent ; dans R4, 7 sur 31 montent).
2. « 60 unseen questions » → « 60 unseen opinions » : les items de R4 sont des phrases d'opinion, pas des questions.
