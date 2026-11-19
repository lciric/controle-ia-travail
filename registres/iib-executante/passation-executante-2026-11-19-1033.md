# Passation de l'exécutante du saboteur à budget — 2026-11-19T10:33:55Z

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Exploratoire, non opposable (R-522). Suite du journal v8 (`journal-v8.md`, `969fd543…1d00`) ; pièces de la course sous `registres/iib-executante/course-836c7ccc-v1/`.

## Fait
- Remise reçue (R-3684). § 5 de l'ordre scellé (`43a7a050…1b3e`) joué avec l'écart de forme R-3683 (PATH vers l'outil de location).
- Création : premier essai en code 4 (création incertaine, aucune instance ; réponse brute effacée par `apres-creation`) ; second essai (R-3687, réponse brute gardée) : **instance 61414494** créée à 2026-11-19T08:54:06Z, A100 SXM4 80 Go, 1,22 USD/h.
- Course `20261119-085912-iib-reel` : suite « 456 passed » sur l'instance ; étalonnage complet ; **arrêt à l'épreuve E-O1** (centrage) à 10:13:45Z (R-3717). Débit J7 : 0,511 s par action.
- Rapatriement : 6 fichiers sur 6 vérifiés, aucun écart ; inventaire et journaux versés avant destruction (commits de9f3088, 22a44015).
- Destruction : premier essai sans effet (confirmation interactive, « Aborted », code 0 ; cas M-018) ; second essai avec `-y` (R-3722) à 10:20:55Z : `{"instances": null}`, plus aucune instance « iib ».
- Diagnostic par un sous-agent neuf du côté du saboteur : `diagnostic-epreuve-E-O1-20261119-085912-iib-reel-v1.md` (`12bfbc78…5fc6`) ; vérification de l'asymétrie des lecteurs du coût (`15d35d9b…b41b`) : défaut de code **non**, propriété réelle de l'oracle ; fiche de décision pour Lazar (`8c4257d1…72ac0`) et résumé sans chiffre (`f4fbb1be…1493`).
- Lazar a tranché : « go recos, A et B avec relance accordée » (GO-2026-11-19-38, R-3727). A et B conduits par une session neuve, `session_013QMayiwfx2DB6CHn9yZ2wH`.

## Réserves
- Écart du sous-agent (lecteurs du coût exécutés sur des chaînes inventées, hors du permis) : consigné R-3726. Règle retenue : dans tout mandat de sous-agent, nommer les gestes interdits un par un.
- Défauts du lanceur relevés : `apres-creation` efface la réponse brute du loueur ; la commande de destruction de l'ordre n'a pas `-y`.
- Coût de la course : estimé 1,7 à 2,7 USD (carte ≈ 1,64 USD, stockage, forfait de téléchargement), facture non lue.

## Reste / prochaine action
- Répondre à la session de reconception (`session_013QMayiwfx2DB6CHn9yZ2wH`) pour les contrôles à blanc au commit de lancement neuf : noms, états, empreintes.
- Aucune création, aucun appel au loueur avant une nouvelle remise de la mère ; création au plus tard le 2026-11-25T23:00Z.

## Instances actives
- Aucune instance de cette session (61414494 détruite). Instances d'autres sessions vues à 10:21:12Z, intouchables : 58936096, 58936099, 58936100, 60988826.
