# Contrôle du différentiel de l'erratum 1 à l'addendum scellé de la ligne 1, version 1 → version 2 — v1

Vérificateur : le relecteur de la version 1 de l'erratum, modèle O, sur GO-2026-11-19-93. Date : 2026-11-19, après 23:30Z (temps universel). Rien lancé ; aucune graine dérivée ; aucun interpréteur appelé ; aucun réseau sauf `git fetch` et `git show` ; aucune écriture dans le dépôt ; aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`.

## Verdict

**Scellable après corrections : deux corrections de tenue, à texte exact (§ 4).** Mes deux corrections sont appliquées à la lettre. Le seul ajout est « (rectification R-3985) », permis par la mère et juste sur le fond. La tenue est juste. Deux phrases de la version 1 sont devenues fausses, parce que l'erratum porte désormais deux précisions de lecture : le chapeau, qui en annonce une seule, et le titre du § 3.

## 1. Empreintes et différentiel

| pièce (commit `a0092f9d` de `lot/compte-organisme-v1`) | sha256 | état |
|---|---|---|
| erratum, version 2 | `f66c3ce8682ef1dd9ced3227378eb18041cff41bea76edfeb2c6373d56d1fcf3` | conforme à son compagnon |
| journal de l'outil de remplacement | `b3595bd8a4996cc8a82436e85b5980d3133f5a1cd0469347230f9d6e1076e90a` | conforme à son compagnon |
| différentiel v1 → v2 | `a84e20f76938f607fe6b386773e20ca22a7140589833221a51dd1784c07375d7` | conforme |
| rapport de recopie | `5e348eb34f3f7304f7d2916ebf5a1edfee1e08e057d2a3e4fe2ac7b2ea28ad94` | conforme |
| liste des remplacements | `bd96a54dd1c65316a391980003b71bac140d3d49215b56105decf7cb0a85c0b9` | conforme |
| mandat de la version 2 | `4d6fd1f7bbb7e2853502f2dbf454166231ae5be461fd88a82c0229201116e663` | égal à l'empreinte citée par l'erratum |
| erratum, version 1 | `a370cf6a…` | intacte (R12) |
| ma relecture | `48f14f5c…` | intacte |
| `registres/decisions.md` au commit `a2be44dbc` de `main` | `452a74bf3dd99621119ad587f90e021606c8fba2188add80ef2abf959a8cb268` | égal à l'empreinte citée ; R-3985 relue sur `main` |

J'ai refait `diff -u` sur les deux versions tirées du dépôt : son corps est identique, octet pour octet, à celui du fichier versé.

## 2. Mes deux corrections

- **Correction 1 (§ 2) :** appliquée à la lettre, avec un seul ajout, « (rectification R-3985) » après « ce sont ces quatre cellules ». La mère l'a permis, et il est juste : R-3985 dit « quatre cellules à remplir, portant sept valeurs », et que le chiffre huit « ne se reprend pas comme un fait ». R-3985 fixe aussi la référence de la garde A14 à 22:25:03Z, ce qui confirme qu'il faut garder le paragraphe « pour mémoire ».
- **Correction 2 (fin du § 3) :** le paragraphe est ajouté au caractère près, à la place demandée, après la phrase citée du § 9, point 5.

## 3. Tenue

La tenue est juste :
- titre en « v2 » ; statut en « version 2 » ;
- une ligne d'auteur pour la version 2 (agent de recopie, écart déclaré sur le précédent de R-3791, accordé par la mère), et l'ancienne ligne d'auteur renommée « Auteur de la version 1 » ;
- date des deux versions ;
- au § 1, le mandat de la version 1 renommé, et trois lignes ajoutées : le mandat de la version 2, la relecture, et `registres/decisions.md` pour R-3985.

Rien d'autre ne change.

**Les deux phrases de la version 1 devenues inexactes demandent une tenue :**
- le chapeau dit « porte une seule précision de lecture (§ 3) », alors que le § 3 en porte maintenant deux (§ 9, point 5 ; phrase de statut de la copie scellée) ;
- le titre du § 3 ne nomme que la première.

Un texte scellé qui annonce une précision et en porte deux se contredit lui-même. La tenue est courte et ne touche aucune valeur (§ 4). La phrase « Elle est portée ici comme précision de lecture » du § 3 reste juste, puisqu'elle parle de la précision du § 9, point 5.

## 4. Corrections (texte exact, tenue)

1. **Chapeau :** remplacer « et porte une seule précision de lecture (§ 3). » par « et porte deux précisions de lecture (§ 3). »
2. **Titre du § 3 :** remplacer « ## 3. Précision de lecture au § 9, point 5 — aucune règle changée » par « ## 3. Précisions de lecture (§ 9, point 5 ; phrase de statut de la copie scellée) — aucune règle changée »

Chaque texte ancien se trouve une seule fois dans la version 2 (contrôlé par recherche de chaîne exacte). Si ces deux remplacements sont faits à la lettre et que rien d'autre ne change, l'erratum est scellable ; un contrôle du différentiel suffit.
