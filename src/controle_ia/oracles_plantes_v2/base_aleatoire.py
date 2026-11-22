"""Base « grammaire aléatoire » : 24 énoncés par monde tirés dans la grammaire à profondeur bornée, par graine.

« Uniformément » s'entend ici production par production : à chaque nœud, chaque production admise à la profondeur
restante est choisie avec la même probabilité (et non uniformément sur l'ensemble des arbres) ; choix ouvert au
concepteur (note de choix). Préfixe : 0 à `quantificateurs_max` quantificateurs universels de tête, domaine tiré
parmi NAT et les domaines nommés du monde. Feuilles : littéral entier de 0 à `litteral_max`, variable liée,
constante du monde. Chaque énoncé est imprimé puis réanalysé : un énoncé que l'analyseur refuserait est un défaut
du générateur (`GardeArret`), jamais une sortie corrigée.
"""
from __future__ import annotations

from fractions import Fraction

from ..gardes import GardeArret
from .grammaire import INTEGREES, FormeInvalide, imprimer

FONCTIONS_INTEGREES_TIREES = ("abs", "min", "max", "mod")
OPS_BIN = ("+", "-", "*", "/", "^")
OPS_CMP = ("=", "!=", "<", "<=", ">", ">=")


def _choix(rng, seq):
    return seq[int(rng.integers(0, len(seq)))]


def _expr(rng, monde, prof, vars_, litteral_max):
    v = monde.vocabulaire()
    feuilles = ["num"] + (["var"] if vars_ else []) + (["cst"] if v.constantes else [])
    prods = feuilles if prof <= 0 else feuilles + ["fn", "bin", "neg"]
    g = _choix(rng, prods)
    if g == "num":
        return ("num", Fraction(int(rng.integers(0, litteral_max + 1))))
    if g == "var":
        return ("var", _choix(rng, vars_))
    if g == "cst":
        return ("cst", _choix(rng, sorted(v.constantes)))
    if g == "neg":
        return ("neg", _expr(rng, monde, prof - 1, vars_, litteral_max))
    if g == "bin":
        op = _choix(rng, OPS_BIN)
        a = _expr(rng, monde, prof - 1, vars_, litteral_max)
        b = (("num", Fraction(int(rng.integers(0, 4)))) if op == "^"
             else _expr(rng, monde, prof - 1, vars_, litteral_max))
        return ("bin", op, a, b)
    noms = sorted(v.fonctions) + list(FONCTIONS_INTEGREES_TIREES)
    nom = _choix(rng, noms)
    arite = v.fonctions.get(nom, INTEGREES.get(nom))
    return ("fn", nom, tuple(_expr(rng, monde, prof - 1, vars_, litteral_max) for _ in range(arite)))


def _formule(rng, monde, prof, vars_, litteral_max):
    prods = ["cmp"] if prof <= 0 else ["cmp", "non", "et", "ou", "imp"]
    g = _choix(rng, prods)
    if g == "cmp":
        return ("cmp", _choix(rng, OPS_CMP), _expr(rng, monde, prof, vars_, litteral_max),
                _expr(rng, monde, prof, vars_, litteral_max))
    if g == "non":
        return ("non", _formule(rng, monde, prof - 1, vars_, litteral_max))
    return ({"et": "et", "ou": "ou", "imp": "imp"}[g], _formule(rng, monde, prof - 1, vars_, litteral_max),
            _formule(rng, monde, prof - 1, vars_, litteral_max))


def tirer_enonce(rng, monde, cfg) -> str:
    nq = int(rng.integers(0, int(cfg["quantificateurs_max"]) + 1))
    domaines = ["NAT"] + sorted(monde.vocabulaire().domaines)
    pre = []
    for i in range(nq):
        d = _choix(rng, domaines)
        pre.append((f"z{i}", ("NAT",) if d == "NAT" else ("dom", d)))
    corps = _formule(rng, monde, int(cfg["profondeur_max"]), [v for v, _ in pre], int(cfg["litteral_max"]))
    f = corps
    for v, d in reversed(pre):
        f = ("tout", v, d, f)
    texte = imprimer(f)
    try:
        monde.analyser(texte)
    except FormeInvalide as e:
        raise GardeArret(f"base aléatoire : énoncé tiré non réanalysable ({e}) : {texte!r}") from None
    return texte


def tirer_base(rng, monde, cfg) -> list[str]:
    return [tirer_enonce(rng, monde, cfg) for _ in range(int(cfg["par_monde"]))]
