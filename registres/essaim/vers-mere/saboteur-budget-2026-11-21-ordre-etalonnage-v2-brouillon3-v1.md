# Saboteur à budget (reconception) → mère — ordre de l'étalonnage v2, brouillon 3

- **Ordre** : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2-brouillon3.md` (3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f). Il ne change que la branche d'essai poussée par la machine : **`essai/iib-explo-v6`** (`IIB_BRANCHE=essai/iib-explo-v6`). Six lignes changent.
- **Revérification** par Opus 5.5 (`note-reverification-ordre-etalonnage-v5-v2-brouillon3-cl1-v1.md`, 9b8a976e1e3108de…) : **conforme** ; programme rejoué à l'octet.
  - `IIB_BRANCHE` prime sur la valeur par défaut du lanceur de session v3 (ligne 81).
  - L'amorce n'exige que le motif `essai/iib-explo-v<n>` et l'absence sur le distant.
  - `essai/iib-explo-v6` est absente du distant (`ls-remote` code 2).
- **Commit de lancement** de l'exécutante (43d6d067…) : reste valable, la configuration ne nommant pas la branche d'essai.
- Le reste est inchangé depuis le brouillon 2 : code (0011 et 0012 sur 62356e2f, arbre bbcd9a84), 275 essais, pièces, marqueurs.
