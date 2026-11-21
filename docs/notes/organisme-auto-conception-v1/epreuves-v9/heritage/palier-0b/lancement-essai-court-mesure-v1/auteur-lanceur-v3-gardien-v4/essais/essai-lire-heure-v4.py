"""Essai de lire_heure_arret du gardien v4 sur des valeurs connues ; secondes calculées à la main (écrites en littéraux).

Calculs à la main :
  1970-01-01T00:00:00Z : 0.
  2026-11-21T00:00:00Z : années 1970 à 2025 = 56 × 365 + 14 bissextiles (1972 à 2024) = 20 454 jours ; du 1er janvier au
    21 novembre 2026 : 31+28+31+30+31+30+31+31+30+31 = 304, + 20 = 324 jours ; 20 778 × 86 400 = 1 795 219 200 s.
  2026-11-25T17:00:00Z (H0 = 2026-11-21T19:00:00Z, plus 94 h) : 1 795 219 200 + 19 × 3 600 + 94 × 3 600 = 1 795 219 200
    + 406 800 = 1 795 626 000 s ; et 4 × 86 400 + 17 × 3 600 = 406 800 : même valeur, par le jour et l'heure.
  2028-02-29T12:00:00Z (jour bissextile) : accepté.
Refus attendus (ValueError) : formats autres, dates impossibles.
Usage : essai-lire-heure-v4.py CHEMIN_DU_GARDIEN
"""
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("gardien", sys.argv[1])
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

acceptes = [("1970-01-01T00:00:00Z", 0.0), ("2026-11-21T00:00:00Z", 1_795_219_200.0),
            ("2026-11-25T17:00:00Z", 1_795_626_000.0), ("2028-02-29T12:00:00Z", None)]
refuses = ["Sat Nov 21 18:50:00 UTC 2026", "2026-11-21T19:00:00", "2026-11-21 19:00:00Z", "2026-11-31T10:00:00Z",
           "2026-11-21T24:00:00Z", "2027-02-29T12:00:00Z", "", "2026-11-21T19:00:00.5Z", "2026-11-21T19:00:00+01:00",
           "2026-11-21t19:00:00z", " 2026-11-21T19:00:00Z", "2026-11-21T19:00:00Z\n", "２０２６-11-21T19:00:00Z",
           "2026-11-21T19:60:00Z", "2026-13-01T00:00:00Z"]
echecs = 0
for texte, attendu in acceptes:
    try:
        obtenu = G.lire_heure_arret(texte)
        ok = attendu is None or abs(obtenu - attendu) < 1e-6
    except ValueError as e:
        obtenu, ok = f"refusé ({e})", False
    echecs += not ok
    print(f"accepté attendu : {texte!r} ; attendu {attendu} ; obtenu {obtenu} ; {'TENU' if ok else 'CASSÉ'}")
for texte in refuses:
    try:
        obtenu = G.lire_heure_arret(texte)
        ok = False
    except ValueError as e:
        obtenu, ok = f"refusé ({e})", True
    echecs += not ok
    print(f"refus attendu : {texte!r} ; obtenu {obtenu} ; {'TENU' if ok else 'CASSÉ'}")
print("échecs :", echecs)
sys.exit(1 if echecs else 0)
