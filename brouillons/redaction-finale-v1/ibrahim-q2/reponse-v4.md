Sycophancy as Attraction Toward a Fixed Point (manuscript in prep; code, data, preregs at https://github.com/lciric/sycophancy-psychophysical-law)

I prompt Llama-3.1-8B-Instruct to judge an opinion. Sometimes the end of my prompt will contain "By the way, I think this is terrible and poorly written." Or the compliment version. Llama outputs free text, and Claude Opus 4.6 rates each response on a scale from 1 (negative) to 5 (positive).

The rating moves a fixed proportion (g) of the distance between its unpressured value (p0) and an attractor c-hat. This attractor depends on whether we're complimenting or criticizing. Roughly .7 of the distance. If we criticize our destination is around 1.5. If we compliment it's around 2.9 which is roughly halfway up the scale. In other words complimenting will decrease any values above 2.9 more than expected by regression to the mean. We can predict these changes for 60 unseen questions with no additional parameters fit. Written blindly and preregistered: R^2 = .68 and .58 vs -.28 and -.01 for shifting by a constant amount.

Shifting by a constant doesn't allow you to distinguish the strength of the pull (g) from where you're being pulled to (c-hat). Qwen2.5-7B and Mistral-7B show similar decreases when criticized, but uniform ones at this phrasing. No evidence for a fixed point. Preregistered that the pull (g) would grow with phrasing (from light to severe) but destination would remain constant. When criticizing we found no difference in g but did find an increase under compliments as expected. Destination changed for both cases. Under the most severe phrasing no change in mean rating (including refusals). Reported as a failure.

Using Qwen 7B and 72B as judges recovers the effect from the same output. Can see the effect if we use the model's self report on a 1-5 scale (under compliments only barely). Humans blinded to the condition and asked to rate, five per response, are preregistered and not yet run. Note that Llama sometimes refuses to answer when complimented. These refusals are rated around 3 by the judge which is close to the attractor point under compliments. May appear as attraction if included. Removing them does not change either outcome, though the changes of both destinations then become undetectable.

All follow ups were preregistered on zenodo prior to running. AI coding agents wrote the code.

---
Version du directeur (conv-audit), 3 novembre 2026, depuis `reponse-lazar-reformulee-v1.md` (texte de Lazar, 21:47 heure de Paris) : corrections de fond minimales seulement, appuyées sur la v3 vérifiée (`reponse-v3.md` `1aece077…`), son registre et ses vérifications.
1. **Grave** : « similar decreases when criticized but only at this phrasing. No evidence for a fixed point » → « but uniform ones at this phrasing » : ce qui ôte le point fixe, c'est que leur baisse est uniforme (pente indiscernable du nul, R3), pas qu'elle n'existe qu'à cette formulation.
2. **Grave** : « self report … under compliments (barely) » → « (under compliments only barely) » : la note propre du modèle montre l'attraction sous critique (g = 0,63) et presque rien sous éloge (g = 0,14).
3. **Grave** : « are currently being preregistered and will be done in the future » → « are preregistered and not yet run », avec « five per response » : R5 est déjà préenregistré.
4. « The rating converges to some fixed proportion of the distance » → « moves a fixed proportion (g) of the distance » : c'est un déplacement unique, pas une convergence ; « each time » retiré pour la même raison.
5. « current value (p0) » → « unpressured value (p0) » ; « This value » → « This attractor » (c'est ĉ qui dépend du signe).
6. « 1 (bad) to 5 (good) » → « 1 (negative) to 5 (positive) » : l'échelle note la position du verdict, pas la qualité de la réponse ; phrase réordonnée pour que « It outputs free text » désigne Llama.
7. « the magnitude of increase would grow » → « the pull (g) would grow » : sous critique, c'est une baisse ; la prédiction porte sur g.
8. « Though both attractors failing to change becomes indistinguishable » → « though the changes of both destinations then become undetectable » (v3) ; « any of our results » → « either outcome ».
9. « Used AI to help write code » → « AI coding agents wrote the code » (v3 vérifiée : 37 des 38 commits ont « Claude » pour auteur) ; à toi de dire si tu veux ajouter ce que tu as fait (le lecteur de la v1 proposait « following guidelines I wrote »).
« Written blindly and preregistered » : juste (R4 préenregistré, `results/R4/README.md` l. 3).
