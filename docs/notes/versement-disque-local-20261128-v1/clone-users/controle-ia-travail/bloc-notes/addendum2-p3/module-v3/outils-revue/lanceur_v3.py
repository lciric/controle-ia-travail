"""Lanceur de la campagne de mutants de la contre-lecture du code v2 (addendum 2 de P3).

COPIE ADAPTÉE AU MODULE v3 (dossier `module-v3/outils-revue/`, copie de `revue-v2/outils/lanceur_v2.py`, sha256
`4a4023378a2558ed040c0c2c5868b6fee1e7fe281cb2983832acdaf6e920503f`). Liste de mutants inchangée (`mutants_v2.py`,
copie octet pour octet, `d9c038e6…`). Seuls changent : la base (module et tests v3, empreintes lues dans leurs
compagnons), le fichier de résultats (`resultats-mutants-v3.jsonl`), les dossiers temporaires (sous
`module-v3/tmp/`, supprimés : le dossier d'un mutant tué est effacé après son lancement ; la fin du journal d'un
mutant non tué est gardée dans sa ligne de résultat), la garde R1 (`garde_r1_v2b`, la version corrigée du
contre-lecteur, CV2-11). Suite entière, sans `-x`, trois mutants à la fois, comme l'original.

Pour chaque mutant de `mutants_v2.MUTANTS` : copie de base (empreintes vérifiées), remplacements appliqués dans l'ordre
(chaque motif présent exactement une fois au moment de son application), compilation, dossier `mutants/<id>/` (module
muté, copie inchangée des tests, différence), puis la SUITE ENTIÈRE des tests de la copie (sans `-x`), depuis la racine
du dépôt, sous la garde R1 de la revue (`garde_r1_v2`), `-B`, sans cache, `--basetemp` et `TMPDIR` dans `tmp/<id>/`.
« tué » : au moins un test échoue ; « SURVIT » : les 118 tests passent. Résultats : `journaux/resultats-mutants-v2.jsonl`
(une ligne par mutant ; un mutant déjà présent n'est pas relancé).

Usage : python lanceur_v2.py [--preparer] [--travailleurs N] [ID …]
"""
import argparse
import concurrent.futures as cf
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
REVUE = ICI.parent
sys.path.insert(0, str(ICI))
from mutants_v2 import MUTANTS  # noqa: E402

PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
BASE_MODULE = REVUE / "audit_verdict_p3_v1.py"
BASE_TESTS = REVUE / "test_audit_verdict_p3_v1.py"
SHA_MODULE = (REVUE / "audit_verdict_p3_v1.py.sha256").read_text(encoding="utf-8").split()[0]
SHA_TESTS = (REVUE / "test_audit_verdict_p3_v1.py.sha256").read_text(encoding="utf-8").split()[0]
RESULTATS = ICI / "resultats-mutants-v3.jsonl"
VERROU = threading.Lock()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def appliquer(texte, remplacements):
    for ancien, nouveau in remplacements:
        n = texte.count(ancien)
        if n != 1:
            raise ValueError(f"motif présent {n} fois : {ancien[:90]!r}")
        texte = texte.replace(ancien, nouveau)
    return texte


def preparer(mid, remplacements):
    base = BASE_MODULE.read_text(encoding="utf-8")
    texte = appliquer(base, remplacements)
    if texte == base:
        raise ValueError("mutant identique à la base")
    compile(texte, f"mutants/{mid}/audit_verdict_p3_v1.py", "exec")
    d = REVUE / "tmp" / "mutants-revue" / mid
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "audit_verdict_p3_v1.py").write_text(texte, encoding="utf-8")
    shutil.copyfile(BASE_TESTS, d / "test_audit_verdict_p3_v1.py")
    diff = "".join(difflib.unified_diff(base.splitlines(True), texte.splitlines(True), "base/audit_verdict_p3_v1.py",
                                        f"mutants/{mid}/audit_verdict_p3_v1.py", n=1))
    (d / "difference.diff").write_text(diff, encoding="utf-8")
    return d


def lancer(mid, famille, regle, remplacements):
    debut = time.time()
    try:
        d = preparer(mid, remplacements)
    except Exception as e:  # motif invalide : consigné, jamais lancé
        return {"id": mid, "famille": famille, "regle": regle, "etat": "motif invalide", "detail": str(e)}
    tmp = REVUE / "tmp" / "bt-revue" / mid
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    journal_r1 = d / "r1.jsonl"
    env = {**os.environ, "REVUE_JOURNAL_R1": str(journal_r1), "PYTHONPATH": f"src:{ICI}", "PYTHONDONTWRITEBYTECODE": "1",
           "TMPDIR": str(tmp)}
    cmd = [PY, "-B", "-m", "pytest", "-q", "-rfE", "-p", "no:cacheprovider", "-p", "garde_r1_v2b",
           f"--basetemp={tmp / 'bt'}", str(d / "test_audit_verdict_p3_v1.py")]
    try:
        r = subprocess.run(cmd, cwd=DEPOT, env=env, capture_output=True, text=True, timeout=3000)
        code, sortie = r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired as e:
        code, sortie = "délai", (e.stdout or "") if isinstance(e.stdout, str) else ""
    (d / "pytest.log").write_text(sortie, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    echecs = re.findall(r"^(?:FAILED|ERROR) \S+::(\S+)(?: - (.*))?$", sortie, flags=re.M)
    resume = re.findall(r"^=*\s*(\d+ (?:passed|failed|error).*?)\s*=*$", sortie, flags=re.M)
    refus = 0
    if journal_r1.exists():
        refus = sum(1 for l in journal_r1.read_text(encoding="utf-8").splitlines() if '"refus": true' in l)
    etat = "SURVIT" if code == 0 else "tué" if code == 1 else f"erreur ({code})"
    r = {"id": mid, "famille": famille, "regle": regle, "etat": etat, "code": code,
         "echecs": [x[0] for x in echecs], "premier_motif": (echecs[0][1] or "")[:300] if echecs else None,
         "resume": resume[-1] if resume else None, "duree_s": round(time.time() - debut, 1), "refus_R1": refus,
         "sha_mutant": sha(d / "audit_verdict_p3_v1.py")}
    if etat != "tué":
        r["fin_du_journal"] = sortie[-3000:]
    shutil.rmtree(d, ignore_errors=True)
    return r


def deja_faits():
    if not RESULTATS.exists():
        return set()
    return {json.loads(l)["id"] for l in RESULTATS.read_text(encoding="utf-8").splitlines() if l.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preparer", action="store_true")
    ap.add_argument("--travailleurs", type=int, default=3)
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    if a.travailleurs > 3:
        raise SystemExit("trois mutants à la fois au plus")
    if sha(BASE_MODULE) != SHA_MODULE or sha(BASE_TESTS) != SHA_TESTS:
        raise SystemExit("copie de base altérée : arrêt")
    ids = [m[0] for m in MUTANTS]
    if len(ids) != len(set(ids)):
        raise SystemExit("identifiants de mutants en double")
    choisis = [m for m in MUTANTS if not a.ids or m[0] in a.ids]
    if a.preparer:
        for mid, famille, regle, rem in choisis:
            try:
                preparer(mid, rem)
                print(f"{mid} prêt")
            except Exception as e:
                print(f"{mid} MOTIF INVALIDE : {e}")
        return
    faits = deja_faits()
    a_faire = [m for m in choisis if m[0] not in faits]
    print(f"{len(a_faire)} mutants à lancer ({len(faits)} déjà faits)", flush=True)
    with cf.ThreadPoolExecutor(max_workers=a.travailleurs) as ex:
        futurs = {ex.submit(lancer, *m): m[0] for m in a_faire}
        for f in cf.as_completed(futurs):
            r = f.result()
            with VERROU:
                with open(RESULTATS, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(f"{r['id']:10s} {r['etat']:8s} {len(r.get('echecs') or [])} échecs {r.get('resume') or ''} "
                  f"{r.get('duree_s', '')} s R1={r.get('refus_R1')}", flush=True)


if __name__ == "__main__":
    main()
