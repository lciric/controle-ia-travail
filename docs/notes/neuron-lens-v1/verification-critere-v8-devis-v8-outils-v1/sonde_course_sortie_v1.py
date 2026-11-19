"""Sonde : une sortie qui apparaît pendant la comparaison (programme v4, création exclusive l. 682). Pièces inventées, rien de diag/."""
import importlib.util, sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cmp4", ICI / "comparer_reajustement_v4.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
sortie = Path(sys.argv[1])
vrai_charger = m.charger
def charger_puis_course(*a, **k):
    sortie.write_text("{}")           # une autre sortie apparaît pendant la comparaison
    raise OSError("pièce illisible (inventée)")
m.charger = charger_puis_course
d = sortie.parent
m.main(["--ref-ajustement", f"{d}/a", "--neuf-ajustement", f"{d}/b", "--ref-manifeste", f"{d}/c", "--neuf-manifeste", f"{d}/e",
        "--lanceur-ref", f"{d}/f", "--lanceur-neuf", f"{d}/g", "--sortie", str(sortie), "--depot", str(d),
        "--commit-resultats", "0" * 40, "--chemin-lanceur-neuf", "g"])
