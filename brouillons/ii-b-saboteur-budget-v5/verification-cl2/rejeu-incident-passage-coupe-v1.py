"""Rejeu, par le vérificateur, de l'incident du passage coupé du contrôle du premier coût : deux configurations rejouées avec
leur graine fille (entropie lue en tête de la sortie du passage), l'une parmi les 389 premières, l'autre parmi les 133 de
l'achèvement ; la ligne rejouée doit être égale, caractère pour caractère, à la ligne versée. Le script du rédacteur est
exécuté sans son bloc principal (fonctions et constantes seulement)."""
import sys
import numpy as np
script, sortie, achevement = sys.argv[1:4]
M = {"__name__": "rejeu"}
exec(compile(open(script).read(), script, "exec"), M)
entropie = int(open(sortie, encoding="utf-8").readline().split(":")[1])
conf = [(n, k, dl, pa, fo) for fo in M["FORMES"] for pa in M["PARTS"] for k in M["KS"] for n in M["NS"] for dl in M["DELTAS"]
        if not (dl == 0 and (pa != 1.0 or fo != M["FORMES"][0]))]
graines = np.random.SeedSequence(entropie).spawn(len(conf))
versees = {}
for chemin in (sortie, achevement):
    for num, l in enumerate(open(chemin, encoding="utf-8").read().split("\n")):
        c = l.split("\t")
        if len(c) == 11 and c[0].isdigit():
            versees[(int(c[0]), int(c[1]), float(c[2]), float(c[3]), c[4])] = (l, f"{chemin.split('/')[-1]}:{num + 1}")
print(f"entropie {entropie} ; configurations {len(conf)} ; lignes versees {len(versees)} ; numpy {np.__version__}")
ordre_ok = all(conf[i] in versees for i in range(len(conf)))
print("toutes les configurations ont une ligne versee :", ordre_ok)
NIV = M["NIVEAUX"]
for i in [int(x) for x in sys.argv[4:]]:
    n, k, dl, pa, fo = conf[i]
    rng = np.random.default_rng(graines[i])
    zs, ts, sc, fait = [], [], [], 0
    while fait < M["N_REP"]:
        rep = min(M["N_REP"] - fait, max(1, int(2e6 // (n * (k + 1) ** 2))))
        z, t, s_ = M["groupe"](rng, n, k, dl, pa, fo, rep)
        zs.append(z); ts.append(t); sc.append(s_); fait += rep
    z, t = np.concatenate(zs), np.concatenate(ts)
    ligne = "\t".join([str(n), str(k), f"{dl:g}", f"{pa:g}", fo, f"{np.mean(sc):+.4f}", f"{(np.abs(z) > NIV['1/20']).mean():.3f}", f"{(np.abs(z) > NIV['1/40']).mean():.3f}",
                       f"{(z > NIV['1/20']).mean():.3f}", f"{(np.abs(t) > NIV['1/20']).mean():.3f}", f"{(t > NIV['1/20']).mean():.3f}"])
    v, ou = versees[conf[i]]
    print(f"configuration {i} {conf[i]} ({'389 premieres' if i < 389 else 'achevement'}) ; versee a {ou}")
    print("  rejouee :", ligne)
    print("  versee  :", v)
    print("  egales :", ligne == v)
