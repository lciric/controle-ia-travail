"""Contre-lecture banque v3 — k6 : `verifier_banque` du noyau (seule porte de `lancer --reel`) sur la v1, la v2, la v3 et les artefacts A1 à A3.
Usage : python3 -I -B k6_verifier_banque_artefacts_v1.py RACINE_ESSAIM BANQUE_DIR"""
import pathlib, sys
R, B = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
sys.path.insert(0, str(R))
from essaim_m3.banque import verifier_banque
for nom in ("banque-confrontation-v1.json", "banque-confrontation-v2.json", "banque-confrontation-v3.json",
            "construction-v3/artefacts-v1/A1-fuite-exacte-train-et-test-final.json",
            "construction-v3/artefacts-v1/A2-fuite-a-80-pour-cent.json",
            "construction-v3/artefacts-v1/A3-numeros-dans-l-ordre-du-fichier.json"):
    pb = verifier_banque(B / nom)
    print(f"{nom} : {'accepté (aucun problème)' if not pb else 'refusé : ' + '; '.join(pb[:2])}")
