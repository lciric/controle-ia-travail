"""S3 : W de Kendall de C-P3a et C-P3b.

(a) Loi exacte, 5 evaluateurs (familles), 3 objets (juges) : reprise independante des mesures de conception
    (bbad099d...) ; probabilite, sous le nul, de la « refutation » W <= 0,20.
(b) Alternatives : les juges different vraiment (ecart delta entre juges successifs, en unites d'erreur type de Gbar) :
    P(p <= 0,05) et P(W <= 0,20).
(c) Regression vers la moyenne propre au juge, AUCUNE attaque : trois juges dont l'interaction contenu x condition a un
    ecart type 0,2 / 0,4 / 0,6 ; Gbar estime par la loi jointe du brouillon 4 (Delta = v_m - v0 sur v0), v0 partage par
    les cinq familles d'un juge ; P(p <= 0,05) ; meme chose avec la loi nette du temoin et calibree (TEM+CAL de S2).
(d) C-P3b, 10 evaluateurs (5 familles x 2 corpus) : corpus A concordant, corpus B au hasard (ou inverse) :
    P(p <= 0,05), c'est-a-dire « invariance au corpus confirmee » alors que le corpus B ne la porte pas ;
    P(W <= 0,10) sous le nul (refutation de C-P3b).
"""
import itertools
import sys

import numpy as np

from commun_v1 import loi_jointe
from s2_regression_moyenne_v1 import agrege, calibre, sommes

PERMS = np.array(list(itertools.permutations([1, 2, 3])))


def w_kendall(rangs):
    """rangs : (..., m, k) sans ex aequo."""
    m, k = rangs.shape[-2], rangs.shape[-1]
    R = rangs.sum(-2)
    S = ((R - R.mean(-1, keepdims=True)) ** 2).sum(-1)
    return 12 * S / (m ** 2 * (k ** 3 - k))


def loi_nulle_exacte(m):
    combos = np.array(list(itertools.product(range(6), repeat=m)))
    return np.sort(w_kendall(PERMS[combos]))


def p_exact(w, nul):
    return 1.0 - np.searchsorted(nul, w - 1e-9, side="left") / len(nul)


def rangs_de(valeurs):
    """valeurs : (..., m, k) -> rangs 1..k par ligne."""
    return valeurs.argsort(-1).argsort(-1) + 1


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C3C).spawn(1)[0])
    nul5 = loi_nulle_exacte(5)
    print("(a) loi exacte m = 5, k = 3 :", len(nul5), "affectations ; esperance", round(nul5.mean(), 4))
    for w in (0.52, 0.64, 0.76):
        print(f"    P(W >= {w}) = {p_exact(w, nul5):.4f}")
    print(f"    P(W <= 0,20) sous le nul (frequence de la « refutation » de C-P3a sans aucune information) = {(nul5 <= 0.2 + 1e-9).mean():.4f}")
    print()
    print("(b) juges vraiment differents : Gbar_jf = delta * (-1, 0, 1)_j + effet de famille + bruit N(0, 1)")
    print("    delta   P(p<=0,05) « confirme »   P(W<=0,20) « refute »")
    R = 20000
    for delta in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0):
        val = delta * np.array([-1.0, 0.0, 1.0])[None, None, :] + rng.normal(0, 1, (R, 5, 1)) + rng.normal(0, 1, (R, 5, 3))
        w = w_kendall(rangs_de(val))
        p = p_exact(w, nul5)
        print(f"    {delta:.2f}    {np.mean(p <= 0.05):.3f}                    {np.mean(w <= 0.2 + 1e-9):.3f}")
    print()
    print("(c) aucune attaque ; trois juges, sd de l'interaction contenu x condition 0,2 / 0,4 / 0,6 ; T = 60 taches ; k = 3")
    sds = (0.2, 0.4, 0.6)
    Rc = 400
    T = 60
    pB4, pCAL, ordre_ok = [], [], []
    for _ in range(Rc):
        u = rng.normal(0, 0.5, T)
        tache = np.repeat(np.arange(T), 2)
        vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
        Gb4 = np.zeros((5, 3))
        Gcal = np.zeros((5, 3))
        for j, sd in enumerate(sds):
            v0 = vrai + rng.normal(0, sd, 2 * T)
            for f in range(5):
                vm = vrai[:, None] + rng.normal(0, sd, (2 * T, 3))
                vt = vrai[:, None] + rng.normal(0, sd, (2 * T, 3))
                Gb4[f, j] = float(loi_jointe(agrege(sommes(vm - v0[:, None], v0, tache, T)))["G"])
                wbar = vt.mean(1)
                s2 = agrege(sommes(vm - vt, v0, tache, T, extra=dict(Sw=wbar, Svw=v0 * wbar)))
                Gcal[f, j] = float(loi_jointe(calibre(s2)[0])["G"])
        pB4.append(p_exact(w_kendall(rangs_de(Gb4)), nul5))
        pCAL.append(p_exact(w_kendall(rangs_de(Gcal)), nul5))
        ordre_ok.append(bool(np.all(np.argsort(Gb4.mean(0)) == np.array([0, 1, 2]))))
    print(f"    loi du brouillon 4 : P(p <= 0,05) = {np.mean(np.array(pB4) <= 0.05):.3f} (niveau nominal 0,05) ;"
          f" ordre des juges = ordre de leur bruit dans {np.mean(ordre_ok):.3f} des essais")
    print(f"    loi nette du temoin, calibree : P(p <= 0,05) = {np.mean(np.array(pCAL) <= 0.05):.3f}")
    print()
    print("(d) C-P3b, 10 evaluateurs ; loi nulle par 200 000 tirages")
    nul10 = np.sort(w_kendall(PERMS[rng.integers(0, 6, (200000, 10))]))
    print(f"    esperance sous le nul {nul10.mean():.4f} ; P(W <= 0,10) sous le nul (« refutation ») = {(nul10 <= 0.1 + 1e-9).mean():.3f}")
    R = 20000
    for titre, dB in (("corpus B au hasard", 0.0), ("corpus B inverse (delta -1)", -1.0)):
        for dA in (1.0, 2.0):
            valA = dA * np.array([-1.0, 0.0, 1.0])[None, None, :] + rng.normal(0, 1, (R, 5, 3))
            valB = dB * np.array([-1.0, 0.0, 1.0])[None, None, :] + rng.normal(0, 1, (R, 5, 3))
            w10 = w_kendall(rangs_de(np.concatenate([valA, valB], axis=1)))
            p10 = 1.0 - np.searchsorted(nul10, w10 - 1e-9, side="left") / len(nul10)
            print(f"    corpus A concordant (delta {dA}) et {titre} : P(p <= 0,05) = {np.mean(p10 <= 0.05):.3f}"
                  f" ; P(W <= 0,10) = {np.mean(w10 <= 0.1 + 1e-9):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
