"""Essai des lignes de projection du gardien v2 (correction 6) : mention « borne basse » sur les trois projections ; mention
« relance entière peu sûre entre deux redémarrages » au-delà de quatre heures (strictement), et seulement alors.

Calculs à la main (total 648) :
  F (sain) : t3 = 0, t_arrêt = 100 s, n = 13 : 100 × 54 = 5 400 s (1,5 h) < 14 400 s : aucune mention.
  G (bord) : t3 = 0, t_arrêt = 266,666… ; plus simple : n = 55, Δt = 1 200 s : 1 200 × 648 / 54 = 14 400 s exactement : aucune
             mention (« au-delà » lu strictement).
  H (artefact) : n = 13, Δt = 600 s : 32 400 s (9 h) > 14 400 s : mention.
  I (artefact) : n = 2, Δt = 23 s : 23 × 648 = 14 904 s > 14 400 s : mention.
  J : n = 1 : « projection impossible », aucune mention.
Usage : essai-projection-v2.py CHEMIN_DU_GARDIEN
"""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("gardien", sys.argv[1])
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

MENTION = "relance entière peu sûre entre deux redémarrages"
cas = [("F sain", (0.0, 100.0, 13, 1000, 900), False, "5400.0 s"),
       ("G bord", (0.0, 1200.0, 55, 1000, 900), False, "14400.0 s"),
       ("H artefact", (0.0, 600.0, 13, 1000, 900), True, "32400.0 s"),
       ("I artefact", (0.0, 23.0, 2, 1000, 900), True, "14904.0 s"),
       ("J n = 1", (0.0, 23.0, 1, 1000, 900), False, None)]
echecs = 0
for nom, args, mention_attendue, duree_attendue in cas:
    lignes = G.lignes_projection(*args)
    texte = "\n".join(lignes)
    mention = MENTION in texte
    if duree_attendue is None:
        ok = lignes == ["projection impossible (n = 1 < 2)"]
    else:
        bornes = sum("borne basse" in l for l in lignes)
        ok = (mention == mention_attendue and bornes == 3 and f"= {duree_attendue}" in lignes[0])
    echecs += not ok
    print(f"{nom} : arguments {args} ; mention attendue {mention_attendue}, rendue {mention} ; "
          f"durée attendue {duree_attendue} ; {'TENU' if ok else 'CASSÉ'}")
    for l in lignes:
        print("    " + l)
print("échecs :", echecs)
sys.exit(1 if echecs else 0)
