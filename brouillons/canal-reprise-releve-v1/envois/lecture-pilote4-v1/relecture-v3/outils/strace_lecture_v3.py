#!/usr/bin/env python3
"""Relecture de la v3 : appels système d'écriture des commandes de lecture (modes test et test_final), relevés par
strace, sous chaque interpréteur, avec et sans -B (v1).

Lancé par : /opt/venv-essaim-sim-v1/bin/python -I strace_lecture_v3.py PYTHON…
Fabrique deux courses inventées (M -tentative2 et S) avec les fonctions reprises des relectures précédentes, puis lance,
pour chaque interpréteur : `test --course M`, `test --course S`, `test_final --course-m M --course-s S`,
`test_final --course-m M --sans-seconde-course`, chacune dans une SORTIE neuve, sous
`strace -f -e trace=%file,%desc` réduit aux appels qui créent, ouvrent en écriture, lient, renomment ou retirent.
Tout appel d'écriture hors de SORTIE est une écriture hors de SORTIE. Journal sur la sortie standard (chemins du
dossier de travail remplacés par <travail>).
"""
import sys

sys.dont_write_bytecode = True

import importlib.util  # noqa: E402
import os  # noqa: E402
import pathlib  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402

R3 = pathlib.Path("/var/tmp/relecture-script-lecture-pilote4-v3")
_spec = importlib.util.spec_from_file_location("artefacts_relecture_v3", R3 / "outils" / "artefacts_relecture_v3.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)
A = H.A

ECRITURE = re.compile(r"^(?:\d+ +)?(?:\[pid +\d+\] )?(openat|open|creat|mkdir|mkdirat|link|linkat|unlink|unlinkat|rename|renameat|renameat2|"
                      r"symlink|symlinkat|truncate|chmod|fchmodat|utimensat)\((.*)\) += (-?\d+)")


def ecritures(journal: str):
    out = []
    for ligne in journal.splitlines():
        m = ECRITURE.match(ligne)
        if not m:
            continue
        appel, args, ret = m.groups()
        if appel in ("openat", "open") and not re.search(r"O_WRONLY|O_RDWR|O_CREAT|O_TRUNC|O_APPEND", args):
            continue
        if int(ret) < 0:
            out.append((appel, args, "échec"))
            continue
        out.append((appel, args, "ok"))
    return out


def principal():
    pythons = sys.argv[1:]
    base = R3 / f"travail-strace-{os.getpid()}"
    base.mkdir()
    try:
        publique, secret, absentes = A.fabriquer_banque(20261026)
        banque = base / "banque"
        var = A.ecrire_banque(banque, publique, secret)
        pm = H.fabriquer(base / "cm", H.M, publique, H.plan_mcnemar(publique, "T-m", "F-m", {H.FAMC: (1, 9, 2), H.FAMD: (6, 6, 0)}))
        ps = H.fabriquer(base / "cs", H.S, publique, H.plan_mcnemar(publique, "T-s", "F-s", {H.FAMC: (0, 12, 0), H.FAMD: (10, 0, 1)}))
        env = {k: v for k, v in os.environ.items() if k != A.VAR}
        env[A.VAR] = var
        k = 0
        total_hors = 0
        for py in pythons:
            for b in (["-B"], []):
                for nom, args in (("test M", ["test", "--course", pm]), ("test S", ["test", "--course", ps]),
                                  ("test_final M et S", ["test_final", "--course-m", pm, "--course-s", ps]),
                                  ("test_final M seule", ["test_final", "--course-m", pm, "--sans-seconde-course"])):
                    k += 1
                    sortie = base / f"s{k:03d}"
                    journal = base / f"strace-{k:03d}.txt"
                    r = subprocess.run(["strace", "-f", "-qq", "-o", str(journal), "-e", "trace=%file,%desc", py, "-I", *b,
                                        str(A.SCRIPT), *[str(x) for x in args], str(banque), str(sortie)],
                                       cwd=base, env=env, capture_output=True, text=True)
                    appels = ecritures(journal.read_text(encoding="utf-8", errors="replace"))
                    hors = [a for a in appels if str(sortie) not in a[1]]
                    total_hors += len(hors)
                    print(f"## {py} -I {' '.join(b)} — {nom} : code {r.returncode}, {len(appels)} appels d'écriture, "
                          f"{len(hors)} hors de SORTIE")
                    for a in appels:
                        print("    " + f"{a[0]}({a[1]}) {a[2]}".replace(str(base), "<travail>")[:260])
                    for a in hors:
                        print("    HORS : " + f"{a[0]}({a[1]})".replace(str(base), "<travail>")[:260])
        caches = [p for p in (A.COPIE / "__pycache__", pathlib.Path(A.NOYAU) / "essaim_m3" / "__pycache__",
                              pathlib.Path(A.NOYAU) / "essaim_m3" / "noyau" / "__pycache__") if p.exists()]
        print(f"# bilan : {k} exécutions ; appels d'écriture hors de SORTIE : {total_hors} ; caches : {caches or 'aucun'}")
        return 0 if total_hors == 0 and not caches else 1
    finally:
        shutil.rmtree(base)


if __name__ == "__main__":
    sys.exit(principal())
