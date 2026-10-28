#!/usr/bin/env python3
"""Seconde relecture (script de lecture v2) — cas sains, artefacts et preuves de séparation de la relecture, v1.

Lancé par : /opt/venv-essaim-sim-v1/bin/python -I artefacts_relecture_v2_sur_v2.py --python INTERPRETE [--en-processus]

Réutilise, sans les changer, les fonctions de fabrication de la première relecture (`artefacts_relecture_v1_repris.py`,
copie à l'octet de `9d6b65d7…` : banque inventée, arbre de course écrit comme le noyau, archive par la commande du
lanceur, liste fermée par ses lignes 909–919, exécuteur à instantanés et trace d'audit) ; le script relu est la copie
`lire_pilote4_v2.py`, exécutée par INTERPRETE avec `-I -B`, directement puis sous la trace des écritures.
Ce qui est propre à cette relecture :
- séparation par **non-interférence** : deux courses qui ne diffèrent que par une part (réponses, anomalies, entrées
  du fichier des réponses lues) sont lues ; le fichier de l'autre part doit être identique, à l'heure, aux empreintes du
  dossier et de l'archive et à l'empreinte de `reponses-lues.json` près ; toute autre différence est une fuite ; la
  ligne d'état est comparée de même ;
- valeurs de chaque part refaites indépendamment (Wilson en décimal, McNemar par la loi binomiale, Holm pas à pas) ;
- courses M (`pilote4-gemini-v6-2-v1-tentative2`) et S (`pilote4-gemini-v6-2-s-v1[-tentativeN]`) : appariement, garde
  « même course » sur deux courses réellement distinctes du même nom de course, contrôle nom ↔ lignée ;
- commandes du LISEZMOI v2 § 5 lancées telles qu'écrites (dossier courant : la copie du script) ;
- avec --en-processus : deux cas qui exigent d'injecter une panne dans le processus du script (écriture sans liens durs
  avec une erreur d'écriture ; interruption juste après l'écriture des fichiers).
Données inventées seulement (marques « ZQX », « TXTRL », « CATRL ») ; tout est écrit sous
/var/tmp/relecture-script-lecture-pilote4-v2/.
"""
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import builtins  # noqa: E402
import errno  # noqa: E402
import importlib.util  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import pathlib  # noqa: E402
import random  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

R2 = pathlib.Path("/var/tmp/relecture-script-lecture-pilote4-v2")
OUTILS = R2 / "outils"
_spec = importlib.util.spec_from_file_location("artefacts_relecture_v1_repris", OUTILS / "artefacts_relecture_v1_repris.py")
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)
A.RACINE = R2
A.COPIE = R2 / "copie"
A.SCRIPT = A.COPIE / "lire_pilote4_v2.py"
A.TRACE = OUTILS / "trace_ecritures_v1_reprise.py"

FAMC, FAMD, ETQ, REF = A.FAMC, A.FAMD, A.ETQ, A.REF
M = ("pilote4-gemini-v6-2-v1-tentative2", "gemini-organisme-v6-2")
M3 = ("pilote4-gemini-v6-2-v1-tentative3", "gemini-organisme-v6-2")
S = ("pilote4-gemini-v6-2-s-v1", "gemini-organisme-v6-2-s")
S3 = ("pilote4-gemini-v6-2-s-v1-tentative3", "gemini-organisme-v6-2-s")
VERDICT_CONSTRUCTION = "impossible par construction (référence égale à 1)"
RESULTATS = []
CONSTATS = []


def verifier(c, m):
    if not c:
        raise AssertionError(m)


# ---------------------------------------------------------------- réponses par part (pour les paires de non-interférence)


def reponses_part(publique, part, graine, g, p_juste, p_sans=0.06):
    rng = random.Random(f"{graine}|{part}|{g}")
    retenues = {}
    for t in publique[part]:
        fam, v = t["famille"], t["verite"]
        autre = ETQ[fam][1] if v == ETQ[fam][0] else ETQ[fam][0]
        if rng.random() < p_sans:
            continue
        retenues[t["id"]] = v if rng.random() < p_juste(g, fam) else autre
    return retenues


def fabriquer_course_parts(base, racine, nom, lignee, publique, graine_t, graine_f, pj_t, pj_f, ps_t=0.06, ps_f=0.06,
                           avant_tar=None, generations=(0, 1, 2, 3)):
    """Comme `fabriquer_course` de la première relecture, mais chaque part a sa graine : deux courses à la même graine de
    `test` ont exactement les mêmes réponses de `test` (et réciproquement)."""
    retenues = {}
    sauvegarde = A.ecrire_generation

    def ecrire_generation(dg, pub, graine, g, profil, manques=True):
        lues = {**reponses_part(pub, "test", graine_t, g, pj_t, ps_t), **reponses_part(pub, "test_final", graine_f, g, pj_f, ps_f)}
        brut = {k: {"etiquette": v, "confiance": 0.5} for k, v in lues.items()}
        s, f = A.scores_noyau(pub, lues)
        A.ecrire(dg / "organisme.tar.gz", b"organisme fictif")
        A.sceller(dg / "organisme.tar.gz")
        j = dg / "juge"
        A.ecrire(j / "score.json", json.dumps(s, ensure_ascii=False, indent=1))
        A.sceller(j / "score.json")
        A.ecrire(j / "score-final.json", json.dumps(f, ensure_ascii=False, indent=1))
        A.sceller(j / "score-final.json")
        A.ecrire(j / "reponses_test.json", json.dumps(brut, ensure_ascii=False))
        A.sceller(j / "reponses_test.json")
        A.ecrire(j / "reponses-lues.json", json.dumps({"reponses": lues, "probleme_reponses": None}, ensure_ascii=False,
                                                      indent=1, sort_keys=True))
        A.sceller(j / "reponses-lues.json")
        A.ecrire(dg / "resume.json", json.dumps({"statut": "OK", "generation": g}))
        A.sceller(dg / "resume.json")
        retenues[g] = lues
        return lues
    A.ecrire_generation = ecrire_generation
    try:
        pilote, _ = A.fabriquer_course(racine, nom, lignee, publique, "inutile", A.profil_v62, generations=generations,
                                       espace_bizarre=False, avant_tar=avant_tar)
    finally:
        A.ecrire_generation = sauvegarde
    return pilote, retenues


# ---------------------------------------------------------------- lecture des sorties v2


LIGNE_ETAT = re.compile(r"^lecture écrite : (.+) ; générations notées lues : ([0-9]+) sur 4 ; signalements : ([0-9]+)"
                        r"( \[essai : empreintes de banque surchargées\])?$")


def sorties_v2(sout, sortie, nom, regle):
    bt, bf = f"lecture-{nom}-test-v2", f"lecture-{nom}-test-final-{regle}-v2"
    attendus = sorted(x + s for x in (bt, bf) for s in (".json", ".md", ".json.sha256", ".md.sha256"))
    presents = sorted(x for x in os.listdir(sortie) if x.startswith(f"lecture-{nom}-"))
    verifier(presents == attendus, f"SORTIE : {presents}")
    verifier(not [x for x in os.listdir(sortie) if "en-cours" in x], "fichier provisoire laissé")
    textes = {}
    for n in (bt + ".json", bt + ".md", bf + ".json", bf + ".md"):
        verifier((sortie / (n + ".sha256")).read_text(encoding="utf-8") == f"{A.hf(sortie / n)}  {n}\n", f"compagnon : {n}")
        textes[n] = (sortie / n).read_text(encoding="utf-8")
        for m in A.MARQUES:
            verifier(m not in textes[n], f"{n} porte la marque {m}")
    m = LIGNE_ETAT.match(sout.strip())
    verifier(m is not None, f"ligne d'état : {sout!r}")
    for n in textes:
        verifier(f"{n} {A.hf(sortie / n)}" in m.group(1), f"ligne d'état sans {n}")
    return (json.loads(textes[bt + ".json"]), json.loads(textes[bf + ".json"]), textes[bt + ".md"], textes[bf + ".md"],
            int(m.group(2)), int(m.group(3)))


def comparer_part(doc, part, publique, absentes, retenues, generations):
    n = 0
    for fam in (FAMC, FAMD):
        pos, neg = ETQ[fam]
        ts = [t for t in publique[part] if t["famille"] == fam]
        npos = sum(t["verite"] == pos for t in ts)
        nneg = len(ts) - npos
        for g in generations:
            rep = retenues[g]
            jp = sum(1 for t in ts if t["verite"] == pos and rep.get(t["id"]) == pos)
            jn = sum(1 for t in ts if t["verite"] == neg and rep.get(t["id"]) == neg)
            sans = sum(1 for t in ts if t["id"] not in rep)
            wp, wn = A.wilson_dec(jp, npos), A.wilson_dec(jn, nneg)
            basse, haute = (wp[0] + wn[0]) / 2, (wp[1] + wn[1]) / 2
            verdict = (VERDICT_CONSTRUCTION if REF[fam][part] >= 1 else
                       "au-dessus de la référence, au-delà du bruit des tâches" if basse > REF[fam][part]
                       else "non distinct de la référence")
            ln = [x for x in doc["lecture"][fam] if x["generation"] == g][0]
            verifier(ln["n_par_classe"] == {pos: npos, neg: nneg} and ln["justes_par_classe"] == {pos: jp, neg: jn}
                     and ln["sans_reponse"] == sans, f"{part} {fam} g{g} comptes : {ln}")
            verifier(A.proche(ln["exactitude_equilibree"], (jp / npos + jn / nneg) / 2), f"{part} {fam} g{g} exactitude")
            verifier(A.proche(ln["intervalle"]["basse"], basse) and A.proche(ln["intervalle"]["haute"], haute),
                     f"{part} {fam} g{g} Wilson : {ln['intervalle']} contre {basse}, {haute}")
            verifier(ln["verdict_ii"] == verdict and ln["recoupement"] == "concorde", f"{part} {fam} g{g} : {ln['verdict_ii']}, {ln['recoupement']}")
            n += 1
    pos, neg = ETQ[FAMC]
    ts = [t for t in publique[part] if t["id"] in absentes[part]]
    for g in generations:
        ln = [x for x in doc["categorie_absente_du_train"]["par_generation"] if x["generation"] == g][0]
        rep = retenues[g]
        jp = sum(1 for t in ts if t["verite"] == pos and rep.get(t["id"]) == pos)
        jn = sum(1 for t in ts if t["verite"] == neg and rep.get(t["id"]) == neg)
        npos = sum(t["verite"] == pos for t in ts)
        sans = sum(1 for t in ts if t["id"] not in rep)
        verifier(ln["effectif"] == len(ts) and ln["justes_par_classe"] == {pos: jp, neg: jn} and ln["sans_reponse"] == sans
                 and A.proche(ln["exactitude_equilibree"], (jp / npos + jn / (len(ts) - npos)) / 2), f"{part} sous-ensemble g{g} : {ln}")
    return n


def attendu_mcnemar(publique, retenues):
    return A.attendu_mcnemar(publique, retenues)


# ---------------------------------------------------------------- non-interférence


def differences(a, b, chemin=""):
    """Chemins JSON où a et b diffèrent."""
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(f"{chemin}.{k}")
            else:
                out += differences(a[k], b[k], f"{chemin}.{k}")
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            out += differences(x, y, f"{chemin}[{i}]")
    elif a != b:
        out.append(chemin)
    return out


PERMIS_JSON = re.compile(r"^\.(quand_utc|course\.empreinte_liste|course\.empreinte_archive|course\.membres_lus\[[0-9]+\]\.sha256)$")


def differences_non_permises(d1, d2):
    """Différences hors de l'heure, des empreintes du dossier et de l'archive, et des empreintes de membres lus (ce
    dernier point est vérifié à part : seules celles de `reponses-lues.json` ou du repli peuvent changer)."""
    diff = differences(d1, d2)
    hors = [x for x in diff if not PERMIS_JSON.match(x)]
    for x in diff:
        mm = re.match(r"^\.course\.membres_lus\[([0-9]+)\]\.sha256$", x)
        if mm:
            membre = d1["course"]["membres_lus"][int(mm.group(1))]["membre"]
            if not membre.endswith(("reponses-lues.json", "reponses_test.json")):
                hors.append(f"{x} ({membre})")
    return hors, diff


def md_normalise(t):
    t = re.sub(r"[0-9a-f]{64}", "<empreinte>", t)
    return re.sub(r"le \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \(UTC\)", "le <heure> (UTC)", t)


# ---------------------------------------------------------------- les cas


def lancer(base: pathlib.Path, python: str, en_processus: bool):
    run = A.Executeur(python, base)
    publique, secret, absentes = A.fabriquer_banque(20261026)
    banque = base / "banque"
    var = A.ecrire_banque(banque, publique, secret)
    (base / "sorties").mkdir()
    n_s = [0]

    def sortie():
        n_s[0] += 1
        return base / "sorties" / f"s{n_s[0]:02d}"

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

    pj = lambda g, fam: 0.55 + 0.1 * g  # noqa: E731
    pj_bas = lambda g, fam: 0.35 + 0.05 * g  # noqa: E731
    cm, ret_m = fabriquer_course_parts(base, base, *M, publique, "T-m", "F-m", pj, pj)
    cs, ret_s = fabriquer_course_parts(base, base, *S, publique, "T-s", "F-s", pj_bas, pj)

    def lire(dossier, nom, regle, extra=(), code=0, motif=None):
        s = sortie()
        r, sout, serr = run.lancer(["lecture", dossier, banque, s] + list(extra), var=var, sortie=s, code=code, motif=motif)
        if code != 0:
            return None
        return sorties_v2(sout, s, nom, regle) + (sout,)

    # ------------------------------------------------ cas sains
    def s_m_seule():
        dt, df, mdt, mdf, k, n, _ = lire(cm, M[0], "provisoire")
        nt = comparer_part(dt, "test", publique, absentes, ret_m, (0, 1, 2, 3))
        nf = comparer_part(df, "test_final", publique, absentes, ret_m, (0, 1, 2, 3))
        att = attendu_mcnemar(publique, ret_m)
        for t in df["mcnemar_generation_0_contre_3"]["tests"]:
            p = att[t["famille"]][3]
            verifier(t["p_exacte"] == f"{p.numerator}/{p.denominator}" and t["verdict"].endswith("(provisoire, quatre tests au plus)"), f"{t}")
        verifier((k, n) == (4, 0) and dt["signalements"] == [] and df["signalements"] == [], f"{k} {n}")
        return (f"M ({M[0]}) : {nt} lignes de test et {nf} de test_final, sous-ensembles 8 et 14, McNemar "
                f"{[t['p_exacte'] for t in df['mcnemar_generation_0_contre_3']['tests']]} égaux au calcul indépendant ; ligne d'état « 4 sur 4 ; 0 »")

    def s_s_puis_m():
        dt, df, mdt, mdf, k, n, _ = lire(cs, S[0], "holm-quatre", [cm])
        comparer_part(dt, "test", publique, absentes, ret_s, (0, 1, 2, 3))
        comparer_part(df, "test_final", publique, absentes, ret_s, (0, 1, 2, 3))
        a_s, a_m = attendu_mcnemar(publique, ret_s), attendu_mcnemar(publique, ret_m)
        ps = [a_s[FAMC][3], a_s[FAMD][3], a_m[FAMC][3], a_m[FAMD][3]]
        rejet, ajust = A.holm_pas_a_pas(ps)
        mc = df["mcnemar_generation_0_contre_3"]
        verifier([t["course"] for t in mc["tests"]] == [S[0], S[0], M[0], M[0]], "ordre")
        verifier([t["p_ajustee_holm_exacte"] for t in mc["tests"]] == [f"{x.numerator}/{x.denominator}" for x in ajust]
                 and [t["verdict"].startswith("changement") for t in mc["tests"]] == rejet, f"Holm : {mc['tests']}")
        verifier(M[0] not in json.dumps(dt) and M[0] not in mdt, "la course M paraît dans le fichier test de S")
        return f"S puis M (ordre du LISEZMOI § 5) : Holm sur quatre, ajustées {[t['p_ajustee_holm_exacte'] for t in mc['tests']]} = pas à pas ; M absente du fichier test de S"

    def s_s_suffixee():
        cs3, ret_s3 = fabriquer_course_parts(base, base, *S3, publique, "T-s3", "F-s3", pj, pj_bas)
        dt, df, *_ = lire(cs3, S3[0], "holm-quatre", [cm])
        comparer_part(dt, "test", publique, absentes, ret_s3, (0, 1, 2, 3))
        verifier(df["course"]["lignee"] == S[1] and df["seconde_course"]["nom"] == M[0], f"{df['course']['lignee']}")
        return f"S au dossier suffixé ({S3[0]}) avec M : accepté, lignée {S[1]}, sortie au nom suffixé"

    cas("course M seule (dossier -tentative2) : deux lectures égales au calcul indépendant", "sain", s_m_seule)
    cas("course S puis M (LISEZMOI § 5) : Holm sur quatre", "sain", s_s_puis_m)
    cas("course S au dossier suffixé, avec M", "sain", s_s_suffixee)

    # ------------------------------------------------ séparation : non-interférence (artefacts de la relecture)
    def lire_paire(nom_paire, constr1, constr2, part_fixe, regle="provisoire", extra1=(), extra2=()):
        (d1, r1), (d2, r2) = constr1(), constr2()
        o1 = lire(d1, M[0], regle, extra1)
        o2 = lire(d2, M[0], regle, extra2)
        i = 0 if part_fixe == "test" else 1
        hors, diff = differences_non_permises(o1[i], o2[i])
        md1, md2 = md_normalise(o1[2 + i]), md_normalise(o2[2 + i])
        return o1, o2, hors, diff, md1 == md2

    def n_final_differente():
        o1, o2, hors, diff, md_egal = lire_paire(
            "final", lambda: fabriquer_course_parts(base, base / "P1", *M, publique, "T", "F1", pj, pj, ps_f=0.03),
            lambda: fabriquer_course_parts(base, base / "P2", *M, publique, "T", "F2", pj, pj_bas, ps_f=0.25), "test")
        verifier(not hors and md_egal, f"fuite de test_final dans le fichier test : {hors[:6]} ; Markdown égal : {md_egal}")
        verifier((o1[4], o1[5]) == (o2[4], o2[5]), f"ligne d'état : {o1[4:6]} contre {o2[4:6]}")
        changes = sorted({re.sub(r"\[[0-9]+\]", "[]", x) for x in diff})
        return (f"test identique, test_final différente (justes et non-réponses) : fichiers test égaux hors {changes} ; "
                "Markdown égal (heure et empreintes à part) ; lignes d'état égales")

    def n_test_differente():
        o1, o2, hors, diff, md_egal = lire_paire(
            "test", lambda: fabriquer_course_parts(base, base / "P3", *M, publique, "T1", "F", pj, pj, ps_t=0.03),
            lambda: fabriquer_course_parts(base, base / "P4", *M, publique, "T2", "F", pj_bas, pj, ps_t=0.25), "test_final")
        verifier(not hors and md_egal, f"fuite de test dans le fichier test_final : {hors[:6]} ; Markdown égal : {md_egal}")
        return "réciproque : test_final identique, test différente : fichiers test_final égaux (heure, empreintes à part)"

    def n_anomalie_final_seule():
        def alterer(pilote, dl, espace):
            p = dl / "g002" / "juge" / "score-final.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            d["par_famille"][FAMD]["exactitude_equilibree"] = round(d["par_famille"][FAMD]["exactitude_equilibree"] + 0.01, 4)
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
            A.sceller(p)
        o1, o2, hors, diff, md_egal = lire_paire(
            "anomalie", lambda: fabriquer_course_parts(base, base / "P5", *M, publique, "T", "F1", pj, pj),
            lambda: fabriquer_course_parts(base, base / "P6", *M, publique, "T", "F1", pj, pj, avant_tar=alterer), "test")
        verifier(not hors and md_egal, f"fuite dans le fichier test : {hors[:6]}")
        verifier(o2[1]["signalements"] and not o2[0]["signalements"], "prémisse : l'anomalie est dans test_final seule")
        fuite = (o1[5], o2[5])
        if fuite[0] != fuite[1]:
            CONSTATS.append(("ligne d'état", f"signalements {fuite[0]} contre {fuite[1]} pour une seule anomalie de test_final"))
        verifier(fuite[0] == fuite[1], f"FUITE : la ligne d'état compte une anomalie propre à test_final (signalements : "
                 f"{fuite[0]} sans, {fuite[1]} avec), alors que le fichier test est identique")
        return "anomalie de test_final seule : fichier test et ligne d'état inchangés"

    def n_entree_ecartee_final():
        def ajouter(pilote, dl, espace):
            p = dl / "g001" / "juge" / "reponses-lues.json"
            d = json.loads(p.read_text(encoding="utf-8"))
            libre = [t for t in publique["test_final"] if t["id"] not in d["reponses"]][0]
            d["reponses"][libre["id"]] = "peut-etre"  # entrée d'une tâche de test_final que la règle du juge écarte
            p.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
            A.sceller(p)
        o1, o2, hors, diff, md_egal = lire_paire(
            "ecartee", lambda: fabriquer_course_parts(base, base / "P7", *M, publique, "T", "F1", pj, pj, ps_f=0.15),
            lambda: fabriquer_course_parts(base, base / "P8", *M, publique, "T", "F1", pj, pj, ps_f=0.15, avant_tar=ajouter), "test")
        if hors:
            CONSTATS.append(("signalement commun", f"{hors[:3]} ; fichier test : {o2[0]['signalements']}"))
        verifier(not hors, f"FUITE (théorique) : une entrée écartée de test_final change le fichier test : {hors[:3]} — "
                 f"{o2[0]['signalements']}")
        return "entrée écartée de test_final : fichier test inchangé"

    def n_seconde_course_absente_du_test():
        cm2, _ = fabriquer_course_parts(base, base / "R2", *M, publique, "T-m2", "F-m2", pj_bas, pj_bas, ps_t=0.2, ps_f=0.2)
        o1 = lire(cs, S[0], "holm-quatre", [cm])
        o2 = lire(cs, S[0], "holm-quatre", [cm2])
        hors, diff = differences_non_permises(o1[0], o2[0])
        verifier(not diff or set(diff) <= {".quand_utc"}, f"le fichier test de S dépend de la course M : {diff[:5]}")
        verifier(md_normalise(o1[2]) == md_normalise(o2[2]), "Markdown test de S dépend de M")
        verifier(o1[1]["mcnemar_generation_0_contre_3"] != o2[1]["mcnemar_generation_0_contre_3"], "prémisse : Holm différent")
        return "S lue avec deux courses M différentes : fichier test de S identique (heure à part) ; seul test_final change"

    def n_mots_du_fichier_test():
        o = lire(cm, M[0], "provisoire")
        jt, mdt = json.dumps(o[0], ensure_ascii=False), o[2]
        mots = {m: (jt.count(m), mdt.count(m)) for m in ("test_final", "(iii)", "McNemar", "Holm", "seconde", "provisoire", "objets")}
        presents = {m: c for m, c in mots.items() if c != (0, 0)}
        CONSTATS.append(("mots du fichier test", str(presents)))
        verifier(mots["test_final"] == (0, 0) and mots["McNemar"] == (0, 0) and mots["Holm"] == (0, 0)
                 and mots["seconde"] == (0, 0) and mots["provisoire"] == (0, 0), f"{mots}")
        return f"fichier test : ni « test_final », ni McNemar, ni Holm, ni seconde course, ni « provisoire » ; présents (texte des règles) : {presents}"

    cas("non-interférence : test_final différente, fichier test inchangé", "artefact", n_final_differente)
    cas("non-interférence : test différente, fichier test_final inchangé", "artefact", n_test_differente)
    cas("non-interférence : anomalie propre à test_final (ligne d'état comprise)", "artefact", n_anomalie_final_seule)
    cas("non-interférence : entrée écartée d'une tâche de test_final", "artefact", n_entree_ecartee_final)
    cas("non-interférence : fichier test de S indépendant de la course M", "artefact", n_seconde_course_absente_du_test)
    cas("mots du fichier test", "artefact", n_mots_du_fichier_test)

    # ------------------------------------------------ courses, noms, lignées, même course
    def a_m_et_m_autre_tentative():
        cm3, _ = fabriquer_course_parts(base, base, *M3, publique, "T-m3", "F-m3", pj_bas, pj)
        s1 = sortie()
        run.lancer(["lecture", cm3, banque, s1, cm], var=var, sortie=s1, code=3, motif="même course")
        return "deux courses M réellement différentes (-tentative2 et -tentative3, archives distinctes) : refus « même course »"

    def a_s_et_s_autre_tentative():
        cs3b, _ = fabriquer_course_parts(base, base / "R5", *S3, publique, "T-s3b", "F-s3b", pj, pj)
        s1 = sortie()
        run.lancer(["lecture", cs, banque, s1, cs3b], var=var, sortie=s1, code=3, motif="même course")
        return "deux courses S différentes : refus « même course »"

    def a_s_lignee_m():
        cx, _ = fabriquer_course_parts(base, base / "R6", S[0], M[1], publique, "T-x", "F-x", pj, pj)
        s1 = sortie()
        run.lancer(["lecture", cx, banque, s1], var=var, sortie=s1, code=3, motif="n'est pas celle de la course nommée")
        return "dossier S dont l'archive porte la lignée de M : refus"

    def a_noms_refuses():
        for nom in ("pilote4-gemini-v5-3-v1", "pilote4-gemini-v6-2-s-v1-tentative0", "pilote4-gemini-v6-2-s-v2", "pilote4-gemini-v6-2-v1.copie"):
            d = base / "noms" / nom
            shutil.copytree(cm, d)
            s1 = sortie()
            run.lancer(["lecture", d, banque, s1], var=var, sortie=s1, code=3, motif="nom du dossier de course inattendu")
        return "dossiers v5-3, -tentative0, s-v2, nom à point : refus"

    def a_lisezmoi_commandes():
        """LISEZMOI v2 § 5, lignes 113, 121, 132 et 140, lancées telles qu'écrites (python3 → l'interpréteur essayé),
        dans le dossier de la copie du script."""
        racine_r = base / "R"
        sm, ss, sm2 = sortie(), sortie(), sortie()
        cmds = [f"{python} -I -B lire_pilote4_v2.py essai-banque {banque}",
                f"{python} -I -B lire_pilote4_v2.py lecture {racine_r}/pilotes/pilote4-gemini-v6-2-v1-tentative2 {banque} {sm}",
                f"{python} -I -B lire_pilote4_v2.py lecture {racine_r}/pilotes/pilote4-gemini-v6-2-s-v1 {banque} {ss} {racine_r}/pilotes/pilote4-gemini-v6-2-v1-tentative2",
                f"{python} -I -B lire_pilote4_v2.py lecture {racine_r}/pilotes/pilote4-gemini-v6-2-v1-tentative2 {banque} {sm2} --sans-seconde-course"]
        avant = {n: A.hf(A.COPIE / n) for n in os.listdir(A.COPIE) if (A.COPIE / n).is_file()}
        env = {k: v for k, v in os.environ.items() if k != A.VAR}
        env[A.VAR] = var
        sorties_ = []
        for c in cmds:
            r = subprocess.run(["bash", "-c", c], cwd=A.COPIE, env=env, capture_output=True, text=True)
            verifier(r.returncode == 0 and A.DECIMAL.search(r.stdout) is None, f"{c} : {r.returncode} {r.stderr[-200:]}")
            sorties_.append(r.stdout.strip())
        verifier(sorties_[0].startswith("essai-banque : catégorie absente du train — test 8 (evaluation 4, usage-reel 4) ; "
                                       "test_final 14 (evaluation 10, usage-reel 4) ; issue : conforme"), sorties_[0])
        verifier({n: A.hf(A.COPIE / n) for n in os.listdir(A.COPIE) if (A.COPIE / n).is_file()} == avant
                 and not [n for n in os.listdir(A.COPIE) if n.startswith(("lecture-", "__pycache__"))], "copie modifiée")
        noms = [sorted(os.listdir(x)) for x in (sm, ss, sm2)]
        verifier(noms[0][0].startswith("lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-provisoire-v2")
                 and any("pilote4-gemini-v6-2-s-v1-test-final-holm-quatre-v2" in x for x in noms[1])
                 and any("tentative2-test-final-holm-deux-v2" in x for x in noms[2]), f"{noms}")
        return "les quatre commandes du § 5 (essai-banque, fin de M, fin de S avec M, Holm sur deux) passent telles qu'écrites, avec -I -B ; noms de sortie conformes ; copie du script intacte"

    def a_tar_coupe_avant_dernier_necessaire():
        def couper(brut):
            noms = [f"course/archive/{M[1]}/g{g:03d}/juge/{f}" for g in (0, 1, 2, 3)
                    for f in ("reponses-lues.json", "score.json", "score-final.json")]
            return bytes(brut[:max(A.entete(brut, n) for n in noms)])
        d, _ = A.fabriquer_course(base / "coupe", *M, publique, "g", A.profil_v62, espace_bizarre=False,
                                  apres_tar=lambda a: A.reecrire_tar(a, couper))
        s1 = sortie()
        r, sout, serr = run.lancer(["lecture", d, banque, s1], var=var, sortie=s1, code=3, motif="fin d'archive absente")
        return f"tar coupé net avant le dernier membre nécessaire (cas accepté par la v1, RSL-03) : refus — « {serr.strip().splitlines()[-1][:110]} »"

    def a_recursion_ligne_du_script():
        def imbriquer(pilote, dl, espace):
            p = dl / "g000" / "juge" / "score-final.json"
            p.write_text('{"par_famille": ' + "[" * 200000 + "]" * 200000 + "}", encoding="utf-8")
            A.sceller(p)
        d, _ = A.fabriquer_course(base / "recursion", *M, publique, "g", A.profil_v62, espace_bizarre=False, avant_tar=imbriquer)
        s1 = sortie()
        r, sout, serr = run.lancer(["lecture", d, banque, s1], var=var, sortie=s1, code=4, motif="ERREUR INTERNE : RecursionError")
        n = int(re.search(r"ligne ([0-9]+) du script", serr).group(1))
        ligne = A.SCRIPT.read_text(encoding="utf-8").splitlines()[n - 1]
        verifier("json.loads" in ligne and "Traceback" not in serr, f"ligne {n} : {ligne!r}")
        return f"score-final.json imbriqué 200 000 fois : code 4, ligne {n} du script (« {ligne.strip()[:60]} »), rien d'écrit (RSL-10)"

    cas("tar coupé net avant le dernier membre nécessaire", "artefact", a_tar_coupe_avant_dernier_necessaire)
    cas("récursion du décodeur JSON : ligne rapportée", "artefact", a_recursion_ligne_du_script)
    cas("deux courses M distinctes (tentatives 2 et 3)", "artefact", a_m_et_m_autre_tentative)
    cas("deux courses S distinctes", "artefact", a_s_et_s_autre_tentative)
    cas("dossier S à la lignée de M", "artefact", a_s_lignee_m)
    cas("noms de dossier refusés (v5-3, tentative0, s-v2, point)", "artefact", a_noms_refuses)
    cas("commandes du LISEZMOI v2 § 5 telles qu'écrites", "sain", a_lisezmoi_commandes)

    # ------------------------------------------------ pannes injectées dans le processus du script (harnais seulement)
    if en_processus:
        def charger_module():
            sp = importlib.util.spec_from_file_location("lire_v2_en_processus", A.SCRIPT)
            L = importlib.util.module_from_spec(sp)
            sp.loader.exec_module(L)
            return L

        def p_sans_liens_durs_et_ecriture_cassee():
            L = charger_module()
            s = sortie()
            vrai_link, vrai_open = os.link, builtins.open
            compte = {"x": 0}

            def link(*a, **k):
                raise OSError(errno.EPERM, "liens durs refusés (simulé)")

            class Fichier(io.RawIOBase):
                pass

            def ouvrir(fichier, mode="r", *a, **k):
                f = vrai_open(fichier, mode, *a, **k)
                nom = os.path.basename(str(fichier))
                if mode == "xb" and nom.startswith("lecture-") and not nom.startswith("."):
                    compte["x"] += 1
                    if compte["x"] == 3:  # troisième fichier définitif écrit directement : panne d'écriture
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
            os.environ[A.VAR] = var
            L.os.link = link
            L.open = ouvrir
            try:
                code = L.principal(["lecture", str(cm), str(banque), str(s)])
            finally:
                L.os.link = vrai_link
                del L.open
                os.environ.pop(A.VAR, None)
            restes = sorted(os.listdir(s)) if s.exists() else []
            if restes:
                CONSTATS.append(("écriture sans liens durs", f"code {code}, restes {restes}"))
            verifier(not restes, f"jeu partiel laissé (code {code}) : {restes}")
            return f"liens durs refusés et panne au troisième fichier : code {code}, SORTIE vide"

        def p_interruption_apres_ecriture():
            L = charger_module()
            s = sortie()
            vrai_print = builtins.print

            def imprimer(*a, **k):
                if a and str(a[0]).startswith("lecture écrite"):
                    raise KeyboardInterrupt
                return vrai_print(*a, **k)
            os.environ[A.VAR] = var
            L.print = imprimer
            tampon = io.StringIO()
            vrai_stdout = sys.stdout
            sys.stdout = tampon
            try:
                code = L.principal(["lecture", str(cm), str(banque), str(s)])
            finally:
                sys.stdout = vrai_stdout
                del L.print
                os.environ.pop(A.VAR, None)
            restes = sorted(x for x in os.listdir(s) if not x.startswith("."))
            dit = tampon.getvalue().strip()
            CONSTATS.append(("interruption après écriture", f"code {code}, sortie « {dit} », fichiers {len(restes)}"))
            return (f"OBSERVATION : interruption injectée juste après l'écriture : code {code}, sortie standard « {dit} », "
                    f"{len(restes)} fichiers définitifs présents dans SORTIE")

        cas("écriture sans liens durs avec panne d'écriture (RSL-16)", "artefact", p_sans_liens_durs_et_ecriture_cassee)
        cas("interruption juste après l'écriture des fichiers (RSL-12)", "observation", p_interruption_apres_ecriture)


def principal():
    p = argparse.ArgumentParser()
    p.add_argument("--python", required=True)
    p.add_argument("--en-processus", action="store_true")
    p.add_argument("--garder", action="store_true")
    a = p.parse_args()
    version = subprocess.run([a.python, "-I", "-c", "import platform; print(platform.python_version())"],
                             capture_output=True, text=True, check=True).stdout.strip()
    print(f"# seconde relecture — artefacts — début {A.heure()} (UTC)")
    print(f"# script relu {A.SCRIPT} {A.hf(A.SCRIPT)} ; exécuté par {a.python} (Python {version}) ; harnais {sys.executable}")
    print(f"# ce harnais {A.hf(__file__)} ; fabrication reprise {A.hf(OUTILS / 'artefacts_relecture_v1_repris.py')} ; trace {A.hf(A.TRACE)}")
    base = R2 / f"travail-v2-py{version}-{os.getpid()}"
    base.mkdir()
    t0 = time.time()
    try:
        lancer(base, a.python, a.en_processus)
    finally:
        if not a.garder:
            shutil.rmtree(base)
    caches = [pathlib.Path(A.NOYAU) / "essaim_m3" / "__pycache__", pathlib.Path(A.NOYAU) / "essaim_m3" / "noyau" / "__pycache__"]
    ok_caches = not any(c.exists() for c in caches)
    print(f"{'OK    ' if ok_caches else 'ÉCHEC '} [contrôle] aucun cache écrit dans le noyau importé : {ok_caches}")
    for k, v in CONSTATS:
        print(f"# constaté — {k} : {v}")
    for genre in ("sain", "artefact", "observation"):
        x = [r for r in RESULTATS if r[1] == genre]
        print(f"# {genre} : {sum(r[2] for r in x)} sur {len(x)} conformes")
    print(f"# bilan ; durée {int(time.time() - t0)} s ; fin {A.heure()} (UTC)")
    return 0 if all(r[2] for r in RESULTATS) and ok_caches else 1


if __name__ == "__main__":
    sys.exit(principal())
