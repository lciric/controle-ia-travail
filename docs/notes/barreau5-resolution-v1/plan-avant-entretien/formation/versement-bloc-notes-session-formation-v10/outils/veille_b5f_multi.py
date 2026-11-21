"""Veille de plusieurs instances de formation du barreau 5 (plan de marche v1, points 2.3 et 2.5 ; cumul fixé par la mère
le 20 novembre vers 10:38Z : heures × prix par instance, somme pour le commun).

Usage : python -I veille_b5f_multi.py CONFIG.json ETAT.json JOURNAL.txt
CONFIG : {"membres": 3, "commun_fixe": <USD des pièces finies>, "instances": {"<n>": {"id": ID, "h": epoch}, ...},
          "suivies": ["<n>", ...]}
Toutes les PAS secondes : liste du loueur, crédit (journal seulement), garde de dépense du lanceur figé par instance, lignes
« B5F » de l'amorce. Ne lit que le loueur, l'horloge et les lignes « B5F » du journal de l'amorce (jamais une sortie).
Sort : 10 ligne d'étape neuve, 20 ARRET/SIGNAL/fin, 30 refus d'une garde de dépense, 40 instance suivie absente ou hors
marche, 50 erreur répétée du loueur. La sortie dit quelle instance. L'état (lignes vues) est gardé dans ETAT.json.
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone

S = "/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad"
V = f"{S}/venv-vast/bin/vastai"
LANCEUR = f"{S}/arbre-course/scripts/lancer_b5f_formation_v1.sh"
PAS = int(os.environ.get("PAS_VEILLE_S", "600"))
ETAPES = ("minuterie lancée", "dépôt au commit", "essais du paquet", "modèle au cache", "marche : début",
          "marche lancée", "marche : code", "versement final prouvé", "NON PROUVÉ", "fin, code", "FIN :")
ALERTES = ("ARRET", "SIGNAL", "MINUTERIE :", "NON PROUVÉ", "hors de la liste blanche", "plus de 94000000")

conf_f, etat_f, journal = sys.argv[1:4]
conf = json.load(open(conf_f))
etat = json.load(open(etat_f)) if os.path.exists(etat_f) else {"vues": {}}


def ecrire(msg):
    ligne = f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} {msg}"
    print(ligne, flush=True)
    with open(journal, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def loueur(*args):
    r = subprocess.run([V, *args], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f"loueur {args[:2]} : code {r.returncode}")
    return r.stdout


erreurs = 0
while True:
    suivies = conf["suivies"]
    try:
        liste = json.loads(loueur("show", "instances", "--raw"))
        liste = liste.get("instances", liste) if isinstance(liste, dict) else liste
        credit = float(json.loads(loueur("show", "user", "--raw"))["credit"])
        logs = {n: loueur("logs", str(conf["instances"][n]["id"]), "--tail", "400") for n in suivies}
        erreurs = 0
    except Exception as x:  # noqa: BLE001
        erreurs += 1
        ecrire(f"erreur du loueur ({erreurs}) : {type(x).__name__}")
        if erreurs >= 3:
            sys.exit(50)
        time.sleep(60)
        continue
    maintenant = datetime.now(timezone.utc).timestamp()
    par_id = {str(x.get("id")): x for x in liste}
    cumuls, prix, etats = {}, {}, {}
    for n, d in conf["instances"].items():
        x = par_id.get(str(d["id"]))
        p = float(x.get("dph_total") or 0) if x else float(d.get("prix", 0))
        d["prix"] = p
        fin = d.get("fin") or maintenant
        cumuls[n] = (fin - d["h"]) / 3600 * p
        prix[n] = p
        etats[n] = x.get("actual_status") if x else "absente"
    commun = conf["commun_fixe"] + sum(cumuls.values())
    prix_commun = sum(prix[n] for n in suivies)
    refus = []
    for n in suivies:
        g = subprocess.run(["bash", LANCEUR, "depense", n, str(conf["membres"]), f"{cumuls[n]:.4f}", f"{prix[n]:.4f}",
                            f"{commun:.4f}", f"{prix_commun:.4f}", "0"], capture_output=True, text=True,
                           env={**os.environ, "PYTHON_B5F": f"{S}/venv-b5f/bin/python"})
        if g.returncode != 0:
            refus.append(n)
    ecrire("crédit {:.2f} ; commun {:.2f} USD ; ".format(credit, commun) + " ; ".join(
        f"{n}:{etats[n]} {cumuls[n]:.2f}" for n in suivies) + (f" ; REFUS de la garde : {refus}" if refus else ""))
    neuves = []
    for n in suivies:
        vues = etat["vues"].setdefault(n, [])
        for l in logs[n].splitlines():
            if " B5F " not in l:
                continue
            l = re.sub(r"[A-Za-z0-9_]{36,}", "<masqué>", l)[:300]
            if l in vues:
                continue
            vues.append(l)
            if any(e in l for e in ETAPES + ALERTES):
                neuves.append((n, l))
    json.dump(etat, open(etat_f, "w"))
    json.dump(conf, open(conf_f, "w"), indent=1)
    for n, l in neuves:
        ecrire(f"LIGNE {n} {l}")
    if refus:
        sys.exit(30)
    if any(a in l for _, l in neuves for a in ALERTES) or any("fin, code" in l for _, l in neuves):
        sys.exit(20)
    if neuves:
        sys.exit(10)
    if any(etats[n] not in ("loading", "running", "created", None) for n in suivies):
        ecrire("hors marche : " + ", ".join(n for n in suivies if etats[n] not in ("loading", "running", "created", None)))
        sys.exit(40)
    time.sleep(PAS)
