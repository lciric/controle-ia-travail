import sys, time, numpy as np, warnings
warnings.simplefilter("ignore")
from scipy.stats import binomtest
from controle_ia.devin_v1.graines import graine_tache, generateur_tache
from controle_ia.devin_v1.statistique import epreuve_globale_piece, epreuve_globale_lecture
from controle_ia.devin_v1.tirage import TireurPiece, TireurLecture, propension_constante
R0 = 0xC0FFEE_1234_5678_9ABC_DEF0_1357_9BDF_2468_ACE1
def rac(*c):
    v = int.from_bytes(graine_tache(R0, *c).generate_state(4, dtype=np.uint32).tobytes(), "big"); return v | (1<<127)
def rapport(nom, rej, n):
    ci = binomtest(rej, n).proportion_ci(0.95)
    print(f"{nom}: {rej}/{n} = {rej/n:.4f}  IC95 [{ci.low:.4f}, {ci.high:.4f}]", flush=True)
reps = 2000
# 1) famille corrélée J=12 dont 1 constant, pi = 0.05 (taux de service), n=300, B=199
tir = TireurPiece(propension_constante(0.05), False)
rej = 0
for k in range(reps):
    ids=[f"a{k}:{t}" for t in range(300)]
    j = tir.tirer(rac("p",k), ids, [{}]*300)
    g = generateur_tache(R0, f"x{k}")
    base = g.normal(size=300)
    s = base + 0.5*g.normal(size=(12,300)); s[0]=1.0; s[3] = np.round(s[3])  # constant et ex-aequo
    rej += epreuve_globale_piece(s, j, tir, rac("r",k), 199)["p"] <= 0.05
rapport("piece pi=0.05 J=12 correles", rej, reps)
# 2) propension dependant du passe, J=5
def pif(t,e,passe):
    return np.full(passe.shape[0],0.3) if passe.shape[1]==0 else np.where(passe[:,-1]==1,0.1,0.5)
tir2 = TireurPiece(pif, True, frozenset({"entrees_consignees","pieces_passees"}))
rej=0
for k in range(reps):
    ids=[f"b{k}:{t}" for t in range(150)]
    j = tir2.tirer(rac("q",k), ids, [{}]*150)
    g = generateur_tache(R0, f"y{k}")
    # predicteurs fonctions de la piece passee (correles a pi, legitimes sous le nul)
    prev = np.r_[0, j.pieces[:-1]]
    s = np.vstack([prev + 0.1*g.normal(size=150), g.normal(size=(4,150))])
    rej += epreuve_globale_piece(s, j, tir2, rac("s",k), 199)["p"] <= 0.05
rapport("piece pi dependant du passe J=5", rej, reps)
# 2b) meme chose mais rejeu INDEPENDANT a tort (propension moyenne) -> doit se biaiser (garde utile)
# 3) lecture equilibre J=6
lt = generateur_tache(R0,"lt").normal(size=500)
tl = TireurLecture(lt, "equilibre", seuil=0.0)
rej=0
for k in range(reps):
    ids=[f"c{k}:{t}" for t in range(200)]
    j = tl.tirer(rac("l",k), ids)
    s = generateur_tache(R0, f"z{k}").normal(size=(6,200))
    rej += epreuve_globale_lecture(s, j, tl, rac("m",k), 199)["p"] <= 0.05
rapport("lecture equilibre J=6", rej, reps)
