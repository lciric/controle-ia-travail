# Erratum 1 — Conception 1 — le hasard du défenseur comme preuve — v2

- **Cet erratum prime sur la v2** : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v2.md` — sha256 47387ebf64c1569fce45a75c31aeae03fc4315c21b43f7581eefd4866e2ed51f (compagnon vérifié). La v2 n'est pas réécrite ; elle se lit avec cet erratum.
- Source des couples : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/verification-conception-1-v2-opus-v1.md` — sha256 3c0c4bc110d442607b9cae54707ea9c8d627d060940bd09e8341d14d7edf80d1 (compagnon vérifié), section « Couples restants ».
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-1-conceptions-v2-v1.py` — sha256 e75e7a49afc57620f477ea6f2852ef17ed6b7d40fa948298720b3c77166014d0.
- Vérifications du programme : chaque ancien figure une seule fois dans la v2 ; appliqués dans l'ordre ci-dessous, chaque ancien est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne exactement la v2.
- Couples (9), à appliquer dans l'ordre : E1.1 ; E1.2 ; E2 ; E3 ; F1.1 ; F1.2 ; F1.3 ; F2 ; F3.

## E1.1 — Conclusion : le contraste dit « exact », et la trouvaille sans ses suppositions (suite des constats 4 et 8, effet sur le fond)

Ancien :
```text
Le contraste avec le jumeau se teste exactement par la même permutation, appliquée à la différence appariée saboteur moins jumeau.
```

Nouveau :
```text
Le contraste avec le jumeau se teste par la même permutation, appliquée à la différence appariée saboteur moins jumeau, avec une statistique studentisée : exact pour le nul en loi, approché pour le seul nul des moyennes (§ 3).
```

## E1.2 — Conclusion : le contraste dit « exact », et la trouvaille sans ses suppositions (suite des constats 4 et 8, effet sur le fond)

Ancien :
```text
la détection par l'audit ne dépend pas de la stratégie du saboteur
```

Nouveau :
```text
la détection par l'audit ne dépend pas, au premier ordre et en régime de signature, de la stratégie du saboteur
```

## E2 — Multiplicité : le « nul strict » qu'on n'emploie plus (suite du constat 1, effet sur le fond)

Ancien :
```text
(Westfall et Young), exact sous le nul strict global.
```

Nouveau :
```text
(Westfall et Young), exact sous le nul en loi global (§ 2).
```

## E3 — Ordre d'écriture, pièce 6 : la mort par désaccord à toute corrélation (suite du bloquant, constat 3, et du constat 12 ; cohérence)

Ancien :
```text
| 6. Table de puissance simulée | accord avec la table du § 4 à 0,10 près | désaccord : mort |
```

Nouveau :
```text
| 6. Table de puissance simulée, cas sain de G5 compris | à corrélation intra-tâche 0, accord avec la table du § 4 à 0,10 près | à corrélation 0, désaccord : mort ; aux corrélations positives, la table simulée remplace l'approximation, sans mort (test de mort 1) |
```

## F1.1 — Antériorités en vraies puces (constat 10, mise en forme)

Ancien :
```text
section 11) ; - Krakovna
```

Nouveau :
```text
section 11) ;
- Krakovna
```

## F1.2 — Antériorités en vraies puces (constat 10, mise en forme)

Ancien :
```text
section 11) ; - voisins
```

Nouveau :
```text
section 11) ;
- voisins
```

## F1.3 — Antériorités en vraies puces (constat 10, mise en forme)

Ancien :
```text
2610.37055) ; - Chung
```

Nouveau :
```text
2610.37055) ;
- Chung
```

## F2 — « Appariement » en puce propre (constat 6, mise en forme)

Ancien :
```text
vérifications. - **Appariement.**
```

Nouveau :
```text
vérifications.
- **Appariement.**
```

## F3 — « Grandeurs secondaires plantées » en puce propre (constat 13, mise en forme)

Ancien :
```text
N/6. - **Grandeurs secondaires plantées**
```

Nouveau :
```text
N/6.
- **Grandeurs secondaires plantées**
```
