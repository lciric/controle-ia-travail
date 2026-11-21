"""Compare ce que le faux programme a reçu (dossier courant, PYTHONPATH, arguments) à la commande du complément 1 v3
(ligne « env -C … » de l'extraction redirigée), les trois chemins étant remplacés : racine, interpréteur, dossier des
sorties. Rend 0 et « ÉGAL » si tout est égal, 1 et la première différence sinon.

Emploi : python controler-argv.py COMPLEMENT RELEVE_DU_PROGRAMME RACINE INTERPRETE SORTIES
"""
import shlex
import sys

complement, releve, racine, interprete, sorties = sys.argv[1:6]
lignes = [l for l in open(complement, encoding="utf-8").read().splitlines() if l.startswith("env -C ")]
if len(lignes) != 1:
    print(f"ÉCHEC : {len(lignes)} lignes « env -C » dans le complément")
    sys.exit(1)
mots = shlex.split(lignes[0])
ANC_SORTIES = "/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-3"
ANC_PY = "/home/user/controle-ia-travail/.venv/bin/python"
ANC_RACINE = "/home/user/palier-0b-racine"


def remplacer(m):
    if m == ANC_SORTIES:
        return sorties
    if m == ANC_PY:
        return interprete
    if m == ANC_RACINE or m.startswith(ANC_RACINE + "/"):
        return racine + m[len(ANC_RACINE):]
    return m


mots = [remplacer(m) for m in mots]
assert mots[0] == "env" and mots[1] == "-C" and mots[3] == "PYTHONPATH=src" and mots[4] == interprete, mots[:5]
attendu = [f"cwd={mots[2]}", "PYTHONPATH=src"] + [f"arg={m}" for m in mots[5:]]
recu = [l for l in open(releve, encoding="utf-8").read().splitlines() if not l.startswith("faux programme")]
if recu == attendu:
    print(f"ÉGAL : {len(attendu)} lignes (dossier courant, PYTHONPATH, {len(attendu) - 2} arguments)")
    sys.exit(0)
for i, (a, b) in enumerate(zip(attendu, recu)):
    if a != b:
        print(f"ÉCHEC : ligne {i} : attendu « {a} », reçu « {b} »")
        sys.exit(1)
print(f"ÉCHEC : longueurs {len(attendu)} attendues, {len(recu)} reçues")
sys.exit(1)
