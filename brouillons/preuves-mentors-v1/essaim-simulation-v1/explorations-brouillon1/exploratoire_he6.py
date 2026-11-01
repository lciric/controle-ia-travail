"""Exploratoire HE6, données jetables (graine 14142), taille hors grille 10 x 22."""
import time
import numpy as np
from controle_ia.simulation_essaim import statistiques as S, calibrage as C, menaces as M
from controle_ia.simulation_t03.lois import tirer
g = np.random.default_rng(np.random.SeedSequence(14142))
q, a = 0.1, 0.05
u = C.seuil_par_case(q)
K, T = 10, 22
p = {'u': u, 'q': q, 'fractions': S.FRACTIONS_LAMBDA, 'rho': C.rho_e_pas(K, T, a)}
noms = ['agent_moyenne', 'agent_comptage', 'pas_moyenne', 'coelev_comptage', 'coelev_somme3', 'e_coelev', 'ed_coelev']
t0 = time.time()
for c in (0.2, 0.4):
    loi = {'type': 'equicorrelation', 'c': c, 'N': K, 'T': T}
    vc = S.calculer(tirer(g, 30000, loi), noms, p)
    s = {k: C.seuil_mc(vc[k], a) for k in noms}
    for nom, f in [('honnete', lambda Y: Y), ('m5', lambda Y: M.synchro(Y, 5, 1, g)[0]), ('m10', lambda Y: M.synchro(Y, 10, 1, g)[0])]:
        Y = tirer(g, 8000, loi); U = g.random(8000)
        v = S.calculer(f(Y), noms, p)
        print('c', c, nom, {k: round(float(C.alarme(v[k], U, s[k]).mean()), 3) for k in noms})
print('durée', round(time.time() - t0, 1), 's')
