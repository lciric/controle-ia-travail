import sys, os, json, tempfile, importlib.util, threading, datetime as dt, multiprocessing as mp
P = "/home/user/controle-ia-travail/docs/notes/memoire-conception-v1/appel-google-garde-v3-v3/appel_google_garde_v3_v3.py"
def charger():
    spec = importlib.util.spec_from_file_location("s", P); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s); return s
class R:
    status = 200
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def __iter__(self):
        import time; time.sleep(0.2)
        return iter([b'data: {"candidates":[{"content":{"parts":[{"text":"x"}]}}]}'])
def un(args):
    i, d = args
    os.environ["GEMINI_API_KEY"] = "F"
    s = charger()
    e = os.path.join(d, f"e{i}.md"); open(e, "w").write("Reponds en 400 mots.")
    sys.stderr = open(os.devnull, "w"); sys.stdout = open(os.devnull, "w")
    return s.main(["argon", e, os.path.join(d, f"o{i}.md"), os.path.join(d, f"o{i}.json"), "--journal", os.path.join(d, "j.jsonl")],
                  ouvrir=lambda req, timeout=None: R(), maintenant=dt.datetime(2026, 11, 22, tzinfo=dt.timezone.utc))
if __name__ == "__main__":
    d = tempfile.mkdtemp()
    with mp.Pool(6) as p: codes = p.map(un, [(i, d) for i in range(6)])
    L = [json.loads(l) for l in open(os.path.join(d, "j.jsonl"))]
    print("codes", sorted(codes), "reserves", sum(l["etat"] == "reserve" for l in L), "soldes", sum(l["etat"] == "solde" for l in L))
