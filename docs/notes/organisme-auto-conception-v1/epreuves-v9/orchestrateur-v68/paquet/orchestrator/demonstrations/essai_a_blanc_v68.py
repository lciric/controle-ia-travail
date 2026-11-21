"""Essai à blanc de bout en bout de la v68 (fichier neuf, R12) — moteur simulé seulement, aucun appel, aucune dépense, aucune clé.

Écrit une configuration d'essai (fiches avec un champ `test_de_mort` à bloc `statistique`, étage de tests de mort v5 avec
l'exécuteur factice, tranche d'essai : `essais/aides_v68.py`), puis lance le lanceur `demonstrations/ideation_v68.py` dans des
processus à part (`python -I -B`, environnement réduit à la liste blanche de la machine jetable, `TMPDIR` dans la sortie) :

| nom | interrupteurs | attendu |
|---|---|---|
| verifier-eteint, verifier-tests-de-mort, verifier-lecture | `--verifier-seulement` | code 0, montant requis par régime, aucune écriture |
| verifier-sans-etage | configuration sans étage, `--verifier-seulement` | code 0 ; interrupteurs « éteints » ; 2 × S17 |
| eteint-sans-etage | **interrupteurs éteints** : configuration sans étage, deux générations | code 0 ; ni étage ni héritage |
| eteint | aucun interrupteur de la v68 (deux générations, étage entre elles : tests de mort allumés au sens du lanceur v10) | code 0 ; rien servi ; sélection scellée jamais servie |
| tests-de-mort-sans-rien-servir | `--etage-apres-derniere` | code 0 ; un étage après chaque génération ; rien servi |
| lecture-de-la-selection | `--lecture-selection oui` | code 0 ; la génération 2 reçoit nom et énoncé des retenues |
| plafond-de-course | `--etage-apres-derniere --plafond-course-usd 50.5` | code 2 ; arrêt avant la génération 2 |
| moteur-reel-refuse | `--lecture-selection oui --moteur reel` | code 2 ; GO nominatif exigé, refus avant toute écriture |
| moteur-reel-eteint-refuse | configuration sans étage, `--moteur reel` | code 2 ; refusé par construction |
| temoin-v59 | lanceur `ideation_v59.py`, deux générations | code 2 ; `JSONDecodeError` (le défaut épinglé au rang 0) |

Puis un résumé par comptes (`verse/resume-essai-a-blanc-v68.json`) et une vérification à part : la section servie à la génération
2 (empreinte au bilan) est recalculée depuis les fichiers scellés de l'étage de la génération 1 (sélection, fiches).

  python -I -B demonstrations/essai_a_blanc_v68.py SORTIE_NEUVE
"""

import hashlib
import json
import os
import platform
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)
sys.path.insert(0, os.path.join(RACINE, "essais"))
sys.dont_write_bytecode = True

import aides_v68 as A  # noqa: E402
from pole.budget_course_v68 import rejouer_journal_course_v68  # noqa: E402
from pole.course2_v68 import TITRE_HERITAGE_SELECTION  # noqa: E402

FICHIERS_V68 = ("pole/configuration_v68.py", "pole/budget_course_v68.py", "pole/course2_v68.py", "pole/simulation_v68.py",
                "demonstrations/ideation_v68.py", "demonstrations/essai_a_blanc_v68.py", "essais/aides_v68.py",
                "essais/test_v68_course2.py")


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def lancer(sortie, nom, lanceur, args, env):
    debut = time.time()
    p = subprocess.run([sys.executable, "-I", "-B", os.path.join(ICI, lanceur)] + args, env=env, cwd=sortie,
                       capture_output=True, text=True, timeout=1800)
    j = os.path.join(sortie, "verse", "journaux")
    for flux, texte in (("stdout", p.stdout), ("stderr", p.stderr)):
        with open(os.path.join(j, f"{nom}.{flux}.txt"), "w", encoding="utf-8") as f:
            f.write(texte)
    return {"nom": nom, "lanceur": lanceur, "arguments": args, "code": p.returncode, "duree_s": round(time.time() - debut, 1),
            "stdout_sha256": hashlib.sha256(p.stdout.encode()).hexdigest(), "stderr_sha256": hashlib.sha256(p.stderr.encode()).hexdigest(),
            "arret": (json.loads(p.stderr.strip().splitlines()[-1]).get("arret", "")[:400] if p.returncode and p.stderr.strip() else None)}


def comptes_course(dossier):
    chemin = os.path.join(dossier, "bilan-course.json")
    if not os.path.exists(chemin):
        return None
    with open(chemin, encoding="utf-8") as f:
        b = json.load(f)
    gens = []
    for l in b["generations"]:
        g = {"generation": l["generation"], "fiches_classees": l["fiches_classees"], "notables": l["notables"],
             "cout_generation_usd": l["cout_generation_usd"], "heritage_lu": None, "etage": None}
        h = l.get("heritage_lu")
        if h:
            g["heritage_lu"] = {k: h[k] for k in ("selection_sha256", "depuis_generation", "retenues", "servies", "section",
                                                  "texte_sha256", "consignes_avec_section")} | {"exclues_a4": len(h["exclues_a4"])}
        if "etage" in l:
            e = l["etage"]
            g["etage"] = {"candidates": len(e["candidates"]), "comptes": e["comptes"], "refusees_a_l_etage": e["refusees_a_l_etage"],
                          "cout_etage_usd": l.get("cout_etage_usd"), "selection": l["selection"],
                          "heritage_servi_a_la_suivante": l["heritage_servi_a_la_suivante"] is not None}
        gens.append(g)
    bc = b["budget_course"]
    return {"version": b["version"], "regime": b["regime"]["nom"], "arret": b["arret"], "noeud": b["noeud"], "generations": gens,
            "budget_course": {"plafond_course_usd": bc["plafond_course_usd"], "cumul_usd": bc["cumul_usd"],
                              "postes": [(j["quoi"], j["poste"]) for j in bc["journal"]],
                              "rejeu_du_journal_usd": rejouer_journal_course_v68(bc)},
            "bilan_sha256": sha256(chemin)}


def principal(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 1:
        print("usage : essai_a_blanc_v68.py SORTIE_NEUVE", file=sys.stderr)
        return 2
    sortie = os.path.abspath(argv[0])
    if os.path.exists(sortie):
        print(f"sortie {sortie} déjà présente (R12)", file=sys.stderr)
        return 2
    for d in ("pieces", "tmp", "courses", os.path.join("verse", "journaux"), os.path.join("verse", "bilans")):
        os.makedirs(os.path.join(sortie, d))
    conf = A.configuration(os.path.join(sortie, "pieces"))
    ch = A.ecrire_configuration(conf, os.path.join(sortie, "pieces", "configuration-essai-v68.json"))
    conf0 = A.configuration(os.path.join(sortie, "pieces"), avec_test=False, etage=False)
    ch0 = A.ecrire_configuration(conf0, os.path.join(sortie, "pieces", "configuration-essai-v68-sans-etage.json"))
    env = {"PATH": "/usr/bin:/bin", "POLE_MACHINE_JETABLE_V56": "1", "TMPDIR": os.path.join(sortie, "tmp"),
           "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    c = lambda nom: os.path.join(sortie, "courses", nom)  # noqa: E731
    plan = [
        ("verifier-eteint", "ideation_v68.py", ["--course-2", ch, c("x"), "--generations", "2", "--verifier-seulement"]),
        ("verifier-tests-de-mort", "ideation_v68.py", ["--course-2", ch, c("x"), "--generations", "2", "--etage-apres-derniere",
                                                       "--verifier-seulement"]),
        ("verifier-lecture", "ideation_v68.py", ["--course-2", ch, c("x"), "--generations", "2", "--lecture-selection", "oui",
                                                 "--verifier-seulement"]),
        ("verifier-sans-etage", "ideation_v68.py", ["--course-2", ch0, c("x"), "--generations", "2", "--verifier-seulement"]),
        ("eteint-sans-etage", "ideation_v68.py", ["--course-2", ch0, c("eteint-sans-etage"), "--generations", "2", "--moteur",
                                                  "simule"]),
        ("eteint", "ideation_v68.py", ["--course-2", ch, c("eteint"), "--generations", "2", "--moteur", "simule"]),
        ("tests-de-mort-sans-rien-servir", "ideation_v68.py", ["--course-2", ch, c("tests-de-mort-sans-rien-servir"), "--generations",
                                                               "2", "--etage-apres-derniere", "--moteur", "simule"]),
        ("lecture-de-la-selection", "ideation_v68.py", ["--course-2", ch, c("lecture-de-la-selection"), "--generations", "2",
                                                        "--lecture-selection", "oui", "--moteur", "simule"]),
        ("plafond-de-course", "ideation_v68.py", ["--course-2", ch, c("plafond-de-course"), "--generations", "2",
                                                  "--etage-apres-derniere", "--plafond-course-usd", "50.5", "--moteur", "simule"]),
        ("moteur-reel-refuse", "ideation_v68.py", ["--course-2", ch, c("moteur-reel-refuse"), "--generations", "2",
                                                   "--lecture-selection", "oui", "--moteur", "reel", "--confirmer-moteur-reel"]),
        ("moteur-reel-eteint-refuse", "ideation_v68.py", ["--course-2", ch0, c("moteur-reel-eteint-refuse"), "--generations",
                                                          "1", "--moteur", "reel", "--confirmer-moteur-reel"]),
        ("temoin-v59", "ideation_v59.py", ["--course-2", ch, c("temoin-v59"), "--generations", "2", "--moteur", "simule"]),
    ]
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    lancements = [lancer(sortie, nom, l, a, env) for nom, l, a in plan]
    courses = {}
    for nom in ("eteint-sans-etage", "eteint", "tests-de-mort-sans-rien-servir", "lecture-de-la-selection", "plafond-de-course",
                "temoin-v59"):
        d = c(nom)
        if nom == "temoin-v59":
            p = os.path.join(d, "bilan-course.json")
            if os.path.exists(p):
                with open(p, encoding="utf-8") as f:
                    b = json.load(f)
                courses[nom] = {"version": b["version"], "arret": b["arret"], "generations_au_bilan": len(b["generations"]),
                                "generation_2_commencee": os.path.isdir(os.path.join(d, "generation-2")),
                                "retenues_generation_1": len(b["generations"][0].get("etage", {}).get("selection", {}).get("retenues", []))
                                if b["generations"] else None}
            continue
        courses[nom] = comptes_course(d)
        if courses[nom] is not None:
            with open(os.path.join(d, "bilan-course.json"), "rb") as f, \
                    open(os.path.join(sortie, "verse", "bilans", f"{nom}-bilan-course.json"), "wb") as g:
                g.write(f.read())
    verifs = {}
    lec = courses.get("lecture-de-la-selection")
    if lec:
        _, sha, lignes, exclues = A.section_attendue(os.path.join(c("lecture-de-la-selection"), "etage-apres-generation-1"),
                                                     TITRE_HERITAGE_SELECTION)
        h2 = lec["generations"][1]["heritage_lu"]
        verifs["lecture : section servie à la génération 2 = section recalculée depuis l'étage de la génération 1"] = \
            bool(h2) and h2["texte_sha256"] == sha and h2["section"] == "servie" and h2["servies"] == len(lignes) >= 1
        verifs["lecture : au moins une fiche exclue par l'étage (éliminée), absente de la section"] = len(exclues) >= 1
        verifs["lecture : la sélection lue est celle que l'étage de la génération 1 a scellée"] = \
            bool(h2) and h2["selection_sha256"] == lec["generations"][0]["etage"]["selection"]["sha256"]
    for nom in ("eteint-sans-etage", "eteint", "tests-de-mort-sans-rien-servir"):
        r = courses.get(nom)
        verifs[f"{nom} : aucune génération n'a reçu d'héritage"] = bool(r) and all(g["heritage_lu"] is None for g in r["generations"])
        verifs[f"{nom} : aucune sélection servie"] = bool(r) and all(not (g["etage"] or {}).get("heritage_servi_a_la_suivante")
                                                                     for g in r["generations"])
    t = courses.get("tests-de-mort-sans-rien-servir")
    verifs["tests de mort : un étage après chaque génération, la dernière comprise"] = bool(t) and all(g["etage"] for g in t["generations"])
    z = courses.get("eteint-sans-etage")
    verifs["éteint sans étage : deux générations, aucun étage"] = bool(z) and len(z["generations"]) == 2 and \
        all(g["etage"] is None for g in z["generations"]) and not any(n.startswith("etage-") for n in os.listdir(c("eteint-sans-etage")))
    e = courses.get("eteint")
    verifs["éteint : étage entre les générations seulement"] = bool(e) and e["generations"][0]["etage"] is not None and \
        e["generations"][1]["etage"] is None
    p = courses.get("plafond-de-course")
    verifs["plafond de la course : arrêt avant la génération 2"] = bool(p) and "PlafondDeCourseAtteint" in (p["arret"] or "") and \
        len(p["generations"]) == 1 and not os.path.exists(os.path.join(c("plafond-de-course"), "generation-2"))
    codes = {x["nom"]: x["code"] for x in lancements}
    verifs["codes attendus"] = codes == {"verifier-sans-etage": 0, "eteint-sans-etage": 0, "moteur-reel-eteint-refuse": 2,
                                         "verifier-eteint": 0, "verifier-tests-de-mort": 0, "verifier-lecture": 0, "eteint": 0,
                                         "tests-de-mort-sans-rien-servir": 0, "lecture-de-la-selection": 0, "plafond-de-course": 2,
                                         "moteur-reel-refuse": 2, "temoin-v59": 2}
    verifs["moteur réel : aucune sortie écrite"] = not os.path.exists(c("moteur-reel-refuse")) and \
        not os.path.exists(c("moteur-reel-eteint-refuse"))
    arrets = {x["nom"]: x["arret"] or "" for x in lancements}
    verifs["moteur réel éteint : refusé par construction"] = "refusé par construction" in arrets["moteur-reel-eteint-refuse"]
    verifs["moteur réel allumé : ligne de GO nominative exigée"] = "--registre-go exigé" in arrets["moteur-reel-refuse"]
    verifs["témoin v59 : JSONDecodeError à la génération 2"] = "JSONDecodeError" in ((courses.get("temoin-v59") or {}).get("arret") or "")
    montants = {}
    for nom in ("verifier-sans-etage", "verifier-eteint", "verifier-tests-de-mort", "verifier-lecture"):
        with open(os.path.join(sortie, "verse", "journaux", f"{nom}.stdout.txt"), encoding="utf-8") as f:
            o = json.loads(f.read())
        montants[nom] = {"regime": o["regime"]["nom"], "montant_requis_go_usd": o["montant_requis_go_usd"],
                         "nombre_etages": o["regime"]["nombre_etages"], "interrupteurs": o["interrupteurs"]}
    resume = {"version": "essai-a-blanc-v68-v1", "debut_utc": debut, "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "moteur": "simulé (aucun appel, aucune dépense, aucune clé) ; étage : exécuteur factice (aucune barrière)",
              "python": platform.python_version(), "configuration_sha256": sha256(ch),
              "configuration_sans_etage_sha256": sha256(ch0),
              "fichiers_v68": {f: sha256(os.path.join(RACINE, f)) for f in FICHIERS_V68},
              "environnement_des_lancements": sorted(env), "lancements": lancements, "montants": montants, "courses": courses,
              "verifications": verifs, "toutes_vraies": all(verifs.values())}
    with open(os.path.join(sortie, "verse", "resume-essai-a-blanc-v68.json"), "w", encoding="utf-8") as f:
        json.dump(resume, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"toutes_vraies": resume["toutes_vraies"], "verifications": verifs}, ensure_ascii=False, indent=1))
    return 0 if resume["toutes_vraies"] else 1


if __name__ == "__main__":
    raise SystemExit(principal())
