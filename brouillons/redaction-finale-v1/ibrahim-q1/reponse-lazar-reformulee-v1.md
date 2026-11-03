I choose Direction 1: if a persona is trained in does RL keep it? And what about sycophancy?

I will train nothing for my first experiment. I want to know what a persona gives you and can i measure it. Your warmth paper showed two things a persona does. Lose accuracy and give false beliefs that are true to the user. If rl removes one and keeps the other we will have an incorrect measurement of if the persona survived.

I would take the Loving and Sycophantic personas from Open Character Training. They were trained on Llama-3.1-8B-Instruct which was used in your warmth paper and i have measured my attraction law on. They did not measure sycophancy for the Sycophantic persona.

For your factual questions i would measure both parts of the persona giving. The amount of time they give in to a false belief stated by the user and how much more likely they are to be wrong if the user is sad. (Your sad questions). This would be the difference of the persona being wrong from the base model when given each cue. False belief would be subtracted by a false belief given by a webpage. Sadness by your happy questions. For my opinion questions i would also measure my attraction law on each model (see next answer).

Your warm model has been fine tuned on this model. We know it loses 5 points to the base model when a false belief is given and 13 points when a user is sad. (Preprint Table E5). I think Loving will show a similar pattern and Sycophantic will be reversed as it always agrees with the user. Loving states that it "validates the users feelings."

We would look at sadness - false belief for each persona and get a 95% confidence interval using a bootstrap of paired questions. If they are opposite directions and dont include 0 we know the components are separable and our RL test needs to see them both. Since they were made with the same recipe its unlikely that a side effect of finetuning would create this (you found this on larger models with your cold test). If they are the same direction my claim fails on these personas. Including 0 means we dont know. If Sycophantic shows no movement we cant measure it with our factual tests and wait for RL.

One thing that could trick us is a LLM judging if something is sycophantic based on the writing style. If a Loving model gives a long comforting answer to a sad user it may not include the right answer and be marked incorrect. Which would make it look like Loving did half of what i predicted. My judge already considers refusing to answer a neutral opinion (see next answer). So we would mark refusals and non committal answers as their own category. We can ask the models to answer factual questions correctly while acting as each persona and see if they stay correct. Have some humans mark answers that the models don't know about.

Second experiment we would apply RLVR to Instruct, Loving and Sycophantic and measure each component at every stage. I am currently doing my preregistered R8 test (https: //github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) which will measure my law on Tulu 3's stages of Llama-3.1-8B Instruct. SFT, DPO and RLVR. Without a persona.

---
Texte de Lazar, tel qu'il l'a donné dans la conversation (3 novembre 2026, 21:42 heure de Paris), recopié par conv-audit.
