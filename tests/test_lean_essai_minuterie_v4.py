"""Essais R5 de la minuterie v4 et du client Hetzner v4 (CLC3-07 à CLC3-10, CLC3-11 k01, k02, k03, k04, k11, k13, k16, notes
4 et 5) : faux transport, aucun appel réseau, aucun serveur créé, aucun processus réel lancé."""
import json
import urllib.parse
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.lean_essai import hetzner_v3 as H3
from controle_ia.lean_essai import hetzner_v4 as H
from controle_ia.lean_essai import minuterie_v3 as M3
from controle_ia.lean_essai import minuterie_v4 as M

T0 = datetime(2026, 11, 11, 1, 0, tzinfo=timezone.utc)
JOUR = date(2026, 11, 11)
TYPES = [{"name": "ccx33", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.2260"}}]},
         {"name": "ccx63", "prices": [{"location": "hel1", "price_hourly": {"gross": "1.3942"}}]}]
FIXES = {"essai": "lean", "pas": "d1a"}


class FauxAPI:
    def __init__(self, serveurs=None, perdre_post=False, statut_post=201, apparition_apres=0):
        self.serveurs = dict(serveurs or {})   # id -> {"name", "labels"}
        self.perdre_post, self.statut_post, self.apparition_apres = perdre_post, statut_post, apparition_apres
        self.cache = {}
        self.recherches = 0
        self.appels, self.corps = [], []
        self.avant_post = None

    def __call__(self, methode, chemin, corps=None):
        self.appels.append((methode, chemin))
        if methode == "GET" and chemin.startswith("/servers/"):
            i = int(chemin.rsplit("/", 1)[1])
            if i not in self.serveurs:
                return 404, {"error": {"code": "not_found"}}
            s = self.serveurs[i]
            return 200, {"server": {"id": i, "name": s["name"], "created": "2026-11-11T01:00:30+00:00",
                                    "server_type": {"name": "ccx33"}, "datacenter": {"location": {"name": "hel1"}},
                                    "public_net": {"firewalls": [{"id": 2, "status": "applied"}]}}}
        if methode == "GET" and chemin.startswith("/servers?label_selector="):
            self.recherches += 1
            if self.recherches > self.apparition_apres:
                self.serveurs.update(self.cache)
                self.cache = {}
            paires = dict(x.split("=") for x in urllib.parse.unquote(chemin.split("=", 1)[1].split("&")[0]).split(","))
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()
                                     if all(s["labels"].get(k) == v for k, v in paires.items())], "meta": {"pagination": {}}}
        if methode == "GET" and chemin.startswith("/servers?"):
            return 200, {"servers": [{"id": i, "name": s["name"]} for i, s in self.serveurs.items()],
                         "meta": {"pagination": {}}}
        if methode == "DELETE" and chemin.startswith("/servers/"):
            self.serveurs.pop(int(chemin.rsplit("/", 1)[1]), None)
            return 200, {}
        if methode == "POST" and chemin == "/servers":
            if self.avant_post:
                self.avant_post()
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
            return 201, {"server": {"id": 778, "name": corps["name"], "created": "2026-11-11T01:00:30Z"}}
        if methode == "GET" and chemin.startswith("/server_types"):
            return 200, {"server_types": TYPES, "meta": {"pagination": {}}}
        if methode == "GET" and chemin == "/pricing":
            return 200, {"pricing": {"currency": "EUR", "primary_ips": [
                {"type": "ipv4", "prices": [{"location": "hel1", "price_hourly": {"gross": "0.0010"}}]}]}}
        if methode == "GET" and chemin.startswith("/firewalls/"):
            return 200, {"firewall": {"rules": H.regles_coupure("203.0.113.5"), "applied_to": []}}
        return 500, {"error": {"code": "inattendu"}}


def client(api):
    return H.ClientHetzner4(transport=api, dormir=lambda s: None)


def lignes(chemin):
    return [json.loads(x) for x in Path(chemin).read_text().splitlines() if x.strip()]


# ---- CLC3-07 (a) : detruire --pas d1a ---------------------------------------------------------------------------------------

def test_detruire_pas_par_etiquettes_et_nom():
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}, 2: {"name": H.NOM_MACHINE, "labels": {}},
                   3: {"name": "organisme-v66-course", "labels": {}}})
    r = M.detruire_pas(client(api), "d1a", dormir=lambda s: None)
    assert sorted(d["identifiant"] for d in r["detruits"]) == [1, 2] and 3 in api.serveurs
    assert M.detruire_pas(client(api), "d1a", dormir=lambda s: None)["message"] == "aucun serveur de l'essai"


def test_detruire_pas_refuse_un_autre_nom():
    api = FauxAPI({1: {"name": "autre", "labels": FIXES}})
    with pytest.raises(GardeArret, match="aucun n'est touché"):
        M.detruire_pas(client(api), "d1a", dormir=lambda s: None)
    assert not any(a[0] == "DELETE" for a in api.appels)


def test_cli_detruire_pas_sans_journal(capsys):
    api = FauxAPI({1: {"name": H.NOM_MACHINE, "labels": FIXES}})
    assert M.main(["detruire", "--pas", "d1a"], client=client(api), dormir=lambda s: None) == 0
    assert 1 not in api.serveurs


# ---- CLC3-07 (b) : minuterie détachée et son PID ------------------------------------------------------------------------------

def test_minuterie_detachee_et_pid(tmp_path):
    vus = {}

    class Processus:
        pid = 4242

    def popen(argv, **k):
        vus.update(argv=argv, **k)
        return Processus()
    r = M.lancer_minuterie_detachee(778, "d1a", T0, 1.25, 0.0, "a" * 32, tmp_path, popen=popen)
    assert vus["start_new_session"] is True and vus["argv"][3:5] == ["controle_ia.lean_essai.minuterie_v4", "veiller"]
    assert ["--identifiant", "778"] == vus["argv"][5:7] and "--depuis" in vus["argv"] and "D-1a" in vus["argv"]
    assert Path(r["fichier_pid"]).read_text().split() == ["4242", "778", "a" * 32]
    proc = tmp_path / "proc"
    (proc / "4242").mkdir(parents=True)
    (proc / "4242" / "cmdline").write_bytes(b"\0".join(x.encode() for x in vus["argv"]) + b"\0")
    assert M.verifier_minuterie(Path(r["fichier_pid"]), proc)["vivante"]
    (proc / "4242" / "cmdline").write_bytes(b"/usr/bin/sleep\x00100\x00")
    assert not M.verifier_minuterie(Path(r["fichier_pid"]), proc)["vivante"]
    (proc / "4242" / "cmdline").unlink()
    (proc / "4242").rmdir()
    assert M.verifier_minuterie(Path(r["fichier_pid"]), proc)["motif"].startswith("processus absent")


# ---- création : (c) procédure, (d) rattrapage, k01, CLC3-08, CLC3-10, note 5 ------------------------------------------------

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
    verse = tmp_path / "verse"
    verse.mkdir(exist_ok=True)
    return go, dep, tmp_path / "creations.jsonl", decisions, verse


def creer(api, go, dep, creations, decisions, verse, **k):
    d = dict(go_id="GO-2026-11-10-13", chemin_go=go, chemin_depenses=dep, journal_creations=creations,
             dossier_verse=verse, dossier_decisions=decisions, type_serveur="ccx33", image="ubuntu-24.04", lieu="hel1",
             cles_ssh=[1], pare_feux=[2], aujourdhui=JOUR, horloge=lambda: T0, dormir=lambda s: None, jeton="a" * 32,
             lancer=lambda ident, pas, depuis, taux, deja, jeton, dossier: {"pid": 4242, "depuis": depuis.isoformat()},
             fenetre_s=60.0)
    d.update(k)
    return M.creer_et_armer(client(api), **d)


def test_creation_saine_rattrapage_avant_l_appel(tmp_path):
    go, dep, creations, decisions, verse = fichiers(tmp_path)
    api = FauxAPI()
    vu = []
    api.avant_post = lambda: vu.append(sorted(p.name for p in verse.iterdir()))
    r = creer(api, go, dep, creations, decisions, verse)
    assert vu == [[f"rattrapage-machine-d1a-{'a' * 12}-v1.json"]]                       # (d) écrit avant l'appel
    ratt = json.loads((verse / vu[0][0]).read_text())
    assert ratt["etiquette"] == "a" * 32 and ratt["etiquettes_fixes"] == FIXES and "detruire --pas d1a" in ratt["commande_par_pas"]
    assert r["identifiant"] == 778 and r["depuis"] == T0.isoformat()                      # k01 : depuis l'intention
    assert r["minuterie"] == {"pid": 4242, "depuis": T0.isoformat()}
    assert "send_later" in r["procedure_mere"] and "2026-11-13 00:00 UTC" in r["procedure_mere"]   # (c) échéance − 1 h
    assert api.corps[0]["labels"]["essai"] == "lean" and api.corps[0]["labels"]["pas"] == "d1a"
    with pytest.raises(GardeArret, match="existe déjà"):
        M.ecrire_rattrapage(verse, {"pas": "d1a", "etiquette": "a" * 32})


def test_rattrapage_sur_une_fenetre(tmp_path):   # CLC3-08 : apparition tardive
    go, dep, creations, decisions, verse = fichiers(tmp_path)
    api = FauxAPI(perdre_post=True, apparition_apres=1)
    with pytest.raises(GardeArret, match="création incertaine.*1 serveur"):
        creer(api, go, dep, creations, decisions, verse)
    assert 778 not in api.serveurs and api.recherches >= 2
    assert lignes(creations)[-1]["destruction_confirmee"]


def test_rattrapage_rien_trouve_non_solde(tmp_path):
    go, dep, creations, decisions, verse = fichiers(tmp_path)
    api = FauxAPI(perdre_post=True, apparition_apres=10 ** 6)
    with pytest.raises(GardeArret, match="rien trouvé pendant 1 minutes.*à refaire"):
        creer(api, go, dep, creations, decisions, verse)
    assert not any(e.get("destruction_confirmee") or e.get("aucune_creation") for e in lignes(creations))


def test_creation_refusee_soldee(tmp_path):   # note 5
    go, dep, creations, decisions, verse = fichiers(tmp_path)
    with pytest.raises(GardeArret, match="aucun serveur créé"):
        creer(FauxAPI(statut_post=422), go, dep, creations, decisions, verse)
    assert lignes(creations)[-1]["aucune_creation"]
    assert M.cout_journal(creations, "GO-2026-11-10-13", T0 + timedelta(hours=30)) == pytest.approx(0.2270 * 1.25)


def test_taux_et_types(tmp_path):   # CLC3-10, k16
    assert M.taux_retenu() == 1.25 and M.taux_retenu(0.5) == 1.25 and M.taux_retenu(1.3) == 1.3
    with pytest.raises(GardeArret):
        M.taux_retenu(0.0)
    go, dep, creations, decisions, verse = fichiers(tmp_path)
    api = FauxAPI()
    with pytest.raises(GardeArret, match="hors de la liste du devis"):
        creer(api, go, dep, creations, decisions, verse, type_serveur="ccx63")
    with pytest.raises(GardeArret, match="hors de la liste du devis"):
        client(api).creer_serveur_etiquete("GO-2026-11-10-13", go, JOUR, "ccx63", "u", "hel1", [1], [2], "b" * 32)
    assert not api.corps


def test_rattrapage_detruit_tous_les_serveurs_de_l_etiquette():   # k02, note 4
    api = FauxAPI({5: {"name": H.NOM_MACHINE, "labels": {"creation": "c" * 32}},
                   6: {"name": H.NOM_MACHINE, "labels": {"creation": "c" * 32}}})
    r = M.rattraper_par_etiquette(client(api), "c" * 32, dormir=lambda s: None, fenetre_s=0.0)
    assert sorted(d["identifiant"] for d in r) == [5, 6] and not api.serveurs
    api = FauxAPI({7: {"name": "autre", "labels": {"creation": "d" * 32}}})
    with pytest.raises(GardeArret, match="autre nom"):
        M.rattraper_par_etiquette(client(api), "d" * 32, dormir=lambda s: None, fenetre_s=0.0)
    assert 7 in api.serveurs


# ---- CLC3-09 : journal au mieux ----------------------------------------------------------------------------------------------

class JournalPlein:
    def write(self, texte):
        raise OSError(28, "No space left on device")

    def flush(self):
        pass


def test_journal_en_echec_ne_tue_rien(capsys):
    M._ecrire(JournalPlein(), {"x": 1})
    assert "journal en échec" in capsys.readouterr().err
    api = FauxAPI({42: {"name": H.NOM_MACHINE, "labels": {}}})
    m = M.Machine(42, H.NOM_MACHINE, T0, 0.3, 65.0, 48.0)
    r = M.veiller(m, client(api), horloge=lambda: T0 + timedelta(hours=49), dormir=lambda s: None, journal=JournalPlein())
    assert r["detruit"] and 42 not in api.serveurs


# ---- CLC3-11 k03, k11, k13 ; k04 --------------------------------------------------------------------------------------------

def test_mot_de_lazar_hors_periode(tmp_path):   # k03
    go, *_rest = fichiers(tmp_path, lignes_go="| GO-2026-11-01-01 | 2026-11-01 | calcul | ancien | 5 USD | 2026-11-05 | Lazar "
                                              "| R |\n")
    with pytest.raises(GardeArret, match="hors de sa période"):
        M3.verifier_mot_de_lazar("GO-2026-11-01-01", go, tmp_path / "decisions", JOUR)


def test_declare_inferieur_au_registre(tmp_path):   # k11
    go, dep, creations, *_ = fichiers(tmp_path, "| 2026-11-11 | GO-2026-11-10-13 | D-1a | — | — | — | 20,00 | — | — |\n")
    with pytest.raises(GardeArret, match="inférieur au registre"):
        M.deja_depense_go(dep, "GO-2026-11-10-13", creations, 10.0, T0)
    assert M.deja_depense_go(dep, "GO-2026-11-10-13", creations, 25.0, T0)["retenu"] == 25.0


def jamais(secondes):
    raise AssertionError("la minuterie a démarré alors que la commande devait être refusée")


def test_cli_veiller_v4(tmp_path):   # k13 et --depuis
    api = FauxAPI({42: {"name": H.NOM_MACHINE, "labels": {}}})
    j = str(tmp_path / "j.jsonl")
    with pytest.raises(GardeArret, match="plus longue"):
        M.main(["veiller", "--identifiant", "42", "--echeance-h", "60", "--journal", j], client=client(api), dormir=jamais)
    with pytest.raises(GardeArret, match="plus tard que la création"):
        M.main(["veiller", "--identifiant", "42", "--depuis", "2026-11-11T02:00:00+00:00", "--journal", j],
               client=client(api), dormir=jamais)
    assert M.main(["veiller", "--identifiant", "42", "--depuis", "2026-11-11T00:59:00+00:00", "--journal", j],
                  client=client(api), dormir=lambda s: None, horloge=lambda: T0 + timedelta(hours=48)) == 0
    assert 42 not in api.serveurs   # échéance comptée depuis --depuis (00:59 + 48 h ≤ maintenant)


def test_coupure_applied_to(tmp_path):   # k04
    api = FauxAPI({777: {"name": H.NOM_MACHINE, "labels": {}}})
    with pytest.raises(GardeArret, match="non appliqué"):
        H3.verifier_coupure_nuage(client(api), 2, 777)


def test_detruire_pas_ne_prend_que_le_pas_demande():
    api = FauxAPI({9: {"name": "lean-outillage-d1b", "labels": {"essai": "lean", "pas": "d1b"}}})
    assert M.detruire_pas(client(api), "d1a", dormir=lambda s: None)["message"] == "aucun serveur de l'essai"
    assert 9 in api.serveurs
