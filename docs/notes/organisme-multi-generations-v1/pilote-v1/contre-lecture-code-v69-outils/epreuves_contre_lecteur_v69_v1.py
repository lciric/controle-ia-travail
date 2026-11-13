"""Épreuves directes du contre-lecteur sur le code v69 du pilote MR-2 — v1 (outil de
`contre-lecture-differentiel-code-pilote-v69-v1.md`).

Aucun réseau hors de la boucle locale (un relais v69 et une doublure d'amont déclarée ici, clé factice posée ici), aucune clé
réelle, aucun appel de modèle. Les mondes de développement (secret public nul) sont lus ; rien de leur contenu n'est écrit : la
sortie ne porte que des booléens, des comptes, des motifs et des empreintes.

  ulimit -v 6000000 ; env -i PATH=/usr/bin:/bin OMP_NUM_THREADS=2 python3 -I -B epreuves_contre_lecteur_v69_v1.py \
      ORCHESTRATEUR MONDES.json SHA BAC SORTIE.json
"""

import copy
import hashlib
import json
import os
import socket
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ORCH, MONDES, SHA_MONDES, BAC, SORTIE = sys.argv[1:6]
sys.path.insert(0, ORCH)
import numpy as np  # noqa: E402

from pole import pilote_mr2_v69 as P  # noqa: E402
from pole import proposeurs_pilote_v69 as PR  # noqa: E402
from pole.outils import json_canonique  # noqa: E402

import importlib.util  # noqa: E402


def charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


C = charger("commande_v69_cl", os.path.join(ORCH, "exemples", "pilote-mr2-v69", "commandes", "commande_pilote_v69.py"))
R = charger("relais_v69_cl", os.path.join(ORCH, "exemples", "pilote-mr2-v69", "commandes", "relais_pilote_v69.py"))
L = charger("lanceur_v69_cl", os.path.join(ORCH, "demonstrations", "pilote_mr2_v69.py"))
CONF = L.CONFIGURATION
V4, M, MP = P.charger_mr2()
os.makedirs(BAC, exist_ok=True)
res = {}
conf, _ = PR.lire_configuration(CONF)

# X4 — gabarit, bloc, configuration (Q-1).
res["X4_gabarit_sha256"] = P.gabarit_sha256()
res["X4_bloc_sha256"] = hashlib.sha256(L.bloc_gele().encode("utf-8")).hexdigest()
res["X4_Q1"] = {n: {"borne": p["borne_sortie_jetons"], "plafond": p["plafond_session_usd"], "part": p["part_usd"],
                    "borne_max_payee": PR.borne_de_sortie_max(p["plafond_session_usd"], p["prix_entree_usd_par_million"],
                                                              p["prix_sortie_usd_par_million"], conf["octets_entree_max"]),
                    "reglages": p["reglages"], "variable_cle": p["variable_cle"], "url_amont": p["url_amont"]}
                for n, p in conf["proposeurs"].items()}
res["X4_go"] = {k: {"montant": g["montant_usd"], "parts": g["parts_usd"]} for k, g in conf["go"].items()}
res["X4_total_au_pire"] = round(sum(g["montant_usd"] for g in conf["go"].values()), 2)

# X1 — dérivation des épisodes : la règle écrite au manifeste (étiquette « v68 ») contre le code (étiquette du module).
mondes = P.charger_mondes_prives(MONDES, SHA_MONDES)
x1 = {}
for w in mondes:
    spec = w["spec"]
    servis = hashlib.sha256(json_canonique(P.episodes_de_developpement(spec))).hexdigest()

    def par_etiquette(etiquette):
        loi = P.compiler_monde(spec)
        cle = int.from_bytes(hashlib.sha256((etiquette + "|" + P.sha_spec(spec)).encode()).digest()[:16], "big")
        rng = np.random.default_rng(np.random.SeedSequence(cle))
        Z, G = M.tirer_instances(rng, 400, spec["dimension"], spec["sous_populations"])
        Y = M.tirer_issues(rng, M.probas(loi, Z, G))
        ep = [{"z": [float(x) for x in z], "g": int(g), "y": int(y)} for z, g, y in zip(Z, G, Y)]
        return hashlib.sha256(json_canonique(ep)).hexdigest()
    x1[str(w["monde"])] = {"egal_a_l_etiquette_v68_du_manifeste": par_etiquette("pilote-mr2-v68|episodes-developpement") == servis,
                           "egal_a_l_etiquette_v69_du_code": par_etiquette("pilote-mr2-v69|episodes-developpement") == servis}
res["X1_derivation_des_episodes"] = {"etiquette_du_code": P.ETIQUETTE_EPISODES, "regle_ecrite_au_manifeste_dit_v68":
                                     "pilote-mr2-v68|episodes-" in L.REGLE_DES_GRAINES, "par_monde": x1}

# X7 — adresses d'amont.
x7 = {}
for d, u in (("astra", "https://api.openai.com/v1/chat/completions"), ("astra", "https://api.openai.com/v1/chat/completions/"),
             ("astra", "http://127.0.0.1:9/x"), ("astra", "http://127.0.0.1:1@exemple.org/x"), ("astra", "http://127.0.0.1.exemple.org:80/x"),
             ("claude", "https://api.anthropic.com/v1/messages?x=1"), ("claude", "http://localhost:9/v1/messages"),
             ("astra", "http://127.0.0.1:8080.exemple.org/x")):
    try:
        x7[u] = R.url_permise(d, "m", u)
    except ValueError as e:
        x7[u] = f"ValueError ({type(e).__name__})"
res["X7_adresses_d_amont"] = x7

# X3 (règle M-1) — rien de plus large qu'un suffixe de date.
res["X3_modele_servi"] = {s: C.modele_conforme(d, s) for d, s in (
    ("gpt-6-astra", "gpt-6-astra"), ("gpt-6-astra", "gpt-6-astra-2026-10-15"), ("gpt-6-astra", "gpt-6-astra-20261015"),
    ("gpt-6-astra", "gpt-6-astra-mini-2026-10-15"), ("gpt-6-astra", "gpt-6-astra-2026-10-15-preview"),
    ("gpt-6-astra", "gpt-6-astra-001"), ("gpt-6-astra", "gpt-6-astra-99999999"), ("gpt-6-astra", "gpt-6-astra2026-10-15"),
    ("claude-opus-5", "claude-opus-5-5"), ("gemini-4-argon", "models/gemini-4-argon"), ("gpt-6-astra", "GPT-6-ASTRA"))}

# X2 — Astra : la réflexion ajoutée à `completion_tokens`. Si le fournisseur la compte déjà dedans (à vérifier par la sonde), une
# réponse valide, tenue sous la borne, est lue « coût au-dessus du pire cas » : échec, et abandon du proposeur.


class Amont(BaseHTTPRequestHandler):
    recues = []

    def log_message(self, *x):
        pass

    def do_POST(self):
        corps = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
        Amont.recues.append({"cle_juste": self.headers.get("Authorization") == "Bearer cle-factice-du-contre-lecteur",
                             "cles_du_corps": sorted(corps), "max_completion_tokens": corps.get("max_completion_tokens")})
        cartes = [{"enonce": "carte", "loi_predictive": {"type": "softmax", "poids": [[0.0] * 8] * 3, "biais": [0.0, 0.0, 0.0]}}]
        rep = {"model": "gpt-6-astra", "choices": [{"index": 0, "finish_reason": "stop", "message": {
            "role": "assistant", "content": "```json\n" + json.dumps(cartes) + "\n```"}}],
            # 30 000 jetons de sortie facturés, dont 25 000 de réflexion : sous la borne de 36 000
            "usage": {"prompt_tokens": 20000, "completion_tokens": 30000, "completion_tokens_details": {"reasoning_tokens": 25000}}}
        o = json.dumps(rep).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(o)))
        self.end_headers()
        self.wfile.write(o)


amont = ThreadingHTTPServer(("127.0.0.1", 0), Amont)
threading.Thread(target=amont.serve_forever, daemon=True).start()
s = socket.socket()
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
s.close()
conf2 = copy.deepcopy(conf)
conf2["proposeurs"]["astra"].update(port=port, url_amont=f"http://127.0.0.1:{amont.server_address[1]}/v1/chat/completions")
jeton = PR.nouveau_jeton()
texte = "Consigne d'épreuve, sans monde. " + "x" * 48600  # la taille d'un texte servi, aucun contenu de monde
proc, _ = PR.lancer_relais(conf2, "astra", os.path.join(BAC, "journal-x2.jsonl"), "astra", jeton, python=sys.executable,
                           environ={"PATH": "/usr/bin:/bin", "OPENAI_API_KEY": "cle-factice-du-contre-lecteur",
                                    "AUTRE_CLE_FACTICE": "ne-doit-pas-passer"})
try:
    etat = PR.etat_relais(conf2, "astra")
    a = PR.appeler(conf2, "astra", texte, os.path.join(BAC, "x2", "astra"), jeton, python=sys.executable)
    visibles_dans_la_borne = 30000 <= conf["proposeurs"]["astra"]["borne_sortie_jetons"]
    res["X2_astra_reflexion_comptee_deux_fois"] = {
        "amont_a_recu": Amont.recues, "ecarts_de_l_etat_en_mode_reel": PR.controler_etat_relais(conf2, "astra", etat, "reel"),
        "sortie_facturee_sous_la_borne": visibles_dans_la_borne, "etat": a["etat"], "cause": a["cause"], "abandon": a["abandon"],
        "jetons_lus": a["jetons"], "cout_lu_usd": a["cout_usd"],
        "pire_cas_usd": round((len(texte.encode()) + 1024) * 10.0 / 1e6 + 36000 * 50.0 / 1e6, 6)}
    with open(f"/proc/{proc.pid}/cmdline", "rb") as f:
        res["X2_cle_absente_de_la_ligne_de_commande_du_relais"] = b"cle-factice-du-contre-lecteur" not in f.read()
finally:
    PR.arreter_relais(proc)
    amont.shutdown()
res["X2_environnement_du_relais_noms"] = sorted(PR.env_du_relais(conf["proposeurs"]["astra"], "j", {
    "PATH": "/usr/bin:/bin", "OPENAI_API_KEY": "v", "GEMINI_API_KEY": "v", "RR_ANTHROPIC_API_KEY_RIGAUD": "v", "HOME": "/x",
    "ANTHROPIC_BASE_URL": "http://exemple.org", "OPENAI_BASE_URL": "http://exemple.org"}, False))
res["X2_environnement_du_relais_a_blanc_noms"] = sorted(PR.env_du_relais(conf["proposeurs"]["astra"], "j", {
    "PATH": "/usr/bin:/bin", "OPENAI_API_KEY": "v"}, True))

# X8 — délai de l'adaptateur : coût compté.


def lent(cmd, **k):
    raise subprocess.TimeoutExpired(cmd, 1)


a = PR.appeler(conf, "astra", "t", os.path.join(BAC, "x8", "astra"), "j", python=sys.executable, executer=lent)
res["X8_delai_de_l_adaptateur"] = {"etat": a["etat"], "abandon": a["abandon"], "cout_compte_usd": a["cout_usd"],
                                   "plafond_de_session_usd": conf["proposeurs"]["astra"]["plafond_session_usd"]}

# X6 — flux de l'interface Messages : formes que la doublure des essais ne sert pas.
base = ['event: message_start\n', 'data: {"type": "message_start", "message": {"id": "m", "model": "claude-fable-5-2", '
        '"usage": {"input_tokens": 12, "output_tokens": 1}}}\n', '\n', 'event: ping\n', 'data: {"type": "ping"}\n', '\n',
        'data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}\n',
        'data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "OK"}}\n',
        'data: {"type": "content_block_stop", "index": 0}\n']
fin = ['data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": null}, "usage": {"output_tokens": 30}}\n',
       'data: {"type": "message_stop"}\n']


def flux(lignes):
    try:
        m = R.lire_flux_anthropic(lignes)
        return {"stop_reason": m.get("stop_reason"), "usage": m.get("usage"), "texte": "".join(b.get("text", "") for b in m["content"])}
    except Exception as e:  # noqa: BLE001
        return f"{type(e).__name__}"


res["X6_flux"] = {
    "sain_avec_ping": flux(base + fin),
    "second_message_delta_sans_raison_d_arret": flux(base + [fin[0], 'data: {"type": "message_delta", "delta": {}, "usage": {"output_tokens": 31}}\n', fin[1]]),
    "ligne_de_donnees_non_json": flux(base + ['data: [DONE]\n'] + fin),
    "evenement_inconnu": flux(base + ['data: {"type": "autre_evenement", "x": 1}\n'] + fin),
    "delta_avant_son_bloc": flux(base[:6] + [base[7]] + fin)}

with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    f.write("\n")
print(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
