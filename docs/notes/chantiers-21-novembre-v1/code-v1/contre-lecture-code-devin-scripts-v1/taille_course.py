import sys, time, numpy as np, warnings
warnings.simplefilter("ignore")
from scipy.stats import binomtest
from controle_ia.devin_v1.graines import graine_tache
from controle_ia.devin_v1.admission import ConfigurationCourse, InventaireSimule, jouer_course
from controle_ia.devin_v1.monde_plante import Fuite
R0 = 0x5EED_0F_C0_2026_1122_ABCD_EF01_2345_6789_AB
def source(pref):
    def f(nom):
        v=int.from_bytes(graine_tache(R0, f"{pref}|{nom}").generate_state(4,dtype=np.uint32).tobytes(),"big"); return v|(1<<127)
    return f
reps=int(sys.argv[1]); devin=sys.argv[2]
lt = tuple(np.random.default_rng(graine_tache(R0,"lt")).normal(size=500))
ps=[]; pf=[]; t0=time.time()
for r in range(reps):
    c = ConfigurationCourse(devin=devin, temoin_fuite=Fuite("horodatage",1.5,"temoin"), nom=f"n{r}", n_apprentissage=100, n_epreuve=100,
        B=99, etages=("0",), cibles=("A1","A2"), lectures_temoins=lt, propension=0.3)
    s = source(f"{devin}{r}")
    v = jouer_course(c, [], InventaireSimule(k_a2=2), racine_monde=s("monde"), source_racines=s)
    ps.append(v["p"]); pf.append(v["temoin_factice_p"])
for nom, x in (("secret",ps),("factice",pf)):
    x=np.array(x); r=int((x<=0.05).sum()); ci=binomtest(r,reps).proportion_ci(0.95)
    print(devin, nom, r, reps, round(r/reps,4), round(ci.low,4), round(ci.high,4))
print("s/course", (time.time()-t0)/reps)
