#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Noms des clés de `contenu` hors des champs de la configuration, fichier des cartes de la course v9 — v1.

Pièce de travail (classe C). Rapporte les seuls NOMS des clés de `contenu` qui ne sont pas des champs
de la configuration A du masque, et, pour chaque nom, le nombre de cartes qui le portent. Ne lit, ne
copie, n'affiche ni n'écrit aucune valeur, aucun identifiant de carte.

Chemin de lecture reproduit à la lettre du masque scellé `masque_style_cartes_v1.py` (empreinte
07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e), fonctions `valider_configuration`
et `extraire_contenus` : configuration validée comme le masque la valide ; champs pris dans
`configuration["champs"]` ; cartes nommées dans `configuration["hors_choix"]` non ouvertes ; seul accès
aux enregistrements : `fiches[identifiant]["contenu"]`, dont seules les clés sont lues. Le masque refuse
à la première carte qui porte une clé hors des champs ; ce programme, à cet endroit, compte au lieu de
refuser, et ne fait rien d'autre.

Ordre : la configuration, puis les cartes. Les deux empreintes sont calculées sur les octets et
comparées aux empreintes gelées avant tout décodage ; toute différence est un refus.
Sortie : un JSON à trois champs (`cles_hors_champs`, `nombre_de_cartes`, `empreintes`) et son
compagnon `.sha256`. À l'écran : « FAIT », ou le motif d'un refus ; jamais un nom de clé, un
identifiant ni une valeur.
Garde : un nom de plus de 64 caractères, ou qui contient un saut de ligne, est remplacé par
« (nom non rapporté : longueur L) » ; son compte est gardé.
Tout refus rend le code 2 et n'écrit rien. Aucun repli silencieux (règle R5).
Bibliothèque standard seulement ; aucun tirage au sort ; aucune liste ni recherche de dossier ;
aucun chemin par défaut.
"""
import argparse
import hashlib
import json
import os
import sys

VERSION = "noms_cles_contenu_hors_champs_v1"

# Empreintes gelées : le point d'entrée en ligne de commande n'accepte que celles-ci.
SHA_FICHES = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
SHA_CONFIGURATION = "8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4"

LONGUEUR_MAXIMALE_NOM = 64
CLES_SORTIE = ("cles_hors_champs", "nombre_de_cartes", "empreintes")

# Reproduit à la lettre de masque_style_cartes_v1.py.
CLES_CONFIGURATION = {"champs", "plafond", "formules", "intertitres", "seuil_formule_recitee",
                      "minimum_formule_recitee", "hors_choix"}


class Refus(Exception):
    """Refus explicite : le programme s'arrête, n'écrit rien, rend le code 2.

    Un motif de refus ne porte jamais un nom de clé, un identifiant ni une valeur."""


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def _empreinte_bien_formee(sha):
    return isinstance(sha, str) and len(sha) == 64 and all(c in "0123456789abcdef" for c in sha)


def lire_octets_verifies(chemin, sha_attendu, role):
    """Lit les octets d'un fichier nommé par son chemin et compare leur empreinte, avant tout décodage."""
    if not _empreinte_bien_formee(sha_attendu):
        raise Refus(f"{role} : empreinte gelée illisible")
    if not os.path.isfile(chemin):
        raise Refus(f"{role} : fichier absent")
    with open(chemin, "rb") as f:
        octets = f.read()
    sha = sha_octets(octets)
    if sha != sha_attendu:
        raise Refus(f"{role} : empreinte différente de l'empreinte gelée")
    return octets, sha


def decoder_json(octets, role):
    """Décodage UTF-8 puis JSON ; le message de l'erreur n'est pas rapporté (il peut citer un octet)."""
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Refus(f"{role} : JSON illisible") from None


def valider_configuration(c):
    """Reproduit à la lettre de masque_style_cartes_v1.py."""
    if not isinstance(c, dict) or set(c) != CLES_CONFIGURATION:
        raise Refus("configuration : clés attendues " + ", ".join(sorted(CLES_CONFIGURATION)))
    ch = c["champs"]
    if not (isinstance(ch, list) and ch and all(isinstance(x, str) and x for x in ch) and len(set(ch)) == len(ch)):
        raise Refus("configuration : liste ordonnée des champs vide, mal formée ou à doublon")
    if set(ch) & {"meta", "empreinte"}:
        raise Refus("configuration : `meta` et `empreinte` ne sont pas des champs de contenu")
    p = c["plafond"]
    if p != "mediane":
        if not (isinstance(p, dict) and set(p) == set(ch)
                and all(isinstance(v, int) and not isinstance(v, bool) and v >= 1 for v in p.values())):
            raise Refus("configuration : plafond « mediane », ou un entier d'au moins 1 pour chaque champ")
    for k in ("formules", "intertitres", "hors_choix"):
        if not (isinstance(c[k], list) and all(isinstance(x, str) and x.strip() for x in c[k])):
            raise Refus(f"configuration : {k} doit être une liste de textes non vides")
    s = c["seuil_formule_recitee"]
    if not (s is None or (isinstance(s, (int, float)) and not isinstance(s, bool) and 0 < s <= 1)):
        raise Refus("configuration : seuil de formule récitée dans ]0, 1], ou null")
    mn = c["minimum_formule_recitee"]
    if not (isinstance(mn, int) and not isinstance(mn, bool) and mn >= 2):
        raise Refus("configuration : minimum de cartes d'une formule récitée, entier d'au moins 2")
    return c


def compter_noms_hors_champs(fiches, champs, hors_choix):
    """Chemin de `extraire_contenus` du masque, à la lettre, jusqu'aux clés de `contenu`.

    Seuls les noms des clés de `contenu` sont lus ; aucune valeur, ni de `contenu` ni d'ailleurs.
    Les identifiants ne servent qu'en mémoire (ordre de parcours, cartes hors du choix) ; ils ne sortent
    jamais. Rend ({nom: nombre de cartes ouvertes qui le portent}, nombre de cartes ouvertes)."""
    if not isinstance(fiches, dict) or not fiches:
        raise Refus("cartes : objet {identifiant: enregistrement} non vide attendu")
    hors, champs_ = set(hors_choix), set(champs)
    comptes, ouvertes = {}, 0
    for ident in sorted(fiches, key=lambda s: s.encode("utf-8")):
        if ident in hors:
            continue                      # carte hors du choix : non ouverte, comme dans le masque
        rec = fiches[ident]
        if not isinstance(rec, dict) or "contenu" not in rec:
            raise Refus("cartes : un enregistrement est sans `contenu`")
        contenu = rec["contenu"]
        if not isinstance(contenu, dict):
            raise Refus("cartes : un `contenu` n'est pas un objet de champs")
        ouvertes += 1
        for nom in set(contenu) - champs_:   # noms seuls : `set(contenu)` ne parcourt que les clés
            comptes[nom] = comptes.get(nom, 0) + 1
    if ouvertes == 0:
        raise Refus("cartes : aucune carte ouverte (toutes hors du choix)")
    return comptes, ouvertes


def _porte_un_saut_de_ligne(nom):
    """Saut de ligne au sens de `str.splitlines` : \\n, \\r, \\v, \\f, \\x1c à \\x1e, \\x85, U+2028, U+2029."""
    return "".join(nom.splitlines()) != nom


def nom_rapporte(nom):
    """Garde : un nom ne doit pas pouvoir porter du contenu."""
    if len(nom) > LONGUEUR_MAXIMALE_NOM or _porte_un_saut_de_ligne(nom):
        return f"(nom non rapporté : longueur {len(nom)})"
    return nom


def construire_sortie(comptes, ouvertes, sha_fiches, sha_configuration):
    liste = [{"nom": nom_rapporte(n), "nombre_de_cartes": k} for n, k in comptes.items()]
    liste.sort(key=lambda d: (d["nom"], d["nombre_de_cartes"]))   # jamais selon le nom d'origine
    return {"cles_hors_champs": liste, "nombre_de_cartes": ouvertes,
            "empreintes": {"fiches": sha_fiches, "configuration": sha_configuration}}


def verifier_sortie(objet, ouvertes):
    """Postcondition, vérifiée avant toute écriture : la sortie est bien celle que le programme dit."""
    if list(objet) != list(CLES_SORTIE):
        raise Refus("postcondition : la sortie ne porte pas exactement les trois champs")
    if objet["nombre_de_cartes"] != ouvertes or not (isinstance(ouvertes, int) and ouvertes >= 1):
        raise Refus("postcondition : nombre de cartes incohérent")
    if set(objet["empreintes"]) != {"fiches", "configuration"} \
            or not all(_empreinte_bien_formee(v) for v in objet["empreintes"].values()):
        raise Refus("postcondition : empreintes mal formées")
    liste = objet["cles_hors_champs"]
    if liste != sorted(liste, key=lambda d: (d["nom"], d["nombre_de_cartes"])):
        raise Refus("postcondition : liste des clés non triée")
    for d in liste:
        if set(d) != {"nom", "nombre_de_cartes"}:
            raise Refus("postcondition : une entrée porte une clé de trop")
        if not isinstance(d["nom"], str) or len(d["nom"]) > LONGUEUR_MAXIMALE_NOM or _porte_un_saut_de_ligne(d["nom"]):
            raise Refus("postcondition : un nom rapporté échappe à la garde")
        n = d["nombre_de_cartes"]
        if not (isinstance(n, int) and not isinstance(n, bool) and 1 <= n <= ouvertes):
            raise Refus("postcondition : un compte de cartes hors de [1, nombre de cartes]")
    return True


def ecrire_neuf(chemin, objet):
    """Écrit la sortie puis son compagnon ; n'écrase jamais (règle R12).

    `ensure_ascii=True` : tout caractère hors ASCII ou de contrôle d'un nom est écrit en échappement
    JSON (le nom reste exact une fois le JSON décodé ; rien ne s'imprime de travers dans un terminal)."""
    compagnon = chemin + ".sha256"
    if os.path.exists(chemin) or os.path.exists(compagnon):
        raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
    octets = (json.dumps(objet, ensure_ascii=True, indent=1) + "\n").encode("utf-8")
    sha = sha_octets(octets)
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(compagnon, "x", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def executer(chemin_fiches, chemin_configuration, chemin_sortie, *, sha_fiches, sha_configuration):
    """Moyen interne : les empreintes attendues sont des paramètres (les essais y passent les leurs)."""
    if os.path.exists(chemin_sortie) or os.path.exists(chemin_sortie + ".sha256"):
        raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
    if not os.path.isdir(os.path.dirname(os.path.abspath(chemin_sortie))):
        raise Refus("dossier de la sortie absent")
    # 1. Octets et empreintes, la configuration puis les cartes, avant tout décodage.
    octets_c, sha_c = lire_octets_verifies(chemin_configuration, sha_configuration, "configuration")
    octets_f, sha_f = lire_octets_verifies(chemin_fiches, sha_fiches, "fiches")
    # 2. La configuration décodée d'abord : les champs et les cartes hors du choix, comme le masque.
    conf = valider_configuration(decoder_json(octets_c, "configuration"))
    champs, hors_choix = list(conf["champs"]), list(conf["hors_choix"])
    del conf, octets_c
    # 3. Les cartes ensuite : les seuls noms des clés de `contenu`.
    fiches = decoder_json(octets_f, "fiches")
    del octets_f
    comptes, ouvertes = compter_noms_hors_champs(fiches, champs, hors_choix)
    del fiches
    objet = construire_sortie(comptes, ouvertes, sha_f, sha_c)
    verifier_sortie(objet, ouvertes)
    return ecrire_neuf(chemin_sortie, objet)


def lancer(chemin_fiches, chemin_configuration, chemin_sortie, *, sha_fiches, sha_configuration):
    """Joue et parle : « FAIT », ou le motif d'un refus ; le message d'une erreur imprévue n'est pas rapporté."""
    try:
        executer(chemin_fiches, chemin_configuration, chemin_sortie,
                 sha_fiches=sha_fiches, sha_configuration=sha_configuration)
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 — aucun message d'erreur imprévue ne sort (il pourrait citer un nom)
        print(f"REFUS : erreur imprévue ({type(e).__name__}), message non rapporté", file=sys.stderr)
        return 2
    print("FAIT")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Noms des clés de `contenu` hors des champs de la configuration (v1). "
                    "Empreintes gelées dans le programme ; aucun chemin par défaut.",
        allow_abbrev=False)
    p.add_argument("--fiches", required=True, metavar="CHEMIN")
    p.add_argument("--configuration", required=True, metavar="CHEMIN")
    p.add_argument("--sortie", required=True, metavar="CHEMIN")
    a = p.parse_args(argv)
    return lancer(a.fiches, a.configuration, a.sortie,
                  sha_fiches=SHA_FICHES, sha_configuration=SHA_CONFIGURATION)


if __name__ == "__main__":
    sys.exit(main())
