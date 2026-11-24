"""(1) Forme discrete : Delta w_bar / w_bar = Var(w / w_bar) (variance de la valeur
selective relative), equivalente a Delta w_bar = Var(w)/w_bar.
(2) Remarque : famille continue pi_s ∝ beta^s mu (rejet repete, s reel) ; avec
m = log beta (parametre malthusien par tour), d/ds E_s[m] = Var_s(m) : forme
clonale exacte, en temps continu, du theoreme de Fisher. Ce n'est PAS notre identite."""
from fractions import Fraction as F
import math, random
p = [F(1,2), F(1,3), F(1,6)]; b = [F(1,10), F(2,5), F(9,10)]
E = sum(x*y for x, y in zip(p, b)); V = sum(x*y*y for x, y in zip(p, b)) - E*E
post = sum(x*y*y for x, y in zip(p, b))/E
rel = [y/E for y in b]; Vrel = sum(x*r*r for x, r in zip(p, rel)) - 1
print("Delta w_bar =", post-E, "; Var/E =", V/E, "; Delta w_bar / w_bar =", (post-E)/E, "; Var(w/w_bar) =", Vrel)
def moments(s, pp, bb):
    w = [x*float(y)**s for x, y in zip(pp, bb)]; Z = sum(w); w = [x/Z for x in w]
    m = [math.log(float(y)) for y in bb]
    Em = sum(a*c for a, c in zip(w, m)); Vm = sum(a*c*c for a, c in zip(w, m)) - Em*Em
    return Em, Vm
pf = [float(x) for x in p]
rng = random.Random(1124); err = 0.0
for _ in range(200):
    k = rng.randint(2, 6); pp = [rng.random() for _ in range(k)]; Z = sum(pp); pp = [x/Z for x in pp]
    bb = [rng.uniform(0.01, 1) for _ in range(k)]; s = rng.uniform(0, 3); h = 1e-6
    d = (moments(s+h, pp, bb)[0] - moments(s-h, pp, bb)[0])/(2*h)
    err = max(err, abs(d - moments(s, pp, bb)[1]))
print("ecart max |d/ds E_s[log beta] - Var_s(log beta)| sur 200 tirages :", f"{err:.2e}")
s1 = moments(1, pf, b)[0] - moments(0, pf, b)[0]
print("pas s=0->1 : Delta E[log beta] =", f"{s1:.6f}", "; Var_0(log beta) =", f"{moments(0, pf, b)[1]:.6f}", "(different : la forme continue n'est exacte qu'a l'instant)")
