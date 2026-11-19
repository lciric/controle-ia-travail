import shutil, sys, tempfile
from pathlib import Path
import numpy as np
from controle_ia import manifeste
from controle_ia.barreau8_moniteurs import lecture_sondes_v5 as L
from controle_ia.barreau8_moniteurs import passe_recalcul_v5 as P
from controle_ia.scellement import sceller
E = 149333987590752343984325077404464904184
src = Path(sys.argv[1])
d = Path(tempfile.mkdtemp(dir=src.parent))
(d / "prereg").mkdir()
t = d / "prereg" / "texte.md"
shutil.copy(src, t)
sha = sceller(t)
print("copie scellée", sha)
print("cellules F-3 trouvées :", L.CELLULE_F3.findall(t.read_text(encoding="utf-8")))
print("sain :", L.exiger_texte_scelle(d, {"chemin": "prereg/texte.md", "sha256": sha}, E) == sha)
for faux in (E + 1, int(str(E)[:-1])):
    try:
        L.exiger_texte_scelle(d, {"chemin": "prereg/texte.md", "sha256": sha}, faux); print("ARTEFACT ACCEPTÉ", faux)
    except L.Refus as e:
        print("artefact refusé :", e.code)
print("chiffres :", len(str(E)), "; < 2**128 :", E < 2**128)
g = manifeste.graines(L.cles_de_graines(("s",)) + ["repetabilite-passe", "injection-adaptateurs"], entropie=E)
print("entropie consignée :", g["puissance"]["entropie"] == str(E))
print("graine entière égale dans les deux codes :", L.graine_entiere(g, "repetabilite-passe") == P._graine_entiere(g["repetabilite-passe"]))
print("analyseur de la passe :", P._analyseur().parse_args(["passe", "--entropie", str(E)]).entropie == E)
print("analyseur de la lecture :", L._analyseur().parse_args(["puissance", "--racine", ".", "--registre", "r", "--entropie", str(E), "--run-id", "x"]).entropie == E)
r = L.recette_de_puissance(E, L.Recette(n_taches=6, n_pas=3, n_plancher=8, n_tirages=40, repetitions=2, aires=(0.8,), fractions=(1.0,)))
print("recette réduite :", r["entropie"] == str(E), [c["etat"] for c in r["cases"]])
shutil.rmtree(d)
