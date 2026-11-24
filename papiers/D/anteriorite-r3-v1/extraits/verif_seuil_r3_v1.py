from fractions import Fraction as F
def c_r3(rho,eps,delta,tmin,dR=F(1)):
    return ((1-rho)*tmin + rho*eps*(tmin-delta))/(rho*(1-eps)*(tmin-delta))*dR
def becker_gh(p,eps,dR=F(1)):
    # Gans-Holden eq.(11)-(12): g <= p*F*d with g=dR, d=1-eps, F=dR+C (forfeiture + penalty)
    # => C >= dR/(p*(1-eps)) - dR
    return dR/(p*(1-eps)) - dR
ex = c_r3(F(1,5),F(1,50),F(1,20),F(1,5))
print("C*_R3 exemple manuscrit:", float(ex))
for rho,eps in [(F(1,5),F(1,50)),(F(1,10),F(0)),(F(1,3),F(1,10))]:
    print(rho,eps,"delta=0:",c_r3(rho,eps,F(0),F(1,5)), "GH:",becker_gh(rho,eps), "egal:", c_r3(rho,eps,F(0),F(1,5))==becker_gh(rho,eps))
# facteur de correction delta
print("rapport exemple / delta=0:", float(ex/c_r3(F(1,5),F(1,50),F(0),F(1,5))))
