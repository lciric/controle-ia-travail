"""Tables de conception de la règle du bras, version 2 : probabilités exactes des quatre verdicts, du témoin à faille
plantée, du nul (décompte et comparaison de rang), du critère de dommage honnête, de la réserve sur plusieurs moniteurs.
Aucune donnée. Usage (racine du dépôt, arbre propre) : PYTHONPATH=src python scripts/bras_attaque_verdicts_v1.py
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

from controle_ia.bras_attaque import puissance_seuil_v1 as p
from controle_ia.bras_attaque import verdicts_v1 as v
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, generateur

CONFIG = {
    "objet": "règle du bras, conception v2 : verdicts, témoin, nul, dommage honnête, réserve",
    "niveau": 0.95,
    "delta": 0.10,
    "verdicts": {"m": [50, 100, 200],
                 "scenarios": [[0.10, 0.10], [0.10, 0.15], [0.10, 0.25], [0.10, 0.40], [0.10, 0.60],
                               [0.30, 0.30], [0.30, 0.45], [0.30, 0.70], [0.05, 0.40]]},
    "temoin": {"m": [50, 100], "cas": [[0.6, 0.1], [0.8, 0.1], [0.8, 0.3], [0.95, 0.05]]},
    "nul": {"n": [600, 1000, 2000], "h": [500, 1000], "inflation": [1.0, 2.0, 5.0],
            "niveaux": {"M=5": 0.99, "M=10": 0.995, "M=20": 0.9975}},
    "dommage_honnete": {"h": [500, 1000], "erreurs": [0.005, 0.01, 0.02], "plafond": 0.02},
    "rang": {"n": 1000, "h": 500, "decalages": [-0.27, -0.15, 0.0, 0.15, 0.27], "niveau_test": 0.01,
             "ecart_aire": 0.05, "tirages": 400},
    "reserve": {"n": [600, 1000], "M": [1, 5, 10], "fpr_max": 0.02},
}
TACHES = ["rang"]


def calculer(manifeste: dict) -> dict:
    c = CONFIG
    verdicts = [{"m": m, "e_naif": en, "e_bras": eb,
                 **v.verdicts_exacts(m, m, eb, en, c["delta"], c["niveau"])}
                for m in c["verdicts"]["m"] for en, eb in c["verdicts"]["scenarios"]]
    temoin = [{"m": m, "e_bras": eb, "e_naif": en, **v.temoin_faille_exact(m, eb, en, c["niveau"])}
              for m in c["temoin"]["m"] for eb, en in c["temoin"]["cas"]]
    pires = {str(m): dict(zip(("probabilite", "evasion"), v.fausse_cassure_pire(m, c["niveau"]))) for m in c["temoin"]["m"]}
    nul = []
    for n in c["nul"]["n"]:
        k = p.k_empirique(n, 0.01)
        for h in c["nul"]["h"]:
            for nom, niv in c["nul"]["niveaux"].items():
                nul.append({"n": n, "h": h, "M": nom, "niveau": niv,
                            "intervalle": list(p.alertes_honnetes_intervalle(n, k, h, niv)),
                            "proba_ecart": {str(f): v.nul_sensibilite_exacte(n, k, h, f, niv)
                                            for f in c["nul"]["inflation"]}})
    dommage = [{"h": h, "erreur_juge": q, "chute": v.dommage_honnete_chute(h, q, c["dommage_honnete"]["plafond"])}
               for h in c["dommage_honnete"]["h"] for q in c["dommage_honnete"]["erreurs"]]
    g = generateur(manifeste["graines"]["rang"])
    r = c["rang"]
    rang = [{"decalage": d, "proba_ecart": v.puissance_rang_binormal(r["n"], r["h"], d, r["niveau_test"],
                                                                    r["ecart_aire"], r["tirages"], g)}
            for d in r["decalages"]]
    reserve = []
    for n in c["reserve"]["n"]:
        q = p.fpr_reel_proba_au_dela(n, p.k_empirique(n, 0.01), c["reserve"]["fpr_max"])
        reserve.append({"n": n, "un_moniteur": q,
                        "au_moins_un_sur_M": {str(M): 1 - (1 - q) ** M for M in c["reserve"]["M"]}})
    return {"verdicts": verdicts, "temoin": temoin, "fausse_cassure_pire": pires, "nul": nul,
            "dommage_honnete": dommage, "rang": rang, "reserve": reserve}


def main() -> int:
    racine = Path(__file__).resolve().parents[1]
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-bras-verdicts-v1"
    chemin, manifeste = creer_manifeste(racine, run_id, CONFIG, TACHES,
                                        commande="PYTHONPATH=src python scripts/bras_attaque_verdicts_v1.py")
    sortie = ecrire_resultat(racine, chemin, "verdicts-v1", calculer(manifeste))
    print(chemin)
    print(sortie)
    return 0


if __name__ == "__main__":
    sys.exit(main())
