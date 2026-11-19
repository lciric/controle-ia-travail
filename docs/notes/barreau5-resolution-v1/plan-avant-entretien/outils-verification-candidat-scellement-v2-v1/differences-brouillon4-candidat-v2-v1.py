#!/usr/bin/env python3
"""Vérification du candidat au scellement v2 (barreau 5) : différences depuis le brouillon 4 vérifié (v1).

Écrit par le vérificateur (Claude Opus 5.5) le 20 novembre 2026. Ne lit que des textes du dépôt ; n'écrit rien. Pour le
texte puis pour le devis : chaque bloc de lignes changé, avec les numéros de ligne du candidat. Une ligne remplacée par
une seule ligne est montrée mot à mot (seuls les passages changés, avec quelques mots de contexte) ; une ligne ajoutée
ou ôtée est montrée en entier. Sert à lire tout ce qui a changé depuis la pièce vérifiée, sans se fier à une table.
"""
from __future__ import annotations

import difflib
import hashlib
from pathlib import Path

PLAN = Path(__file__).resolve().parent.parent
RACINE = PLAN.parents[3]
PAIRES = [
    ("texte", RACINE / "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md", "dbe66dc9",
     RACINE / "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md", "088e15ef"),
    ("devis", PLAN / "devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md", "084cd547",
     PLAN / "devis-adaptateurs-tenus-a-l-ecart-v1-candidat-scellement-v2.md", "94a628a7"),
]
CONTEXTE = 6


def lire(p: Path, attendu: str) -> list[str]:
    brut = p.read_bytes()
    h = hashlib.sha256(brut).hexdigest()
    if not h.startswith(attendu):
        raise SystemExit(f"empreinte inattendue : {p} {h}")
    return brut.decode("utf-8").split("\n")


def mot_a_mot(x: str, y: str) -> list[str]:
    a, b = x.split(" "), y.split(" ")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        avant = " ".join(a[max(0, i1 - CONTEXTE):i1])
        apres = " ".join(a[i2:i2 + CONTEXTE])
        out.append(f"   …{avant} [-{' '.join(a[i1:i2])}-] {{+{' '.join(b[j1:j2])}+}} {apres}…")
    return out


def main():
    for nom, ancien, ea, neuf, en in PAIRES:
        a, b = lire(ancien, ea), lire(neuf, en)
        print(f"\n######## {nom} : {ancien.name} ({ea}…, {len(a)} lignes) -> {neuf.name} ({en}…, {len(b)} lignes)")
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
            if op == "equal":
                continue
            print(f"\n=== {op} : ancien l. {i1 + 1}-{i2}, candidat l. {j1 + 1}-{j2}")
            if op == "replace" and (i2 - i1) == (j2 - j1):
                for k in range(i2 - i1):
                    print(f"  ligne {j1 + k + 1} :")
                    for s in mot_a_mot(a[i1 + k], b[j1 + k]):
                        print(s)
            else:
                for l in a[i1:i2]:
                    print(f"- {l}")
                for l in b[j1:j2]:
                    print(f"+ {l}")


if __name__ == "__main__":
    main()
