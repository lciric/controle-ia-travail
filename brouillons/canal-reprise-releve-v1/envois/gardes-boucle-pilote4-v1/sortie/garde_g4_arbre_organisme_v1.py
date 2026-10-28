#!/usr/bin/env python3
"""Garde G4 de la boucle extérieure du pilote 4 : l'arbre de l'organisme corrigé, avant toute relance — v1.

Protocole de la boucle extérieure v4, § 8 et § 11 (G4) ; § 14 (ce que le correcteur n'écrit jamais). Inspecte l'arbre
corrigé (`copie-organisme/`) contre l'arbre d'origine (`objet-origine/`, empreinte d'arbre attendue) : aucun nom
interdit, aucun fichier compilé ni lien, aucun marqueur (liste empreintée), aucune chaîne tirée de (A-test) ou de (B),
aucune copie d'une pièce de lecture, et, dans les lignes ajoutées (dont un `CORRECTIONS-v<N>.md` nouveau), aucun contenu
du § 14 détectable par motifs (fiche, fait ou nom de course, libellé du point 4 bis, test_final, verdict, registre…).
Rend l'empreinte d'arbre de l'arbre inspecté, que le lanceur épingle. N'ouvre jamais un fichier `test_final`. N'exécute
rien de l'objet. Bibliothèque standard seule ; `python3 -I`.

Codes de sortie : 0 accepté ; 2 usage ; 3 refusé (motif sur la sortie d'erreur, sans le contenu trouvé) ; 4 erreur
interne (type et ligne seulement).
"""

import argparse
import difflib
import hashlib
import json
import os
import pathlib
import re
import stat
import sys
import traceback
import unicodedata
from decimal import Decimal, InvalidOperation

GARDE = "G4"
RE_HEX64 = re.compile(r"[0-9a-f]{64}")
RE_COMPAGNON = re.compile(r"([0-9a-f]{64})  ([^/\\\n]+)\n?")
RE_COMPOSANT = re.compile(r"[A-Za-z0-9_][A-Za-z0-9._-]*")
RE_TEST_FINAL_NOM = re.compile(r"test[\s_-]*final", re.IGNORECASE)

NOMS_INTERDITS = [
    ("nom de test_final", r"test[\s_-]*final"),
    ("pièce provisoire", r"-provisoire-"),
    ("pièce de lecture ou de la boucle",
     r"(?:^|/)(?:lecture|lecture-finale|releve-mecanique|verdicts|contre-lecture|correction|perimetre"
     r"|ouverture-lecture|manifeste-dossier|journal-essais|liste-audit|registre-hypotheses|protocole-boucle"
     r"|carte-facteurs|zones-interdites|brief|points-boucle)[-_]"),
    ("fichier de course ou de banque",
     r"banque-confrontation|-cle\.json$|-secret\.json$|ferme\.tar|journal-appels|extrait-mecanique"
     r"|(?:^|/)lancement\.md$|reponse-question|(?:^|/)question\.md$|score-final|p3-consignes|textes-actions"
     r"|empreintes-pilote|a-pousser"),
    ("dossier interdit", r"(?:^|/)(?:donnees|runs|diag|pilotes)(?:/|$)"),
    ("nom de marqueur", r"marqueur"),
]
NOMS_INTERDITS = [(cat, re.compile(rx)) for cat, rx in NOMS_INTERDITS]

# Même liste que G5 (e) : contenu interdit du § 14 détectable par motifs, cherché dans les lignes ajoutées.
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

RE_NOMBRE = re.compile(r"(?<![\w.,])(?<!\w-)([-+−]?)(\d+(?:[.,]\d+)?)(?:[eE]([-+]?\d+))?(\s?%)?(?![^\W\d])")
RE_VALEUR_NUMERIQUE = re.compile(r"[-+−]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?%?")
RE_DATE_OU_HEX = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2})?Z?)?|\d{2}:\d{2}:\d{2}"
                            r"|(?<![0-9a-fA-F])(?=[0-9a-f]*[a-f])[0-9a-f]{7,}(?![0-9a-fA-F])")
RE_CLE_RELEVE = re.compile(r"([a-z0-9_.<>-]+) = (.*)")


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


def lister_arbre(racine, quoi):
    """Fichiers ordinaires d'un arbre ; refuse liens, fichiers spéciaux, fichiers compilés, noms hors norme."""
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
            if nom == "__pycache__" or nom.endswith(".pyc"):
                raise Refus(f"{quoi} : fichier compilé ou __pycache__ ({rel}) : à retirer avant l'inspection")
            if not RE_COMPOSANT.fullmatch(nom):
                raise Refus(f"{quoi} : nom hors norme {rel!r}")
            if nom in noms:
                if not stat.S_ISREG(mode):
                    raise Refus(f"{quoi} : fichier spécial {rel}")
                fichiers[rel] = p
    return fichiers


def texte_de(chemin, rel, quoi):
    try:
        return chemin.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"{quoi} : {rel} n'est pas un texte UTF-8 (impossible à inspecter)")


# ---------------------------------------------------------------------------------------------------------------------
# Nombres et marqueurs : la valeur exacte, sous toutes ses écritures (virgule ou point, pourcentage, exposant). Les
# arrondis sont cherchés par G8 dans les pièces de la boucle ; dans le code d'un organisme, un arrondi court coïncide trop
# souvent avec une constante du code pour qu'un motif en décide.


def decimal_de(signe, mantisse, exposant, pourcent):
    d = Decimal(("-" if signe in ("-", "−") else "") + mantisse.replace(",", "."))
    if exposant:
        d = d.scaleb(int(exposant))
    if pourcent:
        d = d.scaleb(-2)
    return d


def nombres(texte):
    """Nombres écrits dans un texte (virgule ou point décimal, exposant, pourcentage), hors dates, heures et empreintes."""
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
    """Le nombre écrit (jeton) égale la valeur (0,7317 = 0.7317 = 73,17 % = 7.317e-1)."""
    return jeton == valeur


def lire_marqueurs(chemin):
    """Une valeur par ligne (premier mot ; le reste de la ligne est un libellé, jamais affiché) ; # : commentaire."""
    valeurs = []
    for brut in chemin.read_text(encoding="utf-8").split("\n"):
        ligne = brut.strip()
        if not ligne or ligne.startswith("#"):
            continue
        jeton = ligne.split()[0]
        if RE_VALEUR_NUMERIQUE.fullmatch(jeton):
            m = RE_NOMBRE.fullmatch(jeton)
            if not m:
                raise Refus("liste des marqueurs : valeur numérique illisible")
            valeurs.append(("nombre", decimal_de(*m.groups())))
        else:
            if len(jeton) < 4:
                raise Refus("liste des marqueurs : marqueur textuel de moins de quatre caractères (peu distinctif)")
            valeurs.append(("texte", jeton))
    if not valeurs:
        raise Refus("liste des marqueurs vide")
    return valeurs


def chercher_marqueurs(texte, valeurs):
    """Rend l'indice (1…) du premier marqueur trouvé dans le texte, ou None."""
    jetons = [d for _, d in nombres(texte)]
    t = norm(texte)
    for i, (genre, v) in enumerate(valeurs, 1):
        if genre == "nombre":
            if any(correspond(j, v) for j in jetons):
                return i
        elif re.search(rf"(?<![\w]){re.escape(norm(v))}(?![\w])", t):
            return i
    return None


# ---------------------------------------------------------------------------------------------------------------------
# Chaînes tirées des pièces de lecture (A-test) et (B)


def jetons_de_piece(chemin):
    """(chaînes, nombres) distinctifs d'une pièce de lecture : clés et valeurs du relevé, chaînes et nombres du JSON,
    lignes longues et nombres du Markdown. Chaînes : au moins 16 caractères (64 pour une empreinte) ; nombres : au moins
    trois chiffres significatifs, ou un entier d'au moins quatre chiffres."""
    texte = chemin.read_bytes().decode("utf-8", errors="strict")
    chaines, valeurs = set(), set()

    def nombre(d):
        if (d == d.to_integral_value() and len(str(abs(int(d)))) >= 4) or \
                (d != d.to_integral_value() and chiffres_significatifs(d) >= 3):
            valeurs.add(d)

    lignes = texte.split("\n")
    if sum(1 for l in lignes if RE_CLE_RELEVE.fullmatch(l)) >= max(1, len([l for l in lignes if l.strip()]) // 2):
        for l in lignes:
            m = RE_CLE_RELEVE.fullmatch(l)
            if not m:
                continue
            cle, val = m.groups()
            if cle.count(".") >= 2:
                chaines.add(norm(cle))
            if RE_HEX64.fullmatch(val) or re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", val) or \
                    (re.fullmatch(r"[0-9a-f]{7,40}", val) and re.search(r"[a-f]", val) and re.search(r"\d", val)):
                chaines.add(val)
                continue
            for _, d in nombres(val):
                nombre(d)
    elif chemin.suffix == ".json":
        def parcourir(x):
            if isinstance(x, dict):
                for k, v in x.items():
                    parcourir(k)
                    parcourir(v)
            elif isinstance(x, list):
                for v in x:
                    parcourir(v)
            elif isinstance(x, str):
                if len(x) >= 16:
                    chaines.add(norm(x))
                for _, d in nombres(x):
                    nombre(d)
            elif isinstance(x, (int, float)) and not isinstance(x, bool):
                try:
                    nombre(Decimal(repr(x)))
                except InvalidOperation:
                    pass
        try:
            parcourir(json.loads(texte))
        except json.JSONDecodeError:
            raise Refus(f"pièce de lecture {chemin.name} : JSON illisible")
    else:
        for l in lignes:
            s = l.strip().strip("#|-* \t")
            if len(s) >= 40:
                chaines.add(norm(s))
            for _, d in nombres(l):
                nombre(d)
    return chaines, valeurs


# ---------------------------------------------------------------------------------------------------------------------


def lignes_ajoutees(ancien, nouveau):
    """Lignes du nouveau texte absentes de l'ancien à leur place : (numéro dans le nouveau, texte)."""
    a = ancien.split("\n") if ancien is not None else []
    b = nouveau.split("\n")
    if ancien is None:
        return list(enumerate(b, 1))
    res = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ("replace", "insert"):
            res.extend((j + 1, b[j]) for j in range(j1, j2))
    return res


def analyser(argv):
    p = Analyseur(prog="garde_g4_arbre_organisme_v1.py",
                  description="Garde G4 : l'arbre de l'organisme corrigé, inspecté avant toute relance.")
    p.add_argument("--arbre", required=True, type=pathlib.Path, help="l'arbre corrigé (copie-organisme/)")
    p.add_argument("--origine", required=True, type=pathlib.Path, help="l'arbre au commit précédent (objet-origine/)")
    p.add_argument("--arbre-origine", required=True, help="empreinte d'arbre attendue de l'origine")
    p.add_argument("--marqueurs", type=pathlib.Path, help="liste empreintée des marqueurs (une valeur par ligne)")
    p.add_argument("--empreinte-marqueurs", help="empreinte attendue de la liste des marqueurs")
    p.add_argument("--piece-lecture", action="append", default=[], type=pathlib.Path,
                   help="(A-test) ou (B) de la course ; jamais un fichier test_final")
    a = p.parse_args(argv)
    for nom in ("arbre_origine", "empreinte_marqueurs"):
        v = getattr(a, nom)
        if v is not None and not RE_HEX64.fullmatch(v):
            raise Usage(f"--{nom.replace('_', '-')} : 64 caractères hexadécimaux en minuscules attendus")
    if a.empreinte_marqueurs and not a.marqueurs:
        raise Usage("--empreinte-marqueurs sans --marqueurs")
    for piece in a.piece_lecture:
        if RE_TEST_FINAL_NOM.search(piece.name):
            raise Usage(f"--piece-lecture {piece.name} : fichier test_final, jamais ouvert par G4")
    return a


def executer(a):
    origine = lister_arbre(a.origine, "arbre d'origine")
    if empreinte_arbre(a.origine) != a.arbre_origine:
        raise Refus("arbre d'origine : empreinte d'arbre différente de celle qui est attendue")
    arbre = lister_arbre(a.arbre, "arbre corrigé")
    for rel in arbre:
        r = norm(rel)
        for categorie, rx in NOMS_INTERDITS:
            if rx.search(r):
                raise Refus(f"nom interdit dans l'arbre ({categorie}) : {rel}")
    empreintes_arbre = {}
    for rel, p in arbre.items():
        empreintes_arbre.setdefault(sha256_fichier(p), rel)
    empreintes_pieces = {}
    for piece in a.piece_lecture:
        empreintes_pieces[piece] = verifier_compagnon(piece, f"pièce de lecture {piece.name}")
        if empreintes_pieces[piece] in empreintes_arbre:
            raise Refus(f"{empreintes_arbre[empreintes_pieces[piece]]} : copie d'une pièce de lecture ({piece.name})")
    textes = {rel: texte_de(p, rel, "arbre corrigé") for rel, p in arbre.items()}
    ajoutees = {}
    for rel, texte in textes.items():
        ancien = texte_de(origine[rel], rel, "arbre d'origine") if rel in origine else None
        if ancien != texte:
            ajoutees[rel] = lignes_ajoutees(ancien, texte)
    nb_lignes = sum(len(v) for v in ajoutees.values())
    for rel, lignes in ajoutees.items():
        for n, texte in lignes:
            t = norm(texte)
            for categorie, brut, rx in MOTIFS_INTERDITS:
                if rx.search(texte if brut else t):
                    raise Refus(f"{rel}, ligne {n} : contenu interdit du § 14 ({categorie})")
    nb_marqueurs = 0
    if a.marqueurs:
        empreinte = verifier_compagnon(a.marqueurs, "liste des marqueurs")
        if a.empreinte_marqueurs and empreinte != a.empreinte_marqueurs:
            raise Refus("liste des marqueurs : empreinte différente de celle qui est attendue")
        valeurs = lire_marqueurs(a.marqueurs)
        nb_marqueurs = len(valeurs)
        for rel, p in origine.items():
            i = chercher_marqueurs(texte_de(p, rel, "arbre d'origine"), valeurs)
            if i is not None:
                raise Refus(f"marqueur n° {i} de la liste déjà présent dans l'arbre d'origine ({rel}) : marqueur mal "
                            f"choisi, la garde ne peut pas le distinguer")
        for rel, lignes in ajoutees.items():
            for n, texte in lignes:
                i = chercher_marqueurs(texte, valeurs)
                if i is not None:
                    raise Refus(f"{rel}, ligne {n} : porte le marqueur n° {i} de la liste")
    for piece in a.piece_lecture:
        chaines, valeurs = jetons_de_piece(piece)
        for rel, lignes in ajoutees.items():
            for n, texte in lignes:
                t = norm(texte)
                if any(c in t for c in chaines) or \
                        any(correspond(j, v) for _, j in nombres(texte) for v in valeurs):
                    raise Refus(f"{rel}, ligne {n} : porte une chaîne ou une valeur tirée de la pièce de lecture "
                                f"{piece.name}")
    print(f"G4 : arbre accepté — {len(arbre)} fichiers, empreinte d'arbre {empreinte_arbre(a.arbre)} (à épingler par "
          f"le lanceur) ; lignes ajoutées inspectées : {nb_lignes} ; marqueurs : {nb_marqueurs} ; pièces de lecture : "
          f"{len(a.piece_lecture)}")
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
