"""Essais de `relais_gemini_v4.py` et de `commande_gemini_lot_v1.py` : faux amont Gemini local (comptage, lot, relevé,
annulation), relais réel en processus, commande réelle ; clé factice, aucun réseau sortant, aucun appel payant."""
import json, os, sys, threading, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import commande_gemini_lot_v1 as cmd  # noqa: E402
import relais_gemini_v4 as relais  # noqa: E402

CLE = "cle-factice-du-relais-AIzaTEST-55555"
MODELE = "gemini-4-carbon"
USAGE = {"promptTokenCount": 120, "candidatesTokenCount": 40, "thoughtsTokenCount": 800, "totalTokenCount": 960}


class FauxAmont:
    def __init__(self):
        self.recus, self.releves_avant_fin, self.scenario, self.annules = [], 2, "sain", []
        self.lots = {}
        f = self

        class G(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def _rep(self, statut, o):
                b = json.dumps(o).encode()
                self.send_response(statut); self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
                self.close_connection = True

            def do_POST(self):
                n = int(self.headers.get("content-length") or 0)
                corps = json.loads(self.rfile.read(n)) if n else None
                f.recus.append(("POST", self.path, self.headers.get("x-goog-api-key"), corps))
                if self.path.endswith(":countTokens"):
                    return self._rep(200, {"totalTokens": 100})
                if self.path.endswith(":batchGenerateContent"):
                    nom = f"batches/lot{len(f.lots) + 1}"
                    f.lots[nom] = 0
                    return self._rep(200, {"name": nom, "metadata": {"name": nom, "state": "BATCH_STATE_PENDING"}})
                if self.path.endswith(":cancel"):
                    f.annules.append(self.path)
                    return self._rep(200, {})
                return self._rep(404, {"error": {"message": "inconnu"}})

            def do_GET(self):
                f.recus.append(("GET", self.path, self.headers.get("x-goog-api-key"), None))
                nom = self.path.split("/v1beta/")[1]
                f.lots[nom] = f.lots.get(nom, 0) + 1
                if f.scenario == "jamais" or f.lots[nom] <= f.releves_avant_fin:
                    return self._rep(200, {"name": nom, "metadata": {"state": "BATCH_STATE_RUNNING"}})
                if f.scenario == "echec":
                    return self._rep(200, {"name": nom, "done": True, "metadata": {"state": "BATCH_STATE_FAILED"}})
                rep = {"candidates": [{"content": {"parts": [{"text": "pensée", "thought": True}, {"text": "Réponse " + CLE}]},
                                       "finishReason": "MAX_TOKENS" if f.scenario == "tronque" else "STOP"}],
                       "usageMetadata": USAGE, "modelVersion": "gemini-4-argon" if f.scenario == "autre_modele" else MODELE}
                return self._rep(200, {"name": nom, "done": True, "metadata": {"state": "BATCH_STATE_SUCCEEDED"},
                                       "response": {"inlinedResponses": {"inlinedResponses": [{"response": rep}]}}})

        self.s = ThreadingHTTPServer(("127.0.0.1", 0), G); self.s.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.s.server_address[1]}"
        threading.Thread(target=self.s.serve_forever, daemon=True).start()


@pytest.fixture
def monde(tmp_path):
    a = FauxAmont()
    pret = threading.Event()
    journal = tmp_path / "j.jsonl"
    threading.Thread(target=relais.servir, kwargs=dict(port=0, cle=CLE, amont=a.url, modeles=[MODELE], max_appels=10,
                     max_octets_corps=1_000_000, journal=str(journal), pret=pret, environnement={}, max_lots=2,
                     max_releves=50), daemon=True).start()
    assert pret.wait(10)
    yield a, pret.url, journal
    a.s.shutdown()


ENV = {"PLAFOND_SESSION_USD": "1.5", "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": MODELE}


def lancer(url, env=ENV, extra=(), consigne="Propose une idée.\n" * 10):
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
        code = cmd.principal(["--modele", MODELE, "--prix-entree", "8.3", "--prix-sortie", "41.5", "--url-base",
                              url + "/v1beta", "--intervalle-s", "0", *extra], environ=env, entree=consigne.encode(),
                             dormir=lambda s: None)
    return code, json.loads(out.getvalue().strip().splitlines()[-1])


def test_sain_par_le_relais(monde):
    a, url, journal = monde
    code, l = lancer(url)
    assert code == 0 and l["texte"] == "Réponse [clé]" and l["modele_servi"] == MODELE and l["fin"] == "STOP"
    attendu = (120 * 8.3 + 840 * 41.5) / 1e6
    assert l["cout_usd"] == pytest.approx(attendu)
    creation = [r for r in a.recus if r[1].endswith(":batchGenerateContent")][0]
    assert creation[2] == CLE  # la vraie clé est posée par le relais, jamais par la commande
    req = creation[3]["batch"]["input_config"]["requests"]["requests"]
    assert len(req) == 1 and req[0]["request"]["generationConfig"]["thinkingConfig"]["thinkingBudget"] == 8192
    lignes = [json.loads(x) for x in open(journal)]
    assert CLE not in open(journal).read() and "Réponse" not in open(journal).read()
    fin = [x for x in lignes if x.get("done")]
    assert fin and fin[-1]["reponses"][0]["thoughtsTokenCount"] == 800


def test_facteur_lot(monde):
    _, url, _ = monde
    code, l = lancer(url, extra=("--facteur-lot", "0.5"))
    assert code == 0 and l["cout_usd"] == pytest.approx((120 * 8.3 + 840 * 41.5) / 1e6 * 0.5)


@pytest.mark.parametrize("scenario,code_attendu", [("tronque", 5), ("autre_modele", 5), ("echec", 3)])
def test_echecs_au_pire_cas(monde, scenario, code_attendu):
    a, url, _ = monde
    a.scenario = scenario
    code, l = lancer(url)
    assert code == code_attendu and l["cout_origine"] == "pire_cas" and l["cout_usd"] > 0.3
    assert ("modele_servi" in l) == (scenario in ("tronque", "autre_modele"))  # jamais un modele_servi nul


def test_delai_annule_le_lot(monde):
    a, url, _ = monde
    a.scenario = "jamais"
    t = iter(range(0, 100000, 100))
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
        code = cmd.principal(["--modele", MODELE, "--prix-entree", "8.3", "--prix-sortie", "41.5", "--url-base",
                              url + "/v1beta", "--delai-s", "500"], environ=ENV, entree=b"x" * 200,
                             dormir=lambda s: None, horloge=lambda: next(t))
    l = json.loads(out.getvalue().strip().splitlines()[-1])
    assert code == 6 and a.annules and "annulé" in l["erreur"] and "modele_servi" not in l


@pytest.mark.parametrize("env,code_attendu", [
    (dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon"), 2), (dict(ENV, ROLE_POLE="autre"), 2),
    (dict(ENV, PLAFOND_SESSION_USD="0.05"), 4), ({k: v for k, v in ENV.items() if k != "PLAFOND_SESSION_USD"}, 2)])
def test_refus_sans_envoi(monde, env, code_attendu):
    a, url, _ = monde
    code, l = lancer(url, env=env)
    assert code == code_attendu and l["cout_usd"] == 1e-6
    assert not [r for r in a.recus if r[1].endswith(":batchGenerateContent")]


def test_relais_refuse_le_releve_d_un_lot_etranger(monde):
    a, url, _ = monde
    req = urllib.request.Request(url + "/v1beta/batches/etranger", method="GET")
    with pytest.raises(urllib.error.HTTPError) as e:
        urllib.request.build_opener(urllib.request.ProxyHandler({})).open(req, timeout=5)
    assert e.value.code == 403 and not [r for r in a.recus if r[0] == "GET"]


def test_relais_borne_les_lots(monde):
    _, url, _ = monde
    assert lancer(url)[0] == 0 and lancer(url)[0] == 0
    code, l = lancer(url)
    assert code == 3 and "429" in l["erreur"]


def test_relais_modele_hors_liste(monde):
    a, url, _ = monde
    import io, contextlib
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
        code = cmd.principal(["--modele", "gemini-4-argon", "--prix-entree", "8.3", "--prix-sortie", "41.5", "--url-base",
                              url + "/v1beta"], environ=dict(ENV, MODELE_DEMANDE_POLE="gemini-4-argon"), entree=b"x" * 200)
    assert code == 3 and not a.recus


def test_etat_du_relais(monde):
    _, url, _ = monde
    lancer(url)
    e = json.loads(urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url + "/relais/etat", timeout=5).read())
    assert e["version"] == "relais-gemini-v4" and e["lots_crees"] == 1 and e["releves"] >= 3
