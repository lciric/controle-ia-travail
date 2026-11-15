"""Essai de taille — projection d'information inverse (numéraire) — v1.

Pour chaque cas (monde, carte) : R mondes simulés ; pour chaque méthode, part des mondes où la carte est promue au niveau
du juge (alpha = 0,05, lecture aux 8 instants de T ; M4 : seuil de Bonferroni log(8/alpha)), intervalle de
Clopper-Pearson bilatéral à 95 %. Les deux façons des fiches (A1 en ligne, A2 moitié) sont l'artefact obligatoire.
Usage : python -I essai_projection_taille_v1.py CAS R_DEBUT R_FIN PROCESSUS SORTIE.json (les tranches d'un cas se fusionnent par
essai_projection_fusion_v1.py)
Graines : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(indice du cas, r)) ; écrites dans la sortie."""
import json
import math
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

RACINE = 2026111509
CAS = ["T01_copie_membre_lineaire", "T02_bord_une_loi_connue", "T03_poids_extremes", "T04_bord_loi_aveugle_constante",
       "T05_copie_coupure_archive", "T06_copie_coupure_hors_archive", "T07_copie_sous_population",
       "T08_copie_coupure_archive_bruit_commun", "T09_copie_deux_niveaux_archive", "T10_monde_coupure_carte_neuve",
       "T11_monde_lineaire_carte_surconfiante", "T12_monde_coupure_carte_autre_membre"]
F4 = {"T01", "T02", "T03", "T04", "T05", "T08", "T09", "T10", "T11", "T12"}
CLASSE = {   # cas dont le MONDE est dans la classe couverte par la méthode (sinon : trou, mesuré)
    "M1_lin": {"T01", "T02", "T03", "T04", "T11"},
    "M2_f4_commun": F4, "M4_f4_horizon_fixe_bonferroni": F4, "M9_fraction_prevue_f4": F4,
    "M2b_min_lin_A_B": {"T01", "T02", "T03", "T04", "T05", "T08", "T10", "T11", "T12"},
    "M3_toutes_coupures": {"T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08", "T10", "T11", "T12"},
    "M5_pas_a_pas_avec_bruit": set(c[:3] for c in CAS),
    "M6_pas_a_pas_enveloppe_et_M1": {"T01", "T02", "T03", "T04", "T05", "T06", "T07", "T09", "T10", "T11", "T12"},
    "M2c_f4_cellule": F4, "M7_appris_passe_certifie": F4, "M7b_appris_lisse_certifie": F4, "M8_moitie_certifiee": F4,
    "A1_en_ligne_eta0.05": F4, "A1_en_ligne_eta0.2": F4, "A2_moitie_fin": F4, "A2_moitie_instants": F4,
}


def un_monde(args):
    i_cas, r = args
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(i_cas, r)))
    m = cs.construire(rng, CAS[i_cas])
    res, temps, diag = {}, {}, {}

    def lance(nom, f, seuil=cm.SEUIL, sel=slice(None)):
        t0 = time.process_time()
        w = np.asarray(f())
        temps[nom] = time.process_time() - t0
        res[nom] = (bool(np.max(w[sel]) >= seuil), float(np.max(w[sel])), bool(np.all(np.isfinite(w))))

    lance("M1_lin", lambda: me.m1_lin(m))
    lance("M2_f4_commun", lambda: me.m2_f4(m, diag))
    lance("M2b_min_lin_A_B", lambda: me.m2b_min_lin_A_B(m))
    lance("M3_toutes_coupures", lambda: me.m3_toutes_coupures(m, diag))
    lance("M4_f4_horizon_fixe_bonferroni", lambda: me.m4_f4_horizon_fixe(m), seuil=me.SEUIL_BONFERRONI)
    lance("M5_pas_a_pas_avec_bruit", lambda: me.m5_pas_a_pas_avec_bruit(m))
    lance("M6_pas_a_pas_enveloppe_et_M1", lambda: me.m6_pas_a_pas_enveloppe(m, diag))
    lance("M2c_f4_cellule", lambda: me.m2c_f4_cellule(m, diag))
    lance("M7_appris_passe_certifie", lambda: me.m7_en_ligne_certifie(m))
    lance("M7b_appris_lisse_certifie", lambda: me.m7b_en_ligne_lisse_certifie(m))
    lance("M8_moitie_certifiee", lambda: me.m8_moitie_certifiee(m))
    lance("M9_fraction_prevue_f4", lambda: me.m9_fraction_prevue(m))
    lance("A1_en_ligne_eta0.05", lambda: me.a1_en_ligne(m, 0.05))
    lance("A1_en_ligne_eta0.2", lambda: me.a1_en_ligne(m, 0.2))
    a2 = me.a2_moitie(m)
    lance("A2_moitie_fin", lambda: a2, sel=slice(7, 8))
    lance("A2_moitie_instants", lambda: a2, sel=slice(4, 8))
    cert = {k: float(np.max(v)) for k, v in diag.items()}
    return res, temps, cert


def main():
    nom_cas, r0, r1, proc, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    R = r1 - r0
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, aucun écrasement : {sortie}")
    i_cas = CAS.index(nom_cas)
    t0 = time.time()
    with Pool(proc) as pool:
        tous = pool.map(un_monde, [(i_cas, r) for r in range(r0, r1)], chunksize=10)
    duree = time.time() - t0
    methodes = {}
    for nom in tous[0][0]:
        k = sum(t[0][nom][0] for t in tous)
        mx = [t[0][nom][1] for t in tous]
        methodes[nom] = {"monde_dans_la_classe": nom_cas[:3] in CLASSE[nom], "promues": k, "mondes": R,
                         "taux": round(k / R, 4), "clopper_pearson_95": cm.clopper_pearson(k, R),
                         "log_w_max_mediane": round(float(np.median(mx)), 4), "log_w_max_maximum": round(float(np.max(mx)), 4),
                         "valeurs_non_finies": sum(not t[0][nom][2] for t in tous),
                         "temps_processeur_moyen_s": round(float(np.mean([t[1][nom] for t in tous])), 4)}
    cert = {}
    for t in tous:
        for k, v in t[2].items():
            cert.setdefault(k, []).append(v)
    sortie_json = {
        "essai": "taille", "cas": nom_cas, "indice_cas": i_cas, "mondes": R, "r_debut": r0, "r_fin": r1,
        "graines": {"racine": RACINE, "derivation": "numpy.random.SeedSequence(entropy=racine, spawn_key=(indice_cas, r)), r = r_debut..r_fin-1"},
        "niveau": {"alpha": cm.ALPHA, "instants": cm.T.tolist(), "seuil_log": cm.SEUIL, "seuil_log_bonferroni_M4": me.SEUIL_BONFERRONI},
        "reglages": {"IT_PROJ": me.IT_PROJ, "IT_CHAUD": me.IT_CHAUD, "IT_MV": me.IT_MV},
        "methodes": methodes,
        "certificats_c_moins_1_maximum_par_monde": {k: {"mediane": float(np.median(v)), "maximum": float(np.max(v))} for k, v in cert.items()},
        "duree_murale_s": round(duree, 1), "processus": proc,
        "versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    sortie_json["par_monde"] = {nom: [[int(t[0][nom][0]), round(t[0][nom][1], 4)] for t in tous] for nom in tous[0][0]}
    with open(sortie, "w") as f:
        json.dump(sortie_json, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: (v["promues"], v["taux"], v["monde_dans_la_classe"]) for k, v in methodes.items()}, ensure_ascii=False))
    print("durée", round(duree, 1), "s")


if __name__ == "__main__":
    main()
