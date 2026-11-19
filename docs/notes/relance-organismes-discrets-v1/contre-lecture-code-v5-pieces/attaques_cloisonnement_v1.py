"""Essais d'attaque de la garde statique du cloisonnement (C-6), sur modules plantés dans un dossier temporaire."""
import tempfile
from pathlib import Path
from controle_ia.organismes_discrets import cloisonnement_bras_a_v5 as cl

PLANTES = {
    "a_join.py": 'import json\nnom = "-".join(["rangs", "par", "unite"]) + "-moniteurs-bras-a.jsonl"\nlignes = open("runs/x/" + nom).read()\n',
    "b_glob.py": 'from pathlib import Path\nfor f in Path("runs/bras-a").glob("*.jsonl"):\n    print(f.read_text())\n',
    "c_format.py": 'nom = "%s-par-%s" % ("rangs", "unite")\nopen(nom + "-moniteurs-bras-a.jsonl")\n',
    "d_inverse.py": 'nom = "lnosj.a-sarb-sruetinom-etinu-rap-sgnar"[::-1]\nopen(nom)\n',
    "e_format_methode.py": 'nom = "{}-{}-{}".format("rangs", "par", "unite")\nopen(nom)\n',
    "f_depuis_la_piece.py": 'import json\ns = json.load(open("sortie.json"))\nk = [c for c in s if c.startswith("scores")][0]\nopen(s[k]["fichier"])\n',
    "scripts/analyse_bras_a_v3.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "scripts/t07_lecture_rapide.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "scripts/outils/mots_et_cout_resume.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "g_importlib_format.py": 'import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v%d" % 5)\nf = getattr(an, "_".join(["lire", "fichier", "des", "rangs"]))\n',
    "h_makefile.mk": 'lire:\n\tcat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n',
    "i_commande.zsh": 'cat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n',
    "j_cahier.ipynb": '{"cells": [{"source": ["open(\\"rangs-par-unite-moniteurs-bras-a.jsonl\\")"]}]}\n',
    "k_jeton.py": 'from controle_ia.organismes_discrets import graines_bras_a_v5 as g\nimport numpy as np\nt = g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 1, np.random.default_rng(), False)\n',
    "temoin_sain.py": 'x = 1\n',
    "temoin_artefact.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl")\n',
}
d = Path(tempfile.mkdtemp())
for nom, texte in PLANTES.items():
    p = d / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
v = cl.violations_du_cloisonnement([d])
for nom in PLANTES:
    vu = [x for x in v if x.startswith((d / nom).as_posix())]
    print(("VU    " if vu else "PASSE ") + nom + ("" if not vu else "  (" + str(len(vu)) + ")"))
