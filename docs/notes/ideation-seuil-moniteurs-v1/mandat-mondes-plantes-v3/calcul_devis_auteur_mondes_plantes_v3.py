"""Devis de l'appel à l'auteur des mondes plantés, course « seuil et moniteurs » — calcul v3.

Arithmétique seule : aucun tirage, aucun appel, aucun fichier lu. Sortie : un objet JSON sur la sortie standard.
Usage : python3 -B calcul_devis_auteur_mondes_plantes_v3.py > calcul-devis-auteur-mondes-plantes-v3.json

Un seul changement depuis le calcul v2 (b14a8142c46b0e6d2dbffbbebc1381f2e7fbbd5e3519aacdbf90b50791615fc3), après la
vérification (e21edffb0cd8c5dc9ff9e3b3d5fb786db63a1c70ab4385b3c70cf0b7f091ee1f, § 4) : M1, la taille du mandat v3,
27 421 octets, remplace celle du mandat v2, 27 310 octets.

Rappel du calcul v2 : deux changements depuis le calcul v1 (d715bcf2ed522737934f8a38994e27997e25f46874c4db96058e3c6090f00385), demandés par la
contre-lecture (9ea0ab895fc5bbf6a7226cf11778697da2f0d3ede79d997c43879df50b70ace5, § 6) :
- M1  : la taille du mandat v2, 27 310 octets, remplace celle du mandat v1, 24 062 octets ;
- R2  : le premier essai du candidat R2-a part au plafond de relance, 32 000 jetons de sortie, et non au plafond nominal
        de 18 000 : si l'interface compte la provision de réflexion dans le plafond de sortie, 18 000 ne contient pas la
        sortie demandée.
Rien d'autre ne change : prix, plafonds de relance, provisions, garde d'envoi, nombre d'essais, arrondis.

Entrées et leurs sources (les candidats sont dits par relais, sans nom) :
- S3  : table des espèces du collisionneur v9 v3, docs/notes/collisionneur-v9/collisionneur_v9_v3.py sur origin/main,
        lignes 100 à 141, empreinte 850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910 :
        prix par million de jetons (entrée, sortie), plafond de sortie, plafond de relance, provision de réflexion,
        garde de 2,5 caractères par jeton.
- M1  : mandat de l'auteur, mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md : 27 421 octets (borne haute de ses
        caractères) ; sa sortie est bornée à 40 000 caractères (§ 4.1 du mandat).
- R1  : règles du rédacteur, dites comme telles au devis : garde d'envoi à 30 000 caractères, deux essais au plus.
- R2  : règle du contre-lecteur, reprise par le rédacteur : premier essai de R2-a au plafond de relance.
"""
import json
import sys
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal

MILLION = Decimal(1000000)
CENT = Decimal("0.01")
CAR_PAR_JETON = Decimal("2.5")          # S3
ENTREE_MESUREE_CAR = 27421             # M1
ENTREE_GARDE_CAR = 30000                # R1
SORTIE_BORNE_CAR = 40000                # M1
ESSAIS_MAX = 2                          # R1

# S3. prix_compte : valeur de la table ; prix_bas : tarif lu ou rapporté le plus bas valable après le 1er décembre 2026.
# plafond_essai_1 de R2-a : 32000 depuis le calcul v2 (R2) ; il valait 18000 au calcul v1.
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


def haut(x):
    return str(x.quantize(CENT, rounding=ROUND_CEILING))


def devis(c):
    entree_mesuree = jetons(ENTREE_MESUREE_CAR)
    entree_garde = jetons(ENTREE_GARDE_CAR)
    sortie_borne = jetons(SORTIE_BORNE_CAR)
    bas = cout(entree_mesuree, sortie_borne, c["prix_bas"])
    essai_1 = cout(entree_mesuree, c["plafond_essai_1"] + c["provision"], c["prix_compte"])
    essai_2 = cout(entree_mesuree, c["plafond_relance"] + c["provision"], c["prix_compte"])
    cas_haut = essai_1 + essai_2
    pire_par_essai = cout(entree_garde, c["plafond_relance"] + c["provision"], c["prix_compte"])
    pire = pire_par_essai * ESSAIS_MAX
    plafond_par_essai = pire_par_essai.quantize(CENT, rounding=ROUND_CEILING)
    plafond = plafond_par_essai * ESSAIS_MAX
    return {
        "id": c["id"],
        "relais": c["relais"],
        "designation": c["designation"],
        "statut_tarif": c["statut_tarif"],
        "prix_compte_par_million": list(c["prix_compte"]),
        "prix_bas_par_million": list(c["prix_bas"]),
        "plafond_nominal_jetons": c["plafond_sortie"],
        "plafond_essai_1_jetons": c["plafond_essai_1"],
        "plafond_essai_2_jetons": c["plafond_relance"],
        "provision_jetons": c["provision"],
        "la_sortie_bornee_tient_dans_le_plafond_nominal": sortie_borne <= c["plafond_sortie"],
        "la_sortie_bornee_tient_dans_le_plafond_nominal_provision_deduite": sortie_borne <= c["plafond_sortie"] - c["provision"],
        "la_sortie_bornee_tient_au_premier_essai_provision_deduite": sortie_borne <= c["plafond_essai_1"] - c["provision"],
        "cas_bas": {"essais": 1, "exact": str(bas), "usd": proche(bas)},
        "cas_haut": {"essais": 2, "essai_1": str(essai_1), "essai_2": str(essai_2), "exact": str(cas_haut),
                     "usd": proche(cas_haut), "usd_arrondi_vers_le_haut": haut(cas_haut)},
        "pire": {"essais": ESSAIS_MAX, "par_essai_exact": str(pire_par_essai), "exact": str(pire), "usd": proche(pire)},
        "plafond_d_arret_par_essai_usd": str(plafond_par_essai),
        "plafond_d_arret_usd": str(plafond),
        "plafond_tient_le_pire": plafond >= pire,
        "plafond_tient_le_cas_haut": plafond >= cas_haut,
    }


def main():
    lignes = [devis(c) for c in CANDIDATS]
    sortie = {
        "version": "calcul-devis-auteur-mondes-plantes-v3",
        "entrees": {
            "caracteres_par_jeton": str(CAR_PAR_JETON),
            "entree_mesuree_caracteres": ENTREE_MESUREE_CAR,
            "entree_mesuree_jetons": jetons(ENTREE_MESUREE_CAR),
            "entree_garde_caracteres": ENTREE_GARDE_CAR,
            "entree_garde_jetons": jetons(ENTREE_GARDE_CAR),
            "entree_mesuree_tient_sous_la_garde": ENTREE_MESUREE_CAR <= ENTREE_GARDE_CAR,
            "sortie_bornee_caracteres": SORTIE_BORNE_CAR,
            "sortie_bornee_jetons": jetons(SORTIE_BORNE_CAR),
            "essais_au_plus": ESSAIS_MAX,
        },
        "candidats": lignes,
        "controles": {
            "tous_les_plafonds_tiennent_le_pire": all(l["plafond_tient_le_pire"] for l in lignes),
            "tous_les_plafonds_tiennent_le_cas_haut": all(l["plafond_tient_le_cas_haut"] for l in lignes),
            "plus_haut_plafond_usd": str(max(Decimal(l["plafond_d_arret_usd"]) for l in lignes)),
        },
    }
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
