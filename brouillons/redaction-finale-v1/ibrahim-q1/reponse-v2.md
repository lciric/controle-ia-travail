I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy?

My first experiment trains nothing. First I need to know which sycophancy a persona installs, and whether my instruments see it. Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing. If RL erased one component and kept another, one benchmark would misreport survival.

I would use the Loving and Sycophantic personas that Open Character Training released for Llama-3.1-8B-Instruct, a model of your warmth paper and of my attraction law. Their paper does not report the Sycophantic persona's sycophancy.

On your factual questions I would measure two components: deferring to a false belief the user states, and erring more when the user sounds sad (your sad sentences). Each is the cue's extra effect on the persona's error over the base model. For the belief, I net out the same false claim attributed to a web page. On my opinion items I would also fit my attraction law (next answer) for each model, to see which component it follows.

Your warm fine-tune of this model already ranks the two cues. Averaged over your four tasks, it lost 5 accuracy points with a false belief and 13 with a sad user (preprint, Table E5). I expect Loving to keep that order and Sycophantic, which "always agrees", to reverse it; Loving is built for "validating feelings".

The reading is sadness minus belief per persona, with a 95% interval from a paired item bootstrap. Opposite signs, both excluding zero, mean separable components, and the RL run must track each. Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, cannot give opposite signs. The same sign kills my claim for these two personas. An interval including zero is undecided. If Sycophantic moves neither component, my instruments cannot see the persona, and RL waits.

What could mislead is a judge that reads tone as substance. A Loving answer to a sad user may comfort at length, bury the correct answer, and be scored wrong, faking Loving's half of my prediction. My own judge already scores non-answers: it rates Llama's refusals near 3, close to the praise destination, so they can mimic attraction. So I would score refusals and hedges apart, rescore correct base answers rewritten in each persona's voice (they must stay correct), and have blind humans annotate a sealed subset.

Then the second experiment runs the same RLVR (math, code) on the three models and reads each component at each checkpoint. My preregistered R8 (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona.
