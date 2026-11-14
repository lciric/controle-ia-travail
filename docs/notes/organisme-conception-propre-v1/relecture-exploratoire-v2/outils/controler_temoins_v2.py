#!/usr/bin/env python3
"""Contrôles par programme des témoins v2 (lecteur et hasard) — relecture exploratoire, règle v2.

Écrit le 14 novembre 2026 (vers 11:58 UTC, `date -u`) par le préparateur (modèle A). Applique les contrôles fixés
d'avance par `engagement-avant-epreuve-v2.md` (§ 5 et § 7) :

- **longueurs** : pour chaque champ libre, médiane des idées au hasard dans l'intervalle interquartile des fiches réelles ;
  longueur totale de chaque témoin (lecteur et hasard) entre le minimum et le maximum des fiches réelles ;
- **sans phrases-types** : aucune phrase d'au moins six mots commune à deux idées au hasard, ni entre une idée au hasard et
  un témoin du lecteur (champs de texte libre seulement : ni étiquettes, ni valeurs à liste fermée, ni antériorités) ;
  plus longue suite de mots commune à deux idées au hasard, sur les mêmes champs : au plus 12 mots ;
- **forme** : chaque témoin passe la vue servie et l'admissibilité de l'outil du lecteur (mêmes règles, recopiées ici) ;
  codes uniques ; familles et effectifs (7 publiées, 3 fausses, vrai, jumeau, 8 au hasard).

Rend un rapport JSON (nombres, codes et booléens ; aucun texte de fiche réelle : seules les statistiques de forme des fiches
réelles, déjà scellées, sont lues). Code de sortie 0 si tous les contrôles tiennent, 1 sinon.

Usage : python -I -B controler_temoins_v2.py --stats S.json --lecteur L.json --hasard H.json [--sortie R.json]
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
import statistics
import sys
from pathlib import Path

LEVIERS = ("levier:juge", "levier:proposeurs", "levier:composition", "levier:cout")
NATURES_ADMISES = ("modification", "ajout")
CHAMPS = ("nom", "enonce", "loi_predictive.espace_instances", "loi_predictive.prediction", "loi_predictive.metrique",
          "perte_traduction", "avantage.texte", "avantage.incopiable_parce_que", "originalite.texte",
          "demande_organisme.texte", "cout.ordre_de_grandeur", "piege", "cosmetique_si", "anteriorite.reference")
MOTS_PHRASE_MIN = 6
SUITE_MAX = 12
EFFECTIFS = {"publie": 7, "faux": 3, "vrai": 1, "jumeau": 1}


def feuilles(o) -> list[str]:
    if isinstance(o, str):
        return [o]
    if isinstance(o, list):
        return [t for x in o for t in feuilles(x)]
    if isinstance(o, dict):
        return [t for v in o.values() for t in feuilles(v)]
    return []


def longueur(f: dict, chemin: str) -> int:
    o = f
    for k in chemin.split("."):
        if isinstance(o, list):
            return sum(len(x.get(k, "")) for x in o if isinstance(x, dict))
        o = o.get(k) if isinstance(o, dict) else None
    return len(o) if isinstance(o, str) else 0


LIBRES = ("nom", "enonce", "loi_predictive.espace_instances", "loi_predictive.prediction", "loi_predictive.metrique",
          "perte_traduction", "avantage.texte", "avantage.incopiable_parce_que", "originalite.texte",
          "demande_organisme.texte", "cout.ordre_de_grandeur", "piege", "cosmetique_si")


def textes_libres(f: dict) -> list[str]:
    """Les seuls champs de texte libre (ni étiquettes, ni valeurs à liste fermée, ni antériorités)."""
    out = []
    for c in LIBRES:
        o = f
        for k in c.split("."):
            o = o.get(k) if isinstance(o, dict) else None
        if isinstance(o, str):
            out.append(o)
    return out


def mots(s: str) -> list[str]:
    return re.findall(r"\w+(?:['’]\w+)*", s.lower())


def phrases(f: dict) -> set[tuple[str, ...]]:
    """Phrases (coupées aux . ; ? ! et :) d'au moins six mots, normalisées en suites de mots minuscules."""
    out = set()
    for t in textes_libres(f):
        for p in re.split(r"[.;?!:]", t):
            m = tuple(mots(p))
            if len(m) >= MOTS_PHRASE_MIN:
                out.add(m)
    return out


def plus_longue_suite(a: list[str], b: list[str]) -> int:
    """Plus longue suite de mots consécutifs commune (programmation dynamique)."""
    meilleur, prec = 0, [0] * (len(b) + 1)
    for x in a:
        cour = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            if x == y:
                cour[j] = prec[j - 1] + 1
                meilleur = max(meilleur, cour[j])
        prec = cour
    return meilleur


def texte_mots(f: dict) -> list[str]:
    return [w for t in textes_libres(f) for w in mots(t) + ["¶"]]


def admissible(f: dict) -> bool:
    lev = [q for q in f.get("questions_servies", []) if isinstance(q, str) and q.strip() in LEVIERS]
    return len(lev) == 1 and (f.get("demande_organisme") or {}).get("nature") in NATURES_ADMISES


def controler(stats: dict, lecteur: dict, hasard: dict) -> dict:
    m = stats["fiches_reelles"]["mesures"]
    q, tot = m["longueur_par_champ"], m["longueur_totale_vue"]
    L, H = lecteur["temoins"], hasard["temoins"]
    res = {"controles": {}, "detail": {}}
    # longueurs
    med_h = {c: statistics.median(longueur(t["fiche"], c) for t in H) for c in CHAMPS}
    med_l = {c: statistics.median(longueur(t["fiche"], c) for t in L) for c in CHAMPS}
    hors_iqr_h = {c: med_h[c] for c in CHAMPS if not (q[c]["q1"] <= med_h[c] <= q[c]["q3"])}
    res["detail"]["mediane_par_champ"] = {c: {"reelles_q1": q[c]["q1"], "reelles_mediane": q[c]["mediane"],
                                              "reelles_q3": q[c]["q3"], "hasard": med_h[c], "lecteur": med_l[c]}
                                          for c in CHAMPS}
    totaux = {t["code"]: sum(len(x) for x in feuilles(t["fiche"])) for t in L + H}
    hors_bornes = {k: v for k, v in totaux.items() if not (tot["min"] <= v <= tot["max"])}
    res["detail"]["longueur_totale"] = {"reelles": {k: tot[k] for k in ("min", "q1", "mediane", "q3", "max")},
                                        "temoins": totaux}
    res["controles"]["hasard_medianes_dans_l_intervalle_interquartile"] = not hors_iqr_h
    res["detail"]["hasard_medianes_hors_intervalle"] = hors_iqr_h
    res["controles"]["totaux_entre_min_et_max_des_reelles"] = not hors_bornes
    res["detail"]["totaux_hors_bornes"] = hors_bornes
    # phrases communes et suites
    ph = {t["code"]: phrases(t["fiche"]) for t in L + H}
    communes_hh = {f"{a['code']}|{b['code']}": len(ph[a["code"]] & ph[b["code"]]) for a, b in itertools.combinations(H, 2)}
    communes_hl = {f"{a['code']}|{b['code']}": len(ph[a["code"]] & ph[b["code"]]) for a in H for b in L}
    res["controles"]["aucune_phrase_commune_entre_idees_au_hasard"] = not any(communes_hh.values())
    res["controles"]["aucune_phrase_commune_hasard_et_lecteur"] = not any(communes_hl.values())
    res["detail"]["phrases_communes_non_nulles"] = {k: v for k, v in {**communes_hh, **communes_hl}.items() if v}
    tm = {t["code"]: texte_mots(t["fiche"]) for t in H}
    suites = {f"{a['code']}|{b['code']}": plus_longue_suite(tm[a["code"]], tm[b["code"]])
              for a, b in itertools.combinations(H, 2)}
    res["controles"]["plus_longue_suite_commune_au_plus_12_mots"] = max(suites.values()) <= SUITE_MAX
    res["detail"]["plus_longue_suite_commune"] = {"maximum": max(suites.values()), "par_paire": suites}
    # forme
    codes = [t["code"] for t in L + H]
    res["controles"]["codes_uniques"] = len(set(codes)) == len(codes)
    eff = {}
    for t in L:
        eff[t["famille"]] = eff.get(t["famille"], 0) + 1
    res["controles"]["effectifs_du_lecteur"] = eff == EFFECTIFS
    res["controles"]["huit_idees_au_hasard"] = len(H) == 8 and all(t["famille"] == "hasard" for t in H)
    res["controles"]["tous_admissibles"] = all(admissible(t["fiche"]) for t in L + H)
    res["controles"]["publiees_avec_entree"] = all(t.get("entree") in [f"C{i}" for i in range(1, 13)]
                                                   for t in L if t["famille"] == "publie")
    res["controles"]["fausses_avec_cible"] = sorted(t.get("cible") for t in L if t["famille"] == "faux") == ["R1", "R2",
                                                                                                         "R3"]
    res["detail"]["effectifs_du_lecteur"] = eff
    res["tient"] = all(res["controles"].values())
    return res


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--stats", required=True)
    a.add_argument("--lecteur", required=True)
    a.add_argument("--hasard", required=True)
    a.add_argument("--sortie")
    args = a.parse_args(argv)
    entrees = {k: Path(getattr(args, k)) for k in ("stats", "lecteur", "hasard")}
    donnees = {k: json.loads(p.read_bytes()) for k, p in entrees.items()}
    r = controler(donnees["stats"], donnees["lecteur"], donnees["hasard"])
    r = {"outil": {"chemin": Path(__file__).name, "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
         "entrees": {k: {"chemin": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for k, p in entrees.items()},
         **r}
    texte = json.dumps(r, ensure_ascii=False, indent=1) + "\n"
    if args.sortie:
        s = Path(args.sortie)
        if s.exists():
            print(f"{s} existe déjà (R12)", file=sys.stderr)
            return 2
        s.write_text(texte, encoding="utf-8")
    print(json.dumps({"tient": r["tient"], "controles": r["controles"]}, ensure_ascii=False))
    return 0 if r["tient"] else 1


if __name__ == "__main__":
    sys.exit(main())
