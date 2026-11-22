#!/usr/bin/env python3
"""Pilote-instrument de l'essaim — calcul v2 : coût (estimation, pire de la v1, **vrai pire sous les gardes du lanceur**) par
espèce et par variante, et puissance du test « (a) bat la base » par simulation. Aucun appel, aucun réseau.

Changements par rapport à `devis-et-instruments-v2/calcul_pilote_essaim_v1.py` (`b3770331…`) :
- R1 : la sortie des bases v1 est lue par un chemin relatif à la racine du dépôt (`racine_depot_v1`), plus aucun
  `../essaim-devis-instruments-v1/` ; prix et marges lus par `calcul_devis_essaim_v3` (contrôle des nombres v3) ;
- R6 : le pire est celui des gardes (`garde_pilote_essaim_v1.borne_pire`, plan gelé appel par appel), borne dure appliquée
  par le lanceur ; le pire de la v1 (204 USD sur Kimi, conditionnel) est rendu à côté, pour comparaison ;
- le nombre d'appels est compté sur le plan (plus de troncature `int`, trouvaille de côté de la vérification) ;
- estimation et puissance : formules et graines de la v1, inchangées (la puissance doit se rejouer à l'identique).
Usage : python -I -B calcul_pilote_essaim_v2.py SORTIE.json   (refuse d'écraser)"""
import hashlib
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import racine_depot_v1 as R  # noqa: E402
import calcul_devis_essaim_v3 as C  # noqa: E402
import garde_pilote_essaim_v1 as GP  # noqa: E402

BASES_V1_SORTIE = "docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/bases-sans-modele-v1-sortie.json"
RACINE_GRAINES = 20261123
ENTREE, ENTREE_MAX = 9000, 20000
SURCROIT_A = C.SURCROIT_ENTREE_A
SORTIE_EST = {"conception": 6000, "mesure_v67_kimi": 12800}
MAX_SORTIE_PROPOSEUR, MESSAGE, MAX_SORTIE_MESSAGE = 24000, (3000, 400), 2000
APPELS = {"a": {"proposeur": 24, "message": 12}, "c": {"proposeur": 26, "message": 0}, "b": {"proposeur": 26, "message": 0}}
VARIANTES = {"P-min": {"mondes": 8, "bras": ("a", "c"), "generations": 3}, "P-std": {"mondes": 12, "bras": ("a", "c"), "generations": 3},
             "P-std+b": {"mondes": 12, "bras": ("a", "b", "c"), "generations": 3}, "P-24": {"mondes": 24, "bras": ("a", "c"), "generations": 3}}


def cout_pilote_v1(v, prix, sortie_est, marge, c8):
    """Formule de la v1, recopiée (estimation et pire « conditionnel » de la v1)."""
    g = v["generations"] / 3.0
    est = pire = 0.0
    for b in v["bras"]:
        np_, nm = APPELS[b]["proposeur"] * g, APPELS[b]["message"] * g
        e_in = ENTREE + (SURCROIT_A if b in ("a", "c") else 0)
        est += np_ * (e_in * prix[0] + sortie_est * prix[1]) / 1e6 + nm * (MESSAGE[0] * prix[0] + MESSAGE[1] * prix[1]) / 1e6
        pire += np_ * ((ENTREE_MAX + SURCROIT_A) * prix[0] + MAX_SORTIE_PROPOSEUR * prix[1]) / 1e6 \
            + nm * ((MESSAGE[0] * 2) * prix[0] + MAX_SORTIE_MESSAGE * prix[1]) / 1e6
    return round(est * v["mondes"] * (1 + marge), 2), round(pire * v["mondes"] * (1 + marge) * c8, 2)


def plan_variante(v):
    bras_garde = tuple("c" if b == "b" else b for b in v["bras"])  # (b) : 26 appels de proposeur, même calendrier que (c)
    plan = []
    for b_reel, b in zip(v["bras"], bras_garde):
        for a in GP.plan_pstd(mondes=v["mondes"], generations=v["generations"], bras=(b,)):
            plan.append(dict(a, bras=b_reel, id=a["id"].replace(f"-{b}-", f"-{b_reel}-", 1)))
    plan.sort(key=lambda a: (a["monde"], v["bras"].index(a["bras"]), a["generation"]))
    return plan


def puissance(n, delta, sd, rng, sims=1000, alpha=0.05):
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
    sha = R.verifier_compagnon(BASES_V1_SORTIE)
    b = json.load(open(R.chemin(BASES_V1_SORTIE), encoding="utf-8"))
    b3 = [b["par_monde"][k]["B3-glouton-borne"]["couverture"] for k in sorted(b["par_monde"], key=int)]
    sd_b3 = float(np.std(b3, ddof=1))
    marge = C.nombres_affinage(C.lire("devis_affinage_v5")[0])["MARGE_AFFINAGE"][0]
    c8 = C.nombres_conception(C.lire("conception")[0])["PLAFOND_C8"][0]
    prix, sources = C.tarifs()
    couts = {}
    for nom, v in VARIANTES.items():
        plan = plan_variante(v)
        couts[nom] = {}
        for esp, p in sorted(prix.items()):
            e6, pire_v1 = cout_pilote_v1(v, p, SORTIE_EST["conception"], marge, c8)
            e12, _ = cout_pilote_v1(v, p, SORTIE_EST["mesure_v67_kimi"], marge, c8)
            bg = GP.borne_pire(plan, p)
            couts[nom][esp] = {"estimation_sortie_6000": e6, "estimation_sortie_12800": e12, "pire_v1_conditionnel": pire_v1,
                               "vrai_pire_sous_gardes": round(bg["pire_usd"], 2), "appels_du_plan": bg["appels_du_plan"],
                               "relances_au_plus": bg["relances_au_plus"], "decomposition_vrai_pire": bg}
    taches = np.random.SeedSequence(RACINE_GRAINES).spawn(64)
    k, puiss = 0, {}
    for n in (8, 12, 16, 24):
        for sd in (0.10, 0.15, 0.20, round(math.sqrt(2) * sd_b3, 3)):
            for delta in (0.05, 0.10, 0.15):
                puiss[f"n={n}|sd={sd}|delta={delta}"] = puissance(n, delta, sd, np.random.default_rng(taches[k % 64]))
                k += 1
    out = {"version": "calcul-pilote-essaim-v2", "script_sha256": R.sha_fichier(os.path.abspath(__file__)),
           "garde_sha256": R.sha_fichier(GP.__file__), "devis_v3_sha256": R.sha_fichier(C.__file__),
           "bases_v1": {"chemin": BASES_V1_SORTIE, "sha256": sha, "couverture_B3_par_monde": b3, "mediane": float(np.median(b3)), "ecart_type": round(sd_b3, 4)},
           "graines": f"SeedSequence({RACINE_GRAINES}).spawn(64), une par cellule de puissance (ordre n, sd, delta), comme la v1",
           "numpy": np.__version__,
           "gardes": {"plafond_sortie": GP.PLAFOND_SORTIE, "plafond_entree_jetons": GP.PLAFOND_ENTREE_JETONS, "plafond_entree_octets": GP.PLAFOND_ENTREE_OCTETS,
                      "surcout_format": GP.SURCOUT_FORMAT, "messages_par_monde": GP.MESSAGES_PAR_MONDE, "part_relances": GP.PART_RELANCES,
                      "hypotheses_de_la_borne": "H1 facture ≤ usage rendu ; H2 sortie ≤ max_tokens, réflexion comprise ; H3 un jeton ≥ un octet (+256) ; H4 appel échoué ≤ sa réserve"},
           "marge_relances": marge, "plafond_C8": c8, "tarifs": {k2: list(v2) for k2, v2 in prix.items()},
           "couts_usd": couts, "puissance_unilaterale_alpha_0_05": puiss}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({n: {e: {kk: couts[n][e][kk] for kk in ("estimation_sortie_6000", "estimation_sortie_12800", "pire_v1_conditionnel", "vrai_pire_sous_gardes", "appels_du_plan")}
                          for e in ("kimi", "claude-1", "fable-5-2", "claude-2")} for n in couts}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
