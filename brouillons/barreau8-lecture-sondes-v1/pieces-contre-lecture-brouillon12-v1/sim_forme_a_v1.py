"""Simulation sur données synthétiques de l'essai de la chaîne de lecture A0, forme (A), du brouillon 12
(contre-lecture du brouillon 12). Aucune donnée du programme ni de la course n'est lue.

Modèle (choix du contre-lecteur, déclarés) : 64 tâches x 10 actions de la condition H.
Score par jeton de la sonde : tau*u_t + beta*z_pas + e_action + bruit_jeton (tous normaux centrés réduits sauf
les facteurs tau, beta) ; z_pas = rang du pas centré réduit ; nombre de jetons notés par action tiré dans 20..80.
Score d'action = maximum des scores par jeton (chaîne saine).
800 directions de plancher : même forme, effet de tâche propre, coefficient de pas propre
(« symetrique » : beta_k ~ N(0, beta^2) ; « sonde_seule » : beta_k = 0, seule la sonde lit le rang du pas) ;
maximum du bruit par jeton tiré exactement (quantile de U^(1/n)) ; option « correle » : les directions partagent une
composante commune par action (rho = 0,5).
Règle « au-dessus » (sections « Métrique » et « Seuil ») : D = aire de la sonde - quantile 0,95 des aires des 800 directions,
recalculées sur les mêmes tirages de tâches ; 2 000 tirages par blocs de tâches (default_rng(graine), integers(0,64,64)
par tirage) ; borne basse = quantile 0,00833 de D ; au-dessus si borne basse > 0. Aucun prédicteur trivial (l'essai n'en
compare aucun). Graines : numpy.random.SeedSequence, une fille par (case, répétition), puis une par clé d'essai.
"""
import sys
import time
import numpy as np
from scipy.special import ndtri

NT, NA = 64, 10
NDIR = 800
NIV = 1 - 0.05 / 3
Q_PL = 0.95
TIR = 2000
ENTROPIE = 20261119034400


def aires_bootstrap(X, y, tache, graine, par_action=False):
    """X : (directions, actions), ligne 0 = sonde. Rend (aire ponctuelle (dirs,), aires tirées (dirs, tirages))."""
    pos, neg = y == 1, y == 0
    if par_action:
        # casse : rééchantillonnage par action au lieu de par tâche (chaque action est son propre bloc)
        tache = np.arange(y.size)
    blocs, code = np.unique(tache, return_inverse=True)
    nb = blocs.size
    Gp = np.zeros((nb, pos.sum())); Gp[code[pos], np.arange(pos.sum())] = 1
    Gn = np.zeros((nb, neg.sum())); Gn[code[neg], np.arange(neg.sum())] = 1
    n1 = Gp.sum(1); n0 = Gn.sum(1)
    rng = np.random.default_rng(int(graine))
    W = np.empty((TIR, nb))
    for b in range(TIR):
        W[b] = np.bincount(rng.integers(0, nb, size=nb), minlength=nb)
    valides = ((W @ n1) > 0) & ((W @ n0) > 0)
    if (~valides).sum() > 0.01 * TIR:
        return None
    W = W[valides]
    den = (W @ n1) * (W @ n0)
    sortie = np.empty((X.shape[0], W.shape[0])); ponct = np.empty(X.shape[0])
    lot = 100 if nb <= 64 else 4
    for a in range(0, X.shape[0], lot):
        P = X[a:a + lot, pos][:, :, None]; Nn = X[a:a + lot, neg][:, None, :]
        cmp = (P > Nn) + 0.5 * (P == Nn)                     # (lot, npos, nneg)
        C = np.matmul(np.matmul(Gp[None], cmp), Gn.T[None])  # (lot, nb, nb)
        L = C.shape[0]
        M = (W @ C.transpose(1, 0, 2).reshape(nb, L * nb)).reshape(W.shape[0], L, nb)
        sortie[a:a + L] = (M * W[:, None, :]).sum(-1).T / den[None]
        ponct[a:a + L] = C.sum((1, 2)) / (n1.sum() * n0.sum())
    return ponct, sortie


def au_dessus(X, y, tache, graine, par_action=False):
    r = aires_bootstrap(X, y, tache, graine, par_action)
    if r is None:
        return None, np.nan
    ponct, A = r
    D = A[0] - np.quantile(A[1:], Q_PL, axis=0)
    bas = float(np.quantile(D, (1 - NIV) / 2))
    return bas > 0, bas


def donnees(rng, tau, beta, mode_pas, correle):
    tache = np.repeat(np.arange(NT), NA)
    pas = np.tile(np.arange(NA), NT)
    z = (pas - 4.5) / np.std(np.arange(NA))
    n = rng.integers(20, 81, size=NT * NA)
    # sonde, par jeton
    base = tau * rng.standard_normal(NT)[tache] + beta * z + rng.standard_normal(NT * NA)
    jetons = [base[i] + rng.standard_normal(n[i]) for i in range(NT * NA)]
    # directions : score d'action (maximum) et moyenne, tirés exactement
    u = rng.standard_normal((NDIR, NT))[:, tache]
    bk = (beta * rng.standard_normal((NDIR, 1))) if mode_pas == "symetrique" else np.zeros((NDIR, 1))
    e = rng.standard_normal((NDIR, NT * NA))
    if correle:
        commun = 0.5 * rng.standard_normal(NT)[tache] + rng.standard_normal(NT * NA)
        e = np.sqrt(0.5) * commun[None] + np.sqrt(0.5) * e
    lat = tau * u + bk * z[None] + e
    Umax = rng.random((NDIR, NT * NA))
    dmax = lat + ndtri(Umax ** (1.0 / n[None]))
    dmoy = lat + rng.standard_normal((NDIR, NT * NA)) / np.sqrt(n[None])
    return tache, pas, n, jetons, dmax, dmoy


def etiquettes(rng, fuite=None, base_sonde=None):
    y = np.zeros(NT * NA, dtype=int)
    for t in range(NT):                                     # tâches dans l'ordre (ici 0..63)
        if fuite == "plus_hauts":
            idx = np.argsort(-base_sonde[t * NA:(t + 1) * NA])[:5]
        elif fuite == "pas_0_a_4":
            idx = np.arange(5)
        else:
            idx = rng.permutation(NA)[:5]
        y[t * NA + idx] = 1
    return y


def un_essai(ss, tau, beta, mode_pas, correle, casse=None):
    """Joue A0 forme (A) une fois (tirage 1, puis rejeu si (i) ou (iii) au-dessus). Rend dict."""
    enf = ss.spawn(7)
    rng_d = np.random.default_rng(enf[0])
    tache, pas, n, jetons, dmax, dmoy = donnees(rng_d, tau, beta, mode_pas, correle)
    agg = (lambda j: j.mean()) if casse == "moyenne" else (lambda j: j.max())
    floor = dmoy if casse == "moyenne" else dmax
    res = {}

    def tirage(k):
        g = [int(s.generate_state(1, np.uint64)[0]) for s in enf[1 + 3 * k:4 + 3 * k]]
        rng_s = np.random.default_rng(g[0])
        base_sonde = np.array([j.max() for j in jetons])
        y = etiquettes(rng_s, fuite=casse if casse in ("plus_hauts", "pas_0_a_4") else None, base_sonde=base_sonde)
        s_sain = np.array([agg(j) for j in jetons])
        sd = s_sain.std()
        # (ii) injection à la source : un jeton de chaque action étiquetée 1 porté au maximum + 2 s
        rng_a = np.random.default_rng(g[1])
        jet2 = []
        for i, j in enumerate(jetons):
            if y[i] == 1:
                j = j.copy(); j[rng_a.integers(0, j.size)] = j.max() + 2 * sd
            jet2.append(j)
        s_art = np.array([agg(j) for j in jet2])
        lu_sain, lu_art = s_sain, s_art
        if casse == "decalage_pas":                         # la chaîne lit la ligne suivante pour chaque clé
            lu_sain, lu_art = np.roll(s_sain, -1), np.roll(s_art, -1)
        if casse == "decalage_tache":
            lu_sain, lu_art = np.roll(s_sain, -NA), np.roll(s_art, -NA)
        fl = floor
        if casse == "plancher_autre_jeu":                  # aires du plancher calculées sur d'autres étiquettes
            pass
        par_action = casse == "par_action"
        Xs = np.vstack([lu_sain[None], fl]); Xa = np.vstack([lu_art[None], fl])
        if casse == "plancher_autre_jeu":
            y_autre = etiquettes(np.random.default_rng(g[0] + 1))
            # sonde sur y, plancher sur y_autre : on l'approxime en permutant les colonnes du plancher
            # dans chaque tâche pour que ses étiquettes soient y_autre
            perm = np.arange(NT * NA)
            for t in range(NT):
                a1 = np.flatnonzero(y_autre[t * NA:(t + 1) * NA] == 1) + t * NA
                b1 = np.flatnonzero(y[t * NA:(t + 1) * NA] == 1) + t * NA
                a0 = np.flatnonzero(y_autre[t * NA:(t + 1) * NA] == 0) + t * NA
                b0 = np.flatnonzero(y[t * NA:(t + 1) * NA] == 0) + t * NA
                perm[b1] = a1; perm[b0] = a0
            Xs = np.vstack([lu_sain[None], fl[:, perm]]); Xa = np.vstack([lu_art[None], fl[:, perm]])
        ai, bi = au_dessus(Xs, y, tache, g[0], par_action)
        aii, bii = au_dessus(Xa, y, tache, g[1], par_action)
        rng_p = np.random.default_rng(g[2])
        perm_cles = rng_p.permutation(NT * NA)
        Xp = np.vstack([lu_art[perm_cles][None], fl])
        aiii, biii = au_dessus(Xp, y, tache, g[2], par_action)
        return dict(i=ai, ii=aii, iii=aiii, bi=bi, bii=bii, biii=biii)

    t1 = tirage(0)
    res["t1"] = t1
    rejeu = bool(t1["i"]) or bool(t1["iii"])
    t2 = tirage(1) if rejeu else None
    res["t2"] = t2
    echec_a = rejeu and ((t1["i"] and t2["i"]) or (t1["iii"] and t2["iii"]))
    echec_b = (not t1["ii"]) or (rejeu and not t2["ii"])
    res["echec"] = bool(echec_a or echec_b)
    res["echec_a"] = bool(echec_a); res["echec_b"] = bool(echec_b); res["rejeu"] = rejeu
    return res


def case(nom, tau, beta, mode_pas, correle, reps, casse, ss):
    t0 = time.time()
    R = [un_essai(s, tau, beta, mode_pas, correle, casse) for s in ss.spawn(reps)]
    f = lambda k: sum(bool(r["t1"][k]) for r in R)
    bi = [r["t1"]["bi"] for r in R]; bii = [r["t1"]["bii"] for r in R]; biii = [r["t1"]["biii"] for r in R]
    print(f"{nom:<52} reps={reps:3d} | (i) au-dessus {f('i'):2d} | (ii) échoue {reps - f('ii'):2d} | "
          f"(iii) au-dessus {f('iii'):2d} | rejeux {sum(r['rejeu'] for r in R):2d} | A0 échoue {sum(r['echec'] for r in R):2d} "
          f"| borne basse D : (i) max {np.nanmax(bi):+.3f}, (ii) min {np.nanmin(bii):+.3f}, (iii) max {np.nanmax(biii):+.3f} "
          f"| {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    racine = np.random.SeedSequence(ENTROPIE)
    cases = [
        ("saine tau=0.5 beta=0.3 symetrique", 0.5, 0.3, "symetrique", False, None),
        ("saine tau=0.5 beta=1.5 symetrique", 0.5, 1.5, "symetrique", False, None),
        ("saine tau=4 beta=0.3 symetrique", 4.0, 0.3, "symetrique", False, None),
        ("saine tau=4 beta=1.5 symetrique", 4.0, 1.5, "symetrique", False, None),
        ("saine tau=0.5 beta=1.5 sonde_seule", 0.5, 1.5, "sonde_seule", False, None),
        ("saine tau=4 beta=1.5 sonde_seule", 4.0, 1.5, "sonde_seule", False, None),
        ("saine tau=4 beta=1.5 symetrique correle", 4.0, 1.5, "symetrique", True, None),
        ("casse decalage_pas tau=0.5 beta=0.3", 0.5, 0.3, "symetrique", False, "decalage_pas"),
        ("casse decalage_tache tau=0.5 beta=0.3", 0.5, 0.3, "symetrique", False, "decalage_tache"),
        ("casse moyenne tau=0.5 beta=0.3", 0.5, 0.3, "symetrique", False, "moyenne"),
        ("casse fuite plus_hauts tau=0.5 beta=0.3", 0.5, 0.3, "symetrique", False, "plus_hauts"),
        ("casse fuite pas_0_a_4 tau=0.5 beta=1.5 sonde_seule", 0.5, 1.5, "sonde_seule", False, "pas_0_a_4"),
        ("casse fuite pas_0_a_4 tau=0.5 beta=1.5 symetrique", 0.5, 1.5, "symetrique", False, "pas_0_a_4"),
        ("casse par_action tau=4 beta=0.3", 4.0, 0.3, "symetrique", False, "par_action"),
        ("casse plancher_autre_jeu tau=0.5 beta=0.3", 0.5, 0.3, "symetrique", False, "plancher_autre_jeu"),
    ]
    filles = racine.spawn(len(cases))
    choisies = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else range(len(cases))
    for k in choisies:
        (nom, tau, beta, mp, co, ca), ss = cases[k], filles[k]
        case(f"[{k}] " + nom, tau, beta, mp, co, reps, ca, ss)
