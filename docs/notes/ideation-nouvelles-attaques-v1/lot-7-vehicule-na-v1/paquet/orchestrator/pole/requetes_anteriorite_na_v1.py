"""Véhicule NA-1, lot 7 — les chaînes de requête de la classe (i) de la lecture d'antériorité
(`requetes_anteriorite_na_v1`), produites par programme à partir de la case, avant toute lecture de la fiche.

Lettre : V9 (`864f39a7…`), plan d'analyse, « Périmètre de recherche dans la littérature » : bases ; « (i) les valeurs des
trois champs fermés de sa case, croisées avec les mots du domaine (sonde, moniteur, activations, boîte blanche), en français
et en anglais » ; « les chaînes de requête de la classe (i) sont produites par programme à partir de la case, avant toute
lecture de la fiche » ; trente premiers résultats par base et par chaîne ; conception du véhicule v5 (`1b7f6822…`), § 9,
point 13 ; projet d'additif v2, X-8 et Q14 (passe X sans case).

**Ce que le programme reçoit** : la ligne de case du tirage scellé (`case : <identifiant> ; <v1> ; <v2> ; <v3>`, forme du
lot 1 lue au lot 5), et rien d'autre ; **aucune fiche** n'est une entrée (la signature ne la prend pas, et toute autre forme
d'entrée est refusée).

**Règle de croisement** (proposition du lot 7, déclarée, non tranchée) : pour chaque langue, chaque valeur des trois
champs fermés, croisée avec chaque mot du domaine : `<valeur> <mot>`, une espace entre les deux ; ordre : langue (français,
puis anglais), axe, mot ; une chaîne redite n'est gardée qu'une fois, à sa première place.

**Paramètres gelés à remplir** (`ParametresGeles`) : la traduction anglaise des valeurs de la légende et des quatre mots du
domaine **attend une décision** (traduction non écrite dans une pièce scellée) ; la valeur de la passe X sans case attend
Q14. Tant qu'un paramètre manque, la production qui le demande est refusée par son nom (`ParametreGeleNonRempli`), jamais
complétée : aucune traduction n'est devinée, aucune valeur n'est mise par défaut. Les paramètres remplis se chargent d'un
fichier scellé, à l'empreinte donnée (`charger_parametres`).

Bibliothèque standard, et `commun_na_lot7_v1`.
"""

import dataclasses
import datetime
import os

from pole import commun_na_lot7_v1 as cm

VERSION = "requetes-anteriorite-na-v1"
PREFIXE_LIGNE = "case : "  # forme du lot 1 (contrat_fiche_na_v1.valeurs_de_la_case)
SEPARATEUR_LIGNE = " ; "
MOTS_DOMAINE_FR = ("sonde", "moniteur", "activations", "boîte blanche")  # V9, à la lettre
BASES = ("arXiv", "OpenReview", "ACL Anthology", "Semantic Scholar", "Google Scholar", "Alignment Forum", "LessWrong")
RESULTATS_EXAMINES = 30
LANGUES = ("fr", "en")
FORMAT_PARAMETRES = "parametres-classe-i-na-v1"
NOM_JOURNAL_CHAINES = "chaines-classe-i-na-v1.json"
A_REMPLIR = None


class ParametreGeleNonRempli(RuntimeError):
    """Un paramètre gelé attend sa décision : la production qui le demande est refusée, rien n'est deviné."""

    def __init__(self, nom, attend):
        super().__init__(f"paramètre gelé non rempli : {nom} (attend : {attend}) ; production refusée")
        self.nom, self.attend = nom, attend


class ChainesRefusees(ValueError):
    """Une entrée hors de sa forme (ligne de case, paramètres) ; rien n'est réparé."""


@dataclasses.dataclass(frozen=True)
class ParametresGeles:
    """Les valeurs qui attendent une décision. `traduction_valeurs` : {valeur française de la légende : valeur anglaise} ;
    `mots_domaine_en` : les quatre mots du domaine en anglais, dans l'ordre des mots français ; `valeur_passe_x` : la valeur
    de l'axe « menace du programme » d'où partent les chaînes de la passe X (Q14)."""

    traduction_valeurs: object = A_REMPLIR
    mots_domaine_en: object = A_REMPLIR
    valeur_passe_x: object = A_REMPLIR
    statut: str = "gelé, à remplir (Q14 ; traduction)"


PARAMETRES_GELES = ParametresGeles()


def _chaine(t):
    return type(t) is str and t != "" and t == t.strip() and "\n" not in t and "\r" not in t


def charger_parametres(chemin, empreinte_attendue):
    """Les paramètres remplis, d'un fichier scellé à l'empreinte donnée ; une valeur absente reste `A_REMPLIR`."""
    o = cm.lire_json_scelle(chemin, empreinte_attendue)
    permis = {"format", "traduction_valeurs", "mots_domaine_en", "valeur_passe_x", "statut"}
    if not isinstance(o, dict) or o.get("format") != FORMAT_PARAMETRES or set(o) - permis or not _chaine(o.get("statut")):
        raise ChainesRefusees("paramètres hors de leur forme")
    tr, mots, px = o.get("traduction_valeurs"), o.get("mots_domaine_en"), o.get("valeur_passe_x")
    if tr is not None and (not isinstance(tr, dict) or not all(_chaine(k) and _chaine(v) for k, v in tr.items())):
        raise ChainesRefusees("traduction des valeurs hors de sa forme")
    if mots is not None and (not isinstance(mots, list) or len(mots) != len(MOTS_DOMAINE_FR) or not all(map(_chaine, mots))):
        raise ChainesRefusees("mots du domaine en anglais : quatre chaînes, dans l'ordre")
    if px is not None and not _chaine(px):
        raise ChainesRefusees("valeur de la passe X hors de sa forme")
    return ParametresGeles(tr, None if mots is None else tuple(mots), px, o["statut"])


def lire_ligne_de_case(ligne):
    """(identifiant, (v1, v2, v3)) d'une ligne de case ; toute autre entrée est refusée (aucune fiche n'est lue ici)."""
    if type(ligne) is not str or not ligne.startswith(PREFIXE_LIGNE) or "\n" in ligne or "\r" in ligne:
        raise ChainesRefusees("une ligne de case du tirage, et rien d'autre")
    parts = ligne[len(PREFIXE_LIGNE):].split(SEPARATEUR_LIGNE)
    if len(parts) != 4 or not all(_chaine(p) for p in parts):
        raise ChainesRefusees("ligne de case : un identifiant et trois valeurs")
    return parts[0], tuple(parts[1:])


def _croiser(valeurs, mots):
    vues, rendu = set(), []
    for v in valeurs:
        for m in mots:
            c = f"{v} {m}"
            if c not in vues:
                vues.add(c)
                rendu.append(c)
    return rendu


def _anglais(valeurs, parametres):
    tr = parametres.traduction_valeurs
    if tr is A_REMPLIR:
        raise ParametreGeleNonRempli("traduction_valeurs", "décision sur la traduction anglaise des valeurs de la légende")
    if parametres.mots_domaine_en is A_REMPLIR:
        raise ParametreGeleNonRempli("mots_domaine_en", "décision sur la traduction anglaise des mots du domaine")
    manquantes = [v for v in valeurs if v not in tr]
    if manquantes:
        raise ParametreGeleNonRempli("traduction_valeurs", f"{len(manquantes)} valeur(s) de la case sans traduction")
    return [tr[v] for v in valeurs], list(parametres.mots_domaine_en)


def chaines_classe_i(ligne_de_case, parametres=PARAMETRES_GELES, langues=LANGUES):
    """Les chaînes de la classe (i) d'une case : {"case", "fr": [...], "en": [...]}. `langues` vaut les deux par défaut ;
    l'anglais demande les paramètres remplis, sinon refus nommé."""
    if not isinstance(parametres, ParametresGeles):
        raise ChainesRefusees("paramètres construits par `ParametresGeles` ou `charger_parametres`")
    if tuple(langues) not in (("fr",), ("en",), ("fr", "en")):
        raise ChainesRefusees("langues : français, anglais, ou les deux dans cet ordre")
    ident, valeurs = lire_ligne_de_case(ligne_de_case)
    rendu = {"case": ident}
    if "fr" in langues:
        rendu["fr"] = _croiser(valeurs, MOTS_DOMAINE_FR)
    if "en" in langues:
        v_en, m_en = _anglais(valeurs, parametres)
        rendu["en"] = _croiser(v_en, m_en)
    return rendu


def chaines_passe_x(parametres=PARAMETRES_GELES):
    """Passe X, sans case (X-8, proposition ; Q14) : la valeur retenue croisée avec les mots du domaine, en français et en
    anglais. Refusée tant que Q14 et la traduction ne sont pas remplies."""
    if not isinstance(parametres, ParametresGeles):
        raise ChainesRefusees("paramètres construits par `ParametresGeles` ou `charger_parametres`")
    if parametres.valeur_passe_x is A_REMPLIR:
        raise ParametreGeleNonRempli("valeur_passe_x", "Q14, passe X sans case")
    v_en, m_en = _anglais([parametres.valeur_passe_x], parametres)
    return {"case": None, "fr": _croiser([parametres.valeur_passe_x], MOTS_DOMAINE_FR), "en": _croiser(v_en, m_en)}


def produire_journal_chaines(dossier, lignes_de_case, parametres, horloge=None):
    """Le journal des chaînes de la classe (i), produit avant toute lecture de fiche : pour chaque case, ses chaînes dans les
    deux langues et la grille (base × chaîne) des trente premiers résultats à examiner ; scellé, sans écrasement. Rend son
    empreinte. Les deux langues sont exigées : sans les paramètres remplis, rien n'est écrit."""
    cases = [chaines_classe_i(l, parametres, LANGUES) for l in lignes_de_case]
    idents = [c["case"] for c in cases]
    if len(set(idents)) != len(idents) or not idents:
        raise ChainesRefusees("des cases distinctes, au moins une")
    heure = (horloge or (lambda: datetime.datetime.now(datetime.timezone.utc)))().strftime("%Y-%m-%dT%H:%M:%SZ")
    objet = {"version": VERSION, "produit_le": heure, "avant_toute_lecture_de_fiche": True,
             "regle_de_croisement": "valeur × mot, par langue (proposition du lot 7)",
             "statut_des_parametres": parametres.statut, "bases": list(BASES), "resultats_examines": RESULTATS_EXAMINES,
             "cases": [{"case": c["case"], "fr": c["fr"], "en": c["en"],
                        "grille": [{"base": b, "chaine": ch, "examines": RESULTATS_EXAMINES}
                                   for ch in c["fr"] + c["en"] for b in BASES]} for c in cases]}
    return cm.ecrire_json_scelle(os.path.join(dossier, NOM_JOURNAL_CHAINES), objet)
