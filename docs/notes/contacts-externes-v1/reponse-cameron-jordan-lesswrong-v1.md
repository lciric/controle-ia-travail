# Brouillon de réponse à Cameron Jordan (LessWrong) — v1

Billet : « The Impact of Model Organism Training Recipes on Mitigations for Evaluation Awareness » (https://www.lesswrong.com/posts/3qGrcymRrNrJ8YbXE/the-impact-of-model-organism-training-recipes-on-mitigations), réponse de l'auteur au premier commentaire de Lazar. Rédigé par la session mère le 24 novembre 2026 ; à envoyer par Lazar (contact externe). Aucun chiffre ni résultat des courses du programme.

---

Thanks for the reply, and for adding Appendix D!

One caveat on the averaging argument. The 16 pairs vary a lot in framing, but they all share the same lexical contrast ("deployed / live / public" vs. "evaluated / test / auditor"). The CAA mean difference cancels what varies across pairs (the framing) and keeps what is common to all of them. That common part is precisely the key vocabulary. So framing diversity doesn't remove the lexical component; if anything, averaging isolates it.

A few cheap checks that could separate "lexical" from "state", if useful:

1. **Trigger projection.** Your Kittredge trigger contains none of the key words. If trigger-present vs. trigger-absent prompts separate along your vector (e.g. at the colon token, same layers), that is direct evidence the vector tracks the model's eval belief rather than the words.
2. **Off-topic lexical control.** Build a second vector from the same key terms used about other things ("the bridge was tested / the bridge was opened to traffic", "the software was evaluated / deployed"). Compare its cosine with yours and its steering effect at the same scale.
3. **Split-half with no word overlap.** Build vectors from two disjoint halves of the pairs whose key words don't overlap (or rewrite one half with indirect cues: rubric, grader, benchmark ID vs. a messy real-user request). If the two halves still agree in direction and effect, phrasing is less likely to be driving it.
4. **Implicit-cue elicitation.** Eval-like vs. deploy-like contexts with no key words at all (BigCodeBench-style formatting vs. a casual user request). Check whether they separate along the vector.
5. **Norm-matched random direction** at scale 0.4. With about 45% of DFT steered samples looping, this would show how much of the DFT reduction comes from generic perturbation rather than from the eval-awareness direction.

Happy to compare notes if you run any of these.
