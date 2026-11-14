#!/usr/bin/env python3
"""Statistiques de forme des fiches de la course « conception propre » — v1 (relecture exploratoire v2).

Écrit le 14 novembre 2026 (11:28 UTC, `date -u`) par le préparateur de la relecture exploratoire (modèle A). But : donner le
gabarit (longueurs par champ, nombre de champs, valeurs des champs à liste fermée, quelques mesures de style) des fiches
réelles admissibles, pour écrire les témoins v2 et régler le générateur de hasard v2 **sans lire le contenu des fiches**.

**Aucun texte de fiche n'est affiché ni écrit** : seules sortent des longueurs (caractères, mots), des comptes, des
quantiles, et les valeurs des champs à liste fermée du gabarit de l'orchestrateur (`type`, `signe`, `avantage.source`,
`originalite.niveau`, `demande_organisme.nature`, `cout.nature`, `anteriorite[].statut`) ; une valeur hors de sa liste fermée
est comptée « hors_liste », jamais montrée. Les étiquettes de `questions_servies` sont comptées par classe (levier nommé de
la liste fermée, `QOn`, `Qn`, `nouvelle`, `Q-pont`, autre), jamais recopiées hors de ces classes. Aucun identifiant de
fiche ni d'auteur n'est écrit : les mesures par fiche sont rendues triées, sans clé.

Même règle d'admissibilité que l'outil du lecteur (§ 4.1 de la conception) : exactement une étiquette de levier, demande
`modification` ou `ajout`. Les témoins v1 et v2 (fichiers du dépôt, non secrets) sont mesurés de la même façon, pour
comparaison.

Usage : python -I -B stats_forme_fiches_v1.py --fiches F.json [--temoins T.json …] --sortie S.json   (S absent : jamais
écrasé). Aucun réseau, aucun appel.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import sys
from pathlib import Path

LEVIERS = ("levier:juge", "levier:proposeurs", "levier:composition", "levier:cout")
NATURES_ADMISES = ("modification", "ajout")
FERMES = {
    "type": ("question", "approche"),
    "loi_predictive.signe": ("+", "-", "0"),
    "avantage.source": ("organisme", "programme", "methodes", "aucune"),
    "originalite.niveau": ("inedite", "transposition", "occupee"),
    "demande_organisme.nature": ("rien", "modification", "ajout"),
    "cout.nature": ("processeur", "depense"),
}
STATUTS = ("RAPPORTE", "SUPPOSE", "MOISSONNE")
# champs textuels libres (chemin → clés), dans l'ordre du gabarit
LIBRES = ("nom", "enonce", "loi_predictive.espace_instances", "loi_predictive.prediction", "loi_predictive.metrique",
          "perte_traduction", "avantage.texte", "avantage.incopiable_parce_que", "originalite.texte",
          "demande_organisme.texte", "cout.ordre_de_grandeur", "piege", "cosmetique_si", "anteriorite.reference")
# les six champs de la mesure de l'audit (`audit-proprete-lecture-g1-v3-1-v1.md`, § 1) : feuilles textuelles sommées
SIX = ("enonce", "loi_predictive", "demande_organisme", "cout", "perte_traduction", "piege")


def feuilles(o) -> list[str]:
    if isinstance(o, str):
        return [o]
    if isinstance(o, list):
        return [t for x in o for t in feuilles(x)]
    if isinstance(o, dict):
        return [t for v in o.values() for t in feuilles(v)]
    return []


def valeur(f: dict, chemin: str):
    o = f
    for k in chemin.split("."):
        if isinstance(o, list):
            return [x.get(k) if isinstance(x, dict) else None for x in o]
        o = o.get(k) if isinstance(o, dict) else None
    return o


def longueur(f: dict, chemin: str) -> int:
    v = valeur(f, chemin)
    if isinstance(v, list):
        return sum(len(x) for x in v if isinstance(x, str))
    return len(v) if isinstance(v, str) else 0


def leviers(f: dict) -> list[str]:
    return [q for q in f.get("questions_servies", []) if isinstance(q, str) and q.strip() in LEVIERS]


def admissible(f: dict) -> bool:
    return len(leviers(f)) == 1 and (f.get("demande_organisme") or {}).get("nature") in NATURES_ADMISES


def classe_etiquette(q: str) -> str:
    q = q.strip()
    if q in LEVIERS:
        return q
    for motif, nom in ((r"QO\d{1,2}", None), (r"Q\d{1,2}", None)):
        if re.fullmatch(motif, q):
            return q
    if q in ("nouvelle", "Q-pont"):
        return q
    return "autre"


PHRASE = re.compile(r"[^.!?;]+[.!?;]?")


def style(textes: list[str]) -> dict:
    """Mesures de style, sur la concaténation des champs libres (nombres seulement)."""
    t = " ".join(textes)
    mots = re.findall(r"\w+(?:[’'-]\w+)*", t)
    phrases = [p for p in PHRASE.findall(t) if re.search(r"\w", p)]
    long_phr = [len(re.findall(r"\w+", p)) for p in phrases]
    return {"caracteres": len(t), "mots": len(mots), "phrases": len(phrases),
            "mots_par_phrase_moyenne": round(sum(long_phr) / len(long_phr), 2) if long_phr else 0.0,
            "part_chiffres": round(sum(c.isdigit() for c in t) / len(t), 4) if t else 0.0,
            "pourcent": t.count("%"), "parentheses": t.count("("), "points_virgules": t.count(";"),
            "deux_points": t.count(":"), "guillemets": t.count("«") + t.count('"'),
            "mots_distincts_sur_mots": round(len({m.lower() for m in mots}) / len(mots), 4) if mots else 0.0}


def quantiles(xs: list) -> dict:
    if not xs:
        return {"n": 0}
    s = sorted(xs)
    q = statistics.quantiles(s, n=4, method="inclusive") if len(s) > 1 else [s[0]] * 3
    return {"n": len(s), "min": s[0], "q1": round(q[0], 2), "mediane": round(statistics.median(s), 2),
            "q3": round(q[2], 2), "max": s[-1], "moyenne": round(sum(s) / len(s), 2)}


def mesurer(fiches: list[dict]) -> dict:
    par_champ = {c: [] for c in LIBRES}
    six, totaux, nb_champs, nb_feuilles, nb_ant, nb_qs = [], [], [], [], [], []
    fermes = {c: {} for c in FERMES}
    statuts, etiquettes = {}, {}
    styles = []
    for f in fiches:
        for c in LIBRES:
            par_champ[c].append(longueur(f, c))
        six.append(sum(len(x) for c in SIX for x in feuilles(f.get(c))))
        vue = {k: v for k, v in f.items() if k not in ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin")}
        totaux.append(sum(len(x) for x in feuilles(vue)))
        nb_champs.append(len(vue))
        nb_feuilles.append(len(feuilles(vue)))
        ant = f.get("anteriorite") if isinstance(f.get("anteriorite"), list) else []
        nb_ant.append(len(ant))
        qs = f.get("questions_servies") if isinstance(f.get("questions_servies"), list) else []
        nb_qs.append(len(qs))
        for c, permis in FERMES.items():
            v = valeur(f, c)
            k = v if v in permis else "hors_liste"
            fermes[c][k] = fermes[c].get(k, 0) + 1
        for a in ant:
            s = a.get("statut") if isinstance(a, dict) else None
            k = s if s in STATUTS else "hors_liste"
            statuts[k] = statuts.get(k, 0) + 1
        for q in qs:
            k = classe_etiquette(q) if isinstance(q, str) else "autre"
            etiquettes[k] = etiquettes.get(k, 0) + 1
        styles.append(style([x for c in LIBRES for x in ([valeur(f, c)] if not isinstance(valeur(f, c), list)
                                                          else valeur(f, c)) if isinstance(x, str)]))
    return {
        "fiches": len(fiches),
        "longueur_par_champ": {c: quantiles(v) for c, v in par_champ.items()},
        "longueur_six_champs_de_l_audit": quantiles(six),
        "longueur_totale_vue": quantiles(totaux),
        "longueurs_totales_triees": sorted(totaux),
        "nombre_de_champs": quantiles(nb_champs),
        "nombre_de_feuilles_textuelles": quantiles(nb_feuilles),
        "nombre_d_anteriorites": quantiles(nb_ant),
        "nombre_d_etiquettes_questions_servies": quantiles(nb_qs),
        "champs_a_liste_fermee": fermes,
        "statuts_d_anteriorite": statuts,
        "classes_d_etiquettes": etiquettes,
        "style": {k: quantiles([s[k] for s in styles]) for k in (styles[0] if styles else {})},
    }


def main() -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--fiches", required=True, help="fiches validées (liste) : seules les admissibles sont mesurées")
    a.add_argument("--temoins", action="append", default=[], help="fichier de témoins {temoins: [{code, fiche}]}")
    a.add_argument("--sortie", required=True)
    args = a.parse_args()
    sortie = Path(args.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 2
    brut = Path(args.fiches).read_bytes()
    fiches = json.loads(brut)
    if not isinstance(fiches, list):
        print("fiches : liste attendue", file=sys.stderr)
        return 2
    adm = [f for f in fiches if isinstance(f, dict) and admissible(f)]
    res = {"outil": {"chemin": Path(__file__).name, "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
           "versions": {"python": sys.version.split()[0]},
           "fiches_reelles": {"chemin": args.fiches, "sha256": hashlib.sha256(brut).hexdigest(), "validees": len(fiches),
                              "admissibles": len(adm), "mesures": mesurer(adm)},
           "temoins": {}}
    for t in args.temoins:
        b = Path(t).read_bytes()
        d = json.loads(b)
        fs = [x["fiche"] for x in d["temoins"]]
        res["temoins"][Path(t).name] = {"sha256": hashlib.sha256(b).hexdigest(), "mesures": mesurer(fs)}
    sortie.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    m = res["fiches_reelles"]["mesures"]
    print(json.dumps({"admissibles": len(adm), "six_champs_mediane": m["longueur_six_champs_de_l_audit"]["mediane"]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
