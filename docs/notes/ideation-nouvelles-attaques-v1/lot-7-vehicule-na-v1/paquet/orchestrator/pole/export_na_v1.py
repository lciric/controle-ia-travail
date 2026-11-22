"""Véhicule NA-1, lot 7 — l'export hors quarantaine, à champs fermés (`export_na_v1`) ; arrêt n° 17, premier temps.

Lettre : V9 (`864f39a7…`), l. 82 (« Dehors : identifiants, empreintes, tailles, comptes par case »), l. 84, l. 388 (n° 17) ;
conception du véhicule v5 (`1b7f6822…`), § 2.6 (quarantaine : « sur une liste fermée de champs, et refuse tout champ
libre »), § 2.8 (« seuls des comptes, des parts et des identifiants sortent du dossier »), § 6.1 (n° 17).

**Ce qui sort** : un objet construit par `construire_export` à partir des mesures, puis vérifié par `verifier_export`
contre un **schéma fermé** (`SCHEMA`) : chaque clé est nommée au schéma ou est un identifiant de la liste permise
(cases servies, fiches gardées, témoins, rôles) ; chaque valeur est d'un type fermé : compte (entier positif ou nul), part
(numérateur, dénominateur), dollars, booléen, empreinte (64 caractères hexadécimaux), étiquette d'une liste fermée. **Une
chaîne qui n'est ni une empreinte, ni un identifiant permis, ni une étiquette de sa liste est un champ libre : refus,
arrêt n° 17**, qui nomme le chemin de la clé, jamais la valeur. Rien de l'énoncé, du nom, du champ `filiation`, d'un
modèle, d'une catégorie de refus ni d'une clé ne sort.

Bibliothèque standard, et les modules du lot 7.
"""

import re

from pole import commun_na_lot7_v1 as cm
from pole import mesures_na_v1 as ms

VERSION = "export-na-v1"
NOM_EXPORT = "export-hors-quarantaine-na-v1.json"
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
NOMS_ARRETS = (  # lot 6 v3, ARRETS_CONNUS, et l'arrêt n° 15 du lot 7 ; liste fermée
    "empreinte d'une pièce scellée différente", "garde de disjonction", "consigne plus longue que sa borne",
    "registre servi non conforme (n° 8, 9 ou 19)", "garde du coffre", "plafond de la course atteint (réservation impossible)",
    "cumul de la course au-delà de son plafond", "seuils d'une génération", "part d'une clé épuisée ou rôle sur une autre clé",
    "motif interdit dans un texte à servir", "refus pour crédit", "refus d'un classifieur de sûreté",
    "A2, modèle servi absent ou changé", "requête journalisée", "A17, fiche sans passeport du portier neuf",
    "garde de remplacement : refus écrits d'un même proposeur", "étape neutralisée jouée",
    "câblage de la colonne : journal du contexte d'appel autre que celui de la colonne",
    "garde de la colonne « matière première »", "garde de la colonne « matière première », registre servi",
    "refus de la colonne « matière première »", "nœud")
TITRES = ("course complète, trois générations",) + tuple(f"course arrêtée par {n}" for n in NOMS_ARRETS)


class ArretQuarantaineRompueNA17(RuntimeError):
    """Arrêt n° 17 de la V9 : quarantaine rompue (un champ libre dans l'export, une branche liée à `main`, une empreinte de
    la branche hors d'elle). La lecture des mesures s'arrête ; consigné sans recopier ce qui a fui ; nœud de Lazar."""

    numero = 17
    nom = "quarantaine rompue"

    def __init__(self, cause):
        super().__init__(f"arrêt n° 17, {self.nom} : {cause} ; consigné, nœud de Lazar")
        self.cause = cause


# --- types fermés -----------------------------------------------------------------------------------------------------
COMPTE, USD, BOOLEEN, EMPREINTE, PART = "compte", "usd", "booléen", "empreinte", "part"


def ETIQUETTE(*liste):
    return ("étiquette", tuple(liste))


def DICT(cles, valeur):  # cles : "identifiant", "rôle", "génération" ou un tuple de clés fixes
    return ("dict", cles, valeur)


def LISTE(valeur):
    return ("liste", valeur)


def OU(*types):
    return ("ou", types)


SANS_OBJET = ETIQUETTE(ms.SANS_OBJET)
LECTURE = {
    "M1": OU(SANS_OBJET, {"part": PART, "par_generation": DICT("génération", PART), "par_espece": DICT("rôle", PART),
                          "servies_par_repli": PART}),
    "M1_bis": OU(SANS_OBJET, COMPTE),
    "M2": OU(SANS_OBJET, {"parentes_distinctes": COMPTE, "part_vers_la_plus_citee": PART}),
    "M3": DICT("génération", {"par_case": DICT("identifiant", {"au_coffre": PART, "hors_case": PART}),
                              "generation": {"au_coffre": PART, "hors_case": PART}}),
    "M7": {"autre, à nommer": PART, "autres cases": PART},
}
SCHEMA = {
    "version": ETIQUETTE(VERSION),
    "titre": ETIQUETTE(*TITRES),
    "generations_completes": COMPTE,
    "arret": OU(ETIQUETTE("aucun"), {"numero": OU(COMPTE, ETIQUETTE("à l'additif")), "nom": ETIQUETTE(*NOMS_ARRETS)}),
    "empreintes_des_entrees": DICT(("journal_arrets", "bilan", "attestation", "anteriorite", "registre_g1", "registre_g2",
                                    "registre_g3"), EMPREINTE),
    "lectures": {"scellée": LECTURE, "espèces seules": LECTURE},
    "M3_relecture_au_coffre": COMPTE,
    "M4": DICT("génération", {"cout_par_role_usd": DICT("rôle", USD), "cout_par_espece_usd": DICT("espèce", USD),
                              "replis": {"cout_usd": USD, "tentatives": COMPTE, "fiches": COMPTE}}),
    "M5": {"par_etiquette": DICT(ms.ETIQUETTES_ANTERIORITE, COMPTE), "non_lues": COMPTE,
           "temoins": DICT("identifiant", ETIQUETTE(*ms.ETIQUETTES_ANTERIORITE, *ms.CLASSES_EPREUVE_4, "passée", "manqué")),
           "branche": ETIQUETTE(*ms.BRANCHES), "par_classe": DICT(ms.CLASSES_EPREUVE_4, COMPTE), "desaccords": COMPTE},
    "M6": DICT("génération", DICT("identifiant", DICT("rôle", DICT(ms.CLASSES_M6 + (ms.ARRET_1,), COMPTE)))),
    "M6_sous_comptes": DICT("génération", {"cause non établie, par rôle": DICT("rôle", COMPTE),
                                           ms.SOUS_COMPTE_PORTIER: COMPTE}),
    "replis": DICT("rôle", {"tentatives": COMPTE, "cout_usd": USD, "fiches": COMPTE}),
    "C1": {"aucune_case_servie_deux_fois": BOOLEEN, "cases_servies": COMPTE, "cases_attendues": COMPTE,
           "trente_trois_cases_servies": BOOLEEN, "aucune_case_de_la_famille_tenue_a_l_ecart": BOOLEEN},
    "I1": {"titre": ETIQUETTE("pour information"),
           "par_generation": DICT("génération", {"fiches_jugees": COMPTE, "appels_juge": DICT("rôle", COMPTE),
                                                  "verdicts_absents": DICT("rôle", DICT(("non lancé", "refus écrit",
                                                                                         "verdict illisible"), COMPTE))})},
}
CLES_OPTIONNELLES = {("M5", "par_classe"), ("M5", "desaccords")}
ROLES_EXPORT = ms.ROLES  # rôles de l'interface ; ceux de la configuration (lot 6) sont donnés à part


def _refus(chemin, cause):
    raise ArretQuarantaineRompueNA17(f"export, champ « {'/'.join(chemin) or '(racine)'} » : {cause}")


def _verifier(v, t, chemin, permis):
    if isinstance(t, dict):
        if not isinstance(v, dict):
            _refus(chemin, "objet attendu")
        hors = set(v) - set(t)
        if hors:
            _refus(chemin, "clé hors du schéma (champ libre)")
        for k, tk in t.items():
            if k not in v:
                if tuple(chemin[-1:]) + (k,) in CLES_OPTIONNELLES:
                    continue
                _refus(chemin + [k], "clé du schéma absente")
            _verifier(v[k], tk, chemin + [k], permis)
        return
    if isinstance(t, tuple) and t[0] == "ou":
        for u in t[1]:
            try:
                _verifier(v, u, chemin, permis)
                return
            except ArretQuarantaineRompueNA17:
                continue
        _refus(chemin, "valeur d'aucun type permis")
    if isinstance(t, tuple) and t[0] == "étiquette":
        if type(v) is not str or v not in t[1]:
            _refus(chemin, "étiquette hors de sa liste fermée (champ libre)")
        return
    if isinstance(t, tuple) and t[0] == "liste":
        if not isinstance(v, list):
            _refus(chemin, "liste attendue")
        for i, x in enumerate(v):
            _verifier(x, t[1], chemin + [str(i)], permis)
        return
    if isinstance(t, tuple) and t[0] == "dict":
        if not isinstance(v, dict):
            _refus(chemin, "objet attendu")
        cles = t[1]
        for k, x in v.items():
            if isinstance(cles, tuple):
                ok = k in cles
            elif cles == "identifiant":
                ok = k in permis[0]
            elif cles == "rôle":
                ok = k in permis[1]
            elif cles == "génération":
                ok = k in ("1", "2", "3")
            elif cles == "espèce":
                ok = k in ("1", "2", "3", "4", "5")
            else:
                ok = False
            if not ok:
                _refus(chemin, "clé hors de sa liste fermée (champ libre)")
            _verifier(x, t[2], chemin + [k], permis)
        return
    if t == COMPTE:
        if type(v) is not int or v < 0:
            _refus(chemin, "compte attendu")
    elif t == USD:
        if type(v) not in (int, float) or v < 0 or v != v:
            _refus(chemin, "montant attendu")
    elif t == BOOLEEN:
        if type(v) is not bool:
            _refus(chemin, "booléen attendu")
    elif t == EMPREINTE:
        if type(v) is not str or not _HEX64.match(v):
            _refus(chemin, "empreinte attendue")
    elif t == PART:
        if not isinstance(v, dict) or set(v) != {"numerateur", "denominateur"} \
                or not all(type(x) is int and x >= 0 for x in v.values()) or v["numerateur"] > v["denominateur"]:
            _refus(chemin, "part attendue (numérateur, dénominateur)")
    else:
        _refus(chemin, "type inconnu du schéma")


def verifier_export(objet, identifiants_permis, roles_de_configuration=()):
    """Vérifie l'objet contre le schéma fermé ; lève `ArretQuarantaineRompueNA17` au premier champ libre. Les clés de
    rôle permises sont les rôles de l'interface et les étiquettes de rôle de la configuration (liste fermée donnée)."""
    ids, roles = frozenset(identifiants_permis), frozenset(ROLES_EXPORT) | frozenset(roles_de_configuration)
    if not all(type(i) is str and re.fullmatch(r"[a-z0-9_-]{1,40}", i) for i in ids | roles):
        raise ArretQuarantaineRompueNA17("la liste des identifiants ou des rôles permis porte autre chose que des identifiants")
    _verifier(objet, SCHEMA, [], (ids, roles))
    return objet


def _lecture(L):
    sortie = {}
    m1 = L["M1"]
    if m1 == ms.SANS_OBJET:
        sortie["M1"] = ms.SANS_OBJET
    else:
        par_e = {k: v for k, v in m1["par_espece"].items() if k in ms.PROPOSEURS}
        repli = [v for k, v in m1["par_espece"].items() if k not in ms.PROPOSEURS]
        sortie["M1"] = {"part": m1["part"], "par_generation": m1["par_generation"], "par_espece": par_e,
                        "servies_par_repli": {"numerateur": sum(v["numerateur"] for v in repli),
                                              "denominateur": sum(v["denominateur"] for v in repli)}}
    sortie["M1_bis"] = L["M1_bis"]
    sortie["M2"] = L["M2"] if L["M2"] == ms.SANS_OBJET else {
        "parentes_distinctes": L["M2"]["parentes_distinctes"], "part_vers_la_plus_citee": L["M2"]["part_vers_la_plus_citee"]}
    sortie["M3"] = L["M3"]
    sortie["M7"] = L["M7"]
    return sortie


def construire_export(mesures):
    """Les seuls champs fermés des mesures ; aucun modèle, aucune catégorie, aucune parente nommée."""
    replis = {}
    for r in mesures["replis"]:
        d = replis.setdefault(r["role"], {"tentatives": 0, "cout_usd": 0.0, "fiches": 0})
        d["tentatives"] += r["tentatives"]
        d["cout_usd"] = round(d["cout_usd"] + r["cout_usd"], 6)
        d["fiches"] += r["fiches"]
    m4 = {}
    for g, d in mesures["M4"].items():
        rep = {"cout_usd": round(sum(x["cout_usd"] for x in d["replis"].values()), 6),
               "tentatives": sum(x["tentatives"] for x in d["replis"].values()),
               "fiches": sum(x["fiches"] for x in d["replis"].values())}
        m4[g] = {"cout_par_role_usd": d["cout_par_role_usd"], "cout_par_espece_usd": d["cout_par_espece_usd"], "replis": rep}
    arret = "aucun" if mesures["arret"] is None else {
        "numero": mesures["arret"]["numero"] if type(mesures["arret"]["numero"]) is int else "à l'additif",
        "nom": mesures["arret"]["nom"]}
    m5 = {k: v for k, v in mesures["M5"].items()}
    return {
        "version": VERSION, "titre": mesures["titre"], "generations_completes": mesures["generations_completes"],
        "arret": arret, "empreintes_des_entrees": mesures["empreintes_des_entrees"],
        "lectures": {k: _lecture(v) for k, v in mesures["lectures"].items()},
        "M3_relecture_au_coffre": mesures["M3_relecture_au_coffre"], "M4": m4, "M5": m5, "M6": mesures["M6"],
        "M6_sous_comptes": mesures["M6_sous_comptes"], "replis": replis, "C1": mesures["C1"], "I1": mesures["I1"],
    }


def identifiants_permis_de(mesures):
    ids = mesures["identifiants"]
    return set(ids["cases"]) | set(ids["temoins"])


def ecrire_export(chemin, mesures, roles_de_configuration=()):
    """Construit, vérifie (n° 17), puis écrit l'export scellé, sans écrasement ; rend son empreinte."""
    objet = verifier_export(construire_export(mesures), identifiants_permis_de(mesures), roles_de_configuration)
    return cm.ecrire_json_scelle(chemin, objet)
