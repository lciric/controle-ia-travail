import numpy as np, math
rng = np.random.default_rng(np.random.SeedSequence(2026112415))
# 1. inversion en niche parfaite avec R0
bad = 0
for _ in range(100000):
    p = rng.dirichlet([1,1,1]); bv = rng.uniform(0.01,0.99); eta = rng.uniform(0.05,5)
    R0 = rng.uniform(-3,3); dR = rng.uniform(0.05,3); C = rng.uniform(-2,4)
    R = np.array([R0, R0+dR, R0+dR]); beta = np.array([1,bv,1.0])
    A = p*beta*np.exp(eta*R); A/=A.sum()
    B = p*np.exp(eta*(beta*R-(1-beta)*C)); B/=B.sum()
    cond = eta*(1-bv)*(R0+dR+C) > math.log(1/bv)
    if (B[2]>A[2]) != cond and abs(B[2]-A[2])>1e-12: bad+=1
print("inversion desaccords", bad)
# 2. freinage transitoire sous gradient ordinaire (logits), penalite sur le visible seul
def dlogpf(pi, r):
    mu = pi@r; th = pi*(r-mu); return th[2]-pi@th
bad=0; n=0
for _ in range(100000):
    pi = rng.dirichlet([1,1,1]); bv = rng.uniform(0.01,0.99); dR=rng.uniform(0.1,3); C=rng.uniform(0,4)
    def r(C): return np.array([0, bv*dR-(1-bv)*C, dR])
    h=1e-6; d=(dlogpf(pi,r(C+h))-dlogpf(pi,r(C-h)))/(2*h)
    form = -(1-bv)*pi[1]*((pi**2).sum()-pi[1]-pi[2])
    if abs(d-form)>1e-6: bad+=1
    if pi[0]>1/math.sqrt(3):
        n+=1
        if d>=0: bad+=1
print("freinage desaccords", bad, "cas pi_h>1/sqrt3", n)
# 3. pieges par melange : rapport de densite 1/(1-q), TV = q ; seuil sans plancher
bad=0
for _ in range(20000):
    q=rng.uniform(0.01,0.9); rho=rng.uniform(0.02,0.5); eps=rng.uniform(0,0.3); dR=1.0
    tau=rng.uniform(1e-4,1)  # triche sur les contextes non marques
    M=1/(1-q); Cstar=((1-rho)*M+rho*eps)/(rho*(1-eps))*dR
    for C in (Cstar*1.01, Cstar*0.99):
        gain=(1-rho)*tau*dR + rho*(1-q)*tau*(eps*dR-(1-eps)*C)
        if (gain<0) != (C>Cstar): bad+=1
print("melange desaccords", bad)
# 4. point fixe sous normalisation par l'ecart-type (champ moyen, ancre) : pi ∝ p exp(eta rbar/sigma(pi))
p=np.array([0.85,0.14,0.01]); beta=np.array([1,0.2,0.6]); dR=1.0; C=0.5; eta=1.5
rbar=np.array([0, beta[1]*dR-(1-beta[1])*C, beta[2]*dR-(1-beta[2])*C])
def sigma(pi):
    m1 = pi@rbar
    m2 = pi[0]*0 + sum(pi[i]*(beta[i]*dR**2+(1-beta[i])*C**2) for i in (1,2))
    return math.sqrt(m2-m1**2)
th=np.log(p).copy()
for _ in range(400000):
    pi=np.exp(th-th.max()); pi/=pi.sum()
    g=(rbar-pi@rbar)/sigma(pi) - (np.log(pi)-np.log(p))/eta
    g=g-pi@g
    th+=0.01*g
pi=np.exp(th-th.max()); pi/=pi.sum()
fp=p*np.exp(eta*rbar/sigma(pi)); fp/=fp.sum()
Bsame=p*np.exp(eta*rbar); Bsame/=Bsame.sum()
print("ecart au point fixe auto-coherent", abs(pi-fp).max(), "ecart a B meme eta", abs(pi-Bsame).max(), "pression effective", eta/sigma(pi))
