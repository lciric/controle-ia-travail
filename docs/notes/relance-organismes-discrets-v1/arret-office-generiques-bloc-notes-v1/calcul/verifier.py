# -*- coding: utf-8 -*-
"""Contrôle et application des opérations sur une copie du brouillon 51 (le texte du dépôt n'est pas touché)."""
import hashlib
import importlib
import itertools
import json
import sys

TEXTE = sys.argv[1]
SORTIE = sys.argv[2]            # dossier de travail
ops_mod = importlib.import_module("ops")
OPS = ops_mod.OPS

brut = open(TEXTE, "rb").read()
assert hashlib.sha256(brut).hexdigest() == "6de63aabf773559b43574b25737b4b93f1d87ab3665603c462da1627cbaa97bf", "texte d'une autre empreinte"
texte = brut.decode("utf-8")
assert texte.endswith("\n")
LIGNES = texte[:-1].split("\n")      # LIGNES[i-1] = ligne i
N = len(LIGNES)

problemes = []

# --- 1. contrôles de forme
for k, op in enumerate(OPS):
    assert op["type"] in ("remplacer", "inserer_apres")
    assert 1 <= op["ligne"] <= N
    if op["type"] == "remplacer":
        a, n = op["ancien"], op["nouveau"]
        if "\n" in a or "\n" in n:
            problemes.append((k, "saut de ligne"))
        if a == n:
            problemes.append((k, "ancien = nouveau"))
        c = LIGNES[op["ligne"] - 1].count(a)
        if c != 1:
            problemes.append((k, f"ancien présent {c} fois dans la ligne {op['ligne']} d'origine"))
        tot = texte.count(a)
        op["_ailleurs"] = tot - c
        if a not in n:
            op["_ancien_garde"] = False
        else:
            op["_ancien_garde"] = True
    else:
        if "\n" in op["texte"]:
            problemes.append((k, "saut de ligne"))

# --- 2. ordre : du bas vers le haut
lignes_ops = [op["ligne"] for op in OPS]
if lignes_ops != sorted(lignes_ops, reverse=True):
    problemes.append(("ordre", "les opérations ne sont pas rangées du bas vers le haut"))
# une seule insertion par numéro de ligne
ins = [op["ligne"] for op in OPS if op["type"] == "inserer_apres"]
if len(ins) != len(set(ins)):
    problemes.append(("insertions", "deux insertions après la même ligne"))

# --- 3. application séquentielle, dans l'ordre écrit, sur les numéros courants
def appliquer_sequentiel(ops):
    L = list(LIGNES)
    for k, op in enumerate(ops):
        i = op["ligne"] - 1
        if op["type"] == "remplacer":
            c = L[i].count(op["ancien"])
            if c != 1:
                raise AssertionError(f"op {k} ligne {op['ligne']} : ancien présent {c} fois au moment de l'application")
            L[i] = L[i].replace(op["ancien"], op["nouveau"])
        else:
            L.insert(i + 1, op["texte"])
    return "\n".join(L) + "\n"

# --- 4. application par numéros de ligne d'origine (toutes les opérations d'une ligne, puis les insertions)
def appliquer_origine(ops, ordre_dans_la_ligne=None):
    par_ligne = {}
    for op in ops:
        par_ligne.setdefault(op["ligne"], []).append(op)
    out = []
    for i, x in enumerate(LIGNES, 1):
        lops = par_ligne.get(i, [])
        rem = [op for op in lops if op["type"] == "remplacer"]
        if ordre_dans_la_ligne is not None:
            rem = ordre_dans_la_ligne(rem)
        for op in rem:
            c = x.count(op["ancien"])
            if c != 1:
                raise AssertionError(f"ligne {i} : ancien présent {c} fois ({op['ancien'][:40]}…)")
            x = x.replace(op["ancien"], op["nouveau"])
        out.append(x)
        for op in lops:
            if op["type"] == "inserer_apres":
                out.append(op["texte"])
    return "\n".join(out) + "\n"

try:
    t_seq = appliquer_sequentiel(OPS)
    t_ori = appliquer_origine(OPS)
    if t_seq != t_ori:
        problemes.append(("application", "séquentiel et par numéros d'origine diffèrent"))
except AssertionError as e:
    problemes.append(("application", str(e)))
    t_seq = t_ori = None

# --- 5. indépendance de l'ordre à l'intérieur d'une ligne : toutes les permutations
if t_ori is not None:
    par_ligne = {}
    for op in OPS:
        if op["type"] == "remplacer":
            par_ligne.setdefault(op["ligne"], []).append(op)
    for i, rem in par_ligne.items():
        if len(rem) < 2:
            continue
        resultats = set()
        perms = list(itertools.permutations(rem)) if len(rem) <= 6 else [tuple(rem), tuple(reversed(rem))]
        for perm in perms:
            x = LIGNES[i - 1]
            ok = True
            for op in perm:
                if x.count(op["ancien"]) != 1:
                    ok = False
                    break
                x = x.replace(op["ancien"], op["nouveau"])
            resultats.add(x if ok else None)
        if len(resultats) != 1 or None in resultats:
            problemes.append((i, f"l'ordre des remplacements change le résultat de la ligne {i} ({len(perms)} ordres essayés)"))
        # ancres disjointes dans la ligne d'origine
        x = LIGNES[i - 1]
        places = sorted((x.find(op["ancien"]), x.find(op["ancien"]) + len(op["ancien"])) for op in rem)
        for (a1, b1), (a2, b2) in zip(places, places[1:]):
            if a2 < b1:
                problemes.append((i, "ancres qui se chevauchent"))

# --- 6. bilan
print("lignes d'origine :", N, "; opérations :", len(OPS),
      "dont remplacements :", sum(op["type"] == "remplacer" for op in OPS),
      "et insertions :", sum(op["type"] == "inserer_apres" for op in OPS))
for k, op in enumerate(OPS):
    if op["type"] == "remplacer":
        print(f"  {k:2d} remplacer    ligne {op['ligne']:4d} | {op['raison']:18s} | ancien {len(op['ancien']):4d} car., nouveau {len(op['nouveau']):4d} car. | ailleurs dans le fichier : {op['_ailleurs']} | ancien gardé en tête : {op['nouveau'].startswith(op['ancien'])}")
    else:
        print(f"  {k:2d} inserer_apres ligne {op['ligne']:4d} | {op['raison']:18s} | texte {len(op['texte']):4d} car.")
print("problèmes :", problemes if problemes else "aucun")

if t_ori is not None and not problemes:
    h = hashlib.sha256(t_ori.encode("utf-8")).hexdigest()
    open(SORTIE + "/texte-apres-application.md", "w", encoding="utf-8", newline="").write(t_ori)
    print("empreinte du texte après application :", h)
    print("lignes après application :", len(t_ori[:-1].split("\n")))
    # lignes changées
    apres = t_ori[:-1].split("\n")
    lignes_touchees = sorted({op["ligne"] for op in OPS if op["type"] == "remplacer"})
    print("lignes remplacées :", lignes_touchees)
    print("lignes insérées après :", sorted(op["ligne"] for op in OPS if op["type"] == "inserer_apres"))
    # vérifier que rien d'autre n'a changé
    inter = set(LIGNES)
    autres = 0
    it = iter(apres)
    j = 0
    # alignement simple : on retire les lignes insérées et on compare ligne à ligne
    inseres = {op["texte"] for op in OPS if op["type"] == "inserer_apres"}
    apres_sans = [x for x in apres if x not in inseres]
    assert len(apres_sans) == N
    diff = [i + 1 for i, (a, b) in enumerate(zip(LIGNES, apres_sans)) if a != b]
    print("lignes différentes après application (hors insertions) :", diff)
    assert diff == lignes_touchees
    # JSON propre
    propre = []
    for op in OPS:
        if op["type"] == "remplacer":
            propre.append({"type": "remplacer", "ligne": op["ligne"], "ancien": op["ancien"], "nouveau": op["nouveau"], "raison": op["raison"]})
        else:
            propre.append({"type": "inserer_apres", "ligne": op["ligne"], "texte": op["texte"], "raison": op["raison"]})
    bloc = json.dumps({"operations": propre}, ensure_ascii=False, indent=1)
    open(SORTIE + "/operations.json", "w", encoding="utf-8").write(bloc + "\n")
    print("bloc JSON écrit :", len(bloc), "caractères")
