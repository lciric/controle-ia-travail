"""« Retrouvée » (brouillon 2 du préenregistrement, § Métrique) : une proposition vraie-bornée est retrouvée si elle est
égale à une vérité plantée par l'étage 1 (même forme normale, sous-termes partiels compris) ou par l'étage 2
(équivalence propositionnelle sur les atomes normalisés, même squelette) de T5. L'étage 3 (profil) est exclu. Le
compte par égalité d'empreinte seule est rapporté en sensibilité (`retrouvee_empreinte_seule`).

Le contrôle « vraie-bornée » revient à l'appelant (script d'analyse, lot B3) : ces fonctions ne regardent que la forme.
"""
from __future__ import annotations

from .tests_de_mort import equivalence_propositionnelle


def retrouvee(forme, formes_verites: list):
    """Rend (indice de la vérité plantée, étage 1 ou 2) ou None."""
    for i, v in enumerate(formes_verites):
        if forme.empreinte == v.empreinte:
            return i, 1
    for i, v in enumerate(formes_verites):
        if equivalence_propositionnelle(forme, v):
            return i, 2
    return None


def retrouvee_empreinte_seule(forme, formes_verites: list):
    for i, v in enumerate(formes_verites):
        if forme.empreinte == v.empreinte:
            return i
    return None
