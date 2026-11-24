import importlib.util, os, sys, json
sys.path.insert(0, "/home/user/controle-ia-travail/src")
spec = importlib.util.spec_from_file_location("c", "/home/user/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8n.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
os.environ["GEMINI_API_KEY"] = "cle-factice"
m = dict(c.MODELES_CATALOGUE["carbon"] if hasattr(c, "MODELES_CATALOGUE") else c.CATALOGUE["carbon"], espece="carbon")
print("niveau", m.get("niveau_reflexion"), "max", m["max"], "delai", m["delai_s"])
fini = {"id": "v1_abc", "status": "completed", "model": "gemini-4-carbon",
        "usage": {"total_input_tokens": 100, "total_output_tokens": 50, "total_thought_tokens": 200, "total_tokens": 350},
        "steps": [{"type": "user_input"}, {"type": "thought", "signature": "x"},
                  {"type": "model_output", "content": [{"type": "text", "text": "Bonjour."}]}]}
seq = [{"id": "v1_abc", "status": "in_progress"}, {"id": "v1_abc", "status": "in_progress"}, fini]
envois = []
def faux(requete, delai, cle):
    envois.append((requete.get_method(), requete.full_url, json.loads(requete.data) if requete.data else None))
    return seq.pop(0)
c.lire_json = faux; c.DORMIR = lambda s: None
r = c.appeler_gemini_arriere_plan(m, "Bonjour ?", m["max"])
for e in envois: print(e[0], e[1], e[2])
print(r)
print("statut", c.juger(m, r, "Bonjour ?", 9.9, garde=10**6, max_tokens=m["max"]))
seq[:] = [{"id": "v1_abc", "status": "failed", "error": {"code": 500}}]
r = c.appeler_gemini_arriere_plan(m, "x", m["max"]); print("echec:", r.echec, r.interrompue)
