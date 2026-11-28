import sys, time, json, cProfile, pstats
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "..")
from test_premier_test_ia_lecture import _source, _graines, P
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.manifeste import graines
import complements_p3_v1 as A
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
A.TIRAGES_AIRE, A.TIRAGES_COUT = 200, 1000
src = _source(0)
src["tables"]["valide"][:] = True
lec = lp.lire(src, _graines())
g = graines(A.cles_addendum(P), A.ENTROPIE_P3)
for a in A.ANALYSES:
    D = A._preparer(src, lec); C = A.conclusions_de_la_lecture(lec, P)
    t = time.time()
    if a in A.ANALYSES_GLOBALES: A._executer(a, D, C, g, None, None)
    else:
        for k, p in enumerate(P): A._executer(a, D, C, g, k, p)
    print(a, round(time.time() - t, 2))
D = A._preparer(src, lec); C = A.conclusions_de_la_lecture(lec, P)
cProfile.run("A._executer('A1', D, C, g, 0, P[0])", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/candidat-a/essais/prof.out")
pstats.Stats("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/candidat-a/essais/prof.out").sort_stats("cumtime").print_stats(15)
