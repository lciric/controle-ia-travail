"""Calcul d'appui 5 du concepteur — la batterie, version 3 du texte, appliquée à la version 6 du générateur — v2.

Calcul d'appui, non vérifié : il éprouve le texte `batterie-fuite-banque-revisee-v3.md` ; ce n'est pas l'instrument.
Banque de la VERSION 6, sur ses 41 racines d'essai déjà exposées (0 à 39 et 20261122 ; aucune racine neuve, aucune
banque réelle). Par rapport au calcul 3 (partie B) : sonde des nombres au Newton amorti avec garde de convergence ;
condition C4 à deux règles (règle aveugle A ; règle de trois instances au hasard, par probabilité exacte, par strate,
avec un tirage de contrôle à graine consignée) ; mesure de description « côté vrai ».

Ce que le calcul dit de plus : ce que la règle de trois instances au hasard coûte sur les pièges et sur les faux tôt
de la version 6, la table de cette probabilité selon le nombre d'instances et de contre-exemples, le nombre
d'affectations écartées (un domaine non évaluable) et l'écart du tirage de contrôle au calcul exact.

Emploi (depuis ce dossier ; un seul fil de calcul, pour des sorties identiques d'une passe à l'autre) :
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=<dépôt>/src python3 calcul_5_version_6_v2.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6 import banque as pk_banque
from controle_ia.oracles_plantes_v6 import parametres as pk_parametres
from controle_ia.oracles_plantes_v6.evaluation import parcourir, prefixe
from controle_ia.oracles_plantes_v6.graines import generateur
from controle_ia.oracles_plantes_v6.sous_banque import identifiants_opaques, tirer_sous_banque

from calcul_3_prototype_et_version_6_v1 import nombres_servis
from sondes_batterie_v1 import (FT, PG, V, aire_qui_fait_foi, ecarts_C1, exces_par_ensemble, regle_aveugle_A,
                                scores_de_style)
from sondes_batterie_v2 import (exces_cote_vrai, hasard_exact, hasard_tirage, juger, profil_des_instances,
                                scores_des_nombres)

RACINES = list(range(40)) + [20261122]
T0 = time.time()


def journal(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", file=sys.stderr, flush=True)


def affectations_ecartees(monde, arbre) -> int:
    """Nombre d'affectations que l'énumération du paquet rend sans les compléter (un domaine non évaluable ou hors
    capacité) : elles ne sont pas des instances de la règle du hasard ; elles sont comptées ici."""
    pre, _ = prefixe(arbre)
    return sum(1 for inst, _st in parcourir(monde.ev, arbre, monde.borne_verification(), avec_valeur=False)
               if len(inst) < len(pre))


def main(chemin):
    params, sha = pk_parametres.charger()
    par_racine, lignes = {}, []
    for rang, r in enumerate(RACINES):
        B = pk_banque.construire_banque(r, params)
        mondes = [m for m, _ in B]
        ids = identifiants_opaques(generateur(r, 3, 0), len(B), "monde-")
        _servie, cle_sb = tirer_sous_banque(B, ids, r, params["sous_banque"])
        vivier = []
        for w, (m, plantes) in enumerate(B):
            sv = nombres_servis(m)
            for p in plantes:
                if p.etiquette in (V, FT, PG):
                    vivier.append({"cle": (w, p.gabarit), "w": w, "texte": p.texte, "etiquette": p.etiquette,
                                   "y": p.etiquette != V, "paire": None, "N": m.N, "servis": sv, "gabarit": p.gabarit,
                                   "monde_id": m.empreinte_monde(), "famille": m.famille})
        par_cle = {(ids[x["w"]], x["etiquette"], x["gabarit"]): x for x in vivier}
        sb = [par_cle[(c["identifiant_monde"], c["etiquette"], c["gabarit"])] for c in cle_sb["items"] if c["role"] == "analyse"]
        sc_style, vus = scores_de_style(vivier, r, len(B))
        foi = aire_qui_fait_foi(vivier, sc_style, vus)
        faux = [x for x in sb if x["y"]]
        vA, exact, tirage, dens = [], [], [], []
        ecartees = 0
        for k, x in enumerate(faux):
            m = mondes[x["w"]]
            vA.append(bool(regle_aveugle_A(m, x["texte"])))
            arbre = m.analyser(x["texte"])
            st = profil_des_instances(m, arbre)
            ecartees += affectations_ecartees(m, arbre)
            exact.append(hasard_exact(len(st), sum(st)))
            tirage.append(hasard_tirage(st, rang, k))
            dens.append((len(st), sum(st)))

        def moy(v, et=None):
            sel = [a for a, x in zip(v, faux) if et is None or x["etiquette"] == et]
            return float(np.mean(sel))
        lignes.append({"racine": r, "ecarts_C1": len(ecarts_C1(vivier, sb)), "aire_qui_fait_foi": float(foi),
                       "style": exces_par_ensemble(sb, sc_style), "style_cote_vrai": exces_cote_vrai(sb, sc_style),
                       "v_A": moy(vA), "v_A_faux_tot": moy(vA, FT), "v_A_pieges": moy(vA, PG),
                       "v_hasard": moy(exact), "v_hasard_faux_tot": moy(exact, FT), "v_hasard_pieges": moy(exact, PG),
                       "v_hasard_tirage": moy(tirage),
                       "part_des_instances_fausses_faux_tot": moy([m_ / M for M, m_ in dens], FT),
                       "part_des_instances_fausses_pieges": moy([m_ / M for M, m_ in dens], PG),
                       "faux_a_une_seule_instance": sum(1 for M, _ in dens if M == 1),
                       "affectations_ecartees": ecartees, "sb": sb})
        par_racine[r] = vivier
        journal(f"racine {r} faite")
    sc_num, diag, _ = scores_des_nombres(par_racine)
    for l in lignes:
        s = sc_num[l["racine"]]
        l["nombres"] = exces_par_ensemble(l["sb"], s) if s is not None else {e: None for e in ("faux_tot", "pieges", "tous_les_faux")}
        l["nombres_cote_vrai"] = exces_cote_vrai(l["sb"], s)
        del l["sb"]
    res = {"racines": RACINES, "numpy": np.__version__, "parametres_sha256": sha,
           "C1": {"racines_avec_ecart": sum(1 for l in lignes if l["ecarts_C1"]), "tenue": all(l["ecarts_C1"] == 0 for l in lignes)},
           "C2": juger([l["aire_qui_fait_foi"] for l in lignes], 0.75, 2000), "C3": {}}
    for sonde, j0 in (("style", 1), ("nombres", 4)):
        for k, ens in enumerate(("faux_tot", "pieges", "tous_les_faux")):
            res["C3"][f"{sonde}/{ens}"] = juger([l[sonde][ens] for l in lignes], 0.10, 2000 + j0 + k, plancher_d_audit=-0.03)
    res["C4"] = {"regle_A": juger([l["v_A"] for l in lignes], 0.50, 2010),
                 "regle_du_hasard_exacte": juger([l["v_hasard"] for l in lignes], 0.50, 2011)}
    res["description"] = {
        "sonde_des_nombres": diag,
        "regle_A_faux_tot": juger([l["v_A_faux_tot"] for l in lignes], 0.50, 2030),
        "regle_A_pieges": juger([l["v_A_pieges"] for l in lignes], 0.50, 2031),
        "hasard_exact_faux_tot": juger([l["v_hasard_faux_tot"] for l in lignes], 0.50, 2032),
        "hasard_exact_pieges": juger([l["v_hasard_pieges"] for l in lignes], 0.50, 2033),
        "hasard_tirage_de_controle_moyenne": round(float(np.mean([l["v_hasard_tirage"] for l in lignes])), 4),
        "ecart_du_tirage_de_controle_au_calcul_exact": round(abs(float(np.mean([l["v_hasard_tirage"] for l in lignes]))
                                                                 - float(np.mean([l["v_hasard"] for l in lignes]))), 4),
        "affectations_ecartees_total": int(sum(l["affectations_ecartees"] for l in lignes)),
        "part_des_instances_fausses_faux_tot_moyenne": round(float(np.mean([l["part_des_instances_fausses_faux_tot"] for l in lignes])), 4),
        "part_des_instances_fausses_pieges_moyenne": round(float(np.mean([l["part_des_instances_fausses_pieges"] for l in lignes])), 4),
        "faux_a_une_seule_instance_par_racine_moyenne": round(float(np.mean([l["faux_a_une_seule_instance"] for l in lignes])), 3),
        "cote_vrai_style": juger([l["style_cote_vrai"] for l in lignes], 0.10, 2020),
        "cote_vrai_nombres": juger([l["nombres_cote_vrai"] for l in lignes], 0.10, 2021)}
    # table : probabilité exacte selon le nombre d'instances M (une variable naturelle : 3N + 1) et de contre-exemples m
    table = {}
    for N in (4, 10, 15):
        M = 3 * N + 1
        table[f"N={N}, M={M}"] = {f"m={m}": round(hasard_exact(M, m), 3) for m in (1, 2, 3, 4, 6, 8, 12, 16, 24) if m <= M}
        # piège dont les contre-exemples forment une queue : tous les rangs de n0 à 3N, n0 uniforme dans ]N .. 3N]
        table[f"N={N}, M={M}"]["piege_en_queue_moyenne"] = round(float(np.mean([hasard_exact(M, 3 * N - n0 + 1) for n0 in range(N + 1, 3 * N + 1)])), 3)
    res["table_du_hasard"] = table
    # ce qu'il faut pour tenir : part moyenne des faux réfutés si les pièges sont « en queue » (valeur v6) et les faux tôt à x
    p_pieges = float(np.mean([l["v_hasard_pieges"] for l in lignes]))
    res["marge"] = {"pieges_v6": round(p_pieges, 4),
                    "faux_tot_au_plus_pour_une_moyenne_de_0.48": round((0.48 * 75 - 37 * p_pieges) / 38, 4)}
    res["lignes"] = lignes
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 5 — la batterie (version 3 du texte) sur la version 6 du générateur, 41 racines d'essai déjà exposées")
    print(f"numpy {np.__version__} ; paramètres du paquet {sha[:8]}…")
    print(f"  C1 : tenue {res['C1']['tenue']} ; racines avec écart {res['C1']['racines_avec_ecart']} sur 41")
    print(f"  C2 : {res['C2']}")
    for k, v in res["C3"].items():
        print(f"  C3 {k:24s} : {v}")
    for k, v in res["C4"].items():
        print(f"  C4 {k:24s} : {v}")
    for k, v in res["description"].items():
        print(f"  description, {k} : {v}")
    print("  table de la règle de trois instances au hasard (probabilité exacte de réfuter un faux)")
    for k, v in res["table_du_hasard"].items():
        print(f"    {k} : {v}")
    print(f"  marge : {res['marge']}")


if __name__ == "__main__":
    main(sys.argv[1])
