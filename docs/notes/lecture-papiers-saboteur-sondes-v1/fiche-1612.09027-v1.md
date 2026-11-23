# Fiche de lecture — 1612.09027 — v1

- **Titre** : On Covert Communication with Noise Uncertainty.
- **Auteurs** : Biao He, Shihao Yan, Xiangyun Zhou, Vincent K. N. Lau. **Identifiant** : arXiv 1612.09027 v1 (décembre 2016, 4 pages).
- **PDF** : `docs/sources/pdf/percee-controle-securite-v1/1612.09027v1.pdf`, sha256 `93e703413d59640f1f14d3f97b42a5602a64579a2a84264eaabefb0926fad602` (vérifiée par `sha256sum`).
- **Décision lue** : `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, ligne 72, avec ses errata 1 et 2, qui ne touchent pas ce passage.
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:45Z (`date -u`).

## (a) Ce que le papier établit

Le papier part de la loi en racine, O(√n) bits en n usages, et d'un résultat antérieur. Selon ce dernier, l'incertitude du guetteur sur son bruit rend un débit constant non nul (p. 1 du PDF). Les auteurs montrent que cette analyse au pire, du point de vue du guetteur, est « overly optimistic » (p. 1). Le guetteur y est supposé au pire bruit possible, ce qui ne garantit aucun niveau réel de discrétion (p. 2). Ils mesurent plutôt la discrétion en moyenne sur la loi du bruit, et par probabilité de panne. Le guetteur est un détecteur de puissance avec un nombre d'échantillons infini (p. 1). Le débit discret grandit avec l'incertitude et tend vers zéro sans elle (p. 4). Leur conclusion : un débit positif reste possible pour une probabilité de détection faible mais non nulle. Il tend vers zéro quand cette probabilité tend vers zéro, quel que soit le niveau d'incertitude (p. 4). L'analyse au pire « overestimates the covertness » (p. 4).

## (b) Ce que voulait la décision, et si le papier le permet

La décision citait ce papier, avec 1608.00698, pour un guetteur qui laisse passer un débit constant faute de connaître son bruit. **Le papier ne le permet pas tel qu'écrit ; il dit plutôt l'inverse.** Le débit constant n'existe que si l'on tolère une probabilité de détection fixe. Sous exigence de discrétion parfaite, le débit s'annule. C'est une limite du résultat antérieur, et non un trou du champ (R8). Le papier est un contre-indice qu'il faut citer à côté du revers.

## (c) Usage pour l'entretien et pour le billet

Il prévient une erreur de notre côté : dire « l'incertitude sur l'honnête laisse passer un saboteur à débit constant » sans dire à quel taux de détection. Il fournit aussi une règle de lecture pour la prévision de la référence honnête : rapporter toute borne en moyenne sur la loi du biais, jamais au pire seul. Le pire flatte celui qui se cache, ici le saboteur.

## (d) Plus petite action

Au prochain erratum de N-076, écrire 1612.09027 comme nuance de 1608.00698. Le débit constant tient à probabilité de détection fixée et s'annule quand elle tend vers zéro (p. 4). Coût : dix minutes, aucune dépense.
