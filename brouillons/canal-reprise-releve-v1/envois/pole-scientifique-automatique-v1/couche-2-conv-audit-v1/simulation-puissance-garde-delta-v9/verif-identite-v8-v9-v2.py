"""v9, version 2 du vérificateur (script v9 final, avec la portée partielle de GD8-03) — identité v8 = v9 hors des options nouvelles (GD8-03, GD8-07, GD8-08), et témoin négatif.
Ajout par rapport à `verif-identite-v8-v9.py` : configuration « strates-commune » (portée commune étalonnée) ; dossier d'essais `essais-v9-v2/`.

Lance le script v8 scellé (dossier v8, lecture seule) et le script v9 avec les mêmes options sur quatre configurations courtes (dispersion
combinée avec n80 de la fiche, neuvième comparateur, strates étalonnées, copule), 200 répétitions ; compare champ à champ les blocs
`cellules` et `lois` des sorties (tout champ, à l'égalité exacte des flottants). Témoin négatif : v9 avec `--facteur-rho-honnetes 2` sur la
première configuration doit différer (sinon la vérification ne voit rien : échec déclaré). Critère écrit avant exécution : 0 différence sur
les quatre configurations ET au moins une différence sur le témoin. Sorties conservées dans `essais-v9/` même en cas d'échec.
Graines : graine maîtresse des scripts (20261029), dérivation par étiquette (R9). Manifeste écrit par ce script (GD8-09).
Usage (depuis le dossier v9) : python3 -I -B verif-identite-v8-v9-v2.py COMMIT SORTIE.json
"""
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np

COMMIT, SORTIE = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(ICI, "..", "simulation-puissance-garde-delta-v8", "simulation-puissance-garde-delta-v8.py")
V9 = os.path.join(ICI, "simulation-puissance-garde-delta-v9.py")
DOS = os.path.join(ICI, "essais-v9-v2")
os.makedirs(DOS, exist_ok=True)
CRITERE = "0 différence (cellules et lois) sur les 5 configurations ; au moins 1 différence sur le témoin négatif"
COMMUN = ["--repetitions", "200", "--taux", "0.01", "--deltas", "0.05", "--biais", "0,0.0125", "--lecture-ebh", "A", "--m", "8,2", "--sans-n80",
          "--commit-declare", COMMIT]
COMB = ["--echelle-dispersion", "beta", "--combiner-dispersion-a-et-comparateurs"]
CONFIGS = {
    "combine-n80": ["--comparateurs", "8", "--K", "5", "--K-s", "10", "--tailles", "96", "--n80-fiche", "--cibles-n80", "0.8,0.9"] + COMB
                   + ["--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17"],
    "neuvieme": ["--comparateurs", "9", "--K", "5", "--K-s", "10", "--tailles", "96", "--ecart-contraste-neuvieme", "0.05"] + COMB
                + ["--effet-unite-beta", "0.10", "--rho-comparateurs", "0.10"],
    "strates": ["--comparateurs", "8", "--K", "5", "--K-s", "10", "--tailles", "96"] + COMB
               + ["--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17", "--strates", "3", "--amplitude-strates", "0.4", "--portee-strates", "sujet",
                  "--calibrage-par-strate"],
    "strates-commune": ["--comparateurs", "8", "--K", "5", "--K-s", "10", "--tailles", "96"] + COMB
               + ["--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17", "--strates", "2", "--amplitude-strates", "0.4", "--portee-strates", "commune",
                  "--calibrage-par-strate"],
    "copule": ["--comparateurs", "8", "--K", "5", "--K-s", "10", "--tailles", "96"] + COMB
              + ["--effet-unite-beta", "0.17", "--rho-comparateurs", "0.17", "--correlation-sujet-comparateurs", "0.5"],
}


def lancer(script, nom, options):
    s = os.path.join(DOS, f"identite-{nom}.json")
    r = subprocess.run([sys.executable, "-I", "-B", script] + COMMUN + options + ["--sortie", s], capture_output=True, text=True)
    return r.returncode, r.stderr[-500:], s


def aplatir(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from aplatir(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from aplatir(v, f"{p}[{i}]")
    else:
        yield p, x


def comparer(f1, f2):
    a, b = json.load(open(f1, encoding="utf-8")), json.load(open(f2, encoding="utf-8"))
    da = dict(aplatir({"cellules": a["cellules"], "lois": a["lois"]}))
    db = dict(aplatir({"cellules": b["cellules"], "lois": b["lois"]}))
    communs = set(da) & set(db)
    diff = [k for k in communs if da[k] != db[k]]
    return {"champs_v8": len(da), "champs_v9": len(db), "champs_communs": len(communs), "differences": len(diff),
            "seulement_v8": len(set(da) - set(db)), "seulement_v9": len(set(db) - set(da)), "exemples": sorted(diff)[:5]}


debut = datetime.now(timezone.utc)
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "critere_ecrit_avant_execution": CRITERE,
       "v8_sha256": hashlib.sha256(open(V8, "rb").read()).hexdigest(), "v9_sha256": hashlib.sha256(open(V9, "rb").read()).hexdigest(),
       "configurations": {}}
ok = True
for nom, opt in CONFIGS.items():
    c8, e8, s8 = lancer(V8, f"{nom}-v8", opt)
    c9, e9, s9 = lancer(V9, f"{nom}-v9", opt)
    r = {"codes": [c8, c9], "erreurs": [e8, e9]}
    if c8 == 0 and c9 == 0:
        r |= comparer(s8, s9)
        ok &= r["differences"] == 0 and r["seulement_v8"] == 0 and r["seulement_v9"] == 0
    else:
        ok = False
    res["configurations"][nom] = r
    print(nom, {k: v for k, v in r.items() if k != "erreurs"}, flush=True)
ct, et, st = lancer(V9, "temoin-facteur2-v9", CONFIGS["combine-n80"] + ["--facteur-rho-honnetes", "2"])
t = {"code": ct, "erreur": et}
if ct == 0:
    t |= comparer(os.path.join(DOS, "identite-combine-n80-v8.json"), st)
    # le témoin change le nom des lois : on compare les cellules à étiquette équivalente (nom sans le suffixe du facteur)
    a = json.load(open(os.path.join(DOS, "identite-combine-n80-v8.json"), encoding="utf-8"))
    b = json.load(open(st, encoding="utf-8"))
    cb = {k.replace("_rhoHonnetes2.0x", ""): v for k, v in b["cellules"].items()}
    nd = sum(1 for k in a["cellules"] if k in cb and dict(aplatir(a["cellules"][k])) != dict(aplatir(cb[k])))
    t["cellules_appariees_differentes"] = nd
    temoin_vu = nd >= 1
else:
    temoin_vu = False
res["temoin_negatif"] = t | {"vu": temoin_vu}
res["conforme"] = bool(ok and temoin_vu)
fin = datetime.now(timezone.utc)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
man = {"passage": os.path.basename(SORTIE)[:-5], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc_debut": debut.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin.strftime("%Y-%m-%dT%H:%M:%SZ"),
       "commande": sys.argv, "script_sha256": res["script_sha256"],
       "graines": "graine maîtresse 20261029 des scripts v8 et v9, dérivation SeedSequence([graine, sha256(étiquette)]) (R9)",
       "environnement": {"python": platform.python_version(), "numpy": np.__version__},
       "fichiers": {os.path.basename(SORTIE): hashlib.sha256(open(SORTIE, "rb").read()).hexdigest()}
       | {os.path.basename(p): hashlib.sha256(open(os.path.join(DOS, p), "rb").read()).hexdigest() for p in sorted(os.listdir(DOS)) if p.startswith(("identite-", "manifeste-identite-"))}}
with open(os.path.join(os.path.dirname(os.path.abspath(SORTIE)), "manifeste-" + os.path.basename(SORTIE)), "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("conforme :", res["conforme"], "| témoin vu :", temoin_vu)
