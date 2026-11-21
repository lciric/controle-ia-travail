"""Essai d'artefact (M1) : étalonnage jouet par le point d'entrée, interrompu par SIGTERM après le cinquième lot ; on vérifie que
les lots restent scellés et qu'un `arret.json` dit l'étape et le motif. Appel : python3 ce_script.py DEPOT_JOUET ARBRE"""
import json, os, signal, subprocess, sys, time
from pathlib import Path
D, A = Path(sys.argv[1]), Path(sys.argv[2])
run = "20991231-000102-iib-jouet"
env = {k: v for k, v in os.environ.items() if k != "IIB_GO_ID"}
env.update({"PYTHONPATH": str(A / "src"), "PATH": "/usr/bin:/bin"})
p = subprocess.Popen([sys.executable, "-m", "controle_ia.iib.lanceur_v5", "--phase", "etalonnage", "--config",
                      "entrees/config-iib-v5-jouet.json", "--run-id", run], cwd=D, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
lots = D / "diag" / run / "lots"
t0 = time.time()
while time.time() - t0 < 120 and not (lots.is_dir() and len(list(lots.glob("lot-005-*.json"))) >= 1):
    time.sleep(0.2)
p.send_signal(signal.SIGTERM)
out, err = p.communicate(timeout=60)
print("code de sortie", p.returncode)
print("lots écrits", len(list(lots.glob("lot-*.json"))), "; ids écrits", len(list((D / "donnees" / run / "lots").glob("ids-lot-*.json"))))
a = D / "diag" / run / "arret.json"
print("arret.json présent", a.is_file())
if a.is_file():
    r = json.loads(a.read_text(encoding="utf-8")).get("resultat", json.loads(a.read_text(encoding="utf-8")))
    print("étape", r.get("etape"), "; motif", str(r.get("motif"))[:120], "; écrits listés", len(r.get("ecrits_avant_l_arret", [])))
m=[l for l in err.splitlines() if l.startswith("PROGRES")]; print("dernière marque", m[-1][:120] if m else None); print("fin de la sortie d erreur", err[-300:].replace(chr(10)," | "))
print("étalonnage final absent", not (D / "diag" / run / "etalonnage-oracles-iib-v5.json").exists())
