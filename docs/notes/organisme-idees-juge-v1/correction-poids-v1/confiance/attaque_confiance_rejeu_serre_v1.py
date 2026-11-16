"""Rejeu « serré » de la puissance annoncée : les mondes de l'auteur, mes dénominateurs — v1.

Programme du réfutateur, mise au point exploratoire, aucune revendication. Processeur seul.
But : savoir si le gain de puissance annoncé pour l'ensemble coupé (BB_T_coupe) contre le maximum certifié (v9 du banc)
tient quand les deux dénominateurs sont calculés par un optimiseur serré. Le banc de l'auteur calcule ses maxima par
80 pas d'un algorithme lent ; la valeur rendue reste un majorant, mais elle porte un écart de certificat qui pèse sur
les deux bras, pas forcément de la même façon.

Ce programme importe les modules de l'auteur (ce sont eux qu'on rejoue) pour refaire exactement ses mondes, ses tirages
et le seuil kappa de son ensemble coupé (même prédicteur, même lissage) ; il importe mon programme d'attaque pour le
calcul des majorants (points intérieurs, écart de certificat de l'ordre de 0,002 nat). Aucun fichier des dossiers de
copie n'est importé ni exécuté. Mêmes tirages frais, mêmes instants, mêmes seuils que le lot de l'auteur.

Usage : python -I -B attaque_confiance_rejeu_serre_v1.py CAS DEBUT FIN N_TR SORTIE.json LOT_AUTEUR.json [LOT_AUTEUR.json ...]
(CAS : V1_0.25, V1_0.50 ou V1_0.75 ; J = 3 ; les lots de l'auteur donnent ses promotions, monde par monde.)
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

GAMMAS_AUTEUR = tuple(bc.GAMMAS)                       # (0 ; 0,3 ; 1 ; 3)
GAMMAS_UNION = tuple(sorted(set(GAMMAS_AUTEUR) | set(at.GAMMAS)))


def main():
    cas, debut, fin, n_tr, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe")
    auteur = {}
    for p in sys.argv[6:]:
        d = json.load(open(p))
        assert d["cas"] == cas and d["n_tr"] == n_tr and d["J"] == 3
        for l in d["lignes"]:
            auteur[l["monde"]] = l["resultats"]["decouverte"]
    t0 = time.time()
    K = bc.K
    betas = list(bc.BETAS)
    i_aut = [GAMMAS_UNION.index(g) for g in GAMMAS_AUTEUR]
    lignes = []
    for r in range(debut, fin):
        rng, arch, probas_monde, cartes, theta, ss = lot.fabriquer(cas, 3, r)
        d = em.preparer(rng, arch, probas_monde, cartes, n_tr)
        lim = np.array([p["limite"] for p in d["parts"]])
        Af, yf, Mf = d["Af"], d["yf"], d["Mf"]
        At, yt, Mt = d["At"][:n_tr], d["yt"][:n_tr], d["Mt"][:, :n_tr]
        cq = np.concatenate([[0.0], np.cumsum(d["logq"]["decouverte"])])
        # seuil kappa de l'ensemble coupé, par le code de l'auteur (essai_confiance_methodes_v1.juger, bloc BB_T_coupe)
        h = n_tr // 2
        i1, par1 = bc.ajuster_meilleur(At[:h], yt[:h], Mt[:, :h])
        l2 = float(np.log(bc.proba_lissee(At[h:], yt[h:], Mt[:, h:], i1, par1)).sum())
        kap = np.array([l2 - math.log(1.0 / b) for b in betas])
        Ac, yc, Mc = At[h:], yt[h:], Mt[:, h:]
        nc = Ac.shape[0]
        Vc = at.newton(Ac, yc, Mc, np.ones((1, 1, nc)), K)["U"][0]
        w = {"v9": -np.inf, "limite": -np.inf, "v8": -np.inf}
        w.update({f"coupe_grille_auteur|beta={b}": -np.inf for b in betas})
        w.update({f"coupe_grille_union|beta={b}": -np.inf for b in betas})
        ecart = 0.0
        for t in bc.INSTANTS:
            lam = np.array(GAMMAS_UNION) * t / nc
            L = len(lam)
            A = np.vstack([Af[:t], Ac])
            y = np.concatenate([yf[:t], yc])
            M = np.hstack([Mf[:, :t], Mc])
            poids = np.concatenate([np.ones((L, 1, t)), lam[:, None, None] * np.ones((L, 1, nc))], axis=2)
            res = at.newton(A, y, M, poids, K)
            ecart = max(ecart, float(res["ecart"].max()))
            U = res["U"]                                              # (L, P)
            U0 = U[GAMMAS_UNION.index(0.0)]
            w["v9"] = max(w["v9"], cq[t] - float(U0.max()))
            w["limite"] = max(w["limite"], cq[t] - float(U0[lim].max()))
            w["v8"] = max(w["v8"], cq[t] - float(U0[0]))
            for ib, b in enumerate(betas):
                Bu = (U - lam[:, None] * kap[ib])
                vide = Vc < kap[ib]
                Du = float(np.where(vide, -np.inf, Bu.min(axis=0)).max())
                Da = float(np.where(vide, -np.inf, Bu[i_aut].min(axis=0)).max())
                w[f"coupe_grille_union|beta={b}"] = max(w[f"coupe_grille_union|beta={b}"], cq[t] - Du)
                w[f"coupe_grille_auteur|beta={b}"] = max(w[f"coupe_grille_auteur|beta={b}"], cq[t] - Da)
        a = auteur.get(r)
        lignes.append({"monde": r, "ecart_certificat_max": round(ecart, 6),
                       "serre": {k: round(float(min(v, 1e6)), 4) for k, v in w.items()},
                       "auteur": None if a is None else {k: round(a[k]["log_w_max"], 4) for k in
                                                         ("v9_banc", "limite", "v8_banc", "BB_T_coupe|beta=0.01",
                                                          "BB_T_coupe|beta=0.025")}})
    doc = {"essai": "attaque_confiance_rejeu_serre_v1", "cas": cas, "J": 3, "n_tr": n_tr, "mondes": [debut, fin],
           "graines": "celles de l'auteur : SeedSequence(entropy=%d, spawn_key=(indice du cas, J, monde))" % lot.RACINE,
           "alpha": bc.ALPHA, "betas": betas, "instants": list(bc.INSTANTS), "gammas_auteur": list(GAMMAS_AUTEUR),
           "gammas_union": list(GAMMAS_UNION), "paliers_barriere": list(at.PALIERS),
           "seuils_log": {"v9": math.log(1 / bc.ALPHA), **{f"beta={b}": math.log(1 / (bc.ALPHA - b)) for b in betas}},
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "duree_s": round(time.time() - t0, 1), "lignes": lignes}
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    print(f"écrit : {sortie}")


if __name__ == "__main__":
    main()
