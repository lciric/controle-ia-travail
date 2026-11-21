"""Essais de l'enchaînement et des lanceurs de l'idée 1.2 : gardes de la liste d'arrêt (cas sain et artefact), sortie
scellée, oracle scellé avant le rejeu, arrêt consigné, refus du lanceur (préenregistrement, arbre, sortie, addendum)."""
import importlib.util
import json
import shutil
import socket
import subprocess
from pathlib import Path
from unittest import mock

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller, verifier
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import execution_v1 as X
from controle_ia.organisme_idees_juge import mutations_v1 as MU
from controle_ia.organisme_idees_juge import rejeu_v1 as R

DEPOT = Path(__file__).resolve().parents[1]


def _lanceur(nom="jouer_idee_1_2_v1"):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / "scripts" / f"{nom}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_fichiers_geles_presents():
    for f in X.FICHIERS_GELES:
        assert (DEPOT / f).is_file(), f


def test_garde_de_duree():
    t = [0.0]
    g = X.GardeDuree(limite_s=10, horloge=lambda: t[0])
    t[0] = 9.0
    g.verifier("sain")
    t[0] = 11.0
    with pytest.raises(GardeArret, match="durée murale"):
        g.verifier("artefact")


def test_garde_reseau():
    anciens = X.installer_garde_reseau()
    try:
        with pytest.raises(GardeArret, match="réseau"):
            socket.create_connection(("192.0.2.1", 9))
        with pytest.raises(GardeArret, match="réseau"):
            socket.socket().connect(("192.0.2.1", 9))
    finally:
        X.retirer_garde_reseau(anciens)
    assert socket.create_connection is anciens["create_connection"]


def test_ecriture_scellee_sans_ecrasement(tmp_path):
    c, h = X.ecrire_scelle(tmp_path, "x", {"a": 1}, "r", "m" * 64)
    assert verifier(c) == h
    with pytest.raises(GardeArret, match="R12"):
        X.ecrire_scelle(tmp_path, "x", {"a": 2}, "r", "m" * 64)


def test_addendum_sain_et_artefacts(tmp_path):
    (tmp_path / "a").mkdir()
    for n in ("a/f1.py", "a/f2.py"):
        (tmp_path / n).write_text(n, encoding="utf-8")
    fichiers = ("a/f1.py", "a/f2.py")
    add = tmp_path / "addendum.md"
    add.write_text("# addendum\n\n```\n" + X.lister_empreintes(tmp_path, fichiers) + "```\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        X.verifier_addendum(tmp_path, add, fichiers)          # non scellé
    sceller(add)
    assert set(X.verifier_addendum(tmp_path, add, fichiers)) == set(fichiers)
    with pytest.raises(GardeArret, match="absents"):
        X.verifier_addendum(tmp_path, add, fichiers + ("a/f3.py",))
    (tmp_path / "a/f2.py").write_text("modifié", encoding="utf-8")
    with pytest.raises(GardeArret, match="diffère de l'addendum"):
        X.verifier_addendum(tmp_path, add, fichiers)


def test_enchainement_miniature_oracle_scelle_avant_le_rejeu(tmp_path):
    d = tmp_path / "diag" / "run"
    res = X.executer(racine=MU.RACINE_ESSAI, generations={"T": [2], "N": [251]}, dossier_sortie=d,
                     run_id="20261115-000000-essai", manifeste_sha="m" * 64, processus=1, cartes_E1=(),
                     controles={"essai": True})
    for nom in ("controles-avant-jeu", "oracle", "jeu", "journal"):
        verifier(d / f"{nom}.json")
    journal = json.loads((d / "journal.json").read_text())["resultat"]
    phases = [p["phase"] for p in journal["phases"]]
    assert phases == ["E1", "oracle", "jeu", "sortie"]
    jeu = json.loads((d / "jeu.json").read_text())["resultat"]
    assert all(g["oracle_scelle_sha256"] == res["oracle"] for g in jeu["generations"])
    assert set(jeu["generations"][0]["bras"]) in (set(R.BRAS_T), set(R.BRAS_N))


def test_oracle_altere_avant_le_rejeu_run_invalide(tmp_path):
    d = tmp_path / "diag" / "run"
    vrai = X._tache_jeu

    def alterer_puis_jouer(args):
        (d / "oracle.json").write_text("{}", encoding="utf-8")
        return vrai(args)
    with mock.patch.object(X, "_tache_jeu", alterer_puis_jouer):
        with pytest.raises(GardeArret):
            X.executer(racine=MU.RACINE_ESSAI, generations={"T": [2], "N": []}, dossier_sortie=d, run_id="r",
                       manifeste_sha="m" * 64, processus=1, cartes_E1=())
    assert not (d / "jeu.json").exists()


def test_arret_consigne_sans_lecture_partielle(tmp_path):
    d = tmp_path / "diag" / "run"
    journal = {}
    with mock.patch.object(R, "rejouer_generation", side_effect=GardeArret("log W non fini : arrêt du run")):
        with pytest.raises(GardeArret) as e:
            X.executer(racine=MU.RACINE_ESSAI, generations={"T": [2], "N": []}, dossier_sortie=d, run_id="r",
                       manifeste_sha="m" * 64, processus=1, cartes_E1=(), journal=journal)
    c = X.consigner_arret(d, e.value, "r", "m" * 64, journal)
    verifier(c)
    assert "log W non fini" in json.loads(c.read_text())["resultat"]["motif"]
    assert not (d / "jeu.json").exists()


def test_E1_en_echec_arrete_avant_l_oracle(tmp_path):
    d = tmp_path / "diag" / "run"
    faux = lambda J, gen, i, **k: {"generation": gen.nom, "carte": i, "sorte": gen.cartes[i].sorte, "instants": 32,
                                    "echecs": [{"t": 25}], "trajectoire": []}
    with mock.patch.object(B, "essai_E1_carte", faux):
        with pytest.raises(GardeArret, match="E1"):
            X.executer(racine=MU.RACINE_ESSAI, generations={"T": [0], "N": []}, dossier_sortie=d, run_id="r",
                       manifeste_sha="m" * 64, processus=1, cartes_E1=(("T", 0, 0),))
    assert (d / "controles-avant-jeu.json").exists() and not (d / "oracle.json").exists()


def test_processus_au_plus_deux():
    with pytest.raises(GardeArret, match="deux au plus"):
        list(X._carte(3, lambda t: t, [1]))


def test_generations_miniature_et_du_texte():
    g = X.generations_miniature(5, 5)
    assert g == {"T": [0, 1, 2, 3, 4], "N": [0, 1, 2, 250, 251]}
    t = X.generations_du_texte()
    assert len(t["N"]) == 500 and len(t["T"]) == 750


# --- lanceur -------------------------------------------------------------------------------------------------------------
def _depot_avec_prereg(depot, alterer=False):
    p = depot / B.CHEMIN_PREREG
    p.parent.mkdir(parents=True)
    shutil.copyfile(DEPOT / B.CHEMIN_PREREG, p)
    shutil.copyfile(DEPOT / (B.CHEMIN_PREREG + ".sha256"), str(p) + ".sha256")
    if alterer:
        with open(p, "a", encoding="utf-8") as f:
            f.write("\nligne ajoutée\n")
    from conftest import committer
    committer(depot)
    return depot


def _args(**k):
    import argparse
    base = {"addendum": None, "processus": 2, "miniature": False, "sortie": None}
    base.update(k)
    return argparse.Namespace(**base)


def test_lanceur_refuse_un_preenregistrement_non_scelle(depot):
    L = _lanceur()
    _depot_avec_prereg(depot, alterer=True)
    with mock.patch.object(L, "RACINE_DEPOT", depot), mock.patch.object(L, "abaisser_priorite", lambda: None):
        with pytest.raises(GardeArret):
            L.jeu_decisif(_args())
    assert L.exiger_prereg(DEPOT) == B.EMPREINTE_PREREG           # sain : le texte du dépôt est scellé et intact


def test_lanceur_refuse_un_arbre_sale(depot):
    L = _lanceur()
    _depot_avec_prereg(depot)
    (depot / "brouillon.txt").write_text("x", encoding="utf-8")
    with mock.patch.object(L, "RACINE_DEPOT", depot), mock.patch.object(L, "abaisser_priorite", lambda: None):
        with pytest.raises(GardeArret, match="non propre"):
            L.jeu_decisif(_args())


def test_lanceur_refuse_une_sortie_existante_puis_sans_addendum(depot):
    L = _lanceur()
    _depot_avec_prereg(depot)
    with mock.patch.object(L, "RACINE_DEPOT", depot), mock.patch.object(L, "abaisser_priorite", lambda: None):
        with pytest.raises(GardeArret, match="addendum"):
            L.jeu_decisif(_args())                                  # sain jusqu'à l'addendum : refus faute d'addendum
        ancien = depot / X.DOSSIER_DIAG / ("20261101-000000-" + X.NOM_RUN)
        ancien.mkdir(parents=True)
        (ancien / ".gitkeep").write_text("", encoding="utf-8")
        from conftest import committer
        committer(depot)
        with pytest.raises(GardeArret, match="existe déjà"):
            L.jeu_decisif(_args())


def test_miniature_refuse_une_sortie_dans_le_depot_et_la_racine_du_texte(tmp_path):
    L = _lanceur()
    with mock.patch.object(L, "abaisser_priorite", lambda: None):
        with pytest.raises(GardeArret, match="hors du dépôt"):
            L.repetition_miniature(_args(miniature=True, sortie=str(DEPOT / "tmp-mini"), racine_essai=None))
        with pytest.raises(GardeArret, match="racine du texte"):
            L.repetition_miniature(_args(miniature=True, sortie=str(tmp_path / "m"), racine_essai=B.racine_de(B.EMPREINTE_PREREG)))


def test_lecteur_refuse_un_manifeste_non_decisif(tmp_path):
    L = _lanceur("lire_idee_1_2_v1")
    from controle_ia.manifeste import config_canonique
    import hashlib
    m = {"run_id": "r", "config": {"racine_graines": "1"}, "preenregistrement": None, "decisif": False}
    m["config_sha256"] = hashlib.sha256(config_canonique(m["config"])).hexdigest()
    p = tmp_path / "manifeste.json"
    p.write_text(json.dumps(m), encoding="utf-8")
    sceller(p)
    with mock.patch.object(L, "RACINE_DEPOT", tmp_path):
        with pytest.raises(GardeArret, match="non décisif"):
            L.main(["--manifeste", "manifeste.json"])


def test_lancer_essais_refuse_un_essai_qui_echoue():
    """Cas sain : la suite passe par `lancer_essais` au jeu décisif (rapport du développeur) ; artefact : code ≠ 0 refusé."""
    L = _lanceur()
    faux = subprocess.CompletedProcess(args=[], returncode=1, stdout="1 failed", stderr="")
    with mock.patch.object(L.subprocess, "run", return_value=faux):
        with pytest.raises(GardeArret, match="un essai échoue"):
            L.lancer_essais(DEPOT)
    vrai = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")
    with mock.patch.object(L.subprocess, "run", return_value=vrai) as m:
        assert L.lancer_essais(DEPOT)["code"] == 0
        commande = m.call_args.args[0]
        assert commande[1:6] == ["-B", "-m", "pytest", "-q", "-p"] and set(L.ESSAIS) <= set(commande)
