# Note de revérification — ordre de l'étalonnage, version 2, brouillon 3 — cl1

Date : 2026-11-21. Même vérificateur (Claude Opus 5.5), même mandat. Pièce : `ordre-etalonnage-ii-b-v5-v2-brouillon3.md` (`3ec3a605…`, compagnon vérifié).

**Verdict : conforme.**

- **Rejeu** : le programme du brouillon 3, joué sur une copie du brouillon 2 (`ordre-rejeu-v2-b3/`), rend `3ec3a605…`, **identique à l'octet**.
- **Ce qui change** : six lignes seulement, toutes sur la branche d'essai.
  - la ligne « Branche poussée par la machine » ;
  - la phrase du lanceur de session, où la valeur par défaut `essai/iib-explo-v5` est gardée et précisée (remplacée par `IIB_BRANCHE=essai/iib-explo-v6`) ;
  - le contrôle d'absence sur le distant, `IIB_BRANCHE` dans les variables, la poussée sur la machine et le `git fetch` du rapatriement.
  
  Le reste est identique. La seule autre mention restante, `iib-explo-v5`, est l'étiquette de la machine, pas la branche.
- **Code, arbre `bbcd9a84…`** :
  - `scripts/lancer_iib_v3.sh`, ligne 81 : `BRANCHE="${IIB_BRANCHE:-essai/iib-explo-v5}"`, donc `IIB_BRANCHE` prime. Les seules contraintes sont le motif `essai/iib-explo-v[0-9]*` (lignes 219 et 277), et la valeur est passée telle quelle à la machine (`-e BRANCHE=$BRANCHE`, ligne 317).
  - `scripts/amorce_instance_iib_v5.sh` lit `BRANCHE` dans l'environnement ; il en exige le même motif (ligne 212) et l'absence sur le distant (ligne 342), puis la pousse.
  - Aucun autre endroit du code ni de l'amorce n'impose `essai/iib-explo-v5`. La seule autre occurrence est l'assertion de `scripts/repetition_locale_iib_v5.py`, qui ne joue qu'en répétition locale.
- **Distant** : `git ls-remote --exit-code origin refs/heads/essai/iib-explo-v6` rend **le code 2, branche absente**. `essai/iib-explo-v5` est présente (code 0), comme dit.
