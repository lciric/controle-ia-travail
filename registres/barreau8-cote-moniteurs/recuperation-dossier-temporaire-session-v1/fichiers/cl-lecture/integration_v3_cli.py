"""Essai d'intégration, étape 2 : la lecture v3 jouée par sa ligne de commande, en sous-processus, au premier plan, dans le dépôt
d'essai de l'étape 1. Registre propre aux six clés, dans l'ordre et aux formes du texte ; bordereau du code de la lecture écrit
par sa sous-commande ; extrait des états, mandats, pièces d'essai. Argument : le dossier de travail de l'étape 1."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
PY = "/home/user/controle-ia-travail/.venv/bin/python"
base = Path(sys.argv[1])
c = json.loads((base / "cadre-jouet.json").read_text(encoding="utf-8"))
racine, registre = Path(c["racine"]), Path(c["registre"])
env = dict(os.environ, PYTHONPATH=str(racine / "src"), CADRE_JOUET=str(base / "cadre-jouet.json"))
SONDES = ["--sondes-legeres", c["sondes_chemins"]["legeres"], "--planchers", c["sondes_chemins"]["planchers"],
          "--sondes-neuves", c["sondes_chemins"]["neuves"]]
COMMUN = ["--racine", str(racine), "--registre", str(registre)]
sys.path[:0] = [str(racine / "src")]
from controle_ia.scellement import empreinte, sceller  # noqa: E402


def git(*a):
    subprocess.run(["git", "-C", str(racine), "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid",
                    "-c", "commit.gpgsign=false", *a], check=True, capture_output=True)


def committer(m):
    git("add", "-A")
    if subprocess.run(["git", "-C", str(racine), "status", "--porcelain"], capture_output=True, text=True).stdout.strip():
        git("commit", "-q", "-m", m)


def lancer(nom, argv, enveloppe=True, timeout=580):
    cmd = [PY, str(ICI / "cli_jouet_v3.py"), *argv] if enveloppe else [PY, "-m", "controle_ia.barreau8_moniteurs.lecture_sondes_v3", *argv]
    r = subprocess.run(cmd, cwd=racine, env=env, capture_output=True, text=True, timeout=timeout)
    print(f"=== {nom} : code {r.returncode}", flush=True)
    print((r.stdout[-2500:] + ("\n[err] " + r.stderr[-2500:] if r.stderr.strip() else "")).strip(), flush=True)
    return r


def scelle(chemin, texte):
    p = racine / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return sceller(p)


etape = sys.argv[2] if len(sys.argv) > 2 else "tout"
if etape in ("tout", "preparer"):
    lancer("modules (enveloppe)", ["modules"])
    scelle("docs/rapport-conformite-lecture.md", "Rapport de conformité jouet (lecture).\n")
    scelle("docs/notice-lecture.md", "Notice jouet (lecture).\n")
    committer("pièces du code de la lecture")
    r = lancer("bordereau-code (enveloppe)", ["bordereau-code", "--racine", str(racine), "--texte-scelle", "prereg/texte-jouet-v1.md",
                                              "--rapport-conformite", "docs/rapport-conformite-lecture.md", "--notice",
                                              "docs/notice-lecture.md", "--accord-lecture", "GO-2026-11-19-02",
                                              "--sortie", "registres/bordereau-code-lecture.json"])
    assert r.returncode == 0
    ligne_code = [l for l in r.stdout.splitlines() if l.startswith("| CODE-LECTURE-SONDES-IIB |")][0]
    cel = [x.strip() for x in ligne_code.strip("|").split("|")]
    paire = {"cout": "réussit", "traits": "échoue", "mots_et_cout": "échoue"}
    sha_e = scelle("docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json", json.dumps({
        "avertissement": "EXPLORATOIRE, NON OPPOSABLE (R-522) : états des lectures, sans chiffre, pour le côté moniteurs",
        "run_id": "20261119-010203-course-jouet", "lecture_dommage": {"phrase": "dommage agrégé vu"},
        "lecture_diffusion": {"par_paire": {"B100-H": {**paire, "unite": "échoue"}, "B50-H": {**paire, "unite": "échoue"},
                                            "TJ100-H": {**paire, "unite": "réussit"}, "B100-TJ100": {"mots_et_cout": "échoue"}},
                              "phrase": None}}, ensure_ascii=False))
    sha_piece = scelle("docs/piece-ordre-scelle.md", "comparaison de l'ordre faite (pièce d'essai)\n")
    for role in ("lecteur", "juge"):
        scelle(f"docs/mandat-{role}.md", f"exclus {'a' * 64} ; qui a lu quoi {'b' * 64} ; pièce de l'ordre {sha_piece}\n")
    livraison = Path(c["bordereau_livraison"]).relative_to(racine)
    with open(registre, "a", encoding="utf-8") as f:
        f.write(f"| CODE-LECTURE-SONDES-IIB | 2026-11-19T03:10:00Z | {cel[2]} | {cel[3]} |\n")
        f.write(f"| ETATS-COURSE-IIB | 2026-11-19T03:20:00Z | docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json | {sha_e} |\n")
        f.write(f"| LIVRAISON-PASSE-IIB | 2026-11-19T03:30:00Z | {livraison} | {c['bordereau_livraison_sha256']} |\n")
    committer("registre propre : code de la lecture, états, livraison")
    print(registre.read_text(encoding="utf-8"))
if etape in ("tout", "reception"):
    lancer("reception (enveloppe)", ["reception", *COMMUN, *SONDES])
    lancer("etats (enveloppe)", ["etats", *COMMUN])
    lancer("reception par python -m (cadre du texte)", ["reception", *COMMUN, *SONDES], enveloppe=False)
if etape in ("tout", "puissance"):
    r = lancer("puissance (enveloppe, recette réduite)", ["puissance", *COMMUN, "--entropie", str(c["entropie"]),
                                                          "--run-id", "20261119-040000-puissance-barreau8"])
    committer("recette de puissance")
if etape in ("tout", "lecture"):
    LECT = ["lecture", *COMMUN, *SONDES, "--entropie", str(c["entropie"]), "--run-id", "20261119-040100-lecture-sondes-barreau8",
            "--registre-accords", str(racine / "registres" / "go.md"),
            "--puissance", "diag/20261119-040000-puissance-barreau8/aires-minimales-detectables-barreau8-v1.json",
            "--mandat-lecteur", "docs/mandat-lecteur.md", "--mandat-juge", "docs/mandat-juge.md",
            "--empreinte-liste-exclus", "a" * 64, "--empreinte-qui-a-lu-quoi", "b" * 64, "--piece-ordre-scelle", "docs/piece-ordre-scelle.md"]
    r = lancer("lecture (enveloppe)", LECT)
    print("--- registre après la lecture :")
    print(registre.read_text(encoding="utf-8"))
    committer("sortie de la lecture et ligne inscrite")
    LECT2 = [x if x != "20261119-040100-lecture-sondes-barreau8" else "20261119-040200-lecture-sondes-barreau8" for x in LECT]
    lancer("seconde lecture (enveloppe)", LECT2)
    lancer("audit (enveloppe)", ["audit", *COMMUN, *SONDES])
    committer("audit")
