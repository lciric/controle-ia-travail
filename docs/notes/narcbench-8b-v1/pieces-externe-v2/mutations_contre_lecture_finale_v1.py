"""Rejeu, après les essais ajoutés, des mutations de la contre-lecture du code final (`contre-lecture-code-final-externe-v2-v1.md`,
`a0ce022d…`) : les dix-huit mutations de `cellules_externe_v2.py` (lot C : C01 à C15, C18, C21, C22) et les deux de la garde du
registre (lot B : B01, B02), définitions lues telles quelles dans ses pièces (`lot_c.json`, `lot_b.json`), précédées d'une
mutation témoin. Même méthode que `mutations_decisives_v1.py` : copie de `src/controle_ia/narcbench/` seule (reste du paquet en
liens symboliques), `-o pythonpath=<copie>/src`, chaque mutation sous `timeout 600`, l'une après l'autre ; copies supprimées.
Essais joués : le fichier des cellules entier pour le lot C ; pour B01 et B02, les cas de la garde du registre (sélection, pour
tenir le disque). Usage : python mutations_contre_lecture_finale_v1.py <arbre> <python> <paquets> <lot_c.json> <lot_b.json>"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ARBRE, PY, PAQUETS = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
LOT_C = [m for m in json.loads(Path(sys.argv[4]).read_text(encoding="utf-8")) if m["nom"][:3] not in ("C24", "C25")]
LOT_B = [m for m in json.loads(Path(sys.argv[5]).read_text(encoding="utf-8")) if m["nom"][:3] in ("B01", "B02")]
CEL, LEC = "tests/test_narcbench_cellules_externe_v2.py", "tests/test_narcbench_lecture_externe_v2.py"
K_REGISTRE = "code_seule_posterieure or sceau_faux_de_la_fiche or sceau_faux or posterieure or code_au_meme_instant"
MUTATIONS = [{"nom": "T00 témoin : exception en tête de cellules_externe_v2", "fichier": "src/controle_ia/narcbench/cellules_externe_v2.py",
              "avant": "from __future__ import annotations\n", "apres": 'from __future__ import annotations\nraise RuntimeError("copie mutée chargée")\n',
              "essais": CEL, "k": None}]
MUTATIONS += [dict(m, essais=CEL, k=None) for m in LOT_C] + [dict(m, essais=LEC, k=K_REGISTRE) for m in LOT_B]


def copie(d: Path) -> None:
    racine, cible = ARBRE / "src" / "controle_ia", d / "src" / "controle_ia"
    cible.mkdir(parents=True)
    for e in racine.iterdir():
        if e.name == "narcbench":
            shutil.copytree(e, cible / "narcbench", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        elif e.name != "__pycache__":
            (cible / e.name).symlink_to(e)


print(f"{len(MUTATIONS)} mutations (témoin compris)", flush=True)
for i, m in enumerate(MUTATIONS):
    d = ARBRE / ".mutants" / f"m{i:02d}"
    copie(d)
    p = d / m["fichier"]
    s = p.read_text(encoding="utf-8")
    if s.count(m["avant"]) != 1:
        shutil.rmtree(d)
        print(f"{m['nom']} | INAPPLICABLE ({s.count(m['avant'])} occurrences)", flush=True)
        continue
    p.write_text(s.replace(m["avant"], m["apres"]), encoding="utf-8")
    commande = ["timeout", "600", PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-o", f"pythonpath={d}/src",
                f"--basetemp={d}/tmp", m["essais"]] + (["-k", m["k"]] if m["k"] else [])
    r = subprocess.run(commande, cwd=ARBRE, capture_output=True, text=True,
                       env={"PYTHONPATH": f"{d}/src:{PAQUETS}", "PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin", "HOME": "/root"})
    taille = sum(f.stat().st_size for f in d.rglob("*") if f.is_file() and not f.is_symlink()) // 2 ** 20
    shutil.rmtree(d)
    tueur = next((x.group(1) for x in re.finditer(r"^(?:FAILED|ERROR) (\S+)", r.stdout, re.M)), None)
    bilan = [l for l in r.stdout.splitlines() if l.strip()][-1] if r.stdout.strip() else r.stderr.strip()[-150:]
    etat = "TUÉE" if r.returncode not in (0, 124) else ("SURVIVANTE" if r.returncode == 0 else "DÉLAI DÉPASSÉ")
    print(f"{m['nom']} | {etat} | {tueur or '—'} | {bilan} | {taille} Mo", flush=True)
    if i == 0 and "copie mutée chargée" not in r.stdout + r.stderr:
        print("ARRÊT : la mutation témoin ne s'est pas montrée ; la copie mutée n'est pas chargée", flush=True)
        break
shutil.rmtree(ARBRE / ".mutants", ignore_errors=True)
