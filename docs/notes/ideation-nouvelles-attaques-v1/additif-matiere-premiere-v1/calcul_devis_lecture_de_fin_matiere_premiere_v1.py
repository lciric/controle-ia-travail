#!/usr/bin/env python3
"""Calcul du devis de la lecture de fin de la colonne « matière première » — v1.

Arithmétique seule, en décimal exact. Aucun appel, aucun réseau, aucune clé,
aucune lecture hors du fichier d'entrées donné en argument.

Usage :
    python3 calcul_devis_lecture_de_fin_matiere_premiere_v1.py ENTREES.json SORTIE.json

Le programme sort en code 1 si un objet de contrôle ne rend pas ce que le
fichier d'entrées annonce pour lui ; il n'écrit alors aucune sortie.
"""
import json
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP

MILLION = Decimal(1000000)
CENT = Decimal("0.01")
FIN = Decimal("0.000001")


def jetons_d_entree(octets, octets_par_jeton):
    """Jetons d'entrée, arrondis à l'entier supérieur."""
    return (Decimal(octets) / Decimal(octets_par_jeton)).to_integral_value(
        rounding=ROUND_CEILING
    )


def cout_d_un_appel(cas):
    entree = jetons_d_entree(cas["octets_par_requete"], cas["octets_par_jeton"])
    sortie = Decimal(cas["sortie_jetons"])
    usd_entree = entree * Decimal(cas["tarif_entree_usd_par_million"]) / MILLION
    usd_sortie = sortie * Decimal(cas["tarif_sortie_usd_par_million"]) / MILLION
    return entree, sortie, usd_entree, usd_sortie


def lire_un_cas(cas, bornes, appels_par_juge, juges, plafond):
    hors_borne = (
        int(cas["octets_par_requete"]) > int(bornes["requete_octets_au_plus"])
        or int(cas["sortie_jetons"]) > int(bornes["sortie_jetons_au_plus"])
    )
    entree, sortie, usd_entree, usd_sortie = cout_d_un_appel(cas)
    par_appel = usd_entree + usd_sortie
    par_juge = par_appel * appels_par_juge
    total = par_juge * juges
    tient = (not hors_borne) and total <= plafond
    return {
        "requete_dans_ses_bornes": not hors_borne,
        "jetons_d_entree_par_appel": str(int(entree)),
        "jetons_de_sortie_par_appel": str(int(sortie)),
        "usd_par_appel": str(par_appel.quantize(FIN, rounding=ROUND_HALF_UP)),
        "usd_par_juge": str(par_juge.quantize(FIN, rounding=ROUND_HALF_UP)),
        "usd_total": str(total.quantize(FIN, rounding=ROUND_HALF_UP)),
        "usd_total_au_centime_superieur": str(
            total.quantize(CENT, rounding=ROUND_CEILING)
        ),
        "tient_sous_le_plafond": tient,
    }


def main(argv):
    if len(argv) != 3:
        sys.stderr.write("usage : programme ENTREES.json SORTIE.json\n")
        return 2
    with open(argv[1], "r", encoding="utf-8") as f:
        e = json.load(f)

    juges = int(e["appels"]["juges"])
    appels_par_juge = int(e["appels"]["textes_reels_par_juge"]) + int(
        e["appels"]["appels_temoins_par_juge"]
    )
    plafond = Decimal(e["plafond_usd"])
    bornes = e["bornes"]

    cas = {}
    for nom in ("bas", "haut", "pire"):
        cas[nom] = lire_un_cas(e["cas"][nom], bornes, appels_par_juge, juges, plafond)

    controles = []
    echec = False
    for c in e["objets_de_controle"]:
        rendu = lire_un_cas(c["scenario"], bornes, appels_par_juge, juges, plafond)
        conforme = rendu["tient_sous_le_plafond"] == c["attendu_tient_sous_le_plafond"]
        if not conforme:
            echec = True
        controles.append(
            {
                "nom": c["nom"],
                "attendu_tient_sous_le_plafond": c["attendu_tient_sous_le_plafond"],
                "rendu": rendu,
                "conforme_a_l_attendu": conforme,
            }
        )
    if echec:
        sys.stderr.write("objet de contrôle non conforme : aucune sortie écrite\n")
        return 1

    # Grille au pire des tailles, par repère de tarif : aucun n'est le tarif relevé.
    grille = []
    for t in e["reperes_de_tarif_non_releves"]:
        sc = dict(e["cas"]["pire"])
        sc["tarif_entree_usd_par_million"] = t["entree"]
        sc["tarif_sortie_usd_par_million"] = t["sortie"]
        r = lire_un_cas(sc, bornes, appels_par_juge, juges, plafond)
        grille.append({"repere": t, "au_pire_des_tailles": r})

    # Repère mesuré : coût par appel des juges à la course v9 (une fiche par appel).
    reperes_mesures = []
    for m in e["repere_mesure_course_v9"]["juges"]:
        par_appel = Decimal(m["usd_sur_la_course"]) / Decimal(m["appels"])
        reperes_mesures.append(
            {
                "juge": m["juge"],
                "usd_par_appel_a_la_course_v9": str(
                    par_appel.quantize(FIN, rounding=ROUND_HALF_UP)
                ),
            }
        )

    pire_total = Decimal(cas["pire"]["usd_total"])
    sortie = {
        "piece": "calcul du devis de la lecture de fin de la colonne matière première, v1",
        "appels_par_juge": appels_par_juge,
        "appels_en_tout": appels_par_juge * juges,
        "plafond_usd": str(plafond),
        "plafond_par_juge_usd": str((plafond / juges).quantize(CENT)),
        "cas": cas,
        "pire_egal_au_plafond": pire_total == plafond,
        "objets_de_controle": controles,
        "grille_par_repere_de_tarif": grille,
        "reperes_mesures_qui_n_entrent_dans_aucun_total": reperes_mesures,
    }
    with open(argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
