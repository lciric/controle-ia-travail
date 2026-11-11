"""Essais R5 de la minuterie v3 et du client Hetzner v3 (CLC2-03, CLC2-04, CLC2-06, CLC2-07, CLC2-08 n12, n15, n17) :
faux transport, aucun appel réseau, aucun serveur créé."""
import json
import urllib.parse
from datetime import date, datetime, timedelta, timezone

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v3 as H
from controle_ia.lean_essai import minuterie_v3 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)
JOUR = date(2026, 11, 11)
TYPES = [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2260"}}]},
         {"name": "ccx63", "prices": [{"location": "hel1", "price_hourly": {"gross": "1.3942"}}]}]


class FauxAPI:
    def __init__(self, serveurs=None, echecs_delete=0, mal_formes=0, fantome=False, perdre_post=False, devise="EUR",
                 ipv6_avant=False, page_suivante=False, pare_feux_serveur=None):
        self.serveurs = {i: {"name": n, "labels": {}} for i, n in (serveurs or {}).items()}
        self.echecs_delete, self.mal_formes, self.fantome, self.perdre_post = echecs_delete, mal_formes, fantome, perdre_post
        self.devise, self.ipv6_avant, self.page_suivante = devise, ipv6_avant, page_suivante
        self.pare_feux_serveur = pare_feux_serveur if pare_feux_serveur is not None else [{"id": 2, "status": "applied"}]
        self.pare_feux = {}
        self.appels, self.corps = [], []
        self.avant_post = None

    def __call__(self, methode, chemin, corps=None):
        self.appels.append((methode, chemin))
        if methode == "GET" and chemin.startswith("/servers/"):
            i = int(chemin.rsplit("/", 1)[1])
            if self.mal_formes:
                self.mal_formes -= 1
                return 200, {"inattendu": True}
            if i not in self.serveurs or self.fantome:
                return 404, {"error": {"code": "not_found"}}
            s = self.serveurs[i]
            return 200, {"server": {"id": i, "name": s["name"], "created": "2026-11-11T01:00:00+00:00",
                                    "server_type": {"name": "ccx33"}, "datacenter": {"location": {"name": "hel1"}},
                                    "public_net": {"firewalls": self.pare_feux_serveur}}}
        if methode == "GET" and chemin.startswith("/servers?label_selector="):
            selecteur = urllib.parse.unquote(chemin.split("=", 1)[1].split("&")[0])
            cle, valeur = selecteur.split("=")
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()
                                     if s["labels"].get(cle) == valeur]}
        if methode == "GET" and chemin.startswith("/servers?"):
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()],
                         "meta": {"pagination": {}}}
        if methode == "DELETE" and chemin.startswith("/servers/"):
            if self.echecs_delete:
                self.echecs_delete -= 1
                return 503, {"error": {"code": "unavailable"}}
            if not self.fantome:
                self.serveurs.pop(int(chemin.rsplit("/", 1)[1]), None)
            return 200, {}
        if methode == "POST" and chemin == "/servers":
            if self.avant_post:
                self.avant_post()
            self.corps.append(corps)
            self.serveurs[777] = {"name": corps["name"], "labels": corps["labels"]}
            if self.perdre_post:
                raise H.ErreurHetzner("échange avec l'API de Hetzner interrompu (TimeoutError)")
            return 201, {"server": {"id": 777, "name": corps["name"], "created": "2026-11-11T01:00:30Z"}}
        if methode == "GET" and chemin.startswith("/server_types"):
            return 200, {"server_types": TYPES, "meta": {"pagination": {"next_page": 2 if self.page_suivante else None}}}
        if methode == "GET" and chemin == "/pricing":
            ips = [{"type": "ipv4", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.0010"}}]}]
            if self.ipv6_avant:
                ips.insert(0, {"type": "ipv6", "prices": [{"location": "hel1", "price_hourly": {"gross": "9.0"}}]})
            return 200, {"pricing": {"currency": self.devise, "primary_ips": ips}}
        if methode == "GET" and chemin.startswith("/firewalls/"):
            return 200, {"firewall": self.pare_feux[int(chemin.rsplit("/", 1)[1])]}
        return 500, {"error": {"code": "inattendu"}}


def client(api):
    return H.ClientHetzner3(transport=api, dormir=lambda s: None)


def machine(**k):
    d = dict(identifiant=42, nom=H.NOM_MACHINE, cree_a=T0, prix_horaire_usd=0.30, plafond_usd=65.0, echeance_h=48.0)
    d.update(k)
    return M.Machine(**d)


def lignes(chemin):
    return [json.loads(x) for x in chemin.read_text().splitlines() if x.strip()]


# ---- CLC2-03 -------------------------------------------------------------------------------------------------------------------

def test_reponse_mal_formee_retentee(tmp_path):
    api = FauxAPI({42: H.NOM_MACHINE}, mal_formes=2)
    with open(tmp_path / "j.jsonl", "w") as j:
        r = M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, j, dormir=lambda s: None)
    assert r["detruit"] and 42 not in api.serveurs
    assert sum(1 for x in lignes(tmp_path / "j.jsonl") if x.get("destruction") == "échec") == 2


def test_corps_non_utf8_converti(monkeypatch):
    monkeypatch.setenv("HCLOUD_TOKEN", "jeton-factice-0123456789")

    class Reponse:
        status = 200

        def read(self):
            return b"\xff\xfe\xfd"

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False
    monkeypatch.setattr(H.urllib.request, "urlopen", lambda *a, **k: Reponse())
    with pytest.raises(H.ErreurHetzner) as e:
        H.transport_urllib("GET", "/servers/1")
    assert "jeton-factice" not in str(e.value)


def test_un_seul_404_ne_suffit_pas():
    api = FauxAPI({42: H.NOM_MACHINE}, fantome=True)   # 404 sur le serveur, mais toujours dans l'inventaire
    assert not client(api).absence_confirmee(42)
    with pytest.raises(GardeArret, match="non confirmée après 3"):
        M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, dormir=lambda s: None, essais_max=3)


def test_refus_de_nom_journalise(tmp_path):
    api = FauxAPI({42: "organisme-v66-course"})
    with open(tmp_path / "j.jsonl", "w") as j, pytest.raises(GardeArret):
        M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, j, dormir=lambda s: None)
    assert lignes(tmp_path / "j.jsonl")[-1]["destruction"] == "refusée"
    assert not any(a[0] == "DELETE" for a in api.appels)


def test_pause_plafonnee_a_300_s():   # CLC2-08 n12
    api = FauxAPI({42: H.NOM_MACHINE}, echecs_delete=8)
    pauses = []
    r = M.detruire_par_identifiant(client(api), 42, H.NOM_MACHINE, dormir=pauses.append)
    assert r["essais"] == 9 and pauses == [5.0, 10.0, 20.0, 40.0, 80.0, 160.0, 300.0, 300.0]


def test_veiller_survit_a_une_lecture_en_echec(tmp_path):   # CLC2-08 n15
    api = FauxAPI({42: H.NOM_MACHINE}, mal_formes=1)
    with open(tmp_path / "j.jsonl", "w") as j:
        r = M.veiller(machine(), client(api), horloge=lambda: T0 + timedelta(hours=1), dormir=lambda s: None, journal=j,
                      tours_max=2)
    assert r == {"detruit": False, "motif": "garder (cumul 0.30 USD)"}
    assert any(x.get("lecture") == "échec" for x in lignes(tmp_path / "j.jsonl"))


# ---- CLC2-04 ------------------------------------------------------------------------------------------------------------------

def fichiers(tmp_path, ligne_depense="", lignes_go=""):
    go = tmp_path / "go.md"
    go.write_text("| GO-2026-11-10-13 | 2026-11-10 | calcul | Essai Lean, D-1a ; aucun appel de modèle | 65 USD | 2026-11-30 "
                  "| Lazar | R |\n" + lignes_go, encoding="utf-8")
    dep = tmp_path / "depenses.md"
    dep.write_text("| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |\n"
                   "|---|---|---|---|---|---|---|---|---|\n" + ligne_depense, encoding="utf-8")
    decisions = tmp_path / "decisions"
    decisions.mkdir(exist_ok=True)
    (decisions / "decision-N-013-v1.md").write_text("décision\n")
    return go, dep, tmp_path / "creations.jsonl", decisions


def creer(api, go, dep, creations, decisions, **k):
    d = dict(go_id="GO-2026-11-10-13", chemin_go=go, chemin_depenses=dep, journal_creations=creations,
             dossier_decisions=decisions, type_serveur="ccx33", image="ubuntu-24.04", lieu="hel1", cles_ssh=[1],
             pare_feux=[2], taux_usd_eur=1.25, aujourdhui=JOUR, horloge=lambda: T0, dormir=lambda s: None, tours_max=1,
             jeton="a" * 32)
    d.update(k)
    return M.creer_et_veiller(client(api), **d)


def test_creation_saine_intention_avant_l_appel(tmp_path):
    go, dep, journal, decisions = fichiers(tmp_path)
    api = FauxAPI()
    vu = []
    api.avant_post = lambda: vu.append(lignes(journal))
    r = creer(api, go, dep, journal, decisions)
    assert r["detruit"] is False
    assert vu[0][0]["intention"] and vu[0][0]["etiquette"] == "a" * 32          # écrite avant l'appel de création
    assert api.corps[0]["labels"]["creation"] == "a" * 32 and api.corps[0]["public_net"]["enable_ipv6"] is False
    e = lignes(journal)
    assert e[1]["creation"] and e[1]["identifiant"] == 777


def test_reponse_perdue_recherche_par_etiquette_et_destruction(tmp_path):
    go, dep, journal, decisions = fichiers(tmp_path)
    api = FauxAPI(perdre_post=True)
    with open(tmp_path / "j.jsonl", "w") as j, pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, go, dep, journal, decisions, journal=j)
    assert ("DELETE", "/servers/777") in api.appels and 777 not in api.serveurs
    e = lignes(journal)
    assert e[0]["intention"] and e[-1]["destruction_confirmee"] and e[-1]["identifiant"] == 777
    assert any(x.get("creation") == "incertaine" for x in lignes(tmp_path / "j.jsonl"))


def test_cli_detruire_par_etiquette(tmp_path, capsys):
    api = FauxAPI()
    api.serveurs[777] = {"name": H.NOM_MACHINE, "labels": {"creation": "b" * 32}}
    assert M.main(["detruire", "--etiquette", "b" * 32, "--journal", str(tmp_path / "j.jsonl")], client=client(api),
                  dormir=lambda s: None) == 0
    assert 777 not in api.serveurs


# ---- CLC2-06 -------------------------------------------------------------------------------------------------------------------

def test_verifier_coupure_v3(tmp_path):
    api = FauxAPI({777: H.NOM_MACHINE})
    api.pare_feux[2] = {"rules": H.regles_coupure("203.0.113.5"), "applied_to": [{"type": "server", "server": {"id": 777}}]}
    assert H.verifier_coupure_nuage(client(api), 2, 777)["pare_feux_du_serveur"] == [{"id": 2, "status": "applied"}]
    for pares in ([{"id": 2, "status": "pending"}], [{"id": 2, "status": "applied"}, {"id": 3, "status": "applied"}], []):
        api.pare_feux_serveur = pares
        with pytest.raises(GardeArret, match="pare-feux du serveur"):
            H.verifier_coupure_nuage(client(api), 2, 777)
    api.pare_feux_serveur = [{"id": 2, "status": "applied"}]
    j = tmp_path / "j.jsonl"
    assert M.main(["verifier-coupure", "--serveur", "777", "--pare-feu", "2", "--journal", str(j)], client=client(api)) == 0
    assert "verification_coupure" in lignes(j)[0]


# ---- CLC2-07 -------------------------------------------------------------------------------------------------------------------

def test_lire_montant_v3():
    assert M.lire_montant("18.52") == 18.52 and M.lire_montant("1.96") == 1.96
    assert M.lire_montant("≈ 1 050,40") == pytest.approx(1050.40) and M.lire_montant("≈ 0,47") == 0.47
    assert M.lire_montant("1,234.5") is None and M.lire_montant("1.234.5") is None and M.lire_montant("—") is None
    assert M.lire_montant("0,30 0,30") is None and M.lire_montant("≈ 0,47 (≈ 0,5 sur 150)") == 0.47
    with pytest.raises(GardeArret, match="négatif"):
        M.lire_montant("-3,00")


def test_mot_de_lazar_verifie(tmp_path):
    go, dep, journal, decisions = fichiers(tmp_path, lignes_go="| GO-2026-11-11-01 | 2026-11-11 | calcul | seconde "
                                                               "machine | 65 USD | 2026-11-30 | mère | R |\n")
    assert M.verifier_mot_de_lazar("GO-2026-11-10-13", go, decisions, JOUR).startswith("GO GO-2026-11-10-13")
    assert M.verifier_mot_de_lazar("N-013", go, decisions, JOUR).startswith("décision N-013")
    for mot in ("x", "oui", "N-999", "GO-2026-11-11-01", "GO-2026-12-31-01"):
        with pytest.raises(GardeArret):
            M.verifier_mot_de_lazar(mot, go, decisions, JOUR)


def test_seconde_machine_et_journal_fixe(tmp_path):
    go, dep, journal, decisions = fichiers(tmp_path)
    creer(FauxAPI(), go, dep, journal, decisions)
    with pytest.raises(GardeArret, match="seconde machine"):
        creer(FauxAPI(), go, dep, journal, decisions)
    with pytest.raises(GardeArret, match="mot de Lazar 'x'"):
        creer(FauxAPI(), go, dep, journal, decisions, mot_de_lazar="x", jeton="c" * 32)
    assert creer(FauxAPI(), go, dep, journal, decisions, mot_de_lazar="N-013", jeton="d" * 32)["detruit"] is False
    with pytest.raises(SystemExit):   # le chemin du journal n'est pas une option de la commande
        M.main(["creer-et-veiller", "--go", "GO-2026-11-10-13", "--type", "ccx33", "--lieu", "hel1", "--cle-ssh", "1",
                "--pare-feu", "2", "--taux-usd-eur", "1.25", "--journal", str(tmp_path / "j"),
                "--journal-creations", str(tmp_path / "autre.jsonl")], client=client(FauxAPI()))
    assert M.JOURNAL_CREATIONS.name == "journal-creations-machines-v1.jsonl"


def test_deja_depense_par_le_journal(tmp_path):
    go, dep, journal, decisions = fichiers(tmp_path)
    journal.write_text(json.dumps({"go": "GO-2026-11-10-13", "intention": True, "etiquette": "e" * 32,
                                   "heure_intention": (T0 - timedelta(hours=10)).isoformat(), "prix_usd_h": 1.0}) + "\n")
    d = M.deja_depense_go(dep, "GO-2026-11-10-13", journal, None, T0)
    assert d["journal"] == 10.0 and d["retenu"] == 10.0
    # ccx33 à 5,5 USD l'euro : 0,227 × 5,5 = 1,2485 USD/h, × 48 = 59,9 : tient sous 65, pas sous 65 − 10 (journal)
    M.verifier_devis(0.227 * 5.5, "D-1a")
    with pytest.raises(GardeArret, match="reste du plafond 55.00"):
        creer(FauxAPI(), go, dep, journal, decisions, taux_usd_eur=5.5, mot_de_lazar="N-013")


# ---- CLC2-08 n17 et note 6 : prix ------------------------------------------------------------------------------------------------

def test_prix_ipv4_filtre_devise_et_pages():
    assert client(FauxAPI(ipv6_avant=True)).prix_horaire_eur("ccx33", "hel1")["total"] == pytest.approx(0.2270)
    with pytest.raises(GardeArret, match="devise"):
        client(FauxAPI(devise="USD")).prix_horaire_eur("ccx33", "hel1")
    with pytest.raises(GardeArret, match="plusieurs pages"):
        client(FauxAPI(page_suivante=True)).prix_horaire_eur("ccx33", "hel1")
