"""Essais de `relais_gemini_v3.py` (la v2, plus la lecture de l'amont en flux pour la génération). Clé factice, faux amont
local qui parle en flux d'événements, aucun réseau sortant, aucun appel payant. Plus un essai de bout en bout avec la vraie
commande `commande_argon_v3e.py` (inchangée) devant le relais v3.

Lancer (depuis ce dossier) : `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider test_relais_gemini_v3.py`
"""

import json
import os
import socket
import subprocess
import sys
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import relais_gemini_v3 as relais  # noqa: E402

COMMANDE = os.path.join(ICI, "commande_argon_v3e.py")
CLE_REELLE = "cle-factice-du-relais-AIzaTEST-1234567890"  # factice : la « vraie » clé que seul le relais détient
CLE_CLIENT = "factice-relais"
MODELE = "gemini-4-carbon"
CHEMIN_GEN = f"/v1beta/models/{MODELE}:generateContent"
CHEMIN_CT = f"/v1beta/models/{MODELE}:countTokens"
USAGE = {"promptTokenCount": 100, "candidatesTokenCount": 7, "thoughtsTokenCount": 40, "totalTokenCount": 147}
CORPS = {"contents": [{"role": "user", "parts": [{"text": "Bonjour ?"}]}],
         "generationConfig": {"maxOutputTokens": 2000, "thinkingConfig": {"thinkingBudget": 512}}}


def evenement(objet):
    return ("data: " + json.dumps(objet, ensure_ascii=False) + "\r\n\r\n").encode("utf-8")


def morceaux_sains(modele=MODELE):
    return [
        {"candidates": [{"content": {"role": "model", "parts": [{"text": "je réfléchis…", "thought": True}]}, "index": 0}],
         "modelVersion": modele, "responseId": "r-1"},
        {"candidates": [{"content": {"role": "model", "parts": [{"text": "Bon", "thoughtSignature": "sig"}]}, "index": 0}],
         "modelVersion": modele, "usageMetadata": {"promptTokenCount": 100}},
        {"candidates": [{"content": {"role": "model", "parts": [{"text": "jour"}]}, "finishReason": "STOP", "index": 0}],
         "modelVersion": modele, "usageMetadata": USAGE, "responseId": "r-1"},
    ]


class FauxAmontFlux:
    """Faux amont local : `:countTokens` en JSON, `:streamGenerateContent?alt=sse` en flux selon `self.scenario`."""

    def __init__(self):
        self.scenario, self.recus, self.morceaux, self.pause_s = "sain", [], morceaux_sains(), 0.0
        faux = self

        class G(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def do_POST(self):
                corps = self.rfile.read(int(self.headers.get("content-length") or 0))
                faux.recus.append({"chemin": self.path, "en_tetes": {k.lower(): v for k, v in self.headers.items()},
                                   "corps": json.loads(corps) if corps else None})
                if ":countTokens" in self.path:
                    return self._json(200, {"totalTokens": 100})
                if ":generateContent" in self.path:
                    return self._json(500, {"error": {"status": "INTERNAL", "message": "chemin sans flux appelé"}})
                s = faux.scenario
                if s == "erreur400":
                    return self._json(400, {"error": {"code": 400, "status": "INVALID_ARGUMENT", "message": f"clé {CLE_REELLE}"}})
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Transfer-Encoding", "chunked")
                self.end_headers()

                def envoyer(octets):
                    self.wfile.write(f"{len(octets):x}\r\n".encode() + octets + b"\r\n")
                    self.wfile.flush()

                morceaux = list(faux.morceaux)
                if s == "sans_fin":
                    morceaux = morceaux[:2]
                for i, m in enumerate(morceaux):
                    if s == "silence" and i == 1:
                        time.sleep(faux.pause_s)
                    if s == "lent":
                        time.sleep(faux.pause_s)
                    if s == "illisible" and i == 1:
                        envoyer(b"data: {pas du json\r\n\r\n")
                        continue
                    if s == "battement":
                        envoyer(b": battement\r\n\r\n")
                    envoyer(evenement(m))
                    if s == "coupure" and i == 0:
                        self.wfile.flush()
                        self.connection.shutdown(socket.SHUT_RDWR)
                        self.close_connection = True
                        return
                self.wfile.write(b"0\r\n\r\n")
                self.wfile.flush()
                self.close_connection = True

            def _json(self, statut, objet):
                corps = json.dumps(objet).encode("utf-8")
                self.send_response(statut)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(corps)))
                self.end_headers()
                self.wfile.write(corps)
                self.close_connection = True

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), G)
        self.serveur.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()

    def arreter(self):
        self.serveur.shutdown()
        self.serveur.server_close()


@pytest.fixture
def amont():
    a = FauxAmontFlux()
    yield a
    a.arreter()


def demarrer_relais(amont_url, tmp_path, **options):
    journal = tmp_path / "journal.jsonl"
    pret = threading.Event()
    environnement = {}  # la variable de clé n'y est pas : le relais refuserait sinon
    t = threading.Thread(target=relais.servir, kwargs=dict(
        port=0, cle=CLE_REELLE, amont=amont_url, modeles=[MODELE, "gemini-4-argon"], max_appels=64,
        max_octets_corps=8_000_000, journal=str(journal), pret=pret, environnement=environnement, **options), daemon=True)
    t.start()
    assert pret.wait(10)
    return pret.url, journal


@pytest.fixture
def relais_url(amont, tmp_path):
    return demarrer_relais(amont.url, tmp_path)


def appeler(url, chemin, corps=CORPS):
    donnees = json.dumps(corps).encode("utf-8") if not isinstance(corps, bytes) else corps
    req = urllib.request.Request(url + chemin, data=donnees, method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": CLE_CLIENT})
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with ouvreur.open(req, timeout=30) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def journal_de(chemin, au_moins=1, attente_s=5.0):
    """Le relais écrit son journal juste après avoir rendu la réponse au client : on attend l'entrée (au plus 5 s)."""
    fin = time.time() + attente_s
    while True:
        lignes = [json.loads(l) for l in open(chemin, encoding="utf-8")] if os.path.exists(chemin) else []
        if len(lignes) >= au_moins or time.time() > fin:
            return lignes
        time.sleep(0.02)


# === fonctions pures ===================================================================================================

def test_chemin_flux():
    assert relais.chemin_flux(CHEMIN_GEN) == f"/v1beta/models/{MODELE}:streamGenerateContent?alt=sse"
    assert relais.chemin_flux(CHEMIN_GEN + "?alt=json&x=1") == f"/v1beta/models/{MODELE}:streamGenerateContent?alt=sse&x=1"


def test_poser_pensees_garde_le_budget_et_le_reste():
    corps, pose = relais.poser_pensees(json.dumps(CORPS).encode())
    objet = json.loads(corps)
    assert pose and objet["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 512, "includeThoughts": True}
    assert objet["contents"] == CORPS["contents"] and objet["generationConfig"]["maxOutputTokens"] == 2000
    corps2, pose2 = relais.poser_pensees(json.dumps({"contents": []}).encode())
    assert pose2 and json.loads(corps2)["generationConfig"] == {"thinkingConfig": {"includeThoughts": True}}
    for brut in (b"pas du json", b"[1, 2]", json.dumps({"generationConfig": 3}).encode()):
        assert relais.poser_pensees(brut) == (brut, False)


def test_assembler_concatene_retire_les_pensees_garde_les_dernieres_valeurs():
    objet, pensees = relais.assembler(morceaux_sains())
    assert pensees == 1
    (c,) = objet["candidates"]
    assert c["content"] == {"role": "model", "parts": [{"text": "Bonjour"}]} and c["finishReason"] == "STOP"
    assert objet["usageMetadata"] == USAGE and objet["modelVersion"] == MODELE and objet["responseId"] == "r-1"


def test_assembler_garde_les_autres_parties_pour_que_la_commande_les_refuse():
    m = morceaux_sains()
    m[1]["candidates"][0]["content"]["parts"].append({"functionCall": {"name": "x", "args": {}}})
    objet, _ = relais.assembler(m)
    assert objet["candidates"][0]["content"]["parts"] == [{"text": "Bonjour"}, {"functionCall": {"name": "x", "args": {}}}]


@pytest.mark.parametrize("mauvais", [[3], [{"candidates": 3}], [{"candidates": [{"index": 1}]}],
                                     [{"candidates": [{"content": {"parts": ["x"]}}]}]])
def test_assembler_refuse_un_flux_mal_forme(mauvais):
    with pytest.raises(ValueError):
        relais.assembler(mauvais)


# === relais en marche devant le faux amont =============================================================================

def test_generation_relayee_en_flux_et_rendue_entiere(amont, relais_url):
    url, journal = relais_url
    statut, en_tetes, octets = appeler(url, CHEMIN_GEN)
    assert statut == 200 and en_tetes["Content-Type"].startswith("application/json")
    objet = json.loads(octets)
    assert objet["candidates"][0]["content"]["parts"] == [{"text": "Bonjour"}]
    assert objet["candidates"][0]["finishReason"] == "STOP" and objet["modelVersion"] == MODELE
    assert int(en_tetes["Content-Length"]) == len(octets)
    (recu,) = amont.recus
    assert recu["chemin"] == f"/v1beta/models/{MODELE}:streamGenerateContent?alt=sse"
    assert recu["en_tetes"]["x-goog-api-key"] == CLE_REELLE  # la clé du client est remplacée
    assert recu["corps"]["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 512, "includeThoughts": True}
    (e,) = journal_de(journal)
    assert e["statut_amont"] == 200 and e["modele_servi"] == MODELE and e["usageMetadata"] == USAGE
    assert e["flux"]["morceaux"] == 3 and e["flux"]["parties_pensee_retirees"] == 1 and e["flux"]["pensees_demandees"] is True
    assert "Bonjour" not in open(journal, encoding="utf-8").read() and CLE_REELLE not in open(journal, encoding="utf-8").read()


def test_sans_pensees_amont_le_corps_part_tel_quel(amont, tmp_path):
    url, journal = demarrer_relais(amont.url, tmp_path, inclure_pensees=False)
    statut, _, _ = appeler(url, CHEMIN_GEN)
    assert statut == 200 and amont.recus[0]["corps"] == CORPS
    assert journal_de(journal)[0]["flux"]["pensees_demandees"] is False


def test_count_tokens_sans_flux_inchange(amont, relais_url):
    url, journal = relais_url
    statut, _, octets = appeler(url, CHEMIN_CT, {"contents": []})
    assert statut == 200 and json.loads(octets) == {"totalTokens": 100}
    assert amont.recus[0]["chemin"] == CHEMIN_CT and amont.recus[0]["corps"] == {"contents": []}
    assert "flux" not in journal_de(journal)[0]


def test_battements_du_flux_ignores(amont, relais_url):
    amont.scenario = "battement"
    statut, _, octets = appeler(relais_url[0], CHEMIN_GEN)
    assert statut == 200 and json.loads(octets)["candidates"][0]["content"]["parts"] == [{"text": "Bonjour"}]


@pytest.mark.parametrize("scenario,motif", [("sans_fin", "sans finishReason"), ("illisible", "illisible"),
                                            ("coupure", "sans finishReason")])  # coupure franche : fin de flux sans finishReason
def test_flux_incomplet_donne_502_jamais_une_reponse_tronquee(amont, relais_url, scenario, motif):
    amont.scenario = scenario
    url, journal = relais_url
    statut, _, octets = appeler(url, CHEMIN_GEN)
    assert statut == 502 and motif in json.loads(octets)["erreur"]
    (e,) = journal_de(journal)
    assert e["statut"] == 502 and e["statut_amont"] == 200 and "flux" in e


def test_silence_au_dela_du_delai_donne_502(amont, tmp_path):
    amont.scenario, amont.pause_s = "silence", 2.0
    url, journal = demarrer_relais(amont.url, tmp_path, delai_silence_s=0.5)
    debut = time.time()
    statut, _, octets = appeler(url, CHEMIN_GEN)
    assert statut == 502 and "flux amont interrompu" in json.loads(octets)["erreur"] and time.time() - debut < 1.9


def test_flux_lent_mais_jamais_muet_passe(amont, tmp_path):
    """Le délai de silence borne chaque attente, pas la durée totale : 3 morceaux espacés de 0,4 s, silence permis 0,8 s."""
    amont.scenario, amont.pause_s = "lent", 0.4
    url, journal = demarrer_relais(amont.url, tmp_path, delai_silence_s=0.8)
    statut, _, _ = appeler(url, CHEMIN_GEN)
    assert statut == 200 and journal_de(journal)[0]["flux"]["silence_max_s"] >= 0.35


def test_duree_totale_bornee(amont, tmp_path):
    amont.scenario, amont.pause_s = "lent", 0.4
    url, _ = demarrer_relais(amont.url, tmp_path, delai_silence_s=0.8, delai_amont_s=0.6)
    statut, _, octets = appeler(url, CHEMIN_GEN)
    assert statut == 502 and "durée totale" in json.loads(octets)["erreur"]


def test_erreur_amont_relayee_telle_quelle_cle_masquee(amont, relais_url):
    amont.scenario = "erreur400"
    statut, _, octets = appeler(relais_url[0], CHEMIN_GEN)
    assert statut == 400 and json.loads(octets)["error"]["message"] == "clé [clé]"


def test_cle_recopiee_dans_le_flux_masquee(amont, relais_url):
    amont.morceaux = morceaux_sains()
    amont.morceaux[2]["candidates"][0]["content"]["parts"][0]["text"] = f"jour {CLE_REELLE}"
    url, journal = relais_url
    statut, _, octets = appeler(url, CHEMIN_GEN)
    assert statut == 200 and CLE_REELLE.encode() not in octets
    assert json.loads(octets)["candidates"][0]["content"]["parts"][0]["text"] == "Bonjour [clé]"
    assert journal_de(journal)[0]["cle_masquee_dans_reponse"] == 1


def test_modele_hors_liste_refuse_sans_envoi(amont, relais_url):
    statut, _, _ = appeler(relais_url[0], "/v1beta/models/autre:generateContent")
    assert statut == 403 and amont.recus == []


def test_etat_dit_le_flux(amont, relais_url):
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    e = json.loads(ouvreur.open(relais_url[0] + "/relais/etat", timeout=5).read())
    assert e["version"] == "relais-gemini-v3" and e["delai_silence_s"] == 240.0 and e["pensees_amont_demandees"] is True


def test_analyseur_options_v3():
    a = relais.analyseur()
    assert a.parse_args([]).inclure_pensees is True and a.parse_args([]).delai_silence_s == 240.0
    assert a.parse_args(["--sans-pensees-amont"]).inclure_pensees is False
    with pytest.raises(SystemExit):
        a.parse_args(["--sans-pensees-amont", "--inclure-pensees-amont"])


def test_silence_nul_refuse_au_demarrage(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", CLE_REELLE)
    assert relais.principal(["--port", "0", "--delai-silence-s", "0"]) == 2


# === bout en bout : la vraie commande, inchangée, devant le relais v3 ==================================================

def lancer_commande(url_relais, *options):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": "3", "ROLE_POLE": "proposeur_ideation",
           "MODELE_DEMANDE_POLE": MODELE, "GEMINI_API_KEY": CLE_CLIENT}
    r = subprocess.run([sys.executable, "-I", "-B", COMMANDE, "--modele", MODELE, "--prix-entree", "8.3",
                        "--prix-sortie", "41.5", *options, "--url-base", url_relais + "/v1beta"],
                       input=("Propose une idée.\n" * 20).encode("utf-8"), capture_output=True, env=env, timeout=60)
    return r.returncode, json.loads(r.stdout.decode("utf-8").strip().splitlines()[-1])


def test_bout_en_bout_la_commande_rend_le_texte_et_le_modele_servi(amont, relais_url):
    code, objet = lancer_commande(relais_url[0])
    assert code == 0, objet
    assert objet["texte"] == "Bonjour" and objet["modele_servi"] == MODELE and objet["cout_usd"] > 0
    chemins = [r["chemin"] for r in amont.recus]
    assert chemins == [CHEMIN_CT, f"/v1beta/models/{MODELE}:streamGenerateContent?alt=sse"]
    pensee = amont.recus[1]["corps"]["generationConfig"]["thinkingConfig"]
    assert pensee["includeThoughts"] is True and "thinkingBudget" in pensee  # budget posé par la commande, gardé


def test_bout_en_bout_flux_tronque_donne_une_erreur_au_pire_cas(amont, relais_url):
    amont.scenario = "sans_fin"
    code, objet = lancer_commande(relais_url[0])
    assert code != 0 and "502" in objet.get("erreur", "") and objet["cout_usd"] > 0
