import re, sys, difflib
def sents(path):
    txt = open(path, encoding='utf-8').read()
    out = []
    for ln_no, line in enumerate(txt.split('\n'), 1):
        # split on '. ', ' ; ', ' : ' boundaries keep reasonably small
        parts = re.split(r'(?<=[\.;])\s+(?=[^\s])', line)
        for p in parts:
            p = p.strip()
            if p:
                out.append((ln_no, p))
    return out
a = sents(sys.argv[1]); b = sents(sys.argv[2])
sa = [x[1] for x in a]; sb = [x[1] for x in b]
sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
n=0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal': continue
    n+=1
    print(f"=== [{n}] {tag} v1 l.{a[i1][0] if i1<len(a) else '-'}..{a[i2-1][0] if i2>i1 else '-'}  v2 l.{b[j1][0] if j1<len(b) else '-'}..{b[j2-1][0] if j2>j1 else '-'}")
    for k in range(i1,i2): print("  - ", a[k][1])
    for k in range(j1,j2): print("  + ", b[k][1])
print("TOTAL hunks", n)
