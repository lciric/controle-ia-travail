"""Graines (R9) de l'expérience bisociation à deux espaces v2, exactement comme au § 7 du préenregistrement scellé
`prereg/preenregistrement-bisociation-deux-espaces-v2.md` (e821e875…).

Chaque tâche reçoit numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle)) ;
une régénération (G11) ajoute le numéro de tentative comme quatrième élément (tentative 0 : clé à trois éléments).
Rééchantillonnage : spawn_key = (code_condition, code_contraste, 99) et, pour le second ensemble d'un écart entre
ensembles distincts, (code_condition, code_contraste, 99, 1).
"""
import numpy as np

from controle_ia.gardes import GardeArret, exiger_numpy_minimal

RACINE = 20261101
RACINE_VALIDATION = 20261102
RACINES_PERMISES = (RACINE, RACINE_VALIDATION)

CODES_CONDITION = {
    "M_bien": 1, "M_moyen": 2, "M_mal": 3, "SP": 4, "INV": 5, "V_fuite": 6, "V_concepts_absents": 7,
    "V_moyeu_conceptuel": 8, "V_surface": 9, "NR_bien": 10, "NR_moyen": 11, "M_inertes": 12,
    "M_couplage_faible": 13, "M_palettes_communes": 14, "M_palettes_disjointes": 15, "M_fonds_1ou2": 16,
}
ROLE_MONDE, ROLE_OBS_OPERATEURS, ROLE_OBS_CONCEPTS, ROLE_CONTRAINTES = 0, 1, 2, 3
ROLE_PLACEBO_PC, ROLE_PLACEBO_SP, ROLE_PLACEBO_PCG, ROLE_MIROIR = 4, 5, 6, 7
ROLE_BRAS_BASE, ROLE_REECHANTILLONNAGE = 10, 99


def sequence(racine, code_condition, indice, role, tentative=0, extra=None):
    """SeedSequence d'une tâche (§ 7). `extra` sert seulement au second flux du rééchantillonnage."""
    exiger_numpy_minimal()
    if racine not in RACINES_PERMISES:
        raise GardeArret(f"racine {racine} : seules RACINE={RACINE} et RACINE_VALIDATION={RACINE_VALIDATION} "
                         "sont permises (§ 7)")
    cle = (int(code_condition), int(indice), int(role))
    if tentative:
        cle = cle + (int(tentative),)
    if extra is not None:
        if role != ROLE_REECHANTILLONNAGE:
            raise GardeArret("quatrième élément « extra » réservé au rôle 99")
        cle = cle + (int(extra),)
    return np.random.SeedSequence(entropy=racine, spawn_key=cle)


def generateur(racine, code_condition, indice, role, tentative=0, extra=None):
    return np.random.default_rng(sequence(racine, code_condition, indice, role, tentative, extra))


class RngAdapte:
    """Interface de `random.Random` (celle qu'emploient les fonctions reprises de monde_v1) servie par un
    `numpy.random.Generator` issu d'une SeedSequence du § 7. Aucun état global."""

    def __init__(self, gen):
        self.g = gen

    def random(self):
        return float(self.g.random())

    def randrange(self, n):
        if n <= 0:
            raise ValueError("randrange sur un ensemble vide")
        return int(self.g.integers(n))

    def choice(self, seq):
        if len(seq) == 0:
            raise IndexError("choice sur une suite vide")
        return seq[int(self.g.integers(len(seq)))]

    def choices(self, population, weights=None, k=1):
        if weights is None:
            return [population[int(self.g.integers(len(population)))] for _ in range(k)]
        cumul = np.cumsum(np.asarray(weights, dtype=float))
        total = cumul[-1]
        out = []
        for _ in range(k):
            u = self.g.random() * total
            out.append(population[min(int(np.searchsorted(cumul, u, side="right")), len(population) - 1)])
        return out

    def shuffle(self, lst):
        perm = self.g.permutation(len(lst))
        lst[:] = [lst[i] for i in perm]

    def uniform(self, a, b):
        return a + (b - a) * float(self.g.random())

    def sample(self, population, k):
        population = list(population)
        idx = self.g.choice(len(population), size=k, replace=False)
        return [population[int(i)] for i in idx]
