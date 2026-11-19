"""Contre-lecteur Opus 5.5 : le module préparé `statistiques_v2` (commit e2e24cac) contre un calcul direct, direction par direction,
sur les M − 1 autres (moyenne, écart type de population, quantile 0,99 par interpolation linéaire numpy sur M − 1 valeurs), y
compris avec des égalités ; arrêts ; quantile des M pour v égal à numpy « linear ». Aucune donnée réelle."""
import sys

import numpy as np
import torch

sys.path.insert(0, sys.argv[1])
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as s1  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v2 as s2  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

g = np.random.default_rng(int(sys.argv[2]))


def direct(y, k=20):
    T, M = y.shape
    C = np.empty(M); P = np.empty(M)
    for j in range(M):
        autres = np.delete(y, j, axis=1).astype(np.float64)
        m, s = autres.mean(1), autres.std(1)
        C[j] = ((y[:, j] - m) / s).max()
        q = np.quantile(autres, 0.99, axis=1, method="linear")
        top = np.argsort(-y[:, j], kind="stable")[:k]
        P[j] = (y[top, j] > q[top]).mean()
    return C, P


pires = []
for (T, M, egalites) in [(64, 3, False), (64, 5, False), (300, 19, False), (500, 101, False), (500, 101, True), (2000, 40, True)]:
    y = g.standard_normal((T, M)).astype(np.float32)
    if egalites:
        y = np.round(y * 4) / 4                                           # beaucoup d'égalités
        y[:, 1] = y[:, 0]                                                 # deux directions identiques
    t = torch.from_numpy(y)
    r = s2.resumer_nul(t, {})
    C, P = direct(y, min(20, T))
    dC = np.abs(r.concentration.numpy().astype(np.float64) - C).max()
    dP = np.abs(r.part.numpy() - P).max()
    # quantile des M pour v et les témoins : torch.quantile « linear » contre numpy
    dq = np.abs(r.quantile.numpy() - np.quantile(y.astype(np.float64), 0.99, axis=1)).max()
    # statistique d'origine : plus petite (concentration), part ≤
    r1 = s1.resumer_nul(t, {})
    plus_petite = bool((r1.concentration < r.concentration).all())
    pires.append((T, M, egalites, dC, dP, dq, plus_petite))
    print(f"T={T} M={M} égalités={egalites} : |ΔC|max={dC:.2e} ; |ΔP|max={dP:.2e} ; |Δq(M)|max={dq:.2e} ; "
          f"origine strictement plus petite : {plus_petite} ; max d d'origine min = {float(r1.concentration.min()):.3f}")

# arrêts
for nom, y in [("deux directions", g.standard_normal((10, 2)).astype(np.float32)),
               ("jeton constant sur les autres", np.vstack([g.standard_normal((9, 6)), np.r_[5.0, [1.0] * 5][None, :]]).astype(np.float32))]:
    try:
        s2.resumer_nul(torch.from_numpy(y), {})
        print(f"arrêt « {nom} » : AUCUN ARRÊT")
    except Arret as e:
        print(f"arrêt « {nom} » : arrêt ({str(e)[:70]}…)")
# bord du seuil : autres presque constants (variance relative 1e-12 puis 1e-6)
for eps in (1e-6, 1e-3):
    y = np.ones((4, 6), dtype=np.float64)
    y[:, 0] = 10.0
    y[:, 1:] += eps * g.standard_normal((4, 5))
    try:
        r = s2.resumer_nul(torch.from_numpy(y.astype(np.float32)), {})
        print(f"autres de dispersion {eps:g} (simple précision) : pas d'arrêt ; C(u_0) = {float(r.concentration[0]):.3e}")
    except Arret as e:
        print(f"autres de dispersion {eps:g} (simple précision) : arrêt ({str(e)[:60]}…)")
