"""Guetteur « saute Kimi s'il coupe » (mot de Lazar relayé par la session mère, 2 novembre 2026, ≈ 10:16 UTC) pour A1.
Toutes les 300 s : critère 1 = 3 derniers appels Kimi finis en échec (statut ≠ 200) ; critère 2 = aucun appel Kimi fini
(réussi ou non) depuis 900 s alors qu'un appel est en cours (lecture par défaut de la session fille, signalée à la mère).
Si un critère est atteint : état final du relais relevé, relais Kimi arrêté par son PID (5960, vérifié par /proc, R10),
consignation dans journal-lancement-a1-v1.log. Ne touche ni à la course (6064) ni au relais Argon (5961). Sort quand A1 a fini."""
import datetime, json, os, signal, sys, time, urllib.request
D = os.path.dirname(os.path.abspath(__file__)); PID_K, PID_C = 5960, 6064
J = os.path.join(D, "relais-kimi-journal.jsonl"); L = os.path.join(D, "journal-lancement-a1-v1.log")
DEPART = datetime.datetime(2026, 11, 2, 9, 58, 45, tzinfo=datetime.timezone.utc)
def now(): return datetime.datetime.now(datetime.timezone.utc)
def vivant(pid, motif):
    try: return motif in open(f"/proc/{pid}/cmdline", "rb").read().replace(b"\0", b" ").decode()
    except OSError: return False
def etat():
    return json.load(urllib.request.build_opener(urllib.request.ProxyHandler({})).open("http://127.0.0.1:8804/relais/etat", timeout=5))
while True:
    if not vivant(PID_C, "attaque_goodhart_v2.py"): print(f"{now():%FT%TZ} A1 fini : guetteur arrêté, rien fait"); break
    if not vivant(PID_K, "relais_kimi_v3.py"): print(f"{now():%FT%TZ} relais Kimi déjà absent : guetteur arrêté"); break
    E = [json.loads(l) for l in open(J)] if os.path.exists(J) else []
    try: e = etat(); en_cours = e["appels"] - len(E)
    except Exception as ex: e, en_cours = None, -1
    fins = [x for x in E if x.get("statut") != 200]
    c1 = len(E) >= 3 and all(x.get("statut") != 200 for x in E[-3:])
    dernier = datetime.datetime.fromisoformat(E[-1]["quand_utc"]) if E else DEPART
    c2 = en_cours > 0 and (now() - dernier).total_seconds() > 900
    print(f"{now():%FT%TZ} finis {len(E)}, en cours {en_cours}, derniers statuts {[x.get('statut') for x in E[-3:]]}, c1 {c1}, c2 {c2}", flush=True)
    if c1 or c2:
        crit = "critère 1 (3 échecs d'affilée)" if c1 else f"critère 2 (aucun appel fini depuis {int((now()-dernier).total_seconds())} s, {en_cours} en cours)"
        try: json.dump(etat(), open(os.path.join(D, "etat-relais-kimi-avant-arret.json"), "x"), ensure_ascii=False)
        except Exception: pass
        if vivant(PID_K, "relais_kimi_v3.py"):
            os.kill(PID_K, signal.SIGTERM); time.sleep(5)
            if vivant(PID_K, "relais_kimi_v3.py"): os.kill(PID_K, signal.SIGKILL)
        derniers = [(x.get("statut"), x.get("motif")) for x in E[-3:]]
        msg = f"{now():%FT%TZ} « saute Kimi » : {crit} ; derniers statuts et motifs {derniers} ; relais Kimi arrêté par PID {PID_K} (R10) ; course {PID_C} et relais Argon 5961 intacts ; pas de relance."
        open(L, "a").write(msg + "\n"); print(msg, flush=True)
        open(os.path.join(D, "KIMI-SAUTE"), "x").write(msg + "\n"); break
    time.sleep(300)
