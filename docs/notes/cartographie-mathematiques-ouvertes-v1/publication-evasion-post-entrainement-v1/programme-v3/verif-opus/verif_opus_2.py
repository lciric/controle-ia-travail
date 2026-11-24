import numpy as np, math
rng=np.random.default_rng(np.random.SeedSequence(20261124,spawn_key=(2,)))
N=100000; pos=0
for _ in range(N):
    pi=rng.dirichlet([1,1,1]); bv=rng.uniform(0.01,0.99); dR=rng.uniform(0.1,3); C=rng.uniform(0,4); h=1e-6
    def rate(C):
        rb=np.array([0.0,bv*dR-(1-bv)*C,dR]); mu=pi@rb
        m2=pi[1]*(bv*dR**2+(1-bv)*C**2)+pi[2]*dR**2
        return (rb[2]-rb[1])/math.sqrt(m2-mu**2)
    if rate(C+h)>rate(C-h): pos+=1
print("GRPO champ moyen: d/dC taux f:v >0 dans", pos, "/", N)
