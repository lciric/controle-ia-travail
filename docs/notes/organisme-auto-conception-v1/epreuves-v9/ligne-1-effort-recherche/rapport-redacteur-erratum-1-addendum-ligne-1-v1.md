# Rapport du rédacteur — erratum 1 à l'addendum 1 scellé de la ligne 1 — v1

Auteur : rédacteur neuf, modèle F. Date (temps universel, `date -u`) : 2026-11-19, vers 22:34. Pièce de travail (classe C).

## Verdict

L'erratum est écrit. Les quatre cellules « À PORTER » de l'addendum scellé (huit valeurs) sont toutes remplies ; aucune ne reste ouverte. Aucun refus d'outil.

## Fait

- Mandat vérifié : `d2b68c3aa5c04fae922c452a55f834b29dd1d63e2fe126308b866703a9da1064`.
- Addendum scellé lu en entier sur `main` (commit `0dedbcaf9354848d3b070f9f6136cc5a577eb209`, après `git fetch origin main`) : `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67`, égale au commit du scellement `061aeff58d64b43a4843d61137123f3db5d8d650`, à son compagnon et à la version 4 du compte (commit `cf6094a2`).
- Registre des scellements et R-3980, R-3981 lus sur `main` ; contrôle v4 lu en entier, `def81ef33381acd6bbd10926c79f025743cd16de17b0e35621706a262e1bb2c2`, conforme à son compagnon et égal au commit `991e4229233e864def74b525b09d28685c331bb7`.
- Les quatre textes exacts des lignes citées se trouvent chacun une fois dans l'addendum scellé (contrôle par programme) ; la phrase du § 9, point 5, est celle du contrôle v4, au caractère près.

## Places « À PORTER »

| place | état | valeur |
|---|---|---|
| § 6, chemin scellé | remplie | `prereg/organisme-auto-conception-v9/addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4.md` sur `main` |
| § 6, sha256 | remplie | `c29628a0…6e67` |
| § 6, commit et heure du scellement | remplie | commit `061aeff58d64b43a4843d61137123f3db5d8d650` ; `2026-11-19T22:25:03Z` |
| § 8, contrôle du différentiel v3 → v4 | remplie | chemin, `def81ef3…b2c2`, commit `991e4229…`, « Scellable tel quel » |

Quatre autres mentions « À PORTER » (§ 10, § 11 deux fois, § 12) sont des récits de versions antérieures ; l'erratum les nomme et dit qu'elles n'attendent rien.

## Réserves et écarts

1. **Un paragraphe « pour mémoire » au-delà de la lettre du mandat.** L'erratum dit, sous la table du § 6, que R-3980 et R-3981 sont datées 22:25:19Z (commit `3f64028f1…`) et que cette heure est celle de la consignation, non celle du scellement. C'est une précision de source, pour que personne ne prenne 22:25:19Z pour l'heure que lit le contrôle de la garde A14. Le mandat ne permet qu'une phrase de plus : si la mère le lit strictement, ce paragraphe se retire sans rien changer aux valeurs.
2. **Phrase de statut de l'addendum scellé.** La copie scellée dit encore « version 4 […], non scellée, avant le contrôle de son différentiel ». Ce n'est pas une place « À PORTER » ; l'erratum n'en dit rien. À la mère de voir si un mot de lecture est voulu.
3. **Compte de R-3980.** R-3980 parle de « huit places » ; le texte scellé porte quatre cellules, qui appellent huit valeurs. L'erratum le dit en une phrase.
4. **Registres cités à leur état du commit `0dedbcaf9`** de `main` (empreintes des fichiers entiers dans l'erratum) ; ils changeront aux prochaines lignes ajoutées, les lignes citées non.
5. L'erratum n'a pas de compagnon `.sha256` et n'est pas contre-lu : à la mère (règles R2 et R6).

## Fichiers écrits (bloc-notes seulement)

- `erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v1.md`
- `rapport-redacteur-erratum-1-addendum-ligne-1-v1.md` (ce rapport)
- `lu/addendum.md` : copie de lecture de l'addendum scellé tirée par `git show` (`c29628a0…`), à ne pas verser.
