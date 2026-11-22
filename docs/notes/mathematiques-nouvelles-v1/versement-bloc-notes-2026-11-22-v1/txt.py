import re,sys,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 800
idx=[m.start() for m in re.finditer(pat,t,flags=re.I)]
print(sys.argv[1],len(idx),'hits')
last=-10**9
for i in idx:
    if i-last< w: continue
    last=i; print('---',t[max(0,i-150):i+w])
