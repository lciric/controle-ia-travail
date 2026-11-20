#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lecteur par programme des cartes — témoin sans famille pour le critère D et pour la voie — v1.

Ce lecteur n'a pas de famille : c'est une règle de structure, écrite sans lire une carte. Il
sert de TÉMOIN aux deux lecteurs (audit de symétrie, recommandation 2), jamais d'arbitre : il ne
note pas la valeur d'une carte, ne range rien, n'entre dans aucun plancher, aucun rang, aucune
liste. Ce sont les essais qui tranchent (N-058).

Ce qu'il rend, par carte :
  - D (0, 1, 2 ou null) : le champ « ce qui la réfuterait » nomme-t-il ce qui est fait au « non »
    (retirer, couper, ne pas ajouter, garder la base), et la carte nomme-t-elle ce qui est fait au
    « oui » (garder, retenir, régler) ? C'est la lettre du critère D : garder, retirer ou régler
    un module ; l'abandon nommé vaut une décision.
  - la voie (I, P, N ou null) et la sous-strate, par le nombre de termes DISTINCTS d'un lexique
    fixe présents dans les champs désignés ; un terme répété ne compte qu'une fois, pour qu'une
    carte longue ne pèse pas plus qu'une brève.
« null » veut dire indécidable : jamais une valeur par défaut.

Il ne lit d'une carte que `contenu` (format « fiches ») ou les champs d'une sortie du masque de
style (format « masque »). Jamais `meta`. Sa sortie ne porte aucun texte de carte.
Tout refus rend le code 2 et n'écrit rien. Bibliothèque standard seulement ; aucun tirage au sort.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

VERSION = "lecteur_par_programme_cartes_v1"
CLES_CONFIGURATION = {"champ_refutation", "champs_voie", "hors_choix"}
SEUIL_TERMES = 2

# Lexiques fixes, sans accent ni casse. Écrits sans lire une carte ; l'auteur a vu des titres de
# cartes dans des pièces versées (voir son rapport) : ce témoin n'est pas tenu à l'écart de la v9.
NON_NOMME = ["sinon", "couper", "coupe le", "coupe la", "retirer", "retire le", "retire la", "retrait",
             "abandon", "ne pas ajouter", "n'est pas ajoute", "non ajoute", "la base suffit", "garder la base",
             "revenir a", "supprimer", "desactiver", "ne pas adopter", "ne pas retenir", "rejeter le mecanisme"]
OUI_NOMME = ["garder", "conserver", "retenir", "adopter", "regler", "reglage", "maintenir", "seulement si",
             "activer", "promouvoir le mecanisme"]
LEXIQUES = {
    "I": ["instrument", "rejeu", "rejouer", "audit", "banc d'essai", "etalonnage", "etalonner", "harnais",
          "porte de version", "porte d'adoption", "porte de modification", "protocole de mesure",
          "outil de mesure", "adoption d'une modification"],
    "a": ["herit", "registre des tentatives", "course anterieure", "course precedente", "ne vide"],
    "b": ["lois connues", "hypothese nulle", "nul d'archive", "nul classique", "archive comme nul", "nul forme"],
    "c1": ["generation suivante", "ce qui est montre", "ce qui est servi", "masqu", "note du juge", "placebo",
           "archive factice"],
    "c2": ["survie", "oubli", "peremption", "reentree", "quota", "portefeuille", "conservation des fiches"],
    "c3": ["test de mort", "tests de mort", "reimplementation", "interprete", "execution invalide", "avorte"],
    "d": ["multiplicite", "bonferroni", "holm", "comparaisons multiples", "fausses decouvertes", "faux positifs"],
    "e": ["juges croises", "college", "agregation", "erreurs correlees", "votes effectifs", "accord entre juges"],
}
SOUS_STRATES = ["a", "b", "c1", "c2", "c3", "d", "e"]
EN_TETE = [
    "Lecteur par programme : témoin sans famille pour le critère D et pour la voie. Il ne note pas la "
    "valeur d'une carte, ne range rien et n'entre dans aucune liste ; ce sont les essais qui tranchent (N-058).",
    "Limite : règle de structure sur des mots ; elle ne lit pas le sens. Un désaccord avec un lecteur ne dit "
    "pas qui a raison.",
]


class Refus(Exception):
    """Refus explicite : le programme s'arrête, n'écrit rien, rend le code 2."""


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def lire_json_verifie(chemin, sha_attendu, role):
    if not os.path.isfile(chemin):
        raise Refus(f"{role} : fichier absent ({chemin})")
    attendu = str(sha_attendu).strip().lower()
    if len(attendu) != 64 or any(c not in "0123456789abcdef" for c in attendu):
        raise Refus(f"{role} : empreinte attendue illisible")
    with open(chemin, "rb") as f:
        octets = f.read()
    if sha_octets(octets) != attendu:
        raise Refus(f"{role} : empreinte différente de celle annoncée")
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Refus(f"{role} : JSON illisible ({e})")


def valider_configuration(c):
    if not isinstance(c, dict) or set(c) != CLES_CONFIGURATION:
        raise Refus("configuration : clés attendues " + ", ".join(sorted(CLES_CONFIGURATION)))
    if not (isinstance(c["champ_refutation"], str) and c["champ_refutation"]):
        raise Refus("configuration : champ de réfutation non nommé")
    v = c["champs_voie"]
    if not (isinstance(v, list) and v and all(isinstance(x, str) and x for x in v)):
        raise Refus("configuration : champs lus pour la voie, liste non vide")
    if {"meta", "empreinte"} & (set(v) | {c["champ_refutation"]}):
        raise Refus("configuration : `meta` et `empreinte` ne sont pas des champs de contenu")
    if not (isinstance(c["hors_choix"], list) and all(isinstance(x, str) for x in c["hors_choix"])):
        raise Refus("configuration : liste « hors du choix » mal formée")
    return c


def normaliser(texte):
    t = unicodedata.normalize("NFD", texte.casefold().replace("’", "'"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t).strip()


def extraire(donnees, forme, hors_choix):
    """Rend {identifiant: {champ: texte}}. Seuls accès : `contenu` (fiches) ou `champs` (masque)."""
    hors, sortie = set(hors_choix), {}
    if forme == "fiches":
        if not isinstance(donnees, dict) or not donnees:
            raise Refus("cartes : objet {identifiant: enregistrement} non vide attendu")
        for ident in sorted(donnees, key=lambda s: s.encode("utf-8")):
            if ident in hors:
                continue
            rec = donnees[ident]
            if not isinstance(rec, dict) or "contenu" not in rec or not isinstance(rec["contenu"], dict):
                raise Refus("cartes : un enregistrement est sans `contenu`")
            sortie[ident] = dict(rec["contenu"])
    elif forme == "masque":
        if not isinstance(donnees, dict) or not isinstance(donnees.get("cartes"), list):
            raise Refus("cartes masquées : clé « cartes » attendue")
        for c in donnees["cartes"]:
            if not isinstance(c, dict) or set(c) != {"id", "champs"}:
                raise Refus("cartes masquées : enregistrement mal formé")
            if c["id"] in hors:
                raise Refus("cartes masquées : une carte hors du choix y figure")
            if c["id"] in sortie:
                raise Refus("cartes masquées : carte en double")
            sortie[c["id"]] = {k: t for k, t in c["champs"]}
    else:
        raise Refus("forme inconnue : « fiches » ou « masque »")
    if not sortie:
        raise Refus("cartes : aucune carte à lire")
    return sortie


def presents(texte, termes):
    return [t for t in termes if t in texte]


def lire_carte(champs, configuration):
    ref, voie_champs = configuration["champ_refutation"], configuration["champs_voie"]
    for k in [ref] + voie_champs:
        if k not in champs:
            raise Refus(f"une carte n'a pas le champ « {k} » nommé par la configuration : refus, rien n'est deviné")
        if not isinstance(champs[k], str):
            raise Refus(f"le champ « {k} » d'une carte n'est pas un texte")
    refutation = normaliser(champs[ref])
    tout = normaliser(" ".join(v for v in champs.values() if isinstance(v, str)))
    if not refutation:
        d, non, oui = None, None, None
    else:
        non = bool(presents(refutation, NON_NOMME))
        oui = bool(presents(tout, OUI_NOMME))
        d = 2 if (non and oui) else (1 if (non or oui) else 0)
    texte_voie = normaliser(" ".join(champs[k] for k in voie_champs))
    comptes = {s: len(presents(texte_voie, LEXIQUES[s])) for s in ["I"] + SOUS_STRATES}
    s_i = comptes["I"]
    s_p = max(comptes[s] for s in SOUS_STRATES)
    meilleures = [s for s in SOUS_STRATES if comptes[s] == s_p]
    sous = None
    if not texte_voie:
        voie = None
    elif s_i >= SEUIL_TERMES and s_p >= SEUIL_TERMES and s_i == s_p:
        voie = None                                    # instrument ou question du programme : indécidable
    elif s_i >= SEUIL_TERMES and s_i > s_p:
        voie = "I"
    elif s_p >= SEUIL_TERMES:
        voie = "P"
        sous = meilleures[0] if len(meilleures) == 1 else None
    else:
        voie = "N"
    return {"voie": voie, "sous_strate": sous, "D": d, "note": d, "non_nomme": non, "oui_nomme": oui,
            "termes_distincts": comptes}


def lire_tout(cartes, configuration):
    sortie = []
    for ident in sorted(cartes, key=lambda s: s.encode("utf-8")):
        sortie.append({"id": ident, **lire_carte(cartes[ident], configuration)})
    n = len(sortie)
    rapport = {
        "cartes": n,
        "D": {str(k): sum(1 for c in sortie if c["D"] == k) for k in (0, 1, 2)},
        "D_indecidable": sum(1 for c in sortie if c["D"] is None),
        "voie": {v: sum(1 for c in sortie if c["voie"] == v) for v in ("I", "N", "P")},
        "voie_indecidable": sum(1 for c in sortie if c["voie"] is None),
        "sous_strate_indecidable_en_voie_P": sum(1 for c in sortie if c["voie"] == "P" and c["sous_strate"] is None),
    }
    return sortie, rapport


def ecrire_neuf(chemin, objet):
    compagnon = chemin + ".sha256"
    if os.path.exists(chemin) or os.path.exists(compagnon):
        raise Refus(f"sortie déjà présente ({chemin}) : on n'écrase jamais (règle R12)")
    octets = (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(compagnon, "x", encoding="utf-8") as f:
        f.write(f"{sha_octets(octets)}  {os.path.basename(chemin)}\n")
    return sha_octets(octets)


def main(argv=None):
    p = argparse.ArgumentParser(description="Lecteur par programme (v1) : témoin sans famille pour D et la voie.")
    p.add_argument("--cartes", required=True, nargs=2, metavar=("CHEMIN", "SHA256"))
    p.add_argument("--forme", required=True, choices=["fiches", "masque"])
    p.add_argument("--configuration", required=True, nargs=2, metavar=("CHEMIN", "SHA256"))
    p.add_argument("--sortie", required=True)
    args = p.parse_args(argv)
    try:
        if os.path.exists(args.sortie) or os.path.exists(args.sortie + ".sha256"):
            raise Refus("sortie déjà présente : on n'écrase jamais (règle R12)")
        conf = valider_configuration(lire_json_verifie(args.configuration[0], args.configuration[1], "configuration"))
        donnees = lire_json_verifie(args.cartes[0], args.cartes[1], "cartes")
        cartes = extraire(donnees, args.forme, conf["hors_choix"])
        del donnees
        lues, rapport = lire_tout(cartes, conf)
        with open(os.path.abspath(__file__), "rb") as f:
            sha_programme = sha_octets(f.read())
        sha = ecrire_neuf(args.sortie, {
            "piece": VERSION, "lecteur": "programme", "en_tete": EN_TETE, "forme_lue": args.forme,
            "rapport": rapport,
            "empreintes": {"programme": sha_programme, "cartes": args.cartes[1].lower(),
                           "configuration": args.configuration[1].lower()},
            "cartes": lues})
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(json.dumps(rapport, ensure_ascii=False))
    print(f"lecture par programme écrite : {args.sortie} ({sha})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
