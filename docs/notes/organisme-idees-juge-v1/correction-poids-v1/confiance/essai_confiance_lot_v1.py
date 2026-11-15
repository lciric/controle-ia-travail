"""Lot de mondes d'un cas (taille ou puissance) — v1. Mise au point exploratoire, aucune revendication.

Usage : python -I essai_confiance_lot_v1.py CAS DEBUT FIN N_TR J SORTIE.json [--sans-artefacts]
(le dossier du script est ajouté au chemin ; aucun module du dépôt de l'organisme n'est importé).

Graines (règle R9) : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(indice du cas, J, indice du monde)) ; un seul
générateur par monde, pour l'archive, les paramètres du monde, la carte, puis les tirages (frais d'abord, entraînement
ensuite). Les tirages frais d'un monde sont donc les mêmes pour toute méthode et pour tout n_tr.

Cas de taille (monde = membre du v9 du banc ; carte « copie » = loi du monde ; carte « hors_classe » = 0,7 monde + 0,3
softmax aléatoire) : interieur, sommet, bord, morceaux_archive, morceaux_grille, sous_population, bruit_extreme.
Cas de puissance (monde hors du nul ; carte = loi du monde) : V1_0.25, V1_0.50, V1_0.75 (S1' = softmax(W1 + delta Delta, b1),
Delta ~ N(0, 1) centré sur les issues, comme la ligne V1 du préenregistrement de l'idée 1.1).
"""

import json
import os
import platform
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402

import essai_confiance_banc_v1 as bc  # noqa: E402
import essai_confiance_methodes_v1 as em  # noqa: E402

RACINE = 20261115_31
CAS_TAILLE = ("interieur", "sommet", "bord", "morceaux_archive", "morceaux_grille", "sous_population", "bruit_extreme")
CAS_PUISSANCE = ("V1_0.25", "V1_0.50", "V1_0.75")
TOUS = CAS_TAILLE + CAS_PUISSANCE


def _index(parts, pred):
    return [i for i, p in enumerate(parts) if pred(p)]


def monde_taille(rng, arch, cas):
    """Rend (i_part, rho, rt, b) d'un membre du v9 du banc."""
    parts = bc.partitions(arch)
    J = arch["J"]
    e = np.eye(J)
    if cas == "interieur":
        i = 0
        rho = float(rng.uniform(0.05, 0.4))
        rt = rng.dirichlet(np.ones(bc.K))
        bb = rng.dirichlet(np.ones(J))
        b = np.stack([bb, bb])
    elif cas == "sommet":
        i, rho, rt = 0, 0.0, np.full(bc.K, 1.0 / bc.K)
        j = int(rng.integers(0, J))
        b = np.stack([e[j], e[j]])
    elif cas == "bord":
        i = int(rng.choice(_index(parts, lambda p: p["nom"].startswith("grille"))))
        rho, rt = 0.0, np.full(bc.K, 1.0 / bc.K)
        j1, j2 = rng.choice(J, size=2, replace=False)
        a = float(rng.uniform(0.2, 0.8))
        b = np.stack([a * e[j1] + (1 - a) * e[j2], e[int(rng.integers(0, J))]])
    elif cas == "morceaux_archive":
        i = _index(parts, lambda p: p["nom"].startswith("archive"))[0]
        rho, rt = 0.0, np.full(bc.K, 1.0 / bc.K)
        b = np.stack([e[1], e[0]])  # si_sinon(z_jA > s_A, S1, S2)
    elif cas == "morceaux_grille":
        i = int(rng.choice(_index(parts, lambda p: p["nom"].startswith("grille"))))
        rho, rt = 0.0, np.full(bc.K, 1.0 / bc.K)
        b = np.stack([e[1], e[0]])
    elif cas == "sous_population":
        i = _index(parts, lambda p: p["sorte"] == "sp")[0]
        rho, rt = 0.0, np.full(bc.K, 1.0 / bc.K)
        b = np.stack([e[0], e[1]])
    elif cas == "bruit_extreme":
        i = 0
        rho = 0.95
        rt = np.eye(bc.K)[int(rng.integers(0, bc.K))]
        bb = rng.dirichlet(np.ones(J))
        b = np.stack([bb, bb])
    else:
        raise ValueError(cas)
    return i, rho, rt, b


def fabriquer(cas, J, r):
    ss = np.random.SeedSequence(entropy=RACINE, spawn_key=(TOUS.index(cas), J, r))
    rng = np.random.default_rng(ss)
    arch = bc.tirer_archive(rng, J)
    parts = bc.partitions(arch)
    if cas in CAS_TAILLE:
        i, rho, rt, b = monde_taille(rng, arch, cas)
        p = parts[i]

        def probas_monde(z, g):
            m = bc.masques([p], z, g)[0]
            return bc.probas_membre(bc.lois_connues(arch, z), m, rho, rt, b)
        autre = bc.softmax_par(rng)

        def hors_classe(z, g):
            return 0.7 * probas_monde(z, g) + 0.3 * bc.probas_softmax(autre, z)
        return rng, arch, probas_monde, {"copie": probas_monde, "hors_classe": hors_classe}, (i, rho, rt, b), ss
    delta = float(cas.split("_")[1])
    W1, b1 = arch["S1"]
    Dl = rng.normal(size=W1.shape)
    Dl = Dl - Dl.mean(axis=0, keepdims=True)
    par = (W1 + delta * Dl, b1)

    def probas_monde(z, g):
        return bc.probas_softmax(par, z)
    return rng, arch, probas_monde, {"decouverte": probas_monde}, None, ss


def main():
    cas, debut, fin, n_tr, J, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    artefacts = "--sans-artefacts" not in sys.argv
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe (jamais d'écrasement)")
    t0 = time.time()
    lignes = []
    for r in range(debut, fin):
        rng, arch, probas_monde, cartes, theta, ss = fabriquer(cas, J, r)
        d = em.preparer(rng, arch, probas_monde, cartes, n_tr)
        tc = time.perf_counter()
        res, couv = em.juger(d, n_tr, None if theta is None else theta[0], artefacts=artefacts and cas in CAS_TAILLE,
                             theta_star=theta)
        res["_secondes_par_monde"] = round(time.perf_counter() - tc, 4)
        res["_couverture"] = couv
        lignes.append({"monde": r, "spawn_key": list(ss.spawn_key), "resultats": res})
    doc = {"essai": "essai_confiance_lot_v1", "cas": cas, "J": J, "n_tr": n_tr, "mondes": [debut, fin],
           "racine_seedsequence": RACINE, "derivation": "SeedSequence(entropy=RACINE, spawn_key=(indice du cas, J, r))",
           "indice_du_cas": TOUS.index(cas), "alpha": bc.ALPHA, "betas": list(bc.BETAS), "instants": list(bc.INSTANTS),
           "grille": list(bc.GRILLE), "iter_em": bc.ITER, "gammas": list(bc.GAMMAS), "eps_preq": bc.EPS_PREQ,
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "duree_s": round(time.time() - t0, 1), "lignes": lignes}
    with open(sortie, "w") as fh:
        json.dump(doc, fh)
    print(f"{cas} J={J} n_tr={n_tr} [{debut},{fin}) en {doc['duree_s']} s -> {sortie}")


if __name__ == "__main__":
    main()
