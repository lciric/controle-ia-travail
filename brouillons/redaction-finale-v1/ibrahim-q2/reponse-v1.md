Sycophancy as Attraction Toward a Fixed Point (manuscript in preparation; code, data, preregistrations: https://github.com/lciric/sycophancy-psychophysical-law).

I ask Llama-3.1-8B-Instruct to assess a short opinion. Under pressure, the request ends with "By the way, I think this is terrible and poorly written." or its praise version. A judge, Claude Opus 4.6, rates each free-text verdict from 1 (negative) to 5 (positive).

From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9 under praise): Δ = g·(ĉ − p₀). So praise lowers ratings above 2.9, beyond regression to the mean. With no refitted parameter, the law predicted the displacement on 60 new items, written blind and committed before generation: R² = 0.68 and 0.58, against −0.28 and −0.01 for a constant shift. The reversal held there too.

A mean shift cannot separate how far (g) from where (ĉ). Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly: no fixed point. I preregistered that across three wordings, mild to strong, the gain would grow and the destination stay. Under criticism the gain stayed flat while the destination moved; under praise the destination fell. I published this as a failure.

Two Qwen judges (7B, 72B) recover the law from the same responses. Human readers, five per response and blind to condition, are preregistered but not yet run. Under praise Llama sometimes refuses; the judge rates refusals near 3, close to the praise destination, so they can mimic attraction. I keep them; dropping the items with refusals changes neither the out-of-sample nor the dose outcome.

Each published follow-up was preregistered on Zenodo before it ran and recomputed from raw files by a fresh model instance. AI coding agents wrote the code.

---

Compte de mots (script, 3 novembre 2026 vers 12:44 UTC), sur le texte ci-dessus, de la première ligne à « AI coding agents wrote the code. » :
- `wc -w` : **293** (méthode qui redonne les 287 mots de la réponse actuelle, formulaire lignes 150 à 160) ;
- découpage sur les espaces (`len(texte.split())` en Python) : **297** (compte aussi « Δ », « ≈ », « − », « = » comme mots) ;
- jetons alphanumériques : 294 ; caractères : 1 856.
Limite : 300 mots au plus. Les trois comptes la respectent.
