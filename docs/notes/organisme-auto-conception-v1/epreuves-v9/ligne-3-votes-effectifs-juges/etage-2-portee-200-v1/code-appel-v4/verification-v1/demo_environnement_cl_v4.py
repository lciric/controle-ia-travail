"""Contre-lecture S, vérification de la v4 : départ réel par `preparer_reel` (service et registre factices, aucun réseau, aucune clé,
aucun relais) sous divers environnements : sain sans nom de clé, refus pour chaque nom de clé, mandataire absent, variable hors liste.
Usage : <venv>/python -I -B demo_environnement_cl_v4.py
"""
import datetime as dt
import sys
from pathlib import Path

DOSSIER = Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-code-appel-etage-2")
sys.path.insert(0, str(DOSSIER / "copie-v4"))
import essais_epreuve_juges_reels_ligne_3_v4 as E  # noqa: E402
M = E.M
import json  # noqa: E402

configuration = json.loads(M.lire_par_empreinte(M.DEPOT / M.CONFIGURATION[0], M.CONFIGURATION[1], "configuration"))
base = DOSSIER / "demo-env-v4"
base.mkdir()
banque, h = E.ecrire_banque(base, configuration["items_juge"])
decl = base / "declaration.json"
octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
decl.write_bytes(octets)
hd = M.sha256_octets(octets)
Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
registre = lambda: {"texte": E.REGISTRE, "commit": "essai", "sha256": "essai"}  # noqa: E731
print("module", M.VERSION, "| exigees", M.VARIABLES_EXIGEES, "| permises", len(M.VARIABLES_PERMISES))
print("noms de cle dans la liste blanche :", [n for n in M.VARIABLES_PERMISES if "KEY" in n or "TOKEN" in n or "SECRET" in n])
CERTS = {n: "factice" for n in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NODE_EXTRA_CA_CERTS")}
PROXY = {n: "factice" for n in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "NO_PROXY", "no_proxy")}
cas = [
    ("sain : mandataire, certificats, PATH, HOME, GO_ID, aucun nom de cle", dict(PROXY, **CERTS, PATH="/usr/bin", HOME="/tmp", GO_ID="GO-2026-11-20-26")),
    ("sain minimal : HTTPS_PROXY seul", {"HTTPS_PROXY": "factice"}),
    ("RR_ANTHROPIC_API_KEY_LUC present", dict(PROXY, RR_ANTHROPIC_API_KEY_LUC="x")),
    ("GEMINI_API_KEY present", dict(PROXY, GEMINI_API_KEY="x")),
    ("les deux noms presents", dict(PROXY, RR_ANTHROPIC_API_KEY_LUC="x", GEMINI_API_KEY="x")),
    ("sans HTTPS_PROXY (https_proxy seul)", {"https_proxy": "factice", "PATH": "/usr/bin"}),
    ("environnement vide", {}),
    ("ALL_PROXY hors liste", dict(PROXY, ALL_PROXY="x")),
    ("PYTHONPATH hors liste", dict(PROXY, PYTHONPATH="x")),
    ("jeton quelconque", dict(PROXY, GITHUB_TOKEN="x")),
]
construits = []
for nom, env in cas:
    try:
        M.preparer_reel(E._argv(base, banque, h, decl, hd), env, dt.date(2026, 11, 20), lire_registre=registre,
                        construire_service=lambda **kw: (construits.append(kw), (None, {}))[1])
        print("ACCEPTE :", nom)
    except M.Refus as e:
        print("REFUS   :", nom, "->", str(e)[:120])
print("services construits (attendu 2) :", len(construits))
