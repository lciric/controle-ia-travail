"""Greffon pytest de la contre-lecture du code v2 de l'addendum 2 de P3 (copie étendue de `revue-mutants/garde_r1_revue.py`).

Garde R1 : un crochet d'audit (`sys.addaudithook`) refuse, dans ce processus, toute ouverture, tout listage et toute copie
d'un chemin du dépôt de travail sous `donnees/`, `diag/`, `runs/`, `traces/`, de `prereg/P3-consignes-v1.md`, et de tout
chemin du dépôt qui contient `textes-actions`. Chaque refus est journalisé (il doit n'y en avoir aucun) et lève
`PermissionError` avant l'accès. Il trace aussi, sans refuser, chaque ouverture d'un fichier des textes d'action ou des
scores par jeton hors du dépôt (dépôts jouets), avec la pile d'appel.

Variable : REVUE_JOURNAL_R1 (chemin du journal JSONL, obligatoire).
"""
import json
import os
import sys

DEPOT = "/home/user/controle-ia-travail"
INTERDITS = tuple(os.path.join(DEPOT, x) for x in ("donnees", "diag", "runs", "traces")) + (
    os.path.join(DEPOT, "prereg", "P3-consignes-v1.md"),)
TRACES = ("textes-actions", "jetons-principales")
EVENEMENTS = {"open": 0, "os.listdir": 0, "os.scandir": 0, "glob.glob": 0, "glob.glob/2": 0, "shutil.copyfile": 0,
              "shutil.copytree": 0, "os.rename": 0, "os.remove": 0, "os.rmdir": 0, "shutil.rmtree": 0}
JOURNAL = os.environ["REVUE_JOURNAL_R1"]
_ETAT = {"actif": False}


def _pile(depart):
    f, sortie = depart, []
    while f is not None and len(sortie) < 14:
        co = f.f_code
        sortie.append(f"{os.path.basename(co.co_filename)}:{co.co_name}")
        f = f.f_back
    return sortie


def _ecrire(entree):
    with open(JOURNAL, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entree, ensure_ascii=False) + "\n")


def _interdit(absolu):
    if any(absolu == x or absolu.startswith(x + os.sep) for x in INTERDITS):
        return True
    return (absolu == DEPOT or absolu.startswith(DEPOT + os.sep)) and "textes-actions" in absolu


def _crochet(evenement, args):
    if evenement not in EVENEMENTS or _ETAT["actif"]:
        return
    chemins = []
    position = (0, 1) if evenement in ("shutil.copyfile", "shutil.copytree", "os.rename") else (0,)
    for i in position:
        x = args[i] if len(args) > i else None
        if x is None or isinstance(x, int):
            continue
        try:
            chemins.append(os.path.abspath(os.fsdecode(x)))
        except TypeError:
            continue
    for absolu in chemins:
        interdit = _interdit(absolu)
        trace = evenement == "open" and any(t in absolu for t in TRACES)
        if not (interdit or trace):
            continue
        _ETAT["actif"] = True
        try:
            _ecrire({"refus": interdit, "evenement": evenement, "chemin": absolu, "pile": _pile(sys._getframe(1))})
        finally:
            _ETAT["actif"] = False
        if interdit:
            raise PermissionError(f"garde R1 de la revue v2 : {evenement} refusé sur {absolu}")


sys.addaudithook(_crochet)
