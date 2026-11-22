"""Arithmétique exacte : toute valeur d'un chemin de vérité est un `Fraction` (ou un entier converti).

Un flottant glissé dans un chemin de vérité lève `GardeArret` (aucun repli silencieux, R5).
"""
from __future__ import annotations

import re
from fractions import Fraction

from ..gardes import GardeArret


class Indefini(Exception):
    """Valeur mathématiquement indéfinie (division par zéro, indice négatif, argument hors du domaine)."""


class HorsCapacite(Exception):
    """Calcul exact borné dépassé (exposant, taille d'entier, longueur d'intervalle, indice) : rien n'est décidé."""


def exact(x) -> Fraction:
    """Contrôle d'entrée d'un chemin de vérité : entier ou `Fraction` seulement."""
    if isinstance(x, bool):
        raise GardeArret(f"booléen {x!r} employé comme nombre dans un chemin de vérité")
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    raise GardeArret(f"valeur non exacte de type {type(x).__name__} ({x!r}) dans un chemin de vérité : refusée")


_ENTIER = re.compile(r"^-?[0-9]+$")
_RATIONNEL = re.compile(r"^-?[0-9]+/[0-9]+$")
_DECIMAL = re.compile(r"^-?[0-9]+\.[0-9]+$")


def frac_depuis_texte(s: str) -> Fraction:
    """Lit « 3 », « -3/4 » ou « 0.25 » (décimal lu exactement, jamais par un flottant)."""
    if not isinstance(s, str):
        raise GardeArret(f"texte attendu, reçu {type(s).__name__}")
    s = s.strip()
    if _ENTIER.match(s) or _RATIONNEL.match(s) or _DECIMAL.match(s):
        f = Fraction(s)
        return f
    raise GardeArret(f"nombre illisible {s!r}")


def frac_vers_texte(f) -> str:
    f = exact(f)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def entier_exact(f) -> int:
    """Entier exigé ; un rationnel non entier lève `Indefini`."""
    f = exact(f)
    if f.denominator != 1:
        raise Indefini(f"entier attendu, reçu {f}")
    return f.numerator


def controler_taille(f: Fraction, bits_max: int) -> Fraction:
    if f.numerator.bit_length() > bits_max or f.denominator.bit_length() > bits_max:
        raise HorsCapacite(f"nombre de plus de {bits_max} bits")
    return f


def entier_strict(x, quoi: str = "paramètre") -> int:
    """Paramètre entier (v2, remarque 5) : un entier non booléen, ou un texte d'entier ; tout flottant est refusé, jamais
    tronqué."""
    if isinstance(x, bool):
        raise GardeArret(f"{quoi} : booléen {x!r} au lieu d'un entier")
    if isinstance(x, int):
        return x
    if isinstance(x, Fraction) and x.denominator == 1:
        return x.numerator
    if isinstance(x, str) and _ENTIER.match(x.strip()):
        return int(x.strip())
    raise GardeArret(f"{quoi} : {x!r} ({type(x).__name__}) n'est pas un entier exact : refusé")


def rationnel_strict(x, quoi: str = "paramètre") -> Fraction:
    """Paramètre rationnel (v2, remarque 5) : entier, `Fraction`, ou texte « a/b » lu exactement ; flottant refusé."""
    if isinstance(x, bool) or isinstance(x, float):
        raise GardeArret(f"{quoi} : {x!r} ({type(x).__name__}) refusé : rationnel exact attendu")
    if isinstance(x, (int, Fraction)):
        return Fraction(x)
    if isinstance(x, str):
        return frac_depuis_texte(x)
    raise GardeArret(f"{quoi} : {x!r} n'est pas un rationnel exact")
