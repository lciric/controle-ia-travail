"""Tables du rapport (matrices CSV, tableau par item) depuis resultats-appariement-v3.json — v1.
Usage : python3 -I tables_rapport_v1.py DOSSIER
"""
import json
import sys
from pathlib import Path

import numpy as np

d = Path(sys.argv[1])
r = json.loads((d / "resultats-appariement-v3.json").read_text())
m = r["matrices_liste_n200_0_30"]
for nom in ("c2a_neutre", "c2b_neutre"):
    R = np.array(m[nom]["matrice"])
    lignes = ["texte\\item," + ",".join(str(j) for j in range(30))]
    for i in range(30):
        lignes.append(f"{i}," + ",".join(f"{x:.4f}" for x in R[i]))
    (d / f"matrice-{nom}-v1.csv").write_text("\n".join(lignes) + "\n")

out = ["| item | diag c2a | meilleur hors-diag ligne (item) | marge ligne | marge colonne | diag c2b | marge ligne | marge colonne |",
       "|---|---|---|---|---|---|---|---|"]
for i in range(30):
    Ra, Rb = np.array(m["c2a_neutre"]["matrice"]), np.array(m["c2b_neutre"]["matrice"])
    hors = [(j, Ra[i, j]) for j in range(30) if j != i]
    jb, vb = max(hors, key=lambda x: x[1])
    out.append(f"| {i} | {Ra[i, i]:.3f} | {vb:.3f} ({jb}) | {m['c2a_neutre']['marges_lignes'][i]:+.3f} | "
               f"{m['c2a_neutre']['marges_colonnes'][i]:+.3f} | {Rb[i, i]:.3f} | "
               f"{m['c2b_neutre']['marges_lignes'][i]:+.3f} | {m['c2b_neutre']['marges_colonnes'][i]:+.3f} |")
(d / "tableau-par-item-v1.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
for nom in ("c2a_neutre", "c2b_neutre"):
    R = np.array(m[nom]["matrice"])
    print(nom)
    for i in range(30):
        print(f"{i:2d} " + " ".join(f"{int(round(100 * x)):2d}" for x in R[i]))
