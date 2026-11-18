#!/usr/bin/env python3
"""Relevé par programme de la date d'origine de la ligne de la première fiche de code de l'apprentissage des sondes sur la
tâche (étape B bis de T0.7) — v1.

Pièce demandée par la session mère, **sans effet sur la lecture** (quatrième addendum d'écart, QA-3 et fait F7) : la ligne
`CODE-BBIS` de la première fiche a été remise au registre propre sur la lignée de `main` avec une date écrite qui n'est pas
celle de sa ligne d'origine, restée sur une autre lignée. Ce script relève les trois dates et dit si elles sont égales.

Il ne joue que des commandes git **en lecture** (`git log`, `git show`, `git rev-list`, `git merge-base --is-ancestor`) sur
l'histoire de deux fichiers : le registre propre `registres/t07-etape-b-bis-v1.md` et la première fiche
`registres/t07-etape-b-bis/code-bbis-v1.json`. Il n'importe aucun module de `controle_ia`, n'appelle aucune garde, n'ouvre aucun
fichier de résultat, ne lit pas le contenu de la fiche. Il écrit un seul fichier, qu'il n'écrase jamais (R12) ; le scellement
est fait à part (`python -m controle_ia.scellement sceller`).

Usage : `python3 scripts/releve_date_origine_premiere_fiche_bbis_v1.py [RACINE]` (défaut : le dépôt qui porte ce script).
Code 0 : relevé écrit ; code 2 : arrêt, motif imprimé, rien d'écrit.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REGISTRE = "registres/t07-etape-b-bis-v1.md"
FICHE = "registres/t07-etape-b-bis/code-bbis-v1.json"
SORTIE = "registres/t07-etape-b-bis/lecture-v1/releve-date-origine-premiere-fiche-bbis-v1.json"
LIGNEE = "origin/main"


class Arret(RuntimeError):
    pass


def git(racine: Path, *args: str, codes=(0,)) -> tuple[int, str]:
    r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True)
    if r.returncode not in codes:
        raise Arret(f"git {' '.join(args[:3])} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.returncode, r.stdout


def ancetre(racine: Path, commit: str, de: str) -> bool:
    code, _ = git(racine, "merge-base", "--is-ancestor", commit, de, codes=(0, 1))
    return code == 0


def en_utc(date_iso: str) -> str:
    """Heure de commit de git (`%cI`) rendue en `AAAA-MM-JJTHH:MM:SSZ`, la forme des dates écrites du registre."""
    return datetime.fromisoformat(date_iso).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def commits(racine: Path, *args: str) -> list[dict]:
    _, sortie = git(racine, "log", "--all", "--reverse", "--format=%H%x09%cI", *args)
    lus = []
    for l in sortie.splitlines():
        if l.strip():
            c, d = l.split("\t")
            parents = git(racine, "rev-list", "--parents", "-n", "1", c)[1].split()[1:]
            lus.append({"commit": c, "heure_du_commit": en_utc(d), "parents": parents,
                        "ancetre_de_la_lignee": ancetre(racine, c, LIGNEE)})
    return lus


def lignes_ajoutees(racine: Path, commit: str) -> list[dict]:
    """Lignes `| CODE-BBIS | date | FICHE | empreinte |` qu'un commit ajoute au registre propre."""
    _, diff = git(racine, "show", "--format=", commit, "--", REGISTRE)
    vues = []
    for l in diff.splitlines():
        if not l.startswith("+") or l.startswith("+++"):
            continue
        c = [x.strip() for x in l[1:].strip().strip("|").split("|")]
        if len(c) == 4 and c[0] == "CODE-BBIS" and c[2] == FICHE:
            vues.append({"date_ecrite": c[1], "empreinte_citee": c[3]})
    return vues


def relever(racine: Path) -> dict:
    inscriptions = []
    for c in commits(racine, "--", REGISTRE):
        for l in lignes_ajoutees(racine, c["commit"]):
            inscriptions.append({**c, **l})
    hors = [i for i in inscriptions if not i["ancetre_de_la_lignee"]]
    dans = [i for i in inscriptions if i["ancetre_de_la_lignee"]]
    if len(hors) != 1 or len(dans) != 1:
        raise Arret(f"inscriptions de la ligne de la première fiche : {len(hors)} hors de {LIGNEE}, {len(dans)} dans {LIGNEE} ; "
                    "une de chaque attendue : rien n'est deviné")
    origine, reinscrite = hors[0], dans[0]
    versements = commits(racine, "--diff-filter=A", "--", FICHE)
    hors_f = [v for v in versements if not v["ancetre_de_la_lignee"]]
    if len(hors_f) != 1:
        raise Arret(f"commits qui versent la fiche hors de {LIGNEE} : {len(hors_f)} ; un attendu : rien n'est deviné")
    fiche = hors_f[0]
    tete_lignee = git(racine, "rev-list", "-n", "1", LIGNEE)[1].strip()
    return {
        "objet": "date d'origine de la ligne CODE-BBIS de la première fiche de code (étape B bis de T0.7) ; relevé sans effet "
                 "sur la lecture",
        "methode": "commandes git en lecture seulement (log, show, rev-list, merge-base --is-ancestor) sur l'histoire du "
                   "registre propre et de la première fiche ; aucun module de controle_ia importé, aucune garde appelée, "
                   "aucun fichier de résultat ouvert",
        "registre_propre": REGISTRE, "fiche": FICHE, "lignee": LIGNEE, "tete_de_la_lignee": tete_lignee,
        "ligne_d_origine_sur_l_autre_lignee": origine,
        "commit_qui_avait_verse_la_fiche_sur_l_autre_lignee": fiche,
        "ligne_reinscrite_sur_la_lignee": reinscrite,
        "tous_les_commits_qui_versent_la_fiche": versements,
        "egalites": {
            "date_ecrite_reinscrite_egale_a_la_date_ecrite_d_origine":
                reinscrite["date_ecrite"] == origine["date_ecrite"],
            "date_ecrite_reinscrite_egale_a_l_heure_du_commit_qui_avait_verse_la_fiche":
                reinscrite["date_ecrite"] == fiche["heure_du_commit"],
            "date_ecrite_reinscrite_egale_a_l_heure_de_son_propre_commit":
                reinscrite["date_ecrite"] == reinscrite["heure_du_commit"],
            "empreinte_citee_egale_dans_les_deux_lignes":
                reinscrite["empreinte_citee"] == origine["empreinte_citee"],
        },
    }


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    racine = Path(a[0]) if a else Path(__file__).resolve().parent.parent
    sortie = racine / SORTIE
    try:
        if sortie.exists():
            raise Arret(f"{SORTIE} existe déjà (R12 : jamais écrasé)")
        doc = relever(racine)
    except Arret as e:
        print(f"RELEVE ARRET : {e}")
        return 2
    sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"RELEVE ECRIT {SORTIE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
