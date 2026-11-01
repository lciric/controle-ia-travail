"""Exploratoire HE3, données jetables (graine 31337), tailles hors grille : taux de Ville."""
import time, math
import numpy as np
from controle_ia.simulation_essaim import statistiques as S, calibrage as C
from controle_ia.simulation_t03.lois import tirer
ss = np.random.SeedSequence(31337)
g = np.random.default_rng(ss)
q, a = 0.1, 0.05
u = C.seuil_par_case(q)
t0 = time.time()
for K, T in [(10, 24), (10, 45)]:
    p = {'u': u, 'q': q, 'fractions': S.FRACTIONS_LAMBDA, 'rho': C.rho_e_pas(K, T, a)}
    for nom, loi in [('iid', {'type': 'iid'}), ('tau0.1', {'type': 'effet_episode', 'tau': 0.1}),
                     ('tau0.2', {'type': 'effet_episode', 'tau': 0.2}), ('c0.2', {'type': 'equicorrelation', 'c': 0.2}),
                     ('c0.4', {'type': 'equicorrelation', 'c': 0.4})]:
        Y = tirer(g, 4000, {**loi, 'N': K, 'T': T})
        v = S.calculer(Y, ['e_coelev', 'e_pas'], p)
        h = math.log(20)
        print(K, T, nom, 'e_coelev_ville', round(float((v['e_coelev'] >= h).mean()), 4), 'e_pas_ville', round(float((v['e_pas'] >= h).mean()), 4))
print('durée', round(time.time() - t0, 1), 's')
