#!/usr/bin/env python3
"""Arithmétique du devis de la voie (A) du saboteur à budget, version 5, sous la ligne GO-2026-11-22-75 — v2.

Remplace, pour la voie (A), `calcul-devis-voies-A-B-v1.py` (intact, R12). Bibliothèque standard seule.
Sans argument : imprime toutes les lignes [Mnn] citées par le devis et l'additif de la voie (A), brouillons 2.
Trois sous-commandes portent des règles écrites d'avance, jouées par l'exécutante sans rien lire d'une sortie de mesure :

    rythme-etalonnage COUPURE_USD COMPTE_USD
        essai de vitesse en tête de l'étalonnage : délai, compté depuis la marque de début de l'étalonnage, au-delà duquel
        l'absence de la marque du lot 2 commande l'arrêt par l'identifiant.
    echeance COUPURE_USD COMPTE_USD MAINTENANT_S BORNE_H MINIMUM_H
        échéance de la minuterie d'une machine : min(fin de la voie, maintenant + H), H = min(BORNE_H, (coupure − compte −
        forfait de téléchargement à la borne) / prix borne) ; H < MINIMUM_H : « AUCUNE CREATION » (code 3).
    garde-de-rythme COUPURE_USD COMPTE_USD TOURS MAINTENANT_S MINUTES_ETALONNAGE
        course : refus de la création si la course, au rythme relevé de l'étalonnage plus la tolérance, ne tient pas dans les
        heures de son échéance ; sinon délais au-delà desquels l'absence de la marque du tour 1, puis du tour 4, commande l'arrêt.

Aucune donnée mesurée de l'expérience n'est lue : seulement des durées, des prix et des comptes, cités avec leur source.
"""
from __future__ import annotations

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
CREDIT_USD = 12.995                                 # [S5]
PLAFOND, COUPURE = 60.0, 55.0                       # [S6] ; coupure : celle de la configuration, exigée à l'égalité par le code
FIN_DE_VOIE_S = 1796076000                          # 2026-11-30T22:00:00Z, échéance de la minuterie de l'ordre scellé
ENTREES = {"plafond": 45.0, "depense_passee": 0.0, "cout_fixe": 6.90, "prix": PRIX_BORNE, "hors_tours": 3830}   # [S7]
ARRET_AVANT_DESTRUCTION_H = 6.0                     # machine à l'arrêt entre sa fin normale et sa destruction (hypothèse)
TOLERANCE = 1.2                                     # la course comptée 20 % plus lente que l'étalonnage (maître jamais chronométré)
MARGE_DE_MARQUE_H = 0.10                            # tolérance sur l'heure d'une marque de progrès
BORNE_COURSE_H = 30.0
DECLAREE_MAX = 5.00                                 # garde du lanceur : 55 + dépense antérieure ≤ 60

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
    declaree = min(compte, DECLAREE_MAX)
    return 0, (f"ECHEANCE_UTC_S={ech} ({borne} ; dépense de la machine tenue à {(ech - maintenant_s) / HEURE * PRIX_BORNE + TELECHARGEMENT_BORNE:.2f} USD au plus) ; "
               f"dépense antérieure à déclarer : {math.ceil(declaree * 100 - 1e-9) / 100:.2f} (compte {compte:.2f})")


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
    ligne(5, f"ligne GO-2026-11-22-75 : plafond {PLAFOND:g} USD, dépense neuve ; coupure {COUPURE:g} USD (configuration) ; crédit chez le loueur le 22 novembre à 14:11Z : {CREDIT_USD:.3f} USD")

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
    e3 = echeance(COUPURE, 4.20, 1795600000, BORNE_COURSE_H, 11.0)
    ligne(24, f"règle de l'échéance, cas sain (compte attendu {a['etal']:.2f} USD) : code {e1[0]}, « {e1[1]} »")
    ligne(25, f"règle de l'échéance, cas sain (compte 4,20 USD, sous 5) : code {e3[0]}, « {e3[1]} »")
    ligne(26, f"règle de l'échéance, artefact (compte 50 USD) : code {e2[0]}, « {e2[1]} »")
    ligne(27, f"épuisement calculé par le lanceur à 5 USD déclarés, forfait à la borne : (55 − 5 − 2) / 1,38 = {(55 - 5 - 2) / PRIX_BORNE:.2f} h, au-delà de la borne de {BORNE_COURSE_H:g} h de l'échéance")
    ligne(28, f"dates : échéance de la minuterie au plus tard 2026-11-30T22:00:00Z = {FIN_DE_VOIE_S} ; fin de la ligne 2026-12-01T00:00:00Z = {FIN_DE_VOIE_S + 7200} ; "
              f"aucune création à partir de 2026-11-27T00:00:00Z = 1795737600")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
