import numpy as np, warnings
warnings.simplefilter("ignore")
from scipy.stats import binomtest
from controle_ia.devin_v1.graines import graine_tache, generateur_tache
from controle_ia.devin_v1.statistique import epreuve_globale_piece
from controle_ia.devin_v1.tirage import TireurPiece, propension_constante
R0 = 0xBADC0DE_1111_2222_3333_4444_5555_6666_7777_8
def rac(*c):
    v = int.from_bytes(graine_tache(R0, *c).generate_state(4, dtype=np.uint32).tobytes(), "big"); return v | (1<<127)
tir = TireurPiece(propension_constante(0.05), False)
reps=5000; rej=0; ps=[]
for k in range(reps):
    ids=[f"a{k}:{t}" for t in range(300)]
    j = tir.tirer(rac("p",k), ids, [{}]*300)
    g = generateur_tache(R0, f"x{k}")
    base = g.normal(size=300)
    s = base + 0.5*g.normal(size=(12,300)); s[0]=1.0; s[3]=np.round(s[3])
    p = epreuve_globale_piece(s, j, tir, rac("r",k), 199)["p"]; ps.append(p)
ps=np.array(ps)
for a in (0.01,0.05,0.1,0.2):
    r=(ps<=a).sum(); ci=binomtest(int(r),reps).proportion_ci(0.95)
    print(a, r/reps, round(ci.low,4), round(ci.high,4))
