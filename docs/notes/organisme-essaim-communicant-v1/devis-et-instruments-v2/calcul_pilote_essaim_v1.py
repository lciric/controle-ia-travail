#!/usr/bin/env python3
"""Pilote-instrument de l'essaim — v1 : coût (estimation et vrai pire) par espèce et par variante, puissance du test
« (a) bat la base gloutonne sans modèle » par simulation. Aucun appel, aucun réseau. Usage :
python3 -I -B calcul_pilote_essaim_v1.py SORTIE.json   (refuse d'écraser)"""
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import calcul_devis_essaim_v2 as C  # noqa: E402

BASES_V1 = os.path.join(os.path.dirname(ICI), "essaim-devis-instruments-v1", "bases-sans-modele-v1-sortie.json")
RACINE = 20261123

# Dessin du pilote (PROPOSITION ; les tailles de jetons de la section D, la mesure de Kimi en v67 en variante)
ENTREE = 9000                    # section D, cas attendu
ENTREE_MAX = 20000               # section D, cas haut : borne de ce qui est servi (garde du lanceur à exiger)
SURCROIT_A = C.SURCROIT_ENTREE_A  # SUPPOSÉ (messages relus + tableau partagé) ; aussi pour le carnet relu de (c)
SORTIE_EST = {"conception": 6000, "mesure_v67_kimi": 12800}  # 12 800 : 2 × 6 400 jetons par carte (cité, devis multi v1 l. 29)
MAX_SORTIE_PROPOSEUR = 24000     # PROPOSITION : plafond de jetons de sortie par appel (≈ 1,9 × la mesure de Kimi)
MESSAGE = (3000, 400)            # section D (hypothèse de la conception)
MAX_SORTIE_MESSAGE = 2000        # PROPOSITION
APPELS = {"a": {"proposeur": 24, "message": 12}, "c": {"proposeur": 26, "message": 0}, "b": {"proposeur": 26, "message": 0}}
VARIANTES = {
    "P-min": {"mondes": 8, "bras": ("a", "c"), "generations": 3},
    "P-std": {"mondes": 12, "bras": ("a", "c"), "generations": 3},
    "P-std+b": {"mondes": 12, "bras": ("a", "b", "c"), "generations": 3},
    "P-2gen": {"mondes": 12, "bras": ("a", "c"), "generations": 2},
    "P-24": {"mondes": 24, "bras": ("a", "c"), "generations": 3},
}


def cout_pilote(v, prix, sortie_est, marge, c8):
    g = v["generations"] / 3.0
    est = pire = 0.0
    for b in v["bras"]:
        np_, nm = APPELS[b]["proposeur"] * g, APPELS[b]["message"] * g
        e_in = ENTREE + (SURCROIT_A if b in ("a", "c") else 0)
        est += np_ * (e_in * prix[0] + sortie_est * prix[1]) / 1e6 + nm * (MESSAGE[0] * prix[0] + MESSAGE[1] * prix[1]) / 1e6
        pire += np_ * ((ENTREE_MAX + SURCROIT_A) * prix[0] + MAX_SORTIE_PROPOSEUR * prix[1]) / 1e6 \
            + nm * ((MESSAGE[0] * 2) * prix[0] + MAX_SORTIE_MESSAGE * prix[1]) / 1e6
    return round(est * v["mondes"] * (1 + marge), 2), round(pire * v["mondes"] * (1 + marge) * c8, 2), \
        int(sum(APPELS[b]["proposeur"] + APPELS[b]["message"] for b in v["bras"]) * g * v["mondes"])


def puissance(n, delta, sd, rng, sims=1000, alpha=0.05):
    """Test de permutation par inversion de signe, unilatéral, sur la moyenne des différences appariées par monde."""
    if n <= 16:
        signes = np.array([[1 if (k >> j) & 1 else -1 for j in range(n)] for k in range(2 ** n)], dtype=float)
    else:
        signes = rng.choice([-1.0, 1.0], size=(8192, n))
    rej = 0
    for _ in range(sims):
        d = rng.normal(delta, sd, n)
        obs = d.mean()
        nul = (signes @ d) / n
        p = (np.sum(nul >= obs - 1e-12) + (0 if n <= 16 else 1)) / (len(nul) + (0 if n <= 16 else 1))
        rej += p <= alpha
    return round(rej / sims, 3)


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        return 2
    sha = hashlib.sha256(open(BASES_V1, "rb").read()).hexdigest()
    if sha != open(BASES_V1 + ".sha256").read().split()[0]:
        print("refus : sortie des bases v1 non conforme", file=sys.stderr)
        return 3
    b = json.load(open(BASES_V1, encoding="utf-8"))
    b3 = [b["par_monde"][k]["B3-glouton-borne"]["couverture"] for k in sorted(b["par_monde"], key=int)]
    sd_b3 = float(np.std(b3, ddof=1))
    t_marge, _ = C.lire("devis_affinage_v5")
    marge = C.nombres_affinage(t_marge)["MARGE_AFFINAGE"][0]
    c8 = C.nombres_conception(C.lire("conception")[0])["PLAFOND_C8"][0]
    prix, sources = C.tarifs()
    couts = {}
    for nom, v in VARIANTES.items():
        couts[nom] = {}
        for esp, p in sorted(prix.items()):
            e6, pr, appels = cout_pilote(v, p, SORTIE_EST["conception"], marge, c8)
            e12, _, _ = cout_pilote(v, p, SORTIE_EST["mesure_v67_kimi"], marge, c8)
            couts[nom][esp] = {"estimation_sortie_6000": e6, "estimation_sortie_12800": e12, "pire": pr, "appels": appels}
    ss = np.random.SeedSequence(RACINE)
    taches = ss.spawn(64)
    k = 0
    puiss = {}
    for n in (8, 12, 16, 24):
        for sd in (0.10, 0.15, 0.20, round(math.sqrt(2) * sd_b3, 3)):
            for delta in (0.05, 0.10, 0.15):
                puiss[f"n={n}|sd={sd}|delta={delta}"] = puissance(n, delta, sd, np.random.default_rng(taches[k % 64]))
                k += 1
    out = {"version": "calcul-pilote-essaim-v1", "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "bases_v1": {"chemin": BASES_V1, "sha256": sha, "couverture_B3_par_monde": b3, "mediane": float(np.median(b3)), "ecart_type": round(sd_b3, 4)},
           "graines": f"SeedSequence({RACINE}).spawn(64), une par cellule de puissance (dans l'ordre n, sd, delta)",
           "numpy": np.__version__, "dessin": {"variantes": VARIANTES, "appels_par_monde": APPELS, "entree": ENTREE, "entree_max": ENTREE_MAX,
           "surcroit_entree_suppose": SURCROIT_A, "sortie_estimation": SORTIE_EST, "max_sortie_proposeur": MAX_SORTIE_PROPOSEUR,
           "message": MESSAGE, "max_sortie_message": MAX_SORTIE_MESSAGE, "marge_relances": marge, "plafond_C8": c8,
           "tests_de_mort": 0, "aiguilleur": 0, "juge": "statistique, sans appel"},
           "tarifs": {k2: list(v2) for k2, v2 in prix.items()}, "couts_usd": couts, "puissance_unilaterale_alpha_0_05": puiss}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"b3": out["bases_v1"], "couts": {n: {e: couts[n][e] for e in ("kimi", "claude-1", "fable-5-2", "claude-2")} for n in couts},
                      "puissance": puiss}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
