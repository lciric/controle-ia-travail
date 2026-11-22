"""Grammaire fermée des énoncés d'un monde planté : analyseur, imprimeur, schéma de sortie d'un proposeur.

Syntaxe (ASCII seulement ; tout autre caractère rend l'énoncé « informe ») :

    enonce    := implique
    implique  := ou [ "implique" implique ]                (associatif à droite, priorité la plus basse)
    ou        := et { "ou" et }
    et        := non { "et" non }
    non       := "non" non | quant | atome
    quant     := ("pour" "tout" | "il" "existe") VAR "dans" domaine "," implique
    domaine   := "NAT" | NOM_DE_DOMAINE | "[" expr ".." expr "]"
    atome     := "vrai" | "faux" | "(" implique ")" | expr OP expr        OP ∈ = != < <= > >=
    expr      := terme { ("+" | "-") terme }
    terme     := facteur { ("*" | "/") facteur }
    facteur   := "-" facteur | puissance
    puissance := primaire [ "^" facteur ]
    primaire  := NOMBRE | VAR | CONSTANTE | FONCTION "(" expr { "," expr } ")" | "(" expr ")"
               | "somme" "(" VAR "," expr "," expr "," expr ")" | "somme_sur" "(" VAR "," NOM_DE_DOMAINE "," expr ")"

Règles de portée : toute variable est liée (quantificateur ou somme) ; une variable ne masque ni une constante, ni
une fonction, ni un domaine, ni une autre variable liée ; le domaine « NAT » (entiers naturels, tronqués à la borne N
pour la vérité bornée) n'est admis que dans le préfixe universel de tête : tous les autres quantificateurs sont bornés.

Arbre (tuples) — expressions : ('num', Fraction) ('var', nom) ('cst', nom) ('fn', nom, args) ('bin', op, a, b)
('neg', a) ('somme', var, bas, haut, corps) ('somme_sur', var, domaine, corps) ; domaines : ('NAT',) ('dom', nom)
('int', bas, haut) ; formules : ('cmp', op, a, b) ('non', f) ('et', f, g) ('ou', f, g) ('imp', f, g) ('vrai',)
('faux',) ('tout', var, domaine, f) ('existe', var, domaine, f).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from fractions import Fraction

from .exact import frac_vers_texte

MOTS_CLES = {"pour", "tout", "il", "existe", "dans", "et", "ou", "non", "implique", "vrai", "faux", "NAT",
             "somme", "somme_sur"}
# fonctions intégrées : nom → arité
INTEGREES = {"abs": 1, "min": 2, "max": 2, "mod": 2, "quot": 2, "pgcd": 2, "binom": 2, "fact": 1}
OPS_CMP = ("<=", ">=", "!=", "=", "<", ">")
LONGUEUR_MAX_ENONCE = 2000
LONGUEUR_MAX_CE_QUI_TUERAIT = 1000
PROFONDEUR_MAX_ANALYSE = 60


class FormeInvalide(Exception):
    """Sortie hors schéma ou hors grammaire : la proposition est « informe » (A12 : jamais corrigée)."""


@dataclass(frozen=True)
class Vocabulaire:
    constantes: dict = field(default_factory=dict)  # nom → Fraction
    fonctions: dict = field(default_factory=dict)  # nom → arité
    domaines: dict = field(default_factory=dict)  # nom → (bas, haut) entiers inclus

    def reserve(self, nom: str) -> bool:
        return nom in MOTS_CLES or nom in INTEGREES or nom in self.constantes or nom in self.fonctions \
            or nom in self.domaines


_JETON = re.compile(r"\s*(?:(\d+\.\d+|\d+)|([A-Za-z_][A-Za-z0-9_]*)|(\.\.|<=|>=|!=|[=<>+\-*/^(),\[\]]))")


def lexer(texte: str) -> list[tuple[str, str]]:
    if not isinstance(texte, str):
        raise FormeInvalide("l'énoncé n'est pas un texte")
    if len(texte) > LONGUEUR_MAX_ENONCE:
        raise FormeInvalide(f"énoncé de plus de {LONGUEUR_MAX_ENONCE} caractères")
    if any(ord(c) > 126 or (ord(c) < 32 and c not in " \t\n") for c in texte):
        raise FormeInvalide("caractère hors de l'alphabet ASCII de la grammaire")
    jetons, pos = [], 0
    while pos < len(texte):
        if texte[pos:].strip() == "":
            break
        m = _JETON.match(texte, pos)
        if not m or m.end() == pos:
            raise FormeInvalide(f"caractère inattendu à la position {pos} : {texte[pos:pos + 10]!r}")
        if m.group(1) is not None:
            jetons.append(("nombre", m.group(1)))
        elif m.group(2) is not None:
            jetons.append(("nom", m.group(2)))
        else:
            jetons.append(("sym", m.group(3)))
        pos = m.end()
    return jetons


class _Analyseur:
    def __init__(self, jetons, vocab: Vocabulaire):
        self.j, self.i, self.v = jetons, 0, vocab
        self.liees: list[str] = []
        self.en_tete = True  # vrai tant qu'on est dans le préfixe universel de tête
        self.profondeur = 0

    # -- outils
    def voir(self, k=0):
        return self.j[self.i + k] if self.i + k < len(self.j) else ("fin", "")

    def est(self, genre, val=None, k=0):
        t = self.voir(k)
        return t[0] == genre and (val is None or t[1] == val)

    def prendre(self, genre, val=None):
        t = self.voir()
        if t[0] != genre or (val is not None and t[1] != val):
            raise FormeInvalide(f"attendu {val or genre}, trouvé {t[1] or 'la fin'!r}")
        self.i += 1
        return t[1]

    def _plonger(self):
        self.profondeur += 1
        if self.profondeur > PROFONDEUR_MAX_ANALYSE:
            raise FormeInvalide("énoncé trop profond")

    # -- formules
    def enonce(self):
        f = self.implique()
        if self.voir()[0] != "fin":
            raise FormeInvalide(f"jeton en trop : {self.voir()[1]!r}")
        return f

    def implique(self):
        self._plonger()
        g = self.ou()
        if self.est("nom", "implique"):
            self.en_tete = False
            self.i += 1
            d = self.implique()
            g = ("imp", g, d)
        self.profondeur -= 1
        return g

    def ou(self):
        g = self.et()
        while self.est("nom", "ou"):
            self.en_tete = False
            self.i += 1
            g = ("ou", g, self.et())
        return g

    def et(self):
        g = self.non()
        while self.est("nom", "et"):
            self.en_tete = False
            self.i += 1
            g = ("et", g, self.non())
        return g

    def non(self):
        if self.est("nom", "non"):
            self.en_tete = False
            self.i += 1
            self._plonger()
            f = ("non", self.non())
            self.profondeur -= 1
            return f
        if self.est("nom", "pour") or self.est("nom", "il"):
            return self.quant()
        return self.atome()

    def quant(self):
        if self.est("nom", "pour"):
            self.i += 1
            self.prendre("nom", "tout")
            genre = "tout"
        else:
            self.i += 1
            self.prendre("nom", "existe")
            genre = "existe"
        if genre == "existe":
            self.en_tete = False
        var = self.prendre("nom")
        self._verifier_nouveau_nom(var)
        self.prendre("nom", "dans")
        dom = self.domaine(genre)
        self.prendre("sym", ",")
        self.liees.append(var)
        corps = self.implique()
        self.liees.pop()
        return (genre, var, dom, corps)

    def domaine(self, genre):
        if self.est("nom", "NAT"):
            self.i += 1
            if not (genre == "tout" and self.en_tete):
                raise FormeInvalide("« NAT » n'est admis que dans le préfixe universel de tête")
            return ("NAT",)
        if self.est("sym", "["):
            en_tete = self.en_tete
            self.i += 1
            bas = self.expr()
            self.prendre("sym", "..")
            haut = self.expr()
            self.prendre("sym", "]")
            self.en_tete = en_tete
            return ("int", bas, haut)
        nom = self.prendre("nom")
        if nom not in self.v.domaines:
            raise FormeInvalide(f"domaine inconnu {nom!r}")
        return ("dom", nom)

    def _verifier_nouveau_nom(self, var):
        if var in MOTS_CLES or self.v.reserve(var):
            raise FormeInvalide(f"nom de variable réservé {var!r}")
        if var in self.liees:
            raise FormeInvalide(f"variable {var!r} déjà liée")

    def atome(self):
        if self.est("nom", "vrai"):
            self.i += 1
            return ("vrai",)
        if self.est("nom", "faux"):
            self.i += 1
            return ("faux",)
        if self.est("sym", "("):
            # parenthèse de formule ou d'expression : on essaie la formule, puis l'expression
            sauve = (self.i, self.en_tete, self.profondeur)
            self.i += 1
            try:
                f = self.implique()
                self.prendre("sym", ")")
                if not self._est_op_cmp():
                    return f
            except FormeInvalide:
                pass
            self.i, self.en_tete, self.profondeur = sauve
        self.en_tete = False
        a = self.expr()
        if not self._est_op_cmp():
            raise FormeInvalide(f"comparaison attendue après une expression, trouvé {self.voir()[1] or 'la fin'!r}")
        op = self.prendre("sym")
        b = self.expr()
        if self._est_op_cmp():
            raise FormeInvalide("comparaisons enchaînées interdites")
        return ("cmp", op, a, b)

    def _est_op_cmp(self):
        return self.voir()[0] == "sym" and self.voir()[1] in OPS_CMP

    # -- expressions
    def expr(self):
        self._plonger()
        a = self.terme()
        while self.est("sym", "+") or self.est("sym", "-"):
            op = self.prendre("sym")
            a = ("bin", op, a, self.terme())
        self.profondeur -= 1
        return a

    def terme(self):
        a = self.facteur()
        while self.est("sym", "*") or self.est("sym", "/"):
            op = self.prendre("sym")
            a = ("bin", op, a, self.facteur())
        return a

    def facteur(self):
        if self.est("sym", "-"):
            self.i += 1
            self._plonger()
            f = ("neg", self.facteur())
            self.profondeur -= 1
            return f
        p = self.primaire()
        if self.est("sym", "^"):
            self.i += 1
            p = ("bin", "^", p, self.facteur())
        return p

    def primaire(self):
        t = self.voir()
        if t[0] == "nombre":
            self.i += 1
            return ("num", Fraction(t[1]))
        if self.est("sym", "("):
            self.i += 1
            e = self.expr()
            self.prendre("sym", ")")
            return e
        if t[0] != "nom":
            raise FormeInvalide(f"expression attendue, trouvé {t[1] or 'la fin'!r}")
        nom = t[1]
        self.i += 1
        if nom == "somme":
            self.prendre("sym", "(")
            var = self.prendre("nom")
            self._verifier_nouveau_nom(var)
            self.prendre("sym", ",")
            bas = self.expr()
            self.prendre("sym", ",")
            haut = self.expr()
            self.prendre("sym", ",")
            self.liees.append(var)
            corps = self.expr()
            self.liees.pop()
            self.prendre("sym", ")")
            return ("somme", var, bas, haut, corps)
        if nom == "somme_sur":
            self.prendre("sym", "(")
            var = self.prendre("nom")
            self._verifier_nouveau_nom(var)
            self.prendre("sym", ",")
            dom = self.prendre("nom")
            if dom not in self.v.domaines:
                raise FormeInvalide(f"domaine inconnu {dom!r}")
            self.prendre("sym", ",")
            self.liees.append(var)
            corps = self.expr()
            self.liees.pop()
            self.prendre("sym", ")")
            return ("somme_sur", var, ("dom", dom), corps)
        if nom in MOTS_CLES:
            raise FormeInvalide(f"mot-clé {nom!r} à la place d'une expression")
        if nom in self.liees:
            if self.est("sym", "("):
                raise FormeInvalide(f"variable {nom!r} appelée comme une fonction")
            return ("var", nom)
        if nom in self.v.constantes:
            if self.est("sym", "("):
                raise FormeInvalide(f"constante {nom!r} appelée comme une fonction")
            return ("cst", nom)
        arite = INTEGREES.get(nom, self.v.fonctions.get(nom))
        if arite is None:
            raise FormeInvalide(f"identifiant inconnu ou variable libre {nom!r}")
        self.prendre("sym", "(")
        args = [self.expr()]
        while self.est("sym", ","):
            self.i += 1
            args.append(self.expr())
        self.prendre("sym", ")")
        if len(args) != arite:
            raise FormeInvalide(f"{nom} attend {arite} argument(s), {len(args)} donné(s)")
        return ("fn", nom, tuple(args))


def _nat_hors_tete(f) -> bool:
    """Vrai si un domaine NAT apparaît ailleurs que dans le préfixe universel de tête de l'arbre."""
    while isinstance(f, tuple) and f and f[0] == "tout":
        f = f[3]  # le domaine de tête peut être NAT ; il ne contient pas de quantificateur

    def contient(x):
        if not isinstance(x, tuple) or not x:
            return False
        if x == ("NAT",):
            return True
        return any(contient(y) for y in x[1:])

    return contient(f)


def analyser(texte: str, vocab: Vocabulaire):
    """Texte → arbre ; lève `FormeInvalide` hors grammaire.

    Contrôle sur l'arbre (v2, remarque 1 de la contre-lecture) : un quantificateur sur NAT hors du préfixe universel de
    tête est refusé ici, quelle que soit la façon dont l'analyse l'a atteint (parenthèses, « et », « ou »…)."""
    jetons = lexer(texte)
    if not jetons:
        raise FormeInvalide("énoncé vide")
    arbre = _Analyseur(jetons, vocab).enonce()
    if _nat_hors_tete(arbre):
        raise FormeInvalide("« NAT » n'est admis que dans le préfixe universel de tête")
    return arbre


# ---------------------------------------------------------------- imprimeur (parenthésage complet, réanalysable)
def imprimer_expr(e) -> str:
    g = e[0]
    if g == "num":
        s = frac_vers_texte(e[1])
        return f"({s})" if ("/" in s or s.startswith("-")) else s
    if g in ("var", "cst"):
        return e[1]
    if g == "fn":
        return f"{e[1]}(" + ", ".join(imprimer_expr(a) for a in e[2]) + ")"
    if g == "bin":
        return f"({imprimer_expr(e[2])} {e[1]} {imprimer_expr(e[3])})"
    if g == "neg":
        return f"(-{imprimer_expr(e[1])})"
    if g == "somme":
        return f"somme({e[1]}, {imprimer_expr(e[2])}, {imprimer_expr(e[3])}, {imprimer_expr(e[4])})"
    if g == "somme_sur":
        return f"somme_sur({e[1]}, {e[2][1]}, {imprimer_expr(e[3])})"
    raise ValueError(f"nœud d'expression inconnu {g!r}")


def imprimer_domaine(d) -> str:
    if d[0] == "NAT":
        return "NAT"
    if d[0] == "dom":
        return d[1]
    return f"[{imprimer_expr(d[1])} .. {imprimer_expr(d[2])}]"


def imprimer(f) -> str:
    g = f[0]
    if g == "vrai":
        return "vrai"
    if g == "faux":
        return "faux"
    if g == "cmp":
        return f"{imprimer_expr(f[2])} {f[1]} {imprimer_expr(f[3])}"
    if g == "non":
        return f"non ({imprimer(f[1])})"
    if g in ("et", "ou"):
        return f"({imprimer(f[1])}) {g} ({imprimer(f[2])})"
    if g == "imp":
        return f"({imprimer(f[1])}) implique ({imprimer(f[2])})"
    if g in ("tout", "existe"):
        tete = "pour tout" if g == "tout" else "il existe"
        return f"{tete} {f[1]} dans {imprimer_domaine(f[2])}, {imprimer(f[3])}"
    raise ValueError(f"nœud de formule inconnu {g!r}")


# ---------------------------------------------------------------- schéma de sortie d'un proposeur
CLES_SCHEMA = ("enonce", "ce_qui_le_tuerait", "confiance")


def _refuser_constante(nom):
    raise FormeInvalide(f"constante JSON {nom} refusée")


def lire_sortie(sortie) -> dict:
    """Sortie d'un proposeur (texte JSON ou dict) → dict validé ; lève `FormeInvalide` hors schéma.

    Schéma : exactement les clés « enonce » (texte), « ce_qui_le_tuerait » (texte non vide : forme d'instance attendue
    en contre-exemple), « confiance » (nombre ou texte rationnel dans [0, 1], lu exactement)."""
    if isinstance(sortie, (str, bytes)):
        try:
            d = json.loads(sortie, parse_float=Fraction, parse_constant=_refuser_constante)
        except FormeInvalide:
            raise
        except (ValueError, TypeError) as e:
            raise FormeInvalide(f"JSON illisible : {e}") from None
    else:
        d = sortie
    if not isinstance(d, dict):
        raise FormeInvalide("objet JSON attendu")
    if set(d) != set(CLES_SCHEMA):
        raise FormeInvalide(f"clés {sorted(d)} au lieu de {sorted(CLES_SCHEMA)}")
    if not isinstance(d["enonce"], str):
        raise FormeInvalide("« enonce » n'est pas un texte")
    t = d["ce_qui_le_tuerait"]
    if not isinstance(t, str) or not t.strip() or len(t) > LONGUEUR_MAX_CE_QUI_TUERAIT:
        raise FormeInvalide("« ce_qui_le_tuerait » vide, trop long ou non textuel")
    c = d["confiance"]
    if isinstance(c, bool) or isinstance(c, float):
        raise FormeInvalide("« confiance » : booléen ou flottant refusé (lu exactement seulement)")
    if isinstance(c, str):
        try:
            c = Fraction(c.strip())
        except (ValueError, ZeroDivisionError):
            raise FormeInvalide(f"« confiance » illisible {d['confiance']!r}") from None
    if not isinstance(c, (int, Fraction)) or not (0 <= c <= 1):
        raise FormeInvalide("« confiance » hors de [0, 1]")
    return {"enonce": d["enonce"], "ce_qui_le_tuerait": t, "confiance": Fraction(c)}
