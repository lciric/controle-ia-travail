import numpy as np, math
rng=np.random.default_rng(np.random.SeedSequence(20261124))
# A. GRPO mean-field: sign of d/dC of f-advantage (r_f-mu)/sigma ; natural gradient d log pi_f/dt = r_f - mu
def stats(pi,bv,dR,C):
    rb=np.array([0.0, bv*dR-(1-bv)*C, dR]); mu=pi@rb
    m2=pi[1]*(bv*dR**2+(1-bv)*C**2)+pi[2]*dR**2
    return rb,mu,math.sqrt(max(m2-mu**2,1e-300))
pos_nat=0; pos_grpo=0; pos_grpo_hgt=0; n_hgt=0; N=100000
for _ in range(N):
    pi=rng.dirichlet([1,1,1]); bv=rng.uniform(0.01,0.99); dR=rng.uniform(0.1,3); C=rng.uniform(0,4); h=1e-6
    def advf(C):
        rb,mu,s=stats(pi,bv,dR,C); return (rb[2]-mu)/s, rb[2]-mu
    a1,n1=advf(C+h); a0,n0=advf(C-h)
    if n1>n0: pos_nat+=1
    if a1>a0: pos_grpo+=1
    if pi[0]>1/math.sqrt(3):
        n_hgt+=1
        if a1>a0: pos_grpo_hgt+=1
print("A. natural grad: d/dC (r_f-mu) >0 in", pos_nat,"/",N)
print("A. GRPO natural: d/dC adv_f >0 in", pos_grpo,"/",N, "; with pi_h>1/sqrt3:", pos_grpo_hgt,"/",n_hgt)
# B. refill with survivors + survivors mean baseline: fixed point = B at C=-b(pi), pressure eta/Zbar ?
p=np.array([0.85,0.14,0.01]); beta=np.array([1,0.2,0.6]); R=np.array([0,1.0,1.0]); eta=1.5
th=np.log(p).copy()
for _ in range(300000):
    pi=np.exp(th-th.max()); pi/=pi.sum()
    Z=pi@beta; b=(pi*beta)@R/Z
    a=beta*(R-b)/Z
    g=a-(np.log(pi)-np.log(p))/eta; g-=pi@g; th+=0.01*g
pi=np.exp(th-th.max()); pi/=pi.sum(); Z=pi@beta; b=(pi*beta)@R/Z
Cb=-b; Bfp=p*np.exp((eta/Z)*(beta*R-(1-beta)*Cb)); Bfp/=Bfp.sum()
B0=p*np.exp((eta/Z)*(beta*R)); B0/=B0.sum()
print("B. refill+mean baseline: gap to B(C=-b, eta/Z)", abs(pi-Bfp).max(), "; gap to B(C=0, eta/Z)", abs(pi-B0).max(), "b=",b)
# C. mixture traps: ess sup dP_ord/dP_trap with P_trap=q Q + (1-q) P_ord, discrete
worst=0
for _ in range(20000):
    k=6; Po=rng.dirichlet(np.ones(k)); Q=rng.dirichlet(np.ones(k)*0.3); q=rng.uniform(0.01,0.95)
    Pt=q*Q+(1-q)*Po; r=(Po/Pt).max()*(1-q); worst=max(worst,r)
print("C. max of ratio*(1-q) (should be <=1):", worst)
# D. GRPO with anchor: fixed point pi ∝ p exp(eta rbar/sigma(pi)) ; differs from B(eta)
