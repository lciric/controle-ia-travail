# Contrôle différentiel du brouillon 4 de l'addendum de relance de l'idée 1.1 (R2, lecteur neuf, modèle C)

Heure : 2026-11-16T20:52:47Z (`date -u`). Contrôle différentiel seul, aucun fichier existant modifié.

**Verdict : conforme.**

## Pièces
- Brouillon 3 : `addendum-relance-idee-1-1-v1-brouillon3.md`, empreinte 7b11231c58b86e8999d0b6a3740a533473c8093be131107439404fcfe7075c81 (égale à celle citée par l'en-tête du brouillon 4).
- Brouillon 4 : `addendum-relance-idee-1-1-v1-brouillon4.md`, empreinte a692d50c07c1b4b7ef07883ac91124eab4798cab7a579e14235484ea4d2319cf (égale à la consigne et à son compagnon).

## Contrôles
1. `diff` brouillon 3 contre brouillon 4 : 8 blocs, tous rattachés à l'un des trois changements permis.
   - (1) Lettre : lignes 25-26, « lettre C » devenue « lettre A (le modèle des brouillons 1 et 2) », avec la liste des écrits exclus mise à jour au tour 3. Les autres « lettre C » restantes (lignes 377, 416, 431, 436) sont celles des lecteurs ou des cas historiques des tours 1 et 2, inchangées par le diff ; conforme à la raison donnée (ligne 45).
   - (2) Écart D7 : lieu = machine louée (§ 1, 4.9, 4.10, § 5), lieu (i) gardé comme non retenu, limite au bit près déclarée (mêmes graines, mêmes clés, égalité non garantie sur un autre processeur, comparaison des deux runs toujours interdite), renvoi à la procédure de machine `docs/procedures/machine-jeu-idee-1-1-v1/` (annoncée en écriture, absente du dépôt à ce jour : l'en-tête et 4.10 le disent).
   - (3) En-tête : nouvelle puce de version et statut.
2. Ligne du registre : `grep '^| GO-2026-11-16-10 |' registres/go.md` trouve la ligne ; mot de Lazar cité identique (« Ma recommandation est d'accepter, confiance 0,65. : go ») ; l'empreinte bbfefbfd… citée en 4.9 est celle du fichier \`registres/go.md\` entier à la tête d4f18e58 (vérifiée par \`git show\` et \`sha256sum\`), exacte, et le fichier actuel a la même empreinte ; Ordre de grandeur 1 à 3 USD concordant.
3. Lignes au format « <sha256>  <chemin> » dans le brouillon 4 : **0** (deux motifs testés, début de ligne et avec indentation).
4. Aucun critère, graine, condition de relance ni consigne ne change autrement : le diff ne touche aucune ligne de 4.1 à 4.8, ni des § 2, 3, 6, 7, 8 ; les seules phrases de consigne et de lieu modifiées sont celles du § 5 (lieu (i)/(ii)) et de la phrase qui renvoie à l'écart. Les contraintes de « rien d'autre ne change » sont reformulées avec la réserve « hors l'écart D7 » (lignes 83, 86-87), cohérente.

## Remarques (aucune exigée)
- L'en-tête cite la tête `d4f18e58…` ; la tête actuelle est 5b61901 : le texte dit « lu sur main, tête … » à l'heure du scellement, donc exact à cette date.
- La section « Contre-lecture » (§ 7) et le § 8 ne sont pas mis à jour pour le tour 3 : annoncé par l'en-tête, à faire à la recopie sous `prereg/`.
