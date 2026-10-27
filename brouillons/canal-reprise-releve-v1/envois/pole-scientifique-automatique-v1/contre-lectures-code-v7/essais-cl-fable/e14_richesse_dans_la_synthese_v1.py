"""E14 : une richesse chiffrée atteint-elle un agent ? Le motif d'une redite éliminée porte « log W cumulé x »
(`Generation._juger_pari`) ; il entre dans l'index de la mémoire, puis dans `resume_pour_synthese` (causes fréquentes)
servi à l'agent de synthèse, dont la leçon est servie aux expérimentateurs et à la recombinaison. Boucle réelle sur la
banque v2 (sans urne, nul informé), deux générations, puis appel de la synthèse comme `executer_pole`.

Usage : python -I -B e14_richesse_dans_la_synthese_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import json
import os
import sys

COPIE, DOSSIER = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
os.makedirs(DOSSIER, exist_ok=False)

from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import Fiche, RegistreGel  # noqa: E402
from pole.memoire import Memoire  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.pole import _synthese  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

BANQUE = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
with open(os.path.join(COPIE, "exemples", "population-banque-t05-v2.json"), encoding="utf-8") as f:
    modele = next(d for d in json.load(f)["fiches"] if d["identifiant"] == "8B-REDU-actions_-plus")
config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, multiplicite="e-bh", graine=20261026,
                          nul_archive=True, nul_archive_ajuste=True).valider()
monde = MondeBanque(BANQUE, 20261026, nul_informe=True)
adaptateur = AdaptateurSimule(20261026, MondeSimule(20261026))
memoire, registre, depots, lois = Memoire(active=True, graine=config.graine), RegistreGel(), {}, {}
for g in range(2):
    f = Fiche.depuis_dict(dict(modele, identifiant=f"G{g}-F01", enonce=modele["enonce"] + ("" if g == 0 else " (reprise)"))).valider()
    memoire.nouvelle_generation()
    memoire.garde_redite(f)
    lois[f.identifiant] = f.loi_predictive
    rap = Generation(g, adaptateur, config, DOSSIER, registre, Budget(10.0), memoire, lois, monde_noyau=monde,
                     depots=depots).executer([f])
    memoire.indexer(f, rap["issues"][f.identifiant], g)
lecons, _ = _synthese(adaptateur, config, memoire, Budget(10.0), os.path.join(DOSSIER, "synthese"), 1)
resume = memoire.resume_pour_synthese(1)
resultat = {"causes_frequentes_servies_a_la_synthese": resume["causes_frequentes"], "lecon": lecons,
            "richesse_dans_le_resume": any("log W cumulé" in m for m, _ in resume["causes_frequentes"]),
            "richesse_dans_la_consigne_des_experimentateurs": "log W cumulé" in memoire.texte_consigne("experimentateur"),
            "richesse_dans_la_consigne_de_recombinaison": "log W cumulé" in memoire.texte_consigne("recombinaison")}
with open(os.path.join(DOSSIER, "e14-resultat-v1.json"), "w", encoding="utf-8") as fo:
    json.dump(resultat, fo, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
