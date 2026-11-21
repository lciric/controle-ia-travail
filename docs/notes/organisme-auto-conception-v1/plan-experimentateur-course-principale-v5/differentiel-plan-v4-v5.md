# Différentiel du plan — v4 → v5

- v4 : `plan-experimentateur-tests-de-mort-course-principale-v4.md`, `ebb4cb47707e30929b535c8f65249f3f55abe831386e1fcaf5cf69cffcecc14f`, inchangée (règle R12).
- v5 : `plan-experimentateur-tests-de-mort-course-principale-v5.md` ; empreinte à la table jointe. Elle est faite d'une copie à l'octet de la v4, retouchée par remplacements.
- Cause : la vérification de la v4 (`804a6675ea350fbe30835e40f7d538be1f731240c159f01c887da33567f57dbb`, « Conforme, sous deux retouches de lettre ») et les deux relevés de la mère (les dix champs ; la lecture de « GO-15 et GO-28 »).
- Rien d'autre n'a été changé.

## Par partie

| partie | v4 | v5 |
|---|---|---|
| titre, en-tête | « v4 » ; un alinéa de tête | « v5 » ; un alinéa neuf en tête, qui dit les deux retouches et que le défaut de D5 reste compté à partir du texte de la v4 ; l'alinéa de la v4 gardé, introduit par « Comme la v4, elle porte » |
| en-tête, auteur et dates | un relevé de date | deux relevés ; une ligne « lecture neuve de la v5 » ; la configuration dite non ouverte par moi |
| en-tête, calculs | `calculs_plan_v4.py` | `calculs_plan_v5.py` : les mêmes blocs, plus un bloc qui retrouve les heures depuis la table |
| § 1 | — | deux lignes de plus : la vérification de la v4 ; les dix champs, relevé de la mère |
| **§ 4.2, table des lots** | cinq colonnes, sans heures ; E1-AC « 1 à 2 heures, hypothèse » dans son contenu ; E1-v69 sans heures | **une colonne « heures »** : E0 1,25 ; C1 3,5 à 39, texte ; E3 8 à 15 ; C2 2 à 3 ; E2 3,75 ; **E1-v69 au devis d'heures du palier 1, aucune heure dans ce plan** ; **E1-AC 5,75 à 6,75** (les 4,75 de l'ancien E1, plus 1 à 2) ; C3 1 à 2 ; E4 2,75 ; E7 2,75 ; E8 5,5 ; E9 4,75 ; E5 4,75 ; E6 3,75 |
| § 4.2, après la table | — | alinéa neuf « Les heures de la table » : leurs sources ; 46 à 56 heures, 37,5 à 47,5 sans E5 ni E6 |
| § 4.2, chemin critique | « de 18,25 à 20,25 heures » | la même phrase, plus les deux additions lot par lot |
| **§ 7.3, D8 (a)** | « étend le modèle sur deux points » ; champs fermés dits non nommables ; « si aucun des dix n'est fermé, le point (1) tombe » | les dix noms et leur source ; la configuration ne déclare aucune liste de valeurs ; **le point (1) tombe** ; deux branches non tranchées : (a1) les seuls noms, à peu près ce que GO-2026-11-20-28 a rendu ; (a2) la recherche de mots dans `module_change`, qui lit une valeur et n'est donc pas « sans aucune valeur » ; la phrase à dire à Lazar |
| § 7.3, recommandation | « puis (a) avec le devis de la ligne 2 » | « puis (a), dans sa branche (a2) si Lazar accorde la lecture d'une valeur par programme, avec le devis de la ligne 2 » |
| § 7.2, D5, défaut | « compté à partir de ce texte v4 » | « compté à partir du texte de la v4, que cette v5 recopie sans le changer » |
| § 9, réserve 8 | champs fermés non nommés | champs nommés d'après le relevé de la mère, pièce non ouverte par moi ; point (1) tombé ; (a2) lit une valeur |
| signature | planificateur du plan v4 | planificateur du plan v4, auteur de la v5 |

## Chiffres changés

Aucun. Les heures de la colonne neuve redonnent les totaux de la v4 : 46 à 56 heures de code ; 37,5 à 47,5 sans E5 ni E6 ; 18,25 à 20,25 heures jusqu'au premier dollar ; 20,25 à 23,25 avec C2. Seule l'écriture de E1-AC change : « 5,75 à 6,75 » dans la table, là où la v4 n'y écrivait que le supplément de « 1 à 2 ».

## Ce qui n'a pas changé

Tout le reste : les § 0, 2, 3, 5, 6 et 8 ; les deux lignes de coût ; le barreau 2 ; N1 à N7 ; D1, D3, D4, D5 (options, recommandation, nœud déclaré, défaut), D6, D7 ; les options (b), (c) et (d) de D8 ; les réserves 1 à 7.
