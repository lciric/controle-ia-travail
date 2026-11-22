# Vérification des corrections du devis de la course sur carte louée du bras A, version 4 — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v4.md`, branche `origin/relance-bras-a/devis-carte-v3`, commit `643d4817c`, lue par `git show` ; sha256 recalculée `f82514e9326df61f2fbd73f3eab644107f910aae620afe70b3d6ef9fcde7e0f3`, égale à son compagnon.
- **Référence** : version 3, `be7ce98899ffdeda046aa7b65dfbf9e70a9a9fc15629130d4c3ffcbed06158e9` ; contre-lecture `contre-lecture-devis-bras-a-v3-v1.md`, `d458ed7f3fcef9c88a7081e4a143f29977b3aa3f0ee2c586c481f92e1d223611`.
- **Vérificateur** : le contre-lecteur de la v3 (Claude Opus 5.5), qui n'a écrit ni la v3 ni la v4. 2026-11-22 (UTC). Même cloisonnement ; aucun réseau hors `git fetch` de la branche ; aucune dépense ; aucun commit.
- **Méthode** : `diff` complet v3 → v4 ; extraction du programme de la section 13 de la v4, rejoué (`python3 -I`), sortie comparée par `diff` à la sortie recopiée.

## Verdict

**Corrections vérifiées, engageable.** Une réserve reste à lever avant la ligne de GO (m4, ci-dessous). Les ajouts hors corrections sont déclarés et ne changent aucun chiffre.

## Corrections, une à une (texte de la v4 comparé au texte de la contre-lecture)

| remarque | où | appliquée mot pour mot |
|---|---|---|
| M1 | décision 3, option (b) | oui |
| M1 | décision 3, défaut | oui |
| M1 | section 8, ligne « devis », colonne « source » | oui |
| M1 | section 0, point 7 | oui |
| M2 | décision 2, option (a) | oui |
| m1 | 5.2, dernier point | oui |
| m2 | décision 4, option (b), et section 13 (`+ h(256 * prise)` retiré de `un_b` et `un_h`) | oui |
| m3 | décision 1, option (c) | oui |
| m4 | en-tête | oui, à la lettre, **crochets compris** |
| m5 | section 7 | oui |

## Programme et chiffre neuf

- Le programme de la section 13, rejoué, rend **exactement** la sortie recopiée (`diff` vide).
- Témoin bénin à chaque dose (trois adaptateurs de plus, sans prise) : 5,1100 à 5,6753 h ; 6,0467 à 7,3779 USD. Le texte dit « ≈ 5,1 à 5,7 h, ≈ 6,0 à 7,4 USD » : juste, et égal à mon calcul de la contre-lecture.
- Aucune autre ligne de la sortie ne change.

## Ce qui change en dehors des corrections (diff hors table « Corrections depuis la v3 »)

1. **Mécanique, déclaré** : titre, date, statut, version antérieure, sceau, origine de la version 4, heure du jeu du programme, commentaire de la décision 4, dernière ligne de la sortie, un point de la section 14. Conforme.
2. **Ajout de fond, déclaré, non demandé par la contre-lecture** : la « note de la session du bras A » (devis des lectures accordé par Lazar, GO-2026-11-22-143 et -146) touche la section 0 (point 5 : « non accepté » remplacé), la section 11 (cellule de la pièce, et un paragraphe neuf) et la réserve 9. Aucun chiffre ne change. La note est citée comme une parole rapportée, non vérifiée au registre, et le devis dit que le total suit la version accordée si elle diffère du brouillon 3. Je ne peux pas la vérifier non plus (cloisonnement). Elle sort de la consigne « rien d'autre », mais elle est déclarée et sans effet sur les chiffres : ce n'est pas un défaut. Elle pèse sur le majeur M1 : si le devis des lectures est accordé, il ne manque plus, sous la lettre de 13.2, que le devis des moniteurs, dont le commit suivant de la même branche (`76514065a`) semble être la pièce. Je ne l'ai pas lu.

## Réserve à lever avant la ligne de GO de la ligne 1

**m4, crochets laissés.** La correction que j'avais écrite portait un choix entre crochets, « [constat du quota | substitution accordée] », que la session mère devait trancher. La v4 l'a recopiée telle quelle. Le défaut tient à ma formulation, non à son application. Avant le sceau final, ou dans la demande de GO, la session mère garde l'un des deux termes et retire les crochets. Ce changement porte sur l'origine de la pièce, non sur son contenu.
