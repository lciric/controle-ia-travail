"""Essai de la projection du gardien sur des valeurs connues, comparées à des valeurs calculées à la main (écrites ici en
littéraux, non recalculées par la même formule).

Calculs à la main :
  A : t3 = 1000 s, t_arrêt = 1600 s, n = 13, s4 = 120 000 000 o, total 648.
      durée = 600 × 648 / 12 = 600 × 54 = 32 400 s (= 9 h) ; place = 120 000 000 × 54 = 6 480 000 000 o.
  B : t3 = 0, t_arrêt = 90 s, n = 2, s4 = 1 000 o : durée = 90 × 648 / 1 = 58 320 s ; place = 648 000 o.
  C : t3 = 50, t_arrêt = 50 + 2 700 s, n = 7, s4 = 3 000 000 o : durée = 2 700 × 648 / 6 = 2 700 × 108 = 291 600 s ;
      place = 3 000 000 × 108 = 324 000 000 o.
  D : n = 1 : projection impossible ; E : n = 0 : projection impossible.
Usage : essai-projection-v1.py CHEMIN_DU_GARDIEN
"""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("gardien", sys.argv[1])
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

cas = [("A", (1000.0, 1600.0, 13, 120_000_000), (32_400.0, 6_480_000_000.0)),
       ("B", (0.0, 90.0, 2, 1_000), (58_320.0, 648_000.0)),
       ("C", (50.0, 2750.0, 7, 3_000_000), (291_600.0, 324_000_000.0)),
       ("D", (0.0, 90.0, 1, 1_000), None),
       ("E", (0.0, 90.0, 0, 0), None)]
echecs = 0
for nom, args, attendu in cas:
    p = G.projection(*args)
    obtenu = None if p is None else (p["duree_s"], p["place_octets"])
    ok = obtenu == attendu if attendu is None or obtenu is None else all(abs(x - y) < 1e-6 for x, y in zip(obtenu, attendu))
    echecs += not ok
    print(f"{nom} : arguments {args} ; attendu (à la main) {attendu} ; obtenu {obtenu} ; {'TENU' if ok else 'CASSÉ'}")
print("échecs :", echecs)
sys.exit(1 if echecs else 0)
