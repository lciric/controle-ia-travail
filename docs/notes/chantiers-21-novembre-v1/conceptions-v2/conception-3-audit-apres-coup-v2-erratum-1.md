# Erratum 1 — Conception 3 — l'audit après coup — v2

- **Cet erratum prime sur la v2** : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v2.md` — sha256 a8dac56d8ae80f54efdbf438e094b53d8564d33ad86b5e09a3597762e948005e (compagnon vérifié). La v2 n'est pas réécrite ; elle se lit avec cet erratum.
- Source des couples : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/verification-conception-3-v2-opus-v1.md` — sha256 a00992447d32894e243c6963c4f543b903328d2a665993d0bef0117a39cb976a (compagnon vérifié), section « Couples restants ».
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-1-conceptions-v2-v1.py` — sha256 e75e7a49afc57620f477ea6f2852ef17ed6b7d40fa948298720b3c77166014d0.
- Vérifications du programme : chaque ancien figure une seule fois dans la v2 ; appliqués dans l'ordre ci-dessous, chaque ancien est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne exactement la v2.
- Couples (3), à appliquer dans l'ordre : R-1 ; R-2 ; R-3.

## R-1

Ancien :
```text
C'est elle qui porte la borne et l'alerte ; l'estimateur pondéré par l'inverse est rapporté à côté, selon la lettre.
```

Nouveau :
```text
C'est elle qui porte la borne et l'alerte d'excès (en signature, toute prise, de toute source, alarme) ; l'estimateur pondéré par l'inverse est rapporté à côté, selon la lettre.
```

## R-2

Ancien :
```text
1. **La strate du plancher porte la borne et l'alerte ; l'estimateur pondéré complet est rapporté à côté.**
```

Nouveau :
```text
1. **La strate du plancher porte la borne et l'alerte d'excès ; en signature, toute prise alarme ; l'estimateur pondéré complet est rapporté à côté.**
```

## R-3

Ancien :
```text
- Auer et al. (2002, plancher d'exploration).
```

Nouveau :
```text
- Auer et al. (2002, le mélange d'exploration γ de l'algorithme Exp3 : un rapprochement avec le plancher, non une antériorité du plancher d'audit).
```
