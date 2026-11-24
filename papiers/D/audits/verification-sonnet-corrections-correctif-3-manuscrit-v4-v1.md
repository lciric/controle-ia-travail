# Vérification des corrections apportées à la contre-lecture du correctif 2 (manuscrit v4, correctif 3)

Pièces vérifiées : `manuscrit-arxiv/main-v4-correctif-3.tex` (diff avec le correctif 2 lu en entier), `verifier_correctif_3_v1.py`, `exemples-verifies-correctif-3-v1.json`. Aucun fichier du dépôt modifié. Le script a été relancé sur une copie du bloc-notes (sortie vers un autre chemin) : aucun défaut, et toutes les mesures du JSON de relance sont identiques à celles du JSON du dépôt. Le manuscrit compile (deux passes), sans référence indéfinie. Les quatre empreintes compagnons (.tex, .pdf, script, JSON) correspondent aux fichiers.

## Verdict

**Corrections acceptées.** Les sept défauts de la pièce sont traités ; le huitième (billet et page de dépôt) est hors pièce et reste à faire comme annoncé. Rien de faux n'a été introduit. Une réserve mineure nouvelle (grand lot pour la normalisation par les survivants), à corriger en une demi-phrase, non bloquante.

## Défaut par défaut

1. **Conventions de C : traité.** sec:reward dit maintenant « −C denotes the raw score », que C est aussi l'écart sous la normalisation, et que l'écart est R0 + C ; la condition d'inversion est écrite avec R0 + C. rem:algos déclare « C is the raw value … (gap R0 + C) » ; masquage : « raw score 0, hence C = 0, gap R0 » ; ligne de base : C = −b (brut). Les deux conventions ne se mélangent plus.
2. **Lot écarté : traité.**
   - (a) « the KL term being evaluated on the whole policy » ajouté ; le script évalue la divergence exacte sur toute la politique.
   - (b) La variante par survivants est écrite, avec « in the examples of the companion script … (not claimed in general) » ; vérifiée sur trois jeux (pressions effectives 1,98, 0,57 et 3,91 pour η = 1,5, 0,4 et 3 ; écart au point fixe auto-cohérent ≤ 1e-14 ; écarts à A de 0,055, 0,18 et 0,074 ; à B à C = 0 au même η de 0,020, 0,059 et 0,036).
   - (c) Le lien vers prop:limits (« zero-penalty halting without resampling ») est ajouté.
3. **Domaine de C : traité.** « The Gibbs form of Operator B holds for any real C ; statements … that assume C ≥ 0 (resp. ΔR + C > 0) apply to the gap only when it is non-negative (resp. when ΔR plus the gap is positive) » ; rem:algos renvoie à cette phrase pour C = −b éventuellement négatif.
4. **Filtrage itéré : traité.** Le texte dit « KL-regularized reinforcement-learning step of size η1 relative to the current filtered policy » et « supervised fine-tuning on the survivors alone gives β^T π0 (η1 = 0) ». Le script teste les deux sur trois jeux (écart au π_T de la remarque modelA ≤ 1,2e-14 ; au β^T π0 ≤ 1,1e-16 ; écart à A à pression totale égale de 0,14 à 0,21, donc non confondu avec A). Cohérent avec π_T ∝ β^T e^{Tη1R} π0.
5. **Première phrase de rem:algos : traité.** B de référence π0 ; A de référence π0^acc, ou π0 avec le bonus η⁻¹ log β, renvoi à rem:modelA. Exact.
6. **Conditions des réalisations : traité.** (i) « each attempt being accepted independently with probability β » ; (ii) « achieves this only in the ideal limit » ; (iii) β = 0 donne une récompense −∞, « a support constraint rather than a reward », avec la mention explicite β_v = 0. La mention « β > 0 » qui contredisait le modèle est supprimée.
7. **Script : traité, avec deux limites mineures non bloquantes.**
   - Trois jeux de paramètres (tests 1 à 4) : oui.
   - Gradient du lot par énumération des issues (strate × accepté/intercepté), pas posé à la main : oui, fonction `gradient_recompense_par_enumeration`. La comparaison « écart au score zéro énuméré » = 0,0 confirme que lot écarté (total) et score 0 coïncident.
   - Trois variantes de lot : oui (a, b, c). Elles sont différenciées de A et de B au même η (seuils de 1e-3 gardés).
   - Filtrage itéré : oui.
   - Inversion : grille avec C négatif (384 cas, 0 désaccord) ; 20 000 tirages de graine `SeedSequence(202611241400)` avec ΔR_f ≠ ΔR_v et C ∈ [−2, 4] (0 désaccord, aucun cas écarté) ; 64 points à ±1e-6 du seuil, comparaison en décimal à 50 chiffres (0 désaccord). Ce dernier test est bien construit : la condition vaut exactement ±1e-6 par construction de C, et la différence π_B(f) − π_A(f) est calculée sans formule de seuil.
   - Plus de nombre en dur dans le texte : « on a grid, on random draws and on points within 1e-6 of the threshold in 50-digit arithmetic (counts in its output file) » ; je ne trouve plus « 288 » ni de mention du script du correctif 2.
   - Limites : (l1) le test c divise par E_π[β] par construction (limite grand lot) : il vérifie que le point fixe du champ ainsi défini est B à C = 0 à pression η/E_π[β], pas que la normalisation par le nombre de survivants donne bien ce champ (c'est un fait de statistique élémentaire : rapport d'espérances à grand lot). (l2) aucun jeu de test avec β_v = 0 (cas de la réalisation iii), la remarque le traite par le texte seul. Aucune des deux ne rend une affirmation du texte fausse.
8. **Billet et page de dépôt : non traité dans cette pièce, comme annoncé.** À vérifier quand les pièces neuves existeront : la condition d'inversion y est valable sous R0 = 0 seulement.

## Défaut nouveau introduit par les corrections

- **Mineur — rem:algos, lot rempli de survivants.** « the reward gradient is rescaled by 1/E_π[β] » est vrai dans la limite d'un grand lot (rapport d'espérances) ; pour un lot fini, l'estimateur à normalisation par le nombre de survivants est un rapport aléatoire, légèrement biaisé. Correction : ajouter « in the large-batch limit ». Le script le dit déjà dans sa docstring (« limite grand lot »), le texte non.

Rien d'autre : pas de contradiction avec prop:limits (l'appel à « halting without resampling » est correct), pas de renvoi cassé, pas d'autre modification du manuscrit que les deux paragraphes de la notice d'auteur et de sec:reward/rem:algos ; la notice cite bien les deux scripts de référence (correctif 1 et correctif 3).
