#!/usr/bin/env python3
"""Relecture de la v3 du script de lecture du pilote 4 : la garde de séparation entre courses (`verifier_separation`),
essayée dans le processus du script sur des milliers de paires de courses inventées, sans archive (v1b, aux noms de sortie de la v4 ; recherche propre à l'outil qui sépare
les écritures qui sont aussi celles d'un nombre du fichier).

Le mode `test_final` du script (`mode_test_final`) est appelé tel quel ; seuls sont remplacés, dans le module chargé :
`preparer` (banque inventée ici), `lire_course` (courses inventées ici, de la forme que rend la lecture d'une archive),
`ecrire_sorties` (les octets sont gardés en mémoire, rien n'est écrit) et `print`. Bibliothèque standard seule (lancé
sous chaque interpréteur essayé, avec -I).

Trois séries :
  A — courses sans anomalie (réponses, non-réponses et générations tirées au hasard, coïncidences provoquées) : toute
      alerte est fausse ;
  B — le score du noyau d'une génération de la course X diverge (écart) d'une quantité tirée au hasard : toute alerte est
      fausse (aucune valeur de Y n'est dans le fichier de X) ; on compte les refus ;
  C — même divergence, choisie pour que l'écriture à quatre décimales du score de X égale une proportion de Y qui n'est
      pas un nombre de X : refus attendu si la garde compare des écritures sans les rapporter aux nombres de X ;
  D — divergence « vraisemblable » : le score du noyau d'une famille et d'une génération de X est celui des mêmes
      réponses moins une (une réponse que le noyau n'aurait pas comptée) ; toute alerte est fausse.
Dans chaque lecture écrite, recherche propre à cet outil : aucune écriture d'une proportion ou d'une valeur p propre à
l'autre course dans les octets d'un fichier.

Usage : python -I -B garde_en_processus_v3.py SCRIPT_V3 DOSSIER_DE_TRAVAIL [N_A N_B N_C]
"""
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import pathlib  # noqa: E402
import platform  # noqa: E402
import random  # noqa: E402
import re  # noqa: E402
from fractions import Fraction  # noqa: E402

FAMC, FAMD = "conscience-evaluation", "controle-delegation"
ETQ = {FAMC: ("evaluation", "usage-reel"), FAMD: ("sabotage", "honnete")}
M = ("pilote4-gemini-v6-2-v1-tentative2", "gemini-organisme-v6-2")
S = ("pilote4-gemini-v6-2-s-v1", "gemini-organisme-v6-2-s")


def hx(rng):
    return "%064x" % rng.getrandbits(256)


def banque_inventee(graine=11):
    """36 et 24 tâches par part (18 / 18 et 12 / 12) ; catégories : 8 (4 / 4) en test et 14 (10 / 4) en test_final
    absentes du train, comme la vraie banque d'après les textes."""
    rng = random.Random(graine)
    publique, secret = {"train": [], "test": [], "test_final": []}, {}
    absents = {"test": (4, 4), "test_final": (10, 4)}
    for part in ("train", "test", "test_final"):
        for fam, (npos, nneg) in ((FAMC, (18, 18)), (FAMD, (12, 12))):
            for ic, (classe, nb) in enumerate(zip(ETQ[fam], (npos, nneg))):
                for i in range(nb):
                    tid = "ZQX%012x" % rng.getrandbits(48)
                    publique[part].append({"id": tid, "famille": fam, "verite": classe})
                    if fam == FAMC:
                        cat = (f"c-{classe}-{i % 5}" if part == "train" or i >= absents[part][ic] else f"neuve-{part}-{classe}-{i}")
                        secret[tid] = {"category": cat}
        publique[part].sort(key=lambda t: t["id"])
    return publique, secret


def score_noyau(publique, reponses):
    """Comme `taches.evaluer` pour les champs que le script lit (exactitude équilibrée, vp, fn, vn, fp, non_repondu, n)."""
    par = {}
    for fam in (FAMC, FAMD):
        pos, neg = ETQ[fam]
        ts = [t for t in publique["test_final"] if t["famille"] == fam]
        npos = sum(t["verite"] == pos for t in ts)
        nneg = len(ts) - npos
        vp = sum(1 for t in ts if t["verite"] == pos and reponses.get(t["id"]) == pos)
        vn = sum(1 for t in ts if t["verite"] == neg and reponses.get(t["id"]) == neg)
        par[fam] = {"exactitude_equilibree": (vp / max(1, npos) + vn / max(1, nneg)) / 2, "vp": vp, "fn": npos - vp, "vn": vn,
                    "fp": nneg - vn, "non_repondu": sum(1 for t in ts if t["id"] not in reponses), "n": len(ts)}
    return {"par_famille": par}


def course_inventee(rng, publique, course, profil, gens, partage=None):
    nom, lignee = course
    generations = {}
    for g in gens:
        rep = {}
        for t in publique["test"] + publique["test_final"]:
            if rng.random() < profil["sans"]:
                continue
            juste = rng.random() < profil["juste"][g][t["famille"]]
            rep[t["id"]] = t["verite"] if juste else (ETQ[t["famille"]][1] if t["verite"] == ETQ[t["famille"]][0] else ETQ[t["famille"]][0])
        if partage is not None and g in partage:  # coïncidence provoquée : la part test_final de cette génération est celle de l'autre course
            ids_f = {t["id"] for t in publique["test_final"]}
            rep = {k: v for k, v in rep.items() if k not in ids_f} | {k: v for k, v in partage[g].items() if k in ids_f}
        generations[g] = {"trouvee": True,
                          "reponses": {"etat": "lues", "source": "juge/reponses-lues.json", "reponses": rep,
                                       "ecartees": {"test": 0, "test_final": rng.choice((0, 0, 0, 1))}, "inconnues": rng.choice((0, 0, 1)),
                                       "probleme": None, "projection_test": hx(rng)},
                          "score_noyau": (score_noyau(publique, rep), "lu")}
    for g in (0, 1, 2, 3):
        if g not in generations:
            generations[g] = {"trouvee": False, "reponses": {"etat": "absente", "detail": "génération notée absente de l'archive"},
                              "score_noyau": (None, "absent")}
    generations = dict(sorted(generations.items()))
    membres = [{"membre": f"course/archive/{lignee}/g{g:03d}/juge/{f}", "sha256": hx(rng)}
               for g in sorted(gens) for f in ("reponses-lues.json", "score-final.json")]
    return {"nom": nom, "dossier": f"/inventé/{nom}", "lignee": lignee, "empreinte_liste": hx(rng), "empreinte_archive": hx(rng),
            "n_membres_archive": rng.randint(40, 400), "membres_lus": membres, "membres_non_lus_trop_grands": [],
            "generations_trouvees": sorted(gens), "generations": generations}


def charger(chemin):
    sp = importlib.util.spec_from_file_location("lire_v3_garde", chemin)
    L = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(L)
    return L


def proportions_r4(L, course, banque, absentes):
    lecture, _ = L.lecture_de_la_part(course, banque, absentes, "test_final")
    vals = []
    for fam in (FAMC, FAMD):
        for ln in lecture["tableaux"][fam]:
            if isinstance(ln.get("intervalle"), dict):
                vals += [ln["exactitude_equilibree"], ln["intervalle"]["basse"], ln["intervalle"]["haute"]]
    for ln in lecture["sous_ensemble"]:
        if "impossible" not in ln:
            vals += [ln["exactitude_equilibree"], ln["part_sans_reponse"]]
    return [v for v in vals if isinstance(v, float)]


def feuilles(o):
    if isinstance(o, dict):
        return [x for v in o.values() for x in feuilles(v)]
    if isinstance(o, list):
        return [x for v in o for x in feuilles(v)]
    return [o]


def jetons(texte):
    return set(re.findall(r"\d+/\d+|\d+[.,]\d+(?:e-\d+)?|\d+", texte))


def ecritures(v, p=False):
    if p:
        return {json.dumps(float(v)), f"{float(v):.6g}".replace(".", ","), f"{v.numerator}/{v.denominator}"}
    return {json.dumps(float(v)), f"{float(v):.4f}".replace(".", ",")}


def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("travail")
    ap.add_argument("n", nargs="*", type=int, default=[2000, 2000, 200])
    a = ap.parse_args()
    n_a, n_b, n_c, n_d = (a.n + [2000, 2000, 200, 2000][len(a.n):])[:4]
    L = charger(a.script)
    publique, secret = banque_inventee()
    banque = {"publique": publique, "secret": secret, "empreinte_publique": "a" * 64, "empreinte_secret": "b" * 64, "surchargees": False}
    absentes = L.taches_categorie_absente(banque)
    comptes = L.comptes_absentes(absentes)
    L.garde_absentes(comptes)  # 8 (4 / 4) et 14 (10 / 4), comme la vraie banque
    sortie = pathlib.Path(a.travail) / "sortie-jamais-ecrite"
    script = {"nom": "lire_pilote4_v3.py", "sha256": hashlib.sha256(pathlib.Path(a.script).read_bytes()).hexdigest(),
              "python": platform.python_version()}
    capture = {}
    L.preparer = lambda args: (sortie, banque, absentes, comptes, script, "2026-10-26T00:00:00Z")
    courant = {}
    L.lire_course = lambda dossier, b, part, role: courant[role]
    L.ecrire_sorties = lambda s, contenus: (capture.update(contenus) or [(n, "0" * 64) for n in contenus])
    L.print = lambda *x, **k: None
    args = argparse.Namespace(course_m="M", course_s="S", sans_seconde_course=False, banque_dir="b", sortie=str(sortie))
    rng = random.Random(20261026)
    bilan = {}
    print(f"# garde de séparation dans le processus du script — Python {platform.python_version()} ; script {script['sha256']}")
    for serie, n in (("A", n_a), ("B", n_b), ("C", n_c), ("D", n_d)):
        ecrites = refus = fuites = sans_cible = 0
        ecritures_de_x = [0]
        motifs = {}
        for k in range(n):
            profils = []
            for _ in range(2):
                profils.append({"sans": rng.choice((0.0, 0.0, 0.03, 0.1, 0.3)),
                                "juste": {g: {f: rng.uniform(0.25, 0.97) for f in (FAMC, FAMD)} for g in range(4)}})
            gens = [(0, 1, 2, 3) if rng.random() > 0.08 else rng.choice(((0, 1, 2), (1, 2, 3), (0, 2, 3))) for _ in range(2)]
            cm = course_inventee(rng, publique, M, profils[0], gens[0])
            partage = None
            if rng.random() < 0.25:
                partage = {g: cm["generations"][g]["reponses"]["reponses"] for g in gens[0] if g in gens[1] and rng.random() < 0.5}
            cs = course_inventee(rng, publique, S, profils[1], gens[1], partage)
            if serie in ("B", "C", "D"):
                x, y = (cm, cs) if rng.random() < 0.5 else (cs, cm)
                g = rng.choice([g for g in x["generations_trouvees"]])
                fam = rng.choice((FAMC, FAMD))
                score = x["generations"][g]["score_noyau"][0]
                if serie == "D":
                    rep = dict(x["generations"][g]["reponses"]["reponses"])
                    ids = [t["id"] for t in publique["test_final"] if t["famille"] == fam and t["id"] in rep]
                    if not ids:
                        sans_cible += 1
                        continue
                    del rep[rng.choice(ids)]
                    nouvelle = score_noyau(publique, rep)["par_famille"][fam]["exactitude_equilibree"]
                elif serie == "B":
                    nouvelle = round(rng.uniform(0, 1), rng.choice((4, 5, 6))) + rng.choice((0.0, 0.00002))
                else:
                    propres = [v for v in proportions_r4(L, y, banque, absentes)
                               if v not in {float(f) for f in feuilles(L.json_sur(proportions_r4(L, x, banque, absentes)))}]
                    if not propres:
                        sans_cible += 1
                        continue
                    nouvelle = rng.choice(propres) + 0.00002
                score["par_famille"][fam]["exactitude_equilibree"] = nouvelle
            courant["M"], courant["S"] = cm, cs
            capture.clear()
            try:
                L.mode_test_final(args)
            except L.Refus as r:
                refus += 1
                motif = str(r).split(" porterait ")[1].split(" de l'autre")[0] if " porterait " in str(r) else str(r)[:60]
                motifs[motif] = motifs.get(motif, 0) + 1
                continue
            ecrites += 1
            # recherche propre à l'outil : aucune écriture d'une valeur propre à l'autre course
            docs = {}
            for nom in (M[0], S[0]):
                base = f"lecture-{nom}-test-final-holm-quatre-v4"
                docs[nom] = (json.loads(capture[base + ".json"]), capture[base + ".json"].decode() + capture[base + ".md"].decode())
            for xn, yn in ((M[0], S[0]), (S[0], M[0])):
                dx, tx = docs[xn]
                dy, _ = docs[yn]
                nombres_x = {float(f) for f in feuilles(dx) if isinstance(f, (int, float)) and not isinstance(f, bool)}
                propres = set()
                for fam in (FAMC, FAMD):
                    for ln in dy["lecture"][fam]:
                        if isinstance(ln.get("intervalle"), dict):
                            for v in (ln["exactitude_equilibree"], ln["intervalle"]["basse"], ln["intervalle"]["haute"]):
                                if v not in nombres_x and v not in (0.0, 1.0):
                                    propres |= ecritures(v)
                for t in dy["mcnemar_generation_0_contre_3"]["tests"]:
                    if t["p"] is not None and t["p"] not in nombres_x and t["p"] not in (0.0, 1.0):
                        a_, b_ = t["p_exacte"].split("/")
                        propres |= ecritures(Fraction(int(a_), int(b_)), p=True)
                trouves = propres & jetons(tx)
                ecr_x = {e for f in nombres_x for e in (json.dumps(f), f"{f:.4f}".replace(".", ","), f"{f:.6g}".replace(".", ","))}
                ecr_x |= {t["p_exacte"] for t in dx["mcnemar_generation_0_contre_3"]["tests"] if t.get("p_exacte")}
                if trouves - ecr_x:
                    fuites += 1
                if trouves & ecr_x:
                    ecritures_de_x[0] += 1
        bilan[serie] = (ecrites, refus, fuites, motifs, sans_cible)
        print(f"série {serie} : {n} paires ; écrites {ecrites} ; refus {refus} {motifs} ; écritures propres à l'autre course "
              f"trouvées dans un fichier écrit et qui ne sont pas l'écriture d'un nombre de ce fichier : {fuites} ; "
              f"fichiers où une écriture propre à l'autre course est aussi celle d'un nombre du fichier (score du noyau) : {ecritures_de_x[0]}" + (f" ; tirages sans cible {sans_cible}" if serie in ("C", "D") else ""), flush=True)
    ok = bilan["A"][1] == 0 and all(b[2] == 0 for b in bilan.values())
    print(f"# bilan : série A sans fausse alerte : {bilan['A'][1] == 0} ; aucune fuite trouvée : {all(b[2] == 0 for b in bilan.values())} ; "
          f"fausses alertes après un écart du noyau : B {bilan['B'][1]} sur {n_b}, C {bilan['C'][1]} sur {n_c - bilan['C'][4]}, "
          f"D {bilan['D'][1]} sur {n_d - bilan['D'][4]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(principal())
