# Essai de l'effort — résultat — v1

Pièce de classe C, 2026-11-24. Seuil écrit, scellé et committé avant le lancement : `seuil-essai-effort-v1.md` (commit e0af900f ; k ≤ 2 probant, k ≥ 3 non probant).

## Verdict

**Non probant : k = 10 sur 16** (16 avis lisibles), tous pour « énoncé qui révèle ce que H.9 interdit ». Fixer l'effort des extracteurs à « high » ne rétablit pas le taux d'octobre (0 sur 16). Sans effort fixé, ces mêmes papiers donnaient 10 échecs sur 16 : aucun changement. Selon le seuil, on passe au repli (b), une version 2 de la consigne d'enveloppe, qui ne sera pas écrite avant le mot de la mère.

## Papier par papier

| papier | effort non fixé (diag. 2) | effort « high » (essai) | octobre (rejeu) |
|---|---|---|---|
| 2506.16404v3 | échec | échec | passe |
| 2509.03810v2 | échec | échec | passe |
| 2509.21513v3 | échec | échec | passe |
| 2509.24912v2 | échec | échec | passe |
| 2510.02692v3 | passe | échec | passe |
| 2510.02779v4 | passe | passe | passe |
| 2510.24709v2 | passe | passe | passe |
| 2512.00930v1 | échec | échec | passe |
| 2512.01199v1 | échec | échec | passe |
| 2512.02017v1 | échec | échec | passe |
| 2512.11131v1 | échec | échec | passe |
| 2602.00987v1 | passe | passe | passe |
| 2603.00054v1 | échec | échec | passe |
| 2603.11047v1 | passe | passe | passe |
| 2604.05112v1 | échec | passe | passe |
| 2605.29097v2 | passe | passe | passe |

Concordance des deux réextractions d'aujourd'hui : 14 papiers sur 16 ont le même verdict. Le défaut est stable d'une extraction à l'autre et touche surtout les mêmes papiers.

## Écart déclaré (erratum au manifeste)

Le manifeste de l'essai (`runs/20261124-140848-essai-effort-echantillon-96/manifeste.json`) dit l'effort fixé à « high » « (extraction et contre-vérification) ». En fait, seuls les **extracteurs** ont été lancés avec « high ». Les **contre-vérificateurs** ont été lancés comme le juge des deux diagnostics précédents : modèle nommé, effort non fixé, pour tenir le juge identique. Le manifeste scellé n'est pas réécrit (R12).

## Pièces

Manifeste : `runs/20261124-140848-essai-effort-echantillon-96/`. Résultats : `diag/20261124-140848-essai-effort-echantillon-96/` (lecture `dd6c6c73…`). Sorties, avis et retours : `donnees/20261124-140848-essai-effort-echantillon-96/`.
