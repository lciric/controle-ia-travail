"""Écrit le manifeste du paquet du lot 6 v5 (fichier neuf, jamais écrasé) : les trois modules du lot 5 v3, lus dans leur
dossier, et les fichiers du paquet v5, chacun avec son empreinte.

    python3 -B ecrire_manifeste_na_lot6_v5.py
"""

import hashlib
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
LOT_5_V3 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-5-vehicule-na-v3/paquet/orchestrator"
SOURCES_LOT_5_V3 = ("pole/registre_na_v3.py", "pole/verifier_registre_servi_na_v3.py", "pole/portier_na_v3.py")
PAQUET = ("pole/registre_na_v4.py", "pole/code_charge_na_v1.py", "pole/simulation_na_v5.py", "pole/course_na_v5.py",
          "essais/aides_na_lot6_v5.py", "essais/test_na_lot6_v5_course.py", "essais/mutations_na_lot6_v5.py")


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def principal():
    fichiers = []
    for rel in SOURCES_LOT_5_V3:
        src = os.path.join(LOT_5_V3, rel)
        fichiers.append({"source": src, "chemin": "orchestrator/" + rel, "sha256": sha256(src), "lot": "5 v3"})
    for rel in PAQUET:
        src = os.path.join("paquet", "orchestrator", rel)
        fichiers.append({"source": src, "chemin": "orchestrator/" + rel, "sha256": sha256(os.path.join(ICI, src)),
                         "lot": "6 v5"})
    m = {"format": "manifeste-paquet-vehicule-na-lot-6-v5", "commit_de_base": "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb",
         "ordre_de_la_chaine": ["base a41b7b50 (par le programme de la v68)", "v68", "lot 2 v5", "lot 3 v3", "lot 4 v1",
                                "lot 4 v3", "lot 5 v1", "lot 10 a", "lot 6 v3", "lot 6 v5 (ce paquet, lot 5 v3 compris)"],
         "fichiers": fichiers}
    chemin = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-6-v5.json")
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(chemin)


if __name__ == "__main__":
    principal()
