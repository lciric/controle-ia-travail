#!/usr/bin/env python3
"""Recalcul independant du devis v3 de la course « nouvelles attaques » a six especes - v1.

Contre-lecteur neuf, modele O. Ecrit sans reprendre le code du redacteur : arithmetique exacte par
fractions (fractions.Fraction), arrondi au centime seulement a l'affichage, enumeration propre des
repartitions. Les constantes viennent des pieces lues, citees a cote de chaque constante :
  S1  devis de l'heritage v5, § 1 (recopie par le devis v2, § 1) ;
  S3  devis v2i de la course d'auto-conception, § 1 a § 4 (idem) ;
  P3  preenregistrement court v3 (2ea5ad53...), section « Seuil » ;
  GO  registres/go.md (GO-2026-11-20-16, -22, -34) ; R   registres/decisions.md (R-813, R-1780).
Processeur seul : aucun appel, aucun reseau, aucune lecture de fichier.
Usage : python3 -B recalcul_contre_lecteur_devis_v3_v1.py SORTIE.json   (refuse d'ecraser)
"""
import itertools
import json
import sys
from fractions import Fraction as F

# --- constantes ---------------------------------------------------------------------------
PROP = {1: F("4.17"), 2: F("4.75"), 3: F("7.43"), 4: F("17.58"), 5: F("24.72")}  # S1, par generation
AIG = F("4.59")                    # S1, aiguilleur, par generation
JUGE = {3: F("6.86"), 1: F("2.41")}  # S1, juges des especes 3 et 1
FICHES_V9_GEN = 94                 # S1, tentatives attendues a cinq especes
HAUT_V2I = {"prop": F("70.03"), "aig": F("20.46"), "juges": F("47.32")}  # S3, cas haut par etape
PIRE_APPEL = F("6.05")             # S3, pire d'un appel de proposeur
APPELS_PAR_ESPECE = 11
GEN = 3
TEMOINS_EST, TEMOINS_PLAF = F("1.18"), F(5)
SONDE15_PLAF, SONDE6_PLAF = F(1), F("0.01")
SONDE_TROIS_MODELES = F("0.005")   # S4
ECARTS = {"dur_prop": F(10), "aig": F(15), "juges": F(30)}  # S3 : 150 -> 140, 135, 120
# soldes (P3) : Minuit calcule, Luc declare, Rigaud calcule avant la recharge ; X (GO-22)
MINUIT = F(200) - F("0.000108") - F("0.980399") - F("36.457056")
LUC = F(214)
RIGAUD_AVANT = F(47)
X = F("8.35")
# repere de tarif de l'espece 6 (R-813, R-1780), USD par million de jetons, entree et sortie
TARIF_E, TARIF_S = F(2), F(10)
OCTETS_QUESTION = 10562            # wc -c de la question scellee (2cf2aae0...)


def cent(x):
    """Arrondi au centime, demi vers le haut, rendu en texte."""
    q = (x * 100)
    n = int(q) if q >= 0 else -int(-q)
    if q - n >= F(1, 2):
        n += 1
    return "%d.%02d" % (n // 100, n % 100)


def dec(x, k=4):
    m = 10 ** k
    q = x * m
    n = int(q)
    if q - n >= F(1, 2):
        n += 1
    return str(n // m) + "." + str(n % m).zfill(k)


def ceil5(x):
    n = -((-x) // 5)
    return n * 5


f_prop = HAUT_V2I["prop"] / sum(PROP.values())
f_aig = HAUT_V2I["aig"] / AIG
f_jug = HAUT_V2I["juges"] / sum(JUGE.values())


def generation(n_especes_v9, avec_espece_6):
    """Couts par role et par generation (bas, haut)."""
    esp = list(range(1, n_especes_v9 + 1))
    n_appels = APPELS_PAR_ESPECE * (len(esp) + (1 if avec_espece_6 else 0))
    pr = F(n_appels, APPELS_PAR_ESPECE * 5)
    bas, haut = {}, {}
    for e in esp:
        bas["p%d" % e] = PROP[e]
        haut["p%d" % e] = PROP[e] * f_prop
    if avec_espece_6:
        bas["p6"] = sum(PROP.values()) / 5
        haut["p6"] = max(PROP.values()) * f_prop
    bas["aig"], haut["aig"] = AIG * pr, AIG * pr * f_aig
    for j in (3, 1):
        bas["j%d" % j], haut["j%d" % j] = JUGE[j] * pr, JUGE[j] * pr * f_jug
    return bas, haut, pr, n_appels


def etapes(d):
    prop = sum(v for k, v in d.items() if k.startswith("p"))
    jug = d["j3"] + d["j1"]
    return prop, d["aig"], jug


def lecture_seuils(plafond, haut):
    prop, aig, jug = etapes(haut)
    s_dur, s_aig, s_jug = plafond - ECARTS["dur_prop"], plafond - ECARTS["aig"], plafond - ECARTS["juges"]
    aig_lance = prop <= s_aig
    jug_lances = aig_lance and (prop + aig) <= s_jug
    depense = prop + (aig if aig_lance else 0) + (jug if jug_lances else 0)
    return {
        "plafond": str(plafond), "plafond_dur_proposition": str(s_dur), "seuil_aiguillage": str(s_aig),
        "seuil_juges": str(s_jug), "proposition_sous_plafond_dur": prop <= s_dur,
        "aiguillage_lance": aig_lance, "cumul_avant_juges": cent(prop + aig), "juges_lances": jug_lances,
        "depense_au_haut_avec_les_seuils": cent(depense), "depense_sous_le_plafond": depense <= plafond,
        "haut_complet_juges_compris": cent(prop + aig + jug),
        "reste_pour_les_juges_au_haut": cent(plafond - prop - aig), "juges_au_haut": cent(jug),
    }


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : recalcul_contre_lecteur_devis_v3_v1.py SORTIE.json\n")
        return 2
    b6, h6, pr6, appels6 = generation(5, True)
    b5, h5, _, _ = generation(5, False)
    bas_gen, haut_gen = sum(b6.values()), sum(h6.values())
    bas5, haut5 = sum(b5.values()), sum(h5.values())
    regle_marge = ceil5(haut_gen * F(105, 100))
    p6, a6, j6 = etapes(h6)
    regle_juges = ceil5(p6 + a6 + ECARTS["juges"])
    plafond = max(regle_marge, regle_juges)
    ligne = plafond * GEN
    plafonds_part = TEMOINS_PLAF + SONDE15_PLAF + SONDE6_PLAF
    sonde15_est = SONDE_TROIS_MODELES / 3 * 5
    sonde6_est = SONDE_TROIS_MODELES / 3
    total_bas = bas_gen * GEN + TEMOINS_EST + sonde15_est + sonde6_est
    total_haut = haut_gen * GEN + plafonds_part
    total_plafond = ligne + plafonds_part
    pire_prop_course = APPELS_PAR_ESPECE * PIRE_APPEL * GEN

    # par cle, sur la course
    roles_cle = {"Minuit": ["j3"], "Luc": ["aig", "p4"], "Rigaud": ["p3"],
                 "relais_2": ["j1", "p1", "p5"], "relais_3": ["p2"], "cle_espece_6": ["p6"]}
    parts = {"Minuit": MINUIT, "Luc": LUC, "Rigaud": RIGAUD_AVANT - X}
    par_cle = {}
    for c, rs in roles_cle.items():
        bb = sum(b6[r] for r in rs) * GEN
        hh = sum(h6[r] for r in rs) * GEN
        e = {"roles": rs, "bas": cent(bb), "haut": cent(hh)}
        if c in parts:
            e["part_avant_recharge"] = cent(parts[c])
            e["rapport_part_sur_haut"] = dec(parts[c] / hh, 3)
            e["marge_usd_au_haut"] = cent(parts[c] - hh)
        par_cle[c] = e
    # par espece
    par_espece = {}
    for n in range(1, 7):
        rs = ["p%d" % n] + (["j%d" % n] if n in (1, 3) else [])
        par_espece[str(n)] = {"bas": cent(sum(b6[r] for r in rs) * GEN), "haut": cent(sum(h6[r] for r in rs) * GEN)}
    par_espece["aiguilleur"] = {"bas": cent(b6["aig"] * GEN), "haut": cent(h6["aig"] * GEN)}

    # roles Claude
    claude = ["j3", "aig", "p4", "p3"]
    h_claude6 = {r: h6[r] * GEN for r in claude}
    h_claude5 = {r: h5[r] * GEN for r in claude}
    borne = sum(parts.values())
    # regle de choix : maximiser le plus petit rapport part / charge, chaque cle tenant sa charge au haut
    resultats = []
    for aff in itertools.product(["Minuit", "Luc", "Rigaud"], repeat=len(claude)):
        charge = {"Minuit": F(0), "Luc": F(0), "Rigaud": F(0)}
        for r, c in zip(claude, aff):
            charge[c] += h_claude6[r]
        if any(charge[c] > parts[c] for c in charge):
            continue
        mini = min(parts[c] / charge[c] for c in charge if charge[c] > 0)
        resultats.append((mini, dict(zip(claude, aff))))
    meilleur = max(m for m, _ in resultats)
    retenue = {"j3": "Minuit", "aig": "Luc", "p4": "Luc", "p3": "Rigaud"}
    mini_retenue = [m for m, d in resultats if d == retenue][0]

    # variante : plafond de 150 garde a six especes
    variante = lecture_seuils(F(150), h6)
    variante["ligne"] = str(150 * GEN)
    variante["plafond_total"] = cent(150 * GEN + plafonds_part)
    variante["marge_plafond_sur_bas"] = dec(F(150) / bas_gen, 2)

    # sonde de l'espece 6 et pire par appel, au repere de tarif
    jetons_entree_pour_un_centime = SONDE6_PLAF / TARIF_E * 10 ** 6
    entree_au_pire_un_jeton_par_octet = F(OCTETS_QUESTION) * TARIF_E / 10 ** 6

    sortie = {
        "piece": "recalcul independant du devis v3, contre-lecteur neuf, modele O, v1",
        "facteurs_du_haut": {"proposition": dec(f_prop), "aiguillage": dec(f_aig), "juges": dec(f_jug)},
        "prorata_six_especes": dec(pr6), "appels_de_proposeur_par_generation": appels6,
        "par_generation": {
            "bas": cent(bas_gen), "haut": cent(haut_gen),
            "bas_etapes": [cent(x) for x in etapes(b6)], "haut_etapes": [cent(x) for x in etapes(h6)],
            "regle_marge": str(regle_marge), "regle_juges": str(regle_juges), "plafond": str(plafond),
            "marge_plafond_sur_bas": dec(F(plafond) / bas_gen, 2),
            "pire_des_appels_de_proposeur": cent(appels6 * PIRE_APPEL),
        },
        "seuils_au_plafond_retenu": lecture_seuils(F(plafond), h6),
        "course": {"bas": cent(bas_gen * GEN), "haut": cent(haut_gen * GEN), "ligne": str(ligne)},
        "total": {"bas": cent(total_bas), "haut": cent(total_haut), "plafond_total": cent(total_plafond)},
        "cinq_especes_controle": {"bas_gen": cent(bas5), "haut_gen": cent(haut5),
                                  "total_bas": cent(bas5 * GEN + TEMOINS_EST + sonde15_est),
                                  "total_haut": cent(haut5 * GEN + TEMOINS_PLAF + SONDE15_PLAF)},
        "ecarts_a_cinq": {"attendu": cent(total_bas - (bas5 * GEN + TEMOINS_EST + sonde15_est)),
                          "haut_total": cent(total_haut - (haut5 * GEN + TEMOINS_PLAF + SONDE15_PLAF)),
                          "plafond_total": cent(total_plafond - (450 + TEMOINS_PLAF + SONDE15_PLAF))},
        "espece_6": {"bas_gen": cent(b6["p6"]), "haut_gen": cent(h6["p6"]), "pire_gen": cent(APPELS_PAR_ESPECE * PIRE_APPEL),
                     "bas_course": cent(b6["p6"] * GEN), "haut_course": cent(h6["p6"] * GEN),
                     "pire_course": cent(pire_prop_course)},
        "par_espece_course": par_espece,
        "par_cle_course": par_cle,
        "claude": {"somme_bas_six": cent(sum(b6[r] for r in claude) * GEN), "somme_haut_six": cent(sum(h_claude6.values())),
                   "somme_haut_cinq": cent(sum(h_claude5.values())), "borne_avant_recharge": cent(borne),
                   "borne_sur_haut_six": dec(borne / sum(h_claude6.values()), 3),
                   "borne_sur_haut_cinq": dec(borne / sum(h_claude5.values()), 3),
                   "ligne_moins_borne_six": cent(ligne - borne), "ligne_moins_borne_cinq": cent(450 - borne),
                   "ligne_moins_somme_des_soldes_sans_X": cent(ligne - (MINUIT + LUC + RIGAUD_AVANT)),
                   "repartitions_admissibles": len(resultats), "meilleur_plus_petit_rapport": dec(meilleur),
                   "retenue_plus_petit_rapport": dec(mini_retenue), "retenue_au_meilleur": mini_retenue == meilleur,
                   "ex_aequo": [d for m, d in resultats if m == meilleur],
                   "solde_rigaud_minimal_pour_tenir_le_haut": cent(h_claude6["p3"] + X),
                   "solde_rigaud_pour_tenir_le_pire_du_role": cent(pire_prop_course + X)},
        "variante_150": variante,
        "recommandation_151": cent(HAUT_V2I["prop"] + h6["aig"] + h6["j3"] + h6["j1"]),
        "reperes_tarif_espece_6": {
            "jetons_de_sortie_que_vaut_6_05": str(int(PIRE_APPEL / TARIF_S * 10 ** 6)),
            "jetons_d_entree_que_vaut_0_01": str(int(jetons_entree_pour_un_centime)),
            "entree_de_la_question_a_un_jeton_par_octet_usd": dec(entree_au_pire_un_jeton_par_octet, 6),
            "jetons_par_octet_maximum_pour_tenir_0_01_sans_sortie": dec(jetons_entree_pour_un_centime / OCTETS_QUESTION, 3),
            "bas_par_appel_espece_6_usd": dec(b6["p6"] / APPELS_PAR_ESPECE, 4),
            "attendu_si_la_sonde_6_est_estimee_au_pire_par_octet": cent(total_bas - sonde6_est + entree_au_pire_un_jeton_par_octet),
        },
    }
    with open(argv[1], "x", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
