#!/usr/bin/env python3
"""Assemblage d'un dossier de lecture du pilote 4 (boucle extérieure) — v1.

Protocole de la boucle extérieure v4, § 3 (dossiers de lecture), § 1, § 9 et § 11 (gardes G1, G2, G8 bis (b), G12).
Deux modes :
- `course` (fin de course) : MANIFESTE-DOSSIER-v1.txt, ouverture-lecture-<dossier>-v1.txt, lecture/ (A-test : fichiers
  json et md du script de lecture), mecanique/ (relevé B), registre/, protocole/, objet/ (copie de lecture de
  l'organisme) et objet-EMPREINTE-ARBRE.txt à côté, carte-facteurs-v<n>.md et zones-interdites-v<n>.md ;
- `finale` (fin du compteur) : MANIFESTE-DOSSIER-FINAL-v1.txt, ouverture-lecture-finale-<dossier>-v1.txt,
  lecture-finale/ (A-final « holm-quatre » ou « holm-deux », copiés sans être ouverts), mecanique/, registre/,
  protocole/.
Chaque pièce est copiée depuis un chemin nommé en argument, son compagnon vérifié et copié ; aucun journal. Gardes, dans
cet ordre : G12 (noms et versions des fichiers de lecture), compagnons, G2 (forme du fichier d'ouverture ; la référence
elle-même est contrôlée par conv-audit), G1 (liste fermée du dossier de course vérifiée et close ; relevé : fin de course,
recherche des clés, pas de reprise attendue), identité (relevé de ce dossier, commit du segment 1, arbre), G8 bis (b)
(le seul fichier test réel : ni test_final, ni ligne (iii), ni valeur p, ni mention d'essai), arbre de l'objet. Aucun
fichier test_final n'est jamais ouvert : il est haché et copié octet par octet. Au premier échec : refus (code 3, motif
sur la sortie d'erreur, sans contenu de pièce), et rien n'est laissé : le dossier se construit à côté, sous un nom
provisoire, et n'est renommé qu'à la fin. Bibliothèque standard seule ; `python3 -I`.

Codes de sortie : 0 assemblé ; 2 usage ; 3 refusé ; 4 erreur interne (type et ligne seulement).
"""

import argparse
import hashlib
import json
import os
import pathlib
import re
import shutil
import stat
import sys
import traceback
import unicodedata

PROG = "assemblage"
RE_HEX64 = re.compile(r"[0-9a-f]{64}")
RE_HEX64_MOT = re.compile(r"(?<![0-9a-fA-F])[0-9a-f]{64}(?![0-9a-fA-F])")
RE_COMMIT = re.compile(r"[0-9a-f]{7,40}")
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
RE_COMPOSANT = re.compile(r"[A-Za-z0-9_][A-Za-z0-9._-]*")
RE_DOSSIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
RE_SCRIPT = re.compile(r"lire_pilote4_v(\d+)\.py")
RE_LECTURE = re.compile(r"lecture-(?P<d>.+?)-test(?P<f>-final-holm-(?P<h>quatre|deux))?-v(?P<v>\d+)\.(?P<e>json|md)")
RE_REGISTRE = re.compile(r"registre-hypotheses-conception-pilote4-v\d+\.md")
RE_PROTOCOLE = re.compile(r"protocole-boucle-exterieure-pilote4-v\d+\.md")
RE_CARTE = re.compile(r"carte-facteurs-v\d+\.md")
RE_ZONES = re.compile(r"zones-interdites-v\d+\.md")
RE_RELEVE_LIGNE = re.compile(r"([a-z0-9_.<>-]+) = (.*)")
RE_HEURE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z|\d{4}-\d{2}-\d{2} (?:à|a) \d{2}:\d{2}:\d{2} UTC")
LISTE_FERMEE = "EMPREINTES-pilote-v1.txt"

# G8 bis (b) : ce que le fichier test réel ne porte jamais (texte sans accents, en minuscules).
MOTIFS_TEST = [
    ("le mot test_final", r"test[\s_-]*final"),
    ("une ligne (iii)", r"\(iii\)|(?<![a-z0-9])iii(?![a-z0-9])|mcnemar|(?<![a-z])holm(?![a-z])"),
    ("une valeur p", r"(?<![a-z0-9_])valeurs?[\s_]?p(?![a-z0-9_])|(?<![a-z0-9_])p[\s_-]?val(?:ue|eur)s?(?![a-z0-9_])"
                     r"|\"p(?:_[a-z_]+)?\"\s*:|(?<![a-z0-9_.])p\s*[=<>≤≥]\s*\d"),
    ("la mention d'essai", r"empreintes? de (?:la )?banque surcharg|(?<![a-z0-9_])essai\s*:|\"essai\"\s*:"),
]
MOTIFS_TEST = [(quoi, re.compile(rx)) for quoi, rx in MOTIFS_TEST]


class Refus(Exception):
    """Refus de l'assemblage : code 3."""


class Usage(Exception):
    """Erreur d'usage : code 2."""


class Analyseur(argparse.ArgumentParser):
    def error(self, message):
        raise Usage(message)


def norm(texte):
    t = unicodedata.normalize("NFD", texte)
    t = unicodedata.normalize("NFC", "".join(c for c in t if unicodedata.category(c) != "Mn")).casefold()
    for a, b in (("’", "'"), ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " ")):
        t = t.replace(a, b)
    return t


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def empreinte_arbre(dossier: pathlib.Path) -> str:
    """Empreinte d'arbre du noyau (essaim_m3/noyau/boucle.py), reproduite à l'identique."""
    h = hashlib.sha256()
    for f in sorted(p for p in pathlib.Path(dossier).rglob("*")
                    if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(dossier).parts):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()


def mode_de(chemin):
    try:
        return os.lstat(chemin).st_mode
    except FileNotFoundError:
        return None


def fichier_ordinaire(chemin, quoi, garde=""):
    mode = mode_de(chemin)
    prefixe = f"{garde} : " if garde else ""
    if mode is None:
        raise Refus(f"{prefixe}{quoi} absent ({chemin.name})")
    if stat.S_ISLNK(mode):
        raise Refus(f"{prefixe}{quoi} est un lien symbolique ({chemin.name})")
    if not stat.S_ISREG(mode):
        raise Refus(f"{prefixe}{quoi} n'est pas un fichier ordinaire ({chemin.name})")


def verifier_compagnon(chemin, quoi, garde=""):
    """Vérifie le compagnon « empreinte, deux espaces, nom nu » sans ouvrir le contenu du fichier (il est haché)."""
    fichier_ordinaire(chemin, quoi, garde)
    compagnon = chemin.with_name(chemin.name + ".sha256")
    fichier_ordinaire(compagnon, f"compagnon de {quoi}", garde)
    prefixe = f"{garde} : " if garde else ""
    try:
        texte = compagnon.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"{prefixe}compagnon de {quoi} illisible")
    m = RE_COMPAGNON.fullmatch(texte)
    if not m:
        raise Refus(f"{prefixe}compagnon de {quoi} mal formé (attendu : « empreinte, deux espaces, nom nu »)")
    if m.group(2) != chemin.name:
        raise Refus(f"{prefixe}compagnon de {quoi} : il nomme un autre fichier")
    empreinte = sha256_fichier(chemin)
    if empreinte != m.group(1):
        raise Refus(f"{prefixe}compagnon de {quoi} : empreinte différente de celle du fichier")
    return empreinte


def lister_dossier(racine, quoi, garde=""):
    """Fichiers ordinaires sous racine, par chemin relatif ; refuse liens symboliques et fichiers spéciaux."""
    prefixe = f"{garde} : " if garde else ""
    mode = mode_de(racine)
    if mode is None or stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
        raise Refus(f"{prefixe}{quoi} absent, ou n'est pas un dossier ordinaire")
    fichiers = {}
    for dossier, sous, noms in os.walk(racine, followlinks=False):
        for nom in sorted(sous) + sorted(noms):
            p = pathlib.Path(dossier) / nom
            rel = p.relative_to(racine).as_posix()
            m = os.lstat(p).st_mode
            if stat.S_ISLNK(m):
                raise Refus(f"{prefixe}{quoi} : lien symbolique ({rel})")
            if nom in noms:
                if not stat.S_ISREG(m):
                    raise Refus(f"{prefixe}{quoi} : fichier spécial ({rel})")
                fichiers[rel] = p
    return fichiers


# ---------------------------------------------------------------------------------------------------------------------
# G12 : noms et versions des fichiers de lecture


def verifier_noms(a, n):
    tous = [a.releve, a.ouverture, a.lecture_json, a.lecture_md, a.registre, a.protocole, a.script_lecture]
    if a.mode == "course":
        tous += [a.carte, a.zones]
    for p in tous:
        if "-provisoire-" in p.name:
            raise Refus(f"G12 : {p.name} porte « -provisoire- » (sortie d'une version du script inférieure à 3)")
    if n < 3:
        raise Refus(f"G12 : script de lecture de version {n}, inférieure à 3")
    genres = set()
    for p, ext in ((a.lecture_json, "json"), (a.lecture_md, "md")):
        m = RE_LECTURE.fullmatch(p.name)
        if not m:
            raise Refus(f"G12 : {p.name} n'est pas un nom de fichier de lecture du script v3")
        v = int(m.group("v"))
        if v < 3:
            raise Refus(f"G12 : {p.name} : fichier de lecture de version {v}, inférieure à 3")
        if v != n:
            raise Refus(f"G12 : {p.name} : version {v}, autre que celle du script ({n}) écrite au manifeste")
        if m.group("d") != a.dossier:
            raise Refus(f"G12 : {p.name} ne porte pas le nom du dossier {a.dossier}")
        if m.group("e") != ext:
            raise Refus(f"G12 : {p.name} : extension autre que .{ext}")
        if a.mode == "course" and m.group("f"):
            raise Refus(f"G8 bis (b) : {p.name} est un fichier test_final : jamais dans un dossier de course (non "
                        f"ouvert)")
        if a.mode == "finale" and not m.group("f"):
            raise Refus(f"G12 : {p.name} n'est pas un fichier test_final « holm-quatre » ou « holm-deux »")
        genres.add(m.group("h"))
    if len(genres) != 1:
        raise Refus("G12 : les fichiers json et md de lecture ne sont pas du même genre (holm-quatre et holm-deux)")
    attendu = f"ouverture-lecture-{a.dossier}-v1.txt" if a.mode == "course" else \
        f"ouverture-lecture-finale-{a.dossier}-v1.txt"
    if a.ouverture.name != attendu:
        raise Refus(f"G2 : fichier d'ouverture nommé {a.ouverture.name} au lieu de {attendu}")
    if a.releve.name != f"releve-mecanique-{a.dossier}-v1.txt":
        raise Refus(f"G1 : relevé nommé {a.releve.name} au lieu de releve-mecanique-{a.dossier}-v1.txt")
    for p, rx, quoi in ((a.registre, RE_REGISTRE, "registre"), (a.protocole, RE_PROTOCOLE, "protocole")) + \
            (((a.carte, RE_CARTE, "carte des facteurs"), (a.zones, RE_ZONES, "zones interdites"))
             if a.mode == "course" else ()):
        if not rx.fullmatch(p.name):
            raise Refus(f"{quoi} : nom inattendu ({p.name})")


# ---------------------------------------------------------------------------------------------------------------------
# G2 : forme du fichier d'ouverture


def verifier_ouverture(chemin):
    try:
        texte = chemin.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus("G2 : fichier d'ouverture illisible (UTF-8 attendu)")
    if not texte.strip():
        raise Refus("G2 : fichier d'ouverture vide : la lecture n'est pas ouverte")
    reference = False
    for ligne in texte.split("\n"):
        n = norm(ligne)
        if "reference" in n and RE_HEX64_MOT.search(ligne) and re.search(r"(?<![a-z])(?:ligne|message)", n):
            reference = True
    if not reference:
        raise Refus("G2 : le fichier d'ouverture ne cite aucune référence vérifiable (ligne « référence : » qui nomme "
                    "une ligne du registre des décisions ou un message du canal, avec son empreinte complète)")
    if not RE_HEURE.search(texte):
        raise Refus("G2 : le fichier d'ouverture ne porte aucune heure UTC (lue sur date -u)")


# ---------------------------------------------------------------------------------------------------------------------
# G1 : liste fermée et fin de course


def verifier_liste_fermee(dossier_course):
    """Liste fermée : EMPREINTES-pilote-v1.txt et son compagnon ; chaque ligne vérifiée (fichiers hachés, jamais
    ouverts) ; liste close : tout fichier du dossier y figure, hors la liste et son compagnon. Rend son empreinte."""
    racine = pathlib.Path(dossier_course)
    fichiers = lister_dossier(racine, "dossier de course", "G1")
    liste = racine / LISTE_FERMEE
    if LISTE_FERMEE not in fichiers:
        raise Refus(f"G1 : liste fermée absente ({LISTE_FERMEE}) : course non finie ou non poussée")
    empreinte = verifier_compagnon(liste, "liste fermée", "G1")
    try:
        lignes = liste.read_bytes().decode("utf-8").split("\n")
    except UnicodeDecodeError:
        raise Refus("G1 : liste fermée illisible")
    if lignes and lignes[-1] == "":
        lignes.pop()
    if not lignes:
        raise Refus("G1 : liste fermée vide")
    vus = set()
    for i, ligne in enumerate(lignes, 1):
        m = re.fullmatch(r"([0-9a-f]{64})  (.+)", ligne)
        if not m or "\r" in ligne:
            raise Refus(f"G1 : liste fermée, ligne {i} mal formée")
        nom = m.group(2)
        parties = nom.split("/")
        if nom.startswith("/") or "\\" in nom or any(p in ("", ".", "..") for p in parties):
            raise Refus(f"G1 : liste fermée, ligne {i} : nom absolu, vide ou remontant")
        if nom in vus:
            raise Refus(f"G1 : liste fermée, ligne {i} : doublon")
        vus.add(nom)
        if nom not in fichiers:
            raise Refus(f"G1 : liste fermée, ligne {i} : fichier absent du dossier de course (ou lien symbolique)")
        if sha256_fichier(fichiers[nom]) != m.group(1):
            raise Refus(f"G1 : liste fermée, ligne {i} : empreinte différente ({nom})")
    hors = sorted(set(fichiers) - vus - {LISTE_FERMEE, LISTE_FERMEE + ".sha256"})
    if hors:
        raise Refus(f"G1 : fichier du dossier de course hors de la liste fermée ({hors[0]}"
                    f"{' et ' + str(len(hors) - 1) + ' autres' if len(hors) > 1 else ''})")
    return empreinte


def lire_releve(chemin):
    try:
        lignes = chemin.read_bytes().decode("utf-8").split("\n")
    except UnicodeDecodeError:
        raise Refus("G1 : relevé illisible (UTF-8 attendu)")
    champs = {}
    for i, ligne in enumerate(lignes, 1):
        if not ligne.strip() or ligne.startswith("#"):
            continue
        m = RE_RELEVE_LIGNE.fullmatch(ligne)
        if not m:
            raise Refus(f"G1 : relevé, ligne {i} hors de la forme « clé = valeur »")
        if m.group(1) in champs:
            raise Refus(f"G1 : relevé, champ {m.group(1)} présent deux fois")
        champs[m.group(1)] = m.group(2)
    return champs


def exiger(champs, cle, attendu, garde, motif):
    if cle not in champs:
        raise Refus(f"{garde} : champ {cle} absent du relevé")
    if champs[cle] != attendu:
        raise Refus(f"{garde} : {cle} ne vaut pas « {attendu} » ({motif})")


def verifier_g1_et_identite(a, empreinte_liste):
    champs = lire_releve(a.releve)
    exiger(champs, "releve.dossier", a.dossier, "identité (§ 9)", "relevé d'un autre dossier de course")
    exiger(champs, "sources.liste_fermee", empreinte_liste, "G1",
           "le relevé ne cite pas la liste fermée vérifiée du dossier de course")
    exiger(champs, "sources.liste_fermee_verifiee", "oui", "G1", "liste fermée non vérifiée par le relevé")
    exiger(champs, "fin.liste_fermee_poussee", "oui", "G1", "liste fermée non poussée : course non finie")
    exiger(champs, "fin.recherche_cles_faite", "oui", "G1", "recherche des clés non consignée")
    exiger(champs, "fin.reprise_attendue", "non", "G1",
           "course arrêtée entre deux segments, une reprise est attendue : jamais lue")
    commit = champs.get("identite.commit")
    if commit is None:
        raise Refus("identité (§ 9) : champ identite.commit absent du relevé")
    court, long_ = sorted((commit, a.commit_attendu), key=len)
    if not RE_COMMIT.fullmatch(commit) or not long_.startswith(court):
        raise Refus("identité (§ 9) : identite.commit n'est pas la tête citée au message de départ : aucun "
                    "assemblage, fait suspect")
    exiger(champs, "identite.arbre", a.arbre_attendu, "identité (§ 9)", "arbre de l'organisme autre que celui attendu")


# ---------------------------------------------------------------------------------------------------------------------
# G8 bis (b) : le seul fichier test réel


def verifier_fichier_test(chemin):
    try:
        texte = chemin.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"G8 bis (b) : {chemin.name} illisible (UTF-8 attendu)")
    textes = [texte]
    if chemin.suffix == ".json":
        try:
            textes.append(json.dumps(json.loads(texte), ensure_ascii=False))
        except json.JSONDecodeError:
            raise Refus(f"G8 bis (b) : {chemin.name} n'est pas un JSON lisible")
    for t in textes:
        for n, ligne in enumerate(t.split("\n"), 1):
            l = norm(ligne)
            for quoi, rx in MOTIFS_TEST:
                if rx.search(l):
                    raise Refus(f"G8 bis (b) : le fichier test {chemin.name} porte {quoi} (ligne {n}) : assemblage "
                                f"refusé")


# ---------------------------------------------------------------------------------------------------------------------
# Construction


def copier(source, destination, attendue):
    """Copie octet par octet (le fichier n'est ni décodé ni interprété), en création exclusive ; vérifie l'empreinte."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    with open(source, "rb") as s, open(destination, "xb") as d:
        for bloc in iter(lambda: s.read(1 << 20), b""):
            h.update(bloc)
            d.write(bloc)
    if h.hexdigest() != attendue:
        raise Refus(f"copie de {source.name} : empreinte différente après copie (fichier changé pendant l'assemblage)")


def lister_objet(objet):
    fichiers = lister_dossier(objet, "objet")
    for rel in fichiers:
        parties = rel.split("/")
        if "__pycache__" in parties or rel.endswith(".pyc"):
            raise Refus(f"objet : fichier compilé ({rel}) : à retirer avant l'assemblage")
        if not all(RE_COMPOSANT.fullmatch(p) for p in parties):
            raise Refus(f"objet : nom hors norme ({rel!r})")
    return fichiers


def analyser(argv):
    p = Analyseur(prog="assembler_dossier_lecture_v1.py",
                  description="Assemble un dossier de lecture (mode course) ou de lecture finale (mode finale) du "
                              "pilote 4, et applique G1, G2, G8 bis (b) et G12.")
    p.add_argument("--mode", required=True, choices=("course", "finale"))
    p.add_argument("--dossier", required=True, help="nom exact du dossier de course poussé par session-depot")
    p.add_argument("--sortie", required=True, type=pathlib.Path, help="dossier de lecture à créer (n'existe pas)")
    p.add_argument("--dossier-course", required=True, type=pathlib.Path,
                   help="copie poussée du dossier de course (liste fermée ; les fichiers sont hachés, jamais ouverts)")
    p.add_argument("--releve", required=True, type=pathlib.Path, help="releve-mecanique-<dossier>-v1.txt")
    p.add_argument("--ouverture", required=True, type=pathlib.Path,
                   help="ouverture-lecture-<dossier>-v1.txt (course) ou ouverture-lecture-finale-<dossier>-v1.txt")
    p.add_argument("--lecture-json", required=True, type=pathlib.Path)
    p.add_argument("--lecture-md", required=True, type=pathlib.Path)
    p.add_argument("--registre", required=True, type=pathlib.Path)
    p.add_argument("--protocole", required=True, type=pathlib.Path)
    p.add_argument("--script-lecture", required=True, type=pathlib.Path,
                   help="lire_pilote4_v<n>.py (avec compagnon) : sa version et son empreinte font la ligne de version")
    p.add_argument("--commit-attendu", required=True, help="tête citée au message de départ de la course")
    p.add_argument("--arbre-attendu", required=True, help="empreinte d'arbre attendue de l'organisme")
    p.add_argument("--objet", type=pathlib.Path, help="mode course : organisme/ au commit de l'objet")
    p.add_argument("--carte", type=pathlib.Path, help="mode course : carte-facteurs-v<n>.md")
    p.add_argument("--zones", type=pathlib.Path, help="mode course : zones-interdites-v<n>.md")
    a = p.parse_args(argv)
    if not RE_DOSSIER.fullmatch(a.dossier):
        raise Usage("--dossier : nom de dossier hors norme")
    if not RE_COMMIT.fullmatch(a.commit_attendu):
        raise Usage("--commit-attendu : 7 à 40 caractères hexadécimaux en minuscules attendus")
    if not RE_HEX64.fullmatch(a.arbre_attendu):
        raise Usage("--arbre-attendu : 64 caractères hexadécimaux en minuscules attendus")
    supplementaires = [x for x in ("objet", "carte", "zones") if getattr(a, x) is not None]
    if a.mode == "course" and len(supplementaires) != 3:
        raise Usage("mode course : --objet, --carte et --zones sont exigés")
    if a.mode == "finale" and supplementaires:
        raise Usage("mode finale : ni --objet, ni --carte, ni --zones (protocole, § 3)")
    m = RE_SCRIPT.fullmatch(a.script_lecture.name)
    if not m:
        raise Usage("--script-lecture : nom de la forme lire_pilote4_v<n>.py attendu")
    a.version = int(m.group(1))
    return a


def assembler(a):
    sortie = a.sortie.absolute()
    if mode_de(sortie) is not None:
        raise Refus(f"le dossier de sortie existe déjà ({sortie.name}) : rien n'est écrasé")
    parent = sortie.parent
    if mode_de(parent) is None or not stat.S_ISDIR(mode_de(parent)):
        raise Usage("le dossier parent de --sortie n'existe pas")
    for entree in [a.dossier_course] + ([a.objet] if a.objet else []):
        racine = entree.resolve()
        if sortie.resolve() == racine or racine in sortie.resolve().parents:
            raise Usage("--sortie ne peut pas être dans le dossier de course ni dans l'objet")
    verifier_noms(a, a.version)
    pieces = [(a.ouverture, "fichier d'ouverture", "G2"), (a.releve, "relevé", "G1"),
              (a.lecture_json, "fichier de lecture json", ""), (a.lecture_md, "fichier de lecture md", ""),
              (a.registre, "registre", ""), (a.protocole, "protocole", ""),
              (a.script_lecture, "script de lecture", "")]
    if a.mode == "course":
        pieces += [(a.carte, "carte des facteurs", ""), (a.zones, "zones interdites", "")]
    empreintes = {}
    for chemin, quoi, garde in pieces:
        empreintes[chemin] = verifier_compagnon(chemin, quoi, garde)
    verifier_ouverture(a.ouverture)
    empreinte_liste = verifier_liste_fermee(a.dossier_course)
    verifier_g1_et_identite(a, empreinte_liste)
    if a.mode == "course":
        verifier_fichier_test(a.lecture_json)
        verifier_fichier_test(a.lecture_md)
        objet = lister_objet(a.objet)
        if empreinte_arbre(a.objet) != a.arbre_attendu:
            raise Refus("objet : empreinte d'arbre différente de celle qui est attendue")
    provisoire = parent / f".{sortie.name}.en-cours-{os.getpid()}"
    if mode_de(provisoire) is not None:
        raise Refus("un dossier provisoire du même nom existe déjà : rien n'est écrasé")
    os.mkdir(provisoire, 0o755)
    try:
        lecture = "lecture" if a.mode == "course" else "lecture-finale"
        places = [(a.ouverture, "."), (a.releve, "mecanique"), (a.lecture_json, lecture), (a.lecture_md, lecture),
                  (a.registre, "registre"), (a.protocole, "protocole")]
        if a.mode == "course":
            places += [(a.carte, "."), (a.zones, ".")]
        for chemin, ou in places:
            cible = provisoire / ou / chemin.name
            copier(chemin, cible, empreintes[chemin])
            compagnon = chemin.with_name(chemin.name + ".sha256")
            copier(compagnon, cible.with_name(cible.name + ".sha256"), sha256_fichier(compagnon))
        if a.mode == "course":
            for rel, source in sorted(objet.items()):
                copier(source, provisoire / "objet" / rel, sha256_fichier(source))
            arbre = empreinte_arbre(provisoire / "objet")
            if arbre != a.arbre_attendu:
                raise Refus("objet/ : empreinte d'arbre de la copie différente de celle qui est attendue")
            with open(provisoire / "objet-EMPREINTE-ARBRE.txt", "x", encoding="ascii") as f:
                f.write(arbre + "\n")
        nom_manifeste = "MANIFESTE-DOSSIER-v1.txt" if a.mode == "course" else "MANIFESTE-DOSSIER-FINAL-v1.txt"
        fichiers = lister_dossier(provisoire, "dossier provisoire")
        for rel in fichiers:
            if not all(RE_COMPOSANT.fullmatch(x) for x in rel.split("/")):
                raise Refus(f"nom hors norme dans le dossier ({rel!r}) : le manifeste ne le porterait pas tel quel")
        lignes = [f"# script de lecture : {a.script_lecture.name}, sha256 {empreintes[a.script_lecture]}, "
                  f"version {a.version}\n"]
        lignes += [f"{sha256_fichier(p)}  {rel}\n" for rel, p in sorted(fichiers.items())]
        with open(provisoire / nom_manifeste, "x", encoding="utf-8") as f:
            f.writelines(lignes)
        for dossier, _, noms in os.walk(provisoire):
            for nom in noms:
                os.chmod(pathlib.Path(dossier) / nom, 0o444)
        if mode_de(sortie) is not None:
            raise Refus(f"le dossier de sortie est apparu pendant l'assemblage ({sortie.name}) : rien n'est écrasé")
        os.rename(provisoire, sortie)
    except BaseException:
        shutil.rmtree(provisoire, ignore_errors=True)
        raise
    empreinte_manifeste = sha256_fichier(sortie / nom_manifeste)
    print(f"dossier de lecture assemblé : {sortie} ; {nom_manifeste} sha256 {empreinte_manifeste} ; "
          f"{len(fichiers)} fichiers ; mode {a.mode} ; version du script {a.version}")
    return 0


def principal(argv=None):
    try:
        return assembler(analyser(argv))
    except Usage as e:
        print(f"USAGE {PROG} : {e}", file=sys.stderr)
        return 2
    except Refus as e:
        print(f"REFUS {PROG} : {e}", file=sys.stderr)
        return 3
    except Exception as e:  # erreur interne : type et ligne seulement
        pile = traceback.extract_tb(e.__traceback__)
        ligne = pile[-1].lineno if pile else 0
        print(f"ERREUR INTERNE {PROG} : {type(e).__name__} (ligne {ligne})", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(principal())
