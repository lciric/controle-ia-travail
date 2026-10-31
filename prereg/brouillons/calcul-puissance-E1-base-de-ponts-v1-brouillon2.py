"""Calcul de puissance du préenregistrement E1' (base de ponts datés), brouillon 2.

Données entièrement SYNTHÉTIQUES : aucune donnée réelle, aucune moisson, aucun pont réel n'est lu.

Ce qui change par rapport au script du brouillon 1 (contre-lecture `836b8c19…`) :
- § 0 (CE1-01, bloquant) : garde des fenêtres. La fenêtre rétrodite est [t - g - h, t - g) avec
  g = max(w_s) = 5 ; essai sain (w_s = 3 et 5, g = 5) et artefacts (g = 4 avec w_s = 5 ; w_s = 6 ;
  dates de E2 qui recouvrent les années d'événement prospectif de E1) ; le script s'arrête en échec
  si une garde ne refuse pas son artefact.
- § 1 (CE1-05) : valeur critique FIXE, écrite d'avance (C_FIXE = 1,96), éprouvée sous l'hypothèse
  nulle par 2 000 répétitions par configuration, en gardant la dépendance de niche et la
  corrélation du profil avec la distance (aucune permutation).
- § 2 (CE1-15) : puissance à la valeur critique fixe, grille de sensibilité (propension de niche
  sigma_U = 0,4 / 1,2 ; corrélation profil-distance -0,5 / -0,8 ; bruit d'étiquette lié à la distance).
- § 3 (CE1-08) : équivalence sous le nul ET à la borne de la bande (fausse alarme de « réfuté »),
  pour trois bandes.
- § 4 (CE1-02, CE1-08, CE1-11) : règle de rétrodiction à la lettre de la synthèse, « score » lu
  comme l'aire du profil seul (delta0 = 0,03), comparée au gain d'aire et à la règle sur beta2 ;
  caractéristiques opératoires du tableau de lecture ENTIER (ordre du brouillon 2) dans onze mondes,
  dont le nul, la barrière (HR-2), la statique atténuée et des témoins du passé plus forts ou plus faibles.
- § 5 (CE1-07) : disponibilité des ponts et puissance réelle selon le nombre de revues et le taux de base.
- § 6 (CE1-06) : charge de lecture par un modèle par paire (rendement de paire, candidats par paire à
  queue lourde, plafond par paire commun aux cas et aux témoins) ; appels et jetons des lecteurs.
- § 7 (CE1-16) : incertitude du kappa sur un lot d'étalonnage de 100 ou 200 paquets.
- Régression logistique avec drapeau de convergence compté (CE1-20).
- Distance sociale (R-735, décision de Lazar, 31 octobre 2026, 11:51 UTC ; antériorité ASIS&T 2025,
  doi 10.1002/pra2.1298) : cinquième prédicteur SOC (distance dans le réseau de cosignature) ajouté
  au modèle génératif et au modèle ajusté ; le profil doit apporter au-delà de D + P + PA + SOC.
  § 2 rapporte aussi la puissance du modèle sans SOC (coût de l'ajout) ; § 1 et § 2 éprouvent une
  corrélation forte entre profil et distance sociale.

Modèle génératif (toutes valeurs SUPPOSÉ) : comme au brouillon 1 avec un cinquième prédicteur (cinq
prédicteurs standardisés D, P, PA, SOC, PI à composantes de niche, de paire persistante et de date ; issue logistique avec
propension de niche u ~ N(0, sigma_U²) ; plan cas-témoins à K témoins de même date ; erreur type
robuste à deux voies par niche, correction G/(G-1)). Base : 250 niches par moitié, taux de base
P0 = 0,01 par paire et par date.

Graines : numpy.random.SeedSequence (numpy >= 1.25), racine RACINE, un enfant par tâche (clé écrite).
Usage : python3 -I calcul-puissance-E1-base-de-ponts-v1-brouillon2.py   (depuis un dossier vide)
"""
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import sys  # noqa: E402

import numpy as np  # noqa: E402

RACINE = 20261031113500   # relevé `date -u` du rédacteur du brouillon 2 (31 octobre 2026, 11:35 UTC), avant tout tirage
C_FIXE = 1.96             # valeur critique fixe de la règle principale (S4), écrite avant le calcul
Z95 = 1.6448536269514722  # valeur du brouillon 1, pour comparaison seulement

# ---- paramètres SUPPOSÉ ------------------------------------------------------------------
N_DATES = 3
K = 5
N_BASE = 250              # revues par moitié (recommandation S10 du brouillon 2)
P0_BASE = 0.01            # ponts validés par paire et par date (fenêtre de 3 ans)
SIGMA_BASE = 0.4
# ordre des colonnes : D, P, PA, SOC (distance sociale), PI (profil, toujours en dernier)
R_BASE = np.array([[1.0, -0.1, -0.1, 0.4, -0.5],
                   [-0.1, 1.0, 0.6, -0.2, 0.2],
                   [-0.1, 0.6, 1.0, -0.3, 0.1],
                   [0.4, -0.2, -0.3, 1.0, 0.3],
                   [-0.5, 0.2, 0.1, 0.3, 1.0]])
R_FORT = R_BASE.copy()
R_FORT[0, 4] = R_FORT[4, 0] = -0.8          # profil très proche de la distance
R_FORT[3, 4] = R_FORT[4, 3] = 0.0           # (corrélation PI-SOC ramenée à 0 pour garder R définie positive)
R_SOC = R_BASE.copy()
R_SOC[3, 4] = R_SOC[4, 3] = 0.6             # profil très proche de la distance sociale
R_SOC[0, 3] = R_SOC[3, 0] = 0.1             # (corrélation D-SOC ramenée à 0,1 pour garder R définie positive)
A2 = np.array([0.3, 0.9, 0.8, 0.5, 0.4])        # part de variance de niche
B2 = np.array([0.5, 0.05, 0.1, 0.3, 0.4])       # part de variance persistante de paire
BETA_TEMOINS = np.array([-0.5, 0.4, 0.3, -0.3])  # D, P, PA, SOC (log-rapport de cotes par écart type)
NT = BETA_TEMOINS.size
DELTA0 = 0.03                              # marge de la synthèse (T3-B)
M_MIN = 100
BANDES = (("log 1,25", float(np.log(1.25))), ("log 1,33", float(np.log(1.33))), ("log 1,50", float(np.log(1.5))))

REPS_NUL = 2000
REPS_PUIS = 400
REPS_RETRO = 400
REPS_RETRO_HET = 300
REPS_DISPO = 300
NOMS = ("D", "P", "PA", "SOC", "PI")


class GardeFenetres(Exception):
    """Refus d'un jeu de fenêtres qui viole le garde-fou 2 ou le garde-fou 5."""


def enfant(cle):
    """Enfant de la racine pour une tâche nommée par un tuple d'entiers (R9)."""
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=cle))


# ---- § 0. Fenêtres --------------------------------------------------------------------------
def fenetres(t, w_s, g, h=3, w_lab=4, h_nov=6):
    """Fenêtres [début, fin) en années civiles pour une date de coupure t."""
    return {
        "calcul du profil": (t - w_s, t),
        "evenement prospectif": (t, t + h),
        "evenement retrodit": (t - g - h, t - g),
        "termes prospectifs": (t - w_lab, t),
        "termes retrodits": (t - g - h - w_lab, t - g - h),
        "nouveaute prospective": (t - h_nov, t),
        "nouveaute retrodite": (t - g - h - h_nov, t - g - h),
    }


def disjointes(a, b):
    return a[1] <= b[0] or b[1] <= a[0]


def garde_fenetres(dates_e1, dates_e2, variantes_ws, g, h=3, w_lab=4, h_nov=6, debut=1995, fin=2024):
    """Lève GardeFenetres si une fenêtre de calcul recouvre une fenêtre d'événement (GF2), si les
    années d'événement prospectif de E1 et E2 se recouvrent (GF5), ou si une fenêtre sort de la moisson."""
    for t in tuple(dates_e1) + tuple(dates_e2):
        for w_s in variantes_ws:
            f = fenetres(t, w_s, g, h, w_lab, h_nov)
            if not disjointes(f["calcul du profil"], f["evenement retrodit"]):
                raise GardeFenetres(f"GF2 : t={t}, w_s={w_s}, g={g} : calcul {f['calcul du profil']} "
                                    f"recouvre l'événement rétrodit {f['evenement retrodit']}")
            if not disjointes(f["calcul du profil"], f["evenement prospectif"]):
                raise GardeFenetres(f"GF2 : t={t}, w_s={w_s} : calcul recouvre l'événement prospectif")
            if f["termes retrodits"][1] > f["evenement retrodit"][0] or \
               f["nouveaute retrodite"][1] > f["evenement retrodit"][0]:
                raise GardeFenetres(f"t={t} : termes ou nouveauté rétrodits après le début de l'événement")
            bas = min(v[0] for v in f.values())
            haut = max(v[1] for v in f.values())
            if bas < debut or haut > fin:
                raise GardeFenetres(f"t={t}, w_s={w_s} : fenêtre hors de la moisson [{debut}, {fin})")
    ev1 = set()
    for t in dates_e1:
        ev1.update(range(t, t + h))
    ev2 = set()
    for t in dates_e2:
        ev2.update(range(t, t + h))
    if ev1 & ev2:
        raise GardeFenetres(f"GF5 : années d'événement prospectif communes à E1 et E2 : {sorted(ev1 & ev2)}")


def section0():
    print("§ 0. Garde des fenêtres (garde-fou 2, constat CE1-01 ; garde-fou 5).")
    d1, d2, ws, g = (2009, 2011, 2013), (2017, 2019, 2021), (3, 5), 5
    print(f"  Principal : E1 t ∈ {d1}, E2 t ∈ {d2}, w_s ∈ {ws}, décalage rétrodit g = max(w_s) = {g}, "
          f"h = 3, w_lab = 4, historique de nouveauté h_nov = 6 ; moisson [1995, 2024).")
    for t in (2009, 2021):
        f = fenetres(t, 5, g)
        print(f"  t = {t}, w_s = 5 : " + " ; ".join(f"{k} [{a}, {b})" for k, (a, b) in f.items()))
    echecs = 0
    try:
        garde_fenetres(d1, d2, ws, g)
        print("  sain (w_s = 3 et 5, g = 5) : accepté (attendu)")
    except GardeFenetres as e:
        echecs += 1
        print(f"  sain : REFUSÉ, ÉCHEC DE LA GARDE ({e})")
    artefacts = (
        ("g = 4 avec w_s = 5 (brouillon 1)", d1, d2, ws, 4),
        ("w_s = 6 avec g = 5", d1, d2, (3, 6), 5),
        ("E2 t = 2015 (recouvre E1 2013-2015)", d1, (2015, 2019, 2021), ws, 5),
        ("E1 t = 2007 avec g = 5 (moisson avant 1995)", (2007, 2011, 2013), d2, ws, 5),
    )
    for nom, a1, a2, w, gg in artefacts:
        try:
            garde_fenetres(a1, a2, w, gg)
            echecs += 1
            print(f"  artefact {nom} : ACCEPTÉ, ÉCHEC DE LA GARDE")
        except GardeFenetres as e:
            print(f"  artefact {nom} : refusé (attendu) — {e}")
    print()
    return echecs


# ---- modèle synthétique ---------------------------------------------------------------------
_TRIU = {}


def triu(n):
    if n not in _TRIU:
        _TRIU[n] = np.triu_indices(n, 1)
    return _TRIU[n]


class Pop:
    __slots__ = ("X", "I", "J", "pid", "date", "uij", "n", "npaires")


def population(rng, n, sigma_u, lchol):
    iu, ju = triu(n)
    npaires = iu.size
    f = rng.standard_normal((n, NT + 1)) @ lchol.T
    e_pers = rng.standard_normal((npaires, NT + 1)) @ lchol.T
    u = sigma_u * rng.standard_normal(n)
    blocs = []
    for _ in range(N_DATES):
        e_date = rng.standard_normal((npaires, NT + 1)) @ lchol.T
        blocs.append(np.sqrt(A2) * (f[iu] + f[ju]) / np.sqrt(2.0)
                     + np.sqrt(B2) * e_pers + np.sqrt(1.0 - A2 - B2) * e_date)
    p = Pop()
    p.X = np.vstack(blocs)
    p.I = np.tile(iu, N_DATES)
    p.J = np.tile(ju, N_DATES)
    p.pid = np.tile(np.arange(npaires), N_DATES)
    p.date = np.repeat(np.arange(N_DATES), npaires)
    p.uij = u[p.I] + u[p.J]
    p.n = n
    p.npaires = npaires
    return p


def lin(pop, beta2, echelle=1.0):
    return pop.X[:, :NT] @ (BETA_TEMOINS * echelle) + beta2 * pop.X[:, NT] + pop.uij


def alpha_pour(eta, p0):
    lo, hi = -20.0, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if np.mean(1.0 / (1.0 + np.exp(-(mid + eta)))) > p0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def tirer_issue(rng, eta, alpha):
    return rng.random(eta.size) < 1.0 / (1.0 + np.exp(-(alpha + eta)))


def echantillon(rng, y, date, m, lam=0.0, poids=None):
    """Cas (au plus m ponts, tous si la population en offre moins) et K témoins de même date."""
    pos = np.flatnonzero(y)
    m_eff = min(m, pos.size)
    cas = rng.choice(pos, size=m_eff, replace=False)
    neg_par_date = [np.flatnonzero((~y) & (date == d)) for d in range(N_DATES)]
    nf = int(round(lam * m_eff))
    if nf:
        faux = []
        for c in cas[:nf]:
            cand = neg_par_date[date[c]]
            if poids is None:
                faux.append(rng.choice(cand))
            else:
                w = poids[cand]
                faux.append(rng.choice(cand, p=w / w.sum()))
        cas = np.concatenate([np.array(faux), cas[nf:]])
    tem = []
    for d in range(N_DATES):
        nd = int(np.sum(date[cas] == d)) * K
        if nd:
            tem.append(rng.choice(neg_par_date[d], size=nd, replace=False))
    tem = np.concatenate(tem) if tem else np.array([], dtype=int)
    idx = np.concatenate([cas, tem])
    lab = np.concatenate([np.ones(cas.size), np.zeros(tem.size)])
    return idx, lab, m_eff


def plan(pop, idx, avec_pi=True, temoins=tuple(range(NT))):
    cols = [np.ones(idx.size)] + [(pop.date[idx] == d).astype(float) for d in range(1, N_DATES)]
    cols += [pop.X[idx, k] for k in temoins]
    if avec_pi:
        cols.append(pop.X[idx, NT])
    return np.column_stack(cols)


COMPTE = {"non_convergence": 0, "repli_erreur_type": 0, "ajustements": 0}


def logistique(Z, y):
    b = np.zeros(Z.shape[1])
    ok = False
    for _ in range(60):
        p = 1.0 / (1.0 + np.exp(-(Z @ b)))
        g = Z.T @ (y - p)
        H = (Z * (p * (1 - p))[:, None]).T @ Z
        pas = np.linalg.solve(H, g)
        b = b + pas
        if np.max(np.abs(pas)) < 1e-9:
            ok = True
            break
    p = 1.0 / (1.0 + np.exp(-(Z @ b)))
    H = (Z * (p * (1 - p))[:, None]).T @ Z
    ok = ok and bool(np.all(np.isfinite(b)))
    return b, p, H, ok


def se_deux_voies(Z, y, p, H, I, J, pid, n, npaires):
    Hinv = np.linalg.inv(H)
    G = Z * (y - p)[:, None]
    S = np.zeros((n, Z.shape[1]))
    np.add.at(S, I, G)
    np.add.at(S, J, G)
    Sp = np.zeros((npaires, Z.shape[1]))
    np.add.at(Sp, pid, G)
    viande = S.T @ S - Sp.T @ Sp
    V = Hinv @ viande @ Hinv * (n / (n - 1.0))
    v = V[-1, -1]
    naive = np.sqrt(Hinv[-1, -1])
    return (np.sqrt(v) if v > 0 else naive), naive, v <= 0


def ajuster(pop, idx, lab, temoins=tuple(range(NT))):
    Z = plan(pop, idx, True, temoins)
    b, p, H, ok = logistique(Z, lab)
    se, naive, repli = se_deux_voies(Z, lab, p, H, pop.I[idx], pop.J[idx], pop.pid[idx], pop.n, pop.npaires)
    COMPTE["ajustements"] += 1
    COMPTE["non_convergence"] += (not ok)
    COMPTE["repli_erreur_type"] += bool(repli)
    return b[-1], se


def aire(score, y):
    ordre = np.argsort(score, kind="mergesort")
    rangs = np.empty(score.size)
    rangs[ordre] = np.arange(1, score.size + 1)
    n1 = y.sum()
    n0 = y.size - n1
    return (rangs[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def gain_aire_croise(rng, pop, idx, lab):
    plis = rng.integers(0, 5, size=pop.npaires)[pop.pid[idx]]
    pred_c = np.empty(idx.size)
    pred_b = np.empty(idx.size)
    Zc = plan(pop, idx, True)
    Zb = Zc[:, :-1]
    for k in range(5):
        a = plis != k
        t = ~a
        bc = logistique(Zc[a], lab[a])[0]
        bb = logistique(Zb[a], lab[a])[0]
        pred_c[t] = Zc[t] @ bc
        pred_b[t] = Zb[t] @ bb
    return aire(pred_c, lab) - aire(pred_b, lab)


def f3(x):
    return f"{x:.3f}"


def moyenne(v):
    return float(np.mean(v)) if len(v) else float("nan")


# ---- § 1. Valeur critique fixe sous l'hypothèse nulle ---------------------------------------
CONFIGS_NUL = (("base : sigma_U 0,4, corr(PI, D) -0,5, corr(PI, SOC) +0,3", SIGMA_BASE, R_BASE),
               ("niches hétérogènes : sigma_U 1,2", 1.2, R_BASE),
               ("profil proche de la distance : corr(PI, D) -0,8, corr(PI, SOC) 0", SIGMA_BASE, R_FORT),
               ("profil proche de la distance sociale : corr(PI, SOC) +0,6, corr(D, SOC) +0,1", SIGMA_BASE, R_SOC))
M_NUL = (100, 200, 300)


def section1():
    print("§ 1. Règle principale sous l'hypothèse nulle (beta2 = 0) : fausse alarme selon la valeur critique.")
    print(f"     {REPS_NUL} répétitions par configuration ; {N_BASE} niches par moitié ; P0 = {P0_BASE} ; "
          "erreur de Monte-Carlo d'un taux de 0,05 : ± 0,005 (un écart type).")
    stock = {}
    for ic, (nom, sig, r) in enumerate(CONFIGS_NUL):
        lch = np.linalg.cholesky(r)
        pa = population(enfant((1, ic, 0)), N_BASE, sig, lch)
        alpha = alpha_pour(lin(pa, 0.0), P0_BASE)
        zs = {m: [] for m in M_NUL}
        for rep in range(REPS_NUL):
            rng = enfant((1, ic, 1, rep))
            pop = population(rng, N_BASE, sig, lch)
            y = tirer_issue(rng, lin(pop, 0.0), alpha)
            for m in M_NUL:
                idx, lab, _ = echantillon(rng, y, pop.date, m)
                b, se = ajuster(pop, idx, lab)
                zs[m].append((b, se))
        stock[ic] = zs
        print(f"  {nom}")
        print("     M   P(z>1,645)  P(z>1,96)  P(z>2,20)  quantile 0,95 de z  quantile 0,975 de z  P(|z|>1,96)")
        for m in M_NUL:
            a = np.array(zs[m])
            z = a[:, 0] / a[:, 1]
            print(f"   {m:>4}   {np.mean(z > Z95):>9.3f}  {np.mean(z > 1.96):>9.3f}  {np.mean(z > 2.2):>9.3f}"
                  f"  {np.quantile(z, 0.95):>18.3f}  {np.quantile(z, 0.975):>19.3f}  {np.mean(np.abs(z) > 1.96):>11.3f}")
    print(f"  Règle retenue : borne basse beta2 - {C_FIXE} × erreur type > 0 (valeur critique fixe, sans étalonnage sur données).")
    print()
    return stock


# ---- § 2. Puissance à la valeur critique fixe ----------------------------------------------
OR_PUIS = (1.25, 1.33, 1.5, 2.0)
M_PUIS = (100, 150, 200, 300, 400)


def section2():
    print(f"§ 2. Puissance de la règle principale à la valeur critique fixe {C_FIXE} "
          f"({REPS_PUIS} répétitions par case ; erreur de Monte-Carlo <= 0,025).")
    stock = {}
    configs = (("base (sigma_U 0,4, corr(PI, D) -0,5, corr(PI, SOC) +0,3)", SIGMA_BASE, R_BASE, OR_PUIS),
               ("sigma_U 1,2", 1.2, R_BASE, OR_PUIS),
               ("corr(PI, D) -0,8", SIGMA_BASE, R_FORT, (1.5,)),
               ("corr(PI, SOC) +0,6", SIGMA_BASE, R_SOC, (1.5,)))
    bruit = {}
    sans_soc = {}
    for ic, (nom, sig, r, ors) in enumerate(configs):
        lch = np.linalg.cholesky(r)
        print(f"  {nom}")
        print("     rapport de cotes \\ M " + "".join(f"{m:>7}" for m in M_PUIS))
        for io, orv in enumerate(ors):
            beta2 = float(np.log(orv))
            pa = population(enfant((2, ic, io, 0)), N_BASE, sig, lch)
            alpha = alpha_pour(lin(pa, beta2), P0_BASE)
            acc = {m: [] for m in M_PUIS}
            for rep in range(REPS_PUIS):
                rng = enfant((2, ic, io, 1, rep))
                pop = population(rng, N_BASE, sig, lch)
                y = tirer_issue(rng, lin(pop, beta2), alpha)
                for m in M_PUIS:
                    idx, lab, _ = echantillon(rng, y, pop.date, m)
                    acc[m].append(ajuster(pop, idx, lab))
                if ic in (0, 3) and orv in (1.25, 1.5):
                    for m in (200, 300):
                        idx, lab, _ = echantillon(rng, y, pop.date, m)
                        b, se = ajuster(pop, idx, lab, (0, 1, 2))
                        sans_soc.setdefault((ic, orv, m), []).append(b - C_FIXE * se > 0)
                if ic == 0 and orv == 1.5:
                    for m in (200, 300):
                        for nb, poids in (("non différentiel", None), ("lié à la distance", np.exp(0.7 * pop.X[:, 0]))):
                            idx, lab, _ = echantillon(rng, y, pop.date, m, 0.2, poids)
                            b, se = ajuster(pop, idx, lab)
                            bruit.setdefault((m, nb), []).append(b - C_FIXE * se > 0)
            stock[(ic, orv)] = acc
            print(f"     {orv:>20.2f} " + "".join(
                f"{np.mean([b - C_FIXE * s > 0 for b, s in acc[m]]):>7.3f}" for m in M_PUIS))
    print("  Bruit d'étiquette, 20 % de faux ponts (base, rapport de cotes 1,5) :")
    for m in (200, 300):
        base = np.mean([b - C_FIXE * s > 0 for b, s in stock[(0, 1.5)][m]])
        txt = " ; ".join(f"{nb} → {f3(np.mean(bruit[(m, nb)]))}" for nb in ("non différentiel", "lié à la distance"))
        print(f"     M = {m} : sans bruit {f3(base)} ; {txt}")
    print("  (« lié à la distance » : faux ponts tirés avec un poids exp(0,7 × D), plus souvent parmi les paires lointaines.)")
    print("  Effet de l'ajout de la distance sociale (R-735) : puissance du modèle sans SOC (D, P, PA seulement) sur un")
    print("  échantillon cas-témoins frais de la même population (« avec SOC » = tableau ci-dessus). Dans ce modèle")
    print("  génératif, SOC a un effet propre (-0,3) et corr(PI, SOC) > 0 : l'omettre biaise beta2 vers le bas.")
    for ic, nom in ((0, "base"), (3, "corr(PI, SOC) +0,6")):
        for orv in ((1.25, 1.5) if ic == 0 else (1.5,)):
            for m in (200, 300):
                avec = np.mean([b - C_FIXE * s > 0 for b, s in stock[(ic, orv)][m]])
                print(f"     {nom:<20} RC {orv:.2f}, M = {m} : avec SOC {f3(avec)} ; sans SOC {f3(np.mean(sans_soc[(ic, orv, m)]))}")
    print()
    return stock


# ---- § 3. Équivalence ----------------------------------------------------------------------
def section3(nul, puis):
    print(f"§ 3. Équivalence (« réfuté ») : intervalle beta2 ± {C_FIXE} × erreur type contenu dans ± bande.")
    print("     Sous le nul (souhaité grand) et à la borne de la bande (fausse alarme de « réfuté », souhaitée petite).")
    print("     bande      M   P(équiv | nul)  P(équiv | RC = borne)  P(équiv | RC = 1,25)  P(équiv | RC = 1,33)")
    for nom, marge in BANDES:
        borne = round(float(np.exp(marge)), 2)
        for m in (100, 200, 300):
            a0 = np.array(nul[0][m])
            pe0 = np.mean((a0[:, 0] - C_FIXE * a0[:, 1] > -marge) & (a0[:, 0] + C_FIXE * a0[:, 1] < marge))

            def peq(orv):
                a = np.array(puis[(0, orv)][m])
                return np.mean((a[:, 0] - C_FIXE * a[:, 1] > -marge) & (a[:, 0] + C_FIXE * a[:, 1] < marge))
            cle_borne = {1.25: 1.25, 1.33: 1.33, 1.5: 1.5}[borne]
            print(f"     {nom}  {m:>4}  {pe0:>14.3f}  {peq(cle_borne):>21.3f}  {peq(1.25):>20.3f}  {peq(1.33):>20.3f}")
    print("  (sous le nul : 2 000 répétitions ; à la borne : 400 ; configuration de base.)")
    print()


# ---- § 4. Rétrodiction et tableau de lecture entier ----------------------------------------
MONDES = (
    # nom, rapport de cotes prospectif, rapport de cotes rétrodit, échelle des témoins du passé, gain d'aire calculé
    ("nul (beta+ = beta- = 0)", 1.0, 1.0, 1.0, True),
    ("barrière HR-2 (RC 1/1,5 partout)", 1 / 1.5, 1 / 1.5, 1.0, False),
    ("anticipation RC 1,25", 1.25, 1.0, 1.0, False),
    ("anticipation RC 1,5", 1.5, 1.0, 1.0, True),
    ("anticipation RC 2,0", 2.0, 1.0, 1.0, False),
    ("moitié RC 1,5 (beta- = beta+/2)", 1.5, 1.5 ** 0.5, 1.0, False),
    ("statique atténuée 0,6 (RC 1,5)", 1.5, 1.5 ** 0.6, 1.0, False),
    ("statique atténuée 0,8 (RC 1,5)", 1.5, 1.5 ** 0.8, 1.0, False),
    ("statique RC 1,5 (beta- = beta+)", 1.5, 1.5, 1.0, True),
    ("statique RC 1,5, témoins du passé × 0,7", 1.5, 1.5, 0.7, False),
    ("anticipation RC 1,5, témoins du passé × 1,3", 1.5, 1.0, 1.3, False),
)
M_RETRO = (100, 200, 300)
VERDICTS = ("réfuté", "réf. inverse", "suspendu", "non réfuté", "non concl.")


def verdict(bp, sep, auc_p, auc_r, marge):
    """Tableau de lecture du brouillon 2, lignes 2 à 6, dans l'ordre (les lignes 0 et 1 ne sont pas simulées)."""
    lo, hi = bp - C_FIXE * sep, bp + C_FIXE * sep
    if lo > -marge and hi < marge:
        return 0                                   # ligne 2 : équivalence → réfuté
    if hi < 0:
        return 1                                   # ligne 3 : signe inverse
    if lo > 0:
        return 2 if auc_r >= auc_p - DELTA0 else 3  # ligne 4 : suspendu ; ligne 5 : non réfuté
    return 4                                       # ligne 6 : non concluant (puissance)


def bloc_retro(cle, mondes, sig, reps):
    lch = np.linalg.cholesky(R_BASE)
    res = {}
    for iw, (nom, orp, orr, ech, avec_gain) in enumerate(mondes):
        bp_, br_ = float(np.log(orp)), float(np.log(orr))
        pa = population(enfant((4, cle, iw, 0)), N_BASE, sig, lch)
        alpha_p = alpha_pour(lin(pa, bp_), P0_BASE)
        alpha_r = alpha_pour(lin(pa, br_, ech), P0_BASE)
        acc = {m: [] for m in M_RETRO}
        for rep in range(reps):
            rng = enfant((4, cle, iw, 1, rep))
            pop = population(rng, N_BASE, sig, lch)
            yp = tirer_issue(rng, lin(pop, bp_), alpha_p)
            yr = tirer_issue(rng, lin(pop, br_, ech), alpha_r)
            for m in M_RETRO:
                idp, labp, _ = echantillon(rng, yp, pop.date, m)
                idr, labr, _ = echantillon(rng, yr, pop.date, m)
                b1, s1 = ajuster(pop, idp, labp)
                b2, s2 = ajuster(pop, idr, labr)
                ap = aire(pop.X[idp, NT], labp)
                ar = aire(pop.X[idr, NT], labr)
                gp = gr = float("nan")
                if avec_gain and m == 200:
                    gp = gain_aire_croise(rng, pop, idp, labp)
                    gr = gain_aire_croise(rng, pop, idr, labr)
                acc[m].append((b1, s1, b2, s2, ap, ar, gp, gr))
        res[iw] = {m: np.array(acc[m]) for m in M_RETRO}
    return res


def imprimer_retro(res, mondes, m):
    print(f"  M = {m} ponts par portion (prospective et rétrodite) :")
    print("     monde                                        aire+   aire-  susp(a)  susp(a,0,01) susp(c)  susp(a')")
    for iw, (nom, *_r) in enumerate(mondes):
        a = res[iw][m]
        sa = np.mean(a[:, 5] >= a[:, 4] - DELTA0)
        sa1 = np.mean(a[:, 5] >= a[:, 4] - 0.01)
        sc = np.mean((a[:, 2] >= a[:, 0] / 2.0) & (a[:, 0] > 0))
        sg = np.mean(a[:, 7] >= a[:, 6] - DELTA0) if np.all(np.isfinite(a[:, 6])) else float("nan")
        sg_txt = f"{sg:>9.3f}" if np.isfinite(sg) else "        —"
        print(f"     {nom:<44} {a[:, 4].mean():.3f}  {a[:, 5].mean():.3f}  {sa:>7.3f}  {sa1:>12.3f}  {sc:>7.3f}{sg_txt}")


def imprimer_verdicts(res, mondes, m, nom_bande, marge):
    print(f"  Distribution des verdicts, M = {m}, bande {nom_bande}, règle de rétrodiction (a) :")
    print("     monde                                        " + "".join(f"{v:>13}" for v in VERDICTS))
    for iw, (nom, *_r) in enumerate(mondes):
        a = res[iw][m]
        v = np.array([verdict(row[0], row[1], row[4], row[5], marge) for row in a])
        print(f"     {nom:<44} " + "".join(f"{np.mean(v == k):>13.3f}" for k in range(5)))


def section4():
    print("§ 4. Rétrodiction inversée et tableau de lecture entier (constats CE1-02, CE1-08, CE1-11).")
    print("     Règles de suspension (toutes rapportées) :")
    print("       (a)  lettre de la synthèse, « score » = aire du profil seul : aire- >= aire+ - 0,03 ;")
    print("       (a,0,01) même règle, delta0 = 0,01 ;")
    print("       (c)  beta2- estimé >= beta2+/2 et beta2+ > 0 (règle du brouillon 1) ;")
    print("       (a') gain d'aire en validation croisée : gain- >= gain+ - 0,03 (lecture du brouillon 1 ; M = 200, trois mondes).")
    print(f"     {REPS_RETRO} répétitions par monde ; {N_BASE} niches ; sigma_U {SIGMA_BASE} ; les colonnes susp sont "
          "inconditionnelles (sans exiger beta2+ significatif).")
    res = bloc_retro(0, MONDES, SIGMA_BASE, REPS_RETRO)
    for m in M_RETRO:
        imprimer_retro(res, MONDES, m)
    print()
    for nom_b, marge in BANDES:
        for m in M_RETRO:
            imprimer_verdicts(res, MONDES, m, nom_b, marge)
        print()
    print(f"  Niches hétérogènes (sigma_U 1,2), {REPS_RETRO_HET} répétitions, trois mondes :")
    mondes_het = (MONDES[0], MONDES[3], MONDES[8])
    res_h = bloc_retro(1, mondes_het, 1.2, REPS_RETRO_HET)
    for m in (200, 300):
        imprimer_retro(res_h, mondes_het, m)
        imprimer_verdicts(res_h, mondes_het, m, "log 1,33", float(np.log(1.33)))
    print()


# ---- § 5. Disponibilité et puissance réelle ------------------------------------------------
def section5():
    print("§ 5. Disponibilité des ponts et puissance réelle (rapport de cotes 1,5, quota visé 200, "
          f"M_min {M_MIN}, valeur critique {C_FIXE}, {REPS_DISPO} répétitions).")
    print("     Ponts attendus par portion = paires × 3 dates × P0 (arithmétique) :")
    print("     revues/moitié  paires×dates  P0=0,0025  P0=0,005  P0=0,01  P0=0,02")
    for n in (150, 250, 300, 350):
        npd = n * (n - 1) // 2 * N_DATES
        print(f"     {n:>13} {npd:>13} " + "".join(f"{npd * p:>10.0f}" for p in (0.0025, 0.005, 0.01, 0.02)))
    print("     Simulation (M effectif = min(200, ponts disponibles)) :")
    print("     revues/moitié     P0   M eff. moyen  P(M>=200)  P(M<100 : non concl. base)  P(confirmé)")
    lch = np.linalg.cholesky(R_BASE)
    beta2 = float(np.log(1.5))
    for ii, n in enumerate((150, 250, 300)):
        for ip, p0 in enumerate((0.0025, 0.005, 0.01)):
            pa = population(enfant((5, ii, ip, 0)), n, SIGMA_BASE, lch)
            alpha = alpha_pour(lin(pa, beta2), p0)
            meff, conf = [], []
            for rep in range(REPS_DISPO):
                rng = enfant((5, ii, ip, 1, rep))
                pop = population(rng, n, SIGMA_BASE, lch)
                y = tirer_issue(rng, lin(pop, beta2), alpha)
                idx, lab, me = echantillon(rng, y, pop.date, 200)
                meff.append(me)
                if me < M_MIN:
                    conf.append(False)
                    continue
                b, se = ajuster(pop, idx, lab)
                conf.append(b - C_FIXE * se > 0)
            meff = np.array(meff)
            print(f"     {n:>13} {p0:>6.4f} {meff.mean():>14.1f} {np.mean(meff >= 200):>10.3f}"
                  f" {np.mean(meff < M_MIN):>28.3f} {np.mean(conf):>12.3f}")
    print()


# ---- § 6. Charge de lecture ----------------------------------------------------------------
def candidats(rng, n, mu, disp=0.5):
    """Candidats par paire signalée : 1 + binomiale négative de moyenne mu - 1 (queue lourde)."""
    pr = disp / (disp + (mu - 1.0))
    return 1 + rng.negative_binomial(disp, pr, size=n)


def lire_paires(rng, n, r, mu, cap, pi_vrai=0.3, pi_faux=0.01):
    """Pour n paires signalées : (validée, paquets lus). Lecture des candidats (au plus cap, tirés au
    hasard puis en ordre chronologique) jusqu'au premier « oui-oui »."""
    nc = np.minimum(candidats(rng, n, mu), cap)
    vrai = rng.random(n) < r
    pi = np.where(vrai, pi_vrai, pi_faux)
    premier = rng.geometric(pi)
    valide = premier <= nc
    lus = np.where(valide, premier, nc)
    return valide, lus


def charge_portion(rng, m, r, mu, cap, s):
    lus_cas = 0
    trouves = 0
    paires = 0
    while trouves < m:
        v, lus = lire_paires(rng, 20000, r, mu, cap)
        cum = np.cumsum(v)
        if cum[-1] + trouves >= m:
            k = int(np.searchsorted(cum, m - trouves)) + 1
            lus_cas += int(lus[:k].sum())
            paires += k
            trouves = m
        else:
            lus_cas += int(lus.sum())
            paires += v.size
            trouves += int(cum[-1])
    besoin = K * m
    lus_tem = 0
    temoins = 0
    while temoins < besoin:
        nb = besoin - temoins
        signale = rng.random(nb) < s
        v, lus = lire_paires(rng, int(signale.sum()), r, mu, cap)
        lus_tem += int(lus.sum())
        temoins += nb - int(v.sum())
    return lus_cas, lus_tem, paires


def section6():
    print("§ 6. Charge de lecture (modèle par paire, SUPPOSÉ) pour les trois portions (200 + 200 + 100 ponts).")
    print("     r = part des paires signalées qui portent une vraie reprise ; mu = candidats moyens par paire signalée")
    print("     (1 + binomiale négative, dispersion 0,5) ; plafond commun aux cas et aux témoins ; s = part des paires")
    print("     à risque signalées ; validation d'un candidat : 0,3 si vraie reprise, 0,01 sinon.")
    print("     rho = rendement d'une paire signalée ; P0 implicite = s × rho ; ponts disponibles = 93 375 × P0 (250 revues).")
    print("     Paquets = lus par chaque lecteur ; lectures = 2 × paquets ; appels = lectures / 50 (lots de 50).")
    print("       r    mu  plafond    s    rho   P0 impl.  ponts dispo.  paquets cas  paquets tém.  lectures   appels")
    grille = [(r, mu, 10, s) for r in (0.03, 0.10, 0.25) for mu in (3, 8) for s in (0.2, 0.5)]
    grille += [(0.03, 8, 20, 0.5), (0.10, 8, 20, 0.5)]
    totaux = []
    for ig, (r, mu, cap, s) in enumerate(grille):
        rng = enfant((6, ig))
        v, _ = lire_paires(rng, 200000, r, mu, cap)
        rho = v.mean()
        p0 = s * rho
        lc = lt = 0
        for m in (200, 200, 100):
            a, b, _ = charge_portion(rng, m, r, mu, cap, s)
            lc += a
            lt += b
        lec = 2 * (lc + lt)
        totaux.append(lec)
        print(f"     {r:>4.2f} {mu:>4d} {cap:>8d} {s:>5.1f} {rho:>6.3f} {p0:>9.4f} {93375 * p0:>13.0f}"
              f" {lc:>12d} {lt:>13d} {lec:>9d} {lec // 50:>8d}")
    print("     Fixes : étalonnage 2 × 200 lectures (et 2 × 200 si révision) ; audit tiers 60 ; test de masquage 2 × 30 ;")
    print("     exclusion des revues pluridisciplinaires 2 × (500 + 200 de liste d'attente) noms.")
    print(f"     Fourchette des lectures de base : {min(totaux)} à {max(totaux)} (hors fixes, environ 2 300).")
    print()


# ---- § 7. Kappa ----------------------------------------------------------------------------
def kappa_tab(n11, n10, n01, n00):
    n = n11 + n10 + n01 + n00
    po = (n11 + n00) / n
    pa = (n11 + n10) / n
    pb = (n11 + n01) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe)


def section7():
    print("§ 7. Kappa (oui contre autre) sur le lot d'étalonnage : 10 000 tirages, prévalence de « oui » 0,3.")
    print("     kappa vrai   n   écart type de kappa estimé   P(kappa estimé < 0,60)")
    rng = enfant((7,))
    for kv in (0.50, 0.55, 0.65, 0.70):
        p = 0.3
        p11 = p * p + kv * p * (1 - p)
        p10 = p - p11
        probs = np.array([p11, p10, p10, 1 - p11 - 2 * p10])
        for n in (100, 200):
            t = rng.multinomial(n, probs, size=10000)
            k = kappa_tab(t[:, 0], t[:, 1], t[:, 2], t[:, 3])
            print(f"     {kv:>10.2f} {n:>4}   {np.std(k):>26.3f}   {np.mean(k < 0.60):>21.3f}")
    print()


def main():
    print("Calcul de puissance — E1' base de ponts — brouillon 2 (données synthétiques)")
    print(f"numpy {np.__version__} ; racine SeedSequence {RACINE} ; valeur critique fixe {C_FIXE}")
    print(f"Base : {N_BASE} niches par moitié, {N_DATES} dates, paires × dates = {triu(N_BASE)[0].size * N_DATES}, "
          f"K = {K}, P0 = {P0_BASE}, sigma_U = {SIGMA_BASE}, delta0 = {DELTA0}, M_min = {M_MIN}")
    print("Corrélations R (D, P, PA, SOC, PI) de base :")
    for nom, ligne in zip(NOMS, R_BASE):
        print(f"  {nom:>2} " + " ".join(f"{v:+.2f}" for v in ligne))
    print(f"Parts de variance niche {A2.tolist()}, paire {B2.tolist()} ; effets des témoins D, P, PA, SOC = {BETA_TEMOINS.tolist()}")
    print()
    echecs = section0()
    if echecs:
        print(f"ARRÊT : {echecs} garde(s) de fenêtres en échec.")
        sys.exit(1)
    nul = section1()
    puis = section2()
    section3(nul, puis)
    section4()
    section5()
    section6()
    section7()
    print("§ 8. Contrôles numériques : "
          f"ajustements {COMPTE['ajustements']} ; non-convergences {COMPTE['non_convergence']} ; "
          f"replis de l'erreur type {COMPTE['repli_erreur_type']}.")
    print("Fin.")


if __name__ == "__main__":
    main()
