"""Calcul des verdicts du lecteur neuf — tranche de l'ajustement de nos lentilles (B-β), lecture par lentille neuronale, Llama 3.1 8B
Instruct — v1.

Écrit par le lecteur neuf selon son plan de lecture v2 (`plan-de-lecture-b-beta-v2.md`, `391c3b1a…`), section 3 (règles recopiées du
texte gelé `texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, et de l'addendum partie 1 v3, `bd8067dc…`). N'importe aucun code du dépôt
(ni `controle_ia.neuron_lens.verdicts_*`, ni autre) : bibliothèque standard seulement.

Lectures paramétrées (plan v2, section 4) :
- tranchées (portent le verdict ; la lettre seule est un calcul d'information) : T-1 `non_sur_partielle` ('addendum' | 'lettre') ;
  T-2 `temoin` ('lisibles' | 'toutes') ; T-3 `a_moities` (True | False) ; T-4 `arrondi` (True | False) ; T-5 `b5_valeurs`
  ('ecrit' | 'flottant') ;
- ouvertes (verdict sous chaque lecture) : O-1 `reproduit_sur_partielle` ('impossible' | 'possible') ; O-2 `garde_b` ('motif' | 'n') ;
  O-4 `lisible_gardes` (False = toutes les couches | True = lisibles seules) ; O-5/O-6 `audit_absent` ('non_conclu' | 'ignore') ;
  O-9 `ce_moities` (False | True).
"""
from __future__ import annotations

import math
from fractions import Fraction

CIBLES = ("steer 1x", "steer 4x", "ablate pos", "ablate win")
NOTRE_R = "R:dclm-llama"
MOITIES = ("R:dclm-llama-even", "R:dclm-llama-odd")
NOTEES = ("logit", "J", "npJpp", "npR", NOTRE_R)
COUCHES_ACCORD = (2, 7, 12, 18, 23, 28)
N_LISIBLE = 48

LECTURE_EN_VIGUEUR = dict(non_sur_partielle="addendum", temoin="lisibles", a_moities=True, arrondi=True, b5_valeurs="ecrit",
                          reproduit_sur_partielle="impossible", garde_b="motif", lisible_gardes=False, audit_absent="non_conclu",
                          ce_moities=False)


def C(a, b):
    return list(range(a, b + 1))


def diff(x, y, L):
    d = float(x) - float(y)
    return round(d, 4) if L["arrondi"] else d


def lisibles(n, couches):
    if n is None:
        return list(couches)
    return [l for l in couches if n[l] >= N_LISIBLE]


def bande(vals, n, couches, ok=None, contraire=None):
    lis = lisibles(n, couches)
    partielle = (len(couches) - len(lis)) > len(couches) / 4
    r = {"couches": [couches[0], couches[-1]], "lisibles": len(lis), "partielle": partielle, "vide": not lis}
    if ok is not None:
        r["ok_lisibles"] = bool(lis) and all(ok(vals[l]) for l in lis)
        r["manquees"] = [l for l in lis if not ok(vals[l])]
    if contraire is not None:
        k = sum(1 for l in lis if contraire(vals[l]))
        r["contraires"] = k
        r["majorite_contraire"] = bool(lis) and k > len(lis) / 2
    return r


def clause_ok(b, L):
    if b["partielle"] and L["reproduit_sur_partielle"] == "impossible":
        return False
    return b["ok_lisibles"]


def clause_non(b, L):
    if b["partielle"] and L["non_sur_partielle"] == "addendum":
        return False
    return b["majorite_contraire"]


def mesure(oks, nons, L):
    if any(clause_non(b, L) for b in nons):
        return "non reproduit"
    if all(clause_ok(b, L) for b in oks):
        return "reproduit"
    return "autre"


# ------------------------------------------------------------------ mesures

def b1(stab, accord):
    diffs = [(k, i, x) for k, v in stab.items() for i, x in enumerate(v)]
    acc = [accord[l] for l in COUCHES_ACCORD]
    dmax = max(diffs, key=lambda t: t[2])
    det = {"difference_max": dmax[2], "ou": f"{dmax[0]} couche {dmax[1]}", "accord_min": min(acc),
           "accord_min_couche": COUCHES_ACCORD[acc.index(min(acc))], "difference_min": min(t[2] for t in diffs)}
    if any(t[2] > 0.20 for t in diffs) or any(a < 0.60 for a in acc):
        v = "non reproduit"
    elif all(t[2] <= 0.10 for t in diffs) and all(a >= 0.80 for a in acc):
        v = "reproduit"
    else:
        v = "autre"
    return v, det


def b2(t, n, L, lent=NOTRE_R):
    s = t["steer 1x"][lent]
    rm, ps, cm = s["r_med"], s["pass"], s["control_med"]
    r1 = bande(rm, n, C(8, 15), ok=lambda v: v >= 0.40)
    r2 = bande(rm, n, C(16, 23), ok=lambda v: v >= 0.60, contraire=lambda v: v < 0.30)
    r3 = bande(rm, n, C(24, 27), ok=lambda v: v >= 0.85)
    p = bande(ps, n, C(8, 27), ok=lambda v: v >= 0.90)
    pn = bande(ps, n, C(16, 27), contraire=lambda v: v < 0.50)
    tem_couches = C(0, 27)
    tl = lisibles(n, tem_couches) if L["temoin"] == "lisibles" else tem_couches
    h05 = [l for l in tl if abs(cm[l]) > 0.05]
    h10 = [l for l in tl if abs(cm[l]) > 0.10]
    tb = {"partielle": (len(tem_couches) - len(lisibles(n, tem_couches))) > 7 if L["temoin"] == "lisibles" else False,
          "ok_lisibles": len(h05) <= 1 and not h10, "vide": not tl}
    v = mesure([r1, r2, r3, p, tb], [pn, r2], L)
    det = {"r_med_8_15": r1, "r_med_16_23": r2, "r_med_24_27": r3, "pass_8_27": p, "pass_16_27_non": pn,
           "temoin_hors_005": h05, "temoin_hors_010": h10,
           "min_r_med_8_15": min(rm[l] for l in C(8, 15)), "min_r_med_16_23": min(rm[l] for l in C(16, 23)),
           "min_r_med_24_27": min(rm[l] for l in C(24, 27)), "min_pass_8_27": min(ps[l] for l in C(8, 27))}
    return v, det


def b3(t, n, L, lent=NOTRE_R):
    e = [diff(t["steer 1x"][lent]["r_med"][l], t["steer 1x"]["logit"]["r_med"][l], L) for l in range(32)]
    b = bande(e, n, C(4, 15), ok=lambda v: v >= 0.20, contraire=lambda v: v <= 0)
    return mesure([b], [b], L), {"ecarts_4_15": e[4:16], "ecart_min": min(e[4:16]),
                                 "couche_min": 4 + e[4:16].index(min(e[4:16])), "bande": b}


def b4(t, L):
    r = t["steer 1x"][NOTRE_R]["r_med"]
    out = {}
    for k in ("J", "npJpp"):
        e = [diff(r[l], t["steer 1x"][k]["r_med"][l], L) for l in C(4, 23)]
        out[k] = {"ecarts_4_23": e, "negatifs": sum(x < 0 for x in e), "positifs": sum(x > 0 for x in e)}
    return out


def b5(read_S, silent, L):
    f = (lambda x: Fraction(repr(float(x)))) if L["b5_valeurs"] == "ecrit" else float
    rs, si = [f(x) for x in read_S], [f(x) for x in silent]
    m17, m1223, s17 = sum(rs[1:8]) / 7, sum(rs[12:24]) / 12, sum(si[1:8]) / 7
    det = {"read_S_0": float(rs[0]), "moyenne_1_7": float(m17), "moyenne_12_23": float(m1223), "ecart": float(m17 - m1223),
           "silent_0": float(si[0]), "silent_moyen_1_7": float(s17)}
    if si[0] > f("0.40") or s17 > f("0.50"):
        return "non lisible", det
    if rs[0] < f("0.30") or m17 <= m1223:
        return "non reproduit", det
    if rs[0] >= f("0.60") and m17 - m1223 >= f("0.10"):
        return "reproduit", det
    return "autre", det


def b6(t, n, L):
    r, p = t["steer 1x"][NOTRE_R]["r_med"], t["steer 1x"]["npR"]["r_med"]
    ec = [abs(diff(r[l], p[l], L)) for l in range(28)]
    couches = lisibles(n, C(0, 27)) if L["lisible_gardes"] else C(0, 27)
    au_dela = [l for l in couches if ec[l] > 0.15]
    sous05 = sum(1 for l in couches if ec[l] <= 0.05)
    v = "désaccord" if au_dela else ("accord" if sous05 >= 21 else "intermédiaire")
    return v, {"ecarts_abs": ec, "au_dela_015": au_dela, "couches_sous_005": sous05, "max": max(ec[l] for l in couches)}


def a6(t, n, L):
    v, det = b6(t, n, L)
    if v != "désaccord":
        return None
    r = t["steer 1x"][NOTRE_R]["r_med"]
    stable = all(all(abs(diff(t["steer 1x"][m]["r_med"][l], r[l], L)) < 0.05 for m in MOITIES) for l in det["au_dela_015"])
    return "écart de corpus" if stable else "écart d'ajustement"


def b7(t, n, L, lent=NOTRE_R):
    a = t["ablate win"][lent]["r_med"]
    bas = bande(a, n, C(0, 15), ok=lambda v: v < 0.25)
    haut_non = bande(a, n, C(8, 15), contraire=lambda v: v >= 0.40)
    tard = bande(a, n, C(26, 29), ok=lambda v: v >= 0.50, contraire=lambda v: v < 0.30)
    v = mesure([bas, tard], [haut_non, tard], L)
    par_haut, par_bas = clause_non(haut_non, L), clause_non(tard, L)
    det = {"bas_0_15": bas, "haut_8_15": haut_non, "tard_26_29": tard, "par_le_haut": par_haut, "par_le_bas": par_bas,
           "max_0_15": max(a[l] for l in C(0, 15)), "min_26_29": min(a[l] for l in C(26, 29)), "r_med": list(a)}
    return v, det


# ------------------------------------------------------------------ gardes recalculables sur la sortie de score

def gardes_score(t, n, L, lentilles=None, ecartes_nul=None, avec_e=True, repere=None):
    """Rend {lettre: [motifs]} pour (a), (b), (c), part « score » de (e), (j). `ecartes_nul` : pôles écartés pour effet nul en
    « steer 1x », par couche (lecture O-2 (i)) ; sinon n (lecture O-2 (ii))."""
    lentilles = lentilles or (NOTEES + (MOITIES if L["a_moities"] else ()))
    zone = lambda couches: lisibles(n.get("steer 1x") if n else None, couches) if L["lisible_gardes"] else couches
    d = {"a": [], "b": [], "c": [], "e": [], "j": []}
    for c in CIBLES:
        for le in lentilles:
            if le not in t[c]:
                continue
            cz = lisibles(n.get(c) if n else None, C(0, 27)) if L["lisible_gardes"] else C(0, 27)
            hors = [l for l in cz if abs(t[c][le]["control_med"][l]) > 0.10]
            if hors:
                d["a"].append(f"{c}, {le}, couches {hors}")
    if L["garde_b"] == "motif":
        if ecartes_nul is None:
            d["b"] = None  # non calculable sur ces pièces
        else:
            k = [l for l in zone(C(0, 27)) if ecartes_nul[l] > 32]
            if k:
                d["b"].append(f"plus de 32 pôles écartés pour effet nul aux couches {k}")
    else:
        if n is None:
            d["b"] = None
        else:
            k = [l for l in zone(C(0, 27)) if n["steer 1x"][l] < 32]
            if k:
                d["b"].append(f"moins de 32 pôles retenus aux couches {k}")
    seuils = {"logit": 0.80, "npR": 0.85, NOTRE_R: 0.85}
    if L["ce_moities"]:
        seuils.update({m: 0.85 for m in MOITIES})
    for le, s in seuils.items():
        if le in t["steer 1x"]:
            k = [l for l in C(28, 30) if t["steer 1x"][le]["r_med"][l] < s]
            if k:
                d["c"].append(f"{le} sous {s} aux couches {k}")
    if avec_e:
        lg = t["steer 1x"]["logit"]["r_med"]
        for le in ("J", "npJpp", "npR", NOTRE_R) + (MOITIES if L["ce_moities"] else ()):
            if le in t["steer 1x"]:
                k = [l for l in zone(C(0, 23)) if abs(diff(t["steer 1x"][le]["r_med"][l], lg[l], L)) < 1e-3]
                if k:
                    d["e"].append(f"{le} à moins de 10⁻³ des logits aux couches {k}")
    if repere is not None:
        ec = [abs(diff(t["steer 1x"]["npR"]["r_med"][l], repere[l], L)) for l in range(28)]
        zz = zone(C(0, 27))
        p05 = [l for l in zz if ec[l] > 0.05]
        p10 = [l for l in zz if ec[l] > 0.10]
        if len(p05) > 2 or p10:
            d["j"].append(f"écart à la série repère > 0,05 aux couches {p05}, > 0,10 aux couches {p10}")
        d["j_detail"] = {"max": max(ec[l] for l in zz), "au_dela_005": p05}
    else:
        d["j"] = None
    return d


# ------------------------------------------------------------------ déclencheurs

def declencheurs(t, n, stab, accord, read_S, L):
    s = t["steer 1x"][NOTRE_R]
    out = {}
    out["A1"] = any(s["r_med"][l] >= 0.95 for l in C(0, 7)) or sum(1 for l in C(0, 27) if round(s["control_med"][l], 4) == 0) >= 2
    if stab is not None and accord is not None:
        diffs = [x for v in stab.values() for x in v]
        out["A2"] = any(x < 1e-6 for x in diffs) or all(accord[l] == 1 for l in COUCHES_ACCORD)
        out["A3"] = b1(stab, accord)[0] == "non reproduit"
    else:
        out["A2"] = out["A3"] = None
    out["A4"] = (read_S[0] >= 0.99 or all(x == 0 for x in read_S)) if read_S is not None else None
    out["A5"] = b7(t, n.get("ablate win") if n else None, L)[1]["par_le_haut"]
    out["A6"] = b6(t, n.get("steer 1x") if n else None, L)[0] == "désaccord"
    return out


# ------------------------------------------------------------------ verdict

def verdict(e, L=None, audits=None):
    """`e` : dict avec `score` (targets), `n` ({cible: liste} ou None), `ecartes_nul` (liste ou None), `repere` (liste),
    `stab` ({nom: liste}), `accord` ({couche: valeur}), `read_S`, `silent`, `gardes_machine` ({lettre: True si en défaut, False si
    tenue, None si inconnue}). `audits` : {audit: résultat | 'non joué' | None (aucune trace)}."""
    L = dict(LECTURE_EN_VIGUEUR, **(L or {}))
    audits = dict(audits or {})
    t, n = e["score"], e.get("n")
    n1 = n.get("steer 1x") if n else None
    nw = n.get("ablate win") if n else None
    g = gardes_score(t, n, L, ecartes_nul=e.get("ecartes_nul"), repere=e.get("repere"))
    defauts = [f"({k}) {m}" for k in ("a", "b", "c", "e", "j") if g[k] for m in g[k]]
    inconnues = [k for k in ("b", "j") if g[k] is None]
    stab_nf = e["stab"] is not None and any(not math.isfinite(x) for v in e["stab"].values() for x in v)
    if stab_nf:
        defauts.append("(g) différence entre moitiés non finie")
    gm = e.get("gardes_machine") or {}
    defauts += [f"({k}) constatée sur la machine" for k, v in sorted(gm.items()) if v is True]
    inconnues += [k for k, v in sorted(gm.items()) if v is None]
    m = {}
    if not stab_nf:
        m["B-1"] = b1(e["stab"], e["accord"]) if e["stab"] is not None else ("inconnu", {})
    m["B-2"] = b2(t, n1, L)
    m["B-3"] = b3(t, n1, L)
    m["B-4"] = ("rapportée", b4(t, L))
    m["B-5"] = b5(e["read_S"], e["silent"], L)
    m["B-6"] = b6(t, n1, L)
    m["B-7"] = b7(t, nw, L)
    m = {k: [v, d] for k, v, d in ((k, *x) for k, x in m.items())}
    trig = declencheurs(t, n, None if stab_nf else e["stab"], e["accord"], e["read_S"], L)
    reserves, non_conclu, issues = [], [], {}
    a6r = a6(t, n1, L)
    if a6r:
        reserves.append(a6r)
        issues["A6"] = a6r

    def absent(a):
        r = audits.get(a)
        return r is None or r == "non joué"

    relance_audits = [a for a in ("A1", "A5") if trig.get(a)]
    if relance_audits:
        r = audits.get("A1") if "A1" in relance_audits else audits.get("A5")
        if absent("A1" if "A1" in relance_audits else "A5"):
            issues["+".join(relance_audits)] = "non joué" if r == "non joué" else "aucune trace"
            if "A1" in relance_audits and (r == "non joué" or L["audit_absent"] == "non_conclu"):
                non_conclu.append("A1")
            if "A5" in relance_audits and (r == "non joué" or L["audit_absent"] == "non_conclu"):
                m["B-7"][0] = "autre"
                m["B-7"][1]["audit_A5"] = issues["+".join(relance_audits)]
        elif not (r["temoin_distinct"] and r["normes_non_nulles"]):
            defauts.append("(l) témoin ou pilotage dégénéré")
            issues["+".join(relance_audits)] = "chaîne en défaut (l)"
        else:
            g1 = gardes_score(r["score"], r["n"], L, lentilles=("logit", "npR", NOTRE_R), avec_e=False)
            d1 = [x for k in ("a", "b", "c") if g1[k] for x in g1[k]]
            if d1:
                defauts.append("(l) garde (a) à (c) manquée sous la graine 1 : " + " ; ".join(d1))
                issues["+".join(relance_audits)] = "chaîne en défaut (l)"
            else:
                issues["+".join(relance_audits)] = "joué"
                n1b, nwb = r["n"].get("steer 1x"), r["n"].get("ablate win")
                if "A1" in relance_audits:
                    for k, f, nn in (("B-2", b2, n1b), ("B-3", b3, n1b), ("B-7", b7, nwb)):
                        if f(r["score"], nn, L)[0] != m[k][0]:
                            m[k][0] = "autre"
                if "A5" in relance_audits and not b7(r["score"], nwb, L)[1]["par_le_haut"]:
                    m["B-7"][0] = "autre"
    for a in ("A2", "A3"):
        if trig.get(a):
            if absent(a):
                issues[a] = audits.get(a) or "aucune trace"
                if audits.get(a) == "non joué" or L["audit_absent"] == "non_conclu":
                    non_conclu.append(a)
            elif not audits[a]["controles_ok"]:
                defauts.append(f"(g) moitiés ou documents non conformes ({a})")
                issues[a] = "chaîne en défaut (g)"
            else:
                issues[a] = "joué, contrôles tenus"
    if trig.get("A4"):
        if absent("A4"):
            issues["A4"] = audits.get("A4") or "aucune trace"
            if audits.get("A4") == "non joué" or L["audit_absent"] == "non_conclu":
                non_conclu.append("A4")
        else:
            r = audits["A4"]
            if not r["permutation_ok"]:
                defauts.append("(m) appariement dégénéré (A4)")
            if not r["lentille_S_ok"]:
                defauts.append("(k) lentille S différente (A4)")
            issues["A4"] = "joué" if r["permutation_ok"] and r["lentille_S_ok"] else "chaîne en défaut"
    rang3 = "non reproduit" in (m["B-2"][0], m["B-3"][0])
    if rang3 and g["j"] == []:
        pass  # audit « tout négatif » : (j) tenue
    if defauts:
        v = "chaîne en défaut"
    elif non_conclu:
        v = "non conclu"
        reserves.append("audit non joué : " + ", ".join(non_conclu))
    elif rang3:
        v = "non reproduit avec nos lentilles"
        reserves.append("défaut dans notre lentille")
    elif all(m.get(k, ["?"])[0] == "reproduit" for k in ("B-1", "B-2", "B-3", "B-5")):
        v = "reproduit avec nos lentilles"
    else:
        v = "partiel"
    return {"verdict": v, "defauts": defauts, "gardes_inconnues": inconnues, "reserves": reserves, "declencheurs": trig,
            "issues_audits": issues, "mesures": {k: x[0] for k, x in m.items()}, "details": {k: x[1] for k, x in m.items()},
            "gardes_score": g, "lecture": L}


# ------------------------------------------------------------------ référence de Qwen3-8B ramenée à 32 couches

def depuis_reference(causal_qwen, reads_qwen):
    role = {"logit": "logit", "J": "J", "npJpp": "J", "npR": "R:dclm", NOTRE_R: "R:dclm", MOITIES[0]: "R:dclm", MOITIES[1]: "R:dclm"}
    idx = [(l * 36) // 32 for l in range(32)]
    t = {}
    for c in CIBLES:
        t[c] = {}
        for le, src in role.items():
            q = causal_qwen["targets"][c][src]
            t[c][le] = {"layer": list(range(32)), **{k: [q[k][i] for i in idx] for k in ("r_med", "pass", "control_med")}}
    Ls = reads_qwen["neurons"]["layers"]
    return t, [Ls[i]["read_S"] for i in idx], [Ls[i]["silent"] for i in idx]
