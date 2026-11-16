"""Jugement d'un monde simulé par toutes les méthodes étudiées, sur les MÊMES tirages et aux MÊMES instants — v1.

Mise au point exploratoire, aucune revendication. Méthodes (dénominateur D_t ; promotion si log q(y_1..t) − D_t ≥ log 20 à
un instant de T ; « structure » = liste des membres ajustés, voir `essai_regret_banc_v1.partitions`) :
- MAX-v9r  : maximum certifié (façon nul v9) sur la structure « v9 réduit » ;
- MAX-La   : maximum certifié sur la structure « nul limité aux coupures de l'archive » (linéaire + coupure d'archive) ;
- A1-EG-η  : artefact, poids appris en ligne par gradient exponentié (argon-p2-01), par cellule, SANS correction (La) ;
- A1-BAYES : artefact, mélange bayésien uniforme sur le polytope de chaque membre, SANS correction (La) ;
- A2-MOITIE: artefact, poids ajustés sur les tirages 1..100, valeur e sur 101..200 (argon-p1-01), (La) ;
- R1-COVER-La / R1-COVER-v9r : mélange uniforme (« portefeuille universel ») + borne de regret ε (corrigé) ;
- R1-BORNE-v9r : borne haute de la puissance de R1-COVER-v9r exact (D = max certifié − écart ≤ vrai maximum ≤ D_R1) ;
- R2-EG-La / R2-EG-v9r : gradient exponentié lissé + borne certifiée de Hedge (corrigé).
"""
import math
import time

import numpy as np

import essai_regret_banc_v1 as bc

ETA_ARTEFACT = (0.05, 0.2)


def parametres_monde(cas, rng):
    """Paramètres du monde tirés AVANT le plan (poids, issue de la loi certaine) : la même loi sert au plan et aux
    instances d'entraînement."""
    return {"w": rng.dirichlet(np.ones(bc.J + bc.K)), "k": int(rng.integers(0, bc.K))}


def monde_et_carte(cas, prm, arch, z, dose=None, nouvelle=None, mediane_z1=None):
    """Loi du monde P (n, K) ; la carte est la loi du monde (copie exacte, ou vraie découverte)."""
    Lf = bc.lois_connues(arch, z)
    L1, L2 = Lf[:, 0], Lf[:, 1]
    D = np.eye(bc.K)
    k = prm["k"]
    if cas == "interieur_lineaire":
        w = prm["w"]
        P = w[0] * L1 + w[1] * L2 + w[2:][None, :]
    elif cas == "sommet_L1":
        P = L1.copy()
    elif cas == "bord_L2_delta":
        P = 0.7 * L2 + 0.3 * D[k][None, :]
    elif cas == "morceaux_archive":
        P = np.where((z[:, 0] > bc.SEUIL_ARCHIVE)[:, None], L1, L2)
    elif cas == "poids_extremes_morceaux":
        haut = 0.95 * L1 + 0.03 * L2 + 0.02 * D[k][None, :]
        bas = 0.03 * L1 + 0.95 * L2 + 0.02 * D[k][None, :]
        P = np.where((z[:, 0] > bc.SEUIL_ARCHIVE)[:, None], haut, bas)
    elif cas == "morceaux_hors_archive":
        P = np.where((z[:, 1] > mediane_z1)[:, None], L2, L1)
    elif cas == "decouverte":
        Nn = bc.probas_softmax(nouvelle, z)
        P = (1 - dose) * (0.5 * L1 + 0.5 * L2) + dose * Nn
    else:
        raise ValueError(cas)
    P = np.maximum(P, bc.PLANCHER)
    return P / P.sum(axis=1, keepdims=True), Lf


def em_cellules_independantes(X, cellule, C, iterations=400):
    """Poids par cellule indépendante sur les composantes de X (n, m) (lecture des fiches : lois connues et aveugles
    estimées séparément dans chaque cellule), maximum de vraisemblance par EM."""
    m = X.shape[1]
    W = np.full((C, m), 1.0 / m)
    for _ in range(iterations):
        p = np.maximum((W[cellule] * X).sum(axis=1), bc.PLANCHER)
        resp = W[cellule] * X / p[:, None]
        Wn = np.zeros((C, m))
        np.add.at(Wn, cellule, resp)
        Wn += 1e-300
        W = Wn / Wn.sum(axis=1, keepdims=True)
    return W


def juger(cas, graine, methodes_v9r=False, dose=None, nb_is=1000):
    rng = np.random.default_rng(graine)
    arch = bc.archive(rng)
    nouvelle = bc.softmax_alea(rng) if cas == "decouverte" else None
    prm = parametres_monde(cas, rng)
    z_ent, g_ent = bc.plan(rng, bc.ENTRAINEMENT)
    z, g = bc.plan(rng)
    med = float(np.quantile(z[:, 1], 0.5))          # seuil du plan (aussi un octile de la structure v9r)
    P, Lf = monde_et_carte(cas, prm, arch, z, dose, nouvelle, med)
    P_ent, _ = monde_et_carte(cas, prm, arch, z_ent, dose, nouvelle, med)
    y_ent = bc.tirer(rng, P_ent)
    q_ent = np.bincount(y_ent, minlength=bc.K) / len(y_ent)
    q_ent = np.maximum(q_ent, bc.PLANCHER)
    q_ent = q_ent / q_ent.sum()
    y = bc.tirer(rng, P)                                    # tirages frais, après le gel (plan, archive, carte)
    n = bc.N
    idx = np.arange(n)
    Aobs = Lf[idx, :, y]                                    # (n, J)
    logq = np.cumsum(np.log(P[idx, y]))
    lq = logq[bc.INSTANTS - 1]
    fixes = bc.valeurs_fixes(Aobs, y, q_ent)
    res = {}
    maxlw = {}

    def lire(nom, D):
        lw = lq - D
        res[nom] = bool((lw >= bc.SEUIL).any())
        maxlw[nom] = float(lw.max())

    duree = {}
    t_0 = time.perf_counter()
    # --- maximums certifiés et paramètres (structures La et v9r) ---
    parts_La = bc.partitions(z, g, "La")
    parts = bc.partitions(z, g, "v9r") if methodes_v9r else parts_La
    cel, nbc, act, cle = bc.lot_partitions(parts)
    cert, att, gap, (s_, r_, m_) = bc.em_certifie(Aobs, y, cel, nbc, act, rendre_parametres=True)
    T = len(bc.INSTANTS)
    noms = [p[0] for p in parts]
    C_de = {p[0]: p[2] for p in parts}
    cert_m = cert.reshape(len(parts), T)
    gap_m = gap.reshape(len(parts), T)
    iLa = [noms.index(p[0]) for p in parts_La]
    lire("MAX-La", np.maximum(fixes, cert_m[iLa].max(axis=0)))
    if methodes_v9r:
        lire("MAX-v9r", np.maximum(fixes, cert_m.max(axis=0)))
        lire("R1-BORNE-v9r", np.maximum(fixes, (cert_m - gap_m).max(axis=0)))
    duree["maximum_certifie"] = time.perf_counter() - t_0
    t_0 = time.perf_counter()
    # --- mélanges uniformes (IS) ---
    lmix = np.full((len(parts), T), -np.inf)
    rng_is = np.random.default_rng([graine, 7])
    choix_parts = range(len(parts)) if methodes_v9r else iLa
    for ip in choix_parts:
        nom, c, C = parts[ip]
        for it, t in enumerate(bc.INSTANTS):
            b = ip * T + it
            prm = (s_[b], r_[b], m_[b][:C])
            cpt = bc.comptes_em(Aobs[:t], y[:t], c[:t], C, prm)
            lmix[ip, it] = bc.log_melange_uniforme(Aobs[:t], y[:t], c[:t], C, rng_is, nb=nb_is, comptes=cpt)
    Rc = np.stack([bc.regret_cover(bc.INSTANTS, bc.dimension_famille(C_de[nm])) for nm in noms])
    lire("A1-BAYES-La", np.maximum(fixes, lmix[iLa].max(axis=0)))
    lire("R1-COVER-La", np.maximum(fixes, (lmix[iLa] + Rc[iLa]).max(axis=0)))
    res["R1-La-sous-le-maximum"] = int(((lmix[iLa] + Rc[iLa]) < cert_m[iLa] - gap_m[iLa] - 1e-9).sum())
    if methodes_v9r:
        lire("R1-COVER-v9r", np.maximum(fixes, (lmix + Rc).max(axis=0)))
    duree["melange_uniforme"] = time.perf_counter() - t_0
    t_0 = time.perf_counter()
    # --- gradient exponentié ---
    m = bc.J + bc.K
    X_tous = np.concatenate([Aobs, np.eye(bc.K)[y]], axis=1)
    for eta in ETA_ARTEFACT:
        D = fixes.copy()
        for ip in iLa:
            nom, c, C = parts[ip]
            tr = bc.eg_en_ligne(Aobs, y, c, C, eta)
            D = np.maximum(D, tr[bc.INSTANTS - 1])
        lire(f"A1-EG-{eta}-La", D)
    for struct, ids in [("La", iLa)] + ([("v9r", list(range(len(parts))))] if methodes_v9r else []):
        D = fixes.copy()
        for ip in ids:
            nom, c, C = parts[ip]
            borne, eta, gamma = bc.meilleurs_eta_gamma(bc.N, m, C)
            tr = bc.eg_en_ligne(Aobs, y, c, C, eta, gamma)
            D = np.maximum(D, tr[bc.INSTANTS - 1] + bc.regret_eg(bc.INSTANTS, m, C, eta, gamma))
        lire(f"R2-EG-{struct}", D)
    duree["gradient_exponentie"] = time.perf_counter() - t_0
    t_0 = time.perf_counter()
    # --- moitié ---
    h = n // 2
    inst2 = bc.INSTANTS[bc.INSTANTS > h]
    lq2 = logq[inst2 - 1] - logq[h - 1]
    D2 = bc.valeurs_fixes(Aobs, y, q_ent, instants=inst2, debut=h)
    for ip in iLa:
        nom, c, C = parts[ip]
        W = em_cellules_independantes(X_tous[:h], c[:h], C)
        p2 = np.maximum((W[c[h:]] * X_tous[h:]).sum(axis=1), bc.PLANCHER)
        D2 = np.maximum(D2, np.cumsum(np.log(p2))[inst2 - 1 - h])
    lw2 = lq2 - D2
    res["A2-MOITIE-La"] = bool((lw2 >= bc.SEUIL).any())
    maxlw["A2-MOITIE-La"] = float(lw2.max())
    duree["moitie"] = time.perf_counter() - t_0
    return res, maxlw, {"ecart_max_certificat": float(gap_m.max()), "ecart_median": float(np.median(gap_m)),
                        "duree_s": duree, "membres_ajustes": len(parts), "lots": len(cle)}
