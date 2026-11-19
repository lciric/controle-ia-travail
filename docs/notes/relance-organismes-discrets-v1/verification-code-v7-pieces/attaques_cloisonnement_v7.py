"""Essais d'attaque v6 de la garde statique : les seize modules de la v5, et quelques neufs, dans un faux dépôt."""
import tempfile
from pathlib import Path
from controle_ia.organismes_discrets import cloisonnement_bras_a_v7 as cl

P = "src/controle_ia/organismes_discrets/"
PLANTES = {
    "src/a_join.py": 'nom = "-".join(["rangs", "par", "unite"]) + "-moniteurs-bras-a.jsonl"\nopen(nom)\n',
    "src/b_glob.py": 'from pathlib import Path\nfor f in Path("runs/bras-a").glob("*.jsonl"):\n    print(f.read_text())\n',
    "src/b2_iterdir_sans_extension.py": 'from pathlib import Path\nfor f in Path("runs/bras-a").iterdir():\n    print(f.read_text())\n',
    "src/c_format.py": 'nom = "%s-par-%s" % ("rangs", "unite")\nopen(nom)\n',
    "src/d_inverse.py": 'nom = "lnosj.a-sarb-sruetinom-etinu-rap-sgnar"[::-1]\nopen(nom)\n',
    "src/e_format_methode.py": 'nom = "{}-{}-{}".format("rangs", "par", "unite")\nopen(nom)\n',
    "src/f_depuis_la_piece.py": 'import json\ns = json.load(open("sortie.json"))\nk = [c for c in s if c.startswith("scores")][0]\nopen(s[k]["fichier"])\n',
    "scripts/analyse_bras_a_v3.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "scripts/t07_lecture_rapide.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "scripts/outils/mots_et_cout_resume.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl").read()\n',
    "src/g_importlib_format.py": 'import importlib\nan = importlib.import_module("controle_ia.organismes_discrets.analyse_bras_a_v%d" % 7)\nf = getattr(an, "_".join(["lire", "fichier", "des", "rangs"]))\n',
    "scripts/h_makefile.mk": 'lire:\n\tcat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n',
    "scripts/i_commande.zsh": 'cat runs/rangs-par-unite-moniteurs-bras-a.jsonl\n',
    "scripts/j_cahier.ipynb": '{"cells": [{"source": ["open(\\"rangs-par-unite-moniteurs-bras-a.jsonl\\")"]}]}\n',
    "src/k_jeton.py": 'from controle_ia.organismes_discrets import graines_bras_a_v7 as g\nimport numpy as np\nt = g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 1, np.random.default_rng(), False)\n',
    "src/temoin_sain.py": 'x = 1\n',
    "src/temoin_artefact.py": 'open("rangs-par-unite-moniteurs-bras-a.jsonl")\n',
    # neufs
    "src/n1_join_generateur.py": 'nom = "-".join(x for x in ["rangs", "par", "unite"])\nopen(nom)\n',
    "src/n2_fstring_variables.py": 'a, b = "rangs", "unite"\nopen(f"{a}-par-{b}-moniteurs-bras-a.jsonl")\n',
    "src/n3_jeton_par_getattr.py": 'import importlib\ng = importlib.import_module("controle_ia.organismes_discrets.graines_" + "bras_a_v6")\nj = getattr(g, "_JE" "TON")\n',
    "src/n4_jeton_sans_import_ecrit.py": 'import sys\ng = sys.modules["controle_ia.organismes_discrets." + "graines" + "_bras_a_v6"]\nt = vars(g)["_JE" + "TON"]\n',
    "src/n5_rangs_scelles_par_vars.py": 'import sys\nm = sys.modules["controle_ia.organismes_discrets.analyse" + "_bras_a_v6"]\nR = vars(m)["Rangs" + "Scelles"]\n',
    "src/n6_generateur_remplace.py": 'from controle_ia.organismes_discrets import graines_bras_a_v7 as g\nobject.__setattr__(t, "_generateur", None)\n',
    "src/n7_concat_variable_reaffectee.py": 'a = "x"\na = "rangs"\nopen(a + "-par-unite.jsonl")\n',
}
racine = Path(tempfile.mkdtemp())
for nom, texte in PLANTES.items():
    p = racine / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
v = cl.violations_de_la_garde_statique(racine)          # défauts de production : dossiers src et scripts, exclusion par défaut
s = cl.listages_a_relire(racine)
for nom in PLANTES:
    vu = [x for x in v if x.startswith(nom)]
    sig = [x for x in s if x.startswith(nom)]
    print(("REFUSE  " if vu else "SIGNALE " if sig else "PASSE   ") + nom)
