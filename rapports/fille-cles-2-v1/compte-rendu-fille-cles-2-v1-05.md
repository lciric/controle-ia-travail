# Fille clés 2 — compte rendu court 05 — surveillance ; « illisible » d'Argon en hausse

Heures par `date -u`. Nombres de `bloc-4-4-surveillance-principale-v1.sh` seulement.

| heure | processus 340 | A ok | A illisible | A tentatives | A cout_estime | B ok | B illisible | B tentatives | B cout_estime |
|---|---|---|---|---|---|---|---|---|---|
| 12:20:20Z | actif | 236 | 1 | 237 | 11.0162 | 235 | 0 | 241 | 7.2181 |
| 12:35:02Z | actif | 255 | 2 | 257 | 12.8024 | 255 | 0 | 261 | 7.7963 |
| 12:49:46Z | actif | 280 | 4 | 284 | 15.5561 | 282 | 0 | 288 | 8.404 |
| 13:04:25Z | actif | 304 | 6 | 310 | 18.3195 | 308 | 0 | 314 | 9.015 |

(Lecture `principale` seulement.) Dépense estimée cumulée à 13:04Z : 27.3345 (seuil 300).

## Sentinelle
Le lecteur A approche du seuil d'arrêt de la section 4.4 (8 « illisible » ou plus), à environ 2 par quart d'heure, alors que le guet ne rend la main que toutes les 14 minutes au plus. Ajout d'une sentinelle (`sentinelle-illisibles-v1.sh`, versée à côté avec son empreinte) : toutes les 60 secondes, compte des seuls statuts « illisible » de la lecture `principale` par lecteur (même lecture que `bloc-4-4`, aucun autre champ) ; à 8 pour un lecteur, arrêt de la lecture par son numéro (`kill` du numéro de `lecture-principale.pid`, vérifié par `kill -0`). Le relais est ensuite arrêté par l'exécutante (section 3.4 avec `RELAIS_P`). Garde testée (R5) sur un cas sain (7 : aucun arrêt) et sur un artefact (8 : arrêt, processus vérifié mort), dans un dossier factice. Lancée à 13:05Z, en plus du guet.
