#!/usr/bin/env python3
"""Contre-lecture Re-Search (modèle J) : sensibilités de M2 et de M4, et recomptage indépendant de M3.

Lecture seule des sources de l'analyse (S1, S2a, S2b), empreintes vérifiées ; aucun tirage aléatoire (déterministe) ;
aucun appel réseau ni de modèle. Ne qualifie aucune carte par un verdict de juge (N-058) : compte des formes et des essais.
Usage : python3 -I contre-lecture-re-search-organisme-v1-sensibilites.py S1_BOUCLE S2A S2B SORTIE.json
"""
import collections
import hashlib
import json
import sys

ATTENDUES = {
    "s1_boucle": "21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71",
    "s2a": "e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505",
    "s2b": "cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf",
}


def forme(o, entiers_masques=True):
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return o
    if isinstance(o, int):
        return "#" if entiers_masques else o
    if isinstance(o, float):
        return "#"
    if isinstance(o, list):
        return [forme(x, entiers_masques) for x in o]
    return {k: forme(v, entiers_masques) for k, v in o.items()}


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def charger(cle, chemin):
    with open(chemin, "rb") as f:
        brut = f.read()
    e = hashlib.sha256(brut).hexdigest()
    if e != ATTENDUES[cle]:
        print(f"REFUS : empreinte de {cle} : {e}", file=sys.stderr)
        sys.exit(2)
    return json.loads(brut.decode("utf-8"))


def s1(boucle):
    cartes = sorted(boucle["releve"]["cartes"], key=lambda c: (c["generation"], c["proposeur"], c["identifiant"]))
    out = {"cartes": len(cartes), "par_type": dict(sorted(collections.Counter(c["loi"]["type"] for c in cartes).items()))}
    for nom, masque in (("entiers_masques_definition_de_l_analyse", True), ("entiers_gardes", False)):
        fs = [canon(forme(c["loi"], masque)) for c in cartes]
        rep = []
        for i, c in enumerate(cartes):
            ant = {fs[j] for j, x in enumerate(cartes) if x["generation"] < c["generation"]
                   or (x["generation"] == c["generation"] and x["proposeur"] == c["proposeur"]
                       and x["identifiant"] < c["identifiant"])}
            rep.append(fs[i] in ant)
        par_type = collections.Counter(c["loi"]["type"] for c, r in zip(cartes, rep) if r)
        formes_par_type = collections.defaultdict(set)
        for c, f in zip(cartes, fs):
            formes_par_type[c["loi"]["type"]].add(f)
        n_soft = sum(c["loi"]["type"] == "softmax" for c in cartes)
        hors = sum(r for c, r in zip(cartes, rep) if c["loi"]["type"] != "softmax")
        out[nom] = {
            "formes_distinctes": len(set(fs)),
            "tailles_des_classes_de_forme": sorted(collections.Counter(fs).values(), reverse=True),
            "formes_distinctes_par_type": {k: len(v) for k, v in sorted(formes_par_type.items())},
            "repetent_definition_de_l_analyse": sum(rep), "part": round(sum(rep) / len(cartes), 6),
            "repetitions_par_type": dict(sorted(par_type.items())),
            "repetent_hors_softmax": hors, "cartes_hors_softmax": len(cartes) - n_soft,
            "part_hors_softmax_sur_cartes_hors_softmax": round(hors / (len(cartes) - n_soft), 6),
            "part_hors_softmax_sur_toutes_les_cartes": round(hors / len(cartes), 6),
            "repetent_toute_carte_anterieure_dans_l_ordre": sum(fs[i] in set(fs[:i]) for i in range(len(fs))),
        }
    return out


def s2(sortie):
    out = {"n_max": sortie["preenregistrement"]["plan"]["n_max"], "depense_usd": sortie["depense_usd"],
           "appels": sortie["appels"], "usd_par_appel": round(sortie["depense_usd"] / sortie["appels"], 6),
           "fin_utc": sortie["fin_utc"], "par_bras": {}}
    for bras in ("retour", "temoin"):
        ep = ap = et = at = 0
        props, rep, rep_g = collections.Counter(), collections.Counter(), collections.Counter()
        for s in sortie["suites"]:
            if s["condition"] != bras:
                continue
            vues, vues_g = set(), set()
            for t in s["tentatives"]:
                e = int(bool((t.get("verdict") or {}).get("promue")))
                if t["k"] <= 4:
                    ap += 1
                    ep += e
                else:
                    at += 1
                    et += e
                if t.get("loi") is None:
                    continue
                ty = t["loi"].get("type")
                f, g = canon(forme(t["loi"])), canon(forme(t["loi"], False))
                props[ty] += 1
                rep[ty] += f in vues
                rep_g[ty] += g in vues_g
                vues.add(f)
                vues_g.add(g)
        tot, r, rg = sum(props.values()), sum(rep.values()), sum(rep_g.values())
        out["par_bras"][bras] = {
            "m3_recompte_k_le_4": {"evenements_precoces": ep, "essais_precoces": ap, "evenements_tardifs": et,
                                   "essais_tardifs": at},
            "m4": {"propositions": tot, "repetees_ou_meme_forme": r, "part": round(r / tot, 6),
                   "entiers_gardes": {"repetees_ou_meme_forme": rg, "part": round(rg / tot, 6)},
                   "par_type_propositions": dict(sorted(props.items())), "par_type_repetitions": dict(sorted(rep.items())),
                   "hors_softmax": {"propositions": tot - props["softmax"], "repetitions": r - rep["softmax"],
                                    "part": round((r - rep["softmax"]) / (tot - props["softmax"]), 6)}}}
    return out


def principal():
    _, p1, pa, pb, sortie = sys.argv
    res = {"version": "contre-lecture-re-search-organisme-v1-sensibilites", "aleatoire": "aucun (déterministe)",
           "empreintes_sources_verifiees": ATTENDUES,
           "S1": s1(charger("s1_boucle", p1)), "S2a": s2(charger("s2a", pa)), "S2b": s2(charger("s2b", pb))}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("ÉCRIT", sortie)


if __name__ == "__main__":
    principal()
