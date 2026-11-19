"""Données simulées pour les essais du module du papier C (v1). Aucune donnée réelle.

Modèle d'un juge (celui de la vérification courte de méthode de la session 16, repris de sa description) :
lecture vraie T_i d'un contenu ; mu = milieu du corpus ;
  v0_i    = T_i + e0,                       e0 ~ N(0, s0)   (erreur sur la lecture sans insertion)
  v_tau,i = T_i + kap (mu − T_i) + e,       e ~ N(0, sig)   (témoin : compression kap et erreur d'insertion)
  v_m,i   = T_i + kap (mu − T_i) + g_{f,m} (c − T_i) + e    (insertion de rang m de la famille f)
Modèle « erreur sur v0 » : s0 = sig, kap = 0. Modèle « v0 exact et compression » : s0 = 0, kap > 0.
"""
import numpy as np

FAMILLES = ("flatterie_supplication", "revendication_autorite", "approbations_forgees", "usurpation_stylistique",
            "ordres_en_bande")


def appariement(cfg: dict, indices=(1, 8, 16)) -> dict:
    """Règle des témoins de la configuration, sur les longueurs seulement (aucun texte lu)."""
    from derivation import apparier_les_temoins
    lt = cfg["controle_redaction"]["longueurs_temoins"]
    return {f: apparier_les_temoins([cfg["controle_redaction"]["longueurs_A"][f][i - 1] for i in indices], lt)
            for f in FAMILLES}


def corpus_A(rng, T):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    return {"vrai": vrai, "grappes": tache, "mu": 3.0, "v_etoile": 0.0, "saboteur": np.tile([False, True], T)}


def corpus_B(rng, n=30):
    return {"vrai": 4.5 + rng.normal(0, 1.4, n), "grappes": np.arange(n), "mu": 4.5, "v_etoile": 9.0}


def juge(rng, corpus, s0, sig, kap, gains, lam, paires, constat_gain=0.0):
    """`gains` : (5, k) gains vrais g_{f,m}. Rend le dictionnaire d'un juge au format de `analyser_etape2`."""
    vrai, mu = corpus["vrai"], corpus["mu"]
    n = vrai.size
    c = mu + lam * (corpus["v_etoile"] - mu)
    v0 = vrai + (rng.normal(0, s0, n) if s0 > 0 else 0.0)
    base = vrai + kap * (mu - vrai)
    vt = base[:, None] + rng.normal(0, sig, (n, 16))
    retenus = sorted({t for f in FAMILLES for t in paires[f]} | {4})
    familles = {}
    for fi, f in enumerate(FAMILLES):
        k = gains.shape[1]
        vm = base[:, None] + (c - vrai)[:, None] * gains[fi][None, :] + rng.normal(0, sig, (n, k))
        familles[f] = {"v": vm.T, "temoins": list(paires[f])}
    constat = base + constat_gain * (c - vrai) + rng.normal(0, sig, n)
    return {"v0": v0, "familles": familles, "temoins": {t: vt[:, t - 1] for t in retenus},
            "constat": {"v": constat, "temoin": 4}, "neutres": mu + rng.normal(0, 0.3, 6)}


def cellules(rng, T, d0, gains_plaidoyer, gain_usurpation, bruit=0.3, pente_honnete=0.0):
    """Cellules d'un moniteur dans le plan apparié : S − H = d0 en moyenne ; SP_m = S − g_m d0 ; HP_m = H − pente."""
    u = rng.normal(0, 0.5, T)
    H = 2.0 + u + rng.normal(0, bruit, T)
    S = 2.0 + d0 + u + rng.normal(0, bruit, T)
    g = np.asarray(gains_plaidoyer, dtype=float)
    SP = S[None, :] - (g * d0)[:, None] + rng.normal(0, bruit, (g.size, T))
    HP = H[None, :] - pente_honnete + rng.normal(0, bruit, (g.size, T))
    SU = S - gain_usurpation * d0 + rng.normal(0, bruit, T)
    HU = H + rng.normal(0, bruit, T)
    return {"H": H, "S": S, "HP": HP, "SP": SP, "HU": HU[None, :], "SU": SU[None, :]}


def sonde(rng, T, nom="sonde-1", d0=2.0, gains=(0.0, 0.0, 0.0), gain_u=0.0, trahison=0.3, agregation="max"):
    ch = cellules(rng, T, d0, gains, gain_u, 0.15)
    k = len(gains)
    bruit = lambda: rng.normal(0, 0.15, (k, T))
    ex_HP = bruit()
    ex_SP = ex_HP + trahison * d0 + bruit()            # g_trahison = −moyenne(E_SP − E_HP) / D0 ≈ −trahison
    lecteur = cellules(rng, T, d0, (0.3,) * k, 0.0, 0.15)
    lex_HP = bruit()
    return {"nom": nom, "agregation": agregation, "champs": ch,
            "complete": {c: v + rng.normal(0, 0.05, np.shape(v)) for c, v in ch.items()},
            "filtree": {c: v + rng.normal(0, 0.05, np.shape(v)) for c, v in ch.items()},
            "excedent": {"SP": ex_SP, "HP": ex_HP, "L_HP": lex_HP, "L_H": bruit()},
            "lecteur": {"champs": {"H": lecteur["H"], "S": lecteur["S"]},
                        "excedent": {"SP": ex_HP - 0.3 * d0 + bruit(), "HP": ex_HP}},
            "lexical_mesure": True}


def alarme(rng, taches, n_ordres_par_tache=6, detection=0.99):
    T = len(taches)
    tt = np.repeat(taches, 8)
    temoins = np.clip(rng.normal(1.0, 0.8, tt.size), 0, 9)
    to = np.repeat(taches, n_ordres_par_tache)
    ordres = np.where(rng.random(to.size) < detection, rng.normal(7.5, 0.6, to.size), rng.normal(1.0, 0.5, to.size))
    return {"temoins": temoins, "tache_temoins": tt, "ordres": ordres, "tache_ordres": to}


def donnees_completes(cfg, graine=0, T=30, g=0.25, lam=1.0, s0=0.3, sig=0.3, kap=0.0, gains_juges_tc2=(0.5, 0.6, 0.7),
                      sondes=None, gains_par_famille=None):
    """Jeu complet et cohérent pour `analyser_etape2` : trois juges, cinq familles de trois rangs, deux corpus, TC.2."""
    rng = np.random.default_rng(graine)
    paires = appariement(cfg)
    A, Bc = corpus_A(rng, T), corpus_B(rng)
    echelle = np.array([0.5, 1.0, 1.5])
    if gains_par_famille is None:
        gains_par_famille = [g, g, g, g, g]
    juges_A, juges_B, juges_tc2 = [], [], []
    taches = np.arange(T)
    for j in range(3):
        gains = np.array([gf * (1 + 0.3 * j) * echelle for gf in gains_par_famille])
        ja = juge(rng, A, s0, sig, kap, gains, lam, paires, g)
        ja["alarme"] = alarme(rng, taches)
        juges_A.append(ja)
        juges_B.append(juge(rng, Bc, s0, sig, kap, gains, lam, paires, g))
        gj = gains_juges_tc2[j]
        juges_tc2.append(cellules(rng, T, 2.0, (0.6 * gj, gj, 1.4 * gj), gj))
    if sondes is None:
        sondes = [sonde(rng, T, "sonde-1"), sonde(rng, T, "sonde-2")]
    return {"corpus_A": {"taches": A["grappes"], "saboteur": A["saboteur"], "juges": juges_A},
            "corpus_B": {"items": Bc["grappes"], "juges": juges_B},
            "tc2": {"taches": taches, "juges": juges_tc2, "sondes": sondes, "controlabilite_mesuree": True,
                    "hc2_non_testable": False}}
