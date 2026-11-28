import sys, re, os, unicodedata
V='/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/verification'
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('−','-'),('–','-'),('—','-'),('ﬁ','fi'),('ﬂ','fl')]:
        s=s.replace(a,b)
    s=re.sub(r'-\s*\n\s*','',s)
    s=re.sub(r'\s+',' ',s)
    return s
key=sys.argv[1]; phrase=norm(sys.argv[2]).lower(); w=int(sys.argv[3]) if len(sys.argv)>3 else 300
d=os.path.join(V,'pages',key)
for f in sorted(os.listdir(d)):
    if not f.startswith('r'): continue
    t=norm(open(os.path.join(d,f),errors='ignore').read())
    tl=t.lower(); i=tl.find(phrase)
    while i>=0:
        print(f'== {key} page {int(f[1:4])}: ...{t[max(0,i-w):i+len(phrase)+w]}...\n')
        i=tl.find(phrase,i+1)
