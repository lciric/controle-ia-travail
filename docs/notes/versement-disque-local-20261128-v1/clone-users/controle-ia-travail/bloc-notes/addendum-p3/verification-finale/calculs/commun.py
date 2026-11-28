"""Outils communs de la vérification « calculs refaits et verrou par propriétés » (VF3) : chemins, import du module
copié, construction d'un petit run synthétique varié (aides des tests du module), lecture décisive par le code gelé."""
import copy
import json
import os
import sys

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
COPIE = os.path.join(ICI, "copie")
DEPOT = "/home/user/controle-ia-travail"
for _d in (os.path.join(DEPOT, "src"), os.path.join(DEPOT, "tests"), COPIE):
    if _d not in sys.path:
        sys.path.insert(0, _d)

import numpy as np  # noqa: E402

import complements_p3_v1 as cp  # noqa: E402
import test_complements_p3_v1 as tc  # noqa: E402  (aides des tests du module : _texte, _varier, _complet, …)
from test_premier_test_ia_lecture import P, _graines, _source  # noqa: E402

from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.premier_test_ia.conditions import CHAMPS_BORNES  # noqa: E402

SEPS = (" ", " ", " ", " ")


def ecrire_varie(i, c, cout, bizarres=None):
    """Textes variés : milliers séparés par les quatre espaces, décimales, suffixe k, « 3 500-hour blocks », virgule,
    champ du coût en double (divergence A5), action sans ligne ACTION (invalide) ; `bizarres` : conditions qui les
    écrivent (toutes par défaut)."""
    if bizarres is not None and c not in bizarres:
        return tc._texte(c, repr(cout))
    k = i % 23
    n = int(round(cout * 100))
    if k == 0:
        txt = f"{n:,}".replace(",", SEPS[(i // 23) % 4])
    elif k == 5:
        txt = f"{max(n // 1000, 1)} {n % 1000:03d}k"
    elif k == 9:
        txt = "3 500-hour blocks"
    elif k == 13:
        txt = f"{n:,}"
    elif k == 17:
        txt = f"{n:,}.5".replace(",", " ")
    else:
        txt = repr(cout)
    t = tc._texte(c, txt)
    if i % 31 == 0:
        t = t.replace(f"COST: {txt}", f"**COST:**\nCOST: {txt}")
    if i % 37 == 0:
        t = t.replace("ACTION: ADD\n", "")
    return t


def run_synthetique(graine=0, n_taches=14, n_pl=12, bizarres=None, **kw):
    """Petit run varié : bornes (champ du coût plus long que le pré-coût, absent, c = 1, bornes égales, illisibles),
    longueurs d'action (actions courtes de 1 à 3 jetons), actions non notées, textes variés."""
    src = tc._varier(_source(graine, n_taches=n_taches, n_pl=n_pl, **kw), graine=graine + 5)
    t, j = src["tables"], src["jetons"]
    rng = np.random.default_rng(1000 + graine)
    n = j["rang"].size
    j["bornes"] = j["bornes"].copy()
    j["longueur"] = j["longueur"].copy()
    j["bornes_lisibles"] = j["bornes_lisibles"].copy()
    ic = CHAMPS_BORNES.index("COST")
    for r in range(n):
        u = rng.random()
        if u < 0.10:
            j["bornes"][r] = [0, 1, 2, 3, 25]               # L_coût = 22 > c = 3
        elif u < 0.14:
            j["bornes"][r, ic] = -1                         # champ du coût absent
        elif u < 0.17:
            j["bornes_lisibles"][r] = False
        elif u < 0.20:
            j["bornes"][r] = [-1, 0, -1, 1, 6]              # c = 1, L = 1
        elif u < 0.22:
            j["bornes"][r] = [0, 5, 12, 20, 20]             # borne égale : fin = longueur
        elif u < 0.25:
            j["longueur"][r] = int(rng.integers(1, 4))      # action courte (1 à 3 jetons)
        elif u < 0.28:
            j["bornes"][r] = [2, 5, 12, 20, 24]             # premier champ après le début (segment « avant »)
    tc._recalculer_scores(src)
    src = tc._complet(src, lambda i, c, cout: ecrire_varie(i, c, cout, bizarres))
    non_notees = rng.choice(t["condition"].size, size=6, replace=False)
    t["scores"][non_notees, 5] = np.nan
    return src


def lecture_decisive(src):
    """Lecture décisive par le code gelé, aux constantes gelées (2 000 et 10 000 tirages), sérialisée comme sur disque."""
    assert lp.TIRAGES_AIRE == 2000 and lp.TIRAGES_COUT == 10000
    return json.loads(json.dumps(lp.lire(copy.deepcopy(src), _graines())))
