"""S1 : l'estimateur c chapeau (rapport) et le test de lambda, sans regression vers la moyenne (v0 lu sans erreur).

Question : avec un gain g faible ou modere, le test de C-P1 (percentiles de lambda, filtre « famille positive »)
garde-t-il son niveau a lambda = 0,5 ? Couverture de l'intervalle a 95 % de lambda ? Comparaison avec un test
sur le deplacement ajuste au point milieu, delta_mid = Gbar (lambda - 1/2) = Gbar (c - m) / (v* - v0bar), qui
n'a pas de denominateur aleatoire en g.
Modele : T taches, deux contenus par tache (honnete, saboteur), effet de tache ; k = 3 rangs, g_m = g (0,5 ; 1 ; 1,5) ;
v* = 0 ; moyenne de population de v0 = 3 ; c = 3 - 3 lambda ; bruit de lecture sd 0,4 sur chaque condition inseree.
"""
import sys

import numpy as np

from commun_v1 import agrege, comptes_bootstrap, loi_jointe, p_inf, p_sup, sommes_par_tache

V_ETOILE = 0.0
MU = 3.0


def simule(rng, T, g, lam, k=3, sd_e=0.4):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    base = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    c = MU + lam * (V_ETOILE - MU)
    gm = g * np.linspace(0.5, 1.5, k)
    D = (c - base)[:, None] * gm[None, :] + rng.normal(0, sd_e, (2 * T, k))
    return D, base, tache


def un_essai(rng, T, g, lam, B, alpha=0.025):
    D, v0, tache = simule(rng, T, g, lam)
    s = sommes_par_tache(D, v0, tache, T)
    est = loi_jointe(agrege(s))
    W = comptes_bootstrap(rng, T, B)
    bs = loi_jointe(agrege(s, W))
    lam_hat = (est["c"] - est["v0bar"]) / (V_ETOILE - est["v0bar"])
    lam_b = (bs["c"] - bs["v0bar"]) / (V_ETOILE - bs["v0bar"])
    dmid_b = bs["G"] * (lam_b - 0.5)
    positif = p_sup(bs["G"], 0.0) <= alpha
    deg = bs["deg"].mean()
    identifiable = positif and deg <= 0.01
    lo, hi = np.percentile(lam_b, [2.5, 97.5])
    return dict(
        positif=positif, identifiable=identifiable, deg=deg, lam=lam_hat,
        cible_lam=p_sup(lam_b, 0.5) <= alpha, moyenne_lam=p_inf(lam_b, 0.5) <= alpha,
        cible_dm=p_sup(dmid_b, 0.0) <= alpha, moyenne_dm=p_inf(dmid_b, 0.0) <= alpha,
        couvre=(lo <= lam) and (lam <= hi), largeur=hi - lo,
    )


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C1A).spawn(1)[0])
    B, R = 2000, 400
    print("S1 - lambda vrai = 0,5 (frontiere des deux verdicts directionnels) ; niveau nominal de chaque verdict : 0,025")
    print("T(taches)  g     P(positif) P(identif.) | parmi identifiables : P(cible|lam) P(moy.|lam) P(cible|dmid) P(moy.|dmid)"
          " couverture95(lam) mediane lam  | non conditionnel : P(|lam_hat-0,5|>2)")
    for T in (30, 60, 120):
        for g in (0.03, 0.06, 0.10, 0.20):
            res = [un_essai(rng, T, g, 0.5, B) for _ in range(R)]
            ident = [r for r in res if r["identifiable"]]
            f = lambda cle, L: np.mean([r[cle] for r in L]) if L else float("nan")
            lam_all = np.array([r["lam"] for r in res])
            print(f"{T:>4}      {g:.2f}   {f('positif', res):.3f}      {f('identifiable', res):.3f}      |"
                  f"   {f('cible_lam', ident):.3f}          {f('moyenne_lam', ident):.3f}        {f('cible_dm', ident):.3f}"
                  f"          {f('moyenne_dm', ident):.3f}         {f('couvre', ident):.3f}          "
                  f"{np.median([r['lam'] for r in ident]) if ident else float('nan'):.3f}       |  {np.mean(np.abs(lam_all - 0.5) > 2):.3f}")
    print()
    print("S1 bis - puissance : lambda vrai = 1 (destination = cible) et lambda vrai = 0 (destination = moyenne)")
    print("T     g     lam_vrai  P(identif.)  P(cible|lam)  P(cible|dmid)  P(moy.|lam)  P(moy.|dmid)  largeur mediane IC lam")
    for T in (30, 60, 120):
        for g in (0.06, 0.10, 0.20):
            for lam in (1.0, 0.0):
                res = [un_essai(rng, T, g, lam, B) for _ in range(200)]
                ident = [r for r in res if r["identifiable"]]
                f = lambda cle, L: np.mean([r[cle] for r in L]) if L else float("nan")
                print(f"{T:>4}  {g:.2f}  {lam:.1f}       {f('identifiable', res):.3f}        {f('cible_lam', ident):.3f}"
                      f"         {f('cible_dm', ident):.3f}          {f('moyenne_lam', ident):.3f}        {f('moyenne_dm', ident):.3f}"
                      f"         {np.median([r['largeur'] for r in ident]) if ident else float('nan'):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
