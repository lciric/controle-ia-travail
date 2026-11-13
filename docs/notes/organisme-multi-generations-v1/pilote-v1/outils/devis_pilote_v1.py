"""Devis du pilote d'une génération (brouillon 1) : par fournisseur, crédits de Claude à part ; pire = plafonds de session ;
attendu = coûts centraux d'un appel de proposeur du devis v2 (`../../outils-v2/devis_multi_generations_v2.py`, `710954c7…`,
importés, **estimés**). Aucun expérimentateur, aucun vérificateur, aucun test de mort (dessin recommandé, Q-P2 (a)).
Usage : `python3 -I -B devis_pilote_v1.py SORTIE.json`. Bibliothèque standard ; aucun appel."""
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(ICI)), "outils-v2"))
import devis_multi_generations_v2 as D2  # noqa: E402

MONDES = 2
MACHINE_PLAFOND, MACHINE_ATTENDU = 3.0, 0.30  # estimés : quelques heures d'une petite machine, ou zéro au poste local
FAMILLE = {"fable52": "claude", "opus": "claude", "argon": "argon", "astra": "astra"}


def devis(bras):
    appels = MONDES * bras
    out = {f: {"attendu_usd": 0.0, "pire_usd": 0.0, "appels": 0} for f in ("claude", "argon", "astra")}
    for m, f in FAMILLE.items():
        out[f]["attendu_usd"] += appels * D2.CENTRAL_PROPOSEUR[m]
        out[f]["pire_usd"] += appels * D2.PLAFOND_SESSION[m]
        out[f]["appels"] += appels
    out = {f: {k: round(v, 2) for k, v in d.items()} for f, d in out.items()}
    hors = {"attendu_usd": round(out["argon"]["attendu_usd"] + out["astra"]["attendu_usd"] + MACHINE_ATTENDU, 2),
            "pire_usd": round(out["argon"]["pire_usd"] + out["astra"]["pire_usd"] + MACHINE_PLAFOND, 2)}
    return {"par_fournisseur": out, "machine": {"attendu_usd": MACHINE_ATTENDU, "plafond_usd": MACHINE_PLAFOND},
            "credits_de_claude": out["claude"], "hors_credits_avec_machine": hors,
            "total_pire_usd": round(out["claude"]["pire_usd"] + hors["pire_usd"], 2),
            "total_attendu_usd": round(out["claude"]["attendu_usd"] + hors["attendu_usd"], 2)}


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : devis_pilote_v1.py SORTIE.json (neuve)")
        return 2
    res = {"hypotheses": {"plafond_session": {m: D2.PLAFOND_SESSION[m] for m in FAMILLE},
                          "central_proposeur": {m: D2.CENTRAL_PROPOSEUR[m] for m in FAMILLE}, "mondes": MONDES},
           "bras_A_seul": devis(1), "bras_A_et_B": devis(2)}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
