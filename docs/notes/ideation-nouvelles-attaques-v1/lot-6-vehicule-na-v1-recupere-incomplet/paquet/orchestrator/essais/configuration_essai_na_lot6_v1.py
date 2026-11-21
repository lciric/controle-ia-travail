"""Véhicule NA-1, lot 6 — la configuration de course **d'essai** (brouillon, déclaré comme tel) et ses pièces factices.

Rien n'est une valeur de l'additif du véhicule, qui n'est pas écrit : les bornes, les seuils, les délais, la valeur de
désactivation d'A3, la borne de la garde de remplacement, les parts et les pires sont des valeurs d'essai, déclarées dans
le champ `statut`. Les parts et les pires sont ceux des essais du lot 4 (conception v5, § 2.3) ; le plan de dépense est
celui de la configuration v5 de la course v9 tel que l'en-tête du lanceur v10 le décrit (S17 150 ; étapes protégées 45,
15, 30 ; sacrifiables 151 ; plafond dur de la proposition 140, aiguillage lancé si le cumul est au plus 135, juges au plus
120) ; les attendus (40, 4, 6, 0, 0, 0) sont choisis pour rendre ces trois seuils.

Pièces factices, inertes : le gabarit, la synthèse, les consignes, la liste de motifs et le tirage d'essai des lots 1 à 3
(`aides_na_v4`, `aides_na_lot3_v3`) ; une table des rôles et des clés de la forme de la conception v5, § 2.3, aux noms de
clés neutres ; un additif d'essai factice. **Aucun identifiant de modèle** : les modèles sont des noms d'essai inertes.
"""

import copy
import json
import os
import shutil
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v3 as L3  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole import tirage_na_v4 as tn  # noqa: E402

STATUT_ESSAI = ("brouillon d'essai, déclaré comme tel : aucune valeur n'est celle de l'additif du véhicule, qui n'est pas "
                "écrit ; pièces factices et inertes")
MODELE_ESSAI = "modele-essai-inerte"
VALEUR_DESACTIVATION_A3_ESSAI = 1000  # brouillon d'essai ; la valeur est à l'additif, sous le nom de désactivation
DELAI_ESSAI_S = 3600
SEUIL_REMPLACEMENT_ESSAI = 11
TITRE_REGISTRE_ESSAI = "Titre factice de la section du registre"
ADDITIF_ESSAI = "Additif factice d'essai, inerte : il ne déclare rien.\n".encode("utf-8")

# (sorte, espèce, clé, adaptateur), forme de la table du § 2.3 ; clés aux noms neutres
ROLES_ESSAI = {
    "juge-espece-3": ("juge", 3, "cle_a", "ad_a"),
    "proposeur-espece-3": ("proposeur", 3, "cle_a", "ad_a"),
    "aiguilleur": ("portier", 4, "cle_b", "ad_b"),
    "proposeur-espece-4": ("proposeur", 4, "cle_b", "ad_b"),
    "juge-espece-1": ("juge", 1, "cle_c", "ad_c1"),
    "proposeur-espece-1": ("proposeur", 1, "cle_c", "ad_c1"),
    "proposeur-espece-5": ("proposeur", 5, "cle_c", "ad_c2"),
    "proposeur-espece-2": ("proposeur", 2, "cle_d", "ad_d"),
    "lecteur-etiquettes-1": ("juge", 1, "hors_course", "hors_course"),
    "lecteur-etiquettes-2": ("juge", 1, "hors_course", "hors_course"),
    "metteur-fusion": ("proposeur", 1, "hors_course", "hors_course"),
}
PARTS_ESSAI = {"cle_a": 156.56, "cle_b": 125.63, "cle_c": 140.39, "cle_d": 17.01}
PIRES_ESSAI = {"proposeur": 6.05, "portier": 0.25, "juge": 0.60}
ITEMS_ESSAI = ["item_factice_un", "item_factice_deux"]
DECLARATION_ESSAI = {"forme": "ligne ancrée", "cle": "étiquette",
                     "fiche": {"niveau de l'idée": "niveau de l'idée", "concret": "concret"},
                     "reponse_sans_fiche": {"réponse vide motivée": "réponse vide motivée", "refus du modèle": "refus du modèle",
                                            "réponse illisible": "réponse illisible"}}


def objet_table(roles=None, marque="course"):
    roles = ROLES_ESSAI if roles is None else roles
    cles = [
        {"nom": "cle_a", "type": "claude_sdk", "part_usd": PARTS_ESSAI["cle_a"], "adaptateurs": ["ad_a"],
         "relais": "http://127.0.0.1:9"},
        {"nom": "cle_b", "type": "claude_sdk", "part_usd": PARTS_ESSAI["cle_b"], "adaptateurs": ["ad_b"],
         "relais": "http://127.0.0.1:10"},
        {"nom": "cle_c", "type": "commande_externe", "part_usd": PARTS_ESSAI["cle_c"], "adaptateurs": ["ad_c1", "ad_c2"],
         "relais": None},
        {"nom": "cle_d", "type": "kimi_protocole", "part_usd": PARTS_ESSAI["cle_d"], "adaptateurs": ["ad_d"], "relais": None},
        {"nom": "cle_sans_part", "type": "aucun", "part_usd": None, "adaptateurs": ["ad_sans_part"], "relais": None},
        {"nom": "hors_course", "type": "aucun", "part_usd": None, "adaptateurs": ["hors_course"], "relais": None},
    ]
    return {"format": rt.FORMAT_TABLE, "marque": marque, "nom": "course", "plafond_ligne_usd": None, "cles": cles,
            "roles": [{"role": r, "sorte": s, "espece": e, "cle": c, "adaptateur": a} for r, (s, e, c, a) in roles.items()]}


def octets_table(objet):
    return json.dumps(objet, ensure_ascii=False, sort_keys=True).encode("utf-8")


def configuration_noyau():
    """La configuration de l'orchestrateur, sans ses cases (posées par la copie de chaque génération)."""
    pieces = {n: n + ".md" for n in ("consigne_proposeur", "consigne_passe_tableau", "consigne_aiguilleur", "consigne_juge",
                                     "consigne_fusion", "consigne_lecteur")}
    proposeurs = [{"etiquette": r, "modele": MODELE_ESSAI, "fournisseur": a, "consigne": "consigne_proposeur"}
                  for r, (s, e, c, a) in ROLES_ESSAI.items() if s == "proposeur" and c != "hors_course"]
    return {
        "racine_graines": 20261121, "champs_fiche": ["case", "idee"], "champ_titre": "idee", "champ_axe": "case",
        "budget": {"plafond_usd": 150.0, "arret_etape_usd": 150.0, "portee_plafond": "par_generation", "etapes": [
            {"nom": "proposition", "attendu_usd": 40.0, "plafond_relais_usd": 45.0, "role": "protegee"},
            {"nom": "aiguillage", "attendu_usd": 4.0, "plafond_relais_usd": 15.0, "role": "protegee"},
            {"nom": "juges", "attendu_usd": 6.0, "plafond_relais_usd": 30.0, "role": "protegee"},
            {"nom": "passe_tableau", "attendu_usd": 0.0, "plafond_relais_usd": 151.0, "role": "sacrifiable", "rang": 2},
            {"nom": "etiquettes", "attendu_usd": 0.0, "plafond_relais_usd": 0.0, "role": "protegee"},
            {"nom": "fusions", "attendu_usd": 0.0, "plafond_relais_usd": 151.0, "role": "sacrifiable", "rang": 1}]},
        "juges": [{"etiquette": "juge-espece-3", "modele": MODELE_ESSAI, "fournisseur": "ad_a", "consigne": "consigne_juge"},
                  {"etiquette": "juge-espece-1", "modele": MODELE_ESSAI, "fournisseur": "ad_c1", "consigne": "consigne_juge"}],
        "items_juge": list(ITEMS_ESSAI), "agregation": {"regle": "au_moins", "q": 1},
        "aiguilleur": {"etiquette": "aiguilleur", "modele": MODELE_ESSAI, "fournisseur": "ad_b",
                       "consigne": "consigne_aiguilleur"},
        "garde_kimi": {"debordement_max": 1.0, "refus_aiguilleur": "inexploitable", "arret_metteur_fusion": False},
        "tableau": {"longueur_max_titre": 40, "longueur_max_resume": 60, "champ_resume": "idee",
                    "consigne_passe": "consigne_passe_tableau", "juger_passe_tableau": False},
        "memoire": {"methode": "bardeaux", "taille_bardeau": 3, "seuil": 0.6},
        "bisociateur": {"bras": [], "k_paires": 0, "consigne_fusion": "consigne_fusion",
                        "consigne_lecteur_etiquettes": "consigne_lecteur", "fournisseurs_entree": ["*"],
                        "metteur_fusion": {"etiquette": "metteur-fusion", "modele": MODELE_ESSAI, "fournisseur": "hors_course"}},
        "proposeurs": proposeurs,
        "plafonds_session": {"proposeur": 6.05, "aiguilleur": 0.25, "juge": 0.60, "fusion": 0.10, "lecteur": 0.10},
        "etiquettes_interdites": ["ETIQUETTE-FACTICE-INTERDITE"],
        "lecteurs_etiquettes": [{"etiquette": "lecteur-etiquettes-1", "modele": MODELE_ESSAI, "fournisseur": "hors_course"},
                                {"etiquette": "lecteur-etiquettes-2", "modele": MODELE_ESSAI, "fournisseur": "hors_course"}],
        "pieces": pieces,
        "a4": {"mode": "prefixe", "action": "arret"},
        "arrets": {"a3_echecs_consecutifs": VALEUR_DESACTIVATION_A3_ESSAI, "a3_delai_s": {"*": DELAI_ESSAI_S},
                   "a14_part_max": 1.0, "a11_modeles": []},
        "graines": {"prefixe": "na1"},
        "simulation": {"cout_par_appel_usd": 0.01},
    }


def configuration_objet(pieces, pieces_epinglees):
    return {
        "format": cfn.FORMAT_CONFIGURATION, "statut": STATUT_ESSAI, "regime": cfn.REGIME, "nombre_generations": 3,
        "plafond_generation_usd": 150.0, "plafond_course_usd": 450.0, "pieces": pieces, "pieces_epinglees": pieces_epinglees,
        "titre_registre": TITRE_REGISTRE_ESSAI, "permuter_comptes": False, "parts_usd": dict(PARTS_ESSAI),
        "pires_par_role_usd": {r: PIRES_ESSAI[s] for r, (s, e, c, a) in ROLES_ESSAI.items() if c != "hors_course"},
        "portee_arret_1": "appel",
        "bornes": {"fiche_octets": dict({c: 300 for c in L3.rq.CHAMPS_FICHE}, idee=1200), "requete_proposeur_octets": 200000,
                   "registre_octets": 100000, "enonce_octets": 1200},
        "declaration_portier": copy.deepcopy(DECLARATION_ESSAI),
        "gardes_heritees": {"a3_echecs_consecutifs": {cfn.NOM_DESACTIVATION: VALEUR_DESACTIVATION_A3_ESSAI},
                            "a14_part_max": {cfn.NOM_DESACTIVATION: 1.0}, "a3_delai_s": DELAI_ESSAI_S, "a11_modeles": [],
                            "nom_adaptateur_reserve": "kimi",
                            "garde_remplacement_refus_ecrits_proposeur": SEUIL_REMPLACEMENT_ESSAI},
        "noyau": configuration_noyau(),
    }


def _ecrire(dossier, nom, octets):
    chemin = os.path.join(dossier, nom)
    with open(chemin, "xb") as f:
        f.write(octets)
    return {"chemin": nom, "sha256": cfn.sha256_octets(octets)}


def ecrire_configuration_essai(dossier, *, modifier=None, table=None, tirage=None, nom="configuration-course-na-essai-v1.json"):
    """Écrit les pièces factices et la configuration d'essai dans `dossier` (neuf) ; rend (chemin, empreinte).
    `modifier(objet)` change l'objet avant l'écriture (artefacts d'essai)."""
    os.makedirs(dossier, exist_ok=False)
    sortie_tirage = tirage if tirage is not None else A.sortie_factice()
    pieces = {
        "gabarit": _ecrire(dossier, "gabarit-factice.md", A.GABARIT_FACTICE),
        "synthese": _ecrire(dossier, "synthese-factice.md", A.SYNTHESE_FACTICE),
        "consigne_portier": _ecrire(dossier, "consigne-portier-factice.md", L3.CONSIGNE_PORTIER_FACTICE),
        "consigne_juges": _ecrire(dossier, "consigne-juges-factice.md", L3.CONSIGNE_JUGE_FACTICE),
        "table_roles_cles": _ecrire(dossier, "table-roles-cles-essai.json", octets_table(table or objet_table())),
        "liste_motifs": None, "donnees_ignorables": None,
        "tirage": _ecrire(dossier, "tirage-factice.json", tn.serialiser(sortie_tirage)),
    }
    for cle, source, nom_copie in (("liste_motifs", A.CHEMIN_LISTE_ESSAI, "liste-motifs-essai.json"),
                                   ("donnees_ignorables", A.CHEMIN_DONNEES, "ignorables-unicode.json")):
        shutil.copyfile(source, os.path.join(dossier, nom_copie))
        with open(os.path.join(dossier, nom_copie), "rb") as f:
            pieces[cle] = {"chemin": nom_copie, "sha256": cfn.sha256_octets(f.read())}
    epinglees = [dict(_ecrire(dossier, "additif-factice.md", ADDITIF_ESSAI), nom="additif du véhicule")]
    noyau_pieces = configuration_noyau()["pieces"]
    lues = {n: _ecrire(dossier, fichier, f"Consigne factice « {n} », inerte, jamais servie dans ce régime.\n".encode("utf-8"))
            for n, fichier in noyau_pieces.items()}
    objet = configuration_objet(pieces, epinglees)
    objet["noyau"]["pieces"] = lues
    if modifier is not None:
        modifier(objet)
    octets = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    chemin = os.path.join(dossier, nom)
    with open(chemin, "xb") as f:
        f.write(octets)
    return chemin, cfn.sha256_octets(octets)


def additif_essai_sha256():
    return cfn.sha256_octets(ADDITIF_ESSAI)


__all__ = ("ecrire_configuration_essai", "objet_table", "octets_table", "configuration_noyau", "configuration_objet",
           "additif_essai_sha256", "STATUT_ESSAI", "ROLES_ESSAI", "ITEMS_ESSAI", "DECLARATION_ESSAI", "MODELE_ESSAI")
