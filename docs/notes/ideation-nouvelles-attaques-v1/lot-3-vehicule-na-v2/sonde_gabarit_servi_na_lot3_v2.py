"""Sonde du développeur du lot 3 (hors du paquet) : le gabarit servi réel, lu à son empreinte, rempli des 120 lignes de
case possibles (mot de case de rang 0, chaque triplet), par `requete_na_v1`. Ne rend que des comptes, des tailles et des
empreintes ; aucun contenu.

`python -B sonde_gabarit_servi_na_lot3_v2.py RACINE_ORCHESTRATEUR CHEMIN_GABARIT`

v2 (remplace `sonde_gabarit_servi_na_lot3_v1.py`, `29d7b056…`) : des noms seuls changent (`requete_na_v2`, `tirage_na_v3`).
"""

import hashlib
import json
import sys

sys.path.insert(0, sys.argv[1])

from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import requete_na_v2 as rq  # noqa: E402
from pole import tirage_na_v3 as tn  # noqa: E402


def main():
    g = rq.lire_gabarit(sys.argv[2])  # empreinte par défaut : celle du gabarit servi
    legende = tn.lire_legende(g.octets, g.sha256)
    i = g.octets.index(rq.EMPLACEMENT)
    tailles, ok = [], 0
    for triplet in tn.cases_canoniques():
        ligne = tn.ligne_de_case(ident.mot_de_case(0), triplet, legende)
        case = rq.CaseServie(triplet, ident.mot_de_case(0), ligne)
        p = rq.remplir_partie_servie(g, case)
        lo = ligne.encode("utf-8")
        a_l_octet = (p.octets[:i] == g.octets[:i] and p.octets[i:i + len(lo)] == lo
                     and p.octets[i + len(lo):] == g.octets[i + len(rq.EMPLACEMENT):])
        s = rq.assembler_sonde_refus(g, case)
        ok += int(a_l_octet and s.octets == p.octets and p.octets[-1:] == g.octets[-1:])
        tailles.append(p.taille)
    print(json.dumps({"gabarit_sha256": g.sha256, "gabarit_octets": g.taille,
                      "dernier_octet_est_fin_de_ligne": g.octets[-1:] == b"\n",
                      "emplacements": g.octets.count(rq.EMPLACEMENT), "cases_remplies_a_l_octet": ok,
                      "cases": len(tailles), "partie_remplie_octets_min": min(tailles),
                      "partie_remplie_octets_max": max(tailles),
                      "empreinte_programme_requete": hashlib.sha256(open(rq.__file__, "rb").read()).hexdigest()},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
