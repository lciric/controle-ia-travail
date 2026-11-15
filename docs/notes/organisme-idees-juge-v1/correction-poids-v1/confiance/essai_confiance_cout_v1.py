"""Coût de calcul par carte, méthode par méthode — v1. Mise au point exploratoire.

Rejoue, pour 10 mondes du cas « interieur » (mêmes graines que les lots, J et n_tr donnés), les appels de calcul de chaque
méthode séparément (mêmes fonctions que `essai_confiance_methodes_v1.juger`) et mesure le temps processeur
(time.process_time) de chacune. La machine est partagée : les temps sont indicatifs (ordre de grandeur).
Usage : python -I essai_confiance_cout_v1.py N_TR J SORTIE.json
"""

import json
import math
import os
import platform
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402

import essai_confiance_banc_v1 as bc  # noqa: E402
import essai_confiance_lot_v1 as lot  # noqa: E402
import essai_confiance_methodes_v1 as em  # noqa: E402


def mesure(f):
    t = time.process_time()
    f()
    return time.process_time() - t


def main():
    n_tr, J, sortie = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    temps = {}
    for r in range(10):
        rng, arch, pm, cartes, theta, ss = lot.fabriquer("interieur", J, r)
        d = em.preparer(rng, arch, pm, cartes, n_tr)
        At, yt, Mt = d["At"][:n_tr], d["yt"][:n_tr], d["Mt"][:, :n_tr]
        Af, yf, Mf = d["Af"], d["yf"], d["Mf"]
        kap = [0.0, 0.0]

        def v9():
            init = None
            for t in bc.INSTANTS:
                _, _, init = bc.em_certifie(Af[:t], yf[:t], np.ones((1, t)), Mf[:, :t], bc.ITER, init)

        def bb_t(nc):
            def f():
                init, Vc = None, None
                for t in bc.INSTANTS:
                    _, _, init, Vc = bc.borne_sur_ensemble(Af[:t], yf[:t], Mf[:, :t], At[:nc], yt[:nc], Mt[:, :nc], kap,
                                                           init=init, Vc=Vc)
            return f

        def preq():
            bc.log_prequentiel(np.vstack([At, Af]), np.concatenate([yt, yf]), np.hstack([Mt, Mf]), iters=40)

        def bb_s():
            init, Vc = None, None
            for t in em.INSTANTS_B:
                _, _, init, Vc = bc.borne_sur_ensemble(Af[100:t], yf[100:t], Mf[:, 100:t], Af[:100], yf[:100], Mf[:, :100],
                                                       kap, init=init, Vc=Vc)

        def bb_q():
            for t in bc.INSTANTS:
                s0 = t - 25
                bc.borne_sur_ensemble(Af[s0:t], yf[s0:t], Mf[:, s0:t], np.vstack([At, Af[:s0]]), np.concatenate([yt, yf[:s0]]),
                                      np.hstack([Mt, Mf[:, :s0]]), kap)

        for nom, f in (("v9_banc (référence, 8 instants)", v9), ("prédicteur séquentiel (BB_T_seq, BB_Q)", preq),
                       ("BB_T_seq (maximum contraint, 8 instants)", bb_t(n_tr)),
                       ("BB_T_coupe (maximum contraint, 8 instants)", bb_t(n_tr // 2)),
                       ("BB_S_moitie (4 instants)", bb_s), ("BB_Q_blocs (8 blocs)", bb_q),
                       ("F1_en_ligne", lambda: em._f1_en_ligne(d, 0)), ("F2_moitie", lambda: em._f2_moitie(d, 0))):
            temps.setdefault(nom, []).append(mesure(f))
    doc = {"essai": "essai_confiance_cout_v1", "cas": "interieur", "J": J, "n_tr": n_tr, "mondes": 10,
           "racine_seedsequence": lot.RACINE, "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "charge_machine_1min": os.getloadavg()[0],
           "secondes_processeur_par_carte": {k: {"moyenne": round(float(np.mean(v)), 4), "max": round(float(np.max(v)), 4)}
                                             for k, v in temps.items()}}
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(json.dumps(doc, ensure_ascii=False))


if __name__ == "__main__":
    main()
