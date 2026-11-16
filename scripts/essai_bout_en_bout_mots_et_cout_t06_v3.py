"""Essai de bout en bout de la pièce « mots et coût » de T0.6, **mode réel**, par le lanceur, sur données FACTICES — v3
(fichier neuf, R12 ; la v1 reste telle quelle ; v3 : module et lanceur v3 ; contre-lecture factice scellée passée à
`ecrire-fichier-code --contre-lecture`, désormais obligatoire (C-2) ; sortie et progrès sans aucun nombre décimal (C-3) ;
`cout_present` de la base (B) égal à la colonne des mesures factices (R-2765) ; marques de T0.7 recopiées de la
contre-lecture v2, § 5, la configuration de T0.7 n'étant pas ouverte). Répétition des gestes de l'hôte et de la mère dans des dépôts jetables (rien du dépôt n'est touché) :

1. dépôt jetable : textes scellés (base (A), T0.6) recopiés, code de la pièce, lien `src` vers le paquet `controle_ia`, commit ;
2. fichier de `CODE-MOTS-ET-COUT-T06` écrit par `ecrire-fichier-code`, scellé ; registre factice (`SCELLEMENT-T08-BASE-A`,
   `RUN-CONFIRMATION-T06` du run factice de la forme de 7b, `CODE-MOTS-ET-COUT-T06`), commit ; `verifier-code` ;
3. entrées factices à la configuration scellée de 7b dans une racine d'entrées à part ; lanceur en mode réel ; sortie
   (chemins et empreintes seulement) ; fichiers scellés ; issue lue par le lecteur de T0.7 (`lire_issue_mots_et_cout`,
   `deriver_classe`) ; état de BA-L2 par `etat-ba-l2` ;
4. lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` inscrites comme le fera la mère (`registre_v1.ecrire_ligne`) ;
   lecteur de registre de T0.7 (clés de l'étape B) : `ISSUE-MOTS-ET-COUT-T06` lue et scellée, `CODE-…` et `LECTURE-…`
   ignorées ; relance de la pièce refusée (code 2, rien d'écrit) ;
5. variante « entrées placées dans le dépôt, non suivies » (ce que prévoit la commande du compte 3) : code 0, entrées
   non suivies consignées au manifeste.

    PYTHONPATH=src python -P -B scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py [DOSSIER_DE_TRAVAIL]
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUN = "20261114-120000-t06-factice"
TEXTES = ("prereg/T0.8-base-A-mots-et-cout-v1.md", "prereg/T0.6-organismes-v0-v1.md")
CONTRE_LECTURE = "docs/notes/contre-lecture-factice-v1.md"
MARQUES_T07 = ["T06", "T08", "P3BIS", "NARC"]        # contre-lecture v2, § 5 (configuration de T0.7 non ouverte)
DECIMAL = re.compile(r"\d[.,]\d")
RESULTATS: list = []


def _charger(nom: str, chemin: Path):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


mc = _charger("mots_et_cout_t06_v3", RACINE / "scripts" / "mots_et_cout_t06_v3.py")
fab = _charger("fabrique_factice_mots_et_cout_t06_v1", RACINE / "scripts" / "fabrique_factice_mots_et_cout_t06_v1.py")


def verifier(nom: str, condition: bool, detail: str = "") -> None:
    RESULTATS.append((nom, bool(condition)))
    print(f"{'CONFORME' if condition else 'ÉCART'} — {nom}{(' : ' + detail) if detail else ''}", flush=True)


def git(r: Path, *a: str) -> str:
    return subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True, text=True).stdout


def depot(d: Path) -> Path:
    d.mkdir(parents=True)
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "essai@example.invalid")
    git(d, "config", "user.name", "essai")
    shutil.copy2(RACINE / ".gitignore", d / ".gitignore")            # celui du dépôt : __pycache__/, donnees/, …
    for p in TEXTES + tuple(t + ".sha256" for t in TEXTES) + mc.FICHIERS_PIECE:
        (d / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / p, d / p)
    os.symlink(mc.paquet_controle_ia().parent, d / "src")
    cl = d / CONTRE_LECTURE                                       # C-2 : contre-lecture FACTICE, scellée, commitée
    cl.parent.mkdir(parents=True, exist_ok=True)
    cl.write_text("Contre-lecture FACTICE (essai) : sans vue des données de 7b.\n", encoding="utf-8")
    subprocess.run([sys.executable, "-m", "controle_ia.scellement", "sceller", str(cl)], check=True, capture_output=True,
                   env={**os.environ, "PYTHONPATH": str(d / "src")})
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "code de la pièce")
    return d


def registre(d: Path, e: Path) -> None:
    py = [sys.executable, "-P", "-B", str(d / mc.FICHIERS_PIECE[0])]
    env = {**os.environ, "PYTHONPATH": str(d / "src")}
    commit = git(d, "rev-parse", "HEAD").strip()
    code = d / mc.DOSSIER_CODE / "CODE-MOTS-ET-COUT-T06-v1.json"
    sans = subprocess.run(py + ["ecrire-fichier-code", str(d), commit, str(code)], capture_output=True, text=True, env=env)
    verifier("ecrire-fichier-code sans --contre-lecture : refus (code 2), rien d'écrit (C-2)",
             sans.returncode == 2 and not code.exists(), sans.stderr.strip().splitlines()[-1][:160] if sans.stderr.strip() else "")
    r = subprocess.run(py + ["ecrire-fichier-code", str(d), commit, str(code), "--contre-lecture", str(d / CONTRE_LECTURE)],
                       capture_output=True, text=True, env=env)
    verifier("fichier de CODE-MOTS-ET-COUT-T06 écrit (ecrire-fichier-code --contre-lecture)", r.returncode == 0,
             r.stdout.strip()[-120:])
    lu = json.loads(code.read_text(encoding="utf-8"))
    verifier("fichier de CODE-MOTS-ET-COUT-T06 : contre_lecture citée (chemin relatif, empreinte)",
             lu.get("contre_lecture") == {"chemin": CONTRE_LECTURE, "sha256": mc.sha256_fichier(d / CONTRE_LECTURE)})
    subprocess.run([sys.executable, "-m", "controle_ia.scellement", "sceller", str(code)], check=True, env=env,
                   capture_output=True)
    avant = (datetime.now(timezone.utc) - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    sha_m = hashlib.sha256((e / "runs" / RUN / "manifeste.json").read_bytes()).hexdigest()
    lignes = [("SCELLEMENT-T08-BASE-A", mc.TEXTE_BASE_A[0], mc.TEXTE_BASE_A[1]),
              ("RUN-CONFIRMATION-T06", f"runs/{RUN}/manifeste.json", sha_m),
              ("CODE-MOTS-ET-COUT-T06", str(code.relative_to(d)), hashlib.sha256(code.read_bytes()).hexdigest())]
    (d / "registres" / "scellements-v1.md").write_text(
        "# Registre des scellements (factice, essai)\n\n" + "".join(f"| {k} | {avant} | {p} | {s} |\n" for k, p, s in lignes),
        encoding="utf-8")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "registre factice")
    r = subprocess.run(py + ["verifier-code", "--racine", str(d)], capture_output=True, text=True, env=env)
    verifier("verifier-code : CODE-MOTS-ET-COUT-T06 conforme", r.returncode == 0 and "conforme" in r.stdout, r.stdout.strip())


def lancer(d: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", str(d / mc.FICHIERS_PIECE[1]), "--mode", "reel", *args, RUN], capture_output=True,
                          text=True, env={**os.environ, "PY": sys.executable}, timeout=1800)


def main(argv: list[str]) -> int:
    from controle_ia.t07 import criteres_v1 as cr
    from controle_ia.t07 import lecture_v1 as lv
    from controle_ia.t07 import registre_v1 as rg

    debut = time.time()
    travail = Path(argv[0]) if argv else Path(tempfile.mkdtemp(prefix="essai-mots-et-cout-"))
    travail.mkdir(parents=True, exist_ok=True)
    print(f"essai de bout en bout, mode réel, données FACTICES ; {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"pièce : {mc.FICHIERS_PIECE[0]} {mc.sha256_fichier(RACINE / mc.FICHIERS_PIECE[0])}")
    print(f"lanceur : {mc.FICHIERS_PIECE[1]} {mc.sha256_fichier(RACINE / mc.FICHIERS_PIECE[1])}")
    e = travail / "entrees-7b-factices"
    fab.fabriquer(e, RUN, fab.config_scellee(RACINE), graine=21)
    d = depot(travail / "depot-a")
    registre(d, e)
    r = lancer(d, "--racine-entrees", str(e))
    verifier("lanceur, mode réel, racine d'entrées à part : code 0", r.returncode == 0, r.stderr.strip()[-300:])
    lignes = r.stdout.strip().splitlines()
    print("sortie de la pièce (telle quelle) :")
    for l in lignes:
        print("    " + l)
    verifier("sortie : chemins et empreintes seulement (aucune valeur)", len(lignes) == 5 and all(
        len(l.split()) == 2 and len(l.split()[1]) == 64 for l in lignes[1:]))
    progres_lignes = [l for l in r.stderr.splitlines() if l.startswith("PROGRES")]
    verifier("sortie et progrès : aucun nombre décimal (C-3)", not DECIMAL.search(r.stdout) and progres_lignes
             and not any(DECIMAL.search(l) for l in progres_lignes))
    run_mc = lignes[0].split("run ")[1].split(" ")[0]
    dd = d / "diag" / run_mc
    for nom in (mc.FICHIER_DETAILS, mc.FICHIER_BASE_A, mc.FICHIER_ISSUE):
        p = dd / nom
        ok = p.is_file() and (dd / (nom + ".sha256")).read_text().split()[0] == mc.sha256_fichier(p)
        verifier(f"{nom} présent et scellé", ok)
    det = json.loads((dd / mc.FICHIER_DETAILS).read_text(encoding="utf-8"))
    verifier("base (B) : cout_present lu sur le texte égal à la colonne des mesures factices (R-2765), aucune trace d'unité",
             det["cout_present_ecarts_a_la_colonne_des_mesures"] == {c: 0 for c in mc.CONDITIONS_7B}
             and det["reglages_b"]["traits_cout"][-1] == "cout_present" and "unite_presente_par_condition" not in det)
    sha_issue = mc.sha256_fichier(dd / mc.FICHIER_ISSUE)
    lu = lv.lire_issue_mots_et_cout(dd / mc.FICHIER_ISSUE, sha_issue, 0.95)
    verifier("issue lisible par T0.7 (lire_issue_mots_et_cout)", lu["lisible"], lu.get("motif") or "")
    q = cr.deriver_classe(lu["issue"], True, "egalite")
    verifier("deriver_classe de T0.7 : aucun champ en écart", q["champs_en_ecart"] == [],
             f"issue {lu['issue']['issue_mots_et_cout']} (factice), Q = {q['Q']}")
    m = json.loads((d / "runs" / run_mc / "manifeste.json").read_text())
    verifier("manifeste : décisif, préenregistrement = base (A) scellée, dépôt propre, entropie fixée",
             m["decisif"] and m["preenregistrement"]["sha256"] == mc.TEXTE_BASE_A[1] and m["depot_propre"]
             and all(g["entropie"] == str(mc.ENTROPIE_REELLE) for g in m["graines"].values()))
    verifier("manifeste : commit et empreintes de CODE-MOTS-ET-COUT-T06 consignés",
             m["config"]["code"]["commit"] == git(d, "rev-parse", "HEAD~1").strip())
    b = subprocess.run([sys.executable, "-P", "-B", str(d / mc.FICHIERS_PIECE[0]), "etat-ba-l2", str(dd / mc.FICHIER_BASE_A)],
                       capture_output=True, text=True, env={**os.environ, "PYTHONPATH": str(d / "src")})
    verifier("etat-ba-l2 : un seul état imprimé", b.returncode == 0 and b.stdout.strip() in (
        "BA-L2 : s'applique", "BA-L2 : ne s'applique pas"), b.stdout.strip())
    # gestes de la mère : recopie et lignes, dans cet ordre
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "sorties de la pièce (essai)")
    reg = d / "registres" / "scellements-v1.md"
    t = int(time.time()) - 60
    sha_b = mc.sha256_fichier(dd / mc.FICHIER_BASE_A)
    rg.ajouter_ligne(reg, "LECTURE-T08-BASE-A", t, f"diag/{run_mc}/{mc.FICHIER_BASE_A}", sha_b)
    rg.ajouter_ligne(reg, "ISSUE-MOTS-ET-COUT-T06", t + 1, f"diag/{run_mc}/{mc.FICHIER_ISSUE}", sha_issue)
    print("lignes inscrites (forme exacte) :")
    for l in reg.read_text(encoding="utf-8").splitlines():
        if l.startswith("| ") and any(k in l for k in ("CODE-MOTS", "LECTURE-T08", "ISSUE-MOTS")):
            print("    " + l)
    lignes_t07, ignorees = rg.lire_registre_detail(reg, (rg.ISSUE_MOTS_ET_COUT_T06,), (rg.RUN_CONFIRMATION_T06,), None,
                                                   MARQUES_T07)
    verifier("registre lu par T0.7 : ISSUE lue, CODE et LECTURE ignorées (marques T06, T08)",
             set(lignes_t07) >= {"ISSUE-MOTS-ET-COUT-T06"} and sorted(ignorees) == ["CODE-MOTS-ET-COUT-T06", "LECTURE-T08-BASE-A",
                                                                                   "SCELLEMENT-T08-BASE-A"], str(sorted(ignorees)))
    v = rg.verifier_lignes({"ISSUE-MOTS-ET-COUT-T06": lignes_t07["ISSUE-MOTS-ET-COUT-T06"]}, d, int(time.time()) + 5)
    verifier("ligne ISSUE-MOTS-ET-COUT-T06 : sceau vérifié par registre_v1.verifier_lignes", "ISSUE-MOTS-ET-COUT-T06" in v)
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "lignes de la mère (essai)")
    avant = sorted(x.name for x in (d / "diag").iterdir())
    r2 = lancer(d, "--racine-entrees", str(e))
    verifier("relance après les lignes : refus (code 2), rien d'écrit", r2.returncode == 2 and sorted(
        x.name for x in (d / "diag").iterdir()) == avant, r2.stderr.strip().splitlines()[-1][:160] if r2.stderr.strip() else "")
    # variante : entrées placées dans le dépôt, non suivies
    d2 = depot(travail / "depot-b")
    registre(d2, e)
    for sous in ("runs", "diag", "donnees"):                        # placées après le dernier commit : jamais suivies
        shutil.copytree(e / sous, d2 / sous)
    r3 = lancer(d2)
    verifier("entrées placées dans le dépôt (non suivies) : code 0", r3.returncode == 0, r3.stderr.strip()[-300:])
    if r3.returncode == 0:
        run3 = r3.stdout.strip().splitlines()[0].split("run ")[1].split(" ")[0]
        m3 = json.loads((d2 / "runs" / run3 / "manifeste.json").read_text())
        verifier("variante placée : entrées non suivies consignées (6 : donnees/ est ignoré), dépôt non propre déclaré",
                 len(m3["config"]["arbre"]["entrees_non_suivies"]) == 6 and m3["depot_propre"] is False,
                 ", ".join(m3["config"]["arbre"]["entrees_non_suivies"]))
    n_ok = sum(1 for _, ok in RESULTATS if ok)
    print(f"BILAN : {n_ok} conformes sur {len(RESULTATS)} ; durée {time.time() - debut:.0f} s")
    return 0 if n_ok == len(RESULTATS) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
