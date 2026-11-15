"""Essai 3 — puissance : vraies découvertes (une composante neuve, trois doses), toutes méthodes sur les MÊMES tirages et
aux MÊMES instants — v1.

Mise au point exploratoire, aucune revendication. `python -I -B essai_regret_puissance_v1.py DOSE NB` ; 3 processus.
Monde = (1 − dose)·(½ L1 + ½ L2) + dose·N, N loi softmax neuve (hors de l'archive) ; carte = loi du monde.
Comparaisons appariées : pour chaque méthode, nombre de mondes promus par elle et non par MAX-v9r, et l'inverse.
Graines : SeedSequence(ENTROPIE, spawn_key=(indice de la dose,)). Sortie : sorties/essai_regret_puissance_v1--dDOSE.json.
"""
import json
import os
import platform
import sys
import time
from multiprocessing import Pool

import numpy as np
import scipy

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import essai_regret_banc_v1 as bc  # noqa: E402
import essai_regret_juge_v1 as jg  # noqa: E402

ENTROPIE = 2026111503
DOSES = (0.1, 0.2, 0.35)   # fixées avant tout essai de puissance (un seul monde d'essai du code, dose 0,5, log W ≈ 24 : saturé)


def _un(arg):
    dose, graine, nb_is = arg
    return jg.juger("decouverte", graine, methodes_v9r=True, dose=dose, nb_is=nb_is)


def main():
    dose, nb = float(sys.argv[1]), int(sys.argv[2])
    nb_is = int(sys.argv[3]) if len(sys.argv) > 3 else 500
    nom = f"essai_regret_puissance_v1--d{dose}.json"
    chemin = os.path.join(ICI, "sorties", nom)
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    ss = np.random.SeedSequence(ENTROPIE, spawn_key=(DOSES.index(dose),))
    graines = [int(c.generate_state(1)[0]) for c in ss.spawn(nb)]
    t0 = time.time()
    with Pool(3) as pool:
        sorties = pool.map(_un, [(dose, g_, nb_is) for g_ in graines], chunksize=4)
    methodes = [k for k in sorties[0][0] if not k.startswith("R1-La-sous")]
    ref = np.array([s[0]["MAX-v9r"] for s in sorties])
    refLa = np.array([s[0]["MAX-La"] for s in sorties])
    lignes = {}
    for mth in methodes:
        v = np.array([s[0][mth] for s in sorties])
        k = int(v.sum())
        lignes[mth] = {"promues": k, "mondes": nb, "taux": round(k / nb, 4), "intervalle_95": bc.clopper_pearson(k, nb),
                       "promues_par_elle_seule_contre_MAX-v9r": int((v & ~ref).sum()),
                       "promues_par_MAX-v9r_seul": int((~v & ref).sum()),
                       "promues_par_elle_seule_contre_MAX-La": int((v & ~refLa).sum()),
                       "promues_par_MAX-La_seul": int((~v & refLa).sum()),
                       "log_W_max_mediane": round(float(np.median([s[1][mth] for s in sorties])), 3)}
    sortie = {
        "essai": "essai_regret_puissance_v1", "dose": dose, "mondes": nb, "echantillons_importance": nb_is,
        "graines": {"entropie": ENTROPIE, "spawn_key": [DOSES.index(dose)], "premieres": graines[:3]},
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "lignes": lignes,
        "R1_La_lots_sous_le_maximum_exact": int(sum(s[0]["R1-La-sous-le-maximum"] for s in sorties)),
        "ecart_certificat_max": round(max(s[2]["ecart_max_certificat"] for s in sorties), 6),
        "duree_par_monde_s_moyenne": {k: round(float(np.mean([s[2]["duree_s"][k] for s in sorties])), 4)
                                      for k in sorties[0][2]["duree_s"]},
        "membres_ajustes_v9r": sorties[0][2]["membres_ajustes"], "lots_v9r": sorties[0][2]["lots"],
        "duree_totale_s": round(time.time() - t0, 1),
    }
    with open(chemin, "w") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: (v["promues"], v["taux"]) for k, v in sortie["lignes"].items()}, ensure_ascii=False))
    print("durée", sortie["duree_totale_s"])


if __name__ == "__main__":
    main()
