#!/usr/bin/env python3
"""Mutants du contre-lecteur (modèle B) sur `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` — version 1.

Vingt-six mutants, tous distincts des soixante et un du préparateur (`../outils/mutations_lanceur_regard_ou_raisons_v1.py`),
sur quatre familles de gardes : dépense (C), ligne de GO (G), relance (R), environnement, bac à sable, garde de soi (E, B, K,
D, S). Même montage que le banc du préparateur, réécrit ici : chaque mutant est une copie du lanceur, avec son compagnon
recalculé, dans un dossier de travail neuf hors du dépôt ; la suite d'essais est une copie de
`tests/test_lancer_course_ideation_regard_ou_raisons_v1.py` où trois lignes changent (`RACINE`, `SCRIPT`, `lc.DEPOT`).
Le cas « base » doit rendre tous les essais passés. Un mutant est « tué » si au moins un essai échoue (`-x`).

Aucun modèle, aucun réseau, aucun lancement ; le dépôt n'est pas touché ; l'environnement des essais est une liste fixe de
quatre noms (aucune variable de la session n'est transmise).

Usage : <python avec pytest> -B mutants_contre_lecteur_regard_ou_raisons_v1.py DOSSIER_DE_TRAVAIL_NEUF [nom,nom,…]
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
    # ---------------------------------------------------------------------------------------------------------- dépense
    ("C01-cout-externe-oublie-au-manifeste-de-fin", "dépense lue = Claude + externe",
     '            return _cout(j, "cout_total_usd") + _cout(j, "cout_externe_usd"), True, "manifeste de fin de l\'orchestrateur"',
     '            return _cout(j, "cout_total_usd"), True, "manifeste de fin de l\'orchestrateur"'),
    ("C02-cout-externe-oublie-au-controle", "dépense du contrôle = Claude + externe",
     '                total += _cout(m, "reglages", "cout_claude_usd") + _cout(m, "reglages", "cout_externe_usd")',
     '                total += _cout(m, "reglages", "cout_claude_usd")'),
    ("C03-manifeste-de-fin-illisible-compte-zero", "manifeste de fin illisible → plafond",
     '            return PLAFOND_COURSE_USD, False, "manifeste de fin illisible : plafond entier compté"',
     '            return 0.0, True, "manifeste de fin illisible : plafond entier compté"'),
    ("C04-tentative-illisible-ignoree", "tentative de contrôle illisible → plafond",
     '                return PLAFOND_COURSE_USD, False, f"tentative de contrôle illisible ({nom}) : plafond entier compté"',
     "                pass"),
    ("C05-fichier-inattendu-au-controle-ignore", "fichier de contrôle inattendu → plafond",
     '            return PLAFOND_COURSE_USD, False, f"fichier de contrôle inattendu ({nom}) : plafond entier compté"',
     "            continue"),
    ("C06-cout-negatif-admis", "coût négatif refusé",
     "not math.isfinite(objet) or objet < 0:", "not math.isfinite(objet):"),
    ("C07-tolerance-du-cumul-elargie", "garde de cumul : relance seulement si ≤ 2,1 USD",
     "    if deja + suivant > borne + 1e-9:\n", "    if deja + suivant > borne + 0.05:\n"),
    ("C10-refus-de-taille-au-sceau-faux-ignore", "refus de taille au sceau faux → plafond",
     '                return PLAFOND_COURSE_USD, False, f"refus de taille au sceau faux ({nom}) : plafond entier compté"',
     "                pass"),
    ("C12-total-externe-releve", "total externe transmis = 8 USD du devis",
     "TOTAL_EXTERNE_USD = 8.0 ", "TOTAL_EXTERNE_USD = 9.0 "),
    # ------------------------------------------------------------------------------------------------------ ligne de GO
    ("G03-type-de-la-ligne", "type « calcul » exigé", '    if typ != "calcul":', "    if False:"),
    ("G04-deux-lignes-au-meme-identifiant", "une seule ligne principale par identifiant",
     "    if len(doublons) != 1:", "    if False:"),
    ("G05-ligne-citante-mal-formee-ignoree", "ligne qui cite le GO, mal formée → refus",
     '                raise Refus(f"ligne {i} qui cite {go_id} mal formée ({len(cellules)} colonnes) : lecture impossible")',
     "                continue"),
    ("G06-go-echu-admis", "échéance du GO", "    if not d_acc <= aujourd_hui <= d_ech:", "    if not d_acc <= aujourd_hui:"),
    ("G07-plafond-a-suffixe-admis", "forme « <nombre> USD » exacte",
     '    m = re.fullmatch(r"\\s*(\\d+(?:[.,]\\d+)?)\\s*USD\\s*", texte)', '    m = re.match(r"\\s*(\\d+(?:[.,]\\d+)?)\\s*USD\\s*", texte)'),
    # ---------------------------------------------------------------------------------------------------------- relance
    ("R01-course-sans-depart-non-comptee", "toute course lancée compte parmi les deux",
     '    lances = [x for x in runs if x["lance"]]', '    lances = [x for x in runs if x["lance"] and x["depart"] is not None]'),
    ("R02-trois-courses", "deux courses au plus", "MAX_COURSES = 2 ", "MAX_COURSES = 3 "),
    ("R03-fiches-refusees-non-comptees", "aucune relance après une fiche, même refusée ou en quarantaine",
     "    return any(listes)\n", "    return bool(listes[0])\n"),
    ("R08-superviseur-sans-pid-tenu-pour-rien", "superviseur créé sans PID scellé : inconnu, nœud",
     '        return {"inconnu": True, "dossier": str(dossier)}', "        return None"),
    # ----------------------------------------------------------------------- environnement, bac à sable, garde de soi
    ("E01-mandataire-permis", "liste des noms permis",
     'NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")', 'NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR", "HTTPS_PROXY")'),
    ("E02-prefixe-d-essai-libre", "préfixe d'essai : « FAUX_ » seul",
     '    if prefixe_essais is not None and prefixe_essais != "FAUX_":', "    if False:"),
    ("E04-superviseur-herite-de-tout-l-environnement", "environnement filtré transmis au superviseur",
     "str(r.orchestrateur), str(dossier)], cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe,",
     "str(r.orchestrateur), str(dossier)], cwd=str(r.orchestrateur), env=None, stdout=fo, stderr=fe,"),
    ("E05-sous-processus-herite-de-tout-l-environnement", "environnement filtré pour la liste blanche et la mesure",
     "        return subprocess.run(argv, cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=300,",
     "        return subprocess.run(argv, cwd=str(r.orchestrateur), env=None, capture_output=True, text=True, timeout=300,"),
    ("B01-bac-sans-proc-neuf-admis", "bac à sable : /proc neuf exigé", '    if not etat["proc_neuf"]:\n', "    if False:\n"),
    ("K01-noms-exclus-ecrits", "noms exclus jamais écrits (nombre et empreinte seulement)",
     '        "noms_exclus": {"nombre": len(exclus), "sha256_liste_triee"', '        "noms_exclus": {"nombre": len(exclus), "noms": exclus, "sha256_liste_triee"'),
    ("D01-drapeau-abrege-admis", "drapeaux interdits, formes abrégées comprises",
     "        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):", "        if any(f == nom for f in DRAPEAUX_INTERDITS):"),
    ("S01-lanceur-hors-de-sa-place", "M1 : fichier du lanceur à sa place",
     '    if os.path.realpath(f) != os.path.realpath(r.depot / "scripts" / FICHIER_LANCEUR):', "    if False:"),
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
    if DEPOT in travail.parents or travail == DEPOT:
        raise SystemExit("le dossier de travail doit être hors du dépôt")
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
    travail.mkdir(parents=True)
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
