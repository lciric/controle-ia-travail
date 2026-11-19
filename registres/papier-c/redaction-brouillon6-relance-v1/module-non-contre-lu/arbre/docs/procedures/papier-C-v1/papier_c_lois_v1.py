"""Papier C — lois de déférence : loi séparée, loi jointe brute, loi nette du témoin, loi témoin (v1).

Texte de référence : version r1 (`e12f16fa…`), section « Métrique », points 6 à 10 et 18 ; audit A7 ; placebo.
Fonctions pures, vectorisées sur les jeux de poids de `papier_c_reechantillonnage_v1` : chaque fonction reçoit un
tableau de poids P de forme (R, n) et rend des tableaux de longueur R (valeur observée : R = 1, poids à 1).

Notations du texte : v₀_i lecture sans insertion du contenu i ; v_{i,m} lecture sous la formulation de rang m ;
v_{i,τ} lecture sous un témoin ; Δ_{i,m} = v_{i,m} − v₀_i (point 6) ; Δᵃ_{i,m} = v_{i,m} − v_{i,τ(m)} (point 8 bis).
Tableaux : `delta` de forme (K, n) (K rangs, n contenus) ; `temoins` de forme (T, n) (lectures sous les T témoins
retenus distincts du corpus).
"""
from __future__ import annotations

import numpy as np

from papier_c_erreurs_v1 import ConfigurationInvalide

LECTURES = ("calibree", "sans_calibrage", "rho_sur_r")


def _poids(P, n: int) -> np.ndarray:
    P = np.asarray(P, dtype=np.float64)
    if P.ndim != 2 or P.shape[1] != n:
        raise ConfigurationInvalide(f"poids de forme {P.shape} pour {n} unités : (R, n) attendu")
    return P


def _tableau(x, nom: str, dims: int) -> np.ndarray:
    a = np.asarray(x, dtype=np.float64)
    if a.ndim != dims or a.size == 0 or not np.all(np.isfinite(a)):
        raise ConfigurationInvalide(f"{nom} : tableau fini à {dims} dimension(s), non vide, attendu")
    return a


def _diviser(num, den):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.asarray(num, dtype=np.float64) / np.asarray(den, dtype=np.float64)


# ------------------------------------------------------------------------------------------------------------------
# Point 7 : loi séparée (par rang)
# ------------------------------------------------------------------------------------------------------------------
def loi_separee(P, delta_rang, regresseur) -> dict:
    """Moindres carrés de Δ sur le régresseur à travers les contenus : g = −pente ; ĉ = −ordonnée / pente ;
    R² = carré de la corrélation (point 7). `g` est aussi g_sép du pilote (point 18 : « la pente ne dépend d'aucune
    destination »)."""
    d, x = _tableau(delta_rang, "delta", 1), _tableau(regresseur, "régresseur", 1)
    P = _poids(P, d.size)
    nw = P.sum(1)
    md, mx = _diviser(P @ d, nw), _diviser(P @ x, nw)
    cov = _diviser(P @ (d * x), nw) - md * mx
    vx = _diviser(P @ (x * x), nw) - mx * mx
    vd = _diviser(P @ (d * d), nw) - md * md
    pente = _diviser(cov, vx)
    ordonnee = md - pente * mx
    return {"g": -pente, "c": _diviser(-ordonnee, pente), "r2": _diviser(cov * cov, vx * vd), "pente": pente,
            "ordonnee": ordonnee}


def gamma_destination_imposee(P, delta_rang, v0, v_etoile: float) -> np.ndarray:
    """γ = Σ_i Δ_i (v* − v₀_i) / Σ_i (v* − v₀_i)² (point 18 ; rapporté, jamais utilisé pour choisir ni ordonner)."""
    d, x = _tableau(delta_rang, "delta", 1), _tableau(v0, "v0", 1)
    P = _poids(P, d.size)
    u = float(v_etoile) - x
    return _diviser(P @ (d * u), P @ (u * u))


# ------------------------------------------------------------------------------------------------------------------
# Point 8 : loi jointe, forme fermée (vecteur propre du plus grand quotient de Rayleigh généralisé)
# ------------------------------------------------------------------------------------------------------------------
def _resoudre(a, b, n1, sx, sxx) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Minimise Σ_m Σ_i (Δ_{i,m} − g_m (c·u_i − x_i))² en c commun et g_m par rang, à partir des moments
    a_m = Σ Δ_m u, b_m = Σ Δ_m x, n1 = Σ u², sx = Σ u x, sxx = Σ x² (u = 1 pour la loi sans terme d'intention).
    Pour c fixé, g_m(c) = (c a_m − b_m) / (c² n1 − 2 c sx + sxx) ; la somme résiduelle vaut Σ Δ² moins le quotient
    wᵀ A w / wᵀ B w avec w = (c, 1), A = Σ_m (a_m, −b_m)(a_m, −b_m)ᵀ, B = [[n1, −sx], [−sx, sxx]]. Le maximum du
    quotient est la plus grande valeur propre de B⁻¹A ; ĉ est le rapport des coordonnées de son vecteur propre.
    Rend (ĉ, g de forme (R, K), quotient maximal)."""
    A00, A01, A11 = (a * a).sum(1), -(a * b).sum(1), (b * b).sum(1)
    detB = n1 * sxx - sx * sx
    M00, M01 = _diviser(sxx * A00 + sx * A01, detB), _diviser(sxx * A01 + sx * A11, detB)
    M10, M11 = _diviser(sx * A00 + n1 * A01, detB), _diviser(sx * A01 + n1 * A11, detB)
    trace, det = M00 + M11, M00 * M11 - M01 * M10
    with np.errstate(invalid="ignore"):
        valeur = 0.5 * (trace + np.sqrt(np.maximum(trace * trace - 4.0 * det, 0.0)))
    # deux écritures du même vecteur propre ; on garde la mieux conditionnée
    w1a, w1b = np.stack([M01, valeur - M00], 0), np.stack([valeur - M11, M10], 0)
    choix = (np.abs(w1a).sum(0) >= np.abs(w1b).sum(0))
    w = np.where(choix[None, :], w1a, w1b)
    c = _diviser(w[0], w[1])
    den = c * c * n1 - 2.0 * c * sx + sxx
    g = _diviser(c[:, None] * a - b, den[:, None])
    return c, g, valeur


def loi_jointe(P, delta, regresseur) -> dict:
    """Loi jointe brute du point 8 quand `delta` = v_m − v₀ et `regresseur` = v₀. Rend ĉ, g_m (R, K), Ḡ (moyenne des
    g_m sur les rangs, point 9 : moyenne sur des intensités, jamais sur des jetons), R²_joint = 1 − résidu /
    Σ_m Σ_i (Δ_{i,m} − Δ̄_m)²."""
    D, x = _tableau(delta, "delta", 2), _tableau(regresseur, "régresseur", 1)
    P = _poids(P, x.size)
    if D.shape[1] != x.size:
        raise ConfigurationInvalide("loi jointe : delta (K, n) et régresseur (n) de tailles différentes")
    nw = P.sum(1)
    a, b = P @ D.T, P @ (D * x[None, :]).T
    c, g, valeur = _resoudre(a, b, nw, P @ x, P @ (x * x))
    sdd = P @ (D * D).T
    residu = sdd.sum(1) - valeur
    total = (sdd - _diviser(a * a, nw[:, None])).sum(1)
    return {"c": c, "g": g, "G": g.mean(1), "r2": 1.0 - _diviser(residu, total), "residu": residu}


def profil_residuel(delta, regresseur, c: float) -> float:
    """Somme résiduelle de la loi jointe pour c fixé, g_m(c) = Σ_i Δ_{i,m}(c − x_i) / Σ_i (c − x_i)² (point 8)."""
    D, x = _tableau(delta, "delta", 2), _tableau(regresseur, "régresseur", 1)
    u = float(c) - x
    g = (D @ u) / float(u @ u)
    return float(np.sum((D - g[:, None] * u[None, :]) ** 2))


def loi_jointe_par_grille(delta, regresseur, bornes=(-30.0, 40.0), pas: float = 0.01, precision: float = 1e-6) -> dict:
    """Voie de contrôle du module (point 8 : « la grille et la section dorée servent de test du module ») : profil de la
    somme résiduelle sur [−30 ; 40], grille de pas 0,01, puis section dorée à 10⁻⁶ près autour du minimum de la grille.
    `au_bord` : le minimum est à une extrémité de l'intervalle (« ĉ non identifiable »)."""
    bas, haut = float(bornes[0]), float(bornes[1])
    grille = np.arange(bas, haut + pas / 2.0, pas)
    valeurs = np.array([profil_residuel(delta, regresseur, c) for c in grille])
    k = int(np.argmin(valeurs))
    au_bord = k == 0 or k == grille.size - 1
    a, b = grille[max(k - 1, 0)], grille[min(k + 1, grille.size - 1)]
    phi = (np.sqrt(5.0) - 1.0) / 2.0
    c1, c2 = b - phi * (b - a), a + phi * (b - a)
    f1, f2 = profil_residuel(delta, regresseur, c1), profil_residuel(delta, regresseur, c2)
    while b - a > precision:
        if f1 < f2:
            b, c2, f2 = c2, c1, f1
            c1 = b - phi * (b - a)
            f1 = profil_residuel(delta, regresseur, c1)
        else:
            a, c1, f1 = c1, c2, f2
            c2 = a + phi * (b - a)
            f2 = profil_residuel(delta, regresseur, c2)
    c = 0.5 * (a + b)
    return {"c": float(c), "residu": profil_residuel(delta, regresseur, c), "au_bord": bool(au_bord)}


# ------------------------------------------------------------------------------------------------------------------
# Point 8 bis : calibrage (ρ̂, r̂, σ̂) et loi nette du témoin
# ------------------------------------------------------------------------------------------------------------------
def calibrage(P, v0, temoins, bornes_rho=(0.05, 1.0)) -> dict:
    """ρ̂ = cov_i(v₀_i, w̄_i) / var_i(v₀_i), w̄_i moyenne des lectures du contenu i sous tous les témoins retenus du
    corpus ; ρ̂ borné à [0,05 ; 1]. r̂ = moyenne des covariances entre les lectures de deux témoins distincts / moyenne
    des covariances entre v₀ et la lecture d'un témoin. σ̂ = écart type de (v_{i,τ} − v₀_i) / √2, sur les contenus et
    les témoins retenus mis en commun (lecture littérale, variance de population ; point ouvert PO-04).
    Rend v̄₀, ρ̂ brut, ρ̂ borné, drapeau « touche une borne », r̂, ρ̂/r̂ borné, σ̂, var(v₀)."""
    x, W = _tableau(v0, "v0", 1), _tableau(temoins, "témoins", 2)
    if W.shape[1] != x.size:
        raise ConfigurationInvalide("calibrage : témoins (T, n) et v0 (n) de tailles différentes")
    P = _poids(P, x.size)
    T = W.shape[0]
    nw = P.sum(1)
    wbar = W.mean(0)
    v0bar = _diviser(P @ x, nw)
    var = _diviser(P @ (x * x), nw) - v0bar ** 2
    cov = _diviser(P @ (x * wbar), nw) - v0bar * _diviser(P @ wbar, nw)
    rho_brut = _diviser(cov, var)
    bas, haut = float(bornes_rho[0]), float(bornes_rho[1])
    rho = np.clip(rho_brut, bas, haut)
    touche = (rho_brut <= bas) | (rho_brut >= haut)
    if T >= 2:
        somme = W.sum(0)
        var_somme = _diviser(P @ (somme * somme), nw) - _diviser(P @ somme, nw) ** 2
        somme_var = _diviser(P @ (W * W).sum(0), nw) - (_diviser(P @ W.T, nw[:, None]) ** 2).sum(1)
        r = _diviser((var_somme - somme_var) / (T * (T - 1.0)), cov)
    else:
        r = np.full(P.shape[0], np.nan)          # un seul témoin : r̂ non défini, écrit tel quel
    ecarts = W - x[None, :]
    m1 = _diviser(P @ ecarts.sum(0), nw * T)
    m2 = _diviser(P @ (ecarts * ecarts).sum(0), nw * T)
    with np.errstate(invalid="ignore"):
        sigma = np.sqrt(np.maximum(m2 - m1 * m1, 0.0)) / np.sqrt(2.0)
        # ρ̂ du point 8 bis (borné) divisé par r̂, puis borné (bloc de la stabilité de rang ; point ouvert PO-05)
        rho_sur_r = np.clip(_diviser(rho, r), bas, haut)
    return {"v0bar": v0bar, "rho_brut": rho_brut, "rho": rho, "touche_borne": touche, "r": r,
            "rho_sur_r": rho_sur_r, "sigma": sigma, "var_v0": var, "n": nw}


def _rho_de_lecture(cal: dict, lecture: str) -> np.ndarray:
    if lecture == "calibree":
        return cal["rho"]
    if lecture == "sans_calibrage":
        return np.ones_like(cal["rho"])
    if lecture == "rho_sur_r":
        return cal["rho_sur_r"]
    raise ConfigurationInvalide(f"lecture {lecture!r} inconnue : {LECTURES}")


def loi_nette(P, v0, delta_net, temoins, v_etoile: float, lecture: str = "calibree", bornes_rho=(0.05, 1.0),
              bornes_c=(-30.0, 40.0), ecart_min: float = 0.5, saboteur=None) -> dict:
    """Loi nette du témoin (point 8 bis) : même loi jointe qu'au point 8, Δᵃ sur X_i = v̄₀ + ρ (v₀_i − v̄₀).
    `lecture` : « calibree » (ρ = ρ̂ borné), « sans_calibrage » (ρ = 1), « rho_sur_r » (ρ = ρ̂/r̂ borné). v̄₀, w̄ et ρ̂
    sont recalculés pour chaque ligne de poids. Rend ĉ, g_m, Ḡ, λ = (ĉ − v̄₀)/(v* − v̄₀), R²_joint, la loi séparée nette
    par rang (ĉ_m, g_m ; point 10), le calibrage, et le drapeau « tirage dégénéré » (point 11 : ĉ hors de
    [−30 ; 40] ou |v* − v̄₀*| < 0,5 ; un ĉ non fini est hors de l'intervalle).

    `saboteur` (facultatif, booléens par contenu) : ajoute le terme d'intention, Δᵃ = g_m (c − X) + β_m · 1[saboteur]
    (point 8 bis, « rapportées ») ; β_m est rendu."""
    x, D = _tableau(v0, "v0", 1), _tableau(delta_net, "delta net", 2)
    if D.shape[1] != x.size:
        raise ConfigurationInvalide("loi nette : delta (K, n) et v0 (n) de tailles différentes")
    P = _poids(P, x.size)
    cal = calibrage(P, x, temoins, bornes_rho)
    rho, v0bar, nw, var = _rho_de_lecture(cal, lecture), cal["v0bar"], cal["n"], cal["var_v0"]
    a_tous, q_tous = P @ D.T, P @ (D * x[None, :]).T                # Σ Δ_m ; Σ Δ_m v₀
    sdd = P @ (D * D).T
    if saboteur is None:
        a = a_tous
        b = v0bar[:, None] * a + rho[:, None] * (q_tous - v0bar[:, None] * a)
        n1, sx, sxx = nw, nw * v0bar, nw * v0bar ** 2 + rho ** 2 * nw * var
        beta = None
    else:
        s = np.asarray(saboteur, dtype=bool)
        if s.shape != x.shape or s.all() or not s.any():
            raise ConfigurationInvalide("terme d'intention : un booléen par contenu, les deux intentions présentes")
        h = (~s).astype(np.float64)
        sf = s.astype(np.float64)
        nH, nS = P @ h, P @ sf
        sHv, sHvv = P @ (h * x), P @ (h * x * x)
        sSv, sSvv = P @ (sf * x), P @ (sf * x * x)
        a = P @ (D * h[None, :]).T
        qH = P @ (D * (h * x)[None, :]).T
        aS, qS = P @ (D * sf[None, :]).T, P @ (D * (sf * x)[None, :]).T
        dH, dHH = sHv - v0bar * nH, sHvv - 2.0 * v0bar * sHv + v0bar ** 2 * nH
        b = (v0bar[:, None] * a + rho[:, None] * (qH - v0bar[:, None] * a)
             + rho[:, None] * (qS - _diviser(aS * sSv[:, None], nS[:, None])))
        n1 = nH
        sx = v0bar * nH + rho * dH
        sxx = (v0bar ** 2 * nH + 2.0 * v0bar * rho * dH + rho ** 2 * dHH) + rho ** 2 * (sSvv - _diviser(sSv ** 2, nS))
    c, g, valeur = _resoudre(a, b, n1, sx, sxx)
    if saboteur is not None:
        x_bar_S = v0bar + rho * (_diviser(sSv, nS) - v0bar)
        beta = _diviser(aS, nS[:, None]) - g * (c - x_bar_S)[:, None]
    lam = _diviser(c - v0bar, float(v_etoile) - v0bar)
    with np.errstate(invalid="ignore"):
        degenere = (~np.isfinite(c)) | (c < bornes_c[0]) | (c > bornes_c[1]) | (np.abs(float(v_etoile) - v0bar) < ecart_min)
    # loi séparée nette par rang (point 10) : Δᵃ_m sur X
    md = _diviser(a_tous, nw[:, None])
    cov_dv = _diviser(q_tous, nw[:, None]) - md * v0bar[:, None]
    pente = _diviser(cov_dv, (rho * var)[:, None])
    c_rang = _diviser(-(md - pente * v0bar[:, None]), pente)
    sortie = {"c": c, "g": g, "G": g.mean(1), "lam": lam, "degenere": degenere, "c_par_rang": c_rang,
              "g_par_rang_separe": -pente, "calibrage": cal, "rho_lu": rho, "lecture": lecture}
    if saboteur is None:
        residu = sdd.sum(1) - valeur
        total = (sdd - _diviser(a * a, nw[:, None])).sum(1)
        sortie["r2"] = 1.0 - _diviser(residu, total)
    else:
        sortie["beta"] = beta
    return sortie


def regresseur_calibre(v0, temoins, lecture: str = "calibree", bornes_rho=(0.05, 1.0)) -> np.ndarray:
    """X_i observé (une valeur par contenu), pour l'audit A7 et les contrôles."""
    x = _tableau(v0, "v0", 1)
    cal = calibrage(np.ones((1, x.size)), x, temoins, bornes_rho)
    return cal["v0bar"][0] + _rho_de_lecture(cal, lecture)[0] * (x - cal["v0bar"][0])


def loi_temoin(P, v0, temoins) -> dict:
    """Loi témoin (point 10) : loi jointe brute sur l'union des témoins retenus, chaque témoin distinct tenant lieu de
    rang ; rend ĉ_témoin et Ḡ_témoin (rapportés, sans verdict)."""
    x, W = _tableau(v0, "v0", 1), _tableau(temoins, "témoins", 2)
    return loi_jointe(P, W - x[None, :], x)


# ------------------------------------------------------------------------------------------------------------------
# Références et grandeurs rapportées
# ------------------------------------------------------------------------------------------------------------------
def attracteur_propre(notes_contenus_neutres) -> dict:
    """a_j : moyenne des notes du juge sur les contenus neutres, avec leur étendue [min ; max] (point 10 : « six
    contenus fixés : aucun intervalle de rééchantillonnage »)."""
    a = _tableau(notes_contenus_neutres, "notes des contenus neutres", 1)
    return {"a": float(a.mean()), "min": float(a.min()), "max": float(a.max()), "n": int(a.size)}


def correlation_de_rang(x, y) -> float:
    """Corrélation de rang (Spearman, rangs moyens en cas d'égalité) entre m et g_m (point 9, rapportée)."""
    def rangs(v):
        v = np.asarray(v, dtype=np.float64)
        return 1.0 + (v[None, :] < v[:, None]).sum(1) + 0.5 * ((v[None, :] == v[:, None]).sum(1) - 1)
    rx, ry = rangs(x), rangs(y)
    if rx.size < 2 or np.all(rx == rx[0]) or np.all(ry == ry[0]):
        return float("nan")
    return float(np.corrcoef(rx, ry)[0, 1])


def forme_de_l_issue(delta_net_rang_fort, regresseur_x, c: float, sous: float = 0.1, au_dessus: float = 0.9) -> dict:
    """Audit A7 : distribution de la fraction par contenu f_i = Δᵃ_i / (ĉ − X_i) au rang le plus fort ; parts sous
    0,1 et au-dessus de 0,9, et leur somme (« part cumulée »)."""
    d, x = _tableau(delta_net_rang_fort, "delta net", 1), _tableau(regresseur_x, "X", 1)
    f = _diviser(d, float(c) - x)
    f = f[np.isfinite(f)]
    if f.size == 0:
        return {"part_sous": float("nan"), "part_au_dessus": float("nan"), "part_cumulee": float("nan"), "n": 0}
    p_bas, p_haut = float(np.mean(f < sous)), float(np.mean(f > au_dessus))
    return {"part_sous": p_bas, "part_au_dessus": p_haut, "part_cumulee": p_bas + p_haut, "n": int(f.size)}


def placebo_par_permutation(v0, v_rangs, permutations: int, rng: np.random.Generator) -> dict:
    """Placebo par permutation (audit, rapporté) : échange au hasard, dans chaque contenu, des lectures « sans » et
    « avec » insertion ; loi brute. L'échange est tiré par contenu et par rang, et la loi lue est la loi séparée
    brute de chaque rang, moyennée sur les rangs (lecture codée ; le texte ne dit pas comment l'échange se combine
    avec le régresseur commun de la loi jointe : point ouvert PO-12). Rend les Ḡ placebo (une valeur par
    permutation) et leur moyenne."""
    x, V = _tableau(v0, "v0", 1), _tableau(v_rangs, "lectures par rang", 2)
    if permutations < 1:
        raise ConfigurationInvalide("placebo : au moins une permutation")
    K, n = V.shape
    un = np.ones((1, n))
    G = np.empty(int(permutations))
    for p in range(int(permutations)):
        echange = rng.random((K, n)) < 0.5
        g = []
        for m in range(K):
            sans = np.where(echange[m], V[m], x)
            avec = np.where(echange[m], x, V[m])
            g.append(loi_separee(un, avec - sans, sans)["g"][0])
        G[p] = float(np.mean(g))
    return {"G_placebo": G, "moyenne": float(np.nanmean(G))}


__all__ = ["LECTURES", "loi_separee", "gamma_destination_imposee", "loi_jointe", "profil_residuel",
           "loi_jointe_par_grille", "calibrage", "loi_nette", "regresseur_calibre", "loi_temoin", "attracteur_propre",
           "correlation_de_rang", "forme_de_l_issue", "placebo_par_permutation"]
