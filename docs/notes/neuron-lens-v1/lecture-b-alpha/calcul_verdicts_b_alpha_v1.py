"""Calcul indépendant des verdicts de la tranche B-α de « Neuron Lens » — lecteur neuf, v1.

Applique les seuils gelés de `texte-gele-volet-a-et-b-alpha-v6.md` (`34b88243…`), sections « Seuil » (B), « Critères de lecture gelés »
et « Audit symétrique », selon `plan-de-lecture-v1.md` (`5a799918…`). N'importe aucun module de la course ; ne lit pas
`b-alpha-verdicts.json`. Bibliothèque standard et numpy seulement ; aucun modèle, aucun réseau.

Usage : python -I calcul_verdicts_b_alpha_v1.py DOSSIER_DIAG SORTIE.json
Entrées lues dans DOSSIER_DIAG : `causal_lens_llama-3.1-8b-instruct.json` (résumé écrit par `score`), `b-alpha-grandeurs.json` (n et
pôles écartés par motif), `grandeurs-par-pole-b-alpha-v1.json` (r par pôle : recalcul de contrôle et intervalles), `b-alpha-b0.json`,
`b-alpha-fumee.json`.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
LENTILLES = ("logit", "J", "npJpp", "npR")
N_LISIBLE = 48
TIRAGES = 2000
ENTROPIE = 20261115  # graine propre au lecteur (R9) : SeedSequence(entropy=20261115), un enfant par (cible, grandeur)


def empreinte(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mediane_basse(x):
    """Médiane au sens de `torch.median` (celle de `score`) : pour un effectif pair, la plus basse des deux valeurs centrales."""
    x = np.sort(np.asarray(x, float))
    return float(x[(len(x) - 1) // 2])


def bande(a, b):
    return list(range(a, b + 1))


def plus_de_la_moitie(k, m):
    return m > 0 and k > m / 2


def juger_bande(couches, lisible, cond):
    """Rend (lisibles, non_lisibles, partielle, liste des couches lisibles où la condition manque)."""
    lis = [l for l in couches if lisible[l]]
    non = [l for l in couches if not lisible[l]]
    return lis, non, len(non) > len(couches) / 4, [l for l in lis if not cond(l)]


def main(dossier, sortie):
    d = Path(dossier)
    noms = {"score": "causal_lens_llama-3.1-8b-instruct.json", "grandeurs": "b-alpha-grandeurs.json",
            "poles": "grandeurs-par-pole-b-alpha-v1.json", "b0": "b-alpha-b0.json", "fumee": "b-alpha-fumee.json"}
    emp = {k: empreinte(d / v) for k, v in noms.items()}
    sc = json.loads((d / noms["score"]).read_text())
    gr = json.loads((d / noms["grandeurs"]).read_text())["resultat"]
    pp = json.loads((d / noms["poles"]).read_text())
    b0 = json.loads((d / noms["b0"]).read_text())["resultat"]
    fu = json.loads((d / noms["fumee"]).read_text())["resultat"]
    T = sc["targets"]
    ecarts_de_forme = []
    for c in CIBLES:
        for s in LENTILLES:
            if T[c][s]["layer"] != list(range(32)):
                ecarts_de_forme.append(f"{c}|{s} : couches {T[c][s]['layer']}")
    if sc["lenses"] != list(LENTILLES):
        ecarts_de_forme.append(f"lentilles {sc['lenses']}")
    if ecarts_de_forme:
        raise SystemExit("forme inattendue du résumé de score : " + " ; ".join(ecarts_de_forme))

    def v(c, s, cle, l):
        return T[c][s][cle][l]

    n = {c: gr["n"][c] for c in CIBLES}
    lis = {c: [n[c][l] >= N_LISIBLE for l in range(32)] for c in CIBLES}

    # ---------- recalcul de contrôle à partir des r par pôle (valeurs arrondies à 6 décimales dans le fichier versé)
    par = {}  # (cible, lentille, couche) -> (r, r_temoin) des pôles aléatoires retenus
    for p in pp["poles"]:
        if not p["aleatoire"]:
            continue
        for c in CIBLES:
            for s in LENTILLES:
                x = p["lectures"][c][s]
                if x["motif"] == "retenu":
                    par.setdefault((c, s, p["couche"]), []).append((x["r"], x["r_temoin"]))
    par = {k: np.asarray(val, float) for k, val in par.items()}
    seuil_pass = {}
    for c in CIBLES:
        for s in LENTILLES:
            tous = np.concatenate([par[(c, s, l)][:, 1] for l in range(32) if (c, s, l) in par])
            seuil_pass[(c, s)] = float(np.quantile(tous.astype(np.float32), 0.99))
    recalcul_ecart_max = {"r_med": 0.0, "control_med": 0.0, "pass": 0.0, "pass_threshold": 0.0}
    n_poles_differe = []
    rec = {}
    for c in CIBLES:
        for s in LENTILLES:
            recalcul_ecart_max["pass_threshold"] = max(recalcul_ecart_max["pass_threshold"],
                                                       abs(seuil_pass[(c, s)] - T[c][s]["pass_threshold"]))
            for l in range(32):
                a = par.get((c, s, l), np.zeros((0, 2)))
                if len(a) != n[c][l]:
                    n_poles_differe.append(f"{c}|{s}|{l} : {len(a)} pôles retenus contre n = {n[c][l]}")
                if len(a) == 0:
                    continue
                r_med, c_med = mediane_basse(a[:, 0]), mediane_basse(a[:, 1])
                pas = float(np.mean(a[:, 0] > seuil_pass[(c, s)]))
                rec[(c, s, l)] = (r_med, c_med, pas)
                recalcul_ecart_max["r_med"] = max(recalcul_ecart_max["r_med"], abs(r_med - v(c, s, "r_med", l)))
                recalcul_ecart_max["control_med"] = max(recalcul_ecart_max["control_med"], abs(c_med - v(c, s, "control_med", l)))
                recalcul_ecart_max["pass"] = max(recalcul_ecart_max["pass"], abs(pas - v(c, s, "pass", l)))

    # ---------- chaîne en défaut
    defauts = []
    a_liste = [(c, s, l, v(c, s, "control_med", l)) for c in CIBLES for s in LENTILLES for l in range(28)
               if abs(v(c, s, "control_med", l)) > 0.10]
    if a_liste:
        defauts.append({"condition": "(a)", "detail": a_liste})
    nul = gr["ecartes"]["steer 1x"]["effet nul"]
    b_liste = [(l, nul[l]) for l in range(28) if nul[l] > 32]
    if b_liste:
        defauts.append({"condition": "(b)", "detail": b_liste})
    c_liste = [("logit", l, v("steer 1x", "logit", "r_med", l)) for l in (28, 29, 30) if v("steer 1x", "logit", "r_med", l) < 0.80]
    c_liste += [("npR", l, v("steer 1x", "npR", "r_med", l)) for l in (28, 29, 30) if v("steer 1x", "npR", "r_med", l) < 0.85]
    if c_liste:
        defauts.append({"condition": "(c)", "detail": c_liste})
    essais = b0["essais"]
    d_liste = [f"{k} : code {x['code']}, {x['resume']}" for k, x in essais.items()
               if x["code"] != 0 or "skipped" in x["resume"] or "failed" in x["resume"] or "error" in x["resume"]]
    for attendu in ("essai-06_activations-llama-v3.py", "essai-lenses-neuronpedia-v3.py"):
        if attendu not in essais:
            d_liste.append(f"{attendu} : absent du résultat de B0")
    if fu["code"] != 0:
        d_liste.append(f"fumée : code {fu['code']}")
    if d_liste:
        defauts.append({"condition": "(d)", "detail": d_liste})
    e_liste = [(s, l, v("steer 1x", s, "r_med", l), v("steer 1x", "logit", "r_med", l))
               for s in ("J", "npJpp", "npR") for l in range(24)
               if abs(v("steer 1x", s, "r_med", l) - v("steer 1x", "logit", "r_med", l)) < 1e-3]
    e_b0 = [f"{s} : {x['defauts']}" for s, x in b0["lentilles"].items() if x["defauts"]]
    if e_liste or e_b0:
        defauts.append({"condition": "(e)", "detail": {"r_med": e_liste, "b0": e_b0}})
    arrets_b0 = [f"{s} : {x['arrets']}" for s, x in b0["lentilles"].items() if x["arrets"]]
    arrets_b0 += [f"{s} : sortie sans « layers 0-30 »" for s, x in b0["lentilles"].items() if "layers 0-30," not in x["sortie"]]
    marges_defaut = {
        "(a) plus grand |control_med|, couches 0-27, 4 cibles x 4 lentilles":
            max(((abs(v(c, s, "control_med", l)), c, s, l) for c in CIBLES for s in LENTILLES for l in range(28))),
        "(b) plus grand nombre de pôles écartés pour effet nul, steer 1x, couches 0-27": max(nul[:28]),
        "(c) plus petit r_med logits, couches 28-30": min(v("steer 1x", "logit", "r_med", l) for l in (28, 29, 30)),
        "(c) plus petit r_med npR, couches 28-30": min(v("steer 1x", "npR", "r_med", l) for l in (28, 29, 30)),
        "(e) plus petit |r_med(lentille) - r_med(logits)|, couches 0-23":
            min(((round(abs(v("steer 1x", s, "r_med", l) - v("steer 1x", "logit", "r_med", l)), 4), s, l)
                 for s in ("J", "npJpp", "npR") for l in range(24))),
    }

    # ---------- B-2
    L1, R = lis["steer 1x"], (lambda l: v("steer 1x", "npR", "r_med", l))
    P, C = (lambda l: v("steer 1x", "npR", "pass", l)), (lambda l: v("steer 1x", "npR", "control_med", l))
    seuil_r = lambda l: 0.40 if l <= 15 else (0.60 if l <= 23 else 0.85)
    b2 = {"bandes": {}}
    for nom, (a, b), cond in (("r_med 8-15 >= 0,40", (8, 15), lambda l: R(l) >= 0.40), ("r_med 16-23 >= 0,60", (16, 23), lambda l: R(l) >= 0.60),
                              ("r_med 24-27 >= 0,85", (24, 27), lambda l: R(l) >= 0.85), ("pass 8-27 >= 0,90", (8, 27), lambda l: P(l) >= 0.90)):
        li, non, part, manque = juger_bande(bande(a, b), L1, cond)
        b2["bandes"][nom] = {"lisibles": len(li), "non_lisibles": non, "partielle": part, "couches_en_manque": manque}
    hors05 = [l for l in range(28) if abs(C(l)) > 0.05]
    hors10 = [l for l in range(28) if abs(C(l)) > 0.10]
    hors05_lis = [l for l in hors05 if L1[l]]
    hors10_lis = [l for l in hors10 if L1[l]]
    b2["temoin"] = {"hors_0,05_toutes_couches": hors05, "hors_0,10_toutes_couches": hors10,
                    "hors_0,05_couches_lisibles": hors05_lis, "hors_0,10_couches_lisibles": hors10_lis,
                    "tient_lecture_toutes_couches": len(hors05) <= 1 and not hors10,
                    "tient_lecture_couches_lisibles": len(hors05_lis) <= 1 and not hors10_lis}
    bandes_ok = all(not x["couches_en_manque"] for x in b2["bandes"].values())
    l1627 = [l for l in bande(16, 27) if L1[l]]
    l1623 = [l for l in bande(16, 23) if L1[l]]
    k_pass, k_r = [l for l in l1627 if P(l) < 0.50], [l for l in l1623 if R(l) < 0.30]
    b2["non_reproduit"] = {"pass<0,50 (16-27)": k_pass, "r_med<0,30 (16-23)": k_r,
                           "declenche": plus_de_la_moitie(len(k_pass), len(l1627)) or plus_de_la_moitie(len(k_r), len(l1623))}
    b2["partielle"] = any(x["partielle"] for x in b2["bandes"].values())

    def etiquette(rep, nonrep):
        return "non reproduit" if nonrep and not rep else ("reproduit" if rep and not nonrep else ("contradictoire" if rep else "autre"))
    b2["verdict_lecture_temoin_toutes_couches"] = etiquette(bandes_ok and b2["temoin"]["tient_lecture_toutes_couches"], b2["non_reproduit"]["declenche"])
    b2["verdict_lecture_temoin_couches_lisibles"] = etiquette(bandes_ok and b2["temoin"]["tient_lecture_couches_lisibles"], b2["non_reproduit"]["declenche"])
    b2["marge_min_r_med"] = min((round(R(l) - seuil_r(l), 4), l) for l in bande(8, 27) if L1[l])
    b2["marge_min_pass"] = min((round(P(l) - 0.90, 4), l) for l in bande(8, 27) if L1[l])
    b2["plus_grand_abs_control_med_0_27"] = max((abs(C(l)), l) for l in range(28))

    # ---------- B-3
    E = lambda l: round(R(l) - v("steer 1x", "logit", "r_med", l), 4)
    li, non, part, manque = juger_bande(bande(4, 15), L1, lambda l: E(l) >= 0.20)
    neg = [l for l in li if E(l) <= 0]
    b3 = {"ecart_par_couche": {l: E(l) for l in bande(4, 15)}, "lisibles": len(li), "non_lisibles": non, "partielle": part,
          "couches_en_manque": manque, "ecart<=0": neg, "marge_min": min((round(E(l) - 0.20, 4), l) for l in li) if li else None}
    b3["verdict"] = etiquette(not manque and bool(li), plus_de_la_moitie(len(neg), len(li)))

    # ---------- B-4 (rapportée)
    b4 = {"npR - J": {l: round(R(l) - v("steer 1x", "J", "r_med", l), 4) for l in bande(4, 23)},
          "npR - npJpp": {l: round(R(l) - v("steer 1x", "npJpp", "r_med", l), 4) for l in bande(4, 23)}}
    for k in list(b4):
        vals = list(b4[k].values())
        b4[k + " : min, max, nombre de couches > 0"] = [min(vals), max(vals), sum(1 for x in vals if x > 0)]

    # ---------- B-7
    LW, A = lis["ablate win"], (lambda l: v("ablate win", "npR", "r_med", l))
    li_b, non_b, part_b, manque_b = juger_bande(bande(0, 15), LW, lambda l: A(l) < 0.25)
    li_h, non_h, part_h, manque_h = juger_bande(bande(26, 29), LW, lambda l: A(l) >= 0.50)
    l815 = [l for l in bande(8, 15) if LW[l]]
    haut, bas = [l for l in l815 if A(l) >= 0.40], [l for l in li_h if A(l) < 0.30]
    nr_haut, nr_bas = plus_de_la_moitie(len(haut), len(l815)), plus_de_la_moitie(len(bas), len(li_h))
    b7 = {"0-15 r_med < 0,25": {"lisibles": len(li_b), "non_lisibles": non_b, "partielle": part_b, "couches_en_manque": manque_b,
                                "plus_grand_r_med": max((A(l), l) for l in li_b) if li_b else None},
          "26-29 r_med >= 0,50": {"lisibles": len(li_h), "non_lisibles": non_h, "partielle": part_h, "couches_en_manque": manque_h,
                                  "plus_petit_r_med": min((A(l), l) for l in li_h) if li_h else None},
          "non_reproduit_par_le_haut (>= 0,40 sur 8-15)": haut, "non_reproduit_par_le_bas (< 0,30 sur 26-29)": bas,
          "verdict": etiquette(not manque_b and not manque_h and bool(li_b) and bool(li_h), nr_haut or nr_bas),
          "sens": "par le haut" if nr_haut else ("par le bas" if nr_bas else None),
          "ablate win par lentille, couche 26": {s: v("ablate win", s, "r_med", 26) for s in LENTILLES},
          "plus grand écart entre lentilles de r_med (ablate win), couches 0-30":
              max((round(max(v("ablate win", s, "r_med", l) for s in LENTILLES) - min(v("ablate win", s, "r_med", l) for s in LENTILLES), 4), l)
                  for l in range(31))}

    # ---------- audits R4 gelés
    r4 = lambda x: round(x, 4)
    beau_r = [(l, R(l)) for l in range(8) if r4(R(l)) >= 0.95]
    beau_0 = [l for l in range(28) if r4(C(l)) == 0]
    trop_beau = bool(beau_r) or len(beau_0) >= 2
    tout_negatif = {x for x in (b2["verdict_lecture_temoin_toutes_couches"], b2["verdict_lecture_temoin_couches_lisibles"])} == {"non reproduit"} \
        and b3["verdict"] == "non reproduit"

    # ---------- verdict de reproduction
    def reproduction(vb2):
        if defauts or arrets_b0:
            return "chaîne en défaut" if defauts else "arrêt de B-α (contrôle de B0)"
        if trop_beau or tout_negatif:
            return "verdict suspendu à l'audit R4"
        if vb2 == "reproduit" and b3["verdict"] == "reproduit":
            return "reproduit avec la lentille R publique"
        if "non reproduit" in (vb2, b3["verdict"]):
            return "non reproduit avec la lentille R publique"
        return "partiel"

    # ---------- intervalles par rééchantillonnage des pôles (rapportés ; ne décident de rien)
    ss = np.random.SeedSequence(entropy=ENTROPIE)
    enfants = ss.spawn(3)

    def boot(c, fonction, graine):
        g = np.random.default_rng(graine)
        res = {}
        for l in range(32):
            a = {s: par[(c, s, l)][:, 0] for s in LENTILLES if (c, s, l) in par}
            m = len(a["npR"])
            idx = g.integers(0, m, size=(TIRAGES, m))
            tir = np.array([fonction({s: x[i] for s, x in a.items()}) for i in idx])
            res[l] = [round(float(np.quantile(tir, 0.025)), 4), round(float(np.quantile(tir, 0.975)), 4)]
        return res
    ic = {"steer 1x, npR, r_med": boot("steer 1x", lambda a: mediane_basse(a["npR"]), enfants[0]),
          "steer 1x, r_med(npR) - r_med(logit)": boot("steer 1x", lambda a: mediane_basse(a["npR"]) - mediane_basse(a["logit"]), enfants[1]),
          "ablate win, npR, r_med": boot("ablate win", lambda a: mediane_basse(a["npR"]), enfants[2])}

    # ---------- signes de propreté (signalés, sans verdict)
    proprete = {
        "n constant égal à 64 pour toute couche et toute cible": all(x == 64 for c in CIBLES for x in n[c]),
        "aucun pôle écarté (effet nul, sans contexte)": all(x == 0 for c in CIBLES for m in gr["ecartes"][c].values() for x in m),
        "couche 31 : J, npJpp, npR égales aux logits (attendu par le texte)":
            all(v(c, s, k, 31) == v(c, "logit", k, 31) for c in CIBLES for s in ("J", "npJpp", "npR") for k in ("r_med", "control_med", "pass")),
        "couches 0-30 où deux lentilles ont exactement le même r_med (steer 1x)":
            [(l, s1, s2) for l in range(31) for i, s1 in enumerate(LENTILLES) for s2 in LENTILLES[i + 1:]
             if v("steer 1x", s1, "r_med", l) == v("steer 1x", s2, "r_med", l)],
        "nombre de couches 8-27 où pass(npR, steer 1x) vaut exactement 1": sum(1 for l in bande(8, 27) if P(l) == 1.0),
        "pass_control maximal (npR, steer 1x)": max(T["steer 1x"]["npR"]["pass_control"]) if "pass_control" in T["steer 1x"]["npR"] else None,
        "r_med npR steer 1x non décroissant de 8 à 27": all(R(l + 1) >= R(l) for l in range(8, 27)),
    }

    tableau = {c: {s: {k: T[c][s][k] for k in ("r_med", "control_med", "pass")} for s in LENTILLES} for c in CIBLES}
    out = {
        "programme": "calcul_verdicts_b_alpha_v1.py", "texte_gele_sha256": "34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131",
        "entrees_sha256": {noms[k]: emp[k] for k in noms},
        "meta_score": sc["meta"], "n": n, "couches_non_lisibles": {c: [l for l in range(32) if not lis[c][l]] for c in CIBLES},
        "recalcul_par_pole": {"ecart_max_au_resume_de_score": {k: round(x, 6) for k, x in recalcul_ecart_max.items()},
                              "effectifs_differents_de_n": n_poles_differe,
                              "note": "médiane basse (torch.median), centile 0,99 commun des r du témoin, sur les r arrondis à 6 décimales"},
        "chaine_en_defaut": {"defauts": defauts, "arrets_b0": arrets_b0, "marges": marges_defaut,
                             "essais_b0": {k: x["resume"] for k, x in essais.items()}, "fumee_code": fu["code"]},
        "B-2": b2, "B-3": b3, "B-4": b4, "B-7": b7,
        "audits_R4": {"trop_beau": trop_beau, "r_med>=0,95 couches 0-7": beau_r, "control_med écrit égal à 0, couches 0-27": beau_0,
                      "tout_negatif": tout_negatif},
        "verdict_reproduction": {"lecture_temoin_toutes_couches": reproduction(b2["verdict_lecture_temoin_toutes_couches"]),
                                 "lecture_temoin_couches_lisibles": reproduction(b2["verdict_lecture_temoin_couches_lisibles"])},
        "intervalles_95": {"tirages": TIRAGES, "graine": f"SeedSequence(entropy={ENTROPIE}).spawn(3)", "valeurs": ic},
        "proprete": proprete, "tableau": tableau,
    }
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("verdict_reproduction", "audits_R4")}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    if Path(sys.argv[2]).exists():
        raise SystemExit("la sortie existe déjà : on n'écrase jamais (R12)")
    main(sys.argv[1], sys.argv[2])
