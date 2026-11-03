#!/usr/bin/env python3
"""Configurations v2 de la course Kirchner Q2 (trois variantes) — sous-agent de session-depot, 3 novembre 2026.

v2 = configuration v1 (gardée, R12) dont seuls changent, après la contre-lecture de la fiche brouillon 1 : la consigne de
l'aiguilleur (v2, CLK-02), la source du substitut Gu-Krenn (v2, CLK-01), le repère de consigne de l'aiguilleur, `_lisez_moi`.
Le reste est inchangé (vérifié par `course_kirchner_v1`). Refuse d'écraser (R12).
  python3 -I -B construire_configurations_kirchner_v2.py
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))


def piece(p):
    with open(os.path.join(ICI, p), "rb") as f:
        return {"chemin": p, "sha256": hashlib.sha256(f.read()).hexdigest()}


def principal():
    for v in ("sans-kimi", "avec-kimi", "cinq-especes"):
        dst = os.path.join(ICI, f"configuration-course-kirchner-q2-v2-{v}.json")
        if os.path.exists(dst):
            raise SystemExit(f"{dst} existe déjà (R12)")
        c = json.load(open(os.path.join(ICI, f"configuration-course-kirchner-q2-v1-{v}.json"), encoding="utf-8"))
        c["pieces"]["consigne_aiguilleur"] = piece("pieces/consigne-aiguilleur-kirchner-v2.md")
        c["pieces"]["source_gu_krenn"] = piece("pieces/source-gu-krenn-kirchner-v2.json")
        c["bisociateur"]["gu_krenn"]["source"] = piece("pieces/source-gu-krenn-kirchner-v2.json")
        c["canaris"]["consigne_aiguilleur"] = "KQ2-AIGUILLEUR-3d9a61f0"
        c["_lisez_moi"] = c["_lisez_moi"].replace(", v1 — écrite par calcul_devis_course_kirchner_v1.py",
                                                  ", v2 — v1 (gardée, R12) modifiée par construire_configurations_kirchner_v2.py (aiguilleur v2, "
                                                  "source Gu-Krenn v2) ; v1 écrite par calcul_devis_course_kirchner_v1.py")
        assert ", v2 — v1" in c["_lisez_moi"]
        with open(dst, "x", encoding="utf-8") as f:
            f.write(json.dumps(c, ensure_ascii=False, indent=1) + "\n")
        print("écrit :", os.path.basename(dst))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
