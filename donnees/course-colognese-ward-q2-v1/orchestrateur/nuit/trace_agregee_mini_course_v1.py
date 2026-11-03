#!/usr/bin/env python3
"""Agrégateur de la trace publique de la mini-course (Kimi et Argon seuls, GO-2026-11-01-12) — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé par le rédacteur. Adaptation 5 du devis : la
**seule** pièce qui écrit la trace publique. Elle lit, après la course, le dossier du run (sous `donnees/`, exclu de la copie
publique) et rend des **comptes, statuts, coûts et verdicts sous identifiant opaque avec la famille du juge** — jamais une
fiche, un titre, une consigne, une réponse ou un motif en texte libre.

Trois barrières, dans cet ordre, avant toute écriture :

1. **Liste blanche** (`valider_liste_blanche`) : chaque clé de la trace est dans `CLES` ; chaque chaîne est une valeur fixe
   (`VALEURS`), une étiquette de rôle ou un nom d'étape de la configuration, un identifiant opaque `v01`…, ou un nom
   d'exception (lettres seules) ; nombres, booléens et `null` passent ; tout le reste refuse la trace.
2. **Contrôle anti-fuite** (`controle_anti_fuite`) : refus si la trace contient un **canari** (chaîne unique de chaque
   consigne, configuration `canaris`, plus `--canari` en répétition), un **titre** de fiche (fiches du lot et fusions
   archivées), ou une **suite de six mots** tirée d'une fiche (mots normalisés : minuscules, sans accents, `[a-z0-9]+`).
3. **Garde testée** (R5) à chaque exécution, avant l'agrégat : cas sain (trace propre acceptée) et trois artefacts (canari,
   titre, suite de six mots injectés : chacun refusé). Un échec de la garde refuse l'écriture.

Sortie : `trace-agregee-mini-course-v1.json` et son compagnon `.sha256` (R6) dans le dossier du run ; `--sortie` pour un
autre chemin neuf (R12 : jamais écrasé). Codes : 0 trace écrite ; 3 trace refusée (liste blanche ou anti-fuite) ; 2 autre
refus (dossier illisible, garde en échec). Bibliothèque standard seulement.

Critères servis (préenregistrement, L1 à L4) : L1 fin ou arrêt sur un motif codé ; L2 comptes par étape ; L3 part de fiches
« notables » par juge et selon la règle d'agrégation, accord entre les deux juges ; L4 écart entre juge de la même famille et
juge de l'autre famille (réserve, jamais une revendication).

  python3 -I -B trace_agregee_mini_course_v1.py --run RUN --configuration CONF [--canari CHAINE …] [--sortie FICHIER]
  python3 -I -B trace_agregee_mini_course_v1.py --tester-garde
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import registre_depense_cumulee_v1 as reg  # noqa: E402

VERSION = "trace-agregee-mini-course-v1"
NOM_TRACE = "trace-agregee-mini-course-v1.json"
NOM_REGISTRE = "registre-depense-cumulee-v1.jsonl"
FAMILLES = {"kimi": "kimi", "argon": "argon"}
ETATS_ETAPE = ("jouee", "retiree", "non_mesuree_budget", "non_lancee_hors_porte", "non_mesuree_hors_porte",
               "non_mesuree_technique", "non_jouee", "hors_scenario_b")
CLASSES_FIN = ("generation_terminee", "noeud", "arret_motif_code", "non_lance")
MOTIFS_ARRET = (("ArretModeleServiDifferent", "modele_servi_different"), ("ArretTroisEchecs", "trois_echecs_consecutifs"),
                ("ArretDebordementKimi", "debordement_garde_kimi"), ("ArretParSignal", "signal_recu"),
                ("KeyboardInterrupt", "signal_recu"), ("CumulAuDelaDeS17", "plafond_cumule"),
                ("PlafondDeRelaisFaux", "plafond_etape_faux"), ("RelaisSansPlafond", "porte_de_plafond"))
VALEURS = set(ETATS_ETAPE) | set(CLASSES_FIN) | {m for _, m in MOTIFS_ARRET} | {
    "aucun", "autre_exception", "noeud_c13", "kimi", "argon", "proposition", "fusion", "unanimite", "au_moins",
    "majorite_stricte", "conforme", "B", VERSION, "GO-2026-11-01-12", "simule", "reel",
    "L4 : écart rapporté comme réserve ; deux familles seulement, chaque fiche a un juge de sa propre famille (devis, réserves)",
    "scénario B : une génération, bras basique, sans passe tableau"}
MOTIF_OPAQUE = re.compile(r"^v\d{2}$")
MOTIF_EXCEPTION = re.compile(r"^[A-Za-z]{3,60}$")
CLES = {
    "version", "go", "moteur", "scenario", "l1", "l2", "l3", "l4", "verdicts", "couts", "appels", "durees_s", "controle_anti_fuite",
    "fin", "motif_arret", "exception", "etapes", "noeud", "fiches_proposees", "fiches_refusees_forme", "proposeurs_sans_sortie",
    "aiguillage", "niveau_methode", "a_corriger", "concret", "refus_aiguilleur", "passeports", "exclusions_a4", "fusions",
    "ecrites", "completes", "inachevees", "verdicts_presents", "presents", "absents", "lectures_etiquettes", "fiches_etiquetees",
    "lectures_rejetees", "accord_jaccard_moyen", "notables_par_juge", "n", "notables", "part", "agregation", "regle", "accord",
    "n_commun", "accord_brut", "kappa_cohen", "meme_famille", "autre_famille", "part_notable", "x_moyen", "ecart_part_notable",
    "ecart_x_moyen", "reserve", "id", "famille_auteur", "origine", "juges", "famille_juge", "notable", "x", "total_usd",
    "par_fournisseur", "par_role", "par_etape", "registre_cumule_usd", "registre_engage_usd", "registre_appels",
    "registre_par_fournisseur", "controles_usd", "total", "canaris", "titres", "suites_6_mots", "resultat", "garde_testee",
    "cas_sain", "artefacts", "kimi", "argon", "proposition", "fusion", "depassements_reserve", "roles_arretes", "c13_satisfaite",
    "fiches_classees", "notables_agreges", "juge"}


class TraceRefusee(RuntimeError):
    pass


class DossierIllisible(RuntimeError):
    pass


# --- normalisation et contrôle anti-fuite -----------------------------------------------------------------------------------


def mots(texte):
    t = unicodedata.normalize("NFKD", str(texte).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", t)


def chaines(objet):
    if isinstance(objet, str):
        yield objet
    elif isinstance(objet, dict):
        for v in objet.values():
            yield from chaines(v)
    elif isinstance(objet, list):
        for v in objet:
            yield from chaines(v)


def suites(liste, n=6):
    return {tuple(liste[i:i + n]) for i in range(len(liste) - n + 1)}


def controle_anti_fuite(trace, canaris, contenus, titres):
    """Rend {canaris, titres, suites_6_mots, resultat} ; `resultat` = « conforme » si tous les comptes sont nuls."""
    texte = json.dumps(trace, ensure_ascii=False)
    bas = texte.lower()
    m_trace = mots(texte)
    seq_trace = " " + " ".join(m_trace) + " "
    n_can = sum(1 for c in canaris if c and c.lower() in bas)
    n_tit = 0
    for t in titres:
        mt = mots(t)
        if (len(t.strip()) >= 8 and t.strip().lower() in bas) or (len(mt) >= 3 and " " + " ".join(mt) + " " in seq_trace):
            n_tit += 1
    s_fiches = set()
    for c in contenus:
        for ch in chaines(c):
            s_fiches |= suites(mots(ch))
    n_seq = len(suites(m_trace) & s_fiches)
    return {"canaris": n_can, "titres": n_tit, "suites_6_mots": n_seq,
            "resultat": "conforme" if n_can == n_tit == n_seq == 0 else "refusee"}


def tester_garde():
    """R5 : cas sain et trois artefacts ; rend {cas_sain, artefacts} (booléens) ou lève `TraceRefusee`."""
    fiche = {"titre": "Distance de Wasserstein glissante entre trajectoires",
             "hypothese": "la distance entre lois empiriques des scores garde sa puissance hors distribution sur six familles"}
    propre = {"version": VERSION, "l2": {"fiches_proposees": {"kimi": 6, "argon": 6}}, "verdicts": [{"id": "v01", "x": 0.6}]}
    sain = controle_anti_fuite(propre, ["MC1-ESSAI-00000000"], [fiche], [fiche["titre"]])["resultat"] == "conforme"
    a_can = controle_anti_fuite(dict(propre, fin="MC1-ESSAI-00000000"), ["MC1-ESSAI-00000000"], [fiche], [fiche["titre"]])
    a_tit = controle_anti_fuite(dict(propre, fin=fiche["titre"]), [], [fiche], [fiche["titre"]])
    a_seq = controle_anti_fuite(dict(propre, fin="garde sa puissance hors distribution sur six"), [], [fiche], [])
    artefacts = a_can["canaris"] == 1 and a_tit["titres"] == 1 and a_seq["suites_6_mots"] >= 1 and \
        all(x["resultat"] == "refusee" for x in (a_can, a_tit, a_seq))
    lb_sain, lb_art = True, False
    try:
        valider_liste_blanche({"version": VERSION, "n": 3}, set())
    except TraceRefusee:
        lb_sain = False
    try:
        valider_liste_blanche({"version": VERSION, "fin": "texte libre d'une fiche"}, set())
    except TraceRefusee:
        lb_art = True
    if not (sain and artefacts and lb_sain and lb_art):
        raise TraceRefusee(f"garde anti-fuite en échec (R5) : sain={sain and lb_sain}, artefacts={artefacts and lb_art}")
    return {"cas_sain": True, "artefacts": True}


def valider_liste_blanche(objet, permises, chemin="trace"):
    """Lève `TraceRefusee` sur une clé hors `CLES` (hors étiquettes permises) ou une chaîne hors des valeurs permises."""
    if isinstance(objet, dict):
        for k, v in objet.items():
            if k not in CLES and k not in permises:
                raise TraceRefusee(f"liste blanche : clé {k!r} non permise ({chemin})")
            valider_liste_blanche(v, permises, f"{chemin}.{k}")
    elif isinstance(objet, list):
        for i, v in enumerate(objet):
            valider_liste_blanche(v, permises, f"{chemin}[{i}]")
    elif isinstance(objet, str):
        if not (objet in VALEURS or objet in permises or MOTIF_OPAQUE.match(objet) or
                (chemin.endswith(".exception") and MOTIF_EXCEPTION.match(objet))):
            raise TraceRefusee(f"liste blanche : valeur non permise en {chemin}")
    elif objet is not None and not isinstance(objet, (bool, int, float)):
        raise TraceRefusee(f"liste blanche : type {type(objet).__name__} non permis en {chemin}")


# --- lecture du dossier du run ------------------------------------------------------------------------------------------------


def lire_json(chemin, defaut=None, scelle=True):
    if not os.path.isfile(chemin):
        if defaut is not None:
            return defaut
        raise DossierIllisible(f"fichier absent : {chemin}")
    if scelle and os.path.isfile(chemin + ".sha256"):
        with open(chemin, "rb") as f:
            vu = hashlib.sha256(f.read()).hexdigest()
        with open(chemin + ".sha256", encoding="utf-8") as f:
            attendu = f.read().split()[0]
        if vu != attendu:
            raise DossierIllisible(f"empreinte différente de son compagnon : {chemin}")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def kappa_cohen(a, b):
    n = len(a)
    if n == 0:
        return None
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else round((po - pe) / (1 - pe), 6)


def classer_fin(bilan):
    if bilan is None:
        return {"fin": "non_lance", "motif_arret": "aucun", "exception": None}
    arret = bilan.get("arret")
    if arret:
        nom = arret.split(" ", 1)[0].strip(":") if isinstance(arret, str) else ""
        for cle, motif in MOTIFS_ARRET:
            if isinstance(arret, str) and (cle in arret or (cle == "ArretParSignal" and arret.startswith("signal"))):
                return {"fin": "arret_motif_code", "motif_arret": motif, "exception": cle}
        return {"fin": "arret_motif_code", "motif_arret": "autre_exception",
                "exception": nom if MOTIF_EXCEPTION.match(nom or "") else None}
    if bilan.get("noeud"):
        return {"fin": "noeud", "motif_arret": "noeud_c13", "exception": None}
    return {"fin": "generation_terminee", "motif_arret": "aucun", "exception": None}


def agreger(run, conf, canaris_en_plus=()):
    course = os.path.join(run, "course")
    gen = os.path.join(course, "generation-1")
    bilan = lire_json(os.path.join(course, "bilan-course.json"), defaut={}) or None
    manifeste_lancement = lire_json(os.path.join(run, "manifeste-lancement-nuit-v1.json"), defaut={})
    fin = lire_json(os.path.join(gen, "manifeste-fin.json"), defaut={})
    roles = [p["etiquette"] for p in conf["proposeurs"]] + [j["etiquette"] for j in conf["juges"]] + \
        [l["etiquette"] for l in conf["lecteurs_etiquettes"]] + [conf["aiguilleur"]["etiquette"],
                                                                  conf["bisociateur"]["metteur_fusion"]["etiquette"]]
    etapes_noms = [e["nom"] for e in conf["budget"]["etapes"]]
    permises = set(roles) | set(etapes_noms) | {"sans_etape", "controle"}
    famille_de = {p["etiquette"]: FAMILLES[p["fournisseur"]] for p in conf["proposeurs"]}
    juges = {j["etiquette"]: FAMILLES[j["fournisseur"]] for j in conf["juges"]}

    # L1
    l1 = classer_fin(bilan)
    l1["etapes"] = {n: (fin.get("etapes") or {}).get(n, "non_jouee") for n in etapes_noms}
    if any(e.get("evenement") == "passe-tableau-hors-scenario" for e in (fin.get("evenements") or [])):
        l1["etapes"]["passe_tableau"] = "hors_scenario_b"  # aucun appel : jouée à 0 USD au sens du budget seulement
    l1["noeud"] = bool((bilan or {}).get("noeud"))
    l1["c13_satisfaite"] = ((fin.get("budget") or {}).get("c13_satisfaite"))

    # L2
    fiches = lire_json(os.path.join(gen, "fiches.json"), defaut={})
    aig = lire_json(os.path.join(gen, "aiguillage", "journal-aiguillage.json"), defaut={})
    evs = fin.get("evenements") or []
    proposees = {"kimi": 0, "argon": 0}
    for f in fiches.values():
        if f["meta"].get("origine") == "proposition":
            proposees[f["meta"]["fournisseur"]] += 1
    classes = {"niveau_methode": 0, "a_corriger": 0, "concret": 0}
    for r in aig.get("retenues") or []:
        if r.get("origine") == "proposition":
            proposees[r["fournisseur"]] += 1
        if r.get("classe") in classes:
            classes[r["classe"]] += 1
    classes["niveau_methode"] = int(aig.get("passeports") or 0)
    refusees_forme = {}
    for e in evs:
        if e.get("evenement") == "fiche-refusee" and e.get("proposeur") in famille_de:
            refusees_forme[e["proposeur"]] = refusees_forme.get(e["proposeur"], 0) + 1
    sans_sortie = {}
    for e in evs:
        if e.get("evenement") == "appel-inexploitable" and e.get("role") in famille_de and e.get("etape") == "proposition":
            sans_sortie[e["role"]] = sans_sortie.get(e["role"], 0) + 1
    fus = fin.get("fusions") or {}
    archive = lire_json(os.path.join(gen, "fusions-inachevees.json"), defaut={"fusions": []})
    verdicts_fichiers = sorted(n for n in os.listdir(os.path.join(gen, "coffre"))
                               if n.startswith("verdicts-") and n.endswith(".json")) if os.path.isdir(os.path.join(gen, "coffre")) else []
    verdicts = {}
    ouvrir = l1["fin"] == "generation_terminee"  # O12 : après un nœud ou un arrêt, aucun verdict n'est ouvert
    if ouvrir:
        for n in verdicts_fichiers:
            v = lire_json(os.path.join(gen, "coffre", n))
            verdicts[v["ident"]] = v["verdicts"]
        presents = {j: {"presents": 0, "absents": 0} for j in juges}
        for par_juge in verdicts.values():
            for j in juges:
                presents[j]["presents" if par_juge.get(j) is not None else "absents"] += 1
    else:  # noms des dépôts seulement (jamais leur contenu) et absences comptées par le noyau
        absents = fin.get("juges_absents") or {}
        presents = {j: {"presents": max(0, len(verdicts_fichiers) - int(absents.get(j, 0))), "absents": int(absents.get(j, 0))}
                    for j in juges}
    lectures = lire_json(os.path.join(gen, "coffre", f"{conf['graines']['prefixe']}-lectures-etiquettes.json"), defaut={})
    etiquetees = {l: sum(1 for x in ((lectures.get("basique") or {}).get(l) or {}).values() if x)
                  for l in [x["etiquette"] for x in conf["lecteurs_etiquettes"]]}
    accords = lire_json(os.path.join(gen, "accords.json"), defaut={})
    l2 = {"fiches_proposees": proposees, "fiches_refusees_forme": refusees_forme, "proposeurs_sans_sortie": sans_sortie,
          "aiguillage": dict(classes, refus_aiguilleur=int(aig.get("refus_aiguilleur") or 0)), "passeports": int(aig.get("passeports") or 0),
          "exclusions_a4": len(fin.get("exclues_a4") or {}),
          "fusions": {"ecrites": int(fus.get("completes") or 0) + len([x for x in archive.get("fusions", []) if x.get("contenu")]),
                      "completes": int(fus.get("completes") or 0), "inachevees": int(fus.get("inachevees") or 0)},
          "verdicts_presents": presents,
          "lectures_etiquettes": {"fiches_etiquetees": etiquetees, "lectures_rejetees": int(sum((fin.get("refus_lectures") or {}).values())),
                                  "accord_jaccard_moyen": (accords.get("s24_basique") or {}).get("jaccard_moyen")},
          "roles_arretes": len(fin.get("roles_arretes") or {}) + len(fin.get("roles_arretes_a2") or {})}

    # verdicts sous identifiant opaque, famille du juge ; L3, L4
    lignes, tous = [], sorted(verdicts)
    for k, ident in enumerate(tous, 1):
        meta = (fiches.get(ident) or {}).get("meta") or {}
        fam = FAMILLES.get(meta.get("fournisseur"))
        ligne = {"id": f"v{k:02d}", "famille_auteur": fam, "origine": meta.get("origine") if meta.get("origine") in ("proposition", "fusion") else None,
                 "juges": []}
        for j, fj in sorted(juges.items()):
            v = verdicts[ident].get(j)
            ligne["juges"].append({"juge": j, "famille_juge": fj, "meme_famille": (fam == fj) if fam else None,
                                   "notable": None if v is None else bool(v["notable"]), "x": None if v is None else float(v["x"])})
        lignes.append(ligne)
    l3 = {"notables_par_juge": {}, "agregation": {}, "accord": {}}
    for j in juges:
        vus = [x for l in lignes for x in l["juges"] if x["juge"] == j and x["notable"] is not None]
        l3["notables_par_juge"][j] = {"n": len(vus), "notables": sum(x["notable"] for x in vus),
                                      "part": round(sum(x["notable"] for x in vus) / len(vus), 6) if vus else None}
    classement = lire_json(os.path.join(gen, "classement.json"), defaut={"lignes": []})
    ag = conf["agregation"]
    n_ag = len(classement.get("lignes") or [])
    not_ag = sum(1 for l in classement.get("lignes") or [] if l.get("notable"))
    l3["agregation"] = {"regle": ag["regle"], "n": n_ag, "notables": not_ag, "part": round(not_ag / n_ag, 6) if n_ag else None}
    j1, j2 = sorted(juges)
    paires = [(next(x for x in l["juges"] if x["juge"] == j1)["notable"], next(x for x in l["juges"] if x["juge"] == j2)["notable"])
              for l in lignes]
    paires = [(a, b) for a, b in paires if a is not None and b is not None]
    l3["accord"] = {"n_commun": len(paires), "accord_brut": round(sum(a == b for a, b in paires) / len(paires), 6) if paires else None,
                    "kappa_cohen": kappa_cohen([int(a) for a, _ in paires], [int(b) for _, b in paires]) if paires else None}
    groupes = {"meme_famille": [], "autre_famille": []}
    for l in lignes:
        for x in l["juges"]:
            if x["notable"] is not None and x["meme_famille"] is not None:
                groupes["meme_famille" if x["meme_famille"] else "autre_famille"].append(x)
    l4 = {}
    for g, xs in groupes.items():
        l4[g] = {"n": len(xs), "part_notable": round(sum(x["notable"] for x in xs) / len(xs), 6) if xs else None,
                 "x_moyen": round(sum(x["x"] for x in xs) / len(xs), 6) if xs else None}
    a, b = l4["meme_famille"], l4["autre_famille"]
    l4["ecart_part_notable"] = round(a["part_notable"] - b["part_notable"], 6) if None not in (a["part_notable"], b["part_notable"]) else None
    l4["ecart_x_moyen"] = round(a["x_moyen"] - b["x_moyen"], 6) if None not in (a["x_moyen"], b["x_moyen"]) else None
    l4["reserve"] = ("L4 : écart rapporté comme réserve ; deux familles seulement, chaque fiche a un juge de sa propre famille "
                     "(devis, réserves)")

    # coûts, appels, durées
    cons = (lire_json(os.path.join(gen, "consommations.json"), defaut={"consommations": []}).get("consommations")) or []
    cons = [c for c in cons if c.get("role") in roles]
    par_f, par_r, par_e, appels_r, durees_r = {}, {}, {}, {}, {}
    for c in cons:
        for table, cle in ((par_f, c.get("fournisseur")), (par_r, c["role"]), (par_e, c["etape"])):
            table[cle] = round(table.get(cle, 0.0) + float(c["cout_usd"]), 6)
        appels_r[c["role"]] = appels_r.get(c["role"], 0) + 1
        durees_r[c["role"]] = round(durees_r.get(c["role"], 0.0) + float(c.get("duree_s") or 0.0), 3)
    registre = os.path.join(run, NOM_REGISTRE)
    e_reg = reg.etat(registre) if os.path.isfile(registre) else None
    couts = {"total_usd": round(sum(par_f.values()), 6), "par_fournisseur": par_f, "par_role": par_r, "par_etape": par_e,
             "registre_cumule_usd": e_reg["regle_usd"] if e_reg else None, "registre_engage_usd": e_reg["engage_usd"] if e_reg else None,
             "registre_appels": e_reg["appels"] if e_reg else None,
             "registre_par_fournisseur": {k: round(v["regle_usd"] + v["engage_usd"], 6) for k, v in (e_reg or {}).get("par_fournisseur", {}).items()},
             "controles_usd": round(sum(v["regle_usd"] + v["engage_usd"] for k, v in (e_reg or {}).get("par_etape", {}).items()
                                        if k == "controle"), 6) if e_reg else None,
             "depassements_reserve": e_reg["depassements_reserve"] if e_reg else None}
    appels = {"par_role": appels_r, "par_fournisseur": {f: sum(1 for c in cons if c.get("fournisseur") == f) for f in ("kimi", "argon")},
              "total": len(cons)}
    trace = {"version": VERSION, "go": (manifeste_lancement.get("go") or {}).get("identifiant") if isinstance(manifeste_lancement.get("go"), dict) else None,
             "moteur": manifeste_lancement.get("moteur"), "scenario": "scénario B : une génération, bras basique, sans passe tableau",
             "l1": l1, "l2": l2, "l3": dict(l3, notables_agreges=not_ag, fiches_classees=n_ag), "l4": l4, "verdicts": lignes,
             "couts": couts, "appels": appels, "durees_s": {"par_role": durees_r}}
    if trace["go"] not in (None, "GO-2026-11-01-12"):
        trace["go"] = None
    canaris = list((conf.get("canaris") or {}).values()) + list(canaris_en_plus)
    contenus = [f.get("contenu") for f in fiches.values()] + [x.get("contenu") for x in archive.get("fusions", []) if x.get("contenu")]
    titres = []
    for c in contenus:
        if isinstance(c, dict) and isinstance(c.get(conf["champ_titre"]), str):
            titres.append(c[conf["champ_titre"]])
        elif isinstance(c, list):
            titres += [x.get(conf["champ_titre"]) for x in c if isinstance(x, dict) and isinstance(x.get(conf["champ_titre"]), str)]
    return trace, permises, canaris, contenus, titres


def artefacts_sur_run(trace, permises, canaris, contenus, titres):
    """R5 sur le run : chaque fuite injectée dans une copie de la trace est vue ; la trace propre passe."""
    sain = controle_anti_fuite(trace, canaris, contenus, titres)["resultat"] == "conforme"
    resultats = {"cas_sain": sain}
    if canaris:
        resultats["canari"] = controle_anti_fuite(dict(trace, scenario=trace["scenario"] + " " + canaris[-1]), canaris, contenus,
                                                  titres)["canaris"] >= 1
    if titres:
        resultats["titre"] = controle_anti_fuite(dict(trace, scenario=titres[0]), canaris, contenus, titres)["titres"] >= 1
    longs = [m for c in contenus for ch in chaines(c) if len(m := mots(ch)) >= 6]
    if longs:
        resultats["suite_6_mots"] = controle_anti_fuite(dict(trace, scenario=" ".join(longs[0][:6])), canaris, contenus,
                                                        titres)["suites_6_mots"] >= 1
    try:
        valider_liste_blanche(dict(trace, scenario="texte libre hors liste"), permises)
        resultats["liste_blanche"] = False
    except TraceRefusee:
        resultats["liste_blanche"] = True
    resultats["tous_vus"] = all(resultats.values())
    return resultats


def ecrire_neuf_scelle(chemin, objet):
    if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):
        raise DossierIllisible(f"{chemin} existe déjà (R12)")
    octets = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    sha = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--run")
    a.add_argument("--configuration")
    a.add_argument("--canari", action="append", default=[])
    a.add_argument("--sortie")
    a.add_argument("--tester-garde", action="store_true")
    a.add_argument("--artefacts-sur-run", action="store_true",
                   help="R5 sur le run réel : injecte un canari, un titre et six mots d'une fiche dans une copie de la trace ; "
                        "chacun doit être refusé ; rien n'est écrit")
    args = a.parse_args(argv)
    try:
        garde = tester_garde()
        if args.tester_garde:
            print(json.dumps({"garde_testee": garde}, ensure_ascii=False))
            return 0
        if not args.run or not args.configuration:
            raise DossierIllisible("--run et --configuration exigés")
        with open(args.configuration, encoding="utf-8") as f:
            conf = json.load(f)
        trace, permises, canaris, contenus, titres = agreger(args.run, conf, args.canari)
        if args.artefacts_sur_run:
            print(json.dumps(artefacts_sur_run(trace, permises, canaris, contenus, titres), ensure_ascii=False))
            return 0
        valider_liste_blanche(trace, permises)
        anti = controle_anti_fuite(trace, canaris, contenus, titres)
        if anti["resultat"] != "conforme":
            raise TraceRefusee(f"contrôle anti-fuite : {anti['canaris']} canari(s), {anti['titres']} titre(s), "
                               f"{anti['suites_6_mots']} suite(s) de six mots : trace refusée, rien d'écrit")
        trace["controle_anti_fuite"] = dict(anti, garde_testee=garde)
        valider_liste_blanche(trace, permises)
        sortie = args.sortie or os.path.join(args.run, NOM_TRACE)
        sha = ecrire_neuf_scelle(sortie, trace)
        print(json.dumps({"trace": sortie, "sha256": sha, "anti_fuite": anti, "l1": trace["l1"]["fin"]}, ensure_ascii=False))
        return 0
    except TraceRefusee as e:
        print(f"TRACE REFUSÉE : {e}", file=sys.stderr)
        return 3
    except (DossierIllisible, reg.RegistreIllisible, OSError, ValueError, KeyError) as e:
        print(f"REFUS : {type(e).__name__} : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
