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
