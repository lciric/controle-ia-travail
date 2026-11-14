#!/usr/bin/env python3
"""Banc de mutations du lanceur `lancer_course_ideation_regard_ou_raisons_v1.py` — version 1.

Adapté du banc du lanceur « conception propre » (`docs/notes/organisme-conception-propre-v1/outils/
mutations_lanceur_conception_propre_v1.py`, `cbb574d1…`) par le préparateur de la course « Regard ou raisons ». Trois séries :

- **X** : les vingt-cinq mutants du préparateur précédent (X18 adapté : il n'y a plus de réserve du lecteur, le mutant
  oublie le plafond de la course dans la garde de cumul) ;
- **Y** : les vingt-huit mutations que la contre-lecture précédente avait faites à la main (`contre-lecture-lanceur-
  conception-propre-v1.md`, § « Essais et mutations »), réécrites ici d'après leur description : les vingt-trois tuées,
  les trois lacunes d'essai (m4) et les deux « équivalentes », pour lesquelles les essais de cette course ont un cas neuf ;
- **Z** : huit mutants sur ce que ce lanceur change (périmètre de la ligne de GO, pire cas, borne, graine, pièces, bilan de
  l'organisme, dossier de runs, conseil d'arrêt).

Aucun modèle, aucun réseau. Le dépôt n'est pas touché : chaque mutant est une copie du lanceur (avec son compagnon
`.sha256`, recalculé : sinon tout mutant serait « tué » par l'essai du compagnon) écrite dans le dossier de travail, et la
suite des essais est une copie de `tests/test_lancer_course_ideation_regard_ou_raisons_v1.py` où trois lignes seulement
changent : `RACINE` (dépôt réel), `SCRIPT` (le mutant), `lc.DEPOT = RACINE` après le chargement. Le cas « base » (aucune
mutation) doit rendre tous les essais passés : c'est le contrôle de l'outil. Un mutant est « tué » si au moins un essai
échoue (arrêt au premier échec, `-x`, sauf pour la base). Les mutants tournent par quatre à la fois (dossiers de travail
séparés ; l'ordre du résultat est celui de la liste).

Usage : <python avec pytest> -B mutations_lanceur_regard_ou_raisons_v1.py DOSSIER_DE_TRAVAIL_NEUF [nom,nom,…]
Sortie : un objet JSON (par mutant : tué ou survivant, premier essai en échec).
"""
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
NOM = "lancer_course_ideation_regard_ou_raisons_v1"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"
EN_PARALLELE = 4

# (nom, garde visée, texte d'origine — une seule occurrence exigée —, texte muté)
MUTATIONS = [
    ("base", "aucune (contrôle de l'outil)", None, None),
    # ------------------------------------------------------------------------------------------ X : préparateur précédent
    ("X01-option-I", "M1 : -I", '    if not getattr(r.drapeaux, "isolated", 0):', "    if False:"),
    ("X02-option-B", "M1 : -B", '    if not getattr(r.drapeaux, "dont_write_bytecode", 0):', "    if False:"),
    ("X03-commande-d-origine", "M1 : commande exacte", "    if tuple(r.orig_argv) != commande_exacte(r):", "    if False:"),
    ("X04-dossier-courant", "M1 : dossier courant", "    if os.path.realpath(r.cwd) != os.path.realpath(r.depot):",
     "    if False:"),
    ("X05-empreinte-propre", "M1 : empreinte = compagnon",
     '    if lue != attendue:\n        raise Refus(f"empreinte du lanceur', '    if False:\n        raise Refus(f"empreinte du lanceur'),
    ("X06-lien-symbolique", "M1 : lien symbolique", "    if f.is_symlink() or not f.is_file():", "    if not f.is_file():"),
    ("X07-git-apres-detachement", "M2 : git après le détachement",
     '{"pre_depart_sha256": h_pre, "superviseur": sup, "lanceur": {"version": VERSION}}',
     '{"pre_depart_sha256": h_pre, "superviseur": sup, "lanceur": {"version": VERSION}, "git": _depot_git(r)}'),
    ("X08-depart-non-garde", "M2 : PID imprimé si le départ n'est pas écrit",
     '    except BaseException as e:  # noqa: BLE001\n        print(json.dumps({"etat": "COURSE LANCÉE',
     '    except ZeroDivisionError as e:  # noqa: BLE001\n        print(json.dumps({"etat": "COURSE LANCÉE'),
    ("X09-superviseur-sans-pid", "M2 : le superviseur scelle son PID",
     'sceller("pid-superviseur.json", {"pid_superviseur": os.getpid(), "debut_proc": debut_de(os.getpid()), "debut_utc": debut})',
     "pass"),
    ("X10-detachement-incertain-refus", "M2 : jamais de refus si le superviseur a peut-être démarré",
     '        if detachement_tente and (dossier_sortie / SUPERVISEUR_DOSSIER / "superviseur.stdout.txt").exists():',
     "        if False:"),
    ("X11-copies-absentes", "B1 : copies des preuves dans le dépôt", "        copies = copier_preuves(run, sup)",
     "        copies = {}"),
    ("X12-releve-non-lie-a-la-fin", "B1 : relevé lié au manifeste de fin",
     '        if run["fin"].get("releve_sha256") != sha256_fichier(run["dossier"] / "releve-depense.json"):',
     "        if False:"),
    ("X13-copie-non-verifiee", "B1 : copie idempotente vérifiée",
     "        if hashlib.sha256(lire_scelle(dest)).hexdigest() != h:", "        if False:"),
    ("X14-relance-apres-fiches", "R3 : jamais après des fiches", '        if rel["fiches_produites"] is not False:',
     '        if rel["fiches_produites"] is True and False:'),
    ("X15-courses-non-bornees", "une seule relance au total", "    if len(lances) >= MAX_COURSES:",
     "    if len(lances) >= 30:"),
    ("X16-relance-depense-illisible", "relance après dépense illisible",
     '        if not rel["lisible"]:\n            return False, f"course {x[\'nom\']} : dépense illisible',
     '        if False:\n            return False, f"course {x[\'nom\']} : dépense illisible'),
    ("X17-borne-du-lanceur-retiree", "borne du lanceur (pire cas, 17 USD)", "    borne = min(BORNE_LIGNE_USD, plafond_go)",
     "    borne = plafond_go"),
    ("X18-plafond-de-course-oublie-au-cumul", "plafond de la course au cumul (adapté : plus de réserve du lecteur)",
     "    suivant = PLAFOND_COURSE_USD                     # aucun lecteur", "    suivant = 0.0                     # aucun lecteur"),
    ("X19-go-sous-le-pire-cas", "GO au moins au pire cas du devis", "    if plafond_usd < PIRE_CAS_DEVIS_USD:", "    if False:"),
    ("X20-go-perimetre-ignore", "GO trouvé par son périmètre", "all(p in _normal(c[3]) for p in PERIMETRE_GO)", "True"),
    ("X21-arbre-non-verifie", "arbre de l'orchestrateur", "    if arbre != r.arbre_orchestrateur:", "    if False:"),
    ("X22-environnement-entier", "environnement par liste de noms",
     "    garde = {n: env[n] for n in env if n in NOMS_PERMIS or (prefixe_essais and n.startswith(prefixe_essais))}",
     "    garde = {n: env[n] for n in env}"),
    ("X23-verrou-retire", "verrou d'invocation", "        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)", "        pass"),
    ("X24-orphelin-ignore", "orchestrateur orphelin", "    if orphs:", "    if False:"),
    ("X25-zombie-vivant", "zombie tenu pour vivant", '    if len(champs) < 20 or champs[0] == "Z":',
     "    if len(champs) < 20:"),
    # ------------------------------------------------------------------------- Y : contre-lecture précédente, les 23 tuées
    ("Y01-argument-unique", "argument unique", "    if argv != [ARGUMENT]:", "    if False:"),
    ("Y02-revocation", "ligne de GO révoquée", '            if _sans_accent(cellules[2]) == "revocation":',
     "            if False:"),
    ("Y03-accordant", "GO accordé par Lazar", '    if par != "Lazar":', "    if False:"),
    ("Y04-periode", "période de validité du GO", "    if not d_acc <= aujourd_hui <= d_ech:", "    if False:"),
    ("Y05-deux-lignes-de-go", "une seule ligne de GO", "    if len(candidates) != 1:", "    if len(candidates) < 1:"),
    ("Y06-exposition-de-la-course", "exposition de la course ≤ plafond de la course",
     '    if s["total_claude"] + s["exposition_externe_course"] > PLAFOND_COURSE_USD + 1e-9:', "    if False:"),
    ("Y07-nom-d-hote-transmis", "adresse d'hôte jamais transmise",
     "    garde = {n: env[n] for n in env if n in NOMS_PERMIS or (prefixe_essais and n.startswith(prefixe_essais))}",
     '    garde = {n: env[n] for n in env if n in NOMS_PERMIS or n == "ANTHROPIC_BASE_URL" '
     "or (prefixe_essais and n.startswith(prefixe_essais))}"),
    ("Y08-garde-des-drapeaux", "drapeaux interdits", "    garde_drapeaux(argv)\n    sommes = garde_sommes(argv)\n",
     "    sommes = garde_sommes(argv)\n"),
    ("Y09-fiches-illisibles", "fiches illisibles tenues pour produites",
     "    if any(not isinstance(x, list) for x in listes):\n        return None\n",
     "    if any(not isinstance(x, list) for x in listes):\n        return False\n"),
    ("Y10-superviseur-tenu-pour-fini", "fin propre prouvée par le code scellé", "        sup_fini = code is not None\n",
     "        sup_fini = True\n"),
    ("Y11-signal-non-relaye", "signaux relayés par PID", "            enfant.send_signal(num)\n", "            pass\n"),
    ("Y12-pid-reutilise", "PID réutilisé (heure de départ du processus)",
     '        and debut_processus(sup["pid"]) == sup["debut_proc"]\n', "        and True\n"),
    ("Y13-session-non-neuve", "session de processus neuve", "stdin=subprocess.DEVNULL, start_new_session=True)",
     "stdin=subprocess.DEVNULL, start_new_session=False)"),
    ("Y14-run-sans-manifeste", "run sans manifeste : état inconnu", "        if pre is None and refus is None:\n",
     "        if False:\n"),
    ("Y15-orphelin-a-la-cloture", "orphelin dit à la clôture",
     "        orphelin = orchestrateur_orphelin(sup) if code is None else None\n", "        orphelin = None\n"),
    ("Y16-fichiers-ignores-du-clone", "clone sans fichiers ignorés", "    if ignores:\n", "    if False:\n"),
    ("Y17-identifiant-de-go-transmis", "identifiant de GO transmis", '    garde["GO_ID"] = go_id\n',
     '    garde["GO_ID"] = "GO-0000-00-00-00"\n'),
    ("Y18-garde-de-cumul", "garde de cumul", "    if deja + suivant > borne + 1e-9:\n", "    if False:\n"),
    ("Y19-relance-sans-code-scelle", "relance seulement après un code scellé",
     '        if x["fin"] is None or x["fin"].get("code") is None:\n', '        if x["fin"] is None:\n'),
    ("Y20-total-claude-transmis", "total Claude transmis = devis", '"--budget-total-usd", _usd(TOTAL_CLAUDE_USD)',
     '"--budget-total-usd", _usd(TOTAL_CLAUDE_USD + 30.0)'),
    ("Y21-superviseur-inconnu", "superviseur sans PID scellé : nœud", "    if inconnus:\n", "    if False:\n"),
    ("Y22-course-partie-comptee-rien", "course non close : plafond compté",
     '        return {"run": run["nom"], "course_usd": PLAFOND_COURSE_USD, "lisible": False, "fiches_produites": None,\n'
     '                "lecture": "course non close : plafond entier compté"}\n',
     '        return {"run": run["nom"], "course_usd": 0.0, "lisible": True, "fiches_produites": False,\n'
     '                "lecture": "course non close : plafond entier compté"}\n'),
    ("Y23-tentative-non-scellee", "contrôle sans tentative scellée : plafond",
     '        if m and (controle / nom).is_dir() and m.group(1) not in scellees:\n', "        if False:\n"),
    # ------------------------------------------- Y : les trois lacunes d'essai (m4) et les deux « équivalentes », essais neufs
    ("Y24-sortie-sans-manifeste-de-fin", "m4 : sortie sans manifeste de fin → plafond",
     '    if sortie.exists():\n        return PLAFOND_COURSE_USD, False, "sortie sans manifeste de fin scellé',
     '    if False:\n        return PLAFOND_COURSE_USD, False, "sortie sans manifeste de fin scellé'),
    ("Y25-pieces-hors-liste-blanche", "m4 : enveloppe et commande d'Argon vérifiées par empreinte",
     '        if lu != attendu:\n            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}\n',
     '        if lu != attendu and nom in ("question", "faits", "temoins"):\n'
     '            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}\n'),
    ("Y26-bac-inactif", "m4 : bac à sable inactif", '    if not etat["actif"]:\n', "    if False:\n"),
    ("Y27-releve-illisible-non-remonte", "relevé illisible remonté au plafond (« équivalente » de la contre-lecture)",
     '        if not out["lisible"]:\n            out["course_usd"] = max(out["course_usd"], PLAFOND_COURSE_USD)\n',
     '        if False:\n            out["course_usd"] = max(out["course_usd"], PLAFOND_COURSE_USD)\n'),
    ("Y28-nom-de-cle-retire", "liste des noms de clé (« équivalente » de la contre-lecture)",
     '"HF_TOKEN",\n               "KIMI_API_KEY")', '"HF_TOKEN")'),
    # ----------------------------------------------------------------------------------------- Z : ce que ce lanceur change
    ("Z01-perimetre-une-expression-suffit", "périmètre : les deux expressions exigées",
     "all(p in _normal(c[3]) for p in PERIMETRE_GO)", "any(p in _normal(c[3]) for p in PERIMETRE_GO)"),
    ("Z02-pire-cas-abaisse", "pire cas du devis (17 USD)", "PIRE_CAS_DEVIS_USD = 17.0 ", "PIRE_CAS_DEVIS_USD = 14.9 "),
    ("Z03-borne-de-l-ancienne-course", "borne du lanceur (17 USD, non 25)", "BORNE_LIGNE_USD = 17.0 ", "BORNE_LIGNE_USD = 25.0 "),
    ("Z04-graine-de-l-ancienne-course", "graine propre à cette course", "GRAINE = 2026111402\n", "GRAINE = 2026111401\n"),
    ("Z05-faits-d-une-autre-question", "pièces de cette question",
     '    "faits": (f"{NOTES_QUESTION}/faits-v1.md",\n'
     '              "8708619040b1483a97d33bd5dc3576d083656a3a7c29a8b273b0944e964e6642"),\n',
     '    "faits": ("docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md",\n'
     '              "d19b540015ed9480774c020cd7f1a527db32d42600a5bc2bd34c92c17d7be0b3"),\n'),
    ("Z06-bilan-non-designe", "bilan de l'organisme au manifeste de fin",
     '        if code and code["code"] == 0 and "sortie/fiches-validees.json" in copies:\n', "        if False:\n"),
    ("Z07-runs-de-l-ancienne-course", "dossier de runs propre à cette course",
     'SOUS_DOSSIER_RUNS = "course-ideation-regard-ou-raisons-v1"\n', 'SOUS_DOSSIER_RUNS = "course-ideation-conception-propre-v1"\n'),
    ("Z08-conseil-d-arret-term-seul", "conseil d'arrêt : INT d'abord (C1)",
     '            "arret": f"kill -INT {p.pid} d\'abord (relayé par PID à l\'orchestrateur, fin propre ; jamais par motif, R10) ; "\n'
     '                     f"kill -TERM {p.pid} seulement si la course ne finit pas"}\n',
     '            "arret": f"kill -TERM {p.pid} (relayé par PID à l\'orchestrateur ; jamais par motif, R10)"}\n'),
]


def jouer(travail, source, essais, lignes, mutation):
    nom, garde, avant, apres = mutation
    l_racine, l_script, l_charge = lignes
    d = travail / nom
    (d / "scripts").mkdir(parents=True)
    (d / "tests").mkdir()
    mutant = source if avant is None else source.replace(avant, apres)
    chemin_mutant = d / "scripts" / f"{NOM}.py"
    chemin_mutant.write_text(mutant, encoding="utf-8")
    Path(str(chemin_mutant) + ".sha256").write_text(
        hashlib.sha256(mutant.encode("utf-8")).hexdigest() + f"  {chemin_mutant.name}\n", encoding="utf-8")
    t = essais.replace(l_racine, f'RACINE = Path("{DEPOT}")\n').replace(
        l_script, f'SCRIPT = Path("{chemin_mutant}")\n').replace(l_charge, l_charge + "lc.DEPOT = RACINE\n")
    chemin_essais = d / "tests" / f"test_{NOM}.py"
    chemin_essais.write_text(t, encoding="utf-8")
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(d), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    options = [] if avant is None else ["-x"]
    p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(d / "pt"),
                        "-rf", "--tb=no", *options, str(chemin_essais)], cwd=str(d), env=env, capture_output=True,
                       text=True, timeout=1800, stdin=subprocess.DEVNULL)
    bilan = [x for x in p.stdout.splitlines() if re.search(r"\d+ (passed|failed)", x)]
    echecs = sorted(re.sub(r"^FAILED \S+::", "", x).split(" - ")[0] for x in p.stdout.splitlines()
                    if x.startswith(("FAILED ", "ERROR ")))
    r = {"mutant": nom, "garde": garde, "code_pytest": p.returncode,
         "bilan": bilan[-1].strip() if bilan else p.stdout[-300:], "essais_en_echec": echecs,
         "issue": ("contrôle : tous passés" if avant is None and p.returncode == 0 else
                   "CONTRÔLE EN ÉCHEC" if avant is None else "tué" if p.returncode != 0 else "SURVIVANT")}
    print(json.dumps(r, ensure_ascii=False), file=sys.stderr, flush=True)
    return r


def main():
    travail = Path(sys.argv[1]).resolve()
    seulement = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    travail.mkdir(parents=True)
    source = LANCEUR.read_text(encoding="utf-8")
    essais = ESSAIS.read_text(encoding="utf-8")
    lignes = ("RACINE = Path(__file__).resolve().parents[1]\n", f'SCRIPT = RACINE / "scripts" / "{NOM}.py"\n',
              "_spec.loader.exec_module(lc)\n")
    for ligne in lignes:
        assert essais.count(ligne) == 1, ligne
    noms = [m[0] for m in MUTATIONS]
    assert len(set(noms)) == len(noms), "noms de mutants en double"
    for nom, _, avant, apres in MUTATIONS:
        if avant is not None and source.count(avant) != 1:
            raise SystemExit(f"{nom} : {source.count(avant)} occurrence(s) du texte d'origine (une exigée)")
        if avant is not None and avant == apres:
            raise SystemExit(f"{nom} : mutation sans effet")
    choisies = [m for m in MUTATIONS if seulement is None or m[0] in seulement]
    with ThreadPoolExecutor(max_workers=EN_PARALLELE) as bassin:
        resultats = list(bassin.map(lambda m: jouer(travail, source, essais, lignes, m), choisies))
    print(json.dumps({"lanceur": str(LANCEUR), "lanceur_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
                      "essais": str(ESSAIS), "essais_sha256": hashlib.sha256(essais.encode("utf-8")).hexdigest(),
                      "mutants_joues": len([r for r in resultats if r["mutant"] != "base"]),
                      "mutants": resultats, "tues": sum(1 for r in resultats if r["issue"] == "tué"),
                      "survivants": [r["mutant"] for r in resultats if r["issue"] == "SURVIVANT"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
