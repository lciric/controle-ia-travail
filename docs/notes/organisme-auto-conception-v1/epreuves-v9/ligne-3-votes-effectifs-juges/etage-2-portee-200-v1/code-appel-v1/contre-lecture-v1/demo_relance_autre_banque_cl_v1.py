"""Contre-lecture S : une relance sur une AUTRE banque scellée que celle du journal est-elle refusée ?
Service factice seul (aides des essais du développeur), aucun réseau, aucune clé, aucun relais.
Usage : <venv>/python -I -B demo_relance_autre_banque_cl_v1.py
"""
import json
import sys
from pathlib import Path

DOSSIER = Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-code-appel-etage-2")
sys.path.insert(0, str(DOSSIER / "copie"))
import essais_epreuve_juges_reels_ligne_3_v1 as E  # noqa: E402
M = E.M

fonctions = M.charger_service_des_juges()
consigne = M.lire_par_empreinte(M.DEPOT / M.CONSIGNE_JUGE[0], M.CONSIGNE_JUGE[1], "consigne").decode("utf-8")
configuration = json.loads(M.lire_par_empreinte(M.DEPOT / M.CONFIGURATION[0], M.CONFIGURATION[1], "configuration"))
items = configuration["items_juge"]

base = DOSSIER / "demo-relance-2"
base.mkdir(exist_ok=True)
racine = base / "run"
racine.mkdir()
banque_a = E.ecrire_banque(base, items, nom="banque-a.json")
banque_b = E.ecrire_banque(base, items, nom="banque-b.json",
                           contenu_de=lambda k, c: dict(c, titre=c["titre"] + " (autre banque)"))
print("banques differentes :", banque_a[1] != banque_b[1])
banc = E.Banc(items, E.couts_au_facteur(1), panne_a=100)
try:
    M.executer(racine, banque_a[0], banque_a[1], E.PLOMBERIE, E.faire_service(racine, banc, fonctions, consigne, configuration),
               {"commit_depot": "essai"})
except KeyboardInterrupt:
    print("panne simulee a l'envoi 101")
try:
    rapport = M.executer(racine, banque_b[0], banque_b[1], E.PLOMBERIE,
                         E.faire_service(racine, E.Banc(items, E.couts_au_facteur(1)), fonctions, consigne, configuration),
                         {"commit_depot": "essai"})
    print("RELANCE SUR UNE AUTRE BANQUE ACCEPTEE : envois_partis", rapport["envois_partis"], "cumul", rapport["cumul_compte_usd"])
except M.Refus as e:
    print("relance refusee :", e)
journal = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
lignes = [json.loads(x) for x in journal.read_text(encoding="utf-8").splitlines()]
print("ouverture banque_sha256 :", lignes[0]["banque_sha256"] == banque_a[1], "; rendus distincts du journal :",
      len({l["rendu"] for l in lignes if l["type"] == "engagement"}))
