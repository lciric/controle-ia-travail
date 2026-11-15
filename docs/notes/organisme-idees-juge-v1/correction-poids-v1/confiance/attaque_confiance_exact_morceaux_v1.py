"""Calcul exact par morceaux — v1. Programme du réfutateur, mise au point exploratoire, aucune revendication.

Même calcul que le mode « exact » de `attaque_confiance_v1.py` (fonction `exact_promotion`, importée telle quelle), mais
un petit morceau par appel, pour tenir sous dix minutes sur une machine chargée.
Usage : python -I -B attaque_confiance_exact_morceaux_v1.py A2 MONDE SORTIE.json
        (nul convexe [0,3 ; 0,8], 500 + 500 tirages de confiance, huit cartes constantes : taille de la méthode coupée)
        python -I -B attaque_confiance_exact_morceaux_v1.py C MONDE CARTE SORTIE.json
        (nul non convexe {0,3} et {0,7} ; monde dans le nul ou hors du nul ; 50 + 50 puis 500 + 500 tirages de confiance)
"""

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import attaque_confiance_v1 as at  # noqa: E402

NUL_A = [(0.3, 0.8)]
NUL_C = [(0.3, 0.3), (0.7, 0.7)]
CARTES_A2 = (0.15, 0.3, 0.4, 0.5, 0.6, 0.7, 0.85, 0.95)


def main():
    bloc, sortie = sys.argv[1], sys.argv[-1]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    t0 = time.time()
    doc = at.entete("exact_morceaux", bloc=bloc)
    if bloc == "A2":
        pm = float(sys.argv[2])
        lignes = []
        for c in CARTES_A2:
            r = at.exact_promotion(pm, c, NUL_A, 500, 500, at.BETAS)
            lignes.append({"carte": c, **{str(b): {"promotion": r[b][0], "non_couverture": r[b][1]} for b in at.BETAS}})
        doc.update({"nul": NUL_A, "n1": 500, "n2": 500, "monde": pm, "lignes": lignes,
                    "pire_promotion": {str(b): max(l[str(b)]["promotion"] for l in lignes) for b in at.BETAS},
                    "pire_non_couverture": {str(b): max(l[str(b)]["non_couverture"] for l in lignes) for b in at.BETAS}})
    elif bloc == "C":
        pm, c = float(sys.argv[2]), float(sys.argv[3])
        dans = any(abs(pm - a) < 1e-12 for a, _ in NUL_C)
        doc.update({"nul": NUL_C, "monde": pm, "carte": c, "monde_dans_le_nul": dans,
                    "v9": at.exact_promotion(pm, c, NUL_C, 0, 0, at.BETAS, mode="v9")["v9"][0]})
        for n1, n2 in ((50, 50), (500, 500)):
            r = at.exact_promotion(pm, c, NUL_C, n1, n2, at.BETAS)
            doc[f"coupee_n{n1 + n2}"] = {str(b): {"promotion": r[b][0], "non_couverture": r[b][1]} for b in at.BETAS}
    else:
        raise SystemExit("blocs : A2, C")
    doc["duree_s"] = round(time.time() - t0, 1)
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    print("écrit :", sortie)


if __name__ == "__main__":
    main()
