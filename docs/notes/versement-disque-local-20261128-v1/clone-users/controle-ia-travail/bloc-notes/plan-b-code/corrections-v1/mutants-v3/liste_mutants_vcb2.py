"""Mutants rejoués par les corrections VCB2 (rédacteur des corrections, non vérificateur).
(1) Les 35 mutants nommés par la vérification des corrections VCB, tels quels : copie exacte de sa liste
`liste_mutants_v3.py` (sha256 615df4b2…), elle-même bâtie sur la liste recopiée `liste_mutants_verification.py`
(sha256 5747332534241b99…) : RQ-17, VCB-M01 (tel quel ; son ancien texte a disparu avant ces corrections) et son port
VCB-M01p, VCB-M02 à VCB-M19, VCB2-M01 à VCB2-M14.
(2) Mutants neufs contre la garde ajoutée au lecteur pour le point ouvert VCB-b (`max_nouveaux_juge`).
Forme : identifiant, module, ancien texte (une seule occurrence exigée), nouveau texte, tests ciblés, ce qu'il simule."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from liste_mutants_v3 import MUTANTS as M3  # noqa: E402
from liste_mutants_verification import LR, T_LR  # noqa: E402

_PLAFOND = "    if isinstance(plafond, bool) or not isinstance(plafond, int) or plafond < 1:"
MUTANTS = list(M3) + [
    ("VCBb-M01", LR, '    plafond = _champ(c, "max_nouveaux_juge", "configuration de l\'étape")',
     '    plafond = c.get("max_nouveaux_juge", 1)', T_LR,
     "lecteur : max_nouveaux_juge absent accepté (garde de présence retirée)"),
    ("VCBb-M02", LR, _PLAFOND, _PLAFOND.replace("plafond < 1", "plafond < 0"), T_LR,
     "lecteur : max_nouveaux_juge nul accepté"),
    ("VCBb-M03", LR, _PLAFOND, "    if plafond is None:", T_LR,
     "lecteur : max_nouveaux_juge d'une autre forme qu'un entier accepté"),
]
