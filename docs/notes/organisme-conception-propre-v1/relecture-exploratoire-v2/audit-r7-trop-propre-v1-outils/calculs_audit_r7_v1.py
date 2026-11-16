"""Calculs de l'audit « R7 trop propre » (règle de symétrie, R4 du programme) — v1.

Question : la relecture exploratoire v2 a-t-elle relu R7 par des appels neufs, ou une partie de la première lecture
a-t-elle été reprise ? L'accord parfait des valeurs retenues de R7 (23 fiches réelles) est-il explicable ?

Ce programme ne lit que des pièces déjà versées au dépôt (réponses brutes, journaux, clés, piles, lectures vérifiées,
classements des deux lectures). Il ne fait aucun appel, n'écrit qu'un fichier de résultat (jamais d'écrasement), ne
désigne aucune fiche (les fiches ne sont jamais nommées dans la sortie : comptes et motifs seulement) et n'écrit ni le
nom du lecteur ni celui d'un modèle (le champ du modèle servi est seulement comparé entre réponses).

Usage, depuis la racine du dépôt :
    .venv/bin/python -I -B CHEMIN/calculs_audit_r7_v1.py --racine . [--sortie FICHIER.json]

Sans `--sortie`, le résultat est seulement affiché. Aucune graine : tout est exact ou déterministe.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DOS = "docs/notes/organisme-conception-propre-v1"
RE_ = f"{DOS}/relecture-exploratoire-v2"
OUT = f"{RE_}/lecture-classement-v3-2"
LECTURES = {"premiere": ("lecture-g1-v3-1", "v3-1", "manifeste-envois-v3-1.json"),
            "relecture": ("lecture-g1-v3-2", "v3-2", "manifeste-relecture-v3-2.json")}
PASSAGES = ("L1", "L2")
CRITERES = ("R1", "R2", "R3", "R4", "R5", "R6", "R7")
LOTS = range(1, 10)
# Empreinte du journal de la première lecture : ce journal n'a pas de compagnon ; elle est épinglée dans l'outil du
# lecteur v3.2.1 (constante PREMIERE_LECTURE) et portée par le relevé final de la première lecture.
JOURNAL_PREMIERE_EPINGLE = "003546428fc15ed3bc787a1e7dc853b12c105897fdc4f296a239ede81871764a"

PIECES = {}  # chemin relatif -> {"sha256_8": …, "compagnon": "OK" | "absent" | "DIFFERENT"}


class Ecart(Exception):
    pass


def lire(racine: Path, rel: str) -> bytes:
    """Lit une pièce, note son empreinte et la confronte à son compagnon `.sha256` (R6, R11)."""
    p = racine / rel
    b = p.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    c = Path(str(p) + ".sha256")
    if c.is_file():
        etat = "OK" if c.read_text(encoding="utf-8").split()[0] == h else "DIFFERENT"
    else:
        etat = "absent"
    if etat == "DIFFERENT":
        raise Ecart(f"{rel} : empreinte différente de son compagnon")
    PIECES[rel] = {"sha256_8": h[:8], "sha256": h, "compagnon": etat}
    return b


def lire_json(racine: Path, rel: str):
    return json.loads(lire(racine, rel).decode("utf-8"))


def extraire(contenu: str) -> dict:
    """Même règle que l'outil : le texte entier, ou un seul bloc ```json … ```."""
    t = contenu.strip()
    blocs = re.findall(r"```(?:json)?\s*\n(.*?)\n?```", t, flags=re.S)
    if len(blocs) > 1:
        raise Ecart("plusieurs blocs JSON")
    return json.loads(blocs[0] if blocs else t)


def utc(s: str) -> float:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def iso(t: float) -> str:
    return datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def espaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def feuilles(o) -> list:
    if isinstance(o, str):
        return [o]
    if isinstance(o, list):
        return [t for x in o for t in feuilles(x)]
    if isinstance(o, dict):
        return [t for v in o.values() for t in feuilles(v)]
    return []


# --- chargement d'une lecture ------------------------------------------------------------------------------------------

def charger(racine: Path, nom: str) -> dict:
    dossier, suf, manifeste = LECTURES[nom]
    env = f"{DOS}/{dossier}/envois"
    cla = f"{DOS}/{dossier}/classement"
    cle = lire_json(racine, f"{env}/cle-lectures-{suf}.json")
    pile = lire_json(racine, f"{env}/pile-interne-{suf}.json")
    lire(racine, f"{env}/{manifeste}")
    journal_octets = lire(racine, f"{env}/journal-depense-{suf}.jsonl")
    journal = [json.loads(x) for x in journal_octets.decode("utf-8").splitlines()]
    classement = lire_json(racine, f"{cla}/classement-{suf}.json")
    verif, verif_envois_egale = {}, {}
    for L in PASSAGES:
        verif[L] = lire_json(racine, f"{cla}/lecture-verifiee-{L}-{suf}.json")
        a = PIECES[f"{cla}/lecture-verifiee-{L}-{suf}.json"]["sha256"]
        lire(racine, f"{env}/lecture-verifiee-{L}-{suf}.json")
        verif_envois_egale[L] = a == PIECES[f"{env}/lecture-verifiee-{L}-{suf}.json"]["sha256"]
    appels, entrees = [], {}
    for L in PASSAGES:
        for k in LOTS:
            rel = f"{env}/reponse-{L}-lot{k}-{suf}.json"
            r = lire_json(racine, rel)
            corps_rel = f"{env}/envoi-{L}-lot{k}-{suf}.corps.json"
            corps = lire_json(racine, corps_rel)
            contenu = r["choices"][0]["message"]["content"]
            u = r.get("usage") or {}
            appels.append({
                "passage": L, "lot": k, "id": r["id"], "created": r["created"], "modele": r.get("model"),
                "fin": r["choices"][0].get("finish_reason"), "contenu_sha256": hashlib.sha256(contenu.encode()).hexdigest(),
                "reponse_sha256": PIECES[rel]["sha256"], "corps_sha256": PIECES[corps_rel]["sha256"],
                "message": corps["messages"][0]["content"],
                "parametres": {x: y for x, y in corps.items() if x != "messages"},
                "jetons_entree": u.get("prompt_tokens"), "jetons_sortie": u.get("completion_tokens"),
                "jetons_raisonnement": (u.get("completion_tokens_details") or {}).get("reasoning_tokens"),
                "jetons_lus_en_cache": (u.get("prompt_tokens_details") or {}).get("cached_tokens"),
                "fichier": f"reponse-{L}-lot{k}-{suf}.json", "envoi": f"envoi-{L}-lot{k}-{suf}.corps.json"})
            for e in extraire(contenu)["lecture"]:
                ident = cle[L]["etiquettes"][e["etiquette"]]
                if (L, ident) in entrees:
                    raise Ecart("entrée en double")
                entrees[(L, ident)] = {"brut": e, "etiquette": e["etiquette"], "lot": k, "appel": r["id"]}
    par_id = {p["id"]: p for p in pile["fiches"]}
    return {"nom": nom, "suffixe": suf, "cle": cle, "pile": par_id, "ordre_pile": [p["id"] for p in pile["fiches"]],
            "journal": journal, "journal_sha256": hashlib.sha256(journal_octets).hexdigest(), "classement": classement,
            "verif": verif, "verif_envois_egale": verif_envois_egale, "appels": appels, "entrees": entrees}


# --- contrôles d'appels ------------------------------------------------------------------------------------------------

def controle_appels(A: dict, B: dict) -> dict:
    res = {}
    for X in (A, B):
        j = X["journal"]
        envois = {e["envoi"]: e for e in j if e["evenement"] == "envoi"}
        recus = {e["envoi"]: e for e in j if e["evenement"] == "recu"}
        clos = {e["envoi"]: e for e in j if e["evenement"] == "clos"}
        chaine, prec = True, "debut"
        brutes = [json.dumps({k: v for k, v in e.items()}, ensure_ascii=False) for e in j]
        dans_fenetre, fichiers_egaux, statuts = 0, 0, set()
        for a in X["appels"]:
            ev, rc, cl = envois[a["envoi"]], recus[a["envoi"]], clos[a["envoi"]]
            if utc(ev["utc"]) - 2 <= a["created"] <= utc(rc["utc"]) + 2:
                dans_fenetre += 1
            if rc["fichier"] == a["fichier"] and rc["fichier_sha256"] == a["reponse_sha256"] == cl["fichier_sha256"]:
                fichiers_egaux += 1
            statuts.add(cl["statut"])
        t = sorted(a["created"] for a in X["appels"])
        res[X["nom"]] = {
            "appels": len(X["appels"]), "identifiants_distincts": len({a["id"] for a in X["appels"]}),
            "journal_lignes": len(j), "journal_envois": len(envois), "journal_recus": len(recus), "journal_clos": len(clos),
            "journal_arrets": sum(1 for e in j if e["evenement"] == "arret"),
            "anomalies_au_journal": sum(len(e.get("anomalies") or []) for e in clos.values()),
            "statuts": sorted(statuts),
            "horodatage_de_la_reponse_entre_envoi_et_reception_du_journal": f"{dans_fenetre} sur {len(X['appels'])}",
            "fichier_de_reponse_a_l_empreinte_du_journal": f"{fichiers_egaux} sur {len(X['appels'])}",
            "premier_horodatage_utc": iso(t[0]), "dernier_horodatage_utc": iso(t[-1]),
            "journal_premier_utc": j[0]["utc"], "journal_dernier_utc": j[-1]["utc"],
            "jetons_lus_en_cache_total": sum(a["jetons_lus_en_cache"] or 0 for a in X["appels"]),
            "jetons_entree_total": sum(a["jetons_entree"] for a in X["appels"]),
            "jetons_sortie_total": sum(a["jetons_sortie"] for a in X["appels"]),
            "depense_au_journal_usd": round(sum(e["cout_usd"] for e in clos.values()), 6),
            "fin_stop": sum(1 for a in X["appels"] if a["fin"] == "stop"),
            "parametres_distincts_hors_message": len({json.dumps(a["parametres"], sort_keys=True) for a in X["appels"]}),
        }
    ia, ib = {a["id"] for a in A["appels"]}, {a["id"] for a in B["appels"]}
    tous = A["appels"] + B["appels"]
    par_temps = [a["id"] for a in sorted(tous, key=lambda a: a["created"])]
    paires = list(zip(A["appels"], B["appels"]))
    res["croise"] = {
        "identifiants_communs": len(ia & ib),
        "identifiants_distincts_sur_36": len(ia | ib),
        "ordre_des_identifiants_egal_a_l_ordre_du_temps": par_temps == sorted(par_temps),
        "ecart_minimal_entre_lectures_heures": round((min(a["created"] for a in B["appels"])
                                                      - max(a["created"] for a in A["appels"])) / 3600, 2),
        "reponses_a_la_meme_empreinte": len({a["reponse_sha256"] for a in A["appels"]}
                                            & {a["reponse_sha256"] for a in B["appels"]}),
        "contenus_a_la_meme_empreinte": len({a["contenu_sha256"] for a in A["appels"]}
                                            & {a["contenu_sha256"] for a in B["appels"]}),
        "corps_d_envoi_a_la_meme_empreinte": len({a["corps_sha256"] for a in A["appels"]}
                                                 & {a["corps_sha256"] for a in B["appels"]}),
        "meme_modele_servi_dans_les_36_reponses": len({a["modele"] for a in tous}) == 1,
        "memes_parametres_hors_message_dans_les_36_envois": len({json.dumps(a["parametres"], sort_keys=True)
                                                                 for a in tous}) == 1,
        "lots_ou_jetons_d_entree_egaux": sum(1 for a, b in paires if a["jetons_entree"] == b["jetons_entree"]),
        "lots_ou_jetons_de_sortie_egaux": sum(1 for a, b in paires if a["jetons_sortie"] == b["jetons_sortie"]),
        "lots_ou_jetons_de_raisonnement_egaux": sum(1 for a, b in paires
                                                    if a["jetons_raisonnement"] == b["jetons_raisonnement"]),
        "journal_premiere_egal_a_l_epingle_de_l_outil": A["journal_sha256"] == JOURNAL_PREMIERE_EPINGLE,
    }
    return res


def controle_contexte(A: dict, B: dict, reelles: list) -> dict:
    """Ce qui est resté identique d'une lecture à l'autre dans ce qui a été servi au lecteur."""
    res = {"fiches_reelles_communes": len(reelles),
           "vue_servie_identique_au_caractere": sum(1 for i in reelles if A["pile"][i]["vue"] == B["pile"][i]["vue"])}
    for L in PASSAGES:
        ea = {v: k for k, v in A["cle"][L]["etiquettes"].items()}
        eb = {v: k for k, v in B["cle"][L]["etiquettes"].items()}
        la = {et: n for n, lot in enumerate(A["cle"][L]["lots"], 1) for et in lot}
        lb = {et: n for n, lot in enumerate(B["cle"][L]["lots"], 1) for et in lot}
        res[L] = {"meme_etiquette": sum(1 for i in reelles if ea[i] == eb[i]),
                  "meme_lot": sum(1 for i in reelles if la[ea[i]] == lb[eb[i]]),
                  "reelles_par_lot": [sum(1 for et in lot if A["cle"][L]["etiquettes"][et] in reelles)
                                      for lot in A["cle"][L]["lots"]],
                  "taille_des_lots": [len(lot) for lot in A["cle"][L]["lots"]]}
    # position de la fiche dans le passage : même ordre L1 et L2 d'une lecture à l'autre ?
    pos = {}
    for L in PASSAGES:
        pa = {i: n for n, i in enumerate(A["cle"][L]["ordre"])}
        pb = {i: n for n, i in enumerate(B["cle"][L]["ordre"])}
        pos[L] = sum(1 for i in reelles if pa[i] == pb[i])
    res["meme_rang_dans_le_passage"] = pos
    ea1 = {v: k for k, v in A["cle"]["L1"]["etiquettes"].items()}
    ea2 = {v: k for k, v in A["cle"]["L2"]["etiquettes"].items()}
    res["fiches_a_la_meme_etiquette_en_L1_et_L2"] = sum(1 for i in reelles if ea1[i] == ea2[i])
    msgs = []
    for a, b in zip(A["appels"], B["appels"]):
        ma, mb = a["message"], b["message"]
        n = 0
        for x, y in zip(ma, mb):
            if x != y:
                break
            n += 1
        msgs.append({"passage": a["passage"], "lot": a["lot"], "identique": ma == mb, "caracteres_premiere": len(ma),
                     "caracteres_relecture": len(mb), "prefixe_commun": n})
    res["messages_identiques_entre_lectures"] = sum(1 for m in msgs if m["identique"])
    res["messages"] = msgs
    return res


# --- valeurs de R7 et des autres critères ------------------------------------------------------------------------------

def valeurs(X: dict, i: str, c: str) -> tuple:
    return tuple(X["verif"][L]["fiches"][i][c]["compte"] for L in PASSAGES)


def controle_regle(X: dict) -> dict:
    """La valeur retenue du classement est-elle le « et » des deux passages, pour toute la pile ?"""
    ok, n = 0, 0
    brut_egal = 0
    for i in X["ordre_pile"]:
        for c in CRITERES:
            v1, v2 = valeurs(X, i, c)
            n += 1
            ok += int(X["classement"]["retenu"][i][c] == int(v1 == 1 and v2 == 1))
    for (L, i), e in X["entrees"].items():
        if X["verif"][L]["fiches"][i]["R7"]["brut"] == e["brut"]["R7"].get("valeur"):
            brut_egal += 1
    return {"valeurs_retenues_egales_au_et_des_deux_passages": f"{ok} sur {n}",
            "R7_brut_de_la_lecture_verifiee_egal_a_la_reponse_brute": f"{brut_egal} sur {len(X['entrees'])}",
            "lecture_verifiee_du_classement_egale_a_celle_des_envois": X["verif_envois_egale"]}


def preuve_r7(X: dict, reelles: list) -> dict:
    """Refait la preuve « mot pour mot » de R7 sur les fiches réelles (même normalisation que l'outil)."""
    oui, prouves, comptes = 0, 0, 0
    for L in PASSAGES:
        for i in reelles:
            e = X["entrees"][(L, i)]["brut"]["R7"]
            if e.get("valeur") == 1:
                oui += 1
                p = espaces(e.get("passage") or "")
                formes = {p, espaces(p.replace('\\"', '"').replace("\\\\", "\\"))}
                textes = [espaces(t) for t in feuilles(X["pile"][i]["vue"])]
                ok = len(re.sub(r"\s", "", p)) >= 20 and any(f in t for f in formes for t in textes)
                prouves += int(ok)
            comptes += int(X["verif"][L]["fiches"][i]["R7"]["compte"] == 1)
    return {"oui_bruts": oui, "oui_prouves_refaits": prouves, "oui_comptes_par_l_outil": comptes}


def kappa(a: list, b: list) -> dict:
    n = len(a)
    po = sum(int(x == y) for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return {"n": n, "accord_brut": round(po, 4), "desaccords": sum(int(x != y) for x, y in zip(a, b)),
            "kappa": None if pe == 1 else round((po - pe) / (1 - pe), 4)}


def tableau_r7(A: dict, B: dict, reelles: list) -> dict:
    motifs = {}
    for i in reelles:
        m = "".join(map(str, valeurs(A, i, "R7") + valeurs(B, i, "R7")))
        motifs[m] = motifs.get(m, 0) + 1
    a1 = [valeurs(A, i, "R7")[0] for i in reelles]
    a2 = [valeurs(A, i, "R7")[1] for i in reelles]
    b1 = [valeurs(B, i, "R7")[0] for i in reelles]
    b2 = [valeurs(B, i, "R7")[1] for i in reelles]
    ra = [int(x and y) for x, y in zip(a1, a2)]
    rb = [int(x and y) for x, y in zip(b1, b2)]
    changes = [(i, k) for i in range(len(reelles)) for k, (x, y) in enumerate(((a1, b1), (a2, b2))) if x[i] != y[i]]
    masques = sum(1 for i, k in changes if ra[i] == rb[i])
    return {
        "ordre_du_motif": "première L1, première L2, relecture L1, relecture L2 (valeurs comptées après la preuve)",
        "motifs_et_nombre_de_fiches": dict(sorted(motifs.items(), key=lambda kv: (-kv[1], kv[0]))),
        "fiches_unanimes_sur_les_quatre_passages": sum(n for m, n in motifs.items() if len(set(m)) == 1),
        "entre_passages_premiere_lecture": kappa(a1, a2),
        "entre_passages_relecture": kappa(b1, b2),
        "meme_passage_L1_entre_lectures": kappa(a1, b1),
        "meme_passage_L2_entre_lectures": kappa(a2, b2),
        "croise_premiere_L1_relecture_L2": kappa(a1, b2),
        "croise_premiere_L2_relecture_L1": kappa(a2, b1),
        "retenu_entre_lectures": kappa(ra, rb),
        "retenu_a_1": {"premiere": sum(ra), "relecture": sum(rb)},
        "retenu_du_classement_egal_au_recalcul": {
            "premiere": all(A["classement"]["retenu"][i]["R7"] == r for i, r in zip(reelles, ra)),
            "relecture": all(B["classement"]["retenu"][i]["R7"] == r for i, r in zip(reelles, rb))},
        "valeurs_de_passage_changees_entre_lectures": {
            "nombre_sur_46": len(changes), "dans_L1": sum(1 for _, k in changes if k == 0),
            "dans_L2": sum(1 for _, k in changes if k == 1),
            "sens_1_vers_0": sum(1 for i, k in changes if ((a1, a2)[k][i], (b1, b2)[k][i]) == (1, 0)),
            "sens_0_vers_1": sum(1 for i, k in changes if ((a1, a2)[k][i], (b1, b2)[k][i]) == (0, 1)),
            "masquees_par_le_et_car_l_autre_passage_vaut_0_dans_les_deux_lectures": masques},
        "comptes_premiere_lecture": {"deux_oui": sum(1 for x, y in zip(a1, a2) if x and y),
                                     "un_seul_oui": sum(1 for x, y in zip(a1, a2) if x != y),
                                     "aucun_oui": sum(1 for x, y in zip(a1, a2) if not x and not y)},
        "comptes_relecture": {"deux_oui": sum(1 for x, y in zip(b1, b2) if x and y),
                              "un_seul_oui": sum(1 for x, y in zip(b1, b2) if x != y),
                              "aucun_oui": sum(1 for x, y in zip(b1, b2) if not x and not y)},
    }


def textes_r7(A: dict, B: dict, reelles: list) -> dict:
    """Les justifications de R7 sont-elles identiques au caractère près d'une lecture à l'autre ?"""
    def champ(e):
        r = e["brut"]["R7"]
        return ("passage", r.get("passage")) if r.get("valeur") == 1 else ("motif", r.get("motif"))

    res = {}
    for nom, paires in (
            ("meme_passage_entre_lectures", [((A, L, i), (B, L, i)) for L in PASSAGES for i in reelles]),
            ("entre_passages_premiere_lecture", [((A, "L1", i), (A, "L2", i)) for i in reelles]),
            ("entre_passages_relecture", [((B, "L1", i), (B, "L2", i)) for i in reelles])):
        c = {"paires": len(paires), "deux_oui": 0, "deux_oui_passage_identique": 0, "deux_non": 0,
             "deux_non_motif_identique": 0, "valeurs_differentes": 0, "entree_R7_identique_au_caractere": 0,
             "entree_entiere_de_la_fiche_identique_au_caractere": 0}
        for (X, L1, i), (Y, L2, k) in paires:
            ex, ey = X["entrees"][(L1, i)], Y["entrees"][(L2, k)]
            (gx, tx), (gy, ty) = champ(ex), champ(ey)
            if gx != gy:
                c["valeurs_differentes"] += 1
            elif gx == "passage":
                c["deux_oui"] += 1
                c["deux_oui_passage_identique"] += int(tx == ty)
            else:
                c["deux_non"] += 1
                c["deux_non_motif_identique"] += int(tx == ty)
            c["entree_R7_identique_au_caractere"] += int(ex["brut"]["R7"] == ey["brut"]["R7"])
            sx = {k2: v for k2, v in ex["brut"].items() if k2 != "etiquette"}
            sy = {k2: v for k2, v in ey["brut"].items() if k2 != "etiquette"}
            c["entree_entiere_de_la_fiche_identique_au_caractere"] += int(sx == sy)
        res[nom] = c
    return res


def tous_criteres(A: dict, B: dict, reelles: list) -> dict:
    """Répétabilité par critère : même passage entre lectures, contre passages différents."""
    res, cumul = {}, {"cellules": 0, "changees": 0}
    for c in CRITERES:
        ids = [i for i in reelles if not (c == "R4" and A["pile"][i]["levier"] != "levier:juge")]
        va = {i: valeurs(A, i, c) for i in ids}
        vb = {i: valeurs(B, i, c) for i in ids}
        meme = sum(int(va[i][k] != vb[i][k]) for i in ids for k in (0, 1))
        intra_a = sum(int(va[i][0] != va[i][1]) for i in ids)
        intra_b = sum(int(vb[i][0] != vb[i][1]) for i in ids)
        croise = sum(int(va[i][0] != vb[i][1]) + int(va[i][1] != vb[i][0]) for i in ids)
        ret = sum(int((va[i][0] and va[i][1]) != (vb[i][0] and vb[i][1])) for i in ids)
        uns = sum(va[i][0] + va[i][1] + vb[i][0] + vb[i][1] for i in ids)
        res[c] = {"fiches_lues_par_le_lecteur": len(ids), "oui_sur_les_quatre_passages": f"{uns} sur {4 * len(ids)}",
                  "meme_passage_entre_lectures_changees": f"{meme} sur {2 * len(ids)}",
                  "entre_passages_premiere_desaccords": f"{intra_a} sur {len(ids)}",
                  "entre_passages_relecture_desaccords": f"{intra_b} sur {len(ids)}",
                  "passages_differents_entre_lectures_desaccords": f"{croise} sur {2 * len(ids)}",
                  "retenu_change_entre_lectures": f"{ret} sur {len(ids)}"}
        if c != "R7":
            cumul["cellules"] += 2 * len(ids)
            cumul["changees"] += meme
    cumul["taux"] = round(cumul["changees"] / cumul["cellules"], 5)
    res["R1_a_R6_ensemble_meme_passage_entre_lectures"] = cumul
    # choix du passage cité : même contexte contre contexte différent (tous critères, deux « oui »)
    def cite(X, L, i, c):
        r = X["entrees"][(L, i)]["brut"].get(c) or {}
        return r.get("passage") if r.get("valeur") == 1 else None
    meme, autre = [0, 0], [0, 0]
    for c in CRITERES:
        for i in reelles:
            for L in PASSAGES:
                x, y = cite(A, L, i, c), cite(B, L, i, c)
                if x is not None and y is not None:
                    meme[0] += 1
                    meme[1] += int(x == y)
            for X in (A, B):
                x, y = cite(X, "L1", i, c), cite(X, "L2", i, c)
                if x is not None and y is not None:
                    autre[0] += 1
                    autre[1] += int(x == y)
    libres = {"meme_passage_entre_lectures": [0, 0], "entre_passages_d_une_meme_lecture": [0, 0]}
    def motif(X, L, i, c):
        r = X["entrees"][(L, i)]["brut"].get(c) or {}
        return r.get("motif") if r.get("valeur") == 0 else None
    for c in CRITERES:
        for i in reelles:
            for L in PASSAGES:
                x, y = motif(A, L, i, c), motif(B, L, i, c)
                if x is not None and y is not None:
                    libres["meme_passage_entre_lectures"][0] += 1
                    libres["meme_passage_entre_lectures"][1] += int(x == y)
            for X in (A, B):
                x, y = motif(X, "L1", i, c), motif(X, "L2", i, c)
                if x is not None and y is not None:
                    libres["entre_passages_d_une_meme_lecture"][0] += 1
                    libres["entre_passages_d_une_meme_lecture"][1] += int(x == y)
    res["motif_libre_identique_au_caractere_quand_deux_non"] = {k: f"{v[1]} sur {v[0]}" for k, v in libres.items()}
    entieres = {"identiques": 0, "dont_avec_un_motif_libre": 0, "dont_sept_oui_cites": 0}
    for L in PASSAGES:
        for i in reelles:
            x = {k: v for k, v in A["entrees"][(L, i)]["brut"].items() if k != "etiquette"}
            y = {k: v for k, v in B["entrees"][(L, i)]["brut"].items() if k != "etiquette"}
            if x == y:
                entieres["identiques"] += 1
                a_motif = any(isinstance(v, dict) and "motif" in v for v in x.values())
                entieres["dont_avec_un_motif_libre"] += int(a_motif)
                entieres["dont_sept_oui_cites"] += int(all(x[c].get("valeur") == 1 for c in CRITERES))
    res["entrees_entieres_identiques_meme_passage_entre_lectures_sur_46"] = entieres
    non_constants = [c for c in CRITERES if c != "R7" and res[c]["oui_sur_les_quatre_passages"].split(" sur ")[0]
                     != res[c]["oui_sur_les_quatre_passages"].split(" sur ")[1]]
    cel = sum(int(res[c]["meme_passage_entre_lectures_changees"].split(" sur ")[1]) for c in non_constants)
    cha = sum(int(res[c]["meme_passage_entre_lectures_changees"].split(" sur ")[0]) for c in non_constants)
    res["criteres_non_constants_hors_R7_meme_passage_entre_lectures"] = {
        "criteres": non_constants, "cellules": cel, "changees": cha, "taux": round(cha / cel, 5)}
    res["passage_cite_identique_au_caractere_quand_deux_oui"] = {
        "meme_passage_entre_lectures": f"{meme[1]} sur {meme[0]}", "taux_meme_passage": round(meme[1] / meme[0], 4),
        "entre_passages_d_une_meme_lecture": f"{autre[1]} sur {autre[0]}",
        "taux_entre_passages": round(autre[1] / autre[0], 4)}
    return res


# --- probabilités d'un accord parfait des valeurs retenues ----------------------------------------------------------------

def modele_classes_latentes(n11: int, n10: int, n00: int, comptes_cibles: tuple) -> dict:
    """Passages échangeables ; chaque fiche a une vraie valeur, chaque passage se trompe avec la probabilité e,
    indépendamment. e et la part pi de fiches « vraies 1 » sont ajustés sur une lecture (modèle juste identifié) ; on
    prédit ensuite, fiche par fiche selon son motif à la première lecture, que la valeur retenue se répète."""
    n = n11 + n10 + n00
    d = n10 / n
    e = (1 - math.sqrt(1 - 2 * d)) / 2
    pi = (n11 / n - e * e) / ((1 - e) ** 2 - e * e)
    def post(k):  # P(vraie valeur 1 | k oui sur 2)
        l1 = pi * (1 - e) ** k * e ** (2 - k)
        l0 = (1 - pi) * e ** k * (1 - e) ** (2 - k)
        return l1 / (l1 + l0)
    def p11(k):  # P(les deux passages suivants disent oui | k)
        return post(k) * (1 - e) ** 2 + (1 - post(k)) * e ** 2
    m11, m10, m00 = comptes_cibles
    par = {"deux_oui": p11(2), "un_seul_oui": 1 - p11(1), "aucun_oui": 1 - p11(0)}
    p = par["deux_oui"] ** m11 * par["un_seul_oui"] ** m10 * par["aucun_oui"] ** m00
    return {"erreur_par_passage": round(e, 5), "part_de_vraies_1": round(pi, 5),
            "probabilite_que_le_retenu_se_repete_par_motif": {k: round(v, 5) for k, v in par.items()},
            "probabilite_accord_parfait": round(p, 6)}


def modele_beta_binomial(n11: int, n10: int, n00: int, comptes_cibles: tuple) -> dict:
    """Passages échangeables ; chaque fiche a sa propre probabilité de « oui », tirée d'une loi bêta(a, b) ajustée sur
    une lecture (deux paramètres, juste identifié) ; prédiction a posteriori fiche par fiche."""
    n = n11 + n10 + n00
    mu = (2 * n11 + n10) / (2 * n)
    rho = 1 - (n10 / n) / (2 * mu * (1 - mu))      # corrélation entre deux passages
    s = 1 / rho - 1
    a, b = mu * s, (1 - mu) * s
    def p11(k):
        return (a + k) * (a + k + 1) / ((s + 2) * (s + 3))
    m11, m10, m00 = comptes_cibles
    par = {"deux_oui": p11(2), "un_seul_oui": 1 - p11(1), "aucun_oui": 1 - p11(0)}
    p = par["deux_oui"] ** m11 * par["un_seul_oui"] ** m10 * par["aucun_oui"] ** m00
    return {"a": round(a, 5), "b": round(b, 5), "correlation_entre_passages": round(rho, 5),
            "probabilite_que_le_retenu_se_repete_par_motif": {k: round(v, 5) for k, v in par.items()},
            "probabilite_accord_parfait": round(p, 6)}


def modele_contexte_fixe(r: float, comptes: tuple) -> float:
    """Chaque passage est un contexte fixe (même étiquette, même lot, même rang) ; rejoué, il change de valeur avec la
    probabilité r, indépendamment. La valeur retenue (« et ») se répète si : motif 11 → aucun des deux ne change ;
    motif 00 → pas les deux à la fois ; motif 10 ou 01 → pas « le 0 change et le 1 tient »."""
    m11, m10, m00 = comptes
    return (1 - r) ** (2 * m11) * (1 - r * (1 - r)) ** m10 * (1 - r * r) ** m00


def seuil(comptes: tuple, cible: float) -> float:
    lo, hi = 0.0, 0.5
    for _ in range(80):
        mid = (lo + hi) / 2
        if modele_contexte_fixe(mid, comptes) > cible:
            lo = mid
        else:
            hi = mid
    return round(lo, 5)


def probabilites(A: dict, B: dict, reelles: list, t7: dict, tc: dict) -> dict:
    ca = t7["comptes_premiere_lecture"]
    comptes = (ca["deux_oui"], ca["un_seul_oui"], ca["aucun_oui"])
    # ajustement de rechange sur toute la pile de la première lecture (43 fiches)
    pa = [valeurs(A, i, "R7") for i in A["ordre_pile"]]
    pile = (sum(1 for x in pa if x == (1, 1)), sum(1 for x in pa if x[0] != x[1]), sum(1 for x in pa if x == (0, 0)))
    r_r7 = t7["valeurs_de_passage_changees_entre_lectures"]["nombre_sur_46"] / 46
    r_autres = tc["R1_a_R6_ensemble_meme_passage_entre_lectures"]["taux"]
    r_nc = tc["criteres_non_constants_hors_R7_meme_passage_entre_lectures"]["taux"]
    d_a = ca["un_seul_oui"] / len(reelles)
    grille = {f"{r:.3f}": round(modele_contexte_fixe(r, comptes), 5) for r in (0.0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10,
                                                                               0.15, 0.20)}
    return {
        "motifs_de_la_premiere_lecture_fiches_reelles": {"deux_oui": comptes[0], "un_seul_oui": comptes[1],
                                                         "aucun_oui": comptes[2]},
        "motifs_de_la_premiere_lecture_pile_entiere": {"deux_oui": pile[0], "un_seul_oui": pile[1],
                                                       "aucun_oui": pile[2]},
        "A_passages_echangeables": {
            "lecture": "le désaccord entre passages est pris pour du bruit de rejeu ; ajusté sur la première lecture "
                       "seule, puis prédit sur les 23 fiches réelles",
            "classes_latentes_ajuste_sur_les_23_reelles": modele_classes_latentes(*comptes, comptes),
            "classes_latentes_ajuste_sur_la_pile_de_43": modele_classes_latentes(*pile, comptes),
            "beta_binomial_ajuste_sur_les_23_reelles": modele_beta_binomial(*comptes, comptes),
            "beta_binomial_ajuste_sur_la_pile_de_43": modele_beta_binomial(*pile, comptes)},
        "B_contexte_fixe": {
            "lecture": "chaque passage est un contexte rejoué à l'identique ; r = probabilité qu'une valeur de passage "
                       "change au rejeu",
            "formule": "(1-r)^(2·n11) · (1-r(1-r))^(n10) · (1-r²)^(n00)",
            "grille_r_vers_probabilite": grille,
            "r_estime_sur_R1_a_R6_meme_passage_entre_lectures": r_autres,
            "probabilite_a_ce_r": round(modele_contexte_fixe(r_autres, comptes), 5),
            "r_estime_sur_les_criteres_non_constants_hors_R7": r_nc,
            "probabilite_a_ce_r_non_constants": round(modele_contexte_fixe(r_nc, comptes), 5),
            "r_observe_sur_R7_meme_passage_entre_lectures_circulaire": round(r_r7, 5),
            "probabilite_a_ce_r_circulaire": round(modele_contexte_fixe(r_r7, comptes), 5),
            "r_egal_au_desaccord_entre_passages_de_la_premiere_lecture": round(d_a, 5),
            "probabilite_a_ce_r_si_le_desaccord_entre_passages_etait_du_bruit": round(
                modele_contexte_fixe(d_a, comptes), 5),
            "r_maximal_pour_une_probabilite_de_0_05": seuil(comptes, 0.05),
            "r_maximal_pour_une_probabilite_de_0_50": seuil(comptes, 0.50)},
        "C_sans_la_regle_du_et": {
            "lecture": "probabilité que les 46 valeurs de passage soient toutes répétées : (1-r)^46",
            "a_r_estime_sur_R1_a_R6": round((1 - r_autres) ** 46, 5),
            "a_r_estime_sur_les_criteres_non_constants_hors_R7": round((1 - r_nc) ** 46, 5),
            "a_r_observe_sur_R7": round((1 - r_r7) ** 46, 5)},
    }


# --- programme -----------------------------------------------------------------------------------------------------------

def calculer(racine: Path) -> dict:
    A, B = charger(racine, "premiere"), charger(racine, "relecture")
    for rel in (f"{OUT}/outil_lecteur_conception_propre_v3_2_1.py", f"{OUT}/classer_conception_propre_v3_2_1.py",
                f"{RE_}/regle-v2-1.md", f"{RE_}/regle-v2.md", f"{RE_}/commandes-exactes-v3.md",
                f"{RE_}/lecture-exploratoire-classement-v3-2-v1.md",
                f"{DOS}/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py",
                f"{DOS}/lecture-classement-v3-1/classer_conception_propre_v3_1.py"):
        lire(racine, rel)
    for X in (A, B):
        d, suf, _ = LECTURES[X["nom"]]
        k = 1
        while (racine / f"{DOS}/{d}/envois/releve-depense-{suf}-{k}.json").is_file():
            X.setdefault("releves", []).append(lire_json(racine, f"{DOS}/{d}/envois/releve-depense-{suf}-{k}.json"))
            k += 1
    reelles = [i for i in A["ordre_pile"] if A["pile"][i]["origine"] == "reelle"]
    if reelles != [i for i in B["ordre_pile"] if B["pile"][i]["origine"] == "reelle"]:
        raise Ecart("fiches réelles différentes entre les deux piles")
    t7 = tableau_r7(A, B, reelles)
    tc = tous_criteres(A, B, reelles)
    outil = (racine / f"{OUT}/outil_lecteur_conception_propre_v3_2_1.py").read_text(encoding="utf-8")
    classer = (racine / f"{OUT}/classer_conception_propre_v3_2_1.py").read_text(encoding="utf-8")
    code = {
        "ligne_du_et_presente_dans_le_classement": (
            'vec = {c: int(v1[c]["compte"] == 1 and v2[c]["compte"] == 1) for c in CRITERES}' in classer),
        "epingle_du_journal_de_la_premiere_lecture_dans_l_outil": JOURNAL_PREMIERE_EPINGLE in outil,
        "lignes_de_l_outil_qui_nomment_le_dossier_de_la_premiere_lecture": sum(
            1 for x in outil.splitlines() if "lecture-g1-v3-1" in x),
        "lignes_du_classement_qui_nomment_le_dossier_de_la_premiere_lecture": sum(
            1 for x in classer.splitlines() if "lecture-g1-v3-1" in x),
        "lignes_de_l_outil_qui_nomment_une_reponse_de_la_premiere_lecture": sum(
            1 for x in outil.splitlines() if "reponse-" in x and "v3-1" in x),
    }
    man = json.loads((racine / f"{DOS}/lecture-g1-v3-2/envois/manifeste-relecture-v3-2.json").read_text("utf-8"))
    man1 = json.loads((racine / f"{DOS}/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json").read_text("utf-8"))
    code["version_au_manifeste_de_la_relecture"] = man.get("version")
    code["version_au_classement_de_la_relecture"] = B["classement"].get("version")
    code["empreinte_de_l_outil_egale_a_celle_du_manifeste_de_la_relecture"] = (
        man.get("outil_sha256") == PIECES[f"{OUT}/outil_lecteur_conception_propre_v3_2_1.py"]["sha256"])
    code["pieces_servies_a_la_meme_empreinte_dans_les_deux_manifestes"] = sorted(
        k for k in man["pieces"] if k in man1["pieces"] and man["pieces"][k]["sha256"] == man1["pieces"][k]["sha256"])
    code["pieces_servies_changees_ou_propres_a_une_lecture"] = sorted(
        k for k in set(man["pieces"]) | set(man1["pieces"])
        if man["pieces"].get(k, {}).get("sha256") != man1["pieces"].get(k, {}).get("sha256"))
    code["graines_des_ordres_egales_dans_les_deux_manifestes"] = man.get("graines") == man1.get("graines")
    code["reponses_attendues_de_la_relecture_toutes_au_suffixe_v3_2"] = all(
        x.endswith("-v3-2.json") for x in man.get("reponses_attendues", []))
    L4 = {X["nom"]: X["classement"].get("L4") for X in (A, B)}
    res = {
        "version": "calculs-audit-r7-v1",
        "1_regle": {X["nom"]: controle_regle(X) for X in (A, B)},
        "1_code": code,
        "2_appels": controle_appels(A, B),
        "2_releves": {X["nom"]: [{"fin_utc": r["fin_utc"], "issue": r["issue"],
                                  "envoyes_cette_fois": r["envoyes_cette_fois"], "appels": r["appels"],
                                  "depense_comptee_usd": r["depense_comptee_usd"]} for r in X["releves"]]
                      for X in (A, B)},
        "2_contexte_servi": controle_contexte(A, B, reelles),
        "2_R7_fiches_reelles": t7,
        "2_R7_preuve_refaite": {X["nom"]: preuve_r7(X, reelles) for X in (A, B)},
        "2_R7_textes": textes_r7(A, B, reelles),
        "2_tous_criteres_fiches_reelles": tc,
        "2_L4_des_classements_pile_entiere": L4,
        "2_relecture_contre_premiere_du_classement_R7": (B["classement"].get("relecture_contre_premiere_lecture") or {})
        .get("par_critere", {}).get("R7"),
        "3_probabilites": probabilites(A, B, reelles, t7, tc),
        "pieces_lues": {rel: {"sha256_8": v["sha256_8"], "compagnon": v["compagnon"]} for rel, v in sorted(PIECES.items())},
        "pieces_sans_compagnon": sorted(rel for rel, v in PIECES.items() if v["compagnon"] == "absent"),
    }
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", default=".")
    ap.add_argument("--sortie", default=None)
    args = ap.parse_args(argv)
    res = calculer(Path(args.racine).resolve())
    texte = json.dumps(res, ensure_ascii=False, indent=1, allow_nan=False) + "\n"
    if args.sortie:
        p = Path(args.sortie)
        if p.exists() or Path(str(p) + ".sha256").exists():
            print(f"{p} existe : on n'écrase jamais (R12)", file=sys.stderr)
            return 2
        p.write_text(texte, encoding="utf-8")
    else:
        sys.stdout.write(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
