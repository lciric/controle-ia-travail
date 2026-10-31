"""Calcul de puissance du préenregistrement E1' (base de ponts datés), brouillon 1.

Données entièrement SYNTHÉTIQUES : aucune donnée réelle, aucune moisson, aucun pont réel n'est lu.
But : donner la taille de base (nombre de ponts validés dans la moitié de décision E2) nécessaire
pour que la règle principale (coefficient beta2 du profil « trou à structure commune », ajusté sur
distance, popularité et attachement préférentiel, borne basse de l'intervalle à 90 % > 0) ait une
puissance >= 0,80 contre une alternative nommée ; et les caractéristiques opératoires de la règle
de rétrodiction inversée et de la bande d'équivalence.

Modèle génératif (toutes valeurs SUPPOSÉ, choisies par l'auteur, écrites ci-dessous) :
- N_NICHES niches par moitié, 3 dates de coupure ; unité = paire de niches non ordonnée × date ;
- quatre prédicteurs standardisés D (distance), P (popularité), PA (attachement préférentiel),
  PI (profil) ; chacun = composante de niche (partagée par les paires qui contiennent la niche)
  + composante persistante de paire + bruit de date, mêmes corrélations R pour chaque composante ;
- issue : logit p = alpha + bD*D + bP*P + bPA*PA + beta2*PI + u_i + u_j, u ~ N(0, SIGMA_U²) ;
- plan cas-témoins : M cas tirés parmi les ponts, K témoins par cas tirés parmi les non-ponts de
  la même date ; régression logistique (Newton) avec indicatrices de date ;
- erreur type robuste à deux voies par niche (appartenance multiple, intersection = paire),
  correction G/(G-1) ;
- rétrodiction inversée : même population de prédicteurs, issue passée indépendante avec
  beta2_retro ; même plan, même taille M ;
- gain d'aire (aire sous la courbe) en validation croisée à 5 plis par paire : modèle complet
  (avec PI) contre modèle des témoins (sans PI).

Graines : numpy.random.SeedSequence (numpy >= 1.25), racine RACINE ci-dessous, un enfant par
tâche (clé de tâche écrite), sortie reproductible au bit près pour une même version de numpy.
Usage : python3 -I calcul-puissance-E1-base-de-ponts-v1-brouillon1.py
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import numpy as np  # noqa: E402

RACINE = 20261031105700  # date et heure du mot de Lazar (31 octobre 2026, 10:57 UTC), choisie avant tout tirage
Z95 = 1.6448536269514722  # quantile 0,95 : borne basse unilatérale à 95 % = intervalle bilatéral à 90 %

# ---- paramètres SUPPOSÉ ------------------------------------------------------------------
N_NICHES = 150            # niches par moitié (300 revues tirées, coupées en deux moitiés)
N_DATES = 3               # dates de coupure par moitié
K = 5                     # témoins par cas
P0 = 0.04                 # taux de base par paire × date (grille principale ; disponibilité à part)
SIGMA_U = 0.4             # propension de niche (écart type sur l'échelle logit)
NOMS = ("D", "P", "PA", "PI")
R = np.array([[1.0, -0.1, -0.1, -0.5],
              [-0.1, 1.0, 0.6, 0.2],
              [-0.1, 0.6, 1.0, 0.1],
              [-0.5, 0.2, 0.1, 1.0]])
A2 = np.array([0.3, 0.9, 0.8, 0.4])    # part de variance de niche
B2 = np.array([0.5, 0.05, 0.1, 0.4])   # part de variance persistante de paire
BETA_TEMOINS = np.array([-0.5, 0.4, 0.3])  # log-rapports de cotes par écart type : D, P, PA
OR_GRILLE = (1.0, 1.25, 1.5, 2.0, 3.0)
M_GRILLE = (30, 50, 100, 200, 300, 500, 800)
REPS = 400
REPS_RETRO = 300
M_RETRO = (100, 200, 300, 500)
OR_RETRO = (1.5, 2.0)
DELTA0 = 0.03             # marge de la synthèse (T3-B), échelle de l'aire
LAMBDAS = (0.1, 0.2)      # part de faux ponts parmi les cas (bruit d'étiquette)
M_BRUIT = (200, 300, 500)


def enfant(cle):
    """Enfant de la racine pour une tâche nommée par un tuple d'entiers (R9)."""
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=cle))


IU, JU = np.triu_indices(N_NICHES, 1)
NPAIRES = IU.size
LCHOL = np.linalg.cholesky(R)


def population(rng):
    """Prédicteurs (n_obs × 4), niches i, j, identifiant de paire, date, propensions u."""
    f = rng.standard_normal((N_NICHES, 4)) @ LCHOL.T
    e_pers = rng.standard_normal((NPAIRES, 4)) @ LCHOL.T
    u = SIGMA_U * rng.standard_normal(N_NICHES)
    blocs = []
    for _ in range(N_DATES):
        e_date = rng.standard_normal((NPAIRES, 4)) @ LCHOL.T
        x = (np.sqrt(A2) * (f[IU] + f[JU]) / np.sqrt(2.0)
             + np.sqrt(B2) * e_pers + np.sqrt(1.0 - A2 - B2) * e_date)
        blocs.append(x)
    X = np.vstack(blocs)
    I = np.tile(IU, N_DATES)
    J = np.tile(JU, N_DATES)
    pid = np.tile(np.arange(NPAIRES), N_DATES)
    date = np.repeat(np.arange(N_DATES), NPAIRES)
    return X, I, J, pid, date, u[I] + u[J]


def lin(X, uij, beta2):
    return X[:, :3] @ BETA_TEMOINS + beta2 * X[:, 3] + uij


def alpha_pour(eta, p0):
    lo, hi = -15.0, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if np.mean(1.0 / (1.0 + np.exp(-(mid + eta)))) > p0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def tirer_issue(rng, eta, alpha):
    return rng.random(eta.size) < 1.0 / (1.0 + np.exp(-(alpha + eta)))


def echantillon(rng, y, date, m, lam=0.0):
    """Indices des cas et des témoins ; renvoie (indices, étiquettes, suffisant)."""
    pos = np.flatnonzero(y)
    suffisant = pos.size >= m
    cas = rng.choice(pos, size=min(m, pos.size), replace=False)
    neg_par_date = [np.flatnonzero((~y) & (date == d)) for d in range(N_DATES)]
    nf = int(round(lam * cas.size))
    if nf:
        # faux ponts : des non-ponts étiquetés « pont » par erreur (même date que le cas remplacé)
        faux = np.array([rng.choice(neg_par_date[date[c]]) for c in cas[:nf]])
        cas = np.concatenate([faux, cas[nf:]])
    tem = []
    for d in range(N_DATES):
        nd = int(np.sum(date[cas] == d)) * K
        if nd:
            tem.append(rng.choice(neg_par_date[d], size=nd, replace=False))
    tem = np.concatenate(tem) if tem else np.array([], dtype=int)
    idx = np.concatenate([cas, tem])
    lab = np.concatenate([np.ones(cas.size), np.zeros(tem.size)])
    return idx, lab, suffisant


def plan(X, date, idx, avec_pi=True):
    cols = [np.ones(idx.size)] + [(date[idx] == d).astype(float) for d in range(1, N_DATES)]
    cols += [X[idx, 0], X[idx, 1], X[idx, 2]]
    if avec_pi:
        cols.append(X[idx, 3])
    return np.column_stack(cols)


def logistique(Z, y):
    b = np.zeros(Z.shape[1])
    for _ in range(50):
        eta = Z @ b
        p = 1.0 / (1.0 + np.exp(-eta))
        g = Z.T @ (y - p)
        H = (Z * (p * (1 - p))[:, None]).T @ Z
        pas = np.linalg.solve(H, g)
        b = b + pas
        if np.max(np.abs(pas)) < 1e-10:
            break
    p = 1.0 / (1.0 + np.exp(-(Z @ b)))
    H = (Z * (p * (1 - p))[:, None]).T @ Z
    return b, p, H


def se_deux_voies(Z, y, p, H, I, J, pid):
    Hinv = np.linalg.inv(H)
    G = Z * (y - p)[:, None]
    S = np.zeros((N_NICHES, Z.shape[1]))
    np.add.at(S, I, G)
    np.add.at(S, J, G)
    Sp = np.zeros((NPAIRES, Z.shape[1]))
    np.add.at(Sp, pid, G)
    viande = S.T @ S - Sp.T @ Sp
    V = Hinv @ viande @ Hinv * (N_NICHES / (N_NICHES - 1.0))
    v = V[-1, -1]
    naive = np.sqrt(Hinv[-1, -1])
    return (np.sqrt(v) if v > 0 else naive), naive, v <= 0


def aire(score, y):
    ordre = np.argsort(score, kind="mergesort")
    rangs = np.empty(score.size)
    rangs[ordre] = np.arange(1, score.size + 1)
    n1 = y.sum()
    n0 = y.size - n1
    return (rangs[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def gain_aire_croise(rng, X, date, idx, lab, pid):
    plis = rng.integers(0, 5, size=NPAIRES)[pid[idx]]
    pred_c = np.empty(idx.size)
    pred_b = np.empty(idx.size)
    Zc = plan(X, date, idx, True)
    Zb = Zc[:, :-1]
    for k in range(5):
        a = plis != k
        t = ~a
        bc, _, _ = logistique(Zc[a], lab[a])
        bb, _, _ = logistique(Zb[a], lab[a])
        pred_c[t] = Zc[t] @ bc
        pred_b[t] = Zb[t] @ bb
    return aire(pred_c, lab) - aire(pred_b, lab)


def ajuster(X, date, idx, lab, I, J, pid):
    Z = plan(X, date, idx, True)
    b, p, H = logistique(Z, lab)
    se, naive, repli = se_deux_voies(Z, lab, p, H, I[idx], J[idx], pid[idx])
    return b[-1], se, naive, repli


def f3(x):
    return f"{x:.3f}"


def main():
    print("Calcul de puissance — E1' base de ponts — brouillon 1 (données synthétiques)")
    print(f"numpy {np.__version__} ; racine SeedSequence {RACINE}")
    print(f"N_NICHES={N_NICHES} par moitié, N_DATES={N_DATES}, paires × dates = {NPAIRES * N_DATES}, "
          f"K={K}, P0={P0}, SIGMA_U={SIGMA_U}")
    print("Corrélations R (D, P, PA, PI) :")
    for nom, ligne in zip(NOMS, R):
        print(f"  {nom:>2} " + " ".join(f"{v:+.2f}" for v in ligne))
    print(f"Parts de variance niche {A2.tolist()}, paire {B2.tolist()} ; "
          f"effets des témoins (log-rapport de cotes par écart type) D, P, PA = {BETA_TEMOINS.tolist()}")
    print()

    # ---- § 1. Puissance de la règle principale ---------------------------------------------
    print("§ 1. Règle principale : borne basse unilatérale à 95 % de beta2 > 0 "
          "(intervalle bilatéral à 90 % excluant zéro), erreur type robuste à deux voies par niche.")
    print(f"     {REPS} répétitions par case ; erreur de Monte-Carlo d'une puissance <= 0,025.")
    res = {}
    deff = {}
    replis = 0
    equiv = {}
    bruit = {}
    for io, orv in enumerate(OR_GRILLE):
        beta2 = float(np.log(orv))
        rng_a = enfant((1, io, 0))
        Xa, Ia, Ja, pida, datea, uija = population(rng_a)
        alpha = alpha_pour(lin(Xa, uija, beta2), P0)
        for r in range(REPS):
            rng = enfant((1, io, 1, r))
            X, I, J, pid, date, uij = population(rng)
            y = tirer_issue(rng, lin(X, uij, beta2), alpha)
            for im, m in enumerate(M_GRILLE):
                idx, lab, suff = echantillon(rng, y, date, m)
                b, se, naive, rep = ajuster(X, date, idx, lab, I, J, pid)
                replis += rep
                cle = (orv, m)
                res.setdefault(cle, []).append((b - Z95 * se > 0, suff))
                deff.setdefault(cle, []).append(se / naive)
                if orv == 1.0:
                    for marge in (np.log(1.25), np.log(1.5)):
                        equiv.setdefault((m, round(float(marge), 4)), []).append(
                            (b - Z95 * se > -marge) and (b + Z95 * se < marge))
                if orv in (1.5, 2.0) and m in M_BRUIT:
                    for lam in LAMBDAS:
                        idx2, lab2, _ = echantillon(rng, y, date, m, lam)
                        b2, se2, _, rep2 = ajuster(X, date, idx2, lab2, I, J, pid)
                        replis += rep2
                        bruit.setdefault((orv, m, lam), []).append(b2 - Z95 * se2 > 0)
    entete = "  rapport de cotes \\ M " + "".join(f"{m:>7}" for m in M_GRILLE)
    print(entete)
    for orv in OR_GRILLE:
        ligne = f"  {orv:>20.2f} " + "".join(f"{np.mean([a for a, _ in res[(orv, m)]]):>7.3f}" for m in M_GRILLE)
        print(ligne)
    print("  (ligne 1,00 = taux de fausse alarme de la règle ; attendu <= 0,05 si l'erreur type est juste)")
    print("  Part des répétitions où la population offrait au moins M ponts (P0 = 0,04) :")
    print("  " + " " * 21 + "".join(f"{np.mean([s for _, s in res[(1.5, m)]]):>7.3f}" for m in M_GRILLE))
    print("  Rapport moyen erreur type robuste / erreur type naïve (rapport de cotes 1,5) :")
    print("  " + " " * 21 + "".join(f"{np.mean(deff[(1.5, m)]):>7.3f}" for m in M_GRILLE))
    print(f"  Replis sur l'erreur type naïve (variance robuste non positive) : {replis}")
    print()

    print("§ 2. M minimal pour une puissance >= 0,80 (premier M de la grille qui l'atteint) :")
    for orv in OR_GRILLE[1:]:
        ok = [m for m in M_GRILLE if np.mean([a for a, _ in res[(orv, m)]]) >= 0.80]
        print(f"  rapport de cotes {orv:.2f} : " + (f"M = {ok[0]}" if ok else "au-delà de 800"))
    print("  Puissance à M = 30 et M = 50 (fourchette 30–50 de l'espèce B) :")
    for orv in OR_GRILLE[1:]:
        print(f"  rapport de cotes {orv:.2f} : M=30 → {f3(np.mean([a for a, _ in res[(orv, 30)]]))} ; "
              f"M=50 → {f3(np.mean([a for a, _ in res[(orv, 50)]]))}")
    print()

    print("§ 3. Équivalence sous beta2 = 0 : probabilité que l'intervalle à 90 % tienne dans ± marge.")
    print("  marge \\ M " + "".join(f"{m:>7}" for m in M_GRILLE))
    for marge, nom in ((round(float(np.log(1.25)), 4), "log 1,25"), (round(float(np.log(1.5)), 4), "log 1,5 ")):
        print(f"  {nom:>9} " + "".join(f"{np.mean(equiv[(m, marge)]):>7.3f}" for m in M_GRILLE))
    print("  (marge log 1,10 non tabulée : inatteignable dans cette grille, demi-largeur > 0,095 à M = 800)")
    print()

    print("§ 4. Bruit d'étiquette : puissance quand une part lambda des cas sont de faux ponts.")
    for orv in (1.5, 2.0):
        for m in M_BRUIT:
            base = np.mean([a for a, _ in res[(orv, m)]])
            txt = " ; ".join(f"lambda={lam:.1f} → {f3(np.mean(bruit[(orv, m, lam)]))}" for lam in LAMBDAS)
            print(f"  rapport de cotes {orv:.2f}, M={m:>3} : sans bruit {f3(base)} ; {txt}")
    print()

    # ---- § 5. Rétrodiction inversée --------------------------------------------------------
    print("§ 5. Rétrodiction inversée : même M de ponts passés, même plan ; trois mondes :")
    print("     anticipation (beta2_retro = 0), moitié (beta2_retro = beta2/2), statique (beta2_retro = beta2).")
    print("     Règles de suspension comparées :")
    print("       Ra : gain d'aire rétro >= gain d'aire prospectif − 0,03 (lettre de la synthèse, δ0 = 0,03) ;")
    print("       Rb : gain d'aire rétro >= gain d'aire prospectif − 0,01 ;")
    print("       Rc : beta2 rétro estimé >= moitié du beta2 prospectif estimé.")
    print("     Confirmation = borne basse de beta2 prospectif > 0 ET pas de suspension (règle Rc).")
    print(f"     {REPS_RETRO} répétitions par case ; gains d'aire en validation croisée à 5 plis par paire.")
    print("  rapport  M   monde        gain+   gain−   P(susp Ra) P(susp Rb) P(susp Rc) P(confirm Rc) P(confirm Ra)")
    for io, orv in enumerate(OR_RETRO):
        beta2 = float(np.log(orv))
        rng_a = enfant((2, io, 0))
        Xa, Ia, Ja, pida, datea, uija = population(rng_a)
        alpha = alpha_pour(lin(Xa, uija, beta2), P0)
        for iw, (monde, fr) in enumerate((("anticipation", 0.0), ("moitie", 0.5), ("statique", 1.0))):
            alpha_r = alpha_pour(lin(Xa, uija, beta2 * fr), P0)
            acc = {m: [] for m in M_RETRO}
            for r in range(REPS_RETRO):
                rng = enfant((2, io, 1 + iw, r))
                X, I, J, pid, date, uij = population(rng)
                yp = tirer_issue(rng, lin(X, uij, beta2), alpha)
                yr = tirer_issue(rng, lin(X, uij, beta2 * fr), alpha_r)
                for m in M_RETRO:
                    idp, labp, _ = echantillon(rng, yp, date, m)
                    idr, labr, _ = echantillon(rng, yr, date, m)
                    bp, sep, _, _ = ajuster(X, date, idp, labp, I, J, pid)
                    br, _, _, _ = ajuster(X, date, idr, labr, I, J, pid)
                    gp = gain_aire_croise(rng, X, date, idp, labp, pid)
                    gr = gain_aire_croise(rng, X, date, idr, labr, pid)
                    acc[m].append((gp, gr, gr >= gp - DELTA0, gr >= gp - 0.01, br >= bp / 2.0,
                                   bp - Z95 * sep > 0))
            for m in M_RETRO:
                a = np.array(acc[m], dtype=float)
                conf_c = np.mean((a[:, 5] == 1) & (a[:, 4] == 0))
                conf_a = np.mean((a[:, 5] == 1) & (a[:, 2] == 0))
                print(f"  {orv:>6.2f} {m:>4} {monde:<12} {a[:, 0].mean():+.4f} {a[:, 1].mean():+.4f}"
                      f" {a[:, 2].mean():>10.3f} {a[:, 3].mean():>10.3f} {a[:, 4].mean():>10.3f}"
                      f" {conf_c:>13.3f} {conf_a:>13.3f}")
    print()

    # ---- § 6. Disponibilité et charge de lecture (arithmétique) ----------------------------
    print("§ 6. Ponts attendus dans une moitié (paires × 3 dates × taux de base), arithmétique :")
    print("  niches/moitié  paires×dates   p=0,005   p=0,01   p=0,02   p=0,04")
    for n in (100, 150, 200):
        npd = n * (n - 1) // 2 * N_DATES
        print(f"  {n:>13} {npd:>13} " + "".join(f"{npd * p:>9.0f}" for p in (0.005, 0.01, 0.02, 0.04)))
    print()
    print("§ 7. Lectures (deux lecteurs) pour une portion de M ponts validés, arithmétique SUPPOSÉ :")
    print("     lectures = 2 × [M / q + K × M × f × c] ; q = précision du filtre de candidats,")
    print("     f = part des témoins qui ont au moins un candidat, c = candidats lus par témoin signalé (plafond 20).")
    print("     M     q     f     c   lectures")
    for m in (100, 200, 300, 500):
        for q, f, c in ((0.4, 0.2, 3), (0.2, 0.3, 5)):
            lec = 2 * (m / q + K * m * f * c)
            print(f"  {m:>4} {q:>5.1f} {f:>5.1f} {c:>5d} {lec:>10.0f}")
    print()
    print("Fin.")


if __name__ == "__main__":
    main()
