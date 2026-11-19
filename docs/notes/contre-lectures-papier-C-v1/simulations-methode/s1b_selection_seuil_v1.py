"""S1b : biais de selection de lambda quand la famille passe tout juste le filtre « positive ».

Meme modele que S1 (pas de regression vers la moyenne), lambda vrai = 0,5, g faible. On compare le taux de
« vers la moyenne » (niveau nominal 0,025) selon le seuil du filtre : p unilateral de Gbar <= 0,025 (brouillon 4,
dernier rang de Holm), <= 0,005 (premier rang de Holm sur cinq familles), <= 0,001.
"""
import sys

import numpy as np

from commun_v1 import agrege, comptes_bootstrap, loi_jointe, p_inf, p_sup, sommes_par_tache
from s1_rapport_c_chapeau_v1 import V_ETOILE, simule


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C1B).spawn(1)[0])
    B, R = 4000, 1000
    print("T    g      seuil   P(passe)  P(« moyenne » | passe)  P(« cible » | passe)  mediane lambda | passe")
    for T in (30, 60):
        for g in (0.03, 0.045):
            rows = []
            for _ in range(R):
                D, v0, tache = simule(rng, T, g, 0.5)
                s = sommes_par_tache(D, v0, tache, T)
                est = loi_jointe(agrege(s))
                bs = loi_jointe(agrege(s, comptes_bootstrap(rng, T, B)))
                lam_b = (bs["c"] - bs["v0bar"]) / (V_ETOILE - bs["v0bar"])
                lam = float((est["c"] - est["v0bar"]) / (V_ETOILE - est["v0bar"]))
                rows.append((p_sup(bs["G"], 0.0), bs["deg"].mean(), p_inf(lam_b, 0.5) <= 0.025, p_sup(lam_b, 0.5) <= 0.025, lam))
            a = np.array(rows, float)
            for seuil in (0.025, 0.005, 0.001):
                m = (a[:, 0] <= seuil) & (a[:, 1] <= 0.01)
                print(f"{T:>3}  {g:.3f}  {seuil:.3f}   {m.mean():.3f}     {a[m,2].mean() if m.any() else float('nan'):.3f}"
                      f"                   {a[m,3].mean() if m.any() else float('nan'):.3f}                 {np.median(a[m,4]) if m.any() else float('nan'):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
