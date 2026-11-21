"""Nos lentilles (notre R côté sortie, notre S côté entrée) dans la seconde passe : registre, fiche de rangement, condition
de lecture, archive d'ajustement lue en flux, contrôles des matrices.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`), « Entrées » (nos lentilles, condition de lecture, fiche
de rangement, points 1 à 5), « Plan d'analyse » (points 1, 4 et 11), « Liste d'arrêt » (lignes de la v2), « Lignes de
registre », « Code neuf ». Le texte décide, le code suit.

Ce module ne télécharge rien par lui-même : il reçoit un transport (celui du montage) et un flux. Il n'ouvre aucune table. Il
ne lit des registres que les lignes des clés nommées. Il ne recalcule ni ne reformule le verdict d'identité : il le prend dans
la fiche de rangement, mot pour mot. **Jamais de repli** : un fichier introuvable, une autre révision, une autre forme, un
libellé inconnu arrêtent ; rien n'est lu à la place.

Formes fixées par ce code, que le texte ne fixe pas (à contre-lire ; `conformite`, précisions de lecture) :
- la **fiche de rangement** est un fichier JSON dont les champs sont ceux de `CHAMPS_FICHE` ci-dessous ;
- la pièce que cite la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` nomme la lentille par une ligne
  « Lentille nommée : R », « Lentille nommée : S » ou « Lentilles nommées : R et S ».
"""
from __future__ import annotations

import collections
import hashlib
import io
import json
import pickle
import re
import struct
import zlib
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import entrees_v3 as en
from .constantes_v1 import Arret, FormeMalComprise, Refus

# ========================================================================================================================================
# 1. Registre propre : lignes de la v2, place de l'addendum de concentration, état de la première passe
# ========================================================================================================================================
CLES_LUES = (K2.CLE_ADDENDUM,) + K2.CLES_V2 + (K2.CLE_ENTREES_V1, K2.CLE_TABLES_V1, K2.CLE_OUVERTURE_V1)
PREMIERE_PASSE_JAMAIS_LANCEE = "jamais lancée"
PREMIERE_PASSE_ACHEVEE = "achevée"
PREMIERE_PASSE_NON_ACHEVEE = "lancée et non achevée"
MESSAGE_ISSUE_DES_NOEUDS = "issue des nœuds N12 et N17 non conforme au texte scellé"


@dataclass
class EtatRegistre:
    """Lignes du registre propre que la seconde passe lit, par clé, avec leur place (numéro de ligne du fichier)."""
    lignes: dict
    premiere_passe: str

    def presentes(self, cle: str) -> list:
        return self.lignes.get(cle, [])

    def derniere(self, cle: str):
        return self.lignes[cle][-1][1] if self.lignes.get(cle) else None


def etat_premiere_passe(lignes: dict) -> str:
    """Plan, point 11 : « non calculée » veut dire **jamais lancée** (ni `ENTREES-LENTILLES-BBIS` ni `TABLES-LENTILLES-BBIS`) ;
    les deux présentes : achevée ; la ligne des entrées seule : lancée et non achevée (elle n'est pas remplacée) ; la ligne des
    tables sans celle des entrées : arrêt, forme mal comprise."""
    entrees, tables = bool(lignes.get(K2.CLE_ENTREES_V1)), bool(lignes.get(K2.CLE_TABLES_V1))
    if tables and not entrees:
        raise FormeMalComprise(f"{K2.CLE_TABLES_V1} inscrite au registre propre sans {K2.CLE_ENTREES_V1} : arrêt avant tout "
                               "calcul ; nœud (la forme est mal comprise)")
    if tables:
        return PREMIERE_PASSE_ACHEVEE
    return PREMIERE_PASSE_NON_ACHEVEE if entrees else PREMIERE_PASSE_JAMAIS_LANCEE


def exiger_addendum_avant_la_v2(lignes: dict) -> None:
    """Plan, point 1 ; « Liste d'arrêt » : la ligne de l'addendum de concentration est présente, d'une seule ligne, de
    l'empreinte citée en « Documents », et antérieure à toute ligne d'une clé ajoutée par la v2 (place dans le registre et
    heure) ; sinon rien de la seconde passe ne part."""
    addenda = lignes.get(K2.CLE_ADDENDUM, [])
    if not addenda:
        raise Refus(f"{K2.CLE_ADDENDUM} absente du registre propre : rien de la seconde passe ne part ; nœud")
    if len(addenda) > 1:
        raise Refus(f"{K2.CLE_ADDENDUM} en plusieurs lignes ({len(addenda)}) : rien de la seconde passe ne part ; nœud")
    place, ligne = addenda[0]
    if ligne.chemin != K2.ADDENDUM or ligne.sha256 != K2.EMPREINTE_ADDENDUM:
        raise Refus(f"{K2.CLE_ADDENDUM} d'un autre chemin ou d'une autre empreinte que l'addendum scellé cité par le texte : "
                    "rien de la seconde passe ne part ; nœud")
    for cle in K2.CLES_V2:
        for autre_place, autre in lignes.get(cle, []):
            if autre_place < place or autre.heure < ligne.heure:
                raise Refus(f"{K2.CLE_ADDENDUM} postérieure à une ligne d'une clé de la v2 ({cle}) : rien de la seconde passe "
                            "ne part ; nœud")


def exiger_registre_v2(registre_propre: str | Path) -> EtatRegistre:
    """Ce qui est exigé du registre propre avant que rien de la seconde passe ne parte."""
    lignes: dict = {}
    for place, ligne in en.lignes_ordonnees(registre_propre, CLES_LUES):
        lignes.setdefault(ligne.cle, []).append((place, ligne))
    exiger_addendum_avant_la_v2(lignes)
    for cle in K2.CLES_EXIGEES_AVANT_TOUT_V2:
        if not lignes.get(cle):
            raise Refus(f"{cle} absente du registre propre : rien de la seconde passe ne part")
    scellement = lignes[K2.CLE_SCELLEMENT_V2][-1][1]
    if scellement.chemin != K2.TEXTE_V2 or scellement.sha256 != K2.EMPREINTE_TEXTE_V2:
        raise Refus(f"{K2.CLE_SCELLEMENT_V2} ne cite pas le texte scellé de ce code : rien de la seconde passe ne part")
    if lignes.get(K2.CLE_ABANDON_V2):
        raise Refus(f"{K2.CLE_ABANDON_V2} inscrite : la v1 seule est en vigueur ; rien de la seconde passe ne part")
    if lignes.get(K2.CLE_NON_LUES):
        raise Refus(f"{K2.CLE_NON_LUES} inscrite : nos deux lentilles sont définitivement non lues ; la seconde passe s'arrête là")
    place_s, ligne_s = lignes[K2.CLE_SCELLEMENT_V2][0]
    for place, ligne in lignes.get(K2.CLE_OUVERTURE_V1, []):
        if place < place_s or ligne.heure < ligne_s.heure:
            raise Refus(f"{K2.CLE_OUVERTURE_V1} inscrite avant {K2.CLE_SCELLEMENT_V2} : la seconde passe est exposée à la "
                        "première ; rien de la seconde passe ne part ; nœud de Lazar")
    return EtatRegistre(lignes, etat_premiere_passe(lignes))


def exiger_ouverture_permise_des_tables(registre_propre: str | Path) -> None:
    """« Code neuf », procédure : le code n'ouvre une table de la première passe qu'après `SCELLEMENT-LENTILLES-BBIS-V2` ou
    `ABANDON-LENTILLES-BBIS-V2` ; avant : refus."""
    lignes = en.lignes_par_cle(registre_propre, (K2.CLE_SCELLEMENT_V2, K2.CLE_ABANDON_V2))
    if not lignes[K2.CLE_SCELLEMENT_V2] and not lignes[K2.CLE_ABANDON_V2]:
        raise Refus(f"ouverture d'une table par le code avant {K2.CLE_SCELLEMENT_V2} ou {K2.CLE_ABANDON_V2} : refus")


# --- pièce d'un registre, lue sur l'empreinte de sa ligne -------------------------------------------------------------------------------
def lire_piece(racine_depot: str | Path, ligne, quoi: str) -> bytes:
    """Octets de la pièce que cite une ligne du registre propre ; absente, ou d'une autre empreinte que la ligne : arrêt (R11)."""
    chemin = Path(racine_depot) / ligne.chemin
    if not chemin.is_file():
        raise Arret(f"{quoi} : pièce {ligne.chemin} absente sur disque : arrêt (R11)")
    octets = chemin.read_bytes()
    if hashlib.sha256(octets).hexdigest() != ligne.sha256:
        raise Arret(f"{quoi} : pièce {ligne.chemin} d'une autre empreinte que celle de sa ligne de registre : arrêt (R11)")
    return octets


# --- issue des nœuds N12 et N17, recopiée par la pièce de `GO-LENTILLES-BBIS-V2` (« Lignes de registre », point (i)) --------------------
_HEURE = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z"
FORME_N12 = re.compile(r"^N12 : option \(a\) ; ligne d'accord (?P<identifiant>\S+), (?P<heure>" + _HEURE + r")$")
FORME_N17 = re.compile(r"^N17 : option \(a\) au premier palier ; option \(a\) au deuxième palier ; ligne d'accord "
                       r"(?P<identifiant>\S+), (?P<heure>" + _HEURE + r")$")
_AUTRE_ISSUE = {"N12": re.compile(r"option \((?!a\))[a-z]\)"), "N17": re.compile(r"option \((?!a\))[a-z]\)")}
PHRASE_NOEUD_NON_RECOPIE = "Issue du nœud {noeud} : non recopiée par la pièce de `GO-LENTILLES-BBIS-V2` ; celle du texte scellé vaut."


def controler_issue_des_noeuds(texte_piece: str, heure_scellement: str) -> dict:
    """Le code **ne lit dans la pièce aucune option** : la règle qu'il applique est celle du texte. Il contrôle seulement que la
    pièce la recopie. Arrêt nommé : une ligne d'une autre forme ; une autre issue ; une ligne d'accord dont l'heure n'est pas
    strictement antérieure à celle de `SCELLEMENT-LENTILLES-BBIS-V2`, ou absente ou illisible. Pièce muette sur un nœud : rien
    n'arrête ; la phrase « Issue du nœud […] : non recopiée […] » est rendue, pour être écrite en tête."""
    sortie = {"recopiees": {}, "phrases_de_tete": []}
    for noeud, forme in (("N12", FORME_N12), ("N17", FORME_N17)):
        lignes = [l.strip() for l in texte_piece.splitlines() if l.strip().startswith(f"{noeud} :")]
        if not lignes:
            sortie["phrases_de_tete"].append(PHRASE_NOEUD_NON_RECOPIE.format(noeud=noeud))
            continue
        for ligne in lignes:
            m = forme.match(ligne)
            if m is None:
                motif = ("une autre issue que celle du texte" if _AUTRE_ISSUE[noeud].search(ligne)
                         else "heure de la ligne d'accord absente ou illisible" if "ligne d'accord" in ligne
                         and not re.search(_HEURE + r"$", ligne) and FORME_SANS_HEURE[noeud].match(ligne)
                         else "ligne d'une autre forme que celle du texte")
                raise Arret(f"{MESSAGE_ISSUE_DES_NOEUDS} : nœud {noeud} : {motif} : arrêt avant tout calcul ; nœud")
            if not m.group("heure") < heure_scellement:
                raise Arret(f"{MESSAGE_ISSUE_DES_NOEUDS} : nœud {noeud} : ligne d'accord qui n'est pas strictement antérieure à "
                            f"{K2.CLE_SCELLEMENT_V2} : arrêt avant tout calcul ; nœud")
            sortie["recopiees"][noeud] = {"ligne_d_accord": m.group("identifiant"), "heure": m.group("heure")}
    return sortie


FORME_SANS_HEURE = {"N12": re.compile(r"^N12 : option \(a\) ; ligne d'accord"),
                    "N17": re.compile(r"^N17 : option \(a\) au premier palier ; option \(a\) au deuxième palier ; ligne d'accord")}


def exiger_issue_des_noeuds(racine_depot: str | Path, etat: EtatRegistre) -> dict:
    ligne_go = etat.derniere(K2.CLE_GO_V2)
    piece = lire_piece(racine_depot, ligne_go, K2.CLE_GO_V2).decode("utf-8")
    return controler_issue_des_noeuds(piece, etat.presentes(K2.CLE_SCELLEMENT_V2)[0][1].heure)


# ========================================================================================================================================
# 2. Fiche de rangement
# ========================================================================================================================================
CHAMPS_FICHE = {
    "racine": ("critere_identite", "variante_de_la_course", "seconde_course", "avertissement_palier_2", "lecture_seconde_course",
               "lentilles"),
    "lentille": ("depot", "revision", "chemin", "taille", "sha256_avant_envoi", "sha256_relecture", "verdict_identite", "reprise",
                 "verdict_scelle", "sortie_du_programme", "audit", "phrase_du_declencheur_vi", "diffs_out",
                 "seconde_course_par_couche"),
    "sortie_du_programme": ("chemin", "sha256", "ecart_max_abs_diffs_float64", "ecart_max_abs_diffs",
                            "series_export_R_sans_critere", "matrices_moities_egales", "declencheurs", "audit_requis"),
    "diffs_out": ("ajustement_du_18_novembre", "reajustement"),
}
SERIES_R = ("npR_notre_R", "identite_notre_R")          # écart à la lentille publique, écart à l'identité (programme version 4)
_RE_REVISION = re.compile(r"^[0-9a-f]{40}$")
_RE_SHA = re.compile(r"^[0-9a-f]{64}$")


def _piece_scellee(objet) -> bool:
    """Une pièce est tenue pour « versée scellée » quand la fiche en donne le chemin et l'empreinte entière."""
    return (isinstance(objet, dict) and isinstance(objet.get("chemin"), str) and bool(objet.get("chemin"))
            and isinstance(objet.get("sha256"), str) and bool(_RE_SHA.match(objet["sha256"])))


def lire_fiche(racine_depot: str | Path, etat: EtatRegistre) -> dict:
    """« Liste d'arrêt » : `RANGEMENT-NOS-LENTILLES-BBIS` absente ; fiche d'une autre empreinte que celle de la ligne, ou sans
    révision de 40 caractères, ou sans verdict d'identité pour aucune des deux lentilles, ou dont les deux SHA-256 d'un
    fichier diffèrent : rien de la seconde passe ne part ; nœud. La dernière ligne inscrite désigne la fiche en vigueur (une
    fiche neuve, sous un nom neuf, R12, remplace la précédente)."""
    ligne = etat.derniere(K2.CLE_RANGEMENT)
    if ligne is None:
        raise Refus(f"{K2.CLE_RANGEMENT} absente du registre propre : rien de la seconde passe ne part ; nœud")
    chemin = Path(racine_depot) / ligne.chemin
    if not chemin.is_file():
        raise Refus(f"fiche de rangement {ligne.chemin} absente sur disque : rien de la seconde passe ne part ; nœud")
    octets = chemin.read_bytes()
    if hashlib.sha256(octets).hexdigest() != ligne.sha256:
        raise Refus("fiche de rangement d'une autre empreinte que celle de sa ligne de registre : rien de la seconde passe ne "
                    "part ; nœud")
    try:
        fiche = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise FormeMalComprise("fiche de rangement : JSON illisible : arrêt ; nœud (la forme est mal comprise)") from None
    lentilles = fiche.get("lentilles") if isinstance(fiche, dict) else None
    if not isinstance(lentilles, dict) or set(lentilles) - set(K2.NOS_LENTILLES):
        raise FormeMalComprise("fiche de rangement : champ « lentilles » absent ou d'une autre forme (R, S) : arrêt ; nœud")
    verdicts = 0
    for lettre in K2.NOS_LENTILLES:
        l = lentilles.get(lettre)
        if l is None:
            continue
        if not isinstance(l, dict):
            raise FormeMalComprise(f"fiche de rangement : lentille {lettre} d'une autre forme : arrêt ; nœud")
        verdicts += int(isinstance(l.get("verdict_identite"), str) and bool(l["verdict_identite"].strip()))
        if _porte_un_fichier(l):
            if not isinstance(l.get("revision"), str) or not _RE_REVISION.match(l["revision"]):
                raise Refus(f"fiche de rangement : révision absente ou courte pour la lentille {lettre} (40 caractères exigés) : "
                            "rien de la seconde passe ne part ; nœud")
            if l.get("sha256_avant_envoi") != l.get("sha256_relecture") or not _RE_SHA.match(str(l.get("sha256_relecture"))):
                raise Refus(f"fiche de rangement : les deux SHA-256 du fichier de la lentille {lettre} diffèrent ou manquent : "
                            "rien de la seconde passe ne part ; nœud")
    if verdicts == 0:
        raise Refus("fiche de rangement sans verdict d'identité pour aucune des deux lentilles : rien de la seconde passe ne "
                    "part ; nœud")
    fiche["_ligne"] = {"chemin": ligne.chemin, "sha256": ligne.sha256, "heure": ligne.heure}
    return fiche


def _porte_un_fichier(l: dict) -> bool:
    return any(l.get(c) is not None for c in ("depot", "revision", "chemin", "taille", "sha256_avant_envoi", "sha256_relecture"))


# --- phrase que le verdict écrit au déclencheur (vi) (CI, § 6 ; « Entrées », fiche) ---------------------------------------------------
VI_DEBUT = "pour R, "
VI_FIN = " malgré des octets d'ajustement différents ; audit sans contrôle manqué"
VI_FORME_1 = "31 matrices des moitiés égales sur 31"
MESSAGE_PHRASE_VI = "phrase du déclencheur (vi) : forme mal comprise"


def _est_forme_series(mots: str) -> bool:
    """Forme (2), « série … inchangée », ou forme (3), « séries … inchangées » : une seule fois, sans la forme (1) dedans."""
    for debut, fin in (("série ", " inchangée"), ("séries ", " inchangées")):
        if mots.startswith(debut) and mots.endswith(fin):
            milieu = mots[len(debut):len(mots) - len(fin)]
            return "inchangée" not in milieu and VI_FORME_1 not in milieu and bool(milieu.strip())
    return False


def forme_de_la_phrase_vi(phrase: str) -> bool:
    """Vrai si la phrase a l'une des formes admises : début, fin, et entre les deux la forme (1), la forme (2), la forme (3),
    ou la forme (1) et l'une des formes (2) ou (3) jointes par « et », dans un ordre ou dans l'autre."""
    if not isinstance(phrase, str) or not phrase.startswith(VI_DEBUT) or not phrase.endswith(VI_FIN):
        return False
    milieu = phrase[len(VI_DEBUT):len(phrase) - len(VI_FIN)]
    if milieu == VI_FORME_1 or _est_forme_series(milieu):
        return True
    if milieu.startswith(VI_FORME_1 + " et "):
        return _est_forme_series(milieu[len(VI_FORME_1) + 4:])
    if milieu.endswith(" et " + VI_FORME_1):
        return _est_forme_series(milieu[:len(milieu) - len(VI_FORME_1) - 4])
    return False


def controler_phrase_vi(lettre: str, l: dict, palier: int | None) -> str | None:
    """Place et forme de la phrase du déclencheur (vi). Rend la phrase à recopier après la phrase permise, ou `None`.
    Champ absent pour notre R au deuxième palier ; « aucune » là où la phrase est attendue ; phrase là où elle ne l'est pas
    (sans (vi), sans audit sans contrôle manqué, pour notre S, à un autre palier) ; autre forme : arrêt, forme mal comprise."""
    present = "phrase_du_declencheur_vi" in l and l["phrase_du_declencheur_vi"] is not None
    valeur = l.get("phrase_du_declencheur_vi")
    if lettre != "R" or palier != 2:
        if present and valeur != K2.AUCUNE:
            raise FormeMalComprise(f"{MESSAGE_PHRASE_VI} : phrase présente là où elle n'est pas attendue (lentille {lettre}, "
                                   f"palier {palier}) : arrêt avant tout calcul ; nœud")
        return None
    if not present:
        raise FormeMalComprise(f"{MESSAGE_PHRASE_VI} : champ absent de la fiche pour notre R au deuxième palier : arrêt avant "
                               "tout calcul ; nœud")
    sortie = l.get("sortie_du_programme") or {}
    rendu = any(isinstance(d, str) and d.startswith("(vi)") for d in sortie.get("declencheurs", []))
    attendue = rendu and _audit_tenu(l)
    if not attendue:
        if valeur != K2.AUCUNE:
            raise FormeMalComprise(f"{MESSAGE_PHRASE_VI} : phrase présente là où elle n'est pas attendue (déclencheur (vi) non "
                                   "rendu, ou audit non cité sans contrôle manqué) : arrêt avant tout calcul ; nœud")
        return None
    if valeur == K2.AUCUNE:
        raise FormeMalComprise(f"{MESSAGE_PHRASE_VI} : « aucune » alors que le déclencheur (vi) est rendu et l'audit cité sans "
                               "contrôle manqué : arrêt avant tout calcul ; nœud")
    if not forme_de_la_phrase_vi(valeur):
        raise FormeMalComprise(f"{MESSAGE_PHRASE_VI} : phrase d'une autre forme que les formes admises : arrêt avant tout "
                               "calcul ; nœud")
    return valeur


# ========================================================================================================================================
# 3. Condition de lecture (chaque lentille jugée séparément)
# ========================================================================================================================================
COURSE_AJUSTEMENT_SEUL = "ajustement seul"
COURSE_REJOUEE = "course rejouée"
COURSE_REJOUEE_INCOMPLETE = "course rejouée, seconde course incomplète"
COURSE_REJOUEE_MUETTE = "course rejouée, achèvement de la seconde course non dit par la fiche"
NON_LUE = "Non lue : notre lentille {lettre} {motif}"
MOTIF_ABSENTE = "absente"
MOTIF_PALIER_1_SANS_AUDIT = "au premier palier sans audit versé"
MOTIF_SANS_MESURE_PROPRE = "au deuxième palier, sans mesure propre ; aucune lecture sans nœud de Lazar"
MOTIF_FICHE_MUETTE = ("au deuxième palier, fiche muette sur l'achèvement de la seconde course ; aucune lecture sans nœud de "
                      "Lazar")
MOTIF_SANS_AVERTISSEMENT = f"au deuxième palier sans la ligne {K2.CLE_AVERTISSEMENT}"
MOTIF_SANS_LECTURE_SECONDE_COURSE = (f"au deuxième palier, en course rejouée menée en entier, sans la ligne "
                                     f"{K2.CLE_LECTURE_SECONDE_COURSE}")
MOTIF_AUDIT_DU = "dont l'audit est dû et n'est pas versé scellé, sans contrôle manqué"
MOTIF_VERDICT_ABSENT = "sans verdict d'identité dans la fiche de rangement"
MOTIF_VERDICT_NON_SCELLE = "dont le verdict d'identité n'est pas scellé"
MOTIF_CRITERE = "dont le critère d'identité n'est pas scellé à l'empreinte citée par le texte"
MOTIF_AUTRE_VERDICT = "au verdict d'identité « {verdict} »"
NON_LUE_COUCHE = "Non lue à la couche {couche} : {motif}"
MOTIF_STABILITE = "stabilité non tenue dans les deux ajustements"
MOTIF_STABILITE_ABSENTE = "valeur de la différence entre moitiés absente de la fiche"
PHRASE_SANS_MESURE = ("Cette lentille n'a pour mesure à elle que la différence entre moitiés de son ajustement (et, pour notre R, "
                      "les deux séries d'écart) ; aucune des mesures de la tranche du 18 novembre n'a été refaite sur elle.")
FORME_LENTILLE_NOMMEE = re.compile(r"^\s*[-*]?\s*Lentilles? nommées? : (R|S|R et S)\s*$", re.MULTILINE)


@dataclass
class Condition:
    """Ce que la condition de lecture rend pour une de nos lentilles. `mesures_refaites` remplit le dernier crochet de la
    phrase permise du deuxième palier (vrai : « ont été refaites […] et sont rapportées à côté » ; faux : « n'ont pas été
    refaites »). `motif` est la ligne « Non lue : […] » entière."""
    lettre: str
    verdict: str | None
    palier: int | None = None
    reprise: bool = False
    lue: bool = False
    motif: str | None = None
    mesures_refaites: bool | None = None
    phrase_sans_mesure: bool = False
    phrase_vi: str | None = None
    audit_du: bool = False
    couches: dict = field(default_factory=dict)
    chiffres: dict = field(default_factory=dict)

    def lue_a(self, couche: int) -> bool:
        return bool(self.lue and self.couches.get(int(couche), {}).get("lue"))

    def table(self) -> dict:
        return {"lentille": self.lettre, "verdict_identite": self.verdict, "palier": self.palier, "reprise": self.reprise,
                "lue": self.lue, "motif": self.motif, "mesures_refaites": self.mesures_refaites,
                "phrase_sans_mesure": self.phrase_sans_mesure, "phrase_du_declencheur_vi": self.phrase_vi,
                "audit_du": self.audit_du, "couches": {str(c): dict(v) for c, v in sorted(self.couches.items())},
                "chiffres_recopies_de_la_fiche": dict(self.chiffres)}


def course_du_reajustement(fiche: dict) -> str:
    """La ligne « Course du réajustement », dans l'une de ses quatre valeurs. Une variante absente ou inconnue : arrêt."""
    variante = fiche.get("variante_de_la_course")
    if variante == K2.VARIANTE_AJUSTEMENT_SEUL:
        return COURSE_AJUSTEMENT_SEUL
    if variante != K2.VARIANTE_COURSE_REJOUEE:
        raise FormeMalComprise(f"fiche de rangement : variante de la course {variante!r} inconnue : arrêt ; nœud (la forme est "
                               "mal comprise)")
    achevement = fiche.get("seconde_course")
    if achevement == K2.SECONDE_COURSE_ENTIERE:
        return COURSE_REJOUEE
    if achevement == K2.SECONDE_COURSE_INCOMPLETE:
        return COURSE_REJOUEE_INCOMPLETE
    if achevement is None:
        return COURSE_REJOUEE_MUETTE
    raise FormeMalComprise(f"fiche de rangement : achèvement de la seconde course {achevement!r} inconnu : arrêt ; nœud (la "
                           "forme est mal comprise)")


def palier_du_verdict(lettre: str, verdict) -> tuple[str, bool]:
    """Classe le libellé du verdict : (« palier 1 », reprise), (« palier 2 », faux), (« autre », faux), (« absente », faux),
    (« sans verdict », faux). Le premier palier se reconnaît suivi ou non de « ; reprise sur sauvegarde notée » ; tout autre
    ajout, et tout libellé inconnu : arrêt, forme mal comprise."""
    if verdict is None or (isinstance(verdict, str) and not verdict.strip()):
        return "sans verdict", False
    if not isinstance(verdict, str):
        raise FormeMalComprise(f"verdict d'identité de la lentille {lettre} d'une autre forme : arrêt ; nœud")
    if verdict == K2.PALIER_1:
        return "palier 1", False
    if verdict == K2.PALIER_1 + K2.SUITE_REPRISE:
        return "palier 1", True
    if verdict == K2.PALIER_2:
        return "palier 2", False
    if verdict in (K2.DIFFERENTE, K2.NON_COMPARABLE, K2.SUSPENDUE):
        return "autre", False
    if verdict == K2.NON_REAJUSTEE[lettre]:
        return "absente", False
    raise FormeMalComprise(f"verdict d'identité de la lentille {lettre} : libellé inconnu ({verdict!r}) : arrêt ; nœud (la forme "
                           "est mal comprise)")


def _audit_tenu(l: dict) -> bool:
    audit = l.get("audit")
    return _piece_scellee(audit) and audit.get("controles_manques") == 0


def _audit_du(l: dict, palier: int) -> bool:
    """CI, § 6 : l'audit est dû dès que la sortie du programme rend au moins un déclencheur ; toujours au premier palier."""
    sortie = l.get("sortie_du_programme") or {}
    return bool(palier == 1 or sortie.get("declencheurs") or sortie.get("audit_requis"))


def lentilles_nommees_par_le_noeud(racine_depot: str | Path, etat: EtatRegistre) -> set:
    """Nœud N12, option (a) : la lecture attend la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`, **postérieure** à la
    ligne d'avertissement (place dans le registre et heure, strictement, et à toute ligne d'avertissement) ; la pièce qu'elle
    cite nomme la lentille. La ligne d'avertissement seule n'ouvre pas la lecture ; une ligne antérieure non plus."""
    avertissements = etat.presentes(K2.CLE_AVERTISSEMENT)
    nommees: set = set()
    if not avertissements:
        return nommees
    place_a = max(p for p, _ in avertissements)
    heure_a = max(l.heure for _, l in avertissements)
    for place, ligne in etat.presentes(K2.CLE_NOEUD_AJUSTEMENT_SEUL):
        if not (place > place_a and ligne.heure > heure_a):
            continue
        texte = lire_piece(racine_depot, ligne, K2.CLE_NOEUD_AJUSTEMENT_SEUL).decode("utf-8")
        for m in FORME_LENTILLE_NOMMEE.finditer(texte):
            nommees |= set(m.group(1).replace(" et ", " ").split())
    return nommees


def _chiffres(lettre: str, l: dict) -> dict:
    """Chiffres de la sortie du programme de comparaison, tels que la fiche les recopie. Le champ `critere` de cette sortie
    est une étiquette : il n'est ni lu ni recopié."""
    sortie = l.get("sortie_du_programme") or {}
    chiffres = {c: sortie.get(c) for c in ("ecart_max_abs_diffs_float64", "ecart_max_abs_diffs", "declencheurs", "audit_requis")}
    if lettre == "R":
        series = sortie.get("series_export_R_sans_critere")
        chiffres["series_export_R_sans_critere"] = (
            {s: {c: series[s].get(c) for c in ("ecart_max_abs", "ref_min", "ref_max")} for s in SERIES_R
             if isinstance(series.get(s), dict)} if isinstance(series, dict) else None)
        chiffres["matrices_moities_egales"] = sortie.get("matrices_moities_egales")
    return chiffres


def _exiger_chiffres_du_deuxieme_palier(lettre: str, chiffres: dict) -> None:
    """Les crochets de la phrase permise du deuxième palier sont obligatoires : un chiffre absent de la fiche arrête."""
    def nombre(x) -> bool:
        return isinstance(x, (int, float)) and not isinstance(x, bool) and np.isfinite(x)
    manque = not nombre(chiffres.get("ecart_max_abs_diffs_float64"))
    if lettre == "R":
        series = chiffres.get("series_export_R_sans_critere") or {}
        manque = manque or any(not nombre((series.get(s) or {}).get(c)) for s in SERIES_R
                               for c in ("ecart_max_abs", "ref_min", "ref_max"))
    if manque:
        raise FormeMalComprise(f"fiche de rangement : chiffres de la sortie du programme absents pour notre lentille {lettre} au "
                               "deuxième palier (crochets obligatoires de la phrase permise) : arrêt ; nœud")


def _stabilite(l: dict, cond: Condition, course: str) -> None:
    """Stabilité par couche, à tous les paliers : différence entre moitiés au plus 0,10 **dans les deux ajustements** ; au
    deuxième palier en course rejouée menée en entier, couche écartée par la lecture de la seconde course."""
    diffs = l.get("diffs_out") or {}
    limites = l.get("seconde_course_par_couche") or {}
    for couche in K.COUCHES:
        valeurs = [(diffs.get(a) or {}).get(str(couche)) for a in CHAMPS_FICHE["diffs_out"]]
        case = {"lue": True, "motif": None, "diffs": dict(zip(CHAMPS_FICHE["diffs_out"], valeurs)), "limite": None}
        if any(not isinstance(v, (int, float)) or isinstance(v, bool) or not np.isfinite(v) for v in valeurs):
            case.update(lue=False, motif=NON_LUE_COUCHE.format(couche=couche, motif=MOTIF_STABILITE_ABSENTE))
        elif any(v > K2.STABILITE_MAX for v in valeurs):
            case.update(lue=False, motif=NON_LUE_COUCHE.format(couche=couche, motif=MOTIF_STABILITE))
        if cond.palier == 2 and course == COURSE_REJOUEE:
            limite = limites.get(str(couche))
            if not isinstance(limite, dict) or not isinstance(limite.get("limite"), str) or not isinstance(limite.get("ecartee"), bool):
                raise FormeMalComprise(f"fiche de rangement : limite de la lecture de la seconde course absente pour notre "
                                       f"lentille {cond.lettre} à la couche {couche} : arrêt ; nœud")
            case["limite"] = limite["limite"]
            if limite["ecartee"] and case["lue"]:
                case.update(lue=False, motif=NON_LUE_COUCHE.format(couche=couche, motif=limite["limite"]))
        cond.couches[couche] = case


def condition_de_lecture(fiche: dict, etat: EtatRegistre, racine_depot: str | Path) -> dict:
    """Applique la condition de lecture de « Entrées » à chacune de nos deux lentilles. Rend `{« R » : Condition, « S » :
    Condition, « course » : ligne « Course du réajustement »}`. Aucune ligne `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`
    n'est exigée ni lue, à aucun palier (nœud N17, option (a))."""
    course = course_du_reajustement(fiche)
    critere = fiche.get("critere_identite") or {}
    critere_tenu = critere.get("chemin") == K2.CRITERE_IDENTITE and critere.get("sha256") == K2.EMPREINTE_CRITERE_IDENTITE
    nommees = None
    sortie: dict = {"course": course}
    for lettre in K2.NOS_LENTILLES:
        l = fiche["lentilles"].get(lettre) or {}
        verdict = l.get("verdict_identite")
        sorte, reprise = palier_du_verdict(lettre, verdict)
        cond = Condition(lettre, verdict if sorte not in ("sans verdict",) else None, reprise=reprise)
        cond.palier = {"palier 1": 1, "palier 2": 2}.get(sorte)
        cond.phrase_vi = controler_phrase_vi(lettre, l, cond.palier)
        cond.chiffres = _chiffres(lettre, l)

        def non_lue(motif: str) -> None:
            cond.lue, cond.motif = False, NON_LUE.format(lettre=lettre, motif=motif)

        if sorte == "sans verdict":
            non_lue(MOTIF_VERDICT_ABSENT)
        elif sorte == "absente":
            non_lue(MOTIF_ABSENTE)
        elif sorte == "autre":
            non_lue(MOTIF_AUTRE_VERDICT.format(verdict=verdict))
        else:
            cond.audit_du = _audit_du(l, cond.palier)
            if cond.palier == 1 and l.get("sha256_relecture") != K2.EMPREINTE_18_NOVEMBRE[lettre]:
                raise Arret(f"notre lentille {lettre} au premier palier avec une empreinte autre que celle du 18 novembre : "
                            "arrêt ; message à la session principale ; la lentille n'est pas lue sans version neuve")
            if cond.palier == 2:
                _exiger_chiffres_du_deuxieme_palier(lettre, cond.chiffres)
            if not critere_tenu:
                non_lue(MOTIF_CRITERE)
            elif not _piece_scellee(l.get("verdict_scelle")):
                non_lue(MOTIF_VERDICT_NON_SCELLE)
            elif cond.palier == 1:
                if _audit_tenu(l):
                    cond.lue = True
                else:
                    non_lue(MOTIF_PALIER_1_SANS_AUDIT)
            elif not etat.presentes(K2.CLE_AVERTISSEMENT):
                non_lue(MOTIF_SANS_AVERTISSEMENT)
            elif cond.audit_du and not _audit_tenu(l):
                non_lue(MOTIF_AUDIT_DU)
            elif course == COURSE_REJOUEE_MUETTE:
                non_lue(MOTIF_FICHE_MUETTE)                      # avec la ligne du mot de Lazar comme sans elle
            elif course == COURSE_REJOUEE:
                if etat.presentes(K2.CLE_LECTURE_SECONDE_COURSE):
                    cond.lue, cond.mesures_refaites = True, True
                else:
                    non_lue(MOTIF_SANS_LECTURE_SECONDE_COURSE)
            else:                                                # ajustement seul, ou seconde course incomplète
                if nommees is None:
                    nommees = lentilles_nommees_par_le_noeud(racine_depot, etat)
                if lettre in nommees:
                    cond.lue, cond.mesures_refaites, cond.phrase_sans_mesure = True, False, True
                else:
                    non_lue(MOTIF_SANS_MESURE_PROPRE)
        if cond.lue:
            _stabilite(l, cond, course)
        sortie[lettre] = cond
    return sortie


# ========================================================================================================================================
# 4. Archive d'ajustement écrite par `torch.save`, lue en flux
# ========================================================================================================================================
_STOCKAGES = {"FloatStorage": ("<f4", 4), "DoubleStorage": ("<f8", 8), "HalfStorage": ("<f2", 2), "BFloat16Storage": ("<u2", 2),
              "LongStorage": ("<i8", 8), "IntStorage": ("<i4", 4), "ShortStorage": ("<i2", 2), "CharStorage": ("i1", 1),
              "ByteStorage": ("u1", 1), "BoolStorage": ("?", 1)}
CLASSES_PERMISES = ((("collections", "OrderedDict"),) + (("torch._utils", "_rebuild_tensor_v2"),)
                    + tuple(("torch", nom) for nom in _STOCKAGES))
PETIT_MAX = 16 * 1024 * 1024        # borne d'un enregistrement dont la taille n'est donnée que par son descripteur
SIGNATURE_LOCALE, SIGNATURE_DESCRIPTEUR = b"PK\x03\x04", b"PK\x07\x08"
SIGNATURES_DE_FIN = (b"PK\x01\x02", b"PK\x05\x06", b"PK\x06\x06", b"PK\x06\x07")


@dataclass(frozen=True)
class _TypeStockage:
    nom: str


@dataclass(frozen=True)
class StockageFactice:
    """Stockage factice : la clé de son enregistrement, son type et son nombre d'éléments ; aucun octet."""
    cle: str
    type: str
    elements: int

    @property
    def octets(self) -> int:
        return self.elements * _STOCKAGES[self.type][1]


@dataclass(frozen=True)
class TenseurFactice:
    stockage: StockageFactice
    decalage: int
    forme: tuple
    pas: tuple

    @property
    def contigu(self) -> bool:
        attendu, produit = [], 1
        for n in reversed(self.forme):
            attendu.append(produit)
            produit *= int(n)
        return tuple(self.pas) == tuple(reversed(attendu))

    @property
    def elements(self) -> int:
        return int(np.prod(self.forme, dtype=np.int64)) if self.forme else 1


def _reconstruire_tenseur(stockage, decalage, forme, pas, *reste):
    if not isinstance(stockage, StockageFactice):
        raise Arret("archive d'ajustement : tenseur sans stockage reconnu : arrêt avant tout calcul ; nœud")
    return TenseurFactice(stockage, int(decalage), tuple(int(x) for x in forme), tuple(int(x) for x in pas))


class _Depickleur(pickle.Unpickler):
    """Dépickleur à **liste blanche de classes**, sur stockages factices : aucune classe hors de `CLASSES_PERMISES` n'est
    chargée, aucun octet de tenseur n'est lu."""

    def find_class(self, module, name):
        if (module, name) == ("collections", "OrderedDict"):
            return collections.OrderedDict
        if (module, name) == ("torch._utils", "_rebuild_tensor_v2"):
            return _reconstruire_tenseur
        if module == "torch" and name in _STOCKAGES:
            return _TypeStockage(name)
        raise Arret(f"archive d'ajustement : `data.pkl` demande une classe hors de la liste blanche ({module}.{name}) : arrêt "
                    "avant tout calcul ; nœud (la forme est mal comprise)")

    def persistent_load(self, pid):
        if (not isinstance(pid, tuple) or len(pid) < 5 or pid[0] != "storage" or not isinstance(pid[1], _TypeStockage)):
            raise Arret("archive d'ajustement : identifiant persistant d'une autre forme : arrêt avant tout calcul ; nœud")
        return StockageFactice(str(pid[2]), pid[1].nom, int(pid[4]))


def depickler(octets: bytes):
    try:
        return _Depickleur(io.BytesIO(octets)).load()
    except Arret:
        raise
    except Exception as e:   # pickle tronqué ou d'une autre forme
        raise Arret(f"archive illisible : `data.pkl` ne se lit pas ({type(e).__name__}) : arrêt avant tout calcul ; nœud") from None


@dataclass
class Attendu:
    """Ce que le texte attend d'un fichier d'ajustement (table de « Entrées »). Les essais passent de petites dimensions."""
    lettre: str
    n_couches: int
    largeur: int = K.LARGEUR
    couches: tuple = K.COUCHES
    n_docs: tuple = K2.N_DOCS
    next_doc: int = K2.NEXT_DOC
    meta: dict | None = None

    @classmethod
    def du_texte(cls, lettre: str, meta: dict) -> "Attendu":
        return cls(lettre, K2.N_COUCHES_OUT[lettre], meta=dict(meta))


def meta_attendue_de_s(chemin_piece: str | Path, sha256: str = K2.EMPREINTE_PIECE_META_S) -> dict:
    """`meta` attendue de notre S : lue par le code dans la pièce du 18 novembre, **champ `meta` seul**, sur son empreinte ;
    pièce d'une autre empreinte : arrêt ; nœud (jamais une correction silencieuse)."""
    chemin = Path(chemin_piece)
    if not chemin.is_file():
        raise Arret("pièce du 18 novembre de notre S absente sur disque : arrêt ; nœud")
    octets = chemin.read_bytes()
    if hashlib.sha256(octets).hexdigest() != sha256:
        raise Arret("pièce du 18 novembre de notre S d'une autre empreinte que celle citée par le texte : arrêt ; nœud")
    try:
        meta = json.loads(octets.decode("utf-8"))["meta"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        raise FormeMalComprise("pièce du 18 novembre de notre S : champ `meta` illisible : arrêt ; nœud") from None
    del octets
    if not isinstance(meta, dict):
        raise FormeMalComprise("pièce du 18 novembre de notre S : champ `meta` d'une autre forme : arrêt ; nœud")
    return {c: meta.get(c) for c in K2.CHAMPS_META}


class ExtracteurAjustement:
    """Reçoit le flux d'un fichier d'ajustement (archive zip **non compressée** écrite par `torch.save`) ; calcule le SHA-256
    et la taille du flux entier ; lit `data.pkl`, **premier enregistrement**, par le dépickleur à liste blanche ; puis, dans les
    seuls enregistrements des stockages de `sums[("out", 0)]` et `sums[("out", 1)]`, n'écrit sur disque que les octets des
    couches voulues (fichiers `.partiel`, rendus définitifs par `conclure`). Tout autre enregistrement est lu pour l'empreinte
    et jeté. Le fichier entier n'est jamais écrit.

    Taille d'un enregistrement : celle de son en-tête local quand il la porte ; sinon (drapeau du descripteur de données, ce
    qu'écrit la version de torch de l'essai opposable) celle que `data.pkl` donne au stockage, ou, pour un petit
    enregistrement, celle que porte son descripteur, cherché et vérifié par sa somme de contrôle."""

    def __init__(self, attendu: Attendu, dossier: Path):
        self.attendu, self.dossier = attendu, Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.hachage, self.position, self.tampon = hashlib.sha256(), 0, bytearray()
        self.etat = "en-tete"
        self.prefixe: str | None = None
        self.enregistrements: list[dict] = []
        self.objet = None
        self.tenseurs: dict = {}
        self.tailles: dict[str, int] = {}
        self.plages: dict[str, list] = {}
        self.fichiers: dict[tuple, object] = {}
        self.petits: dict[str, bytes] = {}
        self._courant: dict | None = None

    # -- noms des fichiers extraits ------------------------------------------------------------------------------------------------
    def nom_fichier(self, moitie: int, couche: int) -> str:
        return f"notre-{self.attendu.lettre}-out-moitie{moitie}-c{couche}.brut"

    # -- réception ------------------------------------------------------------------------------------------------------------------
    def recevoir(self, bloc: bytes) -> None:
        self.hachage.update(bloc)
        self.position += len(bloc)
        self.tampon += bloc
        while self._avancer():
            pass

    def _illisible(self, motif: str) -> Arret:
        return Arret(f"archive illisible ({motif}) : arrêt avant tout calcul ; nœud (la forme est mal comprise)")

    def _avancer(self) -> bool:
        t = self.tampon
        if self.etat == "fin":
            t.clear()
            return False
        if self.etat == "en-tete":
            if len(t) < 4:
                return False
            if bytes(t[:4]) in SIGNATURES_DE_FIN:
                if not self.enregistrements:
                    raise self._illisible("aucun enregistrement")
                self.etat = "fin"
                return True
            if bytes(t[:4]) != SIGNATURE_LOCALE:
                raise self._illisible("signature d'enregistrement absente")
            if len(t) < 30:
                return False
            (_, _, drapeaux, methode, _, _, _, comprime, taille, n_nom, n_extra) = struct.unpack("<IHHHHHIIIHH", bytes(t[:30]))
            if len(t) < 30 + n_nom + n_extra:
                return False
            nom = bytes(t[30:30 + n_nom]).decode("utf-8", errors="replace")
            extra = bytes(t[30 + n_nom:30 + n_nom + n_extra])
            del t[:30 + n_nom + n_extra]
            if not self.enregistrements:
                if not (nom == "data.pkl" or nom.endswith("/data.pkl")):
                    raise Arret("archive d'ajustement : `data.pkl` n'est pas le premier enregistrement : arrêt avant tout calcul ; "
                                "nœud (la forme est mal comprise)")
                self.prefixe = nom[:-len("data.pkl")]
            if methode != 0:
                raise Arret(f"archive d'ajustement : enregistrement compressé ({nom}) : arrêt avant tout calcul ; nœud (la forme "
                            "est mal comprise)")
            if taille == 0xFFFFFFFF or comprime == 0xFFFFFFFF:
                taille, comprime = self._tailles_zip64(extra, taille, comprime)
            descripteur = bool(drapeaux & 0x0008)
            if taille != comprime:
                raise Arret(f"archive d'ajustement : enregistrement compressé ({nom}) : arrêt avant tout calcul ; nœud (la forme "
                            "est mal comprise)")
            connue = taille if (taille or not descripteur) else self._taille_par_data_pkl(nom)
            self._courant = {"nom": nom, "taille": connue, "descripteur": descripteur, "recu": 0, "crc": 0,
                             "garde": bytearray() if self._est_petit(nom, connue) else None}
            self.etat = "donnees" if connue is not None else "cherche"
            return True
        if self.etat == "donnees":
            c = self._courant
            n = min(len(t), c["taille"] - c["recu"])
            if n:
                self._deposer(c, memoryview(t)[:n])
                del t[:n]
            if c["recu"] < c["taille"]:
                return False
            self.etat = "descripteur" if c["descripteur"] else "clos"
            return True
        if self.etat == "cherche":
            return self._chercher_descripteur()
        if self.etat == "descripteur":
            c = self._courant
            if len(t) < 28 and not (len(t) >= 16 and False):
                return False
            if bytes(t[:4]) != SIGNATURE_DESCRIPTEUR:
                raise self._illisible(f"descripteur de données absent après {c['nom']}")
            crc, a32, b32 = struct.unpack("<III", bytes(t[4:16]))
            a64, b64 = struct.unpack("<QQ", bytes(t[8:24]))
            if a32 == b32 == c["taille"] and (bytes(t[16:20]) == SIGNATURE_LOCALE or bytes(t[16:20]) in SIGNATURES_DE_FIN):
                longueur = 16
            elif a64 == b64 == c["taille"]:
                longueur = 24
            else:
                raise self._illisible(f"descripteur de données de {c['nom']} d'une autre taille que l'enregistrement")
            if c["garde"] is not None and zlib.crc32(bytes(c["garde"])) != crc:
                raise self._illisible(f"somme de contrôle de {c['nom']}")
            del t[:longueur]
            self.etat = "clos"
            return True
        if self.etat == "clos":
            self._clore()
            self.etat = "en-tete"
            return True
        raise Arret(f"état d'analyse inconnu ({self.etat})")

    @staticmethod
    def _tailles_zip64(extra: bytes, taille: int, comprime: int) -> tuple[int, int]:
        i = 0
        while i + 4 <= len(extra):
            ident, n = struct.unpack("<HH", extra[i:i + 4])
            if ident == 0x0001:
                champs = extra[i + 4:i + 4 + n]
                j = 0
                if taille == 0xFFFFFFFF and j + 8 <= len(champs):
                    taille, j = struct.unpack("<Q", champs[j:j + 8])[0], j + 8
                if comprime == 0xFFFFFFFF and j + 8 <= len(champs):
                    comprime = struct.unpack("<Q", champs[j:j + 8])[0]
                return taille, comprime
            i += 4 + n
        raise Arret("archive illisible (tailles sur 64 bits annoncées et absentes) : arrêt avant tout calcul ; nœud")

    def _cle_du_stockage(self, nom: str) -> str | None:
        debut = (self.prefixe or "") + "data/"
        return nom[len(debut):] if nom.startswith(debut) else None

    def _taille_par_data_pkl(self, nom: str) -> int | None:
        cle = self._cle_du_stockage(nom)
        return self.tailles.get(cle) if cle is not None else None

    def _est_petit(self, nom: str, taille: int | None) -> bool:
        if not self.enregistrements:                           # `data.pkl`
            return True
        cle = self._cle_du_stockage(nom)
        return cle is not None and cle in self.petits_voulus and taille is not None

    @property
    def petits_voulus(self) -> set:
        return getattr(self, "_petits_voulus", set())

    def _deposer(self, c: dict, octets) -> None:
        debut, fin = c["recu"], c["recu"] + len(octets)
        c["recu"] = fin
        if c["garde"] is not None:
            if len(c["garde"]) + len(octets) > PETIT_MAX:
                raise self._illisible(f"{c['nom']} de plus de {PETIT_MAX} octets")
            c["garde"] += octets
        cle = self._cle_du_stockage(c["nom"]) if self.enregistrements else None
        for a, b, ou in self.plages.get(cle, ()):
            if a < fin and b > debut:
                self.fichiers[ou].write(octets[max(a, debut) - debut:min(b, fin) - debut])

    def _chercher_descripteur(self) -> bool:
        """Enregistrement dont l'en-tête ne dit pas la taille et que `data.pkl` ne décrit pas : son descripteur est cherché
        dans le flux, et tenu pour le sien quand sa taille égale la distance parcourue et que sa somme de contrôle est celle
        des octets parcourus."""
        t, c = self.tampon, self._courant
        debut = 0
        while True:
            i = t.find(SIGNATURE_DESCRIPTEUR, debut)
            if i < 0:
                if len(t) > PETIT_MAX:
                    raise self._illisible(f"taille de {c['nom']} introuvable")
                return False
            if len(t) < i + 24:
                return False
            crc, a32, b32 = struct.unpack("<III", bytes(t[i + 4:i + 16]))
            a64, b64 = struct.unpack("<QQ", bytes(t[i + 8:i + 24]))
            if (a32 == b32 == i or a64 == b64 == i) and zlib.crc32(bytes(t[:i])) == crc:
                longueur = 16 if a32 == b32 == i and not (a64 == b64 == i and i != 0) else 24
                if a32 == b32 == i and a64 == b64 == i:        # taille nulle : la forme se lit à la signature qui suit
                    longueur = 16 if bytes(t[i + 16:i + 20]) == SIGNATURE_LOCALE or bytes(t[i + 16:i + 20]) in SIGNATURES_DE_FIN else 24
                c["taille"], c["recu"] = i, i
                if c["garde"] is not None:
                    c["garde"] += t[:i]
                del t[:i + longueur]
                self.etat = "clos"
                return True
            debut = i + 1

    def _clore(self) -> None:
        c = self._courant
        premier = not self.enregistrements
        self.enregistrements.append({"nom": c["nom"], "octets": int(c["taille"])})
        if premier:
            self._analyser(bytes(c["garde"]))
        elif c["garde"] is not None:
            self.petits[self._cle_du_stockage(c["nom"])] = bytes(c["garde"])
        self._courant = None

    # -- `data.pkl` -------------------------------------------------------------------------------------------------------------------
    def _analyser(self, octets: bytes) -> None:
        a = self.attendu
        objet = depickler(octets)
        try:
            etat = objet["state"]
            sommes = etat["sums"]
            self.meta, self.n_docs, self.next_doc = objet["meta"], etat["n_docs"], etat["next_doc"]
            tenseurs = {cle: sommes[cle] for cle in sommes}
        except (KeyError, TypeError):
            raise FormeMalComprise("archive d'ajustement : `meta`, `state.n_docs`, `state.next_doc` ou `state.sums` absents : "
                                   "arrêt ; nœud") from None
        self._petits_voulus = set()
        for cle, t in tenseurs.items():
            if not isinstance(t, TenseurFactice):
                raise FormeMalComprise(f"archive d'ajustement : `sums[{cle!r}]` n'est pas un tenseur : arrêt ; nœud")
            if self.tailles.setdefault(t.stockage.cle, t.stockage.octets) != t.stockage.octets:
                raise FormeMalComprise("archive d'ajustement : un stockage de deux tailles : arrêt ; nœud")
            self.tenseurs[cle] = {"cle_du_stockage": t.stockage.cle, "type": t.stockage.type, "forme": list(t.forme),
                                  "pas": list(t.pas), "decalage": t.decalage}
        for nom, objet_etat in (("n_docs", self.n_docs), ("next_doc", self.next_doc)):
            if isinstance(objet_etat, TenseurFactice):
                self.tailles.setdefault(objet_etat.stockage.cle, objet_etat.stockage.octets)
                if objet_etat.stockage.octets > 4096:
                    raise FormeMalComprise(f"archive d'ajustement : `state.{nom}` d'une autre forme : arrêt ; nœud")
                self._petits_voulus.add(objet_etat.stockage.cle)
        m = a.largeur * a.largeur * 4
        for moitie in (0, 1):
            cle = (K2.CIBLE_LUE, moitie)
            if cle not in tenseurs:
                raise FormeMalComprise(f"archive d'ajustement : `sums[{cle!r}]` absent : arrêt ; nœud")
            t = tenseurs[cle]
            if t.stockage.type != "FloatStorage":
                raise Arret(f"archive d'ajustement : `sums[{cle!r}]` n'est pas en simple précision : arrêt ; nœud")
            if tuple(t.forme) != (a.n_couches, a.largeur, a.largeur):
                raise Arret(f"archive d'ajustement : forme de `sums[{cle!r}]` différente de la table de « Entrées » "
                            f"({list(t.forme)} au lieu de {[a.n_couches, a.largeur, a.largeur]}) : arrêt ; nœud")
            if not t.contigu:
                raise Arret(f"archive d'ajustement : tenseur `sums[{cle!r}]` non contigu : arrêt avant tout calcul ; nœud (la "
                            "forme est mal comprise)")
            if t.decalage != 0 or t.stockage.elements != t.elements:
                raise Arret(f"archive d'ajustement : décalage non nul inattendu de `sums[{cle!r}]` (ou stockage partagé) : arrêt "
                            "avant tout calcul ; nœud (la forme est mal comprise)")
            if t.stockage.cle in self.plages:
                raise Arret("archive d'ajustement : les deux moitiés partagent un stockage : arrêt avant tout calcul ; nœud")
            self.plages[t.stockage.cle] = []
            for couche in a.couches:
                if not 0 <= couche < a.n_couches:
                    raise Arret(f"archive d'ajustement : couche {couche} hors de `sums[{cle!r}]` : arrêt ; nœud")
                ou = (moitie, couche)
                self.fichiers[ou] = open(self.dossier / (self.nom_fichier(moitie, couche) + ".partiel"), "xb")
                self.plages[t.stockage.cle].append((couche * m, (couche + 1) * m, ou))

    # -- conclusion -------------------------------------------------------------------------------------------------------------------
    def abandonner(self) -> None:
        for f in self.fichiers.values():
            f.close()
        for moitie, couche in self.fichiers:
            (self.dossier / (self.nom_fichier(moitie, couche) + ".partiel")).unlink(missing_ok=True)

    def conclure(self, taille_attendue: int, sha256_attendu: str, sha256_du_18_novembre: str | None = None) -> dict:
        """SHA-256 et taille calculés **sur le flux entier par ce code**, comparés à la fiche (et, au premier palier, à
        l'empreinte du 18 novembre) ; différents : arrêt, et aucune matrice extraite de ce flux n'est gardée."""
        for f in self.fichiers.values():
            f.close()
        a = self.attendu
        m = a.largeur * a.largeur * 4
        partiels = {ou: self.dossier / (self.nom_fichier(*ou) + ".partiel") for ou in self.fichiers}
        sha = self.hachage.hexdigest()
        if self.position != int(taille_attendue) or sha != sha256_attendu:
            self.abandonner()
            raise Arret(f"notre lentille {a.lettre} : SHA-256 ou taille calculés sur le flux différents de la fiche : arrêt ; "
                        "message à la session principale ; la lentille n'est pas lue sans version neuve")
        if sha256_du_18_novembre is not None and sha != sha256_du_18_novembre:
            self.abandonner()
            raise Arret(f"notre lentille {a.lettre} au premier palier : SHA-256 calculé sur le flux différent de l'empreinte du "
                        "18 novembre : arrêt ; message à la session principale")
        if self.etat != "fin" or len(partiels) != 2 * len(a.couches) or any(p.stat().st_size != m for p in partiels.values()):
            self.abandonner()
            raise self._illisible("archive tronquée, ou matrices extraites incomplètes")
        fichiers = {}
        for ou, p in partiels.items():
            p.rename(self.dossier / self.nom_fichier(*ou))
            fichiers[f"{ou[0]}/{ou[1]}"] = self.nom_fichier(*ou)
        return {"lentille": a.lettre, "sha256": sha, "taille": self.position, "meta": self.meta,
                "n_docs": self._entiers(self.n_docs, "n_docs"), "next_doc": self._entiers(self.next_doc, "next_doc"),
                "sums": {repr(k): v for k, v in self.tenseurs.items()}, "fichiers": fichiers,
                "enregistrements": self.enregistrements, "largeur": a.largeur, "couches": list(a.couches)}

    def _entiers(self, objet, nom: str):
        if isinstance(objet, TenseurFactice):
            brut = self.petits.get(objet.stockage.cle)
            if brut is None:
                raise FormeMalComprise(f"archive d'ajustement : `state.{nom}` illisible : arrêt ; nœud")
            valeurs = np.frombuffer(brut, dtype=_STOCKAGES[objet.stockage.type][0])[objet.decalage:objet.decalage + objet.elements]
            return [int(x) for x in valeurs] if objet.forme else int(valeurs[0])
        if isinstance(objet, (list, tuple)):
            return [int(x) for x in objet]
        if isinstance(objet, int) and not isinstance(objet, bool):
            return int(objet)
        raise FormeMalComprise(f"archive d'ajustement : `state.{nom}` d'une autre forme : arrêt ; nœud")


def lire_ajustement_en_flux(transport, url: str, cle, attendu: Attendu, dossier: Path, taille: int, sha256: str,
                            sha256_du_18_novembre: str | None = None, reprises: int = 5) -> dict:
    """Lit un fichier d'ajustement en flux, à l'adresse de la révision de la fiche (reprise à l'octet atteint si le flux se
    rompt, au plus `reprises` fois). **Jamais** un autre fichier, une autre révision, un fichier exporté ou une lentille d'un
    tiers à la place : un refus du transport remonte tel quel."""
    from .montage_v1 import RefusReseau
    ex = ExtracteurAjustement(attendu, dossier)
    essais = 0
    while True:
        try:
            for bloc in transport.flux(url, cle, ex.position):
                ex.recevoir(bloc)
            break
        except RefusReseau:
            essais += 1
            if essais > reprises or ex.position >= int(taille):
                ex.abandonner()
                raise
        except Arret:
            ex.abandonner()
            raise
    return ex.conclure(taille, sha256, sha256_du_18_novembre)


# ========================================================================================================================================
# 5. Contrôles de `meta`, de l'état et des matrices ; matrices lues
# ========================================================================================================================================
def controler_meta_et_etat(description: dict, attendu: Attendu) -> dict:
    """`meta`, `n_docs`, `next_doc` comparés à la table de « Entrées » (pour notre S : à la `meta` de la pièce du 18
    novembre) ; un écart : arrêt ; nœud. Une `meta` de S chargée comme R, ou l'inverse, ne passe pas (champ `lens`)."""
    meta = description["meta"]
    if not isinstance(meta, dict) or attendu.meta is None:
        raise FormeMalComprise(f"notre lentille {attendu.lettre} : `meta` absente ou d'une autre forme : arrêt ; nœud")
    ecarts = [c for c in K2.CHAMPS_META if _valeur(meta.get(c)) != _valeur(attendu.meta.get(c))]
    if meta.get("lens") != attendu.lettre or attendu.meta.get("lens") != attendu.lettre:
        ecarts = sorted(set(ecarts) | {"lens"})
    if ecarts:
        raise Arret(f"notre lentille {attendu.lettre} : `meta` différente de celle attendue (champs {', '.join(ecarts)}) : "
                    "arrêt ; nœud")
    if list(description["n_docs"]) != list(attendu.n_docs) or description["next_doc"] != attendu.next_doc:
        raise Arret(f"notre lentille {attendu.lettre} : `n_docs` ou `next_doc` différents de la table de « Entrées » : arrêt ; "
                    "nœud")
    return {"meta": {c: meta.get(c) for c in K2.CHAMPS_META}, "n_docs": list(description["n_docs"]),
            "next_doc": description["next_doc"]}


def _valeur(x):
    return list(x) if isinstance(x, (list, tuple)) else x


def empreinte_simple_precision(matrice: np.ndarray) -> str:
    """SHA-256 des octets d'une matrice en simple précision, petit-boutistes, dans l'ordre des lignes."""
    a = np.asarray(matrice)
    if a.dtype != np.float32:
        raise Arret(f"empreinte d'une matrice de nos lentilles : simple précision attendue, {a.dtype} reçue")
    return hashlib.sha256(np.ascontiguousarray(a.astype("<f4", copy=False)).tobytes()).hexdigest()


@dataclass
class NotreLentille:
    """Les matrices décodées d'une de nos lentilles : pour chaque couche gardée, les deux sommes S₀[ℓ] et S₁[ℓ] (simple
    précision, telles que décodées) et les nombres de documents. Matrice lue : (S₀[ℓ] + S₁[ℓ]) / (n₀ + n₁)
    (`Accumulator.mean("out")`) ; moitiés : S₀[ℓ] / n₀ et S₁[ℓ] / n₁. Pour notre S, la matrice est orientée [sortie du bloc ℓ,
    plongement] : elle se lit covecteur à gauche (`c @ K`)."""
    lettre: str
    sommes: dict                      # couche → (S₀[ℓ], S₁[ℓ])
    n_docs: tuple
    empreintes_montage: dict = field(default_factory=dict)   # « couche/quoi » → empreinte relevée au montage
    decalage: int = 0                 # n'existe que pour l'essai de la garde de l'indice (artefact : un cran)

    def _indice(self, couche: int) -> int:
        couches = sorted(self.sommes)
        if int(couche) not in self.sommes:
            raise Arret(f"notre lentille {self.lettre} : aucune matrice décodée d'indice {couche}")
        return int(couche) if not self.decalage else couches[(couches.index(int(couche)) + self.decalage) % len(couches)]

    def matrice(self, couche: int, moitie: int | None = None) -> np.ndarray:
        """Matrice de la couche, ou d'une de ses moitiés (0 : documents pairs ; 1 : documents impairs), en simple précision."""
        s0, s1 = self.sommes[self._indice(couche)]
        n0, n1 = (np.float32(n) for n in self.n_docs)
        if moitie is None:
            return ((s0 + s1) / (n0 + n1)).astype(np.float32, copy=False)
        return ((s0, s1)[moitie] / (n0, n1)[moitie]).astype(np.float32, copy=False)

    def matrice_verifiee(self, couche: int, moitie: int | None = None) -> tuple[np.ndarray, int, str]:
        """Contrôle de l'indice de couche étendu à nos lentilles : l'empreinte de la matrice lue égale celle relevée au
        montage pour l'indice égal à la couche de la sonde ; écart : arrêt."""
        m = self.matrice(couche, moitie)
        lue = empreinte_simple_precision(m)
        cle = f"{int(couche)}/{'entiere' if moitie is None else f'moitie{moitie}'}"
        if cle not in self.empreintes_montage:
            raise Arret(f"notre lentille {self.lettre} : aucune empreinte relevée au montage pour l'indice {couche}")
        if lue != self.empreintes_montage[cle]:
            raise Arret(f"notre lentille {self.lettre} : matrice lue d'un autre indice que la couche {couche} de la sonde : arrêt")
        return m, int(couche), lue

    def relever_empreintes(self) -> dict:
        self.empreintes_montage = {}
        for couche in sorted(self.sommes):
            for moitie in (None, 0, 1):
                cle = f"{couche}/{'entiere' if moitie is None else f'moitie{moitie}'}"
                self.empreintes_montage[cle] = empreinte_simple_precision(self.matrice(couche, moitie))
        return dict(self.empreintes_montage)


def charger_notre_lentille(dossier: Path, description: dict) -> NotreLentille:
    """Charge les matrices extraites (six fichiers par lentille : trois couches, deux moitiés), en simple précision."""
    d = int(description["largeur"])
    sommes = {}
    for couche in description["couches"]:
        moities = []
        for moitie in (0, 1):
            chemin = Path(dossier) / description["fichiers"][f"{moitie}/{couche}"]
            moities.append(np.array(np.memmap(chemin, dtype="<f4", mode="r", shape=(d, d))))
        sommes[int(couche)] = tuple(moities)
    return NotreLentille(description["lentille"], sommes, tuple(description["n_docs"]))


def _ecart_relatif(a: np.ndarray, b: np.ndarray) -> float:
    """Écart relatif de Frobenius de `a` à la référence `b` : ‖a − b‖ / ‖b‖, en double précision."""
    na = float(np.linalg.norm((a.astype(np.float64) - b.astype(np.float64)).ravel()))
    nb = float(np.linalg.norm(b.astype(np.float64).ravel()))
    if nb == 0.0:
        raise Arret("écart relatif à une matrice de norme nulle : arrêt")
    return na / nb


def controler_matrices(lentille: NotreLentille, publique: dict | None = None, notre_r: NotreLentille | None = None) -> dict:
    """Plan, point 4 ; « Liste d'arrêt » : les six matrices décodées sont finies ; les deux moitiés d'une même couche sont
    distinctes (écart maximal > 10⁻⁶) ; chaque matrice de notre R est distincte de l'identité et de la matrice de même couche
    de la lentille publique (écart relatif de Frobenius > 10⁻³) ; chaque matrice de notre S de la matrice de notre R de même
    couche et de sa transposée. Écarts relatifs à l'identité et entre moitiés rapportés par couche, sans critère. `publique` :
    couche → matrice de la lentille publique (simple précision). Arrêt avant tout calcul ; nœud."""
    rapport = {"lentille": lentille.lettre, "couches": {}, "empreintes_des_matrices_decodees": {}}
    for couche in sorted(lentille.sommes):
        s0, s1 = lentille.sommes[couche]
        if not (np.isfinite(s0).all() and np.isfinite(s1).all()):
            raise Arret(f"notre lentille {lentille.lettre} : une matrice non finie à la couche {couche} : arrêt avant tout calcul ; "
                        "nœud")
        for moitie, s in ((0, s0), (1, s1)):
            rapport["empreintes_des_matrices_decodees"][f"{couche}/moitie{moitie}"] = empreinte_simple_precision(s)
        m, m0, m1 = lentille.matrice(couche), lentille.matrice(couche, 0), lentille.matrice(couche, 1)
        if float(np.abs(m0 - m1).max()) <= K.ECART_MATRICES:
            raise Arret(f"notre lentille {lentille.lettre} : deux moitiés égales à la couche {couche} : arrêt avant tout calcul ; "
                        "nœud")
        identite = np.eye(m.shape[0], dtype=np.float32)
        case = {"ecart_relatif_a_l_identite": _ecart_relatif(m, identite), "ecart_relatif_entre_moities": _ecart_relatif(m0, m1)}
        if lentille.lettre == "R":
            if case["ecart_relatif_a_l_identite"] <= K2.ECART_RELATIF_MATRICES:
                raise Arret(f"notre R égale à l'identité à la couche {couche} (écart relatif ≤ 10⁻³) : arrêt avant tout calcul ; "
                            "nœud")
            if publique is None or couche not in publique:
                raise Arret(f"notre R : matrice de la lentille publique absente à la couche {couche} pour le contrôle : arrêt")
            case["ecart_relatif_a_la_lentille_publique"] = _ecart_relatif(m, np.asarray(publique[couche], dtype=np.float32))
            if case["ecart_relatif_a_la_lentille_publique"] <= K2.ECART_RELATIF_MATRICES:
                raise Arret(f"notre R égale à la lentille publique à la couche {couche} (écart relatif ≤ 10⁻³) : arrêt avant tout "
                            "calcul ; nœud")
        elif notre_r is None:
            case["controle_contre_notre_r"] = "sans objet : notre R n'est pas décodée"
        else:
            r = notre_r.matrice(couche)
            case["ecart_relatif_a_notre_r"] = _ecart_relatif(m, r)
            case["ecart_relatif_a_la_transposee_de_notre_r"] = _ecart_relatif(m, r.T)
            if min(case["ecart_relatif_a_notre_r"], case["ecart_relatif_a_la_transposee_de_notre_r"]) <= K2.ECART_RELATIF_MATRICES:
                raise Arret(f"notre S égale à notre R de même couche ou à sa transposée (couche {couche}, écart relatif ≤ 10⁻³) : "
                            "arrêt avant tout calcul ; nœud")
        rapport["couches"][str(couche)] = case
    rapport["empreintes_des_matrices_lues"] = lentille.relever_empreintes()
    return rapport


def cible_un_octet(lettre: str, l: dict):
    """Cible de l'essai d'un octet d'un de nos fichiers : avec la clé, à la révision de la fiche. Un refus arrête avant tout
    flux long, et aucun autre fichier n'est tenté (`montage_v1.essais_un_octet`)."""
    from .montage_v1 import Cible, url_fichier
    return Cible(f"notre lentille {lettre} (dépôt de rangement, révision de la fiche)",
                 url_fichier(l["depot"], l["revision"], l["chemin"]), avec_cle=True)
