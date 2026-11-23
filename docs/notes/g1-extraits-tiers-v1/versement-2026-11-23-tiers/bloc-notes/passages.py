import json, subprocess, sys
D="/home/user/controle-ia-travail"
nom=sys.argv[1]
f=json.load(open(D+"/docs/notes/g1-extraits-tiers-v1/fiches/"+nom))
if f.get("ref"):
    b=subprocess.run(["git","show",f"{f['ref']}:{f['source']}"],capture_output=True,cwd=D,check=True).stdout
else:
    b=open(D+"/"+f["source"],"rb").read()
L=b.decode().split("\n")
if L[-1]=="": L=L[:-1]
for p in f["passages"]:
    l=L[p["ligne"]-1]
    print(f"--- ligne {p['ligne']} [{p['debut']}:{p['fin']}]")
    print("AVANT: ..."+l[max(0,p['debut']-80):p['debut']])
    print("OMIS : "+l[p['debut']:p['fin']])
    print("APRES: "+l[p['fin']:p['fin']+80]+"...")
