"""Resume des sorties de V1 : par case, taux de « etablie » de la lecture jointe du texte (conj3) et seuil de la clause de
repli (0,05 + 2 racine(0,05 x 0,95 / R)) ; cases au-dessus marquees « > ». Aussi conj2 et la lecture rr seule.
Usage : python3 -B resume_v1_v1.py DOSSIER
"""
import math
import os
import re
import sys

COLS = ["C-P3a", "C-P3b", "C-P3c 4 (bruit)", "C-P3c 3 (bruit)", "C-P3c 4 (par.)", "C-P3c 3 (par.)"]


def lire(chemin):
    txt = open(chemin, encoding="utf-8").read()
    m = re.search(r"R = (\d+) ;", txt)
    if not m:
        return None
    R = int(m.group(1))
    lignes = {}
    for ligne in txt.splitlines():
        for r in ("cal", "brut", "rr", "conj2", "conj3"):
            if ligne.startswith(r + " ") or ligne.startswith(r + "\t") or ligne.startswith(f"{r:5s}   |"):
                vals = [float(x.split("±")[0]) for x in ligne.split("|")[1:]]
                lignes[r] = vals
    return R, lignes


def main():
    d = sys.argv[1]
    fichiers = sorted(f for f in os.listdir(d) if f.startswith("v1_") and f.endswith(".txt"))
    print("case | R | seuil | conj3 : " + " ; ".join(COLS) + " | conj2 C-P3a / C-P3b | rr seule C-P3a / C-P3b")
    depass = []
    for f in fichiers:
        res = lire(os.path.join(d, f))
        if res is None:
            print(f"{f} : incomplet")
            continue
        R, L = res
        s = 0.05 + 2 * math.sqrt(0.05 * 0.95 / R)
        cells = []
        for i, c in enumerate(COLS):
            v = L["conj3"][i]
            flag = ">" if v > s else " "
            if v > s:
                depass.append((f, c, v, s))
            cells.append(f"{v:.3f}{flag}")
        print(f"{f[3:-4]:12s} | {R} | {s:.4f} | " + " ; ".join(cells) +
              f" | {L['conj2'][0]:.3f} / {L['conj2'][1]:.3f} | {L['rr'][0]:.3f} / {L['rr'][1]:.3f}")
    print("\nCases au-dessus du seuil de la clause (lecture jointe du texte) :")
    for f, c, v, s in depass:
        print(f"  {f} : {c} {v:.3f} > {s:.4f}")
    if not depass:
        print("  aucune")
    return 0


if __name__ == "__main__":
    sys.exit(main())
