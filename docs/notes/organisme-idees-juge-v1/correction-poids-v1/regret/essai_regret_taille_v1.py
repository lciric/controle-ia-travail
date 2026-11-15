"""Essai 2 — taille : taux de promotion d'une copie exacte d'un membre du nul (et de membres défavorables) — v1.

Mise au point exploratoire, aucune revendication. Un cas par appel (`python -I -B essai_regret_taille_v1.py CAS NB [v9r]`),
3 processus. Carte = loi du monde (copie exacte). Une méthode valide promeut au plus α = 5 % des copies d'un membre de sa
classe ; les deux façons des fiches (A1-EG, A1-BAYES : en ligne sans correction ; A2-MOITIE) servent d'artefact.
Graines : SeedSequence(ENTROPIE, spawn_key=(indice du cas,)) puis un enfant par monde. Sortie :
sorties/essai_regret_taille_v1--CAS.json (jamais écrasée).
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

ENTROPIE = 2026111502
CAS = ("interieur_lineaire", "sommet_L1", "bord_L2_delta", "morceaux_archive", "poids_extremes_morceaux",
       "morceaux_hors_archive")


def _un(arg):
    cas, graine, v9r = arg
    return jg.juger(cas, graine, methodes_v9r=v9r, nb_is=500 if v9r else 1000)  # 500 échantillons sur v9r (temps)


def main():
    cas, nb = sys.argv[1], int(sys.argv[2])
    v9r = len(sys.argv) > 3 and sys.argv[3] == "v9r"
    chemin = os.path.join(ICI, "sorties", f"essai_regret_taille_v1--{cas}.json")
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    ss = np.random.SeedSequence(ENTROPIE, spawn_key=(CAS.index(cas),))
    graines = [int(c.generate_state(1)[0]) for c in ss.spawn(nb)]
    t0 = time.time()
    with Pool(3) as pool:
        sorties = pool.map(_un, [(cas, g_, v9r) for g_ in graines], chunksize=4)
    methodes = [k for k in sorties[0][0] if not k.startswith("R1-La-sous")]
    lignes = {}
    for mth in methodes:
        k = sum(int(s[0][mth]) for s in sorties)
        mx = np.array([s[1][mth] for s in sorties])
        lignes[mth] = {"promues": k, "mondes": nb, "taux": round(k / nb, 4), "intervalle_95": bc.clopper_pearson(k, nb),
                       "log_W_max_mediane": round(float(np.median(mx)), 3), "log_W_max_q95": round(float(np.quantile(mx, 0.95)), 3)}
    sortie = {
        "essai": "essai_regret_taille_v1", "cas": cas, "mondes": nb, "structure_v9r": v9r,
        "graines": {"entropie": ENTROPIE, "spawn_key": [CAS.index(cas)], "premieres": graines[:3]},
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "alpha": bc.ALPHA, "instants": [int(t) for t in bc.INSTANTS], "tirages": bc.N,
        "lignes": lignes,
        "R1_La_lots_sous_le_maximum_exact": int(sum(s[0]["R1-La-sous-le-maximum"] for s in sorties)),
        "ecart_certificat_max": round(max(s[2]["ecart_max_certificat"] for s in sorties), 6),
        "duree_par_monde_s_moyenne": {k: round(float(np.mean([s[2]["duree_s"][k] for s in sorties])), 4)
                                      for k in sorties[0][2]["duree_s"]},
        "duree_totale_s": round(time.time() - t0, 1),
    }
    with open(chemin, "w") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: (v["promues"], v["taux"], v["intervalle_95"]) for k, v in lignes.items()}, ensure_ascii=False))
    print("sous le maximum :", sortie["R1_La_lots_sous_le_maximum_exact"], "durée", sortie["duree_totale_s"])


if __name__ == "__main__":
    main()
