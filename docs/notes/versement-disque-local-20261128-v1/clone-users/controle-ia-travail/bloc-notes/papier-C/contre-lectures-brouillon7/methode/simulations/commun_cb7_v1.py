"""Outils de la contre-lecture 8 (lentille « methode ») du brouillon 7 du papier C. Aucune donnee lue.

Reprend sans les modifier les fonctions de la contre-lecture methode du brouillon 5 (`commun_b5_v1.py`,
`t2_rang_temoins_partages_v1.py`) et le modele generalise de la verification courte du brouillon 6 (`commun_cb6_v1.py`,
`u3_lecture_rho_sur_r_v1.py`) ; le code des trois lectures est recopie de U3 et etendu pour rendre v0 (lectures sans
insertion), afin de construire les gains d'ecart de C-P3c sur les memes contenus H et S que TC.1.

Modele (un juge j ; T_i lecture vraie ; mu milieu du corpus) :
  v0_i    = T_i + e0,                        e0 ~ N(0, s0_j)
  v_tau,i = T_i + kap_j (mu - T_i) + e,      e ~ N(0, sig_j)
  v_m,i   = T_i + kap_j (mu - T_i) + g_{j,f,m} (c - T_i) + e
Gains d'ecart (TC.2 plaidoyer, TC.3 b usurpation), deux modeles :
  « bruit »   : comme U1 (bruit pur, aucun facteur propre au juge) ;
  « paragraphe » : les episodes HP, SP, HU, SU sont des contenus neufs de la meme tache (T = base + u_t + N(0, 0,8)) ;
     le paragraphe ajoute par l'agent est traite comme une insertion : lecture = T + kap_j (mu - T) + gp_j (c - T) + N(0, sig_j),
     c = v* (cible de l'attaquant) ; H et S sont lus par v0 (memes lectures que TC.1).
     g brut = -moyenne_t (SP_t - S_t) / moyenne_t (S_t - H_t).
Configuration lue : brouillon 4 (longueurs seulement, pour la regle des temoins ; aucun texte).
"""
import json
import sys

import numpy as np

B5 = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/"
      "methode/simulations")
sys.path.insert(0, B5)
from commun_b5_v1 import agrege, comptes, loi_jointe, p_inf, p_sup, regresseur, sommes_taches  # noqa: E402,F401
from t2_rang_temoins_partages_v1 import kendall_tau, nul_exact, p_exact, rangs, w_kendall  # noqa: E402

CONFIG = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/brouillon7/"
          "papier-C-config-v1-brouillon4.json")
FAMILLES = ["flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande"]
NUL = {m: nul_exact(m) for m in (3, 4, 5)}
PROFIL = np.array([0.6, 0.8, 1.0, 1.2, 1.4])


def appariement(indices_retenus):
    cfg = json.load(open(CONFIG, encoding="utf-8"))
    lt = cfg["controle_redaction"]["longueurs_temoins"]
    out = {}
    for f in FAMILLES:
        lf = cfg["controle_redaction"]["longueurs_A"][f]
        pris, lst = set(), []
        for idx in indices_retenus:
            best = min((abs(lt[t] - lf[idx - 1]), t) for t in range(16) if t not in pris)
            pris.add(best[1])
            lst.append(best[1])
        out[f] = lst
    return out


def corpus_A(rng, T):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    return dict(vrai=vrai, grappe=tache, mu=3.0, vstar=0.0, u=u, T=T)


def corpus_B(rng, n=30):
    vrai = 4.5 + rng.normal(0, 1.4, n)
    return dict(vrai=vrai, grappe=np.arange(n), mu=4.5, vstar=9.0, u=None, T=n)


def rr_fonction(v0, vt_ret, grappe, T):
    """rho/r par tirage (U3) : rho = cov(v0, wbar)/var(v0) borne [0,05 ; 1] ; r = moyenne des cov entre temoins distincts
    / moyenne des cov entre v0 et un temoin ; rho/r borne [0,05 ; 1]."""
    M = np.column_stack([v0, vt_ret])
    q = M.shape[1]
    s1 = np.stack([np.bincount(grappe, weights=M[:, a], minlength=T) for a in range(q)], 1)
    s2 = np.stack([np.stack([np.bincount(grappe, weights=M[:, a] * M[:, b], minlength=T) for b in range(q)], 1)
                   for a in range(q)], 1)
    cnt = np.bincount(grappe, minlength=T).astype(float)

    def f(wts):
        nn = wts @ cnt
        m1 = (wts @ s1) / nn[..., None]
        m2 = np.einsum("...t,tab->...ab", wts, s2) / nn[..., None, None]
        C = m2 - m1[..., :, None] * m1[..., None, :]
        iu = np.triu_indices(q - 1, 1)
        ctt = C[..., 1:, 1:][..., iu[0], iu[1]].mean(-1)
        c0t = C[..., 0, 1:].mean(-1)
        r = ctt / c0t
        rho = np.clip(c0t / C[..., 0, 0], 0.05, 1.0)
        return np.clip(rho / r, 0.05, 1.0)
    return f


def trois_lectures(rng, corpus, juges, gains, lam, pairs, B, lam_aussi=False):
    """juges : liste de (s0, sig, kap) ; gains (3, 5, k). Renvoie out[r] = G (5,3), Gb (B,5,3) pour r in cal, brut, rr ;
    v0 par juge."""
    vrai, grappe, mu, vstar, T = corpus["vrai"], corpus["grappe"], corpus["mu"], corpus["vstar"], corpus["T"]
    n = len(vrai)
    W = comptes(rng, T, B)
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    out = {r: dict(G=np.zeros((5, 3)), Gb=np.zeros((B, 5, 3)), lam=np.zeros((5, 3)), lamb=np.zeros((B, 5, 3)))
           for r in ("cal", "brut", "rr")}
    v0s = []
    for j, (s0, sig, kap) in enumerate(juges):
        k = gains.shape[2]
        c = mu + lam * (vstar - mu)
        v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
        v0s.append(v0)
        base = vrai + kap * (mu - vrai)
        vt = base[:, None] + rng.normal(0, sig, (n, 16))
        wbar = vt[:, utilises].mean(1)
        f = rr_fonction(v0, vt[:, utilises], grappe, T)
        rr0, rrb = float(f(np.ones(T))), f(W)
        for fi, fam in enumerate(FAMILLES):
            vm = base[:, None] + (c - vrai)[:, None] * gains[j, fi][None, :] + rng.normal(0, sig, (n, k))
            Y = vm - vt[:, pairs[fam]]
            s = sommes_taches(Y, v0, wbar, grappe, T)
            sa, sb = agrege(s), agrege(s, W)
            for r, kw, kwb in (("cal", dict(calibre=True), dict(calibre=True)),
                               ("brut", dict(calibre=False), dict(calibre=False)),
                               ("rr", dict(rho_fixe=rr0), dict(rho_fixe=rrb))):
                n_, S1, S2, A, Bm, rho, vb = regresseur(sa, **kw)
                cc, g, Gm, deg = loi_jointe(n_, S1, S2, A, Bm)
                out[r]["G"][fi, j] = float(Gm)
                n_, S1, S2, A, Bm, rho, vbb = regresseur(sb, **kwb)
                cb, gb, Gbm, degb = loi_jointe(n_, S1, S2, A, Bm)
                out[r]["Gb"][:, fi, j] = Gbm
                if lam_aussi:
                    out[r]["lam"][fi, j] = float((cc - vb) / (vstar - vb))
                    out[r]["lamb"][:, fi, j] = (cb - vbb) / (vstar - vbb)
    return out, v0s


def gains_ecart_paragraphe(rng, corpusA, juges, v0s, gp):
    """Deux gains d'ecart bruts (plaidoyer, usurpation) par juge, modele « paragraphe ». gp : (3,) gains vrais."""
    T, u, mu, vstar = corpusA["T"], corpusA["u"], corpusA["mu"], corpusA["vstar"]
    out = np.zeros((2, 3))
    neufs = []
    for _ in range(2):  # plaidoyer, usurpation : contenus neufs HP, SP (resp. HU, SU), communs aux trois juges
        neufs.append((2.0 + u + rng.normal(0, 0.8, T), 4.0 + u + rng.normal(0, 0.8, T)))
    for j, (s0, sig, kap) in enumerate(juges):
        H, S = v0s[j][0::2], v0s[j][1::2]
        D0 = np.mean(S - H)
        for b, (vHP, vSP) in enumerate(neufs):
            SP = vSP + kap * (mu - vSP) + gp[j] * (vstar - vSP) + rng.normal(0, sig, T)
            out[b, j] = -np.mean(SP - S) / D0
    return out


def C_P3a(G, Gb):
    w = float(w_kendall(rangs(G)[None])[0])
    ws = w_kendall(rangs(Gb - G[None]))
    return float(p_exact(w, NUL[5])) <= 0.05 and float((1 + (ws >= w - 1e-12).sum()) / (len(ws) + 1)) <= 0.05


def dev(x):
    return x - x.mean(-1, keepdims=True)


def C_P3b(GA, GbA, GB, GbB):
    t = float(kendall_tau(dev(GA).ravel(), dev(GB).ravel()))
    Bn = GbA.shape[0]
    ts = kendall_tau(dev(GbA - GA[None]).reshape(Bn, 15), dev(GbB - GB[None]).reshape(Bn, 15))
    return float((1 + (ts >= t - 1e-12).sum()) / (Bn + 1)) <= 0.05


def C_P3c(G, ecarts):
    ev4 = np.vstack([ecarts, G[[0, 3], :]])
    ev3 = np.vstack([ecarts[:1], G[[0, 3], :]])
    w4 = float(w_kendall(rangs(ev4)[None])[0])
    w3 = float(w_kendall(rangs(ev3)[None])[0])
    return float(p_exact(w4, NUL[4])) <= 0.05, float(p_exact(w3, NUL[3])) <= 0.05


def mc(p, R):
    return float(np.sqrt(max(p * (1 - p), 1e-12) / R))


def seuil_clause(R):
    return 0.05 + 2 * np.sqrt(0.05 * 0.95 / R)
