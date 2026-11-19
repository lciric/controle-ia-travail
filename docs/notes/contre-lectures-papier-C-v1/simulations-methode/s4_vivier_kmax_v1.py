"""S4 : regle du vivier (addendum de derivation) : k_max, cibles equidistantes, malediction du vainqueur.

Regle du brouillon 4 : ET(n) = ET(n_cal) sqrt(n_cal / n) ; k_max(n) = 1 + floor[etendue des gamma_bar de la famille /
(1,96 sqrt(2) ET(n))] ; k = min(5, max(3, k_max)) ; reserve « niveaux non separables » si k_max < 3 ; cibles
equidistantes entre le min et le max des gamma_bar du pilote ; formulation la plus proche de chaque cible.
Modele : 16 formulations, gains vrais repartis lineairement sur une etendue vraie E (en unites d'ET(n_cal)) ;
gains du pilote = vrais + N(0, ET(n_cal)^2) ; n_cal = 60.
Mesures : P(reserve) ; k retenu ; etendue (pilote) des formulations retenues contre leur etendue vraie ; part des paires
de rangs adjacents vraiment separables a l'effectif n (ecart vrai >= 1,96 sqrt(2) ET(n)) ; biais du rang le plus fort.
Correction essayee : etendue debiaisee = etendue - E[etendue de 16 N(0,1)] x ET(n_cal), et selection par validation
croisee (moitie des contenus pour choisir, l'autre moitie pour estimer les gains retenus et k_max).
"""
import sys

import numpy as np

NF = 16
NCAL = 60


def regle(gh, se_cal, n, deb=0.0):
    et_n = se_cal * np.sqrt(NCAL / n)
    etendue = gh.max() - gh.min() - deb
    kmax = 1 + int(np.floor(max(etendue, 0.0) / (1.96 * np.sqrt(2) * et_n)))
    k = min(5, max(3, kmax))
    cibles = gh.min() + np.arange(k) * (gh.max() - gh.min()) / (k - 1)
    pris = []
    for t in cibles:
        ordre = np.argsort(np.abs(gh - t), kind="stable")
        for j in ordre:
            if j not in pris:
                pris.append(int(j))
                break
    pris = sorted(pris, key=lambda j: (gh[j], j))
    return kmax, k, pris, et_n


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C4D).spawn(1)[0])
    R = 4000
    e_range = np.mean([np.ptp(rng.normal(0, 1, NF)) for _ in range(100000)])
    print(f"esperance de l'etendue de 16 N(0, 1) : {e_range:.3f}")
    print("E_vraie  n    | brouillon 4 : P(reserve) k_moyen etendue_pilote(retenues) etendue_vraie(retenues) part_paires_separables biais_rang_fort |"
          " debiaisee : P(reserve) | validation croisee : P(reserve) part_paires_separables")
    for E in (0.0, 1.0, 2.0, 4.0, 8.0):
        vrais = np.linspace(0, E, NF)
        for n in (60, 120, 240):
            out = []
            for _ in range(R):
                gh = vrais + rng.normal(0, 1.0, NF)
                kmax, k, pris, et_n = regle(gh, 1.0, n)
                sep = np.diff(vrais[pris]) >= 1.96 * np.sqrt(2) * et_n
                biais = gh[pris[-1]] - vrais[pris[-1]]
                kmax_d, _, _, _ = regle(gh, 1.0, n, deb=e_range * 1.0)
                # validation croisee : deux moities de contenus, ET d'une moitie = sqrt(2)
                ga = vrais + rng.normal(0, np.sqrt(2), NF)
                gb = vrais + rng.normal(0, np.sqrt(2), NF)
                _, kc, pris_c, _ = regle(ga, np.sqrt(2), n)
                et_n_c = np.sqrt(2) * np.sqrt((NCAL / 2) / n)
                etendue_b = gb[pris_c].max() - gb[pris_c].min()
                kmax_c = 1 + int(np.floor(max(etendue_b, 0) / (1.96 * np.sqrt(2) * et_n_c)))
                sep_c = np.diff(vrais[pris_c]) >= 1.96 * np.sqrt(2) * (1.0 * np.sqrt(NCAL / n))
                out.append((kmax < 3, k, np.ptp(gh[pris]), np.ptp(vrais[pris]), sep.mean(), biais, kmax_d < 3, kmax_c < 3, sep_c.mean()))
            o = np.array(out, float)
            print(f"{E:4.1f}  {n:>4}  |  {o[:,0].mean():.3f}  {o[:,1].mean():.2f}  {o[:,2].mean():.2f}  {o[:,3].mean():.2f}  {o[:,4].mean():.3f}  {o[:,5].mean():+.2f}  |"
                  f"  {o[:,6].mean():.3f}  |  {o[:,7].mean():.3f}  {o[:,8].mean():.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
