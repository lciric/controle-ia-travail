"""Évaluateur exact d'un énoncé sur un monde : logique à valeurs V, F, I (indéfini), H (hors capacité).

- Toute valeur numérique est un `Fraction` ; un flottant lève `GardeArret` (`exact`).
- Connecteurs et quantificateurs à la Kleene, indépendants de l'ordre : « et » vaut F dès qu'un membre vaut F,
  sinon H ou I s'il en reste, sinon V ; « ou » symétriquement ; « implique » = (non a) ou b ; « pour tout » comme
  « et » sur le domaine, « il existe » comme « ou ». Parmi les valeurs non décisives, H l'emporte sur I.
- Préfixe universel de tête : ses variables NAT parcourent [0 .. borne] ; ses domaines bornés sont évalués sous
  les variables précédentes. Une instance = une affectation de ce préfixe.
"""
from __future__ import annotations

import math
from fractions import Fraction

from ..gardes import GardeArret
from .exact import HorsCapacite, Indefini, controler_taille, entier_exact, exact

V, F, I, H = "V", "F", "I", "H"


def et3(valeurs) -> str:
    vu_h = vu_i = False
    for x in valeurs:
        if x == F:
            return F
        vu_h |= x == H
        vu_i |= x == I
    return H if vu_h else (I if vu_i else V)


def ou3(valeurs) -> str:
    vu_h = vu_i = False
    for x in valeurs:
        if x == V:
            return V
        vu_h |= x == H
        vu_i |= x == I
    return H if vu_h else (I if vu_i else F)


def non3(x: str) -> str:
    return {V: F, F: V}.get(x, x)


class Evaluateur:
    def __init__(self, monde, capacites: dict):
        self.m = monde
        self.bits_max = int(capacites["taille_entier_bits"])
        self.exposant_max = int(capacites["exposant_max"])
        self.intervalle_max = int(capacites["intervalle_max"])
        self.fact_max = int(capacites["factorielle_max"])
        self.instances_max = int(capacites["instances_max"])

    # ------------------------------------------------------------ expressions
    def expr(self, e, env) -> Fraction:
        g = e[0]
        if g == "num":
            return exact(e[1])
        if g == "var":
            return exact(env[e[1]])
        if g == "cst":
            return exact(self.m.constantes()[e[1]])
        if g == "neg":
            return -self.expr(e[1], env)
        if g == "bin":
            a = self.expr(e[2], env)
            op = e[1]
            if op == "^":
                return self._puissance(a, self.expr(e[3], env))
            b = self.expr(e[3], env)
            if op == "+":
                r = a + b
            elif op == "-":
                r = a - b
            elif op == "*":
                r = a * b
            elif op == "/":
                if b == 0:
                    raise Indefini("division par zéro")
                r = a / b
            else:
                raise GardeArret(f"opérateur inconnu {op!r}")
            return controler_taille(exact(r), self.bits_max)
        if g == "fn":
            args = tuple(self.expr(a, env) for a in e[2])
            return controler_taille(exact(self._fonction(e[1], args)), self.bits_max)
        if g == "somme":
            bas = entier_exact(self.expr(e[2], env))
            haut = entier_exact(self.expr(e[3], env))
            self._taille_intervalle(bas, haut)
            total = Fraction(0)
            for k in range(bas, haut + 1):
                total += self.expr(e[4], {**env, e[1]: Fraction(k)})
                controler_taille(total, self.bits_max)
            return total
        if g == "somme_sur":
            bas, haut = self.m.vocabulaire().domaines[e[2][1]]
            total = Fraction(0)
            for k in range(bas, haut + 1):
                total += self.expr(e[3], {**env, e[1]: Fraction(k)})
            return controler_taille(total, self.bits_max)
        raise GardeArret(f"nœud d'expression inconnu {g!r}")

    def _taille_intervalle(self, bas, haut):
        if haut - bas + 1 > self.intervalle_max:
            raise HorsCapacite(f"intervalle de plus de {self.intervalle_max} éléments")

    def _puissance(self, a: Fraction, b: Fraction) -> Fraction:
        if b.denominator != 1:
            raise Indefini("exposant non entier")
        k = b.numerator
        if abs(k) > self.exposant_max:
            raise HorsCapacite(f"exposant {k} au-delà de {self.exposant_max}")
        if a == 0 and k < 0:
            raise Indefini("zéro à une puissance négative")
        if a != 0 and k * max(a.numerator.bit_length(), a.denominator.bit_length()) > self.bits_max * 2:
            raise HorsCapacite("puissance trop grande")
        return controler_taille(a ** k, self.bits_max)

    def _fonction(self, nom, args):
        if nom == "abs":
            return abs(args[0])
        if nom == "min":
            return min(args)
        if nom == "max":
            return max(args)
        if nom in ("mod", "quot", "pgcd"):
            a, b = entier_exact(args[0]), entier_exact(args[1])
            if nom == "pgcd":
                return Fraction(math.gcd(a, b))
            if b == 0:
                raise Indefini(f"{nom} par zéro")
            q = a // abs(b) if b > 0 else -(a // abs(b))
            r = a - abs(b) * (a // abs(b))
            return Fraction(r) if nom == "mod" else Fraction(q)
        if nom == "binom":
            n, k = entier_exact(args[0]), entier_exact(args[1])
            if n < 0:
                raise Indefini("binom à n négatif")
            if n > self.fact_max:
                raise HorsCapacite("binom trop grand")
            return Fraction(math.comb(n, k) if 0 <= k <= n else 0)
        if nom == "fact":
            n = entier_exact(args[0])
            if n < 0:
                raise Indefini("factorielle négative")
            if n > self.fact_max:
                raise HorsCapacite("factorielle trop grande")
            return Fraction(math.factorial(n))
        return self.m.appeler(nom, args)

    # ------------------------------------------------------------ formules
    def formule(self, f, env) -> str:
        g = f[0]
        if g == "vrai":
            return V
        if g == "faux":
            return F
        if g == "cmp":
            try:
                a = self.expr(f[2], env)
                b = self.expr(f[3], env)
            except Indefini:
                return I
            except HorsCapacite:
                return H
            op = f[1]
            r = {"=": a == b, "!=": a != b, "<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b}[op]
            return V if r else F
        if g == "non":
            return non3(self.formule(f[1], env))
        if g == "et":
            return et3(self.formule(x, env) for x in (f[1], f[2]))
        if g == "ou":
            return ou3(self.formule(x, env) for x in (f[1], f[2]))
        if g == "imp":
            return ou3((non3(self.formule(f[1], env)), self.formule(f[2], env)))
        if g in ("tout", "existe"):
            try:
                valeurs = self.valeurs_domaine(f[2], env, borne=None)
            except Indefini:
                return I
            except HorsCapacite:
                return H
            gen = (self.formule(f[3], {**env, f[1]: Fraction(k)}) for k in valeurs)
            return et3(gen) if g == "tout" else ou3(gen)
        raise GardeArret(f"nœud de formule inconnu {g!r}")

    def valeurs_domaine(self, d, env, borne):
        if d[0] == "NAT":
            if borne is None:
                raise GardeArret("NAT hors du préfixe de tête : l'analyseur aurait dû refuser")
            return range(0, borne + 1)
        if d[0] == "dom":
            bas, haut = self.m.vocabulaire().domaines[d[1]]
            return range(bas, haut + 1)
        bas = entier_exact(self.expr(d[1], env))
        haut = entier_exact(self.expr(d[2], env))
        self._taille_intervalle(bas, haut)
        return range(bas, haut + 1)


# ---------------------------------------------------------------- préfixe et parcours des instances
def prefixe(f):
    """Préfixe universel de tête [(var, domaine)] et corps."""
    pre = []
    while f[0] == "tout":
        pre.append((f[1], f[2]))
        f = f[3]
    return pre, f


def hypotheses(corps):
    """Hypothèses d'un corps « H1 implique (H2 implique C) » : [H1, H2] et la conclusion C."""
    hyps = []
    while corps[0] == "imp":
        hyps.append(corps[1])
        corps = corps[2]
    return hyps, corps


def parcourir(ev: Evaluateur, f, borne: int, avec_valeur=True):
    """Énumère les instances du préfixe de tête jusqu'à `borne` (variables NAT) dans l'ordre lexicographique.

    Rend des couples (instance, statut) ; une instance dont un domaine est indéfini ou hors capacité est rendue
    partielle, avec le statut I ou H. Lève `HorsCapacite` si le nombre d'instances dépasse le plafond."""
    pre, corps = prefixe(f)
    compte = [0]

    def rec(i, env):
        if i == len(pre):
            compte[0] += 1
            if compte[0] > ev.instances_max:
                raise HorsCapacite(f"plus de {ev.instances_max} instances")
            yield dict(env), (ev.formule(corps, env) if avec_valeur else None)
            return
        var, dom = pre[i]
        try:
            valeurs = ev.valeurs_domaine(dom, env, borne)
        except Indefini:
            yield dict(env), I
            return
        except HorsCapacite:
            yield dict(env), H
            return
        for k in valeurs:
            env[var] = Fraction(k)
            yield from rec(i + 1, env)
            del env[var]

    yield from rec(0, {})


def instance_texte(inst: dict) -> dict:
    return {k: (int(v) if Fraction(v).denominator == 1 else str(v)) for k, v in inst.items()}


def variables_nat(f) -> list[str]:
    pre, _ = prefixe(f)
    return [v for v, d in pre if d[0] == "NAT"]
