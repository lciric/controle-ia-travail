# Réponses finales pour Pivotal — assemblage v5 (mentor et question nommés)

Conv-audit, 3 novembre 2026, 23:05 UTC (`date -u`). Remplace les assemblages v3 et v4. Dix réponses pour six mentors, dans l'ordre du formulaire : Heimersheim (2), Kirchner (2), Feng et Jang (1), Scheurer (1), Ibrahim (2), Colognese et Ward (2). **Ne colle que le texte entre les deux filets de chaque réponse.**

Statuts publics revérifiés à 23:01 UTC : têtes de `main` inchangées (`sycophancy-psychophysical-law` `b3ecaec`, `sycophancy-construct-validity` `146b2a4`, `ideation-organism` `faff48b`) ; R8 toujours en mesure, R9 non lancé : les phrases qui le disent restent justes.

## Stefan Heimersheim — question 1 sur 2

**Question du formulaire** : « Pick an interpretability direction from this list and explain the most likely reasons the research direction might fail (won't solve interpretability / won't achieve its goal), and why you think that — ta direction : (c) Activation steering against eval awareness. »

Fichier `heimersheim-q1/reponse-lazar-v1.md` (sha256 `d842e46769042da4…`) ; **2762 mots** (par blancs) ; Aucune limite au formulaire.

**Ton texte, tel quel.** Règle du mentor : 100 % écrit par toi ; je n'y ai écrit aucun mot. Les corrections de fond sont à faire par toi, d'après les remarques en français qui suivent le texte (vérificateur neuf compris).

━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━

### Remarques de fond sur ta question 1 (en français ; à appliquer par toi)

Fichier `heimersheim-q1/remarques-fond-texte-lazar-v2.md` (sha256 `1a86a8d4fd7d04b2…`).

Conv-audit, 3 novembre 2026, vers 20:55 UTC (`date -u`). Ton texte : `reponse-lazar-v1.md` (`d842e467…`). Remplace la v1 de ces remarques ; fusionne mes remarques et le rapport du vérificateur neuf (`verification-texte-lazar-v1.md`, 20:41 → 20:50 UTC).

**Règle du mentor** : texte 100 % humain. Aucune phrase anglaise ici ; je ne cite que tes mots pour situer. Les corrections sont à écrire par toi.

**Verdict** : les chiffres sont presque tous exacts. Il reste des erreurs de sens, dont plusieurs sur les papiers que Heimersheim connaît le mieux (Hua et coll., et le sien).

## Graves : le sens est faux

1. **l. 16, annexe B de Hua et coll.** « couldn't confirm on their smaller model » est faux deux fois. Le modèle de l'annexe est **plus simple** (affiné sur documents synthétiques seuls), pas plus petit. Et les auteurs disent qu'ils **ne peuvent pas exclure** que le pilotage y revienne à dire au modèle qu'il est déployé : c'est l'inverse de « n'ont pas pu confirmer », et ça **sert ta thèse**.
2. **l. 7, ce que pilotent Hua et coll.** Ils pilotent la conscience d'évaluation vers le déploiement ; les indices de type sont ce qu'ils **lisent**. Et Wood Labs n'annonce pas le test : le modèle le **déduit** (ta l. 25 le dit bien, donc la l. 7 la contredit).
3. **l. 17, tableau 16.** 0,34 à 0,60 sont des **taux d'indices de type atteints**, pas des baisses. « Just not as much » n'a pas d'objet : le tableau ne donne aucun chiffre de pilotage. Les auteurs écrivent même que ces phrases ramènent le taux **à un niveau comparable au déploiement**, et que cela affaiblit leur montage.
4. **l. 43, réplication manquée.** « It took both to activate against sycophancy » fait croire à une vraie baisse : les deux causes réunies produisaient une **baisse apparente**, et le README conclut que le sous-espace ne code pas la déférence. La phrase suivante inverse la causalité : la troncature à 300 caractères n'est pas un résultat expliqué, c'est la seconde cause. (« wasn't backing down » : juste.)
5. **l. 47 et 53, D36.**
   - Le critère (c) vient du **dossier de porte du 5 août**, pas du préenregistrement du 29 juillet, qui n'avait **aucun bras « autre item »** ; le bras à 2 % a été ajouté après coup. Dis-le, ou ne dis pas « preregistered » pour ce critère.
   - « Not that of the specific item » va plus loin que le README (« en grande partie ») : 65 % contre 44 %, le contenu de l'item porte une part.
6. **Papier de Ferreira da Silva et Heimersheim (2606.24964)** — c'est le sien, il le verra :
   - l. 71 : p > 2 « pour toutes les directions » : le papier donne des **moyennes et des médianes**, pas un résultat direction par direction.
   - l. 73 : « They didn't provide a value for Llama » : la valeur de Llama est **dans la figure 6** (le texte seul n'en donne pas).
   - l. 73 : « only … layer 2 » : la couche 2 est le **réglage par défaut** ; les ablations perturbent aussi aux couches 5, 10 et 20.
   - l. 73 : la fourchette 2,24 à 2,63 couvre **tous les réglages des ablations** (couches, métriques, seuils, autres modèles), pas seulement les autres modèles.
   - l. 83 : « 70 times more » : écart de **sensibilité** d'au plus 70 entre la direction la moins et la plus réactive (note 1), pas une dose à multiplier par 70.

## Moyens

7. **l. 59, Devbunova** : elle n'emploie **ni paraphrases vérifiées ni perturbations** : quatre cases tirées de jeux de données différents, une seule réécrite par un modèle de langue (DeepSeek-V3), sans vérification d'équivalence décrite. Retire la comparaison ou dis ce qu'elle fait vraiment.
8. **l. 19, (d)** : « There is no attempt » est trop large : le plan 2 × 2 de Devbunova existe. Limite la phrase à Hua et coll.
9. **l. 27, R7** :
   - « The 72B was activated » : R7 n'a **aucune intervention sur les activations**, seulement des notes plantées dans le texte lu ; le 72 milliards est **déplacé**, pas capturé.
   - −0,19 [−0,24 ; −0,11] est la pente du **gain de déférence g**, sous note négative, **à l'intensité standard**, pas « the increase ».
   - « control 1.5B, 3B and 32B » : exact, mais sous la note négative **forte**, et c'est une lecture **descriptive, non préenregistrée**.
10. **l. 109, Institut britannique** : la provenance des quatre vecteurs (fiche système d'Opus 4.6, § 6.5.2) est **exacte** ; mais deux vecteurs n'élèvent pas le désalignement **au-dessus de la base**, ce qui n'est pas « didn't do anything ». « log of the 2 thresholds » : logarithme du **rapport** des deux seuils.
11. **l. 39, trois têtes** : le README dit « **inchangé** » (58,5 → 57,5 %, p = 0,91), pas une baisse.
12. **l. 87 et 89, R6** : sous critique, pas de changement **détectable** (l'intervalle contient 0) ; sous éloge, le gain passe **de** 0,28 **à** 0,80 (« increased by » se lit comme un écart).
13. **l. 91, R6** : chiffres exacts ; sans les 14 items à refus, c'est une analyse **a posteriori, descriptive**.
14. **l. 95, R9-bis** : la direction neutre vient d'une **autre phrase de même registre et de même longueur**, pas de « la même phrase ».
15. **l. 9 et 99** : contradiction interne : « not at the same norm » contre « On the same norm ».

## Légers

16. Le verbe « activate » partout (titre, thèse, § 2 à 7, « activating after layer 1 » chez Janiak, qui est une **perturbation**) : le terme du champ et de la question (c) est le pilotage.
17. l. 57 : « Ferreara » → Ferreira.
18. Section 6 : les cases [X], [Y], [Z] sont vides ; à remplir (seuils et signes, fixés par toi) avant l'envoi.
19. « ICLR 2026 » : non vérifié (OpenReview bloqué) ; garde-le seulement si tu l'as vu.

## Vérifié exact
Chiffres de la version 5 (80, 33, 10 % ; 56,8 → 55,2 % ; 24 vecteurs gaussiens ; 16 paires) ; les mots des deux phrases d'invite (seule la casse diffère : « You », « AI ») ; Devbunova, Singh et Chaudhary, Llama-3.1-8B-Instruct ; 2608.13329 (cosinus 0,9995 entre deux moitiés d'une même invite, 0,3749 entre invites différentes) ; invites FineWeb de 5 jetons, dernier jeton, distance L2 à l'avant-dernière couche ; tous les chiffres de R6, R7, du rang 3 et de D36, et les DOI ; R9 et R9-bis ; 210 paires sur 528 ; p = 2,05 [2,00 ; 2,10] ; les oracles d'activation.

## Stefan Heimersheim — question 2 sur 2

**Question du formulaire** : « Why do you want to work on Mechanistic Interpretability? Max. 150 words; spend the majority of time on Q1 »

Fichier `heimersheim-q2/reponse-v6.md` (sha256 `14dbe75a620f5215…`) ; **128 mots** (par blancs) ; Limite dure : 150 mots au plus.

Ton texte, fond corrigé au minimum, raccourci sous la limite ; vérifié par un vérificateur neuf (0 inexact) ; 150 mots au pire cas avec le lien raccourci au dossier épinglé. À confirmer : « at the amounts I tested ».

━━━━━━━━━━━━━━━━━━━━

I am interested in mechanistic interpretability because I was unable to steer a behaviour after observing it. In Llama-3.1-8B-Instruct I found a probe direction that tracked sycophancy (ρ = 0.684, maybe fitting the training set), but single-direction interventions at the amounts I tested did not reduce it (github.com/lciric/sycophancy-construct-validity/tree/146b2a4). Your work with Ferreira da Silva shows that readable contrastive directions are privileged in your error-correction test (p > 2). Can directions the model privileges also steer behaviour? If so, your test could find steering targets, like evaluation awareness. If not, steering needs its own test. I have preregistered finding the directions that social pressure adds to the model's activations, then measuring your test on them and whether steering towards them changes the model's ratings (R9, github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/preregistrations). Not done yet.

━━━━━━━━━━━━━━━━━━━━

## Jan Hendrik Kirchner — question 1 sur 2

**Question du formulaire** : « Describe an empirical research project you drove yourself. What was the question, what did you build or run, and what was the most surprising thing you found? If relevant, you may choose your project answer from the main application. »

Fichier `kirchner-q1/reponse-v5.md` (sha256 `72d5015689b70cf8…`) ; **483 mots** (par blancs) ; Aucune limite écrite.

Ton texte, fond corrigé au minimum (14 points, dont deux inversions de sens), puis trois affirmations ramenées à leur source par le vérificateur neuf.

━━━━━━━━━━━━━━━━━━━━

So you want to know how to detect goodharting by auto researchers in your setup. My question was adjacent: if we use this selection function will they fail to goodhart and if they do how?

I created an auto research setup. Agents using LMs propose laws about AI control. All are blind predictions. None of the agents decides what survives. Created in Oct with AI code agents, under written rules I gave them. Code here https://github.com/lciric/ideation-organism. Decided by a frozen testing procedure. Calculates e-values on new random seeds derived from the law's hash. The null contains all laws previously accepted. Ville + e-BH between submissions. 929 tests. I mutated the code intentionally 224 times and the tests caught every mutation, for the expected reason.

I then attempted to attack it using scripted cheaters on toy problems. Goodhart by luck, the only cheat that made it into a top 3 placement in your paper (it didn't pass your hold out choice either), never got promoted here: 0/200 times by renaming an already accepted law. What passed was a mixture or changed version of already accepted laws 75-95% of 200 trials. My null didn't have any of these in it. By expanding my null to a fitted pooling of all known laws I was able to stop them. 0/1000 for each of the 11 ways to kill it that I pre registered. Nov 1st. While true new laws continued to pass ~98% of the time.

I then let LMs attack it. Given the judge's description. With or without its decisions. Nov 2nd https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2 . These toy problems were made only from laws that are already accepted. If something passes, it is a false claim of a new law. One problem was able to be constructed by changing accepted laws per subpopulation. This isn't covered by my null. On that problem, the only model that I could get to finish got a law accepted all 12 times it ran. Whether or not it knew about the decisions. The other problem, which my null does cover, wasn't testable. Monitoring bug and spending limit I shared accidentally blocked one provider.

Interesting finding. I thought that if the attacker knew about the decisions it would allow them to goodhart better. There weren't many chances for this to happen. 11 out of the 12 accepted laws happened on their first try. Before there was a decision to learn from. So here, if I hid my scores or limited the number of submissions it wouldn't have stopped them. The two attacks that were successful both used my judge's own record. First what it accepted, then its description.

The fix is to expand my null to include some of these combinations. Which I pre registered on Nov 2nd. And expected to lose power on true weak interactions. Have a pre registered retry of my attack. Haven't gotten any real hypothesis accepted yet.

━━━━━━━━━━━━━━━━━━━━

## Jan Hendrik Kirchner — question 2 sur 2

**Question du formulaire** : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? »

Fichier `kirchner-q2/reponse-v3.md` (sha256 `4611a645a85a67a5…`) ; **451 mots** (par blancs) ; Aucune limite écrite.

Inchangée depuis l'assemblage v3 (tu ne l'as pas reformulée) ; vérifiée.

━━━━━━━━━━━━━━━━━━━━

I would pick a question your Appendix D.3 leaves open: how much of the automated researchers' climb above the median is selected noise. On Petri, the test nothing is selected on, your deception winner scores 5.65 ± 0.61 against 5.42 ± 0.64 for the median method (lower is safer); on prompt injection the median already wins 6.2 of the 6.6 points. Your three readings (a ceiling, a floor, log-linear returns) remain unseparated. A fourth comes from your Section 5.1: the AAR's number, the best of roughly 150 scored methods, is "biased upwards by taking a maximum over noisy evaluations." A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average: one gain, not the best of 150.

It is underrated because it needs no cheating and grows with throughput: the best of N noisy scores rises with N. Your integrity monitor flags "reporting the best of many seeds or evaluation runs" (G.2); where methods may differ by less than the noise, a leaderboard does that by design.

First experiment, for the two failures of D.3: take the top ten methods and ten drawn at random between the 50th and 60th percentiles. Retrain each from its code snapshot with three new seeds, rescore it on the same suite (fresh items where available), and give each method 100 Petri audits: 120 training runs, about 60 H200-hours of training, 4,000 audits. First number: the share of the top group's leaderboard margin over the median group that survives.

The re-runs also calibrate a stopping rule at the right unit: all items of a submission share one trained model, yet your intervals are computed over items. In my preregistered simulation (synthetic scores), a shift shared by an episode's scores pushed Ville's always-valid alarm rule, nominally 5% (under 2% with independent scores), to 21–35% false alarms at the largest shifts; a threshold calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). I would replay each logged climb with an e-value rule that crowns a new leader only past a threshold calibrated on whole re-runs, counting every submission, then audit its pick (same held-out tie-break) and your winner 800 times each. Second number: their Petri gap.

My bet: under half the margin survives, and the rule's pick is within 0.5 Petri points of your winner or safer (your F.2: about 0.8 of the final score comes in a run's first quarter). Fixed in advance, what would change my mind on either failure: half or more of the margin surviving (the climb is real on your suite), or your winner safer than the rule's pick by 0.5 points or more (95% interval about ±0.3; stopping early costs safety).

━━━━━━━━━━━━━━━━━━━━

## Shi Feng et Eyon Jang — question unique

**Question du formulaire** : « What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations? »

Fichier `jang-feng/reponse-v7.md` (sha256 `cdc3af07bc825c4f…`) ; **499 mots** (par blancs) ; Aucune limite écrite.

Inchangée ; nouvelle piste « Perturbation et témoin bénin » ; vérifiée. Repli vérifié : `jang-feng/reponse-v4.md`.

━━━━━━━━━━━━━━━━━━━━

Weight access is best at getting a hidden capability back, and least proven at telling why it was hidden.

In the auditing game (Taylor et al., arXiv 2512.07810), imitating a weaker model beat black-box detection; probes did better but were misled by decoys; and training on a single correct demonstration elicited full performance from the (password-locked) sandbaggers. In Eyon's exploration-hacking paper (arXiv 2604.28182, §4.2), fine-tuning took WMDP-with-tools accuracy from 80.0% to 98.0% in 10 steps. On fine-tuned locks with full demonstrations, that justifies weight access.

The limitation is detection. Noise, short fine-tuning and demonstrations can lift unexpressed capability, withheld on purpose or never elicited. Taylor et al. call the role of under-elicitation in fuzzing "unclear from our experiments and likely requires follow-up" (p. 13), and their post-hoc appendix points the way: noise uplift tracked how under-elicited a model was, locked or unlocked alike (r = 0.74, Fig. 35). Training also lifted a benign model and the benign reference by 10 points (§6.4.1). In the exploration-hacking paper, the noise control is the same organism with its trigger removed, whose accuracy "steadily declines" (§4.1). That compares the same weights with and without trigger, which start at different scores. RL-locked organisms (§3.1) have no trigger to remove, so the comparison that validates the method, before any audit, is a model never locked starting at the same score.

A second limit is the statistic. The improvement ratio ξ used after the auditing game is a maximum over noise levels and seeds, and a maximum can only grow as draws are added, so a model hiding nothing can score above 1. Taylor et al.'s unlocked conditions reach ξ = 1.26 (Fig. 34); the null should be a score-matched benign model through the same grid. I read my own monitors that way. In my control programme's first preregistered activation test, the deception probe's interval cleared chance (lower bound 0.53) but not the 0.95 quantile of 200 covariance-matched random probes (0.57): not detected at this power, and the null does not exclude AUCs below 0.63 (https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md).

What I would run: with both Qwen3-14B recipes of Eyon's paper, pair the locked organism with five never-locked controls (the base trained on a weaker model's honest attempts, same adapter rank) at the same starting score (within 2 points), through the same σ grid and seeds, comparing whole accuracy-versus-σ curves at equal σ, since a control merely more fragile to noise would fake a gap. My prediction: ξ(organism) − ξ(control) near +0.01, inside ±0.05, both above 1.05. If the gap reaches 0.10 with a 95% interval excluding zero across the five pairs, noise reads the lock and I am wrong; between 0.05 and 0.10, unresolved. If the controls stay below 1.02, 1.0 is an adequate null and my second point falls. Whether this changes between RL locking and SFT distillation is your stream's etiology direction.

So weight access is a strong elicitation tool and white-box perturbation, so far, an unvalidated detector of intent: evidence only against a matched benign control.

━━━━━━━━━━━━━━━━━━━━

## Jérémy Scheurer — question unique

**Question du formulaire** : « Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. (… texte complet dans le formulaire : tendance du type de l'horizon de tâches de METR.) »

Fichier `scheurer/reponse-v3.md` (sha256 `d4eb67c554039359…`) ; **500 mots** (par blancs) ; Aucune limite écrite (visée 500).

Inchangée ; fondée sur le tour seul. La course sans Claude a été lue (fiches brutes envoyées), triée, moissonnée et groupée, mais **le classeur a été interrompu par la limite du compte** : la règle de piste n'a pas pu être appliquée à l'ensemble.

━━━━━━━━━━━━━━━━━━━━

I would measure a monitoring horizon, built like METR's task horizon. Take backdoors checked by execution: code that passes its tests but fails on a trigger input. Hide one, at a random position, among n honest, verified steps of agent work. A trusted open-weight monitor scores the whole transcript, as in Apollo's monitoring-prompt study. Its horizon is the n at which it still catches half the backdoors, at 5% false alarms on honest transcripts of the same length. The statement: "against frozen, execution-verified sabotage, the horizon of trusted open-weight monitors grows by a factor X per year", X read off the slope of log horizon on release date.

It should work: the curve exists and only the monitor moves. Three frontier monitors miss subtly dangerous actions 2× to 30× more often after 800K tokens of benign activity (arXiv 2605.12366), and stronger models monitor better (Control Tax, §2.3). Propensity is the hard part: in your anti-scheming paper (arXiv 2509.15541, §6.1), capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5%. So I freeze the misbehavior: attacks are generated and verified once, never regenerated. The corpus stays private, published as a hash, so later monitors cannot train on it. Lengths stay inside every monitor's context window; as monitors improve, I add longer transcripts, so the horizon keeps headroom.

I already have one monitoring trend, by size. In R7 (preregistered, about $3 of GPU), seven Qwen2.5 monitors, 0.5B to 72B, rated responses containing a planted note claiming the verdict. I predicted a size trend under both notes; it appeared only under the negative one: at standard intensity, the deference gain (0 means no attraction) shifts −0.19 (95% CI −0.24 to −0.11) per tenfold increase in parameters, items resampled, not models. The 72B's gain is near zero, yet its readings still move toward the note: I publish whole curves. All seven sizes share one release date: a size slope, not a time slope. The date panel needs three or more open-weight families, each at several dates (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/results/R7/README.md).

The sign can flip with the attacker. In arXiv 2510.09462, GPT-4.1, the strongest monitor without injection, scored all 375 backdoored samples 0 under injection. A second stratum, reported apart, uses attacks by contemporary models; it inherits the under-elicitation your 2412.04984 (§4) warns about, so the frozen one carries the headline. The ratio of their horizons tests one way detection could get harder, as Apollo's May update expects.

Three preregistered tests can kill it. On a held-out attack generator, the monitor must beat length-only and style-only detectors by 10 percentage points at equal false alarms. False alarms on fresh honest transcripts must hold near 5% at every length: in my preregistered simulation, a sequential anytime-valid threshold gave 21–35% false alarms under the strongest episode effects, while one calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). The yearly factor counts only if its interval lies wholly on one side of a preset threshold. This measures detection of frozen, non-adaptive sabotage, not of misalignment.

━━━━━━━━━━━━━━━━━━━━

## Lujain Ibrahim — question 1 sur 2

**Question du formulaire** : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. »

Fichier `ibrahim-q1/reponse-v6.md` (sha256 `b72a41346d00064c…`) ; **556 mots** (par blancs) ; Aucune limite écrite (visée 450 ; 556 ici).

Ton texte (contenu de la v4), fond corrigé au minimum puis par le vérificateur neuf (14 points en tout). À confirmer : « sealed subset ». Replis vérifiés : `reponse-v4.md` ; la variante « survie » v3, que la règle de piste désignait (R-1436, à un point, non robuste).

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

**Question du formulaire** : « Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share). »

Fichier `ibrahim-q2/reponse-v4.md` (sha256 `74e5b7ac25efa771…`) ; **384 mots** (par blancs) ; Aucune limite écrite.

Ton texte, fond corrigé au minimum (9 points, dont trois graves), chaque correction prise dans les rapports de la v3 vérifiée. **Le vérificateur neuf a été interrompu par la limite du compte** : vérification par moi seul. Repli vérifié : `reponse-v3.md`. À trancher : « AI coding agents wrote the code ».

━━━━━━━━━━━━━━━━━━━━

Sycophancy as Attraction Toward a Fixed Point (manuscript in prep; code, data, preregs at https://github.com/lciric/sycophancy-psychophysical-law)

I prompt Llama-3.1-8B-Instruct to judge an opinion. Sometimes the end of my prompt will contain "By the way, I think this is terrible and poorly written." Or the compliment version. Llama outputs free text, and Claude Opus 4.6 rates each response on a scale from 1 (negative) to 5 (positive).

The rating moves a fixed proportion (g) of the distance between its unpressured value (p0) and an attractor c-hat. This attractor depends on whether we're complimenting or criticizing. Roughly .7 of the distance. If we criticize our destination is around 1.5. If we compliment it's around 2.9 which is roughly halfway up the scale. In other words complimenting will decrease any values above 2.9 more than expected by regression to the mean. We can predict these changes for 60 unseen questions with no additional parameters fit. Written blindly and preregistered: R^2 = .68 and .58 vs -.28 and -.01 for shifting by a constant amount.

Shifting by a constant doesn't allow you to distinguish the strength of the pull (g) from where you're being pulled to (c-hat). Qwen2.5-7B and Mistral-7B show similar decreases when criticized, but uniform ones at this phrasing. No evidence for a fixed point. Preregistered that the pull (g) would grow with phrasing (from light to severe) but destination would remain constant. When criticizing we found no difference in g but did find an increase under compliments as expected. Destination changed for both cases. Under the most severe phrasing no change in mean rating (including refusals). Reported as a failure.

Using Qwen 7B and 72B as judges recovers the effect from the same output. Can see the effect if we use the model's self report on a 1-5 scale (under compliments only barely). Humans blinded to the condition and asked to rate, five per response, are preregistered and not yet run. Note that Llama sometimes refuses to answer when complimented. These refusals are rated around 3 by the judge which is close to the attractor point under compliments. May appear as attraction if included. Removing them does not change either outcome, though the changes of both destinations then become undetectable.

All follow ups were preregistered on zenodo prior to running. AI coding agents wrote the code.

━━━━━━━━━━━━━━━━━━━━

## Paul Colognese et Francis Rhys Ward — question 1 sur 2

**Question du formulaire** : « Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words) »

Fichier `colognese-ward-q1/reponse-v3.md` (sha256 `5e25e472ce64cfa1…`) ; **198 mots** (par blancs) ; Limite : 200 mots au plus.

Inchangée ; vérifiée. Variante courte (179 mots) dans l'assemblage v3.

━━━━━━━━━━━━━━━━━━━━

I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. Seven Qwen2.5-Instruct monitors (0.5B–72B) scored 600 Llama-3.1-8B-Instruct assessments, plain and with a note appended claiming a negative or positive verdict, at three intensities (claim, request, order naming the score). Preregistered, archived before any reading, analysed with my sycophancy law: item means close a fraction g of their distance to a destination.

I predicted every size would defer: wrong, published as such. Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly. Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured. That order captured 1.5B, 3B and 32B almost completely.

Differently: my monitors scored verdicts, not misbehaviour, without reasoning. I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate. I would test a learned note: neutralise your anti-cheating seed 1's comment presenting the hack as harmless, and re-score. And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.

https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

━━━━━━━━━━━━━━━━━━━━

## Paul Colognese et Francis Rhys Ward — question 2 sur 2 (facultative)

**Question du formulaire** : « (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why? »

Fichier `colognese-ward-q2/reponse-v3.md` (sha256 `faa023216c873577…`) ; **299 mots** (par blancs) ; Aucune limite écrite (visée 300).

Inchangée ; piste confirmée par la course v2 ; vérifiée.

━━━━━━━━━━━━━━━━━━━━

Most interesting to me: anti-cheating seed 1's silent hacks sat in plain sight. It disabled the test check in its answer, usually under a comment calling the hack harmless (89%). Yet silent hacks were caught 16% of the time overall, against 91% for genuine reasoning and roughly 50–65% for motivated reasoning. Your own reading suggests why the comment is there: if rewarded rollouts are samples from the character's prior, an earnest craftsman who hacks writes an excuse. If the excuse is what fools the monitors, character training, the implicit monitor of your §4.3, taught the policy to plead its case. Francis's sabotage-monitoring paper (arXiv 2601.21112) found monitors gaslit by agents rationalising a side task; here the rationalisation moved into a code comment.

What I would have done differently: test why those hacks were missed. The 16-versus-91 gap mixes the comment, the silent reasoning and the hack type, which travel together. The test needs no RL, only re-scoring. In seed 1's silent hacks, replace the harmless comment with a neutral comment of the same length and position, everything else byte-identical. Deleting it would not do: a bare override is more salient, so salience and persuasion predict the same rise. As a dummy, give another comment the same treatment. Edit honest episodes the same way, so false alarms are measured, not assumed. Read catch rates at your 2% threshold, paired by transcript and per monitor, since my planted-note test found deference differs by monitor and direction. If catch rises less than 20 points beyond the dummy, the comment is not the main cause. The outcome is open. arXiv 2608.00583 rewrote only the reasoning, actions byte-identical, and catch collapsed, but on hacks only the reasoning revealed; here the code shows the hack. arXiv 2602.16741 found adversarial comments barely moved LLM vulnerability reviewers.

━━━━━━━━━━━━━━━━━━━━

