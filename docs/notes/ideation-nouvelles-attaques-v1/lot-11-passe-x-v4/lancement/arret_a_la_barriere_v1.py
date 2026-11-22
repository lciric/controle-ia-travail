import os, signal, sys, time, datetime
J = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/lancement/journal-passe-x-20261122T130454Z.jsonl"
PID = 14688
pos = 0
while True:
    try:
        os.kill(PID, 0)
    except OSError:
        print("exécutant déjà terminé", flush=True); sys.exit(0)
    with open(J, "rb") as f:
        f.seek(pos); morceau = f.read(); pos += len(morceau)
    if b'"type_ligne": "barri' in morceau:
        os.kill(PID, signal.SIGKILL)
        print(datetime.datetime.utcnow().strftime("%H:%M:%S.%fZ"), "SIGKILL au PID", PID, "à la barrière", flush=True)
        sys.exit(0)
    time.sleep(0.02)
