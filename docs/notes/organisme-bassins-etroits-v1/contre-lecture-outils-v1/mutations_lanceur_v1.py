#!/usr/bin/env python3
"""Contre-lecture du lanceur `lancer_course_ideation_bassins_etroits_v1.py` — outil 3 : mutations des gardes, suite des
essais rejouée sur chaque mutant.

Écrit par le contre-lecteur (Claude Fable 5.2), 13 novembre 2026. Aucun modèle, aucun réseau. Le dépôt n'est pas touché :
chaque mutant est une copie du lanceur écrite dans le dossier de travail (`<travail>/<nom>/scripts/…`), et la suite des
essais est une copie de `tests/test_lancer_course_ideation_bassins_etroits_v1.py` où trois lignes seulement changent :
`RACINE` (fixée au dépôt réel, pour le registre et les pièces réels), `SCRIPT` (le mutant), et `lc.DEPOT = RACINE` après le
chargement (pour que `Reglages.production()` vise le dépôt réel comme dans la suite d'origine). Le cas « base » (aucune
mutation) doit rendre les 77 essais passés : c'est le contrôle de l'outil.

Usage : <python avec pytest> -B mutations_lanceur_v1.py DOSSIER_DE_TRAVAIL_NEUF
Un seul processus d'essais à la fois. Sortie : un objet JSON (par mutant : tué ou survivant, essais en échec).
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
NOM = "lancer_course_ideation_bassins_etroits_v1"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"

# (nom, garde visée, texte d'origine — une seule occurrence exigée —, texte muté)
MUTATIONS = [
    ("base", "aucune (contrôle de l'outil)", None, None),
    ("M1-cumul-sans-plafond-suivant", "garde de cumul : le plafond de ce qui va être lancé n'est plus compté",
     "    if deja + plafond_suivant > borne + 1e-9:", "    if deja > borne + 1e-9:"),
    ("M2-depense-illisible-comptee-zero", "dépense illisible : manifeste de fin illisible compté 0 au lieu du plafond",
     '            return PLAFOND_COURSE_USD, "manifeste de fin illisible : plafond entier compté"',
     '            return 0.0, "manifeste de fin illisible : plafond entier compté"'),
    ("M3-relance-apres-depense", "pas de relance après dépense : la condition de dépense est retirée",
     '        if dep["course_usd"] + dep["bras_usd"] > 0 or x["fin"] is None:', '        if x["fin"] is None:'),
    ("M4-generation-suivante-sans-bras", "génération g + 1 admise dès que la course de g est réussie (sans bras)",
     '        prec = [x for x in runs if x["generation"] == g - 1 and bras_reussi(x)]',
     '        prec = [x for x in runs if x["generation"] == g - 1 and course_reussie(x)]'),
    ("M5-argument-non-ferme", "argument unique : des arguments en plus sont admis",
     "    if len(argv) != 1 or argv[0] not in GENERATIONS:", "    if len(argv) < 1 or argv[0] not in GENERATIONS:"),
    ("M6-tentatives-de-course-non-bornees", "borne de trois tentatives de course par génération",
     "    if len(parties) >= 3:", "    if len(parties) >= 30:"),
    ("M7-borne-du-cumul-egale-au-go", "garde de cumul : la borne de 60 USD codée cède devant un plafond de GO plus haut",
     "    borne = min(TOTAL_LIGNE_USD, plafond_go)", "    borne = plafond_go"),
    ("M8-attestation-sans-consigne-du-juge", "attestation : la consigne en attente du juge n'est plus exigée",
     '    if JUGE_EXTERNE[0] not in (a.get("consignes_en_attente_sha256") or {}):', "    if False:"),
    ("M9-bras-non-bornes", "borne de trois bras par course",
     '        if len(run["bras"]) >= 3:', '        if len(run["bras"]) >= 30:'),
    ("M10-bras-reussi-sans-manifeste-du-bras", "génération jouée : le manifeste du bras scellé n'est plus exigé",
     '                and _lire_json_si_scelle(run["sortie"] / "manifeste-bras-rapporte.json") is not None)', "                )"),
    ("M11-classement-illisible-transmis", "règle de passage : un classement illisible est transmis",
     '    if classement.get("lisible_L2_L4") is not True:', "    if False:"),
    ("M12-plancher-du-controle-court-non-garde", "garde du bras : plancher de la commande d'Argon pour le contrôle court",
     ' or r.controle_bras_usd < g["plancher_controle_court"]:', ":"),
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
    for l in (l_racine, l_script, l_charge):
        assert essais.count(l) == 1, l
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
        t = essais.replace(l_racine, f'RACINE = Path("{DEPOT}")\n').replace(
            l_script, f'SCRIPT = Path("{chemin_mutant}")\n').replace(l_charge, l_charge + "lc.DEPOT = RACINE\n")
        chemin_essais = d / "tests" / f"test_{NOM}.py"
        chemin_essais.write_text(t, encoding="utf-8")
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(d), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
        p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(d / "pt"),
                            "-rf", "--tb=no", str(chemin_essais)], cwd=str(d), env=env, capture_output=True, text=True,
                           timeout=600)
        bilan = [x for x in p.stdout.splitlines() if re.search(r"\d+ (passed|failed)", x)]
        echecs = sorted(re.sub(r"^FAILED \S+::", "", x).split(" - ")[0] for x in p.stdout.splitlines() if x.startswith("FAILED "))
        resultats.append({"mutant": nom, "garde": garde, "avant": avant, "apres": apres, "code_pytest": p.returncode,
                          "bilan": bilan[-1].strip() if bilan else p.stdout[-300:], "essais_en_echec": echecs,
                          "issue": ("contrôle : tous passés" if avant is None and p.returncode == 0 else
                                    "CONTRÔLE EN ÉCHEC" if avant is None else "tué" if echecs else "SURVIVANT")})
        print(json.dumps(resultats[-1], ensure_ascii=False), file=sys.stderr, flush=True)
    print(json.dumps({"lanceur": str(LANCEUR), "essais": str(ESSAIS), "mutants": resultats,
                      "tues": sum(1 for r in resultats if r["issue"] == "tué"),
                      "survivants": [r["mutant"] for r in resultats if r["issue"] == "SURVIVANT"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
