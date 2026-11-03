#!/usr/bin/env python3
"""Trace agrégée de la course Kirchner Q2 (comptes, coûts, mariages par bras) — v1, dérivée de `nuit/trace_agregee_mini_course_v2.py`.
(Kit Kirchner Q2, v1, dérivé à l'octet près des substitutions de nom du kit Heimersheim — branche outils/course-heimersheim-v1 — par un sous-agent de session-depot, 3 novembre 2026 ; les mentions de versions antérieures ci-dessous sont celles du kit Heimersheim.)

Rédigé le 3 novembre 2026 (sous-agent de session-depot) ; aucun appel. Lit, APRÈS la course et le scellement de la sortie, le
dossier du run, et rend des **comptes, statuts et coûts** — jamais une fiche, un titre, une consigne, une réponse ou un motif en
texte libre (les fiches elles-mêmes restent dans `course/generation-1/fiches.json`, scellé, pour la lecture de Lazar).

Trois barrières, dans cet ordre, avant toute écriture (celles de la mini-course) :
1. liste blanche des clés (`CLES`) et des chaînes (valeurs fixes, étiquettes de la configuration, modèles, étapes, bras, noms
   d'exception, causes codées du noyau) ;
2. contrôle anti-fuite : refus si la trace contient un canari (configuration `canaris`, plus `--canari`), un titre de fiche
   (lot et fusions archivées) ou une suite de six mots tirée d'une fiche ;
3. garde testée (R5) à chaque exécution : cas sain accepté, trois artefacts (canari, titre, suite de six mots) refusés.

Sortie : `trace-agregee-course-kirchner-v1.json` + `.sha256` dans le dossier du run (jamais écrasée, R12).
`--artefacts-sur-run` : épreuve anti-fuite sur le run réel (la trace du run, munie d'un canari, d'un titre, puis d'une suite
de six mots réels, doit être refusée chaque fois). Codes : 0 écrite (ou épreuve conforme) ; 3 refusée ; 2 autre refus.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

VERSION = "trace-agregee-course-kirchner-v1"
NOM_TRACE = "trace-agregee-course-kirchner-v1.json"
CLES = {"version", "variante", "l1", "fin", "motif_arret", "noeud", "appels", "par_etape", "par_role", "par_modele", "par_fournisseur",
        "couts_usd", "fiches", "proposees_par_proposeur", "refusees_au_format", "passeports", "refus_aiguilleur", "exclues_a4",
        "lectures_rejetees", "bras", "produit", "cause", "paires_par_bras", "fusions_par_bras", "fusions", "completes", "inachevees",
        "causes", "classement", "lignes", "notables", "registre", "regle_usd", "engage_usd", "depassements_reserve",
        "controle_anti_fuite", "resultat", "canaris", "titres", "suites", "garde", "cas_sain", "artefacts", "roles_arretes",
        "temoins_plantes", "etapes", "relais", "appels_relais", "depense_relais_usd", "total_usd", "x"}
VALEURS = {"fini", "arret", "noeud_c13", "aucun", "conforme", "refuse", "jouee", "retiree", "non mesuré (budget)", "aucun (constat)"}
MOTIF_SUR = re.compile(r"^[A-Za-zÀ-ÿ0-9_.\-]{1,60}$")
CAUSES = re.compile(r"^(non produit|non écrite|non mesur|sans passeport|incohérente|jugée en partie|non jugée|exclue par A4|étape des fusions)")


def mots(texte):
    t = unicodedata.normalize("NFKD", str(texte)).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", t)


def chaines(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from chaines(v)
    elif isinstance(o, list):
        for v in o:
            yield from chaines(v)


def suites(liste, n=6):
    return {" ".join(liste[i:i + n]) for i in range(len(liste) - n + 1)}


def controle_anti_fuite(trace, canaris, contenus, titres):
    plat = "\n".join(chaines(trace))
    plat_mots = " ".join(mots(plat))
    can = sorted(c for c in canaris if c and c in plat)
    tit = sorted(t for t in titres if t and len(t) >= 8 and " ".join(mots(t)) and " ".join(mots(t)) in plat_mots)
    sui = set()
    for c in contenus:
        for s in suites(mots(json.dumps(c, ensure_ascii=False))):
            if s in plat_mots:
                sui.add(s)
    ok = not (can or tit or sui)
    return {"resultat": "conforme" if ok else "refuse", "canaris": len(can), "titres": len(tit), "suites": len(sui)}


def tester_garde():
    fiche = {"titre": "Une fiche factice sur la dose et le plateau", "hypothese": "alpha beta gamma delta epsilon zeta eta theta"}
    propre = {"version": VERSION, "fiches": {"proposees_par_proposeur": {"prop-fable": 8}}}
    can = "KQ2-ESSAI-00000000"
    sain = controle_anti_fuite(propre, [can], [fiche], [fiche["titre"]])["resultat"] == "conforme"
    a1 = controle_anti_fuite(dict(propre, fin=can), [can], [fiche], [fiche["titre"]])["resultat"] == "refuse"
    a2 = controle_anti_fuite(dict(propre, fin=fiche["titre"]), [can], [fiche], [fiche["titre"]])["resultat"] == "refuse"
    a3 = controle_anti_fuite(dict(propre, fin="beta gamma delta epsilon zeta eta"), [can], [fiche], [])["resultat"] == "refuse"
    return {"cas_sain": sain, "artefacts": [a1, a2, a3]}


def valider_liste_blanche(o, permises, chemin="trace"):
    if isinstance(o, dict):
        for k, v in o.items():
            if k not in CLES and k not in permises and not CAUSES.match(str(k)):
                raise ValueError(f"clé hors liste blanche : {chemin}.{k}")
            valider_liste_blanche(v, permises, f"{chemin}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            valider_liste_blanche(v, permises, f"{chemin}[{i}]")
    elif isinstance(o, str):
        if not (o in VALEURS or o in permises or CAUSES.match(o) or MOTIF_SUR.match(o)):
            raise ValueError(f"chaîne hors liste blanche : {chemin} = {o[:40]!r}")


def lire(chemin, defaut=None):
    if not os.path.isfile(chemin):
        return defaut
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def permises_de(conf):
    p = {x["etiquette"] for x in conf["proposeurs"] + conf["juges"] + conf["lecteurs_etiquettes"]}
    p |= {conf["aiguilleur"]["etiquette"], conf["bisociateur"]["metteur_fusion"]["etiquette"], "plafond-relais", "coupure", "a14"}
    p |= {x["modele"] for x in conf["proposeurs"] + conf["juges"] + conf["lecteurs_etiquettes"]}
    p |= {conf["aiguilleur"]["modele"], conf["bisociateur"]["metteur_fusion"]["modele"], conf.get("variante", "")}
    p |= set(conf.get("fournisseurs") or {}) | {e["nom"] for e in conf["budget"]["etapes"]} | {"gu_krenn", "basique", "meta"}
    return p


def agreger(run, conf):
    g = os.path.join(run, "course", "generation-1")
    bilan = lire(os.path.join(run, "course", "bilan-course.json"), {}) or {}
    fin = lire(os.path.join(g, "manifeste-fin.json"), {}) or {}
    cons = (lire(os.path.join(g, "consommations.json"), {}) or {}).get("consommations", [])
    fiches = lire(os.path.join(g, "fiches.json"), {}) or {}
    aig = lire(os.path.join(g, "aiguillage", "journal-aiguillage.json"), {}) or {}
    pref = conf["graines"]["prefixe"]
    paires = lire(os.path.join(g, "coffre", f"{pref}-paires-par-bras.json"), {}) or {}
    cle_bras = lire(os.path.join(g, "coffre", f"{pref}-cle-bras.json"), {}) or {}
    classement = lire(os.path.join(g, "classement.json"), {}) or {}
    arret = bilan.get("arret")
    motif = re.sub(r"[^A-Za-z]", "", str(arret).split(" ")[0])[:60] if arret else "aucun"
    appels = [c for c in cons if c.get("modele_demande")]
    compte = lambda cle: {k: sum(1 for c in appels if c.get(cle) == k) for k in sorted({c.get(cle) for c in appels})}  # noqa: E731
    couts = {}
    for c in appels:
        couts[c["modele_demande"]] = round(couts.get(c["modele_demande"], 0.0) + float(c.get("cout_usd") or 0.0), 6)
    evs = fin.get("evenements") or []
    proposees = {}
    for f in fiches.values():
        m = f.get("meta") or {}
        if m.get("origine") != "fusion":
            proposees[m.get("proposeur")] = proposees.get(m.get("proposeur"), 0) + 1
    fus_bras = {}
    for v in cle_bras.values():
        fus_bras[v["bras"]] = fus_bras.get(v["bras"], 0) + 1
    reg_ = None
    p_reg = os.path.join(run, "registre-depense-cumulee-v1.jsonl")
    if os.path.isfile(p_reg):
        lignes = [json.loads(l) for l in open(p_reg, encoding="utf-8") if l.strip()]
        fins = [l for l in lignes if l.get("type") == "fin"]
        reg_ = {"regle_usd": round(sum(float(l.get("cout_usd") or 0) for l in fins), 6),
                "engage_usd": round(sum(float(l.get("pire_cas_usd") or 0) for l in lignes if l.get("type") == "debut")
                                    - sum(float(l.get("pire_cas_usd") or 0) for l in lignes if l.get("type") == "debut"
                                          and l.get("id") in {x.get("id") for x in fins}), 6),
                "depassements_reserve": sum(1 for l in fins if l.get("depassement_reserve"))}
    relais = {}
    for f in sorted(conf.get("fournisseurs") or {}):
        e = lire(os.path.join(run, f"etat-final-relais-{f}.json"))
        if isinstance(e, dict):
            relais[f] = {"appels_relais": e.get("appels"), "depense_relais_usd": e.get("depense_usd")}
    return {"version": VERSION, "variante": conf.get("variante"),
            "l1": {"fin": "arret" if arret else ("noeud_c13" if bilan.get("noeud") else "fini"), "motif_arret": motif or "aucun",
                   "noeud": bool(bilan.get("noeud"))},
            "temoins_plantes": "aucun (constat)",
            "appels": {"par_etape": compte("etape"), "par_role": compte("role"), "par_modele": compte("modele_demande"),
                       "par_fournisseur": compte("fournisseur")},
            "couts_usd": dict(couts, total_usd=round(sum(couts.values()), 6)),
            "fiches": {"proposees_par_proposeur": proposees,
                       "refusees_au_format": sum(1 for e in evs if e.get("evenement") == "fiche-refusee"),
                       "passeports": aig.get("passeports"), "refus_aiguilleur": aig.get("refus_aiguilleur"),
                       "exclues_a4": len(fin.get("exclues_a4") or {}),
                       "lectures_rejetees": sum(1 for e in evs if e.get("evenement") in ("lecture-rejetee", "etiquette-rejetee"))},
            "bras": {b: {"produit": bool(d.get("produit")), "cause": d.get("cause") or (fin.get("non_produits") or {}).get(b) or "aucun"}
                     for b, d in (fin.get("bras") or {}).items()},
            "paires_par_bras": {b: len(v) for b, v in (paires.get("paires") or {}).items()},
            "fusions_par_bras": fus_bras,
            "fusions": {"completes": (fin.get("fusions") or {}).get("completes"), "inachevees": (fin.get("fusions") or {}).get("inachevees"),
                        "causes": (fin.get("fusions") or {}).get("causes") or {}},
            "classement": {"lignes": len(classement.get("lignes") or []),
                           "notables": sum(1 for l in classement.get("lignes") or [] if l.get("notable"))},
            "roles_arretes": sorted((fin.get("roles_arretes") or {}).keys()),
            "etapes": fin.get("etapes") or {}, "registre": reg_, "relais": relais}


def contenus_et_titres(run, conf):
    g = os.path.join(run, "course", "generation-1")
    fiches = lire(os.path.join(g, "fiches.json"), {}) or {}
    arch = (lire(os.path.join(g, "fusions-inachevees.json"), {}) or {}).get("fusions", [])
    contenus = [f["contenu"] for f in fiches.values()] + [a["contenu"] for a in arch if a.get("contenu")]
    titres = [str(c.get(conf["champ_titre"], "")) for c in contenus if isinstance(c, dict)]
    return contenus, titres


def ecrire_neuf_scelle(chemin, objet):
    if os.path.exists(chemin):
        raise FileExistsError(f"{chemin} existe déjà (R12)")
    b = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "wb") as f:
        f.write(b)
    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{hashlib.sha256(b).hexdigest()}  {os.path.basename(chemin)}\n")


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--run")
    a.add_argument("--configuration")
    a.add_argument("--canari", action="append", default=[])
    a.add_argument("--sortie")
    a.add_argument("--tester-garde", action="store_true")
    a.add_argument("--artefacts-sur-run", action="store_true")
    args = a.parse_args(argv)
    garde = tester_garde()
    if args.tester_garde:
        print(json.dumps(garde))
        return 0 if garde["cas_sain"] and all(garde["artefacts"]) else 2
    if not (garde["cas_sain"] and all(garde["artefacts"])):
        print("garde anti-fuite en échec (R5) : aucune trace", file=sys.stderr)
        return 2
    if not args.run or not os.path.isdir(args.run) or not args.configuration:
        print("--run (dossier existant) et --configuration exigés", file=sys.stderr)
        return 2
    with open(args.configuration, encoding="utf-8") as f:
        conf = json.load(f)
    canaris = list((conf.get("canaris") or {}).values()) + list(args.canari)
    trace = agreger(args.run, conf)
    contenus, titres = contenus_et_titres(args.run, conf)
    permises = permises_de(conf)
    if args.artefacts_sur_run:
        essais = [dict(trace, fin=canaris[0] if canaris else "KQ2-X")]
        if titres:
            essais.append(dict(trace, fin=titres[0]))
        m = [w for c in contenus for w in [mots(json.dumps(c, ensure_ascii=False))] if len(w) >= 6]
        if m:
            essais.append(dict(trace, fin=" ".join(m[0][:6])))
        res = [controle_anti_fuite(t, canaris, contenus, titres)["resultat"] for t in essais]
        ok = all(r == "refuse" for r in res) and controle_anti_fuite(trace, canaris, contenus, titres)["resultat"] == "conforme"
        print(f"{'conforme' if ok else 'ÉCHEC'} : {len(res)} artefacts sur le run, refusés : {sum(r == 'refuse' for r in res)} ; trace du run "
              f"{controle_anti_fuite(trace, canaris, contenus, titres)['resultat']}")
        return 0 if ok else 3
    try:
        valider_liste_blanche(trace, permises)
    except ValueError as e:
        print(f"trace refusée (liste blanche) : {e}", file=sys.stderr)
        return 3
    c = controle_anti_fuite(trace, canaris, contenus, titres)
    trace["controle_anti_fuite"] = dict(c, garde=garde)
    if c["resultat"] != "conforme":
        print(f"trace refusée (anti-fuite) : {c}", file=sys.stderr)
        return 3
    sortie = args.sortie or os.path.join(args.run, NOM_TRACE)
    ecrire_neuf_scelle(sortie, trace)
    print(f"trace écrite : {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
