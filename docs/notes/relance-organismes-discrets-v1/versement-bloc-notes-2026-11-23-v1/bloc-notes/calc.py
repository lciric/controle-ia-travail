import math
n=6400; tb,th=4.02,4.28
tJ=lambda t:t*(1+11/400)+0.45
print("juge s",tJ(tb),tJ(th),2*tJ(th), "surcout", tJ(th)/th-1, (4.85-4.28)/4.28)
A=(1+n*tb/3600,1+n*th/3600); B=(n*tJ(tb)/3600+0.1, n*tJ(th)/3600+1.0)
print("A h",A,"B h",B,"tot",A[0]+B[0],A[1]+B[1])
EA=(A[0]*1.1833+1,A[1]*1.30+2); EB=(B[0]*1.1833,B[1]*1.30)
print("EA",EA,"EB",EB,"tot",EA[0]+EB[0],EA[1]+EB[1])
PA=A[1]*4*1.38+4; PB=B[1]*4*1.38+4; PBs=B[1]*4*1.38
print("PA",PA,"PB",PB,"PB sans +4",PBs, "arr unite", math.ceil(PA),math.ceil(PB),math.ceil(PBs))
pA=lambda tA,m=1: 2*1.38*(max(1,m)+n*tA/3600)+4
pB=lambda tB,L=1,k=4: 2*1.38*(n*tB/3600+L)+k
print("mes", pA(th), pB(tJ(th)), pB(tJ(th),k=0))
for d in (40,42.8,45):
  a=pA(2*d/10); b=pB(2*tJ(d/10)); b0=pB(2*tJ(d/10),k=0)
  print(d, a, b, math.ceil(a)+math.ceil(b), "sans+4", b0, math.ceil(a)+math.ceil(b0))
# option c: wall
print("c wall", max(A[0],B[0]+1), max(A[1],B[1]+1))
print("1-99/115",1-99/115,"1-108/115",1-108/115)
# a juge lectures en h
print("lect juge h", n*tJ(tb)/3600, n*tJ(th)/3600, "lect bn", n*tb/3600,n*th/3600)
# v3 ordre de grandeur
print("ecart vs repli 59", 59/115)
# check tB fallback formula equals 2*tJ(d/10)
d=42.8; print(2*(1.0275*d/10+0.45), 2*tJ(d/10))
# 13% claim: section 0 point 5
print("juge vs bn per reading", tJ(tb)/tb-1, tJ(th)/th-1)
