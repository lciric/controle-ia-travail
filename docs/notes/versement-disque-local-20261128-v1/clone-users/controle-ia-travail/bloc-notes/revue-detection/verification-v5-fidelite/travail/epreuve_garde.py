"""Épreuve R5 des deux gardes de verif_pages_v5.py : cas sain (compagnon juste) puis artefact (compagnon faux, préfixe faux)."""
import importlib.util, sys
from pathlib import Path
W = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("vp", W / "verif_pages_v5.py")
vp = importlib.util.module_from_spec(spec); spec.loader.exec_module(vp)
print("sain PDF :", "accepté" if vp.cherche("YS", 3, "Sandbagging performs poorly (0.606 AUROC).") else "?")
vp.D = W / "epreuve-garde"; vp._cache.clear()
try:
    vp.cherche("YS", 3, "Sandbagging performs poorly (0.606 AUROC).")
    print("artefact PDF : ACCEPTÉ (faute)")
except SystemExit as e:
    print("artefact PDF : arrêt :", str(e)[:70])
print("sain dépôt :", "accepté" if "P-016" in vp.ligne("registres/decisions.md", "e8b73c64", 393) else "?")
try:
    vp.ligne("registres/decisions.md", "38579d98", 393)
    print("artefact dépôt : ACCEPTÉ (faute)")
except SystemExit as e:
    print("artefact dépôt : arrêt :", str(e)[:70])
