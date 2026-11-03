#!/usr/bin/env python3
"""Configurations v2 de la course Ibrahim Q1 (trois variantes) — sous-agent de session-depot, 3 novembre 2026.

v2 = configuration v1 (gardée, R12) dont seuls changent, après la contre-lecture de la fiche brouillon 1 :
- la source du substitut Gu-Krenn (v2, CLI-02), dans `pieces` et dans `bisociateur.gu_krenn.source` ;
- le nombre d'appels permis de chaque relais (CLI-01) : `max_appels` = 2 × appels du plan (devis v1, contrôles compris) + 5.
  Les plafonds en dollars des relais, S17 et les plafonds de session sont INCHANGÉS ; ils continuent de borner la dépense ;
- `_lisez_moi`.
Le reste est inchangé (vérifié par `course_ibrahim_v1` et par `test_course_ibrahim_v2.py`). Refuse d'écraser (R12).
  python3 -I -B construire_configurations_ibrahim_v2.py
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
VARIANTES = {"sans-kimi": "sans_kimi", "avec-kimi": "avec_kimi", "cinq-especes": "cinq_especes"}


def piece(p):
    with open(os.path.join(ICI, p), "rb") as f:
        return {"chemin": p, "sha256": hashlib.sha256(f.read()).hexdigest()}


def max_appels_v2(appels_plan):
    return 2 * appels_plan + 5


def principal():
    devis = json.load(open(os.path.join(ICI, "devis-course-ibrahim-v1.json"), encoding="utf-8"))
    for v, cle in VARIANTES.items():
        dst = os.path.join(ICI, f"configuration-course-ibrahim-q1-v2-{v}.json")
        if os.path.exists(dst):
            raise SystemExit(f"{dst} existe déjà (R12)")
        c = json.load(open(os.path.join(ICI, f"configuration-course-ibrahim-q1-v1-{v}.json"), encoding="utf-8"))
        src = piece("pieces/source-gu-krenn-ibrahim-v2.json")
        c["pieces"]["source_gu_krenn"] = src
        c["bisociateur"]["gu_krenn"]["source"] = dict(src)
        plan = devis["variantes"][cle]["par_fournisseur"]
        assert sorted(plan) == sorted(c["relais"]), (v, sorted(plan), sorted(c["relais"]))
        for f, r in c["relais"].items():
            r["max_appels"] = max_appels_v2(plan[f]["appels"])
        c["_lisez_moi"] = c["_lisez_moi"].replace(
            ", v1 — écrite par calcul_devis_course_ibrahim_v1.py",
            ", v2 — v1 (gardée, R12) modifiée par construire_configurations_ibrahim_v2.py (source Gu-Krenn v2, CLI-02 ; "
            "max_appels des relais = 2 × plan + 5, CLI-01 ; plafonds en dollars inchangés) ; v1 écrite par calcul_devis_course_ibrahim_v1.py")
        assert ", v2 — v1" in c["_lisez_moi"]
        with open(dst, "x", encoding="utf-8") as f:
            f.write(json.dumps(c, ensure_ascii=False, indent=1) + "\n")
        print("écrit :", os.path.basename(dst), {f: r["max_appels"] for f, r in sorted(c["relais"].items())})
    return 0


if __name__ == "__main__":
    sys.exit(principal())
