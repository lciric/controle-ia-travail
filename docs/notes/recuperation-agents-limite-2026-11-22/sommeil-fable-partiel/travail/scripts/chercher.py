# usage: python3 -I chercher.py TXT MOTIF [MOTIF…]  -> lignes avec la page (texte aplati par page)
import sys, re
txt = open(sys.argv[1], encoding='utf-8').read()
pages = re.split(r'\n=== PAGE (\d+) / \d+ ===\n', txt)
# pages[0] vide, puis (num, texte)…
for i in range(1, len(pages), 2):
    num, t = pages[i], pages[i+1]
    flat = re.sub(r'\s+', ' ', t.replace('-\n', ''))
    for pat in sys.argv[2:]:
        for m in re.finditer(pat, flat, flags=re.I):
            a, b = max(0, m.start()-150), min(len(flat), m.end()+250)
            print(f'[p.{num}] …{flat[a:b]}…')
