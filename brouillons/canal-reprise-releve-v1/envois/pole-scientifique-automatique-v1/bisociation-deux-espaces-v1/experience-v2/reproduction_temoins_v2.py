"""Reproduction des témoins de v1 sur les mondes NR (liste d'arrêt, marge S12), sur les graines de validation.

NR_bien et NR_moyen : monde_v1 inchangé, graine de monde = premier mot de SeedSequence(...).generate_state(1)
(§ 6), RACINE_VALIDATION, indices 0 à 1199 (le nombre de S7 ; les conditions NR n'apparaissent dans aucune autre plage
de validation). Seuls les témoins b, a, c, d1 tournent : ni N, ni aucune de ses ablations, ni aucun contraste de
décision. Critère (liste d'arrêt) : moyenne de chaque témoin dans l'intervalle à 95 % du tableau de B § 1
(trancher-recombinaison-v1.md, 72cff8a0…) élargi de 2 points (S12).

Usage : PYTHONPATH=<dépôt>/src python3 -B reproduction_temoins_v2.py SORTIE.json [--processus 2]
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

import graines_v2 as gr
import mesures_v2 as ms
import travail_v2 as tr

TEMOINS = ["b", "a", "c", "d1"]
N_MONDES = 1200  # S7


def reproduire(processus=2, n=N_MONDES, racine=gr.RACINE_VALIDATION, indice0=0):
    ms.verifier_racine(racine, decision=False)
    res = {}
    for cond in ("NR_bien", "NR_moyen"):
        lignes = tr.executer_condition(cond, racine, range(indice0, indice0 + n), bras=TEMOINS, processus=processus)
        ok = [l for l in lignes if not l["exclu"]]
        prec = {b: np.array([l["bras"][b]["precision"] for l in ok]) for b in TEMOINS}
        moyennes = {b: float(v.mean()) for b, v in prec.items()}
        demi = {b: float(1.96 * v.std(ddof=1) / np.sqrt(len(v))) for b, v in prec.items()}
        res[cond] = {"n_mondes": len(lignes), "n_exclus": len(lignes) - len(ok), "moyennes": moyennes,
                     "demi_largeur_95": demi, "paires_valides_moyenne": float(np.mean([l["n_valides"] for l in lignes])),
                     "n_complete_moyen": {b: float(np.mean([l["bras"][b]["n_complete"] for l in ok])) for b in TEMOINS}}
        try:
            res[cond]["verification"] = ms.verifier_reproduction(cond, moyennes)
            res[cond]["dans_la_marge"] = True
        except GardeArret as e:
            res[cond]["verification"] = {"echec": str(e)}
            res[cond]["dans_la_marge"] = False
    return res


def main(argv):
    sortie = Path(argv[1])
    processus = int(argv[argv.index("--processus") + 1]) if "--processus" in argv else 2
    res = reproduire(processus)
    passee = all(r["dans_la_marge"] for r in res.values())
    corps = {"reproduction_passee": passee, "racine": gr.RACINE_VALIDATION, "indices": [0, N_MONDES - 1],
             "marge_S12": ms.MARGE_S12, "intervalles_B_1": ms.INTERVALLES_V1, "ecrit_le":
             datetime.now(timezone.utc).isoformat(timespec="seconds"), "conditions": res,
             "empreintes_code": ms.empreintes_code()}
    sortie.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(sortie)
    for cond, r in res.items():
        print(cond, "dans la marge :", r["dans_la_marge"], {b: round(m, 4) for b, m in r["moyennes"].items()},
              "exclus", r["n_exclus"], "paires valides", round(r["paires_valides_moyenne"], 2))
    return 0 if passee else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
