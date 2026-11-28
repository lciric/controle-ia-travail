"""A4 (b) : poids d'une tâche tirée k fois (calcul à la main) ; A4 (a) : nombre de tranches avec des coûts ex aequo."""
import numpy as np
from commun import A, B, GE
from controle_ia.premier_test_ia.statistiques import aire_stratifiee, strates_quantiles

# deux tâches : X (positif 0,9 ; négatif 0,1 : aire 1) et Y (positif 0,2 ; négatif 0,8 : aire 0)
s = np.array([0.9, 0.1, 0.2, 0.8]); y = np.array([1, 0, 1, 0]); t = np.array(["X", "X", "Y", "Y"])
print("observé (une paire par tâche) :", aire_stratifiee(s, y, t), "= (1 + 0) / 2")
i = np.array([0, 1, 0, 1, 2, 3])                                   # tirage : X, X, Y
print("tirage X, X, Y — tranche commune (code des candidats) :")
print("   A", A.aires_stratifiees_par_rangs(s[i][:, None], y[i], t[i])[0], " B", B.aires_par_rangs(s[i], y[i], t[i])[0],
      " Gemini", GE._aires_stratifiees_2d(s[i][:, None], y[i], t[i])[0], " à la main (2·2·1 + 1·0) / (4 + 1) = 0,8")
copie = np.array(["X#1", "X#1", "X#2", "X#2", "Y#1", "Y#1"])
print("   une tranche par copie :", aire_stratifiee(s[i], y[i], copie), " à la main (1 + 1 + 0) / 3 = 0,667 (poids k)")

# effet sur la largeur de l'intervalle : 12 tâches mixtes, tirage par blocs, tranche commune contre tranche par copie
rng = np.random.default_rng(7)
taches, ss, yy = [], [], []
for k in range(12):
    n1, n0 = int(rng.integers(1, 6)), int(rng.integers(1, 6))
    eff = rng.normal(0.4, 1.0)
    ss += list(rng.normal(eff, 1, n1)) + list(rng.normal(0, 1, n0)); yy += [1] * n1 + [0] * n0; taches += [f"t{k}"] * (n1 + n0)
ss, yy, taches = np.array(ss), np.array(yy), np.array(taches)
u = np.unique(taches); membres = [np.flatnonzero(taches == x) for x in u]
r = np.random.default_rng(1); commune, par_copie = [], []
for _ in range(4000):
    ch = r.integers(0, u.size, u.size)
    idx = np.concatenate([membres[c] for c in ch])
    lab = np.concatenate([[f"{c}#{n}"] * membres[c].size for n, c in enumerate(ch)])
    commune.append(aire_stratifiee(ss[idx], yy[idx], taches[idx])); par_copie.append(aire_stratifiee(ss[idx], yy[idx], lab))
print(f"aire observée {aire_stratifiee(ss, yy, taches):.4f} ; intervalle 95 % tranche commune "
      f"[{np.quantile(commune, .025):.4f}, {np.quantile(commune, .975):.4f}] écart type {np.std(commune):.4f} ; "
      f"tranche par copie [{np.quantile(par_copie, .025):.4f}, {np.quantile(par_copie, .975):.4f}] écart type {np.std(par_copie):.4f}")

# A4 (a) : tranches avec ex aequo
v = np.log10(np.array([10, 10, 10, 10, 10, 10, 20, 20, 30, 30, 30, 40.0]))
print("coûts ex aequo : tranches observées", np.unique(strates_quantiles(v, 5)).size, "sur 5")
r = np.random.default_rng(3); nb = [np.unique(strates_quantiles(v[r.integers(0, v.size, v.size)], 5)).size for _ in range(2000)]
print("dans les tirages : nombre de tranches", {k: nb.count(k) for k in sorted(set(nb))})
