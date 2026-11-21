# -*- coding: utf-8 -*-
"""Calcul de l'additif 1 au complément de valeurs v3 (espèce 3 sur la clé Minuit) — v1.

Arithmétique seule : aucune lecture de fichier, aucun appel, aucun aléa.
Toutes les sommes sont en centièmes de dollar (entiers), pour éviter tout
arrondi de virgule flottante. La sortie est un JSON imprimé sur la sortie
standard ; les montants y sont écrits en USD, à deux décimales, en chaînes.

Usage : python3 -B calcul_additif_1_complement_v3_v1.py > SORTIE.json
"""

import json
import sys

COMPLEMENT_V3 = (
    "prereg/ideation-nouvelles-attaques-v1/"
    "complement-valeurs-preenregistrement-court-v9-lot-1-v3.md "
    "(b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2)"
)
DEVIS_V11 = (
    "prereg/ideation-nouvelles-attaques-v1/devis-course-nouvelles-attaques-v11.md "
    "(205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570)"
)

# ---------------------------------------------------------------------------
# Entrées, en centièmes de dollar, chacune avec sa source.
# ---------------------------------------------------------------------------
ENTREES = {
    "minuit_reste": {
        "centimes": 16256,
        "source": COMPLEMENT_V3 + ", § 3, ligne 109 ; registres/go.md, GO-2026-11-20-16",
    },
    "lignes_a_part_temoins_plafond": {
        "centimes": 500,
        "source": COMPLEMENT_V3 + ", § 3, ligne 120 ; " + DEVIS_V11 + ", § 10.2, ligne 381",
    },
    "lignes_a_part_sonde_plafond": {
        "centimes": 100,
        "source": COMPLEMENT_V3 + ", § 3, ligne 120 ; " + DEVIS_V11 + ", § 10.2, ligne 382",
    },
    "minuit_part": {
        "centimes": 15656,
        "source": COMPLEMENT_V3 + ", § 3, ligne 105 ; registres/decisions.md, R-4306",
    },
    "juge_espece_3_bas": {
        "centimes": 2058,
        "source": COMPLEMENT_V3 + ", § 3, ligne 105 ; " + DEVIS_V11 + ", § 10.4, ligne 405",
    },
    "juge_espece_3_haut": {
        "centimes": 10505,
        "source": COMPLEMENT_V3 + ", § 3, ligne 105 ; " + DEVIS_V11 + ", § 10.4, ligne 405",
    },
    "proposeur_espece_3_bas": {
        "centimes": 2229,
        "source": COMPLEMENT_V3 + ", § 3, ligne 107 ; " + DEVIS_V11 + ", § 10.4, ligne 407",
    },
    "proposeur_espece_3_haut": {
        "centimes": 2661,
        "source": COMPLEMENT_V3 + ", § 3, ligne 107 ; " + DEVIS_V11 + ", § 10.4, ligne 407",
    },
    "pire_appel_proposeur": {
        "centimes": 605,
        "source": COMPLEMENT_V3 + ", § 2, ligne 83, et § 6, ligne 166",
    },
    "rigaud_solde_declare": {
        "centimes": 2500,
        "source": "registres/decisions.md, R-4342 ; registres/go.md, GO-2026-11-21-02",
    },
    "rigaud_reserve_bras_a": {
        "centimes": 835,
        "source": "registres/go.md, GO-2026-11-20-22 ; " + COMPLEMENT_V3 + ", § 3, ligne 118",
    },
    "troisieme_relais_bas": {
        "centimes": 1425,
        "source": COMPLEMENT_V3 + ", § 5, ligne 156 ; " + DEVIS_V11 + ", § 10.3, ligne 397",
    },
    "troisieme_relais_haut": {
        "centimes": 1701,
        "source": COMPLEMENT_V3 + ", § 5, ligne 156 ; " + DEVIS_V11
        + ", § 10.3, ligne 397 ; registres/decisions.md, R-4342",
    },
    "luc_part": {
        "centimes": 12563,
        "source": COMPLEMENT_V3 + ", § 3, ligne 106",
    },
    "luc_haut": {
        "centimes": 12435,
        "source": COMPLEMENT_V3 + ", § 3, ligne 106 ; " + DEVIS_V11 + ", § 10.4, ligne 406",
    },
    "deuxieme_relais_part": {
        "centimes": 14039,
        "source": COMPLEMENT_V3 + ", § 4, ligne 138",
    },
    "plafond_total": {
        "centimes": 45600,
        "source": "registres/go.md, GO-2026-11-20-67 ; " + DEVIS_V11 + ", § 10.2, ligne 386",
    },
}

# Les rôles Claude des deux lignes à part, après l'additif : tous sur Minuit.
ROLES_CLAUDE_DES_LIGNES_A_PART = [
    {"ligne": "épreuve des témoins", "role": "l'aiguilleur (le portier)", "cle_v3": "Minuit", "cle_additif": "Minuit"},
    {"ligne": "épreuve des témoins", "role": "le juge de l'espèce 3", "cle_v3": "Minuit", "cle_additif": "Minuit"},
    {"ligne": "sonde de refus", "role": "le proposeur de l'espèce 3", "cle_v3": "Rigaud", "cle_additif": "Minuit"},
    {"ligne": "sonde de refus", "role": "le proposeur de l'espèce 4", "cle_v3": "Minuit", "cle_additif": "Minuit"},
]


def c(nom):
    return ENTREES[nom]["centimes"]


def usd(centimes):
    signe = "-" if centimes < 0 else ""
    valeur = abs(centimes)
    return "%s%d.%02d" % (signe, valeur // 100, valeur % 100)


def rapport_milliemes(numerateur, denominateur):
    """Rapport tronqué au millième, rendu en chaîne (jamais arrondi vers le haut)."""
    milliemes = (numerateur * 1000) // denominateur
    return "%d.%03d" % (milliemes // 1000, milliemes % 1000)


def main():
    controles = {}

    # --- Minuit -----------------------------------------------------------
    plafond_lignes = c("lignes_a_part_temoins_plafond") + c("lignes_a_part_sonde_plafond")
    part_recalculee = c("minuit_reste") - plafond_lignes
    controles["minuit_part_egale_reste_moins_plafond_des_lignes"] = part_recalculee == c("minuit_part")
    controles["minuit_part_bornee_par_le_reste"] = c("minuit_part") <= c("minuit_reste")

    bas_deux_roles = c("juge_espece_3_bas") + c("proposeur_espece_3_bas")
    haut_deux_roles = c("juge_espece_3_haut") + c("proposeur_espece_3_haut")
    marge_part = c("minuit_part") - haut_deux_roles
    marge_v3 = c("minuit_part") - c("juge_espece_3_haut")
    controles["minuit_part_couvre_le_haut_des_deux_roles"] = marge_part >= 0

    reste_apres_lignes_au_plafond = c("minuit_reste") - plafond_lignes
    controles["minuit_reste_apres_lignes_au_moins_egal_a_la_part"] = (
        reste_apres_lignes_au_plafond >= c("minuit_part")
    )
    surplus_apres_lignes = reste_apres_lignes_au_plafond - haut_deux_roles
    reste_minimal_pour_le_haut = haut_deux_roles + plafond_lignes

    roles_sur_minuit = [r for r in ROLES_CLAUDE_DES_LIGNES_A_PART if r["cle_additif"] == "Minuit"]
    controles["lignes_a_part_tous_les_roles_claude_sur_minuit"] = (
        len(roles_sur_minuit) == len(ROLES_CLAUDE_DES_LIGNES_A_PART)
    )
    lignes_changees = [r for r in ROLES_CLAUDE_DES_LIGNES_A_PART if r["cle_v3"] != r["cle_additif"]]
    controles["lignes_a_part_une_seule_ligne_changee"] = len(lignes_changees) == 1

    # --- Rigaud -----------------------------------------------------------
    ancienne_part_rigaud = c("rigaud_solde_declare") - c("rigaud_reserve_bras_a")
    manque_ancienne_part = c("proposeur_espece_3_haut") - ancienne_part_rigaud
    controles["rigaud_ancienne_part_sous_le_haut"] = ancienne_part_rigaud < c("proposeur_espece_3_haut")
    controles["rigaud_reserve_couverte_par_le_solde_declare"] = (
        c("rigaud_solde_declare") >= c("rigaud_reserve_bras_a")
    )
    solde_minimal_v3 = c("proposeur_espece_3_haut") + c("rigaud_reserve_bras_a")

    # --- Troisième relais -------------------------------------------------
    part_troisieme = c("troisieme_relais_haut")
    controles["troisieme_relais_part_egale_son_haut"] = part_troisieme == c("troisieme_relais_haut")

    # --- Parts de la course, après l'additif ------------------------------
    somme_parts = c("minuit_part") + c("luc_part") + c("deuxieme_relais_part") + part_troisieme
    haut_claude = haut_deux_roles + c("luc_haut")

    sortie = {
        "piece": "calcul de l'additif 1 au complément de valeurs v3 — espèce 3 sur la clé Minuit — v1",
        "unite": "USD, deux décimales, en chaînes ; calcul en centièmes entiers",
        "entrees": {
            nom: {"usd": usd(v["centimes"]), "source": v["source"]} for nom, v in sorted(ENTREES.items())
        },
        "minuit": {
            "reste_usd": usd(c("minuit_reste")),
            "plafond_des_deux_lignes_a_part_usd": usd(plafond_lignes),
            "part_usd": usd(c("minuit_part")),
            "part_recalculee_reste_moins_plafond_usd": usd(part_recalculee),
            "bas_des_deux_roles_usd": usd(bas_deux_roles),
            "haut_des_deux_roles_usd": usd(haut_deux_roles),
            "marge_part_moins_haut_des_deux_roles_usd": usd(marge_part),
            "marge_au_complement_v3_un_seul_role_usd": usd(marge_v3),
            "baisse_de_la_marge_usd": usd(marge_v3 - marge_part),
            "rapport_part_sur_haut_des_deux_roles_tronque": rapport_milliemes(c("minuit_part"), haut_deux_roles),
            "reste_apres_les_lignes_a_part_au_plafond_usd": usd(reste_apres_lignes_au_plafond),
            "surplus_apres_les_lignes_a_part_et_le_haut_usd": usd(surplus_apres_lignes),
            "reste_minimal_pour_tenir_haut_et_lignes_usd": usd(reste_minimal_pour_le_haut),
            "marge_en_pires_appels_de_proposeur_entiers": marge_part // c("pire_appel_proposeur"),
        },
        "lignes_a_part": {
            "roles_claude": ROLES_CLAUDE_DES_LIGNES_A_PART,
            "nombre_de_roles_claude_sur_minuit": len(roles_sur_minuit),
            "lignes_changees": lignes_changees,
            "plafond_retranche_de_la_part_de_minuit_usd": usd(plafond_lignes),
        },
        "rigaud": {
            "solde_declare_usd": usd(c("rigaud_solde_declare")),
            "reserve_bras_a_usd": usd(c("rigaud_reserve_bras_a")),
            "solde_declare_moins_reserve_usd": usd(ancienne_part_rigaud),
            "manque_de_l_ancienne_part_au_haut_de_l_espece_3_usd": usd(manque_ancienne_part),
            "solde_minimal_qu_exigeait_le_complement_v3_usd": usd(solde_minimal_v3),
        },
        "troisieme_relais": {
            "bas_usd": usd(c("troisieme_relais_bas")),
            "haut_usd": usd(c("troisieme_relais_haut")),
            "part_usd": usd(part_troisieme),
        },
        "ensemble": {
            "somme_des_parts_de_la_course_usd": usd(somme_parts),
            "plafond_total_usd": usd(c("plafond_total")),
            "haut_des_roles_claude_somme_des_lignes_usd": usd(haut_claude),
        },
        "controles": controles,
        "tous_les_controles_tenus": all(controles.values()),
    }

    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0 if sortie["tous_les_controles_tenus"] else 1


if __name__ == "__main__":
    sys.exit(main())
