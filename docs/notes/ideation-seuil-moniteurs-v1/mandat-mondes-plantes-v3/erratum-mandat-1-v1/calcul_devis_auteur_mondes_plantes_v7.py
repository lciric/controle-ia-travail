"""Devis de l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — calcul v7.

Arithmétique seule : aucun tirage, aucun appel, aucun fichier lu. Sortie : un objet JSON sur la sortie standard.
Usage : python3 -B calcul_devis_auteur_mondes_plantes_v7.py > calcul-devis-auteur-mondes-plantes-v7.json

Un seul changement depuis le calcul v6 (989430a5fd31105c6d059252ce03eba92943a8039dfa96e00f854500a64fc957), sur le mot de
la mère : le plafond d'arrêt est le pire par essai au taux le plus dur des deux, arrondi au cent vers le haut, fois
le nombre d'essais. Il tient ainsi le pire de deux essais aux deux taux, et le second essai reste possible après un
premier essai joué jusqu'au bout de ses plafonds. La fonction plafond_d_arret porte ce changement ; rien d'autre
ne change. La phrase du rappel ci-dessous sur le plafond « au taux de la table » ne vaut donc plus.

Rappel du calcul v6 : deux changements depuis le calcul v5 (b4b1d52ac464a03e105412be4b5e7a72c9a7a2cac26fa7e90ae1117d51fa49df), sur le mot de
la mère :
- E1  : la borne de sortie passe de 55 000 à 52 000 caractères ;
- T2  : un second taux de conversion, 2,227 caractères par jeton, est calculé à côté de la garde de 2,5 de la table.
        C'est une hypothèse prudente : il compte plus de jetons pour un même texte. Tout ce qui dépend d'un compte de
        jetons est rendu aux deux taux, l'entrée comprise.
Le plafond d'arrêt reste calculé comme aux calculs v1 à v5 : au taux de la table, 2,5, sur la garde d'envoi. Le
programme dit, pour chaque taux, si ce plafond tient le cas haut et le pire ; il ne le change pas.

Entrées et leurs sources (les candidats sont dits par relais, sans nom) :
- S3  : table des espèces du collisionneur v9 v3, docs/notes/collisionneur-v9/collisionneur_v9_v3.py sur origin/main,
        lignes 100 à 141, empreinte 850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910 :
        prix par million de jetons (entrée, sortie), plafond de sortie, plafond de relance, provision de réflexion,
        garde de 2,5 caractères par jeton. Valeurs reprises des calculs v2 à v5, sans changement.
- T2  : taux de 2,227 caractères par jeton, « relevé » selon le mot de la mère rapporté au rédacteur ; le rédacteur
        n'a pas vu le relevé.
- M1  : le texte servi, le mandat v3 avec son erratum 1 appliqué, troisième passe
        (f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008) : 27 468 octets, borne haute de ses caractères.
- E1  : borne de sortie de l'erratum 1 du mandat, troisième passe : 52 000 caractères.
- R1  : règles du rédacteur : garde d'envoi à 30 000 caractères, deux essais au plus.
- R2  : premier essai de R2-a au plafond de relance, 32 000 jetons de sortie (devis v2).
- C1  : devis v3 de la course, scellé : 114,48 USD ; plafond indicatif de la course : 120 USD (GO-2026-11-21-16).
"""
import json
import sys
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal

MILLION = Decimal(1000000)
CENT = Decimal("0.01")
TAUX_TABLE = Decimal("2.5")             # S3
TAUX_PRUDENT = Decimal("2.227")         # T2
TAUX = [("taux_de_la_table_2_5", TAUX_TABLE), ("taux_prudent_2_227", TAUX_PRUDENT)]
ENTREE_MESUREE_CAR = 27468              # M1
ENTREE_GARDE_CAR = 30000                # R1
SORTIE_BORNE_CAR = 52000                # E1
ESSAIS_MAX = 2                          # R1
COURSE_USD = Decimal("114.48")          # C1
PLAFOND_INDICATIF_USD = Decimal("120")  # C1
CANDIDAT_DE_LA_LIGNE = "R2-a"

# S3 et R2, comme aux calculs v3 à v5.
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


def jetons(caracteres, taux):
    return int((Decimal(caracteres) / taux).to_integral_value(rounding=ROUND_CEILING))


def cout(jetons_entree, jetons_sortie, prix):
    return (Decimal(jetons_entree) * Decimal(prix[0]) + Decimal(jetons_sortie) * Decimal(prix[1])) / MILLION


def proche(x):
    return str(x.quantize(CENT, rounding=ROUND_HALF_UP))


def plafond_d_arret(c):
    """Plafond d'arrêt (v7) : pire par essai au taux le plus dur des deux, arrondi au cent vers le haut."""
    plus_grand_plafond = max(c["plafond_essai_1"], c["plafond_relance"])
    pire_par_essai = max(
        cout(jetons(ENTREE_GARDE_CAR, taux), plus_grand_plafond + c["provision"], c["prix_compte"]) for _, taux in TAUX)
    par_essai = pire_par_essai.quantize(CENT, rounding=ROUND_CEILING)
    return par_essai, par_essai * ESSAIS_MAX


def a_un_taux(c, taux, plafond):
    entree_mesuree = jetons(ENTREE_MESUREE_CAR, taux)
    entree_garde = jetons(ENTREE_GARDE_CAR, taux)
    sortie_borne = jetons(SORTIE_BORNE_CAR, taux)
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
    reste_provision_dedans = plus_petit_plafond - c["provision"]
    return {
        "caracteres_par_jeton": str(taux),
        "entree_mesuree_jetons": entree_mesuree,
        "entree_garde_jetons": entree_garde,
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
        "le_plafond_d_arret_tient_le_cas_haut": plafond >= cas_haut,
        "le_plafond_d_arret_tient_le_pire": plafond >= pire,
        "depassement_du_cas_haut_usd": str(max(Decimal(0), cas_haut - plafond)),
        "depassement_du_pire_usd": str(max(Decimal(0), pire - plafond)),
        "marge_du_plafond_sur_le_pire_usd": str(plafond - pire),
        "reste_apres_un_premier_essai_au_pire_usd": str(plafond - pire_par_essai),
        "le_second_essai_au_pire_tient_dans_ce_reste": plafond - pire_par_essai >= pire_par_essai,
    }


def devis(c):
    par_essai, plafond = plafond_d_arret(c)
    total = COURSE_USD + plafond
    return {
        "id": c["id"],
        "relais": c["relais"],
        "statut_tarif": c["statut_tarif"],
        "plafond_essai_1_jetons": c["plafond_essai_1"],
        "plafond_essai_2_jetons": c["plafond_relance"],
        "provision_jetons": c["provision"],
        "plafond_d_arret_par_essai_usd": str(par_essai),
        "plafond_d_arret_usd": str(plafond),
        "total_avec_la_course_usd": str(total),
        "marge_sous_le_plafond_indicatif_usd": str(PLAFOND_INDICATIF_USD - total),
        "total_sous_le_plafond_indicatif": total <= PLAFOND_INDICATIF_USD,
        "aux_deux_taux": {nom: a_un_taux(c, taux, plafond) for nom, taux in TAUX},
    }


def main():
    lignes = [devis(c) for c in CANDIDATS]
    ligne = [l for l in lignes if l["id"] == CANDIDAT_DE_LA_LIGNE][0]
    noms = [nom for nom, _ in TAUX]
    sortie = {
        "version": "calcul-devis-auteur-mondes-plantes-v7",
        "entrees": {
            "taux_caracteres_par_jeton": {nom: str(taux) for nom, taux in TAUX},
            "entree_mesuree_caracteres": ENTREE_MESUREE_CAR,
            "entree_garde_caracteres": ENTREE_GARDE_CAR,
            "entree_mesuree_tient_sous_la_garde": ENTREE_MESUREE_CAR <= ENTREE_GARDE_CAR,
            "marge_sous_la_garde_caracteres": ENTREE_GARDE_CAR - ENTREE_MESUREE_CAR,
            "sortie_bornee_caracteres": SORTIE_BORNE_CAR,
            "essais_au_plus": ESSAIS_MAX,
            "course_usd": str(COURSE_USD),
            "plafond_indicatif_usd": str(PLAFOND_INDICATIF_USD),
        },
        "candidat_de_la_ligne": CANDIDAT_DE_LA_LIGNE,
        "ligne": ligne,
        "candidats": lignes,
        "controles": {
            "la_ligne_tient_sous_le_plafond_indicatif": ligne["total_sous_le_plafond_indicatif"],
            "la_sortie_de_la_ligne_tient_provision_dedans": {
                nom: ligne["aux_deux_taux"][nom]["provision_comptee_dedans"]["la_sortie_bornee_tient"] for nom in noms},
            "le_plafond_de_la_ligne_tient_le_cas_haut": {
                nom: ligne["aux_deux_taux"][nom]["le_plafond_d_arret_tient_le_cas_haut"] for nom in noms},
            "le_plafond_de_la_ligne_tient_le_pire": {
                nom: ligne["aux_deux_taux"][nom]["le_plafond_d_arret_tient_le_pire"] for nom in noms},
            "le_second_essai_de_la_ligne_reste_possible_apres_un_premier_au_pire": {
                nom: ligne["aux_deux_taux"][nom]["le_second_essai_au_pire_tient_dans_ce_reste"] for nom in noms},
        },
    }
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
