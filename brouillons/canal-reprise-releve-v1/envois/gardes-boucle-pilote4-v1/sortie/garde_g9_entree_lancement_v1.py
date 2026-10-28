#!/usr/bin/env python3
"""Garde G9 de la boucle extérieure du pilote 4 : entrée de lancement avec une attente chiffrée — v1.

Protocole de la boucle extérieure v4, § 5 (entrée de lancement, avant chaque relance) et § 11 (G9). L'entrée doit porter
une ligne « attente chiffrée : » dont chaque élément nomme une fiche visée par la correction (par défaut HC-P4-01, 03, 07,
08 ou 09 : celles dont une branche propose une correction), l'observation mécanique attendue et son nombre (un entier,
après un comparateur : ≥, ≤, =, >, <, « au moins », « au plus », « exactement ») ; et, pour `test_final`, la phrase
« aucune attente au-delà des nulles HC-P4-11 et 12 ». Refusée : une entrée sans attente, un élément sans nombre, une
attente qui est un score (mot de score, nombre décimal sans unité, fiche HC-P4-11 ou 12, libellé du point 4 bis).
Lit une entrée isolée (`--entree`) ou l'entrée n° N d'un journal (`--journal`, `--numero`). Bibliothèque standard seule ;
`python3 -I`.

Codes de sortie : 0 accepté (relance permise par G9) ; 2 usage ; 3 refusé (relance refusée) ; 4 erreur interne.
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

GARDE = "G9"
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
PHRASE_TEST_FINAL = "aucune attente au-dela des nulles hc-p4-11 et 12"
RE_FICHE = re.compile(r"hc-p4-(\d{2})(?!\d)")
RE_COMPARAISON = re.compile(r"(?:>=|<=|≥|≤|=|>|<|\bau moins\b|\bau plus\b|\bexactement\b|\begale? a\b)\s*"
                            r"(\d+(?:[.,]\d+)?)(?![\d]|[.,]\d)")
RE_DECIMAL_SANS_UNITE = re.compile(r"(?<![\w.])\d+[.,]\d+(?![.\d])(?!\s*(?:usd|s|octets)\b)")
RE_SCORE = re.compile(r"(?<![a-z])(?:scores?|exactitudes?|precisions?|accuracy|rappels?|recall|proportions?|taux|f1"
                      r"|auc|valeurs? p|p-value|test[\s_-]*final|au-dela du bruit|dans le bruit|non distinct"
                      r"|au-dessus de la reference)(?![a-z])")


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
    for a, b in (("’", "'"), ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " "), ("«", " "),
                 ("»", " "), ("\"", " "), ("`", " "), ("*", " ")):
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


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


def extraire_entree(texte, numero):
    """L'entrée « Entrée <numero> » d'un journal : de son titre au titre suivant de même niveau ou plus haut."""
    lignes = texte.split("\n")
    debut, niveau = None, None
    for i, l in enumerate(lignes):
        m = re.match(r"(#{1,6})\s*entree\s+(\d+)\b", norm(l))
        if m and int(m.group(2)) == numero:
            if debut is not None:
                raise Refus(f"journal : deux entrées n° {numero}")
            debut, niveau = i, len(m.group(1))
    if debut is None:
        raise Refus(f"journal : aucune entrée n° {numero}")
    fin = len(lignes)
    for j in range(debut + 1, len(lignes)):
        m = re.match(r"(#{1,6})\s", lignes[j])
        if m and len(m.group(1)) <= niveau:
            fin = j
            break
    return "\n".join(lignes[debut:fin])


def elements_attente(lignes):
    """Les éléments de la ligne « attente chiffrée : » (séparés par « ; ») et de ses sous-éléments en retrait."""
    elements = []
    for i, brut in enumerate(lignes):
        retrait = len(brut) - len(brut.lstrip())
        ligne = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", brut.strip())
        n = norm(ligne).strip()
        if not re.match(r"attentes? chiffrees?\s*:", n):
            continue
        reste = ligne.split(":", 1)[1]
        elements.extend(x.strip() for x in reste.split(";") if x.strip())
        for suite in lignes[i + 1:]:
            if not suite.strip():
                break
            r = len(suite) - len(suite.lstrip())
            if r <= retrait:
                break
            sous = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", suite.strip())
            elements.extend(x.strip() for x in sous.split(";") if x.strip())
    return elements


def analyser(argv):
    p = Analyseur(prog="garde_g9_entree_lancement_v1.py",
                  description="Garde G9 : une entrée de lancement porte une attente chiffrée, jamais un score.")
    p.add_argument("--entree", type=pathlib.Path, help="fichier de l'entrée de lancement (avec compagnon .sha256)")
    p.add_argument("--journal", type=pathlib.Path, help="journal des essais (avec compagnon .sha256)")
    p.add_argument("--numero", type=int, help="numéro de l'entrée de lancement dans le journal")
    p.add_argument("--fiches-motivantes", default="01,03,07,08,09",
                   help="fiches dont une branche propose une correction (défaut : 01,03,07,08,09)")
    a = p.parse_args(argv)
    if (a.entree is None) == (a.journal is None):
        raise Usage("donner --entree, ou --journal avec --numero")
    if a.journal is not None and a.numero is None:
        raise Usage("--journal demande --numero")
    if a.entree is not None and a.numero is not None:
        raise Usage("--numero va avec --journal")
    a.fiches = {f.strip() for f in a.fiches_motivantes.split(",")}
    if not a.fiches or not all(re.fullmatch(r"\d{2}", f) for f in a.fiches):
        raise Usage("--fiches-motivantes : numéros à deux chiffres séparés par des virgules")
    return a


def executer(a):
    source = a.entree or a.journal
    verifier_compagnon(source, "entrée" if a.entree else "journal")
    try:
        texte = unicodedata.normalize("NFC", source.read_bytes().decode("utf-8"))
    except UnicodeDecodeError:
        raise Refus("pas un texte UTF-8")
    if a.journal is not None:
        texte = extraire_entree(texte, a.numero)
    lignes = texte.split("\n")
    titres = [norm(l) for l in lignes if l.lstrip().startswith("#")]
    if not any("entree" in t and "lancement" in t for t in titres):
        raise Refus("pas une entrée de lancement (aucun titre « Entrée … lancement … »)")
    if not any(PHRASE_TEST_FINAL in norm(l) for l in lignes):
        raise Refus("aucune ligne « test_final : aucune attente au-delà des nulles HC-P4-11 et 12 »")
    elements = elements_attente(lignes)
    if not elements:
        raise Refus("entrée sans attente chiffrée (ligne « attente chiffrée : » absente ou vide) : relance refusée")
    attentes = []
    for k, element in enumerate(elements, 1):
        n = norm(element)
        if PHRASE_TEST_FINAL in n:
            continue
        fiches = set(RE_FICHE.findall(n))
        if not fiches:
            raise Refus(f"attente n° {k} : aucune fiche nommée (forme « HC-P4-03 : observation, nombre attendu ≥ 1 »)")
        if fiches & {"11", "12"}:
            raise Refus(f"attente n° {k} : fiche HC-P4-11 ou 12 (lue sur test_final) : une attente sur un score est "
                        f"refusée")
        hors = sorted(fiches - a.fiches)
        if hors:
            raise Refus(f"attente n° {k} : fiche HC-P4-{', HC-P4-'.join(hors)}, dont aucune branche ne propose de "
                        f"correction")
        if RE_SCORE.search(n):
            raise Refus(f"attente n° {k} : l'attente est un score (mot de score ou libellé) : relance refusée")
        if RE_DECIMAL_SANS_UNITE.search(n):
            raise Refus(f"attente n° {k} : nombre décimal sans unité (forme d'un score) : relance refusée")
        nombres = RE_COMPARAISON.findall(n)
        if not nombres:
            raise Refus(f"attente n° {k} : aucun nombre attendu (comparateur suivi d'un entier) : relance refusée")
        attentes.append(f"HC-P4-{'/'.join(sorted(fiches))}")
    if not attentes:
        raise Refus("entrée sans attente chiffrée sur une fiche visée : relance refusée")
    print(f"G9 : entrée de lancement acceptée — {len(attentes)} attente(s) chiffrée(s) ({', '.join(attentes)}) ; "
          f"test_final : aucune attente au-delà des nulles")
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
