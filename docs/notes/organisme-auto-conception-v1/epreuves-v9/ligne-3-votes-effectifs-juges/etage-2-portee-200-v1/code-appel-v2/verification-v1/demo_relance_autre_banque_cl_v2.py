"""Contre-lecture S, vérification de la v2 : ma démonstration C1 (relance sur une autre banque) rejouée contre le module v2,
plus la liste blanche d'environnement par `preparer_reel` et la forme du nom de clé. Service factice seul, aucun réseau,
aucune clé, aucun relais. Usage : <venv>/python -I -B demo_relance_autre_banque_cl_v2.py
"""
import datetime as dt
import json
import sys
from pathlib import Path

DOSSIER = Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-code-appel-etage-2")
sys.path.insert(0, str(DOSSIER / "copie-v2"))
import essais_epreuve_juges_reels_ligne_3_v2 as E  # noqa: E402
M = E.M
print("module", M.VERSION, "plafond_c", M.PLAFOND_C, "liste blanche", M.VARIABLES_PERMISES)

fonctions = M.charger_service_des_juges()
consigne = M.lire_par_empreinte(M.DEPOT / M.CONSIGNE_JUGE[0], M.CONSIGNE_JUGE[1], "consigne").decode("utf-8")
configuration = json.loads(M.lire_par_empreinte(M.DEPOT / M.CONFIGURATION[0], M.CONFIGURATION[1], "configuration"))
items = configuration["items_juge"]

base = DOSSIER / "demo-relance-v2"
base.mkdir()
racine = base / "run"
racine.mkdir()
banque_a = E.ecrire_banque(base, items, nom="banque-a.json")
banque_b = E.ecrire_banque(base, items, nom="banque-b.json",
                           contenu_de=lambda k, c: dict(c, titre=c["titre"] + " (autre banque)"))
print("banques differentes :", banque_a[1] != banque_b[1])
try:
    M.executer(racine, banque_a[0], banque_a[1], E.PLOMBERIE,
               E.faire_service(racine, E.Banc(items, E.couts_au_facteur(1), panne_a=100), fonctions, consigne, configuration),
               {"commit_depot": "essai"})
except KeyboardInterrupt:
    print("panne simulee a l'envoi 101")
journal = racine / "sortie" / "epreuve" / "journal-compteur.jsonl"
avant = journal.read_bytes()
try:
    M.executer(racine, banque_b[0], banque_b[1], E.PLOMBERIE,
               E.faire_service(racine, E.Banc(items, E.couts_au_facteur(1)), fonctions, consigne, configuration),
               {"commit_depot": "essai"})
    print("ECHEC : RELANCE SUR UNE AUTRE BANQUE ACCEPTEE")
except M.Refus as e:
    print("relance sur autre banque REFUSEE :", e)
print("journal inchange par le refus :", journal.read_bytes() == avant)
# relance saine, meme banque : doit aller au bout
rapport = M.executer(racine, banque_a[0], banque_a[1], E.PLOMBERIE,
                     E.faire_service(racine, E.Banc(items, E.couts_au_facteur(1)), fonctions, consigne, configuration),
                     {"commit_depot": "essai"})
print("relance saine : envois", rapport["envois_partis"], "cumul", rapport["cumul_compte_usd"], "arret", rapport["arret"])

# liste blanche et nom de cle, par preparer_reel
jour = dt.date(2026, 11, 20)
decl = base / "declaration.json"
octets = M.json_octets({"fournisseurs": {"claude": {}, "argon": {}}})
decl.write_bytes(octets)
hd = M.sha256_octets(octets)
Path(str(decl) + ".sha256").write_text(f"{hd}  declaration.json\n", encoding="utf-8")
registre = lambda: {"texte": E.REGISTRE, "commit": "essai", "sha256": "essai"}  # noqa: E731
appels = []
for nom, env in (("liste blanche", {"PATH": "/usr/bin", "HOME": "/tmp", "LANG": "C.UTF-8", "LC_CTYPE": "C.UTF-8",
                                    "GO_ID": "GO-2026-11-20-26"}),
                 ("vide", {}), ("HTTPS_PROXY", {"HTTPS_PROXY": "http://127.0.0.1:1"}),
                 ("autre variable", {"PYTHONPATH": "x"}), ("jeton", {"GITHUB_TOKEN": "x"})):
    try:
        M.preparer_reel(E._argv(base, banque_a[0], banque_a[1], decl, hd), env, jour, lire_registre=registre,
                        construire_service=lambda **kw: (appels.append(kw), (None, {}))[1])
        print("environnement", nom, ": accepte")
    except M.Refus as e:
        print("environnement", nom, ": REFUS :", str(e)[:110])
print("services construits (attendu 2 : liste blanche et vide) :", len(appels))
for nom_cle in ("nom_minuscule", "A", "NOM_VALIDE_1"):
    argv = E._argv(base, banque_a[0], banque_a[1], decl, hd)[:-1] + [nom_cle]
    try:
        M.preparer_reel(argv, {}, jour, lire_registre=registre, construire_service=lambda **kw: (None, {}))
        print("nom de cle", nom_cle, ": accepte")
    except M.Refus as e:
        print("nom de cle", nom_cle, ": REFUS :", str(e)[:90])
