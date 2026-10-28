"""E10 : deux essais courts sur la boucle réelle.

(a) Repli silencieux : `temoins_sans_agent=True` sans monde tenu par le noyau (ni banque ni monde du noyau) — la
    configuration est acceptée (`ConfigGeneration.valider`) et les témoins passent quand même par les agents, sans motif.
(b) Classe sans moniteur : la signature d'une fiche (`Memoire.signature`) ignore le moniteur de la banque ; une fiche
    sur le moniteur M2 dont la loi est celle d'une éliminée du moniteur M1 hérite du log W cumulé gagné sur M1.

Usage : python -I -B e10_repli_temoins_et_classe_sans_moniteur_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import json
import os
import sys

COPIE, DOSSIER = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
os.makedirs(DOSSIER, exist_ok=False)

from essais.aides import fiche  # noqa: E402
from essais.test_v7_banque import fiche_banque, loi_trait  # noqa: E402
from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import Fiche, RegistreGel  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

resultat = {}
# (a)
cfg = ConfigGeneration(selection="pari", temoins_sans_agent=True, taille_plan=60, taille_plan_filles=60,
                       part_calibrage=10, reservoir=200).valider()
ad = AdaptateurSimule(3, MondeSimule(3))
t = fiche_banque("TV", loi_trait(0), temoin="vraie")
t.espace_instances = {"nombre_issues": 3, "dimension": 2}
r = Generation(0, ad, cfg, os.path.join(DOSSIER, "a"), RegistreGel(), Budget(10.0)).executer([t])
resultat["a_temoins_sans_agent_sans_monde_du_noyau"] = {
    "configuration_acceptee": True, "agents_lances_pour_le_temoin": sorted({a["role"] for a in ad.appels}),
    "issue_marquee_sans_agent": bool(r["issues"]["TV"].get("sans_agent")), "motif": r["issues"]["TV"].get("motif")}

# (b)
BANQUE = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
with open(os.path.join(COPIE, "exemples", "population-banque-t05-v2.json"), encoding="utf-8") as f:
    modele = next(d for d in json.load(f)["fiches"] if d["identifiant"] == "3B-RESU-jetons_p-plus")
config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, multiplicite="e-bh",
                          nul_archive=True, nul_archive_ajuste=True, graine=20261026).valider()
monde = MondeBanque(BANQUE, 20261026, nul_informe=True)
memoire, registre, depots, lois, journal = Memoire(active=True, graine=config.graine), RegistreGel(), {}, {}, []
for g, moniteur in enumerate(("3B:RESULT_REASONING", "3B:RIGOR")):
    d = dict(modele, identifiant=f"G{g}-F01", enonce=f"Loi sur jetons_par_action_ecart_type pour {moniteur}",
             espace_instances=dict(modele["espace_instances"], moniteur=moniteur))
    f = Fiche.depuis_dict(d).valider()
    memoire.nouvelle_generation()
    garde = memoire.garde_redite(f)
    lois[f.identifiant] = f.loi_predictive
    rap = Generation(g, AdaptateurSimule(5, MondeSimule(5)), config, os.path.join(DOSSIER, "b"), registre, Budget(10.0),
                     memoire, lois, monde_noyau=monde, depots=depots).executer([f])
    issue = rap["issues"][f.identifiant]
    memoire.indexer(f, issue, g)
    pari = issue.get("pari") or {}
    journal.append({"generation": g, "moniteur": moniteur, "garde": garde["motif"], "verdict": issue["verdict_final"],
                    "log_w_finale": pari.get("log_richesse_finale"), "log_w_max": pari.get("log_richesse_max"),
                    "heritage": pari.get("heritage")})
resultat["b_classe_sans_moniteur"] = journal
with open(os.path.join(DOSSIER, "e10-resultat-v1.json"), "w", encoding="utf-8") as fo:
    json.dump(resultat, fo, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
