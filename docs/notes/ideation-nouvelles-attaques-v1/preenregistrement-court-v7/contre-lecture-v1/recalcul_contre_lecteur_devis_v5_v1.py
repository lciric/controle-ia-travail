#!/usr/bin/env python3
"""Recalcul independant du devis v5 de la course « nouvelles attaques » - v1.

Contre-lecteur neuf, modele O. Fractions exactes ; arrondi au centime a l'affichage seulement, et deux
lectures des manques : « exact » (besoin et reste exacts, difference arrondie) et « affiche » (besoin et
reste arrondis au centime, puis difference), pour voir l'effet de l'ordre des arrondis.
Constantes : tailles lues par `wc -c` sur les pieces scellees de main (gabarit 2 957 ; synthese 32 260) ;
couts de la course v9 (S1) et cas haut v2i (S3) comme au devis ; restes nets estimes (62c625ab...) ;
repere de tarif de l'espece 6 (2 et 10 USD par million de jetons, R-813, R-1780).
Processeur seul ; aucune lecture de fichier.
Usage : python3 -B recalcul_contre_lecteur_devis_v5_v1.py SORTIE.json   (refuse d'ecraser)
"""
import json
import sys
from fractions import Fraction as F

PROP = {1: F("4.17"), 2: F("4.75"), 3: F("7.43"), 4: F("17.58"), 5: F("24.72")}
AIG, J3, J1 = F("4.59"), F("6.86"), F("2.41")
F_PROP = F("70.03") / sum(PROP.values())
F_AIG = F("20.46") / AIG
F_JUG = F("47.32") / (J3 + J1)
PR6 = F(66, 55)
GEN = 3
PIRE_APPEL = F("6.05")
LIGNE = F(570)
GABARIT, EMPLACEMENT, BORNE_LIGNE, SYNTHESE = 2957, 8, 256, 32260
TARIF_E, TARIF_S = F(2, 10 ** 6), F(10, 10 ** 6)
RESTE = {
    "Minuit": F(200) - F("0.000108") - F("0.980399") - F("36.457056"),
    "Luc": F("213.999998"),
    "Rigaud_registre": F("47.495696") - F("8.35"),
    "Rigaud_corrige": F("64.207482") - F("8.35"),
    "Rigaud_registre_lots45": F("47.495696") - F(45) - F("8.35"),
    "Rigaud_corrige_lots45": F("64.207482") - F(45) - F("8.35"),
    "espece6": F("32.24463"),
    "relais3_haut": F(30) - F("18.49368"),
    "relais3_bas": F(30) - F("18.49368") - F("2.6"),
}
COLLISIONNEUR_PIRE = {"espece6": F("6.58"), "relais3": F("15.63")}


def cent(x):
    s = -1 if x < 0 else 1
    q = abs(x) * 100
    n = int(q)
    if q - n >= F(1, 2):
        n += 1
    n *= s
    return ("-" if n < 0 else "") + "%d.%02d" % (abs(n) // 100, abs(n) % 100)


def r2(x):
    return F(cent(x))


def dec(x, k):
    m = 10 ** k
    q = x * m
    n = int(q)
    if q - n >= F(1, 2):
        n += 1
    return str(n // m) + "." + str(n % m).zfill(k)


def roles():
    bas = {"p%d" % e: PROP[e] * GEN for e in PROP}
    haut = {"p%d" % e: PROP[e] * F_PROP * GEN for e in PROP}
    bas["p6"] = sum(PROP.values()) / 5 * GEN
    haut["p6"] = max(PROP.values()) * F_PROP * GEN
    bas["aig"], haut["aig"] = AIG * PR6 * GEN, AIG * PR6 * F_AIG * GEN
    bas["j3"], haut["j3"] = J3 * PR6 * GEN, J3 * PR6 * F_JUG * GEN
    bas["j1"], haut["j1"] = J1 * PR6 * GEN, J1 * PR6 * F_JUG * GEN
    return bas, haut


def manque(besoin, reste):
    ex = besoin - reste
    af = r2(besoin) - r2(reste)
    return {"besoin": cent(besoin), "reste": cent(reste), "manque_exact": cent(max(ex, F(0))),
            "manque_affiche": cent(max(af, F(0))), "tient": ex <= 0}


def confrontation(sonde6):
    bas, haut = roles()
    pire_prop = 11 * PIRE_APPEL * GEN
    out = {}
    out["Minuit"] = {c: manque(v, RESTE["Minuit"]) for c, v in
                     (("bas", bas["j3"]), ("haut", haut["j3"]), ("pire", LIGNE))}
    out["Luc"] = {c: manque(v, RESTE["Luc"]) for c, v in
                  (("bas", bas["aig"] + bas["p4"]), ("haut", haut["aig"] + haut["p4"]), ("pire", LIGNE))}
    for k in ("Rigaud_registre", "Rigaud_corrige", "Rigaud_registre_lots45", "Rigaud_corrige_lots45"):
        out[k] = {c: manque(v, RESTE[k]) for c, v in (("bas", bas["p3"]), ("haut", haut["p3"]), ("pire", pire_prop))}
    out["espece6"] = {c: manque(v + sonde6, RESTE["espece6"]) for c, v in
                      (("bas", bas["p6"]), ("haut", haut["p6"]), ("pire", pire_prop))}
    for k in ("relais3_haut", "relais3_bas"):
        out[k] = {c: manque(v, RESTE[k]) for c, v in (("bas", bas["p2"]), ("haut", haut["p2"]), ("pire", pire_prop))}
    out["avec_collisionneur"] = {
        "espece6_bas": manque(bas["p6"] + sonde6 + COLLISIONNEUR_PIRE["espece6"], RESTE["espece6"]),
        "relais3_bas": manque(bas["p2"] + COLLISIONNEUR_PIRE["relais3"], RESTE["relais3_haut"]),
    }
    return out


def totaux(sonde6):
    bas, haut = roles()
    course_bas, course_haut = sum(bas.values()), sum(haut.values())
    a_part = F(5) + F(1) + sonde6
    return {"course_bas": cent(course_bas), "course_haut": cent(course_haut),
            "total_attendu": cent(course_bas + F("1.18") + F("0.005") / 3 * 5 + F("0.005") / 3),
            "total_haut": cent(course_haut + a_part), "plafond_total": cent(LIGNE + a_part),
            "ecart_plafond_total_a_456": cent(LIGNE + a_part - 456),
            "ecart_total_haut_a_419_43": cent(course_haut + a_part - F("419.43"))}


def sonde(plafond, octets):
    out = {}
    for nom, jetons in (("un_jeton_par_octet", F(octets)), ("2_5_octets_par_jeton", F(octets) / F(5, 2))):
        entree = jetons * TARIF_E
        reste = plafond - entree
        out[nom] = {"jetons_entree": dec(jetons, 0), "entree_usd": dec(entree, 6),
                    "sortie_max_jetons": str(int(reste / TARIF_S)) if reste > 0 else "aucune"}
    return out


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : recalcul_contre_lecteur_devis_v5_v1.py SORTIE.json\n")
        return 2
    remplie = GABARIT - EMPLACEMENT + BORNE_LIGNE
    requete = remplie + SYNTHESE
    bas, haut = roles()
    entree_appel = F(requete) * TARIF_E
    pire_permis = (RESTE["espece6"] - F("0.01")) / 33
    sortie = {
        "piece": "recalcul independant du devis v5, contre-lecteur neuf, modele O, v1",
        "tailles": {"partie_servie_remplie_au_plus": remplie, "requete_proposeur_g1_au_plus": requete},
        "sonde_espece6_0_01": sonde(F("0.01"), remplie),
        "sonde_espece6_0_05": sonde(F("0.05"), remplie),
        "sonde_espece6_avec_synthese_entree_usd": dec(F(requete) * TARIF_E, 6),
        "reperes_espece6": {
            "entree_par_appel": dec(entree_appel, 4), "entree_course": cent(entree_appel * 33),
            "sortie_8000": cent((entree_appel + 8000 * TARIF_S) * 33),
            "sortie_16000": cent((entree_appel + 16000 * TARIF_S) * 33),
            "sortie_32000": cent((entree_appel + 32000 * TARIF_S) * 33),
            "sortie_64000": cent((entree_appel + 64000 * TARIF_S) * 33),
            "pire_par_appel_permis": dec(pire_permis, 4),
            "sortie_permise_jetons": str(int((pire_permis - entree_appel) / TARIF_S)),
        },
        "totaux_sonde_0_01": totaux(F("0.01")),
        "totaux_sonde_0_05": totaux(F("0.05")),
        "confrontation_sonde_0_01": confrontation(F("0.01")),
        "confrontation_sonde_0_05": confrontation(F("0.05")),
        "cas_haut_exacts": {"p2": dec(haut["p2"], 5), "p3": dec(haut["p3"], 5), "p6": dec(haut["p6"], 5),
                            "j3": dec(haut["j3"], 5)},
    }
    with open(argv[1], "x", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
