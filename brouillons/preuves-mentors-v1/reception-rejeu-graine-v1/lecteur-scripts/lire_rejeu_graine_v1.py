"""Lecture neuve du rejeu à graine de R1 (addendum v2, sha256 9d17d640…) — calculs du lecteur, sur la copie à l'octet.

Usage : python3 -I lire_rejeu_graine_v1.py RACINE_R
Ne lit que : textes-scelles/ (texte, configuration, table v2), copie/…/rejeu-graine-sortie-v1/ (sortie).
N'importe aucun module du dépôt ; recalcule tout à partir des champs des fichiers.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

R = Path(sys.argv[1])
S = R / "copie/brouillons/canal-reprise-releve-v1/envois/session-depot/rejeu-graine-sortie-v1"
DV = S / "diag/20261102-171752-r1-graine-validation"
DR = S / "diag/20261102-175806-r1-graine-resolution"
HEX = set("0123456789abcdef")
C6 = ["honnete/2512.05150v2/e0", "honnete/2512.11131v1/e0", "temoin/2510.24788v1/e0"]
QUATRE = ["honnete/2602.00987v1/e0", "mention/2605.17899v2/e0", "saboteur/2510.05132v3/e0", "temoin/2512.06870v2/e0"]
CLASSES = ("graines validées", "méthode transposée, graines non validées", "méthode non transposée")
CAUSE_BUDGET = "caractère de remplacement : budget de balayages dépassé"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def compagnon(p):
    return Path(f"{p}.sha256").read_text().split()[0]


def charge(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def est_empreinte(x):
    return isinstance(x, str) and len(x) == 64 and set(x) <= HEX


def resolu_recalcule(f):
    """Règle unique : résolu ssi l'empreinte de l'épisode reconstruit égale celle de P3 (champs du fichier)."""
    return est_empreinte(f.get("empreinte")) and est_empreinte(f.get("empreinte_cible")) \
        and f["empreinte"] == f["empreinte_cible"]


def categorie(f):
    c = f.get("cause") or ""
    if resolu_recalcule(f):
        return "résolu, voie " + str(f.get("voie"))
    if f.get("non_tente"):
        if c.startswith("durée : budget de l'étape"):
            return "non tenté : durée (budget de l'étape épuisé)"
        return "non tenté : autre"
    if c.startswith("durée : budget de l'épisode épuisé pendant le repli"):
        return "tenté, non résolu : durée pendant le repli"
    if c.startswith("durée"):
        return "tenté, non résolu : durée (autre)"
    if c.startswith(CAUSE_BUDGET):
        return "tenté, non résolu : budget de balayages"
    if c.startswith("contradiction"):
        return "tenté, non résolu : contradiction"
    return "tenté, non résolu : autre (" + c[:60] + ")"


def mesures(rows):
    """Comme `mesures_accord` du texte (« Métrique ») : contre le jeton retenu."""
    n = len(rows["choix"])
    if n == 0:
        return {"pas": 0}
    ok = rows["choix"] == rows["non_contraint"]
    inf = rows["choix"] != rows["argmax_p"]
    return {"pas": n, "accords": int(ok.sum()), "accord": float(ok.mean()), "somme_p_k": float(rows["p_k"].sum()),
            "attendu": float(rows["p_k"].mean()), "pas_informatifs": int(inf.sum()),
            "accords_informatifs": int((ok & inf).sum()), "somme_p_k_inf": float(rows["p_k"][inf].sum())}


def agreger(par_ep):
    m = [x for x in par_ep.values() if x["pas"]]
    n = sum(x["pas"] for x in m)
    ni = sum(x["pas_informatifs"] for x in m)
    return {"episodes_mesures": len(m), "pas": n,
            "accord_moyen_par_episode": float(np.mean([x["accord"] for x in m])) if m else None,
            "accord_min_par_episode": min((x["accord"] for x in m), default=None),
            "accord_sur_les_pas": sum(x["accords"] for x in m) / n if n else None,
            "attendu_graine_independante_moyen_par_episode": float(np.mean([x["attendu"] for x in m])) if m else None,
            "attendu_graine_independante_sur_les_pas": sum(x["somme_p_k"] for x in m) / n if n else None,
            "pas_informatifs": ni,
            "accord_informatif": sum(x["accords_informatifs"] for x in m) / ni if ni else None,
            "attendu_informatif": sum(x["somme_p_k_inf"] for x in m) / ni if ni else None}


def classe_regle_gelee(R_, E, acc, regle):
    """Règle de « Seuil » écrite en clair dans le texte scellé (réécrite ici, sans le code)."""
    if E == 0 or R_ < E:
        return CLASSES[2], None
    cond = {"accord_moyen": acc.get("accord_moyen_par_episode") is not None
            and acc["accord_moyen_par_episode"] >= regle["accord_moyen_min"],
            "accord_episode": acc.get("accord_min_par_episode") is not None
            and acc["accord_min_par_episode"] >= regle["accord_episode_min"],
            "pas_informatifs": acc.get("pas_informatifs") is not None
            and acc["pas_informatifs"] >= regle["pas_informatifs_min"],
            "accord_informatif": acc.get("accord_informatif") is not None
            and acc["accord_informatif"] >= regle["accord_informatif_min"]}
    return (CLASSES[0] if all(cond.values()) else CLASSES[1]), cond


def conditions_seules(acc, regle):
    return {"accord_moyen": acc["accord_moyen_par_episode"] >= regle["accord_moyen_min"],
            "accord_episode": acc["accord_min_par_episode"] >= regle["accord_episode_min"],
            "pas_informatifs": acc["pas_informatifs"] >= regle["pas_informatifs_min"],
            "accord_informatif": acc["accord_informatif"] >= regle["accord_informatif_min"]}


def declaration_texte(resolu, cause, classe):
    """« Seuil », Conséquences, et « Critères », ligne k non résolus (cœur seul)."""
    if resolu:
        return "résolu (empreinte de P3 retrouvée)"
    if classe != CLASSES[0]:
        return "non résolu, graines non validées : nœud porté à Lazar"
    if (cause or "").startswith(CAUSE_BUDGET):
        return "non inversible déclaré par la méthode (règle B)"
    return "non résolu par la méthode : nœud porté à Lazar"


def lignes_npz(chemin):
    z = np.load(chemin, allow_pickle=False)
    noms = [str(x) for x in z["episodes"]]
    cols = {k: z[k] for k in ("episode", "pas", "rang", "choix", "non_contraint", "candidats", "ecart", "second",
                              "marge", "balayage", "p_k", "argmax_p")}
    return noms, cols


def par_episode(noms, cols):
    out = {}
    for i, e in enumerate(noms):
        msk = cols["episode"] == i
        out[e] = {k: v[msk] for k, v in cols.items()}
    return out


def compte_sous(x, seuils=(0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0)):
    x = np.asarray([v for v in x if np.isfinite(v)], dtype=np.float64)
    return {"n": int(len(x)), "sous": {f"{s:g}": int((x < s).sum()) for s in seuils},
            "negatifs": int((x < 0).sum()), "min": float(x.min()) if len(x) else None}


sortie = {"lecteur": "lire_rejeu_graine_v1.py"}

# ---------------------------------------------------------------- pièces scellées
texte = R / "textes-scelles/R1-addendum-relance-v2.md"
config = charge(R / "textes-scelles/R1-graine-config-v1.json")
table_v2 = charge(R / "textes-scelles/R1-table-tokenisation-v2.json")
v2_par_ep = {x["episode"]: x for x in table_v2["episodes"]}
regle = config["regle_validation"]
sortie["empreintes_pieces"] = {"texte": sha(texte), "config": sha(R / "textes-scelles/R1-graine-config-v1.json"),
                               "table_v2": sha(R / "textes-scelles/R1-table-tokenisation-v2.json"),
                               "table_v3": sha(S / "prereg/R1-table-tokenisation-v3.json")}

# ---------------------------------------------------------------- manifestes : configuration identique au fichier scellé
for run in ("20261102-171752-r1-graine-validation", "20261102-175806-r1-graine-resolution"):
    m = charge(S / "runs" / run / "manifeste.json")
    sortie.setdefault("manifestes", {})[run] = {
        "config_egale_au_fichier_scelle": m["config"] == config, "config_sha256": m["config_sha256"],
        "commit": m["commit"], "prereg_sha256": m["preenregistrement"]["sha256"], "cree_le": m["cree_le"],
        "depot_propre": m["depot_propre"], "sceau_ok": sha(S / "runs" / run / "manifeste.json") ==
        compagnon(S / "runs" / run / "manifeste.json")}


def lire_etape(D, etape):
    res_f = D / f"resolution-graine-{etape}.json"
    corps = charge(res_f)
    r = corps["resultat"]
    consignes = r["episodes_consignes"]
    detail = {d["episode"]: d for d in r["episodes"]}
    fichiers = sorted((D / f"episodes-{etape}").glob("[0-9][0-9][0-9].json"))
    eps = []
    ecarts_ctrl = []
    for k, fp in enumerate(fichiers):
        f = charge(fp)
        c = consignes[k]
        ok_sceau = sha(fp) == compagnon(fp) == c["sha256"] and c["fichier"].endswith(fp.name) \
            and c["episode"] == f["episode"]
        rr = resolu_recalcule(f)
        d = detail[f["episode"]]
        coherent = (rr == (f["statut"] == "resolu") == bool(d["empreinte_retrouvee"]) == (d["statut"] == "resolu")
                    and d.get("empreinte") == f.get("empreinte"))
        v2 = v2_par_ep.get(f["episode"])
        cible_v2 = None if v2 is None else (v2["trajectoire_p3"] == f["empreinte_cible"])
        if not ok_sceau or not coherent or cible_v2 is False:
            ecarts_ctrl.append({"k": k, "episode": f["episode"], "sceau": ok_sceau, "coherent": coherent,
                                "cible_v2": cible_v2})
        eps.append({"k": k, "episode": f["episode"], "resolu": rr, "statut_ecrit": f["statut"],
                    "categorie": categorie(f), "cause": f.get("cause"), "voie": f.get("voie"),
                    "bascules": len(f.get("forcages") or []), "duree_s": f.get("duree_s"),
                    "passes_essai_direct": f.get("passes"), "combinaisons": f.get("combinaisons_essayees"),
                    "fffd": f.get("fffd"), "balayages_ecrits": f.get("balayages"),
                    "plafond_balayages": f.get("plafond_balayages"),
                    "methode_v2": None if v2 is None else v2["methode"], "cible_egale_v2": cible_v2,
                    "graines": f.get("graines"), "empreinte_cible": f["empreinte_cible"],
                    "empreinte": f.get("empreinte")})
    return corps, r, eps, ecarts_ctrl, res_f


sortie_etapes = {}
for etape, D in (("validation", DV), ("resolution", DR)):
    corps, r, eps, ecarts_ctrl, res_f = lire_etape(D, etape)
    noms, cols = lignes_npz(D / f"pas-resolution-graine-{etape}.npz")
    npz_ok = sha(D / f"pas-resolution-graine-{etape}.npz") == compagnon(D / f"pas-resolution-graine-{etape}.npz") \
        == r["pas_sha256"]
    pe = par_episode(noms, cols)
    par_ep = {e: mesures(rows) for e, rows in pe.items()}
    agr = agreger(par_ep)
    resolus = {x["episode"] for x in eps if x["resolu"]}
    agr_resolus = agreger({e: v for e, v in par_ep.items() if e in resolus})
    multi = cols["candidats"] > 1
    ecarts = cols["ecart"][multi]
    desacc = cols["choix"] != cols["non_contraint"]
    marges = cols["marge"][desacc]
    idx_resolus = np.array([noms[i] in resolus for i in cols["episode"]], dtype=bool)
    # désaccords à grande marge : dans les épisodes résolus ou non
    grandes = {s: {"resolus": int((desacc & idx_resolus & (cols["marge"] >= s)).sum()),
                   "non_resolus": int((desacc & ~idx_resolus & (cols["marge"] >= s)).sum())} for s in (0.5, 1.0, 2.0)}
    # pas forcés (écart négatif) : identifiés
    neg = [(noms[cols["episode"][i]], int(cols["pas"][i]), int(cols["rang"][i]), float(cols["ecart"][i]))
           for i in np.where(multi & (cols["ecart"] < 0))[0]]
    # balayages comptés dans les pas consignés (par épisode à U+FFFD)
    bal = {e: int(rows["balayage"].sum()) for e, rows in pe.items() if int(rows["balayage"].sum())}
    st = {"resultat_sha256": sha(res_f), "resultat_sceau_ok": sha(res_f) == compagnon(res_f), "npz_ok": npz_ok,
          "episodes": len(eps), "ecarts_de_controle": ecarts_ctrl,
          "resolus_recalcules": sum(x["resolu"] for x in eps),
          "ecrit_empreintes_retrouvees": r["empreintes_retrouvees"], "ecrit_directes": r["directes"],
          "ecrit_par_repli": r["par_repli"], "ecrit_par_repli_bascules": r["par_repli_bascules"],
          "ecrit_non_tentes": r["non_tentes"], "ecrit_non_resolus_duree": r["non_resolus_duree"],
          "categories": dict(Counter(x["categorie"] for x in eps)),
          "voies_resolus": {f"{v} ({b} bascule(s))": n for (v, b), n in
                            Counter((x["voie"], x["bascules"]) for x in eps if x["resolu"]).items()},
          "accords_recalcules": agr, "accords_ecrits": r["accord"],
          "accords_resolus_seuls_informatif": agr_resolus,
          "par_episode_accord": {e: {"accord": v.get("accord"), "attendu": v.get("attendu"), "pas": v["pas"],
                                     "pas_informatifs": v.get("pas_informatifs"),
                                     "accord_informatif": (v["accords_informatifs"] / v["pas_informatifs"])
                                     if v.get("pas_informatifs") else None,
                                     "attendu_informatif": (v["somme_p_k_inf"] / v["pas_informatifs"])
                                     if v.get("pas_informatifs") else None}
                                 for e, v in par_ep.items() if v["pas"]},
          "pas_total": int(len(cols["choix"])), "pas_multi_candidats": int(multi.sum()),
          "ecarts_contraints": compte_sous(ecarts), "ecarts_ecrits": r["ecarts_contraints"],
          "desaccords": int(desacc.sum()), "marges_en_desaccord": compte_sous(marges),
          "desaccords_grande_marge": grandes, "pas_forces_ecart_negatif": neg, "balayages_dans_les_pas": bal,
          "duree_etape_ecrite_s": r["duree_s"], "passes_ecrites": r["passes"],
          "erreurs_directes": r["erreurs_directes"]}
    if etape == "validation":
        st["lecture_validation_ecrite"] = r["lecture_validation"]
        st["lecture_ecrite"] = r["lecture"]
        st["corriges_table_v2_ecrit"] = r["corriges_table_v2"]
        cl, cond = classe_regle_gelee(st["resolus_recalcules"], len(eps), agr, regle)
        st["classe_recalculee"] = cl
        st["conditions_accord_recalculees"] = conditions_seules(agr, regle)
        st["classe_egale"] = cl == r["lecture_validation"]["classe"]
        st["corriges_v2_detail"] = [{"episode": x["episode"], "k": x["k"], "methode_v2": x["methode_v2"],
                                     "categorie": x["categorie"]}
                                    for x in eps if x["methode_v2"] not in (None, "non_resolu")]
        st["c6_dans_validation"] = [{"episode": x["episode"], "k": x["k"], "categorie": x["categorie"]}
                                    for x in eps if x["episode"] in C6]
        st["quatre_dans_validation"] = [x["episode"] for x in eps if x["episode"] in QUATRE]
        st["cibles_distinctes"] = len({x["empreinte_cible"] for x in eps}) == len(eps)
        # chronologie des épisodes tentés
        tentes = [x for x in eps if not x["categorie"].startswith("non tenté")]
        st["tentes"] = len(tentes)
        st["somme_durees_tentes_s"] = round(sum(x["duree_s"] for x in tentes), 2)
        par_cat = {}
        for x in tentes:
            c = x["categorie"]
            par_cat.setdefault(c, {"n": 0, "duree_s": 0.0})
            par_cat[c]["n"] += 1
            par_cat[c]["duree_s"] = round(par_cat[c]["duree_s"] + x["duree_s"], 2)
        st["durees_par_categorie"] = par_cat
        st["premier_non_tente"] = min((x["k"] for x in eps if x["categorie"].startswith("non tenté")), default=None)
        st["non_tentes_contigus_jusqu_a_la_fin"] = all(
            x["categorie"].startswith("non tenté") for x in eps if x["k"] >= (st["premier_non_tente"] or 10 ** 9))
        st["non_resolus_tentes"] = [{k2: x[k2] for k2 in ("k", "episode", "cause", "duree_s", "combinaisons",
                                                         "passes_essai_direct", "methode_v2")}
                                    for x in tentes if not x["resolu"]]
        st["tentes_detail"] = [{k2: x[k2] for k2 in ("k", "episode", "categorie", "duree_s", "combinaisons",
                                                    "bascules", "methode_v2")} for x in tentes]
        st["non_tentes_liste"] = [{"k": x["k"], "episode": x["episode"], "methode_v2": x["methode_v2"]}
                                  for x in eps if x["categorie"].startswith("non tenté")]
    else:
        st["lecture_ecrite"] = r["lecture"]
        st["controle_croise_ecrit"] = r["controle_croise"]
        st["controle_croise_lecture_ecrite"] = r["controle_croise_lecture"]
        st["lecture_validation_recopiee"] = r["lecture_validation"]
        st["declarations_ecrites"] = r["declarations"]
        classe = r["lecture_validation"]["classe"]
        st["declarations_recalculees"] = {x["episode"]: declaration_texte(x["resolu"], x["cause"], classe) for x in eps}
        # contrôle croisé recalculé : identifiants retrouvés = base + paires de la table v2 ?
        det = {d["episode"]: d for d in r["episodes"]}
        cc = []
        for e in C6:
            d = det[e]
            ent = v2_par_ep[e]
            base = [list(a) for a in d["base_nv"]]
            attendu = [list(a) for a in base]
            base_ok = True
            for p in ent["paires"]:
                t, s, can, p3 = p["pas"], p["rang"], p["canonique"], p["p3"]
                base_ok &= attendu[t][s:s + len(can)] == can
                attendu[t][s:s + len(can)] = p3
            for t, f_ in (ent.get("fins") or {}).items():
                attendu[int(t)][-1] = int(f_)
            emp_ok = d["empreinte"] == d["empreinte_cible"] == ent["trajectoire_p3"]
            egal = d["ids"] == attendu
            lecture = "conforme" if (emp_ok and egal) else ("non résolu" if not emp_ok else "contraire")
            cc.append({"episode": e, "methode_v2": ent["methode"], "base_coherente_avec_v2": base_ok,
                       "empreinte_retrouvee_et_egale_v2": emp_ok, "identifiants_egaux_v2_recalcule": egal,
                       "lecture": lecture, "voie": d["voie"], "forcages": d["forcages"]})
        st["controle_croise_recalcule"] = cc
        st["controle_croise_lecture_recalculee"] = ("conforme" if all(x["lecture"] == "conforme" for x in cc) else
                                                   "contraire" if any(x["lecture"] == "contraire" for x in cc) else
                                                   "non résolu")
        st["detail_resolution"] = [{k2: x[k2] for k2 in ("k", "episode", "resolu", "voie", "bascules", "duree_s",
                                                        "combinaisons", "fffd", "balayages_ecrits",
                                                        "plafond_balayages", "methode_v2", "cible_egale_v2")}
                                   for x in eps]
        st["_det"] = det
    sortie_etapes[etape] = st

# ---------------------------------------------------------------- table v3
t3p = S / "prereg/R1-table-tokenisation-v3.json"
t3 = charge(t3p)
det_res = sortie_etapes["resolution"].pop("_det")
v3_par_ep = {x["episode"]: x for x in t3["episodes"]}
compte_meth = Counter(x["methode"] for x in t3["episodes"])
anciennes = [e for e, x in v2_par_ep.items() if x["methode"] != "non_resolu"]
nouvelles = {}
for e in QUATRE:
    x = v3_par_ep[e]
    d = det_res[e]
    attendu = [{"pas": t, "canonique": b, "p3": v} for t, (b, v) in enumerate(zip(d["base_nv"], d["ids"])) if b != v]
    nouvelles[e] = {"methode": x["methode"], "trajectoire_egale_v2": x["trajectoire_p3"] == v2_par_ep[e]["trajectoire_p3"],
                    "trajectoire_egale_resultat": x["trajectoire_p3"] == d["empreinte"] == d["empreinte_cible"],
                    "actions_egales_au_resultat": x["actions"] == attendu, "actions_corrigees": [a["pas"] for a in x["actions"]],
                    "jetons_changes": sum(sum(1 for a_, b_ in zip(a["canonique"], a["p3"]) if a_ != b_)
                                          + abs(len(a["canonique"]) - len(a["p3"])) for a in x["actions"]),
                    "resolution_graine": x.get("resolution_graine")}
cles_v2_gardees = {e: {k: v for k, v in v3_par_ep[e].items()} == v2_par_ep[e] for e in anciennes}
sortie["table_v3"] = {
    "sha256": sha(t3p), "sceau_ok": sha(t3p) == compagnon(t3p), "version": t3["version"], "entrees": len(t3["episodes"]),
    "methodes": dict(compte_meth), "comptes_ecrits": t3["comptes"], "corrections_verifiees": t3["corrections_verifiees"],
    "non_resolu_entrees": sum(1 for x in t3["episodes"] if x["methode"] == "non_resolu"),
    "identiques_apres_table_recalcule": t3["comptes"]["identiques_base"] + sum(
        1 for x in t3["episodes"] if x["methode"] != "non_resolu"),
    "entrees_v2_gardees_telles_quelles": sum(cles_v2_gardees.values()), "entrees_v2_anciennes": len(anciennes),
    "nouvelles": nouvelles, "declarations": t3["declarations"],
    "declarations_egales_resultat": t3["declarations"] == sortie_etapes["resolution"]["declarations_ecrites"],
    "lecture_validation_classe": t3["lecture_validation"].get("classe"),
    "lecture_validation_egale_resultat": t3["lecture_validation"] == sortie_etapes["resolution"][
        "lecture_validation_recopiee"],
    "resultat_graine_sha256": t3["resultat_graine_sha256"],
    "resultat_graine_egal_resultat_resolution": t3["resultat_graine_sha256"] == sortie_etapes["resolution"][
        "resultat_sha256"],
    "table_v2_sha256_egale": t3["table_v2_sha256"] == sortie["empreintes_pieces"]["table_v2"],
    "resultat_hors_table": t3.get("resultat_hors_table"),
    "lecture_lot_presente": "lecture_lot" in t3 or "lecture_lot" in t3["lecture_validation"]}

# ---------------------------------------------------------------- audit de symétrie (déclencheurs écrits)
va = sortie_etapes["validation"]["accords_recalcules"]
classe = sortie_etapes["validation"]["classe_recalculee"]
sortie["audit_R4"] = {
    "accord_1_exactement_sur_tous_les_pas": sortie_etapes["validation"]["desaccords"] == 0,
    "aucune_quasi_egalite_sous_1": sortie_etapes["validation"]["ecarts_contraints"]["sous"]["1"] == 0,
    "duree_cumulee_etapes_0_et_1_s": sortie_etapes["validation"]["duree_etape_ecrite_s"]
    + sortie_etapes["resolution"]["duree_etape_ecrite_s"],
    "duree_sous_5_min": sortie_etapes["validation"]["duree_etape_ecrite_s"]
    + sortie_etapes["resolution"]["duree_etape_ecrite_s"] < 300,
    "accord_sur_les_pas": va["accord_sur_les_pas"],
    "attendu_sur_les_pas_plus_0_02": va["attendu_graine_independante_sur_les_pas"] + 0.02,
    "declencheur_pas": va["accord_sur_les_pas"] <= va["attendu_graine_independante_sur_les_pas"] + 0.02,
    "classe": classe, "declencheur_informatif_applicable": classe != CLASSES[0],
    "accord_informatif": va["accord_informatif"], "attendu_informatif_plus_0_10": va["attendu_informatif"] + 0.10,
    "declencheur_informatif": (classe != CLASSES[0]) and va["accord_informatif"] <= va["attendu_informatif"] + 0.10}

sortie["etapes"] = sortie_etapes
print(json.dumps(sortie, ensure_ascii=False, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))
