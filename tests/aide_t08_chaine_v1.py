"""Aide des essais de la chaîne de lancement de T0.8 (v1) : un dépôt git jetable, données factices seulement.

Trois commits orphelins, sur trois branches : « 7b » (sortie factice de la course de confirmation, avec un fichier de sondes
et un `resume.json` qui ne doivent jamais être copiés), « code » (fichiers de `main` lus par la course : tâches, consignes,
invite dérivée, guide de classification ; plus un `resume.json` ancien), « texte » (texte scellé factice et configuration
réelle factice de la course). Aucun fichier réel du programme n'est lu : chemins réels, contenus inventés.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

RUN_7B = "20261111-151701-t06-reel"
CH_TEXTE = "prereg/T0.8-bases-boite-noire-v0-v1.md"
CH_CONFIG = "prereg/T0.8-configuration-course-v1.json"
CH = {"textes_7b": f"donnees/{RUN_7B}/textes-actions-t06.jsonl", "episodes_7b": f"diag/{RUN_7B}/episodes-t06.json",
      "manifeste_7b": f"runs/{RUN_7B}/manifeste.json",
      "taches": "donnees/20261007-082440-t05-extraction/taches-evaluation.json", "consignes": "prereg/P3-consignes-v1.md",
      "invite": "docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt"}
GUIDE = ("docs/sources/invites-2606.08892-v1/index.json", "docs/sources/invites-2606.08892-v1/invites/H1-classification.txt")


def git(d, *a, entree=None):
    r = subprocess.run(["git", "-C", str(d), *a], capture_output=True, input=entree)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode())
    return r.stdout.decode().strip()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def poser(d: Path, chemin: str, contenu: bytes, compagnon: bool = True) -> str:
    p = d / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(contenu)
    if compagnon:
        (d / (chemin + ".sha256")).write_text(f"{sha(contenu)}  {p.name}\n")
    return sha(contenu)


def commit_orphelin(d: Path, branche: str, fichiers: dict[str, bytes], compagnons: bool = True) -> str:
    git(d, "checkout", "-q", "--orphan", branche)
    git(d, "rm", "-rq", "--cached", "--ignore-unmatch", ".")
    for x in list(d.iterdir()):
        if x.name != ".git":
            subprocess.run(["rm", "-rf", str(x)], check=True)
    for c, b in fichiers.items():
        poser(d, c, b, compagnons and not c.endswith(("resume.json",)))
    git(d, "add", "-A", "-f")
    git(d, "commit", "-q", "-m", f"factice : {branche}")
    return git(d, "rev-parse", "HEAD")


def depot_factice(d: Path) -> dict:
    d.mkdir(parents=True, exist_ok=True)
    git(d, "init", "-q", "-b", "amorce")
    git(d, "config", "user.email", "essai@invalid")
    git(d, "config", "user.name", "essai")
    f7b = {CH["textes_7b"]: b'{"cle": "h__t000__p0", "texte": "factice"}\n',
           CH["episodes_7b"]: b'{"resultat": {"effectifs": {}}}\n',
           CH["manifeste_7b"]: b'{"run_id": "20261111-151701-t06-reel"}\n',
           f"diag/{RUN_7B}/lecture-sondes-t06.json": b'{"sondes": "jamais"}\n',
           f"diag/{RUN_7B}/resume.json": b'{"ligne_B": "jamais"}\n',
           f"donnees/{RUN_7B}/mesures-t06.npz": b"npz factice\n"}
    c7b = commit_orphelin(d, "calcul/t06-confirmation-7b-factice", f7b)
    fcode = {CH["taches"]: b'[{"identifiant": "t000", "questions": "q"}]\n', CH["consignes"]: b"consignes factices\n",
             CH["invite"]: b"invite derivee factice\n", GUIDE[0]: b'{"invites": []}\n', GUIDE[1]: b"guide factice\n",
             "diag/20261004-104156-harnais-factice/resume.json": b"{}\n", "src/controle_ia/__init__.py": b""}
    ccode = commit_orphelin(d, "prep/code-factice", fcode)
    emp = {"textes-actions-t06.jsonl": sha(f7b[CH["textes_7b"]]), "episodes-t06.json": sha(f7b[CH["episodes_7b"]]),
           "manifeste.json": sha(f7b[CH["manifeste_7b"]]), "mesures-t06.npz": "1" * 64, "lecture-cout-t06.json": "2" * 64}
    return {"depot": d, "c7b": c7b, "ccode": ccode, "f7b": f7b, "fcode": fcode, "emp": emp}


def config_factice(fx: dict, **changes) -> dict:
    e = {n: {"chemin": CH[n], "sha256": sha((fx["f7b"] if n.endswith("_7b") else fx["fcode"])[CH[n]]), "phase": "course"}
         for n in CH}
    c = {"mode": "reel", "entrees": e, "marqueurs": {"EMPREINTES_ENTREES_7B": dict(fx["emp"]), "COMMIT_CODE_T08": fx["ccode"]}}
    c.update(changes)
    return c


def texte_factice(fx: dict, sans: tuple = ()) -> bytes:
    lignes = ["# Préenregistrement factice de T0.8", f"tête de 7b : `{fx['c7b']}`"]
    lignes += [f"- `{k}`, `{v}`" for k, v in fx["emp"].items() if k not in sans]
    return ("\n".join(lignes) + "\n").encode()


def commit_texte(fx: dict, config: dict | None = None, texte: bytes | None = None, branche: str = "main-factice") -> str:
    config = config if config is not None else config_factice(fx)
    texte = texte if texte is not None else texte_factice(fx)
    return commit_orphelin(fx["depot"], branche, {CH_TEXTE: texte,
                                                  CH_CONFIG: (json.dumps(config, indent=1, sort_keys=True) + "\n").encode()})


# --- monde du lanceur et de l'amorce (dépôt distant jetable, registre des GO factice daté du jour) ------------------------

import os  # noqa: E402
import shutil  # noqa: E402
from datetime import date, timedelta  # noqa: E402

RACINE_DEPOT = Path(__file__).resolve().parents[1]
ORIGINE, PROLONGATION, ECHUE, DECISION = "GO-2099-01-01-11", "GO-2099-01-01-12", "GO-2099-01-01-13", "GO-2099-01-01-14"
ENTETE_GO = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
             "|---|---|---|---|---|---|---|---|\n")


def registre_go(jour: date | None = None, origine_echue=False, revocation=None, plafond="120 USD") -> str:
    j = jour or date.today()
    fin_o = j - timedelta(days=1) if origine_echue else j + timedelta(days=3)
    s = ENTETE_GO
    s += f"| {ORIGINE} | {j - timedelta(days=12)} | calcul | **T0.8 factice**, course | {plafond} | {fin_o} | Lazar | mot |\n"
    s += (f"| {PROLONGATION} | {j - timedelta(days=1)} | calcul | Prolongation de {ORIGINE} (factice), mêmes conditions | "
          f"plafond de {ORIGINE} | {j + timedelta(days=30)} | Lazar | mot |\n")
    s += f"| {ECHUE} | {j - timedelta(days=12)} | calcul | autre accord échu | 50 USD | {j - timedelta(days=1)} | Lazar | mot |\n"
    s += f"| {DECISION} | {j} | décision | un nœud | — | {j} | Lazar | mot |\n"
    if revocation:
        s += f"| GO-2099-01-01-19 | {j} | révocation | révoque {revocation} | — | {j} | Lazar | mot |\n"
    return s


def lancement_factice() -> dict:
    return {"go_origine": ORIGINE, "go_admis": [ORIGINE, PROLONGATION], "plafond_usd": 120, "compte_rendu_usd": 40,
            "carte": {"course": {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000,
                                 "prix_max_usd_h": 1.3}},
            "offre": {"coeurs_effectifs_min": 8, "disque_min_go": 100, "etiquette": "t08-v1", "memoire_vive_min_mo": 64000,
                      "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40, "telechargement_max_usd_go": 0.05},
            "relance": "aucune"}


OFFRE_A100 = {"id": 1, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_ram": 129000, "cpu_cores_effective": 16.0,
              "disk_space": 200.0, "dph_total": 1.05, "storage_total_cost": 0.02, "inet_down_cost": 0.01, "rentable": True,
              "cuda_max_good": 13.0, "reliability2": 0.995, "reliability": 0.995, "inet_down": 900.0, "machine_id": 201}
OFFRE_H200 = {**OFFRE_A100, "gpu_name": "H200 NVL", "gpu_ram": 143000, "dph_total": 1.2, "machine_id": 202}
OFFRE_CHERE = {**OFFRE_A100, "dph_total": 1.9, "machine_id": 203}

VASTAI_FACTICE = """#!/usr/bin/env bash
echo "$*" >> "$FAUX_VASTAI_JOURNAL"
case "$1 $2" in
"search offers") cat "$FAUX_OFFRES"; exit 0 ;;
"create instance") echo '{"success": true, "new_contract": 777777}'; exit 0 ;;
"show instances") cat "${FAUX_INSTANCES:-/dev/null}" 2>/dev/null || true; [ -n "${FAUX_INSTANCES:-}" ] || echo '[]'; exit 0 ;;
"show instance") echo '{"id": 777777, "actual_status": "running"}'; exit 0 ;;
esac
if [ "$1" = logs ]; then cat "$FAUX_JOURNAL"; exit 0; fi
echo "appel inattendu : $*" >&2; exit 3
"""


def monde_lancement(tmp: Path, *, jour: date | None = None, registre: str | None = None, amorce_alteree=False) -> dict:
    """Dépôt distant jetable : branches 7b factice, code (amorce de T0.8 et son compagnon), main (texte et configuration
    scellés, code de session, garde de calcul, registre des GO factice), branche d'entrée écrite par le programme ; clone
    de travail du lanceur (`T08_DEPOT`). Aucun réseau."""
    fx = depot_factice(tmp / "travail")
    d = fx["depot"]
    amorce = (RACINE_DEPOT / "scripts" / "amorce_instance_t08_v1.sh").read_bytes()
    fcode = dict(fx["fcode"])
    fcode["scripts/amorce_instance_t08_v1.sh"] = amorce + (b"# alteree\n" if amorce_alteree else b"")
    ccode = commit_orphelin(d, "prep/code-t08-factice", fcode)
    # compagnon de l'amorce : celui de l'amorce non altérée (l'artefact « amorce altérée » doit être refusé)
    git(d, "checkout", "-q", "prep/code-t08-factice")
    (d / "scripts/amorce_instance_t08_v1.sh.sha256").write_text(f"{sha(amorce)}  amorce_instance_t08_v1.sh\n")
    git(d, "add", "-A", "-f")
    git(d, "commit", "-q", "--allow-empty", "-m", "compagnon de l'amorce")
    ccode = git(d, "rev-parse", "HEAD")
    fx["ccode"] = ccode
    config = config_factice(fx)
    config["marqueurs"]["COMMIT_CODE_T08"] = ccode
    config["lancement"] = lancement_factice()
    texte = texte_factice(fx) + f"GO `{ORIGINE}` et `{PROLONGATION}`\n".encode()
    fmain = {CH_TEXTE: texte, CH_CONFIG: (json.dumps(config, indent=1, sort_keys=True) + "\n").encode()}
    for p in sorted((RACINE_DEPOT / "src" / "controle_ia").rglob("*.py")):
        rel = p.relative_to(RACINE_DEPOT)
        if rel.parts[2] in ("t06", "lancement_t08") or len(rel.parts) == 3:
            fmain[str(rel)] = p.read_bytes()
    fmain[".claude/hooks/garde_calcul.py"] = (RACINE_DEPOT / ".claude/hooks/garde_calcul.py").read_bytes()
    fmain["scripts/construire_branche_entree_t08_v1.py"] = (RACINE_DEPOT / "scripts/construire_branche_entree_t08_v1.py").read_bytes()
    fmain["registres/go.md"] = (registre if registre is not None else registre_go(jour)).encode()
    git(d, "checkout", "-q", "--orphan", "main")
    git(d, "rm", "-rq", "--cached", "--ignore-unmatch", ".")
    for x in list(d.iterdir()):
        if x.name != ".git":
            shutil.rmtree(x) if x.is_dir() else x.unlink()
    for c, b in fmain.items():
        poser(d, c, b, compagnon=c in (CH_TEXTE, CH_CONFIG))
    git(d, "add", "-A", "-f")
    git(d, "commit", "-qm", "main factice : texte et configuration scellés")
    cmain = git(d, "rev-parse", "HEAD")
    import importlib.util
    spec = importlib.util.spec_from_file_location("branche_t08_m", RACINE_DEPOT / "scripts" / "construire_branche_entree_t08_v1.py")
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)
    import contextlib
    import io
    with contextlib.redirect_stdout(io.StringIO()):
        assert B.main(["construire", "--depot", str(d), "--commit-7b", fx["c7b"], "--commit-code", ccode, "--commit-texte", cmain,
                       "--texte", CH_TEXTE, "--config", CH_CONFIG, "--branche", "entree/t08-course-v1"]) == 0
    distant = tmp / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    for b in ("main", "prep/code-t08-factice", "entree/t08-course-v1"):
        git(d, "push", "-q", str(distant), f"{b}:refs/heads/{b}")
    clone = tmp / "depot-lanceur"
    subprocess.run(["git", "clone", "-q", "--branch", "main", str(distant), str(clone)], check=True)
    return {"fx": fx, "distant": distant, "clone": clone, "ccode": ccode, "cmain": cmain, "config": config,
            "amorce_sha": sha(amorce), "entree": git(d, "rev-parse", "entree/t08-course-v1")}


def env_lanceur(m: dict, tmp: Path, **sup) -> dict:
    b = tmp / "bin"
    b.mkdir(exist_ok=True)
    (b / "vastai").write_text(VASTAI_FACTICE)
    (b / "vastai").chmod(0o755)
    e = {k: os.environ[k] for k in ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR") if k in os.environ}
    e.update(PATH=f"{b}:{e.get('PATH', '')}", HOME=str(tmp), T08_DEPOT=str(m["clone"]), GO_ID=ORIGINE,
             T08_BRANCHE_ENTREE="entree/t08-course-v1", T08_BRANCHE_CODE="prep/code-t08-factice",
             T08_AMORCE_SHA256=m["amorce_sha"], HF_TOKEN="hf-jeton-factice-0000", CONTROLE_IA_GITHUB_TOKEN="gh-jeton-factice-0000",
             FAUX_VASTAI_JOURNAL=str(tmp / "appels.txt"), FAUX_OFFRES=str(tmp / "offres.json"), FAUX_JOURNAL=str(tmp / "journal.txt"),
             INTERVALLE="1", ABSENCE_ATTENTE_S="0")
    e.update({k: v for k, v in sup.items()})
    return {k: v for k, v in e.items() if v is not None}
