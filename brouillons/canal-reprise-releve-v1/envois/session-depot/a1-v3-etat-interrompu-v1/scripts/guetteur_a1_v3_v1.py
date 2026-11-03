#!/usr/bin/python3
"""Guetteur A1-v3 : toutes les 5 min, vérifie que le relais (par PID) vit ; s'il est mort, le relance avec les mêmes valeurs.
N'arrête jamais rien. Relève /relais/etat (compteurs seulement) toutes les heures. Signale au journal tout appel du relais
en échec (statuts et compteurs seulement, jamais de texte). S'arrête de lui-même quand le processus de la course a disparu."""
import json, os, subprocess, time, urllib.request, datetime
D = "/home/user/hors-clone-a1-v3"
J = f"{D}/journal-guetteur-a1-v3-v1.log"
JR = f"{D}/relais-argon-journal-a1-v3.jsonl"
ALERTES = f"{D}/alertes-a1-v3-v1.log"
def t(): return datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
def log(m, f=J):
    with open(f, "a") as h: h.write(f"{t()} {m}\n")
def vivant(pid):
    try:
        with open(f"/proc/{pid}/stat") as h: return h.read().split(")")[-1].split()[0] != "Z"
    except OSError: return False
def etat():
    o = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    d = json.load(o.open("http://127.0.0.1:8805/relais/etat", timeout=10))
    return {k: d.get(k) for k in ("pid", "appels", "max_appels", "depense_usd", "engage_usd", "plafond_usd", "refus", "cle_presente")}
course = int(open(f"{D}/course.pid").read())
lus = 0; dernier_etat = 0
log(f"guetteur démarré (PID {os.getpid()}), course PID {course}")
while True:
    relais = int(open(f"{D}/relais-argon.pid").read())
    if not vivant(course):
        log(f"processus de la course {course} disparu ; guetteur s'arrête (n'arrête rien)")
        try: log(f"/relais/etat final : {json.dumps(etat())}")
        except Exception as e: log(f"/relais/etat final illisible : {type(e).__name__}")
        break
    if not vivant(relais):
        log(f"relais PID {relais} mort : relance avec les mêmes valeurs")
        log(f"ALERTE relais PID {relais} mort, relancé", ALERTES)
        nouveau = subprocess.run([f"{D}/scripts/lancer_relais_argon_v1.sh"], capture_output=True, text=True).stdout.strip()
        log(f"relais relancé PID {nouveau}")
    else:
        log(f"relais PID {relais} vivant ; course PID {course} vivante")
    try:
        with open(JR) as h: lignes = h.readlines()
        for l in lignes[lus:]:
            try: d = json.loads(l)
            except Exception: continue
            if d.get("echec") or (d.get("statut") not in (None, "ok", "OK")):
                log(f"ALERTE appel {d.get('appel')} statut={d.get('statut')!r} fin={d.get('fin')!r} echec={'oui' if d.get('echec') else 'non'} quand={d.get('quand_utc')}", ALERTES)
        lus = len(lignes)
    except OSError: pass
    if time.time() - dernier_etat >= 3600:
        try: log(f"/relais/etat : {json.dumps(etat())}")
        except Exception as e: log(f"/relais/etat illisible : {type(e).__name__}")
        dernier_etat = time.time()
    time.sleep(300)
