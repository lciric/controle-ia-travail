# Contre-lecture 5, très ciblée sur la différence v4 → v5 du texte gelé — rapport recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 après 10:31 UTC, rapport rendu avant 10:33 UTC (bornes relevées
par `date -u`) ; il n'a pas écrit le texte. Brouillon relu : `texte-gele-volet-a-et-b-alpha-v5.md`,
`83f42ec1a1762193fefd19f271fc1d400028ef5898c6d80539d3be66cc83c410`. Recopié sans modification de fond.

---

## 1) Empreintes
- Rapport de la contre-lecture 4 : `6b4456164bc9762f156990ba1902b7930e83191eae8428071e027b4e2a8c880e` — conforme.
- v4 : `f7abab54ceb7abb9316102322e4fb167c7aa56dfd54aa5b2e0c737bbd94649c9` — conforme.
- v5 : `83f42ec1a1762193fefd19f271fc1d400028ef5898c6d80539d3be66cc83c410` — conforme.
- Différence fournie : `8ed0aff405ba8f24f6f8249e186696b80244c726afe4a4e94e29198faa05f7e4` ; identique, hors en-têtes, à `diff -u` v4 v5 régénéré.
- Validateur sur la v5 : `[]`.
- Aucun fichier modifié, aucun réseau, aucun appel de modèle, aucun chemin interdit ouvert, aucun refus de permission.

## 2) Verdict
**Scellable après corrections mineures** : une phrase résiduelle contredit la retouche de la remarque 4 (remarque 1 ci-dessous) ; le reste est de libellé.
- Les remarques 1 à 6 de la contre-lecture 4 sont appliquées comme le dit le tableau « Contre-lecture 4 », sauf le résidu de la remarque 4.
- Les remarques 7 et 8 sont honnêtement déclarées « noté, non appliqué », avec motif. L'erratum de la 8 concorde avec le rapport (fichier v2 daté de 10:12).
- La remarque 9 est déclarée constat, sentinelles non ajoutées : exact.
- Sur (b) : aucune issue non couverte ni règle inapplicable. L'attendu (i) de B.3 tient avec la nouvelle règle, d'après le minimum de 0,0008 relevé par le contre-lecteur 4 (donc aucun zéro écrit) ; je ne l'ai pas recalculé.

## 3) Remarques
**1. Mineure, à corriger — préambule, ligne 22 (description du correctif (2)).** Il reste « n = 31 lu à B0 sur la ligne imprimée, sinon arrêt ». La v5 dit ailleurs que notre code de B0 affirme `len(J) == 31` (B.1, (ii-e), liste R5) et a retiré « sur la ligne imprimée » de B.1. Correction : « n = 31 affirmé à B0 par notre code (B.1), sinon arrêt ».

**2. Mineure — audit R4, « B-α, trop beau » : « `control_med` écrit 0,0000 ».** `round(v, 4)` d'une valeur négative minuscule donne `-0.0`. Le texte ne dit pas si ce cas compte comme un zéro. Correction : « valeur écrite égale à 0 en valeur absolue (`0.0` ou `-0.0`) ».

**3. Mineure — Provenance, dernière phrase.** « recalculés … par les contre-lecteurs 1 à 3 (rapport, § 4 : tous en accord) » : changement non demandé par la contre-lecture 4 et absent du tableau de traitement ; le renvoi « rapport, § 4 » ne désigne que le rapport 1 ; les rapports 2 et 3 recalculent les verdicts et attendus de B.3, pas l'ensemble des chiffres publiés. Correction : revenir à « contre-lecteur 1 (rapport, § 4) » et ajouter « attendus de B.3 recalculés par les contre-lecteurs 2 et 3 ».

**4. Détail facultatif — B.1 et (ii-e).** « `len(J) == 31` pour chacun des trois fichiers » : `J` est aussi le nom d'une des trois lentilles. Écrire « nombre de couches lues == 31 pour chacun des trois fichiers (`J`, `npJpp`, `npR`) ».
