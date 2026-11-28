"""VF3 : précision 17 (« seuls les contrôles non faits deviennent « non lus » »). Entrée A1 dont tous les contrôles sont
faits, puis une `GardeArret` hors d'un calcul (permutation du placebo, descriptif seulement), simulée dans ce processus
seulement (le code gelé n'est pas modifié sur disque) : contrôles rendus, réserves et recommandation."""
import copy
import json

import verrou_proprietes as vp
from commun import P, cp, lp
from controle_ia.gardes import GardeArret

G = vp.graines(cp.cles_addendum(P), cp.ENTROPIE_P3)
cp.TIRAGES_AIRE, cp.TIRAGES_COUT = 60, 500
src = vp.base_scenarios()["sain"]()
lec = vp.recalculer(vp.lecture_reduite(src))
D = cp.preparer_donnees(src, lec, G)
sain = cp._executer_entree("A1", P[0], D, G)
print("établies :", D["etablies"])
print("contrôles A1 sains :", [(c["test"], c["cible"], c["controle_contraire"]) for c in sain["controles"]])
vrai = lp._permuter_dans_les_taches
lp._permuter_dans_les_taches = lambda *a: (_ for _ in ()).throw(GardeArret("échec simulé après tous les contrôles"))
x = cp._executer_entree("A1", P[0], D, G)
lp._permuter_dans_les_taches = vrai
n = len(sain["controles"])
print("contrôles faits gardés :", x["controles"][:n] == sain["controles"])
print("contrôles ajoutés :", [(c["test"], c["cible"], c["controle_contraire"], c.get("reserve")) for c in x["controles"][n:]])
vides = {a: ({"etat": "calculé", "controles": []} if a in cp.SANS_SONDE else
             {p: (x if (a, p) == ("A1", P[0]) else {"etat": "calculé", "controles": []}) for p in P}) for a in cp.ANALYSES}
s = cp.synthese(vides, D["etablies"], False)
print("recommandation :", json.dumps(s["recommandation_au_verdict_R13"], ensure_ascii=False, indent=1))
