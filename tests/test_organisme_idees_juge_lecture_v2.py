"""Essais de la lecture v2 et du lecteur v2 : auto-contrôle de l'intervalle, membres à la borne triviale rapportés,
sortie complète exigée (journal, aucun arrêt), empreinte du manifeste comparée, états de contrôle des clés."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from unittest import mock

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import config_canonique
from controle_ia.scellement import empreinte, sceller
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import execution_v2 as X2
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB1
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v2 as LB2
from controle_ia.organisme_idees_juge import mutations_v2 as MU2
from test_organisme_idees_juge_lecture_v1 import fabriquer

DEPOT = Path(__file__).resolve().parents[1]
RAC = 123456789


def _lanceur(nom):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / "scripts" / f"{nom}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _avec_triviaux(s, signalees=(("T", 4), ("N", 2))):
    for t in s["oracle"]["generations"]:
        t["generation"] = f"{t['famille']}{t['g']}"
        t["membres_a_la_borne_triviale"] = ["ajuste_log:archive:S3"] if (t["famille"], t["g"]) in signalees else []
    return s


def test_membres_triviaux_rapportes_sans_toucher_un_critere():
    s = _avec_triviaux(fabriquer())
    r2 = LB2.lire(s, RAC, 300, n_attendus={"N": 500, "T": 750})
    r1 = LB1.lire(copy.deepcopy(s), RAC, 300, n_attendus={"N": 500, "T": 750})
    assert r2["oracle_membres_a_la_borne_triviale"]["generations_signalees"] == 2
    assert r2["audit_R4"]["oracle_membres_a_la_borne_triviale"] == 2
    assert r2["verdict"] == r1["verdict"] and r2["etage_3"] == r1["etage_3"]


def test_lecture_v2_refuse_un_intervalle_mute():
    with mock.patch.object(LB1.Reechantillonneur, "intervalle", MU2._intervalle_90):
        with pytest.raises(GardeArret, match="niveau de l'intervalle"):
            LB2.lire(_avec_triviaux(fabriquer(nT=20, nN=10)), RAC, 300)


def _sortie_scellee(dossier, s, manifeste_sha, journal=True):
    dossier.mkdir(parents=True)
    corps_o = {"run_id": s["run_id"], "manifeste_sha256": manifeste_sha, "resultat": s["oracle"]}
    (dossier / "oracle.json").write_text(json.dumps(corps_o), encoding="utf-8")
    sha_o = sceller(dossier / "oracle.json")
    for g in s["jeu"]["generations"]:
        g["oracle_scelle_sha256"] = sha_o
    (dossier / "jeu.json").write_text(json.dumps({"run_id": s["run_id"], "manifeste_sha256": manifeste_sha, "resultat": s["jeu"]}), encoding="utf-8")
    sceller(dossier / "jeu.json")
    if journal:
        (dossier / "journal.json").write_text(json.dumps({"run_id": s["run_id"], "manifeste_sha256": manifeste_sha, "resultat": {}}), encoding="utf-8")
        sceller(dossier / "journal.json")


def test_sortie_complete_exigee(tmp_path):
    s = _avec_triviaux(fabriquer(nT=20, nN=10))
    s["run_id"] = "r"
    d = tmp_path / "ok"
    _sortie_scellee(d, copy.deepcopy(s), "m" * 64)
    assert LB2.charger_sortie_complete(d, "m" * 64)["run_id"] == "r"                        # sain
    with pytest.raises(GardeArret, match="empreinte du manifeste"):
        LB2.charger_sortie_complete(d, "x" * 64)
    d2 = tmp_path / "sans-journal"
    _sortie_scellee(d2, copy.deepcopy(s), "m" * 64, journal=False)
    with pytest.raises(GardeArret, match="journal"):
        LB2.charger_sortie_complete(d2)
    (d / "arret.json").write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="arret.json"):
        LB2.charger_sortie_complete(d)
    d3 = tmp_path / "ecrit"
    _sortie_scellee(d3, copy.deepcopy(s), "m" * 64)
    c = LB2.ecrire_lecture(d3, RAC, reechantillons=100, manifeste_sha="m" * 64)
    assert c.name == "lecture-gelee-v2.json" and Path(str(c) + ".sha256").is_file()
    with pytest.raises(GardeArret, match="R12"):
        LB2.ecrire_lecture(d3, RAC, reechantillons=100, manifeste_sha="m" * 64)


def _depot_lecteur(tmp_path, alterer_etat=False, autre_sha=False):
    L = _lanceur("jouer_idee_1_2_v2")
    racine = B.racine_de(B.EMPREINTE_PREREG)
    run_id = "20261115-120000-" + X2.NOM_RUN
    config = {"racine_graines": str(racine), "etats_de_controle": L.etats_de_controle(racine)}
    if alterer_etat:
        cle = next(iter(config["etats_de_controle"]))
        config["etats_de_controle"][cle] = [1, 2]
    m = {"run_id": run_id, "decisif": True, "preenregistrement": {"chemin": B.CHEMIN_PREREG, "sha256": B.EMPREINTE_PREREG},
         "config": config, "config_sha256": hashlib.sha256(config_canonique(config)).hexdigest()}
    pm = tmp_path / "runs" / run_id / "manifeste.json"
    pm.parent.mkdir(parents=True)
    pm.write_text(json.dumps(m), encoding="utf-8")
    sha_m = sceller(pm)
    s = _avec_triviaux(fabriquer())
    s["run_id"] = run_id
    _sortie_scellee(tmp_path / X2.DOSSIER_DIAG / run_id, s, "z" * 64 if autre_sha else sha_m)
    return pm, run_id


def test_lecteur_v2_cas_sain_et_artefacts(tmp_path):
    lecteur = _lanceur("lire_idee_1_2_v2")
    pm, run_id = _depot_lecteur(tmp_path / "sain")
    with mock.patch.object(lecteur, "RACINE_DEPOT", tmp_path / "sain"):
        assert lecteur.main(["--manifeste", str(pm.relative_to(tmp_path / "sain"))]) == 0
    assert (tmp_path / "sain" / X2.DOSSIER_DIAG / run_id / "lecture-gelee-v2.json.sha256").is_file()
    for nom, k, motif in (("etat", {"alterer_etat": True}, "état de contrôle"), ("sha", {"autre_sha": True}, "empreinte du manifeste")):
        racine = tmp_path / nom
        pm, _ = _depot_lecteur(racine, **k)
        with mock.patch.object(lecteur, "RACINE_DEPOT", racine):
            with pytest.raises(GardeArret, match=motif):
                lecteur.main(["--manifeste", str(pm.relative_to(racine))])
