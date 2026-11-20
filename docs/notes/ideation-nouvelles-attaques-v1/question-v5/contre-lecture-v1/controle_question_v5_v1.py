#!/usr/bin/env python3
"""Contrôle du différentiel v4 → v5 de la question « nouvelles attaques » — v1.

Contre-lecteur neuf, modèle O. Bibliothèque standard, plus le module voisin `releve_motifs_question_v4_v1.py` (même dossier,
empreinte à son compagnon), dont il reprend le découpage en sections et le relevé des motifs. N'écrit que sur la sortie
standard. Usage :

    python3 -B controle_question_v5_v1.py QUESTION_V4 QUESTION_V5 NOTE_PERIMETRE_V3 REMPLACEMENTS_JSON

Ce qu'il fait :
  1. les deux couples : pour les remplacements 4 et 5 du JSON, compte dans la note la chaîne exacte
     « Avant : « ANCIEN » Après : « NEUF » » (1 attendu), l'ancien dans la v4 et le neuf dans la v5 (1 attendu chacun) ;
  2. le § 4 de la v5 est-il le § 4 de la v4 avec ces deux seuls remplacements ?
  3. comparaison v4 / v5 section par section, à l'octet ;
  4. relevé des motifs sur la v5 (motifs du mandat du 20 novembre et motifs complémentaires).
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import releve_motifs_question_v4_v1 as rel


def lire(p: str) -> str:
    return Path(p).read_bytes().decode("utf-8", errors="strict")


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        print("usage : controle_question_v5_v1.py QUESTION_V4 QUESTION_V5 NOTE_PERIMETRE_V3 REMPLACEMENTS_JSON", file=sys.stderr)
        return 2
    v4, v5, note = lire(argv[1]), lire(argv[2]), lire(argv[3])
    remp = json.loads(lire(argv[4]))
    for nom, t in (("question v4", v4), ("question v5", v5), ("note v3", note)):
        print(f"{nom} : {hashlib.sha256(t.encode('utf-8')).hexdigest()}")
    print()
    print("=== 1. les deux couples, mot pour mot ===")
    couples = remp[3:5]
    for k, r in enumerate(couples, 1):
        a, n = r["ancien"], r["neuf"]
        chaine = f"Avant : « {a} » Après : « {n} »"
        print(f"  couple {k} : chaîne « Avant … Après … » dans la note : {note.count(chaine)} ; "
              f"ancien dans la v4 : {v4.count(a)} ; neuf dans la v5 : {v5.count(n)} ; neuf dans la v4 : {v4.count(n)}")
    print()
    print("=== 2. § 4 de la v5 = § 4 de la v4 avec les deux couples ===")
    s4_v4, s4_v5 = rel.section_octets(v4, "4."), rel.section_octets(v5, "4.")
    attendu = s4_v4
    for r in couples:
        assert attendu.count(r["ancien"]) == 1
        attendu = attendu.replace(r["ancien"], r["neuf"])
    print(f"  égal : {attendu == s4_v5} ; octets du § 4 : v4 {len(s4_v4.encode('utf-8'))}, v5 {len(s4_v5.encode('utf-8'))}, "
          f"écart {len(s4_v5.encode('utf-8')) - len(s4_v4.encode('utf-8'))}")
    print()
    print("=== 3. comparaison v4 / v5, section par section ===")
    s_v4 = {t: "\n".join(l) for t, _, l in rel.decouper(v4)}
    for titre, _, lignes in rel.decouper(v5):
        a = s_v4.get(titre)
        b = "\n".join(lignes)
        if a is None:
            print(f"  « {titre} » : absente de la v4 sous ce titre")
        else:
            print(f"  « {titre} » : {'égale à l octet' if a.encode('utf-8') == b.encode('utf-8') else 'différente'}")
    print()
    print("=== 4. relevé des motifs sur la v5 ===")
    rel.rendre("question v5", v5)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
