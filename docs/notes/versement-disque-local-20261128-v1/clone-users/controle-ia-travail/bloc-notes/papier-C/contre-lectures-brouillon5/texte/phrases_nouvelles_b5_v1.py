"""Phrases du brouillon 5 absentes du brouillon 4 (découpage grossier sur « . », « ; » et fins de ligne de tableau), avec
leur ligne dans le brouillon 5. Sert à repérer les changements non rattachés à un constat."""
import re, sys, pathlib
def morceaux(t):
    t = re.sub(r"[ \t]*\n[ \t]*(?![-|#\d*])", " ", t)
    out = []
    for l in t.splitlines():
        for m in re.split(r"(?<=[.;])\s+|\s\|\s", l):
            m = re.sub(r"\s+", " ", m).strip(" |")
            if len(m) > 25: out.append(m)
    return out
b4 = set(morceaux(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")))
t5 = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
l5 = re.sub(r"\s+", " ", t5)
for m in morceaux(t5):
    if m not in b4:
        cle = m[:40]
        # ligne approximative
        i = next((k for k, l in enumerate(t5.splitlines(), 1) if cle[:25] in l), 0)
        print(f"l.{i:4d} | {m[:200]}")
