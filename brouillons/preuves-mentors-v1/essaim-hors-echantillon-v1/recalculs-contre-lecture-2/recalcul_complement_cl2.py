"""Complément : m = K à e10x10 et m = 8 à e20x10 par la même programmation dynamique sur les pas ; comparaison à
10 chiffres avec `bornes_synchro_v2.puissance_exacte` (module de l'auteur, sans tirage)."""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/cl2-recalculs")
from recalcul_puissance_exacte_cl2 import puissance, seuil_exact
sys.path.insert(0, "/home/claude/controle-ia-travail/src")
from controle_ia.simulation_essaim import bornes_synchro_v2 as BS2
for K, T, m in ((10, 10, 3), (10, 10, 5), (10, 10, 7), (20, 10, 6), (10, 10, 10), (20, 10, 8)):
    s = seuil_exact(K, T)
    v = puissance(K, T, m, s)
    a, e = BS2.puissance_exacte(K, T, m, 0.1, s)
    print(f"e{K}x{T} m = {m} : DP pas {v:.10f} ; auteur {a:.10f} (erreur certifiée {e:.1e}) ; écart {abs(v - a):.1e}", flush=True)
