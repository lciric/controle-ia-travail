"""Essais de la sonde d'Astra commune aux deux courses (`scripts/sonde_astra_courses_v1.py`) et diagnostic, hors ligne, du
défaut de la sonde (réserve du relais jeté, code 4 de la commande).

Le « relais factice » est le **code du relais épinglé lui-même** (`relais_kimi_v4.py`, `67f36951…`) : `Compteur`, `Bareme` et
le gestionnaire HTTP de `fabriquer_gestionnaire` sont importés du fichier épinglé et servis dans ce processus, sur la boucle
locale, avec une clé factice, devant un faux amont local qui rend un flux SSE au format OpenAI. La règle de réserve et de
plafond est donc celle du relais, par construction (rien n'est recopié). La commande d'Astra est extraite de
`refs/remotes/origin/main` (`986cf71e…`) dans le dossier temporaire de l'essai. Aucun appel réel, aucune clé, aucun réseau
hors de la boucle locale."""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
CHEMIN_RELAIS = RACINE / "docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py"
CHEMIN_COMMANDE_MAIN = "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"
EMPREINTE_RELAIS = "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"
EMPREINTE_COMMANDE = "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"


def _charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


assert hashlib.sha256(CHEMIN_RELAIS.read_bytes()).hexdigest() == EMPREINTE_RELAIS
R = _charger("relais_kimi_v4_pour_sonde_commune", CHEMIN_RELAIS)
S = _charger("sonde_astra_courses_v1", RACINE / "scripts" / "sonde_astra_courses_v1.py")
ARGS_SONDE_V2 = ["--max-sortie-jetons", "4096", "--sortie-min-jetons", "16", "--delai-s", "120"]  # ceux de la sonde v2
CONSIGNE = "Réponds par le seul mot : prêt."


def _commande_de_main():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{CHEMIN_COMMANDE_MAIN}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == EMPREINTE_COMMANDE else None


OCTETS_COMMANDE = _commande_de_main()
pytestmark = pytest.mark.skipif(OCTETS_COMMANDE is None, reason="commande d'Astra absente de refs/remotes/origin/main (fetch ciblé requis)")


class FauxAmont:
    """Faux amont compatible OpenAI, en flux SSE : compte les requêtes reçues et garde le dernier corps."""

    def __init__(self, completion_tokens=40, modele="gpt-6-astra"):
        self.recues, self.corps = 0, None
        amont = self

        class H(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                amont.corps = json.loads(self.rfile.read(n))
                amont.recues += 1
                morceaux = [{"id": "x", "model": modele, "choices": [{"index": 0, "delta": {"content": "prêt"}}]},
                            {"id": "x", "model": modele, "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]},
                            {"id": "x", "model": modele, "choices": [],
                             "usage": {"prompt_tokens": 18, "completion_tokens": completion_tokens,
                                       "total_tokens": 18 + completion_tokens}}]
                corps = b"".join(b"data: " + json.dumps(m).encode() + b"\n\n" for m in morceaux) + b"data: [DONE]\n\n"
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Content-Length", str(len(corps)))
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(corps)

            def log_message(self, *a):
                pass
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"


class RelaisFactice:
    """Le gestionnaire du relais épinglé, servi ici avec une clé factice devant le faux amont."""

    def __init__(self, amont: FauxAmont, reserve=R.RESERVE_PAR_APPEL_DEFAUT, plafond=0.05, max_appels=1, prix=(10, 50, 1)):
        self.bareme = R.Bareme(prix[0], prix[1], prix[2], R.MAX_JETONS_SORTIE_PIRE_CAS_DEFAUT)
        self.compteur = R.Compteur(plafond, reserve, max_appels, R.MAX_OCTETS_CORPS_DEFAUT)
        g = R.fabriquer_gestionnaire("cle-factice-essai", amont.url, ("gpt-6-astra",), self.bareme, self.compteur, None,
                                     threading.Lock(), None, None, 60.0, "VARIABLE_FACTICE_ESSAI", 30.0)
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), g)
        self.serveur.daemon_threads = True
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.port = self.serveur.server_address[1]
        self.url = f"http://127.0.0.1:{self.port}"

    def fermer(self):
        self.serveur.shutdown()


@pytest.fixture
def pieces(tmp_path):
    cmd = tmp_path / "commande_astra_v1.py"
    cmd.write_bytes(OCTETS_COMMANDE)
    relais = tmp_path / "relais_kimi_v4.py"
    relais.write_bytes(CHEMIN_RELAIS.read_bytes())
    return {"commande": cmd, "relais": relais, "tmp": tmp_path}


def commande(cmd: Path, url: str, env_plus: dict, args: list) -> tuple:
    env = {"PATH": "/usr/bin:/bin", "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": "gpt-6-astra", **env_plus}
    p = subprocess.run([sys.executable, "-I", "-B", str(cmd), "--url-relais", url, "--modele", "gpt-6-astra", *args],
                       input=CONSIGNE.encode(), env=env, capture_output=True, timeout=60)
    return p.returncode, json.loads(p.stdout.decode().splitlines()[-1])


# --- 1. diagnostic reproduit hors ligne -------------------------------------------------------------------------------------


def test_diagnostic_relais_jete_sans_reserve_reglee_refuse_en_402(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont)                                  # réserve par défaut du relais épinglé : 0,40 USD
    try:
        assert relais.compteur.reserve_min == 0.40 > relais.compteur.plafond == 0.05
        code, ligne = commande(pieces["commande"], relais.url, {"PLAFOND_SESSION_USD": "0.05"}, ARGS_SONDE_V2)
        assert code == 3 and ligne["erreur"].startswith("HTTP 402") and ligne["envoye"] is False
        assert amont.recues == 0 and relais.compteur.appels == 0 and relais.compteur.refus == 1
        assert ligne["pire_cas_usd"] <= 0.05                       # la commande, elle, tenait sous le plafond
    finally:
        relais.fermer()


def test_diagnostic_commande_code_4_sous_le_plafond_par_defaut(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        code, ligne = commande(pieces["commande"], relais.url, {"PLAFOND_SESSION_USD": "0.05"}, [])   # sorties par défaut
        assert code == 4 and ligne["envoye"] is False and "pire cas au-dessus du plafond" in ligne["erreur"]
        code, ligne = commande(pieces["commande"], relais.url, {}, ARGS_SONDE_V2)                    # plafond de session absent
        assert code == 2 and "PLAFOND_SESSION_USD" in ligne["erreur"]
        assert amont.recues == 0 and relais.compteur.appels == 0
    finally:
        relais.fermer()


@pytest.mark.parametrize("sortie_rendue", [40, None])           # réponse triviale ; puis sortie au maximum demandé
def test_configuration_qui_passe_pire_cas_sous_005(pieces, sortie_rendue):
    amont = FauxAmont(completion_tokens=sortie_rendue or 0)
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        if sortie_rendue is None:                                  # pire réel : l'amont facture tout le max demandé
            code0, l0 = commande(pieces["commande"], relais.url, {"PLAFOND_SESSION_USD": "0.05"}, ARGS_SONDE_V2)
            relais.fermer()
            amont = FauxAmont(completion_tokens=l0["max_completion_tokens"])
            relais = RelaisFactice(amont, reserve=0.01)
        code, ligne = commande(pieces["commande"], relais.url, {"PLAFOND_SESSION_USD": "0.05"}, ARGS_SONDE_V2)
        assert code == 0, ligne
        n = ligne["max_completion_tokens"]
        assert 700 <= n <= 4096 and amont.corps["max_completion_tokens"] == n      # ≈ 768 : pas de troncature triviale
        corps = json.dumps({"model": "gpt-6-astra", "messages": [{"role": "user", "content": CONSIGNE}],
                            "max_completion_tokens": n}, ensure_ascii=False).encode()
        pire_relais = relais.bareme.pire_cas(len(corps), json.loads(corps))
        assert abs(pire_relais - ligne["pire_cas_usd"]) < 1e-6 and pire_relais <= 0.05      # même formule, même octets
        assert max(relais.compteur.reserve_min, pire_relais) <= relais.compteur.plafond     # admis par le compteur
        assert relais.compteur.appels == 1 and relais.compteur.refus == 0
        assert relais.compteur.depense <= 0.05 + 1e-12 and ligne["cout_usd"] <= 0.05
    finally:
        relais.fermer()


# --- 2. sonde commune ---------------------------------------------------------------------------------------------------


def _sonder(pieces, relais: RelaisFactice, amont: FauxAmont, url=None, nom="a"):
    t = pieces["tmp"]
    cmdline = [sys.executable, "-I", "-B", str(pieces["relais"]), "--port", str(relais.port)]
    return S.sonder(pieces["commande"], url or relais.url, os.getpid(), t / f"sonde-{nom}.json", t / f"sonde-v2-{nom}.json",
                    lire_etat=S.lire_etat_local, lire_cmd=lambda pid: cmdline, amont=amont.url,
                    horodatage=lambda: "2026-11-18T11:00:00Z")


def _scelle(p: Path) -> bool:
    return Path(str(p) + ".sha256").read_text().split()[0] == hashlib.sha256(p.read_bytes()).hexdigest()


def test_sonde_cas_sain_passe_et_rapport_scelle(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        assert _sonder(pieces, relais, amont) == 0
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert _scelle(pieces["tmp"] / "sonde-a.json") and _scelle(pieces["tmp"] / "sonde-v2-a.json")
        assert o["ok"] is True and o["jour"] == "2026-11-18" and o["appel_envoye"] is True and o["motif"] is None
        assert o["rapport_v2"]["ok"] is True and o["rapport_v2"]["code_commande"] == 0
        assert 0 < o["cout_usd"] <= 0.05 and 0 < o["depense_relais_usd"] <= 0.05
        assert o["commande"]["sha256"] == EMPREINTE_COMMANDE and o["relais_jete"]["programme_sha256"] == EMPREINTE_RELAIS
        assert o["relais_jete"]["port"] not in S.PORTS_DES_COURSES and o["relais_jete"]["reserve_par_appel_usd"] == 0.01
        v2 = json.loads((pieces["tmp"] / "sonde-v2-a.json").read_text())
        assert v2["version"] == "sonde_astra_affinage_v2" and v2["ok"] is True       # format lu par le lanceur de l'affinage v6
        assert amont.recues == 1
    finally:
        relais.fermer()


def test_sonde_artefact_reserve_trop_haute_echec_rapporte_sans_appel(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont)                                  # réserve par défaut 0,40 > plafond 0,05
    try:
        assert _sonder(pieces, relais, amont) == 1
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert _scelle(pieces["tmp"] / "sonde-a.json")
        assert o["ok"] is False and o["echec_de_configuration"] is True and o["appel_envoye"] is False
        assert any("402 certain" in m for m in o["motif"])
        assert not (pieces["tmp"] / "sonde-v2-a.json").exists()    # le chemin du rapport v2 reste libre
        assert amont.recues == 0 and relais.compteur.appels == 0 and relais.compteur.refus == 0
    finally:
        relais.fermer()


@pytest.mark.parametrize("defaut", ["plafond", "prix", "max_appels"])
def test_sonde_autres_defauts_de_configuration_rapportes(pieces, defaut):
    amont = FauxAmont()
    kw = {"plafond": {"plafond": 0.10}, "prix": {"prix": (5, 50, 1)}, "max_appels": {"max_appels": 3}}[defaut]
    relais = RelaisFactice(amont, **dict({"reserve": 0.01}, **kw))
    try:
        assert _sonder(pieces, relais, amont) == 1
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert o["echec_de_configuration"] is True and amont.recues == 0
    finally:
        relais.fermer()


def test_sonde_refuse_un_relais_non_neuf_ou_un_port_de_course(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01, max_appels=2)
    try:
        code, _ = commande(pieces["commande"], relais.url, {"PLAFOND_SESSION_USD": "0.05"}, ARGS_SONDE_V2)
        assert code == 0 and relais.compteur.appels == 1           # relais déjà servi : plus neuf
        with pytest.raises(S.Refus, match="non neuf"):
            _sonder(pieces, relais, amont)
        for port in (8790, 8787, 8792):                            # relais d'une course : refus avant toute lecture
            with pytest.raises(S.Refus, match="port d'un relais de course"):
                _sonder(pieces, relais, amont, url=f"http://127.0.0.1:{port}", nom=str(port))
        assert not list(pieces["tmp"].glob("sonde-*.json"))        # rien d'écrit
        assert amont.recues == 1
    finally:
        relais.fermer()


def test_sonde_refuse_identites_fausses(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    t = pieces["tmp"]
    try:
        autre = t / "autre_relais" / "relais_kimi_v4.py"
        autre.parent.mkdir()
        autre.write_text("# autre relais\n")
        mauvais = {"programme": [sys.executable, str(autre), "--port", str(relais.port)],
                   "port": [sys.executable, str(pieces["relais"]), "--port", "1"]}
        for motif, cmdline in mauvais.items():
            with pytest.raises(S.Refus):
                S.sonder(pieces["commande"], relais.url, os.getpid(), t / f"s-{motif}.json", t / f"v2-{motif}.json",
                         lire_cmd=lambda pid, c=cmdline: c, amont=amont.url, horodatage=lambda: "2026-11-18T11:00:00Z")
        with pytest.raises(S.Refus, match="pid"):                  # PID d'un autre processus que le relais
            S.sonder(pieces["commande"], relais.url, os.getpid() + 1, t / "s-pid.json", t / "v2-pid.json",
                     lire_cmd=lambda pid: [sys.executable, str(pieces["relais"]), "--port", str(relais.port)], amont=amont.url)
        with pytest.raises(S.Refus, match="amont"):                # amont autre que celui exigé (OpenAI en production)
            S.sonder(pieces["commande"], relais.url, os.getpid(), t / "s-amont.json", t / "v2-amont.json",
                     lire_cmd=lambda pid: [sys.executable, str(pieces["relais"]), "--port", str(relais.port)])
        faux_cmd = t / "commande_astra_v1_modifiee.py"
        faux_cmd.write_bytes(OCTETS_COMMANDE + b"\n")
        with pytest.raises(S.Refus, match="empreinte"):
            S.sonder(faux_cmd, relais.url, os.getpid(), t / "s-cmd.json", t / "v2-cmd.json",
                     lire_cmd=lambda pid: [sys.executable, str(pieces["relais"]), "--port", str(relais.port)], amont=amont.url)
        assert amont.recues == 0 and relais.compteur.appels == 0
    finally:
        relais.fermer()


def test_sonde_rapport_existant_refuse(pieces):
    amont = FauxAmont()
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        (pieces["tmp"] / "sonde-a.json").write_text("{}")
        with pytest.raises(S.Refus, match="R12"):
            _sonder(pieces, relais, amont)
        assert amont.recues == 0
    finally:
        relais.fermer()


def test_sonde_modele_servi_autre_echec_rapporte(pieces):
    amont = FauxAmont(modele="gpt-autre")
    relais = RelaisFactice(amont, reserve=0.01)
    try:
        assert _sonder(pieces, relais, amont) == 1
        o = json.loads((pieces["tmp"] / "sonde-a.json").read_text())
        assert o["ok"] is False and o["echec_de_configuration"] is False and o["rapport_v2"]["ok"] is False
    finally:
        relais.fermer()


def test_principal_usage_refuse():
    assert S.principal([]) == 2
