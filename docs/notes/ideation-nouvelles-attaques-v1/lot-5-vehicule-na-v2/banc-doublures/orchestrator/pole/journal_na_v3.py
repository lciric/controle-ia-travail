"""DOUBLURE D'ESSAI du module `journal_na_v3` (lot 3 v3), déclarée comme telle — ce n'est PAS le module du lot 3.

Seul le nom que lit `portier_na_v1` à l'import. Les essais du lot 5 v2 doivent être rejoués sur une copie où le lot 3 v3
est posé.
"""

import dataclasses


@dataclasses.dataclass(frozen=True)
class RenduRefusEcrit:
    sorte: str
