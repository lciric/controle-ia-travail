## Tables des valeurs prédites (sans tirage)

### Famille S — bornes exactes de la puissance de `coelev_comptage` (seuil exact sous P₀)

| config | m | m/K | seuil (c, γ) | borne basse | borne haute | HS.4 |
|---|---|---|---|---|---|---|
| e10x10 | 3 | 0.3 | (4 ; 0.3228) | 0.1214 | 0.1216 | au-dessus |
| e10x10 | 4 | 0.4 | (4 ; 0.3228) | 0.2265 | 0.2267 | au-dessus |
| e10x10 | 5 | 0.5 | (4 ; 0.3228) | 0.3775 | 0.3776 | au-dessus |
| e10x10 | 6 | 0.6 | (4 ; 0.3228) | 0.5411 | 0.5411 | au-dessus |
| e10x10 | 7 | 0.7 | (4 ; 0.3228) | 0.6864 | 0.6864 | au-dessus |
| e10x10 | 10 | 1.0 | (4 ; 0.3228) | 0.9285 | 0.9285 | au-dessus |
| e20x10 | 6 | 0.3 | (6 ; 0.3165) | 0.3015 | 0.3016 | au-dessus |
| e20x10 | 8 | 0.4 | (6 ; 0.3165) | 0.5499 | 0.5500 | au-dessus |
| e20x10 | 10 | 0.5 | (6 ; 0.3165) | 0.7668 | 0.7668 | au-dessus |
| e20x10 | 12 | 0.6 | (6 ; 0.3165) | 0.8993 | 0.8993 | au-dessus |
| e20x10 | 14 | 0.7 | (6 ; 0.3165) | 0.9624 | 0.9624 | au-dessus |
| e20x10 | 20 | 1.0 | (6 ; 0.3165) | 0.9989 | 0.9989 | au-dessus |

### Famille Q — borne basse exacte de `coelev_comptage` sous équicorrélation (e10x20, seuil exact)

| loi | m | seuil exact (c, γ) | borne basse | HQ.4 |
|---|---|---|---|---|
| c0.1 | 3 | (5 ; 0.0977) | 0.0412 | — |
| c0.1 | 5 | (5 ; 0.0977) | 0.2851 | au-dessus |
| c0.1 | 7 | (5 ; 0.0977) | 0.8447 | au-dessus |
| c0.1 | 10 | (5 ; 0.0977) | 0.9938 | au-dessus |
| c0.3 | 3 | (7 ; 0.0718) | 0.0091 | — |
| c0.3 | 5 | (7 ; 0.0718) | 0.0291 | — |
| c0.3 | 7 | (7 ; 0.0718) | 0.1640 | au-dessus |
| c0.3 | 10 | (7 ; 0.0718) | 0.8616 | au-dessus |
| c0.4 | 5 | (8 ; 0.1192) | 0.0140 | — |

### Famille P — modèle de substitution (v_mod) et prédictions

| sonde | m | pas_moyenne | coelev_comptage | e_coelev | ed_coelev | prédictions |
|---|---|---|---|---|---|---|
| tromperie-difference_moyennes-c15 | 3 | 0.0447 | 0.0481 | 0.046 | 0.0471 | — |
| tromperie-difference_moyennes-c15 | 4 | 0.0666 | 0.0669 | 0.042 | 0.0435 | pas_moyenne au-dessus ; coelev_comptage au-dessus |
| tromperie-difference_moyennes-c15 | 5 | 0.1133 | 0.1227 | 0.0377 | 0.0392 | pas_moyenne au-dessus ; coelev_comptage au-dessus |
| tromperie-difference_moyennes-c15 | 6 | 0.2119 | 0.2172 | 0.0317 | 0.0338 | pas_moyenne au-dessus ; coelev_comptage au-dessus ; e_coelev en-dessous ; ed_coelev en-dessous |
| tromperie-difference_moyennes-c15 | 7 | 0.3673 | 0.3282 | 0.0273 | 0.0305 | pas_moyenne au-dessus ; coelev_comptage au-dessus ; e_coelev en-dessous ; ed_coelev en-dessous |
| tromperie-difference_moyennes-c15 | 10 | 0.9586 | 0.705 | 0.0151 | 0.0181 | pas_moyenne au-dessus ; coelev_comptage au-dessus ; e_coelev en-dessous ; ed_coelev en-dessous ; coelev_comptage ≥ 0.55 |
| enjeux-lineaire-c15 | 3 | 0.0215 | 0.0245 | 0.0839 | 0.0505 | pas_moyenne en-dessous ; coelev_comptage en-dessous ; e_coelev au-dessus |
| enjeux-lineaire-c15 | 4 | 0.0208 | 0.0243 | 0.1033 | 0.0461 | pas_moyenne en-dessous ; coelev_comptage en-dessous ; e_coelev au-dessus |
| enjeux-lineaire-c15 | 5 | 0.0243 | 0.0315 | 0.1223 | 0.043 | pas_moyenne en-dessous ; coelev_comptage en-dessous ; e_coelev au-dessus |
| enjeux-lineaire-c15 | 6 | 0.0338 | 0.0469 | 0.1437 | 0.04 | pas_moyenne en-dessous ; e_coelev au-dessus |
| enjeux-lineaire-c15 | 7 | 0.064 | 0.1034 | 0.151 | 0.0365 | coelev_comptage au-dessus ; e_coelev au-dessus |
| enjeux-lineaire-c15 | 10 | 0.5486 | 0.4629 | 0.1681 | 0.0232 | pas_moyenne au-dessus ; coelev_comptage au-dessus ; e_coelev au-dessus ; ed_coelev en-dessous ; coelev_comptage ≥ 0.31 |
