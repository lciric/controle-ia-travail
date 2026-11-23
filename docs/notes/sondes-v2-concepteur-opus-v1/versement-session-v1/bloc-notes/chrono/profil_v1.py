"""Profil d'une réplique du mode complet : temps par fonction SEULEMENT, aucune lecture imprimée."""
import sys, os, cProfile, pstats, io, tempfile
sys.path.insert(0, os.environ["DEPOT"] + "/src")
from controle_ia.sondes_v2 import monde_plante_v3 as mp, statistiques_v1 as st
from controle_ia.sondes_v2.formes_closes_v1 import threadpool_limits
monde = sys.argv[1]; P, T, A = (int(x) for x in sys.argv[2].split(","))
v, _ = mp.charger_verites()
p = mp.parametres(v, monde, P, 1, T, A, 256, "complet")
with tempfile.TemporaryDirectory() as tmp, threadpool_limits(1):
    _, rngs = st.generateurs_nommes(777, f"profil/{monde}/")
    pr = cProfile.Profile(); pr.enable()
    _ = mp.lire_monde(p, rngs, os.path.join(tmp, "j.jsonl"), "x", {"alpha": 0.05, "u_fort": 0.9}, 199, 2000)
    pr.disable(); del _
s = io.StringIO(); pstats.Stats(pr, stream=s).sort_stats("cumulative").print_stats(28)
print("\n".join(l for l in s.getvalue().splitlines() if "sondes_v2" in l or "function calls" in l or "cumtime" in l))
