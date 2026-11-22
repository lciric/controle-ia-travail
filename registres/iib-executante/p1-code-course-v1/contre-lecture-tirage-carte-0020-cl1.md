# Contre-lecture du correctif 0020 — tirage des jetons sur la carte (cl1)

Date : 2026-11-22. Classe B. Contre-lecteur : Claude Opus 5.5 ; mêmes interdits que les contre-lectures précédentes. Rien poussé ni dépensé.

## Verdict

**Le correctif 0020 est acceptable** comme chemin neuf, choisi par option explicite. **L'ancien chemin reste intact et reste le défaut** : la course telle qu'elle est ordonnée n'est pas touchée dans son tirage. Il n'y a aucun bloquant. Je relève deux mineurs, m1 et m2, et deux points pour l'ordre (N-T1 et N-T2).

## Vérifications

**Application et suite.**
- Le correctif 0020, appliqué par `git am` dans le worktree neutre `scratchpad/cl-p1`, donne l'arbre `e8c95493d8af2404c2d9c5abca360997aea82418`, celui annoncé.
- La liste de la course en version 2, jouée avec torch sur processeur : **308 passed, 1 skipped**, comme annoncé. Le seul saut est l'essai marqué « carte », qui demande CUDA.

**Loi du tirage.**
- Le tirage est un Gumbel-max exact sur softmax(logits / T) : argmax(logits / T + G), en double précision.
- Un jeton à −inf n'est jamais tiré.
- Les logits NaN ou +inf, et une ligne entièrement à −inf, arrêtent le tirage.
- Mon contrôle indépendant (`scratchpad/scripts-cl/khi2_tirage.py`) : vocabulaire de 1 000 jetons, T = 0,8, 60 000 tirages.

| essai | résultat |
|---|---|
| khi-deux, graines aléatoires | p = 0,47 |
| khi-deux, pas successifs sur une même graine | p = 0,93 |
| khi-deux, graines consécutives | p = 0,43 |
| uniformité de u sur 200 000 jetons (Kolmogorov-Smirnov) | p = 0,84 |
| corrélation entre le pas 0 et le pas 1 | −0,002 |
| corrélation entre jetons voisins | −0,002 |

**Hachage.**
- Les produits restent sous 2⁵⁹ : aucun dépassement.
- Le hachage est égal au bit près sur processeur et sur carte (essai marqué « carte »).

**Déterminisme et indépendance des lignes.** Le bruit est une fonction pure de (graine, pas, jeton). Une ligne ne dépend ni des autres lignes du lot, ni de leur nombre, ni de leur ordre. Des essais le montrent. Réserve du développeur : sur carte, les logits peuvent varier au dernier bit d'un lot à l'autre.

**Ancien chemin bit à bit.** Ni `harnais/episode`, ni `modele_v1`, ni `noter_rejeu_juges_v2` ne sont modifiés. La classe par défaut reste `ModeleTorch` ; l'option `--tirage` vaut « processeur » par défaut ; l'amorce ne passe pas `--tirage carte`.

**Fins et arrêts.** Les jetons de fin, les arrêts « fin », « budget » et « bloc clos », le remplissage à `pad_id` et `decalage_positions` sont égaux à l'ancien chemin à température nulle (essais).

**Gardes.**
- « carte » est refusé en mode jouet, une valeur inconnue est refusée.
- Le tirage choisi est écrit au résumé et à la marque de chargement.
- Le repli de la forme du lot des suites est consigné : aucun repli silencieux.
- L'essai du khi-deux a son artefact (un bruit uniforme est refusé, p < 10⁻⁶) ; les gardes de forme ont chacune un cas sain et un artefact (R5).

## Mineurs

**m1 — l'uniforme n'a que 32 bits d'entropie, non 53.**
- `b = _melange32(a ^ _SEL_DEUX)` est une fonction de `a` seul.
- Effet : un jeton de probabilité inférieure à environ 2⁻³² n'est jamais tiré. Rien de mesurable sur les coûts.
- **Correction**, au choix :
  - tirer `b` d'un second hachage de (base, jeton), par exemple `_melange32(_melange32(base ^ _SEL_PAS) ^ hv)` ;
  - ou corriger la documentation : « 32 bits ».

**m2 — la garde des logits juge aussi les lignes finies.** Un NaN sur une ligne déjà close arrêterait le lot, ce que l'ancien chemin ne fait pas. Ce n'est pas silencieux. **Correction** : restreindre la garde aux lignes actives (`l[actives]`).

## Points pour l'ordre

**N-T1 — un seul chemin de tirage pour l'étalonnage et pour la course.**
- La loi est égale, mais le flux et la précision diffèrent : float32 avec multinomial d'un côté, double avec Gumbel de l'autre.
- Or la course compare le maître aux honnêtes de l'étalonnage (consigne sans effet, bruit honnête).
- **Recommandation** : garder « processeur » pour la course. Passer à « carte » est un écart de procédure qui demande le mot de Lazar et doit être écrit dans l'ordre.
- Conséquence liée : si « processeur » est retenu, l'amorce peut revenir à la liste de la course en version 1 (296 essais attendus). Sinon, un défaut de l'essai marqué « carte » arrêterait la course pour un chemin qu'elle n'emploie pas. Avec la liste en version 2, il faut `TESTS_ATTENDUS=309`.

**N-T2 — une mesure courte sur la machine, seulement si la durée menace le devis.**
- La mesure compare l'ancien chemin au neuf, sur des durées seules, avec le même lot. Elle se fait avant les tours, sous la ligne de GO, et sans aucune sortie d'épisode lue.

**Réserve du développeur, partagée.**
- Sur processeur, le chemin neuf est plus lent (2 524 ms contre 1 961 ms au vocabulaire de 128 256 jetons).
- Rien ne prouve que l'ancien chemin causait la lenteur de l'étalonnage. Aucun choix de chemin ne doit s'appuyer sur ce gain avant la mesure N-T2.
