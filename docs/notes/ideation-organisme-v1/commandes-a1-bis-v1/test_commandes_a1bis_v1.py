"""Essais hors réseau des commandes Claude et Astra d'A1-bis (R5 : cas sain et artefacts). Faux amonts locaux (Anthropic en flux
SSE, OpenAI chat/completions) ; relais et commandes lancés en sous-processus, sous environnement minimal ; fausse clé ; aucune
clé réelle lue. Lancer avec un Python qui a le paquet `anthropic` (relais Claude) :
    PY_RELAIS=<python avec anthropic> python -m pytest -q test_commandes_a1bis_v1.py
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
PY_RELAIS = os.environ.get("PY_RELAIS", sys.executable)
PY_CMD = "/usr/bin/python3"
FAUSSE_CLE = "sk-FAUSSE-cle-essai-0123456789abcdef"
REQUETES = []


def port_libre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class FauxAmont(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        corps = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        REQUETES.append({"chemin": self.path, "corps": corps, "auth": self.headers.get("Authorization") or self.headers.get("x-api-key")})
        texte = corps["messages"][0]["content"]
        modele = corps["model"]
        if "MODE=autre_modele" in texte:
            modele = modele + "-autre"
        if "MODE=erreur" in texte:
            b = json.dumps({"error": {"type": "overloaded_error", "message": "surcharge factice"}}).encode()
            self.send_response(529 if self.path.startswith("/v1/messages") else 503)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
            return
        if self.path.startswith("/v1/messages"):
            evts = [("message_start", {"type": "message_start", "message": {"id": "msg_f", "type": "message", "role": "assistant",
                     "model": modele, "content": [], "stop_reason": None, "stop_sequence": None,
                     "usage": {"input_tokens": 1200, "output_tokens": 1}}}),
                    ("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}),
                    ("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "réponse factice"}}),
                    ("content_block_stop", {"type": "content_block_stop", "index": 0}),
                    ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None},
                                       "usage": {"output_tokens": 3000}}),
                    ("message_stop", {"type": "message_stop"})]
            b = "".join(f"event: {e}\ndata: {json.dumps(d)}\n\n" for e, d in evts).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
            return
        b = json.dumps({"id": "c1", "model": modele, "choices": [{"index": 0, "finish_reason": "stop",
                        "message": {"role": "assistant", "content": "réponse factice"}}],
                        "usage": {"prompt_tokens": 1000, "completion_tokens": 2000,
                                  "completion_tokens_details": {"reasoning_tokens": 1500}}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)


@pytest.fixture(scope="module")
def amont():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), FauxAmont)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


def lancer_relais(script, tmp, env_cle, extra, plafond="5", nom="r"):
    port = port_libre()
    journal = os.path.join(tmp, f"{nom}-journal.jsonl")
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", **env_cle}
    p = subprocess.Popen([PY_RELAIS, "-I", "-B", os.path.join(ICI, script), "servir", "--port", str(port), "--plafond-usd", plafond,
                          "--max-appels", "20", "--journal", journal] + extra,
                         env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for _ in range(100):
        try:
            urllib.request.build_opener(urllib.request.ProxyHandler({})).open(f"http://127.0.0.1:{port}/relais/etat", timeout=1)
            break
        except OSError:
            if p.poll() is not None:
                raise AssertionError("relais mort : " + p.stdout.read().decode())
            time.sleep(0.1)
    return p, port, journal


def appeler(script, port, tmp, prompt, extra, session="1.8", cumule="80", modele=None):
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": session, "ROLE_POLE": "proposeur_ideation",
           "ETAPE_POLE": "essai", "PLAFOND_ETAPE_USD": "40"}
    if modele:
        env["MODELE_DEMANDE_POLE"] = modele
    r = subprocess.run([PY_CMD, "-I", "-B", os.path.join(ICI, script), "appeler", "--url-relais", f"http://127.0.0.1:{port}",
                        "--registre", os.path.join(tmp, "registre.jsonl"), "--plafond-cumule-usd", cumule,
                        "--max-sortie-proposeur", "32000", "--max-sortie-court", "4000", "--sortie-min-jetons", "1000"] + extra,
                       input=prompt, text=True, capture_output=True, env=env, timeout=60)
    derniere = json.loads(r.stdout.strip().splitlines()[-1])
    return r.returncode, derniere, r.stdout + r.stderr


def sans_cle(*chemins_ou_textes):
    for x in chemins_ou_textes:
        t = open(x).read() if os.path.exists(x) else x
        assert FAUSSE_CLE not in t


# --- Claude ------------------------------------------------------------------------------------------------------------

CL = "commande_claude_a1bis_v1.py"
REG_CL = ["--effort", "high", "--reflexion", "adaptative"]


@pytest.fixture
def relais_claude(amont, tmp_path):
    p, port, j = lancer_relais(CL, str(tmp_path), {"ANTHROPIC_API_KEY": FAUSSE_CLE, "ANTHROPIC_BASE_URL": amont},
                               ["--modeles-permis", "claude-opus-5-5,claude-fable-5-1,claude-opus-4-6"] + REG_CL)
    yield port, j, str(tmp_path)
    p.terminate()
    p.wait(10)


def test_claude_sain(relais_claude):
    port, j, tmp = relais_claude
    REQUETES.clear()
    code, d, brut = appeler(CL, port, tmp, "Consigne d'essai.", ["--modele", "claude-opus-5-5"] + REG_CL, modele="claude-opus-5-5")
    assert code == 0, brut
    assert d["modele_servi"] == "claude-opus-5-5" and d["cout_origine"] == "usage"
    assert abs(d["cout_usd"] - (1200 * 4 + 3000 * 20) / 1e6) < 1e-9
    assert d["reglages"] == {"effort": "high", "reflexion": "adaptative"} == d["reglages_relais"]
    c = REQUETES[-1]["corps"]
    assert c["model"] == "claude-opus-5-5" and c["output_config"] == {"effort": "high"} and c["thinking"] == {"type": "adaptive"}
    assert "fallbacks" not in c
    sans_cle(j, brut, os.path.join(tmp, "registre.jsonl"))


def test_claude_modele_servi_different(relais_claude):
    port, j, tmp = relais_claude
    code, d, brut = appeler(CL, port, tmp, "MODE=autre_modele", ["--modele", "claude-fable-5-1"] + REG_CL)
    assert code == 5 and "modèle servi" in d["erreur"], brut


def test_claude_budget_session_depasse(relais_claude):
    port, j, tmp = relais_claude
    REQUETES.clear()
    code, d, brut = appeler(CL, port, tmp, "x" * 100, ["--modele", "claude-fable-5-1"] + REG_CL, session="0.01")
    assert code == 4 and d["envoye"] is False and not REQUETES, brut


def test_claude_plafond_cumule_depasse(relais_claude):
    port, j, tmp = relais_claude
    code, d, brut = appeler(CL, port, tmp, "Consigne.", ["--modele", "claude-opus-5-5"] + REG_CL, cumule="0.05")
    assert code == 4 and d["envoye"] is False, brut


def test_claude_amont_en_erreur(relais_claude):
    port, j, tmp = relais_claude
    code, d, brut = appeler(CL, port, tmp, "MODE=erreur", ["--modele", "claude-opus-5-5"] + REG_CL)
    assert code == 3 and d["cout_origine"] == "pire_cas" and "529" in d["erreur"], brut
    sans_cle(j, brut)


def test_claude_reglages_differents_refuses(relais_claude):
    port, j, tmp = relais_claude
    REQUETES.clear()
    code, d, brut = appeler(CL, port, tmp, "Consigne.", ["--modele", "claude-opus-5-5", "--effort", "max", "--reflexion", "adaptative"])
    assert code == 3 and d["envoye"] is False and "409" in d["erreur"] and not REQUETES, brut


def test_claude_effort_xhigh_refuse_sur_opus_4_6(tmp_path):
    code, d, brut = appeler(CL, 1, str(tmp_path), "x", ["--modele", "claude-opus-4-6", "--effort", "xhigh", "--reflexion", "omise"])
    assert code == 2 and "effort" in d["erreur"], brut


def test_claude_base_url_tierce_refusee(tmp_path):
    r = subprocess.run([PY_RELAIS, "-I", "-B", os.path.join(ICI, CL), "servir", "--port", str(port_libre()), "--plafond-usd", "1",
                        "--max-appels", "1", "--journal", str(tmp_path / "j"), "--modeles-permis", "claude-opus-5-5"] + REG_CL,
                       env={"PATH": "/usr/bin:/bin", "ANTHROPIC_API_KEY": FAUSSE_CLE, "ANTHROPIC_BASE_URL": "https://tiers.example"},
                       capture_output=True, text=True, timeout=30)
    assert r.returncode != 0 and "ANTHROPIC_BASE_URL" in r.stderr and FAUSSE_CLE not in r.stdout + r.stderr


def test_relais_plafond_propre(amont, tmp_path):
    p, port, j = lancer_relais(CL, str(tmp_path), {"ANTHROPIC_API_KEY": FAUSSE_CLE, "ANTHROPIC_BASE_URL": amont},
                               ["--modeles-permis", "claude-opus-5-5"] + REG_CL, plafond="0.01")
    try:
        code, d, brut = appeler(CL, port, str(tmp_path), "Consigne.", ["--modele", "claude-opus-5-5"] + REG_CL)
        assert code == 4 and "402" in d["erreur"] and d["envoye"] is False, brut
    finally:
        p.terminate()
        p.wait(10)


# --- Astra -------------------------------------------------------------------------------------------------------------

AS = "commande_astra_a1bis_v1.py"


@pytest.fixture
def relais_astra(amont, tmp_path):
    p, port, j = lancer_relais(AS, str(tmp_path), {"OPENAI_API_KEY": FAUSSE_CLE, "OPENAI_BASE_URL": amont},
                               ["--modeles-permis", "gpt-6-astra"])
    yield port, j, str(tmp_path)
    p.terminate()
    p.wait(10)


def test_astra_sain_sans_double_compte(relais_astra):
    port, j, tmp = relais_astra
    code, d, brut = appeler(AS, port, tmp, "Consigne d'essai.", ["--modele", "gpt-6-astra"], modele="gpt-6-astra")
    assert code == 0, brut
    assert d["usage"]["sortie"] == 2000 and d["usage"]["sortie_v8_double_compte"] == 3500
    assert abs(d["cout_usd"] - (1000 * 10 + 2000 * 50) / 1e6) < 1e-9
    assert REQUETES[-1]["auth"] == f"Bearer {FAUSSE_CLE}"
    sans_cle(j, brut, os.path.join(tmp, "registre.jsonl"))


def test_astra_modele_servi_different(relais_astra):
    port, j, tmp = relais_astra
    code, d, brut = appeler(AS, port, tmp, "MODE=autre_modele", ["--modele", "gpt-6-astra"])
    assert code == 5 and "modèle servi" in d["erreur"], brut


def test_astra_budget_depasse(relais_astra):
    port, j, tmp = relais_astra
    code, d, brut = appeler(AS, port, tmp, "x" * 100, ["--modele", "gpt-6-astra"], session="0.01")
    assert code == 4 and d["envoye"] is False, brut


def test_astra_amont_en_erreur(relais_astra):
    port, j, tmp = relais_astra
    code, d, brut = appeler(AS, port, tmp, "MODE=erreur", ["--modele", "gpt-6-astra"])
    assert code == 3 and d["cout_origine"] == "pire_cas" and "503" in d["erreur"], brut
    sans_cle(j, brut)


def test_astra_modele_hors_table(tmp_path):
    code, d, brut = appeler(AS, 1, str(tmp_path), "x", ["--modele", "gpt-6-astra-mini"])
    assert code == 2, brut


def test_registre_partage_compte_les_deux(relais_claude, amont):
    port, j, tmp = relais_claude
    appeler(CL, port, tmp, "Consigne.", ["--modele", "claude-opus-5-5"] + REG_CL)
    lignes = [json.loads(x) for x in open(os.path.join(tmp, "registre.jsonl"))]
    assert {x.get("fournisseur") for x in lignes if x["type"] == "debut"} == {"claude"}
