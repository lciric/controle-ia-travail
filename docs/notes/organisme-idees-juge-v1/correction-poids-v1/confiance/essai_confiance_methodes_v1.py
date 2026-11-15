"""Méthodes jugées sur un monde du banc (mêmes tirages, mêmes instants pour toutes) — v1.

Mise au point exploratoire, aucune revendication. Voir `essai_confiance_banc_v1.py` pour le banc et ses simplifications.

Méthodes (noms des sorties) :
- références (maximum certifié sur les tirages frais eux-mêmes, comme le juge) : `v9_banc` (toutes les partitions),
  `limite` (aucune + coupures de l'archive), `v8_banc` (aucune) ;
- artefacts (façons non valides des fiches, appliquées à la partition du monde lui-même, cas le plus favorable aux fiches) :
  `F1_en_ligne` (poids par morceau appris en ligne par descente exponentielle, pas 0,05, argon-p2-01),
  `F2_moitie` (poids ajustés au maximum de vraisemblance sur la première moitié des tirages frais, valeur e sur la seconde,
  argon-p1-01) ;
- ensemble de confiance (Berger et Boos), chacune à deux parts beta du niveau, pari au niveau alpha - beta :
  `BB_A_memes_tirages` : ensemble construit sur les tirages frais évalués eux-mêmes (suite de confiance séquentielle) ;
  `BB_T_seq` : ensemble construit sur les tirages d'entraînement, par le prédicteur séquentiel (ensemble « préquentiel ») ;
  `BB_T_coupe` : ensemble construit sur les tirages d'entraînement, coupés en deux (ensemble universel : ajustement sur la
  première moitié, test sur la seconde) ;
  `BB_S_moitie` : ensemble construit sur l'entraînement (ajustement) et la première moitié des tirages frais (test) ; pari
  sur la seconde moitié, lu aux instants 125 à 200 ;
  `BB_Q_blocs` : version séquentielle prévisible : à chaque bloc de 25 tirages frais, maximum sur l'ensemble construit sur
  l'entraînement et les blocs précédents (suite de confiance valide à tout instant) ; dénominateur = somme des maxima par
  bloc.
"""

import math

import numpy as np

import essai_confiance_banc_v1 as bc

INSTANTS_B = tuple(t for t in bc.INSTANTS if t > bc.N // 2)  # 125, 150, 175, 200


def _seuils_pari():
    return {b: math.log(1.0 / (bc.ALPHA - b)) for b in bc.BETAS}


def preparer(rng_donnees, arch, probas_monde, cartes, n_tr_max):
    """Tire le plan frais, les issues fraîches, puis n_tr_max instances d'entraînement et leurs issues (dans cet ordre :
    les tirages frais ne dépendent pas de n_tr). `cartes` : nom -> loi ; rend log q par carte (mêmes tirages)."""
    zf, gf = bc.tirer_plan(rng_donnees, bc.N)
    Pf = probas_monde(zf, gf)
    yf = bc.tirer_issues(rng_donnees, Pf)
    zt, gt = bc.tirer_plan(rng_donnees, n_tr_max)
    yt = bc.tirer_issues(rng_donnees, probas_monde(zt, gt))
    parts = bc.partitions(arch)
    Lf, Lt = bc.lois_connues(arch, zf), bc.lois_connues(arch, zt)
    logq = {nom: np.log(np.maximum(c(zf, gf)[np.arange(bc.N), yf], bc.PLANCHER)) for nom, c in cartes.items()}
    return {"parts": parts, "Af": bc.lignes(Lf, yf), "yf": yf, "Mf": bc.masques(parts, zf, gf),
            "At": bc.lignes(Lt, yt), "yt": yt, "Mt": bc.masques(parts, zt, gt), "logq": logq}


def _logp_membre(A, y, M, theta):
    i, rho, rt, b = theta
    m = M[i]
    p = (1 - rho) * np.where(m, A @ b[1], A @ b[0]) + rho * rt[y]
    return np.log(np.maximum(p, bc.PLANCHER))


def _f1_en_ligne(d, i_part, eta=0.05):
    """Artefact 1 : poids appris en ligne (descente exponentielle), par morceau, sur les J lois connues et les K lois
    certaines, partition du monde (oracle). Rend log p_w(y_s) (prévisible), à soustraire de log q."""
    A, y, m = d["Af"], d["yf"], d["Mf"][i_part]
    J = A.shape[1]
    w = np.full((2, J + bc.K), 1.0 / (J + bc.K))
    lp = np.empty(bc.N)
    for t in range(bc.N):
        c = int(m[t])
        comp = np.concatenate([A[t], (np.arange(bc.K) == y[t]).astype(float)])
        p = max(bc.PLANCHER, float(w[c] @ comp))
        lp[t] = math.log(p)
        w[c] = w[c] * np.exp(np.minimum(eta * comp / p, 50.0))
        w[c] /= w[c].sum()
    return lp


def _f2_moitie(d, i_part):
    """Artefact 2 : poids ajustés (maximum de vraisemblance, famille du monde) sur la première moitié des tirages frais ;
    rend log p_ajuste(y_s) sur la seconde moitié."""
    h = bc.N // 2
    A, y, M = d["Af"], d["yf"], d["Mf"][i_part:i_part + 1]
    _, _, (rho, rt, b) = bc.em_certifie(A[:h], y[:h], np.ones((1, h)), M[:, :h], 150)
    rho, rt, b = float(rho[0, 0]), rt[0, 0], b[0, 0]
    m = M[0, h:]
    p = (1 - rho) * np.where(m, A[h:] @ b[1], A[h:] @ b[0]) + rho * rt[y[h:]]
    return np.log(np.maximum(p, bc.PLANCHER))


def juger(d, n_tr, i_part=None, artefacts=False, theta_star=None):
    """Juge un monde préparé, pour chaque carte de d["logq"] (les dénominateurs ne dépendent pas de la carte).

    Rend {carte: {méthode: {log_w_max, promue}}} et, si theta_star (membre du monde) est donné, la couverture de chaque
    ensemble de confiance (theta_star dans C, à tous les blocs pour BB_Q)."""
    parts = d["parts"]
    g_lim = np.array([p["limite"] for p in parts])
    seuils = _seuils_pari()
    lb = {b: math.log(1.0 / b) for b in bc.BETAS}
    betas = list(bc.BETAS)
    At, yt, Mt = d["At"][:n_tr], d["yt"][:n_tr], d["Mt"][:, :n_tr]
    Af, yf, Mf = d["Af"], d["yf"], d["Mf"]
    D = {}          # dénominateurs : méthode -> {instant: valeur} (log, certifié)
    couv = {}

    # prédicteur séquentiel sur la suite « entraînement puis tirages frais » (BB_T_seq et BB_Q_blocs) ; part fraîche à
    # blocs de 25 (prévisible), part d'entraînement à blocs de 25 (n_tr <= 250) ou de n_tr / 10
    Aseq, yseq, Mseq = np.vstack([At, Af]), np.concatenate([yt, yf]), np.hstack([Mt, Mf])
    lm = np.empty(n_tr + bc.N)
    bloc_tr = bc.BLOC_PREQ if n_tr <= 250 else n_tr // 10
    bornes = list(range(0, n_tr, bloc_tr)) + list(range(n_tr, n_tr + bc.N, bc.BLOC_PREQ)) + [n_tr + bc.N]
    defaut = (0, (0.1, np.full(bc.K, 1.0 / bc.K), np.full((2, Af.shape[1]), 1.0 / Af.shape[1])))
    for s0, s1 in zip(bornes[:-1], bornes[1:]):
        i, par = defaut if s0 == 0 else bc.ajuster_meilleur(Aseq[:s0], yseq[:s0], Mseq[:, :s0], 40)
        lm[s0:s1] = np.log(bc.proba_lissee(Aseq[s0:s1], yseq[s0:s1], Mseq[:, s0:s1], i, par))
    cm = np.concatenate([[0.0], np.cumsum(lm)])
    lstar = None if theta_star is None else np.concatenate([[0.0], np.cumsum(_logp_membre(Aseq, yseq, Mseq, theta_star))])

    # --- BB_T_seq (et références v9, limité, v8 par la tranche lambda = 0) ---
    kap = [cm[n_tr] - lb[b] for b in betas]
    if lstar is not None:
        for b, k in zip(betas, kap):
            couv[f"BB_T_seq|beta={b}"] = bool(lstar[n_tr] >= k)
    init, Vc = None, None
    for t in bc.INSTANTS:
        B, U0, init, Vc = bc.borne_sur_ensemble(Af[:t], yf[:t], Mf[:, :t], At, yt, Mt, kap, init=init, Vc=Vc)
        D.setdefault("v9_banc", {})[t] = U0.max()
        D.setdefault("limite", {})[t] = U0[g_lim].max()
        D.setdefault("v8_banc", {})[t] = U0[0]
        for k, b in enumerate(betas):
            D.setdefault(f"BB_T_seq|beta={b}", {})[t] = B[k].max()

    # --- BB_T_coupe : ensemble universel sur l'entraînement coupé en deux ---
    h = n_tr // 2
    i1, par1 = bc.ajuster_meilleur(At[:h], yt[:h], Mt[:, :h])
    l2 = float(np.log(bc.proba_lissee(At[h:], yt[h:], Mt[:, h:], i1, par1)).sum())
    kap = [l2 - lb[b] for b in betas]
    if lstar is not None:
        for b, k in zip(betas, kap):
            couv[f"BB_T_coupe|beta={b}"] = bool(lstar[n_tr] - lstar[h] >= k)
    init, Vc = None, None
    for t in bc.INSTANTS:
        B, _, init, Vc = bc.borne_sur_ensemble(Af[:t], yf[:t], Mf[:, :t], At[h:], yt[h:], Mt[:, h:], kap, init=init, Vc=Vc)
        for k, b in enumerate(betas):
            D.setdefault(f"BB_T_coupe|beta={b}", {})[t] = B[k].max()

    # --- BB_S_moitie : ajustement sur l'entraînement, test sur la première moitié fraîche, pari sur la seconde ---
    hf = bc.N // 2
    i1, par1 = bc.ajuster_meilleur(At, yt, Mt)
    l2 = float(np.log(bc.proba_lissee(Af[:hf], yf[:hf], Mf[:, :hf], i1, par1)).sum())
    kap = [l2 - lb[b] for b in betas]
    if lstar is not None:
        for b, k in zip(betas, kap):
            couv[f"BB_S_moitie|beta={b}"] = bool(lstar[n_tr + hf] - lstar[n_tr] >= k)
    init, Vc = None, None
    for t in INSTANTS_B:
        B, _, init, Vc = bc.borne_sur_ensemble(Af[hf:t], yf[hf:t], Mf[:, hf:t], Af[:hf], yf[:hf], Mf[:, :hf], kap,
                                               init=init, Vc=Vc)
        for k, b in enumerate(betas):
            D.setdefault(f"BB_S_moitie|beta={b}", {})[t] = B[k].max()

    # --- BB_Q_blocs : suite de confiance séquentielle (prédicteur séquentiel, Ville), maximum par bloc de 25 ---
    acc = {b: 0.0 for b in betas}
    cover = {b: True for b in betas}
    for t in bc.INSTANTS:
        s0 = t - bc.BLOC_PREQ
        nc = n_tr + s0
        kap = [cm[nc] - lb[b] for b in betas]
        B, _, _, _ = bc.borne_sur_ensemble(Af[s0:t], yf[s0:t], Mf[:, s0:t], Aseq[:nc], yseq[:nc], Mseq[:, :nc], kap)
        for k, b in enumerate(betas):
            acc[b] += B[k].max()
            D.setdefault(f"BB_Q_blocs|beta={b}", {})[t] = acc[b]   # dénominateur cumulé sur les blocs 1..t/25
            if lstar is not None:
                cover[b] = cover[b] and bool(lstar[nc] >= kap[k])
    if lstar is not None:
        for b in betas:
            couv[f"BB_Q_blocs|beta={b}"] = cover[b]

    # --- BB_A_memes_tirages : ensemble {theta : l_t(theta) >= log m_t - log(1/beta)} sur les tirages évalués eux-mêmes.
    # Lemme : non vide, il contient le maximum (donc sup sur C = sup sur le nul) ; vide si le majorant du v9 est sous le seuil.
    lmf = np.empty(bc.N)
    for s0 in range(0, bc.N, bc.BLOC_PREQ):
        i, par = defaut if s0 == 0 else bc.ajuster_meilleur(Af[:s0], yf[:s0], Mf[:, :s0], 40)
        lmf[s0:s0 + bc.BLOC_PREQ] = np.log(bc.proba_lissee(Af[s0:s0 + bc.BLOC_PREQ], yf[s0:s0 + bc.BLOC_PREQ],
                                                           Mf[:, s0:s0 + bc.BLOC_PREQ], i, par))
    cmf = np.concatenate([[0.0], np.cumsum(lmf)])
    for b in betas:
        D[f"BB_A_memes_tirages|beta={b}"] = {t: (-np.inf if D["v9_banc"][t] < cmf[t] - lb[b] else D["v9_banc"][t])
                                             for t in bc.INSTANTS}

    lp1 = _f1_en_ligne(d, i_part) if (artefacts and i_part is not None) else None
    lp2 = _f2_moitie(d, i_part) if (artefacts and i_part is not None) else None

    out = {}
    for carte, logq in d["logq"].items():
        cq = np.concatenate([[0.0], np.cumsum(logq)])
        r = {}
        for meth, dico in D.items():
            if meth.startswith("BB_S"):
                v = max(cq[t] - cq[hf] - dico[t] for t in dico)
            else:
                v = max(cq[t] - dico[t] for t in dico)
            b = float(meth.split("beta=")[1]) if "beta=" in meth else None
            s = seuils[b] if b is not None else bc.SEUIL
            r[meth] = {"log_w_max": float(v), "promue": bool(v >= s)}
        if lp1 is not None:
            lw = np.cumsum(logq - lp1)
            v = max(lw[t - 1] for t in bc.INSTANTS)
            r["F1_en_ligne"] = {"log_w_max": float(v), "promue": bool(v >= bc.SEUIL)}
            lw = np.cumsum(logq[hf:] - lp2)
            v = max(lw[t - hf - 1] for t in INSTANTS_B)
            r["F2_moitie"] = {"log_w_max": float(v), "promue": bool(v >= bc.SEUIL)}
        out[carte] = r
    return out, couv
