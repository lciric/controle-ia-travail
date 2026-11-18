"""Épreuve par mutation des essais du bras externe NARCBench, v1 : dix mutations décisives et une mutation témoin.

Chaque mutation est appliquée à une copie de `src/controle_ia/narcbench/` seulement (le reste du paquet : liens symboliques vers
l'arbre), dans `<arbre>/.mutants/<id>/` ; la série d'essais visée est jouée **au premier plan, sous `timeout`**, avec
`-o pythonpath=<copie>/src` (le `pyproject.toml` du dépôt déclare `pythonpath = ["src", "tests"]`, qui sinon chargerait le code
non muté) ; puis la copie est supprimée. La mutation témoin (une exception en tête de `externe_v2`) doit faire échouer les essais :
elle prouve que la copie mutée est bien celle qui est chargée. Usage : python mutations_decisives_v1.py <arbre> <python> <paquets>
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ARBRE, PY, PAQUETS = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
N = "src/controle_ia/narcbench/"
EXT, CEL, LEC = "tests/test_narcbench_externe_v2.py", "tests/test_narcbench_cellules_externe_v2.py", "tests/test_narcbench_lecture_externe_v2.py"
MUTATIONS = [
    ("T00 témoin : exception en tête de externe_v2", N + "externe_v2.py", "from __future__ import annotations\n",
     'from __future__ import annotations\nraise RuntimeError("copie mutée chargée")\n', EXT, None),
    ("E01 max_iter 8 → 100", N + "externe_v2.py", 'PARAMETRES_LR = {"max_iter": 8,', 'PARAMETRES_LR = {"max_iter": 100,', EXT, None),
    ("E02 garde de la direction nulle retirée", N + "externe_v2.py", "    if not nrm > 0:", "    if False:", EXT, None),
    ("E03 mode incohérent entre lignes (CORE) ignoré", N + "externe_v2.py",
     '            if mode_run.setdefault(m["run_id"], m["mode"]) != m["mode"]:', "            if False:", EXT, None),
    ("E04 mode incohérent entre agents (STEGO) ignoré", N + "externe_v2.py",
     '            if g["mode"] != m["mode"]:\n                raise GardeArret(f"{rid} : mode incohérent entre agents")',
     '            if False:\n                raise GardeArret(f"{rid} : mode incohérent entre agents")', EXT, None),
    ("E05 seuil STEGO « moins de 4 » → « moins de 3 »", N + "externe_v2.py", "    if len(np.unique(y)) < 2 or len(rids) < 4:",
     "    if len(np.unique(y)) < 2 or len(rids) < 3:", EXT, None),
    ("E06 placebo par agent jamais déclenché", N + "externe_v2.py", '    declenche = S.placebo_declenche(lec["bas"], perm)',
     "    declenche = False", EXT, None),
    ("E07 tolérance de la garde 0,03 → 0,3", N + "externe_v1.py", "TOLERANCE = 0.03", "TOLERANCE = 0.3", EXT, None),
    ("L01 garde « ligne mal formée » du registre retirée", N + "lecture_externe_v2.py",
     '        if len(c) != 4:\n            fautes.append(f"registre : ligne {k} mal formée',
     '        if False:\n            fautes.append(f"registre : ligne {k} mal formée', LEC,
     "cinq_cellules or date_mal_formee or empreinte_mal_formee or chemin_absolu or chemin_remontant"),
    ("L02 garde « texte cité autre » retirée", N + "lecture_externe_v2.py", "    if Path(cs) != Path(texte):", "    if False:", LEC,
     "cite_un_autre_texte or texte_absolu or texte_de_la_section_autre"),
    ("K13 comités : moyenne des messages au lieu du maximum", N + "cellules_externe_v2.py", "seq = [A[messages[(r, n)]] for r in te",
     "seq = [A[messages[(r, n)]].mean(axis=0, keepdims=True) for r in te", CEL, None),
    ("K01 « reproduit » sans l'arrondi de 10⁻⁹", N + "cellules_externe_v2.py", "    if bas >= m - ARRONDI:", "    if bas >= m:", CEL, None),
]


def copie(d: Path) -> None:
    racine = ARBRE / "src" / "controle_ia"
    cible = d / "src" / "controle_ia"
    cible.mkdir(parents=True)
    for e in racine.iterdir():
        if e.name == "narcbench":
            shutil.copytree(e, cible / "narcbench", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        elif e.name != "__pycache__":
            (cible / e.name).symlink_to(e)


for i, (nom, fichier, avant, apres, essais, k) in enumerate(MUTATIONS):
    d = ARBRE / ".mutants" / f"m{i:02d}"
    copie(d)
    p = d / fichier
    s = p.read_text(encoding="utf-8")
    if s.count(avant) != 1:
        shutil.rmtree(d)
        print(f"{nom} : MUTATION INAPPLICABLE ({s.count(avant)} occurrences)", flush=True)
        continue
    p.write_text(s.replace(avant, apres), encoding="utf-8")
    commande = ["timeout", "600", PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-o", f"pythonpath={d}/src",
                f"--basetemp={d}/tmp", essais] + (["-k", k] if k else [])
    r = subprocess.run(commande, cwd=ARBRE, capture_output=True, text=True,
                       env={"PYTHONPATH": f"{d}/src:{PAQUETS}", "PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin", "HOME": "/root"})
    taille = sum(f.stat().st_size for f in d.rglob("*") if f.is_file() and not f.is_symlink()) // 2 ** 20
    shutil.rmtree(d)
    tueur = next((m.group(1) for m in re.finditer(r"^(?:FAILED|ERROR) (\S+)", r.stdout, re.M)), None)
    bilan = [l for l in r.stdout.splitlines() if l.strip()][-1] if r.stdout.strip() else r.stderr.strip()[-150:]
    etat = "TUÉE" if r.returncode not in (0, 124) else ("SURVIVANTE" if r.returncode == 0 else "DÉLAI DÉPASSÉ")
    print(f"{nom} | {etat} | {tueur or '—'} | {bilan} | {taille} Mo | sélection : {k or 'fichier entier'}", flush=True)
    if i == 0 and "copie mutée chargée" not in r.stdout + r.stderr:
        print("ARRÊT : la mutation témoin ne s'est pas montrée ; la copie mutée n'est pas chargée", flush=True)
        break
shutil.rmtree(ARBRE / ".mutants", ignore_errors=True)
