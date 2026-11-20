# Rapport du développeur — calcul des conditions du plafond à 200 témoins (ligne 3) — v2

Pièce d'instrument (classe B), 2026-11-20. Même développeur que la version 1, modèle O ; même mandat (`10f22d1c…`) et mêmes interdits. Sur la demande de la mère, à la suite de la contre-lecture `contre-lecture-calcul-plafond-200-v1.md` (`9adbe32d34dc62948c48fe57aea059f7c804e69fb876a5a5073afa43af739bcc`, empreinte recalculée égale, lue en entier ; verdict « Conforme », § 5 : correction de texte ; § 1 : essais liés au bloc-notes). La version 1 est gardée sans modification.

## Ce qui change

1. **Texte du modèle des refus** (docstring et `regle_du_compteur.texte` de la sortie), mis au texte exact demandé : « un envoi refusé (refusé, coupé par un délai, en erreur) est compté 0,60 USD puis rejoué une fois, avec succès, à son coût ; un envoi revenu sans coût lisible est compté 0,60 USD et n'est pas rejoué (texte l. 193) ; le modèle des refus ne joue que la première forme ». Dans la sortie, cette phrase prend la place de « un envoi refusé, coupé, en erreur ou sans coût lisible est compté 0,60 USD ; rejeu unique ». La première clause (règle d'engagement) et la dernière (coût relevé au-dessus de 0,60 USD) restent. « Engagement sans règlement » n'est plus nommé dans la docstring : il ne l'est pas dans le texte demandé.
2. **Nom et version** : `VERSION = "calcul-conditions-plafond-200-ligne-3-v2"` (règle R12) ; le message d'usage porte le nom v2. Aucune fonction de calcul n'est touchée.
3. **Essais** : ils importent le calcul v2 et lisent le devis v7 scellé par un chemin du dépôt (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/devis-ligne-3-etage-payant-v7.md`, empreinte `382ea448…` vérifiée par l'essai) ; ils ne dépendent plus du bloc-notes. Un essai de plus : le texte de la règle porte la phrase demandée et plus « rejeu unique ».

## Fichiers (bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-calcul-plafond-200/`, chacun avec son compagnon)

| fichier | sha256 |
|---|---|
| `calcul_conditions_plafond_200_ligne_3_v2.py` | `86440df6f81d0c185a8aab375b67ba67a4c09351716dc17acc8988bbc9f098bf` |
| `calcul-conditions-plafond-200-ligne-3-v2.json` | `fe58be3a790ee28db3fadb6370251a69c4378dc887e977a19ab77fd9093eb3e2` |
| `rejeu-calcul-conditions-plafond-200-ligne-3-v2.json` (second jeu) | `fe58be3a790ee28db3fadb6370251a69c4378dc887e977a19ab77fd9093eb3e2` |
| `essais_calcul_conditions_plafond_200_v2.py` | `10672098008cc61b7777f2108629412fece68c1e59fc33c7e94853fc6d12b594` |
| `differentiel_sorties_plafond_200_v1_v2.py` | `b8be019c2df2c5d3d5de7e7c1512803b5fab5f922edf78d3fc96c0e1ef89e504` |
| `differentiel-sorties-plafond-200-v1-v2.json` | `6dc90ba69b5b5928a55a0b398cc0b20c33f07647a318f158499fce0e822cbaea` |
| ce rapport | dans son compagnon |

- Sortie jouée deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN > SORTIE`) : égale à l'octet.
- Essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_calcul_conditions_plafond_200_v2.py` : **20 passés** (les 19 de la v1, plus celui du texte).

## Le différentiel des sorties v1 → v2

Un programme lit les deux sorties par empreinte et les compare feuille par feuille, en décimal exact. Chacune a 489 feuilles, et **2 diffèrent** :
- `regle_du_compteur.texte` : la correction demandée ;
- `version` : `…-v1` → `…-v2`, qui suit le nom neuf.

**Aucun chiffre ne change.** Seule la clé `version` s'ajoute au champ texte attendu. Le différentiel ne pouvait pas montrer le seul champ texte sans garder « v1 » dans la sortie d'une v2. Je l'ai jugé contraire à la règle R12 ; c'est à confirmer par la mère.

## Remarques

- Les deux points que la contre-lecture porte à la mère ne touchent pas ce calcul : citer l. 388 avec l. 337 au scellement de l'additif de code, et le plafond de 88,36 USD sous le pire de 88,3617 USD.
- La liste `hypotheses_de_modele` de la sortie n'est pas changée. Sa ligne « un envoi refusé est compté 0,60 USD puis rejoué une fois avec succès » ne nomme pas le « sans coût lisible » et reste juste.

Aucun refus de permission, de classifieur ou de garde ; aucune écriture dans le dépôt ; aucun appel payant.

Développeur, modèle O.
