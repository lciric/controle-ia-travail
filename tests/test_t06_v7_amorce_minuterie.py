"""Amorce v7 de T0.6 (R-1689, défaut trouvé par E2) : au démarrage d'une instance dont l'heure de dépense épuisée est déjà passée, la minuterie relancée ne doit pas
prendre la branche C08 (`PUT stopped`) puisque l'amorce demande la destruction ; l'arrêt gagnait, l'instance restait « exited », non détruite.
Essais : (1) le scénario d'E2 rejoué en vrai (amorce hors essai local, `curl` factice qui journalise les méthodes) : sur l'amorce v6 le `PUT stopped` part (défaut
reproduit) ; sur la v7 seul le `DELETE` part ; (2) la minuterie seule : un ordre de destruction qui arrive PENDANT la consignation de C08 supprime le `PUT stopped`
(deuxième geste) ; cas sain : sans ordre de destruction, C08 envoie toujours `PUT stopped` puis la minuterie détruit à l'échéance."""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

import pytest

import test_t06_v6_amorce as t6a
from test_t06_v6_amorce import CURL_FACTICE, ENV_DE_BASE, _distant, _lancer_amorce, bac  # noqa: F401

RACINE = Path(__file__).resolve().parents[1]
AMORCE6 = RACINE / "scripts" / "amorce_instance_t06_v6.sh"
AMORCE7 = RACINE / "scripts" / "amorce_instance_t06_v7.sh"


@pytest.fixture(params=["v6", "v7"])
def amorce(request, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE6 if request.param == "v6" else AMORCE7)
    return request.param


def _curl(tmp_path) -> dict:
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "bin" / "curl").write_text(CURL_FACTICE, encoding="utf-8")
    (tmp_path / "bin" / "curl").chmod(0o755)
    return {"PATH": f"{tmp_path / 'bin'}:{os.environ['PATH']}", "CONTAINER_ID": "424242", "CONTAINER_API_KEY": "cle-factice",
            "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1", "FAUX_CURL_JOURNAL": str(tmp_path / "curl.txt")}


def test_demarrage_apres_la_depense_epuisee_la_destruction_gagne_sur_l_arret(bac, amorce, tmp_path):
    """Scénario d'E2 : premier run complet (essai local), puis redémarrage HORS essai local alors que l'heure de dépense épuisée est passée et que le marqueur manque.
    v6 : la minuterie envoie `PUT stopped` (défaut) ; v7 : seul le `DELETE` part."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    assert not (racine / "t06-depense-epuisee").exists() and (racine / "t06-fin-normale").exists()
    (racine / "t06-depense-epuisee-utc.txt").write_text(str(int(time.time()) - 30), encoding="utf-8")            # DEP passée
    (racine / "amorce-depot" / "diag" / "apres").mkdir()
    (racine / "amorce-depot" / "diag" / "apres" / "note.json").write_text("{}", encoding="utf-8")                  # un commit en attente à pousser
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, env_sup={"AMORCE_ESSAI_LOCAL": "0", **_curl(tmp_path)})
    methodes = (tmp_path / "curl.txt").read_text(encoding="utf-8").split()
    j = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
    if amorce == "v6":
        assert "PUT" in methodes, (methodes, j)                       # le défaut d'E2 est reproduit par cet essai
        return
    assert code2 == 0, (sortie2[-1500:], j)
    assert methodes == ["DELETE"], (methodes, j)
    assert "instance 424242 détruite" in j and "PUT stopped (" not in j and "DÉPENSE ÉPUISÉE (C08" not in j
    assert "dépense déjà épuisée au démarrage" in (racine / "t06-depense-epuisee").read_text(encoding="utf-8")
    assert "second démarrage après la dépense épuisée" in sortie2 and "poussée des commits en attente d'abord" in sortie2


def test_minuterie_ordre_de_destruction_pendant_la_consignation_supprime_le_put_stopped(bac, amorce, tmp_path):
    """Minuterie seule : à l'heure de dépense épuisée elle consigne ; si l'amorce pose `t06-detruire` pendant la consignation, le `PUT stopped` n'est pas envoyé
    (v6 : il part). Cas sain : sans ordre de destruction, `PUT stopped` puis `DELETE` à l'échéance."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(HOME=str(tmp_path), **_curl(tmp_path))
    for cas in ("ordre", "sain"):
        (tmp_path / "curl.txt").unlink(missing_ok=True)
        for f in ("t06-detruire", "t06-depense-epuisee", "t06-minuterie.log"):
            (racine / f).unlink(missing_ok=True)
        corps = f'#!/usr/bin/env bash\necho "consignation factice"\n' + (f'echo "ordre de l amorce" > "{racine}/t06-detruire"\n' if cas == "ordre" else "")
        (racine / "t06-consigner.sh").write_text(corps, encoding="utf-8")
        now = int(time.time())
        r = subprocess.run(["bash", str(racine / "t06-minuterie.sh"), str(now + 5), str(now - 5), str(racine), "https://api.invalid/v0"],
                           env=env, capture_output=True, text=True, timeout=120)
        j = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
        methodes = (tmp_path / "curl.txt").read_text(encoding="utf-8").split()
        assert r.returncode == 0 and "instance 424242 détruite" in j, (cas, j)
        if cas == "sain":
            assert methodes == ["PUT", "DELETE"] and "PUT stopped (dépense épuisée) : HTTP 200" in j      # C08 inchangée
        elif amorce == "v6":
            assert "PUT" in methodes                                                                          # défaut reproduit
        else:
            assert methodes == ["DELETE"] and "PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" in j
