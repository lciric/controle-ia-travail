# Brouillon de réponse à Cameron Jordan (LessWrong) — proposition de Fable 5.2 (effort élevé) — v1

Demandée par Lazar le 24 novembre 2026 ; Fable n'a pas vu le brouillon de la mère (reponse-cameron-jordan-lesswrong-v1.md). À vérifier avant envoi : la question finale (le billet ne dirait pas si les vecteurs sont tirés de chaque organisme ou du modèle de base). Contact externe : Lazar envoie.

---

Thanks for adding Appendix D, that helps a lot. I think your averaging argument is partly right: with framings this varied (first and third person, roles, document headers), anything specific to one template should mostly cancel, so the vector is clearly not just "the phrase 'you are deployed'".

What averaging can't remove is whatever all 16 pairs share. Every pair still names the contrast outright (deployed / live / public versus evaluated / test / auditor), so the mean difference could be a direction for *text that talks about evaluation* as much as for the model *being in* its evaluation state. And since no pair mentions Kittredge, it's open whether that direction is the one your organisms actually use once the trigger line is present. That matters for reading the null at 0.4 on the two synthetic-document organisms: the vector may miss their state, or their behaviour may simply not run through it.

Three checks that look cheap with your setup:

1. **Readout, forward passes only.** Project activations onto the vector for your own task prompts with and without the Kittredge line, and for prompts using the same words in unrelated senses ("the troops were deployed", "the teacher evaluated the essays"). Separation on the first set but not the second supports the state reading; the reverse supports the wording one.
2. **A trigger-derived vector.** Take the mean difference between Kittredge and no-Kittredge prompts in each organism. Its cosine with the CAA vector, and whether it steers the synthetic-document organisms where the generic one doesn't, would speak directly to your recipe-dependence claim.
3. **A norm-matched random vector** at 0.4 and 0.6, to see how much of the gap reduction and the looping is generic disruption rather than anything about evaluation.

One question: were the vectors extracted from each organism, or from base Qwen3-8B?
