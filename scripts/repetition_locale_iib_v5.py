"""Répétition locale, en mode jouet, de la chaîne de l'étalonnage de l'organisme retenu (vérification de la contre-lecture, R2).

Bout en bout, **sans loueur ni dépense** : un faux outil de location (aucun réseau), un dépôt source factice et son origine
locale, le lanceur de session en version 3 (`scripts/lancer_iib_v3.sh` : outil, contrôles, création — la commande est imprimée,
jamais exécutée —, après-création, surveillance, destruction), l'amorce en version 5 jouée en essai local
(`AMORCE_ESSAI_LOCAL=1` : aucune minuterie, aucun appel au loueur) avec le vrai lanceur `controle_ia.iib.lanceur_v5` sur le
monde jouet, puis les conditions de départ et la désignation sur les sorties rapatriées (`--phase conditions`).
Usage : PYTHONPATH=src python3 scripts/repetition_locale_iib_v5.py DOSSIER_NEUF [--liste-figee]
Sans `--liste-figee`, l'amorce joue une suite courte (TESTS_ARGS, permis en mode jouet) ; avec, la liste figée entière.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(RACINE / "src"), str(RACINE / "tests")]
from controle_ia.iib import configuration_v5 as cf  # noqa: E402
from controle_ia.iib import lanceur_v5 as la  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from test_iib_lanceur_forme_v2 import FAUX_OUTIL  # noqa: E402
from test_iib_scripts_v1 import LIGNE_7B, SAIN, lignes_go  # noqa: E402
from test_t06_v12_amorce import CONFIG_E2, DF_FACTICE, _dates_epreuve  # noqa: E402
from test_t06_v12_scripts import OFFRES  # noqa: E402

ID, AUTRE = "61414494", 58936096
ATTENDUS = 283        # essais de la liste figée (`scripts/tests-cibles-iib-v5-v6.txt`, correctif 0014 : 275 et les 8 de la poussée par lot)
CONFIG = "prereg/config-iib-v5-jouet.json"
RECHERCHE = '''"search offers")
    case "$3" in id=*) echo '[]'; exit 0;; esac
    cat "$FAUX_OFFRES"; exit 0 ;;
'''


def dire(*a):
    print(*a, flush=True)


def git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, check=True).stdout.strip()


def monde(t: Path) -> dict:
    """Dépôt source factice : le code et les essais de l'arbre, registres factices, configuration jouet en version 5 scellée."""
    src = t / "source"
    for rel in ("src/controle_ia", "tests", "scripts"):
        shutil.copytree(RACINE / rel, src / rel, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for rel in (".claude/hooks/garde_calcul.py", ".gitignore", "pyproject.toml"):
        if (RACINE / rel).is_file():
            (src / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RACINE / rel, src / rel)
    for f in sorted((RACINE / "docs/notes/barreau8-iib-v1").glob("config-iib-organisme-retenu-v5-gabarit-v*.json*")):       # lus par les essais
        (src / "docs/notes/barreau8-iib-v1").mkdir(parents=True, exist_ok=True)
        shutil.copy(f, src / "docs/notes/barreau8-iib-v1" / f.name)
    (src / "registres").mkdir()
    (src / "registres" / "go.md").write_text(lignes_go(), encoding="utf-8")
    (src / "registres" / "decisions.md").write_text(f"| R-0001 | registre factice |\n| {LIGNE_7B} |\n", encoding="utf-8")
    for d in ("runs", "diag"):
        (src / d).mkdir()
        (src / d / ".gitkeep").write_text("", encoding="utf-8")
    c = cf.gabarit("jouet", 20261121)
    pieces = {"conception": "pièce factice", "consigne_maitre_N": "consigne factice N", "consigne_maitre_P": "consigne factice P",
              "consigne_flagrant": "consigne factice du flagrant",
              "taches_reserve": json.dumps({"taches": [{"identifiant": f"r{k}"} for k in range(32)]}),
              "taches_evaluation": json.dumps({"taches": [{"identifiant": f"v{k}"} for k in range(8)]}),
              "entrees": json.dumps({"schema": cf.SCHEMA_ENTREES, "plafond_usd": 45, "depense_passee_usd": 0, "cout_fixe_usd": 6.90,
                                     "prix_horaire_usd": 1.38, "oracles_par_tour": 1, "actions_oracle_hors_tours": 3830,
                                     "plafond_de_tours": {"forme": "formule", "formule": cf.FORMULE_PLAFOND_DE_TOURS}})}
    for nom, texte in pieces.items():
        f = src / "prereg" / f"iib-v5-jouet-{nom}.json"
        f.parent.mkdir(exist_ok=True)
        f.write_text(texte + "\n", encoding="utf-8")
        c["pieces"][nom] = {"chemin": str(f.relative_to(src)), "sha256": sceller(f)}
    sha_module = hashlib.sha256((src / cf.MODULE_DE_LECTURE).read_bytes()).hexdigest()
    e2 = json.loads(CONFIG_E2.read_text(encoding="utf-8"))
    _, ech, fin = _dates_epreuve()
    c.update({"go_id": SAIN, "prefixe_graines": "repetition/", "instances_intouchables": [AUTRE], "jouet": {},
              "code": {"branche": "prep/iib-repetition", "commit": "0" * 40, "module_de_lecture": {"chemin": cf.MODULE_DE_LECTURE, "sha256": sha_module}},
              "marqueurs": {"EMPREINTES_CODE_IIB": f"{cf.MODULE_DE_LECTURE} {sha_module}"},
              "plafond": dict(cf.DEVIS["plafond"]), "plafond_usd": 55, "carte": e2["carte"],
              "offre": {**e2["offre"], "etiquette": "iib-explo-v5", "disque_min_go": 100},
              "calendrier": {"dernier_jour_creation": str(ech - timedelta(days=1)), "fin_go_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ")},
              "prealables": {"ligne_registre_creation_7b": LIGNE_7B}})
    (src / CONFIG).write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(src / CONFIG)
    subprocess.run(["git", "init", "-q", "-b", "main", str(src)], check=True)
    git(src, "config", "user.email", "t@example.invalid")
    git(src, "config", "user.name", "t")
    git(src, "add", "-A")
    git(src, "commit", "-qm", "monde factice de la répétition")
    origine = t / "origine.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(src), str(origine)], check=True)
    git(src, "remote", "add", "origin", str(origine))
    git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/iib-repetition")
    git(src, "fetch", "-q", "origin", "refs/heads/prep/iib-repetition:refs/remotes/origin/prep/iib-repetition")
    outil = t / "outil-vastai-factice" / "bin" / "vastai"
    outil.parent.mkdir(parents=True)
    outil.write_text(FAUX_OUTIL.replace('case "$1 $2" in\n', 'case "$1 $2" in\n' + RECHERCHE, 1), encoding="utf-8")
    outil.chmod(0o755)
    b = t / "bin"
    b.mkdir()
    (b / "df").write_text(DF_FACTICE, encoding="utf-8")
    (b / "df").chmod(0o755)
    (t / "offres.json").write_text(json.dumps(OFFRES), encoding="utf-8")
    venv = t / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    (venv / "bin" / "python").write_text(f'#!/usr/bin/env bash\nexec "{sys.executable}" "$@"\n', encoding="utf-8")
    (venv / "bin" / "python").chmod(0o755)
    return {"t": t, "src": src, "origine": origine, "outil": outil, "bin": b, "venv": venv, "commit": git(src, "rev-parse", "HEAD"), "config": c}


def session(m: dict, *args, attendu=0, **sup) -> str:
    """Une sous-commande du lanceur de session en version 3, faux outil, aucun réseau."""
    t = m["t"]
    e = {"PATH": f"{m['bin']}:/usr/local/bin:/usr/bin:/bin", "HOME": str(t), "LANG": os.environ.get("LANG", "C.UTF-8"), "IIB_DEPOT": str(m["src"]),
         "VAST": str(m["outil"]), "FAUX_VASTAI_JOURNAL": str(t / "appels.txt"), "FAUX_INSTANCES": str(t / "inventaire.json"),
         "FAUX_JOURNAL": str(t / "journal-instance.txt"), "FAUX_OFFRES": str(t / "offres.json"), "HF_TOKEN": "hf_FACTICEfactice0123456789",
         "CONTROLE_IA_GITHUB_TOKEN_2": "ghp_FACTICEfactice0123456789", "VAST_API_KEY": "cle-loueur-factice-0123456789abcdef", "INTERVALLE": "1",
         "IIB_DESTRUCTION_ATTENTE_S": "0", "IIB_DESTRUCTION_RELECTURES": "2", "GO_ID": SAIN, "IIB_REGISTRE_GO": str(m["src"] / "registres" / "go.md"),
         "IIB_BRANCHE_CODE": "prep/iib-repetition", "IIB_DEPENSE_ANTERIEURE_USD": "0", "IIB_TESTS_ATTENDUS": "",
         **la.environnement_du_lanceur_de_session(m["config"])}
    e.update(sup)
    e = {k: v for k, v in e.items() if v is not None}
    r = subprocess.run(["bash", str(m["src"] / "scripts" / "lancer_iib_v3.sh"), *map(str, args)], env=e, capture_output=True, text=True, timeout=300,
                       stdin=subprocess.DEVNULL)
    dire(f"\n$ lancer_iib_v3.sh {' '.join(map(str, args[:2]))} …  → code {r.returncode}")
    for ligne in (r.stdout + r.stderr).strip().splitlines()[-8:]:
        dire("   " + ligne[:260])
    if r.returncode != attendu:
        raise SystemExit(f"ÉCHEC DE LA RÉPÉTITION : code {r.returncode} au lieu de {attendu} ({args[0]})")
    return r.stdout


def main(argv: list[str]) -> int:
    t = Path(argv[0]).resolve()
    figee = "--liste-figee" in argv
    if t.exists():
        raise SystemExit(f"{t} existe déjà : dossier neuf exigé (R12)")
    t.mkdir(parents=True)
    dire(f"RÉPÉTITION LOCALE, MODE JOUET, {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} — aucun loueur, aucune dépense ; dossier {t}")
    m = monde(t)
    (t / "inventaire.json").write_text(json.dumps([{"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    d = t / "session"
    # 1. lanceur de session : outil, contrôles, création (commande imprimée, jamais exécutée)
    session(m, "outil")
    sortie = session(m, "controles-explo", d, m["commit"], CONFIG)
    assert "CONTRÔLES CONFORMES" in sortie, sortie[-600:]
    cmd = session(m, "creation", "auto", "course", "0", d).splitlines()[-1]
    assert "create instance" in cmd and "-e MODE=jouet" in cmd and "--label iib-explo-v5" in cmd and "-e BRANCHE=essai/iib-explo-v5" in cmd, cmd[:400]
    assert "create instance" not in (t / "appels.txt").read_text(encoding="utf-8")
    env_cmd = dict(re.findall(r"-e ([A-Z_0-9]+)=([^ \"\\]+)", cmd))
    dire(f"\ncommande de création imprimée (non exécutée) ; variables passées à l'instance : {sorted(env_cmd)}")
    # 2. l'instance : l'amorce en version 5 telle que la création l'a relevée au commit, en essai local
    amorce = d / "amorce-creation.sh"
    assert amorce.read_bytes() == (RACINE / "scripts" / "amorce_instance_iib_v5.sh").read_bytes()
    inst = t / "instance"
    inst.mkdir()
    env = {k: os.environ[k] for k in ("PATH", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    env.update({k: v for k, v in env_cmd.items() if k not in ("HF_TOKEN", "GH_TOKEN", "DEPOT_URL")})
    env.update(DEPOT_URL=str(m["origine"]), GH_TOKEN="jeton-factice", HF_TOKEN="jeton-hf-factice", RACINE_AMORCE=str(inst), VENV_EXISTANT=str(m["venv"]),
               HOME=str(t), AMORCE_ESSAI_LOCAL="1", POUSSEE_ATTENTE_S="0")
    env.pop("IIB_TOKENISEUR_REEL", None)
    if figee:
        env["TESTS_ATTENDUS"] = str(ATTENDUS)             # le contrôle du nombre de tests attendus est joué lui aussi
    else:
        env["TESTS_ARGS"] = "tests/test_iib_regle_v5.py tests/test_iib_designation_v5.py"
    debut = time.time()
    r = subprocess.run(["bash", str(amorce)], env=env, capture_output=True, text=True, timeout=3000)
    journal = (inst / "iib" / "journal.txt").read_text(encoding="utf-8") if (inst / "iib" / "journal.txt").exists() else ""
    dire(f"\n$ bash amorce_instance_iib_v5.sh (AMORCE_ESSAI_LOCAL=1, MODE=jouet, {'liste figée' if figee else 'suite courte'})  → code {r.returncode}, {time.time() - debut:.0f} s")
    lignes = journal.strip().splitlines()
    for ligne in [l for l in lignes if "PROGRES" not in l][:60]:
        dire("   " + ligne[:230])
    progres = [l for l in lignes if l.startswith("PROGRES ")]
    dire(f"   … {len(progres)} lignes PROGRES relayées ; première : {progres[0] if progres else '-'} ; dernière : {progres[-1] if progres else '-'}")
    if r.returncode != 0 or not (inst / "iib-fin-normale").exists():
        dire((r.stdout + r.stderr)[-3000:])
        raise SystemExit("ÉCHEC DE LA RÉPÉTITION : l'amorce n'a pas fini normalement")
    branche = env_cmd["BRANCHE"]
    fichiers = git(m["origine"], "ls-tree", "-r", "--name-only", branche).splitlines()
    run = next(f.split("/")[1] for f in fichiers if f.startswith("runs/") and f.endswith("manifeste.json"))
    lots = [f for f in fichiers if f.startswith(f"diag/{run}/lots/lot-") and f.endswith(".json")]
    ids = [f for f in fichiers if f.startswith(f"donnees/{run}/lots/ids-lot-") and f.endswith(".json")]
    assert len(lots) == 28 and len(ids) == 28 and f"diag/{run}/resume.json" in fichiers and f"diag/{run}/{la.NOMS['etalonnage']}" in fichiers
    # correctif 0014 : chaque lot est parti sur la branche dès qu'il a été scellé (un commit « versement lot … » par lot, poussé)
    par_lot = [s for s in git(m["origine"], "log", "--format=%s", branche).splitlines() if "(versement lot " in s]
    poussees = [l for l in progres if "etape=versement" in l]
    assert len(par_lot) == 28 and len(poussees) == 28 and all("poussee=faite" in l for l in poussees), (len(par_lot), poussees[-3:])
    dire(f"\nbranche {branche} poussée sur l'origine locale : run {run} ; {len(lots)} lots d'oracle, {len(ids)} lots d'identifiants, résumé et étalonnage présents ; "
         f"{len(par_lot)} poussées par lot, toutes vérifiées par le lanceur")
    # 3. lanceur de session : après-création, surveillance, destruction (faux outil)
    reponse = d / "creation-brute-essai1.json"
    reponse.write_text(json.dumps({"success": True, "new_contract": int(ID)}), encoding="utf-8")
    assert f"CRÉÉE : instance {ID}" in session(m, "apres-creation", reponse, 0, d)
    (t / "journal-instance.txt").write_text(r.stdout + journal, encoding="utf-8")
    (t / "inventaire.json").write_text(json.dumps([{"id": int(ID), "label": "iib-explo-v5", "actual_status": "exited"},
                                                    {"id": AUTRE, "label": "a1-v4", "actual_status": "running"}]), encoding="utf-8")
    assert "FIN" in session(m, "surveillance", ID, d)
    # artefacts de la destruction : l'attestation « aucune intouchable » est refusée ; la liste vide aussi ; une intouchable n'est jamais détruite
    session(m, "destruction", ID, d, attendu=2, RAPATRIEMENT_VERIFIE="oui", IIB_INSTANCES_INTOUCHABLES=None, IIB_AUCUNE_INTOUCHABLE="oui")
    session(m, "destruction", ID, d, attendu=2, RAPATRIEMENT_VERIFIE="oui", IIB_INSTANCES_INTOUCHABLES="")
    session(m, "destruction", AUTRE, d, attendu=2, RAPATRIEMENT_VERIFIE="oui")
    assert "DÉTRUITE" in session(m, "destruction", ID, d, RAPATRIEMENT_VERIFIE="oui")
    reste = [i["id"] for i in json.loads((t / "inventaire.json").read_text(encoding="utf-8"))]
    appels = (t / "appels.txt").read_text(encoding="utf-8").splitlines()
    assert reste == [AUTRE] and [a for a in appels if a.startswith("destroy")] == [f"destroy instance {ID} -y"]
    assert not any(a.startswith("create") for a in appels)
    dire(f"\ninventaire après destruction : {reste} (la machine de l'autre chantier n'est pas touchée) ; appels au faux outil : "
         f"{len(appels)}, dont création 0, destruction 1")
    # 4. sur processeur : conditions de départ et désignation, une fois, sur les sorties rapatriées
    rap = t / "rapatriement"
    subprocess.run(["git", "clone", "-q", "--branch", branche, str(m["origine"]), str(rap)], check=True)
    e = {k: v for k, v in os.environ.items() if k != "IIB_GO_ID"}
    e.update(PYTHONPATH=str(rap / "src"), PATH="/usr/bin:/bin")
    base = [sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--phase", "conditions", "--config", CONFIG, "--run-id", run]
    c1 = subprocess.run(base, cwd=rap, env=e, capture_output=True, text=True, timeout=300)
    c2 = subprocess.run(base, cwd=rap, env=e, capture_output=True, text=True, timeout=300)
    dire(f"\n$ python -m controle_ia.iib.lanceur_v5 --phase conditions  → code {c1.returncode} : {c1.stdout.strip()}")
    dire(f"$ (second passage)  → code {c2.returncode} : {c2.stderr.strip().splitlines()[-1][:200] if c2.stderr.strip() else ''}")
    assert c1.returncode == 0 and c2.returncode == 1 and "second passage" in c2.stderr
    des = json.loads((rap / "diag" / run / la.NOMS["designation"]).read_text(encoding="utf-8"))
    dire(f"désignation scellée : issue {des['issue']}, tours {des['tours']}")
    for p in des["phrases"]:
        dire("   " + p[:300])
    dire("\nRÉPÉTITION RÉUSSIE : lanceur de session v3, amorce v5, lanceur v5 (étalonnage jouet versé par lot, poussé), destruction par identifiant, "
         "conditions et désignation — bout en bout, sans loueur ni dépense.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
