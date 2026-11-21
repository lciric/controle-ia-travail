"""Calculs de la note « taxe d'obscurcissement dans un bras d'attaque déclaré » — Opus 5.5, effort maximal, v1.

Aucun tirage : lois exactes (normale, par erfc) et optimisations déterministes (programmation linéaire par HiGHS,
grilles fixes, bissections, affinage borné). Aucune donnée du programme. Toutes les valeurs d'entrée sont des
suppositions d'illustration, écrites ci-dessous. Approximation déclarée : chaque statistique de test est traitée
comme normale de variance 1 (somme de T épisodes indépendants) ; le changement de variance sous attaque est négligé ;
la fréquence de sabotage n'est pas bornée par 1 (T grand).

Notations (par épisode ; les taux sont en unités de 1/sqrt(T), si bien que T disparaît des rapports) :
  q      réussite attendue de l'honnête ; sigma = sqrt(q(1-q)) écart type de l'issue honnête
  f      taux de fausses alertes de la sonde par épisode honnête ; s_w = sqrt(f(1-f))
  r      rappel de la sonde sur un épisode saboté sans obscurcissement
  d      dommage visé par épisode saboté (baisse de réussite que l'oracle compte, dans sa couverture)
  r_o    rappel résiduel de la sonde sur un épisode saboté obscurci
  tau    perte supplémentaire, vue par l'oracle, que l'obscurcissement cause sur l'épisode où il sert
  k_cap  part du dommage visé que l'obscurcissement fait perdre (taxe de compétence) : d' = d (1 - k_cap)
  k_eff  = tau / (d' + tau) : part de la perte vue par l'oracle qui n'est pas du dommage visé

Blocs :
  A. Coup unique : la valeur de l'étau est min(r, kappa) (cas concentré, pour mémoire).
  B. Régime diffus, deux tests séparés (bilan sur l'issue ; compte des alertes de la sonde), seuils de Bonferroni,
     contrainte « sous le fil » (statistique attendue au plus au seuil) : programme linéaire.
  C. Même jeu, contrainte en probabilité : l'attaquant garde au moins une chance sur deux de ne pas être pris.
  D. Une seule statistique jointe, combinaison linéaire fixée d'avance par le défenseur (minimax).
  E. Taxe permanente (sur tous les épisodes, sabotés ou non) : horizon au-delà duquel le bilan seul la voit.
  F. Tailles : épisodes appariés nécessaires pour borner k_eff par le haut quand la vraie perte vue est nulle.
  G. Poids de la sonde dans la statistique jointe : réglé sur le non adaptatif, ou minimax sur la frontière.
  H. Deux tests séparés à partage inégal du niveau : la part epsilon du niveau alpha donnée à la sonde.
Deux réglages de sonde : « forte » (r = 0,8 ; f = 0,01) et « moyenne » (r = 0,4 ; f = 0,05).
V est rapporté au bilan du même dispositif (même seuil) : V = 1 - dommage soutenable / dommage soutenable du bilan
seul dans ce dispositif. V0 (blocs B et C) est rapporté au bilan seul au niveau alpha, sans la sonde.
Les objets de contrôle sont des assertions écrites avant l'exécution.
"""

import math

import numpy as np
from scipy.optimize import linprog, minimize_scalar
from scipy.stats import norm

# --- suppositions d'illustration -------------------------------------------------------------------------------
Q = 0.8
SIGMA = math.sqrt(Q * (1 - Q))
ALPHA = 0.05
Z1 = float(norm.ppf(1 - ALPHA))        # un seul test au niveau alpha
Z2 = float(norm.ppf(1 - ALPHA / 2))    # deux tests séparés, Bonferroni
DOMMAGES = [0.05, 0.20, 0.50]          # subtil, moyen, franc (borné par q)
SONDES = [("sonde forte", 0.8, 0.01), ("sonde moyenne", 0.4, 0.05)]


def frontiere(r, f):
    """Points de la frontière d'obscurcissement : (nom, rappel résiduel, tau, k_cap)."""
    return [
        ("F1 complet et gratuit", f, 0.00, 0.0),
        ("F2 taxe de compétence pure (k_cap 0,5)", f, 0.00, 0.5),
        ("F3 complet, perte vue 0,01", f, 0.01, 0.0),
        ("F4 complet, perte vue 0,05", f, 0.05, 0.0),
        ("F5 complet, perte vue 0,20", f, 0.20, 0.0),
        ("F6 complet, perte vue 0,05 et k_cap 0,5", f, 0.05, 0.5),
        ("F7 plancher de rappel r/2, aucune perte", r / 2, 0.00, 0.0),
        ("F8 obscurcissement inutile", r, 0.00, 0.0),
    ]


def strategies(d, r, f, point=None):
    """Liste de (dommage visé, perte vue par l'oracle, excès d'alertes) par unité de fréquence."""
    out = [(d, d, max(r - f, 0.0))]
    if point is not None:
        _, r_o, tau, k_cap = point
        d_o = d * (1 - k_cap)
        out.append((d_o, d_o + tau, max(r_o - f, 0.0)))
    return out


def k_eff(d, point):
    _, _, tau, k_cap = point
    d_o = d * (1 - k_cap)
    return tau / (d_o + tau) if (d_o + tau) > 0 else 0.0


def phi_norm(x):
    """Fonction de répartition de la loi normale centrée réduite (forme exacte par erfc)."""
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


# --- B. programme linéaire, deux tests séparés ------------------------------------------------------------------
def lp_separes(strats, f, z=Z2):
    s_w = math.sqrt(f * (1 - f))
    c = [-s[0] for s in strats]
    a_ub = [[s[1] for s in strats], [s[2] for s in strats]]
    b_ub = [z * SIGMA, z * s_w]
    res = linprog(c, A_ub=a_ub, b_ub=b_ub, bounds=[(0, None)] * len(strats), method="highs")
    assert res.status == 0, res.message
    return -res.fun  # dommage soutenable (unités 1/sqrt(T))


# --- C. contrainte en probabilité --------------------------------------------------------------------------------
def proba_non_prise(p, strats, f, z):
    s_w = math.sqrt(f * (1 - f))
    mu_b = sum(pi * s[1] for pi, s in zip(p, strats)) / SIGMA
    mu_w = sum(pi * s[2] for pi, s in zip(p, strats)) / s_w
    return phi_norm(z - mu_b) * phi_norm(z - mu_w)


def dommage_pour_part(phi, strats, f, z):
    parts = [1 - phi, phi] if len(strats) == 2 else [1.0]
    lo, hi = 0.0, 1.0
    while proba_non_prise([hi * x for x in parts], strats, f, z) >= 0.5:
        hi *= 2.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if proba_non_prise([mid * x for x in parts], strats, f, z) >= 0.5:
            lo = mid
        else:
            hi = mid
    return lo * sum(x * s[0] for x, s in zip(parts, strats))


def proba_separes(strats, f, z=Z2, grille=401):
    if len(strats) == 1:
        return dommage_pour_part(0.0, strats, f, z)
    phis = np.linspace(0.0, 1.0, grille)
    vals = [dommage_pour_part(float(ph), strats, f, z) for ph in phis]
    i = int(np.argmax(vals))
    lo, hi = phis[max(i - 1, 0)], phis[min(i + 1, grille - 1)]
    res = minimize_scalar(lambda ph: -dommage_pour_part(float(ph), strats, f, z), bounds=(lo, hi),
                          method="bounded", options={"xatol": 1e-10})
    return max(vals[i], -float(res.fun))


def bilan_seul_proba(f, z=Z2):
    """Dommage soutenable par le seul canal du bilan quand la sonde tourne aussi (aucune alerte en excès)."""
    return dommage_pour_part(0.0, [(1.0, 1.0, 0.0)], f, z)


# --- D. statistique jointe -------------------------------------------------------------------------------------
def ratio_joint(theta, strats, f):
    s_w = math.sqrt(f * (1 - f))
    vals = []
    for d_i, b_i, w_i in strats:
        den = math.cos(theta) * b_i + math.sin(theta) * w_i * SIGMA / s_w
        vals.append(math.inf if den <= 0 else d_i / den)
    return max(vals)


def joint(strats, f):
    """Rapport au bilan seul au même seuil Z1 ; le défenseur choisit le poids d'avance (minimax)."""
    thetas = np.linspace(0.0, math.pi / 2, 4001)
    vals = np.array([ratio_joint(t, strats, f) for t in thetas])
    i = int(np.argmin(vals))
    lo, hi = thetas[max(i - 1, 0)], thetas[min(i + 1, len(thetas) - 1)]
    res = minimize_scalar(lambda t: ratio_joint(t, strats, f), bounds=(lo, hi), method="bounded",
                          options={"xatol": 1e-12})
    return min(float(vals[i]), float(res.fun))


def fmt(x):
    return f"{x:+.4f}"


lignes = []
p = lignes.append
p("Calculs de la note sur la taxe d'obscurcissement (Opus 5.5, effort maximal), v1")
p(f"Suppositions : q = {Q}, sigma = {SIGMA:.4f}, alpha = {ALPHA}, Z1 = {Z1:.4f}, Z2 = {Z2:.4f} ; "
  "sondes : forte (r = 0,8 ; f = 0,01), moyenne (r = 0,4 ; f = 0,05)")
p("V = 1 - dommage soutenable / dommage soutenable du bilan seul dans le même dispositif ; V0 : rapporté au bilan "
  "seul au niveau alpha, sans sonde (blocs B et C).")
p("")

# --- A. coup unique ---------------------------------------------------------------------------------------------
p("A. Coup unique (concentré) : succès S(h) = (1-h)(1-r) + h(1-kappa), h = probabilité de tout cacher, r = 0,8")
for kappa in [0.0, 0.1, 0.3, 0.5, 0.9]:
    hs = np.linspace(0, 1, 1001)
    s = (1 - hs) * (1 - 0.8) + hs * (1 - kappa)
    v = 1 - float(s.max())
    assert abs(v - min(0.8, kappa)) < 1e-12  # contrôle écrit avant : sommet, donc min(r, kappa)
    p(f"  kappa = {kappa:.1f} : V = {v:.4f} = min(r, kappa)")
p("")

for nom_sonde, r, f in SONDES:
    s_w = math.sqrt(f * (1 - f))
    ref0 = Z1 * SIGMA  # bilan seul, niveau alpha, sans sonde
    # --- B ---
    p(f"B. [{nom_sonde}] Régime diffus, deux tests séparés au seuil Z2, contrainte « sous le fil » (programme "
      "linéaire)")
    ref_b = Z2 * SIGMA  # bilan seul dans ce dispositif
    for d in DOMMAGES:
        dn = lp_separes(strategies(d, r, f), f)
        v_nom, v0_nom = 1 - dn / ref_b, 1 - dn / ref0
        p(f"  d = {d:.2f} : V_nom = {fmt(v_nom)} (V0_nom = {fmt(v0_nom)})")
        for point in frontiere(r, f):
            nom, r_o, tau, k_cap = point
            if d * (1 - k_cap) + tau > Q:
                p(f"    {nom} : hors domaine (perte totale > q)")
                continue
            da = lp_separes(strategies(d, r, f, point), f)
            v_ad, v0_ad = 1 - da / ref_b, 1 - da / ref0
            ke = k_eff(d, point)
            p(f"    {nom} : V_adapt = {fmt(v_ad)} (V0 = {fmt(v0_ad)}) ; k_eff = {ke:.4f} ; "
              f"produit = {v_nom * ke:.4f} ; min = {min(v_nom, ke):.4f}")
            if r_o <= f:
                assert abs(v_ad - v_nom * ke) < 1e-9, (nom, d, v_ad)   # loi du produit (contrôle écrit avant)
            if tau == 0.0 and r_o <= f:
                assert abs(v_ad) < 1e-9                                 # aucune perte vue : aucune valeur
            if r_o == r and tau == 0.0 and k_cap == 0.0:
                assert abs(v_ad - v_nom) < 1e-9                         # obscurcissement inutile
            assert v_ad <= min(v_nom, ke) + 1e-9 or r_o > f             # sous le min quand l'obscurcissement est complet
    p("")
    # --- C ---
    p(f"C. [{nom_sonde}] Contrainte en probabilité (P(non pris) >= 1/2), deux tests séparés au seuil Z2")
    ref_c = bilan_seul_proba(f)
    for d in DOMMAGES:
        dn = proba_separes(strategies(d, r, f), f)
        v_nom = 1 - dn / ref_c
        p(f"  d = {d:.2f} : V_nom = {fmt(v_nom)} (V0_nom = {fmt(1 - dn / ref0)})")
        for point in frontiere(r, f):
            nom, r_o, tau, k_cap = point
            if d * (1 - k_cap) + tau > Q:
                continue
            da = proba_separes(strategies(d, r, f, point), f)
            v_ad = 1 - da / ref_c
            ke = k_eff(d, point)
            p(f"    {nom} : V_adapt = {fmt(v_ad)} (V0 = {fmt(1 - da / ref0)}) ; k_eff = {ke:.4f} ; "
              f"produit = {v_nom * ke:.4f} ; min = {min(v_nom, ke):.4f}")
            if tau == 0.0 and r_o <= f:
                assert abs(v_ad) < 1e-6   # contrôle : complet et gratuit, aucune valeur
    p("")
    # --- D ---
    p(f"D. [{nom_sonde}] Une seule statistique jointe au seuil Z1 (poids fixé d'avance par le défenseur, minimax)")
    for d in DOMMAGES:
        v_nom = 1 - joint(strategies(d, r, f), f)
        p(f"  d = {d:.2f} : V_nom = {fmt(v_nom)}")
        for point in frontiere(r, f):
            nom, r_o, tau, k_cap = point
            if d * (1 - k_cap) + tau > Q:
                continue
            v_ad = 1 - joint(strategies(d, r, f, point), f)
            ke = k_eff(d, point)
            p(f"    {nom} : V_adapt = {fmt(v_ad)} ; k_eff = {ke:.4f} ; produit = {v_nom * ke:.4f} ; "
              f"min = {min(v_nom, ke):.4f}")
            if tau == 0.0 and r_o <= f:
                assert abs(v_ad) < 1e-6   # contrôle : complet et gratuit, aucune valeur
            if r_o <= f:
                assert v_ad <= min(v_nom, ke) + 1e-6   # la borne du min tient (contrôle écrit avant)
    p("")
    # --- G ---
    p(f"G. [{nom_sonde}] Poids de la sonde dans la statistique jointe : réglé sur l'attaquant non adaptatif, ou minimax")
    p("   sur un ensemble de points possibles de la frontière (le défenseur ignore lequel l'attaquant atteint)")
    thetas = np.linspace(0.0, math.pi / 2, 4001)
    for d in DOMMAGES:
        nominal = strategies(d, r, f)
        vals_nom = np.array([ratio_joint(t, nominal, f) for t in thetas])
        t_nom = float(thetas[int(np.argmin(vals_nom))])
        cells = []
        for point in frontiere(r, f):
            if d * (1 - point[3]) + point[2] > Q:
                continue
            v = 1 - ratio_joint(t_nom, strategies(d, r, f, point), f)
            cells.append(f"{point[0][:2]} {v:+.2f}")
        p(f"  d = {d:.2f} : poids réglé sur le non adaptatif (angle {math.degrees(t_nom):.1f} degrés) ; V_adapt par point : "
          + " ; ".join(cells))
        for etiquette, garde in [("tous les points, F1 et F2 compris", lambda pt: True),
                                 ("F1 et F2 exclus par la mesure", lambda pt: pt[0][:2] not in ("F1", "F2"))]:
            ens = [pt for pt in frontiere(r, f) if garde(pt) and d * (1 - pt[3]) + pt[2] <= Q]
            pire = np.array([max(ratio_joint(t, strategies(d, r, f, pt), f) for pt in ens) for t in thetas])
            j = int(np.argmin(pire))
            v_mm = 1 - float(pire[j])
            p(f"    minimax, {etiquette} : angle {math.degrees(float(thetas[j])):.1f} degrés ; V garanti = {v_mm:+.4f}")
            if etiquette.startswith("tous"):
                assert abs(float(thetas[j])) < 1e-12 and abs(v_mm) < 1e-9  # contrôle : poids nul si la gratuité est possible
    p("")

# --- H. partage inégal du niveau entre les deux tests séparés --------------------------------------------------
def lp_partage(strats, f, zb, zw):
    s_w = math.sqrt(f * (1 - f))
    c = [-s[0] for s in strats]
    res = linprog(c, A_ub=[[s[1] for s in strats], [s[2] for s in strats]], b_ub=[zb * SIGMA, zw * s_w],
                  bounds=[(0, None)] * len(strats), method="highs")
    assert res.status == 0, res.message
    return -res.fun


p("H. Deux tests séparés, part epsilon du niveau alpha donnée à la sonde (le bilan garde alpha(1 - epsilon)) ;")
p("   V0 rapporté au bilan seul au niveau alpha ; programme linéaire « sous le fil »")
for nom_sonde, r, f in SONDES:
    for d in DOMMAGES:
        cells = []
        for eps in [0.5, 0.2, 0.1, 0.05, 0.01]:
            zb = float(norm.ppf(1 - ALPHA * (1 - eps)))
            zw = float(norm.ppf(1 - ALPHA * eps))
            ref0 = Z1 * SIGMA
            v_nom = 1 - lp_partage(strategies(d, r, f), f, zb, zw) / ref0
            v_f1 = 1 - lp_partage(strategies(d, r, f, frontiere(r, f)[0]), f, zb, zw) / ref0
            v_f4 = 1 - lp_partage(strategies(d, r, f, frontiere(r, f)[3]), f, zb, zw) / ref0
            cells.append(f"eps {eps:.2f} : nominal {v_nom:+.3f}, F1 {v_f1:+.3f}, F4 {v_f4:+.3f}")
        p(f"  [{nom_sonde}] d = {d:.2f} : " + " | ".join(cells))
p("")

# --- E. taxe permanente -----------------------------------------------------------------------------------------
p("E. Taxe permanente (perte sur tous les épisodes, sabotés ou non) : le bilan seul la voit en espérance après")
p("   T* = (Z1 * sigma / tau_perm)^2 épisodes, même si l'attaquant ne sabote jamais")
for tp in [0.001, 0.005, 0.01, 0.02, 0.05]:
    t_star = (Z1 * SIGMA / tp) ** 2
    p(f"  tau_perm = {tp:.3f} : T* = {t_star:,.0f} épisodes".replace(",", " "))
p("  Sur T épisodes, le dommage soutenable devient au mieux max(0, Z1*sigma*sqrt(T) - tau_perm*T).")
p("")

# --- F. tailles -------------------------------------------------------------------------------------------------
p("F. Épisodes appariés (même tâche, saboteur obscurci contre non obscurci) pour que la borne haute unilatérale à 95 %")
p("   de tau tombe sous tau_max avec une probabilité de 0,8 quand la vraie perte vue est nulle ; perte vue binaire de")
p("   taux de base c0 = 0,2 par épisode ; rho = corrélation dans la paire ; tau_max = k* d' / (1 - k*)")
Z95, Z80 = float(norm.ppf(0.95)), float(norm.ppf(0.80))
C0 = 0.2
for d in DOMMAGES:
    for k_star in [0.10, 0.25]:
        tau_max = k_star * d / (1 - k_star)
        cells = []
        for rho in [0.0, 0.5]:
            sd = math.sqrt(2 * C0 * (1 - C0) * (1 - rho))
            n = math.ceil(((Z95 + Z80) * sd / tau_max) ** 2)
            cells.append(f"rho = {rho:.1f} : n = {n}")
        p(f"  d' = {d:.2f}, borne visée k_eff <= {k_star:.2f} (tau_max = {tau_max:.4f}) : " + " ; ".join(cells))
p("")
p("Fin. Tous les contrôles écrits avant l'exécution ont tenu (assertions).")

print("\n".join(lignes))
