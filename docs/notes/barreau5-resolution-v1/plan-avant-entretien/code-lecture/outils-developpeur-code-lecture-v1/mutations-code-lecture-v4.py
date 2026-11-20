"""Passage de mutations v4 du code de lecture du barreau 5 (développeur du code de lecture, 20 novembre 2026) : les règles
de l'addendum 1 au texte (`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md`,
2afa2186…) que le code applique, défaites une à une (couples A à D de `verification-corrections-code-lecture-v1.md`, et
les règles du point 1 que le code faisait déjà). Même procédé que `mutations-code-lecture-v3.py` : copie de travail
unique ; témoins sans mutation exigés verts ; « attrapée » si pytest rend le code 1 ; chaque « avant » paraît une fois
exactement dans le fichier d'origine, sinon « introuvable ».

Usage : python -B mutations-code-lecture-v4.py COPIE BASETEMP [IDENTIFIANTS…]  — imprime le bilan en JSON.
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
L = "src/controle_ia/barreau5_familles/lecture_v1.py"
EL = "tests/test_barreau5_familles_lecture_v1.py"
A_COPIER = ["src", "tests/conftest.py", EL, "prereg/T0.6-organismes-config-7b-v1.json",
            "prereg/T0.6-organismes-config-7b-v1.json.sha256",
            "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md", "pyproject.toml",
            "docs/sources/invites-2606.08892-v1"]

MUTATIONS = [
    ("M01", L, "point 2 défait : chaque membre sur ses propres tâches à coût lisible (lecture écartée)",
     '        m[f] = {membre: {"m": float(np.mean([par_membre[membre][t] for t in retenues])) if retenues else None,\n'
     '                         "taches": len(retenues)} for membre in presents}',
     '        m[f] = {membre: {"m": float(np.mean(list(par_membre[membre].values()))) if par_membre[membre] else None,\n'
     '                         "taches": len(par_membre[membre])} for membre in presents}', [EL]),
    ("M02", L, "point 2, cas limite : motif non écrit",
     '"motif": None if retenues else "aucune tâche retenue : famille absente de M1 et de M3"}', '"motif": None}', [EL]),
    ("M03", L, "point 2, règle 5 : nombre de tâches retenues non écrit", '"taches_retenues": len(retenues), ', "", [EL]),
    ("M04", L, "point 3 défait : borne de la phrase E au plus grand écart",
     "f\"{_x(SEUIL_EMPREINTE * sep['delta_app'])} n'est pas exclue.\")", "f\"{_x(rap['bornes_E3']['max'])} n'est pas exclue.\")",
     [EL]),
    ("M05", L, "point 1, règle 2 : niveau de D sans M1 ni M3",
     'return {"code": "D", "niveau": _niveau_min(manip["M1"], manip["M3"], E3), "motifs": motifs}',
     'return {"code": "D", "niveau": _niveau_min(E3), "motifs": motifs}', [EL]),
    ("M06", L, "point 1, règle 2 : niveau de C sans M1 ni M3",
     'return {"code": "C", "niveau": _niveau_min(manip["M1"], manip["M3"], E3), "motifs": []}',
     'return {"code": "C", "niveau": _niveau_min(E3), "motifs": []}', [EL]),
    ("M07", L, "point 1, règle 2 : niveau de S sans M1 ni M3",
     'return {"code": "S", "niveau": _niveau_min(manip["M1"], manip["M3"], E1, E2a, E2b, E3), "motifs": []}',
     'return {"code": "S", "niveau": _niveau_min(E1, E2a, E2b, E3), "motifs": []}', [EL]),
    ("M08", L, "point 1, règle 1 : famille sans saboteur ôtée aussi de M3",
     'if haut in m[f] and "jumeau" in m[f] and "sur_saboteur" in fam[f] and m[f][haut]["m"] is not None',
     'if haut in m[f] and "jumeau" in m[f] and "sur_saboteur" in fam[f] and "saboteur" in fam[f] and m[f][haut]["m"] is not None',
     [EL]),
    ("M09", L, "point 1, règle 4 : motif sans « niveau non atteignable »",
     '        manque = [e if not manip[e]["non_atteignable"] else', "        manque = [e if True else", [EL]),
    ("M10", L, "point 1, règle 3 : niveau absent du nom de l'issue",
     '"nom": NOMS_ISSUES[i["code"]] + (", au niveau de 95 %" if i["niveau"] == "95"', '"nom": NOMS_ISSUES[i["code"]] + (", au niveau de 95 %" if False',
     [EL]),
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
                        str(base / nom), *essais], cwd=str(copie), env=env, capture_output=True, text=True)
    lignes = [x for x in r.stdout.splitlines() if x.strip() and not x.startswith("PROGRES")]
    echec = [x for x in lignes if x.startswith(("FAILED", "ERROR"))]
    return {"code": r.returncode, "duree_s": round(time.time() - debut, 1), "fin": lignes[-1] if lignes else "",
            "premier_echec": echec[0] if echec else None}


def main(argv: list[str]) -> int:
    copie, base = Path(argv[0]), Path(argv[1])
    choix = set(argv[2:])
    copier(copie)
    base.mkdir(parents=True, exist_ok=False)
    bilan = {"temoins": {"EL": jouer(copie, base, "temoin-EL", [EL])}, "mutations": []}
    print(f"témoin EL : code {bilan['temoins']['EL']['code']} ({bilan['temoins']['EL']['fin']})", file=sys.stderr, flush=True)
    if bilan["temoins"]["EL"]["code"] != 0:
        print(json.dumps(bilan, ensure_ascii=False, indent=1))
        raise SystemExit("le témoin sans mutation échoue : aucun compte de mutations")
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
