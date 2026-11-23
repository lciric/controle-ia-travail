"""Mesure grossière du recouvrement entre réponses (termes longs, trigrammes, références auteur-année)."""
import re, sys, itertools, unicodedata, pathlib
D = pathlib.Path(sys.argv[1])
JEUX = {"q1": {"argon": "reponse-argon-v1.md", "carbon": "reponse-carbon-v1.md", "neon": "reponse-neon-v1.md"},
        "q2": {"argon": "reponse-argon-homomorphisme-v1-relance1.md", "carbon": "reponse-carbon-homomorphisme-v1.md",
               "neon": "reponse-neon-homomorphisme-v1.md"}}
def norm(t):
    t = unicodedata.normalize("NFKD", t.lower()); return "".join(c for c in t if not unicodedata.combining(c))
def termes(t): return {w[:7] for w in re.findall(r"[a-z]{7,}", norm(t))}
def tri(t):
    w = [x[:6] for x in re.findall(r"[a-z]{4,}", norm(t))]; return {tuple(w[i:i+3]) for i in range(len(w)-2)}
def refs(t):
    s = set()
    for m in re.finditer(r"([A-Z][A-Za-zÀ-ÿ'\-]+)(?:\s+(?:et|and|&)\s+[A-Z][A-Za-zÀ-ÿ'\-]+|\s+et al\.?)?,?\s*\(?((?:1[6-9]|20)\d\d)", t):
        s.add((norm(m.group(1)), m.group(2)))
    return s
J = lambda a, b: len(a & b) / max(1, len(a | b))
for q, f in JEUX.items():
    T = {k: (D / v).read_text() for k, v in f.items()}
    print(f"== {q} mots:", {k: len(v.split()) for k, v in T.items()})
    for nom, fn in (("termes", termes), ("trigrammes", tri), ("references", refs)):
        S = {k: fn(v) for k, v in T.items()}
        paires = {f"{a}-{b}": round(J(S[a], S[b]), 3) for a, b in itertools.combinations(S, 2)}
        u = set().union(*S.values())
        propre = {k: len(S[k] - set().union(*(S[j] for j in S if j != k))) for k in S}
        perdu_sans = {k: round(len(u - set().union(*(S[j] for j in S if j != k))) / max(1, len(u)), 3) for k in S}
        seul_c = round(1 - len(S["carbon"]) / max(1, len(u)), 3)
        print(f"  {nom}: Jaccard {paires} | propres {propre} | union {len(u)} | part perdue sans {perdu_sans} | perdue avec Carbon seul {seul_c}")
    R = {k: refs(v) for k, v in T.items()}
    for k in R: print("   refs", k, sorted(R[k] - R["carbon"])[:40] if k != "carbon" else len(R[k]))
