"""Survivants de la première série, rejoués contre les essais de procédure qui les visent (copie extraite du commit)."""
import os, subprocess, sys
from pathlib import Path
R = Path(sys.argv[1]); PY = sys.argv[2]
B = R / "src/controle_ia/lentilles_sondes_bbis"
K = "nettoyage or registre or scellements or disque or phrases or 6_go or 1_go or ligne_de_commande"
M = [
 ("phrases_v1.py", "    if libelle == st.LIBELLE_INTERMEDIAIRE:\n        return None", "    if False:\n        return None"),
 ("lanceur_v1.py", "    if libre < int(minimum):", "    if False:"),
 ("lanceur_v1.py", "    if not (travail / MARQUE).is_file():\n        raise Arret(f\"{travail} ne porte pas", "    if False:\n        raise Arret(f\"{travail} ne porte pas"),
 ("lanceur_v1.py", "    if cle not in K.CLES_PROPRES:", "    if False:"),
]
for f, a, b in M:
    p = B / f; s = p.read_text()
    if s.count(a) != 1: print("MOTIF INTROUVABLE", f, a[:60], flush=True); continue
    p.write_text(s.replace(a, b))
    try:
        r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", K,
                            "tests/test_lentilles_sondes_bbis_procedure_v1.py"], cwd=R, capture_output=True, text=True,
                           env={**os.environ, "PYTHONPATH": "src"})
    finally:
        p.write_text(s)
    print("vue    " if r.returncode else "SURVIT ", f, "|", a.strip()[:80].replace("\n", " "), flush=True)
