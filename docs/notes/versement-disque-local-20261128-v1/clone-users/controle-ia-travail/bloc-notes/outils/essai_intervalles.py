# Essai de la regle des intervalles (VC-06) : motifs gelés recopiés de rubrique.py l. 40-41 (sans importer le dépôt).
import re
_FRACTION = re.compile(r"^([+-]?\d+)\s*/\s*(\d+)(?!\d)")
_ENTIER = re.compile(r"^([+-]?\d+)(?:\.0+)?(?=$|[\s,;)\]]|\.(?!\d))")
_SUITE = re.compile(r"\s*(?:-|–|—|to|or)\s*[+-]?\d", re.I)
def intervalle(valeur):
    s = valeur.strip().replace("−", "-")
    m = _FRACTION.match(s) or _ENTIER.match(s)
    return bool(m and _SUITE.match(s[m.end():]))
cas = ["3", "3 - 4", "3 – 4", "3 — 4", "3 to 4", "3 To 4", "3 or 4", "4/5 - 5/5", "4.0 to 5.0",
       "3 -4", "3 - solid", "3 (competent)", "4, solid", "2 of the proposals", "3-4", "3–4", "3 or more",
       "4/5", "4.0", "3 − 4", "5 - 1 weak point", "3 and 4", "3, 4"]
for c in cas:
    print(f"{c!r:24} -> {'intervalle' if intervalle(c) else '-'}")
