# Vérification des corrections — devis de la garde des activations du barreau 5, v2 — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), le contre-lecteur de la v1 (rapport `contre-lecture-devis-garde-activations-volume-v1.md`, `1d0e7861d935a23b122d8df9d4fb0aea7d2bd761b47bf8874111feb6d228ce00`). Vérification courte, 21 novembre 2026 vers 11:30Z. Aucun appel de réseau, aucune dépense.
- **Pièce vérifiée** : `devis-garde-activations-volume-v2.md` (`8112974bbef45b315c7fe448dc0bd8ab05df46d23613a662a3f85926c01649dc`), calcul `calcul-devis-garde-activations-volume-v2.py` (`ddab89e1…`), sortie `sortie-calcul-devis-garde-activations-volume-v2.txt` (`9b557d66…`), même dossier. Compagnons concordants. Lue par différence ligne à ligne avec la v1.

## Verdict

**Conforme, prêt à sceller comme base d'une ligne d'accord**, avec un erratum d'en-tête sur l'heure (point 4), qui ne touche ni un chiffre ni la ligne d'accord.

## 1. Les corrections

| correction | portée | constat |
|---|---|---|
| A-1 (bloquante) | oui | l. 34 (fin de la puce « Coupures »), l. 45, l. 46, l. 75 : texte exact |
| A-2 (bloquante) | oui | l. 34 et l. 35 : texte exact |
| A-3 | oui, écart de lettre | l. 20, l. 31 ; l'adresse IPv4 est comptée au calcul (bloc 3) au lieu d'être dite « non comptée ». **Acceptable, et meilleur** : 0,069 EUR, 18,85 EUR et 23,56 USD ont désormais une pièce rejouable ; les chiffres sans l'adresse restent imprimés à côté ; le plafond ne change pas ; le bas et l'attendu gagnent un centime d'euro (4,19 et 13,87 EUR ; 17,33 USD), l'oubli d'un serveur passe à 72,65 USD (57,516 + 0,50 × 1,2 = 58,116 EUR) : refait à la main, juste |
| A-4 | oui | l. 59, l. 61 : texte exact ; le calcul compte désormais les cinq offres (bloc 6) |
| A-5 | oui | l. 37 : texte exact |
| A-6 | oui, écart de lettre | l. 77, option (d), et l. 52, l. 68. « 3,6 fois » au lieu de « quatre fois » : **acceptable, et plus juste** (17,16 / 4,80 = 3,575). Le prix du volume et les deux choses à vérifier ajoutées à l'option ne changent pas son statut, « à vérifier avant d'être proposée » |
| A-7 | oui | l. 7 : texte exact |

Les changements hors de la liste sont déclarés au § 11 et ne touchent ni le plafond, ni l'échéance, ni la recommandation. Un seul fait neuf porte un choix : « la formation finit au plus tard le 22 novembre » (l. 77), relu dans `registres/passations/2026-11-21-0745.md`, l. 8 (« fin au plus tard le 22 à 18:30:16Z ») : juste. Le § 10 (relevé de méthode) dit lui-même que le pas 5 (lecture d'un volume attaché seulement) et le pas 7 (la minuterie, sans code ni épreuve) sont supposés : honnête.

## 2. Rejeu

Le programme v2 ne fait aucun appel de réseau (mêmes imports, mêmes deux fichiers lus). Rejoué par `.venv/bin/python -I docs/notes/barreau5-resolution-v1/plan-avant-entretien/calcul-devis-garde-activations-volume-v2.py` : **identique à l'octet** (`cmp`), code de sortie 0 ; les quatre objets de contrôle du bloc 7 rendent leur attendu.

## 3. La ligne d'accord finale

`l. 75` : huit colonnes, aucune barre verticale dans une cellule ; type « calcul » ; plafond 24 USD, échéance 2026-12-21 ; elle cite le devis v2 ; la garde sans séance après l'échéance ou au plafond y est écrite (0,57 USD par jour, compté au-delà du plafond), comme la question du 14 décembre. Elle tient, et elle s'accorde avec le § 3, le § 5 et le calcul (pire cas 23,56 USD, marge 0,44).

## 4. Les heures d'écriture

L'en-tête dit la v2 écrite « de 11:17 à 11:45 UTC ». Sur disque, le fichier est daté de 11:25:05Z et le commit `888d7562b` de 11:27:10Z ; à 11:28Z (`date -u`), 11:45 était encore à venir : l'heure de fin est fausse, l'auteur le reconnaît (fin à 11:25Z). **Cela vaut un erratum**, court, scellé à côté du devis avant ou avec son scellement, et cité par la ligne de scellement : une pièce de classe A scellée ne doit pas porter un fait de provenance qu'on sait faux. Il ne demande ni une v3 ni une nouvelle vérification : il ne touche aucun chiffre, aucune condition, aucune ligne de la ligne d'accord. Texte : « En-tête, puce « Auteur » : lire « la v2 le même jour, de 11:17 à 11:25 UTC » au lieu de « de 11:17 à 11:45 UTC » (fichier daté de 11:25:05Z, commit `888d7562b` à 11:27:10Z). »
