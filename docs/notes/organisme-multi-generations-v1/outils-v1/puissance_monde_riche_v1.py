"""Calculs de puissance hors ligne de la conception « monde riche et doublons » — v1.

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Aucun appel de modèle, aucun réseau. Mondes synthétiques de la famille
MR-1 écrits par programme (`monde_riche_outils_v1.generer_monde_synthetique`), jamais par Kimi. Juge **simplifié** (modèle du
nul v8 avec l'archive) : chaque chiffre de ce script est une estimation de conception, à refaire avec le code gelé de
l'organisme dans le préenregistrement.

Sous-commandes (chacune écrit un JSON neuf et refuse d'écraser) :
  etalonnage   juge simplifié sur le dessin de la course v67 (monde S-V1, archive {K1}, V1-V4, F1-F4, T-ELIM, m = 22),
               à comparer aux chiffres publiés (`puissance-boucle-reelle-v1-r1000.json`, `a23959fa…`) ;
  detection    mondes MR-1 : promotion puis survie des vraies plantées « K1 + un effet » selon leur gain au-delà de
               l'archive, pour n = 200, 400, 800 tirages ; fausses couvertes ; sondes hors classe (par morceaux) ;
  doublons     cartes synthétiques (variantes, reformulations, tempérées, mêlées, distinctes, ajout faible) : taux de
               regroupement juste selon ε ; effet sur e-BH ;
  attribution  l'attribution des effets par l'oracle retrouve-t-elle les effets d'une loi synthétique connue ?
  generations  plusieurs générations avec des proposeurs synthétiques, sur M mondes, trois conditions : sans
               regroupement (règle v67), étape A seule (groupes prédictifs, e-BH par groupe), étapes A et B (A, puis
               élagage par domination des représentants, sur tirages frais).

Graines (R9) : `numpy.random.SeedSequence(GRAINE, spawn_key=(clé de tâche…))`, clés de tâche entières tirées d'un sha256.
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
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import monde_riche_outils_v1 as M  # noqa: E402

VERSION = "puissance-monde-riche-v1"
GRAINE = 20261112
S_V1 = {"type": "softmax", "poids": [[0.833437, 0.861085], [-0.583145, 3.13424], [1.296203, -2.574519]],
        "biais": [-0.082681, 0.10575, -0.944897]}
K1_SV1 = {"type": "softmax", "poids": [[0.0, 0.0], [-0.834964, 0.0], [-0.242046, 0.0]], "biais": [0.0, 0.941698, 0.721847]}
UNIFORME = {"type": "fixe", "probas": [1.0, 1.0, 1.0]}
AVEUGLE = {"type": "fixe", "probas": [0.3, 0.4, 0.3]}


def cle(*parts):
    return int.from_bytes(hashlib.sha256("|".join(map(str, parts)).encode()).digest()[:4], "big")


def rng_de(*parts):
    return np.random.default_rng(np.random.SeedSequence(GRAINE, spawn_key=tuple(cle(*parts[:i + 1]) for i in range(len(parts)))))


def wilson(x, n, z=1.959963984540054):
    if n == 0:
        return [0.0, 1.0]
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def part(x, n):
    return {"x": int(x), "n": int(n), "p": round(x / n, 4) if n else None, "wilson": wilson(x, n)}


fausses_couvertes = M.fausses_couvertes


# ---------------------------------------------------------------------------------------------------------------------
# 1. Étalonnage sur le dessin de la course v67
# ---------------------------------------------------------------------------------------------------------------------

def _etalonnage_rep(r):
    rng = rng_de("etalonnage", r)
    m = 22
    seuil = math.log(m / M.ALPHA)
    vraies = {"V1": S_V1, "V2": {"type": "softmax", "poids": [[0.0, l[1]] for l in S_V1["poids"]], "biais": S_V1["biais"]},
              "V3": {"type": "transformee", "base": S_V1, "puissance": 0.08},
              "V4": {"type": "melange", "composantes": [S_V1, UNIFORME], "poids": [0.15, 0.85]}}
    out = {}
    for groupe, lois, arch in (("vraie", vraies, [K1_SV1]), ("fausse", fausses_couvertes(K1_SV1), [K1_SV1]),
                               ("fausse-sans-archive", fausses_couvertes(K1_SV1), []),
                               ("instrument", {"T-ELIM": {"type": "transformee", "base": S_V1, "puissance": 1.25}}, [K1_SV1])):
        for nom, loi in lois.items():
            ev = M.juger(loi, arch, S_V1, 2, 2, rng)
            pr, le = M.promue_hors_famille(ev, m)
            s, survit = (M.test_de_mort(loi, S_V1, 2, 2, rng, seuil=2.0 if nom == "T-ELIM" else M.SEUIL_MORT) if pr else (None, None))
            out[f"{groupe}|{nom}"] = {"promue": pr, "survit": survit, "log_w_max": round(ev["log_w_max"], 4)}
    return out


def etalonnage(R, proc):
    with ProcessPoolExecutor(proc) as ex:
        reps = list(ex.map(_etalonnage_rep, range(R), chunksize=4))
    cles = sorted(reps[0])
    par_loi = {}
    for k in cles:
        pr = sum(r[k]["promue"] for r in reps)
        ps = sum(1 for r in reps if r[k]["promue"] and r[k]["survit"])
        par_loi[k] = {"promue": part(pr, R), "promue_puis_survivante": part(ps, R),
                      "log_w_max_max": max(r[k]["log_w_max"] for r in reps),
                      "log_w_max_mediane": round(float(np.median([r[k]["log_w_max"] for r in reps])), 3)}
    publie = {"vraie|V1": 1000, "vraie|V2": 1000, "vraie|V3": 617, "vraie|V4": 501,
              "fausse-sans-archive (725 à 810 chacune ; au moins une : 994)": None,
              "source": "docs/notes/organisme-boucle-reelle-v1/sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json (a23959fa…), "
                        "recopié par le texte v2, section 4.2 (80fe4f03…)"}
    au_moins_une = sum(1 for r in reps if any(r[f"fausse-sans-archive|{f}"]["promue"] for f in fausses_couvertes(K1_SV1)))
    oracle = M.Oracle(S_V1, 2, 2, n=20000)
    return {"par_loi": par_loi, "artefact_au_moins_une_fausse_sans_archive": part(au_moins_une, R),
            "publie_course_v67_sur_1000": publie,
            "oracle_20000": {"gain_S_V1": round(oracle.gain(S_V1), 4), "gain_K1": round(oracle.gain(K1_SV1), 4)}}


# ---------------------------------------------------------------------------------------------------------------------
# 2. Détection dans les mondes MR-1
# ---------------------------------------------------------------------------------------------------------------------

def preparer_monde(w):
    spec, cibles = M.generer_monde_synthetique(cle("monde-mr1", w))
    loi = M.compiler_monde(spec)
    o = M.Oracle(loi, spec["dimension"], spec["sous_populations"], n=12000, graine=cle("oracle", w))
    k1, eid_k1, infos = M.k1_du_monde(spec, o)
    return spec, cibles, loi, o, k1, eid_k1, infos


def _detection_monde(args):
    w, reps, ns, m = args
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    k1, eid_k1, infos, vraies, fausses = M.jeu_plante_mr1(spec, o)
    plantees = {}
    for nom, v in vraies.items():
        plantees[f"{nom}-{v['classe']}" if nom.startswith("V-K1+") else nom] = ("vraie", v["loi"], [k1])
    for nom, f in fausses.items():
        plantees[nom] = ("fausse", f, [k1])
        plantees[nom + "-sans-archive"] = ("artefact", f, [])
    # archive à deux lois (« génération 2 ») : K1 et la seconde forte restreinte ; recombinaisons couvertes et par morceaux
    forte2 = next(e["id"] for e in spec["effets"] if cibles[e["id"]][0] == "forte" and e["id"] != eid_k1)
    a2 = M.monde_restreint(spec, [forte2])
    j_k1 = next(e["trait"] for e in spec["effets"] if e["id"] == eid_k1)
    plantees["F5-melange-de-deux-lois-d-archive"] = ("fausse2", {"type": "melange", "composantes": [k1, a2], "poids": [0.5, 0.5]}, [k1, a2])
    plantees["F6-copie-de-la-seconde"] = ("fausse2", json.loads(json.dumps(a2)), [k1, a2])
    plantees["H1-par-morceaux-hors-classe"] = ("sonde-hors-classe",
                                               {"type": "si_sinon", "condition": {"indice": int(j_k1), "seuil": 0.0}, "si": k1, "sinon": a2},
                                               [k1, a2])
    orac = {}
    for nom, (genre, l, arch) in plantees.items():
        orac[nom] = {"genre": genre, "gain": round(o.gain(l), 5), "au_dela_archive_v60": round(o.gain_au_dela(l, arch), 5),
                     "au_dela_enveloppe": round(o.gain_au_dela_enveloppe(l, arch), 5), "archive": len(arch)}
    res = {}
    for nom, (genre, l, arch) in plantees.items():
        for n in ns:
            if genre != "vraie" and n == max(ns) and len(ns) > 2:
                continue
            pr = ps = 0
            for r in range(reps):
                rng = rng_de("detection", w, nom, n, r)
                ev = M.juger(l, arch, loi, D, nsp, rng, n=n)
                p, _ = M.promue_hors_famille(ev, m)
                if p:
                    pr += 1
                    ps += M.test_de_mort(l, loi, D, nsp, rng)[1]
            res[f"{nom}|n={n}"] = {"promue": pr, "promue_puis_survivante": ps, "repetitions": reps}
    return {"monde": w, "effet_k1": eid_k1, "informations": {k: round(v, 5) for k, v in infos.items()},
            "classes": {k: v[0] for k, v in cibles.items()}, "gain_monde": round(o.gain(loi), 4),
            "gain_k1": round(o.gain(k1), 4), "oracle": orac, "jugements": res}


def detection(W, reps, ns, m, proc):
    with ProcessPoolExecutor(proc) as ex:
        mondes = list(ex.map(_detection_monde, [(w, reps, ns, m) for w in range(W)], chunksize=1))
    # résumé : vraies par tranche de gain au-delà de l'archive (oracle v60) et par n
    bornes = [0.0, 0.01, 0.02, 0.03, 0.04, 0.06, 0.08, 0.12, 0.2, 10.0]
    resume = {}
    for n in ns:
        tr = {}
        for a, b in zip(bornes[:-1], bornes[1:]):
            x = tot = 0
            for mo in mondes:
                for nom, o in mo["oracle"].items():
                    if o["genre"] != "vraie" or not (a <= o["au_dela_archive_v60"] < b):
                        continue
                    j = mo["jugements"].get(f"{nom}|n={n}")
                    if j:
                        x += j["promue_puis_survivante"]
                        tot += j["repetitions"]
            if tot:
                tr[f"[{a}; {b}["] = part(x, tot)
        resume[f"vraies_par_gain_au_dela_archive|n={n}"] = tr
        for genre in ("fausse", "fausse2", "artefact", "sonde-hors-classe"):
            x = tot = 0
            for mo in mondes:
                for nom, o in mo["oracle"].items():
                    j = mo["jugements"].get(f"{nom}|n={n}")
                    if o["genre"] == genre and j:
                        x += j["promue"]
                        tot += j["repetitions"]
            if tot:
                resume[f"{genre}|n={n}"] = part(x, tot)
    for classe in ("forte", "moyenne", "faible"):
        for n in ns:
            x = tot = 0
            for mo in mondes:
                for nom, o in mo["oracle"].items():
                    if o["genre"] == "vraie" and nom.endswith(f"-{classe}"):
                        j = mo["jugements"][f"{nom}|n={n}"]
                        x += j["promue_puis_survivante"]
                        tot += j["repetitions"]
            resume[f"vraies_classe_{classe}|n={n}"] = part(x, tot)
    # dispersion entre mondes du taux des faibles
    for n in ns:
        taux = []
        for mo in mondes:
            x = tot = 0
            for nom, o in mo["oracle"].items():
                if o["genre"] == "vraie" and nom.endswith("-faible"):
                    j = mo["jugements"][f"{nom}|n={n}"]
                    x += j["promue_puis_survivante"]
                    tot += j["repetitions"]
            taux.append(x / tot)
        resume[f"faibles_taux_par_monde|n={n}"] = {"min": round(min(taux), 3), "max": round(max(taux), 3),
                                                   "ecart_type_entre_mondes": round(float(np.std(taux, ddof=1)), 4)}
    return {"resume": resume, "mondes": mondes, "m": m, "ns": list(ns), "repetitions_par_loi": reps}


# ---------------------------------------------------------------------------------------------------------------------
# 3. Doublons
# ---------------------------------------------------------------------------------------------------------------------

def _bruiter(spec, garder, sigma, rng):
    s2 = json.loads(json.dumps(spec))
    for e in s2["effets"]:
        f = float(np.exp(rng.normal(0, sigma)))
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = (np.asarray(e[c]) * f).tolist()
    s2["biais"] = (np.asarray(s2["biais"]) + rng.normal(0, sigma * 0.3, len(s2["biais"]))).tolist()
    return M.monde_restreint(s2, garder)


def _reformuler(loi):
    """Même loi écrite autrement : lignes du softmax décalées d'une constante, puis mélange à poids nul d'une loi fixe."""
    def dec(l):
        if l["type"] == "softmax":
            W = np.asarray(l["poids"]) + 0.7
            b = np.asarray(l["biais"]) - 0.3
            return {"type": "softmax", "poids": W.round(6).tolist(), "biais": b.round(6).tolist()}
        if l["type"] in ("si_sinon",):
            return dict(l, si=dec(l["si"]), sinon=dec(l["sinon"]))
        if l["type"] == "par_sous_population":
            return dict(l, lois={k: dec(v) for k, v in l["lois"].items()})
        if l["type"] == "melange":
            return dict(l, composantes=[dec(c) for c in l["composantes"]])
        return l
    return {"type": "melange", "composantes": [dec(loi), UNIFORME], "poids": [1.0, 0.0]}


def _doublons_monde(args):
    w, epsilons = args
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    rng = rng_de("doublons", w)
    Zref, Gref = M.tirer_instances(rng_de("doublons-ref", w), 2000, D, nsp)
    ids = [e["id"] for e in spec["effets"]]
    fortes = [i for i in ids if cibles[i][0] == "forte"]
    moy = [i for i in ids if cibles[i][0] == "moyenne"]
    faibles = [i for i in ids if cibles[i][0] == "faible"]
    base_S = sorted(set(fortes) | {moy[0]})
    base = M.monde_restreint(spec, base_S)
    paires = []  # (catégorie, loi a, loi b, doit_regrouper)
    for s in (0.05, 0.1, 0.2, 0.3):
        paires.append((f"variante-sigma-{s}", base, _bruiter(spec, base_S, s, rng), True))
    paires.append(("reformulation", base, _reformuler(base), True))
    paires.append(("temperee-1.2", base, {"type": "transformee", "base": base, "puissance": 1.2}, True))
    paires.append(("melee-0.8-uniforme", base, {"type": "melange", "composantes": [base, UNIFORME], "poids": [0.8, 0.2]}, True))
    paires.append(("distincte-moyenne", base, M.monde_restreint(spec, sorted(set(fortes) | {moy[1]})), False))
    paires.append(("distincte-forte", base, M.monde_restreint(spec, sorted({fortes[0], moy[0]})), False))
    paires.append(("ajout-faible", base, M.monde_restreint(spec, sorted(set(base_S) | {faibles[0]})), False))
    paires.append(("ajout-moyenne", base, M.monde_restreint(spec, sorted(set(base_S) | {moy[1]})), False))
    out = {"monde": w, "paires": {}}
    for cat, a, b, doit in paires:
        Pa, Pb = M.probas(a, Zref, Gref), M.probas(b, Zref, Gref)
        ca, cb = M.empreinte(M.forme_canonique(a)), M.empreinte(M.forme_canonique(b))
        dab, iab = M.distance_au_nul(Pb, Pa)
        dba, iba = M.distance_au_nul(Pa, Pb)
        d = 0.0 if ca == cb else min(dab, dba)
        out["paires"][cat] = {"doit_regrouper": doit, "canon_egal": ca == cb, "d": round(d, 5),
                              "d_b_vers_a": round(dab, 5), "d_a_vers_b": round(dba, 5),
                              "borne_pire_monde": round(min(iab, iba), 5),
                              "gain_b_au_dela_de_a_oracle": round(o.gain(b) - o.gain(a), 5),
                              "regroupe": {str(e): bool(d < e) for e in epsilons}}
    # une génération synthétique de 24 cartes : 3 idées × 6 variantes, 6 cartes distinctes
    idees = [base_S, sorted(set(fortes) | {moy[1]}), sorted({fortes[0]} | set(faibles[:2]))]
    cartes, verite = [], []
    for k, S in enumerate(idees):
        for v in range(6):
            cartes.append(_bruiter(spec, S, 0.15, rng))
            verite.append(f"idee-{k}")
    for v in range(6):
        S = sorted(set(rng.choice(ids, size=int(rng.integers(2, 5)), replace=False).tolist()))
        cartes.append(_bruiter(spec, S, 0.15, rng))
        verite.append("|".join(S))
    groupes = {}
    for e in epsilons:
        gs, _ = M.grouper(cartes, Zref, Gref, eps=e)
        purs = sum(1 for g in gs if len({verite[i] for i in g}) == 1)
        idees_coupees = sum(1 for k in range(3) if len([g for g in gs if any(verite[i] == f"idee-{k}" for i in g)]) > 1)
        groupes[str(e)] = {"groupes": len(gs), "groupes_purs": purs, "idees_coupees_en_plusieurs_groupes": idees_coupees,
                           "tailles": sorted((len(g) for g in gs), reverse=True)}
    out["generation_24_cartes"] = groupes
    # effet sur le juge : e-BH par carte et par groupe (ε = 0,01), archive {K1}, n = 200, m = 40
    gs, _ = M.grouper(cartes, Zref, Gref, eps=0.01)
    m = 40
    seuil = math.log(m / M.ALPHA)
    les = {}
    for i, c in enumerate(cartes):
        ev = M.juger(c, [k1], loi, D, nsp, rng_de("doublons-juge", w, i))
        les[i] = M.log_e_arrete(ev["traj"], seuil)
    r_cartes = M.e_bh(les, m)
    les_g = {gi: M.log_e_groupe([les[i] for i in g]) for gi, g in enumerate(gs)}
    r_groupes = M.e_bh(les_g, m)
    reps = sorted((max(gs[g], key=lambda i: (les[i], -i)) for g in r_groupes), key=lambda i: (-les[i], i))
    gardes, _ = M.elaguer(reps, cartes, [k1], loi, D, nsp, lambda c: rng_de("doublons-elagage", w, *c), m)
    out["effet_e_bh"] = {"retenues_par_carte": len(r_cartes),
                         "idees_distinctes_parmi_retenues_par_carte": len({verite[i] for i in r_cartes}),
                         "groupes_retenus": len(r_groupes),
                         "idees_distinctes_parmi_representants": len({verite[i] for i in reps}),
                         "gardees_apres_elagage": len(gardes),
                         "idees_distinctes_apres_elagage": len({verite[i] for i in gardes})}
    return out


def doublons(W, epsilons, proc):
    with ProcessPoolExecutor(proc) as ex:
        mondes = list(ex.map(_doublons_monde, [(w, epsilons) for w in range(W)], chunksize=1))
    resume = {}
    cats = list(mondes[0]["paires"])
    for cat in cats:
        doit = mondes[0]["paires"][cat]["doit_regrouper"]
        resume[cat] = {"doit_regrouper": doit,
                       "d_mediane": round(float(np.median([mo["paires"][cat]["d"] for mo in mondes])), 5),
                       "d_max": round(float(np.max([mo["paires"][cat]["d"] for mo in mondes])), 5),
                       "d_min": round(float(np.min([mo["paires"][cat]["d"] for mo in mondes])), 5),
                       "gain_oracle_b_moins_a_median": round(float(np.median([mo["paires"][cat]["gain_b_au_dela_de_a_oracle"] for mo in mondes])), 5),
                       "juste_selon_eps": {str(e): part(sum(1 for mo in mondes if mo["paires"][cat]["regroupe"][str(e)] == doit), len(mondes))
                                           for e in epsilons}}
    gen = {}
    for e in epsilons:
        gen[str(e)] = {"groupes_moyen": round(float(np.mean([mo["generation_24_cartes"][str(e)]["groupes"] for mo in mondes])), 2),
                       "part_groupes_purs": round(float(np.sum([mo["generation_24_cartes"][str(e)]["groupes_purs"] for mo in mondes]) /
                                                        np.sum([mo["generation_24_cartes"][str(e)]["groupes"] for mo in mondes])), 3),
                       "idees_coupees_moyen_sur_3": round(float(np.mean([mo["generation_24_cartes"][str(e)]["idees_coupees_en_plusieurs_groupes"] for mo in mondes])), 2)}
    eb = {k: round(float(np.mean([mo["effet_e_bh"][k] for mo in mondes])), 2) for k in mondes[0]["effet_e_bh"]}
    return {"resume_paires": resume, "resume_generation_24": gen, "resume_e_bh_moyennes": eb, "mondes": mondes}


# ---------------------------------------------------------------------------------------------------------------------
# 4. Attribution des effets par l'oracle
# ---------------------------------------------------------------------------------------------------------------------

def _attribution_monde(w):
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde(w)
    rng = rng_de("attribution", w)
    ids = [e["id"] for e in spec["effets"]]
    out = []
    for t in range(12):
        S = sorted(set(rng.choice(ids, size=int(rng.integers(1, 6)), replace=False).tolist()))
        l = _bruiter(spec, S, 0.15, rng)
        attr = o.attribution(l, spec)
        c = M.captes(attr, infos)
        out.append({"S": S, "captes": c, "classes": {i: cibles[i][0] for i in ids}})
    return out


def attribution(W, proc):
    with ProcessPoolExecutor(proc) as ex:
        res = list(ex.map(_attribution_monde, range(W), chunksize=1))
    vp = fp = fn = 0
    par_classe = {c: {"vrais_positifs": 0, "faux_negatifs": 0, "faux_positifs": 0} for c in ("forte", "moyenne", "faible")}
    exact = tot = 0
    for mo in res:
        for x in mo:
            S, C = set(x["S"]), set(x["captes"])
            tot += 1
            exact += S == C
            for i, cl in x["classes"].items():
                if i in S and i in C:
                    par_classe[cl]["vrais_positifs"] += 1
                elif i in S:
                    par_classe[cl]["faux_negatifs"] += 1
                elif i in C:
                    par_classe[cl]["faux_positifs"] += 1
    return {"lois": tot, "ensemble_exact": part(exact, tot), "par_classe": par_classe}


# ---------------------------------------------------------------------------------------------------------------------
# 5. Plusieurs générations, proposeurs synthétiques
# ---------------------------------------------------------------------------------------------------------------------

PROBA_TROUVER = {"forte": 0.5, "moyenne": 0.25, "faible": 0.1}  # estimé : modèle de proposeur, pas une mesure


def _generations_course(args):
    w, condition, G, n, m, eps = args
    regrouper = condition in ("A", "AB")
    spec, cibles, loi, o, k1, eid_k1, infos = preparer_monde(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    ids = [e["id"] for e in spec["effets"]]
    Zref, Gref = M.tirer_instances(rng_de("gen-ref", w), 1500, D, nsp)
    archive = [k1]
    connus = {eid_k1}
    captes_oracle = set(M.captes(o.attribution(k1, spec), infos))
    seuil = math.log(m / M.ALPHA)
    hist = []
    rng = rng_de("gen", w)  # mêmes cartes proposées avec et sans regroupement (même graine), juge apparié
    for g in range(1, G + 1):
        cartes, S_cartes = [], []
        for p in range(4):
            for c in range(6):
                S = {i for i in connus if rng.random() < 0.9}
                for i in ids:
                    if i not in connus and rng.random() < PROBA_TROUVER[cibles[i][0]]:
                        S.add(i)
                if not S:
                    S = {eid_k1}
                cartes.append(_bruiter(spec, sorted(S), 0.15, rng))
                S_cartes.append(sorted(S))
        les, evs = {}, {}
        for i, c in enumerate(cartes):
            ev = M.juger(c, archive, loi, D, nsp, rng_de("gen-juge", w, g, i), n=n)
            les[i] = M.log_e_arrete(ev["traj"], seuil)
        if regrouper:
            gs, _ = M.grouper(cartes, Zref, Gref, eps=eps)
            les_g = {gi: M.log_e_groupe([les[i] for i in gg]) for gi, gg in enumerate(gs)}
            promus = [max(gs[gi], key=lambda i: (les[i], -i)) for gi in M.e_bh(les_g, m)]
            n_groupes = len(gs)
        else:
            promus = M.e_bh(les, m)
            n_groupes = None
        promus = sorted(promus, key=lambda i: (-les[i], i))
        n_promus = len(promus)
        if condition == "AB":
            promus, _ = M.elaguer(promus, cartes, archive, loi, D, nsp, lambda c: rng_de("gen-elagage", w, g, *c), m, n=n)
        retenues = [i for i in promus if M.test_de_mort(cartes[i], loi, D, nsp, rng_de("gen-mort", w, g, i))[1]]
        avant = list(archive)
        env_avant = o.gain_enveloppe(avant)
        faux = 0
        for i in retenues:
            if o.gain(cartes[i]) - env_avant < M.SEUIL_ORACLE:
                faux += 1
        for i in retenues:
            archive.append(cartes[i])
            connus |= set(S_cartes[i])
            captes_oracle |= set(M.captes(o.attribution(cartes[i], spec), infos))
        hist.append({"generation": g, "cartes": len(cartes), "groupes": n_groupes, "promues": n_promus,
                     "gardees_apres_elagage": len(promus),
                     "retenues": len(retenues), "archive": len(archive),
                     "effets_connus": sorted(connus), "effets_connus_par_classe": {c: sum(1 for i in connus if cibles[i][0] == c) for c in ("forte", "moyenne", "faible")},
                     "effets_captes_oracle": sorted(captes_oracle),
                     "effets_captes_oracle_par_classe": {c: sum(1 for i in captes_oracle if cibles[i][0] == c) for c in ("forte", "moyenne", "faible")},
                     "fausses_decouvertes_au_dela_enveloppe": faux,
                     "gain_enveloppe_archive": round(o.gain_enveloppe(archive), 4)})
    return {"monde": w, "condition": condition, "generations": hist,
            "effets_par_classe": {c: sum(1 for i in ids if cibles[i][0] == c) for c in ("forte", "moyenne", "faible")}}


def generations(W, G, n, m, eps, proc):
    taches = [(w, r, G, n, m, eps) for w in range(W) for r in ("sans", "A", "AB")]
    with ProcessPoolExecutor(proc) as ex:
        courses = list(ex.map(_generations_course, taches, chunksize=1))
    resume = {}
    for r in ("sans", "A", "AB"):
        cs = [c for c in courses if c["condition"] == r]
        par_g = {}
        for g in range(G):
            hs = [c["generations"][g] for c in cs]
            par_g[str(g + 1)] = {
                "promues_moyen": round(float(np.mean([h["promues"] for h in hs])), 2),
                "groupes_moyen": None if hs[0]["groupes"] is None else round(float(np.mean([h["groupes"] for h in hs])), 2),
                "retenues_moyen": round(float(np.mean([h["retenues"] for h in hs])), 2),
                "archive_moyen": round(float(np.mean([h["archive"] for h in hs])), 2),
                "effets_connus_moyen": round(float(np.mean([len(h["effets_connus"]) for h in hs])), 2),
                "effets_connus_ecart_type_entre_mondes": round(float(np.std([len(h["effets_connus"]) for h in hs], ddof=1)), 3),
                "faibles_connus_moyen": round(float(np.mean([h["effets_connus_par_classe"]["faible"] for h in hs])), 2),
                "effets_captes_oracle_moyen": round(float(np.mean([len(h["effets_captes_oracle"]) for h in hs])), 2),
                "effets_captes_oracle_ecart_type_entre_mondes": round(float(np.std([len(h["effets_captes_oracle"]) for h in hs], ddof=1)), 3),
                "faibles_captes_oracle_moyen": round(float(np.mean([h["effets_captes_oracle_par_classe"]["faible"] for h in hs])), 2),
                "moyennes_captees_oracle_moyen": round(float(np.mean([h["effets_captes_oracle_par_classe"]["moyenne"] for h in hs])), 2),
                "part_mondes_au_moins_un_faible_capte": round(float(np.mean([h["effets_captes_oracle_par_classe"]["faible"] >= 1 for h in hs])), 3),
                "moyennes_connues_moyen": round(float(np.mean([h["effets_connus_par_classe"]["moyenne"] for h in hs])), 2),
                "fausses_decouvertes_total": int(sum(h["fausses_decouvertes_au_dela_enveloppe"] for h in hs)),
                "retenues_total": int(sum(h["retenues"] for h in hs)),
                "gain_enveloppe_moyen": round(float(np.mean([h["gain_enveloppe_archive"] for h in hs])), 4),
                "part_mondes_progres_sur_g_precedente": None if g == 0 else round(float(np.mean(
                    [c["generations"][g]["gain_enveloppe_archive"] - c["generations"][g - 1]["gain_enveloppe_archive"] >= 0.01 for c in cs])), 3)}
        resume[{"sans": "sans_regroupement", "A": "etape_A_seule", "AB": "etapes_A_et_B"}[r]] = par_g
    return {"resume": resume, "courses": courses, "parametres": {"mondes": W, "generations": G, "tirages": n, "m": m, "eps": eps,
                                                                  "proba_trouver_estimee": PROBA_TROUVER,
                                                                  "proposeurs": 4, "cartes_par_proposeur": 6,
                                                                  "garder_un_effet_connu": 0.9, "bruit_sigma": 0.15}}


# ---------------------------------------------------------------------------------------------------------------------

def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("commande", choices=("etalonnage", "detection", "doublons", "attribution", "generations"))
    a.add_argument("sortie")
    a.add_argument("--repetitions", type=int, default=200)
    a.add_argument("--mondes", type=int, default=12)
    a.add_argument("--processus", type=int, default=4)
    a.add_argument("--tirages", type=int, nargs="+", default=[200, 400, 800])
    a.add_argument("--m", type=int, default=40)
    a.add_argument("--generations", type=int, default=3)
    a.add_argument("--eps", type=float, nargs="+", default=[0.005, 0.01, 0.02])
    x = a.parse_args(argv)
    if os.path.exists(x.sortie):
        print(f"refus : {x.sortie} existe déjà (on n'écrase jamais)")
        return 2
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if x.commande == "etalonnage":
        res = etalonnage(x.repetitions, x.processus)
    elif x.commande == "detection":
        res = detection(x.mondes, x.repetitions, tuple(x.tirages), x.m, x.processus)
    elif x.commande == "doublons":
        res = doublons(x.mondes, tuple(x.eps), x.processus)
    elif x.commande == "attribution":
        res = attribution(x.mondes, x.processus)
    else:
        res = generations(x.mondes, x.generations, x.tirages[0], x.m, x.eps[0], x.processus)
    sortie = {"version": VERSION, "commande": x.commande, "arguments": vars(x), "debut_utc": debut,
              "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "graine": GRAINE,
              "regle_graines": "numpy.random.SeedSequence(GRAINE, spawn_key=(clés de tâche sha256))",
              "versions": {"python": platform.python_version(), "numpy": np.__version__},
              "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
              "outils_sha256": hashlib.sha256(open(os.path.join(ICI, "monde_riche_outils_v1.py"), "rb").read()).hexdigest(),
              "resultat": res}
    with open(x.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    court = {k: v for k, v in res.items() if k not in ("mondes", "courses")}
    print(json.dumps(court, ensure_ascii=False, indent=1)[:12000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
