import sys, time, json
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "..")
import numpy as np
from test_premier_test_ia_lecture import _source, _graines, P
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.manifeste import graines
import complements_p3_v1 as A
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
A.TIRAGES_AIRE, A.TIRAGES_COUT = 200, 1000
src = _source(0)
src["tables"]["valide"][:] = True
t = time.time(); lec = lp.lire(src, _graines()); print("lecture", time.time() - t)
g = graines(A.cles_addendum(P), A.ENTROPIE_P3)
t = time.time(); s = A.analyser_addendum(src, lec, g); print("addendum", time.time() - t)
for a in A.ANALYSES:
    x = s["analyses"][a]
    ents = [x] if a in A.ANALYSES_GLOBALES else list(x.values())
    for e in ents:
        print(a, e["statut"], e["motif"], {k: v["statut"] for k, v in e["descriptif"]["controles"].items()}, [r["reserve"] for r in e["reserves"]])
print(json.dumps(s["recommandation_au_verdict_R13"], ensure_ascii=False, indent=1))
print(s["issue_primaire_inchangee"]["ligne"])
