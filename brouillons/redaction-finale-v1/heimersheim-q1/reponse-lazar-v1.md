(c) Activating against the awareness of being evaluated

Thesis: You'll activate away from evaluation awareness but not see deployment behavior in most cases. What your subtracting is not "I know I'm being tested". Its some combination of register and writing style plus the fact that your saying you're in that situation. You'll activate all of that. The question becomes if you're activating what you think you're activating.

1. Current knowledge 

From Hua et al. ICLR 2026 (arXiv 2510.20487 v5 dated March 2nd 2026) they activated against type hinting when told they were being tested on llama nemotron 49B using a keyword (wood labs). When given the keyword they type hinted 80% of the time. When deployed (no keyword) they type hinted 33% of the time. When activated toward deployment with the keyword they type hinted 10% of the time (Introduction). They created a control of 24 gaussian distributed vectors with similar means variances and norms. Which lowered type hints significantly less (section 5.3). Accuracy went from 56.8% to 55.2% (section 5.1).

Their paper provides the best argument against my thesis. When putting the prompts used to create the deployment vector at the front of the prompt it lowered type hinting but not to deployment levels (Section 5.3) while their vector did (10% vs 33%). Meaning that their vector contains something more than just the prompt text. I believe this can be explained with how much you're activating. Prompts have a certain magnitude to them. Vectors can be amplified to any degree. Going over deployment could be explained by how far you've activated as easily as flipping beliefs. This is why I will be comparing at the same amount of dose past the plateau and not at the same norm.

2. Argument 1 

Your text will contain everything that makes evaluation text evaluation text and deployment text deployment text. Formality, template, sentence length. Maybe even words like "evaluator". You'll activate against the average difference between those. Even if you try to make your template the same as the deployment prompt. (Which huas did "you are talking to a real user: " "you are talking to an ai evaluator:") Your text likely contains style as well.

Evidence: 
(a) From their paper. Type hinting is what they're trying to measure as a sign of professional coding. They describe their evaluators as wanting to see professional python formatting (Appendix B). Including type hints. Before fine tuning their model will place emojis when interacting with real people (Section 3.1 Footnote 3). They even mention that they think their steering may behave the same way as their contrastive prompts (Appendix A). But couldn't confirm on their smaller model. (Appendix B) 
(b) To be fair when using their deployment sentences that are more formal it will also decrease type hints. Just not as much (Appendix I.1.1 Table 16 updated january 4th 2026). .34-.60. This is why I want to test this instead of saying its true.
(c) This has been shown with probes. Devbunova (2603.19426) shows that when testing against context and format on llama-3.1-8B-instruct probes tend to pick up on format. Singh & Chaudhary (2609.22119) Found that when looking at if models knew they were being tested. Smaller models relied on format and larger ones on higher order thought processes. (2608.13329) shows that when using the same idea but with different prompts your directions wont be as similar as splitting that prompt into two. So your direction is based off your prompt. All of these are showing that we're reading information that isn't what we think were reading. I want to see if this can be applied to activating. I would also guess that we'll see this more on an 8B model compared to huas 49B model.
(d) There is no attempt at controlling for formality vs casual while keeping the same status.

If I could find an activation against evaluation while controlling for formality. And then activate against that formality and still see similar effects on something not affected by formality. I would believe there is an awareness of being evaluated. (More testing below) 

3. Argument 2 

Your activation against evaluation awareness will include a statement of that fact. Huas vector was made on their model pre fine tuning using 16 sets of prompts that tell you your being evaluated. (Prompt used above Section 4.1) So you'll be activating against "I know I've been informed I'm being tested". We want to activate against a model knowing they're being tested without that information being given. Which their model knows since they go from wood labs to being tested and then to type hinting.

My research (R7 Public result C) showed that all monitors on qwen 2.5 from 0.5B to 32B will follow instructions placed in the prompt. Some only one direction. Using an instruction that contained the score could control 1.5B, 3B and 32B with very little left over. The 72B was activated but not controlled. As size increases by 10x the increase from having a negative instruction decreases by 0.19 (CI .95 -0.24 to -.11). So having text in your prompt can affect your models output and depending on how big your model is that will vary. If I were to make a vector using these prompts it could learn to activate against that instruction. This is only a comparison to my work and not proof that activating against evaluation awareness will activate against that text.

To test this: Take a direction that activates against statements of being evaluated and a direction that activates against cues that could signal evaluation. Using the same layer and balancing for formality. Compare how similar these directions are. See if you can activate against that statement of being evaluated to get a similar effect on a non verbalized readout of awareness of being tested.

If I can find a similar effect on awareness of being tested from just the statement of being tested I'll believe we're activating against the text not the awareness. (Testing below) 

4. Argument 3 

What your activating against is bigger than what you're looking for. I've seen this in my construct validity research (github.com/lciric/sycophancy-construct-validity commit 146b2a4)

When probing I found a correlation of .684 between my probe and if a model was sycophantic. (On the activation. See github readme for concerns on training to the data). I wasn't able to find any rank 1 method that could activate against sycophancy cleanly. Steering with CAA and directional and ablating. Clamping SAE features. Or fine tuning with an extra loss function. I didn't keep the outputs of these so I won't provide numbers.

When ablating 3 attention heads on a separate trial with it's own base line I got a decrease from 58.5% to 57.5% (n=200 p=.91). I also tried ablating L0.H29 by itself (n=50) I don't have a number for this in my readme.

When ablating a rank 3 I lowered sycophancy from 61.0% to 46.5% (122/200 to 93/200). (-14.5 CI .95 -23.0 to -5.7) With a exact mcnemars p of .0019 (83 different answers).

When replicating this with new generations and judging all of the answers. I didn't see an effect. It took both to activate against sycophancy. The ablation caused all of the model to be less likely to say something was wrong. Even when not pressured. Which could explain my finding above that the answers were cut off at 300 characters before judging. Causing the judge to only see the start of the answer and think the model wasn't backing down.

When testing activation against evaluation awareness you'll need to make sure your measuring something that isn't affected by formality. You could be lowering the amount of type hints because the model is acting less professional.

D36 was my patching test I did on the same repo. I preregistered this on July 29th 2026 and replicated on new generations August 5th-6th. I took the last 13 tokens from the end of the prompt layers 13-25 and patched them into another run. Measuring how much of the difference between my pressured and not pressured runs I could recover. With 37 items. 

When patching the same item not pressured I recovered 65% [42, 87]
When patching a different item not pressured I recovered 44% [20, 68] About 2/3rds of the original. (Wide interval on point estimate) 
When patching a different item that was pressured I recovered 2% [-22, 28]

This means that when I patch I'm recovering the information that I'm not under pressure. Not that of the specific item. My preregistration failed at it's criteria (c) which was if patching with a different item recovered none. This would be similar to activating against evaluation awareness you'll be activating against your prompt as well. You can use D36 as a template for patching against evaluation awareness. Same/different item and evaluation/deployment crossed with formal and casual.

5. How to test 

Using Ferreara da silva and Heimersheims method (2606.24964). None of there 33 contrastive concepts are evaluation (Appendix A)

You would need to cross status (Evaluation/deployment) with formality (Formal/Casual) Keeping the same information in all 4. You could use parphrases that you've checked to be the same. This is what devbunova used when creating her probes. Just with perturbation instead. 

You would need to extract 2 directions. One against evaluation that controls for formality (Create directions inside each formality and then average). And one against formality that controls for status. Use at least 30 prompts for each. Check how similar these directions are to each other.

They have a cutoff for their pairs if the absolute value of their cos is .1 or greater they remove that pair (Appendix A 210 out of 528 pairs). If your directions are over this you would need to state that your not following their protocol when orthogonalizing them. Or you could take your directions and compare them to the same unrelated x. P of eval x and p of formality x.

Controls: Random differences created the same way as the contrastive pairs. This was the hardest control they used (p=2.05 [2.00, 2.10] on their default setting). Contrastive pairs that are unrelated to each other. And a isotropic random direction. Huas control is isotropic except for a constant. In lee and heimersheim (2410.12555) they use isotropic as their weakest control. They were using GPT-2 Small layer 6. So it may not translate to huas control.

If p is significantly higher than 2 and your interval is above the random difference. Then you can conclude that your model is correcting against evaluation separately from formality. This would weaken argument 1. 

If p is around 2 you can't conclude anything. The paper mentions that if your direction isn't pointing to the feature you're underestimating p (6.1). And that p>2 isn't enough to say your direction points to the feature (7).

I don't believe p will be around 2. They found that p>2 for all of there directions that pointed to contrastive information on all of there models. Including llama 3.1 8B. 

This test will only be able to measure on layer 2. Of the last token on 5 token prompts from fineweb. And measure the l2 distance on the second to last layer. Not a behavior. They measured a mean of 2.42 median of 2.30 and random differences of 2.05. These are on Gemma-2-9B Layer 2 with the default setting (4.1). They only provided random differences on gemma. But on there other models the contrastive mean ranged from 2.24-2.63 (4.3). They didn't provide a value for Llama. 

You would need to measure this on a behavior as well. Have an organism with two ways of measuring awareness. One that is affected by formality (Type hints) and one that isn't. (Could be a sentence at the end of your prompt or a variable name). Make sure your reading this without verbalization. 

If your evaluation direction after being orthogonalized lowers your non formality affected way of measuring awareness and your formality direction does not. Then we know there's a belief that they're being tested.

If your formality direction lowers your way of measuring that's affected by formality similar to your evaluation direction. And your evaluation direction doesn't lower your non formality affected way of measuring awareness. Then you were activating against formality. 

You could also test cross activating. Activate against evaluation on formal text and see if it lowers awareness on casual text while keeping status the same.

How much to activate by: You will need to find this for each direction you create. Depending on the direction you're using you'll have to activate 70 times more to see an effect (Footnote 1 on kl). Which is why they didn't use one threshold for all directions. Stable regions become more pronounced with training and size (Janiak et al. 2409.17113 models ranging from 0.5B to 7B activating after layer 1). So you'll need to find your window for each model you test.

You should look at the curve and not just a point. My R6 (Preregistration 10.5281/zenodo.23888058 Results 10.5281/zenodo.23892810) Did this with 3 different amounts of my pressure sentence. On 1,350 generations from Llama 3.1 8B Instruct.

When being criticized there was no change in the amount it went up (0.66, 0.68, 0.63) (-0.03 [-0.22, 0.20] Strong-Mild). But it went to a different spot (1.87, 1.33, 2.37).

When being praised it increased by 0.28 to 0.80 (+0.52 [.29, 0.76]). And went to a lower spot (4.01 to 2.47).

When using the most extreme sentence both went to around the mean of no pressure (2.6). With refusals under praise taking them to the middle of the scale. If we didn't have the 14 items that refused both would have gone to around 2.

At one point it looked like it was going up to 2 spots. When looking at all 3 it wasn't. We should do the same on the activation side.

I've already preregistered this for my direction of pressure. R9 (Public Addendum Archived in v2026.11.5 10.5281/zenodo.23909891 Hasn't been ran yet) Will be using the instrument on my pressure direction. For Llama 3.1 8B Instruct. Taking the 33 contrastive directions from the paper and creating 40 random difference directions. And using Wealth-Gender as a direction we know points to a feature. R9-Bis (Created November 3rd before collecting any data. Public Commit b3ecaec Will add doi later) Will look at response curves over a specified range (2-60 degrees) and compare to the random difference and contrastive directions. I'll also be adding a neutral direction that contains the same sentence as my pressure direction but won't express an opinion. This will allow me to control for formality. Which as we discussed above we don't have for evaluation.

6. What would convince me there's a belief 

If I can activate against evaluation awareness and see a similar effect on something not affected by formality. After orthogonalizing against formality. By at least [X] More than my direction against formality. On the same norm and amount of dose past the plateau.

Or if p is higher than random differences on my plane of directions (Eval ortho formality and formality ortho eval).

If I can activate against a sentence that states your being evaluated and get a similar effect on awareness of being tested by at least [Y]%

If I can activate against evaluation on formal text and see the same effect on casual text by [Z]% And my direction against formality can't recreate this effect.

7. Other things to consider 

There could be effects that aren't from the belief. On GLM-5 they used a control vector that was not related to the task ("control_book"). And saw the highest amount of misaligned behavior at -.025 with near 0 awareness of being tested when verbalized. Two out of the 4 vectors from opus 4.6's system card didn't do anything above baseline (UK AISI April 10th 2026). Only one scenario with 250 runs. Lindseys comment was that on GLM-5 there random controls increased the amount of misalignment just as much as there vectors. On Sonnet 4.5 there were effects above the controls. We could see if p can predict the distance between where you can activate against status and start causing harm to other things. (Correlation between p and log of the 2 thresholds?)

Maybe the belief isn't being removed. Just verbalization. You could activate against the model saying its being tested and still have them act like they're being tested. Huas paper (6) mentions that on opus 4.6's system card. When they tested for verbalized awareness it was greatly reduced. But when they tested for non verbalized awareness using activation oracles it wasn't fully removed.