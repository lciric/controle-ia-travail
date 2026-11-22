"""Base commune des mondes plantés et outils de gabarits.

Un monde : des paramètres rationnels exacts tirés par graine, un vocabulaire (constantes, fonctions, domaines), une
borne N, des axiomes (définitions servies), des règles de réécriture pour le normaliseur, et des gabarits de
plantation. Ce qui est servi à un proposeur : `definition_servie()` ; la clé (étiquettes, instances) vit ailleurs.
"""
from __future__ import annotations

from fractions import Fraction

from ..gardes import GardeArret
from .evaluation import Evaluateur, parcourir
from .exact import HorsCapacite, Indefini, entier_strict, exact, frac_vers_texte
from .grammaire import Vocabulaire, analyser


def lit(f) -> str:
    """Littéral rationnel réanalysable : « 3 », « (7/24) », « (-5) », « (-7/24) »."""
    s = frac_vers_texte(exact(f))
    return s if (s.isdigit()) else f"({s})"


class Monde:
    famille = "?"

    def __init__(self, parametres: dict, borne_N: int, capacites: dict):
        self.p = parametres
        self.N = entier_strict(borne_N, "borne N")
        self.capacites = capacites
        self.ev = Evaluateur(self, capacites)
        self._vocab = None
        self._axiomes_ast = None
        self.perturbes: list = []  # mondes de même structure, pour le profil de redite (T5)

    # -- à fournir par chaque famille
    def _constantes(self) -> dict:
        raise NotImplementedError

    def _fonctions(self) -> dict:
        raise NotImplementedError

    def _domaines(self) -> dict:
        raise NotImplementedError

    def appeler(self, nom, args):
        raise NotImplementedError

    def axiomes(self) -> list[str]:
        raise NotImplementedError

    def descriptions(self) -> dict:
        raise NotImplementedError

    def parametres_servis(self) -> dict:
        raise NotImplementedError

    def definitionnelles(self) -> set:
        return set()

    def reecrire(self, nom, args, ctx):
        return None

    # -- communs
    def constantes(self) -> dict:
        c = dict(self._constantes())
        c["N"] = Fraction(self.N)
        return c

    def vocabulaire(self) -> Vocabulaire:
        if self._vocab is None:
            self._vocab = Vocabulaire(self.constantes(), self._fonctions(), self._domaines())
        return self._vocab

    def est_definitionnelle(self, nom) -> bool:
        return nom in self.definitionnelles()

    def empreinte_monde(self) -> str:
        """Empreinte de ce qui définit le monde (famille, N, paramètres servis, constantes) : sert au registre de
        lignée à ne comparer une proposition qu'aux mortes du même monde (v2, remarque 10)."""
        import hashlib
        import json
        d = {"famille": self.famille, "N": self.N, "parametres": self.parametres_servis(),
             "constantes": {k: frac_vers_texte(v) for k, v in sorted(self.constantes().items())}}
        return hashlib.sha256(json.dumps(d, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()

    def borne_verification(self) -> int:
        """Plafond des instances vérifiables (pièges et contre-exemples avancés par S) : 3N."""
        return 3 * self.N

    def analyser(self, texte):
        return analyser(texte, self.vocabulaire())

    def axiomes_ast(self):
        if self._axiomes_ast is None:
            self._axiomes_ast = [self.analyser(t) for t in self.axiomes()]
        return self._axiomes_ast

    def definition_servie(self, identifiant: str) -> dict:
        v = self.vocabulaire()
        return {
            "identifiant_monde": identifiant,
            "famille": self.famille,
            "borne_N": self.N,
            "parametres": self.parametres_servis(),
            "constantes": {k: frac_vers_texte(x) for k, x in sorted(v.constantes.items())},
            "domaines": {k: [a, b] for k, (a, b) in sorted(v.domaines.items())},
            "fonctions": {k: {"arite": a, "definition": self.descriptions()[k]} for k, a in sorted(v.fonctions.items())},
            "axiomes": self.axiomes(),
            "verite_bornee": ("un énoncé est vivant s'il n'est pas tué ; il est vrai-borné s'il est vrai sur toutes les "
                              "instances de son préfixe universel de tête dont les variables NAT valent au plus N"),
        }

    # -- outils de gabarits
    def valeurs_en_t(self, texte_expr: str, var: str, jusqua: int) -> list:
        """Valeurs exactes d'une expression en une variable NAT, de 0 à `jusqua` (None si indéfinie)."""
        f = self.analyser(f"pour tout {var} dans NAT, {texte_expr} = {texte_expr}")
        e = f[3][2]
        sortie = []
        for t in range(jusqua + 1):
            try:
                sortie.append(self.ev.expr(e, {var: Fraction(t)}))
            except (Indefini, HorsCapacite):  # la valeur manque ; le gabarit le voit et n'est pas réalisé
                sortie.append(None)
        return sortie

    def piege_seuil(self, rng, texte_expr: str, var: str = "t", essais: int = 4) -> list:
        """Candidats de piège « pour tout var dans NAT, E < c » : pour chaque essai, une instance n0 est tirée dans
        ]N .. 3N] et c = E(n0), retenue seulement si E(n0) dépasse strictement le maximum de E sur [0 .. N] (alors
        aucun contre-exemple jusqu'à N, et n0 en est un) ; le premier contre-exemple est n0 si E croît strictement,
        sinon une instance de ]N .. n0]. Liste vide si E manque quelque part ou si aucun tirage ne convient."""
        vals = self.valeurs_en_t(texte_expr, var, 3 * self.N)
        if any(x is None for x in vals):
            return []
        plafond_bas = max(vals[: self.N + 1])
        sortie = []
        for _ in range(int(essais)):
            n0 = int(rng.integers(self.N + 1, 3 * self.N + 1))
            if vals[n0] > plafond_bas:
                texte = f"pour tout {var} dans NAT, {texte_expr} < {lit(vals[n0])}"
                if texte not in sortie:
                    sortie.append(texte)
        return sortie


def _seuil_tot(self, rng, texte_expr: str, var: str = "t", essais: int = 4) -> list:
    """Candidats de faux tôt de forme seuil (v5, brouillon 2) : « pour tout var dans NAT, E < c », n0 tiré dans
    [1 .. N] et c = E(n0), retenu si E(n0) dépasse strictement le maximum de E sur [0 .. n0 - 1] : le premier
    contre-exemple est alors au plus n0, donc sous N. Même forme que les pièges ; seule la place du dépassement change."""
    vals = self.valeurs_en_t(texte_expr, var, self.N)
    if any(x is None for x in vals):
        return []
    sortie = []
    for _ in range(int(essais)):
        n0 = int(rng.integers(1, self.N + 1))
        if vals[n0] > max(vals[:n0]):
            texte = f"pour tout {var} dans NAT, {texte_expr} < {lit(vals[n0])}"
            if texte not in sortie:
                sortie.append(texte)
    return sortie


Monde.seuil_tot = _seuil_tot


def contre_exemple(monde: Monde, texte: str, borne: int):
    """Première instance (ordre lexicographique) où le corps vaut F ou I jusqu'à `borne`, sinon None."""
    f = monde.analyser(texte)
    for inst, st in parcourir(monde.ev, f, borne):
        if st in ("F", "I"):
            return inst
    return None


def exiger(condition: bool, motif: str):
    if not condition:
        raise GardeArret(motif)
