#!/usr/bin/env python3
"""Vrai pire du pilote sous les gardes v4 (`garde_pilote_essaim_v2.borne_pire`, plan gelé appel par appel), par espèce
(tarifs lus par `calcul_devis_essaim_v4.tarifs()`, pièces à leur empreinte) et par taille de pilote. Seul Kimi est gelé dans
le lanceur v4 (`PRIX_GELES`) : les autres espèces sont rendues pour comparaison, et demanderaient un nouveau gel.
Rend aussi le pire de la v3 (`garde_pilote_essaim_v1`, depuis `devis-et-instruments-v3/`) pour la différence.
Aucun appel, aucun réseau. Usage : python -I -B calcul_vrai_pire_v4.py SORTIE.json"""
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import racine_depot_v1 as R  # noqa: E402
import calcul_devis_essaim_v4 as C4  # noqa: E402
import garde_pilote_essaim_v2 as G2  # noqa: E402

G1_REL = "docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/garde_pilote_essaim_v1.py"


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        return 2
    s1 = R.verifier_compagnon(G1_REL)
    spec = importlib.util.spec_from_file_location("garde_pilote_essaim_v1", R.chemin(G1_REL))
    G1 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G1)
    prix, src = C4.tarifs()
    out = {"version": "calcul-vrai-pire-v4", "script_sha256": R.sha_fichier(os.path.abspath(__file__)), "garde_v2_sha256": R.sha_fichier(G2.__file__),
           "garde_v1": {"chemin": G1_REL, "sha256": s1}, "plan_sha256": G2.PLAN_SHA256, "prix_geles_lanceur": list(G2.PRIX_GELES),
           "kimi_table_egale_gel": tuple(prix["kimi"]) == G2.PRIX_GELES, "par_espece": {}}
    for esp in sorted(prix):
        p = tuple(prix[esp])
        out["par_espece"][esp] = {"prix": list(p),
                                  **{f"P-{n}": {"v4": G2.borne_pire(G2.plan_pstd(mondes=n), p), "v3_pire_usd": G1.borne_pire(G1.plan_pstd(mondes=n), p)["pire_usd"]}
                                     for n in (8, 12, 24)}}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({e: {k: (v["v4"]["pire_usd"], v["v3_pire_usd"]) for k, v in d.items() if k.startswith("P-")} for e, d in out["par_espece"].items()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
