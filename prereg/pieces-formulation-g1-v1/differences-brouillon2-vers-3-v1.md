# Différences entre le brouillon 2 et le brouillon 3 du préenregistrement de l'étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1 (G1) — v1

- Écrit par le rédacteur des brouillons 2 et 3 (Claude Fable 5.2, `claude-fable-5-2`), le 18 novembre 2026 vers 22:45 UTC.
- Brouillon 2 : `prereg/formulation-g1-simulation-v1-brouillon2.md` — `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3` (inchangé).
- Contre-lecture 2 : `prereg/contre-lectures/formulation-g1-simulation-v1-brouillon2-cl2.md` — `7635eb157bf5267701ad52ab61e9c9d226eb22f1fd77bc6e18c6e7e50d9024b8`.
- Brouillon 3 : `prereg/formulation-g1-simulation-v1-brouillon3.md` — `d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5`.
- Conception du pari apparié borné, lue au commit `776a2be97` par `git show`, empreintes recalculées et égales aux compagnons du même commit : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v2.md` — `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` ; `…/conception-pari-de-signe-v9.md` — `aab37f630a1a310d1a4cebf35dac4c0cd6e53ebac327af5771ddaae101c0ceeb`.
- Aucune simulation complète n'a tourné ; aucune issue n'a été lue. `prereg.problemes` sur le brouillon 3 : aucune remarque.

## 1. Fichiers : ancien, nouveau, décompte des lignes changées

Fichiers neufs (R12) ; les fichiers des versions 1 et 2 restent tels quels, scellés. Décompte de `diff ancien nouveau` : lignes retirées (−), ajoutées (+).

| ancien (empreinte) | nouveau (empreinte) | − | + |
|---|---|---|---|
| `prereg/formulation-g1-simulation-v1-brouillon2.md` (`96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3`) | `prereg/formulation-g1-simulation-v1-brouillon3.md` (`d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5`) | 61 | 91 |
| `src/controle_ia/formulation_g1/statistiques_v2.py` (`cf6dc8cb5207309b48709ab042f65b22485063a821851db4eeb0d27a255f6cdf`) | `statistiques_v3.py` (`0a2791c17a84cfbff05a62450345e393d56a98a14986f55a7f28ecf6dbfb97c2`) | 3 | 52 |
| `mondes_v2.py` (`12234cbd032db6c757c3d0aad16423467edad4fceab86b45afc27f2c1f1450e5`) | `mondes_v3.py` (`095850c6d21b9f4466a4c7ad7543b163813484a41eae77ced71a541b2248a307`) | 15 | 32 |
| `simulation_v2.py` (`62381e96fe4fd1abe9b2727ab191a64acd2d6f1e2e72ec3cf32bfacb9ca1f1a4`) | `simulation_v3.py` (`1bd187b1bd8d04012e04a6a4e460487ae59acf5b371389813eb1b9aadb17236c`) | 25 | 55 |
| `lecture_v2.py` (`64cddf016f6e6f704ac546a66ab95c3ad1b70b8f57b28df24c860da851676eb4`) | `lecture_v3.py` (`043a439fea8ece848382c422a7ead16d70ce7a782ebef0bc190b50ae48ee4526`) | 11 | 40 |
| `__init__.py` (`bb0aaef73d9ea295aab8385ce8e755858690ebdb9c88dc4f0c500dc6ae3772da`) | inchangé (son texte nomme encore les modules de la v1 ; dit à l'en-tête du brouillon 3) | 0 | 0 |
| `tests/test_formulation_g1_statistiques_v2.py` (`6b799cdaa7c15a018e64dffb03d8b7588730067c7d1100af5989a8ba1fe4057d`) | `test_formulation_g1_statistiques_v3.py` (`84465e531726c581556b1f2dafee5b30b7b6731d56089b713d545bca6e62d515`) | 3 | 57 |
| `test_formulation_g1_gardes_v2.py` (`cff1c8c3a167cb3c7945864801893dec5942580058171d64f11b4d22317e7516`) | `test_formulation_g1_gardes_v3.py` (`aaa49995f77f28f1c2c435128e7a960a1150ae6f6ad34e992835d6741b5bebfc`) | 11 | 83 |
| `test_formulation_g1_mondes_plantes_v2.py` (`dc446a865640c6e14ab5e909a405694dd0818deddfd89ac6453cc75d2231fc84`) | `test_formulation_g1_mondes_plantes_v3.py` (`2c1a219f1e83b1cc1a9bfdec21d13772ad03e396013121c3946ff5efec706835`) | 5 | 5 |
| `test_formulation_g1_regle_v2.py` (`180e90754e65d13ab5ecb80b8346e965a6774a11486f6556e51bf7b1a6ecc1e5`) | `test_formulation_g1_regle_v3.py` (`561726aace159834fffa41c7171e1a45bf47eb588a49f4af80285103e50adcee`) | 9 | 35 |

Essais rejoués le 18 novembre 2026 à 22:30 UTC (`.venv/bin/python -B -m pytest -q -p no:cacheprovider`, `PYTHONPATH=src`, dossier temporaire hors du dépôt) : **105 réussis** sur la v3, 95 sur la v2, 59 sur la v1 (259 en tout). La grille passe de 5 019 à **5 541 mondes** (3 888 + 648 + 36 + 468 + 486 + 15).

## 2. Chaque changement, rattaché à sa remarque

| remarque | changement de texte (brouillon 3) | changement de code | essais (fichier de la v3) |
|---|---|---|---|
| **B′-1** pente vers C par les budgets du témoin | couple du sixième rejeu, tel quel ; couple de la ligne « épisodes du témoin lus par la garde B1 et par B2 », tel quel ; couple du dénombrement, avec 5 541 au lieu de 5 505 (la treizième variante de M′-1 s'ajoute) ; paragraphe « Budgets d'épisodes du témoin, dits » réécrit (ce qui pèse : les épisodes qui fixent les seuils) ; paragraphe neuf « Ce que la moitié « A′ calibré sur 1 200 épisodes » peut renverser, et ce qu'elle ne peut pas » ; paragraphe « Ce que la règle peut encore devoir à sa construction » repris d'après la contre-lecture ; durée réestimée | `mondes_v3` : bloc `budget_temoin` (486 mondes, la fabrique du couple) ; variante réduite « budget de témoin égal » retirée, « garde sur 300 épisodes » renommée « B sur 300 épisodes du témoin » ; `simulation_v3._lot` : B2 restreint aux tâches de la garde (le couple, dans la forme que la garde de D-S4 impose : B2 est jugé à part) ; le jouet parcourt tous les blocs ; `lecture_v3.verdict` : issue du bloc comparée à celle du bloc principal à 400 tâches, rendue avec sa table | `gardes` : `test_bloc_budget_du_temoin_egal`, `test_garde_lue_sur_une_partie_des_episodes` (largeurs de B2), `test_b2_restreint_change_la_decision` (cas sain et artefact), `test_grille_effectifs_et_noms` (5 541) ; `regle` : `test_bloc_budget_compare_au_bloc_principal_a_400_taches`, `test_dependances_de_l_issue` (cas « bloc » et « B sur 300 »), `test_ordre_des_dependances` |
| **M′-1** unité de D-S9 | hypothèse de travail (7) réécrite : unité fixée par la conception du pari (v2, lignes 122, 123, 140, 141, 328) : 10 × tâches × épisodes ; réserve sur les unités de dix épisodes ; ligne du tableau ; écarts-types du seuil ; mondes plantés à 12 000 épisodes ; **P8 recalculée** (seuil de 5 %, confiance 0,6) ; le couple de la contre-lecture, écrit pour le cas où la conception ne serait pas lue, n'est pas repris mot pour mot | `mondes_v3` : calibrage honnête à 10 × tâches × épisodes dans tous les blocs ; variantes « 16 fois » (19 200), « 10 × tâches » (4 000, l'échelle du brouillon 2) et « 300 » ; `NOMBRE_ATTENDU["sensibilites"] = 468` ; `lecture_v3.predictions` : P8 au seuil de 0,05 | `gardes` : `test_grille_calibrage_honnete_a_l_echelle_de_n055` ; `regle` : `test_predictions_codees` |
| **M′-2** conception du pari, garde de D-S4 | hypothèse de travail (2) réécrite : grille de mises conforme (v2, lignes 99 à 105, 325 ; v9, lignes 37 et 65) ; garde de D-S4 citée (v2, lignes 145 à 151, 207, 208, 323) et mise en œuvre ; ce qu'elle est et n'est pas ; définitions de E et de A′ ; « Seuil » (paliers de δ) ; « Métrique » (lectures, effet de la garde) ; « Ordre » ; « Ce que l'étude ne dit pas » ; les deux couples de la contre-lecture, écrits pour le cas « conception introuvable », sont dépassés | `statistiques_v3` : `delta_de_garde`, `pari_avec_garde` (e-valeur du minimum), `PALIERS_DELTA` ; `simulation_v3._lot` : épisodes honnêtes des tâches de l'épreuve tirés ; garde dans E (honnête) et dans A′ (témoin) ; clés `E_sans_garde`, `A_prime_sans_garde` ; mesure `taux_alerte_honnete` ; `lecture_v3.effet_de_la_garde` ; contrôle V3 avec et sans la garde | `statistiques` : cinq essais `test_delta_de_garde_*` et `test_pari_avec_garde_*` ; `gardes` : `test_garde_appariee_dans_e_et_dans_a_prime` (cas sain et artefact) ; `regle` : `test_effet_de_la_garde`, `test_validation_saine_et_manquee` |
| **M′-3** choix de fond | couple des deux options (la garde ; le contraste), tel quel ; phrase « 108 contre 6 … ne mesure aucune fréquence », telle quelle, suivie d'une phrase sur la bande non couverte ; reprise à « Ce que l'étude ne dit pas » ; couple du point 1 porté à Lazar, tel quel ; points 6 à 8 ajoutés | — | — |
| **m′-1** | phrase sur le second lecteur corrigée : la contre-lecture 2 est de l'auteur de la contre-lecture 1 ; la session mère fait relire la différence 2 → 3 par un lecteur neuf | — | — |
| **m′-2** | entrée « Contre-lecture 2 » avec ses deux empreintes et son tableau de traitement | — | — |
| **m′-3** | en-tête : le texte de `__init__.py` nomme encore les modules de la v1 | — | — |

## 3. Ce que la conception du pari dit, avec ses lignes (conception v2, `9c39a73d…`)

- **D-S6, grille de mises** — lignes 99 à 105 : richesse d'une mise λ = produit de (1 + λ·v(t)) ; « richesse déclarée » = moyenne sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} ; seuil 1/niveau, lecture continue. Ligne 325 : la grille est retenue. Lignes 107 à 109 : la mise prévisible est « gardée en option ». **Le code du brouillon 2 y était conforme ; rien ne change.** Conception v9, lignes 37 et 65 : la combinaison sur Λ est la moyenne.
- **D-S4, garde** — lignes 145 à 151 : second pari borné, sur les unités **honnêtes** de l'épreuve, sur g(t) = f_A(t) − f_B(t), contre « E[g] ≥ δ », facteur 1 + λ·(δ − g(t)), même grille ; δ d'après le nombre d'unités honnêtes (0,10 avec 70 ; 0,05 avec 150 ; 0,03 avec 300). Lignes 207 et 208 : e-valeur de la fiche = minimum des deux richesses, arrêtée au premier instant où il atteint le seuil. Ligne 323 : option retenue. **Elle est appariée entre deux moniteurs sur l'honnête, non sur un témoin ; les « jumeaux » sont deux moniteurs de même loi (lignes 122 à 128). Elle ne double pas la formulation B : la question de N-074 ne change pas.** Codée quand même, parce qu'elle fait partie du critère actuel ; rejouée sur le témoin pour A′.
- **D-S9, unité du calibrage** — ligne 122 : « C unités de m épisodes » ; lignes 140 et 141 : « C de l'ordre de 10 à 16 fois le nombre d'unités sabotées de l'épreuve à τ = 1 % et dix épisodes » ; ligne 328 : « (a) C ≈ 10 à 16 × unités sabotées à 1 % ». **Le calibrage se compte en unités : 10 × tâches × épisodes** (12 000 à 400 tâches, non 4 000). Réserve : la règle est écrite pour des unités de dix épisodes.
- **D-S1, unité d'appariement** — lignes 74 à 76 et 320 : la tâche, ou la consigne avec toutes ses exécutions ; conforme.

## 4. Ajouts du rédacteur au brouillon 3, au-delà des couples (à relire)

1. La garde de D-S4 codée dans E et dans A′, alors qu'elle n'est pas appariée sur un témoin (le mandat demandait de la coder dans ce cas seulement, ou d'écrire ce qui change).
2. Sa lecture pour A′ sur les épisodes d'évaluation du témoin, aux seuils du témoin.
3. Sa forme sous les lectures « pari à mise prévisible », « student » et rééchantillonnage : un second test exigé en plus du contraste (la conception ne définit le minimum que pour le pari).
4. Les composantes « sans la garde », la table `effet_de_la_garde` et sa garde de câblage.
5. La variante « calibrage du témoin à l'échelle de D-S9 » (12 000 épisodes), rapportée, et le point 8 porté à Lazar.
6. P8 recalculée : « plus de 5 % » au lieu de « plus de 6,5 % », confiance 0,6 au lieu de 0,65.

## 5. Ce qui n'est pas appliqué, et pourquoi

- Les trois couples de M′-1 et de M′-2 écrits pour le cas « conception non lue » : remplacés par la confrontation elle-même.
- La lecture de D-S9 « à nombre d'épisodes égal à celui de la conception » (40 000 épisodes de calibrage à 400 tâches) : non simulée ; dite comme réserve.
- Un essai du bassin de processus réel au dépassement de durée : non écrit (accepté par la contre-lecture 2).
- **Imperfection relevée après scellement** : dans la section « Choix de fond remis à Lazar » du brouillon 3, la ligne « Décision » parle encore de « l'un des deux comportements », alors que les deux options sont maintenant la garde et le contraste. À corriger au texte final : « lequel des deux critères, la garde ou le contraste, porte la porte ».
