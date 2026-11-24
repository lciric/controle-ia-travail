import math, itertools
inf = math.inf
def G(k, g, eta):
    return g*k if eta == inf else eta*(1-(1-g/eta)**k)
def Gam(K, g, eta):
    a = 1.0 if eta == inf else 1-g/eta
    return sum(a**(2*i) for i in range(K))
# 1. grille : 144 points, ceux où eps > c
bad = []
tot = 0
for K, n, g, eta, C, d in itertools.product([50,200,500],[100,1000],[0.05,0.2],[1,10,inf],[4,19],[0.05,0.1]):
    tot += 1
    dR = 1.0; W = dR + C
    c = 0.5*dR*G(K, g, eta)
    Lam = math.log(2*K/d); rb = dR/W
    eps = g*W*(math.sqrt(2*rb*Gam(K,g,eta)*Lam/n) + 2*Lam/(3*n))
    if eps > c: bad.append((K,n,g,eta,C,d,round(eps,4),round(c,4)))
print("points", tot, "eps>c", len(bad)); [print(" ", b) for b in bad]

# 2. critère final : plan concentré en fin d'horizon calculé avec gamma_hat, évalué sous gamma
def backloaded(K, g, eta, dR, C, c):
    W = dR + C; a = 1.0 if eta == inf else 1-g/eta
    D = dR*G(K,g,eta) - c
    rho = [0.0]*K
    if D <= 0: return rho
    if a == 0:
        rho[K-1] = D/(g*W); return rho
    m = max(mm for mm in range(K+1) if W*G(mm,g,eta) <= D + 1e-15)
    for j in range(K-m, K): rho[j] = 1.0
    if m < K: rho[K-1-m] = (D - W*G(m,g,eta))/(g*W*a**m)
    return rho
def xK(rho, K, g, eta, dR, C):
    W = dR + C; a = 1.0 if eta == inf else 1-g/eta
    x = 0.0
    for k in range(K): x = a*x + g*dR - g*W*rho[k]
    return x
# contrôle : plan exact faisable
for (K,g,eta,dR,C,c) in [(50,0.1,5,1,4,1.0),(30,0.2,inf,1,9,1.0),(40,0.5,0.5,1,2,0.2)]:
    r = backloaded(K,g,eta,dR,C,c); print("exact  x_K - c =", round(xK(r,K,g,eta,dR,C)-c, 12))
# majorant de gamma, eta fini : gamma_hat = eta (a_hat = 0), gamma < eta
K,g,eta,dR,C,c = 50,0.1,5,1,4,1.0
r = backloaded(K,eta,eta,dR,C,c)
print("gamma_hat=eta>gamma : x_K - c =", round(xK(r,K,g,eta,dR,C)-c,6), " dR*G_{K-1} - c =", round(dR*G(K-1,g,eta)-c,6))
# autre majorant, non dégénéré
r = backloaded(K,0.2,eta,dR,C,c); print("gamma_hat=0.2>0.1 : x_K - c =", round(xK(r,K,g,eta,dR,C)-c,6))
# minorant de gamma, eta infini
K,g,eta,dR,C,c = 30,0.2,inf,1,9,1.0
r = backloaded(K,0.1,eta,dR,C,c); print("gamma_hat=0.1<0.2, eta=inf : x_K - c =", round(xK(r,K,g,eta,dR,C)-c,6))
# minorant de gamma, eta fini
K,g,eta,dR,C,c = 50,0.2,5,1,4,1.0
r = backloaded(K,0.1,eta,dR,C,c); print("gamma_hat=0.1<0.2, eta=5 : x_K - c =", round(xK(r,K,g,eta,dR,C)-c,6))

# 3. exemples chiffrés repris tels quels
N,k,d = 257,1,0.05
q = lambda B: math.comb(N-k,B)/math.comb(N,B)
print("B*_det", min(B for B in range(N+1) if q(B) <= d), " approx", round(N/k*math.log(1/d),1))
