"""Essais R5 de la minuterie v5 et du client Hetzner v5 (contre-lecture `918662a7…`, R-2323) : CLC4-01, -03, -05, -06, -07,
-08 (n1 à n20), et les commandes de la procédure du poste local (préparer, pousser, détacher, accès). Faux transport : aucun
appel réseau, aucun serveur, aucun processus réel de minuterie ; un seul essai lance `git` sur des dépôts jetables du bac.
Toute pause passe par un dormeur borné : une boucle sans fin lève `BoucleSansFin` (hors `Exception`) au lieu de tourner."""
import json
import os
import subprocess
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v5 as H
from controle_ia.lean_essai import minuterie_v5 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)
GO = "GO-2026-11-10-13"
JETON = "a" * 32
FIXES = {"essai": "lean", "pas": "d1a"}
TYPES = [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2390"}},
                                      {"location": "fsn1", "price_hourly": {"gross": "0.2990"}}]}]
PRIX_HEL1 = (0.2390 + 0.0010) * 1.25   # 0,30 USD/h
CLE_PUB = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExempleExempleExempleExempleExempleExemple essai"
PAUSES_MAX = 2000


class BoucleSansFin(BaseException):
    """Hors `Exception` : aucune boucle de retentatives ne l'attrape."""


PAUSES = {"n": 0}


@pytest.fixture(autouse=True)
def _pauses_a_zero():
    PAUSES["n"] = 0


def rien(_s):
    PAUSES["n"] += 1
    if PAUSES["n"] > PAUSES_MAX:
        raise BoucleSansFin(f"plus de {PAUSES_MAX} pauses : boucle sans fin arrêtée par l'essai")


def dormeur(liste):
    def dormir(s):
        liste.append(s)
        rien(s)
    return dormir


def suite_d_heures(*heures):
    """Horloge qui rend les heures données dans l'ordre, puis la dernière pour toujours."""
    reste = list(heures)
    return lambda: reste.pop(0) if len(reste) > 1 else reste[0]


class FauxAPI:
    def __init__(self, serveurs=None, *, forme="location", statut_post=201, perdre_post=False, apparition_apres=0,
                 statut_delete=200, pannes_get=0, page_suivante=False, apres_delete=None, statut_inventaire=200,
                 pannes_delete=0, statut_lecture=200):
        self.serveurs = {i: dict(s) for i, s in (serveurs or {}).items()}
        self.forme, self.statut_post, self.perdre_post = forme, statut_post, perdre_post
        self.apparition_apres, self.statut_delete, self.pannes_get = apparition_apres, statut_delete, pannes_get
        self.page_suivante, self.apres_delete = page_suivante, apres_delete
        self.statut_inventaire, self.pannes_delete, self.statut_lecture = statut_inventaire, pannes_delete, statut_lecture
        self.cache, self.recherches, self.appels, self.corps = {}, 0, [], []
        self.cles, self.pare_feux, self.prochain = {}, {}, 500

    def _serveur(self, i):
        s = self.serveurs[i]
        d = {"id": i, "name": s["name"], "labels": s.get("labels", {}), "created": s.get("created", "2026-11-11T01:00:30+00:00"),
             "server_type": {"name": "ccx33"}, "public_net": {"firewalls": [{"id": 2, "status": "applied"}]}}
        if self.forme in ("location", "les_deux"):
            d["location"] = {"name": "hel1"}
        if self.forme in ("datacenter", "les_deux"):
            d["datacenter"] = {"location": {"name": "hel1" if self.forme == "datacenter" else "fsn1"}}
        return d

    def __call__(self, methode, chemin, corps=None):
        self.appels.append((methode, chemin))
        if methode == "GET" and chemin.startswith("/servers/"):
            if self.pannes_get > 0:
                self.pannes_get -= 1
                raise H.ErreurHetzner("injoignable (essai)")
            if self.statut_lecture != 200:
                return self.statut_lecture, {"error": {"code": "unauthorized"}}
            i = int(chemin.rsplit("/", 1)[1])
            return (200, {"server": self._serveur(i)}) if i in self.serveurs else (404, {"error": {"code": "not_found"}})
        if methode == "GET" and chemin.startswith("/servers?label_selector="):
            self.recherches += 1
            if self.recherches > self.apparition_apres:
                self.serveurs.update(self.cache)
                self.cache = {}
            selecteur = urllib.parse.unquote(chemin.split("label_selector=", 1)[1].split("&")[0])
            paires = dict(x.split("=") for x in selecteur.split(","))
            meta = {"pagination": {"next_page": 2}} if (self.page_suivante and "essai" in paires) else {"pagination": {}}
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()
                                     if all(s.get("labels", {}).get(k) == v for k, v in paires.items())], "meta": meta}
        if methode == "GET" and chemin.startswith("/servers?"):
            if self.statut_inventaire != 200:
                return self.statut_inventaire, {"error": {"code": "unauthorized"}}
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()],
                         "meta": {"pagination": {}}}
        if methode == "DELETE" and chemin.startswith("/servers/"):
            if self.statut_delete != 200:
                return self.statut_delete, {"error": {"code": "forbidden"}}
            if self.pannes_delete > 0:
                self.pannes_delete -= 1
                raise H.ErreurHetzner("échange interrompu (essai)")
            self.serveurs.pop(int(chemin.rsplit("/", 1)[1]), None)
            if self.apres_delete:
                self.apres_delete(self)
            return 200, {}
        if methode == "POST" and chemin == "/servers":
            self.corps.append(corps)
            if self.statut_post == 422:
                return 422, {"error": {"code": "invalid_input"}}
            nouveau = {778: {"name": corps["name"], "labels": corps["labels"]}}
            if self.apparition_apres:
                self.cache.update(nouveau)
            else:
                self.serveurs.update(nouveau)
            if self.perdre_post:
                raise H.ErreurHetzner("échange interrompu (TimeoutError)")
            if self.statut_post != 201:
                return self.statut_post, {"error": {"code": "x"}}
            return 201, {"server": {"id": 778, "name": corps["name"], "created": "2026-11-11T01:00:30Z"}}
        if methode == "GET" and chemin.startswith("/server_types"):
            return 200, {"server_types": TYPES, "meta": {"pagination": {}}}
        if methode == "GET" and chemin == "/pricing":
            return 200, {"pricing": {"currency": "EUR", "primary_ips": [
                {"type": "ipv4", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.0010"}},
                                            {"location": "fsn1", "price_hourly": {"gross": "0.0010"}}]}]}}
        if methode == "POST" and chemin in ("/ssh_keys", "/firewalls"):
            self.prochain += 1
            magasin, cle = (self.cles, "ssh_key") if chemin == "/ssh_keys" else (self.pare_feux, "firewall")
            magasin[self.prochain] = {"id": self.prochain, "name": corps["name"], "labels": corps.get("labels", {}),
                                      "rules": corps.get("rules", []), "fingerprint": "aa:bb:cc"}
            return 201, {cle: magasin[self.prochain]}
        if chemin.startswith("/firewalls/") and chemin.endswith("/actions/set_rules"):
            self.pare_feux[int(chemin.split("/")[2])]["rules"] = corps["rules"]
            return 201, {"actions": []}
        for prefixe, magasin, cle in (("/ssh_keys/", self.cles, "ssh_key"), ("/firewalls/", self.pare_feux, "firewall")):
            if chemin.startswith(prefixe):
                i = int(chemin.rsplit("/", 1)[1])
                if methode == "GET":
                    return (200, {cle: magasin[i]}) if i in magasin else (404, {"error": {"code": "not_found"}})
                if methode == "DELETE":
                    magasin.pop(i, None)
                    return 204, {}
        return 500, {"error": {"code": "inattendu"}}


def client(api):
    return H.ClientHetzner5(transport=api, dormir=rien)


def lignes(chemin):
    return [json.loads(x) for x in Path(chemin).read_text(encoding="utf-8").splitlines() if x.strip()]


def depot(tmp_path, ligne_depense="", lignes_go=""):
    racine = tmp_path / "clone"
    (racine / "registres").mkdir(parents=True)
    (racine / "registres" / "go.md").write_text(
        f"| {GO} | 2026-11-10 | calcul | Essai Lean, D-1a ; aucun appel de modèle | 65 USD | 2026-11-30 | Lazar | R |\n"
        + lignes_go, encoding="utf-8")
    (racine / "registres" / "depenses.md").write_text(
        "| date | GO | devis | instance (identifiant) | type | heures | coût (USD) | cumul sur devis | note |\n"
        "|---|---|---|---|---|---|---|---|---|\n" + ligne_depense, encoding="utf-8")
    (racine / M.DOSSIER_RELATIF).mkdir(parents=True)
    return M.chemins_depot(racine)


def preparer(chemins, limite_h=2.0, tache_h=40.0, jeton=JETON):
    r = M.preparer(go_id=GO, chemins=chemins, heure_limite_creation=T0 + timedelta(hours=limite_h),
                   heure_tache_mere=T0 + timedelta(hours=tache_h), horloge=lambda: T0, jeton=jeton)
    return Path(r["rattrapage"])


def vivante(_mi, _dormir):
    return {"vivante": True, "garder": True, "motif": ""}


def creer(api, chemins, rattrapage, **k):
    vus = k.pop("vus", {})

    def lancer(**kw):
        vus.update(kw)
        return {"pid": 4242, "fichier_pid": "f", "journal": "j"}
    d = dict(go_id=GO, chemins=chemins, rattrapage=rattrapage, type_serveur="ccx33", image="ubuntu-24.04", lieu="hel1",
             cles_ssh=[1], pare_feux=[2], horloge=lambda: T0, dormir=rien, lancer=lancer, controler=vivante,
             verifier_pousse=lambda racine, chemin: (True, "essai"), fenetre_s=60.0)
    d.update(k)
    return M.creer_et_armer(client(api), **d)


def veiller_cli(api, tmp_path, *extra, heure=T0 + timedelta(hours=49), depuis=T0):
    j = tmp_path / f"veille-{len(list(tmp_path.glob('veille-*')))}.jsonl"
    horloge = heure if callable(heure) else (lambda: heure)
    code = M.main(["veiller", "--identifiant", "778", "--depuis", depuis.isoformat(), "--journal", str(j), *extra],
                  client=client(api), dormir=rien, horloge=horloge)
    return code, lignes(j)


SERVEUR = {778: {"name": H.NOM_MACHINE, "labels": dict(FIXES, creation=JETON, go=GO)}}
UNE_HEURE, ECHUE = T0 + timedelta(hours=1), T0 + timedelta(hours=49)


# ---- CLC4-01 : la minuterie ne meurt pas à son démarrage ------------------------------------------------------------------------

def test_lieu_des_deux_formes_et_sans():
    assert H.lieu_du_serveur({"location": {"name": "hel1"}}) == ("hel1", "location")
    assert H.lieu_du_serveur({"datacenter": {"location": {"name": "fsn1"}}}) == ("fsn1", "datacenter.location")
    assert H.lieu_du_serveur({"location": {"name": "hel1"}, "datacenter": {"location": {"name": "fsn1"}}})[0] == "hel1"
    for s in ({}, None, {"location": 5}, {"location": {}}, {"datacenter": "x"}, {"datacenter": {"location": None}},
              {"location": {"name": "  "}}, []):
        assert H.lieu_du_serveur(s) == (None, "aucune")
    assert H.type_du_serveur({"server_type": {"name": "ccx33"}}) == "ccx33" and H.type_du_serveur({}) is None
    assert H.creation_du_serveur({"created": "2026-11-11T01:00:30Z"}) == T0 + timedelta(seconds=30)
    assert H.creation_du_serveur({"created": "hier"}) is None and H.creation_du_serveur({"created": "2026-11-11T01:00"}) is None


@pytest.mark.parametrize("forme,extra,lieu,source", [
    ("location", [], "hel1", "location"), ("datacenter", [], "hel1", "datacenter.location"),
    ("les_deux", [], "hel1", "location"), ("aucune", ["--lieu", "hel1"], "hel1", "--lieu"),
    ("aucune", [], None, "aucune")])
def test_veiller_demarre_sur_chaque_forme(tmp_path, forme, extra, lieu, source):
    api = FauxAPI(SERVEUR, forme=forme)
    code, j = veiller_cli(api, tmp_path, *extra)
    fait = [e for e in j if e.get("demarrage") == "fait"]
    assert code == 0 and 778 not in api.serveurs and len(fait) == 1
    assert fait[0]["lieu"] == lieu and fait[0]["source_lieu"] == source
    if lieu:
        assert fait[0]["prix_usd_h"] == pytest.approx(PRIX_HEL1)
    else:
        assert any("pire cas" in str(e.get("demarrage")) for e in j) and fait[0]["prix_usd_h"] == pytest.approx(65 / 48)


def test_demarrage_sous_retentatives(tmp_path):
    api = FauxAPI(SERVEUR, pannes_get=2)
    code, j = veiller_cli(api, tmp_path, heure=suite_d_heures(UNE_HEURE, UNE_HEURE, UNE_HEURE, ECHUE))
    assert code == 0 and [e["demarrage"] for e in j if "demarrage" in e][:3] == ["échec", "échec", "fait"]
    assert any(e.get("detruire") is False and e["motif"].startswith("garder") for e in j) and 778 not in api.serveurs


def test_demarrage_echeance_passee_sans_lecture(tmp_path):
    api = FauxAPI(SERVEUR, pannes_get=3)
    code, j = veiller_cli(api, tmp_path, "--prix-usd-h", "0.3")
    assert code == 0 and 778 not in api.serveurs
    assert any("échéance passée sans lecture" in str(e.get("demarrage")) for e in j)


def test_depuis_plus_tard_que_la_creation(tmp_path):   # la création lue, plus tôt, compte
    api = FauxAPI(SERVEUR)
    code, _ = veiller_cli(api, tmp_path, heure=T0 + timedelta(hours=48, minutes=1), depuis=T0 + timedelta(hours=5))
    assert code == 0 and 778 not in api.serveurs


def test_echeance_plus_longue_refusee(tmp_path, capsys):   # k13 gardé
    api = FauxAPI(SERVEUR)
    code, _ = veiller_cli(api, tmp_path, "--echeance-h", "60")
    assert code == 1 and "plus longue" in capsys.readouterr().err and 778 in api.serveurs


def test_devis_reverifie_au_demarrage(tmp_path):   # n16 : devis non tenu ⇒ destruction immédiate
    api = FauxAPI(SERVEUR)
    code, j = veiller_cli(api, tmp_path, "--deja-depense-usd", "60", heure=UNE_HEURE)
    assert code == 0 and 778 not in api.serveurs
    assert any("devis non tenu" in str(e.get("demarrage")) for e in j)


def test_plafond_retranche_du_deja_depense(tmp_path):   # n20
    api = FauxAPI(SERVEUR)
    code, j = veiller_cli(api, tmp_path, "--deja-depense-usd", "20", heure=suite_d_heures(UNE_HEURE, ECHUE))
    fait = [e for e in j if e.get("demarrage") == "fait"][0]
    assert code == 0 and fait["plafond_usd"] == pytest.approx(45.0) and 778 not in api.serveurs
    assert any(e.get("detruire") is False and e["motif"].startswith("garder") for e in j)


def test_prix_le_plus_haut_retenu(tmp_path):   # prix passé plus bas que le prix lu : le lu compte
    api = FauxAPI(SERVEUR)
    code, j = veiller_cli(api, tmp_path, "--prix-usd-h", "0.1")
    assert code == 0 and [e for e in j if e.get("demarrage") == "fait"][0]["prix_usd_h"] == pytest.approx(PRIX_HEL1)


def test_minuterie_lecture_refusee_au_demarrage(tmp_path, capsys):   # 401 durable dès la première lecture
    api = FauxAPI(SERVEUR, statut_lecture=401)
    code, j = veiller_cli(api, tmp_path)
    assert code == 3 and "à la main par l'identifiant 778" in capsys.readouterr().err and 778 in api.serveurs


def test_refus_de_nom_au_demarrage(tmp_path, capsys):
    api = FauxAPI({778: {"name": "autre", "labels": {}}})
    code, _ = veiller_cli(api, tmp_path)
    assert code == 1 and 778 in api.serveurs and "R10" in capsys.readouterr().err


def test_minuterie_detachee_arguments_complets(tmp_path):   # n9, n15 : tout passe en arguments, lisibles par `veiller`
    vus = {}

    class P:
        pid = 4242

    def popen(argv, **k):
        vus.update(argv=argv, **k)
        return P()
    k = dict(identifiant=778, pas="d1a", depuis=T0, echeance_h=39.0, taux=1.3, deja=20.0, jeton=JETON, go_id=GO, lieu="hel1",
             prix_usd_h=0.31, dossier=tmp_path, racine=tmp_path, popen=popen)
    r = M.lancer_minuterie_detachee(**k)
    assert vus["start_new_session"] is True and vus["argv"][3] == M.MODULE
    a = M.construire_analyseur().parse_args(vus["argv"][4:])
    assert (a.action, a.identifiant, a.taux_usd_eur, a.deja_depense_usd, a.echeance_h, a.lieu, a.prix_usd_h, a.go,
            a.etiquette, a.depot) == ("veiller", 778, 1.3, 20.0, 39.0, "hel1", 0.31, GO, JETON, str(tmp_path))
    assert Path(r["fichier_pid"]).read_text().split() == ["4242", "778", JETON]
    with pytest.raises(GardeArret, match="R12"):
        M.lancer_minuterie_detachee(**k)


def test_creer_passe_deja_taux_et_echeance(tmp_path):   # n9, n15 côté création ; échéance bornée par la tâche de la mère
    chemins = depot(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | — | — | — | 20,00 | — | — |\n")
    vus = {}
    r = creer(FauxAPI(), chemins, preparer(chemins, tache_h=30.0), taux_declare=1.3, deja_declare=20.0, vus=vus)
    assert vus["deja"] == 20.0 and vus["taux"] == 1.3 and vus["lieu"] == "hel1" and vus["jeton"] == JETON
    assert vus["echeance_h"] == pytest.approx(29.0) and r["echeance"] == (T0 + timedelta(hours=29)).isoformat()
    assert vus["prix_usd_h"] == pytest.approx((0.2390 + 0.0010) * 1.3)
    chemins = depot(tmp_path / "b")
    vus = {}
    creer(FauxAPI(), chemins, preparer(chemins), taux_declare=0.5, vus=vus)
    assert vus["taux"] == 1.25 and vus["prix_usd_h"] == pytest.approx(PRIX_HEL1)


@pytest.mark.parametrize("survie", [{"vivante": False, "garder": False, "motif": "processus absent"},
                                    {"vivante": True, "garder": False, "motif": "aucune ligne « garder » en 60 s"}])
def test_minuterie_morte_ou_muette_detruit(tmp_path, survie):
    chemins = depot(tmp_path)
    api = FauxAPI()
    with pytest.raises(GardeArret, match="minuterie non armée.*détruit"):
        creer(api, chemins, preparer(chemins), controler=lambda mi, d: survie)
    assert 778 not in api.serveurs and lignes(chemins["creations"])[-1]["destruction_confirmee"]


def test_controle_par_defaut_de_la_survie(tmp_path):   # sans contrôleur injecté : PID réel absent ⇒ détruit
    chemins = depot(tmp_path)
    api = FauxAPI()
    pid = tmp_path / "pid.txt"
    pid.write_text(f"{2 ** 22 + 7} 778 {JETON}\n")

    def lancer(**kw):
        return {"pid": 2 ** 22 + 7, "fichier_pid": str(pid), "journal": str(tmp_path / "rien.jsonl")}
    d = dict(go_id=GO, chemins=chemins, rattrapage=preparer(chemins), type_serveur="ccx33", image="ubuntu-24.04",
             lieu="hel1", cles_ssh=[1], pare_feux=[2], horloge=lambda: T0, dormir=rien, lancer=lancer,
             verifier_pousse=lambda racine, chemin: (True, "essai"), fenetre_s=60.0)
    with pytest.raises(GardeArret, match="minuterie non armée.*processus absent"):
        M.creer_et_armer(client(api), **d)
    assert 778 not in api.serveurs


def test_lancement_en_echec_detruit(tmp_path):   # n3
    chemins = depot(tmp_path)
    api = FauxAPI()

    def lancer(**kw):
        raise OSError("python introuvable")
    with pytest.raises(GardeArret, match="minuterie non armée"):
        creer(api, chemins, preparer(chemins), lancer=lancer)
    assert 778 not in api.serveurs


def test_attendre_minuterie(tmp_path):
    j = tmp_path / "j.jsonl"
    mi = {"fichier_pid": str(tmp_path / "pid"), "journal": str(j)}
    pauses = []

    def vit(_f):
        return {"vivante": True, "motif": ""}
    r = M.attendre_minuterie(mi, dormir=dormeur(pauses), verifier=vit, delai_s=10, pas_s=2)
    assert r["motif"].startswith("aucune ligne") and sum(pauses) == 10
    j.write_text(json.dumps({"detruire": False, "motif": "garder (cumul 0.30 USD)"}) + "\n")
    assert M.attendre_minuterie(mi, dormir=dormeur(pauses), verifier=vit)["garder"]
    mort = M.attendre_minuterie(mi, dormir=dormeur(pauses), verifier=lambda f: {"vivante": False, "motif": "absent"})
    assert mort == {"vivante": False, "garder": False, "motif": "absent"}


# ---- CLC4-03 : aucun chemin en dur ; contrôle portable -------------------------------------------------------------------------

def test_racine_deduite_ou_donnee(tmp_path):
    for module in (M, H):
        assert "/home/user" not in Path(module.__file__).read_text(encoding="utf-8")
    assert (M.racine_depot() / "src" / "controle_ia" / "lean_essai" / "minuterie_v5.py").is_file()
    assert M.racine_depot(str(tmp_path)) == tmp_path.resolve()
    with pytest.raises(GardeArret, match="--depot"):
        M.chemins_depot(tmp_path)
    chemins = depot(tmp_path)
    code = M.main(["preparer", "--depot", str(chemins["racine"]), "--go", GO, "--heure-limite-creation",
                   (T0 + timedelta(hours=2)).isoformat(), "--heure-tache-mere", (T0 + timedelta(hours=40)).isoformat()],
                  horloge=lambda: T0)
    assert code == 0 and len(list(chemins["verse"].glob("rattrapage-machine-d1a-*-v1.json"))) == 1


def fichier_pid(tmp_path, pid=4242):
    f = tmp_path / "pid.txt"
    f.write_text(f"{pid} 778 {JETON}\n")
    return f


ARGV = ["/usr/bin/python3", "-B", "-m", M.MODULE, "veiller", "--identifiant", "778", "--journal", "/x y/j.jsonl"]


def faux_proc(tmp_path, argv=ARGV):
    proc = tmp_path / "proc"
    (proc / "self").mkdir(parents=True, exist_ok=True)
    (proc / "4242").mkdir(exist_ok=True)
    (proc / "4242" / "cmdline").write_bytes(b"\0".join(x.encode() for x in argv) + b"\0")
    return proc


def test_verifier_minuterie_linux(tmp_path):
    proc, f = faux_proc(tmp_path), fichier_pid(tmp_path)
    r = M.verifier_minuterie(f, proc)
    assert r["vivante"] and r["conforme"] and r["methode"] == "/proc"
    faux_proc(tmp_path, ["/usr/bin/sleep", "100"])
    assert not M.verifier_minuterie(f, proc)["vivante"]
    faux_proc(tmp_path, ARGV[:6] + ["7781"])
    assert not M.verifier_minuterie(f, proc)["vivante"]
    (proc / "4242" / "cmdline").unlink()
    assert M.verifier_minuterie(f, proc)["motif"].startswith("processus absent")


def test_verifier_minuterie_macos(tmp_path):
    f, sans_proc = fichier_pid(tmp_path), tmp_path / "pas-de-proc"
    ligne = " ".join(ARGV)
    r = M.verifier_minuterie(f, sans_proc, existe=lambda pid: "présent", ps=lambda pid: ligne)
    assert r["vivante"] and r["methode"] == "kill -0 et ps -p"
    assert not M.verifier_minuterie(f, sans_proc, existe=lambda pid: "présent", ps=lambda pid: "/bin/zsh")["vivante"]
    r = M.verifier_minuterie(f, sans_proc, existe=lambda pid: "absent", ps=lambda pid: ligne)
    assert r["motif"].startswith("processus absent")
    assert not M.verifier_minuterie(f, sans_proc, existe=lambda pid: "autre utilisateur", ps=lambda pid: ligne)["vivante"]


def test_kill_0_et_ps_reels():
    vus = []

    def executer(argv, **k):
        vus.append(argv)
        return subprocess.CompletedProcess(argv, 0, stdout="x\n", stderr="")
    assert M._ps(77, executer) == "x" and vus == [["ps", "-ww", "-p", "77", "-o", "command="]]
    assert M._existe(os.getpid()) == "présent" and M._existe(2 ** 22 + 7) == "absent"
    assert "python" in M._ps(os.getpid()).lower()


def test_fraicheur_des_lignes_garder(tmp_path):
    proc, f = faux_proc(tmp_path), fichier_pid(tmp_path)
    j = tmp_path / "j.jsonl"
    j.write_text(json.dumps({"heure": T0.isoformat(), "detruire": False, "motif": "garder (cumul 0.30 USD)"}) + "\n")
    assert M.verifier_minuterie(f, proc, journal_minuterie=j, horloge=lambda: T0 + timedelta(minutes=2))["conforme"]
    r = M.verifier_minuterie(f, proc, journal_minuterie=j, horloge=lambda: T0 + timedelta(minutes=10))
    assert r["vivante"] and not r["conforme"] and "muette" in r["motif"]


# ---- CLC4-05 : refus durable borné, bruyant, code distinct ---------------------------------------------------------------------

def test_detruire_refus_durable_borne(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, statut_delete=403)
    pauses = []
    assert M.main(["detruire", "--pas", "d1a"], client=client(api), dormir=dormeur(pauses)) == M.CODE_DESTRUCTION_REFUSEE == 3
    err = capsys.readouterr().err
    assert "à la main" in err and "identifiant 1" in err and "refus durable" in err
    assert sum(1 for a in api.appels if a[0] == "DELETE") == M.REFUS_DURABLES_MAX and len(pauses) < 10 and 1 in api.serveurs


def test_lecture_refusee_401_bornee(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, statut_inventaire=401)
    assert M.main(["detruire", "--pas", "d1a"], client=client(api), dormir=rien) == 3
    assert "à la main" in capsys.readouterr().err


def test_echecs_passagers_ecrits_sans_journal(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, pannes_delete=2)
    assert M.main(["detruire", "--identifiant", "1"], client=client(api), dormir=rien) == 0 and 1 not in api.serveurs
    assert capsys.readouterr().err.count('"destruction": "échec"') == 2


def test_minuterie_refus_durable_a_l_echeance(tmp_path):
    api = FauxAPI(SERVEUR, statut_delete=403)
    code, j = veiller_cli(api, tmp_path)
    assert code == 3 and 778 in api.serveurs and j[-1]["arret"] == "DestructionRefusee"


# ---- CLC4-06, n1, n17 : bon nom d'abord, autre nom jamais touché ----------------------------------------------------------------

def test_bon_nom_detruit_autre_nom_nomme():
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}, 2: {"name": "lean-outillage-d1a-bis", "labels": FIXES},
                   3: {"name": H.NOM_MACHINE, "labels": {}}})
    with pytest.raises(GardeArret, match=r"2 serveur\(s\).*lean-outillage-d1a-bis.*NON touché"):
        M.detruire_pas(client(api), "d1a", dormir=rien)
    assert sorted(api.serveurs) == [2] and ("DELETE", "/servers/2") not in api.appels
    api = FauxAPI({5: {"name": H.NOM_MACHINE, "labels": {"creation": "c" * 32}},
                   6: {"name": "autre", "labels": {"creation": "c" * 32}}})
    with pytest.raises(GardeArret, match="NON touché"):
        M.rattraper_par_etiquette(client(api), "c" * 32, dormir=rien, fenetre_s=0.0)
    assert sorted(api.serveurs) == [6]


def test_pas_ne_prend_que_son_pas():
    api = FauxAPI({9: {"name": "lean-outillage-d1b", "labels": {"essai": "lean", "pas": "d1b"}}})
    assert M.detruire_pas(client(api), "d1a", dormir=rien)["message"] == "aucun serveur de l'essai" and 9 in api.serveurs


# ---- CLC4-07, n18 : journal soldé ; seconde machine refusée sans exception -----------------------------------------------------

def test_journal_solde_par_detruire_et_par_la_minuterie(tmp_path):
    chemins = depot(tmp_path)
    api = FauxAPI()
    creer(api, chemins, preparer(chemins))
    M.detruire_pas(client(api), "d1a", dormir=rien,
                   solder=M.fabrique_solder(chemins["creations"], lambda: T0 + timedelta(hours=2)))
    cout = [M.cout_journal(chemins["creations"], GO, T0 + timedelta(hours=h)) for h in (3, 48, 400)]
    assert cout[0] == cout[1] == cout[2] == pytest.approx(2 * PRIX_HEL1)
    j = tmp_path / "v.jsonl"
    assert M.main(["veiller", "--identifiant", "778", "--depuis", T0.isoformat(), "--go", GO, "--etiquette", "b" * 32,
                   "--journal", str(j), "--depot", str(chemins["racine"])], client=client(FauxAPI(SERVEUR)), dormir=rien,
                  horloge=lambda: ECHUE) == 0
    assert lignes(chemins["creations"])[-1] == {"go": GO, "etiquette": "b" * 32, "destruction_confirmee": True,
                                                "identifiant": 778, "heure": ECHUE.isoformat()}


def test_seconde_machine_refusee_sans_exception(tmp_path):
    chemins = depot(tmp_path)
    api = FauxAPI()
    ratt = preparer(chemins)
    creer(api, chemins, ratt)
    api.serveurs.clear()
    with pytest.raises(GardeArret, match="sans exception"):
        creer(api, chemins, ratt)
    with pytest.raises(GardeArret, match="sans exception"):
        preparer(chemins, jeton="b" * 32)
    chemins2 = depot(tmp_path / "b",
                     "| 2026-11-11 | GO-2026-11-10-13 | D-1a | Hetzner 12345678 | ccx33 | 3 | 1,00 | — | — |\n")
    with pytest.raises(GardeArret, match="sans exception"):
        preparer(chemins2)
    with pytest.raises(SystemExit):
        M.construire_analyseur().parse_args(["creer-et-armer", "--mot-de-lazar", GO])
    assert len(api.corps) == 1


# ---- CLC4-08 : n5, note 1, n8, n10, n12, n14, n19 ------------------------------------------------------------------------------

def test_statut_500_incertain_detruit(tmp_path):   # n5
    chemins = depot(tmp_path)
    api = FauxAPI(statut_post=500)
    with pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, chemins, preparer(chemins))
    assert 778 not in api.serveurs


def test_refus_4xx_recherche_de_controle(tmp_path):   # note 1
    chemins = depot(tmp_path)
    api = FauxAPI(statut_post=409)   # refus annoncé, serveur pourtant créé
    with pytest.raises(GardeArret, match="refusée par l'API.*trouvé"):
        creer(api, chemins, preparer(chemins))
    assert 778 not in api.serveurs
    chemins = depot(tmp_path / "b")
    with pytest.raises(GardeArret, match="aucun serveur créé"):
        creer(FauxAPI(statut_post=422), chemins, preparer(chemins))
    assert lignes(chemins["creations"])[-1]["aucune_creation"]


def test_rattrapage_fenetre_et_rien_trouve(tmp_path):   # CLC3-08 rejoué ; code 4
    chemins = depot(tmp_path)
    api = FauxAPI(perdre_post=True, apparition_apres=1)
    with pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, chemins, preparer(chemins))
    assert 778 not in api.serveurs and lignes(chemins["creations"])[-1]["destruction_confirmee"]
    chemins = depot(tmp_path / "b")
    with pytest.raises(M.RattrapageARefaire, match="à refaire"):
        creer(FauxAPI(perdre_post=True, apparition_apres=10 ** 6), chemins, preparer(chemins))


def test_intention_exigee_avant_l_appel(tmp_path):   # n8
    chemins = depot(tmp_path)
    ratt = preparer(chemins)
    bloc = tmp_path / "bloc"
    bloc.write_text("un fichier à la place du dossier du journal\n")
    api = FauxAPI()
    with pytest.raises(OSError):
        creer(api, dict(chemins, creations=bloc / NOM_JOURNAL), ratt)
    assert not api.corps


NOM_JOURNAL = M.NOM_JOURNAL_CREATIONS


def test_un_seul_serveur_du_nom(tmp_path):   # n10
    chemins = depot(tmp_path)
    api = FauxAPI({5: {"name": H.NOM_MACHINE, "labels": {}}})
    with pytest.raises(GardeArret, match="existe déjà"):
        creer(api, chemins, preparer(chemins))
    assert not api.corps


def test_inventaire_de_controle_apres_detruire_pas():   # n12 : apparition tardive pendant la destruction
    def apparaitre(api):
        if not api.serveurs and not getattr(api, "deja", False):
            api.deja = True
            api.serveurs[2] = {"name": H.NOM_MACHINE, "labels": {}}
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, apres_delete=apparaitre)
    with pytest.raises(GardeArret, match="encore présents"):
        M.detruire_pas(client(api), "d1a", dormir=rien)


def test_pagination_des_etiquettes_fixes():   # n14
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, page_suivante=True)
    with pytest.raises(GardeArret, match="plus de 50"):
        M.detruire_pas(client(api), "d1a", dormir=rien)
    assert 1 in api.serveurs


def test_jeton_reutilise_refuse(tmp_path):   # n19
    chemins = depot(tmp_path)
    preparer(chemins)
    with pytest.raises(GardeArret, match="existe déjà"):
        M.ecrire_rattrapage(chemins["verse"], {"pas": "d1a", "etiquette": JETON})


# ---- procédure du poste local : préparer, pousser, heure limite, détacher, accès -----------------------------------------------

def test_preparer_sain(tmp_path):
    chemins = depot(tmp_path)
    r = json.loads(preparer(chemins).read_text())
    assert r["etiquette"] == JETON and r["etiquettes_fixes"] == FIXES and r["nom"] == H.NOM_MACHINE and r["go"] == GO
    assert [t["heure"] for t in r["taches_mere"]] == [(T0 + timedelta(hours=40)).isoformat(),
                                                       (T0 + timedelta(hours=64)).isoformat()]
    m = r["taches_mere"][0]["message"]
    for attendu in ("DELETE https://api.hetzner.cloud/v1/servers/<identifiant>", "label_selector=essai%3Dlean%2Cpas%3Dd1a",
                    "name=lean-outillage-d1a", "401 ou 403", "registres/arrets.md", "Ne jamais recréer", "d'un autre nom",
                    "2026-11-12 16:00 UTC"):
        assert attendu in m
    assert "detruire --pas d1a" in r["commandes_poste"]["par_pas"]


@pytest.mark.parametrize("limite_h,tache_h,motif", [(-1.0, 40.0, "déjà passée"), (2.0, 3.0, "moins de 2 heures"),
                                                     (2.0, 48.0, "plus de 47 heures")])
def test_preparer_refus(tmp_path, limite_h, tache_h, motif):
    with pytest.raises(GardeArret, match=motif):
        preparer(depot(tmp_path), limite_h, tache_h)


def test_preparer_go_invalide(tmp_path):
    chemins = depot(tmp_path)
    with pytest.raises(GardeArret, match="attendu"):
        M.preparer(go_id="GO-2026-11-10-14", chemins=chemins, heure_limite_creation=T0 + timedelta(hours=2),
                   heure_tache_mere=T0 + timedelta(hours=40), horloge=lambda: T0)


def test_lire_rattrapage_artefacts(tmp_path):
    chemins = depot(tmp_path)
    ratt = preparer(chemins)
    assert M.lire_rattrapage(ratt, GO)["heure_tache_mere"] == T0 + timedelta(hours=40)
    with pytest.raises(GardeArret, match="porte le GO"):
        M.lire_rattrapage(ratt, "GO-2026-11-10-14")
    d = json.loads(ratt.read_text())
    faux = chemins["verse"] / f"rattrapage-machine-d1a-{'b' * 12}-v1.json"
    faux.write_text(json.dumps(d))
    with pytest.raises(GardeArret, match="incohérents"):
        M.lire_rattrapage(faux)
    faux.write_text(json.dumps(dict(d, format="minuterie_v4")))
    with pytest.raises(GardeArret, match="preparer"):
        M.lire_rattrapage(faux)


def test_heure_limite_et_poussee_avant_tout_appel(tmp_path):
    chemins = depot(tmp_path)
    ratt = preparer(chemins)
    api = FauxAPI()
    with pytest.raises(GardeArret, match="heure limite de création passée"):
        creer(api, chemins, ratt, horloge=lambda: T0 + timedelta(hours=2, seconds=1))
    with pytest.raises(GardeArret, match="non poussé"):
        creer(api, chemins, ratt, verifier_pousse=lambda r, c: (False, "commit non poussé"))
    assert not api.appels and not chemins["creations"].exists()


def test_echeance_trop_proche_de_la_tache(tmp_path):   # défense en profondeur : fichier retouché à la main
    chemins = depot(tmp_path)
    ratt = preparer(chemins)
    d = json.loads(ratt.read_text())
    ratt.write_text(json.dumps(dict(d, heure_tache_mere=(T0 + timedelta(hours=2, minutes=30)).isoformat())))
    api = FauxAPI()
    with pytest.raises(GardeArret, match="moins d'une heure"):
        creer(api, chemins, ratt, horloge=lambda: T0 + timedelta(hours=1))
    assert not api.corps


def git(*args, cwd):
    return subprocess.run(["git", "-c", "user.email=essai@exemple.invalid", "-c", "user.name=essai", *args], cwd=cwd,
                          capture_output=True, text=True, check=True)


def test_fichier_pousse_git_reel(tmp_path):
    distant, clone = tmp_path / "distant.git", tmp_path / "clone"
    git("init", "--bare", "-q", str(distant), cwd=tmp_path)
    git("clone", "-q", str(distant), str(clone), cwd=tmp_path)
    f = clone / "docs" / "r.json"
    f.parent.mkdir()
    f.write_text("{}\n")
    assert M.fichier_pousse(clone, f) == (False, "fichier non suivi par git (git add, commit, push)")
    git("add", "docs/r.json", cwd=clone)
    git("commit", "-q", "-m", "r", cwd=clone)
    ok, motif = M.fichier_pousse(clone, f)
    assert not ok and "non poussé" in motif
    git("push", "-q", "origin", "HEAD:refs/heads/poste", cwd=clone)
    git("fetch", "-q", "origin", cwd=clone)
    ok, motif = M.fichier_pousse(clone, f)
    assert ok and "origin/poste" in motif
    f.write_text("{\"x\": 1}\n")
    assert M.fichier_pousse(clone, f) == (False, "fichier modifié depuis le dernier commit")
    assert M.fichier_pousse(clone, tmp_path / "ailleurs.json")[1] == "fichier hors du dépôt"


def test_detache(tmp_path, capsys):
    vus = {}

    class P:
        pid = 5151

    def popen(argv, **k):
        vus.update(argv=argv, **k)
        return P()
    sortie = tmp_path / "sortie-creation-v1.log"
    argv = ["creer-et-armer", "--go", GO, "--rattrapage", "r.json", "--type", "ccx33", "--lieu", "hel1", "--cle-ssh", "1",
            "--pare-feu", "2", "--journal", "j.jsonl", "--detache", "--sortie", str(sortie)]
    assert M.main(argv, popen=popen) == 0 and json.loads(capsys.readouterr().out)["pid"] == 5151
    enfant = vus["argv"]
    assert enfant[3] == M.MODULE and "--detache" not in enfant and "--sortie" not in enfant and vus["start_new_session"]
    assert not M.construire_analyseur().parse_args(enfant[4:]).detache and sortie.exists()
    assert M.main(argv, popen=popen) == 1   # sortie existante : refus (R12)
    assert M.main(argv[:-2], popen=popen) == 1   # --detache sans --sortie


def test_acces_creer_couper_supprimer(tmp_path):
    chemins = depot(tmp_path)
    prep = M.lire_rattrapage(preparer(chemins))
    api = FauxAPI()
    r = M.creer_acces(client(api), prep, CLE_PUB, "203.0.113.5", chemins["verse"], horloge=lambda: T0)
    cle, pf = api.cles[r["cle_ssh"]["id"]], api.pare_feux[r["pare_feu"]["id"]]
    assert cle["labels"] == {"essai": "lean", "pas": "d1a", "go": GO, "creation": JETON} == pf["labels"]
    assert cle["name"] == pf["name"] == f"{H.NOM_MACHINE}-{JETON[:12]}" and r["cle_ssh"]["empreinte"] == "aa:bb:cc"
    assert pf["rules"] == H.regles_installation("203.0.113.5")
    with pytest.raises(GardeArret, match="R12"):
        M.creer_acces(client(api), prep, CLE_PUB, "203.0.113.5", chemins["verse"])
    M.couper_acces(client(api), prep, chemins["verse"], "203.0.113.5")
    assert pf["rules"] == H.regles_coupure("203.0.113.5")
    api.serveurs[778] = {"name": H.NOM_MACHINE, "labels": {"creation": JETON}}
    with pytest.raises(GardeArret, match="existe encore"):
        M.supprimer_acces(client(api), prep, chemins["verse"])
    api.serveurs.clear()
    assert M.supprimer_acces(client(api), prep, chemins["verse"]) == {"pare_feu": "supprimé", "cle_ssh": "supprimé"}
    assert not api.cles and not api.pare_feux


def test_acces_artefacts(tmp_path):
    chemins = depot(tmp_path)
    prep = M.lire_rattrapage(preparer(chemins))
    api = FauxAPI()
    for cle in ("-----BEGIN OPENSSH PRIVATE KEY-----", CLE_PUB + "\n" + CLE_PUB, "AAAAC3Nza"):
        with pytest.raises(GardeArret, match="jamais une clé privée"):
            M.creer_acces(client(api), prep, cle, "203.0.113.5", chemins["verse"])
    for ip in ("203.0.113.0/24", "203.0.113.999", "poste"):
        with pytest.raises(GardeArret, match="IPv4"):
            M.creer_acces(client(api), prep, CLE_PUB, ip, chemins["verse"])
    assert not api.cles and not api.pare_feux
    M.creer_acces(client(api), prep, CLE_PUB, "203.0.113.5", chemins["verse"])
    next(iter(api.pare_feux.values()))["name"] = "pare-feu-d-un-autre"
    with pytest.raises(GardeArret, match="rien d'autre n'est touché"):
        M.supprimer_acces(client(api), prep, chemins["verse"])
    assert api.pare_feux and api.cles
