import re,subprocess,hashlib,sys
t=open(sys.argv[1]).read()
refs=["origin/main","origin/lot/compte-organisme-v1","origin/prep/affinage-v7-compte-organisme-v1","origin/prep/affinage-v8-compte-organisme-v1","origin/prep/affinage-v9-compte-organisme-v1","origin/prep/affinage-v10-compte-organisme-v1","origin/prep/lanceur-affinage-v11c-interrompu-v1","origin/prep/preenregistrement-affinage-v11-opus-v1"]
files={}
for r in refs:
    out=subprocess.run(["git","ls-tree","-r",r],capture_output=True,text=True).stdout
    for l in out.splitlines():
        meta,p=l.split("\t",1); blob=meta.split()[2]
        files.setdefault(p.rsplit('/',1)[-1],[]).append((r,p,blob))
cache={}
def sha(blob):
    if blob not in cache:
        cache[blob]=hashlib.sha256(subprocess.run(["git","cat-file","blob",blob],capture_output=True).stdout).hexdigest()
    return cache[blob]
# pairs: backticked path then within 400 chars a full 64-hex hash
toks=[(m.start(),'P',m.group(1)) for m in re.finditer(r'`([^`\s]+\.(?:py|md|json|txt|sh|html|md\.txt))`',t)]
toks+=[(m.start(),'H',m.group(0)) for m in re.finditer(r'\b[0-9a-f]{64}\b',t)]
toks.sort()
last=None; seen=set()
allh=set(h for _,k,h in toks if k=='H')
for pos,k,v in toks:
    if k=='P': last=(pos,v)
    else:
        if last is None: print('NOPATH',v);continue
        name=last[1].rsplit('/',1)[-1]
        cands=files.get(name,[])
        ok=[c for c in cands if sha(c[2])==v]
        key=(last[1],v)
        if key in seen: continue
        seen.add(key)
        if ok: print('OK  ',last[1][-60:],v[:8],ok[0][0].replace('origin/',''))
        else:
            # search any file with that hash
            print('??  ',last[1][-60:],v[:8],'cands',len(cands), [ (c[0].replace('origin/',''),sha(c[2])[:8]) for c in cands][:6])
