"""Essais R5 de la minuterie de destruction (A13, R10) et du client Hetzner — essai Lean, D-1a. Aucun appel réseau : un faux
transport tient lieu d'API ; aucun serveur n'est créé."""
from datetime import date, datetime, timedelta, timezone

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v1 as H
from controle_ia.lean_essai import minuterie_v1 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)


class FauxAPI:
    def __init__(self, serveurs):
        self.serveurs = dict(serveurs)  # id -> nom
        self.appels = []

    def __call__(self, methode, chemin, corps=None):
        self.appels.append((methode, chemin))
        if methode == "GET" and chemin.startswith("/servers/"):
            i = int(chemin.rsplit("/", 1)[1])
            return (200, {"server": {"id": i, "name": self.serveurs[i]}}) if i in self.serveurs else \
                (404, {"error": {"code": "not_found"}})
        if methode == "GET" and chemin.startswith("/servers?"):
            return 200, {"servers": [{"id": i, "name": n} for i, n in self.serveurs.items()], "meta": {"pagination": {}}}
        if methode == "DELETE" and chemin.startswith("/servers/"):
            self.serveurs.pop(int(chemin.rsplit("/", 1)[1]))
            return 200, {"action": {"status": "running"}}
        if methode == "POST" and chemin == "/servers":
            return 201, {"server": {"id": 999, "name": corps["name"]}}
        return 500, {"error": {"code": "inattendu"}}


def machine(**k):
    d = dict(identifiant=42, nom=H.NOM_MACHINE, cree_a=T0, prix_horaire_usd=0.10, plafond_usd=65.0, echeance_h=48.0)
    d.update(k)
    return M.Machine(**d)


def test_devis_de_la_machine():
    M.verifier_devis(1.30, "D-1a")  # 62,40 ≤ 65
    M.verifier_devis(1.30, "D-1b")  # 33,80 ≤ 35
    with pytest.raises(GardeArret):
        M.verifier_devis(1.40, "D-1a")  # 67,20 > 65


def test_decision_sain_et_artefacts():
    m = machine()
    assert M.decider(m, T0 + timedelta(minutes=30)) == (False, "garder (cumul 0.10 USD)")
    assert M.heures_entamees(m, T0 + timedelta(hours=2, seconds=1)) == 3
    assert M.decider(m, T0 + timedelta(hours=48))[0]
    cher = machine(prix_horaire_usd=1.30, echeance_h=60.0, plafond_usd=65.0)
    assert not M.decider(cher, T0 + timedelta(hours=47, minutes=59))[0]   # 48 h entamées : 62,40 < 65 − 1,30
    assert M.decider(cher, T0 + timedelta(hours=48, minutes=1))[0]        # 49 h entamées : 63,70 ≥ 63,70
    with pytest.raises(GardeArret):
        machine(cree_a=datetime(2026, 11, 11, 1, 0))  # sans fuseau


def test_veiller_detruit_par_identifiant():
    api = FauxAPI({42: H.NOM_MACHINE, 7: "organisme-v66-course"})
    client = H.ClientHetzner(transport=api, dormir=lambda s: None)
    horloge = iter([T0 + timedelta(hours=h) for h in (1, 2, 48, 48)])
    res = M.veiller(machine(), client, horloge=lambda: next(horloge), dormir=lambda s: None)
    assert res["detruit"] and 42 not in api.serveurs and 7 in api.serveurs
    assert ("DELETE", "/servers/42") in api.appels and not any(c[1] == "/servers/7" and c[0] == "DELETE" for c in api.appels)


def test_veiller_sain_ne_detruit_rien():
    api = FauxAPI({42: H.NOM_MACHINE})
    client = H.ClientHetzner(transport=api, dormir=lambda s: None)
    res = M.veiller(machine(), client, horloge=lambda: T0 + timedelta(hours=1), dormir=lambda s: None, tours_max=3)
    assert not res["detruit"] and 42 in api.serveurs and not any(c[0] == "DELETE" for c in api.appels)


def test_artefact_autre_serveur_jamais_touche():
    api = FauxAPI({42: "organisme-v66-course"})
    client = H.ClientHetzner(transport=api, dormir=lambda s: None)
    with pytest.raises(GardeArret, match="aucun autre serveur"):
        M.veiller(machine(), client, horloge=lambda: T0 + timedelta(hours=49), dormir=lambda s: None)
    assert 42 in api.serveurs and not any(c[0] == "DELETE" for c in api.appels)


def test_artefact_serveur_qui_ne_disparait_pas():
    class Tenace(FauxAPI):
        def __call__(self, methode, chemin, corps=None):
            if methode == "DELETE":
                self.appels.append((methode, chemin))
                return 200, {}
            return super().__call__(methode, chemin, corps)
    api = Tenace({42: H.NOM_MACHINE})
    client = H.ClientHetzner(transport=api, dormir=lambda s: None)
    with pytest.raises(GardeArret, match="encore présent"):
        M.veiller(machine(), client, horloge=lambda: T0 + timedelta(hours=49), dormir=lambda s: None)


def test_erreur_d_api_remonte():
    client = H.ClientHetzner(transport=lambda m, c, b=None: (401, {"error": {"code": "unauthorized", "message": "x"}}))
    with pytest.raises(H.ErreurHetzner, match="401"):
        client.inventaire()


def test_creation_garde_du_go_et_nom_unique(tmp_path):
    go = tmp_path / "go.md"
    go.write_text("| GO-2026-11-10-13 | 2026-11-10 | calcul | Essai Lean, D-1a ; aucun appel de modèle | 65 USD | 2026-11-30 "
                  "| Lazar | R |\n", encoding="utf-8")
    api = FauxAPI({})
    client = H.ClientHetzner(transport=api)
    with pytest.raises(GardeArret):
        client.creer_serveur("GO-2026-11-10-11", go, date(2026, 11, 11), "cpx42", "ubuntu-24.04", "fsn1", [1], [2])
    assert not any(c[0] == "POST" for c in api.appels)
    assert client.creer_serveur("GO-2026-11-10-13", go, date(2026, 11, 11), "cpx42", "ubuntu-24.04", "fsn1", [1], [2])
    api.serveurs[999] = H.NOM_MACHINE
    with pytest.raises(GardeArret, match="existe déjà"):
        client.creer_serveur("GO-2026-11-10-13", go, date(2026, 11, 11), "cpx42", "ubuntu-24.04", "fsn1", [1], [2])


def test_regles_du_pare_feu():
    r = H.regles_coupure("203.0.113.5")
    sortantes = [x for x in r if x["direction"] == "out"]
    assert sortantes == [{"direction": "out", "protocol": "icmp", "destination_ips": ["192.0.2.1/32"],
                          "description": sortantes[0]["description"]}]
    assert [x["source_ips"] for x in r if x["direction"] == "in"] == [["203.0.113.5/32"]]
    assert not [x for x in H.regles_installation("203.0.113.5") if x["direction"] == "out"]
    with pytest.raises(GardeArret):
        H.regles_installation("0.0.0.0/0")


def test_jeton_absent_jamais_devine(monkeypatch):
    monkeypatch.delenv("HCLOUD_TOKEN", raising=False)
    with pytest.raises(H.ErreurHetzner, match="absent"):
        H.transport_urllib("GET", "/servers")
