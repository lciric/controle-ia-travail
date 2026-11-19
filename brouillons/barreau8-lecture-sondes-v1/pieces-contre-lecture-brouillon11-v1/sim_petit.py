"""Réplique à tailles réduites (20 tâches, 3 pas, 20 directions, 400 tirages) du montage de sim_a0 :
vérifie que le modèle synthétique reproduit l'échec vu par la contre-lecture du code de la lecture sous (R).
Sous (A), avec 3 pas, une ou deux actions par tâche (tirage d'une permutation, premières floor(3/2)=1) sont étiquetées."""
import sys
import numpy as np
sys.argv = [sys.argv[0]]
import importlib.util
spec = importlib.util.spec_from_file_location("sim_a0", __file__.replace("sim_petit.py", "sim_a0.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.T, m.A, m.NDIR, m.B = 20, 3, 20, 400
m.main(40, sigmas=(1.0, 2.0, 4.0, 8.0))
