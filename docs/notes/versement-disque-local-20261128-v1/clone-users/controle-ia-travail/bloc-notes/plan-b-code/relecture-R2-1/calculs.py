import math
def q(p, n=16, s=0.005):
    pmf=[math.comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]
    return [t for t in range(n+1) if sum(pmf[:t+1])<s], [t for t in range(n+1) if sum(pmf[t:])<s]
print("8B", q(60/180)); print("3B", q(9/180))
# couverture : probabilité qu'au moins une rangée sur 16 atteigne le seuil
print("8B couv", 1-(1-60/180)**16, "3B couv", 1-(1-45/180)**16)
def k(n): return n-(99*(n-1))//100
for n in (1700, 4300, 4380, 7000, 10075): print(n, k(n-1))
