"""E1b : héritage de la preuve sur une banque figée — la boucle réelle (Memoire, RegistreGel, Generation, agents simulés
honnêtes, MondeBanque), deux générations, comme `executer_pole` (garde de redite, exécution, indexation).

Génération 0 : la fiche F (loi de la population scriptée) est éprouvée sur la partie d'épreuve de son moniteur.
Génération 1 : une redite F' (même loi, autre identifiant et autre énoncé : même classe par la signature) est éprouvée
sur **les mêmes lignes** de la banque (aucune tranche) ; elle hérite du log W final de F (produit d'e-valeurs supposées
« sur des tirages frais »). Lecture : F' est-elle promue alors qu'aucune donnée neuve n'a été vue ?

Usage : python -I -B e1b_heritage_sur_banque_pipeline_v1.py COPIE_DU_CODE DOSSIER_NEUF [urne:0|1] [informe:0|1] [ident]
"""
import json
import os
import sys

COPIE, SORTIE = sys.argv[1], sys.argv[2]
URNE = (sys.argv[3] if len(sys.argv) > 3 else "0") == "1"
INFORME = (sys.argv[4] if len(sys.argv) > 4 else "1") == "1"
IDENT = sys.argv[5] if len(sys.argv) > 5 else "3B-RESU-jetons_p-plus"
sys.path.insert(0, COPIE)
os.makedirs(SORTIE, exist_ok=False)

from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import Fiche, RegistreGel  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

BANQUE = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
with open(os.path.join(COPIE, "exemples", "population-banque-t05-v2.json"), encoding="utf-8") as f:
    modele = next(d for d in json.load(f)["fiches"] if d["identifiant"] == IDENT)

config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=URNE, multiplicite="e-bh",
                          nul_archive=True, nul_archive_ajuste=True, graine=20261026, taille_plan=120,
                          taille_plan_filles=300).valider()
monde = MondeBanque(BANQUE, 20261026, nul_informe=INFORME)
adaptateur = AdaptateurSimule(20261026, MondeSimule(20261026))
memoire, registre, depots = Memoire(active=True, graine=config.graine), RegistreGel(), {}
lois = {}
journal = []
for g, (ident, enonce) in enumerate([("G0-F01", modele["enonce"]),
                                     ("G1-F01", modele["enonce"] + " (reprise d'une éliminée, même loi)")]):
    d = dict(modele, identifiant=ident, enonce=enonce)
    fiche = Fiche.depuis_dict(d).valider()
    memoire.nouvelle_generation()
    garde = memoire.garde_redite(fiche)
    lois[fiche.identifiant] = fiche.loi_predictive
    rapport = Generation(g, adaptateur, config, SORTIE, registre, Budget(10.0), memoire, lois, monde_noyau=monde,
                         depots=depots).executer([fiche])
    issue = rapport["issues"][ident]
    memoire.indexer(fiche, issue, g)
    pari = issue.get("pari") or {}
    journal.append({"generation": g, "identifiant": ident, "garde": garde["motif"], "verdict": issue["verdict_final"],
                    "motif": issue.get("motif"), "log_w_finale": pari.get("log_richesse_finale"),
                    "log_w_max": pari.get("log_richesse_max"), "heritage": pari.get("heritage"),
                    "multiplicite": pari.get("multiplicite"), "nombre_tirages": pari.get("nombre_tirages"),
                    "instances_du_plan": [json.dumps(i, sort_keys=True) for i in
                                          json.load(open(os.path.join(SORTIE, "archive", "generations",
                                                                      f"generation-{g:02d}", ident, "experience",
                                                                      "engagement.json"), encoding="utf-8"))["instances"]],
                    "issues_deposees": json.load(open(os.path.join(SORTIE, "archive", "generations", f"generation-{g:02d}",
                                                                   ident, "experience", "mesures.json"),
                                                      encoding="utf-8"))["issues"]})
meme_lignes = sorted(journal[0]["instances_du_plan"]) == sorted(journal[1]["instances_du_plan"])
for j in journal:
    j["instances_du_plan"] = len(j["instances_du_plan"])
resultat = {"reglages": {"urne": URNE, "nul_informe": INFORME, "multiplicite": config.multiplicite,
                         "politique_redite": config.politique_redite, "fiche": IDENT},
            "journal": journal, "memes_lignes_de_banque_aux_deux_generations": meme_lignes,
            "memes_issues_multiensemble": sorted(journal[0]["issues_deposees"]) == sorted(journal[1]["issues_deposees"]),
            "redite_promue": journal[1]["verdict"] == "survit"}
with open(os.path.join(SORTIE, "e1b-resultat-v1.json"), "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in resultat.items()}, ensure_ascii=False, indent=1)[:4000])
