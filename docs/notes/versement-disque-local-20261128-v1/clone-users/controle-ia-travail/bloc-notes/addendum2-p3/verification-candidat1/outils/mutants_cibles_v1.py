"""Rejoue, sur des copies du module v4 et des tests v4, les mutants visés par les trois tests ajoutés au v4
(vérification mécanique du candidat 1 de l'addendum 2 de P3).

Listes lues comme données (`ast.literal_eval`, aucun import ni exécution des fichiers sources), après vérification de
leurs empreintes : `module-v3/outils-revue/mutants_v2.py` (G6-01, G6-02) et `verification-v3/outils/mutants_verif_v3.py`
(VV-G6-01, VV-G6-02, VV-F-01, VV-F-02, VV-D3-04).

Pour chaque mutant : dossier `mutants/<id>/` (module muté, copie des tests v4, différence), chaque motif présent
exactement une fois, compilation en mémoire, puis pytest depuis la racine du dépôt, sous la garde R1 v2b, `-B`, sans
cache, `--basetemp` et `TMPDIR` sous `tmp/bt/<id>/`. Mode « nouveaux » : les trois tests ajoutés seulement (`-k`) ;
mode « suite » : la suite entière. Résultats : `journaux/mutants-cibles-<mode>.jsonl`.

Usage : python -I -B mutants_cibles_v1.py <mode : nouveaux|suite> ID …
"""
import ast
import concurrent.futures as cf
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
V = ICI.parent                                   # verification-candidat1/
S = V.parent                                     # addendum2-p3/
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
MODULE, TESTS = S / "module-v4" / "audit_verdict_p3_v1.py", S / "module-v4" / "test_audit_verdict_p3_v1.py"
SHA_MODULE = "967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d"
SHA_TESTS = "f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07"
LISTES = {S / "module-v3" / "outils-revue" / "mutants_v2.py": "d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c",
          S / "verification-v3" / "outils" / "mutants_verif_v3.py": "6416f5b745dfe420306224b6c5f1bb55e708e4cd422c8f9da273de38daa24da7"}
GARDE = S / "module-v3" / "outils-revue"
NOUVEAUX = ("test_garde_6_au_lancement_exception_du_chargeur_convertie or test_garde_7_compte_de_chacune_des_cinq_formes"
            " or test_declencheur_3_E0_petit_non_nul")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mutants():
    tous = {}
    for chemin, attendu in LISTES.items():
        if sha(chemin) != attendu:
            raise SystemExit(f"empreinte inattendue : {chemin}")
        arbre = ast.parse(chemin.read_text(encoding="utf-8"))
        for n in arbre.body:
            if isinstance(n, ast.Assign) and any(isinstance(c, ast.Name) and c.id == "MUTANTS" for c in n.targets):
                for ident, famille, regle, remplacements in ast.literal_eval(n.value):
                    tous[ident] = (regle, remplacements, chemin.name)
    return tous


def lancer(mode, ident, regle, remplacements, origine):
    d = V / "mutants" / ident
    d.mkdir(parents=True, exist_ok=True)
    texte = MODULE.read_text(encoding="utf-8")
    for ancien, nouveau in remplacements:
        if texte.count(ancien) != 1:
            return {"id": ident, "mode": mode, "etat": "motif absent ou multiple", "motif": ancien[:80]}
        texte = texte.replace(ancien, nouveau)
    compile(texte, "audit_verdict_p3_v1.py", "exec")
    (d / "audit_verdict_p3_v1.py").write_text(texte, encoding="utf-8")
    (d / "test_audit_verdict_p3_v1.py").write_bytes(TESTS.read_bytes())
    diff = "".join(difflib.unified_diff(MODULE.read_text(encoding="utf-8").splitlines(True), texte.splitlines(True),
                                        "v4/audit_verdict_p3_v1.py", f"{ident}/audit_verdict_p3_v1.py"))
    (d / "difference.diff").write_text(diff, encoding="utf-8")
    bt = V / "tmp" / "bt" / f"{ident}-{mode}"
    bt.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONHOME")}
    env.update({"REVUE_JOURNAL_R1": str(d / f"r1-{mode}.jsonl"), "TMPDIR": str(bt), "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONPATH": f"src:{GARDE}"})
    cmd = [PY, "-B", "-m", "pytest", "-q", "-rf", "-p", "no:cacheprovider", "-p", "garde_r1_v2b",
           f"--basetemp={bt / 'base'}", str(d / "test_audit_verdict_p3_v1.py")]
    if mode == "nouveaux":
        cmd += ["-k", NOUVEAUX]
    p = subprocess.run(cmd, cwd=DEPOT, env=env, capture_output=True, text=True)
    (d / f"pytest-{mode}.log").write_text(p.stdout + p.stderr + f"\ncode {p.returncode}\n", encoding="utf-8")
    echecs = sorted(set(re.findall(r"^FAILED \S+::(\S+)", p.stdout, re.M)))
    bilan = (re.findall(r"^=*\s*(.*(?:passed|failed|error).*?)\s*=*$", p.stdout, re.M) or [""])[-1]
    refus = 0
    jr = d / f"r1-{mode}.jsonl"
    if jr.exists():
        refus = sum(1 for l in jr.read_text(encoding="utf-8").splitlines() if json.loads(l)["refus"])
    return {"id": ident, "mode": mode, "origine": origine, "regle": regle, "sha_mutant": sha(d / "audit_verdict_p3_v1.py"),
            "code": p.returncode, "bilan": bilan, "echecs": echecs, "refus_r1": refus,
            "etat": "tué" if p.returncode == 1 and echecs else ("survit" if p.returncode == 0 else "autre")}


def main():
    mode, ids = sys.argv[1], sys.argv[2:]
    assert mode in ("nouveaux", "suite")
    if sha(MODULE) != SHA_MODULE or sha(TESTS) != SHA_TESTS:
        raise SystemExit("empreinte du module ou des tests v4 inattendue")
    tous = mutants()
    tous["BASE"] = ("cas sain : module v4 sans mutation", [], "aucune")
    sortie = V / "journaux" / f"mutants-cibles-{mode}.jsonl"
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        futurs = [ex.submit(lancer, mode, i, *tous[i]) for i in ids]
        for f in futurs:
            r = f.result()
            with open(sortie, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(json.dumps(r, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
