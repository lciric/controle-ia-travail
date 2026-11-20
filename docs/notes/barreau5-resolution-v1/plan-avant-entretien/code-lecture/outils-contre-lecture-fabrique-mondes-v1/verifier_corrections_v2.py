"""Vérification des corrections de la fabrique, du juge et du traducteur (barreau 5) — v2.

Outil du contre-lecteur (Claude Fable 5.2), 20 novembre 2026. Aucune donnée ; le programme de lecture n'est ni importé ni
joué.

1. Empreintes des fichiers en vigueur.
2. La fabrique d'origine (`f41377ae…`) est retrouvée dans l'historique git ; mes seize couples F lui sont appliqués ;
   l'empreinte doit être `520b8215…`. La fabrique en vigueur ne doit en différer que par des commentaires et la docstring
   de tête : égalité des arbres syntaxiques, docstring de module ôtée ; le diff de texte est écrit à part.
3. Le traducteur versé sous `src/` et le mien : même arbre syntaxique, docstring de module ôtée ; mêmes octets après elle.
4. Mes huit mutations (c4 récrite sur le nom neuf de la table) contre les essais en vigueur, dans une copie entière de
   `src/controle_ia` ; puis, à part, la mutation de l'ordre des noms opaques dans un paquet entier et dans un paquet
   minimal (sans `engagement_v1`).

Usage : `.venv/bin/python -B <ce fichier> --depot <dépôt> --racine /dev/shm/b5f-verification-fabrique-v2 --sortie
<résultats.json> --diff <diff.txt>`.
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import difflib
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
FABRIQUE = "src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py"
JUGE = "src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py"
TRADUCTEUR = "src/controle_ia/barreau5_familles/traducteur_verite_plantee_v1.py"
ESSAIS = "tests/test_barreau5_familles_epreuve_verite_plantee_v1.py"
ORIGINE = "f41377ae202590bb5c05f13bd0ce66bf84dcb5525e10a4f18a753a786e5cc692"
APRES_COUPLES = "520b821543b1624893593403be73b9aa049b46483583ac975cc83982aef69317"

MUTATIONS = (
    ("t0", None, None, None, "témoin sain"),
    ("t1", "F", "from __future__ import annotations\n\nimport argparse",
     "from __future__ import annotations\n\nraise ImportError(\"temoin\")\nimport argparse", "témoin cassé"),
    ("c1", "F", "else rng.normal(0.0, SIGMA_ZETA_LIBRE, off[-1]))",
     "else np.random.default_rng(11).normal(0.0, SIGMA_ZETA_LIBRE, off[-1]))", "V0 : bruit par jeton commun aux membres"),
    ("c2", "F", "lect = {r: b + _xi(rng) / math.sqrt(2.0) for r in ROLES}",
     "lect = {r: b + (2.0 if r == \"sur\" else 1.0) * _xi(rng) / math.sqrt(2.0) for r in ROLES}",
     "V0 : le sur-saboteur n'a plus la loi des deux autres"),
    ("c3", "F", "if pjs <= 0 or pss <= 0:", "if pjs < 0 or pss < 0:", "E2a : produit nul tenu pour positif"),
    ("c4", "F", "poser(\"scores/etiquettes-pli0.json\", table_octets)",
     "_ecrire(arbre / \"scores/etiquettes-pli0.json\", table_octets)", "V7, premier cas : table hors de l'inventaire"),
    ("c5", "F", "\"saboteur\": [0.0, lam_j + e1, 0.0]}", "\"saboteur\": [gam, lam_j + e1, 0.0]}",
     "V9 : le saboteur porte une part sur ĝ"),
    ("c6", "J", "if issue in (\"D\", \"C\") and r.get(\"niveau\") != 99:",
     "if issue in (\"D\", \"C\") and r.get(\"niveau\") != 95:", "V10 : D ou C exigée à 95 %"),
    ("c7", "J", "return _issue_au_niveau(r, a, \"D\") and bool(m) and m <= {\"E2a\", \"E2b\"}",
     "return _issue_au_niveau(r, a, \"D\") and m <= {\"E2a\", \"E2b\"}", "V3 : D sans motif compte"),
    ("c8", "J", "(\"V0\", \"épreuve E3 « contraire » dans 20 mondes au plus\", \"au plus\", 20, p_e3_contraire),",
     "(\"V0\", \"épreuve E3 « contraire » dans 20 mondes au plus\", \"au plus\", 20, p_e3_separe),",
     "V0 : la règle « contraire » compte les « séparé »"),
    ("n1", "F", "return {a: f\"X-{k + 1:02d}\" for k, a in enumerate(ordre)}",
     "return {a: f\"X-{k + 1:02d}\" for k, a in enumerate(reversed(ordre))}", "ordre des noms opaques renversé"),
    ("n1-minimal", "F", "return {a: f\"X-{k + 1:02d}\" for k, a in enumerate(ordre)}",
     "return {a: f\"X-{k + 1:02d}\" for k, a in enumerate(reversed(ordre))}",
     "ordre des noms opaques renversé, paquet minimal (sans engagement_v1)"),
)


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _arbre_sans_docstring(texte: str) -> str:
    a = ast.parse(texte)
    if a.body and isinstance(a.body[0], ast.Expr) and isinstance(getattr(a.body[0], "value", None), ast.Constant) \
            and isinstance(a.body[0].value.value, str):
        a.body = a.body[1:]
    return ast.dump(a)


def _apres_docstring(octets: bytes) -> bytes:
    texte = octets.decode("utf-8")
    fin = texte.index('"""', texte.index('"""') + 3) + 3
    return texte[fin:].encode("utf-8")


def origine_git(depot: Path) -> tuple[str, str] | None:
    commits = subprocess.run(["git", "-C", str(depot), "log", "--format=%H", "--", FABRIQUE], capture_output=True,
                             text=True, check=True).stdout.split()
    for c in commits:
        v = subprocess.run(["git", "-C", str(depot), "show", f"{c}:{FABRIQUE}"], capture_output=True)
        if v.returncode == 0 and _sha(v.stdout) == ORIGINE:
            return c, v.stdout.decode("utf-8")
    return None


def jouer(depot: Path, racine: Path, m) -> dict:
    ident, module, ancien, nouveau, quoi = m
    d = racine / ident
    minimal = ident.endswith("-minimal")
    paquet = d / "src" / "controle_ia"
    if minimal:
        (paquet / "barreau5_familles").mkdir(parents=True)
        (paquet / "__init__.py").write_bytes(b"")
        (paquet / "barreau5_familles" / "__init__.py").write_bytes(b"")
        for rel in (FABRIQUE, JUGE, TRADUCTEUR):
            (d / rel).write_bytes((depot / rel).read_bytes())
    else:
        shutil.copytree(depot / "src" / "controle_ia", paquet, ignore=shutil.ignore_patterns("__pycache__"))
    if module:
        p = d / (FABRIQUE if module == "F" else JUGE)
        texte = p.read_text(encoding="utf-8")
        n = texte.count(ancien)
        if n != 1:
            return {"id": ident, "quoi": quoi, "mal_ecrite": n}
        p.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
    (d / "tests").mkdir()
    (d / "tests" / Path(ESSAIS).name).write_bytes((depot / ESSAIS).read_bytes())
    (d / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    env = dict(os.environ)
    env.update({"PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1", "B5F_ESSAIS_DOSSIER": str(d / "essais")})
    cmd = [sys.executable, "-B", "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", "-c", str(d / "pytest.ini"),
           "--rootdir", str(d), str(d / "tests" / Path(ESSAIS).name)]
    p = subprocess.run(cmd, cwd=d, env=env, capture_output=True, text=True, timeout=1800)
    sortie = p.stdout + p.stderr
    lignes = [x for x in sortie.splitlines() if x.startswith(("FAILED", "ERROR")) or " passed" in x or " failed" in x
              or " error" in x]
    return {"id": ident, "quoi": quoi, "code": p.returncode, "tuee": p.returncode != 0, "resume": lignes[-2:]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", required=True)
    ap.add_argument("--racine", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--diff", required=True)
    a = ap.parse_args(argv)
    depot, racine = Path(a.depot).resolve(), Path(a.racine)
    for p in (racine, Path(a.sortie), Path(a.diff)):
        if p.exists():
            raise SystemExit(f"{p} existe déjà")
    res = {"format": "b5f-verification-corrections-fabrique-v2",
           "empreintes": {rel: _sha((depot / rel).read_bytes()) for rel in (FABRIQUE, JUGE, TRADUCTEUR, ESSAIS)}}
    spec = importlib.util.spec_from_file_location("couples_corrections_v1", ICI / "couples_corrections_v1.py")
    couples = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(couples)
    actuel = (depot / FABRIQUE).read_text(encoding="utf-8")
    trouve = origine_git(depot)
    if trouve is None:
        res["fabrique"] = {"origine_dans_git": False}
    else:
        commit, texte = trouve
        for c in couples.COUPLES:
            if c["fichier"] == FABRIQUE:
                assert texte.count(c["avant"]) == 1, c["id"]
                texte = texte.replace(c["avant"], c["apres"])
        diff = list(difflib.unified_diff(texte.splitlines(), actuel.splitlines(), "apres-les-16-couples", "en-vigueur",
                                         lineterm="", n=1))
        Path(a.diff).write_text("\n".join(diff) + "\n", encoding="utf-8")
        res["fabrique"] = {"origine_dans_git": True, "commit": commit,
                           "apres_les_16_couples_sha256": _sha(texte.encode("utf-8")),
                           "egale_a_520b8215": _sha(texte.encode("utf-8")) == APRES_COUPLES,
                           "meme_arbre_syntaxique_hors_docstring": _arbre_sans_docstring(texte) == _arbre_sans_docstring(actuel),
                           "lignes_du_diff": len(diff)}
    mien = (ICI / "traducteur_resultat_vers_rendu_v1.py").read_bytes()
    verse = (depot / TRADUCTEUR).read_bytes()
    res["traducteur"] = {"mien_sha256": _sha(mien), "verse_sha256": _sha(verse),
                         "meme_arbre_syntaxique_hors_docstring":
                             _arbre_sans_docstring(mien.decode("utf-8")) == _arbre_sans_docstring(verse.decode("utf-8")),
                         "memes_octets_apres_la_docstring": _apres_docstring(mien) == _apres_docstring(verse),
                         "corps_sha256": _sha(_apres_docstring(verse))}
    racine.mkdir(parents=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        res["mutations"] = list(pool.map(lambda m: jouer(depot, racine, m), MUTATIONS))
    octets = json.dumps(res, ensure_ascii=False, indent=1).encode("utf-8")
    with open(a.sortie, "xb") as fh:
        fh.write(octets)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
