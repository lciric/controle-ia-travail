"""Essais de la commande Gemini en flux, version 2 (`scripts/commande_gemini_flux_v2.py`), repris des essais de la v1 (`e92ff4c9…`)
et passés aux réglages de production du lanceur v11c (constat 13 : Carbon et Argon à 4 / 20 USD par million, Carbon
provision 28 672 et sortie 65 536, juge d'Argon à 1,00 USD), plus les essais de l'hypothèse « réflexion comprise dans la
sortie maximale » (constat 12). Texte d'origine : essais de la commande en flux (`scripts/commande_gemini_flux_v1.py`), hors ligne.

Le relais est le **vrai relais Gemini v3** de `main` (`relais_gemini_v3.py`, `2cf6bc6d…`, extrait de `refs/remotes/origin/main`),
servi dans ce processus sur la boucle locale avec une clé factice, devant un **faux amont** local qui rend un flux SSE au format
de Google (`streamGenerateContent?alt=sse`) ; la garde est la vraie `garde_google_v3.py` de `main` (`923679b5…`). La commande
est jouée en sous-processus (`python -I -B`), comme par l'orchestrateur. Aucun appel réel, aucune clé, aucun réseau hors de la
boucle locale. Chaque garde : un cas sain et un artefact (R5) ; mutations : réglage de réflexion retiré ou abaissé, plafond
trop bas, garde d'une autre empreinte."""
import hashlib
import importlib.util
import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
COMMANDE = RACINE / "scripts" / "commande_gemini_flux_v2.py"
RELAIS_MAIN = ("docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py",
               "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378")
GARDE_MAIN = ("src/controle_ia/garde_google_v3.py", "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91")
MODELE = "gemini-4-carbon"
# réglages de production du lanceur v11c pour Carbon (ARGUMENTS_COMMANDES["carbon"] : niveau « high », provision 28 672,
# sortie 65 536, 4 / 20 USD par million ; délais raccourcis pour l'essai seulement)
ARGS = ["--espece", "carbon", "--modele", MODELE, "--prix-entree", "4", "--prix-sortie", "20", "--niveau-reflexion", "high",
        "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "65536", "--delai-s", "60", "--delai-requete-s", "10"]


def _de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS_RELAIS, OCTETS_GARDE = _de_main(*RELAIS_MAIN), _de_main(*GARDE_MAIN)
pytestmark = pytest.mark.skipif(OCTETS_RELAIS is None or OCTETS_GARDE is None, reason="relais v3 ou garde absents de origin/main")


class FauxAmont:
    """Faux amont de Google : `countTokens` rend un compte ; `streamGenerateContent?alt=sse` rend un flux de morceaux."""

    def __init__(self, fin="STOP", pensees=1200, texte="réponse d'essai", modele=MODELE, sortie=300, bloque=None):
        self.corps, self.recues = None, 0
        moi = self

        class H(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                corps = json.loads(self.rfile.read(n) or b"{}")
                if ":countTokens" in self.path:
                    d = json.dumps({"totalTokens": 900}).encode()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(d)))
                    self.end_headers()
                    self.wfile.write(d)
                    return
                moi.corps, moi.recues = corps, moi.recues + 1
                morceaux = [{"candidates": [{"content": {"parts": [{"text": "je pense", "thought": True}]}}]},
                            {"candidates": [{"content": {"parts": [{"text": texte}]}}]},
                            {"candidates": [{"content": {"parts": []}, "finishReason": fin}], "modelVersion": modele,
                             "usageMetadata": dict({"promptTokenCount": 900, "candidatesTokenCount": sortie},
                                                   **({"thoughtsTokenCount": pensees} if pensees is not None else {}))}]
                if bloque:
                    morceaux = [{"promptFeedback": {"blockReason": bloque}, "modelVersion": modele,
                                 "candidates": [{"finishReason": "OTHER"}],
                                 "usageMetadata": {"promptTokenCount": 900, "candidatesTokenCount": 0}}]
                d = b"".join(b"data: " + json.dumps(m).encode() + b"\r\n\r\n" for m in morceaux)
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Content-Length", str(len(d)))
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(d)

            def log_message(self, *a):
                pass
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.serveur.daemon_threads = True
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"


@pytest.fixture
def pieces(tmp_path):
    relais = tmp_path / "relais_gemini_v3.py"
    relais.write_bytes(OCTETS_RELAIS)
    garde = tmp_path / "garde_google_v3.py"
    garde.write_bytes(OCTETS_GARDE)
    spec = importlib.util.spec_from_file_location("relais_gemini_v3_essai_flux", relais)
    R = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(R)
    return {"R": R, "garde": garde, "tmp": tmp_path}


def relais_devant(pieces, amont: FauxAmont, max_appels=10):
    pret = threading.Event()
    t = threading.Thread(target=pieces["R"].servir, args=(0, "cle-factice-essai", amont.url, [MODELE], max_appels, 8_000_000),
                         kwargs={"pret": pret, "environnement": {}, "delai_amont_s": 30.0, "delai_silence_s": 10.0},
                         daemon=True)
    t.start()
    assert pret.wait(10)
    return pret.url


def jouer(pieces, url, args=None, plafond="3.00", role="proposeur_ideation", consigne="Consigne d'essai."):
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": role, "MODELE_DEMANDE_POLE": MODELE}
    a = (args if args is not None else ARGS) + ["--url-base", url + "/v1beta", "--garde", str(pieces["garde"])]
    p = subprocess.run([sys.executable, "-I", "-B", str(COMMANDE)] + a, input=consigne.encode(), env=env, capture_output=True,
                       timeout=90)
    return p.returncode, json.loads(p.stdout.decode().splitlines()[-1])


def test_cas_sain_bout_en_bout_par_le_vrai_relais_en_flux(pieces):
    amont = FauxAmont()
    code, ligne = jouer(pieces, relais_devant(pieces, amont))
    assert code == 0, ligne
    assert ligne["texte"] == "réponse d'essai" and ligne["defaut_google"] is None and ligne["modele_servi"] == MODELE
    tc = amont.corps["generationConfig"]["thinkingConfig"]
    assert tc == {"thinkingLevel": "high", "includeThoughts": True} and amont.corps["generationConfig"]["maxOutputTokens"] == 65536
    assert ligne["cout_usd"] == pytest.approx((900 * 4 + (300 + 1200) * 20) / 1e6)
    assert ligne["hypothese_sortie_maximale_tenue"] is True
    assert ligne["pire_cas_usd"] <= 3.00 and ligne["reglages"]["mode"] == "flux"


@pytest.mark.parametrize("amont_kw,defaut", [({"pensees": 0}, "SANS_PENSEES"), ({"pensees": None}, "SANS_PENSEES"),
                                             ({"fin": "MAX_TOKENS"}, "MAX_TOKENS"), ({"fin": "SAFETY"}, "SAFETY"),
                                             ({"fin": "RECITATION"}, "RECITATION"), ({"texte": "  "}, "VIDE"),
                                             ({"bloque": "PROHIBITED_CONTENT"}, "PROHIBITED_CONTENT")])
def test_defauts_apres_reponse_jamais_une_reponse(pieces, amont_kw, defaut):
    amont = FauxAmont(**amont_kw)
    code, ligne = jouer(pieces, relais_devant(pieces, amont))
    assert code == 5 and ligne["texte"] == "" and ligne["defaut_google"] == defaut, ligne
    assert ligne["cout_usd"] > 1e-6 and ligne["cout_origine"] == "usage"           # la dépense est comptée


@pytest.mark.parametrize("modif,motif", [
    (("--niveau-reflexion", "medium"), "niveau envoyé"),                            # réflexion abaissée
    (("--niveau-reflexion", "aucun"), "non admis"),
    (("--max-sortie-jetons", "40000"), "jetons de texte"),                          # 40 000 − 28 672 < 16 000
    (("--max-sortie-jetons", "70000"), "au-delà de la limite"),                     # > 65 536 en flux
])
def test_garde_avant_envoi_refuse_rien_ne_part(pieces, modif, motif):
    amont = FauxAmont()
    args = list(ARGS)
    args[args.index(modif[0]) + 1] = modif[1]
    code, ligne = jouer(pieces, relais_devant(pieces, amont), args=args)
    assert code == 2 and motif in ligne["erreur"] and ligne["cout_usd"] == 1e-6, ligne
    assert amont.recues == 0


def test_mots_de_l_invite_hors_du_plafond_de_texte_refuse(pieces):
    amont = FauxAmont()
    code, ligne = jouer(pieces, relais_devant(pieces, amont), args=ARGS + ["--mots-invite", "9000"])   # 9 000 × 4,2 ≥ 36 864
    assert code == 2 and "limite de mots" in ligne["erreur"] and amont.recues == 0
    code, ligne = jouer(pieces, relais_devant(pieces, amont), args=ARGS + ["--mots-invite", "8000"])   # 33 600 < 36 864
    assert code == 0, ligne


def test_pire_cas_au_dessus_du_plafond_de_session_refuse(pieces):
    amont = FauxAmont()
    code, ligne = jouer(pieces, relais_devant(pieces, amont), plafond="1.30")      # 65 536 × 20 / 10⁶ = 1,31 > 1,30
    assert code == 4 and "pire cas" in ligne["erreur"] and amont.recues == 0


def test_garde_d_une_autre_empreinte_refusee(pieces):
    amont = FauxAmont()
    pieces["garde"].write_bytes(OCTETS_GARDE + b"\n")
    code, ligne = jouer(pieces, relais_devant(pieces, amont))
    assert code == 2 and "empreinte" in ligne["erreur"] and amont.recues == 0


def test_modele_servi_autre_refuse(pieces):
    amont = FauxAmont(modele="gemini-4-argon")
    code, ligne = jouer(pieces, relais_devant(pieces, amont))
    assert code == 5 and "modèle servi" in ligne["erreur"]


def test_relais_hors_boucle_locale_et_role_refuses(pieces):
    code, ligne = jouer(pieces, "https://generativelanguage.googleapis.com")
    assert code == 2 and "boucle locale" in ligne["erreur"]
    amont = FauxAmont()
    code, ligne = jouer(pieces, relais_devant(pieces, amont), role="juge_ideation")
    assert code == 2 and "ROLE_POLE" in ligne["erreur"] and amont.recues == 0


def test_relais_qui_refuse_compte_au_pire(pieces):
    amont = FauxAmont()
    url = relais_devant(pieces, amont, max_appels=1)                               # countTokens consomme le seul appel
    code, ligne = jouer(pieces, url)
    assert code == 3 and ligne["cout_origine"] == "pire_cas" and ligne["cout_usd"] > 1.31


def test_commande_ne_porte_aucune_cle_et_emploie_la_garde_commune():
    texte = COMMANDE.read_text(encoding="utf-8")
    assert "verifier_reglages_google" in texte and "defaut_reponse_google" in texte and 'mode="flux"' in texte
    assert GARDE_MAIN[1] in texte and "GEMINI_API_KEY" not in texte


# --- Argon sous la même commande (décision de la mère) : réglages du lanceur v11 -------------------------------------------------

ARGS_ARGON = ["--espece", "argon", "--modele", "gemini-4-argon", "--prix-entree", "4", "--prix-sortie", "20",
              "--niveau-reflexion", "high", "--provision-pensee-jetons", "24576", "--max-sortie-jetons", "45056", "--delai-s", "60",
              "--delai-requete-s", "10", "--roles", "proposeur_ideation,juge_ideation"]


def relais_argon(pieces, amont):
    pret = threading.Event()
    threading.Thread(target=pieces["R"].servir, args=(0, "cle-factice-essai", amont.url, ["gemini-4-argon"], 10, 8_000_000),
                     kwargs={"pret": pret, "environnement": {}, "delai_amont_s": 30.0, "delai_silence_s": 10.0}, daemon=True).start()
    assert pret.wait(10)
    return pret.url


def jouer_argon(pieces, url, args=None, plafond="1.00", role="juge_ideation"):  # v2 : juge à 1,00 (production)
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": role, "MODELE_DEMANDE_POLE": "gemini-4-argon"}
    a = (args if args is not None else ARGS_ARGON) + ["--url-base", url + "/v1beta", "--garde", str(pieces["garde"])]
    p = subprocess.run([sys.executable, "-I", "-B", str(COMMANDE)] + a, input=b"Consigne d'essai.", env=env, capture_output=True,
                       timeout=90)
    return p.returncode, json.loads(p.stdout.decode().splitlines()[-1])


@pytest.mark.parametrize("role,plafond", [("juge_ideation", "1.00"), ("proposeur_ideation", "3.00")])
def test_argon_cas_sain_juge_et_proposeur(pieces, role, plafond):
    amont = FauxAmont(modele="gemini-4-argon")
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont), plafond=plafond, role=role)
    assert code == 0, ligne
    assert amont.corps["generationConfig"] == {"maxOutputTokens": 45056, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}


def test_argon_juge_sous_l_ancien_plafond_de_0_60_refuse(pieces):
    amont = FauxAmont(modele="gemini-4-argon")
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont), plafond="0.60")
    assert code == 4 and amont.recues == 0


@pytest.mark.parametrize("modif,motif", [(("--max-sortie-jetons", "30000"), "jetons de texte"),        # plafond de sortie trop bas
                                         (("--niveau-reflexion", "xhigh"), "non admis"),               # niveau hors d'Argon
                                         (("--niveau-reflexion", "low"), "niveau envoyé")])
def test_argon_garde_avant_envoi(pieces, modif, motif):
    amont = FauxAmont(modele="gemini-4-argon")
    args = list(ARGS_ARGON)
    args[args.index(modif[0]) + 1] = modif[1]
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont), args=args)
    assert code == 2 and motif in ligne["erreur"] and amont.recues == 0


@pytest.mark.parametrize("amont_kw,defaut", [({"pensees": 0}, "SANS_PENSEES"), ({"fin": "MAX_TOKENS"}, "MAX_TOKENS")])
def test_argon_defauts_apres_reponse(pieces, amont_kw, defaut):
    amont = FauxAmont(modele="gemini-4-argon", **amont_kw)
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont))
    assert code == 5 and ligne["defaut_google"] == defaut and ligne["texte"] == ""


# --- v2 : hypothèse « réflexion comprise dans la sortie maximale » (constat 12) ---------------------------------------------------


def jouer_complet(pieces, url, args=None, plafond="3.00"):
    env = {"PATH": "/usr/bin:/bin", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": MODELE}
    a = (args if args is not None else ARGS) + ["--url-base", url + "/v1beta", "--garde", str(pieces["garde"])]
    p = subprocess.run([sys.executable, "-I", "-B", str(COMMANDE)] + a, input=b"Consigne d'essai.", env=env, capture_output=True,
                       timeout=90)
    return p.returncode, json.loads(p.stdout.decode().splitlines()[-1]), p.stderr.decode()


def test_v2_hypothese_tenue_au_plafond_exact(pieces):
    amont = FauxAmont(pensees=60000, sortie=5536)                                   # 65 536 : égal au plafond
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont))
    assert code == 0 and ligne["hypothese_sortie_maximale_tenue"] is True and "HYPOTHESE" not in err


def test_v2_hypothese_tombee_signalee_et_journalisee(pieces):
    amont = FauxAmont(pensees=60000, sortie=10000)                                  # 70 000 > 65 536
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont))
    assert code == 0 and ligne["texte"] == "réponse d'essai"                        # réponse gardée, coût lu compté
    assert ligne["hypothese_sortie_maximale_tenue"] is False
    assert ligne["cout_usd"] == pytest.approx((900 * 4 + 70000 * 20) / 1e6) and ligne["cout_usd"] > ligne["pire_cas_usd"]
    assert "HYPOTHESE_SORTIE_MAXIMALE_TOMBEE" in err and "65536" in err


def test_v2_hypothese_tombee_et_plafond_depasse_code_7(pieces):
    amont = FauxAmont(pensees=60000, sortie=10000)
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont), plafond="1.35")   # pire 1,3144 ≤ 1,35 < coût 1,4036
    assert code == 7 and ligne["hypothese_sortie_maximale_tenue"] is False and "HYPOTHESE_SORTIE_MAXIMALE_TOMBEE" in err


def test_v2_hypothese_non_ecrite_si_rien_n_est_parti(pieces):
    amont = FauxAmont()
    code, ligne, err = jouer_complet(pieces, relais_devant(pieces, amont), plafond="1.00")   # pire cas > 1,00 : rien envoyé
    assert code == 4 and "hypothese_sortie_maximale_tenue" not in ligne and amont.recues == 0


def test_v2_argon_juge_aux_reglages_de_production(pieces):
    amont = FauxAmont(modele="gemini-4-argon")
    code, ligne = jouer_argon(pieces, relais_argon(pieces, amont))                  # plafond 1,00, juge
    assert code == 0 and ligne["pire_cas_usd"] <= 1.00 and ligne["prix"] == {"entree": 4.0, "sortie": 20.0}
