# Erratum 2 — Conception 1 — le hasard du défenseur comme preuve — v2

- **Cet erratum prime sur la v2 et sur l'erratum 1** : v2 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v2.md` — sha256 47387ebf64c1569fce45a75c31aeae03fc4315c21b43f7581eefd4866e2ed51f ; erratum 1 `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v2-erratum-1.md` — sha256 25b425e45d9a01c0e74ef8a6500cc545fa0eb39714547ce8ae84c9b3ed97e841 (compagnons vérifiés). Ni la v2 ni l'erratum 1 ne sont réécrits.
- Ses couples s'appliquent à la v2 corrigée par l'erratum 1, dans l'ordre ci-dessous.
- Source des couples : relecture du concepteur `docs/notes/chantiers-21-novembre-v1/relectures-fable-v2/conception-1/relecture-fable-api.md` — sha256 be1a3cdbd36b49d890b4efa8845441a8e3a91a332afa0433886691857c9225f0 (compagnon vérifié).
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-2-conceptions-v2-v2.py` — sha256 768f426d5964dfc74250d6c810a04da45e87b724e62dc648c294570ab6b35c1b.
- **Lecture de R17, tranchée par l'orchestrateur, pas par le concepteur** (lecture de forme). Dans la relecture, la ligne « - R17. » est indentée de deux espaces ; sa colonne de contenu est donc 4, et les 4 espaces de la seconde ligne du nouveau texte sont l'indentation de la liste de la relecture. L'ancien texte est en colonne 0 dans la v2. Le nouveau texte est donc « - Elle ne dit rien d'une sensibilité sans dommage. », un saut de ligne, puis « - Elle ne protège pas l'oracle d'une paraphrase de l'étiquette par l'agent : G3 ne retire que les copies exactes. », en colonne 0 (puce sœur). Le programme retire ces 4 espaces et rien d'autre, et vérifie que le résultat est ce texte.
- Vérifications du programme : « v2 plus erratum 1 » construit en mémoire ; chaque ancien y figure une seule fois ; appliqués dans l'ordre, chacun est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne « v2 plus erratum 1 ».
- Texte consolidé : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v3-consolidee.md`.
- Couples (17), dans l'ordre d'application (ordre numérique, que la relecture prescrit) : R1 ; R2 ; R3 ; R4 ; R5 ; R6 ; R7 ; R8 ; R9 ; R10 ; R11 ; R12 ; R13 ; R14 ; R15 ; R16 ; R17.

## R1 — Constat 2 — clés de dérivation.

Ancien :
```text
spawn_key=(numero_tache, 0))
```

Nouveau :
```text
spawn_key=(0, numero_tache))
```

## R2 — Constat 2 — clés de dérivation.

Ancien :
```text
spawn_key=(numero_tache, 1, numero_emplacement))
```

Nouveau :
```text
spawn_key=(1, numero_tache, numero_emplacement))
```

## R3 — Constat 2 — clés de dérivation.

Ancien :
```text
spawn_key=(numero_tache, 3))
```

Nouveau :
```text
spawn_key=(3, numero_tache))
```

## R4 — La borne basse 0,035 est trop serrée.

Ancien :
```text
à corrélation 0, au moins 0,035 ;
```

Nouveau :
```text
à corrélation 0, au moins 0,030 ; le tout à N = 300 (50 tâches, k = 2), p₀ = 0,10, B = 999 ;
```

## R5 — Suppositions.

Ancien :
```text
- **Test.** La même permutation, la même statistique, appliquées à Z.
```

Nouveau :
```text
- **Test.** La même permutation, appliquée à Z, avec la statistique studentisée T_Δ définie ci-dessous ; p_S et p_J gardent la statistique T du § 2.
```

## R6 — Suppositions.

Ancien :
```text
- Pour p_Δ contre un jumeau insensible, à N = 300 : 0,72 pour δ = 0,15 ; 0,89 pour δ = 0,20.
```

Nouveau :
```text
- Pour p_Δ contre un jumeau insensible, à N = 300 : 0,72 pour δ = 0,15 ; 0,89 pour δ = 0,20. Ces valeurs, et le rejeu du contre-lecteur (0,449 ; 0,708 ; 0,887), valent pour la statistique non studentisée ; la puissance de T_Δ est à simuler par la pièce 6 et n'entre pas dans le test de mort 1, qui ne porte que sur la table de p_S.
```

## R7 — Constat 7 — régime de signature.

Ancien :
```text
les deux classes réunies, sans lire la marque.
```

Nouveau :
```text
les deux classes réunies, sans lire la marque. Par épisode, une seule uniforme u : u < s_c donne un dommage marqué ; s_c ≤ u < s_c + p_t, un dommage honnête ; sinon aucun dommage ; le taux de Y vaut donc min(1, p_t + s_c), comme au § 4.
```

## R8 — Constat 8 — table de l'exemple.

Ancien :
```text
| Conditionnelle (λ = 0, s = 0,20) | 0,46 | 0,88 | 0,98 |
```

Nouveau :
```text
| Conditionnelle (λ = 0, s = 0,20) | 0,45 | 0,87 | 0,98 |
```

## R9 — Constat 8 — table de l'exemple.

Ancien :
```text
| Uniforme (λ = 1, s = 0,067) | 0,46 | 0,88 | α |
```

Nouveau :
```text
| Uniforme (λ = 1, s = 0,067) | 0,45 | 0,87 | α |
```

## R10 — Constat 8 — table de l'exemple.

Ancien :
```text
(rejeu : 0,45 et 0,87 au lieu de 0,46 et 0,88)
```

Nouveau :
```text
(formule ci-dessus et rejeu : 0,452 et 0,867 ; 0,456 et 0,878 pour exactement 20 sabotages ; permutation à corrélation intra-tâche 0)
```

## R11 — Constat 9 — oracle aveugle.

Ancien :
```text
essai : un même épisode présenté sous ses trois étiquettes reçoit trois fois le même Y
```

Nouveau :
```text
essai : la chaîne entière, masquage puis oracle, est appelée trois fois sur les mêmes sorties d'un épisode, le champ de condition du registre prenant tour à tour les trois étiquettes ; les trois Y sont égaux
```

## R12 — Constat 12 — garde du témoin.

Ancien :
```text
moins 0,05, sur 1 000 répliques
```

Nouveau :
```text
moins 0,05, et au moins 0,50 dans l'absolu, sur 1 000 répliques (approximation normale à la main, statistique non studentisée, corrélation 0 : 0,63)
```

## R13 — Suppositions.

Ancien :
```text
- Cas sain : l'union est au moins égale à l'audit partout.
```

Nouveau :
```text
- Cas sain : à λ = 1, la permutation rejette au plus 0,061 des répliques (elle n'ajoute à l'audit que ses fausses alertes) ; à λ = 0 de la lecture (ii), à corrélation intra-tâche 0, elle en rejette au moins 0,93. L'union, au moins égale à l'audit par construction, n'est pas un cas sain.
```

## R14 — Suppositions.

Ancien :
```text
| 7. Simulation d'audit et courbes | union ≥ audit |
```

Nouveau :
```text
| 7. Simulation d'audit et courbes | cas sain de la figure (§ 5) |
```

## R15 — Suppositions.

Ancien :
```text
sans effet de tâche ni stratification, non rejouées.
```

Nouveau :
```text
sans effet de tâche ni stratification ; le contre-lecteur les a rejouées en monde simulé (chiffres marqués « rejeu »), le concepteur non.
```

## R16 — Suppositions.

Ancien :
```text
- Aucun PDF ouvert ; toutes les antériorités sont de mémoire.
```

Nouveau :
```text
- Aucun PDF ouvert par le concepteur ; les antériorités sont de mémoire, celle du concepteur ou celle du contre-lecteur, sauf les deux pages données lues par la note « percée ».
```

## R17 — Suppositions. (passage cité sur 2 lignes : l'indentation de 4 espaces des lignes de suite, colonne de contenu de la ligne de la relecture, est retirée (lecture de forme tranchée par l'orchestrateur))

Ancien :
```text
- Elle ne dit rien d'une sensibilité sans dommage.
```

Nouveau :
```text
- Elle ne dit rien d'une sensibilité sans dommage.
- Elle ne protège pas l'oracle d'une paraphrase de l'étiquette par l'agent : G3 ne retire que les copies exactes.
```
