import json, importlib.util
from pathlib import Path
DEPOT = Path("/home/user/controle-ia-travail")
spec = importlib.util.spec_from_file_location("ex4", DEPOT/"docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for nom in ["T06-organismes-v3","T08-base-A-mots-et-cout-v3","T08-bases-boite-noire-brouillon4-v3"]:
    fp = f"docs/notes/g1-extraits-tiers-v1/fiches/fiche-{nom}.json"
    fiche = json.loads((DEPOT/fp).read_text(encoding="utf-8"))
    assert set(fiche) <= m.CLES, set(fiche)
    disque = (DEPOT/fiche["sortie"]).read_bytes()
    t = m.fabriquer(fiche, fp)
    print(nom, "identique" if t.encode()==disque else "DIFFERENT")
    src = m.lignes_de((DEPOT/fiche["source"]).read_bytes())
    ext = disque.decode().split("\n")
    pl = sorted(tuple(p) for p in fiche["plages"])
    passl = {}
    for p in fiche["passages"]:
        assert set(p)=={"ligne","debut","fin"}
        passl.setdefault(p["ligne"],[]).append((p["debut"],p["fin"]))
    idx = {}
    for i,l in enumerate(ext):
        if l.startswith("<!-- lignes "):
            a,b = l[len("<!-- lignes "):].split(" de la source")[0].split(" à ")
            idx[(int(a),int(b))]=i
    bad=0
    for a,b in pl:
        i = idx[(a,b)]
        for k in range(a,b+1):
            e = ext[i+1+(k-a)]; s = src[k-1]
            r = s
            for d,f in sorted(passl.get(k,[]),reverse=True): r = r[:d]+m.MARQUE+r[f:]
            if r!=e: bad+=1; print("diff",k)
    print("  écarts:", bad)
    for k in sorted(passl):
        for d,f in sorted(passl[k]):
            l=src[k-1]
            print("  ", k, repr(l[max(0,d-50):d]), "<<", repr(l[d:f]), ">>", repr(l[f:f+50]))
