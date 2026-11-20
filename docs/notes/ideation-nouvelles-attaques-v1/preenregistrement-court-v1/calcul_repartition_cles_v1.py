"""Contre-lecture du préenregistrement court « nouvelles attaques » v1 : coûts par rôle du
premier relais sur trois générations et répartition entre les clés Minuit, Luc, Rigaud.

Entrée : le chemin de la sortie du calcul du devis v2 (JSON), passé en argument.
Coûts bas par rôle et par génération : devis v2, § 1, clé S1 (7,43 ; 17,58 ; 4,59 ; 6,86),
contrôlés contre le JSON (somme du premier relais à la course v9, 36,46).
Sortie : JSON sur la sortie standard. Processeur seul ; aucun réseau.
"""
from __future__ import annotations

import itertools
import json
import sys
from decimal import ROUND_HALF_UP, Decimal as D

GEN = 3
Q = D("0.01")


def r2(x: D) -> D:
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def main() -> None:
    sortie_devis = json.loads(open(sys.argv[1], encoding="utf-8").read())
    f = sortie_devis["facteurs_du_haut_par_role"]
    f_prop, f_aig, f_jug = D(f["proposition"]), D(f["aiguillage"]), D(f["juges"])
    a = sortie_devis["compositions"]["A"]
    # facteurs exacts, recalculés à partir des totaux du JSON (contrôle de l'arrondi à 4 décimales)
    bas, haut = a["par_generation_usd"]["bas"], a["par_generation_usd"]["haut"]
    f_exacts = {
        "proposition": D(haut["proposition"]) / D(bas["proposition"]),
        "aiguillage": D(haut["aiguillage"]) / D(bas["aiguillage"]),
        "juges": D(haut["juges"]) / D(bas["juges"]),
    }
    pire_appel_prop = D(sortie_devis["reperes"]["pire_par_appel_de_proposeur_usd"])
    plafond_gen = D(a["par_generation_usd"]["pire_plafond_d_arret"])

    # S1, par génération (devis v2, § 1) ; facteur du haut ; pire sur la course
    roles = {
        "P3": (D("7.43"), f_prop, pire_appel_prop * 11 * GEN),   # proposeur espèce 3
        "P4": (D("17.58"), f_prop, pire_appel_prop * 11 * GEN),  # proposeur espèce 4
        "A": (D("4.59"), f_aig, plafond_gen * GEN),              # aiguilleur
        "J3": (D("6.86"), f_jug, plafond_gen * GEN),             # juge espèce 3
    }
    controle_relais_v9 = sum(v[0] for v in roles.values())

    couts = {}
    for k, (b, fac, pire) in roles.items():
        couts[k] = {"bas": r2(b * GEN), "haut": r2(b * GEN * fac), "pire": r2(pire)}
    somme = {c: str(sum(couts[k][c] for k in couts)) for c in ("bas", "haut")}

    soldes_base = {"Minuit": D("162.56"), "Luc": D("214"), "Rigaud": D("47")}
    cles = list(soldes_base)

    def evaluer(unites: dict[str, list[str]], affect: tuple[str, ...], soldes: dict[str, D]):
        charge = {c: {"bas": D(0), "haut": D(0), "pire": D(0)} for c in cles}
        for (nom, membres), cle in zip(unites.items(), affect):
            for m in membres:
                for cas in ("bas", "haut", "pire"):
                    charge[cle][cas] += couts[m][cas]
        lignes = {}
        ratios, marges = [], []
        tient_haut = True
        for c in cles:
            h = charge[c]["haut"]
            if h == 0:
                lignes[c] = {"roles": [], "bas": "0", "haut": "0"}
                continue
            ratio = soldes[c] / h
            marge = soldes[c] - h
            if marge < 0:
                tient_haut = False
            ratios.append(ratio)
            marges.append(marge)
            lignes[c] = {
                "roles": [n for (n, _), k in zip(unites.items(), affect) if k == c],
                "bas": str(charge[c]["bas"]),
                "haut": str(h),
                "pire": str(charge[c]["pire"]),
                "solde": str(soldes[c]),
                "rapport_solde_sur_haut": str(ratio.quantize(D("0.001"))),
                "marge_usd_sur_haut": str(r2(marge)),
            }
        return tient_haut, min(ratios), min(marges), lignes

    lectures = {
        "role_par_role": {"P3": ["P3"], "P4": ["P4"], "A": ["A"], "J3": ["J3"]},
        "espece_entiere": {"S3": ["P3", "J3"], "S4": ["P4"], "A": ["A"]},
    }
    besoins_bras_a = [D("0"), D("10"), D("20"), D("20.39"), D("20.40"), D("25"), D("47")]

    resultats = {}
    for nom_lecture, unites in lectures.items():
        par_besoin = {}
        for x in besoins_bras_a:
            soldes = dict(soldes_base)
            soldes["Rigaud"] = soldes_base["Rigaud"] - x
            candidates = []
            for affect in itertools.product(cles, repeat=len(unites)):
                tient, rmin, mmin, lignes = evaluer(unites, affect, soldes)
                if tient:
                    candidates.append((rmin, mmin, affect, lignes))
            candidates.sort(key=lambda t: (t[0], t[1]), reverse=True)
            par_besoin[str(x)] = {
                "nombre_de_repartitions_qui_tiennent_au_haut": len(candidates),
                "trois_meilleures_par_rapport_minimal": [
                    {
                        "affectation": dict(zip(unites, aff)),
                        "rapport_minimal": str(rm.quantize(D("0.001"))),
                        "marge_minimale_usd": str(r2(mm)),
                        "cles": lg,
                    }
                    for rm, mm, aff, lg in candidates[:3]
                ],
            }
        resultats[nom_lecture] = par_besoin

    # la proposition du rédacteur, telle qu'écrite, et la variante de repli qu'il écrit
    proposee = {}
    unites_rr = lectures["role_par_role"]
    for nom, aff in {
        "redacteur_Minuit_A_P4__Luc_J3__Rigaud_P3": ("Rigaud", "Minuit", "Minuit", "Luc"),
        "repli_redacteur_Minuit_A_P4_P3__Luc_J3": ("Minuit", "Minuit", "Minuit", "Luc"),
        "contre_lecture_Minuit_J3__Luc_A_P4__Rigaud_P3": ("Rigaud", "Luc", "Luc", "Minuit"),
        "repli_contre_lecture_Minuit_J3__Luc_A_P4_P3": ("Luc", "Luc", "Luc", "Minuit"),
    }.items():
        tient, rm, mm, lg = evaluer(unites_rr, aff, soldes_base)
        proposee[nom] = {
            "tient_au_haut_avec_Rigaud_47": tient,
            "rapport_minimal": str(rm.quantize(D("0.001"))),
            "marge_minimale_usd": str(r2(mm)),
            "cles": lg,
        }

    # recharge de 27 USD sur Minuit (variante écrite par le rédacteur)
    variante_minuit = (soldes_base["Minuit"] + 27) / (couts["A"]["haut"] + couts["P4"]["haut"])

    print(json.dumps({
        "piece": "contre-lecture, calcul de la répartition par clé, v1",
        "controle_relais_1_v9_par_generation": str(controle_relais_v9),
        "facteurs_du_haut_json_4_decimales": {k: str(v) for k, v in f.items()},
        "facteurs_du_haut_exacts": {k: str(v.quantize(D("0.000001"))) for k, v in f_exacts.items()},
        "couts_par_role_sur_trois_generations_usd": {k: {c: str(v) for c, v in d.items()} for k, d in couts.items()},
        "somme_premier_relais_usd": somme,
        "somme_des_soldes_usd": str(sum(soldes_base.values())),
        "manque_a_450_usd": str(D(450) - sum(soldes_base.values())),
        "seuil_besoin_bras_a_pour_P3_sur_Rigaud_au_haut_usd": str(soldes_base["Rigaud"] - couts["P3"]["haut"]),
        "seuil_besoin_bras_a_pour_P3_sur_Rigaud_au_bas_usd": str(soldes_base["Rigaud"] - couts["P3"]["bas"]),
        "variante_recharge_Minuit_27_rapport": str(variante_minuit.quantize(D("0.001"))),
        # besoin du bras A au-delà duquel le repli (Luc : P3, P4, A ; Minuit : J3 ; Rigaud : rien)
        # donne un rapport minimal plus grand que la répartition avec P3 sur Rigaud
        "bascule_de_maximin_besoin_bras_a_usd": str(
            (soldes_base["Rigaud"] - couts["P3"]["haut"] * soldes_base["Luc"]
             / (couts["P3"]["haut"] + couts["P4"]["haut"] + couts["A"]["haut"])).quantize(D("0.01"))
        ),
        "repartitions_nommees": proposee,
        "recherche_exhaustive": resultats,
    }, ensure_ascii=False, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
