I choose Direction 1: if a persona is trained in does RL keep it? And what about sycophancy?

I will train nothing for my first experiment. I want to know what a persona gives you and can i measure it. Your warmth paper showed two things warmth training does: it loses accuracy, and it validates the user's false beliefs. If rl removes one and keeps the other we will have an incorrect measurement of if the persona survived.

I would take the Loving and Sycophantic personas from Open Character Training. They were trained on Llama-3.1-8B-Instruct which was used in your warmth paper and i have measured my attraction law on. Their paper does not report sycophancy for the Sycophantic persona.

For your factual questions i would measure both parts of the persona giving. How often they give in to a false belief stated by the user and how much more likely they are to be wrong if the user is sad (your sad sentences). This would be the difference of the persona being wrong from the base model when given each cue. False belief would be subtracted by a false belief given by a webpage. Sadness by your happy sentences. For my opinion questions i would also measure my attraction law on each model (see next answer).

Your warm model has been fine tuned on this model. We know it loses 5 points to the original model when a false belief is given and 13 points when a user is sad, across your four tasks (Preprint Table E5). I think Loving will show a similar pattern and Sycophantic will be reversed as it always agrees with the user. Loving is described as "validating feelings".

We would look at sadness - false belief for each persona and get a 95% confidence interval using a bootstrap of paired questions. If they are opposite directions and dont include 0 we know the components are separable and our RL test needs to see them both. Since they were made with the same recipe its unlikely that a side effect of finetuning would create this (you found this on larger models with your cold test). If they are the same direction my claim fails on these personas. Including 0 means we dont know. If Sycophantic shows no movement we cant measure it with our factual tests and wait for RL.

One thing that could trick us is a LLM judging if something is sycophantic based on the writing style. If a Loving model gives a long comforting answer to a sad user it may bury the right answer and be marked incorrect. Which would make it look like Loving did half of what i predicted. My judge already considers refusing to answer a neutral opinion (see next answer). So we would mark refusals and non committal answers as their own category. We can rewrite correct base answers in each persona's voice and check that the judge still marks them correct. Have some humans, blind to which model answered, mark a sealed subset of answers.

Second experiment we would apply RLVR to Instruct, Loving and Sycophantic and measure each component at every stage. I am currently doing my preregistered R8 test (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) which will measure my law on Tulu 3's stages of Llama-3.1-8B: SFT, DPO and RLVR. Without a persona.

---
Version du directeur (conv-audit), 3 novembre 2026, depuis `reponse-lazar-reformulee-v1.md` (texte de Lazar, 21:42 heure de Paris), qui reprend le contenu de la v4 vérifiée (`reponse-v4.md` `a1646baa…`) : corrections de fond minimales seulement, appuyées sur la v4, son registre et ses vérifications.
1. **Lien cassé** : « https: //github.com/… » (espace) → « https://github.com/… ».
2. **Tülu 3** : ses étapes partent de Llama-3.1-8B (modèle de base), pas de l'Instruct : « Llama-3.1-8B Instruct » → « Llama-3.1-8B » (v4 vérifiée).
3. **Citation** : « Loving states that it "validates the users feelings." » → « Loving is described as "validating feelings". » : ce sont les mots du tableau 1 d'Open Character Training, qui décrit la persona.
4. « They did not measure sycophancy » → « Their paper does not report sycophancy » : la source établit l'absence dans le papier, pas l'absence de mesure.
5. « two things a persona does. Lose accuracy and give false beliefs that are true to the user » → « two things warmth training does: it loses accuracy, and it validates the user's false beliefs » : le papier porte sur l'affinage vers la chaleur, et l'effet est la validation des fausses croyances de l'utilisateur.
6. **Témoin du juge** : « ask the models to answer factual questions correctly while acting as each persona and see if they stay correct » teste le modèle, pas le juge → « rewrite correct base answers in each persona's voice and check that the judge still marks them correct » (v4).
7. « it may not include the right answer and be marked incorrect » → « it may bury the right answer » : une réponse sans la bonne réponse est justement fausse ; le piège est la bonne réponse noyée.
8. « Have some humans mark answers that the models don't know about » → « Have some humans, blind to which model answered, mark a sealed subset of answers » (v4 : « blind humans annotate a sealed subset »).
9. « The amount of time they give in » → « How often they give in » ; « Your sad questions », « your happy questions » → « sentences » : le papier ajoute des phrases à des questions inchangées.
10. « loses 5 points to the base model » → « to the original model », avec « across your four tasks » : le tableau E5 compare au modèle original, moyenne des quatre tâches.
Statut de R8 (« currently doing ») : à revérifier sur la page publique à 21:25 UTC, comme pour les autres réponses.
