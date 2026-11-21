"""Devis de l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — calcul v5.

Arithmétique seule : aucun tirage, aucun appel, aucun fichier lu. Sortie : un objet JSON sur la sortie standard.
Usage : python3 -B calcul_devis_auteur_mondes_plantes_v5.py > calcul-devis-auteur-mondes-plantes-v5.json

Le calcul v5 est le calcul v4 (bd219a4a857bba1535f5cbf39a576cfc2e7a0c86f0b5bf75f8580c343f04982e) réduit à son scénario
S2, que la mère a retenu : borne de sortie de 55 000 caractères, plafonds de sortie du devis v3. Les scénarios S0 et S1
ne sont plus calculés. Aucune formule ne change ; les nombres du scénario S2 sont les mêmes qu'au calcul v4.

Entrées et leurs sources (les candidats sont dits par relais, sans nom) :
- S3  : table des espèces du collisionneur v9 v3, docs/notes/collisionneur-v9/collisionneur_v9_v3.py sur origin/main,
        lignes 100 à 141, empreinte 850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910 :
        prix par million de jetons (entrée, sortie), plafond de sortie, plafond de relance, provision de réflexion,
        garde de 2,5 caractères par jeton. Valeurs reprises des calculs v2 à v4, sans changement.
- M1  : le texte servi, le mandat v3 avec son erratum 1 appliqué
        (2e675d74cfe035a16ac4e54fcbcae3855ceae9523816f8d1b3e04ebde3b46251) : 27 468 octets, borne haute de ses caractères.
- E1  : borne de sortie de l'erratum 1 du mandat, seconde passe
        (4dd1bb7fa869032ba4c94b74f5d1b54dbbba6462e4ad4aad65bb72b54ab32a38) : 55 000 caractères.
- R1  : règles du rédacteur : garde d'envoi à 30 000 caractères, deux essais au plus.
- R2  : premier essai de R2-a au plafond de relance, 32 000 jetons de sortie (devis v2).
- C1  : devis v3 de la course, scellé : 114,48 USD ; plafond indicatif de la course : 120 USD (GO-2026-11-21-16).
"""
import json
import sys
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal

MILLION = Decimal(1000000)
CENT = Decimal("0.01")
CAR_PAR_JETON = Decimal("2.5")          # S3
ENTREE_MESUREE_CAR = 27468              # M1
ENTREE_GARDE_CAR = 30000                # R1
SORTIE_BORNE_CAR = 55000                # E1
ESSAIS_MAX = 2                          # R1
COURSE_USD = Decimal("114.48")          # C1
PLAFOND_INDICATIF_USD = Decimal("120")  # C1
CANDIDAT_DE_LA_LIGNE = "R2-a"

# S3 et R2, comme aux calculs v3 et v4.
CANDIDATS = [
    {"id": "R2-a", "relais": "deuxième relais", "designation": "modèle au tarif lu sur page versée, compté en borne haute",
     "prix_compte": (10, 50), "prix_bas": (4, 20), "statut_tarif": "lu (page versée), compté en borne haute",
     "plafond_sortie": 18000, "plafond_relance": 32000, "provision": 8192, "plafond_essai_1": 32000},
    {"id": "R2-b", "relais": "deuxième relais", "designation": "modèle au tarif rapporté, réglages supposés",
     "prix_compte": (4, 20), "prix_bas": (4, 20), "statut_tarif": "rapporté, non lu sur page : à relever",
     "plafond_sortie": 65536, "plafond_relance": 65536, "provision": 32768, "plafond_essai_1": 65536},
    {"id": "R3", "relais": "troisième relais", "designation": "modèle unique du relais",
     "prix_compte": (10, 50), "prix_bas": (10, 50), "statut_tarif": "supposé égal au barème du modèle voisin : à relever",
     "plafond_sortie": 8000, "plafond_relance": 32000, "provision": 0, "plafond_essai_1": 32000},
]


def jetons(caracteres):
    return int((Decimal(caracteres) / CAR_PAR_JETON).to_integral_value(rounding=ROUND_CEILING))


def cout(jetons_entree, jetons_sortie, prix):
    return (Decimal(jetons_entree) * Decimal(prix[0]) + Decimal(jetons_sortie) * Decimal(prix[1])) / MILLION


def proche(x):
    return str(x.quantize(CENT, rounding=ROUND_HALF_UP))


def devis(c):
    entree_mesuree = jetons(ENTREE_MESUREE_CAR)
    entree_garde = jetons(ENTREE_GARDE_CAR)
    sortie_borne = jetons(SORTIE_BORNE_CAR)
    plafond_1 = c["plafond_essai_1"]
    plafond_2 = c["plafond_relance"]
    plus_petit_plafond = min(plafond_1, plafond_2)
    plus_grand_plafond = max(plafond_1, plafond_2)
    bas = cout(entree_mesuree, sortie_borne, c["prix_bas"])
    essai_1 = cout(entree_mesuree, plafond_1 + c["provision"], c["prix_compte"])
    essai_2 = cout(entree_mesuree, plafond_2 + c["provision"], c["prix_compte"])
    cas_haut = essai_1 + essai_2
    pire_par_essai = cout(entree_garde, plus_grand_plafond + c["provision"], c["prix_compte"])
    pire = pire_par_essai * ESSAIS_MAX
    plafond_par_essai = pire_par_essai.quantize(CENT, rounding=ROUND_CEILING)
    plafond = plafond_par_essai * ESSAIS_MAX
    reste_provision_dedans = plus_petit_plafond - c["provision"]
    total = COURSE_USD + plafond
    return {
        "id": c["id"],
        "relais": c["relais"],
        "statut_tarif": c["statut_tarif"],
        "plafond_essai_1_jetons": plafond_1,
        "plafond_essai_2_jetons": plafond_2,
        "provision_jetons": c["provision"],
        "sortie_bornee_jetons": sortie_borne,
        "provision_comptee_a_cote": {
            "la_sortie_bornee_tient": sortie_borne <= plus_petit_plafond,
            "marge_jetons": plus_petit_plafond - sortie_borne,
        },
        "provision_comptee_dedans": {
            "jetons_laisses_a_la_sortie": reste_provision_dedans,
            "la_sortie_bornee_tient": sortie_borne <= reste_provision_dedans,
            "marge_jetons": reste_provision_dedans - sortie_borne,
        },
        "cas_bas": {"essais": 1, "exact": str(bas), "usd": proche(bas)},
        "cas_haut": {"essais": 2, "essai_1": str(essai_1), "essai_2": str(essai_2), "exact": str(cas_haut),
                     "usd": proche(cas_haut)},
        "pire": {"essais": ESSAIS_MAX, "par_essai_exact": str(pire_par_essai), "exact": str(pire), "usd": proche(pire)},
        "plafond_d_arret_par_essai_usd": str(plafond_par_essai),
        "plafond_d_arret_usd": str(plafond),
        "plafond_tient_le_pire": plafond >= pire,
        "plafond_tient_le_cas_haut": plafond >= cas_haut,
        "total_avec_la_course_usd": str(total),
        "marge_sous_le_plafond_indicatif_usd": str(PLAFOND_INDICATIF_USD - total),
        "total_sous_le_plafond_indicatif": total <= PLAFOND_INDICATIF_USD,
    }


def main():
    lignes = [devis(c) for c in CANDIDATS]
    ligne = [l for l in lignes if l["id"] == CANDIDAT_DE_LA_LIGNE][0]
    sortie = {
        "version": "calcul-devis-auteur-mondes-plantes-v5",
        "entrees": {
            "caracteres_par_jeton": str(CAR_PAR_JETON),
            "entree_mesuree_caracteres": ENTREE_MESUREE_CAR,
            "entree_mesuree_jetons": jetons(ENTREE_MESUREE_CAR),
            "entree_garde_caracteres": ENTREE_GARDE_CAR,
            "entree_garde_jetons": jetons(ENTREE_GARDE_CAR),
            "entree_mesuree_tient_sous_la_garde": ENTREE_MESUREE_CAR <= ENTREE_GARDE_CAR,
            "marge_sous_la_garde_caracteres": ENTREE_GARDE_CAR - ENTREE_MESUREE_CAR,
            "sortie_bornee_caracteres": SORTIE_BORNE_CAR,
            "sortie_bornee_jetons": jetons(SORTIE_BORNE_CAR),
            "essais_au_plus": ESSAIS_MAX,
            "course_usd": str(COURSE_USD),
            "plafond_indicatif_usd": str(PLAFOND_INDICATIF_USD),
        },
        "candidat_de_la_ligne": CANDIDAT_DE_LA_LIGNE,
        "ligne": ligne,
        "candidats": lignes,
        "controles": {
            "tous_les_plafonds_tiennent_le_pire": all(l["plafond_tient_le_pire"] for l in lignes),
            "tous_les_plafonds_tiennent_le_cas_haut": all(l["plafond_tient_le_cas_haut"] for l in lignes),
            "la_sortie_tient_partout_provision_a_cote": all(
                l["provision_comptee_a_cote"]["la_sortie_bornee_tient"] for l in lignes),
            "la_sortie_tient_partout_provision_dedans": all(
                l["provision_comptee_dedans"]["la_sortie_bornee_tient"] for l in lignes),
            "la_ligne_tient_sous_le_plafond_indicatif": ligne["total_sous_le_plafond_indicatif"],
        },
    }
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
