"""Greffon pytest de la revue par mutants (contre-lecture R2 du code de l'addendum 2 de P3).

Garde R1 : un crochet d'audit (`sys.addaudithook`) refuse toute ouverture, par ce processus, d'un fichier du dépôt de
travail sous `donnees/`, `diag/`, `runs/`, `traces/`, et de `prereg/P3-consignes-v1.md` ; chaque refus est journalisé
(il doit n'y en avoir aucun). Il trace aussi, avec la pile d'appel (fichier et fonction), chaque ouverture d'un fichier
des textes d'action (`textes-actions`) ou des scores par jeton (`jetons-principales`) dans les dépôts jouets : preuve que
le module ne les lit pas lui-même (seuls le chargeur gelé et le hachage les ouvrent).

Variables : REVUE_JOURNAL_R1 (chemin du journal JSONL, obligatoire).
"""
import json
import os
import sys

DEPOT = "/home/user/controle-ia-travail"
INTERDITS = tuple(os.path.join(DEPOT, x) for x in ("donnees", "diag", "runs", "traces")) + (
    os.path.join(DEPOT, "prereg", "P3-consignes-v1.md"),)
TRACES = ("textes-actions", "jetons-principales")
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


def _crochet(evenement, args):
    if evenement != "open" or _ETAT["actif"]:
        return
    chemin = args[0] if args else None
    if isinstance(chemin, int) or chemin is None:
        return
    try:
        chemin = os.fsdecode(chemin)
    except TypeError:
        return
    absolu = os.path.abspath(chemin)
    interdit = any(absolu == x or absolu.startswith(x + os.sep) for x in INTERDITS)
    trace = any(t in absolu for t in TRACES)
    if not (interdit or trace):
        return
    _ETAT["actif"] = True
    try:
        mode = args[1] if len(args) > 1 else None
        _ecrire({"refus": interdit, "chemin": absolu, "mode": str(mode), "pile": _pile(sys._getframe(1))})
    finally:
        _ETAT["actif"] = False
    if interdit:
        raise PermissionError(f"garde R1 de la revue : ouverture refusée de {absolu}")


sys.addaudithook(_crochet)
