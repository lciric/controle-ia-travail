"""Calcul des verdicts du volet A de « Neuron Lens » par le lecteur neuf — v1.

Applique à la lettre le texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b88243…`), sections « Seuil »
(partie A) et « Critères de lecture gelés », selon le plan scellé `plan-de-lecture-v1.md` (`9413e09b…`). N'importe aucun module de la
course : chaque règle est réécrite ici. Entrées : les fichiers de `diag/20261114-165239-neuron-lens-volet-a/`. Les verdicts sont calculés
sur `brut-cas-sains.json` et `brut-mesures-C{1,2,3}.json` ; `volet-a-brut.json` n'est ouvert qu'ensuite, pour la comparaison.

Usage (depuis la racine du dépôt) : python docs/notes/neuron-lens-v1/lecture-volet-a/calcul_verdicts_volet_a_v1.py SORTIE.json
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.stats import rankdata

DIAG = Path("diag/20261114-165239-neuron-lens-volet-a")
COUCHES = ("8", "14", "20", "26")
BUDGETS = ("1", "8", "64", "512")
ENTROPIE = 20261114
MA_GRAINE = 20261115
POS, NEG, IND = "positive", "négative", "indécise"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def charger(nom):
    p = DIAG / f"{nom}.json"
    return json.loads(p.read_text(encoding="utf-8"))["resultat"], sha(p)


def regle(conds):
    assert len(conds) == 5
    k = sum(bool(c) for c in conds)
    return POS if k >= 3 else NEG if k <= 1 else IND


def moy(xs):
    return float(np.mean(xs))


def auc(y, s):
    """AUROC par les rangs moyens (égalités comptées pour 1/2), identique à celle de scikit-learn."""
    y = np.asarray(y)
    r = rankdata(s)
    n1 = int(y.sum())
    n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def cmp_deux(valeur, seuil, op):
    """Comparaison exacte et comparaison après arrondi à 6 décimales ; rend (exacte, arrondie)."""
    f = {">=": lambda a, b: a >= b, ">": lambda a, b: a > b, "<": lambda a, b: a < b}[op]
    return bool(f(valeur, seuil)), bool(f(round(valeur, 6), round(seuil, 6)))


ECARTS_ARRONDI = []  # tout cas où la comparaison exacte et la comparaison arrondie diffèrent


def cmp(nom, valeur, seuil, op):
    e, a = cmp_deux(float(valeur), float(seuil), op)
    if e != a:
        ECARTS_ARRONDI.append({"ou": nom, "valeur": valeur, "seuil": seuil, "op": op, "exacte": e, "arrondie": a})
    return e


# ------------------------------------------------------------------ cas sains
def cas_sains(cs):
    f_owl, f_ger = cs["i_owl"][1], cs["ii_german"][1]
    owl = any(x.startswith("owl") or x.startswith("noct") or x == "night" for x in f_owl)
    ger = any("german" in x or "德" in x for x in f_ger)
    syn = {l: list(v) for l, v in cs["iii_synthetique"].items()}
    out = {"i_owl": {"relu": owl, "course": cs["i_owl"][0], "formes": f_owl, "n_formes": len(f_owl)},
           "ii_german": {"relu": ger, "course": cs["ii_german"][0], "formes": f_ger, "n_formes": len(f_ger)},
           "iii_synthetique": syn, "iii_couches_presentes": sorted(syn) == sorted(COUCHES),
           "vocabulaire_entier_owl": cs["i_owl_vocabulaire_entier"], "vocabulaire_entier_german": cs["ii_german_vocabulaire_entier"]}
    out["tous_passes"] = bool(owl and cs["i_owl"][0] and ger and cs["ii_german"][0] and out["iii_couches_presentes"]
                              and all(len(v) == 2 and all(x is True for x in v) for v in syn.values())
                              and len(f_owl) == 10 and len(f_ger) == 10)
    out["tous_passes_course"] = cs["tous_passes"]
    return out


# ------------------------------------------------------------------ A1
def a1(c2):
    par = {}
    for l in COUCHES:
        ms = [c2["decoupes"][d][l]["a1"] for d in range(5)]
        cond = [bool(m["rang_s"] <= 10 and not m["un_temoin_place_p"]) for m in ms]
        par[l] = {"rang_s": [m["rang_s"] for m in ms], "rang_sans_lentille": [m["rang_sans_lentille"] for m in ms],
                  "rang_s_mediane": float(np.median([m["rang_s"] for m in ms])),
                  "rang_sans_lentille_mediane": float(np.median([m["rang_sans_lentille"] for m in ms])),
                  "s_place_p": [m["s_place_p"] for m in ms], "un_temoin_place_p": [m["un_temoin_place_p"] for m in ms],
                  "condition": cond, "classe": regle(cond),
                  "accord_condition_course": cond == [m["condition"] for m in ms],
                  "accord_s_place_p": [m["s_place_p"] for m in ms] == [m["rang_s"] <= 10 for m in ms],
                  "s_mieux": [bool(m["rang_s"] < m["rang_sans_lentille"]) for m in ms],
                  "classe_s_place_p": regle([m["s_place_p"] for m in ms]),
                  "classe_un_temoin_place_p": regle([m["un_temoin_place_p"] for m in ms])}
        par[l]["classe_s_mieux"] = regle(par[l]["s_mieux"])
    npos = sum(par[l]["classe"] == POS for l in COUCHES)
    verdict = "retrouvée" if npos >= 2 else "non retrouvée" if all(par[l]["classe"] == NEG for l in COUCHES) else "partielle"
    return {"par_couche": par, "verdict": verdict, "n_couches_positives": npos,
            "s_fait_mieux": sum(par[l]["classe_s_mieux"] == POS and par[l]["classe"] == POS for l in COUCHES) >= 2,
            "sans_lentille_au_moins_partout": all(par[l]["classe_s_mieux"] == NEG for l in COUCHES)}


# ------------------------------------------------------------------ A2
def a2(c1):
    par = {}
    for l in COUCHES:
        ms = [c1["decoupes"][d][l]["a2"] for d in range(5)]
        mieux = [bool(m["rho_s"] > m["rho_sans_lentille"]) for m in ms]
        par[l] = {"rho_s": [m["rho_s"] for m in ms], "rho_sans_lentille": [m["rho_sans_lentille"] for m in ms],
                  "rho_permutee": [m["rho_permutee"] for m in ms], "rho_c3": [m["rho_c3"] for m in ms],
                  "condition": [m["condition"] for m in ms], "classe": regle([m["condition"] for m in ms]),
                  "s_mieux": mieux, "classe_s_mieux": regle(mieux),
                  "accord_s_mieux_course": mieux == [m["s_mieux_a2"] for m in ms]}
    sac = {l: [c1["decoupes"][d][l]["auc_sac_id"] for d in range(5)] for l in COUCHES}
    sac_constant = all(len({sac[l][d] for l in COUCHES}) == 1 for d in range(5))
    sac_moy = {l: moy(sac[l]) for l in COUCHES}
    so = cmp("A2 sans objet", sac_moy["8"], 0.60, "<")
    npos = sum(par[l]["classe"] == POS for l in COUCHES)
    return {"par_couche": par, "auc_sac_id_par_decoupe": sac["8"], "auc_sac_id_identique_aux_couches": sac_constant,
            "auc_sac_id_moyenne": sac_moy, "sans_objet": so, "nomme": npos >= 2, "n_couches_positives": npos,
            "s_fait_mieux": sum(par[l]["classe_s_mieux"] == POS and par[l]["classe"] == POS for l in COUCHES) >= 2,
            "sans_lentille_au_moins_partout": all(par[l]["classe_s_mieux"] == NEG for l in COUCHES)}


# ------------------------------------------------------------------ A3
def a3(c, nom):
    par, anomalies = {}, []
    for l in COUCHES:
        ms = [c["decoupes"][d][l]["a3"] for d in range(5)]
        cond, contraire, q95 = [], [], []
        for d, m in enumerate(ms):
            vals = [m["chute_s"], m["chute_sac"], *m["chutes_aleatoires"]]
            if len(m["chutes_aleatoires"]) != 200 or any(v is None for v in vals):
                anomalies.append({"contraste": nom, "couche": l, "decoupe": d, "n_tirages": len(m["chutes_aleatoires"]),
                                  "n_absents": sum(v is None for v in vals)})
                cond.append(None)
                contraire.append(None)
                q95.append(None)
                continue
            q = float(np.quantile(m["chutes_aleatoires"], 0.95))
            q95.append(q)
            m1 = m["chute_s"] > q
            m2 = cmp(f"A3 {nom} couche {l} découpe {d} moitié", m["chute_s"], 0.5 * m["chute_sac"], ">=")
            cond.append(bool(m1 and m2))
            contraire.append(cmp(f"A3 {nom} couche {l} découpe {d} contraire", m["chute_s"], 0.5 * m["chute_sac"], "<"))
        chute_sac_moy = moy([m["chute_sac"] for m in ms]) if all(m["chute_sac"] is not None for m in ms) else None
        so = None if chute_sac_moy is None else cmp(f"A3 {nom} couche {l} plancher", chute_sac_moy, 0.02, "<")
        par[l] = {"chute_s": [m["chute_s"] for m in ms], "chute_sac": [m["chute_sac"] for m in ms], "centile_95": q95,
                  "chute_aleatoire_mediane": [None if any(v is None for v in m["chutes_aleatoires"]) else
                                              float(np.median(m["chutes_aleatoires"])) for m in ms],
                  "chute_aleatoire_max": [None if any(v is None for v in m["chutes_aleatoires"]) else
                                          float(np.max(m["chutes_aleatoires"])) for m in ms],
                  "chute_s_moyenne": moy([m["chute_s"] for m in ms]) if all(m["chute_s"] is not None for m in ms) else None,
                  "chute_sac_moyenne": chute_sac_moy, "sans_objet": so, "condition": cond, "contraire": contraire,
                  "classe": regle(cond) if None not in cond else None,
                  "classe_contraire": regle(contraire) if None not in contraire else None,
                  "jetons_s_presents_test": [m["jetons_s_presents_test"] for m in ms],
                  "exemples_ecartes": [m["exemples_ecartes"] for m in ms], "exemples_ecartes_sac": [m["exemples_ecartes_sac"] for m in ms],
                  "n_jetons_sac": [m["n_jetons_sac"] for m in ms], "jetons_s": [m["jetons_s"] for m in ms]}
    if anomalies:
        return {"par_couche": par, "anomalies": anomalies, "verdict": "non applicable telle quelle (valeur absente)"}
    jug = [l for l in COUCHES if not par[l]["sans_objet"]]
    if len(jug) < 2:
        v = "sans objet"
    elif sum(par[l]["classe"] == POS for l in jug) >= 2:
        v = "dépendance lue"
    elif all(par[l]["classe_contraire"] == POS for l in jug):
        v = "dépendance non lue"
    else:
        v = "indécise"
    return {"par_couche": par, "anomalies": anomalies, "couches_non_sans_objet": jug, "verdict": v}


# ------------------------------------------------------------------ A-ii
def graines_reech(indice_contraste):
    """Graine « rééchantillonnage » de chaque découpe : SeedSequence(20261114).spawn(4)[contraste].spawn(5)[d].spawn(6)[5]."""
    enfant = np.random.SeedSequence(ENTROPIE).spawn(4)[indice_contraste]
    return [d.spawn(6)[5] for d in enfant.spawn(5)]


def intervalle(scores_a, scores_b, ys, graines, n=2000, par_classe=True):
    """Écart moyen d'AUROC (a − b) sur les découpes ; intervalle à 95 % par rééchantillonnage apparié des exemples (dans chaque tirage,
    chaque découpe est retirée avec remise — à l'intérieur de chaque classe si `par_classe` — et l'écart est moyenné)."""
    rngs = [np.random.default_rng(g) for g in graines]
    ys = [np.asarray(y) for y in ys]
    A = [np.asarray(a, float) for a in scores_a]
    B = [np.asarray(b, float) for b in scores_b]
    obs = moy([auc(y, a) - auc(y, b) for a, b, y in zip(A, B, ys)])
    t = np.empty(n)
    for i in range(n):
        e = []
        for a, b, y, rng in zip(A, B, ys, rngs):
            if par_classe:
                idx = np.concatenate([rng.choice(np.flatnonzero(y == c), size=int((y == c).sum()), replace=True) for c in (0, 1)])
            else:
                while True:
                    idx = rng.integers(0, len(y), size=len(y))
                    if 0 < y[idx].sum() < len(y):
                        break
            e.append(auc(y[idx], a[idx]) - auc(y[idx], b[idx]))
        t[i] = np.mean(e)
    return obs, float(np.quantile(t, 0.025)), float(np.quantile(t, 0.975))


def aii(c, nom, indice):
    ood = nom != "C3"
    D = c["decoupes"]
    couches = {}
    for l in COUCHES:
        ms = [D[d][l] for d in range(5)]
        e = {"sonde_id": moy([m["auc_sonde_id"] for m in ms]), "sonde_id_par_decoupe": [m["auc_sonde_id"] for m in ms],
             "sac_id": moy([m["auc_sac_id"] for m in ms]),
             "neurones_id": {k: moy([m["aii"]["id"][f"k{k}"] for m in ms]) for k in BUDGETS},
             "autres_id": {k: moy([m["aii"]["id"][k] for m in ms]) for k in ms[0]["aii"]["id"] if not k.startswith("k")},
             "pca_k_effectif": ms[0]["aii"]["pca_k_effectif"], "C_sonde": [m["C_sonde"] for m in ms],
             "n_test": [len(m["y_id"]) for m in ms]}
        # contrôle : AUROC recalculées sur les scores versés
        e["recalcul_sonde_id_ecart_max"] = max(abs(auc(m["y_id"], m["scores_sonde_id"]) - m["auc_sonde_id"]) for m in ms)
        e["recalcul_neurones_id_ecart_max"] = max(abs(auc(m["y_id"], m["aii"]["id_scores"][f"k{k}"]) - m["aii"]["id"][f"k{k}"])
                                                  for m in ms for k in BUDGETS)
        e["ecart_id"] = {k: e["neurones_id"][k] - e["sonde_id"] for k in BUDGETS}
        # intervalle en distribution (description ; graine du lecteur)
        e["intervalle_id_graine_lecteur"] = {}
        for ik, k in enumerate(BUDGETS):
            g = np.random.SeedSequence([MA_GRAINE, indice, COUCHES.index(l), ik, 1]).spawn(5)
            e["intervalle_id_graine_lecteur"][k] = intervalle([m["aii"]["id_scores"][f"k{k}"] for m in ms],
                                                              [m["scores_sonde_id"] for m in ms], [m["y_id"] for m in ms], g)
        if ood:
            e["sonde_ood"] = moy([m["auc_sonde_ood"] for m in ms])
            e["sonde_ood_par_decoupe"] = [m["auc_sonde_ood"] for m in ms]
            e["sac_ood"] = moy([m["auc_sac_ood"] for m in ms])
            e["neurones_ood"] = {k: moy([m["aii"]["ood"][f"k{k}"] for m in ms]) for k in BUDGETS}
            e["autres_ood"] = {k: moy([m["aii"]["ood"][k] for m in ms]) for k in ms[0]["aii"]["ood"] if not k.startswith("k")}
            e["ecart_ood"] = {k: e["neurones_ood"][k] - e["sonde_ood"] for k in BUDGETS}
            e["n_ood"] = [len(m["y_ood"]) for m in ms]
            e["recalcul_ood_ecart_max"] = max(
                [abs(auc(m["y_ood"], m["scores_sonde_ood"]) - m["auc_sonde_ood"]) for m in ms]
                + [abs(auc(m["y_ood"], m["aii"]["ood_scores"][f"k{k}"]) - m["aii"]["ood"][f"k{k}"]) for m in ms for k in BUDGETS])
            e["intervalle_ood"], e["intervalle_ood_graine_lecteur"], e["intervalle_ood_sans_strate_de_classe"] = {}, {}, {}
            for ik, k in enumerate(BUDGETS):
                arg = ([m["aii"]["ood_scores"][f"k{k}"] for m in ms], [m["scores_sonde_ood"] for m in ms], [m["y_ood"] for m in ms])
                e["intervalle_ood"][k] = intervalle(*arg, graines_reech(indice))
                g = np.random.SeedSequence([MA_GRAINE, indice, COUCHES.index(l), ik, 2]).spawn(5)
                e["intervalle_ood_graine_lecteur"][k] = intervalle(*arg, g)
                g = np.random.SeedSequence([MA_GRAINE, indice, COUCHES.index(l), ik, 3]).spawn(5)
                e["intervalle_ood_sans_strate_de_classe"][k] = intervalle(*arg, g, par_classe=False)
        couches[l] = e

    def verdict(cle_intervalle):
        jug = []
        for l in COUCHES:
            e = couches[l]
            id_so = cmp(f"A-ii {nom} couche {l} plafond en distribution", e["sonde_id"], 0.99, ">=")
            ood_so = (not ood) or cmp(f"A-ii {nom} couche {l} plafond hors distribution", e["sonde_ood"], 0.99, ">=")
            e["partie_id_sans_objet"], e["partie_ood_sans_objet"] = id_so, (ood_so if ood else None)
            e["couche_sans_objet"] = bool(id_so and ood_so)
            if not (id_so and ood_so):
                jug.append((l, id_so))
        if len(jug) < 2:
            return "sans objet", [l for l, _ in jug], {}

        def perd(l, id_so, k):
            e, parts = couches[l], []
            if not id_so:
                parts.append(cmp(f"A-ii {nom} couche {l} k={k} perd id", e["sonde_id"] - e["neurones_id"][k], 0.05, ">"))
            if ood:
                parts.append(cmp(f"A-ii {nom} couche {l} k={k} perd ood", e["sonde_ood"] - e["neurones_ood"][k], 0.05, ">"))
            return all(parts)

        detail = {"perd": {l: {k: perd(l, so, k) for k in BUDGETS} for l, so in jug}, "apporte": {}}
        for k in ("1", "8", "64"):
            detail["apporte"][k] = {}
            for l, id_so in jug:
                e = couches[l]
                c_id = True if id_so else cmp(f"A-ii {nom} couche {l} k={k} id", e["neurones_id"][k] - e["sonde_id"], -0.02, ">=")
                c_ood = True if not ood else cmp(f"A-ii {nom} couche {l} k={k} borne ({cle_intervalle})", e[cle_intervalle][k][1], -0.05, ">=")
                detail["apporte"][k][l] = {"id": c_id if not id_so else "sans objet", "ood": c_ood if ood else "sans objet",
                                           "tient": bool(c_id and c_ood)}
        if all(v for d in detail["perd"].values() for v in d.values()):
            return "n'apporte rien", [l for l, _ in jug], detail
        if any(sum(x["tient"] for x in detail["apporte"][k].values()) >= 2 for k in ("1", "8", "64")):
            return "apporte", [l for l, _ in jug], detail
        return "indéterminé", [l for l, _ in jug], detail

    v, jug, detail = verdict("intervalle_ood")
    out = {"couches": couches, "verdict": v, "couches_non_sans_objet": jug, "detail": detail, "longueur": c["longueur"]}
    if ood:
        out["verdict_graine_lecteur"] = verdict("intervalle_ood_graine_lecteur")[0]
        out["verdict_sans_strate_de_classe"] = verdict("intervalle_ood_sans_strate_de_classe")[0]
    # qualificatif
    if nom == "C2":
        out["qualificatif"] = "sans objet"
    else:
        partie = "ood" if ood else "id"
        meilleur = {l: max(couches[l][f"neurones_{partie}"][k] for k in ("1", "8", "64")) for l in COUCHES}
        sac = {l: couches[l][f"sac_{partie}"] for l in COUCHES}
        tout = cmp(f"qualificatif {nom}", max(meilleur.values()) - max(sac.values()), 0.02, ">=")
        par_c = {l: cmp(f"qualificatif {nom} couche {l}", meilleur[l] - sac[l], 0.02, ">=") for l in COUCHES}
        out["qualificatif"] = "au-delà du texte" if tout else "pas au-delà du texte"
        out["qualificatif_detail"] = {"partie": partie, "meilleur_k64_par_couche": meilleur, "sac_par_couche": sac,
                                      "au_dela_par_couche": par_c, "ecart_toutes_couches": max(meilleur.values()) - max(sac.values())}
    # déclencheur « neurones égaux à la sonde » (définition déclarée par le code de la course : 0,005 en distribution)
    out["ecart_abs_meilleur_k64_sonde_id"] = {l: abs(max(couches[l]["neurones_id"][k] for k in ("1", "8", "64")) - couches[l]["sonde_id"])
                                              for l in COUCHES}
    return out


# ------------------------------------------------------------------ verdict de A-i
def verdict_i(chaine, r1, r2, r3c1, r3c2):
    lignes = {}
    if chaine:
        return "chaîne en défaut", lignes
    a2so = r2["sans_objet"]
    lignes["A1 non retrouvée"] = r1["verdict"] == "non retrouvée"
    lignes["sans lentille ≥ S à chaque couche (A1 et A2, ou A1 seul si A2 sans objet)"] = bool(
        r1["sans_lentille_au_moins_partout"] and (a2so or r2["sans_lentille_au_moins_partout"]))
    v3 = [r3c1["verdict"], r3c2["verdict"]]
    non_so = [v for v in v3 if v != "sans objet"]
    lignes["A3 dépendance non lue dans chaque contraste non sans objet (au moins un)"] = bool(non_so) and all(v == "dépendance non lue" for v in non_so)
    if any(lignes.values()):
        return "n'apporte rien", lignes
    lignes["A1 retrouvée"] = r1["verdict"] == "retrouvée"
    lignes["S fait mieux sur A1"] = bool(r1["s_fait_mieux"])
    lignes["S fait mieux sur A2"] = bool(r2["s_fait_mieux"])
    lignes["A2 sans objet"] = bool(a2so)
    if lignes["A1 retrouvée"] and (lignes["S fait mieux sur A1"] or lignes["S fait mieux sur A2"]):
        if lignes["S fait mieux sur A1"] or not a2so:
            return "apporte quelque chose", lignes
        return "ambigu : « apporte quelque chose » si la voie A2 reste ouverte quand A2 est sans objet, « indéterminé » sinon", lignes
    return "indéterminé", lignes


def main(sortie):
    out = {"sources": {}, "plan": {"chemin": "docs/notes/neuron-lens-v1/lecture-volet-a/plan-de-lecture-v1.md",
                                   "sha256": sha("docs/notes/neuron-lens-v1/lecture-volet-a/plan-de-lecture-v1.md")},
           "versions": {"numpy": np.__version__, "python": sys.version.split()[0]}}
    import scipy
    out["versions"]["scipy"] = scipy.__version__
    cs, h = charger("brut-cas-sains")
    out["sources"]["brut-cas-sains.json"] = h
    out["cas_sains"] = cas_sains(cs)
    if not out["cas_sains"]["tous_passes"]:
        out["verdict_i"] = "chaîne en défaut"
        Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("chaîne en défaut : aucun verdict de mesure")
        return
    c = {}
    for nom in ("C3", "C1", "C2"):
        c[nom], out["sources"][f"brut-mesures-{nom}.json"] = charger(f"brut-mesures-{nom}")
        assert len(c[nom]["decoupes"]) == 5 and all(sorted(d) == sorted(COUCHES) for d in c[nom]["decoupes"])
    out["a1"] = a1(c["C2"])
    out["a2"] = a2(c["C1"])
    out["a3"] = {"C1": a3(c["C1"], "C1"), "C2": a3(c["C2"], "C2")}
    out["verdict_i"], out["verdict_i_lignes"] = verdict_i(False, out["a1"], out["a2"], out["a3"]["C1"], out["a3"]["C2"])
    out["aii"] = {nom: aii(c[nom], nom, i) for i, nom in enumerate(("C1", "C2", "C3"))}
    # déclencheurs de l'audit R4
    med = [out["a1"]["par_couche"][l]["rang_s_mediane"] for l in COUCHES]
    egaux = all(v <= 0.005 for nom in out["aii"] for v in out["aii"][nom]["ecart_abs_meilleur_k64_sonde_id"].values())
    decl = []
    if all(m == 1 for m in med) or egaux:
        decl.append("trop beau")
    if out["a1"]["verdict"] == "non retrouvée" and out["aii"]["C1"]["verdict"] == "n'apporte rien" \
            and out["aii"]["C3"]["verdict"] == "n'apporte rien":
        decl.append("tout négatif")
    out["audit"] = {"declencheurs": decl, "rangs_medians_a1": med, "a1_rang_1_toutes_couches": all(m == 1 for m in med),
                    "neurones_egaux_partout_definition_du_code": egaux,
                    "auc_sonde_c2_id": {l: out["aii"]["C2"]["couches"][l]["sonde_id"] for l in COUCHES},
                    "auc_sonde_c2_id_min_decoupe": {l: min(out["aii"]["C2"]["couches"][l]["sonde_id_par_decoupe"]) for l in COUCHES}}
    out["ecarts_entre_comparaison_exacte_et_arrondie"] = ECARTS_ARRONDI

    # ---------------- seulement maintenant : la sortie complète de la course, pour comparaison
    tout, h = charger("volet-a-brut")
    out["sources"]["volet-a-brut.json"] = h
    comp = {"cles": sorted(tout.keys()), "fumee": tout.get("fumee"),
            "mesures_identiques_aux_bruts": {nom: tout["mesures"][nom] == c[nom]["decoupes"] for nom in c},
            "cas_sains_identiques": tout["cas_sains"] == cs,
            "longueurs": {nom: tout.get(f"longueur_{nom}") for nom in c},
            "avertissements_convergence": tout.get("avertissements_convergence"),
            "info_chargement": tout.get("info_chargement"), "durees_s": tout.get("durees_s"),
            "audit_course": tout.get("audit"), "audit_trop_beau_present": "audit_trop_beau" in tout,
            "course": {"a1": tout.get("a1"), "classes_a1": tout.get("classes_a1"), "a2_sans_objet": tout.get("a2_sans_objet"),
                       "classes_a2": tout.get("classes_a2"), "a3": tout.get("a3"), "verdict_i": tout.get("verdict_i"),
                       "verdict_i_affiche": tout.get("verdict_i_affiche"),
                       "aii": {nom: {"verdict": tout["aii"][nom]["verdict"], "qualificatif": tout["aii"][nom]["qualificatif"]}
                               for nom in tout.get("aii", {})}}}
    comp["accords"] = {
        "a1": tout.get("a1") == out["a1"]["verdict"],
        "classes_a1": tout.get("classes_a1") == [out["a1"]["par_couche"][l]["classe"] for l in COUCHES],
        "a2_sans_objet": tout.get("a2_sans_objet") == out["a2"]["sans_objet"],
        "classes_a2": tout.get("classes_a2") == [out["a2"]["par_couche"][l]["classe"] for l in COUCHES],
        "a3": tout.get("a3") == [out["a3"]["C1"]["verdict"], out["a3"]["C2"]["verdict"]],
        "verdict_i": tout.get("verdict_i") == out["verdict_i"],
        "aii": {nom: (tout["aii"][nom]["verdict"] == out["aii"][nom]["verdict"]
                      and tout["aii"][nom]["qualificatif"] == out["aii"][nom]["qualificatif"]) for nom in tout.get("aii", {})},
        "audit": tout.get("audit") == decl}
    # bornes basses de la course contre mon recalcul (même graine)
    ecarts = []
    for nom in ("C1", "C2"):
        for i, l in enumerate(COUCHES):
            cc = tout["aii"][nom]["couches"][i]
            for k in BUDGETS:
                ecarts.append(abs(cc["borne_basse_ood"][k] - out["aii"][nom]["couches"][l]["intervalle_ood"][k][1]))
            ecarts.append(abs(cc["sonde_ood"] - out["aii"][nom]["couches"][l]["sonde_ood"]))
    comp["borne_basse_ood_ecart_max_course_contre_recalcul"] = max(ecarts)
    if "audit_trop_beau" in tout:
        at = tout["audit_trop_beau"]
        comp["audit_trop_beau"] = {"cles": sorted(at.keys()), "rangs_course_c2": at.get("rangs_course_c2"),
                                   "c2_sans_P": at.get("c2_sans_P"), "c2_sans_P_permutee": at.get("c2_sans_P_permutee"),
                                   "retrait_verifie": {k: {kk: vv for kk, vv in v.items() if kk not in ("chutes_aleatoires",)}
                                                       for k, v in at.get("retrait_verifie", {}).items()}}
        six = at.get("sixieme_decoupe", {})
        s = {}
        if "C2" in six:
            s["a1"] = {l: six["C2"][l]["a1"] for l in COUCHES}
        if "C1" in six:
            s["a2"] = {l: six["C1"][l]["a2"] for l in COUCHES}
        for nom in six:
            s[f"auc_{nom}"] = {l: {"sonde_id": six[nom][l]["auc_sonde_id"], "sonde_ood": six[nom][l].get("auc_sonde_ood"),
                                   "sac_id": six[nom][l]["auc_sac_id"],
                                   "neurones_id": {k: six[nom][l]["aii"]["id"][f"k{k}"] for k in BUDGETS},
                                   "neurones_ood": {k: six[nom][l]["aii"]["ood"].get(f"k{k}") for k in BUDGETS}} for l in COUCHES}
            if nom in ("C1", "C2"):
                s[f"a3_{nom}"] = {l: {kk: vv for kk, vv in six[nom][l]["a3"].items() if kk not in ("chutes_aleatoires", "jetons_s")}
                                  | {"centile_95": float(np.quantile(six[nom][l]["a3"]["chutes_aleatoires"], 0.95))
                                     if all(v is not None for v in six[nom][l]["a3"]["chutes_aleatoires"]) else None}
                                  for l in COUCHES}
        comp["audit_trop_beau"]["sixieme_decoupe"] = s
    out["comparaison_a_la_course"] = comp
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"cas_sains": out["cas_sains"]["tous_passes"], "a1": out["a1"]["verdict"], "a2_sans_objet": out["a2"]["sans_objet"],
                      "a2_nomme": out["a2"]["nomme"], "a3": {k: v["verdict"] for k, v in out["a3"].items()},
                      "s_mieux_a1": out["a1"]["s_fait_mieux"], "s_mieux_a2": out["a2"]["s_fait_mieux"],
                      "verdict_i": out["verdict_i"], "aii": {k: [v["verdict"], v["qualificatif"]] for k, v in out["aii"].items()},
                      "audit": decl, "accords": comp["accords"], "ecarts_arrondi": len(ECARTS_ARRONDI)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
