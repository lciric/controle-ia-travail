"""Mutations du code de la passe (copie hors du dépôt) : les essais du cas sain doivent les attraper.
MUTATION choisie par la variable d'environnement CL_MUTATION. Rien n'est écrit dans le dépôt."""
import importlib.util
import os
import sys
from pathlib import Path

import controle_ia.barreau8_moniteurs as paquet

SOURCE = Path("/home/user/controle-ia-travail/src/controle_ia/barreau8_moniteurs/passe_recalcul_v2.py")
MUT = os.environ.get("CL_MUTATION", "aucune")
texte = SOURCE.read_text(encoding="utf-8")
REMPLACEMENTS = {
    "position": ("        debut = L - len(a.ids)\n", "        debut = L - len(a.ids) - 1\n"),
    "couche": ("self.blocs[c].register_forward_hook(self._crochet(c))", "self.blocs[c - 1].register_forward_hook(self._crochet(c))"),
    "lot": ("    for r, a in enumerate(lot):\n        debut", "    for r, a in enumerate(list(reversed(lot))):\n        debut"),
}
if MUT != "aucune":
    avant, apres = REMPLACEMENTS[MUT]
    assert texte.count(avant) == 1, MUT
    texte = texte.replace(avant, apres)
nom = "controle_ia.barreau8_moniteurs.passe_recalcul_v2"
spec = importlib.util.spec_from_file_location(nom, SOURCE, submodule_search_locations=None)
module = importlib.util.module_from_spec(spec)
sys.modules[nom] = module
exec(compile(texte, str(SOURCE), "exec"), module.__dict__)
paquet.passe_recalcul_v2 = module

sys.path.insert(0, "/home/user/controle-ia-travail/tests")
from test_barreau8_moniteurs_passe_v2 import (monde, saine,  # noqa: E402,F401
                                              test_cas_sain_couche_contexte_et_adaptateur_contre_la_passe_unique_du_harnais,
                                              test_cas_sain_scores_recalcules_sur_processeur_par_le_harnais)
