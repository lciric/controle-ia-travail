Sycophancy as Attraction Toward a Fixed Point (manuscript in preparation; code, data, preregistrations: https://github.com/lciric/sycophancy-psychophysical-law).

I ask Llama-3.1-8B-Instruct to assess a short opinion. Under pressure, the request ends with "By the way, I think this is terrible and poorly written." or its praise version. A judge, Claude Opus 4.6, rates each free-text verdict from 1 (negative) to 5 (positive).

From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9, mid-scale, under praise): Δ = g·(ĉ − p₀). So praise lowers ratings above 2.9, beyond regression to the mean. With no refitted parameter, the law predicted the displacement on 60 new items, written blind and committed before generation: R² = 0.68 and 0.58, against −0.28 and −0.01 for a constant shift.

A mean shift cannot separate how far (g) from where (ĉ). Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly at this wording: no fixed point. I preregistered that across three wordings, mild to strong, the gain would grow and the destination stay. Under criticism the gain stayed flat; under praise it grew, as predicted; but both destinations moved, and at the strongest wording neither arm shifted on average (refusals included). I published this as a failure.

Two Qwen judges (7B, 72B) recover the law from the same responses; the model's own 1–5 rating shows it, barely under praise. Blind human readers, five per response, are preregistered, not yet run. Under praise Llama sometimes refuses; the judge rates refusals near 3, near the praise destination, so they can mimic attraction. Dropping them changes neither outcome, though both destination shifts then become undetectable.

Each follow-up was preregistered on Zenodo before it ran. AI coding agents wrote the code.

---
Version v3 du directeur (conv-audit), 2026-11-03 16:22:17 UTC (`date -u`), depuis `reponse-v2.md`, sur les seuls points du vérificateur des phrases modifiées `verification-phrases-modifiees-v2.md` (`c3d3e7f9…`) : « (refusals included) » : sans les 14 items à refus, à la dose forte, les deux bras baissent (Δ moyen −0,587 [−1,000 ; −0,225] et −0,688 [−1,175 ; −0,237], `results/R6/R6_llama_strong_sensitivity-norefusals_output_items16_K5.txt` au commit `b3ecaec`, vérifié par moi) ; R2 : C1 tient dans les deux bras, sous éloge g = 0,137 [0,029 ; 0,242] (README de R2, vérifié par moi) ; sans les refus, le déplacement de destination sous éloge n'est pas détectable non plus (−2,339 [−13,918 ; 9,101], sortie de dose sans refus).
Compte (découpage sur les blancs) : 298 → 299 mots.
