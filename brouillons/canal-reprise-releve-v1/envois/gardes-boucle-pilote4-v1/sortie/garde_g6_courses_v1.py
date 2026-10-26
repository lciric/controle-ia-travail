#!/usr/bin/env python3
"""Garde G6 de la boucle extérieure du pilote 4 : aucune mise en regard des deux courses — v1.

Protocole de la boucle extérieure v4, § 4, § 5 et § 11 (G6) ; décision E7 (d) : les noms se cherchent en mots entiers.
Une pièce (verdicts, parties A et B, périmètre, correction) ne porte que les noms de sa course. La garde cherche les noms
de l'autre course (nom de course, nom de dossier, lignée, clé : donnés en arguments) ; une occurrence n'est comptée que si
elle n'est ni précédée ni suivie d'une lettre, d'un chiffre, de `-` ou de `_` (ainsi `gemini-organisme-v6-2` n'est pas
trouvé dans `gemini-organisme-v6-2-s`, ni la clé `v6-2` dans `v6-2-s`). Seule exception : la ligne « condition de
préséance » d'une pièce de correction motivée par S (option `--autoriser-preseance`), une seule, sans fiche ni verdict.
Refuse aussi une différence écrite « M − S » ou « S − M ». La phrase qui met les courses en regard sans les nommer reste
au contre-lecteur. Bibliothèque standard seule ; `python3 -I`.

Codes de sortie : 0 accepté ; 2 usage ; 3 refusé ; 4 erreur interne (type et ligne seulement).
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

GARDE = "G6"
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
RE_DIFFERENCE = re.compile(r"(?<![\w-])(?:M\s*[−–-]\s*S|S\s*[−–-]\s*M)(?![\w-])")
RE_FICHE = re.compile(r"hc-p4-?\d*")
RE_VERDICT = re.compile(r"(?<![a-z])(?:tenues?|eliminees?|indecidables?|non rejetees?|rejetees?|non observables?"
                        r"|desaccords?|au-dela du bruit|dans le bruit|transmissibles?|plateau)(?![a-z])")


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
    for a, b in (("’", "'"), ("–", "-"), ("—", "-"), ("−", "-")):
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
    if sha256_fichier(chemin) != m.group(1):
        raise Refus(f"compagnon de {quoi} : empreinte différente de celle du fichier")


def motif_mot_entier(nom):
    """Un nom, ni précédé ni suivi d'une lettre, d'un chiffre, de « - » ou de « _ » (casse ignorée)."""
    return re.compile(rf"(?<![\w-]){re.escape(nom)}(?![\w-])", re.IGNORECASE)


def analyser(argv):
    p = Analyseur(prog="garde_g6_courses_v1.py",
                  description="Garde G6 : une pièce ne porte que les noms de sa course.")
    p.add_argument("--piece", required=True, action="append", type=pathlib.Path,
                   help="pièce à contrôler (répétable), avec son compagnon .sha256")
    p.add_argument("--autre", required=True, action="append",
                   help="un nom de l'autre course (répétable) : nom de course, nom de dossier, lignée, clé")
    p.add_argument("--autoriser-preseance", action="store_true",
                   help="pièce de correction motivée par S : une ligne « condition de préséance » peut nommer M")
    a = p.parse_args(argv)
    for nom in a.autre:
        if len(nom.strip()) < 2 or nom != nom.strip():
            raise Usage(f"--autre {nom!r} : nom vide, trop court ou entouré d'espaces")
    return a


def executer(a):
    motifs = [(nom, motif_mot_entier(nom)) for nom in a.autre]
    for piece in a.piece:
        verifier_compagnon(piece, f"pièce {piece.name}")
        try:
            texte = unicodedata.normalize("NFC", piece.read_bytes().decode("utf-8"))
        except UnicodeDecodeError:
            raise Refus(f"pièce {piece.name} : pas un texte UTF-8")
        lignes = texte.split("\n")
        preseance = [n for n, l in enumerate(lignes, 1) if "condition de preseance" in norm(l)]
        if a.autoriser_preseance:
            if len(preseance) > 1:
                raise Refus(f"{piece.name} : {len(preseance)} lignes « condition de préséance » (une seule permise)")
            for n in preseance:
                t = norm(lignes[n - 1])
                if RE_FICHE.search(t):
                    raise Refus(f"{piece.name}, ligne {n} : la ligne « condition de préséance » porte une fiche")
                if RE_VERDICT.search(t):
                    raise Refus(f"{piece.name}, ligne {n} : la ligne « condition de préséance » porte un verdict")
        for n, ligne in enumerate(lignes, 1):
            if RE_DIFFERENCE.search(ligne):
                raise Refus(f"{piece.name}, ligne {n} : différence entre les deux courses (« M − S »)")
            for nom, motif in motifs:
                if motif.search(ligne):
                    if a.autoriser_preseance and n in preseance:
                        continue
                    raise Refus(f"{piece.name}, ligne {n} : porte le nom « {nom} » de l'autre course (mot entier), "
                                f"hors de la ligne « condition de préséance »")
    print(f"G6 : {len(a.piece)} pièce(s) acceptée(s) — aucun nom de l'autre course hors de la ligne « condition de "
          f"préséance » ({len(a.autre)} nom(s) cherché(s) en mots entiers)")
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
