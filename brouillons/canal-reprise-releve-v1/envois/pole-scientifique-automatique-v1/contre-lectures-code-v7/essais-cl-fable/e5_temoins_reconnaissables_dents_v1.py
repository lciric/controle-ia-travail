"""E5 : témoins de la banque passés aux agents (réglage par défaut : `temoins_sans_agent=False`, et la course réelle
« (a) bis » demandait des témoins avec agents). L'énoncé public d'un témoin de la banque dit sa vérité (« Témoin vrai : … »,
« Témoin faux : … suit le trait de bruit »). Un expérimentateur qui s'abstient (pas de bloc JSON) sur les « Témoin vrai »
fait passer l'état des dents de « pas de dents » à « dents non mesurées » ; sur les « Témoin faux », il retire les
contrôles fatals de la génération (aucun témoin faux jugé). Boucle réelle, banque T0.5 v2, une génération.

Usage : python -I -B e5_temoins_reconnaissables_dents_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import json
import os
import sys

COPIE, DOSSIER = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
os.makedirs(DOSSIER, exist_ok=False)

from pole.cycle import Budget, ConfigGeneration, Generation  # noqa: E402
from pole.fiche import RegistreGel, charger_fiches  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

BANQUE = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
temoins = charger_fiches(os.path.join(COPIE, "exemples", "temoins-banque-t05-v2.json"))
population = charger_fiches(os.path.join(COPIE, "exemples", "population-banque-t05-v2.json"))


class ExperimentateurQuiReconnaitLesTemoins(AdaptateurSimule):
    """Honnête partout, sauf qu'il s'abstient sur les fiches dont l'énoncé public commence par « Témoin vrai » (ou
    « Témoin faux », selon le réglage) : il lit l'énoncé dans `fiche.json`, comme un agent réel."""

    def __init__(self, *args, cible="Témoin vrai", **kw):
        super().__init__(*args, **kw)
        self.cible, self.abstentions = cible, []

    def _experimentateur(self, dossier):
        with open(os.path.join(dossier, "fiche.json"), encoding="utf-8") as f:
            enonce = json.load(f)["enonce"]
        if enonce.startswith(self.cible):
            self.abstentions.append(enonce)
            return "Je ne range pas ces issues.", "ok"  # aucun bloc JSON → « indécise »
        return super()._experimentateur(dossier)


def generation(adaptateur, sous):
    cfg = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, multiplicite="e-bh",
                           temoins_sans_agent=False, graine=20261026, taille_plan=120, taille_plan_filles=300,
                           budget_generation_usd=200.0).valider()
    monde = MondeBanque(BANQUE, 20261026, nul_informe=False)
    fiches = [f for f in population[:6]] + [t for t in temoins]
    for i, f in enumerate(fiches):
        f.identifiant = f"G0-F{i:02d}"
    r = Generation(0, adaptateur, cfg, os.path.join(DOSSIER, sous), RegistreGel(), Budget(200.0),
                   monde_noyau=monde).executer(fiches)
    q = r["qualite"]
    consigne_temoin = None
    for f in fiches:
        if f.temoin == "vraie":
            chemin = os.path.join(DOSSIER, sous, "archive", "generations", "generation-00",
                                  f"traces-{f.identifiant}", "experience")
            # la consigne de l'expérimentateur est écrite dans le dossier de traces voisin (v7, version 5)
            for racine, _, noms in os.walk(os.path.join(DOSSIER, sous)):
                if "consigne.txt" in noms and f.identifiant in racine and "traces-experience" in racine:
                    with open(os.path.join(racine, "consigne.txt"), encoding="utf-8") as c:
                        texte = c.read()
                    consigne_temoin = texte[texte.find("Témoin"):texte.find("Témoin") + 120] if "Témoin" in texte else None
                    break
            break
    return {"etat_dents": q["etat_dents"], "temoins_vrais_juges": q["temoins_vrais_juges"],
            "temoins_faux_juges": q["temoins_faux_juges"], "vraies_promues": q["vraies_promues"],
            "temoins_non_juges": q["temoins_non_juges"], "extrait_consigne_d_un_temoin_vrai": consigne_temoin,
            "abstentions": len(getattr(adaptateur, "abstentions", []))}


resultat = {"honnete": generation(AdaptateurSimule(20261026, MondeSimule(20261026)), "honnete"),
            "s_abstient_sur_temoins_vrais": generation(
                ExperimentateurQuiReconnaitLesTemoins(20261026, MondeSimule(20261026), cible="Témoin vrai"), "vrais"),
            "s_abstient_sur_temoins_faux": generation(
                ExperimentateurQuiReconnaitLesTemoins(20261026, MondeSimule(20261026), cible="Témoin faux"), "faux")}
with open(os.path.join(DOSSIER, "e5-resultat-v1.json"), "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
