#!/usr/bin/env python3
"""Contre-lecture du lanceur `lancer_course_ideation_bassins_etroits_v1.py` — outil de mutations des gardes (version 3, adaptée par le préparateur de l'outil 3 du contre-lecteur, 6fdac21d…), suite des
essais rejouée sur chaque mutant.

Outil du contre-lecteur (Claude Fable 5.2) adapté au lanceur v3 par le préparateur (Claude Opus 5.5), 13 novembre 2026 : treize mutants sur les gardes neuves du v3 (les quatre survivants de la vérification courte, verrou, orphelin, environnement, relance, runs du v2). Aucun modèle, aucun réseau. Le dépôt n'est pas touché :
chaque mutant est une copie du lanceur écrite dans le dossier de travail (`<travail>/<nom>/scripts/…`), et la suite des
essais est une copie de `tests/test_lancer_course_ideation_bassins_etroits_v1.py` où trois lignes seulement changent :
`RACINE` (fixée au dépôt réel, pour le registre et les pièces réels), `SCRIPT` (le mutant), et `lc.DEPOT = RACINE` après le
chargement (pour que `Reglages.production()` vise le dépôt réel comme dans la suite d'origine). Le cas « base » (aucune
mutation) doit rendre tous les essais passés : c'est le contrôle de l'outil.

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
NOM = "lancer_course_ideation_bassins_etroits_v3"
LANCEUR = DEPOT / "scripts" / f"{NOM}.py"
ESSAIS = DEPOT / "tests" / f"test_{NOM}.py"

# (nom, garde visée, texte d'origine — une seule occurrence exigée —, texte muté)
MUTATIONS = [
    ('base', "aucune (contrôle de l'outil)", None, None),
    ('W1-zombie-tenu-pour-vivant', 'V2 : zombie tenu pour vivant', '    if len(champs) < 20 or champs[0] == "Z":', '    if len(champs) < 20:'),
    ('W2-courses-par-generation-non-bornees', 'V3 : plus de deux courses par génération', '    if len(parties) >= MAX_COURSES_PAR_GENERATION:', '    if len(parties) >= 30:'),
    ('W3-relance-apres-fiches', 'relance après des fiches', '        if fp is not False:', '        if fp is True and False:'),
    ('W4-relance-depense-illisible', 'relance après dépense illisible', '        if not dep["course_lisible"]:', '        if False:'),
    ('W5-bras-mort-non-compte', 'V10 : bras mort non compté', '    if manquants:\n', '    if False:\n'),
    ('W6-bras-sans-code-non-verrouillant', 'V16 : bras sans code scellé', '    if any(lire_code(b["depart"]["superviseur"]) is None for b in run["bras"]):', '    if False:'),
    ('W7-verrou-retire', 'R1 : verrou', '        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)', '        pass'),
    ('W8-orphelin-ignore', 'R2 : orphelin ignoré', '    if orphs:', '    if False:'),
    ('W9-orphelin-jamais-vu', 'R2 : orphelin jamais détecté', '    if vu is None or (debut is not None and vu != debut):\n        return None', '    if True:\n        return None'),
    ('W10-environnement-entier', 'environnement entier transmis', '    garde = {n: env[n] for n in env if n in NOMS_PERMIS or (prefixe_essais and n.startswith(prefixe_essais))}', '    garde = {n: env[n] for n in env}'),
    ('W11-runs-v2-ignores', 'runs du v2 non lus', '                   anterieurs=tuple((DEPOT / "runs" / d, s, v) for d, s, v in ANTERIEURS))', '                   anterieurs=())'),
    ('W12-relance-sans-fin-propre', 'relance sans fin propre', '        if x["fin"] is None or x["fin"].get("code") is None:\n            return False, f"tentative {x[\'nom\']} sans fin propre (code non scellé)"', '        if False:\n            return False, ""'),
    ('W13-exception-bras-non-gardee', 'R4', '    except BaseException as e:  # noqa: BLE001\n        raise Refus(f"bras : exception', '    except ZeroDivisionError as e:  # noqa: BLE001\n        raise Refus(f"bras : exception'),
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
