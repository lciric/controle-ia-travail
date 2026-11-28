"""Les 8 mutants survivants de VF2 (M09 à M14, M19, M24) contre le fichier de tests retouché (hors livrable).

Substitutions exactes : lues dans le lanceur de VF2 (`lanceur_vf2.py`, empreinte vérifiée), par l'arbre syntaxique, sans
exécuter ce lanceur. BASE est une copie de final-b4 (`base-vf2/`, empreintes vérifiées), jamais final-b4 lui-même. Pour
chaque mutant : motif présent une seule fois dans la copie de base (sinon refus), copie mutée dans `mutants-vf2/<id>/`,
test tueur de VF2 lancé seul (identifiant exact, arrêt au premier échec). « Tué » : pytest rend 1 ; 0 : survit ; 5 :
sélection vide (erreur). Le témoin lance les mêmes tests sur la copie non mutée : tout doit passer.

Usage : python -I mutants_vf2_b4.py            (témoin et 8 mutants)
        python -I mutants_vf2_b4.py locaux ID …  (mutants relancés avec -l : variables locales, dont `motif`, au
                                                 point d'échec ; copies dans `mutants-vf2/<id>-locaux/`)
"""
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True          # aucun __pycache__ dans le dossier (CB1-07)
ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ICI, "base-vf2")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
VF2 = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/verification-finale/mutants/lanceur_vf2.py"
SHA_VF2 = "76aa1ea5760427990193e06bbf7e955b8bbe977d4c63093da1f6929c409dcb52"
SHA_MODULE = "2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996"
SHA_TESTS = "7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3"
TESTS = "test_complements_p3_v1.py"
IDS = ("M09", "M10", "M11", "M12", "M13", "M14", "M19", "M24")
RESULTATS = os.path.join(ICI, "mutants-vf2-resultats.jsonl")


def _sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def mutants_de_vf2():
    """(id, description, ancien, nouveau, test tueur) des 8 mutants, lus dans `NEUFS` du lanceur de VF2."""
    if _sha(VF2) != SHA_VF2:
        raise SystemExit("lanceur de VF2 : empreinte autre que celle relevée")
    arbre = ast.parse(open(VF2, encoding="utf-8").read())
    noms, neufs = {}, None
    for n in arbre.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            if isinstance(n.value, ast.Constant) and isinstance(n.value.value, str):
                noms[n.targets[0].id] = n.value.value
            elif n.targets[0].id == "NEUFS":
                neufs = n.value

    def valeur(x):
        return noms[x.id] if isinstance(x, ast.Name) else ast.literal_eval(x)

    lus = {}
    for t in neufs.elts:
        if valeur(t.elts[0]) in IDS:
            ident, _, description, ancien, nouveau, tueur = (valeur(x) for x in t.elts)
            lus[ident] = (ident, description, ancien, nouveau, tueur)
    if sorted(lus) != sorted(IDS):
        raise SystemExit(f"mutants absents du lanceur de VF2 : {sorted(set(IDS) - set(lus))}")
    return [lus[i] for i in IDS]


def _pytest(dossier, tests, options=()):
    env = {**os.environ, "PYTHONPATH": os.path.join(DEPOT, "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *options] +
                          [f"{TESTS}::{t}" for t in tests],
                          cwd=dossier, env=env, capture_output=True, text=True, timeout=3600)


def lancer_un(m, options=(), suffixe=""):
    ident, description, ancien, nouveau, tueur = m
    d = os.path.join(ICI, "mutants-vf2", ident + suffixe)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    if src.count(ancien) != 1:
        raise SystemExit(f"{ident} : motif présent {src.count(ancien)} fois dans la copie de base")
    open(os.path.join(d, "complements_p3_v1.py"), "w", encoding="utf-8").write(src.replace(ancien, nouveau))
    shutil.copy(os.path.join(BASE, TESTS), d)
    t0 = time.time()
    r = _pytest(d, [tueur], options)
    lignes = r.stdout.strip().splitlines()
    echec = next((x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")), "")
    res = {"id": ident, "mutant": description, "test_tueur": tueur,
           "etat": {1: "tué", 0: "SURVIT", 5: "SÉLECTION VIDE"}.get(r.returncode, f"ERREUR {r.returncode}"),
           "code": r.returncode, "resume": lignes[-1] if lignes else r.stderr[-300:], "premier_echec": echec,
           "duree_s": round(time.time() - t0)}
    with open(os.path.join(d, "pytest.log"), "w", encoding="utf-8") as f:
        f.write(r.stdout[-20000:] + "\n" + r.stderr[-5000:])
    os.remove(os.path.join(d, "complements_p3_v1.py"))              # garde le journal, pas la copie
    os.remove(os.path.join(d, TESTS))
    return res


def temoin(ms):
    tests = sorted({m[4] for m in ms})
    r = _pytest(BASE, tests)
    with open(os.path.join(ICI, "mutants-vf2-temoin.log"), "w", encoding="utf-8") as f:
        f.write(f"tests : {tests}\n\n" + r.stdout[-20000:] + "\n" + r.stderr[-5000:])
    lignes = r.stdout.strip().splitlines()
    return {"id": "témoin", "tests": tests, "code": r.returncode, "resume": lignes[-1] if lignes else r.stderr[-300:]}


if __name__ == "__main__":
    if (_sha(os.path.join(BASE, "complements_p3_v1.py")), _sha(os.path.join(BASE, TESTS))) != (SHA_MODULE, SHA_TESTS):
        raise SystemExit("copie de base : empreintes autres que celles de final-b4")
    ms = mutants_de_vf2()
    if sys.argv[1:2] == ["locaux"]:
        with ThreadPoolExecutor(max_workers=3) as ex:
            res = list(ex.map(lambda m: lancer_un(m, ("-l",), "-locaux"), [m for m in ms if m[0] in sys.argv[2:]]))
        for x in res:
            print(json.dumps(x, ensure_ascii=False))
        sys.exit(0)
    with ThreadPoolExecutor(max_workers=3) as ex:
        futurs = [ex.submit(temoin, ms)] + [ex.submit(lancer_un, m) for m in ms]
        res = [f.result() for f in futurs]
    with open(RESULTATS, "w", encoding="utf-8") as f:
        for x in res:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    for x in res:
        print(json.dumps(x, ensure_ascii=False))
    tues = sum(1 for x in res[1:] if x["etat"] == "tué")
    print(f"témoin : code {res[0]['code']} ; tués : {tues}/{len(ms)}")
    sys.exit(0 if res[0]["code"] == 0 and tues == len(ms) else 1)
