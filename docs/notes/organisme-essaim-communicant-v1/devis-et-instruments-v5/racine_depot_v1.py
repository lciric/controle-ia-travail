#!/usr/bin/env python3
"""Racine du dépôt et chargement relogé des modules scellés qui portent un chemin absolu — v1 (réserve R1 de la
vérification de la v2). Bibliothèque standard seule. Aucun appel, aucun réseau.

Règle (aucun repli silencieux) :
1. la racine est le premier dossier parent de ce fichier qui contient `docs/sha256sums-lancement-v2.txt` (cas du dossier
   versé sous `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/`) ;
2. sinon (copie dans un bloc-notes), la variable d'environnement `DEPOT_CONTROLE_IA` doit nommer une racine qui contient ce
   même fichier ;
3. sinon : refus (exception `RacineIntrouvable`), jamais de chemin deviné.

Les chemins des pièces sont toujours écrits relatifs à la racine (`docs/...`, `src/...`).

`charger_reloge(rel, sha, remplacements, nom)` charge un module scellé (vérifié à son empreinte, inchangé sur disque) dont une
ou plusieurs lignes portent un chemin absolu : chaque remplacement (ancien → nouveau) doit apparaître **exactement une fois**,
sinon refus. Le module chargé est inscrit dans `sys.modules[nom]`, de sorte que les imports par nom le retrouvent.
"""
import hashlib
import importlib.util
import os
import sys

MARQUE = os.path.join("docs", "sha256sums-lancement-v2.txt")
VARIABLE = "DEPOT_CONTROLE_IA"
CHEMIN_ABSOLU_HISTORIQUE = "/home/user/controle-ia-travail"


class RacineIntrouvable(Exception):
    pass


def trouver_racine(depart=None):
    d = os.path.dirname(os.path.abspath(depart or __file__))
    while True:
        if os.path.isfile(os.path.join(d, MARQUE)):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    v = os.environ.get(VARIABLE)
    if v and os.path.isfile(os.path.join(v, MARQUE)):
        return os.path.abspath(v)
    raise RacineIntrouvable(f"racine du dépôt introuvable au-dessus de ce fichier ; donner {VARIABLE} (racine contenant {MARQUE})")


RACINE = trouver_racine()


def chemin(rel):
    if os.path.isabs(rel):
        raise RacineIntrouvable(f"chemin absolu refusé : {rel}")
    return os.path.join(RACINE, rel)


def sha_fichier(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def verifier_compagnon(rel):
    p = chemin(rel)
    s = sha_fichier(p)
    c = open(p + ".sha256", encoding="utf-8").read().split()[0]
    if s != c:
        raise RacineIntrouvable(f"{rel} : empreinte {s}, compagnon {c}")
    return s


def charger_reloge(rel, sha_attendu, remplacements, nom):
    p = chemin(rel)
    octets = open(p, "rb").read()
    s = hashlib.sha256(octets).hexdigest()
    if s != sha_attendu:
        raise RacineIntrouvable(f"{rel} : empreinte {s}, attendue {sha_attendu}")
    texte = octets.decode("utf-8")
    for ancien, nouveau in remplacements:
        n = texte.count(ancien)
        if n != 1:
            raise RacineIntrouvable(f"{rel} : le remplacement {ancien!r} apparaît {n} fois (une seule attendue)")
        texte = texte.replace(ancien, nouveau)
    spec = importlib.util.spec_from_loader(nom, loader=None, origin=p)
    m = importlib.util.module_from_spec(spec)
    m.__file__ = p
    sys.modules[nom] = m
    exec(compile(texte, p, "exec"), m.__dict__)
    m.SHA_SOURCE_SCELLEE = s
    m.SHA_SOURCE_RELOGEE = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    return m


# --- modules scellés de la v1 et du dossier inachevé, relogés -----------------------------------------------------------------
BASES_V1_REL = "docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/bases_sans_modele_v1.py"
BASES_V1_SHA = "29276c45e88eea80d3f7c1a33dfa5ef206cdb698c36f54ed04c6be56c33e2775"
RENF_REL = ("docs/notes/organisme-essaim-communicant-v1/en-cours-inacheve-2026-11-22-0700/"
            "essaim-glouton-renforce-test-de-mort-v1/base_gloutonne_renforcee_v1.py")
RENF_SHA = "b17c3bdb5754086cd53862a83ba885f812540412984b3683dab5ea65787d65bc"


def charger_bases_v1():
    if "bases_sans_modele_v1" in sys.modules:
        return sys.modules["bases_sans_modele_v1"]
    ancien = f'NOTES = "{CHEMIN_ABSOLU_HISTORIQUE}/docs/notes/organisme-multi-generations-v1"'
    nouveau = f'NOTES = {chemin("docs/notes/organisme-multi-generations-v1")!r}'
    return charger_reloge(BASES_V1_REL, BASES_V1_SHA, [(ancien, nouveau)], "bases_sans_modele_v1")


def charger_renforcee_v1():
    charger_bases_v1()
    if "base_gloutonne_renforcee_v1" in sys.modules:
        return sys.modules["base_gloutonne_renforcee_v1"]
    ancien = f'V1_DOSSIER = "{CHEMIN_ABSOLU_HISTORIQUE}/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1"'
    nouveau = f'V1_DOSSIER = {chemin("docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1")!r}'
    return charger_reloge(RENF_REL, RENF_SHA, [(ancien, nouveau)], "base_gloutonne_renforcee_v1")
