"""Lecture de la liste réelle des noms refusés pour les essais du lot 2 v5 (décision de la mère R-4500) : **aucune copie de
la liste n'est dans le paquet**. Elle est lue à son chemin sur la branche principale, à son empreinte scellée, et rien d'elle
n'est écrit nulle part : `git show` rend ses octets en mémoire. Aucun nom n'est écrit dans ce fichier.

Source, dans cet ordre :
1. `NA_LISTE_REELLE_FICHIER` : un chemin sur disque, si la variable est donnée ;
2. sinon le dépôt `NA_LISTE_REELLE_DEPOT` (par défaut `/home/user/controle-ia-travail-organisme`), à la référence
   `NA_LISTE_REELLE_REF` (par défaut `origin/main`), au chemin `CHEMIN_DEPOT`, lu par `git -C DEPOT show REF:CHEMIN`.

Les mêmes valeurs peuvent être passées en arguments à `lire_liste_reelle`. L'empreinte est vérifiée ; une liste absente,
illisible ou d'une autre empreinte lève `ListeReelleIndisponible` : l'essai qui la lit **échoue**, il ne saute jamais (R5).
"""

import hashlib
import os
import subprocess

CHEMIN_DEPOT = "docs/notes/ideation-seuil-moniteurs-v1/motifs-refuses-v1/motifs-noms-refuses-reels-v1.txt"
EMPREINTE = "583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813"
DEPOT_PAR_DEFAUT = "/home/user/controle-ia-travail-organisme"
REF_PAR_DEFAUT = "origin/main"
LIGNES_ATTENDUES = 34


class ListeReelleIndisponible(RuntimeError):
    """La liste réelle manque, ne se lit pas, ou n'a pas son empreinte : l'essai échoue."""


def octets_liste_reelle(fichier=None, depot=None, ref=None):
    """Rend les octets de la liste réelle, à leur empreinte vérifiée ; sinon lève `ListeReelleIndisponible`."""
    fichier = fichier or os.environ.get("NA_LISTE_REELLE_FICHIER")
    if fichier:
        try:
            with open(fichier, "rb") as f:
                octets = f.read()
        except OSError as e:
            raise ListeReelleIndisponible(f"liste réelle illisible sur disque ({type(e).__name__})") from None
        source = "fichier"
    else:
        depot = depot or os.environ.get("NA_LISTE_REELLE_DEPOT") or DEPOT_PAR_DEFAUT
        ref = ref or os.environ.get("NA_LISTE_REELLE_REF") or REF_PAR_DEFAUT
        try:
            r = subprocess.run(["git", "-C", depot, "show", f"{ref}:{CHEMIN_DEPOT}"], capture_output=True, check=False)
        except OSError as e:
            raise ListeReelleIndisponible(f"git indisponible ({type(e).__name__})") from None
        if r.returncode != 0:
            raise ListeReelleIndisponible(f"liste réelle absente du dépôt {depot} à {ref} (code {r.returncode})")
        octets = r.stdout
        source = f"{depot}@{ref}"
    if hashlib.sha256(octets).hexdigest() != EMPREINTE:
        raise ListeReelleIndisponible(f"empreinte de la liste réelle ({source}) différente de celle qui est scellée")
    return octets


def lire_liste_reelle(fichier=None, depot=None, ref=None):
    """Rend les expressions de la liste (lignes de la forme `\\bnom\\b`) ; les lignes vides et celles qui commencent par
    « # » sont des commentaires."""
    lignes = [l.strip() for l in octets_liste_reelle(fichier, depot, ref).decode("utf-8").split("\n")]
    return [l for l in lignes if l and not l.startswith("#")]
