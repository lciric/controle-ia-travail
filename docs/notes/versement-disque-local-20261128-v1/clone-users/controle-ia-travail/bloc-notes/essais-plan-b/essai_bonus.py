import sys
sys.path.insert(0, "tests")
from controle_ia.environnements import juges
vrai = juges.charger_invite
juges.charger_invite = lambda i, *a, **k: ("## Scoring Rubric\nSPECIFICITY: <score>\nCOHERENCE: <score>\n" if i == "H4" else vrai(i, *a, **k))
import test_plan_b_juges_simplifies as T
from controle_ia.environnements.pilote_a import noter_ensembles
for bonus in (2.0, 2.5, 3.0):
    m = T.modele_qui_s_arrete(bonus=bonus)
    dem = [dict(d, variante="b0") for d in T.DEMANDES]
    a = noter_ensembles(m, T.FMT, dem, T.GRAINES, 2, 10, 1.0)
    print(bonus, [(x["tronquee"], x["jetons_reponse"], x["jetons_contexte"]) for x in a])
