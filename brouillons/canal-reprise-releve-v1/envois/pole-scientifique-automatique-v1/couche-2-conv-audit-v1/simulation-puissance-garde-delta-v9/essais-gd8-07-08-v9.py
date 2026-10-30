"""v9 — essais des deux options nouvelles (règle R5 : chaque garde essayée sur un cas sain et sur un artefact).

GD8-08 (fiches nulles avec neuvième comparateur) :
  sain 1 : neuvième comparateur, sans fiche nulle → code 0 ; sain 2 : fiche nulle sans neuvième → code 0 ;
  artefact 1 : la commande de GD8 (`--ecart-contraste-neuvieme 0.05 --fiches-nulles 1`) → refus nommé (code ≠ 0, « GD8-08 » dans le message) ;
  artefact 2 (garde de second rang, dans la loi) : `variante_nulle()` d'une loi à neuvième comparateur, tirée à k = 9 → Refus ; à k = 8 (neuvième inactif) → tirage.
GD8-07 (ρ honnête = F × ρ saboté) :
  sain : F = 2 en dispersion combinée → code 0 ; décomposition : corrélation intra-unité honnête = 2ρ (A et comparateurs), sabotée = ρ ;
         écart-type tiré des p honnêtes de A et des comparateurs à moins de 10 % de √(2ρ p₀(1 − p₀)) (loi très asymétrique à p₀ = 0,01 : erreur relative ≈ 2,5 %) ; côté saboté à moins de 5 % de √(ρ p₀(1 − p₀)) ;
  artefacts : F sans dispersion combinée ; F avec copule ; F avec neuvième ; F·ρ ≥ 1 ; F = 0 ; F = « nan » → refus nommés, aucun fichier laissé.
Critère écrit avant exécution : tous les cas conformes à l'attendu ci-dessus. Sorties conservées dans `essais-v9/` (R6).
Usage (depuis le dossier v9) : python3 -I -B essais-gd8-07-08-v9.py COMMIT SORTIE.json
"""
import hashlib
import importlib.util
import json
import math
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone

import numpy as np

COMMIT, SORTIE = sys.argv[1:3]
ICI = os.path.dirname(os.path.abspath(__file__))
V9 = os.path.join(ICI, "simulation-puissance-garde-delta-v9.py")
DOS = os.path.join(ICI, "essais-v9")
os.makedirs(DOS, exist_ok=True)
BASE = ["--repetitions", "200", "--taux", "0.01", "--deltas", "0.05", "--biais", "0", "--lecture-ebh", "A", "--m", "8,2", "--sans-n80",
        "--K", "5", "--K-s", "10", "--tailles", "96", "--commit-declare", COMMIT]
COMB = ["--echelle-dispersion", "beta", "--combiner-dispersion-a-et-comparateurs"]


def lancer(nom, options, avec_sortie=True):
    s = os.path.join(DOS, f"essai-{nom}.json")
    cmd = [sys.executable, "-I", "-B", V9] + BASE + options + (["--sortie", s] if avec_sortie else [])
    r = subprocess.run(cmd, capture_output=True, text=True)
    laisses = [p for p in (s, s[:-5] + "-journal.txt", os.path.join(DOS, "manifeste-" + os.path.basename(s))) if os.path.exists(p)]
    return {"code": r.returncode, "message": r.stderr.strip()[-400:], "fichiers_laisses": [os.path.basename(p) for p in laisses], "sortie": s}


cas = []


def attendre(nom, r, ok, attendu):
    cas.append({"cas": nom, "attendu": attendu, "conforme": bool(ok), **{k: v for k, v in r.items() if k != "sortie"}})
    print(("OK   " if ok else "ÉCHEC"), nom, r.get("code"), r.get("message", "")[-160:], flush=True)


debut = datetime.now(timezone.utc)
# ---- GD8-08
r = lancer("gd8-08-sain-neuvieme", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.05"])
attendre("GD8-08 sain 1 : neuvième sans fiche nulle", r, r["code"] == 0, "code 0")
r = lancer("gd8-08-sain-nulle", ["--comparateurs", "9", "--fiches-nulles", "1"])
attendre("GD8-08 sain 2 : fiche nulle sans neuvième particulier", r, r["code"] == 0, "code 0")
r = lancer("gd8-08-artefact-commande-gd8", ["--comparateurs", "9", "--ecart-contraste-neuvieme", "0.05", "--fiches-nulles", "1"])
attendre("GD8-08 artefact 1 : commande de GD8", r, r["code"] != 0 and "GD8-08" in r["message"] and not r["fichiers_laisses"], "refus nommé, aucun fichier")
spec = importlib.util.spec_from_file_location("sim9", V9)
sim9 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim9)
loi = sim9.LoiSynthetique(5, 10, 0.01, 0.4, 0.10, True, 0.0, True, 0.0, 0.0, 0.0, "logit", 0.0, 0.0, None, 0.05)
nulle = loi.variante_nulle(True)
try:
    nulle.tirer(np.random.default_rng(np.random.SeedSequence([20261030, 1])), 10, 32, 32, 9, 0.0)
    r2 = {"code": 0, "message": "aucun refus"}
except sim9.Refus as e:
    r2 = {"code": 1, "message": str(e)}
attendre("GD8-08 artefact 2 : variante nulle tirée à k = 9", r2, r2["code"] == 1 and "GD8-08" in r2["message"], "Refus de la loi")
try:
    nulle.tirer(np.random.default_rng(np.random.SeedSequence([20261030, 2])), 10, 32, 32, 8, 0.0)
    r3 = {"code": 0, "message": "tirage fait (neuvième inactif à k = 8)"}
except sim9.Refus as e:
    r3 = {"code": 1, "message": str(e)}
attendre("GD8-08 sain 3 : variante nulle tirée à k = 8", r3, r3["code"] == 0, "tirage sans refus")
# ---- GD8-07
rho = 0.10
r = lancer("gd8-07-sain-facteur2", ["--comparateurs", "8"] + COMB + ["--effet-unite-beta", str(rho), "--rho-comparateurs", str(rho), "--facteur-rho-honnetes", "2"])
ok, detail = r["code"] == 0, {}
if ok:
    d = json.load(open(r["sortie"], encoding="utf-8"))
    (nom_loi, L), = d["lois"].items()
    dec = L["decomposition_effet_unite"]["biais=0.0"]
    detail["nom_loi"] = nom_loi
    detail["rho_decomposition"] = {c: dec[c]["correlation_intra_unite"] for c in ("honnetes_fA", "sabotes_rA", "comparateurs_honnetes_fB", "comparateurs_sabotes_rB")}
    ok &= all(abs(detail["rho_decomposition"][c] - v) < 1e-12 for c, v in (("honnetes_fA", 2 * rho), ("sabotes_rA", rho),
                                                                             ("comparateurs_honnetes_fB", 2 * rho), ("comparateurs_sabotes_rB", rho)))
    (cel,) = d["cellules"].values()
    m = cel["moments_tires"]
    att = {"ecart_type_pA_honnetes": math.sqrt(2 * rho * 0.01 * 0.99), "ecart_type_pB_honnetes": math.sqrt(2 * rho * 0.01 * 0.99),
           "ecart_type_pA_sabotes": math.sqrt(rho * 0.5 * 0.5), "ecart_type_pB_sabotes": math.sqrt(rho * 0.4 * 0.6)}
    detail["ecarts_types_tires_contre_attendus"] = {c: [m[c], att[c], m[c] / att[c] - 1] for c in att}
    ok &= all(abs(v[2]) < (0.10 if "honnetes" in c else 0.05) for c, v in detail["ecarts_types_tires_contre_attendus"].items())
    ok &= "_rhoHonnetes2.0x" in nom_loi
attendre("GD8-07 sain : F = 2, dispersion combinée", r | {"detail": detail}, ok, "code 0 ; ρ honnête = 2ρ, saboté = ρ ; écarts-types tirés à 10 % (honnêtes) et 5 % (sabotés)")
for nom, opt in (("sans-combine", ["--comparateurs", "8", "--effet-unite-beta", "0.1", "--facteur-rho-honnetes", "2"]),
                 ("copule", ["--comparateurs", "8"] + COMB + ["--effet-unite-beta", "0.1", "--rho-comparateurs", "0.1", "--correlation-sujet-comparateurs", "0.5",
                                                          "--facteur-rho-honnetes", "2"]),
                 ("neuvieme", ["--comparateurs", "9"] + COMB + ["--effet-unite-beta", "0.1", "--rho-comparateurs", "0.1", "--ecart-contraste-neuvieme", "0.05",
                                                            "--facteur-rho-honnetes", "2"]),
                 ("f-rho-sup-1", ["--comparateurs", "8"] + COMB + ["--effet-unite-beta", "0.6", "--rho-comparateurs", "0.1", "--facteur-rho-honnetes", "2"]),
                 ("f-zero", ["--comparateurs", "8"] + COMB + ["--effet-unite-beta", "0.1", "--rho-comparateurs", "0.1", "--facteur-rho-honnetes", "0"]),
                 ("f-nan", ["--comparateurs", "8"] + COMB + ["--effet-unite-beta", "0.1", "--rho-comparateurs", "0.1", "--facteur-rho-honnetes", "nan"])):
    r = lancer(f"gd8-07-artefact-{nom}", opt)
    attendre(f"GD8-07 artefact : {nom}", r, r["code"] != 0 and "refus" in r["message"] and not r["fichiers_laisses"], "refus nommé, aucun fichier")
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "v9_sha256": hashlib.sha256(open(V9, "rb").read()).hexdigest(), "critere_ecrit_avant_execution": "tous les cas conformes à l'attendu (docstring)",
       "cas": cas, "conformes": sum(c["conforme"] for c in cas), "total": len(cas), "conforme": all(c["conforme"] for c in cas)}
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
fin = datetime.now(timezone.utc)
man = {"passage": os.path.basename(SORTIE)[:-5], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc_debut": debut.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin.strftime("%Y-%m-%dT%H:%M:%SZ"), "commande": sys.argv,
       "script_sha256": res["script_sha256"], "graines": "passages : graine maîtresse 20261029 du script v9 ; tirages directs : SeedSequence([20261030, 1|2]) (R9)",
       "environnement": {"python": platform.python_version(), "numpy": np.__version__},
       "fichiers": {os.path.basename(SORTIE): hashlib.sha256(open(SORTIE, "rb").read()).hexdigest()}
       | {p: hashlib.sha256(open(os.path.join(DOS, p), "rb").read()).hexdigest() for p in sorted(os.listdir(DOS)) if "essai-gd8" in p}}
with open(os.path.join(os.path.dirname(os.path.abspath(SORTIE)), "manifeste-" + os.path.basename(SORTIE)), "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("conforme :", res["conforme"], f"({res['conformes']}/{res['total']})")
