# Déclaration : essai de fonctionnement du script v2 sur une configuration de la grille

- **Fait** : le 24 novembre 2026, avant la course, la fille 2 a lancé `traiter_point` du script v2 (`experience_seuil_chantier3_v2.py`) une seule fois, pour vérifier qu'il s'exécutait sans erreur. Elle a utilisé l'indice de point 999, hors de la grille, donc des graines que la course n'emploie jamais.
- **Écart** : les paramètres choisis (K = 50, n = 100, γ = 0,2, η = 10, C = 4, δ = 0,05) **coïncident avec un point de la grille**. La fille 2 a vu, pour cette configuration et avec des tirages indépendants de la course, trois choses :
  - classe de V à λ = 0 : « au-dessus de δ/2 » ;
  - classes à λ = 1 : « sous » (V, V′, D) ;
  - rapport ε_emp/ε ≈ 0,40, bissection valide.
- **Portée** : la course n'a pas été lancée et aucune de ses sorties n'a été lue. Le préenregistrement était déjà scellé (`4f3ee5c3…`), avec ses prédictions et ses critères gelés. Le script était soumis à contre-lecture, et aucune de ses lignes n'a été changée après cet essai. Cet essai ne laissait donc aucune latitude d'ajustement. Il est déclaré au titre de la règle de non-lecture et de la règle de symétrie (R4) ; il revient au lecteur neuf et à la mère de juger s'il affecte la course.
- **Correction pour la suite** : tout essai de fonctionnement se fera sur des paramètres hors de la grille.
