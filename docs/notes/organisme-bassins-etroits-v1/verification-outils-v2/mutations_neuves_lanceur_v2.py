#!/usr/bin/env python3
"""Vérification courte du lanceur v2 — outil 3 : mutations neuves sur le code neuf du v2 (lancement détaché, seuil sans
dépense, bras), suite des 122 essais rejouée sur chaque mutant.

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Même méthode que `contre-lecture-outils-v1/
mutations_lanceur_v1.py` : le dépôt n'est pas touché ; chaque mutant est une copie du lanceur dans le dossier de travail ; la
suite est une copie de `tests/test_lancer_course_ideation_bassins_etroits_v2.py` où trois lignes changent (`RACINE` fixée au
dépôt réel, `SCRIPT` = le mutant, `lc.DEPOT = RACINE`). Aucune de ces mutations n'est dans la liste du préparateur.

Usage : <python avec pytest> -B mutations_neuves_lanceur_v2.py DOSSIER_DE_TRAVAIL [NOM_DE_MUTANT …]
(sans nom : tous ; le dossier de travail peut exister, chaque mutant y a son sous-dossier neuf). Un processus d'essais à la fois.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
NOM = "lancer_course_ideation_bassins_etroits_v2"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"

MUTATIONS = [
    ("base", "aucune (contrôle de l'outil)", None, None),
    ("V1-pid-reutilise-tenu-pour-vivant", "superviseur vivant : l'heure de départ du processus n'est plus comparée",
     '    return bool(sup) and debut_processus(sup["pid"]) is not None and debut_processus(sup["pid"]) == sup["debut_proc"]',
     '    return bool(sup) and debut_processus(sup["pid"]) is not None'),
    ("V2-zombie-tenu-pour-vivant", "un processus fini non récolté (zombie) compte pour vivant",
     '    if len(champs) < 20 or champs[0] == "Z":', "    if len(champs) < 20:"),
    ("V3-seuil-sans-depense-a-1-usd", "relance permise après une dépense relevée jusqu'à 1 USD",
     "SEUIL_SANS_DEPENSE_USD = 1e-5 ", "SEUIL_SANS_DEPENSE_USD = 1.0 "),
    ("V5-en-marche-de-la-seule-generation-demandee", "un processus en marche ne retient que sa propre génération",
     "                 if fin is None and superviseur_vivant(sup)]\n    if en_marche:",
     '                 if fin is None and superviseur_vivant(sup) and run["generation"] == g]\n    if en_marche:'),
    ("V10-bras-mort-non-compte", "dépense : un bras mort sans fin propre n'est plus compté à son plafond",
     '    manquants = max(len(morts) + len(vivants), len(run["bras"]) - expliques)',
     '    manquants = max(len(vivants), len(run["bras"]) - expliques - len(morts))'),
    ("V14-sans-session-neuve", "le superviseur n'est plus détaché dans une session de processus neuve",
     "                             stdin=subprocess.DEVNULL, start_new_session=True)",
     "                             stdin=subprocess.DEVNULL, start_new_session=False)"),
    ("V15-signaux-non-relayes", "le superviseur ne relaie plus les signaux à l'orchestrateur",
     "        signal.signal(s, relayer)", "        pass"),
    ("V16-bras-sans-fin-propre-relancable", "bras : un bras précédent sans code scellé ne verrouille plus",
     '    if any(lire_code(b["depart"]["superviseur"]) is None for b in run["bras"]):', "    if False:"),
]


def main():
    travail = Path(sys.argv[1]).resolve()
    choisis = set(sys.argv[2:])
    travail.mkdir(parents=True, exist_ok=True)
    source = LANCEUR.read_text(encoding="utf-8")
    essais = ESSAIS.read_text(encoding="utf-8")
    l_racine = "RACINE = Path(__file__).resolve().parents[1]\n"
    l_script = f'SCRIPT = RACINE / "scripts" / "{NOM}.py"\n'
    l_charge = "_spec.loader.exec_module(lc)\n"
    for l in (l_racine, l_script, l_charge):
        assert essais.count(l) == 1, l
    resultats = []
    for nom, garde, avant, apres in MUTATIONS:
        if choisis and nom not in choisis:
            continue
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
        t = essais.replace(l_racine, f'RACINE = Path("{DEPOT}")\n').replace(
            l_script, f'SCRIPT = Path("{chemin_mutant}")\n').replace(l_charge, l_charge + "lc.DEPOT = RACINE\n")
        chemin_essais = d / "tests" / f"test_{NOM}.py"
        chemin_essais.write_text(t, encoding="utf-8")
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(d), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
        try:
            p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(d / "pt"),
                                "-rf", "--tb=no", str(chemin_essais)], cwd=str(d), env=env, capture_output=True, text=True,
                               timeout=400)
            sortie, code = p.stdout, p.returncode
        except subprocess.TimeoutExpired as e:
            sortie, code = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or ""), "délai"
        bilan = [x for x in sortie.splitlines() if re.search(r"\d+ (passed|failed)", x)]
        echecs = sorted(re.sub(r"^FAILED \S+::", "", x).split(" - ")[0] for x in sortie.splitlines() if x.startswith("FAILED "))
        issue = ("contrôle : tous passés" if avant is None and code == 0 else "CONTRÔLE EN ÉCHEC" if avant is None
                 else "tué" if echecs else "tué (délai dépassé : un essai ne rend plus la main)" if code == "délai" else "SURVIVANT")
        resultats.append({"mutant": nom, "garde": garde, "avant": avant, "apres": apres, "code_pytest": code,
                          "bilan": bilan[-1].strip() if bilan else sortie[-200:], "essais_en_echec": echecs, "issue": issue})
        print(json.dumps(resultats[-1], ensure_ascii=False), file=sys.stderr, flush=True)
    print(json.dumps({"lanceur": str(LANCEUR), "essais": str(ESSAIS), "mutants": resultats}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
