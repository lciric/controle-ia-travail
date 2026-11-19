"""T3 : hypothese d'identification du regresseur calibre (point 8 bis). Deux modeles qui donnent les memes moments
(v0, wbar) mais demandent des calibrages opposes :

  (S) bruit d'insertion sur toutes les lectures, v0 compris (modele de S2) : v0 = T + e0 ; v_tau = T + e_tau ;
      v_m = T + g_m (c - T) + e_m. Le calibrage par rho = cov(v0, wbar)/var(v0) est juste.
  (D) lecture sans insertion deterministe (v0 = T, aucune erreur), toute insertion comprime vers la moyenne mu de
      kappa (temoins compris) : v_tau = T + kappa (mu - T) + e_tau ; v_m = T + kappa (mu - T) + g_m (c - T) + e_m.
      Ici la loi nette sans calibrage est juste ; rho estime 1 - kappa et le calibrage tire lambda vers 0.

Diagnostic propose : r = moyenne des cov(v_tau, v_tau') entre temoins / moyenne des cov(v0, v_tau) ; r ~ 1 sous (S),
r ~ 1 - kappa sous (D).
Une seule famille, trois rangs, g = 0,10 ; deux contenus par tache comme S2 ; 16 temoins ; tirages par taches.
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, p_inf, p_sup, regresseur, sommes_taches


def essai(rng, T, modele, kappa, sigma, g, lam, B):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    n = 2 * T
    mu = 3.0
    c = mu + lam * (0.0 - mu)
    gm = g * np.array([0.5, 1.0, 1.5])
    if modele == "S":
        v0 = vrai + rng.normal(0, sigma, n)
        comp = 0.0
    else:
        v0 = vrai.copy()
        comp = kappa
    vt = vrai[:, None] + comp * (mu - vrai)[:, None] + rng.normal(0, sigma, (n, 16))
    vm = vrai[:, None] + comp * (mu - vrai)[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, sigma, (n, 3))
    Y = vm - vt[:, :3]
    wbar = vt.mean(1)
    C = np.cov(np.column_stack([v0, vt]).T)
    r = C[1:, 1:][np.triu_indices(16, 1)].mean() / C[0, 1:].mean()
    s = sommes_taches(Y, v0, wbar, tache, T)
    W = comptes(rng, T, B)
    out = dict(r=r)
    for nom, cal in (("cal", True), ("brut", False)):
        n_, S1, S2, A, Bm, rho, vb = regresseur(agrege(s), calibre=cal)
        ce = loi_jointe(n_, S1, S2, A, Bm)[0]
        lam_e = float((ce - vb) / (0.0 - vb))
        n_, S1, S2, A, Bm, rhob, vbb = regresseur(agrege(s, W), calibre=cal)
        cb = loi_jointe(n_, S1, S2, A, Bm)[0]
        lb = (cb - vbb) / (0.0 - vbb)
        out[nom] = dict(lam=lam_e, rho=float(rho), cible=p_sup(lb, 0.5) <= 0.025, moy=p_inf(lb, 0.5) <= 0.025)
    return out


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C3).spawn(1)[0])
    B, R = 1000, 300
    print("modele  kappa  T  lambda | rho med  r med | calibre (texte) : lambda med  P(cible) P(moyenne) | sans calibrage : lambda med  P(cible) P(moyenne)")
    for modele, kappa in (("S", 0.0), ("D", 0.08), ("D", 0.16)):
        for T in (45, 60):
            for lam in (1.0, 0.5):
                L = [essai(rng, T, modele, kappa, 0.4, 0.10, lam, B) for _ in range(R)]
                f = lambda k, x: np.mean([o[k][x] for o in L])
                m = lambda k, x: np.median([o[k][x] for o in L])
                print(f"  {modele}     {kappa:.2f}  {T:3d}  {lam:.1f}  |  {m('cal', 'rho'):.3f}  {np.median([o['r'] for o in L]):.3f} |"
                      f"  {m('cal', 'lam'):+.3f}  {f('cal', 'cible'):.3f}  {f('cal', 'moy'):.3f}  |"
                      f"  {m('brut', 'lam'):+.3f}  {f('brut', 'cible'):.3f}  {f('brut', 'moy'):.3f}")
                sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
