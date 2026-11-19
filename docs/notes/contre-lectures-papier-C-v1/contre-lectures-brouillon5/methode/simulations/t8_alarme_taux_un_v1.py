"""T8 : C-P5 quand toutes les alarmes sortent (p-chapeau = 1), cas que l'hypothese HC3 (composante 1) rend probable et
que l'audit A5 prevoit (« separation parfaite des alarmes »). Formule du point 15 : e = [(T/(T-1)) sum_t (x_t - p N_t)^2 /
N_o^2] / [p (1 - p) / N_o] ; N_eff = N_o / max(1, e). Et la borne BCa (point 11) quand tous les tirages valent 1."""
import numpy as np
T, k5 = 45, 3
N_t = np.full(T, 2 * k5, float)
x_t = N_t.copy()
N_o = N_t.sum(); p = x_t.sum() / N_o
with np.errstate(divide="ignore", invalid="ignore"):
    e = ((T / (T - 1)) * ((x_t - p * N_t) ** 2).sum() / N_o ** 2) / (p * (1 - p) / N_o)
print("p-chapeau =", p, "; e =", e, "; numpy.maximum(1, e) =", np.maximum(1.0, e), "; max(1, e) en Python =", max(1.0, e))
print("N_eff (numpy) =", N_o / np.maximum(1.0, e), "; N_eff (Python max) =", N_o / max(1.0, e))
rng = np.random.default_rng(np.random.SeedSequence(0xB5C8).spawn(1)[0])
W = rng.multinomial(T, np.full(T, 1 / T), size=2000).astype(float)
pb = (W @ x_t) / (W @ N_t)
jack = np.array([(x_t.sum() - x_t[i]) / (N_t.sum() - N_t[i]) for i in range(T)])
jm = jack.mean()
with np.errstate(divide="ignore", invalid="ignore"):
    a = ((jm - jack) ** 3).sum() / (6 * ((jm - jack) ** 2).sum() ** 1.5)
print("tirages : min", pb.min(), "max", pb.max(), "; part < p-chapeau :", (pb < p).mean(), "; acceleration :", a)
print("Clopper-Pearson a l'effectif N_o, x = N_o : borne basse bilaterale 95 % =", 0.025 ** (1 / N_o))
