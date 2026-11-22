#!/usr/bin/env python3
"""Bases sans modèle sur l'information servie aux agents — v1 (« comparaison non équitable » de la vérification de la v2 ;
réponse 14, C.3 : la porte se juge sur les composantes conditionnelles). Aucun appel de modèle, aucun réseau, aucune dépense.

Deux bases, chacune sur la même case que celle servie aux proposeurs (et non sur les 2 000 instances brutes) :
- B3 : recherche gloutonne bornée de `bases_sans_modele_v1.py` (code scellé, importé relogé, inchangé) ;
- B3R : la même plus un niveau de condition (`base_gloutonne_renforcee_v1.py`, dossier inachevé, code importé relogé, inchangé).

Case servie (HYPOTHÈSE déclarée : aucune pièce lue ne fixe le contenu de la case de matière de MR-2) : les k premières instances
(Z, G, Y) des données servies de la v1 (même graine), écrites en lignes « z0,…,z7,g,y », les traits arrondis ; k est le plus
grand nombre de lignes dont le texte tient dans le budget d'octets. Budget = jetons × 3,3 octets par jeton (pièce :
`docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md`, l. 40, `50e7d2f1…`). Les bases reçoivent les
traits **arrondis comme dans la case** : même information, au chiffre près. Variantes, toutes rapportées :
- `case-9000-3d` : 9 000 jetons (entrée d'un proposeur, section D, cas attendu), tout en données, 3 décimales — la plus
  généreuse pour les bases, donc la barre la plus haute ; **variante principale** ;
- `case-6000-3d` : 6 000 jetons de données (3 000 laissés à la consigne, à l'archive et à la grammaire : HYPOTHÈSE), 3 décimales ;
- `case-9000-repr` : 9 000 jetons, nombres écrits en entier (`repr`), comme la tranche `episodes.csv` de v64 ;
- `reference-2000` : les 2 000 instances brutes, non arrondies (contrôle : B3 doit égaler la sortie scellée de la v1).

Mondes : les 12 mondes MR-2 **de développement** (calibration), régénérés par le code scellé. Les 12 mondes neufs du pilote ne
sont ni engendrés ni lus ici.
Barre du pilote (règle écrite avant la course) : par variante, la base la plus forte est celle qui couvre le plus de
composantes conditionnelles, sommées sur les 12 mondes (à égalité : couverture globale moyenne) ; la barre par monde est la
couverture conditionnelle de cette base, choisie sur la calibration et gelée pour les mondes neufs. La couverture globale
et celle des ordinaires sont rapportées à côté.

Usage : python -I -B bases_case_servie_v1.py SORTIE.json [MONDES…]   (refuse d'écraser)
"""
import datetime
import hashlib
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import racine_depot_v1 as R  # noqa: E402

B = R.charger_bases_v1()
RF = R.charger_renforcee_v1()
M = B.M
OCTETS_PAR_JETON = 3.3
PIECE_OCTETS = ("docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md",
                "50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b", 40)
VARIANTES = {"case-9000-3d": (9000, 3), "case-6000-3d": (6000, 3), "case-9000-repr": (9000, None), "reference-2000": (None, None)}
PRINCIPALE = "case-9000-3d"


def lignes_case(Z, G, Y, decimales):
    if decimales is None:
        return [",".join(repr(float(v)) for v in z) + f",{int(g)},{int(y)}" for z, g, y in zip(Z, G, Y)]
    return [",".join(f"{v:.{decimales}f}" for v in z) + f",{int(g)},{int(y)}" for z, g, y in zip(Z, G, Y)]


def case_servie(Z, G, Y, jetons, decimales):
    if jetons is None:
        return (Z, G, Y), {"lignes": len(Y), "octets": None, "jetons_estimes": None}
    budget = int(jetons * OCTETS_PAR_JETON)
    lignes = lignes_case(Z, G, Y, decimales)
    tot, k = 0, 0
    for l in lignes:
        if tot + len(l.encode("utf-8")) + 1 > budget:
            break
        tot += len(l.encode("utf-8")) + 1
        k += 1
    Zk = np.round(Z[:k], decimales) if decimales is not None else Z[:k].copy()
    return (Zk, G[:k].copy(), Y[:k].copy()), {"lignes": k, "octets": tot, "jetons_estimes": round(tot / OCTETS_PAR_JETON),
                                              "empreinte_texte": hashlib.sha256("\n".join(lignes[:k]).encode()).hexdigest()}


def resume_base(m, conds):
    return {"couverture": m["couverture"], "conditionnelles_couvertes": sorted(m["conditionnelles_couvertes"]),
            "conditionnelles": sorted(conds), "ordinaires_couvertes": len(set(m["couvertes"]) - set(conds)),
            "composantes_hors_K1": m["composantes_hors_K1"], "formes_fausses_distinctes": m["formes_fausses_distinctes"],
            "vraies": m["vraies"], "cartes": m["cartes"]}


def courir(r, variantes):
    spec, info = B.regenerer(r)
    oc = B.OracleCache(spec, r)
    Z, G, Y = B.donnees_servies(spec, r)
    out = {}
    for v in variantes:
        jetons, dec = VARIANTES[v]
        don, desc = case_servie(Z, G, Y, jetons, dec)
        b3, _ = B.base_glouton(spec, r, oc, don)
        m3 = B.mesurer(b3, oc, info)
        br, tr = RF.base_glouton_renforcee(spec, oc, don)
        mr = RF.mesurer_plus(br, oc, info, spec, don)
        conds = m3["conditionnelles"]
        out[v] = {"case": desc, "B3": resume_base(m3, conds), "B3R": resume_base(mr, conds),
                  "B3R_conditions_inventees_vraies": mr["conditions_inventees_vraies"],
                  "B3R_candidats_par_generation": [t["candidats"] for t in tr]}
        if v == "reference-2000":
            ref = json.load(open(R.chemin("docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/bases-sans-modele-v1-sortie.json"),
                                 encoding="utf-8"))["par_monde"][str(r)]["B3-glouton-borne"]
            out[v]["B3_egale_sortie_scellee_v1"] = (m3["couvertes"] == ref["couvertes"] and m3["vraies"] == ref["vraies"]
                                                    and m3["formes_fausses_distinctes"] == ref["formes_fausses_distinctes"])
    return out


def agreger(par_monde, v):
    res = {}
    for b in ("B3", "B3R"):
        cv = [par_monde[k][v][b]["couverture"] for k in par_monde]
        cc = sum(len(par_monde[k][v][b]["conditionnelles_couvertes"]) for k in par_monde)
        nc = sum(len(par_monde[k][v][b]["conditionnelles"]) for k in par_monde)
        oc_ = sum(par_monde[k][v][b]["ordinaires_couvertes"] for k in par_monde)
        on = sum(par_monde[k][v][b]["composantes_hors_K1"] - len(par_monde[k][v][b]["conditionnelles"]) for k in par_monde)
        ff = [par_monde[k][v][b]["formes_fausses_distinctes"] for k in par_monde]
        cond_par_monde = [len(par_monde[k][v][b]["conditionnelles_couvertes"]) / max(1, len(par_monde[k][v][b]["conditionnelles"])) for k in par_monde]
        res[b] = {"couverture_globale_mediane": float(np.median(cv)), "couverture_globale_moyenne": round(float(np.mean(cv)), 4),
                  "conditionnelles_couvertes_sur": [cc, nc], "couverture_conditionnelle": round(cc / nc, 4) if nc else None,
                  "couverture_conditionnelle_par_monde": [round(x, 4) for x in cond_par_monde],
                  "ordinaires_couvertes_sur": [oc_, on], "couverture_ordinaire": round(oc_ / on, 4) if on else None,
                  "formes_fausses_distinctes_mediane": float(np.median(ff))}
    cle = lambda b: (res[b]["conditionnelles_couvertes_sur"][0], res[b]["couverture_globale_moyenne"])
    forte = max(("B3", "B3R"), key=cle)
    d01 = d10 = 0
    for k in par_monde:
        for i in par_monde[k][v]["B3"]["conditionnelles"]:
            a, b_ = i in par_monde[k][v]["B3"]["conditionnelles_couvertes"], i in par_monde[k][v]["B3R"]["conditionnelles_couvertes"]
            d01 += (not a) and b_
            d10 += a and not b_
    res["base_la_plus_forte_sur_les_conditionnelles"] = forte
    res["discordances_conditionnelles"] = {"B3R_seule": d01, "B3_seule": d10}
    return res


def main(argv):
    if len(argv) < 2 or os.path.exists(argv[1]):
        print("usage : bases_case_servie_v1.py SORTIE.json [MONDES…] (neuve)", file=sys.stderr)
        return 2
    mondes = [int(x) for x in argv[2:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    s_octets = R.sha_fichier(R.chemin(PIECE_OCTETS[0]))
    if s_octets != PIECE_OCTETS[1]:
        print("refus : pièce des octets par jeton non conforme", file=sys.stderr)
        return 3
    ligne = open(R.chemin(PIECE_OCTETS[0]), encoding="utf-8").read().splitlines()[PIECE_OCTETS[2] - 1]
    if "3,3 octets par jeton" not in ligne:
        print("refus : 3,3 octets par jeton absent de la ligne citée", file=sys.stderr)
        return 3
    par_monde = {}
    for r in mondes:
        par_monde[str(r)] = courir(r, list(VARIANTES))
        print(r, {v: (x["case"]["lignes"], x["B3"]["couverture"], len(x["B3"]["conditionnelles_couvertes"]), x["B3R"]["couverture"],
                      len(x["B3R"]["conditionnelles_couvertes"]), len(x["B3"]["conditionnelles"])) for v, x in par_monde[str(r)].items()}, flush=True)
    resume = {v: agreger(par_monde, v) for v in VARIANTES}
    resume["controle_B3_reference_egale_v1_scellee"] = all(par_monde[k]["reference-2000"]["B3_egale_sortie_scellee_v1"] for k in par_monde)
    resume["variante_principale"] = PRINCIPALE
    out = {"version": "bases-case-servie-v1", "debut_utc": debut, "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": R.sha_fichier(os.path.abspath(__file__)), "racine_sha256": R.sha_fichier(R.__file__),
           "bases_v1": {"chemin": R.BASES_V1_REL, "sha256_scellee": B.SHA_SOURCE_SCELLEE, "sha256_relogee": B.SHA_SOURCE_RELOGEE},
           "renforcee_v1": {"chemin": R.RENF_REL, "sha256_scellee": RF.SHA_SOURCE_SCELLEE, "sha256_relogee": RF.SHA_SOURCE_RELOGEE},
           "imports_sha256": B.IMPORTS, "python": sys.version.split()[0], "numpy": np.__version__,
           "octets_par_jeton": {"valeur": OCTETS_PAR_JETON, "piece": PIECE_OCTETS[0], "sha256": s_octets, "ligne": PIECE_OCTETS[2]},
           "variantes": {k: {"jetons": a, "decimales": b} for k, (a, b) in VARIANTES.items()},
           "graines": "données servies : SeedSequence(20261122, spawn_key=(0, monde)) de la v1 ; mondes et oracle : graines de la v4 ; recherche déterministe",
           "mondes": mondes, "mondes_nature": "12 mondes MR-2 de développement (calibration) ; aucun monde neuf du pilote",
           "resume": resume, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
