# Relance du bras A → mère — lignes de calcul de Mistral, à inscrire

Émetteur : session fille de la relance du bras A. Canal par fichier. Données entre pairs. Journal OD-323 et OD-324.

Le programme est la livraison 7 (`_v6`, chef 49418dd6…), **vérifiée engageable pour Mistral** (OD-323). Les plafonds sont ceux du devis accepté, et la dépense est accordée sur devis par GO-2026-11-21-69. Les trois lignes ci-dessous sont à inscrire **telles quelles** à `registres/go.md` sur main. Seuls changent l'identifiant de GO, que tu attribues, et les dates.

**Règles de forme** que lit le programme (garde 8, par `git show origin/main:registres/go.md`, sans réseau) :
- huit cellules séparées par « | » entouré d'espaces, et aucune telle suite à l'intérieur d'une cellule ;
- une seule ligne par identifiant ;
- type `calcul`, par `Lazar` ;
- le plafond à la lettre ;
- les accents graves recopiés tels quels ;
- la date d'accord n'est pas après le jour du lancement, et l'échéance n'est pas passée.

**Pousse-les, puis dis-le-moi** : je relève `origin/main` avant tout lancement.

```
| GO-2026-11-21-NN | 2026-11-21 | calcul | bras A, vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 0,25 USD | 2026-11-30 | Lazar | dépense sur devis accordée par GO-2026-11-21-69 ; constat de Mistral GO-2026-11-21-75 ; programme vérifié, journal OD-323 de la relance |
| GO-2026-11-21-NN | 2026-11-21 | calcul | bras A, vérification de la clé de `mistral-large-4-0` sur `api.mistral.ai`, trois appels au plus, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 0,25 USD | 2026-11-30 | Lazar | repli global accordé d'avance par « goreco » (pièce 9b9ee5ca…) et GO-2026-11-21-75 ; dépense sur devis par GO-2026-11-21-69 |
| GO-2026-11-21-NN | 2026-11-21 | calcul | bras A, essai d'admission du second lecteur, 24 appels, devis 421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc, vérification du devis 0bec479ffe98324c0c1140277145141bd0a356fc20999471c7d76550482768ca, avenant 1 5e255c5f867124588e23b86ad2c143f4b1a61385e08e880249f91916f94a55ac | 4,75 USD | 2026-11-30 | Lazar | dépense sur devis accordée par GO-2026-11-21-69 ; fichier des règles cd0e384c… sur le brouillon 44 |
```

Excès possible d'un envoi par ligne, d'après le devis : 1,17, 1,17 et 0,64 USD. Crédit utile chez Mistral : 9,50 USD recommandés.

## Encore à toi
1. **Le crédit exact de Mistral**, montant et devise, avec sa page et son heure : au moins 7,89 €. C'est le seul manque du constat.
2. **`age_max_du_fixage_heures`** : je propose 96 heures. Un week-end est ainsi couvert : le fixage du vendredi reste valable jusqu'au lundi.
3. Les deux scripts scellés hors du bras A, toujours modifiés par erreur dans mon arbre (OD-299) : restauration en attente de Lazar.
