#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contre-lecture de la configuration A v2 du masque de style — vérification par programme — v1.

Contre-lecteur, modèle O. Aucune carte lue : le programme ne lit que des pièces nommées, chacune
vérifiée par son empreinte avant usage. Les deux masques sont chargés pour leur seule fonction
`valider_configuration` ; aucun n'est lancé sur une carte.

Usage : python3 -B verifier_configuration_a_v2_v1.py CONF_V1 CONF_V2 NOMS_CLES MASQUE_V1 MASQUE_V2 CONF_B
Rend 0 si tous les contrôles passent, 1 sinon (chaque contrôle est écrit, passé ou non).
"""
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True

ATTENDU = {
    "conf_v1": "8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4",
    "conf_v2": "a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54",
    "noms_cles": "86aecdee84f82003c7a16e8be7acc9fb030adaab2a7ea44db9fa6b2d29a2f5b6",
    "masque_v1": "07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e",
    "masque_v2": "769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01",
    "conf_b": "b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a",
}
FICHES_GO_24 = "ba65c411"
CLE_NEUVE = "cles_hors_champs_retirees"

resultats = []


def controle(nom, vrai, detail=""):
    resultats.append(bool(vrai))
    print(f"[{'PASSE' if vrai else 'ÉCHEC'}] {nom}" + (f" — {detail}" if detail else ""))


def lire(chemin, role):
    with open(chemin, "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    controle(f"empreinte de {role}", vu == ATTENDU[role], vu)
    return octets


def serialiser(objet):
    return (json.dumps(objet, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def valider(m, objet):
    try:
        m.valider_configuration(json.loads(json.dumps(objet)))
        return "passe"
    except m.Refus as e:
        return f"REFUS : {e}"


def main(argv):
    if len(argv) != 7:
        print("six arguments attendus", file=sys.stderr)
        return 2
    c1, c2, nc, m1, m2, cb = argv[1:]
    o1, o2 = lire(c1, "conf_v1"), lire(c2, "conf_v2")
    onc, ob = lire(nc, "noms_cles"), lire(cb, "conf_b")
    lire(m1, "masque_v1")
    lire(m2, "masque_v2")
    v1, v2 = json.loads(o1.decode("utf-8")), json.loads(o2.decode("utf-8"))
    noms, confb = json.loads(onc.decode("utf-8")), json.loads(ob.decode("utf-8"))

    # 1. Forme d'écriture
    controle("v1 relue puis réécrite rend ses octets", serialiser(v1) == o1)
    controle("v2 relue puis réécrite rend ses octets (même forme que la v1)", serialiser(v2) == o2)

    # 2. Une seule clé ajoutée, les sept autres égales
    controle("v1 a sept clés", len(v1) == 7, str(len(v1)))
    controle("v2 a huit clés", len(v2) == 8, str(len(v2)))
    controle("clés de la v2 moins clés de la v1 = la seule clé neuve",
             set(v2) - set(v1) == {CLE_NEUVE}, str(sorted(set(v2) - set(v1))))
    controle("aucune clé de la v1 ne manque à la v2", set(v1) - set(v2) == set())
    for k in v1:
        controle(f"clé « {k} » égale, valeur et type (texte JSON égal)",
                 k in v2 and json.dumps(v1[k], ensure_ascii=False) == json.dumps(v2[k], ensure_ascii=False)
                 and type(v1[k]) is type(v2[k]))
    controle("ordre des sept clés de la v1 gardé dans la v2, la neuve en dernier",
             list(v2)[:7] == list(v1) and list(v2)[7] == CLE_NEUVE)

    # 3. Les nombres attendus égaux au résultat des noms de clés
    controle("résultat des noms de clés calculé contre la configuration A v1",
             noms["empreintes"]["configuration"] == ATTENDU["conf_v1"])
    controle("résultat des noms de clés calculé sur le fichier de cartes de GO-2026-11-20-24 (ba65c411…)",
             noms["empreintes"]["fiches"].startswith(FICHES_GO_24))
    attendu = {x["nom"]: x["nombre_de_cartes"] for x in noms["cles_hors_champs"]}
    retirees = v2[CLE_NEUVE]
    controle("noms et nombres de la clé neuve égaux au résultat des noms de clés",
             retirees == attendu and len(noms["cles_hors_champs"]) == len(attendu),
             json.dumps(retirees, ensure_ascii=False) + " / " + json.dumps(attendu, ensure_ascii=False))
    controle("tous les nombres sont des entiers d'au moins 1",
             all(isinstance(n, int) and not isinstance(n, bool) and n >= 1 for n in retirees.values()))
    controle("aucun nom retiré n'est un champ, ni `meta`, ni `empreinte`",
             not (set(retirees) & (set(v2["champs"]) | {"meta", "empreinte"})))
    controle("hors_choix vide : les nombres attendus portent sur les cartes du résultat (94)",
             v2["hors_choix"] == [] and noms["nombre_de_cartes"] == 94)
    s, mx = sum(retirees.values()), max(retirees.values())
    print(f"       cartes porteuses : de {mx} (si toutes les clés sont sur les mêmes cartes) à {s} au plus")

    # 4. Ce que disent les deux masques
    mv1, mv2 = charger(m1, "masque_style_cartes_v1"), charger(m2, "masque_style_cartes_v2")
    r = valider(mv2, v2)
    controle("masque v2 : valider_configuration(v2) passe", r == "passe", r)
    r = valider(mv1, v2)
    controle("masque v1 : valider_configuration(v2) refuse (attendu)", r.startswith("REFUS"), r)
    r = valider(mv2, v1)
    controle("masque v2 : valider_configuration(v1) passe (sans la clé, conduite du v1)", r == "passe", r)
    controle("masque v2 : constante de la clé neuve égale au nom de la configuration",
             getattr(mv2, "CLE_RETIREES", None) == CLE_NEUVE)
    controle("masque v2 : les sept clés de base égales à celles du v1", mv2.CLES_CONFIGURATION == mv1.CLES_CONFIGURATION)

    # 5. Configuration B
    controle("configuration B : ses trois champs sont dans les dix champs de la v2",
             {confb["champ_refutation"], *confb["champs_voie"]} <= set(v2["champs"])
             and not ({confb["champ_refutation"], *confb["champs_voie"]} & set(retirees)))

    print(f"BILAN : {sum(resultats)} passés sur {len(resultats)}")
    return 0 if all(resultats) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
