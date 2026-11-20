"""Garde de la graphie de `lignee_reconnue` dans une lecture du rejeu des critères v7 — v2.

v2 : couples A et B de la contre-lecture Fable (`e76981b9…`) appliqués à la lettre ; en plus, une liste de
veto passée seule (liste nue, comme les listes des juges données à part au programme d'assemblage) est gardée
de même (point relevé par la même contre-lecture).

Écrit par la mère (session_01XJ6Mgr8BN6UanALsQatc5E) le 20 novembre 2026. Instrument ajouté devant les
trois programmes scellés du juge de sélection : il ne les remplace pas et ne les modifie pas.

Pourquoi. Le programme d'assemblage (`assemblage_selection_v4_v2.py`, `2f5640da…`) ne contrôle que la
présence d'un texte dans `lignee_reconnue` (l. 226, l. 240), puis compte la famille par `familles.get`.
Une graphie fautive (« Opus » au lieu de `prop-opus`) y serait comptée en silence comme « ne reconnaît
pas sa famille ». Cette garde, jouée sur chaque lecture déposée avant `assembler`, refuse toute valeur
qui n'est pas une clé de `familles` du manifeste ou « aucune ».

Ce qu'elle lit : le manifeste (sa seule clé `familles`) et une lecture (ses clés `lignee`, `cartes`,
`veto`, et dans chaque carte et chaque veto les seules clés `id` et `lignee_reconnue`).
Ce qu'elle écrit : des comptes et des identifiants de cartes. Jamais une note, une phrase, une raison,
ni la valeur fautive elle-même.

Codes de sortie : 0 conforme ; 1 au moins une graphie refusée ; 2 manifeste ou lecture mal formés.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VERSION = "garde_lignee_reconnue_v2"
AUCUNE = "aucune"
MOTIF_ID = re.compile(r"[A-Za-z0-9._:/-]{1,120}")


class Malforme(Exception):
    pass


def permis_depuis_manifeste(manifeste) -> set[str]:
    if not isinstance(manifeste, dict) or not isinstance(manifeste.get("familles"), dict) or not manifeste["familles"]:
        raise Malforme("manifeste : table « familles » absente ou vide")
    cles = set(manifeste["familles"])
    if not all(isinstance(k, str) and k for k in cles):
        raise Malforme("manifeste : clé de « familles » non textuelle")
    if AUCUNE in cles:
        raise Malforme("manifeste : « aucune » ne peut pas être une lignée")
    return cles


def controler(lecture, permis: set[str]) -> dict:
    if isinstance(lecture, list):
        # Liste de veto passée seule : aucune lignée de lecteur, aucune carte.
        r = controler({"lignee": sorted(permis)[0], "cartes": [], "veto": lecture}, permis)
        r["refus"]["lignee_du_lecteur"] = False
        r["forme"] = "liste_de_veto"
        r["nombre_de_refus"] = len(r["refus"]["veto"])
        r["issue"] = "conforme" if r["nombre_de_refus"] == 0 and r["entrees_sans_identifiant"] == 0 else "refusee"
        return r
    if not isinstance(lecture, dict):
        raise Malforme("lecture : objet attendu")
    for k in ("lignee", "cartes", "veto"):
        if k not in lecture:
            raise Malforme(f"lecture : clé « {k} » absente")
    if not isinstance(lecture["cartes"], list) or not isinstance(lecture["veto"], list):
        raise Malforme("lecture : « cartes » et « veto » doivent être des listes")
    refus = {"lignee_du_lecteur": not (isinstance(lecture["lignee"], str) and lecture["lignee"] in permis), "cartes": [], "veto": []}
    sans_id = 0
    for nom in ("cartes", "veto"):
        for i, e in enumerate(lecture[nom]):
            if not isinstance(e, dict):
                raise Malforme(f"lecture : entrée {i} de « {nom} » mal formée")
            ident = e.get("id")
            if not (isinstance(ident, str) and MOTIF_ID.fullmatch(ident)):
                sans_id += 1
                ident = f"<position {i}>"
            v = e.get("lignee_reconnue")
            if not (isinstance(v, str) and (v in permis or v == AUCUNE)):
                refus[nom].append(ident)
    n_refus = len(refus["cartes"]) + len(refus["veto"]) + (1 if refus["lignee_du_lecteur"] else 0)
    return {
        "cartes": len(lecture["cartes"]),
        "veto": len(lecture["veto"]),
        "entrees_sans_identifiant": sans_id,
        "refus": refus,
        "nombre_de_refus": n_refus,
        "issue": "conforme" if n_refus == 0 and sans_id == 0 else "refusee",
    }


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--manifeste", required=True, type=Path)
    p.add_argument("--lecture", required=True, type=Path)
    p.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    rapport = {"version": VERSION, "manifeste": str(a.manifeste), "lecture": str(a.lecture)}
    try:
        permis = permis_depuis_manifeste(json.loads(a.manifeste.read_text(encoding="utf-8")))
        rapport["etiquettes_permises"] = sorted(permis) + [AUCUNE]
        rapport.update(controler(json.loads(a.lecture.read_text(encoding="utf-8")), permis))
        code = 0 if rapport["issue"] == "conforme" else 1
    except (Malforme, json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
        rapport["issue"] = "mal_formee"
        rapport["motif"] = f"{type(e).__name__} : {e}"
        code = 2
    a.sortie.parent.mkdir(parents=True, exist_ok=True)
    a.sortie.write_text(json.dumps(rapport, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{rapport['issue']} code={code} sortie={a.sortie}")
    return code


if __name__ == "__main__":
    sys.exit(principal())
