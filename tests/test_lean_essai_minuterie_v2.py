"""Essais R5 de la minuterie v2 et du client Hetzner v2 (CLL-05, CLL-06, CLL-13, CLL-14) : faux transport, aucun appel
réseau, aucun serveur créé."""
import http.client
import json
import socket
from datetime import date, datetime, timedelta, timezone

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v2 as H
from controle_ia.lean_essai import minuterie_v2 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)
JOUR = date(2026, 11, 11)
TYPES = [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2260", "net": "0.19"}}]},
         {"name": "ccx63", "prices": [{"location": "hel1", "price_hourly": {"gross": "1.3942", "net": "1.17"}}]}]
PRICING = {"pricing": {"currency": "EUR", "primary_ips": [
    {"type": "ipv4", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.0010", "net": "0.0008"}}]}]}}


class FauxAPI:
    def __init__(self, serveurs=None, echecs_delete=0, created=True):
        self.serveurs = dict(serveurs or {})
        self.echecs_delete = echecs_delete
        self.created = created
        self.appels, self.corps = [], []
        self.pare_feux = {}

    def __call__(self, methode, chemin, corps=None):
        self.appels.append((methode, chemin))
        if methode == "GET" and chemin.startswith("/servers/"):
            i = int(chemin.rsplit("/", 1)[1])
            if i not in self.serveurs:
                return 404, {"error": {"code": "not_found"}}
            return 200, {"server": {"id": i, "name": self.serveurs[i], "created": "2026-11-11T01:00:00+00:00",
                                    "server_type": {"name": "ccx33"}, "datacenter": {"location": {"name": "hel1"}}}}
        if methode == "GET" and chemin.startswith("/servers?"):
            return 200, {"servers": [{"id": i, "name": n} for i, n in self.serveurs.items()], "meta": {"pagination": {}}}
        if methode == "DELETE" and chemin.startswith("/servers/"):
            if self.echecs_delete:
                self.echecs_delete -= 1
                return 503, {"error": {"code": "unavailable", "message": "plus tard"}}
            self.serveurs.pop(int(chemin.rsplit("/", 1)[1]), None)
            return 200, {"action": {}}
        if methode == "POST" and chemin == "/servers":
            self.corps.append(corps)
            s = {"id": 777, "name": corps["name"]}
            if self.created:
                s["created"] = "2026-11-11T01:00:00Z"
            self.serveurs[777] = corps["name"]
            return 201, {"server": s}
        if methode == "GET" and chemin.startswith("/server_types"):
            return 200, {"server_types": TYPES}
        if methode == "GET" and chemin == "/pricing":
            return 200, PRICING
        if methode == "GET" and chemin.startswith("/firewalls/"):
            return 200, {"firewall": self.pare_feux[int(chemin.rsplit("/", 1)[1])]}
        return 500, {"error": {"code": "inattendu"}}


def client(api):
    return H.ClientHetzner2(transport=api, dormir=lambda s: None)


def machine(**k):
    d = dict(identifiant=42, nom=H.NOM_MACHINE, cree_a=T0, prix_horaire_usd=0.30, plafond_usd=65.0, echeance_h=48.0)
    d.update(k)
    return M.Machine(**d)


# ---- CLL-05 : destruction retentée -----------------------------------------------------------------------------------------

def test_destruction_retentee_jusqu_a_l_absence(tmp_path):
    api = FauxAPI({42: H.NOM_MACHINE}, echecs_delete=3)
    pauses = []
    with open(tmp_path / "j.jsonl", "w") as j:
        r = M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, j, dormir=pauses.append)
    assert r["detruit"] and r["essais"] == 4 and 42 not in api.serveurs and pauses == [5.0, 10.0, 20.0]
    lignes = [json.loads(x) for x in (tmp_path / "j.jsonl").read_text().splitlines()]
    assert [x.get("destruction") for x in lignes] == ["échec", "échec", "échec", "confirmée"]


def test_destruction_transport_qui_casse_puis_reprend():
    api = FauxAPI({42: H.NOM_MACHINE})
    cassures = [OSError("connexion fermée"), H.ErreurHetzner("délai")]

    def transport(m, c, b=None):
        if m == "DELETE" and cassures:
            raise cassures.pop(0)
        return api(m, c, b)
    r = M.detruire_par_identifiant(client(transport), 42, H.NOM_MACHINE, dormir=lambda s: None)
    assert r["detruit"] and r["essais"] == 3


def test_destruction_sans_fin_bornee_dans_l_essai_seulement():
    api = FauxAPI({42: H.NOM_MACHINE}, echecs_delete=10 ** 6)
    with pytest.raises(GardeArret, match="non confirmée après 25"):
        M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, dormir=lambda s: None, essais_max=25)
    assert sum(1 for a in api.appels if a[0] == "DELETE") == 25


def test_refus_de_nom_sans_retentative():
    api = FauxAPI({42: "organisme-v66-course"})
    with pytest.raises(GardeArret, match="aucun autre serveur"):
        M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, dormir=lambda s: None)
    assert not any(a[0] == "DELETE" for a in api.appels)


def test_veiller_v2():
    api = FauxAPI({42: H.NOM_MACHINE}, echecs_delete=2)
    horloge = iter([T0 + timedelta(hours=h) for h in (1, 48)])
    r = M.veiller(machine(), client(api), horloge=lambda: next(horloge), dormir=lambda s: None)
    assert r["detruit"] and r["essais"] == 3
    api = FauxAPI({})
    r = M.veiller(machine(), client(api), horloge=lambda: T0 + timedelta(hours=1), dormir=lambda s: None)
    assert r["absent"] and not r["detruit"]


@pytest.mark.parametrize("exc", [socket.timeout("lecture"), ConnectionResetError("rst"),
                                 http.client.RemoteDisconnected("fermé"), http.client.IncompleteRead(b"")])
def test_transport_convertit_sans_jeton(monkeypatch, exc):
    monkeypatch.setenv("HCLOUD_TOKEN", "jeton-factice-0123456789")

    def urlopen(*a, **k):
        raise exc
    monkeypatch.setattr(H.urllib.request, "urlopen", urlopen)
    with pytest.raises(H.ErreurHetzner) as e:
        H.transport_urllib("GET", "/servers")
    assert "jeton-factice" not in str(e.value)


# ---- CLL-06 : création liée au devis et à la minuterie --------------------------------------------------------------------

def fichiers(tmp_path, ligne_depense=""):
    go = tmp_path / "go.md"
    go.write_text("| GO-2026-11-10-13 | 2026-11-10 | calcul | Essai Lean, D-1a ; aucun appel de modèle | 65 USD | 2026-11-30 "
                  "| Lazar | R |\n", encoding="utf-8")
    dep = tmp_path / "depenses.md"
    dep.write_text("| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |\n"
                   "|---|---|---|---|---|---|---|---|---|\n" + ligne_depense, encoding="utf-8")
    return go, dep, tmp_path / "creations.jsonl"


def creer(api, go, dep, journal, **k):
    d = dict(go_id="GO-2026-11-10-13", chemin_go=go, chemin_depenses=dep, journal_creations=journal,
             type_serveur="ccx33", image="ubuntu-24.04", lieu="hel1", cles_ssh=[1], pare_feux=[2], taux_usd_eur=1.25,
             aujourdhui=JOUR, horloge=lambda: T0 + timedelta(minutes=5), dormir=lambda s: None, tours_max=1)
    d.update(k)
    return M.creer_et_veiller(client(api), **d)


def test_creation_saine_prix_lu_dans_l_api(tmp_path):
    go, dep, journal = fichiers(tmp_path)
    api = FauxAPI()
    r = creer(api, go, dep, journal)
    assert r == {"detruit": False, "motif": "garder (cumul 0.28 USD)"}
    e = json.loads(journal.read_text())
    assert e["identifiant"] == 777 and e["created"] == "2026-11-11T01:00:00Z"
    assert e["prix_usd_h"] == pytest.approx((0.2260 + 0.0010) * 1.25) and e["prix_eur_h"]["ipv4"] == 0.001
    assert api.corps[0]["public_net"] == {"enable_ipv4": True, "enable_ipv6": False}   # mutation 7 de CLL-14


def test_creation_refusee_devis_trop_cher(tmp_path):
    go, dep, journal = fichiers(tmp_path)
    api = FauxAPI()
    with pytest.raises(GardeArret, match="reste du plafond"):
        creer(api, go, dep, journal, type_serveur="ccx63")
    assert not api.corps


def test_seconde_machine_refusee_sans_mot_de_lazar(tmp_path):
    go, dep, journal = fichiers(tmp_path)
    creer(FauxAPI(), go, dep, journal)
    with pytest.raises(GardeArret, match="seconde machine"):
        creer(FauxAPI(), go, dep, journal)
    assert creer(FauxAPI(), go, dep, journal, mot_de_lazar="R-9999")["detruit"] is False
    autre = tmp_path / "b"
    autre.mkdir()
    go2, dep2, journal2 = fichiers(autre, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | Hetzner 175573391 | ccx33 | 1 | 0,30 "
                                          "| 0,30 | — |\n")
    with pytest.raises(GardeArret, match="registre : machine 175573391"):
        creer(FauxAPI(), go2, dep2, journal2)


def test_deja_depense_du_go(tmp_path):
    go, dep, journal = fichiers(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | — | — | — | ≈ 1 050,40 | — | — |\n"
                                          "| 2026-11-11 | GO-2026-11-10-11 | autre | — | — | — | 9,00 | — | — |\n")
    assert M.deja_depense_go(dep, "GO-2026-11-10-13")["retenu"] == pytest.approx(1050.40)
    go, dep, journal = fichiers(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | **0,00 USD** ; reste 65 USD |\n")
    with pytest.raises(GardeArret, match="à déclarer"):
        M.deja_depense_go(dep, "GO-2026-11-10-13")
    assert M.deja_depense_go(dep, "GO-2026-11-10-13", declare=0.0)["retenu"] == 0.0
    go, dep, journal = fichiers(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | — | — | — | 30,00 | — | — |\n")
    with pytest.raises(GardeArret, match="inférieur"):
        M.deja_depense_go(dep, "GO-2026-11-10-13", declare=10.0)
    # ccx63 à 0,6 USD l'euro : 0,837 USD/h × 48 = 40,2 ; tient sous 65, pas sous le reste de 35 (30 déjà dépensés)
    M.verifier_devis(1.3952 * 0.6, "D-1a")
    with pytest.raises(GardeArret, match="reste du plafond"):
        creer(FauxAPI(), go, dep, journal, type_serveur="ccx63", taux_usd_eur=0.6)


def test_erreur_apres_creation_detruit_le_serveur(tmp_path):
    go, dep, journal = fichiers(tmp_path)
    api = FauxAPI(created=False)
    with pytest.raises(KeyError):
        creer(api, go, dep, journal)
    assert ("DELETE", "/servers/777") in api.appels and 777 not in api.serveurs


def test_creation_go_errone(tmp_path):
    go, dep, journal = fichiers(tmp_path)
    api = FauxAPI()
    with pytest.raises(GardeArret):
        creer(api, go, dep, journal, go_id="GO-2026-11-10-11")
    with pytest.raises(GardeArret, match="taux"):
        creer(api, go, dep, journal, taux_usd_eur=0)
    assert not api.corps


# ---- CLL-14, mutations 8 et 9 : ligne de commande ------------------------------------------------------------------------

def jamais(secondes):
    raise AssertionError("la minuterie a démarré alors que la commande devait être refusée")


def test_cli_veiller_echeance_et_devis(tmp_path):
    j = str(tmp_path / "j.jsonl")
    with pytest.raises(GardeArret, match="plus longue"):
        M.main(["veiller", "--identifiant", "42", "--taux-usd-eur", "1.25", "--echeance-h", "60", "--journal", j],
               client=client(FauxAPI({42: H.NOM_MACHINE})), dormir=jamais)
    api = FauxAPI({42: H.NOM_MACHINE})
    with pytest.raises(GardeArret, match="reste du plafond"):
        M.main(["veiller", "--identifiant", "42", "--taux-usd-eur", "10", "--journal", j], client=client(api),
               dormir=jamais)
    assert not any(a[0] == "DELETE" for a in api.appels)


def test_cli_detruire(tmp_path, capsys):
    api = FauxAPI({42: H.NOM_MACHINE}, echecs_delete=1)
    pauses = []
    assert M.main(["detruire", "--identifiant", "42", "--journal", str(tmp_path / "j.jsonl")], client=client(api),
                  dormir=pauses.append) == 0
    assert pauses == [5.0]
    assert 42 not in api.serveurs and '"detruit": true' in capsys.readouterr().out


def test_verifier_devis_v2():
    M.verifier_devis(1.30, "D-1a")
    with pytest.raises(GardeArret):
        M.verifier_devis(1.30, "D-1a", 10.0)
    with pytest.raises(GardeArret):
        M.verifier_devis(0, "D-1a")


# ---- CLL-13 : pare-feu du nuage lu par l'API ------------------------------------------------------------------------------

def pare_feu(regles, serveur=777):
    return {"rules": regles, "applied_to": [{"type": "server", "server": {"id": serveur}}]}


def test_coupure_nuage_saine_et_artefacts():
    api = FauxAPI()
    api.pare_feux[2] = pare_feu(H.regles_coupure("203.0.113.5"))
    assert H.verifier_coupure_nuage(client(api), 2, 777)["serveur"] == 777
    api.pare_feux[3] = pare_feu(H.regles_installation("203.0.113.5"))
    api.pare_feux[4] = pare_feu(H.regles_coupure("203.0.113.5") + [{"direction": "out", "protocol": "tcp",
                                                                   "port": "443", "destination_ips": ["0.0.0.0/0"]}])
    api.pare_feux[5] = pare_feu(H.regles_coupure("203.0.113.5"), serveur=1)
    for ident, motif in ((3, "règles sortantes"), (4, "règles sortantes"), (5, "non appliqué")):
        with pytest.raises(GardeArret, match=motif):
            H.verifier_coupure_nuage(client(api), ident, 777)


def test_prix_lu_et_absences():
    assert client(FauxAPI()).prix_horaire_eur("ccx33", "hel1")["total"] == pytest.approx(0.2270)
    with pytest.raises(GardeArret):
        client(FauxAPI()).prix_horaire_eur("ccx33", "fsn1")
    with pytest.raises(GardeArret):
        client(FauxAPI()).prix_horaire_eur("cx99", "hel1")
