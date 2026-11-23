"""Inventaire et statut des papiers (PDF) du dépôt, par programme — veille de cap, v1 (23 novembre 2026).
Pièce de travail outillée (classe B, non contre-lue). Ne lit AUCUN PDF (niveau « noms seuls » de la boucle, listes_lecture_v3) :
titre tiré des textes ouvrables qui citent le nom ou l'identifiant. Lit les textes de niveau « plein » au bras boucle, au
commit donné (git show), et journalise chaque fichier ouvert (format de recherche_bornee : agent, action, chemin, commit, bras).
Statuts (heuristiques déclarées) :
  verse      : aucun texte hors de son dossier de versement ne cite la clé ;
  cite       : cité hors du dossier de versement, sans décision ;
  decide     : cité dans docs/decisions/ ou dans une ligne R-/GO- de registres/decisions.md ou go.md, rien de lancé ;
  lance      : cité dans une note de lecture ou de vérification sur PDF (chemin avec « lecture », « verification-pdf »,
               « controle-tracabilite ») ou dans papiers/ ;
  r7         : drapeau en plus, seulement dans docs/decisions/, papiers/ et les textes de préenregistrement ou de devis : une ligne qui cite la clé porte un nombre décimal ou un pourcentage sans « p. »/« page ».
Usage : python3 -I papiers_du_depot_v1.py COMMIT AGENT JOURNAL SORTIE.jsonl
"""
import collections, hashlib, importlib.util, json, os, re, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
s = importlib.util.spec_from_file_location("ll", os.path.join(RACINE, "docs/notes/memoire-conception-v1/fusion-outils-v1/listes_lecture_v3.py"))
ll = importlib.util.module_from_spec(s); s.loader.exec_module(ll)
COMMIT, AGENT, JOURNAL, SORTIE = sys.argv[1:5]
def git(*a): return subprocess.run(["git", "-C", RACINE, *a], capture_output=True).stdout
tous = git("ls-tree", "-r", "-z", "--name-only", COMMIT).decode("utf-8", "replace").split("\0")
pdfs = [c for c in tous if c.lower().endswith(".pdf") and not c.startswith("docs/notes/rapports-directeur/")
        and ll.niveau_boucle(c)[0] != "refus"]
textes = [c for c in tous if ll.niveau_boucle(c)[0] == "plein" and not c.endswith(".sha256")
          and c.lower().endswith((".md", ".txt", ".jsonl", ".json", ".tsv", ".csv", ".py", ".bib"))]
# dates de versement : premier ajout
dates = {}
cour = None
for l in git("log", "--diff-filter=A", "--format=@%cs", "--name-only", "--reverse", COMMIT, "--", "*.pdf", "*.PDF").decode("utf-8", "replace").split("\n"):
    if l.startswith("@"): cour = l[1:]
    elif l.strip() and l not in dates: dates[l] = cour
def cle(c):
    b = os.path.basename(c)[:-4]
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", b)
    if m: return m.group(1)
    m = re.search(r"ssrn[-_ ]?(\d{6,8})", b, re.I)
    if m: return m.group(1)
    return b if len(b) >= 8 else None
journal = open(JOURNAL, "a", encoding="utf-8")
corpus = {}
for c in textes:
    b = git("show", f"{COMMIT}:{c}")
    if len(b) > 3_000_000: continue
    corpus[c] = b.decode("utf-8", "replace")
    journal.write(json.dumps({"agent": AGENT, "action": "lire", "chemin": c, "commit": COMMIT, "bras": "boucle"}, ensure_ascii=False) + "\n")
journal.close()
par_cle = collections.defaultdict(list)
for c in pdfs:
    par_cle[cle(c) or c].append(c)
# index : pour chaque clé, fichiers et lignes qui la citent
cles = list(par_cle)
RXARX = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])")
RXJET = re.compile(r"[^/\s`'\"()\[\]<>,;|]+")
cles_set = set(cles)
def cles_de_ligne(ligne):
    trouves = set(m for m in RXARX.findall(ligne) if m in cles_set)
    for j in RXJET.findall(ligne):
        j = re.sub(r"\.(pdf|PDF|sha256)$", "", j.rstrip(".:"))
        if j in cles_set: trouves.add(j)
    return trouves
hits = collections.defaultdict(list)
for c, t in corpus.items():
    for i, ligne in enumerate(t.split("\n"), 1):
        for m in cles_de_ligne(ligne):
            hits[m].append((c, i, ligne[:400]))
RXR7 = re.compile(r"\d+[.,]\d+|\d+ ?%"); RXPAGE = re.compile(r"\bp\. ?\d|\bpage", re.I)
RXLANCE = re.compile(r"(^|/|-)(lecture|lectures|verification-pdf|controle-tracabilite)(-|/|\.|$)|^papiers/")
RXPASLANCE = re.compile(r"contre-lecture|criteres-lecture|texte-de-lecture|textes-de-lecture|/sorties/|regles-communes|demande")
RXR7ZONE = re.compile(r"^docs/decisions/|^papiers/|preenregistrement|prereg|devis")
RXDEC = re.compile(r"\b(R-\d+|GO-\d{4}-\d\d-\d\d-\d+|N-0\d\d)\b")
sortie = []
for k, chemins in par_cle.items():
    dossiers = {os.path.dirname(c) for c in chemins}
    h = [x for x in hits.get(k, []) if os.path.dirname(x[0]) not in dossiers]
    titre = None
    for c, i, l in hits.get(k, []):
        if c.startswith("docs/sources/") and len(l.strip()) > len(k) + 10:
            titre = re.sub(r"\s+", " ", l.strip())[:160]; break
    lance = [x for x in h if RXLANCE.search(x[0]) and not RXPASLANCE.search(x[0])]
    decide = [x for x in h if x[0].startswith("docs/decisions/") or
              (x[0] in ("registres/decisions.md", "registres/go.md") and RXDEC.search(x[2]))]
    statut = "lance" if lance else "decide" if decide else "cite" if h else "verse"
    r7 = [x for x in h if RXR7ZONE.search(x[0]) and RXR7.search(x[2].replace(k, "")) and not RXPAGE.search(x[2])]
    emp = hashlib.sha256(git("show", f"{COMMIT}:{chemins[0]}")).hexdigest()
    sortie.append({"cle": k, "chemins": sorted(chemins), "empreinte": emp, "verse_le": min(dates.get(c) or "?" for c in chemins),
                   "titre": titre, "statut": statut, "r7": bool(r7), "n_citations": len(h),
                   "decisions": sorted({m for x in decide for m in RXDEC.findall(x[2])})[:6],
                   "premier_decide": decide[0][:2] if decide else None, "premier_lance": lance[0][:2] if lance else None,
                   "citants": sorted({x[0] for x in h})[:8]})
with open(SORTIE, "x", encoding="utf-8") as f:
    for e in sorted(sortie, key=lambda e: e["cle"]): f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(json.dumps({"pdf": len(pdfs), "cles": len(par_cle), "textes_lus": len(corpus),
                  "statuts": collections.Counter(e["statut"] for e in sortie), "r7": sum(e["r7"] for e in sortie)}, ensure_ascii=False))
