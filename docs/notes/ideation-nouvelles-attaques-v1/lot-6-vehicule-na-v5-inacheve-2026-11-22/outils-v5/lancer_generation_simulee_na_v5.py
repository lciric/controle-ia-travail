"""Une génération complète simulée du lot 6 v5, dans `GenerationNAV5`, sur le faux fournisseur (adaptateur direct réel du
lot 4 v3 sur le faux client de `simulation_na_v5`) : un refus de classifieur au premier proposeur d'une clé Claude, servi
par repli. Aucune clé, aucun réseau, aucune dépense. Écrit un résumé JSON neuf (jamais écrasé) et son compagnon.

    python -B lancer_generation_simulee_na_v5.py ORCHESTRATOR SORTIE.json
"""

import hashlib
import json
import os
import sys

racine, sortie = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(racine, "essais"))
sys.path.insert(0, racine)
import aides_na_lot6_v5 as H  # noqa: E402
from pole import simulation_na_v5 as s5  # noqa: E402

m = H.MontageV5(scenario={"ad_a": H.selon({("proposeur", H.CE.MODELE_ESSAI): [s5.REFUS]})})
bilan = m.lancer()  # le régime exige trois générations ; la génération 1 est décrite en entier
lignes = m.lignes_registre(1)
l = bilan[0]
resume = {
    "version": "demonstration-generation-simulee-na-v5",
    "generations_completes": len(bilan),
    "arrets": m.arrets(),
    "lignes_registre": {"tentative": sum(1 for x in lignes if x["type_ligne"] == "tentative"),
                        "fiche": sum(1 for x in lignes if x["type_ligne"] == "fiche")},
    "identifiants": [x["id_tentative"] for x in lignes if x["type_ligne"] == "tentative"],
    "chaines_de_repli": [[(x["id_tentative"], x["modele_demande"], x["raison_arret"], x["classe_issue"])
                          for x in lignes if x["type_ligne"] == "tentative" and x["id_tentative"][:8] == i[:8]]
                         for i in sorted({x["id_tentative"] for x in lignes if x["rang_repli"] > 0})],
    "coffre": l["coffre"],
    "coffre_par_generation": [x["coffre"] for x in bilan],
    "marques_par_repli_registre_servi_g2": bilan[1]["registre_servi"]["marques_par_repli"],
    "m6_par_espece": l["comptes_registre_v4"]["m6"]["par_espece"],
    "replis": l["comptes_registre_v4"]["replis"],
    "m4_replis": l["comptes_registre_v4"]["m4"]["replis"],
    "issues_proposeur": l["comptes_lot_6"]["issues_proposeur"],
    "code_charge_au_depart": m.depart()["code_charge"],
    "valeurs": "valeurs d'essai, non opposables",
}
octets = (json.dumps(resume, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
with open(sortie, "xb") as f:
    f.write(octets)
with open(sortie + ".sha256", "x", encoding="utf-8") as f:
    f.write(f"{hashlib.sha256(octets).hexdigest()}  {os.path.basename(sortie)}\n")
print(json.dumps({k: resume[k] for k in ("generations_completes", "arrets", "lignes_registre", "coffre")}, ensure_ascii=False))
