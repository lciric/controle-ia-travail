"""Essais hors ligne du lanceur de formation du barreau 5 (`scripts/lancer_b5f_formation_v1.sh`) : il ne crée, n'arrête
ni ne détruit rien ; il contrôle et imprime. Cas sain et artefact pour chaque garde (R5). Dépôt jetable, registres
fabriqués ; la garde de calcul du dépôt est copiée telle quelle."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
SCRIPT = RACINE_DEPOT / "scripts" / "lancer_b5f_formation_v1.sh"
COMMIT = "c" * 40
GO = "GO-2026-11-20-01"


def _git(r, *args):
    return subprocess.run(["git", "-C", str(r), *args], check=True, capture_output=True, text=True).stdout.strip()


def _ligne_go(ident, typ="calcul", par="Lazar"):
    a, e = date.today() - timedelta(days=1), date.today() + timedelta(days=10)
    return f"| {ident} | {a.isoformat()} | {typ} | formation barreau 5 | 200 USD | {e.isoformat()} | {par} | essai |"


OFFRE = {"id": 123456, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 32,
         "cpu_ram": 257000, "disk_space": 200, "cuda_max_good": 13.0, "dph_total": 1.2, "storage_cost": 0.1}
PREREG = "prereg/barreau5-essai.md"
RUN = "20261123-080000-b5f-formation-3"


def _registre_propre(r, code_commit, go=GO):
    (r / fv.REGISTRE_PROPRE).write_text("\n".join([
        en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", f"commit {code_commit} ; entropie 7", ""),
        en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", go, "")]) + "\n", encoding="utf-8")


@pytest.fixture
def racine(tmp_path):
    """Dépôt jetable à deux commits : le code (garde de calcul copiée, amorce jouet, configuration scellée de la course de
    confirmation), puis la course (registre propre qui cite le commit du code). Rend (racine, commit de la course)."""
    r = tmp_path / "depot"
    (r / ".claude" / "hooks").mkdir(parents=True)
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    shutil.copy(RACINE_DEPOT / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "prereg").mkdir()
    for f in (fv.CONFIG_SCELLEE["chemin"], fv.CONFIG_SCELLEE["chemin"] + ".sha256"):
        shutil.copy(RACINE_DEPOT / f, r / f)
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + _ligne_go(GO) + "\n" + _ligne_go("GO-2026-11-20-02", typ="dépôt") + "\n",
                                          encoding="utf-8")
    (r / "scripts").mkdir()
    (r / fv.AMORCE).write_text("#!/usr/bin/env bash\necho amorce jouet\n", encoding="utf-8")
    (r / "offre.json").write_text(json.dumps(OFFRE), encoding="utf-8")
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "code")
    code = _git(r, "rev-parse", "HEAD")
    _registre_propre(r, code)
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "course")
    return r, _git(r, "rev-parse", "HEAD")


def _commande(r, commit, n=3, offre=None, run=RUN):
    return ["commande", r, n, offre or (r / "offre.json"), commit, "main", PREREG, run]


def _lancer(*args, go=GO):
    env = {k: v for k, v in os.environ.items() if k != "GO_ID"}
    env["PYTHON_B5F"] = sys.executable
    if go is not None:
        env["GO_ID"] = go
    return subprocess.run(["bash", str(SCRIPT), *map(str, args)], capture_output=True, text=True, env=env, timeout=120)


def test_plan_sept_instances_etiquetees():
    r = _lancer("plan")
    assert r.returncode == 0
    lignes = [x for x in r.stdout.splitlines() if x.startswith("b5f-formation-v1-")]
    assert [x.split("\t")[0] for x in lignes] == [f"b5f-formation-v1-{n}" for n in range(1, 8)]


def test_commande_cas_sain_etiquette_accord_echeance_et_garde_de_calcul_rejouee(racine):
    import base64
    import time

    r, course = racine
    avant = time.time()
    p = _lancer(*_commande(r, course))
    assert p.returncode == 0, p.stderr
    cmd = p.stdout.strip().splitlines()[-1]
    assert cmd.startswith(f"GO_ID={GO} vastai create instance 123456 ") and "--label b5f-formation-v1-3" in cmd
    for v in ("INSTANCE_B5F=3", f"COMMIT={course}", "BRANCHE_CODE=main", f"PREREG={PREREG}", f"RUN_B5F={RUN}",
              "PRIX_USD_H=1.2", "HF_TOKEN=\\$HF_TOKEN", "GH_TOKEN=\\$GH_TOKEN"):
        assert v in cmd
    arret = int(cmd.split("ECHEANCE_ARRET_UTC_S=")[1].split()[0])
    assert abs(arret - (avant + (26.0 / 1.2 - 0.25) * 3600)) < 120          # cumul plus un quart d'heure = coupure
    b64 = cmd.split("echo ")[1].split(" |")[0]
    assert base64.b64decode(b64) == (r / fv.AMORCE).read_bytes()
    fv.exiger_garde_de_calcul(r, cmd, date.today())               # la garde de calcul la laisserait passer


@pytest.mark.parametrize("cas", ["sans_go", "code_change", "code_non_ancetre", "amorce", "go_hors_registre",
                                 "go_non_calcul", "instance", "offre_chere", "offre_carte", "offre_cuda", "run"])
def test_commande_artefacts_aucune_commande_de_creation(racine, cas):
    r, course = racine
    go, n, offre, run = GO, 3, None, RUN
    if cas == "sans_go":
        go = None
    elif cas == "code_change":                       # code modifié après le commit de CODE-FORMATION-B5F
        (r / "src").mkdir()
        (r / "src" / "x.py").write_text("x = 1\n")
        _git(r, "add", "-A")
        _git(r, "commit", "-q", "-m", "code changé")
        course = _git(r, "rev-parse", "HEAD")
    elif cas == "code_non_ancetre":
        _registre_propre(r, "d" * 40)
        _git(r, "commit", "-q", "-am", "registre faux")
        course = _git(r, "rev-parse", "HEAD")
    elif cas == "amorce":                            # code cité sans amorce (retirer l'amorce change le code : autre motif)
        _git(r, "rm", "-q", fv.AMORCE)
        _git(r, "commit", "-q", "-m", "code sans amorce")
        _registre_propre(r, _git(r, "rev-parse", "HEAD"))
        _git(r, "commit", "-q", "-am", "course sans amorce")
        course = _git(r, "rev-parse", "HEAD")
    elif cas == "go_hors_registre":
        (r / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | r |\n", encoding="utf-8")
    elif cas == "go_non_calcul":
        go = "GO-2026-11-20-02"
        _registre_propre(r, _git(r, "rev-parse", "HEAD~1"), go)
        _git(r, "commit", "-q", "-am", "accord d'un autre type")
        course = _git(r, "rev-parse", "HEAD")
    elif cas == "instance":
        n, run = 8, "20261123-080000-b5f-formation-8"
    elif cas == "run":
        run = "20261123-080000-b5f-formation-4"
    else:
        o = dict(OFFRE)
        o.update({"offre_chere": {"dph_total": 1.35}, "offre_carte": {"gpu_name": "H100 SXM5"},
                  "offre_cuda": {"cuda_max_good": 12.8}}[cas])
        offre = r / "offre-artefact.json"
        offre.write_text(json.dumps(o), encoding="utf-8")
    p = _lancer(*_commande(r, course, n, offre, run), go=go)
    motifs = {"sans_go": "GO_ID absent", "code_change": "CODE-FORMATION-B5F", "code_non_ancetre": "CODE-FORMATION-B5F",
              "amorce": "amorce", "go_hors_registre": "absent de registres/go.md", "go_non_calcul": "pas « calcul »",
              "instance": "hors du plan", "offre_chere": "dph_total", "offre_carte": "carte", "offre_cuda": "cuda_max_good",
              "run": "identifiant de marche"}
    assert p.returncode == 2 and "vastai create" not in p.stdout
    assert motifs[cas] in p.stderr, p.stderr


def test_config_reelle_de_chaque_instance_cas_sain_et_artefact_prix(racine):
    r, _ = racine
    for n in range(1, 8):
        p = _lancer("config", RACINE_DEPOT, n, 1.25)
        assert p.returncode == 0, p.stderr
        c = json.loads(p.stdout)
        assert c["mode"] == "reel" and c["instance"] == n and c["familles"] == list(fv.familles_de(n))
        assert c["coupure_usd"] == fv.COUPURES_USD[n] and c["prix_usd_h"] == 1.25 and c["go_id"] == GO
        assert c["adaptateur"]["rang"] == 16 and c["distillation"]["epoques"] == 3     # recette scellée
    assert _lancer("config", RACINE_DEPOT, 1, 1.40).returncode == 2              # au-dessus du prix du devis


def test_depense_cas_sain_et_artefacts_coupure_et_plafond():
    assert _lancer("depense", 1, 20.0, 1.3, 100.0, 9.1).returncode == 0
    r = _lancer("depense", 1, 25.7, 1.3, 100.0, 9.1)
    assert r.returncode == 2 and "detruire" in r.stderr
    assert _lancer("depense", 7, 14.7, 1.3, 100.0, 9.1).returncode == 2          # coupure de 15 USD de l'instance 7
    assert _lancer("depense", 1, 10.0, 1.3, 198.0, 9.1).returncode == 2          # plafond commun
    assert _lancer("depense", 9, 1.0, 1.3, 1.0, 1.3).returncode == 2             # instance hors du plan


def _verse(tmp_path):
    racine = tmp_path / "verse"
    racine.mkdir()
    _git(racine, "init", "-q")
    _git(racine, "config", "user.email", "essai@invalid")
    _git(racine, "config", "user.name", "essai")
    sorties = racine / "donnees" / "run"
    sorties.mkdir(parents=True)
    (sorties / "adaptateur-jumeau.pt").write_bytes(b"poids")
    inv = fv.ecrire_inventaire(sorties, racine, "run")
    _git(racine, "add", "-A")
    _git(racine, "commit", "-q", "-m", "versement")
    return racine, inv, _git(racine, "rev-parse", "HEAD")


def _liste(tmp_path, instances):
    p = tmp_path / "instances.json"
    p.write_text(json.dumps(instances), encoding="utf-8")
    return p


def test_detruire_cas_sain_etiquette_et_versement_prouves(tmp_path):
    racine, inv, tete = _verse(tmp_path)
    liste = _liste(tmp_path, [{"id": 42, "label": "b5f-formation-v1-2"}, {"id": 7, "label": "autre"}])
    r = _lancer("detruire", racine, 42, 2, liste, inv, tete)
    assert r.returncode == 0, r.stderr
    assert f"GO_ID={GO} vastai destroy instance 42 -y" in r.stdout


@pytest.mark.parametrize("cas", ["etiquette", "identifiant", "absente", "non_verse", "sans_go"])
def test_detruire_artefacts_rien_n_est_detruit(tmp_path, cas):
    racine, inv, tete = _verse(tmp_path)
    instances, ident, go, commit = [{"id": 42, "label": "b5f-formation-v1-2"}], "42", GO, tete
    if cas == "etiquette":
        instances = [{"id": 42, "label": "bbis-t07-v1"}]
    elif cas == "identifiant":
        ident = "42x"
    elif cas == "absente":
        ident = "43"
    elif cas == "sans_go":
        go = None
    elif cas == "non_verse":
        (racine / "donnees" / "run" / "adaptateur-jumeau.pt").write_bytes(b"autre")
        _git(racine, "commit", "-q", "-am", "changé")
        commit = _git(racine, "rev-parse", "HEAD")
    r = _lancer("detruire", racine, ident, 2, _liste(tmp_path, instances), inv, commit, go=go)
    assert r.returncode == 2 and "destroy" not in r.stdout


def test_verifier_destruction_cas_sain_et_artefacts(tmp_path):
    assert _lancer("verifier-destruction", _liste(tmp_path, [{"id": 7}]), 42, 7).returncode == 0
    assert _lancer("verifier-destruction", _liste(tmp_path, [{"id": 7}, {"id": 42}]), 42, 7).returncode == 2
    assert _lancer("verifier-destruction", _liste(tmp_path, []), 42, 7).returncode == 2


def test_sous_commande_inconnue_refusee():
    assert _lancer("arreter-tout").returncode == 2
