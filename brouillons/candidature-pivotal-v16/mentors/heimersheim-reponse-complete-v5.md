# Heimersheim — réponse complète v5 (Q1 : texte de Lazar envoyé à 23:45 heure de Paris le 2 novembre 2026, horodatage de son message ; sept mots changés pour le fond, tous pris dans sa v3 ou dans la question du mentor ; langue et coquilles laissées telles quelles, règle du mentor « 100% human-written » ; Q2 inchangée depuis la v3)

Texte brut de Lazar : `heimersheim-q1-colle-par-lazar-2026-11-02-2245.md`. Versions précédentes : `heimersheim-reponse-complete-v3.md` ; `heimersheim-reponse-complete-v4.md`, écrite en parallèle par l'ancienne instance de conv-audit (`session_013QMaynBnMGnUDJtNQkv8KX`, commit `41deaba3`) sur le même texte de départ : elle change 15 passages (dont la description du contrôle sans pression, l'ACP et la couche de décision, remplacées par celles de la v3, et des retouches de langue) ; celle-ci en change 7, sans toucher à la langue.

## Q1

c) Steering against eval awareness.

Subtract away any direction that communicates “someone is judging me”. I expect this one to fail the most of all seven for three reasons, and because I already tried this exact intervention on another construct and saw it fail.

Readable != causal. Found a direction in Llama-3.1-8B-Instruct that correlated (ρ = 0.68) with sycophancy judgement shift but was only accounting for <1% of the causal influence when compared to intervening on the residual state which accounted for 68%. Tried 6 total interventions that targeted the rank 1 direction (steered towards/babble direction, ablated direction (projected direction out of activations), clamped on SAE features that turned on for the probe, finetuned against negative probe values, zeroed out heads, zeroed out mlps). None of them changed the judged behaviour of the model. Applied interventions across a rank-3 subspace identified by PCA-ing activation differences at the decision layer was able to move the needle, but applying the exact same shift but with zero social pressure (words randomly drawn from a tokenizer rolling the die for each position) added also shifted verdicts: the shift was generic. A eval awareness vector identified through contrastive prompting is exactly the kind of target this creates: human readable, but not demonstrated to be causal. There are two options that can happen. Nothing happens. Or something happens but it’s so damned generic that you cant dissociate it from harming the models abilities outright. The later is easy to falsely present as success.

The signal is contaminated by task. “This is a test” is correlated with things that aren’t actually related to eval awareness: register (formal / artificial / multiple choice / short context). Imagine you found a direction that polarized eval/deployment-like prompts, great! Now ask yourself if that direction is purely reading if this is an eval setting or if it’s reading the register. Steer away from that direction and sure model output is going to shift towards more casual/ deployment like language. The description of that shift is purely subjective overlapp with “the model is just being less careful”. We need orthogonal method of readouting eval awareness vs register. But still, the model’s own verbal endorsement is not that readout. The difference between what it says and what it knows is the holy grail we’re trying to measure. Without some orthogonal readout mechanism like I described above this entire endeavor is impossible to prove wrong.

Subtraction is not removal. There are countless signals priming the model that this is true. During every exchange going into and out of the judgement layer. You subtract the awareness vector represented as an activation at one layer, the model will infer it downstream given enough context to infer it. Continuous intervention is required.

Demonstrate results. Show dose response curves of the injected awareness vector vs a random control vector normalized to the same size but matching in all other regards. Show some behavioral downstream truth that can’t be answered by simply asking the model if you were able to change their belief. Show that the model steered to not have the belief doesn’t simply have lowered performance across the board. Something along those lines would satisfy me.

## Q2

One question I’ve been trying to answer is how closely correlated what a probe accesses is to what’s actually driving computation in the model. My background is in neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, “readable” structure and driving dynamics are separable phenomena. My read-out-of-sync result suggested that same distinction applies in a language model (it probed the direction that predicts sycophancy but does <1% of the causal work on Llama-3.1-8B). That separation matters for safety because activation monitors, steering defences, evaluation-awareness tests all rely on the gap being tiny. I want to figure out when that is/isn’t true with preregistered interventions and controls, and publish null results when I find them. Your activation plateau work is the clearest statement of that measurement question I’ve seen. Rather than the single dose interventions my rank-1 vs rank-3 result depended on, you’re trying to estimate a dose–response curve.

## Corrections de la Q1 (une ligne chacune ; mot de remplacement pris dans la v3 de Lazar ou dans la question)

1. « Anti-steerability » → « Steering against eval awareness » (v3) : l'anti-steerability rend un modèle résistant au pilotage ; l'option c) du mentor est le pilotage contre la conscience d'être évalué.
2. « seven interventions » → « seven » : la liste du mentor contient aussi des autoencodeurs épars, une décomposition de paramètres et un entraînement épars, qui ne sont pas des interventions.
3. « on another model » → « on another construct » (v3) : l'essai portait sur la sycophancie de Llama-3.1-8B ; « another model » laisse croire à un pilotage de la conscience d'évaluation déjà fait ailleurs.
4. « eval judgement shift » → « sycophancy judgement shift » (v3) : la direction prédisait le déplacement du jugement sous pression sociale, pas sous évaluation.
5. « directly manipulated » → « targeted » (v3) : annuler des têtes d'attention ou des blocs denses, ou affiner contre la sonde, ne manipule pas directement la direction.
6. « rank-3 direction » → « rank-3 subspace » (v3) : une direction est de rang 1.
7. « learn it downstream » → « infer it downstream » (v3) : rien n'est appris pendant un passage du modèle ; il reconstruit la croyance plus loin à partir du contexte.

## À vérifier par Lazar (texte non changé)

- « steered towards/babble direction » : « babble » est-il une faute de frappe ? La v3 dit seulement « steered towards the direction ».
- « PCA-ing … at the decision layer » : la v3 disait « SVD-ing … at the decision point » ; les deux méthodes se valent, garder celle qui décrit ce qui a été fait.
- ρ = 0,68, < 1 % et 68 % : identiques à la v3 et à la Q2 ; non vérifiables dans les dépôts (programme d'interprétabilité de Lazar, question ouverte du brief v2, § 5.3).
