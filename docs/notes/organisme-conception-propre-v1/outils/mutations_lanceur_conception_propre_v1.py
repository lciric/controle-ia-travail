#!/usr/bin/env python3
"""Banc de mutations du lanceur `lancer_course_ideation_conception_propre_v1.py` — version 1.

Adapté de l'outil du lanceur v3 des bassins étroits (`preparateur-outils-v3/mutations_lanceur_v3.py`, `6d7d6c09…`) par le
préparateur de la course « conception propre » : vingt-quatre mutants sur les gardes neuves (M1, M2, preuves dans le dépôt,
relance unique, cumul à 25 USD avec la réserve du lecteur, ligne de GO trouvée par son contenu, arbre de l'orchestrateur) et
sur les gardes reprises du v3. Aucun modèle, aucun réseau. Le dépôt n'est pas touché : chaque mutant est une copie du
lanceur (avec son compagnon `.sha256`, recalculé : sinon tout mutant serait « tué » par l'essai du compagnon) écrite dans le
dossier de travail, et la suite des essais est une copie de `tests/test_lancer_course_ideation_conception_propre_v1.py` où
trois lignes seulement changent : `RACINE` (dépôt réel), `SCRIPT` (le mutant), `lc.DEPOT = RACINE` après le chargement. Le
cas « base » (aucune mutation) doit rendre tous les essais passés : c'est le contrôle de l'outil. Un mutant est « tué » si
au moins un essai échoue (arrêt au premier échec, `-x`, sauf pour la base).

Usage : <python avec pytest> -B mutations_lanceur_conception_propre_v1.py DOSSIER_DE_TRAVAIL_NEUF
Sortie : un objet JSON (par mutant : tué ou survivant, premier essai en échec).
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
NOM = "lancer_course_ideation_conception_propre_v1"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"

# (nom, garde visée, texte d'origine — une seule occurrence exigée —, texte muté)
MUTATIONS = [
    ("base", "aucune (contrôle de l'outil)", None, None),
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
    ("X17-borne-25-retiree", "borne de 25 USD", "    borne = min(BORNE_LIGNE_USD, plafond_go)", "    borne = plafond_go"),
    ("X18-reserve-lecteur-oubliee", "réserve du lecteur au cumul", "    suivant = PLAFOND_COURSE_USD + RESERVE_LECTEUR_USD",
     "    suivant = PLAFOND_COURSE_USD"),
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
]


def main():
    travail = Path(sys.argv[1]).resolve()
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    travail.mkdir(parents=True)
    source = LANCEUR.read_text(encoding="utf-8")
    essais = ESSAIS.read_text(encoding="utf-8")
    l_racine = "RACINE = Path(__file__).resolve().parents[1]\n"
    l_script = f'SCRIPT = RACINE / "scripts" / "{NOM}.py"\n'
    l_charge = "_spec.loader.exec_module(lc)\n"
    for ligne in (l_racine, l_script, l_charge):
        assert essais.count(ligne) == 1, ligne
    resultats = []
    for nom, garde, avant, apres in MUTATIONS:
        d = travail / nom
        (d / "scripts").mkdir(parents=True)
        (d / "tests").mkdir()
        mutant = source
        if avant is not None:
            if source.count(avant) != 1:
                raise SystemExit(f"{nom} : {source.count(avant)} occurrence(s) du texte d'origine (une exigée)")
            mutant = source.replace(avant, apres)
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
                           text=True, timeout=900)
        bilan = [x for x in p.stdout.splitlines() if re.search(r"\d+ (passed|failed)", x)]
        echecs = sorted(re.sub(r"^FAILED \S+::", "", x).split(" - ")[0] for x in p.stdout.splitlines()
                        if x.startswith(("FAILED ", "ERROR ")))
        resultats.append({"mutant": nom, "garde": garde, "code_pytest": p.returncode,
                          "bilan": bilan[-1].strip() if bilan else p.stdout[-300:], "essais_en_echec": echecs,
                          "issue": ("contrôle : tous passés" if avant is None and p.returncode == 0 else
                                    "CONTRÔLE EN ÉCHEC" if avant is None else "tué" if p.returncode != 0 else "SURVIVANT")})
        print(json.dumps(resultats[-1], ensure_ascii=False), file=sys.stderr, flush=True)
    print(json.dumps({"lanceur": str(LANCEUR), "lanceur_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
                      "essais": str(ESSAIS), "essais_sha256": hashlib.sha256(essais.encode("utf-8")).hexdigest(),
                      "mutants": resultats, "tues": sum(1 for r in resultats if r["issue"] == "tué"),
                      "survivants": [r["mutant"] for r in resultats if r["issue"] == "SURVIVANT"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
