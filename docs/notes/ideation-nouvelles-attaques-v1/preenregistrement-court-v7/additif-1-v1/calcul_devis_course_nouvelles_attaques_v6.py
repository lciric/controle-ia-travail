#!/usr/bin/env python3
"""Calcul du devis de la course « nouvelles attaques », trois generations - v6.

La v6 sert le devis v7 : l'espece 6 quitte la course (GO-2026-11-20-60), qui
revient a cinq especes. Elle part du calcul v5 (cdec1d2d...) et en garde les
constantes et les formules ; elle est recrite en fractions exactes
(bibliotheque standard), chaque montant etant arrondi une seule fois, au
centime, a la sortie.

Ce que la v6 rend : la composition a cinq especes (la composition « A » du
calcul v2, que les calculs v3 a v5 rejouaient sous le champ « controle_v2 ») ;
plafond d'une generation, seuils, ligne de course, lignes a part, totaux ;
couts par role, par espece, par relais et par cle ; les trois cles de la
lignee de la mere (Minuit, Luc, Rigaud) a cinq especes, avec la regle de choix
de la repartition rejouee ; tailles de la requete (inchangees) ; confrontation
aux restes nets ESTIMES du comptable (62c625ab..., une estimation, non un
releve).

Retraits par rapport au calcul v5, tous declares dans le champ
« retraits_par_rapport_au_calcul_v5 » de la sortie : l'espece 6 et ses trois
cas ; sa cle et le quatrieme relais ; sa sonde de refus et son plafond de
0,05 USD ; le prorata 1,2 de l'aiguilleur et des juges ; les reperes de tarif
de l'espece 6 ; la variante « plafond de 150 garde » (150 est de nouveau le
plafond) ; les compositions a trois et a deux especes (non retenues,
GO-2026-11-20-16).

Processeur seul : aucun appel, aucun reseau, aucune lecture de fichier. Les
especes sont designees par un numero ; aucun nom de modele n'est ecrit.

Usage : python3 -B calcul_devis_course_nouvelles_attaques_v6.py SORTIE.json
La sortie ne porte ni date ni chemin : deux lancements rendent le meme
fichier a l'octet.
"""
import itertools
import json
import sys
from fractions import Fraction as F

# --- Constantes reprises du calcul v5, inchangees ---------------------------
# S1 : devis de l'heritage v5 (couts reels de la course v9, par role)
V9_PROPOSEURS_USD = [F("4.17"), F("4.75"), F("7.43"), F("17.58"), F("24.72")]
V9_APPELS_PAR_ESPECE = 11
V9_AIGUILLEUR_USD = F("4.59")
V9_JUGES_USD = {"juge_espece_3": F("6.86"), "juge_espece_1": F("2.41")}
V9_FICHES_PAR_GENERATION = 94
# S2 : registre des depenses (cle du premier relais)
V9_PART_CLE_RELAIS_1_USD = F("36.457056")
DEPENSE_VERIFICATION_CLE_RELAIS_1_USD = F("0.000108")
DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD = F("0.980399")
CREDIT_DECLARE_RELAIS_1_USD = F("200")
# S3 : devis v2i de la course d'auto-conception
V2I_HAUT = {"proposition": F("70.03"), "aiguillage": F("20.46"), "juges": F("47.32")}
PLAFOND_ARRET_PAR_GENERATION_USD = F("150")      # retenu par precedent (course v9)
ECART_PLAFOND_DUR_PROPOSITION = F("10")
ECART_SEUIL_AIGUILLAGE = F("15")
ECART_SEUIL_JUGES = F("30")
PIRE_PAR_APPEL_PROPOSEUR_USD = F("6.05")
EPREUVE_TEMOINS = {"estimation": F("1.18"), "plafond": F("5")}
# S4 : sonde de refus, estimation pour trois modeles
SONDE_TROIS_MODELES_USD = F("0.005")
PLAFOND_SONDE_REFUS_USD = F("1")
GENERATIONS = 3
MARGE_SUR_LE_HAUT = F("1.05")
PAS_ARRONDI_PLAFOND = F("5")
# S7 : soldes des trois cles de la lignee de la mere, reserve X
SOLDE_LUC_DECLARE_USD = F("214")
SOLDE_RIGAUD_CALCULE_AVANT_RECHARGE_USD = F("47")
X_RESERVE_BRAS_A_SUR_RIGAUD_USD = F("8.35")
REPARTITION_RETENUE = {
    "juge_espece_3": "Minuit",
    "aiguilleur": "Luc",
    "proposeur_espece_4": "Luc",
    "proposeur_espece_3": "Rigaud",
}
CLES_LIGNEE_MERE = ["Minuit", "Luc", "Rigaud"]
ROLES_PAR_CLE = {
    "Minuit": ["juge_espece_3"],
    "Luc": ["aiguilleur", "proposeur_espece_4"],
    "Rigaud": ["proposeur_espece_3"],
    "cle_du_deuxieme_relais": ["juge_espece_1", "proposeur_espece_1", "proposeur_espece_5"],
    "cle_du_troisieme_relais": ["proposeur_espece_2"],
}
# S11, S12 : tailles des pieces servies (wc -c), legende des axes
TAILLE_GABARIT_PARTIE_SERVIE_OCTETS = 2957
EMPLACEMENT_DE_CASE = "{{CASE}}"
AXE_SUPPOSITION = ["indépendance des traits", "stationnarité", "linéarité", "canal lu",
                   "calibration du seuil", "autre, à nommer"]
AXE_MENACE = ["sabotage diffus", "conscience d'évaluation", "collusion ou co-élévation entre copies",
              "délégation", "corruption d'un juge ou d'un moniteur"]
AXE_ETAGE = ["sonde ponctuelle", "moniteur séquentiel ou agrégé",
             "bases boîte blanche (cascade, dernier état)", "défense jointe"]
BORNE_IDENTIFIANT_OCTETS = 24
BORNE_LIGNE_DE_CASE_OCTETS = 256
SEPARATEUR_IDENTIFIANT = " : "
SEPARATEUR_VALEURS = " / "
TAILLE_SYNTHESE_SERVIE_OCTETS = 32260
# S13 : reste net comptable par cle, ESTIMATION, non un releve
RESTE_MINUIT_USD = F("162.562437")
RESTE_LUC_USD = F("213.999998")
RESTE_RIGAUD_LECTURE_REGISTRE_USD = F("47.495696")
RESTE_RIGAUD_LECTURE_CORRIGEE_USD = F("64.207482")
LOTS_EN_COURS_SUR_RIGAUD_AU_PLUS_USD = F("45")
CLE_RELAIS_3_BORNE_RAPPORTEE_USD = F("30")
CLE_RELAIS_3_DEPENSES_INSCRITES_USD = F("18.49368")
CLE_RELAIS_3_APPELS_COUPES_AU_PIRE_USD = F("2.6")
COLLISIONNEUR_PIRE_CLE_RELAIS_3_USD = F("15.63")


def arrondi(x, decimales=2):
    """Arrondi au plus proche, demi vers l'exterieur ; texte a « decimales » chiffres."""
    q = 10 ** decimales
    negatif = x < 0
    n = (abs(x) * q * 2 + 1) // 2
    n = int(n)
    t = "%d.%0*d" % (n // q, decimales, n % q)
    return "-" + t if negatif and n else t


def plafond_superieur(x, pas):
    k = x / pas
    entier = k.numerator // k.denominator
    if F(entier) < k:
        entier += 1
    return F(entier) * pas


def couts_par_role():
    """Cas bas et cas haut par role, par generation, sans arrondi."""
    f_prop = V2I_HAUT["proposition"] / sum(V9_PROPOSEURS_USD)
    f_aig = V2I_HAUT["aiguillage"] / V9_AIGUILLEUR_USD
    f_juges = V2I_HAUT["juges"] / sum(V9_JUGES_USD.values())
    bas, haut = {}, {}
    for i, v in enumerate(V9_PROPOSEURS_USD):
        bas["proposeur_espece_%d" % (i + 1)] = v
        haut["proposeur_espece_%d" % (i + 1)] = v * f_prop
    bas["aiguilleur"] = V9_AIGUILLEUR_USD
    haut["aiguilleur"] = V9_AIGUILLEUR_USD * f_aig
    for k, v in V9_JUGES_USD.items():
        bas[k] = v
        haut[k] = v * f_juges
    return bas, haut, {"proposition": f_prop, "aiguillage": f_aig, "juges": f_juges}


def somme(d, prefixe):
    return sum(v for k, v in d.items() if k.startswith(prefixe))


def cinq_especes():
    bas_r, haut_r, facteurs = couts_par_role()
    bas = {"proposition": somme(bas_r, "proposeur"), "aiguillage": bas_r["aiguilleur"], "juges": somme(bas_r, "juge")}
    haut = {"proposition": somme(haut_r, "proposeur"), "aiguillage": haut_r["aiguilleur"],
            "juges": somme(haut_r, "juge")}
    bas_gen, haut_gen = sum(bas.values()), sum(haut.values())
    regle_marge = plafond_superieur(haut_gen * MARGE_SUR_LE_HAUT, PAS_ARRONDI_PLAFOND)
    regle_juges = plafond_superieur(haut["proposition"] + haut["aiguillage"] + ECART_SEUIL_JUGES, PAS_ARRONDI_PLAFOND)
    plafond_gen = PLAFOND_ARRET_PAR_GENERATION_USD
    seuil_prop = plafond_gen - ECART_PLAFOND_DUR_PROPOSITION
    seuil_aig = plafond_gen - ECART_SEUIL_AIGUILLAGE
    seuil_juges = plafond_gen - ECART_SEUIL_JUGES
    ligne = plafond_gen * GENERATIONS
    appels = V9_APPELS_PAR_ESPECE * len(V9_PROPOSEURS_USD)
    sonde_estimee = SONDE_TROIS_MODELES_USD / 3 * len(V9_PROPOSEURS_USD)
    lignes_a_part = EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD
    pire_proposeur = V9_APPELS_PAR_ESPECE * PIRE_PAR_APPEL_PROPOSEUR_USD * GENERATIONS

    par_role = {}
    for k in sorted(bas_r):
        par_role[k] = {"bas": arrondi(bas_r[k] * GENERATIONS), "haut": arrondi(haut_r[k] * GENERATIONS),
                       "pire": arrondi(pire_proposeur) if k.startswith("proposeur") else arrondi(ligne)}
    par_espece = {}
    for n in range(1, 6):
        roles = ["proposeur_espece_%d" % n] + (["juge_espece_%d" % n] if n in (1, 3) else [])
        par_espece["espece_%d" % n] = {
            "roles": roles,
            "bas": arrondi(sum(bas_r[k] for k in roles) * GENERATIONS),
            "haut": arrondi(sum(haut_r[k] for k in roles) * GENERATIONS),
        }
    par_espece["aiguilleur"] = {"roles": ["aiguilleur"], "bas": arrondi(bas_r["aiguilleur"] * GENERATIONS),
                                "haut": arrondi(haut_r["aiguilleur"] * GENERATIONS)}
    par_relais = {
        "relais_1_aiguilleur_juge_3_proposeurs_3_et_4": {
            "bas": arrondi(sum(bas_r[k] for k in REPARTITION_RETENUE) * GENERATIONS),
            "haut": arrondi(sum(haut_r[k] for k in REPARTITION_RETENUE) * GENERATIONS),
            "part_au_pire": arrondi(ligne)},
        "relais_2_juge_1_proposeurs_1_et_5": {
            "bas": arrondi(sum(bas_r[k] for k in ROLES_PAR_CLE["cle_du_deuxieme_relais"]) * GENERATIONS),
            "haut": arrondi(sum(haut_r[k] for k in ROLES_PAR_CLE["cle_du_deuxieme_relais"]) * GENERATIONS),
            "part_au_pire": arrondi(ligne)},
        "relais_3_proposeur_2_seul": {
            "bas": arrondi(bas_r["proposeur_espece_2"] * GENERATIONS),
            "haut": arrondi(haut_r["proposeur_espece_2"] * GENERATIONS),
            "part_au_pire": arrondi(pire_proposeur)},
    }
    return {
        "especes": [1, 2, 3, 4, 5],
        "appels_de_proposeur_par_generation": appels,
        "facteurs_du_haut_par_role": {k: arrondi(v, 4) for k, v in facteurs.items()},
        "par_generation_usd": {
            "bas": {k: arrondi(v) for k, v in bas.items()},
            "bas_total": arrondi(bas_gen),
            "haut": {k: arrondi(v) for k, v in haut.items()},
            "haut_total": arrondi(haut_gen),
            "plafond_regle_marge": arrondi(regle_marge),
            "plafond_regle_juges_lances_au_haut": arrondi(regle_juges),
            "plafond_retenu_par_precedent_course_v9": arrondi(plafond_gen),
        },
        "seuils_par_generation_usd": {
            "plafond_dur_proposition": arrondi(seuil_prop),
            "aiguillage_lance_si_cumul_au_plus": arrondi(seuil_aig),
            "juges_lances_si_cumul_au_plus": arrondi(seuil_juges),
            "au_haut_proposition_sous_plafond_dur": haut["proposition"] <= seuil_prop,
            "au_haut_aiguillage_lance": haut["proposition"] <= seuil_aig,
            "au_haut_juges_lances": haut["proposition"] + haut["aiguillage"] <= seuil_juges,
            "au_haut_course_sous_le_plafond": haut_gen <= plafond_gen,
            "pire_des_appels_de_proposeur": arrondi(appels * PIRE_PAR_APPEL_PROPOSEUR_USD),
        },
        "course_usd": {"bas": arrondi(bas_gen * GENERATIONS), "haut": arrondi(haut_gen * GENERATIONS),
                       "ligne_de_course": arrondi(ligne)},
        "lignes_a_part_usd": {
            "epreuve_des_temoins_estimation": arrondi(EPREUVE_TEMOINS["estimation"]),
            "epreuve_des_temoins_plafond": arrondi(EPREUVE_TEMOINS["plafond"]),
            "sonde_de_refus_cinq_especes_estimation": arrondi(sonde_estimee, 4),
            "sonde_de_refus_cinq_especes_plafond": arrondi(PLAFOND_SONDE_REFUS_USD),
            "somme_des_plafonds": arrondi(lignes_a_part),
        },
        "total_usd": {
            "bas": arrondi(bas_gen * GENERATIONS + EPREUVE_TEMOINS["estimation"] + sonde_estimee),
            "haut": arrondi(haut_gen * GENERATIONS + lignes_a_part),
            "plafond_total": arrondi(ligne + lignes_a_part),
        },
        "ecarts_au_devis_v6_a_six_especes_usd": {
            "ligne_de_course": arrondi(ligne - F("570")),
            "plafond_total": arrondi(ligne + lignes_a_part - F("576.05")),
            "total_haut": arrondi(haut_gen * GENERATIONS + lignes_a_part - F("548.70")),
            "total_bas": arrondi(bas_gen * GENERATIONS + EPREUVE_TEMOINS["estimation"] + sonde_estimee - F("262.23")),
        },
        "fiches_attendues_sur_la_course": V9_FICHES_PAR_GENERATION * GENERATIONS,
        "par_role_sur_la_course_usd": par_role,
        "par_espece_sur_la_course_usd": par_espece,
        "par_relais_sur_la_course_usd": par_relais,
    }


def cles_lignee_mere():
    bas_r, haut_r, _ = couts_par_role()
    solde_minuit = (CREDIT_DECLARE_RELAIS_1_USD - DEPENSE_VERIFICATION_CLE_RELAIS_1_USD
                    - DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD - V9_PART_CLE_RELAIS_1_USD)
    parts = {"Minuit": solde_minuit, "Luc": SOLDE_LUC_DECLARE_USD,
             "Rigaud": SOLDE_RIGAUD_CALCULE_AVANT_RECHARGE_USD - X_RESERVE_BRAS_A_SUR_RIGAUD_USD}
    ligne = PLAFOND_ARRET_PAR_GENERATION_USD * GENERATIONS
    par_cle = {}
    for c in CLES_LIGNEE_MERE:
        b = sum(bas_r[k] for k in ROLES_PAR_CLE[c]) * GENERATIONS
        h = sum(haut_r[k] for k in ROLES_PAR_CLE[c]) * GENERATIONS
        par_cle[c] = {"roles": ROLES_PAR_CLE[c], "bas": arrondi(b), "haut": arrondi(h),
                      "part_bornee_avant_recharge_de_rigaud": arrondi(parts[c]),
                      "rapport_part_sur_haut": arrondi(parts[c] / h, 4),
                      "marge_au_haut": arrondi(parts[c] - h),
                      "tient_le_cas_haut": parts[c] >= h}
    roles = sorted(REPARTITION_RETENUE)
    haut_course = {k: haut_r[k] * GENERATIONS for k in roles}
    admissibles, retenue = [], None
    for affect in itertools.product(CLES_LIGNEE_MERE, repeat=len(roles)):
        charge = {c: F(0) for c in CLES_LIGNEE_MERE}
        for r, c in zip(roles, affect):
            charge[c] += haut_course[r]
        if any(charge[c] > parts[c] for c in CLES_LIGNEE_MERE):
            continue
        plus_petit = min(parts[c] / charge[c] for c in CLES_LIGNEE_MERE if charge[c] > 0)
        d = dict(zip(roles, affect))
        if d == REPARTITION_RETENUE:
            retenue = plus_petit
        admissibles.append((plus_petit, d))
    meilleur = max(a[0] for a in admissibles)
    borne = sum(parts.values())
    somme_bas = sum(bas_r[k] for k in roles) * GENERATIONS
    somme_haut = sum(haut_course.values())
    return {
        "par_cle_sur_la_course_usd": par_cle,
        "somme_bas": arrondi(somme_bas),
        "somme_haut": arrondi(somme_haut),
        "x_reserve_bras_a_sur_rigaud": arrondi(X_RESERVE_BRAS_A_SUR_RIGAUD_USD),
        "borne_des_trois_cles_avant_recharge_de_rigaud": arrondi(borne),
        "borne_sur_somme_haut": arrondi(borne / somme_haut, 4),
        "manque_au_pire_du_premier_relais": arrondi(ligne - borne),
        "repartition_retenue_plus_petit_rapport": arrondi(retenue, 4) if retenue is not None else None,
        "regle_de_choix_meilleur_plus_petit_rapport": arrondi(meilleur, 4),
        "regle_de_choix_repartitions_admissibles": len(admissibles),
        "regle_de_choix_repartitions_au_meilleur_rapport": [a[1] for a in admissibles if a[0] == meilleur],
        "la_repartition_retenue_atteint_le_meilleur_rapport": retenue == meilleur,
        "part_de_rigaud_minimale_pour_tenir_le_haut_de_son_role": arrondi(haut_course["proposeur_espece_3"]),
    }


def requete_et_sondes():
    def octets(s):
        return len(s.encode("utf-8"))

    plus_longue = (BORNE_IDENTIFIANT_OCTETS + octets(SEPARATEUR_IDENTIFIANT)
                   + max(octets(v) for v in AXE_SUPPOSITION) + octets(SEPARATEUR_VALEURS)
                   + max(octets(v) for v in AXE_MENACE) + octets(SEPARATEUR_VALEURS)
                   + max(octets(v) for v in AXE_ETAGE))
    partie_remplie = TAILLE_GABARIT_PARTIE_SERVIE_OCTETS - octets(EMPLACEMENT_DE_CASE) + BORNE_LIGNE_DE_CASE_OCTETS
    return {
        "partie_servie": {
            "gabarit_octets": TAILLE_GABARIT_PARTIE_SERVIE_OCTETS,
            "emplacement_de_case_octets": octets(EMPLACEMENT_DE_CASE),
            "cases_de_la_legende": len(AXE_SUPPOSITION) * len(AXE_MENACE) * len(AXE_ETAGE),
            "ligne_de_case_la_plus_longue_a_la_forme_d_essai_octets": plus_longue,
            "borne_de_la_ligne_de_case_octets_valeur_du_redacteur": BORNE_LIGNE_DE_CASE_OCTETS,
            "la_forme_d_essai_tient_sous_la_borne": plus_longue <= BORNE_LIGNE_DE_CASE_OCTETS,
            "partie_servie_remplie_au_plus_octets": partie_remplie,
        },
        "synthese_servie_octets": TAILLE_SYNTHESE_SERVIE_OCTETS,
        "requete_d_un_proposeur_generation_1_au_plus_octets_hors_registre_et_enveloppe":
            partie_remplie + TAILLE_SYNTHESE_SERVIE_OCTETS,
        "sonde_de_refus_des_especes_1_a_5": {
            "ce_qu_elle_porte": "la partie servie remplie, seule",
            "requetes": len(V9_PROPOSEURS_USD),
            "plafond_usd": arrondi(PLAFOND_SONDE_REFUS_USD),
            "plafond_par_requete_si_partage_egal_usd": arrondi(PLAFOND_SONDE_REFUS_USD / len(V9_PROPOSEURS_USD)),
        },
        "non_mesure": ["registre servi aux generations 2 et 3", "enveloppe et separateurs du vehicule",
                       "requetes de l'aiguilleur et des juges", "sorties"],
    }


def confrontation_restes_nets():
    bas_r, haut_r, _ = couts_par_role()
    ligne = PLAFOND_ARRET_PAR_GENERATION_USD * GENERATIONS
    pire_proposeur = V9_APPELS_PAR_ESPECE * PIRE_PAR_APPEL_PROPOSEUR_USD * GENERATIONS

    def face(reste, besoin):
        return {"besoin_usd": arrondi(besoin), "tient": reste >= besoin,
                "manque_usd": arrondi(besoin - reste) if reste < besoin else "0",
                "marge_usd": arrondi(reste - besoin) if reste >= besoin else "0"}

    def cle(nom, restes, pire):
        b = sum(bas_r[k] for k in ROLES_PAR_CLE[nom]) * GENERATIONS
        h = sum(haut_r[k] for k in ROLES_PAR_CLE[nom]) * GENERATIONS
        res = {"roles": ROLES_PAR_CLE[nom]}
        for nom_reste, reste in restes.items():
            res[nom_reste] = {"reste_net_estime_usd": arrondi(reste), "au_cas_bas": face(reste, b),
                              "au_cas_haut": face(reste, h), "au_pire": face(reste, pire)}
        return res

    relais_3_haut = CLE_RELAIS_3_BORNE_RAPPORTEE_USD - CLE_RELAIS_3_DEPENSES_INSCRITES_USD
    relais_3_bas = relais_3_haut - CLE_RELAIS_3_APPELS_COUPES_AU_PIRE_USD
    x = X_RESERVE_BRAS_A_SUR_RIGAUD_USD
    rigaud = {
        "lecture_du_registre_lots_a_zero": RESTE_RIGAUD_LECTURE_REGISTRE_USD - x,
        "lecture_corrigee_lots_a_zero": RESTE_RIGAUD_LECTURE_CORRIGEE_USD - x,
        "lecture_du_registre_lots_a_45": RESTE_RIGAUD_LECTURE_REGISTRE_USD - LOTS_EN_COURS_SUR_RIGAUD_AU_PLUS_USD - x,
        "lecture_corrigee_lots_a_45": RESTE_RIGAUD_LECTURE_CORRIGEE_USD - LOTS_EN_COURS_SUR_RIGAUD_AU_PLUS_USD - x,
    }
    r2 = ROLES_PAR_CLE["cle_du_deuxieme_relais"]
    return {
        "nature": "restes nets ESTIMES par le comptable (62c625ab...), non des releves ; avant toute recharge",
        "Minuit": cle("Minuit", {"reste": RESTE_MINUIT_USD}, ligne),
        "Luc": cle("Luc", {"reste": RESTE_LUC_USD}, ligne),
        "Rigaud_apres_la_reserve_de_8_35_du_bras_A": cle("Rigaud", rigaud, pire_proposeur),
        "cle_du_deuxieme_relais": {
            "roles": r2, "reste_net_estime_usd": None,
            "bas": arrondi(sum(bas_r[k] for k in r2) * GENERATIONS),
            "haut": arrondi(sum(haut_r[k] for k in r2) * GENERATIONS),
            "pire": arrondi(ligne), "verdict": "indecidable : aucun reste connu"},
        "cle_du_troisieme_relais": cle("cle_du_troisieme_relais",
                                       {"reste_haut": relais_3_haut, "reste_bas_si_appels_coupes_factures": relais_3_bas},
                                       pire_proposeur),
        "avec_le_collisionneur_au_pire_pour_information": {
            "cle_du_troisieme_relais_cas_bas_plus_collisionneur": face(
                relais_3_haut, bas_r["proposeur_espece_2"] * GENERATIONS + COLLISIONNEUR_PIRE_CLE_RELAIS_3_USD),
        },
        "lignes_a_part_sans_cle_designee_usd": {
            "epreuve_des_temoins_plafond": arrondi(EPREUVE_TEMOINS["plafond"]),
            "sonde_de_refus_especes_1_a_5_plafond": arrondi(PLAFOND_SONDE_REFUS_USD)},
    }


RETRAITS = [
    "l'espece 6 : ses trois cas (regles du redacteur de la v3), son role de proposeur, ses 11 appels par generation",
    "la cle de l'espece 6 et le quatrieme relais ; leur part au pire de 199,65 USD",
    "la sonde de refus de l'espece 6, son plafond de 0,05 USD, sa borne de sortie, son rappel a 0,01 USD",
    "le prorata 1,2 de l'aiguilleur et des deux juges (66 appels sur 55)",
    "les reperes de tarif et de cout de l'espece 6",
    "la confrontation de la cle de l'espece 6 a son reste lu, avec et sans le collisionneur",
    "la variante « plafond de 150 garde » : 150 USD est de nouveau le plafond d'une generation",
    "les compositions a trois et a deux especes, non retenues (GO-2026-11-20-16)",
]


def calculer():
    return {
        "piece": "calcul du devis de la course nouvelles attaques, v6",
        "generations": GENERATIONS,
        "cinq_especes": cinq_especes(),
        "cles_lignee_mere": cles_lignee_mere(),
        "requete_et_sondes": requete_et_sondes(),
        "confrontation_restes_nets": confrontation_restes_nets(),
        "retraits_par_rapport_au_calcul_v5": RETRAITS,
    }


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : calcul_devis_course_nouvelles_attaques_v6.py SORTIE.json\n")
        return 2
    with open(argv[1], "x", encoding="utf-8", newline="\n") as f:
        json.dump(calculer(), f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
