"""Mutants de la revue CB2 (51, `mutants_b3_2.py`, copié sans modification) sur le module corrigé (hors livrable).

BASE est une copie de final-b4 (`base-b4/`), jamais final-b4 lui-même. Les motifs de V1, V2 et V3 sont adaptés au verrou
de fin réécrit (précision 16 : vérifications sur la liste recalculée), en gardant la règle mutée ; les 48 autres sont
ceux de la revue, tels quels. Chaque mutant change une règle dans une copie du module ; on lance, sur cette copie, le ou
les tests qui doivent le tuer (sélection -k, arrêt au premier échec). Un mutant est « tué » si pytest rend 1 (test en
échec) ; 5 (aucun test sélectionné) ou un autre code est une erreur du lanceur. Le témoin lance l'union des sélections
sur la copie non mutée : tout doit passer.

Usage : python -I mutants_b4.py verifier | temoin | lancer [ID …]
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True          # aucun __pycache__ dans le dossier (CB1-07)
ICI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ICI, "base-b4")
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
RESULTATS = os.path.join(ICI, "mutants-b4-resultats.jsonl")

_spec = importlib.util.spec_from_file_location("mutants_b3_2", os.path.join(ICI, "mutants_b3_2.py"))
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

ADAPTES = {   # même règle mutée, motif du verrou de fin réécrit (vérifications sur la liste recalculée)
    "V1": ('if c["controle_contraire"] != SANS_OBJET and c["cible"] not in recalculees:', "if False:"),
    "V2": ("exiger_verrou(sortie, lecture, etablies, principales, issue_canonique)",
           "exiger_verrou(sortie, lecture, cibles_possibles(principales), principales, issue_canonique)"),
    "V3": ('if r["cible"] not in recalculees:', "if False:"),
}
M = [(i, f, n, *(ADAPTES[i] if i in ADAPTES else (o, nv))) for i, f, n, o, nv in _mb.M]
PAR_ID = {m[0]: m for m in M}

# mutant → sélection (-k) des tests qui doivent le tuer
SELECTION = {
    "V1": "verrou_de_fin", "V2": "verrou_de_fin", "V3": "verrou_de_fin",
    "V4": "conclusions_etablies_table_fermee", "V5": "garde_du_verrou_sain", "V6": "issue_primaire_inchangee",
    "V7": "issue_modifiee_pendant",
    "C1": "A1_sain", "C2": "A1_sain", "C3": "A1_sain", "C4": "A7_sain", "C5": "A7_sain",
    "C6": "entree_entiere", "C7": "entree_entiere", "C8": "entree_entiere",
    "N1": "niveaux_des_intervalles", "N2": "niveaux_des_intervalles", "N3": "A2_sain", "N4": "A4_sain", "N5": "A4_sain",
    "N6": "A4_sain", "N7": "A6_sain", "N8": "A1_sain", "N9": "A7_artefact_forme_du_cout",
    "J1": "aucune_moyenne", "J2": "fenetres_d_une_sonde",
    "R1": "A8_regles", "R2": "A8_regles", "R3": "A4a_chaque", "R4": "A4a_chaque", "R5": "A6_reserve",
    "L1": "A1_calculs", "L2": "toute_exception", "L3": "A4a_chaque", "L4": "A4a_chaque", "L5": "A6_reserve",
    "L6": "A7_formes", "L7": "A7_formes", "L8": "A8_regles", "L9": "A8_regles", "L10": "A8_regles",
    "G1": "jamais_eprouvee", "G2": "degenerescences", "G3": "A7_formes", "G4": "A4_degenere", "G5": "A7_formes",
    "G6": "A8_regles", "G7": "A8_regles", "G8": "regle_stricte", "G9": "aucune_moyenne", "G10": "A2a_et_A5",
}


def verifier():
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    ok = len(M) == 51 and set(SELECTION) == set(PAR_ID)
    for ident, _, nom, old, _new in M:
        n = src.count(old)
        if n != 1:
            ok = False
            print(f"{ident} : motif présent {n} fois ({nom})")
    print("51 motifs uniques, une sélection par mutant" if ok else "MOTIFS OU SÉLECTIONS À CORRIGER")
    return ok


def _pytest(dossier, selection):
    env = {**os.environ, "PYTHONPATH": os.path.join(DEPOT, "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([PY, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", selection,
                           "test_complements_p3_v1.py"], cwd=dossier, env=env, capture_output=True, text=True,
                          timeout=3600)


def lancer_un(ident):
    _, famille, nom, old, new = PAR_ID[ident]
    d = os.path.join(ICI, "mutants", ident)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    src = open(os.path.join(BASE, "complements_p3_v1.py"), encoding="utf-8").read()
    assert src.count(old) == 1, ident
    open(os.path.join(d, "complements_p3_v1.py"), "w", encoding="utf-8").write(src.replace(old, new))
    shutil.copy(os.path.join(BASE, "test_complements_p3_v1.py"), d)
    t0 = time.time()
    r = _pytest(d, SELECTION[ident])
    lignes = r.stdout.strip().splitlines()
    derniere = lignes[-1] if lignes else r.stderr[-300:]
    echec = next((x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")), "")
    etat = {1: "tué", 0: "SURVIT", 5: "SÉLECTION VIDE"}.get(r.returncode, f"ERREUR {r.returncode}")
    res = {"id": ident, "famille": famille, "mutant": nom, "selection": SELECTION[ident], "etat": etat,
           "code": r.returncode, "resume": derniere, "premier_echec": echec, "duree_s": round(time.time() - t0)}
    with open(RESULTATS, "a", encoding="utf-8") as f:
        f.write(json.dumps(res, ensure_ascii=False) + "\n")
    with open(os.path.join(d, "pytest.log"), "w", encoding="utf-8") as f:
        f.write(r.stdout[-20000:] + "\n" + r.stderr[-5000:])
    os.remove(os.path.join(d, "complements_p3_v1.py"))              # garde le journal, pas la copie
    os.remove(os.path.join(d, "test_complements_p3_v1.py"))
    return res


def temoin():
    selection = " or ".join(sorted(set(SELECTION.values())))
    r = _pytest(BASE, selection)
    with open(os.path.join(ICI, "mutants-b4-temoin.log"), "w", encoding="utf-8") as f:
        f.write(f"sélection : {selection}\n\n" + r.stdout[-20000:] + "\n" + r.stderr[-5000:])
    print(f"témoin (copie non mutée, union des sélections) : code {r.returncode} ; "
          f"{r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:]}")
    return r.returncode == 0


if __name__ == "__main__":
    if sys.argv[1] == "verifier":
        sys.exit(0 if verifier() else 1)
    if sys.argv[1] == "temoin":
        sys.exit(0 if temoin() else 1)
    if sys.argv[1] == "lancer":
        par = int(os.environ.get("PARALLELE", "3"))
        ids = sys.argv[2:] or [m[0] for m in M]
        with ThreadPoolExecutor(par) as ex:
            for res in ex.map(lancer_un, ids):
                print(f"{res['etat']:7s} {res['id']:4s} [{res['selection']}] {res['mutant']} — {res['resume']} "
                      f"({res['duree_s']} s)", flush=True)
