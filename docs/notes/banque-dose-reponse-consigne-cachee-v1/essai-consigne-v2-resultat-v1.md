# Essai de la consigne d'enveloppe v2 sur les 16 papiers d'octobre — résultat — v1

Pièce de classe C, 2026-11-24, session fille d'extraction. Seuil écrit, scellé et committé avant le lancement : `seuil-essai-consigne-v2-v1.md` (`5b682899…`, commit `dd1b7717`). Run : `runs/20261124-144227-essai-consigne-v2-echantillon-96/` ; lecture : `diag/20261124-144227-essai-consigne-v2-echantillon-96/lecture-rejeu.json` (`c6e50de4…`).

## Verdict

**Probant.** Il y a 1 papier en échec sur 16 avis lisibles (k = 1 ≤ 2). Son motif est « énoncé qui révèle ce que H.9 interdit ». Aucun avis illisible, aucune réextraction invalide, aucun « theory_only ». Selon le seuil scellé, on passe à l'extraction des 80 papiers sous la consigne v2.

## Conditions

- La consigne d'enveloppe v2 est scellée (`44da46b3…`). La garde de la v2 a vérifié la marque de l'étape 2b dans chacun des 16 dossiers.
- Extracteurs et contre-vérificateurs : modèle nommé à l'appel, effort non fixé, comme à l'extraction de la banque. Un lancement par agent, aucune relance.
- Contre-vérificateur : consigne v1 inchangée, même mécanique de lecture (copie textuelle de la lecture du premier rejeu).

## Repères (non décisifs)

| condition, mêmes 16 papiers | échecs | énoncés : longueur médiane (min–max), en caractères | sous 200 caractères |
|---|---|---|---|
| octobre (énoncés scellés, juge d'aujourd'hui) | 0 | — | — |
| réextraction d'aujourd'hui, consigne v1 | 10 | 3 623 (2 569–5 831) | 0 |
| idem, effort « high » | 10 | 3 523 (2 652–5 501) | 0 |
| **réextraction d'aujourd'hui, consigne v2** | **1** | 3 426 (2 684–5 488) | 0 |

Les longueurs répondent à la remarque CV2-6 de la contre-lecture. Ce sont des compteurs calculés par programme sur les sorties archivées ; aucun énoncé n'a été lu. L'étape 2b n'appauvrit pas les énoncés : la médiane baisse d'environ 5 %, et aucun n'approche le plancher de 200 caractères.

## Réserve (R4)

Le passage de 10 à 1 échec est net. C'est l'effet visé, mais un résultat aussi propre appelle le même audit qu'un résultat sale. L'extraction des 80 garde l'audit R4 de sa procédure : le côté propre est audité par des contre-vérificateurs neufs. Le juge reste celui qui a fait échouer 10 papiers sur 16 sous la v1. Ce n'est donc pas un juge plus indulgent qui fait passer les énoncés. Un même modèle écrit et juge les énoncés. Cette limite, déjà déclarée, demeure.
