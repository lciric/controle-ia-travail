"""Contre-lecture 2 : vérifie, hors pytest et sans module du dépôt, la logique de l'essai proposé en M12."""
import json
from pathlib import Path
D = Path("/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1")
g1 = json.loads((D / "grille-essaim-hors-echantillon-v1-brouillon1.json").read_text(encoding="utf-8"))
g2 = json.loads((D / "grille-essaim-hors-echantillon-v1-brouillon2.json").read_text(encoding="utf-8"))
assert {k: v for k, v in g1.items() if k not in ("predictions", "version")} == \
    {k: v for k, v in g2.items() if k not in ("predictions", "version", "descriptif_maxima")}
cle = lambda p: (p["cellule"], p["alarme"], p["pred"] == "HP.4")
p1, p2 = {cle(p): p for p in g1["predictions"]}, {cle(p): p for p in g2["predictions"]}
assert p1.keys() == p2.keys() and len(p2) == len(g2["predictions"]) == 84
for k, a in p1.items():
    b = p2[k]
    if a["pred"] == "HP.4":
        assert b["pred"] == "HP.4" and b["sens"] == "entre_x" and b["valeur_bas"] == a["valeur"]
    else:
        assert b["sens"] == a["sens"]
        assert b["pred"] == a["pred"] or (a["pred"] == "HP.5" and b["pred"] in ("HP.5a", "HP.5b"))
print("essai M12 : conforme (mêmes cellules, mêmes sens ; seules les étiquettes HP.5 → HP.5a/HP.5b et HP.4 changent)")
