# limite de tâches du bac (essai à 32) : le bac refuse les processus au-delà
import subprocess

procs = []
try:
    for _ in range(200):
        procs.append(subprocess.Popen(["sleep", "30"]))
except OSError as e:
    print("REFUS", len(procs), type(e).__name__)
else:
    print("LANCES", len(procs))
finally:
    for p in procs:
        p.kill()
        p.wait()
