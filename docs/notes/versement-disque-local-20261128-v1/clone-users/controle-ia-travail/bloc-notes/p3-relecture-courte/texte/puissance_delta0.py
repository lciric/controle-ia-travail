# Rejoue la section 1 de docs/notes/P3-mesures-v2/puissance_p3.py (mêmes graines), n'imprime que des nombres (aucun texte).
import json, sys
from itertools import combinations
from pathlib import Path
import numpy as np
from controle_ia.environnements.propositions import heures_declarees, lire_action
from controle_ia.premier_test_ia.statistiques import effet_cout_apparie
racine = np.random.SeedSequence(20261017)
graines = iter(racine.spawn(200))
fiches = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))["resultat"]["fiches"]
par_tache = {}
for f in fiches:
    couts = [heures_declarees(lire_action(a["texte"]).champs.get("COST")) for a in f["actions"]]
    par_tache.setdefault(f["tache"], []).append(couts)
taches = sorted(par_tache)
for delta in (0.0, 0.05):
    for i, j in combinations(range(3), 2):
        hon = {t: par_tache[t][i] for t in taches if len(par_tache[t]) == 3}
        sab = {t: [None if c is None else c * 10 ** delta for c in par_tache[t][j]] for t in hon}
        r = effet_cout_apparie(sab, hon, np.random.default_rng(next(graines)), 10_000, 0.95)
        print(f"delta {delta} e{j}-e{i} effet {r['effet']:+.6f} bas {r['bas']:+.6f} haut {r['haut']:+.6f}")
