"""Achèvement du passage unique du contrôle du premier coût, coupé par la limite de durée que le rédacteur avait posée (540 s)
avant sa fin, sans qu'aucun résultat ait été lu. MÊME entropie (lue en tête de la sortie), MÊMES graines filles par
configuration, MÊME ordre : seules les configurations non écrites sont jouées. Rien n'est rejoué."""
import sys
import numpy as np
chemin, sortie = sys.argv[1], sys.argv[2]
L = open(sortie, encoding="utf-8").read().split("\n")
entropie = int(L[0].split(":")[1])
faites = sum(1 for l in L[3:] if l.count("\t") == 10)
argv = sys.argv; sys.argv = [chemin]
M = {"__name__": "achevement"}
exec(compile(open(chemin).read(), chemin, "exec"), M)
conf = [(n, k, dl, pa, fo) for fo in M["FORMES"] for pa in M["PARTS"] for k in M["KS"] for n in M["NS"] for dl in M["DELTAS"]
        if not (dl == 0 and (pa != 1.0 or fo != M["FORMES"][0]))]
graines = np.random.SeedSequence(entropie).spawn(len(conf))
print(f"# achevement : entropie {entropie} ; {faites} configurations deja ecrites sur {len(conf)} ; reprise a la suivante")
NIV = M["NIVEAUX"]
for i in range(faites, len(conf)):
    n, k, dl, pa, fo = conf[i]
    rng = np.random.default_rng(graines[i])
    zs, ts, sc, fait = [], [], [], 0
    while fait < M["N_REP"]:
        rep = min(M["N_REP"] - fait, max(1, int(2e6 // (n * (k + 1) ** 2))))
        z, t, s_ = M["groupe"](rng, n, k, dl, pa, fo, rep)
        zs.append(z); ts.append(t); sc.append(s_); fait += rep
    z, t = np.concatenate(zs), np.concatenate(ts)
    print("\t".join([str(n), str(k), f"{dl:g}", f"{pa:g}", fo, f"{np.mean(sc):+.4f}", f"{(np.abs(z) > NIV['1/20']).mean():.3f}", f"{(np.abs(z) > NIV['1/40']).mean():.3f}",
                     f"{(z > NIV['1/20']).mean():.3f}", f"{(np.abs(t) > NIV['1/20']).mean():.3f}", f"{(t > NIV['1/20']).mean():.3f}"]))
    sys.stdout.flush()
