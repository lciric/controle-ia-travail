"""Règle des intervalles du brouillon 3 (« Métrique », étape 5), enchaînée avec la fonction gelée `lire_une_note`.

Usage : PYTHONPATH=<clone>/src python essai_intervalles_suite.py
Valeurs écrites à la main ; aucune réponse de juge n'est lue. La règle est reprise du texte du brouillon 3 et de
`travail/essai_intervalles.py` ; les motifs gelés sont importés du dépôt (`rubrique.py`, l. 40-41).
"""
import re

from controle_ia.environnements.rubrique import _ENTIER, _FRACTION, lire_une_note

_SUITE = re.compile(r"\s*(?:-|–|—|to|or)\s*[+-]?\d", re.I)


def lire(valeur):
    s = valeur.strip().replace("−", "-")
    m = _FRACTION.match(s) or _ENTIER.match(s)
    if m and _SUITE.match(s[m.end():]):
        return "invalide (intervalle)"
    v = lire_une_note(valeur, 0, 5)
    return f"invalide ({v})" if isinstance(v, str) else f"lu {v}"


CAS = ["3 - 4", "3 to 4", "3 or 4", "4/5 - 5/5", "4.0 to 5.0", "3 - solid", "3 or more", "2 of the proposals",
       "3, 4", "3 and 4", "3 (4)", "3 (or 4)", "3; 4", "3 ~ 4", "3/5, 4/5", "3/5 (4/5)", "3 / 4", "3-4", "3 out of 5",
       "2 or 3 of the proposals", "3 - 4 proposals are strong"]
for c in CAS:
    print(f"{c!r:30} -> {lire(c)}")
