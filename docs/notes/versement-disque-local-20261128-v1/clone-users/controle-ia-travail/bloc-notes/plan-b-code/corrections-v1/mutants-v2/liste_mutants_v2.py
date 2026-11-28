"""Mutants rejoués après les corrections VCB : les survivants nommés par la vérification des corrections (RQ-17,
VCB-M01 à VCB-M03, VCB-M11 à VCB-M17), tels quels (même substitution, mêmes tests ciblés : copie exacte de sa liste,
`liste_mutants_verification.py`, sha256 5747332534241b99…) ; VCB-M01 porté sur le code corrigé (son ancien texte a
disparu : `lot_juge` est désormais exigé par `exiger_config_de_l_etape`) ; un témoin positif tué par la vérification
(VCB-M04) ; deux mutants neufs contre les deux gardes changées par ces corrections (VCB-M18, VCB-M19).
Forme : identifiant, module, ancien texte (une seule occurrence exigée), nouveau texte, tests ciblés, ce qu'il simule."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from liste_mutants_verification import LR, MUTANTS as MUTANTS_VERIFICATION, RQ, T_LR, T_RQ  # noqa: E402

SURVIVANTS = ("RQ-17", "VCB-M02", "VCB-M03", "VCB-M11", "VCB-M12", "VCB-M13", "VCB-M14", "VCB-M15", "VCB-M16",
              "VCB-M17")
TEMOIN_POSITIF = ("VCB-M04",)
_par_id = {m[0]: m for m in MUTANTS_VERIFICATION}
MUTANTS = [_par_id[i] for i in SURVIVANTS + TEMOIN_POSITIF] + [
    # VCB-M01 porté : même défaut (lot_juge absent de la configuration du run accepté, 8 par défaut), à sa place neuve
    ("VCB-M01p", LR, '    lot = _champ(c, "lot_juge", "configuration de l\'étape")', '    lot = c.get("lot_juge", 8)',
     T_LR, "lecteur : lot_juge absent de la configuration du run accepté (8 par défaut) (porté)"),
    # neufs : les deux gardes changées par les corrections VCB
    ("VCB-M18", RQ, '    for nom, rx in list(CITATIONS.items()) + [("commit du code d\'analyse", COMMIT_CITE)]:',
     "    for nom, rx in CITATIONS.items():", T_RQ,
     "lanceur : commit du code cité deux fois, avec deux valeurs, accepté (seule la première lue)"),
    ("VCB-M19", LR, "    if isinstance(lot, bool) or not isinstance(lot, int) or lot < 1:", "    if lot is None:", T_LR,
     "lecteur : lot_juge présent mais non entier positif accepté"),
]
