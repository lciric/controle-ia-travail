"""Contrôle des survivants de la campagne de mutants sur le module mis au brouillon 4 (dossier module-v2).

Pour chaque mutant : liste et remplacements de `revue-mutants/mutants_revue.py` (lus comme texte, jamais importés) ;
remplacement adapté au module v2 quand le code muté a changé (F23) ; mutants des règles nouvelles du brouillon 4 (N01 à
N10). Copie du module v2, remplacements appliqués dans l'ordre (chaque motif présent exactement une fois), compilation,
dossier temporaire `module-v2/tmp/mutants/<id>/` (module muté, copie des tests v2), puis la suite complète des tests v2
arrêtée au premier échec (`-x`), depuis la racine du dépôt, sous la garde R1 de la revue (`revue-mutants/garde_r1_revue.py` :
toute ouverture de `donnees/`, `diag/`, `runs/`, `traces/` du dépôt ou des consignes privées est refusée et journalisée).
« tué » : la suite échoue ; « SURVIT » : la suite passe en entier. Résultats : `resultats-survivants-v2.jsonl` (une ligne par
mutant). Tables synthétiques seulement.

Usage (depuis n'importe où) : python -B controle_survivants_v2.py [--travailleurs N] [--tous] [ID …]
  sans --tous : les 41 survivants de la campagne (dont les 4 équivalents) et les mutants N01 à N10 ;
  --tous : en plus, les 66 mutants tués de la campagne, portés sur le module v2.
"""
import argparse
import concurrent.futures as cf
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
V2 = ICI.parent
ADDENDUM = V2.parent
REVUE = ADDENDUM / "revue-mutants"
MODULE, TESTS = V2 / "base" / "audit_verdict_p3_v1.py", V2 / "base" / "test_audit_verdict_p3_v1.py"  # copie (mêmes empreintes)
PY = "/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python"
DEPOT = "/home/user/controle-ia-travail"
RESULTATS = ICI / "resultats-survivants-v2.jsonl"
TMP = V2 / "tmp" / "controle-redacteur"
EQUIVALENTS = {"E11", "F13", "F24", "F04"}
VERROU = threading.Lock()

# remplacements adaptés au module v2 (le code d'origine a changé)
ADAPTES = {
    "F23": ("F", "garde 7 : [L] « non calculable » (ou « en échec ») accepté quel que soit l'état recalculé",
            [('        if ici["etat"] != etat:\n', '        if ici["etat"] != etat and etat == CALCULABLE:\n'),
             ('            if motif != ici["motif"]:\n', '            if motif != ici.get("motif", motif):\n')]),
}
# règles nouvelles ou changées au brouillon 4
NOUVEAUX = [
    ("N01", "N", "garde 7 : état de [L] non comparé (seuls les nombres d'une entrée calculable)",
     [('        if ici["etat"] != etat:\n', '        if False:\n'),
      ('            if motif != ici["motif"]:\n', '            if motif != ici.get("motif", motif):\n')]),
    ("N02", "N", "garde 7 : motif de [L] non comparé",
     [('            if motif != ici["motif"]:\n', '            if False:\n')]),
    ("N03", "N", "garde 7 : entrée « en échec » de [L] acceptée sans comparaison (règle du brouillon 2)",
     [('        if ici["etat"] != etat:\n', '        if ici["etat"] != etat and etat != EN_ECHEC:\n'),
      ('            if motif != ici["motif"]:\n', '            if motif != ici.get("motif", motif):\n')]),
    ("N04", "N", "audit (3) : part en échec (garde 15) non rendue « non calculé » (précision d'application 2 retirée)",
     [('    elif pf["part"]["etat"] != CALCULE:\n', '    elif False:\n')]),
    ("N05", "N", "phrase de B3 sans « grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) »",
     [('{a80} ; grandeur calculée avant le "\n                 "scellement, sur des nombres déjà lus (brainstorm)",',
       '{a80}",')]),
    ("N06", "N", "libellé de D de l'ancienne forme (« qui l'abaissent »)",
     [('"abaissent : les actions à forme abaissent la différence"', '"abaissent : les actions à forme qui l\'abaissent"')]),
    ("N07", "N", "phrase de lecture de l'audit jointe à la consigne « cité et soumis à Lazar »",
     [('LECTURE_AUDIT = "addendum 2 suspect de propreté"\n',
       'LECTURE_AUDIT = "addendum 2 suspect de propreté ; cité et soumis à Lazar"\n')]),
    ("N08", "N", "compte des 13 contrôles écrits non vérifié",
     [('    if len(controles) != CONTROLES_ECRITS:\n', '    if False:\n')]),
    ("N09", "N", "nombre de contrôles : ligne d'issue non rapportée",
     [('"ligne_d_issue": ligne, "detail": detail}', '"ligne_d_issue": None, "detail": detail}')]),
    ("N10", "N", "audit (1) : règles dans les deux sens au vocabulaire ancien",
     [('"regles_dans_les_deux_sens": "formes qui élèvent ou abaissent la différence ; puissance plus faible ou plus "\n'
       '                                         "forte"}',
       '"regles_dans_les_deux_sens": "formes qui ajoutent ou retirent (D signé) ; puissance plus faible ou plus forte"}')]),
]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def mutants_de_la_campagne():
    """Liste de la campagne, lue comme texte (aucun import du dossier de la revue)."""
    espace = {}
    exec(compile((REVUE / "mutants_revue.py").read_text(encoding="utf-8"), "mutants_revue.py", "exec"), espace)
    return espace["MUTANTS"]


def etats_de_la_campagne():
    lignes = (REVUE / "journaux" / "resultats-mutants.jsonl").read_text(encoding="utf-8").splitlines()
    return {x["id"]: x["etat"] for x in (json.loads(l) for l in lignes if l.strip())}


def appliquer(texte, remplacements):
    for ancien, nouveau in remplacements:
        n = texte.count(ancien)
        if n != 1:
            raise ValueError(f"motif présent {n} fois : {ancien[:80]!r}")
        texte = texte.replace(ancien, nouveau)
    return texte


def preparer(mid, remplacements):
    base = MODULE.read_text(encoding="utf-8")
    texte = appliquer(base, remplacements)
    if texte == base:
        raise ValueError("mutant identique au module v2")
    compile(texte, f"mutants/{mid}/audit_verdict_p3_v1.py", "exec")
    d = TMP / "mutants" / mid
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    (d / "audit_verdict_p3_v1.py").write_text(texte, encoding="utf-8")
    shutil.copyfile(TESTS, d / "test_audit_verdict_p3_v1.py")
    return d


def lancer(mid, famille, regle, remplacements, origine, etat_campagne):
    debut = time.time()
    try:
        d = preparer(mid, remplacements)
    except Exception as e:                       # motif invalide : consigné, jamais lancé
        return {"id": mid, "famille": famille, "regle": regle, "origine": origine, "etat_campagne": etat_campagne,
                "etat": "motif invalide", "detail": str(e)}
    tmp = TMP / "bt-mutants" / mid
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    journal_r1 = tmp / "r1.jsonl"
    env = {**os.environ, "REVUE_JOURNAL_R1": str(journal_r1), "PYTHONPATH": f"src:{REVUE}", "PYTHONDONTWRITEBYTECODE": "1",
           "TMPDIR": str(tmp)}
    cmd = [PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-p", "garde_r1_revue",
           f"--basetemp={tmp / 'bt'}", str(d / "test_audit_verdict_p3_v1.py")]
    try:
        r = subprocess.run(cmd, cwd=DEPOT, env=env, capture_output=True, text=True, timeout=3600)
        code, sortie = r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        code, sortie = "délai", ""
    echecs = re.findall(r"^(?:FAILED|ERROR) \S+::(\S+)(?: - (.*))?$", sortie, flags=re.M)
    resume = re.findall(r"^=*\s*(\d+ (?:passed|failed).*?)\s*=*$", sortie, flags=re.M)
    refus = sum(1 for l in journal_r1.read_text(encoding="utf-8").splitlines() if '"refus": true' in l) \
        if journal_r1.exists() else 0
    etat = "SURVIT" if code == 0 else "tué" if code == 1 else f"erreur ({code})"
    resultat = {"id": mid, "famille": famille, "regle": regle, "origine": origine, "etat_campagne": etat_campagne,
                "etat": etat, "code": code, "premier_echec": echecs[0][0] if echecs else None,
                "motif_echec": (echecs[0][1] or "")[:300] if echecs else None, "resume": resume[-1] if resume else None,
                "duree_s": round(time.time() - debut, 1), "refus_R1": refus,
                "sha_mutant": sha(d / "audit_verdict_p3_v1.py")}
    if etat != "tué":
        resultat["fin_du_journal"] = sortie[-3000:]
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.rmtree(d, ignore_errors=True)
    return resultat


def deja_faits():
    if not RESULTATS.exists():
        return set()
    return {json.loads(l)["id"] for l in RESULTATS.read_text(encoding="utf-8").splitlines() if l.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--travailleurs", type=int, default=3)
    ap.add_argument("--tous", action="store_true")
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    etats = etats_de_la_campagne()
    survivants = {k for k, v in etats.items() if v == "SURVIT"}
    if len(survivants) != 41 or not EQUIVALENTS <= survivants:
        raise SystemExit(f"liste des survivants inattendue ({len(survivants)})")
    choisis = []
    for mid, famille, regle, rem in mutants_de_la_campagne():
        if mid not in survivants and not a.tous:
            continue
        origine = "campagne"
        if mid in ADAPTES:
            famille, regle, rem = ADAPTES[mid]
            origine = "adapté au module v2"
        choisis.append((mid, famille, regle, rem, origine, etats[mid]))
    choisis += [(mid, f, r, rem, "règle du brouillon 4", "—") for mid, f, r, rem in NOUVEAUX]
    if a.ids:
        choisis = [c for c in choisis if c[0] in a.ids]
    faits = deja_faits()
    a_faire = [c for c in choisis if c[0] not in faits]
    print(f"module v2 {sha(MODULE)[:12]}, tests v2 {sha(TESTS)[:12]} ; {len(a_faire)} mutants à lancer "
          f"({len(faits)} déjà faits)", flush=True)
    with cf.ThreadPoolExecutor(max_workers=a.travailleurs) as ex:
        futurs = {ex.submit(lancer, *c): c[0] for c in a_faire}
        for f in cf.as_completed(futurs):
            r = f.result()
            with VERROU:
                with open(RESULTATS, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(f"{r['id']:4s} {r['etat']:8s} {r.get('premier_echec') or ''} {r.get('duree_s', '')}", flush=True)


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
