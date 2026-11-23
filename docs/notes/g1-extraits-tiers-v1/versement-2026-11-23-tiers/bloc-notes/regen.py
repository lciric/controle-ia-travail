import sys, json, hashlib, importlib.util
from pathlib import Path
sys.dont_write_bytecode = True
D = Path("/home/user/controle-ia-travail")
spec = importlib.util.spec_from_file_location("ex", D/"docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
for nom in sys.argv[1:]:
    chemin = f"docs/notes/g1-extraits-tiers-v1/fiches/{nom}"
    fiche = json.loads((D/chemin).read_text(encoding="utf-8"))
    texte = ex.fabriquer(fiche, chemin)
    disque = (D/fiche["sortie"]).read_bytes()
    print(nom, "identique" if texte.encode("utf-8")==disque else "DIFFÉRENT", hashlib.sha256(texte.encode()).hexdigest())
    # check verbatim: each kept line in extract equals source line (modulo marks)
    src = (D/fiche["source"]).read_bytes().decode().split("\n")
    if src[-1]=="": src=src[:-1]
    ext = disque.decode().split("\n")
    # locate kept blocks
    i=0; nbad=0; nkept=0
    while i < len(ext):
        l = ext[i]
        if l.startswith("<!-- lignes ") and l.endswith(" de la source -->"):
            a,b = map(int, l[len("<!-- lignes "):-len(" de la source -->")].split(" à "))
            for k in range(a,b+1):
                i+=1
                e = ext[i]; s = src[k-1]; nkept+=1
                if e != s:
                    # check marks
                    parts = e.split("[passage non repris]")
                    pos=0; ok=True
                    for j,p in enumerate(parts):
                        idx = s.find(p,pos) if j>0 else (0 if s.startswith(p) else -1)
                        if idx<0: ok=False;break
                        pos=idx+len(p)
                    if not (ok and s.endswith(parts[-1])): nbad+=1; print("  ÉCART ligne", k)
                    else: print("  ligne",k,"avec marque(s):", len(parts)-1)
        i+=1
    print("  lignes gardées:", nkept, "écarts:", nbad)
