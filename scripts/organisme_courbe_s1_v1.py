"""Simulation S1 de la courbe dose-réponse de la chaîne complète : la chaîne sans agents sur les mondes W_λ — v1.

Calcul de dimensionnement (note `docs/notes/organisme-courbe-dose-reponse-v1/conception-simulation-s1-v1.md`, scellée
avant le run). Aucun appel de modèle, aucun réseau, aucune clé. Le code de l'organisme est la copie empreintée au commit
94bfd92 (branche claude/upbeat-cray-dmauvv, commit 8668f0ae), extraite hors du dépôt et importée telle quelle.

Usage (racine d'un arbre propre) :
  PYTHONPATH=src python scripts/organisme_courbe_s1_v1.py CHEMIN/orchestrator --processus 4
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from controle_ia.manifeste import creer_manifeste, ecrire_resultat

CONFIG = {
    "objet": "courbe de la chaîne complète de l'organisme : simulation S1, chaîne sans agents sur les mondes W_λ",
    "doses_lambda": [0.0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.75, 1.0],
    "repetitions_par_dose": 200,
    "racine_graines": 20261111,
    "m_fixe": 22,
    "alpha": 0.05,
    "seuil_mort_nat": 0.02,
    "seuil_oracle_nat": 0.02,
    "code_organisme": {"source": "lciric/ideation-organism@94bfd92", "copie": "claude/upbeat-cray-dmauvv@8668f0ae",
                       "empreintes": "empreintes-copie-v1.txt 0153e02d…"},
}
TACHES = ["s1"]
_ORG = None


def _importer(organisme: str):
    global _ORG
    if _ORG is None:
        if organisme not in sys.path:
            sys.path.insert(0, organisme)
        from pole import a_blanc_v59 as A  # noqa: E402
        from pole import boucle_fermee_v59 as bf  # noqa: E402
        from pole import selection_pari as sp  # noqa: E402
        from pole.oracle_tour_ferme_v60 import Oracle  # noqa: E402
        _ORG = (A, bf, sp, Oracle)
    return _ORG


def monde_lambda(m: dict, lam: float) -> dict:
    loi = m["loi"]
    poids = [[ligne[0], lam * ligne[1]] for ligne in loi["poids"]]
    return {"type": "softmax", "poids": poids, "biais": list(loi["biais"])}


def ajuster_k1(o) -> dict:
    """Meilleure loi softmax du seul trait z0 sous la loi de l'oracle, au maximum de vraisemblance attendue (comme
    `essai-a-blanc-v1/ajuster_k1_v1.py`, colonne 0), arrondie à 6 décimales."""
    from scipy.optimize import minimize
    z = np.array([x["z"] for x in o.instances])
    p = np.asarray(o.P)

    def f(t):
        a, c = t[:3], t[3:]
        s = np.outer(z[:, 0], a) + c
        s -= s.max(1, keepdims=True)
        lq = s - np.log(np.exp(s).sum(1, keepdims=True))
        return -np.mean(np.sum(p * lq, 1))

    r = minimize(f, np.zeros(6), method="BFGS")
    a, c = r.x[:3] - r.x[0], r.x[3:] - r.x[3]
    return {"type": "softmax", "poids": [[round(float(a[k]), 6), 0.0] for k in range(3)],
            "biais": [round(float(v), 6) for v in c]}


def lois_de_la_dose(m: dict, lam: float, k1: dict) -> dict:
    w = monde_lambda(m, lam)
    v2 = {"type": "softmax", "poids": [[0.0, lam * ligne[1]] for ligne in m["loi"]["poids"]],
          "biais": list(m["loi"]["biais"])}
    uniforme = {"type": "fixe", "probas": [1.0, 1.0, 1.0]}
    return {"W": w, "V2": v2, "F1": dict(k1),
            "F2": {"type": "melange", "composantes": [k1, uniforme], "poids": [0.8, 0.2]}}


def _statistique(A, sp, loi, lignes):
    comptes = [0.5] * A.K
    for _, y in lignes:
        comptes[y] += 1
    s = sum(comptes)
    marg = [c / s for c in comptes]
    g = [math.log(max(sp.proba(loi, x, [], 0)[y], 1e-12)) - math.log(marg[y]) for x, y in lignes]
    return sum(g) / len(g)


def _log_e(ev, seuil):
    if ev.get("marge_atteinte") is False:
        return -math.inf
    traj = ev["trajectoire_log_w"]
    return next((v for v in traj if v >= seuil), traj[-1])


def une_repetition(args):
    organisme, lam, rep, racine, k1 = args
    A, bf, sp, _ = _importer(organisme)
    m = A.charger_monde(organisme)
    mw = dict(m, loi=monde_lambda(m, lam))
    lois = lois_de_la_dose(m, lam, k1)
    seuil = math.log(CONFIG["m_fixe"] / CONFIG["alpha"])
    tache = f"courbe-s1|lambda={lam}|rep={rep}"
    rng = __import__("random").Random(bf.graine_de_tache(racine, f"{tache}|tranche"))
    lignes = [(x, sp.tirer_categorie(rng, sp.proba(mw["loi"], x, [], 0)))
              for x in sp.tirer_instances(rng, A.EPISODES_TRANCHE, A.DIM)]
    out = {}
    for nom, loi in lois.items():
        ev, d = A.juger_carte(loi, mw, {"K1": k1}, racine, f"{tache}|{nom}")
        le = _log_e(ev, seuil)
        promue = bool(ev["promue"]) and le >= seuil
        stat = _statistique(A, sp, loi, lignes) if promue else None
        out[nom] = {"promue": promue, "survit": None if stat is None else stat >= CONFIG["seuil_mort_nat"],
                    "log_w_max": round(ev["log_richesse_max"], 6), "membres_d_archive": d["membres_d_archive"]}
    return lam, rep, out


def wilson(x, n, z=1.959963984540054):
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def calculer(organisme: str, processus: int) -> dict:
    A, bf, sp, Oracle = _importer(organisme)
    m = A.charger_monde(organisme)
    racine_oracle = int(np.random.SeedSequence(CONFIG["racine_graines"], spawn_key=(10 ** 6,)).generate_state(
        1, dtype=np.uint64)[0])
    doses = {}
    taches = []
    enfants = np.random.SeedSequence(CONFIG["racine_graines"]).spawn(
        len(CONFIG["doses_lambda"]) * CONFIG["repetitions_par_dose"])
    i = 0
    for lam in CONFIG["doses_lambda"]:
        o = Oracle(monde_lambda(m, lam), racine_oracle, A.DIM)
        k1 = ajuster_k1(o)
        lois = lois_de_la_dose(m, lam, k1)
        mesures = {nom: o.mesurer(loi, {"K1": k1}) for nom, loi in lois.items()}
        doses[str(lam)] = {"k1": k1, "g_lambda_nat": mesures["W"]["delta_gain_nat"], "oracle": mesures}
        for rep in range(CONFIG["repetitions_par_dose"]):
            racine = int(enfants[i].generate_state(1, dtype=np.uint64)[0])
            taches.append((organisme, lam, rep, racine, k1))
            i += 1
    with ProcessPoolExecutor(max_workers=processus) as ex:
        resultats = list(ex.map(une_repetition, taches, chunksize=4))
    n = CONFIG["repetitions_par_dose"]
    for lam in CONFIG["doses_lambda"]:
        reps = [r for (l, _, r) in resultats if l == lam]
        res = {}
        for nom in ("W", "V2", "F1", "F2"):
            ps = sum(1 for r in reps if r[nom]["promue"] and r[nom]["survit"] is True)
            pr = sum(1 for r in reps if r[nom]["promue"])
            res[nom] = {"promue": pr, "promue_puis_survivante": ps, "n": n, "part": round(ps / n, 4),
                        "wilson": wilson(ps, n), "log_w_max_mediane": round(float(np.median(
                            [r[nom]["log_w_max"] for r in reps])), 4)}
        doses[str(lam)]["jugements"] = res
    return {"doses": doses, "monde": {"source": m["source"], "sha256": m["sha256"], "loi_vraie": m["loi_vraie"]}}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("organisme")
    p.add_argument("--processus", type=int, default=4)
    a = p.parse_args()
    racine = Path(__file__).resolve().parents[1]
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-organisme-courbe-s1-v1"
    config = dict(CONFIG, chemin_organisme=a.organisme,
                  empreinte_a_blanc_v59=hashlib.sha256(open(os.path.join(a.organisme, "pole", "a_blanc_v59.py"),
                                                                "rb").read()).hexdigest())
    chemin, manifeste = creer_manifeste(racine, run_id, config, TACHES,
                                        commande="PYTHONPATH=src python scripts/organisme_courbe_s1_v1.py ORGANISME")
    sortie = ecrire_resultat(racine, chemin, "courbe-s1-v1", calculer(a.organisme, a.processus))
    print(chemin)
    print(sortie)
    return 0


if __name__ == "__main__":
    sys.exit(main())
