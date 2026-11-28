"""Lanceur de mutants de la vérification neuve du module v3 (addendum 2 de P3, lentille « code et mutants »).

Trois listes, lues comme données (`ast`, aucun import ni exécution des fichiers sources) :
- CL : liste du contre-lecteur du v2 (`module-v3/outils-revue/mutants_v2.py`, sha256 d9c038e6…), échantillon ;
- RD : mutants V3-01 à V3-12 du rédacteur (`module-v3/controle-survivants/controle_survivants_v3.py`, liste
  `NOUVEAUX_V3`), échantillon ;
- VV : mes mutants (`mutants_verif_v3.py`, à côté).

Pour chaque mutant : copie de la base (`verification-v3/base/`, empreintes vérifiées), remplacements dans l'ordre
(chaque motif présent exactement une fois), compilation, dossier `mutants/<id>/` (module muté, copie des tests,
différence, journal pytest, journal R1), puis la SUITE ENTIÈRE (sans `-x`), depuis la racine du dépôt, sous la garde R1
v2b, `-B`, sans cache, `--basetemp` et `TMPDIR` sous `tmp/bt/<id>/` (supprimé après). Trois mutants à la fois.
Résultats : `journaux/resultats-mutants-verif-v3.jsonl`.

Usage : python -B lanceur_verif_v3.py [--travailleurs N] [ID …]
"""
import argparse
import ast
import concurrent.futures as cf
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import threading
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
VERIF = ICI.parent
S = VERIF.parent
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
BASE_MODULE, BASE_TESTS = VERIF / "base" / "audit_verdict_p3_v1.py", VERIF / "base" / "test_audit_verdict_p3_v1.py"
SHA_MODULE = "967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d"
SHA_TESTS = "d0c5eb07da17a1bf27fc38905edd648e4653ba9f3652076560ee4c4c3ba83b28"
LISTE_CL = S / "module-v3" / "outils-revue" / "mutants_v2.py"
SHA_CL = "d9c038e67b5e2f8cd7016c089faf02d0fd8ab86fee527d34e31304e1cfadf03c"
LISTE_RD = S / "module-v3" / "controle-survivants" / "controle_survivants_v3.py"
SHA_RD = "90e582f7af6e8b7e218449684d7491af32a226988def0a24e0dacde8f152768b"
LISTE_VV = ICI / "mutants_verif_v3.py"
RESULTATS = VERIF / "journaux" / "resultats-mutants-verif-v3.jsonl"
ECHANTILLON_CL = ["DESC-04", "DESC-05", "DESC-08", "DESC-12", "DESC-14", "V2-14", "PHRASE-08", "REGLE-01", "REGLE-02",
                  "G6-01", "G6-02", "G4-02", "SEUIL-11", "V2-12", "G7-05"]
ECHANTILLON_RD = ["V3-01", "V3-02", "V3-03", "V3-05", "V3-07", "V3-09", "V3-10", "V3-12"]
VERROU = threading.Lock()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def liste_litterale(chemin, nom):
    arbre = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(c, ast.Name) and c.id == nom for c in n.targets):
            return ast.literal_eval(n.value)
    raise SystemExit(f"{nom} absent de {chemin}")


def tous_les_mutants():
    if sha(LISTE_CL) != SHA_CL or sha(LISTE_RD) != SHA_RD:
        raise SystemExit("liste de mutants altérée : arrêt")
    cl = {m[0]: m for m in liste_litterale(LISTE_CL, "MUTANTS")}
    rd = {m[0]: m for m in liste_litterale(LISTE_RD, "NOUVEAUX_V3")}
    vv = liste_litterale(LISTE_VV, "MUTANTS")
    sortie = [("CL",) + tuple(cl[i]) for i in ECHANTILLON_CL] + [("RD",) + tuple(rd[i]) for i in ECHANTILLON_RD]
    sortie += [("VV",) + tuple(m) for m in vv]
    ids = [m[1] for m in sortie]
    if len(ids) != len(set(ids)):
        raise SystemExit("identifiants en double")
    return sortie


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
    d = VERIF / "mutants" / mid
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "audit_verdict_p3_v1.py").write_text(texte, encoding="utf-8")
    shutil.copyfile(BASE_TESTS, d / "test_audit_verdict_p3_v1.py")
    diff = "".join(difflib.unified_diff(base.splitlines(True), texte.splitlines(True), "base/audit_verdict_p3_v1.py",
                                        f"mutants/{mid}/audit_verdict_p3_v1.py", n=1))
    (d / "difference.diff").write_text(diff, encoding="utf-8")
    return d


def lancer(origine, mid, famille, regle, remplacements):
    debut = time.time()
    try:
        d = preparer(mid, remplacements)
    except Exception as e:
        return {"origine": origine, "id": mid, "famille": famille, "regle": regle, "etat": "motif invalide",
                "detail": str(e)}
    tmp = VERIF / "tmp" / "bt" / mid
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
    except subprocess.TimeoutExpired:
        code, sortie = "délai", ""
    (d / "pytest.log").write_text(sortie, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    echecs = re.findall(r"^(?:FAILED|ERROR) \S+::(\S+)(?: - (.*))?$", sortie, flags=re.M)
    resume = re.findall(r"^=*\s*(\d+ (?:passed|failed|error).*?)\s*=*$", sortie, flags=re.M)
    lignes_r1 = journal_r1.read_text(encoding="utf-8").splitlines() if journal_r1.exists() else []
    refus = sum(1 for l in lignes_r1 if '"refus": true' in l)
    hors_tmp = sum(1 for l in lignes_r1 if json.loads(l)["chemin"].startswith(str(VERIF / "tmp")) is False)
    etat = "SURVIT" if code == 0 else "tué" if code == 1 else f"erreur ({code})"
    return {"origine": origine, "id": mid, "famille": famille, "regle": regle, "etat": etat, "code": code,
            "echecs": [x[0] for x in echecs], "premier_motif": (echecs[0][1] or "")[:300] if echecs else None,
            "resume": resume[-1] if resume else None, "duree_s": round(time.time() - debut, 1), "refus_R1": refus,
            "traces_R1": len(lignes_r1), "traces_hors_tmp": hors_tmp, "sha_mutant": sha(d / "audit_verdict_p3_v1.py")}


def deja_faits():
    if not RESULTATS.exists():
        return set()
    return {json.loads(l)["id"] for l in RESULTATS.read_text(encoding="utf-8").splitlines() if l.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--travailleurs", type=int, default=3)
    ap.add_argument("--preparer", action="store_true")
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    if a.travailleurs > 3:
        raise SystemExit("trois mutants à la fois au plus")
    if sha(BASE_MODULE) != SHA_MODULE or sha(BASE_TESTS) != SHA_TESTS:
        raise SystemExit("copie de base altérée : arrêt")
    choisis = [m for m in tous_les_mutants() if not a.ids or m[1] in a.ids]
    if a.preparer:
        for origine, mid, famille, regle, rem in choisis:
            try:
                preparer(mid, rem)
                print(f"{origine} {mid} prêt")
            except Exception as e:
                print(f"{origine} {mid} MOTIF INVALIDE : {e}")
        return
    faits = deja_faits()
    a_faire = [m for m in choisis if m[1] not in faits]
    print(f"{len(a_faire)} mutants à lancer ({len(faits)} déjà faits)", flush=True)
    with cf.ThreadPoolExecutor(max_workers=a.travailleurs) as ex:
        futurs = {ex.submit(lancer, *m): m[1] for m in a_faire}
        for f in cf.as_completed(futurs):
            r = f.result()
            with VERROU:
                with open(RESULTATS, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(f"{r['origine']} {r['id']:11s} {r['etat']:8s} {len(r.get('echecs') or [])} échecs "
                  f"{r.get('resume') or ''} {r.get('duree_s', '')} s R1={r.get('refus_R1')}", flush=True)


if __name__ == "__main__":
    main()
