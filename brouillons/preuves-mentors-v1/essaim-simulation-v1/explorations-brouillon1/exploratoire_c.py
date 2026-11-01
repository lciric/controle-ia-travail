"""Exploratoire classe C, données jetables (graine 27182), tailles hors grille."""
import time, math
import numpy as np
from controle_ia.simulation_essaim import statistiques as S, calibrage as C, menaces as M
g = np.random.default_rng(np.random.SeedSequence(27182))
q, a = 0.1, 0.05
u = C.seuil_par_case(q)
t0 = time.time()
for K, T in [(6, 32), (12, 16), (16, 24)]:
    p = {'u': u, 'q': q, 'fractions': S.FRACTIONS_LAMBDA, 'rho': C.rho_e_pas(K, T, a)}
    s = C.seuils_exacts(K, T, q, a)
    Yc = g.standard_normal((20000, K, T))
    s['coelev_somme3'] = C.seuil_mc(S.coelev_somme(Yc), a)
    s['ed_coelev'] = C.seuil_mc(S.ed_coelev(Yc, u, q), a)
    s['e_coelev'] = C.seuil_mc(S.e_coelev(Yc, u, q), a)
    def taux(X, U):
        v = S.calculer(X, ['agent_moyenne', 'agent_comptage', 'pas_moyenne', 'coelev_comptage', 'coelev_somme3', 'ed_coelev', 'e_coelev'], p)
        return {k: round(float(C.alarme(v[k], U, s[k]).mean()), 3) for k in v}
    R = 4000
    for nom, f in [('honnete', lambda Y: Y), ('routage_T/4', lambda Y: M.routage(Y, T // 4, 1, g)),
                   ('routage_T', lambda Y: M.routage(Y, T, 1, g)), ('relais', lambda Y: M.routage(Y, T, K, g)),
                   ('synchro_m2', lambda Y: M.synchro(Y, 2, 1, g)[0]), ('synchro_mK/2', lambda Y: M.synchro(Y, math.ceil(K / 2), 1, g)[0]),
                   ('synchro_mK', lambda Y: M.synchro(Y, K, 1, g)[0])]:
        Y = g.standard_normal((R, K, T)); U = g.random(R)
        print(K, T, nom, taux(f(Y), U))
print('durée', round(time.time() - t0, 1), 's')
