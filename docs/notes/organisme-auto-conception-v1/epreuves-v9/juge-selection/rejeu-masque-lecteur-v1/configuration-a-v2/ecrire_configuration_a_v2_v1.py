#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit la configuration A v2 du masque de style, à partir de la v1 scellée — v1.

Rédacteur neuf, modèle F. Aucune carte lue : le programme ne lit que trois pièces nommées, chacune
vérifiée par son empreinte avant usage — la configuration A v1, le résultat des noms de clés
(noms et nombres de cartes seulement), et le masque v1 (chargé pour sa seule fonction
`valider_configuration` ; le masque n'est lancé sur aucune carte).

Ce qu'il change à la v1, et rien d'autre : il ajoute une clé, `cles_hors_champs_retirees`, qui
nomme les clés de `contenu` hors des dix champs que le masque doit retirer de la forme masquée,
avec le nombre de cartes attendu pour chacune (garde : un autre nombre doit être un refus).

Il ne contourne rien : il appelle `valider_configuration` du masque v1 sur la v2 telle quelle et
rapporte ce que le masque répond, refus compris. Il rapporte à part, comme diagnostic et nommé
comme tel, la validation de la v2 privée de la clé ajoutée.

Usage : python3 -B ecrire_configuration_a_v2_v1.py CONF_V1 SHA_V1 NOMS_CLES SHA_NOMS MASQUE SHA_MASQUE DOSSIER_SORTIE
Écrit, sans jamais écraser : configuration-a-masque-v2.json et sortie-validation-configuration-a-v2-v1.txt.
Tout refus du programme lui-même rend le code 2 et n'écrit rien.
"""
import hashlib
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True          # rien n'est écrit à côté du masque, dans le dépôt

CLE_NEUVE = "cles_hors_champs_retirees"
NOM_V2 = "configuration-a-masque-v2.json"
NOM_SORTIE = "sortie-validation-configuration-a-v2-v1.txt"


def refuser(message):
    print(f"REFUS : {message}", file=sys.stderr)
    sys.exit(2)


def lire_verifie(chemin, attendu, role):
    if not os.path.isfile(chemin):
        refuser(f"{role} : fichier absent ({chemin})")
    with open(chemin, "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != attendu.strip().lower():
        refuser(f"{role} : empreinte {vu}, {attendu} attendue")
    return octets


def serialiser(objet):
    """La forme d'écriture de la v1 (programme 6e648318…, fonction `ecrire`)."""
    return (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def main(argv):
    if len(argv) != 8:
        refuser("sept arguments attendus (voir l'usage)")
    conf_v1, sha_v1, noms, sha_noms, masque, sha_masque, sortie = argv[1:]
    chemin_v2 = os.path.join(sortie, NOM_V2)
    chemin_sortie = os.path.join(sortie, NOM_SORTIE)
    for c in (chemin_v2, chemin_sortie):
        if os.path.exists(c):
            refuser(f"sortie déjà présente ({c}) : on n'écrase jamais (règle R12)")

    octets_v1 = lire_verifie(conf_v1, sha_v1, "configuration A v1")
    octets_noms = lire_verifie(noms, sha_noms, "noms de clés")
    lire_verifie(masque, sha_masque, "masque v1")

    v1 = json.loads(octets_v1.decode("utf-8"))
    if serialiser(v1) != octets_v1:
        refuser("la v1 relue puis réécrite ne rend pas ses octets : la forme d'écriture n'est pas celle attendue")

    resultat = json.loads(octets_noms.decode("utf-8"))
    if set(resultat) != {"cles_hors_champs", "nombre_de_cartes", "empreintes"}:
        refuser("noms de clés : clés inattendues")
    if resultat["empreintes"].get("configuration") != sha_v1.strip().lower():
        refuser("noms de clés : ce résultat n'a pas été calculé contre la configuration A v1 donnée")
    lignes_cles = resultat["cles_hors_champs"]
    if not (isinstance(lignes_cles, list) and lignes_cles
            and all(isinstance(x, dict) and set(x) == {"nom", "nombre_de_cartes"} for x in lignes_cles)):
        refuser("noms de clés : liste mal formée")
    retirees = {}
    for x in sorted(lignes_cles, key=lambda y: y["nom"].encode("utf-8")):
        nom, n = x["nom"], x["nombre_de_cartes"]
        if not (isinstance(nom, str) and nom and isinstance(n, int) and not isinstance(n, bool) and n >= 1):
            refuser("noms de clés : nom vide ou nombre de cartes illisible")
        if nom in retirees:
            refuser("noms de clés : nom en double")
        if nom in v1["champs"] or nom in ("meta", "empreinte"):
            refuser(f"noms de clés : « {nom} » est un champ de la configuration, ou `meta`, ou `empreinte`")
        retirees[nom] = n

    if CLE_NEUVE in v1:
        refuser("la v1 porte déjà la clé neuve")
    v2 = dict(v1)
    v2[CLE_NEUVE] = retirees
    octets_v2 = serialiser(v2)

    spec = importlib.util.spec_from_file_location("masque_style_cartes_v1", masque)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    def valider(objet):
        try:
            m.valider_configuration(objet)
            return "passé, aucun refus"
        except m.Refus as e:
            return f"REFUS : {e}"

    verdict_v2 = valider(json.loads(octets_v2.decode("utf-8")))
    sans_cle = {k: v for k, v in json.loads(octets_v2.decode("utf-8")).items() if k != CLE_NEUVE}
    verdict_sans_cle = valider(sans_cle)
    verdict_v1 = valider(json.loads(octets_v1.decode("utf-8")))

    sha_v2 = hashlib.sha256(octets_v2).hexdigest()
    lignes = [
        "Sortie de ecrire_configuration_a_v2_v1.py — rédacteur neuf, modèle F. Aucune carte lue ; masque lancé sur aucune carte.",
        f"python : {sys.version.split()[0]}",
        "empreintes des entrées : conformes (3)",
        f"  configuration A v1 : {sha_v1.strip().lower()}",
        f"  noms de clés       : {sha_noms.strip().lower()}",
        f"  masque v1          : {sha_masque.strip().lower()}",
        "la v1 relue puis réécrite rend ses octets : oui",
        f"{NOM_V2} : {sha_v2}",
        f"différence v1 -> v2 : une clé ajoutée, `{CLE_NEUVE}` = "
        + json.dumps(retirees, ensure_ascii=False) + " ; les sept clés de la v1 inchangées : "
        + ("oui" if sans_cle == v1 else "NON"),
        f"clés de la v2 : {len(v2)} ; clés attendues par le masque v1 (CLES_CONFIGURATION) : {len(m.CLES_CONFIGURATION)}",
        f"masque v1, valider_configuration(v2 telle quelle) : {verdict_v2}",
        f"diagnostic, non une validation de la v2 — valider_configuration(v2 privée de `{CLE_NEUVE}`) : {verdict_sans_cle}",
        f"rappel — valider_configuration(v1) : {verdict_v1}",
        "lecture : " + ("le masque v1 ne sait pas représenter ce choix ; rien n'est contourné ; c'est le code, ou le choix, qui change"
                        if verdict_v2.startswith("REFUS") else "le masque v1 accepte la v2"),
    ]
    texte = "\n".join(lignes) + "\n"
    with open(chemin_v2, "xb") as f:
        f.write(octets_v2)
    with open(chemin_sortie, "x", encoding="utf-8") as f:
        f.write(texte)
    sys.stdout.write(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
