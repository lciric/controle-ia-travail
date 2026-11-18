"""Essais de commande_astra_v1.py (commande externe de GPT-6 Astra, copie de la commande Kimi v1) devant un **faux relais
local** compatible OpenAI (`http.server` dans un fil, port libre choisi par le système) — aucune clé, aucun appel réseau
hors de la boucle locale, aucune dépense. Écrits le 18 novembre 2026 (R5 : cas sain et artefacts).

Cas sain : code 0, texte rendu, coût = prompt_tokens × 10e-6 + completion_tokens × 50e-6, `modele_servi` égal, champ `prix`
présent, le corps reçu porte `max_completion_tokens` et pas `max_tokens`, `model` égal au modèle ; les deux rôles ; la garde
du pire cas recalculée sur le corps reçu. Artefacts : `MODELE_DEMANDE_POLE` différent (code 2, aucun appel), `ROLE_POLE`
hors des deux rôles (2), `PLAFOND_SESSION_USD` absent (2), consigne vide (2), plafond minuscule (4, aucun appel), relais
injoignable (3, rien envoyé), `finish_reason` `length` (5), modèle servi différent (5), usage absent (5), réponse illisible
(5), réponse vide (5), HTTP 429 du relais (3, coût plancher), HTTP 502 (5, coût pire cas), relais trop lent (6, pire cas).
Chaque essai lit la **dernière ligne** de la sortie standard comme JSON (`texte`, `cout_usd` fini et > 0). Les commandes
tournent dans un processus à part (`python3 -I -B`) avec un environnement explicite minimal, jamais celui de la session.

Trois essais sont marqués `xfail` (strict) : ils révèlent des défauts de la commande (hérités de la commande Kimi v1), non
corrigés ici — l'en-tête du fichier qui contient une copie de code (la docstring n'est pas fermée après la ligne d'usage),
un prix de sortie nul ou non fini qui fait planter la commande sans ligne JSON, un prix négatif accepté par la garde.
Lancement :

    cd docs/notes/ideation-organisme-v1/relais-kimi-v1 && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \\
        -p no:cacheprovider test_commande_astra_v1.py
"""

import ast
import difflib
import http.server
import json
import math
import os
import socket
import subprocess
import sys
import threading
import time

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
ASTRA = os.path.join(ICI, "commande_astra_v1.py")
KIMI = os.path.join(ICI, "commande_kimi_v1.py")
MODELE = "gpt-6-astra"
PRIX_E, PRIX_S = 10.0, 50.0  # défauts de la commande (USD par million de jetons)
ROLES = ("proposeur_ideation", "juge_ideation")
CONSIGNE = "Juge la fiche suivante selon la grille du pôle, puis rends ton verdict.\n" * 12
TEXTE = "Verdict factice d'Astra : la fiche tient.\nDeuxième ligne, avec des accents : été, cœur."
USAGE = {"prompt_tokens": 1234, "completion_tokens": 567, "total_tokens": 1801,
         "completion_tokens_details": {"reasoning_tokens": 400}}


# --- faux relais ---------------------------------------------------------------------------------------------------------

class FauxRelais:
    """Un scénario par instance ; chaque requête reçue est gardée (chemin, en-têtes, corps brut et JSON si lisible)."""

    def __init__(self, scenario="sain", modele_servi=MODELE, usage=USAGE, texte=TEXTE, lenteur_s=0.0):
        self.recus = []
        relais = self

        class Gestionnaire(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.0"

            def log_message(self, *_):  # silence
                pass

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                brut = self.rfile.read(n)
                try:
                    corps = json.loads(brut)
                except ValueError:
                    corps = None
                relais.recus.append({"chemin": self.path, "en_tetes": dict(self.headers), "brut": brut, "corps": corps})
                if lenteur_s:
                    time.sleep(lenteur_s)
                if scenario == "http429":
                    return self._repondre(429, b'{"error": {"message": "plafond du relais atteint (factice)"}}')
                if scenario == "http502":
                    return self._repondre(502, b'{"error": {"message": "modele servi hors liste (factice)"}}')
                if scenario == "illisible":
                    return self._repondre(200, b"pas du JSON {")
                if scenario == "choix_vides":
                    return self._repondre(200, json.dumps({"choices": [], "model": modele_servi}).encode("utf-8"))
                reponse = {"id": "chatcmpl-factice", "object": "chat.completion", "created": 1_800_000_000,
                           "model": modele_servi,
                           "choices": [{"index": 0, "message": {"role": "assistant", "content": texte},
                                        "finish_reason": "length" if scenario == "longueur" else "stop"}]}
                if scenario != "sans_usage":
                    reponse["usage"] = usage
                self._repondre(200, json.dumps(reponse, ensure_ascii=False).encode("utf-8"))

            def _repondre(self, code, octets):
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(octets)))
                self.end_headers()
                self.wfile.write(octets)

        self.serveur = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)  # port libre choisi par le système
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"
        self.fil = threading.Thread(target=self.serveur.serve_forever, daemon=True)
        self.fil.start()

    def arreter(self):
        self.serveur.shutdown()
        self.serveur.server_close()
        self.fil.join(timeout=5)


@pytest.fixture
def relais():
    lances = []

    def lancer(scenario="sain", **params):
        r = FauxRelais(scenario, **params)
        lances.append(r)
        return r

    yield lancer
    for r in lances:
        r.arreter()


def port_ferme():
    """Un port de la boucle locale sur lequel rien n'écoute (lié puis relâché)."""
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


# --- lancement de la commande ---------------------------------------------------------------------------------------------

def lancer(url, *options, plafond="3", role="juge_ideation", demande=MODELE, consigne=CONSIGNE, script=ASTRA):
    """Processus à part, interpréteur isolé, environnement explicite minimal (jamais celui de la session : aucune clé).
    `plafond`, `role` ou `demande` à None : la variable est absente."""
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": role,
           "MODELE_DEMANDE_POLE": demande}
    env = {k: v for k, v in env.items() if v is not None}
    r = subprocess.run([sys.executable, "-I", "-B", script, "--url-relais", url, *options],
                       input=consigne.encode("utf-8"), capture_output=True, env=env, timeout=60)
    sortie = r.stdout.decode("utf-8")
    lignes = sortie.splitlines()
    assert lignes, (r.returncode, r.stderr.decode("utf-8", "replace"))
    objet = json.loads(lignes[-1])  # la dernière ligne de la sortie standard est l'objet rendu
    assert "texte" in objet and isinstance(objet["texte"], str)
    assert isinstance(objet["cout_usd"], (int, float)) and math.isfinite(objet["cout_usd"]) and objet["cout_usd"] > 0
    assert objet["version"] == "commande-astra-v1"
    return r.returncode, objet, sortie, r.stderr.decode("utf-8", "replace")


def cout_attendu(usage=USAGE, pe=PRIX_E, ps=PRIX_S):
    return usage["prompt_tokens"] * pe / 1e6 + usage["completion_tokens"] * ps / 1e6


def n_permis(octets, plafond, pe=PRIX_E, ps=PRIX_S, maxi=32768):
    """La borne de sortie que paie le plafond après le pire cas d'entrée (formule de l'en-tête de la commande Kimi v1)."""
    reste = plafond - (octets + 1024) * pe / 1e6
    return min(maxi, int(reste * 1e6 / ps)) if reste > 0 else 0


# --- cas sain ------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("role", ROLES)
def test_sain_code_0_texte_cout_et_corps(relais, role):
    r = relais()
    code, obj, sortie, erreurs = lancer(r.url, role=role)
    assert code == 0, obj.get("erreur")
    assert obj["texte"] == TEXTE and obj["envoye"] is True and obj["cout_origine"] == "usage"
    assert obj["cout_usd"] == pytest.approx(cout_attendu(), abs=5e-7)  # 1234 × 10e-6 + 567 × 50e-6 = 0,04069
    assert obj["cout_usd"] == pytest.approx(0.04069, abs=5e-7)
    assert obj["modele_servi"] == obj["modele_demande"] == MODELE and obj["finish_reason"] == "stop"
    assert obj["prix"] == {"entree_usd_par_million": 10.0, "sortie_usd_par_million": 50.0}
    assert obj["usage"] == {"prompt_tokens": 1234, "completion_tokens": 567, "total_tokens": 1801}  # champs numériques
    assert "erreur" not in obj and erreurs == ""
    # ce que le faux relais a reçu : une seule requête, au bon chemin, le corps compatible OpenAI
    assert len(r.recus) == 1
    recu = r.recus[0]
    assert recu["chemin"] == "/v1/chat/completions" and recu["en_tetes"]["Content-Type"] == "application/json"
    corps = recu["corps"]
    assert set(corps) == {"model", "messages", "max_completion_tokens"}
    assert "max_tokens" not in corps and "max_tokens" not in recu["brut"].decode("utf-8")
    assert corps["model"] == MODELE
    assert corps["messages"] == [{"role": "user", "content": CONSIGNE}]  # la consigne part telle quelle
    assert corps["max_completion_tokens"] == obj["max_completion_tokens"] == 32768  # le plafond de 3 USD paie le maximum
    assert len(recu["brut"]) == obj["octets_corps"] == int(recu["en_tetes"]["Content-Length"])
    assert "Authorization" not in recu["en_tetes"]  # aucune clé ici : le relais la tient
    assert obj["pire_cas_usd"] == pytest.approx((obj["octets_corps"] + 1024) * PRIX_E / 1e6 + 32768 * PRIX_S / 1e6, abs=5e-7)
    assert obj["pire_cas_usd"] <= 3 and obj["cout_usd"] <= obj["pire_cas_usd"]
    assert len([l for l in sortie.splitlines() if l.strip()]) == 1


def test_sain_la_derniere_ligne_est_du_json_lisible_par_splitlines(relais):
    """Le texte rendu garde ses retours à la ligne échappés dans le JSON : la sortie ne fait qu'une ligne."""
    r = relais(texte="ligne 1\nligne 2\n\nligne 4")
    code, obj, sortie, _ = lancer(r.url)
    assert code == 0 and obj["texte"] == "ligne 1\nligne 2\n\nligne 4"
    assert sortie.count("\n") == 1 and json.loads(sortie.splitlines()[-1]) == obj


def test_sain_plafond_serre_borne_la_sortie_par_le_corps_recu(relais):
    """Plafond 1 USD : la borne de sortie est ce que le reste paie, recalculée ici sur le corps reçu par le relais ; le pire
    cas reste sous le plafond et le coût rendu sous le pire cas."""
    r = relais()
    code, obj, _, _ = lancer(r.url, plafond="1")
    assert code == 0
    octets = len(r.recus[0]["brut"])
    n = n_permis(octets, 1.0)
    assert 4096 <= n < 32768 and r.recus[0]["corps"]["max_completion_tokens"] == obj["max_completion_tokens"] == n
    assert obj["pire_cas_usd"] == pytest.approx((octets + 1024) * PRIX_E / 1e6 + n * PRIX_S / 1e6, abs=5e-7)
    assert obj["cout_usd"] <= obj["pire_cas_usd"] <= 1


def test_sain_prix_regles_par_les_options_comptes_et_rendus(relais):
    r = relais()
    code, obj, _, _ = lancer(r.url, "--prix-entree", "2.5", "--prix-sortie", "20")
    assert code == 0
    assert obj["cout_usd"] == pytest.approx(cout_attendu(pe=2.5, ps=20), abs=5e-7)
    assert obj["prix"] == {"entree_usd_par_million": 2.5, "sortie_usd_par_million": 20.0}


def test_sain_modele_regle_par_l_option_demande_egal_et_servi(relais):
    r = relais(modele_servi="gpt-6-astra-mini")
    code, obj, _, _ = lancer(r.url, "--modele", "gpt-6-astra-mini", demande="gpt-6-astra-mini")
    assert code == 0 and obj["modele_demande"] == obj["modele_servi"] == "gpt-6-astra-mini"
    assert r.recus[0]["corps"]["model"] == "gpt-6-astra-mini"


def test_sain_variable_du_modele_absente_rien_ne_change(relais):
    r = relais()
    code, obj, _, _ = lancer(r.url, demande=None)
    assert code == 0 and obj["modele_demande"] == MODELE and len(r.recus) == 1


# --- artefacts : refus avant tout envoi (code 2 et 4) -----------------------------------------------------------------------

def test_modele_demande_different_code_2_sans_appel(relais):
    r = relais()
    code, obj, _, _ = lancer(r.url, demande="gpt-5-autre")
    assert code == 2 and obj["envoye"] is False and obj["texte"] == "" and obj["cout_usd"] == 1e-6
    assert "MODELE_DEMANDE_POLE" in obj["erreur"] and "'gpt-5-autre'" in obj["erreur"] and f"'{MODELE}'" in obj["erreur"]
    assert r.recus == []
    code, obj, _, _ = lancer(r.url, "--modele", "gpt-6-astra-mini", demande=MODELE)  # l'option diffère de la demande
    assert code == 2 and obj["envoye"] is False and r.recus == []


@pytest.mark.parametrize("role", ["juge", "proposeur", "", None])
def test_role_hors_des_deux_roles_code_2(relais, role):
    r = relais()
    code, obj, _, _ = lancer(r.url, role=role)
    assert code == 2 and obj["envoye"] is False and obj["cout_usd"] == 1e-6
    assert "ROLE_POLE" in obj["erreur"] and "proposeur_ideation" in obj["erreur"] and "juge_ideation" in obj["erreur"]
    assert r.recus == []


@pytest.mark.parametrize("plafond", [None, "", "abc", "0", "-1", "nan", "inf"])
def test_plafond_absent_ou_invalide_code_2(relais, plafond):
    r = relais()
    code, obj, _, _ = lancer(r.url, plafond=plafond)
    assert code == 2 and obj["envoye"] is False and obj["cout_usd"] == 1e-6 and r.recus == []
    if plafond in ("", "abc"):  # valeur non numérique : c'est l'erreur de float() qui est rendue (la variable n'est pas nommée)
        assert "could not convert string to float" in obj["erreur"]
    else:
        assert "PLAFOND_SESSION_USD" in obj["erreur"]


@pytest.mark.parametrize("consigne", ["", "   \n\t\n"])
def test_consigne_vide_code_2(relais, consigne):
    r = relais()
    code, obj, _, _ = lancer(r.url, consigne=consigne)
    assert code == 2 and obj["envoye"] is False and "consigne vide" in obj["erreur"] and r.recus == []


@pytest.mark.parametrize("url", ["https://api.openai.com", "http://exemple.org:8790", "http://127.0.0.1:8790/v1"])
def test_adresse_hors_de_la_boucle_locale_code_2(relais, url):
    code, obj, _, _ = lancer(url)
    assert code == 2 and obj["envoye"] is False and "--url-relais" in obj["erreur"]


def test_pire_cas_au_dessus_du_plafond_code_4_sans_appel(relais):
    r = relais()
    code, obj, _, _ = lancer(r.url, plafond="0.01")  # le minimum de sortie (4 096 × 50e-6 = 0,2048 USD) ne tient pas
    assert code == 4 and obj["envoye"] is False and obj["texte"] == "" and obj["cout_usd"] == 1e-6
    assert "pire cas au-dessus du plafond" in obj["erreur"] and "0.01" in obj["erreur"]
    assert r.recus == []
    # bord : le plus petit plafond qui paie le minimum de sortie passe ; un peu moins ne passe pas
    octets = len(json.dumps({"model": MODELE, "messages": [{"role": "user", "content": CONSIGNE}],
                             "max_completion_tokens": 4096}, ensure_ascii=False).encode("utf-8"))
    bord = (octets + 1024) * PRIX_E / 1e6 + 4096 * PRIX_S / 1e6
    # (+ 1e-5 : le premier tour du point fixe mesure un corps d'un octet de plus, écrit avec 32768 et non 4096)
    code, obj, _, _ = lancer(r.url, plafond=repr(bord + 1e-5 + 1e-6))
    assert code == 0 and obj["max_completion_tokens"] == 4096 and len(r.recus) == 1
    assert obj["pire_cas_usd"] == pytest.approx(bord, abs=5e-7)
    code, obj, _, _ = lancer(r.url, plafond=repr(bord - 1e-4))
    assert code == 4 and len(r.recus) == 1


def test_sortie_minimale_reglable_change_le_refus(relais):
    r = relais()
    assert lancer(r.url, plafond="0.1")[0] == 4
    code, obj, _, _ = lancer(r.url, "--sortie-min-jetons", "512", plafond="0.1")
    assert code == 0 and 512 <= obj["max_completion_tokens"] < 4096


# --- artefacts : relais et amont (code 3, 5, 6) ---------------------------------------------------------------------------

def test_relais_injoignable_code_3_rien_envoye():
    code, obj, _, _ = lancer(f"http://127.0.0.1:{port_ferme()}")
    assert code == 3 and obj["envoye"] is False and obj["texte"] == ""
    assert obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert "injoignable" in obj["erreur"]
    assert obj["pire_cas_usd"] > 0 and obj["max_completion_tokens"] == 32768  # le diagnostic de la garde est rendu


def test_reponse_tronquee_finish_reason_length_code_5(relais):
    r = relais("longueur")
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["envoye"] is True
    assert "tronquée" in obj["erreur"] and "length" in obj["erreur"] and obj["finish_reason"] == "length"
    assert obj["cout_usd"] == pytest.approx(cout_attendu(), abs=5e-7) and obj["cout_origine"] == "usage"


def test_modele_servi_different_code_5(relais):
    r = relais(modele_servi="gpt-5-autre")
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["envoye"] is True
    assert obj["modele_servi"] == "gpt-5-autre" and "'gpt-5-autre'" in obj["erreur"] and f"'{MODELE}'" in obj["erreur"]
    assert obj["cout_usd"] == pytest.approx(cout_attendu(), abs=5e-7)  # l'usage lu est compté quand même


@pytest.mark.parametrize("usage", [None, {}, {"prompt_tokens": 10}, {"prompt_tokens": "10", "completion_tokens": 5},
                                   {"prompt_tokens": True, "completion_tokens": 5}, {"prompt_tokens": -1, "completion_tokens": 5},
                                   {"prompt_tokens": 1.5, "completion_tokens": 5}])
def test_usage_absent_ou_mal_forme_code_5_cout_pire_cas(relais, usage):
    r = relais("sans_usage") if usage is None else relais(usage=usage)
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["envoye"] is True
    assert obj["erreur"] == "usage absent" and obj["cout_origine"] == "pire_cas"
    assert obj["cout_usd"] == obj["pire_cas_usd"] > 1  # 32 768 jetons de sortie au prix de sortie : jamais sous-estimé


@pytest.mark.parametrize("scenario", ["illisible", "choix_vides"])
def test_reponse_illisible_code_5_cout_pire_cas(relais, scenario):
    r = relais(scenario)
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["envoye"] is True
    assert obj["erreur"] == "réponse illisible" and obj["cout_origine"] == "pire_cas"
    assert obj["cout_usd"] == obj["pire_cas_usd"] > 1


def test_reponse_vide_code_5(relais):
    r = relais(texte="  \n ")
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["erreur"] == "réponse vide"
    assert obj["cout_usd"] == pytest.approx(cout_attendu(), abs=5e-7)


def test_http_429_du_relais_code_3_cout_plancher(relais):
    r = relais("http429")
    code, obj, _, _ = lancer(r.url)
    assert code == 3 and obj["texte"] == "" and obj["envoye"] is False
    assert obj["cout_usd"] == 1e-6 and obj["cout_origine"] == "plancher"
    assert obj["erreur"].startswith("HTTP 429") and "plafond du relais" in obj["erreur"]
    assert len(r.recus) == 1  # une seule tentative, aucune relance


def test_http_502_du_relais_code_5_cout_pire_cas(relais):
    r = relais("http502")
    code, obj, _, _ = lancer(r.url)
    assert code == 5 and obj["texte"] == "" and obj["envoye"] is True
    assert obj["cout_usd"] == obj["pire_cas_usd"] > 1 and obj["cout_origine"] == "pire_cas"
    assert obj["erreur"].startswith("HTTP 502") and len(r.recus) == 1


def test_relais_trop_lent_code_6_cout_pire_cas(relais):
    r = relais(lenteur_s=2.0)
    code, obj, _, _ = lancer(r.url, "--delai-s", "0.5")
    assert code == 6 and obj["texte"] == "" and obj["envoye"] is True
    assert obj["cout_usd"] == obj["pire_cas_usd"] and obj["cout_origine"] == "pire_cas"
    assert "timed out" in obj["erreur"]


# --- la source : copie de la commande Kimi v1, avec les seuls changements annoncés --------------------------------------------

def test_code_ne_differe_de_la_commande_kimi_v1_que_par_les_changements_annonces():
    """Après le dernier `import argparse` (le code), les seules différences : VERSION et ROLES, les quatre défauts (relais,
    modèle, prix), `max_tokens` → `max_completion_tokens` dans le corps (deux lignes), et le diagnostic (`prix` ajouté)."""
    k = open(KIMI, encoding="utf-8").read().splitlines()
    a = open(ASTRA, encoding="utf-8").read().splitlines()
    k = k[max(i for i, l in enumerate(k) if l == "import argparse"):]
    a = a[max(i for i, l in enumerate(a) if l == "import argparse"):]
    ops = [op for op in difflib.SequenceMatcher(None, k, a, autojunk=False).get_opcodes() if op[0] != "equal"]
    assert len(ops) == 5, ops
    assert all(op[0] == "replace" for op in ops)
    (_, i1, i2, j1, j2) = ops[0]
    assert k[i1:i2] == ['VERSION = "commande-kimi-v1"', 'ROLES = ("juge_ideation",)']
    assert a[j1:j2] == ['VERSION = "commande-astra-v1"', 'ROLES = ("proposeur_ideation", "juge_ideation")']
    (_, i1, i2, j1, j2) = ops[1]
    assert [l.strip() for l in a[j1:j2]] == ['a.add_argument("--url-relais", default="http://127.0.0.1:8790")',
                                             'a.add_argument("--modele", default="gpt-6-astra")',
                                             'a.add_argument("--prix-entree", type=float, default=10.0)',
                                             'a.add_argument("--prix-sortie", type=float, default=50.0)']
    assert [l.replace("8789", "8790").replace("kimi-k3.1-pro", "gpt-6-astra").replace("default=2.0", "default=10.0")
            .replace("default=10.0)", "default=50.0)") if "prix-sortie" in l else
            l.replace("8789", "8790").replace("kimi-k3.1-pro", "gpt-6-astra").replace("default=2.0", "default=10.0")
            for l in k[i1:i2]] == a[j1:j2]
    for (_, i1, i2, j1, j2) in ops[2:4]:
        assert i2 - i1 == j2 - j1 == 1 and k[i1].replace('"max_tokens"', '"max_completion_tokens"') == a[j1] != k[i1]
    (_, i1, i2, j1, j2) = ops[4]
    assert i2 - i1 == 1 and j2 - j1 == 2 and k[i1].strip().startswith('diag = {"max_tokens": n,')
    assert a[j1].strip().startswith('diag = {"max_completion_tokens": n,') and '"prix": {' in a[j1 + 1]
    assert '"entree_usd_par_million": args.prix_entree' in a[j1 + 1] and '"sortie_usd_par_million": args.prix_sortie' in a[j1 + 1]
    assert '"max_tokens"' not in "\n".join(a)  # plus aucune trace de l'ancien champ dans le code


def test_aide_et_option_inconnue_la_derniere_ligne_reste_du_json():
    """L'aide se construit (la première ligne de la docstring sert de description) et nomme les réglages ; SystemExit
    d'argparse est pris : même sur --help ou une option inconnue, la dernière ligne est l'objet JSON, code 2."""
    r = subprocess.run([sys.executable, "-I", "-B", ASTRA, "--help"], capture_output=True, env={"PATH": "/usr/bin:/bin"},
                       timeout=30)
    aide = r.stdout.decode("utf-8")
    assert "GPT-6 Astra" in aide and "--prix-entree" in aide and "--max-sortie-jetons" in aide and "--delai-s" in aide
    assert r.returncode == 2 and json.loads(aide.splitlines()[-1])["envoye"] is False
    code, obj, _, _ = lancer("http://127.0.0.1:1", "--option-inconnue")
    assert code == 2 and obj["envoye"] is False and obj["cout_usd"] == 1e-6


# --- défauts de la commande révélés par les essais (xfail strict : à retirer quand la commande est corrigée) ----------------

@pytest.mark.xfail(strict=True, reason="défaut de forme de commande_astra_v1.py : la docstring du module n'est pas fermée "
                   "après la ligne d'usage (ligne 37) ; elle court jusqu'au premier \"\"\" du fichier (ligne 80, en tête d'une "
                   "copie tronquée de max_tokens_permis), si bien que les lignes 39 à 80 — une copie des imports, de VERSION, "
                   "ROLES, PLANCHER, rendre, lire_arguments, verifier_url et de l'amorce de max_tokens_permis — sont du texte "
                   "d'en-tête ; le code réel suit (ligne 82) et tourne ; correction : fermer la docstring après la ligne 37 et "
                   "supprimer les lignes 39 à 81")
def test_en_tete_du_fichier_sans_copie_de_code():
    source = open(ASTRA, encoding="utf-8").read()
    doc = ast.get_docstring(ast.parse(source), clean=False)
    assert doc.rstrip().endswith("[--delai-s 1500]")  # l'en-tête finit sur la ligne d'usage
    assert "import argparse" not in doc and "def rendre(" not in doc and "def max_tokens_permis(" not in doc
    assert source.count("import argparse") == 1 and source.count("def max_tokens_permis(") == 1


@pytest.mark.xfail(strict=True, reason="défaut de commande_astra_v1.py (hérité de la commande Kimi v1) : les prix ne sont "
                   "pas vérifiés ; --prix-sortie 0 lève ZeroDivisionError et --prix-sortie nan lève ValueError dans "
                   "max_tokens_permis (int(reste * 1e6 / ps)), hors de tout try : trace sur la sortie d'erreur, code 1, AUCUNE "
                   "ligne JSON sur la sortie standard, contrat de la dernière ligne rompu ; correction : dans le try de main, "
                   "refuser (ValueError → code 2) tout prix qui n'est pas un réel fini strictement positif")
@pytest.mark.parametrize("prix", ["0", "nan"])
def test_prix_de_sortie_nul_ou_non_fini_code_2_et_ligne_json(relais, prix):
    r = relais()
    code, obj, _, _ = lancer(r.url, "--prix-sortie", prix)  # `lancer` exige une dernière ligne JSON
    assert code == 2 and obj["envoye"] is False and r.recus == []


@pytest.mark.xfail(strict=True, reason="défaut de commande_astra_v1.py (hérité de la commande Kimi v1) : un prix négatif ou "
                   "nul d'entrée est accepté ; --prix-entree -1 passe la garde avec un pire cas sous-estimé (le coût d'entrée "
                   "retranché) et rend le champ prix négatif ; --prix-entree 0 et --prix-sortie -1 de même ; correction : la "
                   "même vérification (réel fini strictement positif) sur les deux prix, code 2 sans envoi")
@pytest.mark.parametrize("options", [("--prix-entree", "-1"), ("--prix-entree", "0"), ("--prix-sortie", "-1")])
def test_prix_negatif_ou_nul_refuse_code_2(relais, options):
    r = relais()
    code, obj, _, _ = lancer(r.url, *options)
    assert code == 2 and obj["envoye"] is False and r.recus == []
