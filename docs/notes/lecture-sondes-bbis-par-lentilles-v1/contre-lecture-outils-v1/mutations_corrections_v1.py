"""Essai des essais des corrections du contre-lecteur (copie corrigée seulement)."""
import os, subprocess, sys
from pathlib import Path
R = Path(sys.argv[1]); PY = sys.argv[2]
B = R / "src/controle_ia/lentilles_sondes_bbis"
M = [
 ("lanceur_v1.py", '    if not p.is_file() or mo.sha256_fichier(p) != ligne_code.sha256:', '    if not p.is_file():'),
 ("lanceur_v1.py", '        if fichiers.get(nom) != mo.sha256_fichier(ici / f"{m}.py"):', '        if False:'),
 ("lanceur_v1.py", '    if not forme:', '    if False:'),
 ("entrees_v1.py", '    if not derniere < course.heure_verdict:', '    if False:'),
 ("entrees_v1.py", '    if not lignes["ABSENCE-VERDICT-LENTILLES-BBIS"] or not lignes["SCELLEMENT-LENTILLES-BBIS"]:', '    if False:'),
 ("lanceur_v1.py", '        if t == s or t in s.parents or s in t.parents:', '        if False:'),
 ("lanceur_v1.py", '    versement = verser_travail(travail, sortie, run, "fin")\n    from ..scellement import verifier\n    verifier(Path(sortie) / versement["chemin"])\n', '    versement = {}\n'),
 ("lanceur_v1.py", '        if rel.parts[0] not in NON_COPIES:', '        if True:'),
 ("lanceur_v1.py", '        if not etat["parti"]:\n            raise', '        if True:\n            raise'),
 ("lanceur_v1.py", '                rendu["morceaux"] = [{"fichier": m["fichier"], "sha256": m["sha256"]} for m in rendu["morceaux"]]', '                pass'),
]
for f, a, b in M:
    p = B / f; s = p.read_text()
    if s.count(a) != 1: print("MOTIF INTROUVABLE", f, a[:60], flush=True); continue
    p.write_text(s.replace(a, b))
    try:
        r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                            "tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py",
                            "tests/test_lentilles_sondes_bbis_procedure_v1.py::test_nettoyage_refuse_un_dossier_sans_la_marque"],
                           cwd=R, capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "src"})
    finally:
        p.write_text(s)
    print("vue    " if r.returncode else "SURVIT ", f, "|", a.strip()[:80].replace("\n", " "), flush=True)
