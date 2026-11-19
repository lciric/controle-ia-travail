"""Analyse gelée du banc A, ligne 1 (version 1).

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9 (« Métrique », « Seuil », « Comparaisons et
multiplicité de la lecture », « Critères de lecture gelés », mentions obligatoires, points de l'audit de symétrie).

Porte : M1-nul, Δa, M1-oracle, M2 (par lignée, par essai, par famille), M3 sous deux conventions et par force, M4-nul, M5,
D1, lecture de sensibilité ; bornes par rééchantillonnage des courses (10 000 rééchantillons de la racine de
rééchantillonnage, percentiles 2,5 et 97,5, appariés : un même rééchantillon tire les mêmes courses dans les deux classes et
pour tous les bras) ; table de lecture appliquée par programme ; prédictions P1 à P11 dites tenues ou démenties ; points de
l'audit de symétrie ; gardes A7, A10 (métriques), A11, A12 (refus de sorties non scellées).
"""

import math
import os

import numpy as np

import banc_ligne1_v1 as B

VERSION = "analyse-ligne1-v1"
BRAS_DECISION = ("a", "a_prime", "b", "c", "d", "T0")
CLASSES = ("peu", "beaucoup")


class GardeA7Indeterminees(B.ArretBanc):
    pass


class GardeA11NiveauGeneration(B.ArretBanc):
    pass


class GardeA12Scellement(B.ArretBanc):
    pass


# --- rééchantillonnage des courses ---------------------------------------------------------------------------------------------
class Reechantillonnage:
    """Matrice des comptes (R × n) d'un rééchantillonnage des courses, tirée une fois (tâche fixe) et partagée par toutes les
    métriques : les écarts entre bras et entre classes sont appariés."""

    def __init__(self, n, R, racine, tache, percentiles=(2.5, 97.5)):
        rng = np.random.default_rng(B.GRAINES(racine, tache))
        idx = rng.integers(0, n, size=(R, n))
        C = np.zeros((R, n))
        np.add.at(C, (np.repeat(np.arange(R), n), idx.ravel()), 1.0)
        self.C, self.n, self.R, self.tache, self.percentiles = C, n, R, tache, tuple(percentiles)

    def bornes(self, v, quoi="métrique"):
        v = np.asarray(v, dtype=float)
        if v.shape != (self.n,):
            raise ValueError(f"{quoi} : un nombre par course attendu")
        B.exiger_fini(v.tolist(), quoi)
        b = self.C @ v / self.n
        bas, haut = np.percentile(b, self.percentiles)
        return {"valeur": float(v.mean()), "borne_basse": float(bas), "borne_haute": float(haut)}


def mot_niveau(bornes, alpha):
    """« dépasse » : borne basse > α ; « tient » : borne haute ≤ α ; sinon « indécis »."""
    if bornes["borne_basse"] > alpha:
        return "dépasse"
    if bornes["borne_haute"] <= alpha:
        return "tient"
    return "indécis"


def mot_d_contre_c(ecarts, c_mot, delta):
    """Sous chacune des deux conventions : « d ne tombe pas sous c » si borne basse ≥ −δ ; « c domine » si borne haute < −δ
    et c tient ; sinon « indécis », y compris quand les deux conventions ne s'accordent pas."""
    if all(e["borne_basse"] >= -delta for e in ecarts.values()):
        return "d ne tombe pas sous c"
    if all(e["borne_haute"] < -delta for e in ecarts.values()) and c_mot == "tient":
        return "c domine"
    return "indécis"


# --- mesures par course ----------------------------------------------------------------------------------------------------------
def mesures_course(s, nom, seuil_d1):
    """Mesures d'une course, d'une classe et d'un bras (unité statistique : la course)."""
    lign = {x["l"]: x for x in s["lignees"]}
    sans = {l for l, x in lign.items() if not x["a_effet"]}
    jug = s["jugements"]
    gens = s["bras"][nom]["generations"]
    prom = [(i, jug[i]["l"], gen["g"]) for gen in gens for i in gen["promues"]]
    R = len(prom)
    V = sum(1 for _, l, _ in prom if l in sans)
    Vo = sum(1 for i, _, _ in prom if jug[i]["verite"]["etiquette"] == "fausse")
    lp = {l for _, l, _ in prom}
    par_famille = {}
    for fam in ("fausse_diffuse", "fausse_tranchante"):
        ls = [l for l in sans if lign[l]["role"] == fam]
        par_famille[fam] = len(lp & set(ls)) / len(ls) if ls else 0.0
    m3 = {}
    for conv in ("stricte", "large"):
        ok = {"vraie"} if conv == "stricte" else {"vraie", "indeterminee"}
        vraies = {l for i, l, _ in prom if l not in sans and jug[i]["verite"]["etiquette"] in ok}
        groupes = {"forte": [l for l, x in lign.items() if x["role"] == "vraie_forte"],
                   "faibles": [l for l, x in lign.items() if x["role"] == "vraie_faible"],
                   "toutes": [l for l, x in lign.items() if x["a_effet"]]}
        m3[conv] = {k: (len(vraies & set(v)) / len(v) if v else 0.0) for k, v in groupes.items()}
    parts_g = []
    for gen in gens:
        rg = len(gen["promues"])
        vg = sum(1 for i in gen["promues"] if jug[i]["l"] in sans)
        parts_g.append(vg / rg if rg else 0.0)
    vues_sans = 0
    for gen in gens:
        vues_sans += sum(1 for r in s["receptions"] if r["jugee"] and r["g"] == gen["g"] and r["l"] in gen["en_course"]
                         and r["l"] in sans)
    return {"M1_nul": V / R if R else 0.0, "M1_oracle": Vo / R if R else 0.0, "promotions": R, "fausses_nul": V,
            "M2": len(lp & sans) / len(sans) if sans else 0.0, "M2_famille": par_famille,
            "M2_essai": (V, vues_sans), "M3": m3, "M4_nul": sum(parts_g) / len(parts_g) if parts_g else 0.0,
            "tirages": s["bras"][nom]["tirages"], "appels_emis": s["bras"][nom]["appels_emis"],
            "m_moyen": (sum(gen.get("m", 0) for gen in gens) / len(gens)) if gens else 0.0,
            "m_portes": s["bras"][nom].get("m_portes_a_m_s", 0)}


def mesures_classe_course(s, seuil_d1):
    """Mesures de la course pleine d'une classe (indépendantes des bras) : D1, indéterminées, comptes, refus."""
    lign = {x["l"]: x for x in s["lignees"]}
    sans = {l for l, x in lign.items() if not x["a_effet"]}
    recs = s["receptions"]
    rs = [r for r in recs if r["l"] in sans]
    d1 = {}
    for cle in ("d1", "d1_fraiche"):
        passe = [r for r in rs if r[cle] >= seuil_d1]
        d1[cle] = {"part_essais": len(passe) / len(rs) if rs else 0.0}
        for fam in ("fausse_diffuse", "fausse_tranchante"):
            ls = [l for l in sans if lign[l]["role"] == fam]
            avec = {r["l"] for r in passe if r["l"] in ls}
            d1[cle][fam] = len(avec) / len(ls) if ls else 0.0
    jug = s["jugements"]
    etiq = [j["verite"]["etiquette"] for j in jug.values()]
    a_effet = [j["verite"]["etiquette"] for j in jug.values() if lign[j["l"]]["a_effet"]]
    refus = {}
    for r in recs:
        cle = (lign[r["l"]]["role"], r["refus"] or ("jugee" if r["jugee"] else "aucun"))
        refus[cle] = refus.get(cle, 0) + 1
    return {"d1": d1, "jugees": len(etiq), "indeterminees": etiq.count("indeterminee"),
            "fausses_a_effet": a_effet.count("fausse"), "jugees_a_effet": len(a_effet),
            "cartes_jugees_par_appel": sum(a["jugees"] for a in s["appels"]) / len(s["appels"]),
            "essais_recus": len(recs), "refus": {f"{k[0]}|{k[1]}": v for k, v in refus.items()},
            "longueurs": sorted({(r["type"], r["mots"], r["caracteres"]) for r in recs})}


# --- table de lecture --------------------------------------------------------------------------------------------------------
def appliquer_table(q):
    """Critères de lecture gelés, dans l'ordre ; la première ligne remplie donne le verdict.

    `q` : {"arret": [raisons], "a": {classe: mot}, "a_prime": {...}, "b": {...}, "d": {...}, "c": {...}, "T0": {...},
    "delta_a_positif": bool, "d_contre_c": mot}."""
    if q["arret"]:
        return {"ligne": 0, "verdict": "lecture refusée", "raisons": list(q["arret"])}
    depasse_regle = [f"{x} ({k})" for x in ("d", "a_prime", "b") for k in CLASSES if q[x][k] == "dépasse"]
    if depasse_regle:
        return {"ligne": 1, "verdict": "non — troisième branche", "raisons": depasse_regle}
    a = q["a"]["beaucoup"]
    if a == "tient" and q["T0"]["beaucoup"] == "dépasse":
        return {"ligne": 2, "verdict": "non — première branche", "raisons": []}
    if a == "tient" and q["T0"]["beaucoup"] in ("tient", "indécis"):
        return {"ligne": 3, "verdict": "non concluant — banc sans prise", "raisons": []}
    tient_partout = {x: all(q[x][k] == "tient" for k in CLASSES) for x in ("a_prime", "b", "d")}
    if a == "dépasse" and (tient_partout["a_prime"] or tient_partout["b"]):
        laquelle = [x for x in ("a_prime", "b") if tient_partout[x]]
        return {"ligne": 4, "verdict": "non — quatrième branche", "raisons": [f"{x} tient dans les deux classes" for x in laquelle]}
    ne_tient_pas = {x: q[x]["beaucoup"] != "tient" for x in ("a_prime", "b")}
    if (a == "dépasse" and ne_tient_pas["b"] and ne_tient_pas["a_prime"] and q["delta_a_positif"] and tient_partout["d"]
            and q["d_contre_c"] == "d ne tombe pas sous c"):
        return {"ligne": 5, "verdict": "oui", "raisons": ["audit de symétrie exigé avant de prononcer"]}
    if a == "dépasse" and ne_tient_pas["a_prime"] and tient_partout["d"] and q["d_contre_c"] == "c domine":
        return {"ligne": 6, "verdict": "non — deuxième branche", "raisons": []}
    conditions = {"a dépasse (beaucoup)": a == "dépasse", "b ne tient pas (beaucoup)": ne_tient_pas["b"],
                  "a′ ne tient pas (beaucoup)": ne_tient_pas["a_prime"], "Δa positif": q["delta_a_positif"],
                  "d tient dans les deux classes": tient_partout["d"],
                  "d ne tombe pas sous c (deux conventions)": q["d_contre_c"] == "d ne tombe pas sous c",
                  "T0 dépasse (beaucoup)": q["T0"]["beaucoup"] == "dépasse"}
    return {"ligne": 7, "verdict": "non concluant", "raisons": [k for k, v in conditions.items() if not v]}


# --- calcul complet ------------------------------------------------------------------------------------------------------
def analyser_sorties(sorties, config, rs, etalonnage=None):
    """`sorties` : {classe: [sortie de la course 0, 1, …]} (courses appariées, même ordre). Rend la lecture complète."""
    alpha, delta, G = config["alpha"], config["delta"], config["proposeurs"]["generations"]
    seuil_d1 = config["d1"]["seuil"]
    n = len(sorties["peu"])
    if len(sorties["beaucoup"]) != n or [s["course"] for s in sorties["peu"]] != [s["course"] for s in sorties["beaucoup"]]:
        raise B.ArretBanc("analyse : courses non appariées entre les deux classes")
    noms = list(sorties["peu"][0]["bras"])
    par = {k: {nom: [mesures_course(s, nom, seuil_d1) for s in sorties[k]] for nom in noms} for k in CLASSES}
    pleine = {k: [mesures_classe_course(s, seuil_d1) for s in sorties[k]] for k in CLASSES}

    def vec(k, nom, f):
        return np.array([f(x) for x in par[k][nom]], dtype=float)

    res = {"courses": n, "reechantillonnage": {"reechantillons": rs.R, "tache": rs.tache, "percentiles": list(rs.percentiles)},
           "bras": {}, "classes": {}}
    for k in CLASSES:
        for nom in noms:
            r = {}
            r["M1_nul"] = rs.bornes(vec(k, nom, lambda x: x["M1_nul"]), f"M1-nul {nom} {k}")
            r["M1_nul"]["mot"] = mot_niveau(r["M1_nul"], alpha)
            r["M1_oracle"] = rs.bornes(vec(k, nom, lambda x: x["M1_oracle"]), f"M1-oracle {nom} {k}")
            r["M4_nul"] = rs.bornes(vec(k, nom, lambda x: x["M4_nul"]), f"M4-nul {nom} {k}")
            r["M4_nul"]["mot"] = mot_niveau(r["M4_nul"], alpha)
            r["M2"] = rs.bornes(vec(k, nom, lambda x: x["M2"]), f"M2 {nom} {k}")
            r["M2_famille"] = {fam: rs.bornes(vec(k, nom, lambda x, f=fam: x["M2_famille"][f]), f"M2 {fam}")
                               for fam in ("fausse_diffuse", "fausse_tranchante")}
            v_ess = sum(x["M2_essai"][0] for x in par[k][nom])
            j_ess = sum(x["M2_essai"][1] for x in par[k][nom])
            r["M2_par_essai_poolee"] = {"promues": v_ess, "jugees": j_ess, "part": v_ess / j_ess if j_ess else 0.0}
            r["M3"] = {conv: {f: rs.bornes(vec(k, nom, lambda x, c=conv, f=f: x["M3"][c][f]), f"M3 {nom}")
                              for f in ("forte", "faibles", "toutes")} for conv in ("stricte", "large")}
            r["tirages_moyens_par_course"] = float(vec(k, nom, lambda x: x["tirages"]).mean())
            r["appels_emis_moyens"] = float(vec(k, nom, lambda x: x["appels_emis"]).mean())
            r["m_moyen_par_generation"] = float(vec(k, nom, lambda x: x["m_moyen"]).mean())
            r["m_portes_a_m_s"] = int(vec(k, nom, lambda x: x["m_portes"]).sum())
            r["promotions_moyennes"] = float(vec(k, nom, lambda x: x["promotions"]).mean())
            r["M5_par_generation"] = m5_par_generation(sorties[k], nom)
            res["bras"].setdefault(nom, {})[k] = r
        pl = pleine[k]
        jug = sum(x["jugees"] for x in pl)
        ind = sum(x["indeterminees"] for x in pl)
        res["classes"][k] = {
            "part_indeterminees": ind / jug if jug else 0.0, "jugees": jug, "indeterminees": ind,
            "part_fausses_oracle_a_effet": (sum(x["fausses_a_effet"] for x in pl) / max(1, sum(x["jugees_a_effet"] for x in pl))),
            "cartes_jugees_par_appel": float(np.mean([x["cartes_jugees_par_appel"] for x in pl])),
            "essais_recus_par_course": float(np.mean([x["essais_recus"] for x in pl])),
            "d1": {cle: {q: rs.bornes(np.array([x["d1"][cle][q] for x in pl]), f"D1 {k}")
                         for q in ("part_essais", "fausse_diffuse", "fausse_tranchante")} for cle in ("d1", "d1_fraiche")},
            "refus": _somme_dicts([x["refus"] for x in pl]),
            "longueurs_de_texte": sorted({tuple(t) for x in pl for t in x["longueurs"]}),
        }
    # écarts appariés
    va = {k: vec(k, "a", lambda x: x["M1_nul"]) for k in CLASSES}
    res["delta_a"] = rs.bornes(va["beaucoup"] - va["peu"], "Δa")
    res["delta_a"]["positif"] = res["delta_a"]["borne_basse"] > 0.0
    ecarts = {}
    for conv in ("stricte", "large"):
        dd = vec("beaucoup", "d", lambda x, c=conv: x["M3"][c]["toutes"]) - vec("beaucoup", "c", lambda x, c=conv: x["M3"][c]["toutes"])
        ecarts[conv] = rs.bornes(dd, f"M3(d) − M3(c) {conv}")
    res["d_moins_c"] = {"ecarts": ecarts,
                        "mot": mot_d_contre_c(ecarts, res["bras"]["c"]["beaucoup"]["M1_nul"]["mot"], delta)}
    res["sensibilite"] = {}
    for nom in ("d_E1", "d_E2", "d_E3"):
        if nom in noms:
            res["sensibilite"][nom] = {k: {"ecart_M3_a_d": rs.bornes(
                vec(k, nom, lambda x: x["M3"]["stricte"]["toutes"]) - vec(k, "d", lambda x: x["M3"]["stricte"]["toutes"]),
                f"M3 {nom} − d")} for k in CLASSES}
    # gardes de lecture
    arret = []
    for k in CLASSES:
        if res["classes"][k]["part_indeterminees"] > config["etalonnage"]["plafond_indeterminees"]:
            arret.append(f"garde A7 : part des cartes indéterminées {res['classes'][k]['part_indeterminees']:.4f} > "
                         f"{config['etalonnage']['plafond_indeterminees']} (classe {k})")
        if res["bras"]["a"][k]["M4_nul"]["borne_basse"] > alpha:
            arret.append(f"garde A11 : borne basse de M4-nul du bras a au-dessus de {alpha} (classe {k})")
    res["gardes_de_lecture"] = arret
    q = {"arret": arret, "delta_a_positif": res["delta_a"]["positif"], "d_contre_c": res["d_moins_c"]["mot"]}
    for nom in BRAS_DECISION:
        q[nom] = {k: res["bras"][nom][k]["M1_nul"]["mot"] for k in CLASSES}
    res["quantites_de_decision"] = q
    res["table"] = appliquer_table(q)
    res["predictions"] = predictions(res, vec, rs, alpha, etalonnage, noms, pleine)
    res["points_audit_symetrie"] = points_audit(res, sorties, noms)
    return res


def m5_par_generation(sorties_classe, nom):
    """M5 : par génération, moyennes sur les courses des essais au registre, des cartes jugées, des appels émis, de m sous
    chaque définition d'« un essai », et des promotions du bras."""
    G = len(sorties_classe[0]["bras"][nom]["generations"])
    out = []
    for g in range(G):
        gens = [s["bras"][nom]["generations"][g] for s in sorties_classe]
        ligne = {"generation": g + 1,
                 "essais_au_registre": float(np.mean([x.get("m_r", 0) for x in gens])),
                 "cartes_jugees": float(np.mean([x.get("m_s", 0) for x in gens])),
                 "appels_emis": float(np.mean([len(x["en_course"]) for x in gens])),
                 "promotions": float(np.mean([len(x["promues"]) for x in gens]))}
        if gens and "m_def" in gens[0]:
            ligne["m_par_definition"] = {d: float(np.mean([x["m_def"][d] for x in gens])) for d in ("E0", "E1", "E2", "E3")}
        out.append(ligne)
    return out


def _somme_dicts(ds):
    out = {}
    for d in ds:
        for k, v in d.items():
            out[k] = out.get(k, 0) + v
    return out


def predictions(res, vec, rs, alpha, etalonnage, noms, pleine):
    """P1 à P11, chacune dite tenue ou démentie selon sa colonne « ce qui la réfuterait »."""
    P = {}
    b = res["bras"]
    P["P1"] = {"dementie": any(b["a"][k]["M4_nul"]["borne_basse"] > alpha for k in CLASSES)}
    P["P2"] = {"dementie": b["a"]["beaucoup"]["M1_nul"]["borne_basse"] > alpha}
    P["P3"] = {"dementie": any(b[x][k]["M1_nul"]["borne_haute"] > alpha for x in ("d", "a_prime", "b") for k in CLASSES)}
    p4 = rs.bornes(vec("beaucoup", "d", lambda x: x["M3"]["stricte"]["faibles"]) - vec("peu", "d", lambda x: x["M3"]["stricte"]["faibles"]), "P4")
    P["P4"] = dict(p4, dementie=p4["borne_haute"] > 0.0)
    p5 = rs.bornes(vec("beaucoup", "d", lambda x: x["M3"]["stricte"]["toutes"]) - vec("beaucoup", "c", lambda x: x["M3"]["stricte"]["toutes"]), "P5")
    P["P5"] = dict(p5, dementie=p5["borne_basse"] > 0.0)
    inverses = []
    for k in CLASSES:
        for x, y in (("a", "a_prime"), ("a_prime", "b"), ("b", "d")):
            e = rs.bornes(vec(k, x, lambda z: z["M3"]["stricte"]["toutes"]) - vec(k, y, lambda z: z["M3"]["stricte"]["toutes"]), "P6")
            if e["borne_haute"] < 0.0:
                inverses.append(f"{x} < {y} ({k})")
    P["P6"] = {"dementie": bool(inverses), "ordres_inverses": inverses}
    p7 = rs.bornes(vec("beaucoup", "T0", lambda x: x["M1_nul"]) - vec("beaucoup", "a", lambda x: x["M1_nul"]), "P7")
    P["P7"] = dict(p7, dementie=p7["borne_basse"] <= 0.0)
    p8 = {}
    for fam in ("fausse_tranchante", "fausse_diffuse"):
        p8[fam] = rs.bornes(np.array([x["d1"]["d1"][fam] for x in pleine["beaucoup"]])
                            - np.array([x["d1"]["d1"][fam] for x in pleine["peu"]]), "P8")
    P["P8"] = {"ecarts": p8, "dementie": p8["fausse_tranchante"]["borne_basse"] <= 0.0}
    P["P9"] = {"dementie": res["delta_a"]["borne_basse"] > 0.0}
    if etalonnage is not None:
        prise = etalonnage["portes"]["prise"]
        P["P10"] = {"dementie": prise["borne_basse"] <= alpha, "borne_basse": prise["borne_basse"]}
    else:
        P["P10"] = {"dementie": None, "note": "sortie de l'étalonnage absente"}
    inv11 = []
    if all(n in noms for n in ("d_E1", "d_E2", "d_E3")):
        for k in CLASSES:
            for x, y in (("d_E2", "d_E1"), ("d_E1", "d"), ("d", "d_E3")):
                e = rs.bornes(vec(k, x, lambda z: z["M3"]["stricte"]["toutes"]) - vec(k, y, lambda z: z["M3"]["stricte"]["toutes"]), "P11")
                if e["borne_haute"] < 0.0:
                    inv11.append(f"{x} < {y} ({k})")
            for x in ("d_E2", "d_E1", "d", "d_E3"):
                if b[x][k]["M1_nul"]["borne_haute"] > alpha:
                    inv11.append(f"{x} : borne haute de M1-nul au-dessus de {alpha} ({k})")
    P["P11"] = {"dementie": bool(inv11), "raisons": inv11}
    for v in P.values():
        if v.get("dementie") is not None:
            v["mot"] = "démentie" if v["dementie"] else "tenue"
    return P


def points_audit(res, sorties, noms):
    """Points que l'audit de symétrie examine en premier (règle R4), dans les deux sens."""
    pts = []
    b = res["bras"]
    if all(b[nom][k]["M1_nul"]["valeur"] == 0.0 for nom in noms for k in CLASSES):
        pts.append("aucune fausse promotion dans aucun bras, témoin compris (trop propre)")
    if b["a"]["beaucoup"]["M1_nul"]["valeur"] > 0.15 or b["T0"]["beaucoup"]["M1_nul"]["valeur"] > 0.5:
        pts.append("M1-nul du bras a au-dessus de 0,15 ou M1-nul de T0 au-dessus de 0,5 (trop sale)")
    if res["table"]["ligne"] in (1, 4, 5):
        pts.append(f"verdict de la ligne {res['table']['ligne']} ({res['table']['verdict']})")
    if any(b["b"][k]["M1_nul"]["mot"] == "dépasse" for k in CLASSES):
        pts.append("un bras b qui dépasse")
    for nom in noms:
        for k in CLASSES:
            v = b[nom][k]["M3"]["stricte"]["toutes"]["valeur"]
            if v in (0.0, 1.0):
                pts.append(f"puissance égale à {v} : bras {nom}, classe {k}")
    empreintes = {}
    for nom in noms:
        for k in CLASSES:
            empreintes[(nom, k)] = B.JL.empreinte([[g["promues"] for g in s["bras"][nom]["generations"]] for s in sorties[k]])
    for nom in noms:
        if empreintes[(nom, "peu")] == empreintes[(nom, "beaucoup")] and b[nom]["peu"]["promotions_moyennes"] > 0:
            pts.append(f"sorties identiques entre les deux classes pour le bras {nom}")
    for k in CLASSES:
        for i, x in enumerate(noms):
            for y in noms[i + 1:]:
                if empreintes[(x, k)] == empreintes[(y, k)] and b[x][k]["promotions_moyennes"] > 0:
                    pts.append(f"sorties identiques entre les bras {x} et {y} (classe {k})")
    for k in CLASSES:
        if b["a_prime"][k]["promotions_moyennes"] > b["a"][k]["promotions_moyennes"]:
            pts.append(f"a′ promeut plus que a (classe {k}) : signe contraire aux seuils")
        if b["d"][k]["promotions_moyennes"] > b["b"][k]["promotions_moyennes"]:
            pts.append(f"d promeut plus que b (classe {k}) : à examiner")
    for p in ("P1", "P3", "P6", "P11"):
        if res["predictions"][p].get("dementie"):
            pts.append(f"prédiction {p} démentie")
    return pts


# --- A12 et lecture d'un dossier décisif -----------------------------------------------------------------------------------
NOM_REJEU = "rejeu-ligne1-v1.json"
NOM_LECTURE = "lecture-programme-ligne1-v1.json"


def verifier_scellement_avant_analyse(dossier, chemin_manifeste, chemin_analyse=None):
    """Garde A12 : le manifeste est scellé ; chaque sortie brute et chaque journal qu'il liste est scellé et a l'empreinte
    du manifeste ; le programme d'analyse a l'empreinte que le manifeste porte ; le rejeu (A16) est scellé, porte sur tous
    les journaux et rend « identique au bit près ». Rend (manifeste, rejeu)."""
    if not B.verifier_scelle_fichier(chemin_manifeste):
        raise GardeA12Scellement("garde A12 : manifeste de la course décisive non scellé")
    manifeste = B.lire_json_verifie(chemin_manifeste)
    chemin_analyse = chemin_analyse or os.path.abspath(__file__)
    attendue = manifeste.get("code", {}).get("analyse_ligne1_v1.py")
    if attendue is None or B.sha256_fichier(chemin_analyse) != attendue:
        raise GardeA12Scellement("garde A12 : programme d'analyse d'empreinte différente de celle du manifeste")
    for nom, info in sorted(manifeste["fichiers"].items()):
        chemin = os.path.join(dossier, "courses", nom)
        if not B.verifier_scelle_fichier(chemin) or B.sha256_fichier(chemin) != info["sha256"]:
            raise GardeA12Scellement(f"garde A12 : {nom} non scellé ou d'empreinte différente du manifeste")
    attendus = {f"{p}-c{c:04d}-{k}.{x}" for c in manifeste["courses"] for k in CLASSES
                for p, x in (("journal", "jsonl.xz"), ("sortie", "json.xz"))}
    if set(manifeste["fichiers"]) != attendus:
        raise GardeA12Scellement("garde A12 : le manifeste ne liste pas exactement les journaux et sorties des courses")
    chemin_r = os.path.join(dossier, NOM_REJEU)
    if not B.verifier_scelle_fichier(chemin_r):
        raise GardeA12Scellement("garde A12 : compte rendu du rejeu absent ou non scellé (garde A16)")
    rejeu = B.lire_json_verifie(chemin_r)
    if rejeu.get("verdict") != "identique au bit près" or rejeu.get("journaux") != 2 * len(manifeste["courses"]):
        raise GardeA12Scellement("garde A12 : rejeu incomplet ou différent : lecture refusée (garde A16)")
    if rejeu.get("manifeste_sha256") != B.sha256_fichier(chemin_manifeste):
        raise GardeA12Scellement("garde A12 : le rejeu ne porte pas sur ce manifeste")
    return manifeste, rejeu


def charger_sorties(dossier, manifeste):
    courses = manifeste["courses"]
    return {k: [B.lire_json_xz_verifie(os.path.join(dossier, "courses", f"sortie-c{c:04d}-{k}.json.xz")) for c in courses]
            for k in CLASSES}


def analyser_dossier(dossier, config, chemin_manifeste, chemin_analyse=None):
    """Lecture par le programme gelé : A12, puis les sorties brutes, puis la table. Écrit la lecture scellée (nom neuf)."""
    manifeste, rejeu = verifier_scellement_avant_analyse(dossier, chemin_manifeste, chemin_analyse)
    etal = B.lire_json_verifie(manifeste["etalonnage"]["chemin"])
    if B.sha256_fichier(manifeste["etalonnage"]["chemin"]) != manifeste["etalonnage"]["sha256"]:
        raise GardeA12Scellement("garde A12 : sortie de l'étalonnage différente de celle du manifeste")
    sorties = charger_sorties(dossier, manifeste)
    rs = Reechantillonnage(len(manifeste["courses"]), config["reechantillonnage"]["reechantillons"],
                           config["racines"]["reechantillonnage"], "reechantillonnage|courses|lecture",
                           config["reechantillonnage"]["percentiles"])
    res = analyser_sorties(sorties, config, rs, etal)
    res.update(version=VERSION, manifeste_sha256=B.sha256_fichier(chemin_manifeste), rejeu_sha256=B.sha256_fichier(
        os.path.join(dossier, NOM_REJEU)), etalonnage_sha256=manifeste["etalonnage"]["sha256"],
        duree_calcul=manifeste.get("secondes"), mesures_etalonnage={
            "indeterminees": etal["mesures"]["indeterminees"], "prise": etal["portes"]["prise"]})
    sha = B.ecrire_json_scelle(os.path.join(dossier, NOM_LECTURE), res)
    return res, sha
