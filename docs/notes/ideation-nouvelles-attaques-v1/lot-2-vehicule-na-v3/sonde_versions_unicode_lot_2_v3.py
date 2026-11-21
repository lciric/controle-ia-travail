"""Sonde des versions d'Unicode, lot 2 v3 du véhicule NA-1 (programme écrit sur disque, jamais du code en ligne).

Rend, pour l'interpréteur qui la joue : la version de Python, `unicodedata.unidata_version`, la présence du module `regex`.
Si `regex` est présent : sa version, la plus haute valeur de la propriété « Age » qu'il connaît (donc sa version
d'Unicode), le nombre de points « Default_Ignorable_Code_Point » à sa version, et, parmi eux, ceux dont l'âge dépasse la
version d'Unicode donnée en argument (les points neufs depuis cette version), avec ceux qui sont non assignés à cette
version selon `unicodedata` (catégorie « Cn »). Aucune plage n'est écrite ici : c'est une mesure.

Usage : `INTERPRETE -I sonde_versions_unicode_lot_2_v3.py [VERSION_DE_COMPARAISON]`
"""

import json
import sys
import unicodedata

rendu = {"python": sys.version.split()[0], "executable": sys.executable,
         "unicodedata_unidata_version": unicodedata.unidata_version}
try:
    import regex
except ImportError:
    regex = None
rendu["regex_present"] = regex is not None

if regex is not None:
    rendu["regex_version"] = regex.__version__
    ages = {}
    for majeur in range(1, 30):
        for mineur in range(0, 3):
            for v in (f"{majeur}.{mineur}", f"V{majeur}_{mineur}"):
                try:
                    regex.compile(r"\p{Age=" + v + "}")
                except regex.error:
                    continue
                ages[f"{majeur}.{mineur}"] = v
                break
    rendu["regex_ages_connus"] = list(ages)
    rendu["regex_age_le_plus_haut"] = list(ages)[-1] if ages else None
    tous = "".join(chr(c) for c in range(0x110000) if not 0xD800 <= c <= 0xDFFF)
    di = [ord(ch) for ch in regex.findall(r"\p{Default_Ignorable_Code_Point}", tous)]
    rendu["regex_di_points"] = len(di)
    if len(sys.argv) > 1:
        version = sys.argv[1]
        # « Age » d'un point : la version où il fut assigné ; un point est neuf depuis `version` s'il n'a l'âge d'aucune
        # version jusqu'à elle comprise (les non assignés n'ont aucun âge : ils sont comptés à part).
        jusqu_a = [ages[v] for v in ages if tuple(map(int, v.split("."))) <= tuple(map(int, version.split(".")))]
        motif_age = regex.compile("|".join(r"\p{Age=" + a + "}" for a in jusqu_a)) if jusqu_a else None
        assigne = regex.compile(r"\p{Assigned}")
        neufs = [c for c in di if assigne.match(chr(c)) and (motif_age is None or not motif_age.match(chr(c)))]
        rendu["comparaison_ages_utilises"] = jusqu_a[-3:]
        rendu["comparaison"] = {
            "version": version,
            "di_dont_l_age_depasse_la_version": len(neufs),
            "di_non_assignes_selon_unicodedata_local": sum(1 for c in di if unicodedata.category(chr(c)) == "Cn"),
            "exemples_hexadecimaux": [f"U+{c:04X}" for c in neufs[:12]],
        }
    rendu["quatre_points_du_verificateur_di"] = {
        f"U+{c:04X}": regex.match(r"\p{Default_Ignorable_Code_Point}", chr(c)) is not None
        for c in (0xFE0F, 0x034F, 0x3164, 0x2800)}

print(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1))
