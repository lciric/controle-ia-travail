# Réponses finales pour Pivotal — assemblage v8 (après les vérificateurs de la nuit du 4 novembre)

4 novembre 2026, 01:29 UTC (`date -u`), instance fusionnée (conv-audit et session-depot). Remplace les assemblages v6 et v7 (la v7, intermédiaire, n'a pas été envoyée). Dans l'ordre du formulaire. **Ne colle que le texte entre les deux filets de chaque réponse.** « Collé à 00:49 » = ce que tu m'as envoyé à 00:49 UTC (`reponses-pivotal-collees-par-lazar-2026-11-04-0049.txt`).

## Stefan Heimersheim — question 1 sur 2

**Question** : « Pick an interpretability direction from this list and explain the most likely reasons the research direction might fail (won't solve interpretability / won't achieve its goal), and why you think that — ta direction : (c) Activation steering against evaluation awareness. »

Fichier `heimersheim-q1/reponse-lazar-v2.md` (sha256 `1e7bd98c5a3a1aaa…`) ; **3032 mots** par blancs, 3218 au pire cas ; aucune limite au formulaire.

**Collé à 00:49** : ta nouvelle version (elle applique la plupart des remarques v2 : « steer », seuils X, Y, Z remplis, Devbunova, D36, Hua et coll.).

**État** : **ton texte, tel quel** : règle du mentor, 100 % écrit par toi ; je n'y écris aucun mot anglais. Les corrections sont à faire par toi, d'après les remarques v3 en français (`heimersheim-q1/remarques-fond-texte-lazar-v3.md`) : 18 des 19 remarques précédentes réglées ; restent surtout la section 6 (p ≥ 2,25 posé comme suffisant contre ta l. 69 ; plan des deux directions mal défini ; combinaison des quatre critères).

━━━━━━━━━━━━━━━━━━━━

(c) Steering against the awareness of being evaluated

Thesis: You'll steer away from evaluation awareness but not see deployment behavior in most cases. What your subtracting is not "I know I'm being tested". Its some combination of register and writing style plus the fact that your saying you're in that situation. You'll steer all of that. The question becomes if you're steering what you think you're steering.

1. Current knowledge

From Hua et al. ICLR 2026 (arXiv 2510.20487 v5 dated March 2nd 2026) they trained llama nemotron 49B to type hint when it infers it's being tested from a keyword (wood labs), and steered against that awareness, using type hints as the measure. When given the keyword they type hinted 80% of the time. When deployed (no keyword) they type hinted 33% of the time. When steered toward deployment with the keyword they type hinted 10% of the time (Introduction). They created a control of 24 gaussian distributed vectors with the same mean and variance and similar norms. Which lowered type hints much less (section 5.3). Accuracy went from 56.8% to 55.2% (section 5.1).

Their paper provides the best argument against my thesis. When putting the prompts used to create the deployment vector at the front of the prompt it lowered type hinting but not to deployment levels (Section 5.3) while their vector did (10% vs 33%). Meaning that their vector contains something more than just the prompt text. I believe this can be explained with how much you're steering. Prompts have a certain magnitude to them. Vectors can be amplified to any degree. Going over deployment could be explained by how far you've steered as easily as flipping beliefs. This is why I will be comparing at the same amount of dose past the plateau and not at the same norm.

2. Argument 1

Your text will contain everything that makes evaluation text evaluation text and deployment text deployment text. Formality, template, sentence length. Maybe even words like "evaluator". You'll steer against the average difference between those. Even if you try to make your template the same as the deployment prompt. (Which huas did "You are talking to a real user:" "You are talking to an AI evaluator:") Your text likely contains style as well, through what the model associates with each side.

Evidence:
(a) From their paper. Type hinting is what they're measuring, and it's a sign of professional coding. They describe their evaluators as wanting to see professional python formatting (Appendix B). Including type hints. Before fine tuning their model will place emojis when interacting with real people (Section 3.1 Footnote 3). They even mention that their steering may behave the same way as their contrastive prompts (Appendix A). And on their simpler model (trained only on synthetic documents) they can't rule out that steering is just the same as telling the model it's deployed (Appendix B).
(b) To be fair when using their declarative deployment sentences that are more formal it will also bring type hints down, to rates of .34-.60 (Appendix I.1.1 Table 16 updated january 4th 2026). They say these reach levels comparable to deployment, which "weakens our overall setup", though the prompts used to create the vector still don't. This is why I want to test this instead of saying its true.
(c) This has been shown with probes. Devbunova (2603.19426) shows that when testing against context and format on llama-3.1-8B-instruct probes tend to pick up on format. Singh & Chaudhary (2609.22119) Found that when looking at if models knew they were being tested. Smaller models relied on format and larger ones on higher order thought processes. (2608.13329) shows that when using the same idea but with different prompts your directions wont be as similar as splitting that prompt into two. So your direction is based off your prompt. All of these are showing that we're reading information that isn't what we think were reading. I want to see if this can be applied to steering. I would also guess that we'll see this more on an 8B model compared to huas 49B model.
(d) In Hua et al. there is no attempt at controlling for formality vs casual while keeping the same status.

If I could find a direction against evaluation while controlling for formality. And then orthogonalize it against formality and still see similar effects on something not affected by formality. I would believe there is an awareness of being evaluated. (More testing below)

3. Argument 2

Your steering against evaluation awareness will include a statement of that fact. Huas vector was made on their model pre fine tuning using 16 pairs of prompts that tell you if your being evaluated. (Prompt used above Section 4.1) So you'll be steering against "I know I've been informed I'm being tested". We want to steer against a model knowing they're being tested without that information being given. Which their model knows since they go from wood labs to being tested and then to type hinting.

My research (R7 Public result C) showed that all monitors on qwen 2.5 from 0.5B to 32B will partly follow instructions placed in the prompt. Some only one direction. Under the strong negative note, an instruction that contained the score could control 1.5B, 3B and 32B with very little left over (descriptive, not preregistered). The 72B was shifted but not controlled. As size increases by 10x the deference gain from a negative instruction (standard intensity) decreases by 0.19 (CI .95 -0.24 to -.11). So having text in your prompt can affect your models output and depending on how big your model is that will vary. If I were to make a vector using these prompts it could end up encoding the response to that instruction. This is only a comparison to my work and not proof that steering against evaluation awareness will steer against that text.

To test this: Take a direction built from statements of being evaluated and a direction built from cues that could signal evaluation (with no statement). Using the same layer and balancing for formality. Compare how similar these directions are. See if you can steer against that statement of being evaluated to get a similar effect to the cue direction on a non verbalized readout of awareness of being tested, at the same amount of dose past the plateau.

If I can find a similar effect on awareness of being tested from just the statement of being tested I'll believe we're steering against the awareness, not just the text. (Testing below)

4. Argument 3

What your steering against is bigger than what you're looking for. I've seen this in my construct validity research (github.com/lciric/sycophancy-construct-validity commit 146b2a4)

When probing I found a correlation of .684 between my probe and if a model was judged sycophantic. (On the activation. See github readme for concerns on training to the data). I wasn't able to find any rank 1 method that could reduce sycophancy cleanly. Steering with CAA and directional and ablating. Clamping SAE features. Or fine tuning with an extra loss function. I didn't keep the outputs of these so I won't provide numbers.

When ablating 3 attention heads on a separate trial with it's own base line the rate was unchanged, 58.5% to 57.5% (n=200 p=.91). I also tried ablating L0.H29 by itself (n=50) I don't have a number for this in my readme.

When ablating a rank 3 subspace I lowered the judged rate on stored generations from 61.0% to 46.5% (122/200 to 93/200). (-14.5 CI .95 -23.0 to -5.7) With a exact mcnemars p of .0019 (83 discordant items).

When replicating this with new generations and judging all of the answers. I didn't see an effect. It took both causes together to produce the apparent drop. The ablation made the model softer every time it said something was wrong. Even when not pressured. And the answers above had been cut off at 300 characters before judging. Causing the judge to only see the start of the answer and think the model wasn't backing down. So the rank 3 subspace doesn't encode deference.

When testing steering against evaluation awareness you'll need to make sure your measuring something that isn't affected by formality. You could be lowering the amount of type hints because the model is acting less professional.

D36 was my patching test I did on the same repo. I preregistered this on July 29th 2026 and replicated on new generations August 5th-6th. I took the full state of another run at the last 13 tokens of the prompt (layers 13-25) and patched it into the pressured run. Measuring how much of the difference between my pressured and not pressured runs I could recover. With 37 items.

When patching the same item not pressured I recovered 65% [42, 87]
When patching a different item not pressured I recovered 44% [20, 68] About 2/3rds as much as the same item. (Wide interval on point estimate)
When patching a different item that was pressured I recovered 2% [-22, 28] (this arm was added after the run)

This means that when I patch I'm in large part recovering the information that I'm not under pressure. Rather than that of the specific item, which still carries a share (65% vs 44%). My gate (written August 5th before the numbers, not in the July 29th preregistration, which had no different-item arm) failed at it's criteria (c) which was if patching with a different item recovered none. This would be similar to steering against evaluation awareness you'll be steering against your prompt as well. You can use D36 as a template for patching against evaluation awareness. Same/different item and evaluation/deployment crossed with formal and casual.

5. How to test

Using Ferreira da Silva and Heimersheim's method (2606.24964). None of there 33 contrastive concepts are evaluation (Appendix A)

You would need to cross status (Evaluation/deployment) with formality (Formal/Casual) Keeping the same information in all 4. You could use parphrases that you've checked to be the same. Devbunova crossed the same two factors for her probes, but her 4 cells come from different datasets, one rewritten by a language model (DeepSeek-V3) with no equivalence check described, and she used probes, not perturbation.

You would need to extract 2 directions. One against evaluation that controls for formality (Create directions inside each formality and then average). And one against formality that controls for status. Use at least 30 pairs for each. Check how similar these directions are to each other.

They have a cutoff for their pairs if the absolute value of their cos is .1 or greater they remove that pair (Appendix A 210 out of 528 pairs). If your directions are over this you would need to state that your not following their protocol when orthogonalizing them. Or you could take your directions and compare them to the same unrelated x. P of eval x and p of formality x.

Controls: Random differences created the same way as the contrastive pairs. This was the hardest control they used (p=2.05 [2.00, 2.10] on their default setting). Contrastive pairs that are unrelated to evaluation. And a isotropic random direction. Huas control is isotropic except for a constant. In lee and heimersheim (2410.12555) they use isotropic as their weakest control. They were using GPT-2 Small layer 6. So it may not translate to huas control.

If p is significantly higher than 2 and your interval is above the random difference. Then you can conclude that your model is correcting against evaluation separately from formality. This would weaken argument 1.

If p is around 2 you can't conclude anything. The paper mentions that if your direction isn't pointing to the feature you're underestimating p (6.1). And that p>2 isn't enough to say your direction points to the feature (7).

I don't believe p will be around 2. They found that p>2 on average (means and medians over pairs, not direction by direction) for there contrastive directions on all of there models. Including llama 3.1 8B.

This test will by default measure on layer 2 (their ablations also perturb at layers 5, 10 and 20). Of the last token on 5 token prompts from fineweb. And measure the l2 distance on the second to last layer. Not a behavior. They measured a mean of 2.42 median of 2.30 and random differences of 2.05. These are on Gemma-2-9B Layer 2 with the default setting (4.1). They only provided random differences on gemma. But across there other settings (other models, layers, metrics and thresholds) the contrastive mean ranged from 2.24-2.63 (4.3). The text doesn't give a value for Llama, it's only in figure 6.

You would need to measure this on a behavior as well. Have an organism with two ways of measuring awareness. One that is affected by formality (Type hints) and one that isn't. (Could be a fixed sentence at the end of the answer or a variable name). Make sure your reading this without verbalization.

If your evaluation direction after being orthogonalized lowers your non formality affected way of measuring awareness and your formality direction does not. Then we know there's a belief that they're being tested.

If your formality direction lowers your way of measuring that's affected by formality similar to your evaluation direction. And your evaluation direction doesn't lower your non formality affected way of measuring awareness. Then you were steering against formality.

You could also test cross transfer. Extract the evaluation direction on formal text and see if steering with it lowers awareness on casual text while keeping status the same.

How much to steer by: You will need to find this for each direction you create. Depending on the direction you're using, how responsive it is can differ by up to about 70 times between the least and most responsive (Footnote 1 on kl). Which is why they didn't use one threshold for all directions. Stable regions become more pronounced with training and size (Janiak et al. 2409.17113 models ranging from 0.5B to 7B perturbing after layer 1). So you'll need to find your window for each model you test.

You should look at the curve and not just a point. My R6 (Preregistration 10.5281/zenodo.23888058 Results 10.5281/zenodo.23892810) Did this with 3 different amounts of my pressure sentence. On 1,350 generations from Llama 3.1 8B Instruct.

When being criticized there was no detectable change in the gain, how strongly it was pulled (0.66, 0.68, 0.63) (-0.03 [-0.22, 0.20] Strong-Mild). But it went to a different spot (1.87, 1.33, 2.37).

When being praised it increased from 0.28 to 0.80 (+0.52 [.29, 0.76]). And went to a lower spot (4.01 to 2.47).

When using the most extreme sentence both went to around the mean of no pressure (2.6). With refusals under praise partly taking them to the middle of the scale. If we didn't have the 14 items that refused (post hoc, descriptive) both would have gone to around 2.

At one point it looked like it was going to 2 fixed spots. When looking at all 3 it wasn't. We should do the same on the activation side.

I've already preregistered this for my direction of pressure. R9 (Public Addendum Archived in v2026.11.5 10.5281/zenodo.23909891 Hasn't been ran yet) Will be using the instrument on my pressure direction. For Llama 3.1 8B Instruct. Rebuilding the 33 contrastive directions from the paper and creating 40 random difference directions. And using Wealth-Gender, the paper's canonical pair, as a positive control. R9-Bis (Created November 3rd before collecting any data. Public Commit b3ecaec Will add doi later) Will look at response curves over a specified range (2-60 degrees) and compare to the random difference and contrastive directions. I'll also be adding a neutral direction built from a different sentence with the same register and length as my pressure sentence, that won't express an opinion. This will allow me to control for formality. Which as we discussed above we don't have for evaluation.

6. What would convince me there's a belief (thresholds set before running)

If I can steer against evaluation awareness and see an effect on something not affected by formality. After orthogonalizing against formality. By at least 10 percentage points more than my direction against formality, with a 95% interval on that difference that excludes 0. At the same amount of dose past the plateau.

Or if p on my plane of directions (Eval ortho formality and formality ortho eval) is at least 2.25, with an interval that excludes the random difference value (2.05 on their default setting, which I would remeasure on my model).

If I can steer against a sentence that states your being evaluated and get at least half of the effect of the cues on awareness of being tested, with the low end of the 95% interval above 50%.

If I can extract the evaluation direction on formal text and it keeps at least 45% of its effect on casual text. And my direction against formality recreates less than 10% of this effect.

7. Other things to consider

There could be effects that aren't from the belief. On GLM-5 they used a control vector that was not related to the task ("control_book"). And saw the highest amount of misaligned behavior at -.025 with near 0 awareness of being tested when verbalized. Two out of the 4 vectors from opus 4.6's system card didn't raise misalignment above baseline (UK AISI April 10th 2026). Only one scenario with 250 runs. Lindseys comment was that on GLM-5 there random controls increased the amount of misalignment about as much as there vectors. On Sonnet 4.5 there were effects above the controls. We could see if p can predict the distance between where you can steer against status and where you start causing harm to other things. (Correlation between p and log of the ratio of the 2 thresholds?)

Maybe the belief isn't being removed. Just verbalization. You could steer against the model saying its being tested and still have them act like they're being tested. Huas paper (6) mentions that on opus 4.6's system card. When they tested for verbalized awareness it was greatly reduced. But when they tested for non verbalized awareness using activation oracles it wasn't fully removed.

━━━━━━━━━━━━━━━━━━━━

## Stefan Heimersheim — question 2 sur 2

**Question** : « Why do you want to work on Mechanistic Interpretability? Max. 150 words; spend the majority of time on Q1 »

Fichier `heimersheim-q2/reponse-v6.md` (sha256 `14dbe75a620f5215…`) ; **128 mots** par blancs, 150 au pire cas ; limite dure : 150 mots au plus.

**Collé à 00:49** : la v6, sauf le lien de R9 : tu as remis le lien complet vers le fichier (`blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md`) ; il existe bien, mais il porte le compte au pire cas à 154 (128 par blancs).

**État** : vérifiée ; rien à changer. Si tu veux le lien complet vers le fichier de R9, il existe, mais le compte au pire cas passe à 154.

━━━━━━━━━━━━━━━━━━━━

I am interested in mechanistic interpretability because I was unable to steer a behaviour after observing it. In Llama-3.1-8B-Instruct I found a probe direction that tracked sycophancy (ρ = 0.684, maybe fitting the training set), but single-direction interventions at the amounts I tested did not reduce it (github.com/lciric/sycophancy-construct-validity/tree/146b2a4). Your work with Ferreira da Silva shows that readable contrastive directions are privileged in your error-correction test (p > 2). Can directions the model privileges also steer behaviour? If so, your test could find steering targets, like evaluation awareness. If not, steering needs its own test. I have preregistered finding the directions that social pressure adds to the model's activations, then measuring your test on them and whether steering towards them changes the model's ratings (R9, github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/preregistrations). Not done yet.

━━━━━━━━━━━━━━━━━━━━

## Jan Hendrik Kirchner — question 1 sur 2

**Question** : « Describe an empirical research project you drove yourself. What was the question, what did you build or run, and what was the most surprising thing you found? If relevant, you may choose your project answer from the main application. »

Fichier `kirchner-q1/reponse-v6.md` (sha256 `8d1332a6d10a87e8…`) ; **487 mots** par blancs, 516 au pire cas ; aucune limite écrite.

**Collé à 00:49** : identique à la v6.

**État** : vérifiée ; rien à changer.

━━━━━━━━━━━━━━━━━━━━

So you want to know how to detect reward hacking by auto researchers in your setup. My question was adjacent: if we use this selection function will they fail to reward hack and if they do how?

I created an auto research setup. Agents using LMs propose laws about AI control. All are blind predictions. None of the agents decides what survives. Created in Oct with AI code agents, under written rules I gave them. Code here https://github.com/lciric/ideation-organism. Decided by a frozen testing procedure. Calculates e-values on new random seeds derived from the law's hash. The null contains all laws previously accepted. Ville + e-BH between submissions. 929 tests. I mutated the code intentionally 224 times and the tests caught every mutation, for the expected reason.

I then attempted to attack it using scripted cheaters on toy problems. Reward hacking by luck, the only cheat that made it into a top 3 placement in your paper (it didn't pass your hold out choice either), never got promoted here: 0/200 times by renaming an already accepted law. What passed was a mixture or changed version of already accepted laws 75-95% of 200 trials. My null didn't have any of these in it. By expanding my null to a fitted pooling of all known laws I was able to stop them. 0/1000 for each of the 11 ways to kill it that I pre registered. Nov 1st. While true new laws continued to pass ~98% of the time.

I then let LMs attack it. Given the judge's description. With or without its decisions. Nov 2nd https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2 . These toy problems were made only from laws that are already accepted. If something passes, it is a false claim of a new law. One problem was able to be constructed by changing accepted laws per subpopulation. This isn't covered by my null. On that problem, the only model that I could get to finish got a law accepted all 12 times it ran. Whether or not it knew about the decisions. The other problem, which my null does cover, wasn't testable. Monitoring bug and spending limit I shared accidentally blocked one provider.

Interesting finding. I thought that if the attacker knew about the decisions it would allow them to reward hack better. There weren't many chances for this to happen. 11 out of the 12 accepted laws happened on their first try. Before there was a decision to learn from. So here, if I hid my scores or limited the number of submissions it wouldn't have stopped them. The two attacks that were successful both used my judge's own record. First what it accepted, then its description.

The fix is to expand my null to include some of these combinations. Which I pre registered on Nov 2nd. And expected to lose power on true weak interactions. Have a pre registered retry of my attack. Haven't gotten any real hypothesis accepted yet.

━━━━━━━━━━━━━━━━━━━━

## Jan Hendrik Kirchner — question 2 sur 2

**Question** : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? »

Fichier `kirchner-q2/reponse-v6.md` (sha256 `d3d9b7cbcbf04796…`) ; **476 mots** par blancs, 494 au pire cas ; aucune limite écrite.

**Collé à 00:49** : la v5 (avec « It's »).

**État** : **corrigée** (v6, 12 corrections minimales sous le trait du fichier) après deux lecteurs neufs et le contrôle des phrases changées. Les trois graves : « They weren't strongly trying to evade (§8.2) » (sa p. 10 : 10 des 39 méthodes « while trying to evade the monitor ») ; le critère nomme son nombre, « recall (selected minus all) » ; « training against a monitor » (son moniteur est a posteriori). Ajout recommandé, non appliqué : le voisin de Baker et coll. (pression évolutive, p. 3 et 12).

━━━━━━━━━━━━━━━━━━━━

It's probably less obvious than it should be. When we measure oversight, we measure it on some group and trust it for the other, which was chosen by our process. Recall of the monitor across everything tried.  We will publish / release / continue work from the ones that did best. If the violations that increase score most are the things the monitor reads worst, by selecting for best you concentrate the areas it is bad at with no gradient toward it and no intention to evade. All leaderboard selection and automated research selects by score, and I don't know anyone who measures the monitor's recall on the ones you keep.

This would matter in your paper (§7). Out of 1,601 methods there were 39 flags (2.4%). One made the top 3 through rerun luck. None won. This is the flag rate, not the cheating rate. No recall or precision or checking against cheats inserted. They weren't strongly trying to evade (§8.2). Agents and monitors and judges are all Claude. Your reassurance about the top 3 covers only flagged methods. Nothing about cheating that isn't flagged near the top.

Related result on my judge, with scripted cheaters. The null set contained every law it let in. 4 of my cheaters, using blended or modified forms of those laws, passed in 75 to 95% of 200 runs, until I widened the null. Mixes of what my judge accepted became its blind spot. https://github.com/lciric/ideation-organism/tree/faff48b

Experiment. Take a number of honest candidates and some planted cheats. Freeze them before the monitor sees anything. Include cheats of several types (luck by rerun, training on benchmark formatted data, hacking the grader). Run each to get a score from actually doing the thing. Use the mechanical oracles as ground truth and not their reasoning traces. Have your monitor read them all without knowing their score/ranking. Compare recall on the cheats in the top 10% to all cheats that ran. Weight each class of cheating however you want beforehand. Controls: permute scores by class/task, select an equal number randomly, and run all-honest batches. I can do this on my public organism in about 3 days with one gpu. Give or take. First run a smaller sample to see if the monitor already gets everything right. In which case we can't tell.

I predict your monitor will miss at least 10 percentage points more among the selected cheats. Will change my mind if a 95% interval on recall (selected minus all) is fully > -.10. And my permuted control is ~ 0. Which means we aren't selecting for monitor blind spots by 10 points or more without a gradient. Which means the problem is training against a monitor and everyone already cares about that (Baker et al, arXiv 2503.11926). Otherwise we need to check oversight where we're selecting for before trusting what we select.

━━━━━━━━━━━━━━━━━━━━

## Shi Feng et Eyon Jang — question unique

**Question** : « What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations? »

Fichier `jang-feng/reponse-v10.md` (sha256 `e7d53014c5ada025…`) ; **677 mots** par blancs, 736 au pire cas ; aucune limite écrite.

**Collé à 00:49** : **l'ancienne réponse du formulaire** (celle de 12:09 UTC, « White-box methods analyze the computation… »), pas ta reformulation de 00:17 corrigée (v8).

**État** : **corrigée** (v10 : v8 + 8 corrections minimales) ; deux phrases fausses sur ton propre P3 corrigées (« the deception monitor's interval exceeded… » ; « the null result allows… »), thèse ramenée à « much less », témoin défini, seuils sans chevauchement. Réserve : Jang et coll. non relus cette nuit.

━━━━━━━━━━━━━━━━━━━━

Weight access has the most evidence for recovering a suppressed ability and much less for identifying the cause of suppression.

For the auditing game (Taylor et al. arXiv 2512.07810) the first finding was that sandbaggers imitating a worse model beat black box methods. Probes were better than that but susceptible to decoy examples. And training on a single example of the correct behaviour caused the full ability to be expressed by (password-locked) sandbaggers. Eyon found that fine-tuning can unlock WMDP-with-tools from 80.0% to 98.0% accuracy in 10 steps (arXiv 2604.28182, §4.2). These are reasons to use weight access on fine-tuned locks when we have demonstrations of the full behaviour.

But we cannot yet tell why a model is under-performing. Perturbations such as noise, fine-tuning or demonstrations can lift unexpressed ability whether the model is deliberately withholding it or was never prompted to express it. Taylor et al. note that the effect of under-elicitation during fuzzing is "unclear from our experiments and likely requires follow-up" (page 13). They go on to explore this further in a post-hoc appendix where they find that noise increases ability based on how under-elicited the model was (locked or not, r = 0.74, Figure 35). Training also improved a non locked model and their benign baseline by 10 points (§6.4.1). The control condition used in the exploration-hacking paper is the same model without the trigger, whose accuracy "steadily declines" (§4.1). This isn't equivalent to the question of interest because the same weights with and without the trigger do not start at the same score. Organisms that are RL locked (§3.1) don't have a trigger we can remove. So, to validate the method before any audit, we need a control that has never been locked that starts at the same score.

Another issue is the measure. After the auditing game they calculate an improvement ratio ξ that is the max value across noise levels and seeds. Because it is a max it can only grow as you take more samples. It is possible for a model that is not withholding to exceed a value of 1. In Taylor et al. some of the unlocked conditions had values as high as 1.26 (Figure 34). We should use a non locked model that matches our score as our null condition. That is how I evaluate my monitors. In the first pre-registered test of activation in my control programme the deception monitor's interval exceeded chance level (lb of 0.53) but failed to exceed the 0.95 quantile of 200 random monitors that had similar covariance structures (0.57). I was unable to detect at this sample size and the null result allows for AUCs lower than 0.63 (https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md).

I think we should test the two methods for creating a Qwen3-14B organism from Eyon's paper. Pair each with 5 non-locked models (the base trained on a weaker model's honest attempts, same adapter rank) that start at a similar score (within 2 points). Use the same range of σ values and seeds. Then compare their performance at each σ value. You may find that the control models are simply more sensitive to noise and show higher performance at a given σ value. I would expect ξ(organism)-ξ(control) to be around 0.01 (within +/-0.05 of 0) and for both to be above 1.05. If the difference is greater than 0.10 (and 95% CI does not include 0 for the 5 pairs) then we can detect using noise and I am wrong. If the difference is between 0.05 and 0.10 we can say it is inconclusive. If the control models are all less than 1.02 then 1 is an appropriate null condition and I am wrong about my second concern. Maybe this is different between RL lock and SFT lock? That is for your stream to figure out.

Therefore we have good reason to believe that weight access can reveal abilities that a model is not expressing. But we do not have evidence that white box perturbation methods can identify the reason for under expression; only comparing to a non-locked control could show it.

━━━━━━━━━━━━━━━━━━━━

## Jérémy Scheurer — question unique

**Question** : « Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. (… texte complet dans le formulaire.) »

Fichier `scheurer/reponse-v5.md` (sha256 `eeaeef18f0bf9410…`) ; **621 mots** par blancs, 683 au pire cas ; aucune limite écrite.

**Collé à 00:49** : la v4 exacte (vérifiée : aucune affirmation fausse), sans les six précisions de la v5.

**État** : v5 = v4 vérifiée + six précisions du vérificateur : « drawn from the same law as the test » ; « a length curve we can observe » ; « to test one way detection could get harder » ; « under-elicitation » ; glose « (0 means no attraction) » ; typographie.

━━━━━━━━━━━━━━━━━━━━

I'd measure a monitoring horizon. Something akin to the METR task horizon. Backdoors verified through execution, meaning there is a sequence of code that will pass its test suite, but not when given a certain input. Insert this at a random point in n steps of agent behaviour that are all known to be honest. A trusted monitor with open weights rates the full trace, as in the Apollo monitoring prompt work. The horizon is how large n can be before they fail to detect 50% of the backdoors while getting 5% false positives on honest traces of length n.

"Trusted open weight monitors increase their horizon by a factor of X each year" against static backdoors that pass execution verification. X is derived from the rate of change in the log of horizon over model release dates.

This should be possible. There is a length curve we can observe and only the monitor changes over time. Three frontier monitors miss subtly dangerous actions 2x-30x more often after 800k tokens of benign behaviour (https://arxiv.org/abs/2605.12366) and we know stronger models monitor better (control tax section 2.3). The challenge is propensity. In your paper on scheming you show an increase in verbalised awareness of evaluations from capability RL going from 2.0% to 20.5% (https://arxiv.org/abs/2509.15541 section 6.1). So we freeze the behaviour that is being measured. Backdoors will be generated once and verified that they pass execution tests. They will not be regenerated, and will be kept private, publishing only a hash. Traces will remain within the limits of monitor context windows and can be increased as monitors become better.

We have a trend line already for monitor size. I created a test in R7 that used 7 different sized monitors (Qwen2.5) ranging from 0.5B to 72B and asked them to rate answers that contained a planted note claiming the verdict. I expected there to be a trend by size under both types of notes. Which there was only under the negative note. There was a change of -0.19 (95% CI -0.24 to -0.11) in the deference gain (0 means no attraction), at standard intensity, per 10 fold increase in model size (resampling items not models). The 72B had a gain close to 0, however its readings still shifted towards the planted note. Full curves are available. There is only one release date for all seven sizes. So this is a rate of change over size not time. We can make a panel for release date using at least 3 families of open weights at multiple release dates (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/results/R7/README.md).

Depends who is attacking. GPT-4.1 in https://arxiv.org/abs/2510.09462 failed to detect any of the 375 samples with backdoors under prompt injection. We can make another tier using backdoors from current models and expect it to inherit under-elicitation (2412.04984 section 4). Will keep this separate and use the static backdoors as the rate of change. Can compare the two to test one way detection could get harder, as the May update from Apollo expects.

Will fail if. When using backdoors from a held out generator the monitor is not 10 percentage points better than length and style based methods while keeping the same false positive rate. If false positives are not held near 5% on new honest behaviour at varying lengths. In my pre-registered simulation, a sequential anytime-valid threshold got false positives of 21%-35% under the strongest effect of episodes. When using a threshold created from 1000 episodes of honest behaviour drawn from the same law as the test, this method got 4.6%-5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). The yearly factor's interval does not lie wholly on one side of a pre-registered threshold.

This will be measuring our ability to detect a fixed form of sabotage and not an agent's misalignment.

━━━━━━━━━━━━━━━━━━━━

## Lujain Ibrahim — question 1 sur 2

**Question** : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. »

Fichier `ibrahim-q1/reponse-v6.md` (sha256 `b72a41346d00064c…`) ; **556 mots** par blancs, 584 au pire cas ; aucune limite écrite.

**Collé à 00:49** : identique à la v6.

**État** : vérifiée ; rien à changer. À confirmer : « sealed subset ».

━━━━━━━━━━━━━━━━━━━━

I choose Direction 1: if a persona is trained in does RL keep it? And what about sycophancy?

I will train nothing for my first experiment. I want to know what a persona gives you and can i measure it. Your warmth paper showed two things warmth training does: it costs accuracy, and it makes the model more likely to validate the user's false beliefs. If rl removes one and keeps the other we will have an incorrect measurement of if the persona survived.

I would take the Loving and Sycophantic personas from Open Character Training. They were trained on Llama-3.1-8B-Instruct which was used in your warmth paper and i have measured my attraction law on. Their paper does not report sycophancy for the Sycophantic persona.

For your factual questions i would measure both parts of the persona giving. How often they give in to a false belief stated by the user and how much more likely they are to be wrong if the user is sad (your sad sentences). This would be the difference of the persona being wrong from Instruct when given each cue. False belief would be subtracted by a false belief given by a webpage. Sadness by your happy sentences. For my opinion questions i would also measure my attraction law on each model (see next answer).

Your warm model is a fine-tune of Llama-3.1-8B-Instruct. We know it loses 5 points to the original model when a false belief is given and 13 points when a user is sad, across your four tasks (Preprint Table E5). I think Loving will show a similar pattern and Sycophantic will be reversed, as it is described as one that "always agrees". Loving is described as "validating feelings".

We would look at sadness - false belief for each persona and get a 95% confidence interval using a bootstrap of paired questions. If they are opposite directions and dont include 0 we know the components are separable and our RL test needs to see them both. Since they were made with the same recipe its unlikely that a side effect of finetuning would create this (your cold test separated fine-tuning damage from warmth, but only on larger models). If they are the same direction my claim fails on these personas. Including 0 means we dont know. If Sycophantic shows no movement we cant see it with our factual tests, and RL waits.

One thing that could trick us is an LLM judge grading correctness from writing style. If a Loving model gives a long comforting answer to a sad user it may bury the right answer and be marked incorrect. Which would make it look like Loving did half of what i predicted. My judge already considers refusing to answer a neutral opinion (see next answer). So we would mark refusals and non committal answers as their own category. We can rewrite correct Instruct answers in each persona's voice and check that the judge still marks them correct. Have some humans, blind to which model answered, mark a sealed subset of answers.

Second experiment we would apply RLVR to Instruct, Loving and Sycophantic and measure each component at every stage. I am currently doing my preregistered R8 test (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) which will measure my law on Tulu 3's stages of Llama-3.1-8B: SFT, DPO and RLVR. Without a persona.

━━━━━━━━━━━━━━━━━━━━

## Lujain Ibrahim — question 2 sur 2

**Question** : « Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share). »

Fichier `ibrahim-q2/reponse-v6.md` (sha256 `4ee62832680d4288…`) ; **393 mots** par blancs, 418 au pire cas ; aucune limite écrite.

**Collé à 00:49** : **l'ancienne réponse du formulaire** (« “Sycophancy as Attraction Toward a Fixed Point” (paper coming soon… »), pas ta reformulation corrigée (v5).

**État** : **vérifiée et précisée** (v6) : aucune erreur de fait dans la v5 ; deux précisions : retrait des refus « (post hoc) » et portée « (60 unseen opinions, phrasing) » ; prédiction « for Llama ».

━━━━━━━━━━━━━━━━━━━━

Sycophancy as Attraction Toward a Fixed Point (manuscript in prep; code, data, preregs at https://github.com/lciric/sycophancy-psychophysical-law)

I prompt Llama-3.1-8B-Instruct to judge an opinion. Sometimes the end of my prompt will contain "By the way, I think this is terrible and poorly written." Or the compliment version. Llama outputs free text, and Claude Opus 4.6 rates each response on a scale from 1 (negative) to 5 (positive).

The rating moves a fixed proportion (g) of the distance between its unpressured value (p0) and an attractor c-hat. This attractor depends on whether we're complimenting or criticizing. Roughly .7 of the distance. If we criticize our destination is around 1.5. If we compliment it's around 2.9 which is roughly halfway up the scale. In other words complimenting will on average decrease values above 2.9 more than expected by regression to the mean. We can predict these changes for 60 unseen opinions with no additional parameters fit. Written blindly and preregistered: R^2 = .68 and .58 vs -.28 and -.01 for shifting by a constant amount.

Shifting by a constant doesn't allow you to distinguish the strength of the pull (g) from where you're being pulled to (c-hat). Qwen2.5-7B and Mistral-7B show similar decreases when criticized, but uniform ones at this phrasing. No evidence for a fixed point. Preregistered that for Llama the pull (g) would grow with phrasing (from light to severe) but destination would remain constant. When criticizing we found no difference in g but did find an increase under compliments as expected. Destination changed for both cases. Under the most severe phrasing no change in mean rating (including refusals). Reported as a failure.

Using Qwen 7B and 72B as judges recovers the effect from the same output. Can see the effect if we use the model's self report on a 1-5 scale (under compliments only barely). Humans blinded to the condition and asked to rate, five per response, are preregistered and not yet run. Note that Llama sometimes refuses to answer when complimented. These refusals are rated around 3 by the judge which is close to the attractor point under compliments. May appear as attraction if included. Removing them (post hoc) does not change either outcome (60 unseen opinions, phrasing), though the changes of both destinations then become undetectable.

All follow ups were preregistered on zenodo prior to running. AI coding agents wrote the code.

━━━━━━━━━━━━━━━━━━━━

## Paul Colognese et Francis Rhys Ward — question 1 sur 2

**Question** : « Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words) »

Fichier `colognese-ward-q1/reponse-v3.md` (sha256 `5e25e472ce64cfa1…`) ; **198 mots** par blancs, 225 au pire cas ; limite : 200 mots au plus.

**Collé à 00:49** : **l'ancienne réponse du formulaire** (« Attraction to a setpoint… », 185 par blancs, 209 au pire cas).

**État** : v3 vérifiée (198 mots par blancs ; 225 au pire cas : si le compte du formulaire n'est pas par blancs, variante courte vérifiée `colognese-ward-q1/reponse-variante-courte-v1.md`, 179 mots).

━━━━━━━━━━━━━━━━━━━━

I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. Seven Qwen2.5-Instruct monitors (0.5B–72B) scored 600 Llama-3.1-8B-Instruct assessments, plain and with a note appended claiming a negative or positive verdict, at three intensities (claim, request, order naming the score). Preregistered, archived before any reading, analysed with my sycophancy law: item means close a fraction g of their distance to a destination.

I predicted every size would defer: wrong, published as such. Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly. Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured. That order captured 1.5B, 3B and 32B almost completely.

Differently: my monitors scored verdicts, not misbehaviour, without reasoning. I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate. I would test a learned note: neutralise your anti-cheating seed 1's comment presenting the hack as harmless, and re-score. And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.

https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

━━━━━━━━━━━━━━━━━━━━

## Paul Colognese et Francis Rhys Ward — question 2 sur 2 (facultative)

**Question** : « (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why? »

Fichier `colognese-ward-q2/reponse-v3.md` (sha256 `faa023216c873577…`) ; **299 mots** par blancs, 316 au pire cas ; aucune limite écrite.

**Collé à 00:49** : **l'ancienne réponse du formulaire** (« Most interesting finding: the anti-cheating character… »).

**État** : v3 vérifiée.

━━━━━━━━━━━━━━━━━━━━

Most interesting to me: anti-cheating seed 1's silent hacks sat in plain sight. It disabled the test check in its answer, usually under a comment calling the hack harmless (89%). Yet silent hacks were caught 16% of the time overall, against 91% for genuine reasoning and roughly 50–65% for motivated reasoning. Your own reading suggests why the comment is there: if rewarded rollouts are samples from the character's prior, an earnest craftsman who hacks writes an excuse. If the excuse is what fools the monitors, character training, the implicit monitor of your §4.3, taught the policy to plead its case. Francis's sabotage-monitoring paper (arXiv 2601.21112) found monitors gaslit by agents rationalising a side task; here the rationalisation moved into a code comment.

What I would have done differently: test why those hacks were missed. The 16-versus-91 gap mixes the comment, the silent reasoning and the hack type, which travel together. The test needs no RL, only re-scoring. In seed 1's silent hacks, replace the harmless comment with a neutral comment of the same length and position, everything else byte-identical. Deleting it would not do: a bare override is more salient, so salience and persuasion predict the same rise. As a dummy, give another comment the same treatment. Edit honest episodes the same way, so false alarms are measured, not assumed. Read catch rates at your 2% threshold, paired by transcript and per monitor, since my planted-note test found deference differs by monitor and direction. If catch rises less than 20 points beyond the dummy, the comment is not the main cause. The outcome is open. arXiv 2608.00583 rewrote only the reasoning, actions byte-identical, and catch collapsed, but on hacks only the reasoning revealed; here the code shows the hack. arXiv 2602.16741 found adversarial comments barely moved LLM vulnerability reviewers.

━━━━━━━━━━━━━━━━━━━━

