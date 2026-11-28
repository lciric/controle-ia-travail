import sys, re, os, unicodedata
V=os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('−','-'),('–','-'),('—','-'),('ﬁ','fi'),('ﬂ','fl')]:
        s=s.replace(a,b)
    s=re.sub(r'-\s*\n\s*','',s)  # hyphenation
    s=re.sub(r'\s+',' ',s)
    return s.lower()
key=sys.argv[1]; phrase=norm(sys.argv[2])
d=os.path.join(V,'pages',key)
hits=[]
for f in sorted(os.listdir(d)):
    if not f.startswith('r'): continue
    t=norm(open(os.path.join(d,f),errors='ignore').read())
    if phrase in t: hits.append(int(f[1:4]))
# also layout
hl=[]
for f in sorted(os.listdir(d)):
    if not f.startswith('p'): continue
    t=norm(open(os.path.join(d,f),errors='ignore').read())
    if phrase in t: hl.append(int(f[1:4]))
print(key, repr(sys.argv[2][:70]), 'raw:',hits,'layout:',hl)
