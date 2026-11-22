#!/usr/bin/env python3
# Écrit par Claude Fable 5.2 (rédacteur), sur sa v5. Bibliothèque standard seule.
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v6.

Remplace `calcul-devis-voie-A-v5.py` (intact, R12). Changements, et eux seuls (décision de la mère du 22 novembre à 18:42Z [S14]) :
  - borne horaire du nœud porté à Lazar après un code 7 : sous-commande `borne-du-noeud` ajoutée ; elle rend trois instants
    absolus, comptés depuis l'arrêt (24, 33 et 36 heures), et n'ordonne jamais une destruction ;
  - [M33] ajoutée.
Aucune autre ligne ne change : les 28 lignes de la sortie v5 sont rendues égales à l'octet ; `second-rempart` est inchangée.
Rappel des changements de la v5 sur la v4 (décisions de la mère du 22 novembre à 18:21Z [S13]) :
  - seuil du second rempart : l'échéance plus 80 minutes (4 800 s), et non plus 10. À l'échéance, la minuterie de l'amorce consigne
    2 400 s au plus, puis tente la destruction 1 800 s au plus : avant ce seuil, une machine qui tourne peut être dans le
    fonctionnement normal de la minuterie ;
  - aucune destruction sans rapatriement vérifié : le code 6 de `second-rempart`, qui détruisait « vérifié ou non », est retiré et
    n'est plus jamais rendu ; deux heures après l'arrêt : code 7, machine gardée à l'arrêt, disque gardé, nœud à Lazar ;
  - un instant d'arrêt placé dans le futur est refusé (code 2) ; huitième cas à [M30] ;
  - [M29], [M30] et [M32] refaits ; le chemin (b bis) est ajouté à [M29].
Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 6.
Cinq sous-commandes portent des règles écrites d'avance, jouées par l'exécutante ou par la mère sans rien lire d'une sortie de mesure :

    rythme-etalonnage COUPURE_USD COMPTE_USD
        essai de vitesse en tête de l'étalonnage : délai, compté depuis la marque de début de l'étalonnage, au-delà duquel
        l'absence de la marque du lot 2 commande l'arrêt par l'identifiant.
    echeance COUPURE_USD COMPTE_USD MAINTENANT_S BORNE_H MINIMUM_H
        échéance de la minuterie d'une machine : min(fin de la voie, maintenant + H), H = min(BORNE_H, (coupure − compte −
        forfait de téléchargement à la borne) / prix borne) ; H < MINIMUM_H : « AUCUNE CREATION » (code 3).
    garde-de-rythme COUPURE_USD COMPTE_USD TOURS MAINTENANT_S MINUTES_ETALONNAGE
        course : refus de la création si la course, au rythme relevé de l'étalonnage plus la tolérance, ne tient pas dans les
        heures de son échéance ; sinon délais au-delà desquels l'absence de la marque du tour 1, puis du tour 4, commande l'arrêt.
    second-rempart ECHEANCE_S MAINTENANT_S ETAT [ARRET_PAR_CETTE_REGLE_S]
        ETAT : « tourne », « arret » ou « absente », lu à l'inventaire en champs filtrés. Code 0 : rien à faire. Code 4 :
        arrêter la machine par son identifiant (elle tourne encore 80 minutes après son échéance, au-delà des 70 minutes que
        prend au plus la minuterie de l'amorce : celle-ci a fait défaut). Code 5 : machine arrêtée par cette règle, rapatrier
        et vérifier ; destruction après rapatriement vérifié seulement. Code 7 : deux heures après l'arrêt ; sans
        rapatriement vérifié, machine gardée à l'arrêt, disque gardé, aucune destruction, nœud à Lazar. Code 2 : état ou
        instant illisible ou incohérent, nœud. Cette règle n'ordonne jamais une destruction ; le code 6 n'existe plus.
    borne-du-noeud ARRET_PAR_LE_REMPART_S MAINTENANT_S
        après un code 7 : la machine est gardée à l'arrêt, le nœud est porté à Lazar. Rend trois instants absolus, en secondes
        et en UTC : l'arrêt plus 33 heures (porté au nœud : réponse demandée avant lui), l'arrêt plus 24 heures (relance par
        la mère), l'arrêt plus 36 heures (passage du plafond déclaré comme dépense hors devis). Code 0 : nœud porté, attendre
        le mot de Lazar. Code 8 : 24 heures sans mot, la mère relance Lazar. Code 9 : 36 heures sans mot, déclarer la dépense
        hors devis. Code 2 : instant illisible ou incohérent. Aucun de ces codes n'ordonne une destruction : le silence de
        Lazar ne vaut jamais accord de destruction.

Aucune donnée mesurée de l'expérience n'est lue : seulement des durées, des prix et des comptes, cités avec leur source.
"""
from __future__ import annotations

import datetime
import math
import sys

# --- Sources ------------------------------------------------------------------------------------------------------------------
# [S1] devis scellé, brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-scelle-v1.md (cb881522…) : §§ 1 à 6
# [S2] erratum 1 du devis scellé (90342292…) : 127 épisodes distillés, 3 830 actions d'oracle hors tours, coût fixe 7,03
# [S3] registres/iib-executante/chiffres-devis-code-corrige-v1.md (4e10a004…) : bases mesurées sur la machine 61875617
# [S4] additif 1 à l'ordre de l'étalonnage (a9d43d59…) : forfait de téléchargement relevé, coupure propre à 16 USD
# [S5] mandat du rédacteur (0ead00d9…) : crédit chez le loueur
# [S6] registres/go.md de main (tête 187f4c41…) : GO-2026-11-22-75, 60 USD, échéance 2026-11-30
# [S7] fichier d'entrées scellé de l'étalonnage (44f90de6…) : plafond 45, dépense passée 0, coût fixe 6,90, prix 1,38
# [S8] GO-2026-11-22-77, correctifs 0023 et 0024 (code de la voie f7a5123e…) : total passé à la garde de dépense = min(ligne, configuration + antérieure)
# [S9] amorces du code de la voie (f7a5123e…), minuterie : consignation bornée à 2 400 s (`timeout -k 10 2400`), marge de destruction 1 800 s
# [S10] vérification du brouillon 2 (6be4c5c7…) : crédit relu après la recharge de 30 USD (GO-2026-11-22-77), 39,81 USD
# [S11] mot de la mère sur le second rempart (erratum 1 du mandat du brouillon 4, 4642543b…) : destruction par l'exécutante, échéance plus 10 minutes ; remplacé par [S13]
# [S12] registres/go.md de main : GO-2026-11-22-94, ligne de session de l'exécutante, échéance 2026-11-25
# [S13] décisions de la mère du 22 novembre à 18:21Z (mandat du brouillon 5, c25267a7… ; registre des nœuds de l'exécutante, étage 2,
#       GO-2026-11-22-106), sur la vérification du brouillon 4 (b5e73a07…, majeurs M1 et M2, mineur m1) : seuil du second rempart à
#       l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; instant d'arrêt dans le futur refusé
# [S14] décision de la mère du 22 novembre à 18:42Z (mandat du brouillon 6, b9e923fb… ; registre des nœuds de l'exécutante, étage 2,
#       GO-2026-11-22-106), selon la règle la plus étroite de la vérification du brouillon 5 (5a09da27…, section C) : le nœud du code 7
#       porte l'instant « arrêt plus 33 heures » ; relance de Lazar par la mère à l'arrêt plus 24 heures ; à l'arrêt plus 36 heures, le
#       passage du plafond est déclaré comme dépense hors devis ; le silence de Lazar ne vaut jamais accord de destruction
EPISODE_S = 39.08            # [S1] § 1
ACTION_S = 0.511             # [S1] § 1
COUT_FIXE_DEVIS_H = 3.55     # [S1] § 4
DISTILLATION_S = 1.86        # [S1] § 1
PRIX_BORNE = 1.38            # [S1] § 6
STOCKAGE_BORNE = 0.08
TELECHARGEMENT_BORNE = 2.00  # [S1] § 6
PRIX_CARTE, PRIX_STOCKAGE = 1.16, 0.033333          # [S3]
PRIX_MESURE = PRIX_CARTE + PRIX_STOCKAGE
MISE_EN_ROUTE_H = 70 / 60                           # [S3]
VINGT_SEPT_LOTS_H = 11.5                            # [S3]
TELECHARGEMENT_RELEVE = 1.04                        # [S4]
CONSIGNATION_USD = 0.92                             # [S1] § 3
ARRET_48_H_USD = 48 * STOCKAGE_BORNE                # [S1] § 5 : 48 heures de stockage à l'arrêt, 3,84
MARGE_DESTRUCTION_USD = 1800 / 3600 * PRIX_BORNE    # amorce, marge de la minuterie après l'échéance
COUPURE_PROPRE_USD = 16.0                           # [S4] règle de la surveillance pendant l'étalonnage
CREDIT_USD = 12.995                                 # [S5] valeur d'origine, lue le 22 novembre à 14:11Z
CREDIT_RELU_USD = 39.81                             # [S10]
CONSIGNATION_S, MARGE_DESTRUCTION_S = 2400, 1800    # [S9] ; 2 400 s au prix borne = la consignation de [S1] (0,92 USD)
MARGE_SEUIL_S = 600                                 # [S13] dix minutes au-delà de la fenêtre normale de la minuterie
DELAI_REMPART_S = CONSIGNATION_S + MARGE_DESTRUCTION_S + MARGE_SEUIL_S   # [S13] 4 800 s : l'exécutante agit à l'échéance plus 80 minutes
DELAI_REMPART_V4_S = 600                            # [S11] seuil du brouillon 4, gardé pour dire d'où vient le chiffre de 59,30 USD
GESTE_S = 600                                       # temps compté pour le geste de l'exécutante (relevé, arrêt, relecture) : hypothèse
FENETRE_RAPATRIEMENT_S = 7200                       # après l'arrêt par cette règle : deux heures pour rapatrier et vérifier ; au-delà, nœud à Lazar [S13]
NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H = 24, 33, 36   # [S14] heures comptées depuis l'arrêt par le second rempart
BORNE_ETALONNAGE_H = 14.0                           # échéance de la machine de l'étalonnage
FIN_SESSION_S = 1795651200                          # [S12] 2026-11-26T00:00:00Z, fin du dernier jour de la ligne de session
PLAFOND, COUPURE = 60.0, 55.0                       # [S6] ; coupure : celle de la configuration, exigée à l'égalité par le code
FIN_DE_VOIE_S = 1796076000                          # 2026-11-30T22:00:00Z, échéance de la minuterie de l'ordre scellé
ENTREES = {"plafond": 45.0, "depense_passee": 0.0, "cout_fixe": 6.90, "prix": PRIX_BORNE, "hors_tours": 3830}   # [S7]
ARRET_AVANT_DESTRUCTION_H = 6.0                     # machine à l'arrêt entre sa fin normale et sa destruction (hypothèse)
TOLERANCE = 1.2                                     # la course comptée 20 % plus lente que l'étalonnage (maître jamais chronométré)
MARGE_DE_MARQUE_H = 0.10                            # tolérance sur l'heure d'une marque de progrès
BORNE_COURSE_H = 30.0

HEURE = 3600.0
LOT_GENERE_S = 8 * EPISODE_S + 160 * ACTION_S
LOT_PLANTE_S = 80 * ACTION_S
ETALONNAGE_S = 160 * EPISODE_S + 3840 * ACTION_S
ETALONNAGE_H = ETALONNAGE_S / HEURE
TOUR_H = (32 * EPISODE_S + 320 * ACTION_S) / HEURE
HORS_TOURS_H = 3830 * ACTION_S / HEURE
EVALUATION_H = (256 * EPISODE_S + 2560 * ACTION_S) / HEURE
NON_TIRE_H = COUT_FIXE_DEVIS_H - EVALUATION_H + (127 - 96) * 2 * 3 * DISTILLATION_S / HEURE
PHI_LENT = VINGT_SEPT_LOTS_H * HEURE / (19 * LOT_GENERE_S + 8 * LOT_PLANTE_S)
ARRET_USD = ARRET_AVANT_DESTRUCTION_H * STOCKAGE_BORNE


def tire_h(tours: int) -> float:
    return tours * TOUR_H + HORS_TOURS_H + EVALUATION_H


def etalonnage_h(phi: float) -> float:
    return MISE_EN_ROUTE_H + phi * ETALONNAGE_H


def course_h(phi: float, tours: int = 12) -> float:
    return MISE_EN_ROUTE_H + phi * tire_h(tours) + NON_TIRE_H


def plafond_de_tours(depense_passee: float, depense_etalonnage: float, episode_s: float, action_s: float) -> int:
    """Formule du texte scellé (10.2, nœud 7 (b')), comme `branches_v5.plafond_de_tours`."""
    reste = ENTREES["plafond"] - depense_passee - depense_etalonnage - ENTREES["cout_fixe"] - ENTREES["prix"] * action_s / HEURE * ENTREES["hors_tours"]
    return math.floor(reste / (ENTREES["prix"] * 32 * (episode_s + 10 * action_s) / HEURE))


def tours_finances(phi: float) -> int:
    return plafond_de_tours(ENTREES["depense_passee"], etalonnage_h(phi) * PRIX_BORNE, phi * EPISODE_S, phi * ACTION_S)


def depense_projetee(compte: float, phi: float, tours: int = 12) -> float:
    """Dépense de la voie si l'étalonnage tourne au facteur phi et la course à phi fois la tolérance, prix et forfaits aux bornes."""
    etal = etalonnage_h(phi) * PRIX_BORNE + TELECHARGEMENT_BORNE + ARRET_USD
    course = (MISE_EN_ROUTE_H + TOLERANCE * phi * tire_h(tours) + NON_TIRE_H) * PRIX_BORNE + TELECHARGEMENT_BORNE + ARRET_USD
    return compte + etal + course


def seuil_de_rythme(coupure: float, compte: float) -> float:
    """Plus grand facteur (pas de 0,01) tel que la voie tienne sous la coupure et que 12 tours restent financés."""
    k = 0
    while depense_projetee(compte, (k + 1) / 100) <= coupure and tours_finances((k + 1) / 100) >= 12:
        k += 1
    return k / 100


def heures_permises(coupure: float, compte: float) -> float:
    return (coupure - compte - TELECHARGEMENT_BORNE) / PRIX_BORNE


def echeance(coupure: float, compte: float, maintenant_s: int, borne_h: float, minimum_h: float) -> tuple[int, str]:
    h = min(borne_h, heures_permises(coupure, compte))
    if not math.isfinite(h) or h < minimum_h:
        return 3, f"AUCUNE CREATION : {h:.2f} h permises < {minimum_h:.2f} h exigées (coupure {coupure:g}, compte {compte:.2f}) : nœud"
    ech = min(FIN_DE_VOIE_S, int(maintenant_s + math.floor(h * HEURE)))
    if ech - maintenant_s < minimum_h * HEURE:
        return 3, f"AUCUNE CREATION : {(ech - maintenant_s) / HEURE:.2f} h avant la fin de la voie < {minimum_h:.2f} h exigées : nœud"
    borne = "fin de la voie" if ech == FIN_DE_VOIE_S else f"{h:.2f} h permises"
    declaree = compte                                # correctif 0023 : le compte vrai, sans borne
    return 0, (f"ECHEANCE_UTC_S={ech} ({borne} ; dépense de la machine tenue à {(ech - maintenant_s) / HEURE * PRIX_BORNE + TELECHARGEMENT_BORNE:.2f} USD au plus) ; "
               f"dépense antérieure à déclarer : {math.ceil(declaree * 100 - 1e-9) / 100:.2f} (compte {compte:.3f}, arrondi au centime supérieur)")


def heures_de_la_course(coupure: float, compte: float, maintenant_s: int | None = None) -> float:
    h = min(BORNE_COURSE_H, heures_permises(coupure, compte))
    return h if maintenant_s is None else min(h, (FIN_DE_VOIE_S - maintenant_s) / HEURE)


def garde_de_rythme(coupure: float, compte: float, tours: int, maintenant_s: int | None = None) -> tuple[float, float, float]:
    phi_max = (heures_de_la_course(coupure, compte, maintenant_s) - MISE_EN_ROUTE_H - NON_TIRE_H) / tire_h(tours)
    return phi_max, MARGE_DE_MARQUE_H + phi_max * TOUR_H, MARGE_DE_MARQUE_H + 4 * phi_max * TOUR_H


def decision_course(coupure: float, compte: float, tours: int, maintenant_s: int | None, minutes_etalonnage: float) -> tuple[int, str]:
    phi_etal = minutes_etalonnage * 60 / ETALONNAGE_S
    phi_max, g1, g4 = garde_de_rythme(coupure, compte, tours, maintenant_s)
    if TOLERANCE * phi_etal > phi_max:
        return 3, (f"AUCUNE CREATION : au rythme de l'étalonnage ({phi_etal:.2f} fois les durées du devis scellé) plus la tolérance, une course de {tours} tours "
                   f"ne tient pas dans les heures de son échéance (facteur permis {phi_max:.2f}) : nœud")
    return 0, (f"GARDE DE RYTHME : tour 1 écrit au plus tard {g1 * 60:.0f} min après la marque de début de la course ; tour 4 au plus tard {g4 * 60:.0f} min ; "
               f"au-delà : arrêt par l'identifiant (rythme de l'étalonnage {phi_etal:.2f}, facteur permis {phi_max:.2f})")


def coupure_machine(compte: float) -> float:
    """Correctif 0023 [S8] : la machine dépense au plus min(coupure de la configuration, plafond de la ligne − dépense antérieure)."""
    return min(COUPURE, PLAFOND - compte)


def epuisement_h(compte: float) -> float:
    """Heures avant l'épuisement calculé par le lanceur (`session_v3 depense`, plafond total T, antérieure retranchée), forfait à la borne."""
    total = min(PLAFOND, COUPURE + compte)
    return (total - compte - TELECHARGEMENT_BORNE) / PRIX_BORNE


def second_rempart(echeance_s: int, maintenant_s: int, etat: str, arret_s: int | None = None) -> tuple[int, str]:
    """Règle de l'exécutante [S11] [S13]. Elle n'ordonne jamais une destruction : le lanceur ne détruit pas une machine qui tourne,
    et aucune machine n'est détruite sans rapatriement vérifié. Le code 6 de la v4 n'est plus jamais rendu."""
    seuil = echeance_s + DELAI_REMPART_S
    if (etat not in ("tourne", "arret", "absente") or echeance_s <= 0 or maintenant_s <= 0
            or (arret_s is not None and (arret_s < seuil or arret_s > maintenant_s))):
        return 2, ("ILLISIBLE : état hors de « tourne », « arret », « absente », ou instant incohérent (arrêt avant le seuil, ou placé dans le futur) : "
                   "aucun geste par cette règle, nœud")
    if etat == "absente":
        return 0, "RIEN : machine absente de l'inventaire (un inventaire illisible n'est pas une absence)"
    if arret_s is not None:
        if etat == "tourne":
            return 4, "ARRETER par l'identifiant, maintenant : la machine arrêtée par cette règle tourne de nouveau ; nœud"
        limite = arret_s + FENETRE_RAPATRIEMENT_S
        if maintenant_s < limite:
            return 5, (f"RAPATRIER ET VERIFIER : machine arrêtée par cette règle ; destruction par l'identifiant après rapatriement vérifié seulement ; "
                       f"sans rapatriement vérifié à {limite} : machine gardée à l'arrêt, nœud à Lazar")
        return 7, "GARDER A L'ARRET : deux heures après l'arrêt ; sans rapatriement vérifié, disque gardé, aucune destruction, nœud à Lazar"
    if maintenant_s < seuil:
        return 0, f"RIEN : avant l'échéance plus 80 minutes ({seuil}) ; la minuterie de l'amorce a 70 minutes pour consigner puis détruire"
    if etat == "tourne":
        return 4, "ARRETER par l'identifiant, maintenant : la machine tourne 80 minutes après son échéance, la minuterie a fait défaut ; puis relire son état"
    return 0, "RIEN par cette règle : machine déjà à l'arrêt ; chemin normal (rapatriement vérifié, puis destruction) ; 24 heures d'arrêt sans destruction : nœud"


def utc(s: int) -> str:
    return datetime.datetime.fromtimestamp(s, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def total_gardee_a_l_arret(heures: float) -> float:
    """Total de la voie, au plus, quand la machine arrêtée par le second rempart est gardée à l'arrêt depuis `heures` : [M29], (b bis)."""
    return COUPURE + (DELAI_REMPART_S + GESTE_S) / HEURE * PRIX_BORNE + heures * STOCKAGE_BORNE


def borne_du_noeud(arret_s: int, maintenant_s: int) -> tuple[int, str]:
    """Borne horaire du nœud porté à Lazar après un code 7 [S14]. Elle n'ordonne jamais une destruction."""
    if arret_s <= 0 or maintenant_s < arret_s + FENETRE_RAPATRIEMENT_S:
        return 2, ("ILLISIBLE : instant incohérent (avant l'arrêt plus deux heures, où vient le code 7, ou arrêt placé dans le futur) : "
                   "aucun geste par cette règle, message à la mère")
    relance, borne, hors = (arret_s + h * 3600 for h in (NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H))
    instants = (f"BORNE_DU_NOEUD_UTC_S={borne} = {utc(borne)} : réponse de Lazar demandée avant cet instant, total {total_gardee_a_l_arret(NOEUD_BORNE_H):.2f} USD au plus ; "
                f"relance par la mère à {relance} = {utc(relance)}, {total_gardee_a_l_arret(NOEUD_RELANCE_H):.2f} USD au plus ; "
                f"dépense hors devis déclarée à {hors} = {utc(hors)}, {total_gardee_a_l_arret(NOEUD_HORS_DEVIS_H):.2f} USD au plus, puis {STOCKAGE_BORNE:.2f} USD par heure ; "
                f"machine gardée à l'arrêt, aucune destruction : le silence de Lazar ne vaut jamais accord de destruction ; "
                f"totaux comptés pour un arrêt à l'échéance plus {(DELAI_REMPART_S + GESTE_S) // 60} minutes au plus : le compte vrai de la voie prime")
    if maintenant_s < relance:
        return 0, "NOEUD PORTE A LAZAR : attendre son mot ; " + instants
    if maintenant_s < hors:
        return 8, f"RELANCER LAZAR, par la mère : {NOEUD_RELANCE_H} heures d'arrêt sans son mot ; destruction sur son mot exprès, ou relèvement du plafond de la ligne ; " + instants
    return 9, f"DECLARER LA DEPENSE HORS DEVIS, par la mère, à Lazar : {NOEUD_HORS_DEVIS_H} heures d'arrêt sans son mot, le plafond de {PLAFOND:g} USD va être passé ; " + instants


def usd(h: float, prix: float, telechargement: float, stockage: float) -> float:
    return h * prix + telechargement + ARRET_AVANT_DESTRUCTION_H * stockage


def main(argv: list[str]) -> int:
    if argv and argv[0] == "rythme-etalonnage" and len(argv) == 3:
        s = seuil_de_rythme(float(argv[1]), float(argv[2]))
        if s < 1.0:
            print(f"AUCUNE CREATION : le compte ne laisse pas la voie finir aux durées du devis scellé (facteur permis {s:.2f} < 1) : nœud")
            return 3
        print(f"ESSAI DE VITESSE : marque du lot 2 de l'étalonnage au plus tard {2 * s * LOT_GENERE_S / 60:.1f} min après la marque de début ; "
              f"au-delà : arrêt par l'identifiant (facteur permis {s:.2f} fois les durées du devis scellé)")
        return 0
    if argv and argv[0] == "echeance" and len(argv) == 6:
        code, texte = echeance(float(argv[1]), float(argv[2]), int(argv[3]), float(argv[4]), float(argv[5]))
        print(texte)
        return code
    if argv and argv[0] == "garde-de-rythme" and len(argv) == 6:
        code, texte = decision_course(float(argv[1]), float(argv[2]), int(argv[3]), int(argv[4]), float(argv[5]))
        print(texte)
        return code
    if argv and argv[0] == "second-rempart" and len(argv) in (4, 5):
        try:
            code, texte = second_rempart(int(argv[1]), int(argv[2]), argv[3], int(argv[4]) if len(argv) == 5 else None)
        except ValueError:
            code, texte = 2, "ILLISIBLE : instant non entier : aucun geste par cette règle, nœud"
        print(texte)
        return code
    if argv and argv[0] == "borne-du-noeud" and len(argv) == 3:
        try:
            code, texte = borne_du_noeud(int(argv[1]), int(argv[2]))
        except ValueError:
            code, texte = 2, "ILLISIBLE : instant non entier : aucun geste par cette règle, message à la mère"
        print(texte)
        return code
    if argv:
        print(__doc__, file=sys.stderr)
        return 2

    L = []

    def ligne(n: int, texte: str) -> None:
        L.append(f"[M{n:02d}] {texte}")

    ligne(1, f"prix relevé {PRIX_CARTE:.2f} + {PRIX_STOCKAGE:.6f} = {PRIX_MESURE:.6f} USD/h ; prix borne 1,30 + 0,08 = {PRIX_BORNE:.2f} USD/h ; "
             f"forfait de téléchargement relevé {TELECHARGEMENT_RELEVE:.2f}, borne {TELECHARGEMENT_BORNE:.2f} USD par machine")
    ligne(2, f"lot généré, aux durées du devis scellé : 8 × {EPISODE_S} + 160 × {ACTION_S} = {LOT_GENERE_S:.2f} s ; étalonnage entier : {ETALONNAGE_S:.2f} s = {ETALONNAGE_H:.4f} h ; "
             f"mise en route relevée {MISE_EN_ROUTE_H:.4f} h")
    ligne(3, f"27 lots joués par l'ancien chemin sur 61875617 : {VINGT_SEPT_LOTS_H} h pour {(19 * LOT_GENERE_S + 8 * LOT_PLANTE_S) / HEURE:.3f} h aux durées du devis scellé : "
             f"facteur de la machine lente = {PHI_LENT:.4f}")
    ligne(4, f"course, aux durées du devis scellé : un tour {TOUR_H:.4f} h ; 3 830 actions hors tours {HORS_TOURS_H:.4f} h ; évaluation {EVALUATION_H:.4f} h ; "
             f"part non tirée {NON_TIRE_H:.4f} h ; 12 tours hors mise en route {tire_h(12) + NON_TIRE_H:.3f} h ; 24 tours {tire_h(24) + NON_TIRE_H:.3f} h")
    ligne(5, f"ligne GO-2026-11-22-75 : plafond {PLAFOND:g} USD, dépense neuve ; coupure {COUPURE:g} USD (configuration) ; crédit chez le loueur le 22 novembre à 14:11Z : {CREDIT_USD:.3f} USD (valeur d'origine ; relu ensuite : [M31])")

    A = {}
    for nom, f, prix, tel, stock in (("attendu", 5.0, PRIX_MESURE, TELECHARGEMENT_RELEVE, PRIX_STOCKAGE), ("haut", 3.0, PRIX_BORNE, TELECHARGEMENT_BORNE, STOCKAGE_BORNE)):
        phi = PHI_LENT / f
        A[nom] = {"phi": phi, "etal_h": etalonnage_h(phi), "etal": usd(etalonnage_h(phi), prix, tel, stock),
                  "c12_h": course_h(phi, 12), "c12": usd(course_h(phi, 12), prix, tel, stock),
                  "c24_h": course_h(phi, 24), "c24": usd(course_h(phi, 24), prix, tel, stock), "tours": tours_finances(phi)}
    a, h = A["attendu"], A["haut"]
    ligne(10, f"rythme du tirage sur la carte, en fois les durées du devis scellé : attendu {a['phi']:.4f} (5 fois plus rapide que le rythme relevé) ; "
              f"haut {h['phi']:.4f} (3 fois plus rapide) ; non mesuré")
    ligne(11, f"étalonnage entier rejoué (160 épisodes, 3 840 actions d'oracle), forfait et 6 h d'arrêt compris : attendu {a['etal_h']:.3f} h, {a['etal']:.2f} USD ; "
              f"haut {h['etal_h']:.3f} h, {h['etal']:.2f} USD")
    ligne(12, f"course de 12 tours : attendu {a['c12_h']:.3f} h, {a['c12']:.2f} USD ; haut {h['c12_h']:.3f} h, {h['c12']:.2f} USD ; "
              f"course de 24 tours : attendu {a['c24_h']:.3f} h, {a['c24']:.2f} USD ; haut {h['c24_h']:.3f} h, {h['c24']:.2f} USD")
    haut_releve = usd(h["etal_h"], PRIX_MESURE, TELECHARGEMENT_RELEVE, PRIX_STOCKAGE) + usd(h["c12_h"], PRIX_MESURE, TELECHARGEMENT_RELEVE, PRIX_STOCKAGE)
    ligne(13, f"voie entière, dépense neuve : 12 tours, attendu {a['etal'] + a['c12']:.2f} USD, haut {h['etal'] + h['c12']:.2f} USD ; 24 tours, attendu {a['etal'] + a['c24']:.2f} USD, "
              f"haut {h['etal'] + h['c24']:.2f} USD ; durée de carte, 12 tours : attendu {a['etal_h'] + a['c12_h']:.1f} h, haut {h['etal_h'] + h['c12_h']:.1f} h ; "
              f"3 fois plus rapide au prix relevé, 12 tours : {haut_releve:.2f} USD")
    pire = COUPURE + CONSIGNATION_USD + ARRET_48_H_USD
    ligne(14, f"plafond {PLAFOND:g} USD ; coupure {COUPURE:g} USD ; pire tenu par les gardes : {COUPURE:g} + {CONSIGNATION_USD:.2f} + {ARRET_48_H_USD:.2f} = {pire:.2f} USD ; "
              f"étalonnage seul, coupé par la règle de la surveillance : {COUPURE_PROPRE_USD:g} + {CONSIGNATION_USD:.2f} + {ARRET_48_H_USD:.2f} = {COUPURE_PROPRE_USD + CONSIGNATION_USD + ARRET_48_H_USD:.2f} USD")
    ligne(15, f"dépense au-delà du crédit de {CREDIT_USD:.3f} USD : attendu {a['etal'] + a['c12'] - CREDIT_USD:.2f} ; haut {h['etal'] + h['c12'] - CREDIT_USD:.2f} ; pire {pire - CREDIT_USD:.2f} USD")
    ligne(16, f"fichier d'entrées scellé (plafond 45, dépense passée 0, coût fixe 6,90, prix 1,38) : tours financés par la formule de 10.2 : attendu {a['tours']} ; haut {h['tours']}")
    s = seuil_de_rythme(COUPURE, 0.0)
    ligne(17, f"essai de vitesse en tête de l'étalonnage : la voie tient sous {COUPURE:g} USD (12 tours, course comptée {TOLERANCE:g} fois plus lente que l'étalonnage, prix aux bornes) "
              f"jusqu'à {s:.2f} fois les durées du devis scellé, soit un tirage au moins {PHI_LENT / s:.2f} fois plus rapide que le rythme relevé ; dépense projetée à ce facteur "
              f"{depense_projetee(0.0, s):.2f} USD ; tours financés à ce facteur {tours_finances(s)}")
    ligne(18, f"essai de vitesse : marque du lot 2 au plus tard {2 * s * LOT_GENERE_S / 60:.1f} min après la marque de début ; aux rythmes attendu, haut et lent, elle vient à "
              f"{2 * a['phi'] * LOT_GENERE_S / 60:.1f}, {2 * h['phi'] * LOT_GENERE_S / 60:.1f} et {2 * PHI_LENT * LOT_GENERE_S / 60:.1f} min (cas sains, cas sain, artefact)")
    arret_h = MISE_EN_ROUTE_H + 2 * s * LOT_GENERE_S / HEURE + 0.5
    ligne(19, f"voie arrêtée par l'essai de vitesse (mise en route, délai du lot 2, un relevé de 30 min) : {arret_h:.2f} h ; {arret_h * PRIX_MESURE + TELECHARGEMENT_RELEVE:.2f} USD au prix relevé ; "
              f"{arret_h * PRIX_BORNE + TELECHARGEMENT_BORNE + CONSIGNATION_USD:.2f} USD au plus")
    for n, (nom, v) in zip((20, 21), (("attendu", a), ("haut", h))):
        minutes = v["phi"] * ETALONNAGE_S / 60
        code, texte = decision_course(COUPURE, v["etal"], 12, None, minutes)
        ligne(n, f"course de 12 tours, compte {nom} {v['etal']:.2f} USD, étalonnage joué en {minutes:.0f} min : {heures_de_la_course(COUPURE, v['etal']):.2f} h de course permises ; code {code}, « {texte} »")
    code, texte = decision_course(COUPURE, h["etal"], h["tours"], None, h["phi"] * ETALONNAGE_S / 60)
    ligne(22, f"garde de la course, artefact (rythme haut, {h['tours']} tours, le plus grand nombre financé par la formule) : code {code}, « {texte} »")
    k = 12
    while decision_course(COUPURE, h["etal"], k + 1, None, h["phi"] * ETALONNAGE_S / 60)[0] == 0:
        k += 1
    ligne(23, f"au rythme haut, la garde de la course admet au plus {k} tours ; la formule de 10.2 en finance {h['tours']} : au-delà de {k} tours, aucune création, nœud")
    e1 = echeance(COUPURE, a["etal"], 1795600000, BORNE_COURSE_H, 11.0)
    e2 = echeance(COUPURE, 50.0, 1795600000, BORNE_COURSE_H, 11.0)
    e3 = echeance(COUPURE, h["etal"], 1795600000, BORNE_COURSE_H, 11.0)
    ligne(24, f"règle de l'échéance, cas sain (compte attendu {a['etal']:.2f} USD) : code {e1[0]}, « {e1[1]} »")
    ligne(25, f"règle de l'échéance, cas sain (compte haut {h['etal']:.2f} USD, au-delà de 5) : code {e3[0]}, « {e3[1]} »")
    ligne(26, f"règle de l'échéance, artefact (compte 50 USD) : code {e2[0]}, « {e2[1]} »")
    cas = ", ".join(f"compte {c:.2f} : machine {coupure_machine(c):.2f}, épuisement {epuisement_h(c):.2f} h, échéance {min(BORNE_COURSE_H, heures_permises(COUPURE, c)):.2f} h"
                    for c in (0.0, a["etal"], h["etal"], 16.22))
    ligne(27, f"correctif 0023, forfait à la borne : la machine dépense au plus min({COUPURE:g}, {PLAFOND:g} − compte) ; le lanceur l'épuise à (min({PLAFOND:g}, {COUPURE:g} + compte) − compte − 2) / 1,38 h, "
              f"jamais avant l'échéance min({BORNE_COURSE_H:g}, ({COUPURE:g} − compte − 2) / 1,38) h ; {cas}")
    ligne(28, f"dates : échéance de la minuterie au plus tard 2026-11-30T22:00:00Z = {FIN_DE_VOIE_S} ; fin de la ligne 2026-12-01T00:00:00Z = {FIN_DE_VOIE_S + 7200} ; "
              f"aucune création à partir de 2026-11-27T00:00:00Z = 1795737600")
    amorce_seule = COUPURE + (CONSIGNATION_S + MARGE_DESTRUCTION_S) / HEURE * PRIX_BORNE
    marche_usd = (DELAI_REMPART_S + GESTE_S) / HEURE * PRIX_BORNE            # la machine tourne de l'échéance à l'arrêt par l'exécutante
    executante = COUPURE + marche_usd + FENETRE_RAPATRIEMENT_S / HEURE * STOCKAGE_BORNE
    a_l_arret = COUPURE + marche_usd                                         # (b bis) total de la voie à l'instant de l'arrêt
    gardee_24, gardee_48 = a_l_arret + 24 * STOCKAGE_BORNE, a_l_arret + ARRET_48_H_USD
    h_sous_pire = math.floor((pire - a_l_arret) / STOCKAGE_BORNE * 10 + 1e-9) / 10       # arrondi par défaut, au dixième d'heure
    h_sous_plafond = math.floor((PLAFOND - a_l_arret) / STOCKAGE_BORNE * 10 + 1e-9) / 10
    gardee_48_v4 = COUPURE + (DELAI_REMPART_V4_S + GESTE_S) / HEURE * PRIX_BORNE + ARRET_48_H_USD
    fin_normale = COUPURE + ARRET_48_H_USD
    surv = ", ".join(f"compte {c:.2f} : {min(PLAFOND, COUPURE + c) + CONSIGNATION_USD + ARRET_48_H_USD:.2f}" for c in (0.0, a["etal"], h["etal"], 16.22))
    tenu = max(amorce_seule, executante, fin_normale)
    ligne(29, f"pire de la voie selon le rempart qui joue, prix et forfaits aux bornes, total de la voie à l'échéance {COUPURE:g} USD au plus : "
              f"(a) la minuterie de l'amorce joue seule, les deux remparts de la session tombés : {COUPURE:g} + ({CONSIGNATION_S} + {MARGE_DESTRUCTION_S}) s × {PRIX_BORNE:.2f} = {amorce_seule:.2f} USD, "
              f"{'≤' if amorce_seule <= PLAFOND else '> : RÉSERVE,'} {PLAFOND:g} ; "
              f"(b) la minuterie fait défaut, l'exécutante arrête à l'échéance plus {DELAI_REMPART_S // 60} minutes, le rapatriement est vérifié en {FENETRE_RAPATRIEMENT_S / HEURE:g} h au plus, puis elle détruit : "
              f"{COUPURE:g} + ({DELAI_REMPART_S} + {GESTE_S}) s × {PRIX_BORNE:.2f} + {FENETRE_RAPATRIEMENT_S / HEURE:g} h × {STOCKAGE_BORNE:.2f} = {executante:.2f} USD ; "
              f"(b bis) même chemin, rapatriement non vérifié à {FENETRE_RAPATRIEMENT_S / HEURE:g} h : machine gardée à l'arrêt, aucune destruction, nœud à Lazar : "
              f"{COUPURE:g} + {marche_usd:.2f} = {a_l_arret:.2f} USD à l'arrêt, puis {STOCKAGE_BORNE:.2f} USD par heure : {gardee_24:.2f} USD à 24 h, {gardee_48:.2f} USD à 48 h ; "
              f"sous le pire annoncé de {pire:.2f} USD jusqu'à {h_sous_pire:.1f} h d'arrêt, sous le plafond de {PLAFOND:g} USD jusqu'à {h_sous_plafond:.1f} h ; "
              f"à 48 h : {'sous le plafond' if gardee_48 <= PLAFOND else 'AU-DELÀ DU PLAFOND, RÉSERVE NOMMÉE'} "
              f"(au seuil de {DELAI_REMPART_V4_S // 60} minutes du brouillon 4, ce chemin donnait {gardee_48_v4:.2f} USD à 48 h : ce chiffre ne vaut plus) ; "
              f"(c) fin normale à la coupure, puis 48 h d'arrêt : {COUPURE:g} + {ARRET_48_H_USD:.2f} = {fin_normale:.2f} USD ; "
              f"le plus grand de (a), (b) et (c), {tenu:.2f} USD, est sous le pire annoncé de {pire:.2f} USD [M14] : {'oui' if tenu <= pire else 'NON'} ; "
              f"(d) la minuterie ET l'exécutante font défaut, seule la surveillance du lanceur joue : arrêt au total compté min({PLAFOND:g}, {COUPURE:g} + compte), "
              f"puis {CONSIGNATION_USD:.2f} et 48 h de stockage ({ARRET_48_H_USD:.2f}) : {surv} USD : au-delà du plafond dès un compte de {PLAFOND - COUPURE:g} USD, RÉSERVE NOMMÉE")
    E0 = 1795708000
    seuil_s = DELAI_REMPART_S
    cas = (("une seconde avant le seuil, machine qui tourne (cas sain)", (E0, E0 + seuil_s - 1, "tourne", None)),
           ("au seuil, machine qui tourne (artefact : la minuterie a fait défaut)", (E0, E0 + seuil_s, "tourne", None)),
           ("après le seuil, machine absente (cas sain : la minuterie a détruit)", (E0, E0 + seuil_s, "absente", None)),
           ("après le seuil, machine à l'arrêt avant cette règle", (E0, E0 + seuil_s, "arret", None)),
           ("arrêtée par cette règle depuis 1 h 59", (E0, E0 + seuil_s + 100 + 7199, "arret", E0 + seuil_s + 100)),
           ("arrêtée par cette règle depuis 2 h", (E0, E0 + seuil_s + 100 + 7200, "arret", E0 + seuil_s + 100)),
           ("état illisible (artefact)", (E0, E0 + seuil_s, "running", None)),
           ("instant d'arrêt placé dans le futur (artefact)", (E0, E0 + seuil_s + 100, "arret", E0 + seuil_s + 200)))
    ligne(30, "second rempart, règle de l'exécutante, échéance " + str(E0) + ", seuil " + str(E0 + seuil_s) + ", " + str(len(cas)) + " cas : " + " ; ".join(f"{nom} : code {second_rempart(*args)[0]}, « {second_rempart(*args)[1]} »" for nom, args in cas))
    etal_pire = BORNE_ETALONNAGE_H * PRIX_BORNE + TELECHARGEMENT_BORNE
    ligne(31, f"crédit relu après la recharge de 30 USD (GO-2026-11-22-77) : {CREDIT_RELU_USD:.2f} USD ; pire de la machine de l'étalonnage, échéance à {BORNE_ETALONNAGE_H:g} h : "
              f"{BORNE_ETALONNAGE_H:g} × {PRIX_BORNE:.2f} + {TELECHARGEMENT_BORNE:.2f} = {etal_pire:.2f} USD : couvert : {'oui' if CREDIT_RELU_USD >= etal_pire else 'NON'} ; "
              f"dépense au-delà de ce crédit : attendu {max(0.0, a['etal'] + a['c12'] - CREDIT_RELU_USD):.2f} ; haut {max(0.0, h['etal'] + h['c12'] - CREDIT_RELU_USD):.2f} ; pire {pire - CREDIT_RELU_USD:.2f} USD")
    reste = (BORNE_COURSE_H * HEURE + DELAI_REMPART_S + GESTE_S + FENETRE_RAPATRIEMENT_S)
    ligne(32, f"ligne de session de l'exécutante (GO-2026-11-22-94), dernier jour 2026-11-25, fin 2026-11-26T00:00:00Z = {FIN_SESSION_S} ; le second rempart d'une course à l'échéance de {BORNE_COURSE_H:g} h "
              f"demande l'exécutante jusqu'à {DELAI_REMPART_S + GESTE_S + FENETRE_RAPATRIEMENT_S} s après l'échéance ({DELAI_REMPART_S} + {GESTE_S} + {FENETRE_RAPATRIEMENT_S}), soit {reste / HEURE:.2f} h après la création : création au plus tard à {int(FIN_SESSION_S - reste)} = {datetime.datetime.fromtimestamp(int(FIN_SESSION_S - reste), datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, sinon mot de Lazar avant la création")
    A0 = E0 + seuil_s + 100
    cas_noeud = (("deux heures après l'arrêt, le code 7 vient d'être rendu (cas sain)", (A0, A0 + FENETRE_RAPATRIEMENT_S)),
                 ("une seconde avant l'arrêt plus 24 h (cas sain)", (A0, A0 + NOEUD_RELANCE_H * 3600 - 1)),
                 ("à l'arrêt plus 24 h, sans mot de Lazar", (A0, A0 + NOEUD_RELANCE_H * 3600)),
                 ("une seconde avant l'arrêt plus 36 h, sans mot de Lazar", (A0, A0 + NOEUD_HORS_DEVIS_H * 3600 - 1)),
                 ("à l'arrêt plus 36 h, sans mot de Lazar", (A0, A0 + NOEUD_HORS_DEVIS_H * 3600)),
                 ("une heure après l'arrêt, avant tout code 7 (artefact)", (A0, A0 + 3600)),
                 ("instant d'arrêt placé dans le futur (artefact)", (A0 + 200, A0 + 100)))
    t24, t33, t36 = (total_gardee_a_l_arret(x) for x in (NOEUD_RELANCE_H, NOEUD_BORNE_H, NOEUD_HORS_DEVIS_H))
    ligne(33, f"borne horaire du nœud porté à Lazar après un code 7 (machine gardée à l'arrêt, {a_l_arret:.2f} USD à l'arrêt, puis {STOCKAGE_BORNE:.2f} USD par heure, [M29] (b bis)) : "
              f"à l'arrêt plus {NOEUD_RELANCE_H} h, {t24:.2f} USD : la mère relance Lazar ; "
              f"à l'arrêt plus {NOEUD_BORNE_H} h, {t33:.2f} USD, sous le pire annoncé de {pire:.2f} USD : {'oui' if t33 <= pire else 'NON'} : instant porté au nœud ; "
              f"à l'arrêt plus {NOEUD_HORS_DEVIS_H} h, {t36:.2f} USD, sous le plafond de {PLAFOND:g} USD : {'oui' if t36 <= PLAFOND else 'NON'} : le passage du plafond, qui vient après {h_sous_plafond:.1f} h d'arrêt, "
              f"est déclaré comme dépense hors devis ; aucun de ces instants n'ordonne une destruction ; règle `borne-du-noeud`, arrêt {A0}, {len(cas_noeud)} cas : "
              + " ; ".join(f"{nom} : code {borne_du_noeud(*args)[0]}, « {borne_du_noeud(*args)[1].split(' ; ')[0]} »" for nom, args in cas_noeud)
              + f" ; instants rendus pour cet arrêt : « {borne_du_noeud(A0, A0 + FENETRE_RAPATRIEMENT_S)[1].split(' ; ', 1)[1]} »")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
