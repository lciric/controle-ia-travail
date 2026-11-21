"""Veille de l'instance de formation du barreau 5 (plan de marche v1, points 2.3 et 2.5).

Usage : python -I veille_b5f.py ID N MEMBRES H_ISO CREDIT0 ETAT.json JOURNAL.txt
Toutes les PAS secondes : liste du loueur, crédit, garde de dépense du lanceur figé, lignes « B5F » de l'amorce.
Ne lit que le loueur, l'horloge et les lignes « B5F » du journal de l'amorce (jamais une sortie de la marche).
Sort (pour réveiller la session) : code 10 sur une ligne d'étape neuve, 20 sur ARRET/SIGNAL/fin, 30 sur refus de la
garde de dépense, 40 si l'instance n'est plus en marche ou a disparu, 50 sur erreur répétée du loueur.
L'état (crédit précédent, recharges constatées, lignes déjà vues) est gardé dans ETAT.json entre deux lancements.
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone

S = "/tmp/claude-0/-home-user-controle-ia-travail/4d216d9c-8888-53e9-a254-d89b28078848/scratchpad"
V = f"{S}/venv-vast311/bin/vastai"
LANCEUR = f"{S}/arbre-course/scripts/lancer_b5f_formation_v1.sh"
PAS = int(os.environ.get("PAS_VEILLE_S", "600"))
ETAPES = ("minuterie lancée", "dépôt au commit", "essais du paquet", "modèle au cache", "marche : début",
          "marche lancée", "marche : code", "versement final prouvé", "NON PROUVÉ", "fin, code", "FIN :")
ALERTES = ("ARRET", "SIGNAL", "MINUTERIE :", "NON PROUVÉ", "hors de la liste blanche", "plus de 94000000")

ident, n, membres, h_iso, credit0, etat_f, journal = sys.argv[1:8]
h = datetime.strptime(h_iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
etat = json.load(open(etat_f)) if os.path.exists(etat_f) else {"credit_prec": float(credit0), "recharges": 0.0, "vues": []}


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
    try:
        liste = json.loads(loueur("show", "instances", "--raw"))
        liste = liste.get("instances", liste) if isinstance(liste, dict) else liste
        credit = float(json.loads(loueur("show", "user", "--raw"))["credit"])
        logs = loueur("logs", str(ident), "--tail", "400")
        erreurs = 0
    except Exception as x:  # noqa: BLE001
        erreurs += 1
        ecrire(f"erreur du loueur ({erreurs}) : {type(x).__name__}")
        if erreurs >= 3:
            sys.exit(50)
        time.sleep(60)
        continue
    if credit > etat["credit_prec"] + 0.5:          # recharge automatique constatée
        etat["recharges"] += credit - etat["credit_prec"]
        ecrire(f"recharge constatée : +{credit - etat['credit_prec']:.2f} USD")
    etat["credit_prec"] = credit
    inst = [x for x in liste if str(x.get("id")) == str(ident)]
    heures = (datetime.now(timezone.utc) - h).total_seconds() / 3600
    if not inst:
        json.dump(etat, open(etat_f, "w"))
        ecrire(f"instance {ident} absente de la liste")
        sys.exit(40)
    x = inst[0]
    prix = float(x.get("dph_total") or 0)
    cumul = max(heures * prix, float(credit0) - credit + etat["recharges"])
    g = subprocess.run(["bash", LANCEUR, "depense", n, membres, f"{cumul:.4f}", f"{prix:.4f}", f"{cumul:.4f}",
                        f"{prix:.4f}", "0"], capture_output=True, text=True,
                       env={**os.environ, "PYTHON_B5F": f"{S}/venv-b5f/bin/python"})
    ecrire(f"état {x.get('actual_status')} ; {heures:.2f} h ; prix {prix:.4f} USD/h ; crédit {credit:.2f} ; "
           f"cumul {cumul:.2f} USD ; garde de dépense code {g.returncode}")
    neuves = []
    for l in logs.splitlines():
        if " B5F " not in l:
            continue
        l = re.sub(r"[A-Za-z0-9_]{36,}", "<masqué>", l)[:300]
        if l in etat["vues"]:
            continue
        etat["vues"].append(l)
        if any(e in l for e in ETAPES + ALERTES):
            neuves.append(l)
    json.dump(etat, open(etat_f, "w"))
    for l in neuves:
        ecrire("LIGNE " + l)
    if g.returncode != 0:
        sys.exit(30)
    if any(a in l for l in neuves for a in ALERTES) or any("fin, code" in l for l in neuves):
        sys.exit(20)
    if neuves:
        sys.exit(10)
    if x.get("actual_status") not in (None, "loading", "running", "created"):
        sys.exit(40)
    time.sleep(PAS)
