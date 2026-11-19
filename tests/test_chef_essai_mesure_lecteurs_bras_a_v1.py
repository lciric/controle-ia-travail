"""Essais du chef de l'essai de mesure des lecteurs du bras A (`scripts/chef_essai_mesure_lecteurs_bras_a_v1.py`) et du
générateur des textes synthétiques (`scripts/fabriquer_entrees_essai_mesure_v1.py`).

**Aucun appel payant, aucun réseau vers un fournisseur** : tout passe par un faux fournisseur local (boucle locale),
soit directement à la place du relais, soit derrière les vrais relais du dépôt lancés avec des clés factices
(`--amont http://127.0.0.1:…`). Chaque garde a son cas sain et son artefact (R5).
"""
import copy
import hashlib
import importlib.util
import json
import os
import re
import signal
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def _charger(nom):
    spec = importlib.util.spec_from_file_location(nom, RACINE / "scripts" / f"{nom}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


chef = _charger("chef_essai_mesure_lecteurs_bras_a_v1")
gen = _charger("fabriquer_entrees_essai_mesure_v1")

CONFIG = chef.charger_configuration(RACINE / chef.CONFIGURATION, chef.EMPREINTE_CONFIGURATION)
LOT = chef.charger_textes(CONFIG, RACINE)
INTERDITS = ["nom-de-personne-factice", "projet-factice", "session_factice_0123456789"]
CLE_FACTICE = "cle-factice-des-essais"


# --- faux fournisseur local ----------------------------------------------------------------------------------------------

def texte_conforme(consigne: str) -> str:
    """Réponse de forme exigée pour la consigne reçue (appariement ou couverture)."""
    if consigne.startswith("You will read one entry"):
        return json.dumps({"fit": "answers", "specific": True, "proposal_quote": "We fine-tune a model on some data",
                           "controls_quote": "Run it again with five random seeds"})
    ids = re.findall(r"^- id: (c\d+) \|", consigne, re.M)
    return json.dumps({i: {"content": "absent", "quote": None, "place": None} for i in ids})


class FauxFournisseur:
    """Sert les trois formes d'appel (Anthropic, Google, OpenAI), en flux ou entières, selon un scénario : une fonction
    (rang de la requête, requête) -> dict de comportement. Garde tout ce qu'il reçoit."""

    def __init__(self, scenario=None):
        self.scenario = scenario or (lambda rang, requete: {})
        self.recus = []
        faux = self

        class Gestionnaire(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def _envoyer(self, code, corps: bytes, genre="application/json"):
                self.send_response(code)
                self.send_header("Content-Type", genre)
                self.send_header("Content-Length", str(len(corps)))
                self.send_header("Connection", "close")
                self.end_headers()
                self.wfile.write(corps)
                self.close_connection = True

            def do_POST(self):
                longueur = int(self.headers.get("content-length") or 0)
                brut = self.rfile.read(longueur)
                corps = json.loads(brut.decode("utf-8"))
                requete = {"chemin": self.path, "en_tetes": {k.lower(): v for k, v in self.headers.items()}, "corps": corps,
                           "brut": brut}
                with faux._verrou:
                    rang = len(faux.recus)
                    faux.recus.append(requete)
                c = faux.scenario(rang, requete) or {}
                if c.get("muet"):
                    time.sleep(c["muet"])
                    return
                if "code" in c:
                    return self._envoyer(c["code"], json.dumps(c.get("corps", {"error": {"message": "refus du faux"}})).encode())
                if self.path.startswith("/v1/messages"):
                    return self._anthropic(corps, c)
                if self.path.startswith("/v1beta/models/"):
                    return self._google(corps, c)
                return self._openai(corps, c)

            def _anthropic(self, corps, c):
                consigne = corps["messages"][0]["content"]
                texte = c.get("texte", texte_conforme(consigne))
                modele = c.get("modele", corps["model"])
                sortie = c.get("sortie", 300)
                fin = c.get("fin", "end_turn")
                evenements = [
                    {"type": "message_start", "message": {"id": "msg_faux", "type": "message", "role": "assistant",
                                                          "model": modele, "content": [], "stop_reason": None,
                                                          "usage": {"input_tokens": len(consigne) // 4, "output_tokens": 1}}},
                    {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": "", "signature": ""}},
                    {"type": "content_block_stop", "index": 0},
                    {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}},
                    {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": texte[:len(texte) // 2]}},
                    {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": texte[len(texte) // 2:]}},
                    {"type": "content_block_stop", "index": 1}]
                if not c.get("sans_usage"):
                    evenements += [{"type": "message_delta", "delta": {"stop_reason": fin, "stop_sequence": None},
                                    "usage": {"output_tokens": sortie}}, {"type": "message_stop"}]
                if corps.get("stream"):
                    flux = "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in evenements).encode()
                    return self._envoyer(200, flux, "text/event-stream")
                entier = {"id": "msg_faux", "type": "message", "role": "assistant", "model": modele, "stop_reason": fin,
                          "content": [{"type": "text", "text": texte}],
                          "usage": {"input_tokens": len(consigne) // 4, "output_tokens": sortie}}
                return self._envoyer(200, json.dumps(entier).encode())

            def _google(self, corps, c):
                consigne = corps["contents"][0]["parts"][0]["text"]
                modele = c.get("modele", re.search(r"/models/([^:]+):", self.path).group(1))
                budget = corps["generationConfig"]["thinkingConfig"]["thinkingBudget"]
                usage = {"promptTokenCount": len(consigne) // 4, "candidatesTokenCount": c.get("sortie", 200),
                         "thoughtsTokenCount": c.get("reflexion", min(budget, 500)), "totalTokenCount": 0}
                candidat = {"index": 0, "content": {"role": "model", "parts": [{"text": c.get("texte", texte_conforme(consigne))}]},
                            "finishReason": c.get("fin", "STOP")}
                entier = {"candidates": [candidat], "modelVersion": modele}
                if not c.get("sans_usage"):
                    entier["usageMetadata"] = usage
                if "streamGenerateContent" in self.path:
                    moitie = dict(entier, candidates=[{"index": 0, "content": {"role": "model", "parts": [{"text": ""}]}}])
                    moitie.pop("usageMetadata", None)
                    flux = "".join(f"data: {json.dumps(m)}\r\n\r\n" for m in (moitie, entier)).encode()
                    return self._envoyer(200, flux, "text/event-stream")
                return self._envoyer(200, json.dumps(entier).encode())

            def _openai(self, corps, c):
                consigne = corps["messages"][0]["content"]
                modele = c.get("modele", corps["model"])
                texte = c.get("texte", texte_conforme(consigne))
                usage = {"prompt_tokens": len(consigne) // 4, "completion_tokens": c.get("sortie", 400), "total_tokens": 0,
                         "completion_tokens_details": {"reasoning_tokens": c.get("reflexion", 250)}}
                fin = c.get("fin", "stop")
                if corps.get("stream"):
                    morceaux = [{"id": "c_faux", "model": modele, "choices": [{"index": 0, "delta": {"role": "assistant", "content": texte}, "finish_reason": None}]},
                                {"id": "c_faux", "model": modele, "choices": [{"index": 0, "delta": {}, "finish_reason": fin}]}]
                    if not c.get("sans_usage"):
                        morceaux.append({"id": "c_faux", "model": modele, "choices": [], "usage": usage})
                    flux = "".join(f"data: {json.dumps(m)}\n\n" for m in morceaux).encode() + b"data: [DONE]\n\n"
                    return self._envoyer(200, flux, "text/event-stream")
                entier = {"id": "c_faux", "model": modele,
                          "choices": [{"index": 0, "message": {"role": "assistant", "content": texte, "refusal": c.get("refus")},
                                       "finish_reason": fin}]}
                if not c.get("sans_usage"):
                    entier["usage"] = usage
                return self._envoyer(200, json.dumps(entier).encode())

        self._verrou = threading.Lock()
        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)
        self.serveur.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


@pytest.fixture
def faux():
    serveurs = []

    def fabriquer(scenario=None):
        f = FauxFournisseur(scenario)
        serveurs.append(f)
        return f

    yield fabriquer
    for f in serveurs:
        f.fermer()


def jouer(tmp_path, nom, faux_fournisseur, modifs=None, interdits=None):
    """Joue une file directement contre le faux fournisseur (à la place du relais). Rend bilan, journal, dossier."""
    config = copy.deepcopy(CONFIG)
    if modifs:
        modifs(config)
    dossier = tmp_path / f"course-{nom}"
    dossier.mkdir()
    bilan = chef.jouer_file(config, nom, LOT, dossier, faux_fournisseur.url, interdits if interdits is not None else INTERDITS)
    return bilan, chef.lire_journal(dossier / "journal-essai.jsonl"), dossier, config


def retours(journal):
    return [l for l in journal if l["evenement"] == "retour"]


def envois(journal):
    return [l for l in journal if l["evenement"] == "envoi"]


# --- générateur des textes (devis, section 4 ; R9) -----------------------------------------------------------------------

def test_generateur_deterministe_et_egal_au_lot_verse():
    prereg = (RACINE / gen.PREREG).read_text(encoding="utf-8")
    a, b = gen.fabriquer(prereg), gen.fabriquer(prereg)
    assert a == b
    verse = json.loads((RACINE / gen.SORTIE).read_text(encoding="utf-8"))
    refait = json.loads(json.dumps(a))
    # Seule la version de numpy inscrite peut différer d'un environnement à l'autre ; les textes, eux, sont les mêmes.
    assert {k: v for k, v in refait.items() if k != "numpy"} == {k: v for k, v in verse.items() if k != "numpy"}


def test_generateur_plan_des_24_entrees():
    lot = json.loads((RACINE / gen.SORTIE).read_text(encoding="utf-8"))
    app = [e for e in lot["entrees"] if e["instrument"] == "appariement"]
    couv = [e for e in lot["entrees"] if e["instrument"] == "couverture"]
    assert len(app) == 18 and len(couv) == 6 and len(lot["ordre"]) == 24
    for bloc in (1, 2, 3):
        du_bloc = [e for e in app if e["bloc"] == bloc]
        assert sorted(e["longueur"] for e in du_bloc) == sorted(gen.LONGUEURS * 2)
        assert sorted(e["cas"] for e in du_bloc) == sorted(gen.CAS * 2)
    assert {(e["longueur"], e["cas"]) for e in app} == {(l, c) for l in gen.LONGUEURS for c in gen.CAS}
    for e in app:
        bas, haut = gen.BORNES[e["longueur"]]
        assert bas <= e["caracteres"] <= haut <= 1800
    for bloc in (1, 2):
        assert sorted(e["longueur"] for e in couv if e["bloc"] == bloc) == sorted(gen.LONGUEURS)
    assert sorted(e["n_controles"] for e in couv) == [3, 3, 4, 4, 6, 6]
    for e in couv:
        assert len(e["caracteres_par_action"]) == 10 and max(e["caracteres_par_action"]) <= 1800
        ecrits = [c for c in e["construction"] if c["ecrit"]]
        assert len(ecrits) == (e["n_controles"] + 1) // 2
    assert sum(e["accolades"] for e in app) == 1 and sum(e["accolades"] for e in couv) == 1
    assert "{0.1, 0.3, 1.0}" in next(e for e in app if e["accolades"])["proposal"]
    assert lot["ordre"][:9] == [e["id"] for e in app if e["bloc"] == 1] + [e["id"] for e in couv if e["bloc"] == 1]
    assert all(e["graine"] == {"entropie": gen.ENTROPIE, "cle": [i + 1]} for i, e in enumerate(lot["entrees"]))


def test_generateur_refuse_d_ecraser(tmp_path):
    sortie = tmp_path / "lot.json"
    assert gen.principal(["--sortie", str(sortie)]) == 0
    assert gen.principal(["--sortie", str(sortie)]) == 2


def test_generateur_consigne_alteree_refusee():
    prereg = (RACINE / gen.PREREG).read_text(encoding="utf-8").replace("You will read one entry", "You will read an entry")
    with pytest.raises(SystemExit):
        gen.fabriquer(prereg)


def test_remplissage_garde_accolades_et_marques_intactes():
    consigne = "T: {title}\nP: {proposal}\nC: {controls}"
    rempli = chef.remplir(consigne, {"{title}": "a {proposal} b", "{proposal}": "{0.1, 0.3} et {controls}", "{controls}": "c"})
    assert rempli == "T: a {proposal} b\nP: {0.1, 0.3} et {controls}\nC: c"
    assert gen.remplir(consigne, {"{title}": "{controls}", "{proposal}": "p", "{controls}": "c"}) == "T: {controls}\nP: p\nC: c"


# --- configuration, pièces et consignes ----------------------------------------------------------------------------------

def test_configuration_saine_et_alteree(tmp_path):
    assert CONFIG["files"]["claude"]["go"] == "GO-2026-11-19-34"
    copie = tmp_path / "configuration.json"
    copie.write_bytes((RACINE / chef.CONFIGURATION).read_bytes() + b" ")
    with pytest.raises(chef.Arret, match="empreinte"):
        chef.charger_configuration(copie, chef.EMPREINTE_CONFIGURATION)
    with pytest.raises(chef.Arret, match="absente"):
        chef.charger_configuration(tmp_path / "absente.json", chef.EMPREINTE_CONFIGURATION)


def test_configuration_reprend_le_devis():
    f = CONFIG["files"]
    assert [r["nom"] for r in f["claude"]["reglages"]] == [
        "opus-5-5-effort-bas", "sonnet-5-5-effort-bas", "opus-5-5-effort-moyen", "sonnet-5-5-effort-moyen",
        "haiku-5-5-effort-bas"]
    assert (f["claude"]["plafond_usd"], f["carbon"]["plafond_usd"], f["gpt"]["plafond_usd"]) == (9.25, 6.0, 2.5)
    assert sum(m["plafond_usd"] for m in f["claude"]["modeles"].values()) == 9.25
    assert "claude-fable-5-2" not in f["claude"]["modeles"]
    assert "--sans-pensees-amont" in f["carbon"]["relais"]["arguments"]
    assert [r["budget_reflexion"] for r in f["carbon"]["reglages"]] == [1024, 2048]
    assert len(f["gpt"]["entrees"]) == 8 and sum(i.startswith("A-") for i in f["gpt"]["entrees"]) == 6
    assert f["claude"]["cle"]["attestation"]["sha256"].startswith("7ce262ba")
    assert CONFIG["devis"]["sha256"].startswith("533ad5b1")


def test_pieces_saines_et_empreinte_fausse():
    chef.verifier_piece(RACINE, CONFIG["entrees"], "lot")
    with pytest.raises(chef.Arret, match="empreinte"):
        chef.verifier_piece(RACINE, dict(CONFIG["entrees"], sha256="0" * 64), "lot")
    with pytest.raises(chef.Arret, match="absent"):
        chef.verifier_piece(RACINE, {"chemin": "absent.json", "sha256": "0" * 64}, "lot")


def test_consignes_extraites_et_alterees():
    prereg = (RACINE / CONFIG["prereg"]["chemin"]).read_text(encoding="utf-8")
    c = CONFIG["consignes"]["appariement"]
    bloc = chef.extraire_consigne(prereg, c["lignes"], c["sha256"], "appariement")
    assert bloc.startswith("You will read one entry") and bloc.endswith("CONTROLS: {controls}") and len(bloc) == 2700
    with pytest.raises(chef.Arret, match="empreinte"):
        chef.extraire_consigne(prereg.replace("FIT. Do the CONTROLS", "FIT. Do the controls"), c["lignes"], c["sha256"], "appariement")
    with pytest.raises(chef.Arret, match="clôtures"):
        chef.extraire_consigne("ligne\n" + prereg, c["lignes"], c["sha256"], "appariement")


def test_textes_charges_et_lot_altere(tmp_path):
    assert len(LOT["textes"]) == 24 and LOT["ordre"][0] == "A-b1-01"
    lot = json.loads((RACINE / CONFIG["entrees"]["chemin"]).read_text(encoding="utf-8"))
    lot["entrees"][0]["proposal"] += " One more sentence."
    faux_lot = tmp_path / "lot.json"
    faux_lot.write_text(json.dumps(lot), encoding="utf-8")
    config = copy.deepcopy(CONFIG)
    config["entrees"] = {"chemin": str(faux_lot), "sha256": hashlib.sha256(faux_lot.read_bytes()).hexdigest()}
    with pytest.raises(chef.Arret, match="consigne remplie"):
        chef.charger_textes(config, RACINE)


# --- G7 : ligne de calcul ------------------------------------------------------------------------------------------------

def ligne_go(identifiant="GO-2026-11-19-34", type_="calcul", plafond="9,25 USD", echeance="2026-11-20", devis=None):
    devis = CONFIG["devis"]["sha256"] if devis is None else devis
    return (f"| {identifiant} | 2026-11-19 | {type_} | essai de mesure, devis (`{devis}`) | {plafond} | {echeance} | "
            f"directeur | R-0000 |")


def test_g7_ligne_saine():
    env = {"GO_ID": "GO-2026-11-19-34"}
    assert len(chef.verifier_ligne_de_calcul(CONFIG, "claude", env, "# registre\n" + ligne_go(), "2026-11-19")) == 64
    assert chef.verifier_ligne_de_calcul(CONFIG, "claude", env, ligne_go(), "2026-11-20")


@pytest.mark.parametrize("env,registre,jour,motif", [
    ({}, ligne_go(), "2026-11-19", "GO_ID"),
    ({"GO_ID": "GO-2026-11-19-35"}, ligne_go(), "2026-11-19", "GO_ID"),
    ({"GO_ID": "GO-2026-11-19-34"}, "# registre vide", "2026-11-19", "0 ligne"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go() + "\n" + ligne_go(), "2026-11-19", "2 ligne"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go(type_="décision"), "2026-11-19", "calcul"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go(plafond="92,50 USD"), "2026-11-19", "plafond"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go(), "2026-11-21", "échue"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go(devis="0" * 64), "2026-11-19", "devis"),
    ({"GO_ID": "GO-2026-11-19-34"}, ligne_go() + "\n| GO-2026-11-20-01 | 2026-11-20 | révocation | GO-2026-11-19-34 | — | — | d | r |",
     "2026-11-19", "révoquée"),
])
def test_g7_artefacts(env, registre, jour, motif):
    with pytest.raises(chef.Arret, match=motif):
        chef.verifier_ligne_de_calcul(CONFIG, "claude", env, registre, jour)


def test_g7_lignes_reelles_de_la_branche_principale_si_presentes():
    try:
        registre = chef.lire_registre_git(RACINE, CONFIG)
    except chef.Arret:
        pytest.skip("origin/main absent de ce clone")
    for nom in chef.FILES:
        if f"| {CONFIG['files'][nom]['go']} |" not in registre:
            pytest.skip("lignes de calcul absentes de ce clone")
        assert chef.verifier_ligne_de_calcul(CONFIG, nom, {"GO_ID": CONFIG["files"][nom]["go"]}, registre, "2026-11-19")


# --- G8 : clé Claude vérifiée ----------------------------------------------------------------------------------------------

def file_claude_avec_releve(tmp_path, compagnon=True):
    releve = tmp_path / "releve.json"
    releve.write_text('{"code_http": 200}\n', encoding="utf-8")
    empreinte = hashlib.sha256(releve.read_bytes()).hexdigest()
    if compagnon:
        (tmp_path / "releve.json.sha256").write_text(f"{empreinte}  releve.json\n", encoding="utf-8")
    file = copy.deepcopy(CONFIG["files"]["claude"])
    file["cle"]["attestation"] = {"chemin": str(releve), "sha256": empreinte}
    return file, releve


def test_g8_sain_et_artefacts(tmp_path):
    file, releve = file_claude_avec_releve(tmp_path)
    variable = file["cle"]["variable"]
    chef.verifier_cle(file, {variable: CLE_FACTICE}, RACINE)
    for env in ({}, {variable: ""}):
        with pytest.raises(chef.Arret, match="absente ou vide"):
            chef.verifier_cle(file, env, RACINE)
    autre = copy.deepcopy(file)
    autre["cle"]["attestation"]["sha256"] = "0" * 64
    with pytest.raises(chef.Arret, match="empreinte autre"):
        chef.verifier_cle(autre, {variable: CLE_FACTICE}, RACINE)
    releve.unlink()
    with pytest.raises(chef.Arret, match="absent"):
        chef.verifier_cle(file, {variable: CLE_FACTICE}, RACINE)


def test_g8_sans_compagnon_refuse(tmp_path):
    file, _ = file_claude_avec_releve(tmp_path, compagnon=False)
    with pytest.raises(chef.Arret, match="compagnon"):
        chef.verifier_cle(file, {file["cle"]["variable"]: CLE_FACTICE}, RACINE)


def test_g8_ne_vise_pas_les_files_sans_attestation():
    chef.verifier_cle(CONFIG["files"]["gpt"], {}, RACINE)
    with pytest.raises(chef.Arret, match="absente ou vide"):
        chef.verifier_cle(CONFIG["files"]["carbon"], {}, RACINE)


# --- G5 : rien de personnel dans ce qui part -------------------------------------------------------------------------------

def test_g5_tous_les_corps_reels_passent():
    for nom in chef.FILES:
        prevu = chef.controler_tous_les_corps(CONFIG, nom, LOT, INTERDITS)
        assert prevu["appels"] == {"claude": 120, "carbon": 48, "gpt": 8}[nom]
        assert prevu["pire_cas_usd"] <= {"claude": 29.23, "carbon": 14.41, "gpt": 6.44}[nom]


@pytest.mark.parametrize("ajout,motif", [
    ("ecrire a quelqu.un@exemple.org", "courriel"),
    ("voir /home/quelquun/depot", "chemin du poste"),
    ("session_01AbCdEfGhIjKl", "identifiant de session"),
    ("3f2b8c1a-9d4e-4f6a-8b7c-1a2b3c4d5e6f", "identifiant universel"),
    ("le Projet-Factice avance", "terme de la liste"),
])
def test_g5_artefacts_dans_le_corps(ajout, motif):
    en_tetes = {"Content-Type": "application/json", "User-Agent": chef.AGENT_UTILISATEUR}
    chef.controler_envoi(b'{"texte": "rien de personnel"}', en_tetes, INTERDITS)
    with pytest.raises(chef.Arret, match=motif):
        chef.controler_envoi(json.dumps({"texte": ajout}).encode(), en_tetes, INTERDITS)


def test_g5_artefacts_dans_les_en_tetes():
    with pytest.raises(chef.Arret, match="terme de la liste"):
        chef.controler_envoi(b"{}", {"User-Agent": chef.AGENT_UTILISATEUR, "X-Qui": "nom-de-personne-factice"}, INTERDITS)
    with pytest.raises(chef.Arret, match="agent d'utilisateur"):
        chef.controler_envoi(b"{}", {"User-Agent": "outil-du-projet/1"}, INTERDITS)


def test_g5_liste_locale_exigee(tmp_path):
    config = copy.deepcopy(CONFIG)
    config["garde_g5"]["fichier_local"] = str(tmp_path / "absente.txt")
    with pytest.raises(chef.Arret, match="absente"):
        chef.charger_interdits(config, RACINE, {})
    liste = tmp_path / "interdits.txt"
    liste.write_text("# commentaire\nNom-De-Personne-Factice\nabc\n", encoding="utf-8")
    config["garde_g5"]["fichier_local"] = str(liste)
    termes = chef.charger_interdits(config, RACINE, {"MA_SESSION": "identifiant-de-session-xyz", "AUTRE_SESSION": "true",
                                                     "SESSION_KEY": "valeur-de-cle-jamais-lue"})
    assert "nom-de-personne-factice" in termes and "identifiant-de-session-xyz" in termes
    assert "abc" not in termes and "true" not in termes and "valeur-de-cle-jamais-lue" not in termes
    assert RACINE.name.lower() in termes
    liste.write_text("# rien\n", encoding="utf-8")
    with pytest.raises(chef.Arret, match="vide"):
        chef.charger_interdits(config, RACINE, {})


def test_g5_arrete_la_file_avant_tout_envoi(tmp_path, faux):
    f = faux()
    interdits = INTERDITS + ["tessel-9"]  # un mot du lexique inventé, pour l'essai : la première entrée qui le porte coupe
    bilan, journal, _, _ = jouer(tmp_path, "gpt", f, interdits=interdits)
    assert "G5" in bilan["arret_file"] and not bilan["complet"]
    assert len(f.recus) == len(envois(journal)) < 8


# --- G1 : plafond, avant l'envoi ---------------------------------------------------------------------------------------

def test_g1_compteur_sain_et_artefact():
    c = chef.Compteur(6.0, {"m": 6.0}, {"m": 1.0})
    assert c.motif_de_refus("m", 0.26) is None
    c.compter("m", 4.99)
    assert c.depense["m"] == pytest.approx(5.99) and "plafond du modèle" in c.motif_de_refus("m", 0.26)
    file = chef.Compteur(1.0, {"a": 1.0, "b": 1.0}, {"a": 0.6, "b": 0.3})
    assert "plafond de la file" in file.motif_de_refus("b", 0.2)
    assert chef.pire_cas_usd(24000, 8192, [4, 20]) == pytest.approx(0.25984)


def test_g1_refus_avant_l_envoi_forme_de_google(tmp_path, faux):
    f = faux()

    def modifs(config):
        config["files"]["carbon"]["plafond_usd"] = 0.5
        config["files"]["carbon"]["modeles"]["gemini-4-carbon"]["plafond_usd"] = 0.5

    bilan, journal, _, _ = jouer(tmp_path, "carbon", f, modifs)
    assert "G1" in bilan["arret_file"] and not bilan["complet"]
    refuse = [l for l in journal if l["evenement"] == "envoi_refuse_avant_depart"]
    assert len(refuse) == 1 and len(f.recus) == len(envois(journal)) > 0
    assert bilan["depense_comptee_usd"] <= 0.5
    assert bilan["depense_comptee_usd"] + refuse[0]["pire_cas_usd"] > 0.5


def test_g1_sain_les_trois_formes(tmp_path, faux):
    for nom, attendu in (("carbon", 48), ("gpt", 8)):
        f = faux()
        bilan, journal, _, _ = jouer(tmp_path, nom, f)
        assert bilan["complet"] and bilan["lectures"] == attendu == len(f.recus)
        assert bilan["depense_comptee_usd"] < CONFIG["files"][nom]["plafond_usd"]


# --- G3 : sortie maximale ----------------------------------------------------------------------------------------------

def test_g3_corps_sain_et_artefacts():
    for nom in chef.FILES:
        file = CONFIG["files"][nom]
        for reglage in file["reglages"]:
            corps = chef.construire_corps(file, reglage, "texte", file["appel"].get("temperature") is not None)
            chef.controler_corps(file, reglage, corps)
    file, reglage = CONFIG["files"]["claude"], CONFIG["files"]["claude"]["reglages"][0]
    corps = chef.construire_corps(file, reglage, "texte", False)
    assert corps == {"model": "claude-opus-5-5", "max_tokens": 8192, "output_config": {"effort": "low"},
                     "messages": [{"role": "user", "content": "texte"}], "stream": True}
    sans = {k: v for k, v in corps.items() if k != "max_tokens"}
    for fautif in (sans, dict(corps, max_tokens=32768)):
        with pytest.raises(chef.Arret, match="sortie maximale"):
            chef.controler_corps(file, reglage, fautif)
    for champ in ("temperature", "thinking", "fallbacks"):
        with pytest.raises(chef.Arret, match="exclu"):
            chef.controler_corps(file, reglage, dict(corps, **{champ: 0}))


def test_g3_corps_de_carbon_et_de_gpt():
    carbon = CONFIG["files"]["carbon"]
    corps = chef.construire_corps(carbon, carbon["reglages"][1], "texte", True)
    assert corps["generationConfig"] == {"maxOutputTokens": 4096, "thinkingConfig": {"thinkingBudget": 2048}, "temperature": 0}
    assert "temperature" not in chef.construire_corps(carbon, carbon["reglages"][0], "texte", False)["generationConfig"]
    gpt = CONFIG["files"]["gpt"]
    assert chef.construire_corps(gpt, gpt["reglages"][0], "texte", True) == {
        "model": "gpt-6.2-astra", "messages": [{"role": "user", "content": "texte"}], "max_completion_tokens": 8192,
        "temperature": 0}


def test_g3_compteurs_de_carbon_au_dela_de_la_borne_arretent_la_file(tmp_path, faux):
    f = faux(lambda rang, r: {"sortie": 4000, "reflexion": 1500} if rang == 3 else {})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", f)
    assert "G3" in bilan["arret_file"] and len(f.recus) == 4
    dernier = retours(journal)[-1]
    assert dernier["reflexion_au_dela_du_budget"] and dernier["sortie_au_dela_de_la_sortie_max"]
    assert dernier["compte"] == "reel" and dernier["cout_compte_usd"] > 0


def test_carbon_releve_le_respect_du_budget_envoi_par_envoi(tmp_path, faux):
    f = faux(lambda rang, r: {"sortie": 100, "reflexion": 1030} if rang == 0 else {})
    bilan, journal, dossier, config = jouer(tmp_path, "carbon", f)
    premier = retours(journal)[0]
    assert premier["reflexion_au_dela_du_budget"] and not premier["sortie_au_dela_de_la_sortie_max"]
    assert bilan["complet"]
    rapport = chef.faire_rapport(dossier, config)
    assert rapport["reglages"]["carbon-budget-1024"]["reflexions_au_dela_du_budget"] == 1


# --- G4 : refus, surcharge, codes non nommés -----------------------------------------------------------------------------

def test_g4_sain_la_file_claude_entiere_et_son_ordre(tmp_path, faux):
    f = faux()
    bilan, journal, _, _ = jouer(tmp_path, "claude", f)
    assert bilan["complet"] and bilan["lectures"] == 120 == len(f.recus)
    modeles = [r["corps"]["model"] for r in f.recus]
    assert modeles[:24] == ["claude-opus-5-5"] * 24 and modeles[24] == "claude-sonnet-5-5"   # Sonnet après les 24 d'Opus
    assert modeles[96:] == ["claude-haiku-5-5"] * 24
    assert [r["corps"]["output_config"]["effort"] for r in f.recus[::24]] == ["low", "low", "medium", "medium", "low"]
    assert [e["entree"] for e in envois(journal)[:24]] == LOT["ordre"]
    for r in f.recus:
        assert set(r["corps"]) == {"model", "max_tokens", "output_config", "messages", "stream"}
        assert r["en_tetes"]["user-agent"] == chef.AGENT_UTILISATEUR and "anthropic-beta" not in r["en_tetes"]


@pytest.mark.parametrize("code,corps,origine", [
    (429, {"error": {"type": "rate_limit_error"}}, "amont"),
    (429, {"erreur": "borne d'appels du relais atteinte", "relais": "relais-gemini-v3"}, "relais"),
    (402, {"erreur": "plafond de dépense du relais atteint"}, "relais"),
    (401, {"error": {"type": "authentication_error"}}, "amont"),
    (404, {"error": {"type": "not_found_error"}}, "amont"),
    (413, {"error": {"type": "request_too_large"}}, "amont"),
    (422, {"error": {}}, "amont"),
    (418, {"error": {}}, "amont"),
])
def test_g4_refus_de_compte_et_codes_non_nommes_arretent_la_file_sans_reprise(tmp_path, faux, code, corps, origine):
    f = faux(lambda rang, r: {"code": code, "corps": corps} if rang == 2 else {})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", f)
    assert not bilan["complet"] and str(code) in bilan["arret_file"] and origine in bilan["arret_file"]
    assert len(f.recus) == 3 == len(envois(journal))                      # aucun envoi après, aucune reprise
    dernier = retours(journal)[-1]
    assert dernier["origine"] == origine and dernier["suite"] == "arret_file" and dernier["rang"] == 1
    assert dernier["compte"] == ("zero" if origine == "relais" else "pire_cas")


def test_g4_un_403_au_premier_envoi_de_sonnet_arrete_toute_la_file_claude(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 403, "corps": {"error": {"type": "permission_error"}}}
             if r["corps"]["model"] == "claude-sonnet-5-5" else {})
    bilan, journal, dossier, config = jouer(tmp_path, "claude", f)
    assert len(f.recus) == 25 and bilan["lectures"] == 24 and "403" in bilan["arret_file"]
    rapport = chef.faire_rapport(dossier, config)
    assert rapport["reglages"]["opus-5-5-effort-bas"]["tient"]
    for nom in ("sonnet-5-5-effort-bas", "opus-5-5-effort-moyen", "sonnet-5-5-effort-moyen", "haiku-5-5-effort-bas"):
        assert not rapport["reglages"][nom]["tient"] and rapport["reglages"][nom]["lectures_rendues"] == 0


def test_g4_refus_de_contenu_arrete_le_modele_les_autres_continuent(tmp_path, faux):
    f = faux(lambda rang, r: {"fin": "refusal", "texte": ""} if rang == 30 else {})   # Sonnet 5.5, effort bas
    bilan, journal, _, _ = jouer(tmp_path, "claude", f)
    assert bilan["arret_file"] is None and list(bilan["modeles_arretes"]) == ["claude-sonnet-5-5"]
    modeles = [r["corps"]["model"] for r in f.recus]
    assert modeles.count("claude-sonnet-5-5") == 7 and modeles.count("claude-opus-5-5") == 48
    assert modeles.count("claude-haiku-5-5") == 24 and not bilan["complet"]
    assert [l["reglage"] for l in journal if l["evenement"] == "reglage_non_joue"] == ["sonnet-5-5-effort-moyen"]


def test_g4_refus_de_contenu_de_carbon_et_de_gpt(tmp_path, faux):
    f = faux(lambda rang, r: {"fin": "SAFETY", "texte": ""} if rang == 1 else {})
    bilan, _, _, _ = jouer(tmp_path, "carbon", f)
    assert list(bilan["modeles_arretes"]) == ["gemini-4-carbon"] and len(f.recus) == 2
    g = faux(lambda rang, r: {"refus": "je ne peux pas"} if rang == 1 else {})
    bilan, _, _, _ = jouer(tmp_path, "gpt", g)
    assert list(bilan["modeles_arretes"]) == ["gpt-6.2-astra"] and len(g.recus) == 2
    h = faux(lambda rang, r: {"fin": "content_filter"} if rang == 0 else {})
    (tmp_path / "second").mkdir()
    bilan, _, _, _ = jouer(tmp_path / "second", "gpt", h)
    assert list(bilan["modeles_arretes"]) == ["gpt-6.2-astra"] and len(h.recus) == 1


def test_g4_consigne_bloquee_par_google_sans_compteur_arrete_le_modele(tmp_path, faux):
    bloque = {"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"}, "modelVersion": "gemini-4-carbon"}
    f = faux(lambda rang, r: {"code": 200, "corps": bloque} if rang == 1 else {})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", f)
    assert list(bilan["modeles_arretes"]) == ["gemini-4-carbon"] and len(f.recus) == 2
    assert (retours(journal)[-1]["suite"], retours(journal)[-1]["compte"]) == ("arret_modele", "pire_cas")


def test_g4_modele_servi_autre_arrete_la_file(tmp_path, faux):
    f = faux(lambda rang, r: {"modele": "claude-opus-5"} if rang == 5 else {})
    bilan, journal, _, _ = jouer(tmp_path, "claude", f)
    assert "modèle servi autre" in bilan["arret_file"] and len(f.recus) == 6
    assert retours(journal)[-1]["modele_servi"] == "claude-opus-5"
    g = faux(lambda rang, r: {"code": 502, "corps": {"erreur": "modèle servi différent", "relais": "r",
                                                     "modele_demande": "gpt-6.2-astra", "modele_servi": "gpt-6-astra"}})
    bilan, _, _, _ = jouer(tmp_path, "gpt", g)
    assert "modèle servi autre" in bilan["arret_file"] and len(g.recus) == 1


def test_g4_surcharge_une_reprise_puis_arret_du_reglage(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 529, "corps": {"type": "error", "error": {"type": "overloaded_error"}}}
             if rang in (4, 5) else {})
    bilan, journal, _, _ = jouer(tmp_path, "claude", f)
    assert bilan["arret_file"] is None and list(bilan["reglages_arretes"]) == ["opus-5-5-effort-bas"]
    r = retours(journal)
    assert (r[4]["rang"], r[4]["suite"], r[5]["rang"], r[5]["suite"]) == (1, "reprise", 2, "arret_reglage")
    assert r[4]["compte"] == "pire_cas" and r[6]["reglage"] == "sonnet-5-5-effort-bas"
    assert len(f.recus) == 6 + 4 * 24


def test_g4_surcharge_isolee_reprise_reussie(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 503} if rang == 2 else {})
    bilan, journal, dossier, config = jouer(tmp_path, "gpt", f)
    assert bilan["complet"] and len(f.recus) == 9
    rapport = chef.faire_rapport(dossier, config)
    lecture = rapport["reglages"]["gpt-6-2-astra-defaut"]["lectures"][2]
    assert lecture["envois"] == 2 and lecture["envois_sans_compteur"] == 1 and lecture["dernier"]["suite"] == "lecture"


def test_g4_temperature_refusee_au_premier_envoi(tmp_path, faux):
    refus = {"code": 400, "corps": {"error": {"message": "Unsupported parameter: 'temperature' is not supported"}}}
    f = faux(lambda rang, r: refus if rang == 0 else {})
    bilan, journal, _, _ = jouer(tmp_path, "gpt", f)
    assert bilan["complet"] and bilan["temperature_retiree"] and len(f.recus) == 9
    assert "temperature" in f.recus[0]["corps"] and all("temperature" not in r["corps"] for r in f.recus[1:])
    premier = retours(journal)[0]
    assert premier["suite"] == "retirer_temperature" and premier["compte"] == "pire_cas"     # compté au pire cas pour GPT
    assert premier["cout_compte_usd"] == pytest.approx(envois(journal)[0]["pire_cas_usd"], abs=1e-6)
    g = faux(lambda rang, r: refus if rang == 0 else {})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", g)
    assert bilan["complet"] and retours(journal)[0]["compte"] == "zero"                       # zéro pour Carbon
    assert all("temperature" not in r["corps"]["generationConfig"] for r in g.recus[1:])


def test_g4_autre_400_et_400_tardif_arretent_la_file(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 400, "corps": {"error": {"message": "invalid request"}}} if rang == 0 else {})
    bilan, _, _, _ = jouer(tmp_path, "gpt", f)
    assert "code 400" in bilan["arret_file"] and len(f.recus) == 1
    g = faux(lambda rang, r: {"code": 400, "corps": {"error": {"message": "temperature is not supported"}}} if rang == 3 else {})
    bilan, _, _, _ = jouer(tmp_path, "carbon", g)
    assert "code 400" in bilan["arret_file"] and len(g.recus) == 4     # seul le premier envoi de la file peut la retirer


def test_aucune_reprise_cachee(tmp_path, faux):
    """Une réponse 429, puis une réponse 500 : le faux fournisseur reçoit un envoi, et un seul, par envoi journalisé."""
    f = faux(lambda rang, r: {"code": 429})
    _, journal, _, _ = jouer(tmp_path, "gpt", f)
    assert len(f.recus) == 1 == len(envois(journal))
    g = faux(lambda rang, r: {"code": 500})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", g)
    assert len(g.recus) == len(envois(journal)) == 4            # deux réglages : un envoi et sa seule reprise chacun
    assert set(bilan["reglages_arretes"]) == {"carbon-budget-1024", "carbon-budget-2048"}
    assert "http.client" in (RACINE / "scripts" / "chef_essai_mesure_lecteurs_bras_a_v1.py").read_text(encoding="utf-8")
    source = (RACINE / "scripts" / "chef_essai_mesure_lecteurs_bras_a_v1.py").read_text(encoding="utf-8")
    assert not re.search(r"^\s*(import|from)\s+(anthropic|openai|google|requests|httpx|urllib3)\b", source, re.M)


# --- G2 : délais ---------------------------------------------------------------------------------------------------------

def delais_courts(nom, silence=0.4, total=0.8):
    def modifs(config):
        config["files"][nom]["appel"]["delai_silence_s"] = silence
        config["files"][nom]["appel"]["delai_total_s"] = total
    return modifs


def test_g2_sain_et_muet_une_reprise_puis_lecture_perdue(tmp_path, faux):
    f = faux(lambda rang, r: {"muet": 1.5} if rang in (1, 2) else {})
    bilan, journal, _, _ = jouer(tmp_path, "gpt", f, delais_courts("gpt"))
    r = retours(journal)
    assert (r[0]["suite"], r[0]["incident"]) == ("lecture", None)
    assert (r[1]["incident"], r[1]["suite"], r[1]["compte"]) == ("delai", "reprise", "pire_cas")
    assert (r[2]["rang"], r[2]["suite"]) == (2, "lecture_perdue")
    assert r[3]["suite"] == "lecture" and bilan["lectures"] == 7 and not bilan["complet"]
    assert r[1]["cout_compte_usd"] == pytest.approx(envois(journal)[1]["pire_cas_usd"], abs=1e-6)


def test_g2_trois_delais_de_suite_arretent_le_reglage(tmp_path, faux):
    f = faux(lambda rang, r: {"muet": 1.5} if r["corps"]["generationConfig"]["thinkingConfig"]["thinkingBudget"] == 1024 else {})
    bilan, journal, _, _ = jouer(tmp_path, "carbon", f, delais_courts("carbon"))
    assert bilan["reglages_arretes"] == {"carbon-budget-1024": "G2 : trois délais de suite"}
    assert [r["reglage"] for r in retours(journal)[:4]] == ["carbon-budget-1024"] * 3 + ["carbon-budget-2048"]
    assert bilan["lectures"] == 24


def test_g2_silence_dans_un_flux_claude(tmp_path, faux):
    f = faux(lambda rang, r: {"muet": 1.5} if rang == 0 else {})
    bilan, journal, _, _ = jouer(tmp_path, "claude", f, delais_courts("claude"))
    assert retours(journal)[0]["incident"] == "delai" and retours(journal)[1]["suite"] == "lecture" and bilan["lectures"] == 120


def test_g2_delai_global(tmp_path, faux):
    f = faux()

    def modifs(config):
        config["delai_global_s"] = 0

    bilan, _, _, _ = jouer(tmp_path, "gpt", f, modifs)
    assert "délai global" in bilan["arret_file"] and len(f.recus) <= 1


def test_reponse_200_sans_compteur_comptee_au_pire_cas(tmp_path, faux):
    f = faux(lambda rang, r: {"sans_usage": True} if rang == 0 else {})
    bilan, journal, _, _ = jouer(tmp_path, "claude", f)
    premier = retours(journal)[0]
    assert premier["suite"] == "reprise" and premier["compte"] == "pire_cas" and premier["cout_calcule_usd"] is None
    assert bilan["lectures"] == 120 and len(f.recus) == 121


def test_le_chef_ne_parle_qu_a_la_boucle_locale():
    with pytest.raises(chef.Arret, match="boucle locale"):
        chef.envoyer("http://exemple.invalid:80", "/v1/messages", {}, b"{}", False, 1, 1)
    with pytest.raises(chef.Arret, match="boucle locale"):
        chef.envoyer("https://127.0.0.1:1", "/v1/messages", {}, b"{}", False, 1, 1)


# --- lecture technique et conformité de forme ------------------------------------------------------------------------------

def test_lecture_des_trois_formes():
    google = json.dumps({"candidates": [{"content": {"parts": [{"text": "pensée", "thought": True}, {"text": "{}"}]},
                                         "finishReason": "MAX_TOKENS"}], "modelVersion": "models/gemini-4-carbon",
                         "usageMetadata": {"promptTokenCount": 900, "candidatesTokenCount": 120, "thoughtsTokenCount": 700}}).encode()
    lu = chef.lire_reponse("google", google)
    assert (lu["lisible"], lu["jetons_entree"], lu["jetons_sortie"], lu["jetons_reflexion"], lu["jetons_reponse"]) == (True, 900, 820, 700, 120)
    assert lu["modele_servi"] == "gemini-4-carbon" and lu["texte"] == "{}" and lu["motif_fin"] == "MAX_TOKENS"
    bloque = chef.lire_reponse("google", json.dumps({"promptFeedback": {"blockReason": "SAFETY"}, "usageMetadata": {}}).encode())
    assert bloque["refus_de_contenu"] and not bloque["lisible"]
    openai = json.dumps({"model": "gpt-6.2-astra", "choices": [{"message": {"content": "{}"}, "finish_reason": "stop"}],
                         "usage": {"prompt_tokens": 800, "completion_tokens": 500,
                                   "completion_tokens_details": {"reasoning_tokens": 350}}}).encode()
    lu = chef.lire_reponse("openai", openai)
    assert (lu["jetons_entree"], lu["jetons_sortie"], lu["jetons_reflexion"], lu["lisible"]) == (800, 500, 350, True)
    entier = json.dumps({"model": "claude-opus-5-5", "stop_reason": "end_turn", "content": [{"type": "thinking", "thinking": ""},
                         {"type": "text", "text": "{}"}], "usage": {"input_tokens": 950, "output_tokens": 480}}).encode()
    lu = chef.lire_reponse("anthropic", entier)
    assert (lu["jetons_entree"], lu["jetons_sortie"], lu["jetons_reflexion"], lu["texte"]) == (950, 480, None, "{}")
    for illisible in (b"", b"pas du json", b"[]", b'{"model": "x"}'):
        for fournisseur in ("anthropic", "google", "openai"):
            assert not chef.lire_reponse(fournisseur, illisible)["lisible"]


def test_lecture_d_un_flux_claude_complet_coupe_ou_en_erreur():
    def flux(evenements):
        return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in evenements).encode()
    debut = [{"type": "message_start", "message": {"model": "claude-sonnet-5-5", "usage": {"input_tokens": 900, "output_tokens": 1}}},
             {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": '{"a"'}},
             {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": ": 1}"}}]
    fin = [{"type": "message_delta", "delta": {"stop_reason": "max_tokens"}, "usage": {"output_tokens": 8192}}, {"type": "message_stop"}]
    lu = chef.lire_reponse("anthropic", flux(debut + fin), "text/event-stream")
    assert (lu["lisible"], lu["jetons_entree"], lu["jetons_sortie"], lu["motif_fin"], lu["texte"]) == (True, 900, 8192, "max_tokens", '{"a": 1}')
    assert not chef.lire_reponse("anthropic", flux(debut), "text/event-stream")["lisible"]
    erreur = chef.lire_reponse("anthropic", flux(debut + [{"type": "error", "error": {"type": "overloaded_error"}}]), "text/event-stream")
    assert not erreur["lisible"] and erreur["erreur_de_flux"] == "overloaded_error"


def test_origine_relais_ou_amont():
    assert chef.origine_et_erreur(b'{"erreur": "plafond"}')[0] == "relais"
    assert chef.origine_et_erreur(b'{"error": {"type": "x"}}')[0] == "amont"
    assert chef.origine_et_erreur(b"illisible") == ("amont", {})


@pytest.mark.parametrize("texte,coupee,attendu", [
    ('{"fit": "answers", "specific": false, "proposal_quote": "a", "controls_quote": "b"}', False, (True, None)),
    (' {"fit": "does_not_answer", "specific": null, "proposal_quote": "a", "controls_quote": "b"}\n', False, (True, None)),
    ('{"fit": "cannot_tell", "specific": null, "proposal_quote": null, "controls_quote": null}', False, (True, None)),
    ("", False, (False, "vide")),
    ("   \n", False, (False, "vide")),
    ('{"fit": "answers", "specific": true, "proposal_quote": "a", "contr', True, (False, "coupee")),
    ('```json\n{"fit": "cannot_tell", "specific": null, "proposal_quote": null, "controls_quote": null}\n```', False, (False, "entouree")),
    ('Here is my answer: {"fit": "cannot_tell", "specific": null, "proposal_quote": null, "controls_quote": null}', False, (False, "entouree")),
    ("I cannot answer this.", False, (False, "non_json")),
    ("[1, 2]", False, (False, "non_json")),
    ('{"fit": "answers", "specific": true, "proposal_quote": "a"}', False, (False, "cles")),
    ('{"fit": "answers", "specific": true, "proposal_quote": "a", "controls_quote": "b", "note": 1}', False, (False, "cles")),
    ('{"fit": "maybe", "specific": null, "proposal_quote": "a", "controls_quote": "b"}', False, (False, "valeurs")),
    ('{"fit": "answers", "specific": null, "proposal_quote": "a", "controls_quote": "b"}', False, (False, "valeurs")),
    ('{"fit": "does_not_answer", "specific": true, "proposal_quote": "a", "controls_quote": "b"}', False, (False, "valeurs")),
    ('{"fit": "does_not_answer", "specific": null, "proposal_quote": null, "controls_quote": "b"}', False, (False, "valeurs")),
    ('{"fit": "cannot_tell", "specific": null, "proposal_quote": "a", "controls_quote": null}', False, (False, "valeurs")),
    ('{"fit": "answers", "fit": "answers", "specific": true, "proposal_quote": "a", "controls_quote": "b"}', False, (False, "cles")),
])
def test_conformite_de_l_appariement(texte, coupee, attendu):
    assert chef.conformite_de_forme("appariement", texte, None, coupee) == attendu


@pytest.mark.parametrize("objet,attendu", [
    ({"c1": {"content": "conforme", "quote": "q", "place": "checks"}, "c2": {"content": "absent", "quote": None, "place": None}}, (True, None)),
    ({"c1": {"content": "altere", "quote": "q", "place": "general"}, "c2": {"content": "conforme", "quote": "q", "place": "cannot_check"}}, (True, None)),
    ({"c1": {"content": "conforme", "quote": "q", "place": "checks"}}, (False, "cles")),
    ({"c1": {"content": "conforme", "quote": "q", "place": "checks"}, "c2": {"content": "absent", "quote": None, "place": None}, "c3": {}}, (False, "cles")),
    ({"c1": {"content": "conforme", "quote": "q"}, "c2": {"content": "absent", "quote": None, "place": None}}, (False, "cles")),
    ({"c1": {"content": "present", "quote": "q", "place": "checks"}, "c2": {"content": "absent", "quote": None, "place": None}}, (False, "valeurs")),
    ({"c1": {"content": "conforme", "quote": "q", "place": None}, "c2": {"content": "absent", "quote": None, "place": None}}, (False, "valeurs")),
    ({"c1": {"content": "conforme", "quote": "q", "place": "checks"}, "c2": {"content": "absent", "quote": None, "place": "general"}}, (False, "valeurs")),
    ({"c1": {"content": "conforme", "quote": 3, "place": "checks"}, "c2": {"content": "absent", "quote": None, "place": None}}, (False, "valeurs")),
])
def test_conformite_de_la_couverture(objet, attendu):
    assert chef.conformite_de_forme("couverture", json.dumps(objet), ["c1", "c2"], False) == attendu


def test_conformite_relevee_au_journal_sans_le_texte(tmp_path, faux):
    f = faux(lambda rang, r: {"texte": "Voici ma réponse, hors de la forme exigée."} if rang == 1 else
             ({"fin": "length", "texte": '{"fit": "answers", "specific": true, "propos'} if rang == 2 else {}))
    bilan, journal, dossier, config = jouer(tmp_path, "gpt", f)
    r = retours(journal)
    assert (r[0]["conforme"], r[1]["conforme"], r[1]["cause_non_conformite"]) == (True, False, "non_json")
    assert (r[2]["conforme"], r[2]["cause_non_conformite"], r[2]["fin_par_sortie_max"]) == (False, "coupee", True)
    rapport = chef.faire_rapport(dossier, config)
    reglage = rapport["reglages"]["gpt-6-2-astra-defaut"]
    assert (reglage["conformes"], reglage["fins_par_sortie_max"], reglage["tient"]) == (6, 1, False)
    assert "hors de la forme" not in (dossier / "journal-essai.jsonl").read_text(encoding="utf-8")


# --- récupération, rapport, inventaire -------------------------------------------------------------------------------------

def test_tout_est_garde_corps_envoyes_et_reponses_entieres(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 429, "corps": {"error": {"message": "trop de requêtes"}}} if rang == 3 else {})
    bilan, journal, dossier, _ = jouer(tmp_path, "gpt", f)
    corps = sorted((dossier / "envois").glob("*.json"))
    bruts = sorted((dossier / "reponses-brutes-non-lues").glob("*.corps"))
    assert len(corps) == len(bruts) == 4 == len(list((dossier / "reponses-brutes-non-lues").glob("*.entetes.json")))
    for envoi, fichier, recu in zip(envois(journal), corps, f.recus):
        assert fichier.read_bytes() == recu["brut"] and hashlib.sha256(recu["brut"]).hexdigest() == envoi["sha256_corps"]
    assert b"trop de requ" in bruts[-1].read_bytes()                       # la réponse d'erreur est gardée entière
    assert json.loads((dossier / "reponses-brutes-non-lues" / (bruts[-1].stem + ".entetes.json")).read_text())["code"] == 429
    inventaire = chef.inventorier(dossier, "arretee")
    chemins = {x["chemin"] for x in inventaire["fichiers"]}
    assert "journal-essai.jsonl" in chemins and len(chemins) == 4 * 3 + 1 and inventaire["etat"] == "arretee"
    compagnon = (dossier / "inventaire.json.sha256").read_text().split()[0]
    assert compagnon == hashlib.sha256((dossier / "inventaire.json").read_bytes()).hexdigest()
    for x in inventaire["fichiers"]:
        assert hashlib.sha256((dossier / x["chemin"]).read_bytes()).hexdigest() == x["sha256"]


def test_rapport_sans_aucun_texte_de_reponse(tmp_path, faux):
    marque = "PHRASE-TEMOIN-QUI-NE-DOIT-PARAITRE-NULLE-PART"
    f = faux(lambda rang, r: {"texte": json.dumps({"fit": "cannot_tell", "specific": None, "proposal_quote": None,
                                                   "controls_quote": None, }) + marque} if rang == 0 else {})
    _, _, dossier, config = jouer(tmp_path, "gpt", f)
    rapport = chef.ecrire_rapport(dossier, config)
    ecrit = (dossier / "rapport-technique.json").read_text(encoding="utf-8") + (dossier / "rapport-technique.md").read_text(encoding="utf-8")
    assert marque not in ecrit and marque not in (dossier / "journal-essai.jsonl").read_text(encoding="utf-8")
    assert marque.encode() in b"".join(p.read_bytes() for p in (dossier / "reponses-brutes-non-lues").glob("*.corps"))
    textes = chef.textes_des_reponses(dossier, "openai")
    assert len(textes) == 8 and chef.controler_aucune_sous_chaine(ecrit, textes) == 0
    assert chef.controler_aucune_sous_chaine(ecrit + " " + marque, textes) > 0          # artefact : le contrôle le voit
    assert rapport["reglages"]["gpt-6-2-astra-defaut"]["lectures_rendues"] == 8
    assert set(rapport["reglages"]["gpt-6-2-astra-defaut"]["lectures"][0]["dernier"]) >= {
        "code", "motif_fin", "jetons_entree", "jetons_sortie", "jetons_reflexion", "duree_s", "modele_servi", "conforme"}


def test_recherche_de_formes_de_cle(tmp_path):
    (tmp_path / "journal.jsonl").write_text('{"statut": 200}\n', encoding="utf-8")
    assert chef.chercher_formes_de_cle(tmp_path) == []
    (tmp_path / "relais").mkdir()
    (tmp_path / "relais" / "console.txt").write_text("clé : sk-ant-" + "a1B2" * 8 + "\n", encoding="utf-8")
    assert chef.chercher_formes_de_cle(tmp_path) == ["relais/console.txt"]


# --- règle de choix (devis, section 7), sur des rapports fabriqués ---------------------------------------------------------

def rapport_fabrique(reglages):
    """`reglages` : {nom: (sortie de l'appariement par longueur, tient)}."""
    sortie = {"reglages": {}}
    for nom, (par_longueur, tient, prix) in reglages.items():
        c, m, l = par_longueur
        def bloc(s, entree=1000):
            return {"lectures": 6, "sortie_moyenne": s, "entree_moyenne": entree, "cout_moyen_usd": (entree * prix[0] + s * prix[1]) / 1e6}
        app = {"lectures": 18, "par_longueur": {"courte": bloc(c), "mediane": bloc(m), "longue": bloc(l)},
               "sortie_moyenne_simple": (c + m + l) / 3, "sortie_max": int(l * 1.5), "reponse_seule_max": 400, "non_conformes": 0}
        couv = {"lectures": 6, "par_longueur": {k: dict(bloc(2 * m, 4000), lectures=2) for k in ("courte", "mediane", "longue")},
                "sortie_moyenne_simple": 2 * m, "sortie_max": int(3 * m), "reponse_seule_max": 700, "non_conformes": 0}
        sortie["reglages"][nom] = {"tient": tient, "par_instrument": {"appariement": app, "couverture": couv}}
    return sortie


OPUS, SONNET = [4, 20], [2, 10]


def test_regle_opus_sous_le_seuil():
    r = rapport_fabrique({"opus-5-5-effort-bas": ((400, 600, 900), True, OPUS), "sonnet-5-5-effort-bas": ((300, 400, 500), True, SONNET)})
    choix = chef.appliquer_regle(CONFIG, r, None)["claude"]
    assert choix["choix"] == "claude-opus-5-5" and choix["reglage"] == "opus-5-5-effort-bas"
    assert choix["efforts_retenus"]["claude-opus-5-5"]["S_a"] == pytest.approx(0.25 * 400 + 0.5 * 600 + 0.25 * 900)
    assert choix["sortie_maximale_du_devis_des_lectures"] == 8192          # 4 × 1 800 = 7 200 < 8 192


def test_regle_effort_moyen_si_le_bas_ne_tient_pas_et_sortie_maximale():
    r = rapport_fabrique({"opus-5-5-effort-bas": ((400, 600, 900), False, OPUS), "opus-5-5-effort-moyen": ((900, 1400, 2000), True, OPUS)})
    choix = chef.appliquer_regle(CONFIG, r, None)["claude"]
    assert (choix["choix"], choix["reglage"]) == ("claude-opus-5-5", "opus-5-5-effort-moyen")
    assert choix["sortie_maximale_du_devis_des_lectures"] == 17408         # maximum observé 4 200 (couverture) ; 4 × 4 200 = 16 800, arrondi aux 1 024 supérieurs


def test_regle_bascule_vers_sonnet_au_dessus_du_seuil():
    r = rapport_fabrique({"opus-5-5-effort-bas": ((1200, 1800, 2400), True, OPUS), "sonnet-5-5-effort-bas": ((900, 1300, 1700), True, SONNET)})
    choix = chef.appliquer_regle(CONFIG, r, None)["claude"]
    assert choix["choix"] == "claude-sonnet-5-5" and "point 3" in choix["motif"]
    cher = rapport_fabrique({"opus-5-5-effort-bas": ((1200, 1800, 2400), True, OPUS), "sonnet-5-5-effort-bas": ((2000, 2600, 3200), True, SONNET)})
    assert chef.appliquer_regle(CONFIG, cher, None)["claude"]["choix"] is None      # ni sous le seuil, ni à la moitié du coût


def test_regle_opus_ecarte_et_aucun_reglage():
    r = rapport_fabrique({"opus-5-5-effort-bas": ((400, 600, 900), False, OPUS), "opus-5-5-effort-moyen": ((400, 600, 900), False, OPUS),
                          "sonnet-5-5-effort-bas": ((2000, 3000, 4000), True, SONNET)})
    choix = chef.appliquer_regle(CONFIG, r, None)["claude"]
    assert choix["choix"] == "claude-sonnet-5-5" and "point 4" in choix["motif"]
    rien = rapport_fabrique({"opus-5-5-effort-bas": ((400, 600, 900), False, OPUS), "haiku-5-5-effort-bas": ((100, 100, 100), True, [0.1, 0.5])})
    sortie = chef.appliquer_regle(CONFIG, rien, None)["claude"]
    assert sortie["choix"] is None and "claude-haiku-5-5" in sortie["jamais_retenus_par_la_regle"]


def test_regle_carbon():
    r = rapport_fabrique({"carbon-budget-1024": ((500, 700, 900), False, [4, 20]), "carbon-budget-2048": ((800, 1100, 1500), True, [4, 20])})
    choix = chef.appliquer_regle(CONFIG, None, r)["carbon"]
    assert choix["choix"] == "carbon-budget-2048" and choix["sortie_maximale_du_devis_des_lectures"] == 8192
    aucun = rapport_fabrique({"carbon-budget-1024": ((1, 1, 1), False, [4, 20]), "carbon-budget-2048": ((1, 1, 1), False, [4, 20])})
    assert chef.appliquer_regle(CONFIG, None, aucun)["carbon"]["choix"] is None


def test_regle_calculee_depuis_un_vrai_rapport(tmp_path, faux):
    f = faux(lambda rang, r: {"sortie": 2000} if r["corps"]["model"] == "claude-opus-5-5" else {"sortie": 500})
    _, _, dossier, config = jouer(tmp_path, "claude", f)
    choix = chef.appliquer_regle(config, chef.faire_rapport(dossier, config), None)["claude"]
    assert choix["efforts_retenus"]["claude-opus-5-5"]["S_a"] == 2000 and choix["choix"] == "claude-sonnet-5-5"
    assert choix["efforts_retenus"]["claude-sonnet-5-5"]["C_usd"] < choix["efforts_retenus"]["claude-opus-5-5"]["C_usd"] / 2


# --- de bout en bout : amorce, vrais relais du dépôt, clés factices, faux fournisseur --------------------------------------

def preparer(tmp_path, nom, faux_fournisseur, modifs=None):
    config = copy.deepcopy(CONFIG)
    file = config["files"][nom]
    file["relais"]["arguments"] = file["relais"]["arguments"] + ["--amont", faux_fournisseur.url]
    config["dossier_des_courses"] = str(tmp_path / "courses")
    liste = tmp_path / "interdits.txt"
    liste.write_text("nom-de-personne-factice\n", encoding="utf-8")
    config["garde_g5"]["fichier_local"] = str(liste)
    if nom == "claude":
        releve = tmp_path / "releve.json"
        releve.write_text('{"code_http": 200}\n', encoding="utf-8")
        empreinte = hashlib.sha256(releve.read_bytes()).hexdigest()
        (tmp_path / "releve.json.sha256").write_text(f"{empreinte}  releve.json\n", encoding="utf-8")
        file["cle"]["attestation"] = {"chemin": str(releve), "sha256": empreinte}
    if modifs:
        modifs(config)
    chemin = tmp_path / "configuration-essai.json"
    chemin.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(tmp_path), "LANG": "C.UTF-8", "GO_ID": file["go"],
           "RR_ANTHROPIC_API_KEY_RIGAUD": CLE_FACTICE, "GEMINI_API_KEY": CLE_FACTICE,
           "OPENAI_API_KEY": "valeur-presente-dans-le-conteneur-jamais-transmise"}
    registre = ligne_go(file["go"], plafond=file["plafond_registre"])
    arguments = dict(racine=RACINE, chemin_configuration=chemin,
                     empreinte_configuration=hashlib.sha256(chemin.read_bytes()).hexdigest(), registre=registre,
                     aujourd_hui="2026-11-19")
    return config, env, arguments


def dossier_de_course(tmp_path, nom):
    trouves = list((tmp_path / "courses").glob(f"*-file-{nom}"))
    assert len(trouves) == 1
    return trouves[0]


def relais_arrete(dossier):
    amorce = chef.lire_journal(dossier / "journal-amorce.jsonl")
    arret = next(l for l in amorce if l["evenement"] == "relais_arrete")
    return arret["arrete"] and not chef.processus_vivant(arret["pid"])


@pytest.mark.parametrize("nom,appels", [("claude", 120), ("carbon", 48), ("gpt", 8)])
def test_bout_en_bout_file_saine_par_le_vrai_relais(tmp_path, faux, nom, appels, capsys):
    f = faux()
    config, env, arguments = preparer(tmp_path, nom, f)
    assert chef.executer(nom, env, **arguments) == 0
    dossier = dossier_de_course(tmp_path, nom)
    assert len(f.recus) == appels
    # G6 : le fournisseur reçoit la clé du relais ; le chef n'a envoyé que le jeton factice ; rien n'est écrit nulle part.
    attendues = {"claude": ("x-api-key", CLE_FACTICE), "carbon": ("x-goog-api-key", CLE_FACTICE),
                 "gpt": ("authorization", "Bearer factice-secret-de-reseau")}[nom]
    assert all(r["en_tetes"].get(attendues[0]) == attendues[1] for r in f.recus)
    tout = b"".join(p.read_bytes() for p in dossier.rglob("*") if p.is_file())
    assert CLE_FACTICE.encode() not in tout and b"jamais-transmise" not in tout and b"factice-secret-de-reseau" not in tout
    manifeste = json.loads((dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
    assert manifeste["go"] == config["files"][nom]["go"] and manifeste["cle"]["variable"] == config["files"][nom]["cle"]["variable"]
    assert manifeste["prevu"]["appels"] == appels and "interdits" not in json.dumps(manifeste["interdits_g5"])[20:]
    rapport = json.loads((dossier / "rapport-technique.json").read_text(encoding="utf-8"))
    assert all(r["tient"] and r["lectures_rendues"] == r["lectures_attendues"] for r in rapport["reglages"].values())
    etat = json.loads((dossier / "relais" / "etat-final.json").read_text(encoding="utf-8"))
    assert etat["appels"] == appels
    assert (dossier / "relais" / "journal-relais.jsonl").exists() and (dossier / "relais" / "console-relais.txt").exists()
    assert relais_arrete(dossier)
    inventaire = json.loads((dossier / "inventaire.json").read_text(encoding="utf-8"))
    assert inventaire["etat"] == "finie" and inventaire["nombre"] >= 3 * appels + 8
    if nom == "carbon":   # les résumés de pensée ne sont pas demandés à l'amont (devis, 5.3)
        assert all("includeThoughts" not in json.dumps(r["corps"]) for r in f.recus)
        assert all("streamGenerateContent" in r["chemin"] for r in f.recus)
    if nom == "gpt":
        assert all(r["corps"].get("stream") is True and r["corps"]["max_completion_tokens"] == 8192 for r in f.recus)
    # une ligne ne se rejoue pas
    assert chef.executer(nom, env, **arguments) == 2
    assert "ne se rejoue pas" in capsys.readouterr().err and len(f.recus) == appels


def test_bout_en_bout_arret_par_un_refus_tout_est_inventorie_et_le_relais_arrete(tmp_path, faux):
    f = faux(lambda rang, r: {"code": 429, "corps": {"error": {"message": "quota"}}} if rang == 5 else {})
    _, env, arguments = preparer(tmp_path, "carbon", f)
    assert chef.executer("carbon", env, **arguments) == 1
    dossier = dossier_de_course(tmp_path, "carbon")
    assert len(f.recus) == 6 and relais_arrete(dossier)
    inventaire = json.loads((dossier / "inventaire.json").read_text(encoding="utf-8"))
    chemins = {x["chemin"] for x in inventaire["fichiers"]}
    assert inventaire["etat"] == "arretee" and {"journal-essai.jsonl", "journal-amorce.jsonl", "manifeste-depart.json",
                                                "rapport-technique.json", "relais/etat-final.json",
                                                "relais/journal-relais.jsonl", "relais/console-relais.txt"} <= chemins
    assert sum(c.startswith("envois/") for c in chemins) == 6 and sum(c.endswith(".corps") for c in chemins) == 6
    bilan = [l for l in chef.lire_journal(dossier / "journal-essai.jsonl") if l["evenement"] == "fin_de_la_file"][0]
    assert "429" in bilan["arret_file"] and "amont" in bilan["arret_file"]


def test_bout_en_bout_borne_d_appels_du_relais_de_google_lue_comme_refus_du_relais(tmp_path, faux):
    f = faux()

    def modifs(config):
        arguments = config["files"]["carbon"]["relais"]["arguments"]
        arguments[arguments.index("--max-appels") + 1] = "3"
        config["files"]["carbon"]["relais"]["etat_attendu"]["max_appels"] = 3

    _, env, arguments = preparer(tmp_path, "carbon", f, modifs)
    assert chef.executer("carbon", env, **arguments) == 1
    dossier = dossier_de_course(tmp_path, "carbon")
    dernier = retours(chef.lire_journal(dossier / "journal-essai.jsonl"))[-1]
    assert (dernier["code"], dernier["origine"], dernier["suite"], dernier["compte"]) == (429, "relais", "arret_file", "zero")
    assert len(f.recus) == 3


def test_bout_en_bout_plafond_du_relais_claude_et_modele_non_permis(tmp_path, faux):
    f = faux()

    def modifs(config):
        arguments = config["files"]["claude"]["relais"]["arguments"]
        arguments[arguments.index("--modeles-permis") + 1] = "claude-opus-5-5"
        config["files"]["claude"]["relais"]["etat_attendu"]["modeles_permis"] = ["claude-opus-5-5"]

    _, env, arguments = preparer(tmp_path, "claude", f, modifs)
    assert chef.executer("claude", env, **arguments) == 1
    dossier = dossier_de_course(tmp_path, "claude")
    dernier = retours(chef.lire_journal(dossier / "journal-essai.jsonl"))[-1]
    assert (dernier["code"], dernier["origine"], dernier["modele"]) == (403, "relais", "claude-sonnet-5-5")
    assert len(f.recus) == 24                      # le relais a refusé Sonnet avant l'amont ; toute la file s'arrête


def test_bout_en_bout_interruption_en_cours_inventaire_d_abord(tmp_path, faux):
    f = faux(lambda rang, r: {"muet": 30} if rang == 4 else {})
    _, env, arguments = preparer(tmp_path, "carbon", f)
    resultat = {}

    def lancer():
        resultat["code"] = chef.executer("carbon", env, **arguments)

    # `executer` pose ses gestionnaires de signaux : il doit tourner dans le fil principal ; le signal vient d'un minuteur.
    minuteur = threading.Timer(4.0, lambda: os.kill(os.getpid(), signal.SIGTERM))
    minuteur.start()
    try:
        lancer()
    finally:
        minuteur.cancel()
    assert resultat["code"] == 3
    dossier = dossier_de_course(tmp_path, "carbon")
    inventaire = json.loads((dossier / "inventaire.json").read_text(encoding="utf-8"))
    chemins = {x["chemin"] for x in inventaire["fichiers"]}
    assert inventaire["etat"] == "arretee" and sum(c.startswith("envois/") for c in chemins) == 5
    assert "relais/etat-final.json" in chemins and relais_arrete(dossier)
    bilan = [l for l in chef.lire_journal(dossier / "journal-essai.jsonl") if l["evenement"] == "fin_de_la_file"][0]
    assert "interruption" in bilan["arret_file"]


# --- gardes de départ de l'amorce : rien ne part ---------------------------------------------------------------------------

def test_amorce_sans_ligne_de_calcul_rien_ne_part(tmp_path, faux, capsys):
    f = faux()
    _, env, arguments = preparer(tmp_path, "gpt", f)
    assert chef.executer("gpt", dict(env, GO_ID="GO-2026-11-19-35"), **arguments) == 2
    assert chef.executer("gpt", {k: v for k, v in env.items() if k != "GO_ID"}, **arguments) == 2
    assert chef.executer("gpt", env, **dict(arguments, registre="# registre sans la ligne")) == 2
    assert chef.executer("gpt", env, **dict(arguments, empreinte_configuration="0" * 64)) == 2
    assert chef.executer("inconnue", env, **arguments) == 2
    assert not (tmp_path / "courses").exists() and f.recus == []
    assert "ARRÊT avant tout envoi" in capsys.readouterr().err


def test_amorce_page_de_prix_de_carbon_non_conforme_rien_ne_part(tmp_path, faux, capsys):
    f = faux()

    def modifs(config):
        config["files"]["carbon"]["pages_de_prix"][0]["sha256"] = "0" * 64

    _, env, arguments = preparer(tmp_path, "carbon", f, modifs)
    assert chef.executer("carbon", env, **arguments) == 2
    assert "page de prix" in capsys.readouterr().err and f.recus == [] and not (tmp_path / "courses").exists()


def test_amorce_g8_la_file_claude_ne_part_pas_les_autres_ne_l_attendent_pas(tmp_path, faux):
    f = faux()
    _, env, arguments = preparer(tmp_path, "claude", f)
    sans_cle = {k: v for k, v in env.items() if k != "RR_ANTHROPIC_API_KEY_RIGAUD"}
    assert chef.executer("claude", sans_cle, **arguments) == 2
    (tmp_path / "releve.json").write_text('{"code_http": 403}\n', encoding="utf-8")      # relevé d'une autre empreinte
    assert chef.executer("claude", env, **arguments) == 2
    assert not (tmp_path / "courses").exists() and f.recus == []
    autre = tmp_path / "gpt"
    autre.mkdir()
    g = faux()
    _, env_gpt, arguments_gpt = preparer(autre, "gpt", g)
    assert chef.executer("gpt", {k: v for k, v in env_gpt.items() if "RIGAUD" not in k}, **arguments_gpt) == 0
    assert len(g.recus) == 8


def test_g6_cle_exigee_par_son_nom_et_valeur_factice_pour_gpt(tmp_path, faux):
    f = faux()
    _, env, arguments = preparer(tmp_path, "carbon", f)
    sans = {k: v for k, v in env.items() if k != "GEMINI_API_KEY"}
    assert chef.executer("carbon", sans, **arguments) == 2                 # garde de départ : variable absente
    config = copy.deepcopy(CONFIG)
    dossier = tmp_path / "direct"
    dossier.mkdir()
    with pytest.raises(chef.Arret, match="G6"):
        chef.lancer_relais(config, "carbon", RACINE, dossier, {"PATH": env["PATH"]})
    assert f.recus == [] and not (dossier / "relais" / "console-relais.txt").exists()
    lanceur = chef.charger_lanceur(RACINE, CONFIG)
    with pytest.raises(lanceur.Refus):                                      # artefact : relais de GPT lancé sans la variable
        lanceur.environnement_reduit(["PATH", "!OPENAI_API_KEY"], {"PATH": env["PATH"]})


def test_ouvrier_refuse_un_nom_de_cle_et_un_lancement_hors_amorce(tmp_path, capsys):
    assert chef.ouvrier(tmp_path, {"PATH": "/bin", "OPENAI_API_KEY": "x"}, b"{}") == 2
    (tmp_path / "manifeste-depart.json").write_text(json.dumps({"pid_amorce": 1, "go": "GO-2026-11-19-36"}), encoding="utf-8")
    assert chef.ouvrier(tmp_path, {"PATH": "/bin", "GO_ID": "GO-2026-11-19-36"}, b"{}") == 2
    erreurs = capsys.readouterr().err
    assert "nom de clé" in erreurs and "lancé que par son amorce" in erreurs


def test_etat_initial_du_relais_controle():
    attendu = CONFIG["files"]["claude"]["relais"]["etat_attendu"]
    sain = {"plafond_usd": 9.25, "reserve_par_appel_usd": 0.27, "depense_usd": 0.0, "appels": 0, "refus": 0,
            "modeles_permis": ["claude-opus-5-5", "claude-haiku-5-5", "claude-sonnet-5-5"]}
    chef.controler_etat_initial(sain, attendu)
    for cle, valeur in (("appels", 3), ("plafond_usd", 92.5), ("modeles_permis", ["claude-opus-5-5"])):
        with pytest.raises(chef.Arret, match=cle):
            chef.controler_etat_initial(dict(sain, **{cle: valeur}), attendu)


def test_ligne_de_commande_refuse_sans_rien_lancer(monkeypatch, capsys):
    """Jamais de `GO_ID` valide ici : avec la vraie configuration, une ligne valide ferait partir de vrais appels."""
    monkeypatch.delenv("GO_ID", raising=False)
    assert chef.principal(["claude"]) == 2
    monkeypatch.setenv("GO_ID", "GO-0000-00-00-00")
    assert chef.principal(["gpt"]) == 2
    assert chef.principal([]) == 2 and chef.principal(["claude", "option"]) == 2
    erreurs = capsys.readouterr().err
    assert erreurs.count("GO_ID") == 2 and "usage" in erreurs


def test_commandes_exactes_ecrites_en_tete_du_fichier():
    source = (RACINE / "scripts" / "chef_essai_mesure_lecteurs_bras_a_v1.py").read_text(encoding="utf-8")
    for nom in chef.FILES:
        assert f"GO_ID={CONFIG['files'][nom]['go']} python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py {nom}\n" in source
