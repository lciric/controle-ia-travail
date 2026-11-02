"""Guetteur « saute Kimi s'il coupe », v3 (session fille, 2 novembre 2026), après l'erratum du v2 (arrêt fautif de 10:39:15).
Lecture d'une entrée du journal du relais Kimi : SUCCÈS si et seulement si statut_amont == 200 ; ÉCHEC pour tout le reste
(champ « statut » compris). Règle de la session mère (10:41 UTC), état neuf sur le journal v2 :
critère 1 = les 2 dernières entrées sont des échecs ; critère 2 = aucun succès dans les 45 min qui suivent la reprise (10:40:44)
alors qu'un appel est en cours. Si un critère est atteint : relais Kimi arrêté par son PID seulement (vérifié par /proc, R10),
consignation, fichier KIMI-SAUTE-V3. Ne touche ni à la course ni au relais Argon. Sort quand la course a fini.
Mode d'essai : --essai JOURNAL [--maintenant ISO] [--en-cours N] : lit le journal, imprime la classification et la décision,
n'arrête rien."""
import argparse, datetime, json, os, signal, time, urllib.request
D = os.path.dirname(os.path.abspath(__file__))
PID_K, PID_C = 9209, 6064
J = os.path.join(D, "relais-kimi-journal-v2.jsonl"); L = os.path.join(D, "journal-lancement-a1-v1.log")
REPRISE = datetime.datetime(2026, 11, 2, 10, 40, 44, tzinfo=datetime.timezone.utc)
def utc(): return datetime.datetime.now(datetime.timezone.utc)
def succes(e): return e.get("statut_amont") == 200
def lire(j): return [json.loads(l) for l in open(j)] if os.path.exists(j) else []
def decider(E, maintenant, en_cours):
    c1 = len(E) >= 2 and not succes(E[-1]) and not succes(E[-2])
    c2 = (not any(succes(e) for e in E)) and en_cours > 0 and (maintenant - REPRISE).total_seconds() > 2700
    return c1, c2
def vivant(pid, motif):
    try: return motif in open(f"/proc/{pid}/cmdline", "rb").read().replace(b"\0", b" ").decode()
    except OSError: return False
def etat(): return json.load(urllib.request.build_opener(urllib.request.ProxyHandler({})).open("http://127.0.0.1:8804/relais/etat", timeout=5))
a = argparse.ArgumentParser(); a.add_argument("--essai"); a.add_argument("--maintenant"); a.add_argument("--en-cours", type=int, default=0)
a = a.parse_args()
if a.essai:
    E = lire(a.essai); m = datetime.datetime.fromisoformat(a.maintenant) if a.maintenant else utc()
    print("classement :", ["succès" if succes(e) else "échec" for e in E], "décision (c1, c2) :", decider(E, m, a.en_cours)); raise SystemExit(0)
while True:
    if not vivant(PID_C, "attaque_goodhart_v2.py"): print(f"{utc():%FT%TZ} course finie : guetteur arrêté, rien fait", flush=True); break
    if not vivant(PID_K, "relais_kimi_v3.py"): print(f"{utc():%FT%TZ} relais Kimi {PID_K} absent : guetteur arrêté", flush=True); break
    E = lire(J)
    try: en_cours = etat()["appels"] - len(E)
    except Exception: en_cours = -1
    c1, c2 = decider(E, utc(), en_cours)
    print(f"{utc():%FT%TZ} finis {len(E)} {['S' if succes(e) else 'E' for e in E[-3:]]}, en cours {en_cours}, c1 {c1}, c2 {c2}", flush=True)
    if c1 or c2:
        crit = "critère 1 (2 échecs d'affilée)" if c1 else "critère 2 (aucun succès 45 min après la reprise, appel en cours)"
        try: json.dump(etat(), open(os.path.join(D, "etat-relais-kimi-v2-avant-arret.json"), "x"), ensure_ascii=False)
        except Exception: pass
        t = utc()
        if vivant(PID_K, "relais_kimi_v3.py"):
            os.kill(PID_K, signal.SIGTERM); time.sleep(5)
            if vivant(PID_K, "relais_kimi_v3.py"): os.kill(PID_K, signal.SIGKILL)
        derniers = [(e.get("statut"), e.get("statut_amont"), e.get("motif")) for e in E[-2:]]
        msg = f"{t:%FT%TZ} « saute Kimi » v3 : {crit} ; dernières entrées (statut, statut_amont, motif) {derniers} ; SIGTERM au relais Kimi PID {PID_K} à {t:%FT%TZ} (R10) ; course et relais Argon intacts ; pas de relance."
        open(L, "a").write(msg + "\n"); print(msg, flush=True); open(os.path.join(D, "KIMI-SAUTE-V3"), "x").write(msg + "\n"); break
    time.sleep(60)
