"""Contre-lecture (bloc-notes, hors dépôt) : monde jouet à nul composite, juge à maximum de vraisemblance recalculé,
allocation par blocs. Aucun code du dépôt, aucun résultat du banc. Graines : numpy.random.SeedSequence."""
import sys, math, numpy as np
RACINE = 20261115
M, BLOC, NB, PART, ALPHA = 24, 25, 32, 8, 0.05     # 24 cartes, blocs de 25, plafond 32 blocs (800), part fixe 8 blocs
BUDGET = M * PART                                   # 192 blocs = 4 800 tirages
SEUIL = math.log(M / ALPHA); BAS = math.log(1 / 20)

def lois(rng):
    def sm(a): a = np.exp(a); return a / a.sum(-1, keepdims=True)
    S1, S2 = sm(rng.normal(0, 1.0, (2, 3))), sm(rng.normal(0, 1.0, (2, 3)))
    P = 0.4 * S1 + 0.6 * S2                          # monde : membre de la classe {w S1 + (1-w) S2}
    eps = np.linspace(0.10, 0.30, M)
    Q = np.stack([sm(np.log(P) + e * rng.normal(0, 1, (2, 3))) for e in eps])   # cartes voisines, hors classe
    return S1, S2, P, Q

def trajectoires(rng, R, S1, S2, P, Q, denominateur="max"):
    """log W aux 32 instants pour R générations × 24 cartes ; flux propres et indépendants par carte."""
    nx1 = rng.binomial(BLOC, 0.5, (R, M, NB))
    c = np.zeros((R, M, NB, 2, 3))
    c[..., 0, :] = rng.multinomial(BLOC - nx1, P[0]); c[..., 1, :] = rng.multinomial(nx1, P[1])
    C = c.cumsum(2).reshape(R, M, NB, 6)             # comptes cumulés (x, y) à chaque instant
    lq = np.log(Q).reshape(M, 6)
    num = np.einsum("rmtk,mk->rmt", C, lq)
    lam = num - C @ np.log(P).reshape(6)             # log du rapport à la vraie loi (martingale)
    a, b = S1.reshape(6), S2.reshape(6)
    if denominateur == "max":                        # maximum de vraisemblance sur w, recalculé à chaque instant
        def d(w): return (C * ((a - b) / (w[..., None] * a + (1 - w[..., None]) * b))).sum(-1)
        lo, hi = np.zeros(C.shape[:3]), np.ones(C.shape[:3])
        for _ in range(45):
            mi = (lo + hi) / 2; pos = d(mi) > 0
            lo, hi = np.where(pos, mi, lo), np.where(pos, hi, mi)
        w = (lo + hi) / 2
        den = (C * np.log(w[..., None] * a + (1 - w[..., None]) * b)).sum(-1)
        den = np.maximum(den, C @ np.log(P).reshape(6))   # w = 0,4 est dans la classe : le maximum le domine
    else:                                            # mélange à poids fixés d'avance sur une grille de w (condition de la critique)
        g = np.linspace(0, 1, 101)
        L = np.stack([(C * np.log(x * a + (1 - x) * b)).sum(-1) for x in g], -1)
        h = L.max(-1, keepdims=True); den = h[..., 0] + np.log(np.exp(L - h).mean(-1))
    return num - den, lam

def lire(lw, n):
    """Valeur e : richesse au premier instant révélé où elle atteint m/α, sinon au dernier instant révélé (n blocs)."""
    R = lw.shape[0]; rev = np.arange(NB)[None, None, :] < n[..., None]
    haut = (lw >= SEUIL) & rev
    prem = np.where(haut.any(-1), haut.argmax(-1), np.maximum(n - 1, 0))
    return np.take_along_axis(lw, prem[..., None], -1)[..., 0]

def ebh(le, m=None):
    m = np.full(le.shape[0], M) if m is None else m
    s = -np.sort(-le, axis=1); k = np.arange(1, M + 1)[None, :]
    return (s >= np.log(np.maximum(m, 1)[:, None] / (ALPHA * k))).any(1) & (m > 0)

def etat(lw, n):
    """Arrêts lus sur les seuls instants révélés : haut (≥ m/α), bas (< 1/20 après au moins 50 tirages)."""
    rev = np.arange(NB)[None, None, :] < n[..., None]
    haut = ((lw >= SEUIL) & rev).any(-1)
    bas = ((lw < BAS) & rev & (np.arange(NB) >= 1)[None, None, :]).any(-1)
    return haut, bas

def regle_A(lw):
    R = lw.shape[0]; n = np.zeros((R, M), int)
    for tour in range(NB):
        haut, bas = etat(lw, n); actif = ~haut & ~bas & (n < NB)
        ordre = (np.arange(M) + tour) % M
        rang = np.cumsum(actif[:, ordre], 1); reste = BUDGET - n.sum(1)
        donne = np.zeros_like(actif); donne[:, ordre] = actif[:, ordre] & (rang <= reste[:, None])
        n += donne
    return n

def regle_gloutonne(lw, anticipe=False):
    """Règle adverse : après 50 tirages chacun, chaque bloc va à la carte de plus grande valeur e courante.
    anticipe=True (défaut volontaire, C4 violée) : elle choisit la carte dont la valeur e *après* le bloc sera la plus grande."""
    R = lw.shape[0]; n = np.full((R, M), 2); r = np.arange(R)
    for _ in range(BUDGET - 2 * M):
        haut, _b = etat(lw, n); libre = ~haut & (n < NB)
        idx = np.minimum(n if anticipe else n - 1, NB - 1)
        v = np.where(libre, np.take_along_axis(lw, idx[..., None], -1)[..., 0], -np.inf)
        j = v.argmax(1); ok = libre[r, j]; n[r[ok], j[ok]] += 1
    return n

def resume(nom, le, promu, extra=""):
    e = np.exp(le); R = le.shape[0]
    moy = e.mean(); se = e.std() / math.sqrt(e.size)
    p = promu.mean(); sp = math.sqrt(max(p * (1 - p), 1e-12) / R)
    print(f"{nom:<46} P(au moins une promotion) = {p:.4f} ± {1.96*sp:.4f} ; moyenne des valeurs e = {moy:.3f} ± {1.96*se:.3f} {extra}")

def main(R_total=40000, lot=2000):
    ss = np.random.SeedSequence(entropy=RACINE)
    rng0 = np.random.default_rng(ss.spawn(1)[0]); S1, S2, P, Q = lois(rng0)
    kl = (P * (np.log(P) - np.log(Q))).sum(-1).mean(-1)
    print("divergence du monde à chaque carte, nat par tirage : min %.4f, max %.4f" % (kl.min(), kl.max()))
    acc = {}
    def ajoute(nom, le, promu): acc.setdefault(nom, [[], []]); acc[nom][0].append(le); acc[nom][1].append(promu)
    viol = 0
    for b, s in enumerate(np.random.SeedSequence(entropy=RACINE, spawn_key=(1,)).spawn(R_total // lot)):
        rng = np.random.default_rng(s); lw, lam = trajectoires(rng, lot, S1, S2, P, Q); viol += int((lw > lam + 1e-9).sum())
        nF = np.full((lot, M), PART); le = lire(lw, nF); ajoute("F  part fixe 200", le, ebh(le))
        nA = regle_A(lw); assert (nA.sum(1) <= BUDGET).all(); le = lire(lw, nA); ajoute("A  blocs, arrêts, réallocation", le, ebh(le))
        _h, bas = etat(lw, nA); ajoute("A  avec m compté après coup (défaut)", le, ebh(np.where(bas, -np.inf, le), (~bas).sum(1)))
        nG = regle_gloutonne(lw); assert (nG.sum(1) <= BUDGET).all(); le = lire(lw, nG); ajoute("G  gloutonne sur les valeurs e courantes", le, ebh(le))
        ajoute("G  même règle, rapport exact à la vraie loi", lire(lam, nG), ebh(lire(lam, nG)))
        nH = regle_gloutonne(lw, True); le = lire(lw, nH); ajoute("X1 règle qui lit le bloc suivant (défaut)", le, ebh(le))
        nH = regle_gloutonne(lam, True); le = lire(lam, nH); ajoute("X1 même défaut, rapport exact à la vraie loi", le, ebh(le))
        mx = np.minimum(np.maximum.accumulate(lw, 2)[..., -1], 50.0); ajoute("X2 valeur e = maximum de la trajectoire (défaut)", mx, ebh(mx))
        lwm, _ = trajectoires(np.random.default_rng(s.spawn(1)[0]), lot, S1, S2, P, np.broadcast_to(P, Q.shape), "melange")
        le = lire(lwm, regle_gloutonne(lwm)); ajoute("X3 dénominateur à poids fixés, carte = le monde", le, ebh(le))
    print("instants où W dépasse le rapport à la vraie loi :", viol)
    for nom, (a, p) in acc.items(): resume(nom, np.concatenate(a), np.concatenate(p))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 40000)
