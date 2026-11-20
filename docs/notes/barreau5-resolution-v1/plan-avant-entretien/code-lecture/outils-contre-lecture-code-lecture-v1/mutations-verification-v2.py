"""Mutations du contre-lecteur à la seconde vérification du code de lecture du barreau 5 (20 novembre 2026) : cinq défauts
sur les zones changées par les corrections de V-1, v-1 et v-2 (un fichier de scores par jeton par série, borne de la taille
d'un fichier fermé, branche de `SCORES-B5F`).

Même procédé que `mutations-verification-v1.py` : une copie de travail sous le bloc-notes ; chaque « avant » exactement une
fois ; attrapée si pytest rend le code 1 ; témoins sans mutation exigés verts ; fichier remis à l'identique.

Usage : python -B mutations-verification-v2.py COPIE BASETEMP
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
P = "src/controle_ia/barreau5_familles/"
L, S, R = f"{P}lecture_v1.py", f"{P}sondes_v1.py", f"{P}relecture_v1.py"
EL, ES = "tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py"
# essais du lanceur : les seuls essais de la ligne SCORES-B5F (premier passage de cet outil, nul : un autre essai du lanceur
# lit des fichiers du dépôt que la copie de travail ne porte pas ; le fichier entier passe sur le dépôt)
ELA = "tests/test_lancer_b5f_lecture_v1.py -k ligne_scores"
A_COPIER = ["src", "tests/conftest.py", EL, ES, "tests/test_lancer_b5f_lecture_v1.py",
            "tests/test_barreau5_familles_relecture_v1.py",
            "tests/test_amorce_b5f_lecture_v1.py", "scripts/lancer_b5f_lecture_v1.sh", "scripts/amorce_b5f_lecture_v1.sh",
            "prereg/T0.6-organismes-config-7b-v1.json", "prereg/T0.6-organismes-config-7b-v1.json.sha256", "pyproject.toml",
            "docs/sources/invites-2606.08892-v1", "requirements-gpu.txt",
            # la fixture des essais du lanceur copie ces deux fichiers (second passage nul sans eux)
            ".claude/hooks/garde_calcul.py", "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md"]

MUTATIONS = [
    ("W1", L, "garde d'ouverture : la borne de la taille d'un fichier fermé n'est plus revue",
     '        exiger_taille_bornee(arbre / rel, f["octets"])', "        pass", [EL]),
    ("W2", L, "chargement : un fichier de scores par jeton hors du plan est admis",
     '_exiger(not intrus, f"fichiers de scores par jeton hors du plan', '_exiger(True, f"fichiers de scores par jeton hors du plan',
     [EL]),
    ("W3", L, "chargement : la série d'un fichier de scores par jeton n'est plus comparée à son nom",
     'and j.get("pli") == k and j.get("serie") == nom and set(j)', 'and j.get("pli") == k and set(j)', [EL]),
    ("W4", S, "écriture : la borne de la taille n'est plus éprouvée avant d'écrire",
     "        _lv.exiger_taille_bornee(dossier / rel, len(octets[rel]))", "        pass", [ES]),
    ("W5", R, "SCORES-B5F : un commit d'une branche distante quelconque est admis",
     'if r.returncode != 0 or f"origin/{branche}" not in r.stdout.split():', "if r.returncode != 0 or not r.stdout.strip():",
     [ELA]),
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
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHONPATH": str(copie / "src"), "TMPDIR": "/dev/shm",
           "PYTHONDONTWRITEBYTECODE": "1", "HOME": os.environ.get("HOME", "/root")}
    debut = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-x", "--basetemp",
                        str(base / nom), *[a for e in essais for a in e.split()]], cwd=str(copie), env=env,
                       capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith("FAILED") or x.startswith("ERROR")]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1][:200] if lignes else "",
            "premier_echec": echec[0][:220] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {}, "mutations": []}
    for nom, essais in {"EL": [EL], "ES": [ES], "ELA": [ELA]}.items():
        bilan["temoins"][nom] = jouer(copie, base, f"temoin-{nom}", essais)
        print(f"témoin {nom} : code {bilan['temoins'][nom]['code']} ({bilan['temoins'][nom]['fin']}) "
              f"{bilan['temoins'][nom]['premier_echec'] or ''}", file=sys.stderr, flush=True)
    if any(t["code"] != 0 for t in bilan["temoins"].values()):
        raise SystemExit("un témoin sans mutation échoue : aucun compte de mutations")
    for mid, fichier, quoi, avant, apres, essais in MUTATIONS:
        origine = (DEPOT / fichier).read_text(encoding="utf-8")
        n = origine.count(avant)
        x = {"id": mid, "fichier": fichier, "defaut": quoi}
        if n != 1:
            x.update({"etat": "introuvable", "occurrences": n})
            bilan["mutations"].append(x)
            print(f"{mid} introuvable ({n})", file=sys.stderr, flush=True)
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
    print(json.dumps({"jouees": len(joues), "attrapees": sum(m["etat"] == "attrapée" for m in joues),
                      "manquees": [m["id"] for m in joues if m["etat"] == "MANQUÉE"],
                      "autres": [m["id"] for m in bilan["mutations"] if m["etat"] not in ("attrapée", "MANQUÉE")]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
