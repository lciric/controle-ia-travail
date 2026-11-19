import re,sys,json
t=open(sys.argv[1],encoding='utf-8').read()
lines=t.split('\n')
# positions
def lineno(pos): return t.count('\n',0,pos)+1
H=re.compile(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])')
P=re.compile(r'`([^`\n]+)`')
ticks=[(m.start(),m.group(1)) for m in P.finditer(t.replace('\n',' '))]  # same offsets
out=[]
for m in H.finditer(t):
    prev=[x for x in ticks if x[0]<m.start() and not H.fullmatch(x[1])]
    p=prev[-1] if prev else (0,'')
    out.append((lineno(m.start()),m.group(0),p[1],m.start()-p[0]))
for o in out: print("H\t%d\t%s\t%s\t%d"%o)
seen=set()
for pos,s in ticks:
    if H.fullmatch(s): continue
    if ('/' in s or re.search(r'\.(md|py|json|txt|pdf|sha256|csv|jsonl|gz|zip|npz|yaml|toml)\b',s)) and s not in seen:
        seen.add(s); print("P\t%d\t%s"%(lineno(pos),s))
