"""Instrument : convergence de la copie de decomposer_jacobi_symetrique avec son plafond par défaut (120 rotations).

(i) 20 x 20, forme du rapport (usage de l'essai 1) ; (ii) 16 x 16 semi-définies positives du type de la mémoire
ISVD (somme pondérée de psi psi^T, psi = extraire_vecteur_koopman sur textes synthétiques, copie exacte) —
hors périmètre des briques 2 à 4, signalé parce que le seuil sigma_1 / sigma_6 = 60,9 du protocole P1 en dépend.
Usage : python3 -I -B essai_instrument_jacobi_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np

import commun_v1 as cm
import textes_v1 as tx

JEUX = 200


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    jac, emp_j = cm.jacobi_organisme()
    fs, emp_k = cm.copier_fonctions("organisme/memoire_isvd.py", ["extraire_vecteur_koopman"])
    koop = fs["extraire_vecteur_koopman"]
    res = {}
    for nom in ("rapport_20", "isvd_16_12_traces", "isvd_16_40_traces"):
        residus, err_s6, err_ratio, err_s1 = [], [], [], []
        for r in range(JEUX):
            rng = cm.generateur("b2_psd", 5000 + ("rapport_20", "isvd_16_12_traces", "isvd_16_40_traces").index(nom), r)
            if nom == "rapport_20":
                d, o, q = cm.unitaires(rng, 20), cm.unitaires(rng, 20), rng.uniform(0.5, 1.5, 20)
                m = cm.noyau_rapport(d, o, q)
            else:
                nb = 12 if "12" in nom else 40
                vocab = tx.pseudo_mots(rng, 300, set())
                m = np.zeros((16, 16))
                for _ in range(nb):
                    psi = np.array(koop(" ".join(rng.choice(vocab, size=int(rng.integers(20, 80)))), dim=16))
                    m += rng.uniform(0.05, 1.0) * np.outer(psi, psi)
            n = m.shape[0]
            _, s120, res120 = cm.valeurs_propres_jacobi(jac, m, 120)
            _, sconv, _ = cm.valeurs_propres_jacobi(jac, m, 5000)
            ref = np.sort(np.abs(np.linalg.eigvalsh(m)))[::-1]
            residus.append(float(res120.max() / ref[0]))
            err_s1.append(float(abs(s120[0] - ref[0]) / ref[0]))
            if n == 16:
                err_s6.append(float(abs(s120[5] - ref[5]) / ref[5]))
                err_ratio.append(float(abs(s120[0] / s120[5] - ref[0] / ref[5]) / (ref[0] / ref[5])))
            assert np.allclose(np.sort(sconv)[::-1], ref, rtol=1e-8, atol=1e-10)

        def q(v):
            v = np.array(v)
            return {"mediane": float(np.median(v)), "q95": float(np.quantile(v, 0.95)), "max": float(v.max())} if len(v) else None
        res[nom] = {"jeux": JEUX, "residu_relatif_120_iter": q(residus), "erreur_relative_sigma1_120_iter": q(err_s1),
                    "erreur_relative_sigma6_120_iter": q(err_s6), "erreur_relative_sigma1_sur_sigma6_120_iter": q(err_ratio)}
    sortie = {"essai": "instrument : convergence de Jacobi à 120 rotations", "heure_lancement_utc": args.heure,
              "graines": cm.description_graines() | {"tache": "b2_psd", "spawn_key": "(1, 5000 + id_cas, r)"},
              "versions": cm.versions(), "empreintes_segments": {"decomposer_jacobi_symetrique": emp_j, **emp_k},
              "verification": "5 000 rotations : spectre égal à LAPACK (rtol 1e-8) sur tous les jeux", "resultats": res}
    cm.ecrire_json(cm.SORTIE / "resultats-instrument-jacobi-v1.json", sortie)
    print(res)


if __name__ == "__main__":
    main()
