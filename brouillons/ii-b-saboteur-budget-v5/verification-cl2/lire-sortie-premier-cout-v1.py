"""Lecture, par le vérificateur, des sorties du passage du contrôle du premier coût (passage coupé + achèvement) : table de 6 bis.3."""
import sys
R = {}
for chemin in sys.argv[1:]:
    for n, l in enumerate(open(chemin, encoding="utf-8").read().split("\n")):
        c = l.split("\t")
        if len(c) == 11 and c[0].isdigit():
            R[(int(c[0]), int(c[1]), float(c[2]), float(c[3]), c[4])] = (c[5:], f"{chemin.split('/')[-1]}:{n+1}")
print("configurations lues :", len(R))
for k in (8, 16, 32):
  print(f"\n== k = {k} ; P(rangs alerte 1/20), moins favorable des formes [et l'autre] ; moyenne 1/20 ; rangs 1/40")
  for n in (32, 64, 96, 128, 384, 768):
    ligne = []
    for pa in (1.0, 0.5):
        for dl in (0.0, 0.2, 0.301, 0.5, 1.0, 0.05, 0.1, 0.15):
            if dl == 0 and pa != 1.0: continue
            v = [(float(R[(n, k, dl, pa, fo)][0][1]), fo, float(R[(n,k,dl,pa,fo)][0][4]), float(R[(n,k,dl,pa,fo)][0][2]), R[(n,k,dl,pa,fo)][1]) for fo in ("arrondi a la grille", "tel quel") if (n, k, dl, pa, fo) in R]
            m = min(v)
            ligne.append(f"d{dl:g}/p{pa:g}:{m[0]:.3f}({m[1][:3]};moy {m[2]:.3f};1/40 {m[3]:.3f};{m[4]})" + (f"[{max(v)[0]:.3f}]" if len(v) > 1 else ""))
    print(n, " | ".join(ligne))
