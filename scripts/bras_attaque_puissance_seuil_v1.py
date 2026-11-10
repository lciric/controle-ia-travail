"""Tables de conception du bras d'attaque : bruit du seuil à 1 % de fausses alertes, réserve honnête, puissance des
témoins, précision d'un point de la courbe. Aucune donnée : lois exactes et simulations sous manifeste (R9).

Usage (racine du dépôt, arbre propre) : PYTHONPATH=src python scripts/bras_attaque_puissance_seuil_v1.py
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

from scipy import stats

from controle_ia.bras_attaque import puissance_seuil_v1 as p
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, generateur

CONFIG = {
    "objet": "conception du bras d'attaque : bruit du seuil, réserve honnête, puissance des témoins",
    "alpha": 0.01,
    "grille_n": [100, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 3000, 5000],
    "probas_fpr": [0.5, 0.9, 0.95, 0.99],
    "objectif_reserve": {"fpr_max": 0.02, "delta": 0.05, "balayage_n": [100, 5000]},
    "garanti": {"alpha": 0.01, "delta": 0.05},
    "nul": {"n": [600, 1000, 2000], "h": [200, 500, 1000], "inflation": [1.0, 2.0, 3.0, 5.0],
            "niveaux": [0.95, 0.99], "tirages": 20000},
    "rappel_binormal": {"n": [200, 600, 1000, 2000], "m": [50, 100, 200], "rappel_vrai": [0.2, 0.5, 0.8],
                        "tirages": 4000},
    "temoin_faille": {"m": [20, 30, 50, 100],
                      "cas": [[0.6, 0.1], [0.8, 0.1], [0.8, 0.3], [0.95, 0.05], [0.3, 0.3]],
                      "niveau": 0.95, "tirages": 20000},
    "precision_courbe": {"m": [30, 50, 100, 200, 400], "niveau": 0.95},
}
TACHES = ["nul", "rappel_binormal", "temoin_faille"]


def calculer(manifeste: dict) -> dict:
    c = CONFIG
    a = c["alpha"]
    fpr = []
    for n in c["grille_n"]:
        k = p.k_empirique(n, a)
        fpr.append({"n": n, "k": k,
                    "quantiles": dict(zip(map(str, c["probas_fpr"]), p.fpr_reel_quantiles(n, k, c["probas_fpr"]))),
                    "p_au_dela_2pc": p.fpr_reel_proba_au_dela(n, k, 0.02),
                    "k_garanti": p.k_garanti(n, c["garanti"]["alpha"], c["garanti"]["delta"])})
    o = c["objectif_reserve"]
    ok = {n: p.fpr_reel_proba_au_dela(n, p.k_empirique(n, a), o["fpr_max"]) <= o["delta"]
          for n in range(o["balayage_n"][0], o["balayage_n"][1] + 1)}
    n_min = next((n for n in sorted(ok) if all(ok[x] for x in ok if x >= n)), None)

    g = generateur(manifeste["graines"]["nul"])
    nul = []
    for n in c["nul"]["n"]:
        k = p.k_empirique(n, a)
        for h in c["nul"]["h"]:
            for niv in c["nul"]["niveaux"]:
                bas, haut = p.alertes_honnetes_intervalle(n, k, h, niv)
                nul.append({"n": n, "h": h, "niveau": niv, "intervalle": [bas, haut],
                            "proba_ecart": {str(f): p.puissance_nul(n, k, h, f, niv, c["nul"]["tirages"], g)
                                            for f in c["nul"]["inflation"]}})

    g = generateur(manifeste["graines"]["rappel_binormal"])
    rb = c["rappel_binormal"]
    rappel = [p.simuler_rappel_binormal(n, m, r, a, rb["tirages"], g)
              for n in rb["n"] for m in rb["m"] for r in rb["rappel_vrai"]]

    g = generateur(manifeste["graines"]["temoin_faille"])
    tf = c["temoin_faille"]
    faille = [{"m": m, "e_bras": eb, "e_naif": en,
               "puissance": p.puissance_temoin_faille(m, eb, en, tf["niveau"], tf["tirages"], g)}
              for m in tf["m"] for eb, en in tf["cas"]]

    pc = c["precision_courbe"]
    precision = []
    for m in pc["m"]:
        bas, haut = p.clopper_pearson(m // 2, m, pc["niveau"])
        precision.append({"m": m, "demi_largeur_a_0_5": float((haut - bas) / 2)})

    return {"fpr_reel": fpr, "n_minimal_reserve": n_min, "nul": nul, "rappel_binormal": rappel,
            "temoin_faille": faille, "precision_courbe": precision,
            "versions_lois": {"scipy_beta": stats.beta.name, "scipy_betabinom": stats.betabinom.name}}


def main() -> int:
    racine = Path(__file__).resolve().parents[1]
    horodatage = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    run_id = f"{horodatage}-bras-puissance-seuil-v1"
    chemin, manifeste = creer_manifeste(racine, run_id, CONFIG, TACHES,
                                        commande="PYTHONPATH=src python scripts/bras_attaque_puissance_seuil_v1.py")
    resultat = calculer(manifeste)
    sortie = ecrire_resultat(racine, chemin, "puissance-seuil-v1", resultat)
    print(chemin)
    print(sortie)
    print("n minimal de la réserve honnête :", resultat["n_minimal_reserve"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
