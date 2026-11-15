"""Essai de puissance — projection d'information inverse (numéraire) — v1.

Vraies découvertes (une composante neuve, trois doses) ; carte = monde ; mêmes tirages et mêmes instants pour tous les
bras. Références (maximum de vraisemblance sur les tirages mêmes, valeur ATTEINTE par l'EM, donc plus favorable aux
références que leur certificat) : R8 (membre linéaire du v8), RLa (nul limité aux coupures de l'archive : linéaire, A, B),
RF4 (partition à 4 cellules de l'archive), R9 (façon nul v9 : linéaire, sous-population, toutes les coupures des deux
traits). Méthodes : celles de essai_projection_methodes_v1.py.
Usage : python -I essai_projection_puissance_v1.py CAS DOSE R_DEBUT R_FIN PROCESSUS SORTIE.json
Graines : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(indice du cas, indice de dose, r))."""
import json
import os
import platform
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np

import essai_projection_cas_v1 as cs
import essai_projection_commun_v1 as cm
import essai_projection_methodes_v1 as me

RACINE = 2026111510
CAS = {"V1_effet_neuf_global": (0.25, 0.5, 0.75), "V4_loi_neuve_sous_population": (0.1, 0.2, 0.3),
       "V3_conditionnelle_seuil_decentre": (0.4, 0.8, 1.2)}
NOMS = list(CAS)


def un_monde(args):
    i_cas, i_dose, r = args
    nom = NOMS[i_cas]
    dose = CAS[nom][i_dose]
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(i_cas, i_dose, r)))
    m = cs.construire(rng, (nom, dose))
    res, temps = {}, {}

    def note(n, w, dt, seuil=cm.SEUIL):
        w = np.asarray(w)
        res[n] = (bool(np.max(w) >= seuil), float(np.max(w)))
        temps[n] = dt

    t0 = time.process_time(); refs = me.references(m); dt = time.process_time() - t0
    for k, w in refs.items():
        note(k, w, dt / len(refs))
    bras = [("M1_lin", lambda: me.m1_lin(m)), ("M2_f4_commun", lambda: me.m2_f4(m)),
            ("M2b_min_lin_A_B", lambda: me.m2b_min_lin_A_B(m)), ("M3_toutes_coupures", lambda: me.m3_toutes_coupures(m)),
            ("M5_pas_a_pas_avec_bruit", lambda: me.m5_pas_a_pas_avec_bruit(m)),
            ("M6_pas_a_pas_enveloppe_et_M1", lambda: me.m6_pas_a_pas_enveloppe(m)),
            ("M2c_f4_cellule", lambda: me.m2c_f4_cellule(m)), ("M7_appris_passe_certifie", lambda: me.m7_en_ligne_certifie(m)),
            ("M7b_appris_lisse_certifie", lambda: me.m7b_en_ligne_lisse_certifie(m)),
            ("M8_moitie_certifiee", lambda: me.m8_moitie_certifiee(m)), ("M9_fraction_prevue_f4", lambda: me.m9_fraction_prevue(m))]
    for n, f in bras:
        t0 = time.process_time(); w = f(); note(n, w, time.process_time() - t0)
    t0 = time.process_time(); w = me.m4_f4_horizon_fixe(m)
    note("M4_f4_horizon_fixe_bonferroni", w, time.process_time() - t0, seuil=me.SEUIL_BONFERRONI)
    return res, temps


def apparie(a, b):
    """Différence appariée taux(a) − taux(b), comptes discordants, intervalle de Wald à 95 % de la différence."""
    a, b = np.asarray(a, int), np.asarray(b, int)
    n = len(a)
    n10, n01 = int(((a == 1) & (b == 0)).sum()), int(((a == 0) & (b == 1)).sum())
    d = (n10 - n01) / n
    var = max(((n10 + n01) / n - d * d) / n, 0.0)
    return {"difference": round(d, 4), "a_seul": n10, "b_seul": n01,
            "wald_95": [round(d - 1.96 * var ** 0.5, 4), round(d + 1.96 * var ** 0.5, 4)]}


def main():
    nom, i_dose, r0, r1, proc, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, aucun écrasement : {sortie}")
    i_cas = NOMS.index(nom)
    t0 = time.time()
    with Pool(proc) as pool:
        tous = pool.map(un_monde, [(i_cas, i_dose, r) for r in range(r0, r1)], chunksize=5)
    duree = time.time() - t0
    R = r1 - r0
    bras = {}
    for n in tous[0][0]:
        k = sum(t[0][n][0] for t in tous)
        bras[n] = {"promues": k, "mondes": R, "taux": round(k / R, 4), "clopper_pearson_95": cm.clopper_pearson(k, R),
                   "log_w_max_mediane": round(float(np.median([t[0][n][1] for t in tous])), 4),
                   "temps_processeur_moyen_s": round(float(np.mean([t[1][n] for t in tous])), 4)}
    prom = {n: [t[0][n][0] for t in tous] for n in tous[0][0]}
    comp = {f"{n}_contre_{ref}": apparie(prom[n], prom[ref]) for n in prom if n[0] == "M" for ref in ("R9", "RLa", "R8")}
    sortie_json = {
        "essai": "puissance", "cas": nom, "dose": CAS[nom][i_dose], "indice_cas": i_cas, "indice_dose": i_dose,
        "mondes": R, "r_debut": r0, "r_fin": r1,
        "graines": {"racine": RACINE, "derivation": "numpy.random.SeedSequence(entropy=racine, spawn_key=(indice_cas, indice_dose, r))"},
        "niveau": {"alpha": cm.ALPHA, "instants": cm.T.tolist(), "seuil_log": cm.SEUIL, "seuil_log_bonferroni_M4": me.SEUIL_BONFERRONI},
        "reglages": {"IT_PROJ": me.IT_PROJ, "IT_CHAUD": me.IT_CHAUD, "IT_MV": me.IT_MV,
                     "references": "valeur atteinte par l'EM (borne basse du maximum : plus favorable aux références)"},
        "bras": bras, "comparaisons_appariees": comp, "par_monde": {n: [int(x) for x in v] for n, v in prom.items()},
        "duree_murale_s": round(duree, 1), "processus": proc,
        "versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    with open(sortie, "w") as f:
        json.dump(sortie_json, f, ensure_ascii=False, indent=1)
    print(json.dumps({n: v["taux"] for n, v in bras.items()}, ensure_ascii=False))
    print("durée", round(duree, 1), "s")


if __name__ == "__main__":
    main()
