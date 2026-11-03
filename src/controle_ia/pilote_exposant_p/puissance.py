"""Simulation de puissance du pilote sur des superellipses synthétiques bruitées.

Générateur de grilles par ancre (même grille que le run : 31 × 31 angles sur [0, 60°], 30 ancres par ajustement) :
pour l'ancre n, réponse R_n(α₁, α₂) = A_n · u_n^γ + plancher, avec
    u_n = sin r · ( |cos φ / s₁ₙ|^pₙ + |sin φ / s₂ₙ|^pₙ )^(1/pₙ),  r = √(α₁² + α₂²), φ = atan2(α₂, α₁),
pₙ = p · exp(σ_p z), sᵢₙ = sin(aᵢ · exp(σ_a z')) (angles de rupture hétérogènes), A_n log-normale (σ_A = 0,5, relevé
sur les grilles publiées), plancher numérique ≈ 0,66 ± 0,3 (relevé). Chaque ancre a pour contour une superellipse
d'exposant pₙ ; la grille médiane mélange les ancres, comme dans le run. L'ajustement est celui du run
(`ajustement.ajuster_plan`, protocole du papier).

Calage du « bruit plausible » : σ_p et σ_a sont choisis pour que l'écart type de p estimé sur 30 ancres approche les
écarts types relevés par rééchantillonnage des ancres sur les grilles publiées de Llama-3.1-8B (calcul) : ≈ 0,22 vers
p ≈ 2, ≈ 0,27 vers p ≈ 2,5, ≈ 0,33 vers p ≈ 3.

Plan simulé (celui du préenregistrement) : le plan lu (E, R) sur S sous-ensembles indépendants de 30 ancres ; la
référence = M plans de différences aléatoires disjointes, chacun ajusté sur 30 ancres, de moyenne mesurée tirée selon
N(μ, τ²) (hétérogénéité des directions ; τ = 0,17 d'après l'écart type publié de 0,262 entre paires de différences
aléatoires sur Gemma, dont ≈ 0,2 de bruit d'ancres ; calcul). L'estimateur étant biaisé vers le bas (grille médiane
d'ancres hétérogènes), tout est exprimé sur l'échelle mesurée : Δ = moyenne mesurée du plan lu − μ. Lecture : règle
gelée de `analyse.issue_principale` (intervalle à 95 % par rééchantillonnage conjoint des sous-ensembles et des plans
de référence).

Pour la vitesse, les estimations sont tirées de banques : pour chaque p vrai d'une grille (pas 0,05), n tirages
indépendants de p estimé sur 30 ancres synthétiques.

    python -I -B -m controle_ia.pilote_exposant_p.puissance --sortie FICHIER.json [--rapide]
"""
from __future__ import annotations

import argparse
import json
import sys
import time

import numpy as np

from .ajustement import ajuster_plan, bootstrap_difference
from .analyse import DELTA_EQUIVALENCE, issue_principale

ANGLES = np.linspace(0.0, 60.0, 31)
# calage prudent (relevé le 2026-11-03) : σ_p = 0,40, σ_a = 0,30 donnent un écart type de p estimé de ≈ 0,22 vers
# p mesuré ≈ 1,84 (cible publiée 0,22) et un bruit plus fort que publié au-dessus (≈ 0,31 vers 2,24 ; ≈ 0,47 vers
# 2,77) : la puissance estimée est une borne basse
PARAMS_DEFAUT = {"sigma_p": 0.40, "sigma_a": 0.30, "sigma_A": 0.5, "gamma": 2.5, "a1_deg": 42.0, "a2_deg": 38.0,
                 "plancher": 0.66, "plancher_et": 0.3}
ENTROPIE = 2026110302
GRILLE_P_VRAI = np.round(np.arange(1.5, 4.01, 0.05), 2)


def grilles_synthetiques(p: float, n_ancres: int, rng: np.random.Generator, params: dict = PARAMS_DEFAUT,
                         angles_deg: np.ndarray = ANGLES) -> np.ndarray:
    al = np.deg2rad(angles_deg)
    A1, A2 = np.meshgrid(al, al, indexing="ij")
    r = np.hypot(A1, A2)
    phi = np.arctan2(A2, A1)
    c, s = np.abs(np.cos(phi)), np.abs(np.sin(phi))
    out = np.empty((n_ancres, len(al), len(al)))
    for n in range(n_ancres):
        pn = p * np.exp(params["sigma_p"] * rng.standard_normal())
        s1 = np.sin(np.deg2rad(min(params["a1_deg"] * np.exp(params["sigma_a"] * rng.standard_normal()), 85.0)))
        s2 = np.sin(np.deg2rad(min(params["a2_deg"] * np.exp(params["sigma_a"] * rng.standard_normal()), 85.0)))
        A = np.exp(params["sigma_A"] * rng.standard_normal())
        with np.errstate(divide="ignore", invalid="ignore"):
            norme = ((c / s1) ** pn + (s / s2) ** pn) ** (1.0 / pn)
        u = np.sin(r) * norme
        plancher = params["plancher"] + params["plancher_et"] * rng.standard_normal(r.shape)
        out[n] = A * 10.0 * u ** params["gamma"] + np.abs(plancher)
    return out


def tirage_p(p: float, rng: np.random.Generator, params: dict = PARAMS_DEFAUT, n_ancres: int = 30) -> float:
    return ajuster_plan(ANGLES, grilles_synthetiques(p, n_ancres, rng, params))["p"]


def banque(valeurs_p: np.ndarray, n_tirages: int, ss: np.random.SeedSequence, params: dict = PARAMS_DEFAUT) -> dict:
    sortie = {}
    for v, e in zip(valeurs_p, ss.spawn(len(valeurs_p))):
        rng = np.random.default_rng(e)          # un générateur par valeur, tirages successifs (jamais recréé)
        sortie[round(float(v), 4)] = np.array([tirage_p(float(v), rng, params) for _ in range(n_tirages)])
    return sortie


def isotone(y: np.ndarray) -> np.ndarray:
    """Régression isotone croissante (regroupement des voisins en violation, poids égaux)."""
    blocs = [[float(v), 1] for v in y]
    i = 0
    while i < len(blocs) - 1:
        if blocs[i][0] > blocs[i + 1][0]:
            s = blocs[i][0] * blocs[i][1] + blocs[i + 1][0] * blocs[i + 1][1]
            n = blocs[i][1] + blocs[i + 1][1]
            blocs[i:i + 2] = [[s / n, n]]
            i = max(i - 1, 0)
        else:
            i += 1
    return np.concatenate([np.full(n, v) for v, n in blocs])


class Banque:
    """Estimations de p sur 30 ancres synthétiques, par p vrai ; correspondance p vrai ↔ p mesuré (moyenne)."""

    def __init__(self, b: dict):
        self.b = {k: v[np.isfinite(v)] for k, v in b.items()}
        self.cles = np.array(sorted(self.b))
        self.moy_brute = np.array([self.b[k].mean() for k in self.cles])
        self.moy = isotone(self.moy_brute)
        if not self.moy[-1] > self.moy[0]:
            raise ValueError("p mesuré ne croît pas avec p vrai sur la grille : générateur inutilisable")
        # départage des paliers de la régression isotone (interpolation strictement croissante)
        self.moy = self.moy + np.arange(len(self.moy)) * 1e-9

    def p_vrai(self, p_mesure: float) -> float:
        """p vrai dont la moyenne mesurée vaut `p_mesure` (interpolation linéaire, bornée à la grille)."""
        return float(np.interp(p_mesure, self.moy, self.cles))

    def tirer(self, p_vrai: float, rng: np.random.Generator) -> float:
        k = float(self.cles[np.argmin(np.abs(self.cles - p_vrai))])
        return float(rng.choice(self.b[k]))


def simuler(bq: Banque, mu: float, tau: float, deltas: list[float], S: int, M: int, R: int, B: int,
            rng: np.random.Generator) -> list[dict]:
    """`mu`, `tau`, `deltas` sur l'échelle mesurée : référence de moyenne mesurée `mu`, hétérogénéité `tau` des plans
    de référence ; plan lu de moyenne mesurée `mu + delta`."""
    lignes = []
    for d in deltas:
        issues = {"au-dessus": 0, "au-dessous": 0, "égal": 0, "non concluant": 0}
        largeurs, estimes, et_ref = [], [], []
        pv = bq.p_vrai(mu + d)
        for _ in range(R):
            pe = np.array([bq.tirer(pv, rng) for _ in range(S)])
            pr = np.array([bq.tirer(bq.p_vrai(rng.normal(mu, tau)), rng) for _ in range(M)])
            r = bootstrap_difference(pe, pr, B, rng)
            issues[issue_principale(r["ic"][0], r["ic"][1])] += 1
            largeurs.append(r["ic"][1] - r["ic"][0])
            estimes.append(r["delta"])
            et_ref.append(pr.std(ddof=1))
        lignes.append({"delta_mesure": d, "p_vrai_plan_lu": round(pv, 3), **{k: v / R for k, v in issues.items()},
                       "demi_largeur_ic_mediane": float(np.median(largeurs) / 2),
                       "delta_estime_moyen": float(np.mean(estimes)), "delta_estime_et": float(np.std(estimes)),
                       "et_entre_plans_reference_median": float(np.median(et_ref))})
    return lignes


def delta_detectable(lignes: list[dict], puissance: float = 0.8) -> float | None:
    """Plus petit Δ > 0 de la grille simulée dont le taux « au-dessus » atteint `puissance`."""
    for l in sorted(lignes, key=lambda x: x["delta_mesure"]):
        if l["delta_mesure"] > 0 and l["au-dessus"] >= puissance:
            return l["delta_mesure"]
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--rapide", action="store_true", help="banques et répétitions réduites (essais)")
    ap.add_argument("--entropie", type=int, default=ENTROPIE)
    a = ap.parse_args(argv)
    t0 = time.time()
    ss = np.random.SeedSequence(a.entropie)
    s_banque, s_calage, s_sim = ss.spawn(3)
    n_t = 40 if a.rapide else 400
    R = 40 if a.rapide else 400
    grille_p = GRILLE_P_VRAI[::4] if a.rapide else GRILLE_P_VRAI
    b = banque(grille_p, n_t, s_banque)
    calage = {}
    for k in sorted(b):
        v = b[k][np.isfinite(b[k])]
        calage[f"{k:.2f}"] = {"p_mesure_moyen": float(v.mean()), "ecart_type": float(v.std(ddof=1)),
                              "echecs": int(np.isnan(b[k]).sum())}
    bq = Banque(b)
    rng = np.random.default_rng(s_sim)
    mu, deltas = 2.0, [-0.3, -0.2, -0.1, 0.0, 0.1, 0.15, 0.2, 0.3, 0.4]
    plans = []
    for S, M, tau in ((32, 60, 0.17), (16, 60, 0.17), (8, 30, 0.17), (4, 60, 0.17), (32, 60, 0.10), (32, 60, 0.25),
                      (32, 30, 0.17)):
        lignes = simuler(bq, mu, tau, deltas, S, M, R, 2000, rng)
        plans.append({"S": S, "M": M, "tau": tau, "delta_detectable_80": delta_detectable(lignes), "lignes": lignes})
    sortie = {"version": "puissance-pilote-exposant-p-v1", "entropie_seedsequence": a.entropie, "rapide": a.rapide,
              "parametres_generateur": PARAMS_DEFAUT, "angles": "31 × 31 sur [0, 60°]", "ancres_par_ajustement": 30,
              "tirages_par_banque": n_t, "repetitions": R, "B_bootstrap": 2000, "mu_reference_mesure": mu,
              "delta_equivalence": DELTA_EQUIVALENCE, "echelle": "p mesuré (estimateur du papier sur 30 ancres)",
              "calage_bruit_par_p_vrai": calage,
              "cibles_calage_publiees_calcul": {"isotropes Llama, p mesuré ≈ 1,93": 0.217,
                                                 "contrastives Llama, p mesuré ≈ 2,4 à 2,7": "0,25 à 0,31",
                                                 "Wealth × Gender Llama, p mesuré 3,00": 0.329,
                                                 "différences aléatoires Gemma, ET entre paires": 0.262},
              "plans": plans, "duree_s": round(time.time() - t0, 1)}
    with open(a.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(json.dumps({"calage_bruit": calage, "duree_s": sortie["duree_s"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
