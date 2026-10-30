# Critère de la vérification d'écrêtage v9 (GD8-05) — écrit et scellé AVANT l'exécution de `verif-ecretage-v9.py`

Objet : deux conventions d'écrêtage des écarts étalonnés par strate. (S) simulation : δ − g_cal écrêté à [−1 ; 1] (`processus`) ; (J) juge : g_cal écrêté à
[−1 ; 1], puis δ − g_cal. Contraste : v_cal écrêté à [−1 ; 1] dans les deux (identiques par construction ; vérifié quand même).

Critère scindé, déclaré d'avance :

- **C1, périmètre** (tous les cas suivants) : K_h ∈ {5 ; 10}, K_s = 10, τ = 0,01, ρ_A = ρ_B = 0,17, S ∈ {2 ; 3}, γ = 0,4, portée ∈ {sujet ; commune}, étalonnage par
  strate, 288 unités, k = 8, biais ∈ {0 ; 0,0125}, 2 000 répétitions (32 cas). Exigé dans chaque cas : (a) part des valeurs de garde étalonnées hors de [−1 ; 1]
  < 10⁻³ ; (b) |puissance (S) − puissance (J)| ≤ 0,003 pour « les 8 gardes atteignent 40 » et pour « les 8 gardes atteignent 160 » (mêmes tirages) ;
  (c) puissance des 8 contrastes à 40 : (S) = (J) exactement.
- **C2, hors périmètre** (K_h ∈ {2 ; 3}, mêmes autres réglages, S = 3, portée sujet, biais 0) : **aucun critère** ; valeurs écrites à titre descriptif seulement.
- Conformité = C1 dans les 32 cas. **La sortie est conservée et scellée même en cas d'échec** ; aucun critère n'est réécrit après lecture (règle R4) ; un échec
  serait rapporté comme tel.

Graine : SeedSequence([20261029, sha256(« ecretage-v9|… »)]) par cas (R9).
