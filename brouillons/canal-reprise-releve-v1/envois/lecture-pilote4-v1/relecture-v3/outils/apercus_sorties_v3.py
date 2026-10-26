#!/usr/bin/env python3
"""Relecture de la v3 : aperçus des sorties sur données inventées (fichier test de M ; fichiers holm-quatre de M et de S ;
fichier holm-deux de M), recopiés dans journaux/ pour lecture à l'œil (v1). Lancé par le Python du venv, avec -I ;
le script relu est exécuté par /usr/bin/python3.13 -I -B. Rien d'autre n'est écrit que sous le dossier de la relecture.
"""
import sys

sys.dont_write_bytecode = True

import importlib.util  # noqa: E402
import os  # noqa: E402
import pathlib  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402

R3 = pathlib.Path("/var/tmp/relecture-script-lecture-pilote4-v3")
_spec = importlib.util.spec_from_file_location("artefacts_relecture_v3", R3 / "outils" / "artefacts_relecture_v3.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)
A = H.A


def principal():
    base = R3 / f"travail-apercus-{os.getpid()}"
    base.mkdir()
    try:
        publique, secret, absentes = A.fabriquer_banque(20261026)
        banque = base / "banque"
        var = A.ecrire_banque(banque, publique, secret)
        pm = H.fabriquer(base / "cm", H.M, publique, H.plan_mcnemar(publique, "T-m", "F-m", {H.FAMC: (1, 9, 2), H.FAMD: (6, 6, 0)}))
        ps = H.fabriquer(base / "cs", H.S, publique, H.plan_mcnemar(publique, "T-s", "F-s", {H.FAMC: (0, 12, 0), H.FAMD: (10, 0, 1)}))
        env = {k: v for k, v in os.environ.items() if k != A.VAR}
        env[A.VAR] = var
        for args, sortie in ((["test", "--course", pm], base / "s-test"),
                             (["test_final", "--course-m", pm, "--course-s", ps], base / "s-quatre"),
                             (["test_final", "--course-m", pm, "--sans-seconde-course"], base / "s-deux")):
            r = subprocess.run(["/usr/bin/python3.13", "-I", "-B", str(A.SCRIPT), *map(str, args), str(banque), str(sortie)],
                               cwd=base, env=env, capture_output=True, text=True)
            print(f"{args[0]} : code {r.returncode} ; {r.stdout.strip()[:120]}…")
            for n in sorted(os.listdir(sortie)):
                if n.endswith((".md", ".json")):
                    cible = R3 / "journaux" / f"apercu-v3-{n}"
                    with open(cible, "xb") as f:
                        f.write((sortie / n).read_bytes())
                    print(f"   recopié : journaux/{cible.name}")
    finally:
        shutil.rmtree(base)


if __name__ == "__main__":
    principal()
