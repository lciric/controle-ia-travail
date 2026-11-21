# Vérification des corrections — devis de la part du lot honnête neuf qui étalonne les deux verdicts principaux du bras « papier dopamine », v2 — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), le contre-lecteur de la v1 (rapport `contre-lecture-devis-lot-l-1-v1.md`, `8bfdbd027112267fda841b973edac991fb5f36c22bc64878021628a48903285d`). Vérification courte, 21 novembre 2026 vers 11:30Z. Aucun appel de réseau, aucune dépense.
- **Pièce vérifiée** : `devis-lot-l-1-v2.md` (`a31d53e0a68e76a182f9305fedcadb2d6714249111ff330273526d1b7cc9766e`), calcul `calculs-devis-lot-l-1-v2.py` (`1c56ef84…`), sortie `calculs-devis-lot-l-1-v2.txt` (`76524524…`), même dossier. Compagnons concordants. Lue par différence ligne à ligne avec la v1.

## Verdict

**Conforme, prêt à sceller comme base d'une ligne d'accord**, avec un erratum d'en-tête sur l'heure (point 4), qui ne touche ni un chiffre ni la ligne d'accord.

## 1. Les corrections

| correction | portée | constat |
|---|---|---|
| B-1 (bloquante) | oui | l. 119, ligne d'accord : texte exact |
| B-2 | oui | l. 119 : texte exact ; l. 69 et l. 74 mises en accord ; le calcul chiffre deux instances (bloc 9) : 41,86 USD à la borne haute avec des hôtes 1,5 fois plus lents, couverture jusqu'à 1,31 fois, arrêt vers 1 071 épisodes. Refait : (37 − 4,10) / 1,38 = 23,84 h ; (23,84 − 0,5 − 1,5 × 3,6) / (1,5 × 40,2 / 3 600) = 1 071 : juste |
| B-3 | oui | l. 103 : texte exact |
| B-4 | oui | l. 32 : texte exact |
| B-5 | oui | l. 66 : texte exact |
| B-6 | oui | l. 54 et l. 93 : texte exact |

Changements hors de la liste, déclarés au § 13 : le pire cas sous la borne de l'offre, 47,5 USD (l. 67), que j'avais refait à la main, désormais rejouable (bloc 9) ; le compteur commun aux deux instances (l. 74) ; le relevé de méthode (§ 12). Aucun ne change la règle d'achat, la grille, la borne haute, la coupure, l'échéance ni la recommandation (b). Les blocs 1 à 8 de la sortie v2 sont identiques à ceux de la v1 (différence des sorties : seul le titre et les blocs 9 et 10 neufs).

## 2. Rejeu

Le programme v2 ne fait aucun appel de réseau (mêmes imports, seul le relevé voisin est lu). Rejoué par `.venv/bin/python -I prereg/papier-dopamine-moniteur-v1/calculs-devis-lot-l-1-v2.py` : **identique à l'octet** (`cmp`), code de sortie 0 ; les seize objets de contrôle du bloc 10 rendent leur attendu, dont la voie indépendante 1 − 0,99ⁿ pour 368 et 437.

## 3. La ligne d'accord finale

`l. 119` : huit colonnes, aucune barre verticale dans une cellule ; type « calcul » ; plafond 37 USD, échéance 2026-12-15 ; elle cite le devis v2 ; la cible (437 visés, 368 pour la seule première question, rien sinon) suit la règle du § 3 ; « une instance, deux au plus, sous la coupure commune » suit le § 5 et le bloc 9 ; conditions de validité écrites. Elle tient. La recommandation reste (b) : ne l'accorder qu'après l'addendum de l'étape 2a.

## 4. Les heures d'écriture

L'en-tête dit la v2 écrite « de 11:17 à 11:50 UTC ». Sur disque, le fichier est daté de 11:25:05Z et le commit `888d7562b` de 11:27:10Z ; à 11:28Z (`date -u`), 11:50 était encore à venir : l'heure de fin est fausse, l'auteur le reconnaît (fin à 11:25Z). **Cela vaut un erratum**, court, scellé à côté du devis avant ou avec son scellement, et cité par la ligne de scellement : une pièce de classe A scellée ne doit pas porter un fait de provenance qu'on sait faux. Il ne demande ni une v3 ni une nouvelle vérification : il ne touche aucun chiffre, aucune condition, aucune ligne de la ligne d'accord. Texte : « En-tête, puce « Auteur » : lire « la v2 le même jour, de 11:17 à 11:25 UTC » au lieu de « de 11:17 à 11:50 UTC » (fichier daté de 11:25:05Z, commit `888d7562b` à 11:27:10Z). »
