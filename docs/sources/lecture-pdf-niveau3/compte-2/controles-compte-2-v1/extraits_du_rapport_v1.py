"""Chaque extrait anglais cité entre guillemets dans un rapport figure-t-il dans le JSON des citations contrôlées ?
Usage : python3 -I extraits_du_rapport.py <rapport.md> <citations.json>"""
import json, re, sys, unicodedata
def n(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in {"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-"}.items():
        s = s.replace(a, b)
    s = s.replace("[…]", " ").replace("[...]", " ").replace("…", " ")
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip().lower()
r = open(sys.argv[1], encoding="utf-8").read()
cits = [n(c["citation"]) for c in json.load(open(sys.argv[2], encoding="utf-8"))]
seg = re.findall(r"«\s*([^«»]{12,}?)\s*»", r) + re.findall(r"“([^”]{12,}?)”", r)
anglais = [s for s in seg if len(re.findall(r"\b(the|of|and|is|we|to|a|in|that|with|as|on|for)\b", s.lower())) >= 2]
ko = 0
for s in anglais:
    parts = [p for p in re.split(r"\s*(?:\[…\]|\[\.\.\.\]|…)\s*", s) if len(p.strip()) >= 8]
    if not all(any(n(p) in c for c in cits) for p in parts):
        ko += 1; print("HORS JSON :", s[:110])
print(f"extraits anglais dans le rapport : {len(anglais)} ; hors du JSON contrôlé : {ko}")
sys.exit(1 if ko else 0)
