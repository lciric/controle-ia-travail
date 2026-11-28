import sys, re
def norm(s):
    s = s.replace('’', "'").replace('–', '-').replace('—', '-')
    s = re.sub(r'-\s*\n\s*', '', s)  # césure
    return re.sub(r'\s+', ' ', s).lower()
txt = open(sys.argv[1], encoding='utf-8', errors='replace').read()
pages = txt.split('\f')
for ph in sys.argv[2:]:
    n = norm(ph); hits = [i + 1 for i, p in enumerate(pages) if n in norm(p)]
    print(f"{'OK' if hits else 'ABSENT'}\tpages={hits}\t{ph}")
