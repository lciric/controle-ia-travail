"""Lecture, par le vérificateur, de la sortie du passage « épreuve de fuite, deux lectures, règle composée » : agrégats cités par le brouillon 3."""
import sys, numpy as np
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
iA = next(i for i,l in enumerate(L) if l.startswith("# A.")); iV = next(i for i,l in enumerate(L) if l.startswith("# V.")); iD = next(i for i,l in enumerate(L) if l.startswith("# D."))
iE = next(i for i,l in enumerate(L) if l.startswith("# ERREURS"))
hA = L[iA+1].split("\t"); A = [l.split("\t") for l in L[iA+2:iV] if l.strip()]
hD = L[iD+1].split("\t"); D = [(n+iD+2, l.split("\t")) for n,l in enumerate(L[iD+2:iE]) if l.strip()]
print("A colonnes:", hA)
for r in A:
    if r[0]=="0.8" and r[1]=="0.08" and r[2]=="0.9": print("A point situe:", r)
print("D colonnes:", list(enumerate(hD)))
lects = sorted({r[3] for _,r in D})
for lec in lects:
    S = [r for _,r in D if r[3]==lec and r[4]=="sain"]
    f = lambda j, sel=S: np.mean([float(r[j]) for r in sel])
    print(f"\n[{lec}] sain {len(S)} cellules : arret composantes 1/80", [round(f(j),4) for j in range(5,9)], "arretN4", round(f(9),4), "min/max", min(float(r[9]) for r in S), max(float(r[9]) for r in S),
          "b2", round(f(10),4), "quatre 1/60", round(f(11),4), "arretP", round(f(12),4))
    print("  pente fuite: arret moy", round(f(8),4), "min/max", min(float(r[8]) for r in S), max(float(r[8]) for r in S), "pente sd", [r[14] for r in S][:3])
    print("  condN", round(f(16),4), "condP", round(f(17),4), "issueN", round(f(18),4), "issueP", round(f(19),4), "ne part pas", round(f(20),4))
    for rho in ("0.7","0.9","1.0"):
        for s1 in ("0.05","0.08","0.12"):
            sel=[r for r in S if r[2]==rho and r[1]==s1]
            print(f"   ancrage {rho} s1 {s1}: condN {f(16,sel):.3f} issueN {f(18,sel):.3f} issueP {f(19,sel):.3f}")
    for n,r in D:
        if r[3]==lec and r[0]=="0.8" and r[1]=="0.08" and r[2]=="0.9" and r[4]=="sain": print("  ligne", n+1, "point situe sain:", r[16:25])
for etat in sorted({r[4] for _,r in D}):
    S = [r for _,r in D if r[4]==etat]
    print(f"etat {etat}: n {len(S)} pente moy {np.mean([float(r[13]) for r in S]):.3f} arret fuite {np.mean([float(r[8]) for r in S]):.3f} [{min(float(r[8]) for r in S)}, {max(float(r[8]) for r in S)}] arretN4 {np.mean([float(r[9]) for r in S]):.3f} [{min(float(r[9]) for r in S)},{max(float(r[9]) for r in S)}] condN {np.mean([float(r[16]) for r in S]):.3f} issueP {np.mean([float(r[19]) for r in S]):.3f}")
    for lec in lects:
        S2=[r for r in S if r[3]==lec]
        print(f"    {lec}: arretN4 {np.mean([float(r[9]) for r in S2]):.3f} [{min(float(r[9]) for r in S2)},{max(float(r[9]) for r in S2)}] fuite {np.mean([float(r[8]) for r in S2]):.3f} [{min(float(r[8]) for r in S2)},{max(float(r[8]) for r in S2)}]")
