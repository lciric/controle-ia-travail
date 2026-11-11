"""Essais R5 de la minuterie v6 (contre-lecture machine de la v5 `897b7438…`, R-2333) : CLC5-01, -03, -06 (m01, m09, m10, m11,
m15), -07, notes, et les essais v5 repris sur la v6. Faux transport : aucun appel réseau, aucun serveur. Les vrais processus
(minuteries avec un faux client dans l'enfant, `sleep`) sont arrêtés par leur PID (R10). Toute pause passe par un dormeur borné :
une boucle sans fin lève `BoucleSansFin` (hors `Exception`) au lieu de tourner ; les essais réels sont bornés en temps."""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v5 as H
from controle_ia.lean_essai import minuterie_v6 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)
GO = "GO-2026-11-10-13"
JETON = "a" * 32
FIXES = {"essai": "lean", "pas": "d1a"}
IP_POSTE = "203.0.113.5"          # plage de documentation : jamais une vraie adresse
TYPES = [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2390"}},
                                      {"location": "fsn1", "price_hourly": {"gross": "0.2990"}}]}]
PRIX_HEL1 = (0.2390 + 0.0010) * 1.25   # 0,30 USD/h
CLE_PUB = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExempleExempleExempleExempleExempleExemple utilisateur@machine-du-poste"
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
    reste = list(heures)
    return lambda: reste.pop(0) if len(reste) > 1 else reste[0]


class FauxAPI:
    def __init__(self, serveurs=None, *, forme="location", statut_post=201, perdre_post=False, apparition_apres=0,
                 statut_delete=200, pannes_get=0, page_suivante=False, apres_delete=None, statut_inventaire=200,
                 pannes_delete=0, statut_lecture=200, faux_404=0):
        self.serveurs = {i: dict(s) for i, s in (serveurs or {}).items()}
        self.forme, self.statut_post, self.perdre_post = forme, statut_post, perdre_post
        self.apparition_apres, self.statut_delete, self.pannes_get = apparition_apres, statut_delete, pannes_get
        self.page_suivante, self.apres_delete = page_suivante, apres_delete
        self.statut_inventaire, self.pannes_delete, self.statut_lecture = statut_inventaire, pannes_delete, statut_lecture
        self.faux_404 = faux_404
        self.cache, self.recherches, self.appels, self.corps = {}, 0, [], []
        self.cles, self.pare_feux, self.prochain = {}, {}, 500

    def _serveur(self, i):
        s = self.serveurs[i]
        d = {"id": i, "name": s["name"], "labels": s.get("labels", {}), "created": s.get("created", "2026-11-11T01:00:30+00:00"),
             "server_type": {"name": "ccx33"},
             "public_net": {"ipv4": {"ip": "198.51.100.7"}, "firewalls": [{"id": 2, "status": "applied"}]}}
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
                return self.statut_lecture, {"error": {"code": "forbidden"}}
            if self.faux_404 > 0:   # 404 erroné : le serveur reste à l'inventaire
                self.faux_404 -= 1
                return 404, {"error": {"code": "not_found"}}
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
        if methode == "GET" and chemin.startswith("/primary_ips"):
            return 200, {"primary_ips": [{"id": 31, "name": "primary_ip-31", "assignee_id": None},
                                         {"id": 32, "name": "primary_ip-32", "assignee_id": 778}], "meta": {"pagination": {}}}
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
                                      "rules": corps.get("rules", []), "fingerprint": "aa:bb:cc",
                                      "public_key": corps.get("public_key"), "applied_to": []}
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
    return chemins["verse"] / r["rattrapage"]


def armer(chemins, api, **k):
    """Préparation, accès créés sur le faux transport ; rend le fichier de rattrapage et son empreinte (mot « armée »)."""
    ratt = preparer(chemins, **k)
    M.creer_acces(client(api), M.lire_rattrapage(ratt), CLE_PUB, IP_POSTE, chemins["verse"], horloge=lambda: T0)
    return ratt, hashlib.sha256(ratt.read_bytes()).hexdigest()


def vivante(_mi, _dormir):
    return {"vivante": True, "garder": True, "motif": ""}


def creer(api, chemins, ratt, empreinte, **k):
    vus = k.pop("vus", {})

    def lancer(**kw):
        vus.update(kw)
        return {"pid": 4242, "fichier_pid": "f", "journal": "j"}
    d = dict(go_id=GO, chemins=chemins, rattrapage=ratt, empreinte_mere=empreinte, type_serveur="ccx33", image="ubuntu-24.04",
             lieu="hel1", horloge=lambda: T0, dormir=rien, lancer=lancer, controler=vivante,
             verifier_pousse=lambda racine, chemin: (True, "essai"), fenetre_s=60.0)
    d.update(k)
    return M.creer_et_armer(client(api), **d)


def pret(tmp_path, api=None, **k):
    """Dépôt jetable, préparation et accès : (api, chemins, rattrapage, empreinte)."""
    api = api or FauxAPI()
    chemins = depot(tmp_path)
    ratt, emp = armer(chemins, api, **k)
    return api, chemins, ratt, emp


def veiller_cli(api, tmp_path, *extra, heure=T0 + timedelta(hours=49), depuis=T0):
    j = tmp_path / f"veille-{len(list(tmp_path.glob('veille-*')))}.jsonl"
    horloge = heure if callable(heure) else (lambda: heure)
    code = M.main(["veiller", "--identifiant", "778", "--depuis", depuis.isoformat(), "--journal", str(j), *extra],
                  client=client(api), dormir=rien, horloge=horloge)
    return code, lignes(j)


SERVEUR = {778: {"name": H.NOM_MACHINE, "labels": dict(FIXES, creation=JETON, go=GO)}}
UNE_HEURE, ECHUE = T0 + timedelta(hours=1), T0 + timedelta(hours=49)

# ---- vrais processus : minuterie avec un faux client dans l'enfant ; lanceur retardé qui reproduit la course (CLC5-01) ------

ENFANT = r"""
import sys
from controle_ia.lean_essai import hetzner_v5 as H, minuterie_v6 as M
s = {"id": 778, "name": H.NOM_MACHINE, "labels": {}, "created": sys.argv[1 + sys.argv.index("--depuis")],
     "server_type": {"name": "ccx33"}, "location": {"name": "hel1"}}
def transport(methode, chemin, corps=None):
    if methode == "GET" and chemin == "/servers/778":
        return 200, {"server": s}
    if methode == "GET" and chemin.startswith("/servers?"):
        return 200, {"servers": [{"id": 778, "name": s["name"]}], "meta": {"pagination": {}}}
    if methode == "GET" and chemin.startswith("/server_types"):
        return 200, {"server_types": [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2390"}}]}],
                     "meta": {"pagination": {}}}
    if methode == "GET" and chemin == "/pricing":
        return 200, {"pricing": {"currency": "EUR", "primary_ips": [{"type": "ipv4", "prices": [
            {"location": "hel1", "price_hourly": {"gross": "0.0010"}}]}]}}
    return 500, {}
sys.exit(M.main(sys.argv[2:], client=H.ClientHetzner5(transport=transport)))
"""
# Lanceur retardé : pendant `retard` secondes, la ligne de commande du PID n'est pas celle de la minuterie (« autre
# processus »), puis `execv` garde le même PID et pose la vraie : la fenêtre de la course de l'`exec`, élargie et déterministe.
LANCEUR = "import json, os, sys, time; time.sleep(float(sys.argv[1])); a = json.loads(os.environ['ARGV_REEL']); os.execv(a[0], a)"


def popen_reel(vus, retard=0.0, code=ENFANT):
    def lancer(argv, **k):
        i = argv.index("-m")
        reel = argv[:i] + ["-c", code] + argv[i + 1:]
        if retard:
            k["env"] = dict(k["env"], ARGV_REEL=json.dumps(reel))
            p = subprocess.Popen([sys.executable, "-c", LANCEUR, str(retard)], **k)
        else:
            p = subprocess.Popen(reel, **k)
        vus.append(p)
        return p
    return lancer


def arreter(vus):
    for p in vus:
        if p.poll() is None:
            os.kill(p.pid, 15)   # par son PID (R10)
            p.wait(timeout=30)


def k_lancement(tmp_path, jeton=JETON):
    return dict(identifiant=778, pas="d1a", depuis=datetime.now(timezone.utc), echeance_h=2.0, taux=1.25, deja=0.0,
                jeton=jeton, go_id=GO, lieu="hel1", prix_usd_h=0.3, racine=tmp_path)


# ---- CLC5-01 : pas de « morte » sur une seule lecture négative ------------------------------------------------------------------

def test_survie_ne_conclut_pas_sur_une_lecture_negative(tmp_path):
    j = tmp_path / "j.jsonl"
    j.write_text(json.dumps({"detruire": False, "motif": "garder (cumul 0.30 USD)"}) + "\n")
    reponses = iter([{"vivante": False, "motif": "le PID désigne un autre processus"}] * 2 + [{"vivante": True, "motif": ""}] * 9)
    r = M.attendre_minuterie({"fichier_pid": "f", "journal": str(j)}, dormir=rien, verifier=lambda f: next(reponses))
    assert r == {"vivante": True, "garder": True, "motif": "", "lectures_negatives": 2}


def test_survie_jamais_vue_vivante_jusqu_au_delai(tmp_path):
    pauses = []
    r = M.attendre_minuterie({"fichier_pid": "f", "journal": str(tmp_path / "j")}, dormir=dormeur(pauses),
                             verifier=lambda f: {"vivante": False, "motif": "processus absent"}, delai_s=10, pas_s=2)
    assert not r["vivante"] and r["motif"].startswith("jamais vue vivante en 10 s") and sum(pauses) == 10
    assert r["lectures_negatives"] == 6


def test_survie_par_poll(tmp_path):
    j = tmp_path / "j.jsonl"

    class Vit:
        def poll(self):
            j.write_text(json.dumps({"detruire": False, "motif": "garder"}) + "\n")
            return None

    class Fini:
        def poll(self):
            return 2

    def jamais(_f):
        raise AssertionError("le PID ne doit pas être lu quand l'objet du processus est là")
    assert M.attendre_minuterie({"fichier_pid": "f", "journal": str(j)}, dormir=rien, verifier=jamais, processus=Vit())["garder"]
    mort = M.attendre_minuterie({"fichier_pid": "f", "journal": str(j)}, dormir=rien, verifier=jamais, processus=Fini())
    assert mort["vivante"] is False and mort["motif"] == "processus fini (code 2)"


def test_delai_de_survie_par_defaut(tmp_path):   # m09
    j = tmp_path / "j.jsonl"
    appels = []

    def verifier(_f):
        appels.append(1)
        if len(appels) == 5:
            j.write_text(json.dumps({"detruire": False, "motif": "garder"}) + "\n")
        return {"vivante": True, "motif": ""}
    assert M.DELAI_SURVIE_S >= 60 and M.attendre_minuterie({"fichier_pid": "f", "journal": str(j)}, dormir=rien,
                                                           verifier=verifier)["garder"]


def test_controle_par_defaut_utilise_poll(tmp_path):   # poll() vivant, PID illisible : armée, rien n'est détruit
    api, chemins, ratt, emp = pret(tmp_path)
    j = tmp_path / "j.jsonl"
    j.write_text(json.dumps({"detruire": False, "motif": "garder"}) + "\n")
    pid = tmp_path / "pid.txt"
    pid.write_text(f"{2 ** 22 + 7} 778 {JETON}\n")

    class Vit:
        def poll(self):
            return None
    r = creer(api, chemins, ratt, emp, controler=None,
              lancer=lambda **kw: {"pid": 2 ** 22 + 7, "fichier_pid": str(pid), "journal": str(j), "_processus": Vit()})
    assert r["survie"]["garder"] and 778 in api.serveurs and "_processus" not in r["minuterie"]


# ---- CLC5-06 : m01, m10, m11, m15 (m09 plus haut) ------------------------------------------------------------------------------

def test_veiller_absence_sur_deux_lectures():   # m10 : dans la boucle, un 404 seul n'arrête pas la garde
    api = FauxAPI(SERVEUR, faux_404=2)
    m = M.Machine(778, H.NOM_MACHINE, T0, 0.3, 65.0, 48.0)
    r = M.veiller(m, client(api), horloge=suite_d_heures(UNE_HEURE, UNE_HEURE, ECHUE), dormir=rien)
    assert r["detruit"] and not r.get("absent") and 778 not in api.serveurs
    assert ("DELETE", "/servers/778") in api.appels and api.faux_404 == 0


def test_lecture_refusee_401_bornee_a_trois(capsys):   # m01
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, statut_inventaire=401)
    assert M.main(["detruire", "--pas", "d1a"], client=client(api), dormir=rien) == 3
    assert sum(1 for a in api.appels if a[1].startswith("/servers?per_page")) == M.REFUS_DURABLES_MAX == 3
    assert "à la main" in capsys.readouterr().err


def test_lecture_403_n_est_pas_une_absence():   # m15
    with pytest.raises(H.RefusDurable):
        client(FauxAPI(SERVEUR, statut_lecture=403)).serveur(778)
    with pytest.raises(H.RefusDurable):
        client(FauxAPI(SERVEUR, statut_lecture=401)).serveur(778)


# ---- CLC5-03 : une seule préparation, même sans journal des créations -----------------------------------------------------------

def test_seconde_preparation_refusee(tmp_path):
    chemins = depot(tmp_path)
    preparer(chemins)
    with pytest.raises(GardeArret, match="une préparation existe déjà"):
        preparer(chemins, jeton="b" * 32)


def test_creation_refusee_si_autre_rattrapage(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    d = json.loads(ratt.read_text())
    (chemins["verse"] / f"rattrapage-machine-d1a-{'b' * 12}-v1.json").write_text(json.dumps(dict(d, etiquette="b" * 32)))
    api.appels.clear()
    assert not chemins["creations"].exists()
    with pytest.raises(GardeArret, match="CLC5-03"):
        creer(api, chemins, ratt, emp)
    assert not api.appels


# ---- CLC5-07 : aucune donnée du poste dans un fichier versé ou poussé ----------------------------------------------------------

def test_acces_sans_adresse_du_poste(tmp_path, capsys):
    api, chemins, ratt, emp = pret(tmp_path)
    fichier = next(chemins["verse"].glob("acces-machine-d1a-*-v1.json"))
    texte = fichier.read_text()
    d = json.loads(texte)
    assert IP_POSTE not in texte and "ip_poste" not in d and "regles" not in d and "machine-du-poste" not in texte
    cle = api.cles[d["cle_ssh"]["id"]]
    assert cle["public_key"] == " ".join(CLE_PUB.split()[:2])   # commentaire « utilisateur@machine » non envoyé
    assert api.pare_feux[d["pare_feu"]["id"]]["rules"] == H.regles_installation(IP_POSTE)   # chez Hetzner seulement
    capsys.readouterr()
    assert M.main(["acces-couper", "--depot", str(chemins["racine"]), "--rattrapage", str(ratt), "--ip-poste", IP_POSTE],
                  client=client(api)) == 0
    sortie = capsys.readouterr().out
    assert IP_POSTE not in sortie and json.loads(sortie)["regles_posees"] == 2


def test_verifier_coupure_masque(tmp_path, capsys):
    api = FauxAPI(SERVEUR)
    api.pare_feux[2] = {"id": 2, "name": "pf", "rules": H.regles_coupure(IP_POSTE),
                        "applied_to": [{"type": "server", "server": {"id": 778}}]}
    j = tmp_path / "coupure.jsonl"
    assert M.main(["verifier-coupure", "--serveur", "778", "--pare-feu", "2", "--journal", str(j)], client=client(api)) == 0
    sortie = capsys.readouterr().out
    for texte in (sortie, j.read_text()):
        assert IP_POSTE not in texte and "<adresse masquée>" in texte and "192.0.2.1/32" in texte


def test_sorties_sans_chemin_du_poste(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("HOME", str(tmp_path))
    api, chemins, ratt, emp = pret(tmp_path)
    verse = chemins["verse"]
    r = creer(api, chemins, ratt, emp, lancer=lambda **kw: {"pid": 4242, "fichier_pid": str(verse / "m-pid-v1.txt"),
                                                            "journal": str(verse / "m-journal-v1.jsonl")})
    assert str(tmp_path) not in json.dumps(r) and r["minuterie"]["journal"] == str(M.DOSSIER_RELATIF / "m-journal-v1.jsonl")
    code = M.main(["acces-creer", "--depot", str(chemins["racine"]), "--rattrapage", str(ratt), "--ip-poste", IP_POSTE,
                   "--cle-publique", str(tmp_path / "absente.pub")], client=client(api))
    err = capsys.readouterr().err
    assert code == 1 and "ERREUR INATTENDUE" in err and str(tmp_path) not in err and "absente.pub" in err


def git(*args, cwd):
    return subprocess.run(["git", "-c", "user.email=essai@exemple.invalid", "-c", "user.name=essai", *args], cwd=cwd,
                          capture_output=True, text=True, check=True, timeout=60)


def test_garde_poste_avant_commit(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("HOME", str(tmp_path / "Users" / "lazar"))
    clone = tmp_path / "clone-du-poste"
    clone.mkdir()
    git("init", "-q", cwd=clone)

    def garde(*extra):
        code = M.main(["garde-poste", "--ip-poste", IP_POSTE, "--depot", str(clone), *extra])
        sortie = capsys.readouterr().out
        assert IP_POSTE not in sortie and str(tmp_path) not in sortie
        return code, json.loads(sortie)
    (clone / "propre.json").write_text('{"identifiant": 778, "voisine": "203.0.113.50"}\n')
    git("add", "propre.json", cwd=clone)
    assert garde()[0] == 0
    for nom, contenu, nature in (("ip.json", f'{{"source": "{IP_POSTE}/32"}}', "adresse IPv4 du poste"),
                                 ("home.log", f"trace : {tmp_path / 'Users' / 'lazar'}/x.py", "dossier personnel"),
                                 ("clone.log", f"chemin : {clone.resolve()}/V/f.json", "chemin du clone")):
        (clone / nom).write_text(contenu + "\n")
        git("add", nom, cwd=clone)
        code, r = garde()
        assert code == 1 and [x[1] for x in r["trouves"]] == [nature]
        git("rm", "-q", "--cached", nom, cwd=clone)
    assert garde("--fichier", str(clone / "ip.json"))[0] == 1 and garde("--fichier", str(clone / "propre.json"))[0] == 0


# ---- notes : nom du pare-feu relu, branche distante lue, bornes du pilote ------------------------------------------------------

def test_couper_relit_le_nom(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    pf = next(iter(api.pare_feux.values()))
    pf["name"] = "pare-feu-renomme"
    avant = list(pf["rules"])
    with pytest.raises(GardeArret, match="aucune règle posée"):
        M.couper_acces(client(api), M.lire_rattrapage(ratt), chemins["verse"], IP_POSTE)
    assert pf["rules"] == avant


def test_fichier_pousse_par_ls_remote(tmp_path):
    distant, clone = tmp_path / "distant.git", tmp_path / "clone"
    git("init", "--bare", "-q", str(distant), cwd=tmp_path)
    git("clone", "-q", str(distant), str(clone), cwd=tmp_path)
    f = clone / "docs" / "r.json"
    f.parent.mkdir()
    f.write_text("{}\n")
    assert M.fichier_pousse(clone, f) == (False, "fichier non suivi par git (git add, commit, push)")
    git("add", "docs/r.json", cwd=clone)
    git("commit", "-q", "-m", "r", cwd=clone)
    assert M.fichier_pousse(clone, f) == (False, "branche sans amont (pousser avec `git push -u`)")
    git("push", "-q", "-u", "origin", "HEAD:refs/heads/poste", cwd=clone)
    ok, motif = M.fichier_pousse(clone, f)
    assert ok and "origin/poste" in motif and "ls-remote" in motif
    f.write_text("{\"x\": 1}\n")
    assert M.fichier_pousse(clone, f) == (False, "fichier modifié depuis le dernier commit")
    git("commit", "-q", "-am", "r2", cwd=clone)
    git("update-ref", "refs/remotes/origin/poste", "HEAD", cwd=clone)   # référence de suivi écrite à la main
    ok, motif = M.fichier_pousse(clone, f)
    assert not ok and "absent de la branche distante" in motif
    assert M.fichier_pousse(clone, tmp_path / "ailleurs.json")[1] == "fichier hors du dépôt"
    git("--git-dir", str(distant), "update-ref", "-d", "refs/heads/poste", cwd=tmp_path)   # branche retirée du distant
    git("reset", "-q", "--hard", "HEAD~1", cwd=clone)
    assert M.fichier_pousse(clone, f) == (False, "branche poste absente du dépôt distant (lu par git ls-remote)")


def test_pilote_bornes_ssh():
    pilote = M.racine_depot() / "scripts" / "lean_essai_d1a_v6" / "piloter_poste_v6.sh"
    texte = pilote.read_text(encoding="utf-8")
    appels = [x for x in texte.splitlines() if '"${S[@]}"' in x and not x.lstrip().startswith("#") and "S=(" not in x]
    assert len(appels) >= 10 and all('"${S[@]}" timeout ' in x for x in appels)
    assert "ConnectTimeout=" in texte and "ServerAliveInterval=" in texte and "ServerAliveCountMax=" in texte
    assert subprocess.run(["bash", "-n", str(pilote)], capture_output=True, timeout=30).returncode == 0


# ---- empreinte de la mère, objets du fichier d'accès, adresse du serveur, commandes bornées, tâches ----------------------------

def test_empreinte_mere(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    api.appels.clear()
    with pytest.raises(GardeArret, match="empreinte"):
        creer(api, chemins, ratt, "0" * 64)
    assert not api.appels
    assert creer(api, chemins, ratt, emp.upper())["identifiant"] == 778


def test_objets_du_fichier_d_acces(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    d = json.loads(next(chemins["verse"].glob("acces-machine-d1a-*-v1.json")).read_text())
    creer(api, chemins, ratt, emp)
    assert api.corps[-1]["ssh_keys"] == [d["cle_ssh"]["id"]] and api.corps[-1]["firewalls"] == [{"firewall": d["pare_feu"]["id"]}]
    api2, chemins2, ratt2, emp2 = pret(tmp_path / "b")
    next(chemins2["verse"].glob("acces-machine-d1a-*-v1.json")).unlink()
    with pytest.raises(GardeArret, match="fichier d'accès"):
        creer(api2, chemins2, ratt2, emp2)


def test_acces_non_pousse_refuse(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    api.appels.clear()
    with pytest.raises(GardeArret, match="acces-machine-d1a-.*non poussé"):
        creer(api, chemins, ratt, emp, verifier_pousse=lambda r, c: (not c.name.startswith("acces"), "non poussé"))
    assert not api.appels


def test_adresse_serveur(capsys):
    api = FauxAPI(SERVEUR)
    assert M.main(["adresse-serveur", "--identifiant", "778"], client=client(api)) == 0
    assert json.loads(capsys.readouterr().out)["ipv4"] == "198.51.100.7"
    assert M.main(["adresse-serveur", "--identifiant", "779"], client=client(api)) == 1
    api = FauxAPI({778: {"name": "autre", "labels": {}}})
    assert M.main(["adresse-serveur", "--identifiant", "778"], client=client(api)) == 1 and "R10" in capsys.readouterr().err


def test_commandes_bornees_code_5(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, pannes_delete=10 ** 6)
    pauses = []
    assert M.main(["detruire", "--identifiant", "1", "--duree-max-s", "60"], client=client(api), dormir=dormeur(pauses)) == 5
    assert sum(pauses) <= 60 and "15 minutes" in capsys.readouterr().err and 1 in api.serveurs
    pauses = []
    assert M.main(["inventaire", "--duree-max-s", "30"], client=client(FauxAPI(statut_inventaire=500)),
                  dormir=dormeur(pauses)) == 5 and sum(pauses) <= 30
    a = M.construire_analyseur().parse_args(["detruire", "--pas", "d1a"])
    assert a.duree_max_s == M.DUREE_MAX_COMMANDE_S == 480.0
    pauses = []
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, pannes_delete=2)
    assert M.main(["detruire", "--identifiant", "1"], client=client(api), dormir=dormeur(pauses)) == 0 and 1 not in api.serveurs


def test_taches_de_la_mere_et_ligne_d_etat(tmp_path):
    r = json.loads(preparer(depot(tmp_path)).read_text())
    H0 = T0 + timedelta(hours=40)
    assert [t["heure"] for t in r["taches_mere"]] == [H0.isoformat(), (H0 + timedelta(minutes=30)).isoformat(),
                                                       (H0 + timedelta(hours=24)).isoformat()]
    assert "send_later" in r["taches_mere"][0]["mode"] and all("session neuve" in t["mode"] for t in r["taches_mere"][1:])
    for t in r["taches_mere"]:
        m = t["message"]
        for attendu in ("printf 'Authorization: Bearer %s\\n' \"$HCLOUD_TOKEN\" | curl -sS --max-time 30 -H @-",
                        "label_selector=essai%3Dlean%2Cpas%3Dd1a", "name=lean-outillage-d1a", "erreur passagère",
                        "401 ou 403", "d'un autre nom", "registres/arrets.md", "en tâche jusqu'à",
                        "Ne jamais recréer de serveur.", "2026-11-12 16:00 UTC", f"creation={JETON}"):
            assert attendu in m, attendu
    assert all("pas d'autre mémoire" in t["message"] for t in r["taches_mere"][1:])
    assert "pas d'autre mémoire" not in r["taches_mere"][0]["message"]
    e = r["ligne_etat_mere"]
    assert "en tâche jusqu'à 2026-11-12 16:00 UTC" in e and f"creation={JETON}" in e and "Rappel de Lazar : 2026-11-12 18:00 UTC" in e
    assert r["rappel_lazar"] == (H0 + timedelta(hours=1)).isoformat()


# ---- essais v5 repris sur la v6 : CLC4-01 à CLC4-08 -----------------------------------------------------------------------------

def test_lieu_des_deux_formes_et_sans():
    assert H.lieu_du_serveur({"location": {"name": "hel1"}}) == ("hel1", "location")
    assert H.lieu_du_serveur({"datacenter": {"location": {"name": "fsn1"}}}) == ("fsn1", "datacenter.location")
    for s in ({}, None, {"location": 5}, {"datacenter": "x"}, {"location": {"name": "  "}}):
        assert H.lieu_du_serveur(s) == (None, "aucune")


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
    assert fait[0]["prix_usd_h"] == pytest.approx(PRIX_HEL1 if lieu else 65 / 48)


def test_demarrage_sous_retentatives(tmp_path):
    api = FauxAPI(SERVEUR, pannes_get=2)
    code, j = veiller_cli(api, tmp_path, heure=suite_d_heures(UNE_HEURE, UNE_HEURE, UNE_HEURE, ECHUE))
    assert code == 0 and [e["demarrage"] for e in j if "demarrage" in e][:3] == ["échec", "échec", "fait"]
    assert 778 not in api.serveurs


def test_demarrage_echeance_passee_sans_lecture(tmp_path):
    api = FauxAPI(SERVEUR, pannes_get=3)
    code, j = veiller_cli(api, tmp_path, "--prix-usd-h", "0.3")
    assert code == 0 and 778 not in api.serveurs
    assert any("échéance passée sans lecture" in str(e.get("demarrage")) for e in j)


def test_depuis_plus_tard_que_la_creation(tmp_path):
    api = FauxAPI(SERVEUR)
    code, _ = veiller_cli(api, tmp_path, heure=T0 + timedelta(hours=48, minutes=1), depuis=T0 + timedelta(hours=5))
    assert code == 0 and 778 not in api.serveurs


def test_echeance_plus_longue_refusee(tmp_path, capsys):
    api = FauxAPI(SERVEUR)
    code, _ = veiller_cli(api, tmp_path, "--echeance-h", "60")
    assert code == 1 and "plus longue" in capsys.readouterr().err and 778 in api.serveurs


def test_devis_reverifie_au_demarrage(tmp_path):   # n16
    api = FauxAPI(SERVEUR)
    code, j = veiller_cli(api, tmp_path, "--deja-depense-usd", "60", heure=UNE_HEURE)
    assert code == 0 and 778 not in api.serveurs and any("devis non tenu" in str(e.get("demarrage")) for e in j)


def test_plafond_retranche_du_deja_depense(tmp_path):   # n20
    api = FauxAPI(SERVEUR)
    code, j = veiller_cli(api, tmp_path, "--deja-depense-usd", "20", heure=suite_d_heures(UNE_HEURE, ECHUE))
    fait = [e for e in j if e.get("demarrage") == "fait"][0]
    assert code == 0 and fait["plafond_usd"] == pytest.approx(45.0) and 778 not in api.serveurs


def test_prix_le_plus_haut_retenu(tmp_path):
    code, j = veiller_cli(FauxAPI(SERVEUR), tmp_path, "--prix-usd-h", "0.1")
    assert code == 0 and [e for e in j if e.get("demarrage") == "fait"][0]["prix_usd_h"] == pytest.approx(PRIX_HEL1)


def test_minuterie_lecture_refusee_au_demarrage(tmp_path, capsys):
    api = FauxAPI(SERVEUR, statut_lecture=401)
    code, _ = veiller_cli(api, tmp_path)
    assert code == 3 and "à la main par l'identifiant 778" in capsys.readouterr().err and 778 in api.serveurs


def test_refus_de_nom_au_demarrage(tmp_path, capsys):
    code, _ = veiller_cli(FauxAPI({778: {"name": "autre", "labels": {}}}), tmp_path)
    assert code == 1 and "R10" in capsys.readouterr().err


def test_minuterie_detachee_arguments_complets(tmp_path):   # n9, n15
    vus = {}

    class P:
        pid = 4242

    def popen(argv, **k):
        vus.update(argv=argv, **k)
        return P()
    k = dict(identifiant=778, pas="d1a", depuis=T0, echeance_h=39.0, taux=1.3, deja=20.0, jeton=JETON, go_id=GO, lieu="hel1",
             prix_usd_h=0.31, dossier=tmp_path, racine=tmp_path, popen=popen)
    r = M.lancer_minuterie_detachee(**k)
    assert vus["start_new_session"] is True and vus["argv"][3] == M.MODULE and isinstance(r["_processus"], P)
    a = M.construire_analyseur().parse_args(vus["argv"][4:])
    assert (a.action, a.identifiant, a.taux_usd_eur, a.deja_depense_usd, a.echeance_h, a.lieu, a.prix_usd_h, a.go,
            a.etiquette, a.depot) == ("veiller", 778, 1.3, 20.0, 39.0, "hel1", 0.31, GO, JETON, str(tmp_path))
    with pytest.raises(GardeArret, match="R12"):
        M.lancer_minuterie_detachee(**k)


def test_creer_passe_deja_taux_et_echeance(tmp_path):
    api = FauxAPI()
    chemins = depot(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | — | — | — | 20,00 | — | — |\n")
    ratt, emp = armer(chemins, api, tache_h=30.0)
    vus = {}
    r = creer(api, chemins, ratt, emp, taux_declare=1.3, deja_declare=20.0, vus=vus)
    assert vus["deja"] == 20.0 and vus["taux"] == 1.3 and vus["echeance_h"] == pytest.approx(29.0)
    assert r["echeance"] == (T0 + timedelta(hours=29)).isoformat() and vus["prix_usd_h"] == pytest.approx(0.24 * 1.3)


@pytest.mark.parametrize("survie", [{"vivante": False, "garder": False, "motif": "processus fini (code 1)"},
                                    {"vivante": True, "garder": False, "motif": "aucune ligne « garder » en 120 s"}])
def test_minuterie_morte_ou_muette_detruit(tmp_path, survie):
    api, chemins, ratt, emp = pret(tmp_path)
    with pytest.raises(GardeArret, match="minuterie non armée.*détruit"):
        creer(api, chemins, ratt, emp, controler=lambda mi, d: survie)
    assert 778 not in api.serveurs and lignes(chemins["creations"])[-1]["destruction_confirmee"]


def test_controle_par_defaut_de_la_survie(tmp_path):   # sans contrôleur ni objet du processus : PID réel absent ⇒ détruit
    api, chemins, ratt, emp = pret(tmp_path)
    pid = tmp_path / "pid.txt"
    pid.write_text(f"{2 ** 22 + 7} 778 {JETON}\n")
    with pytest.raises(GardeArret, match="minuterie non armée.*jamais vue vivante"):
        creer(api, chemins, ratt, emp, controler=None,
              lancer=lambda **kw: {"pid": 2 ** 22 + 7, "fichier_pid": str(pid), "journal": str(tmp_path / "rien.jsonl")})
    assert 778 not in api.serveurs


def test_lancement_en_echec_detruit(tmp_path):   # n3
    api, chemins, ratt, emp = pret(tmp_path)

    def lancer(**kw):
        raise OSError("python introuvable")
    with pytest.raises(GardeArret, match="minuterie non armée"):
        creer(api, chemins, ratt, emp, lancer=lancer)
    assert 778 not in api.serveurs


def test_racine_deduite_ou_donnee(tmp_path):
    assert "/home/user" not in Path(M.__file__).read_text(encoding="utf-8")
    assert (M.racine_depot() / "src" / "controle_ia" / "lean_essai" / "minuterie_v6.py").is_file()
    with pytest.raises(GardeArret, match="--depot") as e:
        M.chemins_depot(tmp_path)
    assert str(tmp_path) not in str(e.value)
    chemins = depot(tmp_path)
    assert M.main(["preparer", "--depot", str(chemins["racine"]), "--go", GO, "--heure-limite-creation",
                   (T0 + timedelta(hours=2)).isoformat(), "--heure-tache-mere", (T0 + timedelta(hours=40)).isoformat()],
                  horloge=lambda: T0) == 0
    assert len(list(chemins["verse"].glob("rattrapage-machine-d1a-*-v1.json"))) == 1


ARGV = ["/usr/bin/python3", "-B", "-m", M.MODULE, "veiller", "--identifiant", "778", "--journal", "/x y/j.jsonl"]


def fichier_pid(tmp_path, pid=4242):
    f = tmp_path / "pid.txt"
    f.write_text(f"{pid} 778 {JETON}\n")
    return f


def faux_proc(tmp_path, argv=ARGV):
    proc = tmp_path / "proc"
    (proc / "self").mkdir(parents=True, exist_ok=True)
    (proc / "4242").mkdir(exist_ok=True)
    (proc / "4242" / "cmdline").write_bytes(b"\0".join(x.encode() for x in argv) + b"\0")
    return proc


def test_verifier_minuterie_linux_et_macos(tmp_path):
    proc, f = faux_proc(tmp_path), fichier_pid(tmp_path)
    assert M.verifier_minuterie(f, proc)["vivante"]
    faux_proc(tmp_path, ARGV[:6] + ["7781"])
    assert not M.verifier_minuterie(f, proc)["vivante"]
    (proc / "4242" / "cmdline").unlink()
    r = M.verifier_minuterie(f, proc)
    assert r["motif"].startswith("processus absent") and "jamais de relance" in r["motif"]
    sans = tmp_path / "pas-de-proc"
    assert M.verifier_minuterie(f, sans, existe=lambda p: "présent", ps=lambda p: " ".join(ARGV))["vivante"]
    assert not M.verifier_minuterie(f, sans, existe=lambda p: "présent", ps=lambda p: "/bin/zsh")["vivante"]
    assert not M.verifier_minuterie(f, sans, existe=lambda p: "autre utilisateur", ps=lambda p: " ".join(ARGV))["vivante"]


def test_kill_0_et_ps_reels():
    vus = []

    def executer(argv, **k):
        vus.append(argv)
        return subprocess.CompletedProcess(argv, 0, stdout="x\n", stderr="")
    assert M._ps(77, executer) == "x" and vus == [["ps", "-ww", "-p", "77", "-o", "command="]]
    assert M._existe(os.getpid()) == "présent" and M._existe(2 ** 22 + 7) == "absent"


def test_fraicheur_des_lignes_garder(tmp_path):
    proc, f = faux_proc(tmp_path), fichier_pid(tmp_path)
    j = tmp_path / "j.jsonl"
    j.write_text(json.dumps({"heure": T0.isoformat(), "detruire": False, "motif": "garder (cumul 0.30 USD)"}) + "\n")
    assert M.verifier_minuterie(f, proc, journal_minuterie=j, horloge=lambda: T0 + timedelta(minutes=2))["conforme"]
    r = M.verifier_minuterie(f, proc, journal_minuterie=j, horloge=lambda: T0 + timedelta(minutes=10))
    assert r["vivante"] and not r["conforme"] and "muette" in r["motif"] and "jamais de relance" in r["motif"]


def test_detruire_refus_durable_borne(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, statut_delete=403)
    pauses = []
    assert M.main(["detruire", "--pas", "d1a"], client=client(api), dormir=dormeur(pauses)) == 3
    assert "à la main" in capsys.readouterr().err and sum(1 for a in api.appels if a[0] == "DELETE") == 3


def test_echecs_passagers_ecrits_sans_journal(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}}, pannes_delete=2)
    assert M.main(["detruire", "--identifiant", "1"], client=client(api), dormir=rien) == 0 and 1 not in api.serveurs
    assert capsys.readouterr().err.count('"destruction": "échec"') == 2


def test_minuterie_refus_durable_a_l_echeance(tmp_path):
    code, j = veiller_cli(FauxAPI(SERVEUR, statut_delete=403), tmp_path)
    assert code == 3 and j[-1]["arret"] == "DestructionRefusee"


def test_bon_nom_detruit_autre_nom_nomme():   # CLC4-06, n1, n17
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}, 2: {"name": "lean-outillage-d1a-bis", "labels": FIXES},
                   3: {"name": H.NOM_MACHINE, "labels": {}}})
    with pytest.raises(GardeArret, match=r"2 serveur\(s\).*lean-outillage-d1a-bis.*NON touché"):
        M.detruire_pas(client(api), "d1a", dormir=rien)
    assert sorted(api.serveurs) == [2]


def test_inventaire_lecture_seule(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}, 3: {"name": H.NOM_MACHINE, "labels": {}},
                   4: {"name": "organisme-v66-course", "labels": {}}})
    assert M.main(["inventaire"], client=client(api), dormir=rien) == 0
    r = json.loads(capsys.readouterr().out)
    assert r["serveurs_de_l_essai"] == [[1, H.NOM_MACHINE], [3, H.NOM_MACHINE]]
    assert r["ips_primaires_non_attribuees"] == [[31, "primary_ip-31"]] and not any(a[0] != "GET" for a in api.appels)


def test_journal_solde(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    creer(api, chemins, ratt, emp)
    M.detruire_pas(client(api), "d1a", dormir=rien,
                   solder=M.fabrique_solder(chemins["creations"], lambda: T0 + timedelta(hours=2)))
    cout = [M.cout_journal(chemins["creations"], GO, T0 + timedelta(hours=h)) for h in (3, 48, 400)]
    assert cout[0] == cout[1] == cout[2] == pytest.approx(2 * PRIX_HEL1)
    j = tmp_path / "v.jsonl"
    assert M.main(["veiller", "--identifiant", "778", "--depuis", T0.isoformat(), "--go", GO, "--etiquette", "b" * 32,
                   "--journal", str(j), "--depot", str(chemins["racine"])], client=client(FauxAPI(SERVEUR)), dormir=rien,
                  horloge=lambda: ECHUE) == 0
    assert lignes(chemins["creations"])[-1]["etiquette"] == "b" * 32


def test_seconde_machine_refusee_sans_exception(tmp_path):   # n18
    api, chemins, ratt, emp = pret(tmp_path)
    creer(api, chemins, ratt, emp)
    api.serveurs.clear()
    with pytest.raises(GardeArret, match="sans exception"):
        creer(api, chemins, ratt, emp)
    chemins2 = depot(tmp_path / "b",
                     "| 2026-11-11 | GO-2026-11-10-13 | D-1a | Hetzner 12345678 | ccx33 | 3 | 1,00 | — | — |\n")
    with pytest.raises(GardeArret, match="sans exception"):
        preparer(chemins2)
    with pytest.raises(SystemExit):
        M.construire_analyseur().parse_args(["creer-et-armer", "--mot-de-lazar", GO])
    assert len(api.corps) == 1


def test_statut_500_incertain_detruit(tmp_path):   # n5
    api, chemins, ratt, emp = pret(tmp_path, FauxAPI(statut_post=500))
    with pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, chemins, ratt, emp)
    assert 778 not in api.serveurs


def test_refus_4xx_recherche_de_controle(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path, FauxAPI(statut_post=409))
    with pytest.raises(GardeArret, match="refusée par l'API.*trouvé"):
        creer(api, chemins, ratt, emp)
    assert 778 not in api.serveurs
    api, chemins, ratt, emp = pret(tmp_path / "b", FauxAPI(statut_post=422))
    with pytest.raises(GardeArret, match="aucun serveur créé"):
        creer(api, chemins, ratt, emp)
    assert lignes(chemins["creations"])[-1]["aucune_creation"]


def test_rattrapage_fenetre_et_rien_trouve(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path, FauxAPI(perdre_post=True, apparition_apres=1))
    with pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, chemins, ratt, emp)
    assert 778 not in api.serveurs
    api, chemins, ratt, emp = pret(tmp_path / "b", FauxAPI(perdre_post=True, apparition_apres=10 ** 6))
    with pytest.raises(M.RattrapageARefaire, match="à refaire"):
        creer(api, chemins, ratt, emp)


def test_intention_exigee_avant_l_appel(tmp_path):   # n8
    api, chemins, ratt, emp = pret(tmp_path)
    bloc = tmp_path / "bloc"
    bloc.write_text("un fichier à la place du dossier du journal\n")
    with pytest.raises(OSError):
        creer(api, dict(chemins, creations=bloc / M.NOM_JOURNAL_CREATIONS), ratt, emp)
    assert not api.corps


def test_un_seul_serveur_du_nom(tmp_path):   # n10
    api, chemins, ratt, emp = pret(tmp_path, FauxAPI({5: {"name": H.NOM_MACHINE, "labels": {}}}))
    with pytest.raises(GardeArret, match="existe déjà"):
        creer(api, chemins, ratt, emp)
    assert not api.corps


def test_inventaire_de_controle_apres_detruire_pas():   # n12
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


def test_jeton_reutilise_refuse(tmp_path):   # n19
    chemins = depot(tmp_path)
    preparer(chemins)
    with pytest.raises(GardeArret, match="existe déjà"):
        M.ecrire_rattrapage(chemins["verse"], {"pas": "d1a", "etiquette": JETON})


@pytest.mark.parametrize("limite_h,tache_h,motif", [(-1.0, 40.0, "déjà passée"), (2.0, 3.0, "moins de 2 heures"),
                                                     (2.0, 48.0, "plus de 47 heures")])
def test_preparer_refus(tmp_path, limite_h, tache_h, motif):
    with pytest.raises(GardeArret, match=motif):
        preparer(depot(tmp_path), limite_h, tache_h)


def test_lire_rattrapage_artefacts(tmp_path):
    chemins = depot(tmp_path)
    ratt = preparer(chemins)
    assert M.lire_rattrapage(ratt, GO)["heure_tache_mere"] == T0 + timedelta(hours=40)
    with pytest.raises(GardeArret, match="porte le GO"):
        M.lire_rattrapage(ratt, "GO-2026-11-10-14")
    d = json.loads(ratt.read_text())
    faux = tmp_path / f"rattrapage-machine-d1a-{'b' * 12}-v1.json"
    faux.write_text(json.dumps(d))
    with pytest.raises(GardeArret, match="incohérents"):
        M.lire_rattrapage(faux)
    faux.write_text(json.dumps(dict(d, format="minuterie_v5")))
    with pytest.raises(GardeArret, match="minuterie_v6 preparer"):
        M.lire_rattrapage(faux)


def test_heure_limite_et_poussee_avant_tout_appel(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    api.appels.clear()
    with pytest.raises(GardeArret, match="heure limite de création passée"):
        creer(api, chemins, ratt, emp, horloge=lambda: T0 + timedelta(hours=2, seconds=1))
    with pytest.raises(GardeArret, match="non poussé"):
        creer(api, chemins, ratt, emp, verifier_pousse=lambda r, c: (False, "commit non poussé"))
    assert not api.appels and not chemins["creations"].exists()


def test_echeance_trop_proche_de_la_tache(tmp_path):   # défense en profondeur : fichier retouché à la main
    api, chemins, ratt, emp = pret(tmp_path)
    d = json.loads(ratt.read_text())
    ratt.write_text(json.dumps(dict(d, heure_tache_mere=(T0 + timedelta(hours=2, minutes=30)).isoformat())))
    with pytest.raises(GardeArret, match="moins d'une heure"):
        creer(api, chemins, ratt, hashlib.sha256(ratt.read_bytes()).hexdigest(), horloge=lambda: T0 + timedelta(hours=1))
    assert not api.corps


def test_detache(tmp_path, capsys):
    vus = {}

    class P:
        pid = 5151

    def popen(argv, **k):
        vus.update(argv=argv, **k)
        return P()
    sortie = tmp_path / "sortie-creation-v1.log"
    argv = ["creer-et-armer", "--go", GO, "--rattrapage", "r.json", "--empreinte-mere", "0" * 64, "--type", "ccx33",
            "--lieu", "hel1", "--journal", "j.jsonl", "--detache", "--sortie", str(sortie)]
    assert M.main(argv, popen=popen) == 0
    r = json.loads(capsys.readouterr().out)
    assert r["pid"] == 5151 and "argv" not in r and str(tmp_path) not in json.dumps(r)
    enfant = vus["argv"]
    assert enfant[3] == M.MODULE and "--detache" not in enfant and "--sortie" not in enfant and vus["start_new_session"]
    assert not M.construire_analyseur().parse_args(enfant[4:]).detache and sortie.exists()
    assert M.main(argv, popen=popen) == 1 and "sortie-creation-v1.log existe déjà (R12)" in capsys.readouterr().err
    assert M.main(argv[:-2], popen=popen) == 1 and "--detache exige --sortie" in capsys.readouterr().err


def test_acces_creer_couper_supprimer(tmp_path):
    api, chemins, ratt, emp = pret(tmp_path)
    prep = M.lire_rattrapage(ratt)
    d = json.loads(next(chemins["verse"].glob("acces-machine-d1a-*-v1.json")).read_text())
    cle, pf = api.cles[d["cle_ssh"]["id"]], api.pare_feux[d["pare_feu"]["id"]]
    assert cle["labels"] == {"essai": "lean", "pas": "d1a", "go": GO, "creation": JETON} == pf["labels"]
    with pytest.raises(GardeArret, match="R12"):
        M.creer_acces(client(api), prep, CLE_PUB, IP_POSTE, chemins["verse"])
    M.couper_acces(client(api), prep, chemins["verse"], IP_POSTE)
    assert pf["rules"] == H.regles_coupure(IP_POSTE)
    api.serveurs[778] = {"name": H.NOM_MACHINE, "labels": {"creation": JETON}}
    with pytest.raises(GardeArret, match="existe encore"):
        M.supprimer_acces(client(api), prep, chemins["verse"])
    api.serveurs.clear()
    pf["name"] = "pare-feu-d-un-autre"
    with pytest.raises(GardeArret, match="rien d'autre n'est touché"):
        M.supprimer_acces(client(api), prep, chemins["verse"])
    assert d["pare_feu"]["id"] in api.pare_feux and d["cle_ssh"]["id"] in api.cles
    pf["name"] = d["nom"]
    assert M.supprimer_acces(client(api), prep, chemins["verse"]) == {"pare_feu": "supprimé", "cle_ssh": "supprimé"}
    assert not api.cles and not api.pare_feux


def test_acces_artefacts(tmp_path):
    chemins = depot(tmp_path)
    prep = M.lire_rattrapage(preparer(chemins))
    api = FauxAPI()
    for cle in ("-----BEGIN OPENSSH PRIVATE KEY-----", CLE_PUB + "\n" + CLE_PUB, "AAAAC3Nza", "ssh-ed25519"):
        with pytest.raises(GardeArret, match="clé"):
            M.creer_acces(client(api), prep, cle, IP_POSTE, chemins["verse"])
    for ip in ("203.0.113.0/24", "203.0.113.999", "poste"):
        with pytest.raises(GardeArret, match="IPv4"):
            M.creer_acces(client(api), prep, CLE_PUB, ip, chemins["verse"])
    assert not api.cles and not api.pare_feux


# ---- vrais processus (CLC5-01, m11), en fin de fichier ----------------------------------------------------------------------

def test_course_reproduite_et_sans_destruction(tmp_path):
    """La course est reproduite (première lecture du PID négative, comme les 6 sur 138 du lecteur) ; elle ne fait plus conclure
    « morte », ni par les lectures du PID, ni par `poll()`."""
    vus, lectures = [], []

    def verifier(f):
        r = M.verifier_minuterie(f)
        lectures.append(r["vivante"])
        return r
    try:
        mi = M.lancer_minuterie_detachee(dossier=tmp_path / "a", popen=popen_reel(vus, retard=0.4), **k_lancement(tmp_path))
        r = M.attendre_minuterie(mi, verifier=verifier, delai_s=30.0, pas_s=0.05, dormir=time.sleep)
        assert lectures[0] is False and r["vivante"] and r["garder"] and r["lectures_negatives"] >= 1
        mi = M.lancer_minuterie_detachee(dossier=tmp_path / "b", popen=popen_reel(vus, retard=0.4), **k_lancement(tmp_path))
        r = M.attendre_minuterie(mi, processus=mi["_processus"], delai_s=30.0, pas_s=0.05, dormir=time.sleep)
        assert r["vivante"] and r["garder"]
    finally:
        arreter(vus)


def test_creation_avec_course_ne_detruit_pas(tmp_path):
    """Vrai chemin de `creer_et_armer` (contrôle par défaut, `poll()`), vraie minuterie retardée : le serveur reste."""
    api, chemins, ratt, emp = pret(tmp_path)
    vus = []
    try:
        r = creer(api, chemins, ratt, emp, controler=None, dormir=time.sleep,
                  lancer=lambda **kw: M.lancer_minuterie_detachee(popen=popen_reel(vus, retard=0.4), **kw))
        assert 778 in api.serveurs and r["survie"]["garder"] and r["minuterie"]["pid"] == vus[0].pid
        assert r["minuterie"]["journal"].startswith(str(M.DOSSIER_RELATIF))
    finally:
        arreter(vus)


def test_lancements_reels_en_serie(tmp_path):
    """25 vrais lancements sans retard, contrôle par les lectures du PID : aucun « morte » à tort."""
    vus, negatifs = [], 0
    try:
        for n in range(25):
            jeton = f"{n:02x}" * 16
            mi = M.lancer_minuterie_detachee(dossier=tmp_path / f"s{n}", popen=popen_reel(vus),
                                             **k_lancement(tmp_path, jeton))
            r = M.attendre_minuterie(mi, delai_s=20.0, pas_s=0.02, dormir=time.sleep)
            assert r["vivante"] and r["garder"], r
            negatifs += r["lectures_negatives"]
            arreter(vus[-1:])
    finally:
        arreter(vus)
    print(f"lectures négatives du PID sur 25 lancements : {negatifs} (sans conclusion « morte »)")


def test_minuterie_reelle_detachee(tmp_path):
    vus = []
    try:
        mi = M.lancer_minuterie_detachee(dossier=tmp_path / "vivante", popen=popen_reel(vus), **k_lancement(tmp_path))
        assert os.getsid(vus[0].pid) == vus[0].pid != os.getsid(0)   # session à elle
        survie = M.attendre_minuterie(mi, delai_s=30.0, pas_s=0.2, dormir=time.sleep, processus=mi["_processus"])
        assert survie["vivante"] and survie["garder"]
        r = M.verifier_minuterie(Path(mi["fichier_pid"]), journal_minuterie=Path(mi["journal"]))
        assert r["conforme"] and r["pid"] == vus[0].pid
        morte = M.lancer_minuterie_detachee(dossier=tmp_path / "morte", popen=popen_reel(vus, code="import sys; sys.exit(2)"),
                                            **k_lancement(tmp_path))
        vus[1].wait(timeout=30)
        assert not M.attendre_minuterie(morte, delai_s=2.0, pas_s=0.5, dormir=time.sleep)["vivante"]
        assert M.attendre_minuterie(morte, processus=morte["_processus"], dormir=rien)["motif"] == "processus fini (code 2)"
    finally:
        arreter(vus)
    assert not M.verifier_minuterie(Path(mi["fichier_pid"]))["vivante"]


def test_branche_macos_avec_vrai_ps(tmp_path):   # m11 : `kill -0` et `ps -ww` réels, sans /proc
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)", M.MODULE, "veiller", "--identifiant", "778"])
    try:
        f = tmp_path / "pid.txt"
        f.write_text(f"{p.pid} 778 {JETON}\n")
        r = M.verifier_minuterie(f, tmp_path / "pas-de-proc")
        assert r["vivante"] and r["methode"] == "kill -0 et ps -p"
    finally:
        os.kill(p.pid, 15)
        p.wait(timeout=30)
    assert M.verifier_minuterie(f, tmp_path / "pas-de-proc")["motif"].startswith("processus absent")
