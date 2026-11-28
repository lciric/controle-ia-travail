"""Partie B de la vérification des corrections du brouillon 7 (VB7) : tests corrigés de l'addendum de P3.

Copie à moi (`base/` : module réel 2b16179d…, tests corrigés 7387910d…). Rien n'est écrit hors de `partie-b/`.
Usage : python -B lanceur_b.py collecte | temoin | mutants [ID …]
- collecte : nombre de tests collectés (attendu : 165), sans rien lancer ;
- temoin : les six tests retouchés sur le module réel (tous doivent passer) ;
- mutants : les 8 mutants survivants de VF2 (substitutions de `verification-finale/mutants/lanceur_vf2.py`, motif
  présent une seule fois), chacun avec son test tueur ; au plus deux processus à la fois.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ICI, "base")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
SRC = "/home/user/controle-ia-travail/src"
SHA = {"complements_p3_v1.py": "2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996",
       "test_complements_p3_v1.py": "7387910d3b5851026f316e89df3f1b84e4a39758e9d73da52cea166f5223e0a3"}
TESTS = "test_complements_p3_v1.py"
DRAPEAUX = "test_garde_7_drapeaux_bruts_recoupes_avec_les_etats"
ORGANISME = "test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet"
COHERENCE = "test_garde_coherence_de_la_lecture_avec_le_run_source"
LOCALISATION = "test_garde_localisation_egale_a_celle_de_la_lecture"
G4T = "test_garde_4_textes_lus_sur_les_seuls_sauts_de_ligne"
COMMANDE = "test_forme_de_la_commande"
RETOUCHES = (G4T, COHERENCE, LOCALISATION, ORGANISME, DRAPEAUX, COMMANDE)

# substitutions recopiées de verification-finale/mutants/lanceur_vf2.py (NEUFS), test tueur de VF2
MUTANTS = [
    ("M09", "attendu = st == lp.AU_DESSUS and th == lp.NON_AU_DESSUS", "attendu = st == lp.AU_DESSUS", DRAPEAUX),
    ("M10", 'return L["etats"][p]["mention-honnete"] == lp.NON_AU_DESSUS and L["etats"][p]["saboteur-mention"] == lp.AU_DESSUS',
     'return L["etats"][p]["mention-honnete"] == lp.NON_AU_DESSUS', DRAPEAUX),
    ("M11", 'if f"P3-P3/{p}" in etablies:', "if True:", ORGANISME),
    ("M12", "    return bas > seuil", "    return bas >= seuil", DRAPEAUX),
    ("M13", "TOLERANCE_COHERENCE = 1e-9 ", "TOLERANCE_COHERENCE = 1e-3 ", COHERENCE),
    ("M14", "TOLERANCE_LOCALISATION = 1e-9 ", "TOLERANCE_LOCALISATION = 1e-7 ", LOCALISATION),
    ("M19", "        if not ligne:\n            continue", "        if not ligne.strip():\n            continue", G4T),
    ("M24", 'RUN_ADDENDUM = re.compile(r"^[0-9]{8}-[0-9]{6}-addendum-p3$")',
     'RUN_ADDENDUM = re.compile(r"^[0-9]{8}-[0-9]{6}-addendum-p3")', COMMANDE),
]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def env():
    e = dict(os.environ, PYTHONPATH=SRC, PYTHONDONTWRITEBYTECODE="1", TMPDIR=os.path.join(ICI, "tmp"))
    return e


def pytest(dossier, noeuds, journal, extra=()):
    bt = os.path.join(ICI, "basetemp", os.path.basename(dossier) + "-" + str(int(time.time() * 1000)))
    cmd = [PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", f"--basetemp={bt}", *extra,
           *[f"{os.path.join(dossier, TESTS)}::{n}" for n in noeuds]]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=dossier, env=env(), capture_output=True, text=True)
    with open(journal, "w", encoding="utf-8") as f:
        f.write(" ".join(cmd) + "\n\n" + r.stdout + "\n" + r.stderr)
    shutil.rmtree(bt, ignore_errors=True)
    return r.returncode, round(time.time() - t0, 1), r.stdout


def verifier_base():
    for nom, e in SHA.items():
        assert sha(os.path.join(BASE, nom)) == e, nom


def collecte():
    verifier_base()
    cmd = [PY, "-B", "-m", "pytest", "-q", "--collect-only", "-p", "no:cacheprovider", os.path.join(BASE, TESTS)]
    r = subprocess.run(cmd, cwd=BASE, env=env(), capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if "::" in x]
    with open(os.path.join(ICI, "collecte.log"), "w", encoding="utf-8") as f:
        f.write(r.stdout + r.stderr)
    print("code", r.returncode, "; tests collectés :", len(lignes), ";", r.stdout.strip().splitlines()[-1])


def temoin():
    verifier_base()
    code, duree, sortie = pytest(BASE, RETOUCHES, os.path.join(ICI, "temoin-six-tests.log"))
    print("témoin (six tests retouchés, module réel) : code", code, ";", duree, "s ;", sortie.strip().splitlines()[-1])
    verifier_base()


def un_mutant(m):
    ident, ancien, nouveau, tueur = m
    d = os.path.join(ICI, "m", ident)
    os.makedirs(d, exist_ok=True)
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    n = src.count(ancien)
    if n != 1:
        return {"id": ident, "statut": f"REFUS : motif présent {n} fois"}
    open(os.path.join(d, "complements_p3_v1.py"), "w", encoding="utf-8").write(src.replace(ancien, nouveau))
    shutil.copyfile(os.path.join(BASE, TESTS), os.path.join(d, TESTS))
    assert sha(os.path.join(d, TESTS)) == SHA[TESTS]
    code, duree, sortie = pytest(d, (tueur,), os.path.join(d, "pytest-tueur.log"), extra=("-x",))
    lignes = re.findall(r"test_complements_p3_v1\.py:(\d+): ", sortie)
    erreurs = [x for x in sortie.splitlines() if x.startswith("E ")][:3]
    return {"id": ident, "tueur": tueur, "code": code, "statut": "tué" if code == 1 else ("SURVIT" if code == 0 else
            f"code {code}"), "duree_s": duree, "ligne_du_test": lignes[-1] if lignes else None, "erreur": erreurs,
            "module_mute_sha256": sha(os.path.join(d, "complements_p3_v1.py"))}


def mutants(ids):
    verifier_base()
    choisis = [m for m in MUTANTS if not ids or m[0] in ids]
    with ThreadPoolExecutor(max_workers=2) as ex:
        resultats = list(ex.map(un_mutant, choisis))
    with open(os.path.join(ICI, "mutants-b-resultats.jsonl"), "a", encoding="utf-8") as f:
        for r in resultats:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(json.dumps(r, ensure_ascii=False))
    verifier_base()


if __name__ == "__main__":
    action = sys.argv[1]
    if action == "collecte":
        collecte()
    elif action == "temoin":
        temoin()
    elif action == "mutants":
        mutants(sys.argv[2:])
