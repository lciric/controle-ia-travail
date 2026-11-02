"""Comptes seulement : nombre de U+FFFD par épisode des 7 de la résolution (vraies pièces de P3, liens symboliques dans
un dossier temporaire). Aucun texte, aucun score, aucune étiquette n'est affiché."""
import json, shutil, sys, tempfile
from pathlib import Path
ARBRE, PRINCIPAL = Path(sys.argv[1]), Path(sys.argv[2])
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.scellement import sceller
R = Path(tempfile.mkdtemp(prefix="fffd7-"))
for d in ("donnees/20261019-230011-p3-reel", "donnees/t05-pilote-v1", "diag/20261019-230011-p3-reel",
          "runs/20261019-230011-p3-reel"):
    (R / d).parent.mkdir(parents=True, exist_ok=True)
    (R / d).symlink_to(PRINCIPAL / d)
(R / "prereg").mkdir(exist_ok=True)
for n in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
    (R / "prereg" / n).symlink_to(PRINCIPAL / "prereg" / n)
shutil.copy(ARBRE / "prereg/R1-table-tokenisation-v2.json", R / "prereg/R1-table-tokenisation-v2.json")
sceller(R / "prereg/R1-table-tokenisation-v2.json")
config = json.loads((ARBRE / "prereg/R1-graine-config-v1.json").read_text(encoding="utf-8"))
p = rg.charger_pieces(config, R)
T = int(config["T"])
tot = 0
for e in config["episodes_resolution"]:
    n = sum(x["texte"].count(rg.FFFD) for x in rg.EpisodeP3(p, e, T).lignes)
    tot += n
    print(f"{e} : U+FFFD {n}")
print("total des 7 :", tot)
shutil.rmtree(R)
