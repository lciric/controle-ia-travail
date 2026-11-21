"""Effet, sur la médiane des écarts honnêtes bornables, des actions dont la valeur du champ COST est à la ligne suivante."""
import json, sys, statistics
A=[o for o in json.load(open(sys.argv[1]))["actions"] if o["phase"]=="etalonnage-honnete" and o["bornable"]]
ep="2510.26243v1/e1"
es=sorted(o["e"] for o in A); print("n",len(es),"mediane",statistics.median(es))
rang=sorted(range(len(A)),key=lambda i:-A[i]["e"])
print("rangs (du plus grand) des 10 actions de l'episode:",sorted(rang.index(i) for i in range(len(A)) if A[i]["episode"]==ep))
sans=[o["e"] for o in A if o["episode"]!=ep]; print("sans l'episode: n",len(sans),"mediane",statistics.median(sans))
p0=[o["e"] for o in A if o["pas"]==0]; p0s=[o["e"] for o in A if o["pas"]==0 and o["episode"]!=ep]
print("pas 0: mediane",statistics.median(p0),"n",len(p0),"; sans l'episode",statistics.median(p0s),len(p0s))
print("pas 0 sup a toutes les suites:",sum(o["cout_declare"]>max(s for s in o["suites"] if s) for o in A if o["pas"]==0),
      "; sans l'episode:",sum(o["cout_declare"]>max(s for s in o["suites"] if s) for o in A if o["pas"]==0 and o["episode"]!=ep))
bas=sans+[-9.0]*10; print("borne basse (les 10 remplacees par des ecarts negatifs):",statistics.median(bas))
nul=sans+[0.0]*10; print("les 10 remplacees par 0:",statistics.median(nul))
