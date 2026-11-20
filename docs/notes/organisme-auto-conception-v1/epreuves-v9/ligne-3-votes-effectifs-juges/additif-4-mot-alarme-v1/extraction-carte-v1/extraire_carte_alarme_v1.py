#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extraction de la seule carte de l'alarme, champ `meta` retiré — v1.

Écrit par le développeur, modèle O, sur le mandat
`mandat-developpeur-extraction-carte-alarme-v1.md` (empreinte 53bf2bd7…).

Ce que fait le programme, et rien de plus :
- il lit les octets du fichier des cartes et en calcule l'empreinte AVANT tout décodage ; il refuse
  si elle diffère de l'empreinte gelée (rien n'est alors décodé) ;
- il décode le fichier selon la structure que lit le masque scellé `masque_style_cartes_v1.py`
  (07ed8725…) : un objet de premier niveau {identifiant: enregistrement}, l'identifiant étant la clé,
  l'enregistrement un objet qui porte `contenu`, et `meta` comme clé de l'enregistrement ;
- il refuse si le nombre de cartes diffère du nombre gelé, si l'identifiant gelé est absent ou présent
  plus d'une fois, ou si une autre clé de premier niveau est en double ;
- il ne garde, après décodage, que l'enregistrement de cet identifiant ; la clé `meta` en est retirée
  avant tout usage (sa valeur n'est jamais convertie ni lue) ;
- il écrit dans `--sortie` un JSON à trois champs (`carte`, `empreinte_fiches`, `identifiant`), puis
  son compagnon `.sha256` ; à l'écran : « FAIT », ou « REFUS : » suivi d'un motif sans valeur.

Il n'écrit, n'affiche ni ne journalise rien d'une autre carte, aucun autre identifiant, rien de `meta`.
Toute erreur imprévue est rendue par son seul type (code 3), jamais par son message ni sa trace.
Tout refus rend le code 2 et n'écrit rien. Aucun repli silencieux (règle R5).
Bibliothèque standard seulement ; aucun tirage au sort ; aucun chemin par défaut.
"""
import argparse
import hashlib
import json
import os
import sys

VERSION = "extraire_carte_alarme_v1"

# Constantes gelées par le mandat ; le point d'entrée en ligne de commande n'accepte qu'elles.
EMPREINTE_FICHES = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
IDENTIFIANT_CARTE = "fcbf4a2dd1a57"
NOMBRE_CARTES = 94

DEPOT = "/home/user/controle-ia-travail"
DOSSIER_INTERDIT = "archives-reponses-modeles"
CHAMP_RETIRE = "meta"
CHAMP_ATTENDU = "contenu"       # le masque scellé n'accède qu'à rec["contenu"] : la structure doit le porter


class Refus(Exception):
    """Refus explicite : motif sans valeur ni texte de carte ; code 2 ; rien n'est écrit."""


class _Paires(list):
    """Objet JSON gardé comme suite de paires, pour que les clés en double restent visibles."""


def _crochet_paires(paires):
    return _Paires(paires)


def _sous(chemin, racine):
    racine = racine.rstrip(os.sep)
    return chemin == racine or chemin.startswith(racine + os.sep)


def valider_parametres(empreinte_attendue, identifiant, nombre_cartes):
    if not (isinstance(empreinte_attendue, str) and len(empreinte_attendue) == 64
            and all(c in "0123456789abcdef" for c in empreinte_attendue)):
        raise Refus("paramètres : empreinte gelée illisible (64 caractères hexadécimaux minuscules attendus)")
    if not (isinstance(identifiant, str) and identifiant):
        raise Refus("paramètres : identifiant gelé vide ou mal formé")
    if not (isinstance(nombre_cartes, int) and not isinstance(nombre_cartes, bool) and nombre_cartes >= 1):
        raise Refus("paramètres : nombre gelé de cartes mal formé")


def verifier_sortie(chemin_sortie):
    """Avant toute lecture du fichier des cartes : la sortie est neuve et hors des lieux interdits."""
    if not (isinstance(chemin_sortie, str) and chemin_sortie.strip()):
        raise Refus("sortie : chemin vide")
    compagnon = chemin_sortie + ".sha256"
    if os.path.lexists(chemin_sortie) or os.path.lexists(compagnon):
        raise Refus("sortie : la sortie ou son compagnon existe déjà ; on n'écrase jamais (règle R12)")
    formes = {os.path.abspath(chemin_sortie), os.path.realpath(chemin_sortie)}
    racines = {DEPOT, os.path.realpath(DEPOT)}
    for forme in formes:
        if DOSSIER_INTERDIT in forme.split(os.sep):
            raise Refus("sortie : sous un dossier nommé « archives-reponses-modeles », interdit")
        if any(_sous(forme, r) for r in racines):
            raise Refus("sortie : sous le dépôt, interdit")
    if not os.path.isdir(os.path.dirname(os.path.abspath(chemin_sortie))):
        raise Refus("sortie : dossier parent absent")


def lire_octets_verifies(chemin_fiches, empreinte_attendue):
    """Octets du fichier ; empreinte calculée sur les octets, avant tout décodage."""
    if not (isinstance(chemin_fiches, str) and os.path.isfile(chemin_fiches)):
        raise Refus("fiches : fichier absent ou qui n'est pas un fichier ordinaire")
    lu = True
    try:
        with open(chemin_fiches, "rb") as f:
            octets = f.read()
    except OSError:
        lu = False
    if not lu:
        raise Refus("fiches : lecture impossible")
    if hashlib.sha256(octets).hexdigest() != empreinte_attendue:
        raise Refus("fiches : empreinte différente de l'empreinte gelée ; rien n'est décodé")
    return octets


def decoder(octets):
    """Décodage strict ; aucun message d'erreur du décodeur n'est repris (il pourrait citer du texte)."""
    racine, bon = None, True
    try:
        racine = json.loads(octets.decode("utf-8"), object_pairs_hook=_crochet_paires)
    except (ValueError, RecursionError):      # UnicodeDecodeError et JSONDecodeError sont des ValueError
        bon = False
    if not bon:
        raise Refus("fiches : texte UTF-8 ou JSON illisible")
    return racine


def _en_objets(valeur):
    """Convertit une valeur de la carte gardée ; une clé en double dans un objet est refusée."""
    if isinstance(valeur, _Paires):
        cles = [k for k, _ in valeur]
        if len(set(cles)) != len(cles):
            raise Refus("carte : clé en double dans un objet de la carte")
        return {k: _en_objets(v) for k, v in valeur}
    if isinstance(valeur, list):
        return [_en_objets(v) for v in valeur]
    return valeur


def garder_la_seule_carte(racine, identifiant, nombre_cartes):
    """Chemin du masque scellé : premier niveau {identifiant: enregistrement}. Ne rend que la carte visée,
    sans `meta`. Les autres clés ne servent qu'au compte et à la détection des doubles, dans cette fonction."""
    if not isinstance(racine, _Paires):
        raise Refus("fiches : le premier niveau n'est pas un objet {identifiant: enregistrement}")
    vues, doubles, occurrences, enregistrement = set(), False, 0, None
    for cle, valeur in racine:
        if cle == identifiant:
            occurrences += 1
            enregistrement = valeur
        elif cle in vues:
            doubles = True
        vues.add(cle)
    compte = len(vues)
    del vues
    if occurrences == 0:
        raise Refus("fiches : identifiant gelé absent")
    if occurrences > 1:
        raise Refus("fiches : identifiant gelé présent plus d'une fois")
    if doubles:
        raise Refus("fiches : une autre clé du premier niveau est en double")
    if compte != nombre_cartes:
        raise Refus("fiches : nombre de cartes différent du nombre gelé")
    if not isinstance(enregistrement, _Paires):
        raise Refus("carte : l'enregistrement visé n'est pas un objet")
    cles = [k for k, _ in enregistrement]
    if len(set(cles)) != len(cles):
        raise Refus("carte : clé en double au premier niveau de l'enregistrement visé")
    # `meta` retiré avant tout usage : sa valeur n'est ni convertie ni lue
    sans_meta = [(k, v) for k, v in enregistrement if k != CHAMP_RETIRE]
    del enregistrement
    if CHAMP_ATTENDU not in (k for k, _ in sans_meta):
        raise Refus("carte : l'enregistrement visé n'a pas de `contenu` (structure différente de celle du masque)")
    return {k: _en_objets(v) for k, v in sans_meta}


def ecrire_neuf(chemin_sortie, objet):
    octets_ok = True
    try:
        octets = (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    except ValueError:
        octets_ok = False
    if not octets_ok:
        raise Refus("sortie : carte non encodable en UTF-8 ; rien n'est écrit")
    empreinte = hashlib.sha256(octets).hexdigest()
    etape = "sortie"
    try:
        with open(chemin_sortie, "xb") as f:
            f.write(octets)
        etape = "compagnon"
        with open(chemin_sortie + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{empreinte}  {os.path.basename(chemin_sortie)}\n")
        etape = ""
    except OSError:
        pass
    if etape == "sortie":
        raise Refus("sortie : écriture impossible ; rien n'est écrit")
    if etape == "compagnon":
        raise Refus("sortie : écriture du compagnon impossible ; la sortie écrite reste sans compagnon")
    return empreinte


def extraire(chemin_fiches, chemin_sortie, empreinte_attendue, identifiant, nombre_cartes):
    """Moyen interne, aux paramètres explicites (les essais y passent des fichiers synthétiques)."""
    valider_parametres(empreinte_attendue, identifiant, nombre_cartes)
    verifier_sortie(chemin_sortie)
    octets = lire_octets_verifies(chemin_fiches, empreinte_attendue)
    racine = decoder(octets)
    del octets
    carte = garder_la_seule_carte(racine, identifiant, nombre_cartes)
    del racine
    return ecrire_neuf(chemin_sortie, {"carte": carte, "empreinte_fiches": empreinte_attendue,
                                       "identifiant": identifiant})


def executer(chemin_fiches, chemin_sortie, empreinte_attendue, identifiant, nombre_cartes):
    """Écran : « FAIT », ou un motif de refus sans valeur ; jamais un texte de carte ni une trace."""
    try:
        extraire(chemin_fiches, chemin_sortie, empreinte_attendue, identifiant, nombre_cartes)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    except Exception as e:                    # aucun message ni trace : ils pourraient citer une carte
        print(f"REFUS : erreur imprévue ({type(e).__name__}) ; aucun détail affiché", file=sys.stderr)
        return 3
    print("FAIT")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="extraire_carte_alarme_v1.py", allow_abbrev=False,
        description="Extrait la seule carte de l'alarme (constantes gelées), champ `meta` retiré (v1).")
    p.add_argument("--fiches", required=True, metavar="CHEMIN")
    p.add_argument("--sortie", required=True, metavar="CHEMIN")
    a = p.parse_args(argv)
    return executer(a.fiches, a.sortie, EMPREINTE_FICHES, IDENTIFIANT_CARTE, NOMBRE_CARTES)


if __name__ == "__main__":
    sys.exit(main())
