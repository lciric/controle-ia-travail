"""É0 (suite) — nombres dérivés du brouillon (G1) et du texte des arbitrages, recalculés. Aucune donnée du programme,
sauf la dernière section : aire de trois prédicteurs triviaux entre conditions de la course de dose-réponse (comptes et
taux du dispositif, aucun seuil réglé), pour situer la garde « prédicteurs triviaux »."""
import json, sys
from pathlib import Path
import numpy as np
from scipy import stats, optimize, integrate
from controle_ia.sondes.evaluation import aire_sous_courbe

S = Path(sys.argv[1])
r = {}
# --- effectifs
r["effectifs"] = {
 "727 = 64 + 64 + 599": 64 + 64 + 599 == 727, "599 = 399 + 200": 399 + 200 == 599, "264 = 64 + 200": 64 + 200 == 264,
 "actions_par_condition = 200 × 4 × 10": 200 * 4 * 10, "episodes_par_condition": 200 * 4,
 "46 550 = (5×800 + 399 + 64×2×2) × 10": (5 * 800 + 399 + 64 * 2 * 2) * 10, "40 000 = 5×800×10": 5 * 800 * 10,
 "N_act de l'ajustement = 64 × 2 × 10 × 2": 64 * 2 * 10 * 2,
 "colonnes de W = 3 × (2 + 800)": 3 * 802, "largeur de Z = 4096 + 11": 4096 + 11,
 "dimension de Psi = 1 + 1 + 1 + 8 + 8": 19, "dimension de Phi = 1 + 1 + 1 + 8": 11,
}
# --- calibrage conforme
b = stats.beta(4, 396)
r["conforme_amont"] = {"rang m = floor(0,01 × 400)": int(np.floor(0.01 * 400)), "E[U]": b.mean(), "CV": b.std() / b.mean(),
                       "P(U < 0,2 %)": b.cdf(0.002), "brouillon": {"CV": 0.497, "P(U < 0,2 %)": 0.0089}}
b1 = stats.beta(1, 99)
r["conforme_intra"] = {"rang m = floor(0,01 × 100)": 1, "E[U]": b1.mean(), "P(U < 0,2 %)": b1.cdf(0.002), "brouillon": {"P(U < 0,2 %)": 0.18}}
# espérance de la 4e plus grande de 399 normales réduites (seuil attendu, en écarts-types)
n, k = 399, 4
f = lambda x: x * stats.norm.pdf(x) * stats.beta.pdf(stats.norm.cdf(x), n - k + 1, k)
r["seuil_attendu_4e_plus_grande_de_399_normales"] = {"valeur": integrate.quad(f, -8, 8)[0], "brouillon": 2.368}
# --- niveaux
r["niveaux"] = {"alpha_s = 0,025 / 3": 0.025 / 3, "z(1 - alpha_s)": stats.norm.ppf(1 - 0.025 / 3), "rang du quantile 0,833 % sur 10 000 tirages": 0.00833 * 10000}
# --- différences minimales détectables annoncées
z = stats.norm.ppf(1 - 0.025 / 3) + stats.norm.ppf(0.80)
def mde(n_obs, par_grappe, icc, p):
    return z * np.sqrt(p * (1 - p) / (n_obs / (1 + (par_grappe - 1) * icc)))
r["mde"] = {"H1 : 8 000 actions, 40 par tâche, ICC 0,30": {f"p={p}": round(float(mde(8000, 40, 0.30, p)), 4) for p in (0.05, 0.10, 0.15, 0.20, 0.50)},
            "H2 : 800 épisodes, 4 par tâche, ICC 0,50": {f"p={p}": round(float(mde(800, 4, 0.50, p)), 4) for p in (0.10, 0.20, 0.30, 0.50)},
            "brouillon": {"H1": 0.046, "H2": 0.089},
            "lecture": "formule d'une proportion seule (non d'une différence appariée), sans le bruit du seuil ni les clauses « Porteuse »"}
# --- constantes de la pré-gaussianisation de Gumbel
med = -np.log(np.log(2.0))
F = lambda x: np.exp(-np.exp(-x))
mad = optimize.brentq(lambda d: F(med + d) - F(med - d) - 0.5, 0.1, 3.0)
iqr = -np.log(-np.log(0.75)) + np.log(-np.log(0.25))
sd = np.pi / np.sqrt(6)
BG = 1.137205
r["gumbel"] = {"m_G = -ln ln 2": med, "1,4826 × MAD": 1.4826 * mad, "0,7413 × IQR": 0.7413 * iqr, "écart-type": sd,
               "beta_G du brouillon": BG, "beta_0 = 0,5 × beta_G × ln 2 × sqrt(2 pi)": 0.5 * BG * np.log(2) * np.sqrt(2 * np.pi), "beta_0 du brouillon": 0.98791,
               "sigma_rob d'une Gumbel = max des trois": max(1.4826 * mad, 0.7413 * iqr, sd),
               "constat": "beta_G = 1,4826 × MAD de la Gumbel réduite, alors que l'échelle robuste du même texte est le maximum de trois échelles, qui vaut l'écart-type (1,2825) pour une Gumbel : la transformation n'envoie pas un score de Gumbel normalisé par sigma_rob sur une normale réduite"}
# effet : loi de u_G2N(z) quand z = (x - med)/sigma_rob et x Gumbel réduite
rng = np.random.default_rng(1)
x = rng.gumbel(size=2_000_000)
sys.path.insert(0, str(S / "scripts"))
import e5_regle_g1 as m
for nom, ech in (("normalisé par 1,4826 × MAD", 1.4826 * mad), ("normalisé par sigma_rob (écart-type)", sd)):
    u = m.g2n((x - med) / ech)
    r["gumbel"][f"u_G2N, score {nom}"] = {"écart-type": float(u.std()), "P(u > 2,326)": float((u > 2.326).mean()), "attendu sous normale": 0.01}
# --- prédicteurs triviaux sur données réelles (course de dose-réponse)
blocs = S / "entrees/dose-reponse-blocs"
don = {}
for d in sorted(blocs.iterdir()):
    for l in (d / "mesures.jsonl").read_text().splitlines():
        a = json.loads(l)
        don.setdefault(a["condition"], []).append((a["jetons_notes"], a["pas"], a["tache"]))
def aire(c1, c0, champ=0):
    x1 = np.array([v[champ] for v in don[c1]], float); x0 = np.array([v[champ] for v in don[c0]], float)
    a = aire_sous_courbe(np.concatenate([x1, x0]), np.concatenate([np.ones(x1.size, int), np.zeros(x0.size, int)]))
    return {"aire": round(a, 4), "separation max(a, 1-a)": round(max(a, 1 - a), 4)}
r["predicteur_trivial_longueur_donnees_reelles"] = {f"{c1} contre {c0}": aire(c1, c0) for c1, c0 in
    (("consigne_neutre", "honnete"), ("gonfle_3", "honnete"), ("gonfle_5", "honnete"), ("gonfle_3", "consigne_neutre"), ("gonfle_5", "consigne_neutre"))}
print(json.dumps(r, indent=1, ensure_ascii=False, default=float))
