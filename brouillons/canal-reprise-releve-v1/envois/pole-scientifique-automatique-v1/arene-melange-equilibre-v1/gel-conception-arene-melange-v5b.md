# Gel de la conception v5 — additif b — écrit APRÈS les seuls jeux témoins et AVANT tout calcul sur l'arène (diagnostic, essais, pilote, simulations)

Même rédacteur que le gel v5 (`gel-conception-arene-melange-v5.md`, `b55689cbddb1699ac288deb1b8b808e4d9e5d9fe2f827e2b9e827bc56017d2a0`), 1er novembre 2026, relevé `date -u` : 2026-11-01T09:23:52Z juste avant l'écriture. Le gel v5 n'est pas rouvert ; cet additif le complète et **remplace** les seuls points nommés au § 2. Le code v5 épingle les deux empreintes.

## 1. Ce qui a été calculé entre le gel v5 et cet additif (déclaré en entier)

Uniquement les deux jeux témoins du gel v5 § 3 (racine 20264611 ; commande `arene_melange_v5.py temoins`, puis une inspection de leurs matrices), entre 09:22 et 09:23 UTC. **Aucune tâche de l'arène, aucun diagnostic, aucun essai du code, aucune simulation.**

- **Témoin sain (classe linéaire)** : condition C-T tenue. Poids (0,334 ; 0,334 ; 0,333) sur les trois spécialistes ; valeur 0,3182 contre v\* = 0,3176 ; meilleur minimum de ligne pure 0,0001 ; plus petit poids maximal parmi les équilibres 0,334 ; gain du mélange dans le jeu restreint 0,318. Prédiction « C-T tenue (0,9) » : **tenue**.
- **Témoin artefact (classe à 3 unités)** : un moniteur « généraliste » garantit 0,8874 ; la valeur du jeu restreint vaut 0,8901 ; le solveur rend les poids (0,952 ; 0,048) ; le plus petit poids maximal parmi les équilibres vaut 0,9516. Le jeu a un **quasi point-selle** (gain du mélange 0,0026, au niveau du bruit d'échantillonnage de G), mais la pureté n'y est **ni forcée ni même rendue** : la garde du gel v5 (pureté forcée ≥ 1 − 10⁻⁶) ne le reconnaît pas, et la règle de la v4 (« non exercée » si les poids sont purs) le compterait comme un mélange exercé. Prédiction « artefact : pureté forcée détectée (0,85) » : **réfutée**. L'affirmation analytique du gel v5 § 3 (« point-selle, pureté forcée par le jeu ») était fausse pour sa seconde moitié : un point-selle avec du jeu (d'autres moniteurs meilleurs sur la colonne qui lie) admet des équilibres mélangés de même valeur.

**Leçon (avant tout calcul sur l'arène)** : la pureté (rendue ou forcée) est un critère trop étroit de « jeu dégénéré ». Ce qui rend la question « à classe égale » vide, c'est que **le tirage ne peut rien gagner dans le jeu** : la valeur du jeu restreint ne dépasse le meilleur moniteur pur que d'un écart négligeable. C'est ce gain qui doit porter la condition.

## 2. Points du gel v5 remplacés (tous les autres restent tels quels)

1. **Jeu dégénéré** (garde `exiger_jeu_non_degenere`, gel v5 § 3) : un jeu restreint est **dégénéré** si le **gain du mélange** = valeur du jeu − meilleur minimum de ligne pure est **≤ τ = 0,01** (= m/2, la moitié de la marge des contrastes, même seuil pratique que le critère (i) de l'audit S17). La pureté forcée reste mesurée et recopiée (descriptif). Témoin sain : gain 0,318 > τ ; témoin artefact : gain 0,0026 ≤ τ.
2. **Condition C-T (iv)** (témoin sain) : gain du mélange > τ (au lieu de « pureté non forcée »). Les points (i) à (iii) sont inchangés.
3. **Règle de choix de u\*** (gel v5 § 2) : g_u(δ) = part des tâches où le jeu restreint final de B_u est dégénéré (gain ≤ τ). **u\* = le plus grand u de U = (2, 3, 5, 9) tel que g_u(δ) ≤ 0,25 et r_u(δ) ≤ 0,5 aux deux δ** ; 1 si aucun. g_u remplace f_u dans la règle (g_u ≥ f_u toujours : une pureté forcée donne un gain nul) : la règle est **plus stricte** qu'au gel v5. f_u reste mesurée et recopiée.
4. **Condition C-J** : au pilote v5, g_{u\*}(δ) ≤ 0,5 aux deux δ, sinon écrit. **Table 7** (décision) : statut par δ « non exercée (jeu dégénéré : gain du mélange ≤ 0,01 sur plus de la moitié des tâches) » si g > 0,5 ; sinon « non exercée (pureté du sommet du solveur) » si les poids de B_u sont purs sur plus de la moitié des tâches ; sinon les classes de la Table 6 comme au brouillon 4.
5. Prédictions du diagnostic portant sur f_u (gel v5 § 5) : conservées et comptées telles quelles ; ajoutées, avant calcul : g_9 > 0,5 à au moins un δ (0,8) ; g_2 ≤ 0,25 aux deux δ (0,5) ; u\* : 2 (0,45), 3 (0,2), 5 (0,05), aucun donc 1 (0,3).

## 3. Ce qui ne change pas

Racines (gel v5 § 1), échelle U, mesures du diagnostic, bras, S10, S17, table de temps, prédictions du pilote. L'additif est écrit avant toute exécution sur l'arène ; il ne sera jamais rouvert.
