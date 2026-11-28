"""Prototype de la correction proposée (RC-donnees-01, 02) : fenêtres glissantes de 48 caractères à pas de 24 sur chaque
texte honnête (toute fuite d'au moins 71 caractères contient une fenêtre entière), cherchées dans le texte brut de chaque
fichier ajouté et dans sa forme déséchappée (\\n, \\t, \\r, \\", \\', \\\\, \\uXXXX). Comptes seulement, aucun texte
affiché. Usage : python -I -B prototype_fenetres_v1.py TEXTES DEPOT S BRANCHE…  (lecture par git show, rien n'est écrit)"""
import json
import re
import subprocess
import sys

L, PAS = 48, 24


def fenetres(chemin):
    f = set()
    for brut in open(chemin, encoding="utf-8"):
        x = json.loads(brut)
        t = x.get("texte")
        if x.get("condition") != "honnete" or not isinstance(t, str) or len(t) < 64:
            continue
        debuts = list(range(0, len(t) - L + 1, PAS)) + [len(t) - L]
        f |= {t[i:i + L] for i in debuts if len(set(t[i:i + L])) > 1}
    return f


ECHAPPE = re.compile(r'\\(u[0-9a-fA-F]{4}|[ntr"\'\\/])')


def deseschapper(s):
    def r(m):
        c = m.group(1)
        return chr(int(c[1:], 16)) if c[0] == "u" else {"n": "\n", "t": "\t", "r": "\r"}.get(c, c)
    return ECHAPPE.sub(r, s)


def trouve(s, f):
    return sum(1 for i in range(len(s) - L + 1) if s[i:i + L] in f)


textes, depot, s = sys.argv[1:4]
f = fenetres(textes)
print(f"{len(f)} fenêtres glissantes (pas de {PAS})")
for b in sys.argv[4:]:
    noms = subprocess.run(["git", "-C", depot, "diff", "--name-only", "--diff-filter=A", s, b], capture_output=True,
                          text=True, check=True).stdout.split()
    n_brut = n_des = 0
    for nom in noms:
        if nom.endswith(".npz"):
            continue
        o = subprocess.run(["git", "-C", depot, "show", f"{b}:{nom}"], capture_output=True, check=True).stdout
        t = o.decode("utf-8", errors="replace")
        n_brut += trouve(t, f)
        n_des += trouve(deseschapper(t), f)
    print(f"{b} : {len(noms)} fichiers ajoutés ; fenêtres retrouvées : {n_brut} (brut), {n_des} (déséchappé)")
