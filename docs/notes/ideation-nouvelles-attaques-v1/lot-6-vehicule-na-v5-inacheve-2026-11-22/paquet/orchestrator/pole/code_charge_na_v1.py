"""Véhicule NA-1, lot 6 v5 — contrôle d'empreinte du code chargé (`code_charge_na_v1`) : additif v2, C-1 à C-4 ; arrêt
n° 33 (proposé). Repris du lot 6 v4 (`course_na_v4.py`, `285a6353…`), fonctions `lire_table_empreintes`,
`verifier_code_charge`, `RESERVE_C3`, sans changement de règle ; seul le module change (R12).

C-1 : pour chaque module chargé qui vit sous la racine du paquet, ou dont le nom est dans un espace protégé, l'empreinte du
fichier source est celle de la table ; hors table, autre empreinte, source absente, hors racine : arrêt n° 33. C-3, réserve
déclarée : une modification en mémoire n'est pas vue. Bibliothèque standard seule.
"""

import hashlib
import os
import re
import sys

VERSION = "code-charge-na-v1"
NUMERO_ARRET_CODE_CHARGE = 33
NUMERO_ARRET = NUMERO_ARRET_CODE_CHARGE
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


class ArretNommeV4(RuntimeError):
    numero = None
    nom = None


class ArretCodeChargeNA(ArretNommeV4):
    """N° 33 : module chargé hors table, ou d'une autre empreinte, ou sans source lisible ; départ ou génération refusé."""

    numero = NUMERO_ARRET_CODE_CHARGE
    nom = "code chargé hors table ou d'une autre empreinte"

    def __init__(self, moment, module, cause):
        super().__init__(f"arrêt n° {self.numero}, {self.nom} ({moment}) : module « {module} » ; {cause}")
        self.moment, self.module, self.cause = moment, module, cause


def lire_table_empreintes(chemin, sha256_attendu):
    """La table d'empreintes du paquet (`<sha256>  <chemin relatif>` par ligne), vérifiée à son empreinte ; rend
    {chemin relatif normalisé : sha256}."""
    with open(chemin, "rb") as f:
        octets = f.read()
    if hashlib.sha256(octets).hexdigest() != sha256_attendu:
        raise ArretCodeChargeNA("lecture de la table", os.path.basename(chemin), "table d'une autre empreinte")
    table = {}
    for ligne in octets.decode("utf-8").splitlines():
        if not ligne.strip():
            continue
        h, _, rel = ligne.partition("  ")
        if not _HEX64.match(h) or not rel or os.path.isabs(rel) or ".." in rel.split("/"):
            raise ArretCodeChargeNA("lecture de la table", os.path.basename(chemin), "ligne hors forme")
        if rel in table:
            raise ArretCodeChargeNA("lecture de la table", rel, "chemin deux fois")
        table[os.path.normpath(rel)] = h
    return table


def verifier_code_charge(table, racine, moment, *, espaces_proteges=("pole",), modules=None):
    """C-1 : pour chaque module de `sys.modules` (ou `modules`) dont le fichier vit sous `racine`, ou dont le nom est dans
    un espace protégé, l'empreinte du fichier source est celle de la table. Refus (n° 33) : module protégé sans fichier
    source `.py`, fichier hors de la racine, fichier hors table, autre empreinte. Rend la liste triée des chemins vérifiés.
    C-3 : ne voit pas une modification en mémoire (ce n'est pas le fichier qui change)."""
    racine = os.path.realpath(racine)
    modules = sys.modules if modules is None else modules
    vus = []
    for nom, m in sorted(list(modules.items()), key=lambda e: e[0]):
        if m is None:
            continue
        fichier = getattr(m, "__file__", None)
        protege = any(nom == p or nom.startswith(p + ".") for p in espaces_proteges)
        reel = os.path.realpath(fichier) if isinstance(fichier, str) else None
        sous_racine = reel is not None and (reel == racine or reel.startswith(racine + os.sep))
        if not protege and not sous_racine:
            continue
        chemins = getattr(m, "__path__", None)
        if fichier is None and chemins is not None and getattr(getattr(m, "__spec__", None), "origin", None) is None:
            # paquet d'espace de noms : aucun fichier ; chacun de ses dossiers doit être sous la racine
            if not all(os.path.realpath(c).startswith(racine + os.sep) for c in list(chemins)):
                raise ArretCodeChargeNA(moment, nom, "paquet d'espace de noms hors de la racine du paquet")
            continue
        if reel is None or not reel.endswith(".py"):
            raise ArretCodeChargeNA(moment, nom, "aucun fichier source lisible")
        if not sous_racine:
            raise ArretCodeChargeNA(moment, nom, "fichier hors de la racine du paquet")
        rel = os.path.normpath(os.path.relpath(reel, racine))
        if rel not in table:
            raise ArretCodeChargeNA(moment, nom, "module hors table")
        try:
            with open(reel, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
        except OSError:
            raise ArretCodeChargeNA(moment, nom, "fichier source illisible") from None
        if h != table[rel]:
            raise ArretCodeChargeNA(moment, nom, "autre empreinte que celle de la table")
        vus.append(rel)
    return sorted(vus)


RESERVE_C3 = ("C-3, réserve déclarée : le contrôle compare les fichiers sources aux empreintes de la table ; il ne voit "
              "pas une modification en mémoire (méthode vidée sur une classe, `__code__` échangé, objet remplacé après "
              "le contrôle).")


def controle_sur_table(chemin_table, sha256_table, racine, espaces_proteges=("pole",)):
    """La fonction que la course reçoit (`controle_code_charge`) : lit la table à son empreinte une fois, puis vérifie
    `sys.modules` à chaque moment."""
    table = lire_table_empreintes(chemin_table, sha256_table)

    def controler(moment):
        return verifier_code_charge(table, racine, moment, espaces_proteges=espaces_proteges)
    return controler


__all__ = ("ArretCodeChargeNA", "lire_table_empreintes", "verifier_code_charge", "controle_sur_table", "RESERVE_C3",
           "NUMERO_ARRET")
