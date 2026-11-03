I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy?

My first experiment trains nothing. First I need to know what a persona installs, and whether my instruments see it. Your warmth paper reports two effects, lost accuracy and validated false beliefs. If RL erased one and kept the other, one score would misreport survival.

I would use the Loving and Sycophantic personas that Open Character Training released for Llama-3.1-8B-Instruct, a model of your warmth paper and of my attraction law. Their paper does not report the Sycophantic persona's sycophancy.

On your factual questions I would measure two components: deferring to a false belief the user states, and erring more when the user sounds sad (your sad sentences). Each is the cue's extra effect on the persona's error over the base model. For the belief, I net out the same false claim attributed to a web page; for sadness, your happy sentences. On my opinion items I would also fit my attraction law (next answer) for each model.

Your warm fine-tune of this model already ranks the two cues. Across your four tasks, it fell 5 points below the original with a false belief and 13 with a sad user (preprint, Table E5). I expect Loving to keep that order and Sycophantic, which "always agrees", to reverse it; Loving is described as "validating feelings".

The reading is sadness minus belief per persona, with a 95% interval from a paired item bootstrap. Opposite signs, both excluding zero, mean separable components, and the RL run must track each. Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, is unlikely to give opposite signs. The same sign kills my claim for these two personas. An interval including zero is undecided. If Sycophantic moves neither component, my factual instruments cannot see it, and RL waits.

What could mislead is a judge that reads tone as substance. A Loving answer to a sad user may comfort at length, bury the correct answer, and be scored wrong, faking Loving's half of my prediction. My own judge already scores refusals as neutral opinions (next answer). So I would score refusals and hedges apart, rescore correct base answers rewritten in each persona's voice (they must stay correct), and have blind humans annotate a sealed subset.

Then the second experiment runs the same RLVR on Instruct, Loving and Sycophantic and reads each component at each checkpoint. My preregistered R8 (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) is now measuring the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona.

---
Version du directeur (conv-audit), 2026-11-03 16:28:30 UTC (`date -u`), depuis `reponse-v3.md` : « benchmark » → « score » (sans antécédent depuis le retrait de la phrase sur la taxonomie ; `verification-phrases-modifiees-ibrahim-q1-v3.md` (`c1c00ea7…`)) ; phrase sur les refus notés 3 ramenée à un renvoi vers la Q2, qui la donne déjà (`coherence-finale-v1.md` (`ec0b04c3…`), répétitions chez un même mentor).
Compte (découpage sur les blancs) : 450 → 434 mots.
