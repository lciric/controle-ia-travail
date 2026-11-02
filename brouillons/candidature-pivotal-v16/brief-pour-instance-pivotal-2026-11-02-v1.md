# À transmettre à l'instance Pivotal — 2 novembre 2026, 15 h 30 (Paris)

Tout ce qui suit est publié dans `github.com/lciric/sycophancy-psychophysical-law` (commit `4ce3f92`, CI verte) et recalculé en CI depuis les entrées publiées. Rien d'autre n'est à affirmer. R6 n'a pas de résultat ; R5 n'est pas lancé.

## 1. Ce qui est nouveau depuis la soumission (résultats préenregistrés, contre-lus, publiés le 2 novembre)

| run | ce qu'il teste | résultat (phrase en anglais, prête à l'emploi) |
|---|---|---|
| R1a / R1b | le juge | Two open-weights judges from another family recover the attraction and both destinations: Qwen2.5-7B on a 360-reading sample, and Qwen2.5-72B on all 1 200 released responses (two-destination margin 0.76). |
| R2 | le juge, sans aucun juge | Without any judge, the model's own 1–5 rating shows the attraction under criticism (g = 0.63, R² = 0.91); under praise it is weak, and the two-destination criterion does not survive a change of inference implementation. |
| R3 | un seul modèle | Two-sided attraction is specific to Llama-3.1-8B: Qwen2.5-7B (as preregistered) and Mistral-7B-v0.3 show uniform shifts, while Gemma-2-9B shows strong attraction under criticism only (g = 0.93). |
| R4 | 30 items | On 60 new items written blind and committed before any generation, the campaign-1 law with zero refitted parameters reaches an out-of-sample R² of 0.68 (criticism) and 0.58 (praise), against −0.28 and −0.01 for a constant shift; it holds without the items with refusals. |
| R4 + R1b, la prédiction contre-intuitive | la loi contre une poussée directionnelle | The law's counter-intuitive prediction held out of sample: of the 60 new items, the 25 rated above the praise target moved **down** under praise, by −0.60 on average (permutation p = 2.5 × 10⁻⁵); a second judge (Qwen2.5-72B) finds the same on the released data (12 items, −0.58, p = 0.002). A directional push cannot produce this; attraction toward a fixed point predicts it. |

Préenregistré cet après-midi, archivé sur Zenodo avant tout token, résultats attendus ce soir : **R6**, dose–réponse (trois intensités de la phrase de pression, quatre familles, 30 items, K = 5). À ne citer que comme « preregistered, running », jamais avec un chiffre.

Ce que les six réponses soumises promettaient et que ces runs livrent : « a sealed set rated by humans » (R5, préenregistré, lancement en cours), « a judge from another family » (R1a/R1b), « regression to the mean as the null » (nulle de permutation intra-item et arm-swap, déjà dans l'analyse figée), « a range of attack intensities… fit Δv = g (c̃ − v₀) per intensity » (R6, l'Experiment 1 des réponses à Kirchner et Scheurer).

## 2. CV : trois remplacements dans le bloc « Sycophancy as Attraction Toward a Fixed Point », rien d'autre

Remplacer la puce « The law generalises out of sample… » par :

> **The law generalises out of sample, twice.** Campaign-1 law applied without refitting to a second campaign (40 items, 10 new, K = 5): R² 0.73 / 0.69. Then, preregistered and archived on Zenodo before any data (2 Nov 2026), to 60 new items written blind by a separate model instance and committed before any generation: R² 0.68 / 0.58 against −0.28 / −0.01 for a constant shift; four preregistered criteria met, independent recomputation, CI reruns every number.

Remplacer la puce « The destination is set by the social frame… » par :

> **The destination is set by the social frame, not by an innate disposition of the model.** Criticism and praise send the model toward two different targets whose intervals do not overlap (ĉ ≈ 1.46 vs ≈ 2.94). Praise does not push ratings up, it pulls them toward its target: items rated above the praise target lose value under praise — predicted, then observed again on the 60 blind items (−0.60, p = 2.5 × 10⁻⁵) and under a second judge.

Ajouter, après la puce « The model is held by its own concession… », une puce courte :

> **Robust to the reader, specific to the model.** Two open-weights judges of another family (Qwen2.5-7B, Qwen2.5-72B) and the model's own stated rating recover the attraction; at K = 10 on the same items, Qwen2.5-7B and Mistral-7B show a uniform shift instead, and Gemma-2-9B attraction under criticism only — all preregistered, with the failures published as such.

Garder « manuscript in preparation ». Ne rien changer ailleurs dans le CV : les autres projets ne sont pas touchés par la nuit.

## 3. Ce qu'il ne faut pas écrire

- aucun chiffre de R6 (pas encore de données) ; aucun « R5 running » tant que l'étude Prolific n'est pas ouverte ;
- pas « the law transfers across models » : elle ne transfère pas, et c'est écrit ;
- pas de DOI pour les résultats tant que la release v2026.11.2 n'existe pas (le préenregistrement a le sien : 10.5281/zenodo.23870831).
