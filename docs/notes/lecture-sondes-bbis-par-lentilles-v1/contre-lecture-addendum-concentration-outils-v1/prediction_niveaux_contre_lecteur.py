"""Contre-lecteur Opus 5.5 : prédiction au premier ordre du terme de couplage (§ 6 (d) de l'addendum) aux niveaux 0,05, 0,01 et
0,001, T = 8 192 jetons, M infini, lois gaussiennes corrélées. Réemploie `couplage_contre_lecteur.py`.
Usage : python -I -B prediction_niveaux_contre_lecteur.py ENTROPIE"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import couplage_contre_lecteur as c  # noqa: E402

E2 = int(sys.argv[1])
T = 8192
print(f"partie P par niveau (0,05 ; 0,01 ; 0,001), T = 8 192, n = 300 000 ; entropie {E2} ; numpy {np.__version__}")
for idx, sc in enumerate(('equi-0.3', 'blocs-0.6', 'equi-0.9')):
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E2, spawn_key=(4 * 10**6 + idx,))))
    ch = c.charge(sc, T, np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E2, spawn_key=(10**6,)))))
    Cs, Ds = [], []
    for _ in range(300):
        a = c.tirer(g, 1000, T, ch)
        C = a.max(1)
        Cs.append(C)
        Ds.append((C[:, None] * (a * a - 1) / 2 + a).mean(1))
    C, D = np.concatenate(Cs), np.concatenate(Ds)
    out = []
    for al in (0.05, 0.01, 0.001):
        q = np.quantile(C, 1 - al)
        lar = 0.05 * C.std()
        fen = np.abs(C - q) < lar
        h = fen.mean() / (2 * lar) / al
        ed = D[fen].mean()
        et = D[fen].std() / np.sqrt(fen.sum())
        out.append(f'niveau {al}: q={q:.2f} h={h:.2f} E[Md]={ed:+.2f}±{et:.2f} prédit {-h*ed:+.1f}/M ({-h*ed/20:+.2f} % à M=2000)')
    print(sc, ' ; '.join(out))
