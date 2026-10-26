"""Champs, candidats, structure de cooccurrence, tirage des paires, scores et issues — rétrodiction Swanson v1.

Tout ce qui sert aux scores ne reçoit que la matrice des documents d'avant (X_avant) ; les issues ne lisent que la matrice
des documents d'après. Sections 4 à 7 du préenregistrement.
"""
import math
import multiprocessing as mp
from collections import Counter

import numpy as np
from scipy import sparse

from termes_v1 import AUTRE

PARAMS = dict(df_min=50, df_max_frac=0.05, cand_df_min=50, cand_df_max=3000, part_min=0.6, n_paires=1_000_000,
              seuil_issue=3, frac_top=0.01, seuil_domine=0.5)
N_CHAMPS = 6


def lots_par_cout(cout, budget):
    """Bornes [i0, i1) consécutives, somme des coûts d'un lot ≤ budget (au moins un élément par lot)."""
    cout = np.asarray(cout, dtype=np.float64)
    n = cout.size
    cumul = np.concatenate([[0.0], np.cumsum(cout)])
    bornes, i0 = [], 0
    while i0 < n:
        i1 = int(np.searchsorted(cumul, cumul[i0] + budget, side="right")) - 1
        i1 = min(max(i1, i0 + 1), n)
        bornes.append((i0, i1))
        i0 = i1
    return bornes


def transposee(X):
    XT = X.T.tocsr()
    XT.sort_indices()
    return XT


def structure_avant(X_avant, groupes_avant, params, budget_cout=40_000_000):
    """Fréquences, champs, candidats, r, degrés, idf, top 1 %, effectifs de strates — sur les seuls documents d'avant."""
    N, V = X_avant.shape
    XT = transposee(X_avant)
    df = np.diff(XT.indptr).astype(np.int64)
    if df.min() < 1:
        raise RuntimeError("terme de vocabulaire absent des documents d'avant")
    G = sparse.csr_matrix((np.ones(N, np.float32), groupes_avant.astype(np.int32), np.arange(N + 1)), shape=(N, 7))
    par_groupe = np.rint((XT @ G).toarray()).astype(np.int64)
    if not np.array_equal(par_groupe.sum(axis=1), df):
        raise RuntimeError("comptes par groupe incohérents")
    champ = np.argmax(par_groupe, axis=1)
    part = par_groupe[np.arange(V), champ] / df
    specifique = (part >= params["part_min"]) & (champ != AUTRE)
    candidat = specifique & (df >= params["cand_df_min"]) & (df <= params["cand_df_max"])
    longueur = np.diff(X_avant.indptr).astype(np.float64)
    r = XT @ (longueur - 1.0)
    cout = XT @ longueur
    idf = np.log(N / df)
    deg = np.empty(V, np.int64)
    code = np.where(candidat, champ, -1).astype(np.int8)
    cooc = np.zeros(N_CHAMPS * N_CHAMPS, np.int64)
    for t0, t1 in lots_par_cout(cout, budget_cout):
        Gb = XT[t0:t1] @ X_avant
        nnz = np.diff(Gb.indptr)
        numero = np.repeat(np.arange(t1 - t0, dtype=np.int32), nnz)
        sur_diagonale = Gb.indices == (numero + t0)
        if not (np.array_equal(np.bincount(numero[sur_diagonale], minlength=t1 - t0), np.ones(t1 - t0, np.int64))
                and np.array_equal(np.rint(Gb.data[sur_diagonale]).astype(np.int64), df[t0:t1])):
            raise RuntimeError("diagonale de cooccurrence incohérente")
        del numero, sur_diagonale
        deg[t0:t1] = nnz - 1
        rc = code[t0:t1]
        if (rc >= 0).any():
            ligne = np.repeat(rc, nnz)
            col = code[Gb.indices]
            m = (ligne >= 0) & (col >= 0) & (ligne != col)
            cooc += np.bincount(ligne[m].astype(np.int64) * N_CHAMPS + col[m], minlength=N_CHAMPS * N_CHAMPS)
        del Gb
    cooc = cooc.reshape(N_CHAMPS, N_CHAMPS)
    if not np.array_equal(cooc, cooc.T):
        raise RuntimeError("double comptage des cooccurrences inter-champs incohérent")
    n_top = math.ceil(params["frac_top"] * V)
    top1 = np.zeros(V, bool)
    top1[np.lexsort((np.arange(V), -df))[:n_top]] = True
    T = [np.flatnonzero(candidat & (champ == f)) for f in range(N_CHAMPS)]
    strates = [(f, g) for f in range(N_CHAMPS) for g in range(f + 1, N_CHAMPS)]
    N_s = np.array([len(T[f]) * len(T[g]) - cooc[f, g] for f, g in strates], np.int64)
    return dict(N=N, V=V, df=df, par_groupe=par_groupe, champ=champ, part=part, specifique=specifique,
                candidat=candidat, r=r, deg=deg, idf=idf, top1=top1, n_top=n_top, T=T, strates=strates, N_s=N_s,
                cooc_inter=cooc, XT=XT)


def allouer(N_s, total):
    """Allocation proportionnelle, plus fort reste (égalité : ordre des strates), somme exacte."""
    N_s = np.asarray(N_s, np.int64)
    somme = int(N_s.sum())
    if somme <= total:
        return N_s.copy()
    base = (N_s * total) // somme
    reste = (N_s * total) % somme
    manque = total - int(base.sum())
    ordre = np.lexsort((np.arange(N_s.size), -reste))
    base[ordre[:manque]] += 1
    return base


def cooccurrences(XT, A, C, budget=4_000_000):
    """Nombre de documents (lignes de XT : termes × documents) contenant A[i] et C[i]."""
    df = np.diff(XT.indptr)
    sortie = np.zeros(len(A), np.int64)
    for i0, i1 in lots_par_cout(df[A] + df[C], budget):
        P = XT[A[i0:i1]].multiply(XT[C[i0:i1]])
        sortie[i0:i1] = np.rint(np.asarray(P.sum(axis=1)).ravel()).astype(np.int64)
    return sortie


def tirer_paires(XT_avant, struct, n_s, seedseq):
    """Tirage uniforme sans remise par rejet dans chaque strate (section 5) ; A = terme du premier champ."""
    T, strates = struct["T"], struct["strates"]
    enfants = seedseq.spawn(len(strates))
    As, Cs, Ss, tires = [], [], [], []
    for k, ((f, g), n, ss) in enumerate(zip(strates, n_s, enfants)):
        n = int(n)
        if n == 0:
            tires.append(0)
            continue
        rng = np.random.default_rng(ss)
        Tf, Tg = T[f], T[g]
        ng = len(Tg)
        vus = np.empty(0, np.int64)
        acceptes, n_acc, n_tires = [], 0, 0
        while n_acc < n:
            reste = n - n_acc
            m = int(1.1 * reste) + 1000
            a = rng.integers(0, len(Tf), m, dtype=np.int64)
            c = rng.integers(0, ng, m, dtype=np.int64)
            n_tires += m
            cles = a * ng + c
            _, premier = np.unique(cles, return_index=True)
            premier.sort()
            cles = cles[premier]
            cles = cles[~np.isin(cles, vus)]
            vus = np.union1d(vus, cles)
            n_avant = cooccurrences(XT_avant, Tf[cles // ng], Tg[cles % ng])
            ok = cles[n_avant == 0][:reste]
            acceptes.append(ok)
            n_acc += ok.size
        cles = np.concatenate(acceptes)
        As.append(Tf[cles // ng])
        Cs.append(Tg[cles % ng])
        Ss.append(np.full(cles.size, k, np.int16))
        tires.append(n_tires)
    return np.concatenate(As), np.concatenate(Cs), np.concatenate(Ss), tires


_S = {}


def _scorer_blocs(bornes):
    b0, b1 = bornes
    X, XT, Hs, Ls, debut, uniq_H = _S["X"], _S["XT"], _S["Hs"], _S["Ls"], _S["debut"], _S["uniq_H"]
    df, w, wtop, inv_ln_deg, inv_deg = _S["df"], _S["w"], _S["wtop"], _S["inv_ln_deg"], _S["inv_deg"]
    budget_L = _S["budget_L"]
    hb = uniq_H[b0:b1]
    p0 = int(debut[b0])
    p1 = int(debut[b1]) if b1 < len(uniq_H) else len(Hs)
    GH = (XT[hb] @ X).toarray()
    lignes_h = np.arange(len(hb))
    if not np.array_equal(np.rint(GH[lignes_h, hb]).astype(np.int64), df[hb]):
        raise RuntimeError("diagonale incohérente (bloc H)")
    GH[lignes_h, hb] = 0.0
    hloc = np.searchsorted(hb, Hs[p0:p1]).astype(np.int64)
    sortie = np.zeros((6, p1 - p0))
    for q0, q1 in lots_par_cout(df[Ls[p0:p1]], budget_L):
        lrows = Ls[p0 + q0:p0 + q1]
        GL = XT[lrows] @ X
        nnz = np.diff(GL.indptr)
        n = q1 - q0
        ligne = np.repeat(np.arange(n, dtype=np.int64), nnz)
        cols = GL.indices
        cnt_L = GL.data.astype(np.float64)
        cnt_L[cols == lrows[ligne]] = 0.0
        cnt_H = GH[hloc[q0:q1][ligne], cols].astype(np.float64)
        produit = cnt_L * cnt_H
        commun = produit > 0
        sortie[0, q0:q1] = np.bincount(ligne, weights=produit * w[cols], minlength=n)
        sortie[1, q0:q1] = np.bincount(ligne, weights=produit * wtop[cols], minlength=n)
        sortie[2, q0:q1] = np.bincount(ligne[commun], minlength=n)
        sortie[3, q0:q1] = np.bincount(ligne[commun], weights=inv_ln_deg[cols[commun]], minlength=n)
        sortie[4, q0:q1] = np.bincount(ligne[commun], weights=inv_deg[cols[commun]], minlength=n)
        sortie[5, q0:q1] = GH[hloc[q0:q1], lrows]
        del GL, ligne, cols, cnt_L, cnt_H, produit, commun
    return p0, p1, sortie


def scorer(X_avant, struct, A, C, n_proc=1, taille_bloc=256, budget_L=150_000):
    """Scores S (et variantes orientées), AA, RA, CN, PA et K, K_top, sur les seules données d'avant (section 7)."""
    XT, df, r, deg, idf, top1 = struct["XT"], struct["df"], struct["r"], struct["deg"], struct["idf"], struct["top1"]
    if np.any(r <= 0):
        raise RuntimeError("r nul pour un terme du vocabulaire")
    w = idf / r
    inv_ln_deg = np.zeros(df.size)
    inv_ln_deg[deg >= 2] = 1.0 / np.log(deg[deg >= 2])
    inv_deg = np.zeros(df.size)
    inv_deg[deg >= 1] = 1.0 / deg[deg >= 1]
    haut = df[A] >= df[C]
    H = np.where(haut, A, C)
    L = np.where(haut, C, A)
    ordre = np.argsort(H, kind="stable")
    Hs, Ls = H[ordre], L[ordre]
    uniq_H, debut = np.unique(Hs, return_index=True)
    _S.clear()
    _S.update(X=X_avant, XT=XT, Hs=Hs, Ls=Ls, debut=debut, uniq_H=uniq_H, df=df, w=w, wtop=w * top1,
              inv_ln_deg=inv_ln_deg, inv_deg=inv_deg, budget_L=budget_L)
    blocs = [(b, min(b + taille_bloc, len(uniq_H))) for b in range(0, len(uniq_H), taille_bloc)]
    if n_proc <= 1:
        resultats = map(_scorer_blocs, blocs)
    else:
        pool = mp.get_context("fork").Pool(n_proc)
        resultats = pool.imap_unordered(_scorer_blocs, blocs, chunksize=1)
    tableau = np.zeros((6, len(A)))
    for p0, p1, sortie in resultats:
        tableau[:, ordre[p0:p1]] = sortie
    if n_proc > 1:
        pool.close()
        pool.join()
    _S.clear()
    K, K_top, CN, AA, RA, n_HL = tableau
    if np.any(n_HL != 0):
        raise RuntimeError("paire cooccurrente avant parmi les paires scorées")
    S_AC = K / r[A]
    S_CA = K / r[C]
    return dict(S=0.5 * (S_AC + S_CA), S_AC=S_AC, S_CA=S_CA, AA=AA, RA=RA, CN=CN,
                PA=df[A].astype(np.float64) * df[C].astype(np.float64), K=K, K_top=K_top)


def issues(XT_apres, A, C, seuil):
    n_apres = cooccurrences(XT_apres, A, C)
    return n_apres, (n_apres >= seuil).astype(np.int8)


def _termes_doc(X, d):
    return X.indices[X.indptr[d]:X.indptr[d + 1]].tolist()


def _docs_terme(XT, t):
    return XT.indices[XT.indptr[t]:XT.indptr[t + 1]].tolist()


def reference_paire(X, XT, a, c, idf, r, deg, top1):
    """Implémentation lente (compteurs Python) des composantes d'une paire, sur les seuls documents d'avant."""
    n_a, n_c = Counter(), Counter()
    for d in _docs_terme(XT, a):
        n_a.update(_termes_doc(X, d))
    for d in _docs_terme(XT, c):
        n_c.update(_termes_doc(X, d))
    del n_a[a]
    del n_c[c]
    communs = set(n_a) & set(n_c)
    K = sum(n_a[b] * n_c[b] * idf[b] / r[b] for b in communs)
    K_top = sum(n_a[b] * n_c[b] * idf[b] / r[b] for b in communs if top1[b])
    return dict(K=K, K_top=K_top, CN=float(len(communs)), AA=sum(1.0 / math.log(deg[b]) for b in communs),
                RA=sum(1.0 / deg[b] for b in communs), r_A=float(sum(n_a.values())), r_C=float(sum(n_c.values())),
                n_AC=float(n_a.get(c, 0)))


def reference_terme(X, XT, t):
    voisins, r = set(), 0
    for d in _docs_terme(XT, t):
        termes = _termes_doc(X, d)
        voisins.update(termes)
        r += len(termes) - 1
    voisins.discard(t)
    return len(voisins), float(r)


def ecart_relatif(x, y):
    x, y = float(x), float(y)
    if x == y:
        return 0.0
    return abs(x - y) / max(abs(x), abs(y))
