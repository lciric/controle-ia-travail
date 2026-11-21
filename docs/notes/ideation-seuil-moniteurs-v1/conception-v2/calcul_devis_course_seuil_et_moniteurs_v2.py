#!/usr/bin/env python3
"""Calcul du devis de la course « seuil et moniteurs », option (b) : l'étage des tests de mort seul — v2.

Arithmétique seule : aucun fichier lu, aucun réseau, aucun aléa. La sortie (JSON, clés triées) va sur la sortie standard.
Le programme v1 (ea47f6ee…) reste intact ; celui-ci ne garde de lui que les coûts réels de la course v9 et le facteur du haut
de la proposition. Les entrées marquées « règle du rédacteur » ou « supposé » ne sont mesurées nulle part.

Usage : python3 -B calcul_devis_course_seuil_et_moniteurs_v2.py > SORTIE.json
"""
import json
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR

D = Decimal
CENT = D("0.01")
MILLION = D("1000000")


def arrondi(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def texte(x):
    return format(arrondi(x), "f")


SOURCES = {
    "S1": "coûts réels des proposeurs de la course v9 (4,17 ; 4,75 ; 7,43 ; 17,58 ; 24,72 ; onze appels chacun) : devis v6 de "
          "la course « nouvelles attaques » (d825cb31…), § 1, ligne S1",
    "S2": "facteur du cas haut de la proposition, 1,1940 : préenregistrement court v9 de la course « nouvelles attaques » "
          "(864f39a7…), section « Seuil »",
    "S3": "prix par million de jetons, entrée et sortie, bornes de la table du collisionneur v9 v3 (850df311…), lignes 100 à "
          "141 : le plus haut 10 et 50, le plus bas des espèces présentes 4 et 20 ; garde de 2,5 caractères par jeton",
    "S4": "plafond indicatif de 120 : registre des accords, GO-2026-11-21-16",
    "R1": "règle du rédacteur : expérimentateur, deux sessions au plus par unité, plafond de session 3,00 (au-dessus du coût "
          "réel le plus haut d'un appel de proposeur fois le facteur du haut, 2,68) ; cas bas = une session au coût réel "
          "moyen d'un appel ; cas haut = deux sessions au coût réel le plus haut fois le facteur du haut",
    "R2": "règle du rédacteur : machine jetable du bac, 2 au cas bas, 5 au cas haut, 10 de plafond ; seule source « quelques "
          "dollars » (registre, R-3984)",
    "R3": "supposé : quatorze textes sources (dix cellules du collisionneur, trois consultations, un texte du moniteur de "
          "dissonance) ; à remplacer par le compte de la mère",
    "R4": "règle du rédacteur : mise en fiches par deux traducteurs, un appel par texte et par traducteur, plus deux textes "
          "témoins ; entrée gardée à 60 000 caractères, sortie plafonnée à 8 000 jetons",
}

PLAFOND_INDICATIF = D("120")

# ---------- expérimentateur ----------
PROPOSEURS_REEL = [D("4.17"), D("4.75"), D("7.43"), D("17.58"), D("24.72")]
APPELS_PAR_PROPOSEUR = 11
FACTEUR_HAUT_PROPOSITION = D("1.1940")
CANDIDATES = 11
TEMOINS_ETAGE = 3
SESSIONS_MAX = 2
PLAFOND_SESSION = D("3.00")

unites = CANDIDATES + TEMOINS_ETAGE
cout_moyen_appel = sum(PROPOSEURS_REEL) / (APPELS_PAR_PROPOSEUR * len(PROPOSEURS_REEL))
cout_max_appel = max(PROPOSEURS_REEL) / APPELS_PAR_PROPOSEUR
session_haut = cout_max_appel * FACTEUR_HAUT_PROPOSITION
etage = {"bas": unites * cout_moyen_appel,
         "haut": unites * SESSIONS_MAX * session_haut,
         "pire": unites * SESSIONS_MAX * PLAFOND_SESSION}


# ---------- règle de réservation (contre-lecture de la v1, § 1, point 4) ----------
# Une unité ne part que si son pire tient dans ce qui reste du plafond de l'étage. On compte combien d'unités partent quand
# chacune coûte un coût donné, et le plus petit plafond qui les laisse toutes partir : (n − 1) × coût + pire d'une unité.
def unites_qui_partent(n, cout_unite, pire_unite, plafond):
    depense, parties = D("0"), 0
    for _ in range(n):
        if depense + pire_unite > plafond:
            break
        depense += cout_unite
        parties += 1
    return parties, depense


def plafond_pour_toutes(n, cout_unite, pire_unite):
    return (n - 1) * cout_unite + pire_unite


PIRE_UNITE = SESSIONS_MAX * PLAFOND_SESSION
HAUT_UNITE = SESSIONS_MAX * session_haut
PLAFOND_ETAGE = etage["pire"]
parties_haut, depense_haut = unites_qui_partent(unites, HAUT_UNITE, PIRE_UNITE, PLAFOND_ETAGE)
parties_pire, depense_pire = unites_qui_partent(unites, PIRE_UNITE, PIRE_UNITE, PLAFOND_ETAGE)
# Contrôle : la même fonction rend les chiffres de la contre-lecture pour la v1 (vingt candidates à 110 ; dix à 55).
V1_HAUT_UNITE = 2 * cout_max_appel * FACTEUR_HAUT_PROPOSITION
V1_PIRE_UNITE = D("12.10")
v1_parties_20, v1_depense_20 = unites_qui_partent(20, V1_HAUT_UNITE, V1_PIRE_UNITE, D("110"))
v1_parties_10, _ = unites_qui_partent(10, V1_HAUT_UNITE, V1_PIRE_UNITE, D("55"))

# ---------- mise en fiches ----------
TEXTES_SOURCES = 14
TEXTES_TEMOINS = 2
TRADUCTEURS = 2
CAR_PAR_JETON = D("2.5")
ENTREE_GARDEE_CAR = D("60000")
ENTREE_BAS_CAR = D("25000")
SORTIE = {"bas": D("4000"), "haut": D("6000"), "pire": D("8000")}
PRIX_HAUT = (D("10"), D("50"))
PRIX_BAS = (D("4"), D("20"))

appels_traduction = (TEXTES_SOURCES + TEXTES_TEMOINS) * TRADUCTEURS


def appel(car, sortie, prix):
    return car / CAR_PAR_JETON / MILLION * prix[0] + sortie / MILLION * prix[1]


par_appel = {"bas": appel(ENTREE_BAS_CAR, SORTIE["bas"], PRIX_BAS),
             "haut": appel(ENTREE_GARDEE_CAR, SORTIE["haut"], PRIX_HAUT),
             "pire": appel(ENTREE_GARDEE_CAR, SORTIE["pire"], PRIX_HAUT)}
traduction = {k: appels_traduction * v for k, v in par_appel.items()}

# ---------- machine ----------
MACHINE = {"bas": D("2"), "haut": D("5"), "pire": D("10")}

total = {k: etage[k] + traduction[k] + MACHINE[k] for k in ("bas", "haut", "pire")}
marge = PLAFOND_INDICATIF - total["pire"]
unites_de_plus = int((marge / (SESSIONS_MAX * PLAFOND_SESSION)).to_integral_value(rounding=ROUND_FLOOR))


def trois(d):
    return {k: texte(v) for k, v in d.items()}


sortie = {
    "piece": "calcul-devis-course-seuil-et-moniteurs-v2",
    "unite": "USD",
    "sources": SOURCES,
    "regime": {"generations": 0, "etages_de_tests_de_mort": 1, "proposeurs": 0, "juges": 0,
               "candidates": CANDIDATES, "temoins_de_l_etage": TEMOINS_ETAGE, "unites_jouees": unites,
               "sessions_au_plus_par_unite": SESSIONS_MAX, "textes_sources_supposes": TEXTES_SOURCES,
               "textes_temoins_de_la_mise_en_fiches": TEXTES_TEMOINS, "traducteurs": TRADUCTEURS,
               "appels_de_mise_en_fiches": appels_traduction},
    "etage_des_tests_de_mort": dict(trois(etage),
                                    cout_reel_moyen_d_un_appel_de_proposeur=texte(cout_moyen_appel),
                                    session_au_cas_haut=texte(session_haut),
                                    plafond_de_session=texte(PLAFOND_SESSION),
                                    pire_par_unite=texte(SESSIONS_MAX * PLAFOND_SESSION),
                                    toutes_les_unites_tiennent_au_pire=True),
    "regle_de_reservation": {
        "regle": "une unité ne part que si son pire tient dans ce qui reste du plafond de l'étage",
        "plafond_de_l_etage": texte(PLAFOND_ETAGE),
        "unites_qui_partent_au_cas_haut": parties_haut, "depense_au_cas_haut": texte(depense_haut),
        "unites_qui_partent_si_tout_va_au_pire": parties_pire, "depense_si_tout_va_au_pire": texte(depense_pire),
        "plafond_qu_il_faut_pour_toutes_au_cas_haut": texte(plafond_pour_toutes(unites, HAUT_UNITE, PIRE_UNITE)),
        "plafond_qu_il_faut_pour_toutes_au_pire": texte(plafond_pour_toutes(unites, PIRE_UNITE, PIRE_UNITE)),
        "controle_sur_la_v1": {"vingt_candidates_a_110_partent": v1_parties_20, "depense": texte(v1_depense_20),
                               "plafond_pour_les_vingt": texte(plafond_pour_toutes(20, V1_HAUT_UNITE, V1_PIRE_UNITE)),
                               "dix_candidates_a_55_partent": v1_parties_10,
                               "plafond_pour_les_dix": texte(plafond_pour_toutes(10, V1_HAUT_UNITE, V1_PIRE_UNITE)),
                               "attendus_de_la_contre_lecture": "19 ; 101,96 ; 114,07 ; 8 ; 60,40"}},
    "mise_en_fiches": dict(trois(traduction), par_appel=trois(par_appel)),
    "machine_jetable_du_bac": trois(MACHINE),
    "total": trois(total),
    "ligne_de_calcul_a_demander": texte(total["pire"]),
    "plafond_indicatif": texte(PLAFOND_INDICATIF),
    "marge_sous_le_plafond_indicatif": texte(marge),
    "candidates_de_plus_que_la_marge_paierait_au_pire": unites_de_plus,
    "par_candidate_de_plus": {"bas": texte(cout_moyen_appel), "haut": texte(SESSIONS_MAX * session_haut),
                              "pire": texte(SESSIONS_MAX * PLAFOND_SESSION)},
    "controles": {"total_au_pire_sous_le_plafond_indicatif": total["pire"] <= PLAFOND_INDICATIF,
                  "plafond_de_session_au_dessus_de_la_session_au_cas_haut": PLAFOND_SESSION >= session_haut},
}

print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))
