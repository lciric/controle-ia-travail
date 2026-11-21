"""Complément DESCRIPTIF de `simulation-organisme-change-ii-b-v1.py` : détail par cellule et étalonnage des deux candidats de
plus grande couverture. NE DÉCIDE RIEN : la décision du passage qui fait foi (« aucun candidat ne couvre l'environnement »)
est acquise et n'est pas rejouée. Le passage principal n'imprimait le détail par cellule que pour l'organisme d'origine et
pour l'organisme retenu ; aucun n'ayant été retenu, ce détail manque pour instruire les nœuds. Déclaré avant le passage :
`grille-declaree-simulation-organisme-change-detail-v1.md`. Candidats et planchers : ceux que le passage principal a rendus
(phi repris tel quel, aucun choix refait). Entropie neuve. Arguments : script principal, script du couplage v4, chaîne v2.
"""
import sys
import time
from multiprocessing import Pool

import numpy as np

_argv = sys.argv
sys.argv = [_argv[1], _argv[2], _argv[3]]
P = {"__name__": "principal"}
exec(compile(open(_argv[1]).read(), _argv[1], "exec"), P)
sys.argv = _argv
ORG, MS, N_LOTS = P["ORGANISMES"], P["MS"], P["N_LOTS"]
# (indice de l'organisme, bloc) -> phi rendu par le passage principal
A_DETAILLER = {(1, 8): 0.9, (1, 4): 0.9, (5, 8): 0.7, (5, 4): 0.5}


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gL, gD = ss.spawn(2)
    cells = [(s0, s1, rho, a, p) for p in P["PROFILS"] for a in P["ANCRES"] for rho in P["RHOS"] for s1 in P["S1S"] for s0 in P["S0S"]]
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"complement descriptif ; {N_LOTS} lots x {P['N_PAR_LOT']} episodes ; etalonnages {P['N_REP_D']} ; configurations : "
          + " ; ".join(f"{P['nom_org'](ORG[io])}, bloc {m}, phi {phi}" for (io, m), phi in A_DETAILLER.items()))
    ios = sorted({io for io, _ in A_DETAILLER})
    taches = [(cle, io, b) for b in range(N_LOTS) for io in ios for cle in cells]
    with Pool(4) as pool:
        par = {}
        for r in pool.imap(P["lot"], zip(taches, gL.spawn(len(taches))), chunksize=16):
            par[(r["cle"], r["io"], r["lot"])] = r
        g = lambda cle, io, k_: float(np.mean([par[(cle, io, b)][k_] for b in range(N_LOTS)]))
        vrais = {}
        for (io, m), phi in A_DETAILLER.items():
            print(f"\n# B. detail par cellule : {P['nom_org'](ORG[io])}, bloc de {m}, phi {phi} (dix lots reunis)")
            print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "taux_honnete", "taux_plante", "taux_ancre", "distingue", "snr_plante", "snr_ancre",
                             "ecart_type_e_honnete", "mesure/vrai_plante", "mesure/vrai_ancre"]))
            n = 0
            for cle in cells:
                pH, pP, pA = (g(cle, io, f"{x}_{m}_{phi}") for x in ("th", "tp", "ta"))
                dv = P["distingue"](pH, pP)
                n += dv
                vrais[(cle, io, m)] = (pP, pA, dv)
                print("\t".join([str(x) for x in cle] + [f"{pH:.4f}", f"{pP:.4f}", f"{pA:.4f}", str(int(dv))]
                                + [f"{g(cle, io, f'{x}_{m}'):.3f}" for x in ("snr_p", "snr_a", "sd_e", "mv_p", "mv_a")]))
            print(f"# cellules distinguees : {n} sur {len(cells)}")
        sys.stdout.flush()
        cD = [(cle, io, m, phi, *vrais[(cle, io, m)]) for (io, m), phi in A_DETAILLER.items() for cle in cells]
        print(f"\n# D. etalonnage et branches ({len(cD)} cellules x configurations)")
        print("\t".join(["s0", "s1", "ancrage", "ancre", "profil", "organisme", "bloc", "distingue_vrai", "taux_plante_vrai", "taux_ancre_vrai", "part_i", "part_ii", "part_iii",
                         "arret_epreuves", "motif_C1", "motif_C2", "motif_C3", "motif_C4", "motif_C4_du_a_la_marge", "P(aboutit|part,plante)", "P(aboutit|part,ancre)",
                         "tours_medians", "k_H_moyen", "k_P_moyen", "EMD_mediane", "exces_moyen_des_plantes_mediane"]))
        err = {}
        for l, (io, m, pp, dv) in pool.imap(P["etalonnage"], zip(cD, gD.spawn(len(cD))), chunksize=2):
            print(l)
            err.setdefault((io, m), {True: [], False: []})[dv].append((1 - pp) if dv else pp)
        for (io, m), e in err.items():
            a_, b_ = e[False], e[True]
            print(f"# ERREURS DES BRANCHES, {P['nom_org'](ORG[io])}, bloc de {m} : part alors que le plante ne se distingue pas : "
                  + (f"moyenne {np.mean(a_):.3f}, maximum {np.max(a_):.3f} sur {len(a_)} cellules" if a_ else "aucune cellule")
                  + " ; ne part pas alors qu'il se distingue : " + (f"moyenne {np.mean(b_):.3f}, maximum {np.max(b_):.3f} sur {len(b_)} cellules" if b_ else "aucune cellule"))
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()
