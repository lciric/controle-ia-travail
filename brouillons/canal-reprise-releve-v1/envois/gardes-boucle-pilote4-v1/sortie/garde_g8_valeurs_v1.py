#!/usr/bin/env python3
"""Garde G8 de la boucle extérieure du pilote 4 : aucune valeur de `test_final` recopiée dans une pièce — v1.

Protocole de la boucle extérieure v4, § 5 et § 11 (G8). Cherche, dans des pièces de la boucle (verdicts, parties A et
B, pièces de périmètre et de correction, lecture finale, entrées du journal), les valeurs d'une liste donnée en
argument : les marqueurs d'un dossier d'audit (liste empreintée que les agents ne voient pas), ou, à la fin du compteur
seulement, les valeurs finales. La garde ne lit jamais un fichier `test_final` : elle refuse d'en ouvrir un comme pièce,
et ne tire aucune valeur d'un tel fichier. Une valeur se reconnaît écrite telle quelle, avec une virgule décimale, en
pourcentage, en notation exponentielle, ou arrondie à la précision du nombre écrit (au moins deux chiffres
significatifs). La sortie ne cite jamais une valeur : seulement son rang dans la liste et l'endroit trouvé.
Bibliothèque standard seule ; `python3 -I`.

Codes de sortie : 0 aucune valeur trouvée ; 2 usage ; 3 refusé (une valeur trouvée, ou liste ou pièce invalide) ;
4 erreur interne (type et ligne seulement).
"""

import argparse
import hashlib
import os
import pathlib
import re
import stat
import sys
import traceback
import unicodedata
from decimal import Decimal, InvalidOperation, ROUND_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP

GARDE = "G8"
RE_HEX64 = re.compile(r"[0-9a-f]{64}")
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
RE_TEST_FINAL_NOM = re.compile(r"test[\s_-]*final", re.IGNORECASE)
RE_NOMBRE = re.compile(r"(?<![\w.,])(?<!\w-)([-+−]?)(\d+(?:[.,]\d+)?)(?:[eE]([-+]?\d+))?(\s?%)?(?![^\W\d])")
RE_VALEUR_NUMERIQUE = re.compile(r"[-+−]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?%?")
RE_DATE_OU_HEX = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?Z?)?|\d{2}:\d{2}:\d{2}"
                            r"|(?<![0-9a-fA-F])(?=[0-9a-f]*[a-f])[0-9a-f]{7,}(?![0-9a-fA-F])")
MAX_CITES = 20


class Refus(Exception):
    """Refus de la garde : code 3."""


class Usage(Exception):
    """Erreur d'usage : code 2."""


class Analyseur(argparse.ArgumentParser):
    def error(self, message):
        raise Usage(message)


def norm(texte):
    t = unicodedata.normalize("NFD", texte)
    t = unicodedata.normalize("NFC", "".join(c for c in t if unicodedata.category(c) != "Mn")).casefold()
    return t.replace("’", "'")


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


def decimal_de(signe, mantisse, exposant, pourcent):
    d = Decimal(("-" if signe in ("-", "−") else "") + mantisse.replace(",", "."))
    if exposant:
        d = d.scaleb(int(exposant))
    if pourcent:
        d = d.scaleb(-2)
    return d


def nombres(texte):
    """(position, nombre) des nombres écrits dans un texte, hors dates, heures, empreintes et identifiants (HC-P4-11,
    g003, v3, t-0001 : un nombre collé à une lettre ou à « lettre- » n'est pas lu)."""
    texte = RE_DATE_OU_HEX.sub(lambda m: " " * len(m.group(0)), texte)
    for m in RE_NOMBRE.finditer(texte):
        try:
            yield m.start(), decimal_de(*m.groups())
        except InvalidOperation:
            continue


def chiffres_significatifs(d):
    chiffres = "".join(map(str, d.as_tuple().digits)).lstrip("0")
    return len(chiffres) if chiffres else 1


def correspond(jeton, valeur):
    if jeton == valeur:
        return True
    if chiffres_significatifs(jeton) < 2:
        return False
    e_jeton = jeton.as_tuple().exponent
    if not isinstance(e_jeton, int) or e_jeton <= valeur.as_tuple().exponent:
        return False
    quantum = Decimal((0, (1,), e_jeton))
    for mode in (ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN):
        try:
            if valeur.quantize(quantum, rounding=mode) == jeton:
                return True
        except InvalidOperation:
            return False
    return False


def lire_valeurs(chemin):
    """Une valeur par ligne : le premier mot ; le reste de la ligne est un libellé (catégorie, cellule), jamais affiché.
    Lignes vides et lignes commençant par # ignorées."""
    valeurs = []
    try:
        lignes = chemin.read_bytes().decode("utf-8").split("\n")
    except UnicodeDecodeError:
        raise Refus("liste des valeurs : pas un texte UTF-8")
    for brut in lignes:
        ligne = brut.strip()
        if not ligne or ligne.startswith("#"):
            continue
        jeton = ligne.split()[0]
        if RE_VALEUR_NUMERIQUE.fullmatch(jeton):
            m = RE_NOMBRE.fullmatch(jeton)
            if not m:
                raise Refus("liste des valeurs : valeur numérique illisible")
            d = decimal_de(*m.groups())
            entier = d == d.to_integral_value() and "." not in jeton and "," not in jeton
            faible = (entier and len(str(abs(int(d)))) < 3) or (not entier and chiffres_significatifs(d) < 2)
            valeurs.append(("nombre", d, faible))
        else:
            if len(jeton) < 4:
                raise Refus("liste des valeurs : valeur textuelle de moins de quatre caractères (peu distinctive)")
            valeurs.append(("texte", jeton, False))
    if not valeurs:
        raise Refus("liste des valeurs vide : la garde ne vérifierait rien")
    return valeurs


def analyser(argv):
    p = Analyseur(prog="garde_g8_valeurs_v1.py",
                  description="Garde G8 : aucune valeur de la liste (marqueurs, ou valeurs finales à la fin du "
                              "compteur) dans les pièces.")
    p.add_argument("--valeurs", required=True, type=pathlib.Path,
                   help="liste des valeurs (une par ligne), avec son compagnon .sha256")
    p.add_argument("--empreinte-valeurs", help="empreinte attendue de la liste (consignée par conv-audit)")
    p.add_argument("--piece", required=True, action="append", type=pathlib.Path,
                   help="pièce à contrôler (répétable), avec son compagnon .sha256 ; jamais un fichier test_final")
    a = p.parse_args(argv)
    if a.empreinte_valeurs is not None and not RE_HEX64.fullmatch(a.empreinte_valeurs):
        raise Usage("--empreinte-valeurs : 64 caractères hexadécimaux en minuscules attendus")
    for piece in a.piece:
        if RE_TEST_FINAL_NOM.search(piece.name):
            raise Usage(f"--piece {piece.name} : fichier test_final, jamais ouvert par G8")
    return a


def executer(a):
    empreinte = verifier_compagnon(a.valeurs, "liste des valeurs")
    if a.empreinte_valeurs and empreinte != a.empreinte_valeurs:
        raise Refus("liste des valeurs : empreinte différente de celle qui est attendue")
    valeurs = lire_valeurs(a.valeurs)
    trouvees = []
    for piece in a.piece:
        verifier_compagnon(piece, f"pièce {piece.name}")
        try:
            texte = piece.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            raise Refus(f"pièce {piece.name} : pas un texte UTF-8")
        for n, ligne in enumerate(unicodedata.normalize("NFC", texte).split("\n"), 1):
            jetons = list(nombres(ligne))
            t = norm(ligne)
            for i, (genre, v, faible) in enumerate(valeurs, 1):
                if genre == "nombre":
                    for pos, j in jetons:
                        if correspond(j, v):
                            trouvees.append((piece.name, n, pos + 1, i, faible))
                else:
                    for m in re.finditer(rf"(?<![\w]){re.escape(norm(v))}(?![\w])", t):
                        trouvees.append((piece.name, n, m.start() + 1, i, False))
    if trouvees:
        lignes = []
        for nom, n, col, i, faible in trouvees[:MAX_CITES]:
            note = " (valeur peu distinctive : un nombre court peut être une coïncidence ; trancher par lecture)" \
                if faible else ""
            lignes.append(f"  valeur n° {i} de la liste : {nom}, ligne {n}, colonne {col}{note}")
        reste = f"\n  … et {len(trouvees) - MAX_CITES} autres" if len(trouvees) > MAX_CITES else ""
        raise Refus(f"{len(trouvees)} occurrence(s) d'une valeur de la liste dans les pièces :\n" + "\n".join(lignes)
                    + reste)
    print(f"G8 : aucune valeur de la liste dans les pièces ({len(a.piece)} pièce(s), {len(valeurs)} valeur(s) ; liste "
          f"sha256 {empreinte})")
    return 0


def principal(argv=None):
    try:
        return executer(analyser(argv))
    except Usage as e:
        print(f"USAGE {GARDE} : {e}", file=sys.stderr)
        return 2
    except Refus as e:
        print(f"REFUS {GARDE} : {e}", file=sys.stderr)
        return 3
    except Exception as e:  # erreur interne : type et ligne seulement
        pile = traceback.extract_tb(e.__traceback__)
        ligne = pile[-1].lineno if pile else 0
        print(f"ERREUR INTERNE {GARDE} : {type(e).__name__} (ligne {ligne})", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(principal())
