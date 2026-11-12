"""Calculs hors ligne v2 de la conception « monde riche et doublons » (corrections E-1, E-2, E-3, E-4 de la contre-lecture
`e7d5cda0…`). N'écrase rien de la v1 ; importe `../outils-v1/` tel quel.

Changements : **mondes tirés de la famille** (générateur v2 : gabarits tirés, trait latent possible ; E-4) au lieu du gabarit
fixe de la v1 ; **règle de représentant v2** et regroupement stratifié (E-1) ; **parcours déterministes** (ensembles triés,
lanceur à `PYTHONHASHSEED=0` en plus ; E-2) ; m = 44 (décompte du dessin : 24 cartes, 13 vraies plantées au plus, 4 fausses,
4 copies, T-ELIM ; E-3) ; puissance selon la taille de l'archive (E-3).

Sous-commandes : representant, doublons, detection, attribution, archive, generations. Juge simplifié de la v1 (étalonné) :
tous les chiffres sont des estimations de conception, à refaire au banc de calibration avec le code v68 gelé.
"""

import argparse
import datetime
import hashlib
import json
import math
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(os.path.dirname(ICI), "outils-v1")
for p in (V1, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import generateur_mondes_v2 as G  # noqa: E402
import monde_riche_outils_v1 as M  # noqa: E402
import monde_riche_outils_v2 as M2  # noqa: E402
import puissance_monde_riche_v1 as P1  # noqa: E402

VERSION = "puissance-monde-riche-v2"
M_DESSIN = 44
rng_de, part, cle = P1.rng_de, P1.part, P1.cle
UNIFORME = P1.UNIFORME


def preparer_monde_v2(w):
    spec = G.generer_monde_v2(cle("monde-mr1-v2", w))
    loi = M.compiler_monde(spec)
    o = M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=12000, graine=cle("oracle", w))
    k1, eid_k1, infos = M.k1_du_monde(spec, o)
    cibles = {e["id"]: (e["classe"], None) for e in spec["effets"]}
    return spec, cibles, loi, o, k1, eid_k1, infos


P1.preparer_monde = preparer_monde_v2  # détection et attribution de la v1, sur la famille tirée


def gabarit_de(spec):
    return [(e["classe"], e["type"]) for e in spec["effets"]]


# --- représentant : le cas de la contre-lecture (E-1) ---------------------------------------------------------------------

def _representant_monde(w):
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    ids = [e["id"] for e in spec["effets"]]
    fortes = sorted(i for i in ids if cibles[i][0] == "forte")
    moy = sorted(i for i in ids if cibles[i][0] == "moyenne")
    L = M.monde_restreint(spec, fortes + moy[:1])
    var = {"loi": L,
           "diluee-0.5": {"type": "melange", "composantes": [L, UNIFORME], "poids": [0.5, 0.5]},
           "diluee-0.2": {"type": "melange", "composantes": [L, UNIFORME], "poids": [0.2, 0.8]},
           "diluee-0.05": {"type": "melange", "composantes": [L, UNIFORME], "poids": [0.05, 0.95]},
           "temperee-0.3": {"type": "transformee", "base": L, "puissance": 0.3},
           "temperee-2.0": {"type": "transformee", "base": L, "puissance": 2.0}}
    noms = sorted(var)
    lois = [var[n] for n in noms]
    gains = [o.gain(l) for l in lois]
    Zref, Gref = M.tirer_instances(rng_de("rep-ref", w), 2000, D, nsp)
    mats = M2.matrices(lois, Zref, Gref, nsp)
    choix = lambda i: M.test_de_mort(lois[i], loi, D, nsp, rng_de("rep-choix", w, i))[0]  # noqa: E731
    out = {"monde": w, "gains": {n: round(g, 4) for n, g in zip(noms, gains)}, "cas": []}

    def un_cas(nom_cas, membres):
        gs, (dg, ds, can) = M2.grouper_v2([lois[i] for i in membres], Zref, Gref, nsp,
                                          mats=(mats[0][np.ix_(membres, membres)], mats[1][np.ix_(membres, membres)],
                                                [mats[2][i] for i in membres]))
        for g in gs:
            if len(g) < 2:
                continue
            gm = [membres[i] for i in g]
            best = max(gains[i] for i in gm)
            d_sym = np.minimum(dg, dg.T)
            r1 = membres[M2.medoide_v1(g, d_sym, can)]
            r2, info = M2.representant_v2(g, dg, can, statistique_de_choix=lambda i: choix(membres[i]))
            r2 = membres[r2]
            out["cas"].append({"cas": nom_cas, "membres": [noms[i] for i in gm], "meilleur_gain": round(best, 4),
                               "medoide_v1": noms[r1], "perte_v1": round(best - gains[r1], 4),
                               "regle_v2": noms[r2], "perte_v2": round(best - gains[r2], 4), "departage_v2": info["departage"],
                               "v1_sous_g0_meilleur_au_dessus": bool(gains[r1] < 0.02 <= best),
                               "v2_sous_g0_meilleur_au_dessus": bool(gains[r2] < 0.02 <= best)})

    un_cas("six-variantes", list(range(len(noms))))
    i_loi = noms.index("loi")
    for j in range(len(noms)):
        if j != i_loi:
            un_cas(f"paire-loi+{noms[j]}", [i_loi, j])
    return out


def representant(W, proc):
    with ProcessPoolExecutor(proc) as ex:
        mondes = list(ex.map(_representant_monde, range(W), chunksize=1))
    cas = [c for m in mondes for c in m["cas"]]
    res = {"groupes_regroupes": len(cas)}
    for r in ("v1", "v2"):
        pertes = [c[f"perte_{r}"] for c in cas]
        res[r] = {"perte_max": round(max(pertes), 4), "perte_mediane": round(float(np.median(pertes)), 4),
                  "groupes_perte_sup_0.01": sum(p > 0.01 for p in pertes),
                  "representant_sous_g0_alors_que_le_meilleur_au_dessus": sum(c[f"{r}_sous_g0_meilleur_au_dessus"] for c in cas)}
    res["departages_v2"] = {k: sum(c["departage_v2"] == k for c in cas) for k in ("couverture", "tranche de choix", "empreinte")}
    return {"resume": res, "mondes": mondes}


# --- doublons sur la famille tirée -------------------------------------------------------------------------------------------

def _doublons_monde_v2(w):
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    rng = rng_de("doublons-v2", w)
    Zref, Gref = M.tirer_instances(rng_de("doublons-ref", w), 2000, D, nsp)
    ids = [e["id"] for e in spec["effets"]]
    fortes = sorted(i for i in ids if cibles[i][0] == "forte")
    moy = sorted(i for i in ids if cibles[i][0] == "moyenne")
    faibles = sorted(i for i in ids if cibles[i][0] == "faible")
    base_S = sorted(set(fortes) | {moy[0]})
    base = M.monde_restreint(spec, base_S)
    paires = []
    for s in (0.05, 0.1, 0.2, 0.3):
        paires.append((f"variante-sigma-{s}", base, P1._bruiter(spec, base_S, s, rng), True))
    paires.append(("reformulation", base, P1._reformuler(base), True))
    paires.append(("temperee-1.2", base, {"type": "transformee", "base": base, "puissance": 1.2}, True))
    paires.append(("melee-0.8-uniforme", base, {"type": "melange", "composantes": [base, UNIFORME], "poids": [0.8, 0.2]}, True))
    paires.append(("distincte-moyenne", base, M.monde_restreint(spec, sorted(set(fortes) | {moy[1]})), False))
    paires.append(("ajout-faible", base, M.monde_restreint(spec, sorted(set(base_S) | {faibles[0]})), False))
    paires.append(("ajout-moyenne", base, M.monde_restreint(spec, sorted(set(base_S) | {moy[1]})), False))
    out = {"monde": w, "gabarit": gabarit_de(spec), "paires": {}}
    for cat, a, b, doit in paires:
        gs, _ = M2.grouper_v2([a, b], Zref, Gref, nsp)
        out["paires"][cat] = {"doit_regrouper": doit, "regroupe": len(gs) == 1, "gain_b_moins_a": round(o.gain(b) - o.gain(a), 5)}
    idees = [base_S, sorted(set(fortes) | {moy[1]}), sorted({fortes[0]} | set(faibles[:2]))]
    cartes, verite = [], []
    for k, S in enumerate(idees):
        for v in range(6):
            cartes.append(P1._bruiter(spec, S, 0.15, rng))
            verite.append(f"idee-{k}")
    for v in range(6):
        S = sorted(set(rng.choice(ids, size=int(rng.integers(2, 5)), replace=False).tolist()))
        cartes.append(P1._bruiter(spec, S, 0.15, rng))
        verite.append("|".join(S))
    gs, (dg, ds, can) = M2.grouper_v2(cartes, Zref, Gref, nsp)
    seuil = math.log(M_DESSIN / M.ALPHA)
    les = {i: M.log_e_arrete(M.juger(c, [k1], loi, D, nsp, rng_de("doublons-juge", w, i), n=400)["traj"], seuil)
           for i, c in enumerate(cartes)}
    r_cartes = M.e_bh(les, M_DESSIN)
    les_g = {gi: M.log_e_groupe([les[i] for i in g]) for gi, g in enumerate(gs)}
    r_groupes = M.e_bh(les_g, M_DESSIN)
    reps = [gs[g][0] if len(gs[g]) == 1 else M2.representant_v2(
        gs[g], dg, can, statistique_de_choix=lambda i: M.test_de_mort(cartes[i], loi, D, nsp, rng_de("doublons-choix", w, i))[0])[0]
        for g in r_groupes]
    out["generation_24"] = {"groupes": len(gs), "groupes_purs": sum(1 for g in gs if len({verite[i] for i in g}) == 1),
                            "retenues_par_carte": len(r_cartes), "idees_par_carte": len({verite[i] for i in r_cartes}),
                            "groupes_retenus": len(r_groupes), "idees_par_groupe": len({verite[i] for i in reps})}
    return out


def doublons(W, proc):
    with ProcessPoolExecutor(proc) as ex:
        mondes = list(ex.map(_doublons_monde_v2, range(W), chunksize=1))
    cats = list(mondes[0]["paires"])
    res = {c: {"doit_regrouper": mondes[0]["paires"][c]["doit_regrouper"],
               "juste": part(sum(m["paires"][c]["regroupe"] == m["paires"][c]["doit_regrouper"] for m in mondes), len(mondes))}
           for c in cats}
    g24 = {k: round(float(np.mean([m["generation_24"][k] for m in mondes])), 2) for k in mondes[0]["generation_24"]}
    return {"resume_paires": res, "resume_generation_24": g24, "mondes": mondes}


# --- puissance selon la taille de l'archive (E-3) ----------------------------------------------------------------------------

def _archive_monde(args):
    w, reps, tailles = args
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    ids = [e["id"] for e in spec["effets"]]
    rng = rng_de("archive", w)
    out = {"monde": w, "effets": {}}
    for e in spec["effets"]:
        if e["classe"] not in ("moyenne", "faible"):
            continue
        Wm = M.compiler_monde(spec, sans=(e["id"],))
        autres = [i for i in ids if i != e["id"]]
        extras = []
        for _ in range(max(tailles)):
            S = sorted(set(rng.choice(autres, size=int(rng.integers(2, len(autres))), replace=False).tolist()))
            extras.append(P1._bruiter(spec, S, 0.15, rng))
        res = {}
        for k in tailles:
            x = 0
            for r in range(reps):
                ev = M.juger(loi, [Wm] + extras[:k], loi, D, nsp, rng_de("archive-juge", w, e["id"], k, r), n=400)
                x += M.promue_hors_famille(ev, M_DESSIN)[0]
            res[str(k + 1)] = x
        out["effets"][e["id"]] = {"classe": e["classe"], "information": round(infos[e["id"]], 4), "promus": res, "repetitions": reps}
    return out


def archive(W, reps, proc, tailles=(0, 7, 15)):
    with ProcessPoolExecutor(proc) as ex:
        mondes = list(ex.map(_archive_monde, [(w, reps, tailles) for w in range(W)], chunksize=1))
    res = {}
    for c in ("moyenne", "faible"):
        for k in tailles:
            x = sum(e["promus"][str(k + 1)] for m in mondes for e in m["effets"].values() if e["classe"] == c)
            n = sum(e["repetitions"] for m in mondes for e in m["effets"].values() if e["classe"] == c)
            res[f"{c}|archive={k + 1}"] = part(x, n)
    return {"resume": res, "mondes": mondes}


# --- plusieurs générations, déterministe (E-2), famille tirée (E-4), règle v2 (E-1) -------------------------------------------

PROBA_TROUVER = {"forte": 0.5, "moyenne": 0.25, "latente": 0.25, "faible": 0.1}


def _generations_course_v2(args):
    w, condition, G_, n, m = args
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    ids = [e["id"] for e in spec["effets"]]
    Zref, Gref = M.tirer_instances(rng_de("gen-ref", w), 1500, D, nsp)
    archive_ = [k1]
    connus = {eid_k1}
    captes = set(M.captes(o.attribution(k1, spec), infos))
    seuil = math.log(m / M.ALPHA)
    hist = []
    rng = rng_de("gen-v2", w)
    for g in range(1, G_ + 1):
        cartes, S_cartes = [], []
        for _p in range(4):
            for _c in range(6):
                S = {i for i in sorted(connus) if rng.random() < 0.9}
                for i in ids:
                    if i not in connus and rng.random() < PROBA_TROUVER[cibles[i][0]]:
                        S.add(i)
                S = sorted(S) or [eid_k1]
                cartes.append(P1._bruiter(spec, S, 0.15, rng))
                S_cartes.append(S)
        les = {i: M.log_e_arrete(M.juger(c, archive_, loi, D, nsp, rng_de("gen-juge", w, g, i), n=n)["traj"], seuil)
               for i, c in enumerate(cartes)}
        if condition == "A2":
            gs, (dg, ds, can) = M2.grouper_v2(cartes, Zref, Gref, nsp)
            les_g = {gi: M.log_e_groupe([les[i] for i in gg]) for gi, gg in enumerate(gs)}
            promus = []
            for gi in M.e_bh(les_g, m):
                gg = gs[gi]
                promus.append(gg[0] if len(gg) == 1 else M2.representant_v2(
                    gg, dg, can, statistique_de_choix=lambda i: M.test_de_mort(cartes[i], loi, D, nsp, rng_de("gen-choix", w, g, i))[0])[0])
            n_groupes = len(gs)
        else:
            promus = M.e_bh(les, m)
            n_groupes = None
        promus = sorted(promus)
        retenues = [i for i in promus if M.test_de_mort(cartes[i], loi, D, nsp, rng_de("gen-mort", w, g, i))[1]]
        env = o.gain_enveloppe(archive_)
        faux = sum(1 for i in retenues if o.gain(cartes[i]) - env < M.SEUIL_ORACLE)
        for i in retenues:
            archive_.append(cartes[i])
            connus |= set(S_cartes[i])
            captes |= set(M.captes(o.attribution(cartes[i], spec), infos))
        hist.append({"generation": g, "groupes": n_groupes, "promues": len(promus), "retenues": len(retenues),
                     "archive": len(archive_), "captes": sorted(captes),
                     "captes_par_classe": {c: sum(1 for i in captes if cibles[i][0] == c) for c in ("forte", "moyenne", "latente", "faible")},
                     "fausses_decouvertes": faux, "gain_enveloppe": round(o.gain_enveloppe(archive_), 4)})
    return {"monde": w, "condition": condition, "composantes": len(ids), "gabarit": gabarit_de(spec), "generations": hist}


def generations(W, G_, n, m, proc):
    taches = [(w, c, G_, n, m) for w in range(W) for c in ("sans", "A2")]
    with ProcessPoolExecutor(proc) as ex:
        courses = list(ex.map(_generations_course_v2, taches, chunksize=1))
    res = {}
    for c in ("sans", "A2"):
        cs = [x for x in courses if x["condition"] == c]
        par = {}
        for g in range(G_):
            hs = [x["generations"][g] for x in cs]
            par[str(g + 1)] = {
                "promues_moyen": round(float(np.mean([h["promues"] for h in hs])), 2),
                "retenues_moyen": round(float(np.mean([h["retenues"] for h in hs])), 2),
                "archive_moyen": round(float(np.mean([h["archive"] for h in hs])), 2),
                "part_captee_moyenne": round(float(np.mean([len(h["captes"]) / x["composantes"] for h, x in zip(hs, cs)])), 3),
                "part_captee_ecart_type": round(float(np.std([len(h["captes"]) / x["composantes"] for h, x in zip(hs, cs)], ddof=1)), 3),
                "faibles_captees_moyen": round(float(np.mean([h["captes_par_classe"]["faible"] for h in hs])), 2),
                "fausses_decouvertes_total": int(sum(h["fausses_decouvertes"] for h in hs)),
                "retenues_total": int(sum(h["retenues"] for h in hs)),
                "gain_enveloppe_moyen": round(float(np.mean([h["gain_enveloppe"] for h in hs])), 4)}
        res["sans_regroupement" if c == "sans" else "regroupement_v2"] = par
    return {"resume": res, "courses": courses,
            "parametres": {"mondes": W, "generations": G_, "tirages": n, "m": m, "proba_trouver_estimee": PROBA_TROUVER}}


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("commande", choices=("representant", "doublons", "detection", "attribution", "archive", "generations"))
    a.add_argument("sortie")
    a.add_argument("--mondes", type=int, default=12)
    a.add_argument("--repetitions", type=int, default=40)
    a.add_argument("--processus", type=int, default=4)
    x = a.parse_args(argv)
    if os.path.exists(x.sortie):
        print(f"refus : {x.sortie} existe déjà (on n'écrase jamais)")
        return 2
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if x.commande == "representant":
        res = representant(x.mondes, x.processus)
    elif x.commande == "doublons":
        res = doublons(x.mondes, x.processus)
    elif x.commande == "detection":
        res = P1.detection(x.mondes, x.repetitions, (200, 400), M_DESSIN, x.processus)
    elif x.commande == "attribution":
        res = P1.attribution(x.mondes, x.processus)
    elif x.commande == "archive":
        res = archive(x.mondes, x.repetitions, x.processus)
    else:
        res = generations(x.mondes, 3, 400, M_DESSIN, x.processus)
    sortie = {"version": VERSION, "commande": x.commande, "arguments": vars(x), "debut_utc": debut,
              "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
              "pythonhashseed": os.environ.get("PYTHONHASHSEED"),
              "versions": {"python": platform.python_version(), "numpy": np.__version__},
              "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
              "resultat": res}
    with open(x.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in res.items() if k not in ("mondes", "courses")}, ensure_ascii=False)[:6000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
