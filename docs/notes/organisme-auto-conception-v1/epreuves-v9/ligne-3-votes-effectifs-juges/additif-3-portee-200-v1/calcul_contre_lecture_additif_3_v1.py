"""Calcul de contre-lecture — additif 3 de la ligne 3 (portée à 200) — v1.

Contre-lecteur, modèle O. Aucun tirage aléatoire, aucune graine, aucun appel de modèle.
Ne lance ni n'importe le banc : les formules du monde de puissance sont réécrites ici, à la main,
d'après le texte (l. 236 à 240) et l'additif 1 (règles B et C).

Ce que ce programme calcule :
 1. Faisabilité des 210 cellules (bissection, loi 3 jouable) : ne dépend pas de n.
 2. Une approximation de la puissance de chaque comparaison, par cellule faisable, à n = 100 et à n = 200 :
    - loi exacte, par classe, des erreurs des bras (U, S1, S2, R3, et la règle choisie par C) sur un témoin ;
    - loi exacte de la règle choisie par le bras C sur la moitié d'étalonnage (énumération des comptes
      multinomiaux, réécriture de la règle de covariance du texte : w = (S + lambda I)^-1 d, bornes 0,2 à 5,
      seuil au milieu, égalité à 1e-9 près) ;
    - approximation normale de l'écart apparié sur la moitié « lecture », avec deux bornes de Holm :
      basse = rejet au seuil alpha / 4 (suffisant), haute = rejet au seuil alpha (nécessaire) ;
      écart observé de 0,05 au moins exigé dans les deux.
 3. Les chiffres du compteur à 200 témoins et au plafond 88,36 USD, sur les tarifs du devis v7.
 4. L'égalité, à l'octet, de la ligne GO-2026-11-20-26 citée par l'additif et de celle du registre.

Usage : python3 calcul_contre_lecture_additif_3_v1.py ADDITIF GO_MAIN GO_E50FF62E SORTIE
"""
import hashlib
import json
import math
import sys
from statistics import NormalDist

import numpy as np

P_MOY = 0.20
D_MAX = 0.20
F_DIFF = 0.25
EPS = 1e-12
RHOS = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
RHOS_P = (0.0, 0.5, 0.9)
ECARTS = (0.05, 0.10, 0.15)
LOIS = (1, 3)
COMPARAISONS = ("unanimite", "juge_seul", "juge_repete_trois_votes_majorite")
ALPHA = 0.05
MARGE = 0.05
ND = NormalDist()


def conj(p, r):
    return p * p + r * p * (1 - p)


def maj3(p, rp):
    return rp * p + (1 - rp) * (3 * p * p - 2 * p ** 3)


def ee(d, rho, rp):
    a, b = P_MOY + d, P_MOY - d
    a11, b11 = conj(a, rho), conj(b, rho)
    return {"F": (a11 + 2 * b - b11) / 2, "U": (2 * a - a11 + b11) / 2, "S": (a + b) / 2,
            "R": (maj3(a, rp) + maj3(b, rp)) / 2}


CLE = {"unanimite": "U", "juge_seul": "S", "juge_repete_trois_votes_majorite": "R"}


def resoudre(comp, ecart, rho, rp):
    def f(d):
        e = ee(d, rho, rp)
        return e[CLE[comp]] - e["F"] - ecart
    if f(D_MAX) < 0:
        return None
    lo, hi = 0.0, D_MAX
    if f(lo) >= 0:
        return 0.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return hi


def loi3_ok(p, rho):
    x = (rho * p * (1 - p) / (F_DIFF * (1 - F_DIFF))) ** 0.5
    return p - 0.25 * x >= -EPS and p + 0.75 * x <= 1 + EPS


def cellules():
    out = []
    for comp in COMPARAISONS:
        primes = RHOS_P if comp == "juge_repete_trois_votes_majorite" else (0.0,)
        for ecart in ECARTS:
            for loi in LOIS:
                for rho in RHOS:
                    for rp in primes:
                        d = resoudre(comp, ecart, rho, rp)
                        faisable = d is not None
                        if faisable and loi == 3:
                            faisable = loi3_ok(P_MOY + d, rho) and loi3_ok(P_MOY - d, rho)
                        out.append({"comparaison": comp, "ecart": ecart, "loi": loi, "rho": rho, "rho_prime": rp,
                                    "d": d, "faisable": faisable})
    return out


# --- loi d'une paire d'erreurs (juge 1, juge 2, premier rendu), par classe ---------------------------------------
def paire(loi, p, rho):
    if loi == 1:
        p11 = conj(p, rho)
    else:
        x = (rho * p * (1 - p) / (F_DIFF * (1 - F_DIFF))) ** 0.5
        ph, pl = p + 0.75 * x, p - 0.25 * x
        p11 = F_DIFF * ph * ph + (1 - F_DIFF) * pl * pl
    p10 = p - p11
    return {(0, 0): 1 - 2 * p + p11, (0, 1): p10, (1, 0): p10, (1, 1): p11}


def loi_temoin(loi, p, rho, rp):
    """Loi de (e1, e2, r2, r3) : r2, r3 rendus suivants du juge 2 (règle C de l'additif 1), copie avec prob. rho'."""
    out = {}
    for (e1, e2), q in paire(loi, p, rho).items():
        out[(e1, e2, e2, e2)] = out.get((e1, e2, e2, e2), 0.0) + q * rp
        for r2 in (0, 1):
            for r3 in (0, 1):
                w = q * (1 - rp) * (p if r2 else 1 - p) * (p if r3 else 1 - p)
                out[(e1, e2, r2, r3)] = out.get((e1, e2, r2, r3), 0.0) + w
    return out


def erreurs_bras(classe_bon, e1, e2, r2, r3):
    """Erreur de chaque bras sur un témoin (1 = erreur)."""
    maj = 1 if (e2 + r2 + r3) >= 2 else 0
    if classe_bon:
        return {"F": e1 & e2, "U": e1 | e2, "S1": e1, "S2": e2, "R3": maj, "jamais": 1, "toujours": 0}
    return {"F": e1 | e2, "U": e1 & e2, "S1": e1, "S2": e2, "R3": maj, "jamais": 0, "toujours": 1}


REGLE_VERS_BRAS = {"au_moins_un": "F", "unanimite": "U", "juge_1_seul": "S1", "juge_2_seul": "S2",
                   "constante_jamais": "jamais", "constante_toujours": "toujours"}


def moments_diff(loi, a, b, rho, rp, bras_c):
    """Pour chaque comparaison k : (moyenne, variance) par classe de D = err_k − err_C."""
    res = {}
    for k in ("U", "S1", "S2", "R3"):
        res[k] = {}
        for classe_bon, p in ((True, a), (False, b)):
            m1 = m2 = 0.0
            for (e1, e2, r2, r3), q in loi_temoin(loi, p, rho, rp).items():
                er = erreurs_bras(classe_bon, e1, e2, r2, r3)
                dlt = er[k] - er[bras_c]
                m1 += q * dlt
                m2 += q * dlt * dlt
            res[k]["bons" if classe_bon else "mauvais"] = (m1, m2 - m1 * m1)
    return res


def bornes_puissance(mom, m_lecture):
    """Bornes (basse, haute) de la part des répliques gagnées, approximation normale."""
    out = {}
    zb = ND.inv_cdf(1 - ALPHA / 4)
    zh = ND.inv_cdf(1 - ALPHA)
    for k, v in mom.items():
        mu = 0.5 * (v["bons"][0] + v["mauvais"][0])
        var = 0.25 * (v["bons"][1] / m_lecture + v["mauvais"][1] / m_lecture)
        if var <= 1e-15:
            gagne = 1.0 if mu >= MARGE - EPS and mu > 0 else 0.0
            out[k] = (gagne, gagne, mu, 0.0)
            continue
        se = math.sqrt(var)
        bas = 1 - ND.cdf((max(MARGE, zb * se) - mu) / se)
        haut = 1 - ND.cdf((max(MARGE, zh * se) - mu) / se)
        out[k] = (bas, haut, mu, se)
    return out


# --- loi exacte de la règle choisie par le bras C sur la moitié d'étalonnage --------------------------------------
def compositions(m):
    rows = []
    for c00 in range(m + 1):
        for c01 in range(m + 1 - c00):
            for c10 in range(m + 1 - c00 - c01):
                rows.append((c00, c01, c10, m - c00 - c01 - c10))
    return np.array(rows, dtype=np.int64)


def log_pmf(C, probs):
    m = int(C[0].sum())
    lg = np.vectorize(math.lgamma)
    out = math.lgamma(m + 1) - lg(C + 1).sum(axis=1)
    for j, pj in enumerate(probs):
        out = out + C[:, j] * (math.log(pj) if pj > 0 else -np.inf)
    return np.where(np.isfinite(out), out, -np.inf)


def stats_classe(C, bon):
    c00, c01, c10, c11 = (C[:, i].astype(float) for i in range(4))
    m = C.sum(axis=1).astype(float)
    if bon:
        s1 = c00 + c01 - c10 - c11
        s2 = c00 + c10 - c01 - c11
    else:
        s1 = c10 + c11 - c00 - c01
        s2 = c01 + c11 - c00 - c10
    s12 = c00 + c11 - c01 - c10
    ss11 = m - s1 * s1 / m
    ss22 = m - s2 * s2 / m
    ss12 = s12 - s1 * s2 / m
    return s1 / m, s2 / m, ss11, ss22, ss12


def loi_regle_c(loi, a, b, rho, m_cal, seuil_prob=1e-14):
    Cb = compositions(m_cal)
    ordre = ((0, 0), (0, 1), (1, 0), (1, 1))
    pb = paire(loi, a, rho)
    pm = paire(loi, b, rho)
    lb = np.exp(log_pmf(Cb, [pb[o] for o in ordre]))
    lm = np.exp(log_pmf(Cb, [pm[o] for o in ordre]))
    gb = lb > seuil_prob
    gm = lm > seuil_prob
    Cb_g, wb = Cb[gb], lb[gb]
    Cm_g, wm = Cb[gm], lm[gm]
    mb1, mb2, b11, b22, b12 = stats_classe(Cb_g, True)
    mm1, mm2, m11, m22, m12 = stats_classe(Cm_g, False)
    n_cal = 2 * m_cal
    masse = {}
    for i in range(Cb_g.shape[0]):
        S11 = (b11[i] + m11) / (n_cal - 2)
        S22 = (b22[i] + m22) / (n_cal - 2)
        S12 = (b12[i] + m12) / (n_cal - 2)
        d1 = mb1[i] - mm1
        d2 = mb2[i] - mm2
        tr = S11 + S22
        lam = 0.1 * tr / 2
        A11, A22, A12 = S11 + lam, S22 + lam, S12
        det = A11 * A22 - A12 * A12
        with np.errstate(all="ignore"):
            w1 = (A22 * d1 - A12 * d2) / det
            w2 = (A11 * d2 - A12 * d1) / det
        moy = (w1 + w2) / 2
        repli = ~(tr > 1e-12) | ~np.isfinite(w1) | ~np.isfinite(w2) | ~(moy > 0)
        moy_s = np.where(repli, 1.0, moy)
        w1 = np.where(repli, 1.0, np.clip(w1, 0.2 * moy_s, 5.0 * moy_s))
        w2 = np.where(repli, 1.0, np.clip(w2, 0.2 * moy_s, 5.0 * moy_s))
        s = ((w1 * mb1[i] + w2 * mb2[i]) + (w1 * mm1 + w2 * mm2)) / 2
        tol = 1e-9 * (1 + np.abs(s) + np.abs(w1) + np.abs(w2))
        o_mm = (-w1 - w2 - s) > tol
        o_mp = (-w1 + w2 - s) > tol
        o_pm = (w1 - w2 - s) > tol
        o_pp = (w1 + w2 - s) > tol
        code = o_mm.astype(int) * 8 + o_mp.astype(int) * 4 + o_pm.astype(int) * 2 + o_pp.astype(int)
        poids = wb[i] * wm
        cumul = np.bincount(code, weights=poids, minlength=16)
        for c in np.nonzero(cumul)[0]:
            masse[int(c)] = masse.get(int(c), 0.0) + float(cumul[c])
    noms = {1: "unanimite", 7: "au_moins_un", 3: "juge_1_seul", 5: "juge_2_seul", 0: "constante_jamais",
            15: "constante_toujours"}
    out = {}
    for c, v in masse.items():
        out[noms.get(c, f"inconnue_{c}")] = v
    out["_masse_couverte"] = float(sum(masse.values()))
    return out


_CACHE_REGLES = {}


def puissance_approchee(cell, n):
    loi, rho, rp, d = cell["loi"], cell["rho"], cell["rho_prime"], cell["d"]
    a, b = P_MOY + d, P_MOY - d
    m_lect = n // 4
    m_cal = n // 4
    cle = (loi if rho > 0 else 1, rho, round(d, 15), m_cal)
    if cle not in _CACHE_REGLES:
        _CACHE_REGLES[cle] = loi_regle_c(loi, a, b, rho, m_cal)
    regles = _CACHE_REGLES[cle]
    bas = {k: 0.0 for k in ("U", "S1", "S2", "R3")}
    haut = dict(bas)
    par_regle = {}
    for nom, prob in regles.items():
        if nom.startswith("_"):
            continue
        bras_c = REGLE_VERS_BRAS[nom]
        bp = bornes_puissance(moments_diff(loi, a, b, rho, rp, bras_c), m_lect)
        par_regle[nom] = {"probabilite": prob, "bornes": {k: [v[0], v[1]] for k, v in bp.items()}}
        for k in bas:
            bas[k] += prob * bp[k][0]
            haut[k] += prob * bp[k][1]
    cond_f = bornes_puissance(moments_diff(loi, a, b, rho, rp, "F"), m_lect)
    return {"regle_c": regles, "bornes_globales": {k: [bas[k], haut[k]] for k in bas},
            "si_c_vaut_au_moins_un": {k: {"bas": v[0], "haut": v[1], "ecart_moyen": v[2], "ecart_type": v[3]}
                                      for k, v in cond_f.items()},
            "par_regle": par_regle}


QUI = {"unanimite": ("U",), "juge_seul": ("S1", "S2"), "juge_repete_trois_votes_majorite": ("R3",)}


# --- compteur à 200 témoins ---------------------------------------------------------------------------------------
def compteur(n_temoins, plafond, facteur, engagement=0.60):
    o = 6.863 / 94 * facteur
    g = 2.409 / 94 * facteur
    seq = [("P", o), ("P", o), ("P", g), ("P", g)]
    seq += [("A", o)] * n_temoins + [("A", g)] * n_temoins
    for t in range(n_temoins):
        seq += [("B", o, t), ("B", g, t), ("B", g, t)]
    total = sum(x[1] for x in seq)
    cumul = 0.0
    partis = 0
    for x in seq:
        if cumul + engagement > plafond + 1e-12:
            break
        cumul += x[1]
        partis += 1
    complets_b = 0
    idx_b = 4 + 2 * n_temoins
    if partis > idx_b:
        complets_b = (partis - idx_b) // 3
    tous_refuses = int(math.floor(plafond / engagement + 1e-9))
    return {"appels": len(seq), "total_usd": total, "envois_partis": partis, "cumul_compte_usd": cumul,
            "temoins_complets_bloc_b": complets_b, "lecture_complete": complets_b >= n_temoins // 2,
            "tous_refuses_envois": tous_refuses, "tous_refuses_cumul": tous_refuses * engagement}


def multiples(n_temoins, plafond, engagement=0.60):
    o = 6.863 / 94
    g = 2.409 / 94
    utile = plafond - engagement
    pa = 2 * (o + g) + n_temoins * (o + g)
    b = o + 2 * g
    return {"plomberie_et_bloc_a": utile / (pa - g),
            "plus_b_sur_40_lecture": utile / (pa + 40 * b - g),
            "plus_b_sur_la_moitie_lecture": utile / (pa + (n_temoins // 2) * b - g),
            "tout": utile / (pa + n_temoins * b - g)}


def refus_supportes(n_temoins, plafond, facteur, engagement=0.60):
    o = 6.863 / 94 * facteur
    g = 2.409 / 94 * facteur
    total = 2 * (o + g) + n_temoins * (o + g) + n_temoins * (o + 2 * g)
    return int(math.floor((plafond - engagement - total + g) / engagement + 1e-9))


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    additif, go_main, go_e50, sortie = sys.argv[1:5]
    out = {"version": "calcul-contre-lecture-additif-3-ligne-3-v1"}
    # 4. ligne de GO
    lig_add = open(additif, encoding="utf-8").read().split("\n")[6]
    lig_main = open(go_main, encoding="utf-8").read().split("\n")[556]
    lig_e50 = open(go_e50, encoding="utf-8").read().split("\n")[556]
    out["ligne_go"] = {"additif_l7_commence_par_chevron": lig_add.startswith("> "),
                       "egale_main_l557": lig_add[2:] == lig_main,
                       "egale_e50ff62e_l557": lig_add[2:] == lig_e50,
                       "sha256_go_e50ff62e": sha(go_e50), "sha256_go_main": sha(go_main)}
    # 1. faisabilité
    cs = cellules()
    out["cellules"] = len(cs)
    out["faisables_par_ecart"] = {str(e): sum(1 for c in cs if c["faisable"] and abs(c["ecart"] - e) < 1e-12)
                                  for e in ECARTS}
    f10 = [c for c in cs if c["faisable"] and abs(c["ecart"] - 0.10) < 1e-12]
    out["faisables_a_0_10"] = [{k: c[k] for k in ("comparaison", "loi", "rho", "rho_prime", "d")} for c in f10]
    # 2. puissance approchée
    approx = {}
    for n in (100, 200):
        lignes = []
        minimum_bas = minimum_haut = None
        for c in f10:
            r = puissance_approchee(c, n)
            for k in QUI[c["comparaison"]]:
                bb, hh = r["bornes_globales"][k]
                lignes.append({"comparaison": c["comparaison"], "bras": k, "loi": c["loi"], "rho": c["rho"],
                               "rho_prime": c["rho_prime"], "d": c["d"], "borne_basse": bb, "borne_haute": hh,
                               "si_c_vaut_au_moins_un": r["si_c_vaut_au_moins_un"][k],
                               "regle_c": r["regle_c"]})
                minimum_bas = bb if minimum_bas is None else min(minimum_bas, bb)
                minimum_haut = hh if minimum_haut is None else min(minimum_haut, hh)
        approx[str(n)] = {"cellules": lignes, "plus_basse_borne_basse": minimum_bas,
                          "plus_basse_borne_haute": minimum_haut}
    out["puissance_approchee"] = approx
    # 3. compteur
    pire = 6.863 / 3.478
    out["compteur"] = {
        "n100_plafond25_haut": compteur(100, 25.0, 1.0), "n100_plafond25_pire": compteur(100, 25.0, pire),
        "n200_plafond8836_haut": compteur(200, 88.36, 1.0), "n200_plafond8836_pire": compteur(200, 88.36, pire),
        "multiples_n100_plafond25": multiples(100, 25.0), "multiples_n200_plafond8836": multiples(200, 88.36),
        "refus_supportes_n100_haut": refus_supportes(100, 25.0, 1.0),
        "refus_supportes_n200_haut": refus_supportes(200, 88.36, 1.0),
        "refus_supportes_n200_pire": refus_supportes(200, 88.36, pire),
        "facteur_pire": pire,
    }
    texte = json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(texte)


if __name__ == "__main__":
    main()
