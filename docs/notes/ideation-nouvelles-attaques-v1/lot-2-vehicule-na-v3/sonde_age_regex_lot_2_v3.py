"""Seconde sonde, lot 2 v3 : la version d'Unicode du module `regex`, par sa table de propriétés et par le compte des
points assignés, comparés à `unicodedata` de l'interpréteur ; puis les points « Default_Ignorable_Code_Point » de `regex`
qui sont non assignés (« Cn ») selon cet `unicodedata`, rangés par leur assignation chez `regex`. Mesure seulement.

Usage : `.venv/bin/python -I sonde_age_regex_lot_2_v3.py`
"""

import json
import sys
import unicodedata

import regex
from regex import _regex_core as coeur

rendu = {"python": sys.version.split()[0], "unicodedata_unidata_version": unicodedata.unidata_version,
         "regex_version": regex.__version__}

table = getattr(coeur, "PROPERTIES", None)
noms_age = []
if isinstance(table, dict):
    noms_age = sorted(k for k in table if "AGE" in str(k).upper())
    rendu["regex_proprietes_age"] = noms_age
    for k in noms_age:
        valeurs = table[k][1] if isinstance(table[k], tuple) and len(table[k]) > 1 else None
        if isinstance(valeurs, dict):
            rendu.setdefault("regex_valeurs_age", {})[k] = sorted(valeurs, key=str)[-6:]
else:
    rendu["regex_proprietes_age"] = "table introuvable"

tous = "".join(chr(c) for c in range(0x110000) if not 0xD800 <= c <= 0xDFFF)
assignes_regex = set(ord(ch) for ch in regex.findall(r"\p{Assigned}", tous))
assignes_ud = set(c for c in range(0x110000) if not 0xD800 <= c <= 0xDFFF and unicodedata.category(chr(c)) != "Cn")
rendu["assignes_regex_hors_substituts"] = len(assignes_regex)
rendu["assignes_unicodedata_hors_substituts"] = len(assignes_ud)
rendu["assignes_chez_regex_seulement"] = len(assignes_regex - assignes_ud)
rendu["assignes_chez_unicodedata_seulement"] = len(assignes_ud - assignes_regex)

di = set(ord(ch) for ch in regex.findall(r"\p{Default_Ignorable_Code_Point}", tous))
neufs_di = sorted(di & (assignes_regex - assignes_ud))
rendu["di_regex"] = len(di)
rendu["di_assignes_chez_regex_et_non_assignes_selon_unicodedata"] = len(neufs_di)
rendu["exemples"] = [f"U+{c:04X}" for c in neufs_di[:20]]
print(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1))
