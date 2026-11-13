"""Épreuves (R5) de comparer-versions-7b-venv-v1.py sur pièces factices ; aucune donnée de 7b lue.

Usage : python3 -I essais-comparer-versions-7b-venv-v1.py RACINE_DEPOT DOSSIER_NEUF PYTHON
Chaque cas a son dossier (copie de `src/`, registre et manifeste factices) ; le résultat attendu est écrit à côté.
"""
import hashlib, json, shutil, subprocess, sys
from pathlib import Path

depot, base, python = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), sys.argv[3]
if base.exists():
    sys.exit(f"ARRÊT : {base} existe déjà")
script = depot / "brouillons/audit-fuites-t07-preparation-compte4-v1/comparer-versions-7b-venv-v1.py"
cas = [  # nom, course citée, altération des versions, ligne en double, empreinte de ligne fausse, code attendu
    ("sain", "20261112-000000-t06-factice", None, False, False, 0),
    ("version-differente", "20261112-000000-t06-factice", ("numpy", "0.0.0"), False, False, 1),
    ("plateforme-differente", "20261112-000000-t06-factice", ("plateforme", "autre"), False, False, 0),
    ("course-7a", "20261109-070232-t06-reel", None, False, False, 2),
    ("ligne-en-double", "20261112-000000-t06-factice", None, True, False, 2),
    ("empreinte-fausse", "20261112-000000-t06-factice", None, False, True, 2),
]
ok = True
for nom, run, alt, double, fausse, attendu in cas:
    r = base / nom
    shutil.copytree(depot / "src", r / "src")
    v = json.loads(subprocess.run([python, "-I", "-c", "import json,sys; sys.path.insert(0,'src'); "
                                   "from controle_ia.manifeste import versions; print(json.dumps(versions()))"],
                                  cwd=r, capture_output=True, text=True, check=True).stdout)
    if alt:
        v[alt[0]] = alt[1]
    p = r / "runs" / run / "manifeste.json"
    p.parent.mkdir(parents=True)
    p.write_text(json.dumps({"run_id": run, "config": {}, "versions": v}), encoding="utf-8")
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    (p.parent / "manifeste.json.sha256").write_text(f"{sha}  manifeste.json\n", encoding="utf-8")
    ligne = f"| RUN-CONFIRMATION-T06 | 2026-11-12T00:00:00Z | runs/{run}/manifeste.json | {'0' * 64 if fausse else sha} |\n"
    (r / "registre.md").write_text("| CLÉ | date | chemin | sha256 |\n" + ligne * (2 if double else 1), encoding="utf-8")
    res = subprocess.run([python, "-I", str(script), str(r), str(r / "registre.md"), python], capture_output=True, text=True)
    bon = res.returncode == attendu
    ok &= bon
    motif = (res.stderr.strip() or "toutes_egales=" + str(json.loads(res.stdout)["toutes_egales"]))[:120]
    print(f"{nom} : code {res.returncode} (attendu {attendu}) {'conforme' if bon else 'NON CONFORME'} ; {motif}")
print("bilan :", "toutes les épreuves conformes" if ok else "ÉCHEC")
sys.exit(0 if ok else 1)
