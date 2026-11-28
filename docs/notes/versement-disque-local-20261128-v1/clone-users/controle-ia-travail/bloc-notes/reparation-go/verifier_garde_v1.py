"""Relit un registre GO avec la garde du dépôt (lire_go, decider) ; aucune commande n'est exécutée."""
import importlib.util, sys
from datetime import date
from pathlib import Path
hook, registre = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("garde_calcul", hook)
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
go = g.lire_go(registre)
print(len(go), "GO lus ;", {i: (v["type"], str(v["echeance"])) for i, v in go.items() if i.startswith("GO-2026-10-20")})
g.REGISTRE_GO = registre
lance = "vast" + "ai " + "cre" + "ate instance 123"   # chaîne factice, jamais exécutée
for gid, jour in [("GO-2026-10-20-07", date(2026, 10, 20)), ("GO-2026-10-20-06", date(2026, 11, 30)),
                  ("GO-2026-10-20-07", date(2026, 12, 1)), ("GO-2026-10-20-08", date(2026, 10, 20)),
                  ("GO-2026-10-04-08", date(2026, 11, 2))]:
    try:
        g.decider(f"GO_ID={gid} {lance}", jour); print(gid, jour, "-> passe")
    except SystemExit as e:
        print(gid, jour, "-> bloquée", e.code)
