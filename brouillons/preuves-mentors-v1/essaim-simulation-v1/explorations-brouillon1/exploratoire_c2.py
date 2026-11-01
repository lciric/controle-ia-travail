"""Exploratoire 2, données jetables (graine 16180), tailles voisines mais hors grille."""
import time, math
import numpy as np
from controle_ia.simulation_essaim import statistiques as S, calibrage as C, menaces as M
g = np.random.default_rng(np.random.SeedSequence(16180))
q, a = 0.1, 0.05
u = C.seuil_par_case(q)
t0 = time.time()
for K, T in [(5, 36), (10, 22), (20, 22)]:
    p = {'u': u, 'q': q, 'fractions': S.FRACTIONS_LAMBDA, 'rho': C.rho_e_pas(K, T, a)}
    s = C.seuils_exacts(K, T, q, a)
    Yc = g.standard_normal((30000, K, T))
    for k, f in (('e_coelev', S.e_coelev), ('ed_coelev', S.ed_coelev)):
        s[k] = C.seuil_mc(f(Yc, u, q), a)
    s['coelev_somme3'] = C.seuil_mc(S.coelev_somme(Yc), a)
    R = 8000
    for nom, f in [('honnete', lambda Y: Y), ('relais', lambda Y: M.routage(Y, T, K, g)),
                   ('synchro_mK/2', lambda Y: M.synchro(Y, math.ceil(K / 2), 1, g)[0]), ('synchro_mK', lambda Y: M.synchro(Y, K, 1, g)[0])]:
        Y = g.standard_normal((R, K, T)); U = g.random(R)
        X = f(Y)
        v = S.calculer(X, ['agent_moyenne', 'agent_comptage', 'e_coelev', 'ed_coelev', 'coelev_somme3', 'pas_moyenne'], p)
        print(K, T, nom, {k: round(float(C.alarme(v[k], U, s[k]).mean()), 4) for k in v},
              'Ville', round(float((v['e_coelev'] >= math.log(20)).mean()), 4))
print('durée', round(time.time() - t0, 1), 's')
