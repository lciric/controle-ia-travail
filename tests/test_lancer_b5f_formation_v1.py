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


@pytest.fixture
def racine(tmp_path):
    r = tmp_path / "depot"
    (r / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE_DEPOT / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + _ligne_go(GO) + "\n" + _ligne_go("GO-2026-11-20-02", typ="dépôt") + "\n",
                                          encoding="utf-8")
    (r / fv.REGISTRE_PROPRE).write_text("\n".join([
        en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", f"commit {COMMIT} ; entropie 7", ""),
        en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", GO, "")]) + "\n", encoding="utf-8")
    (r / "scripts").mkdir()
    (r / fv.AMORCE).write_text("#!/usr/bin/env bash\necho amorce jouet\n", encoding="utf-8")
    return r


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


def test_commande_cas_sain_etiquette_accord_et_garde_de_calcul_rejouee(racine):
    r = _lancer("commande", racine, 3, 123456, COMMIT)
    assert r.returncode == 0, r.stderr
    cmd = r.stdout.strip().splitlines()[-1]
    assert cmd.startswith(f"GO_ID={GO} ") and "--label b5f-formation-v1-3" in cmd and "INSTANCE_B5F=3" in cmd
    fv.exiger_garde_de_calcul(racine, cmd, date.today())        # la garde de calcul la laisserait passer


@pytest.mark.parametrize("cas", ["sans_go", "commit", "amorce", "go_hors_registre", "go_non_calcul", "instance", "offre"])
def test_commande_artefacts_aucune_commande_de_creation(racine, cas):
    args, go = ["commande", racine, 3, 123456, COMMIT], GO
    if cas == "sans_go":
        go = None
    elif cas == "commit":
        args[4] = "d" * 40
    elif cas == "amorce":
        (racine / fv.AMORCE).unlink()
    elif cas == "go_hors_registre":
        (racine / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | r |\n", encoding="utf-8")
    elif cas == "go_non_calcul":
        go = "GO-2026-11-20-02"
        (racine / fv.REGISTRE_PROPRE).write_text((racine / fv.REGISTRE_PROPRE).read_text().replace(GO, go))
    elif cas == "instance":
        args[2] = 8
    elif cas == "offre":
        args[3] = "12a"
    r = _lancer(*args, go=go)
    motifs = {"sans_go": "GO_ID absent", "commit": "CODE-FORMATION-B5F", "amorce": "amorce", "go_hors_registre":
              "absent de registres/go.md", "go_non_calcul": "pas « calcul »", "instance": "hors du plan",
              "offre": "identifiant d'offre"}
    assert r.returncode == 2 and "vastai create" not in r.stdout
    assert motifs[cas] in r.stderr, r.stderr


def test_depense_cas_sain_et_artefacts_coupure_et_plafond():
    assert _lancer("depense", 1, 20.0, 1.3, 100.0, 9.1).returncode == 0
    r = _lancer("depense", 1, 25.7, 1.3, 100.0, 9.1)
    assert r.returncode == 2 and "detruire" in r.stderr
    assert _lancer("depense", 7, 14.7, 1.3, 100.0, 9.1).returncode == 2          # coupure de 15 USD de l'instance 7
    assert _lancer("depense", 1, 10.0, 1.3, 198.0, 9.1).returncode == 2          # plafond commun
    assert _lancer("depense", 9, 1.0, 1.3, 1.0, 1.3).returncode == 2             # instance hors du plan


def _verse(racine):
    _git(racine, "init", "-q")
    _git(racine, "config", "user.email", "essai@invalid")
    _git(racine, "config", "user.name", "essai")
    sorties = racine / "donnees" / "run"
    sorties.mkdir(parents=True)
    (sorties / "adaptateur-jumeau.pt").write_bytes(b"poids")
    inv = fv.ecrire_inventaire(sorties, racine, "run")
    _git(racine, "add", "-A")
    _git(racine, "commit", "-q", "-m", "versement")
    return inv, _git(racine, "rev-parse", "HEAD")


def _liste(tmp_path, instances):
    p = tmp_path / "instances.json"
    p.write_text(json.dumps(instances), encoding="utf-8")
    return p


def test_detruire_cas_sain_etiquette_et_versement_prouves(racine, tmp_path):
    inv, tete = _verse(racine)
    liste = _liste(tmp_path, [{"id": 42, "label": "b5f-formation-v1-2"}, {"id": 7, "label": "autre"}])
    r = _lancer("detruire", racine, 42, 2, liste, inv, tete)
    assert r.returncode == 0, r.stderr
    assert f"GO_ID={GO} vastai destroy instance 42 -y" in r.stdout


@pytest.mark.parametrize("cas", ["etiquette", "identifiant", "absente", "non_verse", "sans_go"])
def test_detruire_artefacts_rien_n_est_detruit(racine, tmp_path, cas):
    inv, tete = _verse(racine)
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
