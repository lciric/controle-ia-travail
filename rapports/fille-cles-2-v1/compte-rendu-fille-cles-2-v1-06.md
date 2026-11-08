# Fille clés 2 — compte rendu court 06 — lecture principale finie chez les deux lecteurs, relecture en cours

Heures par `date -u`. Nombres de `bloc-4-4-surveillance-principale-v1.sh` seulement.

| heure | 340 | A principale ok | A principale illisible | A relecture ok | A relecture illisible | A tentatives | A cout_estime | B principale ok | B illisible | B relecture ok | B tentatives | B cout_estime |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13:19:50Z | actif | 334 | 6 | 0 | 0 | 340 | 19.6179 | 338 | 0 | 0 | 344 | 9.6536 |
| 13:34:33Z | actif | 362 | 6 | 0 | 0 | 368 | 20.7941 | 366 | 0 | 0 | 372 | 10.2229 |
| 13:49:13Z | actif | 385 | 6 | 0 | 0 | 391 | 21.7757 | 389 | 0 | 0 | 395 | 10.7423 |
| 14:03:53Z | actif | 389 | 7 | 16 | 1 | 413 | 24.4404 | 396 | 0 | 15 | 417 | 11.291 |

- Lecture `principale` de A terminée : 389 + 7 = 396 ; **7 « illisible » (1,77 % de 396), sous le seuil d'arrêt de 8** ; la sentinelle ne compte que la lecture principale et ne peut plus se déclencher. B : 396 « ok », 0 illisible.
- Dépense estimée cumulée à 14:03Z : 1.164904 + 24.4404 + 11.291 = 36.8963 (seuil 300).
- Échanges avec la mère depuis le compte rendu 05 (par `send_message`, nombres et codes seulement) : nature des illisibles de A (`promptFeedback.blockReason` = OTHER, réponse 200, aucun candidat, coût estimé = réservation au pire cas, ligne 505) ; longueurs des consignes (rangs 24 à 45 sur 341, pas les plus longues) ; décisions de la mère R-1809, R-1811, R-1814.
- Mots de Lazar dans cette session, transmis à la mère : « go par anticipation pendant 8h a tout ce que voudra faire la session mere , go depenses » (13:33:57Z, inscrit GO-2026-11-08-09) ; « go » ; « course de l’organisme sur la v1 go » (13:36:55Z, destiné à la fille idéation 2 selon la mère, non exécuté ici).
