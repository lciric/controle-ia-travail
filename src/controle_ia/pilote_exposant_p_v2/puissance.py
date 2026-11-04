"""Simulation de puissance du pilote, version 2 (contre-lecture R2, point 5 de « Pour le brouillon 2 »).

Ce qui change depuis la v1 (`controle_ia.pilote_exposant_p.puissance`, dont le générateur de grilles et les banques
sont repris sans modification) :
- **bruit recalé** sur des sous-ensembles d'ancres distinctes : σ_p = 0,15 et σ_a = 0,10 donnent un écart type de p
  estimé de ≈ 0,10 vers p ≈ 2 sur 30 ancres (calcul, `calage_bruit_par_p_vrai`), proche du 0,096 relevé entre les
  17 isotropes publiés sur leurs 30 ancres distinctes (contre-lecture R2, B3) ; le calage prudent de la v1 (σ_p = 0,40,
  σ_a = 0,30 : ≈ 0,22, calé sur un rééchantillonnage avec remise qui gonfle la dispersion) est gardé en variante ;
- **effet commun des sous-ensembles** : chaque sous-ensemble s ajoute c_s ~ N(0, σ_c²) à tous les plans mesurés sur
  lui (σ_c ∈ {0 ; 0,035 ; 0,06}, ordres de grandeur de la contre-lecture) ;
- **référence répartie** (plan k sur le sous-ensemble k mod 32) et **intervalle par sous-ensembles** : le lecteur du
  run (`analyse.bootstrap_sous_ensembles`), appelé tel quel ;
- **plan lu tiré de la famille** : en plus du plan lu situé exactement à μ + Δ, un plan lu de moyenne μ + Δ + τ z,
  comme une paire sans concept ordinaire quand Δ = 0 ;
- **qualificatif de famille** (voie B) : K = 8 plans de référence mesurés sur les 32 sous-ensembles, intervalle de
  prédiction (`analyse.position_famille`) ;
- **sensibilité** : part des tirages où la borne basse de l'intervalle dépasse δ (règle du témoin de sensibilité,
  appliquée à un plan d'écart Δ, par exemple Wealth × Gender).
Tout est sur l'échelle mesurée (estimateur du papier sur 30 ancres), comme en v1.

    python -I -B -m controle_ia.pilote_exposant_p_v2.puissance --sortie FICHIER.json [--rapide] [--processus N]
(avec PYTHONPATH=src, sans -I, ou depuis le dépôt installé)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

from ..pilote_exposant_p.puissance import PARAMS_DEFAUT, Banque, tirage_p
from .analyse import DELTA_EQUIVALENCE, K_FAMILLE, bootstrap_sous_ensembles, issue_principale, position_famille

ENTROPIE = 2026110402
CALAGES = {"recale": dict(PARAMS_DEFAUT, sigma_p=0.15, sigma_a=0.10), "prudent_v1": dict(PARAMS_DEFAUT)}
GRILLE_P_VRAI = np.round(np.arange(1.5, 3.81, 0.05), 2)
S, M = 32, 60


def _banque_une_valeur(arg):
    p, n, etat, params = arg
    rng = np.random.default_rng(np.random.SeedSequence(etat))
    return round(float(p), 4), np.array([tirage_p(float(p), rng, params) for _ in range(n)])


def banque(valeurs_p, n, ss: np.random.SeedSequence, params: dict, processus: int) -> dict:
    enfants = ss.spawn(len(valeurs_p))
    args = [(v, n, e.generate_state(4).tolist(), params) for v, e in zip(valeurs_p, enfants)]
    if processus > 1:
        with ProcessPoolExecutor(processus) as ex:
            return dict(ex.map(_banque_une_valeur, args))
    return dict(map(_banque_une_valeur, args))


def une_repetition(bq: Banque, mu: float, delta: float, tau: float, sigma_c: float, tire_famille: bool, B: int,
                   rng: np.random.Generator, K: int = K_FAMILLE) -> dict:
    c = rng.normal(0.0, sigma_c, S) if sigma_c > 0 else np.zeros(S)
    m_er = mu + delta + (tau * rng.standard_normal() if tire_famille else 0.0)
    pv_er = bq.p_vrai(m_er)
    p_er = {s: bq.tirer(pv_er, rng) + c[s] for s in range(S)}
    mu_k = mu + tau * rng.standard_normal(M)
    pv_k = [bq.p_vrai(x) for x in mu_k]
    ref = [(k % S, bq.tirer(pv_k[k], rng) + c[k % S]) for k in range(M)]
    d = bootstrap_sous_ensembles(p_er, ref, B, rng)
    moyennes = []
    for k in range(K):
        v = [ref[k][1]] + [bq.tirer(pv_k[k], rng) + c[s] for s in range(S) if s != k % S]
        moyennes.append(float(np.nanmean(v)))
    pos = position_famille(d["moyenne_plan"], moyennes)
    return {"issue": issue_principale(*d["ic"]), "demi_largeur": (d["ic"][1] - d["ic"][0]) / 2, "delta": d["delta"],
            "ic_bas_sup_delta": bool(d["ic"][0] > DELTA_EQUIVALENCE), "position": pos["position"],
            "et_famille": pos.get("ecart_type_entre_plans", float("nan"))}


def simuler(bq: Banque, mu: float, tau: float, sigma_c: float, tire_famille: bool, deltas, R: int, B: int,
            rng: np.random.Generator) -> list[dict]:
    lignes = []
    for dl in deltas:
        rs = [une_repetition(bq, mu, dl, tau, sigma_c, tire_famille, B, rng) for _ in range(R)]
        compte = lambda cle, v: float(np.mean([r[cle] == v for r in rs]))
        lignes.append({
            "delta_mesure": dl, **{k: compte("issue", k) for k in ("au-dessus", "au-dessous", "égal", "non concluant")},
            "sensibilite_ic_bas_sup_delta": float(np.mean([r["ic_bas_sup_delta"] for r in rs])),
            **{f"famille_{k}": compte("position", k) for k in ("au-delà de la famille", "en deçà de la famille",
                                                                 "dans la famille", "famille non mesurée")},
            "demi_largeur_mediane": float(np.median([r["demi_largeur"] for r in rs])),
            "demi_largeur_q01": float(np.percentile([r["demi_largeur"] for r in rs], 1)),
            "delta_estime_moyen": float(np.mean([r["delta"] for r in rs])),
            "delta_estime_et": float(np.std([r["delta"] for r in rs])),
            "et_entre_plans_famille_median": float(np.nanmedian([r["et_famille"] for r in rs]))})
    return lignes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--rapide", action="store_true", help="banques et répétitions réduites (essais)")
    ap.add_argument("--entropie", type=int, default=ENTROPIE)
    ap.add_argument("--processus", type=int, default=1)
    a = ap.parse_args(argv)
    t0 = time.time()
    ss = np.random.SeedSequence(a.entropie)
    s_banques, s_sim = ss.spawn(2)
    n_t = 30 if a.rapide else 300
    R = 20 if a.rapide else 300
    B = 500 if a.rapide else 2000
    grille = GRILLE_P_VRAI[::6] if a.rapide else GRILLE_P_VRAI
    banques, calage = {}, {}
    for (nom, params), e in zip(CALAGES.items(), s_banques.spawn(len(CALAGES))):
        b = banque(grille, n_t, e, params, a.processus)
        banques[nom] = Banque(b)
        calage[nom] = {f"{k:.2f}": {"p_mesure_moyen": float(np.nanmean(v)), "ecart_type": float(np.nanstd(v, ddof=1)),
                                    "echecs": int(np.isnan(v).sum())} for k, v in sorted(b.items())}
    rng = np.random.default_rng(s_sim)
    mu = 2.0
    deltas_complets = [-0.3, -0.2, -0.1, 0.0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6]
    deltas_courts = [-0.2, 0.0, 0.2, 0.4]
    scenarios = []
    for nom in CALAGES:
        for sigma_c in (0.0, 0.035, 0.06):
            for tau in (0.10, 0.17, 0.25):
                for tire in (False, True):
                    central = sigma_c == 0.035 and tau == 0.17
                    if a.rapide and not central:
                        continue
                    lignes = simuler(banques[nom], mu, tau, sigma_c, tire, deltas_complets if central else deltas_courts,
                                     R, B, rng)
                    scenarios.append({"calage": nom, "sigma_c": sigma_c, "tau": tau, "plan_lu_tire_de_la_famille": tire,
                                      "central": central, "lignes": lignes})
    sortie = {"version": "puissance-pilote-exposant-p-v2", "entropie_seedsequence": a.entropie, "rapide": a.rapide,
              "calages": CALAGES, "angles": "31 × 31 sur [0, 60°]", "ancres_par_ajustement": 30,
              "sous_ensembles_S": S, "plans_reference_M": M, "K_famille": K_FAMILLE, "tirages_par_banque": n_t,
              "repetitions": R, "B_bootstrap": B, "mu_reference_mesure": mu, "delta_equivalence": DELTA_EQUIVALENCE,
              "echelle": "p mesuré (estimateur du papier sur 30 ancres)",
              "cibles_calage": {"isotropes publiés de Llama, 30 ancres distinctes, ET entre les 17 plans (contre-lecture R2)": 0.096,
                                "rééchantillonnage avec remise (v1)": 0.217},
              "calage_bruit_par_p_vrai": calage, "scenarios": scenarios, "duree_s": round(time.time() - t0, 1)}
    with open(a.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(json.dumps({"duree_s": sortie["duree_s"], "scenarios": len(scenarios)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
