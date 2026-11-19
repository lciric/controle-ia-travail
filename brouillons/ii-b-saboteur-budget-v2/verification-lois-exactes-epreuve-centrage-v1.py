"""Vérification des lois exactes de l'épreuve du centrage révisée contre l'approximation normale de la simulation — v1.

Reprend le bloc E de `simulation-chaine-oracle-revise-ii-b-v1.py`, dont le calcul passait par le logarithme des fonctions
caractéristiques : il a émis des avertissements (logarithme de zéro), et un essai dont la loi contiendrait une valeur non
définie n'aurait pas été compté dans l'écart maximal (défaut de la vérification, pas de l'épreuve). Ici la loi exacte est le
produit direct des fonctions caractéristiques (aucun logarithme), les valeurs non définies sont comptées, et la somme de la
loi est contrôlée. S'y ajoute la loi exacte de la composante « lisibilité » (somme de Bernoulli indépendantes).
Aucune donnée du programme ; numpy seul ; entropie tirée une fois et écrite.
"""
import importlib.util
import math
import sys

import numpy as np

sp = importlib.util.spec_from_file_location("sim", sys.argv[1])
sim = importlib.util.module_from_spec(sp)
sp.loader.exec_module(sim)
A = 1.0 / 60.0


def p_exacte_strates(noyaux, observe):
    groupes = {}
    for nq in noyaux:
        groupes[nq] = groupes.get(nq, 0) + 1
    portee = sum(max(abs(v) for v in nq) * m for nq, m in groupes.items())
    M = 1 << int(math.ceil(math.log2(2 * portee + 2)))
    w = 2 * np.pi * np.fft.fftfreq(M)
    prod = np.ones(M, dtype=complex)
    for nq, m in groupes.items():
        vals, cnt = np.unique(np.array(nq), return_counts=True)
        phi = sum(cn * np.exp(1j * w * v) for v, cn in zip(vals, cnt)) / len(nq)
        prod *= phi ** m
    loi = np.real(np.fft.ifft(prod))
    s = np.fft.fftfreq(M, 1.0 / M).astype(int)
    return float(loi[np.abs(s) >= abs(observe)].sum()), float(loi.sum())


ss = np.random.SeedSequence()
print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; niveau {A:.6f}")
rng = np.random.default_rng(ss)
for rond, essais in (("aucun", 40), ("1-2-5", 16)):
    dmax, disc, nan, smax = 0.0, 0, 0, 0.0
    for _ in range(essais):
        noyaux, obs, var = [], 0, 0.0
        for _a in range(640):
            k1 = int(rng.integers(sim.K_MIN + 1, sim.K + 2))
            v = sim.arrondir(sim.MU0 + 0.3 * rng.standard_normal(k1), rond)
            moins = (v[None, :] < v[:, None]).sum(axis=1)
            egal = (v[None, :] == v[:, None]).sum(axis=1)
            num = np.rint(2 * (moins + (egal + 1) / 2.0) - (k1 + 1)).astype(int) * (1008 // (2 * k1))
            noyaux.append(tuple(sorted(int(u) for u in num)))
            obs += int(num[0])
            var += float((num.astype(float) ** 2).mean())
        (pe, somme), pn = p_exacte_strates(noyaux, obs), sim.p_normale(obs / math.sqrt(var))
        if not math.isfinite(pe):
            nan += 1
            continue
        dmax, smax = max(dmax, abs(pe - pn)), max(smax, abs(somme - 1.0))
        disc += int((pe < A) != (pn < A))
    print(f"rangs stratifies\trond={rond}\tessais={essais}\tnon_definis={nan}\tecart_max_p={dmax:.6f}\tecart_max_somme_loi={smax:.2e}\tdecisions_discordantes={disc}")
for u in (0.10, 0.30):
    dmax, disc, nan, smax = 0.0, 0, 0, 0.0
    for _ in range(40):
        L = rng.random((640, sim.K + 1)) >= u
        m = L.sum(axis=1)
        # score entier : (K + 1)·L0 − m ; noyau : m fois (K + 1 − m), (K + 1 − m) fois (−m)
        noyaux = [tuple(sorted([sim.K + 1 - int(mm)] * int(mm) + [-int(mm)] * (sim.K + 1 - int(mm)))) for mm in m]
        obs = int(((sim.K + 1) * L[:, 0] - m).sum())
        var = float((m * (sim.K + 1 - m)).sum())
        (pe, somme), pn = p_exacte_strates(noyaux, obs), sim.p_normale(obs / math.sqrt(var))
        if not math.isfinite(pe):
            nan += 1
            continue
        dmax, smax = max(dmax, abs(pe - pn)), max(smax, abs(somme - 1.0))
        disc += int((pe < A) != (pn < A))
    print(f"lisibilite\tpart_illisible={u}\tessais=40\tnon_definis={nan}\tecart_max_p={dmax:.6f}\tecart_max_somme_loi={smax:.2e}\tdecisions_discordantes={disc}")
for n_u in (32, 64):
    dmax, disc, rej_e, rej_n = 0.0, 0, 0, 0
    for _ in range(2000):
        x = rng.standard_normal(n_u)
        z, _n = sim.rangs_signes(x[None, :])
        pe, pn = sim.p_exacte_rangs_signes(x), sim.p_normale(float(z[0]))
        dmax = max(dmax, abs(pe - pn))
        disc += int((pe < A) != (pn < A))
        rej_e += int(pe < A)
        rej_n += int(pn < A)
    print(f"rangs signes\tunites={n_u}\tessais=2000\tecart_max_p={dmax:.6f}\tdecisions_discordantes={disc}\trejets_exact={rej_e}\trejets_normale={rej_n}")
