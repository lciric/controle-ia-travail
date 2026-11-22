# Instrument — bases sans modèle sur la famille MR-2 — v1

- Aucun appel de modèle, aucun réseau, aucune dépense ; calcul seul (environ 7 minutes de processeur pour 12 mondes). Script : `bases_sans_modele_v1.py` ; sortie : `bases-sans-modele-v1-sortie.json` ; essais préalables sur le monde 1 : `essai-bases-monde-1.json` (première écriture) et `essai-bases-monde-1-b.json` (après correction, voir § 4). Empreintes dans les compagnons `.sha256`.
- Mondes : les 12 graines de développement de la conception v4 (`conception-monde-riche-doublons-v4.md`, `47e38ec0…`), régénérés par le code scellé `outils-v4/monde_riche_v4.py` (`4b165847…`) au tirage conforme que rapporte chaque partie scellée (`sorties-v4/partie-v4-monde-r.json`, champ `refus`) ; contrôle : le gabarit régénéré est égal au gabarit scellé dans les 12 mondes. Tous les modules importés sont vérifiés contre leur compagnon avant l'import.
- Graines : `SeedSequence(20261122, spawn_key=(tâche, monde))`, tâche 0 pour les données servies, 1 pour la base B1, 2 pour la base B2 ; la base B3 est déterministe ; mondes et oracle gardent les graines de la v4. Python 3.13.18, numpy 2.5.3. Graines et versions sont consignées dans la sortie.
- **Verdict d'abord.** Avec 52 cartes sur trois générations (le compte du bras (c) au cas attendu) et le même oracle sur toutes les cartes, la **recherche gloutonne bornée** couvre en médiane **0,69** des composantes hors celle de la loi connue (de 0,43 à 0,86 selon le monde) et n'a que 4 formes fausses distinctes en médiane. Elle ne couvre que **3 conditionnelles sur 14**. Le **tirage uniforme dans la grammaire** couvre 0, avec 52 formes fausses sur 52. **K1 plus un effet au hasard** couvre 0,15 en médiane, avec 47,5 formes fausses. Les trois bras de l'essaim devront battre au moins la base gloutonne, qui ne coûte aucun appel.

## 1. Bases

Aucune base ne lit l'oracle, la loi du monde ou un verdict. Elles n'utilisent que les données servies et l'archive de départ {K1}.
- **B1, uniforme** : 52 lois tirées dans la grammaire servie, sans données et sans K1. On tire de 0 à 3 conditions de seuil sur un trait, de seuil 0 une fois sur deux, sinon uniforme sur [−1 ; 1,2]. On découpe par sous-population une fois sur deux. Les feuilles sont des softmax où chaque trait est présent avec la probabilité 1/2, avec des pentes N(0 ; 1) et un biais N(0 ; 0,3²).
- **B2, K1 plus un effet au hasard** : 52 additions distinctes, tirées uniformément parmi les effets de la grammaire. Les sortes sont principal, seuil, interaction de seuil, sous-population et interaction de sous-population, avec des seuils dans {−0,5 ; 0 ; 0,5}. Les paramètres sont ajustés sur les données servies.
- **B3, glouton borné** : à chaque génération (18, 17 puis 17 cartes), on ajuste toutes les additions d'un effet à la loi courante, soit environ 227 candidats, sur les trois quarts des données. On les classe sur le quart restant, et les meilleures deviennent les cartes. La meilleure devient la loi courante si elle gagne. Aucun juge n'intervient.
- **Données servies** : 2 000 instances (traits, sous-population, issue) tirées du monde. Cette taille est une **hypothèse** : aucune pièce lue ne fixe la taille de la case de matière servie.

## 2. Oracle et métriques (celles de la section C.5, sur toutes les cartes)

- Les instances sont celles de l'oracle de la v4 (`Oracle(…, n = 12000, graine = cle("oracle-v4", r))`).
- Une carte est **vraie** si son gain au-delà de l'enveloppe du nul de {K1} atteint 0,02. Elle est **fausse** si elle est évaluable sans atteindre ce seuil, et classée **rien** si elle n'est pas évaluable.
- Une composante est **couverte** si une carte vraie au moins la capte, selon l'attribution de la v1 (Δ_i ≥ max(0,005 ; 0,75·I_i)). L'attribution est faite par un cache, dont l'égalité exacte avec `M.Oracle.attribution` est vérifiée dans chaque monde (écart maximal 0).
- **Couverture** = composantes couvertes / composantes du monde hors celle de K1. **Garde** = nombre de formes canoniques distinctes parmi les cartes fausses.

## 3. Résultats (12 mondes ; `resume` et `par_monde` de la sortie)

| base | couverture médiane (min ; max) | moyenne | certifiées, médiane | conditionnelles couvertes | cartes vraies | formes fausses distinctes, médiane |
|---|---|---|---|---|---|---|
| B1 uniforme | 0 (0 ; 0) | 0 | 0 | 0 / 14 | 0 / 624 | 52 |
| B2 K1 plus un effet au hasard | 0,155 (0 ; 0,625) | 0,19 | 0,25 | 0 / 14 | 58 / 624 | 47,5 |
| B3 glouton borné | **0,690** (0,429 ; 0,857) | 0,69 | 0,71 | **3 / 14** | 562 / 624 | 4 |

Couverture de B3 par monde, de 0 à 11 : 0,71 ; 0,57 ; 0,75 ; 0,83 ; 0,86 ; 0,67 ; 0,83 ; 0,83 ; 0,57 ; 0,43 ; 0,63 ; 0,57. La couverture cumulée par génération est dans la sortie (`couverture_cumulee_par_generation`).

Lecture : une recherche gloutonne sur les seules données servies prend presque toutes les composantes ordinaires. Elle manque surtout les conditionnelles, que la famille MR-2 rend invisibles marginalement. C'est l'interaction prédite par la conception (C.5 : (a) > (b) sur MR-2), mais vue ici sur une base sans modèle et sans masquage supposé : 3 conditionnelles sur 14 sont trouvées sans proposeur. Ce n'est pas une pièce sur de vrais modèles.

## 4. Épreuves et écarts (déclarés, non réparés après la course complète)

| épreuve | attendu | rendu |
|---|---|---|
| gabarit régénéré = gabarit scellé | 12 / 12 | 12 / 12 |
| attribution du cache = attribution de référence | 12 / 12 | 12 / 12 (écart 0) |
| K1 classée fausse | 12 / 12 | 12 / 12 |
| loi du monde classée vraie et captant toute composante certifiée non latente | 12 / 12 | **11 / 12** : dans le **monde 0**, la loi du monde elle-même ne « capte » pas E3 (moyenne certifiée, décalage de sous-population) |

- **Écart 1, après l'essai sur le monde 1, avant la course complète** : la première écriture comptait une composante couverte par toute carte évaluable. B1 rendait alors une couverture de **1,0 avec 0 carte vraie**, car l'attribution donne des Δ_i grands à des lois absurdes. La couverture ne compte désormais que les cartes vraies. La couverture « brute » reste rapportée : B1 1,0, B2 0,29, B3 0,69 en médiane. **Conséquence pour la conception** : la métrique de C.5, « au moins une carte proposée », doit être conditionnée, ou l'attribution doit être remplacée par une correspondance canonique à la composante (ce que dit d'ailleurs C.5). Sinon un essaim bavard gagnerait par le bruit.
- **Écart 2, même moment** : l'objet de contrôle « la loi du monde capte toutes les non latentes » échouait sur une faible non certifiée, sous le plancher de 0,005. Il a été restreint aux composantes certifiées.
- **Échec d'épreuve non réparé** : monde 0, E3. L'oracle par attribution ne sait pas dire que la loi vraie porte un décalage de sous-population certifié. La couverture de E3 n'y est donc pas mesurable par cet instrument. La v4 signalait déjà ce monde (E3, « non captée en génération 1 par le hasard du flux »). À porter à la seconde écriture de l'oracle (A.4, point 2).

## 5. Réserves

1. La grammaire de B1 est mon approximation de la grammaire servie, car le gabarit exact (v3, § 3.6) n'a pas été lu. B1 n'est donc qu'un plancher.
2. La taille des données servies (2 000 instances) n'a pas de pièce, et le résultat de B3 en dépend. Une sensibilité (500, 8 000) reste à faire.
3. Les mondes sont des graines de développement publiques, non les mondes scellés de calibration ou de test.
4. Les seuils candidats de B3 ({−0,5 ; 0 ; 0,5}) comprennent le seuil 0 des conditionnelles. Cela favorise B3 sur MR-2, puisque la régularité « condition sur le signe » est publique (Q-10 (a)), mais cela doit être dit.
5. Les bases comptent 52 cartes par monde, mais la couverture d'un essaim porte aussi sur des cartes de forme plus libre : la comparaison n'est juste qu'à oracle identique, appliqué par le même code.
