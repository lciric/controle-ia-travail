#!/usr/bin/env python3
"""Assemble l'erratum 1 de la v3 consolidée (outil de bloc-notes du concepteur ; classe C, sans valeur de pièce).
Les textes sont dans erratum_textes.py et erratum_couples.py ; chaque ancien est contrôlé (une seule fois dans la v3).
Usage : python batir_erratum.py CHEMIN_SORTIE [--essai]
La pièce qui fait foi est l'erratum scellé ; son contrôle est verification-couples-erratum-1-v3-consolidee-v1.py.
"""
import hashlib
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[6]   # racine du dépôt
DOSSIER = RACINE / "docs/notes/chantiers-21-novembre-v1/conceptions-v2"
V3 = DOSSIER / "conception-2-epreuves-du-devin-v3-consolidee.md"
CALC = DOSSIER / "calculs-devin-option-d-v1"
v3 = V3.read_text(encoding="utf-8")


ESSAI = "--essai" in sys.argv


def sha(p: Path) -> str:
    if not p.exists():
        assert ESSAI, f"{p} absent"
        return "EMPREINTE-EN-ATTENTE"
    return hashlib.sha256(p.read_bytes()).hexdigest()


exec((Path(__file__).parent / "erratum_textes.py").read_text(encoding="utf-8"))  # noqa: S102 — textes du concepteur

couples = COUPLES  # noqa: F821
for c in couples:
    assert v3.count(c["ancien"]) == 1, (c["id"], v3.count(c["ancien"]))
ids = [c["id"] for c in couples]
assert len(set(ids)) == len(ids)

entete = ENTETE.format(  # noqa: F821
    e_script=sha(CALC / "calculs-devin-option-d-v1.py"),
    e_sortie=sha(CALC / "calculs-devin-option-d-v1-sortie.txt"),
    e_json=sha(CALC / "calculs-devin-option-d-v1-sortie.json"),
    e_verif=sha(CALC / "verification-couples-erratum-1-v3-consolidee-v1.py"),
    n=len(couples), ordre=" ; ".join(ids),
)
blocs = []
for c in couples:
    cloture = "```"
    while cloture in c["ancien"] or cloture in c["nouveau"]:
        cloture += "`"
    blocs.append(f"## {c['id']} — {c['lieu']}\n\nAncien :\n{cloture}text\n{c['ancien']}\n{cloture}\n\nNouveau :\n{cloture}text\n{c['nouveau']}\n{cloture}\n"
                 + (f"\n{c['note']}\n" if c.get("note") else ""))
avant = CORPS_AVANT  # noqa: F821
for cle, val in CHIFFRES_TARDIFS.items():  # noqa: F821
    assert avant.count("{" + cle + "}") == 1, cle
    avant = avant.replace("{" + cle + "}", val)
texte = entete + avant + "\n".join(blocs) + CORPS_APRES  # noqa: F821
if not ESSAI:
    assert "À REMPLIR" not in texte and "EMPREINTE-EN-ATTENTE" not in texte
sortie = Path(sys.argv[1])
sortie.write_text(texte, encoding="utf-8")
print(f"{sortie} : {len(couples)} couples, {len(texte)} signes, {len(texte.split())} mots")
