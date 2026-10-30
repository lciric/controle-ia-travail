"""v9 — manifeste d'ensemble `manifeste-puissance-garde-delta-v9.json` (R9, R6, GD8-09), assemblé depuis le dossier v9 et les manifestes par passage.

Contenu : commit de l'arbre lu par l'appelant (`git rev-parse HEAD`, lecture seule, hors de ce script) ; versions (Python, numpy, scipy) ; pour chaque passage
(sortie `simulation-puissance-garde-delta-v9-sortie-*.json`) : script exécuté et son empreinte, commande, graine maîtresse, empreinte des réglages, durée, empreintes de
la sortie, du journal et du manifeste ; manifestes des scripts auxiliaires ; entrées lues dans le dossier v8 (empreintes) ; inventaire de tous les fichiers du dossier v9
(sous-dossiers compris) avec empreinte, et contrôle des compagnons `.sha256`. Aucun tirage.
Usage (depuis le dossier v9) : python3 -I -B assembler-manifeste-v9.py COMMIT SORTIE.json
"""
import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone

import numpy as np

COMMIT, SORTIE = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(ICI, "..", "simulation-puissance-garde-delta-v8")
h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
try:
    import scipy
    v_scipy = scipy.__version__
except Exception:  # pragma: no cover
    v_scipy = None
man = {"version": "manifeste-puissance-garde-delta-v9", "date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "commit_lu_par_l_appelant": COMMIT, "ecrit_par": os.path.basename(__file__), "script_sha256": h(__file__),
       "environnement": {"python": platform.python_version(), "numpy": np.__version__, "scipy": v_scipy},
       "graines": "R9 : SeedSequence([graine maîtresse, entier des 8 premiers octets de sha256(étiquette)]) ; graine maîtresse 20261029 (passages de grille, ρ honnête, "
                  "strates, vérifications), 11 à 18 (passages `graine…`, GD8-04) ; graines dérivées par cellule dans chaque manifeste de passage",
       "passages": {}, "manifestes_auxiliaires": {}, "entrees_v8": {}, "fichiers": {}, "compagnons": {}}
for f in sorted(os.listdir(ICI)):
    if f.startswith("simulation-puissance-garde-delta-v9-sortie-") and f.endswith(".json"):
        base = f[:-5]
        mf = os.path.join(ICI, "manifeste-" + base + ".json")
        jr = os.path.join(ICI, base + "-journal.txt")
        m = json.load(open(mf, encoding="utf-8")) if os.path.exists(mf) else None
        man["passages"][base] = {"sortie_sha256": h(os.path.join(ICI, f)), "journal_sha256": h(jr) if os.path.exists(jr) else None,
                                 "manifeste_sha256": h(mf) if m else None,
                                 "script": None if m is None else {"chemin": os.path.relpath(m["script"]["chemin"], ICI), "sha256": m["script"]["sha256"]},
                                 "commande": None if m is None else m["commande"]["ligne"], "graine_maitresse": None if m is None else m["graines"]["graine_maitresse"],
                                 "reglages_sha256": None if m is None else m["reglages_sha256"], "duree_s": None if m is None else m["duree_s"],
                                 "environnement": None if m is None else m["environnement"], "commit_declare": None if m is None else m["script"].get("commit")}
    elif f.startswith("manifeste-") and f.endswith("-sortie.json"):
        man["manifestes_auxiliaires"][f] = h(os.path.join(ICI, f))
for f in sorted(os.listdir(V8)):
    if (f.startswith("simulation-puissance-garde-delta-v8-sortie-") and f.endswith(".json")) or f in (
            "simulation-puissance-garde-delta-v8.py", "precision-rho-pilote-v8-sortie.json", "tableaux-v8-sortie.json", "rapport-puissance-garde-delta-v8.md"):
        man["entrees_v8"][f] = h(os.path.join(V8, f))
for racine, dossiers, fichiers in os.walk(ICI):
    dossiers.sort()
    for f in sorted(fichiers):
        p = os.path.join(racine, f)
        rel = os.path.relpath(p, ICI)
        if rel == SORTIE or rel == SORTIE + ".sha256":
            continue
        if f.endswith(".sha256"):
            continue
        man["fichiers"][rel] = h(p)
        c = p + ".sha256"
        man["compagnons"][rel] = (open(c).read().split()[0] == man["fichiers"][rel]) if os.path.exists(c) else None
man["bilan_compagnons"] = {"conformes": sum(1 for v in man["compagnons"].values() if v), "ecarts": [k for k, v in man["compagnons"].items() if v is False],
                           "sans_compagnon": [k for k, v in man["compagnons"].items() if v is None]}
with open(SORTIE, "x", encoding="utf-8") as fh:
    json.dump(man, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
print(len(man["passages"]), "passages ;", len(man["fichiers"]), "fichiers ;", man["bilan_compagnons"]["conformes"], "compagnons conformes ;",
      "écarts :", man["bilan_compagnons"]["ecarts"], "; sans compagnon :", man["bilan_compagnons"]["sans_compagnon"][:10])
