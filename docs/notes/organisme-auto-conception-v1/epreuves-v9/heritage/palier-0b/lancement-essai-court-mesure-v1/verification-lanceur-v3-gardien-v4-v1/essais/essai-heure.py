"""Essai de lire_heure_arret du gardien v4 sur des heures limites que je choisis (secondes 60 et 61, année 0001, très lointaine)."""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("gardien4", sys.argv[1])
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
for t in ["2026-11-25T17:00:00Z", "2026-11-25T17:00:59Z", "2026-11-25T17:00:60Z", "2026-11-25T17:00:61Z",
          "0001-01-01T00:00:00Z", "9999-12-31T23:59:59Z", "2026-11-25T17:00:00z", "2026-11-25T17:00:00Z\n"]:
    try:
        print(repr(t), "->", g.lire_heure_arret(t))
    except Exception as e:
        print(repr(t), "-> refus", type(e).__name__)
