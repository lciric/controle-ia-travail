# Réponses des questions témoins — réserve v1 — NE PAS SERVIR

Pièce séparée des questions (règle 2). Les calculs sont refaits par `scripts/temoins_v1.py` ; les faits publiés sont lus à la page dite, le passage attendu figurant mot pour mot dans la sortie de `pdftotext` (le script échoue sinon).

| id | sorte | réponse | tolérance ou source |
|---|---|---|---|
| C-01 | calcul refait par code | 2995 | entier exact |
| C-02 | calcul refait par code | 0.8674 | ±0,0001 |
| C-03 | calcul refait par code | 2 | entier exact |
| C-04 | calcul refait par code | 0.4 | ±0,01 |
| C-05 | calcul refait par code | 0.18 | ±0,005 |
| C-06 | calcul refait par code | 0.0711 | ±0,0001 |
| C-07 | calcul refait par code | 0.0547 | ±0,0001 |
| C-08 | calcul refait par code | (2.773, -1.558) | ±0,001 chacune |
| C-09 | calcul refait par code | 0.025 | exact (0,025) |
| C-10 | calcul refait par code | 0.00417 | ±0,00001 |
| P-01 | fait publié, PDF du dépôt, à la page | 80 % | docs/sources/pdf/2411.17693v1.pdf, page 1 du fichier : « reduces the number of backdoors by 80% compared to non-adaptive baselines » |
| P-02 | fait publié, PDF du dépôt, à la page | de 100 % à 0 %, en gardant 90 % | docs/sources/pdf/2412.09565v2.pdf, page 1 du fichier : « reduce recall from 100% to 0% while retaining a 90% jailbreaking rate » |
| P-03 | fait publié, PDF du dépôt, à la page | 5 000 | docs/sources/pdf/2312.06942v5.pdf, page 3 du fichier : « solve 5,000 » |
| P-04 | fait publié, PDF du dépôt, à la page | cinq (M1 à M5) | docs/sources/pdf/2504.05259v1.pdf, page 1 du fichier : « five fictional models (M1-M5) » |
| P-05 | fait publié, PDF du dépôt, à la page | non, impossible sans hypothèse sur la loi | docs/sources/pdf/1903.04684v2.pdf, page 1 du fichier : « exact conditional inference guarantees are known to be impossible without imposing assumptions » |
| P-06 | fait publié, PDF du dépôt, à la page | Statistical Science, 2008, volume 23, numéro 1 | docs/sources/pdf/0808.0572v1.pdf, page 1 du fichier : « Statistical Science 2008, Vol. 23, No. 1 » |

Notation : exactitude = part des réponses justes à la tolérance dite ; score de Brier = moyenne de (confiance − juste)², juste valant 1 ou 0.
