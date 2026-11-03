#!/usr/bin/env python3
"""Configurations v2 de la course Heimersheim (trois variantes) — sous-agent de session-depot, 3 novembre 2026.

v2 = configuration v1 (gardée, R12) dont seuls changent, suite à la contre-lecture de la fiche brouillon 2 : la consigne de
l'aiguilleur (v2, CLH-02), la consigne du lecteur (v2, CLH-11), la source du substitut Gu-Krenn (v2, CLH-05), la garde lexicale
(« gpt » → « gpt 6 », « gpt6 », « gpt-6 », CLH-03), les repères de consigne de l'aiguilleur et du lecteur, le texte `_lisez_moi`.
Budget, plafonds de session, relais, commandes, proposeurs et rôles : inchangés (vérifiés par `course_heimersheim_v2`).
Refuse d'écraser (R12).  python3 -I -B construire_configurations_heimersheim_v2.py
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))
sys.path.insert(0, ICI)
import course_heimersheim_v2 as ch  # noqa: E402

VARIANTES = ("sans-kimi", "avec-kimi", "cinq-especes")


def piece(p):
    with open(os.path.join(ICI, p), "rb") as f:
        return {"chemin": p, "sha256": hashlib.sha256(f.read()).hexdigest()}


def principal():
    for v in VARIANTES:
        src = os.path.join(ICI, f"configuration-course-heimersheim-v1-{v}.json")
        dst = os.path.join(ICI, f"configuration-course-heimersheim-v2-{v}.json")
        if os.path.exists(dst):
            raise SystemExit(f"{dst} existe déjà (R12)")
        c = json.load(open(src, encoding="utf-8"))
        c["pieces"]["consigne_aiguilleur"] = piece("pieces/consigne-aiguilleur-heimersheim-v2.md")
        c["pieces"]["consigne_lecteur"] = piece("pieces/consigne-lecteur-heimersheim-v2.md")
        c["pieces"]["source_gu_krenn"] = piece("pieces/source-gu-krenn-heimersheim-v2.json")
        c["bisociateur"]["gu_krenn"]["source"] = piece("pieces/source-gu-krenn-heimersheim-v2.json")
        c["etiquettes_interdites"] = list(ch.ETIQUETTES_EXIGEES)
        c["canaris"]["consigne_aiguilleur"] = "HQ1-AIGUILLEUR-5c1e9a27"
        c["canaris"]["consigne_lecteur"] = "HQ1-LECTEUR-d4b7203e"
        c["_lisez_moi"] = c["_lisez_moi"].replace(", v1 — écrite par calcul_devis_course_heimersheim_v1.py le 3 novembre 2026",
                                                  ", v2 — v1 (gardée, R12) modifiée par construire_configurations_heimersheim_v2.py le 3 novembre 2026 "
                                                  "(aiguilleur v2, lecteur v2, source Gu-Krenn v2, garde lexicale CLH-03)")
        assert ", v2 — v1" in c["_lisez_moi"]
        with open(dst, "x", encoding="utf-8") as f:
            f.write(json.dumps(c, ensure_ascii=False, indent=1) + "\n")
        print("écrit :", os.path.basename(dst))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
