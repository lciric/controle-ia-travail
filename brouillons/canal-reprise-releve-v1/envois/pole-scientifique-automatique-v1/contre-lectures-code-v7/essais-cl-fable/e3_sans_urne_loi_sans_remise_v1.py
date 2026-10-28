"""E3 : configuration « sans urne » sur une banque figée. Le plan d'une fiche couvre toute la partie d'épreuve de son
moniteur (taille du plan 120 > 41 à 75 lignes) : la suite des issues est un tirage **sans remise** dans un effectif fini.
Le nul aveugle sans urne (marginale ajustée, uniforme, moyennes glissantes) ne domine pas une loi « sans_remise » (type
permis à toute fiche hors proposeur : `selection_pari.TYPES_LOI`, contrôlé par `valider_loi` seulement).

Pour chaque moniteur : log W final d'une fiche « sans_remise » dont la composition déclarée est l'effectif exact de
l'épreuve plus une marge s par classe (s = 0, 1, 2, 3), sans urne (nul informé ou non) et avec urne. Puis la fiche
s = 0 du moniteur le plus favorable passe dans la boucle réelle (`Generation`, agents simulés, e-BH, m = 1).
Note : cette loi n'emploie **aucun trait** ; toute promotion est fausse par construction.

Usage : python -I -B e3_sans_urne_loi_sans_remise_v1.py COPIE_DU_CODE DOSSIER_NEUF
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402
from pole.cycle import Budget, Generation  # noqa: E402
from pole.fiche import Fiche, RegistreGel  # noqa: E402
from pole.simulation import AdaptateurSimule, MondeSimule  # noqa: E402

DOSSIER = sys.argv[2]
os.makedirs(DOSSIER, exist_ok=False)
with open(a.BANQUE_V2, encoding="utf-8") as f:
    banque = json.load(f)
gabarit = a.charger(a.POPULATION_V2)[0]


def fiche_sans_remise(moniteur, composition, ident="SR-1"):
    k = banque["moniteurs"][moniteur]["nombre_issues"]
    d = dict(gabarit, identifiant=ident, enonce=f"La note {moniteur} suit un tirage sans remise (aucun trait)",
             loi_predictive={"type": "sans_remise", "composition": composition},
             espace_instances=dict(gabarit["espace_instances"], moniteur=moniteur, nombre_issues=k),
             operateurs=["sans_remise"])
    return a.fiche_depuis(d)


tableau = []
for moniteur in sorted(banque["moniteurs"]):
    k = banque["moniteurs"][moniteur]["nombre_issues"]
    ep = collections.Counter(l["issues"][moniteur] for l in banque["instances"]
                             if l["partie"] == "epreuve" and moniteur in l["issues"])
    exacte = [ep.get(c, 0) for c in range(k)]
    ligne = {"moniteur": moniteur, "k": k, "composition_epreuve": exacte, "n": sum(exacte)}
    for s in (0, 1, 2, 3):
        comp = [c + s for c in exacte]
        for nom, urne, informe in (("sans_urne_informe", False, True), ("sans_urne_aveugle", False, False),
                                   ("avec_urne_informe", True, True)):
            monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=informe)
            config = a.config_ligne_de_commande(urne=urne, multiplicite="aucune")
            _, ev, _ = a.juger(fiche_sans_remise(moniteur, comp), monde, config)
            ligne[f"s{s}_{nom}"] = {"log_w_finale": round(ev["log_richesse_finale"], 3),
                                    "log_w_max": round(ev["log_richesse_max"], 3), "promue": ev["promue"]}
    tableau.append(ligne)

# Boucle réelle : sans urne, nul informé, e-BH (réglages du bras « informe » de la démonstration de la couche 1)
meilleur = max(tableau, key=lambda l: l["s0_sans_urne_informe"]["log_w_finale"])
config = a.config_ligne_de_commande(urne=False, multiplicite="e-bh")
monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=True)
fiche = fiche_sans_remise(meilleur["moniteur"], meilleur["composition_epreuve"], ident="G0-F01")
adaptateur = AdaptateurSimule(20261026, MondeSimule(20261026))
r = Generation(0, adaptateur, config, os.path.join(DOSSIER, "boucle"), RegistreGel(), Budget(10.0),
               monde_noyau=monde).executer([fiche])
issue = r["issues"]["G0-F01"]
resultat = {"tableau": tableau, "boucle_reelle": {"moniteur": meilleur["moniteur"], "verdict": issue["verdict_final"],
                                                  "motif": issue.get("motif"),
                                                  "log_w_max": (issue.get("pari") or {}).get("log_richesse_max"),
                                                  "multiplicite": (issue.get("pari") or {}).get("multiplicite")}}
with open(os.path.join(DOSSIER, "e3-resultat-v1.json"), "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
for l in tableau:
    print(l["moniteur"], l["composition_epreuve"],
          {s: (l[f"s{s}_sans_urne_informe"]["log_w_finale"], l[f"s{s}_sans_urne_aveugle"]["log_w_finale"],
               l[f"s{s}_avec_urne_informe"]["log_w_finale"]) for s in (0, 1, 2, 3)})
print(json.dumps(resultat["boucle_reelle"], ensure_ascii=False))
