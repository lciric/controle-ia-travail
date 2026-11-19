"""Outils de la verification courte de methode du brouillon 6 du papier C (lentille « methode-courte »). Aucune donnee lue.

Reprend, sans les modifier, les fonctions de la contre-lecture methode du brouillon 5 (dossier
`contre-lectures-brouillon5/methode/simulations/`, manifeste 6f76e9df...) : loi jointe en forme fermee, regresseur
calibre ou non (rho = 1), sommes par tache, comptes multinomiaux, lois exactes du W.

Modele generalise (un juge j) : lecture vraie T_i d'un contenu ; mu = milieu du corpus ;
  v0_i      = T_i + e0,           e0 ~ N(0, s0_j)                (erreur sur la lecture sans insertion)
  v_tau,i   = T_i + kap_j (mu - T_i) + e,       e ~ N(0, sig_j)  (temoin : compression kap_j et erreur d'insertion)
  v_m,i     = T_i + kap_j (mu - T_i) + g_{j,f,m} (c - T_i) + e   (insertion de rang m de la famille f)
Modele « S » de T3 : s0 = sig, kap = 0. Modele « D » de T3 : s0 = 0, kap > 0. Un juge peut porter les deux.
Le reechantillonnage par grappes (taches du corpus A, items du corpus B) utilise les memes comptes pour les trois juges et
pour toutes les familles d'un corpus (point 11 : memes tirages pour toutes les statistiques d'un corpus).
"""
import json
import sys

import numpy as np

B5 = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5/"
      "methode/simulations")
sys.path.insert(0, B5)
from commun_b5_v1 import agrege, comptes, loi_jointe, p_inf, p_sup, regresseur, sommes_taches  # noqa: E402
from t2_rang_temoins_partages_v1 import kendall_tau, nul_exact, p_exact, rangs, w_kendall  # noqa: E402

CONFIG = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/brouillon6/"
          "papier-C-config-v1-brouillon3.json")
FAMILLES = ["flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande"]
NUL = {m: nul_exact(m) for m in (3, 4, 5)}


def appariement(indices_retenus):
    """Regle `regle_temoins` de la configuration brouillon 3 : dans l'ordre des rangs croissants, temoin de longueur la
    plus proche parmi ceux non encore pris dans la meme famille ; egalites : plus petit indice ; reutilisable entre
    familles. Seules les longueurs sont lues (aucun texte)."""
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
    return vrai, tache, 3.0, 0.0  # vrai, grappe, mu, v*


def corpus_B(rng, n=30):
    vrai = 4.5 + rng.normal(0, 1.4, n)
    return vrai, np.arange(n), 4.5, 9.0


def lectures_juge(rng, vrai, mu, vstar, s0, sig, kap, gains, lam, pairs):
    """gains : (5, k) gains vrais g_{f,m} du juge. Renvoie v0, wbar, liste des Y (n, k) par famille."""
    n = len(vrai)
    k = gains.shape[1]
    c = mu + lam * (vstar - mu)
    v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
    base = vrai + kap * (mu - vrai)
    vt = base[:, None] + rng.normal(0, sig, (n, 16))
    utilises = sorted({t for f in FAMILLES for t in pairs[f]})
    wbar = vt[:, utilises].mean(1)
    Ys = []
    for fi, f in enumerate(FAMILLES):
        vm = base[:, None] + (c - vrai)[:, None] * gains[fi][None, :] + rng.normal(0, sig, (n, k))
        Ys.append(vm - vt[:, pairs[f]])
    return v0, wbar, Ys


def G_corpus(rng, corpus, juges, gains, lam, pairs, B):
    """juges : liste de (s0, sig, kap) ; gains : (3, 5, k). Renvoie, pour chaque lecture ('cal', 'brut'),
    G (5, 3) et Gb (B, 5, 3), et lam_hat (5, 3), lamb (B, 5, 3)."""
    vrai, grappe, mu, vstar = corpus
    T = int(grappe.max()) + 1
    W = comptes(rng, T, B)
    out = {r: dict(G=np.zeros((5, 3)), Gb=np.zeros((B, 5, 3)), lam=np.zeros((5, 3)), lamb=np.zeros((B, 5, 3)),
                   deg=np.zeros((5, 3))) for r in ("cal", "brut")}
    for j, (s0, sig, kap) in enumerate(juges):
        v0, wbar, Ys = lectures_juge(rng, vrai, mu, vstar, s0, sig, kap, gains[j], lam, pairs)
        for fi, Y in enumerate(Ys):
            s = sommes_taches(Y, v0, wbar, grappe, T)
            sa, sb = agrege(s), agrege(s, W)
            for r, cal in (("cal", True), ("brut", False)):
                n_, S1, S2, A, Bm, rho, vb = regresseur(sa, calibre=cal)
                c, g, Gm, deg = loi_jointe(n_, S1, S2, A, Bm)
                out[r]["G"][fi, j] = float(Gm)
                out[r]["lam"][fi, j] = float((c - vb) / (vstar - vb))
                n_, S1, S2, A, Bm, rho, vbb = regresseur(sb, calibre=cal)
                cb, gb, Gbm, degb = loi_jointe(n_, S1, S2, A, Bm)
                out[r]["Gb"][:, fi, j] = Gbm
                out[r]["lamb"][:, fi, j] = (cb - vbb) / (vstar - vbb)
                out[r]["deg"][fi, j] = (degb | (np.abs(vstar - vbb) < 0.5)).mean()
    return out


def C_P3a(G, Gb):
    """Renvoie (W, p exact, p centre)."""
    w = float(w_kendall(rangs(G)[None])[0])
    ws = w_kendall(rangs(Gb - G[None]))
    return w, float(p_exact(w, NUL[5])), float((1 + (ws >= w - 1e-12).sum()) / (len(ws) + 1))


def dev(x):
    return x - x.mean(-1, keepdims=True)


def C_P3b(GA, GbA, GB, GbB):
    """tau entre ecarts intra-famille de A et de B ; p unilateral par reechantillonnage centre des deux corpus."""
    t = float(kendall_tau(dev(GA).ravel(), dev(GB).ravel()))
    Bn = GbA.shape[0]
    ts = kendall_tau(dev(GbA - GA[None]).reshape(Bn, 15), dev(GbB - GB[None]).reshape(Bn, 15))
    return t, float((1 + (ts >= t - 1e-12).sum()) / (Bn + 1))


def C_P3c(G, bruit):
    """bruit : (2, 3) gains d'ecart (TC.2, TC.3 b). Renvoie p exact a quatre evaluateurs et a trois (sans P-020)."""
    ev4 = np.vstack([bruit, G[[0, 3], :]])
    ev3 = np.vstack([bruit[:1], G[[0, 3], :]])
    w4 = float(w_kendall(rangs(ev4)[None])[0])
    w3 = float(w_kendall(rangs(ev3)[None])[0])
    return float(p_exact(w4, NUL[4])), float(p_exact(w3, NUL[3]))


def mc(p, R):
    """erreur de Monte-Carlo d'une proportion."""
    return float(np.sqrt(max(p * (1 - p), 1e-12) / R))
