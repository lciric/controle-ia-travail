# Essai « Boucle d'or » v1 — verdict : à garder sous condition (seulement si l'on sait d'avance que la valeur suit la fenêtre)

Exploratoire, non opposable. 2026-10-27T08:26:12Z (date -u). Graine 20261027 ; 30 répétitions par monde ; budget 40 tests sur un réservoir de 300 ; juge v1 ; plan `plan-essai-boucle-d-or-v1.md`.

| monde | attendu | hasard | Thompson | tri | fenêtre | D1 (fenêtre − meilleur appris) | D2 (fenêtre − hasard) | Thompson − hasard |
|---|---|---|---|---|---|---|---|---|
| cloche | gagner | 0.124 | 0.170 | 0.251 | 0.481 | +0.230 [+0.186 ; +0.273] gagne | +0.357 [+0.325 ; +0.388] gagne | +0.046 [+0.020 ; +0.072] gagne |
| bords | perdre | 0.185 | 0.287 | 0.391 | 0.052 | -0.338 [-0.373 ; -0.302] perd | -0.133 [-0.154 ; -0.112] perd | +0.103 [+0.068 ; +0.140] gagne |
| croissant | perdre | 0.316 | 0.405 | 0.432 | 0.193 | -0.239 [-0.283 ; -0.194] perd | -0.123 [-0.155 ; -0.092] perd | +0.089 [+0.046 ; +0.132] gagne |
| decroissant | perdre | 0.341 | 0.361 | 0.438 | 0.444 | +0.007 [-0.031 ; +0.043] indistincte | +0.103 [+0.066 ; +0.139] gagne | +0.020 [-0.007 ; +0.048] indistincte |
| plat | ne rien changer | 0.201 | 0.188 | 0.207 | 0.193 | -0.014 [-0.045 ; +0.017] indistincte | -0.008 [-0.041 ; +0.025] indistincte | -0.013 [-0.041 ; +0.017] indistincte |

Découvertes vraies par dollar (moyennes sur les répétitions). Promotions fausses par dollar, par monde et allocateur : cloche hasard 0.000, thompson 0.000, tri 0.000, fenetre 0.000; bords hasard 0.000, thompson 0.000, tri 0.000, fenetre 0.000; croissant hasard 0.000, thompson 0.000, tri 0.000, fenetre 0.000; decroissant hasard 0.000, thompson 0.000, tri 0.000, fenetre 0.000; plat hasard 0.000, thompson 0.000, tri 0.000, fenetre 0.000.
