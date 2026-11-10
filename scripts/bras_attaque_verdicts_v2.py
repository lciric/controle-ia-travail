"""Tables de conception de la règle du bras, version 3 (contre-lecture 3) : pire fausse hausse d'une cellule ordinaire
selon les tailles, « résiste » quand la hausse vraie vaut δ ou 15 points, échelon « sans objet » sur une course saine,
test de rang à 4 000 tirages, notes entières avec et sans départage. Aucune donnée.
Usage (racine d'un arbre propre) : PYTHONPATH=src python scripts/bras_attaque_verdicts_v2.py
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy import stats

from controle_ia.bras_attaque import verdicts_v1 as v1
from controle_ia.bras_attaque import verdicts_v2 as v2
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, generateur

CONFIG = {
    "objet": "règle du bras, conception v3 (contre-lecture 3) : multiplicité, résiste, sans objet, rang, notes entières",
    "niveau": 0.95,
    "delta": 0.10,
    "fausse_hausse": {"tailles": [[100, 100], [200, 200], [100, 200], [100, 300], [100, 1000], [200, 400]],
                      "grille": 201},
    "temoin_pire": {"m": [100, 200], "grille": 201},
    "resiste": {"m": [100, 200], "hausses": [0.10, 0.15], "naifs": [0.0, 0.5, 51],
                "cas": [[0.02, 0.06], [0.30, 0.0], [0.10, 0.0]]},
    "sans_objet": {"temoin": {"m": 100, "e_bras": 0.6, "e_naif": 0.1},
                   "nul": [[1000, 1000], [1000, 500], [600, 1000], [2000, 1000]], "M": [1, 5, 10],
                   "tirages_rang": 4000, "ecart_aire": 0.05, "alpha_famille": 0.05},
    "rang": {"n": 1000, "h": 500, "decalages": [-0.27, -0.15, 0.0, 0.15, 0.27], "niveau_test": 0.01,
             "ecart_aire": 0.05, "tirages": 4000},
    "notes_entieres": {"n": 200, "k": 2, "seuil_fpr": 0.02, "tirages": 20000,
                       "lois": {"decroissante": [0.30, 0.25, 0.18, 0.12, 0.07, 0.04, 0.02, 0.01, 0.005, 0.003, 0.002],
                                "binomiale_10_0.3": [float(x) for x in stats.binom.pmf(np.arange(11), 10, 0.3)]}},
}
TACHES = ["sans_objet", "rang", "notes_entieres"]


def calculer(manifeste: dict) -> dict:
    c = CONFIG
    fausse = [{"m_bras": mb, "m_naif": mn,
               **dict(zip(("probabilite", "evasion"), v2.fausse_hausse_pire(mb, mn, c["delta"], c["niveau"],
                                                                         c["fausse_hausse"]["grille"])))}
              for mb, mn in c["fausse_hausse"]["tailles"]]
    temoin_pire = {str(m): dict(zip(("probabilite", "evasion"),
                                    v1.fausse_cassure_pire(m, c["niveau"], c["temoin_pire"]["grille"])))
                   for m in c["temoin_pire"]["m"]}
    r = c["resiste"]
    naifs = np.linspace(*r["naifs"][:2], int(r["naifs"][2]))
    resiste_pire = [{"m": m, "hausse": hs,
                     **dict(zip(("probabilite", "evasion_naive"),
                                v2.resiste_sous_hausse_pire(m, m, hs, naifs, c["delta"], c["niveau"])))}
                    for m in r["m"] for hs in r["hausses"]]
    resiste_cas = [{"m": m, "e_naif": en, "hausse": hs,
                    "resiste": v2.resiste_sous_hausse(m, m, en, hs, c["delta"], c["niveau"])}
                   for m in r["m"] for en, hs in r["cas"]]
    s = c["sans_objet"]
    t = s["temoin"]
    tenu = v1.temoin_faille_exact(t["m"], t["e_bras"], t["e_naif"], c["niveau"])["constitue_et_casse"]
    g = generateur(manifeste["graines"]["sans_objet"])
    sans_objet = []
    for n, h in s["nul"]:
        for M in s["M"]:
            nul = v2.nul_echec_course_saine(n, h, M, s["tirages_rang"], g, s["ecart_aire"], s["alpha_famille"])
            sans_objet.append({"n": n, "h": h, "M": M, "temoin_tenu": tenu, **nul,
                               "sans_objet": v2.sans_objet_course_saine(tenu, nul["un_nul"], M)})
    q = c["rang"]
    gr = generateur(manifeste["graines"]["rang"])
    rang = [{"decalage": d, "proba_ecart": v1.puissance_rang_binormal(q["n"], q["h"], d, q["niveau_test"],
                                                                       q["ecart_aire"], q["tirages"], gr)}
            for d in q["decalages"]]
    e = c["notes_entieres"]
    ge = generateur(manifeste["graines"]["notes_entieres"])
    notes = {nom: v2.fpr_notes_entieres(e["n"], e["k"], np.array(loi), e["seuil_fpr"], e["tirages"], ge)
             for nom, loi in e["lois"].items()}
    return {"fausse_hausse_pire": fausse, "temoin_pire": temoin_pire, "resiste_sous_hausse_pire": resiste_pire,
            "resiste_cas": resiste_cas, "sans_objet": sans_objet, "rang": rang, "notes_entieres": notes}


def main() -> int:
    racine = Path(__file__).resolve().parents[1]
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-bras-verdicts-v2"
    chemin, manifeste = creer_manifeste(racine, run_id, CONFIG, TACHES,
                                        commande="PYTHONPATH=src python scripts/bras_attaque_verdicts_v2.py")
    sortie = ecrire_resultat(racine, chemin, "verdicts-v2", calculer(manifeste))
    print(chemin)
    print(sortie)
    return 0


if __name__ == "__main__":
    sys.exit(main())
