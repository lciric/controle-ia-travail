#!/usr/bin/env python3
"""Essai de composition du rédacteur des fragments (mode essai seulement, racine 2026111930, sortie sous mon dossier).

Ne lance jamais la garde de recouvrement, n'ouvre jamais le fichier des cartes, ne fait aucun appel réseau.
Usage : python3 -I -B essai_composition.py valider | stats | composer N | v2
"""
import hashlib
import importlib.util
import json
import os
import statistics
import sys
from pathlib import Path

ICI = Path(os.path.dirname(os.path.abspath(__file__)))
FRAGMENTS = ICI / "fragments-etage-2-ligne-3-v1.json"
GENERATEUR = ICI / "generer_temoins_ligne_3_v2.py"
EMPREINTE_GENERATEUR = "a3a4e82f15afbabfb53a954e24ed9db709c5d8f2da5f907978e7612e3fddca65"


def charger_generateur():
    if hashlib.sha256(GENERATEUR.read_bytes()).hexdigest() != EMPREINTE_GENERATEUR:
        raise SystemExit("copie du générateur : empreinte différente")
    spec = importlib.util.spec_from_file_location("gen_l3_v2", str(GENERATEUR))
    m = importlib.util.module_from_spec(spec)
    sys.modules["gen_l3_v2"] = m
    spec.loader.exec_module(m)
    return m


def valider(gen):
    objet = json.loads(FRAGMENTS.read_text(encoding="utf-8"))
    conf = gen.lire_configuration()
    interdites = conf["etiquettes_interdites_fixes"]
    try:
        fr = gen.valider_fragments(objet, interdites)
    except gen.FragmentsRefuses as e:
        print("REFUS :", len(e.fautes), "faute(s)")
        for f in e.fautes:
            print(" -", f)
        raise SystemExit(2)
    return fr, interdites, conf


def traits_fragment(gen, f):
    champs = f["champs"]
    texte = " ".join(champs.values())
    return {"longueur": sum(len(v) for v in champs.values()),
            "phrases": sum(gen.phrases(v) for v in champs.values()),
            "chiffres": sum(ch.isdigit() for ch in texte),
            "modules": len(gen.modules_nommes(texte)),
            "non_verifie": gen.compte_non_verifie(texte),
            "predit": gen.compte_predit(texte),
            **{"L:" + k: len(v) for k, v in champs.items()},
            **{"P:" + k: gen.phrases(v) for k, v in champs.items()}}


def resume(valeurs):
    if not valeurs:
        return "—"
    return f"n={len(valeurs)} moy={statistics.mean(valeurs):.1f} min={min(valeurs)} max={max(valeurs)}"


def stats(gen, fr):
    print("== comptes ==")
    for cat in gen.CATEGORIES:
        c = fr["conformes"][cat]
        print(cat, "simples non citants", sum(1 for f in c if f["piege"] is None and not f["citation"]),
              "| simples citants", sum(1 for f in c if f["piege"] is None and f["citation"]),
              "| pièges", {p: sum(1 for f in c if f["piege"] == p) for p in gen.PIEGES})
    for it in gen.ITEMS:
        for niv in gen.NIVEAUX:
            g = [f for f in fr["fautifs"] if f["item"] == it and f["niveau"] == niv]
            cats = {}
            for f in g:
                cats[f["categorie"]] = cats.get(f["categorie"], 0) + 1
            print(it, niv, "total", len(g), "non citants", sum(1 for f in g if not f["citation"]), cats)
    print("== traits par catégorie : simples non citants / simples citants / pièges / fautifs par item ==")
    for cat in gen.CATEGORIES:
        groupes = {"simples-nc": [f for f in fr["conformes"][cat] if f["piege"] is None and not f["citation"]],
                   "simples-cit": [f for f in fr["conformes"][cat] if f["piege"] is None and f["citation"]],
                   "pieges": [f for f in fr["conformes"][cat] if f["piege"] is not None]}
        for it in gen.ITEMS:
            g = [f for f in fr["fautifs"] if f["item"] == it and f["categorie"] == cat]
            if g:
                groupes["fautifs:" + it] = g
        print("---", cat)
        cles = None
        for nom, g in groupes.items():
            t = [traits_fragment(gen, f) for f in g]
            if not t:
                continue
            cles = cles or list(t[0])
            print("  [" + nom + "]")
            for k in cles:
                print("     ", k, resume([x[k] for x in t]))
    print("== longueurs par fragment ==")
    for cat in gen.CATEGORIES:
        for f in fr["conformes"][cat]:
            print(cat, f["id"], sum(len(v) for v in f["champs"].values()))
    for f in fr["fautifs"]:
        print(f["categorie"], f["id"], sum(len(v) for v in f["champs"].values()))


def service_essai(gen, consigne, interdites):
    def entree_une_fiche(consigne_, fiche, interdites_, identifiant_servi=None):
        corps = dict(fiche["contenu"])
        servi = {"identifiant": identifiant_servi}
        servi.update(corps)
        return consigne_ + "\n\n" + gen.MARQUE_FICHE + json.dumps(servi, ensure_ascii=False, indent=1) + "\n```\n"

    def lire_verdict(reponse, items):
        corps = reponse.split("```json\n", 1)[1].rsplit("\n```", 1)[0]
        return json.loads(corps)

    return gen.ServiceAudit(nature="essai", entree_une_fiche=entree_une_fiche, lire_verdict=lire_verdict,
                            consigne=consigne, items=list(gen.ITEMS), interdites=interdites)


def composer(gen, tour):
    fr, interdites, conf = valider(gen)
    h = hashlib.sha256(FRAGMENTS.read_bytes()).hexdigest()
    racine = ICI / "essais"
    racine.mkdir(exist_ok=True)
    sortie = racine / f"tour-{tour}"
    ctx = gen.Contexte("essais")
    try:
        res = gen.geste_composer(str(FRAGMENTS), h, str(sortie), ctx, interdites, tuple(conf["items_juge"]))
    except gen.Refus as e:
        print("REFUS de composition :", type(e).__name__, str(e))
        raise SystemExit(2)
    banque, journal = res["banque"], res["journal"]
    print("fragments sha256 :", h)
    print("comptes :", json.dumps(gen.comptes_de_la_banque(banque), ensure_ascii=False))
    print("contenus identiques : 0 (vérifié par le générateur)")
    print("fragments communs :", json.dumps(res["communs"], ensure_ascii=False))
    L = [j["longueur"] for j in journal]
    print("longueurs : min", min(L), "max", max(L))
    print("tirages : max", max(j["tirages"] for j in journal), "moyenne", statistics.mean(j["tirages"] for j in journal))
    usages = {}
    for j in journal:
        for fid in j["fragments"].values():
            usages[fid] = usages.get(fid, 0) + 1
    print("fragments jamais employés :", sorted(set(fr["par_id"]) - set(usages)))
    print("usage maximal d'un fragment :", max(usages.values()), [k for k, v in usages.items() if v == max(usages.values())])
    print("empreintes des sorties :", json.dumps(res["empreintes"], ensure_ascii=False))
    consigne = gen.lire_par_empreinte(gen.DEPOT / gen.CONSIGNE_JUGE[0], gen.CONSIGNE_JUGE[1], "consigne").decode("utf-8")
    ctx_a = gen.Contexte("essais")
    rapport = gen.auditer(banque, ctx_a, service_essai(gen, consigne, interdites))
    print("AUDIT décision :", rapport["decision"], rapport["motifs_de_refus"])
    print("  aire qui décide :", rapport["aire_qui_decide"]["aire"], "convergence", rapport["aire_qui_decide"]["convergence"])
    print("  aire à tous les traits :", rapport["aire_a_tous_les_traits"]["aire"])
    for k, v in rapport["traits_de_la_lettre"].items():
        print("  lettre", k, v["aire"], v["dans_la_bande"], v["bons"], v["mauvais"])
    for g in ("parfait", "longueur", "champ_lu", "citation"):
        print("  juge scripté", g, rapport["juges_scriptes_de_surface"][g]["erreur_equilibree"])
    with open(sortie / "rapport-audit-essai.json", "x", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1, sort_keys=True)
    # diagnostic : moyennes des traits de présentation par classe, et aire de chaque trait seul
    import numpy as np
    y = np.array([t["classe"] == "mauvais" for t in banque], dtype=float)
    Xp = np.array([gen.traits_presentation(t["contenu"], t["citation"]) for t in banque])
    print("  traits seuls (aire, moyenne bons, moyenne mauvais) :")
    for k, nom in enumerate(gen.NOMS_TRAITS_PRESENTATION):
        a = float(gen.aire_par_rangs(Xp[:, k], y))
        if abs(a - 0.5) >= 0.04:
            print("    ", nom, round(a, 3), round(float(Xp[y == 0, k].mean()), 1), round(float(Xp[y == 1, k].mean()), 1))
    for it in gen.ITEMS:
        idx = np.array([t["classe"] == "bon" or t["item"] == it for t in banque])
        ligne = []
        for k, nom in enumerate(gen.NOMS_TRAITS_PRESENTATION):
            a = float(gen.aire_par_rangs(Xp[idx, k], y[idx]))
            if abs(a - 0.5) >= 0.12:
                ligne.append(f"{nom}={a:.2f}")
        print("    item", it, "(20 mauvais contre 100 bons) :", ", ".join(ligne) or "rien au-delà de 0,12")


def bardeaux(gen, texte, n=8):
    m = gen.mots(texte)
    return {" ".join(m[i:i + n]) for i in range(len(m) - n + 1)}


def controle_v2(gen):
    """Contrôle propre au rédacteur : bardeaux de huit mots communs entre mes fragments et les onze témoins v2 ou la
    consigne figée. Ce n'est pas la garde de recouvrement : aucune carte de la course n'est ouverte."""
    fr, _, _ = valider(gen)
    v2 = json.loads(gen.lire_par_empreinte(gen.DEPOT / gen.TEMOINS_V2[0], gen.TEMOINS_V2[1], "témoins v2").decode("utf-8"))
    consigne = gen.lire_par_empreinte(gen.DEPOT / gen.CONSIGNE_JUGE[0], gen.CONSIGNE_JUGE[1], "consigne").decode("utf-8")
    ref = set()
    for t in v2["temoins"]:
        for v in t["contenu"].values():
            ref |= bardeaux(gen, v)
    ref_c = bardeaux(gen, consigne)
    n = 0
    for fid, f in fr["par_id"].items():
        for k, v in f["champs"].items():
            b = bardeaux(gen, v)
            c1, c2 = b & ref, b & ref_c
            if c1 or c2:
                n += 1
                print(fid, k, "communs avec v2 :", sorted(c1), "| avec la consigne :", sorted(c2))
    print("champs de fragments avec un bardeau commun :", n)
    # entre fragments : bardeaux de huit mots partagés par deux fragments différents (information)
    vus = {}
    partages = {}
    for fid, f in fr["par_id"].items():
        for v in f["champs"].values():
            for b in bardeaux(gen, v):
                if b in vus and vus[b] != fid:
                    partages[(vus[b], fid)] = partages.get((vus[b], fid), 0) + 1
                vus.setdefault(b, fid)
    print("paires de fragments qui partagent un bardeau de huit mots :", len(partages))
    for (a, b), c in sorted(partages.items()):
        print("  ", a, b, c)


def main():
    gen = charger_generateur()
    geste = sys.argv[1] if len(sys.argv) > 1 else "valider"
    if geste == "valider":
        valider(gen)
        print("schéma : passe valider_fragments")
    elif geste == "stats":
        fr, _, _ = valider(gen)
        stats(gen, fr)
    elif geste == "composer":
        composer(gen, int(sys.argv[2]))
    elif geste == "v2":
        controle_v2(gen)
    else:
        raise SystemExit("geste inconnu")


if __name__ == "__main__":
    main()
