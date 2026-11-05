"""Addendum factice de répétition (mode jouet seulement), v8. Bibliothèque standard seule : la répétition le charge par
son chemin (`git show <commit>:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py`), hors du paquet.

Le texte écrit est conforme à `controle_ia.prereg.problemes` (les huit sections exigées, aucun marqueur, une section
« Contre-lecture » qui porte deux empreintes), pour que la répétition atteigne le calcul. Il est **marqué factice** en
tête (`MARQUE`) et ses deux empreintes de contre-lecture sont celles de deux chaînes connues, jamais celles d'une pièce
réelle. `manifeste_phase` refuse un addendum qui porte la marque hors du mode jouet.

    python3 -I -B addendum_factice.py CHEMIN_ADDENDUM COMMIT_CODE
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

MARQUE = "ADDENDUM FACTICE DE RÉPÉTITION (mode jouet ; aucune valeur ; jamais scellé au dépôt de travail)"
EMPREINTE_BROUILLON = hashlib.sha256(b"brouillon factice de repetition SPARKS-EXP7-NUL").hexdigest()
EMPREINTE_RAPPORT = hashlib.sha256(b"rapport factice de repetition SPARKS-EXP7-NUL").hexdigest()
SECTIONS = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
            "Critères de lecture gelés", "Liste d'arrêt")


def texte(commit_code: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", commit_code):
        raise ValueError("commit du code : 40 chiffres hexadécimaux attendus")
    corps = [f"# {MARQUE}", "", f"Commit du code : {commit_code}.", ""]
    for s in SECTIONS:
        corps += [f"## {s}", "", f"Factice (répétition) : aucune valeur ; le texte qui ferait foi est l'addendum scellé réel.", ""]
    corps += ["## Contre-lecture", "",
              f"Contre-lecture factice (répétition ; aucune contre-lecture réelle) : brouillon relu factice `{EMPREINTE_BROUILLON}` ; "
              f"rapport factice `{EMPREINTE_RAPPORT}`.", ""]
    return "\n".join(corps)


def ecrire(chemin: str | Path, commit_code: str) -> str:
    """Écrit l'addendum factice et son compagnon `.sha256` (format de `sha256sum`) ; refuse d'écraser (R12)."""
    p = Path(chemin)
    c = Path(str(p) + ".sha256")
    if p.exists() or c.exists():
        raise FileExistsError(f"{p} ou son compagnon existe déjà (R12)")
    b = texte(commit_code).encode("utf-8")
    p.write_bytes(b)
    h = hashlib.sha256(b).hexdigest()
    c.write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


if __name__ == "__main__":
    print(ecrire(sys.argv[1], sys.argv[2]))
