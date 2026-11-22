#!/usr/bin/env python3
"""Arithmétique des devis des voies (A) et (B) du saboteur à budget, version 5 — v1 (bibliothèque standard seule).

Sans argument : imprime toutes les lignes [Lnn] citées par les deux devis et les deux additifs.
Trois sous-commandes portent des règles écrites d'avance, jouées par l'exécutante sans rien lire d'une sortie de mesure :

    echeance COUPURE_USD COMPTE_USD MAINTENANT_S BORNE_H MINIMUM_H
        échéance de la minuterie d'une machine : min(fin de la voie, maintenant + H), H = min(BORNE_H, (coupure − compte −
        forfait de téléchargement à la borne) / prix borne) ; H < MINIMUM_H : « AUCUNE CREATION » (code 3).
    essai-de-vitesse EPISODE_S ACTION_S DEPENSE_ESSAI_USD
        voie (A) : plafond de tours projeté par la formule du texte scellé (10.2) aux durées mesurées du chemin neuf ;
        « PART » si au moins 12 tours sont financés, « NE PART PAS » sinon (code 3).
    garde-de-rythme COUPURE_USD COMPTE_USD TOURS MAINTENANT_S
        course : délais au-delà desquels l'absence de la marque du tour 1, puis du tour 4, commande l'arrêt par l'identifiant ;
        les heures de la course sont celles de son échéance : min(30 h, heures permises par le compte, heures avant la fin de la voie).

Aucune donnée mesurée de l'expérience n'est lue : seulement des durées, des prix et des comptes, cités avec leur source.
"""
from __future__ import annotations

import math
import sys

# --- Sources ------------------------------------------------------------------------------------------------------------------
# [S1] devis scellé, brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-scelle-v1.md (cb881522…) : §§ 1 à 4
# [S2] erratum 1 du devis scellé (90342292…) : 127 épisodes distillés, 3 830 actions d'oracle hors tours, coût fixe 7,03
# [S3] registres/iib-executante/chiffres-devis-code-corrige-v1.md (4e10a004…) : bases mesurées sur la machine 61875617
# [S4] additif 1 à l'ordre de l'étalonnage (a9d43d59…) : forfait de téléchargement relevé, consignation
# [S5] mandat du rédacteur (0ead00d9…) : crédit chez le loueur, lignes proposées
# [S6] amorce de l'étalonnage au commit 43d6d067 : marge de destruction de la minuterie (1 800 s), consignation (2 400 s)
EPISODE_S = 39.08            # [S1] § 1 : un épisode généré (10 actions), machine du 19 novembre
ACTION_S = 0.511             # [S1] § 1 : une action d'oracle (un préremplissage, huit suites)
COUT_FIXE_DEVIS_H = 3.55     # [S1] § 4 : évaluation, distillation (96 épisodes), fin, aux durées attendues
DISTILLATION_S = 1.86        # [S1] § 1 : par transcription et par époque (chiffre du premier devis, jamais mesuré)
PRIX_BORNE = 1.38            # [S1] § 6 : 1,30 (carte) + 0,08 (stockage)
STOCKAGE_BORNE = 0.08
TELECHARGEMENT_BORNE = 2.00  # [S1] § 6 : 40 gigaoctets à 0,05
PRIX_CARTE, PRIX_STOCKAGE = 1.16, 0.033333          # [S3] prix relevés
PRIX_MESURE = PRIX_CARTE + PRIX_STOCKAGE
MISE_EN_ROUTE_H = 70 / 60                           # [S3] de la création au début du run, machine 61875617
VINGT_SEPT_LOTS_H = 11.5                            # [S3] 27 lots joués en environ 11,5 heures
TELECHARGEMENT_RELEVE = 1.04                        # [S4] forfait de téléchargement de l'offre de 61875617
CONSIGNATION_USD = 0.92                             # [S1] § 3 : consignation au plus (40 min à 1,38) ; [S6] 2 400 s
MARGE_DESTRUCTION_USD = 1800 / 3600 * PRIX_BORNE    # [S6] marge de la minuterie après l'échéance
PASSE_USD = 16.1 + 0.12                             # [S3] § 4 : étalonnage coupé et relance courte, ligne GO-2026-11-21-70
STOCKAGE_ARRET_JOUR = 0.80                          # [S3] machine 61875617 à l'arrêt
CREDIT_USD = 12.995                                 # [S5] crédit chez le loueur le 22 novembre à 14:11Z
PLAFOND_A, PLAFOND_B = 44.0, 55.0                   # GO-2026-11-22-71
COUPURE_A, COUPURE_B = 42.0, 52.0                   # proposées par les devis (dépense neuve de la voie)
RESERVE_TOURS = 10.0                                # même réserve que le devis scellé ([S1] § 6 : 55 − 10 = 45)
FIN_DE_VOIE_S = 1795816800                          # 2026-11-27T22:00:00Z
ENTREES = {"plafond": 45.0, "cout_fixe": 6.90, "prix": PRIX_BORNE, "hors_tours": 3830}   # fichier d'entrées, valeurs figées par le code
ARRET_AVANT_DESTRUCTION_H = 6.0                     # machine à l'arrêt entre sa fin normale et sa destruction (hypothèse)
CHARGEMENT_H = 0.25                                 # tolérance de chargement du modèle avant le premier tour

HEURE = 3600.0
LOT_GENERE_S = 8 * EPISODE_S + 160 * ACTION_S       # lot honnête, régénéré ou flagrant : 8 épisodes, 160 actions d'oracle
LOT_PLANTE_S = 80 * ACTION_S                        # lot planté : 80 actions de l'oracle à contexte réécrit, rien de généré
ETALONNAGE_H = (160 * EPISODE_S + 3840 * ACTION_S) / HEURE
TOUR_H = (32 * EPISODE_S + 320 * ACTION_S) / HEURE
HORS_TOURS_H = 3830 * ACTION_S / HEURE
EVALUATION_H = (256 * EPISODE_S + 2560 * ACTION_S) / HEURE
NON_TIRE_H = COUT_FIXE_DEVIS_H - EVALUATION_H + (127 - 96) * 2 * 3 * DISTILLATION_S / HEURE   # distillation à 127 et fin
PHI_LENT = VINGT_SEPT_LOTS_H * HEURE / (19 * LOT_GENERE_S + 8 * LOT_PLANTE_S)


def tire_h(tours: int) -> float:
    """Part de la course qui dépend du tirage (tours, actions hors tours, évaluation), aux durées du devis scellé."""
    return tours * TOUR_H + HORS_TOURS_H + EVALUATION_H


def course_h(phi: float, tours: int = 12) -> float:
    return MISE_EN_ROUTE_H + phi * tire_h(tours) + NON_TIRE_H


def plafond_de_tours(depense_passee: float, depense_etalonnage: float, episode_s: float, action_s: float) -> int:
    """Formule du texte scellé (10.2, nœud 7 (b')), comme `branches_v5.plafond_de_tours`."""
    reste = ENTREES["plafond"] - depense_passee - depense_etalonnage - ENTREES["cout_fixe"] - ENTREES["prix"] * action_s / HEURE * ENTREES["hors_tours"]
    tour = ENTREES["prix"] * 32 * (episode_s + 10 * action_s) / HEURE
    return math.floor(reste / tour)


def heures_permises(coupure: float, compte: float) -> float:
    return (coupure - compte - TELECHARGEMENT_BORNE) / PRIX_BORNE


def echeance(coupure: float, compte: float, maintenant_s: int, borne_h: float, minimum_h: float) -> tuple[int, str]:
    h = min(borne_h, heures_permises(coupure, compte))
    if not math.isfinite(h) or h < minimum_h:
        return 3, f"AUCUNE CREATION : {h:.2f} h permises < {minimum_h:.2f} h exigées (coupure {coupure:g}, compte {compte:.2f}) : nœud"
    ech = min(FIN_DE_VOIE_S, int(maintenant_s + math.floor(h * HEURE)))
    borne = "fin de la voie" if ech == FIN_DE_VOIE_S else f"{h:.2f} h permises"
    if ech - maintenant_s < minimum_h * HEURE:
        return 3, f"AUCUNE CREATION : {(ech - maintenant_s) / HEURE:.2f} h avant la fin de la voie < {minimum_h:.2f} h exigées : nœud"
    return 0, f"ECHEANCE_UTC_S={ech} ({borne} ; dépense de la machine tenue à {(ech - maintenant_s) / HEURE * PRIX_BORNE + TELECHARGEMENT_BORNE:.2f} USD au plus)"


def depense_passee_de_A(depense_essai: float) -> float:
    """Écriture du fichier d'entrées de la voie (A) : le code fige le plafond à 45 ; la voie planifie sous coupure − réserve."""
    return ENTREES["plafond"] - (COUPURE_A - RESERVE_TOURS) + depense_essai


def essai_de_vitesse(episode_s: float, action_s: float, depense_essai: float) -> tuple[int, str]:
    etalonnage_h = MISE_EN_ROUTE_H + (160 * episode_s + 3840 * action_s) / HEURE
    r = plafond_de_tours(depense_passee_de_A(depense_essai), etalonnage_h * PRIX_BORNE, episode_s, action_s)
    mot = "PART" if r >= 12 else "NE PART PAS"
    return (0 if r >= 12 else 3), (f"{mot} : plafond de tours projeté {r} (12 exigés) ; épisode {episode_s:.2f} s, action d'oracle {action_s:.3f} s, "
                                   f"étalonnage projeté {etalonnage_h:.2f} h, dépense passée écrite {depense_passee_de_A(depense_essai):.2f} USD")


BORNE_COURSE_H = 30.0                               # borne de l'échéance de la machine de la course (additifs, § 4.2)


def heures_de_la_course(coupure: float, compte: float, maintenant_s: int | None = None) -> float:
    """Heures que l'échéance laisse à la machine de la course : la borne, le compte de la voie, la fin de la voie."""
    h = min(BORNE_COURSE_H, heures_permises(coupure, compte))
    return h if maintenant_s is None else min(h, (FIN_DE_VOIE_S - maintenant_s) / HEURE)


def garde_de_rythme(coupure: float, compte: float, tours: int, maintenant_s: int | None = None) -> tuple[float, float, float]:
    phi_max = (heures_de_la_course(coupure, compte, maintenant_s) - MISE_EN_ROUTE_H - NON_TIRE_H) / tire_h(tours)
    return phi_max, CHARGEMENT_H + phi_max * TOUR_H, CHARGEMENT_H + 4 * phi_max * TOUR_H


def usd(h: float, prix: float, telechargement: float) -> float:
    return h * prix + telechargement


def main(argv: list[str]) -> int:
    if argv and argv[0] == "echeance" and len(argv) == 6:
        code, texte = echeance(float(argv[1]), float(argv[2]), int(argv[3]), float(argv[4]), float(argv[5]))
        print(texte)
        return code
    if argv and argv[0] == "essai-de-vitesse" and len(argv) == 4:
        code, texte = essai_de_vitesse(float(argv[1]), float(argv[2]), float(argv[3]))
        print(texte)
        return code
    if argv and argv[0] == "garde-de-rythme" and len(argv) == 5:
        phi, g1, g4 = garde_de_rythme(float(argv[1]), float(argv[2]), int(argv[3]), int(argv[4]))
        if phi < 1.0:
            print(f"AUCUNE CREATION : le compte ne laisse pas une course de {argv[3]} tours aux durées du devis scellé (facteur permis {phi:.2f} < 1) : nœud")
            return 3
        print(f"GARDE DE RYTHME : tour 1 écrit au plus tard {g1:.2f} h après la marque de début du run ; tour 4 au plus tard {g4:.2f} h ; "
              f"au-delà : arrêt par l'identifiant (facteur permis {phi:.2f} fois les durées du devis scellé)")
        return 0
    if argv:
        print(__doc__, file=sys.stderr)
        return 2

    L = []

    def ligne(n: int, texte: str) -> None:
        L.append(f"[L{n:02d}] {texte}")

    # --- bases -----------------------------------------------------------------------------------------------------------------
    ligne(1, f"prix relevé {PRIX_CARTE:.2f} + {PRIX_STOCKAGE:.6f} = {PRIX_MESURE:.6f} USD/h ; prix borne 1,30 + 0,08 = {PRIX_BORNE:.2f} USD/h")
    ligne(2, f"lot généré (honnête, régénéré, flagrant), aux durées du devis scellé : 8 × {EPISODE_S} + 160 × {ACTION_S} = {LOT_GENERE_S:.2f} s ; "
             f"lot planté : 80 × {ACTION_S} = {LOT_PLANTE_S:.2f} s")
    ligne(3, f"27 lots joués (8 honnêtes, 8 régénérés, 8 plantés, 3 flagrants) : modèle {19 * LOT_GENERE_S + 8 * LOT_PLANTE_S:.2f} s "
             f"= {(19 * LOT_GENERE_S + 8 * LOT_PLANTE_S) / HEURE:.3f} h ; relevé {VINGT_SEPT_LOTS_H} h ; facteur de la machine lente = {PHI_LENT:.4f}")
    ligne(4, f"étalonnage entier, aux durées du devis scellé : 160 × {EPISODE_S} + 3 840 × {ACTION_S} = {ETALONNAGE_H * HEURE:.2f} s = {ETALONNAGE_H:.4f} h ; "
             f"au rythme lent : {PHI_LENT * ETALONNAGE_H:.2f} h ; lot flagrant au rythme lent : {PHI_LENT * LOT_GENERE_S / 60:.1f} min")
    ligne(5, f"course, aux durées du devis scellé : un tour {TOUR_H:.4f} h ; 3 830 actions hors tours {HORS_TOURS_H:.4f} h ; évaluation {EVALUATION_H:.4f} h ; "
             f"part non tirée (distillation à 127 épisodes, fin) {NON_TIRE_H:.4f} h ; contrôle : coût fixe à 1,38 + 2,00 = "
             f"{(EVALUATION_H + NON_TIRE_H) * PRIX_BORNE + TELECHARGEMENT_BORNE:.2f} USD (erratum 1 du devis : 7,03)")
    ligne(6, f"course hors mise en route, aux durées du devis scellé : 12 tours {tire_h(12) + NON_TIRE_H:.3f} h ; 24 tours {tire_h(24) + NON_TIRE_H:.3f} h ; "
             f"mise en route relevée {MISE_EN_ROUTE_H:.4f} h")
    ligne(7, f"déjà dépensé sous GO-2026-11-21-70 : 16,1 + 0,12 = {PASSE_USD:.2f} USD ; stockage de 61875617 à l'arrêt : {STOCKAGE_ARRET_JOUR:.2f} USD par jour")
    ligne(8, f"crédit chez le loueur (22 novembre, 14:11Z) : {CREDIT_USD:.3f} USD ; consignation au plus {CONSIGNATION_USD:.2f} ; marge de destruction "
             f"{MARGE_DESTRUCTION_USD:.2f} ; dépassement au plus après une échéance : {CONSIGNATION_USD + MARGE_DESTRUCTION_USD:.2f} USD")

    # --- voie (A) --------------------------------------------------------------------------------------------------------------
    A = {}
    for nom, f, prix, tel, stock in (("attendu", 5.0, PRIX_MESURE, TELECHARGEMENT_RELEVE, PRIX_STOCKAGE), ("haut", 3.0, PRIX_BORNE, TELECHARGEMENT_BORNE, STOCKAGE_BORNE)):
        phi = PHI_LENT / f
        essai_h = MISE_EN_ROUTE_H + PHI_LENT * LOT_GENERE_S / HEURE + 2 * phi * LOT_GENERE_S / HEURE + 20 / 60
        etal_h = MISE_EN_ROUTE_H + phi * ETALONNAGE_H
        arret = ARRET_AVANT_DESTRUCTION_H * stock
        A[nom] = {"phi": phi, "essai_h": essai_h, "essai": usd(essai_h, prix, tel), "etal_h": etal_h, "etal": usd(etal_h, prix, tel) + arret,
                  "c12_h": course_h(phi, 12), "c12": usd(course_h(phi, 12), prix, tel) + arret,
                  "c24_h": course_h(phi, 24), "c24": usd(course_h(phi, 24), prix, tel) + arret, "prix": prix, "tel": tel, "arret": arret}
    a, h = A["attendu"], A["haut"]
    ligne(10, f"voie (A), facteur du chemin neuf sur le rythme lent : f = 5 → {a['phi']:.4f} fois les durées du devis scellé (attendu) ; "
              f"f = 3 → {h['phi']:.4f} fois (haut) ; non mesuré")
    ligne(11, f"voie (A), essai de vitesse (mise en route, un lot honnête par l'ancien chemin au rythme lent, deux lots par le chemin neuf, 20 min de marge) : "
              f"attendu {a['essai_h']:.3f} h, {a['essai']:.2f} USD ; haut {h['essai_h']:.3f} h, {h['essai']:.2f} USD ; "
              f"borne de 3 h : {usd(3, PRIX_BORNE, TELECHARGEMENT_BORNE):.2f} USD")
    ligne(12, f"voie (A), étalonnage rejoué (160 épisodes, 3 840 actions d'oracle), arrêt de 6 h avant destruction compris : attendu {a['etal_h']:.3f} h, "
              f"{a['etal']:.2f} USD ; haut {h['etal_h']:.3f} h, {h['etal']:.2f} USD ; borne de 6,5 h : {usd(6.5, PRIX_BORNE, TELECHARGEMENT_BORNE):.2f} USD")
    ligne(13, f"voie (A), course de 12 tours : attendu {a['c12_h']:.3f} h, {a['c12']:.2f} USD ; haut {h['c12_h']:.3f} h, {h['c12']:.2f} USD")
    ligne(14, f"voie (A), course de 24 tours : attendu {a['c24_h']:.3f} h, {a['c24']:.2f} USD ; haut {h['c24_h']:.3f} h, {h['c24']:.2f} USD")
    tot_a12, tot_h12 = a["essai"] + a["etal"] + a["c12"], h["essai"] + h["etal"] + h["c12"]
    tot_a24, tot_h24 = a["essai"] + a["etal"] + a["c24"], h["essai"] + h["etal"] + h["c24"]
    ligne(15, f"voie (A) entière, dépense neuve : 12 tours, attendu {tot_a12:.2f} USD, haut {tot_h12:.2f} USD ; 24 tours, attendu {tot_a24:.2f} USD, haut {tot_h24:.2f} USD "
              f"(durée de carte, 12 tours : attendu {a['essai_h'] + a['etal_h'] + a['c12_h']:.1f} h, haut {h['essai_h'] + h['etal_h'] + h['c12_h']:.1f} h)")
    pire_a = COUPURE_A + CONSIGNATION_USD + MARGE_DESTRUCTION_USD
    ligne(16, f"voie (A), plafond {PLAFOND_A:g} USD ; coupure {COUPURE_A:g} USD de dépense neuve, tenue par les échéances ; pire tenu par les gardes : "
              f"{COUPURE_A:g} + {CONSIGNATION_USD:.2f} + {MARGE_DESTRUCTION_USD:.2f} = {pire_a:.2f} USD")
    ligne(17, f"voie (A), dépense au-delà du crédit de {CREDIT_USD:.3f} USD : attendu {tot_a12 - CREDIT_USD:.2f} ; haut {tot_h12 - CREDIT_USD:.2f} ; pire {pire_a - CREDIT_USD:.2f} USD")
    ligne(18, f"voie (A), si 44 USD est un total de la ligne GO-2026-11-21-70, passé compris : dépense neuve permise 44 − {PASSE_USD:.2f} − stockage "
              f"(un jour : {STOCKAGE_ARRET_JOUR:.2f}) = {PLAFOND_A - PASSE_USD - STOCKAGE_ARRET_JOUR:.2f} USD ; l'attendu ({tot_a12:.2f}) y tient, le haut ({tot_h12:.2f}) non")
    for nom, v in (("attendu", a), ("haut", h)):
        dp = depense_passee_de_A(v["essai"])
        r = plafond_de_tours(dp, v["etal_h"] * PRIX_BORNE, v["phi"] * EPISODE_S, v["phi"] * ACTION_S)
        v["dp"], v["r"] = dp, r
    ligne(19, f"voie (A), fichier d'entrées : dépense passée écrite = 45 − ({COUPURE_A:g} − {RESERVE_TOURS:g}) + dépense de l'essai de vitesse = 13 + essai ; "
              f"attendu {a['dp']:.2f} USD, plafond de tours {a['r']} ; haut {h['dp']:.2f} USD, plafond de tours {h['r']}")
    # seuil de la règle de l'essai de vitesse : plus grand facteur qui finance encore 12 tours (pas de 0,01), essai à sa dépense attendue puis haute
    seuils = []
    for essai in (a["essai"], h["essai"]):
        k = 100
        while essai_de_vitesse(k / 100 * EPISODE_S, k / 100 * ACTION_S, essai)[0] == 0:
            k += 1
        seuils.append((k - 1) / 100)
    ligne(20, f"voie (A), règle de l'essai de vitesse (12 tours financés par la formule de 10.2) : passe jusqu'à {seuils[0]:.2f} fois les durées du devis scellé "
              f"(essai à {a['essai']:.2f} USD), jusqu'à {seuils[1]:.2f} fois (essai à {h['essai']:.2f} USD) ; soit f ≥ {PHI_LENT / seuils[0]:.2f} et f ≥ {PHI_LENT / seuils[1]:.2f}")
    sain = essai_de_vitesse(a["phi"] * EPISODE_S, a["phi"] * ACTION_S, a["essai"])
    artefact = essai_de_vitesse(PHI_LENT * EPISODE_S, PHI_LENT * ACTION_S, a["essai"])
    ligne(21, f"règle de l'essai de vitesse, cas sain (f = 5) : code {sain[0]}, « {sain[1]} »")
    ligne(22, f"règle de l'essai de vitesse, artefact (chemin neuf aussi lent que l'ancien) : code {artefact[0]}, « {artefact[1]} »")
    for n, (nom, v) in zip((23, 24), (("attendu", a), ("haut", h))):
        compte = v["essai"] + v["etal"]
        phi, g1, g4 = garde_de_rythme(COUPURE_A, compte, 12)
        ligne(n, f"voie (A), garde de rythme de la course de 12 tours, compte {nom} {compte:.2f} USD : {heures_de_la_course(COUPURE_A, compte):.2f} h de course permises ; "
                 f"facteur permis {phi:.2f} ; tour 1 avant {g1:.2f} h ; tour 4 avant {g4:.2f} h")
    # à f = 3 : plus grande dépense de l'essai de vitesse (au centime) qui laisse encore 12 tours financés
    c = 0
    while essai_de_vitesse(h["phi"] * EPISODE_S, h["phi"] * ACTION_S, c / 100)[0] == 0:
        c += 1
    ligne(25, f"voie (A), à f = 3 : 12 tours restent financés tant que l'essai de vitesse coûte au plus {(c - 1) / 100:.2f} USD ; "
              f"heures de course permises alors, compte attendu des deux premières étapes à f = 3 et au prix relevé "
              f"({usd(h['essai_h'], PRIX_MESURE, TELECHARGEMENT_RELEVE) + usd(h['etal_h'], PRIX_MESURE, TELECHARGEMENT_RELEVE) + ARRET_AVANT_DESTRUCTION_H * PRIX_STOCKAGE:.2f} USD) : "
              f"{heures_permises(COUPURE_A, usd(h['essai_h'], PRIX_MESURE, TELECHARGEMENT_RELEVE) + usd(h['etal_h'], PRIX_MESURE, TELECHARGEMENT_RELEVE) + ARRET_AVANT_DESTRUCTION_H * PRIX_STOCKAGE):.2f} h "
              f"pour {h['c12_h']:.2f} h attendues à ce rythme")

    # --- voie (B) --------------------------------------------------------------------------------------------------------------
    fin_h = 10 / 60
    lot28_lent_h = MISE_EN_ROUTE_H + PHI_LENT * LOT_GENERE_S / HEURE + fin_h
    lot28_vif_h = MISE_EN_ROUTE_H + LOT_GENERE_S / HEURE + fin_h
    b_lot_att = usd(lot28_lent_h, PRIX_MESURE, TELECHARGEMENT_RELEVE) + ARRET_AVANT_DESTRUCTION_H * PRIX_STOCKAGE
    b_lot_vif = usd(lot28_vif_h, PRIX_MESURE, TELECHARGEMENT_RELEVE) + ARRET_AVANT_DESTRUCTION_H * PRIX_STOCKAGE
    b_lot_haut = usd(lot28_lent_h, PRIX_BORNE, TELECHARGEMENT_BORNE) + ARRET_AVANT_DESTRUCTION_H * STOCKAGE_BORNE
    ligne(30, f"voie (B), lot 28 (8 épisodes flagrants, 160 actions d'oracle) et écriture de fin (10 min), arrêt de 6 h compris : machine au rythme lent "
              f"{lot28_lent_h:.3f} h, {b_lot_att:.2f} USD ; machine au rythme du devis scellé {lot28_vif_h:.3f} h, {b_lot_vif:.2f} USD ; haut {b_lot_haut:.2f} USD ; "
              f"borne de 3 h : {usd(3, PRIX_BORNE, TELECHARGEMENT_BORNE):.2f} USD")
    h_61875617 = 13.4                                   # du début de l'amorce (création 23:29Z le 21) à l'arrêt (12:54:36Z le 22), à relever par l'exécutante
    etal_les_deux = (h_61875617 + lot28_lent_h) * PRIX_BORNE
    etal_les_deux_vif = (h_61875617 + lot28_vif_h) * PRIX_BORNE
    r_a = plafond_de_tours(0.0, etal_les_deux, PHI_LENT * EPISODE_S, PHI_LENT * ACTION_S)
    # bornes du partage inconnu entre génération et oracle : 152 épisodes générés et 3 680 actions d'oracle en 41 400 s
    ep_max = (VINGT_SEPT_LOTS_H * HEURE - 3680 * ACTION_S) / 152
    ac_max = (VINGT_SEPT_LOTS_H * HEURE - 152 * EPISODE_S) / 3680
    r_a1 = plafond_de_tours(0.0, etal_les_deux, ep_max, ACTION_S)
    r_a2 = plafond_de_tours(0.0, etal_les_deux, EPISODE_S, ac_max)
    ligne(31, f"voie (B), plafond de tours, variante (a), durées de l'étalonnage tel qu'il a été joué (machine lente), dépense de l'étalonnage des deux machines à 1,38 "
              f"({h_61875617} h + {lot28_lent_h:.2f} h = {etal_les_deux:.2f} USD) : {r_a} tours si le facteur est le même pour l'épisode et l'action d'oracle ; "
              f"{r_a1} si toute la lenteur est dans l'épisode ({ep_max:.0f} s) ; {r_a2} si elle est toute dans l'action d'oracle ({ac_max:.2f} s) ; 12 exigés")
    r_b_vif = plafond_de_tours(0.0, etal_les_deux_vif, EPISODE_S, ACTION_S)
    r_b_lent = plafond_de_tours(0.0, etal_les_deux, PHI_LENT * EPISODE_S, PHI_LENT * ACTION_S)
    k = 100
    while plafond_de_tours(0.0, (h_61875617 + MISE_EN_ROUTE_H + k / 100 * LOT_GENERE_S / HEURE + fin_h) * PRIX_BORNE, k / 100 * EPISODE_S, k / 100 * ACTION_S) >= 12:
        k += 1
    ligne(32, f"voie (B), plafond de tours, variante (b), durées du seul lot 28 (machine neuve), même dépense de l'étalonnage : {r_b_vif} tours si la machine neuve "
              f"est au rythme du devis scellé ; {r_b_lent} si elle est au rythme lent ; 12 tours financés jusqu'à {(k - 1) / 100:.2f} fois les durées du devis scellé")
    B = {}
    for phi, prix, tel, stock in ((1.0, PRIX_MESURE, TELECHARGEMENT_RELEVE, PRIX_STOCKAGE), (2.0, PRIX_BORNE, TELECHARGEMENT_BORNE, STOCKAGE_BORNE),
                                  (3.0, PRIX_BORNE, TELECHARGEMENT_BORNE, STOCKAGE_BORNE), (PHI_LENT, PRIX_BORNE, TELECHARGEMENT_BORNE, STOCKAGE_BORNE)):
        B[phi] = (course_h(phi, 12), usd(course_h(phi, 12), prix, tel) + ARRET_AVANT_DESTRUCTION_H * stock, course_h(phi, 24),
                  usd(course_h(phi, 24), prix, tel) + ARRET_AVANT_DESTRUCTION_H * stock)
    ligne(33, "voie (B), course sur une carte, ancien code, 12 tours ; 24 tours : " + " ; ".join(
        f"à {phi:.2f} fois les durées du devis scellé {v[0]:.2f} h, {v[1]:.2f} USD ; {v[2]:.2f} h, {v[3]:.2f} USD" for phi, v in B.items())
        + f" (première colonne au prix relevé, les autres au prix borne ; au rythme lent et au prix relevé, 12 tours : "
          f"{usd(course_h(PHI_LENT, 12), PRIX_MESURE, TELECHARGEMENT_RELEVE):.2f} USD)")
    phi_b, g1_b, g4_b = garde_de_rythme(COUPURE_B, b_lot_att, 12)
    phi_b2, g1_b2, g4_b2 = garde_de_rythme(COUPURE_B, usd(3, PRIX_BORNE, TELECHARGEMENT_BORNE), 12)
    ligne(34, f"voie (B), garde de rythme de la course de 12 tours : compte attendu {b_lot_att:.2f} USD, {heures_de_la_course(COUPURE_B, b_lot_att):.2f} h de course permises "
              f"(borne de 30 h), facteur permis {phi_b:.2f}, tour 1 avant {g1_b:.2f} h, tour 4 avant {g4_b:.2f} h ; compte à la borne du lot 28 "
              f"{usd(3, PRIX_BORNE, TELECHARGEMENT_BORNE):.2f} USD : facteur permis {phi_b2:.2f}, tour 1 avant {g1_b2:.2f} h, tour 4 avant {g4_b2:.2f} h ; "
              f"pour 24 tours, compte attendu : facteur permis {garde_de_rythme(COUPURE_B, b_lot_att, 24)[0]:.2f}, tour 1 avant {garde_de_rythme(COUPURE_B, b_lot_att, 24)[1]:.2f} h")
    arrete_h = MISE_EN_ROUTE_H + CHARGEMENT_H + g1_b
    arrete = usd(arrete_h, PRIX_BORNE, TELECHARGEMENT_BORNE) + CONSIGNATION_USD
    ligne(35, f"voie (B), course arrêtée par la garde de rythme au tour 1 (machine lente) : {arrete_h:.2f} h de carte, {arrete:.2f} USD au plus, consignation comprise")
    ligne(36, "voie (B), course répartie sur N cartes (tours, actions hors tours et évaluation partagés ; distillation sur une carte), 12 tours : " + " ; ".join(
        f"rythme {nom}, N = {n} : {MISE_EN_ROUTE_H + phi * tire_h(12) / n + NON_TIRE_H:.1f} h de calendrier, "
        f"{(phi * tire_h(12) + n * MISE_EN_ROUTE_H + NON_TIRE_H) * PRIX_BORNE + n * TELECHARGEMENT_BORNE:.2f} USD"
        for nom, phi in (("du devis scellé", 1.0), ("lent", PHI_LENT)) for n in (1, 2, 4)) + " (prix borne ; temps de coordination non compté)")
    lot28_double_h = MISE_EN_ROUTE_H + 2 * LOT_GENERE_S / HEURE + fin_h
    b_lot_double = usd(lot28_double_h, PRIX_BORNE, TELECHARGEMENT_BORNE) + ARRET_AVANT_DESTRUCTION_H * STOCKAGE_BORNE
    b_att = b_lot_vif + B[1.0][1]                    # lot 28 puis course sur des machines au rythme du devis scellé
    b_att_arretee = b_lot_vif + arrete               # lot 28 au rythme du devis scellé, course sur une machine lente, arrêtée par la garde
    b_haut = b_lot_double + B[2.0][1]                # lot 28 puis course à deux fois les durées du devis scellé, prix aux bornes
    pire_b = COUPURE_B + CONSIGNATION_USD + MARGE_DESTRUCTION_USD
    ligne(37, f"voie (B) entière, dépense neuve, 12 tours : lot 28 puis course sur des machines au rythme du devis scellé {b_lot_vif:.2f} + {B[1.0][1]:.2f} = {b_att:.2f} USD ; "
              f"lot 28 au rythme du devis scellé puis course arrêtée par la garde de rythme {b_lot_vif:.2f} + {arrete:.2f} = {b_att_arretee:.2f} USD ; "
              f"lot 28 seul sur une machine lente (issue « ne part pas », motif « tours ») {b_lot_att:.2f} USD ; "
              f"haut (lot 28 puis course à 2 fois les durées, prix aux bornes) {b_lot_double:.2f} + {B[2.0][1]:.2f} = {b_haut:.2f} USD")
    ligne(38, f"voie (B), plafond {PLAFOND_B:g} USD ; coupure {COUPURE_B:g} USD de dépense neuve, tenue par les échéances ; pire tenu par les gardes : "
              f"{COUPURE_B:g} + {CONSIGNATION_USD:.2f} + {MARGE_DESTRUCTION_USD:.2f} = {pire_b:.2f} USD")
    ligne(39, f"voie (B), dépense au-delà du crédit de {CREDIT_USD:.3f} USD : course aboutie au rythme du devis scellé {b_att - CREDIT_USD:.2f} ; "
              f"course arrêtée par la garde {max(0.0, b_att_arretee - CREDIT_USD):.2f} ; lot 28 seul {max(0.0, b_lot_att - CREDIT_USD):.2f} ; "
              f"haut {b_haut - CREDIT_USD:.2f} ; pire {pire_b - CREDIT_USD:.2f} USD")
    ligne(40, f"voie (B), si 55 USD est un total de la ligne GO-2026-11-21-70, passé compris : dépense neuve permise 55 − {PASSE_USD:.2f} − {STOCKAGE_ARRET_JOUR:.2f} "
              f"= {PLAFOND_B - PASSE_USD - STOCKAGE_ARRET_JOUR:.2f} USD")

    # --- les deux voies ----------------------------------------------------------------------------------------------------------
    ligne(50, f"les deux voies, dépense neuve : attendu {tot_a12 + b_att:.2f} USD ; haut {tot_h12 + b_haut:.2f} USD ; pire tenu {pire_a + pire_b:.2f} USD ; "
              f"au-delà du crédit : {tot_a12 + b_att - CREDIT_USD:.2f} ; {tot_h12 + b_haut - CREDIT_USD:.2f} ; {pire_a + pire_b - CREDIT_USD:.2f} USD")
    ligne(51, f"ligne GO-2026-11-21-70 lue comme enveloppe unique (plafond 60, coupure 55), passé {PASSE_USD:.2f} et un jour de stockage compris : il reste "
              f"{55 - PASSE_USD - STOCKAGE_ARRET_JOUR:.2f} USD avant la coupure pour les deux voies ensemble ; attendu des deux voies {tot_a12 + b_att:.2f} USD")
    ligne(52, f"fin de la voie : minuterie 2026-11-27T22:00:00Z = {FIN_DE_VOIE_S} ; fin de la ligne GO-2026-11-22-71 2026-11-28T00:00:00Z = {FIN_DE_VOIE_S + 7200} ; "
              f"aucune création à partir de 2026-11-27T00:00:00Z = {FIN_DE_VOIE_S - 22 * 3600}")
    # échéances : cas sain et artefact (R5)
    e1 = echeance(COUPURE_A, 0.0, 1795500000, 3.0, 2.5)
    e2 = echeance(COUPURE_A, 41.0, 1795500000, 3.0, 2.5)
    e3 = echeance(COUPURE_B, 3.32, FIN_DE_VOIE_S - 5 * 3600, 30.0, 11.0)
    ligne(53, f"règle de l'échéance, cas sain (voie A, compte 0, borne 3 h) : code {e1[0]}, « {e1[1]} »")
    ligne(54, f"règle de l'échéance, artefact (voie A, compte 41 USD) : code {e2[0]}, « {e2[1]} »")
    ligne(55, f"règle de l'échéance, artefact (voie B, cinq heures avant la fin de la voie, 11 h exigées) : code {e3[0]}, « {e3[1]} »")
    gs = garde_de_rythme(COUPURE_A, 30.0, 12)
    ligne(56, f"garde de rythme, artefact (voie A, compte 30 USD, 12 tours) : facteur permis {gs[0]:.2f} : {'aucune création' if gs[0] < 1 else 'création permise'}")
    gt = garde_de_rythme(COUPURE_B, 3.0, 12, FIN_DE_VOIE_S - 8 * 3600)
    ligne(57, f"garde de rythme, artefact (voie B, compte 3 USD, 12 tours, huit heures avant la fin de la voie) : facteur permis {gt[0]:.2f} : "
              f"{'aucune création' if gt[0] < 1 else 'création permise'}")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
