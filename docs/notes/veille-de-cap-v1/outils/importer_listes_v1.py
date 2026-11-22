"""Import unique (récolte du 22 novembre, demande de la mère) : la liste exhaustive de la bibliothécaire
(§ 15, tableau récapitulatif ; § 16, « jamais éprouvé chez nous ») et le relevé des 93 idées des mentors
entrent au journal, une fiche par entrée, rattachée à son gisement. Extrait : la ligne du tableau, coupée
sous 300 signes, mot pour mot au commit cité. Aucun résultat recopié. Sortie : JSON Lines.
"""
import json, re, subprocess, sys
QUAND = sys.argv[1]; PREMIER = int(sys.argv[2])
def com(p): return subprocess.run(["git","log","-1","--format=%h","--",p],capture_output=True,text=True).stdout.strip()
def show(c,p): return subprocess.run(["git","show",f"{c}:{p}"],capture_output=True,check=True).stdout.decode()
def couper(t,n=300):
    t=t.strip()
    return t if len(t)<=n else t[:n].rsplit(" ",1)[0]
def mots(t):
    v=[]
    for m in re.split(r"[\s,;:.()«»'’/]+",t.lower()):
        if len(m)>5 and m not in v: v.append(m)
    return v[:5] or ["idée"]
out=[]; n=PREMIER
L="docs/notes/memoire-conception-v1/liste-exhaustive-hypotheses-exploration-allumage-v1.md"
cl=com(L); tl=show(cl,L).split("\n")
i15=next(i for i,l in enumerate(tl) if l.startswith("## 15."))
i16=next(i for i,l in enumerate(tl) if l.startswith("## 16."))
i17=next(i for i,l in enumerate(tl) if l.startswith("## 17."))
jamais=set(re.findall(r"\b([A-N]\d+)\b"," ".join(tl[i16:i17])))
for l in tl[i15:i16]:
    m=re.match(r"\| ([A-N]\d+) \| (.+?) \| ([A-N]) \| (.+?) \| (.+?) \|$",l)
    if not m: continue
    code,nom,fam,etat,ret=m.groups()
    note=f"bibliothécaire : état « {etat} », {ret}" + (" ; jamais éprouvé chez nous (§ 16)" if code in jamais else "")
    out.append({"quand":QUAND,"fiche":f"I-{n:04d}","evenement":"naissance","nom":f"{nom} (liste de la bibliothécaire, {code})","etat":"proposée",
      "source":{"chemin":L,"commit":cl,"repere":f"§ 15, {code}","extrait":couper(l)},"porteur":"synthèse ou décision",
      "sert":"organisme, exploration et allumage","issue":None,"raison":None,"reveil":None,"mots":mots(nom),"gisement":"G-0005",
      "note":note,"origine":"2026-11-22","derniere_trace":"2026-11-22"}); n+=1
M="docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md"
cm=com(M)
for l in show(cm,M).split("\n"):
    m=re.match(r"\| ((?:H|K|I|S|CW|JF)\d+) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$",l)
    if not m: continue
    code,idee,esp,prov,sert=m.groups()
    out.append({"quand":QUAND,"fiche":f"I-{n:04d}","evenement":"naissance","nom":f"Idée des mentors {code} : {couper(idee,140)}","etat":"proposée",
      "source":{"chemin":M,"commit":cm,"repere":f"§ 1, {code}","extrait":couper(l)},"porteur":"synthèse ou décision",
      "sert":f"idées des mentors ; {sert.strip()}","issue":None,"raison":None,"reveil":None,"mots":mots(idee),"gisement":"G-0002",
      "note":"matière première de l'atelier d'idées (N-072) ; affinage jamais joué (fiche I-0003)","origine":"2026-11-03","derniere_trace":"2026-11-18"}); n+=1
for e in out: print(json.dumps(e,ensure_ascii=False))
print(f"{len(out)} fiches, dernière I-{n-1:04d}",file=sys.stderr)
