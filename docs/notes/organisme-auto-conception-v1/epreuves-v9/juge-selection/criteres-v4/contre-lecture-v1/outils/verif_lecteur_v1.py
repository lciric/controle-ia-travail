# -*- coding: utf-8 -*-
"""Vérification du contre-lecteur (modèle O) — v1 : D du lecteur par programme sur des phrases inventées.
Usage : python3 -B verif_lecteur_v1.py DOSSIER_DES_COPIES
"""
import sys

sys.path.insert(0, sys.argv[1])
import lecteur_par_programme_cartes_v1 as L  # noqa: E402

conf = {"champ_refutation": "ref", "champs_voie": ["titre"], "hors_choix": []}
cas = [
    "Si le bras ne bat pas le témoin, ne pas adopter.",
    "Sinon, garder la base.",
    "Si l'écart est nul, ne pas retenir le module.",
    "Si l'écart est nul, retirer le module.",
    "L'écart reste sous le seuil.",
]
for phrase in cas:
    r = L.lire_carte({"ref": phrase, "titre": "sablier synthétique"}, conf)
    print(f"{phrase!r} -> D = {r['D']} (non nommé : {r['non_nomme']}, oui nommé : {r['oui_nomme']}) ; voie = {r['voie']}")
