#!/usr/bin/env python3
"""Analyse préenregistrée de nos journaux pour la table de décision Re-Search — v1 (analyste : modèle I).

Applique le préenregistrement scellé
docs/notes/organisme-re-search-v1/preenregistrement-analyse-journaux-organisme-re-search-v1.md (mesures M1 à M4), avec les
définitions opératoires écrites avant calcul dans docs/notes/organisme-re-search-v1/analyse-journaux-re-search-v1.md,
section 1. Lit les sources par chemins passés en argument, recalcule leurs empreintes et refuse (code 2, rien écrit) si
l'une diffère de l'empreinte attendue. Graines : numpy.random.SeedSequence(20261118), une graine fille par tâche (R9).
Aucun appel réseau, aucun appel de modèle. Ne qualifie jamais une carte par le verdict du juge (N-058) : le verdict est
rapporté à côté ; en S2, l'événement « promue » n'est qualifié de fausse promotion que là où le monde la rend fausse par
construction.

Usage :
  python3 -I analyse_journaux_re_search_v1.py --s1-boucle F --s1-lecture F --s2a F --s2a-manifeste F --s2b F
      --s2b-manifeste F --sortie SORTIE.json [--empreintes-attendues ESSAI.json]
L'option --empreintes-attendues ne sert qu'aux essais (R5) : elle remplace les empreintes attendues par celles d'un
fichier JSON {clé: sha256} ; la sortie porte alors "essai": true et les empreintes réellement attendues ne sont pas
déclarées vérifiées.
"""
import argparse
import hashlib
import json
import math
import platform
import sys

import numpy as np

VERSION = "analyse-journaux-re-search-v1"
RACINE_GRAINES = 20261118
TIRAGES = 10_000
SEUIL_PLATEAU = 0.5
SEUIL_MODE = 0.25
PART_PRECOCE = 0.3

EMPREINTES = {
    "s1_boucle": "21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71",
    "s1_lecture": "d0ef1ee7667bdc665747c2822dcb031abfea3b38b3094782ad72ae593c016086",
    "s2a": "e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505",
    "s2a_manifeste": "8180db228ead856fac28e9f002a8324b909f9f69411f42bac5a7c96ad5007d84",
    "s2b": "cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf",
    "s2b_manifeste": "81f40feb7d38cb2241e45af80950913cc74ad24ae0ae484f50250fd1f5fedcd8",
}

# Vérité du monde, par source et par monde (section 1 de la note) : « fausse » = toute promotion y est fausse par
# construction ; « non_definie » = le monde porte une loi neuve mais la source n'écrit aucune vérité par loi proposée.
VERITE_DES_MONDES = {
    "s2a": {"W1": "fausse_par_construction", "W2": "fausse_par_construction"},
    "s2b": {"W2": "fausse_par_construction", "W2g": "non_definie"},
}


class Refus(Exception):
    pass


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def charger(chemins, attendues):
    lus, empreintes = {}, {}
    for cle, chemin in chemins.items():
        e = sha256_fichier(chemin)
        if e != attendues[cle]:
            raise Refus(f"empreinte de {cle} ({chemin}) : {e} ≠ attendue {attendues[cle]}")
        empreintes[cle] = {"chemin": chemin, "sha256": e}
    for cle, chemin in chemins.items():
        if cle.endswith("_manifeste"):
            continue  # vérifié par empreinte seulement
        with open(chemin, encoding="utf-8") as f:
            lus[cle] = json.load(f)
    return lus, empreintes


# --- formes ---------------------------------------------------------------------------------------------------------------
def forme(o):
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return o
    if isinstance(o, (int, float)):
        return "#"
    if isinstance(o, list):
        return [forme(x) for x in o]
    if isinstance(o, dict):
        return {k: forme(v) for k, v in o.items()}
    raise Refus(f"feuille inattendue dans une loi : {type(o).__name__}")


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def cle_forme(loi):
    return canon(forme(loi))


def feuilles(o):
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return []
    if isinstance(o, (int, float)):
        return [float(o)]
    if isinstance(o, list):
        return [x for e in o for x in feuilles(e)]
    return [x for k in sorted(o) for x in feuilles(o[k])]


# --- M1 et M2 (S1) --------------------------------------------------------------------------------------------------------
def mesures_s1(boucle, lecture):
    r = boucle["releve"]
    cartes = sorted(r["cartes"], key=lambda c: (c["generation"], c["proposeur"], c["identifiant"]))
    plantees = r["plantees"]
    canons_plantes = {canon(p["loi"]): p["nom"] for p in plantees}
    # coût : un appel par proposeur et par génération (événements « generation » du journal)
    couts, depense_cumulee = {}, {}
    for ev in boucle["journal"]:
        if ev.get("evenement") == "generation":
            g = ev["generation"]
            depense_cumulee[g] = ev["depense"]["depense_usd"]
            for a in ev["comptes"]["appels_proposeurs"]:
                couts[(g, a["proposeur"])] = {"cout_usd": a["cout_usd"], "propositions": a["propositions"]}
    gens = sorted(depense_cumulee)
    depense_gen = {g: depense_cumulee[g] - (depense_cumulee[gens[i - 1]] if i else 0.0) for i, g in enumerate(gens)}
    m1 = {}
    for g in gens:
        cg = [c for c in cartes if c["generation"] == g]
        m1[str(g)] = {"depense_de_la_generation_usd": round(depense_gen[g], 6), "cartes": len(cg),
                      "depense_de_la_generation_par_carte_usd": round(depense_gen[g] / len(cg), 6) if cg else None,
                      "par_proposeur": {}}
        for p in sorted({c["proposeur"] for c in cg}):
            cp = [c for c in cg if c["proposeur"] == p]
            identiques = [c["identifiant"] for c in cp if canon(c["loi"]) in canons_plantes]
            proches = []
            for c in cp:
                fc, vc = cle_forme(c["loi"]), feuilles(c["loi"])
                d = [max(abs(a - b) for a, b in zip(vc, feuilles(pl["loi"]))) if vc else 0.0
                     for pl in plantees if cle_forme(pl["loi"]) == fc]
                proches.append({"carte": c["identifiant"], "plantees_de_meme_forme": len(d),
                                "plus_petit_ecart_max_de_parametre": round(min(d), 6) if d else None})
            cout = couts.get((g, p))
            m1[str(g)]["par_proposeur"][p] = {
                "cartes": len(cp), "formes_distinctes": len({cle_forme(c["loi"]) for c in cp}),
                "types": sorted({c["loi"]["type"] for c in cp}),
                "cartes_identiques_a_une_loi_plantee": len(identiques), "lesquelles": identiques,
                "proximite_aux_plantees_information": proches,
                "cout_proposeur_usd": cout["cout_usd"] if cout else None,
                "cout_proposeur_par_carte_usd": round(cout["cout_usd"] / len(cp), 6) if cout and cp else None,
                "propositions_comptees_par_la_course": cout["propositions"] if cout else None,
                "verdict_du_juge_information": {"promues": sum(bool(c["promue"]) for c in cp),
                                                "survivantes_test_de_mort": sum(c.get("verdict") == "survit" for c in cp)},
            }
    oracle = lecture["oracle"]["par_fournisseur"]
    m1["oracle_par_proposeur_promues_seulement"] = {
        p: {k: oracle[p][k] for k in ("proposees", "promues", "vraies_decouvertes", "fausses_decouvertes")} for p in sorted(oracle)}
    m1["oracle_note"] = ("vérité de l'oracle écrite sur les seules cartes promues ; aucune carte de la génération 2 n'est "
                         "promue : leur vérité n'est pas rendue par la source")
    m1["c1_sur_s1"] = "indécidable (déclaré d'avance : deux générations, 23 cartes)"

    # M2
    archive_formes = {cle_forme(_loi_archive(r))} if _loi_archive(r) is not None else set()
    def repetitions(avec_archive):
        detail, n_rep = [], 0
        for c in cartes:
            f = cle_forme(c["loi"])
            anterieures = {cle_forme(x["loi"]) for x in cartes if x["generation"] < c["generation"]}
            meme = [x for x in cartes if x["generation"] == c["generation"] and x["proposeur"] == c["proposeur"]
                    and x["identifiant"] < c["identifiant"]]
            anterieures |= {cle_forme(x["loi"]) for x in meme}
            if avec_archive:
                anterieures |= archive_formes
            rep = f in anterieures
            n_rep += rep
            detail.append({"carte": c["identifiant"], "type": c["loi"]["type"], "repete_une_forme": rep})
        return n_rep, detail
    n_rep, detail = repetitions(False)
    n_rep_k1, _ = repetitions(True)
    par = {}
    for (g, p) in sorted({(c["generation"], c["proposeur"]) for c in cartes}):
        ids = [c["identifiant"] for c in cartes if c["generation"] == g and c["proposeur"] == p]
        k = sum(d["repete_une_forme"] for d in detail if d["carte"] in ids)
        par[f"{g}|{p}"] = {"cartes": len(ids), "repetent": k, "part": round(k / len(ids), 6)}
    part = n_rep / len(cartes)
    m2 = {"cartes": len(cartes), "repetent_une_forme": n_rep, "part": round(part, 6),
          "refusees_par_la_memoire": "champ absent de la source (non observable)",
          "decision": "mode dominant (sur-exploitation d'une forme)" if part > SEUIL_MODE else "pas de mode dominant",
          "sensibilite_archive_K1_comptee": {"repetent": n_rep_k1, "part": round(n_rep_k1 / len(cartes), 6),
                                              "decision": "mode dominant" if n_rep_k1 / len(cartes) > SEUIL_MODE else "pas de mode dominant"},
          "formes_distinctes_toutes_cartes": len({cle_forme(c["loi"]) for c in cartes}),
          "par_generation_et_proposeur": par, "detail": detail}
    return m1, m2


def _loi_archive(r):
    arch = r.get("archives_de_jugement", {}).get("1", {})
    return arch.get("K1")


# --- M3 et M4 (S2) --------------------------------------------------------------------------------------------------------
def quantiles(v):
    s = np.sort(v)
    n = len(s)
    return float(s[int(math.floor(0.025 * n))]), float(s[int(math.ceil(0.975 * n)) - 1])


def rapport(ev_p, at_p, ev_t, at_t):
    """Rapport taux tardif / taux précoce, vectorisé ; nan si indéfini, +inf si précoce nul et tardif positif."""
    with np.errstate(divide="ignore", invalid="ignore"):
        tp = np.where(at_p > 0, ev_p / np.where(at_p > 0, at_p, 1), np.nan)
        tt = np.where(at_t > 0, ev_t / np.where(at_t > 0, at_t, 1), np.nan)
        r = np.where(tp > 0, tt / np.where(tp > 0, tp, 1), np.where(tt > 0, np.inf, np.nan))
        r = np.where(np.isnan(tp) | np.isnan(tt), np.nan, r)
    return r


def comptes_unite(suite, coupe):
    ev_p = at_p = ev_t = at_t = 0
    for t in suite["tentatives"]:
        e = int(bool((t.get("verdict") or {}).get("promue")))
        if t["k"] <= coupe:
            at_p += 1
            ev_p += e
        else:
            at_t += 1
            ev_t += e
    return ev_p, at_p, ev_t, at_t


def _decision(point, lo, hi, indefinis):
    if point is None or (isinstance(point, float) and math.isnan(point)):
        return "indécidable (rapport indéfini au point : sans objet)"
    if indefinis > 0:
        return f"indécidable ({indefinis} tirages sur {TIRAGES} au rapport indéfini)"
    if hi < SEUIL_PLATEAU:
        return "plateau"
    if lo > SEUIL_PLATEAU:
        return "pas de plateau"
    return "indécidable (intervalle à cheval sur 0,5)"


def _f(x):
    if x is None:
        return None
    x = float(x)
    if math.isnan(x):
        return "indéfini"
    if math.isinf(x):
        return "+inf" if x > 0 else "-inf"
    return round(x, 6)


def m3_groupe(strates, coupe, rng):
    """strates : {nom: {bras: [suites ordonnées par carte]}} ; même tirage de cartes pour les deux bras d'une strate."""
    bras_tous = sorted({b for s in strates.values() for b in s})
    sommes = {b: np.zeros((TIRAGES, 4)) for b in bras_tous}
    points = {b: np.zeros(4) for b in bras_tous}
    for nom in sorted(strates):
        s = strates[nom]
        n = len(next(iter(s.values())))
        cartes = {b: [u["carte"] for u in s[b]] for b in s}
        if len({tuple(v) for v in cartes.values()}) != 1:
            raise Refus(f"strate {nom} : cartes différentes entre bras, plan apparié rompu")
        idx = rng.integers(0, n, size=(TIRAGES, n))
        for b in s:
            c = np.array([comptes_unite(u, coupe) for u in s[b]], dtype=float)
            points[b] += c.sum(axis=0)
            sommes[b] += c[idx].sum(axis=1)
    out = {}
    tir = {}
    for b in bras_tous:
        p = points[b]
        rp = rapport(p[0:1], p[1:2], p[2:3], p[3:4])[0]
        rt = rapport(sommes[b][:, 0], sommes[b][:, 1], sommes[b][:, 2], sommes[b][:, 3])
        tir[b] = rt
        indef = int(np.isnan(rt).sum())
        lo, hi = quantiles(np.where(np.isnan(rt), np.inf, rt)) if indef < TIRAGES else (float("nan"), float("nan"))
        out[b] = {"evenements_precoces": int(p[0]), "essais_precoces": int(p[1]), "evenements_tardifs": int(p[2]),
                  "essais_tardifs": int(p[3]),
                  "taux_precoce": _f(p[0] / p[1]) if p[1] else "indéfini",
                  "taux_tardif": _f(p[2] / p[3]) if p[3] else "indéfini",
                  "rapport_tardif_sur_precoce": _f(rp), "ic95": [_f(lo), _f(hi)] if indef == 0 else "non calculé (tirages indéfinis)",
                  "tirages_indefinis": indef, "decision": _decision(None if math.isnan(rp) else rp, lo, hi, indef)}
    if {"retour", "temoin"} <= set(tir):
        with np.errstate(invalid="ignore"):
            d = tir["retour"] - tir["temoin"]
        indef = int(np.isnan(d).sum())
        pr = out["retour"]["rapport_tardif_sur_precoce"]
        pt = out["temoin"]["rapport_tardif_sur_precoce"]
        point = (pr - pt) if isinstance(pr, float) and isinstance(pt, float) else "indéfini"
        out["difference_retour_moins_temoin"] = {
            "point": _f(point) if not isinstance(point, str) else point,
            "ic95": [_f(x) for x in quantiles(d)] if indef == 0 else "non calculé (tirages indéfinis)",
            "tirages_indefinis": indef, "regle": "aucune (le texte n'en fixe pas) : rapportée seulement"}
    return out


def m4_cellule(suites):
    props = rep = quasi = props_k2 = rep_k2 = 0
    formes = set()
    for s in suites:
        vus, vues = set(), set()
        for t in s["tentatives"]:
            if t.get("loi") is None:
                continue
            c, f = canon(t["loi"]), cle_forme(t["loi"])
            formes.add(f)
            props += 1
            r = c in vus
            q = f in vues
            if t["k"] >= 2:
                props_k2 += 1
                rep_k2 += int(r or q)
            rep += int(r)
            quasi += int(q and not r)
            vus.add(c)
            vues.add(f)
    part = (rep + quasi) / props if props else None
    return {"propositions": props, "repetees_a_l_octet": rep, "quasi_identiques_meme_forme": quasi,
            "part": _f(part) if part is not None else "indéfini",
            "decision": ("mode dominant (sur-exploitation)" if part > SEUIL_MODE else "pas de mode dominant") if part is not None else "indécidable",
            "complement_parmi_k_ge_2": {"propositions": props_k2, "repetees_ou_quasi": rep_k2,
                                        "part": _f(rep_k2 / props_k2) if props_k2 else "indéfini"},
            "formes_distinctes": len(formes)}


def mesures_s2(nom, sortie, seq):
    n_max = sortie["preenregistrement"]["plan"]["n_max"]
    coupe = int(math.floor(PART_PRECOCE * n_max))
    suites = sortie["suites"]
    for s in suites:
        if s.get("interrompue"):
            raise Refus(f"{nom} : suite interrompue présente (course interrompue : non lue)")
    cases = {}
    for s in suites:
        cases.setdefault((s["monde"], s["juge"], s["condition"]), []).append(s)
    for k in cases:
        cases[k].sort(key=lambda u: u["carte"])
    mondes = sorted({k[0] for k in cases})
    juges = sorted({k[1] for k in cases})
    taches = seq.spawn(4)
    res = {"n_max": n_max, "coupe_precoce": coupe, "unites": len(suites),
           "essais_joues": sum(len(s["tentatives"]) for s in suites),
           "cases": {f"{m}|{j}|{b}": len(v) for (m, j, b), v in sorted(cases.items())},
           "verite_des_mondes": VERITE_DES_MONDES[nom]}
    m3 = {}
    for etiquette, c, graine in (("principale_k_le_%d" % coupe, coupe, taches[0]),
                                 ("sensibilite_k_le_%d" % (coupe + 1), coupe + 1, taches[1])):
        strates = {}
        for (m, j, b), v in cases.items():
            strates.setdefault(f"{m}|{j}", {})[b] = v
        enfants = graine.spawn(len(strates) + 1)
        par_bras = m3_groupe(strates, c, np.random.default_rng(enfants[0]))
        par_case = {}
        for i, sn in enumerate(sorted(strates)):
            par_case[sn] = m3_groupe({sn: strates[sn]}, c, np.random.default_rng(enfants[i + 1]))
            par_case[sn]["verite_du_monde"] = VERITE_DES_MONDES[nom][sn.split("|")[0]]
        m3[etiquette] = {"evenement": "verdict.promue (verdict du juge de la suite)",
                         "par_bras_lettre_du_texte": par_bras, "par_case_monde_juge": par_case}
    m3["second_evenement_loi_vraie_selon_le_monde"] = {
        m: ("sans objet : le monde n'admet aucune loi au-delà de l'archive (toute promotion y est fausse)"
            if VERITE_DES_MONDES[nom][m] == "fausse_par_construction"
            else "indécidable : la source n'écrit aucune vérité par loi proposée") for m in mondes}
    # information : rejeux des lois promues au-dessus de alpha après Holm (machinerie du juge, pas vérité du monde)
    info = {}
    for a in sortie.get("audit_A2", []):
        cle = a["etiquette"]
        d = info.setdefault(cle, {"lois_promues_rejouees": 0, "au_dessus_de_alpha_holm": 0})
        d["lois_promues_rejouees"] += 1
        d["au_dessus_de_alpha_holm"] += int(bool(a.get("au_dessus_de_alpha_holm")))
    m3["information_rejeux_audit_A2"] = dict(sorted(info.items()))
    # M4
    m4 = {"par_case": {f"{m}|{j}|{b}": m4_cellule(v) for (m, j, b), v in sorted(cases.items())}, "par_bras": {}}
    for b in sorted({k[2] for k in cases}):
        m4["par_bras"][b] = m4_cellule([s for k, v in cases.items() if k[2] == b for s in v])
    res["juges"], res["mondes"] = juges, mondes
    return res, m3, m4


def principal(argv=None):
    ap = argparse.ArgumentParser()
    for a in ("s1-boucle", "s1-lecture", "s2a", "s2a-manifeste", "s2b", "s2b-manifeste", "sortie"):
        ap.add_argument("--" + a, required=True)
    ap.add_argument("--empreintes-attendues")
    a = ap.parse_args(argv)
    chemins = {"s1_boucle": a.s1_boucle, "s1_lecture": a.s1_lecture, "s2a": a.s2a, "s2a_manifeste": a.s2a_manifeste,
               "s2b": a.s2b, "s2b_manifeste": a.s2b_manifeste}
    attendues, essai = dict(EMPREINTES), False
    if a.empreintes_attendues:
        with open(a.empreintes_attendues, encoding="utf-8") as f:
            attendues.update(json.load(f))
        essai = True
    try:
        lus, empreintes = charger(chemins, attendues)
        seq = np.random.SeedSequence(RACINE_GRAINES)
        t_s2a, t_s2b = seq.spawn(2)
        m1, m2 = mesures_s1(lus["s1_boucle"], lus["s1_lecture"])
        s2a, m3a, m4a = mesures_s2("s2a", lus["s2a"], t_s2a)
        s2b, m3b, m4b = mesures_s2("s2b", lus["s2b"], t_s2b)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    with open(__file__, "rb") as f:
        prog = hashlib.sha256(f.read()).hexdigest()
    sortie = {"version": VERSION, "essai": essai, "programme_sha256": prog,
              "manifeste": {"python": platform.python_version(), "numpy": np.__version__,
                            "graines": {"racine": RACINE_GRAINES, "regle": "SeedSequence(racine).spawn(2) -> S2a, S2b ; par source spawn(4) : [0] coupe principale, [1] sensibilité, [2] et [3] non employées ; dans chacune spawn(n+1) : [0] groupe par bras, [1..n] cases (monde|juge) dans l'ordre des noms"},
                            "tirages": TIRAGES, "seuil_plateau": SEUIL_PLATEAU, "seuil_mode_dominant": SEUIL_MODE,
                            "part_precoce": PART_PRECOCE},
              "sources": empreintes,
              "S1": {"M1": m1, "M2": m2},
              "S2a_reprise_propre_5_novembre": {"structure": s2a, "M3": m3a, "M4": m4a},
              "S2b_attaque_v9_10_novembre": {"structure": s2b, "M3": m3b, "M4": m4b}}
    with open(a.sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")
    print(f"ÉCRIT {a.sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
