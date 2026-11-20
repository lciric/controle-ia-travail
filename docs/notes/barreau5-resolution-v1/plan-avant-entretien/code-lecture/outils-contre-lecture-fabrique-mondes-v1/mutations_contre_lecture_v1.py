"""Mutations du contre-lecteur sur la fabrique des mondes et le juge de l'épreuve à vérité plantée (barreau 5) — v1.

Outil du contre-lecteur (Claude Fable 5.2), 20 novembre 2026. Aucune donnée ; le programme de lecture n'est ni importé ni
joué. Huit mutations absentes de la liste du développeur (`outils-developpeur-fabrique-mondes-v1/
mutations_fabrique_juge_v1.py`), jouées contre ses essais, par le même montage que le sien : pour chaque mutation, un
paquet minimal copié sous `<racine>/<id>/` (fabrique, juge, essais, `pytest.ini` vide), `PYTHONPATH` sur ce seul paquet.
Témoins (R5) : « t0 » sans mutation doit passer ; « t1 », import cassé, doit échouer. Une mutation est tuée si le code de
sortie des essais n'est pas nul.

Usage : `.venv/bin/python -B <ce fichier> --depot <dépôt> --racine /dev/shm/b5f-contre-lecture-fabrique-v1/mutations
--sortie <résultats.json>`. La racine ne doit pas exister ; elle s'efface ensuite par son chemin écrit en toutes lettres.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

FABRIQUE = "src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py"
JUGE = "src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py"
ESSAIS = "tests/test_barreau5_familles_epreuve_verite_plantee_v1.py"

# (identifiant, module, texte d'origine, texte muté, ce que la mutation casse, prédiction écrite avant le passage)
MUTATIONS = (
    ("t0", None, None, None, "témoin sain : aucune mutation", "passe"),
    ("t1", "F", "from __future__ import annotations\n\nimport argparse",
     "from __future__ import annotations\n\nraise ImportError(\"temoin\")\nimport argparse",
     "témoin cassé : l'import de la fabrique échoue", "tuée"),
    ("c1", "F", "else rng.normal(0.0, SIGMA_ZETA_LIBRE, off[-1]))",
     "else np.random.default_rng(11).normal(0.0, SIGMA_ZETA_LIBRE, off[-1]))",
     "V0 (régime libre) : le bruit par jeton est le même pour tous les membres (point 11 : « bruits indépendants d'un "
     "membre à l'autre », au niveau des scores par jeton)", "survit"),
    ("c2", "F", "lect = {r: b + _xi(rng) / math.sqrt(2.0) for r in ROLES}",
     "lect = {r: b + (2.0 if r == \"sur\" else 1.0) * _xi(rng) / math.sqrt(2.0) for r in ROLES}",
     "V0 : le sur-saboteur n'a plus la loi des deux autres membres (point 11 : « de même loi pour les trois membres »)",
     "survit"),
    ("c3", "F", "if pjs <= 0 or pss <= 0:", "if pjs < 0 or pss < 0:",
     "règle d'échec de E2a : un produit nul n'est plus « non positif » dans la vérité", "tuée"),
    ("c4", "F", "poser(\"etiquettes.json\", table_octets)", "_ecrire(arbre / \"etiquettes.json\", table_octets)",
     "V7, premier cas : la table est dans l'arbre sans être inventoriée (le refus viendrait de l'inventaire, non de la "
     "garde des étiquettes)", "survit"),
    ("c5", "F", "\"saboteur\": [0.0, lam_j + e1, 0.0]}", "\"saboteur\": [gam, lam_j + e1, 0.0]}",
     "V9 : le saboteur porte une part sur ĝ ; l'écart ne disparaît plus exactement en E2a", "tuée"),
    ("c6", "J", "if issue in (\"D\", \"C\") and r.get(\"niveau\") != 99:", "if issue in (\"D\", \"C\") and r.get(\"niveau\") != 95:",
     "V10, nœud 6 : une issue D ou C exigée au niveau de 95 % (addendum 1, point 1 : E2a ne fonde ni D ni C)", "survit"),
    ("c7", "J", "return _issue_au_niveau(r, a, \"D\") and bool(m) and m <= {\"E2a\", \"E2b\"}",
     "return _issue_au_niveau(r, a, \"D\") and m <= {\"E2a\", \"E2b\"}",
     "V3 : une issue D sans aucun motif compte pour « au seul motif « force non écartée » »", "survit"),
    ("c8", "J", "(\"V0\", \"épreuve E3 « contraire » dans 20 mondes au plus\", \"au plus\", 20, p_e3_contraire),",
     "(\"V0\", \"épreuve E3 « contraire » dans 20 mondes au plus\", \"au plus\", 20, p_e3_separe),",
     "V0 : la règle « contraire » compte les « séparé »", "tuée"),
)


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def preparer(depot: Path, dossier: Path, module, ancien, nouveau) -> dict:
    src = dossier / "src" / "controle_ia" / "barreau5_familles"
    src.mkdir(parents=True)
    (dossier / "src" / "controle_ia" / "__init__.py").write_bytes(b"")
    (src / "__init__.py").write_bytes(b"")
    (dossier / "tests").mkdir()
    (dossier / "tests" / Path(ESSAIS).name).write_bytes((depot / ESSAIS).read_bytes())
    (dossier / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    info = {}
    for code, rel in (("F", FABRIQUE), ("J", JUGE)):
        texte = (depot / rel).read_text(encoding="utf-8")
        if code == module:
            n = texte.count(ancien)
            if n != 1:
                raise SystemExit(f"mutation mal écrite : le texte d'origine est {n} fois dans {rel}")
            texte = texte.replace(ancien, nouveau)
        octets = texte.encode("utf-8")
        (src / Path(rel).name).write_bytes(octets)
        info[code] = _sha(octets)
    return info


def jouer(dossier: Path, delai: int) -> dict:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(dossier / "src")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["B5F_ESSAIS_DOSSIER"] = str(dossier / "essais")
    cmd = [sys.executable, "-B", "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", "-c", str(dossier / "pytest.ini"),
           "--rootdir", str(dossier), str(dossier / "tests" / Path(ESSAIS).name)]
    t0 = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=dossier, env=env, capture_output=True, text=True, timeout=delai)
        code, sortie = p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired as e:
        code, sortie = "delai", (e.stdout or "") if isinstance(e.stdout, str) else ""
    (dossier / "sortie-pytest.txt").write_text(sortie, encoding="utf-8")
    lignes = [x for x in sortie.splitlines() if x.startswith(("FAILED", "ERROR")) or " passed" in x or " failed" in x
              or " error" in x]
    return {"code": code, "duree_s": round(time.monotonic() - t0, 1), "resume": lignes[-3:]}


def une(depot: Path, racine: Path, m, delai: int) -> dict:
    ident, module, ancien, nouveau, quoi, prediction = m
    d = racine / ident
    info = preparer(depot, d, module, ancien, nouveau)
    r = jouer(d, delai)
    r.update({"id": ident, "module": {"F": "fabrique", "J": "juge", None: None}[module], "quoi": quoi,
              "prediction": prediction, "tuee": r["code"] != 0, "sha256_fabrique_jouee": info["F"],
              "sha256_juge_joue": info["J"]})
    return r


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--depot", required=True)
    ap.add_argument("--racine", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--delai", type=int, default=1500)
    ap.add_argument("--ouvriers", type=int, default=3)
    ap.add_argument("--verifier", action="store_true", help="compte seulement chaque texte d'origine, sans rien jouer")
    a = ap.parse_args(argv)
    depot, racine, sortie = Path(a.depot).resolve(), Path(a.racine), Path(a.sortie)
    sources = {"F": (depot / FABRIQUE).read_text(encoding="utf-8"), "J": (depot / JUGE).read_text(encoding="utf-8")}
    fautes = [(m[0], sources[m[1]].count(m[2])) for m in MUTATIONS if m[1] and sources[m[1]].count(m[2]) != 1]
    if a.verifier or fautes:
        print(json.dumps({"mutations": len(MUTATIONS), "mal_ecrites": fautes}, ensure_ascii=False))
        return 0 if not fautes else 2
    if racine.exists():
        raise SystemExit(f"{racine} existe déjà")
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    racine.mkdir(parents=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.ouvriers) as pool:
        resultats = list(pool.map(lambda m: une(depot, racine, m, a.delai), MUTATIONS))
    res = {"format": "b5f-mutations-contre-lecture-fabrique-juge-v1",
           "depot_fichiers": {rel: _sha((depot / rel).read_bytes()) for rel in (FABRIQUE, JUGE, ESSAIS)},
           "outil_sha256": _sha(Path(__file__).read_bytes()), "python": sys.version.split()[0], "mutations": resultats}
    temoins = {r["id"]: r["tuee"] for r in resultats if r["id"] in ("t0", "t1")}
    if temoins != {"t0": False, "t1": True}:
        res["arret"] = f"témoins hors de l'attendu ({temoins}) : rien n'est conclu"
    mutantes = [r for r in resultats if r["id"] not in ("t0", "t1")]
    res["bilan"] = {"mutations": len(mutantes), "tuees": sum(r["tuee"] for r in mutantes),
                    "survivantes": [r["id"] for r in mutantes if not r["tuee"]],
                    "predictions_justes": sum((r["prediction"] == "tuée") == r["tuee"] for r in mutantes)}
    octets = json.dumps(res, ensure_ascii=False, indent=1).encode("utf-8")
    with open(sortie, "xb") as fh:
        fh.write(octets)
    print(json.dumps({"bilan": res["bilan"], "arret": res.get("arret"), "sha256": _sha(octets)}, ensure_ascii=False))
    return 0 if "arret" not in res else 2


if __name__ == "__main__":
    sys.exit(main())
