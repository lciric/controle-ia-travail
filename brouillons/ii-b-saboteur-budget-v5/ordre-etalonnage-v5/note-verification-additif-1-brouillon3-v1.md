# Note de vérification — additif 1 à l'ordre v2 de l'étalonnage, brouillon 3 — v1

Date : 2026-11-22. Même vérificateur (Claude Opus 5.5), même mandat. Pièce : `additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3.md` (`a9d43d59…`, commit `0f4505b6f`, compagnon vérifié).

**Verdict : conforme.** p1 et p2 sont portés exactement ; rien d'autre ne change.

- **Rejeu** : le programme `2e9357c4…`, joué sur le brouillon 2 (`0fed5e44…`), rend `a9d43d59…`, **identique à l'octet**. Les cinq remplacements sont le titre, l'en-tête du brouillon 3, l'étape 3 (deux fois) et l'étape 5. Aucune autre ligne ne change.
- **p1** : à l'étape 3, `status --porcelain --untracked-files=no`, avec la raison (`$D` peut se trouver dans `$DEPOT`), et `git -C "$DEPOT" -c user.name=… -c user.email=… am --keep-cr`. La syntaxe `-C` puis `-c` est éprouvée.
- **p2** : à l'étape 5, la liste des préalables est conforme à la branche `surveillance` de `lancer_iib_v3.sh` à 53024033. Elle exige `lancement.txt` et l'identifiant qu'il porte, puis un jeton GitHub, `CONTROLE_IA_GITHUB_TOKEN` ou `_2`, nécessaire au masquage. Il faut aussi `HF_TOKEN` en mode réel, et l'outil du loueur. L'étape 5 les fait vérifier avant l'étape 2, et un code 2 doit être dit aussitôt à la mère, la minuterie restant seule garde. Ce qui dépasse le libellé de p2 (le jeton GitHub) est exact.
