"""VF3 : motif de l'échec de A1 T4 dans le second run (le nombre de tirages dégénérés n'est que dans le motif)."""
from commun import P, cp, lecture_decisive, run_synthetique
from controle_ia.manifeste import graines
src = run_synthetique(0, bizarres=("temoin", "mention"))
s = cp.analyser_addendum(src, lecture_decisive(src), graines(cp.cles_addendum(P), cp.ENTROPIE_P3))
for p in P:
    print(p, s["analyses"]["A1"][p]["descriptif"]["T4"], s["analyses"]["A1"][p]["etat"],
          [c for c in s["analyses"]["A1"][p]["controles"] if c["test"] == "T4"])
