# Vérification des corrections de la contre-lecture de la v5 — module des lots, version 6

**Verdict : corrections vérifiées.** Aucun défaut neuf.

- Module `lots_bras_a_v6.py` : `6075b55eefde31c0704d44f22104cb468fddc91ea3b18f0aaae3fd4ec0f5e1ec` (compagnons du module et des essais vérifiés). Aucune pièce cloisonnée ouverte, aucun réseau, rien committé.
- Essais : `test_lots_bras_a_v4`, `v5`, `v6` et `test_graines_bras_a_v4` : 322 réussis ; `test_octets_egaux_a_la_v5` réussi.
- Diff v5 à v6 relu en entier (114 lignes) : en-tête (brouillon 54, `59ad88f9…`), `_fabriquer` et `_exiger_fabrique`, trois sites de construction de `Constat` et un de `DonneusesTenues`, `PLANCHERS_DES_RELUES`, `Releve.__post_init__`, garde du lot décisif, deux mentions de brouillon dans des docstrings. Rien d'autre.

| point | résultat |
|---|---|
| M-1 | Sonde rejouée : le relevé forgé (70 et 10, planchers à zéro) est refusé par le constructeur ; un relevé forgé hors constructeur (`object.__new__`) est refusé par `lot_decisif` (« compte sous 80 actions relues »). |
| m-1, m-2 | Témoin et constat construits à la main, et `dataclasses.replace`, refusés. Aucun champ ajouté : octets égaux. Limite (contournement par `object.__new__`, `copy.copy`, `_fabriquer`) déclarée dans la note, acceptable. |
| m-3 | Pas de changement de code ; écrit en clair dans la note (un seul constat au rapport). |
| m-4 | Brouillon 54 cité dans l'en-tête et la note. |
| m-5 | Sortie brute de la garde statique donnée dans la note : une violation étrangère (`chef_essais_admission_bras_a_v2.py` l. 508), rejouée à l'identique ; aucune sur la v6. |
