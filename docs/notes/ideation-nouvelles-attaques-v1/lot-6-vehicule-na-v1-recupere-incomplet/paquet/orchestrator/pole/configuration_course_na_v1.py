"""Véhicule NA-1, lot 6 — la configuration de la course (`configuration_course_na_v1`) : lecture à son empreinte, régime,
gardes héritées du noyau vérifiées au départ, copie de la configuration par génération, garde d'empreintes (arrêt n° 14).

Lettre : V9 (`864f39a7…`), l. 60, 61, 377, 381, 385, 402 ; conception du véhicule v5 (`1b7f6822…`), § 1.4 (nom du régime),
§ 2.9 (copie par génération, six étapes, `hors_course`, gardes héritées dans la configuration), § 2.13 (A3 et A14
désactivées par écrit, voie 1 ; délai d'A3 actif ; A11 inerte ; nom d'adaptateur réservé ; garde de remplacement), § 6.2
(régime ; A3 et A14 ; configuration par génération) ; contrôle de la v5 (`4b369004…`), point 1.

**Les valeurs ne sont pas celles du développeur.** Les bornes, les seuils, les délais, la valeur de désactivation d'A3, la
borne de la garde de remplacement, les parts et les pires viennent de l'additif du véhicule, qui n'est pas écrit : ce code
les lit dans la configuration, dont le champ `statut` dit d'où elles viennent (« brouillon d'essai » tant que l'additif
n'est pas scellé). Aucune valeur n'est écrite en dur ici, hors du nom du régime, que la conception fixe (§ 1.4).

**Gardes héritées, vérifiées au départ, une par une, par leur nom** (§ 2.13) :
- A3, échecs consécutifs : la valeur de la configuration du noyau doit être **égale** à la valeur que l'additif déclare
  sous le nom de désactivation ; la valeur héritée (3) ou toute autre est refusée par son nom ;
- A14, part d'inexploitables : de même, la part déclarée sous le nom de désactivation (1 au brouillon) ;
- A3, délai : actif, chaque délai de la configuration du noyau égal au délai déclaré, au moins celui du kit (3 600 s) ;
- A11 : la liste des modèles sous garde doit être vide ;
- la garde propre au nom d'adaptateur réservé (S12) : aucun adaptateur de la table, ni de la configuration du noyau, ne
  porte ce nom ;
- la garde de remplacement : sa borne (onze refus écrits d'un même proposeur par génération) est lue, entière, ≥ 1.

Un refus nomme la garde ; il est levé **avant toute écriture**. Bibliothèque standard et modules des lots 1 à 5.
"""

import copy
import dataclasses
import hashlib
import json
import os

from pole import contrat_fiche_na_v1 as ct
from pole import portier_na_v1 as pt
from pole import requete_na_v3 as rq
from pole import routage_na_v1 as rt
from pole import tirage_na_v4 as tn

VERSION = "configuration-course-na-v1"
FORMAT_CONFIGURATION = "configuration-course-na-v1"
REGIME = "trois_generations_sans_etage_lecture_du_registre_des_tentatives"  # conception v5, § 1.4
NOMBRE_GENERATIONS = 3
NOM_DESACTIVATION = "désactivation"
DELAI_KIT_S = 3600  # délai de session du kit (`adaptateurs.py`, l. 57) : borne basse du délai d'A3 (§ 2.13)
VALEUR_HERITEE_A3 = 3  # configuration v5 de la course v9 (relevé du lot 0, Q12)
VALEUR_HERITEE_A14 = 0.34
PIECES_EXIGEES = ("gabarit", "synthese", "consigne_portier", "consigne_juges", "table_roles_cles", "liste_motifs",
                  "donnees_ignorables", "tirage")
NUMERO_ARRET_EMPREINTE = 14


class ConfigurationCourseRefusee(ValueError):
    """La configuration de la course ne tient pas sa forme : rien n'est écrit, rien ne part."""


class GardeHeriteeRefusee(ConfigurationCourseRefusee):
    """Une garde héritée du noyau n'est pas dans l'état que l'additif déclare : refus nommé, avant toute écriture."""

    def __init__(self, garde, cause):
        super().__init__(f"garde héritée « {garde} » refusée au départ : {cause}")
        self.garde, self.cause = garde, cause


class RegimeRefuse(ConfigurationCourseRefusee):
    """Le régime demandé n'est pas le seul régime permis (§ 2.9) : refus avant toute écriture."""


class ArretEmpreinteNA(RuntimeError):
    """Arrêt n° 14 : une pièce épinglée n'a pas son empreinte ; le message nomme la pièce, jamais son contenu."""

    numero = NUMERO_ARRET_EMPREINTE
    nom = "empreinte d'une pièce scellée différente"

    def __init__(self, piece, moment):
        super().__init__(f"arrêt n° {NUMERO_ARRET_EMPREINTE}, empreinte différente : pièce « {piece} » ({moment}) ; "
                         "départ refusé")
        self.piece, self.moment = piece, moment


def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


def sha256_objet(objet):
    """L'empreinte d'un objet JSON sous sa forme canonique (clés triées, UTF-8, séparateurs fixes)."""
    return sha256_octets(json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def _entier(v, minimum=1):
    return type(v) is int and v >= minimum


def _reel(v, strict=True):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and (v > 0 if strict else v >= 0)


@dataclasses.dataclass(frozen=True)
class PieceEpinglee:
    nom: str
    chemin: str
    sha256: str


@dataclasses.dataclass(frozen=True)
class ConfigurationCourseNA:
    """La configuration de la course, lue à son empreinte ; `objet` est l'objet JSON tel que lu (jamais modifié)."""

    chemin: str
    sha256: str
    objet: dict
    statut: str
    pieces: tuple  # PieceEpinglee, pièces lues par le véhicule
    pieces_epinglees: tuple  # PieceEpinglee, pièces épinglées seulement (V9, compléments, additif, programme de la garde)

    def piece(self, nom):
        for p in self.pieces:
            if p.nom == nom:
                return p
        raise ConfigurationCourseRefusee(f"pièce « {nom} » absente de la configuration")

    def octets_piece(self, nom):
        """Les octets d'une pièce, vérifiés à leur empreinte (arrêt n° 14)."""
        p = self.piece(nom)
        return lire_piece_epinglee(p, "lecture")

    @property
    def noyau(self):
        return self.objet["noyau"]

    @property
    def gardes(self):
        return self.objet["gardes_heritees"]


def lire_piece_epinglee(p, moment):
    try:
        with open(p.chemin, "rb") as f:
            octets = f.read()
    except OSError:
        raise ArretEmpreinteNA(p.nom, moment + " ; pièce illisible") from None
    if sha256_octets(octets) != p.sha256:
        raise ArretEmpreinteNA(p.nom, moment)
    return octets


def _piece(nom, e, base):
    if not isinstance(e, dict) or set(e) != {"chemin", "sha256"} or type(e["chemin"]) is not str or not e["chemin"] \
            or type(e["sha256"]) is not str or len(e["sha256"]) != 64:
        raise ConfigurationCourseRefusee(f"pièce « {nom} » : {{chemin, sha256}} exigés")
    chemin = e["chemin"] if os.path.isabs(e["chemin"]) else os.path.normpath(os.path.join(base, e["chemin"]))
    return PieceEpinglee(nom, chemin, e["sha256"])


def lire_configuration_course(chemin, empreinte_attendue):
    """La configuration de la course à son empreinte (arrêt n° 14), puis sa forme ; rend `ConfigurationCourseNA`."""
    with open(chemin, "rb") as f:
        octets = f.read()
    if type(empreinte_attendue) is not str or sha256_octets(octets) != empreinte_attendue:
        raise ArretEmpreinteNA("configuration de la course", "lecture")
    try:
        objet = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise ConfigurationCourseRefusee("configuration illisible") from None
    return configuration_depuis_objet(objet, os.path.dirname(os.path.abspath(chemin)), os.path.abspath(chemin),
                                      empreinte_attendue)


def configuration_depuis_objet(objet, base, chemin="(en mémoire)", sha256=None):
    if not isinstance(objet, dict) or objet.get("format") != FORMAT_CONFIGURATION:
        raise ConfigurationCourseRefusee(f"format « {FORMAT_CONFIGURATION} » exigé")
    statut = objet.get("statut")
    if type(statut) is not str or not statut:
        raise ConfigurationCourseRefusee("statut des valeurs : dit (brouillon d'essai ou additif scellé)")
    for c in ("regime", "nombre_generations", "plafond_generation_usd", "plafond_course_usd", "pieces", "pieces_epinglees",
              "titre_registre", "permuter_comptes", "parts_usd", "pires_par_role_usd", "portee_arret_1", "bornes",
              "declaration_portier", "gardes_heritees", "noyau"):
        if c not in objet:
            raise ConfigurationCourseRefusee(f"champ « {c} » manquant (aucun défaut)")
    pieces = objet["pieces"]
    if not isinstance(pieces, dict) or sorted(pieces) != sorted(PIECES_EXIGEES):
        raise ConfigurationCourseRefusee("pièces : exactement " + ", ".join(PIECES_EXIGEES))
    lues = tuple(_piece(n, pieces[n], base) for n in PIECES_EXIGEES)
    ep = objet["pieces_epinglees"]
    if not isinstance(ep, list) or not all(isinstance(e, dict) and type(e.get("nom")) is str and e["nom"] for e in ep):
        raise ConfigurationCourseRefusee("pièces épinglées : une liste de {nom, chemin, sha256}")
    noms = [p.nom for p in lues] + [e["nom"] for e in ep]
    if len(set(noms)) != len(noms):
        raise ConfigurationCourseRefusee("pièces : un nom en double")
    epinglees = tuple(_piece(e["nom"], {k: e[k] for k in ("chemin", "sha256") if k in e}, base) for e in ep)
    if not isinstance(objet["noyau"], dict):
        raise ConfigurationCourseRefusee("noyau : la configuration de l'orchestrateur, sans ses cases")
    if "cases" in objet["noyau"] or "empreinte_configuration" in objet["noyau"]:
        raise ConfigurationCourseRefusee("noyau : les cases et l'empreinte sont posées par la copie de chaque génération")
    if not isinstance(objet["permuter_comptes"], bool):
        raise ConfigurationCourseRefusee("permuter_comptes : vrai ou faux, dit")
    return ConfigurationCourseNA(chemin, sha256 or sha256_objet(objet), objet, statut, lues, epinglees)


# --- régime ------------------------------------------------------------------------------------------------------------

def verifier_regime(config, *, regime, nombre_generations, ligne_accord_usd, additif_sha256, additif_epingle_sha256,
                    etage=None):
    """Les quatre conditions tenues ensemble (§ 2.9) : le nom du régime ; la ligne d'accord au montant exact ; l'additif
    épinglé à son empreinte ; trois générations, aucun étage. Rend le montant requis ; sinon `RegimeRefuse`, sans écriture."""
    o = config.objet
    if regime != REGIME or o["regime"] != REGIME:
        raise RegimeRefuse(f"régime : « {REGIME} » seul permis")
    if isinstance(nombre_generations, bool) or nombre_generations != NOMBRE_GENERATIONS \
            or o["nombre_generations"] != NOMBRE_GENERATIONS:
        raise RegimeRefuse("trois générations exactement")
    if etage is not None:
        raise RegimeRefuse("aucun étage de tests de mort dans ce régime")
    s17 = o["plafond_generation_usd"]
    plafond = o["plafond_course_usd"]
    if not _reel(s17) or not _reel(plafond) or rt.micro_exact(plafond) != rt.micro_exact(NOMBRE_GENERATIONS * s17):
        raise RegimeRefuse("plafond de la course : trois fois le plafond d'une génération, sans étage")
    if float(o["noyau"].get("budget", {}).get("plafond_usd", -1)) != float(s17):
        raise RegimeRefuse("le plafond d'une génération est S17 de la configuration du noyau")
    if not _reel(ligne_accord_usd) or rt.micro_exact(ligne_accord_usd) != rt.micro_exact(plafond):
        raise RegimeRefuse("ligne d'accord : au montant exact requis")
    if type(additif_sha256) is not str or len(additif_sha256) != 64 or additif_sha256 != additif_epingle_sha256:
        raise RegimeRefuse("additif du véhicule : épinglé à son empreinte")
    return float(plafond)


# --- gardes héritées (§ 2.13) --------------------------------------------------------------------------------------------

def _valeur_desactivation(g, nom):
    d = g.get(nom)
    if not isinstance(d, dict) or set(d) != {NOM_DESACTIVATION}:
        raise GardeHeriteeRefusee(nom, f"la valeur s'écrit sous le nom « {NOM_DESACTIVATION} », et lui seul")
    return d[NOM_DESACTIVATION]


def verifier_gardes_heritees(config):
    """§ 2.13, une par une, par leur nom ; rend l'état vérifié (pour le manifeste)."""
    g = config.gardes
    noyau = config.noyau
    arrets = noyau.get("arrets")
    if not isinstance(arrets, dict):
        raise GardeHeriteeRefusee("A3", "la configuration du noyau ne porte pas ses arrêts")
    # A3, échecs consécutifs : désactivée par écrit
    v_a3 = _valeur_desactivation(g, "a3_echecs_consecutifs")
    if not _entier(v_a3, VALEUR_HERITEE_A3 + 1):
        raise GardeHeriteeRefusee("A3, échecs consécutifs", "valeur de désactivation : un entier hors d'atteinte")
    if type(arrets.get("a3_echecs_consecutifs")) is not int or arrets["a3_echecs_consecutifs"] != v_a3:
        raise GardeHeriteeRefusee("A3, échecs consécutifs", "la configuration du noyau ne porte pas la valeur que l'additif "
                                  "déclare sous le nom de désactivation")
    # A14, part d'inexploitables : désactivée par écrit
    v_a14 = _valeur_desactivation(g, "a14_part_max")
    if not _reel(v_a14) or float(v_a14) != 1.0:
        raise GardeHeriteeRefusee("A14, part d'inexploitables", "part de désactivation : 1")
    if not _reel(arrets.get("a14_part_max")) or float(arrets["a14_part_max"]) != float(v_a14):
        raise GardeHeriteeRefusee("A14, part d'inexploitables", "la configuration du noyau ne porte pas la part que l'additif "
                                  "déclare sous le nom de désactivation")
    # A3, délai : actif, aligné
    delai = g.get("a3_delai_s")
    if not _reel(delai) or float(delai) < DELAI_KIT_S:
        raise GardeHeriteeRefusee("A3, délai", f"délai déclaré : au moins celui du kit ({DELAI_KIT_S} s)")
    delais = arrets.get("a3_delai_s")
    if not isinstance(delais, dict) or "*" not in delais \
            or any(not _reel(v) or float(v) != float(delai) for v in delais.values()):
        raise GardeHeriteeRefusee("A3, délai", "chaque délai de la configuration du noyau est le délai déclaré")
    # A11 : inerte, liste vide
    if g.get("a11_modeles") != [] or arrets.get("a11_modeles") != []:
        raise GardeHeriteeRefusee("A11", "la liste des modèles sous garde de bascule est vide")
    # S12 : nom d'adaptateur réservé
    reserve = g.get("nom_adaptateur_reserve")
    if type(reserve) is not str or not reserve:
        raise GardeHeriteeRefusee("S12, nom d'adaptateur réservé", "le nom réservé est dit")
    noms = {p.get("fournisseur") for p in noyau.get("proposeurs") or []} | {j.get("fournisseur") for j in noyau.get("juges") or []} \
        | {(noyau.get("aiguilleur") or {}).get("fournisseur")} | {l.get("fournisseur") for l in noyau.get("lecteurs_etiquettes") or []} \
        | {((noyau.get("bisociateur") or {}).get("metteur_fusion") or {}).get("fournisseur")}
    if reserve in noms:
        raise GardeHeriteeRefusee("S12, nom d'adaptateur réservé", "un adaptateur de la configuration porte le nom réservé")
    # garde de remplacement
    borne = g.get("garde_remplacement_refus_ecrits_proposeur")
    if not _entier(borne):
        raise GardeHeriteeRefusee("garde de remplacement", "borne des refus écrits d'un même proposeur : un entier ≥ 1")
    return {"a3_echecs_consecutifs": {NOM_DESACTIVATION: v_a3}, "a14_part_max": {NOM_DESACTIVATION: v_a14},
            "a3_delai_s": float(delai), "a11_modeles": [], "nom_adaptateur_reserve": "absent de la table et du noyau",
            "garde_remplacement_refus_ecrits_proposeur": borne}


def verifier_nom_reserve_dans_table(config, table):
    """S12 : aucun adaptateur de la table des rôles et des clés ne porte le nom réservé."""
    reserve = config.gardes.get("nom_adaptateur_reserve")
    if any(reserve in c.adaptateurs for c in table.cles.values()):
        raise GardeHeriteeRefusee("S12, nom d'adaptateur réservé", "un adaptateur de la table porte le nom réservé")


# --- pièces lues --------------------------------------------------------------------------------------------------------

def table_de_course(config):
    """La table des rôles et des clés, à son empreinte, marquée « course » ; une table marquée « artefact » (ou « ligne à
    part ») est refusée au départ (erratum 1, E7)."""
    p = config.piece("table_roles_cles")
    octets = lire_piece_epinglee(p, "départ")
    t = rt.lire_table(octets, p.sha256, rt.MARQUE_COURSE, p.nom)
    if t.marque != rt.MARQUE_COURSE:
        raise rt.TableRefusee("table de routage : seule une table « course » part")
    verifier_nom_reserve_dans_table(config, t)
    return t


def bornes_fiche(config):
    return ct.bornes_de(dict(config.objet["bornes"]["fiche_octets"]), config.statut)


def declaration_portier(config):
    d = config.objet["declaration_portier"]
    return pt.declaration_de(forme=d["forme"], cle=d["cle"], fiche=dict(d["fiche"]),
                             reponse_sans_fiche=dict(d["reponse_sans_fiche"]), statut=config.statut)


def borne(config, nom):
    v = config.objet["bornes"].get(nom)
    if not _entier(v):
        raise ConfigurationCourseRefusee(f"borne « {nom} » : un entier strictement positif")
    return v


# --- copie de la configuration par génération (§ 2.9) --------------------------------------------------------------------

def deriver_copie_generation(config, cases_generation):
    """La configuration de l'orchestrateur pour une génération : copie de `noyau`, ses cases à la forme que le noyau exige
    (`[identifiant de la case, ligne de case]`) dans l'ordre du tirage, et son empreinte posée dans
    `empreinte_configuration`. Rend (copie, empreinte de la copie sans le champ d'empreinte)."""
    copie = copy.deepcopy(config.noyau)
    copie["cases"] = [[c.identifiant, c.ligne] for c in cases_generation]
    empreinte = sha256_objet(copie)
    copie["empreinte_configuration"] = empreinte
    copie["_base"] = os.path.dirname(config.chemin) if os.path.isabs(config.chemin) else os.getcwd()
    return copie, empreinte


CLES_HORS_EMPREINTE = ("empreinte_configuration", "_base")  # `_base` : le dossier où le noyau lit ses pièces, hors empreinte


def empreinte_copie(copie):
    sans = {k: v for k, v in copie.items() if k not in CLES_HORS_EMPREINTE}
    return sha256_objet(sans)


def verifier_copie(copie, empreinte_journalisee, generation):
    """Arrêt n° 14 sur la copie de la génération : son empreinte recalculée est celle du journal."""
    if not isinstance(copie, dict) or copie.get("empreinte_configuration") != empreinte_journalisee \
            or empreinte_copie(copie) != empreinte_journalisee:
        raise ArretEmpreinteNA(f"configuration de la génération {generation}", f"départ de la génération {generation}")
    return empreinte_journalisee


def triplets_de_la_copie(copie, tirage, generation):
    """Les triplets des cases que la copie va servir, lus au tirage par leur identifiant (pour la garde de disjonction)."""
    par_identifiant = {e["identifiant"]: tuple(e["triplet"]) for e in tirage["identifiants"]}
    rendu = []
    for c in copie["cases"]:
        if not (isinstance(c, list) and len(c) == 2) or c[0] not in par_identifiant:
            raise tn.ArretDisjonction(generation, "case de la copie hors du tirage")
        rendu.append(par_identifiant[c[0]])
    return rendu


# --- garde d'empreintes (arrêt n° 14), au départ de chaque génération ----------------------------------------------------

def verifier_empreintes(config, moment):
    """Chaque pièce lue et chaque pièce épinglée, relue à son empreinte ; la première fautive est nommée."""
    for p in config.pieces + config.pieces_epinglees:
        lire_piece_epinglee(p, moment)
    if config.chemin != "(en mémoire)":
        with open(config.chemin, "rb") as f:
            if sha256_octets(f.read()) != config.sha256:
                raise ArretEmpreinteNA("configuration de la course", moment)
    return len(config.pieces) + len(config.pieces_epinglees)


def table_des_empreintes(config):
    """La table des empreintes épinglées, sans chemin (pour le manifeste et le journal)."""
    rendu = {p.nom: p.sha256 for p in config.pieces + config.pieces_epinglees}
    rendu["configuration de la course"] = config.sha256
    return rendu


def charger_pieces_servies(config):
    """Les pièces fixes servies, à leur empreinte : gabarit, synthèse, consignes du portier et des juges."""
    gabarit = rq.charger_gabarit(config.octets_piece("gabarit"), config.piece("gabarit").sha256)
    synthese = rq.charger_piece("synthèse servie", config.octets_piece("synthese"), config.piece("synthese").sha256)
    portier = rq.charger_piece("consigne du portier", config.octets_piece("consigne_portier"),
                               config.piece("consigne_portier").sha256)
    juges = rq.charger_piece("consigne des juges", config.octets_piece("consigne_juges"), config.piece("consigne_juges").sha256)
    return gabarit, synthese, portier, juges


def lire_tirage(config):
    octets = config.octets_piece("tirage")
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise ConfigurationCourseRefusee("tirage illisible") from None


__all__ = ("ConfigurationCourseNA", "ConfigurationCourseRefusee", "GardeHeriteeRefusee", "RegimeRefuse", "ArretEmpreinteNA",
           "lire_configuration_course", "configuration_depuis_objet", "verifier_regime", "verifier_gardes_heritees",
           "table_de_course", "deriver_copie_generation", "verifier_copie", "verifier_empreintes", "REGIME",
           "NOMBRE_GENERATIONS", "NOM_DESACTIVATION")
