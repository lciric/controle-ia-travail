"""Jonctions de la v6 : 160 caractères avant et après chaque texte neuf (blancs ramenés à une espace). Lecture seule.
Les entrées sont prises de la copie du script du correcteur (rejeu/), qui recontrôle les empreintes.
Usage : python3 -I -B jonctions_v6.py V6.md
"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "rejeu"))
import appliquer_corrections_v6 as ap
t = re.sub(r"\s+", " ", Path(sys.argv[1]).read_text(encoding="utf-8"))
for etiq, a, b in ap.entrees(ap.corrections(), ap.comptes()):
    nb = re.sub(r"\s+", " ", b).strip()
    i = t.find(nb)
    if i < 0 or t.count(nb) != 1:
        print(f"FAUTE {etiq}: trouvé {t.count(nb)} fois"); continue
    print(f"== {etiq}\n  AVANT : …{t[max(0,i-160):i]}\n  APRÈS : {t[i+len(nb):i+len(nb)+160]}…")
