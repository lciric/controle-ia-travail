"""Sonde à beaucoup de tirages de confiance — v1. Programme du réfutateur, mise au point exploratoire, aucune revendication.

Même calcul que le mode « hors_nul » de `attaque_confiance_v1.py` (fonction `un_monde_hors`, importée telle quelle), pour
des cas que ce programme ne liste pas : l'ensemble coupé (BB_T_coupe) seul, avec 5 000 tirages d'entraînement (2 500 pour
l'ensemble). Les mondes, l'archive, les cartes et les tirages frais sont ceux des cas à 100 et 1 000 tirages (même clé de
graine) ; seuls les tirages d'entraînement s'allongent.
Usage : python -I -B attaque_confiance_sonde_v1.py FORME DEBUT FIN SORTIE.json     (FORME : oblique, V1_0.50 ou V1_0.75)
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import attaque_confiance_v1 as at  # noqa: E402

N_TR = 5000


def main():
    forme, debut, fin, sortie = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    if forme == "oblique":
        cas, spec = f"oblique_ntr{N_TR}", ("oblique", None, N_TR, ("BB_T_coupe",))
    elif forme.startswith("V1_"):
        cas, spec = f"{forme}_ntr{N_TR}", ("V1", float(forme.split("_")[1]), N_TR, ("BB_T_coupe",))
    else:
        raise SystemExit("formes : oblique, V1_0.50, V1_0.75")
    at.CAS_HORS[cas] = spec                       # cas ajouté à l'exécution ; le programme d'attaque n'est pas modifié
    t0 = time.time()
    lignes = [at.un_monde_hors(cas, r)[0] for r in range(debut, fin)]
    seuils = {"v9": at.SEUIL_V9, "v8": at.SEUIL_V9, "limite": at.SEUIL_V9}
    seuils.update({f"BB_T_coupe|beta={b}": at.SEUILS[b] for b in at.BETAS})
    cle = {"V1": 10 + int(round((spec[1] or 0) * 100)), "oblique": 50}[spec[0]]
    at.ecrire(sortie, at.entete("hors_nul", cas=cas, indice_du_cas=None, forme=spec[0], parametre=spec[1], n_tr=N_TR,
                                cle_de_graine=[2, cle, "monde"], J=3, K=3, methodes=["BB_T_coupe"], mondes=[debut, fin],
                                seuils_log=seuils, programme="attaque_confiance_sonde_v1", duree_s=round(time.time() - t0, 1),
                                lignes=lignes))


if __name__ == "__main__":
    main()
