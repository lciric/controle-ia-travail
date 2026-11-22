# Collisionneur v9, mode essaim (v5) : rapport

Écrit à 2026-11-22T07:53:34Z (`date -u`). Pièce d'instrument (classe B), Opus 5.5, session des collisionneurs. Aucun réseau, aucune clé, aucune course. Le pilote ne part qu'après le feu écrit de la mère.

## Pièces
- Base : la v4 (brouillon de l'ancien développeur, versé non scellé ; scellée ici telle quelle, 9ae76a54…, avec ses essais et sa configuration) ; vérifiée par un contre-lecteur Opus neuf : `verification-essaim-v4-opus-neuf-v1.md` (à corriger, un bloquant).
- `collisionneur_v9_essaim_v5.py` (f2593ce9…), fabriquée depuis la v4 par `fabriquer_essaim_v5_depuis_v4_v1.py` (remplacements exacts ; reproductible, comparé octet par octet) ; essais `test_collisionneur_v9_essaim_v5.py` (ad2bf66c…) : 52 passés ; configuration `configuration-pilote-essaim-v5.json` (8b91d92f…), `place_iii3` à null : refusée tant que la place n'est pas fixée.

## Changements, et seulement ceux-là
1. **Moteur v8e** (0d591933…, ordre de la mère du 22 novembre, 07:40Z), empreinte contrôlée au chargement (noms `SCRIPT_MOTEUR`, `SHA_MOTEUR`, `charger_moteur`, clé de journal `sha256_moteur`). Le temps 0 reste l'invite III.1 du moteur, mot pour mot : il porte donc la « forme imposée » des duels (essai). Clé neuve `place_iii3` (l'une des places de la v8e), obligatoire.
2. **Bloquant de la vérification** : la borne d'un brouillon non écrit prend le plus grand de `max` et `max_relance` (Astra : 144 000 caractères au lieu de 36 000). Mutation (retour à `max`) prise.
3. **Essais neufs** : moteur et place ; temps 0 balisé, cycles et finale sans la forme ; borne avec relance ; balise de bloc refusée par `verifier` (non-bloquant 2 de la vérification, par substitution de la lecture d'un élément). Mutation « place non posée » prise (40 échecs).
4. Une phrase affichée par `devis` nommait encore la v8d : « du moteur (v8e) ».

Non portés (non-bloquants de la vérification, laissés tels quels) : garde redondante de l'origine d'un rejeu ; caractères des textes publiés bornés par la seule limite de mots (le plafond reste tenu sur l'entrée comptée).

## Devis du pilote (commande `devis`, question générale v2 caa3365b…, ordre simultané, parts non bloquantes, place « fin », sans réseau)
| cycles | pire sans relance | pire avec relances | finales, sans relance | finales, avec relances |
|---|---|---|---|---|
| 2 | 48,78 USD | 126,34 USD | 13,02 | 33,53 |
| 3 | 65,40 USD | 167,97 USD | 13,56 | 34,74 |
| 4 | 83,54 USD | 213,04 USD | 14,10 | 35,96 |

Sorties brutes : `devis-pilote-v5/`. Rapporté au plafond dur de 64 USD (GO-2026-11-22-24) : seul le pilote à **2 cycles** tient au pire sans relance ; aucun ne tient avec relances. Le contre-lecteur trouve les mêmes nombres à 3 et 4 cycles sur la v4 corrigée (65,39 et 83,54). La simulation du contre-lecteur (coût attendu, v4) : 22,30 USD à 3 cycles, 27,50 à 4 ; aucun nombre de cycles ne tient la tolérance de Fable par modèle (1,16 à 1,86 fois la référence). Ce sont des chiffres de travail : le devis du pilote (pièce décisive) revient à la mère et à Fable.

## Ouvert, pour la mère et Fable
- **Appariement avec le mode isolé** : les dossiers isolés de référence (protocoles X en cours) tournent sur la v8d, sans balises ; l'essaim sur la v8e sert au temps 0 une invite III.1 balisée. Le brouillon de l'essaim et le tour III.1 isolé n'ont plus la même consigne. À trancher avant le pilote (essaim sur la v8d pour la comparaison, ou jumeaux isolés rejoués sur la v8e).
- **Consigne finale** : elle reprend la seule ligne « Livrable » du tour III.3, donc sans la forme imposée, quelle que soit la place ; faut-il l'ajouter ?
- Place des balises au tour III.3 (`place_iii3`) : voir le rapport de la v8e.
- Nombre de cycles et plafond : voir le devis ci-dessus.
