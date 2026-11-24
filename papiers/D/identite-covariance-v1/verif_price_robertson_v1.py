"""Verifie que l'identite de variance du theoreme 1, partie 1, est l'equation (4)
de Price 1970 (p. 520) avec z_i = beta_i (valeur selective), q_i = beta_i (trait),
Delta q_i = 0 (pas de terme de transmission), normalisee par la moyenne de z ;
et la forme de Robertson 1966 (p. 97) : D = Cov(y, q)/q_bar avec y = beta."""
from fractions import Fraction as F
import random

def moments(w, x):
    E = sum(wi*xi for wi, xi in zip(w, x))
    return E

def verifie(poids, beta, trait=None):
    # poids : loi mu_tr (somme 1) ; beta : survie ; trait : valeur du trait (defaut beta)
    trait = beta if trait is None else trait
    Eb = moments(poids, beta)
    Et = moments(poids, trait)
    # loi apres operateur A conditionnee aux tricheurs : densite beta / E[beta]
    post = [p*b/Eb for p, b in zip(poids, beta)]
    E_post_t = moments(post, trait)
    # Price (4), z = beta, q = trait, Delta q_i = 0 : Delta Q = Cov(z, q)/z_bar
    cov = moments(poids, [b*t for b, t in zip(beta, trait)]) - Eb*Et
    price = cov/Eb
    # Price (3) sous forme directe : Q2 = sum z_i q'_i / (N z_bar), avec q'_i = q_i
    Q2 = sum(p*b*t for p, b, t in zip(poids, beta, trait))/Eb
    var = moments(poids, [b*b for b in beta]) - Eb*Eb
    return E_post_t - Et, price, Q2 - Et, (var/Eb if trait is beta else None)

# exemple rationnel du manuscrit (poids 1/2, 1/3, 1/6 ; survies 1/10, 2/5, 9/10)
p = [F(1,2), F(1,3), F(1,6)]; b = [F(1,10), F(2,5), F(9,10)]
print("exemple manuscrit :", verifie(p, b))
# exemple R2 du manuscrit : deux atomes equiprobables, audit (2/10, 8/10)
pa = [F(1,2), F(1,2)]; bl = [F(1,10), F(9,10)]; au = [F(2,10), F(8,10)]
d, pr, q2, _ = verifie(pa, bl, au)
print("R2 : E_post[audit] =", F(1,2)+d, "; Price Cov/E =", pr)
# tirages aleatoires rationnels
rng = random.Random(20261124)
ok = 0
for _ in range(2000):
    k = rng.randint(2, 7)
    w = [F(rng.randint(1, 50)) for _ in range(k)]; s = sum(w); w = [x/s for x in w]
    bb = [F(rng.randint(0, 100), 100) for _ in range(k)]
    if sum(x*y for x, y in zip(w, bb)) == 0: continue
    a, c, e, v = verifie(w, bb)
    assert a == c == e == v, (w, bb)
    tt = [F(rng.randint(-100, 100), 37) for _ in range(k)]
    a2, c2, e2, _ = verifie(w, bb, tt)
    assert a2 == c2 == e2
    ok += 1
print("tirages verifies en arithmetique exacte :", ok)
