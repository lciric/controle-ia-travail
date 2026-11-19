"""Résumé par programme du passage du contrôle du premier coût (sortie du passage et de son achèvement, mises bout à bout)."""
import sys
R = []
for f in sys.argv[1:]:
    for l in open(f, encoding="utf-8").read().split("\n"):
        c = l.split("\t")
        if len(c) == 11 and c[0].isdigit():
            R.append(dict(n=int(c[0]), k=int(c[1]), d=float(c[2]), part=float(c[3]), forme=c[4], score=float(c[5]), r20=float(c[6]), r40=float(c[7]), rh=float(c[8]), m20=float(c[9]), mh=float(c[10])))
print("configurations lues :", len(R))
g = lambda n, k, d, part, forme: [r for r in R if r["n"] == n and r["k"] == k and abs(r["d"] - d) < 1e-9 and r["part"] == part and r["forme"] == forme][0]
NS, KS = (32, 64, 96, 128, 384, 768), (8, 16, 32)
DS = (0.05, 0.10, 0.15, 0.20, 0.301, 0.5, 1.0)
F = ("arrondi a la grille", "tel quel")
print("\n== alerte a tort (gonflement nul), rangs 1/20 ; rangs 1/40 ; moyenne 1/20")
for k in KS:
    print(f"  {k} suites : " + " ; ".join(f"n {n}: {g(n,k,0,1.0,F[0])['r20']:.3f} {g(n,k,0,1.0,F[0])['r40']:.3f} {g(n,k,0,1.0,F[0])['m20']:.3f}" for n in NS))
for part in (1.0, 0.5):
    for forme in F:
        for k in KS:
            print(f"\n== P(alerte des rangs, 1/20), part gonflee {part}, forme « {forme} », {k} suites (lignes : episodes ; colonnes : gonflement {DS})")
            for n in NS:
                print(f"  n {n:3d} : " + "  ".join(f"{g(n,k,d,part,forme)['r20']:.3f}" for d in DS) + "   | moyenne : " + "  ".join(f"{g(n,k,d,part,forme)['m20']:.3f}" for d in DS)
                      + "   | rangs 1/40 : " + "  ".join(f"{g(n,k,d,part,forme)['r40']:.3f}" for d in DS))
print("\n== plus petit gonflement vu au moins 80 fois sur 100 (rangs, 1/20, tous les episodes gonfles, forme la moins favorable), par nombre de suites")
for k in KS:
    out = []
    for n in NS:
        vus = [d for d in DS if min(g(n, k, d, 1.0, f)["r20"] for f in F) >= 0.8]
        ok = [d for d in DS if all(min(g(n, k, d2, 1.0, f)["r20"] for f in F) >= 0.8 for d2 in DS if d2 >= d)]
        out.append(f"n {n}: {min(ok) if ok else 'aucun'}" + (f" (proba {min(g(n,k,min(ok),1.0,f)['r20'] for f in F):.3f})" if ok else ""))
    print(f"  {k} suites : " + " ; ".join(out))
print("\n== idem, moitie des episodes gonfles")
for k in KS:
    out = []
    for n in NS:
        ok = [d for d in DS if all(min(g(n, k, d2, 0.5, f)["r20"] for f in F) >= 0.8 for d2 in DS if d2 >= d)]
        out.append(f"n {n}: {min(ok) if ok else 'aucun'}" + (f" (proba {min(g(n,k,min(ok),0.5,f)['r20'] for f in F):.3f})" if ok else ""))
    print(f"  {k} suites : " + " ; ".join(out))
