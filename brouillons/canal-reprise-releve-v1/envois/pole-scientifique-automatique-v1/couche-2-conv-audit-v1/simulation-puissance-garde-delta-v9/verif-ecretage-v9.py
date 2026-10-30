"""v9 (GD8-05) — vérification de l'écrêtage des écarts étalonnés par strate, au critère scindé déclaré d'avance dans `verif-ecretage-v9-critere.md`
(scellé avant l'exécution ; son empreinte est vérifiée ici et recopiée dans la sortie). Utilise les fonctions du script v9 (identiques à la v8 hors
options nouvelles : `verif-identite-v8-v9`). La sortie est écrite et conservée même en cas d'échec. Manifeste écrit par ce script (GD8-09).
Usage (depuis le dossier v9) : python3 -I -B verif-ecretage-v9.py COMMIT SORTIE.json
"""
import hashlib
import importlib.util
import json
import os
import platform
import sys
import time
from datetime import datetime, timezone

import numpy as np

COMMIT, SORTIE = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(__file__))
CRIT = os.path.join(ICI, "verif-ecretage-v9-critere.md")
attendu = open(CRIT + ".sha256").read().split()[0]
reel = hashlib.sha256(open(CRIT, "rb").read()).hexdigest()
if attendu != reel:
    raise SystemExit("refus : le critère a changé depuis son scellement")
V9 = os.path.join(ICI, "simulation-puissance-garde-delta-v9.py")
spec = importlib.util.spec_from_file_location("sim9", V9)
s9 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s9)
REPS, N, K, DELTA = 2000, 288, 8, 0.05
debut, t0 = datetime.now(timezone.utc), time.time()


def puissances(g, v):
    def part(gg, seuil):
        tr = np.stack([s9.prolonger(s9.log_richesse(s9.ecreter(DELTA - gg[:, j, :])), N) for j in range(K)])
        return float((s9.premiere_atteinte(tr.min(axis=0), seuil) > 0).mean())
    def part_c(vv, seuil):
        tr = np.stack([s9.prolonger(s9.log_richesse(s9.ecreter(vv[:, j, :])), N) for j in range(K)])
        return float((s9.premiere_atteinte(tr.min(axis=0), seuil) > 0).mean())
    gj, vj = np.clip(g, -1.0, 1.0), np.clip(v, -1.0, 1.0)
    return {"gardes_40_S": part(g, 40.0), "gardes_40_J": part(gj, 40.0), "gardes_160_S": part(g, 160.0), "gardes_160_J": part(gj, 160.0),
            "contrastes_40_S": part_c(v, 40.0), "contrastes_40_J": part_c(vj, 40.0)}


cas = []
for perim, K_hs, Ss, portees, biais_l in ((True, (5, 10), (2, 3), ("sujet", "commune"), (0.0, 0.0125)), (False, (2, 3), (3,), ("sujet",), (0.0,))):
    for K_h in K_hs:
        for S in Ss:
            for portee in portees:
                for b in biais_l:
                    et = f"ecretage-v9|Kh={K_h}|S={S}|portee={portee}|biais={b}"
                    rng, red = s9.rng_de(20261029, et)
                    loi = s9.LoiSynthetique(K_h, 10, 0.01, 0.4, 0.10, True, 0.0, True, 0.17, 0.0, 0.0, "beta", rho_b=0.17,
                                            strates=(S, 0.4, portee, True, "bloc"))
                    g, v = loi.tirer(rng, REPS, N, N, K, b)
                    p = puissances(g, v)
                    c = {"perimetre": perim, "K_h": K_h, "S": S, "portee": portee, "biais": b, "graine_derivee": red,
                         "part_garde_hors_intervalle": float((np.abs(g) > 1).mean()), "part_contraste_hors_intervalle": float((np.abs(v) > 1).mean()),
                         **p, "diff_gardes_40": p["gardes_40_S"] - p["gardes_40_J"], "diff_gardes_160": p["gardes_160_S"] - p["gardes_160_J"],
                         "diff_contrastes_40": p["contrastes_40_S"] - p["contrastes_40_J"]}
                    if perim:
                        c["C1"] = bool(c["part_garde_hors_intervalle"] < 1e-3 and abs(c["diff_gardes_40"]) <= 0.003 and abs(c["diff_gardes_160"]) <= 0.003
                                       and c["diff_contrastes_40"] == 0.0)
                    cas.append(c)
                    print({k: (round(x, 5) if isinstance(x, float) else x) for k, x in c.items() if k != "graine_derivee"}, flush=True)
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "v9_sha256": hashlib.sha256(open(V9, "rb").read()).hexdigest(),
       "critere": os.path.basename(CRIT), "critere_sha256": reel, "cas": cas,
       "C1_cas": sum(1 for c in cas if c["perimetre"]), "C1_conformes": sum(1 for c in cas if c.get("C1")),
       "conforme": all(c["C1"] for c in cas if c["perimetre"]), "duree_s": round(time.time() - t0, 1)}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
fin = datetime.now(timezone.utc)
man = {"passage": os.path.basename(SORTIE)[:-5], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc_debut": debut.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin.strftime("%Y-%m-%dT%H:%M:%SZ"), "commande": sys.argv,
       "script_sha256": res["script_sha256"], "graines": {"graine_maitresse": 20261029, "derivation": "rng_de du script v9 : SeedSequence([graine, sha256(étiquette)])",
                                                         "par_cas": {f"Kh={c['K_h']}|S={c['S']}|{c['portee']}|{c['biais']}": c["graine_derivee"] for c in cas}},
       "configuration": {"repetitions": REPS, "n": N, "k": K, "delta": DELTA, "rho": 0.17, "gamma": 0.4},
       "environnement": {"python": platform.python_version(), "numpy": np.__version__},
       "fichiers": {os.path.basename(SORTIE): hashlib.sha256(open(SORTIE, "rb").read()).hexdigest(), os.path.basename(CRIT): reel}}
with open(os.path.join(os.path.dirname(os.path.abspath(SORTIE)), "manifeste-" + os.path.basename(SORTIE)), "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("conforme :", res["conforme"], f"({res['C1_conformes']}/{res['C1_cas']})")
