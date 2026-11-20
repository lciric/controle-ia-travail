#!/usr/bin/env python3
"""Calcul du devis de la course « nouvelles attaques », trois generations - v3.

La v3 part du programme v2 (cefe9783...) et ajoute la sixieme espece
(GO-2026-11-20-33) : une composition « S » a six especes, toutes
proposeuses ; l'aiguilleur et les deux juges inchanges ; la cle propre de
l'espece 6 ; les couts par role, par espece et par cle ; la repartition des
roles Claude sur les trois cles (GO-2026-11-20-22) relue a six especes.
Les compositions A, B et C de la v2 sont rejouees sans changement : elles
servent de controle (champ « controle_v2 »).

L'espece 6 n'a aucun cout mesure dans l'organisme a cette composition. Ses
trois cas sont des regles du redacteur, ecrites ici :
  bas   = la moyenne des cinq couts reels de proposeur de la course v9 ;
  haut  = le cout reel le plus haut des cinq, fois le facteur du haut de la
          proposition ;
  pire  = onze appels au pire d'un appel de proposeur (6,05 USD), comme
          pour le troisieme relais.

Processeur seul : aucun appel, aucun reseau, aucune lecture de fichier.
Toutes les constantes sont recopiees de pieces du depot, citees avec leur
chemin et leur empreinte dans le devis (section « Sources »). Les especes
sont designees par un numero ; aucun nom de modele n'est ecrit.

Usage : python3 -B calcul_devis_course_nouvelles_attaques_v3.py SORTIE.json
La sortie ne porte ni date ni chemin : deux lancements rendent le meme
fichier a l'octet.
"""
import itertools
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING

D = Decimal

# --- Constantes de la v2, inchangees (cle de source reprise dans le devis) ---

# S1 : devis de l'heritage v5, section 1 (couts reels de la course v9, par role)
V9_PROPOSEURS_USD = [D("4.17"), D("4.75"), D("7.43"), D("17.58"), D("24.72")]
V9_APPELS_PAR_ESPECE = 11
V9_AIGUILLEUR_USD = D("4.59")
V9_AIGUILLEUR_APPELS = 96
V9_JUGES_USD = [D("6.86"), D("2.41")]   # juge de l'espece 3, juge de l'espece 1
V9_JUGES_APPELS = [94, 94]
V9_COURSE_USD = D("72.50")
# S1 bis : devis de l'heritage v5, section 2 (tentatives attendues)
V9_FICHES = {"A": 94, "B": 56, "C": 38}
# S2 : registre des depenses sur main, ligne 536
V9_COURSE_EXACT_USD = D("72.502472")
V9_PART_CLE_RELAIS_1_USD = D("36.457056")
# S3 : devis v2i de la course d'auto-conception, sections 1, 2, 3 et 4
V2I_ESTIMATION = {"proposition": D("44.64"), "aiguillage": D("3.41"), "juges": D("7.89"), "course": D("55.94")}
V2I_HAUT = {"proposition": D("70.03"), "aiguillage": D("20.46"), "juges": D("47.32"), "course": D("137.81")}
V2I_PLAFOND_ARRET_USD = D("150")
V2I_ECART_PLAFOND_DUR_PROPOSITION = D("10")   # 150 -> 140
V2I_ECART_SEUIL_AIGUILLAGE = D("15")          # 150 -> 135
V2I_ECART_SEUIL_JUGES = D("30")               # 150 -> 120
V2I_PIRE_PAR_APPEL_PROPOSEUR_USD = D("6.05")
V2I_EPREUVE_TEMOINS = {"estimation": D("1.18"), "plafond": D("5")}
DEPENSE_VERIFICATION_CLE_RELAIS_1_USD = D("0.000108")  # S2, ligne 528
DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD = D("0.980399")  # S2, ligne 532
V2I_CREDIT_DECLARE_RELAIS_1_USD = D("200")
V2I_PART_AU_PIRE_RELAIS_3_PAR_GENERATION_USD = D("66.55")
# S4 : devis de la course d'ideation sur la question v2 du pilier attaque
PILIER_SONDE_TROIS_MODELES_USD = D("0.005")
PILIER_REEL_COURSE_UNE_GENERATION_USD = D("8.42")
PILIER_PLAFOND_USD = D("20")

# --- Parametres de la v2, inchanges ----------------------------------------
GENERATIONS = 3
MARGE_SUR_LE_HAUT = D("1.05")
PAS_ARRONDI_PLAFOND = D("5")
PLAFOND_SONDE_REFUS_USD = D("1")
COMPOSITIONS = {"A": [0, 1, 2, 3, 4], "B": [0, 1, 2], "C": [0, 1]}
PLAFOND_RETENU_PAR_PRECEDENT = {"A": V2I_PLAFOND_ARRET_USD}

# --- Constantes neuves de la v3 --------------------------------------------
# S7 : preenregistrement court v3 (2ea5ad53...), section « Seuil » ;
#      GO-2026-11-20-16 et -22 : soldes des trois cles Claude et reserve X
SOLDE_LUC_DECLARE_USD = D("214")
SOLDE_RIGAUD_CALCULE_AVANT_RECHARGE_USD = D("47")
X_RESERVE_BRAS_A_SUR_RIGAUD_USD = D("8.35")
# S8 : mandat du redacteur (GO-2026-11-20-33) : plafond de la sonde de refus
#      de l'espece 6
PLAFOND_SONDE_REFUS_ESPECE_6_USD = D("0.01")
# S9 : registre des decisions sur main, R-813 et R-1780 : tarif de sortie de
#      l'espece 6, en USD par million de jetons ; repere seulement, non relu
#      ce jour sur la page du fournisseur ; il n'entre dans aucun total
REPERE_TARIF_SORTIE_ESPECE_6_USD_PAR_MILLION = D("10")

# Roles Claude du premier relais du devis, et repartition retenue (GO-22)
REPARTITION_RETENUE = {
    "juge_espece_3": "Minuit",
    "aiguilleur": "Luc",
    "proposeur_espece_4": "Luc",
    "proposeur_espece_3": "Rigaud",
}
CLES_CLAUDE = ["Minuit", "Luc", "Rigaud"]


def c2(x):
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def c4(x):
    return x.quantize(D("0.0001"), rounding=ROUND_HALF_UP)


def plafond_superieur(x, pas):
    return (x / pas).to_integral_value(rounding=ROUND_CEILING) * pas


def texte(x):
    return format(x, "f")


def facteurs_du_haut():
    prop_v9 = sum(V9_PROPOSEURS_USD)
    juges_v9 = sum(V9_JUGES_USD)
    return {
        "proposition": V2I_HAUT["proposition"] / prop_v9,
        "aiguillage": V2I_HAUT["aiguillage"] / V9_AIGUILLEUR_USD,
        "juges": V2I_HAUT["juges"] / juges_v9,
    }


def seuils(plafond_gen, haut):
    seuil_dur_prop = plafond_gen - V2I_ECART_PLAFOND_DUR_PROPOSITION
    seuil_aig = plafond_gen - V2I_ECART_SEUIL_AIGUILLAGE
    seuil_juges = plafond_gen - V2I_ECART_SEUIL_JUGES
    return {
        "plafond_dur_proposition": texte(seuil_dur_prop),
        "aiguillage_lance_si_cumul_au_plus": texte(seuil_aig),
        "juges_lances_si_cumul_au_plus": texte(seuil_juges),
        "au_haut_proposition_sous_plafond_dur": haut["proposition"] <= seuil_dur_prop,
        "au_haut_aiguillage_lance": haut["proposition"] <= seuil_aig,
        "au_haut_juges_lances": haut["proposition"] + haut["aiguillage"] <= seuil_juges,
        "au_haut_course_sous_le_plafond": sum(haut.values()) <= plafond_gen,
    }


def controle_v2():
    """Les compositions A, B et C, par les formules de la v2, sans changement."""
    prop_v9 = sum(V9_PROPOSEURS_USD)
    juges_v9 = sum(V9_JUGES_USD)
    f = facteurs_du_haut()
    res = {}
    for nom, especes in COMPOSITIONS.items():
        appels = V9_APPELS_PAR_ESPECE * len(especes)
        part = D(appels) / D(V9_APPELS_PAR_ESPECE * len(V9_PROPOSEURS_USD))
        bas = {
            "proposition": sum(V9_PROPOSEURS_USD[i] for i in especes),
            "aiguillage": V9_AIGUILLEUR_USD * part,
            "juges": juges_v9 * part,
        }
        haut = {k: bas[k] * f[k] for k in bas}
        bas_gen = sum(bas.values())
        haut_gen = sum(haut.values())
        regle_marge = plafond_superieur(haut_gen * MARGE_SUR_LE_HAUT, PAS_ARRONDI_PLAFOND)
        regle_juges = plafond_superieur(
            haut["proposition"] + haut["aiguillage"] + V2I_ECART_SEUIL_JUGES, PAS_ARRONDI_PLAFOND
        )
        plafond_gen = PLAFOND_RETENU_PAR_PRECEDENT.get(nom, max(regle_marge, regle_juges))
        ligne_course = plafond_gen * GENERATIONS
        sonde_estimee = PILIER_SONDE_TROIS_MODELES_USD / 3 * len(especes)
        res[nom] = {
            "especes": [i + 1 for i in especes],
            "appels_de_proposeur_par_generation": appels,
            "bas_par_generation": texte(c2(bas_gen)),
            "haut_par_generation": texte(c2(haut_gen)),
            "plafond_d_arret_par_generation": texte(plafond_gen),
            "course_bas": texte(c2(bas_gen * GENERATIONS)),
            "course_haut": texte(c2(haut_gen * GENERATIONS)),
            "ligne_de_course": texte(ligne_course),
            "total_bas": texte(c2(bas_gen * GENERATIONS + V2I_EPREUVE_TEMOINS["estimation"] + sonde_estimee)),
            "total_haut": texte(c2(haut_gen * GENERATIONS + V2I_EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD)),
            "plafond_total": texte(ligne_course + V2I_EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD),
            "fiches_attendues_sur_la_course": V9_FICHES[nom] * GENERATIONS,
        }
    return res


def six_especes():
    f = facteurs_du_haut()
    n5 = len(V9_PROPOSEURS_USD)
    espece_6_bas = sum(V9_PROPOSEURS_USD) / n5
    espece_6_haut = max(V9_PROPOSEURS_USD) * f["proposition"]
    espece_6_pire = D(V9_APPELS_PAR_ESPECE) * V2I_PIRE_PAR_APPEL_PROPOSEUR_USD
    appels = V9_APPELS_PAR_ESPECE * (n5 + 1)
    part = D(appels) / D(V9_APPELS_PAR_ESPECE * n5)

    # --- par role, par generation ---
    roles_bas = {}
    roles_haut = {}
    for i, v in enumerate(V9_PROPOSEURS_USD):
        roles_bas["proposeur_espece_%d" % (i + 1)] = v
        roles_haut["proposeur_espece_%d" % (i + 1)] = v * f["proposition"]
    roles_bas["proposeur_espece_6"] = espece_6_bas
    roles_haut["proposeur_espece_6"] = espece_6_haut
    roles_bas["aiguilleur"] = V9_AIGUILLEUR_USD * part
    roles_haut["aiguilleur"] = V9_AIGUILLEUR_USD * part * f["aiguillage"]
    roles_bas["juge_espece_3"] = V9_JUGES_USD[0] * part
    roles_haut["juge_espece_3"] = V9_JUGES_USD[0] * part * f["juges"]
    roles_bas["juge_espece_1"] = V9_JUGES_USD[1] * part
    roles_haut["juge_espece_1"] = V9_JUGES_USD[1] * part * f["juges"]

    def somme(d, prefixe):
        return sum(v for k, v in d.items() if k.startswith(prefixe))

    bas = {"proposition": somme(roles_bas, "proposeur"), "aiguillage": roles_bas["aiguilleur"],
           "juges": somme(roles_bas, "juge")}
    haut = {"proposition": somme(roles_haut, "proposeur"), "aiguillage": roles_haut["aiguilleur"],
            "juges": somme(roles_haut, "juge")}
    bas_gen = sum(bas.values())
    haut_gen = sum(haut.values())
    regle_marge = plafond_superieur(haut_gen * MARGE_SUR_LE_HAUT, PAS_ARRONDI_PLAFOND)
    regle_juges = plafond_superieur(
        haut["proposition"] + haut["aiguillage"] + V2I_ECART_SEUIL_JUGES, PAS_ARRONDI_PLAFOND
    )
    plafond_gen = max(regle_marge, regle_juges)
    ligne_course = plafond_gen * GENERATIONS
    pire_appels_prop = D(appels) * V2I_PIRE_PAR_APPEL_PROPOSEUR_USD
    sonde_cinq_estimee = PILIER_SONDE_TROIS_MODELES_USD / 3 * n5
    sonde_six_estimee = PILIER_SONDE_TROIS_MODELES_USD / 3
    lignes_a_part_plafond = V2I_EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD + PLAFOND_SONDE_REFUS_ESPECE_6_USD
    total_bas = bas_gen * GENERATIONS + V2I_EPREUVE_TEMOINS["estimation"] + sonde_cinq_estimee + sonde_six_estimee
    total_haut = haut_gen * GENERATIONS + lignes_a_part_plafond
    total_plafond = ligne_course + lignes_a_part_plafond
    fiches_gen = D(V9_FICHES["A"]) * part

    pire_proposeur = D(V9_APPELS_PAR_ESPECE) * V2I_PIRE_PAR_APPEL_PROPOSEUR_USD * GENERATIONS
    par_role_course = {}
    for k in sorted(roles_bas):
        par_role_course[k] = {
            "bas": texte(c2(roles_bas[k] * GENERATIONS)),
            "haut": texte(c2(roles_haut[k] * GENERATIONS)),
            "pire": texte(c2(pire_proposeur)) if k.startswith("proposeur") else texte(ligne_course),
        }

    # --- par espece (une espece additionne ses roles ; l'aiguilleur a part) ---
    par_espece = {}
    for n in range(1, 7):
        cles = ["proposeur_espece_%d" % n] + (["juge_espece_%d" % n] if n in (1, 3) else [])
        par_espece["espece_%d" % n] = {
            "roles": cles,
            "bas": texte(c2(sum(roles_bas[k] for k in cles) * GENERATIONS)),
            "haut": texte(c2(sum(roles_haut[k] for k in cles) * GENERATIONS)),
        }
    par_espece["aiguilleur"] = {
        "roles": ["aiguilleur"],
        "bas": texte(c2(roles_bas["aiguilleur"] * GENERATIONS)),
        "haut": texte(c2(roles_haut["aiguilleur"] * GENERATIONS)),
    }

    # --- par cle ---
    solde_minuit = (V2I_CREDIT_DECLARE_RELAIS_1_USD - DEPENSE_VERIFICATION_CLE_RELAIS_1_USD
                    - DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD - V9_PART_CLE_RELAIS_1_USD)
    parts_claude = {
        "Minuit": solde_minuit,
        "Luc": SOLDE_LUC_DECLARE_USD,
        "Rigaud": SOLDE_RIGAUD_CALCULE_AVANT_RECHARGE_USD - X_RESERVE_BRAS_A_SUR_RIGAUD_USD,
    }
    cles = {
        "Minuit": ["juge_espece_3"],
        "Luc": ["aiguilleur", "proposeur_espece_4"],
        "Rigaud": ["proposeur_espece_3"],
        "cle_du_deuxieme_relais": ["juge_espece_1", "proposeur_espece_1", "proposeur_espece_5"],
        "cle_du_troisieme_relais": ["proposeur_espece_2"],
        "cle_de_l_espece_6": ["proposeur_espece_6"],
    }
    pire_cle = {
        "cle_du_deuxieme_relais": ligne_course,
        "cle_du_troisieme_relais": pire_proposeur,
        "cle_de_l_espece_6": pire_proposeur,
    }
    par_cle = {}
    for nom, rs in cles.items():
        b = sum(roles_bas[k] for k in rs) * GENERATIONS
        h = sum(roles_haut[k] for k in rs) * GENERATIONS
        e = {"roles": rs, "bas": texte(c2(b)), "haut": texte(c2(h))}
        if nom in parts_claude:
            e["part_bornee_avant_recharge_de_rigaud"] = texte(c2(parts_claude[nom]))
            e["rapport_part_sur_haut"] = texte(c4(parts_claude[nom] / h))
            e["tient_le_cas_haut"] = parts_claude[nom] >= h
        else:
            e["part_au_pire"] = texte(c2(pire_cle[nom]))
            e["rapport_part_au_pire_sur_haut"] = texte(c4(pire_cle[nom] / h))
        par_cle[nom] = e

    # --- roles Claude du premier relais : six especes, et controle a cinq ---
    roles_claude = sorted(REPARTITION_RETENUE)
    claude_six = {k: {"bas": roles_bas[k] * GENERATIONS, "haut": roles_haut[k] * GENERATIONS} for k in roles_claude}
    cinq_bas = {
        "proposeur_espece_3": V9_PROPOSEURS_USD[2], "proposeur_espece_4": V9_PROPOSEURS_USD[3],
        "aiguilleur": V9_AIGUILLEUR_USD, "juge_espece_3": V9_JUGES_USD[0],
    }
    cinq_f = {"proposeur_espece_3": f["proposition"], "proposeur_espece_4": f["proposition"],
              "aiguilleur": f["aiguillage"], "juge_espece_3": f["juges"]}
    claude_cinq = {k: {"bas": cinq_bas[k] * GENERATIONS, "haut": cinq_bas[k] * cinq_f[k] * GENERATIONS}
                   for k in roles_claude}
    borne_trois_cles = sum(parts_claude.values())
    somme_haut_six = sum(v["haut"] for v in claude_six.values())
    somme_haut_cinq = sum(v["haut"] for v in claude_cinq.values())

    # --- la regle de choix de la v3, rejouee a six especes, parts d'avant recharge ---
    admissibles = []
    retenue = None
    for affect in itertools.product(CLES_CLAUDE, repeat=len(roles_claude)):
        charge = {c: D("0") for c in CLES_CLAUDE}
        for r, c in zip(roles_claude, affect):
            charge[c] += claude_six[r]["haut"]
        if any(charge[c] > parts_claude[c] for c in CLES_CLAUDE):
            continue
        rapports = [parts_claude[c] / charge[c] for c in CLES_CLAUDE if charge[c] > 0]
        plus_petit = min(rapports)
        d = dict(zip(roles_claude, affect))
        if d == REPARTITION_RETENUE:
            retenue = plus_petit
        admissibles.append((plus_petit, d))
    meilleur_rapport = max(a[0] for a in admissibles)
    ex_aequo = [a[1] for a in admissibles if a[0] == meilleur_rapport]

    return {
        "especes": [1, 2, 3, 4, 5, 6],
        "appels_de_proposeur_par_generation": appels,
        "facteur_de_prorata_aiguilleur_et_juges": texte(c4(part)),
        "espece_6_regles_du_redacteur": {
            "bas_par_generation_moyenne_des_cinq": texte(c2(espece_6_bas)),
            "bas_par_appel": texte(c4(espece_6_bas / V9_APPELS_PAR_ESPECE)),
            "haut_par_generation_le_plus_cher_des_cinq_fois_le_facteur": texte(c2(espece_6_haut)),
            "pire_par_generation_onze_appels_au_pire": texte(c2(espece_6_pire)),
            "course_bas": texte(c2(espece_6_bas * GENERATIONS)),
            "course_haut": texte(c2(espece_6_haut * GENERATIONS)),
            "course_pire_part_au_pire_de_sa_cle": texte(c2(espece_6_pire * GENERATIONS)),
            "mesure": False,
        },
        "par_generation_usd": {
            "bas": {k: texte(c2(v)) for k, v in bas.items()},
            "bas_total": texte(c2(bas_gen)),
            "haut": {k: texte(c2(v)) for k, v in haut.items()},
            "haut_total": texte(c2(haut_gen)),
            "plafond_regle_marge": texte(regle_marge),
            "plafond_regle_juges_lances_au_haut": texte(regle_juges),
            "plafond_selon_la_regle": texte(plafond_gen),
            "marge_plafond_sur_bas": texte(c4(plafond_gen / bas_gen)),
        },
        "seuils_internes_par_generation_usd": dict(
            seuils(plafond_gen, haut),
            pire_des_appels_de_proposeur=texte(c2(pire_appels_prop)),
            proposition_coupee_au_pire_des_appels=pire_appels_prop > plafond_gen - V2I_ECART_PLAFOND_DUR_PROPOSITION,
        ),
        "course_usd": {
            "bas": texte(c2(bas_gen * GENERATIONS)),
            "haut": texte(c2(haut_gen * GENERATIONS)),
            "pire_ligne_de_course": texte(ligne_course),
        },
        "lignes_a_part_usd": {
            "epreuve_des_temoins_estimation": texte(V2I_EPREUVE_TEMOINS["estimation"]),
            "epreuve_des_temoins_plafond": texte(V2I_EPREUVE_TEMOINS["plafond"]),
            "sonde_de_refus_cinq_especes_estimation": texte(c4(sonde_cinq_estimee)),
            "sonde_de_refus_cinq_especes_plafond": texte(PLAFOND_SONDE_REFUS_USD),
            "sonde_de_refus_espece_6_estimation": texte(c4(sonde_six_estimee)),
            "sonde_de_refus_espece_6_plafond": texte(PLAFOND_SONDE_REFUS_ESPECE_6_USD),
            "somme_des_plafonds": texte(lignes_a_part_plafond),
        },
        "total_usd": {
            "bas": texte(c2(total_bas)),
            "haut": texte(c2(total_haut)),
            "plafond_total": texte(total_plafond),
        },
        "ecarts_a_la_composition_A_usd": {
            "course_bas": texte(c2(bas_gen * GENERATIONS) - D(controle_v2()["A"]["course_bas"])),
            "course_haut": texte(c2(haut_gen * GENERATIONS) - D(controle_v2()["A"]["course_haut"])),
            "ligne_de_course": texte(ligne_course - D(controle_v2()["A"]["ligne_de_course"])),
            "plafond_total": texte(total_plafond - D(controle_v2()["A"]["plafond_total"])),
        },
        "fiches_attendues": {
            "par_generation_a_la_proportion_de_la_v9": texte(c2(fiches_gen)),
            "sur_la_course": texte(c2(fiches_gen * GENERATIONS)),
        },
        "plafonds_par_relais_usd": {
            "relais_1_aiguilleur_juge_3_proposeurs_3_et_4": texte(ligne_course),
            "relais_2_juge_1_proposeurs_1_et_5": texte(ligne_course),
            "relais_3_proposeur_2_seul": texte(c2(pire_proposeur)),
            "relais_4_proposeur_6_seul": texte(c2(pire_proposeur)),
        },
        "par_role_sur_la_course_usd": par_role_course,
        "par_espece_sur_la_course_usd": par_espece,
        "par_cle_sur_la_course_usd": par_cle,
        "cles_claude": {
            "roles_a_six_especes": {k: {"bas": texte(c2(v["bas"])), "haut": texte(c2(v["haut"]))}
                                    for k, v in claude_six.items()},
            "controle_roles_a_cinq_especes": {k: {"bas": texte(c2(v["bas"])), "haut": texte(c2(v["haut"]))}
                                              for k, v in claude_cinq.items()},
            "somme_bas_a_six": texte(c2(sum(v["bas"] for v in claude_six.values()))),
            "somme_haut_a_six": texte(c2(somme_haut_six)),
            "controle_somme_bas_a_cinq": texte(c2(sum(v["bas"] for v in claude_cinq.values()))),
            "controle_somme_haut_a_cinq": texte(c2(somme_haut_cinq)),
            "x_reserve_bras_a_sur_rigaud": texte(X_RESERVE_BRAS_A_SUR_RIGAUD_USD),
            "borne_des_trois_cles_avant_recharge_de_rigaud": texte(c2(borne_trois_cles)),
            "borne_sur_somme_haut_a_six": texte(c4(borne_trois_cles / somme_haut_six)),
            "controle_borne_sur_somme_haut_a_cinq": texte(c4(borne_trois_cles / somme_haut_cinq)),
            "manque_au_pire_du_premier_relais": texte(c2(ligne_course - borne_trois_cles)),
            "controle_manque_au_pire_a_cinq": texte(c2(V2I_PLAFOND_ARRET_USD * GENERATIONS - borne_trois_cles)),
            "repartition_retenue_plus_petit_rapport": texte(c4(retenue)) if retenue is not None else None,
            "regle_de_choix_meilleur_plus_petit_rapport": texte(c4(meilleur_rapport)),
            "regle_de_choix_repartitions_admissibles": len(admissibles),
            "regle_de_choix_repartitions_ex_aequo_au_meilleur_rapport": ex_aequo,
            "la_repartition_retenue_atteint_le_meilleur_rapport": retenue == meilleur_rapport,
            "part_de_rigaud_minimale_pour_tenir_le_haut_de_son_role": texte(c2(claude_six["proposeur_espece_3"]["haut"])),
        },
        "variante_plafond_de_150_garde": dict(
            seuils(V2I_PLAFOND_ARRET_USD, haut),
            ligne_de_course=texte(V2I_PLAFOND_ARRET_USD * GENERATIONS),
            plafond_total=texte(V2I_PLAFOND_ARRET_USD * GENERATIONS + lignes_a_part_plafond),
            marge_plafond_sur_bas=texte(c4(V2I_PLAFOND_ARRET_USD / bas_gen)),
            cumul_au_haut_avant_les_juges=texte(c2(haut["proposition"] + haut["aiguillage"])),
        ),
        "reperes": {
            "pire_par_appel_de_proposeur_usd": texte(V2I_PIRE_PAR_APPEL_PROPOSEUR_USD),
            "tarif_de_sortie_espece_6_usd_par_million_non_relu_ce_jour": texte(REPERE_TARIF_SORTIE_ESPECE_6_USD_PAR_MILLION),
            "jetons_de_sortie_que_vaut_le_pire_par_appel_a_ce_tarif": texte(
                (V2I_PIRE_PAR_APPEL_PROPOSEUR_USD / REPERE_TARIF_SORTIE_ESPECE_6_USD_PAR_MILLION * D("1000000")).quantize(D("1"))
            ),
        },
    }


def calculer():
    return {
        "piece": "calcul du devis de la course nouvelles attaques, v3",
        "generations": GENERATIONS,
        "facteurs_du_haut_par_role": {k: texte(c4(v)) for k, v in facteurs_du_haut().items()},
        "controle_v2": controle_v2(),
        "six_especes": six_especes(),
    }


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : calcul_devis_course_nouvelles_attaques_v3.py SORTIE.json\n")
        return 2
    sortie = calculer()
    with open(argv[1], "x", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
