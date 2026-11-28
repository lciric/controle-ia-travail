"""Lanceur de la revue par mutants (contre-lecture R2 du code de l'addendum 2 de P3).

Pour chaque mutant de `mutants_revue.MUTANTS` : copie de base (empreinte vérifiée), remplacements appliqués dans l'ordre
(chaque motif présent exactement une fois au moment de son application), compilation, dossier `mutants/<id>/` (module
muté, copie inchangée des tests, différence), puis la suite complète des tests de la copie, arrêtée au premier échec
(`-x`), sous la garde R1 de la revue. « tué » : la suite échoue ; « SURVIT » : la suite passe (42 tests). Résultats :
`journaux/resultats-mutants.jsonl` (une ligne par mutant ; un mutant déjà présent n'est pas relancé).

Usage : python lanceur_revue.py [--preparer] [--travailleurs N] [ID …]
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
sys.path.insert(0, str(ICI))
from mutants_revue import MUTANTS  # noqa: E402

PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
BASE_MODULE = ICI / "base" / "audit_verdict_p3_v1.py"
BASE_TESTS = ICI / "base" / "test_audit_verdict_p3_v1.py"
SHA_MODULE = "0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf"
SHA_TESTS = "ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3"
RESULTATS = ICI / "journaux" / "resultats-mutants.jsonl"
VERROU = threading.Lock()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def appliquer(texte, remplacements):
    for ancien, nouveau in remplacements:
        n = texte.count(ancien)
        if n != 1:
            raise ValueError(f"motif présent {n} fois : {ancien[:80]!r}")
        texte = texte.replace(ancien, nouveau)
    return texte


def preparer(mid, remplacements):
    base = BASE_MODULE.read_text(encoding="utf-8")
    texte = appliquer(base, remplacements)
    if texte == base:
        raise ValueError("mutant identique à la base")
    compile(texte, f"mutants/{mid}/audit_verdict_p3_v1.py", "exec")
    d = ICI / "mutants" / mid
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
    tmp = ICI / "tmp" / mid
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    journal_r1 = d / "r1.jsonl"
    env = {**os.environ, "REVUE_JOURNAL_R1": str(journal_r1), "PYTHONPATH": f"src:{ICI}", "PYTHONDONTWRITEBYTECODE": "1",
           "TMPDIR": str(tmp)}
    cmd = [PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-p", "garde_r1_revue",
           f"--basetemp={tmp / 'bt'}", str(d / "test_audit_verdict_p3_v1.py")]
    try:
        r = subprocess.run(cmd, cwd=DEPOT, env=env, capture_output=True, text=True, timeout=2400)
        code, sortie = r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired as e:
        code, sortie = "délai", (e.stdout or "") if isinstance(e.stdout, str) else ""
    (d / "pytest.log").write_text(sortie, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    echecs = re.findall(r"^(?:FAILED|ERROR) \S+::(\S+)(?: - (.*))?$", sortie, flags=re.M)
    resume = re.findall(r"^=*\s*(\d+ (?:passed|failed).*?)\s*=*$", sortie, flags=re.M)
    refus = 0
    if journal_r1.exists():
        refus = sum(1 for l in journal_r1.read_text(encoding="utf-8").splitlines() if '"refus": true' in l)
    etat = "SURVIT" if code == 0 else "tué" if code == 1 else f"erreur ({code})"
    return {"id": mid, "famille": famille, "regle": regle, "etat": etat, "code": code,
            "premier_echec": echecs[0][0] if echecs else None, "motif_echec": (echecs[0][1] or "")[:300] if echecs else None,
            "resume": resume[-1] if resume else None, "duree_s": round(time.time() - debut, 1), "refus_R1": refus,
            "sha_mutant": sha(d / "audit_verdict_p3_v1.py")}


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
    if sha(BASE_MODULE) != SHA_MODULE or sha(BASE_TESTS) != SHA_TESTS:
        raise SystemExit("copie de base altérée : arrêt")
    choisis = [m for m in MUTANTS if not a.ids or m[0] in a.ids]
    ids = [m[0] for m in MUTANTS]
    if len(ids) != len(set(ids)):
        raise SystemExit("identifiants de mutants en double")
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
            print(f"{r['id']:4s} {r['etat']:8s} {r.get('premier_echec') or ''} {r.get('duree_s', '')}", flush=True)


if __name__ == "__main__":
    main()
