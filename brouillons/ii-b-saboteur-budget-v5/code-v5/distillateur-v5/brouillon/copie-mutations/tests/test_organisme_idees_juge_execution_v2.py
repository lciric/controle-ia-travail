"""Essais de l'enchaînement v2 et du lanceur v2 : attente bornée (fils mort, garde des 24 h relue), constantes du texte,
oracle v2, refus du lanceur pour la bonne raison (préenregistrement absent, compagnon absent, modifié puis rescellé),
ordre des gardes, manifeste antérieur sous `runs/`, champ `graines`, signal TERM."""
import importlib.util
import json
import math
import os
import shutil
import signal
import time
from pathlib import Path
from unittest import mock

import pytest

from controle_ia.gardes import GardeArret, lever_sur_term
from controle_ia.manifeste import creer_manifeste, lire_manifeste
from controle_ia.scellement import sceller, verifier
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import execution_v2 as X2
from controle_ia.organisme_idees_juge import mutations_v1 as MU1
from controle_ia.organisme_idees_juge import rejeu_v1 as R

DEPOT = Path(__file__).resolve().parents[1]


def _lanceur():
    spec = importlib.util.spec_from_file_location("jouer_idee_1_2_v2", DEPOT / "scripts" / "jouer_idee_1_2_v2.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --- attente bornée -----------------------------------------------------------------------------------------------------
def _saine(t):
    time.sleep(0.1)
    return t


def _fils_mort(t):
    if t == 3:
        os._exit(137)          # mort brutale d'un fils, comme un arrêt par le système
    time.sleep(0.1)
    return t


def _lente(t):
    time.sleep(20)
    return t


def test_attente_bornee_cas_sain():
    g = X2.GardeDuree(limite_s=60, horloge=time.time)
    assert list(X2._carte(2, _saine, range(8), g, pas=0.3)) == list(range(8))


def test_attente_bornee_fils_mort():
    t0 = time.time()
    with pytest.raises(GardeArret, match="processus fils est mort"):
        list(X2._carte(2, _fils_mort, range(8), X2.GardeDuree(limite_s=600, horloge=time.time), pas=0.3))
    assert time.time() - t0 < 30


def test_attente_bornee_garde_des_24_h_relue():
    t0 = time.time()
    with pytest.raises(GardeArret, match="durée murale"):
        list(X2._carte(2, _lente, range(4), X2.GardeDuree(limite_s=1.5, horloge=time.time), pas=0.3))
    assert time.time() - t0 < 15
    with pytest.raises(GardeArret, match="durée murale"):
        list(X2._carte(1, _saine, range(3), X2.GardeDuree(limite_s=-1, horloge=time.time)))
    with pytest.raises(GardeArret, match="deux au plus"):
        list(X2._carte(3, _saine, range(3), X2.GardeDuree(horloge=time.time)))


def _oracle_factice(args):
    racine, famille, g, _ = args
    return {"famille": famille, "g": g, "cartes": [], "membres_a_la_borne_triviale": [], "duree_s": 0.0}


def _jeu_qui_meurt(args):
    if args[2] == 3:
        os._exit(137)
    time.sleep(0.1)
    return {"duree_s": 0.0}


def test_arret_consigne_sur_fils_mort(tmp_path):
    d = tmp_path / "diag" / "run"
    journal = {}
    with mock.patch.object(X2, "_tache_oracle", _oracle_factice), mock.patch.object(X2, "_tache_jeu", _jeu_qui_meurt):
        with pytest.raises(GardeArret, match="processus fils est mort") as e:
            X2.executer(racine=MU1.RACINE_ESSAI, generations={"T": [0, 1, 2, 3, 4, 5], "N": []}, dossier_sortie=d,
                        run_id="r", manifeste_sha="m" * 64, processus=2, cartes_E1=(), journal=journal, pas=0.3)
    c = X2.consigner_arret(d, e.value, "r", "m" * 64, journal)
    verifier(c)
    assert "processus fils est mort" in json.loads(c.read_text())["resultat"]["motif"]
    assert (d / "oracle.json").exists() and not (d / "jeu.json").exists()


# --- enchaînement v2 ------------------------------------------------------------------------------------------------------
def test_fichiers_geles_v2():
    for f in X2.FICHIERS_GELES:
        assert (DEPOT / f).is_file(), f
    assert len(set(X2.FICHIERS_GELES)) == len(X2.FICHIERS_GELES)
    for f in ("src/controle_ia/gardes.py", "src/controle_ia/manifeste.py", "tests/conftest.py",
              "tests/test_organisme_idees_juge_execution_v1.py", "tests/test_organisme_idees_juge_execution_v2.py"):
        assert f in X2.FICHIERS_GELES
    assert all(f.startswith("tests/test_") for f in X2.ESSAIS) and len(X2.ESSAIS) == 10


def test_executer_v2_oracle_v2_et_troisieme_ecriture(tmp_path):
    d = tmp_path / "diag" / "run"
    vu = []
    vrai = X2.VT.verifier_generation

    def espion(r, racine):
        vu.append((r["famille"], r["g"]))
        return vrai(r, racine)
    with mock.patch.object(X2.VT, "verifier_generation", espion):
        res = X2.executer(racine=MU1.RACINE_ESSAI, generations={"T": [6], "N": []}, dossier_sortie=d, run_id="r",
                          manifeste_sha="m" * 64, processus=1, cartes_E1=())
    assert vu == [("T", 6)]
    for nom in ("controles-avant-jeu", "oracle", "jeu", "journal"):
        verifier(d / f"{nom}.json")
    o = json.loads((d / "oracle.json").read_text())["resultat"]["generations"]
    assert "membres_a_la_borne_triviale" in o[0]
    j = json.loads((d / "journal.json").read_text())["resultat"]
    assert j["version_execution"] == 2 and [p["phase"] for p in j["phases"]] == ["E1", "oracle", "jeu", "sortie"]
    assert res["jeu"] == verifier(d / "jeu.json")


def test_executer_v2_refuse_une_constante_alteree(tmp_path):
    d = tmp_path / "diag" / "run"
    with mock.patch.object(R, "SEUIL_BAS", math.log(1 / 10)):
        with pytest.raises(GardeArret, match="constante"):
            X2.executer(racine=MU1.RACINE_ESSAI, generations={"T": [0], "N": []}, dossier_sortie=d, run_id="r",
                        manifeste_sha="m" * 64, processus=1, cartes_E1=())
    assert not d.exists()


# --- lanceur v2 -------------------------------------------------------------------------------------------------------------
def _depot_avec_prereg(depot, cas="sain"):
    p = depot / B.CHEMIN_PREREG
    p.parent.mkdir(parents=True)
    shutil.copyfile(DEPOT / B.CHEMIN_PREREG, p)
    shutil.copyfile(DEPOT / (B.CHEMIN_PREREG + ".sha256"), str(p) + ".sha256")
    if cas == "absent":
        p.unlink(); Path(str(p) + ".sha256").unlink()
    elif cas == "compagnon absent":
        Path(str(p) + ".sha256").unlink()
    elif cas == "modifié puis rescellé":
        p.write_text(p.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        Path(str(p) + ".sha256").unlink()
        sceller(p)
    elif cas == "modifié":
        with open(p, "a", encoding="utf-8") as f:
            f.write("\nligne ajoutée\n")
    (depot / "garde.txt").write_text("x", encoding="utf-8")
    from conftest import committer
    committer(depot)
    return depot


def _args(**k):
    import argparse
    base = {"addendum": None, "processus": 2, "miniature": False, "sortie": None}
    base.update(k)
    return argparse.Namespace(**base)


MOTIFS_PREREG = {"absent": "fichier absent", "compagnon absent": "compagnon", "modifié puis rescellé": "texte scellé attendu",
                 "modifié": "organisme-idee-1-2-tirages-repartis"}


def test_exiger_prereg_cas_sain_et_trois_artefacts(tmp_path):
    L = _lanceur()
    assert L.exiger_prereg(DEPOT) == B.EMPREINTE_PREREG
    import inspect
    assert inspect.signature(L.exiger_prereg).parameters["racine_depot"].default is inspect.Parameter.empty
    for cas, motif in MOTIFS_PREREG.items():
        d = tmp_path / cas.replace(" ", "-")
        d.mkdir()
        import subprocess
        subprocess.run(["git", "-C", str(d), "init", "-q", "-b", "main"], check=True)
        subprocess.run(["git", "-C", str(d), "config", "user.email", "t@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(d), "config", "user.name", "t"], check=True)
        _depot_avec_prereg(d, cas)
        with pytest.raises(GardeArret, match=motif):
            L.exiger_prereg(d)


@pytest.mark.parametrize("cas", list(MOTIFS_PREREG))
def test_jeu_decisif_refuse_le_preenregistrement_pour_la_bonne_raison(depot, cas):
    """Garde vérifiée la première : arbre propre, aucune sortie, pas d'addendum — c'est le préenregistrement qui refuse."""
    L = _lanceur()
    _depot_avec_prereg(depot, cas)
    with mock.patch.object(L, "RACINE_DEPOT", depot), mock.patch.object(L, "abaisser_priorite", lambda: None), \
            mock.patch.object(L, "installer_signaux", lambda: None):
        with pytest.raises(GardeArret, match=MOTIFS_PREREG[cas]):
            L.jeu_decisif(_args())


def test_ordre_des_gardes_puis_sorties_et_manifestes_anterieurs(depot):
    L = _lanceur()
    _depot_avec_prereg(depot)
    from conftest import committer
    with mock.patch.object(L, "RACINE_DEPOT", depot), mock.patch.object(L, "abaisser_priorite", lambda: None), \
            mock.patch.object(L, "installer_signaux", lambda: None):
        with pytest.raises(GardeArret, match="addendum d'empreintes scellé exigé"):
            L.jeu_decisif(_args())                       # sain jusqu'à l'addendum
        (depot / "brouillon.txt").write_text("x", encoding="utf-8")
        with pytest.raises(GardeArret, match="non propre"):
            L.jeu_decisif(_args())
        (depot / "brouillon.txt").unlink()
        ancien = depot / "runs" / ("20261101-000000-" + X2.NOM_RUN)
        ancien.mkdir(parents=True)
        (ancien / "manifeste.json").write_text("{}", encoding="utf-8")
        committer(depot)
        with pytest.raises(GardeArret, match="un manifeste de ce jeu existe déjà"):
            L.jeu_decisif(_args())
        shutil.rmtree(depot / "runs")
        diag = depot / X2.DOSSIER_DIAG / ("20261101-000000-" + X2.NOM_RUN)
        diag.mkdir(parents=True)
        (diag / "arret.json").write_text("{}", encoding="utf-8")
        committer(depot)
        with pytest.raises(GardeArret, match="une sortie de ce jeu existe déjà"):
            L.jeu_decisif(_args())


def test_champ_graines_et_etats_de_controle(depot):
    L = _lanceur()
    racine = B.racine_de(B.EMPREINTE_PREREG)
    config = L.config_du_jeu(racine, {"N": [0], "T": [0]}, {}, None, {}, 2, False)
    chemin, _ = creer_manifeste(depot, "20261115-000000-essai-graines", config, ["racine-du-texte"], entropie=racine)
    m, _ = lire_manifeste(chemin)
    assert m["graines"]["racine-du-texte"]["entropie"] == str(racine)
    assert m["config"]["etats_de_controle"]["(0, 0, 0, 2)"] == B.etat_graine(racine, 0, 0, 0, 2)
    lecteur_spec = importlib.util.spec_from_file_location("lire_idee_1_2_v2", DEPOT / "scripts" / "lire_idee_1_2_v2.py")
    lecteur = importlib.util.module_from_spec(lecteur_spec)
    lecteur_spec.loader.exec_module(lecteur)
    lecteur.exiger_etats_de_controle(m["config"], racine)                       # sain
    with pytest.raises(GardeArret, match="état de contrôle"):
        lecteur.exiger_etats_de_controle(m["config"], racine + 1)               # artefact


def test_signal_term_consigne():
    L = _lanceur()
    ancien = L.installer_signaux()
    try:
        assert signal.getsignal(signal.SIGTERM) is lever_sur_term
        with pytest.raises(GardeArret, match="signal TERM"):
            os.kill(os.getpid(), signal.SIGTERM)
            time.sleep(1)
    finally:
        signal.signal(signal.SIGTERM, ancien)


def test_miniature_v2_refus(tmp_path):
    L = _lanceur()
    with mock.patch.object(L, "abaisser_priorite", lambda: None), mock.patch.object(L, "installer_signaux", lambda: None):
        with pytest.raises(GardeArret, match="hors du dépôt"):
            L.repetition_miniature(_args(miniature=True, sortie=str(DEPOT / "tmp-mini"), racine_essai=None))
        with pytest.raises(GardeArret, match="racine du texte"):
            L.repetition_miniature(_args(miniature=True, sortie=str(tmp_path / "m"), racine_essai=B.racine_de(B.EMPREINTE_PREREG)))


def test_lancer_essais_v2_couvre_les_dix_fichiers():
    L = _lanceur()
    import subprocess
    vrai = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")
    with mock.patch.object(L.subprocess, "run", return_value=vrai) as m:
        L.lancer_essais(DEPOT)
        assert set(X2.ESSAIS) <= set(m.call_args.args[0])
    with mock.patch.object(L.subprocess, "run", return_value=subprocess.CompletedProcess(args=[], returncode=1, stdout="", stderr="")):
        with pytest.raises(GardeArret, match="un essai échoue"):
            L.lancer_essais(DEPOT)
