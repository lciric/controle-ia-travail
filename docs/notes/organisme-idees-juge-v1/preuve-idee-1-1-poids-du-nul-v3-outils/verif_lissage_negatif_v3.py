"""Preuve v3 de l'idée 1.1 — contre-exemple à P4 par une `moyenne_glissante` à lissage négatif (acceptée par
`valider_loi`, qui ne contrôle pas `lissage` : selection_pari.py, copie 94bfd92, l. 212 à 214).
Énumération exacte des 2^n suites ; deux issues ; monde constant p = 1/2 (membre de la famille des lois constantes,
sommets δ_0, δ_1, donc de tout membre linéaire) ; blocs de b ; projection de bloc = moyenne des lois réalisées (exacte
sur les lois constantes) ; certificat exact. Formes : « nu » (historique complet), « gel » (historique arrêté au début du
bloc) ; comparaisons : maximum exact des lois constantes sur les tirages mêmes (carte non gelée), rapport au monde.
Aucun code du juge importé : `moyenne_glissante` et `sans_remise` recopiées de selection_pari.proba (l. 131 à 135,
156 à 159) avec le plancher 1e-12 et la renormalisation de `_normaliser` (l. 97 à 100). Aucun aléa : pas de graine.
"""
import itertools
import math

import numpy as np

PLANCHER = 1e-12


def normaliser(p):
    p = [max(PLANCHER, float(x)) for x in p]
    s = sum(p)
    return np.array([x / s for x in p])


def moyenne_glissante(k, w, lam, h, t):
    recents = list(h[max(0, t - w):t])
    compte = [recents.count(i) for i in range(k)]
    return normaliser([(compte[i] + lam) / (len(recents) + k * lam) for i in range(k)])


def sans_remise(c, h, t):
    vus = [list(h[:t]).count(k) for k in range(len(c))]
    return normaliser([max(0, ci - v) for ci, v in zip(c, vus)])


def lois(carte, y, b, forme):
    return np.array([carte(y[:s] if forme == "nu" else y[:(s // b) * b], s) for s in range(len(y))])


def e_bloc(Q, yb):
    phi = Q.mean(0)
    c = max((Q[:, k] / phi[k]).mean() for k in range(Q.shape[1]))
    return float(np.prod(Q[np.arange(len(yb)), yb] / phi[yb]) / max(1.0, c) ** len(yb))


def pire_rapport(M):
    m = np.sort(M.max(1))[::-1]
    meilleur, a = 0.0, None
    for v in m:
        if v <= 1e-12:
            break
        r = float((m >= v - 1e-12).mean()) * math.exp(v)
        if r > meilleur:
            meilleur, a = r, math.exp(-v)
    return meilleur, a


def jouer(nom, carte, b, n):
    suites = np.array(list(itertools.product(range(2), repeat=n)))
    nb = n // b
    lw = {f: np.zeros((len(suites), nb)) for f in ("nu", "gel")}
    lmax, lvrai = np.zeros((len(suites), nb)), np.zeros((len(suites), nb))
    eb = {f: np.zeros(nb) for f in ("nu", "gel")}
    for i, y in enumerate(suites):
        for f in ("nu", "gel"):
            Q = lois(carte, y, b, f)
            acc = 0.0
            for B in range(nb):
                idx = np.arange(B * b, (B + 1) * b)
                e = e_bloc(Q[idx], y[idx])
                eb[f][B] += e / len(suites)
                acc += math.log(max(e, 1e-300))
                lw[f][i, B] = acc
        lq = np.cumsum(np.log(lois(carte, y, b, "nu")[np.arange(n), y]))
        for B in range(nb):
            t = (B + 1) * b
            k1 = int(y[:t].sum())
            lm = (k1 * math.log(k1 / t) if k1 else 0.0) + ((t - k1) * math.log(1 - k1 / t) if t - k1 else 0.0)
            lmax[i, B] = lq[t - 1] - lm
            lvrai[i, B] = lq[t - 1] - t * math.log(0.5)
    rn, an = pire_rapport(lw["nu"])
    p05 = float((lw["nu"] >= math.log(20) - 1e-12).any(1).mean())
    print(f"{nom:44s} b={b} n={n:2d} E[e_B] par bloc nu {np.round(eb['nu'], 4).tolist()} gel {np.round(eb['gel'], 4).tolist()}")
    print(f"{'':44s} sup_α P/α : nu {rn:.4f} (α = {an if an is None else round(an, 4)}) ; gel {pire_rapport(lw['gel'])[0]:.4f} ; "
          f"maximum {pire_rapport(lmax)[0]:.4f} ; rapport au monde {pire_rapport(lvrai)[0]:.4f} ; P(nu, α = 0,05) {p05:.4f}")


def main():
    # 1. lois prédictives : moyenne_glissante à lissage négatif
    for lam in (-0.6, -0.4, 0.5):
        print(f"moyenne_glissante fenêtre 1, lissage {lam} : historique [] {moyenne_glissante(2, 1, lam, [], 0).round(6).tolist()} ; "
              f"[0] {moyenne_glissante(2, 1, lam, [0], 1).round(6).tolist()} ; [1] {moyenne_glissante(2, 1, lam, [1], 1).round(6).tolist()}")
    try:
        moyenne_glissante(2, 1, 0.0, [], 0)
        print("lissage 0, fenêtre vide : pas d'erreur")
    except ZeroDivisionError:
        print("lissage 0, fenêtre vide : ZeroDivisionError (fenêtre vide ⇒ loi uniforme seulement si le lissage est fini et non nul)")
    # 2. fenêtre ≥ horizon et lissage −c, avec 2c > horizon (sinon le dénominateur s'annule quand 2c issues sont vues :
    #    ZeroDivisionError, comme dans le code réel) : même loi que sans_remise [c, c], sur toutes les suites de 8 tirages
    try:
        moyenne_glissante(2, 8, -1.0, [0, 1], 2)
    except ZeroDivisionError:
        print("fenêtre 8, lissage −1, après deux issues : ZeroDivisionError (longueur + 2·lissage = 0)")
    for c in (5, 6, 8):
        ecart = 0.0
        for y in itertools.product(range(2), repeat=8):
            for t in range(9):
                ecart = max(ecart, float(np.abs(moyenne_glissante(2, 8, -c, y, t) - sans_remise([c, c], y, t)).max()))
        print(f"moyenne_glissante(fenêtre 8, lissage −{c}) contre sans_remise [{c}, {c}], 2^8 suites, tous les instants : plus grand écart {ecart:.3e}")
    # 3. énumération exacte
    cartes = {"moyenne_glissante fenêtre 1, lissage -0.6": lambda h, s: moyenne_glissante(2, 1, -0.6, h, s),
              "moyenne_glissante fenêtre 2, lissage -1.5": lambda h, s: moyenne_glissante(2, 2, -1.5, h, s),
              "moyenne_glissante fenêtre 12, lissage -7": lambda h, s: moyenne_glissante(2, 12, -7.0, h, s)}
    for nom, carte in cartes.items():
        for b, n in ((2, 2), (2, 8), (2, 12), (4, 12)):
            jouer(nom, carte, b, n)


if __name__ == "__main__":
    main()
