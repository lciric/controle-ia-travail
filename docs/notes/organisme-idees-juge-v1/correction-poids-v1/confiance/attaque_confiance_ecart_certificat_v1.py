"""Écart de certificat du « v9 du banc » de l'auteur, mesuré avec ses propres fonctions — v1.

Programme du réfutateur, mise au point exploratoire, aucune revendication. Processeur seul.
Pour des mondes de puissance de l'auteur (V1, J = 3, mêmes graines), on calcule le dénominateur du v9 du banc de trois
façons, toujours sur les mêmes tirages frais et aux mêmes instants :
  (a) comme le banc : `essai_confiance_banc_v1.em_certifie`, 80 pas, départ chaud d'un instant au suivant ;
  (b) la même fonction de l'auteur, 5 000 pas, départ à froid à chaque instant ;
  (c) mon optimiseur (points intérieurs, `attaque_confiance_v1.newton`).
Les trois valeurs sont des majorants certifiés du même maximum ; leur écart est donc de l'écart de certificat pur.
On rapporte, par monde : la richesse maximale log W du v9 sous (a), (b), (c) ; l'écart de certificat de (a) à l'instant et
à la partition où il est le plus grand ; et la promotion (seuil log 20) sous chacun.
Usage : python -I -B attaque_confiance_ecart_certificat_v1.py CAS DEBUT FIN SORTIE.json
"""

import json
import math
import os
import platform
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import numpy as np  # noqa: E402

import attaque_confiance_v1 as at  # noqa: E402
import essai_confiance_banc_v1 as bc  # noqa: E402
import essai_confiance_lot_v1 as lot  # noqa: E402
import essai_confiance_methodes_v1 as em  # noqa: E402


def main():
    cas, debut, fin, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe")
    t0 = time.time()
    seuil = math.log(1.0 / bc.ALPHA)
    lignes = []
    for r in range(debut, fin):
        rng, arch, probas_monde, cartes, theta, ss = lot.fabriquer(cas, 3, r)
        d = em.preparer(rng, arch, probas_monde, cartes, 100)
        Af, yf, Mf = d["Af"], d["yf"], d["Mf"]
        cq = np.concatenate([[0.0], np.cumsum(d["logq"]["decouverte"])])
        w = {"a_banc_80_pas": -np.inf, "b_auteur_5000_pas": -np.inf, "c_points_interieurs": -np.inf}
        pire = {"ecart": 0.0}
        init = None
        for t in bc.INSTANTS:
            Ua, fa, init = bc.em_certifie(Af[:t], yf[:t], np.ones((1, t)), Mf[:, :t], bc.ITER, init)
            Ub, fb, _ = bc.em_certifie(Af[:t], yf[:t], np.ones((1, t)), Mf[:, :t], 5000)
            Uc = at.newton(Af[:t], yf[:t], Mf[:, :t], np.ones((1, 1, t)), bc.K)["U"]
            w["a_banc_80_pas"] = max(w["a_banc_80_pas"], cq[t] - float(Ua[0].max()))
            w["b_auteur_5000_pas"] = max(w["b_auteur_5000_pas"], cq[t] - float(Ub[0].max()))
            w["c_points_interieurs"] = max(w["c_points_interieurs"], cq[t] - float(Uc[0].max()))
            e = float(Ua[0].max() - min(Ub[0].max(), Uc[0].max()))
            if e > pire["ecart"]:
                i = int(np.argmax(Ua[0]))
                pire = {"ecart": round(e, 4), "instant": t, "partition": d["parts"][i]["nom"],
                        "valeur_atteinte_80_pas": round(float(fa[0, i]), 4), "majorant_80_pas": round(float(Ua[0, i]), 4),
                        "majorant_5000_pas_meme_partition": round(float(Ub[0, i]), 4),
                        "points_dans_le_petit_morceau": int(min(Mf[i, :t].sum(), t - Mf[i, :t].sum()))}
        lignes.append({"monde": r, "log_w_v9": {k: round(v, 4) for k, v in w.items()},
                       "promue_v9": {k: bool(v >= seuil) for k, v in w.items()}, "pire_ecart_du_banc": pire})
    ec = np.array([l["pire_ecart_du_banc"]["ecart"] for l in lignes])
    pr = {k: int(sum(l["promue_v9"][k] for l in lignes)) for k in lignes[0]["promue_v9"]}
    doc = {"essai": "attaque_confiance_ecart_certificat_v1", "cas": cas, "J": 3, "mondes": [debut, fin],
           "graines": "celles de l'auteur : SeedSequence(entropy=%d, spawn_key=(indice du cas, J, monde))" % lot.RACINE,
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "pas_du_banc": bc.ITER, "promues_v9_sur_%d" % len(lignes): pr,
           "pire_ecart_par_monde_nat": {"mediane": float(np.median(ec)), "quartile_haut": float(np.percentile(ec, 75)),
                                        "max": float(ec.max()), "part_au_dessus_de_1_nat": float((ec > 1.0).mean())},
           "ecart_b_c_max_nat": float(max(abs(l["log_w_v9"]["b_auteur_5000_pas"] - l["log_w_v9"]["c_points_interieurs"])
                                         for l in lignes)),
           "duree_s": round(time.time() - t0, 1), "lignes": lignes}
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    print(json.dumps({k: v for k, v in doc.items() if k != "lignes"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
