"""Aide de lecture du trieur : pour chaque identifiant, titre, score, mots, images, en-tête,
intertitres et quelques passages chiffrés. Usage : lire_v2.py [--long N] id1 id2 ..."""
import sys, re
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import billets, texte, IMAGE
args = sys.argv[1:]; tete = 900
if args and args[0] == "--long": tete = int(args[1]); args = args[2:]
for i in args:
    p = billets[i]; t = texte(i)
    heads = [l.strip("# ").strip()[:70] for l in t.split("\n") if re.match(r"#{1,4} ", l)]
    nb = [m.group(0) for m in re.finditer(r"[^.\n]{0,70}\b\d{1,3}(?:\.\d+)?\s?%[^.\n]{0,40}", t)][:3]
    corps = re.sub(r"!\[[^\]]*\]\([^)]*\)", "[IMG]", t)
    corps = re.sub(r"\s+", " ", corps)
    print(f"=== {i} | {p['title'][:100]} | s={p['baseScore']} | {p['mots']}m | img={len(re.findall(IMAGE, t))} | {p['postedAt'][:10]}")
    print("TETE:", corps[:tete])
    print("H:", " / ".join(heads[:14]))
    if nb: print("NB:", " || ".join(x.strip() for x in nb))
