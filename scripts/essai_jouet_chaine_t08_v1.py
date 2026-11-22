#!/usr/bin/env python3
"""Essai de bout en bout de l'amorce de T0.8 en mode jouet (consigne de la chaîne de lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 4) — v1.

Sur processeur, sans réseau du loueur ni dépense. Construit un dépôt distant jetable (`file://`) :
- branche du code : un commit dont l'arbre est celui du commit courant **restreint aux chemins que l'amorce extrait**
  (`CHEMINS_CODE`, copiés à l'octet par `git archive`) ; l'arbre réel de `main` porte en plus 34 `resume.json` anciens que la
  garde de l'instance refuse (question posée au rédacteur, réserve du rapport) : l'essai ne les reproduit que sur demande
  (`--interdit-dans-code`) ;
- branche d'entrée : orpheline, entrées factices de la course jouet (`essai_jouet_v1.fabriquer_entrees` : tâches, textes,
  épisodes et manifeste de 7b factices, avec leurs compagnons) et la configuration jouet de la course, scellée, portant la
  section `lancement` ; sur demande, un `lecture-sondes-t06.json` factice glissé (`--interdit-dans-entree`).
Puis joue l'amorce (`AMORCE_ESSAI_LOCAL=1` : ni minuterie ni appel au loueur ; la destruction et l'arrêt demandés s'écrivent
dans un fichier), MODE=jouet, jusqu'à la poussée de la branche de sortie sur le dépôt distant, et relève ce qui a été poussé
(noms, empreintes ; données factices). Deux essais de même entropie se comparent (`--comparer`).

    python3 -B scripts/essai_jouet_chaine_t08_v1.py --dossier <neuf> --horodatage AAAAMMJJ-HHMMSS --entropie N [--nom a]
    python3 -B scripts/essai_jouet_chaine_t08_v1.py --comparer <dossier a> <dossier b>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

CHEMINS_CODE = (".gitignore", "src", "tests", "scripts", "pyproject.toml", "requirements-cpu.txt", "requirements-gpu.txt", ".claude",
                "registres/go.md", "registres/scellements-v1.md", "registres/code-mots-et-cout-t06",
                "docs/sources/invites-2606.08892-v1", "prereg/T0.8-base-A-mots-et-cout-v1.md",
                "prereg/T0.8-base-A-mots-et-cout-v1.md.sha256")
CONFIG_JOUET = "prereg/T0.8-configuration-course-jouet-v1.json"
GO_ORIGINE, GO_PROLONGATION = "GO-2026-11-10-12", "GO-2026-11-22-79"
# noms de deux des 34 resume.json anciens de l'arbre de main (runs jouets, notes), recréés vides dans l'arbre du code de l'essai :
# la garde resserrée ne doit pas s'y arrêter (contre-lecture B-1, cas sain)
RESUME_ETRANGERS = ("diag/20261004-104156-harnais-factice/resume.json",
                    "docs/notes/collisionneur-bassins-etroits-v1/consultations-a-part-v1/resume.json")
BRANCHE_CODE, BRANCHE_ENTREE = "prep/code-t08-jouet", "entree/t08-jouet-v1"


def git(d, *a, entree=None, env=None) -> str:
    r = subprocess.run(["git", "-C", str(d), *a], capture_output=True, input=entree, env={**os.environ, **(env or {})})
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a[:3])} : {r.stderr.decode()[:400]}")
    return r.stdout.decode().strip()


ID = {"GIT_AUTHOR_NAME": "essai", "GIT_AUTHOR_EMAIL": "essai@invalid", "GIT_COMMITTER_NAME": "essai",
      "GIT_COMMITTER_EMAIL": "essai@invalid", "GIT_AUTHOR_DATE": "2026-11-22T12:00:00Z", "GIT_COMMITTER_DATE": "2026-11-22T12:00:00Z"}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def go_du_jour(jour: date) -> str:
    return GO_ORIGINE if jour <= date(2026, 11, 30) else GO_PROLONGATION


def construire(dossier: Path, horodatage: str, entropie: int, interdit_code=False, interdit_entree=False,
               plus_dans_entree=(), moins_dans_entree=()) -> dict:
    from controle_ia.scellement import sceller
    from controle_ia.t08 import essai_jouet_v1 as ej

    dossier.mkdir(parents=True)
    # 1. branche du code
    w = dossier / "code"
    w.mkdir()
    a = subprocess.run(["git", "-C", str(RACINE), "archive", "HEAD", *CHEMINS_CODE], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(w)], input=a, check=True)
    for etranger in RESUME_ETRANGERS:   # cas sain de la garde resserrée (B-1) : des resume.json d'autres runs, comme dans l'arbre de main
        (w / etranger).parent.mkdir(parents=True, exist_ok=True)
        (w / etranger).write_text("{}\n")
    if interdit_code:              # un resume.json de 7b (run factice de l'essai) dans l'arbre du code, hors des motifs extraits
        (w / "diag" / f"{horodatage}-t06-7b-jouet").mkdir(parents=True)
        (w / "diag" / f"{horodatage}-t06-7b-jouet" / "resume.json").write_text("{}\n")
    git(w, "init", "-q", "-b", BRANCHE_CODE)
    git(w, "add", "-A", "-f")
    git(w, "commit", "-qm", "code de l'essai (arbre restreint)", env=ID)
    commit = git(w, "rev-parse", "HEAD")
    # 2. branche d'entrée (entrées factices de la course jouet, configuration jouet scellée avec la section lancement)
    f = dossier / "fabrique"
    e = ej.fabriquer_entrees(f / "r", horodatage, entropie)
    course, _ = ej.configs(e["racine"], e["runs"], e["s7b"], e["base_a"], e["hd"], e["taches"], entropie)
    course["lancement"] = {"go_origine": GO_ORIGINE, "go_admis": [GO_ORIGINE, GO_PROLONGATION], "plafond_usd": 120,
                           "compte_rendu_usd": 40,
                           "carte": {"course": {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000,
                                                "prix_max_usd_h": 1.3}},
                           "offre": {"coeurs_effectifs_min": 8, "disque_min_go": 100, "etiquette": "t08-v1",
                                     "memoire_vive_min_mo": 64000, "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40,
                                     "telechargement_max_usd_go": 0.05}, "relance": "aucune"}
    en = dossier / "entree"
    en.mkdir()
    for nom in ("taches", "textes_7b", "episodes_7b", "manifeste_7b"):
        ch = course["entrees"][nom]["chemin"]
        for x in (ch, ch + ".sha256"):
            (en / x).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(e["racine"] / x, en / x)
    from controle_ia.lancement_t08.commit_local_v1 import GUIDE     # invite dérivée et guide : comme la branche d'entrée réelle
    for ch in (course["entrees"]["invite"]["chemin"], *GUIDE):
        for x in (ch, ch + ".sha256"):
            (en / x).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(RACINE / x, en / x)
    for ch in plus_dans_entree:
        (en / ch).parent.mkdir(parents=True, exist_ok=True)
        (en / ch).write_text("fichier de plus (artefact)\n", encoding="utf-8")
    for ch in moins_dans_entree:
        (en / ch).unlink()
    (en / CONFIG_JOUET).parent.mkdir(parents=True, exist_ok=True)
    (en / CONFIG_JOUET).write_text(json.dumps(course, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(en / CONFIG_JOUET)
    if interdit_entree:
        run7b = e["runs"]["t06-7b-jouet"]
        (en / "diag" / run7b / "lecture-sondes-t06.json").write_text('{"jamais": true}\n')
    git(en, "init", "-q", "-b", BRANCHE_ENTREE)
    git(en, "add", "-A", "-f")
    git(en, "commit", "-qm", "branche d'entrée de l'essai jouet", env=ID)
    entree = git(en, "rev-parse", "HEAD")
    # 3. dépôt distant
    distant = dossier / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    git(distant, "config", "uploadpack.allowFilter", "true")
    git(w, "push", "-q", str(distant), f"{BRANCHE_CODE}:refs/heads/{BRANCHE_CODE}")
    git(en, "push", "-q", str(distant), f"{BRANCHE_ENTREE}:refs/heads/{BRANCHE_ENTREE}")
    return {"commit": commit, "entree": entree, "distant": distant}


def jouer(dossier: Path, monde: dict, nom: str, env_sup: dict | None = None) -> dict:
    jour = datetime.now(timezone.utc).date()
    go = go_du_jour(jour)
    ech = date(2026, 11, 30) if go == GO_ORIGINE else date(2026, 12, 31)
    fin = int(datetime.combine(ech + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp())
    r = dossier / "racine"
    r.mkdir()
    venv = os.environ.get("VIRTUAL_ENV") or str(RACINE / ".venv")
    e = {k: os.environ[k] for k in ("PATH", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    e.update(HOME=str(dossier), RACINE_AMORCE=str(r), AMORCE_ESSAI_LOCAL="1", MODE="jouet", PREREG_ABSENT="1",
             CONFIG=CONFIG_JOUET, COMMIT=monde["commit"], BRANCHE_CODE=BRANCHE_CODE, BRANCHE_ENTREE=BRANCHE_ENTREE,
             ENTREE_COMMIT=monde["entree"], GH_TOKEN="jeton-factice-0000", GO_ID_T08=go,
             DEPOT_URL=f"file://{monde['distant']}", ECHEANCE_UTC_S=str(fin), FIN_GO_UTC_S=str(fin),
             DEPENSE_EPUISEE_UTC_S=str(int(time.time()) + 36000), BRANCHE=f"calcul/t08-jouet-{nom}", VENV_EXISTANT=venv,
             POUSSEE_ATTENTE_S="1")
    e.update(env_sup or {})
    t0 = time.time()
    p = subprocess.run(["bash", str(RACINE / "scripts" / "amorce_instance_t08_v1.sh")], env=e, capture_output=True, text=True,
                       timeout=7200)
    (dossier / "amorce-sortie.txt").write_text(p.stdout + "\n--- erreur ---\n" + p.stderr, encoding="utf-8")
    pousse = {}
    try:
        tete = git(monde["distant"], "rev-parse", f"refs/heads/calcul/t08-jouet-{nom}")
        for l in git(monde["distant"], "ls-tree", "-r", tete).splitlines():
            meta, chemin = l.split("\t", 1)
            pousse[chemin] = meta.split()[2]
        commits = git(monde["distant"], "log", "--format=%s", tete).splitlines()
    except RuntimeError:
        tete, commits = None, []
    return {"code": p.returncode, "secondes": round(time.time() - t0, 1), "go": go,
            "fin_normale": (r / "t08-fin-normale").is_file(), "arret_demande": (r / "t08-arret-demande").read_text().strip()
            if (r / "t08-arret-demande").is_file() else None,
            "detruire": (r / "t08-detruire").read_text().strip() if (r / "t08-detruire").is_file() else None,
            "tete_sortie": tete, "commits_sortie": commits, "pousse_hors_code": {k: v for k, v in sorted(pousse.items())
                                                                                  if k.split("/")[0] in ("runs", "diag", "donnees", "traces")}}


def comparer(a: Path, b: Path) -> dict:
    """Mêmes fichiers de données à l'octet (chemins rapportés au dossier du run) ; `course-t08.json` : `resultat` égal en
    JSON canonique, l'identifiant du run normalisé ; manifestes et compagnons d'enveloppes exclus (date de création,
    identifiant du run) ; traces exclues (heures)."""
    ra, rb = (json.loads((x / "rapport.json").read_text()) for x in (a, b))
    def norm(r):
        out = {}
        for k, v in r["pousse_hors_code"].items():
            parties = k.split("/")
            if parties[0] == "traces":
                continue
            if parties[0] in ("runs", "diag", "donnees") and len(parties) > 2 and "-t08-" in parties[1]:
                out["/".join([parties[0], "<run>", *parties[2:]])] = v
        return out
    na, nb = norm(ra), norm(rb)
    egaux, differents, exclus = [], [], []
    for k in sorted(set(na) | set(nb)):
        if k.startswith("runs/") or k.endswith(".json.sha256") and k.startswith("diag/"):
            exclus.append(k)
        elif k == "diag/<run>/course-t08.json":
            # `resultat` en JSON canonique, l'identifiant du run (tiré de l'heure par l'amorce) remplacé par « <run> »
            ca, cb = (json.dumps(json.loads(git(x / "distant.git", "cat-file", "blob", n[k]))["resultat"], sort_keys=True)
                      .replace(json.loads(git(x / "distant.git", "cat-file", "blob", n[k]))["run_id"], "<run>")
                      for x, n in ((a, na), (b, nb)))
            (egaux if ca == cb else differents).append(k + " (resultat, identifiant du run normalisé)")
        elif na.get(k) == nb.get(k):
            egaux.append(k)
        else:
            differents.append(k)
    return {"egaux": egaux, "differents": differents, "exclus": exclus, "codes": [ra["code"], rb["code"]],
            "fin_normale": [ra["fin_normale"], rb["fin_normale"]]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier")
    ap.add_argument("--horodatage")
    ap.add_argument("--entropie", type=int)
    ap.add_argument("--nom", default="a")
    ap.add_argument("--interdit-dans-code", action="store_true")
    ap.add_argument("--interdit-dans-entree", action="store_true")
    ap.add_argument("--comparer", nargs=2)
    a = ap.parse_args(argv)
    if a.comparer:
        r = comparer(Path(a.comparer[0]), Path(a.comparer[1]))
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0 if not r["differents"] and r["egaux"] else 1
    d = Path(a.dossier)
    if d.exists():
        print(f"{d} existe déjà (R12)", file=sys.stderr)
        return 2
    m = construire(d, a.horodatage, a.entropie, a.interdit_dans_code, a.interdit_dans_entree)
    r = jouer(d, m, a.nom)
    r.update(commit_code=m["commit"], commit_entree=m["entree"])
    (d / "rapport.json").write_text(json.dumps(r, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: r[k] for k in ("code", "secondes", "fin_normale", "arret_demande", "detruire", "tete_sortie")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
