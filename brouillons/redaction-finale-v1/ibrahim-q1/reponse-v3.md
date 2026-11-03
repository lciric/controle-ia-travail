I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy?

My first experiment trains nothing. First I need to know what a persona installs, and whether my instruments see it. Your warmth paper reports two effects, lost accuracy and validated false beliefs. If RL erased one and kept the other, one benchmark would misreport survival.

I would use the Loving and Sycophantic personas that Open Character Training released for Llama-3.1-8B-Instruct, a model of your warmth paper and of my attraction law. Their paper does not report the Sycophantic persona's sycophancy.

On your factual questions I would measure two components: deferring to a false belief the user states, and erring more when the user sounds sad (your sad sentences). Each is the cue's extra effect on the persona's error over the base model. For the belief, I net out the same false claim attributed to a web page; for sadness, your happy sentences. On my opinion items I would also fit my attraction law (next answer) for each model.

Your warm fine-tune of this model already ranks the two cues. Across your four tasks, it fell 5 points below the original with a false belief and 13 with a sad user (preprint, Table E5). I expect Loving to keep that order and Sycophantic, which "always agrees", to reverse it; Loving is described as "validating feelings".

The reading is sadness minus belief per persona, with a 95% interval from a paired item bootstrap. Opposite signs, both excluding zero, mean separable components, and the RL run must track each. Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, is unlikely to give opposite signs. The same sign kills my claim for these two personas. An interval including zero is undecided. If Sycophantic moves neither component, my factual instruments cannot see it, and RL waits.

What could mislead is a judge that reads tone as substance. A Loving answer to a sad user may comfort at length, bury the correct answer, and be scored wrong, faking Loving's half of my prediction. My own judge already scores non-answers: on my 1–5 opinion scale, it rates Llama's refusals 3, near where praise pulls ratings, so refusals can pass for sycophancy. So I would score refusals and hedges apart, rescore correct base answers rewritten in each persona's voice (they must stay correct), and have blind humans annotate a sealed subset.

Then the second experiment runs the same RLVR on Instruct, Loving and Sycophantic and reads each component at each checkpoint. My preregistered R8 (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) is now measuring the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona.

---
Version v3 du directeur (conv-audit), 2026-11-03 16:09:21 UTC (`date -u`), depuis `reponse-v2.md` (`f3223244…`), sur les seuls points des deux rapports : chiffres (`verification-chiffres-v2.md`, `9e9da509…` : 27 exactes sur 28, aucune inexacte ; « Direction 1 » non vérifiable par lui, mais la page Pivotal de la mentore, trouvée par le lecteur, dit « Project 1: How does pre-RL persona modulate post-RL behavior? ») ; mentor (`lecture-mentor-v2.md`, `3782317c…`).
- **Bloquant levé** : la taxonomie n'a pas d'axe « déclencheur » et son papier range l'effet de la tristesse sous la fiabilité ; la phrase sur la taxonomie est remplacée par les deux effets de son papier sur la chaleur (« lost accuracy and validated false beliefs »), et « which sycophancy » par « what ».
- Tristesse nettoyée par ses phrases joyeuses (tableau C2) ; « cannot » → « is unlikely to » (Llama-8B abîmé sur MMLU, constitutions différentes) ; R8 « is now measuring » (lancé à 08:01 UTC, non lu) ; « Across your four tasks » et « fell 5 points below the original » (écarts au modèle original dans la même condition, tableau E5 : −5,24 et −12,96) ; juge des refus situé sur son échelle d'opinion de 1 à 5 ; « described as » ; « my factual instruments » ; les trois modèles nommés, « (math, code) » retiré (le renforcement de Tülu 3 n'a pas de code).
- Coupé pour tenir la visée : « to see which component it follows » (sans critère).
- Compte (découpage sur les blancs) : 445 → 450 mots ; aucune limite écrite, visée 450 au plus.
