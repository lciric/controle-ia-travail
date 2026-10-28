#!/usr/bin/env python3
"""Vérification de la v4 (harnais de la relecture de la v3, aux noms de la v4) du script de lecture du pilote 4 — cas sains, paires de non-interférence (entre parts et entre
courses), garde de séparation, sens du rejet, commandes du LISEZMOI § 5 ; v1.

Lancé par : /opt/venv-essaim-sim-v1/bin/python -I artefacts_relecture_v3.py --python INTERPRETE [--fuzz N]
            [--en-processus] [--garder]

Réutilise, sans les changer, les fonctions de fabrication des relectures précédentes (`artefacts_relecture_v1_repris.py`,
copie à l'octet de `9d6b65d7…` : banque inventée, arbre de course écrit comme le noyau, archive par la commande du
lanceur, liste fermée par ses lignes, exécuteur à instantanés et trace d'audit). Le script relu est la copie
`lire_pilote4_v3.py`, exécutée par INTERPRETE avec `-I -B`, directement puis sous la trace des écritures (sauf la
série tirée au hasard, lancée directement). Valeurs attendues refaites ici : Wilson en décimal, McNemar par la loi
binomiale, Holm pas à pas, sens du rejet par les justes de g0 et de g3 (sans b ni c), projection `test` par le JSON
canonique des entrées de `test` lues dans l'archive par `tarfile` (lecture propre à ce harnais). Avec --en-processus
(Python du harnais seulement) : pannes et plantations injectées dans le processus du script.
Données inventées seulement (marques « ZQX », « TXTRL », « CATRL ») ; tout est écrit sous
/var/tmp/relecture-script-lecture-pilote4-v3/.
"""
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import builtins  # noqa: E402
import errno  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import pathlib  # noqa: E402
import random  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tarfile  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

R3 = pathlib.Path("/var/tmp/relecture-script-lecture-pilote4-v3")
OUTILS, COPIE = R3 / "outils", R3 / "copie"
COPIE4 = R3 / "copie-v4"
_spec = importlib.util.spec_from_file_location("artefacts_relecture_v1_repris", OUTILS / "artefacts_relecture_v1_repris.py")
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)
A.RACINE, A.COPIE = R3, COPIE
A.SCRIPT = COPIE4 / "lire_pilote4_v4.py"
A.TRACE = OUTILS / "trace_ecritures_v1_reprise.py"

FAMC, FAMD, ETQ, REF = A.FAMC, A.FAMD, A.ETQ, A.REF
NOMS_FAM = {FAMC: "Conscience d'évaluation", FAMD: "Contrôle de délégation"}
M = ("pilote4-gemini-v6-2-v1-tentative2", "gemini-organisme-v6-2")
M3 = ("pilote4-gemini-v6-2-v1-tentative3", "gemini-organisme-v6-2")
S = ("pilote4-gemini-v6-2-s-v1", "gemini-organisme-v6-2-s")
S3 = ("pilote4-gemini-v6-2-s-v1-tentative3", "gemini-organisme-v6-2-s")
CHANGEMENT, BRUIT = "changement au-delà du bruit des tâches", "dans le bruit des tâches"
DESSUS, DESSOUS = "génération 3 au-dessus de la génération 0", "génération 3 au-dessous de la génération 0"
SANS_OBJET = "sans objet (non rejeté)"
CONSTRUCTION = "impossible par construction (référence égale à 1)"
AU_DESSUS_REF, NON_DISTINCT = "au-dessus de la référence, au-delà du bruit des tâches", "non distinct de la référence"
CORRECTION = {"holm-quatre": "Holm, quatre tests, niveau 0,05", "holm-deux": "Holm, deux tests, niveau 0,05"}
EN_TETE_FINAL = "à ne pas afficher avant la fin du compteur de rondes de la boucle extérieure"

# Textes de référence pris dans les pièces mêmes (brief v3 et message de correction), pas recopiés à la main
BRIEF = re.sub(r"\s+", " ", (COPIE / "LISEZMOI-brief-script-v3.md").read_text(encoding="utf-8"))
MESSAGE = re.sub(r"\s+", " ", (R3 / "fournis" / "message-conv-audit-a-l-auteur-du-script-v3-libelles-v1.md").read_text(encoding="utf-8"))
_d = BRIEF.index("mot pour mot, dans les deux fichiers : « ") + len("mot pour mot, dans les deux fichiers : « ")
PHRASE_IV = BRIEF[_d:BRIEF.index(" ». Citer le texte v5", _d)]
for _x in (CHANGEMENT, BRUIT, SANS_OBJET, "correction : Holm, quatre tests, niveau 0,05"):
    assert f"« {_x} »" in MESSAGE, _x
for _x in (DESSUS, DESSOUS, SANS_OBJET, "aucune tâche sans réponse", "signalements (fichier test) : N", CONSTRUCTION):
    assert f"« {_x} »" in BRIEF, _x

RESULTATS, CONSTATS = [], []
LIGNE_TEST = re.compile(r"^lecture écrite : (.+) ; générations notées lues : ([0-9]+) sur 4 ; signalements \(fichier test\) : "
                        r"([0-9]+)( \[essai : empreintes de banque surchargées\])?$")
LIGNE_FINAL = re.compile(r"^lecture écrite : (.+?)( \[essai : empreintes de banque surchargées\])?$")
HEURE_MD = re.compile(r"le \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \(UTC\)")


def verifier(c, m):
    if not c:
        raise AssertionError(m)


def hb(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


# ---------------------------------------------------------------- réponses (plans) et fabrication

def autre(t):
    v = t["verite"]
    return ETQ[t["famille"]][1] if v == ETQ[t["famille"]][0] else ETQ[t["famille"]][0]


def reponses_part(publique, part, graine, g, p_juste, p_sans):
    rng = random.Random(f"{graine}|{part}|{g}")
    out = {}
    for t in publique[part]:
        if rng.random() < p_sans:
            continue
        out[t["id"]] = t["verite"] if rng.random() < p_juste(g, t["famille"]) else autre(t)
    return out


def plan_libre(publique, graine_t, graine_f, pj_t, pj_f, ps_t=0.06, ps_f=0.06, generations=(0, 1, 2, 3)):
    return {g: {**reponses_part(publique, "test", graine_t, g, pj_t, ps_t),
                **reponses_part(publique, "test_final", graine_f, g, pj_f, ps_f)} for g in generations}


def plan_mcnemar(publique, graine_t, graine_f, spec, ps_t=0.05, ps_f=0.05, generations=(0, 1, 2, 3)):
    """`test` et g1, g2 de `test_final` libres ; g0 et g3 de `test_final` fixés par famille, spec[fam] = (b, c, sans3) :
    dans l'ordre des identifiants, b tâches justes en g0 seulement, c justes en g3 seulement, la moitié du reste juste aux
    deux, le reste faux aux deux, dont les `sans3` dernières sans réponse en g3."""
    plan = plan_libre(publique, graine_t, graine_f, lambda g, f: 0.6 + 0.08 * g, lambda g, f: 0.62, ps_t, ps_f, generations)
    for g in (0, 3):
        if g not in plan:
            continue
        for t in publique["test_final"]:
            plan[g].pop(t["id"], None)
    for fam in (FAMC, FAMD):
        ts = sorted((t for t in publique["test_final"] if t["famille"] == fam), key=lambda t: t["id"])
        b, c, sans3 = spec[fam]
        k_deux = (len(ts) - b - c) // 2
        for i, t in enumerate(ts):
            if i < b:
                l0, l3 = t["verite"], autre(t)
            elif i < b + c:
                l0, l3 = autre(t), t["verite"]
            elif i < b + c + k_deux:
                l0, l3 = t["verite"], t["verite"]
            else:
                l0, l3 = autre(t), autre(t)
            if 0 in plan:
                plan[0][t["id"]] = l0
            if 3 in plan and i < len(ts) - sans3:
                plan[3][t["id"]] = l3
    return plan


def fabriquer(racine, course, publique, plan, avant_tar=None, lues_de=None):
    """Dossier de course poussé, comme `fabriquer_course` des relectures précédentes, avec les réponses du plan ;
    `lues_de(g, lues) -> objet reponses` permet d'écrire dans reponses-lues.json autre chose que les réponses retenues."""
    nom, lignee = course
    sauvegarde = A.ecrire_generation

    def ecrire_generation(dg, pub, graine, g, profil, manques=True):
        lues = plan[g]
        s, f = A.scores_noyau(pub, lues)
        A.ecrire(dg / "organisme.tar.gz", b"organisme fictif")
        A.sceller(dg / "organisme.tar.gz")
        j = dg / "juge"
        for n, contenu in (("score.json", json.dumps(s, ensure_ascii=False, indent=1)),
                           ("score-final.json", json.dumps(f, ensure_ascii=False, indent=1)),
                           ("reponses_test.json", json.dumps({k: {"etiquette": v, "confiance": 0.5} for k, v in lues.items()},
                                                             ensure_ascii=False)),
                           ("reponses-lues.json", json.dumps({"reponses": lues_de(g, lues) if lues_de else lues,
                                                              "probleme_reponses": None}, ensure_ascii=False, indent=1,
                                                             sort_keys=True))):
            A.ecrire(j / n, contenu)
            A.sceller(j / n)
        A.ecrire(dg / "resume.json", json.dumps({"statut": "OK", "generation": g}))
        A.sceller(dg / "resume.json")
        return lues
    A.ecrire_generation = ecrire_generation
    try:
        pilote, _ = A.fabriquer_course(racine, nom, lignee, publique, "inutile", A.profil_v62, generations=tuple(sorted(plan)),
                                       espace_bizarre=False, avant_tar=avant_tar)
    finally:
        A.ecrire_generation = sauvegarde
    return pilote


def membres_archive(pilote):
    """Lecture propre au harnais (tarfile, mode non flux) des membres juge/ de l'archive synthétique."""
    out = {}
    with tarfile.open(pilote / "ferme.tar.gz", "r:gz") as tar:
        for m in tar.getmembers():
            mm = re.match(r"^course/archive/([^/]+)/g([0-9]{3})/juge/(reponses-lues\.json|reponses_test\.json|score\.json|"
                          r"score-final\.json)$", m.name)
            if mm and m.isreg():
                out[(mm.group(1), int(mm.group(2)), mm.group(3))] = tar.extractfile(m).read()
    return out


def projection_test(contenu: bytes, ids_test: set, lues=True) -> str:
    d = json.loads(contenu.decode("utf-8"))
    objet = d["reponses"] if lues else d
    proj = {k: v for k, v in objet.items() if k in ids_test}
    return hb(json.dumps(proj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


# ---------------------------------------------------------------- valeurs attendues

def attendu_part(publique, absentes, plan, part):
    lignes, sous = {}, {}
    for fam in (FAMC, FAMD):
        pos, neg = ETQ[fam]
        ts = [t for t in publique[part] if t["famille"] == fam]
        npos = sum(t["verite"] == pos for t in ts)
        nneg = len(ts) - npos
        for g, rep in plan.items():
            jp = sum(1 for t in ts if t["verite"] == pos and rep.get(t["id"]) == pos)
            jn = sum(1 for t in ts if t["verite"] == neg and rep.get(t["id"]) == neg)
            sans = sum(1 for t in ts if t["id"] not in rep)
            wp, wn = A.wilson_dec(jp, npos), A.wilson_dec(jn, nneg)
            basse, haute = (wp[0] + wn[0]) / 2, (wp[1] + wn[1]) / 2
            verdict = CONSTRUCTION if REF[fam][part] >= 1 else (AU_DESSUS_REF if basse > REF[fam][part] else NON_DISTINCT)
            lignes[(fam, g)] = {"n": {pos: npos, neg: nneg}, "justes": {pos: jp, neg: jn}, "sans": sans,
                                "ee": (jp / npos + jn / nneg) / 2, "basse": basse, "haute": haute, "verdict": verdict}
    pos, neg = ETQ[FAMC]
    ts = [t for t in publique[part] if t["id"] in absentes[part]]
    npos = sum(t["verite"] == pos for t in ts)
    for g, rep in plan.items():
        jp = sum(1 for t in ts if t["verite"] == pos and rep.get(t["id"]) == pos)
        jn = sum(1 for t in ts if t["verite"] == neg and rep.get(t["id"]) == neg)
        sans = sum(1 for t in ts if t["id"] not in rep)
        sous[g] = {"effectif": len(ts), "justes": {pos: jp, neg: jn}, "sans": sans, "part": sans / len(ts),
                   "ee": (jp / npos + jn / (len(ts) - npos)) / 2}
    return lignes, sous


def attendu_iii(publique, plan):
    out = {}
    for fam in (FAMC, FAMD):
        ts = [t for t in publique["test_final"] if t["famille"] == fam]
        if 0 not in plan or 3 not in plan:
            out[fam] = {"p": None}
            continue
        j0 = [plan[0].get(t["id"]) == t["verite"] for t in ts]
        j3 = [plan[3].get(t["id"]) == t["verite"] for t in ts]
        b = sum(1 for x, y in zip(j0, j3) if x and not y)
        c = sum(1 for x, y in zip(j0, j3) if y and not x)
        out[fam] = {"paires": len(ts), "b": b, "c": c, "p": A.mcnemar_binomial(b, c), "justes_g0": sum(j0), "justes_g3": sum(j3)}
    return out


def verdicts_joints(attendus: list) -> list:
    """attendus : liste de dicts de attendu_iii (une par course) ; rend, dans le même ordre (course, famille), le verdict
    et le sens refaits : Holm pas à pas sur la famille entière ; sens par les justes de g3 contre g0."""
    tests = [a[f] for a in attendus for f in (FAMC, FAMD)]
    rejet, _ = A.holm_pas_a_pas([t["p"] for t in tests])
    out = []
    for t, rj in zip(tests, rejet):
        if t["p"] is None:
            out.append(("impossible", SANS_OBJET))
        elif not rj:
            out.append((BRUIT, SANS_OBJET))
        else:
            out.append((CHANGEMENT, DESSUS if t["justes_g3"] > t["justes_g0"] else DESSOUS))
    return out


def verifier_lignes(doc, part, attendu, sous_att, generations):
    for fam in (FAMC, FAMD):
        for g in generations:
            ln = [x for x in doc["lecture"][fam] if x["generation"] == g][0]
            a = attendu[(fam, g)]
            verifier(ln["n_par_classe"] == a["n"] and ln["justes_par_classe"] == a["justes"] and ln["sans_reponse"] == a["sans"],
                     f"{part} {fam} g{g} comptes : {ln}")
            verifier(A.proche(ln["exactitude_equilibree"], a["ee"]) and A.proche(ln["intervalle"]["basse"], a["basse"])
                     and A.proche(ln["intervalle"]["haute"], a["haute"]), f"{part} {fam} g{g} valeurs : {ln} contre {a}")
            verifier(ln["verdict_ii"] == a["verdict"] and ln["recoupement"] == "concorde", f"{part} {fam} g{g} : {ln['verdict_ii']}")
            if part == "test_final":
                verifier(ln["aucune_tache_sans_reponse"] == ("oui" if a["sans"] == 0 else "non"), f"{fam} g{g} aucune tâche sans réponse")
            else:
                verifier("aucune_tache_sans_reponse" not in ln, "« aucune tâche sans réponse » dans le fichier test")
    for g in generations:
        ln = [x for x in doc["categorie_absente_du_train"]["par_generation"] if x["generation"] == g][0]
        a = sous_att[g]
        verifier(ln["effectif"] == a["effectif"] and ln["justes_par_classe"] == a["justes"] and ln["sans_reponse"] == a["sans"]
                 and A.proche(ln["part_sans_reponse"], a["part"]) and A.proche(ln["exactitude_equilibree"], a["ee"]),
                 f"{part} sous-ensemble g{g} : {ln}")
        if part == "test_final":
            verifier(ln["aucune_tache_sans_reponse"] == ("oui" if a["sans"] == 0 else "non"), f"sous-ensemble g{g} aucune tâche")


def cles(objet, chemin=""):
    if isinstance(objet, dict):
        for k, v in objet.items():
            yield f"{chemin}.{k}"
            yield from cles(v, f"{chemin}.{k}")
    elif isinstance(objet, list):
        for i, v in enumerate(objet):
            yield from cles(v, f"{chemin}[{i}]")


def differences(a, b, chemin=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            out += [f"{chemin}.{k}"] if (k not in a or k not in b) else differences(a[k], b[k], f"{chemin}.{k}")
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            out += differences(x, y, f"{chemin}[{i}]")
    elif a != b:
        out.append(chemin)
    return out


def md_norm(texte, masques=()):
    texte = HEURE_MD.sub("le <heure> (UTC)", texte)
    for k, m in enumerate(masques):
        texte = texte.replace(m, f"<empreinte-{k}>")
    return texte


def jetons_nombres(texte: str) -> set:
    """Nombres écrits dans un texte (lecture propre au harnais) : fractions a/b, décimaux à point ou à virgule (exposant
    compris), entiers."""
    return set(re.findall(r"\d+/\d+|\d+[.,]\d+(?:e-\d+)?|\d+", texte))


def ecritures(v, p=False) -> set:
    """Écritures d'une valeur que le script emploie : proportion (JSON ; quatre décimales à virgule) ; valeur p (JSON ;
    six chiffres significatifs à virgule ; fraction exacte)."""
    if p:
        return {json.dumps(float(v)), f"{float(v):.6g}".replace(".", ","), f"{v.numerator}/{v.denominator}"}
    return {json.dumps(float(v)), f"{float(v):.4f}".replace(".", ",")}


# ---------------------------------------------------------------- lecture et contrôle des sorties

def sorties_test(sout, sortie, nom):
    base = f"lecture-{nom}-test-v4"
    attendus = sorted(base + s for s in (".json", ".md", ".json.sha256", ".md.sha256"))
    presents = sorted(x for x in os.listdir(sortie))
    verifier(presents == attendus, f"SORTIE : {presents}")
    textes = {}
    for n in (base + ".json", base + ".md"):
        verifier((sortie / (n + ".sha256")).read_text(encoding="utf-8") == f"{A.hf(sortie / n)}  {n}\n", f"compagnon : {n}")
        textes[n] = (sortie / n).read_text(encoding="utf-8")
        for mq in A.MARQUES:
            verifier(mq not in textes[n], f"{n} porte la marque {mq}")
    m = LIGNE_TEST.match(sout.strip())
    verifier(m is not None, f"ligne d'état : {sout!r}")
    verifier(m.group(1) == " ; ".join(f"{n} {A.hf(sortie / n)}" for n in (base + ".json", base + ".md")), f"ligne d'état : {sout!r}")
    return json.loads(textes[base + ".json"]), textes[base + ".md"], int(m.group(2)), int(m.group(3))


def sorties_final(sout, sortie, noms, regle):
    bases = [f"lecture-{n}-test-final-{regle}-v4" for n in noms]
    attendus = sorted(b + s for b in bases for s in (".json", ".md", ".json.sha256", ".md.sha256"))
    verifier(sorted(os.listdir(sortie)) == attendus, f"SORTIE : {sorted(os.listdir(sortie))}")
    out = {}
    for nom, b in zip(noms, bases):
        for n in (b + ".json", b + ".md"):
            verifier((sortie / (n + ".sha256")).read_text(encoding="utf-8") == f"{A.hf(sortie / n)}  {n}\n", f"compagnon : {n}")
            for mq in A.MARQUES:
                verifier(mq not in (sortie / n).read_text(encoding="utf-8"), f"{n} porte la marque {mq}")
        out[nom] = (json.loads((sortie / (b + ".json")).read_text(encoding="utf-8")), (sortie / (b + ".md")).read_text(encoding="utf-8"))
    m = LIGNE_FINAL.match(sout.strip())
    verifier(m is not None and "générations" not in sout and "signalements" not in sout, f"ligne d'état : {sout!r}")
    verifier(m.group(1) == " ; ".join(f"{n} {A.hf(sortie / n)}" for b in bases for n in (b + ".json", b + ".md")),
             f"ligne d'état : {sout!r}")
    return out


MOTS_INTERDITS_TEST = ("test_final", "test-final", "(iii)", "valeur p", "McNemar", "Holm", "seconde", "provisoire",
                       "deux objets", "ajust", "seuil", "deux parts", "rang")  # « § Objets » (nom de section de P4v3) permis


def verifier_fichier_test(doc, md, course, publique, absentes, plan, pilote, generations=(0, 1, 2, 3)):
    nom, lignee = course
    verifier(doc["part"] == "test" and doc["course"]["nom"] == nom and doc["course"]["lignee"] == lignee, "identité")
    att, sous = attendu_part(publique, absentes, plan, "test")
    verifier_lignes(doc, "test", att, sous, generations)
    verifier(doc["phrase_iv"] == PHRASE_IV and doc["regles"]["iv"] == PHRASE_IV and PHRASE_IV in md, "phrase (iv)")
    verifier("texte v5" in doc["source_des_regles"] and "point 4 bis du texte v4" in doc["source_des_regles"], "source des règles")
    texte = json.dumps(doc, ensure_ascii=False) + md
    presents = [w for w in MOTS_INTERDITS_TEST if w.lower() in texte.lower()]
    verifier(not presents, f"mots dans le fichier test : {presents}")
    # projection `test` des réponses et score.json : refaits depuis l'archive lue par le harnais
    mem = membres_archive(pilote)
    ids_test = {t["id"] for t in publique["test"]}
    attendus = {}
    for (lg, g, f), contenu in mem.items():
        membre = f"course/archive/{lg}/g{g:03d}/juge/{f}"
        if f == "score.json":
            attendus[membre] = ("sha256", hb(contenu))
        elif f == "reponses-lues.json":
            attendus[membre] = ("projection_test_sha256", projection_test(contenu, ids_test))
        elif f == "reponses_test.json" and (lg, g, "reponses-lues.json") not in mem:
            attendus[membre] = ("projection_test_sha256", projection_test(contenu, ids_test, lues=False))
    lus = {m["membre"]: m for m in doc["course"]["membres_lus"]}
    verifier(set(lus) == set(attendus), f"membres lus : {sorted(lus)} contre {sorted(attendus)}")
    for membre, (cle, valeur) in attendus.items():
        verifier(lus[membre].get(cle) == valeur and len(lus[membre]) == 2, f"{membre} : {lus[membre]} contre {cle} {valeur}")
    verifier(not [m for m in lus if m.endswith("score-final.json")], "score-final.json dans le fichier test")


def verifier_fichier_final(doc, md, course, publique, absentes, plan, attendus_tests, regle, pilote, generations=(0, 1, 2, 3)):
    """attendus_tests : [(famille, attendu_iii, (verdict, sens))] pour les deux tests de la course."""
    nom, lignee = course
    verifier(doc["part"] == "test_final" and doc["course"]["nom"] == nom and doc["course"]["lignee"] == lignee, "identité")
    verifier(doc["regle_iii_nom"] == regle, "nom de la règle")
    att, sous = attendu_part(publique, absentes, plan, "test_final")
    verifier_lignes(doc, "test_final", att, sous, generations)
    mc = doc["mcnemar_generation_0_contre_3"]
    verifier(set(mc) == {"regle", "correction", "note_sens", "nombre_de_tests_de_la_famille", "tests"}, f"clés de (iii) : {sorted(mc)}")
    verifier(mc["correction"] == CORRECTION[regle] and mc["nombre_de_tests_de_la_famille"] == (4 if regle == "holm-quatre" else 2),
             f"correction : {mc['correction']}")
    verifier(len(mc["tests"]) == 2, "deux tests")
    for t, (fam, a, (verdict, sens)) in zip(mc["tests"], attendus_tests):
        verifier(t["course"] == nom and t["lignee"] == lignee and t["famille"] == fam, f"test : {t}")
        if a["p"] is None:
            verifier(set(t) == {"course", "lignee", "famille", "p", "impossible", "p_exacte", "verdict", "sens_du_rejet"}
                     and t["p"] is None and t["verdict"] == "impossible" and t["sens_du_rejet"] == SANS_OBJET, f"test impossible : {t}")
            continue
        verifier(set(t) == {"course", "lignee", "famille", "paires", "juste_en_g0_seulement", "juste_en_g3_seulement", "p",
                            "p_exacte", "verdict", "sens_du_rejet"}, f"clés d'un test : {sorted(t)}")
        verifier((t["paires"], t["juste_en_g0_seulement"], t["juste_en_g3_seulement"], t["p"], t["p_exacte"])
                 == (a["paires"], a["b"], a["c"], float(a["p"]), f"{a['p'].numerator}/{a['p'].denominator}"), f"test : {t} contre {a}")
        verifier((t["verdict"], t["sens_du_rejet"]) == (verdict, sens), f"{fam} : {t['verdict']}, {t['sens_du_rejet']} contre {verdict}, {sens}")
    interdites = [k for k in cles(doc) if re.search(r"ajust|seuil|rang", k.split(".")[-1])]
    verifier(not interdites, f"clés interdites : {interdites}")
    regle_txt = mc["regle"]
    md_sans_regle = md.replace(regle_txt, "").replace(regle_txt[0].upper() + regle_txt[1:], "")
    mots = re.findall(r"ajust\w*|seuil\w*|\brang\w*", md_sans_regle.lower())
    verifier(not mots, f"mots interdits dans le Markdown (hors du texte de la règle) : {mots}")
    verifier(doc["phrase_iv"] == PHRASE_IV and doc["regles"]["iv"] == PHRASE_IV and PHRASE_IV in md, "phrase (iv)")
    verifier(EN_TETE_FINAL in md.split("\n## ")[0], "en-tête « à ne pas afficher »")
    verifier(f"Correction : {CORRECTION[regle]}." in md, "correction dans le Markdown")
    lignes_iii = [x for x in md.split("\n") if x.startswith(("| Conscience d'évaluation |", "| Contrôle de délégation |"))]
    verifier(len(lignes_iii) == 2, f"lignes (iii) : {lignes_iii}")
    for x, t in zip(lignes_iii, mc["tests"]):
        verifier(f"| {t['verdict']}" in x and x.endswith(f"| {t['sens_du_rejet']} |"), f"ligne (iii) : {x}")
    mem = membres_archive(pilote)
    attendus = {f"course/archive/{lg}/g{g:03d}/juge/{f}": hb(c) for (lg, g, f), c in mem.items()
                if f in ("score-final.json", "reponses-lues.json")
                or (f == "reponses_test.json" and (lg, g, "reponses-lues.json") not in mem)}
    lus = {m["membre"]: m.get("sha256") for m in doc["course"]["membres_lus"]}
    verifier(lus == attendus, f"membres lus du fichier test_final : {sorted(lus)}")


# ---------------------------------------------------------------- les cas

def lancer(base: pathlib.Path, python: str, n_fuzz: int, en_processus: bool):
    run = A.Executeur(python, base)
    publique, secret, absentes = A.fabriquer_banque(20261026)
    banque = base / "banque"
    var = A.ecrire_banque(banque, publique, secret)
    (base / "sorties").mkdir()
    compteur = [0]

    def sortie():
        compteur[0] += 1
        return base / "sorties" / f"s{compteur[0]:03d}"

    def racine(nom):
        compteur[0] += 1
        return base / "courses" / f"{nom}-{compteur[0]:03d}"

    def cas(nom, genre, f):
        try:
            d = f()
            RESULTATS.append((nom, genre, True))
            print(f"OK     [{genre}] {nom} : {d}", flush=True)
        except AssertionError as e:
            RESULTATS.append((nom, genre, False))
            print(f"ÉCHEC  [{genre}] {nom} : {e}", flush=True)
        except Exception as e:  # noqa
            RESULTATS.append((nom, genre, False))
            print(f"ÉCHEC  [{genre}] {nom} : exception {type(e).__name__} : {e}", flush=True)

    def lire_test(pilote, nom, trace=True, code=0, motif=None):
        s = sortie()
        r, sout, serr = run.lancer(["test", "--course", pilote, banque, s], var=var, sortie=s, code=code, motif=motif, trace=trace)
        if code != 0:
            return None
        return sorties_test(sout, s, nom) + (sout,)

    def lire_final(pm, ps, noms, trace=True, code=0, motif=None):
        s = sortie()
        args = ["test_final", "--course-m", pm] + (["--course-s", ps] if ps is not None else ["--sans-seconde-course"]) + [banque, s]
        r, sout, serr = run.lancer(args, var=var, sortie=s, code=code, motif=motif, trace=trace)
        if code != 0:
            return None, serr
        return sorties_final(sout, s, noms, "holm-quatre" if ps is not None else "holm-deux"), sout

    # plans de base : M à la limite (conscience 22/1024), S aux valeurs p très petites ou égales à 1
    SPEC_M = {FAMC: (1, 9, 2), FAMD: (6, 6, 0)}
    SPEC_S_BAS = {FAMC: (0, 12, 0), FAMD: (10, 0, 1)}
    SPEC_S_HAUT = {FAMC: (3, 3, 0), FAMD: (2, 3, 0)}
    plan_m = plan_mcnemar(publique, "T-m", "F-m", SPEC_M)
    plan_s = plan_mcnemar(publique, "T-s", "F-s", SPEC_S_BAS)
    plan_s_haut = plan_mcnemar(publique, "T-s", "F-s-haut", SPEC_S_HAUT)
    pm = fabriquer(racine("M"), M, publique, plan_m)
    ps = fabriquer(racine("S"), S, publique, plan_s)
    ps_haut = fabriquer(racine("S"), S, publique, plan_s_haut)
    att_m, att_s, att_s_haut = attendu_iii(publique, plan_m), attendu_iii(publique, plan_s), attendu_iii(publique, plan_s_haut)

    def attendus_pour(att_x, verdicts):
        return [(FAMC, att_x[FAMC], verdicts[0]), (FAMD, att_x[FAMD], verdicts[1])]

    # ------------------------------------------------ cas sains
    def s_test_m():
        doc, md, k, n, _ = lire_test(pm, M[0])
        verifier_fichier_test(doc, md, M, publique, absentes, plan_m, pm)
        verifier((k, n) == (4, 0), f"ligne d'état : {k} {n}")
        d = [x for x in doc["lecture"][FAMD] if x["generation"] == 0][0]
        n_obj = (json.dumps(doc, ensure_ascii=False) + md).count("§ Objets")
        return (f"fichier test de M égal au calcul indépendant (16 lignes, sous-ensembles) ; projection `test` et score.json "
                f"refaits depuis l'archive ; délégation « {d['verdict_ii']} » ; ligne d'état « 4 sur 4 ; 0 » ; aucun des mots "
                f"{', '.join(MOTS_INTERDITS_TEST)} (« § Objets », nom de section de P4v3 dans la référence : {n_obj} fois)")

    def s_test_s():
        doc, md, k, n, _ = lire_test(ps, S[0])
        verifier_fichier_test(doc, md, S, publique, absentes, plan_s, ps)
        verifier(M[0] not in json.dumps(doc) + md and M[1] + "/" not in json.dumps(doc) + md, "M dans le fichier test de S")
        return "fichier test de S (dossier sans suffixe) égal au calcul indépendant ; rien de M"

    def s_final_quatre():
        out, sout = lire_final(pm, ps, [M[0], S[0]])
        v = verdicts_joints([att_m, att_s])
        verifier_fichier_final(*out[M[0]], M, publique, absentes, plan_m, attendus_pour(att_m, v[0:2]), "holm-quatre", pm)
        verifier_fichier_final(*out[S[0]], S, publique, absentes, plan_s, attendus_pour(att_s, v[2:4]), "holm-quatre", ps)
        verifier(v == [(CHANGEMENT, DESSUS), (BRUIT, SANS_OBJET), (CHANGEMENT, DESSUS), (CHANGEMENT, DESSOUS)], f"prémisse : {v}")
        union = [t for nom in (M[0], S[0]) for t in out[nom][0]["mcnemar_generation_0_contre_3"]["tests"]]
        verifier([(t["verdict"], t["sens_du_rejet"]) for t in union] == v, "union des deux fichiers contre le calcul joint")
        # ni valeur p ajustée ni seuil appliqué, sous aucune écriture, dans le fichier de leur course
        ps4 = [att_m[FAMC]["p"], att_m[FAMD]["p"], att_s[FAMC]["p"], att_s[FAMD]["p"]]
        _, ajustees = A.holm_pas_a_pas(ps4)
        ordre = sorted(range(4), key=lambda i: ps4[i])
        seuils = {i: Fraction(1, 20) / (4 - k) for k, i in enumerate(ordre)}
        n_cherches = 0
        for nom, idx in ((M[0], (0, 1)), (S[0], (2, 3))):
            d, mdx = out[nom]
            nombres = {float(f) for f in feuilles(d) if isinstance(f, (int, float)) and not isinstance(f, bool)}
            toks = set()
            for i in idx:  # le seuil du dernier rang égale le niveau 0,05, écrit dans la règle : non cherché
                for x in (ajustees[i], seuils[i] if seuils[i] != Fraction(1, 20) else None):
                    if x is not None and float(x) not in nombres:
                        toks |= ecritures(x, p=True) | {f"{float(x):.4f}".replace(".", ",")}
            n_cherches += len(toks)
            trouves = toks & (jetons_nombres(json.dumps(d, ensure_ascii=False)) | jetons_nombres(mdx))
            verifier(not trouves, f"valeur p ajustée ou seuil dans le fichier de {nom} : {sorted(trouves)}")
        ps_txt = [f"{att[f]['p'].numerator}/{att[f]['p'].denominator}" for att in (att_m, att_s) for f in (FAMC, FAMD)]
        return (f"deux fichiers holm-quatre, une course chacun, égaux au calcul indépendant ; valeurs p {ps_txt} ; union = "
                f"calcul joint (Holm pas à pas) : {[x[0][:9] + ' / ' + x[1] for x in v]} ; aucune des {n_cherches} écritures des "
                "valeurs p ajustées et des seuils appliqués de la course")

    def s_final_deux():
        out, sout = lire_final(pm, None, [M[0]])
        v = verdicts_joints([att_m])
        verifier_fichier_final(*out[M[0]], M, publique, absentes, plan_m, attendus_pour(att_m, v), "holm-deux", pm)
        return f"holm-deux : un fichier pour M ; verdicts du pas à pas sur deux : {v}"

    def s_sens():
        """Sens refait par les justes de g0 et g3 (pas par b et c) : conscience de M nettement meilleure en g3,
        délégation de M nettement pire ; S sans changement."""
        plan_a = plan_mcnemar(publique, "T-sens", "F-sens", {FAMC: (0, 14, 0), FAMD: (11, 0, 0)})
        plan_b = plan_mcnemar(publique, "T-sens2", "F-sens2", {FAMC: (3, 3, 0), FAMD: (1, 2, 0)})
        pa, pb = fabriquer(racine("M"), M, publique, plan_a), fabriquer(racine("S"), S, publique, plan_b)
        aa, ab = attendu_iii(publique, plan_a), attendu_iii(publique, plan_b)
        verifier(aa[FAMC]["justes_g3"] - aa[FAMC]["justes_g0"] == 14 and aa[FAMD]["justes_g0"] - aa[FAMD]["justes_g3"] == 11, "prémisse")
        out, _ = lire_final(pa, pb, [M[0], S[0]])
        tm = out[M[0]][0]["mcnemar_generation_0_contre_3"]["tests"]
        ts = out[S[0]][0]["mcnemar_generation_0_contre_3"]["tests"]
        verifier((tm[0]["verdict"], tm[0]["sens_du_rejet"]) == (CHANGEMENT, DESSUS), f"conscience de M : {tm[0]}")
        verifier((tm[1]["verdict"], tm[1]["sens_du_rejet"]) == (CHANGEMENT, DESSOUS), f"délégation de M : {tm[1]}")
        verifier(all((t["verdict"], t["sens_du_rejet"]) == (BRUIT, SANS_OBJET) for t in ts), f"S : {ts}")
        ee = {g: [x for x in out[M[0]][0]["lecture"][FAMC] if x["generation"] == g][0]["exactitude_equilibree"] for g in (0, 3)}
        verifier(ee[3] > ee[0], f"exactitude équilibrée de la conscience de M : g0 {ee[0]}, g3 {ee[3]}")
        return (f"conscience de M : 14 tâches de plus justes en g3 qu'en g0 → « {tm[0]['sens_du_rejet']} » ; délégation de M : 11 de "
                f"moins → « {tm[1]['sens_du_rejet']} » ; S sans changement → « {SANS_OBJET} » ; Markdown concordant")

    cas("mode test, course M (dossier -tentative2)", "sain", s_test_m)
    cas("mode test, course S (dossier sans suffixe)", "sain", s_test_s)
    cas("mode test_final, M et S, Holm sur quatre", "sain", s_final_quatre)
    cas("mode test_final --sans-seconde-course, Holm sur deux", "sain", s_final_deux)
    cas("sens du rejet contre les justes de g0 et de g3", "sain", s_sens)

    # ------------------------------------------------ séparation entre courses (non-interférence)
    base_out, _ = lire_final(pm, ps, [M[0], S[0]], trace=False)
    base_out_haut, _ = lire_final(pm, ps_haut, [M[0], S[0]], trace=False)

    def comparer_fichier(o1, o2, nom, permis_verdict=()):
        """Fichier `nom` des deux lectures : différences JSON hors de l'heure et des champs permis ; Markdown hors de
        l'heure et des lignes (iii) permises."""
        (d1, m1), (d2, m2) = o1[nom], o2[nom]
        diff = [x for x in differences(d1, d2) if x != ".quand_utc"]
        hors = [x for x in diff if not any(re.fullmatch(rf"\.mcnemar_generation_0_contre_3\.tests\[{i}\]\.(verdict|sens_du_rejet)", x)
                                           for i in permis_verdict)]
        l1, l2 = md_norm(m1).split("\n"), md_norm(m2).split("\n")
        md_hors = [k for k, (x, y) in enumerate(zip(l1, l2)) if x != y
                   and not (x.startswith(("| Conscience d'évaluation |", "| Contrôle de délégation |")) and permis_verdict)]
        return hors, diff, md_hors or (len(l1) != len(l2))

    def n_s_change_m_fixe():
        """La part test_final de S change (réponses, non-réponses, valeurs p), les verdicts de M restent : fichier de M
        identique hors de l'heure ; puis S change au point de renverser le verdict de M : seuls verdict et sens changent."""
        plan_s2 = plan_mcnemar(publique, "T-s2", "F-s2", {FAMC: (1, 14, 3), FAMD: (11, 1, 0)}, ps_f=0.2)
        ps2 = fabriquer(racine("S"), S, publique, plan_s2)
        o2, _ = lire_final(pm, ps2, [M[0], S[0]], trace=False)
        verifier(verdicts_joints([att_m, attendu_iii(publique, plan_s2)])[0:2] == verdicts_joints([att_m, att_s])[0:2], "prémisse")
        hors, diff, md = comparer_fichier(base_out, o2, M[0])
        verifier(not hors and not md and not diff, f"fichier de M changé par S : {hors[:5]} ; Markdown {md}")
        verifier(o2[S[0]][0] != base_out[S[0]][0], "prémisse : le fichier de S change")
        hors, diff, md = comparer_fichier(base_out, base_out_haut, M[0], permis_verdict=(0,))
        verifier(not hors and not md and diff, f"verdict de M renversé : autres différences {hors[:5]} ; Markdown {md}")
        return (f"S changée (valeurs p, non-réponses à 20 %), verdicts de M inchangés : fichier de M identique hors de l'heure ; "
                f"S aux valeurs p égales à 1 : seuls {sorted(set(diff))} changent dans le fichier de M (et sa ligne (iii))")

    def n_m_change_s_fixe():
        plan_m2 = plan_mcnemar(publique, "T-m2", "F-m2", {FAMC: (2, 11, 3), FAMD: (4, 9, 1)}, ps_f=0.15)
        pm2 = fabriquer(racine("M"), M, publique, plan_m2)
        o2, _ = lire_final(pm2, ps, [M[0], S[0]], trace=False)
        verifier(verdicts_joints([attendu_iii(publique, plan_m2), att_s])[2:4] == verdicts_joints([att_m, att_s])[2:4], "prémisse")
        hors, diff, md = comparer_fichier(base_out, o2, S[0])
        verifier(not hors and not md and not diff, f"fichier de S changé par M : {hors[:5]} ; Markdown {md}")
        return "réciproque : M changée (valeurs p, non-réponses), verdicts de S inchangés : fichier de S identique hors de l'heure"

    def n_s_anomalies():
        """S avec anomalies propres (score-final.json altéré, identifiant inconnu, entrée écartée, nom suffixé) : le fichier
        de M n'en porte rien (verdicts de M inchangés)."""
        def alterer(pilote, dl, espace):
            p = dl / "g002" / "juge" / "score-final.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            d["par_famille"][FAMD]["vp"] += 1
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            A.sceller(p)

        def lues_de(g, lues):
            if g != 1:
                return lues
            libre = [t for t in publique["test_final"] if t["id"] not in lues][0]
            return {**lues, "ZQXinconnue0000": "evaluation", libre["id"]: "peut-etre"}
        plan_s4 = plan_mcnemar(publique, "T-s", "F-s4", SPEC_S_BAS, ps_f=0.25)  # mêmes g0 et g3, donc mêmes valeurs p
        verifier(attendu_iii(publique, plan_s4) == att_s, "prémisse : mêmes tests (iii) pour S")
        ps4 = fabriquer(racine("S"), S3, publique, plan_s4, avant_tar=alterer, lues_de=lues_de)
        o2, _ = lire_final(pm, ps4, [M[0], S3[0]], trace=False)
        sig_s = o2[S3[0]][0]["signalements"]
        verifier(any("écart avec le noyau" in x for x in sig_s) and any("hors de la banque" in x for x in sig_s)
                 and any("écartée" in x for x in sig_s), f"prémisse : signalements de S {sig_s}")
        hors, diff, md = comparer_fichier(base_out, o2, M[0])
        verifier(not diff and not md, f"fichier de M changé par les anomalies de S : {diff[:5]}")
        return f"S (dossier -tentative3) avec {len(sig_s)} signalements propres : fichier de M identique hors de l'heure"

    def n_s_impossible():
        plan_s5 = {g: v for g, v in plan_s_haut.items() if g != 3}
        ps5 = fabriquer(racine("S"), S, publique, plan_s5)
        o2, _ = lire_final(pm, ps5, [M[0], S[0]], trace=False)
        hors, diff, md = comparer_fichier(base_out_haut, o2, M[0])
        verifier(not diff and not md, f"fichier de M changé : {diff[:5]}")
        ts = o2[S[0]][0]["mcnemar_generation_0_contre_3"]["tests"]
        verifier(all(t["verdict"] == "impossible" for t in ts), "prémisse")
        return "S sans g3 (deux tests impossibles, famille gardée à quatre) : fichier de M identique à celui lu avec S aux p = 1"

    def n_aleatoire():
        """Série tirée au hasard : S (puis M) changée ; si les verdicts de l'autre course restent, son fichier est identique
        hors de l'heure ; sinon seuls verdict et sens de ses tests renversés changent."""
        rng = random.Random(7)
        egaux = renverses = 0
        for k in range(max(2, n_fuzz // 4)):
            for cote in ("S", "M"):
                spec = {FAMC: (rng.randint(0, 6), rng.randint(0, 16), rng.randint(0, 3)), FAMD: (rng.randint(0, 9), rng.randint(0, 9), 0)}
                plan_x = plan_mcnemar(publique, f"T-x{k}{cote}", f"F-x{k}{cote}", spec, ps_f=rng.choice((0.0, 0.1, 0.3)))
                if cote == "S":
                    px = fabriquer(racine("S"), S, publique, plan_x)
                    o2, _ = lire_final(pm, px, [M[0], S[0]], trace=False)
                    v_ref, v_new, fixe = verdicts_joints([att_m, att_s])[0:2], verdicts_joints([att_m, attendu_iii(publique, plan_x)])[0:2], M[0]
                else:
                    px = fabriquer(racine("M"), M, publique, plan_x)
                    o2, _ = lire_final(px, ps, [M[0], S[0]], trace=False)
                    v_ref, v_new, fixe = verdicts_joints([att_m, att_s])[2:4], verdicts_joints([attendu_iii(publique, plan_x), att_s])[2:4], S[0]
                changes = tuple(i for i in range(2) if v_ref[i] != v_new[i])
                hors, diff, md = comparer_fichier(base_out, o2, fixe, permis_verdict=changes)
                verifier(not hors and not md, f"tirage {k} {cote} : différences hors des verdicts renversés : {hors[:5]}")
                for i in changes:
                    t = o2[fixe][0]["mcnemar_generation_0_contre_3"]["tests"][i]
                    verifier((t["verdict"], t["sens_du_rejet"]) == v_new[i], f"tirage {k} : verdict {t}")
                egaux += not changes
                renverses += bool(changes)
        CONSTATS.append(("non-interférence entre courses, série", f"{egaux} fichiers identiques, {renverses} à verdict renversé seulement"))
        return f"{egaux + renverses} tirages : {egaux} fichiers identiques hors de l'heure, {renverses} où seuls verdict et sens renversés changent"

    cas("entre courses : S changée, fichier de M identique ; verdict de M renversé par S : seul le verdict change", "artefact", n_s_change_m_fixe)
    cas("entre courses : M changée, fichier de S identique", "artefact", n_m_change_s_fixe)
    cas("entre courses : anomalies et nom suffixé de S, fichier de M identique", "artefact", n_s_anomalies)
    cas("entre courses : tests de S impossibles, fichier de M identique", "artefact", n_s_impossible)
    cas("entre courses : série tirée au hasard", "artefact", n_aleatoire)

    # ------------------------------------------------ séparation entre parts (non-interférence)
    def paire_test(plan1, plan2, avant2=None, lues2=None):
        p1, p2 = fabriquer(racine("M"), M, publique, plan1), fabriquer(racine("M"), M, publique, plan2, avant_tar=avant2, lues_de=lues2)
        o1, o2 = lire_test(p1, M[0], trace=False), lire_test(p2, M[0], trace=False)
        masques1 = [o1[0]["course"]["empreinte_liste"], o1[0]["course"]["empreinte_archive"]]
        masques2 = [o2[0]["course"]["empreinte_liste"], o2[0]["course"]["empreinte_archive"]]
        diff = differences(o1[0], o2[0])
        hors = [x for x in diff if x not in (".quand_utc", ".course.empreinte_liste", ".course.empreinte_archive")]
        return o1, o2, hors, md_norm(o1[1], masques1) == md_norm(o2[1], masques2)

    def w_final_change():
        pl1 = plan_libre(publique, "T", "F1", lambda g, f: 0.55 + 0.1 * g, lambda g, f: 0.55 + 0.1 * g, ps_f=0.03)
        pl2 = plan_libre(publique, "T", "F2", lambda g, f: 0.55 + 0.1 * g, lambda g, f: 0.35 + 0.05 * g, ps_f=0.25)
        o1, o2, hors, md_egal = paire_test(pl1, pl2)
        verifier(not hors and md_egal, f"fichier test changé par test_final : {hors[:5]} ; Markdown égal {md_egal}")
        verifier((o1[2], o1[3]) == (o2[2], o2[3]), f"ligne d'état : {o1[2:4]} contre {o2[2:4]}")
        return ("test_final changée (justes, non-réponses de 3 % à 25 %) : fichier test identique hors de l'heure et des empreintes "
                "de la liste et de l'archive (projection `test` et score.json identiques) ; ligne d'état identique")

    def w_anomalie_final():
        def alterer(pilote, dl, espace):
            p = dl / "g002" / "juge" / "score-final.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            d["par_famille"][FAMD]["exactitude_equilibree"] = round(d["par_famille"][FAMD]["exactitude_equilibree"] + 0.01, 4)
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            A.sceller(p)
        pl = plan_libre(publique, "T", "F1", lambda g, f: 0.6, lambda g, f: 0.6)
        o1, o2, hors, md_egal = paire_test(pl, pl, avant2=alterer)
        verifier(not hors and md_egal and (o1[2], o1[3]) == (o2[2], o2[3]) == (4, 0), f"{hors[:5]} ; {o1[2:4]} {o2[2:4]}")
        return "anomalie de score-final.json seule : fichier test et ligne d'état (« signalements (fichier test) : 0 ») identiques"

    def w_ecartee_final():
        pl = plan_libre(publique, "T", "F1", lambda g, f: 0.6, lambda g, f: 0.6, ps_f=0.2)

        def lues_de(g, lues):
            if g != 1:
                return lues
            libre = [t for t in publique["test_final"] if t["id"] not in lues][0]
            return {**lues, libre["id"]: "peut-etre"}
        o1, o2, hors, md_egal = paire_test(pl, pl, lues2=lues_de)
        verifier(not hors and md_egal and o1[3] == o2[3], f"fichier test changé par une entrée écartée de test_final : {hors[:5]}")
        return "entrée écartée d'une tâche de test_final : fichier test et ligne d'état identiques"

    def w_test_change():
        pl1 = plan_libre(publique, "T1", "F", lambda g, f: 0.6, lambda g, f: 0.6, ps_t=0.03)
        pl2 = plan_libre(publique, "T2", "F", lambda g, f: 0.4, lambda g, f: 0.6, ps_t=0.25)
        p1, p2 = fabriquer(racine("M"), M, publique, pl1), fabriquer(racine("M"), M, publique, pl2)
        o1, _ = lire_final(p1, None, [M[0]], trace=False)
        o2, _ = lire_final(p2, None, [M[0]], trace=False)
        (d1, m1), (d2, m2) = o1[M[0]], o2[M[0]]
        diff = differences(d1, d2)
        hors = [x for x in diff if x not in (".quand_utc", ".course.empreinte_liste", ".course.empreinte_archive")
                and not (re.fullmatch(r"\.course\.membres_lus\[[0-9]+\]\.sha256", x)
                         and d1["course"]["membres_lus"][int(re.search(r"\[([0-9]+)\]", x).group(1))]["membre"].endswith("reponses-lues.json"))]
        masques = lambda d: [d["course"]["empreinte_liste"], d["course"]["empreinte_archive"]] + [  # noqa: E731
            m["sha256"] for m in d["course"]["membres_lus"] if m["membre"].endswith("reponses-lues.json")]
        verifier(not hors and md_norm(m1, masques(d1)) == md_norm(m2, masques(d2)), f"fichier test_final changé par test : {hors[:5]}")
        return ("réciproque : test changée : fichier test_final (holm-deux) identique hors de l'heure, des empreintes de la liste, "
                "de l'archive et de reponses-lues.json")

    def w_inconnue_ecartee_test():
        pl = plan_libre(publique, "T", "F", lambda g, f: 0.6, lambda g, f: 0.6, ps_t=0.2)

        def lues_de(g, lues):
            if g != 2:
                return lues
            libre = [t for t in publique["test"] if t["id"] not in lues][0]
            return {**lues, "ZQXinconnue0000": "evaluation", libre["id"]: "peut-etre"}
        p = fabriquer(racine("M"), M, publique, pl, lues_de=lues_de)
        dt, mdt, k, n, _ = lire_test(p, M[0], trace=False)
        o, _ = lire_final(p, None, [M[0]], trace=False)
        df = o[M[0]][0]
        st, sf = dt["signalements"], df["signalements"]
        inc_t, inc_f = [x for x in st if "hors de la banque" in x], [x for x in sf if "hors de la banque" in x]
        ec_t, ec_f = [x for x in st if "écartée" in x and "hors de la banque" not in x], [x for x in sf if "écartée" in x and "hors" not in x]
        verifier(inc_t == inc_f and len(inc_t) == 1 and len(ec_t) == 1 and not ec_f and n == 2, f"test {st} ; test_final {sf} ; N {n}")
        return "identifiant hors banque : signalement commun (les deux fichiers) ; entrée écartée d'une tâche de test : fichier test seul ; N = 2"

    cas("entre parts : test_final changée, fichier test et ligne d'état identiques", "artefact", w_final_change)
    cas("entre parts : anomalie de score-final.json, fichier test et ligne d'état identiques (RSL2-02)", "artefact", w_anomalie_final)
    cas("entre parts : entrée écartée d'une tâche de test_final, fichier test identique (RSL2-03)", "artefact", w_ecartee_final)
    cas("entre parts : test changée, fichier test_final identique", "artefact", w_test_change)
    cas("entre parts : identifiant inconnu (commun) et entrée écartée de test (fichier test seul)", "artefact", w_inconnue_ecartee_test)

    # ------------------------------------------------ garde de séparation : fausses alertes
    def g_serie_aleatoire():
        """Paires tirées au hasard (profils, non-réponses, g3 absente, anomalies) : jamais de refus ; union = calcul joint ;
        recherche propre au harnais : aucun nombre propre à l'autre course dans un fichier."""
        rng = random.Random(20261026)
        n_ok, n_cherches = 0, 0
        for k in range(n_fuzz):
            plans = []
            for cote in ("M", "S"):
                pj = {g: {f: rng.uniform(0.3, 0.95) for f in (FAMC, FAMD)} for g in range(4)}
                gens = (0, 1, 2) if rng.random() < 0.1 else (0, 1, 2, 3)
                plans.append(plan_libre(publique, f"T{k}{cote}", f"F{k}{cote}", lambda g, f, pj=pj: pj[g][f],
                                        lambda g, f, pj=pj: pj[g][f], ps_t=rng.uniform(0, 0.3), ps_f=rng.uniform(0, 0.3), generations=gens))
            if rng.random() < 0.2:  # coïncidences : la même part test_final en g1 dans les deux courses
                ids_f = {t["id"] for t in publique["test_final"]}
                plans[1][1] = ({k: v for k, v in plans[1][1].items() if k not in ids_f}
                               | {k: v for k, v in plans[0][1].items() if k in ids_f})
            px = fabriquer(racine("M"), M, publique, plans[0])
            py = fabriquer(racine("S"), S, publique, plans[1])
            out, _ = lire_final(px, py, [M[0], S[0]], trace=False)
            atts = [attendu_iii(publique, p) for p in plans]
            v = verdicts_joints(atts)
            union = [t for nom in (M[0], S[0]) for t in out[nom][0]["mcnemar_generation_0_contre_3"]["tests"]]
            verifier([(t["verdict"], t["sens_du_rejet"]) for t in union] == v, f"tirage {k} : union {union} contre {v}")
            for (x, y) in ((M[0], S[0]), (S[0], M[0])):
                dx, mdx = out[x]
                dy, _ = out[y]
                nombres_x = {float(f) for f in feuilles(dx) if isinstance(f, (int, float)) and not isinstance(f, bool)}
                propres = set()
                for v_ in valeurs_doc(dy):
                    if float(v_) not in nombres_x and float(v_) not in (0.0, 1.0):
                        propres |= ecritures(v_, p=isinstance(v_, Fraction))
                n_cherches += len(propres)
                fuite = propres & (jetons_nombres(json.dumps(dx, ensure_ascii=False)) | jetons_nombres(mdx))
                verifier(not fuite, f"tirage {k} : nombres propres à {y} dans le fichier de {x} : {sorted(fuite)[:5]}")
            n_ok += 1
        CONSTATS.append(("garde, série tirée au hasard", f"{n_ok} lectures écrites, aucune fausse alerte ; {n_cherches} écritures propres cherchées"))
        return f"{n_ok} paires tirées au hasard : toutes écrites (aucune fausse alerte), union = calcul joint, aucune écriture propre à l'autre course ({n_cherches} cherchées)"

    def nombres_de_m():
        att_m_l, sous_m = attendu_part(publique, absentes, plan_m, "test_final")
        return ({round(a[k], 4) for a in att_m_l.values() for k in ("ee", "basse", "haute")}
                | {round(a[k], 4) for a in sous_m.values() for k in ("ee", "part")}
                | {0.8333, 0.75, 0.6944, 0.8056, 0.7818, 0.7049, 0.0, 1.0})

    def proportions_propres_a_s():
        """Proportions de S (lignes et sous-ensemble de test_final) égales à aucun nombre de M (refaites ici)."""
        att_s_l, sous_s = attendu_part(publique, absentes, plan_s, "test_final")
        nm = nombres_de_m()
        vals = ([round(a[k], 4) for _, a in sorted(att_s_l.items()) for k in ("ee", "basse", "haute")]
                + [round(a[k], 4) for _, a in sorted(sous_s.items()) for k in ("part", "ee")])
        return [v for v in vals if v not in nm]

    def g_ecart_noyau():
        """Score du noyau de M divergent (écart), écrit à quatre décimales comme une proportion de S sans lui être égal :
        si la garde y voit l'écriture de S, elle refuse toute la lecture finale (fausse alerte, aucune valeur de S n'est
        dans le fichier de M)."""
        cible = proportions_propres_a_s()[0]

        def alterer(pilote, dl, espace):
            p = dl / "g002" / "juge" / "score-final.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            d["par_famille"][FAMC]["exactitude_equilibree"] = cible + 0.00002
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            A.sceller(p)
        pm_ecart = fabriquer(racine("M"), M, publique, plan_m, avant_tar=alterer)
        s = sortie()
        try:
            run.lancer(["test_final", "--course-m", pm_ecart, "--course-s", ps, banque, s], var=var, sortie=s, code=0, trace=False)
            issue = "écrite"
        except AssertionError as e:
            issue = f"non écrite : {str(e)[:200]}"
        CONSTATS.append(("garde, score du noyau de M divergent (écrit à quatre décimales comme une proportion de S, "
                         f"{cible + 0.00002!r} contre {cible!r})", issue))
        verifier(issue == "écrite", f"FAUSSE ALERTE : {issue}")
        return "score du noyau de M divergent, écrit comme une proportion de S : lecture écrite"

    cas("garde : série tirée au hasard, aucune fausse alerte", "sain", g_serie_aleatoire)
    cas("garde : score du noyau divergent écrit comme une proportion de l'autre course", "artefact", g_ecart_noyau)

    # ------------------------------------------------ noms, options, même course
    def a_options():
        s = sortie()
        run.lancer(["test_final", "--course-m", ps, "--course-s", pm, banque, s], var=var, sortie=s, code=3, motif="--course-m attend")
        s = sortie()
        run.lancer(["test_final", "--course-m", pm, "--course-s", pm, banque, s], var=var, sortie=s, code=3, motif="--course-s attend")
        pm3 = fabriquer(racine("M"), M3, publique, plan_m)
        s = sortie()
        run.lancer(["test_final", "--course-m", pm3, "--course-s", pm, banque, s], var=var, sortie=s, code=3, motif="--course-s attend")
        s = sortie()
        run.lancer(["test_final", "--course-m", pm, banque, s], var=var, sortie=s, code=2)
        s = sortie()
        run.lancer(["test_final", "--course-m", pm, "--course-s", ps, "--sans-seconde-course", banque, s], var=var, sortie=s, code=2)
        cs_lignee_m = fabriquer(racine("S"), (S[0], M[1]), publique, plan_s)
        s = sortie()
        run.lancer(["test_final", "--course-m", pm, "--course-s", cs_lignee_m, banque, s], var=var, sortie=s, code=3,
                   motif="n'est pas celle de la course nommée")
        return "options échangées, M deux fois, deux tentatives de M, aucune option S, deux options S : refus ; S à la lignée de M : refus"

    def a_noms():
        for nom in ("pilote4-gemini-v5-3-v1", "pilote4-gemini-v6-2-s-v1-tentative0", "pilote4-gemini-v6-2-s-v2", "pilote4-gemini-v6-2-v1.copie"):
            d = base / "noms" / nom
            shutil.copytree(pm, d)
            s = sortie()
            run.lancer(["test", "--course", d, banque, s], var=var, sortie=s, code=3, motif="nom du dossier de course inattendu")
        return "dossiers v5-3, -tentative0, s-v2, nom à point : refus en mode test"

    def a_sortie_existante():
        s = sortie()
        run.lancer(["test_final", "--course-m", pm, "--course-s", ps, banque, s], var=var, sortie=s, trace=False)
        avant = {n: A.hf(s / n) for n in os.listdir(s)}
        run.lancer(["test_final", "--course-m", pm, "--course-s", ps, banque, s], var=var, sortie=s, code=3, motif="existe déjà", trace=False)
        verifier({n: A.hf(s / n) for n in os.listdir(s)} == avant, "SORTIE changée")
        return "seconde lecture test_final dans la même SORTIE : refus, fichiers inchangés"

    def a_score_final_trop_grand():
        """score-final.json de g1 au-delà de la borne des membres : le mode test ne le voit pas (lecture écrite, égale au
        calcul) ; le mode test_final refuse l'archive."""
        def gonfler(pilote, dl, espace):
            p = dl / "g001" / "juge" / "score-final.json"
            p.write_bytes(b"{" + b" " * 16_500_000 + b"}")
            A.sceller(p)
        pg = fabriquer(racine("M"), M, publique, plan_m, avant_tar=gonfler)
        dt, mdt, k, n, _ = lire_test(pg, M[0], trace=False)
        verifier_fichier_test(dt, mdt, M, publique, absentes, plan_m, pg)
        s = sortie()
        run.lancer(["test_final", "--course-m", pg, "--sans-seconde-course", banque, s], var=var, sortie=s, code=3,
                   motif="au-delà de 16000000 octets", trace=False)
        return "score-final.json de g1 de 16,5 Mo : mode test écrit (égal au calcul), mode test_final refuse l'archive"

    cas("score-final.json trop grand : mode test indifférent, mode test_final refuse", "artefact", a_score_final_trop_grand)
    cas("options, rôles M et S, lignée", "artefact", a_options)
    cas("noms de dossier refusés", "artefact", a_noms)
    cas("SORTIE déjà écrite (R12)", "artefact", a_sortie_existante)

    # ------------------------------------------------ commandes du LISEZMOI v3 § 5, telles qu'écrites
    def c_lisezmoi():
        lis = (COPIE4 / "LISEZMOI-script-lecture-v4.md").read_text(encoding="utf-8")
        sec = lis[lis.index("## 5. Commandes pour session-depot"):lis.index("## 6. ")]
        blocs = re.findall(r"```\n(.*?)```", sec, re.S)
        verifier(len(blocs) == 6, f"{len(blocs)} blocs de commandes")
        lanc = base / "lancement"
        for course, plan in ((M, plan_m), (S, plan_s)):
            p = fabriquer(lanc, course, publique, plan)
        (lanc / "R").rename(lanc / "essaim-m3-refonte-v1")
        sorties5 = base / "sorties-commandes"
        sorties5.mkdir()
        script = "\n".join(blocs)
        remplacements = [
            ("BANQUE_DIR=<dossier qui porte banque-confrontation-v3.json et banque-confrontation-v3-secret.json>", f"BANQUE_DIR='{banque}'"),
            ("LECTURE=<dossier où sont copiés lire_pilote4_v4.py et lire_pilote4_v4.py.sha256>", f"LECTURE='{COPIE4}'"),
            ("SORTIES=<dossier existant où naissent les dossiers de sortie>", f"SORTIES='{sorties5}'"),
            ("unset LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE", f"export LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE='{var}'"),
            ("python3 -I -B", f"{python} -I -B")]
        for a, b in remplacements:
            verifier(a in script, f"ligne attendue absente du § 5 : {a}")
            script = script.replace(a, b)
        avant = {n: A.hf(COPIE4 / n) for n in os.listdir(COPIE4) if (COPIE4 / n).is_file()}
        r = subprocess.run(["bash", "-c", "set -u\n" + script], cwd=lanc, capture_output=True, text=True,
                           env={k: v for k, v in os.environ.items() if k != A.VAR})
        lignes = r.stdout.strip().splitlines()
        verifier(r.returncode == 0 and lignes[0] == "lire_pilote4_v4.py: OK" and lignes.count("code 0") == 4
                 and lignes[1].startswith("essai-banque : catégorie absente du train — test 8 (evaluation 4, usage-reel 4) ; "
                                          "test_final 14 (evaluation 10, usage-reel 4) ; issue : conforme"), f"sortie : {lignes} ; {r.stderr[-300:]}")
        attendu = {"lecture-test-M-v4": [f"lecture-{M[0]}-test-v4"], "lecture-test-S-v4": [f"lecture-{S[0]}-test-v4"],
                   "lecture-test-final-holm-quatre-v4": [f"lecture-{M[0]}-test-final-holm-quatre-v4", f"lecture-{S[0]}-test-final-holm-quatre-v4"],
                   "lecture-test-final-holm-deux-v4": [f"lecture-{M[0]}-test-final-holm-deux-v4"]}
        for d, bases in attendu.items():
            verifier(sorted(os.listdir(sorties5 / d)) == sorted(b + s for b in bases for s in (".json", ".md", ".json.sha256", ".md.sha256")),
                     f"{d} : {sorted(os.listdir(sorties5 / d))}")
        for n in ("test-M", "test-S", "test-final-holm-quatre", "test-final-holm-deux"):
            etat = (sorties5 / f"etat-lecture-{n}-v4.txt").read_text(encoding="utf-8").splitlines()
            err = (sorties5 / f"erreurs-lecture-{n}-v4.txt").read_text(encoding="utf-8").splitlines()
            verifier(len(etat) == 1 and etat[0].startswith("lecture écrite : ") and A.DECIMAL.search(etat[0]) is None, f"état {n} : {etat}")
            verifier(len(err) == 1 and err[0].startswith("ESSAI : "), f"erreurs {n} : {err}")
        verifier({n: A.hf(COPIE4 / n) for n in os.listdir(COPIE4) if (COPIE4 / n).is_file()} == avant
                 and not [n for n in os.listdir(COPIE4) if n.startswith(("lecture-", "__pycache__"))], "copie modifiée")
        return ("les six blocs du § 5 lancés tels qu'écrits depuis le dossier de lancement (chemins relatifs « essaim-m3-refonte-v1 ») : "
                "sha256sum -c OK, essai-banque conforme, quatre « code 0 », noms et fichiers d'état conformes, copie inchangée")

    cas("commandes du LISEZMOI v3 § 5 telles qu'écrites", "sain", c_lisezmoi)

    # ------------------------------------------------ pannes et plantations injectées dans le processus du script
    if en_processus:
        def charger():
            sp = importlib.util.spec_from_file_location("lire_v3_en_processus", A.SCRIPT)
            L = importlib.util.module_from_spec(sp)
            sp.loader.exec_module(L)
            return L

        def principal_capture(L, argv):
            tampon, vrai = io.StringIO(), sys.stdout
            sys.stdout = tampon
            os.environ[A.VAR] = var
            try:
                code = L.principal([str(a) for a in argv])
            finally:
                sys.stdout = vrai
                os.environ.pop(A.VAR, None)
            return code, tampon.getvalue().strip()

        def p_plantations():
            """Plantées dans les octets du fichier de M, juste avant la garde : une écriture de S qui n'est égale à aucun
            nombre de M (proportion du sous-ensemble, borne haute en nombre JSON, valeur p en fraction) : refus attendu ;
            un entier de S (justes d'une classe) : non cherché (déclaré au LISEZMOI § 3.2)."""
            propres = proportions_propres_a_s()
            verifier(len(propres) >= 2, f"prémisse : proportions propres à S {propres}")
            p_s = att_s[FAMC]["p"]
            issues = []
            for etiquette, planter, attendu_refus in (
                    (f"proportion de S ({propres[-1]}) écrite à quatre décimales dans le Markdown",
                     lambda j, m: (j, m + f"\n({propres[-1]:.4f})".replace(".", ",").encode()), True),
                    (f"proportion de S ({propres[0]}) en nombre JSON",
                     lambda j, m: (j.replace(b'"phrase_iv"', f'"note": {propres[0]!r}, "phrase_iv"'.encode(), 1), m), True),
                    ("valeur p de S en fraction", lambda j, m: (j, m + f"\n({p_s.numerator}/{p_s.denominator})".encode()), True),
                    ("justes d'une classe de S (entier)", lambda j, m: (j, m + b"\n| 17 |"), False)):
                L = charger()
                vrai = L.contenus_du_fichier

                def contenus(doc, vrai=vrai, planter=planter):
                    j, m = vrai(doc)
                    return planter(j, m) if doc["course"]["nom"] == M[0] else (j, m)
                L.contenus_du_fichier = contenus
                s = sortie()
                code, dit = principal_capture(L, ["test_final", "--course-m", pm, "--course-s", ps, banque, s])
                vide = not s.exists() or not os.listdir(s)
                verifier((code == 3 and vide) if attendu_refus else (code == 0), f"{etiquette} : code {code}, SORTIE vide {vide}")
                issues.append(f"{etiquette} : {'refus' if code == 3 else 'écrit (non cherché, déclaré)'}")
            return " ; ".join(issues)

        def p_rsl2_05():
            L = charger()
            vrai_link, vrai_open = os.link, builtins.open
            compte = {"x": 0}

            def link(*a, **k):
                raise OSError(errno.EPERM, "liens durs refusés (simulé)")

            def ouvrir(fichier, mode="r", *a, **k):
                f = vrai_open(fichier, mode, *a, **k)
                nom = os.path.basename(str(fichier))
                if mode == "xb" and nom.startswith("lecture-"):
                    compte["x"] += 1
                    if compte["x"] == 3:
                        class Casse:
                            def __enter__(self_):
                                return self_

                            def __exit__(self_, *e):
                                f.close()
                                return False

                            def write(self_, octets):
                                f.write(octets[: len(octets) // 2])
                                raise OSError(errno.ENOSPC, "plus de place (simulé)")
                        return Casse()
                return f
            L.os.link, L.open = link, ouvrir
            s = sortie()
            try:
                code, dit = principal_capture(L, ["test_final", "--course-m", pm, "--course-s", ps, banque, s])
            finally:
                L.os.link = vrai_link
                del L.open
            restes = sorted(os.listdir(s)) if s.exists() else []
            verifier(code == 4 and not restes, f"code {code}, restes {restes}")
            return "liens durs refusés, moitié du troisième fichier écrite puis « plus de place » : code 4, SORTIE vide"

        def p_rsl2_06():
            L = charger()
            vrai_print = builtins.print

            def imprimer(*a, **k):
                if a and str(a[0]).startswith("lecture écrite : ") and k.get("file") is None:
                    raise KeyboardInterrupt
                return vrai_print(*a, **k)
            L.print = imprimer
            s = sortie()
            try:
                code, dit = principal_capture(L, ["test", "--course", pm, banque, s])
            finally:
                del L.print
            presents = sorted(x for x in os.listdir(s) if not x.startswith("."))
            verifier(code == 130 and dit.startswith("lecture écrite, interrompue avant la ligne d'état : ") and len(presents) == 4,
                     f"code {code}, « {dit} », {presents}")
            return f"interruption sur la ligne d'état : code 130, « {dit[:52]}… », 4 fichiers présents"

        cas("plantations dans le fichier de M avant la garde", "artefact", p_plantations)
        cas("écriture sans liens durs, panne au troisième fichier (RSL2-05)", "artefact", p_rsl2_05)
        cas("interruption après l'écriture (RSL2-06)", "artefact", p_rsl2_06)


def feuilles(objet):
    if isinstance(objet, dict):
        return [x for v in objet.values() for x in feuilles(v)]
    if isinstance(objet, list):
        return [x for v in objet for x in feuilles(v)]
    return [objet]


def valeurs_doc(doc) -> list:
    """Proportions (exactitudes, bornes, sous-ensembles) et valeurs p (fractions) d'un fichier, relues par le harnais."""
    out = []
    for fam in (FAMC, FAMD):
        for ln in doc["lecture"][fam]:
            if isinstance(ln.get("intervalle"), dict):
                out += [ln["exactitude_equilibree"], ln["intervalle"]["basse"], ln["intervalle"]["haute"]]
    for ln in doc["categorie_absente_du_train"]["par_generation"]:
        if "impossible" not in ln:
            out += [ln["exactitude_equilibree"], ln["part_sans_reponse"]]
    for t in doc.get("mcnemar_generation_0_contre_3", {}).get("tests", []):
        if t["p"] is not None:
            a, b = t["p_exacte"].split("/")
            out.append(Fraction(int(a), int(b)))
    return out


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--python", required=True)
    p.add_argument("--fuzz", type=int, default=24)
    p.add_argument("--en-processus", action="store_true")
    p.add_argument("--garder", action="store_true")
    a = p.parse_args()
    version = subprocess.run([a.python, "-I", "-c", "import platform; print(platform.python_version())"],
                             capture_output=True, text=True, check=True).stdout.strip()
    print(f"# vérification de la v4 — artefacts — début {A.heure()} (UTC)")
    print(f"# script relu {A.SCRIPT} {A.hf(A.SCRIPT)} ; exécuté par {a.python} (Python {version}) ; harnais {sys.executable}")
    print(f"# ce harnais {A.hf(__file__)} ; fabrication reprise {A.hf(OUTILS / 'artefacts_relecture_v1_repris.py')} ; trace {A.hf(A.TRACE)}")
    print(f"# phrase (iv) prise dans le brief : {len(PHRASE_IV)} caractères ; libellés pris dans le brief et le message de correction")
    base = R3 / f"travail-v4-py{version}-{os.getpid()}"
    base.mkdir()
    t0 = time.time()
    try:
        lancer(base, a.python, a.fuzz, a.en_processus)
    finally:
        if not a.garder:
            shutil.rmtree(base)
    caches = [pathlib.Path(A.NOYAU) / "essaim_m3" / "__pycache__", pathlib.Path(A.NOYAU) / "essaim_m3" / "noyau" / "__pycache__"]
    ok_caches = not any(c.exists() for c in caches) and not (COPIE / "__pycache__").exists() and not (COPIE4 / "__pycache__").exists()
    print(f"{'OK    ' if ok_caches else 'ÉCHEC '} [contrôle] aucun cache écrit dans le noyau importé ni dans la copie : {ok_caches}")
    for k, v in CONSTATS:
        print(f"# constaté — {k} : {v}")
    for genre in ("sain", "artefact"):
        x = [r for r in RESULTATS if r[1] == genre]
        print(f"# {genre} : {sum(r[2] for r in x)} sur {len(x)} conformes")
    print(f"# bilan ; durée {int(time.time() - t0)} s ; fin {A.heure()} (UTC)")
    return 0 if all(r[2] for r in RESULTATS) and ok_caches else 1


if __name__ == "__main__":
    sys.exit(principal())
