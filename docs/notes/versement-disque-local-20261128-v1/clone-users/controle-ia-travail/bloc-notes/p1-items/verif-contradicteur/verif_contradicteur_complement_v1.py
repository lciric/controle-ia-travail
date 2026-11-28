# -*- coding: utf-8 -*-
"""
COMPLEMENT CONTRADICTEUR v1 - deux points que la passe principale laissait trop larges.
Lecture seule, aucun reseau. Lancer avec : python3 -I verif_contradicteur_complement_v1.py

E'. VARIANTES DE CORPUS, CRITERE STRICT : une VALEUR ENTIERE (chaine JSON, cellule TSV/CSV,
    ligne de texte, litteral Python) dont la forme aplatie est egale a celle d'un des 30
    textes, mais dont les caracteres different. Une reponse de modele qui CITE le texte
    sans son point final n'est pas une variante du corpus et n'est pas comptee.
    Temoin positif : les 30 textes exacts doivent etre retrouves comme valeurs entieres.
    Temoin d'artefact : une variante fabriquee en memoire (point final retire) doit etre vue.
C'. Les items ou l'argmax sur les 200 textes de n200 ne tombe pas sur l'item : lesquels,
    quel concurrent, quelle marge.
"""
import ast, collections, csv, hashlib, io, json, os, re, unicodedata

ICI = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p1-items/verif-contradicteur"
EXT = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p1-items/extraction"
N200 = ("/home/user/archive-2026-09/depots/sycophancy-construct-validity/results/n200_complete_results.json",
        "64894c215d68a4566bb0f232cf9c565285a23b3186607bdf0a436384b7a759e9")
C2A = ("/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1/c2a_generations.json",
       "a7c85816e2ce60fd86727fe367cb1d63335940a13b50ba3e33c9e16b3ba6189a")
C2B = ("/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1/c2b_generations.json",
       "ec2f7ca5cc80c249fd861a77fb360a8e1c4d59f1788ada2a7864b88ec72586c2")
RACINES = ["/home/user/archive-2026-09", "/home/user/p1-auto", "/home/user/sycophancy-construct-validity",
           "/home/user/lciric", "/home/user/cplt_run_2026-09-03", "/home/user/controle-ia-travail"]
INTERDIT = "/home/user/controle-ia-travail/prereg/P3-consignes-v1.md"
SORTIE = []


def dire(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    SORTIE.append(s)


def sha_f(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def aplatir(s):
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKC", s).lower())


def chaines_json(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from chaines_json(v)
    elif isinstance(o, list):
        for v in o:
            yield from chaines_json(v)


def valeurs(p, s):
    """Toutes les valeurs entieres d'un fichier, selon son type."""
    f = p.lower()
    out = []
    if f.endswith((".json", ".ipynb")):
        try:
            out.extend(chaines_json(json.loads(s)))
        except Exception:
            pass
    if f.endswith(".jsonl"):
        for ln in s.splitlines():
            try:
                out.extend(chaines_json(json.loads(ln)))
            except Exception:
                pass
    if f.endswith((".tsv", ".csv")):
        try:
            for row in csv.reader(io.StringIO(s), delimiter="\t" if f.endswith(".tsv") else ","):
                out.extend(row)
        except Exception:
            pass
    if f.endswith(".py"):
        try:
            for n in ast.walk(ast.parse(s)):
                if isinstance(n, ast.Constant) and isinstance(n.value, str):
                    out.append(n.value)
        except Exception:
            pass
    # lignes nues, et lignes debarrassees de puces / guillemets / numeros
    for ln in s.splitlines():
        out.append(ln)
        out.append(re.sub(r"^\s*(?:[-*>|]|\d+[.)])?\s*[\"'`“]?|[\"'`”]?\s*[|,]?\s*$", "", ln))
    return out


def main():
    for p, att in (N200, C2A, C2B):
        h = sha_f(p)
        dire("  %s  %s  %s" % (h, "CONFORME" if h == att else "*** DIVERGE ***", p))
        if h != att:
            raise SystemExit("ARRET NOMME - empreinte divergente")
    n200 = json.load(open(N200[0], encoding="utf-8"))["texts"]
    textes = n200[:30]
    plats = {aplatir(t): i for i, t in enumerate(textes)}

    # temoins
    faux = textes[3][:-1]
    dire("\nTEMOINS")
    v_sain = [x for x in valeurs("x.json", json.dumps({"a": textes[3]})) if x == textes[3]]
    v_art = [x for x in valeurs("x.json", json.dumps({"a": faux}))
             if aplatir(x) in plats and x != textes[plats[aplatir(x)]]]
    dire("  [%s] sain : un texte exact en valeur JSON est lu comme valeur entiere" % ("OK   " if v_sain else "ECHEC"))
    dire("  [%s] artefact : une variante fabriquee (point final retire) est detectee" % ("OK   " if v_art else "ECHEC"))
    if not (v_sain and v_art):
        raise SystemExit("ARRET NOMME - temoin rouge")

    dire("\nE'. VARIANTES DE CORPUS, CRITERE STRICT (valeur entiere)")
    n = 0
    exacts = collections.defaultdict(set)
    variantes = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in RACINES:
        for d, ds, fs in os.walk(r):
            ds[:] = [x for x in ds if x not in (".git", ".venv", "__pycache__")]
            for f in fs:
                p = os.path.join(d, f)
                if p == INTERDIT or "textes-actions-" in f or p.startswith(ICI) or p.startswith(EXT):
                    continue
                if not f.lower().endswith((".json", ".jsonl", ".ipynb", ".tsv", ".csv", ".py", ".md",
                                           ".txt", ".log")):
                    continue
                try:
                    if os.path.getsize(p) > 60 * 1024 * 1024:
                        continue
                    s = open(p, "rb").read().decode("utf-8", errors="replace")
                except OSError:
                    continue
                n += 1
                for v in valeurs(p, s):
                    if len(v) > 300 or len(v) < 20:
                        continue
                    a = aplatir(v)
                    if a in plats:
                        i = plats[a]
                        if v == textes[i]:
                            exacts[i].add(p)
                        else:
                            variantes[i][v].add(p)
    dire("  fichiers lus : %d" % n)
    dire("  temoin positif : items retrouves EXACTS comme valeur entiere : %d/30" % len(exacts))
    dire("  items ayant au moins une VARIANTE de valeur entiere : %d" % len(variantes))
    for i in sorted(variantes):
        for v, ps in sorted(variantes[i].items(), key=lambda x: -len(x[1])):
            ps = sorted(ps)
            dire("    item %2d  variante %r" % (i, v))
            dire("             texte n200 %r" % textes[i])
            dire("             %d fichier(s), ex. %s" % (len(ps), ps[:4]))

    # C'
    dire("\nC'. ITEMS OU L'ARGMAX SUR LES 200 TEXTES NE TOMBE PAS SUR L'ITEM")
    VIDES = set("""a an the of to in on for and or but is are was were be been it its this that these those
with as at by from not no you your i we they he she which what who how why when where all any some
more most less than then so such if do does did can could would should may might must have has had
""".split())
    mots = lambda t: {w for w in re.findall(r"[a-z]{4,}", t.lower()) if w not in VIDES}
    for path, nom in ((C2A[0], "c2a"), (C2B[0], "c2b")):
        d = json.load(open(path, encoding="utf-8"))
        for cond in sorted({r["cond"] for r in d["rows"]}):
            rep = collections.defaultdict(set)
            for r in d["rows"]:
                if r["cond"] == cond:
                    rep[int(r["item"])] |= mots(r["resp"])
            for i in range(30):
                sc = [(len(mots(t) & rep[i]) / max(1, len(mots(t))), a) for a, t in enumerate(n200)]
                best = max(sc)
                propre = sc[i][0]
                if best[1] != i and not (i == 27 and best[1] == 59):
                    if best[0] >= propre:
                        dire("  %s %-8s item %2d : propre %.3f ; concurrent n200[%d] %.3f %r" % (
                            nom, cond, i, propre, best[1], best[0], n200[best[1]]))
                        dire("                 texte de l'item : %r" % n200[i])
    dire("\nFIN")


if __name__ == "__main__":
    try:
        main()
    finally:
        j = os.path.join(ICI, "journal-verif-contradicteur-complement-v1.txt")
        open(j, "w", encoding="utf-8", newline="\n").write("\n".join(SORTIE) + "\n")
        h = sha_f(j)
        open(j + ".sha256", "w", encoding="utf-8", newline="\n").write("%s  %s\n" % (h, os.path.basename(j)))
        print("journal", j, h)
