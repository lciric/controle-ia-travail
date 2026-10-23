BASSIN_MATH: Marché-VCG à Score Propre Décorrélé (MVSPD)
LOI_PROPOSEE: x* = argmax_x Σ_i E_θ[v_i(x,θ_i)] s.c. Σ_{i∈Claude} c_i ≤ 100, Σ_{i∈Gemini} c_i ≤ 20 ; paiement VCG t_i = Σ_{j≠i} v_j(x*_{-i}) − Σ_{j≠i} v_j(x*) ; récompense R_i = S_log(p_i,y) − S_log(p̄_{f(i)\i},y).

1. **Auto-organisation hors-poids.** Chaque sous-tâche τ est une enchère
