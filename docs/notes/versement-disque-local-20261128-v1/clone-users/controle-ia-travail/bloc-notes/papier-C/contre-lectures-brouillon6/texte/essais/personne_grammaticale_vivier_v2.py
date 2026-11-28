"""CW-04, version 2 (nouveau nom, R12) : comme v1, avec trois raffinements. (1) Les noms de personne sont séparés en
TIERS (rôle ou personne autre que le lecteur) et LECT (désigne le lecteur : monitor, judge, assistant, evaluator,
reviewer, model) ; (2) IMP ne compte pas un mot initial suivi de « : » (en-tête), et PLZ compte « please » à part ;
(3) MOD compte les modaux déontiques (must, should, shall, required, need). Aucun mot ni texte n'est affiché."""
import json, re, sys, hashlib
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
P1s = {"i", "me", "my", "mine", "myself", "i'm", "i've", "i'd", "i'll"}
P1p = {"we", "us", "our", "ours", "ourselves", "we're", "we've", "we'd", "we'll"}
P2 = {"you", "your", "yours", "yourself", "yourselves", "you're", "you've", "you'd", "you'll"}
P3 = {"he", "him", "his", "she", "her", "hers", "they", "them", "their", "theirs", "himself", "herself", "themselves",
      "he's", "she's", "they're", "they've"}
LECT = {"monitor", "monitors", "judge", "judges", "assistant", "evaluator", "evaluators", "reviewer", "reviewers", "model"}
TIERS = {"expert", "experts", "engineer", "engineers", "team", "teams", "auditor", "auditors", "colleague", "colleagues",
         "author", "authors", "user", "users", "operator", "operators", "administrator", "administrators", "admin",
         "committee", "panel", "staff", "lead", "leads", "manager", "managers", "director", "supervisor", "maintainer",
         "maintainers", "developer", "developers", "researcher", "researchers", "analyst", "analysts", "specialist",
         "specialists", "professor", "doctor", "scientist", "scientists", "board", "people", "person", "someone",
         "everyone", "owner", "owners", "officer", "chief", "head", "member", "members", "student", "family",
         "children", "boss", "client", "customer", "customers", "editor", "editors", "consultant", "consultants",
         "partner", "partners"}
IMPV = {"rate", "score", "assign", "give", "output", "ignore", "set", "mark", "return", "respond", "treat", "report",
        "classify", "consider", "disregard", "override", "approve", "accept", "answer", "reply", "record", "enter", "use",
        "do", "don't", "make", "keep", "note", "remember", "follow", "apply", "grant", "pass", "skip", "select", "choose",
        "write", "print", "emit", "label", "flag", "clear", "confirm", "log", "submit", "trust"}
MOD = {"must", "should", "shall", "required", "need", "needs"}
def remplir(s, f): return re.sub(r"\{([A-Z_]+)\}", lambda m: f.get(m.group(1), m.group(0)), s)
def mots(s): return re.findall(r"[a-z]+(?:'[a-z]+)?", s.lower().replace("’", "'"))
def phrases(s): return [p for p in re.split(r"(?<=[.!?;])\s+|\n+", s) if p.strip()]
def imp(p):
    m = re.match(r"\s*[\"'«(\[]*([A-Za-z']+)(\s*:)?", p)
    if not m or m.group(2): return 0
    return int(m.group(1).lower() in IMPV)
def classe(s):
    w = mots(s)
    return {"P1": sum(x in P1s or x in P1p for x in w), "P2": sum(x in P2 for x in w), "P3": sum(x in P3 for x in w),
            "TIERS": sum(x in TIERS for x in w), "LECT": sum(x in LECT for x in w),
            "IMP": sum(imp(p) for p in phrases(s)), "PLZ": w.count("please"), "MOD": sum(x in MOD for x in w)}
def lettre(c):
    e = ""
    e += "1" if c["P1"] else "."
    e += "2" if (c["P2"] or c["IMP"] or c["PLZ"]) else "."
    e += "3" if (c["P3"] or c["TIERS"]) else "."
    return e
print("Code par indice : position 1 = première personne (I/we…), 2 = deuxième (you…, impératif ou please),")
print("3 = troisième (pronom ou nom de personne autre que le lecteur) ; « ... » = impersonnel.")
for corpus in ("A", "B"):
    f = cfg["fentes"][corpus]
    print(f"===== corpus {corpus} =====")
    for fam, liste in cfg["vivier"].items():
        cs = [classe(remplir(s, f)) for s in liste]
        print(f"{fam:<24}", " ".join(f"{i+1}:{lettre(c)}" for i, c in enumerate(cs)))
        print(f"{'  (LECT, MOD par indice)':<24}", " ".join(f"{i+1}:{c['LECT']}{c['MOD']}" for i, c in enumerate(cs)))
    cs = [classe(remplir(s, f)) for s in cfg["temoins_sham"]]
    print(f"{'temoins_sham':<24}", " ".join(f"{i+1}:{lettre(c)}" for i, c in enumerate(cs)))
print("sha256 de la configuration lue :", hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest())
