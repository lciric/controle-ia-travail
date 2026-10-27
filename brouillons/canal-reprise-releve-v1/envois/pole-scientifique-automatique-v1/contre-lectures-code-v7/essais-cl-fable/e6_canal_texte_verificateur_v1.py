"""E6 : canal de texte. Le vérificateur reçoit `mesures.json` (issues d'épreuve, copié avec le dossier de l'expérience :
pas dans `EXCLUS_DU_REJEU`) ; quand il ne confirme pas, son motif libre entre dans le motif de la fiche
(`Generation._verifier`), donc dans l'index de la mémoire, dans `resume-index.json` servi à la synthèse
(`causes_frequentes`), dans la leçon, et dans la consigne de l'agent de recombinaison qui écrit les lois des filles —
éprouvées sur les **mêmes lignes** d'épreuve (monde sur banque sans tranches). Boucle réelle `executer_pole`, banque jouet
des essais (`essais/test_v7_banque.banque_jouet`), agents simulés ; seul le vérificateur d'une fiche est remplacé.

Usage : python -I -B e6_canal_texte_verificateur_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import json
import os
import sys

COPIE, DOSSIER = sys.argv[1], sys.argv[2]
sys.path.insert(0, COPIE)
os.makedirs(DOSSIER, exist_ok=False)

from essais.test_v7_banque import banque_jouet, fiche_banque, loi_trait  # noqa: E402
from pole.cycle import ConfigGeneration  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.pole import executer_pole  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule, _bloc  # noqa: E402


class VerificateurBavard(AdaptateurSimule):
    def _verificateur(self, dossier):
        with open(os.path.join(dossier, "fiche.json"), encoding="utf-8") as f:
            enonce = json.load(f)["enonce"]
        if "FUITE" in enonce:
            with open(os.path.join(dossier, "mesures.json"), encoding="utf-8") as f:
                issues = json.load(f)["issues"]
            return _bloc("Je ne confirme pas.", {"confirme": False, "test_conforme": True,
                                                 "motif": "issues lues dans mesures.json : " + "".join(map(str, issues))}), "ok"
        return super()._verificateur(dossier)


chemin = os.path.join(DOSSIER, "banque-jouet.json")
banque_jouet(chemin)
population = [fiche_banque("A1", loi_trait(0), enonce="L'issue du moniteur A croît avec le premier trait (forte)"),
              fiche_banque("A2", loi_trait(0, force=0.9), enonce="L'issue du moniteur A croît avec le premier trait (douce)"),
              fiche_banque("A3", loi_trait(0, force=1.1), enonce="FUITE : l'issue du moniteur A suit le premier trait")]
temoins = [fiche_banque("TV", loi_trait(0, force=1.0), enonce="Témoin de contrôle numéro un", temoin="vraie"),
           fiche_banque("TF", loi_trait(1), enonce="Témoin de contrôle numéro deux", temoin="fausse")]
config = ConfigGeneration(selection="pari", juge="v1", nul_filles="v2", urne=False, multiplicite="e-bh",
                          temoins_sans_agent=True, taille_plan=120, taille_plan_filles=120, part_calibrage=12,
                          budget_generation_usd=50.0, graine=20261026).valider()
adaptateur = VerificateurBavard(20261026, MondeSimule(20261026))
monde = MondeBanque(chemin, 7, nul_informe=False)
bilan = executer_pole(population, temoins, adaptateur, config, 1, 50.0, os.path.join(DOSSIER, "course"),
                      monde_noyau=monde, temoins_par_generation=1)
racine = os.path.join(DOSSIER, "course", "archive", "generations", "generation-00")
mesures_fuite = None
for nom in os.listdir(racine):
    p = os.path.join(racine, nom, "experience", "fiche.json")
    if os.path.exists(p) and "FUITE" in json.load(open(p, encoding="utf-8"))["enonce"]:
        mesures_fuite = "".join(map(str, json.load(open(os.path.join(racine, nom, "experience", "mesures.json"),
                                                         encoding="utf-8"))["issues"]))
consignes_reco = []
for r, _, noms in os.walk(os.path.join(racine, "recombinaison")):
    if "consigne.txt" in noms:
        consignes_reco.append(open(os.path.join(r, "consigne.txt"), encoding="utf-8").read())
resume = open(os.path.join(racine, "synthese", "resume-index.json"), encoding="utf-8").read()
resultat = {"survivantes": bilan["survivantes"], "consignes_de_recombinaison": len(consignes_reco),
            "issues_d_epreuve_de_la_fiche_FUITE": mesures_fuite,
            "issues_dans_resume_index_servi_a_la_synthese": bool(mesures_fuite) and mesures_fuite in resume,
            "issues_dans_la_consigne_de_recombinaison": bool(mesures_fuite) and any(mesures_fuite in c for c in consignes_reco),
            "extrait_consigne": next((c[c.find("issues lues"):c.find("issues lues") + 160] for c in consignes_reco
                                      if "issues lues" in c), None)}
with open(os.path.join(DOSSIER, "e6-resultat-v1.json"), "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
