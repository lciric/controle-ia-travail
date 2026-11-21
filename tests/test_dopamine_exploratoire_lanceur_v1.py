"""Lanceur de la machine A100 (exploratoire) : il imprime, il ne lance rien. Chaque garde : cas sain et artefact (R5)."""
import hashlib
import json
import shutil
import subprocess
from datetime import date
from pathlib import Path

import pytest

from controle_ia.dopamine_exploratoire import lanceur_v1 as L
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

RACINE_REELLE = Path(__file__).resolve().parents[1]
AUJ = date(2026, 11, 21)
RUN = "20261121-130000-dopamine-exploratoire-v1-etape-1"
OFFRE = {"id": 123456, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cuda_max_good": 13.0,
         "cpu_ram": 129000, "cpu_cores_effective": 16, "disk_space": 120, "dph_total": 1.19, "storage_cost": 0.3}


def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def depot(tmp_path):
    """Dépôt d'essai : la garde de calcul copiée telle quelle, un registre des accords synthétique, l'amorce, un dépôt
    distant nu ; commit poussé."""
    nu = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(nu)], check=True)
    d = tmp_path / "depot"
    d.mkdir()
    _git(d, "init", "-q")
    _git(d, "config", "user.email", "e@invalid")
    _git(d, "config", "user.name", "essai")
    (d / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE_REELLE / ".claude" / "hooks" / "garde_calcul.py", d / ".claude" / "hooks" / "garde_calcul.py")
    (d / "registres").mkdir()
    (d / "registres" / "go.md").write_text(
        "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
        "| GO-2026-11-21-48 | 2026-11-21 | calcul | étape 1 | 10 USD | 2026-11-24 | Lazar | mot |\n"
        "| GO-2026-11-01-01 | 2026-11-01 | calcul | ancien | 1 USD | 2026-11-02 | Lazar | mot |\n"
        "| GO-2026-11-21-44 | 2026-11-21 | décision | réouverture | — | — | Lazar | mot |\n", encoding="utf-8")
    am = d / L.AMORCE
    am.parent.mkdir(parents=True)
    shutil.copy(RACINE_REELLE / L.AMORCE, am)
    (d / "ctx").mkdir()
    for n in ("contextes.jsonl", "honnetes.json"):
        (d / "ctx" / n).write_text("{}\n")
        sceller(d / "ctx" / n)
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "init")
    _git(d, "remote", "add", "origin", str(nu))
    _git(d, "push", "-q", "origin", "HEAD:refs/heads/prep")
    _git(d, "fetch", "-q", "origin")
    return d


def test_offre_saine_et_artefacts():
    assert L.exiger_offre(OFFRE) == {"id": "123456", "prix_usd_h": 1.19}
    for cle, v in (("gpu_name", "A100 PCIE"), ("dph_total", 1.5), ("num_gpus", 2), ("cuda_max_good", 12.4),
                   ("disk_space", 60), ("storage_cost", 1.0), ("cpu_cores_effective", 8)):
        with pytest.raises(GardeArret):
            L.exiger_offre(dict(OFFRE, **{cle: v}))
    o = dict(OFFRE)
    del o["cpu_ram"]
    with pytest.raises(GardeArret, match="absent"):
        L.exiger_offre(o)


def test_horaires_du_devis():
    h = L.horaires(0, 1.38)
    assert h["fin_lancements_s"] == int(5.5 * 3600) and h["destruction_s"] == int(6.5 * 3600)
    assert 6.5 * 1.38 + L.DEVIS["reseau_max_usd"] <= L.DEVIS["plafond_usd"]           # pire cas payable du devis
    h2 = L.horaires(0, 2.0)                                                            # prix plus haut : destruction avancée
    assert h2["destruction_h"] < 6.5 and h2["destruction_h"] * 2.0 + 0.68 <= 10.0
    with pytest.raises(GardeArret):
        L.horaires(0, 9.0)


def test_garde_de_depense():
    assert L.garde_depense(5.0, 1.2)["projete"] == pytest.approx(5.3)
    with pytest.raises(GardeArret, match="coupure"):
        L.garde_depense(9.7, 1.2)
    with pytest.raises(GardeArret):
        L.garde_depense(-1, 1.2)


def test_commande_saine(depot):
    commit = _git(depot, "rev-parse", "HEAD")
    c = L.commande_de_creation(depot, "1", OFFRE, commit, RUN, "GO-2026-11-21-48", AUJ, 1_000_000.0)
    assert c.startswith("GO_ID=GO-2026-11-21-48 vastai create instance 123456 ")
    assert f"-e COMMIT={commit}" in c and "--label dopamine-exploratoire-v1-etape-1" in c
    assert f"-e FIN_LANCEMENTS_UTC_S={1_000_000 + int(5.5 * 3600)}" in c
    assert f"-e DESTRUCTION_UTC_S={1_000_000 + int(6.5 * 3600)}" in c
    assert "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" in c and "-e CONTEXTES=-" in c
    c2 = L.commande_de_creation(depot, "1", OFFRE, commit, RUN, "GO-2026-11-21-48", AUJ, 0.0,
                                "ctx/contextes.jsonl", "ctx/honnetes.json")
    assert "-e CONTEXTES=ctx/contextes.jsonl -e LISTE_HONNETES=ctx/honnetes.json" in c2


@pytest.mark.parametrize("go,motif", [("GO-2026-11-30-99", "absent"), ("GO-2026-11-01-01", "période"),
                                      ("GO-2026-11-21-44", "calcul"), ("rien", "illisible")])
def test_commande_refusee_sans_go_valide(depot, go, motif):
    commit = _git(depot, "rev-parse", "HEAD")
    with pytest.raises(GardeArret, match=motif):
        L.commande_de_creation(depot, "1", OFFRE, commit, RUN, go, AUJ, 0.0)


def test_commande_refusee_go_revoque(depot):
    with open(depot / "registres" / "go.md", "a", encoding="utf-8") as f:
        f.write("| GO-2026-11-21-60 | 2026-11-21 | révocation | révoque GO-2026-11-21-48 | — | — | Lazar | mot |\n")
    with pytest.raises(GardeArret, match="révoqué"):
        L.commande_de_creation(depot, "1", OFFRE, _git(depot, "rev-parse", "HEAD"), RUN, "GO-2026-11-21-48", AUJ, 0.0)


def test_commande_refusee_autres_artefacts(depot):
    commit = _git(depot, "rev-parse", "HEAD")
    with pytest.raises(GardeArret, match="identifiant de course"):
        L.commande_de_creation(depot, "1", OFFRE, commit, "20261121-130000-dopamine-etape-1", "GO-2026-11-21-48", AUJ, 0)
    with pytest.raises(GardeArret, match="les deux ou aucun"):
        L.commande_de_creation(depot, "1", OFFRE, commit, RUN, "GO-2026-11-21-48", AUJ, 0, "ctx/contextes.jsonl", None)
    with pytest.raises(GardeArret, match="étape"):
        L.commande_de_creation(depot, "2a", OFFRE, commit, RUN, "GO-2026-11-21-48", AUJ, 0)
    (depot / "neuf").write_text("x")
    _git(depot, "add", "neuf")
    _git(depot, "commit", "-q", "-m", "non poussé")
    with pytest.raises(GardeArret, match="branche distante"):
        L.commande_de_creation(depot, "1", OFFRE, _git(depot, "rev-parse", "HEAD"), RUN, "GO-2026-11-21-48", AUJ, 0)


def test_ligne_de_commande_sans_go(depot, monkeypatch, capsys):
    monkeypatch.delenv("GO_ID", raising=False)
    f = depot / "offre.json"
    f.write_text(json.dumps(OFFRE))
    assert L._main(["commande", str(depot), "1", str(f), _git(depot, "rev-parse", "HEAD"), RUN]) == 2
    assert "GO_ID absent" in capsys.readouterr().err
    monkeypatch.setenv("GO_ID", "GO-2026-11-21-48")
    assert L._main(["plan"]) == 0


def _verser(depot, contenu=b"donnees\n"):
    """Sorties d'une course poussées sur la branche de sortie ; rend (commit, inventaire)."""
    _git(depot, "checkout", "-q", "-b", "sortie")
    f = depot / "donnees" / RUN / "generations" / "lot-00000.jsonl"
    f.parent.mkdir(parents=True)
    f.write_bytes(contenu)
    (depot / "runs" / RUN).mkdir(parents=True)
    (depot / "runs" / RUN / "manifeste.json").write_text("{}")
    _git(depot, "add", "-A")
    _git(depot, "commit", "-q", "-m", "sorties")
    _git(depot, "push", "-q", "origin", f"HEAD:refs/heads/{L.BRANCHE_SORTIE}")
    _git(depot, "fetch", "-q", "origin")
    inv = depot.parent / "inventaire-final.json"
    inv.write_text(json.dumps({"run_id": RUN, "fichiers": [
        {"chemin": f"donnees/{RUN}/generations/lot-00000.jsonl", "octets": len(contenu),
         "sha256": hashlib.sha256(contenu).hexdigest(), "verse": True},
        {"chemin": f"donnees/{RUN}/etats/couche-02/lot-00000.npy", "octets": 9, "sha256": "0" * 64, "verse": False}]}))
    sceller(inv)
    return _git(depot, "rev-parse", "HEAD"), inv


def _liste(tmp_path, ident="777", label="dopamine-exploratoire-v1-etape-1"):
    f = tmp_path / "liste.json"
    f.write_text(json.dumps([{"id": int(ident), "label": label}, {"id": 1, "label": "autre"}]))
    return f


def test_destruction_saine_apres_versement_prouve(depot, tmp_path):
    commit, inv = _verser(depot)
    c = L.commande_de_destruction(depot, "777", "1", _liste(tmp_path), inv, commit, "GO-2026-11-21-48")
    assert c == "GO_ID=GO-2026-11-21-48 vastai destroy instance 777 -y"


def test_destruction_refusee_artefacts(depot, tmp_path):
    commit, inv = _verser(depot)
    with pytest.raises(GardeArret, match="R10"):
        L.commande_de_destruction(depot, "77x", "1", _liste(tmp_path), inv, commit, "GO-2026-11-21-48")
    with pytest.raises(GardeArret, match="étiquetée"):
        L.commande_de_destruction(depot, "777", "1", _liste(tmp_path, label="b5f-formation-v1-1"), inv, commit,
                                  "GO-2026-11-21-48")
    d = json.loads(inv.read_text())
    d["fichiers"][0]["sha256"] = "f" * 64
    inv2 = tmp_path / "inv2.json"
    inv2.write_text(json.dumps(d))
    sceller(inv2)
    with pytest.raises(GardeArret, match="empreinte ou taille"):
        L.commande_de_destruction(depot, "777", "1", _liste(tmp_path), inv2, commit, "GO-2026-11-21-48")
    (depot / "local").write_text("x")
    _git(depot, "add", "local")
    _git(depot, "commit", "-q", "-m", "non versé")
    with pytest.raises(GardeArret, match="hors de la branche distante"):
        L.commande_de_destruction(depot, "777", "1", _liste(tmp_path), inv, _git(depot, "rev-parse", "HEAD"),
                                  "GO-2026-11-21-48")


def test_absence_prouvee(tmp_path):
    f = tmp_path / "l.json"
    f.write_text(json.dumps([{"id": 1}, {"id": 2}]))
    L.absence_prouvee(f, "777", "1")
    with pytest.raises(GardeArret, match="encore présente"):
        L.absence_prouvee(f, "2", "1")
    with pytest.raises(GardeArret, match="témoin"):
        L.absence_prouvee(f, "777", "9")
