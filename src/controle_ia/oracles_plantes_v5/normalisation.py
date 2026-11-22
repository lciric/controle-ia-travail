"""Normaliseur : forme normale canonique d'un énoncé, empreinte de lignée, squelette du préfixe.

Ce qu'il fait, exactement (rien de plus) :
- expressions → polynômes à coefficients rationnels exacts sur des « atomes opaques » (variables, applications de
  fonctions dérivées du monde, sommes non développées, puissances à exposant variable, divisions par une expression
  non constante) ; les constantes du monde sont substituées ; les fonctions « définitionnelles » du monde (paramètres
  servis : lois P et Q, marges, termes d'une suite à indice littéral) sont évaluées à argument littéral ; les règles
  de réécriture du monde (définitions : récurrence, complément) sont appliquées ; les sommes à bornes littérales
  courtes sont développées ; l'arithmétique littérale est faite exactement ;
- comparaisons → « d < 0 », « d <= 0 », « d = 0 » ou « d != 0 », d mis à l'échelle (coefficient de tête 1, ou ±1
  pour < et <=) ; une comparaison constante est close à vrai ou faux ;
- formules → forme normale négative (implication réécrite, négations poussées jusqu'aux atomes et à travers les
  quantificateurs), « et » et « ou » aplatis, membres dédoublonnés et triés, constantes simplifiées ;
- variables liées renommées par position ; le préfixe de tête (universel, ou existentiel) est essayé dans toutes
  ses permutations compatibles avec les dépendances de domaines (au plus 5 variables), la plus petite chaîne retenue.
Ce qu'il ne fait pas : aucune énumération d'instances, aucune équivalence propre aux entiers (x < y + 1 contre
x <= y), aucune permutation de blocs de quantificateurs internes.
"""
from __future__ import annotations

import hashlib
import itertools
from dataclasses import dataclass
from fractions import Fraction

from .evaluation import Evaluateur, prefixe
from .exact import HorsCapacite, Indefini
from .grammaire import imprimer, imprimer_domaine

TERMES_MAX = 400
DEVELOPPEMENT_SOMME_MAX = 64
EXPOSANT_DEVELOPPE_MAX = 16
PERMUTATIONS_PREFIXE_MAX = 5


# ---------------------------------------------------------------- polynômes sur atomes opaques
COEF_BITS_MAX = 8192


def _borne_coef(c: Fraction) -> Fraction:
    """v4 : un coefficient démesuré lève `HorsCapacite` (sinon sa conversion en texte échoue au-delà de 4 300 chiffres) ;
    `normaliser` garde alors une forme brute de l'énoncé."""
    if c.numerator.bit_length() > COEF_BITS_MAX or c.denominator.bit_length() > COEF_BITS_MAX:
        raise HorsCapacite("coefficient démesuré")
    return c


def p_const(c) -> dict:
    c = _borne_coef(Fraction(c))
    return {(): c} if c != 0 else {}


def p_atome(cle: str) -> dict:
    return {((cle, 1),): Fraction(1)}


def p_add(a: dict, b: dict) -> dict:
    r = dict(a)
    for m, c in b.items():
        v = r.get(m, Fraction(0)) + c
        if v == 0:
            r.pop(m, None)
        else:
            r[m] = v
    return r


def p_scale(a: dict, k) -> dict:
    k = Fraction(k)
    return {m: _borne_coef(c * k) for m, c in a.items()} if k != 0 else {}


def _m_mul(m1, m2):
    d = dict(m1)
    for cle, e in m2:
        d[cle] = d.get(cle, 0) + e
    return tuple(sorted(d.items()))


def p_mul(a: dict, b: dict) -> dict:
    r: dict = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = _m_mul(m1, m2)
            v = _borne_coef(r.get(m, Fraction(0)) + c1 * c2)
            if v == 0:
                r.pop(m, None)
            else:
                r[m] = v
    if len(r) > TERMES_MAX:
        raise HorsCapacite("polynôme trop grand")
    return r


def p_est_const(a: dict) -> bool:
    return all(m == () for m in a)


def p_val(a: dict) -> Fraction:
    return a.get((), Fraction(0))


def _txt_frac(c: Fraction) -> str:
    return str(c.numerator) if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def p_str(a: dict) -> str:
    if not a:
        return "0"
    morceaux = []
    for m in sorted(a, key=lambda m: (len(m), m)):
        mon = "*".join(f"{k}" if e == 1 else f"{k}^{e}" for k, e in m)
        morceaux.append(f"{_txt_frac(a[m])}" + (f"·{mon}" if mon else ""))
    return " + ".join(morceaux)


def p_tete(a: dict) -> Fraction:
    m = sorted(a, key=lambda m: (len(m), m))[-1]
    return a[m]


def p_var_plus_const(a: dict):
    """Si a = x + c (x une variable de coefficient 1, c entier), rend (clé de x, c) ; sinon None."""
    vars_ = [m for m in a if m != ()]
    if len(vars_) != 1:
        return None
    m = vars_[0]
    if len(m) != 1 or m[0][1] != 1 or a[m] != 1 or not m[0][0].startswith("v:"):
        return None
    c = p_val(a)
    if c.denominator != 1:
        return None
    return m[0][0], c.numerator


# ---------------------------------------------------------------- contexte de normalisation
class _Ctx:
    """Variables liées nommées par profondeur de liaison (x0 pour la plus externe) : deux énoncés qui ne diffèrent que
    par l'ordre de membres contenant des quantificateurs reçoivent les mêmes noms."""

    def __init__(self, monde, ev: Evaluateur):
        self.m = monde
        self.ev = ev
        self.noms: dict[str, str] = {}  # nom d'origine → nom canonique
        self.valeurs: dict[str, dict] = {}  # variable de somme développée → polynôme constant
        self.pile: list[tuple[str, bool]] = []  # (nom canonique, NAT ?)
        # v2 (remarque 2) : sous-termes partiels rencontrés (fonctions, divisions, puissances, bornes), avant toute
        # simplification ; ils entrent dans la chaîne canonique pour que deux énoncés de même forme normale aient aussi
        # les mêmes points d'indéfinition possibles
        self.defs: set[str] = set()

    def lier(self, nom, nat=False) -> str:
        c = f"x{len(self.pile)}"
        self.pile.append((c, nat))
        self.noms[nom] = c
        return c

    def delier(self, nom, ancien):
        self.pile.pop()
        if ancien is None:
            self.noms.pop(nom, None)
        else:
            self.noms[nom] = ancien

    def est_nat(self, cle_var: str) -> bool:
        """`cle_var` = « v:xK » : vrai si xK est liée sur NAT."""
        c = cle_var[2:]
        return any(n == c and nat for n, nat in self.pile)


def _norm_expr(e, ctx: _Ctx) -> dict:
    g = e[0]
    if g == "num":
        return p_const(e[1])
    if g == "var":
        if e[1] in ctx.valeurs:
            return ctx.valeurs[e[1]]
        return p_atome("v:" + ctx.noms[e[1]])
    if g == "cst":
        return p_const(ctx.m.constantes()[e[1]])
    if g == "neg":
        return p_scale(_norm_expr(e[1], ctx), -1)
    if g == "bin":
        a = _norm_expr(e[2], ctx)
        b = _norm_expr(e[3], ctx)
        op = e[1]
        if op == "+":
            return p_add(a, b)
        if op == "-":
            return p_add(a, p_scale(b, -1))
        if op == "*":
            try:
                return p_mul(a, b)
            except HorsCapacite:  # v4 : un produit trop grand reste un atome opaque, jamais une exception
                return p_atome(f"mul({p_str(a)};{p_str(b)})")
        if op == "/":
            if not (p_est_const(b) and p_val(b) != 0):
                ctx.defs.add(f"div({p_str(b)})")
            if p_est_const(b):
                if p_val(b) == 0:
                    return p_atome(f"indef_div({p_str(a)};0)")
                return p_scale(a, 1 / p_val(b))
            return p_atome(f"div({p_str(a)};{p_str(b)})")
        if op == "^":
            if not (p_est_const(b) and p_val(b).denominator == 1 and p_val(b) >= 0):
                ctx.defs.add(f"pow({p_str(a)};{p_str(b)})")
            if p_est_const(b) and p_val(b).denominator == 1:
                k = p_val(b).numerator
                if p_est_const(a):
                    try:
                        return p_const(ctx.ev._puissance(p_val(a), Fraction(k)))
                    except (Indefini, HorsCapacite):
                        return p_atome(f"pow({p_str(a)};{k})")
                if 0 <= k <= EXPOSANT_DEVELOPPE_MAX:
                    r = p_const(1)
                    try:
                        for _ in range(k):
                            r = p_mul(r, a)
                        return r
                    except HorsCapacite:  # v4 : développement trop grand, puissance gardée opaque
                        pass
            return p_atome(f"pow({p_str(a)};{p_str(b)})")
    if g == "fn":
        args = [_norm_expr(a, ctx) for a in e[2]]
        nom = e[1]
        if nom not in ("abs", "min", "max"):
            ctx.defs.add(f"{nom}(" + ";".join(p_str(a) for a in args) + ")")
        if all(p_est_const(a) for a in args) and (nom in ("abs", "min", "max", "mod", "quot", "pgcd", "binom", "fact")
                                                  or ctx.m.est_definitionnelle(nom)):
            try:
                return p_const(ctx.ev._fonction(nom, tuple(p_val(a) for a in args)))
            except (Indefini, HorsCapacite):
                pass
        r = ctx.m.reecrire(nom, args, ctx)
        if r is not None:
            return r
        return p_atome(f"{nom}(" + ";".join(p_str(a) for a in args) + ")")
    if g == "somme":
        bas = _norm_expr(e[2], ctx)
        haut = _norm_expr(e[3], ctx)
        if not (p_est_const(bas) and p_est_const(haut)):
            ctx.defs.add(f"bornes({p_str(bas)};{p_str(haut)})")
        if p_est_const(bas) and p_est_const(haut) and p_val(bas).denominator == 1 and p_val(haut).denominator == 1:
            lo, hi = p_val(bas).numerator, p_val(haut).numerator
            if hi - lo + 1 <= DEVELOPPEMENT_SOMME_MAX:
                total: dict = {}
                for k in range(lo, hi + 1):
                    ancien = ctx.valeurs.get(e[1])
                    ctx.valeurs[e[1]] = p_const(k)
                    total = p_add(total, _norm_expr(e[4], ctx))
                    if ancien is None:
                        del ctx.valeurs[e[1]]
                    else:
                        ctx.valeurs[e[1]] = ancien
                return total
        ancien = ctx.noms.get(e[1])
        c = ctx.lier(e[1])
        corps = _norm_expr(e[4], ctx)
        ctx.delier(e[1], ancien)
        return p_atome(f"somme({c};{p_str(bas)};{p_str(haut)};{p_str(corps)})")
    if g == "somme_sur":
        ancien = ctx.noms.get(e[1])
        c = ctx.lier(e[1])
        corps = _norm_expr(e[3], ctx)
        ctx.delier(e[1], ancien)
        return p_atome(f"somme_sur({c};{e[2][1]};{p_str(corps)})")
    raise ValueError(f"nœud d'expression inconnu {g!r}")


# ---------------------------------------------------------------- formules en forme normale négative
COMPLEMENT = {"<": ">=", ">=": "<", "<=": ">", ">": "<=", "=": "!=", "!=": "="}
VRAI, FAUX = ("V",), ("F",)


def _atome(op, d: dict):
    """Atome canonique ("A", chaîne, base, polarité) : « d < 0 » a pour base « -d <= 0 » et polarité fausse,
    « d != 0 » a pour base « d = 0 » et polarité fausse ; la base sert à l'équivalence propositionnelle (redite)."""
    if op in (">", ">="):
        d = p_scale(d, -1)
        op = {">": "<", ">=": "<="}[op]
    if p_est_const(d):
        v = p_val(d)
        r = {"<": v < 0, "<=": v <= 0, "=": v == 0, "!=": v != 0}[op]
        return VRAI if r else FAUX
    t = p_tete(d)
    d = p_scale(d, 1 / t) if op in ("=", "!=") else p_scale(d, 1 / abs(t))
    chaine = f"{p_str(d)} {op} 0"
    if op == "=":
        return ("A", chaine, chaine, True)
    if op == "!=":
        return ("A", chaine, f"{p_str(d)} = 0", False)
    if op == "<=":
        return ("A", chaine, chaine, True)
    return ("A", chaine, f"{p_str(p_scale(d, -1))} <= 0", False)


def _chaine(n) -> str:
    g = n[0]
    if g in ("V", "F"):
        return g
    if g == "A":
        return f"[{n[1]}]"
    if g in ("ET", "OU"):
        return f"{g}(" + ", ".join(_chaine(x) for x in n[1]) + ")"
    if g == "Q":
        return f"{n[1]} {n[3]}∈{n[2]}: {_chaine(n[4])}"
    raise ValueError(g)


def _assoc(genre, membres):
    neutre, absorbant = (VRAI, FAUX) if genre == "ET" else (FAUX, VRAI)
    plats = []
    for x in membres:
        if x == absorbant:
            return absorbant
        if x == neutre:
            continue
        if x[0] == genre:
            plats.extend(x[1])
        else:
            plats.append(x)
    uniques = {(_chaine(x)): x for x in plats}
    if not uniques:
        return neutre
    if len(uniques) == 1:
        return next(iter(uniques.values()))
    return (genre, tuple(uniques[k] for k in sorted(uniques)))


def _domaine_str(d, ctx) -> str:
    if d[0] == "NAT":
        return "NAT"
    if d[0] == "dom":
        return d[1]
    bas, haut = _norm_expr(d[1], ctx), _norm_expr(d[2], ctx)
    if not (p_est_const(bas) and p_est_const(haut)):
        ctx.defs.add(f"bornes({p_str(bas)};{p_str(haut)})")
    return f"[{p_str(bas)};{p_str(haut)}]"


def _norm_f(f, ctx: _Ctx, neg: bool):
    g = f[0]
    if g == "vrai":
        return FAUX if neg else VRAI
    if g == "faux":
        return VRAI if neg else FAUX
    if g == "cmp":
        op = COMPLEMENT[f[1]] if neg else f[1]
        d = p_add(_norm_expr(f[2], ctx), p_scale(_norm_expr(f[3], ctx), -1))
        return _atome(op, d)
    if g == "non":
        return _norm_f(f[1], ctx, not neg)
    if g in ("et", "ou"):
        genre = {"et": "ET", "ou": "OU"}[g]
        if neg:
            genre = "OU" if genre == "ET" else "ET"
        return _assoc(genre, [_norm_f(f[1], ctx, neg), _norm_f(f[2], ctx, neg)])
    if g == "imp":
        # a implique b  ≡  (non a) ou b
        if neg:
            return _assoc("ET", [_norm_f(f[1], ctx, False), _norm_f(f[2], ctx, True)])
        return _assoc("OU", [_norm_f(f[1], ctx, True), _norm_f(f[2], ctx, False)])
    if g in ("tout", "existe"):
        genre = "∀" if (g == "tout") != neg else "∃"
        dom = _domaine_str(f[2], ctx)
        ancien = ctx.noms.get(f[1])
        c = ctx.lier(f[1], nat=f[2][0] == "NAT")
        corps = _norm_f(f[3], ctx, neg)
        ctx.delier(f[1], ancien)
        if corps in (VRAI, FAUX):
            # domaine vide possible pour les intervalles : on ne simplifie que les domaines non vides par nature
            if f[2][0] in ("NAT", "dom"):
                return corps
        return ("Q", genre, dom, c, corps)
    raise ValueError(f"nœud de formule inconnu {g!r}")


# ---------------------------------------------------------------- permutations du préfixe de tête
def _vars_expr(e, acc):
    if isinstance(e, tuple):
        if e and e[0] == "var":
            acc.add(e[1])
        # v5 (remarque 19) : un tuple d'arguments de fonction se parcourt en entier, premier argument compris
        for x in (e if e and not isinstance(e[0], str) else e[1:]):
            _vars_expr(x, acc)
    return acc


def _bloc_tete(f):
    """Bloc de tête de quantificateurs de même genre : [(genre, var, dom)], reste."""
    if f[0] not in ("tout", "existe"):
        return [], f
    genre = f[0]
    bloc = []
    while f[0] == genre:
        bloc.append((genre, f[1], f[2]))
        f = f[3]
    return bloc, f


def _permutations_valides(bloc):
    noms = [v for _, v, _ in bloc]
    if len(bloc) > PERMUTATIONS_PREFIXE_MAX:
        yield bloc
        return
    for perm in itertools.permutations(bloc):
        vus, ok = set(), True
        for _, v, d in perm:
            dep = _vars_expr(d, set()) & set(noms)
            if not dep <= vus:
                ok = False
                break
            vus.add(v)
        if ok:
            yield list(perm)


def _reconstruire(bloc, reste):
    f = reste
    for genre, v, d in reversed(bloc):
        f = (genre, v, d, f)
    return f


def renommer(f, table: dict):
    """Renomme les variables liées selon `table` (nom → nom) ; arbre neuf."""
    if not isinstance(f, tuple) or not f:
        return f
    g = f[0]
    if g == "var":
        return ("var", table.get(f[1], f[1]))
    if g in ("tout", "existe"):
        return (g, table.get(f[1], f[1]), renommer(f[2], table), renommer(f[3], table))
    if g == "somme":
        return (g, table.get(f[1], f[1]), renommer(f[2], table), renommer(f[3], table), renommer(f[4], table))
    if g == "somme_sur":
        return (g, table.get(f[1], f[1]), f[2], renommer(f[3], table))
    if g == "fn":
        return (g, f[1], tuple(renommer(a, table) for a in f[2]))
    if g in ("num", "cst"):
        return f
    if g in ("NAT", "dom"):
        return f
    return (g,) + tuple(renommer(x, table) if isinstance(x, tuple) else x for x in f[1:])


def _toutes_liees(f, acc):
    if isinstance(f, tuple) and f:
        if f[0] in ("tout", "existe", "somme", "somme_sur"):
            acc.append(f[1])
        for x in (f if not isinstance(f[0], str) else f[1:]):
            _toutes_liees(x, acc)
    return acc


@dataclass(frozen=True)
class Forme:
    chaine: str  # forme normale canonique, suivie des sous-termes partiels rencontrés (« ⟂déf{…} », v2)
    empreinte: str  # sha256 de la chaîne : clé du registre de lignée
    noeud: tuple  # forme normale négative (arbre)
    arbre: tuple  # arbre d'origine, préfixe permuté selon la forme retenue, variables renommées y0, y1…
    squelette: tuple  # domaines du préfixe universel de tête, sous forme canonique
    defs: frozenset = frozenset()  # sous-termes partiels rencontrés (v2, remarque 2)
    noms_prefixe: tuple = ()  # noms d'origine des variables du préfixe de tête, dans l'ordre canonique (v3)


def normaliser(f, monde, ev: Evaluateur) -> Forme:
    """Forme canonique ; si un calcul du normaliseur dépasse ses bornes (v4), forme brute : le texte imprimé de l'arbre,
    variables renommées, sans aucune équivalence (sûr : deux formes brutes égales sont le même texte)."""
    try:
        return _normaliser(f, monde, ev)
    except HorsCapacite:
        return _forme_brute(f)


def _forme_brute(f) -> Forme:
    table = {}
    for nom in _toutes_liees(f, []):
        if nom not in table:
            table[nom] = f"y{len(table)}"
    arbre = renommer(f, table)
    ch = "brut:" + imprimer(arbre)
    pre, _ = prefixe(arbre)
    sq = tuple("brut:" + imprimer_domaine(d) for _, d in pre)
    noeud = ("A", ch, ch, True)
    return Forme(ch, hashlib.sha256(ch.encode("utf-8")).hexdigest(), noeud, arbre, sq, frozenset({"brut"}),
                 tuple(v for v, _ in prefixe(f)[0]))


def _normaliser(f, monde, ev: Evaluateur) -> Forme:
    bloc, reste = _bloc_tete(f)
    meilleure = None
    for perm in _permutations_valides(bloc) if bloc else [[]]:
        g = _reconstruire(perm, reste) if bloc else f
        ctx = _Ctx(monde, ev)
        noeud = _norm_f(g, ctx, False)
        ch = _chaine(noeud) + " ⟂déf{" + ", ".join(sorted(ctx.defs)) + "}"
        if meilleure is None or ch < meilleure[0]:
            meilleure = (ch, noeud, g, frozenset(ctx.defs))
    ch, noeud, g, defs = meilleure
    # renommage d'évaluation : variables liées y0, y1… dans l'ordre de liaison
    table = {}
    for nom in _toutes_liees(g, []):
        if nom not in table:
            table[nom] = f"y{len(table)}"
    arbre = renommer(g, table)
    pre, _ = prefixe(arbre)
    ctx = _Ctx(monde, ev)
    sq = []
    for v, d in pre:
        sq.append(_domaine_str(d, ctx))
        ctx.noms[v] = f"x{len(ctx.pile)}"
        ctx.pile.append((ctx.noms[v], d[0] == "NAT"))
    noms = tuple(v for v, _ in prefixe(g)[0])
    return Forme(ch, hashlib.sha256(ch.encode("utf-8")).hexdigest(), noeud, arbre, tuple(sq), defs, noms)


def texte_canonique(forme: Forme) -> str:
    return imprimer(forme.arbre)
