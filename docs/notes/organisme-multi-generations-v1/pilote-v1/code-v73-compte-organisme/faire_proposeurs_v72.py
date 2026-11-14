"""Écrit pole/proposeurs_pilote_v72.py depuis la fonction lire_configuration de la v70 (recopiée, version exigée changée)."""
import sys
racine = sys.argv[1]
src = open(f"{racine}/pole/proposeurs_pilote_v70.py", encoding="utf-8").read().splitlines(keepends=True)
debut = next(i for i, l in enumerate(src) if l.startswith("def lire_configuration("))
fin = next(i for i, l in enumerate(src) if l.startswith("def verifier_section_sonde("))
corps = "".join(src[debut:fin]).rstrip("\n") + "\n"
vieux = 'if conf.get("version") != "configuration-pilote-mr2-v11":\n        raise Refus("configuration : version « configuration-pilote-mr2-v11 » exigée")'
assert corps.count(vieux) == 1
corps = corps.replace(vieux, 'if conf.get("version") != VERSION_CONFIGURATION:\n        raise Refus(f"configuration : version « {VERSION_CONFIGURATION} » exigée")')
assert corps.count("    verifier_section_sonde(conf, props)") == 1
corps = corps.replace("    verifier_section_sonde(conf, props)", "    _V70.verifier_section_sonde(conf, props)")
assert "v11" not in corps
entete = '''"""Lecture de la configuration v12 du pilote MR-2 — code v72 (fichier neuf, R12 ; `proposeurs_pilote_v70.py` reste en place,
inchangé, et sert tout le reste : relais, appels, lignes de GO, parts de la sonde, empreinte de la configuration).

Pourquoi ce module : la fonction `lire_configuration` de la v70 exige la version « configuration-pilote-mr2-v11 » ; la
configuration v12 (consignes de la sonde réécrites pour faire réfléchir les proposeurs, R-2621) ne peut donc être lue que par une
fonction neuve, sans réécrire un fichier (R12). `lire_configuration` ci-dessous est **la fonction de la v70 recopiée**, dont seule
la version exigée change (« configuration-pilote-mr2-v12 ») ; les contrôles qu'elle appelle sont ceux de la v70, appelés depuis
son module (`verifier_section_sonde` comprise). Un essai compare les deux textes (même code hormis la version exigée et l'appel
qualifié de `verifier_section_sonde`). Aucun réseau ici.
"""

import json
import math
import os

from . import proposeurs_pilote_v70 as _V70
from .outils import sha256_fichier
from .pilote_mr2_v70 import PROPOSEURS, Refus
from .proposeurs_pilote_v70 import CHAMPS_PROPOSEUR, URL_AMONT, amont_boucle_locale, borne_de_sortie_max

VERSION = "proposeurs-pilote-v72"
VERSION_CONFIGURATION = "configuration-pilote-mr2-v12"


'''
pied = '''

__all__ = ["VERSION", "VERSION_CONFIGURATION", "lire_configuration"]
'''
open(f"{racine}/pole/proposeurs_pilote_v72.py", "x", encoding="utf-8").write(entete + corps + pied)
