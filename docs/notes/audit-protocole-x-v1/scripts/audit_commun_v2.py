"""Outils communs de l'audit du protocole X, version 2 (remplace la v1 pour les scripts du jalon 3 : graines par SHA-256 du nom de tâche).

Aucun appel réseau. Graines dérivées par numpy.random.SeedSequence (règle R9).
"""
import json
import math
import re
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path

import numpy as np
import os

RACINE_DEPOT = Path(__file__).resolve().parents[4]
os.chdir(RACINE_DEPOT)  # les chemins git sont relatifs à la racine du dépôt

ICI = Path(__file__).resolve().parent
SORTIES = ICI.parent / "sorties"
GRAINE_RACINE = 20261124  # graine racine de l'audit ; chaque tâche en dérive par spawn_key

ESPECE_FOURNISSEUR = {
    "fable": "Anthropic", "opus": "Anthropic", "opus46": "Anthropic", "fable51": "Anthropic",
    "argon": "Google", "carbon": "Google", "neon": "Google",
    "astra": "OpenAI", "kimi": "Moonshot",
}


def graine(tache, derivation="sha256"):
    """Générateur dérivé de la graine racine pour une tâche nommée.

    derivation="sha256" (défaut) : clé = 4 premiers octets du SHA-256 du nom de tâche.
    derivation="v0" : clé = 8 premiers octets du nom (première version ; des noms au même début
    partagent la clé). Gardée seulement pour rejouer les deux échantillons codés à la main
    (précision des unités, étiquettes « VÉRIFIÉ »), tirés avec elle.
    """
    import hashlib
    if derivation == "v0":
        cle = int.from_bytes(tache.encode("utf-8")[:8].ljust(8, b"\0"), "little") % (2 ** 32)
    else:
        cle = int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:4], "little")
    ss = np.random.SeedSequence(GRAINE_RACINE, spawn_key=(cle,))
    return np.random.default_rng(ss), {"racine": GRAINE_RACINE, "spawn_key": [cle], "tache": tache, "derivation": derivation}


def montrer(branche, chemin):
    r = subprocess.run(["git", "show", f"origin/{branche}:{chemin}"], capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None


def lister(branche, prefixe=""):
    args = ["git", "ls-tree", "-r", "--name-only", f"origin/{branche}"] + ([prefixe] if prefixe else [])
    return [x for x in subprocess.run(args, capture_output=True, text=True).stdout.split("\n") if x]


def inventaire():
    return json.loads((SORTIES / "inventaire-v1.json").read_text())


VIDES = set("""le la les un une des du de d l et ou en au aux a à ce cet cette ces se sa son ses sur sous par pour pas
plus ne que qui quoi dont où est sont être été avoir a ont il elle ils elles on nous vous je tu y si mais donc car
ni comme avec sans dans entre vers chez leur leurs lui même tout tous toute toutes autre autres fait faire peut
deux trois un une non oui très bien aussi alors puis chaque quand ici cela ça c s n qu m t lors avant après the of
and to in is for on that by with as be are this an it or from at not which can its""".split())


def mots(texte):
    t = unicodedata.normalize("NFKD", (texte or "").lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return [w for w in re.findall(r"[a-z][a-z0-9]{2,}", t) if w not in VIDES]


class Tfidf:
    def __init__(self, corpus):
        self.df = Counter()
        for d in corpus:
            self.df.update(set(mots(d)))
        self.n = len(corpus)

    def vec(self, texte):
        c = Counter(mots(texte))
        v = {w: (1 + math.log(k)) * math.log((1 + self.n) / (1 + self.df.get(w, 0))) for w, k in c.items()}
        nrm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {w: x / nrm for w, x in v.items()}


def cos(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(x * b.get(w, 0.0) for w, x in a.items())


def sections(texte):
    """Liste (niveau, titre, début, fin) des titres Markdown."""
    lignes = texte.split("\n")
    pos, out = 0, []
    for i, l in enumerate(lignes):
        m = re.match(r"^(#{1,6})\s+(.*)$", l)
        if m:
            out.append([len(m.group(1)), m.group(2).strip(), i])
    res = []
    for k, (niv, titre, i) in enumerate(out):
        fin = len(lignes)
        for niv2, _, j in out[k + 1:]:
            if niv2 <= niv:
                fin = j
                break
        res.append((niv, titre, i, fin))
    return res, lignes
