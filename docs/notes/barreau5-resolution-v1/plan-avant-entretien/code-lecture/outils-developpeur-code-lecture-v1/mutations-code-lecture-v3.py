"""Passage de mutations v3 du code de lecture du barreau 5 (développeur du code de lecture, 20 novembre 2026) : les
corrections de la vérification (`verification-corrections-code-lecture-v1.md`, fb1b7d04…) défaites une à une — V-1 (un
fichier de scores par jeton par série ; borne écrite de la taille d'un fichier fermé), v-1 (branche de sortie de la pièce
pour `SCORES-B5F`), v-2 (aucun score par jeton d'une série propre). Même procédé que `mutations-code-lecture-v2.py` :
copie de travail unique ; témoins sans mutation exigés verts avant tout compte ; « attrapée » si pytest rend le code 1 ;
chaque « avant » paraît une fois exactement dans le fichier d'origine, sinon « introuvable ».

Usage : python -B mutations-code-lecture-v3.py COPIE BASETEMP [IDENTIFIANTS…]  — imprime le bilan en JSON.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[6]
R, AM = "src/controle_ia/barreau5_familles/relecture_v1.py", "scripts/amorce_b5f_lecture_v1.sh"
L, S = "src/controle_ia/barreau5_familles/lecture_v1.py", "src/controle_ia/barreau5_familles/sondes_v1.py"
EA, EE, ELA, ER = ("tests/test_amorce_b5f_lecture_v1.py", "tests/test_amorce_b5f_lecture_entiere_v1.py",
                   "tests/test_lancer_b5f_lecture_v1.py", "tests/test_barreau5_familles_relecture_v1.py")
EL, ES = "tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py"
RAPIDE = "not bout_en_bout and not produits_ecrits and not deplacement_moyen"
A_COPIER = ["src", "tests/conftest.py", EA, EE, ELA, ER, EL, ES, AM, "scripts/lancer_b5f_lecture_v1.sh",
            "prereg/T0.6-organismes-config-7b-v1.json", "prereg/T0.6-organismes-config-7b-v1.json.sha256",
            "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md", "pyproject.toml", ".gitignore",
            ".gitattributes", "requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt",
            ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    ("J01", L, "V-1 : fichiers de scores par jeton non lus", "            if s in SONDES_PAR_JETON:\n                for nom in gardees:",
     "            if False:\n                for nom in gardees:", [EL]),
    ("J02", L, "V-1 : fichier de scores par jeton hors du plan admis",
     '_exiger(not intrus, f"fichiers de scores par jeton hors du plan', '_exiger(True, f"fichiers de scores par jeton hors du plan',
     [EL]),
    ("J03", L, "V-1 : étiquette de série non comparée", 'and j.get("pli") == k and j.get("serie") == nom and set(j)',
     'and j.get("pli") == k and set(j)', [EL]),
    ("J04", L, "V-1 : scores par jeton admis dans le fichier de scores",
     '_exiger(isinstance(series[nom], dict) and set(series[nom]) == {"actions"},', "_exiger(isinstance(series[nom], dict),",
     [EL]),
    ("J05", L, "V-1 : borne de la taille non comparée", "    _exiger(n <= TAILLE_MAX_FICHIER,", "    _exiger(True,", [EL, ES]),
    ("J06", L, "V-1 : borne absente de la garde d'ouverture", '        exiger_taille_bornee(arbre / rel, f["octets"])\n', "",
     [EL]),
    ("J07", L, "V-1 : borne absente de l'inventaire de l'instance", "        exiger_taille_bornee(arbre / f)\n", "", [EL]),
    ("J08", S, "V-1 : borne absente de l'écriture des scores", "        _lv.exiger_taille_bornee(dossier / rel, len(octets[rel]))\n",
     "", [ES]),
    ("J09", S, "V-1 : scores par jeton laissés dans le fichier de scores",
     '"series": {s: {"actions": v["actions"]} for s, v in (series or {}).items()}}}', '"series": dict(series or {})}}', [ES]),
    ("J10", S, "v-2 : scores par jeton des séries propres gardés", '_PROPRE = re.compile(r"propre-A[1-3]-saboteur")',
     '_PROPRE = re.compile(r"(?!)")', [ES]),
    ("J11", R, "v-1 : commit admis sur une branche distante quelconque",
     'if r.returncode != 0 or f"origin/{branche}" not in r.stdout.split():\n        raise GardeArret(f"commit {commit[:12]} absent',
     'if r.returncode != 0 or not r.stdout.strip():\n        raise GardeArret(f"commit {commit[:12]} absent', [ELA]),
    ("J12", R, "V-1 : fichiers de scores par jeton hors de la liste blanche des sorties",
     r'                     r"jetons/[a-zA-Z0-9-]+-pli[01]/[A-Za-z0-9_-]+\.json)(?:\.sha256)?|"',
     r'                     r"x)(?:\.sha256)?|"', [(ER, RAPIDE)]),
    ("J13", AM, "V-1 : fichiers de scores par jeton hors de la liste blanche de l'amorce",
     r"|jetons/[a-zA-Z0-9-]+-pli[01]/[A-Za-z0-9_-]+\\.json)(\\.sha256)?\$", r")(\\.sha256)?\$", [EA]),
]


def copier(copie: Path) -> None:
    if copie.exists():
        raise SystemExit(f"{copie} existe déjà : une seule copie de travail, neuve")
    for rel in A_COPIER:
        s, d = DEPOT / rel, copie / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)


def jouer(copie: Path, base: Path, nom: str, essais) -> dict:
    cibles = []
    for e in essais:
        cibles += [e[0], "-k", e[1]] if isinstance(e, tuple) else [e]
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *cibles], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith(("FAILED", "ERROR"))]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1] if lignes else "",
            "premier_echec": echec[0] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    choix = set(argv[2:])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {}, "mutations": []}
    for nom, essais in {"EA": [EA], "ELA": [ELA], "ER": [(ER, RAPIDE)], "EL": [EL], "ES": [ES]}.items():
        bilan["temoins"][nom] = jouer(copie, base, f"temoin-{nom}", essais)
        print(f"témoin {nom} : code {bilan['temoins'][nom]['code']} ({bilan['temoins'][nom]['fin']})", file=sys.stderr,
              flush=True)
    if any(t["code"] != 0 for t in bilan["temoins"].values()):
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        raise SystemExit("un témoin sans mutation échoue : aucun compte de mutations")
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        if choix and mid not in choix:
            continue
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if origine.count(avant) != 1:
            x.update({"etat": "introuvable", "occurrences": origine.count(avant)})
            bilan["mutations"].append(x)
            print(f"{mid} introuvable ({x['occurrences']})", file=sys.stderr, flush=True)
            continue
        cible = copie / fichier
        cible.write_text(origine.replace(avant, apres), encoding="utf-8")
        try:
            r = jouer(copie, base, mid, essais)
        finally:
            cible.write_text(origine, encoding="utf-8")
        etat = "attrapée" if r["code"] == 1 else ("MANQUÉE" if r["code"] == 0 else f"erreur de l'outil (code {r['code']})")
        x.update({"etat": etat, **r})
        bilan["mutations"].append(x)
        print(f"{mid} {etat} ({r['duree_s']} s) {r['premier_echec'] or ''}", file=sys.stderr, flush=True)
    joues = [m for m in bilan["mutations"] if m["etat"] in ("attrapée", "MANQUÉE")]
    bilan["compte"] = {"jouees": len(joues), "attrapees": sum(m["etat"] == "attrapée" for m in joues),
                       "manquees": [m["id"] for m in joues if m["etat"] == "MANQUÉE"],
                       "erreurs_de_l_outil": [m["id"] for m in bilan["mutations"] if m["etat"].startswith("erreur")],
                       "introuvables": [m["id"] for m in bilan["mutations"] if m["etat"] == "introuvable"]}
    print(json.dumps(bilan, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
