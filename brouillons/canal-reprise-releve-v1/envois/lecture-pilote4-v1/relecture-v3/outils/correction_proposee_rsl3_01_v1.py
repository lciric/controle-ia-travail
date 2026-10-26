#!/usr/bin/env python3
"""Relecture de la v3 : essai, en mémoire seulement, de la correction proposée pour RSL3-01 (la copie du script n'est pas
modifiée). La garde `verifier_separation` est enveloppée : avant de chercher une écriture de l'autre course, elle écarte
toute écriture égale à l'écriture (JSON, quatre décimales, six chiffres, fraction exacte) d'un nombre du document de la
course du fichier — dont le score du noyau. Trois contrôles sur des paires inventées (mêmes courses que
`garde_en_processus_v3b.py`) : (1) divergence vraisemblable du noyau (série D) : aucun refus ; (2) divergence choisie
(série C) : aucun refus ; (3) une proportion propre à l'autre course plantée dans le Markdown, en JSON, ou une valeur p
de l'autre course en fraction : refus, comme avant la correction.

Usage : python -I -B correction_proposee_rsl3_01_v1.py SCRIPT_V3 DOSSIER_DE_TRAVAIL [N]
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

_spec = importlib.util.spec_from_file_location("garde_v3b", pathlib.Path(__file__).with_name("garde_en_processus_v3b.py"))
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)


def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("travail")
    ap.add_argument("n", nargs="?", type=int, default=1000)
    a = ap.parse_args()
    L = G.charger(a.script)
    publique, secret = G.banque_inventee()
    banque = {"publique": publique, "secret": secret, "empreinte_publique": "a" * 64, "empreinte_secret": "b" * 64, "surchargees": False}
    absentes = L.taches_categorie_absente(banque)
    comptes = L.comptes_absentes(absentes)
    sortie = pathlib.Path(a.travail) / "sortie-jamais-ecrite"
    script = {"nom": "lire_pilote4_v3.py", "sha256": hashlib.sha256(pathlib.Path(a.script).read_bytes()).hexdigest(),
              "python": platform.python_version()}
    L.preparer = lambda args: (sortie, banque, absentes, comptes, script, "2026-10-26T00:00:00Z")
    courant = {}
    L.lire_course = lambda dossier, b, part, role: courant[role]
    capture, docs = {}, {}
    L.ecrire_sorties = lambda s, contenus: (capture.update(contenus) or [(n, "0" * 64) for n in contenus])
    L.print = lambda *x, **k: None
    vrai_contenus = L.contenus_du_fichier

    def contenus(doc):
        octets = vrai_contenus(doc)
        docs[doc["course"]["nom"]] = (doc, octets)
        return octets
    L.contenus_du_fichier = contenus

    # la correction proposée, par enveloppe (aucune ligne du script changée)
    orig_vs, orig_present = L.verifier_separation, L.present
    ecritures_x = set()

    def present(jeton, texte, nom=False):
        if not nom and jeton in ecritures_x:
            return False
        return orig_present(jeton, texte, nom)

    def verifier_separation(doc_x, contenus_x, doc_y, n_tests):
        ecritures_x.clear()
        for f in G.feuilles(L.json_sur(doc_x)):
            if isinstance(f, (int, float)) and not isinstance(f, bool):
                ecritures_x.update({json.dumps(float(f)), L.fr(f), L.fr_p(f)})
        for t in (doc_x.get("mcnemar_generation_0_contre_3") or {}).get("tests", []):
            if t.get("p_exacte"):
                ecritures_x.add(t["p_exacte"])
        return orig_vs(doc_x, contenus_x, doc_y, n_tests)
    L.present, L.verifier_separation = present, verifier_separation

    args = argparse.Namespace(course_m="M", course_s="S", sans_seconde_course=False, banque_dir="b", sortie=str(sortie))
    rng = random.Random(4)
    resultats = {"D refus": 0, "C refus": 0, "plantation non refusée": 0, "plantations": 0, "paires": 0}
    for k in range(a.n):
        profils = [{"sans": rng.choice((0.0, 0.03, 0.1, 0.3)), "juste": {g: {f: rng.uniform(0.25, 0.97) for f in (G.FAMC, G.FAMD)}
                                                                             for g in range(4)}} for _ in range(2)]
        cm = G.course_inventee(rng, publique, G.M, profils[0], (0, 1, 2, 3))
        cs = G.course_inventee(rng, publique, G.S, profils[1], (0, 1, 2, 3))
        x, y = (cm, cs) if rng.random() < 0.5 else (cs, cm)
        g, fam = rng.choice((0, 1, 2, 3)), rng.choice((G.FAMC, G.FAMD))
        score = x["generations"][g]["score_noyau"][0]
        if k % 2 == 0:  # série D : une réponse que le noyau n'aurait pas comptée
            rep = dict(x["generations"][g]["reponses"]["reponses"])
            ids = [t["id"] for t in publique["test_final"] if t["famille"] == fam and t["id"] in rep]
            if not ids:
                continue
            del rep[rng.choice(ids)]
            score["par_famille"][fam]["exactitude_equilibree"] = G.score_noyau(publique, rep)["par_famille"][fam]["exactitude_equilibree"]
            cle = "D refus"
        else:  # série C : écriture du noyau de X égale à une proportion propre à Y
            propres = [v for v in G.proportions_r4(L, y, banque, absentes) if v not in set(G.proportions_r4(L, x, banque, absentes))]
            score["par_famille"][fam]["exactitude_equilibree"] = rng.choice(propres) + 0.00002
            cle = "C refus"
        courant["M"], courant["S"] = cm, cs
        capture.clear()
        docs.clear()
        try:
            L.mode_test_final(args)
        except L.Refus:
            resultats[cle] += 1
            continue
        resultats["paires"] += 1
        # plantations : la garde corrigée refuse toujours une écriture propre à l'autre course
        (dx, (jx, mx)), (dy, _) = docs[x["nom"]], docs[y["nom"]]
        nombres_x = {float(f) for f in G.feuilles(L.json_sur(dx)) if isinstance(f, (int, float)) and not isinstance(f, bool)}
        ecr_x = {L.fr(v) for v in nombres_x}
        props_y, ps_y = L.valeurs_mesurees(dy)
        cand = [v for v in props_y if v not in nombres_x and L.fr(v) not in ecr_x and v not in (0.0, 1.0)]
        cand_p = [p for p in ps_y if float(p) not in nombres_x and p not in (0, 1)]
        for octets in ([(jx, mx + f"\n({L.fr(cand[0])})".encode())] if cand else []) \
                + ([(jx.replace(b'"phrase_iv"', f'"note": {cand[-1]!r}, "phrase_iv"'.encode(), 1), mx)] if cand else []) \
                + ([(jx, mx + f"\n({L.frac(cand_p[0])})".encode())] if cand_p else []):
            resultats["plantations"] += 1
            try:
                L.verifier_separation(dx, octets, dy, 2)
                resultats["plantation non refusée"] += 1
            except L.Refus:
                pass
    print(f"# correction proposée de RSL3-01, essayée en mémoire — Python {platform.python_version()} ; script {script['sha256']}")
    print(f"paires : {a.n} ; divergence vraisemblable (D) refusée : {resultats['D refus']} sur {a.n // 2 + a.n % 2} ; "
          f"divergence choisie (C) refusée : {resultats['C refus']} sur {a.n // 2} ; plantations : {resultats['plantations']}, "
          f"non refusées : {resultats['plantation non refusée']}")
    return 0 if resultats["D refus"] == resultats["C refus"] == resultats["plantation non refusée"] == 0 else 1


if __name__ == "__main__":
    sys.exit(principal())
