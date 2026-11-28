"""CW-04 : personne grammaticale des formulations du vivier, par famille et par indice (1 à 16).
Lit $.vivier.* et $.fentes ; n'affiche jamais un mot ni un texte de formulation : seulement des comptes
par classe de mots, calculés sur la formulation remplie pour chaque corpus (A et B).
Classes : P1s (I, me, my, mine, myself et contractions), P1p (we, us, our, ours, ourselves et contractions),
P2 (you, your, yours, yourself, yourselves et contractions), P3 (he, him, his, she, her, hers, they, them, their,
theirs, himself, herself, themselves), HUM (noms de personne ou de rôle, liste fixe ci-dessous), IMP (phrase qui
commence par un verbe à l'impératif de la liste fixe, ou par please), et taille (mots)."""
import json, re, sys, hashlib
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
P1s = {"i", "me", "my", "mine", "myself", "i'm", "i've", "i'd", "i'll", "im"}
P1p = {"we", "us", "our", "ours", "ourselves", "we're", "we've", "we'd", "we'll"}
P2 = {"you", "your", "yours", "yourself", "yourselves", "you're", "you've", "you'd", "you'll"}
P3 = {"he", "him", "his", "she", "her", "hers", "they", "them", "their", "theirs", "himself", "herself", "themselves",
      "he's", "she's", "they're", "they've"}
HUM = {"reviewer", "reviewers", "expert", "experts", "engineer", "engineers", "team", "teams", "auditor", "auditors",
       "colleague", "colleagues", "author", "authors", "user", "users", "operator", "operators", "administrator",
       "administrators", "admin", "committee", "panel", "staff", "lead", "leads", "manager", "managers", "director",
       "supervisor", "maintainer", "maintainers", "developer", "developers", "researcher", "researchers", "analyst",
       "analysts", "specialist", "specialists", "professor", "doctor", "scientist", "scientists", "board", "people",
       "person", "someone", "everyone", "evaluator", "evaluators", "judge", "judges", "monitor", "assistant",
       "owner", "owners", "officer", "chief", "head", "member", "members", "student", "family", "children", "boss",
       "client", "customer", "customers", "editor", "editors", "consultant", "consultants", "partner", "partners"}
IMPV = {"please", "rate", "score", "assign", "give", "output", "ignore", "set", "mark", "return", "respond", "treat",
        "report", "classify", "consider", "disregard", "override", "approve", "accept", "answer", "reply", "record",
        "enter", "use", "do", "don't", "make", "keep", "note", "remember", "follow", "apply", "grant", "pass", "skip",
        "select", "choose", "write", "print", "emit", "label", "flag", "clear", "confirm", "log", "submit", "trust"}
def remplir(s, f):
    return re.sub(r"\{([A-Z_]+)\}", lambda m: f.get(m.group(1), m.group(0)), s)
def mots(s):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", s.lower().replace("’", "'"))
def phrases(s):
    return [p for p in re.split(r"(?<=[.!?:;])\s+|\n+", s) if p.strip()]
def classe(s):
    w = mots(s)
    c = {"P1s": sum(x in P1s for x in w), "P1p": sum(x in P1p for x in w), "P2": sum(x in P2 for x in w),
         "P3": sum(x in P3 for x in w), "HUM": sum(x in HUM for x in w),
         "IMP": sum(1 for p in phrases(s) if (mots(p)[:1] or [""])[0] in IMPV), "mots": len(w)}
    return c
def etiquette(c):
    e = []
    if c["P1s"] or c["P1p"]: e.append("1re")
    if c["P2"]: e.append("2e")
    if c["IMP"]: e.append("2e-imp")
    if c["P3"] or c["HUM"]: e.append("3e")
    return "+".join(e) if e else "impers."
for corpus in ("A", "B"):
    f = cfg["fentes"][corpus]
    print(f"===== corpus {corpus} (formulations remplies) =====")
    for fam, liste in cfg["vivier"].items():
        print(f"--- {fam} ---")
        print("ind  P1s P1p  P2  P3 HUM IMP mots  étiquette")
        for i, s in enumerate(liste, start=1):
            c = classe(remplir(s, f))
            print(f"{i:>3} {c['P1s']:>4} {c['P1p']:>3} {c['P2']:>3} {c['P3']:>3} {c['HUM']:>3} {c['IMP']:>3} {c['mots']:>4}  {etiquette(c)}")
print("===== témoins (corpus A) =====")
for i, s in enumerate(cfg["temoins_sham"], start=1):
    c = classe(remplir(s, cfg["fentes"]["A"]))
    print(f"{i:>3} {c['P1s']:>4} {c['P1p']:>3} {c['P2']:>3} {c['P3']:>3} {c['HUM']:>3} {c['IMP']:>3} {c['mots']:>4}  {etiquette(c)}")
print("sha256 de la configuration lue :", hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest())
