"""E5b : clés complètes de la qualité quand l'expérimentateur s'abstient sur les 13 « Témoin faux » (reprise, en script,
d'une vérification faite d'abord en ligne de commande, dossier `sorties/e5-bis`), et m de la règle e-BH.

Usage : python -I -B e5b_qualite_temoins_faux_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
COPIE, DOSSIER = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
os.makedirs(DOSSIER, exist_ok=False)
source = open(os.path.join(ICI, "e5_temoins_reconnaissables_dents_v1.py"), encoding="utf-8").read().split('resultat = {"honnete"')[0]
sys.argv = [sys.argv[0], COPIE, os.path.join(DOSSIER, "inutilise")]
exec(compile(source, "e5", "exec"))  # classes et données de e5 (ExperimentateurQuiReconnaitLesTemoins, banque, témoins)
from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402

cfg = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, multiplicite="e-bh", temoins_sans_agent=False,
                       graine=20261026, taille_plan=120, taille_plan_filles=300, budget_generation_usd=200.0).valider()
monde = MondeBanque(BANQUE, 20261026, nul_informe=False)
fiches = list(population[:6]) + list(temoins)
for i, f in enumerate(fiches):
    f.identifiant = f"G0-F{i:02d}"
ad = ExperimentateurQuiReconnaitLesTemoins(20261026, MondeSimule(20261026), cible="Témoin faux")
r = Generation(0, ad, cfg, os.path.join(DOSSIER, "course"), RegistreGel(), Budget(200.0), monde_noyau=monde).executer(fiches)
q = dict(r["qualite"])
q.pop("detail")
ms = sorted({i["pari"]["multiplicite"]["m"] for i in r["issues"].values() if i.get("pari")})
resultat = {"qualite": q, "m_e_bh": ms, "fiches_gelees": len(fiches)}
with open(os.path.join(DOSSIER, "e5b-resultat-v1.json"), "w", encoding="utf-8") as fo:
    json.dump(resultat, fo, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
