#!/usr/bin/env python3
"""Garde G5 de la boucle extérieure du pilote 4 : périmètre, facteurs, zones — v1.

Protocole de la boucle extérieure v4, § 6 (point 3) et § 11 (G5, artefacts (a) à (i)) ; décisions E8 (carte lue au
niveau des colonnes, par segments ; ligne VERSION dans la liste d'accompagnement) et D7 (préfixes des en-têtes) ; règles
1 à 9 du § 0 de la carte des facteurs, la règle 9 (lignes insérées) telle qu'elle est écrite (décision de conv-audit).

Lit : la carte des facteurs et les zones interdites (JSON, toute version de même forme), la pièce de périmètre (dont
l'empreinte a été consignée avant le diff), le diff `LC_ALL=C diff -ruN objet-origine copie-organisme`, et les deux
dossiers. N'exécute rien de l'objet. Bibliothèque standard seule ; `python3 -I`.

Codes de sortie : 0 accepté ; 2 usage ; 3 refusé (motif sur la sortie d'erreur : lettre de l'artefact, fichier, ligne,
facteur ou zone ; jamais le contenu du diff) ; 4 erreur interne (type et ligne seulement).
"""

import argparse
import ast
import hashlib
import json
import keyword
import os
import pathlib
import re
import stat
import sys
import traceback
import unicodedata

GARDE = "G5"
PREFIXE_ANCIEN = "objet-origine/"
PREFIXE_NOUVEAU = "copie-organisme/"
RE_HEX64 = re.compile(r"[0-9a-f]{64}")
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
RE_COMPOSANT = re.compile(r"[A-Za-z0-9_][A-Za-z0-9._-]*")
RE_BLOC = re.compile(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?: .*)?")
RE_VERSION = re.compile(r'VERSION\s*=\s*"[^"\\]*"\s*')
RE_CORRECTIONS_NOUVEAU = re.compile(r"CORRECTIONS-v(\d+)\.md")
RE_ESSAI_NOUVEAU = re.compile(r"tests/test_corrections_v(\d+)\.py")
RE_ID_FACTEUR = re.compile(r"(?<![A-Za-z0-9])F\d{2}(?![0-9])")
RE_ID_SOUS = re.compile(r"(?<![A-Za-z0-9])F\d{2}-[a-z](?![A-Za-z0-9])")
RE_NOM_FICHIER = re.compile(r"(?<![A-Za-z0-9_./-])((?:organisme/)?[A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:py|md|json))(?![A-Za-z0-9_])")
RE_MARQUE_LIGNES = re.compile(r"(?:^|(?<=[\s,;]))(?:l\.|lignes?|plages?)(?=[\s\d])")
RE_ITEM = re.compile(r"\s*(?:(?:,|;|\bet\b)\s*)?(\d+)(?:\s*-\s*(\d+))?(?![\w]|\.\d)")

# Contenu interdit du § 14 détectable par motifs, cherché dans les lignes ajoutées (texte sans accents, en minuscules,
# sauf les motifs « bruts », cherchés sur le texte tel quel). Aucun motif ne recopie un contenu de l'objet.
MOTIFS_INTERDITS = [
    ("nom de fiche (HC-P4-)", False, r"hc-p4"),
    ("identifiant de tâche de la forme t-0001", False, r"(?<![a-z0-9_])t-\d{4}(?![0-9])"),
    ("nom de test_final", False, r"test[\s_-]*final"),
    ("libellé du point 4 bis ou d'une cellule (ii)",
     False, r"au-dela du bruit des taches|dans le bruit des taches|non distinct de la reference"
            r"|au-dessus de la reference|impossible par construction"),
    ("valeur p", False, r"(?<![a-z0-9_])valeurs?[\s_]p(?![a-z0-9_])|(?<![a-z0-9_])p[\s_-]?value"),
    ("mention du secret, d'une clé ou de l'archive",
     False, r"(?<![a-z0-9_])secrets?(?![a-z0-9_])|ferme\.tar|archive fermee|banque-confrontation|-cle\.json"
            r"|-secret\.json|api[\s_-]?key|(?<![a-z0-9_])cles? (?:d'?api|secretes?)(?![a-z0-9_])"),
    ("réponses par tâche", False, r"reponses? par taches?"),
    ("question M ou S", True, r"(?<![\w-])[Qq]uestions?\s+[MS](?![\w-])"),
    ("nom ou fait de course", True, r"(?<![\w-])[Cc]ourses?\s+[MS](?![\w-])"),
    ("nom ou fait de course", False, r"pilote\s?4|tentative\d|gemini-v6-2|gemini-organisme-v6"),
    ("verdict ou registre", False, r"(?<![a-z0-9_])verdicts?(?![a-z0-9_])|(?<![a-z0-9_])registres?(?![a-z0-9_])"),
    ("champ du relevé (B)",
     False, r"(?<![a-z0-9_])(?:identite|releve)\.[a-z]|(?<![a-z0-9_])unite\.[cg]\d{3}"
            r"|conception\.(?:declaration|rondes_tournees)|(?<![a-z0-9_])evenements\.(?:delai_depasse|plafond_refus|stop)"
            r"|(?<![a-z0-9_])fin\.(?:reprise_attendue|liste_fermee_poussee|recherche_cles_faite|dernier_code|lignee)"
            r"|(?<![a-z0-9_])(?:mutation|memoire|castes)\.[cg]\d{3}|sources\.liste_fermee"),
]
MOTIFS_INTERDITS = [(cat, brut, re.compile(rx)) for cat, brut, rx in MOTIFS_INTERDITS]
MOT = r"[^\W\d_][^\W\d_'’-]*"
RE_MOT = re.compile(MOT)
RE_LITTERAL = re.compile(r"""(?:"([^"\\\n]*)"|'([^'\\\n]*)')""")
RE_GROUPE = re.compile(r"[\[\(\{]([^\[\]\(\)\{\}]*)[\]\)\}]")
RE_ALTERNANCE = re.compile(rf"{MOT}(?:\|{MOT}){{3,}}")
# Champs de premier niveau lus par cette version. Un autre champ fait refuser la carte : une forme nouvelle demande une
# version nouvelle de G5 (aucun champ ignoré en silence). « noms_geles » : liste close des noms gelés annoncée pour la
# carte v2 (message de conv-audit), lue dans l'un ou l'autre fichier ; absente de la v1.
CHAMPS_CARTE = {"piece", "ecrit_le", "auteur", "brief", "objet", "conventions", "facteurs", "lignes_partagees",
                "segments_interdits_sur_lignes_de_facteur", "points_hors_boucle", "noms_geles"}
CHAMPS_ZONES = {"piece", "ecrit_le", "auteur", "brief", "objet", "conventions", "statuts", "zones", "segments",
                "noms_geles"}


class Refus(Exception):
    """Refus de la garde : code 3."""


class Usage(Exception):
    """Erreur d'usage : code 2."""


class Analyseur(argparse.ArgumentParser):
    def error(self, message):
        raise Usage(message)


def sans_accents(texte):
    t = unicodedata.normalize("NFD", texte)
    return unicodedata.normalize("NFC", "".join(c for c in t if unicodedata.category(c) != "Mn"))


def norm(texte):
    t = sans_accents(texte).casefold()
    for a, b in (("’", "'"), ("–", "-"), ("—", "-"), ("−", "-"), ("\u00a0", " "), ("\u202f", " ")):
        t = t.replace(a, b)
    return t


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def fichier_ordinaire(chemin, quoi):
    try:
        mode = os.lstat(chemin).st_mode
    except FileNotFoundError:
        raise Refus(f"{quoi} absent : {chemin.name}")
    if stat.S_ISLNK(mode):
        raise Refus(f"{quoi} est un lien symbolique : {chemin.name}")
    if not stat.S_ISREG(mode):
        raise Refus(f"{quoi} n'est pas un fichier ordinaire : {chemin.name}")


def verifier_compagnon(chemin, quoi):
    """Vérifie le compagnon « empreinte, deux espaces, nom nu » et rend l'empreinte du fichier."""
    fichier_ordinaire(chemin, quoi)
    compagnon = chemin.with_name(chemin.name + ".sha256")
    fichier_ordinaire(compagnon, f"compagnon de {quoi}")
    try:
        texte = compagnon.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"compagnon de {quoi} illisible")
    m = RE_COMPAGNON.fullmatch(texte)
    if not m:
        raise Refus(f"compagnon de {quoi} mal formé (attendu : « empreinte, deux espaces, nom nu »)")
    if m.group(2) != chemin.name:
        raise Refus(f"compagnon de {quoi} : il nomme un autre fichier")
    empreinte = sha256_fichier(chemin)
    if empreinte != m.group(1):
        raise Refus(f"compagnon de {quoi} : empreinte différente de celle du fichier")
    return empreinte


def lister_fichiers(racine, quoi):
    """Fichiers ordinaires sous racine, par chemin relatif ; refuse liens symboliques, fichiers spéciaux, noms hors norme."""
    racine = pathlib.Path(racine)
    try:
        mode = os.lstat(racine).st_mode
    except FileNotFoundError:
        raise Refus(f"{quoi} absent")
    if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
        raise Refus(f"{quoi} n'est pas un dossier ordinaire")
    fichiers = {}
    for dossier, sous, noms in os.walk(racine, followlinks=False):
        for nom in sorted(sous) + sorted(noms):
            p = pathlib.Path(dossier) / nom
            rel = p.relative_to(racine).as_posix()
            mode = os.lstat(p).st_mode
            if stat.S_ISLNK(mode):
                raise Refus(f"{quoi} : lien symbolique {rel}")
            if not RE_COMPOSANT.fullmatch(nom):
                raise Refus(f"{quoi} : nom hors norme {rel!r}")
            if nom in noms and not stat.S_ISREG(mode):
                raise Refus(f"{quoi} : fichier spécial {rel}")
            if nom in noms:
                fichiers[rel] = p
    return fichiers


def decouper(texte):
    """Lignes d'un texte, et présence de la fin de ligne finale."""
    if texte == "":
        return [], True
    parties = texte.split("\n")
    if parties[-1] == "":
        return parties[:-1], True
    return parties, False


def lire_texte(chemin, quoi):
    try:
        return chemin.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"{quoi} n'est pas un texte UTF-8")


# ---------------------------------------------------------------------------------------------------------------------
# Carte et zones


class Carte:
    """La carte des facteurs et les zones interdites, rapportées aux lignes de l'objet au commit."""

    def __init__(self, carte, zones, objet):
        self.entier = {}
        self.segments = {}
        self.zone_ligne = {}
        self.zone_seg = {}
        self.phb = {}
        self.domaine = set()
        self.sous_lignes = {}
        self.facteurs = {}
        self.id_defaut = None
        self.id_elements = None
        self.id_instances = None
        self.lignes = {}
        self.ligne_version = None
        self.noms_geles = set()
        if not isinstance(carte, dict) or not isinstance(zones, dict):
            raise Refus("carte ou zones : forme inattendue")
        for donnees, connus, quoi in ((carte, CHAMPS_CARTE, "carte"), (zones, CHAMPS_ZONES, "zones")):
            inconnus = sorted(set(donnees) - connus)
            if inconnus:
                raise Refus(f"{quoi} : champ inconnu de cette version de G5 ({', '.join(inconnus)}) : une forme "
                            f"nouvelle demande une version nouvelle de la garde")
        try:
            self._charger(carte, zones, objet)
        except (KeyError, TypeError, ValueError, AttributeError):
            raise Refus("carte ou zones : forme inattendue (champ absent ou de mauvais type)")

    def _incoherente(self, motif):
        raise Refus(f"carte incohérente : {motif}")

    def _lire_noms_geles(self, valeur, quoi):
        if not isinstance(valeur, list) or not valeur:
            self._incoherente(f"{quoi}, noms_geles : liste non vide attendue")
        for e in valeur:
            if isinstance(e, str):
                nom, fichier = e, None
            elif isinstance(e, dict) and isinstance(e.get("nom"), str):
                nom, fichier = e["nom"], e.get("fichier")
            else:
                self._incoherente(f"{quoi}, noms_geles : entrée sans nom")
            if not nom.isidentifier() or keyword.iskeyword(nom):
                self._incoherente(f"{quoi}, noms_geles : {nom!r} n'est pas un identifiant")
            if fichier is not None and fichier not in self.lignes:
                self._incoherente(f"{quoi}, noms_geles : fichier {fichier!r} absent de l'objet")
            motif = re.compile(rf"(?<![\w]){re.escape(nom)}(?![\w])")
            if not any(motif.search("\n".join(lignes)) for rel, (lignes, _) in self.lignes.items()
                       if rel.endswith(".py")):
                self._incoherente(f"{quoi}, noms_geles : {nom!r} absent du code de l'objet")
            self.noms_geles.add(nom)

    def _charger(self, carte, zones, objet):
        attendus = carte["objet"]["sha256_fichiers"]
        if zones["objet"]["sha256_fichiers"] != attendus:
            self._incoherente("la carte et les zones ne décrivent pas le même objet")
        fichiers = lister_fichiers(objet, "objet d'origine")
        if set(fichiers) != set(attendus):
            raise Refus("objet d'origine : ses fichiers ne sont pas ceux de la carte")
        for rel, p in fichiers.items():
            if sha256_fichier(p) != attendus[rel]:
                raise Refus(f"objet d'origine : {rel} diffère de la carte (empreinte)")
            self.lignes[rel] = decouper(lire_texte(p, f"objet d'origine, {rel}"))
        for rel, (lignes, _) in self.lignes.items():
            for n, texte in enumerate(lignes, 1):
                if rel == "principal.py" and RE_VERSION.fullmatch(texte):
                    if self.ligne_version is not None:
                        raise Refus("objet d'origine : deux lignes VERSION dans principal.py")
                    self.ligne_version = (rel, n)
        entrees = {}
        for fa in carte["facteurs"]:
            fid = fa["id"]
            if fid in self.facteurs or not re.fullmatch(r"F\d{2}", fid):
                self._incoherente(f"identifiant de facteur {fid!r}")
            self.facteurs[fid] = fa
            for e in fa["entrees"]:
                entrees[e["id"]] = (fid, e)
                f, d, fin = e["fichier"], int(e["ligne_debut"]), int(e["ligne_fin"])
                self._verifier_plage(f, d, fin, e["id"])
                if "colonne_debut" in e:
                    if d != fin:
                        self._incoherente(f"segment {e['id']} sur plusieurs lignes")
                    seg = self._segment(e["id"], fid, f, d, e)
                    self.segments.setdefault((f, d), []).append(seg)
                else:
                    for n in range(d, fin + 1):
                        if (f, n) in self.entier:
                            self._incoherente(f"{f} l. {n} dans deux facteurs ({self.entier[(f, n)]} et {fid})")
                        self.entier[(f, n)] = fid
            if "domaine" in fa:
                if self.id_defaut is not None:
                    self._incoherente("deux facteurs portent un domaine")
                self.id_defaut = fid
                for dom in fa["domaine"]:
                    for d, fin in dom["plages"]:
                        self._verifier_plage(dom["fichier"], int(d), int(fin), f"domaine de {fid}")
                        for n in range(int(d), int(fin) + 1):
                            self.domaine.add((dom["fichier"], n))
            if "elements" in fa:
                if self.id_elements is not None:
                    self._incoherente("deux facteurs portent des éléments")
                self.id_elements = fid
                for el in fa["elements"]:
                    self.sous_lignes[el["id"]] = {(el["fichier"], int(n)) for n in el["lignes"]}
            if "instances" in fa:
                if self.id_instances is not None:
                    self._incoherente("deux facteurs portent des instances")
                self.id_instances = fid
        for fid in (self.id_instances,):
            if fid is None:
                continue
            for inst in self.facteurs[fid]["instances"]:
                lignes = set()
                for eid in inst["entrees"]:
                    if eid not in entrees or entrees[eid][0] != fid:
                        self._incoherente(f"instance {inst['id']} : entrée {eid} inconnue")
                    e = entrees[eid][1]
                    lignes |= {(e["fichier"], n) for n in range(int(e["ligne_debut"]), int(e["ligne_fin"]) + 1)}
                self.sous_lignes[inst["id"]] = lignes
        if self.id_elements is not None:
            for sid, lignes in self.sous_lignes.items():
                if sid.startswith(self.id_elements + "-"):
                    for cle in lignes:
                        if self.entier.get(cle) != self.id_elements:
                            self._incoherente(f"élément {sid} : {cle[0]} l. {cle[1]} hors des lignes de son facteur")
        for lp in carte["lignes_partagees"]:
            cle = (lp["fichier"], int(lp["ligne"]))
            facteurs_seg = set()
            for eid in lp["segments"]:
                if eid not in entrees or "colonne_debut" not in entrees[eid][1]:
                    self._incoherente(f"ligne partagée {cle[0]} l. {cle[1]} : segment {eid} inconnu")
                facteurs_seg.add(entrees[eid][0])
            if len(facteurs_seg) < 2:
                self._incoherente(f"ligne partagée {cle[0]} l. {cle[1]} : moins de deux facteurs")
            if {s["facteur"] for s in self.segments.get(cle, [])} != facteurs_seg:
                self._incoherente(f"ligne partagée {cle[0]} l. {cle[1]} : segments différents des entrées")
        for cle, segs in self.segments.items():
            if cle in self.entier:
                self._incoherente(f"{cle[0]} l. {cle[1]} : segment de facteur sur une ligne entière d'un facteur")
            self._disjoints(cle, segs)
        for z in zones["zones"]:
            for e in z["entrees"]:
                f, d, fin = e["fichier"], int(e["ligne_debut"]), int(e["ligne_fin"])
                if e["statut"] not in ("Z", "R", "E"):
                    self._incoherente(f"zone {e['id']} : statut {e['statut']!r}")
                if e["statut"] == "E" and e.get("exception") not in ("format", "analyse", "délai"):
                    self._incoherente(f"zone {e['id']} : type d'exception {e.get('exception')!r}")
                self._verifier_plage(f, d, fin, e["id"])
                for n in range(d, fin + 1):
                    cle = (f, n)
                    if cle in self.zone_ligne:
                        self._incoherente(f"{f} l. {n} dans deux zones")
                    if cle in self.entier or cle in self.segments or cle in self.domaine:
                        self._incoherente(f"{f} l. {n} à la fois dans une zone et dans un facteur")
                    self.zone_ligne[cle] = {"zone": z["id"], "id": e["id"], "statut": e["statut"],
                                            "exception": {"délai": "delai"}.get(e.get("exception"), e.get("exception"))}
        segs_zones = {}
        for s in zones["segments"]:
            cle = (s["fichier"], int(s["ligne"]))
            segs_zones[s["id"]] = cle
            seg = self._segment(s["id"], None, s["fichier"], int(s["ligne"]), s)
            seg["zone"] = s["zone"]
            if self.entier.get(cle) != s["facteur_de_la_ligne"]:
                self._incoherente(f"segment interdit {s['id']} hors d'une ligne de {s['facteur_de_la_ligne']}")
            self.zone_seg.setdefault(cle, []).append(seg)
        for s in carte["segments_interdits_sur_lignes_de_facteur"]:
            cle = (s["fichier"], int(s["ligne"]))
            if segs_zones.get(s["id"]) != cle:
                self._incoherente(f"segment interdit {s['id']} : la carte et les zones diffèrent")
            ref = [x for x in self.zone_seg[cle] if x["id"] == s["id"]][0]
            if (ref["c1"], ref["c2"]) != (int(s["colonne_debut"]), int(s["colonne_fin"])):
                self._incoherente(f"segment interdit {s['id']} : colonnes différentes entre la carte et les zones")
        if len(segs_zones) != len(carte["segments_interdits_sur_lignes_de_facteur"]):
            self._incoherente("segments interdits : la carte et les zones n'en comptent pas autant")
        for p in carte["points_hors_boucle"]:
            cle = (p["fichier"], int(p["ligne"]))
            seg = self._segment(p["id"], p["facteur"], p["fichier"], int(p["ligne"]), p)
            if self.entier.get(cle) != p["facteur"]:
                self._incoherente(f"point hors boucle {p['id']} hors d'une ligne de son facteur")
            self.phb.setdefault(cle, []).append(seg)
        for cle in set(self.zone_seg) | set(self.phb):
            self._disjoints(cle, self.zone_seg.get(cle, []) + self.phb.get(cle, []))
        if self.id_defaut is not None:
            for cle in self.domaine:
                if cle in self.entier or cle in self.segments or cle in self.zone_ligne:
                    self._incoherente(f"{cle[0]} l. {cle[1]} : domaine de {self.id_defaut} et autre facteur ou zone")
        for donnees, quoi in ((carte, "carte"), (zones, "zones")):
            if "noms_geles" in donnees:
                self._lire_noms_geles(donnees["noms_geles"], quoi)

    def _verifier_plage(self, f, d, fin, quoi):
        if f not in self.lignes:
            self._incoherente(f"{quoi} : fichier {f!r} absent de l'objet")
        n_max = len(self.lignes[f][0])
        if d < 1 or fin < d or fin > n_max:
            self._incoherente(f"{quoi} : plage {d}–{fin} hors de {f} ({n_max} lignes)")

    def _segment(self, sid, fid, f, n, e):
        c1, c2 = int(e["colonne_debut"]), int(e["colonne_fin"])
        texte = self.lignes[f][0][n - 1]
        if not (1 <= c1 <= c2 <= len(texte)):
            self._incoherente(f"segment {sid} : colonnes hors de la ligne")
        if hashlib.sha256(texte[c1 - 1:c2].encode("utf-8")).hexdigest() != e["sha256_segment"]:
            self._incoherente(f"segment {sid} : empreinte du segment différente du texte de l'objet")
        return {"id": sid, "facteur": fid, "c1": c1, "c2": c2}

    def _disjoints(self, cle, segs):
        bornes = sorted((s["c1"], s["c2"], s["id"]) for s in segs)
        for (a1, a2, ia), (b1, b2, ib) in zip(bornes, bornes[1:]):
            if b1 <= a2:
                self._incoherente(f"{cle[0]} l. {cle[1]} : segments {ia} et {ib} se chevauchent")


# ---------------------------------------------------------------------------------------------------------------------
# Pièce de périmètre


class Perimetre:
    def __init__(self):
        self.facteur = None
        self.sous = None
        self.exception = set()
        self.lignes = set()
        self.essais = set()
        self.accompagne_principal = False


CLES_PERIMETRE = {
    "facteur": "facteur", "facteur declare": "facteur",
    "element": "element", "element du contrat": "element",
    "instance": "instance", "borne": "instance",
    "exception": "exception",
    "lieu": "lieu", "lieux": "lieu", "lignes": "lieu", "plages": "lieu", "plages de lignes": "lieu",
    "accompagnement": "accompagnement", "fichier d'accompagnement": "accompagnement",
    "fichiers d'accompagnement": "accompagnement",
    "essai herite adapte": "essai", "essais herites adaptes": "essai",
}


def lignes_cles(texte):
    """Lignes « clé : valeur » de la pièce de périmètre (puces, gras et code retirés)."""
    for brut in texte.split("\n"):
        ligne = unicodedata.normalize("NFC", brut).strip()
        ligne = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", ligne).replace("**", "").replace("`", "")
        if ":" not in ligne:
            continue
        cle, valeur = ligne.split(":", 1)
        cle = re.sub(r"\s+", " ", norm(cle)).strip()
        if cle in CLES_PERIMETRE:
            yield CLES_PERIMETRE[cle], valeur.strip()


def sans_parentheses(texte):
    while True:
        nouveau = re.sub(r"\([^()]*\)", " ", texte)
        if nouveau == texte:
            return texte
        texte = nouveau


def lire_plages(texte):
    """Numéros de lignes après la marque « l. » : « 988–996, 998 », « 2102 et 2104 » ; s'arrête au premier mot."""
    plages = []
    pos = 0
    while True:
        m = RE_ITEM.match(texte, pos)
        if not m:
            return plages
        d = int(m.group(1))
        plages.append((d, int(m.group(2)) if m.group(2) else d))
        pos = m.end()


def fichiers_et_plages(valeur):
    """Pour une valeur « fichier, fonction, l. plages ; fichier… » : la liste (fichier, plages) ; le texte entre
    parenthèses (colonnes, entrées de la carte, remarques) n'est pas lu."""
    v = sans_parentheses(valeur)
    for a, b in (("–", "-"), ("—", "-"), ("−", "-")):
        v = v.replace(a, b)
    v = re.sub(r"(\d)\s+à\s+(\d)", r"\1-\2", v)
    trouves = list(RE_NOM_FICHIER.finditer(v))
    res = []
    for i, m in enumerate(trouves):
        fin = trouves[i + 1].start() if i + 1 < len(trouves) else len(v)
        morceau = v[m.end():fin]
        marque = RE_MARQUE_LIGNES.search(morceau)
        res.append((m.group(1).removeprefix("organisme/"), lire_plages(morceau[marque.end():]) if marque else []))
    return res


def lire_perimetre(texte, carte):
    per = Perimetre()
    vus = {"facteur": [], "element": [], "instance": [], "exception": [], "lieu": [], "accompagnement": [], "essai": []}
    for cle, valeur in lignes_cles(texte):
        vus[cle].append(valeur)
    if not vus["facteur"]:
        raise Refus("(b) pièce de périmètre : aucune ligne « facteur : » (forme lue par G5 : LISEZMOI, § 3)")
    if len(vus["facteur"]) > 1:
        raise Refus("(b) pièce de périmètre : plusieurs lignes « facteur : »")
    ids = set(RE_ID_FACTEUR.findall(vus["facteur"][0]))
    if len(ids) != 1:
        raise Refus(f"(b) pièce de périmètre : la ligne « facteur : » nomme {len(ids)} facteurs (un seul permis)")
    per.facteur = ids.pop()
    if per.facteur not in carte.facteurs:
        raise Refus(f"(b) pièce de périmètre : facteur {per.facteur} absent de la carte")
    for cle, fid, mot, mots in (("element", carte.id_elements, "élément", "éléments"),
                                ("instance", carte.id_instances, "instance", "instances")):
        if per.facteur == fid and fid is not None:
            if len(vus[cle]) != 1:
                raise Refus(f"(b) pièce de périmètre : {fid} demande une seule ligne « {mot} : »")
            sous = set(RE_ID_SOUS.findall(vus[cle][0]))
            if len(sous) != 1:
                raise Refus(f"(b) pièce de périmètre : {len(sous)} {mots} de {fid} déclarés (un seul par correction)")
            per.sous = sous.pop()
            if per.sous not in carte.sous_lignes or not per.sous.startswith(fid + "-"):
                raise Refus(f"(b) pièce de périmètre : {mot} {per.sous} absent de la carte")
        elif vus[cle]:
            raise Refus(f"(b) pièce de périmètre : ligne « {mot} : » pour le facteur {per.facteur}, qui n'en a pas")
    if vus["exception"]:
        if per.facteur != carte.id_defaut:
            raise Refus(f"(c) pièce de périmètre : exception « défaut du chemin des réponses » hors du facteur "
                        f"{carte.id_defaut}")
        for valeur in vus["exception"]:
            v = norm(valeur)
            if "defaut du chemin des reponses" not in v:
                raise Refus("(c) pièce de périmètre : exception autre que « défaut du chemin des réponses »")
            for mot, type_ in (("format", "format"), ("analyse", "analyse"), ("delai", "delai")):
                if re.search(rf"(?<![a-z]){mot}", v):
                    per.exception.add(type_)
        if not per.exception:
            raise Refus("(c) pièce de périmètre : exception sans type (format, analyse ou délai)")
    for valeur in vus["essai"]:
        noms = [nom for nom, _ in fichiers_et_plages(valeur)]
        if not noms:
            raise Refus("pièce de périmètre : « essai hérité adapté : » sans fichier")
        for nom in noms:
            if not nom.startswith("tests/") or nom not in carte.lignes:
                raise Refus(f"pièce de périmètre : essai hérité adapté {nom!r} absent des essais de l'objet")
            per.essais.add(nom)
    for valeur in vus["accompagnement"]:
        for nom, plages in fichiers_et_plages(valeur):
            if nom == "principal.py":
                per.accompagne_principal = True
                for d, fin in plages:
                    for n in range(d, fin + 1):
                        if ("principal.py", n) != carte.ligne_version:
                            raise Refus(f"(i) pièce de périmètre : principal.py l. {n} déclarée comme accompagnement "
                                        f"(seule la ligne VERSION l'est)")
            elif not (nom == "manifeste.json" or RE_CORRECTIONS_NOUVEAU.fullmatch(nom)
                      or RE_ESSAI_NOUVEAU.fullmatch(nom) or nom in per.essais):
                raise Refus(f"(i) pièce de périmètre : {nom} déclaré comme accompagnement, hors de la liste close")
    if not vus["lieu"]:
        raise Refus("(b) pièce de périmètre : aucune ligne « lieu : » (fichier, fonction, l. plages ; LISEZMOI, § 3)")
    for valeur in vus["lieu"]:
        lieux = fichiers_et_plages(valeur)
        if not lieux:
            raise Refus("(b) pièce de périmètre : ligne « lieu : » sans fichier")
        for nom, plages in lieux:
            if not plages:
                raise Refus(f"(b) pièce de périmètre : ligne « lieu : » de {nom} sans lignes (forme « l. 988–996 »)")
            if nom not in carte.lignes:
                if RE_CORRECTIONS_NOUVEAU.fullmatch(nom) or RE_ESSAI_NOUVEAU.fullmatch(nom):
                    continue
                raise Refus(f"(b) pièce de périmètre : {nom} absent de l'objet au commit")
            n_max = len(carte.lignes[nom][0])
            for d, fin in plages:
                if d < 1 or fin < d or fin > n_max:
                    raise Refus(f"(b) pièce de périmètre : {nom} l. {d}–{fin} hors du fichier ({n_max} lignes)")
                for n in range(d, fin + 1):
                    per.lignes.add((nom, n))
    verifier_lignes_declarees(per, carte)
    return per


def verifier_lignes_declarees(per, carte):
    X = per.facteur
    for f, n in sorted(per.lignes):
        cle = (f, n)
        if f == "manifeste.json" or cle == carte.ligne_version or f in per.essais:
            continue
        if f.startswith("tests/"):
            raise Refus(f"(b) pièce de périmètre : {f} l. {n} déclaré sans « essai hérité adapté : »")
        z = carte.zone_ligne.get(cle)
        if z is not None:
            if X == carte.id_defaut and z["statut"] == "E" and z["exception"] in per.exception:
                continue
            raise Refus(f"(c) pièce de périmètre : {f} l. {n} dans la zone interdite {z['zone']} (ligne {z['statut']})")
        if carte.entier.get(cle) == X:
            if per.sous is not None and cle not in carte.sous_lignes[per.sous]:
                raise Refus(f"(b) pièce de périmètre : {f} l. {n} hors de {per.sous} (un seul élément ou une seule "
                            f"borne par correction)")
            continue
        segs = carte.segments.get(cle)
        if segs:
            if any(s["facteur"] == X for s in segs):
                continue
            autres = sorted({s["facteur"] for s in segs})
            raise Refus(f"(b) pièce de périmètre : {f} l. {n} (ligne partagée de {', '.join(autres)}) hors de {X}")
        if cle in carte.entier:
            raise Refus(f"(b) pièce de périmètre : {f} l. {n} est une ligne de {carte.entier[cle]} : le périmètre "
                        f"couvre deux facteurs ({X} et {carte.entier[cle]})")
        if cle in carte.domaine:
            if X == carte.id_defaut:
                continue
            raise Refus(f"(b) pièce de périmètre : {f} l. {n} est du domaine de {carte.id_defaut} : le périmètre "
                        f"couvre deux facteurs ({X} et {carte.id_defaut})")
        raise Refus(f"(b) pièce de périmètre : {f} l. {n} hors de tout facteur")


# ---------------------------------------------------------------------------------------------------------------------
# Diff


class FichierDiff:
    def __init__(self, rel):
        self.rel = rel
        self.blocs = []


class Bloc:
    def __init__(self, a_debut, a_nb, n_debut, n_nb):
        self.a_debut, self.a_nb, self.n_debut, self.n_nb = a_debut, a_nb, n_debut, n_nb
        self.lignes = []


def chemin_entete(reste, prefixe, quoi):
    chemin = reste.split("\t", 1)[0]
    if chemin.startswith('"'):
        raise Refus(f"(f) en-tête {quoi} entre guillemets : chemin non lu")
    if not chemin.startswith(prefixe):
        raise Refus(f"(f) en-tête {quoi} : le chemin ne commence pas par {prefixe}")
    rel = chemin[len(prefixe):]
    parties = rel.split("/")
    if not rel or any(not RE_COMPOSANT.fullmatch(p) or p in (".", "..") for p in parties):
        raise Refus(f"(f) en-tête {quoi} : chemin hors norme")
    return rel


def lire_diff(texte):
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes.pop()
    fichiers = []
    courant = None
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        if ligne.startswith("diff "):
            morceaux = ligne.split(" ")
            if len(morceaux) < 3 or not morceaux[-2].startswith(PREFIXE_ANCIEN) \
                    or not morceaux[-1].startswith(PREFIXE_NOUVEAU):
                raise Refus(f"(f) ligne « diff » du diff (l. {i + 1}) : chemins hors des préfixes "
                            f"{PREFIXE_ANCIEN} et {PREFIXE_NOUVEAU}")
            courant = None
            i += 1
            continue
        if ligne.startswith("Binary files ") or ligne.startswith("Les fichiers binaires "):
            raise Refus(f"diff, l. {i + 1} : fichier binaire, que G5 ne peut pas lire")
        if ligne.startswith("--- "):
            if i + 1 >= len(lignes) or not lignes[i + 1].startswith("+++ "):
                raise Refus(f"diff mal formé, l. {i + 1} : « --- » sans « +++ »")
            ancien = chemin_entete(ligne[4:], PREFIXE_ANCIEN, "ancien (---)")
            nouveau = chemin_entete(lignes[i + 1][4:], PREFIXE_NOUVEAU, "nouveau (+++)")
            if ancien != nouveau:
                raise Refus(f"(f) diff, l. {i + 1} : les en-têtes nomment deux fichiers différents")
            if any(fd.rel == ancien for fd in fichiers):
                raise Refus(f"diff mal formé, l. {i + 1} : fichier {ancien} présent deux fois")
            courant = FichierDiff(ancien)
            fichiers.append(courant)
            i += 2
            continue
        if ligne.startswith("@@"):
            m = RE_BLOC.fullmatch(ligne)
            if courant is None or not m:
                raise Refus(f"diff mal formé, l. {i + 1} : en-tête de bloc")
            bloc = Bloc(int(m.group(1)), int(m.group(2) or 1), int(m.group(3)), int(m.group(4) or 1))
            reste_a, reste_n = bloc.a_nb, bloc.n_nb
            i += 1
            while reste_a > 0 or reste_n > 0:
                if i >= len(lignes):
                    raise Refus("diff mal formé : bloc tronqué")
                x = lignes[i]
                if x.startswith("\\"):
                    if not bloc.lignes:
                        raise Refus(f"diff mal formé, l. {i + 1} : marque de fin de fichier isolée")
                    bloc.lignes[-1][2] = True
                    i += 1
                    continue
                tag = x[:1]
                if tag == " ":
                    reste_a -= 1
                    reste_n -= 1
                elif tag == "-":
                    reste_a -= 1
                elif tag == "+":
                    reste_n -= 1
                else:
                    raise Refus(f"diff mal formé, l. {i + 1} : ligne de bloc sans marque")
                if reste_a < 0 or reste_n < 0:
                    raise Refus(f"diff mal formé, l. {i + 1} : comptes du bloc dépassés")
                bloc.lignes.append([tag, x[1:], False])
                i += 1
            while i < len(lignes) and lignes[i].startswith("\\"):
                bloc.lignes[-1][2] = True
                i += 1
            courant.blocs.append(bloc)
            continue
        raise Refus(f"diff mal formé, l. {i + 1} : ligne hors d'un bloc")
    return fichiers


def appliquer(lignes_a, fin_a, blocs, rel):
    """Applique les blocs aux lignes de l'objet, en vérifiant chaque ligne de contexte et chaque ligne retirée ; rend les
    lignes nouvelles, avec leur fin de ligne."""
    sortie = []
    pos = 0

    def a_fin(idx):
        return True if idx < len(lignes_a) - 1 else fin_a

    for b in blocs:
        debut = b.a_debut - 1 if b.a_nb > 0 else b.a_debut
        if debut < pos or debut > len(lignes_a):
            raise Refus(f"{rel} : blocs du diff hors d'ordre ou hors du fichier")
        sortie.extend([lignes_a[idx], a_fin(idx)] for idx in range(pos, debut))
        pos = debut
        for tag, texte, sans_fin in b.lignes:
            if tag in " -":
                if pos >= len(lignes_a) or lignes_a[pos] != texte or a_fin(pos) == sans_fin:
                    raise Refus(f"{rel} l. {pos + 1} : le diff ne correspond pas à l'objet au commit")
                if tag == " ":
                    sortie.append([texte, not sans_fin])
                pos += 1
            else:
                sortie.append([texte, not sans_fin])
    sortie.extend([lignes_a[idx], a_fin(idx)] for idx in range(pos, len(lignes_a)))
    if any(not fin for _, fin in sortie[:-1]):
        raise Refus(f"{rel} : diff mal formé (fin de ligne absente avant la dernière ligne)")
    return sortie


class Run:
    def __init__(self, ecart):
        self.ecart = ecart
        self.retirees = []
        self.ajoutees = []


def runs_du_bloc(b):
    a = b.a_debut if b.a_nb > 0 else b.a_debut + 1
    n = b.n_debut if b.n_nb > 0 else b.n_debut + 1
    runs = []
    courant = None
    for tag, texte, sans_fin in b.lignes:
        if tag == " ":
            if courant is not None:
                runs.append(courant)
                courant = None
            a += 1
            n += 1
            continue
        if courant is None:
            courant = Run(a - 1)
        if tag == "-":
            courant.retirees.append((a, texte, not sans_fin))
            a += 1
        else:
            courant.ajoutees.append((n, texte, not sans_fin))
            n += 1
    if courant is not None:
        runs.append(courant)
    return runs


# ---------------------------------------------------------------------------------------------------------------------
# Jugement des blocs


def fenetre(a, b):
    """Caractères changés de l'ancienne ligne : ("r", c1, c2) remplacés, ou ("i", g) insertion après la colonne g."""
    p = 0
    m = min(len(a), len(b))
    while p < m and a[p] == b[p]:
        p += 1
    s = 0
    while s < m - p and a[-1 - s] == b[-1 - s]:
        s += 1
    if p + 1 <= len(a) - s:
        return ("r", p + 1, len(a) - s)
    return ("i", p)


def touche(fen, c1, c2):
    if fen[0] == "r":
        return fen[1] <= c2 and fen[2] >= c1
    return c1 - 1 <= fen[1] <= c2


def dedans(fen, c1, c2):
    if fen[0] == "r":
        return c1 <= fen[1] and fen[2] <= c2
    return c1 - 1 <= fen[1] <= c2


class Juge:
    def __init__(self, carte, per):
        self.c = carte
        self.p = per
        self.X = per.facteur

    def exception_couvre(self, z):
        return (self.X == self.c.id_defaut and z["statut"] == "E" and z["exception"] in self.p.exception)

    def ligne_X(self, f, n):
        """Ligne « à X en entier » (carte, § 0, règles 2, 7 et 9)."""
        cle = (f, n)
        if f in self.p.essais:
            return cle not in self.c.zone_ligne
        if self.c.entier.get(cle) == self.X:
            return True
        if self.X == self.c.id_defaut:
            if cle in self.c.domaine:
                return True
            z = self.c.zone_ligne.get(cle)
            if z is not None and self.exception_couvre(z):
                return True
        return False

    def ligne_libre(self, f, n):
        cle = (f, n)
        return cle not in self.c.entier and cle not in self.c.segments and cle not in self.c.zone_ligne

    def declaree(self, f, n):
        return f in self.p.essais or (f, n) in self.p.lignes

    def hors_facteur(self, f, n):
        cle = (f, n)
        if f == "principal.py" and self.p.accompagne_principal:
            return ("i", f"principal.py l. {n} : changement hors de la ligne VERSION, déclaré comme accompagnement")
        z = self.c.zone_ligne.get(cle)
        if z is not None:
            return ("c", f"{f} l. {n} : zone interdite {z['zone']} (ligne {z['statut']})")
        if cle in self.c.entier:
            return ("a", f"{f} l. {n} : ligne du facteur {self.c.entier[cle]}, hors du facteur déclaré {self.X} "
                         f"(deux facteurs)")
        if cle in self.c.domaine:
            return ("a", f"{f} l. {n} : ligne du domaine de {self.c.id_defaut} (défaut nommé), hors du facteur "
                         f"déclaré {self.X} (deux facteurs)")
        return ("hors", f"{f} l. {n} : ligne hors de tout facteur et de la liste d'accompagnement")

    def juger_modif(self, f, n, a, b, fin_a, fin_b):
        cle = (f, n)
        if a == b and fin_a == fin_b:
            return None
        if cle == self.c.ligne_version:
            if RE_VERSION.fullmatch(b) and fin_a == fin_b:
                return None
            return ("i", f"{f} l. {n} : ligne VERSION changée hors de sa forme (sa valeur seulement)")
        fen = fenetre(a, b)
        z = self.c.zone_ligne.get(cle)
        if z is not None and not self.exception_couvre(z):
            precision = "" if z["statut"] != "E" or self.X != self.c.id_defaut else \
                " (exception non déclarée, ou d'un autre type)"
            return ("c", f"{f} l. {n} : zone interdite {z['zone']} (ligne {z['statut']}){precision}")
        for s in self.c.zone_seg.get(cle, []):
            if touche(fen, s["c1"], s["c2"]):
                return ("c", f"{f} l. {n} : caractère changé dans le segment interdit {s['id']} (zone {s['zone']})")
        for s in self.c.phb.get(cle, []):
            if touche(fen, s["c1"], s["c2"]):
                return ("h", f"{f} l. {n} : caractère changé dans le point hors boucle {s['id']} (seuil gelé)")
        segs = self.c.segments.get(cle)
        if segs:
            miens = [s for s in segs if s["facteur"] == self.X]
            autres = [s for s in segs if s["facteur"] != self.X]
            if any(dedans(fen, s["c1"], s["c2"]) for s in miens) and \
                    not any(touche(fen, s["c1"], s["c2"]) for s in autres):
                if not self.declaree(f, n):
                    return ("hors", f"{f} l. {n} : segment de {self.X} hors du périmètre déclaré")
                return None
            touches = sorted({s["facteur"] for s in autres if touche(fen, s["c1"], s["c2"])})
            if touches:
                return ("g", f"{f} l. {n} : ligne partagée, caractère changé dans le segment de {', '.join(touches)} "
                             f"(facteur déclaré : {self.X})")
            return ("g", f"{f} l. {n} : ligne partagée, caractère changé hors des segments de {self.X} (reste de la "
                         f"ligne, à aucun facteur)")
        if self.ligne_X(f, n):
            if not self.declaree(f, n):
                return ("hors", f"{f} l. {n} : ligne de {self.X} hors du périmètre déclaré")
            return None
        return self.hors_facteur(f, n)

    def juger_suppression(self, f, n):
        cle = (f, n)
        if cle == self.c.ligne_version:
            return ("i", f"{f} l. {n} : ligne VERSION supprimée")
        z = self.c.zone_ligne.get(cle)
        if z is not None and not self.exception_couvre(z):
            return ("c", f"{f} l. {n} : ligne de la zone interdite {z['zone']} supprimée")
        if cle in self.c.zone_seg:
            return ("c", f"{f} l. {n} : ligne supprimée qui porte un segment interdit")
        if cle in self.c.phb:
            return ("h", f"{f} l. {n} : ligne supprimée qui porte un point hors boucle")
        if cle in self.c.segments:
            return ("g", f"{f} l. {n} : ligne partagée supprimée (reste de la ligne et autres segments touchés)")
        if self.ligne_X(f, n):
            if not self.declaree(f, n):
                return ("hors", f"{f} l. {n} : ligne de {self.X} hors du périmètre déclaré")
            return None
        return self.hors_facteur(f, n)

    def decrire(self, f, n, n_max):
        cle = (f, n)
        if n < 1:
            return "début du fichier", None
        if n > n_max:
            return "fin du fichier", None
        if self.ligne_X(f, n):
            return f"ligne de {self.X}", None
        z = self.c.zone_ligne.get(cle)
        if z is not None:
            return f"zone {z['zone']}", "c"
        if cle in self.c.segments:
            return "ligne partagée", "g"
        if cle in self.c.entier:
            return f"ligne de {self.c.entier[cle]}", "a"
        return "ligne libre", None

    def juger_insertion(self, f, ecart, n_max):
        n, m = ecart, ecart + 1
        xn = 1 <= n <= n_max and self.ligne_X(f, n)
        xm = 1 <= m <= n_max and self.ligne_X(f, m)
        if n < 1:
            ok = xm
        elif m > n_max:
            ok = xn
        else:
            ok = (xn and (xm or self.ligne_libre(f, m))) or (xm and (xn or self.ligne_libre(f, n)))
        if not ok:
            dn, ln = self.decrire(f, n, n_max)
            dm, lm = self.decrire(f, m, n_max)
            lettre = "c" if "c" in (ln, lm) else "g" if "g" in (ln, lm) else "a" if "a" in (ln, lm) else "hors"
            return (lettre, f"{f} : lignes insérées entre les l. {n} et {m} ({dn} ; {dm}) : n'appartiennent pas à "
                            f"{self.X} (carte, § 0, règle 9)")
        if not ((xn and self.declaree(f, n)) or (xm and self.declaree(f, m))):
            return ("hors", f"{f} : lignes insérées entre les l. {n} et {m}, hors du périmètre déclaré")
        return None

    def juger_run(self, f, run, n_max):
        R, A = run.retirees, run.ajoutees
        if not R:
            return self.juger_insertion(f, run.ecart, n_max)
        k = min(len(R), len(A))
        alignements = [(0, 0, "debut")]
        if len(R) != len(A):
            alignements.append((len(R) - k, len(A) - k, "fin"))
        premier = None
        for dr, da, nom in alignements:
            motif = None
            for i in range(k):
                n, a, fin_a = R[dr + i]
                _, b, fin_b = A[da + i]
                motif = self.juger_modif(f, n, a, b, fin_a, fin_b)
                if motif:
                    break
            if motif is None:
                for n, _, _ in R[:dr] + R[dr + k:]:
                    motif = self.juger_suppression(f, n)
                    if motif:
                        break
            if motif is None and len(A) > k:
                if nom == "debut":
                    ecart = R[k - 1][0] if k > 0 else run.ecart
                else:
                    ecart = R[0][0] - 1
                motif = self.juger_insertion(f, ecart, n_max)
            if motif is None:
                return None
            if premier is None:
                premier = motif
        return premier


def listes_de_mots(texte):
    trouvees = set()
    for g in RE_GROUPE.finditer(texte):
        interieur = g.group(1)
        litteraux = [x or y for x, y in RE_LITTERAL.findall(interieur)]
        reste = RE_LITTERAL.sub("", interieur)
        if len(litteraux) >= 4 and re.fullmatch(r"[\s,]*", reste) and all(RE_MOT.fullmatch(x) for x in litteraux):
            trouvees.add(("liste", tuple(litteraux)))
    for lit in RE_LITTERAL.finditer(texte):
        contenu = lit.group(1) or lit.group(2) or ""
        for m in RE_ALTERNANCE.finditer(contenu):
            trouvees.add(("alternance", m.group(0)))
    return trouvees


def verifier_contenu(rel, run_ajoutees, run_retirees):
    for n, texte, _ in run_ajoutees:
        t = norm(texte)
        for categorie, brut, rx in MOTIFS_INTERDITS:
            if rx.search(texte if brut else t):
                raise Refus(f"(e) {rel}, ligne {n} du nouveau fichier : contenu interdit détectable par motifs "
                            f"({categorie})")
    nouvelles = listes_de_mots("\n".join(t for _, t, _ in run_ajoutees))
    anciennes = listes_de_mots("\n".join(t for _, t, _ in run_retirees))
    for genre, _ in sorted(nouvelles - anciennes):
        premier = run_ajoutees[0][0] if run_ajoutees else 0
        quoi = "liste d'au moins quatre mots" if genre == "liste" else "alternance d'au moins quatre mots"
        raise Refus(f"(e) {rel}, lignes ajoutées à partir de la ligne {premier} du nouveau fichier : contenu interdit "
                    f"détectable par motifs ({quoi}, forme d'une liste de mots)")


def liaisons_gelees(arbre, noms):
    """Occurrences qui affectent, réaffectent, suppriment ou masquent un nom gelé : (nom, genre, ligne début, ligne fin).
    Affectation simple, augmentée ou annotée (l'instruction entière), « := », for, with, except, compréhension, match ;
    attribut ou entrée d'un espace de noms (globals(), vars(), locals(), __dict__) ; def et class ; paramètre (avec sa
    valeur par défaut) ; import ; global et nonlocal ; setattr et delattr (fonction ou méthode) à nom constant."""
    trouvees = []
    parents = {}
    for parent in ast.walk(arbre):
        for enfant in ast.iter_child_nodes(parent):
            parents[enfant] = parent

    def portee(noeud):
        p = parents.get(noeud)
        while p is not None and not isinstance(p, (ast.stmt, ast.NamedExpr)):
            p = parents.get(p)
        return p if isinstance(p, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.NamedExpr)) else noeud

    def ajouter(nom, genre, debut, fin):
        if nom in noms:
            trouvees.append((nom, genre, debut.lineno, getattr(fin, "end_lineno", None) or fin.lineno))

    def espace_de_noms(e):
        return (isinstance(e, ast.Call) and isinstance(e.func, ast.Name) and e.func.id in ("globals", "vars", "locals")) \
            or (isinstance(e, ast.Attribute) and e.attr == "__dict__")

    def chaine(e):
        return e.value if isinstance(e, ast.Constant) and isinstance(e.value, str) else None

    for n in ast.walk(arbre):
        if isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            p = portee(n)
            ajouter(n.id, "affectation ou suppression", p, p)
        elif isinstance(n, ast.Attribute) and isinstance(n.ctx, (ast.Store, ast.Del)):
            p = portee(n)
            ajouter(n.attr, "affectation ou suppression d'attribut", p, p)
        elif isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)) and espace_de_noms(n.value):
            if chaine(n.slice):
                p = portee(n)
                ajouter(chaine(n.slice), "écriture dans un espace de noms", p, p)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            trouvees.extend([(n.name, "définition (def ou class)", n.lineno, n.lineno)] if n.name in noms else [])
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            for x in n.names:
                ajouter(x, "déclaration global ou nonlocal", n, n)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            for alias in n.names:
                if alias.name == "*":
                    if noms:
                        trouvees.append(("*", "import * (peut masquer un nom gelé)", n.lineno, n.end_lineno or n.lineno))
                    continue
                ajouter(alias.asname or alias.name.split(".")[0], "import", n, n)
        elif isinstance(n, ast.ExceptHandler) and n.name:
            trouvees.extend([(n.name, "except … as", n.lineno, n.lineno)] if n.name in noms else [])
        elif isinstance(n, ast.arguments):
            positionnels = n.posonlyargs + n.args
            defauts = [None] * (len(positionnels) - len(n.defaults)) + list(n.defaults)
            for arg, defaut in list(zip(positionnels, defauts)) + list(zip(n.kwonlyargs, n.kw_defaults)):
                ajouter(arg.arg, "paramètre" if defaut is None else "paramètre avec valeur par défaut", arg,
                        defaut if defaut is not None else arg)
            for arg in (n.vararg, n.kwarg):
                if arg is not None:
                    ajouter(arg.arg, "paramètre", arg, arg)
        elif isinstance(n, ast.MatchAs) and n.name:
            ajouter(n.name, "capture de match", n, n)
        elif isinstance(n, ast.MatchStar) and n.name:
            ajouter(n.name, "capture de match", n, n)
        elif isinstance(n, ast.MatchMapping) and n.rest:
            ajouter(n.rest, "capture de match", n, n)
        elif isinstance(n, ast.Call):
            f = n.func
            nom_f = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
            if nom_f in ("setattr", "delattr"):
                for a in n.args[:3]:
                    if chaine(a):
                        ajouter(chaine(a), nom_f, n, n)
            elif nom_f in ("update", "setdefault", "pop", "__setitem__", "__delitem__") and \
                    isinstance(f, ast.Attribute) and espace_de_noms(f.value):
                for a in n.args[:1]:
                    if chaine(a):
                        ajouter(chaine(a), "écriture dans un espace de noms", n, n)
                    if isinstance(a, ast.Dict):
                        for k in a.keys:
                            if k is not None and chaine(k):
                                ajouter(chaine(k), "écriture dans un espace de noms", n, n)
                for kw in n.keywords:
                    if kw.arg:
                        ajouter(kw.arg, "écriture dans un espace de noms", n, n)
    return trouvees


def controler_noms_geles(rel, ancien, nouveau, ajoutees, retirees, noms):
    """Analyse syntaxique du fichier nouveau, comparé à l'ancien : aucune ligne ajoutée ou changée ne porte une liaison
    d'un nom gelé, aucune ligne retirée n'en portait une."""
    try:
        arbre_nouveau = ast.parse(nouveau)
    except SyntaxError as e:
        raise Refus(f"(noms gelés) {rel} : le fichier nouveau ne s'analyse pas (ligne {e.lineno}) : contrôle impossible")
    for nom, genre, d, f in liaisons_gelees(arbre_nouveau, noms):
        if any(d <= x <= f for x in ajoutees):
            raise Refus(f"(noms gelés) {rel}, ligne {d} du nouveau fichier : {genre} du nom gelé « {nom} »")
    if ancien is not None and retirees:
        try:
            arbre_ancien = ast.parse(ancien)
        except SyntaxError as e:
            raise Refus(f"(noms gelés) {rel} : l'objet ne s'analyse pas (ligne {e.lineno}) : contrôle impossible")
        for nom, genre, d, f in liaisons_gelees(arbre_ancien, noms):
            if any(d <= x <= f for x in retirees):
                raise Refus(f"(noms gelés) {rel}, l. {d} de l'objet : {genre} du nom gelé « {nom} » retirée ou changée")


def verifier_manifeste(ancien, nouveau):
    try:
        a = json.loads(ancien)
        b = json.loads(nouveau)
    except json.JSONDecodeError:
        raise Refus("manifeste.json : JSON illisible après le diff")
    if not isinstance(a, dict) or not isinstance(b, dict) or list(a) != list(b):
        raise Refus("manifeste.json : clés changées (accompagnement : version et description seulement)")
    for cle in a:
        if cle not in ("version", "description") and a[cle] != b[cle]:
            raise Refus(f"manifeste.json : champ « {cle} » changé (accompagnement : version et description seulement)")


# ---------------------------------------------------------------------------------------------------------------------


def analyser(argv):
    p = Analyseur(prog="garde_g5_perimetre_v1.py",
                  description="Garde G5 : un diff de correction contre la carte des facteurs, les zones interdites et "
                              "la pièce de périmètre.")
    p.add_argument("--diff", required=True, type=pathlib.Path)
    p.add_argument("--perimetre", required=True, type=pathlib.Path)
    p.add_argument("--empreinte-perimetre", required=True,
                   help="empreinte de la pièce de périmètre consignée par conv-audit avant le diff")
    p.add_argument("--carte", required=True, type=pathlib.Path, help="carte-facteurs-v<n>.json")
    p.add_argument("--empreinte-carte", required=True)
    p.add_argument("--zones", required=True, type=pathlib.Path, help="zones-interdites-v<n>.json")
    p.add_argument("--empreinte-zones", required=True)
    p.add_argument("--objet", required=True, type=pathlib.Path, help="objet-origine/")
    p.add_argument("--copie", required=True, type=pathlib.Path, help="copie-organisme/")
    a = p.parse_args(argv)
    for nom in ("empreinte_perimetre", "empreinte_carte", "empreinte_zones"):
        if not RE_HEX64.fullmatch(getattr(a, nom)):
            raise Usage(f"--{nom.replace('_', '-')} : 64 caractères hexadécimaux en minuscules attendus")
    return a


def executer(a):
    for chemin, attendue, quoi in ((a.carte, a.empreinte_carte, "carte des facteurs"),
                                   (a.zones, a.empreinte_zones, "zones interdites"),
                                   (a.perimetre, a.empreinte_perimetre, "pièce de périmètre")):
        if verifier_compagnon(chemin, quoi) != attendue:
            raise Refus(f"{quoi} : empreinte différente de celle qui est attendue")
    empreinte_diff = verifier_compagnon(a.diff, "diff")
    try:
        carte_json = json.loads(a.carte.read_text(encoding="utf-8"))
        zones_json = json.loads(a.zones.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Refus("carte ou zones : JSON illisible")
    carte = Carte(carte_json, zones_json, a.objet)
    per = lire_perimetre(lire_texte(a.perimetre, "pièce de périmètre"), carte)
    fichiers = lire_diff(lire_texte(a.diff, "diff"))
    if not fichiers:
        raise Refus("diff vide : aucune correction")
    copie = lister_fichiers(a.copie, "copie-organisme")
    juge = Juge(carte, per)
    nouveaux = {"corrections": 0, "essai": 0}
    reconstruits = {}
    nb_blocs = 0
    accompagnement = []
    for fd in fichiers:
        rel = fd.rel
        if not fd.blocs:
            raise Refus(f"diff mal formé : {rel} sans bloc")
        nouveau = rel not in carte.lignes
        if nouveau:
            if any(b.a_debut != 0 or b.a_nb != 0 for b in fd.blocs) or len(fd.blocs) != 1:
                raise Refus(f"{rel} : fichier absent de l'objet, mais le diff le traite comme ancien")
            if RE_CORRECTIONS_NOUVEAU.fullmatch(rel):
                genre = "corrections"
            elif RE_ESSAI_NOUVEAU.fullmatch(rel):
                genre = "essai"
            else:
                raise Refus(f"(d) {rel} : fichier nouveau hors de la liste d'accompagnement")
            nouveaux[genre] += 1
            if nouveaux[genre] > 1:
                raise Refus(f"(d) {rel} : deuxième fichier nouveau du même genre (un seul permis)")
            lignes_a, fin_a = [], True
            accompagnement.append(rel)
        else:
            if rel not in copie:
                raise Refus(f"(d) {rel} : fichier de l'objet supprimé (hors de la liste d'accompagnement)")
            lignes_a, fin_a = carte.lignes[rel]
        sortie = appliquer(lignes_a, fin_a, fd.blocs, rel)
        reconstruits[rel] = "".join(t + ("\n" if fin else "") for t, fin in sortie)
        runs = [r for b in fd.blocs for r in runs_du_bloc(b)]
        nb_blocs += len(runs)
        if not nouveau:
            if rel == "manifeste.json":
                for run in runs:
                    for n, _, _ in run.retirees:
                        z = carte.zone_ligne.get((rel, n))
                        if z is not None:
                            raise Refus(f"(c) manifeste.json l. {n} : zone interdite {z['zone']}")
                verifier_manifeste("\n".join(lignes_a) + ("\n" if fin_a else ""), reconstruits[rel])
                accompagnement.append(rel)
            else:
                if rel.startswith("tests/") and rel not in per.essais:
                    raise Refus(f"{rel} : essai hérité modifié sans « essai hérité adapté : » dans la pièce de "
                                f"périmètre")
                for run in runs:
                    motif = juge.juger_run(rel, run, len(lignes_a))
                    if motif is not None:
                        lettre, texte = motif
                        prefixe = "" if lettre == "hors" else f"({lettre}) "
                        raise Refus(prefixe + texte)
                if carte.ligne_version is not None and carte.ligne_version[0] == rel and any(
                        n == carte.ligne_version[1] for run in runs for n, _, _ in run.retirees):
                    accompagnement.append(f"{rel} (ligne VERSION)")
        for run in runs:
            verifier_contenu(rel, run.ajoutees, run.retirees)
        if carte.noms_geles and rel.endswith(".py"):
            ancien = None if nouveau else "\n".join(lignes_a) + ("\n" if fin_a and lignes_a else "")
            controler_noms_geles(rel, ancien, reconstruits[rel],
                                 {n for run in runs for n, _, _ in run.ajoutees},
                                 {n for run in runs for n, _, _ in run.retirees}, carte.noms_geles)
    for rel, p in copie.items():
        if rel in reconstruits:
            if p.read_bytes() != reconstruits[rel].encode("utf-8"):
                raise Refus(f"copie-organisme : {rel} n'est pas l'objet modifié par le diff")
        elif rel in carte.lignes:
            if sha256_fichier(p) != carte_json["objet"]["sha256_fichiers"][rel]:
                raise Refus(f"copie-organisme : {rel} changé hors du diff")
        else:
            raise Refus(f"copie-organisme : {rel} absent du diff (fichier nouveau non déclaré au diff)")
    for rel in carte.lignes:
        if rel not in copie and rel not in reconstruits:
            raise Refus(f"copie-organisme : {rel} absent, sans que le diff le supprime")
    sous = f", {per.sous}" if per.sous else ""
    exc = f", exception « défaut du chemin des réponses » ({', '.join(sorted(per.exception))}) : revue à part par le " \
          f"contre-lecteur" if per.exception else ""
    acc = ", ".join(accompagnement) if accompagnement else "aucun"
    print(f"G5 : diff accepté — facteur {per.facteur}{sous}{exc} ; {nb_blocs} blocs dans le périmètre ; "
          f"accompagnement : {acc} ; diff sha256 {empreinte_diff}")
    return 0


def principal(argv=None):
    try:
        return executer(analyser(argv))
    except Usage as e:
        print(f"USAGE {GARDE} : {e}", file=sys.stderr)
        return 2
    except Refus as e:
        print(f"REFUS {GARDE} {e}" if str(e).startswith("(") else f"REFUS {GARDE} : {e}", file=sys.stderr)
        return 3
    except Exception as e:  # erreur interne : type et ligne seulement, jamais le message (il pourrait citer un contenu)
        pile = traceback.extract_tb(e.__traceback__)
        ligne = pile[-1].lineno if pile else 0
        print(f"ERREUR INTERNE {GARDE} : {type(e).__name__} (ligne {ligne})", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(principal())
