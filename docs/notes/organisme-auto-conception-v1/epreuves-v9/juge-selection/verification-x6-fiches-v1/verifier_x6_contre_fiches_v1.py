"""Vérification X6 contre le fichier des cartes de la course v9 — v1.

Bibliothèque standard seulement. Écrit, dans --sortie, un JSON à trois champs :
nombre_de_cles, retenues_presentes, empreintes ; puis son compagnon .sha256.
À l'écran : « FAIT » ou le motif d'un refus, jamais un identifiant.

Commande unique de jeu :
    python3 -B verifier_x6_contre_fiches_v1.py --fiches F --extraction E --sortie S

Développeur, modèle L′.
"""

import argparse
import hashlib
import json
import os
import sys

# Empreintes attendues, gelées. Le point d'entrée n'accepte que celles-ci.
EMPREINTE_FICHES = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
EMPREINTE_EXTRACTION = "f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb"

CHAMPS_SORTIE = ("nombre_de_cles", "retenues_presentes", "empreintes")


class Refus(Exception):
    """Refus ; le motif ne contient jamais un identifiant ni une valeur lue."""


class _Cles(tuple):
    """Clés d'un objet JSON, valeurs jetées dès le décodage."""


def _seulement_les_cles(paires):
    # Les valeurs sont abandonnées ici : elles ne sont ni gardées ni copiées.
    return _Cles(cle for cle, _valeur in paires)


def _lire_octets(chemin, nom):
    try:
        with open(chemin, "rb") as f:
            return f.read()
    except OSError:
        raise Refus(f"lecture impossible du fichier {nom}") from None


def _cles_des_fiches(octets):
    try:
        texte = octets.decode("utf-8")
        objet = json.loads(texte, object_pairs_hook=_seulement_les_cles)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Refus("fiches : JSON illisible") from None
    if not isinstance(objet, _Cles):
        raise Refus("fiches : la racine n'est pas un objet JSON")
    cles = tuple(objet)
    if len(set(cles)) != len(cles):
        raise Refus("fiches : clé en double")
    return frozenset(cles), len(cles)


def _retenues_de_l_extraction(octets):
    try:
        objet = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Refus("extraction : JSON illisible") from None
    if not isinstance(objet, dict):
        raise Refus("extraction : la racine n'est pas un objet JSON")
    classes = objet.get("identifiants_par_classe")
    if not isinstance(classes, dict):
        raise Refus("extraction : identifiants_par_classe absent ou mal formé")
    liste = classes.get("a_corriger")
    if not isinstance(liste, list):
        raise Refus("extraction : a_corriger absent ou mal formé")
    if len(liste) != 2:
        raise Refus("extraction : a_corriger ne compte pas exactement deux identifiants")
    if not all(isinstance(x, str) for x in liste):
        raise Refus("extraction : a_corriger contient autre chose que des chaînes")
    if liste[0] == liste[1]:
        raise Refus("extraction : les deux identifiants de a_corriger sont égaux")
    return list(liste)


def executer(chemin_fiches, chemin_extraction, chemin_sortie,
             empreinte_fiches, empreinte_extraction):
    """Cœur du programme ; les empreintes attendues sont passées en paramètre.

    Le point d'entrée en ligne de commande passe toujours les constantes gelées.
    """
    chemin_compagnon = chemin_sortie + ".sha256"
    if os.path.lexists(chemin_sortie):
        raise Refus("le fichier de sortie existe déjà")
    if os.path.lexists(chemin_compagnon):
        raise Refus("le compagnon du fichier de sortie existe déjà")

    # Empreintes calculées sur les octets lus, avant tout décodage ;
    # le décodage porte sur ces mêmes octets.
    octets_fiches = _lire_octets(chemin_fiches, "fiches")
    octets_extraction = _lire_octets(chemin_extraction, "extraction")
    calc_fiches = hashlib.sha256(octets_fiches).hexdigest()
    calc_extraction = hashlib.sha256(octets_extraction).hexdigest()
    if calc_fiches != empreinte_fiches:
        raise Refus("empreinte du fichier fiches différente de l'attendue")
    if calc_extraction != empreinte_extraction:
        raise Refus("empreinte du fichier extraction différente de l'attendue")

    cles, nombre = _cles_des_fiches(octets_fiches)
    del octets_fiches
    retenues = _retenues_de_l_extraction(octets_extraction)
    del octets_extraction

    sortie = {
        "nombre_de_cles": nombre,
        "retenues_presentes": [r in cles for r in retenues],
        "empreintes": {"fiches": calc_fiches, "extraction": calc_extraction},
    }
    del retenues, cles
    if tuple(sortie) != CHAMPS_SORTIE or set(sortie["empreintes"]) != {"fiches", "extraction"}:
        raise Refus("sortie mal formée")

    contenu = (json.dumps(sortie, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    try:
        with open(chemin_sortie, "xb") as f:
            f.write(contenu)
        ligne = f"{hashlib.sha256(contenu).hexdigest()}  {os.path.basename(chemin_sortie)}\n"
        with open(chemin_compagnon, "xb") as f:
            f.write(ligne.encode("utf-8"))
    except FileExistsError:
        raise Refus("le fichier de sortie ou son compagnon existe déjà") from None
    except OSError:
        raise Refus("écriture impossible de la sortie") from None


class _Analyseur(argparse.ArgumentParser):
    def error(self, message):  # motif sans écho des arguments
        print("REFUS : arguments invalides", file=sys.stderr)
        raise SystemExit(2)


def principal(argv=None):
    analyseur = _Analyseur(add_help=False, allow_abbrev=False)
    analyseur.add_argument("--fiches", required=True)
    analyseur.add_argument("--extraction", required=True)
    analyseur.add_argument("--sortie", required=True)
    args = analyseur.parse_args(argv)
    try:
        executer(args.fiches, args.extraction, args.sortie,
                 EMPREINTE_FICHES, EMPREINTE_EXTRACTION)
    except Refus as refus:
        print(f"REFUS : {refus}", file=sys.stderr)
        return 1
    except Exception:
        print("REFUS : erreur inattendue", file=sys.stderr)
        return 1
    print("FAIT")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
