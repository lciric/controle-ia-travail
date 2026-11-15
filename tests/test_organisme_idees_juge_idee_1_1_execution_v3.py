"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — enchaînement du jeu en miniature (hors du dépôt, racine d'essai) :
tranches scellées, reprise, arrêt consigné qui interdit la reprise, lecture refusée d'une sortie incomplète ; lanceurs
(refus sans addendum, répétition miniature) ; banc de mutations : toutes tuées, cas sains passés."""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import verifier
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import execution_idee_1_1_v3 as X
from controle_ia.organisme_idees_juge import mutations_idee_1_1_v3 as MU
from controle_ia.organisme_idees_juge import vue_v9_v1 as VV

RACINE_DEPOT = Path(__file__).resolve().parents[1]
RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v1, execution").hexdigest(), 16)


def _env():
    return {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/tmp"), "LANG": "C.UTF-8",
            "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1"}


def test_fichiers_geles_et_essais_existent():
    for f in X.FICHIERS_GELES:
        assert (RACINE_DEPOT / f).is_file(), f
    assert len(X.ESSAIS) == 7
    assert len(X.taches()) == 30 * 20


def test_jeu_miniature_tranches_reprise_et_arret(tmp_path):
    d = tmp_path / "run"
    liste = [(B.INDICE["H7"], 0, 1), (B.INDICE["Hs"], 0, 1)]
    args = (RACINE_ESSAI, liste[0][0], 0, 1, (), str(d), "essai", "manifeste-essai", time.time())
    r = X._tache(args)                                       # une tranche déjà écrite (interruption simulée)
    assert verifier(d / "lignes" / f"{X.nom_tranche(liste[0][0], 0)}.json") == r["sha256"]
    journal = {}
    res = X.executer(racine=RACINE_ESSAI, dossier=d, run_id="essai", manifeste_sha="manifeste-essai", processus=1,
                     reductions=(), debut=time.time(), journal=journal, liste=liste)
    assert journal["reprises"][0]["tranches_deja_ecrites"] == 1 and journal["reprises"][0]["a_faire"] == 1
    index = json.loads((d / "sortie.json").read_text(encoding="utf-8"))
    assert verifier(d / "sortie.json") == res["sortie_sha256"] and len(index["tranches"]) == 2
    assert (d / "lignes" / f"{X.nom_tranche(liste[0][0], 0)}-journal.npz").is_file()
    with pytest.raises(GardeArret, match="déjà scellée"):
        X.executer(racine=RACINE_ESSAI, dossier=d, run_id="essai", manifeste_sha="m", processus=1, reductions=(),
                   debut=time.time(), journal={}, liste=liste)
    with pytest.raises(GardeArret, match="incomplètes"):
        X.charger_sortie(d)                                  # 1 répétition au lieu de 1 000 : lecture refusée
    d2 = tmp_path / "run2"
    X.consigner_arret(d2, RuntimeError("panne simulée"), "essai", "m", {})
    with pytest.raises(GardeArret, match="reprise interdite"):
        X.executer(racine=RACINE_ESSAI, dossier=d2, run_id="essai", manifeste_sha="m", processus=1, reductions=(),
                   debut=time.time(), journal={}, liste=liste)


def test_tranche_alteree_refusee_a_la_reprise(tmp_path):
    d = tmp_path / "run"
    X._tache((RACINE_ESSAI, B.INDICE["H7"], 0, 1, (), str(d), "essai", "m", time.time()))
    p = d / "lignes" / f"{X.nom_tranche(B.INDICE['H7'], 0)}.json"
    p.write_text(p.read_text(encoding="utf-8").replace('"r0":0', '"r0":0 '), encoding="utf-8")
    with pytest.raises(GardeArret):
        X.tranches_deja_ecrites(d)


def test_duree_depassee_dans_une_tache():
    with pytest.raises(GardeArret, match="48 h"):
        X._tache((RACINE_ESSAI, B.INDICE["H7"], 0, 1, (), "/nonexistent", "essai", "m", time.time() - 49 * 3600))


def test_processus_au_plus_trois():
    with pytest.raises(GardeArret, match="trois au plus"):
        list(X._carte(4, lambda x: x, [1], X.GardeDuree(time.time())))


def test_lanceur_refuse_sans_addendum_et_miniature_hors_du_depot(tmp_path):
    r = subprocess.run([sys.executable, "-I", "-B", "scripts/jouer_idee_1_1_v3.py", "--miniature", "--sortie",
                        str(RACINE_DEPOT / "jetable")], cwd=RACINE_DEPOT, env=_env(), capture_output=True, text=True)
    assert r.returncode == 1 and "hors du dépôt" in r.stderr
    r = subprocess.run([sys.executable, "-I", "-B", "scripts/jouer_idee_1_1_v3.py", "--miniature", "--sortie", str(tmp_path / "m"),
                        "--lignes", str(B.INDICE["H7"]), "--repetitions", "1"], cwd=RACINE_DEPOT, env=_env(),
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-2000:]
    assert json.loads(r.stdout)["tranches"] == 1
    r = subprocess.run([sys.executable, "-I", "-B", "scripts/lire_idee_1_1_v3.py", str(tmp_path / "rien")], cwd=RACINE_DEPOT,
                       env=_env(), capture_output=True, text=True)
    assert r.returncode != 0


def test_banc_de_mutations_toutes_tuees_cas_sains_passes():
    V = VV.charger()
    r = MU.jouer_banc(V, RACINE_ESSAI, n_certificat=2)
    assert len(r["mutations"]) == 17
    survivantes = [m["mutation"] for m in r["mutations"] if not m["tuee"]]
    sains = [m["mutation"] for m in r["mutations"] if not m["cas_sain_passe"]]
    assert not survivantes and not sains, (survivantes, sains)


def test_verdict_de_la_garde_p4_criteres_ecrits():
    h7 = {"sans_garde_terme": 20, "gel_terme": 2}
    hn = {"gel_terme": 2, "gel_lineaire": 2}
    assert not MU.verdict_garde(h7, hn)["bloque_le_jeu"]
    assert MU.verdict_garde({**h7, "sans_garde_terme": 19}, hn)["bloque_le_jeu"]
    assert MU.verdict_garde({**h7, "gel_terme": 3}, hn)["bloque_le_jeu"]
    assert MU.verdict_garde(h7, {**hn, "gel_lineaire": 3})["bloque_le_jeu"]
