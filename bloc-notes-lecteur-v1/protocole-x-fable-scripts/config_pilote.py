"""Clés N, T, épisodes par tâche et modèle de l'agent dans la configuration scellée du pilote de l'environnement (branche main).
N'affiche que ces valeurs et les noms des clés de premier niveau."""
import hashlib, json, subprocess
DEPOT = "/home/user/controle-ia-travail"
CHEMIN = "prereg/T0.5-pilote-config-v1.json"
brut = subprocess.run(["git", "-C", DEPOT, "show", f"main:{CHEMIN}"], check=True, capture_output=True).stdout
print("sha256", hashlib.sha256(brut).hexdigest(), "octets", len(brut))
c = json.loads(brut.decode("utf-8"))
print("clés de premier niveau:", list(c.keys()))
for k in ("N", "T", "episodes_par_tache", "max_nouveaux", "temperature"):
    if k in c:
        print(k, "=", c[k])
def chercher(o, chemin=""):
    if isinstance(o, dict):
        for k, v in o.items():
            p = f"{chemin}.{k}" if chemin else k
            if isinstance(v, str) and any(m in v.lower() for m in ("llama", "qwen", "meta-")):
                print("  ", p, "=", v)
            chercher(v, p)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            chercher(v, f"{chemin}[{i}]")
chercher(c)
