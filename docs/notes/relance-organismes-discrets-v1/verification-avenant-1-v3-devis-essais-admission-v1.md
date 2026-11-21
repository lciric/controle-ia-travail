# Vérification de la version 3 de l'avenant 1 au devis des deux essais d'admission — v1

- **Objet** : la section 13, « Changements depuis la version 2 », de `docs/notes/relance-organismes-discrets-v1/avenant-1-devis-essais-admission-recharge-et-deux-cles-v3.md`. Son empreinte est vérifiée contre son compagnon `.sha256` : OK. Elle est confrontée à ma contre-lecture de la version 2 (`contre-lecture-avenant-1-v2-devis-essais-admission-v1.md`).
- **Vérificateur** : le même agent Claude Opus 5.5. Écrit le 2026-11-21. Non scellé.

## Verdict : corrections fermées ; engageable sur ces points

Mes deux corrections, C-1 et C-2, et mes quatre mineurs, m-1 à m-4, sont appliqués aux endroits que dit la section 13. Le chiffre de 23,44 USD par projet est juste. Je ne relève rien de neuf.

## Point par point

| point | vu dans la version 3 | fermé |
|---|---|---|
| **C-1** dépense retirée | 4.4, point 4 : on retire la somme des deux dépenses, sauf si `google_deux_projets_distincts` vaut `oui`. La clé est en 5.1 ; elle est dite non levée en 5.2 (ligne 310) ; la pièce passe à vingt-huit clés (lignes 18, 298, 354 et 487). Elle est reprise à la ligne 4 de la section 6 et au point 7 de la section 7, avec un cas sain et un artefact justes (19,76 − 3,68 = 16,08, la file part ; 19,76 − 3,70 = 16,06, elle ne part pas). | oui |
| **C-2** question manquante | 8.2, point 4, repris au texte de ma contre-lecture, avec une puce de plus qui ne lève rien. Section 0, point 6 : « Quatre points ». | oui |
| **m-1** plafond mensuel | 2.4 : la v3 dit que c'est une lecture. | oui |
| **m-2** ligne nouvelle de vérification | Ligne 2 de la section 6 : « ajoute 3,68 USD au pire cas et exige de nouveau 19,76 USD ». Ligne 4 : « pour les lignes 2, 4 et 6 telles qu'accordées ». Section 9, point 12. | oui |
| **m-3** contrôle avant la seconde vérification | 4.4, point 3 (on retire la dépense ; elle est nulle avant la première vérification) ; ligne 2 de la section 6 ; section 7, point 7. | oui |
| **m-4** « 3 levées » | Section 11 : « 2 levées + 1 décision (plafond) = 9 » ; six clés levées au total. | oui |

Les trois ajouts que la v3 déclare de son fait (les artefacts et la phrase du point 6 de 4.4) vont dans le sens du durcissement. Aucun n'allège une garde.

## 23,44 USD par projet

Prenons le cas où les deux clés sont sur un même projet. Ce projet porte les deux vérifications au pire, 2 × 3,68 = 7,36 USD comptés, puis la file, 16,08 USD. Il lui faut donc un crédit compté d'au moins 16,08 + 7,36 = **23,44 USD**. La règle de la somme l'exige bien, avant la file comme avant la seconde vérification : 23,44 − 3,68 = 19,76.

Avec un solde visé de 20 €, on compte 20 × 0,95 = 19,00 × t USD. Il faut alors un taux t d'au moins 23,44 ÷ 19,00 = 1,233684, soit **1,2337** arrondi par excès. Le chiffre est juste.

## Ce que j'ai ouvert

- La version 3 : la liste de ses titres, les lignes 12 à 20, 157 à 164, 253 à 268, 333, 337, 355 et 401 à 407, la section 13, et les lignes rendues par une recherche de « deux_projets_distincts », « vingt-huit », « 1,2337 », « 23,44 », « Point 4 », « lignes 2, 4 et 6 », « ligne nouvelle » et « 2 levées ».
- Son compagnon `.sha256`.
- Aucun réseau, aucun `git fetch`, aucune clé, aucun chemin interdit.
